# -*- coding: utf-8 -*-
"""Chapter-level content for Class 7 Chapter 14, Constructions and Tilings (Ganita Prakash Grade 7 Part II, Chapter 6).
Book lines elsewhere are verbatim except: the book's dashes become commas, colons or "to"; minus is U+2212.

Scope (workflow instruction): the perpendicular bisector, a right angle at a point, angle bisection, copying an
angle, the parallel line, the regular hexagon with 60, 120, 30 and 15 degree angles, the six-pointed star, the
perpendicular from an outside point, tiling with 2 by 1 tiles and the colouring argument, and tiling the plane.
Left out: the rope (Sulba) constructions and their questions, the arch designs and their questions, the tangram
pieces and their questions, the free design questions after the star (figures a to e, the optical illusion, the
star in a hexagon), the pure figure-recreation questions (perpendicular bisector
Q4, the eight-petal figure in angle bisection Q2, the sector-row figure in copying-an-angle Q2; the eight-petal
construction and the repeating unit stay taught in the text), the rope question in the angle-bisection set, and the parallel-lines figure question (its
outer points carry no lengths or angles, so it cannot be stated exactly)."""
from __future__ import annotations

CHAPTER = {
    "grade": 7,
    "label": "Class 7",
    "chapter_no": 14,
    "name": "Constructions and Tilings",
    "book_part": "Ganita Prakash Grade 7 Part II, Chapter 6",
    "source_pdf": "textbooks/class7/gegp206.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Equal Distances: the Perpendicular Bisector",
     "Two eyes drawn with a compass lead to the perpendicular bisector. Congruent triangles explain why it cuts the "
     "segment in half at a right angle, and the same arcs give a right angle at any point on a line."),
    ("M2", "Bisecting and Copying Angles",
     "Equal arcs and the SSS condition halve an angle and copy an angle anywhere; a copied corresponding angle gives "
     "a line parallel to a given line."),
    ("M3", "Regular Hexagons and Special Angles",
     "Six equilateral triangles fit round a point because their angles add to 360°. That gives the regular hexagon, "
     "the 60° and 120° constructions, 30° and 15° by halving, the six-pointed star and the perpendicular from a "
     "point outside a line."),
    ("M4", "Tiling",
     "Covering a region with 2 × 1 tiles: counting squares, the even and odd cases of an m × n grid, the "
     "black-and-white colouring argument, and shapes that tile the whole plane."),
    ("M5", "Summary",
     "The chapter's constructions and the tiling ideas in one place."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "Every construction uses only an unmarked ruler and a compass, and every one is followed by its reason: "
             "which triangles are congruent, and by which condition. The chapter opens with a pair of eyes drawn "
             "with two arcs and ends with tilings, where counting and colouring decide what is possible.",
    "points": [
        {"title": "Try first, name later",
         "text": "The hook video leaves the eyes question open: where must the compass point go so that both arcs "
                 "meet at the corners? The perpendicular bisector is named only after the student has found the "
                 "two centres."},
        {"title": "Every step has a reason",
         "text": "Each construction is justified by congruent triangles: SSS for the bisector, the copied angle "
                 "and the angle bisector, SAS for the right angle at the midpoint, and an equilateral triangle for "
                 "60°."},
        {"title": "Concept, then practice, topic by topic",
         "text": "Each idea gets its own topic: one video per concept, a closing practice concept (with a tool where "
                 "the manipulation is the idea), then the book's Figure it Out questions in their own topic, one "
                 "question and one video per concept."},
        {"title": "Counting and colouring decide tilings",
         "text": "A 2 × 1 tile covers two squares, and one black and one white on a chessboard colouring. An odd "
                 "count, or unequal black and white counts, shows a region can never be tiled."},
    ],
}

# Coverage ids for the in-scope book items (teaching lines, in-text questions and Figure it Out questions).
NCERT_ITEMS = [
    "opening.eyes",
    # 6.1 perpendicular bisector
    "6.1.eye_centres", "6.1.why_bisector", "6.1.equidistant", "6.1.pb_steps",
    "6.1.FiO_pb1", "6.1.FiO_pb2", "6.1.FiO_pb3",
    "6.1.right_angle",
    # angle bisection
    "6.1.bisect_method", "6.1.bisect_45",
    "6.1.FiO_ab1", "6.1.FiO_ab3", "6.1.FiO_ab4", "6.1.FiO_ab6",
    # copying an angle and the parallel line
    "6.1.copy_steps", "6.1.FiO_ca1",
    "6.1.parallel_steps", "6.1.FiO_pl1",
    # regular hexagon
    "6.1.hex_triangles", "6.1.gap_360", "6.1.straight_lines",
    "6.1.angle_60", "6.1.angle_120", "6.1.hex_4cm", "6.1.hex_5cm",
    "6.1.angle_30", "6.1.angle_15", "6.1.star", "6.1.FiO_perp_outside",
    # 6.2 tiling
    "6.2.tiling_def", "6.2.grid_4x6", "6.2.grid_4x7", "6.2.grid_5x7",
    "6.2.mn_even", "6.2.mn_mixed", "6.2.mn_odd",
    "6.2.minus_corner", "6.2.minus_middle", "6.2.colour_613", "6.2.colour_another",
    "6.2.FiO_t1", "6.2.FiO_t2",
    "6.2.plane",
    "summary",
]

LEFT_OUT = [
    "Sulba-Sutra rope construction of a right angle and its Figure it Out (2 questions)",
    "Angle-bisection Figure it Out, question 5 (rope)",
    "Arch designs (trefoil, pointed) and their Figure it Out (2 questions)",
    "Figure it Out after the six-pointed star: question 1 (a) to (e), question 2 (optical illusion), "
    "question 3 (star in a hexagon)",
    "Parallel-lines Figure it Out, question 2 (the eight-pointed figure: no lengths or angles are given for its "
    "outer points, so it cannot be stated exactly)",
    "Pure figure-recreation Figure it Out questions: perpendicular bisector Q4 (four-petal design), angle "
    "bisection Q2 (8-petalled figure), copying an angle Q2 (sector row); the 8-petal method stays taught in-text",
    "Tangram pieces and their Figure it Out (10 figures)",
    "Pentagon Try This (construction deferred to later years by the book itself)",
]

MISCONCEPTIONS = [
    ("M_SAME_RADIUS_ALL", "Every arc in the perpendicular bisector construction must use one and the same radius."),
    ("M_RADIUS_SMALL", "Any radius works for the bisector arcs, even one less than half the segment."),
    ("M_MIDPOINT_ONLY", "The perpendicular bisector only passes through the midpoint; it need not be at a right angle."),
    ("M_EQUIDISTANT_OFF", "A point can be the same distance from X and Y without lying on the perpendicular bisector."),
    ("M_ARC_RADIUS_CHANGE", "When copying or bisecting an angle, the second arc may use any new radius."),
    ("M_ANGLE_ARM_LENGTH", "A longer arm or a bigger drawing makes a bigger angle."),
    ("M_CONGRUENCE_GUESS", "Two triangles that look alike are congruent; no condition needs to be named."),
    ("M_ANY_ANGLE_BISECT", "Repeated halving can give any angle, such as 65.5°."),
    ("M_GAP_GUESS", "An angle fits a gap round a point if it looks about the right size."),
    ("M_HEX_ANGLE_60", "Each angle of a regular hexagon is 60°, the same as the triangles inside it."),
    ("M_EVEN_ENOUGH", "A region with an even number of squares can always be tiled with 2 × 1 tiles."),
    ("M_TILE_COLOUR", "A 2 × 1 tile can cover two black squares of a chessboard colouring."),
]

SOLUTION_NOTES = [
    "Tiling Figure it Out 1: the region (rows 2, 2, 4, 4 squares, the two short rows on the left) has 12 squares and "
    "a tiling with four L-shaped 3-square tiles exists (checked by an exhaustive search); it is unique, and it "
    "needs the tile turned to different positions, as the book allows turning a 2 × 1 tile.",
    "Tiling Figure it Out 2: an 8 × 8 grid with the top-right and bottom-left corner squares removed; both removed "
    "squares have the same colour, leaving 32 of one colour and 30 of the other, so it cannot be tiled with 2 × 1 "
    "tiles (checked by colour count).",
    "5 × 3 grid with one square removed (corners white): tileable exactly when the removed square is white "
    "(8 such squares); removing any of the 7 black squares leaves 8 white and 6 black, which cannot be tiled "
    "(checked by exhaustive search).",
    "65.5° cannot be made by halving: from 90° and 60° the angles reachable by repeated halving are multiples of 15° "
    "divided by a power of 2 (and their sums); 65.5 × 2ⁿ is never a multiple of 15 (65.5 = 131/2 and 131 is prime).",
]
ERRATA = []

DESIGN_REFERENCES = [
    {"text": "docs/25_new_design_learning_plan_playbook.md: framing intro, idea topics ending in "
             "a practice concept, a question topic after each idea topic, and one summary topic; the Class 7 "
             "Chapter 10 plan for one video per concept and one question per concept.", "url": ""},
]

FIGURES = {
    "T1.C1": ["Two eyes, each a lens shape made of two arcs, drawn side by side; each eye has corners X and Y."],
    "T2.C2": ["The eye with points X and Y, the arc centres A and B, the line A B crossing X Y at O."],
}
