# -*- coding: utf-8 -*-
"""House style for the plain text of book questions, applied just before core/solutions/latex_convert.latex_wrap().

docs/karan-MD/LEARNING_PLAN_FIELD_CLEANUP_AND_LATEX 1.md, Part 2, section 7: do not ask the tokenizer to guess; write
the text in the shapes it converts cleanly. The general rules below were found converting Class 5 Ch 1 and Class 7 Ch 10
and reading every result (the Class 5-only rules - place-value letters, token counts, town rows - stay in that chapter's
own latex_house.py, they would damage geometry text):

  1. A part label glued to a number, "(a) 7,418", became ONE maths span, "$(a) 7,418$". A colon after a label that
     starts a part, "(a): 7,418", converts as "$(a)$: $7,418$".
  2. A label that follows a number or a closing bracket with nothing between ("Difference = 9 (b) Sum = 4") is split
     off with a semicolon so it stays outside the previous number's span: "Difference = 9; (b): Sum = 4".
  3. A numbered label that starts a sentence, "(3) A 1-digit number ...": colon too.
  4. A blank written "___" ends up inside maths mode, where it is invalid: after conversion it becomes an underline,
     \\underline{\\hspace{1.2em}} (fix_blanks).

house(text, phrases) first applies the chapter's own whole-phrase replacements (edits.json "_phrases", for a shape
that only that chapter has), then the general rules. Only question / steps / answer strings go through this, and only
on their way to the displayed LaTeX text; the plain question / steps / answer fields keep the book's wording.
Nothing here changes a number or a letter."""
from __future__ import annotations

import re

_LABEL = r"\((?:[a-hj-l]|iv|ix|x|vi{1,3}|v|i{1,3})\)"
_CHAIN = _LABEL + r"(?:" + _LABEL + r")?"
_LABEL_BEFORE_NUMBER = re.compile(
    r"(?<![\w)$])(?<!steps )(?<!step )(?<!part )(?<!of )(?<!from )(?<!in )(?<!and )(?<!or )(?<!to )(?<!with )"
    r"(" + _CHAIN + r")\s+(?!(?:and|or|to)\b)(?=[A-Za-z0-9₹−(])")
_LABEL_AFTER_VALUE = re.compile(r"(?<=[0-9)A-Z])\s+(?=" + _CHAIN + r"(?::|\s))")
_NUM_LABEL = re.compile(r"(^|[.?!]\s)(\(\d\))\s+(?=[A-Za-z])")
_BLANK = re.compile(r"_{3,}")
# "a. +5  b. +5  c. +1": a list whose parts are lettered "a." "b." (no brackets). Left alone, the label of the next part
# was read as a unit or variable and swallowed into the previous number's maths span ("$+5 b$."). Only a run that
# starts a, b ... in order is a list; a lone "a." at the end of a sentence is not touched.
_DOT_LABEL = re.compile(r"(?:^|(?<=[\s;:,]))([a-hj-l])\.\s+(?=\S)")


def _dot_labels(text):
    ms = list(_DOT_LABEL.finditer(text))
    letters = [m.group(1) for m in ms]
    if len(letters) < 2 or letters[0] != "a" or letters[1] != "b":
        return text
    return _DOT_LABEL.sub(lambda m: "(%s): " % m.group(1), text)


# "a) inverse of +4  b) inverse of -4": a label with only its closing bracket. Wrapped as it stands, the letter became a
# variable ("$a$) ..."), the bracket stayed outside and the next label was swallowed. It becomes "(a) ..." (and then follows
# the rules above), but only where the bracket does not close one opened earlier in the text: "(3x + a) is" is not a label.
_CLOSE_LABEL = re.compile(r"(?<![\w(])([a-hj-l]|iv|v|i{1,3})\)(?=\s)")
_AMPM = re.compile(r"(\d)\s*([apAP])\.[mM]\.")
_AMPM_END = re.compile(r"(\d)\s*([apAP])\.[mM]\.(?=\s+[A-Z(]|\s*$)")


def _close_labels(text):
    def rep(m):
        before = text[:m.start()]
        return m.group(0) if before.count("(") > before.count(")") else "(%s)" % m.group(1)
    return _CLOSE_LABEL.sub(rep, text)


# a text that starts with its own part label "a. ..." or "a: ...": the letter was a variable and the dot ended its span
_LEAD_LABEL = re.compile(r"^([a-hj-l])[.:]\s+(?=\S)")


# "1 + 2 + 3 + ... + 99 + 100", "1, 2, 3, ..., 10": an ellipsis between two operators / commas belongs to the expression
_ELLIPSIS = re.compile(r"(?<=[+\-\u2212\u00d7\u00f7,])\s*(?:\.\.\.|\u2026)\s*(?=([+\-\u2212\u00d7\u00f7,]))")


def house(text, phrases=None):
    if not isinstance(text, str) or not text:
        return text
    for old, new in (phrases or {}).items():
        text = text.replace(old, new)
    # "10:00 a.m." was split into "a.$m$."; the final dot of "a.m." also ends the sentence when a new sentence follows
    text = _AMPM_END.sub(lambda m: m.group(1) + "\\text{ %sM}." % m.group(2).upper(), text)
    text = _AMPM.sub(lambda m: m.group(1) + "\\text{ %sM}" % m.group(2).upper(), text)
    text = _ELLIPSIS.sub(lambda m: " \\ldots" + ("" if m.group(1) == "," else " "), text)
    text = _dot_labels(text)                       # "a. 1 b. 2 c. 3" lists first: they need the "a."
    text = _LEAD_LABEL.sub(lambda m: "(%s): " % m.group(1), text)
    text = _close_labels(text)
    text = _LABEL_AFTER_VALUE.sub("; ", text)
    text = _LABEL_BEFORE_NUMBER.sub(lambda m: m.group(1) + ": ", text)
    text = _NUM_LABEL.sub(lambda m: m.group(1) + m.group(2) + ": ", text)
    return text


def fix_blanks(tex):
    if not isinstance(tex, str):
        return tex
    return _BLANK.sub(lambda m: r"\underline{\hspace{1.2em}}", tex)
