# -*- coding: utf-8 -*-
"""Post-generation LaTeX checker/fixer for inline $...$ math, per core/solutions/LATEX_REFERENCE.md.

Unlike latex_convert.py (which builds $...$ delimiters from plain text), this module scans text
that ALREADY has $...$ in place - whether produced by latex_convert.latex_wrap(), or authored
directly by a human/agent per LATEX_REFERENCE.md's rules (the normal path for solutions.json's
question_tex/given/find/method/steps/answer_tex fields) - and catches mistakes either one can
still make: an exponent swallowing a fraction that belongs to the whole term, a LaTeX command
glued to the next letter, a lone parenthesis wrapped on its own, a doubled \\text{\\text{}}, a
roman-numeral label split across math/text mode, or an unbalanced $ count.

Design: fix what is UNAMBIGUOUSLY wrong (changes the rendered value, or is invalid/ugly LaTeX no
matter the context); flag what is AMBIGUOUS (a bare unit letter that might be a variable, the same
letter wrapped in some places and bare in others) for a human to resolve, rather than guessing -
guessing has a real history of introducing new regressions in this exact module's sibling.

CLI usage: `python -B latex_checker.py <plan.json> [--write]` walks every concept's content block's
text/publication_text field, reports every issue found (grouped by concept_id), and only rewrites
the file if --write is passed and at least one AUTO-FIXABLE issue was found (flag-only issues are
reported but never change the file).
"""
from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field


@dataclass
class Issue:
    kind: str
    message: str
    excerpt: str
    fixable: bool
    fixed: bool = False


# ---------------------------------------------------------------------------------------------
# auto-fixable: unambiguously wrong, safe to rewrite without a human in the loop
# ---------------------------------------------------------------------------------------------

_EXP_BASE = r"(?:\([^()]*\)|[0-9A-Za-z]+)"
_EXP_FRAC_RE = re.compile(r"(?<![\\^])(%s)\^(\d+)/(\d+)(?![\w(])" % _EXP_BASE)
# the SAME bug, already one step further along: someone (or some other converter) already turned
# the "/" into a \frac, but left it sitting as the caret's argument - "a^\frac{2}{4}" means the
# same wrong a^(2/4) as "a^2/4" did, just spelled with \frac instead of a bare slash.
_EXP_FRAC_CMD_RE = re.compile(r"(?<![\\^])(%s)\^\\frac\{(\d+)\}\{(\d+)\}" % _EXP_BASE)


def _fix_exponent_fraction(math, issues):
    """"a^2/4" means (a^2)/4 here (a fraction OF an already-squared term) - never a^(2/4). Left
    alone, '^' in real LaTeX binds to the single token after it, so a bare \\frac{2}{4} sitting
    right after '^' becomes the WHOLE exponent: a^(2/4) = a^0.5 = sqrt(a), a different number."""
    def repl(m):
        base, exp, den = m.groups()
        issues.append(Issue(
            "exponent_fraction",
            "'%s^%s/%s' reads as %s^(%s/%s) in real LaTeX (the exponent swallows the whole "
            "fraction), not the intended (%s^%s)/%s" % (base, exp, den, base, exp, den, base, exp, den),
            m.group(0), True, True))
        return r"\frac{%s^%s}{%s}" % (base, exp, den)
    math = _EXP_FRAC_RE.sub(repl, math)
    math = _EXP_FRAC_CMD_RE.sub(repl, math)
    return math


# A plain "\\[a-zA-Z]+(?=[A-Za-z])" cannot tell "command ends here, an unrelated letter follows"
# apart from "greedy match stopped one letter short of the command's OWN name, which continues
# right here" - "\frac{2}{4}" would backtrack from "\frac" down to "\fra" purely because "c" (the
# command's own next letter) happens to satisfy the lookahead, corrupting it into "\fra c{2}{4}".
# Matching against the FIXED vocabulary of command names this pipeline actually emits sidesteps
# that ambiguity entirely: a name is either whole and in the list, or it isn't a match at all.
_KNOWN_COMMANDS = (
    "frac", "text", "sqrt", "triangle", "angle", "theta", "alpha", "beta", "phi", "pi",
    "times", "div", "approx", "neq", "ne", "leq", "le", "geq", "ge", "circ", "pm", "mp",
    "cdot", "cdots", "ldots", "sin", "cos", "tan", "cot", "sec", "csc", "log", "ln", "lim",
    "gcd", "lcm",
)
_GLUED_CMD_RE = re.compile(r"\\(%s)(?=[A-Za-z])" % "|".join(
    sorted(_KNOWN_COMMANDS, key=len, reverse=True)))


def _fix_glued_command(math, issues):
    def repl(m):
        cmd = "\\" + m.group(1)
        tail = math[m.end():m.end() + 3]
        issues.append(Issue("glued_command",
                             "LaTeX command runs straight into the next letter: '%s%s...'"
                             % (cmd, tail), cmd, True, True))
        return cmd + " "
    return _GLUED_CMD_RE.sub(repl, math)


_DOUBLE_TEXT_RE = re.compile(r"\\text\{\s*\\text\{([^{}]*)\}\s*\}")


def _fix_double_text(math, issues):
    def repl(m):
        issues.append(Issue("double_text", "doubled \\text{\\text{...}}", m.group(0), True, True))
        return r"\text{%s}" % m.group(1)
    return _DOUBLE_TEXT_RE.sub(repl, math)


def _fix_lone_paren_span(math, issues):
    """A $...$ span holding nothing but "(" and/or ")" is never meaningful on its own - it is the
    stray edge of a plain-text parenthetical a converter (or a person) mis-split. Returns the
    span's own text (for the caller to emit outside the dollars) and whether it changed."""
    if math and not math.strip("()"):
        issues.append(Issue("lone_paren_span",
                             "a whole $...$ span is just parenthesis characters, no real math: '$%s$'"
                             % math, math, True, True))
        return math, True
    return math, False


_ROMAN = r"(?:i|ii|iii|iv|v|vi|vii|viii|ix|x|xi|xii|xiii|xiv|xv)"
_SPLIT_LABEL_RES = [
    re.compile(r"\$\(\$(%s)\$\)\$" % _ROMAN, re.IGNORECASE),  # "$($iii$)$"
    re.compile(r"\$\((%s)\$\)" % _ROMAN, re.IGNORECASE),       # "$(iii$)"
    re.compile(r"\$(%s)\$\)" % _ROMAN, re.IGNORECASE),         # "$iii$)"  (open paren already bare)
]


def _fix_split_label(text, issues):
    def repl(m):
        issues.append(Issue("split_label", "roman-numeral part-label split across math/text mode",
                             m.group(0), True, True))
        return "(%s)" % m.group(1)
    for pat in _SPLIT_LABEL_RES:
        text = pat.sub(repl, text)
    return text


def _apply_math_fixes(math, issues):
    math = _fix_exponent_fraction(math, issues)
    math = _fix_glued_command(math, issues)
    math = _fix_double_text(math, issues)
    math, changed = _fix_lone_paren_span(math, issues)
    return math


_MATH_SPAN_RE = re.compile(r"\$(.*?)\$")


def _fix_math_spans(text, issues):
    """Run the per-span fixes on the content of every $...$ in text, leaving everything outside
    the dollars (ordinary prose) untouched. A span fixed down to a lone paren is emitted WITHOUT
    its dollars (literal "(" / ")"), everything else keeps its dollars."""
    def repl(m):
        original = m.group(1)
        fixed = _apply_math_fixes(original, issues)
        if fixed and not fixed.strip("()"):
            return fixed
        return "$%s$" % fixed
    return _MATH_SPAN_RE.sub(repl, text)


# ---------------------------------------------------------------------------------------------
# flag-only: ambiguous, reported for a human to resolve, never auto-fixed
# ---------------------------------------------------------------------------------------------

_BARE_UNIT_LETTERS = {"m", "s", "g", "l", "t"}  # also common variable names - never auto-wrap
_BARE_UNIT_RE = re.compile(
    r"\$[^$]*?(?<=[0-9.])\s(%s)\b[^$]*\$" % "|".join(_BARE_UNIT_LETTERS)
)


def _flag_bare_unit_letter(text, issues):
    for m in _MATH_SPAN_RE.finditer(text):
        math = m.group(1)
        mm = re.search(r"(?<=[0-9.])\s(%s)\b(?!\w)" % "|".join(_BARE_UNIT_LETTERS), math)
        if mm:
            issues.append(Issue(
                "bare_unit_letter",
                "'%s' after a number, not wrapped in \\text{} - confirm by hand whether it's a "
                "unit (should be \\text{ %s}) or a genuine variable named '%s'"
                % (mm.group(1), mm.group(1), mm.group(1)),
                "$%s$" % math, False))


_SPLIT_WORD_UNIT_RE = re.compile(r"(?<=[a-z])[a-z]\$?\\text\{\s*[a-z]+\}")


def _flag_split_word_unit(text, issues):
    """A variable glued straight to \\text{units} ("a\\text{ units}") is correct output - but if
    the letter right before \\text{} is itself preceded by ANOTHER letter (mid-word, not a
    standalone single-letter token), a word got cut in half instead: "trapeziu\\text{ m}" is not
    "the variable u, units m" - it's "trapezium" with the last two letters torn apart."""
    for m in _SPLIT_WORD_UNIT_RE.finditer(text):
        issues.append(Issue("split_word_unit",
                             "a letter sits directly against \\text{} with no number in between "
                             "- likely a word split in half: '...%s...'" % m.group(0),
                             m.group(0), False))


_WRAPPED_LETTER_RE = re.compile(r"\$([a-zA-Z])\$")
# excludes a letter preceded by an apostrophe: "Heron's" must not read as the bare variable s.
_BARE_LETTER_RE = re.compile(r"(?<![\w$\\'’])([a-zA-Z])(?![\w$])")
_COMMON_WORDS_1_2 = {
    "a", "i", "is", "it", "in", "on", "of", "to", "or", "as", "be", "by", "we", "he", "so", "if",
    "no", "do", "am", "us", "an", "at", "up",
}


def _flag_inconsistent_wrapping(text, issues):
    """The SAME letter appearing both wrapped ($a$) and bare (a) as a standalone token across one
    text field is a strong sign of a missed wrap, not a deliberate choice - LATEX_REFERENCE.md
    says every mathematical identifier should be wrapped consistently. Skips "a"/"i" (handled
    separately below, since they double as the English article/pronoun) and anything inside an
    existing $...$ span for the bare-token scan."""
    wrapped = {m.group(1) for m in _WRAPPED_LETTER_RE.finditer(text)}
    outside_dollars = _MATH_SPAN_RE.sub(" ", text)
    bare = set()
    for m in _BARE_LETTER_RE.finditer(outside_dollars):
        low = m.group(1).lower()
        if low not in _COMMON_WORDS_1_2 or low in ("a",):
            bare.add(m.group(1))
    both = (wrapped & bare) - {"a", "A", "i", "I"}
    for letter in sorted(both):
        issues.append(Issue(
            "inconsistent_wrapping",
            "'%s' appears both as $%s$ and bare elsewhere in the same text - check whether the "
            "bare one(s) should also be $%s$" % (letter, letter, letter),
            letter, False))


_UNBALANCED_DOLLAR_RE = None  # computed per-text via a simple count, not a regex


def _flag_unbalanced_dollars(text, issues):
    if text.count("$") % 2 != 0:
        issues.append(Issue("unbalanced_dollars",
                             "odd number of '$' - a math span is unterminated", text[:120], False))


# ---------------------------------------------------------------------------------------------
# public API
# ---------------------------------------------------------------------------------------------

def check(text):
    """Return every issue found in text (fixable and flag-only), without changing it."""
    if not text:
        return []
    issues = []
    _fix_math_spans(text, issues)  # run for its side-effect of recording issues; discard the text
    _flag_bare_unit_letter(text, issues)
    _flag_split_word_unit(text, issues)
    _flag_inconsistent_wrapping(text, issues)
    _flag_unbalanced_dollars(text, issues)
    return issues


def fix(text):
    """Return (new_text, issues). Only the auto-fixable issues change new_text; flag-only issues
    are still reported but text passes through unchanged for those spots."""
    if not text:
        return text, []
    issues = []
    new_text = _fix_math_spans(text, issues)
    _flag_bare_unit_letter(new_text, issues)
    _flag_split_word_unit(new_text, issues)
    _flag_inconsistent_wrapping(new_text, issues)
    _flag_unbalanced_dollars(new_text, issues)
    return new_text, issues


# ---------------------------------------------------------------------------------------------
# CLI: walk a whole learning-plan JSON's content blocks
# ---------------------------------------------------------------------------------------------

_TEXT_FIELDS = ("text", "publication_text")


def _iter_concepts(plan):
    for m in plan.get("modules", []):
        for s in m.get("segments", []):
            for t in s.get("topics", []):
                for c in t.get("concepts", []):
                    yield c


def _run_cli(path, write):
    with open(path, encoding="utf-8") as f:
        plan = json.load(f)

    total_issues = 0
    total_fixed = 0
    for c in _iter_concepts(plan):
        for b in c.get("content", []):
            for field_name in _TEXT_FIELDS:
                if not b.get(field_name):
                    continue
                new_text, issues = fix(b[field_name])
                if not issues:
                    continue
                print("== %s (%s / %s) ==" % (c["concept_id"], c.get("concept_name", ""), field_name))
                for issue in issues:
                    tag = "FIXED" if issue.fixed else ("fixable" if issue.fixable else "FLAG")
                    print("  [%s] %s: %s" % (tag, issue.kind, issue.message))
                total_issues += len(issues)
                total_fixed += sum(1 for i in issues if i.fixed)
                if write:
                    b[field_name] = new_text

    print()
    print("Total issues: %d (%d auto-fixed, %d flagged for review)"
          % (total_issues, total_fixed, total_issues - total_fixed))

    if write and total_fixed:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(plan, f, ensure_ascii=False, indent=1)
        print("Wrote fixes back to", path)
    elif write:
        print("Nothing auto-fixable found - file left unchanged.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python -B latex_checker.py <plan.json> [--write]")
        sys.exit(1)
    _run_cli(sys.argv[1], "--write" in sys.argv)
