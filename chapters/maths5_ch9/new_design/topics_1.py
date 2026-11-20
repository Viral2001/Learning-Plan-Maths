# -*- coding: utf-8 -*-
"""Topics T1, T1B and T2 (module M1: Division Facts and Patterns). The framing intro (Susie's array of coconuts hook and the
free Coconut Array try), the short idea topic T1B (Division Facts, with the book's opener questions), and Patterns in
Division and Place Value.
Every teaching concept has one worked example with the plan's own numbers; every book question is an FIO item of its
topic's DOER, in the book's order. Numbers the plan adds are practice values. A division with a remainder is never written
as one chain (see division_steps.py and DESIGN.md section 1)."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Susie's Array of Coconuts (framing) =====================================
# The framing topic holds only the hook video and the free-try tool, and no book question. The concept videos and the
# opener's questions follow in the short idea topic T1B.
TOPICS.append(TOPIC(
    "T1", "M1", "Susie's Array of Coconuts", ["Chapter opening"], "Understand",
    "",
    "Susie and Sunitha lay their coconuts out in an array, rows and columns. One multiplication fact tells how many "
    "coconuts there are, and the same coconuts can be split into equal groups in two ways. Try the coconut tray and "
    "find out.",
    [A("T1.C1", "Susie's Array of Coconuts", "Understand",
       "",
       textbook=["Observe the following array of coconuts. Write two division facts using the given multiplication "
                 "fact."],
       teach=["Predict first: Susie and Sunitha lay their coconuts out in 5 rows with 7 coconuts in each row. How many "
              "coconuts is that, and in how many ways can you split them into equal groups?",
              "Susie and Sunitha have a large coconut farm in Kerala. Today they lay coconuts out in an array: 5 rows, "
              "and 7 coconuts in each row.",
              "5 rows of 7 coconuts make 5 × 7 = 35 coconuts.",
              "Now think about sharing the same 35 coconuts. Split them into 7 equal groups: how many are in each "
              "group? Split them into 5 equal groups: how many now?",
              "Think about it, then try it with the coconut tray on the next screen."],
       ncert=["open.story"], key_terms=["array", "coconuts", "multiplication fact"],
       video_focus=["HOOK"], enrichment=True, minutes=4),
     DOER("T1.C3", "Coconut Array: Explore", "coconut_array", "Understand",
          "",
          ["Susie and Sunitha lay coconuts out in rows and columns.",
           "The same coconuts can be split into equal groups in two ways.",
           "Build an array, read the facts and find out."],
          misconceptions=["M_DIV_COMMUTES"], role="try_it", enrichment=True)],
    topic_type="framing", key_terms=["array", "multiplication fact", "division"]))

# ============================== T1B Division Facts =========================================================
TOPICS.append(TOPIC(
    "T1B", "M1", "Division Facts", ["Chapter opening"], "Understand",
    "Students write two division facts from one multiplication fact, name the dividend, divisor and quotient, and check "
    "a division with Dividend = Divisor × Quotient.",
    "One multiplication fact gives two division facts: the total is split into groups by the columns or by the rows. "
    "In a division fact the number that is split is the dividend, the number divided by is the divisor, and the answer "
    "is the quotient, and Dividend = Divisor × Quotient.",
    [A("T1B.C1", "Two Division Facts from One Multiplication Fact", "Understand",
       "Students write two division facts from one multiplication fact of an array of coconuts, and say what each division "
       "fact means in groups.",
       textbook=["5 × 7 = 35", "35 ÷ 5 = 7", "35 ÷ 7 = 5"],
       teach=["Predict first: 3 rows of 9 coconuts make 27. If you split the 27 coconuts into 9 equal groups, how many "
              "are in each group? If you split them into 3 equal groups, how many?",
              "The array has 3 rows and 9 columns, so the multiplication fact is 3 × 9 = 27.",
              "Split the 27 coconuts into 9 equal groups, one group for each column. Each group has 3 coconuts. That is "
              "27 ÷ 9 = 3.",
              "Split the same 27 coconuts into 3 equal groups, one group for each row. Each group has 9 coconuts. That "
              "is 27 ÷ 3 = 9.",
              "Rule: one multiplication fact gives two division facts. Divide the total by one of the two numbers and "
              "the answer is the other number."],
       examples=[WE("Susie lays out an array of 27 coconuts in 3 rows of 9 (practice values). Write the multiplication "
                    "fact and the two division facts.",
                    ["Count the rows and the columns: 3 rows and 9 columns.",
                     "Multiplication fact: 3 × 9 = 27.",
                     "Split the 27 coconuts into 9 equal groups, one for each column: 3 in each group, so 27 ÷ 9 = 3.",
                     "Split the 27 coconuts into 3 equal groups, one for each row: 9 in each group, so 27 ÷ 3 = 9.",
                     "Check: 9 × 3 = 27 and 3 × 9 = 27, so both division facts match the multiplication fact."],
                    "3 × 9 = 27, 27 ÷ 9 = 3 and 27 ÷ 3 = 9")],
       ncert=["div.facts"], key_terms=["division facts", "multiplication fact", "array", "groups"],
       misconceptions=["M_DIV_COMMUTES"], minutes=5),
     A("T1B.C2", "Dividend, Divisor and Quotient", "Understand",
       "Students name the dividend, divisor and quotient in a division fact and check it by writing Dividend = Divisor × "
       "Quotient.",
       textbook=["Dividend (N) = Divisor (D) × Quotient (Q)"],
       teach=["Predict first: in 45 ÷ 5 = 9, which number is being split, which number do we divide by, and which is the "
              "answer? Name each one.",
              "The number that is split is the dividend (N). The number we divide by is the divisor (D). The answer is "
              "the quotient (Q).",
              "In 45 ÷ 5 = 9 the dividend is 45, the divisor is 5, and the quotient is 9.",
              "Notice: Dividend = Divisor × Quotient. Here 45 = 5 × 9. This is how to check any division.",
              "Dividing by 1: 45 ÷ 1 = 45, because 1 × 45 = 45. Dividing by 1 does not make the number smaller.",
              "Rule: N = D × Q."],
       examples=[WE("Name the dividend, divisor and quotient in 45 ÷ 5 = 9, check the fact, and find 45 ÷ 1 (practice "
                    "values).",
                    ["The dividend (N) is 45, the number that is split.",
                     "The divisor (D) is 5, the number we divide by.",
                     "The quotient (Q) is 9, the answer.",
                     "Check with N = D × Q: 5 × 9 = 45, which is the dividend.",
                     "Dividing by 1: 45 ÷ 1 asks how many are in each group when 45 is split into 1 group. All 45 are "
                     "in that one group, so 45 ÷ 1 = 45.",
                     "Check: 1 × 45 = 45."],
                    "The dividend is 45, the divisor is 5 and the quotient is 9, and 45 ÷ 1 = 45")],
       ncert=["div.nqd"], key_terms=["dividend", "divisor", "quotient"],
       misconceptions=["M_DIV_SHRINKS", "M_DIV_COMMUTES"], minutes=5),
     DOER("T1B.C3", "Practice: Division Facts", None, "Apply",
          "Students write division facts for an array, find 35 ÷ 1, find numbers for the circle puzzles, and write two "
          "division statements for each multiplication.",
          ["One multiplication fact gives two division facts.",
           "Dividend = Divisor × Quotient.",
           "Check every division by multiplying the divisor and the quotient."],
          items=[
              FIO("div.example", "Example 1: array of 35 coconuts",
                  "Observe the following array of coconuts. Write two division facts using the given multiplication "
                  "fact. The array has 5 rows of 7 coconuts, and the multiplication fact is 5 × 7 = 35.",
                  ["The array has 5 rows and 7 columns, so 5 × 7 = 35 coconuts.",
                   "Split the 35 coconuts into 7 equal groups, one for each column: 5 in each group, so 35 ÷ 7 = 5.",
                   "Split the 35 coconuts into 5 equal groups, one for each row: 7 in each group, so 35 ÷ 5 = 7.",
                   "Check: 7 × 5 = 35 and 5 × 7 = 35."],
                  "35 ÷ 7 = 5 and 35 ÷ 5 = 7", kind="example",
                  q_figure="An array of coconuts, 5 rows of 7 coconuts, with the multiplication fact 5 × 7 = 35 written "
                           "under it.",
                  s_figure="The same array with the 7 columns outlined as 7 groups of 5 coconuts, beside a second copy "
                           "with the 5 rows outlined as 5 groups of 7 coconuts."),
              FIO("div.one", "Division Facts: think and answer 35 ÷ 1",
                  "Think and answer: 35 ÷ 1 = ___",
                  ["35 ÷ 1 asks: if 35 is split into 1 group, how many are in the group?",
                   "All 35 are in that one group, so 35 ÷ 1 = 35.",
                   "Check with Dividend = Divisor × Quotient: 1 × 35 = 35.",
                   "Dividing by 1 does not make the number smaller."],
                  "35 ÷ 1 = 35", kind="prompt"),
              FIO("div.array2", "Division Facts: write the facts for the second array",
                  "Write the appropriate multiplication fact for the array shown below. Write two division facts that "
                  "follow from the multiplication fact.",
                  ["Count the array: 4 rows and 8 columns.",
                   "Multiplication fact: 4 × 8 = 32.",
                   "Split the 32 coconuts into 8 equal groups, one for each column: 4 in each group, so 32 ÷ 8 = 4.",
                   "Split the 32 coconuts into 4 equal groups, one for each row: 8 in each group, so 32 ÷ 4 = 8.",
                   "Check: 8 × 4 = 32."],
                  "4 × 8 = 32, 32 ÷ 8 = 4 and 32 ÷ 4 = 8", kind="prompt",
                  q_figure="An array of coconuts, 4 rows of 8, with an empty box beside the rows and an empty box above "
                           "the columns, and three lines to fill in: one multiplication fact and two division facts.",
                  s_figure="The same array with the box beside the rows showing 4, the box above the columns showing 8, "
                           "and the three facts filled in."),
              FIO("play.times", "Let Us Play: products",
                  "Identify the numbers that can fill the circles such that the numbers in the squares are the products "
                  "or the quotients of the numbers in the circles. This row has the sign ×. The squares are 72, 60, 48, "
                  "36, 24 and 40, and the first triangle already has the circles 36 and 2.",
                  ["A product is two numbers multiplied. The two circles are multiplied to give the number in the square.",
                   "First triangle: 36 × 2 = 72, already filled in.",
                   "Square 60: find two numbers that multiply to 60: 6 × 10 = 60.",
                   "Square 48: 6 × 8 = 48.",
                   "Square 36: 4 × 9 = 36.",
                   "Square 24: 3 × 8 = 24.",
                   "Square 40: 5 × 8 = 40.",
                   "Many pairs fit each square, for example 60 = 5 × 12. Check each pair by multiplying."],
                  "Sample answer: 6 × 10 = 60, 6 × 8 = 48, 4 × 9 = 36, 3 × 8 = 24, 5 × 8 = 40. Your answer may differ",
                  kind="prompt",
                  q_figure="Six triangles each with a × sign between two circles and a square on top, the squares showing "
                           "72, 60, 48, 36, 24 and 40, the first triangle with the circles 36 and 2 filled in and the "
                           "other five with empty circles.",
                  s_figure="The same six triangles with every pair of circles filled in with a pair that multiplies to "
                           "the square."),
              FIO("play.divide", "Let Us Play: quotients",
                  "Identify the numbers that can fill the circles such that the numbers in the squares are the products "
                  "or the quotients of the numbers in the circles. This row has the sign ÷. Three triangles have the "
                  "squares 54, 42 and 56 and empty circles. Three triangles have 54, 42 and 56 in the first circle, an "
                  "empty second circle and an empty square.",
                  ["A quotient is what we get when one circle is divided by the other.",
                   "Square 54: 108 ÷ 2 = 54, because 2 × 54 = 108.",
                   "Square 42: 84 ÷ 2 = 42, because 2 × 42 = 84.",
                   "Square 56: 112 ÷ 2 = 56, because 2 × 56 = 112.",
                   "First circle 54: choose a divisor that divides 54 exactly, for example 6: 54 ÷ 6 = 9, because 6 × 9 = 54.",
                   "First circle 42: choose 7: 42 ÷ 7 = 6, because 7 × 6 = 42.",
                   "First circle 56: choose 8: 56 ÷ 8 = 7, because 8 × 7 = 56.",
                   "Other pairs fit too, for example 54 ÷ 9 = 6. Check each pair by multiplying back."],
                  "Sample answer: 108 ÷ 2 = 54, 84 ÷ 2 = 42, 112 ÷ 2 = 56, 54 ÷ 6 = 9, 42 ÷ 7 = 6, 56 ÷ 8 = 7. Your answer "
                  "may differ",
                  kind="prompt",
                  q_figure="Six triangles each with a ÷ sign between two circles and a square on top: three with the "
                           "squares 54, 42 and 56 and empty circles, and three with 54, 42 and 56 in the first circle, an "
                           "empty second circle and an empty square.",
                  s_figure="The same six triangles with the empty circles and squares filled in."),
              FIO("lud1.q1", "Let Us Do (division facts), Q1",
                  "Solve the following multiplication problems. Write two division statements in each case. (a): 30 × "
                  "30 = ___; (b): 15 × 60 = ___; (c): 400 × 8 = ___; (d): 200 × 16 = ___.",
                  ["(a): 30 × 30 = 900. Both numbers are 30, so the two division statements are the same: 900 ÷ 30 = 30.",
                   "(b): 15 × 60 = 900, so 900 ÷ 15 = 60 and 900 ÷ 60 = 15.",
                   "(c): 400 × 8 = 3200, so 3200 ÷ 400 = 8 and 3200 ÷ 8 = 400.",
                   "(d): 200 × 16 = 3200, so 3200 ÷ 200 = 16 and 3200 ÷ 16 = 200.",
                   "Relationship: the dividend is the product, and the divisor and the quotient are the two numbers that "
                   "were multiplied.",
                   "Check: 30 × 30 = 900, 60 × 15 = 900, 8 × 400 = 3200 and 16 × 200 = 3200."],
                  "900 ÷ 30 = 30; 900 ÷ 15 = 60, 900 ÷ 60 = 15; 3200 ÷ 400 = 8, 3200 ÷ 8 = 400; 3200 ÷ 200 = 16, "
                  "3200 ÷ 16 = 200",
                  kind="exercise",
                  q_figure="Four boxes in two rows of two, each with a multiplication to solve and two lines for the two "
                           "division statements.")],
          misconceptions=["M_DIV_COMMUTES", "M_DIV_SHRINKS"])],
    key_terms=["division facts", "dividend", "divisor", "quotient"]))

# ============================== T2 Patterns in Division and Place Value ====================================
_chart_note = ("The chart has the columns Problem, Hundreds, Tens and Ones. The rows 40 ÷ 10, 400 ÷ 10 and 4000 ÷ 10 are "
               "filled in as examples: 4 in the ones place; 4 in the tens place and 0 in the ones place; 4 in the "
               "hundreds place and 0 in the tens and ones places.")

TOPICS.append(TOPIC(
    "T2", "M1", "Patterns in Division and Place Value", ["Patterns in Division and Place Value"], "Apply",
    "Students divide tens, hundreds and thousands using a table fact, and describe the pattern of zeros and place value "
    "when a number is divided by 10.",
    "A table fact such as 27 ÷ 9 = 3 gives 270 ÷ 9 = 30 and 2700 ÷ 9 = 300. Each zero added to the dividend adds a zero to "
    "the quotient, and dividing by 10 moves every digit one place to the right.",
    [A("T2.C1", "Table Facts for Tens and Hundreds", "Apply",
       "Students divide tens and hundreds by using a table fact, such as 27 ÷ 9 = 3 to find 270 ÷ 9, and check the "
       "quotient by multiplying.",
       teach=["Predict first: how many groups of 9 are in 270? Start with the table fact 27 ÷ 9 = 3.",
              "270 is 27 tens. The table fact says 27 ÷ 9 = 3, so 27 tens split into groups of 9 gives 3 tens.",
              "3 tens is 30, so 270 ÷ 9 = 30.",
              "Check the quotient by multiplying: 9 × 30 = 270.",
              "The same works with hundreds. 2700 is 27 hundreds, so 2700 ÷ 9 = 300.",
              "Rule: use the table fact, then put back the tens or the hundreds."],
       examples=[WE("How many groups of 9 are in 270? Then find 2700 ÷ 9 and 2700 ÷ 90 (practice values).",
                    ["270 is 27 tens, and the table fact is 27 ÷ 9 = 3.",
                     "27 tens split into groups of 9 gives 3 tens, which is 30. So 270 ÷ 9 = 30.",
                     "Check: 9 × 30 = 270.",
                     "2700 is 27 hundreds. 27 hundreds split into groups of 9 gives 3 hundreds. So 2700 ÷ 9 = 300.",
                     "Check: 9 × 300 = 2700.",
                     "2700 ÷ 90: 90 is 9 tens, so the answer is the same as for 270 ÷ 9. 2700 ÷ 90 = 30.",
                     "Check: 90 × 30 = 2700."],
                    "270 ÷ 9 = 30, 2700 ÷ 9 = 300 and 2700 ÷ 90 = 30")],
       key_terms=["table fact", "tens", "hundreds", "quotient"], misconceptions=["M_ZEROS_LOST"], minutes=5),
     A("T2.C2", "Zeros and Place Value Patterns", "Understand",
       "Students describe how the zeros and the digits change in a quotient when a number is divided by 10, by 100 or by "
       "a number with the same digits.",
       textbook=["What patterns do you notice here?",
                 "What is happening to the quotients in each case? Discuss."],
       teach=["Predict first: 50 ÷ 10 = 5. What is 500 ÷ 10, and what is 5000 ÷ 10?",
              "Look at 70 ÷ 10 = 7, 700 ÷ 10 = 70 and 7000 ÷ 10 = 700. Each time the dividend gets one more zero, the "
              "quotient gets one more zero.",
              "On a place value chart the digit 7 slides one place to the right each time we divide by 10: from the tens "
              "to the ones, from the hundreds to the tens, from the thousands to the hundreds.",
              "Dividing by 100 slides the digits two places: 7000 ÷ 100 = 70.",
              "When the dividend is the divisor with zeros added, the quotient is 10 or 100: 3500 ÷ 35 = 100, because 35 × "
              "100 = 3500.",
              "Rule: dividing by 10 moves every digit one place to the right, and dividing by 100 moves it two places."],
       examples=[WE("Divide 70, 700 and 7000 by 10, and then divide 3500 by 35 (practice values).",
                    ["70 ÷ 10 = 7: the 7 tens become 7 ones.",
                     "700 ÷ 10 = 70: the 7 hundreds become 7 tens.",
                     "7000 ÷ 10 = 700: the 7 thousands become 7 hundreds.",
                     "Pattern: one more zero in the dividend gives one more zero in the quotient, and the digit 7 moves "
                     "one place to the right each time.",
                     "3500 is 35 with two zeros added, so 3500 ÷ 35 = 100.",
                     "Check: 35 × 100 = 3500."],
                    "70 ÷ 10 = 7, 700 ÷ 10 = 70, 7000 ÷ 10 = 700 and 3500 ÷ 35 = 100")],
       ncert=["pd.notice", "pd.quotients"], key_terms=["zeros", "place value", "pattern", "digits"],
       misconceptions=["M_ZEROS_LOST"], minutes=6),
     DOER("T2.C3", "Practice: Place Value Shifter", "place_value_shifter", "Apply",
          "Students solve divisions of tens, hundreds and thousands, fill the place value charts with the quotient digits, "
          "and solve the money, distance and puzzle questions by dividing.",
          ["Use a table fact for tens and hundreds.",
           "One more zero in the dividend gives one more zero in the quotient.",
           "Check every division by multiplying the divisor and the quotient."],
          items=[
              FIO("pd.q2", "Let Us Do (dividing tens and hundreds), Q2",
                  "Solve the following division problems. Notice the patterns and discuss in class. (a): 150 ÷ 3 = ___; "
                  "(b): 80 ÷ 4 = ___; (c): 500 ÷ 5 = ___; (d): 100 ÷ 10 = ___; (e): 300 ÷ 100 = ___; (f): 500 ÷ 50 = ___; "
                  "(g): 200 ÷ 20 = ___; (h): 440 ÷ 44 = ___; (i): 630 ÷ 63 = ___. The book's hints: how many groups of 3 "
                  "are in 150; 5 × ___ = 500; 44 × ___ = 440.",
                  ["(a): 150 is 15 tens, and 15 ÷ 3 = 5, so 150 ÷ 3 = 50. Check: 3 × 50 = 150.",
                   "(b): 80 is 8 tens, and 8 ÷ 4 = 2, so 80 ÷ 4 = 20. Check: 4 × 20 = 80.",
                   "(c): 500 is 5 hundreds, and 5 ÷ 5 = 1, so 500 ÷ 5 = 100. Check: 5 × 100 = 500.",
                   "(d): 100 ÷ 10 = 10, because 10 × 10 = 100.",
                   "(e): 300 ÷ 100 = 3, because 100 × 3 = 300.",
                   "(f): 500 ÷ 50 = 10, because 50 × 10 = 500.",
                   "(g): 200 ÷ 20 = 10, because 20 × 10 = 200.",
                   "(h): 440 ÷ 44 = 10, because 44 × 10 = 440.",
                   "(i): 630 ÷ 63 = 10, because 63 × 10 = 630.",
                   "Pattern: when the dividend is the divisor with a zero added, the quotient is 10."],
                  "(a): 50; (b): 20; (c): 100; (d): 10; (e): 3; (f): 10; (g): 10; (h): 10; (i): 10",
                  kind="exercise",
                  q_figure="Nine boxes in three rows of three, each with a division and a blank, and three small hints "
                           "beside three of the boxes."),
              FIO("pd.patterns", "Patterns in Division and Place Value: nine divisions",
                  "Patterns in Division and Place Value. Solve: (a): 1000 ÷ 10 = ___; (b): 1000 ÷ 100 = ___; (c): 1600 ÷ 4 = "
                  "___; (d): 2000 ÷ 2 = ___; (e): 2000 ÷ 20 = ___; (f): 3700 ÷ 37 = ___; (g): 3300 ÷ 3 = ___; (h): 3300 ÷ "
                  "300 = ___; (i): 4000 ÷ 40 = ___. The book's hints: 10 × ___ = 1000 and 37 × ___ = 3700.",
                  ["(a): 1000 ÷ 10 = 100, because 10 × 100 = 1000.",
                   "(b): 1000 ÷ 100 = 10, because 100 × 10 = 1000.",
                   "(c): 1600 is 16 hundreds, and 16 ÷ 4 = 4, so 1600 ÷ 4 = 400.",
                   "(d): 2000 is 2 thousands, and 2 ÷ 2 = 1, so 2000 ÷ 2 = 1000.",
                   "(e): 2000 ÷ 20 = 100, because 20 × 100 = 2000.",
                   "(f): 3700 ÷ 37 = 100, because 37 × 100 = 3700.",
                   "(g): 3300 is 33 hundreds, and 33 ÷ 3 = 11, so 3300 ÷ 3 = 1100.",
                   "(h): 3300 ÷ 300 = 11, because 300 × 11 = 3300.",
                   "(i): 4000 ÷ 40 = 100, because 40 × 100 = 4000.",
                   "Pattern: take the zeros of the divisor away from the zeros of the dividend and use the table fact."],
                  "(a): 100; (b): 10; (c): 400; (d): 1000; (e): 100; (f): 100; (g): 1100; (h): 11; (i): 100",
                  kind="prompt",
                  q_figure="Nine boxes in three rows of three, each with a division to solve, and two small hints beside "
                           "two of the boxes."),
              FIO("pd.chart_left", "Patterns in Division and Place Value: place value chart (1)",
                  "Now fill the place value chart. " + _chart_note + " Fill the rows (a): 700 ÷ 70; (b): 1400 ÷ 100; "
                  "(c): 220 ÷ 20; (d): 2200 ÷ 20.",
                  ["(a): 700 ÷ 70 = 10, because 70 × 10 = 700. Write 1 in the tens place and 0 in the ones place.",
                   "(b): 1400 ÷ 100 = 14, because 100 × 14 = 1400. Write 1 in the tens place and 4 in the ones place.",
                   "(c): 220 ÷ 20 = 11, because 20 × 11 = 220. Write 1 in the tens place and 1 in the ones place.",
                   "(d): 2200 ÷ 20 = 110, because 20 × 110 = 2200. Write 1 in the hundreds place, 1 in the tens place and "
                   "0 in the ones place."],
                  "(a): 10; (b): 14; (c): 11; (d): 110, with hundreds 1, tens 1, ones 0",
                  kind="prompt",
                  q_figure="A table with the columns Problem, Hundreds, Tens and Ones: the rows 40 ÷ 10, 400 ÷ 10 and "
                           "4000 ÷ 10 are filled in and the rows 700 ÷ 70, 1400 ÷ 100, 220 ÷ 20 and 2200 ÷ 20 are empty.",
                  s_figure="The same table with the four empty rows filled in."),
              FIO("pd.chart_right", "Patterns in Division and Place Value: place value chart (2)",
                  "Now fill the place value chart. The second chart has the columns Problem, Hundreds, Tens and Ones and "
                  "the empty rows (a): 110 ÷ 11; (b): 860 ÷ 86; (c): 7500 ÷ 750; (d): 8800 ÷ 88; (e): 2400 ÷ 24; (f): "
                  "440 ÷ 22.",
                  ["(a): 110 ÷ 11 = 10, because 11 × 10 = 110. Tens 1, ones 0.",
                   "(b): 860 ÷ 86 = 10, because 86 × 10 = 860. Tens 1, ones 0.",
                   "(c): 7500 ÷ 750 = 10, because 750 × 10 = 7500. Tens 1, ones 0.",
                   "(d): 8800 ÷ 88 = 100, because 88 × 100 = 8800. Hundreds 1, tens 0, ones 0.",
                   "(e): 2400 ÷ 24 = 100, because 24 × 100 = 2400. Hundreds 1, tens 0, ones 0.",
                   "(f): 440 ÷ 22 = 20, because 22 × 20 = 440. Tens 2, ones 0."],
                  "(a): 10; (b): 10; (c): 10; (d): 100; (e): 100; (f): 20",
                  kind="prompt",
                  q_figure="A table with the columns Problem, Hundreds, Tens and Ones and six empty rows: 110 ÷ 11, 860 ÷ "
                           "86, 7500 ÷ 750, 8800 ÷ 88, 2400 ÷ 24 and 440 ÷ 22.",
                  s_figure="The same table with the six rows filled in."),
              FIO("lud2.q1", "Let Us Do (division with tens and hundreds), Q1",
                  "Sabina cycles 160 km in 20 days and the same distance each day. How many kilometres does she cycle "
                  "each day?",
                  ["The distance is shared equally over the days, so divide: 160 ÷ 20.",
                   "160 is 16 tens and 20 is 2 tens, so 16 ÷ 2 = 8 gives 160 ÷ 20 = 8.",
                   "Check: 20 × 8 = 160."],
                  "8 km each day", kind="exercise"),
              FIO("lud2.q2", "Let Us Do (division with tens and hundreds), Q2",
                  "How many notes of ₹100 does Seema need to carry if she wants to buy coconuts worth ₹4200?",
                  ["The notes are of ₹100 each, so divide the money by 100: 4200 ÷ 100.",
                   "4200 is 42 hundreds, so 4200 ÷ 100 = 42.",
                   "Check: 100 × 42 = 4200."],
                  "42 notes", kind="exercise"),
              FIO("lud2.q3", "Let Us Do (division with tens and hundreds), Q3",
                  "The owner of an electric store has decided to distribute ₹5500 equally amongst 5 of his employees as a "
                  "Diwali gift. What amount will each employee get?",
                  ["Share ₹5500 equally among 5 employees: 5500 ÷ 5.",
                   "5500 is 55 hundreds, and 55 ÷ 5 = 11, so 5500 ÷ 5 = 1100.",
                   "Check: 5 × 1100 = 5500."],
                  "₹1100", kind="exercise"),
              FIO("lud2.q3b", "Let Us Do (division with tens and hundreds), Q3 continued",
                  "What will happen if he distributes the same amount of money among 10 employees? Will each employee get "
                  "more or less? How much money would he have to distribute if everyone must get the same amount as "
                  "earlier?",
                  ["Share ₹5500 among 10 employees: 5500 ÷ 10 = 550.",
                   "Each employee now gets ₹550, which is less than ₹1100. There are twice as many employees sharing the "
                   "same money, so each gets half.",
                   "For every employee to get ₹1100 as earlier, 10 employees need 10 × 1100 = 11000 rupees.",
                   "Check: 11000 ÷ 10 = 1100."],
                  "Each gets ₹550, which is less; he needs ₹11000", kind="exercise"),
              FIO("lud2.q4", "Let Us Do (division with tens and hundreds), Q4",
                  "Place the numbers 1 to 8 in the following boxes so that all the four operations, division, "
                  "multiplication, addition and subtraction are correct. No number must be repeated. How did you think "
                  "about solving this? Is there more than one answer?",
                  ["Name the boxes: top row A ÷ B = C; A − D = F down the left; C × E = H down the right; F + G = H along "
                   "the bottom.",
                   "Start with the division A ÷ B = C. The numbers are from 1 to 8 and each is used once, so try 6 ÷ 3 = 2 "
                   "and 8 ÷ 4 = 2.",
                   "Try 6 ÷ 3 = 2: then A = 6, B = 3, C = 2. Left column: 6 − D = F. Right column: 2 × E = H.",
                   "The numbers left are 1, 4, 5, 7 and 8. Try E = 4: 2 × 4 = 8, so H = 8. Then D = 5 gives 6 − 5 = 1, so "
                   "F = 1, and G = 7 gives 1 + 7 = 8.",
                   "First answer: 6 ÷ 3 = 2, 6 − 5 = 1, 2 × 4 = 8, 1 + 7 = 8. All eight numbers 6, 3, 2, 5, 1, 4, 7, 8 are "
                   "different.",
                   "Try 8 ÷ 4 = 2: then A = 8, B = 4, C = 2. Try E = 3: 2 × 3 = 6, so H = 6. Then D = 7 gives 8 − 7 = 1, so "
                   "F = 1, and G = 5 gives 1 + 5 = 6.",
                   "Second answer: 8 ÷ 4 = 2, 8 − 7 = 1, 2 × 3 = 6, 1 + 5 = 6. All eight numbers 8, 4, 2, 7, 1, 3, 5, 6 are "
                   "different.",
                   "Trying every placement of 1 to 8 shows there are exactly two answers."],
                  "Yes, two answers: 6 ÷ 3 = 2, 6 − 5 = 1, 2 × 4 = 8, 1 + 7 = 8; or 8 ÷ 4 = 2, 8 − 7 = 1, 2 × 3 = 6, 1 + 5 = 6",
                  kind="exercise",
                  q_figure="Eight empty hexagon boxes: a top row of three with a ÷ sign after the first and an = sign after "
                           "the second; one box under the first with a − sign between them; one box under the third with a "
                           "× sign between them; and a bottom row of three with a + sign after the first and an = sign after "
                           "the second.",
                  s_figure="The same eight boxes filled in with the first answer: 6, 3, 2 on top, 5 and 4 below, and 1, 7, 8 "
                           "at the bottom."),
              FIO("lud2.q5", "Let Us Do (division with tens and hundreds), Q5",
                  "Fill in the blanks. (a): ___ ÷ 18 = 100; (b): ___ ÷ 10 = 610; (c): ___ ÷ 100 = 72; (d): ___ ÷ 100 = 10; "
                  "(e): 870 ÷ ___ = 87; (f): ___ ÷ 100 = 70; (g): 200 ÷ ___ = 2; (h): 130 ÷ ___ = 13.",
                  ["Use Dividend = Divisor × Quotient.",
                   "(a): the dividend is 18 × 100 = 1800.",
                   "(b): the dividend is 10 × 610 = 6100.",
                   "(c): the dividend is 100 × 72 = 7200.",
                   "(d): the dividend is 100 × 10 = 1000.",
                   "(e): the divisor is 870 ÷ 87 = 10.",
                   "(f): the dividend is 100 × 70 = 7000.",
                   "(g): the divisor is 200 ÷ 2 = 100.",
                   "(h): the divisor is 130 ÷ 13 = 10.",
                   "Check: 1800 ÷ 18 = 100 and 130 ÷ 10 = 13."],
                  "(a): 1800; (b): 6100; (c): 7200; (d): 1000; (e): 10; (f): 7000; (g): 100; (h): 10",
                  kind="exercise")],
          misconceptions=["M_ZEROS_LOST"])],
    key_terms=["table fact", "zeros", "place value", "quotient"]))
