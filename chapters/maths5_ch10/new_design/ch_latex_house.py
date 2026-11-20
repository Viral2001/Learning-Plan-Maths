# -*- coding: utf-8 -*-
"""House style for the plain text of the book questions of Class 5 Chapter 10 (Symmetrical Designs), applied around
core/solutions/latex_convert.latex_wrap(). Adapted from chapters/maths5_ch2/new_design/frac_latex_house.py (same idea:
do not ask the tokenizer to guess; write the text in the shapes it converts cleanly), found by converting this chapter's
own strings and reading every result:
  1. A part label glued to a word or number, "(a) Which", became ONE maths span. The label gets a colon, "(a): Which", and
     then converts as "(a): Which" (see fix_blanks for the unwrapping of the label itself). A label that follows a value
     with nothing between ("... ___ (b) ...") is split off with a semicolon.
  2. A blank inside a fraction ("___/10") is not used in this chapter, but the helpers stay: a blank that stands alone
     ("___") becomes an underline.
  3. The pronoun "I" and the article "a" before a fraction ("a 1/4 turn") were wrapped as variables: fix_blanks() puts
     them back as words.
  4. The converter wraps every single capital letter as a maths variable ("$E$", "$B$"). This chapter has no variables:
     the capital letters are the letters of the alphabet, the names of blocks and designs, so fix_blanks() unwraps them
     back to plain letters. The part labels "(a)" to "(h)" are unwrapped too, so that "(a)" and "(iv)" look alike.
  5. "digit(s)", "shape(s)" and "line(s)", and "2-, 3- and 4-digit", cannot be converted cleanly: they are written
     "digits", "shapes", "lines" and "2-digit, 3-digit and 4-digit" (checked by bad_forms()).
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
    tex = re.sub(r"\$([aA]) (\\frac)", r"\1 $\2", tex)
    # a single capital letter is a letter of the alphabet here, not a variable; a part label (a) to (h) is plain text
    tex = re.sub(r"\$([A-Z])\$", r"\1", tex)
    return re.sub(r"\$\(([a-h])\)\$", r"(\1)", tex)


def plural_fractions(text):
    """Strings that hold a fraction with a plural s ("1/6s"): the authoring rule forbids them."""
    return _PLURAL_FRACTION.findall(text or "")


_BAD_FORMS = re.compile(r"\b\w+\((?:s|es)\)|\d-,|\b\d+s\b")


def bad_forms(text):
    """Strings with a form the converter turns into nonsense: (s) plurals, "2-," lists, a plural digit like 0s."""
    return _BAD_FORMS.findall(text or "")
