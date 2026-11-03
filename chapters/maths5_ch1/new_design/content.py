# -*- coding: utf-8 -*-
"""Chapter-level content for Class 5 Chapter 1, We the Travellers - I (Maths Mela, Grade 5, Chapter 1).

Built on the latest structure: the user's priority doc (priority_doc.md) decides the topic flow, the video types and
the 8 tools; the book decides every number and every question. Book lines are verbatim except: the book's dashes
become commas, colons or "to"; minus is U+2212; blanks in the book's Let Us Do items are solved in the plan.
No em dash and no en dash anywhere in this file."""
from __future__ import annotations

CHAPTER = {
    "grade": 5,
    "label": "Class 5",
    "chapter_no": 1,
    "name": "We the Travellers - I",
    "book_part": "Maths Mela, Grade 5, Chapter 1",
    "source_pdf": "textbooks/class-5/eemm101.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Journeys and Big Numbers",
     "Journeys of the past and today, then the new Ten Thousands place: reading large numbers, writing them from their "
     "names with zeros in the right places, and continuing number patterns."),
    ("M2", "Comparing, Swapping and Rounding Numbers",
     "Comparing and ordering large numbers on a number line, swapping two digits to change a number, breaking numbers "
     "into tens, hundreds and thousands, and finding the nearest ten, hundred and thousand."),
    ("M3", "Large Numbers on the Move and Pastime Mathematics",
     "How far vehicles travel in an hour and how many carry a school, large counts around us, three puzzles on a "
     "train, the King's Horses, and a revision of the whole journey."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter is a journey. It starts with how people travelled long ago and today, then uses travel to make "
             "large numbers real: the new Ten Thousands place, reading and writing numbers, comparing and rounding them, "
             "and finally puzzles that two children play on a train. A short video explains each idea, and an "
             "interactive tool lets the student try it alone.",
    "points": [
        {"title": "Videos teach, tools explore",
         "text": "Every idea has one short concept video. The tool that follows is where the student explores, "
                 "builds and checks the idea alone, with hints, retry and reset. Eight tools, each with its own purpose, "
                 "follow the chapter's own plan."},
        {"title": "A tool in three steps",
         "text": "Each tool opens with a short recall of the video idea, then lets the student play and apply it, and "
                 "ends with the chapter's own question or puzzle, used exactly as the book gives it."},
        {"title": "Every book question has its own video",
         "text": "Every solved example, Let Us Do and Let Us Think question and every answerable prompt of the book is "
                 "its own short video with a step by step solution and a question picture and a solution picture, in a "
                 "Questions topic that follows the idea it practises."},
        {"title": "One picture for every idea",
         "text": "Each teaching idea has one clear concept picture: tokens and place value charts, number lines, a digit "
                 "train, the rabbit and the carrots, the stable. Numbers stay the largest and clearest thing on screen."},
        {"title": "Only the book's facts",
         "text": "Distances, vehicle sizes and puzzle rules are the book's own. The plan never adds a speed, a fare or "
                 "a dataset of its own."},
    ],
}

# every book item, with its kind. Home concepts are listed in DESIGN.md section 3.
NCERT_ITEMS = [
    # chapter opening
    ("opening", "text"), ("open.vehicles", "talk"),
    # reading and writing large numbers: ten thousand and place value
    ("r.ten_thousand", "text"), ("r.place_chart", "text"), ("r.comma", "text"), ("r.indian_system", "text"),
    ("r.expanded_1380", "text"), ("r.expanded_9123", "text"),
    ("r.thousands", "prompt"),
    # the token table beyond 10,000
    ("r.tok_rows", "text"), ("r.tok_a", "prompt"), ("r.tok_b", "prompt"),
    # Let Us Do, first set (large numbers)
    ("LUDa.Q1abc", "exercise"), ("LUDa.Q1defg", "exercise"), ("LUDa.Q1hi", "exercise"),
    ("LUDa.Q2read", "exercise"), ("LUDa.Q2write", "exercise"),
    ("LUDa.Q3", "exercise"), ("LUDa.Q4", "exercise"), ("LUDa.Q5", "exercise"),
    # nearest tens, hundreds and thousands
    ("rab.tens", "example"), ("rab.hundreds", "prompt"), ("rab.thousands", "prompt"), ("rab.table", "prompt"),
    ("note.rounding", "text"),
    ("LUT.Q1", "exercise"), ("LUT.Q2", "exercise"), ("LUT.Q3", "exercise"),
    # travelling, now and then
    ("tr.now_then", "text"), ("tr.speeds", "text"), ("tr.note", "text"),
    ("LUDb.Q1", "exercise"), ("LUDb.Q2ad", "exercise"), ("LUDb.Q2eh", "exercise"),
    # finding large numbers around us
    ("ar.intro", "text"), ("ar.book", "example"), ("ar.mathsbook", "prompt"), ("ar.school", "talk"),
    ("ar.classroom", "prompt"), ("ar.tree_village", "prompt"),
    # pastime mathematics
    ("pm.intro", "text"), ("pm.river", "prompt"), ("pm.pebbles", "prompt"), ("pm.mira_steps", "text"),
    ("pm.mira_process", "example"), ("pm.mira_explore", "prompt"), ("pm.mira_table", "prompt"),
    ("pm.mira_asks", "prompt"), ("note.puzzles", "text"),
    # Let Us Do, second set (comparing, expanded form, place value)
    ("LUDc.Q1", "exercise"), ("LUDc.Q2", "exercise"), ("LUDc.Q3", "exercise"), ("LUDc.Q4", "exercise"),
    ("LUDc.Q5", "exercise"), ("LUDc.Q6", "exercise"), ("LUDc.Q7", "exercise"), ("LUDc.Q8ab", "exercise"),
    ("LUDc.Q8cg", "exercise"), ("LUDc.Q9a", "exercise"), ("LUDc.Q9b", "exercise"),
    # King's Horses
    ("kh.story", "text"), ("kh.mistake", "prompt"), ("kh.eighteen", "prompt"), ("kh.more", "prompt"),
    ("summary", "text"),
]

MISCONCEPTIONS = [
    ("M_TT_COLUMN", "Ten thousand is written as 10 in the Thousands column instead of 1 in a new column to its left."),
    ("M_COMMA_PLACE", "A comma goes after every two or three digits from the left, so ten thousand is written 100,00."),
    ("M_ZERO_NAME", "A zero is dropped when a number is read or written, so 10,010 is read ten thousand one ten and "
                    "forty thousand eight is written 4,008."),
    ("M_FIRST_DIGIT", "The number with the bigger first digit is the bigger number, whatever the number of digits."),
    ("M_PATTERN_RULE", "The rule of a pattern can be read from the first two numbers alone, or the step may change "
                       "from one number to the next."),
    ("M_SWAP_VALUE", "Swapping two digits of a number leaves its value the same."),
    ("M_ROUND_UP", "The nearest ten, hundred or thousand is always the bigger neighbour."),
    ("M_NEAR_FAR", "The nearest number is the neighbour that shares more digits with the number."),
    ("M_ZERO_HOLDER", "A place that holds a zero has no place in the expanded form, so the other digits move."),
    ("M_TENS_COUNT", "The number of tens in 983 is the tens digit, 8."),
    ("M_CORNER_TWICE", "A horse standing in a corner of the stable is counted only once when each side is counted."),
    ("M_DIGIT_DIFF", "The difference of the two numbers made from two digits is the same as the difference of the "
                     "two digits."),
    ("M_RIVER_BOTH", "The boatman can carry two things across at once."),
]

SOLUTION_NOTES = [
    {"item": "Let Us Do Q9 (hint)", "printed_solution": "The hint says 'Observe the answer of (iii)'.",
     "correct": "The parts are lettered, so the hint points to part (c), the number of thousands. The plan writes (c)."},
    {"item": "King's Horses: how many more horses can the thief steal",
     "printed_solution": "The book prints no limit.",
     "correct": "The number of horses is 20 minus the horses in the four corner stalls. One horse per corner stall gives "
                "16 horses, so 2 more can be taken after the 18. Crowding more horses into corner stalls keeps every "
                "side at 5 down to 10 horses, but the king would notice. This is the plan's own reading, to be "
                "confirmed."},
    {"item": "Let Us Do Q4 (number line 5,000 to 50,000)",
     "printed_solution": "The line has 10 marks with 5,000 and 10,000 and 50,000 printed and 7 blanks.",
     "correct": "The marks are 5,000 apart: 15,000, 20,000, 25,000, 30,000, 35,000, 40,000, 45,000."},
    {"item": "Rounding at an exact halfway number",
     "printed_solution": "The book shows the halfway mark on each picture but states no rule for a number on it.",
     "correct": "The plan uses only numbers that are nearer to one neighbour and teaches the jumps method of the book."},
    {"item": "Open prompts (items counted around us, numbers between two numbers, same nearest number)",
     "printed_solution": "No single answer.",
     "correct": "The plan gives one reasoned sample answer and says the student's answer may differ."},
    {"item": "Priority doc: Travelling Then and Now, short recap video",
     "printed_solution": "The doc asks for a short recap video.",
     "correct": "The pipeline has no recap video, so the slot is a real concept, Travelling, Now and Then, that adds "
                "the animals and modern vehicles of the book."},
]
ERRATA = []

DESIGN_REFERENCES = [
    {"text": "priority_doc.md (the user's 'We The Travellers 1' plan, 2026-11-03): topic flow, video types, the 8 tools, "
             "the shared visual language and the learning rules decide this chapter's design.", "url": ""},
    {"text": "docs/01_runbook.md and .claude/skills/lp/SKILL.md: framing intro with a free-try tool, idea topics each "
             "ending in a Practice concept, a Questions topic after every idea topic with one concept per book question, "
             "and one summary topic.", "url": ""},
]

# The book's own figures that carry mathematics, keyed by authored concept key. One concept image per teaching,
# hook and summary concept (user instruction); the tool concepts (Practice / free try) are pictured by their tool.
FIGURES = {
    "T1.C1": ["The three opening pictures: a bullock cart under trees, a man on a bicycle in a market street, a wide "
              "road full of cars. No numbers."],
    "T1B.C1": ["A then and now line: a boat, a bullock cart, a train, a car and a bicycle in a row from long ago to today, "
              "no dates and no numbers."],
    "T2.C1": ["Ten tokens each marked 1,000 in two rows of five, an arrow, and one token marked 10,000."],
    "T2.C2": ["A place value chart with columns TTh, Th, H, T, O and five rows 1, 10, 100, 1,000, 10,000, curved arrows "
              "marked x10 above the columns, and 1,380 and 9,123 as token groups."],
    "T3.C1": ["Token rows for 10,001, 10,010 and 10,024 each with its place value digits and number name."],
    "T3.C2": ["The chart for 10,010 and 50,005 with the zeros highlighted and the number names beside them."],
    "T4.C1": ["A number name on a ticket, the chart below it and the digits written in the five places."],
    "T4.C2": ["The chart for forty thousand eight with the empty places filled by zeros."],
    "T5.C1": ["A chain of number boxes joined by arrows each marked with the same step."],
    "T5.C2": ["A chain that goes down and a chain that passes ten thousand, boxes in two rows."],
    "T6.C1": ["Two numbers one above the other in the place value chart with a comparing arrow."],
    "T6.C2": ["A number line from 0 to 40,000 with equal marks and number cards placed on it."],
    "T6.C3": ["A number line with two end numbers and five marks between them."],
    "T7.C1": ["A number train whose coaches are digits, two coaches marked to swap."],
    "T7.C2": ["Before and after rows of digit coaches, the bigger and the smaller number side by side."],
    "T8.C1": ["Tokens for a number grouped under its expanded form."],
    "T8.C2": ["Bundles of notes: tens, hundreds and thousands counted from one amount."],
    "T9.C1": ["The rabbit on a line between two carrots at neighbouring tens, with the halfway mark."],
    "T9.C2": ["Two lines: the rabbit between neighbouring hundreds and between neighbouring thousands."],
    "T9.C3": ["A number line where two different numbers jump to the same nearest hundred."],
    "T10.C1": ["The book's picture of vehicles: a ship with a sail, an aeroplane, an electric bike, a train, a bus, a "
               "submarine, a space shuttle and a sled pulled by dogs."],
    "T10.C2": ["A board listing the eight means of travel with the book's distance in one hour for each."],
    "T10.C3": ["A group of people shown in equal vehicles, each vehicle holding the same number."],
    "T11.C1": ["A book with pages and words, the pages times the words grouped into a large count."],
    "T12.C1": ["A river with a lion, a sheep and a bundle of grass on one bank and a boatman in a boat."],
    "T12.C2": ["Two piles of pebbles."],
    "T12.C3": ["Digit subtraction chain boxes in a row."],
    "T13.C1": ["The square stable of twelve stalls with the horses as dots: top row 1, 2, 2, 0; sides 1 and 3 on the left, "
               "2 and 3 on the right; bottom row 0, 2, 3, 0."],
    "T14.C1": ["A journey map that touches each idea of the chapter in order."],
}
