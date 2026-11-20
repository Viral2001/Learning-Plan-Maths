# -*- coding: utf-8 -*-
"""Chapter-level content for Class 5 Chapter 5, Far and Near (Maths Mela, Grade 5, Chapter 5).

The plan follows the "Class 5 Mathematics Learning Experience Designer" brief (priority_doc.md sections A to F) and the
/lp pipeline's structure; the book decides every number and every question. Book lines are verbatim except: the book's
dashes become commas, colons or "to"; minus is U+2212; the book's "4 km 450 m" stays as printed. No em dash and no en
dash anywhere here."""
from __future__ import annotations

CHAPTER = {
    "grade": 5,
    "label": "Class 5",
    "chapter_no": 5,
    "name": "Far and Near",
    "book_part": "Maths Mela, Grade 5, Chapter 5",
    "source_pdf": "textbooks/class-5/eemm105.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Units, Names and Comparing Lengths",
     "Choosing the unit that fits a length, seeing one length in two units (metres and centimetres), comparing lengths "
     "given in different units and finding how much longer one is than another."),
    ("M2", "Far and Near: Kilometres, Millimetres and Changing Units",
     "The kilometre for long distances, equal stops along a distance, the distance between two stations, the "
     "millimetre for small lengths, and changing a length between mm, cm, m and km."),
    ("M3", "Working with Lengths",
     "Adding, subtracting, multiplying and dividing lengths, the cost of a length, estimating with a reference, feet "
     "and inches, a sign puzzle and a revision of the chapter."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter takes place in a village weaving centre with a long measuring tape on the wall, and on the "
             "roads, rulers and walls around it. Saris, stoles, ropes, trains, sprouts and statues are the lengths. "
             "Measuring them shows which unit fits, how one length has two names, and how to compare, add, subtract, "
             "multiply and divide lengths. A short video explains each idea, and an interactive tool lets the student "
             "try it alone.",
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
         "text": "Tapes, rulers, bars and double number lines carry each idea: equal marks, the length as the largest "
                 "thing on screen, and the unit written beside every number."},
        {"title": "Only the book's numbers",
         "text": "Heights of statues, station distances, ropes, cloth prices and every question are the book's own. Any "
                 "number the plan adds is a practice value and is said to be one."},
    ],
}

# {module_id: strand letter}: the subject strand each module belongs to (core/qt.py builds every objective's strand).
# CBSE maths catalog: N Number, A Algebra, G Geometry, M Measurement, D Data, S Statistics and Probability.
MODULE_STRANDS = {"M1": "M", "M2": "M", "M3": "M"}

# every book item, with its kind. Home concepts are listed in DESIGN.md section 3.
NCERT_ITEMS = [
    # the opener: Let Us Find, Different Units but Same Measure
    ("open.intro", "text"), ("sari.story", "text"),
    ("find.units", "exercise"), ("sari.line", "prompt"), ("sari.match", "prompt"),
    # Let Us Compare
    ("cmp.q1", "exercise"), ("cmp.q2a", "exercise"), ("cmp.q2b", "exercise"), ("cmp.q2c", "exercise"),
    ("cmp.q2d", "exercise"),
    # Measuring Long Distances, the kilometre, Kilometre Race
    ("km.tools", "text"), ("walk.steps", "exercise"), ("km.def", "text"), ("rope.table", "prompt"),
    ("race.q1", "exercise"), ("race.q2", "exercise"), ("race.q3", "exercise"),
    # Longest Train Journey
    ("train.q1", "exercise"), ("train.q2", "exercise"), ("train.q3", "exercise"), ("train.q4", "exercise"),
    ("train.q5", "exercise"),
    # The World of Small Things
    ("small.how", "talk"), ("mm.def", "text"), ("ruler.count", "prompt"), ("design.measure", "exercise"),
    ("sprout.diary", "exercise"), ("draw.lines", "exercise"), ("draw.how", "talk"),
    # Relationships between Different Units and Let Us Do on changing units
    ("rel.units", "text"), ("dnl.a", "exercise"), ("dnl.b", "exercise"), ("dnl.c", "exercise"),
    ("conv.ex_mm", "text"), ("conv.ex_cm", "text"),
    ("conv.mmcm", "exercise"), ("conv.mcm", "exercise"), ("conv.kmm", "exercise"),
    # Adding and Subtracting Lengths
    ("add.saji", "example"), ("add.cable", "example"), ("addsub.note", "text"),
    ("addsub.q1", "exercise"), ("addsub.q2", "exercise"), ("addsub.q3", "exercise"), ("addsub.q4a", "exercise"),
    ("addsub.q4b", "exercise"),
    # Multiplying and Dividing Lengths
    ("md.method", "text"), ("md.shirt", "example"), ("md.bag", "example"), ("md.line", "prompt"),
    ("md.anita", "exercise"), ("md.road", "exercise"),
    # Let Us Estimate, feet and inches, Measure Your Height
    ("est.pictures", "text"), ("est.q1", "exercise"), ("est.q2", "exercise"), ("est.q3", "exercise"),
    ("inch.def", "text"), ("inch.find", "prompt"), ("height.measure", "prompt"),
    # Try This and the summary
    ("sign.puzzle", "prompt"),
    ("summary", "text"),
]

MISCONCEPTIONS = [
    ("M_UNIT_ANY", "Any unit will do for any length: the height of India Gate can be written in centimetres as easily "
                   "as in metres, and a pencil in metres as easily as in centimetres."),
    ("M_BIGGER_NUMBER", "The bigger number is the longer length, even when the units are different, so 456 cm is more "
                        "than 5 m."),
    ("M_M_TEN_CM", "1 m is 10 cm, so 3 m is 30 cm."),
    ("M_KM_HUNDRED", "1 km is 100 m, so 7 km is 700 m."),
    ("M_CM_HUNDRED_MM", "1 cm is 100 mm, so 4 cm is 400 mm."),
    ("M_JOIN_NUMBERS", "A length such as 6 m 5 cm is the number 65 or 650 in cm: the two numbers are written side by "
                       "side without changing the unit."),
    ("M_ADD_ALL", "To add 3 km 450 m and 4 km 650 m, add all four numbers, 3 + 450 + 4 + 650."),
    ("M_BORROW_TEN", "When subtracting, 1 m is borrowed as 10 cm, and 1 km as 100 m."),
    ("M_DIST_SUM", "The distance between two stations is found by adding their distances from the start."),
    ("M_STOP_COUNT", "Stops after every 500 m on a 3 km race are counted with the start line too, or by counting the "
                     "marks instead of the gaps."),
    ("M_MULT_PART", "20 times 1 m 80 cm is 20 m 80 cm: only the metres are multiplied, or the 80 cm is left as it "
                    "is."),
    ("M_FOOT_TEN", "1 foot is 10 inches."),
    ("M_GUESS", "An estimate is a wild guess with no reference needed."),
    ("M_SIGN_REPEAT", "A sign can repeat in a row if it is in a different column."),
]

SOLUTION_NOTES = [
    {"item": "Let Us Find (the unit for each quantity)",
     "printed_solution": "The table's second column is headed 'Metre (m) or centimetre (cm)' but holds numbers (42, 40, "
                         "50, 13, 2, 5); the book prints no answers.",
     "correct": "The plan reads each number as the measure and the student chooses the unit: India Gate 42 m, handkerchief "
                "40 cm, well 50 m, mobile phone 13 cm, elephant's trunk 2 m, buttons 5 cm. The well is the only doubtful "
                "one; a well 50 cm deep is not possible."},
    {"item": "Different Units but Same Measure (the match table)",
     "printed_solution": "The table at the top of the next page has no heading and no instruction; the book prints no "
                         "answers.",
     "correct": "The plan reads it as matching: 204 cm = 2 m 4 cm, 540 cm = 5 m 40 cm, 750 cm = 6 m 150 cm, 240 cm = "
                "2 m 40 cm, 404 cm = 2 m 204 cm (each in the other column, not in its own row). The double number line "
                "above it has the blanks 200 cm, 4 m, 5 m, 7 m."},
    {"item": "Let Us Compare, Q2 (the statues)",
     "printed_solution": "The book prints no answers. Heights: 182 m, 128 m, 108 m, 93 m, 91 m, 38 m.",
     "correct": "(a) 182 − 93 = 89 m. (b) the Statue of Liberty and The Motherland Calls, 2 m (checked against all 15 "
                "pairs). (c) the Statue of Unity and Christ the Redeemer, 144 m. (d) 91 m doubled is 182 m, The "
                "Motherland Calls."},
    {"item": "Let Us Do on measuring long distances (walk and count steps)",
     "printed_solution": "The book gives no numbers: the student's own school, steps and home.",
     "correct": "The plan gives a sample answer with practice values (125 steps for 100 m, 250 steps for 200 m, so a step is "
                "80 cm; a tea shop 120 m, a school gate 400 m, a temple 1,600 m) and says 'Your answer may differ'."},
    {"item": "Kilometre Race",
     "printed_solution": "The book does not say whether a stop stands at the start line or at the finish line, or which "
                         "colour the first flag is.",
     "correct": "Positions are read from the starting point, the first stop at the first interval and the last at the "
                "finish line (3 km): 6 water stations, 10 children, 60 flags (30 red and 30 blue; red first, the counts "
                "are the same either way). A stop at the start line would add one to each count."},
    {"item": "Longest Train Journey",
     "printed_solution": "The table gives distances from Dibrugarh; the book does not say how to find the distance between "
                         "two stations, and prints no answers.",
     "correct": "The route starts at Dibrugarh (0 km). The distance between two stations is the difference of their "
                "distances from Dibrugarh. The route length is the distance of Kanniyakumari, 4,187 km."},
    {"item": "Let Us Measure (the design)",
     "printed_solution": "The book prints no measurements. The design has eight lines with an empty box beside each.",
     "correct": "The plan measured the lines on the PDF drawing at the printed page size (1 pt = 0.3528 mm): 48, 35, 60, 27, "
                "22, 19, 44 and 61 mm, each within 0.3 mm of a whole millimetre. A printed copy may be scaled, so a ruler "
                "may read 1 mm different. The plan numbers the lines 1 to 8 from the top of the picture to the bottom."},
    {"item": "Let Us Do on the sprout diary",
     "printed_solution": "A real four-day activity with the student's own seeds; the book gives no numbers.",
     "correct": "The plan gives a sample row of practice values and says 'Your answer may differ'."},
    {"item": "Let Us Do on double number lines, line (a): the last blank",
     "printed_solution": "The blank under the 50 cm tick is printed with the unit m, but every other blank on that line is "
                         "in mm.",
     "correct": "The plan answers 500 mm and notes that 50 cm is also half a metre, so both readings are covered. The "
                "number lines are drawn with evenly spaced ticks although the values are not evenly spaced."},
    {"item": "Let Us Do on conversions, Q2",
     "printed_solution": "Fourteen parts (a) to (n) in one question; (b) and (h) have a printed solved case in the margin.",
     "correct": "The plan keeps the printed method for (b) and (h) and splits the fourteen parts into three question sets "
                "by unit pair: (a) to (d), (e) to (i), (j) to (n), so that each answer fits the display limit."},
    {"item": "Let Us Do on adding and subtracting, Q4",
     "printed_solution": "Seven pairs (a) to (g) in one question.",
     "correct": "The plan splits them into two question sets, (a) to (d) and (e) to (g), so that each answer fits the "
                "display limit."},
    {"item": "Let Us Do on conversions and Saji's walk: two printed methods",
     "printed_solution": "The book shows two methods for Saji's walk and for the cable (like units, or change everything to "
                         "the smaller unit; a column with carrying or with borrowing).",
     "correct": "The plan uses the change-to-the-smaller-unit method in the solution steps and shows the like-unit method as "
                "a check; both give the printed answer (8 km 100 m, 46 m 25 cm)."},
    {"item": "Multiplying and Dividing Lengths, Q3 (Anita's thread)",
     "printed_solution": "'She needs a 1 m long thread to embroider a 50 cm sari' does not say what the 50 cm is.",
     "correct": "The plan reads it as 1 m of thread for every 50 cm of sari border: a 5 m border is 500 cm = 10 times 50 cm, "
                "so 10 m of thread, costing 10 times ₹50 = ₹500."},
    {"item": "Let Us Estimate (the student's own neighbourhood)",
     "printed_solution": "The three estimates depend on the student's own tallest building, tallest tree and well or pool.",
     "correct": "The plan gives a sample answer with a reference and practice values for each and says 'Your answer may "
                "differ'."},
    {"item": "Measure Your Height",
     "printed_solution": "A real activity with the student's class; the book prints no heights.",
     "correct": "The plan gives a sample list of practice values and finds the tallest by changing feet and inches to inches."},
    {"item": "Try This (the sign puzzle): 'each 4 × 4 box'",
     "printed_solution": "The book says each row, each column and each 4 × 4 box should not repeat the sign, but the grid is "
                         "itself 4 by 4. Printed-book error.",
     "correct": "The plan reads the boxes as the four 2 × 2 boxes of the grid. The puzzle has exactly one solution from the "
                "rows and columns alone, and that solution also has no sign repeated in any 2 × 2 box."},
    {"item": "Note for the Teachers (p. 65)",
     "printed_solution": "A note addressed to teachers about mental strategies and column strategies.",
     "correct": "The plan keeps the idea as its own teaching line (work in your head when the numbers are easy, use a column "
                "method otherwise) and gives no teaching role to a teacher."},
    {"item": "The kit of long-distance tools (long tape, rodometer, rangefinder, laser distance meter)",
     "printed_solution": "The book only names the four tools.",
     "correct": "The plan names them and adds no facts about how they work."},
    {"item": "Brief: revision video",
     "printed_solution": "The brief asks for an interactive recap or revision video.",
     "correct": "The pipeline has no recap video, so the last topic is a text summary with short concept checks."},
    {"item": "Open prompts (activities and estimates that need the student's own measuring)",
     "printed_solution": "No single answer.",
     "correct": "The plan gives one reasoned sample answer built on practice values and says the student's answer may differ."},
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

# The book's own figures that carry mathematics, keyed by authored concept key. One concept image per teaching,
# hook and summary concept where a drawn figure is the maths; the tool concepts (Practice / free try) are pictured by
# their tool.
FIGURES = {
    "T1.C1": ["Two people at a weaving centre table, one holding a tape marked in centimetres and one holding a tape marked "
              "in metres, with a folded sari between them. No numbers written."],
    "T1B.C1": ["A pencil of 17 cm beside a short ruler and a classroom wall of 8 m beside a long tape, each with the right "
               "unit chip and the other unit chip crossed out."],
    "T1B.C2": ["A double number line: the top line marked 0 to 5 in m and the bottom line marked 0 to 500 in cm, with an arrow "
               "marked x100 and the examples 3 m = 300 cm and 450 cm = 4 m 50 cm."],
    "T2.C1": ["Two bars on one tape in cm, 7 m 9 cm (709 cm) and 790 cm, with the sign between them."],
    "T2.C2": ["Two bars of 285 cm and 2 m 60 cm on one tape with the gap between them marked 25 cm."],
    "T3.C1": ["A road strip marked 0 to 7 km with 1 km = 1,000 m on the first km and 7 km = 7,000 m on the whole road."],
    "T3.C2": ["A 2 km track with a flag after every 400 m: five flags at 400, 800, 1,200, 1,600 and 2,000 m."],
    "T4.C1": ["A route line from a start point with two stations at 340 km and 615 km, the gap between them marked 275 km."],
    "T5.C1": ["A ruler with a lens on one centimetre: ten equal parts, each 1 mm, with 9 small marks."],
    "T5.C2": ["A ruler with a line from 0 to 4 cm 6 mm and the reading 4 cm 6 mm = 46 mm."],
    "T6.C1": ["Three double number lines side by side: cm over mm with x10, m over cm with x100, km over m with x1,000."],
    "T6.C2": ["A length of 7,305 cm split into 7,300 cm (73 m) and 5 cm."],
    "T7.C1": ["Two lengths, 2 km 700 m and 1 km 800 m, in a two-column table with a carry circle, and the total 4 km 500 m."],
    "T7.C2": ["A ribbon of 9 m with 3 m 40 cm cut off and the part left, 5 m 60 cm, shown on a tape."],
    "T8.C1": ["Twelve curtain strips of 2 m 40 cm, the metres and the centimetres sorted into two piles."],
    "T8.C2": ["A road bar of 18 km 900 m shared into 3 equal day parts of 6 km 300 m."],
    "T8.C3": ["A double number line with metres over rupees: 3 m over ₹90, 6 m over ₹180, 9 m over ₹270."],
    "T9.C1": ["A wall with a door beside it, the wall as high as two doors, with a reference line of about 2 m."],
    "T10.C1": ["A wall chart with feet marks and a child standing against it at 4 feet 6 inches, and the read-out 54 inches."],
    "T11.C1": ["A 3 by 3 grid with the signs +, minus and times, three placed and six empty boxes."],
    "T12.C1": ["The weaving centre wall tape with eight cards, one for each idea of the chapter."],
}
