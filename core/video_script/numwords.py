# -*- coding: utf-8 -*-
"""Read the numbers out of spoken English, the way the video scripts write them.

    "two thousand and forty-eight"  -> 2048
    "one lakh twenty thousand"      -> 120000
    "three point two five"          -> 3.25
    "three quarters", "two thirds"  -> 3 and 4, 2 and 3 (numerator and denominator, as separate values)
    "negative three", "minus three" -> 3 (the sign is dropped: the book guard compares sizes)

The book guard (check.py) uses these values to see whether a hook or a your-turn question reuses an
exercise's numbers. It errs towards finding numbers, never towards inventing them.
"""
from __future__ import annotations

import re

UNITS = {"zero": 0, "nought": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
         "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
         "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19}
TENS = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80,
        "ninety": 90}
SCALES = {"hundred": 100, "thousand": 1000, "lakh": 100000, "lakhs": 100000, "million": 1000000,
          "crore": 10000000, "crores": 10000000, "billion": 1000000000}
DENOMS = {"half": 2, "halves": 2, "third": 3, "thirds": 3, "quarter": 4, "quarters": 4, "fourth": 4,
          "fourths": 4, "fifth": 5, "fifths": 5, "sixth": 6, "sixths": 6, "seventh": 7, "sevenths": 7,
          "eighth": 8, "eighths": 8, "ninth": 9, "ninths": 9, "tenth": 10, "tenths": 10, "eleventh": 11,
          "elevenths": 11, "twelfth": 12, "twelfths": 12, "hundredth": 100, "hundredths": 100}
NUMBER_WORDS = set(UNITS) | set(TENS) | set(SCALES)


def _tokens(text: str):
    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace("[chintu]", " ")
    return re.findall(r"[a-z]+", text.lower().replace("-", " "))


def _value(words):
    """Value of a run of cardinal words (no 'and', no 'point')."""
    total, current = 0, 0
    for w in words:
        if w in UNITS:
            current += UNITS[w]
        elif w in TENS:
            current += TENS[w]
        elif w == "hundred":
            current = (current or 1) * 100
        elif w in SCALES:
            total += (current or 1) * SCALES[w]
            current = 0
    return total + current


def numbers(text: str):
    """All numbers said in `text`, in order, as ints or floats."""
    toks = _tokens(text)
    out, i, n = [], 0, len(toks)
    while i < n:
        if toks[i] not in NUMBER_WORDS:
            i += 1
            continue
        run = []
        while i < n and (toks[i] in NUMBER_WORDS or (toks[i] == "and" and run and i + 1 < n
                                                        and toks[i + 1] in NUMBER_WORDS
                                                        and run[-1] in SCALES)):
            if toks[i] != "and":
                run.append(toks[i])
            i += 1
        # "one two three" said as a list is three numbers, not 6: split a run where two units follow each other
        pieces, cur = [], []
        for w in run:
            if cur and (w in UNITS or w in TENS) and (cur[-1] in UNITS or (cur[-1] in TENS and w in TENS)):
                pieces.append(cur)
                cur = []
            cur.append(w)
        if cur:
            pieces.append(cur)
        vals = [_value(p) for p in pieces]
        # decimals: "three point two five"
        if i < n and toks[i] == "point" and vals:
            j = i + 1
            digits = []
            while j < n and toks[j] in UNITS and UNITS[toks[j]] < 10:
                digits.append(str(UNITS[toks[j]]))
                j += 1
            if digits:
                vals[-1] = float(f"{vals[-1]}.{''.join(digits)}")
                i = j
        # fractions: "three quarters"
        if i < n and toks[i] in DENOMS and vals:
            out.extend(vals)
            out.append(DENOMS[toks[i]])
            i += 1
            continue
        out.extend(vals)
    return out


def digit_numbers(text: str):
    """Numbers written with digits (maths_rules, on_screen): 1,20,000 and 1.25 and 3/4 read as 3 and 4."""
    vals = []
    for m in re.finditer(r"\d[\d,]*(?:\.\d+)?", text):
        s = m.group(0).rstrip(",")
        if re.fullmatch(r"\d{1,3}(,\d{2,3})+(\.\d+)?", s):
            s = s.replace(",", "")
        elif "," in s:
            for part in s.split(","):
                if part:
                    vals.append(float(part) if "." in part else int(part))
            continue
        vals.append(float(s) if "." in s else int(s))
    return vals


if __name__ == "__main__":
    cases = {
        "two thousand and forty-eight": [2048],
        "one lakh twenty thousand": [120000],
        "three point two five": [3.25],
        "three quarters of sixty": [3, 4, 60],
        "negative three plus seven": [3, 7],
        "a hundred and forty percent of forty": [140, 40],
        "five hundred and seventeen thousand six hundred and forty-seven": [517647],
        "one, two, three": [1, 2, 3],
        "twenty-five out of a hundred": [25, 100],
        "nought point eight times seventy-five": [0.8, 75],
    }
    bad = 0
    for text, want in cases.items():
        got = numbers(text)
        if got != want:
            bad += 1
            print("FAIL", repr(text), got, "want", want)
    assert digit_numbers("1,20,000 and 1.25 and 3/4") == [120000, 1.25, 3, 4], digit_numbers("1,20,000 and 1.25 and 3/4")
    print("numwords self-test:", "OK" if not bad else f"{bad} failures")
