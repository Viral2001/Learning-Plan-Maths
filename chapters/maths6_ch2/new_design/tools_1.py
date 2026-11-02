# -*- coding: utf-8 -*-
"""Tool specs for the opening topics: name_it, angle_namer, angle_comparer. Doer tools only."""
from topics_common import T

TOOLS = {
    "name_it": T(
        "tool_m1t3c3", "Name It", "manipulative",
        "A line, a ray and a line segment are told apart by their ends, and each is named with its letters in the "
        "right order.",
        "A figure with points on a sheet; a toolbar to draw a segment, a ray or a line through two points; a "
        "name box that takes letters; a check button.",
        ["Predict which of segment, ray or line the picture shows.",
         "Draw or choose the object between the marked points.",
         "Type its name with the letters in the right order."],
        ["Two points A and B joined by the shortest path: name the segment.",
         "A ray from O through P: name it (OP, not PO).",
         "A line through points L and M: name it.",
         "Points A, B and C on one line: list every segment on it.",
         "A ray from a torch T through a lamp L: which of TL and LT matches it.",
         "Through one point draw as many lines as you can, then through two points."],
        ["A segment drawn with a curve shows the straight one shorter beside it.",
         "A ray named with the end point second is shown pointing the other way.",
         "A solved card shows the object with its name and its ends marked."],
        "All six cards are named correctly.",
        ["tool", "points", "name", "answer", "cardIndex"],
        ["M_SEG_ANY_ROUTE", "M_LINE_ENDS", "M_ONE_LINE_POINT", "M_RAY_BOTH", "M_RAY_ENDS"],
        ["What does the picture have at its ends: two, one or none?",
         "A segment has two ends, a ray one, and a line none. The end point comes first in the name of a ray.",
         "Look at the end point of the ray and write its letter first, then a point on the ray.",
         "The object is shown with its ends marked; a similar card follows."]),

    "angle_namer": T(
        "tool_m1t4c3", "Name the Angle", "manipulative",
        "An angle is named with three letters, the vertex in the middle, and the arms are the two rays from the "
        "vertex.",
        "A figure of rays from points; tap two arms to highlight an angle with an arc; three letter boxes for "
        "the name; a check button.",
        ["Predict which angle the arc shows.",
         "Tap two arms, or read the arc on the figure.",
         "Type the name with the vertex in the middle."],
        ["One angle with arms OA and OB: name it.", "The same angle written the other way round.",
         "Three rays from one vertex: name all three angles.",
         "An arc drawn between two arms on a bigger figure: name the angle shown.",
         "Two angles with the same vertex: why one letter is not enough.",
         "A figure with four points on two lines: list every angle."],
        ["A name with the vertex at the end shows the angle it describes, which is a different one.",
         "A single letter shows the other angles at that vertex.",
         "A solved card shows the arc and the name with the vertex in the middle."],
        "All six cards are named correctly.",
        ["arms", "arc", "name", "answer", "cardIndex"],
        ["M_ANGLE_P"],
        ["Which point do the two arms start from?",
         "The vertex goes in the middle of the name.",
         "Write one point on an arm, then the vertex, then a point on the other arm.",
         "The angle is shown with its arc and name; a similar card follows."]),

    "angle_comparer": T(
        "tool_m2t5c4", "Which Angle Is Greater?", "manipulative",
        "Two angles are compared by laying one over the other with the vertices and one arm together; the one "
        "whose second arm falls outside is greater.",
        "Two angles on a sheet; a drag handle to move and turn one angle onto the other; a ghost copy that "
        "stays; buttons Greater, Smaller, Equal.",
        ["Predict which angle is greater before moving.",
         "Drag one angle over the other with the vertex and one arm together.",
         "Choose greater, smaller or equal."],
        ["Two angles with long and short arms: which is greater.",
         "Two angles that look equal but one has longer arms.",
         "Two angles turned in different directions.",
         "Three angles: order them from smallest to largest.",
         "Two angles that are equal but drawn differently.",
         "Two angles very close in size: compare on a transparent circle."],
        ["A pair laid with the vertices apart shows why the comparison does not yet work.",
         "Arms of different lengths are shown trimmed to the same length to show the angles unchanged.",
         "A solved card shows the angles laid together with the outside arm marked."],
        "All six comparisons are correct.",
        ["angleA", "angleB", "overlay", "answer", "cardIndex"],
        ["M_ARM_LENGTH", "M_COMPARE_EYE", "M_ANGLE_AS_GAP"],
        ["What two things must meet before you compare the angles?",
         "Put the vertices together and one arm on one arm. Then look at the other arms.",
         "Whichever second arm lies outside the other belongs to the greater angle.",
         "The angles are shown laid together with the greater one marked; a similar pair follows."]),
}
