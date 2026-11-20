# -*- coding: utf-8 -*-
"""House style for the plain text of the book questions of Class 5 Chapter 14 (Maps and Locations), applied around
core/solutions/latex_convert.latex_wrap(). Copied from the Class 5 Chapter 2 house module (frac_latex_house.py); the
rules that matter for this chapter are:
  1. A part label glued to a position or a word, "(a) (11,11)" or "(a) Lion", became ONE maths span. The label gets a
     colon, "(a): (11,11)", and then converts as "$(a)$: $(11,11)$". A label that follows a value with nothing between
     is split off with a semicolon.
  2. A blank that stands alone ("___") becomes an underline after conversion (fix_blanks). A blank inside a fraction
     does not occur in this chapter (the helpers stay in the file unchanged and harmless).
  3. The pronoun "I" and the article "a" before a number were wrapped as variables: fix_blanks() puts them back as
     words.
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
    # a blank followed by the unit cm: the unit goes inside \text{} like every other cm
    tex = re.sub(r"(\\underline\{\\hspace\{1\.2em\}\}) cm\$", lambda m: m.group(1) + r"\text{ cm}$", tex)
    # "Stop 1 (S1)" became one maths span "$1 (S_1)$": the number and the stop label are two spans, and "(s)" is words
    tex = re.sub(r"\$(\d+) \(S_(\d+)\)\$", lambda m: "$%s$ ($S_%s$)" % (m.group(1), m.group(2)), tex)
    tex = tex.replace("$(s)$", "(s)")
    # the converter reads the pronoun I and the article a or A before a fraction as maths variables: put them back
    tex = re.sub(r"\$I\$", "I", tex)
    return re.sub(r"\$([aA]) (\\frac)", r"\1 $\2", tex)


def plural_fractions(text):
    """Strings that hold a fraction with a plural s ("1/6s"): the authoring rule forbids them."""
    return _PLURAL_FRACTION.findall(text or "")
