# -*- coding: utf-8 -*-
"""Topics T10 to T16 of Class 5 Chapter 6, The Dairy Farm: T10 Check, Check! (module M3), then T11 Same Product Easy
Ways, T12 Estimates and Digit Puzzles, T13 The King's Reward, T14 Multiplication Patterns, T15 Let Us Solve: Putting It
Together and T16 the chapter revision (module M4). None of these topics has a tool.
Every teaching concept has one worked example with the plan's own numbers; every book question is an FIO item of its
topic's DOER, in the book's order. Reading adopted for the unclear points of the book: see content.SOLUTION_NOTES."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T10 Check, Check! ==========================================================
TOPICS.append(TOPIC(
    "T10", "M3", "Check, Check!", ["Check, Check!"], "Analyze",
    "Students check a worked multiplication by estimating the product and testing each line, find a missing zero or a "
    "wrong place value, and write the correct working and product.",
    "A neat working can still be wrong. Estimate the product first, then check each line for its zeros and its place "
    "value, and add the lines again. If the answer is wrong, find the slip and write the right working.",
    [A("T10.C1", "Check a Solution", "Analyze",
       "Students check a worked multiplication by estimating first, testing every line for its zeros and place value, "
       "adding the lines again, and writing the correct product when a slip is found.",
       textbook=["Check if the following children's solutions are correct. If correct, explain why the solution is "
                 "correct. If it is incorrect, then identify the error and correct the solution."],
       teach=["Predict first: a friend says that the answer to 24 × 31 is 96. Before you multiply anything, how can "
              "you tell in a few seconds that 96 cannot be right?",
              "Estimate first. 31 is close to 30, so 24 × 31 is close to 24 × 30 = 720. An answer of 96 is far too "
              "small.",
              "When an answer looks wrong, look at each line of the working. Ask: does this line have the right place "
              "value, and does it have the right zeros?",
              "The friend wrote 24 × 3 = 72. But the 3 in 31 is 3 tens, so that line must be 24 × 30 = 720. The zero "
              "was missing.",
              "Look for three slips: a missing zero at the end of a line for tens or hundreds, a digit read with the "
              "wrong place value, and lines that are added wrongly.",
              "Add the lines again yourself. Do not trust the total that is written.",
              "If every line is right and the lines add up, the solution is correct. Say why: each line is one small "
              "product with its right zeros, and the total is their sum.",
              "Rule: estimate first, check each line for its zeros and place value, add again, and when you find a "
              "slip, write the right lines and the right product."],
       examples=[WE("A friend solved 24 × 31 in two lines: 24 × 1 = 24 and 24 × 3 = 72. Then the friend added 24 + 72 "
                    "= 96 and said that the answer is 96. Check the solution. Is it correct? If it is not, find the "
                    "error and correct it.",
                    ["Estimate first. 31 is close to 30, so 24 × 31 is close to 24 × 30 = 720.",
                     "The friend's answer 96 is far below 720, so something is wrong.",
                     "Check line 1. The 1 in 31 is 1 one, so 24 × 1 = 24 is right.",
                     "Check line 2. The 3 in 31 is 3 tens, not 3 ones, so the line must be 24 × 30, not 24 × 3.",
                     "24 × 3 = 72, so 24 × 30 = 720. The friend left out the zero.",
                     "Add the right lines: 24 + 720 = 744.",
                     "Check: 744 is close to the estimate 720, and 24 × 31 = 24 × 30 + 24 = 720 + 24 = 744."],
                    "Not correct. The line for the 3 tens is 24 × 30 = 720, not 72. The right product is 24 + 720 = "
                    "744")],
       key_terms=["check", "solution", "estimate", "missing zero", "place value"],
       misconceptions=["M_MISSING_ZERO", "M_PLACE_SLIP"], minutes=6),
     DOER("T10.C2", "Practice: Check, Check!", None, "Analyze",
          "Students check five children's solutions by estimating and testing each line, say which are correct and why, "
          "and correct each wrong solution with the right working and product.",
          ["Estimate first. If the answer is far from the estimate, there is a slip.",
           "Check every line: the zeros at the end and the place value of each digit.",
           "Add the lines again. If the solution is wrong, write the right lines and the right product."],
          items=[FIO("ck.a", "Check, Check!: (a) Asma's solution",
                     "Check if the following children's solutions are correct. If correct, explain why the solution is "
                     "correct. If it is incorrect, then identify the error and correct the solution. Asma's solution "
                     "for 46 × 59: the four lines 2,000, 300, 360 and 54 are added to get 2,714.",
                     ["Estimate first: 46 is close to 50 and 59 is close to 60, so 46 × 59 is about 50 × 60 = 3,000.",
                      "Split both numbers: 46 = 40 + 6 and 59 = 50 + 9.",
                      "Check line 1: 40 × 50 = 2,000, and the line shows 2,000. Right.",
                      "Check line 2: 6 × 50 = 300, and the line shows 300. Right.",
                      "Check line 3: 40 × 9 = 360, and the line shows 360. Right.",
                      "Check line 4: 6 × 9 = 54, and the line shows 54. Right.",
                      "Add the lines again: 2,000 + 300 + 360 + 54 = 2,714. The total shown is right.",
                      "Check: 2,714 is a little less than the estimate 3,000, which fits because both numbers were "
                      "rounded up. Also 46 × 59 = 46 × 60 − 46 = 2,760 − 46 = 2,714."],
                     "Correct. The four lines are the four small products of 46 split into 40 and 6 and 59 split into "
                     "50 and 9, each with its right zeros, and 2,000 + 300 + 360 + 54 = 2,714.",
                     kind="prompt",
                     q_figure="Asma's working for 46 times 59: the four lines 2,000, 300, 360 and 54 one under the "
                              "other, then a line and the total 2,714.",
                     s_figure="A box with columns 40 and 6 and rows 50 and 9: the cells 2,000, 300, 360 and 54 are "
                              "Asma's four lines, and the total is 2,714."),
                 FIO("ck.b", "Check, Check!: (b) Pankaj's solution",
                     "Pankaj's solution for 203 × 54: 80 + 12 = 92 and 100 + 15 = 115, so the answer is 135. Is it "
                     "correct? If correct, explain why. If it is incorrect, identify the error and correct the "
                     "solution.",
                     ["Estimate first: 203 is close to 200 and 54 is close to 50, so 203 × 54 is about 200 × 50 = "
                      "10,000.",
                      "Pankaj's answer 135 is far below 10,000, so the solution is wrong.",
                      "Error 1: Pankaj read 203 as 20 + 3. The 2 is 2 hundreds, so 203 = 200 + 3.",
                      "Error 2: the line for the 5 in 54 has no zero. The 5 is 5 tens, so that line is for 50, not 5.",
                      "Error 3: his two lines add to 92 + 115 = 207, not 135, so the printed total is not even the "
                      "sum of his own lines.",
                      "Right working, line for the 4 ones: 4 × 200 = 800 and 4 × 3 = 12, so 800 + 12 = 812.",
                      "Right working, line for the 5 tens: 50 × 200 = 10,000 and 50 × 3 = 150, so 10,000 + 150 = "
                      "10,150.",
                      "Add the right lines: 812 + 10,150 = 10,962.",
                      "Check: 10,962 is close to the estimate 10,000, and 203 × 54 = 203 × 50 + 203 × 4 = 10,150 + "
                      "812 = 10,962."],
                     "Not correct. Errors: 203 read as 20 + 3, no zero in the line for 50, and 92 + 115 = 207, not "
                     "135. Right product: 812 + 10,150 = 10,962.",
                     kind="prompt",
                     q_figure="Pankaj's working for 203 times 54: two lines, 80 + 12 = 92 and 100 + 15 = 115, then a "
                              "line and the total 135.",
                     s_figure="A box with columns 200 and 3 and rows 50 and 4: the cells 10,000, 150, 800 and 12, the "
                              "row sums 10,150 and 812, and the total 10,962."),
                 FIO("ck.c", "Check, Check!: (c) Lado's solution",
                     "Lado's solution for 38 × 150: 1,500 + 400 = 1,900 and 3,000 + 800 = 3,800, so the answer is "
                     "5,700. Is it correct? If correct, explain why. If it is incorrect, identify the error and "
                     "correct the solution.",
                     ["Estimate first: 38 is close to 40, so 38 × 150 is about 40 × 150 = 6,000.",
                      "Split 150 into 100 + 50. The 0 ones of 150 add nothing.",
                      "Check line 1, for the 50: 50 × 30 = 1,500 and 50 × 8 = 400, so 1,500 + 400 = 1,900. Right.",
                      "Check line 2, for the 100: 100 × 30 = 3,000 and 100 × 8 = 800, so 3,000 + 800 = 3,800. Right.",
                      "Add the lines again: 1,900 + 3,800 = 5,700. The total shown is right.",
                      "Check: 5,700 is a little less than the estimate 6,000, which fits because 38 is less than 40. "
                      "Also 38 × 150 = 38 × 100 + 38 × 50 = 3,800 + 1,900 = 5,700."],
                     "Correct. Each line multiplies 30 and 8 by one part of 150, the 50 and the 100, with the right "
                     "zeros, and 1,900 + 3,800 = 5,700.",
                     kind="prompt",
                     q_figure="Lado's working for 38 times 150: two lines, 1,500 + 400 = 1,900 and 3,000 + 800 = "
                              "3,800, then a line and the total 5,700."),
                 FIO("ck.d", "Check, Check!: (d) Kira's solution",
                     "Kira's solution for 193 × 272: 200 + 180 + 6 = 386; 700 + 630 + 21 = 1,351; 20,000 + 18,000 + "
                     "600 = 38,600; so the answer is 40,337. Is it correct? If correct, explain why. If it is "
                     "incorrect, identify the error and correct the solution.",
                     ["Estimate first: 193 is close to 200 and 272 is close to 270, so 193 × 272 is about 200 × 270 = "
                      "54,000.",
                      "Kira's answer 40,337 is well below 54,000, so there is a slip.",
                      "Split 272 into 200 + 70 + 2. The lines must be for 2 × 193, 70 × 193 and 200 × 193.",
                      "Line 1: 2 × 193 is 200 + 180 + 6 = 386. Right.",
                      "Line 2: the 7 is 7 tens, so every part needs one more zero: 70 × 100 = 7,000, 70 × 90 = 6,300 "
                      "and 70 × 3 = 210. Kira wrote 700 + 630 + 21 = 1,351, which is only 7 × 193. The zero for the "
                      "tens is missing.",
                      "Right line 2: 7,000 + 6,300 + 210 = 13,510.",
                      "Line 3: 200 × 193 is 20,000 + 18,000 + 600 = 38,600. Right.",
                      "Her addition of her own lines is right: 386 + 1,351 + 38,600 = 40,337. So the missing zero is "
                      "the only error.",
                      "Add the right lines: 386 + 13,510 + 38,600 = 52,496.",
                      "Check: 52,496 is close to the estimate 54,000, and 193 × 272 = 200 × 272 − 7 × 272 = 54,400 "
                      "− 1,904 = 52,496."],
                     "Not correct. The second line is missing a zero: 700 + 630 + 21 should be 7,000 + 6,300 + 210 = "
                     "13,510. Right product: 386 + 13,510 + 38,600 = 52,496.",
                     kind="prompt",
                     q_figure="Kira's working for 193 times 272: three lines, 200 + 180 + 6 = 386, 700 + 630 + 21 = "
                              "1,351 and 20,000 + 18,000 + 600 = 38,600, then a line and the total 40,337.",
                     s_figure="Kira's three lines redrawn with the right amounts 386, 13,510 and 38,600, the zero "
                              "that was missing in the second line shown in green, and the total 52,496."),
                 FIO("ck.e", "Check, Check!: (e) Asher's solution",
                     "Asher's solution for 626 × 323 on the place value table (columns TTh, Th, H, T, O): the three "
                     "rows are 1,878, 1,252 and 1,878 and the answer is 5,018. Is it correct? If correct, explain "
                     "why. If it is incorrect, identify the error and correct the solution.",
                     ["Estimate first: 626 is close to 600 and 323 is close to 300, so 626 × 323 is about 600 × 300 = "
                      "180,000.",
                      "Asher's answer 5,018 is far below 180,000, so the solution is wrong.",
                      "Split 323 into 3 + 20 + 300. The rows must be for 3 × 626, 20 × 626 and 300 × 626.",
                      "Row 1: 3 × 626 = 1,878. Right.",
                      "Row 2: 2 × 626 = 1,252, but this row is for 2 tens, so it needs a 0 at the end: 20 × 626 = "
                      "12,520. Asher wrote 1,252.",
                      "Row 3: 3 × 626 = 1,878, but this row is for 3 hundreds, so it needs 00 at the end: 300 × 626 = "
                      "187,800. Asher wrote 1,878.",
                      "The total is also wrong: his own rows add to 1,878 + 1,252 + 1,878 = 5,008, not 5,018.",
                      "Add the right rows: 1,878 + 12,520 + 187,800 = 202,198.",
                      "Check: 202,198 is above the estimate 180,000 because 626 and 323 were rounded down, and 626 × "
                      "323 = 626 × 300 + 626 × 23 = 187,800 + 14,398 = 202,198."],
                     "Not correct. The rows for the tens and hundreds have no zeros, and 1,878 + 1,252 + 1,878 = "
                     "5,008, not 5,018. Right product: 1,878 + 12,520 + 187,800 = 202,198.",
                     kind="prompt",
                     q_figure="Asher's working: 626 times 323 in a place value table with carry circles 1, 1 and 1 "
                              "above the top number, three rows 1,878, 1,252 and 1,878 each with a crossed carry, and "
                              "the total 5,018.",
                     s_figure="Asher's place value table redrawn with the right rows: 1,878, then 12,520 with a 0 "
                              "added in the ones, then 187,800 with 00 added, and the total 202,198.")],
          misconceptions=["M_MISSING_ZERO", "M_PLACE_SLIP"])],
    key_terms=["check", "estimate", "missing zero", "place value"]))

# ============================== T11 Same Product, Easy Ways ================================================
TOPICS.append(TOPIC(
    "T11", "M4", "Same Product, Easy Ways", ["Same product"], "Apply",
    "Students decide without calculating whether two problems have the same product, and find a new product from a "
    "given product by adding or taking away the right number.",
    "Some problems have the same product without any calculating: halve and double, split a number, or one group more "
    "or less. When one number grows by 1, add the other number to the product. When it drops by 1, take the other "
    "number away.",
    [A("T11.C1", "Same Product Without Calculating", "Apply",
       "Students decide without calculating whether two multiplication problems have the same product by naming the "
       "change made: halving and doubling, splitting one number, or one group more or less.",
       teach=["Predict first: 14 × 15 is some number. Without calculating, is 7 × 30 the same number? Is 13 × 16?",
              "Halve one number and double the other. 14 becomes 7 and 15 becomes 30. The product stays the same, so "
              "7 × 30 is the same as 14 × 15.",
              "Split one number and add the small products. 15 is 10 + 5, so 14 × 15 is the same as 14 × 10 + "
              "14 × 5.",
              "One group more or less changes the product by that group. 14 × 16 has one more group of 14 than "
              "14 × 15, so 14 × 15 is the same as 14 × 16 − 14.",
              "Be careful with 13 × 16. One number goes down by 1 and the other goes up by 1, but the groups that move "
              "are not the same size, so the product changes.",
              "Rule: to decide if two problems have the same product, name the change: halve and double, split one "
              "number, or one group more or less. If no such change fits, calculate to be sure."],
       examples=[WE("Is 14 × 15 the same as 7 × 30? As 14 × 10 + 14 × 5? As 14 × 16 − 14? As 13 × 16? Decide without "
                    "calculating, then check.",
                    ["Half of 14 is 7 and double 15 is 30. Halving one number and doubling the other keeps the "
                     "product, so 7 × 30 is the same as 14 × 15.",
                     "15 is 10 + 5. Splitting a number and adding both small products keeps the product, so "
                     "14 × 15 = 14 × 10 + 14 × 5.",
                     "14 × 16 has one more group of 14 than 14 × 15. Taking that group away gives back the same "
                     "product, so 14 × 15 = 14 × 16 − 14.",
                     "13 × 16: one group of 15 is taken away but only 13 is added, and 15 and 13 are not the same "
                     "amount. No change in the list fits, so we cannot say the product is the same. Calculating will show.",
                     "Check by calculating: 14 × 15 = 210, 7 × 30 = 210, and 13 × 16 = 208, which is 2 less."],
                    "Yes for 7 × 30, 14 × 10 + 14 × 5 and 14 × 16 − 14: each is 210. No for 13 × 16, which is 208")],
       key_terms=["same product", "halve and double", "split a number", "calculating"],
       misconceptions=["M_HALVE_BOTH", "M_SPLIT_ONE"], minutes=6),
     A("T11.C2", "Grow from a Known Product", "Apply",
       "Students find a new product from a given product by adding or taking away the right number: one more column "
       "adds the number of rows, and one row less takes away the length of a row.",
       teach=["Predict first: you have 7 × 14 = 98. Without multiplying, how much do you add to get 7 × 15? Is it 7 or "
              "14?",
              "Draw 7 rows of 14 squares. 7 × 15 has one more column. That column has 7 squares, one in each row. "
              "Add 7: 98 + 7 = 105.",
              "6 × 14 has one row less. That row has 14 squares. Take away 14: 98 − 14 = 84.",
              "Ten more rows add ten rows of 14. 17 × 14 = 98 + 10 × 14 = 98 + 140 = 238.",
              "The slip to avoid: adding the number that was already multiplied. To go from 7 × 14 to 7 × 15, add 7, "
              "not 14.",
              "Rule: when one number grows by 1, add the other number to the product. When one number drops by 1, "
              "take the other number away."],
       examples=[WE("7 × 14 = 98. Without multiplying, find 7 × 15, 6 × 14 and 17 × 14.",
                    ["Picture 7 rows of 14 squares: 7 × 14 = 98 squares.",
                     "7 × 15 has one more column. A column has 7 squares, one in each row, so add 7: "
                     "7 × 15 = 98 + 7 = 105.",
                     "6 × 14 has one row less. A row has 14 squares, so take away 14: 6 × 14 = 98 − 14 = 84.",
                     "17 × 14 has 10 more rows. Each row has 14 squares, so 10 rows add 10 × 14 = 140, and "
                     "17 × 14 = 98 + 140 = 238.",
                     "Check: the number you add or take away is the length of the line that is added or removed: 7 for "
                     "a column of 7, 14 for a row of 14, and 140 for ten rows."],
                    "7 × 15 = 105, 6 × 14 = 84 and 17 × 14 = 238")],
       key_terms=["known product", "one more column", "one row less", "grow"],
       misconceptions=["M_WRONG_STRIP"], minutes=6),
     DOER("T11.C3", "Practice: Same Product, Easy Ways", None, "Apply",
          "Students identify problems with the same product without calculating, find easy ways to multiply, and use a "
          "given product to find the next products.",
          ["Name the change: halve and double, split one number, or one group more or less.",
           "Look at the numbers first: a 25, a 50, a number just below a ten or a hundred, all have an easy way.",
           "When one number grows by 1, add the other number. When it drops by 1, take the other number away."],
          items=[FIO("ld2.q1", "Let Us Do, Q1 same answer",
                     "Identify the problems that have the same answer as the one given at the top of each box. Do not "
                     "calculate. (a): 12 × 17: 11 × 18, 6 × 34. (b): 26 × 11: 26 × 10 and 26 × 1, 20 × 11 and "
                     "6 × 11. (c): 18 × 4: 9 × 8, 20 × 4 − 8. (d): 55 × 9: 50 × 9 and 5 × 9, 54 × 10, "
                     "55 × 10 − 55. (e): 101 × 42: 100 × 42 and 100, 100 × 42 and 42. (f): 247 × 8: "
                     "250 × 8 − 24, 247 × 10 − 247. (g): 1,001 × 5: 1,000 × 6, 1,000 × 5 and 5. (h): 1,999 × 2: "
                     "2,000 × 2 − 4, 2,000 × 2 − 2.",
                     ["Reading used: the boxes are lettered (a) to (h) from left to right and from top to bottom, "
                      "and the word 'and' between two products means plus.",
                      "(a): half of 12 is 6 and double 17 is 34, so 12 × 17 = 6 × 34. 11 × 18 is not the same: 12 to "
                      "11 takes away one group of 17, but 17 to 18 adds only 11.",
                      "(b): 11 is 10 + 1, so 26 × 11 = 26 × 10 + 26 × 1. 26 is 20 + 6, so 26 × 11 = 20 × 11 + "
                      "6 × 11. Both are the same.",
                      "(c): half of 18 is 9 and double 4 is 8, so 18 × 4 = 9 × 8. 20 × 4 has two more groups of 4 "
                      "than 18 × 4, and 2 × 4 = 8, so 18 × 4 = 20 × 4 − 8. Both are the same.",
                      "(d): 55 is 50 + 5, so 55 × 9 = 50 × 9 + 5 × 9. 55 × 10 has one more 55 than 55 × 9, so "
                      "55 × 9 = 55 × 10 − 55. 54 × 10 is not the same: 55 to 54 takes away a group of 9, but 9 to 10 "
                      "adds a group of 54.",
                      "(e): 101 is 100 + 1, so 101 × 42 = 100 × 42 + 42. Adding 100 instead of 42 is not the same.",
                      "(f): 247 is 3 less than 250, and 3 × 8 = 24, so 247 × 8 = 250 × 8 − 24. 247 × 10 − 247 is "
                      "247 × 9, not 247 × 8, so it is not the same.",
                      "(g): 1,001 is 1,000 + 1, so 1,001 × 5 = 1,000 × 5 + 5. 1,000 × 6 changes the 5 into 6, which "
                      "adds 1,000, not 5, so it is not the same.",
                      "(h): 1,999 is 1 less than 2,000, so 1,999 × 2 = 2,000 × 2 − 1 × 2 = 2,000 × 2 − 2. Taking "
                      "away 4 is not the same.",
                      "Check by calculating only now: the top problems give 204, 286, 72, 495, 4,242, 1,976, 5,005 "
                      "and 3,998. Every problem we chose gives the same number. The others do not: 11 × 18 = 198, "
                      "54 × 10 = 540, 247 × 10 − 247 = 2,223, 1,000 × 6 = 6,000 and 2,000 × 2 − 4 = 3,996."],
                     "(a): the second; (b): both; (c): both; (d): the first and the third; (e): the second; "
                     "(f): the first; (g): the second; (h): the second. Count the problems in a box from left to "
                     "right.",
                     kind="exercise",
                     q_figure="Eight boxes in four rows of two. Each box has one problem on top and two or three "
                              "problems in cells below it. Row 1: 12 × 17 with 11 × 18 and 6 × 34; 26 × 11 with "
                              "26 × 10 and 26 × 1, and 20 × 11 and 6 × 11. Row 2: 18 × 4 with 9 × 8 and 20 × 4 − 8; "
                              "55 × 9 with 50 × 9 and 5 × 9, 54 × 10, and 55 × 10 − 55. Row 3: 101 × 42 with "
                              "100 × 42 and 100, and 100 × 42 and 42; 247 × 8 with 250 × 8 − 24 and 247 × 10 − 247. "
                              "Row 4: 1,001 × 5 with 1,000 × 6, and 1,000 × 5 and 5; 1,999 × 2 with 2,000 × 2 − 4 "
                              "and 2,000 × 2 − 2.",
                     s_figure="The same eight boxes with the problems that have the same answer shaded green and the "
                              "others left white."),
                 FIO("ld2.q2", "Let Us Do, Q2 easy ways",
                     "Find easy ways of solving these problems. (a): 16 × 25 (b): 12 × 125 (c): 24 × 250 "
                     "(d): 36 × 25 (e): 28 × 75 (f): 300 × 15 (g): 50 × 78 (h): 199 × 63 (i): 128 × 35",
                     ["(a): 16 = 4 × 4 and 4 × 25 = 100, so 16 × 25 = 4 × 100 = 400.",
                      "(b): split 125 into 100 + 25: 12 × 125 = 12 × 100 + 12 × 25 = 1,200 + 300 = 1,500.",
                      "(c): 24 = 4 × 6 and 4 × 250 = 1,000, so 24 × 250 = 6 × 1,000 = 6,000.",
                      "(d): 36 = 4 × 9 and 4 × 25 = 100, so 36 × 25 = 9 × 100 = 900.",
                      "(e): 28 = 4 × 7 and 4 × 75 = 300, so 28 × 75 = 7 × 300 = 2,100.",
                      "(f): 300 × 15 = 3 × 15 × 100 = 45 × 100 = 4,500.",
                      "(g): halve 78 and double 50: 50 × 78 = 100 × 39 = 3,900.",
                      "(h): 199 is 1 less than 200: 199 × 63 = 200 × 63 − 63 = 12,600 − 63 = 12,537.",
                      "(i): halve 128 and double 35: 128 × 35 = 64 × 70 = 4,480.",
                      "Check: each product is near an estimate, for example 128 × 35 is near 130 × 35 = 4,550, and "
                      "4,480 is near it."],
                     "(a): 400; (b): 1,500; (c): 6,000; (d): 900; (e): 2,100; (f): 4,500; (g): 3,900; (h): 12,537; "
                     "(i): 4,480",
                     kind="exercise"),
                 FIO("ld2.q3", "Let Us Do, Q3 your own examples",
                     "Write 5 other examples for which you can find easy ways of getting products.",
                     ["This question is open, so there is no single answer. Pick numbers with an easy way: a 25, a 50, "
                      "a number just below a hundred, or a number that splits into 100 and a little more.",
                      "Example 1: 25 × 44 = 100 × 11 = 1,100 (halve 44 twice, double 25 twice).",
                      "Example 2: 99 × 24 = 100 × 24 − 24 = 2,400 − 24 = 2,376.",
                      "Example 3: 15 × 18 = 30 × 9 = 270 (halve 18, double 15).",
                      "Example 4: 102 × 15 = 100 × 15 + 2 × 15 = 1,500 + 30 = 1,530.",
                      "Example 5: 75 × 12 = 3 × 300 = 900, because 12 = 3 × 4 and 75 × 4 = 300.",
                      "Check: each example has an easy way, and each product is true: 1,100, 2,376, 270, 1,530 and "
                      "900."],
                     "Sample answer: 25 × 44 = 1,100; 99 × 24 = 2,376; 15 × 18 = 270; 102 × 15 = 1,530; "
                     "75 × 12 = 900. Your answer may differ.",
                     kind="prompt"),
                 FIO("ld2.q4", "Let Us Do, Q4 use the given information",
                     "Find the answers to the following questions based on the given information. (a): 17 × 23 = 391 "
                     "(b): 17 × 24 = ___ (c): 17 × 22 = ___ (d): 16 × 23 = ___ (e): 8 × 9 = 72 (f): 18 × 9 = ___ "
                     "(g): 28 × 9 = ___ (h): 108 × 9 = ___ (i): 18 × 23 = ___. To find 17 × 24, how much is to be "
                     "added to 17 × 23, 17 or 23? To find 18 × 23, how much is to be added to 17 × 23, 17 or 23?",
                     ["(b): 17 × 24 has one more column than 17 × 23. The column has 17 squares, so add 17: "
                      "391 + 17 = 408.",
                      "(c): 17 × 22 has one column less. Take away 17: 391 − 17 = 374.",
                      "(d): 16 × 23 has one row less. A row has 23 squares, so take away 23: 391 − 23 = 368.",
                      "(f): 18 is 10 more than 8, so 18 × 9 has 10 more nines: 72 + 10 × 9 = 72 + 90 = 162.",
                      "(g): 28 is 20 more than 8: 72 + 20 × 9 = 72 + 180 = 252.",
                      "(h): 108 is 100 more than 8: 72 + 100 × 9 = 72 + 900 = 972.",
                      "(i): 18 × 23 has one more row than 17 × 23. The row has 23 squares, so add 23: "
                      "391 + 23 = 414.",
                      "To find 17 × 24 add 17, because the new column has 17 squares. To find 18 × 23 add 23, because "
                      "the new row has 23 squares.",
                      "Check: 17 × 24 = 17 × 20 + 17 × 4 = 340 + 68 = 408, and 18 × 9 = 162 and 108 × 9 = 972."],
                     "(b): 408; (c): 374; (d): 368; (f): 162; (g): 252; (h): 972; (i): 414. To find 17 × 24 add 17, "
                     "and to find 18 × 23 add 23.",
                     kind="exercise",
                     q_figure="Three arrays of squares drawn with place value blocks. The first has 17 rows by 23 "
                              "columns. The second has 17 rows by 24 columns, with the extra column of 17 squares "
                              "coloured blue. The third has 18 rows by 23 columns, with the extra row of 23 squares "
                              "coloured blue.",
                     s_figure="The 17 by 23 array with its blue column of 17 squares making 17 by 24, and with its "
                              "blue row of 23 squares making 18 by 23, and the amounts 17 and 23 written beside the "
                              "blue strips.")],
          misconceptions=["M_WRONG_STRIP", "M_SPLIT_ONE"])],
    key_terms=["same product", "known product", "calculating"]))

# ============================== T12 Estimates and Digit Puzzles ============================================
TOPICS.append(TOPIC(
    "T12", "M4", "Estimates and Digit Puzzles", ["Estimates", "Let Us Think"], "Apply",
    "Students estimate products by rounding to friendly numbers, and find the digits in multiplication puzzles by "
    "starting from the ones digit, using the size of the answer and testing every answer.",
    "An estimate is a number close to the product, found by rounding each number to a friendly number. In a digit "
    "puzzle, the same colour is the same digit: start from the ones digit, use the size of the answer, and test by "
    "multiplying.",
    [A("T12.C1", "Estimate a Product", "Apply",
       "Students estimate a product by rounding each number to a friendly number, multiply the friendly numbers, and "
       "decide whether an exact answer is close to the estimate.",
       teach=["Predict first: you do not need the exact answer, only a number that is close. For 52 × 48, which "
              "friendly numbers would you use?",
              "An estimate is a number that is close to the product. Round each number to a friendly number, a number "
              "that is easy to multiply, like 50, 100 or 25.",
              "52 is close to 50 and 48 is close to 50, so 52 × 48 is about 50 × 50 = 2,500.",
              "The exact product is 2,496. The estimate is close to it, but not equal. An estimate does not have to "
              "be exactly equal to the product.",
              "Use an estimate to check an answer. If your answer is far from the estimate, look for a missing zero or "
              "a wrong place value.",
              "To match products with numbers, estimate each product and pick the number that is closest.",
              "Rule: round each number to a friendly number, multiply, and say about. A good estimate is close to the "
              "exact product, and it does not have to be equal."],
       examples=[WE("Estimate 52 × 48 by rounding to friendly numbers. Then compare the estimate with the exact "
                    "product.",
                    ["52 is close to 50 and 48 is close to 50. These are friendly numbers.",
                     "Multiply the friendly numbers: 50 × 50 = 2,500. So 52 × 48 is about 2,500.",
                     "Now the exact product: 52 × 48 = 50 × 48 + 2 × 48 = 2,400 + 96 = 2,496.",
                     "The estimate 2,500 and the exact product 2,496 are close but not equal. An estimate only has to "
                     "be close.",
                     "Check: 52 × 48 should be near 2,500, and 2,496 is only 4 less."],
                    "About 2,500, from 50 × 50. The exact product is 2,496, so the estimate is close but not equal")],
       key_terms=["estimate", "friendly number", "round", "product"],
       misconceptions=["M_ESTIMATE_EXACT"], minutes=5),
     A("T12.C2", "Digit Puzzles: Start from the Ones Digit", "Apply",
       "Students find the digits in a multiplication puzzle by starting from the ones digit, using the size of the "
       "answer, and testing every answer by multiplying.",
       textbook=["Find the possible values of the coloured boxes in each of the following problems. The same colour "
                 "indicates the same number in a problem. Some problems can have more than one answer."],
       teach=["Predict first: two boxes times 6 give three boxes with the same digit. Is the digit at the end of the "
              "answer odd or even?",
              "In a digit puzzle the same colour is the same digit in that problem. A box with a black border can be "
              "any digit. Some puzzles have more than one answer, and some have none.",
              "Start from the ones digit. The ones digit of the answer comes only from the ones digits that are "
              "multiplied. Try each ones digit from 0 to 9 and keep the ones that fit.",
              "Then look at the size. Round the number and multiply to see how big the answer can be. This tells you "
              "which of the digits that fit are really possible.",
              "Test each number you find by multiplying. If every box matches, it is an answer. If no number passes "
              "the test, say that the puzzle has no answer.",
              "Rule: ones digit first, then the size, then test by multiplying, and list every answer."],
       examples=[WE("Two black boxes times 6 give an answer with three orange boxes. All three orange boxes hold the "
                    "same digit. Find the two-digit numbers.",
                    ["Reading used: the same colour is the same digit, so the three orange boxes hold one digit. The "
                     "boxes with a black border can be any digits.",
                     "The answer is one of 111, 222, 333, 444, 555, 666, 777, 888 or 999.",
                     "Start from the ones digit. 6 times any number is even, so the orange digit is even: 2, 4, 6 or "
                     "8.",
                     "Use the size. The biggest two-digit number is 99 and 6 × 99 = 594, so 666 and 888 are too big. "
                     "Only 222 and 444 are left.",
                     "For 222, the ones digit of the number gives a 2 at the end of 6 times it: 6 × 2 = 12 and "
                     "6 × 7 = 42, so it is 2 or 7.",
                     "For 222 the size is: 6 × 30 = 180 and 6 × 40 = 240, so the number is between 30 and 40. Test "
                     "32 and 37: 6 × 32 = 192 does not fit, 6 × 37 = 222 fits.",
                     "For 444, the ones digit is 4 or 9, because 6 × 4 = 24 and 6 × 9 = 54.",
                     "For 444 the size is: 6 × 70 = 420 and 6 × 80 = 480, so the number is between 70 and 80. Test "
                     "74 and 79: 6 × 74 = 444 fits, 6 × 79 = 474 does not fit.",
                     "Check by multiplying: 37 × 6 = 222 and 74 × 6 = 444."],
                    "37 × 6 = 222 and 74 × 6 = 444, so the orange digit is 2 or 4")],
       key_terms=["digit puzzle", "ones digit", "same colour", "start"], minutes=7),
     DOER("T12.C3", "Practice: Estimates and Digit Puzzles", None, "Apply",
          "Students find the possible digits in nine multiplication puzzles by starting from the ones digit and testing "
          "every answer, and estimate products and match them to the right numbers.",
          ["Digit puzzles: ones digit first, then the size of the answer, then test by multiplying.",
           "The same colour is the same digit, and a puzzle can have one answer, many answers or none.",
           "Estimate: round each number to a friendly number and multiply."],
          items=[FIO("lt2.abc", "Let Us Think: Q1 (a) to (c) digit boxes",
                     "Find the possible values of the coloured boxes in each of the following problems. The same "
                     "colour indicates the same number in a problem. Some problems can have more than one answer. "
                     "(a): a two-digit number × 3 gives a two-digit answer. (b): a three-digit number × 3 gives a "
                     "three-digit answer. (c): a four-digit number × 3 gives a four-digit answer.",
                     ["Reading used: all the orange answer boxes in a problem hold the same digit, and the boxes with "
                      "a black border can be any digits.",
                      "(a): the answer is 11, 22, 33, 44, 55, 66, 77, 88 or 99. Only 33, 66 and 99 are in the 3 times "
                      "table: 33 = 3 × 11, 66 = 3 × 22 and 99 = 3 × 33. So the orange digit is 3, 6 or 9.",
                      "(b): 3 × 37 = 111, so the top number must be 37 times a digit, and then the answer is 111 times "
                      "that digit, three equal digits. 37 × 3 = 111, 37 × 4 = 148, 37 × 5 = 185, 37 × 6 = 222, 37 × 7 = 259, 37 × 8 = 296 and 37 × 9 = 333.",
                      "(b): these are the top numbers. Times 3 they give 333, 444, 555, 666, 777, 888 and 999. The "
                      "digits 1 and 2 need top numbers 37 and 74, which have only two digits. So the orange digit is "
                      "3, 4, 5, 6, 7, 8 or 9.",
                      "(c): the answer is 1,111 times a digit. 3 × 1,111 = 3,333, 3 × 2,222 = 6,666 and "
                      "3 × 3,333 = 9,999 work. The other answers are not in the 3 times table: for example "
                      "3 × 370 = 1,110 and 3 × 371 = 1,113, so 1,111 is not. So the orange digit is 3, 6 or 9.",
                      "Check: 11 × 3 = 33, 148 × 3 = 444 and 1,111 × 3 = 3,333."],
                     "(a): the orange digit is 3, 6 or 9; (b): 3, 4, 5, 6, 7, 8 or 9; (c): 3, 6 or 9. For example "
                     "11 × 3 = 33.",
                     kind="prompt",
                     q_figure="Three frames. (a): two boxes with a black border, a times sign, a 3, and two orange "
                              "result boxes. (b): three boxes with a black border, a times sign, a 3, and three "
                              "orange result boxes. (c): four boxes with a black border, a times sign, a 3, and four "
                              "orange result boxes.",
                     s_figure="The three frames with the digits filled in for one answer each: 11 times 3 with the "
                              "answer 33, 148 times 3 with the answer 444, and 1,111 times 3 with the answer 3,333."),
                 FIO("lt2.def", "Let Us Think: Q1 (d) to (f) digit boxes",
                     "Find the possible values of the coloured boxes in each of the following problems. The same "
                     "colour indicates the same number in a problem. Some problems can have more than one answer. "
                     "(d): purple, blue × 5 gives 1, green, 0. (e): purple, purple, blue × 5 gives green, green, 0. "
                     "(f): purple, purple, purple, blue × 5 gives 1, green, green, green, 0.",
                     ["(d): the answer is 1, green, 0: a number from 100 to 190 that ends in 0. 5 times a number ends "
                      "in 0 only when the number is even. 5 × 20 = 100 and 5 × 38 = 190, so the top number is an even "
                      "number from 20 to 38.",
                      "(d): the ten top numbers are 20, 22, 24, 26, 28, 30, 32, 34, 36 and 38. Times 5 they give 100, "
                      "110, 120, 130, 140, 150, 160, 170, 180 and 190, so the green digit goes from 0 to 9. The sets "
                      "of purple, blue and green are (2, 0, 0), (2, 2, 1), (2, 4, 2), (2, 6, 3), (2, 8, 4), "
                      "(3, 0, 5), (3, 2, 6), (3, 4, 7), (3, 6, 8) and (3, 8, 9).",
                      "(e): 5 × 200 = 1,000, so the answer has three digits only if the top number is less than 200. "
                      "So purple is 1 and the top number is 11 and blue. The answer ends in 0, so blue is even.",
                      "(e): test 110, 112, 114, 116 and 118: 5 × 110 = 550, 5 × 112 = 560, 5 × 114 = 570, "
                      "5 × 116 = 580 and 5 × 118 = 590. Only 550 has its first two digits equal. So purple is 1, "
                      "blue is 0 and green is 5.",
                      "(f): the answer is between 10,000 and 19,999 and ends in 0. 5 × 2,000 = 10,000 and "
                      "5 × 4,000 = 20,000, so purple is 2 or 3. Blue is even.",
                      "(f): with purple 2: 5 × 2,220 = 11,100, 5 × 2,222 = 11,110, 5 × 2,224 = 11,120, "
                      "5 × 2,226 = 11,130 and 5 × 2,228 = 11,140. Only 11,110 has three equal digits after the 1, "
                      "so it is 2,222 with green 1.",
                      "(f): with purple 3: 5 × 3,330 = 16,650, 5 × 3,332 = 16,660, 5 × 3,334 = 16,670, "
                      "5 × 3,336 = 16,680 and 5 × 3,338 = 16,690. Only 16,660 fits, so it is 3,332 with green 6.",
                      "Check by multiplying: 24 × 5 = 120, 110 × 5 = 550, 2,222 × 5 = 11,110 and "
                      "3,332 × 5 = 16,660."],
                     "(d): an even number from 20 to 38, for example 24 × 5 = 120; (e): 110 × 5 = 550; (f): "
                     "2,222 × 5 = 11,110 and 3,332 × 5 = 16,660.",
                     kind="prompt",
                     q_figure="Three frames. (d): two boxes, the first purple and the second blue, times 5, with the "
                              "result 1, a green box, 0. (e): three boxes, purple, purple, blue, times 5, with the "
                              "result green, green, 0. (f): four boxes, purple, purple, purple, blue, times 5, with "
                              "the result 1, green, green, green, 0.",
                     s_figure="The frames with the digits filled in for one answer each: 24 times 5 with the answer "
                              "120, 110 times 5 with the answer 550, and 2,222 times 5 with the answer 11,110."),
                 FIO("lt2.ghi", "Let Us Think: Q1 (g) to (i) digit boxes",
                     "Find the possible values of the coloured boxes in each of the following problems. The same "
                     "colour indicates the same number in a problem. Some problems can have more than one answer. "
                     "(g): red, green, red × 9 = purple, brown, purple, brown. (h): red, green, purple × purple = "
                     "5,999. (i): red, green, purple × green = 2,000.",
                     ["(g): try green 0. The top number red, 0, red is 101 times red. Times 9 it becomes 101 times "
                      "the number 9 × red. 101 times a two-digit number writes that number twice: 101 × 18 = 1,818. "
                      "So when 9 × red has two digits, the answer is purple, brown, purple, brown. That needs red "
                      "from 2 to 9.",
                      "(g): the eight answers are 202 × 9 = 1,818, 303 × 9 = 2,727, 404 × 9 = 3,636, "
                      "505 × 9 = 4,545, 606 × 9 = 5,454, 707 × 9 = 6,363, 808 × 9 = 7,272 and 909 × 9 = 8,181. "
                      "Red 1 gives 101 × 9 = 909, which has only three digits.",
                      "(g): green must be 0. Any other middle digit breaks the repeat: 212 × 9 = 1,908 and "
                      "232 × 9 = 2,088 are not of the form purple, brown, purple, brown.",
                      "(h): the ones digit of purple × purple is 9, so purple is 3 or 7, because 3 × 3 = 9 and "
                      "7 × 7 = 49. With 3, the answer 5,999 must be in the 3 times table, but 3 × 1,999 = 5,997 and "
                      "3 × 2,000 = 6,000, so it is not.",
                      "(h): with 7: 7 × 800 = 5,600 and 7 × 900 = 6,300, so the number is between 800 and 900. "
                      "7 × 850 = 5,950, and 5,999 − 5,950 = 49 = 7 × 7, so the number is 857. Its last digit is 7, "
                      "the same as purple. So red is 8, green is 5 and purple is 7.",
                      "(i): the multiplier is the green digit and the top number has three digits. 1 × 2,000, "
                      "2 × 1,000, 4 × 500, 5 × 400 and 8 × 250 all make 2,000. For green 1 and 2 the top number has "
                      "four digits. For green 4, 5 and 8 the top numbers 500, 400 and 250 have a middle digit 0, 0 and "
                      "5, which is not the green digit.",
                      "(i): the digits 3, 6, 7 and 9 do not make 2,000 at all: for example 3 × 666 = 1,998 and "
                      "3 × 667 = 2,001. So no digits fit and puzzle (i) has no answer. This may be a printing slip in "
                      "the colours of the boxes.",
                      "Check by multiplying: 202 × 9 = 1,818, 909 × 9 = 8,181 and 857 × 7 = 5,999."],
                     "(g): green 0 and red 2 to 9, for example 202 × 9 = 1,818; (h): 857 × 7 = 5,999; (i): no digits "
                     "fit, so no answer.",
                     kind="prompt",
                     q_figure="Three frames. (g): three boxes, red, green, red, times 9, with four result boxes "
                              "purple, brown, purple, brown. (h): three boxes, red, green, purple, times one purple "
                              "box, with the result 5,999. (i): three boxes, red, green, purple, times one green "
                              "box, with the result 2,000.",
                     s_figure="The frames with the digits filled in: 202 times 9 with the answer 1,818 for (g), and "
                              "857 times 7 with the answer 5,999 for (h)."),
                 FIO("lt2.q2", "Let Us Think: Q2 estimate and match",
                     "Estimate the products on the left and match them to the numbers given on the right. 25 × 31, "
                     "132 × 19, 101 × 11, 248 × 49, 12 × 25. The numbers on the right are 2,600; 12,500; 300; 750; "
                     "1,000. Discuss how you estimated.",
                     ["25 × 31: 31 is close to 30, so the product is about 25 × 30 = 750. Match with 750.",
                      "132 × 19: 132 is close to 130 and 19 is close to 20, so about 130 × 20 = 2,600. Match with "
                      "2,600.",
                      "101 × 11: 101 is close to 100 and 11 is close to 10, so about 100 × 10 = 1,000. Match with "
                      "1,000.",
                      "248 × 49: 248 is close to 250 and 49 is close to 50, so about 250 × 50 = 12,500. Match with "
                      "12,500.",
                      "12 × 25: 12 = 3 × 4 and 4 × 25 = 100, so 12 × 25 = 3 × 100 = 300. Match with 300. This one is "
                      "exact.",
                      "Check: the exact products are 775, 2,508, 1,111, 12,152 and 300. Each one is close to its "
                      "match, and no other number on the right is closer."],
                     "25 × 31 with 750; 132 × 19 with 2,600; 101 × 11 with 1,000; 248 × 49 with 12,500; 12 × 25 with "
                     "300",
                     kind="prompt",
                     q_figure="A table with two columns. The left column has the five products 25 × 31, 132 × 19, "
                              "101 × 11, 248 × 49 and 12 × 25. The right column has the five numbers 2,600, 12,500, "
                              "300, 750 and 1,000.",
                     s_figure="The same table with a green line from each product to its estimate: 25 × 31 to 750, "
                              "132 × 19 to 2,600, 101 × 11 to 1,000, 248 × 49 to 12,500 and 12 × 25 to 300.")],
          misconceptions=["M_ESTIMATE_EXACT"])],
    key_terms=["estimate", "digit puzzle", "ones digit"]))

# ============================== T13 The King's Reward ======================================================
TOPICS.append(TOPIC(
    "T13", "M4", "The King's Reward", ["The King's Reward"], "Analyze",
    "Students follow a coin amount that is multiplied by the same number every day, write it day by day, and compare "
    "growing amounts to decide which start and which multiplier give the most.",
    "A king gives three ministers three choices of gold. Each choice starts with some coins and multiplies them by the "
    "same number every day. Write the amount day by day and compare. A small start with a big multiplier can end "
    "with the most coins.",
    [A("T13.C1", "The King's Reward: Growing Day by Day", "Analyze",
       "Students follow a growing amount day by day, multiplying by the same number once each day, and compare two "
       "growing amounts to say which one ends with more.",
       textbook=["One day, a king decided to reward three of his most talented ministers. The king called them to his "
                 "court and said, \"You all have served my empire with great dedication. As a reward, I give you "
                 "three choices of gold.\"",
                 "Choose wisely!",
                 "Choice 1: Take 5 gold coins and double the number of coins every day for 7 days.",
                 "Choice 2: Take 3 gold coins and triple the number of coins every day for 7 days.",
                 "Choice 3: Take 1 gold coin and multiply the number of coins by 5 every day for 7 days.",
                 "Minister 1: I will take 5 gold coins and double the number of coins every day for 7 days.",
                 "Minister 2: I will take 3 gold coins and triple the number of coins every day for 7 days.",
                 "Minister 3: I will take 1 gold coin and multiply the number of coins by 5 every day for 7 days.",
                 "The King gave 5 coins to Minister 1, 3 coins to Minister 2 and 1 coin to Minister 3."],
       teach=["Predict first: one chest of gold starts with 3 coins and doubles the coins every day. Another chest "
              "starts with 1 coin and triples them every day. After 4 days, which chest has more: the one that starts "
              "with more, or the one that grows faster?",
              "In your maths book a king gives three ministers three choices of gold. Each choice starts with a few "
              "coins and multiplies them every day for 7 days. One doubles, one triples and one multiplies by 5.",
              "The three ministers take the choices in order, and the king gives them their start coins: 5 coins, "
              "3 coins and 1 coin.",
              "To follow a growing amount, write the start coins on day 0. Then every day multiply by the same "
              "number, and write the new amount.",
              "Compare the lists day by day. A choice that starts with fewer coins can catch up and pass the other, "
              "because multiplying by a bigger number makes the amount grow faster.",
              "Count the multiplications carefully. The start coins are day 0, and each of the days adds one "
              "multiplication, so 7 days means 7 multiplications.",
              "Rule: write the start on day 0, multiply once each day by the same number, and compare day by day. A "
              "small start with a big multiplier can end with the most."],
       examples=[WE("The king offers two chests of gold coins. The first chest starts with 3 coins and doubles the coins "
                    "every day for 4 days. The second chest starts with 1 coin and triples the coins every day for 4 "
                    "days. Which chest has more coins after 4 days?",
                    ["Day 0: the first chest has 3 coins and the second chest has 1 coin. No multiplying has happened "
                     "yet.",
                     "The first chest doubles every day. Day 1: 3 × 2 = 6 coins. Day 2: 6 × 2 = 12 coins.",
                     "First chest, day 3: 12 × 2 = 24 coins. Day 4: 24 × 2 = 48 coins.",
                     "The second chest triples every day. Day 1: 1 × 3 = 3 coins. Day 2: 3 × 3 = 9 coins.",
                     "Second chest, day 3: 9 × 3 = 27 coins. Day 4: 27 × 3 = 81 coins.",
                     "Compare day by day. On day 2, the first chest has 12 coins and the second has 9 coins, so the "
                     "first chest is ahead. On day 3, the second chest has 27 coins and the first has 24 coins, so the "
                     "second chest has passed it.",
                     "After day 4, the second chest has 81 coins and the first chest has 48 coins. The second chest "
                     "started with fewer coins but ends with more, because multiplying by 3 grows faster than "
                     "multiplying by 2.",
                     "Check: 4 multiplications each time: 3 × 2 × 2 × 2 × 2 = 48 and 1 × 3 × 3 × 3 × 3 = 81."],
                    "The second chest has more: 81 coins against 48 coins, although it starts with fewer coins")],
       ncert=["kr.text"], key_terms=["king's reward", "growing", "every day", "multiplier"],
       misconceptions=["M_START_MOST"], minutes=7),
     DOER("T13.C2", "Pull it together and do it: The King's Reward", None, "Analyze",
          "Students follow a growing amount day by day, calculate the coins in the king's reward for each minister, and "
          "compare the three amounts to say which choice gives the most.",
          ["Write the start coins on day 0.",
           "Multiply once each day by the same number and write the new amount.",
           "Compare the three lists day by day and look at the last day."],
          items=[FIO("kr.choose", "The King's Reward: which choice",
                     "A king rewards three of his most talented ministers and gives three choices of gold. Choice 1: "
                     "Take 5 gold coins and double the number of coins every day for 7 days. Choice 2: Take 3 gold "
                     "coins and triple the number of coins every day for 7 days. Choice 3: Take 1 gold coin and "
                     "multiply the number of coins by 5 every day for 7 days. The King gave 5 coins to Minister 1, "
                     "3 coins to Minister 2 and 1 coin to Minister 3. Which of the rewards would you have chosen?",
                     ["This question asks for your opinion, so there is no single right answer. Give a choice and a "
                      "reason.",
                      "Look at the start: Choice 1 starts with 5 coins, Choice 2 with 3 coins and Choice 3 with 1 "
                      "coin. Choice 1 starts with the most.",
                      "Look at the multiplier: Choice 1 doubles, Choice 2 triples and Choice 3 multiplies by 5. "
                      "Choice 3 grows fastest every day.",
                      "Try only the first day: Choice 1 gives 5 × 2 = 10, Choice 2 gives 3 × 3 = 9 and Choice 3 gives "
                      "1 × 5 = 5. After one day Choice 1 is still ahead, so the start is not everything.",
                      "Sample answer: Choice 3, because it multiplies by the biggest number every day, even though it "
                      "starts with the fewest coins. A week is long enough for a fast multiplier to catch up.",
                      "Check: this is a guess with a reason. The next question calculates all three amounts, and that "
                      "shows whether the guess was right."],
                     "Sample answer: Choice 3, because it multiplies by the biggest number, 5, every day, so it may "
                     "catch up in a week. Your answer may differ. The next question checks it.",
                     kind="prompt"),
                 FIO("kr.calc", "The King's Reward: how many coins",
                     "After a week, the 3 ministers were surprised at the final amount of gold coins. Guess who "
                     "received the most gold coins? Calculate how much gold coins each minister received. Minister 1 "
                     "took 5 coins and doubled them every day for 7 days. Minister 2 took 3 coins and tripled them "
                     "every day for 7 days. Minister 3 took 1 coin and multiplied the coins by 5 every day for 7 days.",
                     ["Day 0: Minister 1 has 5 coins, Minister 2 has 3 coins and Minister 3 has 1 coin.",
                      "Minister 1 doubles 7 times: 5 × 2 = 10, 10 × 2 = 20, 20 × 2 = 40, 40 × 2 = 80, 80 × 2 = 160, "
                      "160 × 2 = 320, 320 × 2 = 640.",
                      "Minister 2 triples 7 times: 3 × 3 = 9, 9 × 3 = 27, 27 × 3 = 81, 81 × 3 = 243, 243 × 3 = 729, "
                      "729 × 3 = 2,187, 2,187 × 3 = 6,561.",
                      "Minister 3 multiplies by 5 seven times: 1 × 5 = 5, 5 × 5 = 25, 25 × 5 = 125, 125 × 5 = 625, "
                      "625 × 5 = 3,125, 3,125 × 5 = 15,625, 15,625 × 5 = 78,125.",
                      "Compare the three amounts after 7 days: 78,125 is more than 6,561, and 6,561 is more than 640.",
                      "Minister 3 started with the fewest coins, 1, but multiplied by the biggest number, 5, so "
                      "Minister 3 received the most.",
                      "Reading used: the start coins are day 0, and the coins are multiplied 7 times, once on each of "
                      "the 7 days. If the first day's coins counted as day 1 there would be 6 multiplications, giving "
                      "320, 2,187 and 15,625, and Minister 3 would still win.",
                      "Check: each amount is the start multiplied 7 times by the same number, for example "
                      "1 × 5 × 5 × 5 × 5 × 5 × 5 × 5 = 78,125."],
                     "Minister 1: 640 coins; Minister 2: 6,561 coins; Minister 3: 78,125 coins. Minister 3 received "
                     "the most.",
                     kind="prompt",
                     q_figure="Three rows for the three ministers. Each row has the start coins in the first box (5, 3 "
                              "and 1) and 7 empty boxes for the 7 days.",
                     s_figure="The same three rows filled in. Minister 1: 5, 10, 20, 40, 80, 160, 320, 640. Minister "
                              "2: 3, 9, 27, 81, 243, 729, 2,187, 6,561. Minister 3: 1, 5, 25, 125, 625, 3,125, "
                              "15,625, 78,125.")],
          misconceptions=["M_START_MOST"])],
    key_terms=["king's reward", "growing", "day by day"]))

# ============================== T14 Multiplication Patterns ================================================
TOPICS.append(TOPIC(
    "T14", "M4", "Multiplication Patterns", ["Multiplication Patterns"], "Analyze",
    "Students predict how a product changes when numbers are halved or doubled, use patterns for numbers ending in 5 "
    "and for 11 to find products, and compare number pairs by looking at the numbers.",
    "When a number in a product is halved or doubled, the product changes in a way you can predict. Products also "
    "follow patterns: numbers ending in 5, times 11, and rows of the digit 1. A pattern is a shortcut that you can always check "
    "by splitting a number.",
    [A("T14.C1", "How a Product Changes When a Number Changes", "Analyze",
       "Students predict how a product changes when one or both numbers are halved or doubled, and state the new "
       "product as half, double, a quarter, four times or the same.",
       teach=["Predict first: 20 × 36 = 720. If you halve only the 20, what happens to the product? And if you halve "
              "both numbers?",
              "Halve one number and keep the other: the product is half as big. Double one number and keep the "
              "other: the product is double.",
              "Halve both numbers: the product is halved twice, so it is a quarter. Double both numbers: the product "
              "is doubled twice, so it is four times as big.",
              "Halve one number and double the other: the product is halved and then doubled, so it is the same.",
              "Why: a product counts equal groups. Half as many groups, or groups half as big, is half as many in "
              "all.",
              "Look at what changes before you multiply: each number that is halved halves the product, and each "
              "number that is doubled doubles it.",
              "Rule: halving a number halves the product and doubling a number doubles the product. Count how many "
              "times each change happens."],
       examples=[WE("20 × 36 = 720. Without multiplying, find 10 × 36, 40 × 36, 10 × 18 and 10 × 72, and say how each "
                    "product compares with 720.",
                    ["10 × 36: the 20 is halved to 10 and the 36 stays. Halving one number halves the product, so "
                     "the product is half of 720, which is 360.",
                     "40 × 36: the 20 is doubled to 40 and the 36 stays. Doubling one number doubles the product, so "
                     "it is 720 × 2 = 1,440.",
                     "10 × 18: both numbers are halved, 20 to 10 and 36 to 18. The product is halved twice, so it is "
                     "a quarter of 720, which is 180.",
                     "10 × 72: the 20 is halved to 10 and the 36 is doubled to 72. Halving and then doubling puts "
                     "the product back, so it is 720, the same.",
                     "Check by multiplying: 10 × 36 = 360, 40 × 36 = 1,440, 10 × 18 = 180 and 10 × 72 = 720, and "
                     "180 × 4 = 720."],
                    "10 × 36 = 360, half; 40 × 36 = 1,440, double; 10 × 18 = 180, a quarter; 10 × 72 = 720, the "
                    "same")],
       key_terms=["product changes", "half", "double", "quarter"],
       misconceptions=["M_HALVE_BOTH", "M_DOUBLE_BOTH"], minutes=6),
     A("T14.C2", "Patterns in Products", "Analyze",
       "Students use the patterns for a number ending in 5 times itself and for multiplying by 11 to find products "
       "quickly, and check each pattern by splitting a number.",
       textbook=["Remember number pairs from Grade 4? Any two adjacent numbers in a row or a column are number "
                 "pairs."],
       teach=["Predict first: 15 × 15 = 225 and 25 × 25 = 625. Can you guess 75 × 75 without multiplying?",
              "A number ending in 5 times itself ends in 25. The front part is the tens digit times the next number: "
              "1 × 2 = 2 gives 225, and 2 × 3 = 6 gives 625.",
              "So for 75 × 75, the front part is 7 × 8 = 56, and the product is 5,625.",
              "Times 11 with a two-digit number: write the first digit, then the sum of the two digits, then the last "
              "digit. For 11 × 12 the digits are 1, then 1 + 2 = 3, then 2, so the answer is 132.",
              "If the sum of the digits is 10 or more, carry 1 to the first digit. For 11 × 57 the digits are 5, "
              "then 5 + 7 = 12, then 7. The 12 carries 1 to the 5, so the answer is 6, 2, 7: 627.",
              "Check every pattern by splitting a number: 11 × 57 = 57 × 10 + 57 = 570 + 57 = 627.",
              "Number pairs are any two numbers that are neighbours in a row or in a column. The size of the numbers in "
              "a pair tells you a lot about its product.",
              "Rule: a pattern is a shortcut, and you can always check it by splitting a number and adding."],
       examples=[WE("Use patterns to find 65 × 65 and 11 × 36 without long multiplication.",
                    ["65 ends in 5, so 65 × 65 ends in 25.",
                     "The front part is the tens digit times the next number: 6 × 7 = 42.",
                     "Put the parts together: 65 × 65 = 4,225.",
                     "Check by splitting: 65 × 65 = 65 × 60 + 65 × 5 = 3,900 + 325 = 4,225.",
                     "For 11 × 36, write the first digit 3 and the last digit 6 at the two ends.",
                     "In the middle write the sum of the two digits: 3 + 6 = 9. So 11 × 36 = 396.",
                     "Check by splitting: 11 × 36 = 36 × 10 + 36 = 360 + 36 = 396."],
                    "65 × 65 = 4,225 and 11 × 36 = 396")],
       ncert=["mp.pairs_def"], key_terms=["pattern", "number pairs", "ends in 5", "multiply by 11"], minutes=6),
     DOER("T14.C3", "Practice: Multiplication Patterns", None, "Analyze",
          "Students predict new products from a given product by halving and doubling, complete the patterns for the digit 1, "
          "numbers ending in 5, 11 and 9, and find the smallest and largest products of number pairs.",
          ["Halving a number halves the product and doubling a number doubles it.",
           "A number ending in 5 times itself ends in 25, and times 11 uses the sum of the digits in the middle.",
           "Look at the size of the numbers before you multiply every pair."],
          items=[FIO("mp.q1a", "Multiplication Patterns: Q1 (a) 16 × 44",
                     "Notice how the multiplier, multiplicand, and products are changing in each of the following. "
                     "What is the relationship of the new product with the original product? Solve part (a) "
                     "completely, and then predict the answers for the rest. (a): 16 × 44 = 704. (1): 8 × 88 = 704. "
                     "(2): 8 × 22 = 176. (3): 16 × 22 = ___. (4): 32 × 44 = ___.",
                     ["Solve (a) completely: 16 × 44 = 16 × 40 + 16 × 4 = 640 + 64 = 704.",
                      "(1): 16 becomes 8 (half) and 44 becomes 88 (double). Halving one number and doubling the other "
                      "keeps the product the same: 8 × 88 = 704.",
                      "(2): 16 becomes 8 and 44 becomes 22. Both numbers are halved, so the product is a quarter: "
                      "176 × 4 = 704.",
                      "(3): 16 × 22: only the 44 is halved, so the product is half of 704, which is 352.",
                      "(4): 32 × 44: only the 16 is doubled, so the product is double: 704 × 2 = 1,408.",
                      "Check by multiplying: 16 × 22 = 16 × 20 + 16 × 2 = 320 + 32 = 352 and 32 × 44 = 32 × 40 + "
                      "32 × 4 = 1,280 + 128 = 1,408."],
                     "(3): 16 × 22 = 352, half of 704; (4): 32 × 44 = 1,408, double 704. Also (1) is the same and (2) "
                     "is a quarter.",
                     kind="exercise"),
                 FIO("mp.q1b", "Multiplication Patterns: Q1 (b) 12 × 32",
                     "(b): 12 × 32 = 384. (1): 6 × 16 = ___. (2): 24 × 16 = ___. (3): 24 × 64 = ___. (4): "
                     "12 × 16 = ___. What is the relationship of the new product with the original product?",
                     ["(1): 12 to 6 and 32 to 16. Both are halved, so the product is a quarter of 384, which is 96: "
                      "6 × 16 = 96.",
                      "(2): 12 to 24 (double) and 32 to 16 (half). Double and half keep the product the same: "
                      "24 × 16 = 384.",
                      "(3): 12 to 24 and 32 to 64. Both are doubled, so the product is four times as big: "
                      "384 × 4 = 1,536, so 24 × 64 = 1,536.",
                      "(4): 12 × 16: only the 32 is halved, so the product is half of 384, which is 192.",
                      "Check by multiplying: 6 × 16 = 96, 24 × 16 = 384, 24 × 64 = 1,536 and 12 × 16 = 192."],
                     "(1): 6 × 16 = 96, a quarter; (2): 24 × 16 = 384, the same; (3): 24 × 64 = 1,536, four times; "
                     "(4): 12 × 16 = 192, half.",
                     kind="exercise"),
                 FIO("mp.q2", "Multiplication Patterns: Q2 complete the patterns",
                     "Observe and complete the given patterns. (a): 1 × 1 = 1; 11 × 11 = 121; 111 × 111 = 12,321; "
                     "1,111 × 1,111 = ___. (b): 5 × 5 = 25; 15 × 15 = 225; 25 × 25 = 625; 35 × 35 = 1,225; "
                     "45 × 45 = ___; 55 × 55 = ___. (c): 11 × 12 = 132; 11 × 34 = 374; 11 × 56 = 616; "
                     "11 × 78 = 858; 11 × 54 = ___; 11 × 82 = ___. (d): 1 × 9 + 1 = 10; 12 × 9 + 2 = 110; "
                     "123 × 9 + 3 = 1,110; 1,234 × 9 + 4 = ___.",
                     ["(a): the answers 1, 121 and 12,321 climb up from 1 and then come back down. The highest digit is "
                      "how many times the digit 1 is written in the number. 1,111 has the digit 1 written four times, "
                      "so the digits go 1, 2, 3, 4, 3, 2, 1 and 1,111 × 1,111 = 1,234,321.",
                      "(b): every answer ends in 25. The front part is the tens digit times the next number: "
                      "1 × 2 = 2, 2 × 3 = 6 and 3 × 4 = 12 give 225, 625 and 1,225.",
                      "(b): for 45 × 45 the front part is 4 × 5 = 20, so 45 × 45 = 2,025.",
                      "(b): for 55 × 55 the front part is 5 × 6 = 30, so 55 × 55 = 3,025.",
                      "(c): write the first digit, then the sum of the digits, then the last digit. For 11 × 54: 5, "
                      "5 + 4 = 9 and 4, so 11 × 54 = 594.",
                      "(c): for 11 × 82: 8, 8 + 2 = 10 and 2. The 10 carries 1 to the 8, so the answer is 9, 0, 2: "
                      "11 × 82 = 902.",
                      "(d): the answers 10, 110 and 1,110 are the digit 1 written more and more times, then a 0. So "
                      "1,234 × 9 + 4 = 11,110.",
                      "Check by calculating: 11 × 54 = 540 + 54 = 594, 11 × 82 = 820 + 82 = 902, 45 × 45 = 1,800 + "
                      "225 = 2,025 and 1,234 × 9 = 11,106, and 11,106 + 4 = 11,110."],
                     "(a): 1,234,321; (b): 2,025 and 3,025; (c): 594 and 902; (d): 11,110",
                     kind="exercise",
                     q_figure="Four dotted boxes of patterns. The first has the rows of the digit 1. The second has the "
                              "rows 5 × 5 to 55 × 55, with the notes 5 × 5 = 25 and 2 × 1 = 2 beside 15 × 15, and "
                              "5 × 5 = 25 and 3 × 2 = 6 beside 25 × 25. The third has the 11 times rows, with the "
                              "small labels for hundreds, tens and ones over the result digits and the notes 1 × 1, 1 + 2, 1 × 2 beside "
                              "11 × 12 and 1 × 3, 3 + 4, 1 × 4 beside 11 × 34. The fourth has the rows with 9 and a plus sign.",
                     s_figure="The four boxes completed: 1,234,321 in the first, 2,025 and 3,025 in the second, 594 and "
                              "902 in the third, and 11,110 in the fourth."),
                 FIO("mp.pairs", "Multiplication Patterns: Q2 number pairs",
                     "Here are some numbers. Remember number pairs from Grade 4? Any two adjacent numbers in a row or "
                     "a column are number pairs. Can you identify the pair whose product is the smallest and another "
                     "pair whose product is the largest? Do you need to find every product or can you find this by "
                     "looking at the numbers?",
                     ["Only two numbers joined by a line are a pair: 6 pairs along the rows and 6 pairs down the "
                      "columns, 12 pairs in all.",
                      "For the largest product, look at the big numbers: 75, 66, 62, 35 and 32. The pairs of them "
                      "joined by a line are 75 and 35, 66 and 32, 62 and 35, and 62 and 32.",
                      "Estimate them: 75 × 35 is about 80 × 35 = 2,800, 66 × 32 is about 70 × 30 = 2,100, 62 × 35 is "
                      "about 60 × 35 = 2,100 and 62 × 32 is about 60 × 30 = 1,800. The biggest is 75 × 35.",
                      "A pair that has a small number is smaller still: the biggest of those is 13 × 75 = 975, which is "
                      "less than 62 × 32, about 1,800.",
                      "For the smallest product, look at the small numbers: 8, 11, 13 and 14. The pairs of them joined "
                      "by a line are 11 and 14, and 13 and 14. 11 × 14 is less than 13 × 14, because 11 is less than "
                      "13.",
                      "The small number 8 is joined only to 35 and 32, which are big. 8 × 32 is about 8 × 30 = 240, "
                      "much more than 11 × 14, which is about 10 × 14 = 140.",
                      "So the smallest product is 11 × 14 = 154 and the largest is 35 × 75 = 2,625. We did not need "
                      "every product: looking at the size of the numbers was enough.",
                      "Check by finding all 12 products: 154, 182, 256, 280, 682, 726, 806, 975, 1,984, 2,112, 2,170 "
                      "and 2,625. The smallest is 154 and the largest is 2,625."],
                     "Smallest: 11 × 14 = 154. Largest: 35 × 75 = 2,625. We do not need every product: look at the "
                     "numbers.",
                     kind="prompt",
                     q_figure="A grid of 3 rows and 3 columns of boxes joined by lines: 8, 35, 75 in the first row; 32, "
                              "62, 13 in the second row; 66, 11, 14 in the third row.",
                     s_figure="The same grid with the pair 11 and 14 circled in green and the pair 35 and 75 circled in "
                              "orange, and the 12 joining lines drawn.")],
          misconceptions=["M_HALVE_BOTH", "M_DOUBLE_BOTH"])],
    key_terms=["pattern", "product", "number pairs"]))

# ============================== T15 Let Us Solve: Putting It Together ======================================
TOPICS.append(TOPIC(
    "T15", "M4", "Let Us Solve: Putting It Together", ["Let Us Solve"], "Apply",
    "Students plan and solve word problems that need more than one step, estimate and check the answer against the "
    "question, and find a product from a neighbouring product without multiplying.",
    "A word problem is solved in steps: read it, decide what to multiply and what to add, estimate, solve and check. "
    "Do not multiply every pair of numbers you see. A product next to a known product needs only one more or one less "
    "group.",
    [A("T15.C1", "Plan, Solve and Check", "Apply",
       "Students read a word problem, decide which numbers to multiply and which to add or take away, estimate the "
       "answer, solve it with a chapter method and check the answer against the estimate.",
       teach=["Predict first: a word problem has three numbers, 24, 35 and 120. Do you multiply all three? Which two "
              "do you multiply and which do you add?",
              "Read the problem slowly and say in your own words what is asked.",
              "Ask: are there equal groups? Then multiply. Is there one extra amount paid or received once? Then add "
              "it or take it away.",
              "Do not multiply every pair of numbers you see. A charge that is paid once is added after the "
              "multiplying, not multiplied.",
              "Estimate first with friendly numbers: 24 × 35 is about 20 × 40 = 800.",
              "Solve with a method that fits the numbers: split a number, halve and double, nearest multiple, a box "
              "or lines.",
              "Check the answer against the estimate, and read the question again to see that the answer fits it, "
              "with its unit.",
              "Rule: read, decide what to multiply and what to add, estimate, solve, then check against the estimate "
              "and the question."],
       examples=[WE("The dairy cooperative buys 24 packets of butter at ₹35 each and pays ₹120 once to carry them to "
                    "the shop. How much does it pay in all?",
                    ["Read and say what is asked: the total money paid for the packets and the carrying.",
                     "Decide: 24 packets at ₹35 each are 24 equal groups, so multiply 24 × 35. The carrying charge is "
                     "paid once, so add ₹120 after.",
                     "Estimate: 24 is close to 20 and 35 is close to 40, so the packets cost about 20 × 40 = 800 "
                     "rupees.",
                     "Multiply: 24 × 35 = 24 × 30 + 24 × 5 = 720 + 120 = 840.",
                     "Add the carrying charge: 840 + 120 = 960.",
                     "Check: 840 is close to the estimate 800, and 960 − 120 = 840 takes the carrying charge back "
                     "off. The answer is in rupees."],
                    "₹960 in all")],
       key_terms=["plan", "solve", "check", "estimate", "multiply and add"],
       misconceptions=["M_MULT_ALL"], minutes=6),
     DOER("T15.C2", "Pull it together and do it: Let Us Solve", None, "Apply",
          "Students solve six problems: word problems with more than one step, products of two-digit and three-digit "
          "numbers, and two products found from a given product without multiplying.",
          ["Read, decide what to multiply and what to add, estimate, solve and check.",
           "Choose a method that fits the numbers: split, halve and double, nearest multiple, box or lines.",
           "A product next to a given product needs one more or one less group."],
          items=[FIO("ls3.q1", "Let Us Solve: Q1 Mala's books",
                     "Mala went to a book exhibition and bought 18 books. The shop was selling 3 books for ₹150. After "
                     "buying the books, she still had ₹20 left. How much money did Mala have at the beginning?",
                     ["18 books in groups of 3 books: 3 × 6 = 18, so there are 6 groups.",
                      "Each group of 3 books costs ₹150, so the 6 groups cost 6 × 150 = 900, that is ₹900.",
                      "She spent ₹900 and still had ₹20 left, so at the beginning she had 900 + 20 = 920 rupees.",
                      "Check: 1 book costs 150 ÷ 3 = 50, so 18 books cost 18 × 50 = 900, and 920 − 900 = 20, the "
                      "money left."],
                     "₹920 at the beginning",
                     kind="exercise"),
                 FIO("ls3.q2", "Let Us Solve: Q2 football tournament",
                     "A village sports club organises a women's football tournament. The club earned money by selling "
                     "match tickets and charging fees for team participation. They sold 57 tickets for ₹115 each. They "
                     "had 3 teams joining the tournament, with each team paying a participation fee of ₹1,599. The "
                     "teams paid ₹1,750 in total to rent the football ground and ₹1,129 for food and water. (a): How "
                     "much money did the club collect in total from ticket sales and team participation fees? (b): "
                     "What were the total expenses on renting the ground and food and water?",
                     ["Tickets: 57 tickets at ₹115 each, so multiply 57 × 115. Split 115 into 100 + 15.",
                      "57 × 100 = 5,700.",
                      "57 × 15 = 57 × 10 + 57 × 5 = 570 + 285 = 855.",
                      "57 × 115 = 5,700 + 855 = 6,555, so the tickets bring ₹6,555.",
                      "Fees: 3 teams pay ₹1,599 each. 3 × 1,599 = 3 × 1,600 − 3 = 4,800 − 3 = 4,797, so the fees are "
                      "₹4,797.",
                      "(a): the club collected 6,555 + 4,797 = 11,352 rupees in all.",
                      "(b): the expenses are the ground rent ₹1,750 and the food and water ₹1,129: 1,750 + 1,129 = "
                      "2,879. The question asks only for the two totals, so we do not subtract them.",
                      "Check: 57 × 115 is a little less than 60 × 115 = 6,900, and 6,555 is a little less. 3 × 1,599 "
                      "is just below 3 × 1,600 = 4,800, and 4,797 is just below."],
                     "(a): ₹11,352; (b): ₹2,879",
                     kind="exercise"),
                 FIO("ls3.q3", "Let Us Solve: Q3 Republic Day",
                     "Ananya is watching Republic Day celebrations on the city's public ground. There are 12 rows of "
                     "students sitting in front of her and 17 rows behind her. There are 18 students to her right and "
                     "22 students to her left. (a): How many rows of students are there in total? (b): How many "
                     "students are there in Ananya's row? (c): What is the total number of students on the ground?",
                     ["(a): the rows in front, her own row and the rows behind: 12 + 1 + 17 = 30 rows.",
                      "(b): the students on her right, the students on her left and Ananya herself: 18 + 22 + 1 = 41 "
                      "students.",
                      "(c): the book does not say that every row has the same number of students. We take every row "
                      "to have as many students as Ananya's row, 41.",
                      "30 rows of 41 students: 30 × 41 = 30 × 40 + 30 = 1,200 + 30 = 1,230.",
                      "Check: 41 × 30 = 41 × 3 × 10 = 123 × 10 = 1,230."],
                     "(a): 30 rows; (b): 41 students; (c): 1,230 students, if every row has 41 students",
                     kind="exercise"),
                 FIO("ls3.q4", "Let Us Solve: Q4 multiply",
                     "Multiply. (a): 67 × 78 (b): 34 × 56 (c): 45 × 263 (d): 86 × 542 (e): 432 × 107 (f): 310 × 120",
                     ["(a): 78 = 8 + 70. 8 × 67 = 536 and 70 × 67 = 4,690, so 67 × 78 = 536 + 4,690 = 5,226.",
                      "(b): 56 = 6 + 50. 6 × 34 = 204 and 50 × 34 = 1,700, so 34 × 56 = 204 + 1,700 = 1,904.",
                      "(c): 263 = 3 + 60 + 200. 3 × 45 = 135, 60 × 45 = 2,700 and 200 × 45 = 9,000, so "
                      "45 × 263 = 135 + 2,700 + 9,000 = 11,835.",
                      "(d): 542 = 2 + 40 + 500. 2 × 86 = 172, 40 × 86 = 3,440 and 500 × 86 = 43,000, so "
                      "86 × 542 = 172 + 3,440 + 43,000 = 46,612.",
                      "(e): 107 = 7 + 100, with 0 tens. 7 × 432 = 3,024 and 100 × 432 = 43,200, so "
                      "432 × 107 = 3,024 + 43,200 = 46,224.",
                      "(f): 120 = 20 + 100. 20 × 310 = 6,200 and 100 × 310 = 31,000, so 310 × 120 = 6,200 + 31,000 = "
                      "37,200.",
                      "Check by estimating: 70 × 80 = 5,600, 30 × 60 = 1,800, 45 × 260 = 11,700, 90 × 540 = 48,600, "
                      "430 × 110 = 47,300 and 300 × 120 = 36,000. Each is close to its answer."],
                     "(a): 5,226; (b): 1,904; (c): 11,835; (d): 46,612; (e): 46,224; (f): 37,200",
                     kind="exercise"),
                 FIO("ls3.q5", "Let Us Solve: Q5 from 67 × 67",
                     "If 67 × 67 = 4,489, without multiplication find 67 × 68.",
                     ["Picture 67 rows of 67 squares: 67 × 67 = 4,489 squares.",
                      "67 × 68 has one more column. The column has 67 squares, one in each row.",
                      "Add the new column: 4,489 + 67 = 4,556.",
                      "We add 67, the number that did not change, not 68.",
                      "Check: 67 × 68 = 67 × 70 − 67 × 2 = 4,690 − 134 = 4,556."],
                     "67 × 68 = 4,556",
                     kind="exercise"),
                 FIO("ls3.q6", "Let Us Solve: Q6 from 99 × 100",
                     "If 99 × 100 = 9,900, without multiplication find 99 × 99.",
                     ["Picture 99 rows of 100 squares: 99 × 100 = 9,900 squares.",
                      "99 × 99 has one column less. The column has 99 squares, one in each row.",
                      "Take away the column: 9,900 − 99 = 9,801.",
                      "We take away 99, the number that did not change, not 100.",
                      "Check: 99 × 99 is just below 100 × 100 = 10,000, and 9,801 is just below."],
                     "99 × 99 = 9,801",
                     kind="exercise")],
          misconceptions=["M_MULT_ALL", "M_WRONG_STRIP"])],
    key_terms=["plan", "solve", "check", "word problems"]))

# ============================== T16 Chapter Revision (summary) =============================================
TOPICS.append(TOPIC(
    "T16", "M4", "Chapter Revision: The Dairy Farm", ["Chapter summary"], "Understand",
    "",
    "The chapter's ideas in one walk through the dairy: equal groups, the order of numbers, multiplying by 10s, 100s "
    "and 1,000s, splitting, halving and doubling, the nearest multiple, choosing the easy way, the box, Kanti's lines "
    "and John's lines, carries, checking, equal products, estimates, digit puzzles, the King's Reward, patterns and "
    "word problems.",
    [A("T16.C1", "Chapter Revision: The Dairy Farm", "Understand",
       "",
       teach=["Predict first: you have walked through the whole dairy, from the pouches to the word problems. Can you "
              "say one idea from each stop? Read the lines below and tick each idea you remembered.",
              "Equal groups: a total can be packed in many different equal groups, and number of groups × group size "
              "= total.",
              "Check: 24 pouches can be 4 groups of 6 or 3 groups of 8, because 4 × 6 = 24 and 3 × 8 = 24.",
              "Order: swapping the number of groups and the group size does not change the product, and any number "
              "times 0 is 0.",
              "Check: 9 × 4 = 36 and 4 × 9 = 36, and 0 × 6 = 0.",
              "Multiplying by 10, 100 and 1,000: every digit moves one, two or three places to the left. For tens and "
              "hundreds, multiply the digits and then write the zeros of both numbers.",
              "Check: 47 × 10 = 470, 47 × 100 = 4,700, and 30 × 70 = 2,100 because 3 × 7 = 21 and there are two "
              "zeros.",
              "Many ways to multiply: split a number into parts, multiply each part and add the small products.",
              "Check: 15 × 6 = 10 × 6 + 5 × 6 = 60 + 30 = 90.",
              "Halve one number and double the other and the product stays the same. It works well with 5 and 25, "
              "because 5 is half of 10 and 25 is a quarter of 100.",
              "Check: 14 × 5 = 7 × 10 = 70 and 25 × 24 = 100 × 6 = 600.",
              "Nearest multiple: round one number to a friendly ten, multiply, then take away or add the extra "
              "strip.",
              "Check: 9 × 29 = 9 × 30 − 9 = 270 − 9 = 261 and 8 × 41 = 8 × 40 + 8 = 320 + 8 = 328.",
              "Choose the easy way: look at the numbers first. A 5, 25 or 50 means halve and double. A number just "
              "below or above a ten means nearest multiple. Otherwise split.",
              "Check: 50 × 18 has a 50, so halve and double: 50 × 18 = 100 × 9 = 900.",
              "The box: split both numbers into tens and ones, multiply each pair of parts and add the four small "
              "products.",
              "Check: for 12 × 13 the four cells are 100, 30, 20 and 6, and 100 + 30 + 20 + 6 = 156.",
              "Kanti's four lines write the four small products one under the other. John joins them into two "
              "lines. Both give the same total.",
              "Check: John's two lines for 12 × 13 are 3 × 12 = 36 and 10 × 12 = 120, and 36 + 120 = 156.",
              "Place by place and carries: multiply each place and add. A carry is added after you multiply the next "
              "place, not before.",
              "Check: 3 × 28: 3 × 8 = 24, write 4 and carry 2. Then 3 × 2 = 6, and 6 + 2 = 8. So 3 × 28 = 84.",
              "Check a solution: estimate first, check each line for its zeros and its place value, then add the "
              "lines again.",
              "Check: for 42 × 31 a line 42 × 3 = 126 is missing a zero. It should be 42 × 30 = 1,260, and "
              "1,260 + 42 = 1,302.",
              "Same product and growing from a known product: halve and double, split a number, or one group more or "
              "less. One more group adds that group and one less takes it away.",
              "Check: 9 × 13 = 117, so 9 × 14 = 117 + 9 = 126 and 8 × 13 = 117 − 13 = 104.",
              "Estimate: round each number to a friendly number. An estimate is close to the product, and it does "
              "not have to be equal.",
              "Check: 49 × 31 is about 50 × 30 = 1,500, and the exact product is 1,519.",
              "Digit puzzles: start from the ones digit, then use the size of the answer, then test by multiplying. "
              "Some puzzles have more than one answer and some have none.",
              "Check: a number times 5 ends in 0 only when the number is even: 5 × 14 = 70 and 5 × 13 = 65.",
              "The King's Reward: write the start coins on day 0, multiply once each day by the same number and "
              "compare day by day. A small start with a big multiplier can win.",
              "Check: 2 coins doubled every day for 4 days make 4, 8, 16 and 32 coins, and 2 × 2 × 2 × 2 × 2 = 32.",
              "Patterns: halving one number halves the product, doubling one number doubles it, and halving both gives "
              "a quarter. A number ending in 5 times itself ends in 25, and times 11 puts the sum of the digits in the "
              "middle.",
              "Check: 16 × 30 = 480, so 8 × 30 = 240 and 8 × 15 = 120. Also 85 × 85 = 7,225 because 8 × 9 = 72, and "
              "11 × 45 = 495 because 4 + 5 = 9.",
              "Plan, solve and check: read the problem, decide what to multiply and what to add, estimate, solve and "
              "check against the estimate.",
              "Check: 18 packets at ₹25 each and ₹30 once for the delivery cost 18 × 25 = 450 and 450 + 30 = 480, so "
              "₹480 in all."],
       ncert=["summary"], key_terms=["revision", "dairy farm", "multiplication"], minutes=8,
       enrichment=True)],
    topic_type="summary"))
