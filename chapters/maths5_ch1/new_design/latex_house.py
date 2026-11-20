# -*- coding: utf-8 -*-
"""House style for the plain text of the book questions, applied around core/solutions/latex_convert.latex_wrap().

docs/karan-MD/LEARNING_PLAN_FIELD_CLEANUP_AND_LATEX 1.md, Part 2, section 7: do not ask the tokenizer to guess; write
the text in the shapes it converts cleanly. Found by converting this chapter's own text and reading every result:
  1. A part label glued to a number, "(a) 7,418", became ONE maths span, "$(a) 7,418$". A colon after a label that
     is followed by a number, "(a): 7,418", converts as "$(a)$: $7,418$". A label followed by a word is fine as is.
  2. A label that follows a number or a closing bracket with nothing between ("... + 3 (b): ...") is split off with
     a semicolon so it stays outside the previous number's span.
  3. Place-value letters Th, H, T, O were wrapped as maths variables, "$Th$". They are written as words instead:
     ten thousands, thousands, hundreds, tens, ones.
  4. "three 10s" / "four 1s" (token counts) became "$10s$": written "three tokens of 10".
  5. "Town 1 65,232" (a table row) became one span "$1 65,232$": written "Town 1: 65,232".
  6. A parenthesis that opens on a digit, "53,000 (11 numbers)", merged into the number's span: those few phrases
     are rewritten below.
  7. A blank written "___" ended up inside maths mode, where it is invalid: after conversion it becomes an
     underline, \\underline{\\hspace{1.2em}} (fix_blanks).
Only the book-question strings (question, steps, answer) go through this; nothing here changes a number."""
from __future__ import annotations

import re

_LABEL = r"\((?:[a-h]|iv|v|i{1,3})\)"
_CHAIN = _LABEL + r"(?:" + _LABEL + r")?"
# a part label (or a chain like "(b)(i)") followed by a number: add the colon
_LABEL_BEFORE_NUMBER = re.compile(
    r"(?<![\w)$])(?<!steps )(?<!step )(?<!part )(?<!of )(?<!from )(?<!in )(?<!and )(?<!or )(?<!to )(?<!with )"
    r"(" + _CHAIN + r")\s+(?!(?:and|or|to)\b)(?=[A-Za-z0-9₹−(])")
# (a label that starts a part gets the colon; a label mentioned inside a phrase, "repeat steps (b) and (c)", does not)
# a label that follows a number or a closing bracket with no punctuation between: a semicolon first
_LABEL_AFTER_VALUE = re.compile(r"(?<=[0-9)])\s+(?=" + _CHAIN + r"(?::|\s))")

_PLACE = [(re.compile(r"\bTTh\b"), "ten thousands"), (re.compile(r"\bTh\b"), "thousands"),
          (re.compile(r"\bH\b"), "hundreds"), (re.compile(r"\bT\b"), "tens"), (re.compile(r"\bO\b"), "ones")]
_TOKEN_COUNT = re.compile(r"\b(one|two|three|four|five|six|seven|eight|nine|ten|\d+) (\d[\d,]*)s\b")
# a numbered label that starts a sentence, "(3) A 1-digit number ...": colon too (a count like "Bicycle (2)" is not touched)
_NUM_LABEL = re.compile(r"(^|[.?!]\s)(\(\d\))\s+(?=[A-Za-z])")
_TOWN_ROW = re.compile(r"\bTown (\d+) (?=\d)")
_TOWN_BRACKET = re.compile(r"\bTown (\d+) \((\d[\d,]*)\)")
_CAP_PLACE = re.compile(r"(^|[.?!]\s+)(ten thousands|thousands|hundreds|tens|ones)\b")

# whole-phrase fixes (applied first)
PHRASES = {
    " and 53,000 (11 numbers)": " and 53,000: 11 numbers in all",
    "about 2,400 (16 pages with about 150 words each), a 4-digit number":
        "about 2,400, a 4-digit number: 16 pages with about 150 words each",
    "the two piles are equal (4 and 4, 3 and 3, 0 and 0)":
        "the two piles are equal, such as 4 and 4, 3 and 3 or 0 and 0",
    "in ₹7,934? 793 (b)": "in ₹7,934? The answer 793 is given. (b)",
}

_BLANK = re.compile(r"_{3,}")


def house(text):
    if not isinstance(text, str) or not text:
        return text
    for old, new in PHRASES.items():
        text = text.replace(old, new)
    text = _TOKEN_COUNT.sub(lambda m: "%s tokens of %s" % (m.group(1), m.group(2)), text)
    text = _TOWN_ROW.sub(lambda m: "Town %s: " % m.group(1), text)
    text = _TOWN_BRACKET.sub(lambda m: "Town %s: %s" % (m.group(1), m.group(2)), text)
    text = _LABEL_AFTER_VALUE.sub("; ", text)
    text = _LABEL_BEFORE_NUMBER.sub(lambda m: m.group(1) + ": ", text)
    text = _NUM_LABEL.sub(lambda m: m.group(1) + m.group(2) + ": ", text)
    for rx, word in _PLACE:
        text = rx.sub(word, text)
    # a place name that now starts a sentence takes a capital letter
    return _CAP_PLACE.sub(lambda m: m.group(1) + m.group(2)[0].upper() + m.group(2)[1:], text)


def fix_blanks(tex):
    """After latex_wrap: a blank ("___") is an underline, valid inside maths mode as well as outside it."""
    if not isinstance(tex, str):
        return tex
    return _BLANK.sub(lambda m: r"\underline{\hspace{1.2em}}", tex)
