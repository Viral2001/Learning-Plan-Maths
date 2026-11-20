# -*- coding: utf-8 -*-
"""Topics T1, T1B, T2 and T3 (module M1: Perimeter, Tiles and Area). The framing intro (Grandmother's quilt hook and the free
Quilt Lace try), the short idea topic T1B (Perimeter: The Border of a Shape with the opener's questions), Covering a
Surface with Tiles, and Comparing Shapes.
Every teaching concept has one worked example with the plan's own numbers; every book question is an FIO item of its
topic's DOER, in the book's order."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Grandmother's Quilt (framing) ===========================================
# The framing topic holds only the hook video and the free-try tool, and no book question. The concept video and the
# opener's questions follow in the short idea topic T1B.
TOPICS.append(TOPIC(
    "T1", "M1", "Grandmother's Quilt", ["Chapter opening"], "Understand",
    "",
    "Grandmother has made a quilt cover and wants to put lace all the way round it. She has three reels of lace. Try "
    "laying each lace round the quilt and find out which one is long enough.",
    [A("T1.C1", "Grandmother's Quilt and the Lace", "Understand",
       "",
       textbook=["Preetha and Adrit's grandmother made a quilt cover using old clothes. Now she wants to decorate it "
                 "with lace."],
       teach=["Predict first: Grandmother has a red reel, a green reel and a blue reel of lace. Which one will go all "
              "the way round the edge of her quilt?",
              "Preetha and Adrit's grandmother made a quilt cover using old clothes.",
              "Now she wants to decorate it with lace, all the way round the edge of the quilt.",
              "Is a short lace enough? Is a long lace enough? Think about it, then try the three laces on the quilt on "
              "the next screen."],
       ncert=["open.story"], key_terms=["quilt", "lace", "border"],
       video_focus=["HOOK"], enrichment=True, minutes=4),
     DOER("T1.C3", "Quilt Lace: Explore", "quilt_lace", "Understand",
          "",
          ["Grandmother has made a quilt cover.",
           "She wants to put lace all the way round its edge.",
           "Lay the laces along the edge, count the units and find out which one is long enough."],
          misconceptions=["M_BORDER_PATCHES"], role="try_it", enrichment=True)],
    topic_type="framing", key_terms=["quilt", "lace", "border"]))

# ============================== T1B Perimeter: The Border of a Shape =======================================
TOPICS.append(TOPIC(
    "T1B", "M1", "Perimeter: The Border of a Shape", ["Chapter opening"], "Understand",
    "Students find the perimeter of a shape by adding the lengths of all its sides, and use it to say how much lace "
    "covers the border of the quilt.",
    "The length of the border of a shape is its perimeter. Walk once round the border and add the length of every "
    "side. When all the sides are equal, count the sides and multiply by one side.",
    [A("T1B.C1", "Perimeter: The Border of a Shape", "Understand",
       "Students find the perimeter of a shape by adding the length of every side, and by multiplying when all the "
       "sides are equal.",
       textbook=["Recall that the length of the border of a shape is called its perimeter."],
       teach=["Predict first: a mat is 8 patches long and 3 patches broad, and each patch side is 1 unit. How much lace "
              "goes all the way round its edge?",
              "The edge of a shape is its border. The length of the border is called the perimeter.",
              "To find it, walk once round the border and add the length of every side. For the mat: 8 + 3 + 8 + 3 = "
              "22, so 22 units of lace.",
              "When all the sides of a shape are equal, count the sides and multiply by one side. A shape with 3 equal "
              "sides of 6 cm has a perimeter of 3 × 6 = 18 cm.",
              "Rule: the perimeter is the length of the whole border, found by adding all the sides."],
       examples=[WE("A mat has 5 equal sides, and each side is 7 cm long. Grandmother wants to sew a lace all the way "
                    "round its border. How long is the lace?",
                    ["The border is the line all the way round the mat, so we add the length of all 5 sides.",
                     "7 + 7 + 7 + 7 + 7 = 35.",
                     "All the sides are equal, so we can also multiply: 5 sides of 7 cm make 5 × 7 = 35.",
                     "Check: adding and multiplying both give 35, so the lace must be 35 cm long."],
                    "The perimeter is 35 cm, so the lace is 35 cm long")],
       ncert=["open.perimeter"], key_terms=["perimeter", "border", "side"],
       misconceptions=["M_BORDER_PATCHES", "M_PERIM_TWO_SIDES"], minutes=5),
     DOER("T1B.C2", "Practice: Perimeter", None, "Understand",
          "Students find the length of lace that covers the border of the quilt and the perimeter of shapes whose "
          "sides are all equal.",
          ["The perimeter is the length of the whole border.",
           "Add the length of every side, one side at a time.",
           "When all the sides are equal, count the sides and multiply."],
          items=[FIO("open.tick", "Grandmother's Quilt: tick the lace",
                     "Preetha and Adrit's grandmother made a quilt cover using old clothes. Now she wants to decorate "
                     "it with lace. Tick the lace option that would cover the entire border of the quilt. (i) Red lace "
                     "40 units (ii) Green lace 50 units (iii) Blue lace 25 units",
                     ["The border is the line all the way round the quilt. Count one unit of lace for each patch side "
                      "along it.",
                      "One long side has 15 patches, so it needs 15 units. One short side has 10 patches, so it needs "
                      "10 units.",
                      "The quilt has 2 long sides and 2 short sides: 15 + 10 + 15 + 10 = 50.",
                      "The border is 50 units long.",
                      "Red lace is 40 units and 40 is less than 50, so it is too short. Blue lace is 25 units and 25 "
                      "is less than 50, so it is too short.",
                      "Green lace is 50 units, exactly the length of the border.",
                      "Check: 2 × 15 = 30, 2 × 10 = 20 and 30 + 20 = 50."],
                     "(ii) Green lace, 50 units, because the border is 15 + 10 + 15 + 10 = 50 units.",
                     kind="prompt",
                     q_figure="A quilt cover made of square patches in rows of green, red and yellow with a pink rim, "
                              "with three lace reels marked (i) red lace 40 units, (ii) green lace 50 units and (iii) "
                              "blue lace 25 units, where each side of a patch is 1 unit.",
                     s_figure="The same quilt with its border outlined and its four sides marked 15, 10, 15 and 10 "
                              "units."),
                 FIO("open.twolaces", "Grandmother's Quilt: two laces",
                     "She decides to use two different coloured laces. How much lace of each kind will be needed to "
                     "cover the entire border?",
                     ["The whole border is 50 units: 15 + 10 + 15 + 10 = 50.",
                      "Use one colour for the two long sides and the other colour for the two short sides.",
                      "The two long sides need 15 + 15 = 30 units. Use 30 units of the red lace, because the red reel "
                      "has 40 units.",
                      "The two short sides need 10 + 10 = 20 units. Use 20 units of the blue lace, because the blue "
                      "reel has 25 units.",
                      "Check: 30 + 20 = 50, the whole border.",
                      "Another split works too: 25 units of blue lace and 25 units of red lace, because 25 + 25 = 50. "
                      "Your answer may differ."],
                     "Sample answer: 30 units of red lace and 20 units of blue lace, because 30 + 20 = 50. Your "
                     "answer may differ.",
                     kind="prompt",
                     q_figure="The same quilt cover with its three lace reels: red lace 40 units, green lace 50 units "
                              "and blue lace 25 units.",
                     s_figure="The quilt with its two long sides in red lace marked 30 units in all and its two short "
                              "sides in blue lace marked 20 units in all."),
                 FIO("LUD1.Q1", "Let Us Do (perimeter), Q1",
                     "Find the perimeter of the following shapes. All sides of the following shapes are equal. (a) the "
                     "shape on the left, with a side of 4 cm; (b) the shape on the right, with a side of 5 cm",
                     ["(a) The shape on the left has 5 sides, and every side is 4 cm.",
                      "Add the sides: 4 + 4 + 4 + 4 + 4 = 20.",
                      "All the sides are equal, so multiply: 5 × 4 = 20. The perimeter is 20 cm.",
                      "(b) The shape on the right has 4 sides, and every side is 5 cm.",
                      "Add the sides: 5 + 5 + 5 + 5 = 20.",
                      "All the sides are equal, so multiply: 4 × 5 = 20. The perimeter is 20 cm.",
                      "Check: for each shape, adding and multiplying give the same number."],
                     "(a): 20 cm; (b): 20 cm",
                     kind="exercise",
                     q_figure="On the left a shape with 5 equal sides and one side marked 4 cm; on the right a shape "
                              "made of a top line marked 5 cm, a bottom line and two lines that cross in the middle, "
                              "with all its sides equal.",
                     s_figure="The two shapes with every side marked: five sides of 4 cm on the left and four sides "
                              "of 5 cm on the right.")],
          misconceptions=["M_BORDER_PATCHES", "M_PERIM_TWO_SIDES"])],
    key_terms=["perimeter", "border", "side"]))

# ============================== T2 Covering a Surface with Tiles ===========================================
TOPICS.append(TOPIC(
    "T2", "M1", "Covering a Surface with Tiles", ["Preetha and Adrit's tables"], "Understand",
    "Students say which shapes cover a surface without gaps and overlaps, and find the area of a region by counting "
    "the tiles that cover it.",
    "A shape tiles a surface when there are no gaps and no overlaps. Squares, rectangles and triangles tile; circles "
    "leave gaps. The region the tiles cover is its area, and it is counted in the tiles used.",
    [A("T2.C1", "Tiles That Cover Without Gaps", "Understand",
       "Students name the shapes that cover a table top without gaps and overlaps and the shape that leaves gaps.",
       textbook=["To find the area of a region, we usually fill it with shapes that tile (no gaps and overlaps), like "
                 "squares, rectangles and triangles."],
       teach=["Predict first: Preetha covers a table top with circles and Adrit covers one with squares. Whose table "
              "top will have gaps?",
              "A tile is a shape used to cover a surface. Tiles must fit together with no gaps and no overlaps.",
              "Squares fit edge to edge with no gaps. Rectangles fit the same way. Triangles fit too: one table top in "
              "your maths book is covered by triangles with no gaps.",
              "Circles do not tile. Between round tiles there are always gaps, and to close the gaps the circles would "
              "have to overlap.",
              "Rule: squares, rectangles and triangles tile a surface; circles leave gaps."],
       examples=[WE("Grandmother wants to cover a tray top with identical tiles. She tries 12 square tiles in 3 rows "
                    "of 4, and 6 round tiles in 2 rows of 3. Which tiles cover the tray with no gaps and no overlaps?",
                    ["Squares first: 3 rows of 4 squares, 3 × 4 = 12 squares.",
                     "The squares meet edge to edge, so there are no gaps and no overlaps: squares tile.",
                     "Now the round tiles: 2 rows of 3 circles, 2 × 3 = 6 circles.",
                     "There are gaps between the circles and at the corners of the tray. Pushing the circles together "
                     "to close the gaps would make them overlap.",
                     "Check: only the squares cover the tray with no gaps and no overlaps."],
                    "The square tiles cover the tray exactly; the round tiles leave gaps")],
       ncert=["tab.story", "tab.tile"], key_terms=["tile", "gap", "overlap"],
       misconceptions=["M_CIRCLE_TILES"], minutes=5),
     A("T2.C2", "Area: The Region Covered", "Understand",
       "Students find the area of a region as the number of tiles that cover it and say it in the unit of the tile.",
       textbook=["The region covered by the triangles, squares or rectangles is called the area of the table."],
       teach=["Predict first: a table top is covered by 20 triangles. What do we call the amount of table top that the "
              "triangles cover?",
              "The region that the tiles cover is called the area. To find the area, count the tiles.",
              "Say the tile in the unit: 20 triangles make an area of 20 triangle units, and 8 squares make an area "
              "of 8 square units.",
              "The same region can be covered with different tiles. Preetha covers her desk with squares, then with "
              "triangles: the triangles are more in number, because each square is cut into 2 triangles.",
              "Rule: the area is the number of tiles that cover the region, counted in the unit of the tile. A "
              "different tile gives a different count."],
       examples=[WE("A tray top is covered by 24 square tiles in 4 rows of 6. Every square is then cut from corner to "
                    "corner into 2 triangles, and the same tray top is covered with the triangles. What is the area "
                    "of the tray top in square units and in triangle units?",
                    ["Count the squares: 4 rows of 6, 4 × 6 = 24 squares. The area is 24 square units.",
                     "Each square makes 2 triangles, so the triangles are 24 × 2 = 48.",
                     "The same tray top is covered by 48 triangles. The area is 48 triangle units.",
                     "The region did not change, only the tile did, so a different tile gives a different count.",
                     "Check: 48 ÷ 2 = 24, so 2 triangles make 1 square."],
                    "The area is 24 square units, which is 48 triangle units")],
       ncert=["tab.areadef", "desk.story"], key_terms=["area", "region", "unit"],
       misconceptions=["M_TILE_COUNT"], minutes=5),
     DOER("T2.C3", "Practice: Tile the Table", "tile_the_table", "Apply",
          "Students count the tiles on the rug, the tables and the desk and say the area in the unit of the tile.",
          ["A tile covers with no gaps and no overlaps.",
           "Count the tiles to find the area, and name the tile in the unit.",
           "A different tile gives a different count for the same region."],
          items=[FIO("rug.patches", "Tiles and Tables: the rug",
                     "Preetha and Adrit's grandmother is making a rug with square patches. The picture below shows "
                     "the rug. How many patches have they used to make this?",
                     ["Look at the rug. The patches are in rows, and every row has the same number of patches.",
                      "Count the rows: there are 6 rows.",
                      "Count the patches in one row: there are 15 patches.",
                      "Add the rows: 15 + 15 + 15 + 15 + 15 + 15 = 90. Or multiply: 6 × 15 = 90.",
                      "Check by columns: there are 15 columns of 6 patches, and 15 × 6 = 90."],
                     "90 patches",
                     kind="prompt",
                     q_figure="A rug made of square patches in alternate red and yellow colours.",
                     s_figure="The same rug with its 6 rows marked and 15 patches in each row."),
                 FIO("tab.shapes", "Tiles and Tables: which shapes cover",
                     "Preetha and Adrit are trying to cover their table with different shapes. Preetha covered it "
                     "with triangles and circles. Adrit covered with squares and rectangles. They found that ___, ___ "
                     "and ___ shapes cover the top of the table without gaps and overlaps. ___ shape leaves gaps.",
                     ["Table 1 is covered by triangles with no gaps and no overlaps.",
                      "Table 3 is covered by squares with no gaps and no overlaps.",
                      "Table 4 is covered by rectangles with no gaps and no overlaps.",
                      "Table 2 is covered by circles, and there are gaps between the circles.",
                      "So triangle, square and rectangle shapes cover the top without gaps and overlaps, and the "
                      "circle shape leaves gaps."],
                     "Triangle, square and rectangle shapes cover the top of the table; the circle shape leaves gaps.",
                     kind="prompt",
                     q_figure="Four table tops: Table 1 covered with triangles, Table 2 with circles, Table 3 with "
                              "squares and Table 4 with rectangles.",
                     s_figure="The four tables with the gaps between the circles of Table 2 shaded orange."),
                 FIO("tab.counts", "Tiles and Tables: how many tiles",
                     "___ triangles cover Table 1. ___ squares cover Table 3. ___ rectangles cover Table 4.",
                     ["Table 1: the triangles come from squares in 5 columns and 2 rows, and each square is cut from "
                      "corner to corner into 2 triangles.",
                      "5 × 2 = 10 squares, and 10 × 2 = 20 triangles.",
                      "Table 3: the squares are in 4 columns and 2 rows, 4 × 2 = 8 squares.",
                      "Table 4: the rectangles are in 3 columns and 4 rows, 3 × 4 = 12 rectangles.",
                      "Check: count each table once more, tile by tile: 20, 8 and 12."],
                     "20 triangles cover Table 1, 8 squares cover Table 3 and 12 rectangles cover Table 4.",
                     kind="prompt",
                     q_figure="The four table tops, each covered with its own tiles.",
                     s_figure="Table 1 with its 20 triangles, Table 3 with its 8 squares and Table 4 with its 12 "
                              "rectangles numbered one by one."),
                 FIO("tab.circles", "Tiles and Tables: do circles tile",
                     "Do circles tile? Can we use them to cover a region?",
                     ["Look at Table 2. It is covered by 8 circles, 4 in a row and 2 rows.",
                      "There are gaps between the circles and at the edges of the table.",
                      "To close the gaps the circles would have to overlap each other.",
                      "A shape tiles only when there are no gaps and no overlaps, so circles do not tile.",
                      "Check: squares, rectangles and triangles left no gaps, but the circles did."],
                     "No. Circles leave gaps, so they do not tile and cannot cover a region without gaps or overlaps.",
                     kind="prompt",
                     q_figure="Table 2 covered with 8 circles in 2 rows of 4.",
                     s_figure="Table 2 with the gaps between the circles shaded orange."),
                 FIO("tab.area", "Tiles and Tables: the area of each table",
                     "The area of Table 1 is ___ triangle units. The area of Table 3 is ___ square units. The area of "
                     "Table 4 is ___ rectangle units.",
                     ["The area is the number of tiles that cover the table, said in the unit of the tile.",
                      "Table 1: 20 triangles cover it, so its area is 20 triangle units.",
                      "Table 3: 8 squares cover it, so its area is 8 square units.",
                      "Table 4: 12 rectangles cover it, so its area is 12 rectangle units.",
                      "Check: the counts 20, 8 and 12 are the same as the tile counts before."],
                     "Table 1: 20 triangle units. Table 3: 8 square units. Table 4: 12 rectangle units.",
                     kind="prompt",
                     q_figure="The four table tops, each covered with its own tiles."),
                 FIO("tab.objects", "Tiles and Tables: cover your own table",
                     "Now, try to cover the top of your table without gaps and overlaps with the following objects of "
                     "same size. (a) Notebooks (b) Lunch boxes (c) Pencil boxes (d) Maths books. Which of the "
                     "above objects covered the region completely?",
                     ["Notebooks, lunch boxes, pencil boxes and maths books are all rectangles. Rectangles tile: they "
                      "fit side by side with no gaps and no overlaps.",
                      "So each of the four objects can cover a table top without gaps and overlaps if you lay it in "
                      "neat rows.",
                      "Whether an object covers the table completely depends on the table: its length and breadth "
                      "must hold a whole number of the objects.",
                      "Sample answer with practice values: a notebook 20 cm long and 15 cm broad, and a table top 60 "
                      "cm long and 30 cm broad.",
                      "Along the length: 60 ÷ 20 = 3 notebooks. Along the breadth: 30 ÷ 15 = 2 notebooks.",
                      "3 × 2 = 6 notebooks cover this table top completely.",
                      "Your answer may differ, because your table and your objects may be different sizes."],
                     "Sample answer: all four, because every one is a rectangle and rectangles tile. Your answer may "
                     "differ.",
                     kind="prompt"),
                 FIO("LUD.desk", "Let Us Do (the desk), Q1",
                     "Preetha is playing with tiles. She covers her desk with different shapes as shown below. Look "
                     "at the different tiles on her desk and answer how many of the following shapes will cover the "
                     "desk. (a) Green triangles ___ (b) Red triangles ___ (c) Blue squares ___",
                     ["Count the squares of the desk: 9 squares in a row and 6 rows, 9 × 6 = 54 squares.",
                      "(a) A green triangle is half a square, so 2 green triangles cover 1 square.",
                      "54 × 2 = 108 green triangles cover the desk.",
                      "(b) 2 red triangles put together make a square 3 squares long and 3 squares broad, which is 9 "
                      "squares.",
                      "The desk holds 9 ÷ 3 = 3 of these big squares in a row and 6 ÷ 3 = 2 rows, so 3 × 2 = 6 big "
                      "squares.",
                      "Each big square is 2 red triangles: 6 × 2 = 12 red triangles cover the desk.",
                      "(c) A blue square is 1 square, so 54 blue squares cover the desk.",
                      "Check: 1 red triangle covers 9 green triangles, and 12 × 9 = 108, the same as the green "
                      "count."],
                     "(a): 108 green triangles; (b): 12 red triangles; (c): 54 blue squares",
                     kind="exercise",
                     q_figure="A desk drawn as a grid of equal squares, with three tiles beside it: a blue square tile "
                              "the size of one grid square, a green triangle tile that is a grid square cut from "
                              "corner to corner, and a red triangle tile whose two shorter sides are each as long as "
                              "3 grid squares.",
                     s_figure="The desk grid, 9 squares in a row and 6 rows, with one big square 3 by 3 split into 2 "
                              "red triangles to show how 6 such squares fill the desk.")],
          misconceptions=["M_CIRCLE_TILES", "M_TILE_COUNT"])],
    key_terms=["tile", "area", "region"]))

# ============================== T3 Comparing Shapes ========================================================
TOPICS.append(TOPIC(
    "T3", "M1", "Comparing Shapes", ["Comparing Shapes"], "Apply",
    "Students compare the areas of shapes by laying one on another and by counting unit squares on a square grid.",
    "If one shape fits inside another, it has the smaller area. When neither fits inside the other, cover both with "
    "the same unit square and count. A square with sides 1 unit has an area of 1 unit square.",
    [A("T3.C1", "Comparing Areas: Which Is Larger?", "Understand",
       "Students compare two areas by laying one shape on the other when one fits inside, and by counting equal "
       "squares when it does not.",
       textbook=["Which of the above rectangles has the largest area? Trace these shapes on to a paper and cut them "
                 "to find out the one that has the largest area."],
       teach=["Predict first: rectangle A is wide and short and rectangle C is narrow and tall. Which one has the "
              "larger area, and how could you find out?",
              "If one shape fits inside the other, the shape that fits inside has the smaller area. Trace it, cut it "
              "out and lay it on the other.",
              "Sometimes neither shape fits inside the other. A is wider but C is taller, so laying one on the other "
              "does not settle it.",
              "Then cover both shapes with the same small square and count the squares. The shape with more squares "
              "has the larger area.",
              "Rule: compare areas by laying one on the other when one fits inside, and by counting equal squares "
              "when it does not."],
       examples=[WE("Mat P is 7 squares long and 2 squares broad. Mat Q is 4 squares long and 4 squares broad. Which "
                    "mat has the larger area?",
                    ["Lay mat Q on mat P. Q is shorter than P in length, but Q is broader. Neither mat fits inside "
                     "the other, so laying them does not settle it.",
                     "Cover both with the same square tiles and count. Mat P has 2 rows of 7 squares: 2 × 7 = 14 "
                     "squares.",
                     "Mat Q has 4 rows of 4 squares: 4 × 4 = 16 squares.",
                     "16 is more than 14, so mat Q has the larger area.",
                     "Check: Q is not the longer mat, yet it has the larger area, so length alone cannot decide."],
                    "Mat Q has the larger area: 16 squares is more than 14 squares")],
       ncert=["cmp.story"], key_terms=["area", "compare", "larger"],
       misconceptions=["M_ONE_SIDE"], minutes=5),
     A("T3.C2", "The Unit Square and Counting Squares", "Understand",
       "Students find the area of a shape on a square grid by counting unit squares, and count two half squares as "
       "one square.",
       textbook=["Using square grids is the most convenient way to find the area of regions. We say that the area of "
                 "a square with sides 1 unit is 1 unit square."],
       teach=["Predict first: a shape on a grid covers 6 whole squares and 4 half squares. How many squares is that in "
              "all?",
              "The most convenient way to find an area is to put the shape on a square grid. A square with sides 1 "
              "unit has an area of 1 unit square.",
              "When the sides are 1 cm, the area of the square is 1 square cm.",
              "The area of a shape is the number of unit squares it covers. Count the whole squares first.",
              "Two half squares together make 1 whole square, so put the half squares in pairs.",
              "We choose a square as the unit because all its sides are equal, just as we measure a length with a "
              "unit of length.",
              "Rule: the area is the number of unit squares that cover the shape, and two half squares make one."],
       examples=[WE("A triangle is drawn on a grid of 1 cm squares. It covers 6 whole squares and 4 half squares. "
                    "What is its area?",
                    ["The area of a square with sides 1 cm is 1 square cm, so each whole square counts 1 square cm.",
                     "Count the whole squares: 6 whole squares are 6 square cm.",
                     "Count the half squares: there are 4, and 2 half squares make 1 whole square, so 4 ÷ 2 = 2 "
                     "whole squares.",
                     "Add: 6 + 2 = 8.",
                     "Check: the 4 half squares match up in 2 pairs, so none is left over."],
                    "The area is 8 square cm")],
       ncert=["sq.unit", "note.unit"], key_terms=["unit square", "square cm", "grid"],
       misconceptions=["M_AREA_UNIT"], minutes=5),
     DOER("T3.C3", "Practice: Grid Area", "grid_area", "Apply",
          "Students compare the areas of rectangles and gardens by counting unit squares on a grid.",
          ["Lay one shape on the other when one fits inside.",
           "When it does not, count the unit squares on a grid.",
           "The area is written in square units, such as square cm."],
          items=[FIO("cmp.largest", "Comparing Shapes: which rectangle is largest",
                     "Which of the above rectangles has the largest area? Trace these shapes on to a paper and cut "
                     "them to find out the one that has the largest area.",
                     ["Trace the three rectangles on paper and cut them out.",
                      "Lay B on A: B fits inside A, so the area of A is larger than the area of B.",
                      "Lay B on C: B fits inside C, so the area of C is larger than the area of B. So B is the "
                      "smallest.",
                      "Lay A on C: neither fits inside the other, because A is wider and C is taller. Cutting alone "
                      "does not tell us.",
                      "Put the rectangles on a square grid and count the unit squares: A has 3 × 4 = 12, C has 2 × 5 "
                      "= 10 and B has 2 × 4 = 8.",
                      "12 is the most, so A has the largest area.",
                      "Check: 12 is more than 10, and 10 is more than 8."],
                     "A has the largest area: 12 unit squares, against 10 for C and 8 for B.",
                     kind="prompt",
                     q_figure="Three rectangles side by side: A yellow, B pink and C purple, with A the widest and C "
                              "the tallest, drawn without a grid.",
                     s_figure="The three rectangles on a square grid with their unit squares counted: A 12, B 8 and C "
                              "10."),
                 FIO("cmp.ab_bc", "Comparing Shapes: A and B, B and C",
                     "Do you see that the area of rectangle A is larger than that of B? What about B and C?",
                     ["Trace and cut out A, B and C. Lay B on A: B fits inside A.",
                      "So A covers more than B: the area of A is larger than the area of B.",
                      "Now lay B on C: B fits inside C.",
                      "So C covers more than B: the area of C is larger than the area of B.",
                      "Check: B fits inside both, so B is smaller than A and smaller than C."],
                     "Yes, A is larger than B because B fits inside A. C is larger than B because B fits inside C.",
                     kind="prompt",
                     q_figure="The same three rectangles side by side: A yellow, B pink and C purple.",
                     s_figure="Rectangle B drawn inside rectangle A, and again inside rectangle C."),
                 FIO("cmp.ac", "Comparing Shapes: A and C",
                     "Which shape has a larger area among A and C? How will you find out?",
                     ["Lay A on C. A is wider than C, but C is taller than A, so neither fits inside the other.",
                      "We cannot tell by laying one on the other, so put both on a square grid.",
                      "Count the unit squares of A: 3 columns and 4 rows, 3 × 4 = 12.",
                      "Count the unit squares of C: 2 columns and 5 rows, 2 × 5 = 10.",
                      "12 is more than 10, so A has the larger area.",
                      "Check: count A row by row: 3 + 3 + 3 + 3 = 12."],
                     "A has the larger area. Put both on a square grid and count: A has 12 unit squares and C has 10.",
                     kind="prompt",
                     q_figure="The same three rectangles side by side: A yellow, B pink and C purple.",
                     s_figure="A and C on a square grid with their unit squares counted: A 12 and C 10."),
                 FIO("cmp.grid", "Comparing Shapes: on a square grid",
                     "Let us put these rectangles on a square grid. Now, can you identify the rectangle that has the "
                     "largest area?",
                     ["On the grid every square is 1 unit square, so the area is the number of squares covered.",
                      "A covers 3 columns and 4 rows: 3 × 4 = 12 squares.",
                      "B covers 2 columns and 4 rows: 2 × 4 = 8 squares.",
                      "C covers 2 columns and 5 rows: 2 × 5 = 10 squares.",
                      "12 is more than 10, and 10 is more than 8, so A has the largest area, then C, then B.",
                      "Check: count A again by columns: 4 + 4 + 4 = 12."],
                     "Yes. A covers 12 unit squares, B covers 8 and C covers 10, so A has the largest area.",
                     kind="prompt",
                     q_figure="The three rectangles A, B and C placed on a square grid, with a key square marked 1 "
                              "unit.",
                     s_figure="The same grid with the squares of A, B and C counted: 12, 8 and 10."),
                 FIO("LUD.garden", "Let Us Do (square grid), Q1",
                     "Compare the areas of the two gardens given below on the square grid. Share your observations. "
                     "Area of Garden A: ___ square cm. Area of Garden B: ___ square cm.",
                     ["Garden A is 2 columns wide and 5 rows tall, so each row has 2 squares.",
                      "5 rows of 2 squares: 5 × 2 = 10. The area of garden A is 10 square cm.",
                      "Garden B is 4 columns wide and 3 rows tall, so each row has 4 squares.",
                      "3 rows of 4 squares: 3 × 4 = 12. The area of garden B is 12 square cm.",
                      "12 is more than 10, so garden B has the larger area, by 12 − 10 = 2 square cm.",
                      "The pale strip is part of neither garden, so it is not counted.",
                      "Check: count garden A square by square: 2, 4, 6, 8, 10."],
                     "Garden A: 10 square cm. Garden B: 12 square cm. Garden B has the larger area.",
                     kind="exercise",
                     q_figure="A grid of 1 cm squares with a green garden A on the left, a pale strip one square "
                              "wide beside it, and a green garden B on the right.",
                     s_figure="The same grid with the squares of garden A and garden B numbered one by one."),
                 FIO("LUD.palm", "Let Us Do (square grid), Q2",
                     "Trace your palm on the square grid given below and find the approximate area of your palm. "
                     "Compare the area of your palm with your friend's palm. Who has a bigger palm?",
                     ["Put your hand flat on the grid and trace round it with a pencil. Each square of the grid is 1 "
                      "square cm.",
                      "Count the whole squares inside the outline.",
                      "Then look at the squares that are only partly inside. Put them together in your mind: two part "
                      "squares make about 1 whole square.",
                      "Add the whole squares and the squares made from the parts. This is the approximate area of your "
                      "palm.",
                      "Do the same for your friend's palm and compare the two numbers: the bigger number is the "
                      "bigger palm.",
                      "Sample answer with practice values: my palm has 54 whole squares and 12 part squares, which "
                      "make about 6 whole squares, so the area is about 54 + 6 = 60 square cm.",
                      "My friend's palm is about 48 square cm. 60 is more than 48, so my palm is bigger. Your answer "
                      "may differ."],
                     "Sample answer: my palm is about 60 square cm and my friend's is about 48 square cm, so my palm "
                     "is bigger. Your answer may differ.",
                     kind="exercise",
                     q_figure="An empty square grid made of 1 cm squares, with room to trace a hand."),
                 FIO("LUD.leaves", "Let Us Do (square grid), Q3",
                     "Collect leaves of different kinds. Put them on a square grid and find their area. (a) Name the "
                     "leaf with the largest area. (b) Name the leaf with the smallest area.",
                     ["Collect a few different leaves and lay each one flat on the square grid. Trace its outline.",
                      "For each leaf count the whole squares inside, then put the part squares together to make about "
                      "whole squares, and add. This gives the area of the leaf.",
                      "Compare the numbers: the leaf with the biggest number has the largest area, and the leaf with "
                      "the smallest number has the smallest area.",
                      "Sample answer with practice values: leaf P is about 30 square cm, leaf Q about 18 square cm and "
                      "leaf R about 24 square cm.",
                      "(a) The largest area is 30 square cm, leaf P.",
                      "(b) The smallest area is 18 square cm, leaf Q.",
                      "Check: 18 is less than 24 and 24 is less than 30. Your answer may differ."],
                     "Sample answer with practice values: (a): leaf P, 30 square cm; (b): leaf Q, 18 square cm. Your "
                     "answer may differ.",
                     kind="exercise")],
          misconceptions=["M_ONE_SIDE", "M_AREA_UNIT"])],
    key_terms=["area", "unit square", "grid"]))
