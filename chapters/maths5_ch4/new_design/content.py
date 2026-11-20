# -*- coding: utf-8 -*-
"""Chapter-level content for Class 5 Chapter 4, We the Travellers - II (Maths Mela, Grade 5, Chapter 4).

The plan follows the "Class 5 Mathematics Learning Experience Designer" brief (priority_doc.md sections A to F) and the
/lp pipeline's structure; the book decides every number and every question. Book lines are verbatim except: the book's
dashes become commas, colons, hyphens inside words or "to"; minus is U+2212; litres are written in full; numbers of four
or more digits carry commas as in the book (1301 and 2700 are written 1,301 and 2,700). No em dash and no en dash
anywhere here."""
from __future__ import annotations

CHAPTER = {
    "grade": 5,
    "label": "Class 5",
    "chapter_no": 4,
    "name": "We the Travellers - II",
    "book_part": "Maths Mela, Grade 5, Chapter 4",
    "source_pdf": "textbooks/class-5/eemm104.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Balancing Sums, Addition and Subtraction",
     "Making two sums equal by swapping, adding large numbers by place value, adding near-round numbers the easier way, "
     "and subtraction and its relationship with addition."),
    ("M2", "Consecutive Numbers, Large Numbers and Journey Problems",
     "Patterns in the sums of consecutive numbers and the pair-the-ends shortcut, adding and subtracting large numbers, "
     "and journey problems that add, subtract and compare."),
    ("M3", "Quick Number Strategies and Number Puzzles",
     "Making 100, 1,000 and 10,000, subtracting 9 and 99, palindrome numbers and number grid puzzles."),
    ("M4", "Even and Odd, Thinking Puzzles and Tables",
     "Even and odd numbers and their sums, two thinking puzzles about coins and a torch, reading tables, and a revision "
     "of the whole road trip."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter is a road trip. Fuel, distances, money and weights are the numbers a traveller meets, and "
             "adding and subtracting them, even when they are large, uses the same steps as small numbers. Number "
             "patterns and puzzles fill the long hours on the road. A short video explains each idea, and an "
             "interactive tool lets the student try it alone.",
    "points": [
        {"title": "Videos teach, tools explore",
         "text": "Every idea has one short concept video. The tool that follows is where the student explores, "
                 "builds and checks the idea alone, with hints, retry and reset. Eight tools, each with its own "
                 "purpose, follow the chapter's own plan."},
        {"title": "A tool in three steps",
         "text": "Each tool opens with a short recall of the video idea, then lets the student play and apply it, and "
                 "ends with the chapter's own question, used exactly as the book gives it."},
        {"title": "Every book question has its own video",
         "text": "Every solved example, Let Us Solve, Let Us Think and Let Us Do question and every answerable prompt "
                 "of the book is its own short video with a step by step solution and a question picture and a "
                 "solution picture, in a Questions topic that follows the idea it practises."},
        {"title": "The picture is the mathematics",
         "text": "Place value charts, number lines, cards in two trays, milestones, grids and counters in pairs carry "
                 "each idea. The numbers stay the largest and clearest thing on screen."},
        {"title": "Only the book's numbers",
         "text": "Distances, amounts, tables and puzzles are the book's own. Any number the plan adds is a practice "
                 "value and is said to be one."},
    ],
}

# {module_id: strand letter}: the subject strand each module belongs to (core/qt.py builds every objective's strand).
# CBSE maths catalog: N Number, A Algebra, G Geometry, M Measurement, D Data, S Statistics and Probability.
MODULE_STRANDS = {"M1": "N", "M2": "N", "M3": "N", "M4": "N"}

# every book item, with its kind. Home concepts are listed in DESIGN.md section 3.
NCERT_ITEMS = [
    # the opener: Making Sums Equal
    ("open.intro", "text"), ("open.hint", "talk"),
    ("msq.a", "prompt"), ("msq.b", "prompt"), ("msq.c", "prompt"), ("msq.d", "prompt"),
    # Fuel Arithmetic
    ("fuel.facts", "text"), ("fuel.remember", "text"),
    ("fuel.lorry", "example"), ("fuel.49_89", "prompt"), ("LUS43.add", "exercise"),
    # relationship between addition and subtraction, More Fuel Arithmetic, Let Us Solve (subtracting)
    ("rel.Q1", "exercise"), ("rel.Q2", "exercise"),
    ("fuel2.minibus", "example"),
    ("LUS45.Q1", "exercise"), ("LUS45.Q2to9", "exercise"),
    # Sums of Consecutive Numbers
    ("cons.def", "text"), ("cons.boxes", "text"),
    ("cons.q1", "exercise"), ("cons.q2", "exercise"), ("cons.q3", "exercise"),
    ("cons.patterns", "text"), ("cons.find", "exercise"),
    # the longest land route, subtracting large numbers, Let Us Solve, Let Us Do
    ("land.intro", "text"), ("land.nl", "text"), ("land.same", "text"),
    ("land.ns", "example"), ("land.mahesh", "example"), ("land.aligned", "text"),
    ("LUSbig.Q1", "exercise"), ("land.trip", "exercise"), ("land.closest", "exercise"),
    ("sub.intro", "talk"), ("sub.same", "text"),
    ("sub.ship", "example"), ("sub.talon", "example"), ("sub.aligned", "text"),
    ("LUSsub.Q1", "exercise"),
    ("LUD.Q1", "exercise"), ("LUD.Q2", "exercise"),
    # journey problems
    ("mary", "exercise"), ("council", "exercise"), ("truck", "exercise"),
    ("LUD.Q3", "exercise"), ("LUD.Q4", "exercise"), ("LUD.Q5", "exercise"),
    # Quick Sums and Differences
    ("qs.intro", "text"), ("qs.piku", "text"), ("qs.always", "talk"), ("qs.zero", "talk"),
    ("qs.namita", "talk"), ("qs.rev_intro", "text"),
    ("qs.sukanta", "example"), ("qs.fifty_nine", "prompt"), ("qs.use", "prompt"), ("qs.zero_set", "exercise"),
    ("qs.sub", "exercise"), ("qs.rev", "exercise"),
    # palindromes and grids
    ("pal.def", "text"), ("pal.1", "exercise"), ("pal.2", "exercise"), ("pal.3", "exercise"),
    ("grid.rules", "text"),
    ("grid.a", "exercise"), ("grid.b", "exercise"), ("grid.c", "exercise"), ("grid.d", "exercise"),
    ("grid.e", "exercise"),
    # even and odd numbers
    ("eo.arrange", "text"),
    ("eo.circle", "exercise"), ("eo.add18", "exercise"), ("eo.add23", "exercise"),
    ("eo.q3a", "exercise"), ("eo.q3b", "exercise"), ("eo.q3c", "exercise"),
    # Let Us Think: coins and the torch, mountain climbing; Math Metric Mela
    ("jincy", "exercise"), ("torch23", "exercise"), ("torchrule", "exercise"),
    ("mtn.intro", "text"), ("mtn.award", "text"), ("mtn", "exercise"),
    ("mela.text", "text"), ("mela", "exercise"),
    # the summary
    ("summary", "text"),
]

MISCONCEPTIONS = [
    ("M_NO_CARRY", "When the ones add to 10 or more, write both digits in the ones place and do not regroup, so "
                   "28 + 75 = 913."),
    ("M_SMALL_FROM_BIG", "In a subtraction, take the smaller digit from the bigger digit in every column, so "
                         "65 − 18 = 53."),
    ("M_FORGET_ONE", "To add 99 add 100 and stop, and to take away 99 take away 100 and stop: the 1 is forgotten."),
    ("M_UNRELATED", "Knowing 46 + 21 = 67 does not help to find 67 − 21: addition and subtraction are separate."),
    ("M_MISALIGN", "Numbers are lined up from the left, so 12 + 123 is added with the 1 of 12 under the 1 of 123."),
    ("M_SWAP_ONE_SUM", "When two numbers are swapped between two groups, only one of the sums changes."),
    ("M_SWAP_BIGGEST", "Swapping the two biggest numbers always brings the sums closer together."),
    ("M_CONSEC_PARITY", "The sum of consecutive numbers is always even, or always odd."),
    ("M_SUCC_DIFF_ONE", "Successive sums of consecutive numbers always go up by 1 or by 2, whatever the count."),
    ("M_FIRST_TIMES", "A run of 5 consecutive numbers adds up to 5 times the first number."),
    ("M_PAL_SAME", "A palindrome number has all its digits the same, so 121 is not a palindrome."),
    ("M_GRID_ROWS_ONLY", "A grid is right when every row follows its arrow; the columns can be ignored."),
    ("M_ODD_ODD_ODD", "Two odd numbers add up to an odd number."),
    ("M_ZERO_NOT_EVEN", "A number that ends in 0 is neither even nor odd."),
    ("M_LESS_THAN_TAKE", "\"Has 6,758 runs less than Sachin\" means take 6,758 away from the runs given."),
    ("M_ONE_WAY_COINS", "There is only one way to pay an exact amount with coins."),
    ("M_TORCH_COUNT", "To know the torch after the 23rd press you must go through all 23 presses one by one."),
    ("M_ESTIMATE_EXACT", "An estimate must be exactly equal to the real answer."),
    ("M_NINES_ZERO", "The nines method for making 100 or 1,000 does not work when the units digit is 0."),
]

SOLUTION_NOTES = [
    {"item": "Making Sums Equal, the least number of moves",
     "printed_solution": "The book prints no answer and does not define a move.",
     "correct": "A move is the interchange of one number from one group with one number from the other group. "
                "Checking every possible swap: (a) 1 move, swap 2 and 3; (b) 1 move, swap 5 and 9, or 7 and 11; "
                "(c) 2 moves, for example 11 with 13 and 15 with 17; (d) 2 moves, for example 77 with 81 and 78 with "
                "82. Plan's own reading."},
    {"item": "Making Sums Equal, the hint about 2 and 5",
     "printed_solution": "The book asks what happens to the sums if 2 and 5 are interchanged.",
     "correct": "In puzzle (a) the sums become 22 and 18, further apart than 19 and 21. The plan uses the hint as a "
                "first try that shows what a swap does."},
    {"item": "Map label 1885 km on the North-South Corridor map",
     "printed_solution": "The map prints 1885 km, the text and the book's sum use 1,855 km.",
     "correct": "The plan uses 1,855 km (the text and the sum 1,855 + 1,862 = 3,717). To be confirmed."},
    {"item": "Let Us Do, Q1 and Q2: repeated letter (f)",
     "printed_solution": "Both questions have nine parts but the printed letters run a to f, then f to h.",
     "correct": "The plan letters the nine parts (a) to (i) in the order printed."},
    {"item": "Let Us Do, Q1 (h): 50,050 + 55,000",
     "printed_solution": "The sum has six digits, one place beyond the chart of this chapter.",
     "correct": "The plan writes 1,05,050 (Indian comma pattern), writes the extra 1 in a new place on the left and "
                "does not name that place. To be confirmed."},
    {"item": "Sums of Consecutive Numbers, Q1 to Q3",
     "printed_solution": "The book prints no answers.",
     "correct": "Plan's reading: sums of 2 consecutive numbers are always odd, of 3 alternate odd and even, of 4 are "
                "always even; the difference between successive sums is 2, 3 and 4 in the three boxes and 5 and 6 "
                "for 5 and 6 consecutive numbers."},
    {"item": "Patterns in sums with arrows, and the four sums to find without adding directly",
     "printed_solution": "The book says to notice how the sums are related to the numbers added.",
     "correct": "Plan's reading: pairs from the two ends make the same total, so 67 + 68 + 69 = 3 × 68 = 204, "
                "24 + 25 + 26 + 27 = 2 × 51 = 102, 48 + 49 + 50 + 51 + 52 = 5 × 50 = 250 and 237 + 238 + 239 + 240 + "
                "241 + 242 = 3 × 479 = 1,437."},
    {"item": "The great Indian road trip",
     "printed_solution": "Four distances sit on the map; the label 590 km sits under the word Mumbai.",
     "correct": "Plan's reading: Delhi to Mumbai 1,600 km, Mumbai to Goa 590 km, Goa to Hyderabad 670 km, Hyderabad to "
                "Puri 1,055 km, total 3,915 km."},
    {"item": "Find 2 numbers whose sum is closest to 10,000, 15,000, 13,000, 16,000",
     "printed_solution": "The book prints no answer.",
     "correct": "All ten pairs were checked: 5,205 + 4,840 = 10,045; 6,220 + 8,455 = 14,675; 8,455 + 4,840 = 13,295, "
                "and the next pair for 13,000, 6,220 + 7,095 = 13,315, is 20 further away; 7,095 + 8,455 = 15,550."},
    {"item": "School council: estimate whether the money is enough",
     "printed_solution": "The book does not say how to estimate.",
     "correct": "The plan rounds each amount up to the next thousand: 40,000 + 10,000 + 20,000 = 70,000, which is less "
                "than 70,500, so the real total is less still: enough. Exact total 68,878, left 1,622."},
    {"item": "Quick Sums, will the method always work, and the units digit 0",
     "printed_solution": "Discussion prompts with no printed answer.",
     "correct": "Plan's reading: it always works; with a 0 in the units place the last nine is still 9 and the extra 1 "
                "carries (180: 819 + 1 = 820); other methods: count up to the next hundred then to 1,000, or take 180 "
                "from 1,000."},
    {"item": "Quick Sums, use the above solutions, do not calculate again",
     "printed_solution": "The book does not say which solutions are meant.",
     "correct": "Plan's reading: the quick method for 9 and 99 (take away 10 or 100, then add 1) and the link between "
                "addition and subtraction: 32 − 23 = 9, 56 − 47 = 9, 877 − 778 = 99, 666 − 567 = 99."},
    {"item": "Number grids",
     "printed_solution": "The book prints no answers and does not say which way a row or column is read.",
     "correct": "Rows are read left to right and columns top to bottom. Each grid has many answers (42, 42, 42, 60, 60); "
                "any valid grid is accepted and one is shown."},
    {"item": "Palindromes between 900 and 1,200",
     "printed_solution": "The book prints no answer.",
     "correct": "909 to 999 (ten numbers) and the four digit numbers 1,001 and 1,111: twelve in all. Between 100 and "
                "200: ten. Between 25,000 and 27,000: twenty (25,052 to 25,952 and 26,062 to 26,962)."},
    {"item": "Paired arrangements for 18 and 23",
     "printed_solution": "The picture shows 18 as two rows of 9 and 23 as a row of 12 and a row of 11.",
     "correct": "Counted on the page. Adding 2 to 18 adds one more pair, so no counter is left over; adding 2 to 23 "
                "adds one more pair and the single counter is still left over."},
    {"item": "Jincy's coins",
     "printed_solution": "The book asks for the possible combinations and prints no answer.",
     "correct": "A systematic search gives 11 combinations of coins of 1, 2 and 5 rupees with at most 8, 9 and 5 coins "
                "that make 38 rupees; the plan lists them and shows two or three as the sample."},
    {"item": "Raghu's torch",
     "printed_solution": "The book asks about the 23rd press and for the presses that give ON and OFF.",
     "correct": "The torch is OFF at the start. Odd presses give ON and even presses give OFF, so the 23rd press gives ON."},
    {"item": "Mountain climbing and Math Metric Mela",
     "printed_solution": "The book prints no answers.",
     "correct": "Highest peak Mount Everest, 8,848 metres; highest minus lowest 8,848 − 5,642 = 3,206 metres; Elbrus and "
                "Kanchenjunga 8,586 − 5,642 = 2,944 metres; born in 2013 − 20 = 1993. Certificates: Chittoor 121 extra, "
                "Jaunpur 222 short, Raigad 889 extra."},
    {"item": "Real people in the questions",
     "printed_solution": "Priyanka Mohite, Virat Kohli and Sachin Tendulkar are named by the book.",
     "correct": "The plan quotes the book's data and adds no fact about them; a video must follow the real-person rule."},
    {"item": "Numbering of solved examples and the unnumbered questions on the subtraction page",
     "printed_solution": "The book does not number its solved examples; its eight bare subtractions are numbered 2 to 9.",
     "correct": "The plan numbers the seven printed solved examples 1 to 7 in book order and letters the eight "
                "subtractions (a) to (h)."},
    {"item": "Unprinted commas and the unit l",
     "printed_solution": "The book prints 1301 and 2700 without a comma, and writes litres as l.",
     "correct": "The plan writes 1,301 and 2,700, and writes litres in full."},
    {"item": "Brief: revision video",
     "printed_solution": "The brief asks for an interactive recap or revision video.",
     "correct": "The pipeline has no recap video, so the last topic is a text summary with short concept checks."},
    {"item": "Open prompts (discussion, sample pairs, easier ways)",
     "printed_solution": "No single answer.",
     "correct": "The plan gives one reasoned sample answer and says the student's answer may differ."},
]
ERRATA = []

DESIGN_REFERENCES = [
    {"text": "priority_doc.md (the plan written to the 'Class 5 Mathematics Learning Experience Designer' brief): topic "
             "flow, video types, the 8 tools, the shared visual language and the learning rules decide this chapter's "
             "design.", "url": ""},
    {"text": "docs/01_runbook.md and .claude/skills/lp/SKILL.md: framing intro with a free-try tool, idea topics each "
             "ending in a Practice concept, a Questions topic after every idea topic with a question concept and an "
             "answer concept per book question, and one summary topic.", "url": ""},
]

# The figures that carry mathematics, keyed by authored concept key. One concept image per teaching, hook and summary
# concept where a drawn figure is the maths (two for a merged concept with two labelled sections: one sentence per
# image, IMG1 then IMG2); the tool concepts (Practice / free try) are pictured by their tool.
FIGURES = {
    "T1.C1": ["Two groups of four number cards on small slips of paper side by side, 1, 2, 7, 9 and 3, 4, 5, 9, with "
              "the sums 19 and 21 written under them."],
    "T1B.C1": ["Two groups of three cards, 2, 6, 9 with the sum 17 and 4, 7, 10 with the sum 21, the gap 4 between the "
               "sums, and a double arrow between the 2 and the 4 with the new sums 19 and 19."],
    "T2.C1": ["A fuel display with a place value chart of hundreds, tens and ones for 67 + 58 with the carries and the "
              "sum 125 litres."],
    "T2B.C1": ["A road with the milestones 54, 152 and 154, a long hop of 100 from 54 to 154 and a short hop back of 2 "
               "to 152."],
    "T3.C1": ["Section A: a bar for 63 split into 35 and 28, with the four sentences 35 + 28 = 63, 28 + 35 = 63, "
              "63 − 28 = 35 and 63 − 35 = 28.",
              "Section B: a tens and ones chart for 72 − 38 with 1 ten traded for 10 ones, the difference 34 and the "
              "check 38 + 34 = 72."],
    "T4.C1": ["Three rows of stepping stones, 10, 11, 12 and 11, 12, 13 and 12, 13, 14, each with its running total, "
              "ending in the sums 33, 36 and 39 with the difference 3 between successive sums."],
    "T4B.C1": ["The run 41 + 42 + 43 + 44 + 45 with arrows joining 41 and 45, and 42 and 44, each pair making 86, and "
               "the middle number 43."],
    "T5.C1": ["Section A: a chart of thousands, hundreds, tens and ones for 3,486 + 2,729 with the digits lined up, the "
              "carries and the sum 6,215.",
              "Section B: a chart of thousands, hundreds, tens and ones for 6,402 − 2,758 with the trades across the "
              "zero and the difference 3,644."],
    "T6.C1": ["Section A: a road with four stops and the amounts of a traveller's trip: start 15,000 rupees, spends "
              "4,250, gets 2,000, spends 3,160, and 9,590 left (practice values).",
              "Section B: three amounts of money, each rounded up to the next thousand, with the rounded total 45,000 "
              "beside the 50,000 rupees to be spent (practice values)."],
    "T7.C1": ["Section A: the sum 46 + 53 = 99 with an arrow +1 giving 46 + 54 = 100.",
              "Section B: a number line with a hop back of 10 from 52 to 42 and a short hop forward of 1 to 43."],
    "T8.C1": ["The digits of 2,442 joined by mirror arcs, first with last and second with third, and the four numbers "
              "303, 313, 323 and 333."],
    "T9.C1": ["Two 2 by 2 grids with the arrow words written the way the book writes them: inc beside the rows and "
              "under the columns, with 1 top left and 4 bottom right and two blanks; and inc beside the rows and dec "
              "under the columns, with 4 top right and 1 bottom left and two blanks."],
    "T10.C1": ["Counters in two rows: 14 counters in 7 pairs and 15 counters in 7 pairs with one left over."],
    "T10B.C1": ["Two groups of counters, 9 and 13, each with one left over, and the two leftovers joining into one "
                "pair."],
    "T11.C1": ["A coin mat of the four ways to pay 12 rupees with coins of 5, 2 and 1 rupees, from a purse of 2 five "
               "rupee coins, 3 two rupee coins and 4 one rupee coins."],
    "T11B.C1": ["A row of eight torch pictures for presses 1 to 8, alternately ON and OFF."],
    "T12.C1": ["Section A: a bus information board with a table of three buses, their distances and years bought "
               "(practice values).",
               "Section B: two pairs of bars, tickets printed against people who came, with the difference marked "
               "as short in the first pair and extra in the second."],
    "T13.C1": ["A winding road with fifteen signposts, one for each main idea of the chapter, each with a short "
               "label."],
}
