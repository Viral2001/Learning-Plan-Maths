# -*- coding: utf-8 -*-
"""Chapter-level content for Class 8 Chapter 4, Quadrilaterals (Ganita Prakash Grade 8 Part I, Chapter 4).
Book lines elsewhere are verbatim except: the book's dashes become commas, colons or "to"; minus is U+2212;
angle measures inside worked arithmetic are written without the degree sign so the arithmetic checker reads them."""
from __future__ import annotations

CHAPTER = {
    "grade": 8,
    "label": "Class 8",
    "chapter_no": 4,
    "name": "Quadrilaterals",
    "book_part": "Ganita Prakash Grade 8 Part I, Chapter 4",
    "source_pdf": "textbooks/class8/hegp104.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Four Sides, Four Angles",
     "What makes a figure a quadrilateral, and the carpenter who wants a frame that is exactly rectangular."),
    ("M2", "Rectangles and Squares",
     "A rectangle defined three ways: by its angles and sides, by its diagonals, and by its angles alone. Its "
     "diagonals are equal and bisect each other, its opposite sides are equal and parallel, and the square is the "
     "special rectangle whose diagonals also meet at right angles and bisect its angles."),
    ("M3", "Angles in a Quadrilateral",
     "A diagonal splits any quadrilateral into two triangles, so its four angles always add up to 360°."),
    ("M4", "Parallelograms and Rhombuses",
     "Quadrilaterals with parallel opposite sides: their angles, sides and diagonals, and the rhombus, whose "
     "equal sides make it a parallelogram with diagonals that meet at right angles."),
    ("M5", "Kites, Trapeziums and the Family",
     "Building quadrilaterals from diagonals and from pairs of triangles, the kite and the trapezium, and the "
     "family diagram that shows which quadrilaterals sit inside which."),
    ("M6", "Looking Back",
     "A summary of every quadrilateral and its properties, and the Which Quad? folding puzzle."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter starts from a carpenter's problem: how must two wooden strips be joined so that a thread "
             "through their ends makes a rectangle? Answering it needs deductions, and each later family "
             "(square, parallelogram, rhombus, kite, trapezium) is met the same way: define it, predict a "
             "property, prove it with congruent triangles or parallel lines, then check it by constructing and "
             "measuring.",
    "points": [
        {"title": "Predict, then prove",
         "text": "Every concept opens with a question the student answers first, such as whether the diagonals of "
                 "a parallelogram are equal, and then a short deduction settles it."},
        {"title": "Measuring makes a conjecture, reasoning makes it sure",
         "text": "Constructions and measurements suggest a property; only a deduction shows it holds for every "
                 "quadrilateral of that kind."},
        {"title": "One shape, several names",
         "text": "A square is a rectangle and a rhombus, and every rhombus is a parallelogram and a kite. Venn "
                 "diagrams make the family visible."},
        {"title": "Tools only where handling is the idea",
         "text": "Ten tools, each used once: crossing strips, dragging a quadrilateral, a square in a square, tearing "
                 "and placing the four angles, sides and angles, a hinged rhombus, diagonals, sliding kites and "
                 "trapeziums, and sorting figures into the family rings."},
    ],
}

NCERT_ITEMS = [
    "opening",
    # 4.1 Rectangles: definition and the Carpenter's Problem (pp 83 to 88)
    "4.1.rect_def", "4.1.carpenter", "4.1.ded1", "4.1.ded2", "4.1.mt_aod", "4.1.ded3_60", "4.1.ded3_x",
    "4.1.carpenters_world", "4.1.process",
    # Other definitions and properties of a rectangle (pp 89 to 90)
    "4.1.alt_def", "4.1.all90_question", "4.1.ded4", "4.1.wrong_bad", "4.1.props", "4.1.parallel",
    # A special rectangle: the square (pp 90 to 93)
    "4.1.special_rect", "4.1.square_def", "4.1.venn_square", "4.1.carpenter_square", "4.1.ded5",
    "4.1.square_construct", "4.1.square_props", "4.1.angles45",
    # Figure it Out, rectangles and squares (questions 1 to 5)
    "FiO1.q1", "FiO1.q2", "FiO1.q3", "FiO1.q4", "FiO1.q5",
    # 4.2 Angles in a quadrilateral (pp 94 to 95)
    "4.2.three_right", "4.2.angle_sum",
    # 4.3 Parallelograms (pp 95 to 99)
    "4.3.construct_parallel", "4.3.venn_pgram", "4.3.construct_4_5_30", "4.3.ded6", "4.3.ded7", "4.3.wrong_abd",
    "4.3.props", "4.3.diag_equal", "4.3.ded8", "4.3.wrong_aoe", "4.3.diag_angle",
    # 4.4 Rhombus (pp 99 to 102)
    "4.4.construct_rhombus", "4.4.ded9", "4.4.rhombus_pgram", "4.4.venn", "4.4.props", "4.4.ded10",
    # Figure it Out, parallelograms and rhombuses (questions 1 to 3)
    "FiO2.q1", "FiO2.q2", "FiO2.q3",
    # 4.5 Playing with quadrilaterals (pp 103 to 105)
    "4.5.geoboard", "4.5.join_equilateral", "4.5.join_isosceles", "4.5.join_scalene",
    # 4.6 Kite and trapezium (pp 105 to 107)
    "4.6.kite_def", "4.6.kite_prop", "4.6.trap_def", "4.6.trap_prop1", "4.6.iso_trap", "4.6.iso_prop2",
    # Figure it Out, kites and trapeziums (questions 1 to 11)
    "FiO3.q1", "FiO3.q2", "FiO3.q3", "FiO3.q4", "FiO3.q5", "FiO3.q6", "FiO3.q7", "FiO3.q8", "FiO3.q9",
    "FiO3.q10", "FiO3.q11",
    # Summary and Puzzle Time (pp 109 to 111)
    "summary", "puzzle",
]

MISCONCEPTIONS = [
    ("M_SQUARE_NOT_RECT", "A square is not a rectangle, because a rectangle must have two long sides and two short sides."),
    ("M_ONE_NAME", "A quadrilateral can belong to only one family, so a figure is either a rhombus or a parallelogram."),
    ("M_DIAG_EQUAL_ALL", "The diagonals of every parallelogram (and every rhombus) are equal."),
    ("M_DIAG_PERP_RHOMBUS", "Any quadrilateral whose diagonals are perpendicular must be a rhombus."),
    ("M_ANGLE_SUM_180", "The angles of a quadrilateral add up to 180°, the same as a triangle."),
    ("M_MEASURE_PROVES", "Measuring a few figures proves that a property is always true."),
    ("M_CONGRUENCE_ORDER", "In a congruence statement the order of the letters does not matter."),
    ("M_ADJ_EQUAL", "In a parallelogram the next-door angles are equal and the opposite angles add up to 180°."),
    ("M_RIGHT_ANGLES_ONLY", "A rectangle needs both its angles and its sides stated; four right angles alone are not enough."),
    ("M_TRAP_EXACTLY_ONE", "A trapezium must have exactly one pair of parallel sides, so a parallelogram is not a trapezium."),
    ("M_KITE_RHOMBUS", "Every kite is a rhombus."),
]

SOLUTION_NOTES = [
    "Figure it Out (kites and trapeziums) question 4(ii): the answer key printed with the book says "
    "No, but a square has AB = BC and CD = DA, so it is a kite, and all its angles are 90°, so it is a rectangle. "
    "The plan answers: yes, a square (and only a square) is both a kite and a rectangle.",
    "Joining Triangles 3: two copies of a 6 cm, 9 cm, 12 cm triangle can be joined along any of the three sides in "
    "two ways: one copy turned half round gives a parallelogram, one copy flipped over gives a kite. Flipped over the "
    "12 cm side it is the usual kite with sides 6, 6, 9 and 9; flipped over the 6 cm or 9 cm side the kite caves in "
    "(one angle is about 209°), because the angle between the 6 cm and 9 cm sides is obtuse (about 104°).",
    "Figure it Out (kites and trapeziums) question 5: in rectangle PAIR, ∠ORI = 30° and ∠RIO = 90°, so "
    "∠ROI = 60°; ∠ROD = 90° because RODS is a rectangle, so ∠IOD = 90° − 60° = 30°.",
]
ERRATA = [
    "Answer key, Figure it Out (kites and trapeziums) question 4(ii) prints No; the square is both a "
    "kite and a rectangle, so the plan's answer is yes, the square.",
]

DESIGN_REFERENCES = [
    {"text": "docs/25_new_design_learning_plan_playbook.md: framing intro, idea topics each ending in a doer, a "
             "question topic after each idea topic, and one summary topic.", "url": ""},
]

FIGURES = {}
