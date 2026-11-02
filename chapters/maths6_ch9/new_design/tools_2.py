# -*- coding: utf-8 -*-
"""Tool specs for module M2 (rotational symmetry): rotate_match, radial_arms, angle_ladder. Doer tools only."""
from topics_common import T

TOOLS = {
    "rotate_match": T(
        "tool_m2s1t6c4", "Turn and Match", "manipulative",
        "A figure has rotational symmetry when a turn between 0° and 360° about its centre makes it look the same "
        "as before.",
        "A figure on a fixed outline of itself with a red centre dot; a turn dial from 0° to 360° in steps of 15°; "
        "a Turn button that rotates the figure and flashes green on a match; a record of the angles that matched.",
        ["Predict the smallest turn that will match.",
         "Turn the figure with the dial or the button.",
         "Record each angle where it matches and list them, 360° last."],
        ["A 4-bladed windmill (90°, 180°, 270°, 360°).", "A strip with one short side (360° only).",
         "A plus shape with 4 equal arms (90°, 180°, 270°, 360°).",
         "A long rectangle (180°, 360°).", "A figure with 3 equal arms 120° apart (120°, 240°, 360°).",
         "An isosceles triangle (360° only)."],
        ["A turn that nearly matches shows the gap in red so near misses are not counted.",
         "A list that leaves out 360° is reminded that a full turn always matches.",
         "A solved card shows the matched positions in colour around the centre."],
        "All six figures have the right list of angles.",
        ["centre", "turnAngle", "matches", "answer", "cardIndex"],
        ["M_ORDER_DISTINCT", "M_NO_LINE_NO_SYM"],
        ["Where is the centre of rotation marked?",
         "Turn the figure slowly and watch for the outline to match.",
         "Note each angle where it matches, and add 360° at the end.",
         "The matching angles are shown in colour; a similar figure follows."]),

    "radial_arms": T(
        "tool_m2s2t7c4", "Radial Arms Builder", "manipulative",
        "Equal arms placed at equal angles of 360 ÷ n give exactly n angles of symmetry; unequal spacing leaves "
        "only 360°.",
        "A centre point with up to 8 identical arms; a number-of-arms stepper; sliders to set each angle between "
        "neighbours; a Turn button that rotates a copy over the fixed figure and counts matches; a list of angles "
        "of symmetry.",
        ["Predict the angle of symmetry before turning.",
         "Set the number of arms and the angles between them.",
         "Turn the copy and read the angles and the order."],
        ["4 arms at 90° (90°, 180°, 270°, 360°).",
         "4 arms where opposite arms are alike but the two pairs differ (180°, 360°).",
         "3 arms at 120° (120°, 240°, 360°).", "3 arms with angles 100°, 120° and 140° (360° only).",
         "5 arms at 72° (72°, 144°, 216°, 288°, 360°).", "6 arms at 60° (order 6)."],
        ["Unequal angles show the copy failing to land on the figure, with the gap in red.",
         "A wrong order shows the angles counted one by one along a clock face.",
         "A solved card shows the angle between arms as 360 ÷ n."],
        "All six figures are built and read correctly.",
        ["arms", "gaps", "turnAngle", "order", "answer", "cardIndex"],
        ["M_ARMS_ENOUGH", "M_ORDER_DISTINCT"],
        ["How many arms does the figure have, and are they all the same?",
         "For equal arms, share the full turn of 360° equally among the gaps.",
         "Divide 360° by the number of arms to get the gap and the smallest angle.",
         "The angles are shown on a clock face; count them for the order and a similar figure follows."]),

    "angle_ladder": T(
        "tool_m2s3t8c3", "Angle Ladder", "simulation",
        "With n equal turns the smallest angle of symmetry is 360 ÷ n, and the other angles are its multiples up "
        "to 360°.",
        "A circle of 12 coloured sectors; a repeat-every stepper; a ladder of rungs showing the multiples of the "
        "smallest angle up to 360°; a dial that tests a target angle; a mixed-fraction read-out when 360 ÷ n is "
        "not whole.",
        ["Predict the smallest angle before moving the stepper.",
         "Choose how often the colour pattern repeats around the circle.",
         "Read the ladder, or type whether a target angle is possible."],
        ["Colour so that the figure has 3 angles of symmetry (every 4th sector).",
         "Colour so that it has 4 angles of symmetry (every 3rd sector).",
         "Smallest angle is 60°: the other angles (120°, 180°, 240°, 300°, 360°).",
         "60° is an angle and there are two angles below 60°: the smallest (20°).",
         "Can the smallest angle be 45°? (yes, 8 turns)", "Can the smallest angle be 17°? (no)"],
        ["A repeat that does not divide 12 shows the pattern failing to close up.",
         "A target angle that is not a factor of 360 shows the remainder left over at 360°.",
         "A solved card shows the ladder with each rung marked."],
        "All six cards are solved.",
        ["repeatEvery", "smallestAngle", "ladder", "answer", "cardIndex"],
        ["M_ANY_SMALLEST", "M_ORDER_DISTINCT"],
        ["How many equal turns make one full turn?",
         "The smallest angle is 360° divided by the number of turns.",
         "Every other angle is that angle added again and again, up to 360°.",
         "The ladder is shown rung by rung; a similar card follows."]),
}
