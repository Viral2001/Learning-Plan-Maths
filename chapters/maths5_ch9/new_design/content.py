# -*- coding: utf-8 -*-
"""Chapter-level content for Class 5 Chapter 9, Coconut Farm (Maths Mela, Grade 5, Chapter 9).

The plan follows the "Class 5 Mathematics Learning Experience Designer" brief (priority_doc.md sections A to F) and the
/lp pipeline's structure; the book decides every number and every question. Book lines are verbatim except: the book's
dashes become commas, colons or "to"; minus is U+2212; the division sign is U+00F7 and the times sign U+00D7; a division
that leaves a remainder is never written as one chain "n ÷ d = q" (the equation gate would call it false), it is written
"quotient q, remainder r" and "n = d × q + r". No em dash and no en dash anywhere here."""
from __future__ import annotations

CHAPTER = {
    "grade": 5,
    "label": "Class 5",
    "chapter_no": 9,
    "name": "Coconut Farm",
    "book_part": "Maths Mela, Grade 5, Chapter 9",
    "source_pdf": "textbooks/class-5/eemm109.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Division Facts and Patterns",
     "Every multiplication fact gives two division facts, a dividend is a divisor times a quotient, and dividing tens, "
     "hundreds and thousands follows the table facts and the place value pattern."),
    ("M2", "Smart Ways to Divide",
     "Dividing in the head by splitting the number or halving, dividing by taking away groups of the divisor (partial "
     "quotients) on Susie and Sunitha's farm, and the remainder rule N = D × Q + R."),
    ("M3", "Place Value Division and Problems",
     "Dividing by regrouping hundreds, tens and ones, solving word problems with remainders, bills and several steps, "
     "and seeing how the quotient changes when the dividend or the divisor changes."),
    ("M4", "Mathematical Statements and Revision",
     "Checking that both sides of an equal sign have the same value, deciding when a statement is always, sometimes or "
     "never true, and a revision of the whole farm of division."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter takes place on Susie and Sunitha's coconut farm in Kerala. Arrays of coconuts, bags, crates, "
             "oil, husk and a market stall carry every division, from the two division facts of one multiplication fact "
             "to dividing thousands by a two-digit number with a remainder. A short video explains each idea, and an "
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
         "text": "Every solved example, Let Us Do and Let Us Solve question and every answerable prompt of the book is "
                 "its own short video with a step by step solution and a question picture and a solution picture, in "
                 "a Questions topic that follows the idea it practises."},
        {"title": "Two ways to divide, side by side",
         "text": "Susie takes away many small groups and Sunitha takes away the biggest groups that fit. The chapter "
                 "also divides by place value. The student sees that every method gives the same quotient and the "
                 "same remainder, and checks each answer with N = D × Q + R."},
        {"title": "Only the book's numbers",
         "text": "Every number on the farm, in a bill or in a word problem is the book's own. Any number the plan adds "
                 "to teach an idea is a practice value and is said to be one."},
    ],
}

# {module_id: strand letter}: the subject strand each module belongs to (core/qt.py builds every objective's strand).
# CBSE maths catalog: N Number, A Algebra, G Geometry, M Measurement, D Data, S Statistics and Probability.
MODULE_STRANDS = {"M1": "N", "M2": "N", "M3": "N", "M4": "N"}

# every book item, with its kind. Home concepts are listed in DESIGN.md section 3.
NCERT_ITEMS = [
    # the opener and division facts (pp. 119 to 120)
    ("open.story", "text"),
    ("div.example", "example"), ("div.facts", "text"), ("div.nqd", "text"),
    ("div.one", "prompt"), ("div.array2", "prompt"),
    ("play.times", "prompt"), ("play.divide", "prompt"),
    ("lud1.q1", "exercise"),
    # patterns in division and place value (pp. 121 to 122)
    ("pd.q2", "exercise"), ("pd.patterns", "prompt"), ("pd.notice", "talk"),
    ("pd.chart_left", "prompt"), ("pd.chart_right", "prompt"), ("pd.quotients", "talk"),
    ("lud2.q1", "exercise"), ("lud2.q2", "exercise"), ("lud2.q3", "exercise"), ("lud2.q3b", "exercise"),
    ("lud2.q4", "exercise"), ("lud2.q5", "exercise"),
    # mental strategies (pp. 123 to 124)
    ("ms.ex1", "example"), ("ms.ex2", "example"), ("ms.ex3", "example"),
    ("ms.five", "prompt"), ("ms.halving", "prompt"),
    ("try.split", "exercise"), ("try.halve", "exercise"), ("ls.a_h", "exercise"),
    # Susie's farm, remainders (pp. 124 to 126)
    ("sf.text", "text"), ("sf.q1", "example"), ("sf.estimate", "talk"), ("sf.discuss", "talk"),
    ("sf.bags", "example"), ("sf.q2", "example"),
    ("ld.726", "prompt"), ("ld.902", "prompt"), ("ld.rule", "text"), ("ld.relation", "prompt"),
    ("ls1.q5", "exercise"),
    # Kalpavruksha Coconut Oil (pp. 126 to 128)
    ("oil.text", "text"), ("oil.q1", "example"), ("oil.earn", "prompt"), ("oil.husk", "example"),
    ("oil.hint", "talk"), ("oil.tender", "prompt"), ("oil.extra", "prompt"),
    # division using place value and Let Us Divide (pp. 128 to 134)
    ("pv.text", "text"), ("pv.ex1", "example"), ("pv.ex2", "example"), ("pv.ex3", "example"), ("pv.zero", "talk"),
    ("pv.ex4", "example"), ("pv.digits", "prompt"),
    ("ldv.a", "prompt"), ("ldv.b", "prompt"), ("ldv.zero", "talk"), ("ldv.c", "prompt"), ("ldv.d", "prompt"),
    ("ldv.compare", "talk"),
    ("lud3.q1", "exercise"), ("lud3.riddle", "prompt"),
    ("vm.q1to6", "exercise"), ("vm.q7to12", "exercise"),
    # word problems, remainders and bills (pp. 126, 132 to 134)
    ("ls1.q1", "exercise"), ("ls1.q2", "exercise"), ("ls1.q3", "exercise"), ("ls1.q4", "exercise"),
    ("ls2.q1", "exercise"), ("ls2.q2", "exercise"), ("ls2.q3", "exercise"), ("ls2.q4", "exercise"),
    ("ls2.q6", "exercise"), ("ls2.q7", "exercise"), ("ls2.q8", "exercise"),
    ("vm.text", "text"), ("vm.table", "prompt"), ("vm.info", "talk"), ("vm.activity", "talk"),
    # how the quotient changes (p. 132)
    ("ls2.q5a", "exercise"), ("ls2.q5b", "exercise"), ("ls2.q5c", "exercise"),
    # mathematical statements (p. 135)
    ("st.def", "text"), ("st.q1", "exercise"), ("st.q2", "exercise"),
    ("st.labels", "text"), ("st.q3a", "exercise"), ("st.q3b", "exercise"), ("st.q3c", "exercise"),
    ("st.q4", "exercise"),
    ("summary", "text"),
]

MISCONCEPTIONS = [
    ("M_DIV_COMMUTES", "A division fact works in either order, so 35 ÷ 7 and 7 ÷ 35 both give 5."),
    ("M_DIV_SHRINKS", "Dividing always makes a number smaller, so 35 ÷ 1 must be less than 35."),
    ("M_ZEROS_LOST", "When a number ends in zeros, dividing makes the zeros disappear, so 400 ÷ 10 = 4."),
    ("M_BAD_SPLIT", "Any split of the dividend is a convenient split, even a part the divisor does not divide "
                    "easily."),
    ("M_ROUND_WRONG", "When you round the dividend up to an easy number you can forget to take the extra away from "
                      "the answer."),
    ("M_TOO_BIG_GROUP", "You can take away a group that is bigger than the number left."),
    ("M_REMAINDER_BIG", "The remainder can be as big as the divisor or bigger, so 902 = 16 × 55 + 22 is a finished "
                        "division."),
    ("M_DROP_REMAINDER", "The remainder can always be ignored in a word problem, so 97 coconuts in bags of 25 need "
                         "only 3 bags."),
    ("M_ZERO_SKIPPED", "A zero in the quotient can be left out, so 324 ÷ 3 = 18."),
    ("M_DIGITS_SAME", "The quotient always has as many digits as the dividend."),
    ("M_DIVISOR_DOUBLE", "If the divisor is doubled, the quotient is doubled too."),
    ("M_EQUAL_ANSWER", "The = sign means the answer comes next, so 8 × 9 = 70 + 2 is false because 70 + 2 is not a "
                       "single number written as the answer."),
    ("M_ONE_EXAMPLE", "One example that works is enough to show that a statement is always true."),
    ("M_SUB_ORDER", "Changing the order of the numbers in a subtraction makes no difference."),
    ("M_HALF_EVEN", "Halving a number always gives an even number."),
    ("M_ALWAYS_ENOUGH", "Every word problem can be solved with the numbers it gives."),
    ("M_UNIT_MIX", "Kilograms and grams can be subtracted or divided as plain numbers without changing the unit."),
]

SOLUTION_NOTES = [
    {"item": "Coverage of the book's Notes for Teachers (pages 120, 122, 125, 129)",
     "printed_solution": "Four boxes addressed to the teacher.",
     "correct": "They are not student questions, examples or activities, so they are not coverage items. The plan "
                "does not give a classroom teacher a teaching role. What they ask for (the link between "
                "multiplication and division, tens and hundreds patterns, partial quotients and place value) is "
                "taught by the concept videos and tools."},
    {"item": "Opener page (no printed number)",
     "printed_solution": "The first page of the chapter carries no page number.",
     "correct": "It is page 119 by sequence, because the next page prints 120."},
    {"item": "Let Us Do on division facts, Q1: 30 × 30",
     "printed_solution": "The book asks for two division statements in each case.",
     "correct": "30 × 30 = 900 gives only one division statement, 900 ÷ 30 = 30, because both numbers are the same. "
                "The plan writes it once and says so."},
    {"item": "Let Us Play (circles and squares)",
     "printed_solution": "The book prints no answer, and many pairs of numbers fit.",
     "correct": "The plan gives one reasoned sample pair for each shape and says the student's pair may differ. For the "
                "quotient shapes it uses small whole-number pairs (a number and 1 is allowed)."},
    {"item": "Let Us Do on patterns, Q4 (the hexagon puzzle)",
     "printed_solution": "The book prints no answer. The four equations are read from the picture as: top row A ÷ B = "
                         "C, the left column A − D = F, the right column C × E = H and the bottom row F + G = H.",
     "correct": "Exactly two solutions exist, found by trying every placement of 1 to 8: first 6 ÷ 3 = 2, 6 − 5 = 1, "
                "2 × 4 = 8 and 1 + 7 = 8, and second 8 ÷ 4 = 2, 8 − 7 = 1, 2 × 3 = 6 and 1 + 5 = 6. The book's own question "
                "'Is there more than one answer?' is answered yes, two."},
    {"item": "Let Us Do on patterns, Q3 (the Diwali gift)",
     "printed_solution": "The book asks three questions: the share of each of 5 employees, what happens with 10 "
                         "employees, and the money needed to give everyone the same amount as before.",
     "correct": "5500 ÷ 5 = 1100; with 10 employees each gets less, 5500 ÷ 10 = 550; to give each of 10 employees "
                "1100 the owner needs 10 × 1100 = 11000 rupees. The plan splits it into two question cards."},
    {"item": "Mental Strategies: 'Can you give 5 such examples' and 'for which other divisors and dividends might "
             "repeated halving work'",
     "printed_solution": "Open prompts with no printed answer.",
     "correct": "The plan gives a sample answer and says the student's answer may differ. Repeated halving works for "
                "divisors 2, 4, 8, 16 (each is made of halvings) when the dividend can be halved that many times."},
    {"item": "Try It! (page 123)",
     "printed_solution": "Boxes for a split are shown with a plus or a minus sign and the divisor under each part, "
                         "but no numbers are given in the boxes.",
     "correct": "The student chooses the split. The plan's sample splits: 64 = 40 + 24, 265 = 250 + 15, 1560 = 1600 − "
                "40, 4824 = 4800 + 24. Q5 halves 168 three times (84, 42, 21) and Q6 halves 144 twice (72, 36); "
                "the third box of Q5 and the second Halve box of Q6 are blank, so the number of halvings is read "
                "from the number of boxes."},
    {"item": "Susie's Farm: 'each person will get 4 bags'",
     "printed_solution": "The book writes each person where the story speaks of each customer.",
     "correct": "Kept as the story's meaning: each customer's 97 coconuts need 4 bags of 25 (3 full bags hold 75, "
                "the other 22 coconuts need one more bag)."},
    {"item": "Let Us Learn to Divide: 726 ÷ 4 and 902 ÷ 16",
     "printed_solution": "Blanks in a partial quotient layout, with margin hints 'Could we have written 200 here?' and "
                         "'Could we have multiplied 16 by a larger tens?'.",
     "correct": "726 ÷ 4: 100 + 80 + 1, quotient 181, remainder 2, and 200 is too big because 4 × 200 = 800 is more than 726. "
                "902 ÷ 16: 50 + 6, quotient 56, remainder 6, and 60 is too big because 16 × 60 = 960 is more than 902."},
    {"item": "Let Us Solve (word problems), Q1: which samosa pack",
     "printed_solution": "No price is given, so the question cannot be settled by cost.",
     "correct": "The plan reads it as: which pack leaves fewer samosas over. 250 samosas in packs of 6 need 42 packs "
                "(252 samosas, 2 extra); in packs of 8 they need 32 packs (256 samosas, 6 extra). Packs of 6 waste "
                "fewer. Sample answer; to be confirmed."},
    {"item": "Let Us Solve (word problems), Q2: 'a maximum of of 41 students'",
     "printed_solution": "The book prints 'of of' (a repeated word) and a space before the question mark.",
     "correct": "Printed-book typing slip. The plan writes 'a maximum of 41 students'. Answer: 342 ÷ 41 gives 8 with "
                "14 students left, so 9 buses."},
    {"item": "Let Us Solve (word problems), Q3: Sofia's notes",
     "printed_solution": "The book asks for the different possible combinations of Rs 50 and Rs 20 notes that make Rs "
                         "520.",
     "correct": "Six combinations: 0 and 26, 2 and 21, 4 and 16, 6 and 11, 8 and 6, 10 and 1 (fifty-rupee notes and "
                "twenty-rupee notes). The book does not say whether both kinds of note must be used, so the plan lists "
                "the combination with no Rs 50 note (26 notes of Rs 20) as the first and says so."},
    {"item": "Let Us Solve (word problems) on page 132, Q1 (a) and (b)",
     "printed_solution": "The book prints 'accomodate' (spelling).",
     "correct": "Printed-book spelling slip, written 'accommodate' in the plan. 475 ÷ 45 gives 10 shows with 25 "
                "people left, so 11 shows; 11 shows at 2 a day need 6 days (5 days seat 10 shows and one more day is "
                "needed)."},
    {"item": "Let Us Solve (word problems) on page 132, Q3: 'how many biscuits can one person have each day.'",
     "printed_solution": "The sentence ends with a full stop instead of a question mark.",
     "correct": "Printed-book punctuation slip, written with a question mark in the plan. 15 × 8 = 120 biscuits; 120 "
                "÷ 6 = 20 for each person for the 4 days; 20 ÷ 4 = 5 biscuits a person each day."},
    {"item": "Let Us Solve (relations), Q5 part B, (c) and (e)",
     "printed_solution": "The book prints 384 ÷ 8 = ___ twice, as (c) and as (e).",
     "correct": "Printed twice; the plan keeps both as printed (both answers are 48) and notes it. It may be a "
                "printing slip for a different division."},
    {"item": "Let Us Solve (word problems) on page 133, Q6: the rally",
     "printed_solution": "The map prints 344 km (Mumbai to Ratnagiri), 232 km (Ratnagiri to Goa) and 576 km in all.",
     "correct": "(a) 576 ÷ 12 = 48 km a day. (b) After Ratnagiri the road left is 232 km, so 232 ÷ 4 = 58 km a "
                "day. The 232 km is read from the map's printed number."},
    {"item": "Let Us Solve (word problems) on page 133, Q7: missing information",
     "printed_solution": "Four problems, each needing something added. The book prints no answer.",
     "correct": "(a) the price of one mango (or of one basket); (b) the total number of desks; (c) nothing is missing, "
                "3500 ÷ 5 = 700 rupees for one bat; (d) the total number of idlis (or the price of one idli). Where "
                "the student needs a number the plan uses a practice value and says so. To be confirmed that (c) is "
                "complete as printed."},
    {"item": "Let Us Solve (word problems) on page 133, Q8: bookshelves",
     "printed_solution": "No answer is printed.",
     "correct": "264 ÷ 4 = 66, 306 ÷ 8 gives 38 (2 left), 2400 ÷ 16 = 150, 120 ÷ 4 = 30, 2800 ÷ 32 gives 87 (16 "
                "left). The smallest is 30 (the large clips), so 30 bookshelves."},
    {"item": "Let Us Do on page 131, Q1 (missing numbers with no remainder)",
     "printed_solution": "Ten boxes, 'there could be more than one solution'. No answers are printed. A divisor box is "
                         "one box wide.",
     "correct": "The plan reads every divisor box as one digit. Answers: 4) 480 (120; 3) 906 (302; 20) 400 (20; "
                "50) 1000 (20; 4) 848 (212 or 4) 868 (217; 3) 936 (312; 1, 2, 4 or 8 for 88 (88, 44, 22, 11); "
                "9_0 has many answers, sample 5) 950 (190; 1) 180 (180; 8) 6480 (810 or 9) 6480 (720."},
    {"item": "Let Us Divide (a) to (d)",
     "printed_solution": "Two layouts for each division (partial quotients and place value) with blanks. In (b) the "
                         "book asks 'Discuss why we have to write this 0 here' and below the page 'Compare both "
                         "solutions. Also, remember to put 0 in the right places.'",
     "correct": "(a) 7,032 ÷ 6: 1000 + 100 + 70 + 2, quotient 1172. (b) 3,005 ÷ 5: 600 + 1, quotient 601 (the 0 holds "
                "the tens place, 0 tens cannot be shared). (c) 2,874 ÷ 14: 200 + 5, quotient 205, remainder 4. (d) "
                "9,805 ÷ 32: 300 + 6, quotient 306, remainder 13."},
    {"item": "Number riddle (page 131): 'I am a 3-digit number'",
     "printed_solution": "The book prints the question and no answer.",
     "correct": "42 × 5 = 210 and 210 × 2 = 420, so the number is 210."},
    {"item": "Vegetable Market table (page 134)",
     "printed_solution": "Four rows with erased numbers, and the question 'What information is recorded in this table?'.",
     "correct": "Radish 26 × 78 = 2,028 rupees; potato 2,240 ÷ 20 = 112 kg; cabbage 32 × 56 = 1,792 rupees; green "
                "peas 3,125 ÷ 125 = 25 rupees for 1 kg; total money 2,028 + 2,240 + 1,792 + 3,125 = 9,185 rupees. "
                "The table records the cost of 1 kg, the kilograms supplied, and the amount for each vegetable."},
    {"item": "Vegetable Market: Activity (bills and role-play)",
     "printed_solution": "A classroom activity: collect bills from shops and read them, and play shopkeeper and customer.",
     "correct": "Kept as a discussion item in the teaching text (what information a bill records). The role-play is a "
                "classroom activity with no answer, so it has no tool and no solution card."},
    {"item": "Mathematical Statements, Q4 (always, sometimes, never)",
     "printed_solution": "A table of five statements with three tick columns and no answers.",
     "correct": "Plan's reading, with whole numbers: adding 10 to a number gives a multiple of ten: sometimes true "
                "(only if the number is a multiple of ten); changing the order in subtraction makes no difference: "
                "sometimes true (only when the two numbers are the same, for example 6 − 6; for two different numbers "
                "the answer changes or cannot be found with whole numbers); doubling one number and halving the other "
                "keeps the product the same: always true; multiplication by an odd number gives an even number: "
                "sometimes true; multiplying a number by 5 leads to numbers with 0 in the ones place: sometimes "
                "true (always 0 or 5). To be confirmed, especially the second."},
    {"item": "Mathematical Statements, Q3 (a), (b), (c)",
     "printed_solution": "The margin names (a) always true, (b) never true, (c) sometimes true. The book asks for "
                         "examples and for a counter-example where one may exist.",
     "correct": "(a) five examples, and no example shows it false (odd + odd is always even); (b) no example exists "
                "(a number times 2 is always even); (c) examples where it holds (halving 8 gives 4) and where it does "
                "not (halving 6 gives 3, halving 10 gives 5)."},
    {"item": "Brief: revision video",
     "printed_solution": "The brief asks for an interactive recap or revision video.",
     "correct": "The pipeline has no recap video, so the last topic is a text summary with short concept checks."},
    {"item": "Open prompts (samples)",
     "printed_solution": "No single answer.",
     "correct": "The plan gives one reasoned sample answer and says the student's answer may differ."},
]
ERRATA = []

DESIGN_REFERENCES = [
    {"text": "priority_doc.md (the plan written to the 'Class 5 Mathematics Learning Experience Designer' brief, "
             "2026-11-06): topic flow, video types, the 8 tools, the shared visual language and the learning rules "
             "decide this chapter's design.", "url": ""},
    {"text": "docs/01_runbook.md and .claude/skills/lp/SKILL.md: framing intro with a free-try tool, idea topics each "
             "ending in a Practice concept, a Questions topic after every idea topic with a question concept and an "
             "answer concept per book question, and one summary topic.", "url": ""},
]

# The book's own figures that carry mathematics, keyed by authored concept key. One concept image per hook and
# teaching concept where a drawn figure is the maths; the tool concepts (Practice / free try) are pictured by their tool.
FIGURES = {
    "T1.C1": ["An array of coconuts, 5 rows of 7, with no fact written."],
    "T1B.C1": ["An array of coconuts, 3 rows of 9, shown as 9 groups of 3 and as 3 groups of 9."],
    "T1B.C2": ["The three numbers of a division fact named: dividend, divisor and quotient."],
    "T2.C1": ["Tens shown as bundles: 270 as 27 bundles of ten, shared into 9 equal groups."],
    "T2.C2": ["A place value chart with Hundreds, Tens and Ones columns and the digit 7 moving one place right each "
              "time the number is divided by 10."],
    "T3.C1": ["A bar for 2856 cut into 2800 and 56, each part divided by 7."],
    "T3.C2": ["A bar for 2994 shown as 3000 with 6 taken away, each divided by 3."],
    "T3.C3": ["A chain of boxes: 264, halve to 132, halve to 66."],
    "T4.C1": ["A bar of 378 coconuts with a block of 360 (6 times 60) and a block of 18 (6 times 3) taken away."],
    "T4.C2": ["A bar of 861 coconuts with blocks 700, 140 and 21 taken away in groups of 7."],
    "T4.C3": ["A bar of 487 coconuts: 486 in 54 groups of 9 and 1 left over."],
    "T5.C1": ["A bar of 6,534 taken away in blocks of 18 times 300, 18 times 60 and 18 times 3."],
    "T6.C1": ["Base ten blocks for 83: 8 tens and 3 ones, shared among 6 plates."],
    "T6.C2": ["Base ten blocks for 412: 4 hundreds, 1 ten, 2 ones, shared among 4 plates with a regrouped ten."],
    "T6.C3": ["Two layouts for 3,648 ÷ 12 side by side, partial quotients and place value."],
    "T7.C1": ["Coconuts in bags of 8: 11 full bags and 6 coconuts left that need a twelfth bag."],
    "T7.C2": ["A bill table with cost of 1 kg, kilograms and total amount, one value missing."],
    "T7.C3": ["Four baskets of 36 coconuts packed into 8 sacks."],
    "T8.C1": ["A rectangle of dividend N with sides divisor D and quotient Q, doubled and halved."],
    "T9.C1": ["A balance with 6 times 5 on one side and 20 plus 10 on the other."],
    "T10.C1": ["Three bins: always true, sometimes true, never true."],
    "T11.C1": ["A farm scene with an array, a bag, a place value chart and a bill, one for each idea."],
}
