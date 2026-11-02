# -*- coding: utf-8 -*-
"""Tool specs for module M5 (alternate and interior angles)."""
from topics_common import T

TOOLS = {
    "alternate_chaser": T(
        "tool_alternate_chaser", "Alternate Angle Chaser", "manipulative",
        "An alternate angle is reached in two moves: to the corresponding angle, then to its vertically opposite "
        "angle. Both moves keep the size, so alternate angles of parallel lines are equal.",
        "Two parallel lines cut by a transversal, with the angles a to h marked, a at the top left of the upper "
        "crossing and e at the top left of the lower crossing. The student taps an angle, then a button moves to "
        "the corresponding angle and another moves to the vertically opposite angle. A readout keeps the value "
        "through each move. A switch un-parallels the lines.",
        ["Tap the starting angle and set its value.",
         "Move to the corresponding angle, then to the vertically opposite angle.",
         "Read the alternate angle and say why the value did not change.",
         "Un-parallel the lines and watch the chain break."],
        ["f is 120 degrees: chase to the alternate angle d (120).",
         "e is 65 degrees: chase to the alternate angle c (65).",
         "f is 70 degrees: find d (70).",
         "c is 100 degrees: find the alternate angle e (100).",
         "Given 6 is 135 degrees: find all eight angles (135 four times and 45 four times).",
         "a is 120 degrees and f is 70 degrees: are the lines parallel (no, b is 60 and f is 70).",
         "Alternate angles measure 80 and 100: are the lines parallel (no)."],
        ["A chain that skips a move shows the missing angle highlighted between the start and the end.",
         "A claim that alternate angles add to 180 shows two alternate angles measured as equal on parallel lines.",
         "On un-parallel lines the chain breaks at the corresponding step and the two corresponding angles are "
         "shown unequal."],
        "Seven cards are answered with both moves of the chain named.",
        ["angleF", "chainStep", "currentAngle", "parallelSwitch", "cardIndex"],
        ["M_ALT_SUM", "M_WRONG_PAIR", "M_LOOKS_PARALLEL"],
        ["Which angle do you start from, and which one do you need to reach?",
         "First go to the corresponding angle, then to the vertically opposite angle.",
         "Copy the value across: the corresponding angle has the same size, and so has its vertically opposite.",
         "The chain is shown with both moves and the value on each angle; a similar card follows."]),

    "same_side_lab": T(
        "tool_same_side_lab", "Same Side Interior Angle Lab", "manipulative",
        "Interior angles on the same side of a transversal across parallel lines always add up to 180 degrees, "
        "because one of them is a linear pair of the corresponding angle of the other.",
        "Two parallel lines and a transversal, with the angles 1 to 8 numbered. The two interior angles on the "
        "right side and on the left side are shaded. A slider turns the transversal; a sum bar shows the two "
        "shaded angles end to end against a straight line. A four-sided figure mode shows two pairs of parallel "
        "lines.",
        ["Set one interior angle with the slider.",
         "Predict the same-side partner and type it.",
         "Check the sum bar against the straight line.",
         "Switch to the four-sided figure and find an angle from its neighbour."],
        ["Angle 3 is 50 degrees: find angle 6 (130).",
         "Angle 3 is 72 degrees: find angle 6 (108).",
         "Angle 4 is 110 degrees: find the same-side partner angle 5 (70).",
         "Angle 3 is 50 degrees: find angle 5 and angle 6 (50 and 130).",
         "A four-sided figure with two pairs of parallel sides has one angle 60 degrees: find its two neighbours "
         "(120 and 120).",
         "Angle 3 is 70 degrees and angle 6 is 100 degrees: are the lines parallel (no, the sum is 170).",
         "The lines are parallel and angle 3 is 90 degrees: find all the angles (90 each)."],
        ["A sum that is not 180 shows a gap on the straight line, and the lines extended until they meet.",
         "A claim that interior angles are equal shows angles of 50 and 130 side by side.",
         "A correct answer shows the linear pair and the corresponding angle that explain it."],
        "Seven cards are answered with the same-side pair named and the sum checked.",
        ["transversalAngle", "angleThree", "shadedSide", "shapeMode", "cardIndex"],
        ["M_INTERIOR_EQUAL", "M_ALT_SUM"],
        ["Which two angles are on the same side of the transversal and between the lines?",
         "They add up to 180 degrees, because one is a linear pair of the other's corresponding angle.",
         "Subtract the given angle from 180 to get its same-side partner.",
         "The two angles are placed end to end on a straight line; a similar card follows."]),
}
