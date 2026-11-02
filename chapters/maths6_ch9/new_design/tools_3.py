# -*- coding: utf-8 -*-
"""Tool specs for module M3 (lines and turns together, tiles): symmetry_sorter, tile_designer. Doer tools only."""
from topics_common import T

TOOLS = {
    "symmetry_sorter": T(
        "tool_m3s1t10c3", "Lines and Turns Sorter", "manipulative",
        "A figure is tested for lines by folding and for turns by rotating, two separate tests, and the answers "
        "may differ.",
        "A tray of figures; a Fold test and a Turn test button on each; a two-way table with rows 'has a line' and "
        "'has no line' and columns 'has a turn' and 'has no turn'; counters for lines and for angles of symmetry.",
        ["Predict which box the figure belongs in.",
         "Run the fold test, then the turn test.",
         "Drop the figure in its box and type the counts."],
        ["An equilateral triangle (3 lines, 3 angles).", "A square (4 lines, 4 angles).",
         "A kite (1 line, only 360°).", "A twisted six-petal flower (0 lines, 6 angles).",
         "A regular hexagon (6 lines, 6 angles).", "A scalene triangle (0 lines, only 360°)."],
        ["A figure dropped in the wrong box has both test results replayed beside it.",
         "A count that ignores 360° is reminded that a full turn is an angle of symmetry.",
         "A solved card shows the fold lines and the matching turns on the figure."],
        "All six figures are sorted with the right counts.",
        ["foldResult", "turnResult", "lines", "angles", "answer", "cardIndex"],
        ["M_NO_LINE_NO_SYM", "M_ORDER_LINES", "M_EVERY_LINE"],
        ["Which test finds lines, and which finds turns?",
         "Run the fold test first, then turn the figure about its centre.",
         "Count the matching folds and the matching turns, including 360°.",
         "Both results are shown on the figure; the box is filled and a similar figure follows."]),

    "tile_designer": T(
        "tool_m3s2t11c3", "Tile Designer", "manipulative",
        "A tile design is symmetric by a line when each tile matches its mirror partner, and by a turn when it "
        "matches its half-turn partner.",
        "A 4 by 4 grid; 16 two-colour tiles that can be placed and turned; a Check Lines button showing every line "
        "of symmetry found; a Check Turns button; a counter.",
        ["Predict the number of lines before checking.",
         "Place and turn tiles on the grid.",
         "Press Check Lines and Check Turns, and read the counts."],
        ["Make a design with exactly 1 line of symmetry.", "Make a design with exactly 2 lines of symmetry.",
         "Make a design with 4 lines of symmetry.", "Make a design with a half-turn but no line.",
         "Complete a quarter into a design with exactly 2 lines and no diagonal line.",
         "Make a design with no line and no turn (only 360°)."],
        ["An extra diagonal line is drawn on the design so a design with too many lines is seen.",
         "A tile with no partner is highlighted when a line is missing.",
         "A solved card shows the lines and the turns found."],
        "All six designs are made and checked.",
        ["tiles", "linesFound", "turnsFound", "answer", "cardIndex"],
        ["M_ONE_LINE", "M_BALANCED"],
        ["What must each tile match for a line to work?",
         "Fill one part, then copy it across the line you want.",
         "Check for extra lines, especially along the diagonals.",
         "The tile with no partner is highlighted; fix it and check again."]),
}
