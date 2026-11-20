# -*- coding: utf-8 -*-
"""Topics T4, T5 and T6 (module M2: Patterns, Large Numbers and Journey Problems): Sums of Consecutive Numbers, Adding and
Subtracting Large Numbers (with the aligned digits and the book's Let Us Solve and Let Us Do sets), and Journey Problems.
Every teaching concept has one worked example with the plan's own numbers (practice values); every book question is an
FIO item of its topic's DOER, in the book's order. Chains the equation gate reads are written with the numbers alone."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T4 Sums of Consecutive Numbers =============================================
TOPICS.append(TOPIC(
    "T4", "M2", "Sums of Consecutive Numbers", ["Sums of Consecutive Numbers"], "Understand",
    "Students find the patterns in the sums of consecutive numbers and use pairs from the two ends to add a run of "
    "consecutive numbers without adding one by one.",
    "Consecutive numbers follow one another with none skipped. The difference between successive sums is the number of "
    "numbers added, and pairs from the two ends of a run make the same total.",
    [A("T4.C1", "Consecutive Numbers and Their Sums", "Understand",
       "Students explain whether the sums of consecutive numbers are even or odd and find the difference between "
       "successive sums.",
       textbook=["Numbers that follow one another in order without skipping any number are called consecutive numbers. "
                 "Here are some examples: 1, 2, 3, 4, 5; 29, 30, 31, 32; 512, 513; 2023, 2024, 2025."],
       teach=["Predict first: add 10 + 11 + 12, then 11 + 12 + 13, then 12 + 13 + 14. How much does the sum go up each "
              "time?",
              "Consecutive numbers follow one another in order, with no number skipped. 10, 11 and 12 are consecutive.",
              "The sums are 33, 36 and 39. Each time the sum goes up by 3.",
              "Why 3? When the start moves up by 1, each of the 3 numbers goes up by 1, so the sum goes up by 3. For a "
              "run of 4 numbers it would go up by 4.",
              "Look at the sums: 33 is odd, 36 is even and 39 is odd. The sums of 3 consecutive numbers take turns, odd "
              "then even.",
              "Rule: the difference between successive sums is the number of numbers added. Whether the sums are even "
              "or odd depends on how many numbers are added."],
       examples=[WE("Find the sums of 3 consecutive numbers that start at 10, 11 and 12 (practice values). What is the "
                    "difference between successive sums, and are the sums even or odd?",
                    ["10 + 11 + 12 = 33.",
                     "11 + 12 + 13 = 36.",
                     "12 + 13 + 14 = 39.",
                     "The differences are 36 − 33 = 3 and 39 − 36 = 3. Each time the start moves up by 1, each of the 3 "
                     "numbers goes up by 1, so the sum goes up by 3.",
                     "33 is odd, 36 is even and 39 is odd. The sums take turns.",
                     "Check: 33 + 3 = 36 and 36 + 3 = 39."],
                    "The sums 33, 36 and 39 go up by 3 each time and take turns, odd, even, odd")],
       ncert=["cons.def", "cons.boxes"], key_terms=["consecutive numbers", "successive sums", "even", "odd"],
       misconceptions=["M_CONSEC_PARITY", "M_SUCC_DIFF_ONE"], minutes=6),
     A("T4.C2", "Pair the Ends", "Understand",
       "Students find the sum of a run of consecutive numbers by pairing the two ends, without adding one by one.",
       textbook=["Let us see some more interesting patterns in sums."],
       teach=["Predict first: in 41 + 42 + 43 + 44 + 45 the first and last numbers are 41 and 45. What is 41 + 45, and "
              "what is 42 + 44?",
              "41 + 45 = 86 and 42 + 44 = 86. The pairs from the two ends make the same total.",
              "The middle number, 43, has no partner. It is half of 86, so the middle number is half of every pair "
              "total.",
              "So the sum is 86 + 86 + 43 = 215. That is 5 times the middle number: 5 × 43 = 215.",
              "With an even number of numbers there is no middle number. For 52 + 53 + 54 + 55: 52 + 55 = 107 and 53 + "
              "54 = 107, so the sum is 107 + 107 = 214, or 2 × 107.",
              "Rule: pair the numbers from the two ends. Every pair makes the same total. The sum is the number of pairs "
              "times the pair total, plus the middle number if there is one."],
       examples=[WE("Find 41 + 42 + 43 + 44 + 45 and 52 + 53 + 54 + 55 without adding one by one (practice values).",
                    ["Pair the ends of 41 + 42 + 43 + 44 + 45: 41 + 45 = 86 and 42 + 44 = 86.",
                     "The middle number 43 has no partner.",
                     "The sum is 86 + 86 + 43 = 215. Another way: 5 × 43 = 215.",
                     "Pair the ends of 52 + 53 + 54 + 55: 52 + 55 = 107 and 53 + 54 = 107.",
                     "There is no middle number. The sum is 107 + 107 = 214.",
                     "Check: 52 + 53 + 54 + 55 = 105 + 109 = 214."],
                    "41 + 42 + 43 + 44 + 45 = 215 and 52 + 53 + 54 + 55 = 214")],
       ncert=["cons.patterns"], key_terms=["pairs", "ends", "middle number", "total"],
       misconceptions=["M_FIRST_TIMES"], minutes=6),
     DOER("T4.C3", "Practice: Consecutive Sums Lab", "consecutive_sums_lab", "Understand",
          "Students explain the even and odd sums of consecutive numbers, find the difference between successive sums "
          "and add runs of consecutive numbers by pairing the ends.",
          ["The difference between successive sums is the number of numbers added.",
           "Two consecutive numbers make an odd sum, and four make an even sum.",
           "Pairs from the two ends of a run make the same total."],
          items=[FIO("cons.q1", "Sums of Consecutive Numbers: even or odd",
                     "In each of the boxes above, state whether the sums are even or odd. Explain why this is "
                     "happening.",
                     ["Box 1 (2 consecutive numbers): the sums 3, 5, 7 and 9 are all odd.",
                      "Why: two consecutive numbers are one even number and one odd number, and even plus odd is odd.",
                      "Box 2 (3 consecutive numbers): the sums 6, 9, 12 and 15 are even, odd, even, odd.",
                      "Why: the sum is 3 times the middle number, so it is odd when the middle number is odd and even when "
                      "the middle number is even. The middle numbers 2, 3, 4 and 5 take turns, even and odd.",
                      "Box 3 (4 consecutive numbers): the sums 10, 14, 18 and 22 are all even.",
                      "Why: 4 consecutive numbers make two pairs of consecutive numbers. Each pair adds to an odd number, "
                      "and odd plus odd is even.",
                      "Check: 1 + 2 + 3 + 4 = 10 is even."],
                     "Box 1: all odd, one even and one odd number. Box 2: even and odd in turn, 3 times the middle "
                     "number. Box 3: all even, two odd pairs.",
                     kind="exercise",
                     q_figure="Three boxes of sums of consecutive numbers: the sums of 2 consecutive numbers are 3, 5, 7 "
                              "and 9, the sums of 3 consecutive numbers are 6, 9, 12 and 15, and the sums of 4 "
                              "consecutive numbers are 10, 14, 18 and 22."),
                 FIO("cons.q2", "Sums of Consecutive Numbers: the difference between successive sums",
                     "What is the difference between two successive sums in each box? Is it the same throughout?",
                     ["Box 1: 5 − 3 = 2, 7 − 5 = 2 and 9 − 7 = 2. The difference is 2 each time.",
                      "Box 2: 9 − 6 = 3, 12 − 9 = 3 and 15 − 12 = 3. The difference is 3 each time.",
                      "Box 3: 14 − 10 = 4, 18 − 14 = 4 and 22 − 18 = 4. The difference is 4 each time.",
                      "Yes, it is the same throughout each box. It is the number of numbers being added, because each "
                      "number goes up by 1 when the start moves up by 1."],
                     "Box 1: 2; box 2: 3; box 3: 4. Yes, the same throughout each box.",
                     kind="exercise",
                     q_figure="Three boxes of sums of consecutive numbers: the sums of 2 consecutive numbers are 3, 5, 7 "
                              "and 9, the sums of 3 consecutive numbers are 6, 9, 12 and 15, and the sums of 4 "
                              "consecutive numbers are 10, 14, 18 and 22."),
                 FIO("cons.q3", "Sums of Consecutive Numbers: 5 and 6 consecutive numbers",
                     "What will be the difference between two successive sums for (a): 5 consecutive numbers; (b): 6 "
                     "consecutive numbers?",
                     ["(a): Each time the start moves up by 1, each of the 5 numbers goes up by 1, so the sum goes up by 5.",
                      "Check: 1 + 2 + 3 + 4 + 5 = 15 and 2 + 3 + 4 + 5 + 6 = 20, and 20 − 15 = 5.",
                      "(b): For 6 numbers the sum goes up by 6.",
                      "Check: 1 + 2 + 3 + 4 + 5 + 6 = 21 and 2 + 3 + 4 + 5 + 6 + 7 = 27, and 27 − 21 = 6."],
                     "(a): 5; (b): 6",
                     kind="exercise"),
                 FIO("cons.find", "Sums of Consecutive Numbers: sums without adding directly",
                     "Notice how the sums of 3, 4, and 5 consecutive numbers are related to the numbers being added. Use "
                     "your understanding to find the following sums without adding the numbers directly. (a): 67 + 68 + "
                     "69; (b): 24 + 25 + 26 + 27; (c): 48 + 49 + 50 + 51 + 52; (d): 237 + 238 + 239 + 240 + 241 + 242.",
                     ["(a): Pair the ends: 67 + 69 = 136. The middle number 68 stands alone: 136 + 68 = 204. Another way: "
                      "3 × 68 = 204.",
                      "(b): Pair the ends: 24 + 27 = 51 and 25 + 26 = 51. There are 2 pairs: 51 + 51 = 102.",
                      "(c): Pair the ends: 48 + 52 = 100 and 49 + 51 = 100. The middle number is 50: 100 + 100 + 50 = "
                      "250. Another way: 5 × 50 = 250.",
                      "(d): Pair the ends: 237 + 242 = 479, 238 + 241 = 479 and 239 + 240 = 479. There are 3 pairs: 479 "
                      "+ 479 + 479 = 1,437. Another way: 3 × 479 = 1,437.",
                      "Check (b): 24 + 25 + 26 + 27 = 49 + 53 = 102."],
                     "(a): 204; (b): 102; (c): 250; (d): 1,437",
                     kind="exercise",
                     s_figure="The four runs with arrows joining the first and last numbers and then the next pair in, "
                              "each pair marked with its total.")],
          misconceptions=["M_CONSEC_PARITY", "M_SUCC_DIFF_ONE", "M_FIRST_TIMES"])],
    key_terms=["consecutive numbers", "successive sums", "pairs"]))

# ============================== T5 Adding and Subtracting Large Numbers ====================================
TOPICS.append(TOPIC(
    "T5", "M2", "Adding and Subtracting Large Numbers",
    ["The Longest Land Route", "Subtracting Large Numbers", "Let Us Solve", "Let Us Do"], "Apply",
    "Students add and subtract numbers up to 5 digits with place value and with the digits aligned and no place names.",
    "Large numbers are added and subtracted in the same way as small numbers: one place at a time, starting with the "
    "ones, regrouping 10 of one place as 1 of the next place on the left, or 1 as 10 of the place on the right. When "
    "the digits are aligned, ones under ones and tens under tens, the place names are not needed.",
    [A("T5.C1", "Adding Large Numbers", "Apply",
       "Students add two numbers of 4 or 5 digits with place value, regrouping 10 of one place as 1 of the next place on "
       "the left.",
       textbook=["The longest distance one can travel by road is between Talon (in Russia) and Sagres (in Portugal). It "
                 "is 15,150 km long.",
                 "In 2019, the North-South Corridor was the longest land route within India, starting from Srinagar in "
                 "Jammu and Kashmir and ending at Kanniyakumari in Tamil Nadu. Do you know how long it was? Let us "
                 "find out.",
                 "Do you remember how to add large numbers?",
                 "Adding larger numbers is the same as adding smaller numbers."],
       teach=["Predict first: you add 3,486 and 2,729. Is it harder than adding 2 digit numbers, or are the steps the "
              "same?",
              "The steps are the same. Add one place at a time, from the ones to the thousands.",
              "Ones: 6 + 9 = 15. Write 5 and regroup 10 ones as 1 ten. Tens: 8 + 2 + 1 = 11. Write 1 and regroup 10 tens "
              "as 1 hundred.",
              "Hundreds: 4 + 7 + 1 = 12. Write 2 and regroup 10 hundreds as 1 thousand. Thousands: 3 + 2 + 1 = 6.",
              "The sum is 6,215. A 5 digit number has a ten thousands place too, and it is added in the same way.",
              "Rule: add one place at a time, starting with the ones, and regroup 10 of one place as 1 of the next place "
              "on the left."],
       examples=[WE("Add 3,486 and 2,729 (practice values).",
                    ["Write the numbers with ones under ones, tens under tens, hundreds under hundreds and thousands "
                     "under thousands.",
                     "Ones: 6 + 9 = 15. Write 5 and regroup 10 ones as 1 ten.",
                     "Tens: 8 + 2 + 1 = 11. Write 1 and regroup 10 tens as 1 hundred.",
                     "Hundreds: 4 + 7 + 1 = 12. Write 2 and regroup 10 hundreds as 1 thousand.",
                     "Thousands: 3 + 2 + 1 = 6. Write 6.",
                     "The sum is 6,215.",
                     "Check: 3,486 + 2,729 = 3,486 + 2,700 + 29 = 6,186 + 29 = 6,215."],
                    "6,215, because 3,486 + 2,729 = 6,215")],
       ncert=["land.intro", "land.nl", "land.same"], key_terms=["large numbers", "place value", "regroup", "sum"],
       misconceptions=["M_NO_CARRY"], minutes=7),
     A("T5.C2", "Subtracting Large Numbers", "Apply",
       "Students subtract two numbers of 4 or 5 digits with place value, regrouping across a zero, and check by adding.",
       textbook=["The place where passengers board a bus is called a bus stand or bus station. Similarly, a railway "
                 "station is the place where people board trains. The place where people board ships is called a port.",
                 "Do you remember how to subtract numbers using place value?",
                 "We subtract large numbers in the same way as smaller numbers."],
       teach=["Predict first: in 6,402 − 2,758 the tens digit of 6,402 is 0 and the ones digit is 2. How can you take 8 "
              "ones away?",
              "There are only 2 ones, so 8 ones cannot be taken away. There are no tens to regroup, so go to the "
              "hundreds first.",
              "Regroup 1 hundred as 10 tens. Now there are 3 hundreds and 10 tens. Then regroup 1 of those tens as 10 "
              "ones: 9 tens and 12 ones.",
              "Ones: 12 − 8 = 4. Tens: 9 − 5 = 4. Hundreds: 3 is less than 7, so regroup 1 thousand as 10 hundreds: 5 "
              "thousands and 13 hundreds, and 13 − 7 = 6. Thousands: 5 − 2 = 3.",
              "The difference is 3,644. Check by adding: 2,758 + 3,644 = 6,402.",
              "Rule: go place by place from the ones. If a place has too few, regroup 1 from the place on its left as 10 "
              "here. If that place is 0, go one more place to the left."],
       examples=[WE("Find 6,402 − 2,758 and check the answer (practice values).",
                    ["Write 6,402 with 2,758 below it, ones under ones.",
                     "Ones: 2 is less than 8 and the tens digit is 0, so regroup 1 hundred as 10 tens, then 1 ten as 10 "
                     "ones. Now there are 3 hundreds, 9 tens and 12 ones.",
                     "Ones: 12 − 8 = 4. Tens: 9 − 5 = 4.",
                     "Hundreds: 3 is less than 7, so regroup 1 thousand as 10 hundreds. Now there are 5 thousands and "
                     "13 hundreds.",
                     "Hundreds: 13 − 7 = 6. Thousands: 5 − 2 = 3.",
                     "The difference is 3,644.",
                     "Check: 2,758 + 3,644 = 6,402."],
                    "6,402 − 2,758 = 3,644, and 2,758 + 3,644 = 6,402")],
       ncert=["sub.intro", "sub.same"], key_terms=["subtract", "regroup", "difference", "zero"],
       misconceptions=["M_SMALL_FROM_BIG"], minutes=7),
     A("T5.C3", "Aligned Digits, No Labels", "Apply",
       "Students line up the digits of two numbers, ones under ones and tens under tens, and add or subtract without "
       "writing the place names.",
       textbook=["If we keep the digits aligned: Ones below Ones, Tens below Tens, and so on, we do not need to label "
                 "each place value.",
                 "Like addition, here too we can try not to write the positions of the digits and align the numbers "
                 "appropriately."],
       teach=["Predict first: you add 536 and 87. Where does the 7 of 87 go: under the 5, under the 3 or under the 6?",
              "The 7 is the ones digit of 87, so it goes under the ones digit of 536, which is the 6. The 8 goes under "
              "the 3.",
              "Always start from the right. Put ones under ones, tens under tens and hundreds under hundreds. A digit "
              "with nothing under it just comes down.",
              "You do not need to write the place names when the digits are lined up. Keep track of the places in your "
              "head.",
              "Add: 6 + 7 = 13, write 3 and regroup. 3 + 8 + 1 = 12, write 2 and regroup. 5 + 1 = 6. The sum is 623.",
              "Rule: line up the digits from the right, ones under ones, and then add or subtract one place at a time."],
       examples=[WE("Add 536 and 87, and subtract 275 from 913, with the digits aligned and no place names (practice "
                    "values).",
                    ["Line up 536 and 87 from the right: the 7 goes under the 6 and the 8 under the 3.",
                     "Ones: 6 + 7 = 13. Write 3 and regroup 10 ones as 1 ten.",
                     "Tens: 3 + 8 + 1 = 12. Write 2 and regroup 10 tens as 1 hundred.",
                     "Hundreds: 5 + 1 = 6. The sum is 623.",
                     "Line up 913 and 275 from the right. Ones: 3 is less than 5, so regroup 1 ten as 10 ones: 13 − 5 = "
                     "8.",
                     "Tens: the 1 ten was regrouped, so 0 tens are left, and 0 is less than 7. Regroup 1 hundred as 10 "
                     "tens: 10 − 7 = 3.",
                     "Hundreds: 9 − 1 = 8, and 8 − 2 = 6. The difference is 638.",
                     "Check: 275 + 638 = 913."],
                    "536 + 87 = 623 and 913 − 275 = 638")],
       ncert=["land.aligned", "sub.aligned"], key_terms=["aligned", "digits", "ones under ones"],
       misconceptions=["M_MISALIGN"], minutes=6),
     DOER("T5.C4", "Practice: Line Up and Solve", "line_up_and_solve", "Apply",
          "Students add and subtract large numbers with aligned digits, and use the sums and differences to solve the "
          "book's route and distance questions.",
          ["Line up the digits from the right, ones under ones, and work one place at a time.",
           "Regroup 10 of one place as 1 of the next place on the left when adding, and 1 as 10 of the place on the "
           "right when subtracting.",
           "Check a subtraction by adding the answer to the smaller number."],
          items=[FIO("land.ns", "Example 3: The North-South Corridor",
                     "One of the places on the North-South Corridor was 1,855 km from Srinagar and 1,862 km from "
                     "Kanniyakumari. What was the total length of the North-South Corridor in 2019?",
                     ["The total length is 1,855 km + 1,862 km, so add 1,855 and 1,862.",
                      "Ones: 5 + 2 = 7.",
                      "Tens: 5 + 6 = 11. Write 1 and regroup 10 tens as 1 hundred.",
                      "Hundreds: 8 + 8 + 1 = 17. Write 7 and regroup 10 hundreds as 1 thousand.",
                      "Thousands: 1 + 1 + 1 = 3. The sum is 3,717.",
                      "Check: 1,855 + 1,862 = 1,855 + 1,800 + 62 = 3,655 + 62 = 3,717."],
                     "The North-South Corridor was 3,717 km long in 2019.",
                     kind="example",
                     q_figure="A map of India with Srinagar at the top and Kanniyakumari at the bottom of a route, and a "
                              "point between them marked 1,855 km from Srinagar and 1,862 km from Kanniyakumari.",
                     s_figure="A chart with thousands, hundreds, tens and ones columns: 1,855 above 1,862, a 1 above the "
                              "hundreds column and a 1 above the thousands column for the two regroups, and the sum "
                              "3,717 below."),
                 FIO("land.mahesh", "Example 4: Mahesh's journey",
                     "Mahesh and his family decide to drive from Srinagar to Kanniyakumari. He spends ₹21,880 on fuel "
                     "and toll tax, and ₹38,900 on other expenses during this journey. How much did he spend in total?",
                     ["The total spent is the fuel and toll tax plus the other expenses, so add 21,880 and 38,900.",
                      "Ones: 0 + 0 = 0. Tens: 8 + 0 = 8.",
                      "Hundreds: 8 + 9 = 17. Write 7 and regroup 10 hundreds as 1 thousand.",
                      "Thousands: 1 + 8 + 1 = 10. Write 0 and regroup 10 thousands as 1 ten thousand.",
                      "Ten thousands: 2 + 3 + 1 = 6. The sum is 60,780.",
                      "Check: 21,880 + 38,900 = 22,000 + 38,780 = 60,780."],
                     "Mahesh spent ₹60,780 in total.",
                     kind="example",
                     s_figure="A chart with ten thousands, thousands, hundreds, tens and ones columns: 21,880 above "
                              "38,900, a 1 above the thousands column and a 1 above the ten thousands column for the two "
                              "regroups, and the sum 60,780 below."),
                 FIO("LUSbig.Q1", "Let Us Solve (adding large numbers): the six sums",
                     "Find the following sums. Try not to write ten thousands, thousands, hundreds, tens and ones at the "
                     "top. Just align the digits properly, at least for the smaller numbers. (a): 238 + 367; (b): 1,234 "
                     "+ 12,345; (c): 12 + 123; (d): 46,120 + 12,890; (e): 878 + 8,789; (f): 1,749 + 17,490.",
                     ["(a): Align the ones: 238 + 367. Ones: 8 + 7 = 15, write 5 and regroup. Tens: 3 + 6 + 1 = 10, "
                      "write 0 and regroup. Hundreds: 2 + 3 + 1 = 6. So 238 + 367 = 605.",
                      "(b): Align the ones: 1,234 + 12,345. Ones: 4 + 5 = 9. Tens: 3 + 4 = 7. Hundreds: 2 + 3 = 5. "
                      "Thousands: 1 + 2 = 3. Ten thousands: 0 + 1 = 1. So the sum is 13,579.",
                      "(c): 12 + 123: the 2 of 12 goes under the 3 of 123 and the 1 of 12 under the 2. Ones: 2 + 3 = 5. "
                      "Tens: 1 + 2 = 3. Hundreds: 1. So the sum is 135.",
                      "(d): 46,120 + 12,890. Ones: 0 + 0 = 0. Tens: 2 + 9 = 11, write 1 and regroup. Hundreds: 1 + 8 + 1 "
                      "= 10, write 0 and regroup. Thousands: 6 + 2 + 1 = 9. Ten thousands: 4 + 1 = 5. So the sum is "
                      "59,010.",
                      "(e): 878 + 8,789. Ones: 8 + 9 = 17, write 7 and regroup. Tens: 7 + 8 + 1 = 16, write 6 and "
                      "regroup. Hundreds: 8 + 7 + 1 = 16, write 6 and regroup. Thousands: 8 + 1 = 9. So the sum is "
                      "9,667.",
                      "(f): 1,749 + 17,490. Ones: 9 + 0 = 9. Tens: 4 + 9 = 13, write 3 and regroup. Hundreds: 7 + 4 + 1 "
                      "= 12, write 2 and regroup. Thousands: 1 + 7 + 1 = 9. Ten thousands: 0 + 1 = 1. So the sum is "
                      "19,239.",
                      "Check (b): 1,234 + 12,345 = 12,345 + 1,000 + 234 = 13,345 + 234 = 13,579."],
                     "(a): 605; (b): 13,579; (c): 135; (d): 59,010; (e): 9,667; (f): 19,239",
                     kind="exercise"),
                 FIO("land.trip", "Let Us Solve (adding large numbers): the great Indian road trip",
                     "The great Indian road trip! Nazrana and her friends planned a road trip across India, starting "
                     "from Delhi. They first drove to Mumbai, then Goa, then Hyderabad, and finally Puri. Look at the "
                     "distances marked on the map and help them find the total distance travelled.",
                     ["The legs are Delhi to Mumbai, Mumbai to Goa, Goa to Hyderabad and Hyderabad to Puri: 1,600 km, "
                      "590 km, 670 km and 1,055 km.",
                      "Add the first two legs: 1,600 + 590 = 2,190.",
                      "Add the third leg: 2,190 + 670 = 2,860.",
                      "Add the last leg: 2,860 + 1,055 = 3,915.",
                      "Check: 1,600 + 1,055 = 2,655 and 590 + 670 = 1,260, and 2,655 + 1,260 = 3,915."],
                     "They travelled 3,915 km in all.",
                     kind="exercise",
                     q_figure="A map of India with a route from Delhi to Mumbai, then Goa, then Hyderabad, then Puri, "
                              "with the four legs marked 1,600 km, 590 km, 670 km and 1,055 km.",
                     s_figure="The four legs written in a row with a plus sign between them and the total 3,915 km."),
                 FIO("land.closest", "Let Us Solve (adding large numbers): the closest sum",
                     "Find 2 numbers among 5,205, 6,220, 7,095, 8,455, and 4,840 whose sum is closest to the following. "
                     "(a): 10,000; (b): 15,000; (c): 13,000; (d): 16,000.",
                     ["Add every pair of numbers. There are 10 pairs.",
                      "5,205 + 6,220 = 11,425; 5,205 + 7,095 = 12,300; 5,205 + 8,455 = 13,660; 5,205 + 4,840 = 10,045.",
                      "6,220 + 7,095 = 13,315; 6,220 + 8,455 = 14,675; 6,220 + 4,840 = 11,060.",
                      "7,095 + 8,455 = 15,550; 7,095 + 4,840 = 11,935; 8,455 + 4,840 = 13,295.",
                      "(a): The closest to 10,000 is 10,045, only 45 away: 5,205 and 4,840.",
                      "(b): The closest to 15,000 is 14,675, which is 325 away: 6,220 and 8,455. The next, 15,550, is "
                      "550 away.",
                      "(c): The closest to 13,000 is 13,295, which is 295 away: 8,455 and 4,840. The next, 13,315, is "
                      "315 away.",
                      "(d): The closest to 16,000 is 15,550, which is 450 away: 7,095 and 8,455.",
                      "Check (c): 13,295 − 13,000 = 295 and 13,315 − 13,000 = 315, and 295 is less than 315."],
                     "(a): 5,205 and 4,840; (b): 6,220 and 8,455; (c): 8,455 and 4,840; (d): 7,095 and 8,455",
                     kind="exercise"),
                 FIO("sub.ship", "Example 5: The ship from Mumbai to Chennai",
                     "The total distance of the sea route from Mumbai to Chennai is 2,700 km. A ship starting from "
                     "Mumbai first reaches the Cochin port, travelling 1,083 km by sea. How much more distance does it "
                     "have to travel to reach the Chennai port?",
                     ["The distance still to travel is 2,700 km − 1,083 km, so subtract 1,083 from 2,700.",
                      "Ones: 0 is less than 3 and the tens digit is 0, so regroup 1 hundred as 10 tens, then 1 ten as 10 "
                      "ones. Now there are 6 hundreds, 9 tens and 10 ones.",
                      "Ones: 10 − 3 = 7. Tens: 9 − 8 = 1.",
                      "Hundreds: 6 − 0 = 6. Thousands: 2 − 1 = 1.",
                      "The difference is 1,617.",
                      "Check by adding: 1,083 + 1,617 = 2,700."],
                     "The ship has to travel 1,617 km more.",
                     kind="example",
                     q_figure="A map of India with Mumbai port, Cochin port and Chennai port on a sea route, the part "
                              "from Mumbai to Cochin marked 1,083 km and the whole sea route from Mumbai to Chennai "
                              "marked 2,700 km.",
                     s_figure="A chart with thousands, hundreds, tens and ones columns: 2,700 above 1,083 with the "
                              "regroup marks 6 hundreds, 9 tens and 10 ones, and the difference 1,617 below."),
                 FIO("sub.talon", "Example 6: The longest land route",
                     "As you learnt earlier, the longest land route is 15,150 km between Talon (Russia) and Sagres "
                     "(Portugal). The longest highway in Africa is 10,228 km long, connecting the cities of Cairo, in "
                     "Egypt and Cape Town, in South Africa. How much longer is the land route between Talon and Sagres "
                     "compared to the highway between Cairo and Cape Town?",
                     ["The difference is 15,150 km − 10,228 km, so subtract 10,228 from 15,150.",
                      "Ones: 0 is less than 8, so regroup 1 ten as 10 ones. Now there are 4 tens and 10 ones. Ones: 10 − "
                      "8 = 2.",
                      "Tens: 4 − 2 = 2.",
                      "Hundreds: 1 is less than 2, so regroup 1 thousand as 10 hundreds. Now there are 4 thousands and "
                      "11 hundreds. Hundreds: 11 − 2 = 9.",
                      "Thousands: 4 − 0 = 4. Ten thousands: 1 − 1 = 0.",
                      "The difference is 4,922.",
                      "Check by adding: 10,228 + 4,922 = 15,150."],
                     "The land route is 4,922 km longer.",
                     kind="example",
                     s_figure="A chart with ten thousands, thousands, hundreds, tens and ones columns: 15,150 above "
                              "10,228 with the regroup marks 4 thousands, 11 hundreds, 4 tens and 10 ones, and the "
                              "difference 4,922 below."),
                 FIO("LUSsub.Q1", "Let Us Solve (subtracting large numbers): the six subtractions",
                     "Subtract the following. Try not to write ten thousands, thousands, hundreds, tens and ones at the "
                     "top. Align the digits carefully. (a): 4,578 − 2,222; (b): 15,324 − 11,780; (c): 5,423 − 423; (d): "
                     "123 − 12; (e): 77,777 − 777; (f): 826 − 752.",
                     ["(a): Ones: 8 − 2 = 6. Tens: 7 − 2 = 5. Hundreds: 5 − 2 = 3. Thousands: 4 − 2 = 2. So 4,578 − "
                      "2,222 = 2,356.",
                      "(b): Ones: 4 − 0 = 4. Tens: 2 is less than 8, so regroup 1 hundred as 10 tens: 12 − 8 = 4. "
                      "Hundreds: 2 is less than 7, so regroup 1 thousand as 10 hundreds: 12 − 7 = 5. Thousands: 4 − 1 "
                      "= 3. Ten thousands: 1 − 1 = 0. So the difference is 3,544.",
                      "(c): Align the ones of 423 under the ones of 5,423. Ones: 3 − 3 = 0. Tens: 2 − 2 = 0. Hundreds: "
                      "4 − 4 = 0. Thousands: 5 comes down. So the difference is 5,000.",
                      "(d): 123 − 12: the 2 goes under the 3 and the 1 under the 2. Ones: 3 − 2 = 1. Tens: 2 − 1 = 1. "
                      "Hundreds: 1 comes down. So the difference is 111.",
                      "(e): 77,777 − 777: align the ones. Ones: 7 − 7 = 0. Tens: 7 − 7 = 0. Hundreds: 7 − 7 = 0. The "
                      "thousands 7 and the ten thousands 7 come down. So the difference is 77,000.",
                      "(f): 826 − 752. Ones: 6 − 2 = 4. Tens: 2 is less than 5, so regroup 1 hundred as 10 tens: 12 − 5 "
                      "= 7. Hundreds: 7 − 7 = 0. So the difference is 74.",
                      "Check (f): 752 + 74 = 826."],
                     "(a): 2,356; (b): 3,544; (c): 5,000; (d): 111; (e): 77,000; (f): 74",
                     kind="exercise"),
                 FIO("LUD.Q1", "Let Us Do (add): nine sums",
                     "Add. (a): 2,009 + 7,388; (b): 26,444 + 71,111; (c): 777 + 888; (d): 1,234 + 1,234; (e): 56 + "
                     "56,789; (f): 777 + 77,777; (g): 5,922 + 9,221; (h): 4,321 + 8,765; (i): 50,050 + 55,000.",
                     ["(a): Ones: 9 + 8 = 17, write 7 and regroup. Tens: 0 + 8 + 1 = 9. Hundreds: 0 + 3 = 3. Thousands: "
                      "2 + 7 = 9. So 2,009 + 7,388 = 9,397.",
                      "(b): 26,444 + 71,111: no place makes 10 or more. Ones: 4 + 1 = 5. Tens: 4 + 1 = 5. Hundreds: 4 + "
                      "1 = 5. Thousands: 6 + 1 = 7. Ten thousands: 2 + 7 = 9. So the sum is 97,555.",
                      "(c): 777 + 888. Ones: 7 + 8 = 15, write 5 and regroup. Tens: 7 + 8 + 1 = 16, write 6 and "
                      "regroup. Hundreds: 7 + 8 + 1 = 16, write 6 and regroup 10 hundreds as 1 thousand. So the sum is "
                      "1,665.",
                      "(d): 1,234 + 1,234: each place doubles. 4 + 4 = 8, 3 + 3 = 6, 2 + 2 = 4, 1 + 1 = 2. So the sum "
                      "is 2,468.",
                      "(e): 56 + 56,789: align the ones. Ones: 6 + 9 = 15, write 5 and regroup. Tens: 5 + 8 + 1 = 14, "
                      "write 4 and regroup. Hundreds: 7 + 1 = 8. The thousands 6 and the ten thousands 5 come down. So "
                      "the sum is 56,845.",
                      "(f): 777 + 77,777. Ones: 7 + 7 = 14, write 4 and regroup. Tens: 7 + 7 + 1 = 15, write 5 and "
                      "regroup. Hundreds: 7 + 7 + 1 = 15, write 5 and regroup. Thousands: 7 + 1 = 8. Ten thousands: 7. "
                      "So the sum is 78,554.",
                      "(g): 5,922 + 9,221. Ones: 2 + 1 = 3. Tens: 2 + 2 = 4. Hundreds: 9 + 2 = 11, write 1 and regroup. "
                      "Thousands: 5 + 9 + 1 = 15, write 5 and regroup 10 thousands as 1 ten thousand. So the sum is "
                      "15,143.",
                      "(h): 4,321 + 8,765. Ones: 1 + 5 = 6. Tens: 2 + 6 = 8. Hundreds: 3 + 7 = 10, write 0 and regroup. "
                      "Thousands: 4 + 8 + 1 = 13, write 3 and regroup. So the sum is 13,086.",
                      "(i): 50,050 + 55,000. Ones: 0. Tens: 5. Hundreds: 0. Thousands: 0 + 5 = 5. Ten thousands: 5 + 5 = "
                      "10, so write 0 and put the 1 in a new place on the left. The sum is 1,05,050.",
                      "Check (i): 50,000 + 55,000 = 1,05,000, and 1,05,000 + 50 = 1,05,050."],
                     "(a): 9,397; (b): 97,555; (c): 1,665; (d): 2,468; (e): 56,845; (f): 78,554; (g): 15,143; (h): "
                     "13,086; (i): 1,05,050",
                     kind="exercise"),
                 FIO("LUD.Q2", "Let Us Do (subtract): nine subtractions",
                     "Subtract. (a): 458 − 226; (b): 7,777 − 4,449; (c): 65,447 − 47,299; (d): 1,234 − 123; (e): 12,345 "
                     "− 1,234; (f): 56,789 − 56; (g): 87,326 − 11,111; (h): 878 − 52; (i): 749 − 222.",
                     ["(a): 458 − 226. Ones: 8 − 6 = 2. Tens: 5 − 2 = 3. Hundreds: 4 − 2 = 2. So the difference is 232.",
                      "(b): 7,777 − 4,449. Ones: 7 is less than 9, so regroup: 17 − 9 = 8. Tens: 7 − 1 = 6, and 6 − 4 = "
                      "2. Hundreds: 7 − 4 = 3. Thousands: 7 − 4 = 3. So the difference is 3,328.",
                      "(c): 65,447 − 47,299. Ones: 7 is less than 9, so regroup: 17 − 9 = 8. Tens: 4 − 1 = 3, and 3 is "
                      "less than 9, so regroup: 13 − 9 = 4. Hundreds: 4 − 1 = 3, and 3 − 2 = 1. Thousands: 5 is less "
                      "than 7, so regroup: 15 − 7 = 8. Ten thousands: 6 − 1 = 5, and 5 − 4 = 1. So the difference is "
                      "18,148.",
                      "(d): 1,234 − 123. Ones: 4 − 3 = 1. Tens: 3 − 2 = 1. Hundreds: 2 − 1 = 1. Thousands: 1 comes down. "
                      "So the difference is 1,111.",
                      "(e): 12,345 − 1,234. Ones: 5 − 4 = 1. Tens: 4 − 3 = 1. Hundreds: 3 − 2 = 1. Thousands: 2 − 1 = 1. "
                      "Ten thousands: 1 comes down. So the difference is 11,111.",
                      "(f): 56,789 − 56: align the ones. Ones: 9 − 6 = 3. Tens: 8 − 5 = 3. The hundreds 7, thousands 6 "
                      "and ten thousands 5 come down. So the difference is 56,733.",
                      "(g): 87,326 − 11,111. Ones: 6 − 1 = 5. Tens: 2 − 1 = 1. Hundreds: 3 − 1 = 2. Thousands: 7 − 1 = "
                      "6. Ten thousands: 8 − 1 = 7. So the difference is 76,215.",
                      "(h): 878 − 52. Ones: 8 − 2 = 6. Tens: 7 − 5 = 2. Hundreds: 8 comes down. So the difference is 826.",
                      "(i): 749 − 222. Ones: 9 − 2 = 7. Tens: 4 − 2 = 2. Hundreds: 7 − 2 = 5. So the difference is 527.",
                      "Check (c): 47,299 + 18,148 = 65,447."],
                     "(a): 232; (b): 3,328; (c): 18,148; (d): 1,111; (e): 11,111; (f): 56,733; (g): 76,215; (h): 826; "
                     "(i): 527",
                     kind="exercise")],
          misconceptions=["M_NO_CARRY", "M_SMALL_FROM_BIG", "M_MISALIGN"])],
    key_terms=["large numbers", "aligned", "regroup", "sum", "difference"]))

# ============================== T6 Journey Problems ========================================================
TOPICS.append(TOPIC(
    "T6", "M2", "Journey Problems", ["Let Us Solve", "Let Us Do"], "Apply",
    "Students solve journey problems that add, take away and compare amounts, and estimate before they calculate.",
    "In a journey problem, read the story one step at a time and decide whether to add, take away or find how many more. "
    "Estimating first, by rounding each amount up to a friendly number, tells you quickly whether an answer can be "
    "right.",
    [A("T6.C1", "Add or Subtract? Reading a Journey Problem", "Apply",
       "Students decide whether a story asks to add, take away or find how many more, and solve a problem that has "
       "more than one step.",
       teach=["Predict first: a traveller starts with ₹15,000, spends ₹4,250, is paid back ₹2,000, then spends ₹3,160. "
              "Which steps add and which take away?",
              "Read the story one step at a time. Words like spends, pays and left mean take away. Words like gets, is "
              "given and in all mean add.",
              "Start with ₹15,000. Spends ₹4,250: take away, 15,000 − 4,250 = 10,750.",
              "Is paid back ₹2,000: add, 10,750 + 2,000 = 12,750. Spends ₹3,160: take away, 12,750 − 3,160 = 9,590.",
              "To find how many more or how many less, subtract the smaller number from the bigger one. If the red bag has "
              "8 less than the blue bag, the blue bag has 8 more: add 8 to the red bag to get the blue bag.",
              "Rule: read the story one step at a time and decide at each step whether to add or take away. Check the "
              "last answer by going back through the steps."],
       examples=[WE("A traveller starts a trip with ₹15,000. She spends ₹4,250 on fuel, is paid back ₹2,000 by a friend, "
                    "then spends ₹3,160 on tickets. How much money is left? (practice values)",
                    ["Start with 15,000 rupees.",
                     "She spends 4,250 rupees, so take away: 15,000 − 4,250 = 10,750.",
                     "She is paid back 2,000 rupees, so add: 10,750 + 2,000 = 12,750.",
                     "She spends 3,160 rupees on tickets, so take away: 12,750 − 3,160 = 9,590.",
                     "She is left with ₹9,590.",
                     "Check: the money spent is 4,250 + 3,160 = 7,410, and 15,000 + 2,000 − 7,410 = 9,590."],
                    "₹9,590 is left")],
       key_terms=["add", "take away", "how many more", "step"], misconceptions=["M_LESS_THAN_TAKE"], minutes=6),
     A("T6.C2", "Estimate First, Then Check", "Apply",
       "Students estimate whether an amount of money is enough by rounding each price up to the next thousand, then "
       "check with exact addition and subtraction.",
       textbook=["Estimate whether the school council has raised enough money to make the purchases. Share your thoughts "
                 "in the class.",
                 "Check your estimate with calculations."],
       teach=["Predict first: a council has ₹50,000 and wants to buy things that cost ₹19,820, ₹14,480 and ₹9,765. "
              "Without adding exactly, can you tell if the money is enough?",
              "Round each price up to the next thousand: ₹19,820 becomes ₹20,000, ₹14,480 becomes ₹15,000 and ₹9,765 "
              "becomes ₹10,000.",
              "Add the rounded prices: 20,000 + 15,000 + 10,000 = 45,000. The real prices are a little less, so the real "
              "total is less than ₹45,000.",
              "₹45,000 is less than ₹50,000, so the money is enough. That is the estimate.",
              "Now check: 19,820 + 14,480 = 34,300 and 34,300 + 9,765 = 44,065. Then 50,000 − 44,065 = 5,935 is left.",
              "Rule: an estimate is a quick answer that is close, not exact. Round the prices up, add and compare, then "
              "check with the real numbers."],
       examples=[WE("A school council has ₹50,000 and wants to buy things that cost ₹19,820, ₹14,480 and ₹9,765. "
                    "Estimate whether the money is enough, then check (practice values).",
                    ["Round each price up to the next thousand: 19,820 becomes 20,000, 14,480 becomes 15,000 and 9,765 "
                     "becomes 10,000.",
                     "Add the rounded prices: 20,000 + 15,000 + 10,000 = 45,000.",
                     "The real prices are less than the rounded prices, so the real total is less than 45,000, and 45,000 "
                     "is less than 50,000. The estimate says: enough.",
                     "Check with the real prices: 19,820 + 14,480 = 34,300.",
                     "34,300 + 9,765 = 44,065.",
                     "50,000 − 44,065 = 5,935 is left, so the money is enough.",
                     "Check: 44,065 + 5,935 = 50,000."],
                    "Enough: the total is ₹44,065 and ₹5,935 is left")],
       key_terms=["estimate", "round up", "enough", "check"], misconceptions=["M_ESTIMATE_EXACT"], minutes=6),
     DOER("T6.C3", "Practice: Journey Problems", None, "Apply",
          "Students solve journey problems by deciding when to add, take away or find how many more, and by estimating "
          "first.",
          ["Read the story one step at a time and decide at each step whether to add or take away.",
           "To find how many more or how many less, subtract the smaller number from the bigger one.",
           "Estimate first by rounding up, then check with the real numbers."],
          items=[FIO("mary", "Let Us Solve (journey problems): Mary's train journey",
                     "Mary's train journey to Delhi. Mary is on a train journey. She starts from Kolkata with ₹12,540. "
                     "She spends ₹3,275 on food and other expenses during her trip to Varanasi. In Varanasi, her uncle "
                     "gives her a gift worth ₹4,900. She then travels to Delhi, spending ₹2,645 on the train ticket. She "
                     "spends ₹1,275 on souvenirs in Delhi. How much money is Mary left with at the end of the Delhi "
                     "trip?",
                     ["Mary starts with ₹12,540.",
                      "She spends ₹3,275 on the way to Varanasi, so take away: 12,540 − 3,275 = 9,265.",
                      "Her uncle gives her ₹4,900, so add: 9,265 + 4,900 = 14,165.",
                      "She spends ₹2,645 on the train ticket, so take away: 14,165 − 2,645 = 11,520.",
                      "She spends ₹1,275 on souvenirs, so take away: 11,520 − 1,275 = 10,245.",
                      "Check: the money spent is 3,275 + 2,645 + 1,275 = 7,195, and 12,540 + 4,900 − 7,195 = 10,245."],
                     "Mary is left with ₹10,245.",
                     kind="exercise",
                     q_figure="A route from Kolkata to Varanasi to Delhi, with ₹3,275 marked at Kolkata, ₹2,645 at "
                              "Varanasi and ₹1,275 at Delhi."),
                 FIO("council", "Let Us Solve (journey problems): the school council",
                     "Members of a school council have raised ₹70,500. They plan to setup a Maths Lab with some games "
                     "and models worth ₹39,785, buy library books worth ₹9,545, and purchase sports equipment worth "
                     "₹19,548. (a): Estimate whether the school council has raised enough money to make the purchases. "
                     "Share your thoughts in the class. (b): Check your estimate with calculations.",
                     ["(a): Round each amount up to the next thousand: 39,785 becomes 40,000, 9,545 becomes 10,000 and "
                      "19,548 becomes 20,000.",
                      "Add the rounded amounts: 40,000 + 10,000 + 20,000 = 70,000. The real amounts are a little less, "
                      "so the real total is less than 70,000.",
                      "70,000 is less than ₹70,500, so the council has raised enough. That is the estimate.",
                      "(b): Add the real amounts: 39,785 + 9,545 = 49,330.",
                      "49,330 + 19,548 = 68,878.",
                      "Take the total from the money raised: 70,500 − 68,878 = 1,622.",
                      "Check: 68,878 + 1,622 = 70,500."],
                     "(a): Sample estimate: about ₹70,000, less than ₹70,500, so enough. Your answer may differ. (b): "
                     "₹68,878 in all, ₹1,622 left.",
                     kind="exercise"),
                 FIO("truck", "Let Us Solve (journey problems): the truck",
                     "A truck can carry 8,250 kg of goods. A factory loads 3,675 kg of cement and 2,850 kg of steel on "
                     "it. (a): What is the total weight loaded onto the truck? (b): How much more weight can the truck "
                     "carry before reaching its maximum capacity?",
                     ["(a): The weight loaded is 3,675 kg + 2,850 kg, so add 3,675 and 2,850.",
                      "Ones: 5 + 0 = 5. Tens: 7 + 5 = 12, write 2 and regroup. Hundreds: 6 + 8 + 1 = 15, write 5 and "
                      "regroup. Thousands: 3 + 2 + 1 = 6. The total is 6,525.",
                      "(b): The truck can carry 8,250 kg. The room left is 8,250 kg − 6,525 kg, so subtract 6,525 from "
                      "8,250.",
                      "Ones: 0 is less than 5, so regroup 1 ten as 10 ones: 10 − 5 = 5. Tens: 5 − 1 = 4, and 4 − 2 = 2. "
                      "Hundreds: 2 is less than 5, so regroup 1 thousand as 10 hundreds: 12 − 5 = 7. Thousands: 8 − 1 = "
                      "7, and 7 − 6 = 1. The difference is 1,725.",
                      "Check: 6,525 + 1,725 = 8,250."],
                     "(a): 6,525 kg; (b): 1,725 kg",
                     kind="exercise"),
                 FIO("LUD.Q3", "Let Us Do (problems): Ambrish's savings",
                     "Ambrish saved ₹92,375 over a year to buy cows and goats. He buys a cow for ₹26,000 and a goat for "
                     "₹17,000. He also buys a milking machine for ₹19,873. Does he have enough money to buy these? How "
                     "much more or less does he have than he needs?",
                     ["The things cost ₹26,000 for the cow, ₹17,000 for the goat and ₹19,873 for the milking machine.",
                      "Add the cow and the goat: 26,000 + 17,000 = 43,000.",
                      "Add the milking machine: 43,000 + 19,873 = 62,873. That is the money he needs.",
                      "He saved ₹92,375, and 92,375 is more than 62,873, so he has enough money.",
                      "How much more: 92,375 − 62,873 = 29,502.",
                      "Check: 62,873 + 29,502 = 92,375."],
                     "Yes, he has enough. He needs ₹62,873 and has ₹29,502 more than he needs.",
                     kind="exercise"),
                 FIO("LUD.Q4", "Let Us Do (problems): the factory",
                     "A factory produces 54,000 nuts and bolts in a day. An order is placed for 85,300 nuts and bolts. "
                     "How many more nuts and bolts does the factory need to produce to complete the order?",
                     ["The order is for 85,300 and the factory makes 54,000 in a day, so it needs to make more.",
                      "The number still needed is 85,300 − 54,000.",
                      "Subtract place by place: thousands 5 − 4 = 1 and ten thousands 8 − 5 = 3, and the 300 stays. The "
                      "difference is 31,300.",
                      "Check: 54,000 + 31,300 = 85,300."],
                     "The factory needs to produce 31,300 more nuts and bolts.",
                     kind="exercise"),
                 FIO("LUD.Q5", "Let Us Do (problems): the runs",
                     "Virat Kohli has scored 27,599 runs. He has 6,758 runs less than Sachin Tendulkar. How many runs has "
                     "Sachin Tendulkar scored?",
                     ["Virat Kohli has 6,758 runs less than Sachin Tendulkar, so Sachin Tendulkar has 6,758 runs more "
                      "than Virat Kohli.",
                      "Add 6,758 to 27,599: 27,599 + 6,758.",
                      "Ones: 9 + 8 = 17, write 7 and regroup. Tens: 9 + 5 + 1 = 15, write 5 and regroup. Hundreds: 5 + "
                      "7 + 1 = 13, write 3 and regroup. Thousands: 7 + 6 + 1 = 14, write 4 and regroup. Ten thousands: "
                      "2 + 1 = 3. The sum is 34,357.",
                      "Check: 34,357 − 6,758 = 27,599."],
                     "Sachin Tendulkar has scored 34,357 runs.",
                     kind="exercise")],
          misconceptions=["M_LESS_THAN_TAKE", "M_ESTIMATE_EXACT"])],
    key_terms=["journey problem", "estimate", "add", "take away"]))
