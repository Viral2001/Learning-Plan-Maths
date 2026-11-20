# -*- coding: utf-8 -*-
"""House style for the plain text of the book questions of Class 5 Chapter 8 (Weight and Capacity), applied around
core/solutions/latex_convert.latex_wrap(). Adapted from chapters/maths5_ch2/new_design/frac_latex_house.py (Ch2 found the
quirks; this chapter has no fractions but has units: kg, g, mg, l, ml, quintal, tonne, and the rupee sign).
(A chapter file called latex_house.py is SHADOWED by core/solutions/latex_house.py and silently ignored: hence ch_.)
Quirks found by converting this chapter's own strings and reading every result:
  1. A part label glued to a number, "(a) 7 kg 67 g", became ONE maths span, "$(a) 7\\text{ kg} ...$". The label gets a
     colon, "(a): 7 kg 67 g", and then converts as "$(a)$: $7 ...$". A label that follows a value with nothing between
     ("... 3/4 (b) 5/6") is split off with a semicolon.
  2. The converter only wraps kg, cm, ml and (sometimes) g as units. A bare "g", "mg" or "l" stays italic maths, and a
     unit followed by a number ("1\\text{ kg} 250\\text{ g}") loses the space in maths mode. wrap_units() puts every
     unit after a number inside \\text{ } and adds a thin space after a unit that is followed by a number.
  3. A blank "___" becomes an underline (fix_blanks), also inside a maths span.
  4. The pronoun "I" and the article "a" before a number were wrapped as variables: fix_blanks() puts them back as words.
Only the book-question strings (question, steps, answer) go through this; nothing here changes a number."""
from __future__ import annotations

import re

_LABEL = r"\((?:[a-h]|iv|v|i{1,3}|[A-C])\)"
_CHAIN = _LABEL + r"(?:" + _LABEL + r")?"
# a part label followed by a number: add the colon
_LABEL_BEFORE_NUMBER = re.compile(
    r"(?<![\w)$])(?<!steps )(?<!step )(?<!part )(?<!of )(?<!from )(?<!in )(?<!and )(?<!or )(?<!to )(?<!with )"
    r"(" + _CHAIN + r")\s+(?!(?:and|or|to)\b)(?=[A-Za-z0-9₹−(_])")
# a label that follows a number or a closing bracket with no punctuation between: a semicolon first
_LABEL_AFTER_VALUE = re.compile(
    r"(?:(?<=[0-9)_])|(?<=\bg)|(?<=\bkg)|(?<=\bmg)|(?<=\bml)|(?<=\bl)|(?<=\btonnes)|(?<=\bquintals))\s+(?=" + _CHAIN
    + r"(?::|\s))")
_BLANK = re.compile(r"_{3,}")
_UNDERLINE = r"\underline{\hspace{1.2em}}"
# a unit directly after a number (or a closing brace of one) inside a maths span, not already in \text{ }
_UNIT_AFTER_NUMBER = re.compile(r"(?<=[0-9}])(\s?)(mg|ml|kg|g|l)(?![A-Za-z\\{])")
_UNIT_THEN_NUMBER = re.compile(r"(\\text\{ (?:mg|ml|kg|g|l)\})\s+(?=[0-9\\])")


def house(text):
    """The plain text: part labels get their colon. Blanks stay as written (___)."""
    if not isinstance(text, str) or not text:
        return text
    text = _LABEL_AFTER_VALUE.sub("; ", text)
    text = _LABEL_BEFORE_NUMBER.sub(lambda m: m.group(1) + ": ", text)
    return text


def for_tex(text):
    """Only on the way into latex_wrap. Nothing to do in this chapter (no blank inside a fraction); kept so the
    concept_plan loop is the same as Chapter 2's."""
    return text


def wrap_units(tex):
    """Inside every $...$ span: units after a number go inside \\text{ }, and a unit followed by a number gets a thin
    space."""
    if not isinstance(tex, str) or "$" not in tex:
        return tex
    parts = tex.split("$")
    for i in range(1, len(parts), 2):
        seg = parts[i]
        seg = _UNIT_AFTER_NUMBER.sub(lambda m: r"\text{ %s}" % m.group(2), seg)
        seg = _UNIT_THEN_NUMBER.sub(lambda m: m.group(1) + r"\; ", seg)
        parts[i] = seg
    return "$".join(parts)


def fix_blanks(tex):
    """After latex_wrap: every ___ becomes an underline, units are wrapped, and the pronoun I and the article a are
    words again."""
    if not isinstance(tex, str):
        return tex
    tex = _BLANK.sub(lambda m: _UNDERLINE, tex)
    tex = wrap_units(tex)
    tex = re.sub(r"\$I\$", "I", tex)
    return re.sub(r"\$([aA]) (\d|\\)", r"\1 $\2", tex)
