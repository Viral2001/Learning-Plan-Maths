# -*- coding: utf-8 -*-
"""Chapter-level content for Class 7 Chapter 4, Expressions using Letter-Numbers (Ganita Prakash Grade 7 Part I,
Chapter 4). Book lines elsewhere are verbatim except: the book's dashes become commas, colons or "to"; minus is U+2212."""
from __future__ import annotations

CHAPTER = {
    "grade": 7,
    "label": "Class 7",
    "chapter_no": 4,
    "name": "Expressions using Letter-Numbers",
    "book_part": "Ganita Prakash Grade 7 Part I, Chapter 4",
    "source_pdf": "textbooks/class7/gegp104.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Letter-Numbers and Expressions",
     "A sweet shop order, ages and matchstick Ls lead to letter-numbers and algebraic expressions. Words become "
     "expressions, arithmetic expressions are revisited, and the multiplication sign is dropped."),
    ("M2", "Simplifying Expressions",
     "Like terms are added, brackets with a minus sign are opened, simplest forms are checked and mistakes mended, "
     "and number machines give formulas."),
    ("M3", "Expressions that Describe Patterns",
     "A saree border, a calendar and matchsticks show how an expression models a pattern, predicts far positions "
     "and proves a pattern for every case."),
    ("M4", "Review and Summary", "A closing summary of the chapter."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter follows the book's own order: a sweet shop with a different order every day opens the need "
             "for a short rule, letter-numbers give the rule, and simplifying then patterns put it to work. Every "
             "story is a video that ends on a question the student answers before the idea is named, and an "
             "interactive tool appears only where handling the expression is the idea itself.",
    "points": [
        {"title": "Try first, name later",
         "text": "The hook video leaves the laddu order question open. The word letter-number arrives only after the "
                 "student has seen that the way to work out the bill stays fixed while the numbers change."},
        {"title": "Concept, then practice, topic by topic",
         "text": "Each idea gets its own topic: story or concept videos, one per concept, a closing practice concept "
                 "(with a tool where handling the expression is the concept), then the book's Figure it Out "
                 "questions in their own topic, one question and one video per concept."},
        {"title": "Say it in words first",
         "text": "Every expression is first said in plain words, then written with letter-numbers, then tested by "
                 "replacing the letter-numbers by numbers."},
        {"title": "Simplify, then generalise",
         "text": "Like terms and brackets reduce an expression to its simplest form, and the same moves let an "
                 "expression prove that a calendar or matchstick pattern holds for every case."},
    ],
}

NCERT_ITEMS = [
    "opening", "4.1.ex1_s", "4.1.ex1_a", "4.1.ex2", "4.1.ex3_a", "4.1.ex3_b", "4.1.ex3_c", "4.1.ex4",
    "4.1.FiO_1", "4.1.FiO_2", "4.1.FiO_3", "4.1.FiO_4", "4.1.FiO_5", "4.1.FiO_6", "4.1.FiO_7", "4.2.value",
    "4.2.arith_a", "4.2.arith_b", "4.2.arith_c", "4.3.nth", "4.3.value_a", "4.3.value_b", "4.3.mtm1_a",
    "4.3.mtm1_b", "4.3.mtm1_c", "4.4.rect", "4.4.ex5_a", "4.4.ex5_b", "4.4.ex6_a", "4.4.ex6_b", "4.4.ex7",
    "4.4.ex7_talk", "4.4.ex8_a", "4.4.ex8_b", "4.4.ex8_c", "4.4.ex9", "4.4.ex10_u", "4.4.ex10_y", "4.4.ex11",
    "4.4.mtm2_a", "4.4.mtm2_b", "4.4.mtm2_c", "4.4.terms_letters", "4.4.FiO_1", "4.4.FiO_2", "4.5.detective",
    "4.5.machines_1", "4.5.machines_2", "4.5.make_own", "4.6.saree_pos", "4.6.saree_design", "4.6.cal_diag",
    "4.6.cal_verify", "4.6.cal_cross", "4.6.cal_talk", "4.6.match_far", "4.6.match_formula",
    "4.6.match_orient", "4.6.FiO_1", "4.6.FiO_2", "4.6.FiO_3", "4.6.FiO_4", "4.6.FiO_5", "4.6.FiO_6",
    "4.6.FiO_7", "4.6.FiO_8", "4.6.FiO_9", "4.6.FiO_10", "4.6.FiO_11", "4.6.FiO_12", "4.6.FiO_13",
    "4.6.FiO_14", "4.6.FiO_15", "summary",
]

MISCONCEPTIONS = [
    ("M_LETTER_FIXED", "A letter-number stands for one fixed number, or for a particular object, not for any number it can take."),
    ("M_JOIN_DIGITS", "A number and a letter-number written side by side are joined as digits or added, so 7k means 7 plus k or the number 7k."),
    ("M_ORDER_OPS", "An expression with several operations is worked from left to right, whatever the operations are."),
    ("M_BRACKET_SIGN", "A minus sign before a bracket changes only the first term inside it, or none of them."),
    ("M_SIGN_VALUE", "A letter-number can only take positive values, or the value of an expression with a negative number is found by dropping the sign."),
    ("M_UNLIKE_ADD", "Unlike terms can be added into one term, so 3a + 2b becomes 5 or 5ab."),
    ("M_DISTRIB_FIRST", "A number outside a bracket multiplies only the first term inside it."),
    ("M_ADD_NOT_MULT", "5u and 5 + u mean the same thing, since both put 5 and u together."),
    ("M_BRACKET_EARLY", "10y − 3 and 10(y − 3) are the same expression."),
    ("M_PATTERN_STEP", "The count at Step y is the amount added each step times y, with no regard for the start or the first step."),
    ("M_REMAINDER_DESIGN", "A remainder of 1 or 2 on dividing a position by 3 gives the design number in the order of the cycle in the wrong direction."),
]

SOLUTION_NOTES = []
ERRATA = []

DESIGN_REFERENCES = [
    {"text": "docs/25_new_design_learning_plan_playbook.md: framing intro, idea topics ending in "
             "a practice concept, a question topic after each idea topic, and one summary topic; the Class 7 "
             "Chapter 10 plan for one video per concept and one question per concept.", "url": ""},
]

FIGURES = {
    "T1.C1": ["A sweet shop counter with trays of coconut-jaggery laddus and boxes ready to be packed."],
    "T10.C1": ["A saree border with the six designs A, B, C, D, E, F repeating along it."],
    "T11.C1": ["The November 2024 calendar with a 2 by 2 square 12, 13, 19, 20 marked."],
    "T11.C2": ["A cross shape on the calendar: 8 above, 14, 15, 16 in the middle row, 22 below."],
    "T12.C1": ["Steps 1 to 4 of a triangle pattern built from matchsticks: 3, 5, 7, 9 matchsticks."],
}
