# -*- coding: utf-8 -*-
"""Topics T6 and T7 (module M3: Place Value Division and Problems): Division Using Place Value (regroup and share, the zero that
holds an empty place, thousands and two-digit divisors with both methods) and Division in Word Problems (what the remainder
means, missing numbers in a bill, breaking a problem into steps).
Every teaching concept has one worked example with the plan's own numbers (practice values); every book question is an FIO
item of its topic's DOER, in the book's order. The working is written with division_steps.py, which asserts every number.
A division with a remainder is never written as one chain."""
from topics_common import A, DOER, FIO, TOPIC, WE
import division_steps as D

TOPICS = []

# ============================== T6 Division Using Place Value ==============================================
_pv62 = D.pv(62, 5)[0]
_pv75 = D.pv(75, 8)[0]
_pv324 = D.pv(324, 3)[0]
_pv136 = D.pv(136, 6)[0]
assert 215 // 4 == 53 and 215 % 4 == 3 and 4 * 53 + 3 == 215

_ldv_a = (["First way: take away groups of 6."] + D.pq(7032, 6, [1000, 100, 70, 2], True)[0]
          + ["Second way: by place value, one short line for each place."] + D.pv(7032, 6, True, True)[0]
          + ["The blanks of the first way are 100 and 2 in the quotient parts, and 6,000, 420 and 12 to take away."])
_ldv_b = (["First way: take away groups of 5."] + D.pq(3005, 5, [600, 1], True)[0]
          + ["Second way: by place value."] + D.pv(3005, 5, True, True)[0]
          + ["Why the 0? In the tens place there is 0 tens to share among 5 parts, so each part gets 0 tens. Without the 0 "
             "the answer would be 61, and 5 × 61 = 305 is not 3,005."])
assert 5 * 61 == 305
_ldv_c = (["First way: take away groups of 14."] + D.pq(2874, 14, [200, 5], True)[0]
          + ["Second way: by place value."] + D.pv(2874, 14, True, True)[0]
          + ["The blanks of the first way are 200 and 5 in the quotient parts, then 74 left, then 70 to take away and 4 left."])
_ldv_d = (["First way: take away groups of 32."] + D.pq(9805, 32, [300, 6], True)[0]
          + ["Second way: by place value."] + D.pv(9805, 32, True, True)[0]
          + ["Compare both: each way gives quotient 306 and remainder 13. The 0 in 306 holds the tens place, where 20 tens "
             "cannot be shared among 32 parts."])

_vm1, _vm1a = [], []
for _i, (_n, _d) in enumerate([(506, 5), (918, 8), (8126, 7), (9324, 4), (876, 6), (7008, 3)], 1):
    _t, _q, _r = D.nqdr(_n, _d, True)
    _ds = ", ".join(str(x) for x in D.pv(_n, _d)[3])
    _vm1.append("%d. By place value the quotient digits are %s. %s" % (_i, _ds, _t))
    _vm1a.append("%d. %s remainder %d" % (_i, "{:,}".format(_q), _r))
_vm2, _vm2a = [], []
for _i, (_n, _d) in enumerate([(934, 12), (829, 23), (705, 18), (8704, 32), (6790, 45), (5074, 21)], 7):
    _t, _q, _r = D.nqdr(_n, _d, True)
    _ds = ", ".join(str(x) for x in D.pv(_n, _d)[3])
    _vm2.append("%d. By place value the quotient digits are %s. %s" % (_i, _ds, _t))
    _vm2a.append("%d. %s remainder %d" % (_i, "{:,}".format(_q), _r))

assert 480 // 4 == 120 and 906 // 3 == 302 and 400 // 20 == 20 and 1000 // 50 == 20 and 848 // 4 == 212 and 868 // 4 == 217
assert 936 // 3 == 312 and 88 // 1 == 88 and 88 // 2 == 44 and 88 // 4 == 22 and 88 // 8 == 11
assert 950 // 5 == 190 and 920 // 2 == 460 and 930 // 3 == 310 and 990 // 9 == 110 and 180 // 1 == 180
assert 6480 // 8 == 810 and 6480 // 9 == 720 and 4 * 120 == 480 and 8 * 810 == 6480 and 42 * 5 == 210 and 210 * 2 == 420
assert 100 * 3 <= 1000 and 50 * 20 == 1000 and 50 * 30 == 1500

TOPICS.append(TOPIC(
    "T6", "M3", "Division Using Place Value", ["Division Using Place Value", "Let Us Divide"], "Apply",
    "Students divide by place value: share the thousands, hundreds, tens and ones equally, regroup what is left, write 0 in an "
    "empty place, and divide by two-digit divisors.",
    "To divide by place value, share each place equally among the parts and regroup what is left into the next place. A place "
    "that cannot be shared gets a 0 in the quotient. Place value and taking away groups give the same quotient.",
    [A("T6.C1", "Regroup and Share", "Apply",
       "Students share tens equally among the parts, regroup the tens left into ones, and share the ones to divide a "
       "two-digit number.",
       textbook=["Sunitha's mother has 62 candies to be distributed equally among 5 children. How many candies would each "
                 "child get? She shows the following way of doing division using place value."],
       teach=["Predict first: 83 candies are shared equally among 6 children. Can the 8 tens be shared among 6 without "
              "breaking a ten?",
              "83 is 8 tens and 3 ones. Share the 8 tens among 6 children: each child gets 1 ten, and 2 tens are left.",
              "The 2 tens left cannot be shared without breaking them, so regroup them into 20 ones. With the 3 ones that "
              "makes 23 ones.",
              "Share the 23 ones among 6 children: each child gets 3 ones, because 6 × 3 = 18, and 5 ones are left.",
              "Each child gets 1 ten and 3 ones, which is 13, and 5 candies are left. So 83 ÷ 6: quotient 13, remainder 5.",
              "Check: 83 = 6 × 13 + 5.",
              "Rule: share the tens, regroup the tens left into ones, then share the ones."],
       examples=[WE("83 candies are shared equally among 6 children (practice values). How many candies does each child "
                    "get? Use place value.",
                    D.pv(83, 6)[0], "Each child gets 13 candies and 5 are left over")],
       ncert=["pv.text"], key_terms=["regroup", "share", "tens", "ones"], minutes=6),
     A("T6.C2", "Regroup Hundreds, Hold the Place with Zero", "Apply",
       "Students regroup hundreds into tens, write 0 in a place that cannot be shared, and tell how many digits a quotient "
       "has from the first digit of the dividend.",
       textbook=["Why do we put a 0 here?",
                 "Can you tell just by looking at the divisor and dividend, how many digits the quotient would have?"],
       teach=["Predict first: in 412 ÷ 4, can the 1 ten be shared among 4 equal parts? What should the tens digit of the "
              "answer be?",
              "412 is 4 hundreds, 1 ten and 2 ones. Share the 4 hundreds among 4 parts: 1 hundred each.",
              "The 1 ten cannot be shared among 4 parts without breaking it, so each part gets 0 tens. Write 0 in the tens "
              "place.",
              "Regroup the 1 ten into 10 ones. With the 2 ones that makes 12 ones. Share them among 4 parts: 3 ones each, "
              "because 4 × 3 = 12.",
              "So 412 ÷ 4 = 103. The 0 holds the tens place, and 103 is not 13.",
              "How many digits? For a one-digit divisor: if the first digit of the dividend is at least the divisor, the "
              "quotient has as many digits as the dividend. If it is less, the quotient has one digit fewer.",
              "412 has the first digit 4, and 4 is at least 4, so the quotient has 3 digits. For 215 ÷ 4 the first digit 2 "
              "is less than 4, so the quotient has 2 digits.",
              "Check: 4 × 103 = 412."],
       examples=[WE("Find 412 ÷ 4 by place value (practice values), and say how many digits the quotient has.",
                    D.pv(412, 4)[0]
                    + ["Digits: the first digit of 412 is 4, which is at least the divisor 4, so the quotient has 3 digits, "
                       "as many as the dividend.",
                       "Compare 215 ÷ 4: the first digit 2 is less than 4, so the quotient has one digit fewer. "
                       + D.nqdr(215, 4)[0]],
                    "412 ÷ 4 = 103, with 3 digits")],
       ncert=["pv.zero"], key_terms=["regroup", "hundreds", "zero", "digits"],
       misconceptions=["M_ZERO_SKIPPED", "M_DIGITS_SAME"], minutes=7),
     A("T6.C3", "Thousands and Two-Digit Divisors: Both Methods", "Analyze",
       "Students divide thousands by a two-digit divisor by taking away groups and by place value, and see that both "
       "methods give the same quotient.",
       textbook=["Discuss why we have to write this 0 here.",
                 "Compare both solutions. Also, remember to put 0 in the right places."],
       teach=["Predict first: for 3,648 ÷ 12, will taking away groups and place value give the same answer?",
              "Taking away groups: 12 × 300 = 3,600, and 3,648 − 3,600 = 48. Then 12 × 4 = 48. So 300 + 4 = 304.",
              "Place value: 36 hundreds shared among 12 parts gives 3 hundreds each, because 12 × 3 = 36.",
              "The 4 tens cannot be shared among 12 parts, so each part gets 0 tens. The 0 holds the tens place. Then 48 ones "
              "shared among 12 parts gives 4 ones each.",
              "Both ways give 304. The 0 in 304 is the tens place that had nothing to share.",
              "Check: 12 × 304 = 3,648.",
              "Rule: both methods give the same quotient. Write 0 in every place that cannot be shared."],
       examples=[WE("Find 3,648 ÷ 12 in two ways (practice values).",
                    ["First way: take away groups of 12."] + D.pq(3648, 12, [300, 4], True)[0]
                    + ["Second way: by place value."] + D.pv(3648, 12, True)[0]
                    + ["Both ways give 304."],
                    "3,648 ÷ 12 = 304")],
       ncert=["ldv.zero", "ldv.compare"], key_terms=["thousands", "divisors", "methods", "zero"],
       misconceptions=["M_ZERO_SKIPPED"], minutes=8),
     DOER("T6.C4", "Practice: Regroup and Share", "regroup_and_share", "Apply",
          "Students regroup tens and hundreds, share the blocks equally to divide by place value, write zeros in the right "
          "places, find missing numbers, and check each answer with N = D × Q + R.",
          ["Share each place equally, then regroup what is left into the next place.",
           "Write 0 in a place that cannot be shared.",
           "Check every division with N = D × Q + R."],
          items=[
              FIO("pv.ex1", "Example 10: 62 candies for 5 children",
                  "Sunitha's mother has 62 candies to be distributed equally among 5 children. How many candies would each "
                  "child get? She shows the following way of doing division using place value. 62 ÷ 5: Divide 62 into 5 "
                  "equal parts.",
                  _pv62 + ["So each child gets 12 candies and 2 candies are left."],
                  "Each child gets 12 candies, with 2 left over", kind="example",
                  q_figure="Six rods of ten and two single cubes in a row, with five empty groups beside them.",
                  s_figure="Five groups with 1 rod each, the sixth rod broken into 10 cubes that join the 2 cubes, 2 cubes on "
                           "each group and 2 cubes left over."),
              FIO("pv.ex2", "Example 11: 75 ÷ 8",
                  "75 ÷ 8: Divide 75 into 8 equal parts. Can we divide this into 8 equal parts without breaking them? What "
                  "can we do? Regrouping this into Ones, we get 75 Ones. How much is each part?",
                  _pv75 + ["So each part is 9 and 3 are left."],
                  "Each part is 9, with 3 left over", kind="example",
                  q_figure="Seven rods of ten and five single cubes, with eight empty groups beside them.",
                  s_figure="The 7 rods broken into 70 cubes that join the 5 cubes, then 9 cubes on each of the eight groups and "
                           "3 cubes left over."),
              FIO("pv.ex3", "Example 12: 324 ÷ 3",
                  "324 ÷ 3: Divide 324 into 3 equal parts. 324 = 3 Hundreds + 2 Tens + 4 Ones. 3 Hundreds ÷ 3 = 1 Hundred. 2 "
                  "Tens ÷ 3: Not possible without regrouping, so everyone gets 0 Tens. Regroup 2 Tens into Ones. 20 Ones + 4 "
                  "Ones = 24 Ones. 24 Ones ÷ 3 = 8 Ones.",
                  _pv324 + ["So each of the 3 parts gets 1 hundred, 0 tens and 8 ones, which is 108."],
                  "324 ÷ 3 = 108", kind="example",
                  q_figure="Three hundred blocks, two ten blocks and four one blocks, with three empty groups beside them.",
                  s_figure="Three groups with 1 hundred block each, no ten blocks, and 8 one blocks each."),
              FIO("pv.ex4", "Example 13: 136 ÷ 6",
                  "136 ÷ 6: Divide 136 into 6 equal parts. 136 = 1 Hundred + 3 Tens + 6 Ones. 1 Hundred ÷ 6: not possible "
                  "without regrouping into Tens. Regroup 1 Hundred into 10 Tens. Total 13 Tens. Continue dividing.",
                  _pv136 + ["So each of the 6 parts gets 2 tens and 2 ones, which is 22, and 4 are left."],
                  "Quotient 22, remainder 4", kind="example"),
              FIO("pv.digits", "Division Using Place Value: digits of the quotient",
                  "Can you tell just by looking at the divisor and dividend, how many digits the quotient would have? Look at "
                  "the problems above and find this out. Explain your thoughts.",
                  ["Look at the four problems: 62 ÷ 5, 75 ÷ 8, 324 ÷ 3 and 136 ÷ 6.",
                   "62 ÷ 5: the first digit 6 is at least 5, and the quotient 12 has 2 digits, as many as 62.",
                   "324 ÷ 3: the first digit 3 is at least 3, and the quotient 108 has 3 digits, as many as 324.",
                   "75 ÷ 8: the first digit 7 is less than 8, and the quotient 9 has 1 digit, one fewer than 75.",
                   "136 ÷ 6: the first digit 1 is less than 6, and the quotient 22 has 2 digits, one fewer than 136.",
                   "Rule for a one-digit divisor: if the first digit of the dividend is at least the divisor, the quotient has "
                   "as many digits as the dividend. If it is less, the quotient has one digit fewer."],
                  "With a one-digit divisor: as many digits as the dividend if its first digit is at least the divisor, "
                  "otherwise one fewer",
                  kind="prompt"),
              FIO("ldv.a", "Let Us Divide: (a) 7,032 ÷ 6",
                  "Let Us Divide. (a): 7,032 ÷ 6. First way, taking away groups of 6: the quotient parts are 1,000 + ___ + 70 "
                  "+ ___; take away ___ and 1,032 is left; take away 600 and 432 is left; take away ___ and 12 is left; take "
                  "away ___ and nothing is left. Second way, by place value: the quotient digits (thousands, hundreds, tens, "
                  "ones) are 1, 1, 7, 2.",
                  _ldv_a, "Quotient 1,172: the blanks are 100, 2, 6,000, 420 and 12", kind="prompt",
                  q_figure="Two layouts of 7,032 ÷ 6 side by side: on the left the take-away layout with blanks, on the right "
                           "the place value layout with the columns thousands, hundreds, tens and ones and the quotient "
                           "digits 1, 1, 7, 2."),
              FIO("ldv.b", "Let Us Divide: (b) 3,005 ÷ 5",
                  "(b): 3,005 ÷ 5. First way: the quotient parts are ___ + ___; take away 3,000 and 5 is left; take away ___ "
                  "and nothing is left. Second way, by place value: the quotient digits (thousands, hundreds, tens, ones) are "
                  "___, ___, 0, ___. Discuss why we have to write this 0 here.",
                  _ldv_b, "Quotient 601, with the digits 0, 6, 0, 1", kind="prompt",
                  q_figure="Two layouts of 3,005 ÷ 5 side by side: the take-away layout with blanks and the place value layout "
                           "with the columns thousands, hundreds, tens and ones and a 0 in the tens place."),
              FIO("ldv.c", "Let Us Divide: (c) 2,874 ÷ 14",
                  "(c): 2,874 ÷ 14. First way: the quotient parts are ___ + ___; take away 2,800 and ___ is left; take away "
                  "___ and ___ is left. Second way, by place value: 28 hundreds are shared first; fill the four quotient "
                  "digits (thousands, hundreds, tens, ones) and the numbers left at each place.",
                  _ldv_c, "Quotient 205, remainder 4, with the digits 0, 2, 0, 5", kind="prompt",
                  q_figure="Two layouts of 2,874 ÷ 14 side by side: the take-away layout with blanks and the place value "
                           "layout with four empty quotient digits and the columns thousands, hundreds, tens and ones."),
              FIO("ldv.d", "Let Us Divide: (d) 9,805 ÷ 32",
                  "(d): 9,805 ÷ 32. First way: the quotient parts are ___ + ___; take away ___ and 205 is left; take away "
                  "___ and ___ is left. Second way, by place value: fill the four quotient digits and the numbers left at each "
                  "place. Compare both solutions. Also, remember to put 0 in the right places.",
                  _ldv_d, "Quotient 306, remainder 13, with the digits 0, 3, 0, 6", kind="prompt",
                  q_figure="Two layouts of 9,805 ÷ 32 side by side: the take-away layout with blanks and the place value "
                           "layout with four empty quotient digits and the columns thousands, hundreds, tens and ones."),
              FIO("lud3.q1", "Let Us Do (missing numbers), Q1",
                  "Find the missing numbers such that there is no remainder. Remember, there could be more than one solution. "
                  "Each box shows a divisor, a dividend and a quotient with some digits missing (written ___): (a): 4 into "
                  "480, quotient ___ ___ 0; (b): 3 into 906, quotient ___ 0 ___; (c): 20 into 400, quotient ___ 0; (d): 50 "
                  "into 100___, quotient ___ 0; (e): ___ into 8___8, quotient 2 1 ___; (f): 3 into ___36, quotient 3 ___ ___; "
                  "(g): ___ into 88, quotient ___ ___; (h): ___ into 9___0, quotient ___ ___ ___; (i): ___ into 180, quotient "
                  "___ ___ ___; (j): ___ into 6,480, quotient ___ ___ ___.",
                  ["Each missing number must make the division exact. Use Dividend = Divisor × Quotient.",
                   "(a): 480 ÷ 4 = 120, so the missing digits are 1 and 2.",
                   "(b): 906 ÷ 3 = 302, so the missing digits are 3 and 2.",
                   "(c): 400 ÷ 20 = 20, so the missing digit is 2.",
                   "(d): the dividend 100___ must be a multiple of 50. Only 1000 works, and 1000 ÷ 50 = 20, so the missing "
                   "digits are 0 and 2.",
                   "(e): only the divisor 4 fits. 848 ÷ 4 = 212 (digits 4 and 2) or 868 ÷ 4 = 217 (digits 6 and 7).",
                   "(f): the dividend is 936, and 936 ÷ 3 = 312, so the missing digits are 9, 1 and 2.",
                   "(g): 88 can be divided exactly by 1, 2, 4 or 8: the quotient is 88, 44, 22 or 11.",
                   "(h): there are many answers, for example 950 ÷ 5 = 190, 920 ÷ 2 = 460, 930 ÷ 3 = 310 and 990 ÷ 9 = 110.",
                   "(i): a quotient with 3 digits needs the divisor 1, and 180 ÷ 1 = 180.",
                   "(j): 6,480 ÷ 8 = 810 and 6,480 ÷ 9 = 720 both fit.",
                   "Check by multiplying back, for example 4 × 120 = 480 and 8 × 810 = 6,480."],
                  "(a): 120; (b): 302; (c): 20; (d): 20; (e): 212 or 217; (f): 312; (g): 88, 44, 22 or 11; (h): many; "
                  "(i): 180; (j): 810 or 720",
                  kind="exercise"),
              FIO("lud3.riddle", "Number Riddle: I am a 3-digit number",
                  "I am a 3-digit number. If you divide me by 5, you get 42. If you multiply me by 2, you get 420. What number "
                  "am I?",
                  ["The number divided by 5 gives 42, so use Dividend = Divisor × Quotient: 5 × 42 = 210.",
                   "Check the second clue: 210 × 2 = 420, which matches.",
                   "The number is a 3-digit number, and 210 has 3 digits."],
                  "210", kind="prompt"),
              FIO("vm.q1to6", "Let Us Solve (place value): divisions 1 to 6",
                  "Divide the following. Try dividing using place values, whenever you can. Identify the remainder, if any, "
                  "and check whether N = D × Q + R. 1. 506 ÷ 5; 2. 918 ÷ 8; 3. 8,126 ÷ 7; 4. 9,324 ÷ 4; 5. 876 ÷ 6; 6. "
                  "7,008 ÷ 3.",
                  ["Divide each number by place value, then check with N = D × Q + R."] + _vm1,
                  "; ".join(_vm1a), kind="exercise"),
              FIO("vm.q7to12", "Let Us Solve (place value): divisions 7 to 12",
                  "Divide the following. Try dividing using place values, whenever you can. Identify the remainder, if any, "
                  "and check whether N = D × Q + R. 7. 934 ÷ 12; 8. 829 ÷ 23; 9. 705 ÷ 18; 10. 8,704 ÷ 32; 11. 6,790 ÷ 45; "
                  "12. 5,074 ÷ 21.",
                  ["Divide each number by place value, then check with N = D × Q + R."] + _vm2,
                  "; ".join(_vm2a), kind="exercise")],
          misconceptions=["M_ZERO_SKIPPED", "M_DIGITS_SAME"])],
    key_terms=["place value", "regroup", "zero", "quotient"]))

# ============================== T7 Division in Word Problems ===============================================
_q1_6 = D.nqdr(250, 6)[0]
assert 250 == 6 * 41 + 4 and 42 * 6 == 252 and 252 - 250 == 2 and 250 == 8 * 31 + 2 and 32 * 8 == 256 and 256 - 250 == 6
assert 50 * 10 == 500 and 50 * 11 == 550 and 470 // 20 == 23 and 470 % 20 == 10 and 4 * 50 + 16 * 20 == 520
assert 157 + 124 + 136 == 417 and 417 // 3 == 139 and 3 * 139 == 417
assert 11 == 2 * 5 + 1 and 5000 - 400 == 4600 and 23 * 200 == 4600 and 15 * 8 == 120 and 5 * 4 * 6 == 120
assert 12 * 48 == 576 and 344 + 232 == 576 and 4 * 58 == 232
assert 6 * 12 == 72 and 72 * 5 == 360 and 240 // 8 == 30 and 3500 // 5 == 700 and 6250 // 125 == 50 and 50 // 10 == 5
assert 264 // 4 == 66 and 306 // 8 == 38 and 306 % 8 == 2 and 2400 // 16 == 150 and 120 // 4 == 30
assert 2800 // 32 == 87 and 2800 % 32 == 16 and 30 * 4 == 120 and 4 * 31 == 124
assert 26 * 78 == 2028 and 26 * 70 == 1820 and 26 * 8 == 208 and 1820 + 208 == 2028 and 2240 // 20 == 112
assert 32 * 56 == 1792 and 32 * 50 == 1600 and 32 * 6 == 192 and 1600 + 192 == 1792 and 3125 // 125 == 25
assert 2028 + 2240 + 1792 + 3125 == 9185 and 18 * 45 == 810 and 18 * 40 == 720 and 18 * 5 == 90 and 990 // 18 == 55
assert 1260 // 36 == 35 and 4 * 36 == 144 and 144 // 8 == 18 and 94 == 8 * 11 + 6 and 88 + 6 == 94

TOPICS.append(TOPIC(
    "T7", "M3", "Division in Word Problems", ["Let Us Solve", "Vegetable Market"], "Apply",
    "Students decide what the remainder means in a story, find a missing number in a bill by dividing, and solve a problem in "
    "steps after finding the information that is missing.",
    "In a story the remainder can mean one more bag or a few left over. A bill has a cost, a quantity and a total, and a "
    "missing number is found by dividing. A longer problem is broken into steps, and a missing number must be found first.",
    [A("T7.C1", "What the Remainder Means", "Apply",
       "Students decide whether a remainder needs one more container or is left over, and give the answer in words for the "
       "story.",
       textbook=["They need 21 full bags and 1 more bag to pack the 10 remaining coconuts, that is, 22 bags."],
       teach=["Predict first: 94 coconuts are packed in bags of 8. Do you need 11 bags or 12 bags? And what if the 94 "
              "coconuts are shared among 8 customers?",
              "94 ÷ 8: quotient 11, remainder 6, because 94 = 8 × 11 + 6.",
              "Packing in bags: 11 full bags hold 88 coconuts. The 6 coconuts left still need a bag, so 11 + 1 = 12 bags.",
              "Sharing among customers: each customer gets 11 coconuts. The 6 left over are not shared, so the answer is 11 "
              "each.",
              "Always read the story: when the leftover needs a container, add one more. When it is not shared, the "
              "quotient is the answer.",
              "Rule: the same remainder can mean one more bag or a few left over, depending on the story."],
       examples=[WE("94 coconuts (practice values). How many bags of 8 are needed? If the 94 coconuts are shared equally among "
                    "8 customers, how many does each get?",
                    D.pq(94, 8, [10, 1])[0]
                    + ["Bags: the 11 full bags hold 88 coconuts and 6 are left. The 6 need one more bag, so 11 + 1 = 12 "
                       "bags.",
                       "Sharing: each of the 8 customers gets 11 coconuts, and the 6 left over are not shared."],
                    "12 bags are needed, and each customer gets 11 coconuts")],
       key_terms=["remainder", "container", "bags", "left over"], misconceptions=["M_DROP_REMAINDER"], minutes=6),
     A("T7.C2", "Missing Numbers in a Bill", "Apply",
       "Students use total = cost of 1 kg × quantity to find a missing total by multiplying, and a missing quantity or cost "
       "by dividing.",
       textbook=["Munshi Lal has a big farm in Bihar. Every Saturday, he sells the vegetables from his farm at Sundar Sabzi "
                 "Mandi.",
                 "What information is recorded in this table?"],
       teach=["Predict first: onions cost ₹18 for 1 kg and 45 kg were sold. How much money is that? And if the bill says "
              "₹990, how many kg were sold?",
              "A bill has three numbers: the cost of 1 kg, the quantity in kg, and the total amount. Total amount = cost of "
              "1 kg × quantity.",
              "Total: 18 × 45 = 810, so 45 kg of onions cost ₹810.",
              "Missing quantity: the total is ₹990 and 1 kg costs ₹18, so the quantity is 990 ÷ 18 = 55 kg. Check: 18 × 55 "
              "= 990.",
              "Missing cost: the total is ₹1260 for 36 kg, so 1 kg costs 1260 ÷ 36 = ₹35. Check: 35 × 36 = 1260.",
              "Look at a real bill from a shop and name the information it records. Which number could you find by "
              "dividing?",
              "Rule: if the total is missing, multiply. If the quantity or the cost of 1 kg is missing, divide the total by "
              "the number you know."],
       examples=[WE("A bill has onions at ₹18 for 1 kg and 45 kg sold (practice values). Find the total. Then find the "
                    "quantity for a total of ₹990, and the cost of 1 kg for 36 kg with a total of ₹1260.",
                    ["Total amount = cost of 1 kg × quantity.",
                     "Total: 18 × 45 = 810, so the total is ₹810.",
                     "Check 18 × 45: 18 × 40 = 720 and 18 × 5 = 90, and 720 + 90 = 810.",
                     "Missing quantity: 990 ÷ 18 = 55 kg, because 18 × 55 = 990.",
                     "Missing cost: 1260 ÷ 36 = 35, because 35 × 36 = 1260, so 1 kg costs ₹35."],
                    "The total is ₹810, the quantity is 55 kg and 1 kg costs ₹35")],
       ncert=["vm.text", "vm.info", "vm.activity"], key_terms=["bill", "total", "cost", "quantity"], minutes=6),
     A("T7.C3", "Break a Problem into Steps", "Analyze",
       "Students break a word problem into steps, find what is asked, what is given and what is missing, and solve it in order.",
       teach=["Predict first: 4 baskets hold 36 coconuts each, and all the coconuts are packed equally into 8 sacks. What "
              "do you find first?",
              "Step 1: what is asked? The coconuts in each sack. Step 2: what is given? 4 baskets, 36 coconuts in each, "
              "and 8 sacks.",
              "Step 3: find all the coconuts: 4 × 36 = 144.",
              "Step 4: share them into 8 sacks: 144 ÷ 8 = 18. Check: 8 × 18 = 144.",
              "If the question asked how much money the farm earns, the price of a coconut is missing. The problem cannot be "
              "solved until that number is given.",
              "Rule: read what is asked, list what is given, find what is missing, then solve in order and check."],
       examples=[WE("4 baskets hold 36 coconuts each. All the coconuts are packed equally into 8 sacks (practice values). How "
                    "many coconuts are in each sack? What would be missing if we asked for the money earned?",
                    ["What is asked: the coconuts in each sack.",
                     "What is given: 4 baskets, 36 coconuts in each basket, and 8 sacks.",
                     "All the coconuts: 4 × 36 = 144.",
                     "Share into 8 sacks: 144 ÷ 8 = 18.",
                     "Check: 8 × 18 = 144.",
                     "For the money earned, the price of one coconut is missing, so it is needed first."],
                    "18 coconuts in each sack, and the price of one coconut is missing for the money")],
       key_terms=["steps", "problem", "missing information", "given"],
       misconceptions=["M_ALWAYS_ENOUGH", "M_UNIT_MIX"], minutes=6),
     DOER("T7.C4", "Practice: Word Problems", None, "Apply",
          "Students solve the word problems by dividing, decide what each remainder means, change units when needed, and name "
          "the missing information.",
          ["Read what is asked and what is given.",
           "Decide what the remainder means in the story.",
           "Find the missing information before you solve."],
          items=[
              FIO("ls1.q1", "Let Us Solve (word problems): Rani's samosas",
                  "Rani is planning to host a party. She estimates that 250 guests will attend. She plans to serve one samosa "
                  "to each guest. Samosas are available in packs of 6 or 8. Which pack should Rani buy? Explain your answer.",
                  ["Rani needs 250 samosas, one for each guest.",
                   "Packs of 6: 250 ÷ 6: quotient 41, remainder 4, because 250 = 6 × 41 + 4. The 4 left need one more pack, "
                   "so 41 + 1 = 42 packs.",
                   "42 packs of 6 are 42 × 6 = 252 samosas, which is 252 − 250 = 2 extra.",
                   "Packs of 8: 250 ÷ 8: quotient 31, remainder 2, because 250 = 8 × 31 + 2. The 2 left need one more pack, "
                   "so 31 + 1 = 32 packs.",
                   "32 packs of 8 are 32 × 8 = 256 samosas, which is 256 − 250 = 6 extra.",
                   "Packs of 6 leave 2 extra samosas and packs of 8 leave 6 extra, so packs of 6 waste fewer.",
                   "The book gives no prices, so this is the plan's reading: the pack with fewer extra samosas."],
                  "Sample answer: packs of 6, 42 packs with 2 extra (packs of 8: 32 packs with 6 extra). Your answer may "
                  "differ",
                  kind="exercise"),
              FIO("ls1.q2", "Let Us Solve (word problems): buses to the Science Park",
                  "342 students from a school are going on a trip to the Science Park. Each bus can carry a maximum of 41 "
                  "students. How many buses does the school need to arrange?",
                  ["Each bus carries at most 41 students, so divide 342 by 41."] + D.pq(342, 41, [8])[0]
                  + ["The 8 full buses carry 328 students. The 14 students left need one more bus.",
                     "So 8 + 1 = 9 buses."],
                  "9 buses", kind="exercise"),
              FIO("ls1.q3", "Let Us Solve (word problems): Sofia's notes",
                  "Sofia has only ₹50 and ₹20 notes. She needs to pay ₹520 using these notes. How many ₹50 and ₹20 notes does "
                  "she need to make ₹520? Find out the different possible combinations.",
                  ["Let the ₹50 notes be a few, from 0 to 10, because 50 × 10 = 500 and 50 × 11 = 550 is more than 520.",
                   "The money left for ₹20 notes must be a multiple of 20.",
                   "No ₹50 note: 520 ÷ 20 = 26 notes of ₹20.",
                   "2 notes of ₹50: 520 − 100 = 420 and 420 ÷ 20 = 21 notes of ₹20.",
                   "4 notes of ₹50: 520 − 200 = 320 and 320 ÷ 20 = 16 notes of ₹20.",
                   "6 notes of ₹50: 520 − 300 = 220 and 220 ÷ 20 = 11 notes of ₹20.",
                   "8 notes of ₹50: 520 − 400 = 120 and 120 ÷ 20 = 6 notes of ₹20.",
                   "10 notes of ₹50: 520 − 500 = 20 and 20 ÷ 20 = 1 note of ₹20.",
                   "An odd number of ₹50 notes does not work. For 1 note: 520 − 50 = 470, and 470 ÷ 20: quotient 23, "
                   "remainder 10, which is not a whole number of notes.",
                   "Check one: 4 × 50 + 16 × 20 = 200 + 320 = 520. The book does not say if both kinds of note must be used."],
                  "Six ways (₹50 notes and ₹20 notes): 0 and 26, 2 and 21, 4 and 16, 6 and 11, 8 and 6, 10 and 1",
                  kind="exercise"),
              FIO("ls1.q4", "Let Us Solve (word problems): the picnic",
                  "Three friends decide to split the money spent on their picnic equally. They buy snacks and sweets for ₹157, "
                  "juice and fruits for ₹124 and pulav and paratha for ₹136. How much should each person pay to share the "
                  "cost equally?",
                  ["Add the three amounts: 157 + 124 + 136 = 417.",
                   "Share 417 equally among 3 friends: 417 ÷ 3 = 139.",
                   "Check: 3 × 139 = 417."],
                  "₹139", kind="exercise"),
              FIO("ls2.q1", "Let Us Solve (word problems): theatre shows",
                  "A theatre company can accommodate 45 people during one show. (a): A total of 475 people bought tickets for a "
                  "puppet show. How many shows are needed to seat all the people who bought tickets? (b): There are 2 shows in "
                  "a day. How many days will be needed to accommodate all the people?",
                  ["(a): each show seats 45 people, so divide 475 by 45."] + D.pq(475, 45, [10])[0]
                  + ["(a): 10 shows seat 450 people and 25 people are left. They need one more show, so 10 + 1 = 11 shows.",
                     "(b): 11 shows at 2 shows a day: 11 ÷ 2: quotient 5, remainder 1, because 11 = 2 × 5 + 1.",
                     "(b): 5 days hold 10 shows. The last show needs one more day, so 5 + 1 = 6 days."],
                  "(a): 11 shows; (b): 6 days", kind="exercise"),
              FIO("ls2.q2", "Let Us Solve (word problems): Naina's ice cream",
                  "Naina bought 5 kg of ice cream as a birthday treat for her 23 friends. 400 g ice cream was left after "
                  "everyone had an equal share. How much ice cream did each of her friends eat?",
                  ["The ice cream is 5 kg and the part left is 400 g, so change the kilograms to grams: 5 × 1000 = 5000 g.",
                   "The friends ate 5000 − 400 = 4600 g.",
                   "Share equally among 23 friends: 4600 ÷ 23 = 200.",
                   "Check: 23 × 200 = 4600."],
                  "200 g", kind="exercise"),
              FIO("ls2.q3", "Let Us Solve (word problems): Megha's biscuits",
                  "Megha packs 15 packets of ragi-oats biscuits for a 4-day group trip. Each packet contains 8 biscuits. "
                  "There are 6 people in the group. If distributed evenly, how many biscuits can one person have each day?",
                  ["Count all the biscuits: 15 × 8 = 120 biscuits in all.",
                   "Share equally among 6 people: 120 ÷ 6 = 20 biscuits for each person for the whole trip.",
                   "The trip is 4 days long: 20 ÷ 4 = 5 biscuits for each person each day.",
                   "Check: 5 × 4 × 6 = 120."],
                  "5 biscuits", kind="exercise"),
              FIO("ls2.q6", "Let Us Solve (word problems): the cycle rally",
                  "A company in Mumbai organises cycle rallies from Mumbai to Panjim, Goa every year. They aim to cover 576 km "
                  "in 12 days. (a): How much distance should they cycle every day, to cover the distance evenly? (b): After "
                  "reaching Ratnagiri, they rest for 1 day. How much distance should they cycle each day to reach Goa in 4 "
                  "days? Assume that they cover the distance evenly.",
                  ["(a): 576 km in 12 days, the same distance each day: 576 ÷ 12 = 48 km a day, because 12 × 48 = 576.",
                   "(b): the map shows 344 km from Mumbai to Ratnagiri and 232 km from Ratnagiri to Goa, and 344 + 232 = 576.",
                   "After Ratnagiri and the rest day, 232 km are left to cover in 4 days.",
                   "232 ÷ 4 = 58 km a day, because 4 × 58 = 232."],
                  "(a): 48 km a day; (b): 58 km a day", kind="exercise",
                  q_figure="A map of the west coast with Mumbai at the top, Ratnagiri in the middle and Goa at the bottom, "
                           "and the distances 344 km (Mumbai to Ratnagiri), 232 km (Ratnagiri to Goa) and 576 km (Mumbai to "
                           "Goa) marked along the coast.",
                  s_figure="The same map with the 232 km from Ratnagiri to Goa split into 4 equal days of 58 km."),
              FIO("ls2.q7", "Let Us Solve (word problems): missing information",
                  "Given below are a few problems. You may need some additional information to solve these. Identify the "
                  "missing information. Write the missing information and find the answer. (a): A fruit vendor sells 6 baskets "
                  "of mangoes. Each basket contains 12 mangoes. How much did the vendor earn in total? (b): A school has 8 "
                  "classrooms, and each classroom has an equal number of desks. How many desks are there in each classroom? "
                  "(c): Rahul buys 5 cricket bats for his team. The total bill is ₹3500. How much does one bat cost? (d): A "
                  "restaurant serves 125 plates of idlis in a day. The total earnings from selling all the idli plates is "
                  "₹6250. How many idlis are there in each plate?",
                  ["(a): the price of one mango is missing. Practice value: ₹5 for one mango.",
                   "(a): the mangoes are 6 × 12 = 72, and the vendor earns 72 × 5 = 360 rupees.",
                   "(b): the total number of desks is missing. Practice value: 240 desks.",
                   "(b): the desks in each classroom are 240 ÷ 8 = 30.",
                   "(c): nothing is missing. One bat costs 3500 ÷ 5 = 700 rupees, because 5 × 700 = 3500.",
                   "(d): the price of one idli is missing. One plate earns 6250 ÷ 125 = 50 rupees, because 125 × 50 = 6250.",
                   "(d): practice value: ₹10 for one idli. Then the idlis in each plate are 50 ÷ 10 = 5."],
                  "(a): price of one mango; (b): total desks; (c): none, ₹700; (d): price of one idli. Practice values used",
                  kind="exercise"),
              FIO("ls2.q8", "Let Us Solve (word problems): the bookshelves",
                  "To make one bookshelf, a carpenter needs the following things: 4 long wooden panels, 8 short wooden panels, "
                  "16 small clips, 4 large clips, 32 screws. The carpenter has a stock of 264 long wooden panels, 306 short "
                  "wooden panels, 2400 small clips, 120 large clips, and 2800 screws. How many bookshelves can the carpenter "
                  "make? Discuss your thoughts.",
                  ["One bookshelf needs 4 long panels, 8 short panels, 16 small clips, 4 large clips and 32 screws.",
                   "Long panels: 264 ÷ 4 = 66 shelves.",
                   "Short panels: 306 ÷ 8: quotient 38, remainder 2, so 38 shelves.",
                   "Small clips: 2400 ÷ 16 = 150 shelves.",
                   "Large clips: 120 ÷ 4 = 30 shelves.",
                   "Screws: 2800 ÷ 32: quotient 87, remainder 16, so 87 shelves.",
                   "The carpenter can only make as many shelves as the scarcest part allows. The smallest number is 30, from "
                   "the large clips.",
                   "Check: 30 shelves use 30 × 4 = 120 large clips, which is all of them, and 31 shelves would need 124."],
                  "30 bookshelves", kind="exercise",
                  q_figure="A bookshelf made of two side panels and four shelves.",
                  s_figure="The five parts in a row, each with the number of shelves it allows: 66, 38, 150, 30 and 87, with 30 "
                           "circled."),
              FIO("vm.table", "Vegetable Market: complete the table",
                  "His naughty grandson has erased some numbers from his record book. Help Munshi Lal complete the table.",
                  ["Total amount = cost of 1 kg × quantity.",
                   "Radish: 26 × 78 = 2,028 rupees, because 26 × 70 = 1,820 and 26 × 8 = 208, and 1,820 + 208 = 2,028.",
                   "Potato: the quantity is 2,240 ÷ 20 = 112 kg, because 20 × 112 = 2,240.",
                   "Cabbage: 32 × 56 = 1,792 rupees, because 32 × 50 = 1,600 and 32 × 6 = 192, and 1,600 + 192 = 1,792.",
                   "Green peas: the cost of 1 kg is 3,125 ÷ 125 = 25 rupees, because 125 × 25 = 3,125.",
                   "Total money earned: 2,028 + 2,240 + 1,792 + 3,125 = 9,185 rupees."],
                  "Radish ₹2,028; potato 112 kg; cabbage ₹1,792; green peas ₹25; total ₹9,185", kind="prompt",
                  q_figure="A table with the columns S.No., Vegetable, Cost of 1 kg, Quantity Supplied (in kg) and Total "
                           "Amount, with the rows Radish ₹26, 78 kg, blank; Potato ₹20, blank, ₹2,240; Cabbage ₹32, 56 kg, "
                           "blank; Green peas blank, 125 kg, ₹3,125; and a last row Total money earned through the sale, "
                           "blank.",
                  s_figure="The same table with every blank filled in.")],
          misconceptions=["M_DROP_REMAINDER", "M_ALWAYS_ENOUGH", "M_UNIT_MIX"])],
    key_terms=["remainder", "bill", "steps", "problem"]))
