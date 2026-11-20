# -*- coding: utf-8 -*-
"""Topics T4 and T5 (module M2: Area and Perimeter of Rectangles). Area and Perimeter Are Different (same area with
different perimeters, same perimeter with different areas, the book's mats, Trisha and Let Us Explore) and Area and
Perimeter of Rectangles and Squares (length times breadth, two lengths and two breadths, the square).
Every teaching concept has one worked example with the plan's own numbers; every book question is an FIO item of its
topic's DOER, in the book's order."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T4 Area and Perimeter Are Different ========================================
TOPICS.append(TOPIC(
    "T4", "M2", "Area and Perimeter Are Different", ["Let Us Explore"], "Analyze",
    "Students show with examples that area and perimeter are different measures: shapes with the same area can have "
    "different perimeters, and shapes with the same perimeter can have different areas.",
    "Area counts the squares inside a shape and perimeter counts the edges all the way round it. They are different "
    "measures, so one can stay the same while the other changes.",
    [A("T4.C1", "Same Area, Different Perimeter", "Analyze",
       "Students find the perimeters of shapes that have the same area and see that the perimeters can be different.",
       teach=["Predict first: three rectangles are each made of 16 unit squares. Will they all have the same "
              "perimeter?",
              "Area counts the squares inside a shape. Perimeter counts the edges all the way round it. They are two "
              "different measures.",
              "A square 4 by 4, a rectangle 8 by 2 and a thin strip 16 by 1 are all made of 16 squares. Their borders "
              "are not the same length.",
              "The long thin shape has the longest border, because its squares are spread out along its sides.",
              "Rule: shapes with the same area can have different perimeters."],
       examples=[WE("Three rectangles are each made of 16 unit squares: 4 by 4, 8 by 2 and 16 by 1. Find the area and "
                    "the perimeter of each.",
                    ["Areas: 4 × 4 = 16, 8 × 2 = 16 and 16 × 1 = 16. All three have the same area, 16 square units.",
                     "Perimeter of the 4 by 4 rectangle: 4 + 4 + 4 + 4 = 16 units.",
                     "Perimeter of the 8 by 2 rectangle: 8 + 2 + 8 + 2 = 20 units.",
                     "Perimeter of the 16 by 1 rectangle: 16 + 1 + 16 + 1 = 34 units.",
                     "Check: 16, 20 and 34 are three different numbers."],
                    "All three have an area of 16 square units, but the perimeters are 16, 20 and 34 units")],
       key_terms=["area", "perimeter", "same area"],
       misconceptions=["M_AREA_IS_PERIM", "M_SAME_AREA_SAME_PERIM"], minutes=5),
     A("T4.C2", "Same Perimeter, Different Area", "Analyze",
       "Students find the areas of shapes that have the same perimeter and see that a bigger area does not always "
       "mean a bigger perimeter.",
       teach=["Predict first: Trisha makes a bigger rectangle, so its area grows. Must its perimeter grow too?",
              "Shapes can also have the same perimeter and different areas. The area depends on how many squares fit "
              "inside the border, not on how long the border is.",
              "Compare a 1 by 8 rectangle with a 3 by 3 square. The 1 by 8 rectangle has area 1 × 8 = 8 and perimeter "
              "1 + 8 + 1 + 8 = 18. The 3 by 3 square has area 3 × 3 = 9 and perimeter 3 + 3 + 3 + 3 = 12.",
              "The area grew from 8 to 9, but the perimeter became smaller, from 18 to 12.",
              "Rule: area and perimeter are different measures. One can stay the same while the other changes, so a "
              "bigger area does not always mean a bigger perimeter."],
       examples=[WE("Three rectangles each have a perimeter of 20 units: 5 by 5, 7 by 3 and 9 by 1. Find the area of "
                    "each.",
                    ["Check the perimeters first: 5 + 5 + 5 + 5 = 20, 7 + 3 + 7 + 3 = 20 and 9 + 1 + 9 + 1 = 20.",
                     "Area of the 5 by 5 rectangle: 5 × 5 = 25 square units.",
                     "Area of the 7 by 3 rectangle: 7 × 3 = 21 square units.",
                     "Area of the 9 by 1 rectangle: 9 × 1 = 9 square units.",
                     "Check: 25, 21 and 9 are different, though the perimeter is 20 for all three."],
                    "The perimeter is 20 units for all three, but the areas are 25, 21 and 9 square units")],
       key_terms=["area", "perimeter", "same perimeter"],
       misconceptions=["M_BIGGER_AREA_BIGGER_PERIM", "M_AREA_IS_PERIM"], minutes=5),
     DOER("T4.C3", "Practice: Shape Builder", "shape_builder", "Analyze",
          "Students find the area and the perimeter of the mats and shapes in the questions and say what they notice "
          "about them.",
          ["Count the squares inside a shape for its area.",
           "Count the edges all the way round it for its perimeter.",
           "The same area can have different perimeters, and the same perimeter can have different areas."],
          items=[FIO("LUD.mats", "Let Us Do (mats), Q4",
                     "The following mats are made of square patches of equal size. How many square patches will be "
                     "required to cover each mat? Would both mats require an equal or different number of patches? "
                     "Trace and cut out a small square of the size given below and find the area. (a) Area = ___ "
                     "Perimeter = ___ (b) Area = ___ Perimeter = ___",
                     ["Lay the small patch along mat (a) again and again: it fits 5 times in a row and 2 times along "
                      "the breadth. The patch is 1 cm by 1 cm, the same as a 1 cm square of the grids.",
                      "Mat (a): 2 rows of 5 patches, 2 × 5 = 10 patches. The area is 10 square cm.",
                      "The perimeter of mat (a): 5 + 2 + 5 + 2 = 14 cm.",
                      "Mat (b): the patch fits 4 times in a row and 3 times along the breadth, so 3 rows of 4 patches, "
                      "3 × 4 = 12 patches. The area is 12 square cm.",
                      "The perimeter of mat (b): 4 + 3 + 4 + 3 = 14 cm.",
                      "10 patches and 12 patches are different numbers, so the two mats need a different number of "
                      "patches.",
                      "Check: the perimeters are equal, 14 cm and 14 cm, but the areas are not."],
                     "(a): 10 patches, area 10 square cm, perimeter 14 cm; (b): 12 patches, area 12 square cm, "
                     "perimeter 14 cm. Different numbers of patches.",
                     kind="exercise",
                     q_figure="Two rectangular mats, (a) and (b), each with one small square patch drawn in its top "
                              "left corner to show the size of a patch; mat (a) is wide and short, and mat (b) is "
                              "narrower and taller.",
                     s_figure="The two mats filled with patches: mat (a) with 5 patches in a row and 2 rows, mat (b) "
                              "with 4 patches in a row and 3 rows."),
                 FIO("trisha", "Trisha's Rectangles: is it always true",
                     "Trisha makes these two rectangles. She says, \"I increased the area of my rectangle, and the "
                     "perimeter increased.\" Do you think this is always true?",
                     ["First rectangle: 2 squares wide and 3 squares tall. Area: 2 × 3 = 6 square units. Perimeter: "
                      "2 + 3 + 2 + 3 = 10 units.",
                      "Second rectangle: 3 squares wide and 4 squares tall. Area: 3 × 4 = 12 square units. Perimeter: "
                      "3 + 4 + 3 + 4 = 14 units.",
                      "Here the area grew from 6 to 12 and the perimeter grew from 10 to 14. Trisha is right for these "
                      "two rectangles.",
                      "But is it always true? Look at the two mats: the area grew from 10 to 12, and the perimeter "
                      "stayed 14.",
                      "Try one more pair. A 1 by 8 rectangle has area 1 × 8 = 8 and perimeter 1 + 8 + 1 + 8 = 18. A "
                      "3 by 3 square has area 3 × 3 = 9 and perimeter 3 + 3 + 3 + 3 = 12. The area grew and the "
                      "perimeter became smaller.",
                      "So a bigger area does not always give a bigger perimeter.",
                      "Check: 18 is more than 12, so the perimeter went down while the area went up."],
                     "No, it is not always true. Here both grew (area 6 to 12, perimeter 10 to 14), but the mats have "
                     "areas 10 and 12 and the same perimeter 14.",
                     kind="prompt",
                     q_figure="Two rectangles of orange squares: the first 2 squares wide and 3 squares tall, the "
                              "second 3 squares wide and 4 squares tall.",
                     s_figure="The two rectangles with their area and perimeter written under each."),
                 FIO("LUE.Q1", "Let Us Explore: same area",
                     "Tick the shapes with the same area. Find the perimeters of these shapes. What do you notice? "
                     "Discuss.",
                     ["Count the squares of each shape. (a) is 6 squares wide and 2 tall: 6 × 2 = 12 squares.",
                      "(b) is a block 2 wide and 5 tall, 2 × 5 = 10 squares, with a row of 2 more on top: 10 + 2 = 12 "
                      "squares.",
                      "(c) is 3 wide and 4 tall: 3 × 4 = 12 squares. (d) is 4 wide and 3 tall: 4 × 3 = 12 squares.",
                      "(e) is a row of 8 squares, so its area is 8. (f) is a row of 12 squares, so its area is 12.",
                      "The shapes with the same area, 12 square cm, are (a), (b), (c), (d) and (f). Tick these five.",
                      "Now find the perimeters. (a): 6 + 2 + 6 + 2 = 16 cm. (c): 3 + 4 + 3 + 4 = 14 cm. (d): 4 + 3 + "
                      "4 + 3 = 14 cm. (f): 12 + 1 + 12 + 1 = 26 cm.",
                      "(b): the 2 by 5 block has 2 + 5 + 2 + 5 = 14 cm round it, and the row of 2 on top, shifted one "
                      "square to the left, adds 4 more: 14 + 4 = 18 cm.",
                      "For (e): 8 + 1 + 8 + 1 = 18 cm.",
                      "Notice: the five shapes all cover 12 square cm, but their perimeters 16, 18, 14, 14 and 26 cm "
                      "are different. The same area can have different perimeters."],
                     "Same area, 12 square cm: (a), (b), (c), (d), (f). Perimeters: 16, 18, 14, 14, 26 cm. Same area, "
                     "different perimeters.",
                     kind="exercise",
                     q_figure="Six shaded shapes labelled (a) to (f) on a grid of 1 cm squares: (a) a rectangle 6 "
                              "squares wide and 2 tall, (b) a block 2 wide and 5 tall with a row of 2 squares joined "
                              "on top and shifted one square to the left, (c) a rectangle 3 wide and 4 tall, (d) a "
                              "rectangle 4 wide and 3 tall, (e) a row of 8 squares, (f) a row of 12 squares.",
                     s_figure="The same shapes with a tick on (a), (b), (c), (d) and (f), and the area and perimeter "
                              "written beside each shape."),
                 FIO("LUE.Q2", "Let Us Explore: same perimeter",
                     "Tick the shapes with the same perimeter. Find the areas of these shapes. What do you notice? "
                     "Discuss.",
                     ["Count the squares of each shape. Every shape is made of 7 squares, so every area is 7 square "
                      "cm.",
                      "Now find the perimeter of each shape by walking round its border and counting the outer edges.",
                      "(a): 3 across the top, 3 down the right side, 1 back, 1 up, 2 back, 2 up the left side: 3 + 3 + "
                      "1 + 1 + 2 + 2 = 12 cm.",
                      "(b): 3 across the top, 1 down, 1 back, 2 down, 2 back, 3 up the left side: 3 + 1 + 1 + 2 + 2 + "
                      "3 = 12 cm.",
                      "(c): a column of 4 squares has 4 + 1 + 4 + 1 = 10 edges round it. Each of the 3 squares joined "
                      "to its side hides 1 edge and shows 3 new edges, so each adds 2: 10 + 2 + 2 + 2 = 16 cm.",
                      "(d): 1 across the top, 4 down, 2 across, 1 down, 3 back along the bottom, 5 up the left side: "
                      "1 + 4 + 2 + 1 + 3 + 5 = 16 cm.",
                      "(e): a row of 7 squares has 7 + 1 + 7 + 1 = 16 cm.",
                      "Shapes (a) and (b) have the same perimeter, 12 cm. Shapes (c), (d) and (e) have the same "
                      "perimeter, 16 cm. Tick these.",
                      "Notice: all five shapes have the area 7 square cm, but the perimeter is 12 cm for two of them "
                      "and 16 cm for three. The same area can have different perimeters."],
                     "Perimeter 12 cm: (a), (b). Perimeter 16 cm: (c), (d), (e). Every shape has an area of 7 square "
                     "cm.",
                     kind="exercise",
                     q_figure="Five shaded shapes labelled (a) to (e) on a grid of 1 cm squares, each made of 7 "
                              "squares: (a) a block 3 wide and 2 tall with one square under its right end, (b) a row "
                              "of 3 squares over a 2 by 2 block, sticking out to the right, (c) a column of 4 squares "
                              "with one square left of its third square, one right of its third square and one right "
                              "of its top square, (d) a column of 5 squares with a row of 2 more squares joined to "
                              "the right of its bottom square, (e) a row of 7 squares.",
                     s_figure="The same shapes with the perimeter 12 cm or 16 cm and the area 7 square cm written "
                              "beside each shape."),
                 FIO("LUD.same_area", "Let Us Do (same area), Q1",
                     "Draw different shapes having the same area as the given shape. Write the perimeter of each "
                     "shape. What do you notice? Discuss.",
                     ["The given shape is a rectangle 9 squares long and 2 squares broad. Its area is 9 × 2 = 18 "
                      "square cm.",
                      "Its perimeter is 9 + 2 + 9 + 2 = 22 cm.",
                      "Draw other shapes made of exactly 18 squares. A 6 by 3 rectangle has 6 × 3 = 18 squares and "
                      "perimeter 6 + 3 + 6 + 3 = 18 cm.",
                      "A thin strip 18 by 1 has 18 × 1 = 18 squares and perimeter 18 + 1 + 18 + 1 = 38 cm.",
                      "A block of 4 by 4 squares with 2 more squares in a row below its left end has 16 + 2 = 18 "
                      "squares. Walking round it: 4 across the top, 4 down, 2 back, 1 down, 2 back, 5 up the left "
                      "side: 4 + 4 + 2 + 1 + 2 + 5 = 18 cm.",
                      "Notice: all these shapes have the area 18 square cm, but the perimeters 22, 18, 38 and 18 cm "
                      "are not all the same. Shapes with the same area can have different perimeters.",
                      "Your shapes may be different from these. Your answer may differ."],
                     "Sample answer: area 18 square cm; 6 by 3 has perimeter 18 cm and 18 by 1 has 38 cm. Same area, "
                     "different perimeters. Your answer may differ.",
                     kind="exercise",
                     q_figure="A square grid of 1 cm squares with a green rectangle marked (a), 9 squares long and 2 "
                              "squares tall.",
                     s_figure="Three shapes of 18 squares on the grid, 6 by 3, 18 by 1 and a 4 by 4 block with 2 "
                              "squares below it, each with its perimeter written beside it."),
                 FIO("LUD.a_less_b", "Let Us Do (same area), Q2",
                     "Is the area of shape (a) less than the area of shape (b) given below? Discuss.",
                     ["Shape (a) is a square 3 squares wide and 3 squares tall. Its area is 3 × 3 = 9 square units.",
                      "Shape (b) is a triangle. Count its whole squares row by row: the top row has 4 whole squares, "
                      "the next row has 2 and the last row has 0: 4 + 2 + 0 = 6 whole squares.",
                      "Count its half squares: each row has 2, so there are 6 half squares. 2 half squares make 1 "
                      "whole square, so 6 ÷ 2 = 3 whole squares.",
                      "The area of shape (b) is 6 + 3 = 9 square units.",
                      "Shape (a) has 9 and shape (b) has 9, so the two areas are equal.",
                      "Check: 9 is not less than 9, so the area of (a) is not less than the area of (b)."],
                     "No. Shape (a) has 9 unit squares. Shape (b) has 6 whole squares and 6 half squares, which is "
                     "also 9. The areas are equal.",
                     kind="exercise",
                     q_figure="A square grid with shape (a), a blue square 3 squares wide and 3 tall, and shape (b), "
                              "an orange triangle whose top side is 6 squares long and whose point touches the bottom "
                              "line 3 squares below the middle of the top side.",
                     s_figure="The triangle with its 6 whole squares and 6 half squares marked, next to the square "
                              "with its 9 squares.")],
          misconceptions=["M_AREA_IS_PERIM", "M_BIGGER_AREA_BIGGER_PERIM", "M_SAME_AREA_SAME_PERIM"])],
    key_terms=["area", "perimeter"]))

# ============================== T5 Area and Perimeter of Rectangles and Squares ============================
TOPICS.append(TOPIC(
    "T5", "M2", "Area and Perimeter of Rectangles and Squares",
    ["Area of a Rectangle", "Perimeter of a Rectangle", "Square"], "Apply",
    "Students find the area and the perimeter of rectangles and squares from their length and breadth.",
    "The area of a rectangle is length × breadth and its perimeter is 2 × length + 2 × breadth. A square is a "
    "rectangle with equal sides: its area is length × length and its perimeter is 4 × length.",
    [A("T5.C1", "Area of a Rectangle: Length × Breadth", "Apply",
       "Students find the area of a rectangle by multiplying its length and its breadth, as the number of rows times "
       "the number of patches in a row.",
       textbook=["We don't need to count them all. Look! There are 6 rows of 4 patches each. That is 6 × 4 = 24 "
                 "patches.", "Area of Rectangle = Length × Breadth"],
       teach=["Predict first: a patchwork has 5 rows with 8 patches in each row. Do we have to count the patches one by "
              "one to find how many there are?",
              "No. Count by rows: the number of rows times the number of patches in a row. That is 5 × 8 = 40 patches.",
              "The number of patches in a row is the length of the rectangle, and the number of rows is its breadth. "
              "Each patch is a unit square, so the area is the same number.",
              "Rule: area of a rectangle = length × breadth. If the sides are in cm the area is in square cm, and if "
              "the sides are in m the area is in square m.",
              "Rows times columns is multiplication: this is why area and multiplication go together."],
       examples=[WE("A rectangular patchwork has 5 rows of 8 patches. Each patch is a square of side 1 cm. Find the "
                    "area of the patchwork.",
                    ["Count by rows: 5 rows of 8 patches, 5 × 8 = 40 patches.",
                     "The length is 8 cm and the breadth is 5 cm.",
                     "Area = Length × Breadth, so the area is 8 × 5 = 40.",
                     "Each patch is 1 square cm, so the area is 40 square cm.",
                     "Check: counting by rows and multiplying the sides both give 40."],
                    "The area is 40 square cm")],
       ncert=["rect.rule", "note.rows"], key_terms=["area", "length", "breadth"],
       misconceptions=["M_AREA_IS_PERIM", "M_AREA_UNIT"], minutes=5),
     A("T5.C2", "Perimeter of a Rectangle", "Apply",
       "Students find the perimeter of a rectangle by adding its four sides, and by 2 × length + 2 × breadth.",
       textbook=["Perimeter = Length + Length + Breadth + Breadth", "= 2 × Length + 2 × Breadth",
                 "The lengths of the opposite sides of a rectangle are equal."],
       teach=["Predict first: a rectangle is 12 cm long and 5 cm broad. How many different side lengths do you need to "
              "measure to find its perimeter?",
              "Only two. The opposite sides of a rectangle are equal: the two long sides are the same, and the two "
              "short sides are the same.",
              "Walk round the border and add: length + length + breadth + breadth.",
              "That is 2 lengths and 2 breadths, so the perimeter is 2 × length + 2 × breadth.",
              "Half of the perimeter is length + breadth. This helps when you know the perimeter and want to find "
              "possible sides.",
              "Rule: perimeter of a rectangle = 2 × length + 2 × breadth."],
       examples=[WE("A rectangle is 11 cm long and 4 cm broad. Find its perimeter.",
                    ["The opposite sides are equal: two sides of 11 cm and two sides of 4 cm.",
                     "Add all four sides: 11 + 4 + 11 + 4 = 30.",
                     "Or use the rule: 2 × 11 = 22 and 2 × 4 = 8.",
                     "22 + 8 = 30.",
                     "Check: adding the sides and using the rule both give 30."],
                    "The perimeter is 30 cm")],
       ncert=["rect.perimeter"], key_terms=["perimeter", "length", "breadth"],
       misconceptions=["M_PERIM_TWO_SIDES", "M_AREA_IS_PERIM"], minutes=5),
     A("T5.C3", "Squares: Length × Length and 4 × Length", "Apply",
       "Students find the area and the perimeter of a square from the length of one side.",
       textbook=["What will happen if all the sides of a rectangle are equal, that is, the case of square?",
                 "Area of Square = Length × Length",
                 "Perimeter of Square = Length + Length + Length + Length = 4 × Length"],
       teach=["Predict first: all the sides of a square patch are equal. How many lengths do you need to measure?",
              "Only one. A square is a rectangle whose length and breadth are equal.",
              "Area of a square = length × length: the side times itself.",
              "Perimeter of a square = length + length + length + length = 4 × length.",
              "Do not mix them up: the area is the side times itself, and the perimeter is 4 times the side.",
              "Rule: area of a square = length × length, and perimeter of a square = 4 × length."],
       examples=[WE("A square patch has a side of 7 cm. Find its area and its perimeter.",
                    ["All the sides of a square are equal, so the length and the breadth are both 7 cm.",
                     "Area = Length × Length = 7 × 7 = 49 square cm.",
                     "Perimeter = 4 × Length = 4 × 7 = 28 cm.",
                     "Check: adding the four sides, 7 + 7 + 7 + 7 = 28."],
                    "The area is 49 square cm and the perimeter is 28 cm")],
       ncert=["square.rule"], key_terms=["square", "area", "perimeter"],
       misconceptions=["M_SQUARE_MIX"], minutes=5),
     DOER("T5.C4", "Practice: Rectangle Maker", "rectangle_maker", "Apply",
          "Students find the area and the perimeter of rectangles and squares, and draw rectangles with a given "
          "perimeter.",
          ["Area is length × breadth, in square units.",
           "Perimeter is 2 × length + 2 × breadth, in units.",
           "A square has equal sides: area length × length, perimeter 4 × length."],
          items=[FIO("LUD1.Q2", "Let Us Do (perimeter), Q2",
                     "Draw two rectangles each having the following perimeters. (a) 26 cm; (b) 18 cm",
                     ["The perimeter of a rectangle is 2 × length + 2 × breadth, so length + breadth is half of the "
                      "perimeter.",
                      "(a) Half of 26 is 26 ÷ 2 = 13, so length + breadth = 13.",
                      "Choose a length and a breadth that add to 13: 8 + 5 = 13 and 10 + 3 = 13. Draw a rectangle 8 "
                      "cm by 5 cm and another 10 cm by 3 cm.",
                      "Check: 8 + 5 + 8 + 5 = 26 and 10 + 3 + 10 + 3 = 26.",
                      "(b) Half of 18 is 18 ÷ 2 = 9, so length + breadth = 9.",
                      "Choose 6 + 3 = 9 and 7 + 2 = 9. Draw a rectangle 6 cm by 3 cm and another 7 cm by 2 cm.",
                      "Check: 6 + 3 + 6 + 3 = 18 and 7 + 2 + 7 + 2 = 18. Your rectangles may be different."],
                     "Sample answer: (a): 8 cm by 5 cm and 10 cm by 3 cm; (b): 6 cm by 3 cm and 7 cm by 2 cm. Your "
                     "answer may differ.",
                     kind="exercise",
                     s_figure="Four rectangles drawn on a grid with their sides marked: 8 by 5 and 10 by 3 for 26 cm, "
                              "6 by 3 and 7 by 2 for 18 cm."),
                 FIO("patch.example", "Example 1: the square patchwork",
                     "Preetha and Adrit's grandmother is making another square patchwork. She arranges the patches as "
                     "shown below. Can you guess how many patches she will need? How did you find it?",
                     ["We do not need to count the patches one by one. Look at the rows.",
                      "There are 6 rows, and each row has 4 patches.",
                      "6 × 4 = 24, so she will need 24 patches.",
                      "The length of one side is 6 and the other side is 4, so Area = Length × Breadth = 6 cm × 4 cm "
                      "= 24 square cm.",
                      "Check by columns: 4 columns of 6 patches, 4 × 6 = 24."],
                     "24 patches. Area = Length × Breadth = 6 cm × 4 cm = 24 square cm.",
                     kind="example",
                     q_figure="A rectangle of square patches with only the patches of its top row and its left "
                              "column coloured pink and the rest drawn empty, and its sides marked Length and "
                              "Breadth.",
                     s_figure="The same rectangle with all its patches coloured, in 6 rows of 4."),
                 FIO("patch.check", "Area of a Rectangle: check the earlier examples",
                     "Go back to the previous examples and check whether the product of the length and the breadth "
                     "of the rectangles is the same as the area you had calculated by counting.",
                     ["Take each rectangle from before and multiply its length and its breadth.",
                      "Rectangles A, B and C: 3 × 4 = 12, 2 × 4 = 8 and 2 × 5 = 10. These are the numbers of unit "
                      "squares we counted.",
                      "Gardens A and B: 2 × 5 = 10 and 4 × 3 = 12. These are the numbers we counted.",
                      "Mats (a) and (b): 5 × 2 = 10 and 4 × 3 = 12. These are the numbers of patches we counted.",
                      "Check: for every rectangle, length × breadth is the same as the count."],
                     "Yes. In every example length × breadth is the same as the area counted: 12, 8, 10, 10, 12, 10 "
                     "and 12.",
                     kind="prompt"),
                 FIO("square.example", "Example 2: a square of side 5",
                     "All the sides of a rectangle are equal, that is, the case of a square. Think about a square "
                     "whose sides are 5 units long. What are its area and its perimeter?",
                     ["All the sides of a square are equal, so the length and the breadth are both 5 units.",
                      "Area of a square = Length × Length = 5 × 5 = 25 square cm.",
                      "Perimeter of a square = Length + Length + Length + Length = 4 × Length.",
                      "4 × 5 = 20, so the perimeter is 20 cm.",
                      "Check: adding the four sides, 5 + 5 + 5 + 5 = 20."],
                     "Area = 5 × 5 = 25 square cm. Perimeter = 4 × 5 = 20 cm.",
                     kind="example",
                     q_figure="A square with its side marked 5 cm."),
                 FIO("LUD.floor", "Let Us Do (rectangle rules), Q1",
                     "Find the area of your classroom floor in square meters. Take the help of your teacher to "
                     "measure the length and breadth of the floor. What is the perimeter of the classroom floor?",
                     ["Measure the length and the breadth of the floor with a measuring tape, in metres.",
                      "Area of the floor = Length × Breadth, in square m. Perimeter = 2 × Length + 2 × Breadth, in "
                      "metres.",
                      "Sample answer with practice values: a floor 8 m long and 6 m broad.",
                      "Area: 8 × 6 = 48 square m.",
                      "Perimeter: 2 × 8 = 16 and 2 × 6 = 12, and 16 + 12 = 28 m.",
                      "Check: 8 + 6 + 8 + 6 = 28. Your answer may differ, because your classroom may be a different "
                      "size."],
                     "Sample answer with practice values: 8 m by 6 m gives an area of 48 square m and a perimeter of "
                     "28 m. Your answer may differ.",
                     kind="exercise"),
                 FIO("LUD.five", "Let Us Do (rectangle rules), Q2",
                     "Find the area and perimeter of the following shapes.",
                     ["Read the length and the breadth of each shape from the grid. Each square is 1 cm.",
                      "(a) 6 cm by 6 cm. Area: 6 × 6 = 36 square cm. Perimeter: 4 × 6 = 24 cm.",
                      "(b) 4 cm by 7 cm. Area: 4 × 7 = 28 square cm. Perimeter: 4 + 7 + 4 + 7 = 22 cm.",
                      "(c) 12 cm by 4 cm. Area: 12 × 4 = 48 square cm. Perimeter: 12 + 4 + 12 + 4 = 32 cm.",
                      "(d) 3 cm by 3 cm. Area: 3 × 3 = 9 square cm. Perimeter: 4 × 3 = 12 cm.",
                      "(e) 6 cm by 5 cm. Area: 6 × 5 = 30 square cm. Perimeter: 6 + 5 + 6 + 5 = 22 cm.",
                      "Check: (a) and (d) are squares, so their length and breadth are equal."],
                     "Area, perimeter: (a): 36 square cm, 24 cm; (b): 28, 22; (c): 48, 32; (d): 9, 12; (e): 30, 22.",
                     kind="exercise",
                     q_figure="Five orange shapes labelled (a) to (e) on a grid of 1 cm squares, each with arrows and "
                              "a blank for its length and its breadth: (a) a square 6 wide and 6 tall, (b) 4 wide and "
                              "7 tall, (c) 12 wide and 4 tall, (d) a square 3 wide and 3 tall, (e) 6 wide and 5 tall.",
                     s_figure="The same shapes with the length and the breadth of each filled in beside the arrows.")],
          misconceptions=["M_AREA_IS_PERIM", "M_PERIM_TWO_SIDES", "M_SQUARE_MIX"])],
    key_terms=["rectangle", "square", "area", "perimeter"]))
