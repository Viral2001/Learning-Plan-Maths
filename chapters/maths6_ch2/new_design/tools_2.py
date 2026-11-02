# -*- coding: utf-8 -*-
"""Tool specs for the right-angle and paper-protractor topics: fold_right, paper_protractor. Doer tools only."""
from topics_common import T

TOOLS = {
    "fold_right": T(
        "tool_m2t7c3", "Fold a Right Angle", "manipulative",
        "Folding a straight angle so its arms overlap makes two equal angles, each a right angle or quarter "
        "turn.",
        "A paper strip showing a straight angle with a vertex O; a draggable fold line; a Fold button with a "
        "ghost of the other side; a corner checker to test a grid corner.",
        ["Predict whether the fold will put the arms on top of each other.",
         "Drag the crease and press Fold.",
         "Keep the crease that makes the two angles overlap."],
        ["Fold a straight angle to get two equal angles.",
         "Fold again to get four equal angles at O.",
         "Test an L-shaped corner turned to a slant: is it a right angle.",
         "A grid with a point: count the ways to make a straight angle.",
         "The same grid: count the ways to make a right angle.",
         "Find right angles around the classroom picture."],
        ["A crease that misses the middle shows the arms not overlapping.",
         "A corner that sticks out past the checker shows it is not a right angle.",
         "A solved card shows the fold with two matching right angles."],
        "All six cards are solved.",
        ["foldAngle", "overlap", "answer", "cardIndex"],
        ["M_RIGHT_UPRIGHT", "M_RIGHT_ANY_L", "M_STRAIGHT_NOT_ANGLE"],
        ["What do the two arms of a straight angle look like when folded together?",
         "Drag the crease until the two arms lie exactly on each other.",
         "Test a corner by laying it on the folded right angle.",
         "The right angle is shown on the fold; a similar card follows."]),

    "paper_protractor": T(
        "tool_m3t11c4", "Paper Protractor", "manipulative",
        "Each fold halves an angle, so a paper semicircle folded again and again gives marks at 90, 45 and 22.5 "
        "degrees.",
        "A paper semicircle with its centre O; a Fold button that halves the marked angle with the crease shown; "
        "a label that fills the measure; a check button.",
        ["Predict the measure the next fold will give.",
         "Press Fold to halve the angle.",
         "Place the label for each crease."],
        ["Fold the semicircle in half: mark the angle 90.",
         "Fold the quarter in half: mark 45.",
         "Fold again: mark 22.5.",
         "Mark 135 from the crease at 90 and the one at 45.",
         "Mark all marks from 0 to 180 in steps of 22.5.",
         "Use the paper protractor to measure a given angle."],
        ["A label that is not half of the one before shows the angle the fold really makes.",
         "A crease that is not through the middle shows two unequal parts.",
         "A solved card shows the marks 0, 22.5, 45, 67.5, 90, 112.5, 135, 157.5 and 180."],
        "All six marks are placed.",
        ["folds", "marks", "answer", "cardIndex"],
        ["M_BISECT_ANY_PART", "M_DEGREE_FULL"],
        ["What angle is the semicircle at the centre?",
         "Each fold halves the angle that was marked before it.",
         "Half of 90 is 45, and half of 45 is 22.5.",
         "The folds are shown with their measures; a similar card follows."]),
}
