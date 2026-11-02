# -*- coding: utf-8 -*-
"""Topics T11 to T14 (module M4: tiling; module M5: summary). Book section 6.2 and the chapter summary."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T11 Tiling grids with 2 x 1 tiles ============================================
TOPICS.append(TOPIC(
    "T11", "M4", "Tiling Grids with 2 × 1 Tiles", ["6.2"], "Analyze",
    "Students define tiling, tile 4 × 6 and 4 × 7 grids with 2 × 1 tiles, prove that a 5 × 7 grid cannot be tiled "
    "by counting squares, and decide for any m × n grid when tiling is possible.",
    "Each 2 × 1 tile covers two squares, so an odd number of squares can never be tiled; an even side makes it easy.",
    [A("T11.C1", "What tiling means: 4 × 6 and 4 × 7 grids", "Apply",
       "Students state what a tiling is and tile 4 × 6 and 4 × 7 grids with vertical and horizontal 2 × 1 tiles.",
       textbook=["6.2 Tiling",
                 "Covering a region using a set of shapes, without gaps or overlaps, is called tiling.",
                 "Consider a rectangular grid made of unit squares. We call this a 4 × 6 grid, since it has 4 rows "
                 "and 6 columns.",
                 "Can a 4 × 6 grid be tiled using multiple copies of 2 × 1 tiles? We are allowed to rotate a 2 × 1 "
                 "tile and use it. (Vertical tile, horizontal tile.)",
                 "Here is one way. This is not the only tiling possible.",
                 "Can a 4 × 7 grid be tiled using 2 × 1 tiles?"],
       teach=["Predict first: a tile covers two squares. How many tiles would a 4 × 6 grid need?",
              "Tiling means covering the whole region with no gaps and no overlaps.",
              "4 rows is even, so each column fills with 2 vertical tiles.",
              "The same works for 4 × 7: each of the 7 columns takes 2 vertical tiles."],
       examples=[
           WE("Can a 4 × 6 grid be tiled with 2 × 1 tiles? Show one way.",
              ["The grid has 4 × 6 = 24 unit squares, and each tile covers 2, so 12 tiles are needed.",
               "Each column has 4 squares, one above another.",
               "Two vertical tiles cover one column exactly.",
               "Do this for all 6 columns: 6 × 2 = 12 tiles, with no gap and no overlap."],
              "Yes: 12 vertical tiles, 2 in each column",
              ncert=["6.2.tiling_def", "6.2.grid_4x6"]),
           WE("Can a 4 × 7 grid be tiled with 2 × 1 tiles?",
              ["The grid has 4 × 7 = 28 unit squares, an even number, so 14 tiles would be needed.",
               "Each of the 7 columns has 4 squares.",
               "Two vertical tiles cover each column.",
               "7 columns use 7 × 2 = 14 tiles, with no gap and no overlap."],
              "Yes: 14 vertical tiles, 2 in each column",
              ncert=["6.2.grid_4x7"])],
       key_terms=["tiling", "grid"], misconceptions=["M_EVEN_ENOUGH"], minutes=10),
     A("T11.C2", "Why a 5 × 7 grid cannot be tiled", "Analyze",
       "Students complete the counting argument that a 5 × 7 grid cannot be tiled with 2 × 1 tiles.",
       textbook=["What about a 5 × 7 grid?",
                 "To see that there is no way to tile a 5 × 7 grid using 2 × 1 tiles, observe that this grid has 35 "
                 "unit squares. Each tile covers exactly 2 unit squares. Complete the justification."],
       teach=["Predict first: can you tile 5 × 7 by trying for long enough?",
              "Count the squares: 5 × 7 = 35.",
              "Any number of tiles covers 2, 4, 6, and so on squares: always an even number.",
              "35 is odd, so no tiling exists; one square would always be left over."],
       examples=[
           WE("Prove that a 5 × 7 grid cannot be tiled with 2 × 1 tiles.",
              ["The grid has 5 × 7 = 35 unit squares.",
               "Each tile covers exactly 2 unit squares, with no overlap.",
               "So any number of tiles covers an even number of squares.",
               "35 is odd, so it is not a number of squares that tiles can cover exactly.",
               "So there is no tiling of the 5 × 7 grid."],
              "Not possible: tiles always cover an even number of squares, and 35 is odd",
              ncert=["6.2.grid_5x7"])],
       key_terms=["odd", "even"], minutes=8),
     A("T11.C3", "Which m × n grids can be tiled?", "Analyze",
       "Students decide whether an m × n grid can be tiled with 2 × 1 tiles when both sides are even, one is even, "
       "or both are odd, and give a strategy or a reason.",
       textbook=["Is an m × n grid tileable with 2 × 1 tiles, if both m and n are even? If yes, come up with a "
                 "general strategy to tile it.",
                 "One general strategy for this case is to cover each column with vertical tiles. This is possible "
                 "because the number of rows is even.",
                 "Is an m × n grid tileable with 2 × 1 tiles, if one of m and n is even and the other is odd? If "
                 "yes, come up with a general strategy to tile it.",
                 "Is an m × n grid tileable with 2 × 1 tiles, if both m and n are odd? Give reasons."],
       teach=["Predict first: which matters more, the number of rows or the number of columns?",
              "If the number of rows is even, every column fills with vertical tiles.",
              "If only the number of columns is even, every row fills with horizontal tiles.",
              "If both are odd, m × n is odd, so it can never be tiled."],
       examples=[
           WE("Is an m × n grid tileable with 2 × 1 tiles if both m and n are even? Give a strategy.",
              ["Each column has m squares, and m is even.",
               "Cover each column with m ÷ 2 vertical tiles.",
               "Every column is covered, so the whole grid is covered with no gaps or overlaps.",
               "For example, a 6 × 4 grid uses 3 vertical tiles in each of 4 columns, 12 tiles in all."],
              "Yes: cover each column with vertical tiles",
              ncert=["6.2.mn_even"]),
           WE("Is an m × n grid tileable with 2 × 1 tiles if one of m and n is even and the other is odd? Give a "
              "strategy.",
              ["If the number of rows m is even, cover each column with vertical tiles, as before.",
               "If instead the number of columns n is even, each row has an even number of squares.",
               "Then cover each row with n ÷ 2 horizontal tiles.",
               "For example, a 3 × 4 grid: each of the 3 rows takes 2 horizontal tiles, 6 tiles in all."],
              "Yes: use vertical tiles along the even side's columns, or horizontal tiles along rows of even length",
              ncert=["6.2.mn_mixed"]),
           WE("Is an m × n grid tileable with 2 × 1 tiles if both m and n are odd? Give reasons.",
              ["The number of unit squares is m × n.",
               "An odd number times an odd number is odd, for example 3 × 5 = 15.",
               "Each tile covers 2 squares, so tiles always cover an even number of squares.",
               "An odd number of squares can never be covered exactly."],
              "No: m × n is odd, and tiles always cover an even number of squares",
              ncert=["6.2.mn_odd"])],
       key_terms=["m × n grid"], misconceptions=["M_EVEN_ENOUGH"], minutes=12),
     DOER("T11.C4", "Practice: tile grids or prove it impossible", "domino_grid", "Analyze",
          "Students tile grids of different sizes with 2 × 1 tiles, or show by counting that a grid cannot be "
          "tiled.",
          ["Tiling means no gaps and no overlaps.",
           "An even side lets every column, or every row, fill with tiles.",
           "If both sides are odd, the number of squares is odd, so no tiling exists."])]))

# ============================== T12 Colouring argument =======================================================
TOPICS.append(TOPIC(
    "T12", "M4", "Missing Squares and the Colouring Argument", ["6.2"], "Analyze",
    "Students tile a 5 × 3 grid with one square removed where possible, and use a black-and-white colouring to "
    "prove that some regions with an even number of squares can never be tiled.",
    "Every 2 × 1 tile covers one black and one white square, so a region with unequal counts cannot be tiled.",
    [A("T12.C1", "A 5 × 3 grid with one square removed", "Apply",
       "Students tile a 5 × 3 grid with a corner square removed, and with the middle square of the second row removed, using 7 tiles.",
       textbook=["Here is a 5 × 3 grid, with a unit square removed. Now, it has an even number of unit squares. Is it "
                 "tileable with 2 × 1 tiles?",
                 "Is the following region tileable with 2 × 1 tiles?"],
       teach=["Predict first: 14 squares is even. Is that enough to be sure it can be tiled?",
              "Try it: place tiles one at a time, starting from a corner, where a tile can go in only two ways.",
              "With the top right corner removed, the grid can be tiled with 7 tiles.",
              "With the middle square of row 2 removed, it can also be tiled with 7 tiles."],
       examples=[
           WE("A 5 × 3 grid (5 rows, 3 columns) has its top right square removed. Can the remaining 14 squares be "
              "tiled with 2 × 1 tiles?",
              ["14 squares would need 7 tiles.",
               "Top row: the two squares left form one horizontal tile.",
               "Rows 2 and 3: put a vertical tile in each of the 3 columns.",
               "Rows 4 and 5: put a vertical tile in each of the 3 columns.",
               "That is 1 + 3 + 3 = 7 tiles, with no gaps and no overlaps."],
              "Yes: 1 horizontal tile in the top row and 6 vertical tiles below",
              ncert=["6.2.minus_corner"]),
           WE("A 5 × 3 grid has the middle square of its second row removed. Can the remaining squares be tiled "
              "with 2 × 1 tiles?",
              ["14 squares would need 7 tiles.",
               "Row 1: the left two squares form one horizontal tile.",
               "The top right square goes with the square below it: one vertical tile.",
               "The left square of row 2 goes with the left square of row 3: one vertical tile.",
               "The middle and right squares of row 3 form one horizontal tile.",
               "Rows 4 and 5: one vertical tile in each of the 3 columns.",
               "That is 4 tiles above and 3 tiles below, 7 tiles with no gaps and no overlaps."],
              "Yes: a tiling with 7 tiles exists",
              ncert=["6.2.minus_middle"])],
       key_terms=["unit square"], misconceptions=["M_EVEN_ENOUGH"], minutes=10),
     A("T12.C2", "Colour the squares: black and white must match", "Analyze",
       "Students colour a grid like a chessboard, compare black and white counts to prove a region cannot be "
       "tiled, and find other squares whose removal makes a 5 × 3 grid non-tileable.",
       textbook=["What about this one? Were you able to tile this? How can we be sure that this is not tileable?",
                 "Can you find another unit square that, when removed from a 5 × 3 grid, makes it non-tileable?",
                 "There is an interesting way to look at these questions. For any tiling problem of this kind, we can "
                 "create a similar problem with the unit squares coloured black and white so that black squares have "
                 "only white neighbours and white squares have only black neighbours.",
                 "In the black-and-white region, the problem is to tile the region with the 2 × 1 black-and-white "
                 "tiles so that each black square of a tile sits on a black square of the grid, and each white "
                 "square sits on a white square.",
                 "If the plain grid is tileable, is the black-and-white-grid tileable? If the black-and-white grid "
                 "is tileable, is the plain grid tileable? It can be seen that the answer to both the questions is "
                 "yes.",
                 "Is the black-and-white region tileable?",
                 "Any region tiled with black-and-white-tiles must have an equal number of black tiles and white "
                 "tiles.",
                 "Since the black-and-white region has 8 white squares and 6 black squares, it can never be tiled "
                 "with these tiles!",
                 "Use this idea to find another unit square that, when removed from a 5 × 3 grid, makes it "
                 "non-tileable?",
                 "Isn't it surprising how, by introducing colours and making the problem more complicated, it "
                 "becomes easier to tackle? What a creative way of looking at the problem!"],
       teach=["Predict first: the grid with the top middle square removed has 14 squares. Can it be tiled?",
              "Colour the grid like a chessboard, with the corners white: 8 white and 7 black squares.",
              "A 2 × 1 tile always covers two neighbouring squares, one white and one black.",
              "Remove a black square and 8 white and 6 black are left; 7 tiles would need 7 of each, so it is "
              "impossible."],
       examples=[
           WE("A 5 × 3 grid has the middle square of its top row removed. Colour it like a chessboard with white "
              "corners, and decide whether it can be tiled with 2 × 1 tiles.",
              ["With white corners, the full 5 × 3 grid has 8 white and 7 black squares.",
               "The top middle square sits between two white corners, so it is black.",
               "After removing it, 8 white and 6 black squares are left.",
               "Each 2 × 1 tile covers two neighbouring squares, and neighbours have different colours, so each tile "
               "covers one white and one black.",
               "7 tiles would cover 7 white and 7 black squares, but there are 8 white and 6 black.",
               "So no tiling exists."],
              "Not tileable: 8 white and 6 black squares remain, but every tile covers one of each",
              ncert=["6.2.colour_613"]),
           WE("Use the colouring to find another unit square that, when removed from a 5 × 3 grid, makes it "
              "non-tileable.",
              ["Colour the 5 × 3 grid with white corners: 8 white and 7 black squares.",
               "Removing any black square leaves 8 white and 6 black, which no set of tiles can cover.",
               "The black squares are the ones whose row number plus column number is odd.",
               "Besides the top middle square, these are: row 2, column 1; row 2, column 3; row 3, column 2; row 4, "
               "column 1; row 4, column 3; row 5, column 2.",
               "For example, removing the square in row 2, column 1 makes the grid non-tileable."],
              "Any black square works, for example row 2, column 1; the others are row 2 column 3, row 3 column 2, "
              "row 4 column 1, row 4 column 3 and row 5 column 2",
              ncert=["6.2.colour_another"])],
       key_terms=["colouring"], misconceptions=["M_TILE_COLOUR", "M_EVEN_ENOUGH"], minutes=12),
     DOER("T12.C3", "Practice: count colours before you tile", "colour_count", "Analyze",
          "Students colour regions like a chessboard, compare black and white counts, and either tile the region "
          "or prove that it cannot be tiled.",
          ["Every 2 × 1 tile covers one black and one white square.",
           "A region with unequal black and white counts cannot be tiled.",
           "Equal counts do not promise a tiling; try to build one."],
          items=[
              FIO("6.2.FiO_t1", "Figure it Out (tiling), Q1",
                  "Is the following tiling possible? Region to be tiled: 12 unit squares in 4 rows, where the top two "
                  "rows have 2 squares each, at the left, and the bottom two rows have 4 squares each. Tile: an L "
                  "shape of 3 unit squares (two squares stacked, with one more square beside the bottom one). The "
                  "tile may be turned.",
                  ["12 squares need 4 tiles of 3 squares.",
                   "One way: cover the top left square with an L that also covers the square beside it and the "
                   "square below it, in rows 1 and 2.",
                   "Then row 2, column 2 is left in the top part; cover it with row 3, columns 2 and 3, in an L.",
                   "Row 3, column 1 goes with row 4, columns 1 and 2, in an L.",
                   "Row 3, column 4 goes with row 4, columns 3 and 4, in an L.",
                   "All 12 squares are covered by 4 tiles, with no gaps and no overlaps."],
                  "Yes, it is possible: four L tiles, turned to different positions",
                  tool="colour_count"),
              FIO("6.2.FiO_t2", "Figure it Out (tiling), Q2",
                  "Is the following tiling possible? Region to be tiled: an 8 × 8 grid with the top right corner "
                  "square and the bottom left corner square removed. Tile: 2 × 1.",
                  ["The region has 64 squares minus 2, which is 62 squares, an even number.",
                   "Colour it like a chessboard. In an 8 × 8 board, the top right and bottom left corners have the "
                   "same colour, say black.",
                   "The full board has 32 white and 32 black squares. Removing two black ones leaves 32 white and 30 "
                   "black.",
                   "Each 2 × 1 tile covers one white and one black square.",
                   "31 tiles would cover 31 of each colour, but the counts are 32 and 30.",
                   "So the region cannot be tiled."],
                  "Not possible: the two removed corners have the same colour, leaving 32 of one colour and 30 of "
                  "the other",
                  tool="colour_count"),
          ])]))

# ============================== T13 Tiling the plane =========================================================
TOPICS.append(TOPIC(
    "T13", "M4", "Tiling the Whole Plane", ["6.2"], "Understand",
    "Students explain why squares, equilateral triangles and regular hexagons tile the whole plane by checking "
    "that the angles meeting at a corner add to 360°, and meet tilings in art and nature.",
    "A regular polygon tiles the plane when copies of its angle fill 360° at a point exactly.",
    [A("T13.C1", "Squares, triangles and hexagons tile the plane", "Understand",
       "Students explain why squares, equilateral triangles and regular hexagons tile the plane, using the angles "
       "that meet round a corner.",
       textbook=["Tiling the Entire Plane",
                 "So far we have seen how to tile a given region. What about tiling the entire plane?",
                 "Can you think of a shape whose copies can tile the entire plane? Clearly, squares can.",
                 "Are there other regular polygons that can tile the plane? What about equilateral triangles?",
                 "Tiling with equilateral triangles shows the possibility of tiling with another regular polygon.",
                 "A plane can be tiled using regular hexagons as well."],
       teach=["Predict first: at a corner of a tiling, what must the angles that meet add up to?",
              "Squares: 4 × 90 = 360, so four squares meet at each corner.",
              "Equilateral triangles: 6 × 60 = 360, so six meet at a corner.",
              "Regular hexagons: 3 × 120 = 360, so three meet at a corner."],
       examples=[
           WE("Explain why squares, equilateral triangles and regular hexagons can each tile the whole plane.",
              ["Where tiles meet at a corner, their angles must fill the full 360° with no gap and no overlap.",
               "A square has angles of 90°, and 4 × 90 = 360, so four squares fill a corner.",
               "An equilateral triangle has angles of 60°, and 6 × 60 = 360, so six triangles fill a corner.",
               "A regular hexagon has angles of 120°, and 3 × 120 = 360, so three hexagons fill a corner.",
               "Repeating these corners in every direction covers the whole plane."],
              "Each angle goes into 360° exactly: four 90°, six 60°, three 120°",
              ncert=["6.2.plane"])],
       key_terms=["plane"], minutes=8),
     A("T13.C2", "Tilings in art and in nature", "Understand", "",
       textbook=["A plane can also be tiled using more than one shape, and using non-regular polygons. People such as "
                 "the great Dutch artist Escher (1898 to 1972), whose works explored mathematical themes such as "
                 "tiling, have come up with creative ways of tiling a plane with animal shapes!",
                 "Mathematicians are still exploring various ways of tiling the plane! One of these tilings was found "
                 "as recently as 2023.",
                 "Have you seen tilings in daily life? They are often used in buildings and in designs. Tilings are "
                 "found in nature too. The front face of bee hives and some wasp nests are tiled using hexagonal "
                 "cells!",
                 "These cells are used by the insects to keep their eggs, larvae and pupae safe, as well as to store "
                 "food. Because the region is tiled, no space is wasted.",
                 "Scientists still wonder how bees and wasps are able to make hexagonal cells. Next time you see any "
                 "tiling, pay closer attention to it!",
                 "Tiling is still one of the most exciting and active areas of research in geometry."],
       teach=["Look for tilings around you: floors, walls, fabric and honeycombs.",
              "Artists tile the plane with animal shapes; bees tile with hexagons and waste no space."],
       enrichment=True),
     DOER("T13.C3", "Practice: which shapes tile the plane?", None, "Analyze",
          "Students test whether copies of a regular polygon can meet round a corner with no gap, and name the "
          "three regular polygons that tile the plane.",
          ["At every corner of a tiling the angles add to 360°.",
           "90°, 60° and 120° each divide 360° exactly.",
           "Squares, equilateral triangles and regular hexagons tile the plane."])]))

# ============================== T14 Summary =================================================================
TOPICS.append(TOPIC(
    "T14", "M5", "Summary: Constructions and Tilings", ["Summary"], "Remember",
    None,
    "Bisection, the perpendicular bisector, right angles, bisecting and copying angles, 60° from an equilateral "
    "triangle, and tiling, in one place.",
    [A("T14.C1", "What we found about constructions and tilings", "Remember",
       "Students restate the chapter's constructions with their congruence reasons and the meaning of tiling, and "
       "use them on a new question.",
       textbook=["Summary",
                 "A division of a line segment, or any geometrical quantity, into two identical parts is called "
                 "bisection.",
                 "Any point that is of equal distance from the two endpoints of a given line segment lies on its "
                 "perpendicular bisector. This property can be used to construct the perpendicular bisector using a "
                 "ruler and compass.",
                 "The method of constructing the perpendicular bisector can be modified to draw a 90° angle at any "
                 "point on a line using only a ruler and compass.",
                 "An angle can be bisected and copied using the congruence properties of triangles.",
                 "A 60° angle can be constructed using a ruler and compass by constructing an equilateral triangle.",
                 "Covering a region using a set of shapes, without gaps or overlaps, is called tiling."],
       teach=["Our opening question is settled: the centres of an eye's arcs lie on the perpendicular bisector of XY.",
              "Equal arcs and congruent triangles give every construction in the chapter.",
              "Counting and colouring decide whether a region can be tiled.",
              "Still open for you: can you construct a 75° angle, and can a 3 × 3 grid with one corner removed be "
              "tiled?"],
       ncert=["summary"], video_focus=["RECAP"], minutes=8)],
    topic_type="summary"))
