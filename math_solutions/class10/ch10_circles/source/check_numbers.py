"""Recompute every numeric answer used in the Class 10 Ch10 (Circles) solutions."""
from math import sqrt, isclose, cos, sin, radians, acos, degrees
from fractions import Fraction

# Ex 10.1 Q3: tangent PQ, r = 5, OQ = 12, OP perpendicular to PQ
pq = sqrt(12**2 - 5**2)
assert isclose(pq, sqrt(119))
print("10.1 Q3  PQ^2 =", 12**2 - 5**2, "-> sqrt(119) =", round(pq, 4), "(D)")

# Ex 10.2 Q1: tangent 24, OQ = 25
r = sqrt(25**2 - 24**2)
assert r == 7
print("10.2 Q1  r =", r, "(A)")

# Ex 10.2 Q2: angle POQ = 110 -> angle PTQ
ptq = 360 - 90 - 90 - 110
assert ptq == 70
print("10.2 Q2  PTQ =", ptq, "(B); supplementary check:", ptq + 110)

# Ex 10.2 Q3: angle APB = 80 -> angle POA
poa = 180 - 90 - 80 / 2
assert poa == 50
print("10.2 Q3  POA =", poa, "(A); supplementary check:", 2 * poa + 80)

# Ex 10.2 Q6: OA = 5, tangent = 4
r = sqrt(5**2 - 4**2)
assert r == 3
print("10.2 Q6  r =", r)

# Ex 10.2 Q7: radii 5 and 3
half = sqrt(5**2 - 3**2)
assert half == 4
print("10.2 Q7  half chord =", half, " chord =", 2 * half)

# Ex 10.2 Q12: r = 4, BD = 8, DC = 6
# Heron: s = x + 14, area = sqrt(48 x (x + 14)); area = 4 s = 4 (x + 14)
sol = [x for x in range(1, 100) if 48 * x * (x + 14) == 16 * (x + 14) ** 2]
assert sol == [7]
x = sol[0]
ab, ac, bc = x + 8, x + 6, 14
s = (ab + ac + bc) / 2
area = sqrt(s * (s - ab) * (s - ac) * (s - bc))
assert isclose(area, 0.5 * 4 * (ab + ac + bc)) and isclose(area, 84)
print("10.2 Q12 x =", x, " AB =", ab, " AC =", ac, " s =", s, " area =", area)
# inradius check from the coordinates used in the figure: A(5,12), B(14,0), C(0,0)
assert isclose(abs(12 * 6 - 5 * 4) / 13, 4)       # distance of O(6,4) from line AC
assert isclose(abs(12 * 6 - 5 * 4) / 13, 4)
assert isclose(sqrt((14 - 5) ** 2 + 12 ** 2), 15)  # AB from the coordinates
assert isclose(sqrt(5 ** 2 + 12 ** 2), 13)         # AC from the coordinates

# Example 3: chord PQ = 8, r = 5 -> TP
OR = sqrt(5**2 - 4**2)
TP = Fraction(5 * 4, 3)
assert OR == 3 and TP == Fraction(20, 3)
# Pythagoras route: x^2 = y^2 + 16, x^2 + 25 = (y + 3)^2 -> y = 16/3
y = Fraction(16, 3)
x2 = y**2 + 16
assert x2 == Fraction(400, 9)
assert x2 + 25 == (y + 3) ** 2
print("Ex 3     OR =", OR, " TP =", TP, " y =", y, " x^2 =", x2)

# Figure geometry sanity checks
# Q2 figure: tangents at P (110 deg) and Q (0 deg) meet at T = (r, r tan 55)
r = 2
T = (r, r * sin(radians(55)) / cos(radians(55)))
P = (r * cos(radians(110)), r * sin(radians(110)))
tp = ((T[0] - P[0]) ** 2 + (T[1] - P[1]) ** 2) ** 0.5
tq = T[1]
assert isclose(tp, tq)
print("Q2 fig   T =", [round(v, 3) for v in T], " TP = TQ =", round(tq, 3))
# Q10/Q3 figure: external point at distance d, half angle at P
d = 3.11
print("Q3 fig   OP for r=2, angle 80 =", round(2 / sin(radians(40)), 3))
print("ALL NUMERIC CHECKS PASSED")
