# -*- coding: utf-8 -*-
"""Chapter-level content for Class 7 Chapter 7, A Tale of Three Intersecting Lines (Ganita Prakash Grade 7 Part I,
Chapter 7). Book lines elsewhere are verbatim except: the book's dashes become commas, colons or "to"; minus is
U+2212."""
from __future__ import annotations

CHAPTER = {
    "grade": 7,
    "label": "Class 7",
    "chapter_no": 7,
    "name": "A Tale of Three Intersecting Lines",
    "book_part": "Ganita Prakash Grade 7 Part I, Chapter 7",
    "source_pdf": "textbooks/class7/gegp107.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Triangles from Three Lengths",
     "Building equilateral and other triangles with a ruler and compass, the lengths that cannot make a triangle, "
     "the triangle inequality, and why the circles meet exactly when it holds."),
    ("M2", "Triangles from Angles",
     "Triangles from two sides and the angle between them, from two angles and the side between them, when two "
     "angles fail, the third angle, the angle sum and exterior angles."),
    ("M3", "Altitudes and Kinds of Triangles",
     "Altitudes inside and outside a triangle, right-angled triangles, and sorting triangles by their sides and by "
     "their angles."),
    ("M4", "Puzzle and Summary",
     "The shortest path for a spider across a box, and a closing summary of the chapter."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter follows the book's own order: triangles from three lengths first, then triangles from "
             "angles, then altitudes and kinds of triangles. Every rule is reached by building a triangle and "
             "asking when it cannot be built, so a rule such as the triangle inequality is a finding and not a "
             "fact to memorise.",
    "points": [
        {"title": "Try first, name later",
         "text": "The hook video leaves one question open: what happens when three corner points lie on a straight "
                 "line. The compass construction and the triangle inequality arrive only after the student has "
                 "tried to build triangles."},
        {"title": "When a triangle cannot be built",
         "text": "For lengths, for two sides and an angle, and for two angles and a side, the chapter asks when the "
                 "construction fails. Each failure leads to a rule: the triangle inequality, an angle below 180 "
                 "degrees, and two angles that add to less than 180 degrees."},
        {"title": "Parallel lines explain the angles",
         "text": "One line drawn through a vertex parallel to the opposite side explains why two angles must add to "
                 "less than 180 degrees, how to find the third angle, and why the three angles always add to 180 "
                 "degrees."},
        {"title": "Concept, then practice, topic by topic",
         "text": "Each idea gets its own topic with one video per concept and a practice concept at the end; "
                 "interactive tools appear only where handling the figure is the idea. The book's questions follow "
                 "in their own topic, one question and one video per concept."},
    ],
}

NCERT_ITEMS = [
    "opening", "opening.collinear",
    # 7.1 Equilateral triangles
    "7.1.ruler", "7.1.compass",
    # 7.2 Sides given
    "7.2.build", "7.2.why", "7.2.steps", "7.2.iso",
    "7.2.construct", "7.2.FiOA1", "7.2.FiOA2",
    # impossible lengths and the triangle inequality
    "imp.try", "imp.more", "ti.path", "ti.ex", "ti.337", "ti.mathtalk", "ti.def",
    "ti.FiOB1", "ti.FiOB2", "ti.FiOB3",
    "c458.exists", "c458.why_longest", "c458.circles", "c458.FiOC1",
    "case.three", "case.touch", "case.apart", "case.overlap", "case.examples", "case.procedure",
    "case.conclusion", "case.FiOD1", "case.FiOD2", "case.FiOD3",
    # 7.3 Sides and angles given
    "sas.included", "sas.construct", "sas.FiOE1", "sas.FiOE2",
    "asa.included", "asa.construct", "asa.mathtalk", "asa.FiOF1",
    "ang.always", "ang.find", "ang.visual", "ang.ninety", "ang.forty", "ang.parallel",
    "ang.FiOG1", "ang.FiOG2", "ang.FiOG3",
    "third.same", "third.data", "third.parallel", "third.FiOH1", "third.FiOH2", "third.FiOH3",
    "sum.property", "sum.history", "sum.fold",
    "ext.def", "ext.ex", "ext.relation",
    # 7.4 Altitudes
    "alt.height", "alt.others", "alt.obtuse", "alt.fold", "alt.setsquare", "alt.right",
    # 7.5 Types of triangles
    "types.sides", "types.angles", "types.acute",
    "types.FiOI1", "types.FiOI2", "types.FiOI3", "types.FiOI4",
    "puzzle.spider", "summary",
]

MISCONCEPTIONS = [
    ("M_ANY_LENGTHS", "A triangle can be built from any three lengths."),
    ("M_TWO_COMPARISONS", "Only two of the three lengths need to be compared, or the two shorter lengths can be "
                          "compared with each other instead of with the longest."),
    ("M_SUM_EQUALS", "When the two shorter lengths add up to exactly the longest length, a triangle can still be "
                     "built."),
    ("M_ANGLE_TOO_BIG", "Any angle, even 180 degrees or more, can be used between two sides of a triangle."),
    ("M_ANGLE_PAIR", "Any two angles can be the angles of a triangle, however big they are."),
    ("M_THIRD_ANGLE_SIDE", "The third angle of a triangle depends on how long the side between the two given "
                           "angles is."),
    ("M_ALTITUDE_INSIDE", "An altitude always lies inside the triangle, and it is always one of the sides."),
    ("M_ACUTE_ONE", "An acute-angled triangle is a triangle with one acute angle."),
    ("M_EXTERIOR_ANGLE", "An exterior angle equals the angle next to it, or the third angle of the triangle."),
    ("M_EQUILATERAL_RIGHT", "An equilateral triangle can have a right angle or an obtuse angle."),
]

SOLUTION_NOTES = [
    "Figure it Out (two sides and the included angle) follow-up: the book's key says a triangle is not possible "
    "when the included angle is 180 degrees or more. The plan teaches the same rule and adds that the angle must "
    "also be more than 0 degrees: the angle must lie strictly between 0 and 180 degrees.",
    "Figure it Out (triangles from angles) Q3 and the rule questions: the book asks for a rule on two angles "
    "without a number; the plan states it as: the two angles must be more than 0 degrees each and add to less "
    "than 180 degrees.",
    "Two angles and the included side: the Math Talk box on that page has no text in the source; nothing is "
    "taught from it, and the plan covers the same ground in the next idea (when do two angles fail).",
    "Figure it Out (circles and triangles) Q1 and Q2 depend on figures: the plan describes them in words (one "
    "circle with its centre marked; two and then three circles of the same size, each passing through the "
    "centres of the others) and solves them from that description.",
    "Shortest Path in a Box: the book's hint figure shows the box laid flat. The plan uses a box 6 cm long, 4 cm "
    "wide and 3 cm high, lays two faces flat, and compares the three possible straight paths by measuring on the "
    "drawn flat faces; the shortest is about 9.2 cm.",
]
ERRATA = []

DESIGN_REFERENCES = [
    {"text": "docs/25_new_design_learning_plan_playbook.md: framing intro, idea topics ending in "
             "a practice concept, a question topic after each idea topic, and one summary topic; the Class 7 "
             "Chapter 10 plan for one video per concept and one question per concept.", "url": ""},
]

FIGURES = {
    "T1.C1": ["Three roof beams of a shed pushed flat until they lie on one straight line."],
    "T2.C2": ["Base AB of 4 cm with two arcs of radius 4 cm from A and from B crossing at C."],
    "T3.C1": ["Base AB of 4 cm, an arc of radius 5 cm from A and an arc of radius 6 cm from B crossing at C."],
    "T5.C1": ["Base AB of 8 cm, a circle of radius 4 cm at A and a circle of radius 5 cm at B crossing in two "
              "points, with X the point where the circle at A meets AB."],
    "T6.C1": ["Two circles on the base AB: touching at one point, apart, and overlapping."],
    "T7.C2": ["Base AB of 5 cm, an angle of 45 degrees at A, and C marked 4 cm along the other arm."],
    "T8.C1": ["Base AB of 5 cm with an angle of 45 degrees at A and 80 degrees at B, the arms crossing at C."],
    "T9.C2": ["Base AB, an angle of 40 degrees at A, the line l along the other arm, and the parallel line m "
              "through B that never meets l."],
    "T10.C2": ["Triangle ABC with a line XY through A parallel to BC, marking the angles XAB and YAC."],
    "T12.C2": ["An obtuse triangle with BC extended and the perpendicular from A meeting the extension."],
    "T14.C1": ["A box with a spider at one corner and the opposite corner marked, and two faces laid flat."],
}

# Hook slot extras (build.py passes these into the hook's worklist slot).
HOOK_HANDOVER = ("Try it: take three sticks of different lengths and see how many different triangles you can "
                 "make, and what happens when two sticks are laid end to end along the third.")
HOOK_NOTE = ("The hook leaves the question open: do not say that a triangle cannot be built, and do not say how "
             "long the beams are. The compass construction and the triangle inequality settle it later.")

# Words the narration may need that are hard for a Class 7 reader; the script author defines or avoids them.
HARD_WORDS = ["vertex", "vertices", "included", "altitude", "perpendicular", "inequality", "scalene", "isosceles",
              "equilateral", "obtuse", "acute", "transversal", "exterior", "collinear"]
