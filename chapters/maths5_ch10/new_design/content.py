# -*- coding: utf-8 -*-
"""Chapter-level content for Class 5 Chapter 10, Symmetrical Designs (Maths Mela, Grade 5, Chapter 10).

The plan follows the "Class 5 Mathematics Learning Experience Designer" brief (priority_doc.md sections A to F) and the
/lp pipeline's structure; the book decides every letter, digit, design and question. Book lines are verbatim except: the
book's dashes become commas, colons or "to"; minus is U+2212; fractions are written a/b; the book's "(tick)" symbol is
written "tick mark". No em dash and no en dash anywhere here."""
from __future__ import annotations

CHAPTER = {
    "grade": 5,
    "label": "Class 5",
    "chapter_no": 10,
    "name": "Symmetrical Designs",
    "book_part": "Maths Mela, Grade 5, Chapter 10",
    "source_pdf": "textbooks/class-5/eemm110.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Folding and Lines of Symmetry",
     "Cutting letters from folded paper by drawing half or a quarter of them, and finding the horizontal and vertical "
     "lines of symmetry of a letter."),
    ("M2", "Turning and Rotational Symmetry",
     "Quarter, half and three-quarter turns, the windmill firki, shapes that look the same after a turn, and telling "
     "reflection symmetry from rotational symmetry in letters, digits and numbers."),
    ("M3", "Designs, Block Prints and Revision",
     "Making designs that look the same after a turn and finding their lines of symmetry, block printing, shapes on "
     "the border, a project with vegetable blocks, and a revision of the whole craft table."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter takes place at Lali's craft table. Paper cutouts, a windmill firki, wooden printing blocks and "
             "cards of letters and digits show what a line of symmetry is, what it means for a shape to look the same "
             "after a turn, and how to tell the two apart. A short video explains each idea, and an interactive tool "
             "lets the student try it alone.",
    "points": [
        {"title": "Videos teach, tools explore",
         "text": "Every idea has one short concept video. The tool that follows is where the student explores, "
                 "builds and checks the idea alone, with hints, retry and reset. Four tools, each with its own "
                 "purpose, follow the chapter's own plan."},
        {"title": "A tool in three steps",
         "text": "Each tool opens with a short recall of the video idea, then lets the student play and apply it, and "
                 "ends with the chapter's own question, used exactly as the book gives it."},
        {"title": "Every book question has its own video",
         "text": "Every solved example, Let Us Do question and every answerable prompt of the book is its own short "
                 "video with a step by step solution and a question picture and a solution picture, in a Questions "
                 "topic that follows the idea it practises."},
        {"title": "Two tests for symmetry",
         "text": "A fold line tests reflection symmetry and a turn tests rotational symmetry. A shape can pass one, "
                 "both or neither, so the student runs both tests every time."},
        {"title": "Only the book's shapes",
         "text": "Letters, digits, designs and block prints are the book's own. Any shape or number the plan adds is "
                 "a practice value and is said to be one."},
    ],
}

# {module_id: strand letter}: the subject strand each module belongs to (core/qt.py builds every objective's strand).
# CBSE maths catalog: N Number, A Algebra, G Geometry, M Measurement, D Data, S Statistics and Probability.
MODULE_STRANDS = {"M1": "G", "M2": "G", "M3": "G"}

# every book item, with its kind. Home concepts are listed in DESIGN.md section 3.
NCERT_ITEMS = [
    # the opener: Alphabet Cutout
    ("open.story", "text"), ("open.A", "text"), ("open.H", "text"),
    ("open.cutouts", "prompt"), ("open.lines", "prompt"), ("open.diya", "exercise"),
    # Let Us Make a Windmill Firki and the turning table
    ("firki.steps", "text"), ("firki.tips", "text"), ("firki.same", "prompt"),
    ("rot.method", "text"), ("rot.H", "example"), ("rot.IXY", "prompt"), ("rot.box", "text"),
    # Let Us Do: digits
    ("dig.sym", "exercise"), ("dig.nums", "exercise"), ("dig.examples", "exercise"),
    # Making Designs, Let Us Think, Let Us Do (squares and triangles)
    ("mk.design", "prompt"),
    ("lt.half_quarter", "prompt"), ("lt.colour", "prompt"), ("lt.reflection", "prompt"),
    ("sq.make", "exercise"), ("sq.shape", "exercise"), ("sq.sort", "exercise"),
    # Let Us Explore (block printing), designs A and B, the border shapes, the project
    ("block.intro", "text"), ("block.example", "text"), ("bp.match", "prompt"),
    ("block.A", "text"), ("bp.designB", "prompt"),
    ("bd.border", "exercise"), ("pw.veg", "prompt"),
    # the summary
    ("summary", "text"),
]

MISCONCEPTIONS = [
    ("M_ANY_LINE", "Any line through the middle of a shape is a line of symmetry, even when the two halves do not "
                   "match."),
    ("M_FULL_TURN", "Every shape has rotational symmetry, because every shape looks the same after a full turn."),
    ("M_DOT_MOVES", "If the dot moves after a turn, the shape looks different."),
    ("M_BOTH_ALWAYS", "A shape that has one kind of symmetry has the other kind too: a letter with a line of symmetry "
                      "also looks the same after a turn."),
    ("M_ONE_LINE", "A symmetrical shape has just one line of symmetry."),
    ("M_SIX_NINE", "The digits 6 and 9 have rotational symmetry, because a half turn turns one into the other."),
    ("M_HALF_IMPLIES_QUARTER", "A design that looks the same after a 1/2 turn also looks the same after a 1/4 turn."),
    ("M_COLOUR_IGNORED", "Colours do not matter when checking symmetry: only the shape counts."),
    ("M_FLIP_IS_TURN", "Turning a shape by a 1/2 turn is the same as folding it over a line of symmetry."),
]

SOLUTION_NOTES = [
    {"item": "Squares and equilateral triangles (Let Us Do on squares and triangles)",
     "printed_solution": "The book says the squares and equilateral triangles with the same side length are provided at "
                         "the end of the book.",
     "correct": "The sheet is supplied: the Learning Material Sheet Tessellation and Shapes (the 15th PDF page of the "
                "Class 5 Chapter 15 file) holds 6 squares (side 38 on the sheet) and 6 equilateral triangles (base 38, "
                "height 33, so the same side as the squares), and also 6 five-sided shapes, 6 six-sided shapes, 6 "
                "circles and two cut-out puzzles, which this chapter does not use. The plan uses only the squares "
                "and the triangles, at most 6 of each (its sample designs use 1 square and 4 triangles at most). The "
                "squares are light blue and the triangles pink on the sheet. Nothing is assumed."},
    {"item": "The triangles in the pictures of the squares and triangles activity",
     "printed_solution": "The text says equilateral triangles; in the pictures of the activity each triangle is as tall "
                         "as it is wide (height 48 on a base of 48, so the other two sides are 54).",
     "correct": "The triangles on the sheet are equilateral (base 38, height 33), so the plan follows the words and "
                "the sheet. The symmetry answers are the same either way."},
    {"item": "Let Us Do on the digits",
     "printed_solution": "The book prints no answer. It draws the digit 1 as a plain bar and draws 3 and 8 with a "
                         "slightly smaller top.",
     "correct": "The plan reads 1 as the bar and reads 3 and 8 as having two equal halves. Reflection symmetry: 0, 1, 3, "
                "8. Rotational symmetry: 0, 1, 8. Both: 0, 1, 8. 6 and 9 turn into each other, so neither looks the "
                "same after a 1/2 turn by itself. Plan's own reading."},
    {"item": "Let Us Do on the numbers 11 and 1001 and the examples of 2-, 3- and 4-digit numbers",
     "printed_solution": "The book prints no answer.",
     "correct": "11 and 1001 have both symmetries. Sample examples: rotation only 69, 619, 6969; reflection only 38, "
                "383, 3883 (a horizontal line); both 88, 808, 8118. The plan says the student's answer may differ."},
    {"item": "How many times does this shape look the same during a full turn (Let Us Think)",
     "printed_solution": "The book prints no answer.",
     "correct": "The plan counts the 1/4, 1/2, 3/4 and full turn: 4 times. If the book means only the turns before the "
                "full turn, the count is 3. To be confirmed."},
    {"item": "Let Us Think: colour the square and the reflection question",
     "printed_solution": "The book prints no answer.",
     "correct": "A colouring that looks the same after every 1/4 turn must alternate the two colours on the 8 triangles; "
                "such a design has no line of symmetry. The green and pink square has 2 lines of symmetry, its two "
                "diagonals. Plan's own reading."},
    {"item": "Making Designs (b) and (c), and the designs the student makes",
     "printed_solution": "The book prints no answer; these are open.",
     "correct": "The plan gives one sample design for each and says the student's design may differ."},
    {"item": "The border shapes (Let Us Do, shapes on the border)",
     "printed_solution": "The book prints no answer and does not number the shapes.",
     "correct": "The plan numbers the 19 shapes 1 to 19 round the border from the top-left corner, going to the right, "
                "then down, then to the left, then up. Reflection symmetry: all except 13 and 15. Rotational "
                "symmetry: all except 15. The turns of some shapes are 1/3, 1/5, 1/6 and 1/7 of a full turn, which the "
                "chapter has not named. Shapes 4 (three circles and a Y) and 9 (a ring of small triangles) are drawn "
                "a little unevenly and are read as even. Measured on the page's drawing. To be confirmed."},
    {"item": "Let Us Explore: match the blocks to the prints",
     "printed_solution": "The book prints only the line from (iv) to (e).",
     "correct": "Worked out from the pictures: (i) to (c), (ii) to (d), (iii) to (a), (v) to (b). Each print shows half "
                "of its block along the block's line of symmetry."},
    {"item": "Design A and design B",
     "printed_solution": "The book prints that design A looks the same after every 1/4 turn and leaves two blanks for "
                         "design B.",
     "correct": "Design A is kept as a printed fact (text). Design B: every 1/4 turn; both rotational and reflection "
                "symmetry (the dashed lines show the vertical and the horizontal line)."},
    {"item": "Alphabet Cutout: the letter questions",
     "printed_solution": "The book prints no answer.",
     "correct": "Read for plain sans-serif capitals. Can be cut by drawing half or a quarter: E, X, T, K, V, O. N cannot "
                "(no line of symmetry). Horizontal: E, X, K, O. Vertical: X, T, V, O. Both: X, O. The plan letters the "
                "three blanks (a), (b), (c). Measured on the printed K, a horizontal fold matches only roughly "
                "(60%): it is read as symmetric, as the choice of the seven letters suggests."},
    {"item": "The turning table (I, X and Y) and the firki question",
     "printed_solution": "The book fills in the row of H only.",
     "correct": "H (printed): yes, at 1/2 turn. I: yes, at 1/2 turn. X: yes, at 1/4 turn. Y: no. The firki looks the "
                "same after 1/4, 1/2, 3/4 and a full turn. The book gives no turn direction, so the plan turns shapes "
                "to the right, the same way each time."},
    {"item": "Let Us Do on the border: the tick",
     "printed_solution": "The book writes Put a (tick symbol) mark.",
     "correct": "The plan writes Put a tick mark."},
    {"item": "Wording of the question cards that the LaTeX converter cannot read",
     "printed_solution": "The book writes digit(s), shape(s), line(s), 2-, 3-, and 4-digit, and the options (a), (b), (c) "
                         "of the question on the numbers 11 and 1001.",
     "correct": "The plan writes digits, shapes, lines, 2-digit, 3-digit and 4-digit, and drops the printed options "
                "(the question then reads: Do these have rotational symmetry, reflection symmetry or both "
                "symmetries?). The meaning is the book's."},
    {"item": "Open activities (diya and boat cutouts, designs, sorting, project work)",
     "printed_solution": "No single answer.",
     "correct": "The plan gives one reasoned sample answer and says the student's answer may differ."},
    {"item": "Brief: revision video",
     "printed_solution": "The brief asks for an interactive recap or revision video.",
     "correct": "The pipeline has no recap video, so the last topic is a text summary with short concept checks."},
]
ERRATA = []

DESIGN_REFERENCES = [
    {"text": "priority_doc.md (the plan written to the 'Class 5 Mathematics Learning Experience Designer' brief, "
             "2026-11-06): topic flow, video types, the 4 tools, the shared visual language and the learning rules "
             "decide this chapter's design.", "url": ""},
    {"text": "docs/01_runbook.md and .claude/skills/lp/SKILL.md: framing intro with a free-try tool, idea topics each "
             "ending in a Practice concept, a Questions topic after every idea topic with a question concept and an "
             "answer concept per book question, and one summary topic.", "url": ""},
]

# The book's own figures that carry mathematics, keyed by authored concept key. One concept image per teaching,
# hook and summary concept where a drawn figure is the maths; the tool concepts (Practice / free try) are pictured by
# their tool.
FIGURES = {
    "T1.C1": ["Four pictures in a row: a square paper folded in half with a dashed vertical fold line, half of the "
              "letter A drawn along the fold, the half A cut out, and the opened paper showing the full letter A."],
    "T1B.C1": ["A square paper folded in half along a dashed vertical line with half of the letter M drawn along the "
               "fold, beside the opened paper showing the full M."],
    "T1B.C2": ["The letters B, W and H, each with its lines of symmetry as dashed lines: a horizontal line on B, a "
               "vertical line on W, both lines on H."],
    "T2.C1": ["A pinwheel with four blades and a dot on the top blade, shown at the start and after a 1/4 turn, a 1/2 "
              "turn and a 3/4 turn, with the dot on the right, bottom and left blade."],
    "T2.C2": ["The letter Z at the start, after a 1/4 turn (it lies on its side) and after a 1/2 turn (it looks the "
              "same), beside the letter T after a 1/2 turn (upside down, not the same)."],
    "T3.C1": ["Three cards: M with a dashed vertical line, S with a curved arrow for a 1/2 turn, and a plus sign with "
              "dashed lines and a curved arrow for a 1/4 turn."],
    "T4.C1": ["A circle with a triangle above it, then the same design with a triangle added below it, then with "
              "triangles at the left and the right too."],
    "T4.C2": ["A square cut by its two diagonals into 4 triangles, the top and bottom orange and the left and right "
              "blue, with a dashed vertical line and a dashed horizontal line."],
    "T5.C1": ["A leaf-shaped block, its half print with a straight edge on the right, and the whole print made of the "
              "half and its copy on the other side of the edge."],
    "T5.C2": ["A flower block stamped twice, one flower at the top and one at the bottom, with a curved arrow for the "
              "1/2 turn between the stamps."],
    "T6.C1": ["A craft table with a letter A cutout with a dashed line, a pinwheel with a curved arrow and a letter H "
              "with dashed lines and a curved arrow, one for each kind of symmetry of the chapter."],
}
