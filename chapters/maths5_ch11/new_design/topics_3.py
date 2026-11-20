# -*- coding: utf-8 -*-
"""Topics T6, T7 and T8: Using the Area and Perimeter Rules (T6, module M2: a missing side, a side given in parts and the
book's objects, field, garden and figure), Let Us Play: Perimeter of Tiles (T7, module M3: counting the outer edges of
tiles with the book's perimeter 24 game) and the Chapter Revision summary (T8, module M3).
Every teaching concept has one worked example with the plan's own numbers; every book question is an FIO item of its
topic's DOER, in the book's order."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T6 Using the Area and Perimeter Rules ======================================
TOPICS.append(TOPIC(
    "T6", "M2", "Using the Area and Perimeter Rules", ["Let Us Do"], "Apply",
    "Students use the area rule to find a missing side and the area of a figure whose side is marked in parts, and "
    "find the area and perimeter of real objects.",
    "The area rule can be used backwards: the breadth is the area divided by the length. When a side of a figure is "
    "marked in parts, add the parts to get the whole side and then multiply.",
    [A("T6.C1", "Finding a Missing Side", "Apply",
       "Students find the breadth of a rectangle from its area and its length by dividing.",
       teach=["Predict first: a rectangular lawn has an area of 72 square m and a length of 9 m. How can you find its "
              "breadth?",
              "We know that the area is length × breadth. So 9 times the breadth must be 72: some number times 9 "
              "makes 72.",
              "To find that number, divide the area by the length: breadth = area ÷ length.",
              "Check the answer by multiplying back: length × breadth must give the area.",
              "Rule: breadth = area ÷ length, and length = area ÷ breadth."],
       examples=[WE("A rectangular lawn has an area of 72 square m and a length of 9 m. What is its breadth?",
                    ["Area = Length × Breadth, so 9 times the breadth is 72.",
                     "Find the breadth by dividing the area by the length: 72 ÷ 9 = 8.",
                     "Check by multiplying back: 9 × 8 = 72, which is the area.",
                     "The breadth is 8 m."],
                    "The breadth is 8 m")],
       key_terms=["area", "breadth", "length"], misconceptions=["M_AREA_IS_PERIM"], minutes=5),
     A("T6.C2", "A Side Given in Parts", "Apply",
       "Students find the area of a rectangle whose side is marked in two parts by adding the parts first.",
       teach=["Predict first: the height of a rectangle is marked in two parts, 5 cm and 7 cm. What is the whole "
              "height?",
              "The two parts together make the whole side, so add them: 5 + 7 = 12 cm.",
              "Then use the area rule with the whole sides: area = length × breadth.",
              "You can check by finding the area of each part and adding: the parts of the area add up to the whole "
              "area.",
              "Rule: when a side is marked in parts, add the parts to get the whole side, then multiply."],
       examples=[WE("A rectangle is 20 cm wide. Its height is marked in two parts, 5 cm and 7 cm. Find the area of the "
                    "rectangle.",
                    ["The whole height is the two parts added: 5 + 7 = 12 cm.",
                     "Area = Length × Breadth = 20 × 12 = 240 square cm.",
                     "Check by parts: the upper part has an area of 20 × 5 = 100 and the lower part has an area of "
                     "20 × 7 = 140.",
                     "100 + 140 = 240, the same area."],
                    "The area is 240 square cm")],
       key_terms=["area", "side", "parts"], misconceptions=["M_AREA_IS_PERIM"], minutes=5),
     DOER("T6.C3", "Practice: Using the Rules", None, "Apply",
          "Students find the area and perimeter of objects they measure, using the rules for area and perimeter, and "
          "the area of a field, a missing breadth and the area of a figure with a side marked in parts.",
          ["Area is length × breadth; perimeter is 2 × length + 2 × breadth.",
           "To find a missing side, divide the area by the side you know.",
           "When a side is marked in parts, add the parts first."],
          items=[FIO("LUD.objects", "Let Us Do (using the rules), Q3",
                     "Find the area and perimeter of the following objects. Use a scale or measuring tape to find the "
                     "length and the breadth of each of the objects. Objects: Cover of the Notebook; Newspaper; "
                     "Blackboard; Ludo board; and two more objects of your own choice.",
                     ["For each object measure the length and the breadth with a scale or a measuring tape. Small "
                      "objects are measured in centimetres and big ones in metres.",
                      "Area = Length × Breadth, in square cm or square m. Perimeter = 2 × Length + 2 × Breadth, in "
                      "centimetres or metres.",
                      "Sample answer with practice values. Notebook cover, 24 cm by 18 cm: area 24 × 18 = 432 square "
                      "cm; perimeter 2 × 24 = 48, 2 × 18 = 36 and 48 + 36 = 84 cm.",
                      "Newspaper, 60 cm by 40 cm: area 60 × 40 = 2400 square cm; perimeter 2 × 60 = 120, 2 × 40 = 80 "
                      "and 120 + 80 = 200 cm.",
                      "Blackboard, 3 m by 1 m: area 3 × 1 = 3 square m; perimeter 2 × 3 = 6, 2 × 1 = 2 and 6 + 2 = 8 m.",
                      "Ludo board, 40 cm by 40 cm, a square: area 40 × 40 = 1600 square cm; perimeter 4 × 40 = 160 cm.",
                      "Rows 5 and 6: choose two objects of your own and do the same.",
                      "Check each perimeter by adding the four sides, for example 24 + 18 + 24 + 18 = 84. Your answer "
                      "may differ."],
                     "Sample answer with practice values: a notebook cover 24 cm by 18 cm has an area of 432 square "
                     "cm and a perimeter of 84 cm. Your answer may differ.",
                     kind="exercise",
                     q_figure="A table with the columns Name of the objects, Area and Perimeter, and the rows Cover of "
                              "the Notebook, Newspaper, Blackboard and Ludo board, and two empty rows."),
                 FIO("LUD.field", "Let Us Do (using the rules), Q4",
                     "Find the area of a rectangular field whose length is 42 m and breadth is 34 m.",
                     ["The area of a rectangle is Length × Breadth.",
                      "The length is 42 m and the breadth is 34 m, so the area is 42 × 34.",
                      "42 × 30 = 1260.",
                      "42 × 4 = 168.",
                      "1260 + 168 = 1428.",
                      "The area of the field is 1428 square m.",
                      "Check: 34 × 40 = 1360 and 34 × 2 = 68, and 1360 + 68 = 1428."],
                     "1428 square m",
                     kind="exercise"),
                 FIO("LUD.garden64", "Let Us Do (using the rules), Q5",
                     "The area of a rectangular garden is 64 square m and its length is 16 m. What is its breadth?",
                     ["The area of a rectangle is Length × Breadth.",
                      "The area is 64 square m and the length is 16 m, so 16 times the breadth is 64.",
                      "Find the breadth by dividing the area by the length: 64 ÷ 16 = 4.",
                      "The breadth is 4 m.",
                      "Check by multiplying back: 16 × 4 = 64, which is the area."],
                     "4 m",
                     kind="exercise"),
                 FIO("LUD.figure", "Let Us Do (using the rules), Q6",
                     "Find the area of the following figure with the dimensions as marked in the figure.",
                     ["The figure is one rectangle. Its width is 32 cm.",
                      "Its height is marked in two parts, 6 cm and 12 cm. Add them: 6 + 12 = 18 cm.",
                      "Area = Length × Breadth = 32 × 18.",
                      "32 × 10 = 320 and 32 × 8 = 256.",
                      "320 + 256 = 576. The area is 576 square cm.",
                      "Check by parts: 32 × 6 = 192 and 32 × 12 = 384, and 192 + 384 = 576."],
                     "576 square cm",
                     kind="exercise",
                     q_figure="One rectangle with 32 cm marked along its top; on its left side an arrow marked 6 cm "
                              "from the top edge to a dotted line and an arrow marked 12 cm from that dotted line to "
                              "the bottom edge, with the dotted lines inside carrying no numbers.",
                     s_figure="The same figure with the whole height 6 + 12 = 18 cm written on its left side.")],
          misconceptions=["M_AREA_UNIT", "M_AREA_IS_PERIM"])],
    key_terms=["area", "perimeter", "breadth"]))

# ============================== T7 Let Us Play: Perimeter of Tiles =========================================
TOPICS.append(TOPIC(
    "T7", "M3", "Let Us Play: Perimeter of Tiles", ["Let Us Play"], "Apply",
    "Students find the perimeter of a figure of square tiles by counting its outer edges and plan where to add tiles "
    "to reach a perimeter of 24.",
    "The perimeter of a figure of square tiles is the number of its outer edges. A tile added along one edge makes "
    "the perimeter 2 more. A tile added in a corner where it touches two edges leaves the perimeter the same.",
    [A("T7.C1", "Counting the Outer Edges of Tiles", "Apply",
       "Students find the perimeter of a figure of square tiles by counting its outer edges and say how adding a tile "
       "changes it.",
       textbook=["Take some square tiles and a die and play the game in pairs.",
                 "Do not move the tiles. The second player can take turn and add tiles to the same tiled figure."],
       teach=["Predict first: two square tiles are joined along one edge, and each tile side is 1. How many outer edges "
              "does the figure have?",
              "Every side of a tile is 1 unit long. The perimeter of a figure of tiles is the number of outer edges, "
              "the edges that are not shared with another tile.",
              "Two tiles have 4 + 4 = 8 edges in all. The 2 edges where they touch are inside, so there are 8 − 2 = 6 "
              "outer edges and the perimeter is 6.",
              "When you add a tile that touches the figure along 1 edge, the perimeter becomes 2 more. When the tile "
              "sits in a corner and touches 2 edges, the perimeter stays the same.",
              "Rule: the perimeter of a figure of tiles is the number of its outer edges."],
       examples=[WE("Five square tiles are placed like the letter L: 3 tiles in the top row and 2 more tiles below the "
                    "left tile. Each tile side is 1. Find the perimeter. Then say what happens when one more tile is "
                    "added at the end of the top row, and when one is added in the corner where the two arms meet.",
                    ["Count the outer edges of each tile. The left tile of the top row has 2 outer edges, the middle "
                     "tile 2 and the right tile 3.",
                     "Of the two lower tiles, the upper one has 2 outer edges and the lowest has 3.",
                     "Add: 2 + 2 + 3 + 2 + 3 = 12. The perimeter is 12.",
                     "A tile added at the end of the top row touches the figure along 1 edge, so the perimeter becomes "
                     "2 more: 12 + 2 = 14.",
                     "A tile added in the corner where the arms meet touches 2 edges, so the perimeter stays 12.",
                     "Check: counting the outer edges again, one by one, gives 12."],
                    "The perimeter is 12; one more tile at the end makes it 14, and one in the corner leaves it 12")],
       ncert=["play.rules"], key_terms=["perimeter", "tile", "outer edge"],
       misconceptions=["M_ADD_TILE"], minutes=6),
     DOER("T7.C2", "Practice: Perimeter 24 Game", "perimeter_game", "Apply",
          "Students find the perimeter of a figure of tiles and say how adding tiles gets to a perimeter of 24.",
          ["The perimeter of tiles is the number of outer edges.",
           "A tile along 1 edge adds 2; a tile in a corner touching 2 edges adds nothing.",
           "The player who makes the perimeter exactly 24 wins."],
          items=[FIO("play.perimeter", "Let Us Play: find the perimeter of the tiles",
                     "Find the perimeter of the tiles.",
                     ["Each side of a tile is 1. The perimeter is the number of outer edges.",
                      "Count along the top: the 3 tiles of the top row show 3 outer edges.",
                      "Count down the right side of the top row: 1 outer edge.",
                      "Count under the top row, along the two tiles on the right: 2 outer edges.",
                      "Count the edge on the right of the lower tile and the edge under it: 1 + 1 = 2 outer edges.",
                      "Count the left side of both tiles: 2 outer edges.",
                      "Add: 3 + 1 + 2 + 2 + 2 = 10. The perimeter of the tiles is 10.",
                      "Check: 4 tiles have 4 × 4 = 16 edges in all, and the 3 places where tiles touch hide 2 edges "
                      "each, 3 × 2 = 6, so 16 − 6 = 10."],
                     "10",
                     kind="prompt",
                     q_figure="4 square tiles joined edge to edge: a row of 3 tiles and one tile below the left tile, "
                              "each tile side being 1.",
                     s_figure="The same tiles with every outer edge marked 1 and the total 10 written beside them."),
                 FIO("play.win", "Let Us Play: perimeter 24",
                     "Take turns and add tiles to the same figure till the perimeter becomes 24. The one who makes "
                     "the perimeter 24 wins the game.",
                     ["Start with the 4 tiles from before: the perimeter is 10.",
                      "Player 1 rolls a 1 and adds 1 tile that touches the figure along 1 edge. The perimeter becomes "
                      "2 more: 10 + 2 = 12, with 5 tiles.",
                      "Player 2 rolls a 6 and adds 6 tiles to the same figure, without moving any tile. The figure now "
                      "has 11 tiles.",
                      "Count the edges of 11 tiles: 11 × 4 = 44.",
                      "10 places where tiles touch each hide 2 edges: 10 × 2 = 20.",
                      "The perimeter is 44 − 20 = 24.",
                      "Player 2 has made the perimeter exactly 24, so Player 2 wins. Your game may go differently. "
                      "Your answer may differ."],
                     "Sample play: the perimeter goes 10, then 12 with one more tile, then 24 with six more tiles (11 "
                     "tiles). Your answer may differ.",
                     kind="prompt",
                     q_figure="A figure of 5 square tiles, with a die showing 6 beside it.",
                     s_figure="The figure grown to 11 tiles with every outer edge marked 1 and the total 24 written "
                              "beside it.")],
          misconceptions=["M_ADD_TILE"])],
    key_terms=["perimeter", "tile", "outer edge"]))

# ============================== T8 Chapter Revision (summary) ==============================================
TOPICS.append(TOPIC(
    "T8", "M3", "Chapter Revision: Grandmother's Quilt", ["Chapter summary"], "Understand",
    "",
    "The chapter's ideas in one walk through the patchwork room: the quilt border and perimeter, tiles and area, "
    "comparing areas and the unit square, area and perimeter as different measures, the rectangle and square rules, "
    "the missing side, and the tile game.",
    [A("T8.C1", "Chapter Revision: Grandmother's Quilt", "Understand",
       "",
       teach=["Predict first: you have walked through the whole patchwork room. Can you say one idea from each stop, "
              "from the quilt border to the tile game? Read the lines below and tick each idea you remembered.",
              "Perimeter: the length of the whole border of a shape, found by adding all its sides. A quilt 15 patches "
              "long and 10 patches broad has a border of 15 + 10 + 15 + 10 = 50 units.",
              "Check: a shape with 3 equal sides of 6 cm has a perimeter of 3 × 6 = 18 cm.",
              "Tiles and area: tiles cover with no gaps and no overlaps. Squares, rectangles and triangles tile; "
              "circles leave gaps. The area is the number of tiles that cover the region, in the unit of the tile.",
              "Check: 24 square tiles cover a tray. Cut each one into 2 triangles and 48 triangles cover the same "
              "tray, because 24 × 2 = 48.",
              "Comparing and the unit square: if one shape fits inside the other it has the smaller area. If not, "
              "count unit squares on a grid. The area of a square with sides 1 cm is 1 square cm, and 2 half squares "
              "make 1 square.",
              "Check: 7 × 2 = 14 and 4 × 4 = 16, so a 4 by 4 square has a larger area than a 7 by 2 rectangle.",
              "Area and perimeter are different measures. Shapes with the same area can have different perimeters: "
              "16 squares as 4 by 4, 8 by 2 and 16 by 1 have perimeters 16, 20 and 34.",
              "Check: shapes with the same perimeter can have different areas. With a perimeter of 20 units, a 5 by 5 "
              "square has area 25 and a 9 by 1 strip has area 9.",
              "Rectangle: area = length × breadth and perimeter = 2 × length + 2 × breadth. For 8 by 5: the area is "
              "8 × 5 = 40 square cm and the perimeter is 8 + 5 + 8 + 5 = 26 cm.",
              "Square: area = length × length and perimeter = 4 × length. For a side of 7 cm: the area is 7 × 7 = 49 "
              "square cm and the perimeter is 4 × 7 = 28 cm.",
              "Missing side: breadth = area ÷ length. A lawn of area 72 square m and length 9 m has a breadth of 72 ÷ "
              "9 = 8 m. When a side is marked in parts, add the parts first.",
              "Tiles and the game: the perimeter of a figure of tiles is the number of its outer edges. A tile added "
              "along 1 edge makes the perimeter 2 more, and a tile in a corner touching 2 edges leaves it the same.",
              "Check: 5 tiles placed like the letter L have a perimeter of 12, and one more tile at the end of the top "
              "row makes it 14."],
       ncert=["summary"], key_terms=["perimeter", "area", "unit square"], minutes=6, enrichment=True)],
    topic_type="summary"))
