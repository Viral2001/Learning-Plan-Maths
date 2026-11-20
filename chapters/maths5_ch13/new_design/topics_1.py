# -*- coding: utf-8 -*-
"""Topics T1, T1B and T2 (module M1: Factors, Multiples and Arrays). The framing intro (the hidden number box: the
hook and the free Hidden Number Box), the short idea topic T1B (Factors and Multiples with the book's opener questions),
and Arrays Show Factors. Every teaching concept has one worked example with the plan's own numbers; every book
question is an FIO item of its topic's DOER, in the book's order."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Find the Hidden Numbers (framing) ======================================
# The framing topic holds only the hook video and the free-try tool, and no book question. The concept video and the
# book's opener questions follow in the short idea topic T1B.
TOPICS.append(TOPIC(
    "T1", "M1", "Find the Hidden Numbers", ["Chapter opening"], "Understand",
    "",
    "Numbers go into a box and come out multiplied by a secret number. Four numbers have come out: 28, 36, 48 and 72. "
    "Try the box and find the secret number.",
    [A("T1.C1", "Find the Hidden Numbers", "Understand",
       "",
       textbook=["Find the hidden numbers.",
                 "Numbers put in this box get multiplied by a number and come out."],
       teach=["Predict first: a box takes a number, multiplies it by a secret number and lets the answer fly out. Four "
              "numbers have flown out: 28, 36, 48 and 72. Can you guess the secret number?",
              "Robby the rabbit and Deeku the deer watch the box. Numbers go in, and multiplied numbers come out.",
              "The four numbers that came out are 28, 36, 48 and 72. Which number did the box multiply by?",
              "Is there only one secret number, or could there be more than one? And which numbers went inside?",
              "Think about it, then try the hidden number box on the next screen."],
       ncert=["open.story"], key_terms=["multiplied", "box", "hidden numbers"],
       video_focus=["HOOK"], enrichment=True, minutes=4),
     DOER("T1.C3", "Hidden Number Box: Explore", "hidden_number_box", "Understand",
          "",
          ["Numbers go into the box and come out multiplied by a secret number.",
           "Four numbers have come out: 28, 36, 48 and 72.",
           "Try a multiplier, run the box backwards and find out which numbers could have gone in."],
          misconceptions=["M_ONE_MULTIPLIER"], role="try_it", enrichment=True)],
    topic_type="framing", key_terms=["multiplier", "box", "hidden numbers"]))

# ============================== T1B Factors and Multiples ================================================
TOPICS.append(TOPIC(
    "T1B", "M1", "Factors and Multiples", ["Chapter opening"], "Understand",
    "Students name the numbers a box multiplies by as factors and the numbers that come out as multiples, find the "
    "factors that fit a whole list of numbers, and answer the book's questions about the hidden numbers.",
    "A number you multiply by is a factor of the answer, and the answer is a multiple of that number. A factor that "
    "fits every number on a list is a common factor of the list.",
    [A("T1B.C1", "Factors and Multiples", "Understand",
       "Students find the numbers a box could multiply by to make a list of numbers, and name these multipliers as "
       "factors and the numbers that come out as multiples of them.",
       textbook=["The multipliers 1, 2, and 4 that you found above are the factors of the numbers that have come out "
                 "of the box, that is, 28, 36, 48, and 72. In fact, these are the common factors of all the numbers. "
                 "The numbers 28, 36, 48, and 72 are multiples of 1, 2 and 4.",
                 "The product of two or more factors gives a multiple."],
       teach=["Predict first: a box multiplies every number by 6. You put in 5, 7 and 9. What comes out, and how are "
              "6 and the numbers that come out related?",
              "5 × 6 = 30, 7 × 6 = 42 and 9 × 6 = 54. The numbers 30, 42 and 54 come out.",
              "The number the box multiplies by is a factor of every number that comes out. The numbers that come out "
              "are multiples of that factor: 30, 42 and 54 are multiples of 6.",
              "A factor that works for every number on a list is a common factor of those numbers.",
              "The product of two or more factors gives a multiple. 2 × 3 = 6, so 6 is a multiple of 2 and of 3.",
              "Rule: factors multiply to make a multiple, and a multiple is made by multiplying its factors."],
       examples=[WE("A box multiplies by a secret number. The numbers 30, 42, 54 and 90 come out. Find every number "
                    "the box might multiply by, and the numbers that went in for the biggest one.",
                    ["Try 1: 1 × 30 = 30, 1 × 42 = 42, 1 × 54 = 54 and 1 × 90 = 90. So 1 works.",
                     "Try 2: 15 × 2 = 30, 21 × 2 = 42, 27 × 2 = 54 and 45 × 2 = 90. So 2 works.",
                     "Try 3: 10 × 3 = 30, 14 × 3 = 42, 18 × 3 = 54 and 30 × 3 = 90. So 3 works.",
                     "Try 4: 7 × 4 = 28 and 8 × 4 = 32, so 30 is not a multiple of 4. So 4 does not work.",
                     "Try 5: 8 × 5 = 40 and 9 × 5 = 45, so 42 is not a multiple of 5. So 5 does not work.",
                     "Try 6: 5 × 6 = 30, 7 × 6 = 42, 9 × 6 = 54 and 15 × 6 = 90. So 6 works.",
                     "The numbers from 7 to 30 are checked the same way and none of them fits all four numbers. For "
                     "example 10 does not fit: 4 × 10 = 40 and 5 × 10 = 50, so 42 is not a multiple of 10.",
                     "The multipliers 1, 2, 3 and 6 are the common factors of 30, 42, 54 and 90, and the four numbers "
                     "are multiples of each of them.",
                     "Check: 2 × 3 × 5 = 30, a product of factors that gives a multiple."],
                    "The box might multiply by 1, 2, 3 or 6. For 6, the numbers 5, 7, 9 and 15 went in")],
       ncert=["open.factors", "open.product"], key_terms=["factor", "multiple", "multiplier", "common factors"],
       misconceptions=["M_FACTOR_MULTIPLE", "M_ONE_MULTIPLIER"], minutes=5),
     DOER("T1B.C2", "Practice: Hidden Numbers", None, "Understand",
          "Students find the multipliers that fit the numbers coming out of the box, and say which numbers could have "
          "gone in for each multiplier.",
          ["The box multiplies every number by the same secret number.",
           "Each secret number that fits is a factor of every number that comes out.",
           "Dividing a number that came out by the multiplier gives the number that went in."],
          items=[FIO("open.box", "Find the hidden numbers: guess the multiplier",
                     "Numbers put in this box get multiplied by a number and come out. Four numbers come out of the "
                     "box: 28, 36, 48 and 72. (a) Can you guess the multiplier if you see the 4 numbers coming out of "
                     "the box? (b) Is there more than one possible multiplier? (c) What numbers might have been put "
                     "inside the box? Share your thoughts in the class.",
                     ["The box multiplied each number that went in, so every number that comes out is a multiple of "
                      "the multiplier.",
                      "Try 4: 28 ÷ 4 = 7, 36 ÷ 4 = 9, 48 ÷ 4 = 12 and 72 ÷ 4 = 18. All four are whole numbers, so 4 "
                      "can be the multiplier.",
                      "Try 2: 28 ÷ 2 = 14, 36 ÷ 2 = 18, 48 ÷ 2 = 24 and 72 ÷ 2 = 36. So 2 can be the multiplier too.",
                      "Try 1: the numbers that went in are 28, 36, 48 and 72 themselves. So 1 works too.",
                      "Try 3: 9 × 3 = 27 and 10 × 3 = 30, so 28 is not a multiple of 3. So 3 does not work.",
                      "(a): the multiplier can be 4. (b): yes, 1, 2 and 4 all work. They are the common factors of "
                      "28, 36, 48 and 72. (c): Sample answer: with multiplier 4 the numbers 7, 9, 12 and 18 went in. "
                      "Your answer may differ.",
                      "Check: 7 × 4 = 28, 9 × 4 = 36, 12 × 4 = 48 and 18 × 4 = 72."],
                     "(a): 4 (2 and 1 work too). (b): Yes, 1, 2 and 4. (c): Sample answer: 7, 9, 12 and 18 went in "
                     "with 4. Your answer may differ.",
                     kind="prompt",
                     q_figure="A cardboard box with an arrow going in and an arrow coming out, and four number tags "
                              "coming out of it: 28, 36, 48 and 72.",
                     s_figure="The same box with the multiplier 4 written on it, the numbers 7, 9, 12 and 18 going in "
                              "and the numbers 28, 36, 48 and 72 coming out.")],
          misconceptions=["M_ONE_MULTIPLIER", "M_FACTOR_MULTIPLE"])],
    key_terms=["factor", "multiple", "common factors"]))

# ============================== T2 Arrays Show Factors ====================================================
TOPICS.append(TOPIC(
    "T2", "M1", "Arrays Show Factors", ["Arrays", "Let Us Do (arrays)"], "Apply",
    "Students make arrays to list the factors of a number, show that the number is a multiple of each of its factors, "
    "and tell which numbers have only the two factors 1 and themselves.",
    "Laying a number of tiles in equal rows makes an array. Each array is a multiplication, and the numbers in all the "
    "arrays are the factors. A number is a multiple of each of its factors, and a number with only one array is a "
    "prime number.",
    [A("T2.C1", "Arrays Show Factors", "Apply",
       "Students make every array of a number with square tiles, write each array as a multiplication, and list all "
       "the factors of the number.",
       textbook=["A number, when arranged in an array, shows the factors of that number.",
                 "3 × 5 = 15",
                 "Let us make arrays for the number 12.",
                 "3 × 4 = 12", "2 × 6 = 12", "1 × 12 = 12"],
       teach=["Predict first: you have 18 square tiles. Can you lay them in equal rows? Try 1 row, 2 rows and 3 rows. "
              "How many different arrays can you make?",
              "An array puts tiles in equal rows. 3 rows of 5 tiles is the array 3 × 5 = 15, so 3 and 5 are factors "
              "of 15.",
              "For 18 tiles, 1 row of 18 works (1 × 18), 2 rows of 9 work (2 × 9) and 3 rows of 6 work (3 × 6). 4 rows "
              "and 5 rows do not use the tiles evenly.",
              "Every array is a multiplication, and the two numbers in it are factors of 18. 6 rows of 3 is the "
              "3 × 6 array turned round, so it gives nothing new.",
              "Rule: the numbers in the multiplications of all the arrays of a number are the factors of the number."],
       examples=[WE("You have 18 square tiles. Make every array of 18 tiles and list the factors of 18.",
                    ["Try 1 row: all 18 tiles in one row. 1 × 18 = 18, so the array is 1 × 18.",
                     "Try 2 rows: 18 ÷ 2 = 9 tiles in each row. 2 × 9 = 18, so the array is 2 × 9.",
                     "Try 3 rows: 18 ÷ 3 = 6 tiles in each row. 3 × 6 = 18, so the array is 3 × 6.",
                     "Try 4 rows: 4 × 4 = 16 and 4 × 5 = 20, so 18 tiles cannot fill 4 equal rows. 4 is not a "
                     "factor.",
                     "Try 5 rows: 5 × 3 = 15 and 5 × 4 = 20, so 5 is not a factor either.",
                     "Try 6 rows: 6 × 3 = 18. This is the 3 × 6 array turned round, so it gives no new factor.",
                     "Write the numbers from the arrays: 1, 18, 2, 9, 3 and 6. In order they are 1, 2, 3, 6, 9 and 18.",
                     "Check: 18 ÷ 9 = 2 and 18 ÷ 6 = 3, so both divide 18 completely."],
                    "The arrays are 1 × 18, 2 × 9 and 3 × 6. The factors of 18 are 1, 2, 3, 6, 9 and 18")],
       ncert=["arr.def", "arr.twelve"], key_terms=["array", "arrays", "factors", "tiles"],
       misconceptions=["M_MISS_ONE_SELF"], minutes=6),
     A("T2.C2", "A Number Is a Multiple of Its Factors", "Understand",
       "Students show that a number is a multiple of each of its factors, including 1 and the number itself, by "
       "writing the multiplications that make the number.",
       textbook=["1, 2, 3, 4, 6, and 12 are all factors of 12. Each of the numbers can divide 12 completely. 12 is a "
                 "multiple of these numbers.",
                 "Do you see why 12 is a multiple of 1, 2, 3, 4, 6, and 12?",
                 "The number itself is always a multiple of itself.",
                 "The number itself and 1 are always factors of any number."],
       teach=["Predict first: the factors of 44 are 1, 2, 4, 11, 22 and 44. Is 44 a multiple of each of them? Is 44 a "
              "multiple of itself?",
              "Yes to both. A factor divides the number completely, so the number is a multiple of that factor.",
              "Each array gives two facts: 4 × 11 = 44 says that 44 is a multiple of 4 and of 11. 2 × 22 = 44 says that "
              "44 is a multiple of 2 and of 22.",
              "1 × 44 = 44 and 44 × 1 = 44. So 1 and 44 are factors of 44, and 44 is a multiple of 1 and of itself.",
              "Rule: 1 and the number itself are always factors of the number, and the number is a multiple of each "
              "of its factors."],
       examples=[WE("Show that 44 is a multiple of each of its factors 1, 2, 4, 11, 22 and 44. Is 44 a multiple of 8?",
                    ["Write the arrays of 44: 1 × 44 = 44, 2 × 22 = 44 and 4 × 11 = 44.",
                     "Each multiplication is a factor times a whole number that makes 44. So 44 is a multiple of 1, "
                     "44, 2, 22, 4 and 11.",
                     "The number itself: 44 × 1 = 44, so 44 is a multiple of itself.",
                     "Is 44 a multiple of 8? 8 × 5 = 40 and 8 × 6 = 48. 44 is between them, so 8 is not a factor of "
                     "44 and 44 is not a multiple of 8.",
                     "Check: 44 ÷ 4 = 11 and 44 ÷ 22 = 2, both exact."],
                    "44 is a multiple of each of 1, 2, 4, 11, 22 and 44, but not of 8")],
       ncert=["mult.def", "one.self"], key_terms=["multiple", "factors", "itself"],
       misconceptions=["M_FACTOR_MULTIPLE", "M_MISS_ONE_SELF"], minutes=5),
     A("T2.C3", "Numbers With Only Two Factors", "Understand",
       "Students decide whether a number has only one array by trying every number of rows, and name a number with "
       "only two factors a prime number.",
       teach=["Predict first: how many different arrays can you make with 19 tiles? And with 21 tiles?",
              "19 tiles make only one array, 1 × 19. Its only factors are 1 and 19.",
              "21 tiles make two arrays, 1 × 21 and 3 × 7. Its factors are 1, 3, 7 and 21.",
              "A number with only two factors, 1 and itself, is called a prime number. Your maths book calls 13 and "
              "37 prime numbers: each has only the array 1 × 13 or 1 × 37.",
              "Rule: a number with only one array is a prime number. Every number has at least the factors 1 and "
              "itself."],
       examples=[WE("How many arrays can you make with 19 tiles and with 21 tiles? Which of the two numbers is a "
                    "prime number?",
                    ["19 tiles: 1 row of 19 gives the array 1 × 19, because 1 × 19 = 19.",
                     "Try 2 rows: 2 × 9 = 18 and 2 × 10 = 20, so 19 tiles cannot fill 2 equal rows.",
                     "Try 3, 4 and 5 rows in the same way: 3 × 6 = 18 and 3 × 7 = 21; 4 × 4 = 16 and 4 × 5 = 20; "
                     "5 × 3 = 15 and 5 × 4 = 20. None of them makes 19.",
                     "No number of rows from 2 to 18 makes 19, so 19 has only the array 1 × 19 and only the factors "
                     "1 and 19.",
                     "21 tiles: 1 × 21 = 21 and 3 × 7 = 21, so 21 has the arrays 1 × 21 and 3 × 7 and the four "
                     "factors 1, 3, 7 and 21.",
                     "19 has only two factors, so 19 is a prime number. 21 has four factors, so it is not.",
                     "Check: 3 × 7 = 21, but no multiplication of two numbers bigger than 1 makes 19."],
                    "19 makes only the array 1 × 19, so it is a prime number. 21 makes 1 × 21 and 3 × 7, so it is "
                    "not")],
       key_terms=["prime number", "only two factors", "array"],
       misconceptions=["M_PRIME_NO_FACTORS", "M_MISS_ONE_SELF"], minutes=5),
     DOER("T2.C4", "Practice: Arrays and Factors", "array_maker", "Apply",
          "Students make the arrays of a number, list its factors, and explain why a number such as 13 or 37 has "
          "only two factors.",
          ["Each array of a number is a multiplication that shows two factors.",
           "A number is a multiple of each of its factors, and of itself.",
           "A number with only the array 1 × the number has only two factors: it is a prime number."],
          items=[FIO("arr.fifteen", "Arrays: other arrays for 15",
                     "A number, when arranged in an array, shows the factors of that number. Are there other numbers "
                     "that are factors of 15? Try to make other arrays for the number 15.",
                     ["The array in your maths book has 3 rows of 5 tiles: 3 × 5 = 15. So 3 and 5 are factors of 15.",
                      "Try 1 row: all 15 tiles in one row. 1 × 15 = 15. So 1 and 15 are factors of 15.",
                      "Try 2 rows: 2 × 7 = 14 and 2 × 8 = 16, so 15 tiles cannot fill 2 equal rows. 2 is not a "
                      "factor.",
                      "Try 4 rows: 4 × 3 = 12 and 4 × 4 = 16, so 4 is not a factor either.",
                      "5 rows of 3 is the same array as 3 rows of 5, turned round: 5 × 3 = 15.",
                      "Check: 15 ÷ 1 = 15, 15 ÷ 3 = 5, 15 ÷ 5 = 3 and 15 ÷ 15 = 1. Each division is exact."],
                     "Yes. 1 and 15, from the array 1 × 15. The factors of 15 are 1, 3, 5 and 15.",
                     kind="prompt",
                     q_figure="An array of 15 square tiles in 3 rows of 5, with the label 3 × 5 = 15 under it.",
                     s_figure="Two arrays of 15 square tiles: 3 rows of 5 labelled 3 × 5 = 15, and 1 row of 15 "
                              "labelled 1 × 15 = 15."),
                 FIO("arr.blanks12", "Arrays: why 12 is a multiple of its factors",
                     "Do you see why 12 is a multiple of 1, 2, 3, 4, 6, and 12? (a) 2 × ___ = 12 (b) 3 × ___ = 12 "
                     "(c) 12 × ___ = 12 (d) 1 × ___ = 12",
                     ["(a): 2 × 6 = 12, so the blank is 6. 12 is six 2s.",
                      "(b): 3 × 4 = 12, so the blank is 4.",
                      "(c): 12 × 1 = 12, so the blank is 1. The number itself is always a multiple of itself.",
                      "(d): 1 × 12 = 12, so the blank is 12. 1 is a factor of every number.",
                      "In each line a factor times a whole number makes 12, so 12 is a multiple of each of its "
                      "factors.",
                      "Check: 6 × 2 = 12, 4 × 3 = 12, 1 × 12 = 12 and 12 × 1 = 12."],
                     "(a): 6; (b): 4; (c): 1; (d): 12",
                     kind="prompt"),
                 FIO("LUDa.arrays", "Let Us Do (arrays), Q1",
                     "Make different arrays for the following numbers. Identify the factors in each case. (a) 10 "
                     "(b) 14 (c) 13 (d) 20 (e) 25 (f) 32 (g) 37 (h) 46 (i) 54",
                     ["(a): 10 has the arrays 1 × 10 and 2 × 5. Factors: 1, 2, 5, 10.",
                      "(b): 14 has the arrays 1 × 14 and 2 × 7. Factors: 1, 2, 7, 14.",
                      "(c): 13 has only the array 1 × 13. Factors: 1, 13.",
                      "(d): 20 has the arrays 1 × 20, 2 × 10 and 4 × 5. Factors: 1, 2, 4, 5, 10, 20.",
                      "(e): 25 has the arrays 1 × 25 and 5 × 5. Factors: 1, 5, 25. The factor 5 counts once.",
                      "(f): 32 has the arrays 1 × 32, 2 × 16 and 4 × 8. Factors: 1, 2, 4, 8, 16, 32.",
                      "(g): 37 has only the array 1 × 37. Factors: 1, 37.",
                      "(h): 46 has the arrays 1 × 46 and 2 × 23. Factors: 1, 2, 23, 46.",
                      "(i): 54 has the arrays 1 × 54, 2 × 27, 3 × 18 and 6 × 9. Factors: 1, 2, 3, 6, 9, 18, 27, 54.",
                      "Check: 5 × 5 = 25, 4 × 8 = 32, 2 × 23 = 46 and 6 × 9 = 54."],
                     "Number of factors: (a): 4; (b): 4; (c): 2; (d): 6; (e): 3; (f): 6; (g): 2; (h): 4; (i): 8. "
                     "The factors are listed in the steps.",
                     kind="exercise",
                     s_figure="The arrays of 54 as four rows of square tiles: 1 row of 54 as 1 × 54, 2 × 27, 3 × 18 "
                              "and 6 × 9, with the factors 1, 2, 3, 6, 9, 18, 27, 54 listed beside them."),
                 FIO("prime.why", "Arrays: why 13 and 37 are called prime numbers",
                     "Numbers like 13 and 37 are called prime numbers. Why?",
                     ["Make the arrays of 13: only 1 row of 13 works, so the only array is 1 × 13. The factors of 13 "
                      "are 1 and 13.",
                      "Make the arrays of 37: only 1 row of 37 works, so the only array is 1 × 37. The factors of 37 "
                      "are 1 and 37.",
                      "Each of them has only two factors, 1 and the number itself.",
                      "A number that has only two factors, 1 and itself, is called a prime number. That is why 13 "
                      "and 37 are prime numbers.",
                      "Check: 14 has 4 factors (1, 2, 7, 14), so 14 is not a prime number."],
                     "Because each has only two factors, 1 and the number itself, and only one array: 1 × 13 and "
                     "1 × 37.",
                     kind="prompt",
                     s_figure="Two arrays side by side: 13 square tiles in one row labelled 1 × 13 and 37 square "
                              "tiles in one row labelled 1 × 37, each with the note only two factors.")],
          misconceptions=["M_MISS_ONE_SELF", "M_PRIME_NO_FACTORS", "M_FACTOR_MULTIPLE"])],
    key_terms=["arrays", "factors", "prime number"]))
