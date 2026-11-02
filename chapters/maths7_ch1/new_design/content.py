# -*- coding: utf-8 -*-
"""Chapter-level content for Class 7 Chapter 1, Large Numbers Around Us (Ganita Prakash Grade 7 Part I, Chapter 1).
Book lines elsewhere are verbatim except: the book's dashes become commas, colons or "to"; minus is U+2212."""
from __future__ import annotations

CHAPTER = {
    "grade": 7,
    "label": "Class 7",
    "chapter_no": 1,
    "name": "Large Numbers Around Us",
    "book_part": "Ganita Prakash Grade 7 Part I, Chapter 1",
    "source_pdf": "textbooks/class7/gegp101.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "A Lakh and Reading Large Numbers",
     "A question about a lakh varieties of rice leads to building up to one lakh, getting a feel for large numbers by "
     "comparing them with familiar things, and reading and writing numbers in words and numerals."),
    ("M2", "The Land of Tens and Calculators",
     "Calculators with buttons for tens, hundreds and thousands show how the same number is made in many ways, how "
     "the fewest presses match the digits, and how ten lakhs make a crore."),
    ("M3", "Crores and Two Naming Systems",
     "The Indian system with lakh, crore and arab and the international system with million and billion, with commas "
     "placed in each and numbers read in both."),
    ("M4", "Exact and Approximate Values",
     "When an exact number is needed and when rounding up or down is better, the five nearest neighbours of a number, "
     "estimating sums and differences, and reading a table of city populations."),
    ("M5", "Patterns in Products",
     "A shortcut for multiplying by 5 and 25, patterns in products and the number of digits in a product, and facts "
     "hidden in large products and quotients."),
    ("M6", "Did You Ever Wonder, a Puzzle and the Summary",
     "What-if questions tested with stated assumptions, the book's closing questions, a toothpick digit puzzle, and "
     "a closing summary."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter opens with Estu's question about a lakh varieties of rice and keeps it open until the student has "
             "climbed to one lakh and worked out the days in a lifetime. Every story is a video that ends on a question "
             "the student answers before the idea is named, and an interactive tool appears only where handling the "
             "numbers is the idea itself.",
    "points": [
        {"title": "Try first, name later",
         "text": "The hook video leaves Estu's question open. The word lakh is built up from the largest five-digit "
                 "number before anyone is told how big it is, and the answer comes only after the student has "
                 "compared a lifetime of days with one lakh."},
        {"title": "Concept, then practice, topic by topic",
         "text": "Each idea gets its own topic: concept videos, one per concept, a closing practice concept (with a "
                 "tool where handling the numbers is the concept), then the book's Figure it Out questions in their "
                 "own topic, one question and one video per concept."},
        {"title": "Feel the size, then name it",
         "text": "A large number is compared with something familiar: a building, a lifetime, a city. Lakh, crore, arab, "
                 "million and billion are placed on one picture with the zeros counted."},
        {"title": "Estimate, then calculate",
         "text": "Rounding, benchmarks and what-if questions with stated assumptions are used before and after the exact "
                 "calculation, so the student can tell if an answer is reasonable."},
    ],
}

NCERT_ITEMS = [
    "opening", "1.1.lifetime", "1.1.pattern", "1.1.days", "1.1.choose_y", "1.1.FiO_1", "1.1.FiO_2", "1.1.FiO_3",
    "1.1.somu", "1.1.somu_statue", "1.1.somu_waterfall", "1.1.somu_floors", "1.1.lakh_big", "1.1.words_ex",
    "1.1.words_a", "1.1.words_b", "1.1.words_c", "1.1.words_d", "1.1.num_a", "1.1.num_b", "1.1.num_c", "1.1.num_d",
    "1.2.tt_a", "1.2.tt_b", "1.2.tt_c", "1.2.tt_d", "1.2.tt_e", "1.2.tt_f", "1.2.tt_g", "1.2.tens_a", "1.2.tens_b",
    "1.2.tens_c", "1.2.tens_d", "1.2.tens_e", "1.2.tens_f", "1.2.tens_g", "1.2.hh_a", "1.2.hh_b", "1.2.hh_c",
    "1.2.hh_d", "1.2.hh_e", "1.2.hh_f", "1.2.hh_g", "1.2.hh_h", "1.2.hh_i", "1.2.hh_j", "1.2.hh_k",
    "1.2.chitti_5072", "1.2.chitti_a", "1.2.chitti_b", "1.2.chitti_create", "1.2.FiO_chitti", "1.2.sippy_a",
    "1.2.sippy_b", "1.2.crore", "1.2.FiO_sippy1", "1.2.FiO_sippy2", "1.2.FiO_sippy3", "1.3.commas", "1.3.table",
    "1.3.zeros", "1.3.zeros_thousand_lakh", "1.3.zeros_hundred_thousand", "1.3.read_big", "1.3.FiO_1", "1.3.FiO_2",
    "1.3.FiO_3", "1.4.round_updown", "1.4.think_share", "1.4.nn_example", "1.4.nn_a", "1.4.nn_b", "1.4.five_equal",
    "1.4.sum_a", "1.4.sum_b", "1.4.sum_c", "1.4.sum_d", "1.4.diff_a", "1.4.diff_b", "1.4.diff_c", "1.4.diff_d",
    "1.4.table_obs", "1.4.table_title", "1.4.pune", "1.4.most_increase", "1.4.doubled", "1.4.patna_mumbai",
    "1.5.shortcut_roxie", "1.5.shortcut_estu", "1.5.why_five", "1.5.FiO_1", "1.5.FiO_2", "1.5.patterns",
    "1.5.roxie_claim", "1.5.three_by_three", "1.5.four_by_two", "1.5.digit_rule", "1.5.digit_5_5", "1.5.digit_8_3",
    "1.5.digit_12_13", "1.5.fact_songs", "1.5.fact_sun", "1.5.fact_amazon", "1.5.fact_train", "1.5.fact_whale",
    "1.5.fact_plastic", "1.5.fact_soil", "1.6.buses", "1.6.ships", "1.6.moon_year", "1.6.moon_ten", "1.6.sun",
    "1.6.sheets", "1.6.babies", "1.6.coins", "1.6.create", "1.6.FiO_1", "1.6.FiO_2", "1.6.FiO_3", "1.6.FiO_4",
    "1.6.FiO_5", "1.6.FiO_6", "1.6.FiO_7", "1.6.FiO_8", "1.6.FiO_9", "1.6.FiO_10", "1.6.FiO_11", "1.6.FiO_12",
    "1.6.FiO_13", "1.6.FiO_14", "puzzle.tp_count", "puzzle.tp_add", "puzzle.tp_insert", "puzzle.tp_other",
    "puzzle.tp_move", "puzzle.tp_24", "puzzle.tp_24_big", "puzzle.tp_24_small", "puzzle.tp_own", "summary",
]

MISCONCEPTIONS = [
    ("M_LAKH_ZEROS", "A lakh has the wrong number of zeros, or a crore is taken to be a hundred lakh zeros short or long."),
    ("M_LAKH_SMALL", "A lakh is either always a very large number or always a small one, whatever it is compared with."),
    ("M_COMMA_PLACE", "Commas in the Indian system are placed every three digits, as in the international system."),
    ("M_BUTTON_ONE_WAY", "A number can be made by only one combination of button presses."),
    ("M_FEWEST_BIG", "The fewest presses use the biggest buttons as many times as possible, or a button is pressed ten or more times."),
    ("M_COMPARE_UNITS", "Two amounts can be compared by their numbers alone, without changing both to the same unit."),
    ("M_ROUND_PLACE", "A number is rounded by the digit at the place itself, not by the digit just to its right."),
    ("M_ESTIMATE_SIDE", "An estimate by rounding is the same as the exact value, or it tells nothing about whether the value is more or less."),
    ("M_SHORTCUT_ORDER", "Multiplying by 5 means dividing by 5, or the halving and the multiplying by ten can be done in any way with no check."),
    ("M_DIGIT_PRODUCT", "The product of an m-digit and an n-digit number always has exactly m plus n digits."),
    ("M_PRESS_COUNT", "A digit takes as many sticks as its value."),
]

SOLUTION_NOTES = []
ERRATA = []

DESIGN_REFERENCES = [
    {"text": "docs/25_new_design_learning_plan_playbook.md: framing intro, idea topics ending in "
             "a practice concept, a question topic after each idea topic, and one summary topic; the Class 7 "
             "Chapter 10 plan for one video per concept and one question per concept.", "url": ""},
]

FIGURES = {
    "T3.C1": ["A picture of Somu, 1 metre tall, standing beside a building of 10 floors; each floor is about as tall as "
              "four Somus."],
    "T11.C1": ["A table of 20 Indian cities ranked by population in 2011, with a column for 2011 and a column for 2001."],
    "T15.C4": ["For one question, two rows of boxes lined up on the right: 7 boxes on top and 5 boxes below, to be filled "
               "with number cards 1 to 9."],
    "T16.C1": ["Digits drawn as sticks in the style of a calculator display, for example 7 with three sticks."],
    "T16.C2": ["The number 63,890 drawn with sticks, to be rearranged by moving four sticks."],
}
