# -*- coding: utf-8 -*-
"""Chapter-level content for Class 5 Chapter 12, Racing Seconds (Maths Mela, Grade 5, Chapter 12).

The plan follows the "Class 5 Mathematics Learning Experience Designer" brief (priority_doc.md sections A to F) and the
/lp pipeline's structure; the book decides every number and every question. Book lines are verbatim except: the book's
dashes become commas, colons or "to"; minus is U+2212; the book's unit abbreviations (sec., min, hr) are written in full
(seconds, minutes, hours) and its slips ("1 hours 10 minutes") are corrected. No em dash and no en dash anywhere here."""
from __future__ import annotations

CHAPTER = {
    "grade": 5,
    "label": "Class 5",
    "chapter_no": 12,
    "name": "Racing Seconds",
    "book_part": "Maths Mela, Grade 5, Chapter 12",
    "source_pdf": "textbooks/class-5/eemm112.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Clock Time, Time Elapsed and Two Ways to Write the Time",
     "Reading a clock, finding how much time has passed between two times, comparing times taken, and writing a time "
     "in the 12-hour and the 24-hour format."),
    ("M2", "A New Unit: Seconds",
     "Minutes and seconds in a race, choosing seconds or minutes for an activity, and reading and drawing the seconds "
     "hand on a clock."),
    ("M3", "Changing Units and Solving Time Problems",
     "Changing hours to minutes and minutes to seconds and back on a double number line, finding the time after and the "
     "time before a given time, and a revision of the whole school day."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter follows one school day. Clocks on the wall, a race on the track and a notice board are the "
             "places where time is read, measured and changed from one unit to another. A short video explains each "
             "idea, and an interactive tool lets the student try it alone.",
    "points": [
        {"title": "Videos teach, tools explore",
         "text": "Every idea has one short concept video. The tool that follows is where the student explores, "
                 "builds and checks the idea alone, with hints, retry and reset. Five tools, each with its own "
                 "purpose, follow the chapter's own plan."},
        {"title": "A tool in three steps",
         "text": "Each tool opens with a short recall of the video idea, then lets the student play and apply it, and "
                 "ends with the chapter's own question, used exactly as the book gives it."},
        {"title": "Every book question has its own video",
         "text": "Every solved example, Let Us Do question and every answerable prompt of the book is its own short "
                 "video with a step by step solution and a question picture and a solution picture, in a Questions "
                 "topic that follows the idea it practises."},
        {"title": "The picture is the mathematics",
         "text": "Clock faces, a strip for the whole day, time lines and double number lines carry each idea: every "
                 "clock has the same three hands in the same three colours, and the time being asked about is the "
                 "largest thing on screen."},
        {"title": "Only the book's numbers",
         "text": "Every time, every clock and every question is the book's own. Any number the plan adds is a "
                 "practice value and is said to be one."},
    ],
}

# {module_id: strand letter}: the subject strand each module belongs to (core/qt.py builds every objective's strand).
# CBSE maths catalog: N Number, A Algebra, G Geometry, M Measurement, D Data, S Statistics and Probability.
MODULE_STRANDS = {"M1": "M", "M2": "M", "M3": "M"}

# every book item, with its kind. Home concepts are listed in DESIGN.md section 3.
NCERT_ITEMS = [
    # the opener: Raghav's yoga clocks and Let us find out
    ("open.story", "text"),
    ("LFO.Q1", "exercise"), ("LFO.Q2", "exercise"), ("LFO.Q3", "exercise"), ("LFO.Q4", "exercise"),
    ("LFO.Q5", "exercise"),
    # 12-hour and 24-hour formats, and the solved example on 24-hour times
    ("LFO.Q6", "exercise"), ("LFO.Q7", "exercise"), ("ex.nana", "example"),
    # School Race and seconds
    ("school.race", "text"), ("school.unit", "text"), ("note.podium", "talk"),
    ("sec.more", "prompt"), ("sec.winner", "prompt"),
    ("LUDunit", "exercise"), ("list.events", "prompt"), ("est.verify", "prompt"),
    ("LF.Q1", "exercise"), ("LF.Q2", "exercise"), ("LF.Q3", "exercise"),
    # the seconds hand
    ("note.hand", "text"),
    ("LUDsec.Q1", "exercise"), ("LUDsec.Q2", "exercise"), ("LUDsec.Q3", "exercise"), ("LUDsec.Q4", "exercise"),
    ("LUDdraw.Q1", "exercise"), ("LUDdraw.Q2", "exercise"), ("LUDdraw.Q3", "exercise"), ("LUDdraw.Q4", "exercise"),
    # conversions
    ("conv.zainab", "text"),
    ("LUDconv.Q1a", "exercise"), ("LUDconv.Q1b", "exercise"), ("LUDconv.Q1c_line", "exercise"),
    ("LUDconv.Q1c_conv", "exercise"), ("LUDconv.Q2", "exercise"),
    # time problems
    ("note.oral", "text"),
    ("LUDtime.Q4", "exercise"), ("LUDtime.Q5", "exercise"), ("LUDtime.Q6", "exercise"), ("LUDtime.Q7", "exercise"),
    ("LUDtime.Q8", "exercise"), ("LUDtime.Q9", "exercise"), ("LUDtime.Q10", "exercise"),
    ("summary", "text"),
]

MISCONCEPTIONS = [
    ("M_TIME_HUNDRED", "An hour has 100 minutes and a minute has 100 seconds, so 1 hour 10 minutes is 110 minutes."),
    ("M_MINUTE_NUMBER", "The number the minute hand points at is the number of minutes, so the minute hand on 7 "
                        "means 7 minutes."),
    ("M_MINUTES_FIRST", "To compare 1 hour 35 minutes and 2 hours 10 minutes, look at the minutes first: 35 is more "
                        "than 10, so 1 hour 35 minutes is longer."),
    ("M_PM_SAME", "A p.m. time keeps its digits in the 24-hour format, so 05:30 p.m. is 05:30 hours."),
    ("M_MINUTES_OVER_59", "Minutes can go past 59 on a clock, so 06:45 plus 30 minutes is 06:75."),
    ("M_BIGGER_TIME_WINS", "In a race the child with the bigger time won."),
    ("M_SMALL_NUMBER_SMALL_UNIT", "55 seconds is more time than 1 minute because 55 is more than 1."),
    ("M_ROUND_ZERO", "If the seconds hand is on the same number at the start and at the end, no time has passed."),
    ("M_HAND_SUBTRACT", "When the seconds hand goes past 12, take the smaller number from the bigger: from 9 to 2 is "
                        "9 − 2 = 7 numbers, 35 seconds."),
    ("M_PAST_24", "A time can go past 24:00 hours, so 8 hours 25 minutes after 08:35 PM is 29:00 hours."),
    ("M_NOON_AM", "A time after 12 noon is still a.m., so 08:30 AM plus 4 hours 10 minutes is 12:40 AM."),
]

SOLUTION_NOTES = [
    {"item": "Let us find out Q1 to Q3: Raghav's yoga clocks",
     "printed_solution": "The book prints no digits and no answer; the two clocks show only hands.",
     "correct": "Measured on the page: the first clock has the minute hand on 7 and the hour hand between 5 and 6, the "
                "second has the minute hand on 11 and the hour hand just before 6. The plan reads 05:35 a.m. and "
                "05:55 a.m. (the book says morning), so 20 minutes. Plan's own reading, to be confirmed."},
    {"item": "Let us find out Q4 and Q5",
     "printed_solution": "No answers are printed; Q4 asks the student to share strategies.",
     "correct": "Worked out: (a) 27 minutes, (b) 5 hours, (c) 2 hours 15 minutes; Q5 the longest time is Rani's "
                "(2 hours 10 minutes), the least is Raghav's (1 hour 20 minutes). One strategy per part is shown; the "
                "student's own strategy may differ."},
    {"item": "Let us find out Q6 and Q7 (12-hour and 24-hour formats)",
     "printed_solution": "Two rows are worked in the table (05:30 a.m. = 05:30 hours, 02:30 p.m. = 14:30 hours); the "
                         "book never states the rule and prints no answers.",
     "correct": "The rule is read from the two worked rows: a.m. keeps its digits, p.m. adds 12 to the hour, the "
                "minutes never change. Q6: 08:35 hours is 08:35 a.m.; 11:55 a.m. is 11:55 hours; 05:30 p.m. is 17:30 "
                "hours; 09:35 p.m. is 21:35 hours. Q7: 06:30 a.m. with 06:30 hours, 08:45 p.m. with 20:45 hours, "
                "11:45 p.m. with 23:45 hours, 04:30 a.m. with 04:30 hours, 07:30 p.m. with 19:30 hours, 01:30 a.m. "
                "with 01:30 hours. The book shows no 12:xx a.m. time; the plan uses none."},
    {"item": "Opener and School Race: which child is which",
     "printed_solution": "The book names Akira, Sunita and Mary but never matches a name to a child on the winners' "
                         "stand; the track picture shows four children, the stand three.",
     "correct": "The plan answers 'the child on the first stand won, with 01:55, 1 minute 55 seconds' and gives no "
                "name. Each child took 1 minute and 55, 56 and 57 seconds more."},
    {"item": "Raghav and Raghu",
     "printed_solution": "Both spellings are used in the clock boxes of pp. 159 and 160.",
     "correct": "The plan keeps both as printed and does not decide whether they are one boy or two."},
    {"item": "Let Us Do: seconds or minutes (p. 157)",
     "printed_solution": "The student estimates; no answers are printed.",
     "correct": "The plan's reading: seconds for blinking, switching the lights on and off, counting 1 to 20, filling a "
                "glass from the tap, sitting down on the floor, drinking a glass of water, snapping fingers and "
                "washing hands; minutes for melting an ice-cube and making a phone call. The student's own estimate "
                "may differ for the last two and for washing hands."},
    {"item": "The open activities of p. 158 (list events, estimate and verify, skip the rope, write FRIEND, run 100 m)",
     "printed_solution": "They depend on the student; no answer is printed.",
     "correct": "The plan gives one labelled Sample answer with practice values (said to be practice values) and says "
                "the student's answer may differ."},
    {"item": "Let Us Do on the seconds hand, p. 159 and p. 160",
     "printed_solution": "No answers are printed; the pictures are approximate.",
     "correct": "p. 159: Rani 30 seconds (12 to 6), Raghav 35 seconds (12 to 7), Ritu 15 seconds (9 to 12), Raghu 60 "
                "seconds (the seconds hand is on 5 both times and the minute hand has moved one mark). p. 160: the "
                "missing seconds hand goes on 4 (20 seconds), on 6 (30 seconds), on 9 again with the minute hand one "
                "mark on (60 seconds), and on 7 (55 + 40 = 95, 95 − 60 = 35 seconds). In the fourth picture the book "
                "draws the minute hand still on 12; one minute has passed in the plan's reading."},
    {"item": "Double number lines of p. 161 and p. 162",
     "printed_solution": "The blanks are not printed.",
     "correct": "The tick spacing is equal, so the blanks are: (a) above 2, 8, 11, 12 hr and below 240, 420, 540 min; "
                "(c) above 2, 20, 25 min and below 300, 600, 900 sec."},
    {"item": "Let Us Do Q1 (b) (i): '1 hours 10 minutes'",
     "printed_solution": "The book writes '1 hours'.",
     "correct": "The plan writes 1 hour 10 minutes (same meaning)."},
    {"item": "Zainab and Remo's speech bubbles (p. 161)",
     "printed_solution": "The book writes 'As 3 hrs = 3 times 60 = 180 min.'",
     "correct": "The plan's quotation of the bubble writes 3 × 60 in place of '3 times 60', so that the arithmetic gate can "
                "read the chain; the meaning is the same."},
    {"item": "Printed-book slips",
     "printed_solution": "'fromat' in both headings of the 12-hour and 24-hour table; en dashes in '12-hour', '24-hour' "
                         "and '1 to 20'; a.m./p.m. on pp. 155 to 156 but AM/PM on p. 163; the minute hand is green on "
                         "p. 159 and orange on pp. 155 and 160.",
     "correct": "The plan writes 12-hour and 24-hour, and 1 to 20; keeps each question's own a.m./p.m. or AM/PM "
                "style; draws every minute hand orange."},
    {"item": "Let Us Do Q10 (p. 163): 08:35 PM and 8 hours 25 minutes",
     "printed_solution": "The book teaches nothing about crossing midnight and prints no answer.",
     "correct": "20:35 + 8:25 = 29:00 hours; the day ends at 24:00, so 29:00 is 05:00 the next day: 05:00 AM. Plan's "
                "reading, to be confirmed."},
    {"item": "Let Us Do Q6 and Q9 (p. 163): across 12 noon",
     "printed_solution": "No answers are printed.",
     "correct": "08:30 AM + 4 hours 10 minutes = 12:40 PM; 12:30 PM + 35 minutes = 01:05 PM. The label changes to PM "
                "at 12 noon (the book's own Q9 starts at 12:30 PM)."},
    {"item": "Let Us Do Q3 (p. 162): solved in the book",
     "printed_solution": "The book prints the answer in a speech bubble: 1 hour 5 minutes.",
     "correct": "Kept as the book's solved example; the plan shows the steps (08:00 to 09:00 is 1 hour, 09:00 to 09:05 "
                "is 5 minutes)."},
    {"item": "Notes for the Teachers (p. 157 and p. 163)",
     "printed_solution": "Two notes: discuss who stood first, second and third, and that 60 movements of the seconds "
                         "hand shift the minute hand; solve the problems orally, not in columns.",
     "correct": "Folded into the teaching lines and the solutions, with no role for a teacher."},
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
# hook and summary concept where a drawn figure is the maths; the tool concepts (Practice / free try) and the concepts
# whose idea is a judgement or a comparison of numbers have no image (media_specs/ gives the reason).
FIGURES = {
    "T1.C1": ["Two wall clocks above a yoga mat, before and after: the first with the minute hand on 7 and the hour hand "
              "between 5 and 6, the second with the minute hand on 11 and the hour hand just before 6. No times "
              "written."],
    "T1B.C1": ["A time line from 04:25 p.m. to 05:10 p.m. with a hop of 35 minutes up to the 5 o'clock mark and a hop of "
               "10 minutes after it, 45 minutes in all."],
    "T2.C1": ["A strip for the whole day from 00:00 to 24:00, the a.m. half and the p.m. half, with 07:45 p.m. marked and "
              "its 24-hour name 19:45 hours."],
    "T2.C2": ["A time line from 13:40 hours to 16:15 hours with hops of 20 minutes, 2 hours and 15 minutes."],
    "T3.C1": ["A race clock reading 01:48 (minutes and seconds) and a bar of 60 seconds with 48 seconds more marked."],
    "T4.C1": ["Two clocks, the seconds hand on 3 and on 8, with the stretch between them shaded and counted in fives."],
    "T4.C2": ["A clock with the seconds hand on 10 and a pale hand on 3 after 25 seconds, the arc past 12, and the minute "
              "hand one mark on."],
    "T5.C1": ["A double number line, hours above and minutes below, from 0 to 6 hours with the multiply by 60 arrow."],
    "T5.C2": ["A double number line, minutes above and seconds below, from 0 to 5 minutes with the multiply by 60 arrow."],
    "T6.C1": ["A time line from 03:20 p.m. to 05:10 p.m. with a hop of 1 hour and then hops of 40 minutes and 10 minutes."],
    "T6.C2": ["A time line going back from 08:15 p.m. to 05:35 p.m. with a hop back of 2 hours and then hops back of 15 "
              "minutes and 25 minutes."],
    "T6.C3": ["A time line across midnight from 10:00 p.m. to 05:00 a.m. with midnight marked at 24:00 hours, a trip from "
              "10:15 p.m. to 04:00 a.m. the next day, and the 24-hour count going on to 28:00 hours."],
    "T7.C1": ["The two time ladders of the chapter: 1 hour = 60 minutes and 1 minute = 60 seconds with multiply by 60 "
              "arrows, and the 12-hour and 24-hour names of one afternoon time."],
}
