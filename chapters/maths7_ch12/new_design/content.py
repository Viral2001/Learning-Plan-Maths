# -*- coding: utf-8 -*-
"""Chapter-level content for Class 7 Chapter 12, Another Peek Beyond the Point (Ganita Prakash Grade 7 Part II,
Chapter 4). Book lines elsewhere are verbatim except: the book's dashes become commas, colons or "to"; minus is
U+2212; Indian digit grouping (3,65,240) is written without commas so every equation can be checked."""
from __future__ import annotations

CHAPTER = {
    "grade": 7,
    "label": "Class 7",
    "chapter_no": 12,
    "name": "Another Peek Beyond the Point",
    "book_part": "Ganita Prakash Grade 7 Part II, Chapter 4",
    "source_pdf": "textbooks/class7/gegp204.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Multiplying Decimals",
     "A quick recap of decimals as tenths, hundredths and thousandths, then multiplication of decimals by turning "
     "them into fractions, the rule that counts digits after the decimal point, and when a product is smaller than "
     "the numbers multiplied."),
    ("M2", "Dividing Decimals",
     "Dividing by 10, 100 and 1000, sharing into decimal parts with equivalent fractions, long division that keeps "
     "going past the Ones, dividing by a decimal, divisions that never end, and how the quotient compares with the "
     "dividend."),
    ("M3", "Decimals at Work",
     "Leap years from the decimal 365.2422, then everyday problems and reasoning questions with decimal products "
     "and quotients."),
    ("M4", "Puzzle and Summary",
     "A Hidato number path puzzle and a closing summary of the chapter."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter follows the book's own order: multiplication first, then division, then the calendar "
             "story and a set of mixed problems. Every rule is reached from fractions the student already knows, "
             "so a decimal rule is never a trick to remember but a short cut for a fraction calculation.",
    "points": [
        {"title": "Try first, name later",
         "text": "The hook video leaves Arshad's pen bill open. The fraction method and the digit-counting rule "
                 "arrive only after the student has tried to multiply a decimal on their own."},
        {"title": "Fractions underneath every rule",
         "text": "A decimal is a fraction with denominator 10, 100 or 1000. Multiplying decimals multiplies those "
                 "fractions, and dividing by a decimal multiplies by its reciprocal, so both rules are explained "
                 "rather than told."},
        {"title": "Place value carries division past the Ones",
         "text": "Long division regroups Ones into Tenths, Tenths into Hundredths and so on. The decimal point in "
                 "the quotient appears at the moment Ones are regrouped into Tenths."},
        {"title": "Concept, then practice, topic by topic",
         "text": "Each idea gets its own topic with one video per concept and a practice concept at the end; "
                 "interactive tools appear only where handling the numbers is the idea. The book's questions "
                 "follow in their own topic, one question and one video per concept."},
    ],
}

NCERT_ITEMS = [
    "opening",
    # 4.1 A quick recap of decimals
    "4.1.place_value", "4.1.game", "4.1.spices", "4.1.expand_table", "4.1.div_rule",
    # 4.2 Decimal multiplication
    "4.2.ex1", "4.2.ex2", "4.2.natural", "4.2.ex3", "4.2.ex4", "4.2.digits_table", "4.2.known_product",
    "4.2.rule", "4.2.ex5", "4.2.size_three", "4.2.situations",
    "4.2.FiO1", "4.2.FiO2", "4.2.FiO3", "4.2.FiO4", "4.2.FiO5", "4.2.FiO6", "4.2.FiO7", "4.2.FiO8",
    "4.2.FiO9", "4.2.FiO10",
    # 4.3 Decimal division
    "4.3.ex6", "4.3.ribbon_units", "4.3.div_rule", "4.3.div_table",
    "4.3.ex7", "4.3.ex7_four", "4.3.ten_thirds", "4.3.two_five",
    "4.3.ex8", "4.3.ex8_1325", "4.3.ex9", "4.3.ex10", "4.3.ex11",
    "4.3.FiOA1", "4.3.FiOA2", "4.3.FiOA3", "4.3.FiOA4",
    "4.3.ex12", "4.3.ex13", "4.3.ex13_b",
    "4.3.never_10_3", "4.3.never_more", "4.3.one_seventh", "4.3.magic", "4.3.seventeenth", "4.3.artin",
    "4.3.ddq", "4.3.ddq_table",
    "4.3.FiOB1", "4.3.FiOB2", "4.3.FiOB3", "4.3.FiOB4", "4.3.FiOB5", "4.3.FiOB6", "4.3.FiOB7", "4.3.FiOB8",
    "4.3.FiOB9", "4.3.FiOB10",
    # 4.4 Look before you leap
    "4.4.year", "4.4.four_years", "4.4.hundred_years", "4.4.no_100th", "4.4.thousand", "4.4.rule_400",
    "4.4.try_10000", "4.4.how_measured", "4.4.try_calendars",
    "4.4.end1", "4.4.end2", "4.4.end3", "4.4.end4", "4.4.end5", "4.4.end6", "4.4.end7", "4.4.end8",
    "4.4.end9", "4.4.end10", "4.4.end11",
    "puzzle.hidato", "summary",
]

MISCONCEPTIONS = [
    ("M_POINT_ALIGN", "When multiplying decimals the decimal point is lined up as in addition, or the product keeps "
                      "the decimal places of only one of the numbers."),
    ("M_PRODUCT_BIGGER", "Multiplication always makes a number bigger, so a product is always greater than both "
                         "numbers multiplied."),
    ("M_QUOTIENT_SMALLER", "Division always makes a number smaller, so a quotient is always less than the dividend."),
    ("M_TRAILING_ZERO", "Dropping or adding zeroes at the end of a decimal (56.50 and 56.5) changes its value."),
    ("M_POINT_WRONG_WAY", "Dividing by 10, 100 or 1000 moves the decimal point to the right, or by the wrong number of "
                          "places."),
    ("M_REMAINDER_STOP", "Long division must stop at the Ones, leaving a remainder, instead of regrouping Ones into "
                         "Tenths."),
    ("M_POINT_IN_QUOTIENT", "The decimal point in the quotient is placed at the end, or not at the moment Ones are "
                            "regrouped into Tenths."),
    ("M_DIVISOR_ONLY", "When the divisor is a decimal, only the divisor is multiplied by 10 or 100, and the dividend "
                       "is left as it is."),
    ("M_EVERY_DIVISION_ENDS", "Every division of whole numbers ends after a few decimal places."),
    ("M_MISSING_ZERO", "A zero place holder is left out, so 0.06 ÷ 5 is written as 0.12 instead of 0.012."),
    ("M_UNIT_MIX", "Quantities in different units (metres and centimetres, grams and kilograms) are combined "
                   "without converting first."),
]

SOLUTION_NOTES = [
    "Leap years: the book states once that the Earth goes round the Sun in 'exactly 364.2422 days'; every "
    "calculation in the book uses 365.2422, which is the value taught here.",
    "Figure it Out (decimal division) Q2(b): options (i) and (iv) are both printed as 4458.75; the correct choice "
    "is (iii) 445.875 either way.",
    "End of chapter Figure it Out Q8: parts (b) and (f) are the same division, 7.56 ÷ 0.36; both give 21.",
    "Hidato solution: the printed solution grid shows 39 in the fourth row (should be 29) and 16 in the seventh "
    "row (should be 6); the corrected path is taught.",
    "Hidato: the three practice grids are given without solutions in the book. Grids 1 (1 to 25) and 3 (1 to 56) "
    "were checked with a solver and each has exactly one solution, which the plan gives. Grid 2 has only 37 cells "
    "for a path from 1 to 39, so it cannot be completed as printed; the plan says so.",
    "End of chapter Figure it Out Q2: the two arrow number lines are recovered from the figure: 3.1 to 3.2 and 2.15 "
    "to 2.17, each split into 10 equal parts, with the arrow at the 6th mark (3.16 and 2.162).",
]
ERRATA = []

DESIGN_REFERENCES = [
    {"text": "docs/25_new_design_learning_plan_playbook.md: framing intro, idea topics ending in "
             "a practice concept, a question topic after each idea topic, and one summary topic; the Class 7 "
             "Chapter 10 plan for one video per concept and one question per concept.", "url": ""},
]

FIGURES = {
    "T1.C1": ["A stationery shop counter with a row of pens, each pen priced at nine rupees fifty paisa."],
    "T3.C3": ["A rectangle 5.7 cm by 13.3 cm, sides labelled."],
    "T8.C1": ["Place value blocks for 1325 shared into 4 equal groups: Hundreds, Tens, Ones, then Tenths and "
              "Hundredths after regrouping."],
    "T10.C2": ["The remainder chain for 1 ÷ 7: 1, 3, 2, 6, 4, 5 and back to 1."],
    "T12.C2": ["The leap year flow chart: is the year divisible by 4? Yes gives 366 days, no gives 365 days."],
    "T15.C1": ["The Hidato puzzle grid with 1 and 40 given and the path of consecutive numbers."],
}

# Hook slot extras (build.py passes these into the hook's worklist slot).
HOOK_HANDOVER = ("Try it: write down what Arshad pays for 5 pens at ₹9.5 each, and how you worked it out, "
                 "before the next topic.")
HOOK_NOTE = ("The hook leaves Arshad's bill open. Do not confirm any total; the fraction method in the "
             "multiplication topic settles it.")

# Words the narration may need that are hard for a Class 7 reader; the script author defines or avoids them.
HARD_WORDS = ["multiplicand", "multiplier", "reciprocal", "regroup", "conjecture", "revolution", "cyclic",
              "overcompensated", "equivalent", "dividend", "divisor"]
