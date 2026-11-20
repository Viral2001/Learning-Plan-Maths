# -*- coding: utf-8 -*-
"""House style for the plain text of the book questions of Class 5 Chapter 4 (We the Travellers - II), applied around
core/solutions/latex_convert.latex_wrap(). The file is named ch_latex_house.py on purpose: a chapter file called
latex_house.py is shadowed by core/solutions/latex_house.py and silently ignored.
Same idea as chapters/maths5_ch1/new_design/latex_house.py (docs/karan-MD/LEARNING_PLAN_FIELD_CLEANUP_AND_LATEX 1.md,
Part 2, section 7: do not ask the tokenizer to guess; write the text in the shapes it converts cleanly). Found by
converting this chapter's own strings and reading every result:
  1. A part label glued to a number, "(a) 297", became ONE maths span, "$(a) 297$". A colon after a label that is
     followed by a number, "(a): 297", converts as "$(a)$: $297$". A label that follows a number or a closing bracket
     with nothing between ("... 297 (b) 498") is split off with a semicolon.
  2. Place-value letters Th, H, T, O (and TTh) were wrapped as maths variables. They are written as words: ten
     thousands, thousands, hundreds, tens, ones.
  3. The words ON and OFF (the torch), the pronoun I and a lone letter before a number were wrapped as variables,
     "$ON$": fix_blanks() puts them back as words.
  4. A blank written "___" ended up inside maths mode, where it is invalid: it becomes an underline,
     \\underline{\\hspace{1.2em}} (fix_blanks).
Only the book-question strings (question, steps, answer) go through this; nothing here changes a number."""
from __future__ import annotations

import re

_LABEL = r"\((?:[a-i]|iv|v|i{1,3})\)"
_CHAIN = _LABEL + r"(?:" + _LABEL + r")?"
# a part label (or a chain like "(b)(i)") followed by a number: add the colon
_LABEL_BEFORE_NUMBER = re.compile(
    r"(?<![\w)$])(?<!steps )(?<!step )(?<!part )(?<!of )(?<!from )(?<!in )(?<!and )(?<!or )(?<!to )(?<!with )"
    r"(" + _CHAIN + r")\s+(?!(?:and|or|to)\b)(?=[A-Za-z0-9₹−(_])")
# a label that follows a number, a blank or a closing bracket with no punctuation between: a semicolon first
_LABEL_AFTER_VALUE = re.compile(r"(?<=[0-9)_])\s+(?=" + _CHAIN + r"(?::|\s))")

_PLACE = [(re.compile(r"\bTTh\b"), "ten thousands"), (re.compile(r"\bTh\b"), "thousands"),
          (re.compile(r"\bH\b"), "hundreds"), (re.compile(r"\bT\b"), "tens"), (re.compile(r"\bO\b"), "ones")]
_CAP_PLACE = re.compile(r"(^|[.?!]\s+)(ten thousands|thousands|hundreds|tens|ones)\b")
_BLANK = re.compile(r"_{3,}")


def house(text):
    """The plain text: part labels get their colon, place letters become words. Blanks stay as written (___)."""
    if not isinstance(text, str) or not text:
        return text
    text = _LABEL_AFTER_VALUE.sub("; ", text)
    text = _LABEL_BEFORE_NUMBER.sub(lambda m: m.group(1) + ": ", text)
    for rx, word in _PLACE:
        text = rx.sub(word, text)
    # a place name that now starts a sentence takes a capital letter
    return _CAP_PLACE.sub(lambda m: m.group(1) + m.group(2)[0].upper() + m.group(2)[1:], text)


def for_tex(text):
    """Only on the way into latex_wrap (nothing to do in this chapter: no fraction blanks)."""
    return text


def fix_blanks(tex):
    """After latex_wrap: a blank is an underline; the words ON, OFF and I are put back outside maths mode."""
    if not isinstance(tex, str):
        return tex
    tex = _BLANK.sub(lambda m: r"\underline{\hspace{1.2em}}", tex)
    tex = re.sub(r"\$(ON|OFF|I)\$", r"\1", tex)
    return tex
