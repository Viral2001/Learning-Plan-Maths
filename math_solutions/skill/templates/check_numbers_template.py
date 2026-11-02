"""Recompute every numeric answer used in a chapter's solutions.

Copy to <class>/<chapter>/source/check_numbers.py. One block per question:
compute the answer independently of the LaTeX, assert it, then print it so the
printed value can be compared with the .tex file.
"""
from math import sqrt, isclose
from fractions import Fraction

# Example: tangent PQ to a circle of radius 5 with OQ = 12  ->  PQ = sqrt(119)
pq = sqrt(12**2 - 5**2)
assert isclose(pq, sqrt(119))
print("Ex N.1 Q3  PQ^2 =", 12**2 - 5**2, "-> sqrt(119) =", round(pq, 4), "(D)")

# Use Fraction for exact rational answers
tp = Fraction(5 * 4, 3)
assert tp == Fraction(20, 3)
print("Example 3  TP =", tp)

print("ALL NUMERIC CHECKS PASSED")
