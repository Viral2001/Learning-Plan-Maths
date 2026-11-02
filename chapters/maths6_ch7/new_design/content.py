# -*- coding: utf-8 -*-
"""Chapter-level content for Class 6 Chapter 7, Fractions (Ganita Prakash Grade 6, Chapter 7).
Book lines elsewhere are verbatim except: the book's dashes become commas, colons or "to"; minus is U+2212;
"3 times 1/4" is written "3 × 1/4" so the equation checker reads it as a product, not as "1/4 = 3/4"."""
from __future__ import annotations

CHAPTER = {
    "grade": 6,
    "label": "Class 6",
    "chapter_no": 7,
    "name": "Fractions",
    "book_part": "Ganita Prakash Grade 6, Chapter 7",
    "source_pdf": "textbooks/class6/fegp107.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Fractional Units and Equal Shares",
     "Sharing rotis and chikki fairly gives fractional units. Folding strips measures lengths in those units, and "
     "the same lengths are marked on the number line."),
    ("M2", "Beyond One, and Equal Fractions",
     "Fractions bigger than one become mixed numbers. Different fractions can name the same share: equivalent "
     "fractions, and the simplest name for a share, its lowest terms."),
    ("M3", "Comparing, Adding and Subtracting",
     "Two fractions are compared, added and subtracted by first writing them in the same fractional unit, "
     "Brahmagupta's method."),
    ("M4", "History and Summary",
     "How India wrote and named fractions, the Egyptian unit fraction puzzle, and the chapter summary."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter follows the book's order. Equal sharing gives the fractional unit, measuring and the "
             "number line make a fraction a length and a number, and one idea, write both fractions in the same "
             "fractional unit, carries comparing, adding and subtracting.",
    "points": [
        {"title": "Shares before symbols",
         "text": "Every new idea starts from a share of roti, chikki or a paper strip, so the symbol 3/4 always "
                 "means three pieces of one quarter."},
        {"title": "Concept, then practice, topic by topic",
         "text": "Each idea gets its own topic: worked videos for the book's examples, one tool to do it by hand, "
                 "then the book's Figure it Out questions in a practice topic, each with its own video."},
        {"title": "One unit for everything",
         "text": "Equivalent fractions are the tool: to compare, add or subtract, rewrite both fractions in the "
                 "same fractional unit, then count units."},
        {"title": "Keeko's doubts",
         "text": "The common wrong ideas, such as '1/9 is more than 1/5' or '1/2 + 1/3 makes 2/5', are raised by Keeko and fixed "
                 "with a picture, never just a rule."},
    ],
}

# Every book item, in book order. Ids come from the page-image inventory (page = rendered image index).
NCERT_ITEMS = [
    "opening",
    # 7.0 opening dialogue and 7.1
    "7.0.ex1", "7.1.ex1", "7.1.FiO.Q1", "7.1.FiO.Q2", "7.1.FiO.Q3", "7.1.FiO.Q4", "7.1.q1", "7.1.FiO.Q5",
    # 7.2
    "7.2.ex1", "7.2.q1", "7.2.ex2", "7.2.FiO.Q1",
    # 7.3
    "7.3.ex1", "7.3.ex2", "7.3.q1", "7.3.ex3", "7.3.FiO.Q1", "7.3.FiO.Q2", "7.3.FiO.Q3", "7.3.FiO.Q4",
    "7.3.FiO.Q5",
    # 7.4
    "7.4.ex1", "7.4.q1", "7.4.q2", "7.4.q3", "7.4.FiO.Q1", "7.4.FiO.Q2", "7.4.FiO.Q3", "7.4.FiO.Q4",
    "7.4.FiO.Q5",
    # 7.5
    "7.5.q1", "7.5.q2", "7.5.ex1", "7.5.ex2", "7.5.ex3", "7.5.FiO1.Q1", "7.5.FiO1.Q2", "7.5.ex4",
    "7.5.FiO2.Q1", "7.5.ex5", "7.5.FiO2.Q2", "7.5.FiO2.Q3", "7.5.ex6", "7.5.FiO3.Q1",
    # 7.6
    "7.6.q1", "7.6.q2", "7.6.q3", "7.6.q4", "7.6.q5", "7.6.q6", "7.6.FiO1.Q1", "7.6.FiO1.Q2", "7.6.FiO1.Q3",
    "7.6.ex1", "7.6.FiO2.Q1", "7.6.FiO2.Q2", "7.6.FiO2.Q3", "7.6.q7", "7.6.q8", "7.6.q9", "7.6.q10",
    "7.6.q11", "7.6.FiO3.Q1", "7.6.ex2", "7.6.ex3", "7.6.q12", "7.6.q13", "7.6.ex4", "7.6.q14", "7.6.ex5",
    "7.6.ex6", "7.6.FiO4.Q1",
    # 7.7
    "7.7.q1", "7.7.q2", "7.7.FiO.Q1", "7.7.FiO.Q2", "7.7.FiO.Q3",
    # 7.8
    "7.8.q1", "7.8.q2", "7.8.ex1", "7.8.ex2", "7.8.q3", "7.8.ex3", "7.8.ex4", "7.8.ex5", "7.8.FiO1.Q1",
    "7.8.FiO1.Q2", "7.8.FiO1.Q3", "7.8.q4", "7.8.q5", "7.8.FiO2.Q1", "7.8.FiO2.Q2", "7.8.FiO2.Q3", "7.8.ex6",
    "7.8.q6", "7.8.q7", "7.8.FiO3.Q1", "7.8.FiO3.Q2", "7.8.FiO3.Q3",
    # 7.9
    "7.9.q1", "7.9.q2", "7.9.q3", "7.9.q4",
    "summary",
]

# Frozen home of every book item: (topic key, concept key, "WE" worked example in a teaching concept, or
# "FIO" Figure it Out item in the topic's DOER, which core.qt then moves into the practice topic).
ITEM_HOME = {
    "opening": ("T1", "T1.C1", "HOOK"),
    "7.0.ex1": ("T2", "T2.C1", "WE"), "7.1.ex1": ("T2", "T2.C2", "WE"), "7.1.q1": ("T2", "T2.C2", "WE"),
    "7.1.FiO.Q1": ("T2", "T2.C3", "FIO"), "7.1.FiO.Q2": ("T2", "T2.C3", "FIO"),
    "7.1.FiO.Q3": ("T2", "T2.C3", "FIO"), "7.1.FiO.Q4": ("T2", "T2.C3", "FIO"),
    "7.1.FiO.Q5": ("T2", "T2.C3", "FIO"),
    "7.2.ex1": ("T3", "T3.C1", "WE"), "7.2.q1": ("T3", "T3.C1", "WE"), "7.2.ex2": ("T3", "T3.C2", "WE"),
    "7.2.FiO.Q1": ("T3", "T3.C3", "FIO"),
    "7.3.ex1": ("T4", "T4.C1", "WE"), "7.3.ex2": ("T4", "T4.C1", "WE"), "7.3.q1": ("T4", "T4.C1", "WE"),
    "7.3.ex3": ("T4", "T4.C2", "WE"),
    "7.3.FiO.Q1": ("T4", "T4.C3", "FIO"), "7.3.FiO.Q2": ("T4", "T4.C3", "FIO"),
    "7.3.FiO.Q3": ("T4", "T4.C3", "FIO"), "7.3.FiO.Q4": ("T4", "T4.C3", "FIO"),
    "7.3.FiO.Q5": ("T4", "T4.C3", "FIO"),
    "7.4.ex1": ("T5", "T5.C1", "WE"), "7.4.q1": ("T5", "T5.C1", "WE"), "7.4.q2": ("T5", "T5.C2", "WE"),
    "7.4.q3": ("T5", "T5.C2", "WE"),
    "7.4.FiO.Q1": ("T5", "T5.C3", "FIO"), "7.4.FiO.Q2": ("T5", "T5.C3", "FIO"),
    "7.4.FiO.Q3": ("T5", "T5.C3", "FIO"), "7.4.FiO.Q4": ("T5", "T5.C3", "FIO"),
    "7.4.FiO.Q5": ("T5", "T5.C3", "FIO"),
    "7.5.q1": ("T6", "T6.C1", "WE"), "7.5.q2": ("T6", "T6.C1", "WE"), "7.5.ex1": ("T6", "T6.C1", "WE"),
    "7.5.ex2": ("T6", "T6.C1", "WE"), "7.5.ex3": ("T6", "T6.C2", "WE"), "7.5.ex4": ("T6", "T6.C2", "WE"),
    "7.5.ex5": ("T6", "T6.C2", "WE"), "7.5.ex6": ("T6", "T6.C2", "WE"),
    "7.5.FiO1.Q1": ("T6", "T6.C3", "FIO"), "7.5.FiO1.Q2": ("T6", "T6.C3", "FIO"),
    "7.5.FiO2.Q1": ("T6", "T6.C3", "FIO"), "7.5.FiO2.Q2": ("T6", "T6.C3", "FIO"),
    "7.5.FiO2.Q3": ("T6", "T6.C3", "FIO"), "7.5.FiO3.Q1": ("T6", "T6.C3", "FIO"),
    "7.6.q1": ("T7", "T7.C1", "WE"), "7.6.q2": ("T7", "T7.C1", "WE"), "7.6.q3": ("T7", "T7.C1", "WE"),
    "7.6.q4": ("T7", "T7.C1", "WE"), "7.6.q5": ("T7", "T7.C1", "WE"), "7.6.q6": ("T7", "T7.C1", "WE"),
    "7.6.ex1": ("T7", "T7.C2", "WE"), "7.6.q7": ("T7", "T7.C2", "WE"), "7.6.q8": ("T7", "T7.C2", "WE"),
    "7.6.q9": ("T7", "T7.C3", "WE"), "7.6.q10": ("T7", "T7.C3", "WE"), "7.6.q11": ("T7", "T7.C3", "WE"),
    "7.6.FiO1.Q1": ("T7", "T7.C4", "FIO"), "7.6.FiO1.Q2": ("T7", "T7.C4", "FIO"),
    "7.6.FiO1.Q3": ("T7", "T7.C4", "FIO"), "7.6.FiO2.Q1": ("T7", "T7.C4", "FIO"),
    "7.6.FiO2.Q2": ("T7", "T7.C4", "FIO"), "7.6.FiO2.Q3": ("T7", "T7.C4", "FIO"),
    "7.6.FiO3.Q1": ("T7", "T7.C4", "FIO"),
    "7.6.ex5": ("T8", "T8.C1", "WE"), "7.6.ex6": ("T8", "T8.C1", "WE"),
    "7.6.FiO4.Q1": ("T8", "T8.C2", "FIO"),
    "7.6.ex2": ("T9", "T9.C1", "WE"), "7.6.ex3": ("T9", "T9.C1", "WE"), "7.6.q12": ("T9", "T9.C1", "WE"),
    "7.6.q13": ("T9", "T9.C2", "WE"), "7.6.ex4": ("T9", "T9.C2", "WE"), "7.7.q1": ("T9", "T9.C2", "WE"),
    "7.7.q2": ("T9", "T9.C2", "WE"),
    "7.6.q14": ("T9", "T9.C3", "FIO"), "7.7.FiO.Q1": ("T9", "T9.C3", "FIO"),
    "7.7.FiO.Q2": ("T9", "T9.C3", "FIO"), "7.7.FiO.Q3": ("T9", "T9.C3", "FIO"),
    "7.8.q1": ("T10", "T10.C1", "WE"), "7.8.q2": ("T10", "T10.C1", "WE"), "7.8.ex1": ("T10", "T10.C1", "WE"),
    "7.8.ex2": ("T10", "T10.C1", "WE"), "7.8.q3": ("T10", "T10.C1", "WE"),
    "7.8.ex3": ("T10", "T10.C2", "WE"), "7.8.ex4": ("T10", "T10.C2", "WE"), "7.8.ex5": ("T10", "T10.C2", "WE"),
    "7.8.FiO1.Q1": ("T10", "T10.C3", "FIO"), "7.8.FiO1.Q2": ("T10", "T10.C3", "FIO"),
    "7.8.FiO1.Q3": ("T10", "T10.C3", "FIO"),
    "7.8.q4": ("T11", "T11.C1", "WE"), "7.8.q5": ("T11", "T11.C1", "WE"),
    "7.8.ex6": ("T11", "T11.C2", "WE"), "7.8.q6": ("T11", "T11.C2", "WE"), "7.8.q7": ("T11", "T11.C2", "WE"),
    "7.8.FiO2.Q1": ("T11", "T11.C3", "FIO"), "7.8.FiO2.Q2": ("T11", "T11.C3", "FIO"),
    "7.8.FiO2.Q3": ("T11", "T11.C3", "FIO"), "7.8.FiO3.Q1": ("T11", "T11.C3", "FIO"),
    "7.8.FiO3.Q2": ("T11", "T11.C3", "FIO"), "7.8.FiO3.Q3": ("T11", "T11.C3", "FIO"),
    "7.9.q1": ("T12", "T12.C1", "WE"),
    "7.9.q2": ("T12", "T12.C2", "FIO"), "7.9.q3": ("T12", "T12.C2", "FIO"), "7.9.q4": ("T12", "T12.C2", "FIO"),
    "summary": ("T13", "T13.C1", "RECAP"),
}
assert set(ITEM_HOME) == set(NCERT_ITEMS), set(ITEM_HOME) ^ set(NCERT_ITEMS)

MISCONCEPTIONS = [
    ("M_BIG_DENOM", "A bigger denominator means a bigger fraction, so 1/9 is greater than 1/5."),
    ("M_UNEQUAL_PARTS", "Any piece cut from a whole is a fraction of it, even when the pieces are not equal."),
    ("M_COUNT_PIECES", "A piece's fraction is set by how many pieces there are, not by how many equal units of "
                       "the whole fit into it."),
    ("M_NUM_DENOM", "The numerator and the denominator mean the same kind of thing, so they can be swapped or "
                    "read in either order."),
    ("M_TICKS_NOT_GAPS", "On a number line, count the marks rather than the equal gaps between 0 and 1."),
    ("M_LESS_THAN_ONE", "A fraction is always less than 1, so 5/4 or 7/2 is not a real fraction."),
    ("M_MIXED_PRODUCT", "A mixed number such as 2 1/2 means 2 × 1/2, or 21/2."),
    ("M_EQUIV_ADD", "Adding the same number to the numerator and the denominator gives an equal fraction."),
    ("M_EQUIV_DIFFERENT", "Fractions with different numbers, such as 1/2 and 4/8, must be different amounts."),
    ("M_LOWEST_PARTIAL", "A fraction is in lowest terms as soon as it has been divided once, even when a "
                         "common factor is left."),
    ("M_COMPARE_PARTS", "Compare two fractions by their numerators, or by the gap between numerator and "
                        "denominator, without making the units the same."),
    ("M_ADD_TOPS_BOTTOMS", "Add fractions by adding the numerators and adding the denominators, so "
                           "1/2 + 1/3 would make 2/5."),
    ("M_SUB_TOPS_BOTTOMS", "Subtract fractions by subtracting the numerators and the denominators separately."),
    ("M_SAME_UNIT_ONLY", "Fractions with different denominators cannot be added or subtracted at all."),
]

SOLUTION_NOTES = [
    "7.3.FiO.Q3: the official solution says only 'Try Further!'; the answer given (fold in thirds, then in half) "
    "is worked here.",
    "7.4.FiO.Q3: the official solution says 'uncountable'; there are infinitely many fractions between 0 and 1, "
    "and the plan says 'infinitely many'.",
    "7.6.q13 part 1: the official solution answers only part 2; part 1 (3/4 > 7/10) is worked here.",
]
ERRATA = [
    "7.6.ex3: the book prints 'compare 1/7 and 4/7'; the comparison is 1/2 and 4/7.",
    "7.6.FiO4.Q1: the parts are printed a, b, e, d; the third part is c.",
    "7.8.FiO1.Q1: part k repeats part e (3/4 + 1/3 + 1/5).",
]

DESIGN_REFERENCES = [
    {"text": "maths6_ch3 new_design Phase 2 plan: framing intro with one hook, idea topics ending in one doer "
             "tool, a practice topic after each idea topic with one video per book question, one summary topic.",
     "url": ""},
]

FIGURES = {
    "T1.C1": ["A round roti cut into 2 equal halves, and another into 4 equal quarters, with children around."],
    "T3.C1": ["A chikki bar drawn as 24 equal small squares, 6 across and 4 down, broken into pieces."],
    "T4.C1": ["A paper strip folded into 2, then 4, then 8 equal parts, each part labelled."],
    "T5.C1": ["A number line from 0 to 1 split into equal gaps, with blue lines of fraction lengths above it."],
    "T7.C1": ["A fraction wall: rows for 1, halves, thirds and so on down to tenths, aligned at the left."],
}
