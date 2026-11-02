# -*- coding: utf-8 -*-
"""Chapter-level content for Class 6 Chapter 8, Playing with Constructions (Ganita Prakash Grade 6, Chapter 8).
Book lines elsewhere are verbatim except: the book's dashes become commas, colons or "to"; minus is U+2212.
Lengths and roots are written as measurements ("about 7.2 cm"), never as equations between bare numbers."""
from __future__ import annotations

CHAPTER = {
    "grade": 6,
    "label": "Class 6",
    "chapter_no": 8,
    "name": "Playing with Constructions",
    "book_part": "Ganita Prakash Grade 6, Chapter 8",
    "source_pdf": "textbooks/class6/fegp108.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "The Compass and Circles",
     "A compass keeps one distance fixed, so it draws circles and arcs. Circles, half circles and arcs build "
     "faces, waves and other artwork."),
    ("M2", "Squares and Rectangles",
     "What makes a square and a rectangle, how to construct them with a ruler and a compass, and how rectangles "
     "break into squares."),
    ("M3", "Diagonals of Rectangles",
     "The diagonals of a rectangle are equal, and they split the corners into angles. A rectangle is built from "
     "the angle of a diagonal, or from a side and a diagonal."),
    ("M4", "Equal Distances and Summary",
     "Two arcs of one radius find the point that is the same distance from two points; this builds the house and "
     "a figure with four equal sides that is not a square."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter follows the book's order. A compass keeps one distance fixed, so circles and arcs give "
             "exact lengths; squares and rectangles are then built from their properties, and the same two ideas, "
             "perpendiculars and arcs, find every corner.",
    "points": [
        {"title": "Draw, then reason",
         "text": "Each construction starts from a rough diagram and a prediction, then the steps are carried out "
                 "and checked with a ruler and a protractor."},
        {"title": "Concept, then practice, topic by topic",
         "text": "Each idea gets its own topic: worked videos for the book's examples, one tool to do it by hand "
                 "where the manipulation is the idea, then the book's construction questions in a practice topic."},
        {"title": "Properties do the work",
         "text": "A square and a rectangle have fixed properties, so we measure only what is needed and the "
                 "properties give the remaining sides and angles."},
        {"title": "Keeko's doubts",
         "text": "Wrong ideas such as 'a square is not a rectangle' or 'a diagonal always splits a corner into "
                 "two equal angles' are raised by Keeko and fixed with a drawing, never just a rule."},
    ],
}

# Every book item, in book order. Ids come from the page-image inventory.
NCERT_ITEMS = [
    "opening",
    "8.1.q1", "8.1.q2", "8.1.q3", "8.1.q4", "8.1.q5", "8.1.q6", "8.1.ex1", "8.1.ex2", "8.1.ex3",
    "8.1.FiO.Q1", "8.1.FiO.Q2", "8.1.FiO.Q3", "8.2.q1", "8.2.q2", "8.2.q3", "8.2.q4", "8.2.FiO.Q1",
    "8.2.FiO.Q2", "8.2.q5", "8.2.FiO.Q3", "8.3.ex1", "8.3.q1", "8.3.q2", "8.3.ex2", "8.3.ex3", "8.3.q3",
    "8.4.ex1", "8.4.q1", "8.4.q2", "8.4.q3", "8.4.q4", "8.4.q5", "8.4.q6", "8.4.q7", "8.4.ex2", "8.4.ex3",
    "8.4.q8", "8.4.ex4", "8.4.ex5", "8.4.ex6", "8.4.ex7", "8.4.ex8", "8.4.ex9", "8.5.q1", "8.5.q2",
    "8.5.q3", "8.5.q4", "8.5.q5", "8.5.q6", "8.5.q7", "8.5.ex1", "8.5.q8", "8.5.ex2", "8.5.q9", "8.5.q10",
    "8.5.q11", "8.5.q12", "8.5.FiO.Q1", "8.5.FiO.Q2", "8.5.FiO.Q3", "8.5.FiO.Q4", "8.6.ex1", "8.6.q1",
    "8.6.q2", "8.6.FiO.Q1", "8.6.FiO.Q2", "8.6.FiO.Q3",
    "summary",
]

ITEM_HOME = {
    "opening": ("T1", "T1.C1", "HOOK"),
    "8.1.q1": ("T2", "T2.C1", "WE"),
    "8.1.q2": ("T2", "T2.C2", "WE"),
    "8.1.q3": ("T2", "T2.C2", "WE"),
    "8.1.q4": ("T2", "T2.C3", "WE"),
    "8.1.q5": ("T2", "T2.C3", "WE"),
    "8.1.q6": ("T2", "T2.C4", "FIO"),
    "8.1.ex1": ("T4", "T4.C1", "WE"),
    "8.1.ex2": ("T3", "T3.C1", "WE"),
    "8.1.ex3": ("T4", "T4.C2", "WE"),
    "8.1.FiO.Q1": ("T3", "T3.C2", "FIO"),
    "8.1.FiO.Q2": ("T3", "T3.C2", "FIO"),
    "8.1.FiO.Q3": ("T4", "T4.C3", "FIO"),
    "8.2.q1": ("T5", "T5.C1", "WE"),
    "8.2.q2": ("T5", "T5.C2", "WE"),
    "8.2.q3": ("T5", "T5.C2", "WE"),
    "8.2.q4": ("T6", "T6.C1", "WE"),
    "8.2.FiO.Q1": ("T6", "T6.C3", "FIO"),
    "8.2.FiO.Q2": ("T5", "T5.C3", "FIO"),
    "8.2.q5": ("T6", "T6.C2", "WE"),
    "8.2.FiO.Q3": ("T6", "T6.C3", "FIO"),
    "8.3.ex1": ("T7", "T7.C1", "WE"),
    "8.3.q1": ("T7", "T7.C2", "WE"),
    "8.3.q2": ("T7", "T7.C2", "WE"),
    "8.3.ex2": ("T8", "T8.C2", "FIO"),
    "8.3.ex3": ("T8", "T8.C2", "FIO"),
    "8.3.q3": ("T8", "T8.C1", "WE"),
    "8.4.ex1": ("T9", "T9.C1", "WE"),
    "8.4.q1": ("T9", "T9.C1", "WE"),
    "8.4.q2": ("T9", "T9.C1", "WE"),
    "8.4.q3": ("T9", "T9.C2", "WE"),
    "8.4.q4": ("T9", "T9.C2", "WE"),
    "8.4.q5": ("T9", "T9.C3", "WE"),
    "8.4.q6": ("T9", "T9.C3", "WE"),
    "8.4.q7": ("T9", "T9.C3", "WE"),
    "8.4.ex2": ("T10", "T10.C2", "WE"),
    "8.4.ex3": ("T10", "T10.C1", "WE"),
    "8.4.q8": ("T10", "T10.C3", "WE"),
    "8.4.ex4": ("T10", "T10.C4", "FIO"),
    "8.4.ex5": ("T11", "T11.C2", "FIO"),
    "8.4.ex6": ("T11", "T11.C2", "FIO"),
    "8.4.ex7": ("T11", "T11.C1", "WE"),
    "8.4.ex8": ("T11", "T11.C2", "FIO"),
    "8.4.ex9": ("T11", "T11.C2", "FIO"),
    "8.5.q1": ("T12", "T12.C1", "WE"),
    "8.5.q2": ("T12", "T12.C2", "WE"),
    "8.5.q3": ("T12", "T12.C2", "WE"),
    "8.5.q4": ("T13", "T13.C1", "WE"),
    "8.5.q5": ("T13", "T13.C3", "FIO"),
    "8.5.q6": ("T13", "T13.C3", "FIO"),
    "8.5.q7": ("T13", "T13.C2", "WE"),
    "8.5.ex1": ("T14", "T14.C1", "WE"),
    "8.5.q8": ("T14", "T14.C1", "WE"),
    "8.5.ex2": ("T15", "T15.C1", "WE"),
    "8.5.q9": ("T15", "T15.C1", "WE"),
    "8.5.q10": ("T15", "T15.C2", "WE"),
    "8.5.q11": ("T15", "T15.C2", "WE"),
    "8.5.q12": ("T15", "T15.C3", "WE"),
    "8.5.FiO.Q1": ("T14", "T14.C2", "FIO"),
    "8.5.FiO.Q2": ("T14", "T14.C2", "FIO"),
    "8.5.FiO.Q3": ("T15", "T15.C4", "FIO"),
    "8.5.FiO.Q4": ("T15", "T15.C4", "FIO"),
    "8.6.ex1": ("T16", "T16.C2", "WE"),
    "8.6.q1": ("T16", "T16.C1", "WE"),
    "8.6.q2": ("T16", "T16.C1", "WE"),
    "8.6.FiO.Q1": ("T16", "T16.C3", "FIO"),
    "8.6.FiO.Q2": ("T17", "T17.C2", "FIO"),
    "8.6.FiO.Q3": ("T17", "T17.C2", "FIO"),
    "summary": ("T18", "T18.C1", "RECAP"),
}

assert set(ITEM_HOME) == set(NCERT_ITEMS), set(ITEM_HOME) ^ set(NCERT_ITEMS)

MISCONCEPTIONS = [
    ("M_FREEHAND_CIRCLE", "A circle drawn by hand is good enough, so no tool is needed to make it round."),
    ("M_RULER_END", "Measure a length from the end of the ruler, not from its zero mark."),
    ("M_RADIUS_DIAMETER", "The opening of the compass is the width of the circle, so radius 3 cm gives a circle "
                          "3 cm across."),
    ("M_ARC_TIP_ON_FIGURE", "The compass tip always goes on the figure itself, so an arc that bulges inward is "
                            "drawn from a point on the side."),
    ("M_SQUARE_NOT_RECT", "A square is not a rectangle, because a rectangle has a long side and a short side."),
    ("M_EQUAL_SIDES_SQUARE", "Any four-sided figure with four equal sides is a square."),
    ("M_NAME_ANY_ORDER", "The corners of a figure can be named in any order, and a construction can be done in "
                         "any order."),
    ("M_TILT_NOT_SQUARE", "A square turned on its corner is a different shape and is no longer a square."),
    ("M_SLANT_SHORTER", "A slanting line across a rectangle is shorter than a straight one, because it looks "
                        "closer."),
    ("M_SPLIT_ANY", "Any rectangle can be cut into two or into three identical squares."),
    ("M_CENTRE_ON_SIDE", "The centre of a square is found anywhere on one of its sides."),
    ("M_DIAG_EQUAL_SQUARE", "A rectangle whose diagonals are equal must be a square."),
    ("M_DIAG_BISECT_ANGLES", "The diagonal of a rectangle always splits each corner into two equal angles."),
    ("M_ARC_FROM_ONE_POINT", "One arc is enough to fix a point that is a given distance from two points."),
]

SOLUTION_NOTES = [
    "8.1.ex1, 8.1.ex3: the book gives no measurements; the radii used in the plan are chosen examples.",
    "8.2.FiO.Q1, 8.2.FiO.Q2: dot counts are read from the picture and are approximate; the answers agree with "
    "the book.",
    "8.4.q3: the book answers 7.43 cm, 7.00 cm and 7.28 cm are confirmed; in the figure for case 2 the book "
    "marks Y 2 cm from B, while the text says 1 cm. The plan follows the text.",
    "8.4.q5: the printed solution copies the question table with distances of 5 cm, 1 cm and 4 cm for Y, while "
    "the chapter has 5 mm, 1 cm and 1 cm 5 mm. The answer, 7 cm for equal distances, holds either way.",
    "8.4.q7: the book says only that the longest XY equals AC or BD; for 7 cm by 4 cm the diagonal is about "
    "8.1 cm, computed here.",
    "8.4.ex3: the book does not print the value of AC; it is 4 cm and 4 cm together, 8 cm, computed here.",
    "8.4.ex4: the book gives a hint only; the sides were found from the figure and are computed here.",
    "8.4.ex9: the book gives only a hint about where the compass tip goes; the radius of 8 cm is a chosen "
    "example.",
    "8.5.q1, 8.5.q2, 8.5.q3: the book prints no answers; they were checked by calculation (diagonal of a 6 cm "
    "by 4 cm rectangle about 7.2 cm, angles about 34° and 56°).",
    "8.5.q5, 8.5.q6: open discussion questions; the answers shown are correct summaries.",
    "8.5.ex2, 8.5.FiO.Q3, 8.5.FiO.Q4: the missing sides (about 4.9 cm, 6.9 cm and 6.3 cm) are computed checks "
    "that the book does not print.",
    "8.6.FiO.Q1: the book fixes only the border at 7 cm; the door of 2 cm by 3 cm is from the book's solution "
    "figure.",
    "8.6.FiO.Q3: the book's solution figure shows a rhombus without measurements; any angle other than 90° works.",
]
ERRATA = [
    "8.4.q3: the book's figure marks Y 2 cm from B in case 2, but the text says 1 cm from B.",
    "8.4.q5: the printed solution table lists Y distances of 5 cm, 1 cm and 4 cm, while the chapter has 5 mm, "
    "1 cm and 1 cm 5 mm.",
]

DESIGN_REFERENCES = [
    {"text": "maths6_ch7 new_design Phase 2 plan: framing intro with one hook, idea topics ending in one doer "
             "tool, a practice topic after each idea topic with one video per book question, one summary topic.",
     "url": ""},
]

FIGURES = {
    "T2.C1": ["Five artwork pictures made of circles: touching, sharing a centre, overlapping, a mouse face."],
    "T7.C1": ["A square PQRS of side 6 cm with perpendiculars at P and Q and equal marks on its sides."],
    "T10.C1": ["A rough diagram of rectangle ACDF made of two identical squares ABEF and BCDE with tick marks."],
    "T15.C2": ["Base DC of 5 cm, perpendicular line l at C, and a circle of radius 7 cm around D cutting l at B."],
    "T16.C2": ["The house figure: rectangle with a door, apex A from two arcs of 5 cm, and an arc from B to C."],
}
