# -*- coding: utf-8 -*-
"""Chapter-level content for Class 7 Chapter 8, Working with Fractions (Ganita Prakash Grade 7 Part I,
Chapter 8). Book lines elsewhere are verbatim except: the book's dashes become commas, colons or "to"; minus is
U+2212; fractions are written a/b and mixed numbers as "2 1/2"."""
from __future__ import annotations

CHAPTER = {
    "grade": 7,
    "label": "Class 7",
    "chapter_no": 8,
    "name": "Working with Fractions",
    "book_part": "Ganita Prakash Grade 7 Part I, Chapter 8",
    "source_pdf": "textbooks/class7/gegp108.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Multiplying Fractions",
     "Multiplying a fraction and a whole number as repeated addition and as dividing by the denominator then "
     "multiplying by the numerator, multiplying two fractions with a unit square, Brahmagupta's rule for "
     "numerators and denominators, cancelling common factors, and when a product is smaller than the numbers "
     "multiplied."),
    ("M2", "Dividing Fractions",
     "Division restated as a multiplication, the reciprocal, Brahmagupta's rule for dividing fractions, and how "
     "the quotient compares with the dividend."),
    ("M3", "Fractions at Work",
     "Everyday and ancient problems with fractions, fractions of fractions in a square, and the story of a "
     "dramma and a cowrie shell."),
    ("M4", "Puzzle and Summary",
     "A chess puzzle about non-attacking queens and a closing summary of the chapter."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter follows the book's own order: multiplication of fractions, division of fractions, and then "
             "problems that use both. Every rule is reached from a picture or a question about distance, area or "
             "sharing, so a rule is never a trick to remember but a short way of doing something the student "
             "already understands.",
    "points": [
        {"title": "Try first, name later",
         "text": "The hook video leaves Aaron's tortoise on the road. The student first meets the idea that a "
                 "journey can last a fraction of an hour, and the rules arrive after the question has been felt."},
        {"title": "A unit square behind every product",
         "text": "A fraction of a fraction is first cut out of a unit square. Counting the rows and columns gives "
                 "the denominator and the shaded parts give the numerator, so Brahmagupta's rule is seen before "
                 "it is stated."},
        {"title": "Division is multiplication turned round",
         "text": "Dividing is asking which number multiplied by the divisor gives the dividend. That question "
                 "leads to the reciprocal and to the rule of multiplying by it."},
        {"title": "Concept, then practice, topic by topic",
         "text": "Each idea gets its own topic with one video per concept and a practice concept at the end; "
                 "interactive tools appear only where handling the numbers is the idea. The book's questions "
                 "follow in their own topic, one question and one video per concept."},
    ],
}

NCERT_ITEMS = [
    "opening",
    # 8.1 Multiplication of fractions
    "8.1.aaron", "8.1.tortoise3", "8.1.fifth", "8.1.two_fifths", "8.1.rule_whole",
    "8.1.ex1", "8.1.ex2",
    "8.1.FiOA1", "8.1.FiOA2", "8.1.FiOA3", "8.1.FiOA4", "8.1.FiOA5",
    "8.1.half_quarter", "8.1.three_fourths_two_fifths", "8.1.mathtalk_54_32", "8.1.area_link",
    "8.1.FiOB1",
    "8.1.unit_rule", "8.1.five_twelfths", "8.1.brahmagupta_mult", "8.1.whole_as_fraction",
    "8.1.FiOB2",
    "8.1.cancel1", "8.1.cancel2", "8.1.history_apavartana",
    "8.1.FiOC1", "8.1.FiOC2", "8.1.FiOC3", "8.1.FiOC4", "8.1.FiOC5",
    "8.1.size_sit1", "8.1.size_sit2", "8.1.size_sit3", "8.1.size_conclude", "8.1.order",
    # 8.2 Division of fractions
    "8.2.twelve_by_four", "8.2.one_by_twothirds", "8.2.three_by_twothirds", "8.2.fifth_by_half",
    "8.2.twothirds_by_threefifths", "8.2.rule_reciprocal", "8.2.brahmagupta_div",
    "8.2.sizes", "8.2.sizes_talk",
    # 8.3 Some problems involving fractions
    "8.3.ex3", "8.3.ex4", "8.3.ex5",
    "8.3.fig84", "8.3.practice_a", "8.3.practice_b",
    "8.3.dramma", "8.3.coins", "8.3.history_final",
    "8.3.FiOD1", "8.3.FiOD2", "8.3.FiOD3", "8.3.FiOD4", "8.3.FiOD5", "8.3.FiOD6", "8.3.FiOD7", "8.3.FiOD8",
    "8.3.FiOD9", "8.3.FiOD10", "8.3.FiOD11", "8.3.FiOD12",
    "puzzle.queens", "summary",
]

MISCONCEPTIONS = [
    ("M_MULT_BIGGER", "Multiplication always makes a number bigger, so a product is always greater than both "
                      "numbers multiplied."),
    ("M_DIV_SMALLER", "Division always makes a number smaller, so a quotient is always less than the dividend."),
    ("M_ADD_ACROSS", "Two fractions are multiplied by adding the numerators and the denominators, or by "
                     "multiplying only the numerators."),
    ("M_WHOLE_ONLY_TOP", "A whole number multiplied by a fraction is multiplied into the numerator and the "
                         "denominator both, or into the denominator."),
    ("M_CANCEL_SAME_FRACTION", "Common factors can be cancelled only inside one fraction, never between the "
                               "numerator of one fraction and the denominator of the other."),
    ("M_FLIP_DIVIDEND", "In a division of fractions the dividend is turned upside down instead of the divisor."),
    ("M_FLIP_BOTH", "Both fractions are turned upside down when dividing."),
    ("M_WRONG_OPERATION", "A word problem is multiplied when it should be divided, or the other way round."),
    ("M_FRACTION_OF_WHOLE", "A fraction of a part is taken as a fraction of the whole, so the part is not shrunk."),
    ("M_MIXED_PARTS", "A mixed number is multiplied by multiplying the whole part and the fraction part apart."),
    ("M_UNIT_MIX", "Quantities in different units (grams and kilograms) are compared without converting first."),
]

SOLUTION_NOTES = [
    "Figure it Out (multiplying two fractions) first set: the last part, 1/12 x 1/18 = 1/216, is the lead-in to "
    "the rule for unit fractions; it is solved with the rows and columns of the unit square.",
    "Figure it Out (problems with fractions) Q4 of the Moon: the answer is a clock time; the plan teaches it as "
    "2 1/2 hours after 10 pm, which is 12:30 am on Thursday.",
    "A Pinch of History: the apavartana box dates Umasvati to c. 150 CE, but the closing history box says 150 BCE. "
    "The plan quotes neither date for Umasvati and says only that he was a Jaina scholar.",
    "The text working out 5/12 x 7/18 prints one factor as 7/8 in the step line; the plan teaches the correct "
    "7/18, which gives 35/216.",
    "Figure it Out (multiplying fractions) Q3: 3 3/4 x 9 3/5 = 15/4 x 48/5 = 36 square feet.",
    "Figure it Out (problems with fractions) Q10 and Q11 are figure questions. Q10 is described in words (a "
    "square cut into four equal quadrants, one quadrant divided by a V-shaped fold into a half and then a "
    "three-quarter part) and solved as 1/4 x 1/2 x 3/4 = 3/32. Q11 is the ant-splitting figure, solved as 29/32 "
    "for the mango tree and 3/32 for the sugarcane field.",
    "The two in-text practice squares (a) and (b) are described in words; they give 3/8 and 1/16.",
]
ERRATA = []

DESIGN_REFERENCES = [
    {"text": "docs/25_new_design_learning_plan_playbook.md: framing intro, idea topics ending in "
             "a practice concept, a question topic after each idea topic, and one summary topic; the Class 7 "
             "Chapter 10 plan for one video per concept and one question per concept.", "url": ""},
]

FIGURES = {
    "T3.C1": ["A unit square with a quarter shaded, then that quarter cut into two equal parts, one part shaded: "
              "one eighth of the whole."],
    "T3.C2": ["A unit square with 5 rows and 4 columns; two of the 20 small parts shaded for one quarter of two fifths."],
    "T3.C3": ["A unit square showing one and a half, cut into 2 rows and 4 columns, with 3 parts shaded: 3/8."],
    "T10.C1": ["A square with a red top-right quarter, a yellow triangle inside it that is half of the quarter, "
               "and three quarters of the triangle shaded."],
}

# Hook slot extras (build.py passes these into the hook's worklist slot).
HOOK_HANDOVER = ("Try it: Aaron's tortoise walks 1/4 km in 1 hour. Write down how far you think it walks in half an "
                 "hour, and why, before the next topic.")
HOOK_NOTE = ("The hook leaves the tortoise's half hour open. Do not confirm any distance; the multiplication "
             "topics settle it.")

# Words the narration may need that are hard for a Class 7 reader; the script author defines or avoids them.
HARD_WORDS = ["multiplicand", "multiplier", "reciprocal", "numerator", "denominator", "dividend", "divisor",
              "apavartana", "cancelling"]
