# -*- coding: utf-8 -*-
"""Topics T3, T4 and T5 (module M2: Smart Ways to Divide): Mental Strategies for Division, Susie's Farm (taking away groups,
the biggest group that fits, the remainder rule) and Kalpavruksha Coconut Oil (bigger numbers).
Every teaching concept has one worked example with the plan's own numbers (practice values); every book question is an FIO
item of its topic's DOER, in the book's order. The working is written with division_steps.py, which asserts every number.
A division with a remainder is never written as one chain."""
from topics_common import A, DOER, FIO, TOPIC, WE
import division_steps as D

TOPICS = []
MINUS = D.MINUS


def _one(n, d, a, b, sign="+"):
    """One line of splitting n = a + b (or a − b), for the list questions."""
    assert (a + b if sign == "+" else a - b) == n and a % d == 0 and b % d == 0
    x, y = a // d, b // d
    z = x + y if sign == "+" else x - y
    assert z * d == n
    s = "+" if sign == "+" else MINUS
    return ("%d ÷ %d: %d = %d %s %d, %d ÷ %d = %d and %d ÷ %d = %d, so %d %s %d = %d." %
            (n, d, n, a, s, b, a, d, x, b, d, y, x, s, y, z)), z


# ============================== T3 Mental Strategies for Division ==========================================
_s_five, _z_five = [], []
for _n, _d, _a, _b in [(906, 3, 900, 6), (2412, 6, 2400, 12), (3515, 5, 3500, 15), (4812, 4, 4800, 12), (6309, 3, 6300, 9)]:
    _line, _z = _one(_n, _d, _a, _b)
    _s_five.append(_line)
    _z_five.append(_z)

_try = []
for _i, (_n, _d, _a, _b, _sg) in enumerate([(64, 4, 40, 24, "+"), (265, 5, 250, 15, "+"), (1560, 8, 1600, 40, "-"),
                                          (4824, 24, 4800, 24, "+")], 1):
    _line, _z = _one(_n, _d, _a, _b, _sg)
    _try.append("(%d): %s" % (_i, _line))
    _try.append("Check: %d × %d = %d." % (_d, _z, _n))
    assert _d * _z == _n

_h5, _r5 = D.halve(168, 3)
_h6, _r6 = D.halve(144, 2)
_ahs = []
_a_h = [("(a)", 256, 4, "halve"), ("(b)", 545, 5, (500, 45, "+")), ("(c)", 147, 7, (140, 7, "+")),
        ("(d)", 1212, 6, (1200, 12, "+")), ("(e)", 648, 12, (600, 48, "+")), ("(f)", 9648, 48, (9600, 48, "+")),
        ("(g)", 775, 25, (750, 25, "+")), ("(h)", 796, 4, (800, 4, "-"))]
_ans_ah = []
for _lab, _n, _d, _how in _a_h:
    if _how == "halve":
        _hs, _z = D.halve(_n, 2)
        _ahs.append("%s: %d ÷ %d: halve twice, %d and %d, so %d ÷ %d = %d." % (_lab, _n, _d, _n // 2, _n // 4, _n, _d, _z))
    else:
        _a, _b, _sg = _how
        _line, _z = _one(_n, _d, _a, _b, _sg)
        _ahs.append("%s: %s" % (_lab, _line))
    assert _d * _z == _n
    _ans_ah.append("%s: %d" % (_lab, _z))

TOPICS.append(TOPIC(
    "T3", "M2", "Mental Strategies for Division", ["Mental Strategies for Division"], "Apply",
    "Students divide in the head: split the dividend into convenient parts, round up and take the extra away, or halve "
    "again and again for the divisors 4 and 8.",
    "A hard division can often be done in the head. Split the number into parts the divisor divides easily, or round up "
    "to an easy number and take the extra away, or halve again and again when the divisor is 4 or 8.",
    [A("T3.C1", "Split the Number into Convenient Parts", "Apply",
       "Students split a dividend into convenient parts that the divisor divides easily, divide each part, and add the "
       "answers to find the quotient.",
       textbook=["I can split the number into convenient parts."],
       teach=["Predict first: 2856 ÷ 7 looks hard. Can you cut 2856 into two parts that 7 divides easily?",
              "Split 2856 into 2800 + 56. Both parts are easy to divide by 7.",
              "2800 ÷ 7 = 400, because 28 ÷ 7 = 4 and there are two zeros. And 56 ÷ 7 = 8.",
              "Put the answers together: 400 + 8 = 408. So 2856 ÷ 7 = 408.",
              "Check the answer: 7 × 408 = 2856.",
              "Rule: split the number into parts the divisor divides easily, divide each part, then add the answers."],
       examples=[WE("Find 2856 ÷ 7 in the head by splitting the number into convenient parts (practice values).",
                    ["Look for parts that 7 divides easily. 2856 is close to 2800, and 28 is a table fact of 7."]
                    + D.split(2856, 7, 2800, 56)[0],
                    "2856 ÷ 7 = 408")],
       key_terms=["split", "convenient parts", "dividend"], misconceptions=["M_BAD_SPLIT"], minutes=5),
     A("T3.C2", "Round Up, Divide, Take Away", "Apply",
       "Students divide by rounding the dividend up to an easy number, dividing it, and taking the share of the extra part "
       "away from the answer.",
       textbook=["I can do it in a different way."],
       teach=["Predict first: 2994 is just 6 less than 3000. How could 3000 help you find 2994 ÷ 3?",
              "Write 2994 = 3000 − 6. The number 3000 is easy to divide by 3.",
              "3000 ÷ 3 = 1000, and the extra part is 6 ÷ 3 = 2.",
              "The 6 was added to reach 3000, so take its share away: 1000 − 2 = 998.",
              "Check the answer: 3 × 998 = 2994.",
              "Rule: round up to an easy number, divide, then take away the share of the extra."],
       examples=[WE("Find 2994 ÷ 3 in the head by rounding up (practice values).",
                    ["2994 is close to the easy number 3000, and 3000 is 6 more than 2994."]
                    + D.split(2994, 3, 3000, 6, "-")[0],
                    "2994 ÷ 3 = 998")],
       key_terms=["round up", "take away", "extra"], misconceptions=["M_ROUND_WRONG"], minutes=5),
     A("T3.C3", "Halve Again and Again", "Apply",
       "Students divide a number by 4 or by 8 by halving it two or three times, and check the answer by multiplying.",
       textbook=["To divide by 4, I can halve twice."],
       teach=["Predict first: how can you divide 264 by 4 using only halves?",
              "Dividing by 4 is the same as halving twice, because 2 × 2 = 4.",
              "Half of 264 is 132. Half of 132 is 66. So 264 ÷ 4 = 66.",
              "Check the answer: 4 × 66 = 264.",
              "Dividing by 8 is halving three times, because 2 × 2 × 2 = 8. For example 216 ÷ 8: halves 108, 54 and 27.",
              "Rule: halve once to divide by 2, twice to divide by 4 and three times to divide by 8."],
       examples=[WE("Find 264 ÷ 4 in the head by halving twice (practice values).",
                    ["Dividing by 4 is halving twice, because 2 × 2 = 4."] + D.halve(264, 2)[0]
                    + ["So 264 ÷ 4 = 66."],
                    "264 ÷ 4 = 66")],
       key_terms=["halve", "halving", "half"], minutes=5),
     DOER("T3.C4", "Practice: Smart Splitter", "smart_splitter", "Apply",
          "Students use smart mental methods, split, round up or halve, to solve the book's divisions, give examples of "
          "their own, and check each answer by multiplying.",
          ["Split the number into parts the divisor divides easily.",
           "Round up to an easy number, then take the extra away.",
           "Halve again and again for the divisors 4 and 8."],
          items=[
              FIO("ms.ex1", "Example 2: 1248 ÷ 6 by splitting",
                  "Observe the division carefully. 1248 ÷ 6. I can split the number into convenient parts.",
                  ["1248 = 1200 + 48 is a good split, because 6 divides both parts easily."]
                  + D.split(1248, 6, 1200, 48)[0][1:],
                  "1248 ÷ 6 = 208", kind="example"),
              FIO("ms.ex2", "Example 3: 1992 ÷ 4 by rounding",
                  "1992 ÷ 4. I can do it in a different way.",
                  ["1992 is just 8 less than 2000, so use 2000."] + D.split(1992, 4, 2000, 8, "-")[0],
                  "1992 ÷ 4 = 498", kind="example"),
              FIO("ms.ex3", "Example 4: 128 ÷ 4 by halving",
                  "128 ÷ 4. To divide by 4, I can halve twice.",
                  ["Dividing by 4 is halving twice, because 2 × 2 = 4."] + D.halve(128, 2)[0]
                  + ["So 128 ÷ 4 = 32."],
                  "128 ÷ 4 = 32", kind="example"),
              FIO("ms.five", "Mental Strategies: five examples of splitting",
                  "Can you give 5 such examples where you can split the number conveniently?",
                  ["Choose a divisor, then split the number into a round part and a small part that the divisor divides "
                   "easily."] + _s_five + ["Many other examples work. Check each answer by multiplying."],
                  "Sample answer: 906 ÷ 3 = 302, 2412 ÷ 6 = 402, 3515 ÷ 5 = 703, 4812 ÷ 4 = 1203, 6309 ÷ 3 = 2103. Your "
                  "answer may differ",
                  kind="prompt"),
              FIO("ms.halving", "Mental Strategies: when repeated halving works",
                  "For which other divisors and dividend might this strategy of repeated halving work?",
                  ["Halving twice divides by 4. Halving three times divides by 8. Halving four times divides by 16, "
                   "because 2 × 2 × 2 × 2 = 16.",
                   "So repeated halving works for the divisors 2, 4, 8 and 16.",
                   "The dividend must be able to be halved that many times with whole-number halves.",
                   "Example: 96 ÷ 8 by halving three times: 48, 24, 12, so 96 ÷ 8 = 12. Check: 8 × 12 = 96.",
                   "Example: 240 ÷ 16 by halving four times: 120, 60, 30, 15, so 240 ÷ 16 = 15. Check: 16 × 15 = 240.",
                   "It does not work for a divisor like 5 or 6, because halving does not divide by 5 or by 6."],
                  "Sample answer: the divisors 2, 4, 8 and 16, with a dividend that halves that many times, such as 96 ÷ 8 "
                  "= 12. Your answer may differ",
                  kind="prompt"),
              FIO("try.split", "Try It!: splitting, Q1 to Q4",
                  "Try It! Split the number into two parts, divide each part, and put the answers together. (1): 64 ÷ 4; "
                  "(2): 265 ÷ 5; (3): 1560 ÷ 8; (4): 4824 ÷ 24. The boxes show a plus sign for (1), (2) and (4) and a "
                  "minus sign for (3).",
                  _try + ["Other splits work too, for example 64 = 32 + 32."],
                  "(1): 16; (2): 53; (3): 195; (4): 201. Your split may differ",
                  kind="exercise",
                  q_figure="Four box diagrams: in each the number splits into two empty boxes joined by a plus sign (a minus "
                           "sign in the third), each part has an arrow marked with the divisor to a new empty box, and the "
                           "new boxes are joined by the same sign to a last empty box."),
              FIO("try.halve", "Try It!: halving, Q5 and Q6",
                  "Try It! (5): 168 ÷ 8, halve 168, then halve the answer, then halve again. (6): 144 ÷ 4, halve 144, then "
                  "halve the answer.",
                  ["(5): dividing by 8 is halving three times, because 2 × 2 × 2 = 8."] + [
                      "(5): " + s for s in _h5[:-1]] + ["(5): so 168 ÷ 8 = %d." % _r5, "(5): " + _h5[-1],
                      "(6): dividing by 4 is halving twice, because 2 × 2 = 4."] + ["(6): " + s for s in _h6[:-1]]
                  + ["(6): so 144 ÷ 4 = %d." % _r6, "(6): " + _h6[-1]],
                  "(5): 21; (6): 36", kind="exercise",
                  q_figure="Two chains of boxes: for (5) the words Halve 168 lead to a box, then Halve with a blank to a "
                           "box, then Halve with a blank to a box; for (6) the words Halve 144 lead to a box, then Halve "
                           "with a blank to a box."),
              FIO("ls.a_h", "Let Us Solve (mental strategies): (a) to (h)",
                  "Solve the following problems using strategies used in the previous question. (a): 256 ÷ 4; (b): 545 ÷ 5; "
                  "(c): 147 ÷ 7; (d): 1212 ÷ 6; (e): 648 ÷ 12; (f): 9648 ÷ 48; (g): 775 ÷ 25; (h): 796 ÷ 4.",
                  _ahs + ["Other strategies work too. Check each answer by multiplying."],
                  "; ".join(_ans_ah), kind="exercise")],
          misconceptions=["M_BAD_SPLIT", "M_ROUND_WRONG"])],
    key_terms=["split", "round up", "halve", "mental"]))

# ============================== T4 Susie's Farm: Taking Away Groups =========================================
_sf1 = D.pq(582, 6, [20, 20, 20, 20, 10, 7])[0]
_sf1b = ["Sunitha's way: take away the biggest groups that fit. 6 × 90 = 540 is less than 582, so take away 90 groups: "
         "582 − 540 = 42.",
         "Then take away 7 groups of 6: 6 × 7 = 42, and 42 − 42 = 0.",
         "90 + 7 = 97. Both ways give 97 coconuts. Sunitha's way takes 2 steps and Susie's way takes 6 steps.",
         "Estimate check: 6 × 100 = 600 is more than 582, so each customer gets less than 100 coconuts."]
assert 6 * 90 == 540 and 582 - 540 == 42 and 6 * 7 == 42 and 90 + 7 == 97 and 6 * 100 == 600

_bags = D.pq(97, 25, [3])[0]
_q2 = D.pq(535, 25, [20, 1])[0]
_s726 = D.pq(726, 4, [100, 80, 1])[0]
_s902 = D.pq(902, 16, [50, 6])[0]
assert 4 * 200 == 800 > 726 and 16 * 50 == 800 and 16 * 60 == 960 > 902 and 4 * 181 == 724 and 16 * 56 == 896
_ls1q5, _ans1 = [], []
for _lab, _n, _d in [("(a)", 887, 3), ("(b)", 283, 8), ("(c)", 745, 5), ("(d)", 767, 26), ("(e)", 530, 41), ("(f)", 888, 67)]:
    _t, _q, _r = D.nqdr(_n, _d)
    _ls1q5.append("%s: %s" % (_lab, _t))
    _ans1.append("%s: %d remainder %d" % (_lab, _q, _r))
_ls2q4, _ans2 = [], []
for _lab, _n, _d in [("(a)", 9045, 5), ("(b)", 1034, 4), ("(c)", 2504, 7), ("(d)", 8900, 15), ("(e)", 9876, 32),
                     ("(f)", 7506, 24)]:
    _t, _q, _r = D.nqdr(_n, _d, True)
    _ls2q4.append("%s: %s" % (_lab, _t))
    _ans2.append("%s: %s remainder %d" % (_lab, "{:,}".format(_q), _r))

TOPICS.append(TOPIC(
    "T4", "M2", "Susie's Farm: Taking Away Groups", ["Susie's Farm in Kerala", "Let Us Learn to Divide"], "Apply",
    "Students divide by taking away groups of the divisor, choose the biggest group that fits, and write the remainder rule "
    "N = D × Q + R with the remainder less than the divisor.",
    "Susie takes away many small groups of the divisor and Sunitha takes away the biggest groups that fit. Both add up "
    "the groups to get the quotient. What is left is the remainder, and N = D × Q + R.",
    [A("T4.C1", "Take Away Groups of the Divisor", "Apply",
       "Students divide a number by taking away groups of the divisor again and again, and add the group counts to find "
       "the quotient.",
       textbook=["Susie and Sunitha have a large coconut farm and they have harvested 1,117 coconuts in April."],
       teach=["Predict first: Susie packs 378 coconuts into groups of 6. If she takes away 20 groups of 6 each time, how "
              "many times can she do it?",
              "She takes away 20 groups of 6, which is 6 × 20 = 120 coconuts. She does it again and again until the "
              "coconuts run out.",
              "378 − 120 = 258, then 258 − 120 = 138, then 138 − 120 = 18. Now 3 groups of 6 take away the last 18.",
              "The groups taken away: 20 + 20 + 20 + 3 = 63. So 378 ÷ 6 = 63.",
              "Check the answer: 6 × 63 = 378.",
              "Rule: take away groups of the divisor, add up how many groups you took, and that is the quotient."],
       examples=[WE("Susie packs 378 coconuts into groups of 6 (practice values). Find 378 ÷ 6 by taking away groups.",
                    D.pq(378, 6, [20, 20, 20, 3])[0], "378 ÷ 6 = 63")],
       ncert=["sf.text"], key_terms=["groups", "divisor", "quotient", "partial quotients"],
       misconceptions=["M_TOO_BIG_GROUP"], minutes=6),
     A("T4.C2", "Choose the Biggest Group That Fits", "Apply",
       "Students estimate a quotient first, then divide by taking away the biggest tens or hundreds of groups that fit, "
       "in fewer steps.",
       textbook=["Estimate the answer first. Do you realise that each customer will likely get less than 100 coconuts?",
                 "Do you think Sunitha's method is better? Discuss which one you would prefer and why."],
       teach=["Predict first: for 861 ÷ 7, is the answer more or less than 100? Is it more or less than 200?",
              "Estimate first: 7 × 100 = 700 is less than 861 and 7 × 200 = 1400 is more, so the answer is between 100 "
              "and 200.",
              "Take away the biggest group that fits. 100 groups of 7 is 700, and 861 − 700 = 161. Then 20 groups of 7 is "
              "140, and 161 − 140 = 21. Then 3 groups of 7 is 21, and 21 − 21 = 0.",
              "100 + 20 + 3 = 123, in only 3 steps. So 861 ÷ 7 = 123.",
              "A group that is too big cannot be taken away: 200 groups of 7 is 1400, which is more than 861.",
              "Rule: estimate first, then take away the biggest tens or hundreds of groups that fit."],
       examples=[WE("Find 861 ÷ 7 by estimating first and taking away the biggest groups that fit (practice values).",
                    ["Estimate: 7 × 100 = 700 and 7 × 200 = 1400, so the answer is between 100 and 200.",
                     "200 groups are too big, because 1400 is more than 861."] + D.pq(861, 7, [100, 20, 3])[0],
                    "861 ÷ 7 = 123")],
       ncert=["sf.estimate", "sf.discuss"], key_terms=["estimate", "biggest group", "multiples of ten"],
       misconceptions=["M_TOO_BIG_GROUP"], minutes=6),
     A("T4.C3", "The Remainder Rule", "Understand",
       "Students find the remainder of a division and write the check N = D × Q + R, with the remainder less than the "
       "divisor.",
       textbook=["Sometimes, the divisor (D) does not completely divide the dividend (N) and leaves a remainder (R).",
                 "N = D × Q + R"],
       teach=["Predict first: for 487 ÷ 9, after you take away all the groups of 9 that fit, will anything be left over?",
              "Take away 50 groups of 9, which is 450: 487 − 450 = 37. Take away 4 groups of 9, which is 36: 37 − 36 = 1.",
              "The 1 that is left is smaller than 9, so no more groups of 9 can be taken away. It is the remainder (R).",
              "The quotient is 50 + 4 = 54, so 487 ÷ 9: quotient 54, remainder 1.",
              "Check with N = D × Q + R: 9 × 54 + 1 = 487.",
              "Rule: N = D × Q + R, and the remainder is always less than the divisor."],
       examples=[WE("Find 487 ÷ 9 and check it with N = D × Q + R (practice values).",
                    D.pq(487, 9, [50, 4])[0] + ["The remainder 1 is less than the divisor 9, as it must be."],
                    "Quotient 54, remainder 1, and 487 = 9 × 54 + 1")],
       ncert=["ld.rule"], key_terms=["remainder", "rule", "dividend", "quotient"],
       misconceptions=["M_REMAINDER_BIG"], minutes=6),
     DOER("T4.C4", "Practice: Take Away Groups", "take_away_groups", "Apply",
          "Students divide by taking away groups, find the quotient and the remainder, and check each answer with "
          "N = D × Q + R.",
          ["Take away groups of the divisor, the biggest that fit.",
           "Add the groups to get the quotient. What is left is the remainder.",
           "Check: N = D × Q + R, and the remainder is less than the divisor."],
          items=[
              FIO("sf.q1", "Example 5: 582 coconuts to 6 customers",
                  "Susie and Sunitha have a large coconut farm and they have harvested 1,117 coconuts in April. They sold "
                  "582 coconuts equally to 6 regular customers. How many coconuts did each customer get? They sold 582 ÷ 6 "
                  "coconuts to each customer.",
                  ["Susie's way: take away groups of 6 again and again."] + _sf1 + _sf1b,
                  "97 coconuts for each customer", kind="example",
                  s_figure="Two ways side by side: Susie's six take-away steps ending in 97 and Sunitha's two steps ending "
                           "in 97."),
              FIO("sf.bags", "Example 6: bags for 97 coconuts",
                  "Each bag can hold 25 coconuts. How many bags would be needed to pack 97 coconuts?",
                  ["Each bag holds 25 coconuts, so divide 97 by 25."] + _bags
                  + ["The 3 full bags hold 75 coconuts. The 22 coconuts left need one more bag.",
                     "So 3 + 1 = 4 bags are needed."],
                  "4 bags", kind="example"),
              FIO("sf.q2", "Example 7: 535 coconuts left",
                  "They pack the remaining coconuts for drying and extracting oil. They can pack 25 coconuts in each bag. "
                  "How many bags will they need to pack the remaining coconuts? The number of coconuts left after selling "
                  "582 coconuts is 1117 − 582 = 535. The number of bags needed is 535 ÷ 25. Guess the number of bags needed. "
                  "Use the strategies learnt.",
                  ["The coconuts left after selling 582: 1117 − 582 = 535.",
                   "Guess first: 25 × 20 = 500 and 25 × 30 = 750, so the answer is between 20 and 30.",
                   "30 groups are too big, because 750 is more than 535."] + _q2
                  + ["21 bags are full. The 10 coconuts left need 1 more bag.",
                     "So 21 + 1 = 22 bags are needed."],
                  "22 bags", kind="example"),
              FIO("ld.726", "Let Us Learn to Divide: 726 ÷ 4",
                  "Let Us Learn to Divide. Find 726 ÷ 4 by taking away groups of 4. The first part of the quotient is 100: "
                  "take away ___ and 326 is left. Take away 320, which is ___ groups of 4, and 6 is left. Take away ___, "
                  "which is ___ group of 4, and 2 is left. Could we have written 200 here?",
                  _s726 + ["Could we have written 200 as the first part? 4 × 200 = 800, which is more than 726, so no."],
                  "The blanks are 400, 80, 4 and 1: quotient 181, remainder 2", kind="prompt"),
              FIO("ld.902", "Let Us Learn to Divide: 902 ÷ 16",
                  "902 ÷ 16. Take away groups of 16: the quotient parts are ___ + 6. Take away 800, then take away 96, and 6 "
                  "is left. What should we write here so that we get a number close to 902 but less than it? Could we have "
                  "multiplied 16 by a larger tens?",
                  _s902 + ["Why 50? 16 × 50 = 800 is close to 902 and less than it. 16 × 60 = 960 is more than 902, so a "
                           "larger tens cannot be used."],
                  "The blank is 50: quotient 56, remainder 6", kind="prompt"),
              FIO("ld.relation", "Let Us Learn to Divide: the remainder rule",
                  "Sometimes, the divisor (D) does not completely divide the dividend (N) and leaves a remainder (R). What is "
                  "the relationship between the dividend (N) and divisor (D), quotient (Q), and remainder (R)? Try to find "
                  "out! Is 726 = 4 × 181? Yes/No. So, 726 = 4 × 181 + ___. Is 902 = 16 × 56? Yes/No. So, 902 = 16 × 56 + ___.",
                  ["Check 726 and 4 × 181: 4 × 181 = 724, which is not 726, so the answer is No.",
                   "726 is 2 more than 724, so 726 = 4 × 181 + 2.",
                   "Check 902 and 16 × 56: 16 × 56 = 896, which is not 902, so the answer is No.",
                   "902 is 6 more than 896, so 902 = 16 × 56 + 6.",
                   "The relationship: Dividend (N) = Divisor (D) × Quotient (Q) + Remainder (R), and the remainder is less "
                   "than the divisor."],
                  "No, and No: 726 = 4 × 181 + 2 and 902 = 16 × 56 + 6, so N = D × Q + R", kind="prompt"),
              FIO("ls1.q5", "Let Us Solve (remainders), Q5",
                  "Identify the remainder, if any. Check if N = D × Q + R. (a): 887 ÷ 3; (b): 283 ÷ 8; (c): 745 ÷ 5; (d): "
                  "767 ÷ 26; (e): 530 ÷ 41; (f): 888 ÷ 67.",
                  ["Divide each number by taking away the biggest groups that fit, then check with N = D × Q + R."]
                  + _ls1q5,
                  "; ".join(_ans1), kind="exercise"),
              FIO("ls2.q4", "Let Us Solve (remainders), Q4",
                  "Solve the following and identify the remainder, if any. Check whether N = D × Q + R in each case. (a): "
                  "9,045 ÷ 5; (b): 1,034 ÷ 4; (c): 2,504 ÷ 7; (d): 8,900 ÷ 15; (e): 9,876 ÷ 32; (f): 7,506 ÷ 24.",
                  ["Divide each number by taking away the biggest groups that fit, then check with N = D × Q + R."]
                  + _ls2q4,
                  "; ".join(_ans2), kind="exercise")],
          misconceptions=["M_TOO_BIG_GROUP", "M_REMAINDER_BIG"])],
    key_terms=["groups", "divisor", "remainder", "quotient"]))

# ============================== T5 Kalpavruksha Coconut Oil: Bigger Numbers =================================
_oil1 = D.pq(4376, 8, [200, 200, 100, 40, 7])[0]
_oil1b = ["Sunitha's way: 8 × 500 = 4000, and 4376 − 4000 = 376. Then 8 × 40 = 320, and 376 − 320 = 56. Then 8 × 7 = 56, "
          "and 56 − 56 = 0.",
          "500 + 40 + 7 = 547, in 3 steps. Both ways give 547 litres."]
assert 8 * 500 == 4000 and 4376 - 4000 == 376 and 8 * 40 == 320 and 376 - 320 == 56 and 500 + 40 + 7 == 547
assert 547 * 100 == 54700 and 547 * 70 == 38290 and 547 * 5 == 2735 and 54700 + 38290 + 2735 == 95725 == 547 * 175
_husk = D.pq(9913, 23, [400, 30, 1])[0]
assert 23 * 400 == 9200 and 23 * 500 == 11500 and 23 * 300 == 6900
_tender = D.pq(8890, 35, [200, 50, 4])[0]
assert 254 * 20 == 5080 and 8890 - 5080 == 3810 and 254 * 15 == 3810 and 35 - 20 == 15

TOPICS.append(TOPIC(
    "T5", "M2", "Kalpavruksha Coconut Oil: Bigger Numbers", ["Kalpavruksha Coconut Oil"], "Apply",
    "Students divide bigger numbers by taking away hundreds, tens and ones groups, and use the quotient in the next step "
    "of a problem.",
    "Bigger numbers are divided the same way: take away hundreds of groups, then tens, then ones, always the biggest that "
    "fits. The quotient is then used in the next step, such as the earnings from the oil.",
    [A("T5.C1", "Hundreds, Tens and Ones Groups", "Apply",
       "Students divide a number of thousands by a one-digit or two-digit divisor by taking away hundreds, tens and ones "
       "groups, and check by multiplying.",
       textbook=["In a particular year, Susie and Sunitha used 4376 coconuts for extracting coconut oil. They can extract "
                 "1 litre of oil from 8 coconuts.",
                 "Let us take away maximum groups of 23 in multiples of hundreds and tens.",
                 "What would happen if 23 is multiplied by 300 or 500?"],
       teach=["Predict first: for 6534 ÷ 18, which groups can you take away first: hundreds of groups, tens of groups or "
              "ones?",
              "Start with the biggest. 18 × 300 = 5400 is less than 6534, and 18 × 400 = 7200 is more, so take away 300 "
              "groups: 6534 − 5400 = 1134.",
              "Next, 18 × 60 = 1080 fits in 1134: 1134 − 1080 = 54.",
              "Last, 18 × 3 = 54: 54 − 54 = 0.",
              "300 + 60 + 3 = 363, so 6534 ÷ 18 = 363. Check: 363 × 18 = 6534.",
              "Rule: take away hundreds of groups, then tens, then ones, always the biggest that fits."],
       examples=[WE("Find 6534 ÷ 18 by taking away hundreds, tens and ones groups (practice values).",
                    ["Try the hundreds first: 18 × 400 = 7200 is more than 6534, so 400 groups are too big. 18 × 300 = 5400 "
                     "fits."] + D.pq(6534, 18, [300, 60, 3])[0],
                    "6534 ÷ 18 = 363")],
       ncert=["oil.text", "oil.hint"], key_terms=["hundreds", "tens", "ones", "groups"],
       misconceptions=["M_TOO_BIG_GROUP"], minutes=7),
     DOER("T5.C2", "Practice: Coconut Oil and Husk", None, "Apply",
          "Students solve the coconut oil, husk and tender coconut problems by dividing, and use the quotient to find the "
          "earnings and the extra money.",
          ["Take away the biggest groups that fit, from hundreds down to ones.",
           "Check every quotient by multiplying.",
           "Use the quotient in the next step of the problem."],
          items=[
              FIO("oil.q1", "Example 8: oil from 4376 coconuts",
                  "In a particular year, Susie and Sunitha used 4376 coconuts for extracting coconut oil. They can extract "
                  "1 litre of oil from 8 coconuts. What quantity of oil were they able to extract? They would get 4376 ÷ 8 "
                  "litres of coconut oil.",
                  ["Susie's way: take away groups of 8."] + _oil1 + _oil1b + ["So they extracted 547 litres of oil."],
                  "547 litres of oil", kind="example"),
              FIO("oil.earn", "Kalpavruksha Coconut Oil: earnings from the oil",
                  "How much will they earn if they sell the oil at ₹175 for 1 litre? They will earn ₹547 × 175. Find out.",
                  ["Money earned = litres × price for 1 litre = 547 × 175.",
                   "Split 175 into 100 + 70 + 5.",
                   "547 × 100 = 54700.",
                   "547 × 70 = 38290.",
                   "547 × 5 = 2735.",
                   "Add the three parts: 54700 + 38290 + 2735 = 95725.",
                   "Check by estimating: 500 × 200 = 100000, and 95725 is close to it."],
                  "₹95725", kind="prompt",
                  q_figure="A column multiplication with the columns hundreds, tens and ones: 547 on top, × 175 below, and "
                           "two empty lines for the working.",
                  s_figure="The same column multiplication with the three partial products 2735, 38290 and 54700 and the "
                           "total 95725."),
              FIO("oil.husk", "Example 9: coconut husk",
                  "Coconut husk is used for making coir. Coir is a natural fibre used in gardening, farming, boat making, "
                  "and making decorative items. Susie and Sunitha's farm sells coconut husk at ₹23 per kilogram. They "
                  "earned ₹9913 from the sale of husk in May. What quantity of husk did they sell in May? The quantity of "
                  "husk sold in May is 9913 ÷ 23 kg. Make a guess first.",
                  ["Guess first: 23 × 400 = 9200 is close to 9913, and 23 × 500 = 11500 is more than 9913.",
                   "So 500 groups are too big. 23 × 300 = 6900 fits, but 400 groups fit too, so take the biggest."]
                  + _husk + ["So the farm sold 431 kg of coconut husk in May."],
                  "431 kg of husk", kind="example"),
              FIO("oil.tender", "Kalpavruksha Coconut Oil: tender coconuts",
                  "In the hot summer months, tender coconuts are sold for ₹35. Ibrahim earns ₹8890 in a week. How many "
                  "tender coconuts did he sell? The number of tender coconuts sold by Ibrahim is 8890 ÷ 35. Take away groups "
                  "of 35 and fill the blanks: the quotient parts are ___ + 50 + ___; take away 7000, and 1890 is left; take "
                  "away ___, and 140 is left; take away ___, and nothing is left. Ibrahim sold ___ tender coconuts.",
                  ["Guess first: 35 × 200 = 7000 is less than 8890, and 35 × 300 = 10500 is more, so the answer is between "
                   "200 and 300."] + _tender + ["So Ibrahim sold 254 tender coconuts."],
                  "The blanks are 200, 1750, 140 and 4: 254 tender coconuts", kind="prompt"),
              FIO("oil.extra", "Kalpavruksha Coconut Oil: extra money",
                  "Ibrahim had bought the tender coconuts for ₹20 each. How much extra money did he earn by selling the "
                  "coconuts at ₹35? The cost of ___ coconuts at ₹20 each = ___ × ₹20 = ₹___. He earned ₹8890 from the "
                  "sale. The extra amount he earned is ₹8890 − ₹___ = ₹___.",
                  ["Ibrahim sold 254 tender coconuts, and he bought each for ₹20.",
                   "The cost of 254 coconuts at ₹20 each is 254 × 20 = 5080 rupees.",
                   "He earned 8890 rupees from the sale.",
                   "The extra amount is 8890 − 5080 = 3810 rupees.",
                   "Check another way: each coconut gave 35 − 20 = 15 rupees extra, and 254 × 15 = 3810."],
                  "The cost is ₹5080 and the extra amount is ₹3810", kind="prompt")],
          misconceptions=["M_TOO_BIG_GROUP"])],
    key_terms=["hundreds", "tens", "ones", "groups"]))
