# -*- coding: utf-8 -*-
"""Chapter-level content for Class 6 Chapter 9, Symmetry (Ganita Prakash Grade 6, Chapter 9).
Book lines elsewhere are verbatim except: the book's dashes become commas, colons or "to"; minus is U+2212."""
from __future__ import annotations

CHAPTER = {
    "grade": 6,
    "label": "Class 6",
    "chapter_no": 9,
    "name": "Symmetry",
    "book_part": "Ganita Prakash Grade 6, Chapter 9",
    "source_pdf": "textbooks/class6/fegp109.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Line Symmetry",
     "A line of symmetry cuts a figure into mirror halves that overlap when folded. Figures can have one line, "
     "many lines or none, and folding, punching and cutting paper make symmetric shapes."),
    ("M2", "Rotational Symmetry",
     "A figure that looks the same after a turn about a fixed centre has rotational symmetry. Counting the turns "
     "gives its angles of symmetry, and the circle has a turn for every angle."),
    ("M3", "Both Together, Tiles and a Game",
     "Lines and turns can appear together or alone. Colour tiles and a grid game put both ideas to work, and the "
     "summary closes the chapter."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter follows the book's order. Folding paper finds lines of symmetry, turning cut-outs finds "
             "angles of symmetry, and each idea is tested on rangoli, kolam, wheels and tiles from everyday life.",
    "points": [
        {"title": "Fold it, turn it, then say it",
         "text": "Every new idea starts from a paper fold or a paper turn, so a line of symmetry and an angle of "
                 "symmetry are first seen, then named."},
        {"title": "Concept, then practice, topic by topic",
         "text": "Each idea gets its own topic: worked videos for the book's questions, a tool only where "
                 "handling the figure is the idea, then the book's Figure it Out questions in a practice topic, "
                 "each with its own video."},
        {"title": "Lines and turns are different",
         "text": "A figure may have lines, turns, both or neither, and the plan keeps the two ideas apart until "
                 "the chapter brings them together."},
        {"title": "Keeko's doubts",
         "text": "The common wrong ideas, such as 'the diagonal of a rectangle is a line of symmetry', are raised by "
                 "Keeko and fixed with a fold or a cut-out, never just a rule."},
    ],
}

# Every book item, in book order. Ids come from the page-image inventory (page = rendered image index).
NCERT_ITEMS = [
    "opening", "9.1.q1", "9.1.q2", "9.1.q3", "9.1.q4", "9.1.FiO1.Q1", "9.1.FiO1.Q2", "9.1.q5", "9.1.q6",
    "9.1.q7", "9.1.q8", "9.1.q9", "9.1.q10", "9.1.q11", "9.1.q12", "9.1.q13", "9.1.FiO2.Q1", "9.1.FiO2.Q2",
    "9.1.FiO2.Q3", "9.1.FiO2.Q4", "9.1.FiO2.Q5", "9.1.FiO2.Q6", "9.1.FiO2.Q7", "9.1.FiO2.Q8", "9.1.FiO2.Q9",
    "9.1.FiO2.Q10", "9.1.FiO2.Q11", "9.1.FiO2.Q12", "9.1.FiO2.Q13", "9.2.q1", "9.2.q2", "9.2.q3", "9.2.q4",
    "9.2.q5", "9.2.ex1", "9.2.q6", "9.2.q7", "9.2.q8", "9.2.q9", "9.2.q10", "9.2.q11", "9.2.q12", "9.2.q13",
    "9.2.q14", "9.2.q15", "9.2.q16", "9.2.q17", "9.2.FiO1.Q1", "9.2.FiO1.Q2", "9.2.FiO1.Q3", "9.2.q18",
    "9.2.q19", "9.2.q20", "9.2.q21", "9.2.q22", "9.2.FiO2.Q1", "9.2.FiO2.Q2", "9.2.FiO2.Q3", "9.2.FiO2.Q4",
    "9.2.FiO2.Q5", "9.2.FiO2.Q6", "9.2.FiO2.Q7", "9.2.FiO2.Q8", "9.2.FiO2.Q9", "9.2.FiO2.Q10", "9.2.FiO2.Q11",
    "9.2.q23", "9.2.q24", "9.2.q25", "9.3.q1", "summary",
]

# Frozen home of every book item: (topic key, concept key, "WE" worked example in a teaching concept, or
# "FIO" Figure it Out item in the topic's DOER, which core.qt then moves into the practice topic).
ITEM_HOME = {
    "opening": ("T1", "T1.C1", "HOOK"), "9.1.q1": ("T6", "T6.C1", "WE"), "9.1.q2": ("T8", "T8.C1", "WE"),
    "9.1.q3": ("T2", "T2.C2", "WE"), "9.1.q4": ("T2", "T2.C1", "WE"), "9.1.FiO1.Q1": ("T2", "T2.C3", "FIO"),
    "9.1.FiO1.Q2": ("T2", "T2.C3", "FIO"), "9.1.q5": ("T3", "T3.C1", "WE"), "9.1.q6": ("T3", "T3.C1", "WE"),
    "9.1.q7": ("T3", "T3.C2", "WE"), "9.1.q8": ("T3", "T3.C3", "WE"), "9.1.q9": ("T4", "T4.C1", "WE"),
    "9.1.q10": ("T4", "T4.C2", "WE"), "9.1.q11": ("T5", "T5.C1", "WE"), "9.1.q12": ("T5", "T5.C2", "WE"),
    "9.1.q13": ("T5", "T5.C3", "WE"), "9.1.FiO2.Q1": ("T5", "T5.C4", "FIO"),
    "9.1.FiO2.Q2": ("T5", "T5.C4", "FIO"), "9.1.FiO2.Q3": ("T5", "T5.C4", "FIO"),
    "9.1.FiO2.Q4": ("T5", "T5.C4", "FIO"), "9.1.FiO2.Q5": ("T5", "T5.C4", "FIO"),
    "9.1.FiO2.Q6": ("T3", "T3.C4", "FIO"), "9.1.FiO2.Q7": ("T3", "T3.C4", "FIO"),
    "9.1.FiO2.Q8": ("T3", "T3.C4", "FIO"), "9.1.FiO2.Q9": ("T3", "T3.C4", "FIO"),
    "9.1.FiO2.Q10": ("T3", "T3.C4", "FIO"), "9.1.FiO2.Q11": ("T4", "T4.C3", "FIO"),
    "9.1.FiO2.Q12": ("T4", "T4.C3", "FIO"), "9.1.FiO2.Q13": ("T4", "T4.C3", "FIO"),
    "9.2.q1": ("T6", "T6.C1", "WE"), "9.2.q2": ("T6", "T6.C1", "WE"), "9.2.q3": ("T6", "T6.C2", "WE"),
    "9.2.q4": ("T6", "T6.C2", "WE"), "9.2.q5": ("T6", "T6.C2", "WE"), "9.2.ex1": ("T6", "T6.C3", "WE"),
    "9.2.q6": ("T6", "T6.C3", "WE"), "9.2.q7": ("T7", "T7.C1", "WE"), "9.2.q8": ("T7", "T7.C1", "WE"),
    "9.2.q9": ("T7", "T7.C1", "WE"), "9.2.q10": ("T7", "T7.C2", "WE"), "9.2.q11": ("T7", "T7.C2", "WE"),
    "9.2.q12": ("T7", "T7.C2", "WE"), "9.2.q13": ("T7", "T7.C3", "WE"), "9.2.q14": ("T7", "T7.C3", "WE"),
    "9.2.q15": ("T7", "T7.C3", "WE"), "9.2.q16": ("T8", "T8.C1", "WE"), "9.2.q17": ("T8", "T8.C1", "WE"),
    "9.2.FiO1.Q1": ("T6", "T6.C4", "FIO"), "9.2.FiO1.Q2": ("T6", "T6.C4", "FIO"),
    "9.2.FiO1.Q3": ("T7", "T7.C4", "FIO"), "9.2.q18": ("T8", "T8.C2", "WE"), "9.2.q19": ("T8", "T8.C2", "WE"),
    "9.2.q20": ("T9", "T9.C1", "WE"), "9.2.q21": ("T9", "T9.C2", "WE"), "9.2.q22": ("T9", "T9.C3", "WE"),
    "9.2.FiO2.Q1": ("T8", "T8.C3", "FIO"), "9.2.FiO2.Q2": ("T10", "T10.C3", "FIO"),
    "9.2.FiO2.Q3": ("T10", "T10.C3", "FIO"), "9.2.FiO2.Q4": ("T8", "T8.C3", "FIO"),
    "9.2.FiO2.Q5": ("T8", "T8.C3", "FIO"), "9.2.FiO2.Q6": ("T8", "T8.C3", "FIO"),
    "9.2.FiO2.Q7": ("T10", "T10.C3", "FIO"), "9.2.FiO2.Q8": ("T10", "T10.C3", "FIO"),
    "9.2.FiO2.Q9": ("T10", "T10.C3", "FIO"), "9.2.FiO2.Q10": ("T10", "T10.C3", "FIO"),
    "9.2.FiO2.Q11": ("T9", "T9.C4", "FIO"), "9.2.q23": ("T11", "T11.C1", "WE"),
    "9.2.q24": ("T11", "T11.C3", "FIO"), "9.2.q25": ("T11", "T11.C3", "FIO"),
    "9.3.q1": ("T11", "T11.C2", "WE"), "summary": ("T12", "T12.C1", "RECAP"),
}
assert set(ITEM_HOME) == set(NCERT_ITEMS), set(ITEM_HOME) ^ set(NCERT_ITEMS)

MISCONCEPTIONS = [
    ("M_BALANCED", "A shape has symmetry as long as it looks balanced or pretty, so no fold test is needed."),
    ("M_HALVES_ANY", "Any line that cuts a figure into two equal-looking halves is a line of symmetry, even when "
                     "the halves do not overlap when folded."),
    ("M_DIAGONAL_RECT", "The diagonal of a rectangle is a line of symmetry, because it cuts the rectangle into "
                        "two equal triangles."),
    ("M_ONE_LINE", "A figure can have only one line of symmetry, and the line is always vertical."),
    ("M_EVERY_LINE", "Every shape has a line of symmetry."),
    ("M_REFLECT_STAYS", "When a figure is reflected in a line, every point moves to the other side."),
    ("M_CUT_SAME", "A cut on a folded sheet makes a hole of the same shape and number as the cut, with no mirror "
                   "copies."),
    ("M_NO_LINE_NO_SYM", "A figure with no line of symmetry has no symmetry at all."),
    ("M_ORDER_DISTINCT", "The order of rotational symmetry counts only the turns that look different from the "
                         "start, so the full turn of 360° is not counted."),
    ("M_ORDER_LINES", "The order of rotational symmetry always equals the number of lines of symmetry."),
    ("M_ARMS_ENOUGH", "Three radial arms always give three angles of symmetry, whatever the angles between them."),
    ("M_ANY_SMALLEST", "Any whole number of degrees can be the smallest angle of symmetry of a figure."),
    ("M_CIRCLE_SMALLEST", "A circle has a smallest angle of symmetry, just like other figures."),
]

SOLUTION_NOTES = [
    "9.1.q1, 9.1.q2, 9.1.q3, 9.1.q11, 9.1.q13, 9.2.q8, 9.2.q9, 9.2.q22, 9.2.q23, 9.2.q24, 9.2.q25: the book gives "
    "no printed answer (open ended, hands-on or drawing); the answers worked here follow the expected observation.",
    "9.1.FiO1.Q2: the official solution draws lines on only three of the five figures; the other two are left "
    "without lines, which is read as no line of symmetry.",
    "9.1.q7: the book solutions do not answer it; the counts (6, 0 and 4 lines) are read from the picture and "
    "should be checked against the printed figures.",
    "9.1.FiO2.Q3: only sets up the notation for vertical and horizontal folds used in Q4; it has no question or "
    "answer of its own.",
    "9.1.FiO2.Q8: the book prints no number; the 6 lines of the kolam are read from the solution picture, which "
    "shows dashed lines through the centre at equal angles. To be checked.",
    "9.2.FiO2.Q1: the official solution says only that 12 angles of symmetry are possible, and its pictures for "
    "parts (i) and (ii) do not give 3 and 4 angles. The answer here is computed from the divisors of 12.",
    "9.2.FiO2.Q9: the solutions skip it; the answer is computed and equals Q8 (3, 4, 5 and so on).",
    "9.3.q1: no strategy is printed; the half-turn reply is computed.",
]
ERRATA = [
    "9.1.FiO2.Q5: the book says 'a square' for both parts; part (b) shows the tilted square.",
]

DESIGN_REFERENCES = [
    {"text": "maths6_ch7 new_design Phase 2 plan: framing intro with one hook, idea topics ending in one doer, "
             "optional tool where the manipulation is the idea, a practice topic after each idea topic with one "
             "video per book question, one summary topic.",
     "url": ""},
]

FIGURES = {
    "T1.C1": ["A flower, a butterfly, a rangoli, a pinwheel and a cloud in a row, with the Taj Mahal and a gopuram."],
    "T2.C1": ["A blue triangle with a dotted line down its middle, and four puzzle pieces with a dotted line "
              "that does not give mirror halves."],
    "T3.C1": ["A square sheet folded four ways: vertical, horizontal and the two diagonals."],
    "T3.C3": ["A rectangle with its diagonal drawn, and the two triangles that do not overlap when folded."],
    "T4.C1": ["A square with corners A, B, C, D and a vertical dashed line of symmetry."],
    "T5.C2": ["A folded paper with a dotted cut line, then the opened paper with the mirrored cut."],
    "T6.C1": ["A four-bladed paper windmill with a red dot at its centre, shown turned by 90°."],
    "T7.C3": ["A three-armed figure with 120° marked between adjacent dotted lines."],
    "T9.C1": ["A circle turned about its centre, and the same circle with a diameter drawn."],
}
