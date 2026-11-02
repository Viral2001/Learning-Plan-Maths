# -*- coding: utf-8 -*-
"""Tool specs for modules M1 and M2 (intersecting lines, dot paper)."""
from topics_common import T

TOOLS = {
    "crossing_angle_lab": T(
        "tool_crossing_angle_lab", "Crossing Angle Lab", "manipulative",
        "When two lines cross, the four angles are linked: neighbours add to 180 degrees and opposite angles are "
        "equal, so one angle fixes the other three.",
        "Two long lines crossing at a point, with the four angles named a, b, c and d. One line can be turned by a "
        "handle. Four answer boxes sit beside the angles. A check button reveals the true value of each box. A "
        "protractor overlay can be switched on to show the measured value, which may be a degree off.",
        ["Read the given angle or the clue on the card.",
         "Predict the other three angles by reasoning and type them in.",
         "Press Check and compare the answers with the lines.",
         "Turn the line to a new angle and watch which angles change together."],
        ["a is 120 degrees: find b, c and d (60, 120, 60).",
         "a is 35 degrees: find b, c and d (145, 35, 145).",
         "b is 100 degrees: find a, c and d (80, 80, 100).",
         "c is 72 degrees: find a, b and d (72, 108, 108).",
         "a is twice b: find all four (120, 60, 120, 60).",
         "a is 20 degrees more than b: find all four (100, 80, 100, 80).",
         "d is 90 degrees: find the other three and name the lines (90, 90, 90, perpendicular)."],
        ["A pair of neighbouring angles that do not add to 180 shows the two angles side by side on a straight line "
         "with the gap highlighted.",
         "A pair of opposite angles typed as different values shows one copied onto the other, and they match.",
         "A protractor reading that is a degree off is shown with a note: the reasoning says 180, the pencil line "
         "has thickness."],
        "Seven cards are answered, each with all four angles reasoned before the check.",
        ["lineAngle", "givenAngleName", "givenAngleValue", "answers", "protractorOn", "cardIndex"],
        ["M_ADJACENT_EQUAL", "M_MEASURE_EXACT"],
        ["Which angle is given, and which angles sit next to it on a straight line?",
         "Neighbouring angles add to 180 degrees; opposite angles are equal.",
         "Subtract the given angle from 180 for each neighbour and copy it to the opposite angle.",
         "The four angles are shown on the lines with their sums marked; a similar card follows."]),

    "dot_paper_studio": T(
        "tool_dot_paper_studio", "Dot Paper Line Studio", "manipulative",
        "On dot paper a line is described by its steps across and up. Equal steps make parallel lines; swapping "
        "the steps and changing one sign makes a perpendicular line.",
        "A grid of dots up to 13 by 13. The student joins two dots to draw a segment between dots. A readout shows "
        "the steps across and up of the last segment. A mode switch asks for a parallel, a perpendicular, or a "
        "yes-or-no test for a pair of segments. Arrow marks and a square are added automatically to a correct "
        "pair.",
        ["Read the task card: draw a parallel, draw a perpendicular, or decide for a pair.",
         "Join dots to draw the segment and read its steps.",
         "Draw the new segment and press Check.",
         "Move a dot of the new segment and watch the steps readout."],
        ["A flat segment: draw a perpendicular (an upright segment).",
         "A segment with steps 2 across and 2 up: draw a perpendicular (2 across and 2 down).",
         "A segment with steps 1 across and 3 up: draw a parallel (1 across and 3 up from another dot).",
         "A segment with steps 2 across and 3 up: try a perpendicular (3 across and 2 down), and say how wide the "
         "grid must be to hold it (at least 4 dots across).",
         "Do segments with steps 3 across and 3 down, and 1 across and 1 down, lie on parallel lines (no, they "
         "lean opposite ways).",
         "Do segments with steps 5 across and 2 up, and 10 across and 4 up, lie on parallel lines (yes, 5 times "
         "4 is 2 times 10).",
         "Draw lines parallel to a 4 by 4 diagonal, a 1 by 6 steep segment and a 5 by 2 shallow segment."],
        ["A segment that does not repeat the steps shows both segments on a shared grid with the steps written on "
         "each, and the mismatch is circled.",
         "A perpendicular that has the right steps but different lengths is accepted, with a note that length does "
         "not matter.",
         "A drawn pair that looks parallel but whose steps differ is shown extended until the lines cross."],
        "Seven tasks are completed, each checked by the steps across and up.",
        ["gridSize", "givenSegment", "drawnSegment", "mode", "stepsReadout", "cardIndex"],
        ["M_LOOKS_PARALLEL", "M_PERP_TILT"],
        ["What are the steps across and up of the given segment?",
         "A parallel line keeps the same steps; a perpendicular swaps them and changes one sign.",
         "Start at any dot and take the same steps across and up; the other end is a dot too.",
         "The new segment is drawn with the steps marked on both; a similar card follows."]),
}
