# -*- coding: utf-8 -*-
"""Chapter-level content for Class 7 Chapter 11, Finding Common Ground (Ganita Prakash Grade 7 Part II, Chapter 3).
Book lines elsewhere are verbatim except: the book's dashes become commas, colons or "to"; minus is U+2212."""
from __future__ import annotations

CHAPTER = {
    "grade": 7,
    "label": "Class 7",
    "chapter_no": 11,
    "name": "Finding Common Ground",
    "book_part": "Ganita Prakash Grade 7 Part II, Chapter 3",
    "source_pdf": "textbooks/class7/gegp203.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "The Greatest of All: Common Factors and HCF",
     "Tiles, rice bags and treasure jumps lead to the Highest Common Factor. Prime factorisation then gives a "
     "faster, more reliable way to list factors and to find the HCF."),
    ("M2", "Least, but not Last: Common Multiples and LCM",
     "Torans, a sweet shop and the idli-vada game lead to the Lowest Common Multiple. Prime factorisation again "
     "gives a quick method, this time taking the most occurrences of each prime."),
    ("M3", "Patterns, Properties and a Pretty Procedure",
     "General statements about HCF and LCM, the common division method that gives both at once, the relation "
     "HCF × LCM = product, and application problems that call for one or the other."),
    ("M4", "Review and Summary",
     "One practice tool for the whole chapter, a closing summary, and a colour puzzle to decode."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter follows the book's own order: a tile problem opens the idea of a greatest common factor, "
             "prime factorisation makes it quick, and the same two moves, list then compress, repeat for the "
             "lowest common multiple. Every story is a video that ends on a question the student answers before the idea is named, and "
             "an interactive tool appears only where handling the numbers is the idea itself.",
    "points": [
        {"title": "Try first, name later",
         "text": "The hook video leaves Sameeksha's tile question open. The word HCF arrives only after the student "
                 "has worked out which tiles fit and felt why the largest tile uses the fewest."},
        {"title": "Concept, then practice, topic by topic",
         "text": "Each idea gets its own topic: story or concept videos, one per concept, a closing practice concept "
                 "(with a tool on the ten topics where the manipulation is the concept), then the book's Figure it "
                 "Out questions in their own topic, one question and one video per concept."},
        {"title": "Minimum for HCF, maximum for LCM",
         "text": "The chapter keeps one picture throughout: every factor is a subpart of the prime factorisation, "
                 "so the HCF takes the fewest copies of each shared prime and the LCM takes the most copies of "
                 "every prime."},
        {"title": "Generalise and explain",
         "text": "Patterns for consecutive, even, odd and co-prime pairs, the doubling rule and HCF × LCM = "
                 "product are found from examples, stated as general statements, then explained from the primes."},
    ],
}

NCERT_ITEMS = [
    "opening",
    # 3.1
    "3.1.tile", "3.1.tile_largest", "3.1.tile_count", "3.1.tile_fraction", "3.1.hcf_def",
    "3.1.rice",
    "3.1.jump_a", "3.1.jump_b", "3.1.jump_c", "3.1.jump_d", "3.1.jump_hcf",
    "3.1.primes", "3.1.pf_90", "3.1.pf_prime", "3.1.pf_trees", "3.1.pf_division",
    "3.1.f840", "3.1.f225", "3.1.FiO_factors", "3.1.anshu_claim",
    "3.1.ex1", "3.1.ex2", "3.1.ex3", "3.1.FiO_common",
    "3.1.ex4", "3.1.ex5", "3.1.more_than_two", "3.1.FiO_hcf1", "3.1.FiO_hcf2",
    # 3.2
    "3.2.toran", "3.2.toran_largest", "3.2.lcm_def", "3.2.sweet",
    "3.2.idli_a", "3.2.idli_b", "3.2.idli_c", "3.2.idli_d", "3.2.idli_lcm",
    "3.2.lcm_intro", "3.2.ex6", "3.2.ex7", "3.2.FiO_lcm",
    # 3.3
    "3.3.pattern_hcf", "3.3.pattern_algebra", "3.3.FiO1", "3.3.FiO2", "3.3.FiO3",
    "3.3.double", "3.3.multiples14", "3.3.common_mult",
    "3.3.div_explore", "3.3.div_hcf", "3.3.div_lcm", "3.3.guna_anshu", "3.3.try_pairs",
    "3.3.lcm_vs_product", "3.3.hcf_lcm_105_95", "3.3.hcf_lcm_try", "3.3.hcf_lcm_why", "3.3.three_numbers",
    "3.3.end1", "3.3.end2", "3.3.end3", "3.3.end4", "3.3.end5", "3.3.end6", "3.3.end7",
    "3.3.end8", "3.3.end9", "3.3.end10", "3.3.end11", "3.3.end12", "3.3.end13",
    "puzzle.colours", "summary",
]

MISCONCEPTIONS = [
    ("M_HCF_BIG", "The HCF is the bigger of the two numbers, or the biggest number that divides either one."),
    ("M_COMMON_ONLY", "A common factor must divide only one of the numbers, so factors of just one number get listed."),
    ("M_LCM_PRODUCT", "The LCM of two numbers is always their product."),
    ("M_LCM_BIG", "There is a largest common multiple, as there is a greatest common factor."),
    ("M_PRIME_ONE", "1 is a prime number, or an odd number is always prime."),
    ("M_LONGER_BIGGER", "A larger number always has a longer prime factorisation."),
    ("M_MIN_MAX", "HCF takes the maximum count of each prime, or LCM takes the minimum count."),
    ("M_COMMON_PRIMES_ONLY", "The LCM contains only the primes the two numbers share."),
    ("M_COPRIME_ONE_FACTOR", "Two numbers whose factorisations look different, such as 6 × 12 and 8 × 18, have no common factor."),
    ("M_ORDER", "A different order of prime factors, or a different factor tree, gives a different prime factorisation."),
    ("M_FACTOR_MULTIPLE", "Factor and multiple mean the same thing, so a factor can be larger than the number."),
    ("M_PROCEDURE", "In the division method the answer is the last row, not the product of the divisors."),
]

SOLUTION_NOTES = []
ERRATA = []

DESIGN_REFERENCES = [
    {"text": "docs/25_new_design_learning_plan_playbook.md: framing intro, idea topics ending in "
             "a practice concept, a question topic after each idea topic, and one summary topic; the Class 7 "
             "Chapter 10 plan for one video per concept and one question per concept.", "url": ""},
]

FIGURES = {
    "T1.C1": ["A rectangular room 12 ft by 16 ft drawn from above, partly covered with square floor tiles."],
    "T2.C1": ["The 12 by 16 room split into 4 ft squares: 3 rows of 4 tiles."],
}
