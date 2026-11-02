# -*- coding: utf-8 -*-
"""Tool specs for module M3 (shape sequences): shape_sequence_drawer, shape_count_table. Doer tools only."""
from topics_common import T

TOOLS = {
    "shape_sequence_drawer": T(
        "tool_m3s1t9c3", "Next Shape Drawer", "manipulative",
        "Each shape sequence has a rule for getting the next shape, and a rule is tested by drawing the next shape.",
        "A sequence picker for the five Table 3 sequences with the first four shapes shown; a drawing board for "
        "the fifth; Add Side, Add Point, Add Row and Add Bump buttons; a Check button.",
        ["Predict the rule before drawing.",
         "Draw the next shape with the buttons.",
         "Press Check and write the rule."],
        ["Regular polygons: the fifth shape (a pentagon).",
         "Complete graphs: the next shape after K4 (K5).",
         "Stacked squares: the next stack (4 by 4).",
         "Stacked triangles: the next stack (5 rows).",
         "Koch snowflake: the next stage (each segment gets a speed bump).",
         "Regular polygons: the shape after the decagon (11 sides)."],
        ["A shape that breaks the rule is marked where it differs from the previous one.",
         "A wrong rule is shown next to the last two shapes for comparing.",
         "A solved card lists the change from one shape to the next."],
        "All six next shapes are drawn.",
        ["sequence", "shapeNo", "drawing", "answer", "cardIndex"],
        ["M_SHAPE_ALWAYS_DRAWABLE", "M_KOCH_ADDS", "M_SHAPES_NO_NUMBERS"],
        ["What changed between the third and the fourth shape?",
         "Describe the change in one short sentence, then repeat it.",
         "Use the button that matches the change and draw one step.",
         "The next shape is drawn and the rule is written; a similar sequence follows."]),

    "shape_count_table": T(
        "tool_m3s2t10c3", "Shape Count Table", "simulation",
        "Counting a part of each shape in a sequence gives a number sequence, and the table shows which.",
        "A table with one row per shape and a count column; a Part picker (sides, corners, lines, little squares, "
        "little triangles, segments); a Fill In button; a Name It box.",
        ["Predict the counts before filling in.",
         "Pick the part and fill in the count for each shape.",
         "Name the number sequence."],
        ["Regular polygons, sides (3, 4, 5, 6, 7, counting numbers from 3).",
         "Regular polygons, corners (3, 4, 5, 6, 7, the same).",
         "Complete graphs, lines (1, 3, 6, 10, 15, triangular numbers).",
         "Stacked squares, little squares (1, 4, 9, 16, 25).",
         "Stacked triangles, rows of 1, 3, 5, 7, 9 (1, 4, 9, 16, 25).",
         "Koch snowflake, segments (3, 12, 48, 192, 768)."],
        ["A count that skips a shape is marked on the table row.",
         "A wrong name puts the counts beside Table 1.",
         "A solved card shows how each count comes from the one before."],
        "All six counts and names are right.",
        ["part", "counts", "answer", "cardIndex"],
        ["M_SIDES_CORNERS", "M_COMPLETE_SAME_ADD", "M_STACK_ROWS_SAME", "M_KOCH_ADDS"],
        ["Which part of the shape are you counting?",
         "Fill in the first few rows and look at the jumps.",
         "Compare the counts with the sequences in Table 1.",
         "The counts are matched with a sequence and the reason is shown; a similar table follows."]),
}
