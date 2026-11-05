# -*- coding: utf-8 -*-
"""solutions.json: the single source of truth for every question's solution in a chapter.

    {"<coverage id>": {
        "kind":        "exercise" | "example",     # images are made for exercises (examples only if "images": true)
        "label":       "Missing Sides and New Squares, Q3",   # right of the image header; no NCERT / page words
        "question":    "plain text of the question, as in the book",
        "question_tex": "the same question as LaTeX text (inline maths in $...$), for the question card",
        "given":       "LaTeX text",               # board format: Given
        "find":        "LaTeX text",               # To find
        "method":      "the general formula or property used, named, in LaTeX text",
        "steps":       ["LaTeX text, one operation per line; show values before squaring/rooting", ...],
        "answer_tex":  "LaTeX text; the highlighted answer",
        # Every *_tex / given / find / method / steps / answer_tex field above is written in STRICT
        # inline LaTeX per core/solutions/LATEX_REFERENCE.md: every number, variable, operator, unit
        # and step index is wrapped in its own $...$ (or merged into one coherent equation span),
        # units sit inside \text{}, fractions are \frac{a}{b}, and ordinary prose stays outside the
        # dollars. core/solutions/latex_convert.py's latex_wrap()/wrap_steps_and_answer() implement
        # this conversion programmatically from plain text and are tested against that reference's
        # own worked examples - use them (or follow the same rules by hand) whenever authoring these
        # fields, rather than preserving raw unicode symbols or bare "a/b" fractions. gates/latex_content.py
        # checks every one of these fields automatically inside gate_runner.run() (plain build.py, no extra
        # step) and fails the build on a mistake a converter OR a person can make (an exponent swallowing a
        # fraction that belongs to the whole term, e.g. a^2/4 meaning a^(2/4) instead of the intended
        # (a^2)/4; a command glued to the next letter; a lone "(" wrapped on its own) while downgrading
        # genuinely ambiguous findings (a bare unit letter, a variable wrapped in some places but not
        # others) to warnings for a human to check. core/solutions/latex_checker.py is the same logic,
        # runnable directly on one field or a whole plan for faster feedback while still authoring.
        "common_mistake": "LaTeX text",            # the slip a student who got it wrong makes
        "verification": "LaTeX text, optional",
        "figure":      {"type": "right_triangle", ...},   # optional, see figure_from_spec in style/_style.py;
                                                          # side labels are math mode: write 6\\,\\text{cm}
        "source":      "book" | "authored",
        "images":      true | false                # optional override of the kind default
        "cards":       1 | 2                        # optional: solution cards. Default 1; 2 when the chapter config
                                                    # has "solution_continuation" and the working is long
                                                    # (core/solutions/layout.py)
        "cut":         k                            # optional: steps kept on card 1 when there are two cards
    }}

The format rules are the teacher's board-solution rules (math_solutions/skill/references/format-rules.md):
name the general formula, one operation per line with the values shown, a common-mistake note, the answer
merged into the solution in a highlighted box, a figure that matches the question and never shows the answer.
"""
from __future__ import annotations

import io
import json
import os
import re

REQUIRED = ("kind", "label", "question", "question_tex", "steps", "answer_tex", "common_mistake", "source")
KINDS = ("exercise", "example")
SOURCES = ("book", "authored")
FIGURE_TYPES = ("right_triangle", "dot_grid", "grid_table", "none")
PATH_NAME = "solutions.json"


def path_for(folder):
    return os.path.join(folder, PATH_NAME)


def load(folder):
    p = path_for(folder)
    if not os.path.exists(p):
        return {}
    with io.open(p, encoding="utf-8") as f:
        return json.load(f)


def wants_images(sol):
    return sol.get("images", sol.get("kind") == "exercise")


def validate(sol_map):
    """Structural problems of a solutions.json, as a list of strings (empty = fine)."""
    errs = []
    for cov, s in sol_map.items():
        for k in REQUIRED:
            if not s.get(k):
                errs.append("%s: '%s' is empty or missing" % (cov, k))
        if s.get("kind") not in KINDS:
            errs.append("%s: kind must be one of %s" % (cov, KINDS))
        if s.get("source") not in SOURCES:
            errs.append("%s: source must be one of %s" % (cov, SOURCES))
        if not isinstance(s.get("steps"), list) or not all(isinstance(x, str) and x.strip() for x in s.get("steps") or []):
            errs.append("%s: steps must be a list of non-empty strings" % cov)
        if "cards" in s and s["cards"] not in (1, 2):
            errs.append("%s: cards must be 1 or 2" % cov)
        if "cut" in s and not (isinstance(s["cut"], int) and 1 <= s["cut"] < len(s.get("steps") or [])):
            errs.append("%s: cut must be a whole number from 1 to the number of steps minus 1" % cov)
        fig = s.get("figure")
        if fig and fig.get("type") not in FIGURE_TYPES:
            errs.append("%s: figure.type must be one of %s" % (cov, FIGURE_TYPES))
        for field, text in _strings(s):
            if _CONTROL.search(text):
                errs.append("%s: '%s' has a control character (a tab, newline or backspace): a LaTeX backslash "
                            "was lost, e.g. \\times written as \\\\times in the wrong place" % (cov, field))
    return errs


_CONTROL = re.compile(r"[\x00-\x1f]")


def _strings(value, name=""):
    if isinstance(value, str):
        yield name, value
    elif isinstance(value, dict):
        for k, v in value.items():
            yield from _strings(v, k)
    elif isinstance(value, list):
        for v in value:
            yield from _strings(v, name)


# ---------------------------------------------------------------------------
# plain text for the plan's `steps` / `answer` fields (the eqcheck gates read these)
# ---------------------------------------------------------------------------
_SUP = {"2": "\u00b2", "3": "\u00b3"}


def tex_to_plain(t):
    """LaTeX text -> the plain text the plan's steps/answer carry. Not a full LaTeX parser: it covers the
    commands the solution rules use (\\times \\div \\cdot \\sqrt \\frac \\text \\textbf ^n \\, and $)."""
    s = t
    for _ in range(3):
        s = re.sub(r"\\(?:text|textbf|mathrm|textit)\{([^{}]*)\}", r"\1", s)
        s = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"(\1)/(\2)", s)
        s = re.sub(r"\\sqrt\{([^{}]*)\}", "\u221a(\\1)", s)
    s = re.sub(r"\\sqrt\s*(\w)", "\u221a\\1", s)
    s = s.replace(r"\times", "\u00d7").replace(r"\div", "\u00f7").replace(r"\cdot", "\u00d7")
    s = s.replace(r"\neq", "\u2260").replace(r"\approx", "\u2248").replace(r"\pi", "\u03c0")
    s = s.replace(r"\therefore", "so").replace(r"\angle", "\u2220").replace(r"\circ", "\u00b0")
    s = re.sub(r"\^\{?(\d)\}?", lambda m: _SUP.get(m.group(1), "^" + m.group(1)), s)
    s = re.sub(r"\\[,;:! ]", " ", s)
    s = re.sub(r"\\\\(\[[^\]]*\])?", " ", s)
    s = s.replace("$", "").replace("{", "").replace("}", "")
    s = re.sub(r"\\([a-zA-Z]+)", r"\1", s)
    return re.sub(r"\s+", " ", s).strip()


def plan_fields(sol):
    """(steps, answer) for the plan's worked_example / exercise block: Given and To find first, then the
    working, each as plain text; verification last. The answer is the highlighted answer."""
    steps = []
    if sol.get("given"):
        steps.append("Given: " + tex_to_plain(sol["given"]))
    if sol.get("find"):
        steps.append("To find: " + tex_to_plain(sol["find"]))
    if sol.get("method"):
        steps.append("Use: " + tex_to_plain(sol["method"]))
    steps += [tex_to_plain(x) for x in sol["steps"]]
    if sol.get("verification"):
        steps.append("Check: " + tex_to_plain(sol["verification"]))
    return steps, tex_to_plain(sol["answer_tex"])


# ---------------------------------------------------------------------------
# display text for the plan's concept text (what the student reads): the same shape as plan_fields,
# but keeping each field's own inline LaTeX ($...$, already how given/find/method/steps/question_tex/
# answer_tex are authored above) instead of flattening it with tex_to_plain - so a reader can tell the
# maths from the prose. gates/eqcheck_* keep reading plan_fields()'s plain steps/answer, unaffected.
# ---------------------------------------------------------------------------

def display_fields(sol):
    """(steps, answer) for display: one entry per plan_fields() entry, same order, each kept as the
    inline-LaTeX text it was authored with."""
    steps = []
    if sol.get("given"):
        steps.append("Given: " + sol["given"])
    if sol.get("find"):
        steps.append("To find: " + sol["find"])
    if sol.get("method"):
        steps.append("Use: " + sol["method"])
    steps += list(sol["steps"])
    if sol.get("verification"):
        steps.append("Check: " + sol["verification"])
    return steps, sol["answer_tex"]


def display_question(sol):
    """The question for display: question_tex (inline LaTeX) when authored, else the plain question."""
    return sol.get("question_tex") or sol.get("question", "")
