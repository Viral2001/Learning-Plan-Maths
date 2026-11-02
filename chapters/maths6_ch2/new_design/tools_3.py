# -*- coding: utf-8 -*-
"""Tool specs for measuring, drawing and sorting: protractor_reader, angle_drawer, angle_classifier."""
from topics_common import T

TOOLS = {
    "protractor_reader": T(
        "tool_m3t12c2", "Protractor Reader", "manipulative",
        "To measure an angle, put the protractor centre on the vertex and one arm on 0, then read the scale "
        "that starts at 0 on that arm.",
        "A protractor that can be dragged and turned over an angle; a highlighted 0 mark; a number box for the "
        "reading; a check button.",
        ["Predict whether the angle is acute or obtuse.",
         "Drag and turn the protractor so the centre sits on the vertex and one arm on 0.",
         "Read the scale that starts at 0 and type the number."],
        ["An acute angle with the base arm on the left.", "An obtuse angle with the base arm on the right.",
         "An angle that opens upward and one that opens downward.",
         "Two angles at one vertex: find the angle between by two readings.",
         "An angle read from the wrong scale: find the mistake.",
         "The three angles of a triangle: measure and add."],
        ["A reading from the wrong scale shows the angle's size beside the number and a clue.",
         "A protractor not centred shows the centre dot off the vertex.",
         "A solved card shows the protractor placed with the reading marked."],
        "All six angles are measured correctly.",
        ["protractorPosition", "scale", "reading", "answer", "cardIndex"],
        ["M_PROTRACTOR_ANYWHERE", "M_WRONG_SCALE", "M_START_AT_ONE"],
        ["Is the angle smaller or bigger than a right angle?",
         "Put the centre on the vertex, one arm on 0, and read the scale that starts at 0 there.",
         "If the angle is acute, the reading is less than 90.",
         "The protractor is shown placed correctly with the reading; a similar card follows."]),

    "angle_drawer": T(
        "tool_m4t14c3", "Draw the Angle", "manipulative",
        "To draw an angle, draw one arm, set the protractor centre and the 0 mark on it, mark the measure, and "
        "join to the vertex.",
        "A sheet with a ray; a draggable protractor; a dot tool for the mark; a Join button; a check that reads "
        "the finished angle.",
        ["Predict where on the scale the mark will go.",
         "Put the protractor on the arm and mark the measure.",
         "Join the vertex to the mark."],
        ["Draw a 30 degree angle.", "Draw a 75 degree angle.", "Draw a 120 degree angle.",
         "Draw an angle with the base arm on the right.", "Draw an angle equal to a given angle.",
         "Draw a 140 degree angle."],
        ["A mark on the wrong scale shows the angle that was drawn and its measure.",
         "An arm not on 0 shows the offset between the arm and the mark.",
         "A solved card shows the finished angle with its measure."],
        "All six angles are drawn within 2 degrees.",
        ["armPosition", "mark", "measure", "answer", "cardIndex"],
        ["M_WRONG_SCALE", "M_START_AT_ONE", "M_ANGLE_P"],
        ["Which arm is already drawn, and where is the 0 mark?",
         "Mark the number on the scale that starts at 0 on your base arm.",
         "For 120, count from the 0 mark to the 120 mark and put the dot there.",
         "The mark is shown on the scale; a similar card follows."]),

    "angle_classifier": T(
        "tool_m4t15c4", "Sort the Angle", "manipulative",
        "Every angle is acute, right, obtuse, straight or reflex, decided by comparing its measure with 90, 180 "
        "and 360.",
        "An angle with a draggable arm and a live measure; five labelled bins; an estimate box; a check "
        "button.",
        ["Predict the type and estimate the measure.",
         "Turn the arm to the target or read the measure.",
         "Drop the angle into its bin."],
        ["An angle of 35: acute.", "An angle of 90: right.", "An angle of 120: obtuse.",
         "An angle of 180: straight.", "An angle of 260: reflex.",
         "Estimate an angle, then measure it, and name its type."],
        ["An angle of exactly 90 placed in obtuse shows the right angle mark.",
         "A reflex angle measured on the small side shows the 360 minus rule.",
         "A solved card shows the angle with its measure and type."],
        "All six angles are sorted and measured.",
        ["measure", "type", "estimate", "answer", "cardIndex"],
        ["M_90_OBTUSE", "M_REFLEX_NOT_MEASURABLE", "M_ESTIMATE_POINTLESS"],
        ["Is the angle smaller than a right angle?",
         "Under 90 is acute, 90 is right, 90 to 180 is obtuse, 180 is straight, over 180 is reflex.",
         "Compare the measure with 90 and 180 in turn.",
         "The angle is shown with its type; a similar card follows."]),
}
