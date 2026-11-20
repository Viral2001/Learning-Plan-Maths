# -*- coding: utf-8 -*-
"""House style for the plain text of the book questions of Class 5 Chapter 7 (Shapes and Patterns), applied around
core/solutions/latex_convert.latex_wrap(). Copied from the Class 5 Chapter 2 file (fractions rules kept, none of them fires here but the part-label colon and the blank rules); same idea as chapters/maths5_ch1/new_design/latex_house.py
(docs/karan-MD/LEARNING_PLAN_FIELD_CLEANUP_AND_LATEX 1.md, Part 2, section 7: do not ask the tokenizer to guess; write
the text in the shapes it converts cleanly), found by converting this chapter's own strings and reading every result:
  1. A part label glued to a fraction or number, "(a) 2/5", became ONE maths span, "$(a) \\frac{2}{5}$". The label
     gets a colon, "(a): 2/5", and then converts as "$(a)$: $\\frac{2}{5}$". A label that follows a value with nothing
     between ("... 3/4 (b) 5/6") is split off with a semicolon.
  2. A blank inside a fraction, "___/10" or "8/___", split the fraction into pieces outside maths mode. It is
     written with the placeholder letter q before conversion ("q/10", "8/q") and the placeholder becomes an
     underline inside the \\frac afterwards (fix_blanks). A blank that stands alone ("___", also between two
     fractions, "1/4 ___ 3/4") becomes an underline too.
  3. The pronoun "I" and the article "a" before a fraction ("a 1/6 piece") were wrapped as variables: fix_blanks()
     puts them back as words.
  4. A unit fraction with a plural s ("1/6s") is read as the fraction 1 over 6s. Never written; the authoring rule is
     "pieces of 1/6" (checked by plural_fractions()).
Only the book-question strings (question, steps, answer) go through this; nothing here changes a number."""
from __future__ import annotations

import re

_LABEL = r"\((?:[a-h]|iv|v|i{1,3}|[A-C])\)"
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
    return re.sub(r"\$([aA]) (\\frac)", r"\1 $\2", tex)


def plural_fractions(text):
    """Strings that hold a fraction with a plural s ("1/6s"): the authoring rule forbids them."""
    return _PLURAL_FRACTION.findall(text or "")
