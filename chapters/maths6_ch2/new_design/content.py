# -*- coding: utf-8 -*-
"""Chapter-level content for Class 6 Chapter 2, Lines and Angles (Ganita Prakash Grade 6, Chapter 2).
Book lines elsewhere are verbatim except: the book's dashes become commas or "to"; minus is U+2212."""
from __future__ import annotations

import io as _io
import json as _json
import os as _os

CHAPTER = {
    "grade": 6,
    "label": "Class 6",
    "chapter_no": 2,
    "name": "Lines and Angles",
    "book_part": "Ganita Prakash Grade 6, Chapter 2",
    "source_pdf": "textbooks/class6/fegp102.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Points, Lines, Rays and Angles",
     "A point marks a place, a line segment is the shortest path between two points, a line and a ray go on "
     "without end, and two rays from one point make an angle whose size is the amount of turn."),
    ("M2", "Comparing Angles and Special Angles",
     "Angles are compared by laying one over another or by a transparent circle. A straight angle is a half turn, "
     "a right angle is a quarter turn, and angles are sorted as acute, right or obtuse."),
    ("M3", "Measuring Angles",
     "A full turn is split into 360 equal parts called degrees. A protractor reads the number of degrees, a paper "
     "protractor shows where its marks come from, and angles turn up in clocks, doors and swings."),
    ("M4", "Drawing Angles and Types of Angles",
     "A protractor also draws an angle of a given size. Every angle is acute, right, obtuse, straight or reflex "
     "by its measure, and the summary closes the chapter."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter follows the book's order. It starts from points, segments, lines and rays, then builds "
             "the angle as a turn, compares angles by laying one over another, and only then measures and draws "
             "them in degrees.",
    "points": [
        {"title": "A turn first, a number later",
         "text": "An angle is first seen as the amount one arm turns about a point, compared by laying angles over "
                 "each other, and only afterwards given a size in degrees."},
        {"title": "Concept, then practice, topic by topic",
         "text": "Each idea gets its own topic: worked videos for the book's questions, a tool only where handling "
                 "the angle is the idea, then the book's Figure it Out questions in a practice topic, each with "
                 "its own video."},
        {"title": "Fold it, turn it, measure it",
         "text": "Paper folds make the straight angle, the right angle and a paper protractor, so the numbers on a "
                 "protractor are understood and not just read."},
        {"title": "Keeko's doubts",
         "text": "The common wrong ideas, such as 'longer arms make a bigger angle', are raised by Keeko and "
                 "fixed with a turn or an overlap, never just a rule."},
    ],
}

with _io.open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "book_items.json"), encoding="utf-8") as _f:
    NCERT_ITEMS = [_i["id"] for _i in _json.load(_f)]

MISCONCEPTIONS = [
    ("M_SEG_ANY_ROUTE", "Any route between two points, even a curved or zig-zag one, is a line segment, and "
                        "all routes are equally short."),
    ("M_LINE_ENDS", "A line has two end points and a fixed length, like a line segment."),
    ("M_ONE_LINE_POINT", "Through one point only one line can be drawn, and through two points many lines can be "
                         "drawn."),
    ("M_RAY_BOTH", "The ray OA and the ray AO are the same thing, because they use the same two letters."),
    ("M_RAY_ENDS", "A ray stops at the last point marked on it."),
    ("M_ANGLE_P", "An angle can be named by its vertex letter alone, even when more than one angle has that "
                  "vertex."),
    ("M_ARM_LENGTH", "Longer arms make a bigger angle."),
    ("M_ANGLE_AS_GAP", "The size of an angle is the distance between the tips of its arms, or the area between "
                       "them."),
    ("M_COMPARE_EYE", "The angle that looks bigger on the page is bigger, whatever way the two angles are "
                      "turned."),
    ("M_RIGHT_UPRIGHT", "A right angle must have one arm horizontal and one vertical."),
    ("M_RIGHT_ANY_L", "Any corner that looks like an L is a right angle without checking."),
    ("M_ACUTE_SMALL_DRAWING", "An angle is acute when it is drawn small, with short arms."),
    ("M_STRAIGHT_NOT_ANGLE", "A straight line is not an angle at all."),
    ("M_DEGREE_FULL", "A full turn is 100 degrees, or 180 degrees."),
    ("M_PROTRACTOR_ANYWHERE", "A protractor can be placed anywhere on the angle, as long as it touches an arm."),
    ("M_WRONG_SCALE", "Always read the inner scale, or always read the outer scale, whichever way the angle "
                      "opens."),
    ("M_START_AT_ONE", "The first mark on a protractor scale to count from is 1, not 0."),
    ("M_REFLEX_NOT_MEASURABLE", "A protractor cannot give a measure above 180 degrees, so a reflex angle has no "
                                "measure."),
    ("M_BISECT_ANY_PART", "To bisect an angle is to cut it into two parts of any size."),
    ("M_ESTIMATE_POINTLESS", "Guessing an angle is pointless when a protractor is at hand."),
    ("M_90_OBTUSE", "90 degrees counts as an obtuse angle."),
]

SOLUTION_NOTES = [
    "Items with no printed answer in the book (open ended, hands-on, drawing, craft or discussion): 2.2.q1, 2.2.q2, "
    "2.3.q1, 2.5.q1 to 2.5.q6, 2.5.FiO.Q1, 2.5.FiO.Q3, 2.6.q1, 2.6.q3, 2.6.q5, 2.7.q1, 2.8.q3, 2.8.FiO1.Q1, "
    "2.9.q3, 2.9.FiO2.Q2, 2.9.FiO2.Q8, 2.9.MtM, 2.10.act1, 2.10.act2. The answers worked here follow the expected "
    "observation, as in Chapter 9.",
    "2.9.q7: the 80 degrees is read from the picture (the base arm OB is on the 0 mark and the arm OA passes the 80 "
    "on the scale that starts at 0 on the right). It is not printed in the book. The reading was checked against "
    "the printed protractor.",
    "2.10.FiO.Q1: the book's solution lists ten angle names, but ∠CLP and ∠DLP name the same angle (C and D lie on "
    "one arm from L), so the figure gives nine different angles with named points: ∠CAP, ∠ACD, ∠APL, ∠RPL, "
    "∠PRS, ∠BRS, ∠DLP, ∠SLP and ∠LSR. The book prints no measures; the measuring is left to the child.",
    "2.10.FiO.Q3: the book prints no measure. In the figure the angle at H between HI and HJ is about 116 degrees "
    "(the same figure as the second angle of 2.9.FiO2.Q3, whose solution gives 116 degrees), not the 40 or 45 "
    "degrees guessed in the page inventory.",
    "2.11.FiO2.Q2: the book prints no values. Read from the picture, to be confirmed with a protractor: a about 45 "
    "degrees (acute), b about 165 degrees (obtuse), c about 120 degrees (obtuse), d about 32 degrees (acute), e "
    "about 97 degrees (obtuse, close to a right angle), f about 340 degrees (reflex, the arc goes round the "
    "outside).",
    "2.6.q6 and 2.6.q7: the book prints no answer for which crane has the bigger angle. In the picture Y falls "
    "almost exactly on B, so the two angles are nearly equal and the second is, if anything, very slightly "
    "smaller. The answer given here teaches the method (compare where the second arm meets the circle with B) and "
    "does not name a winner.",
    "2.5.FiO.Q4: the book's solution is ∠RTQ and ∠RTP, and the two arcs in the figure start from TR, so the "
    "printed answer is used.",
    "2.8.FiO1.Q2 and 2.8.FiO1.Q3: not in the book's solutions. The counts (3 and 2 ways for a straight angle, 5 and "
    "4 ways for a right angle) are computed from the grid positions read from the picture and should be checked "
    "against the printed grids.",
    "2.8.FiO2.Q4: the book writes the pattern as 3 × 0 + 1, 3 × 1 + 1 and so on, which counts the small triangles "
    "(1, 4, 7, 10), not the acute angles. The answer here multiplies by 3: 3, 12, 21, 30.",
    "2.9.q4: the book lists 14 angles; the straight angle ∠POU of 180 degrees is also there, which makes 15.",
    "2.9.FiO2.Q9: no printed answer; the angle sum of 180 degrees is the standard result and is stated as what "
    "the measuring shows.",
    "2.11.FiO2.Q7: the book lists whole numbers only (19, 20, 21, 22). Strictly, every angle above 18 degrees and "
    "below 22.5 degrees works.",
    "2.11.FiO1.Q1: open ended grid constructions; no solution is printed.",
]
ERRATA = [
    "2.8.FiO2.Q4: the printed pattern '3 × 0 + 1, 3 × 1 + 1, ...' does not give 3, 12, 21, 30 as written; it counts "
    "triangles. Corrected here to the number of acute angles.",
    "2.10.FiO.Q1: the printed list has ten names but two of them (∠CLP and ∠DLP) are the same angle.",
    "2.9.FiO2.Q4: the book says only 'try other ways'; the answer here is the reflex measure, 360 less 100 is "
    "260 degrees, reached by measuring the other side.",
]

DESIGN_REFERENCES = [
    {"text": "maths6_ch9 new_design Phase 2 plan: framing intro with one hook, idea topics ending in one doer, "
             "optional tool where the manipulation is the idea, a practice topic after each idea topic with one "
             "video per book question, one summary topic.",
     "url": ""},
]

FIGURES = {
    "T1.C1": ["Five dancing stick figures with arms and legs bent at different angles."],
    "T3.C2": ["A torch at T, a beam passing a lamp post at L and carrying on."],
    "T4.C1": ["A book cover opened wide, with the vertex at the spine and the cover and pages as arms."],
    "T5.C2": ["Two angles with the same vertex, laid over each other so the arms overlap."],
    "T7.C1": ["A straight angle AOB with a crease OC that folds OB onto OA."],
    "T10.C3": ["A semicircular protractor with the base arm OB on 0 and the arm OA at 80 degrees."],
}
