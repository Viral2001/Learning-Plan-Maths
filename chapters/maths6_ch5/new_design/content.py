# -*- coding: utf-8 -*-
"""Chapter-level content for Class 6 Chapter 5, Prime Time (Ganita Prakash Grade 6, Chapter 5).
Book lines elsewhere are verbatim except: the book's dashes become commas, colons or "to"; minus is U+2212;
exponent notation such as 2^6 is written out as a product so the equation checker reads it."""
from __future__ import annotations

import io
import json
import os

CHAPTER = {
    "grade": 6,
    "label": "Class 6",
    "chapter_no": 5,
    "name": "Prime Time",
    "book_part": "Ganita Prakash Grade 6, Chapter 5",
    "source_pdf": "textbooks/class6/fegp105.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Common Multiples and Common Factors",
     "Two games, idli-vada and the treasure jumps, show multiples, common multiples, factors and common factors "
     "of two numbers."),
    ("M2", "Primes and Co-primes",
     "Numbers with exactly two factors are primes. The sieve finds them, and pairs with no common factor other "
     "than 1 are co-prime."),
    ("M3", "Prime Factorisation",
     "Every number above 1 breaks into primes in only one way, and that one factorisation can check whether two "
     "numbers are co-prime or whether one divides the other."),
    ("M4", "Divisibility Tests and Fun with Numbers",
     "The last digits of a number can show whether 10, 5, 2, 4 or 8 divide it. Special numbers, a prime puzzle "
     "and the summary close the chapter."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter follows the book's order. Two games give multiples and factors, primes and co-primes "
             "grow out of the factors, and prime factorisation then replaces guessing with one sure method.",
    "points": [
        {"title": "Games before definitions",
         "text": "Every word, multiple, common multiple, factor, prime, co-prime, comes from the idli-vada game or "
                 "Jumpy's treasure jumps before it gets its name."},
        {"title": "Concept, then practice, topic by topic",
         "text": "Each idea gets its own topic: worked videos for the book's examples, one tool to do it by hand, "
                 "then the book's Figure it Out questions in a practice topic, each with its own video."},
        {"title": "One sure method",
         "text": "Writing a number as a product of primes is unique, so it answers two questions without long "
                 "division: are two numbers co-prime, and does one number divide another."},
        {"title": "Keeko's doubts",
         "text": "Common wrong ideas, such as 'a number ending in 4 can be prime' or 'one factor pair shows every "
                 "factor', are raised by Keeko and fixed with a picture, never just a rule."},
    ],
}

# Every book item in the inventory (page-image read of the chapter), in book order. concept_plan.py checks that
# each one is homed exactly once.
_HERE = os.path.dirname(os.path.abspath(__file__))
with io.open(os.path.join(_HERE, "book_items.json"), encoding="utf-8") as _f:
    NCERT_ITEMS = [_i["id"] for _i in json.load(_f)]

MISCONCEPTIONS = [
    ("M_MULTIPLE_FACTOR", "A factor and a multiple are the same thing, or the multiples of 3 can be smaller than 3."),
    ("M_ONLY_FIRST_COMMON", "There is only one common multiple of two numbers, the first one the game finds."),
    ("M_FACTORS_MISS_ENDS", "The factors of 24 are 2, 3, 4, 6, 8 and 12, so 1 and 24 are not factors."),
    ("M_JUMP_ONE_ALWAYS", "A jump of 1 does not count, so pairs always have a common factor you can use."),
    ("M_ONE_IS_PRIME", "1 is a prime number because only 1 and itself divide it."),
    ("M_ODD_MEANS_PRIME", "Every odd number is prime, or a prime can end in 4."),
    ("M_ALL_EVEN_COMPOSITE", "Every even number is composite, including 2."),
    ("M_SIEVE_MAGIC", "The sieve works by magic, so any circled number could be wrong."),
    ("M_COPRIME_BOTH_PRIME", "Two numbers are co-prime only if each of them is prime."),
    ("M_ONE_PAIR_ENOUGH", "One factor pair of each number shows all their factors, so no shared factor in "
                          "those pairs means co-prime."),
    ("M_TREE_DIFFERENT", "Different factor trees for the same number give different prime factorisations."),
    ("M_ORDER_MATTERS", "3 × 3 × 7 and 3 × 7 × 3 are different factorisations."),
    ("M_STOP_AT_COMPOSITE", "A factorisation is finished once every factor is smaller, even if a composite "
                            "number such as 4 or 9 is still in it."),
    ("M_SHARED_PRIME_DIVIDES", "If two numbers share a prime factor, one of them must divide the other."),
    ("M_LAST_DIGIT_FOR_4", "A number is divisible by 4 if its last digit is 0, 4 or 8, so the last digit alone "
                           "decides divisibility by 4."),
    ("M_LAST_TWO_FOR_8", "The last two digits are enough to test divisibility by 8."),
    ("M_FIVE_ONLY_ENDS_FIVE", "A number is divisible by 5 only when it ends in 5."),
    ("M_ONE_REASON_SPECIAL", "A number in a box is special for only one reason."),
]

SOLUTION_NOTES = [
    "5.1.q3: the blank is filled with 'common multiples', confirmed by the book's own answer to the table question.",
    "5.1.FiO2.Q6: the book lists 7 and 8, and 8 and 9; 7 and 9 also works (first common multiple 63) and is worked "
    "here.",
    "5.1.q8: the official answer says 3 or 5 and adds 1 and 15; the plan gives all four jump sizes.",
    "5.2.FiO.Q5 and Q12: the official answer says 'try other possibilities'; the plan gives several valid examples.",
    "5.5.FiO.Q1 part a: open ended, it depends on the year of birth.",
    "5.6.q1, q2: open ended; the plan checks that every classmate's reason is true for its box.",
]
ERRATA = [
    "5.1.FiO1.Q4: the printed Fig. 5.1 leaves 6 out of the left circle (multiples of 3 up to 30); 6 belongs there.",
    "5.1.q5: the book answers 8 only. With 'idli' for the smaller number, 2 and 4 also give no 'just vada' (every "
    "multiple of 4 is a multiple of 2), so 2 and 8 both work.",
    "5.1.FiO2.Q8: the book answers 'multiples of 3 and multiples of 4', but those would also put 12, 36 and 60 in "
    "the overlap, and the figure shows only 24, 48 and 72. A pair whose first common multiple is 24 and where "
    "neither number divides the other, such as 3 and 8, matches the figure.",
    "5.4.FiO1.Q1: the printed solution gives 729 with five 3s (3 × 3 × 3 × 3 × 3 is 243); 729 has six 3s.",
    "5.4.FiO2.Q1: the printed solution labels the last part 'c' a second time; it is part d.",
    "5.4.FiO2.Q4: the book says yes. Two different primes are co-prime, but a prime with itself, such as 3 and 3, "
    "shares the factor 3, so the plan answers 'yes, for two different primes'.",
    "5.5.FiO.Q2: the printed answers 9999 and 1001 are odd, so not divisible by 4; the correct largest and smallest "
    "are 8888 and 2112.",
    "5.5.FiO.Q5: the book gives 5 and 8; 8 and 10 also work, since 8 covers 2 and 4, and 10 covers 2 and 5.",
]

DESIGN_REFERENCES = [
    {"text": "maths6_ch7 new_design Phase 2 plan: framing intro with one hook, idea topics ending in one doer "
             "tool, a practice topic after each idea topic with one video per book question, one summary topic.",
     "url": ""},
]

FIGURES = {
    "T1.C1": ["A treasure chest with a four-digit code lock, Jumpy and Grumpy beside it."],
    "T2.C1": ["Children in a circle saying numbers, with 'idli' and 'vada' speech bubbles."],
    "T4.C1": ["Figs arranged in rectangles of 12 = 4 rows of 3, and 7 in a single row."],
}
