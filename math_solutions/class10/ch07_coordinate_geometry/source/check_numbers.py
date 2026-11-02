"""Check the numbers in the Ch 7 solution book.

1. Every \\dist{name}{x1}{y1}{x2}{y2}{value} call in latex/*.tex: the simplified
   value written in the .tex (for example 2\\sqrt{13} or 39) must equal the distance
   between the two points. (TeX computes the substituted rows itself with \\numexpr,
   so only this last, hand-typed value can be wrong.)
2. A few key answers of the chapter, recomputed independently.

Run:  python check_numbers.py
"""
import re
import glob
import os
from math import sqrt, isclose
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
TEX = sorted(glob.glob(os.path.join(HERE, "..", "latex", "*.tex")))


def read_args(s, i, n):
    """Read n brace-delimited arguments starting at s[i]; return (list, next index)."""
    out = []
    for _ in range(n):
        if i >= len(s) or s[i] != "{":
            return None, i
        depth, j = 0, i
        while j < len(s):
            if s[j] == "{":
                depth += 1
            elif s[j] == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        out.append(s[i + 1 : j])
        i = j + 1
    return out, i


def value_of(text):
    """Turn '2\\sqrt{13}\\approx 7.21', '3\\sqrt2' or '39' into a float."""
    text = text.split("\\approx")[0].strip()
    m = re.fullmatch(r"(\d*)\\sqrt\{?(\d+)\}?", text)
    if m:
        coeff = int(m.group(1)) if m.group(1) else 1
        return coeff * sqrt(int(m.group(2)))
    return float(text)


checked = 0
for path in TEX:
    s = open(path, encoding="utf-8").read()
    for m in re.finditer(r"\\dist(n?)\{", s):
        is_n = m.group(1) == "n"
        nargs = 5 if is_n else 6
        args, _ = read_args(s, m.end() - 1, nargs)
        if args is None:
            continue
        coords = args[1:5]
        if not all(re.fullmatch(r"-?\d+", c) for c in coords):
            continue  # the macro definition or a comment, not a real call
        x1, y1, x2, y2 = map(int, coords)
        d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        if not is_n:
            written = value_of(args[5])
            assert isclose(d, written, rel_tol=1e-9), (
                os.path.basename(path), args, d, written)
        checked += 1
print(f"{checked} distance rows checked against the .tex files")

# ---- key answers, recomputed independently of the LaTeX ----
def sq(a, b, c, d):
    return (c - a) ** 2 + (d - b) ** 2

# Example 1: P(3,2) Q(-2,-3) R(2,3): PQ^2=50, QR^2=52, PR^2=2 -> right angle at P
assert sq(3, 2, -2, -3) == 50 and sq(-2, -3, 2, 3) == 52 and sq(3, 2, 2, 3) == 2
assert 50 + 2 == 52

# Example 4: x - y = 2 is equidistant from (7,1) and (3,5)
for x in range(-3, 8):
    y = x - 2
    assert sq(7, 1, x, y) == sq(3, 5, x, y)

# Example 5: (0,9) equidistant from (6,5) and (-4,3)
assert sq(6, 5, 0, 9) == sq(-4, 3, 0, 9) == 52

# Example 6: (4,-3),(8,5) divided 3:1 -> (7,3)
assert (Fraction(3 * 8 + 1 * 4, 4), Fraction(3 * 5 + 1 * -3, 4)) == (7, 3)

# Example 7: (-4,6) divides A(-6,10),B(3,-8) in 2:7
m1, m2 = 2, 7
assert Fraction(m1 * 3 + m2 * -6, m1 + m2) == -4
assert Fraction(m1 * -8 + m2 * 10, m1 + m2) == 6

# Example 8: trisection points of A(2,-2), B(-7,4)
assert (Fraction(1 * -7 + 2 * 2, 3), Fraction(1 * 4 + 2 * -2, 3)) == (-1, 0)
assert (Fraction(2 * -7 + 1 * 2, 3), Fraction(2 * 4 + 1 * -2, 3)) == (-4, 2)

# Example 9: y-axis divides (5,-6),(-1,-4) in k:1 with k = 5, point (0,-13/3)
k = 5
assert Fraction(k * -1 + 5, k + 1) == 0
assert Fraction(k * -4 - 6, k + 1) == Fraction(-13, 3)

# Example 10: parallelogram A(6,1) B(8,2) C(9,4) D(p,3): p = 7
p = 7
assert Fraction(6 + 9, 2) == Fraction(8 + p, 2) and Fraction(1 + 4, 2) == Fraction(2 + 3, 2)

print("ALL NUMERIC CHECKS PASSED")
