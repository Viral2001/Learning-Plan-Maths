# -*- coding: utf-8 -*-
"""Chapter-level content for Class 5 Chapter 1, We the Travellers - I (Maths Mela, Grade 5, Chapter 1). Book lines are
verbatim except: the book's dashes become commas, colons or "to"; minus is U+2212; the book's "Let Us Do" blanks are
solved in the plan, not printed blank."""
from __future__ import annotations

CHAPTER = {
    "grade": 5,
    "label": "Class 5",
    "chapter_no": 1,
    "name": "We the Travellers - I",
    "book_part": "Maths Mela, Grade 5, Chapter 1",
    "source_pdf": "textbooks/class5/eemm101.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Big Numbers: Reading, Writing and Comparing",
     "Counting thousands up to ten thousand, the new Ten Thousands column, reading and writing five-digit numbers with "
     "commas and number names, patterns in sequences, comparing and ordering large numbers, placing them on a number "
     "line, swapping digits, expanded form and counting in tens, hundreds and thousands."),
    ("M2", "Nearest Numbers and Journeys",
     "A hungry rabbit finds the nearest ten, hundred and thousand of a number, and then the numbers become real: how "
     "far people travel in an hour on foot, by horse, cycle, train, ship, aircraft and spacecraft, and how many "
     "vehicles carry a school of 900 people."),
    ("M3", "Large Numbers Around Us and Pastime Mathematics",
     "Finding four-digit and five-digit counts in the book, the classroom, a tree and a village, then three train "
     "puzzles and a story: the river crossing, the pile of pebbles, Mira's puzzle that always ends in 9, and the "
     "King's Horses."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter follows the book's own order: ten thousand and the new TTh column first, then reading, "
             "writing, patterns, comparing and ordering, the number line and rounding, and finally the journeys and "
             "puzzles that use large numbers. Every idea starts with something the student does, and the tools put "
             "number cards, tokens and number lines in the student's hands.",
    "points": [
        {"title": "Build it, then name it",
         "text": "Students first build a number from tokens or cards and only then read it, write it in digits with "
                 "commas and write its name. The chart shows where every digit sits."},
        {"title": "Predict before the reveal",
         "text": "Each idea opens with a question answered before the picture: what comes after nine thousand, which "
                 "of two numbers is greater, which ten is nearest to 2,346."},
        {"title": "Tools only where handling is the idea",
         "text": "Ten tools, each used once: an odometer, ten-thousand builder, token table, pattern rule finder, "
                 "compare chart, number line, rabbit rounder, vehicle loader, digit difference machine and the king's "
                 "stable. Ideas about meaning and puzzles that need only a discussion carry no tool."},
        {"title": "Every book question has its own video",
         "text": "Each Let Us Do, Let Us Think and puzzle question is its own short video, in a Questions topic that "
                 "follows the idea it practises."},
    ],
}

NCERT_ITEMS = [
    "opening",
    # Reading and writing large numbers: ten thousand
    "r.thousands", "r.ten_thousand", "r.place_chart", "r.comma", "r.indian_system", "r.expanded_1380", "r.expanded_9123",
    # Token table beyond 10,000
    "r.tok_10001_10002", "r.tok_10010_10024", "r.tok_10033", "r.tok_10458", "r.tok_11214", "r.tok_13520",
    "r.tok_20000", "r.tok_45867",
    "LUD1.names", "LUD1.numbers",     # Let Us Do 2 of the first set, names and numbers
    # Patterns and order
    "LUD1.p_abc", "LUD1.p_defg", "LUD1.p_hi",
    "LUD3.order", "LUD4.claim",
    # Digit swap
    "LUD5.a", "LUD5.b", "LUD5.c",
    # Nearest tens, hundreds, thousands
    "rab.tens", "rab.hundreds", "rab.thousands", "rab.table",
    "LUT1", "LUT2", "LUT3",
    # Travelling, now and then
    "tr.intro", "tr.speeds", "tr.cyclist", "tr.vehicles_ad", "tr.vehicles_eh",
    # Finding large numbers around us
    "ar.book", "ar.school", "ar.classroom", "ar.tree_village",
    # Pastime mathematics
    "pm.river", "pm.pebbles", "pm.mira_steps", "pm.mira_explore", "pm.mira_table", "pm.mira_asks",
    # Let Us Do, second set
    "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8.ab", "B8.cdefg", "B9.hundreds_tens", "B9.big",
    # King's Horses
    "kh.story", "kh.mistake", "kh.eighteen", "kh.more",
    "summary",
]

MISCONCEPTIONS = [
    ("M_TT_COLUMN", "Ten thousand is written in the Thousands column as 10 Th, not in a new column to the left."),
    ("M_COMMA_PLACE", "A comma is placed after every three digits counting from the left, so 10,000 is written 100,00."),
    ("M_ZERO_NAME", "A zero in a number is dropped when it is read, so 10,010 is read as ten thousand one ten."),
    ("M_FIRST_DIGIT", "The number with the bigger first digit is the bigger number, whatever the number of digits."),
    ("M_ROUND_UP", "Rounding always goes up, so 2,346 rounds to 2,400 as its nearest hundred."),
    ("M_HALFWAY", "A number halfway between two tens rounds down."),
    ("M_CORNER_TWICE", "A horse at a corner of the stable is counted only once when counting each side."),
    ("M_DIGIT_DIFF", "The difference of the two-digit numbers can be any number, not always a multiple of 9."),
    ("M_ZERO_HOLDER", "A number such as 8,062 has no hundreds, so its expanded form has no place for them."),
]

SOLUTION_NOTES = [
    "Let Us Do 2 table (names and numbers): 7,209 Seven thousand two hundred nine; 10,599 Ten thousand five hundred "
    "ninety-nine; 10,743; 13,579 Thirteen thousand five hundred seventy-nine; 10,010; 56,491; 45,045 Forty-five thousand "
    "forty-five; 39,593 Thirty-nine thousand five hundred ninety-three; 50,005 Fifty thousand five; 26,050 Twenty-six "
    "thousand fifty; 81,200 Eighty-one thousand two hundred; 90,009; 23,230; 36,001.",
    "Number line questions (Let Us Do 3 and 4) are read from the printed lines 0 to 80,000 and 5,000 to 50,000; the plan "
    "gives the order and the digits, and the position is a described estimate.",
    "Open prompts (vehicles in your state, things counted in the classroom, tree and village) have no single answer; the "
    "plan gives one reasoned sample answer.",
    "Mira's puzzle: the difference of a two-digit number and the number with its digits swapped is 9 times the "
    "difference of the digits, so every difference is a multiple of 9 and the process ends at 9.",
    "King's Horses: a horse at a corner is counted on two sides, so 20 counted horses on 4 sides means 20 minus the "
    "number of corner horses. 19 horses need 1 corner horse, 18 need 2, 17 need 3, 16 need 4. The thief can steal 2 more "
    "from 18 before the count of 5 on every side is impossible.",
]
ERRATA = []

DESIGN_REFERENCES = [
    {"text": "docs/25_new_design_learning_plan_playbook.md: framing intro, idea topics each ending in a practice "
             "concept, a question topic after each idea topic with exercises, and one summary topic.", "url": ""},
]

FIGURES = {}
