# -*- coding: utf-8 -*-
"""Chapter-level content for Class 5 Chapter 11, Grandmother's Quilt (Maths Mela, Grade 5, Chapter 11).

The plan follows the "Class 5 Mathematics Learning Experience Designer" brief (priority_doc.md sections A to F) and the
/lp pipeline's structure; the book decides every number and every question. Book lines are verbatim except: the book's
dashes become commas, colons or "to"; minus is U+2212; "give below" in the mats question is corrected to "given below".
No em dash and no en dash anywhere here."""
from __future__ import annotations

CHAPTER = {
    "grade": 5,
    "label": "Class 5",
    "chapter_no": 11,
    "name": "Grandmother's Quilt",
    "book_part": "Maths Mela, Grade 5, Chapter 11",
    "source_pdf": "textbooks/class-5/eemm111.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Perimeter, Tiles and Area",
     "Finding the lace for the border of a quilt as the perimeter of a shape, covering a surface with tiles that leave "
     "no gaps, naming the region covered as its area, and comparing areas by counting unit squares on a grid."),
    ("M2", "Area and Perimeter of Rectangles",
     "Seeing that area and perimeter are different measures, finding the area and the perimeter of rectangles and "
     "squares with the book's rules, and using the rules for a missing side, a side given in parts and real objects."),
    ("M3", "A Tile Game and Revision",
     "Counting the outer edges of a figure of square tiles to play the perimeter 24 game, and a revision of the whole "
     "patchwork room."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter takes place in Grandmother's patchwork room. A quilt, a rug, table tops, a desk, grids, mats "
             "and square tiles are the shapes, and laying lace round them, covering them with tiles and counting "
             "squares shows what the perimeter and the area of a shape are, how they differ, and how to find them for "
             "rectangles and squares. A short video explains each idea, and an interactive tool lets the student try "
             "it alone.",
    "points": [
        {"title": "Videos teach, tools explore",
         "text": "Every idea has one short concept video. The tool that follows is where the student explores, "
                 "builds and checks the idea alone, with hints, retry and reset. Six tools, each with its own "
                 "purpose, follow the chapter's own plan."},
        {"title": "A tool in three steps",
         "text": "Each tool opens with a short recall of the video idea, then lets the student play and apply it, and "
                 "ends with the chapter's own question, used exactly as the book gives it."},
        {"title": "Every book question has its own video",
         "text": "Every solved example, Let Us Do and Let Us Explore question and every answerable prompt of the book "
                 "is its own short video with a step by step solution and a question picture and a solution picture, "
                 "in a Questions topic that follows the idea it practises."},
        {"title": "The picture is the mathematics",
         "text": "Quilts, tables, grids and rectangles of patches carry each idea: the border outlined for perimeter, "
                 "the squares inside counted for area, with every edge and every square clear."},
        {"title": "Only the book's numbers",
         "text": "The quilt, the tables, the desk, the grids, the mats and every question are the book's own. Any "
                 "number the plan adds is a practice value and is said to be one."},
    ],
}

# {module_id: strand letter}: the subject strand each module belongs to (core/qt.py builds every objective's strand).
# CBSE maths catalog: N Number, A Algebra, G Geometry, M Measurement, D Data, S Statistics and Probability.
MODULE_STRANDS = {"M1": "M", "M2": "M", "M3": "M"}

# every book item, with its kind. Home concepts are listed in DESIGN.md section 3.
NCERT_ITEMS = [
    # the opener: the quilt and the lace
    ("open.story", "text"), ("open.perimeter", "text"),
    ("open.tick", "prompt"), ("open.twolaces", "prompt"), ("LUD1.Q1", "exercise"),
    # the rug and the four tables
    ("tab.story", "text"), ("tab.tile", "text"), ("tab.areadef", "text"), ("desk.story", "text"),
    ("rug.patches", "prompt"), ("tab.shapes", "prompt"), ("tab.counts", "prompt"), ("tab.circles", "prompt"),
    ("tab.area", "prompt"), ("tab.objects", "prompt"), ("LUD.desk", "exercise"),
    # Comparing Shapes
    ("cmp.story", "text"), ("sq.unit", "text"), ("note.unit", "text"),
    ("cmp.largest", "prompt"), ("cmp.ab_bc", "prompt"), ("cmp.ac", "prompt"), ("cmp.grid", "prompt"),
    ("LUD.garden", "exercise"), ("LUD.palm", "exercise"), ("LUD.leaves", "exercise"),
    # area and perimeter are different measures
    ("LUD.mats", "exercise"), ("trisha", "prompt"), ("LUE.Q1", "exercise"), ("LUE.Q2", "exercise"),
    ("LUD.same_area", "exercise"), ("LUD.a_less_b", "exercise"),
    # rectangles and squares
    ("rect.rule", "text"), ("note.rows", "text"), ("rect.perimeter", "text"), ("square.rule", "text"),
    ("LUD1.Q2", "exercise"), ("patch.example", "example"), ("patch.check", "prompt"), ("square.example", "example"),
    ("LUD.floor", "exercise"), ("LUD.five", "exercise"),
    # using the rules
    ("LUD.objects", "exercise"), ("LUD.field", "exercise"), ("LUD.garden64", "exercise"), ("LUD.figure", "exercise"),
    # Let Us Play and the summary
    ("play.rules", "text"), ("play.perimeter", "prompt"), ("play.win", "prompt"),
    ("summary", "text"),
]

MISCONCEPTIONS = [
    ("M_BORDER_PATCHES", "The perimeter is found by counting the patches along the border, so a quilt 15 patches long "
                         "and 10 broad has 46 patches on its border and the corners are missed (the border is 50 "
                         "units)."),
    ("M_PERIM_TWO_SIDES", "The perimeter of a rectangle is its length plus its breadth only."),
    ("M_AREA_IS_PERIM", "Area and perimeter are the same measure, and both are found by adding the sides."),
    ("M_CIRCLE_TILES", "Circles can cover a surface with no gaps if they are packed close."),
    ("M_TILE_COUNT", "The region that needs more tiles has the larger area, even when the tiles are of different "
                     "sizes."),
    ("M_ONE_SIDE", "The shape that is longer in one direction has the larger area."),
    ("M_BIGGER_AREA_BIGGER_PERIM", "If the area of a rectangle grows, its perimeter grows too."),
    ("M_SAME_AREA_SAME_PERIM", "Shapes with the same area have the same perimeter."),
    ("M_SQUARE_MIX", "The area of a square is 4 times its side and its perimeter is the side times itself."),
    ("M_AREA_UNIT", "An area is written in cm, like a length, and not in square cm."),
    ("M_ADD_TILE", "Adding a tile to a figure of tiles always makes the perimeter 4 more."),
]

SOLUTION_NOTES = [
    {"item": "The quilt (opener: tick the lace, two laces)",
     "printed_solution": "The quilt has no numbers on it, and the book prints no answer for either question.",
     "correct": "The plan counts the picture: 15 patches along the long side and 10 along the short side, each patch "
                "side 1 unit. The border is 15 + 10 + 15 + 10 = 50 units: the green lace (50 units) covers it exactly "
                "and the red (40) and blue (25) laces are too short. For two coloured laces the plan gives a sample "
                "split (30 units for the two long sides, 20 for the two short sides); any split that makes 50 and "
                "fits the reels is accepted. To be confirmed."},
    {"item": "Let Us Do p. 142 Q1, the shape with 5 cm",
     "printed_solution": "The picture is a bow-tie (a top line, a bottom line and two crossing lines) but the text says "
                         "all sides are equal.",
     "correct": "The plan reads 4 equal sides of 5 cm: 4 × 5 = 20 cm. The shape with the 4 cm side has 5 sides: "
                "5 × 4 = 20 cm. The plan letters the two shapes (a) and (b)."},
    {"item": "Let Us Do p. 142 Q2: draw two rectangles each having the perimeters 26 cm and 18 cm",
     "printed_solution": "No answer; many pairs of length and breadth work.",
     "correct": "Read as two rectangles for each perimeter. Sample: 8 by 5 and 10 by 3 for 26 cm; 6 by 3 and 7 by 2 for "
                "18 cm (length + breadth is 13 and 9). The question is practised with the perimeter of a rectangle, "
                "where half the perimeter equals length + breadth is learnt."},
    {"item": "The rug and the four tables (p. 143)",
     "printed_solution": "No counts are printed.",
     "correct": "Counted from the pictures: rug 15 × 6 = 90 patches; Table 1 has 5 by 2 squares each cut into 2 "
                "triangles = 20 triangles; Table 3 8 squares; Table 4 12 rectangles; Table 2 8 circles with gaps."},
    {"item": "Cover your table with notebooks, lunch boxes, pencil boxes, maths books (p. 143)",
     "printed_solution": "Hands-on with the student's own table; no answer.",
     "correct": "All four are rectangles and rectangles tile; whether one covers the table exactly depends on the "
                "table. Sample with practice values (a notebook 20 cm by 15 cm on a top 60 cm by 30 cm: 6 notebooks)."},
    {"item": "Preetha's desk (Let Us Do p. 144)",
     "printed_solution": "No answers; the unit lengths are not given.",
     "correct": "The grid squares are read as unit squares: the desk is 9 × 6 = 54 squares; blue squares 54; green "
                "triangles (half a square) 108; red triangles (2 make a 3 by 3 square, the desk holds 6 such squares) "
                "12. Plan's own reading."},
    {"item": "Comparing Shapes: rectangles A, B, C (pp. 144 to 145)",
     "printed_solution": "No answers are printed.",
     "correct": "Counted on the grid: A 3 × 4 = 12, B 2 × 4 = 8, C 2 × 5 = 10. B fits inside A and inside C; A "
                "and C cannot be settled by laying one on the other, so the squares are counted."},
    {"item": "Cover your table with Maths textbooks (p. 143, object (d))",
     "printed_solution": "The book names the objects Notebooks, Lunch boxes, Pencil boxes, Maths textbooks.",
     "correct": "The plan writes Maths books, because a student never reads the word textbook in the plan."},
    {"item": "The gardens (Let Us Do p. 145 Q1)",
     "printed_solution": "A pale one-square-wide strip lies beside the gardens and carries no label; the unit is "
                         "written \"cm square\" here and \"square cm\" in its rules.",
     "correct": "The strip is treated as belonging to neither garden. Garden A 2 × 5 = 10 square cm, garden B 4 × 3 = "
                "12 square cm. The plan writes square cm in the question as well (the book's \"= ___ cm square\" becomes \": ___ square "
                "cm\", same meaning)."},
    {"item": "Palm and leaves (Let Us Do p. 146 Q2 and Q3) and the classroom floor and objects (p. 151 Q1, p. 153 Q3)",
     "printed_solution": "These use real objects the student measures or traces; there is no single answer, and the "
                         "book does not say how to count a part square.",
     "correct": "The plan gives the method (count whole squares, put part squares together to make about whole "
                "squares) and a sample with practice values, and says the answer may differ. Rows 5 and 6 of the "
                "table are the student's own objects."},
    {"item": "The mats (Let Us Do p. 147 Q4)",
     "printed_solution": "The size of the patch is not stated, and the question has a typo (\"of the size give below\").",
     "correct": "The drawn patch is as large as a 1 cm grid square on the same pages, so a patch is 1 cm by 1 cm. Mat (a) "
                "5 by 2: 10 patches, 10 square cm, perimeter 14 cm. Mat (b) 4 by 3: 12 patches, 12 square cm, "
                "perimeter 14 cm. The typo is corrected to \"given below\"."},
    {"item": "Trisha's rectangles (p. 147)",
     "printed_solution": "No answer.",
     "correct": "Her rectangles 2 by 3 and 3 by 4: area 6 to 12 and perimeter 10 to 14, so she is right for them, but "
                "not always: the mats go from area 10 to 12 with the same perimeter 14, and 1 by 8 to 3 by 3 raises "
                "the area and lowers the perimeter."},
    {"item": "Let Us Explore p. 147 and p. 148",
     "printed_solution": "No answers; the shapes are only drawn on grids.",
     "correct": "Counted cell by cell. Q1: shapes (a), (b), (c), (d), (f) each have area 12 and perimeters 16, 18, 14, "
                "14, 26; shape (e) has area 8 and perimeter 18. Q2: all five shapes have area 7; perimeters 12, 12, "
                "16, 16, 16, so two groups share a perimeter, (a) with (b) and (c) with (d) and (e)."},
    {"item": "Let Us Do p. 149 Q1 (draw shapes of the same area)",
     "printed_solution": "No answer; many shapes work.",
     "correct": "The given shape is 9 by 2: area 18, perimeter 22. Samples: 6 by 3 (perimeter 18), 18 by 1 (38), a 4 by "
                "4 block with 2 squares below (18). Same area, different perimeters."},
    {"item": "Let Us Do p. 150 Q2 (square (a) and triangle (b))",
     "printed_solution": "No answer.",
     "correct": "(a) is 3 × 3 = 9. (b) covers 6 whole squares and 6 half squares = 6 + 3 = 9. The areas are equal, so "
                "(a) is not less than (b)."},
    {"item": "The patchwork figure (p. 150): the words Length and Breadth",
     "printed_solution": "The figure puts Length under the 4-patch side and Breadth beside the 6-patch side, but the "
                         "text says 6 is the length and 4 the breadth and writes 6 cm × 4 cm.",
     "correct": "The product is the same. The plan follows the text (length 6, breadth 4) and does not rely on which "
                "side carries the word."},
    {"item": "The square of side 5 (p. 151)",
     "printed_solution": "The book prints the working but no question sentence.",
     "correct": "The plan adds the question: what are its area and its perimeter?"},
    {"item": "Let Us Do p. 152 Q2: the five shapes",
     "printed_solution": "Each shape has two blanks for cm (ten in all).",
     "correct": "The plan asks for length, breadth, area and perimeter: (a) 6 by 6, (b) 4 by 7, (c) 12 by 4, (d) 3 by 3, "
                "(e) 6 by 5, read from the grid."},
    {"item": "Let Us Do p. 153 Q6 (the figure with 32 cm, 6 cm and 12 cm)",
     "printed_solution": "The figure is not drawn to scale and has dotted lines without numbers.",
     "correct": "Read as one rectangle 32 cm wide and 6 + 12 = 18 cm high: area 32 × 18 = 576 square cm, checked by the "
                "two parts 32 × 6 + 32 × 12."},
    {"item": "Let Us Play (p. 154)",
     "printed_solution": "The rules do not say what happens when the perimeter goes past 24, or whether a tile must "
                         "touch along a whole edge.",
     "correct": "The plan follows the pictures: tiles touch edge to edge and are not moved; the perimeter must be "
                "exactly 24 to win; a tile that fills a notch and touches 3 edges brings it down by 2. The pictures "
                "give 10 (4 tiles), 12 (5 tiles) and 24 (11 tiles). To be confirmed."},
    {"item": "The book's Note for Teachers boxes (pp. 145 and 151)",
     "printed_solution": "Two boxes addressed to teachers.",
     "correct": "Kept as coverage ids (note.unit, note.rows); their ideas (a square is the unit because its sides are "
                "equal; rows times columns) are used in the concepts. No teacher is given a role."},
    {"item": "Brief: revision video",
     "printed_solution": "The brief asks for an interactive recap or revision video.",
     "correct": "The pipeline has no recap video, so the last topic is a text summary with short concept checks."},
]
ERRATA = []

DESIGN_REFERENCES = [
    {"text": "priority_doc.md (the plan written to the 'Class 5 Mathematics Learning Experience Designer' brief, "
             "6 November 2026): topic flow, video types, the 6 tools, the shared visual language and the learning rules "
             "decide this chapter's design.", "url": ""},
    {"text": "docs/01_runbook.md and .claude/skills/lp/SKILL.md: framing intro with a free-try tool, idea topics each "
             "ending in a Practice concept, a Questions topic after every idea topic with a question concept and an "
             "answer concept per book question, and one summary topic.", "url": ""},
]

# The book's own figures that carry mathematics, keyed by authored concept key. One concept image per teaching,
# hook and summary concept where a drawn figure is the maths; the tool concepts (Practice / free try) are pictured by
# their tool.
FIGURES = {
    "T1.C1": ["A quilt cover of 15 patches by 10 patches in rows of green, red and yellow with a pink rim, and three lace "
              "reels (red, green, blue) beside it. No number written."],
    "T1B.C1": ["A mat with 5 equal sides of 7 cm, each side marked."],
    "T2.C1": ["A tray top covered by 12 squares in 3 rows of 4, beside a tray top with 6 circles in 2 rows of 3 and gaps "
              "between them."],
    "T2.C2": ["A tray top of 24 squares in 4 rows of 6, beside the same tray with every square cut from corner to corner "
              "into 2 triangles, 48 triangles."],
    "T3.C1": ["Mat P, 7 squares by 2, and mat Q, 4 squares by 4, laid on each other so that neither covers the other."],
    "T3.C2": ["A triangle on a grid of 1 cm squares with 6 whole squares and 4 half squares marked."],
    "T4.C1": ["Three rectangles of 16 unit squares: 4 by 4, 8 by 2 and 16 by 1, each with its border marked."],
    "T4.C2": ["Three rectangles with a border of 20 units: 5 by 5, 7 by 3 and 9 by 1."],
    "T5.C1": ["A rectangle of 5 rows of 8 patches with its length 8 cm and its breadth 5 cm marked."],
    "T5.C2": ["A rectangle 11 cm long and 4 cm broad with its four sides marked."],
    "T5.C3": ["A square of side 7 cm with its four equal sides marked."],
    "T6.C1": ["A lawn of area 72 square m with its length 9 m marked and its breadth unknown."],
    "T6.C2": ["A rectangle 20 cm wide whose height is marked in two parts, 5 cm and 7 cm."],
    "T7.C1": ["Five square tiles placed like the letter L with every outer edge marked 1."],
    "T8.C1": ["The patchwork room with one small panel for each idea of the chapter: border, tiles, unit square, area "
              "and perimeter, rectangle, square, missing side, tiles."],
}
