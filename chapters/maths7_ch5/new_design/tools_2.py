# -*- coding: utf-8 -*-
"""Tool specs for modules M3 and M4 (transversals, corresponding angles, drawing parallels)."""
from topics_common import T

TOOLS = {
    "transversal_board": T(
        "tool_transversal_board", "Eight Angle Transversal Board", "manipulative",
        "A transversal crossing two lines makes eight angles, which fall into four vertically opposite pairs and "
        "four corresponding pairs; a few of them are always equal.",
        "Two lines l and m and a transversal t that can be dragged and turned. The eight angles are numbered 1 to 8, "
        "four at each crossing. Tapping an angle highlights its vertically opposite angle in one colour and its "
        "corresponding angle in another. A counter shows how many different angle measures there are. A switch "
        "makes l and m parallel.",
        ["Tap an angle and name its corresponding angle.",
         "Turn the transversal and watch the counter of different measures.",
         "Switch the lines to parallel and compare the counter.",
         "Check the answer on the card."],
        ["Name the corresponding angle of angle 1 (angle 5).",
         "Name the corresponding angle of angle 4 (angle 8).",
         "Name the corresponding angle of angle 7 (angle 3).",
         "Name the corresponding angle of angle 6 (angle 2).",
         "Turn the transversal with the lines not parallel: how many different measures at most (4).",
         "Switch to parallel lines: how many different measures now (2).",
         "Make the lines parallel and the transversal perpendicular: how many different measures (1, all 90)."],
        ["A wrong corresponding angle is shown with its two arms against the lines: it is at the other crossing "
         "but in the opposite corner.",
         "A wrong count of different measures shows the pairs coloured by equal size.",
         "A claim that corresponding angles are always equal is shown with the lines not parallel and the two angles "
         "measured."],
        "Seven cards are answered with the angle positions named before the check.",
        ["lineLAngle", "lineMAngle", "transversalAngle", "parallelSwitch", "selectedAngle", "cardIndex"],
        ["M_WRONG_PAIR", "M_CORR_ANY"],
        ["At which crossing does the given angle sit, and in which corner of it?",
         "The corresponding angle sits in the same corner at the other crossing.",
         "Go to the other crossing and pick the same corner: top left, top right, bottom left or bottom right.",
         "The two angles light up in one colour at the same corner; a similar card follows."]),

    "corresponding_test": T(
        "tool_corresponding_test", "Corresponding Angle Parallel Test", "manipulative",
        "Two lines are parallel exactly when a transversal makes equal corresponding angles with them, so equal "
        "corresponding angles can be used to draw or to test a pair of lines.",
        "A line l and a transversal t meeting at X. A second line m through a point Y on t can be turned about Y "
        "with a handle. A tracing-paper overlay copies the angle at X to Y. Two readouts show the corresponding "
        "angles; a lamp turns green when they are equal and the lines then show arrow marks.",
        ["Set the angle at X, then turn m so the angle at Y matches it.",
         "Watch the lamp and the arrow marks.",
         "For a given pair of lines, read both corresponding angles and decide.",
         "Press Check to compare with the lines extended."],
        ["Make m parallel to l when the angle at X is 60 degrees (60 at Y, and the other angle is 120).",
         "Corresponding angles are 75 and 75: are the lines parallel (yes).",
         "Corresponding angles are 64 and 66: are the lines parallel (no, they differ by 2).",
         "Corresponding angles are 110 and 70: are the lines parallel (no, they are not equal).",
         "Two lines lean 10 degrees apart: try three transversals and compare the corresponding angles (they "
         "always differ by 10, never equal).",
         "The lines are parallel and one angle at l is 65 degrees: find the other seven angles (65 or 115)."],
        ["A pair of corresponding angles that differ shows both lines extended until they meet, with the meeting "
         "point marked.",
         "Equal angles that are not corresponding (for example vertically opposite) are flagged as the wrong pair.",
         "A match found at one transversal only is repeated at a second transversal to confirm."],
        "Six cards are answered, and the lines are decided by corresponding angles, not by eye.",
        ["angleAtX", "angleAtY", "lamp", "transversalAngle", "linesLean", "cardIndex"],
        ["M_LOOKS_PARALLEL", "M_CORR_ANY", "M_WRONG_PAIR"],
        ["Which two angles are corresponding, and are they in the same corner at the two crossings?",
         "Equal corresponding angles make the lines parallel; unequal ones do not.",
         "Read both corresponding angles and compare the two numbers.",
         "The lines are extended: parallel lines never meet, the others do; a similar card follows."]),

    "set_square_slider": T(
        "tool_set_square_slider", "Set Square Slide Constructor", "simulation",
        "A set square slid along a ruler keeps the same angle with the ruler, so every line drawn along the same "
        "edge makes equal corresponding angles and the lines are parallel.",
        "A line l with a ruler along it and a set square that slides along the ruler. The student chooses the set "
        "square (right angle, 45 degrees, or 30 and 60 degrees), chooses an edge, slides, and draws along the edge "
        "at two or three places. A readout shows the angle each drawn line makes with l. A point A can be placed "
        "on the paper.",
        ["Choose a set square and an edge, then slide it along the ruler.",
         "Draw a line at two positions.",
         "Read the angle each line makes with l.",
         "Decide if the two lines are parallel and say why."],
        ["Draw two lines with the right-angle edge, both at 90 degrees to l, and say why they are parallel.",
         "Draw two lines with the long side of the 45 degree set square: the angle with l is 45 each time.",
         "Draw two lines with the long side of the 30 and 60 degree set square: the angle with l is the same each "
         "time.",
         "Draw a line through point A parallel to l by sliding the edge until it reaches A.",
         "Turn the set square between two draws (45 then 60): are the lines parallel (no).",
         "Draw a third parallel line and check all three have the same corresponding angle."],
        ["A line drawn after the set square was turned shows the two angles 45 and 60 side by side and the lines "
         "extended until they meet.",
         "A line that passes near A but not through it is shown with the gap enlarged.",
         "A correct line is confirmed by the equal corresponding angles marked in one colour."],
        "Six constructions are made with the edge kept on the ruler and the reason given each time.",
        ["setSquareType", "edgeChoice", "slidePosition", "drawnAngles", "pointA", "cardIndex"],
        ["M_LOOKS_PARALLEL", "M_WRONG_PAIR"],
        ["Which edge of the set square rests on the ruler, and which edge will you draw along?",
         "Slide without turning: the angle with the ruler stays the same, so corresponding angles are equal.",
         "Keep one edge on the ruler, slide to the new place, and draw along the other edge.",
         "The set square is slid for you and both lines are drawn with their angle; a similar card follows."]),
}
