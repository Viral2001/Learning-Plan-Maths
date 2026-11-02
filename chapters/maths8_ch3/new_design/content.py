# -*- coding: utf-8 -*-
"""Chapter-level content for Class 8 Chapter 3, A Story of Numbers (Ganita Prakash Grade 8 Part I, Chapter 3).
Book lines elsewhere are verbatim except: the book's dashes become commas, colons or "to"; minus is U+2212;
picture numerals (Egyptian, base-5, Mesopotamian, Mayan and rod symbols) are described in words; a value in
another numeral system is linked to its Hindu numeral by "is" or "is written as", never by an equals sign;
superscripts other than 2, 3 and 4 are written "to the power n"."""
from __future__ import annotations

CHAPTER = {
    "grade": 8,
    "label": "Class 8",
    "chapter_no": 3,
    "name": "A Story of Numbers",
    "book_part": "Ganita Prakash Grade 8 Part I, Chapter 3",
    "source_pdf": "textbooks/class8/hegp103.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Counting Before Numerals",
     "Reema's loose page opens the story; counting starts as a one-to-one mapping with sticks, letters, body parts "
     "and tally marks, and the idea of counting in groups appears in the Gumulgal names."),
    ("M2", "Landmarks and Bases",
     "Roman numerals group a number into landmark numbers; the Egyptian system makes every landmark 10 times the "
     "one before, which is the idea of a base, and a base makes adding and multiplying easy."),
    ("M3", "Place Value and Zero",
     "The Mesopotamians let position stand for the landmark number, blanks cause confusion, the Mayan and Chinese "
     "systems add a placeholder or rods, and the Hindu system with 0 as a digit and a number finishes the story."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter is a journey through five ideas: counting in groups, landmark numbers, a base, place value "
             "and zero. Each number system is used, not just looked at: students write numbers in it, add in it and "
             "find where it breaks, so that the next idea arrives as the fix for a real difficulty.",
    "points": [
        {"title": "Use each system before judging it",
         "text": "Every system is met through writing and adding numbers in it, and its weakness is found by trying "
                 "a number it cannot handle."},
        {"title": "Tools only where handling is the idea",
         "text": "Nine tools, each used once: matching sticks to tally marks, building names and Roman numerals, "
                 "reading Egyptian symbols, grouping counters into a base, regrouping on a counting board, a base 60 "
                 "place board, holding an empty place, and sorting number systems by their features."},
        {"title": "Our own symbols for strange numerals",
         "text": "Picture numerals are always read back into Hindu numerals with the grouping written out, so the "
                 "structure is clear even when the symbols are new."},
        {"title": "History as a story, not a list",
         "text": "Reema and her father carry the story; dates and names are context, and the chapter keeps asking "
                 "what problem each new idea solved."},
    ],
}

NCERT_ITEMS = [
    # 3.1 Reema's Curiosity (pp 48 to 50)
    "3.1.reema", "3.1.questions", "3.1.need_count", "3.1.yajurveda", "3.1.bakhshali", "3.1.transmission",
    "3.1.laplace", "3.1.naming", "3.1.digit_evolution",
    # The Mechanism of Counting (pp 51 to 54)
    "3.1.cows_mt", "3.1.sticks", "3.1.sticks_q2q3", "3.1.letters", "3.1.letters_mt", "3.1.symbols_extend",
    "3.1.number_system", "3.1.roman_table1", "3.1.numerals",
    "FiOA.q1", "FiOA.q2", "FiOA.q3",
    # 3.2 Some Early Number Systems (pp 54 to 61)
    "3.2.body_parts", "3.2.tally", "3.2.bones", "3.2.gumulgal", "3.2.gumulgal_mt", "3.2.equivalent_systems",
    "3.2.group_size", "3.2.subitize", "3.2.only_fives_mt",
    "3.2.roman_27", "3.2.roman_L_XL", "3.2.landmarks", "3.2.roman_2367", "FiOB.q1", "3.2.roman_history",
    "3.2.roman_add_a", "3.2.roman_add_b", "3.2.roman_multiply", "3.2.roman_product_big", "3.2.abacus_note",
    "3.2.not_linear",
    "FiOC.q1", "FiOC.q2", "FiOC.q3", "FiOC.q4",
    # 3.3 The Idea of a Base (pp 61 to 70)
    "3.3.egypt_landmarks", "3.3.egypt_symbols", "3.3.egypt_324", "FiOD.q1", "FiOD.q2",
    "3.3.base5_build", "3.3.base5_143", "3.3.base_n_def", "FiOE.q1", "FiOE.q2", "FiOE.q3", "3.3.base_n_landmarks",
    "3.3.egypt_add", "FiOF.q1", "FiOF.q2", "3.3.contrast_roman", "3.3.land_x10", "3.3.land_x100",
    "3.3.land_products", "3.3.reema_board", "3.3.base5_property_mt", "3.3.distributive_x10", "3.3.now_find",
    "3.3.x10_rule", "3.3.base_efficiency",
    "3.3.abacus_3426", "3.3.abacus_add", "3.3.egypt_shortcoming",
    "FiOG.q1", "FiOG.q2", "FiOG.q3",
    # 3.4 Place Value Representation (pp 70 to 80)
    "3.4.base60_why", "3.4.time_units", "3.4.own_symbols", "3.4.meso_640", "3.4.meso_7530", "3.4.meso_regroup",
    "3.4.drop_symbols", "FiOH.q1", "3.4.place_value_def", "3.4.meso_defects", "3.4.blank_ambiguity",
    "3.4.placeholder",
    "3.4.mayan_intro", "3.4.mayan_card", "3.4.mayan_360", "3.4.mayan_try", "3.4.mayan_base20_note",
    "3.4.chinese_rods", "3.4.chinese_2634", "3.4.chinese_blank",
    "3.4.hindu_375", "3.4.hindu_zero_digit", "3.4.zero_number", "3.4.brahmagupta_ring", "3.4.evolution_ideas",
    "3.4.map",
    "FiOI.q1", "FiOI.q2", "FiOI.q3", "FiOI.q4",
    # Summary (p 81)
    "summary",
]

MISCONCEPTIONS = [
    ("M_COUNT_NEEDS_NAMES", "You cannot compare or count collections without number names."),
    ("M_SYSTEM_ENDLESS", "Any way of naming numbers can go on for ever without new symbols."),
    ("M_ROMAN_PLACE", "In Roman numerals the position of a symbol decides its value, like in our numerals."),
    ("M_ROMAN_ADD_DIGITS", "Roman numerals are added by joining the strings, with no regrouping."),
    ("M_LANDMARK_PRODUCT", "The product of two landmark numbers is always another landmark number, in any system."),
    ("M_BASE_TEN_ONLY", "Grouping in tens is the only way to build a number system."),
    ("M_TEN_SYMBOLS_OK", "A symbol may appear 10 or more times in an Egyptian numeral."),
    ("M_POSITION_SAME", "A symbol means the same amount wherever it is written."),
    ("M_BLANK_NOTHING", "A blank space between symbols does not change the number, so it can be left out."),
    ("M_ZERO_NOTHING", "Zero means nothing, so it is not a real number and can be dropped from a numeral."),
    ("M_ARABIC_ORIGIN", "Our numerals were invented by the Arabs, as the name Arabic numerals suggests."),
    ("M_LINEAR_HISTORY", "Each number system was invented as an improvement of the one before it."),
]

SOLUTION_NOTES = [
    "Roman numerals: 1222 is MCCXXII, 2999 is MMCMXCIX, 302 is CCCII, 715 is DCCXV; the book's sums are "
    "CCXXXII + CCCCXIII giving DCXLV (232 + 413 = 645) and LXXXVII + LXXVIII giving CLXV (87 + 78 = 165).",
    "Roman products: V × L is CCL, L × D is 25000 written as 25 M's, V × D is MMD, VII × IX is LXIII; "
    "CCXXXI × MDCCCLII is 231 × 1852 = 427812.",
    "Gumulgal sums: 9 + 7 = 16 (eight ukasar), 9 − 6 = 3 (ukasar-urapon), 9 × 4 = 36 (eighteen ukasar), "
    "16 ÷ 4 = 4 (ukasar-ukasar).",
    "Egyptian symbols: stroke 1, heel 10, coil 100, lotus 1000, finger 10000, tadpole 100000, man 1000000, sun "
    "10000000; the two numerals to read are 276 and 4322.",
    "Base 5 (triangle 1, square 5, hexagon 25, circle 125, wave 625, arrow 3125): 15 is 3 squares, 50 is 2 "
    "hexagons, 137 is 1 circle, 2 squares and 2 triangles, 293 is 2 circles, 1 hexagon, 3 squares and 3 "
    "triangles, 651 is 1 wave, 1 hexagon and 1 triangle; the sum asked is 182 + 412 = 594.",
    "Mesopotamian: 63 is 1|3, 132 is 2|12, 200 is 3|20, 60 is 1|blank, 3605 is 1|blank|5 (digits in base 60).",
    "Mayan (landmarks 1, 20, 360, 7200): 77 is 3|17, 100 is 5|shell, 361 is 1|shell|1, 721 is 2|shell|1.",
    "Base conversion: 25 is 31 in base 8, 100 in base 5 and 11001 in base 2.",
    "Open questions (make your own system, Pacific islanders' many counting sequences, features of the Hindu "
    "system, daily uses of 0) accept any well-reasoned answer.",
]
ERRATA = [
    "Page 59: 2367 is written as MMCCCLXII; the correct Roman numeral is MMCCCLXVII.",
    "Page 62: the step to 125 says 'the previous landmark number (5)'; the previous landmark there is 25.",
    "Page 75 (Mayan card): one line shows (3) × 10 where the ones place holds the shell, which is (0) × 1.",
    "Page 60 answer: L × D is 25000, written as 25 M's; the Roman system has no single symbol for it.",
    "Page 67 answer: 10 to the power 4 times 10 to the power 6 is 10 to the power 10, beyond the largest Egyptian "
    "symbol (10 to the power 7), so it has no Egyptian numeral.",
]

DESIGN_REFERENCES = [
    {"text": "docs/25_new_design_learning_plan_playbook.md: framing intro, idea topics each ending in a practice "
             "concept, a question topic after each idea topic with several questions, and one summary topic.",
     "url": ""},
]

FIGURES = {}
