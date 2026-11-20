# -*- coding: utf-8 -*-
"""Chapter-level content for Class 5 Chapter 6, The Dairy Farm (Maths Mela, Grade 5, Chapter 6).

The plan follows the "Class 5 Mathematics Learning Experience Designer" brief (priority_doc.md sections A to F) and the
/lp pipeline's structure; the book decides every number and every question. Book lines are verbatim except: the book's
dashes become commas, colons or "to"; minus is U+2212; the blanks are ___; the book's unlettered boxes and arrangements
are lettered in reading order. No em dash and no en dash anywhere here."""
from __future__ import annotations

CHAPTER = {
    "grade": 5,
    "label": "Class 5",
    "chapter_no": 6,
    "name": "The Dairy Farm",
    "book_part": "Maths Mela, Grade 5, Chapter 6",
    "source_pdf": "textbooks/class-5/eemm106.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Equal Groups, Order and Place Value",
     "Packing a total in equal groups, why the order of the numbers does not change a product, and multiplying by 10, "
     "100 and 1,000 by moving digits in the place value table."),
    ("M2", "Smart Ways to Multiply",
     "Splitting a number into parts, halving one number and doubling the other, using a friendly nearest multiple, "
     "and choosing the easy way for the numbers at hand."),
    ("M3", "Multiplying Larger Numbers",
     "Multiplying with a box, with four lines and with two lines, then place by place with carries, and checking "
     "a worked multiplication for slips."),
    ("M4", "Equal Products, Estimates, Puzzles and Patterns",
     "Finding equal products without calculating, growing from a known product, estimating, digit puzzles, the King's "
     "Reward, patterns in products, mixed word problems and a revision of the whole dairy."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter takes place on a village dairy farm. Pouches of butter milk, packets of butter, cows, ghee jars "
             "and the compost pit are the things we count, and packing them in groups shows how to multiply in many "
             "ways. A short video explains each idea, and an interactive tool lets the student try it alone.",
    "points": [
        {"title": "Videos teach, tools explore",
         "text": "Every idea has one short concept video. The tool that follows is where the student explores, "
                 "builds and checks the idea alone, with hints, retry and reset. Six tools, each with its own "
                 "purpose, follow the chapter's own plan."},
        {"title": "A tool in three steps",
         "text": "Each tool opens with a short recall of the video idea, then lets the student play and apply it, and "
                 "ends with the chapter's own question, used exactly as the book gives it."},
        {"title": "Every book question has its own video",
         "text": "Every solved example, Let Us Do, Let Us Solve and Let Us Think question and every answerable prompt "
                 "of the book is its own short video with a step by step solution and a question picture and a "
                 "solution picture, in a Questions topic that follows the idea it practises."},
        {"title": "The picture is the mathematics",
         "text": "Arrays of pouches, place value boards, boxes and carry columns carry each idea: equal rows, clear "
                 "columns, the numbers as the largest thing on screen."},
        {"title": "Only the book's numbers",
         "text": "Arrays, tables and every question are the book's own. Any number the plan adds is a practice value "
                 "and is said to be one."},
    ],
}

# {module_id: strand letter}: the subject strand each module belongs to (core/qt.py builds every objective's strand).
# CBSE maths catalog: N Number, A Algebra, G Geometry, M Measurement, D Data, S Statistics and Probability.
MODULE_STRANDS = {"M1": "N", "M2": "N", "M3": "N", "M4": "N"}

# every book item, with its kind. Home concepts are listed in DESIGN.md section 3.
NCERT_ITEMS = [
    ("open.intro", "text"), ("lt.shapes", "prompt"), ("lt.digits", "prompt"),
    ("lt.pouches", "prompt"), ("lt.number", "prompt"), ("lt.make", "prompt"),
    ("ord.text", "text"), ("ord.pairs", "prompt"), ("ord.zero", "prompt"),
    ("pat.note", "text"), ("pat.q1", "exercise"), ("pat.order", "text"),
    ("pat.q2", "exercise"), ("pat.q2b", "exercise"), ("pat.thousand", "prompt"),
    ("pat.tk", "exercise"), ("pat.th", "exercise"), ("many.18x5", "prompt"),
    ("dh.intro", "text"), ("ex.dh", "example"), ("dh.b", "prompt"),
    ("dh.c", "exercise"), ("dh.why", "talk"), ("dh.d", "exercise"),
    ("dh.e", "prompt"), ("nm.intro", "text"), ("ex.nm4", "example"),
    ("ex.nm14", "example"), ("nm.c", "prompt"), ("nm.d", "exercise"),
    ("ls1.q1", "exercise"), ("ls1.q2", "exercise"), ("ls1.q3", "exercise"),
    ("ls1.q4", "exercise"), ("ls1.q5", "exercise"), ("ls1.q6", "exercise"),
    ("ex.wc12", "example"), ("ex.compost", "example"), ("wc.same", "talk"),
    ("wc.note", "text"), ("lm.a", "exercise"), ("lm.b", "exercise"),
    ("ld1.q1", "exercise"), ("ld1.q2", "exercise"), ("ld1.q3", "exercise"),
    ("ld1.q4a", "exercise"), ("ld1.q4b", "exercise"), ("ld1.q4c", "exercise"),
    ("ld1.q4d", "exercise"), ("ld1.q4e", "exercise"), ("dc.remember", "text"),
    ("dc.fact", "text"), ("ex.dc1", "example"), ("dc.discuss", "talk"),
    ("ex.dc2", "example"), ("dc.note", "text"), ("ex.dc3", "example"),
    ("ls2.q1", "exercise"), ("ls2.q2", "exercise"), ("ls2.q3a", "exercise"),
    ("ls2.q3b", "exercise"), ("ck.a", "prompt"), ("ck.b", "prompt"),
    ("ck.c", "prompt"), ("ck.d", "prompt"), ("ck.e", "prompt"),
    ("ld2.q1", "exercise"), ("ld2.q2", "exercise"), ("ld2.q3", "prompt"),
    ("ld2.q4", "exercise"), ("lt2.abc", "prompt"), ("lt2.def", "prompt"),
    ("lt2.ghi", "prompt"), ("lt2.q2", "prompt"), ("kr.text", "text"),
    ("kr.choose", "prompt"), ("kr.calc", "prompt"), ("mp.q1a", "exercise"),
    ("mp.q1b", "exercise"), ("mp.q2", "exercise"), ("mp.pairs_def", "text"),
    ("mp.pairs", "prompt"), ("ls3.q1", "exercise"), ("ls3.q2", "exercise"),
    ("ls3.q3", "exercise"), ("ls3.q4", "exercise"), ("ls3.q5", "exercise"),
    ("ls3.q6", "exercise"), ("summary", "text"),
]

MISCONCEPTIONS = [
    ("M_ONE_WAY", "A total can be packed in equal groups in only one way, so 60 pouches can only be 30 groups of 2."),
    ("M_ORDER_CHANGES", "Changing the order of the numbers changes the product, so 9 × 0 is not the same as 0 × 9."),
    ("M_ZERO_TIMES", "A number times 0 is the number itself, so 9 × 0 = 9."),
    ("M_ZERO_COUNT", "To multiply tens or hundreds you multiply the digits and forget the zeros, so 30 × 20 = 6."),
    ("M_ADD_ZERO", "Multiplying by 10 just means writing a zero at the end, with no idea that every digit moves one "
                   "place to the left."),
    ("M_HALVE_BOTH", "To halve and double, halve both numbers, so 14 × 6 becomes 7 × 3."),
    ("M_DOUBLE_BOTH", "Doubling both numbers keeps the product the same, so 6 × 8 = 12 × 16."),
    ("M_NO_ADJUST", "Rounding is enough: 4 × 19 = 4 × 20 = 80, with nothing taken away."),
    ("M_WRONG_STRIP", "To get 17 × 24 from 17 × 23 you add 23, the number that was already multiplied."),
    ("M_SPLIT_ONE", "When a number is split into parts, only one of the parts needs to be multiplied."),
    ("M_MISSING_ZERO", "The line for the tens digit needs no zero at the end, so 70 × 193 is written as 7 × 193."),
    ("M_CARRY_FIRST", "A carry is added to the digit before it is multiplied: for 4 × 68, add 3 to 6 and then "
                      "multiply."),
    ("M_PLACE_SLIP", "The 2 in 203 stands for 2 tens, so 203 is 20 + 3."),
    ("M_ESTIMATE_EXACT", "An estimate has to be exactly equal to the product."),
    ("M_START_MOST", "The choice that starts with the most coins always ends with the most coins."),
    ("M_MULT_ALL", "In a word problem you multiply every pair of numbers you see."),
]

SOLUTION_NOTES = [
    {"item": "Opener (LUT Q1 shapes)",
     "printed_solution": "The book does not say whether two different shapes may stand for the same number, and prints no answer.",
     "correct": "The plan reads: different shapes stand for different numbers from 1 to 24. Then 5 full sets fit; the "
                "pentagon is always 1 and the sentence (f) holds whenever (a) and (e) hold. One set is shown and the "
                "student's own set may differ."},
    {"item": "Opener (LUT Q3 pouches)",
     "printed_solution": "The four arrangements carry no letters and the book does not say which number counts the groups.",
     "correct": "The plan letters them (a) to (d) and reads number of groups × group size, as the done example 30 × 2 = 60 "
                "(30 pairs) shows: (b) 20 × 3, (c) 6 × 10, (d) 5 × 12."},
    {"item": "Opener (LUT Q4 which number am I)",
     "printed_solution": "Clue (d) odd number and clue (g) ones digit even contradict each other; no answer is printed.",
     "correct": "No number meets all eight clues. Leaving out (d), exactly 18 fits. The plan answers 18 and says that "
                "(d) cannot be used with (g)."},
    {"item": "Opener (LUT Q5 make your own numbers)",
     "printed_solution": "The book does not say whether the same tile may be used twice and prints no answer.",
     "correct": "The plan reads two different tiles and a whole-number answer: 0 and 19 cannot be made; with three "
                "numbers 0 = (100 ÷ 25) − 4 and 19 = 25 − (10 − 4). Sample answers say the student's answer may differ."},
    {"item": "Order of Numbers (p. 72) lettering",
     "printed_solution": "The letters a, b, e, f, g are printed; the pair of big arrays has no letter.",
     "correct": "The plan keeps the printed letters and calls the unlettered pair the two big arrays."},
    {"item": "Patterns in Multiplication by 10s and 100s, Q1 (h) and (i)",
     "printed_solution": "Each has two blanks after the given line (g) 3 × 100 = 100 × 3 = 300.",
     "correct": "The plan reads the blanks as the swapped product and the answer: 8 × 100 = 100 × 8 = 800 and "
                "10 × 100 = 100 × 10 = 1,000."},
    {"item": "Patterns, Q2: 700 × 4 in the boxes and 700 × 8 in the table",
     "printed_solution": "The boxes and the first table print different problems.",
     "correct": "The plan solves both as printed: 700 × 4 = 2,800 and 700 × 8 = 5,600."},
    {"item": "Tables on p. 74",
     "printed_solution": "5 × 7,000 is printed in both tables.",
     "correct": "Kept as printed; it is 35,000 in both."},
    {"item": "Doubling and halving, nearest multiple: no question sentence",
     "printed_solution": "The book prints the solved working and a prompt (Discuss why these are the same; find why we "
                         "need to subtract 4 or add 14), but no question sentence.",
     "correct": "The plan words each question from the printed working and prompt."},
    {"item": "Doubling and halving (c): the box 35 × 14",
     "printed_solution": "The arrows carry no Half and Double labels.",
     "correct": "The plan halves 14 and doubles 35 (70 × 7 = 490), because 35 cannot be halved into a whole number."},
    {"item": "Let Us Do Q4 (a) cinema",
     "printed_solution": "'If 3 more rows get filled' is not explained.",
     "correct": "Read as 3 more full rows of 12 people on top of the 48 who were watching: 48 + 36 = 84."},
    {"item": "Let Us Do Q4 (b) cricket",
     "printed_solution": "The book does not say whether extras count in the team's runs.",
     "correct": "A team's score includes extras: 96 + 108 + 234 + 23 = 461."},
    {"item": "Note on p. 83 (574 × 125)",
     "printed_solution": "The note says 2 Tens × 574 = 2 × 3,740.",
     "correct": "20 × 574 = 2 × 5,740 = 11,480. 3,740 is a printed slip; the plan uses 5,740."},
    {"item": "Check, Check! (p. 85)",
     "printed_solution": "Pankaj's total 135 is not the sum of his lines (92 + 115 = 207) and Asher's 5,018 is not the sum "
                         "of his rows (1,878 + 1,252 + 1,878 = 5,008).",
     "correct": "Asma's and Lado's solutions are correct; Pankaj's, Kira's and Asher's are not. The plan names every "
                "error, including the wrong additions, and gives the right products 10,962, 52,496 and 202,198."},
    {"item": "Let Us Do p. 86 Q1 boxes",
     "printed_solution": "The eight boxes carry no letters; 'and' joins two products.",
     "correct": "The plan letters the boxes (a) to (h) in reading order and reads 'and' as plus."},
    {"item": "Let Us Do p. 87 Q4 (e)",
     "printed_solution": "'8 × 9 = 72' is printed with an uneven gap.",
     "correct": "Read as 8 × 9 = 72, the given fact for (f), (g) and (h)."},
    {"item": "Let Us Think Q1 (a) to (i) digit boxes",
     "printed_solution": "The book prints no answers. In (a) to (c) the answer boxes are orange and the top boxes have a "
                         "black border.",
     "correct": "The plan reads each colour as one digit and the black boxes as free digits. (a) 3, 6 or 9; (b) 3 to 9; "
                "(c) 3, 6 or 9; (d) ten sets; (e) 110 × 5 = 550; (f) 2222 × 5 and 3332 × 5; (g) eight sets with a green 0; "
                "(h) 857 × 7 = 5,999; (i) no answer, so a printed colour slip is possible."},
    {"item": "The King's Reward (p. 88 to 89)",
     "printed_solution": "'For 7 days' does not say whether the start counts as day 1.",
     "correct": "The plan reads 7 multiplications after the starting coins: 640, 6,561 and 78,125. With 6 "
                "multiplications (320, 2,187, 15,625) Minister 3 still wins. 'Which reward would you have chosen?' is "
                "an opinion; the plan gives a reasoned sample and says it may differ."},
    {"item": "Number pairs (p. 90)",
     "printed_solution": "'Any two adjacent numbers in a row or a column.'",
     "correct": "Only pairs joined by a line count: 12 pairs. Smallest 11 × 14 = 154, largest 35 × 75 = 2,625."},
    {"item": "Let Us Solve Q3 Ananya (p. 91)",
     "printed_solution": "The total does not say that every row has as many students.",
     "correct": "Her own row is counted (30 rows, 41 in her row) and every row is taken to have 41 students: 1,230. "
                "Assumption stated in the solution."},
    {"item": "Let Us Solve Q2 football (p. 91)",
     "printed_solution": "'The teams paid ₹1,750 in total to rent the ground and ₹1,129 for food and water.'",
     "correct": "Both are expenses: ₹2,879. The question does not ask for the profit."},
    {"item": "Brief: revision video",
     "printed_solution": "The brief asks for an interactive recap or revision video.",
     "correct": "The pipeline has no recap video, so the last topic is a text summary with short concept checks."},
    {"item": "Open prompts (examples of your own, number pairs reasoning, which choice, discussions)",
     "printed_solution": "No single answer.",
     "correct": "The plan gives one reasoned sample answer and says the student's answer may differ."},
    {"item": "Book examples have no numbers",
     "printed_solution": "The book's solved examples (halving 3 × 18, nearest multiple 4 × 19 and 14 × 21, kitchen waste, "
                         "compost, cows, Gir milk, ghee) are not numbered.",
     "correct": "The plan numbers them Example 1 to Example 8 in book order."},
]
ERRATA = []

DESIGN_REFERENCES = [
    {"text": "priority_doc.md (the plan written to the 'Class 5 Mathematics Learning Experience Designer' brief, "
             "2026-11-06): topic flow, video types, the 6 tools, the shared visual language and the learning rules "
             "decide this chapter's design.", "url": ""},
    {"text": "docs/01_runbook.md and .claude/skills/lp/SKILL.md: framing intro with a free-try tool, idea topics each "
             "ending in a Practice concept, a Questions topic after every idea topic with a question concept and an "
             "answer concept per book question, and one summary topic.", "url": ""},
]

# The book's own figures that carry mathematics, keyed by authored concept key. One concept image per teaching,
# hook and summary concept where a drawn figure is the maths; the tool concepts (Practice / free try) are pictured by
# their tool. Numbers here are the PLAN's own practice values, never a book question's numbers.
FIGURES = {
    "T1.C1": ["Two panels of the same 60 butter milk pouches on a packing table: in the left panel 30 rings of 2 pouches, "
              "in the right panel 20 rings of 3 pouches. No numbers written."],
    "T1B.C1": ["36 pouches packed in two ways: 4 rows of 9 and the same pouches turned as 9 rows of 4."],
    "T2.C1": ["Two arrays of butter packets: 7 rows of 12 and 12 rows of 7, with the number of groups and the group "
              "size marked."],
    "T3.C1": ["A place value board with 37 in the tens and ones columns and then 370 and 3,700 with every digit moved "
              "left."],
    "T3.C2": ["6 rows of 7 hundred-blocks (42 hundreds) beside the sentence 60 × 70."],
    "T4.C1": ["An array of 6 rows of 14 packets split by a line into a block of 10 columns and a block of 4 columns."],
    "T5.C1": ["An array of 8 rows of 13 packets cut across the middle into two blocks of 4 rows, and the two blocks "
              "placed side by side as 4 rows of 26."],
    "T6.C1": ["An array of 6 rows of 19 squares inside a frame of 6 rows of 20, the missing strip of 6 squares shown "
              "dashed."],
    "T8.C1": ["A box with columns 20 and 3 and rows 10 and 4, the four cells 200, 30, 80 and 12, the column sums 280 and "
              "42 and the total 322."],
    "T8.C2": ["The same four small products shown as four lines (Kanti) and as two lines (John) for 26 × 13."],
    "T9.C2": ["A place value ledger for 176 × 24 with the carry circles, two rows of small products and the total 4,224."],
    "T11.C2": ["An array of 7 rows of 14 squares with one extra column of 7 squares coloured and, beside it, the same array "
               "with one row of 14 squares removed."],
    "T16.C1": ["A village dairy counter with a pouch crate, a butter packet tray, a place value board, a box, and a "
               "ledger, one for each idea of the chapter."],
}
