# -*- coding: utf-8 -*-
"""Chapter-level content for Class 8 Chapter 6, We Distribute, Yet Things Multiply (Ganita Prakash Grade 8 Part I,
Chapter 6). Book lines elsewhere are verbatim except: the book's dashes become commas, colons or "to"; minus is
U+2212; powers are written with superscripts (a², 65²) and fractions with a slash (3/10)."""
from __future__ import annotations

CHAPTER = {
    "grade": 8,
    "label": "Class 8",
    "chapter_no": 6,
    "name": "We Distribute, Yet Things Multiply",
    "book_part": "Ganita Prakash Grade 8 Part I, Chapter 6",
    "source_pdf": "textbooks/class8/hegp106.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "How Products Grow",
     "A product is a rectangle of rows and columns, so the question of how much it grows when one number grows "
     "opens the chapter."),
    ("M2", "Distributing and Multiplying",
     "The distributive property a(b + c) = ab + ac, how a product changes when its numbers change, the product of "
     "two sums term by term, like terms, and quick multiplication by 11, 101, 99 and their relatives."),
    ("M3", "Special Products",
     "The square of a sum, the square of a difference and the difference of two squares, seen as areas and used "
     "for fast squaring and for explaining number patterns."),
    ("M4", "Many Ways to See",
     "Finding and mending mistakes in simplification, choosing a suitable identity, and describing one pattern or "
     "one area in several equivalent ways."),
    ("M5", "Looking Back",
     "A summary of the identities and the Coin Conjoin puzzle."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter grows out of one question: when a number in a product changes, how does the product "
             "change? A product is drawn as a rectangle of rows and columns, so splitting a side splits the "
             "rectangle, and every identity in the chapter (the product of two sums, the square of a sum or a "
             "difference, the difference of two squares) is first seen as an area and then checked by the "
             "distributive property.",
    "points": [
        {"title": "Predict, then expand",
         "text": "Every concept opens with a prediction, such as whether (a + b)² is bigger than a² + b², and the "
                 "distributive property then settles it term by term."},
        {"title": "Areas make identities visible",
         "text": "Rectangles split into rows and columns, a square of 65 split into four parts, and a square of 55 "
                 "carved out of a square of 60 show why each identity holds."},
        {"title": "Numbers first, letters next",
         "text": "Fast multiplication, fast squaring and number patterns come first as arithmetic and are then "
                 "explained with letter-numbers that work for every integer and fraction."},
        {"title": "Tools only where handling is the idea",
         "text": "Ten tools, each used once: splitting a rectangle, collecting the four parts of a product of two "
                 "sums, adding neighbour digits, building the square of a sum and of a difference, sliding a "
                 "difference of squares, generalising a pattern, sorting expressions by identity, four rectangles in a "
                 "square, and regrouping a growing pattern."},
    ],
}

NCERT_ITEMS = [
    "opening",
    # 6.1 Increments in products and the distributive property (pp 136 to 139)
    "6.1.increments_q", "6.1.dist_prop", "6.1.ab_c", "6.1.both_inc", "6.1.both_inc_other_order", "6.1.inc_dec",
    "6.1.decrease_examples", "6.1.negatives", "6.1.identities",
    # Identity for (a + m)(b + n) and its sign cases (pp 139 to 140)
    "6.1.identity1", "6.1.id1_minus1", "6.1.id1_decrease_task", "6.1.au_bv", "6.1.au_bv_expand",
    # More than two terms, like terms, worked examples and history (pp 140 to 142)
    "6.1.ex1", "6.1.like_terms", "6.1.ex2", "6.1.ex3", "6.1.history_khanda",
    # Figure it Out, set 1 (questions 1 to 5)
    "FiO1.q1", "FiO1.q2", "FiO1.q3", "FiO1.q4", "FiO1.q5",
    # Fast multiplication (pp 143 to 144)
    "6.1.fast11", "6.1.fast11_rule", "6.1.fast11_eval", "6.1.fast101", "6.1.fast101_rule", "6.1.fast101_eval",
    "6.1.history_ista",
    # 6.2 Square of a sum (pp 145 to 146)
    "6.2.sq65", "6.2.sq65_splits", "6.2.id_sum_sq", "6.2.compare_sum_sq", "6.2.sq104_37", "6.2.m3_6p",
    "6.2.6x5", "6.2.3j2k",
    # Square of a difference (pp 146 to 147)
    "6.2.sq55", "6.2.id_diff_sq", "6.2.diff_sq_geometry", "6.2.sq99_58", "6.2.expand_diff_sq",
    # Investigating patterns, difference of squares, Sridharacharya (pp 147 to 149)
    "6.2.pattern1", "6.2.pattern2", "6.2.id_diff_squares", "6.2.use_diff_squares", "6.2.try_geometric",
    "6.2.sridhara",
    # Figure it Out, set 2 (questions 1 to 4)
    "FiO2.q1", "FiO2.q2", "FiO2.q3", "FiO2.q4",
    # 6.3 Mind the mistake, mend the mistake (p 150)
    "6.3.cards_a", "6.3.cards_b",
    # 6.4 This way or that way (pp 150 to 154)
    "6.4.circles", "6.4.circles_step15", "6.4.many_ways", "6.4.tiles", "6.4.tadang_yusuf", "6.4.slanted",
    "6.4.dashed",
    # Figure it Out, set 3 (questions 1 to 11)
    "FiO3.q1", "FiO3.q2", "FiO3.q3", "FiO3.q4", "FiO3.q5", "FiO3.q6", "FiO3.q7", "FiO3.q8", "FiO3.q9",
    "FiO3.q10", "FiO3.q11",
    # Summary and Coin Conjoin (pp 157 to 158)
    "summary", "puzzle",
]

MISCONCEPTIONS = [
    ("M_SUM_SQUARE", "(a + b)² is just a² + b²; the two rectangles ab are forgotten."),
    ("M_DIFF_SQUARE", "(a − b)² is just a² − b², or the sign of b² is taken as minus."),
    ("M_DISTRIBUTE_FIRST_ONLY", "In a(b + c) only the first term is multiplied, giving ab + c."),
    ("M_SIGN_DISTRIBUTE", "A minus sign in front of a bracket changes only the first term inside it."),
    ("M_UNLIKE_ADD", "Unlike terms such as 5w² and 6w can be added into one term, 11w²."),
    ("M_PRODUCT_INCREASE", "If one number goes up by 1 and the other down by 1, the product stays the same."),
    ("M_TWO_TERMS_ONLY", "The product of two sums has only two terms, first times first and last times last."),
    ("M_MULTIPLY_EACH_FACTOR", "In a × (b × c) the multiplier a is applied to both b and c."),
    ("M_ONE_RIGHT_WAY", "A pattern has only one correct expression, so different-looking answers must be wrong."),
]

SOLUTION_NOTES = [
    "Pattern 2 (p 148): the book prints (a + b) × (a − b) = a² − ab + ba − a²; the last term should be −b², and the "
    "plan quotes the corrected line.",
    "Identity 1 with a decrease (p 140): the book prints (a + 1)(b + (–1); the bracket is not closed. The plan "
    "writes (a + 1)(b + (−1)).",
    "Figure it Out set 3, question 6: the difference of the two numbers leaves remainder 2 when divided by 7 if the "
    "second number is subtracted from the first in the order (remainder 5) minus (remainder 3), and remainder 5 "
    "the other way round; the plan gives both.",
    "Figure it Out set 3, question 5(iii): squares of odd numbers are 1 more than a multiple of 8, because "
    "(2m + 1)² − 1 = 4m(m + 1) and m(m + 1) is even; the statement is true.",
    "Figure it Out set 3, question 5(iv): (6n + 2)² − (4n + 3)² = 20n² − 5, which is 5 less than 20n²; 20n² is not "
    "a square for every n (for n = 1 it is 20), so the statement is false in general.",
    "Answer key, Figure it Out set 3, question 4 (calendar): the working printed with the key has a typo in one "
    "line; the plan works it as (a + 1)(a + 7) − a(a + 8) = 7.",
]
ERRATA = [
    "Pattern 2 (p 148): (a + b) × (a − b) = a² − ab + ba − a² should end with −b².",
    "Identity 1 (p 140): (a + 1)(b + (–1) is missing a closing bracket.",
    "Answer key, calendar question: a typo in the printed working; the result, a difference of 7, is right.",
]

DESIGN_REFERENCES = [
    {"text": "docs/25_new_design_learning_plan_playbook.md: framing intro, idea topics each ending in a doer, a "
             "question topic after each idea topic, and one summary topic.", "url": ""},
]

FIGURES = {}
