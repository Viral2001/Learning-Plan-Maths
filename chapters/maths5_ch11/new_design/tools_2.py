# -*- coding: utf-8 -*-
"""Tool specs for T4 and T5 of Class 5 Chapter 11 (Grandmother's Quilt): Shape Builder (area and perimeter side by side)
and Rectangle Maker (area as rows times patches in a row, perimeter as the sum of the four sides). Specs only; the tool
pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds are labelled practice values. One activity at a
time, one instruction at a time, large controls, Back and Next in the same place, visible progress, Hint, Retry and
Reset always present, immediate specific feedback that is never red."""
from topics_common import T

TOOLS = {
    "shape_builder": T(
        "tool_shape_builder", "Shape Builder", "manipulative",
        "Build shapes on a square grid and read the area and the perimeter side by side, to see that shapes with the "
        "same area can have different perimeters, that shapes with the same perimeter can have different areas, and "
        "that a bigger area does not always give a bigger perimeter.",
        "Grandmother's patchwork board, drawn as a warm 3D isometric scene with soft shadows and gentle animation. A big "
        "grid of 15 columns by 12 rows of equal unit squares lies on the table and is the largest thing on screen, with "
        "a box of loose unit patches beside it. Two read-outs sit above the grid: Area, the number of squares inside the "
        "shape, and Perimeter, the number of edges all the way round it, with the outline of the shape drawn thick. A "
        "shelf below the grid keeps up to 3 saved shapes, each with its Area and Perimeter written on it. An "
        "instruction strip at the top shows one sentence in large type, with progress dots under it. Controls: tap a "
        "square to place a patch and tap it again to take it away; drag across squares to place several at once; a "
        "Save shape button that puts the shape on the shelf; a Show outline switch that lights the outer edges one by "
        "one as they are counted; a Clear button; Check, Hint, Undo, Retry (clears the grid of this step), Reset "
        "(clears the grid and the shelf), Back and Next in the same places on every card. Read-outs: Area (squares), "
        "Perimeter (edges), the saved shapes on the shelf, and a card number out of 7.",
        ["Look at a rug of 2 by 3 patches with its Area 6 and its Perimeter 10 shown. "
         "Count the patches inside, then count the edges round the outside, and say which number is which.",
         "Build three rectangles of the same area and read their perimeters, build three "
         "rectangles of the same perimeter and read their areas, and find two shapes where the area goes up and the "
         "perimeter goes down.",
         "Answer the book's own questions: Trisha's two rectangles and her claim, which shapes have "
         "the same area and what their perimeters are, which shapes have the same perimeter and what their areas are, "
         "and drawing different shapes with the same area as the given shape."],
        ["Card 1 (practice values): build a 4 by 4 rectangle, an 8 by 2 rectangle and a 16 by 1 rectangle, and "
         "save each one. What do you notice? Answer: all three have an area of 16 square units, because 4 × 4 = 16, 8 × "
         "2 = 16 and 16 × 1 = 16, but the perimeters are different: 16, 20 and 34 units.",
         "Card 2 (practice values): build a 5 by 5, a 7 by 3 and a 9 by 1 rectangle, and save each one. What "
         "do you notice? Answer: all three have a perimeter of 20 units, because 5 + 5 + 5 + 5 = 20, 7 + 3 + 7 + 3 = "
         "20 and 9 + 1 + 9 + 1 = 20, but the areas are different: 25, 21 and 9 square units.",
         "Card 3 (practice values): build a 1 by 8 rectangle and then a 3 by 3 square. Which number goes up "
         "and which goes down? Answer: the area goes up, from 1 × 8 = 8 to 3 × 3 = 9, and the perimeter goes down, "
         "from 18 to 12. A bigger area does not always give a bigger perimeter.",
         "Challenge: 'Trisha makes these two rectangles. She says, \"I increased the area of my rectangle, and "
         "the perimeter increased.\" Do you think this is always true?' Build her two rectangles, 2 squares by 3 and 3 "
         "squares by 4, and then try 5 by 2 and 4 by 3. Answer: for her rectangles the area grows from 6 to 12 and the "
         "perimeter from 10 to 14, but 5 by 2 and 4 by 3 have areas 10 and 12 and the same perimeter, 14. No, it is "
         "not always true.",
         "Challenge: 'Tick the shapes with the same area. Find the perimeters of these shapes. What do you "
         "notice?' The six shapes (a) to (f) are on the grid. Answer: (a), (b), (c), (d) and (f) have an area of 12 "
         "square cm, and their perimeters are 16, 18, 14, 14 and 26 cm. Shape (e) has an area of 8. The same area can "
         "have different perimeters.",
         "Challenge: 'Tick the shapes with the same perimeter. Find the areas of these shapes. What do you "
         "notice?' The five shapes (a) to (e) are on the grid. Answer: (a) and (b) have a perimeter of 12 cm and (c), "
         "(d) and (e) have a perimeter of 16 cm. Every shape has an area of 7 square cm.",
         "Challenge: 'Draw different shapes having the same area as the given shape. Write the perimeter of "
         "each shape. What do you notice?' The given shape is 9 squares by 2 and has an area of 18. Answer: any shape of "
         "exactly 18 squares is right, for example 6 by 3 with a perimeter of 18 cm, or 18 by 1 with a perimeter of 38 "
         "cm; the given shape has a perimeter of 22 cm. The perimeters are not all the same. Your answer may differ."],
        ["Each patch placed adds 1 to Area, and Perimeter shows the number of outer edges. When a patch is placed the "
         "outline redraws, and the tool says for example: Area 16 and Perimeter 20.",
         "When two saved shapes have the same Area the tool says: Same area, different perimeters. When they have the "
         "same Perimeter it says: Same perimeter, different areas.",
         "When the student builds a shape that does not match the card, a soft amber note says what is off, for "
         "example: This shape has 15 squares. The card asks for 16.",
         "In the Trisha card, after the second pair, the tool says: The area went up from 10 to 12 and the perimeter "
         "stayed 14. So a bigger area does not always give a bigger perimeter.",
         "A wrong tick shows a soft amber note and never a red cross, and it asks the student to count the squares and "
         "the outer edges again."],
        "The student has built shapes of one area with different perimeters and shapes of one perimeter with different "
        "areas, has found a pair where the area goes up and the perimeter goes down, and has answered Trisha's "
        "question, the two Let Us Explore questions and the drawing question with the shapes.",
        ["gridShape", "areaCount", "perimeterCount", "savedShapes", "outlineShown", "ticks", "challengeIndex"],
        ["M_AREA_IS_PERIM", "M_BIGGER_AREA_BIGGER_PERIM", "M_SAME_AREA_SAME_PERIM"],
        ["What does each number count? Area counts the squares inside, and perimeter counts the edges round the "
         "outside.",
         "Count the squares of the shape first, then walk round the outside and count the edges.",
         "Compare the two numbers for each shape. Which one stayed the same and which one changed?",
         "For a 4 by 4 shape: 4 × 4 = 16 squares, and 4 + 4 + 4 + 4 = 16 edges. The tool builds it and counts the "
         "edges so you can see them."]),

    "rectangle_maker": T(
        "tool_rectangle_maker", "Rectangle Maker", "manipulative",
        "Set the length and the breadth of a rectangle and see the patches fill in rows, so that the area is the rows "
        "times the patches in a row (length × breadth), and walk round the border to see that the perimeter is 2 × "
        "length + 2 × breadth, with the square as a rectangle whose sides are equal.",
        "Grandmother's rug frame, drawn as a warm 3D isometric scene with soft shadows and gentle animation. A "
        "rectangular frame on the table is the largest thing on screen, and unit patches are laid in it in rows. The "
        "length and the breadth of the rectangle are set from 1 to 12, and the side labels in cm sit along the edges. "
        "An instruction strip at the top shows one sentence in large type, with progress dots under it. Controls: a "
        "stepper for the length and a stepper for the breadth, each with plus and minus buttons; a Fill rows button "
        "that lays the patches one row at a time; a Walk the border button that sends a small marker round the "
        "rectangle adding the four sides; a Show the rule switch that writes Length × Breadth and 2 × Length + 2 × "
        "Breadth under the read-outs; answer boxes that take a number for a length, a breadth, an area or a perimeter "
        "in the challenge cards; Check, Hint, Undo, Retry (returns the rectangle of this step), Reset (returns the "
        "first rectangle), Back and Next in the same places on every card. Read-outs: the rows of patches (for example "
        "5 rows of 8), Area in square cm, the sum of the four sides while the marker walks, Perimeter in cm, a Square "
        "badge that lights when the length and the breadth are equal, and a card number out of 7.",
        ["Look at 5 rows of 4 patches (practice values) with the count 20 shown. Say how "
         "many rows there are and how many patches are in a row, and how you could find the total without counting "
         "one by one.",
         "Make a rectangle and read its area and perimeter, change one side and watch both "
         "numbers move, make a square, and make a rectangle with a given perimeter and one given side.",
         "Answer the book's own questions: draw two rectangles of the perimeters 26 cm and 18 cm, "
         "find the area and the perimeter of the five shapes on the grid, and find the area of the patchwork of 6 "
         "rows of 4 patches and the area and perimeter of a square with sides of 5 units."],
        ["Card 1 (practice values): make a rectangle with the length 8 and the breadth 5. What are its area and "
         "its perimeter? Answer: 5 rows of 8 patches, 5 × 8 = 40, so the area is 40 square cm. The perimeter is 8 + 5 + "
         "8 + 5 = 26 cm.",
         "Card 2 (practice values): change the breadth of that rectangle to 6. What happens to the area and the "
         "perimeter? Answer: the area becomes 8 × 6 = 48 square cm and the perimeter becomes 8 + 6 + 8 + 6 = 28 cm. "
         "Both numbers change.",
         "Card 3 (practice values): make a square with a side of 9. What are its area and its perimeter? "
         "Answer: the Square badge lights, because the length and the breadth are equal. The area is 9 × 9 = 81 square "
         "cm and the perimeter is 4 × 9 = 36 cm.",
         "Card 4 (practice values): make a rectangle with a perimeter of 20 cm and a length of 7 cm. What is "
         "its breadth? Answer: half of 20 is 10, and 7 + 3 = 10, so the breadth is 3 cm. Check: 2 × 7 = 14, 2 × 3 = 6 "
         "and 14 + 6 = 20.",
         "Challenge: 'Draw two rectangles each having the following perimeters. (a) 26 cm (b) 18 cm.' Make "
         "two different rectangles for each perimeter. Answer: for (a) the length and the breadth must add to 13, for "
         "example 8 by 5 and 10 by 3; for (b) they must add to 9, for example 6 by 3 and 7 by 2. Your answer may "
         "differ.",
         "Challenge: 'Find the area and perimeter of the following shapes.' The five shapes (a) to (e) are on "
         "the grid with a blank for the length and the breadth of each. Answer: (a) 6 by 6, area 36 square cm, "
         "perimeter 24 cm; (b) 4 by 7, area 28 square cm, perimeter 22 cm; (c) 12 by 4, area 48 square cm, perimeter 32 "
         "cm; (d) 3 by 3, area 9 square cm, perimeter 12 cm; (e) 6 by 5, area 30 square cm, perimeter 22 cm.",
         "Challenge: the patchwork of 6 rows of 4 patches, and a square whose sides are 5 units long. Find "
         "the area of the patchwork, and the area and the perimeter of the square. Answer: 6 × 4 = 24 patches, so the "
         "area is 24 square cm; the square has an area of 5 × 5 = 25 square cm and a perimeter of 4 × 5 = 20 cm."],
        ["Fill rows lays the patches one row at a time and the read-out says for example 5 rows of 8 patches, 5 × 8 = "
         "40. The area is shown in square cm.",
         "Walk the border adds the sides as the marker passes them and says for example 8 + 5 + 8 + 5 = 26 cm.",
         "When the length and the breadth are equal the Square badge lights and the tool says: A square has equal "
         "sides, so the area is Length × Length and the perimeter is 4 × Length.",
         "A wrong number in an answer box shows a soft amber note, for example: The two long sides and the two short "
         "sides must all be added. The tool names the number it expected only after the second try.",
         "A wrong tick or a wrong rectangle never shows a red cross; the tool asks the student to fill the rows or "
         "walk the border again."],
        "The student has made rectangles and read both numbers, has changed a side and watched both numbers move, has "
        "made a square, has found a rectangle of a given perimeter, and has answered the book's questions about the "
        "rectangles of 26 cm and 18 cm, the five shapes, the patchwork and the square.",
        ["lengthValue", "breadthValue", "rowsFilled", "borderWalked", "ruleShown", "squareBadge", "challengeIndex"],
        ["M_AREA_IS_PERIM", "M_PERIM_TWO_SIDES", "M_SQUARE_MIX", "M_AREA_UNIT"],
        ["Is the question about the patches inside, or the edge all the way round? Area is inside, perimeter is "
         "round.",
         "For the area, count the rows and the patches in one row, and multiply. For the perimeter, add all four "
         "sides.",
         "The opposite sides of a rectangle are equal, so the perimeter is 2 × length + 2 × breadth. Half of the "
         "perimeter is length + breadth.",
         "For a rectangle 8 by 5: 5 × 8 = 40 for the area, and 8 + 5 + 8 + 5 = 26 for the perimeter. The tool fills the "
         "first row and walks the first side so you can see it."]),
}
