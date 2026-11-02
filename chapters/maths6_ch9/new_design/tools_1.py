# -*- coding: utf-8 -*-
"""Tool specs for module M1 (line symmetry): fold_finder, mirror_completer, punch_unfold. Doer tools only."""
from topics_common import T

TOOLS = {
    "fold_finder": T(
        "tool_m1s1t2c3", "Fold and Find Lines", "manipulative",
        "A line is a line of symmetry only if folding along it makes the two parts overlap exactly.",
        "A figure on a sheet; a draggable fold line that can be set vertical, horizontal or at an angle; a Fold "
        "button that flips one side over the line with a ghost of the other side; an overlap meter; a list of lines "
        "found so far.",
        ["Predict whether the fold will work before pressing Fold.",
         "Drag the fold line to a position and press Fold.",
         "Keep the lines that overlap and count them, or say none."],
        ["An isosceles triangle (1 line).", "A square (4 lines).",
         "A rectangle that is not a square (2 lines, and the diagonal fails).",
         "A kite (1 line).", "A scalene triangle (0 lines).", "A regular hexagon (6 lines)."],
        ["A fold that leaves a corner sticking out shows the unmatched part in red, so equal-looking halves are "
         "seen not to overlap.",
         "A wrong count shows the lines found so far on the figure and asks to try another direction.",
         "A solved card shows each line of symmetry as a dashed line with the two halves overlapping."],
        "All six figures have the right number of lines.",
        ["foldAngle", "overlap", "linesFound", "answer", "cardIndex"],
        ["M_BALANCED", "M_HALVES_ANY", "M_DIAGONAL_RECT", "M_EVERY_LINE"],
        ["What does it mean for two halves to overlap exactly?",
         "Try a vertical, a horizontal and a slanted fold on the figure.",
         "Press Fold on a line and look for any part that sticks out.",
         "The lines that overlap are shown as dashed lines; count them and a similar figure follows."]),

    "mirror_completer": T(
        "tool_m1s2t4c3", "Mirror Completer", "manipulative",
        "A figure is completed by reflecting each point in the line of symmetry: the mirror partner is the same "
        "distance from the line on the other side.",
        "A square grid with one blue mirror line and a half-figure on one side; dots for the corners; a Reflect "
        "button that drops the mirror partner of each dot with a dashed link crossing the line at right angles; a "
        "second blue line on later cards.",
        ["Predict where the mirror partner of a corner will land.",
         "Tap or drag a corner to its partner position, or press Reflect to check.",
         "Join the dots to finish the figure."],
        ["A vertical line with a 3-square L-shape on one side.", "A horizontal line with a triangle touching it.",
         "A diagonal line with a one-square staircase.", "A vertical line where the figure crosses the line.",
         "Two lines, vertical and horizontal, with a small shape in one corner (4 copies in all).",
         "Two diagonal lines with a small shape in one gap (4 copies in all)."],
        ["A partner on the wrong side shows the dashed link and the unequal distances to the line.",
         "A point on the line is shown staying fixed.",
         "A solved card shows the completed figure with its line, or lines, as dashed lines."],
        "All six figures are completed.",
        ["mirrorLine", "points", "placed", "answer", "cardIndex"],
        ["M_REFLECT_STAYS"],
        ["Which side of the line is the figure on now?",
         "Each point goes to the other side at the same distance from the line.",
         "Count the squares from the point to the line, and count the same number on the other side.",
         "The partner is shown with its dashed link; a similar figure follows."]),

    "punch_unfold": T(
        "tool_m1s3t5c4", "Punch and Unfold", "simulation",
        "A hole or cut on a folded sheet appears once for each layer, mirrored across every fold line.",
        "A square sheet; fold buttons for vertical, horizontal and diagonal folds with a fold counter; a Punch tool "
        "and a Cut tool; an Unfold button that opens the sheet with the folds shown as dashed lines.",
        ["Predict how many holes the opened sheet will have.",
         "Fold the sheet, punch or cut, and press Unfold.",
         "Name the fold lines, or choose the folds that give a target pattern."],
        ["One vertical fold and one punch: how many holes (2).", "A diagonal fold and one punch (2 holes).",
         "A vertical fold then a horizontal fold and one punch (4 holes).",
         "Two holes on the left and right at the same height: which fold (vertical).",
         "Four holes, one near each corner, from a single punch: which folds (vertical and horizontal).",
         "Get a square hole in the centre with folds and one straight cut (fold twice and cut a corner)."],
        ["A wrong fold shows where the punched holes would land and how they differ from the target.",
         "The fold lines are shown dashed on the opened sheet so the line of symmetry is seen.",
         "A solved card shows the sheet folded, punched and opened in three small pictures."],
        "All six cards are solved.",
        ["folds", "punchSpot", "holes", "answer", "cardIndex"],
        ["M_CUT_SAME"],
        ["How many layers does the folded sheet have?",
         "Each layer gets one hole, so the holes are mirror partners across each fold.",
         "The fold line sits halfway between a pair of matching holes.",
         "The fold lines are shown dashed; a similar card follows."]),
}
