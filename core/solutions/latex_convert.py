# -*- coding: utf-8 -*-
"""Plain text -> strict inline LaTeX, per core/solutions/LATEX_REFERENCE.md (sections 11-12):
every number, variable, operator and step index gets wrapped in its own `$...$` or merged into one
coherent equation span; units go inside `\\text{}`; fractions become `\\frac{a}{b}`; punctuation
(commas, periods, colons) and ordinary prose stay OUTSIDE the dollars.

Algorithm: classify the text into MATH / PROSE / break tokens, then merge consecutive MATH tokens
(and the whitespace between them) into one `$...$` span, closing the span at any prose word or
sentence punctuation. This single rule reproduces both the "$N$." step-number convention and
whole-equation wrapping with no special-casing - verified against LATEX_REFERENCE.md's own two
worked examples in `latex_wrap.__doc__`'s sibling self-test (see bottom of this file).
"""
from __future__ import annotations

import re

_GREEK_WORD = {"pi": r"\pi", "theta": r"\theta", "alpha": r"\alpha", "beta": r"\beta", "phi": r"\phi"}
_GREEK_UNI = {"π": r"\pi", "θ": r"\theta", "α": r"\alpha", "β": r"\beta", "φ": r"\phi"}
_SUB_DIGITS = "₀₁₂₃₄₅₆₇₈₉"
_SUP_DIGITS = "⁰¹²³⁴⁵⁶⁷⁸⁹"
_MATH_FUNC_WORDS = {"sin", "cos", "tan", "cot", "sec", "csc", "log", "ln", "lim", "gcd", "lcm"}
_STOPWORDS = {
    "is", "it", "in", "on", "of", "to", "or", "as", "be", "by", "we", "he", "so", "if", "no", "do", "am", "us", "an",
    "at", "up", "go", "rs",
    "the", "and", "for", "are", "not", "all", "its", "this", "that", "with", "from", "then", "than", "such", "both",
    "let", "has", "have", "can", "will", "each", "every", "find", "answer", "given",
}

# ---------------------------------------------------------------------------------------------
# Phase 1: normalize unicode/shorthand math notation into canonical LaTeX source (no $ yet)
# ---------------------------------------------------------------------------------------------


def _convert_sqrt(s):
    """unicode sqrt -> \\sqrt{...}: sqrt(...) takes the matching-paren group; sqrt128 (no parens)
    takes the next maximal alnum run."""
    out, i, n = [], 0, len(s)
    while i < n:
        if s[i] == "√":
            j = i + 1
            if j < n and s[j] == "(":
                depth, k = 1, j + 1
                while k < n and depth:
                    if s[k] == "(":
                        depth += 1
                    elif s[k] == ")":
                        depth -= 1
                    k += 1
                inner = _fix_exponent_fraction(s[j + 1:k - 1])
                out.append(r"\sqrt{%s}" % _convert_fractions(inner))
                i = k
            else:
                m = re.match(r"[0-9A-Za-z]+(?:\.\d+)?", s[j:])
                if m:
                    out.append(r"\sqrt{%s}" % m.group(0))
                    i = j + m.end()
                else:
                    out.append("√")
                    i += 1
        else:
            out.append(s[i])
            i += 1
    return "".join(out)


_FRAC_SHORT_STOP = r"(?:is|it|in|on|of|to|or|as|be|by|we|he|so|if|no|do|am|us|an|at|up)\b"
# a digit-led token (44, 44r, 3.5) or a bracketed group - these glue into a chain with NO separator
# needed ("2(A + C)(B + C)"), so the '+' below is safe: each repetition still starts at a digit/"(".
_FRAC_GLUE_FACTOR = r"(?:\([^()]*\)|[0-9][0-9A-Za-z]*(?:\.\d+)?)"
# a standalone short variable (not repeated!) - "[A-Za-z]{1,2}" repeated via '+' would silently
# reassemble ANY word out of 1-2 letter chunks ("using" -> "us"+"in"+"g"); the trailing (?!\w) forces
# the match to end exactly at a word boundary, so a real multi-letter word can never match at all.
_FRAC_VAR = r"(?:(?!%s)[A-Za-z]{1,2}(?!\w))" % _FRAC_SHORT_STOP
_FRAC_FACTOR_CHAIN = r"(?:%s+|%s)" % (_FRAC_GLUE_FACTOR, _FRAC_VAR)
# operator/relation commands never belong INSIDE a fraction's numerator or denominator as their own
# "factor" - without this exclusion, the multi-unit rule below would let "2 \times 22" (coefficient,
# operator, unrelated number) bridge across the operator and get treated as one combined numerator.
_FRAC_NOT_CMD = r"(?:times|div|pm|mp|cdot|approx|neq|ne|leq|le|geq|ge|circ|cdots|ldots)\b"
_FRAC_CMD = r"\\(?!%s)[a-zA-Z]+(?:\{[^{}]*\})*" % _FRAC_NOT_CMD
_FRAC_UNIT = (
    r"(?:[0-9A-Za-z]+(?:\.\d+)?%s"  # a coefficient glued to a command: 3\sqrt{3}, 4\pi
    r"|%s|%s)" % (_FRAC_CMD, _FRAC_CMD, _FRAC_FACTOR_CHAIN)  # bare command, or a factor chain
)
# a CONTINUATION unit (after the first, space-joined) must be a command or a short variable only -
# never a bracketed group. Without this, "1/2 (a + a + a)" would let "(a + a + a)" glue onto the
# "2" as a second space-joined unit, turning \frac{1}{2}\,(a+a+a) (half, times the group) into the
# wrong \frac{1}{2 (a + a + a)} (one over the whole product) - a different number, not just a style
# difference. A bracketed group may still START a token (glued with no space, "2(A+C)(B+C)"), just
# never continue one after a space.
_FRAC_CONT_UNIT = r"(?:%s|%s)" % (_FRAC_CMD, _FRAC_VAR)
_FRAC_NUMERATOR = r"(?:%s(?: %s){0,2})" % (_FRAC_UNIT, _FRAC_CONT_UNIT)  # "4\pi r": coefficient+command+var
# the DENOMINATOR never continues past a space, even into a short variable: "1/2 ah" is (1/2)*(ah),
# not 1/(2ah), and "1/2 wh" is (1/2)*(wh), not 1/(2wh) - a space after a simple a/b fraction starts a
# separate multiplied term, it never widens the denominator itself.
_FRAC_RE = re.compile(r"(?<![\w)}\\])(%s)/(%s)(?![\w(])" % (_FRAC_NUMERATOR, _FRAC_UNIT))


def _strip_wrap(tok):
    return tok[1:-1] if tok[:1] == "(" and tok[-1:] == ")" else tok


def _looks_mathy(tok):
    """A numerator/denominator is only converted if it actually looks mathematical (has a digit or
    a LaTeX command, or is itself a short 1-2 letter variable name) - guards the space-joined,
    multi-word _FRAC_TOKEN above from firing on an ordinary English phrase like "and/or"."""
    stripped = _strip_wrap(tok)
    if re.search(r"[0-9\\]", stripped):
        return True
    return bool(re.fullmatch(r"[A-Za-z]{1,2}", stripped))


def _convert_fractions(s):
    """a/b -> \\frac{a}{b} for numeric/variable tokens (optionally one \\cmd{} or bracketed group,
    or up to 3 space-joined such units per side, e.g. "4\\pi r"); runs to a fixed point so a/b/c or
    a fraction nested in \\sqrt{} fully converts. Doesn't touch a slash without mathy content on
    either side (dates, "and/or")."""
    def repl(m):
        num, den = m.group(1), m.group(2)
        if not (_looks_mathy(num) or _looks_mathy(den)):
            return m.group(0)
        return r"\frac{%s}{%s}" % (_strip_wrap(num), _strip_wrap(den))
    prev = None
    while prev != s:
        prev = s
        s = _FRAC_RE.sub(repl, s)
    return s


_UNIT_RE = re.compile(
    r"(?<=[0-9A-Za-z\}])(\s?)((?:sq\.?\s*)?(?:units?|cm2|cm|mm|km|kg|m2|sec|min|hr))\b(?!\w)(?!\s*\\text)"
)
# bare "m" (metres) needs its OWN, much stricter rule, kept separate from the general unit regex
# above: that regex's lookbehind only requires "preceded by any alnum character", which is fine for
# multi-letter units (no English word coincidentally ends in "cm" or "mm") but catastrophic for a
# single letter - "trapezium", "from", "parallelogram", "sum" all end in "m" too, and the general
# rule would wrap the END OF THOSE WORDS as a unit ("trapeziu\text{ m}"). Requiring the character
# immediately before to be a DIGIT (not just alnum) is what actually distinguishes "6.3 m" from the
# tail of an ordinary word; confirmed "m" is never used as a variable anywhere in this corpus, only
# ever as a measurement directly after a number, so this is safe here - if a future chapter needs
# "m" as a variable, watch for it specifically (latex_checker.py's bare_unit_letter flag still
# catches a genuinely ambiguous case when this rule doesn't already decide it).
# "}" and ")" are included alongside digits: "1500\sqrt{3} m" ends the quantity on a closing
# brace, not a bare digit, but no English word ends in "}" or ")" either, so this stays just as
# safe against the "trapezium" false-positive while also covering that shape.
_BARE_M_RE = re.compile(r"(?<=[0-9\}\)])(\s)(m)\b(?!\w)(?!\s*\\text)")


def _convert_units(s):
    s = _UNIT_RE.sub(lambda m: r"\text{%s%s}" % (m.group(1) or " ", m.group(2)), s)
    s = _BARE_M_RE.sub(lambda m: r"\text{%s%s}" % m.groups(), s)
    return s


_EXP_BASE = r"(?:\([^()]*\)|[0-9A-Za-z]+)"
# (?<!\\): a base match must not start right after a backslash, or "4\pi^2r^2/12" would let the
# base-capture steal "pi" out of "\pi" (ignoring its backslash) instead of leaving \pi untouched.
# (?<!\^): nor right after a caret, or in that same "...\pi^2r^2/12" string the base-capture
# would instead start AT the "2" of the first exponent, greedily absorb the following "r" too
# ("2r"), and match "2r^2/12" as if "2r" were one base - two chained exponents, not one.
_EXP_FRAC_RE = re.compile(r"(?<![\\^])(%s)\^(\d+)/(\d+)(?![\w(])" % _EXP_BASE)


def _fix_exponent_fraction(s):
    """"a^2/4" (from plain "a2/4" or unicode "a²/4") means (a^2)/4 in this content - a fraction OF
    an already-squared term - never a^(2/4). This MUST run before _convert_fractions: left alone,
    the general a/b rule below would see the bare "2/4" sitting right after the "^" and convert
    just that into \\frac{2}{4}, leaving "a^\\frac{2}{4}" - and because '^' in real LaTeX binds to
    the single token after it, \\frac then grabs BOTH its own braces as that token's content, so
    the WHOLE fraction becomes the exponent: $a^{2/4}$ = $a^{0.5}$ = sqrt(a), a different number
    from the intended $\\frac{a^2}{4}$. Fixing the grouping first avoids that collision entirely."""
    return _EXP_FRAC_RE.sub(lambda m: r"\frac{%s^%s}{%s}" % m.groups(), s)


def _convert_symbols(s):
    for k, v in _GREEK_UNI.items():
        # a command name swallows any letter glued right after it ("\pi" + "r" -> the undefined
        # command "\pir"), so a trailing letter needs a separating space; anything else (space,
        # digit, operator, punctuation) already terminates the command name safely.
        s = re.sub(re.escape(k) + r"(?=[A-Za-z])", lambda m, v=v: v + " ", s)
        s = s.replace(k, v)
    s = re.sub(r"(?<![A-Za-z\\])(pi|theta|alpha|beta|phi)(?![A-Za-z])", lambda m: _GREEK_WORD[m.group(1)], s)
    s = re.sub(r"(?<![A-Za-z\\])sqrt(?![A-Za-z])", "√", s, flags=re.IGNORECASE)
    s = re.sub(r"\s*[×*]\s*", r" \\times ", s)
    s = re.sub(r"\s*÷\s*", r" \\div ", s)
    s = re.sub(r"\s*≈\s*", r" \\approx ", s)
    s = re.sub(r"\s*≠\s*", r" \\neq ", s)
    s = re.sub(r"\s*≤\s*", r" \\leq ", s)
    s = re.sub(r"\s*≥\s*", r" \\geq ", s)
    s = re.sub(r"\s*⊥\s*", r" \\perp ", s)
    s = s.replace("−", "-")
    s = re.sub(r"(\d)\s*°(?=[A-Za-z])", r"\1^\\circ ", s)
    s = re.sub(r"(\d)\s*°", r"\1^\\circ", s)
    s = re.sub(r"Δ\s*([A-Z][A-Za-z0-9]*)", r"\\triangle \1", s)
    s = re.sub(r"∠\s*([A-Z][A-Za-z0-9]*)", r"\\angle \1", s)
    for i, ch in enumerate(_SUP_DIGITS):
        s = re.sub(r"(?<=[0-9A-Za-z)}])" + ch, "^" + str(i), s)
    for i, ch in enumerate(_SUB_DIGITS):
        s = re.sub(r"(?<=[A-Za-z0-9)}])" + ch, "_" + str(i), s)
    s = _convert_sqrt(s)
    s = _fix_exponent_fraction(s)
    s = _convert_fractions(s)
    s = _convert_units(s)
    s = re.sub(r"[ \t]+", " ", s)
    return s


# ---------------------------------------------------------------------------------------------
# Phase 2: tokenize into MATH / PROSE / break, then merge consecutive MATH (+ interior spaces)
# into $...$ spans. Punctuation (. , ; :) always breaks a span and stays outside it.
# ---------------------------------------------------------------------------------------------


def _match_latex_cmd(s, i):
    """At s[i] == '\\', consume \\name plus any chain of balanced {..}/^{..}/_{..}/^x/_x groups."""
    m = re.match(r"\\[a-zA-Z]+", s[i:])
    if not m:
        return i
    j = i + m.end()
    n = len(s)
    while j < n:
        if s[j] == "{":
            depth, k = 1, j + 1
            while k < n and depth:
                if s[k] == "{":
                    depth += 1
                elif s[k] == "}":
                    depth -= 1
                k += 1
            j = k
        elif s[j] in "^_" and j + 1 < n and s[j + 1] == "{":
            depth, k = 1, j + 2
            while k < n and depth:
                if s[k] == "{":
                    depth += 1
                elif s[k] == "}":
                    depth -= 1
                k += 1
            j = k
        elif s[j] in "^_" and j + 1 < n and s[j + 1].isalnum():
            j += 2
        else:
            break
    return j


_ENUM_CUE_WORDS = {
    "side", "sides", "radii", "radius", "length", "lengths", "segment", "segments",
    "angle", "angles", "semicircle", "semicircles", "vertex", "vertices", "point", "points",
    "value", "values", "diagonal", "diagonals", "chord", "chords", "path", "paths",
    "base", "leg", "legs", "height", "heights",
}


def _a_enum_context(text, start, end):
    """True when a "list a quantity by letter" cue word ("sides", "radii", "semicircle", "Path", ...)
    names "a" as a variable - "the radii of semicircles a, b, c, d", "Semicircle a has length...",
    "(i) Path a is longer." But "the sides of a 10 cm square" and "the arc of a circle" use the very
    same cue words in ordinary prose with "a" as the plain article, so a nearby cue word is only
    trusted when it's the WORD RIGHT BEFORE "a" (no other noun/preposition between them, as in "the
    sides of a square" where "of" intervenes); a cue word a few words further back only counts if
    "a" is ALSO immediately followed by a comma, i.e. it is plainly continuing a list ("sides are a,
    so ...") rather than quantifying the next noun."""
    clause = re.split(r"[.;:]", text[:start])[-1]
    words = re.findall(r"[A-Za-z]+", clause.lower())
    if not words:
        return False
    if words[-1] in _ENUM_CUE_WORDS:
        return True
    k = end
    while k < len(text) and text[k] == " ":
        k += 1
    followed_by_comma = k < len(text) and text[k] == ","
    return followed_by_comma and any(w in _ENUM_CUE_WORDS for w in words[-5:])


def _word_before(text, pos):
    """The word (and its start index) ending right before `pos`, skipping one run of spaces -
    used to look one or two words back without re-deriving the same scan each time."""
    p = pos - 1
    while p >= 0 and text[p] == " ":
        p -= 1
    end_p = p + 1
    while p >= 0 and text[p].isalpha():
        p -= 1
    start_p = p + 1
    return text[start_p:end_p], start_p


def _is_a_mathy(text, start, end):
    """Disambiguate the lone word "a": a variable (math) next to an operator/digit, named right
    after a "list of labelled quantities" cue word, directly against a LaTeX command, paired with
    "by"/"and" in a dimension or list phrase, or an English article (prose) otherwise."""
    j = start - 1
    while j >= 0 and text[j] == " ":
        j -= 1
    prev = text[j] if j >= 0 else ""
    prev_word, prev_word_start = _word_before(text, start)
    k = end
    while k < len(text) and text[k] == " ":
        k += 1
    nxt = text[k] if k < len(text) else ""
    nxt_word_m = re.match(r"[A-Za-z]+", text[k:])
    nxt_word = nxt_word_m.group(0) if nxt_word_m else ""
    # a trailing prime mark, glued directly on with no space ("a'"), is never English - "a" cannot
    # take a possessive ('s) as an article, so a bare apostrophe right after it only ever means the
    # primed variable a', regardless of how far this is from the list that first introduced it.
    if text[end:end + 1] in ("'", "’"):
        return True
    # directly against a LaTeX command ("\times a", "a \times"): the command's own last/first
    # letter reads like plain prose to a single-character check, so this looks at the word itself.
    if (prev.isalpha() and prev_word_start > 0 and text[prev_word_start - 1] == "\\") or nxt == "\\":
        return True
    # "a by b": a dimension phrase - an article is never directly followed by the preposition
    # "by" (it always introduces a noun), so this is an unambiguous signal "a" is the variable.
    if nxt_word.lower() == "by":
        return True
    # "a by a square": the SECOND "a" is preceded by "by" instead, which by itself is NOT safe -
    # "divided by a factor" is ordinary prose with "a" as the article. The guard: a genuine
    # dimension phrase always has another short variable-like token (not a real verb) before "by"
    # too ("an A by a square", "p by a"); "divided"/"multiplied"/"bounded" are not short.
    if prev_word.lower() == "by":
        word_before_by, _ = _word_before(text, prev_word_start)
        if 1 <= len(word_before_by) <= 2:
            return True
    # "legs be a and b": an article is never directly followed by the conjunction "and" either.
    if nxt_word.lower() == "and":
        return True
    # NOT a comma in prev, and NOT a bare digit in nxt: ", a square" and "fill a 6r by 2r rectangle"
    # are far more often the English article "a" quantifying the next noun/measurement than a bare
    # list of single-letter variables - only an adjacent operator (no intervening punctuation or
    # quantified noun) is a strong enough signal that this "a" is itself a variable. A digit or a
    # closing "}" right before "a" is trusted only when GLUED on with no space ("2a", an implied-
    # multiplication coefficient; a bare "}a" group-then-variable) - spaced, either reads as ordinary
    # prose instead: "say 2 a child needs..." (the number ends one clause, "a" starts the article that
    # opens the next), and "...40 km a day" (a \text{} unit's closing brace, then "a" meaning "per",
    # not a variable - the single most common way this shape actually occurs, since \text{} is this
    # converter's own unit wrapping, always followed by ordinary prose, never a glued variable).
    prev_glued = text[start - 1] if start > 0 else ""
    return (prev in "=+-*/^_()" or prev_glued in "}" or prev_glued.isdigit() or nxt in "=+-*/^_(){}"
            or _a_enum_context(text, start, end))


_ROMAN = r"(?:i|ii|iii|iv|v|vi|vii|viii|ix|x|xi|xii|xiii|xiv|xv)"
_LABEL_RE = re.compile(r"\(" + _ROMAN + r"\)", re.IGNORECASE)
# "i.e." and "e.g." must stay one atomic prose token - letter by letter, "i" and "e" are each
# short enough to pass as a bare math variable, and the periods between them would each end a
# $...$ span, scattering the abbreviation into "$i$.$e$." instead of leaving it as plain text.
_ABBREV_RE = re.compile(r"(?:i\.e\.|e\.g\.)", re.IGNORECASE)

# an ordinal suffix glued directly onto a number ("2nd", "15th") - not followed by another letter,
# so it doesn't eat into an unrelated word that happens to start the same way.
_ORDINAL_SUFFIX_RE = re.compile(r"(st|nd|rd|th)(?![A-Za-z])", re.IGNORECASE)


_A_NOT_NOUN = {
    "and", "or", "but", "was", "are", "lies", "lie", "has", "have", "touches", "touching",
    "subtends", "meets", "passes", "bisects", "divides", "cuts", "joins", "coincides",
}


def _looks_prose_word(word):
    """True for a word that would read as ordinary English right after "(" - "the", "using",
    "twice" - as opposed to one short enough, or special enough, to be a variable or label: "a",
    "AB", "sin". Mirrors the same length/shape cutoffs _tokenize uses for a bare word elsewhere."""
    low = word.lower()
    if len(word) <= 2:
        return False
    if low in _MATH_FUNC_WORDS:
        return False
    if word.isupper() and len(word) <= 4:
        return False
    return True


def _tokenize(text):
    tokens = []
    i, n = 0, len(text)
    paren_stack = []  # True per open "(" that started a prose aside, for the matching ")" to read
    while i < n:
        c = text[i]
        if c == "\\":
            j = _match_latex_cmd(text, i)
            if j > i:
                tokens.append(("MATH", text[i:j]))
                i = j
                continue
            tokens.append(("PROSE", c))
            i += 1
            continue
        if c.isdigit():
            # a comma glued directly between two digit groups, with no space, is one formatted
            # number regardless of grouping convention: Western thousands ("12,345") and Indian
            # lakh/crore grouping ("1,10,000", groups of 2 after the first) both read as a single
            # number. A comma in a plain list ("5, 10, 15") always has a space after it in this
            # corpus's prose, which already stops the match, so this stays unambiguous.
            m = re.match(r"\d+(?:,\d+)*(?:\.\d+)?", text[i:])
            j = i + m.end()
            j = _match_latex_cmd(text, j) if j < n and text[j] in "^_" else j
            # an ordinal suffix glued directly on ("2nd", "5th") stays in the same math span as the
            # number but in upright text, not math italics - \text{} is itself a MATH-kind token so
            # it merges with the digits into one run ("$2\text{nd}$"), per LaTeX's own convention for
            # ordinal/unit suffixes (the same reason units go in \text{} elsewhere in this converter).
            om = _ORDINAL_SUFFIX_RE.match(text, j)
            if om:
                tokens.append(("MATH", text[i:j] + "\\text{%s}" % om.group(1)))
                i = om.end()
                continue
            tokens.append(("MATH", text[i:j]))
            i = j
            continue
        if c.isalpha():
            abbrev_m = _ABBREV_RE.match(text, i)
            if abbrev_m:
                tokens.append(("PROSE", abbrev_m.group(0)))
                i = abbrev_m.end()
                continue
            # unicode-aware (not just A-Za-z): NCERT history asides use transliterated names with
            # diacritics (Aryabhata, Sulba Sutra, ...) - match the WHOLE word so it classifies as
            # one PROSE token, instead of falling through and crashing on an unmatched character.
            m = re.match(r"[^\W\d_]+", text[i:])
            if not m:
                tokens.append(("PROSE", c))
                i += 1
                continue
            word = m.group(0)
            j = i + len(word)
            low = word.lower()
            if low == "s" and i > 0 and text[i - 1] in "'’":
                # the English possessive suffix ("Heron's", "r's", "\pi's") - always prose, never
                # the math variable s, regardless of what precedes the apostrophe.
                tokens.append(("PROSE", word))
                i = j
                continue
            if word == "A":
                # bare capital "A" doubles as the English indefinite article at a sentence/clause
                # start ("A chord of a circle...", "(vi) A semicircle..."), capitalised by ordinary
                # grammar, not because it names a point - distinguish the same way as lowercase
                # "a": a genuine prose NOUN right after means article, anything else (another
                # letter, a verb/conjunction, punctuation) means the usual point label. A
                # conjunction or verb is excluded even though it passes the general prose-word
                # length test - an article is never followed by one ("centres A and B" is a label
                # list, not "a-and-b"; "A is the centre" is the label A, verb is).
                k = j
                while k < n and text[k] == " ":
                    k += 1
                nxt_word_m = re.match(r"[A-Za-z]+", text[k:])
                if nxt_word_m and _looks_prose_word(nxt_word_m.group(0)) \
                        and nxt_word_m.group(0).lower() not in _A_NOT_NOUN:
                    tokens.append(("PROSE", word))
                    i = j
                    continue
            if word.isupper() and len(word) <= 4:
                dm = re.match(r"\d+", text[j:])
                if dm:
                    tokens.append(("MATH", "%s_%s" % (word, dm.group(0))))
                    i = j + dm.end()
                else:
                    tokens.append(("MATH", word))
                    i = j
                continue
            if low in _MATH_FUNC_WORDS:
                tokens.append(("MATH", "\\" + low))
                i = j
                continue
            if low == "a":
                tokens.append(("MATH" if _is_a_mathy(text, i, j) else "PROSE", word))
                i = j
                continue
            if len(word) <= 2 and low not in _STOPWORDS:
                tokens.append(("MATH", word))
                i = j
                continue
            tokens.append(("PROSE", word))
            i = j
            continue
        if c in "'’":
            # a trailing prime mark right after a variable ("a'", "x''") is valid LaTeX as-is and
            # belongs in the same $...$ span as the variable; the English possessive suffix
            # ("Heron's", "it's") is the only case that must stay outside - distinguished by whether
            # the very next character is "s" (already handled on its own as PROSE above) and by
            # whether what precedes the apostrophe was itself classified as math.
            prev_was_math = bool(tokens) and tokens[-1][0] == "MATH"
            nxt = text[i + 1] if i + 1 < n else ""
            tokens.append(("MATH" if prev_was_math and nxt.lower() != "s" else "PROSE", c))
            i += 1
            continue
        if c == ",":
            tokens.append(("COMMA", c))
            i += 1
            continue
        if c in ".;:":
            tokens.append(("BREAK", c))
            i += 1
            continue
        if c.isspace():
            tokens.append(("SPACE", c))
            i += 1
            continue
        if c == "-" and i > 0 and i + 1 < n and text[i + 1].isalpha() \
                and (text[i - 1].isalpha() or text[i - 1].isdigit()):
            # a hyphen glued directly between two letters ("right-angled", "mid-point", "non-
            # parallel") is an English compound word, not a minus sign - real subtraction in this
            # corpus is always written with spaces around it ("a - b"), so the letter-hyphen-letter
            # shape is an unambiguous signal. A digit immediately before the hyphen is the same
            # compound-adjective shape ("5-digit number", "3-year-old") - a letter can never follow a
            # genuine subtraction, so the digit case is just as unambiguous; digit-hyphen-digit
            # ("5-3") is untouched and still renders as subtraction.
            tokens.append(("PROSE", c))
            i += 1
            continue
        if c == "(":
            m = _LABEL_RE.match(text, i)
            if m:
                # a parenthesized part-label - "(i)", "(ii)", "(iii)", "(a)" - is a plain-text
                # marker, not math: keep it whole and unwrapped so every label looks the same
                # (the old per-character rule wrapped short ones like "(i)" as "$(i)$" while
                # breaking longer ones like "(iii)" into "$($iii$)$" - both wrong).
                tokens.append(("PROSE", m.group(0)))
                i = m.end()
                continue
            wm = re.match(r"[A-Za-z]+", text[i + 1:])
            is_prose_open = bool(wm and _looks_prose_word(wm.group(0)))
            if is_prose_open:
                # "(using 22/7)", "(the left side)", "(twice)": an ordinary English word right after
                # "(" means this paren opens an aside, not a math grouping - force-close whatever math
                # run came before it (an empty BREAK token - nothing is emitted, it just stops the run
                # from absorbing this "(" the way "(a + b)" or "f(x)" legitimately do, where the word
                # right after "(" is itself short enough to read as a variable).
                tokens.append(("BREAK", ""))
            paren_stack.append(is_prose_open)
            tokens.append(("MATH", c))
            i += 1
            continue
        if c == ")":
            # the matching close for a paren that opened a prose aside ("(and than 5347)", "(the 4th
            # and 5th)") must itself stay prose - otherwise it glues onto whatever MATH token sits
            # right before it ("5347" + ")" -> one run "$5347)$", a stray, mismatched close-paren
            # inside the dollars). A math-opened paren ("(a + b)", "f(x)") keeps the old behaviour.
            if paren_stack and paren_stack.pop():
                tokens.append(("BREAK", ""))
                tokens.append(("PROSE", c))
                i += 1
                continue
            tokens.append(("MATH", c))
            i += 1
            continue
        if c in "=+-*^_{}<>":
            tokens.append(("MATH", c))
            i += 1
            continue
        tokens.append(("PROSE", c))
        i += 1
    return tokens


def _render(tokens):
    out, run = [], []

    def flush():
        lead = []
        while run and run[0][0] == "SPACE":
            lead.append(run.pop(0)[1])
        trail = []
        while run and run[-1][0] == "SPACE":
            trail.append(run.pop()[1])
        math_text = "".join(t for k, t in run if k == "MATH")
        # a run made of nothing but bare "(" / ")" characters (no digit, letter or command) isn't
        # math on its own - it's the edge of a plain-text parenthetical note ("(Ignore the dotted
        # portions...)") or a sub-part label ("(using 22/7)"'s opening paren before "using" breaks
        # the run) that got split off; wrapping a lone paren in $...$ is never correct LaTeX output.
        if run and math_text.strip("()"):
            out.append("".join(lead))
            out.append("$" + "".join(t for _, t in run) + "$")
            out.append("".join(trail))
        else:
            out.append("".join(lead) + "".join(t for _, t in run) + "".join(trail))
        run.clear()

    for kind, tok_text in tokens:
        if kind in ("MATH", "SPACE"):
            run.append((kind, tok_text))
        else:
            flush()
            out.append(tok_text)
    flush()
    return "".join(out)


_OPEN_PAREN_GLUED_RE = re.compile(r"\$\(([A-Za-z])\$")
_CLOSE_PAREN_GLUED_RE = re.compile(r"\$([A-Za-z])\)\$")


def _fix_glued_list_parens(text):
    """"(b, c and d)" (a parenthetical list of short variables) merges "(" into the first item and
    ")" into the last ("$(b$, $c$ and $d)$") because both are single-letter tokens with nothing to
    force a run break, unlike a multi-letter prose word. Move each paren outside its neighbour's
    dollars so the parens read as plain text and every item is wrapped on its own, like the rest of
    the list already is: "($b$, $c$ and $d$)"."""
    text = _OPEN_PAREN_GLUED_RE.sub(lambda m: "($%s$" % m.group(1), text)
    text = _CLOSE_PAREN_GLUED_RE.sub(lambda m: "$%s$)" % m.group(1), text)
    return text


def latex_wrap(text):
    """Convert plain text (optionally already containing unicode math shorthand: pi/theta/sqrt
    words, x/*, degree signs, superscript/subscript digits, Greek letters, Delta/angle symbols)
    into text with strict inline LaTeX `$...$` spans per LATEX_REFERENCE.md. Idempotent on pure
    prose; safe to call on an already-plain string with no math in it (returned unchanged)."""
    if not text:
        return text
    converted = _convert_symbols(text)
    rendered = _render(_tokenize(converted))
    return _fix_glued_list_parens(rendered)


def wrap_numbered_steps(steps, answer_label="Answer"):
    """Join a list of plain-text working steps into one '1. ...\\n2. ...\\nAnswer: ...' string and
    latex_wrap() it as a whole, so the step index itself becomes its own "$1$." span exactly like
    LATEX_REFERENCE.md section 12's worked examples (do NOT latex_wrap() each step separately and
    then prepend a bare "1. " outside it - that leaves the step index unwrapped)."""
    lines = ["%d. %s" % (i, s) for i, s in enumerate(steps, 1) if s]
    plain = "\n".join(lines)
    return latex_wrap(plain)


def wrap_steps_and_answer(steps, answer, answer_label="Answer"):
    """Like wrap_numbered_steps(), plus a trailing 'Answer: ...' line, all converted together in one
    pass so the whole block's LaTeX is consistent."""
    lines = ["%d. %s" % (i, s) for i, s in enumerate(steps, 1) if s]
    if answer:
        lines.append("%s: %s" % (answer_label, answer))
    plain = "\n".join(lines)
    return latex_wrap(plain)


if __name__ == "__main__":
    # Self-test against LATEX_REFERENCE.md section 12's two worked examples.
    ex1_in = ("Worked example: The movements are 1, -2, 3, -4, and so on up to -10. "
              "Where does the coin end? 1. Pair the movements: 1 + (-2) = -1. 2. 3 + (-4) = -1. "
              "3. 5 + (-6) = -1. 4. 7 + (-8) = -1. 5. 9 + (-10) = -1. "
              "6. (-1) + (-1) + (-1) + (-1) + (-1) = -5. Answer: At -5.")
    ex2_in = "1. 2pi r = 44. 2. 2 * 22/7 * r = 44, so 44r/7 = 44. 3. r = 7 cm. Answer: 7 cm."
    ex2_expected = (
        "$1$. $2\\pi r = 44$. $2$. $2 \\times \\frac{22}{7} \\times r = 44$, so "
        "$\\frac{44r}{7} = 44$. $3$. $r = 7\\text{ cm}$. Answer: $7\\text{ cm}$."
    )
    out1 = latex_wrap(ex1_in)
    out2 = latex_wrap(ex2_in)
    print("Example 1 ->", out1)
    print("Example 2 ->", out2)
    assert out2 == ex2_expected, "Example 2 mismatch:\n  got: %r\n  exp: %r" % (out2, ex2_expected)
    print("Self-test OK: matches LATEX_REFERENCE.md section 12 Example 2 exactly.")
