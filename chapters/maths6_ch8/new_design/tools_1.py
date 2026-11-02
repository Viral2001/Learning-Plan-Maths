# -*- coding: utf-8 -*-
"""Tool specs for modules M1 and M2 (compass circles, waves, shape checker, construction stepper). Doer tools only."""
from topics_common import T

TOOLS = {
    "compass_circle": T(
        "tool_m1s2c4", "Compass Circle Maker", "manipulative",
        "A compass keeps one distance fixed, so every point it draws is the same distance, the radius, from the "
        "centre; the radius is half of the width across.",
        "A sheet with a ruler along the bottom; a compass whose opening is set against the ruler; a centre point "
        "that can be dragged; a pencil that sweeps round; a radius read-out and a width-across read-out.",
        ["Predict the radius or the width across before drawing.",
         "Set the compass opening against the ruler and fix the centre.",
         "Sweep the pencil, then type the radius or the width across."],
        ["Radius 3 cm: how wide is the circle across? (6 cm)",
         "A circle 10 cm across: what radius do you set? (5 cm)",
         "Two circles of radius 2 cm touch: how far apart are the centres? (4 cm)",
         "Two circles share a centre, radii 2 cm and 4 cm: how wide is the gap between them? (2 cm)",
         "Two circles of radius 3 cm overlap with centres 4 cm apart: is the centre of one inside the other? (yes)",
         "Radius 2.5 cm: how wide across? (5 cm)"],
        ["Setting the opening from the end of the ruler instead of its zero mark shows the true opening beside the "
         "one typed, so the slip is seen.",
         "Typing the width across as the radius shows the radius as half of that width.",
         "A solved card shows the centre, the radius line and the finished circle."],
        "All six cards are solved.",
        ["radius", "centre", "opening", "answer", "cardIndex"],
        ["M_FREEHAND_CIRCLE", "M_RULER_END", "M_RADIUS_DIAMETER"],
        ["What does the compass opening stand for?",
         "The opening is the radius, and the width across is two radii.",
         "Read the radius or the width in the card and halve or double it.",
         "The tool shows the radius line and the width across; a similar card follows."]),

    "wave_builder": T(
        "tool_m1s3c2", "Wave Builder", "simulation",
        "A wavy line is a row of half circles along a central line; the width of each half circle across is the "
        "central line divided by the number of waves, and the radius is half of that.",
        "A central line with a ruler; a stepper for the number of waves; a radius dial; half circles that appear "
        "alternately above and below the line; read-outs for the width of each wave and the radius.",
        ["Predict the radius before setting the dial.",
         "Choose the number of waves and set the radius.",
         "Check that the half circles join end to end along the line."],
        ["A central line of 12 cm with 3 waves: radius of each half circle? (2 cm)",
         "A central line of 8 cm with 2 waves: radius? (2 cm)",
         "A central line of 10 cm with 5 waves: radius? (1 cm)",
         "A central line of 9 cm with 3 waves: radius? (1.5 cm)",
         "Radius 1.5 cm on a line of 12 cm: how many waves? (4)",
         "A line of 6 cm with 1 wave: radius? (3 cm)"],
        ["A radius that is too small leaves a gap along the line, and one that is too big runs past its end; the "
         "tool shows both.",
         "Using the width of the wave as the radius shows the half circles overlapping.",
         "A solved card shows the half circles joined along the central line."],
        "All six cards are solved.",
        ["waves", "radius", "lineLength", "answer", "cardIndex"],
        ["M_RADIUS_DIAMETER", "M_ARC_TIP_ON_FIGURE"],
        ["How many half circles must fit along the line?",
         "Each half circle spans the line length divided by the number of waves; the radius is half of that.",
         "Divide the line length in the card by the waves, then halve it.",
         "The tool shows the span and the radius; a similar card follows."]),

    "property_checker": T(
        "tool_m2s5c3", "Shape Property Checker", "manipulative",
        "A square and a rectangle are told apart by measuring: a rectangle has four angles of 90° and equal "
        "opposite sides, and a square also has all four sides equal; tilting a figure changes nothing.",
        "A figure that can be tilted; a ruler and a protractor that snap to a side or a corner; a checklist of "
        "opposite sides equal, four sides equal and four angles of 90°; a name box with square, rectangle or "
        "neither.",
        ["Predict the name before measuring.",
         "Measure sides and angles and tick the checklist.",
         "Pick the name the checklist allows."],
        ["Four sides of 4 cm and four angles of 90°: name it. (square, which is also a rectangle)",
         "Sides 6 cm and 3 cm, four angles of 90°: name it. (rectangle, not a square)",
         "Four sides of 5 cm, angles 60° and 120°: name it. (neither a square nor a rectangle)",
         "A square of side 4 cm tilted by 45°: name it. (square)",
         "Opposite sides 5 cm and 3 cm, angles 70° and 110°: name it. (neither)",
         "Sides 5 cm and 5 cm, four angles of 90°: name it. (square)"],
        ["Naming a figure from its looks alone shows the checklist items not yet measured.",
         "Calling a square not a rectangle shows that a square passes both rectangle checks.",
         "A solved card shows the measured sides and angles and the ticked checklist."],
        "All six cards are solved.",
        ["sides", "angles", "tilt", "answer", "cardIndex"],
        ["M_SQUARE_NOT_RECT", "M_EQUAL_SIDES_SQUARE", "M_TILT_NOT_SQUARE"],
        ["What must be true for a rectangle?",
         "A rectangle has four angles of 90° and equal opposite sides; a square also has all sides equal.",
         "Measure the angles first, then compare the sides in the card.",
         "The tool shows the checklist filled in; a similar card follows."]),

    "construction_stepper": T(
        "tool_m2s7c3", "Construction Stepper", "simulation",
        "A square or a rectangle is built in order: one side, perpendiculars at both ends, the other corners at "
        "the right length, then the last side; the properties fix the lengths and angles that are not measured.",
        "A drawing sheet with a ruler, a protractor and a compass; a list of steps that unlock one at a time; "
        "a measuring read-out for every side and angle; a Check button.",
        ["Predict the length of the fourth side before drawing it.",
         "Choose the right tool for each step and carry it out.",
         "Press Check and read the sides and angles."],
        ["A square of side 5 cm: how long is the fourth side? (5 cm)",
         "A rectangle 6 cm by 4 cm: how long is the side opposite the 6 cm side? (6 cm)",
         "A square of side 3 cm: what is each angle? (90°)",
         "A rectangle 8 cm by 3 cm: how many lengths must you mark by compass or ruler? (two, one on each "
         "perpendicular)",
         "A rectangle 5 cm by 2 cm: how long is the side opposite the 2 cm side? (2 cm)",
         "A rectangle 7 cm by 4 cm: what is each angle? (90°)"],
        ["Measuring from the end of the ruler instead of the zero mark gives a side that is too short, and the "
         "Check button shows the actual length.",
         "Marking an equal length on only one perpendicular leaves the figure open, and the tool shows the gap.",
         "A solved card shows every step in order with the final sides and angles."],
        "All six cards are solved.",
        ["step", "sideLength", "angle", "answer", "cardIndex"],
        ["M_RULER_END", "M_EQUAL_SIDES_SQUARE"],
        ["Which side is drawn first?",
         "Perpendiculars at the two ends of the first side stay the same distance apart, so the opposite side "
         "matches it.",
         "Mark the length from the card on each perpendicular, then join the two marks.",
         "The tool shows each step done in order; a similar card follows."]),
}
