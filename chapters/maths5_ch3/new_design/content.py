# -*- coding: utf-8 -*-
"""Chapter-level content for Class 5 Chapter 3, Angles as Turns (Maths Mela, Grade 5, Chapter 3).

The plan follows the "Class 5 Mathematics Learning Experience Designer" brief (priority_doc.md sections A to F) and the
/lp pipeline's structure; the book decides every number and every question. Book lines are verbatim except: the book's
dashes become commas, colons or "to"; minus is U+2212; fractions are written a/b; where the book says "she" about Reema
or Padma, the card names her so that it stands alone. The chapter measures an angle only as a part of a turn: no degrees
anywhere. No em dash and no en dash anywhere here."""
from __future__ import annotations

CHAPTER = {
    "grade": 5,
    "label": "Class 5",
    "chapter_no": 3,
    "name": "Angles as Turns",
    "book_part": "Maths Mela, Grade 5, Chapter 3",
    "source_pdf": "textbooks/class-5/eemm103.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Turns and Angles",
     "Full turns and half turns in games, clocks and wheels, halves and quarters that make a full turn, how far "
     "everyday things turn, and the right, acute, obtuse and straight angles that a turn makes."),
    ("M2", "Measuring Turns",
     "Measuring turns with a circle cut into 8, 6 and 12 equal parts, guessing and checking the angles in pictures, "
     "drawing angles for given turns, and the turn of the minute hand."),
    ("M3", "Direction and Revision",
     "Clockwise and anti-clockwise, finding the direction faced after right-angle turns, and a revision of the whole "
     "playground of turns."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter takes place on a school playground and its fair. Children turn on the spot, a giant wheel "
             "comes back to its starting seat, a straw and a paper fan turn, and a minute hand goes round. Turning "
             "shows what an angle is, how to name it and how to measure it as a part of a turn. A short video "
             "explains each idea, and an interactive tool lets the student try it alone.",
    "points": [
        {"title": "Videos teach, tools explore",
         "text": "Every idea has one short concept video. The tool that follows is where the student explores, "
                 "turns, measures and checks the idea alone, with hints, retry and reset. Seven tools, each with its "
                 "own purpose, follow the chapter's own plan."},
        {"title": "A tool in three steps",
         "text": "Each tool opens with a short recall of the video idea, then lets the student play and apply it, and "
                 "ends with the chapter's own question, used exactly as the book gives it."},
        {"title": "Every book question has its own video",
         "text": "Every Let Us Do part, Let Us Think question, Fun with Turns question and every answerable prompt of "
                 "the book is its own short video with a step by step solution and a question picture and a "
                 "solution picture, in a Questions topic that follows the idea it practises."},
        {"title": "An angle is a turn",
         "text": "Every angle is shown as a start mark, a turning arm and the part of a full turn it has made. "
                 "Angles are measured as parts of a full turn: halves, quarters, eighths, sixths and "
                 "twelfths."},
        {"title": "Only the book's numbers",
         "text": "The pieces, the clock positions, the compass and every question are the book's own. Any number the "
                 "plan adds is a practice value and is said to be one."},
    ],
}

# {module_id: strand letter}: the subject strand each module belongs to (core/qt.py builds every objective's strand).
# CBSE maths catalog: N Number, A Algebra, G Geometry, M Measurement, D Data, S Statistics and Probability.
MODULE_STRANDS = {"M1": "G", "M2": "G", "M3": "G"}

# every book item, with its kind. Home concepts are listed in DESIGN.md section 3. The two "Note for Teachers" boxes
# (pages 32 and 37) give a teacher a role and are not student items: they are left out on purpose.
NCERT_ITEMS = [
    # the opener and the statue game
    ("open.story", "text"), ("open.statue", "prompt"), ("open.examples", "talk"),
    ("open.circles", "text"), ("open.minute", "text"),
    # the giant wheel, Reema, everyday objects
    ("turn.wheel", "text"), ("reema.half", "prompt"), ("reema.quarter2", "prompt"), ("reema.quarter4", "prompt"),
    ("objects.list", "prompt"), ("objects.table", "prompt"), ("objects.half", "prompt"), ("objects.full", "prompt"),
    # Pragya's straws, the paper fan, Let Us Do (a) to (d)
    ("straws.setup", "text"), ("angles.names", "text"), ("angles.straight", "text"), ("angles.arise", "text"),
    ("fan.make", "text"), ("LUDa.fan", "exercise"), ("fan.table", "text"), ("fan.circles", "text"),
    ("fan.acute2", "exercise"), ("LUDb.house", "exercise"), ("LUDc.pentagon", "exercise"),
    ("LUDd.gymnasts", "exercise"),
    # Angle Measuring Tool, Let Us Think
    ("amt.make", "text"), ("amt.show", "prompt"), ("amt.2of8", "prompt"), ("amt.4of8", "prompt"),
    ("amt.continue", "prompt"), ("amt.cut", "text"), ("LUT.Q1", "exercise"),
    ("sixth.make", "text"), ("sixth.show", "prompt"), ("sixth.cut", "text"), ("sixth.half", "prompt"),
    # Let Us Do (pages 38 and 39)
    ("LUD2.Q1", "exercise"), ("LUD2.Q2", "exercise"), ("LUD2.Q3", "exercise"), ("LUD2.Q4", "exercise"),
    ("LUD2.Q5", "exercise"), ("LUD2.Q6", "exercise"),
    # clockwise and anti-clockwise, Fun with Turns
    ("dir.def", "text"), ("dir.creatures", "prompt"), ("dir.try", "prompt"),
    ("FWT.Q1", "exercise"), ("FWT.Q2", "exercise"), ("FWT.Q2b", "exercise"),
    ("summary", "text"),
]

MISCONCEPTIONS = [
    ("M_SAME_FACING_NO_TURN", "A child who faces the same way as at the start has not turned at all."),
    ("M_ARM_LENGTH", "A longer arm, or longer lines, make a bigger angle."),
    ("M_ACUTE_ADD_ACUTE", "Two acute turns together always make another acute turn."),
    ("M_STRAIGHT_NOT_ANGLE", "A straight line is not an angle, and a turn of more than a half turn is not an angle."),
    ("M_BIGGER_DENOM_TURN", "A 1/8 turn is bigger than a 1/4 turn, because 8 is bigger than 4."),
    ("M_CLOCK_FROM_12", "The minute hand always turns from the 12, not from the place where it starts."),
    ("M_DIR_SAME_END", "A turn ends in the same place whichever way you turn, so clockwise and anti-clockwise "
                       "do not matter."),
]

SOLUTION_NOTES = [
    {"item": "Notes for Teachers (the two boxes in the chapter)",
     "printed_solution": "Two boxes tell a teacher to play the statue game and to help learners make the angle "
                         "measuring tools.",
     "correct": "The plan gives a teacher no teaching role, so the boxes are not made into content. The statue game "
                "is in the hook, and the tracing-paper tools are replaced by on-screen discs and pieces (Tools 4 "
                "and 5)."},
    {"item": "Fun with Turns, Q1, last row (West, right angles clockwise, four 1/2 right angles anti-clockwise)",
     "printed_solution": "The number in front of 'right angles clockwise' is not printed; the ending direction box "
                         "is empty.",
     "correct": "Four 1/2 right angles are 2 right angles anti-clockwise, so the end is the start turned (that "
                "number − 2) right angles clockwise. The plan shows this rule and one sample: if the number is 3, "
                "West ends at North. To be confirmed with the intended number."},
    {"item": "The statue picture: who made a full turn",
     "printed_solution": "The book asks for the child who has made a full turn, in the singular.",
     "correct": "B and C both face the front, as at the start, so the plan reads both as a full turn; A faces "
                "away, a half turn; D faces the side, neither. To be confirmed."},
    {"item": "The notebook house, angles A to H",
     "printed_solution": "The book prints no answers.",
     "correct": "Read from the red arcs: A obtuse, B right, C acute, D acute, E acute, F right, G right, H obtuse. "
                "The picture is drawn in perspective; to be confirmed."},
    {"item": "Let Us Do, Q1, seven angles on a dotted grid",
     "printed_solution": "The angles carry no letters or numbers and the book prints no answers.",
     "correct": "The plan numbers them 1 to 7 from the left (4 is the upper of the two in the middle) and reads "
                "them from the drawn lines: about 1/12, 1/6, 1/8, 1/6, 1/4, 1/3, 3/8 of a turn, named acute, "
                "acute, acute, acute, right, obtuse, obtuse. The question says guess, so the answers are about."},
    {"item": "Let Us Do, Q2 (d)",
     "printed_solution": "The arrow turns from the upper right to a little left of straight down; the book prints "
                         "only part (a).",
     "correct": "(b) 5/8 and (c) 1/8 are exact. (d) is read as about 5/12 = 1/4 + 1/6, the nearest turn that the "
                "chapter's pieces make. A guess; to be confirmed."},
    {"item": "Let Us Do, Q4, five given lines",
     "printed_solution": "Each line has a dot at both ends and the book does not say which end is the corner.",
     "correct": "The plan lets the student take either end as the corner."},
    {"item": "Let Us Think, Q1",
     "printed_solution": "The book does not say which way the turns go.",
     "correct": "The green dashed arrows go the way the hands of a clock move, so the plan turns back from the end "
                "arrow in the anti-clockwise way to find the start. The words clockwise and anti-clockwise only "
                "come later in the chapter."},
    {"item": "Everyday objects: list, table, half turn and full turn",
     "printed_solution": "The book asks the student to check real objects and prints no answers.",
     "correct": "Sample answers for common objects: clothes clip less than 1/4 turn, door more than 1/4, tongs "
                "less than 1/4, scissors 1/4, file cover more than 1/4; half turn: door and file cover; full "
                "turn: none. The student's own objects may differ."},
    {"item": "Which Direction: tap, lid and nut",
     "printed_solution": "The book asks the student to observe and prints no answer.",
     "correct": "Usually all three turn anti-clockwise to open, unscrew or loosen. A sample answer; a tap may "
                "differ."},
    {"item": "Let Us Do (a): can two acute turns together make another acute turn",
     "printed_solution": "The book prints no answer.",
     "correct": "Sometimes: two small acute turns can still be acute; two bigger acute turns can make a right "
                "angle or an obtuse angle."},
    {"item": "Let Us Do (c): a 5-sided shape with 2 right angles, 2 obtuse angles and 1 acute angle",
     "printed_solution": "Many shapes fit; the book prints no answer.",
     "correct": "The plan gives one sample, a house shape on a square grid. The student's shape may differ."},
    {"item": "Let Us Do, Q5, 1/8 + 1/6 turn",
     "printed_solution": "The book asks to draw the angle.",
     "correct": "The plan names the angle by comparing with 1/4 and 1/2: 1/6 is more than 1/8, so the sum is more "
                "than 1/8 + 1/8 = 1/4, and it is less than 1/4 + 1/4 = 1/2: an obtuse angle."},
    {"item": "Paper, straws, ice cream sticks, tracing paper and paper clips",
     "printed_solution": "The chapter says how to make each piece; no kit or cut-out sheet is referred to.",
     "correct": "The plan uses only the pieces the chapter names (circles in 8, 6 and 12 equal parts, 1/8, 2/8, 1/6, "
                "2/6 and 1/12 pieces) as on-screen pieces. No printed sheet is missing."},
    {"item": "Fun with Turns, Q1 and the creatures: part letters",
     "printed_solution": "The creatures and the table rows carry no letters.",
     "correct": "The plan letters them (a) onward in reading order: creatures ladybug, snail, bee, ant; table "
                "rows from the top."},
    {"item": "Brief: revision video",
     "printed_solution": "The brief asks for an interactive recap or revision video.",
     "correct": "The pipeline has no recap video, so the last topic is a text summary with short concept checks."},
    {"item": "Open prompts (examples of turns, everyday objects, a 5-sided shape, a paper fan)",
     "printed_solution": "No single answer.",
     "correct": "The plan gives one reasoned sample answer and says the student's answer may differ."},
]
ERRATA = []

DESIGN_REFERENCES = [
    {"text": "priority_doc.md (the plan written to the 'Class 5 Mathematics Learning Experience Designer' brief, "
             "2026-11-06): topic flow, video types, the 7 tools, the shared visual language and the learning rules "
             "decide this chapter's design.", "url": ""},
    {"text": "docs/01_runbook.md and .claude/skills/lp/SKILL.md: framing intro with a free-try tool, idea topics each "
             "ending in a Practice concept, a Questions topic after every idea topic with a question concept and an "
             "answer concept per book question, and one summary topic.", "url": ""},
]

# The book's own figures that carry mathematics, keyed by authored concept key. One concept image per teaching,
# hook and summary concept where a drawn figure is the maths; the tool concepts (Practice / free try) are pictured by
# their tool.
FIGURES = {
    "T1.C1": ["Four children in a row on a playground, A, B, C and D, all facing the front, and the same four after "
              "the call STATUE with one facing away, two facing the front and one facing the side."],
    "T1B.C1": ["A child standing on a ring on the ground, with a start arrow, a full circle drawn by the free foot, "
               "and a half-moon drawn by the free foot; a clock face with the minute hand back where it started."],
    "T2.C1": ["A giant wheel with the starting seat at the top and curved arrows showing 1 half turn and 2 quarter "
              "turns joining into a full turn."],
    "T2B.C1": ["Three hinges with a square-corner guide: one opening exactly to the guide, one less, one more."],
    "T3.C1": ["A paper fan opened at three places, each with its angle marked: a quarter turn, a little less, and "
              "between a quarter and a half."],
    "T3.C2": ["A paper fan opened to a half turn and then a further quarter turn, with the 3/4 turn marked."],
    "T4.C1": ["A circle folded into 8 equal parts with a straw on the starting point and the turns 5/8 and then 2/8 "
              "more marked."],
    "T4.C2": ["A circle in 6 equal parts, and one 1/6 part folded in half into two 1/12 parts."],
    "T5.C1": ["An angle covered by one 1/6 piece and one 1/12 piece side by side."],
    "T5B.C1": ["A line with a 1/2 piece and then a 1/12 piece laid after it, and the second line drawn along the last "
              "piece."],
    "T6.C1": ["A clock face with the minute hand at 2 and at 7 and the 5 minute pieces between them."],
    "T7.C1": ["An arrow pointing down and the same arrow pointing left after a quarter turn, with a small clock showing "
              "the way a clock moves."],
    "T7.C2": ["A compass with North, East, South and West and a child at the centre turning 3 right angles "
              "anti-clockwise from West."],
    "T8.C1": ["A playground showing a child turning, a giant wheel, a straw and fan, a disc, a clock and a compass, one "
              "for each idea of the chapter."],
}
