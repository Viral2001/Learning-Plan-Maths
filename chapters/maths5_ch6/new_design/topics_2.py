# -*- coding: utf-8 -*-
"""Topics T6, T7, T8 and T9 of Class 5 Chapter 6 (The Dairy Farm): Nearest Multiple and Using Strategies Flexibly
(module M2), Waste and Composting and Dairy Cooperative (module M3).
Every teaching concept has one worked example with the plan's own numbers; every book question is an FIO item of its
topic's DOER, in the book's order. The multi-part questions work every part with the method named in the question
(Nida's box, Kanti's lines, John's lines, Mili's father's carries)."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T6 Nearest Multiple ========================================================
TOPICS.append(TOPIC(
    "T6", "M2", "Nearest Multiple", ["Nearest Multiple"], "Apply",
    "Students find a product by rounding one number to the nearest multiple of 10, multiplying, and then taking away "
    "the strip that was counted by mistake or adding the strip that was left out.",
    "Round one number to the nearest multiple of 10 and multiply. Then fix the product: take away the strip you "
    "counted by mistake, or add the strip you left out.",
    [A("T6.C1", "Use a Friendly Number, Then Adjust", "Apply",
       "Students find a product by rounding one number to the nearest multiple of 10, multiplying, and then taking "
       "away the strip that was counted by mistake or adding the strip that was left out.",
       textbook=["Nearest Multiple"],
       teach=["Predict first: a tray has 6 rows of 19 squares. Is 6 × 20 more than, less than or the same as the "
              "number of squares in the tray?",
              "6 × 20 is easy, because 20 is a multiple of 10. But the tray has only 19 squares in each row, so "
              "6 × 20 counts one extra square in every row.",
              "There are 6 rows, so 6 extra squares were counted. Take them away: 6 × 19 = 6 × 20 − 6 = 120 − 6 = 114.",
              "Now the other way. A tray has 13 rows of 31 squares. 13 × 30 is easy, but it leaves out the 31st "
              "square of every row. There are 13 rows, so add 13: 13 × 31 = 13 × 30 + 13 = 390 + 13 = 403.",
              "If the friendly number is a little more than the number, take away. If it is a little less, add.",
              "Rule: round one number to the nearest multiple of 10, multiply, then take away the strip that was "
              "counted by mistake or add the strip that was left out."],
       examples=[WE("A tray has 6 rows with 19 squares in each row. Find 6 × 19 with the nearest multiple of 10. Then "
                    "find 13 × 31 the same way.",
                    ["The nearest multiple of 10 to 19 is 20. Multiply 6 × 20 = 120.",
                     "6 × 20 counts 20 squares in every row, but each row has only 19. One extra square is counted "
                     "in each of the 6 rows.",
                     "Take away the extra strip of 6 squares: 120 − 6 = 114.",
                     "So 6 × 19 = 6 × 20 − 6 = 120 − 6 = 114.",
                     "The nearest multiple of 10 to 31 is 30. Multiply 13 × 30 = 390.",
                     "13 × 30 leaves out the 31st square of every row, which is a strip of 13 squares. Add the "
                     "strip: 390 + 13 = 403.",
                     "So 13 × 31 = 13 × 30 + 13 = 390 + 13 = 403.",
                     "Check: 6 × 19 is 6 less than 6 × 20 = 120, so it is a little less than 120, and 114 is. "
                     "13 × 31 is 13 more than 13 × 30 = 390, so it is a little more than 390, and 403 is."],
                    "6 × 19 = 114 and 13 × 31 = 403")],
       ncert=["nm.intro"], key_terms=["nearest multiple", "friendly number", "adjust", "strip"],
       misconceptions=["M_NO_ADJUST"], minutes=6),
     DOER("T6.C2", "Practice: Nearest Multiple Grid", "nearest_multiple_grid", "Apply",
          "Students find products with the nearest multiple of 10, and explain from a picture of squares why they take "
          "away or add a strip to get the exact product.",
          ["Round one number to the nearest multiple of 10 and multiply.",
           "If you rounded up, the product counts extra squares: take them away.",
           "If you rounded down, the product leaves squares out: add them.",
           "The strip has one square in each row, so it is as long as the other number."],
          items=[FIO("ex.nm4", "Example 2: nearest multiple 4 × 19",
                     "Find 4 × 19 using the nearest multiple of 10. 4 × 19 = 4 × 20 − 4 = 80 − 4 = 76. Observe the "
                     "picture and find why we need to subtract 4.",
                     ["The nearest multiple of 10 to 19 is 20, so use 4 × 20 = 80.",
                      "Look at the picture. It has 4 rows of 20 squares, and the last square of every row is white.",
                      "Only 19 squares in each row are real, so 4 × 20 counts one extra square in every row.",
                      "There are 4 rows, so 4 squares were counted by mistake. That is why we subtract 4.",
                      "80 − 4 = 76, so 4 × 19 = 76.",
                      "Check: 4 × 19 = 4 × 10 + 4 × 9 = 40 + 36 = 76."],
                     "We subtract 4 because 4 × 20 counts one extra square in each of the 4 rows. 4 × 19 = 76.",
                     kind="example",
                     q_figure="An arrangement of 4 rows of 20 squares in which the 19 squares of each row are shaded and "
                              "the last square of each row is white, with a note: Observe the picture and find why we "
                              "need to subtract 4.",
                     s_figure="The same 4 rows of 20 squares with the 4 white squares of the last column marked as the "
                              "extra squares, and the sentence 4 × 19 = 80 − 4 = 76 below the picture."),
                 FIO("ex.nm14", "Example 3: nearest multiple 14 × 21",
                     "Find 14 × 21 using the nearest multiple of 10. 14 × 21 = 14 × 20 + 14 = 280 + 14 = 294. Observe "
                     "the picture and find why we need to add 14.",
                     ["The nearest multiple of 10 to 21 is 20, so use 14 × 20 = 280.",
                      "Look at the picture. It has 14 rows of 21 squares. The first 20 squares of every row are yellow "
                      "and the last square is green.",
                      "14 × 20 counts only the yellow squares. The green column of 14 squares, one in each of the 14 "
                      "rows, was left out.",
                      "Add the green column. That is why we add 14.",
                      "280 + 14 = 294, so 14 × 21 = 294.",
                      "Check: 14 × 21 = 14 × 20 + 14 × 1 = 280 + 14 = 294."],
                     "We add 14 because 14 × 20 leaves out the green column of 14 squares. 14 × 21 = 294.",
                     kind="example",
                     q_figure="An arrangement of 14 rows of 21 squares in which the first 20 columns are yellow and the "
                              "last column of 14 squares is green, with a note: Observe the picture and find why we "
                              "need to add 14.",
                     s_figure="The same 14 rows of 21 squares with the green column of 14 squares outlined as the squares "
                              "that were left out, and the sentence 14 × 21 = 280 + 14 = 294 below the picture."),
                 FIO("nm.c", "Nearest Multiple: Q(c) your own examples",
                     "Give 5 examples of problems where you can use the nearest multiple to find the product easily. "
                     "Find the products as well.",
                     ["Choose a number just below or just above a multiple of 10, and any other number to multiply it "
                      "with.",
                      "6 × 29: 29 is 1 less than 30. 6 × 30 = 180, then take away 6: 180 − 6 = 174.",
                      "5 × 41: 41 is 1 more than 40. 5 × 40 = 200, then add 5: 200 + 5 = 205.",
                      "13 × 19: 19 is 1 less than 20. 13 × 20 = 260, then take away 13: 260 − 13 = 247.",
                      "9 × 31: 31 is 1 more than 30. 9 × 30 = 270, then add 9: 270 + 9 = 279.",
                      "8 × 99: 99 is 1 less than 100. 8 × 100 = 800, then take away 8: 800 − 8 = 792.",
                      "Check: when we took away, the answer is a little less than the rounded product: 174 is less than "
                      "180, 247 is less than 260, 792 is less than 800. When we added, it is a little more: 205 is more "
                      "than 200 and 279 is more than 270."],
                     "Sample answer: 6 × 29 = 174; 5 × 41 = 205; 13 × 19 = 247; 9 × 31 = 279; 8 × 99 = 792. Your "
                     "answer may differ.",
                     kind="prompt"),
                 FIO("nm.d", "Nearest Multiple: Q(d) nearest multiple",
                     "Find the products of the following numbers by finding the nearest multiple. (1): 7 × 52 (2): "
                     "12 × 28 (3): 75 × 31 (4): 99 × 15 (5): 8 × 25 (6): 22 × 42",
                     ["(1): 7 × 52. The nearest multiple of 10 to 52 is 50, so 7 × 50 = 350.",
                      "(1): the strip is 2 squares in each row, 7 × 2 = 14. Add it: 350 + 14 = 364.",
                      "(2): 12 × 28. The nearest multiple of 10 to 28 is 30, so 12 × 30 = 360.",
                      "(2): the strip is 2 squares in each row, 12 × 2 = 24. Take it away: 360 − 24 = 336.",
                      "(3): 75 × 31. The nearest multiple of 10 to 31 is 30, so 75 × 30 = 2,250.",
                      "(3): the strip is 1 square in each row, so add 75: 2,250 + 75 = 2,325.",
                      "(4): 99 × 15. The nearest multiple of 10 to 99 is 100, so 100 × 15 = 1,500.",
                      "(4): the strip is 15 squares, so take it away: 1,500 − 15 = 1,485.",
                      "(5): 8 × 25. 25 is as far from 20 as from 30, so use 30: 8 × 30 = 240.",
                      "(5): the strip is 5 squares in each row, 8 × 5 = 40. Take it away: 240 − 40 = 200.",
                      "(6): 22 × 42. The nearest multiple of 10 to 42 is 40, so 22 × 40 = 880.",
                      "(6): the strip is 2 squares in each row, 22 × 2 = 44. Add it: 880 + 44 = 924.",
                      "Check with a rough product: 364 is a little more than 7 × 50 = 350, 336 is a little less than "
                      "12 × 30 = 360, 2,325 is a little more than 75 × 30 = 2,250, 1,485 is a little less than "
                      "100 × 15 = 1,500, 200 is between 8 × 20 = 160 and 8 × 30 = 240, and 924 is a little more than "
                      "22 × 40 = 880."],
                     "(1): 364; (2): 336; (3): 2,325; (4): 1,485; (5): 200; (6): 924")],
          misconceptions=["M_NO_ADJUST"])],
    key_terms=["nearest multiple", "friendly number", "strip"]))

# ============================== T7 Using Strategies Flexibly ===============================================
TOPICS.append(TOPIC(
    "T7", "M2", "Using Strategies Flexibly", ["Let Us Solve (using strategies flexibly)"], "Apply",
    "Students look at the numbers of a problem, choose the easy way to multiply, and solve word problems with halving "
    "and doubling, the nearest multiple or a split.",
    "Before you multiply, look at the numbers. Halve and double for a 5, 25 or 50, use the nearest multiple for a "
    "number close to a ten, and split a number in the other cases. Read the story to decide which numbers to "
    "multiply.",
    [A("T7.C1", "Choose the Easy Way", "Apply",
       "Students choose the easy way to multiply by looking at the numbers first, then use halving and doubling, the "
       "nearest multiple or a split to find the product.",
       teach=["Predict first: you need 50 × 34. Would you split a number, use the nearest multiple of 10, or halve and "
              "double?",
              "Look at the numbers before you start. A 5, 25 or 50 means halve and double: 50 × 34 = 100 × 17 = "
              "1,700.",
              "A number just below or just above a multiple of 10, like 39 or 41, means the nearest multiple: "
              "8 × 39 = 8 × 40 − 8 = 312.",
              "With any other numbers, split one number into parts, multiply each part and add: 18 × 26 = "
              "18 × 20 + 18 × 6 = 360 + 108 = 468.",
              "Say how you chose. Different ways give the same product, so you can check one way with another.",
              "Rule: look at the numbers first, then choose the strategy that gives the shortest work."],
       examples=[WE("A dairy packs butter packets. 50 boxes hold 34 packets each. 8 trays hold 39 packets each. "
                    "18 crates hold 26 packets each. Find each total and say why you chose that way.",
                    ["50 × 34: the 50 is a friendly number, so halve and double. Halve 34 to get 17 and double 50 to "
                     "get 100.",
                     "100 × 17 = 1,700, so 50 × 34 = 1,700 packets.",
                     "8 × 39: 39 is just below 40, so use the nearest multiple. 8 × 40 = 320.",
                     "The strip is 8 packets too many: 320 − 8 = 312, so 8 × 39 = 312 packets.",
                     "18 × 26: no number is friendly, so split 26 into 20 + 6. 18 × 20 = 360.",
                     "18 × 6 = 108.",
                     "360 + 108 = 468, so 18 × 26 = 468 packets.",
                     "Check with rough products: 50 × 34 is near 50 × 35 = 1,750, 8 × 39 is near 8 × 40 = 320, and "
                     "18 × 26 is near 20 × 25 = 500. The answers 1,700, 312 and 468 are close."],
                    "50 × 34 = 1,700, 8 × 39 = 312 and 18 × 26 = 468")],
       key_terms=["easy way", "strategy", "choose", "numbers"],
       misconceptions=["M_HALVE_BOTH", "M_NO_ADJUST"], minutes=6),
     DOER("T7.C2", "Practice: Choose a Strategy", None, "Apply",
          "Students solve word problems by choosing a strategy that fits the numbers, and explain why that strategy "
          "makes the work short.",
          ["Look at the numbers first: a 5, 25 or 50 means halve and double.",
           "A number just below or just above a multiple of 10 means the nearest multiple.",
           "With other numbers, split one number into parts and add.",
           "Read the story and decide which numbers to multiply. Do not multiply every pair of numbers."],
          items=[FIO("ls1.q1", "Let Us Solve: Q1 auditorium",
                     "Use strategies flexibly to answer the following questions. Discuss your thoughts in class. A "
                     "school has an auditorium with 35 rows, with 42 seats in each row. How many people can sit in this "
                     "auditorium?",
                     ["Each row has 42 seats and there are 35 rows, so multiply 35 × 42.",
                      "The numbers are not friendly, so split 42 into 40 + 2.",
                      "35 × 40 = 1,400.",
                      "35 × 2 = 70.",
                      "1,400 + 70 = 1,470.",
                      "Check with another way: double 35 and halve 42, and 70 × 21 = 1,470. Both ways agree."],
                     "1,470 people can sit in the auditorium."),
                 FIO("ls1.q2", "Let Us Solve: Q2 Priya jogs",
                     "Priya jogs 4 kilometres every day. How many kilometers will she jog in 31 days?",
                     ["She jogs 4 kilometres each day for 31 days, so multiply 4 × 31.",
                      "31 is just above 30, so use the nearest multiple. 4 × 30 = 120.",
                      "One more day is 4 more kilometres: 120 + 4 = 124.",
                      "Check: 124 is a little more than 4 × 30 = 120, which is right because 31 is a little more than "
                      "30."],
                     "Priya will jog 124 kilometres in 31 days."),
                 FIO("ls1.q3", "Let Us Solve: Q3 boxes of books",
                     "A school has received 36 boxes of books with 48 books in each box. How many total books did the "
                     "school receive in the boxes?",
                     ["There are 36 boxes with 48 books in each box, so multiply 36 × 48.",
                      "48 is just below 50, so use the nearest multiple. 36 × 50 = 1,800.",
                      "The strip is 2 books in each box, 36 × 2 = 72. Take it away.",
                      "1,800 − 72 = 1,728.",
                      "Check with another way: split 36 into 30 + 6. 30 × 48 = 1,440 and 6 × 48 = 288, and "
                      "1,440 + 288 = 1,728."],
                     "The school received 1,728 books."),
                 FIO("ls1.q4", "Let Us Solve: Q4 kurtas",
                     "Priya uses 16 metres of cloth to make 4 kurtas. How much cloth would she need to make 8 kurtas?",
                     ["4 kurtas need 16 metres of cloth.",
                      "8 kurtas are double 4 kurtas, because 4 × 2 = 8.",
                      "Twice the kurtas need twice the cloth, so double 16: 16 × 2 = 32.",
                      "Do not multiply every pair of numbers. The cloth for 4 kurtas is already 16 metres.",
                      "Check: 4 kurtas need 16 metres, and 4 × 4 = 16, so each kurta needs 4 metres. Then 8 kurtas need "
                      "8 × 4 = 32 metres."],
                     "Priya needs 32 metres of cloth."),
                 FIO("ls1.q5", "Let Us Solve: Q5 Gollappa's cows",
                     "Gollappa has 29 cows on his farm. Each cow produces 5 litres of milk per day. How many litres of "
                     "milk do the cow produce in total, each day?",
                     ["There are 29 cows and each gives 5 litres, so multiply 29 × 5.",
                      "29 is just below 30, so use the nearest multiple. 30 × 5 = 150.",
                      "That counts one cow too many. Take away the milk of one cow, 5 litres: 150 − 5 = 145.",
                      "Check with halving: 5 is half of 10, and 29 × 10 = 290. Half of 290 is 145."],
                     "The cows give 145 litres of milk each day."),
                 FIO("ls1.q6", "Let Us Solve: Q6 Maska Cow Farm",
                     "Maska Cow Farm has 297 cows. Each cow requires 18 kg of fodder per day. How much total fodder is "
                     "needed to feed 297 cows every day?",
                     ["There are 297 cows and each needs 18 kg, so multiply 297 × 18.",
                      "297 is just below 300, so use the nearest multiple. 300 × 18 = 5,400.",
                      "That counts 3 cows too many. Take away the fodder of 3 cows: 3 × 18 = 54.",
                      "5,400 − 54 = 5,346.",
                      "Check with another way: 297 × 18 = 297 × 20 − 297 × 2 = 5,940 − 594 = 5,346."],
                     "5,346 kg of fodder is needed each day.")],
          misconceptions=["M_MULT_ALL", "M_NO_ADJUST"])],
    key_terms=["strategy", "easy way", "numbers"]))

# ============================== T8 Waste and Composting ====================================================
TOPICS.append(TOPIC(
    "T8", "M3", "Waste and Composting",
    ["Waste and Composting", "Let Us Multiply", "Let Us Do (box and lines)"], "Apply",
    "Students split both numbers into tens and ones, find the small products in a box, and write the same products in "
    "Kanti's four lines and John's two lines to multiply two numbers.",
    "Split both numbers into tens and ones. The small products can sit in a box, in Kanti's four lines or in John's two "
    "lines. Add them to get the product, and keep the zeros: 10 × 20 is 200.",
    [A("T8.C1", "The Box Method", "Apply",
       "Students split both numbers into tens and ones, find the four small products in a box, and add them to get the "
       "product of two numbers.",
       textbook=["Waste and Composting"],
       teach=["Predict first: you split both numbers of 23 × 14 into tens and ones, 20 + 3 and 10 + 4. How many small "
              "products do you need to multiply?",
              "Four. Every part of 23 is multiplied by every part of 14.",
              "Draw a box. Write the parts of 23 along the top, 20 and 3. Write the parts of 14 down the side, 10 and 4.",
              "Each cell holds one small product: 10 × 20 = 200, 10 × 3 = 30, 4 × 20 = 80 and 4 × 3 = 12.",
              "Add each column first: 200 + 80 = 280 and 30 + 12 = 42. Then add the two sums: 280 + 42 = 322.",
              "Mind the zeros: 10 × 20 is 200, not 20, because 1 ten times 2 tens is 2 hundreds.",
              "Rule: split both numbers, multiply the parts in a box, then add the column sums."],
       examples=[WE("A dairy shed has 14 shelves with 23 ghee jars on each shelf. Use a box to find 23 × 14.",
                    ["Split 23 into 20 + 3 and 14 into 10 + 4.",
                     "Draw a box with 20 and 3 along the top and 10 and 4 down the side.",
                     "The row of 10: 10 × 20 = 200 and 10 × 3 = 30.",
                     "The row of 4: 4 × 20 = 80 and 4 × 3 = 12.",
                     "Add the column of 20: 200 + 80 = 280. Add the column of 3: 30 + 12 = 42.",
                     "Add the column sums: 280 + 42 = 322.",
                     "Check: 23 × 14 is near 20 × 15 = 300, and 322 is close."],
                    "23 × 14 = 322")],
       key_terms=["box", "tens", "ones", "small products"],
       misconceptions=["M_ZERO_COUNT", "M_SPLIT_ONE"], minutes=6),
     A("T8.C2", "Write the Parts in Lines", "Apply",
       "Students write the same small products in Kanti's four lines and John's two lines, and explain how the box and "
       "the lines are the same and different.",
       textbook=["Kanti and John tried to solve it in the following ways.",
                 "How are these solutions same or different? Discuss in class."],
       teach=["Predict first: the box for 26 × 13 holds four small products. If you write them in lines instead of "
              "cells, how many lines do you need?",
              "Kanti writes every small product on its own line, so she needs four lines. Her lines for 26 × 13 are "
              "18 (3 × 6), 60 (3 × 20), 60 (10 × 6) and 200 (10 × 20). Add them: 18 + 60 + 60 + 200 = 338.",
              "John joins two small products in each line. 3 × 26 = 18 + 60 = 78 and 10 × 26 = 60 + 200 = 260. Add "
              "the two lines: 78 + 260 = 338.",
              "The box, Kanti's four lines and John's two lines use the same four small products: 18, 60, 60 and 200. "
              "Only the layout is different.",
              "John's way has the fewest lines. Each of his lines multiplies the whole 26 by one part of 13.",
              "In every layout keep the place value of each product: 10 × 20 is 200, not 20.",
              "Rule: the same small products can sit in a box, in four lines or in two lines. The answer does not "
              "change."],
       examples=[WE("A dairy packs 13 trays with 26 butter packets in each tray. Find 26 × 13 with Kanti's four lines, "
                    "and then with John's two lines.",
                    ["Split 26 into 20 + 6 and 13 into 10 + 3.",
                     "Kanti's lines, the ones of 13 first: 3 × 6 = 18 and 3 × 20 = 60.",
                     "Then the tens of 13: 10 × 6 = 60 and 10 × 20 = 200.",
                     "Add the four lines: 18 + 60 + 60 + 200 = 338.",
                     "John's first line joins 18 and 60: 3 × 26 = 18 + 60 = 78.",
                     "John's second line joins 60 and 200: 10 × 26 = 60 + 200 = 260.",
                     "Add the two lines: 78 + 260 = 338.",
                     "Check: 25 × 13 = 325, and one more 13 makes 325 + 13 = 338."],
                    "26 × 13 = 338, with Kanti's four lines and with John's two lines")],
       ncert=["wc.same", "wc.note"], key_terms=["lines", "four lines", "two lines", "same products"],
       misconceptions=["M_MISSING_ZERO", "M_SPLIT_ONE"], minutes=7),
     DOER("T8.C3", "Practice: Box and Lines", "box_and_lines", "Apply",
          "Students solve multiplication problems by splitting both numbers, filling a box, and writing Kanti's four "
          "lines or John's two lines, and check each answer with an estimate.",
          ["Split both numbers into tens and ones, and fill the box with the small products.",
           "Kanti writes each small product on its own line. John joins them into two lines.",
           "Keep the zeros: 10 × 20 is 200.",
           "Add the column sums or the lines to get the total."],
          items=[FIO("ex.wc12", "Example 4: kitchen waste in a year",
                     "A family of 4 produces around 35 kg of kitchen waste in a month. How much waste will the family "
                     "produce in a year? Quantity of kitchen waste in 1 month is 35 kg. Quantity of kitchen waste in 12 "
                     "months is 12 × 35 kg. The family produces ___ kg of waste in a year.",
                     ["The waste in a year is 12 months of 35 kg each, so 12 × 35 kg.",
                      "Nida's box: split 12 into 10 + 2 and 35 into 30 + 5.",
                      "The cells: 10 × 30 = 300, 10 × 5 = 50, 2 × 30 = 60 and 2 × 5 = 10.",
                      "Column sums: 300 + 60 = 360 and 50 + 10 = 60.",
                      "Total: 360 + 60 = 420.",
                      "Kanti's four lines: 10 (2 × 5), 60 (2 × 30), 50 (10 × 5) and 300 (10 × 30). Add them: "
                      "10 + 60 + 50 + 300 = 420.",
                      "John's two lines: 60 + 10 = 70 (2 × 35) and 300 + 50 = 350 (10 × 35). Add them: 70 + 350 = 420.",
                      "All three ways use the same four small products. John's way has the fewest lines.",
                      "Check: 12 × 35 = 12 × 30 + 12 × 5 = 360 + 60 = 420."],
                     "The family produces 420 kg of waste in a year.",
                     kind="example",
                     q_figure="A woman pours kitchen waste into a compost pit. Beside it are 12 rows of place value tags: "
                              "every row has three blue tags marked 10 and five pink tags marked 1. The first 10 rows "
                              "are inside one dashed box and the last 2 rows inside another.",
                     s_figure="Nida's box with columns 30 kg and 5 kg and rows 10 and 2, the cells 300, 50, 60 and 10, the "
                              "column sums 360 and 60 and the total 420, with Kanti's four lines and John's two lines "
                              "beside it."),
                 FIO("ex.compost", "Example 5: compost savings",
                     "The family regularly composts the collected waste. They get around 150 kg of compost each year, "
                     "which they use in their garden. 1 kg of compost is often sold in the market at ₹24. By creating "
                     "their own compost, how much money have they saved in a year? Savings on 1 kg compost is ₹24. "
                     "Savings on 150 kg will be ₹24 × 150.",
                     ["The savings on 150 kg are ₹24 for every 1 kg, so ₹24 × 150.",
                      "Nida's box: split 24 into 20 + 4 and 150 into 100 + 50.",
                      "The cells: 20 × 100 = 2,000, 20 × 50 = 1,000, 4 × 100 = 400 and 4 × 50 = 200.",
                      "Column sums: 2,000 + 400 = 2,400 and 1,000 + 200 = 1,200.",
                      "Total: 2,400 + 1,200 = 3,600.",
                      "Kanti's four lines: 200 (4 × 50), 400 (4 × 100), 1,000 (20 × 50) and 2,000 (20 × 100). Add them: "
                      "200 + 400 + 1,000 + 2,000 = 3,600.",
                      "John's two lines: 400 + 200 + 0 = 600 (4 × 150) and 2,000 + 1,000 + 0 = 3,000 (20 × 150). Add "
                      "them: 600 + 3,000 = 3,600.",
                      "The three ways have the same small products. The 0 in each of John's lines is the 0 of 150.",
                      "Check: 24 × 150 = 24 × 100 + 24 × 50 = 2,400 + 1,200 = 3,600."],
                     "The family saves ₹3,600 in a year.",
                     kind="example",
                     q_figure="A heap of compost on a wooden board with a price tag marked ₹24 for 1 kg and a label 150 kg.",
                     s_figure="Nida's box with columns 100 and 50 and rows 20 and 4, the cells 2,000, 1,000, 400 and 200, "
                              "the column sums 2,400 and 1,200 and the total 3,600."),
                 FIO("lm.a", "Let Us Multiply: (a) 32 × 8",
                     "Let Us Multiply. 32 × 8. Fill the box with columns 30 and 2 and row 8, then complete the line "
                     "methods: 32 (30 + 2) × 8: ___ (8 × 2), ___0 (8 × 30), total 256; and John's way: ___0 + 16 gives "
                     "256.",
                     ["The box has the columns 30 and 2 and the row 8.",
                      "Fill the cells: 8 × 30 = 240 and 8 × 2 = 16.",
                      "Add the cells: 240 + 16 = 256.",
                      "Kanti's lines: the first blank is 8 × 2 = 16.",
                      "The second line is 8 × 30 = 240. The blank before the 0 is 24, because 8 × 3 tens is 24 tens.",
                      "Add the lines: 16 + 240 = 256.",
                      "John's way: 8 × 30 = 240 is the line ___0, so the blank is 24, and 240 + 16 = 256.",
                      "Check by halving and doubling: 32 × 8 = 16 × 16 = 256."],
                     "Box cells 240 and 16. The blanks are 16, 24 and 24. Total 256.",
                     q_figure="A box with columns 30 and 2, one row 8 and empty cells, and below it two line forms with "
                              "blanks: Kanti's lines and John's line.",
                     s_figure="The box with the cells 240 and 16 and the total 256, and the two line forms with the blanks "
                              "filled: 16, 240 and the total 256."),
                 FIO("lm.b", "Let Us Multiply: (b) 69 × 45",
                     "Let Us Multiply. 69 × 45. Fill the box with columns 60 and 9 and rows 40 and 5 (the column sums "
                     "2,700 and 405 and the total 3,105 are already filled in), then complete the lines: 69 (60 + 9) × "
                     "45 (40 + 5): 45 (5 × 9), ___0 (5 × 60), ___0 (40 × 9), ___00 (40 × 60), total 3,105; and John's "
                     "way: 300 + ___ = 345 (5 × 69), ___ + ___ = 2,760 (40 × 69), total 3,105.",
                     ["The box has the columns 60 and 9 and the rows 40 and 5.",
                      "The row of 40: 40 × 60 = 2,400 and 40 × 9 = 360.",
                      "The row of 5: 5 × 60 = 300 and 5 × 9 = 45.",
                      "Column sums: 2,400 + 300 = 2,700 and 360 + 45 = 405. They match the box.",
                      "Total: 2,700 + 405 = 3,105.",
                      "Kanti's lines: 45 is 5 × 9. 5 × 60 = 300, so the blank before the 0 is 30.",
                      "40 × 9 = 360, so the blank before the 0 is 36. 40 × 60 = 2,400, so the blank before the 00 is 24.",
                      "Add the four lines: 45 + 300 + 360 + 2,400 = 3,105.",
                      "John's way: 5 × 69 = 300 + 45 = 345, so the blank is 45.",
                      "40 × 69 = 2,400 + 360 = 2,760, so the two blanks are 2,400 and 360.",
                      "Add the two lines: 345 + 2,760 = 3,105.",
                      "Check: 70 × 45 = 3,150, and 69 × 45 is one 45 less: 3,150 − 45 = 3,105."],
                     "Kanti: 30, 36, 24. John: 45; 2,400 and 360. Total 3,105.",
                     q_figure="A box with columns 60 and 9 and rows 40 and 5. The column sums 2,700 and 405 and the total "
                              "3,105 are filled in and the four cells are empty. Beside it, two line forms with blanks: "
                              "Kanti's lines and John's lines.",
                     s_figure="The box with the cells 2,400, 360, 300 and 45, the column sums 2,700 and 405 and the total "
                              "3,105."),
                 FIO("ld1.q1", "Let Us Do, Q1 like Nida",
                     "Solve the following problems like Nida did. (a): 78 × 4 (b): 83 × 9 (c): 67 × 28 (d): 53 × 37",
                     ["(a): 78 = 70 + 8, and 4 is the row. The cells: 70 × 4 = 280 and 8 × 4 = 32.",
                      "(a): add the cells: 280 + 32 = 312.",
                      "(b): 83 = 80 + 3, and 9 is the row. The cells: 80 × 9 = 720 and 3 × 9 = 27.",
                      "(b): add the cells: 720 + 27 = 747.",
                      "(c): 67 = 60 + 7 and 28 = 20 + 8. The cells: 60 × 20 = 1,200, 7 × 20 = 140, 60 × 8 = 480 and "
                      "7 × 8 = 56.",
                      "(c): column sums: 1,200 + 480 = 1,680 for the 60 and 140 + 56 = 196 for the 7.",
                      "(c): total: 1,680 + 196 = 1,876.",
                      "(d): 53 = 50 + 3 and 37 = 30 + 7. The cells: 50 × 30 = 1,500, 3 × 30 = 90, 50 × 7 = 350 and "
                      "3 × 7 = 21.",
                      "(d): column sums: 1,500 + 350 = 1,850 for the 50 and 90 + 21 = 111 for the 3.",
                      "(d): total: 1,850 + 111 = 1,961.",
                      "Check the ones digits: 8 × 4 = 32 ends in 2, 3 × 9 = 27 ends in 7, 7 × 8 = 56 ends in 6 and "
                      "3 × 7 = 21 ends in 1, like 312, 747, 1,876 and 1,961."],
                     "(a): 312; (b): 747; (c): 1,876; (d): 1,961",
                     q_figure="Four empty boxes drawn as tables, one for each problem. The boxes of (a) and (b) have 2 "
                              "columns and 1 row, the boxes of (c) and (d) have 2 columns and 2 rows, and each has a "
                              "bottom row for the sums and the total.",
                     s_figure="The four boxes filled in, with the totals 312, 747, 1,876 and 1,961 in the bottom rows."),
                 FIO("ld1.q2", "Let Us Do, Q2 like Kanti",
                     "Solve the following problems like Kanti. (a): 94 × 5 (b): 49 × 6 (c): 37 × 53 (d): 28 × 79",
                     ["(a): 94 (90 + 4) × 5. The lines: 20 (5 × 4) and 450 (5 × 90).",
                      "(a): add the lines: 20 + 450 = 470.",
                      "(b): 49 (40 + 9) × 6. The lines: 54 (6 × 9) and 240 (6 × 40).",
                      "(b): add the lines: 54 + 240 = 294.",
                      "(c): 37 (30 + 7) × 53 (50 + 3). The lines: 21 (3 × 7), 90 (3 × 30), 350 (50 × 7) and "
                      "1,500 (50 × 30).",
                      "(c): add the lines: 21 + 90 + 350 + 1,500 = 1,961.",
                      "(d): 28 (20 + 8) × 79 (70 + 9). The lines: 72 (9 × 8), 180 (9 × 20), 560 (70 × 8) and "
                      "1,400 (70 × 20).",
                      "(d): add the lines: 72 + 180 + 560 + 1,400 = 2,212.",
                      "Check with rough products: 95 × 5 = 475 is near 470, 50 × 6 = 300 is near 294, 40 × 50 = 2,000 "
                      "is near 1,961 and 28 × 80 = 2,240 is near 2,212."],
                     "(a): 470; (b): 294; (c): 1,961; (d): 2,212"),
                 FIO("ld1.q3", "Let Us Do, Q3 like John",
                     "Solve the following problems like John. (a): 86 × 3 (b): 72 × 7 (c): 94 × 36 (d): 66 × 22",
                     ["(a): 86 (80 + 6) × 3. One line: 240 + 18 = 258 (3 × 86).",
                      "(b): 72 (70 + 2) × 7. One line: 490 + 14 = 504 (7 × 72).",
                      "(c): 94 (90 + 4) × 36 (30 + 6). First line: 24 + 540 = 564 (6 × 94). Second line: "
                      "120 + 2,700 = 2,820 (30 × 94).",
                      "(c): add the two lines: 564 + 2,820 = 3,384.",
                      "(d): 66 (60 + 6) × 22 (20 + 2). First line: 12 + 120 = 132 (2 × 66). Second line: "
                      "120 + 1,200 = 1,320 (20 × 66).",
                      "(d): add the two lines: 132 + 1,320 = 1,452.",
                      "Check with rough products: 85 × 3 = 255 is near 258, 70 × 7 = 490 is near 504, 95 × 36 = 3,420 "
                      "is near 3,384 and 65 × 22 = 1,430 is near 1,452."],
                     "(a): 258; (b): 504; (c): 3,384; (d): 1,452"),
                 FIO("ld1.q4a", "Let Us Do, Q4 (a) cinema",
                     "A movie theater has 8 rows of seats, and each row has 12 seats. If half the seats are filled, how "
                     "many people are watching the movie? If 3 more rows get filled, how many total people will be "
                     "there?",
                     ["The movie theater has 8 rows with 12 seats in each row, so 8 × 12 seats.",
                      "Split 12 into 10 + 2. 8 × 10 = 80 and 8 × 2 = 16, and 80 + 16 = 96 seats.",
                      "Half the seats are filled. Half of 96 is 48, because 48 + 48 = 96. So 48 people are watching.",
                      "3 more rows get filled and each row has 12 seats, so 3 × 12 = 36 more people.",
                      "Your maths book does not say where the first 48 people sit, so we read it this way: the 3 more "
                      "rows are full rows of 12 new people.",
                      "Total people: 48 + 36 = 84.",
                      "Check: 84 is less than the 96 seats, so everyone has a seat."],
                     "48 people are watching. With 3 more rows filled there are 84 people.",
                     q_figure="A cinema hall with rows of seats in front of a screen.",
                     s_figure="A seating plan of 8 rows of 12 seats with 48 seats marked, and then 3 more full rows of 12 "
                              "seats marked."),
                 FIO("ld1.q4b", "Let Us Do, Q4 (b) cricket",
                     "In a test match between India and West Indies, the Indian team hit twenty-four fours and eighteen "
                     "sixes across the two innings. How many runs were scored in fours and sixes each? 234 runs were made by "
                     "running between the wickets. If 23 runs were extras, how many runs were scored by Indian team in "
                     "the two innings?",
                     ["Each four is worth 4 runs. Runs from fours: 24 × 4 = 96.",
                      "Each six is worth 6 runs. Runs from sixes: 18 × 6 = 108.",
                      "Runs made by running between the wickets: 234. Extras: 23.",
                      "Total runs: 96 + 108 + 234 + 23 = 461.",
                      "A team's score includes the extras, so the 23 extras are added.",
                      "Check: 96 + 108 = 204, then 204 + 234 = 438, then 438 + 23 = 461."],
                     "96 runs from fours and 108 runs from sixes. The team scored 461 runs."),
                 FIO("ld1.q4c", "Let Us Do, Q4 (c) bulbs and tube lights",
                     "Anjali buys 15 bulbs and 12 tube lights from Sudha Electricals. Each bulb costs ₹25 and each tube "
                     "light costs ₹34. How much money should Anjali give to the shopkeeper?",
                     ["The 15 bulbs cost 15 × 25. Split 15 into 10 + 5: 10 × 25 = 250 and 5 × 25 = 125.",
                      "250 + 125 = 375, so the bulbs cost ₹375.",
                      "The 12 tube lights cost 12 × 34. Split 12 into 10 + 2: 10 × 34 = 340 and 2 × 34 = 68.",
                      "340 + 68 = 408, so the tube lights cost ₹408.",
                      "Money to give: 375 + 408 = 783.",
                      "Check: 12 × 34 = 6 × 68 = 408 by halving and doubling, and 15 × 25 = 3 × 5 × 25 = 3 × 125 = "
                      "375."],
                     "Anjali should give ₹783 to the shopkeeper."),
                 FIO("ld1.q4d", "Let Us Do, Q4 (d) rice bags",
                     "A shopkeeper sold 28 bags of rice. Each bag costs ₹350. How much money did he earn by selling "
                     "rice bags?",
                     ["28 bags at ₹350 each give 28 × 350.",
                      "Split 350 into 300 + 50.",
                      "28 × 300 = 8,400.",
                      "28 × 50 = 1,400.",
                      "8,400 + 1,400 = 9,800.",
                      "Check: 28 × 35 = 980, and 28 × 350 is 10 times as much: 980 × 10 = 9,800."],
                     "He earned ₹9,800."),
                 FIO("ld1.q4e", "Let Us Do, Q4 (e) library",
                     "A school library has 86 shelves and each shelf has 162 books. Find the number of books in the "
                     "library.",
                     ["86 shelves with 162 books on each shelf give 86 × 162.",
                      "Split 162 into 100 + 60 + 2.",
                      "86 × 100 = 8,600.",
                      "86 × 60 = 5,160.",
                      "86 × 2 = 172.",
                      "8,600 + 5,160 + 172 = 13,932.",
                      "Check: 86 × 162 is near 90 × 160 = 14,400, and 13,932 is a little less."],
                     "The library has 13,932 books.")],
          misconceptions=["M_MISSING_ZERO", "M_ZERO_COUNT", "M_SPLIT_ONE"])],
    key_terms=["box", "lines", "tens and ones", "small products"]))

# ============================== T9 Dairy Cooperative =======================================================
TOPICS.append(TOPIC(
    "T9", "M3", "Dairy Cooperative", ["Dairy Cooperative", "Let Us Solve (large numbers)"], "Apply",
    "Students multiply large numbers place by place, write each carry above the next place, and add the carry after "
    "multiplying that place, for one-digit, two-digit and three-digit multipliers.",
    "Multiply place by place from the ones. Write the carry above the next place and add it after multiplying that "
    "place. For a two-digit or three-digit multiplier, write one row for each digit, with a 0 or 00 at the end of the "
    "tens and hundreds rows, and add the rows.",
    [A("T9.C1", "Multiply Place by Place", "Apply",
       "Students multiply a three-digit number by a one-digit number place by place, keeping the place value of each "
       "product, and add the products.",
       textbook=["Remember! 4 × 6 Tens = 24 Tens = 240; 4 × 2 Hundreds = 8 Hundreds = 800",
                 "Mili says her father has taught her to use place values of digits to multiply large numbers.",
                 "Many women dairy entrepreneurs are playing significant role in the dairy sector. Jamanaben Maganbhai "
                 "Naku of village Tuked in Surat possesses 27 Gir cows and rears the cows through Low-cost Farm "
                 "Investment."],
       teach=["Predict first: to find 235 × 4 you split 235 into hundreds, tens and ones. What is 4 × 3 tens, and how do "
              "you write it as a number?",
              "Mili says her father taught her to use the place value of every digit.",
              "Split 235 into 200 + 30 + 5. Multiply each part by 4: 4 × 5 = 20, 4 × 30 = 120 and 4 × 200 = 800.",
              "Remember: 4 × 3 tens is 12 tens, and 12 tens is 120. 4 × 2 hundreds is 8 hundreds, and 8 hundreds is "
              "800.",
              "Add the three products: 20 + 120 + 800 = 940.",
              "Rule: multiply the ones, then the tens, then the hundreds, keep the place value of each product, and add."],
       examples=[WE("A packing hall fills 4 trays with 235 butter packets in each tray. Find 235 × 4 place by place.",
                    ["Split 235 into 200 + 30 + 5.",
                     "Ones: 4 × 5 = 20.",
                     "Tens: 4 × 30 = 120, because 4 × 3 tens is 12 tens.",
                     "Hundreds: 4 × 200 = 800, because 4 × 2 hundreds is 8 hundreds.",
                     "Add the three products: 20 + 120 + 800 = 940.",
                     "Check by doubling twice: 235 × 4 = 235 × 2 × 2 = 470 × 2 = 940."],
                    "235 × 4 = 940")],
       ncert=["dc.remember", "dc.fact"], key_terms=["place by place", "place value", "hundreds", "tens", "ones"],
       misconceptions=["M_SPLIT_ONE", "M_ZERO_COUNT"], minutes=6),
     A("T9.C2", "Carry to the Right Place", "Apply",
       "Students multiply by a one-digit and a two-digit number, write each carry above the next place and add it after "
       "multiplying that place, and put a 0 at the end of the tens row.",
       teach=["Predict first: in 68 × 4 the ones product 4 × 8 = 32 leaves 30 over. Is the 30 added to the 60 before "
              "multiplying by 4, or to 4 × 60 after?",
              "4 × 8 = 32. Write 2 in the ones place. The 30 in 32 is 3 tens, so carry 3 to the tens place.",
              "Tens: 4 × 6 = 24 tens. Now add the carry: 24 + 3 = 27 tens. The 30 is added to 4 × 60 = 240, not to 60.",
              "27 tens is 270. Write 7 in the tens place and carry 2 to the hundreds place: 68 × 4 = 272.",
              "In lines this is 4 × 60 = 240, then 240 + 30 = 270, then 270 + 2 = 272.",
              "With a two-digit multiplier, write one row for the ones digit and one row for the tens digit. Put a 0 at "
              "the end of the tens row, then add the rows.",
              "Rule: the carry is added after multiplying the next place, not before."],
       examples=[WE("A cooperative fills 24 crates with 176 milk pouches in each crate. Find 176 × 24 with carries.",
                    ["176 × 24 has two rows: 4 ones × 176 and 2 tens × 176.",
                     "Row 1, ones: 4 × 6 = 24. Write 4 and carry 2 to the tens.",
                     "Tens: 4 × 7 = 28. Add the carry: 28 + 2 = 30. Write 0 and carry 3 to the hundreds.",
                     "Hundreds: 4 × 1 = 4. Add the carry: 4 + 3 = 7. Write 7. Row 1 is 704.",
                     "Row 2 is 2 tens × 176, the same as 20 × 176. Write a 0 in the ones place first.",
                     "2 × 6 = 12. Write 2 and carry 1.",
                     "2 × 7 = 14. Add the carry: 14 + 1 = 15. Write 5 and carry 1.",
                     "2 × 1 = 2. Add the carry: 2 + 1 = 3. Write 3. So 2 × 176 = 352, and with the 0 the row is 3,520.",
                     "Add the rows: 704 + 3,520 = 4,224.",
                     "Check: 176 × 25 = 4,400, and one 176 less is 4,400 − 176 = 4,224."],
                    "176 × 24 = 4,224")],
       ncert=["dc.discuss", "dc.note"], key_terms=["carry", "next place", "right place", "zero"],
       misconceptions=["M_CARRY_FIRST", "M_MISSING_ZERO"], minutes=8),
     DOER("T9.C3", "Practice: Carry Columns", "carry_columns", "Apply",
          "Students multiply three-digit numbers by one-digit, two-digit and three-digit numbers, writing each carry in "
          "the right place and adding it after multiplying that place, and check the product with an estimate.",
          ["Multiply place by place: ones, then tens, then hundreds.",
           "Write the carry above the next place and add it after multiplying that place.",
           "For a two-digit or three-digit multiplier, write one row for each digit and put a 0 or 00 at the end of the "
           "tens and hundreds rows.",
           "Add the rows to get the product."],
          items=[FIO("ex.dc1", "Example 6: cows of the dairy cooperative",
                     "A dairy cooperative in a small town gets its milk from 268 villagers. Each villager has at least "
                     "4 milk-giving cows. What is the minimum number of cows the dairy cooperative gets its milk from? "
                     "1 villager has at least 4 milk-giving cows. 268 villagers will have at least 268 × 4 cows.",
                     ["The minimum number of cows is 268 villagers with 4 cows each, so 268 × 4.",
                      "Split 268 into 200 + 60 + 8. 4 × 8 = 32, 4 × 60 = 240 and 4 × 200 = 800.",
                      "Add the products: 800 + 240 + 32 = 1,072.",
                      "Now Mili's father's way, place by place. Ones: 4 × 8 = 32. Write 2 and carry 3 to the tens.",
                      "Tens: 4 × 6 = 24, and 24 + 3 = 27. Write 7 and carry 2 to the hundreds.",
                      "Hundreds: 4 × 2 = 8, and 8 + 2 = 10. Write 0 and carry 1 to the thousands. Thousands: 1.",
                      "Read the digits: 1, 0, 7, 2. The number is 1,072.",
                      "The carry is added after multiplying: 30 from 32 joins 4 × 60 = 240 to make 270, and 200 from "
                      "270 joins 4 × 200 = 800 to make 1,000.",
                      "Check: 268 × 4 is a little less than 270 × 4 = 1,080, and 1,072 is."],
                     "The dairy cooperative gets its milk from at least 1,072 cows.",
                     kind="example",
                     q_figure="A line of women pouring milk into milk cans at the dairy cooperative.",
                     s_figure="A place value table with columns thousands, hundreds, tens and ones: 268 times 4 with the "
                              "carry 3 above the tens and the carry 2 above the hundreds, and the answer 1,072."),
                 FIO("ex.dc2", "Example 7: litres from Gir cows",
                     "The villagers rear various breeds of cows. Gir is an Indian cow breed from Gujarat, with a high "
                     "milk-producing capacity. Among the villagers, there are 453 Gir cows. Each of these cows give 13 "
                     "litres of milk each day. How many litres of milk does the dairy cooperative receive from Gir cows "
                     "everyday? One Gir cow produces 13 litres of milk. 453 Gir cows will produce 453 × 13 litres of "
                     "milk.",
                     ["The milk is 453 cows with 13 litres each, so 453 × 13 litres.",
                      "13 is 10 + 3, so there are two rows: 3 × 453 and 10 × 453.",
                      "Row 1, 3 × 453. Ones: 3 × 3 = 9. Write 9.",
                      "Tens: 3 × 5 = 15. Write 5 and carry 1 to the hundreds.",
                      "Hundreds: 3 × 4 = 12, and 12 + 1 = 13. Write 13. Row 1 is 1,359.",
                      "Row 2, 10 × 453: 1 ten × 453 = 453 tens = 4,530. Write 0 in the ones place, then 453.",
                      "Add the rows: 1,359 + 4,530 = 5,889.",
                      "The 100 from 150 is added to 3 × 400 = 1,200, not to 400.",
                      "Check: 453 × 13 is a little more than 450 × 13 = 5,850, and 5,889 is."],
                     "The dairy cooperative receives 5,889 litres of milk from Gir cows every day.",
                     kind="example",
                     q_figure="A Gir cow standing on grass.",
                     s_figure="A place value table with columns thousands, hundreds, tens and ones: 453 times 13 with the "
                              "carry 1 above the hundreds, the two rows 1,359 and 4,530, and the answer 5,889."),
                 FIO("ex.dc3", "Example 8: earnings from ghee",
                     "The dairy cooperative sells 1 kg cow ghee for ₹574. The cooperative is able to produce around 125 "
                     "kg of ghee in a month. How much do they earn by selling ghee in a month? Discuss what the same "
                     "coloured digits might mean.",
                     ["The earnings are ₹574 for each of 125 kg, so ₹574 × 125.",
                      "125 is 100 + 20 + 5, so there are three rows: 5 × 574, 20 × 574 and 100 × 574.",
                      "Row 1, 5 × 574. Ones: 5 × 4 = 20. Write 0 and carry 2 to the tens.",
                      "Tens: 5 × 7 = 35, and 35 + 2 = 37. Write 7 and carry 3 to the hundreds.",
                      "Hundreds: 5 × 5 = 25, and 25 + 3 = 28. Write 28. Row 1 is 2,870.",
                      "Row 2, 2 tens × 574, the same as 20 × 574. 2 × 574 = 1,148, so with a 0 at the end the row is "
                      "11,480.",
                      "A note in your maths book says 2 × 3,740 here. It should be 2 × 5,740, so 3,740 is a printed "
                      "slip.",
                      "Row 3, 1 hundred × 574 = 574 hundreds = 57,400.",
                      "Add the three rows: 2,870 + 11,480 + 57,400 = 71,750.",
                      "One way to read the colours: digits of the same colour sit in the same place, so they are added "
                      "together. The two blue digits are 5 hundreds and 3 hundreds: 5 + 3 = 8 hundreds. The two red "
                      "digits are 5 tens and 2 tens: 5 + 2 = 7 tens.",
                      "Check: 574 × 125 = 574 × 100 + 574 × 25 = 57,400 + 14,350 = 71,750."],
                     "The cooperative earns ₹71,750 in a month.",
                     kind="example",
                     q_figure="Three stacked jars of ghee, each with a label GHEE.",
                     s_figure="The lines 574 (500 + 70 + 4) × 125 (100 + 20 + 5) with the three results 2,870, 11,480 and "
                              "57,400 and the total 71,750, and beside them the place value table with the three rows."),
                 FIO("ls2.q1", "Let Us Solve: Q1 like Nida (large numbers)",
                     "Solve the following problems like Nida. (a): 548 × 6 (b): 682 × 3 (c): 324 × 18 (d): 507 × 23 "
                     "(e): 190 × 65",
                     ["(a): 548 = 500 + 40 + 8, and 6 is the row. The cells: 500 × 6 = 3,000, 40 × 6 = 240 and "
                      "8 × 6 = 48.",
                      "(a): add the cells: 3,000 + 240 + 48 = 3,288.",
                      "(b): 682 = 600 + 80 + 2, and 3 is the row. The cells: 600 × 3 = 1,800, 80 × 3 = 240 and "
                      "2 × 3 = 6.",
                      "(b): add the cells: 1,800 + 240 + 6 = 2,046.",
                      "(c): 324 = 300 + 20 + 4 and 18 = 10 + 8. The cells: 10 × 300 = 3,000, 10 × 20 = 200, "
                      "10 × 4 = 40, 8 × 300 = 2,400, 8 × 20 = 160 and 8 × 4 = 32.",
                      "(c): column sums: 3,000 + 2,400 = 5,400, 200 + 160 = 360 and 40 + 32 = 72.",
                      "(c): total: 5,400 + 360 + 72 = 5,832.",
                      "(d): 507 = 500 + 7 (there are no tens, so no column for them) and 23 = 20 + 3. The cells: "
                      "20 × 500 = 10,000, 20 × 7 = 140, 3 × 500 = 1,500 and 3 × 7 = 21.",
                      "(d): column sums: 10,000 + 1,500 = 11,500 and 140 + 21 = 161.",
                      "(d): total: 11,500 + 161 = 11,661.",
                      "(e): 190 = 100 + 90 (there are no ones, so no column for them) and 65 = 60 + 5. The cells: "
                      "60 × 100 = 6,000, 60 × 90 = 5,400, 5 × 100 = 500 and 5 × 90 = 450.",
                      "(e): column sums: 6,000 + 500 = 6,500 and 5,400 + 450 = 5,850.",
                      "(e): total: 6,500 + 5,850 = 12,350.",
                      "Check the ones digits: 8 × 6 = 48 ends in 8, 2 × 3 = 6 ends in 6, 4 × 8 = 32 ends in 2, "
                      "7 × 3 = 21 ends in 1 and 0 × 5 = 0 ends in 0, like 3,288, 2,046, 5,832, 11,661 and 12,350."],
                     "(a): 3,288; (b): 2,046; (c): 5,832; (d): 11,661; (e): 12,350"),
                 FIO("ls2.q2", "Let Us Solve: Q2 like John (large numbers)",
                     "Solve the following problems like John. (a): 123 × 84 (b): 368 × 32 (c): 159 × 324 (d): 239 × "
                     "401 (e): 592 × 5 (f): 101 × 22",
                     ["(a): 123 (100 + 20 + 3) × 84 (80 + 4). First line: 400 + 80 + 12 = 492 (4 × 123). Second line: "
                      "8,000 + 1,600 + 240 = 9,840 (80 × 123).",
                      "(a): add the two lines: 492 + 9,840 = 10,332.",
                      "(b): 368 (300 + 60 + 8) × 32 (30 + 2). First line: 600 + 120 + 16 = 736 (2 × 368). Second line: "
                      "9,000 + 1,800 + 240 = 11,040 (30 × 368).",
                      "(b): add the two lines: 736 + 11,040 = 11,776.",
                      "(c): 159 (100 + 50 + 9) × 324 (300 + 20 + 4). First line: 400 + 200 + 36 = 636 (4 × 159). "
                      "Second line: 2,000 + 1,000 + 180 = 3,180 (20 × 159). Third line: 30,000 + 15,000 + 2,700 = "
                      "47,700 (300 × 159).",
                      "(c): add the three lines: 636 + 3,180 + 47,700 = 51,516.",
                      "(d): 239 (200 + 30 + 9) × 401 (400 + 0 + 1). First line: 200 + 30 + 9 = 239 (1 × 239). The "
                      "tens digit is 0, so there is no line for it. Last line: 80,000 + 12,000 + 3,600 = 95,600 "
                      "(400 × 239).",
                      "(d): add the two lines: 239 + 95,600 = 95,839.",
                      "(e): 592 (500 + 90 + 2) × 5. The multiplier has one digit, so there is one line: "
                      "2,500 + 450 + 10 = 2,960 (5 × 592).",
                      "(f): 101 (100 + 0 + 1) × 22 (20 + 2). First line: 200 + 2 = 202 (2 × 101). Second line: "
                      "2,000 + 20 = 2,020 (20 × 101).",
                      "(f): add the two lines: 202 + 2,020 = 2,222.",
                      "Check with rough products: 120 × 85 = 10,200, 370 × 32 = 11,840, 160 × 320 = 51,200, "
                      "240 × 400 = 96,000, 600 × 5 = 3,000 and 100 × 22 = 2,200 are near the six answers."],
                     "(a): 10,332; (b): 11,776; (c): 51,516; (d): 95,839; (e): 2,960; (f): 2,222"),
                 FIO("ls2.q3a", "Let Us Solve: Q3 like Mili's father, three frames",
                     "Let us solve a few questions like Mili's father. Use the place value frames (columns Th, H, T, "
                     "O; the third frame has TTh, Th, H, T, O). (i): 806 × 9. (ii): 455 × 26. (iii): 143 × 208.",
                     ["(i): 806 × 9. Ones: 9 × 6 = 54. Write 4 and carry 5 to the tens.",
                      "(i): tens: 9 × 0 = 0, and 0 + 5 = 5. Write 5. There is no carry.",
                      "(i): hundreds: 9 × 8 = 72. Write 72. The product is 7,254.",
                      "(ii): 455 × 26 has two rows: 6 × 455 and 20 × 455.",
                      "(ii): row 1. 6 × 5 = 30, write 0 and carry 3. 6 × 5 = 30, and 30 + 3 = 33, write 3 and carry 3. "
                      "6 × 4 = 24, and 24 + 3 = 27, write 27. Row 1 is 2,730.",
                      "(ii): row 2. Write a 0 first, then 2 × 455 = 910, so the row is 9,100.",
                      "(ii): add the rows: 2,730 + 9,100 = 11,830.",
                      "(iii): 143 × 208 has rows for 8 ones, 0 tens and 2 hundreds.",
                      "(iii): row 1. 8 × 3 = 24, write 4 and carry 2. 8 × 4 = 32, and 32 + 2 = 34, write 4 and carry 3. "
                      "8 × 1 = 8, and 8 + 3 = 11, write 11. Row 1 is 1,144.",
                      "(iii): row 2 is for 0 tens: 0 × 143 = 0, so the row is 0.",
                      "(iii): row 3. Write 00 first, then 2 × 143 = 286, so the row is 28,600.",
                      "(iii): add the rows: 1,144 + 0 + 28,600 = 29,744.",
                      "Check with rough products: 800 × 9 = 7,200, 450 × 26 = 11,700 and 140 × 200 = 28,000 are near "
                      "7,254, 11,830 and 29,744."],
                     "(i): 7,254; (ii): 11,830; (iii): 29,744",
                     q_figure="Three place value frames with carry circles above the number: 806 times 9; 455 times 26 "
                              "with a carry 3 already written; 143 times 208 with a carry 3 and a carry 2 already "
                              "written, and empty boxes for the rows.",
                     s_figure="The three frames filled in: 7,254 for 806 times 9; the rows 2,730 and 9,100 and the total "
                              "11,830 for 455 times 26; the rows 1,144, 0 and 28,600 and the total 29,744 for 143 times "
                              "208."),
                 FIO("ls2.q3b", "Let Us Solve: Q3 now use Mili's father's method",
                     "Now use Mili's father's method to solve the following questions. (a): 807 × 5 (b): 143 × 28 "
                     "(c): 309 × 9 (d): 450 × 38 (e): 584 × 23 (f): 302 × 13 (g): 604 × 54 (h): 112 × 23 (i): 237 × "
                     "19",
                     ["(a): 807 × 5. Ones: 5 × 7 = 35, write 5, carry 3. Tens: 5 × 0 = 0, 0 + 3 = 3, write 3. "
                      "Hundreds: 5 × 8 = 40, write 40. The product is 4,035.",
                      "(b): 143 × 28. Row 1, 8 × 143: 8 × 3 = 24, write 4, carry 2; 8 × 4 = 32, 32 + 2 = 34, write 4, "
                      "carry 3; 8 × 1 = 8, 8 + 3 = 11, write 11. Row 1 is 1,144.",
                      "(b): row 2, 2 tens × 143: write a 0 first, then 2 × 3 = 6, 2 × 4 = 8, 2 × 1 = 2, so the row is "
                      "2,860. Add the rows: 1,144 + 2,860 = 4,004.",
                      "(c): 309 × 9. Ones: 9 × 9 = 81, write 1, carry 8. Tens: 9 × 0 = 0, 0 + 8 = 8, write 8. "
                      "Hundreds: 9 × 3 = 27, write 27. The product is 2,781.",
                      "(d): 450 × 38. Row 1, 8 × 450: 8 × 0 = 0; 8 × 5 = 40, write 0, carry 4; 8 × 4 = 32, 32 + 4 = 36, "
                      "write 36. Row 1 is 3,600.",
                      "(d): row 2, 3 tens × 450: write a 0 first, then 3 × 0 = 0; 3 × 5 = 15, write 5, carry 1; "
                      "3 × 4 = 12, 12 + 1 = 13, write 13, so the row is 13,500. Add the rows: 3,600 + 13,500 = 17,100.",
                      "(e): 584 × 23. Row 1, 3 × 584: 3 × 4 = 12, write 2, carry 1; 3 × 8 = 24, 24 + 1 = 25, write 5, "
                      "carry 2; 3 × 5 = 15, 15 + 2 = 17, write 17. Row 1 is 1,752.",
                      "(e): row 2, 2 tens × 584: write a 0 first, then 2 × 4 = 8; 2 × 8 = 16, write 6, carry 1; "
                      "2 × 5 = 10, 10 + 1 = 11, write 11, so the row is 11,680. Add the rows: 1,752 + 11,680 = 13,432.",
                      "(f): 302 × 13. Row 1, 3 × 302: 3 × 2 = 6, 3 × 0 = 0, 3 × 3 = 9. Row 1 is 906.",
                      "(f): row 2, 1 ten × 302: write a 0 first, then 302, so the row is 3,020. Add the rows: "
                      "906 + 3,020 = 3,926.",
                      "(g): 604 × 54. Row 1, 4 × 604: 4 × 4 = 16, write 6, carry 1; 4 × 0 = 0, 0 + 1 = 1, write 1; "
                      "4 × 6 = 24, write 24. Row 1 is 2,416.",
                      "(g): row 2, 5 tens × 604: write a 0 first, then 5 × 4 = 20, write 0, carry 2; 5 × 0 = 0, "
                      "0 + 2 = 2, write 2; 5 × 6 = 30, write 30, so the row is 30,200. Add the rows: "
                      "2,416 + 30,200 = 32,616.",
                      "(h): 112 × 23. Row 1, 3 × 112: 3 × 2 = 6, 3 × 1 = 3, 3 × 1 = 3. Row 1 is 336.",
                      "(h): row 2, 2 tens × 112: write a 0 first, then 2 × 2 = 4, 2 × 1 = 2, 2 × 1 = 2, so the row is "
                      "2,240. Add the rows: 336 + 2,240 = 2,576.",
                      "(i): 237 × 19. Row 1, 9 × 237: 9 × 7 = 63, write 3, carry 6; 9 × 3 = 27, 27 + 6 = 33, write 3, "
                      "carry 3; 9 × 2 = 18, 18 + 3 = 21, write 21. Row 1 is 2,133.",
                      "(i): row 2, 1 ten × 237: write a 0 first, then 237, so the row is 2,370. Add the rows: "
                      "2,133 + 2,370 = 4,503.",
                      "Check with rough products: 800 × 5 = 4,000, 140 × 30 = 4,200, 300 × 9 = 2,700, "
                      "450 × 40 = 18,000, 600 × 22 = 13,200, 300 × 13 = 3,900, 600 × 54 = 32,400, 110 × 23 = 2,530 "
                      "and 240 × 19 = 4,560 are near the nine answers."],
                     "(a): 4,035; (b): 4,004; (c): 2,781; (d): 17,100; (e): 13,432; (f): 3,926; (g): 32,616; (h): "
                     "2,576; (i): 4,503")],
          misconceptions=["M_CARRY_FIRST", "M_MISSING_ZERO"])],
    key_terms=["carry", "place by place", "place value"]))
