# -*- coding: utf-8 -*-
"""House style for the plain text of the book questions of Class 5 Chapter 5 (Far and Near), applied around
core/solutions/latex_convert.latex_wrap(). Adapted from chapters/maths5_ch2/new_design/frac_latex_house.py (same idea;
the file is named ch_latex_house.py because a chapter file named latex_house.py is shadowed by
core/solutions/latex_house.py). Found by converting this chapter's own strings and reading every result:
  1. A part label glued to a number or a length, "(a) 456 cm", became ONE maths span, "$(a) 456\\text{ cm}$". The label
     gets a colon, "(a): 456 cm", and then converts as "$(a)$: $456\\text{ cm}$". A label that follows a value with
     nothing between ("... 5 m (b) 55 cm") is split off with a semicolon. The labels run (a) to (n).
  2. A blank before a unit, "___ mm" or "___ m", left the unit outside \\text (the converter reads a lone m as a
     variable). Every blank is written as the number 7654321 before conversion, so the converter wraps the unit in
     \\text{ mm} as it does after any number, and the number becomes an underline afterwards (fix_blanks).
  3. The article "a" or the pronoun "I" before a number was wrapped as a variable: fix_blanks() puts them back as words.
  4. Two lengths side by side, "3 km 450 m", came out as "$3\\text{ km} 450\\text{ m}$", where maths mode drops the space
     and shows "3 km450 m". The space is moved inside the text, "\\text{ km } 450".
  5. A unit written alone in a sentence ("to cm", "in m") came out as "to$\\text{ cm}$" or "$m$": it goes back to the
     plain word.
  6. The list of signs "(+, −, ×, ÷)" came out as "$(+$, $-$, $\\times$ , $\\div )$": for the display text the brackets are
     dropped ("+, −, × or ÷"). The plain text is not changed.
Only the book-question strings (question, steps, answer) go through this; nothing here changes a number."""
from __future__ import annotations

import re

_LABEL = r"\((?:[a-n]|iv|v|i{1,3}|[A-C])\)"
_CHAIN = _LABEL + r"(?:" + _LABEL + r")?"
# a part label followed by a number or a word: add the colon
_LABEL_BEFORE_NUMBER = re.compile(
    r"(?<![\w)$])(?<!steps )(?<!step )(?<!part )(?<!of )(?<!from )(?<!in )(?<!and )(?<!or )(?<!to )(?<!with )"
    r"(" + _CHAIN + r")\s+(?!(?:and|or|to)\b)(?=[A-Za-z0-9₹−(_])")
# a label that follows a number or a closing bracket with no punctuation between: a semicolon first
_LABEL_AFTER_VALUE = re.compile(r"(?<=[0-9)_])\s+(?=" + _CHAIN + r"(?::|\s))")
_BLANK = re.compile(r"_{3,}")
_PLACEHOLDER = "7654321"
_UNDERLINE = r"\underline{\hspace{1.2em}}"
_SIGNS = re.compile(r"\(\+, −, ×, ÷\)")
_UNIT_GAP = re.compile(r"(\\text\{ (?:km|m|cm|mm)\})(?= ?(?:[0-9]|\\underline))")


def house(text):
    """The plain text: part labels get their colon. Blanks stay as written (___)."""
    if not isinstance(text, str) or not text:
        return text
    text = _LABEL_AFTER_VALUE.sub("; ", text)
    text = _LABEL_BEFORE_NUMBER.sub(lambda m: m.group(1) + ": ", text)
    return text


def for_tex(text):
    """Only on the way into latex_wrap: every blank becomes the number 7654321 (so a unit after it is wrapped), and
    the bracketed list of signs loses its brackets."""
    if not isinstance(text, str) or not text:
        return text
    text = _SIGNS.sub("+, −, × or ÷", text)
    return _BLANK.sub(_PLACEHOLDER, text)


def fix_blanks(tex):
    """After latex_wrap: the placeholder becomes an underline, the article a and the pronoun I go back to words, and a
    length of two units gets its space back."""
    if not isinstance(tex, str):
        return tex
    tex = tex.replace(_PLACEHOLDER, _UNDERLINE)
    tex = re.sub(r"\$I\$", "I", tex)
    tex = re.sub(r"\$([aA]) (?=[0-9\\])", r"\1 $", tex)
    # a unit written alone in a sentence ("to cm", "in m") is a word, not maths: the converter wraps it as a variable or as
    # \text glued to the word before it, so it goes back to plain text
    tex = re.sub(r"(?<=[A-Za-z])\$\\text\{ (km|m|cm|mm)\}\$", r" \1", tex)
    tex = re.sub(r"(?<![\w$])\$(km|m|cm|mm)\$(?![\w$])", r"\1", tex)
    return _UNIT_GAP.sub(lambda m: m.group(1)[:-1] + " }", tex)


def plural_fractions(text):
    """Kept for the shared self-check: strings that hold a fraction with a plural s ("1/6s"). This chapter has no
    fractions, so the list is normally empty."""
    return re.findall(r"\d+/\d+s\b", text or "")
