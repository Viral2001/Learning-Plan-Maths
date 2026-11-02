# -*- coding: utf-8 -*-
"""Topics T4 to T8 (module M2: pictures and relations among sequences). Book sections 1.3 and 1.4."""
from topics_common import A, DOER, TOPIC, WE, BOOK_TEXT, book, fio, we

TOPICS = []
H_PIC = "A picture can explain it"
H_UPDOWN = "Another example of such a relation between sequences: Adding up and down"

# ============================== T4 Visualising number sequences (1.3) ========================================
TOPICS.append(TOPIC(
    "T4", "M2", "Dot Pictures of Number Sequences", ["1.3"], "Apply",
    "Students draw the dot picture of a number sequence, extend it by one picture, and explain why triangular, "
    "square and cube numbers have those names.",
    "Many number sequences can be drawn with dots or blocks, and the picture explains the name and the rule.",
    [A("T4.C1", "Drawing counting, odd and even numbers", "Apply",
       "Students draw the dot pictures of the counting, odd and even number sequences, and tell how each next "
       "picture grows from the one before.",
       textbook=book("1.3", stop=3),
       teach=["Predict first: how would you draw 1, 2, 3, 4, 5 with dots? How would you draw 1, 3, 5, 7, 9?",
              "Counting numbers: a row of dots, one more dot each time. Odd numbers: add 2 dots each time. "
              "Even numbers: two rows, one more dot in each row each time.",
              "A picture shows the rule: each next picture is the last one with something added."],
       examples=[WE('Draw the first three pictures of the sequence 3, 6, 9 with dots, and say how the picture grows.',
                   ['Picture 1 is one column of 3 dots.', 'Picture 2 is two columns of 3 dots, 6 dots in all.', 'Picture 3 is three columns of 3 dots, 9 dots in all.'],
                   'Each picture adds a column of 3 dots.')],
       key_terms=["dot picture", "number sequence"], misconceptions=["M_ALL_ONES_NO_PATTERN"], minutes=8),
     A("T4.C2", "Why triangular, square and cube?", "Understand",
       "Students see that triangular numbers stack in a triangle of dots, square numbers fill a square grid and "
       "cube numbers build a cube of blocks.",
       textbook=[],
       teach=["Predict first: 1, 3, 6, 10, 15. What shape could the dots make?",
              "Triangular numbers: rows of 1, 2, 3, 4, 5 dots stack into a triangle. Square numbers: n rows of "
              "n dots make a square grid. Cube numbers: n layers of an n by n square of blocks make a cube.",
              "So the names come from the pictures, not by chance."],
       examples=[WE('How many dots are in a triangle with 4 rows, and why is the number called triangular?',
                   ['The rows have 1, 2, 3 and 4 dots.', '1 + 2 + 3 + 4 = 10.', 'The 10 dots stack in the shape of a triangle.'],
                   '10 dots; the rows stack into a triangle.')],
       key_terms=["triangular number", "square number", "cube"],
       misconceptions=["M_NAMES_ARBITRARY"], minutes=10),
     DOER("T4.C3", "Pull it together and do it: Dot Picture Builder", "dot_picture_builder", "Apply",
          "Students build the next dot picture of a sequence on the tool and name the number it shows.",
          ["Each number sequence can be drawn as dots or blocks.",
           "Triangular numbers make triangles, square numbers make squares and cube numbers make cubes.",
           "The next picture is found by following the same rule."],
          items=[fio("1.3.FiO.Q1"), fio("1.3.FiO.Q2")],
          misconceptions=["M_NAMES_ARBITRARY"])]))

# ============================== T5 One number, many pictures (1.3) ===========================================
TOPICS.append(TOPIC(
    "T5", "M2", "One Number, Many Pictures", ["1.3"], "Analyze",
    "Students show that one number can be drawn in more than one way, and find the next hexagonal number from "
    "the rings of dots around a centre.",
    "The same number can be pictured in different ways and play different roles, and some sequences are drawn as "
    "rings around a centre.",
    [A("T5.C1", "One number, two pictures", "Understand",
       "Students show that a number such as 6 can be drawn in two different ways, and say that the same number "
       "can play different roles depending on the picture.",
       textbook=book("1.3", start=7, stop=8),
       teach=["Predict first: the number 6. Can you draw 6 dots in two different neat shapes?",
              "Six dots make a triangle of rows 1, 2 and 3. Six dots also make a rectangle of 2 rows of 3.",
              "So 6 is a triangular number, and it is also a number that can be shown as a rectangle.",
              "The same number can be represented differently and play different roles."],
       examples=[WE('Show 10 dots as a triangle and as a rectangle.',
                   ['Triangle: rows of 1, 2, 3 and 4 dots, since 1 + 2 + 3 + 4 = 10.', 'Rectangle: 2 rows of 5 dots, since 2 × 5 = 10.'],
                   'The same 10 dots make a triangle and a rectangle.')],
       key_terms=["triangular number", "dot picture"], misconceptions=["M_ONE_PICTURE"], minutes=8),
     A("T5.C2", "Hexagonal numbers: rings around a centre", "Analyze",
       "Students build a hexagonal number picture as a centre dot with rings of 6, 12 and more dots, and find "
       "each next number by adding the next ring.",
       textbook=book("1.3", start=9, stop=10),
       teach=["Predict first: a hexagon of dots with 1 dot, then a centre dot with a ring of 6. How many dots in "
              "all?",
              "A centre dot and one ring of 6 dots make 1 + 6 = 7. Adding a ring of 12 more makes 7 + 12 = 19.",
              "The rings grow by 6 each time: 6, 12, 18, 24. The pictures 1, 7, 19, 37 are called hexagonal "
              "numbers."],
       examples=[WE('A hexagon cluster has a centre dot and one ring of 6 dots. How many dots are there after the next ring of 12 is added?',
                   ['The centre dot and the first ring make 1 + 6 = 7 dots.', 'The next ring has 12 dots, and 7 + 12 = 19.'],
                   '19 dots.')],
       key_terms=["hexagonal number", "ring"], misconceptions=["M_HEX_SAME_JUMP"], minutes=10),
     DOER("T5.C3", "Practice: Same number, different pictures", None, "Analyze",
          "Students draw 36 as a triangle and as a square, find the next hexagonal number, and picture the powers "
          "of 2 and 3.",
          ["A number can be pictured in more than one way.",
           "Hexagonal numbers are a centre dot plus rings of 6, 12, 18, 24 dots.",
           "Powers of 2 can be drawn as shapes that double each time."],
          items=[fio("1.3.FiO.Q3"), fio("1.3.FiO.Q4"), fio("1.3.FiO.Q5")],
          misconceptions=["M_ONE_PICTURE", "M_HEX_SAME_JUMP"])]))

# ============================== T6 Adding odd numbers (1.4) ==================================================
TOPICS.append(TOPIC(
    "T6", "M2", "Adding Odd Numbers Gives Squares", ["1.4"], "Analyze",
    "Students find that the sums of the first odd numbers are square numbers, explain it with L-shaped layers of "
    "dots on a square grid, and use the picture for any size.",
    "Adding the first n odd numbers gives n × n, because a square grid splits into L-shapes of 1, 3, 5, 7, ... "
    "dots.",
    [A("T6.C1", "Adding odd numbers: what do the sums show?", "Understand",
       "Students add the first few odd numbers one at a time, see that the sums are square numbers, and say the "
       "pattern is worth explaining.",
       textbook=book("1.4", stop=9),
       teach=["Predict first: add 1 + 3. Then 1 + 3 + 5. Will the sums be odd or even? Will you get a pattern?",
              "The sums are 1, 4, 9, 16, 25, 36, the square numbers.",
              "This is a beautiful pattern. A mathematician also asks why it happens and whether it will go on "
              "forever."],
       examples=[we("1.4.ex1")],
       key_terms=["odd numbers", "square number", "sum"],
       misconceptions=["M_ODD_SUM_ODD", "M_CHECK_FEW"], minutes=8),
     A("T6.C2", "The L-shapes that explain it", "Analyze",
       "Students cut a square grid of dots into nested L-shaped layers of 1, 3, 5, 7, ... dots, explain why the "
       "pattern goes on forever, and find the sum of the first 10 and 100 odd numbers.",
       textbook=book("1.4", start=9, stop=11) + book("1.4", H_PIC),
       teach=["Predict first: a 6 by 6 square grid of dots. Can you cut it into pieces of 1, 3, 5, 7, 9 and 11 "
              "dots?",
              "Start at one corner with 1 dot. Wrap an L-shape of 3 dots around it, then an L of 5, then 7, and so "
              "on, each L having 2 more dots than the one before.",
              "A square of any size can be cut this way, so adding odd numbers gives squares forever.",
              "The picture works for the 10 by 10 and the 100 by 100 grid too."],
       examples=[we("1.4.q2"), we("1.4.q1"), we("1.4.q3"), we("1.4.q4")],
       key_terms=["L-shape", "square grid", "odd numbers"],
       misconceptions=["M_PICTURE_ONE_SIZE", "M_CHECK_FEW"], minutes=10),
     DOER("T6.C3", "Pull it together and do it: Odd Number L-Shape Builder", "odd_sum_builder", "Apply",
          "Students wrap L-shapes of odd numbers of dots around a corner on the tool and read the square number "
          "each time.",
          ["The first n odd numbers add up to n × n.",
           "Each L-shape has two more dots than the one before.",
           "The picture works for a grid of any size."],
          items=[],
          misconceptions=["M_ODD_SUM_ODD", "M_PICTURE_ONE_SIZE"])]))

# ============================== T7 Adding up and down (1.4) ==================================================
TOPICS.append(TOPIC(
    "T7", "M2", "Adding Up and Down Gives Squares", ["1.4"], "Analyze",
    "Students see that adding the counting numbers up and then down gives square numbers, and explain it with a "
    "diamond of dots.",
    "Adding the counting numbers up to n and back down gives n × n, because the rows of a tilted square grid "
    "count 1, 2, 3, ..., n, ..., 3, 2, 1.",
    [A("T7.C1", "Up and then down: another way to get squares", "Understand",
       "Students add the counting numbers up and then down for the first few lines, see squares, and predict "
       "the next line.",
       textbook=book("1.4", H_UPDOWN, stop=8),
       teach=["Predict first: what is 1 + 2 + 1? And 1 + 2 + 3 + 2 + 1? Look at your two answers.",
              "The answers are 4 and 9. The next lines give 16, 25 and 36, the square numbers again.",
              "Predict the 7th line: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 6 + 5 + 4 + 3 + 2 + 1 should be 49.",
              "This is yet another way to get the square numbers."],
       examples=[WE('Find the value of 1 + 2 + 3 + 4 + 5 + 6 + 7 + 6 + 5 + 4 + 3 + 2 + 1.',
                   ['The numbers go up to 7 and back down.', 'The pattern says an up-and-down sum to n is n × n.', '7 × 7 = 49.'],
                   '49.')],
       key_terms=["counting numbers", "square number", "up and down"],
       misconceptions=["M_UP_DOWN_DOUBLE", "M_CHECK_FEW"], minutes=8),
     A("T7.C2", "The diamond of dots", "Analyze",
       "Students tilt a square grid of dots so that its rows count 1, 2, 3, ..., n, ..., 3, 2, 1, and use it to "
       "explain why adding up and down gives squares.",
       textbook=book("1.4", H_UPDOWN, start=7, stop=9),
       teach=["Predict first: tilt a 3 by 3 grid so a corner points up. How many dots are in each row?",
              "The rows have 1, 2, 3, 2 and 1 dots, so 1 + 2 + 3 + 2 + 1 = 9, the same 3 by 3 grid.",
              "For any n, the tilted n by n grid has rows 1, 2, ..., n, ..., 2, 1, so the sum is n × n."],
       examples=[we("1.4.q5")],
       key_terms=["diamond", "square grid"], misconceptions=["M_UP_DOWN_DOUBLE", "M_PICTURE_ONE_SIZE"], minutes=10),
     DOER("T7.C3", "Pull it together and do it: Diamond Dot Builder", "updown_builder", "Apply",
          "Students build up-and-down sums as a diamond of dots on the tool and read off the square number.",
          ["Adding the counting numbers up to n and back down gives n × n.",
           "The diamond is an n by n grid seen along its diagonals.",
           "The picture works for any n, so the pattern never stops."],
          items=[fio("1.4.FiO.Q1"), fio("1.4.FiO.Q2")],
          misconceptions=["M_UP_DOWN_DOUBLE", "M_PICTURE_ONE_SIZE"])]))

# ============================== T8 More relations among sequences (1.4) ======================================
TOPICS.append(TOPIC(
    "T8", "M2", "More Relations Among Sequences", ["1.4"], "Analyze",
    "Students add up a sequence step by step, add neighbouring terms, and find which sequence results, testing "
    "each on the first terms and explaining with a picture where they can.",
    "Running totals and sums of neighbouring terms turn one number sequence into another, and a picture shows "
    "why.",
    [A("T8.C1", "Adding a sequence up: running totals", "Understand",
       "Students form the running totals of a sequence and see that they make a new number sequence.",
       textbook=book("1.4", stop=1),
       teach=["Predict first: add up the even numbers step by step: 2, then 2 + 4, then 2 + 4 + 6. What do you "
              "get?",
              "The running totals are 2, 6, 12 and then 20, because 2 + 4 + 6 + 8 = 20.",
              "Adding a sequence up step by step makes a new sequence, not the same one.",
              "Different starting sequences give different results, so each one needs its own check."],
       examples=[WE('Find the running totals of the sequence 3, 6, 9, 12.',
                   ['The first total is 3.', '3 + 6 = 9.', '3 + 6 + 9 = 18.', '3 + 6 + 9 + 12 = 30.'],
                   'The running totals are 3, 9, 18, 30.')],
       key_terms=["running total", "number sequence"], misconceptions=["M_RUNNING_SAME"], minutes=8),
     A("T8.C2", "Adding neighbouring terms", "Analyze",
       "Students add each pair of neighbouring terms of a sequence and find the new sequence, checking it on the "
       "first terms.",
       textbook=[],
       teach=["Predict first: add neighbouring counting numbers: 1 + 2, then 2 + 3, then 3 + 4. What do you "
              "get?",
              "The sums are 3, 5, 7, 9, the odd numbers after 1.",
              "Each sum is the smaller number twice plus 1, which is why it is odd.",
              "A picture or a reason shows whether the pattern goes on, and a check of the first few terms alone "
              "does not."],
       examples=[WE('Add each pair of neighbouring even numbers: 2 and 4, 4 and 6, 6 and 8, 8 and 10.',
                   ['2 + 4 = 6.', '4 + 6 = 10.', '6 + 8 = 14.', '8 + 10 = 18.'],
                   'The sums are 6, 10, 14, 18, going up by 4 each time.')],
       key_terms=["neighbouring terms", "odd numbers"], misconceptions=["M_PAIRS_SAME", "M_CHECK_FEW"],
       minutes=8),
     DOER("T8.C3", "Pull it together and do it: Sequence Relations Lab", "sequence_relations_lab", "Analyze",
          "Students combine sequences on the tool by running totals and sums of neighbours, and name the sequence "
          "that results.",
          ["Running totals and sums of neighbours make new sequences.",
           "Check a relation on the first terms, then explain it with a picture.",
           "Sums of triangular numbers, powers of 2 and hexagonal numbers give squares, powers of 2 and cubes."],
          items=[fio("1.4.FiO.Q3"), fio("1.4.FiO.Q4"), fio("1.4.FiO.Q5"), fio("1.4.FiO.Q6"), fio("1.4.FiO.Q7"),
                 fio("1.4.FiO.Q8"), fio("1.4.FiO.Q9")],
          misconceptions=["M_RUNNING_SAME", "M_PAIRS_SAME"])]))
