# -*- coding: utf-8 -*-
"""Chapter-level content for Class 8 Chapter 2, Power Play (Ganita Prakash Grade 8 Part I, Chapter 2).
Book lines elsewhere are verbatim except: the book's dashes become commas, colons or "to"; minus is U+2212;
Indian comma groups in long numbers are written as plain digits so no lakh comma sits next to an equals sign;
superscripts other than 2, 3 and 4 are written "to the power n"."""
from __future__ import annotations

CHAPTER = {
    "grade": 8,
    "label": "Class 8",
    "chapter_no": 2,
    "name": "Power Play",
    "book_part": "Ganita Prakash Grade 8 Part I, Chapter 2",
    "source_pdf": "textbooks/class8/hegp102.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Folding and Growing",
     "A sheet of paper is folded again and again: the thickness doubles with every fold and passes the Moon after "
     "46 folds, the first taste of multiplicative growth."),
    ("M2", "Exponential Notation",
     "Repeated multiplication is written as a power with a base and an exponent, including negative bases, zero, "
     "letters and prime factorisations."),
    ("M3", "Multiplying Powers",
     "Powers of the same base multiply by adding exponents, powers of powers multiply exponents, equal exponents "
     "let bases be multiplied or divided, and counting combinations gives powers."),
    ("M4", "The Other Side of Powers",
     "Dividing powers subtracts exponents, which gives meaning to zero and negative exponents, and power lines show "
     "how powers sit one step apart."),
    ("M5", "Powers of 10",
     "Numbers are expanded with powers of 10 and very large numbers are written in scientific notation, where the "
     "exponent tells the size."),
    ("M6", "Large Numbers Around Us",
     "Guessing, modelling and estimating, linear against exponential growth, populations and times as powers of 10, "
     "historical number names, and a closing summary."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter opens with a fold of paper and keeps asking how big things get when we multiply again and "
             "again. Each rule for exponents is found by writing out the factors and counting them, then used on "
             "numbers too large to write out, and finally on real large numbers from nature and history.",
    "points": [
        {"title": "Count the factors first",
         "text": "Every exponent rule is reached by expanding the powers into factors and counting or cancelling them, "
                 "so the rule is a shortcut for something already seen."},
        {"title": "Tools only where handling is the idea",
         "text": "Ten tools, each used once: folding to double, building a power from factor blocks, joining strips to "
                 "multiply powers, pairing and cancelling factors, counting codes, a staircase of powers down past 1, "
                 "walking a line of powers, a duel to compare powers with a reason, and fixing numbers in standard "
                 "form."},
        {"title": "Guess, then calculate",
         "text": "Every estimation starts with an instinctive guess, then a model, sensible assumptions and a "
                 "calculation, ending with a check of how close the guess was."},
        {"title": "Multiplying against adding",
         "text": "Folding paper, the ladder to the Moon and the time scale keep contrasting multiplicative growth "
                 "with additive growth."},
    ],
}

NCERT_ITEMS = [
    # 2.1 Experiencing the Power Play (pp 19 to 21)
    "2.1.intro", "2.1.table17", "2.1.mt_guess", "2.1.burj_mariana", "2.1.two_folds", "2.1.three_folds",
    "2.1.ten_folds", "2.1.fill_table",
    # 2.2 Exponential Notation and Operations (pp 21 to 27)
    "2.2.fold_power", "2.2.read_powers", "2.2.base_exponent", "2.2.ten_folds_v", "2.2.add_vs_mult", "2.2.neg_base",
    "2.2.neg1_powers", "2.2.neg2_pow4", "2.2.zero_powers", "2.2.letters", "2.2.prime_32400",
    "FiO1.q1", "FiO1.q2", "FiO1.q3",
    "2.2.stones_rooms", "2.2.stones_diamonds", "2.2.why_3p2_3p5", "2.2.p4p6", "2.2.product_law", "2.2.compute_three",
    "2.2.four_pow6", "2.2.seven4_two10", "2.2.power_of_power", "2.2.mt_two_ways",
    "2.2.pond_half", "2.2.pond_exp", "2.2.damayanti", "2.2.order_swap", "2.2.same_exp_law", "2.2.compute_2p5_5p5",
    "2.2.simplify_10p4_5p4", "2.2.quotient_same_exp",
    "2.2.dresses_caps", "2.2.roxie_outfits", "2.2.lock_2digit", "2.2.lock_3digit", "2.2.lock_5digit",
    "2.2.letter_lock", "2.2.try_codes",
    # 2.3 The Other Side of Powers (pp 27 to 30)
    "2.3.halving_line", "2.3.two100_two25", "2.3.quotient_law", "2.3.mt_n_not_zero", "2.3.zero_exponent",
    "2.3.neg_halving", "2.3.reciprocal", "2.3.mt_integers", "2.3.equiv_forms", "2.3.simplify",
    "2.3.power_line4", "2.3.times_larger", "2.3.power_line7",
    # 2.4 Powers of 10 (pp 30 to 32)
    "2.4.expanded", "2.4.write_three", "2.4.decimal", "2.4.facts", "2.4.5900", "2.4.write_facts", "2.4.sci_form",
    "2.4.mumbai_kohima", "2.4.comic", "2.4.distances", "2.4.mark_earth", "2.4.standard_form",
    # 2.5 Did You Ever Wonder? (pp 33 to 42)
    "2.5.tulabhara", "2.5.coins_weight", "2.5.coins_notes", "2.5.mt_donations", "2.5.padayatra",
    "2.5.circumnavigate", "2.5.ladder", "2.5.linear_exp_examples",
    "2.5.lakh_crore_arab", "2.5.species", "2.5.starling_mosquito", "2.5.per_elephant", "2.5.calc_four",
    "2.5.age_hours", "2.5.age_puzzle", "2.5.estu_birth", "2.5.million_seconds",
    "2.5.time_table", "2.5.events_order", "2.5.terror_plants", "2.5.try_stars_water",
    # 2.5 (second) A Pinch of History (pp 42, 43)
    "hist.lalitavistara", "hist.indian_names", "hist.western_names", "hist.googol_notes", "hist.first_part",
    # Figure it Out (pp 44, 45)
    "FiO2.q1", "FiO2.q2", "FiO2.q3", "FiO2.q4", "FiO2.q5", "FiO2.q6", "FiO2.q7", "FiO2.q8", "FiO2.q9",
    "FiO2.q10", "FiO2.q11", "FiO2.q12", "FiO2.q13", "FiO2.q14",
    # Summary (p 46) and the Tremendous in Ten game (p 47)
    "summary", "tremendous_ten",
]

MISCONCEPTIONS = [
    ("M_POW_TIMES", "A power is the base times the exponent, so 2 to the power 5 is 10."),
    ("M_NEG_BASE", "A power of a negative number is always negative."),
    ("M_ADD_EXP_MULT", "To multiply powers of the same base, multiply the exponents."),
    ("M_POWPOW_ADD", "A power of a power adds the exponents, so (4³)² is 4 to the power 5."),
    ("M_DIV_EXP", "To divide powers of the same base, divide the exponents."),
    ("M_ZERO_POW", "Any number to the power 0 is 0."),
    ("M_NEG_EXP_NEG", "A negative exponent makes the value negative."),
    ("M_BIGGER_BASE", "The power with the bigger base is always the bigger number."),
    ("M_SCI_COEFF", "In scientific notation the number with the bigger coefficient is bigger, whatever the exponents."),
    ("M_POW_COUNT", "Large numbers can be compared or estimated by their first digits, without counting the zeroes."),
    ("M_LINEAR_EXP", "Repeated doubling grows by adding the same amount each time, so it stays small."),
    ("M_HALF_DAY", "If a doubling pond is full on day 30, it was half full on day 15."),
    ("M_COMB_ADD", "To count combinations of choices, add the numbers of choices."),
]

SOLUTION_NOTES = [
    "Folding: the thickness after n folds is 0.001 × 2 to the power n cm; fold 45 is about 351844 km and fold 46 "
    "about 703687 km, so the 46th fold passes the Moon at 384400 km.",
    "Estu's 4070 days: 11 years and 55 days of 365 days, less about 3 leap days, so about 11 years and 52 days.",
    "Roxie's 6970710: in minutes 4840 days is 6969600, so the number is her age in minutes, a few hours into day 4841.",
    "Figure it Out question 12: (v) 2 × 10 to the power 9 is the same number as (vi) 10 to the power 9 + 10 to the "
    "power 9; both are correct, though the book's answer lists only (vi).",
    "Coins, walking and estimation answers depend on stated assumptions (a 4 g coin, 25 km a day, 5 km an hour); "
    "other sensible assumptions give other reasonable answers.",
]
ERRATA = [
    "Page 26: the list of 3-digit passwords reads 997, 997, 999; it should read 997, 998, 999.",
    "Page 45, question 12: the first option is labelled (ii) instead of (i).",
    "Two sections are numbered 2.5 (Did You Ever Wonder? and A Pinch of History); history items use the hist. prefix.",
]

DESIGN_REFERENCES = [
    {"text": "docs/25_new_design_learning_plan_playbook.md: framing intro, idea topics each ending in a practice "
             "concept, a question topic after each idea topic with several questions, and one summary topic.",
     "url": ""},
]

FIGURES = {}
