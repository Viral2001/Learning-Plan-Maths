# -*- coding: utf-8 -*-
"""House style for the plain text of the book questions of Class 5 Chapter 13 (Animal Jumps), applied around
core/solutions/latex_convert.latex_wrap(). Adapted from chapters/maths5_ch2/new_design/frac_latex_house.py (which was
adapted from maths5_ch1/new_design/latex_house.py); the named file is NOT latex_house.py, because a chapter file with that
name is shadowed by core/solutions/latex_house.py and silently ignored. Found by converting this chapter's own strings and
reading every result:
  1. A part label glued to a number, "(a) 10", became ONE maths span, "$(a) 10$". The label gets a colon, "(a): 10",
     and then converts as "$(a)$: $10$". A label that follows a value with nothing between ("... 12 (b) 3 ...") is
     split off with a semicolon. Labels run (a) to (i) in this chapter.
  2. A blank that stands alone ("2 x ___ = 12", "the numbers ___") becomes an underline after conversion
     (fix_blanks). This chapter has no fraction, so the blank-in-a-fraction rule is kept only for safety.
  3. The pronoun "I" and the article "a" before a fraction were wrapped as variables: fix_blanks() puts them back as
     words (kept for safety; this chapter writes no fraction).
  4. The plural of a unit fraction ("1/6s") is never written (checked by plural_fractions(); none in this chapter).
Only the book-question strings (question, steps, answer) go through this; nothing here changes a number."""
from __future__ import annotations

import re

_LABEL = r"\((?:[a-i]|iv|v|i{1,3}|[A-C])\)"
_CHAIN = _LABEL + r"(?:" + _LABEL + r")?"
# a part label followed by a number or fraction: add the colon
_LABEL_BEFORE_NUMBER = re.compile(
    r"(?<![\w)$])(?<!steps )(?<!step )(?<!part )(?<!of )(?<!from )(?<!in )(?<!and )(?<!or )(?<!to )(?<!with )"
    r"(" + _CHAIN + r")\s+(?!(?:and|or|to)\b)(?=[A-Za-z0-9₹−(_])")
# a label that follows a number or a closing bracket with no punctuation between: a semicolon first
_LABEL_AFTER_VALUE = re.compile(r"(?<=[0-9)_])\s+(?=" + _CHAIN + r"(?::|\s))")
# a blank on the top or the bottom of a fraction
_BLANK_TOP = re.compile(r"_{3,}/(?=\d)")
_BLANK_BOTTOM = re.compile(r"(?<=\d)/_{3,}")
_BLANK = re.compile(r"_{3,}")
_UNDERLINE = r"\underline{\hspace{1.2em}}"
_PLURAL_FRACTION = re.compile(r"\d+/\d+s\b")


def house(text):
    """The plain text: part labels get their colon. Blanks stay as written (___/10, 8/___, ___)."""
    if not isinstance(text, str) or not text:
        return text
    text = _LABEL_AFTER_VALUE.sub("; ", text)
    text = _LABEL_BEFORE_NUMBER.sub(lambda m: m.group(1) + ": ", text)
    return text


def for_tex(text):
    """Only on the way into latex_wrap: a blank on the top or bottom of a fraction becomes the placeholder letter q,
    which fix_blanks() turns into an underline inside the \\frac afterwards."""
    if not isinstance(text, str) or not text:
        return text
    text = _BLANK_TOP.sub("q/", text)
    return _BLANK_BOTTOM.sub("/q", text)


def fix_blanks(tex):
    """After latex_wrap: the placeholder q inside a fraction and every ___ become an underline."""
    if not isinstance(tex, str):
        return tex
    tex = re.sub(r"\\frac\{q\}", lambda m: r"\frac{" + _UNDERLINE + "}", tex)
    tex = re.sub(r"(\\frac\{[^{}]*\})\{q\}", lambda m: m.group(1) + "{" + _UNDERLINE + "}", tex)
    tex = _BLANK.sub(lambda m: _UNDERLINE, tex)
    # the converter reads the pronoun I and the article a or A before a fraction as maths variables: put them back
    tex = re.sub(r"\$I\$", "I", tex)
    # the book's (T) and (F) are words in brackets, not variables; the part label (i) is left bare by the converter
    # (it reads it as a roman numeral), so wrap it like (a) to (h) for a consistent look
    tex = re.sub(r"\$\(([TF])\)\$", r"(\1)", tex)
    tex = re.sub(r"(?<![\w$\\])\(i\)(?=:)", r"$(i)$", tex)
    return re.sub(r"\$([aA]) (\\frac)", r"\1 $\2", tex)


def plural_fractions(text):
    """Strings that hold a fraction with a plural s ("1/6s"): the authoring rule forbids them."""
    return _PLURAL_FRACTION.findall(text or "")
