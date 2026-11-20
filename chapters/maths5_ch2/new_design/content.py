# -*- coding: utf-8 -*-
"""Chapter-level content for Class 5 Chapter 2, Fractions (Maths Mela, Grade 5, Chapter 2).

The plan follows the "Class 5 Mathematics Learning Experience Designer" brief (priority_doc.md sections A to F) and the
/lp pipeline's structure; the book decides every number and every question. Book lines are verbatim except: the book's
dashes become commas, colons or "to"; minus is U+2212; fractions are written a/b; the book's "1/6s" is written "pieces
of 1/6" (a plural letter glued to a fraction cannot be converted to LaTeX). No em dash and no en dash anywhere here."""
from __future__ import annotations

CHAPTER = {
    "grade": 5,
    "label": "Class 5",
    "chapter_no": 2,
    "name": "Fractions",
    "book_part": "Maths Mela, Grade 5, Chapter 2",
    "source_pdf": "textbooks/class-5/eemm102.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Same Whole, Equal Parts and Equivalent Fractions",
     "Why two fractions can be compared only on the same whole, finding fractions of a grid, making a whole from "
     "fraction pieces, and making equivalent fractions by cutting parts into more equal parts."),
    ("M2", "Comparing Fractions and Going Past One",
     "Comparing fractions that have the same denominator or the same numerator, and showing fractions greater than 1 "
     "with parathas, a pizza and number lines."),
    ("M3", "References, a Puzzle and Revision",
     "Comparing fractions with 1 and with 1/2 as references, a puzzle about family relations, and a revision of the "
     "whole kitchen of fractions."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter takes place in a family kitchen. Chocolates, chikki, parathas and pizza are the wholes, and "
             "cutting and sharing them shows what a fraction is, when two fractions name the same part, and how to "
             "tell which of two fractions is more. A short video explains each idea, and an interactive tool lets the "
             "student try it alone.",
    "points": [
        {"title": "Videos teach, tools explore",
         "text": "Every idea has one short concept video. The tool that follows is where the student explores, "
                 "builds and checks the idea alone, with hints, retry and reset. Eight tools, each with its own "
                 "purpose, follow the chapter's own plan."},
        {"title": "A tool in three steps",
         "text": "Each tool opens with a short recall of the video idea, then lets the student play and apply it, and "
                 "ends with the chapter's own question, used exactly as the book gives it."},
        {"title": "Every book question has its own video",
         "text": "Every solved example, Let Us Do question and every answerable prompt of the book is its own short "
                 "video with a step by step solution and a question picture and a solution picture, in a Questions "
                 "topic that follows the idea it practises."},
        {"title": "The picture is the mathematics",
         "text": "Bars, circles, grids and number lines carry each idea: equal parts with clear cut lines, the "
                 "fraction as the largest thing on screen, number lines with 0, 1 and 2 labelled."},
        {"title": "Only the book's numbers",
         "text": "Grid sizes, bar sizes, kit pieces and every question are the book's own. Any number the plan adds is "
                 "a practice value and is said to be one."},
    ],
}

# {module_id: strand letter}: the subject strand each module belongs to (core/qt.py builds every objective's strand).
# CBSE maths catalog: N Number, A Algebra, G Geometry, M Measurement, D Data, S Statistics and Probability.
MODULE_STRANDS = {"M1": "N", "M2": "N", "M3": "N"}

# every book item, with its kind. Home concepts are listed in DESIGN.md section 3.
NCERT_ITEMS = [
    # the opener: same whole
    ("open.story", "text"), ("open.rule", "text"),
    ("open.chocolate", "prompt"), ("open.when", "prompt"),
    # Playing with a Grid
    ("grid.setup", "text"), ("grid.shade", "prompt"), ("grid.third", "prompt"),
    # Fun with the Fraction Kit and Let Us Do (kit)
    ("kit.intro", "text"), ("kit.half_quarter", "text"), ("kit.relation", "talk"), ("eq.term", "text"),
    ("kit.generate", "talk"),
    ("eq.strip", "prompt"), ("kit.five", "prompt"), ("kit.half", "prompt"),
    ("LUD1.Q1", "exercise"), ("LUD1.Q2A", "exercise"), ("LUD1.Q2B", "exercise"), ("LUD1.Q2C", "exercise"),
    ("LUD1.Q3", "exercise"),
    # Making Equivalent Fractions and Let Us Do (equivalent fractions)
    ("mk.sameer", "text"), ("mk.equivalent_def", "text"), ("mk.pattern", "talk"),
    ("mk.third_divide", "prompt"), ("mk.twofifths", "prompt"),
    ("LUDeq.Q1", "exercise"), ("LUDeq.Q2", "exercise"), ("LUDeq.Q3", "exercise"),
    # comparing, same denominator
    ("sd.chikki", "example"), ("LUDsd.Q1", "exercise"),
    # comparing, same numerator
    ("sn.reason", "talk"), ("sn.paratha", "example"), ("LUDsn.Q1", "exercise"),
    # fractions greater than 1
    ("gt1.intro", "text"), ("gt1.nl_halves", "text"), ("gt1.nl_fourths", "text"),
    ("gt1.maa", "example"), ("gt1.radhika", "example"), ("gt1.dadiji", "prompt"), ("gt1.three_lines", "prompt"),
    ("gt1.day_halves", "prompt"), ("gt1.dadaji9", "example"), ("gt1.five_lines", "prompt"),
    ("gt1.day_fourths", "prompt"), ("gt1.pizza_share", "example"), ("gt1.pizza_more", "example"),
    ("LUDgt1.Q1", "exercise"), ("LUDgt1.Q2", "exercise"), ("try.ants", "prompt"),
    # comparing with reference to 1 and to 1/2
    ("r1.example", "example"), ("LUDr1.Q1", "exercise"),
    ("rh.pictures", "text"), ("LUDh.Q1", "exercise"), ("LUDh.Q2", "exercise"), ("rh.example", "example"),
    ("LUDh.Q3", "exercise"),
    # Fun with Relations and the summary
    ("rel.puzzle", "prompt"),
    ("summary", "text"),
]

MISCONCEPTIONS = [
    ("M_DIFF_WHOLE", "1/2 of something is always more than 1/3 of something, whatever the two wholes are."),
    ("M_UNEQUAL_PARTS", "The parts of a whole need not be equal: shading any 1 of 3 parts shows 1/3."),
    ("M_BIGGER_DENOM", "The bigger the bottom number, the bigger the fraction, so 1/8 is more than 1/6."),
    ("M_EQUIV_ADD", "Equivalent fractions come from adding the same number to the top and the bottom, so 1/3 = 2/4."),
    ("M_SAME_TOP_BIGGER", "With the same top number, the fraction with the bigger bottom number is the bigger "
                          "fraction, so 4/6 is more than 4/5."),
    ("M_TOP_ONLY", "The fraction with the bigger top number is always the bigger fraction, so 3/8 is more than 2/3."),
    ("M_NO_PAST_ONE", "A fraction cannot be more than one whole, so 5/2 is not a possible fraction."),
    ("M_MIXED_TIMES", "2 1/2 means 2 times 1/2, or the fraction 21/2."),
    ("M_NEAR_HALF", "A fraction whose top is close to half of its bottom, such as 5/9 or 3/5, is equal to 1/2."),
    ("M_NEW_PERSON", "In the relation puzzle the only brother of the father's sister is a new person, not the "
                     "father."),
]

SOLUTION_NOTES = [
    {"item": "The fraction kit (Fun with Fraction Kit and Let Us Do on the kit)",
     "printed_solution": "The book says a kit is given at the end of the textbook.",
     "correct": "The kit is the Fractions Kit sheet in the book's Learning Material Sheets (the 13th PDF page of "
                "eemm115.pdf): twelve round discs, the whole and the discs cut into 2 to 12 equal pieces (1/2 to 1/12). "
                "The plan uses exactly these. Names that need pieces the kit does not have (such as 4/16, 3/15, 4/20, "
                "3/18, 4/24) come from the pattern of equivalent fractions."},
    {"item": "Let Us Do on the kit, Q3: make a whole using any seven pieces",
     "printed_solution": "The book does not say whether the seven pieces are of one size.",
     "correct": "The plan accepts any seven pieces that make a whole: two 1/4, one 1/6 and four 1/12 (6/12 + 2/12 + "
                "4/12 = 12/12 = 1), or seven pieces of 1/7 (the kit has a 1/7 disc)."},
    {"item": "How many parathas were made on this day (halves day and fourths day)",
     "printed_solution": "The book does not say whose pieces to add.",
     "correct": "The plan adds all six family members of the story (a family of 6): 36 halves = 18 parathas, and 52 "
                "fourths = 13 parathas. To be confirmed."},
    {"item": "Dadiji and Dadaji (halves)",
     "printed_solution": "The book prints Dadiji had 7 pieces, then Dadaji ate 7 pieces.",
     "correct": "Both are in the family, so the plan keeps both names as printed."},
    {"item": "Let Us Do on reference to 1, Q1 (f) 15/5 and 16/4",
     "printed_solution": "The book asks to compare using 1 as a reference.",
     "correct": "15/5 = 3 and 16/4 = 4 are both greater than 1, so 1 cannot decide. The plan settles it by counting "
                "wholes: 3 is less than 4. The other five parts do split around 1."},
    {"item": "Let Us Do on fractions greater than 1, Q2",
     "printed_solution": "The box prints 14 fractions and 9/4 appears twice.",
     "correct": "Kept as printed; both 9/4 are greater than 1."},
    {"item": "Let Us Do on the kit: the wording 1/6s, 1/8s and 1/12s",
     "printed_solution": "The book writes the number of pieces as a fraction with an s, such as 1/6s.",
     "correct": "The plan writes pieces of 1/6, pieces of 1/8 and pieces of 1/12 (same meaning)."},
    {"item": "Opener: Is Tamanna correct, and which grid holds 1/3",
     "printed_solution": "The book prints no answer for either.",
     "correct": "Chocolates: the small bar has 4 blocks and the big bar 9 blocks, all blocks the same size, so 1/2 of the "
                "small bar is 2 blocks and 1/3 of the big bar is 3 blocks, which is more. Grids: 1/3 of 48 is 16 squares, "
                "two 1/6 parts of grid B and four 1/12 parts of grid C; grid A cannot make it. Plan's own reading."},
    {"item": "Let Us Do on reference to 1/2, Q3",
     "printed_solution": "The book prints the eight pairs in a table without letters.",
     "correct": "The plan letters the pairs (a) to (h) in order."},
    {"item": "Try This (the ants)",
     "printed_solution": "The book places it at the end of the chapter.",
     "correct": "The plan practises it with fractions greater than 1, where 16 pieces of 1/4 = 16/4 = 4 cm is learnt."},
    {"item": "Brief: revision video",
     "printed_solution": "The brief asks for an interactive recap or revision video.",
     "correct": "The pipeline has no recap video, so the last topic is a text summary with short concept checks."},
    {"item": "Open prompts (equivalents the kit gives, combinations of pieces, fractions to find)",
     "printed_solution": "No single answer.",
     "correct": "The plan gives one reasoned sample answer and says the student's answer may differ."},
]
ERRATA = []

DESIGN_REFERENCES = [
    {"text": "priority_doc.md (the plan written to the 'Class 5 Mathematics Learning Experience Designer' brief, "
             "2026-11-05): topic flow, video types, the 8 tools, the shared visual language and the learning rules "
             "decide this chapter's design.", "url": ""},
    {"text": "docs/01_runbook.md and .claude/skills/lp/SKILL.md: framing intro with a free-try tool, idea topics each "
             "ending in a Practice concept, a Questions topic after every idea topic with a question concept and an "
             "answer concept per book question, and one summary topic.", "url": ""},
]

# The book's own figures that carry mathematics, keyed by authored concept key. One concept image per teaching,
# hook and summary concept where a drawn figure is the maths; the tool concepts (Practice / free try) are pictured by
# their tool.
FIGURES = {
    "T1.C1": ["Two chocolate bars on a table: a small bar of 4 equal blocks in 2 rows of 2 and a big bar of 9 equal blocks "
              "in 3 rows of 3, every block the same size. No fractions written."],
    "T1B.C1": ["Two rotis of different sizes, half of each marked, next to two rotis of the same size with half and a "
              "quarter marked."],
    "T2.C1": ["A grid of 20 equal squares in 4 rows of 5 with the squares split into 4 equal groups of 5 and one group "
              "shaded."],
    "T2.C2": ["A grid of 24 equal squares: one 1/4 part of 6 squares shaded, beside the same 6 squares seen as two 1/8 "
              "parts of 3 squares."],
    "T3.C1": ["A round whole made of 4 equal pieces, each marked 1/4."],
    "T3.C2": ["A round whole made of one 1/2 piece, one 1/4 piece and two 1/8 pieces, and a 1/4 piece covered by two 1/8 "
              "pieces."],
    "T3.C3": ["A grid of 20 squares: a 1/4 part of 5 squares and one single 1/20 square placed on it five times."],
    "T4.C1": ["A shape in 5 equal rows with 4 shaded, then the same shape with every row cut into 2 equal parts: 4/5 and "
              "8/10, the shaded area outlined the same."],
    "T4.C2": ["Three copies of a shape with 3/8, 6/16 and 9/24 shaded, the top and bottom numbers joined by arrows marked "
              "x2 and x3."],
    "T5.C1": ["A chocolate bar cut into 10 equal pieces with 3 pieces marked beside the same bar with 7 pieces marked."],
    "T6.C1": ["Two bars of equal length, one cut into 4 equal pieces and one into 10, three pieces of each marked."],
    "T7.C1": ["Pieces of 1/2 paratha: 4 whole parathas each cut in two and one half piece, with a number line from 0 to 5 "
              "marked at every 1/2."],
    "T7.C2": ["A number line marked at every 1/4 from 0 to 3 with 11 hops, and a pizza cut in 3 slices with 8 slices "
              "shown as 2 whole pizzas and 2 slices."],
    "T7.C3": ["Two sets of pieces of 1/5: 8 pieces forming one whole and 3 more, and 3 pieces of 1/10."],
    "T8.C1": ["A number line with 1 marked, 3/5 to its left and 10/9 to its right."],
    "T8.C2": ["A circle in 18 equal pieces with 9 marked and a circle in 15 equal pieces with 7 marked, a half line "
              "through each."],
    "T8.C3": ["A number line with 1/2 and 1 marked, 5/12 just left of 1/2 and 7/10 between 1/2 and 1."],
    "T9.C1": ["A small family tree with a grandfather, a father, a mother and children, one link highlighted at a time."],
    "T10.C1": ["A kitchen counter with a chocolate bar, a grid, a kit tray, parathas and a number line, one for each idea of "
               "the chapter."],
}
