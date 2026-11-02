# -*- coding: utf-8 -*-
"""Chapter-level content for Class 7 Chapter 2, Arithmetic Expressions (Ganita Prakash Grade 7 Part I, Chapter 2).
Book lines elsewhere are verbatim except: the book's dashes become commas, colons or "to"; minus is U+2212."""
from __future__ import annotations

CHAPTER = {
    "grade": 7,
    "label": "Class 7",
    "chapter_no": 2,
    "name": "Arithmetic Expressions",
    "book_part": "Ganita Prakash Grade 7 Part I, Chapter 2",
    "source_pdf": "textbooks/class7/gegp102.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Same Value, Different Looks: Simple Expressions",
     "A daily spend opens the idea of an expression and its value. Different expressions can share a value, and "
     "two expressions can be compared by reasoning about how they differ instead of working both out."),
    ("M2", "Reading Complex Expressions: Terms, Order and Swapping",
     "Brackets and terms tell us which part to work out first. Terms can be swapped and grouped in any way without "
     "changing the value, and everyday stories turn into expressions made of terms."),
    ("M3", "Removing Brackets",
     "A bracket after a plus sign can be dropped, a bracket after a minus sign flips the signs inside, and a number "
     "outside a bracket multiplies every term inside. The same ideas make some products quick to find."),
    ("M4", "Using Expressions, Puzzle and Summary",
     "Word problems are written as expressions, matched with others of equal value and compared by reasoning. A "
     "closing puzzle builds numbers from a few digits, and a summary gathers the whole chapter."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter follows the book's own order: a daily spend opens the idea of an expression and its value, "
             "comparing expressions by reasoning comes next, then terms and brackets that fix the order of work, "
             "swapping and grouping, and finally removing brackets. Every story is a video that ends on a question "
             "the student answers before the idea is named, and an interactive tool appears only where handling the "
             "numbers is the idea itself.",
    "points": [
        {"title": "Try first, name later",
         "text": "The hook video leaves a question about the same spend written two ways open. The words value and "
                 "expression arrive only after the student has worked a few out and felt that different looks can "
                 "share one value."},
        {"title": "Concept, then practice, topic by topic",
         "text": "Each idea gets its own topic: concept videos, one per concept, a closing practice concept (with a "
                 "tool only on the topics where the manipulation is the concept), then the book's Figure it Out "
                 "questions in their own topic, one question and one video per concept."},
        {"title": "Reason, do not just calculate",
         "text": "Two expressions are compared by asking how their numbers differ, not by working both out. "
                 "Brackets are removed by asking what the bracket means, not by memorising a rule about signs."},
        {"title": "Terms are the unit",
         "text": "An expression is read as a sum of terms. Swapping and grouping terms, removing brackets and "
                 "multiplying a bracket all come from keeping the terms and their signs together."},
    ],
}

NCERT_ITEMS = [
    "opening",
    # 2.1 Simple expressions
    "2.1.ex1", "2.1.same_value", "2.1.favourite", "2.1.compare",
    "2.1.FiO1", "2.1.FiO2",
    "2.1.ex2", "2.1.ex3", "2.1.compare5",
    # 2.2 Reading and evaluating complex expressions
    "2.2.language", "2.2.ex4", "2.2.brackets", "2.2.ex5",
    "2.2.terms", "2.2.subtract_add", "2.2.try_terms",
    "2.2.swap", "2.2.ex6", "2.2.swap_neg", "2.2.three_terms", "2.2.any_terms", "2.2.manasa", "2.2.properties",
    "2.2.swap_life",
    "2.2.ex7", "2.2.ex8", "2.2.ex9", "2.2.ex10", "2.2.ex11",
    "2.2.FiO1", "2.2.FiO2", "2.2.FiO3",
    # 2.3 Removing brackets I
    "2.3.minus_bracket", "2.3.ex12", "2.3.ex13", "2.3.ex14", "2.3.reason", "2.3.tinker1",
    "2.3.FiO1", "2.3.FiO2", "2.3.FiO3", "2.3.FiO4", "2.3.FiO5", "2.3.FiO6", "2.3.FiO7", "2.3.FiO8", "2.3.FiO9",
    # 2.4 Removing brackets II
    "2.4.ex15", "2.4.sangmu", "2.4.ex16", "2.4.general", "2.4.tinker2", "2.4.ex17", "2.4.ex18", "2.4.use_method",
    "2.4.FiO1", "2.4.FiO2", "2.4.FiO3", "2.4.FiO4",
    # end of chapter
    "2.5.FiO1", "2.5.FiO2", "2.5.FiO3", "2.5.FiO4", "2.5.FiO5", "2.5.FiO6",
    "puzzle.engineer", "summary",
]

MISCONCEPTIONS = [
    ("M_LEFT_TO_RIGHT", "An expression is always worked out strictly from left to right, so 30 + 5 × 4 is 35 × 4."),
    ("M_BRACKET_IGNORED", "Brackets can be dropped anywhere without changing the value of the expression."),
    ("M_MINUS_BRACKET", "Removing a bracket after a minus sign leaves the signs inside unchanged."),
    ("M_TERM_SIGN", "A minus sign belongs to the operation only, so it does not travel with the number when terms move."),
    ("M_SWAP_ANYTHING", "Any two numbers in an expression can be swapped, including across a minus sign, without "
                        "changing the value."),
    ("M_EVALUATE_TO_COMPARE", "The only way to compare two expressions is to work both of them out in full."),
    ("M_MULT_ONE_TERM", "A number outside a bracket multiplies only the first term inside it."),
    ("M_EQUALS_ANSWER", "The equals sign means the answer comes next, so the two sides of an equation must look alike."),
    ("M_BIGGER_NUMBERS", "The expression with the bigger numbers always has the bigger value."),
    ("M_TERM_PRODUCT", "A product like 6 × 5 is two terms because it has two numbers."),
]

SOLUTION_NOTES = []
ERRATA = []

DESIGN_REFERENCES = [
    {"text": "docs/25_new_design_learning_plan_playbook.md: framing intro, idea topics ending in "
             "a practice concept, a question topic after each idea topic, and one summary topic; the Class 7 "
             "Chapter 10 plan for one video per concept and one question per concept.", "url": ""},
]

FIGURES = {
    "T6.C3": ["Two arrangements of squares: five rows of two with three more, and two rows of five yellow and three blue."],
    "T8.C2": ["Scouts in four rows of five beside guides in three rows of five, marching in a parade."],
}
