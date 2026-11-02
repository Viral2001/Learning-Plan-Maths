# -*- coding: utf-8 -*-
"""Chapter-level content for Class 8 Chapter 1, A Square and A Cube (Ganita Prakash Grade 8 Part I, Chapter 1).
Book lines elsewhere are verbatim except: the book's dashes become commas, colons or "to"; minus is U+2212;
the book's "±" is written out as "8 or −8"."""
from __future__ import annotations

CHAPTER = {
    "grade": 8,
    "label": "Class 8",
    "chapter_no": 1,
    "name": "A Square and A Cube",
    "book_part": "Ganita Prakash Grade 8 Part I, Chapter 1",
    "source_pdf": "textbooks/class8/hegp101.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "The Queen's Locker Puzzle",
     "A hundred lockers are opened and closed by a hundred people. Counting how often each locker is touched turns "
     "into counting factors, and the lockers left open are exactly the square numbers."),
    ("M2", "Square Numbers and Square Roots",
     "Squares as areas, the digits squares can and cannot end in, squares built from odd numbers, the gaps between "
     "consecutive squares, and three ways to find a square root: listing, subtracting odd numbers and pairing prime "
     "factors, plus estimating roots that are not whole numbers."),
    ("M3", "Cubic Numbers and Cube Roots",
     "Cubes as solids built from unit cubes, the digits cubes end in, taxicab numbers, cubes made from consecutive "
     "odd numbers, successive differences, and cube roots found by grouping prime factors in threes."),
    ("M4", "Looking Back",
     "A summary of squares and cubes, the history of the words square, cube and root, and the Square Pairs puzzle."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter opens with the queen's locker puzzle and lets the answer, the square numbers, lead into "
             "everything else. Each idea starts with a prediction (will this locker stay open, can a square end in "
             "7, how many cubes make this block), then a picture or a pattern explains why. Squares come first, as "
             "areas, digits and sums of odd numbers; then square roots by three methods and by estimation; then "
             "the same journey for cubes.",
    "points": [
        {"title": "Predict, then check",
         "text": "Every concept opens with a question the student answers before the video reveals it, such as "
                 "which lockers stay open or whether 2032 can be a square."},
        {"title": "Pictures that prove",
         "text": "Squares are drawn as tiles and cubes as stacks of unit cubes, and the odd number pattern is shown "
                 "with inverted L shapes, so each rule is seen before it is used."},
        {"title": "One tool, one idea",
         "text": "Ten tools, each used once, appear only where handling the objects is the idea itself: lockers and "
                 "squares, building squares and cubes, odd-number corners, the gap between squares, finding a side "
                 "from an area, pairing and tripling prime factors, trapping a root between two whole numbers, and a "
                 "ladder of differences."},
        {"title": "Several roads to a root",
         "text": "Square roots are found by listing squares, by subtracting odd numbers, by pairing prime factors "
                 "and by estimating with nearby squares, and the student learns when each road is quickest."},
    ],
}

NCERT_ITEMS = [
    "opening",
    # The locker puzzle (pp 1 to 3)
    "1.0.factors", "1.0.even_factors", "1.0.odd_insight", "1.0.square_def", "1.0.open_lockers", "1.0.five_lockers",
    # 1.1 Square numbers as areas (p 3 to 4)
    "1.1.area_table", "1.1.notation", "1.1.perfect_def",
    # Patterns and properties of squares (pp 4 to 5)
    "1.1.table30", "1.1.mt_patterns", "1.1.mt_always", "1.1.five_nonsquares", "1.1.ends1", "1.1.ends6",
    "1.1.which6", "1.1.more_patterns", "1.1.zeros", "1.1.parity",
    # Perfect squares and odd numbers (pp 5 to 6)
    "1.1.odd_diffs", "1.1.odd_sum", "1.1.subtract_test", "1.1.next_square", "1.1.nth_odd",
    # Between squares, triangular numbers (p 7)
    "1.1.between", "1.1.blocks", "1.1.triangular",
    # Square roots (pp 7 to 9)
    "1.1.root_side", "1.1.root_def", "1.1.mt_576", "1.1.subtract_root",
    "1.1.prime_324", "1.1.prime_156", "1.1.prime_try",
    # Estimating square roots (pp 9 to 10)
    "1.1.est_1936", "1.1.est_game", "1.1.est_cloth",
    # Figure it Out, square numbers (questions 1 to 9)
    "FiO1.q1", "FiO1.q2", "FiO1.q3", "FiO1.q4", "FiO1.q5", "FiO1.q6", "FiO1.q7", "FiO1.q8", "FiO1.q9",
    # 1.2 Cubic numbers (pp 11 to 13)
    "1.2.cube_2", "1.2.cube_3", "1.2.cube_9", "1.2.cube_4", "1.2.cube_table", "1.2.mt_cube_patterns",
    "1.2.cube_digits", "1.2.cube_count_digits", "1.2.cube_00", "1.2.cube_other",
    # Taxicab numbers, cubes and odd numbers (pp 13 to 14)
    "1.2.taxicab", "1.2.try_taxicab", "1.2.odd_cubes", "1.2.odd_91",
    # Cube roots and successive differences (pp 14 to 15)
    "1.2.root_def", "1.2.root_3375", "1.2.root_500", "1.2.root_find", "1.2.diff_squares", "1.2.diff_cubes",
    # Figure it Out, cubic numbers (questions 1 to 5)
    "FiO2.q1", "FiO2.q2", "FiO2.q3", "FiO2.q4", "FiO2.q5",
    # 1.3 A Pinch of History, summary, puzzle (pp 15 to 18)
    "history", "summary", "puzzle",
]

MISCONCEPTIONS = [
    ("M_FACTORS_EVEN", "Every number has an even number of factors, because factors always come in pairs."),
    ("M_SQUARE_DOUBLE", "Squaring a number means doubling it, so 6 squared is 12."),
    ("M_DIGIT_ENOUGH", "Any number that ends in 0, 1, 4, 5, 6 or 9 must be a perfect square."),
    ("M_ZEROS_SAME", "A number with 3 zeros at the end has a square with 3 zeros at the end."),
    ("M_ROOT_HALF", "The square root of a number is half of it, so the square root of 64 is 32."),
    ("M_ROOT_ONE_SIGN", "Only 8 squares to 64; a negative number can never square to a positive number."),
    ("M_PRIME_ANY", "A number is a perfect square if it has any repeated prime factor."),
    ("M_ROOT_NEAREST", "The square root of a number that is not a perfect square is the nearest whole number."),
    ("M_CUBE_TRIPLE", "Cubing a number means multiplying it by 3, so 4 cubed is 12."),
    ("M_CUBE_DIGITS", "Cubes can only end in the same digits as squares."),
    ("M_CUBE_ZEROS", "A cube can end in exactly two zeros."),
    ("M_BETWEEN_N", "Between n squared and the next square there are n numbers."),
    ("M_ODD_CUBE_EVEN", "The cube of an odd number can be even."),
]

SOLUTION_NOTES = [
    "Figure it Out (square numbers) question 9: the picture has 9 rows of 9 tiles, and every tile, upright or turned, "
    "is a 5 by 5 grid of tiny squares, so there are 81 × 25 = 2025 = 3⁴ × 5² tiny squares, which is 45².",
    "Square Pairs: up to reversal, 16, 9, 7, 2, 14, 11, 5, 4, 12, 13, 3, 6, 10, 15, 1, 8, 17 is the only line of 1 to "
    "17 (checked by a computer search); a circle of 1 to 32 exists, for example 1, 8, 28, 21, 4, 32, 17, 19, 30, 6, 3, "
    "13, 12, 24, 25, 11, 5, 31, 18, 7, 29, 20, 16, 9, 27, 22, 14, 2, 23, 26, 10, 15.",
]
ERRATA = []

DESIGN_REFERENCES = [
    {"text": "docs/25_new_design_learning_plan_playbook.md: framing intro, idea topics each ending in a doer, a "
             "question topic after each idea topic, and one summary topic.", "url": ""},
]

FIGURES = {}
