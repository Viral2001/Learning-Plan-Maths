# -*- coding: utf-8 -*-
"""Topics T3 and T4 (module M2: pyramids and grids). Book sections 6.3 and 6.4, pp 137 to 142."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T3 Number pyramids ========================================================
TOPICS.append(TOPIC(
    "T3", "M2", "Number Pyramids", ["6.3"], "Analyze",
    "Students fill number pyramids upward by adding and downward by subtracting, use letter-numbers for boxes that "
    "cannot be filled directly, and write the top of a pyramid in terms of its bottom row.",
    "Each box is the sum of the two boxes below it. Going up we add, going down we subtract, a letter fills a box we "
    "cannot reach, and the top of a three row pyramid is a + 2b + c.",
    [A("T3.C1", "Building a pyramid upward", "Apply",
       "Students apply the rule that each box is the sum of the two boxes directly below it to fill pyramids with "
       "two, three and four rows.",
       textbook=["6.3 Number Pyramids",
                 "In a number pyramid, each number is the sum of the two numbers directly below it (see the figure).",
                 "Bottom row 1, 9, 4; middle row 10, 13; top 23.",
                 "Use the same rule to fill these pyramids: bottom row 6, 2; bottom row 3, 4, 3; bottom row 5, 4, 5, 0."],
       teach=["Predict first: in the pyramid with bottom row 1, 9, 4, which bottom number counts most towards the top?",
              "Add neighbours: 1 + 9 = 10 and 9 + 4 = 13, then 10 + 13 = 23 at the top.",
              "Each new row is one box shorter, so a pyramid with a bottom row of four boxes has four rows."],
       examples=[
           WE("Fill the pyramids with bottom rows 6, 2 and 3, 4, 3 and 5, 4, 5, 0.",
              ["Bottom row 6, 2: the top is 6 + 2 = 8.",
               "Bottom row 3, 4, 3: the middle row is 3 + 4 = 7 and 4 + 3 = 7, and the top is 7 + 7 = 14.",
               "Bottom row 5, 4, 5, 0: the next row is 5 + 4 = 9, 4 + 5 = 9 and 5 + 0 = 5.",
               "Then 9 + 9 = 18 and 9 + 5 = 14, and the top is 18 + 14 = 32."],
              "Tops 8, 14 and 32",
              ncert=["6.3.rule", "6.3.fill_up"])],
       key_terms=["number pyramid", "sum"], misconceptions=["M_PYR_TOP_SUM"], minutes=8),
     A("T3.C2", "Working back down a pyramid", "Apply",
       "Students fill a pyramid from the top down by subtracting a given box from the box above it, and choose the "
       "box where the filling can start.",
       textbook=["How do we fill this pyramid? Top 10; middle row 4 and a blank; bottom row 1 and two blanks.",
                 "10 − 4 = 6. 4 − 1 = 3. 6 − 3 = 3."],
       teach=["Predict first: which empty box can you fill straight away, and how?",
              "A box above is the sum of the two below, so a missing box below is the box above minus its neighbour.",
              "Start where a box and one of its two parts are known, then keep going."],
       examples=[
           WE("A pyramid has top 10, middle row 4 and a blank, and bottom row 1 and two blanks. Fill it.",
              ["The middle blank is 10 − 4 = 6.",
               "Below the 4 sit 1 and a blank, so that blank is 4 − 1 = 3.",
               "Below the 6 sit 3 and the last blank, so it is 6 − 3 = 3.",
               "Check going up: 1 + 3 = 4, 3 + 3 = 6, 4 + 6 = 10."],
              "Middle row 4, 6; bottom row 1, 3, 3",
              ncert=["6.3.fill_down"])],
       key_terms=["subtract", "missing box"], misconceptions=["M_PYR_DOWN_ADD"], minutes=8),
     A("T3.C2x", "Letters for the boxes we cannot reach", "Analyze",
       "Students put letter-numbers in the empty boxes of a pyramid with top 60 and bottom row 12, blank, 8, write "
       "equations from the rule, and solve them.",
       textbook=["What about filling in the numbers in this pyramid? Where do we start? Top 60; middle row two blanks; "
                 "bottom row 12, a blank, 8.",
                 "Let us fill the empty boxes with letter-numbers. From the rules for filling up pyramids, we get the "
                 "following equations. a + b = 60. 12 + c = a. c + 8 = b.",
                 "From this, we see that, (12 + c) + (c + 8) = a + b = 60. Hence, 20 + 2c = 60. 2c = 60 − 20 = 40. "
                 "c = 20.",
                 "Once we know c, we can find a and b, and complete the pyramid."],
       teach=["Predict first: no box here has both of its parts known, so where can we start?",
              "Name the blanks a, b and c, write one equation for each box, and combine them.",
              "Once c is found, a and b follow."],
       examples=[
           WE("Fill the pyramid with top 60 and bottom row 12, a blank, 8.",
              ["Call the middle row a and b and the bottom blank c.",
               "The rule gives a + b = 60, a = 12 + c and b = c + 8.",
               "So (12 + c) + (c + 8) = 60, which is 20 + 2c = 60.",
               "Then 2c = 40, so c is 20, a is 32 and b is 28.",
               "Check: 12 + 20 = 32, 20 + 8 = 28, 32 + 28 = 60."],
              "Middle row 32, 28; bottom row 12, 20, 8",
              ncert=["6.3.fill60"])],
       key_terms=["letter-number", "equation"], minutes=8, thin=True),
     A("T3.C2y", "A four row pyramid with top 50", "Analyze",
       "Students fill a four row pyramid with top 50, a 22 in the second row and bottom row 4, blank, 6, blank by "
       "writing the blanks as letters.",
       textbook=["Fill the following pyramids:",
                 "First pyramid: top 50; second row a blank and 22; third row three blanks; bottom row 4, a blank, 6, a "
                 "blank."],
       teach=["Predict first: two bottom boxes are missing, so how many equations will we need?",
              "Call the missing bottom boxes p and q and write the rows above in terms of them.",
              "One equation comes from the 22 and one from the top; solve them together."],
       examples=[
           WE("Fill the four row pyramid with top 50, second row a blank and 22, and bottom row 4, a blank, 6, a blank.",
              ["Call the bottom blanks p and q: the bottom row is 4, p, 6, q.",
               "Third row: 4 + p, p + 6, 6 + q. The 22 is (p + 6) + (6 + q), so p + q + 12 = 22 and p + q = 10.",
               "The top is (4 + p) + 2(p + 6) + (6 + q), which is 3p + q + 22, so 3p + q + 22 = 50 and 3p + q = 28.",
               "Take p + q = 10 away from 3p + q = 28: that leaves 2p = 18, so p is 9 and q is 1.",
               "Third row 13, 15, 7; second row 28, 22; check 28 + 22 = 50."],
              "Bottom row 4, 9, 6, 1; third row 13, 15, 7; second row 28, 22",
              ncert=["6.3.fill_three_a"])],
       key_terms=["letter-number", "pyramid"], minutes=8, thin=True),
     A("T3.C2z", "Two more four row pyramids", "Analyze",
       "Students fill two more four row pyramids, one with a 40 and a 9 given and one with top 35, by choosing the box "
       "to start from or by using letter-numbers.",
       textbook=["Second pyramid: top blank; second row 40 and a blank; third row two blanks and 9; bottom row 5, a "
                 "blank, 7, a blank.",
                 "Third pyramid: top 35; second row two blanks; third row two blanks and 7; bottom row 3, 5, two "
                 "blanks."],
       teach=["Predict first: in the second pyramid, which bottom blank can be found at once?",
              "The 9 sits above 7 and a blank, so that blank is 9 − 7 = 2. Then a letter handles the other blank.",
              "In the third pyramid two bottom boxes are missing: use the 7 and the top 35 as the two equations."],
       examples=[
           WE("Fill the pyramid with second row 40 and a blank, third row ending in 9, and bottom row 5, a blank, 7, a "
              "blank. Then fill the pyramid with top 35, third row ending in 7, and bottom row 3, 5, two blanks.",
              ["Second pyramid: the last bottom box is 9 − 7 = 2. Call the other blank p.",
               "The 40 is (5 + p) + (p + 7), so 2p + 12 = 40 and p is 14. Third row 19, 21, 9; second row 40, 30; "
               "top 40 + 30 = 70.",
               "Third pyramid: call the bottom blanks r and s, so r + s = 7 from the 7 above them.",
               "The top is 3 + 3 × 5 + 3r + s, so 18 + 3r + s = 35 and 3r + s = 17. With r + s = 7, 2r = 10, so r is 5 "
               "and s is 2.",
               "Third row 8, 10, 7; second row 18, 17; check 18 + 17 = 35."],
              "First: bottom 5, 14, 7, 2 and top 70. Second: bottom 3, 5, 5, 2 with rows 8, 10, 7 and 18, 17",
              ncert=["6.3.fill_three_bc"])],
       key_terms=["letter-number", "pyramid"], minutes=8, thin=True),
     A("T3.C3", "The top in terms of the bottom row", "Analyze",
       "Students write the top of two and three row pyramids in terms of the bottom row letters and use a + 2b + c "
       "to find a top without building the pyramid.",
       textbook=["What is the relationship between the numbers in the bottom row and the number at the top?",
                 "Let us start with the simplest pyramid. Bottom row a, b; top a + b.",
                 "What about a pyramid with three rows?",
                 "Using letter numbers for the bottom row, we can write an expression for the top row. Bottom row a, b, "
                 "c; middle row a + b, b + c; top a + 2b + c."],
       teach=["Predict first: is the top just the sum of the bottom row?",
              "With bottom a, b, c the middle row is a + b and b + c, so the top is a + 2b + c.",
              "The middle number counts twice, because it feeds both boxes above it.",
              "Check with 1, 9, 4: 1 + 2 × 9 + 4 = 23, the same top as before."],
       examples=[
           WE("Write the top of a three row pyramid with bottom row a, b, c. Use it for the bottom row 1, 9, 4.",
              ["The middle row is a + b and b + c.",
               "The top is (a + b) + (b + c), which is a + 2b + c.",
               "For 1, 9, 4: 1 + 2 × 9 + 4 = 23.",
               "Building it gives 10, 13 and then 23, the same top."],
              "The top is a + 2b + c; for 1, 9, 4 it is 23",
              ncert=["6.3.relation"])],
       key_terms=["expression", "top", "bottom row"], misconceptions=["M_PYR_TOP_SUM"], minutes=10),
     DOER("T3.C4", "Practice: tops of pyramids and Fibonacci pyramids", "pyramid_builder", "Analyze",
          "Students find pyramid tops from the bottom row with a + 2b + c and its four row version, and build "
          "pyramids on Virahanka-Fibonacci numbers to spot which numbers appear.",
          ["Each box is the sum of the two below it.",
           "Three rows: the top is a + 2b + c. Four rows: the top is a + 3b + 3c + d."],
          items=[
              FIO("FiOA.q1", "Figure it Out (number pyramids, question 1)",
                  "Without building the entire pyramid, find the number in the topmost row given the bottom row in "
                  "each of these cases: 4, 13, 8 and 7, 11, 3 and 10, 14, 25.",
                  ["The top of a three row pyramid is a + 2b + c.",
                   "4, 13, 8: 4 + 26 + 8 = 38.",
                   "7, 11, 3: 7 + 22 + 3 = 32.",
                   "10, 14, 25: 10 + 28 + 25 = 63."],
                  "38, 32 and 63"),
              FIO("FiOA.q2", "Figure it Out (number pyramids, question 2)",
                  "Write an expression for the topmost row of a pyramid with 4 rows in terms of the values in the "
                  "bottom row.",
                  ["Bottom row a, b, c, d. The next row is a + b, b + c, c + d.",
                   "The row above that is a + 2b + c and b + 2c + d.",
                   "The top is (a + 2b + c) + (b + 2c + d), which is a + 3b + 3c + d."],
                  "a + 3b + 3c + d"),
              FIO("FiOA.q3", "Figure it Out (number pyramids, question 3)",
                  "Without building the entire pyramid, find the number in the topmost row given the bottom row in "
                  "each of these cases: 8, 19, 21, 13 and 7, 18, 19, 6 and 9, 7, 5, 11.",
                  ["Use a + 3b + 3c + d.",
                   "8, 19, 21, 13: 8 + 57 + 63 + 13 = 141.",
                   "7, 18, 19, 6: 7 + 54 + 57 + 6 = 124.",
                   "9, 7, 5, 11: 9 + 21 + 15 + 11 = 56."],
                  "141, 124 and 56"),
              FIO("FiOA.q4", "Figure it Out (number pyramids, question 4)",
                  "Recall the Virahanka-Fibonacci number sequence 1, 2, 3, 5, ... where each number is the sum of the "
                  "two numbers before it. If the first three Virahanka-Fibonacci numbers are written in the bottom row "
                  "of a number pyramid with three rows, fill in the rest of the pyramid. What numbers appear in the "
                  "grid? What is the number at the top? Are they all Virahanka-Fibonacci numbers?",
                  ["The bottom row is 1, 2, 3.",
                   "The middle row is 1 + 2 = 3 and 2 + 3 = 5.",
                   "The top is 3 + 5 = 8.",
                   "The sequence goes 1, 2, 3, 5, 8, so every number in the grid is in it."],
                  "The grid holds 1, 2, 3, 3, 5 and 8; the top is 8; all are Virahanka-Fibonacci numbers"),
              FIO("FiOA.q5", "Figure it Out (number pyramids, question 5)",
                  "What can you say about the numbers in the pyramid and the number at the top in the following cases? "
                  "(i) The first four Virahanka-Fibonacci numbers are written in the bottom row of a four row pyramid. "
                  "(ii) The first 29 Virahanka-Fibonacci numbers are written in the bottom row of a 29 row pyramid.",
                  ["(i) Bottom row 1, 2, 3, 5. Next row 3, 5, 8. Next row 8, 13. Top 8 + 13 = 21.",
                   "All of them are Virahanka-Fibonacci numbers, and the top 21 is the 7th number of 1, 2, 3, 5, ...",
                   "Two neighbours in the sequence add to the number two places further on, so every row is again a "
                   "run of Virahanka-Fibonacci numbers, moved two places along.",
                   "(ii) Each row moves two places along, so after 28 steps up the single top box is the 57th number "
                   "of the sequence."],
                  "(i) All are Virahanka-Fibonacci numbers and the top is 21 (ii) All are Virahanka-Fibonacci numbers "
                  "and the top is the 57th number of the sequence"),
              FIO("FiOA.q6", "Figure it Out (number pyramids, question 6)",
                  "If the bottom row of an n row pyramid contains the first n Virahanka-Fibonacci numbers, what can we "
                  "say about the numbers in the pyramid? What can we say about the number at the top?",
                  ["Two neighbours of the sequence add to the number two places further on.",
                   "So each row is a run of Virahanka-Fibonacci numbers, starting two places further along than the "
                   "row below.",
                   "The bottom row starts at the 1st number, so the top row, n − 1 steps up, is the number at place "
                   "1 + 2(n − 1), which is the (2n − 1)th number.",
                   "Check: n = 3 gives the 5th number, 8; n = 4 gives the 7th number, 21."],
                  "Every number in the pyramid is a Virahanka-Fibonacci number, and the top is the (2n − 1)th number of "
                  "the sequence")],
          misconceptions=["M_PYR_TOP_SUM", "M_PYR_DOWN_ADD"])],
    key_terms=["number pyramid", "expression", "letter-number"]))

# ============================== T4 Calendar magic and algebra grids =======================================
TOPICS.append(TOPIC(
    "T4", "M2", "Calendar Magic and Algebra Grids", ["6.4"], "Apply",
    "Students write the dates of a calendar block in terms of the top left date, find the block from its sum, "
    "design a calendar trick of their own, and find the values of shapes in an algebra grid from its row sums.",
    "In a calendar block the dates are a, a + 1, a + 7 and a + 8, so their sum 4a + 16 gives a away. In an algebra "
    "grid each shape is an unknown number found from the row sums.",
    [A("T4.C1", "The 2 by 2 calendar block trick", "Apply",
       "Students write a 2 by 2 calendar block as a, a + 1, a + 7, a + 8, add them to get 4a + 16, and solve for the "
       "block when the sum is given.",
       textbook=["6.4 Fun with Grids",
                 "Calendar Magic",
                 "A page from a calendar is given below. Your friend picks a 2 × 2 grid from this calendar, adds the 4 "
                 "numbers in this grid and tells you the sum.",
                 "August 2025 block 6, 7, 13, 14: 6 + 7 + 13 + 14 = 40.",
                 "Can we find the 4 numbers in the grid from just knowing this sum?",
                 "Let us use algebra. Consider a 2 × 2 grid. Let a represent the top left number. What are the other "
                 "numbers in terms of a? a, a + 1, a + 7, a + 8.",
                 "Adding all four numbers, the sum is a + (a + 1) + (a + 7) + (a + 8) = 4a + 16.",
                 "Suppose you are told that the sum is 36. Can you find the 4 numbers in the grid?",
                 "4a + 16 = 36. 4a = 20 (subtracting 16 from both sides). a = 5 (dividing both sides by 4).",
                 "Now that we have found a, we know that the other three numbers are a + 1, a + 7 and a + 8. Therefore, "
                 "the grid must be the following: 5, 6, 12, 13."],
       teach=["Predict first: if a friend tells you only the sum of a block, can you name all four dates?",
              "The date to the right is one more and the date below is seven more, because a week has seven days.",
              "So the block is a, a + 1, a + 7, a + 8 and its sum is 4a + 16.",
              "Take 16 from the sum and divide by 4 to get the top left date."],
       examples=[
           WE("A friend picks a 2 by 2 block from a calendar page and says the sum is 36. Find the block. Check the "
              "trick on the block 6, 7, 13, 14 too.",
              ["Write the block as a, a + 1, a + 7, a + 8. The sum is 4a + 16.",
               "So 4a + 16 = 36, which gives 4a = 20 and a is 5.",
               "The block is 5, 6, 12, 13. Check: 5 + 6 + 12 + 13 = 36.",
               "For 6, 7, 13, 14 the sum is 6 + 7 + 13 + 14 = 40, and 4 × 6 + 16 = 40 as well."],
              "The block is 5, 6, 12, 13",
              ncert=["6.4.calendar_sum", "6.4.calendar_algebra"])],
       key_terms=["calendar", "block", "expression"], misconceptions=["M_CAL_STEP"], minutes=10),
     A("T4.C2", "Make your own calendar trick", "Create",
       "Students choose a calendar block of a new shape, write its dates in terms of one letter, and use the sum to "
       "find the dates, creating their own calendar trick.",
       textbook=["Create your own calendar trick. For instance, choose a grid of a different size and shape.",
                 "The book shows blocks of other shapes on the August 2025 calendar and on a number grid with 10 "
                 "columns."],
       teach=["Predict first: for three dates one below the other, how far apart are they?",
              "Write every date in the shape in terms of the top one. Below is plus 7, to the right is plus 1.",
              "Add them to get an expression, then undo it to find the top date from the sum.",
              "On a grid with 10 columns the number below is plus 10 instead of plus 7."],
       examples=[
           WE("A friend picks three dates one below the other on a calendar page and says their sum is 51. Find the "
              "dates.",
              ["Call the top date a. The dates below it are a + 7 and a + 14.",
               "The sum is a + (a + 7) + (a + 14), which is 3a + 21.",
               "So 3a + 21 = 51, which gives 3a = 30 and a is 10.",
               "The dates are 10, 17 and 24. Check: 10 + 17 + 24 = 51."],
              "10, 17 and 24",
              ncert=["6.4.mt_calendar_own"])],
       key_terms=["calendar", "shape"], misconceptions=["M_CAL_STEP"], minutes=8),
     A("T4.C3", "Shapes that stand for numbers", "Apply",
       "Students read an algebra grid where shapes stand for numbers and each row ends in its sum, and find the "
       "value of each shape one row at a time.",
       textbook=["Algebra Grids",
                 "In the following grid, shapes represent numbers. In each row, the last column is the sum of the "
                 "values to its left. How do we find the values of the shapes?",
                 "Row 1: square, square, square, sum 27. Row 2: circle, circle, square, sum 19.",
                 "So, square = 9. Now, two circles and the square 9 make 19, so two circles make 10 and each circle is 5."],
       teach=["Predict first: which row can be solved on its own?",
              "A row made of one shape gives that shape at once: three squares make 27, so a square is 9.",
              "Put 9 in the next row and solve for the circle.",
              "Check every row with the values found."],
       examples=[
           WE("In a grid, three squares make 27 and two circles with a square make 19. Find the square and the circle.",
              ["Three equal squares make 27, so one square is 27 ÷ 3 = 9.",
               "Two circles and a square make 19, so two circles make 19 − 9 = 10.",
               "One circle is 10 ÷ 2 = 5.",
               "Check: 9 + 9 + 9 = 27 and 5 + 5 + 9 = 19."],
              "Square 9, circle 5",
              ncert=["6.4.grid_example"])],
       key_terms=["algebra grid", "shape", "sum"], misconceptions=["M_SHAPE_SAME"], minutes=8,
       tool="shape_grid"),
     DOER("T4.C4", "Practice: solve the algebra grids", "calendar_frame", "Apply",
          "Students find the values of the shapes in two algebra grids where no row has a single shape, and fill the "
          "empty sums.",
          ["Calendar block: a, a + 1, a + 7, a + 8, with sum 4a + 16.",
           "Algebra grid: write each row as an equation and combine rows to find each shape."],
          items=[
              FIO("6.4.grids_fill", "Fun with Grids: fill the algebra grids",
                  "In the following grids, find the values of the shapes and fill in the empty squares. Grid 1: "
                  "square, square, circle make 27; circle, circle, square make 21; circle, square, circle make a blank. "
                  "Grid 2: circle, diamond, diamond make 18; diamond, circle, circle make 15; diamond, circle, circle "
                  "make a blank; the last row is blank under every column.",
                  ["Grid 1: two squares and a circle make 27, two circles and a square make 21.",
                   "Adding both rows, three squares and three circles make 48, so a square and a circle make 16.",
                   "Take that from the first row: one square is 27 − 16 = 11, so a circle is 5. The last row is "
                   "5 + 11 + 5 = 21.",
                   "Grid 2: a circle and two diamonds make 18, two circles and a diamond make 15, so a circle and a "
                   "diamond make 33 ÷ 3 = 11.",
                   "One diamond is 18 − 11 = 7 and a circle is 4. The third row is 7 + 4 + 4 = 15.",
                   "Read the last row as column sums: 4 + 7 + 7 = 18, 7 + 4 + 4 = 15, 7 + 4 + 4 = 15, and the corner is "
                   "18 + 15 + 15 = 48."],
                  "Grid 1: square 11, circle 5, last row 21. Grid 2: circle 4, diamond 7, third row 15, column sums "
                  "18, 15, 15 and 48 in the corner")],
          misconceptions=["M_SHAPE_SAME", "M_CAL_STEP"])],
    key_terms=["calendar", "algebra grid", "expression"]))
