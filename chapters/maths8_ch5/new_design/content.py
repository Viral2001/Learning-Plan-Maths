# -*- coding: utf-8 -*-
"""Chapter-level content for Class 8 Chapter 5, Number Play (Ganita Prakash Grade 8 Part I, Chapter 5, book pp 112
to 135). Book lines elsewhere are verbatim except: the book's dashes become commas, colons or "to"; minus is U+2212;
x2 and 5133 in the book's flattened print are written x² and 513³."""
from __future__ import annotations

CHAPTER = {
    "grade": 8,
    "label": "Class 8",
    "chapter_no": 5,
    "name": "Number Play",
    "book_part": "Ganita Prakash Grade 8 Part I, Chapter 5",
    "source_pdf": "textbooks/class8/hegp105.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Is This a Multiple Of?",
     "Sums of consecutive numbers, the parity of signed sums, even and odd expressions, pairs of even numbers that "
     "make multiples of 4, statements about divisibility that are always, sometimes or never true, and numbers "
     "described by their remainders."),
    ("M2", "Checking Divisibility Quickly",
     "Place value explains the shortcuts for 10, 5, 2, 4 and 8; remainders of place values give the shortcuts for "
     "9, 3 and 11; divisibility by 6 and 24 is checked through suitable factors; digital roots show the remainder "
     "on division by 9."),
    ("M3", "Digits in Disguise",
     "Cryptarithms with addition and multiplication are solved by reasoning about digits, carries and sizes, followed "
     "by the chapter summary and the game of Navakankari."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "Number Play is about noticing a pattern and then proving that it must always happen. Each idea starts "
             "with a few numbers to try, a guess about what always happens, and then a reason using algebra, a dot "
             "picture or place value. Examples show a statement is true for those numbers; a single counterexample "
             "shows a claim is false.",
    "points": [
        {"title": "Try, guess, then prove",
         "text": "Students try a pattern on a few numbers first, say what they think always happens, and only then "
                 "write the letter-number or dot-grid reason that makes it certain."},
        {"title": "Always, sometimes or never",
         "text": "Statements about divisibility are sorted by finding a proof (always), an example and a "
                 "counterexample (sometimes), or a reason it can never hold (never)."},
        {"title": "Shortcuts with reasons",
         "text": "Every divisibility shortcut is explained by the remainders that place values leave, so the shortcut "
                 "for 9, 3 or 11 is understood and not just remembered."},
        {"title": "Tools only where handling is the idea",
         "text": "Ten tools, each used once: flipping signs between four numbers, dot grids of even numbers, testing a "
                 "claim, remainder rows, a place-value rule bench, breaking a number into nines and ones, excess and "
                 "shortfall for 11, a two-test trap for combined divisibility, a digital root dial, and a digit puzzle "
                 "solver. The other ideas are taught without a tool because the reasoning itself is the move."},
    ],
}

NCERT_ITEMS = [
    # 5.1 Is This a Multiple Of? (pp 112 to 123)
    "5.1.wonder",
    "5.1.anshu", "5.1.anshu_questions",
    "5.1.signs_list", "5.1.signs_evaluate", "5.1.even_parity", "5.1.any4",
    "5.1.expl1", "5.1.expl1_task", "5.1.expl2", "5.1.expl3", "5.1.limit4",
    "5.1.breaking_numeric", "5.1.breaking_algebra", "5.1.breaking_4m2q", "5.1.breaking_task",
    "5.1.pairs_question", "5.1.pairs_types", "5.1.pairs_cases", "5.1.pairs_task",
    "5.1.asn_s1", "5.1.asn_s2", "5.1.asn_s3", "5.1.asn_s4", "5.1.asn_s5", "5.1.asn_mt67", "5.1.asn_s8",
    "5.1.remains_find", "5.1.remains_5k3", "5.1.remains_other",
    "FiO1.q1", "FiO1.q2", "FiO1.q3", "FiO1.q4", "FiO1.q5", "FiO1.q6", "FiO1.q7", "FiO1.q8",
    # 5.2 Checking Divisibility Quickly (pp 123 to 131)
    "5.2.place_value_10", "5.2.explain_5_2", "5.2.explain_4_8",
    "5.2.nine_intro", "5.2.nine_tens", "5.2.nine_427", "5.2.nine_bigger", "5.2.nine_statements",
    "FiO2.q1", "FiO2.q2", "FiO2.q3", "FiO2.q4",
    "5.2.three",
    "5.2.eleven_table", "5.2.eleven_462", "5.2.eleven_steps", "5.2.eleven_alt", "5.2.eleven_test",
    "5.2.table",
    "5.2.six", "5.2.twentyfour",
    "5.2.dr_def", "5.2.aryabhata", "5.2.dr_range", "5.2.dr_consec", "5.2.dr_multiples", "5.2.dr_riddle",
    "FiO3.q1", "FiO3.q2", "FiO3.q3", "FiO3.q4",
    # 5.3 Digits in Disguise (pp 131 to 134)
    "5.3.rules", "5.3.add_more", "5.3.mult_pq8", "5.3.mult_gh", "5.3.mult_bye", "5.3.solve_six",
    "FiO4.q1", "FiO4.q2", "FiO4.q3", "FiO4.q4", "FiO4.q5", "FiO4.q6", "FiO4.q7", "FiO4.q8",
    "FiO4.q9", "FiO4.q10", "FiO4.q11", "FiO4.q12", "FiO4.q13", "FiO4.q14", "FiO4.q15", "FiO4.q16",
    # Summary and game (pp 134, 135)
    "summary", "navakankari",
]

MISCONCEPTIONS = [
    ("M_EXAMPLES_PROVE", "A pattern that works for a few numbers must work for every number."),
    ("M_CONSEC_ALL", "Every natural number can be written as a sum of consecutive numbers."),
    ("M_SIGN_PARITY", "Changing a plus sign to a minus sign can change an even result into an odd one."),
    ("M_NEG_NOT_EVEN", "Negative numbers such as −2 or −12 are neither even nor odd."),
    ("M_ODD_COEFF", "An expression with an odd number in it, like 13k − 5k, can never be always even."),
    ("M_EVEN_SUM_4", "The sum of two even numbers is always a multiple of 4."),
    ("M_DIV_ADDENDS", "If 8 divides a sum, then 8 must divide each of the two numbers added."),
    ("M_DIV_MULTIPLE", "A number divisible by 7 is also divisible by every multiple of 7."),
    ("M_PRODUCT_RULE", "A number divisible by two numbers is always divisible by their product."),
    ("M_REMAINDER_FORM", "Numbers with remainder 3 on division by 5 are 3k + 5, writing the divisor and remainder "
                         "the wrong way round."),
    ("M_LAST_DIGIT_9", "Divisibility by 9 can be read from the units digit, like divisibility by 2, 5 or 10."),
    ("M_ELEVEN_SUM", "For 11 you add all the digits, the same as for 9."),
    ("M_DIGITAL_ROOT_ZERO", "The digital root of a multiple of 9 is 0."),
    ("M_CRYPT_SAME", "Two different letters in a cryptarithm may stand for the same digit."),
]

SOLUTION_NOTES = [
    "Sums of consecutive numbers here use two or more consecutive natural numbers; with that meaning 1, 2, 4, 8 and "
    "16 (the powers of 2) cannot be written, every other natural number can, and 0 needs negative numbers, for "
    "example −2, −1, 0, 1 and 2.",
    "Four consecutive numbers a, a + 1, a + 2, a + 3 with signs always give the three values 0, −2 and −4 among their "
    "eight results, whichever a is chosen.",
    "Cryptarithm ON + ON + ON = PO has three solutions (17, 24 and 31, giving 51, 72 and 93); L2N × 2 = 2NP has two "
    "(124 × 2 makes 248 and 125 × 2 makes 250); PP × QQ = PRP has three (22, 33 or 44 times 11). The plan shows "
    "every solution.",
    "BYE × 6 = RAY: the only solution is 105 × 6, which makes 630 (B is 1, Y is 0, E is 5, R is 6, A is 3).",
    "Digital roots between 600 and 700 are listed for the numbers strictly between them; 700 itself also has digital "
    "root 7.",
    "Multiples of 36 between 45000 and 47000: 45036, 45072, 45108, 45144 and 45180 (45000 itself is also a multiple).",
]
ERRATA = [
    "Divisibility table: the book's filled row for 128 prints No under 4, but 128 is 4 × 32, so the plan gives Yes.",
    "Shortcut for 11: the steps table works the number 320185 and the sentence after it names 3,28,105. Both numbers "
    "are 3 short of a multiple of 11 (remainder 8), so the conclusion holds for both; the plan works 320185 in the "
    "steps and 328105 in the alternating sign procedure, as the book's two tables do.",
]

DESIGN_REFERENCES = [
    {"text": "docs/25_new_design_learning_plan_playbook.md: framing intro, idea topics each ending in a practice "
             "concept, a question topic after each idea topic with several questions, and one summary topic.",
     "url": ""},
]

FIGURES = {}
