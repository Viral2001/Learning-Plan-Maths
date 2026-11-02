# -*- coding: utf-8 -*-
"""Chapter-level content for Class 8 Chapter 7, Proportional Reasoning (Ganita Prakash Grade 8 Part I, Chapter 7).
Book lines elsewhere are verbatim except: the book's dashes become commas, colons or "to"; minus is U+2212;
fractions are written with a slash (3/7) and mixed numbers as decimals (2.5)."""
from __future__ import annotations

CHAPTER = {
    "grade": 8,
    "label": "Class 8",
    "chapter_no": 7,
    "name": "Proportional Reasoning",
    "book_part": "Ganita Prakash Grade 8 Part I, Chapter 7",
    "source_pdf": "textbooks/class8/hegp107.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Similar Change",
     "Pictures that are resized well keep their shape because width and height change by the same factor, which "
     "opens the chapter and names the idea: proportional change."),
    ("M2", "Ratios and Proportions",
     "Ratios and their terms, the simplest form by dividing by the HCF, proportion written a : b :: c : d, mixtures "
     "that taste the same, and finding a missing term with one factor of change."),
    ("M3", "The Rule of Three",
     "Three known quantities and one unknown, cross multiplication ad = bc as Aryabhata described it, changes that "
     "are not proportional, and comparing offers by the rate for one unit."),
    ("M4", "Sharing and Units",
     "Sharing a whole in a ratio m : n, changing a mixture's ratio, and converting units of length, area, volume and "
     "temperature before reasoning proportionally."),
    ("M5", "Looking Back",
     "A summary of ratio, proportion and sharing in a ratio, and the Binairo puzzle."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter grows out of one question: why do some resized copies of a picture look right and others "
             "look stretched? The answer, that both measurements change by the same factor, becomes the idea of a "
             "ratio and of two ratios being proportional, and every later problem (recipes, wages, speeds, prices, "
             "sharing, units) is first tested for proportionality before it is scaled.",
    "points": [
        {"title": "Predict, then test the factor",
         "text": "Every concept opens with a prediction, such as which coffee is stronger or how much rice a cook "
                 "needs, and the factor of change or the simplest form then settles it."},
        {"title": "Multiply, do not add",
         "text": "Adding the same number to both terms (ages, picture sides) is set against multiplying both terms by "
                 "the same factor, so students learn to ask which change keeps the ratio."},
        {"title": "Check before you scale",
         "text": "Speed and time, and the prices of different shampoo bottles, show that not every pair of "
                 "quantities is proportional; the Rule of Three is used only after that check."},
        {"title": "Tools only where handling is the idea",
         "text": "Nine tools, each used once: stretching a picture, mixing two drinks, filling a ratio table, a double "
                 "number line, judging additive or multiplicative change, finding a unit rate, sharing a bar in a "
                 "ratio, matching temperatures, and bridging units."},
    ],
}

NCERT_ITEMS = [
    # 7.1 Observing similarity in change (pp 159 to 160)
    "7.1.images", "7.1.why", "7.1.factor_ac", "7.1.diff_ab", "7.1.factor_ad", "7.1.proportional",
    # 7.2 Ratios (p 161)
    "7.2.ratio", "7.2.meaning", "7.2.half", "7.2.factor_d",
    # 7.3 Ratios in their simplest form (pp 161 to 162)
    "7.3.simplest", "7.3.b_e", "7.3.proportion",
    # 7.4 Problem solving with proportional reasoning (pp 162 to 165)
    "7.4.ex1", "7.4.ex2", "7.4.ex3", "7.4.ex4", "7.4.ex5", "7.4.note_relate", "7.4.ex6", "7.4.ex7",
    "7.4.coffee", "7.4.coffee_strong", "7.4.coffee_light", "7.4.coffee_table",
    # Figure it Out, set 1 (questions 1 to 7)
    "FiO1.q1", "FiO1.q2", "FiO1.q3", "FiO1.q4", "FiO1.q5", "FiO1.q6", "FiO1.q7", "7.4.note_drawings",
    # Trairasika, the Rule of Three (pp 167 to 172)
    "7.4.ex8", "7.4.trairasika", "7.4.cross_mult", "7.4.aryabhata", "7.4.ex9", "7.4.note_strategies",
    "7.4.ex10", "7.4.note_tea", "7.4.act1",
    # Figure it Out, set 2 (questions 1 to 2)
    "FiO2.q1", "FiO2.q2",
    "7.4.puneeth", "7.4.act2", "7.4.act2_eco", "7.4.note_project",
    # 7.5 Sharing, but not equally (pp 172 to 175)
    "7.5.act3", "7.5.share_42", "7.5.general", "7.5.ex11", "7.5.ex12",
    # Figure it Out, set 3 (questions 1 to 5)
    "FiO3.q1", "FiO3.q2", "FiO3.q3", "FiO3.q4", "FiO3.q5",
    # 7.6 Unit conversions (p 176)
    "7.6.units", "7.6.temperature",
    # Figure it Out, set 4 (questions 1 to 11, and the Try This question 12)
    "FiO4.q1", "FiO4.q2", "FiO4.q3", "FiO4.q4", "FiO4.q5", "FiO4.q6", "FiO4.q7", "FiO4.q8", "FiO4.q9",
    "FiO4.q10", "FiO4.q11", "FiO4.q12",
    # Summary and Binairo (pp 177 to 178)
    "summary", "puzzle",
]

MISCONCEPTIONS = [
    ("M_ADD_SAME", "Adding or subtracting the same number from both terms keeps a ratio the same."),
    ("M_RATIO_ORDER", "The order of the terms does not matter, so 7 : 12 is the same as 12 : 7."),
    ("M_ONE_TERM_SCALED", "Only one term of a ratio needs to be multiplied to get a proportional ratio."),
    ("M_MIXED_UNITS", "A ratio can compare quantities in different units, such as minutes with hours or grams with "
                      "kilograms."),
    ("M_ALWAYS_PROPORTIONAL", "Any two quantities that grow together are proportional, so the Rule of Three always "
                              "works (for example, faster speed means more time)."),
    ("M_BIGGER_COSTS_MORE", "The pack with the bigger total price is always the more expensive one, without comparing "
                            "the price of one unit."),
    ("M_SHARE_BY_TERMS", "Sharing x in the ratio m : n means giving m to one and n to the other, without first "
                         "finding the size of one part."),
    ("M_FACTOR_INTEGER", "The factor of change must be a whole number, so 14 : 21 cannot become 6 : something."),
]

SOLUTION_NOTES = [
    "Kesang's lemonade (p 162): the question says her father asked her to make 18 more glasses, but the book's own "
    "working models 6 : 10 :: 18 : ? and ends with 30 spoons to make 18 glasses. The plan follows the book's working "
    "(18 glasses in all, 30 spoons) and phrases the question as 18 glasses in all.",
    "Aryabhata (p 168): the book prints the date as 199 CE; Aryabhata is usually dated to 499 CE. No year is stated in "
    "any student-facing line of the plan.",
    "Figure it Out set 2, question 1 (Earth): the answer key uses 52 weeks in a year, giving about 18076923 km; using "
    "365 days ÷ 7 gives a slightly different value. The plan follows the key and says 'about'.",
    "Figure it Out set 2, question 2 (mason): the wall lengths come from the house diagram; the key adds "
    "12 + 12 + 12 + 15 + 9 + 15 + 9 + 9 + 9 + 6 = 108 ft, and the plan uses that total.",
    "Figure it Out set 1, question 3: the third missing term is a fraction, 20 : 80/3.",
    "Figure it Out set 3, question 5 (orange paint): the answer 3 : 13 assumes the added bucket of yellow holds the "
    "same amount as the bucket of orange paint; the plan states that assumption.",
    "Figure it Out set 4, question 12 (coin): the costs are rounded to the nearest paisa (about ₹5.26 and ₹2.59, "
    "about ₹7.85 in all).",
    "Figure it Out set 4, questions 8 and 10: both answers are rounded (about 22956.8 kg of manure, about ₹82645).",
]
ERRATA = [
    "Kesang's lemonade: '18 more glasses' in the question disagrees with the book's working, which uses 18 glasses in "
    "all.",
    "Aryabhata's date is printed as 199 CE (usually 499 CE).",
]

DESIGN_REFERENCES = [
    {"text": "docs/25_new_design_learning_plan_playbook.md: framing intro, idea topics each ending in a doer, a "
             "question topic after each idea topic, and one summary topic.", "url": ""},
]

FIGURES = {}
