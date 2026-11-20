# -*- coding: utf-8 -*-
"""House style for the plain text of the book questions of Class 5 Chapter 12 (Racing Seconds), applied around
core/solutions/latex_convert.latex_wrap(). Adapted from chapters/maths5_ch2/new_design/frac_latex_house.py; this file is
NOT called latex_house.py (a chapter file of that name is shadowed by core/solutions/latex_house.py and silently
ignored). Found by converting this chapter's own strings and reading every result:
  1. A part label glued to a number or a time, "(a) 01:15", became ONE maths span. The label gets a colon, "(a): 01:15",
     and then converts as "$(a)$: ...". A label that follows a value with nothing between is split off with a semicolon.
  2. A blank, "___", stays a blank; it becomes an underline after the conversion (fix_blanks).
  3. A clock time such as 01:15 p.m., 08:35 PM or 14:30 hours was split into "$01$:$15 p$.$m$." (the a.m./p.m. letters
     read as variables, the colon outside the maths). Every clock time, with its a.m. / p.m. / AM / PM / hours word, is
     therefore hidden behind a plain-letter placeholder before the conversion and put back as plain text after it
     (for_tex / fix_blanks). A time is a label, not a number to compute with, so it stays plain text.
  3b. "12-hour", "24-hour" and "Nana ji" (the 2-letter ji read as a variable) are held back the same way.
  4. The unit abbreviations min, sec, hr (and sec. read as the function secant) are never written in a book question:
     the authoring rule is "minutes", "seconds", "hours" in full (checked by abbreviations()).
  5. The pronoun I and the article a before a number were wrapped as variables: fix_blanks() puts them back.
Only the book-question strings (question, steps, answer) go through this; nothing here changes a number."""
from __future__ import annotations

import re

_LABEL = r"\((?:[a-h]|iv|v|i{1,3}|vi{1,3}|ix|x|[A-C])\)"
_CHAIN = _LABEL + r"(?:" + _LABEL + r")?"
# a part label followed by a number, a time or a blank: add the colon
_LABEL_BEFORE_NUMBER = re.compile(
    r"(?<![\w)$])(?<!steps )(?<!step )(?<!part )(?<!of )(?<!from )(?<!in )(?<!and )(?<!or )(?<!to )(?<!with )"
    r"(" + _CHAIN + r")\s+(?!(?:and|or|to)\b)(?=[A-Za-z0-9₹−(_])")
# a label that follows a number or a closing bracket with no punctuation between: a semicolon first
_LABEL_AFTER_VALUE = re.compile(r"(?<=[0-9)_])\s+(?=" + _CHAIN + r"(?::|\s))")
_BLANK = re.compile(r"_{3,}")
_UNDERLINE = r"\underline{\hspace{1.2em}}"
# a clock time with the word that follows it (a.m., p.m., AM, PM, hours); 1 or 2 digit hour
_TIME = re.compile(r"\b\d{1,2}:\d{2}(?:\s?(?:a\.m\.|p\.m\.|AM|PM|hours)(?![A-Za-z]))?")
# a stand-alone a.m. / p.m. / AM / PM
_AMPM = re.compile(r"(?<![\w.])(?:a\.m\.|p\.m\.|AM|PM)(?![\w])")
# words the converter would read as variables or numbers: kept as plain text
_PLAIN = re.compile(r"\b(?:12|24)-hour\b|\bNana ji(?:'s)?")
_ABBREV = re.compile(r"\b(?:min|sec|hr|hrs)\b\.?", re.IGNORECASE)
_HOLD = "HOLDZZ"


def house(text):
    """The plain text: part labels get their colon. Blanks stay as written (___)."""
    if not isinstance(text, str) or not text:
        return text
    text = _LABEL_AFTER_VALUE.sub("; ", text)
    text = _LABEL_BEFORE_NUMBER.sub(lambda m: m.group(1) + ": ", text)
    return text


def _letters(n):
    """0 -> A, 1 -> B, ..., 26 -> BA: the placeholder must be letters only so the converter reads it as a word."""
    s = ""
    n += 1
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


_store = []


def for_tex(text):
    """Only on the way into latex_wrap: every clock time and stand-alone a.m./p.m. becomes a plain-letter word."""
    if not isinstance(text, str) or not text:
        return text
    del _store[:]

    def hold(m):
        _store.append(m.group(0))
        return _HOLD + _letters(len(_store) - 1)

    text = _TIME.sub(hold, text)
    text = _PLAIN.sub(hold, text)
    return _AMPM.sub(hold, text)


def fix_blanks(tex):
    """After latex_wrap: put the held times back as plain text; every ___ becomes an underline."""
    if not isinstance(tex, str):
        return tex
    tex = _BLANK.sub(lambda m: _UNDERLINE, tex)
    for i in range(len(_store) - 1, -1, -1):
        tex = tex.replace(_HOLD + _letters(i), _store[i])
    # the converter reads the pronoun I and the article a or A before a number as maths variables: put them back
    tex = re.sub(r"\$I\$", "I", tex)
    return re.sub(r"\$([aA]) (\d)", r"\1 $\2", tex)


def abbreviations(text):
    """Strings that hold min / sec / hr: the authoring rule forbids them in a book question."""
    return _ABBREV.findall(text or "")
