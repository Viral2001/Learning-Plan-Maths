# -*- coding: utf-8 -*-
"""Chapter-level content for Class 6 Chapter 1, Patterns in Mathematics (Ganita Prakash Grade 6, Chapter 1).
Book lines elsewhere are verbatim except: the book's dashes become commas; "3x4x4" is written "3 × 4 × 4"."""
from __future__ import annotations

CHAPTER = {
    "grade": 6,
    "label": "Class 6",
    "chapter_no": 1,
    "name": "Patterns in Mathematics",
    "book_part": "Ganita Prakash Grade 6, Chapter 1",
    "source_pdf": "textbooks/class6/fegp101.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Patterns and Number Sequences",
     "Mathematics is the search for patterns and for the reasons behind them. The most basic patterns are number "
     "sequences: lists of whole numbers that follow a rule."),
    ("M2", "Pictures and Relations Among Sequences",
     "Dot pictures show why triangular, square and cube numbers have their names, and the same pictures explain "
     "surprising relations, such as odd numbers adding up to squares."),
    ("M3", "Patterns in Shapes",
     "Shape sequences, such as regular polygons, complete graphs, stacked squares and the Koch snowflake, hide "
     "number sequences in their counts. The summary closes the chapter."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter follows the book's order. A pattern is first noticed in a list of numbers, then drawn "
             "with dots, then explained by the picture, and finally found again in sequences of shapes.",
    "points": [
        {"title": "Notice, draw, explain",
         "text": "Every new sequence is first written out, then drawn with dots, and only then explained, because "
                 "the book asks not just what the pattern is but why it happens."},
        {"title": "Concept, then practice, topic by topic",
         "text": "Each idea gets its own topic: worked videos for the book's examples, a tool only where drawing "
                 "or testing the sequence is the idea, then the book's Figure it Out questions in a practice "
                 "topic, each with its own video."},
        {"title": "A picture is a reason",
         "text": "Adding odd numbers gives squares because an L-shape of dots wraps around a square grid. The "
                 "picture works for a square of any size, so the pattern never stops."},
        {"title": "Keeko's doubts",
         "text": "The common wrong ideas, such as 'adding odd numbers must give an odd number', are raised by "
                 "Keeko and fixed with a picture or a check of the first few terms, never just a rule."},
    ],
}

# Every book item, in book order. Ids come from the page-image inventory.
NCERT_ITEMS = [
    "opening",
    "1.1.FiO.Q1", "1.1.FiO.Q2",
    "1.2.FiO.Q1", "1.2.FiO.Q2",
    "1.3.FiO.Q1", "1.3.FiO.Q2", "1.3.FiO.Q3", "1.3.FiO.Q4", "1.3.FiO.Q5",
    "1.4.ex1", "1.4.q1", "1.4.q2", "1.4.q3", "1.4.q4", "1.4.q5",
    "1.4.FiO.Q1", "1.4.FiO.Q2", "1.4.FiO.Q3", "1.4.FiO.Q4", "1.4.FiO.Q5", "1.4.FiO.Q6", "1.4.FiO.Q7",
    "1.4.FiO.Q8", "1.4.FiO.Q9",
    "1.5.FiO.Q1", "1.5.FiO.Q2",
    "1.6.ex1", "1.6.FiO.Q1", "1.6.FiO.Q2", "1.6.FiO.Q3", "1.6.FiO.Q4", "1.6.FiO.Q5",
    "summary",
]

# Frozen home of every book item: (topic key, concept key, "WE" worked example in a teaching concept, or
# "FIO" Figure it Out item in the topic's DOER, which core.qt then moves into the practice topic).
ITEM_HOME = {
    "opening": ("T1", "T1.C1", "HOOK"),
    "1.1.FiO.Q1": ("T2", "T2.C3", "FIO"), "1.1.FiO.Q2": ("T2", "T2.C3", "FIO"),
    "1.2.FiO.Q1": ("T3", "T3.C4", "FIO"), "1.2.FiO.Q2": ("T3", "T3.C4", "FIO"),
    "1.3.FiO.Q1": ("T4", "T4.C3", "FIO"), "1.3.FiO.Q2": ("T4", "T4.C3", "FIO"),
    "1.3.FiO.Q3": ("T5", "T5.C4", "FIO"), "1.3.FiO.Q4": ("T5", "T5.C4", "FIO"),
    "1.3.FiO.Q5": ("T5", "T5.C4", "FIO"),
    "1.4.ex1": ("T6", "T6.C1", "WE"), "1.4.q2": ("T6", "T6.C2", "WE"), "1.4.q1": ("T6", "T6.C2", "WE"),
    "1.4.q3": ("T6", "T6.C2", "WE"), "1.4.q4": ("T6", "T6.C2", "WE"),
    "1.4.q5": ("T7", "T7.C1", "WE"),
    "1.4.FiO.Q1": ("T7", "T7.C3", "FIO"), "1.4.FiO.Q2": ("T7", "T7.C3", "FIO"),
    "1.4.FiO.Q3": ("T8", "T8.C3", "FIO"), "1.4.FiO.Q4": ("T8", "T8.C3", "FIO"), "1.4.FiO.Q5": ("T8", "T8.C3", "FIO"),
    "1.4.FiO.Q6": ("T8", "T8.C3", "FIO"), "1.4.FiO.Q7": ("T8", "T8.C3", "FIO"), "1.4.FiO.Q8": ("T8", "T8.C3", "FIO"),
    "1.4.FiO.Q9": ("T8", "T8.C3", "FIO"),
    "1.5.FiO.Q1": ("T9", "T9.C3", "FIO"), "1.5.FiO.Q2": ("T9", "T9.C3", "FIO"),
    "1.6.ex1": ("T10", "T10.C1", "WE"),
    "1.6.FiO.Q1": ("T10", "T10.C3", "FIO"), "1.6.FiO.Q2": ("T10", "T10.C3", "FIO"),
    "1.6.FiO.Q3": ("T10", "T10.C3", "FIO"), "1.6.FiO.Q4": ("T10", "T10.C3", "FIO"),
    "1.6.FiO.Q5": ("T10", "T10.C3", "FIO"),
    "summary": ("T11", "T11.C1", "RECAP"),
}
assert set(ITEM_HOME) == set(NCERT_ITEMS), set(ITEM_HOME) ^ set(NCERT_ITEMS)

MISCONCEPTIONS = [
    ("M_MATHS_SUMS", "Mathematics is only sums and answers, not a search for patterns and the reasons for them."),
    ("M_ADD_SAME_ONLY", "A number pattern must add the same number every time, so 1, 3, 6, 10, 15 has no pattern."),
    ("M_ALL_ONES_NO_PATTERN", "A list of all 1's is not a pattern, because nothing changes."),
    ("M_RULE_FROM_TWO", "Two terms are enough to know the rule, so 1, 2, ... must go 3, 4, 5."),
    ("M_SQUARE_IS_DOUBLE", "A square number is the number doubled, so the fifth square would be 10."),
    ("M_POWERS_ADD", "Powers of 2 go up by adding 2 each time, so after 8 comes 10."),
    ("M_VIRAHANKA_COUNT", "Virahanka numbers grow by the next counting number: after 1, 2, 3, 5 comes 8 because "
                          "the jump grows by 1 each time."),
    ("M_NAMES_ARBITRARY", "Triangular, square and cube are only names; they have no link to a picture."),
    ("M_ONE_PICTURE", "A number can be drawn in only one way, so one number cannot be both triangular and square."),
    ("M_HEX_SAME_JUMP", "Hexagonal numbers go up by the same amount each time."),
    ("M_PICTURE_ONE_SIZE", "A dot picture explains only the size that is drawn, not every size."),
    ("M_ODD_SUM_ODD", "Adding odd numbers must give an odd number, so the sum 1 + 3 + 5 + 7 cannot be a square."),
    ("M_CHECK_FEW", "A pattern that works for the first few cases is proved for all cases."),
    ("M_UP_DOWN_DOUBLE", "Adding up and down is just double the adding up."),
    ("M_RUNNING_SAME", "Adding up a sequence step by step gives back the same sequence."),
    ("M_PAIRS_SAME", "Adding two neighbouring terms of a sequence gives the same sequence again."),
    ("M_COMPLETE_SAME_ADD", "Each new point of a complete graph adds the same number of lines."),
    ("M_SIDES_CORNERS", "A shape can have more corners than sides."),
    ("M_KOCH_ADDS", "Each Koch step adds 3 more segments instead of making 4 times as many."),
    ("M_STACK_ROWS_SAME", "Stacked triangles add the same number of little triangles at each step."),
    ("M_SHAPES_NO_NUMBERS", "Shape sequences and number sequences are different things with nothing in common."),
    ("M_SHAPE_ALWAYS_DRAWABLE", "Every next shape in a shape sequence can always be drawn exactly."),
]

SOLUTION_NOTES = [
    "1.1.FiO.Q1, 1.1.FiO.Q2: open discussion; the book's examples are given as sample answers.",
    "1.2.FiO.Q1: the official solution gives the rules only for Virahanka numbers, powers of 2 and powers of 3; "
    "the rules for the other sequences in Table 1 are read from Table 1 and worked here.",
    "1.2.FiO.Q2: the next three terms are not printed in the solutions; they are computed here and checked: "
    "1, 1, 1; 8, 9, 10; 15, 17, 19; 16, 18, 20; 36, 45, 55; 64, 81, 100; 343, 512, 729; 34, 55, 89; "
    "128, 256, 512; 2187, 6561, 19683.",
    "1.3.FiO.Q1: the solutions say only to refer to Table 2; the sixth picture of each sequence is computed here "
    "(1, 6, 11, 12, 21, 36 and 216 dots or blocks). Table 2 does not picture Virahanka numbers or powers.",
    "1.3.FiO.Q2: the solutions say only to refer to Table 2; the reasons are read off the pictures.",
    "1.3.FiO.Q3: 36 as a triangle of 8 rows (1 + 2 + ... + 8) and as a 6 by 6 square is computed here.",
    "1.4.FiO.Q3: the printed solution shows only bracketed sums of 1's and does not name the two sequences; adding "
    "the All 1's sequence up gives the counting numbers, and adding it up and down gives the odd numbers (1, 1 + 1 "
    "+ 1, 1 + 1 + 1 + 1 + 1, ...). The plan uses these mathematically correct answers.",
    "1.4.FiO.Q5, 1.4.FiO.Q6, 1.4.FiO.Q7: the solutions refer to the book's pictures; the written reasons are "
    "worked here.",
    "1.4.FiO.Q9: open ended; no solution is printed.",
    "1.5.FiO.Q1: the printed solution bullets are in a garbled order; they are matched here to the five sequences "
    "of Table 3 in order (3 to 10 sides; 1, 3, 6, 10, 15 lines; 1, 4, 9, 16, 25 squares; 1, 4, 9, 16, 25 "
    "triangles; 3, 3 × 4, 3 × 4 × 4, ... segments).",
    "1.5.FiO.Q2: open ended; the sample answers are computed here.",
    "1.6.FiO.Q2: the solutions do not give the reason; the plan gives it (each new point joins all the earlier "
    "points, adding 1, 2, 3, 4, 5 lines).",
    "1.6.FiO.Q4: the printed solution writes the totals as up-and-down sums; the plan gives the equivalent reading "
    "from the hint, rows of 1, 3, 5, 7, 9 triangles.",
]
ERRATA = [
    "1.4.FiO.Q3: the printed solution brackets do not name the sequences; the plan answers 'counting numbers' for "
    "adding up and 'odd numbers' for adding up and down.",
]

DESIGN_REFERENCES = [
    {"text": "maths6_ch9 and maths6_ch7 new_design Phase 2 plans: framing intro with one hook, idea topics ending "
             "in one doer concept (a tool where handling the idea is the idea), a practice topic after each "
             "idea topic with one video per book question, one summary topic.",
     "url": ""},
]

FIGURES = {
    "T1.C1": ["Five orange matchstick figures growing step by step: one stick, then a small ladder, then larger "
              "nested squares made of matchsticks."],
    "T3.C1": ["Table 1 as ten rows of number sequences with their names."],
    "T4.C1": ["Dot pictures of the counting, odd and even sequences, five pictures each."],
    "T4.C2": ["Dot triangles of 1, 3, 6, 10, 15, square grids of 1, 4, 9, 16, 25 and cubes of 1, 8, 27, 64, 125."],
    "T6.C2": ["A 6 by 6 square grid of dots cut into nested L-shapes of 1, 3, 5, 7, 9 and 11 dots."],
    "T7.C1": ["A diamond of dots with rows of 1, 2, 3, 2, 1, the diagonal view of a 3 by 3 grid."],
    "T9.C1": ["Table 3: regular polygons, complete graphs K2 to K6, stacked squares, stacked triangles and the "
              "Koch snowflake in five steps."],
}
