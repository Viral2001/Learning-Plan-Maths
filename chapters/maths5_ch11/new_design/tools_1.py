# -*- coding: utf-8 -*-
"""Tool specs for T1, T2 and T3 of Class 5 Chapter 11 (Grandmother's Quilt): Quilt Lace (the free try of the intro, right
after the hook), Tile the Table and Grid Area. Specs only; the tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds are labelled practice values. One
activity at a time, one instruction at a time, large controls, Back and Next in the same place, visible progress,
Hint, Retry and Reset always present, immediate specific feedback that is never red."""
from topics_common import T

TOOLS = {
    "quilt_lace": T(
        "tool_quilt_lace", "Quilt Lace", "manipulative",
        "Find out by laying lace along the border of a quilt that the lace needed is the length all the way round, "
        "counted in units: the red and blue reels run out, the green reel fits exactly, and two laces of different "
        "colours can share the border. This is the free first try of the chapter, so it asks and shows; the video that "
        "follows names the perimeter.",
        "Grandmother's sunny patchwork room, drawn as a warm 3D isometric scene with soft shadows and gentle animation. "
        "The quilt cover is spread on the floor and is the largest thing on screen: 15 patches along the long side and "
        "10 patches along the short side in rows of green, red and yellow patches with a pink rim, as in your maths "
        "book. Every patch side is 1 unit. On a stool beside the quilt stand three lace reels with the lengths of "
        "your maths book: red lace 40 units, green lace 50 units and blue lace 25 units, each lace marked in units. An "
        "instruction strip at the top shows one sentence in large type, with progress dots under it. Controls: tap a "
        "reel to pick its lace; drag the end of the lace along the border of the quilt, and it snaps to the patch "
        "edges, one unit for each patch side, and turns at the corners; a Cut button that cuts the lace at the place "
        "reached; an Undo button that picks the lace up one unit at a time; a Two laces switch that gives a second reel "
        "slot, so that a second colour can be laid after the first one is cut; Check, Hint, Retry (picks up the lace "
        "of this step), Reset (returns the quilt and the three reels), Back and Next in the same places on every card. "
        "Read-outs: a counter units laid (for example 25), the units left to cover (for example 25 left), the length of "
        "the reel chosen, and a card number out of 7. On the small practice quilt the student taps each outer edge and "
        "a counter adds one for each tap.",
        ["Look at Grandmother's quilt and the three lace reels from the story. She wants "
         "to put lace all the way round the edge of the quilt. Tap the reel you think will go all the way round, then "
         "press Next.",
         "Lay each lace along the border from the top left corner and watch where it ends, "
         "count the units on each side, count the border of a small practice quilt edge by edge, and see why counting "
         "the patches along the border is not the same as counting the lace units.",
         "Answer Grandmother's own questions from the story: Tick the lace option that would cover "
         "the entire border of the quilt. She decides to use two different coloured laces. How much lace of each kind "
         "will be needed to cover the entire border? Cut two laces that go all the way round."],
        ["Card 1: pick the blue lace and drag it along the border from the top left corner. Where does it run "
         "out? Answer: after 25 units, at the bottom right corner, because the top side is 15 units and the right side "
         "is 10 units and 15 + 10 = 25. The bottom side and the left side are not covered, so the blue lace is too "
         "short.",
         "Card 2: pick the red lace and lay it the same way. Where does it run out? Answer: after 40 units, at "
         "the bottom left corner, because 15 + 10 + 15 = 40. The left side, 10 units, is still not covered, so the red "
         "lace is too short.",
         "Card 3: pick the green lace and lay it all the way round. What do the four sides add up to? Answer: "
         "15 + 10 + 15 + 10 = 50 units. The green lace is 50 units, so it fits all the way round exactly.",
         "Card 4 (practice values): a small quilt of 6 patches by 4 patches. Tap every outer edge once and read "
         "the counter. Answer: 6 + 4 + 6 + 4 = 20, so the border has 20 units.",
         "Card 5: count the patches along the border of the big quilt, then count the units of lace. Why are "
         "the two numbers different? Answer: the patches on the border are 46 and the lace units are 50, because each "
         "of the 4 corner patches has 2 sides on the border but is counted once as a patch: 46 + 4 = 50. Count the "
         "units of lace, not the patches.",
         "Challenge: 'Tick the lace option that would cover the entire border of the quilt. (i) Red lace 40 "
         "units (ii) Green lace 50 units (iii) Blue lace 25 units.' Lay each lace and tick the one that covers the "
         "entire border. Answer: (ii) the green lace, 50 units, because the border is 15 + 10 + 15 + 10 = 50 units; "
         "the red lace and the blue lace are too short.",
         "Challenge: 'She decides to use two different coloured laces. How much lace of each kind will be "
         "needed to cover the entire border?' Turn on Two laces, lay the first lace, cut it, then lay a lace of a "
         "different colour to finish the border. Answer: any two lengths that make 50 units in all and fit the reels "
         "are right, for example 30 units of red lace for the two long sides and 20 units of blue lace for the two "
         "short sides, because 30 + 20 = 50, or 25 units of blue lace and 25 units of red lace. Your answer may "
         "differ. Next stop: the name for the length of the border."],
        ["The lace follows the finger along the patch edges and the counter units laid goes up one for each patch side. "
         "When a reel runs out the lace stops with a soft note, for example: The red lace has 40 units. The border is "
         "longer, 10 units still to cover.",
         "When a lace goes all the way round exactly, the quilt shines softly and the tool names the sides: 15, 10, 15 "
         "and 10 units.",
         "A tap on an outer edge of the practice quilt lights it orange and adds one to the counter. An edge that is "
         "inside the quilt gives a soft amber note: This edge is inside. Count the edges on the outside.",
         "In the two-lace challenge the tool accepts any split that covers the whole border, and says for example: 30 "
         "units of red and 20 units of blue make 50 units, the whole border. If the lace is too long for a reel it "
         "says: The blue reel has only 25 units.",
         "A wrong tick shows a soft amber note and never a red cross, and it asks the student to lay that lace along "
         "the border and look again."],
        "The student has laid the red, blue and green laces along the border and seen which one is long enough, has "
        "counted the border of the small quilt edge by edge, has seen why the patches on the border are fewer than the "
        "units of lace, and has ticked the right lace and cut two laces for the border.",
        ["laceColour", "unitsLaid", "unitsLeft", "twoLacesOn", "outerEdgesTapped", "tickedLace", "challengeIndex"],
        ["M_BORDER_PATCHES", "M_PERIM_TWO_SIDES"],
        ["What does the lace have to go round? Look at the edge of the quilt, all the way round.",
         "Count the lace units along one side of the quilt, one unit for each patch side. Then count the next side.",
         "The long side is 15 units and the short side is 10 units. How many long sides and how many short sides does "
         "the border have? Add them all.",
         "15 + 10 + 15 + 10 = 50. The border is 50 units, so the lace must be 50 units or more. The tool lays the "
         "first side so you can see it."]),

    "tile_the_table": T(
        "tool_tile_the_table", "Tile the Table", "manipulative",
        "Find out which shapes cover a surface with no gaps and no overlaps, and count the tiles that cover a region as "
        "its area in the unit of the tile: triangles, squares and rectangles tile and circles leave gaps, and the same "
        "region needs a different number of different tiles.",
        "The table corner of Grandmother's patchwork room, drawn as a warm 3D isometric scene with soft shadows and "
        "gentle animation. Four table tops stand in a row, Table 1, Table 2, Table 3 and Table 4, as in your maths "
        "book, and the table being covered is the largest thing on screen, in the middle. Table 1 takes triangles "
        "(each square of a 5 by 2 top is cut from corner to corner into 2 triangles), Table 2 takes circles (a 4 by 2 "
        "top), Table 3 takes squares (a 4 by 2 top) and Table 4 takes rectangles (a 3 by 4 top). Preetha's desk is a "
        "9 by 6 grid of equal squares with three tiles for it: a blue square, a green triangle that is half a square "
        "and a red triangle whose two shorter sides are each 3 squares long. A tile shelf at the side holds a "
        "triangle, a circle, a square and a rectangle. An instruction strip at the top shows one sentence in large "
        "type, with progress dots under it. Controls: tap a tile on the shelf and then tap places on the table to put "
        "the tile down; a Fill the rest button that repeats the tile over the empty places; an Undo button; a Gaps "
        "glow that turns the empty spaces between tiles soft orange; Check, Hint, Retry (clears the table in front), "
        "Reset (returns all the tables and the desk), Back and Next in the same places on every card. Read-outs: a "
        "tile counter with the name of the tile (for example 20 triangles), a note when there are gaps or overlaps, "
        "the area sentence (for example The area of Table 1 is 20 triangle units), and a card number out of 7.",
        ["Look at Grandmother's rug of square patches from the story, with its rows and "
         "columns of patches. Tap the shapes you think can cover a table top with no gaps and no overlaps, then press "
         "Next.",
         "Cover Table 1 with triangles, Table 3 with squares and Table 4 with rectangles and "
         "read the counts, put circles on Table 2 and watch the gaps, and cover one small tray first with squares and "
         "then with triangles to see that the count changes.",
         "Complete the sentences of your maths book about the four tables, ___, ___ and ___ shapes "
         "cover the top of the table without gaps and overlaps, ___ shape leaves gaps, and the areas of Table 1, Table "
         "3 and Table 4 in triangle units, square units and rectangle units. Then cover Preetha's desk with the green "
         "triangles, the red triangles and the blue squares."],
        ["Card 1: pick the triangle and cover Table 1. How many triangles cover it? Answer: 20 triangles, "
         "because the table has 5 by 2 squares, 10 squares, and each square is 2 triangles, 10 × 2 = 20. So the area "
         "of Table 1 is 20 triangle units.",
         "Card 2: pick the square and cover Table 3. How many squares cover it? Answer: 8 squares, because 4 × "
         "2 = 8. The area of Table 3 is 8 square units.",
         "Card 3: pick the rectangle and cover Table 4. How many rectangles cover it? Answer: 12 rectangles, "
         "because 3 × 4 = 12. The area of Table 4 is 12 rectangle units.",
         "Card 4: pick the circle and cover Table 2, then press Gaps. What do you see? Answer: 8 circles fit, "
         "4 in a row and 2 rows, but there are gaps between them, so circles do not tile.",
         "Card 5 (practice values): a tray of 6 squares by 4 squares. Cover it with square tiles, then with "
         "triangle tiles, each square cut from corner to corner. Answer: 24 squares, because 6 × 4 = 24, and 48 "
         "triangles, because 24 × 2 = 48. The tray did not change, only the tile did.",
         "Challenge: 'They found that ___, ___ and ___ shapes cover the top of the table without gaps and "
         "overlaps. ___ shape leaves gaps. ___ triangles cover Table 1. ___ squares cover Table 3. ___ rectangles "
         "cover Table 4. The area of Table 1 is ___ triangle units. The area of Table 3 is ___ square units. The area "
         "of Table 4 is ___ rectangle units.' Answer: triangle, square and rectangle shapes cover the table, and the "
         "circle shape leaves gaps. 20 triangles, 8 squares and 12 rectangles, so the areas are 20 triangle units, 8 "
         "square units and 12 rectangle units.",
         "Challenge: 'Look at the different tiles on her desk and answer how many of the following shapes "
         "will cover the desk. (a) Green triangles (b) Red triangles (c) Blue squares.' Cover the desk with each tile "
         "in turn. Answer: (a) 108 green triangles, because the desk has 9 × 6 = 54 squares and 54 × 2 = 108; (b) 12 "
         "red triangles, because 2 red triangles make a square 3 by 3 and the desk holds 6 of them, 6 × 2 = 12; (c) 54 "
         "blue squares."],
        ["A tile snaps into the next free place and the counter shows the number and the name of the tile, for example "
         "20 triangles. When the table is full the tool says: No gaps and no overlaps, this tile covers the table.",
         "With circles the Gaps glow lights the empty spaces and the tool says: There are gaps between the circles, so "
         "circles do not tile.",
         "The area sentence appears when a table is full, for example: 20 triangles cover Table 1, so its area is 20 "
         "triangle units.",
         "On the desk, a tile that is put over another one blinks softly in amber and the tool says: This tile overlaps "
         "another one. A tile needs its own place.",
         "A wrong count shows a soft amber note and never a red cross, and the tool names the number it expected only "
         "after the second try."],
        "Tables 1, 3 and 4 are covered and counted, the circles have been tried on Table 2, the small tray has been "
        "counted in squares and in triangles, the sentences of the four tables are complete, and the desk is covered "
        "with each of the three tiles.",
        ["selectedTile", "tilesPlaced", "tileCount", "gapsShown", "activeTable", "areaSentence", "challengeIndex"],
        ["M_CIRCLE_TILES", "M_TILE_COUNT"],
        ["What does the table need? Look for gaps between the tiles and for tiles that lie on top of each other.",
         "Count the tiles in one row, then count the rows. How many tiles are there in all?",
         "Say the area with the name of the tile, for example 20 triangles make 20 triangle units. A different tile "
         "gives a different number.",
         "For the desk: 9 × 6 = 54 squares. Each square is 2 green triangles, 54 × 2 = 108. The tool fills the first "
         "row so you can count."]),

    "grid_area": T(
        "tool_grid_area", "Grid Area", "manipulative",
        "Compare areas by laying shapes on each other when one fits inside the other, and by counting unit squares on "
        "a square grid when neither fits inside the other, so that the unit square becomes the measure of area.",
        "A patchwork board in Grandmother's room, drawn as a warm 3D isometric scene with soft shadows and gentle "
        "animation. A square grid mat of equal unit squares lies on the table and is the largest thing on screen, with "
        "a key square marked 1 unit square and, for the gardens, 1 cm. Beside it lie paper cut-outs: rectangle A "
        "(yellow, 3 squares wide and 4 tall), rectangle B (pink, 2 wide and 4 tall) and rectangle C (purple, 2 wide "
        "and 5 tall), as in your maths book. A second board shows the two gardens of your maths book on a grid of 1 cm "
        "squares: garden A (green, 2 wide and 5 tall) and garden B (green, 4 wide and 3 tall) with a pale strip one "
        "square wide that belongs to neither. A trace pad is an empty grid on which a finger draws an outline, for "
        "the palm and the leaf. An instruction strip at the top shows one sentence in large type, with progress dots "
        "under it. Controls: drag a cut-out onto another one to overlay it and see whether it fits inside; drag a "
        "cut-out onto the grid; tap a square to count it, and it turns orange and the counter goes up; a Show unit "
        "squares switch; on the trace pad, draw the outline and tap the whole squares inside it and the part squares "
        "that are more than half covered; Check, Hint, Undo, Retry (returns the shapes of this step), Reset (clears "
        "the board), Back and Next in the same places on every card. Read-outs: the unit squares counted for each "
        "shape (for example A 12), a note saying whether one shape fits inside the other, and a card number out of 7.",
        ["Look at the picture of Preetha's desk with its different tiles. Three "
         "rectangles lie on the table. Say which one you think has the largest area, then press Next.",
         "Overlay B on A and on C, overlay A and C, put A and C on the grid and count their "
         "unit squares, compare two practice rectangles by counting, and count a triangle that has whole squares and "
         "half squares.",
         "Answer the book's own questions: Which of the above rectangles has the largest area? "
         "Compare the areas of the two gardens given below on the square grid. Then trace your own palm or a leaf on "
         "the trace pad and find its approximate area."],
        ["Card 1: drag B onto A, then onto C. What do you see? Answer: B fits inside A and B fits inside C, so "
         "A has a larger area than B and C has a larger area than B.",
         "Card 2: drag A onto C. Does one fit inside the other? Answer: no. A is wider than C, but C is taller "
         "than A, so laying one on the other does not tell us which area is larger.",
         "Card 3: put A and C on the grid and count their unit squares. Answer: A has 3 × 4 = 12 unit squares "
         "and C has 2 × 5 = 10 unit squares, so A has the larger area.",
         "Card 4 (practice values): a rectangle 7 squares long and 2 broad and a rectangle 4 squares long and "
         "4 broad. Count the squares of each. Answer: 2 × 7 = 14 squares and 4 × 4 = 16 squares, so the 4 by 4 "
         "rectangle has the larger area, though it is the shorter one.",
         "Card 5 (practice values): a triangle on a grid of 1 cm squares with two sides 4 squares long. Count "
         "the whole squares and the half squares. Answer: 6 whole squares and 4 half squares. 4 ÷ 2 = 2, so the area "
         "is 6 + 2 = 8 square cm.",
         "Challenge: 'Which of the above rectangles has the largest area?' Put A, B and C on the square grid "
         "and count. Answer: A has 12 unit squares, B has 8 and C has 10, so A has the largest area.",
         "Challenge: 'Compare the areas of the two gardens given below on the square grid. Area of Garden A = "
         "___ cm square. Area of Garden B = ___ cm square.' Count the squares of each garden. Answer: garden A is 2 × "
         "5 = 10 square cm and garden B is 4 × 3 = 12 square cm, so garden B has the larger area. The pale strip "
         "belongs to neither garden."],
        ["A cut-out that fits inside another one clicks into place and the tool says: B fits inside A, so the area of A "
         "is larger. A cut-out that does not fit stays half over the edge and the tool says: Neither shape fits inside "
         "the other. Count unit squares.",
         "Each tapped square turns orange and the counter goes up by one. The count is shown with the name of the "
         "shape, for example A has 12 unit squares.",
         "On the trace pad a whole square tapped inside the outline counts 1, and two part squares count together as 1; "
         "the tool shows the total and says it is an approximate area.",
         "When two shapes are counted the tool compares them: 12 is more than 10, so A has the larger area.",
         "A wrong count shows a soft amber note and never a red cross, and the tool names the number it expected only "
         "after the second try."],
        "The student has seen that B fits inside A and inside C, has seen that A and C cannot be settled by laying one "
        "on the other, has counted A, B and C and the two gardens on the grid, has counted the two practice "
        "rectangles and the triangle, and has traced a palm or a leaf and found an approximate area.",
        ["overlaidShape", "fitsInside", "gridShapes", "squaresCounted", "traceOutline", "activeBoard", "challengeIndex"],
        ["M_ONE_SIDE", "M_AREA_UNIT"],
        ["Which shapes are you comparing? Try laying one on the other first.",
         "If one shape does not fit inside the other, put both on the grid and count the same small squares in each.",
         "Count the squares in one row, then count the rows, and multiply. Do this for each shape.",
         "A is 3 columns and 4 rows, so 3 × 4 = 12. C is 2 columns and 5 rows, so 2 × 5 = 10. The tool counts the "
         "first row so you can see it."]),
}
