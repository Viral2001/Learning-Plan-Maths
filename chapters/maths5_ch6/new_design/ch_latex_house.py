# -*- coding: utf-8 -*-
"""House style for the plain text of the book questions of Class 5 Chapter 6 (The Dairy Farm), applied around
core/solutions/latex_convert.latex_wrap(). Same idea as chapters/maths5_ch2/new_design/frac_latex_house.py and
chapters/maths5_ch1/new_design/latex_house.py (docs/karan-MD/LEARNING_PLAN_FIELD_CLEANUP_AND_LATEX 1.md, Part 2,
section 7: do not ask the tokenizer to guess; write the text in the shapes it converts cleanly), found by converting
this chapter's own strings and reading every result. (The file is named ch_latex_house.py: a chapter file named
latex_house.py is shadowed by core/solutions/latex_house.py and silently ignored.)
  1. A part label glued to a number, "(a) 78 × 4", became ONE maths span, "$(a) 78 \\times 4$". The label gets a
     colon, "(a): 78 × 4", and then converts as "$(a)$: $78 \\times 4$". A numbered label "(1) 7 × 52" is the same.
  2. A label that follows a value with nothing between ("... 78 × 4 (b): ...") is split off with a semicolon.
  3. Place value letters Th, H, T, O, TTh were wrapped as maths variables, "$Th$". They are written as words:
     ten thousands, thousands, hundreds, tens, ones.
  4. A blank "___" ended up inside maths mode, where it is invalid: after conversion it becomes an underline,
     \\underline{\\hspace{1.2em}} (fix_blanks).
  5. The pronoun "I" before a number was wrapped as a variable: fix_blanks() puts it back as a word.
Only the book-question strings (question, steps, answer) go through this; nothing here changes a number."""
from __future__ import annotations

import re

_LABEL = r"\((?:[a-h]|iv|v|i{1,3}|[A-C]|[1-9])\)"
_CHAIN = _LABEL + r"(?:" + _LABEL + r")?"
# a part label followed by a number: add the colon
_LABEL_BEFORE_NUMBER = re.compile(
    r"(?<![\w)$])(?<!steps )(?<!step )(?<!part )(?<!of )(?<!from )(?<!in )(?<!and )(?<!or )(?<!to )(?<!with )"
    r"(" + _CHAIN + r")\s+(?!(?:and|or|to)\b)(?=[A-Za-z0-9₹−(_])")
# a label that follows a number or a closing bracket with no punctuation between: a semicolon first
_LABEL_AFTER_VALUE = re.compile(r"(?<=[0-9)_])\s+(?=" + _CHAIN + r"(?::|\s))")
_PLACE = [(re.compile(r"\bTTh\b"), "ten thousands"), (re.compile(r"\bTh\b"), "thousands"),
          (re.compile(r"\bH\b"), "hundreds"), (re.compile(r"\bT\b"), "tens"), (re.compile(r"\bO\b"), "ones")]
_CAP_PLACE = re.compile(r"(^|[.?!]\s+)(ten thousands|thousands|hundreds|tens|ones)\b")
_BLANK = re.compile(r"_{3,}")
_UNDERLINE = r"\underline{\hspace{1.2em}}"


def house(text):
    """The plain text: part labels get their colon; place value letters become words. Blanks stay as written."""
    if not isinstance(text, str) or not text:
        return text
    text = _LABEL_AFTER_VALUE.sub("; ", text)
    text = _LABEL_BEFORE_NUMBER.sub(lambda m: m.group(1) + ": ", text)
    for rx, word in _PLACE:
        text = rx.sub(word, text)
    return _CAP_PLACE.sub(lambda m: m.group(1) + m.group(2)[0].upper() + m.group(2)[1:], text)


def for_tex(text):
    """Only on the way into latex_wrap (nothing to do here: no blank sits inside a fraction in this chapter)."""
    return text


def fix_blanks(tex):
    """After latex_wrap: every ___ becomes an underline; the pronoun I is a word again."""
    if not isinstance(tex, str):
        return tex
    tex = _BLANK.sub(lambda m: _UNDERLINE, tex)
    return re.sub(r"\$I\$", "I", tex)
