# -*- coding: utf-8 -*-
"""Chapter-level content for Class 8 Chapter 13, Algebra Play (Ganita Prakash Grade 8 Part II, Chapter 6).
Book lines elsewhere are verbatim except: the book's dashes become commas, colons or "to"; minus is U+2212;
dates are written in words (26 January) instead of the book's 26/01, so no date sits next to an equals sign."""
from __future__ import annotations

CHAPTER = {
    "grade": 8,
    "label": "Class 8",
    "chapter_no": 13,
    "name": "Algebra Play",
    "book_part": "Ganita Prakash Grade 8 Part II, Chapter 6",
    "source_pdf": "textbooks/class8/hegp206.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Tricks That Always Work",
     "Think of a Number tricks and the date trick are explained with letter-numbers: the starting number cancels, "
     "or the answer hides the month and the day in its digits."),
    ("M2", "Pyramids and Grids",
     "Number pyramids are filled upward and downward, letters fill the hard boxes, and the top is written in terms "
     "of the bottom row. Calendar blocks and shape grids are decoded with simple equations."),
    ("M3", "Products, Divisibility and Puzzles",
     "The largest product from three digits is found and proved, reverse and subtract tricks are decoded with place "
     "value, and word puzzles are modelled and solved with letter-numbers, followed by a closing summary."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter is a set of games: tricks, pyramids, grids, products and puzzles. Each game is played with "
             "numbers first, the pattern is guessed, and then a letter-number explains why the pattern must hold. "
             "Students end each idea by inventing a trick or puzzle of their own.",
    "points": [
        {"title": "Play first, then explain",
         "text": "Every trick is tried with two or three starting numbers before any letter appears, so the letter "
                 "explains a pattern the student has already seen."},
        {"title": "Tools only where handling is the idea",
         "text": "Nine tools, each used once: building a trick, decoding a date trick, a pyramid builder, a shape "
                 "grid, a calendar frame, a digit arranger, a digit lab for 9, 11, 37 and 1001, a rounds machine, and "
                 "a swap counter. The remaining tricks and puzzles are taught without a tool because the algebra "
                 "itself is the move."},
        {"title": "Check by substituting",
         "text": "Every answer found with a letter-number is put back into the story or the grid to check it."},
        {"title": "Invent your own",
         "text": "Math Talk prompts ask for new tricks, new calendar shapes and new puzzles, built from the same "
                 "algebra."},
    ],
}

NCERT_ITEMS = [
    "6.1.intro",
    # 6.2 Thinking about Think of a Number tricks (pp 135 to 137)
    "6.2.trick2", "6.2.make3_5", "6.2.complicated", "6.2.date_trick", "6.2.date_1390", "6.2.find_dates",
    "6.2.mt_change_steps", "6.2.mt_own_trick",
    # 6.3 Number Pyramids (pp 137 to 140)
    "6.3.rule", "6.3.fill_up", "6.3.fill_down", "6.3.fill60", "6.3.fill_three_a", "6.3.fill_three_bc", "6.3.relation",
    "FiOA.q1", "FiOA.q2", "FiOA.q3", "FiOA.q4", "FiOA.q5", "FiOA.q6",
    # 6.4 Fun with Grids (pp 141, 142)
    "6.4.calendar_sum", "6.4.calendar_algebra", "6.4.mt_calendar_own", "6.4.grid_example", "6.4.grids_fill",
    # 6.5 The Largest Product (pp 142 to 144)
    "6.5.digits235", "6.5.six_pairs", "6.5.general",
    "FiOB.q1", "FiOB.q2",
    # 6.6 Decoding Divisibility Tricks (pp 144 to 147)
    "6.6.mukta_trick", "6.6.always", "6.6.a_gt_b",
    "FiOC.q1", "FiOC.q2", "FiOC.q3", "FiOC.q4", "FiOC.q5", "FiOC.q6", "FiOC.q7", "FiOC.q8", "FiOC.q9",
    "FiOC.q10", "FiOC.q11",
    "summary",
]

MISCONCEPTIONS = [
    ("M_TRICK_MAGIC", "A Think of a Number trick works only for the numbers tried, not for every number."),
    ("M_LETTER_ONE_VALUE", "A letter-number stands for one fixed value, so a trick with x cannot work for every start."),
    ("M_DATE_DIGITS", "In 100M + D the month is the first digit only, even when the month is 10, 11 or 12."),
    ("M_PYR_TOP_SUM", "The top of a pyramid is the plain sum of the bottom row."),
    ("M_PYR_DOWN_ADD", "To go down a pyramid you add, the same way as going up."),
    ("M_CAL_STEP", "In a calendar block the number below a date is one more, not seven more."),
    ("M_SHAPE_SAME", "Different shapes in a grid can stand for the same number without any check."),
    ("M_BIG_TENS", "The largest digit should always go in the tens place of the two digit number."),
    ("M_DIFF_ORDER", "When the reversed number is smaller the difference is not a multiple of 9."),
    ("M_STORY_ORDER", "In a word puzzle the numbers can be combined in the order they appear, without a model."),
    ("M_PROFIT_PRICE", "Profit is the selling price minus the cost of one item, ignoring fixed costs like rent."),
]

SOLUTION_NOTES = [
    "Algebra grid with circles and diamonds: the book leaves a blank fourth row; it is read here as the column "
    "sums (18, 15, 15) with the grand total 48 in the corner.",
    "Shrines puzzle: any start of 7k flowers with 8k in each shrine works; the smallest is 7 flowers and 8 per shrine.",
    "Karim and the Genie: Karim starts with 7 coins; with c coins taken each round his coins grow only when c is "
    "less than what he holds; to take everything in three rounds the genie sets c to 8 ÷ 7 of Karim's coins.",
]
ERRATA = []

DESIGN_REFERENCES = [
    {"text": "docs/25_new_design_learning_plan_playbook.md: framing intro, idea topics each ending in a practice "
             "concept, a question topic after each idea topic with several questions, and one summary topic.",
     "url": ""},
]

FIGURES = {}
