# -*- coding: utf-8 -*-
"""Chapter-level content for Class 5 Chapter 13, Animal Jumps (Maths Mela, Grade 5, Chapter 13).

The plan follows the "Class 5 Mathematics Learning Experience Designer" brief (priority_doc.md sections A to F) and the
/lp pipeline's structure; the book decides every number and every question. Book lines are verbatim except: the book's
dashes become commas, colons or "to"; minus is U+2212; the book's "Multiple of 6" (a missing s) is written "Multiples
of 6" and "each the numbers" is written "each of the numbers". No em dash and no en dash anywhere here."""
from __future__ import annotations

CHAPTER = {
    "grade": 5,
    "label": "Class 5",
    "chapter_no": 13,
    "name": "Animal Jumps",
    "book_part": "Maths Mela, Grade 5, Chapter 13",
    "source_pdf": "textbooks/class-5/eemm113.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Factors, Multiples and Arrays",
     "A box that multiplies numbers shows what a factor and a multiple are. Arrays of square tiles then show all the "
     "factors of a number, why a number is a multiple of each of its factors, and why 13 and 37 are prime numbers."),
    ("M2", "Common Multiples and Common Factors",
     "Animals jump along a number line from 0. The numbers two animals both touch are common multiples, and the jump "
     "sizes that reach several places on Mowgli's trail are common factors."),
    ("M3", "Using Factors and Multiples",
     "Testing statements about factors and multiples, sorting numbers by the factors 2, 5 and 10, using common "
     "multiples and common factors for the hunting days and the trail, and a revision of the whole chapter."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter takes place in the jungle trail of Mowgli and his animal friends. Animals jump along a number "
             "line from 0, and where they land shows what factors, multiples, common multiples and common factors "
             "are. A short video explains each idea, and an interactive tool lets the student try it alone.",
    "points": [
        {"title": "Videos teach, tools explore",
         "text": "Every idea has one short concept video. The tool that follows is where the student explores, "
                 "builds and checks the idea alone, with hints, retry and reset. Five tools, each with its own "
                 "purpose, follow the chapter's own plan."},
        {"title": "A tool in three steps",
         "text": "Each tool opens with a short recall of the video idea, then lets the student play and apply it, and "
                 "ends with the chapter's own questions, used exactly as the book gives them."},
        {"title": "Every book question has its own video",
         "text": "Every answerable prompt and every Let Us Do question of the book is its own short video with a step "
                 "by step solution and a question picture and a solution picture, in a Questions topic that follows "
                 "the idea it practises."},
        {"title": "The picture is the mathematics",
         "text": "Arrays of square tiles, number lines with animal jumps, the numbered trail and the three circles for "
                 "sorting carry each idea, with the numbers large and clear."},
        {"title": "Only the book's numbers",
         "text": "The box numbers, the trail and its friends, the cobbled road and every question are the book's own. "
                 "Any number the plan adds is a practice value and is said to be one."},
    ],
}

# {module_id: strand letter}: the subject strand each module belongs to (core/qt.py builds every objective's strand).
# CBSE maths catalog: N Number, A Algebra, G Geometry, M Measurement, D Data, S Statistics and Probability.
MODULE_STRANDS = {"M1": "N", "M2": "N", "M3": "N"}

# every book item, with its kind. Home concepts are listed in DESIGN.md section 3.
NCERT_ITEMS = [
    # the opener: the hidden numbers, factors and multiples
    ("open.story", "text"), ("open.factors", "text"), ("open.product", "text"),
    ("open.box", "prompt"),
    # arrays and Let Us Do (arrays)
    ("arr.def", "text"), ("arr.twelve", "text"), ("arr.fifteen", "prompt"),
    ("mult.def", "text"), ("one.self", "text"), ("arr.blanks12", "prompt"),
    ("LUDa.arrays", "exercise"), ("prime.why", "prompt"),
    # Animal Jumps: common multiples and Let Us Do (common multiples)
    ("cm.def34", "text"), ("cm.more34", "prompt"), ("cm.notice34", "talk"),
    ("cm.spider", "text"), ("cm.notice36", "talk"),
    ("cm.lists46", "text"), ("cm.list46", "prompt"),
    ("LUD.Q1", "exercise"), ("cm.noticeQ1", "talk"), ("LUD.Q2", "exercise"),
    # Mowgli's trail: common factors and Let Us Do (jumps and factors)
    ("LUD.Q3", "exercise"), ("trail.answer2", "text"), ("trail.three", "prompt"), ("trail.five", "prompt"),
    ("trail.ten", "prompt"), ("cf.def", "text"),
    ("LUD.Q4", "exercise"), ("LUD.Q5", "exercise"), ("LUD.Q6", "exercise"), ("LUD.Q7", "exercise"),
    ("cf.notice7", "talk"),
    # Let Us Do (factors and multiples at work)
    ("LUD.Q8", "exercise"), ("LUD.Q9", "exercise"), ("LUD.Q10", "exercise"), ("LUD.Q11", "exercise"),
    # the summary
    ("summary", "text"),
]

MISCONCEPTIONS = [
    ("M_ONE_MULTIPLIER", "There is only one possible multiplier for the numbers that come out of the box, the biggest "
                         "one, so 4 is the only answer and 2 and 1 are wrong."),
    ("M_FACTOR_MULTIPLE", "A factor and a multiple are the same thing, or a number is a multiple of its bigger "
                          "factors only: 3 is a multiple of 12, or 12 is a factor of 3."),
    ("M_MISS_ONE_SELF", "The factors of a number are only the pair in one array, so the factors of 15 are 3 and 5 and "
                        "1 and 15 do not count."),
    ("M_PRIME_NO_FACTORS", "13 has no factors because it has only one array, or 1 is not a factor of a prime number."),
    ("M_CM_ONLY_PRODUCT", "The first common multiple of two numbers is always their product, so it is 18 for 3 and 6 "
                          "and 24 for 4 and 6."),
    ("M_FIRST_ONLY", "The first common multiple is the only common multiple, or the list of common multiples ends "
                     "after a few numbers."),
    ("M_CF_CM_MIX", "Common factors and common multiples are the same: the common factors of 4 and 6 are 12 and 24."),
    ("M_JUMP_NEAR", "A jump of 4 reaches 10 because it goes from 8 to 12 past it, or a jump reaches a number it jumps "
                    "over."),
    ("M_CF_BIGGEST_ONLY", "Two numbers have only one common factor, the biggest, so 12 is the only common factor of 24 "
                          "and 36."),
    ("M_EVEN_FACTORS", "Every factor of an even number is even, so 3 cannot be a factor of 12."),
    ("M_ODD_MULTIPLES", "Every multiple of an odd number is odd, so 3 × 2 = 6 cannot be a multiple of 3."),
    ("M_ZERO_FACTOR", "0 is a factor of every number, because 0 times a number is a number."),
    ("M_TEN_ONLY", "A number can be divisible by 10 only, and not by 2 and 5."),
]

SOLUTION_NOTES = [
    {"item": "The opener: the four numbers of the box and the animals",
     "printed_solution": "The numbers 28, 36, 48 and 72 are only in the picture of the box. The picture shows a rabbit "
                         "and a deer; the book names a rabbit Robby and a deer Deeku only in a later question.",
     "correct": "The plan reads the four numbers off the picture and says them in the question. It lets Robby the "
                "rabbit and Deeku the deer watch the box in the hook, which is the plan's own reading."},
    {"item": "Let Us Do, Q1 (common multiples) and Q7 (common factors): the part letters",
     "printed_solution": "Each question prints the letter (f) twice and has nine pairs: the third column starts again "
                         "at (f).",
     "correct": "The plan letters the nine pairs (a) to (i) in the book's order."},
    {"item": "The trail of Mowgli's friends: the last stones",
     "printed_solution": "The last two stones are both printed 59 (the trail has 61 stones).",
     "correct": "The plan reads the last stone as 60, so the trail runs from 0 to 60. No friend lives there, so no "
                "answer about the friends changes."},
    {"item": "The trail: where Sher Khan lives",
     "printed_solution": "The number 26 is printed in red next to the tiger, but Let Us Do Q10 says Sher Khan's house "
                         "is on number 25, and the jumps of 5 (5 is a common factor of 25, 30, 35 and 50) need 25.",
     "correct": "The plan places Sher Khan on 25. The red 26 is a printing slip."},
    {"item": "The trail: the red and blue numbers and the book's answer lines",
     "printed_solution": "The book prints 4, 12, 14 and 50 as the places a jump of 2 reaches, and 9, 21, 39 and 57 for a "
                         "jump of 3. The red numbers in the picture are 4, 12, 26 and 50.",
     "correct": "Baloo (30) is also reached by jumps of 2, and the frog (12) and Baloo (30) are also reached by "
                "jumps of 3. The plan gives the full lists: jump 2: 4, 12, 14, 30, 50; jump 3: 9, 12, 21, 30, 39, "
                "57; jump 5: 25, 30, 35, 50; jump 10: 30, 50."},
    {"item": "Mowgli's friends and their places",
     "printed_solution": "Only some friends have a number printed in the picture; the others stand next to a stone.",
     "correct": "The plan reads: ant 4, spider 9, frog 12, bird 14, Kaa the snake 21, Sher Khan the tiger 25, Baloo "
                "the bear 30, Akela the wolf 35, deer 39, rabbit 50, monkey 57 (from the picture and from "
                "Let Us Do Q10 and the jumps of 5)."},
    {"item": "Let Us Do, Q2: where the food is",
     "printed_solution": "The food is drawn after the last stone, 64, and no number is printed on it.",
     "correct": "The plan reads the end of the road as stone 64: Robby lands on it (4 × 16 = 64), Deeku does not "
                "(6 × 10 = 60 and 6 × 11 = 66). If the food were a stone further on, the question would have a "
                "different answer. To be confirmed."},
    {"item": "Let Us Do, Q9: counting the days",
     "printed_solution": "The book does not say whether the first day is day 0 or day 1.",
     "correct": "The plan counts the day they start together as day 0, like the start of a number line, so they hunt "
                "together on days 15, 30, 45 and so on. If the first day is day 1, they hunt together on days 1, 16, "
                "31 and so on. To be confirmed."},
    {"item": "Let Us Do, Q8 (f): 0 as a factor",
     "printed_solution": "The book gives no answer key.",
     "correct": "The plan answers True: a jump of 0 never leaves 0, and 0 times any number is 0, so 0 cannot be a "
                "factor of a number you want to reach. Whether 0 is a factor of 0 itself is not discussed in the "
                "book."},
    {"item": "Let Us Do, Q11: the circle for divisible by 10 only",
     "printed_solution": "The three circles of the book have a place for numbers divisible by 10 only.",
     "correct": "No number can go there: a number divisible by 10 is also divisible by 2 and by 5. The plan says so "
                "in the answer (none) and puts 90, 30 and 40 in the middle."},
    {"item": "Let Us Do, Q1 (common multiples) and the open prompts with many answers",
     "printed_solution": "The book asks for any 5 common multiples, a few more common multiples, and what numbers "
                         "might have gone into the box.",
     "correct": "The plan gives one reasoned sample answer (the first common multiple and its next multiples) and "
                "says the student's answer may differ."},
    {"item": "Let Us Do, Q3 to Q5 and the trail lines: the blanks",
     "printed_solution": "The lines 'Which numbers will he touch if he jumps by 5 steps?' and 'the common factor of "
                         "the numbers ___' have blanks and no answer.",
     "correct": "The plan answers both blanks: the numbers he touches on the trail, and the friends' numbers that "
                "5 (and 10) is a common factor of."},
    {"item": "The book's wording: 'Multiple of 6' and 'each the numbers'",
     "printed_solution": "Page 166 prints 'Multiple of 6' and page 168 prints 'exactly divides each the numbers'.",
     "correct": "The plan writes 'Multiples of 6' and 'each of the numbers'."},
    {"item": "Prime numbers",
     "printed_solution": "The book names 13 and 37 as prime numbers and asks Why, but does not define the word.",
     "correct": "The plan answers from the arrays: each has only the array 1 × 13 or 1 × 37, so only two factors, "
                "1 and itself. It teaches no more about prime numbers than this."},
    {"item": "Divisible by 2, 5 and 10 and testing statements",
     "printed_solution": "Let Us Do Q8 and Q11 need these ideas; the chapter does not teach them in words before the "
                         "questions.",
     "correct": "The plan adds one short idea for each (checking a statement with examples, and divisible = a "
                "factor, using only the chapter's own words: divide completely, factor, multiple)."},
    {"item": "Brief: revision video",
     "printed_solution": "The brief asks for an interactive recap or revision video.",
     "correct": "The pipeline has no recap video, so the last topic is a text summary with short concept checks."},
]
ERRATA = []

DESIGN_REFERENCES = [
    {"text": "priority_doc.md (the plan written to the 'Class 5 Mathematics Learning Experience Designer' brief, "
             "2026-11-06): topic flow, video types, the 5 tools, the shared visual language and the learning rules "
             "decide this chapter's design.", "url": ""},
    {"text": "docs/01_runbook.md and .claude/skills/lp/SKILL.md: framing intro with a free-try tool, idea topics each "
             "ending in a Practice concept, a Questions topic after every idea topic with a question concept and an "
             "answer concept per book question, and one summary topic.", "url": ""},
]

# The book's own figures that carry mathematics, keyed by authored concept key. One concept image per teaching,
# hook and summary concept where a drawn figure is the maths; the tool concepts (Practice / free try) are pictured by
# their tool.
FIGURES = {
    "T1.C1": ["A cardboard box with an arrow going in and an arrow coming out, and four number tags coming out of it: "
              "28, 36, 48 and 72."],
    "T1B.C1": ["The same kind of box marked with the multiplier 6, the numbers 5, 7 and 9 going in and 30, 42 and 54 "
               "coming out."],
    "T2.C1": ["The arrays of 18 square tiles: 1 row of 18, 2 rows of 9 and 3 rows of 6, each written as a "
              "multiplication."],
    "T2.C2": ["The arrays of 44 square tiles written as 1 × 44, 2 × 22 and 4 × 11, with the six factors named."],
    "T2.C3": ["One row of 19 square tiles as the only array of 19, beside the two arrays of 21 tiles, 1 × 21 and "
              "3 × 7."],
    "T3.C1": ["A number line from 0 to 30 with Robby's jumps of 2 and Deeku's jumps of 5, and 10, 20 and 30 marked "
              "where both land."],
    "T3.C2": ["A number line from 0 to 90 with jumps of 6 and jumps of 15 meeting at 30, 60 and 90, each 30 apart."],
    "T4.C1": ["A number line from 0 to 28 with Mowgli's jumps of 4, landing on 8 and 20 and skipping 14 and 26."],
    "T4.C2": ["Two lists, the factors of 18 and the factors of 30, with the four numbers in both lists circled."],
    "T5.C1": ["Two statement cards, one marked true with the multiples of 4 split into 2s, and one marked false with "
              "6 as a multiple of 6 that is not a multiple of 4."],
    "T5.C2": ["Three overlapping circles for divisible by 2, 5 and 10 with 16 and 48 in the circle for 2 only, 35 and "
              "85 in the circle for 5 only, 60 and 70 in the middle."],
    "T6.C1": ["The jungle trail from the hidden box to the hunting days, one stop for each idea of the chapter."],
}
