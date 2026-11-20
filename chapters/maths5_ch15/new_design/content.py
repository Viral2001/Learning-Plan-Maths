# -*- coding: utf-8 -*-
"""Chapter-level content for Class 5 Chapter 15, Data Through Pictures (Maths Mela, Grade 5, Chapter 15).

The plan follows the "Class 5 Mathematics Learning Experience Designer" brief (priority_doc.md sections A to F) and the
/lp pipeline's structure; the book decides every number and every question. Book lines are verbatim except: the book's
dashes become commas, colons or "to"; minus is U+2212; fractions are written a/b. No em dash and no en dash anywhere
here."""
from __future__ import annotations

CHAPTER = {
    "grade": 5,
    "label": "Class 5",
    "chapter_no": 15,
    "name": "Data Through Pictures",
    "book_part": "Maths Mela, Grade 5, Chapter 15",
    "source_pdf": "textbooks/class-5/eemm115.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Recording Data and Pictographs",
     "Collecting the answers of many friends, recording them in a table, and showing numbers with icons and a scale in "
     "a pictograph: reading it, comparing its rows and choosing another scale."),
    ("M2", "Bar Graphs",
     "Standing rows of squares up into bars, reading and comparing bars, making a bar graph of a day and of real "
     "lengths, and using a bar graph to find the highest, the total and a prediction."),
    ("M3", "Reading a Picture and Revision",
     "Judging statements about a picture of school children by counting, and a revision of tables, pictographs, bar "
     "graphs and pictures."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter takes place in the class newsroom of two child reporters, Samaira and Kabir. They ask friends "
             "questions, record the answers and show them in a table, a pictograph and a bar graph. A short video "
             "explains each idea, and an interactive tool lets the student try it alone.",
    "points": [
        {"title": "Videos teach, tools explore",
         "text": "Every idea has one short concept video. The tool that follows is where the student sorts, builds and "
                 "checks the idea alone, with hints, retry and reset. Five tools, each with its own purpose, follow the "
                 "chapter's own plan."},
        {"title": "A tool in three steps",
         "text": "Each tool opens with a short recall of the video idea, then lets the student play and apply it, and "
                 "ends with the chapter's own question, used exactly as the book gives it."},
        {"title": "Every book question has its own video",
         "text": "Every numbered question and every answerable activity of the book is its own short video with a step "
                 "by step solution and a question picture and a solution picture, in a Questions topic that follows "
                 "the idea it practises."},
        {"title": "The picture is the data",
         "text": "The notebook, the table, the icons, the bars and the picture of school children carry each idea. The "
                 "data is always the largest thing on screen, and a bar graph always has its vertical line with "
                 "numbers and its horizontal base with names."},
        {"title": "Only the book's data",
         "text": "The notebook of 35 answers, the pictographs, the two days, the food graph and the picture of children "
                 "are the book's own. Any number the plan adds is a practice value and is said to be one."},
    ],
}

# {module_id: strand letter}: the subject strand each module belongs to (core/qt.py builds every objective's strand).
# CBSE maths catalog: N Number, A Algebra, G Geometry, M Measurement, D Data Handling, S Statistics and Probability.
MODULE_STRANDS = {"M1": "D", "M2": "D", "M3": "D"}

# every book item, with its kind. Home concepts are listed in DESIGN.md section 3.
NCERT_ITEMS = [
    # Child TV Reporter
    ("tv.story", "text"), ("tv.tablehead", "text"), ("tv.eyes", "talk"),
    ("tv.table", "prompt"), ("tv.q1", "exercise"), ("tv.q2", "exercise"), ("tv.q3", "exercise"),
    ("tv.q4", "exercise"),
    # Stock-Taking in a Shop
    ("shop.story", "text"), ("shop.suggest", "talk"), ("shop.scale", "text"),
    ("shop.q1", "exercise"), ("shop.q2", "exercise"), ("shop.q3", "exercise"), ("shop.choose", "prompt"),
    # Two-wheelers on the Road
    ("road.story", "text"),
    ("road.q1", "exercise"), ("road.q2", "exercise"), ("road.q3", "exercise"), ("road.q4", "exercise"),
    ("road.q5", "prompt"),
    # Recording a Day
    ("day.story", "text"), ("day.bar", "text"), ("day.diff", "talk"),
    ("day.q1", "exercise"), ("day.q2", "exercise"), ("day.q3", "exercise"), ("day.q4", "exercise"),
    ("day.q5", "exercise"),
    # Day in My Life and Whose Index Finger is Longer?
    ("mine.record", "prompt"), ("mine.graph", "prompt"),
    ("finger.make", "prompt"), ("finger.q1", "exercise"), ("finger.q2", "exercise"), ("finger.q3", "exercise"),
    ("finger.q4", "exercise"),
    # Food Wastage in the School Canteen
    ("food.story", "text"), ("food.think", "talk"),
    ("food.q1", "exercise"), ("food.q2", "exercise"), ("food.q3", "exercise"), ("food.q4", "exercise"),
    ("food.q5", "exercise"), ("food.q6", "exercise"),
    # True or False
    ("pic.setup", "text"),
    ("tf.s1", "prompt"), ("tf.s2", "prompt"), ("tf.s3", "prompt"), ("tf.s4", "prompt"), ("tf.s5", "prompt"),
    ("tf.s6", "prompt"), ("tf.s7", "prompt"), ("tf.s8", "prompt"),
    # the summary
    ("summary", "text"),
]

MISCONCEPTIONS = [
    ("M_ICON_IS_ONE", "Each icon stands for one item, so the number of icons is the number of items."),
    ("M_SCALE_NO_FIT", "Any scale can be used for any numbers, even if some items are left over."),
    ("M_BIG_SCALE_MORE", "A bigger scale needs more icons."),
    ("M_MORE_THAN_INCLUDES", "More than half an hour includes the row for half an hour."),
    ("M_COUNT_TWICE", "When sorting many answers, an answer can be counted twice or missed without anyone noticing."),
    ("M_BAR_WIDTH", "A wider bar means a bigger number."),
    ("M_BAR_LABEL", "The number written near a bar is its height, even where the top of the bar meets another number "
                    "on the vertical line."),
    ("M_ONE_LOOK", "A statement about a picture can be judged by a quick look, without counting."),
    ("M_HALF_ODD", "Half of an odd number cannot be found, or half of 17 is 8, so 8 is more than half."),
]

SOLUTION_NOTES = [
    {"item": "Child TV Reporter: the counts of the notebook and the empty table",
     "printed_solution": "The book prints the notebook of 35 answers and an empty table, with no counts and no "
                         "instruction to fill the table.",
     "correct": "The plan counts the 35 speech bubbles (zoomed 4.5 times, twice): 1/2 hr 9, 1 hr 13, 1 1/2 hr 7, 2 hr 3, "
                "2 1/2 hr 3, in all 35. The three 2 1/2 hr answers go in the row More than 2 hours. Filling the table is "
                "a prompt of its own, worded by the plan. Plan's own reading."},
    {"item": "Child TV Reporter, Q1 and Q2: more than half an hour, less than two hours",
     "printed_solution": "The book prints no answer.",
     "correct": "More than half an hour is every row after 1/2 hour: 13 + 7 + 3 + 3 = 26. Less than two hours is the rows "
                "1/2 hour, 1 hour and 1 1/2 hour: 9 + 13 + 7 = 29. The row 2 hours is not less than two hours."},
    {"item": "Whose Index Finger is Longer?: the four questions",
     "printed_solution": "The book prints no data: the answers depend on the student's friends.",
     "correct": "The plan answers with a sample of practice values: Mine 6 cm, Friend 1 7 cm, Friend 2 5 cm, Friend 3 8 cm, "
                "Friend 4 6 cm (the page has five places, Mine and four blanks). Each answer says the student's answer "
                "will differ. The paper strips are hands-on; the tool takes the measured lengths."},
    {"item": "Day in My Life: the data and the minutes",
     "printed_solution": "The book prints no data, and says in hours and minutes, as necessary, but marks the graph in "
                         "whole hours from 0 to 9.",
     "correct": "The sample uses whole hours (9 + 5 + 2 + 2 + 3 + 3 = 24) and the two blank rows for Playing and Other "
                "activities. How to show part of an hour on the graph is not taught and is not introduced."},
    {"item": "Recording a Day: Raman's table is not named a pictograph",
     "printed_solution": "The book calls Raman's recording a table and Sheela's a bar graph.",
     "correct": "The plan calls Raman's table a table of squares (one square = 1 hour), a row of icons, and uses it as the "
                "bridge from icons to bars. The activity names differ slightly (Time spent sleeping, Sleeping) and are "
                "read as the same five activities."},
    {"item": "Recording a Day, Q4: the same amount of time",
     "printed_solution": "The book prints no answer.",
     "correct": "Raman 9, 6, 2, 6, 1 and Sheela 8, 7, 4, 3, 2 differ on every activity, so the answer is No."},
    {"item": "Recording a Day, Q5: a more balanced routine",
     "printed_solution": "The book prints no answer; it is a matter of opinion.",
     "correct": "Sample: Sheela's routine, because her study time 4 hours and play time 3 hours are closer than Raman's 2 "
                "and 6. Another answer is right if its reason uses the numbers."},
    {"item": "Food Wastage, Q5 and Q6",
     "printed_solution": "Two blanks and a prediction: no single answer.",
     "correct": "Sample: Friday had less food wastage than Monday (4 kg and 5 kg); Khichdi is likely to be wasted the "
                "most again (8 kg this week). A prediction is a careful guess from the graph."},
    {"item": "Food Wastage: the notice board and Q4 use different rates",
     "printed_solution": "The notice board says 13 kg could have fed 25 people; Q4 says 1 kg can feed 3 children.",
     "correct": "13 × 3 is 39, not 25. The plan uses the question's own rule for Q4 (30 kg gives 90 children) and uses no "
                "number of the notice board in any calculation. To be confirmed."},
    {"item": "True or False: the picture of 17 children",
     "printed_solution": "The book prints no answers and no counts.",
     "correct": "Read at 5 to 9 times zoom: 17 children (8 girls, 9 boys), 10 caps, 7 pairs of glasses, 14 books, 4 "
                "backpacks; 6 children wear a cap and glasses; one child, the girl at the back on the left, has a cap, a "
                "book and a backpack. Boys and girls are read from the uniform and the hair; some back-row children are "
                "partly hidden. Statements 3 (7 boys and 7 girls hold books) and 6 (4 boys and 3 girls wear glasses) "
                "depend on this reading. To be confirmed against the original artwork."},
    {"item": "True or False: eight statements, one question each",
     "printed_solution": "The book prints one box of eight statements to mark TRUE or FALSE.",
     "correct": "The plan makes each statement its own question (its own video) because each needs a different count. The "
                "opening sentence of the box is repeated in the singular for each. The dash in statement 8 is written as "
                "commas."},
    {"item": "Choose your scale (Stock-Taking in a Shop and Two-wheelers on the Road)",
     "printed_solution": "A notebook task with no answer.",
     "correct": "One sample each: scale 10 for 40, 50, 60 gives 4, 5, 6 icons; scale 6 for 24, 12, 36 gives 4, 2, 6 icons. "
                "Another scale that fits every number is also right. The student's answer may differ."},
    {"item": "Printed-book typo",
     "printed_solution": "The table heading on the page of Raman's table reads Activites.",
     "correct": "The plan writes Activities."},
    {"item": "The PDF holds more than the chapter",
     "printed_solution": "The 22-page file has the chapter on PDF pages 1 to 9, then two Notes pages and the Learning Material "
                         "Sheets of the book (a grid, a Fractions Kit, Tessellation and Shapes, Number Tokens, nets, a dot "
                         "grid, a graph paper).",
     "correct": "None of the sheets is used by this chapter. The Fractions Kit sheet shows 12 round pieces from 1 to 1/12, "
                "which the Chapter 2 plan says was not supplied."},
    {"item": "Brief: revision video",
     "printed_solution": "The brief asks for an interactive recap or revision video.",
     "correct": "The pipeline has no recap video, so the last topic is a text summary with short concept checks."},
    {"item": "Open prompts (the notebook tasks, the activities, the opinions)",
     "printed_solution": "No single answer.",
     "correct": "The plan gives one reasoned sample answer and says the student's answer may differ."},
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

# The book's own figures that carry mathematics, keyed by authored concept key. One concept image per teaching, hook
# and summary concept where a drawn figure is the maths; the tool concepts (Practice / free try) are pictured by their
# tool or by their own question cards.
FIGURES = {
    "T1.C1": ["Samaira with a microphone and Kabir with a notebook asking a row of five friends how many hours a day "
              "they watch TV, each friend answering in a speech bubble with a different number of hours."],
    "T1B.C1": ["Twelve answers in a row and the finished table with one row for each answer, the count of each row and "
               "the total."],
    "T2.C1": ["A pictograph of three rows of icons with the icon box 1 icon = 5 items, the number of each row written "
              "at its end."],
    "T2.C2": ["The same three numbers shown twice as a pictograph, once with a bigger scale and fewer icons and once "
              "with a smaller scale and more icons."],
    "T3.C1": ["A pictograph of three days with the icon box 1 icon = 10 samosas, the number of each day written at the "
              "end of its row."],
    "T4.C1": ["Three rows of squares (1 square = 1 hour) and the same data as a bar graph with the vertical line, the "
              "horizontal base and three bars, a dotted arrow from each row to its bar."],
    "T4.C2": ["Two bar graphs side by side with the same three activities, one for each child."],
    "T5.C1": ["A bar graph of five activities on the horizontal base with the vertical line marked from 0 to 9."],
    "T5.C2": ["Three paper-strip bars of different lengths on a graph whose vertical line is marked in cm."],
    "T6.C1": ["A bar graph of five days with bars of different heights and the vertical line marked from 0 to 7."],
    "T7.C1": ["A row of nine children, some with a hat, some with a flag, some with both and some with neither."],
    "T8.C1": ["A newsroom wall with four small panels: a table, a pictograph, a bar graph and a picture of children."],
}
