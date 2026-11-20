# -*- coding: utf-8 -*-
"""Chapter-level content for Class 5 Chapter 7, Shapes and Patterns (Maths Mela, Grade 5, Chapter 7).

The plan follows the "Class 5 Mathematics Learning Experience Designer" brief (priority_doc.md sections A to F) and the
/lp pipeline's structure; the book decides every number and every question. Book lines are verbatim except: the book's
dashes become commas, colons or "to"; minus is U+2212; where the book tells the student to cut a piece out of its back
sheet, the tool supplies the piece. No em dash and no en dash anywhere here."""
from __future__ import annotations

CHAPTER = {
    "grade": 5,
    "label": "Class 5",
    "chapter_no": 7,
    "name": "Shapes and Patterns",
    "book_part": "Maths Mela, Grade 5, Chapter 7",
    "source_pdf": "textbooks/class-5/eemm107.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Weaving Patterns",
     "Weaving paper strips over and under to make a mat, writing a weave row in words, and seeing when the rows start "
     "to repeat."),
    ("M2", "Tiling and Tessellation",
     "Regular shapes, which regular shapes fit round a point with no gap and no overlap, and patterns made of two "
     "shapes."),
    ("M3", "Triangles, Four-Sided Shapes and Tangram",
     "Making triangles and four-sided shapes from the pieces of a rhombus, the seven tangram pieces, and telling "
     "square, rectangle, rhombus and parallelogram apart."),
    ("M4", "Circles, Cubes and Solids",
     "Two diameters of a circle, designs made by joining points on a circle, cubes and their nets, a clue puzzle, the "
     "icosahedron and the dodecahedron, and a revision of the whole chapter."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter is a craft table: paper strips, tiles, cut-out pieces, thread and clay. Making and fitting "
             "shapes shows which shapes fit together, what makes a triangle or a four-sided shape what it is, and how "
             "patterns repeat. A short video explains each idea, and an interactive tool lets the student try it "
             "alone.",
    "points": [
        {"title": "Videos teach, tools explore",
         "text": "Every idea has one short concept video. The tool that follows is where the student weaves, fits, "
                 "joins, folds and counts alone, with hints, retry and reset. Eleven tools, each with its own purpose, "
                 "follow the chapter's own activities."},
        {"title": "A tool in three steps",
         "text": "Each tool opens with a short recall of the video idea, then lets the student play and apply it, and "
                 "ends with the chapter's own question, used exactly as the book gives it."},
        {"title": "Every book question has its own video",
         "text": "Every answerable question and activity of the book is its own short video with a step by step "
                 "solution and a question picture and a solution picture, in a Questions topic that follows the idea "
                 "it practises."},
        {"title": "The pieces are on screen",
         "text": "The book's cut-out pieces (the rhombus with four triangles, the tangram, the regular shapes, the nets) "
                 "are shown on screen, so every student has a full set to turn, flip and join."},
        {"title": "No measuring of angles",
         "text": "The chapter compares angles by folding and by fitting pieces. It says right angle and equal angles "
                 "and never measures an angle, and so does the plan."},
    ],
}

# {module_id: strand letter}: the subject strand each module belongs to (core/qt.py builds every objective's strand).
# CBSE maths catalog: N Number, A Algebra, G Geometry, M Measurement, D Data, S Statistics and Probability.
MODULE_STRANDS = {"M1": "G", "M2": "G", "M3": "G", "M4": "G"}

# every book item, with its kind. Home concepts are listed in DESIGN.md section 3.
NCERT_ITEMS = [
    # Weaving Mats
    ("w.intro", "text"), ("w.make", "text"), ("w.describe", "text"),
    ("w.q2", "prompt"), ("w.q3", "prompt"), ("w.q4", "prompt"), ("w.try", "exercise"),
    # Tiling and Tessellation, Find Out
    ("tt.intro", "text"), ("tt.regular", "text"), ("tt.no_pentagon", "text"), ("tt.triangle", "text"),
    ("tt.octagon", "text"),
    ("tt.pent4", "prompt"), ("fo.triangle", "prompt"), ("fo.square", "prompt"), ("fo.five", "prompt"),
    ("fo.hexagon", "prompt"), ("tt.oct", "prompt"),
    # patterns with more than one shape
    ("tp.two_shapes_text", "text"),
    ("tp.two", "prompt"), ("tp.cont1", "prompt"), ("tp.oct_sq", "prompt"), ("tp.sq_tri_eq", "prompt"),
    ("tp.sq_tri_pts", "prompt"), ("tp.create", "prompt"),
    # the rhombus pieces: triangles
    ("rh.def", "text"), ("rh.iso", "text"), ("tr.equi", "text"),
    ("rh.two", "prompt"), ("rh.q1", "prompt"), ("rh.fold", "prompt"), ("rh.q2", "prompt"), ("rh.q3", "prompt"),
    ("try.equi", "prompt"), ("try.halve", "prompt"), ("try.scalene", "prompt"),
    # four-sided shapes and kites
    ("kite.text", "text"), ("par.text", "text"),
    ("rq.four", "prompt"), ("rq.measure", "prompt"), ("rq.angles", "prompt"), ("rq.draw", "prompt"),
    ("rq.three", "prompt"), ("rq.four_pieces", "prompt"), ("kite.fold", "prompt"),
    # tangram
    ("tg.intro", "text"),
    ("tg.name", "prompt"), ("tg.same", "prompt"), ("tg.angles", "prompt"), ("tg.sides", "prompt"),
    ("tg.make", "prompt"),
    # which shape am I
    ("ws.match", "prompt"),
    # circles
    ("pc.shape", "prompt"), ("pc.diff", "prompt"), ("pc.other", "prompt"), ("cd.join", "prompt"),
    ("cd.flower", "prompt"),
    # cubes
    ("cc.views", "prompt"), ("cc.frames", "prompt"), ("cc.paint", "prompt"),
    # puzzle
    ("puz.tanu", "prompt"),
    # icosahedron and dodecahedron, summary
    ("ico.intro", "text"),
    ("ico.names", "prompt"), ("ico.shapes", "prompt"), ("ico.vertex", "prompt"), ("ico.edges", "prompt"),
    ("ico.other", "prompt"), ("ico.make", "prompt"),
    ("summary", "text"),
]

MISCONCEPTIONS = [
    ("M_WEAVE_SAME", "Every row of a weave is the same as the row above it."),
    ("M_WEAVE_RESTART", "The weave rule starts again at the same place in every row."),
    ("M_ALL_REGULAR_TILE", "Any regular shape fits round a point with no gap, so every regular shape tessellates."),
    ("M_NEARLY_FITS", "If the gap round a point is small, the shapes still tessellate."),
    ("M_SAME_SET", "The shapes that meet at two points of a pattern can be different ones."),
    ("M_ISO_ANGLES", "Only the sides of an isosceles triangle are equal; its angles are all different."),
    ("M_KITE_OPPOSITE", "In a kite the opposite sides are equal."),
    ("M_RECT_NOT_PARA", "A rectangle is not a parallelogram."),
    ("M_COUNT_EDGE_TWICE", "The edges of a solid are the sum of the sides of all its faces, with no halving."),
    ("M_FORGET_INSIDE", "The small cube hidden in the middle of a big cube has paint on it."),
    ("M_PIECES_AREA", "Shapes made of the same pieces always have the same number of sides."),
    ("M_CIRCLE_ANY", "Joining the ends of two diameters of a circle can make any four-sided shape."),
]

SOLUTION_NOTES = [
    {"item": "The cut-out pieces (rhombus, tangram, regular shapes, nets, dot grids)",
     "printed_solution": "The book says samples are given at the end of the book (its Learning Material Sheets).",
     "correct": "The sheet 'Tessellation and Shapes' holds the rhombus with four triangles, the tangram, 6 each of "
                "regular pentagon, regular hexagon (cut into 6 triangles), square, equilateral triangle and circle; "
                "the nets of the icosahedron and the dodecahedron and the dot grids are on other sheets. The tools show "
                "the same pieces on screen. The question wording drops 'a sample is given at the end of the book' "
                "because the tool supplies the piece. The sheet has no octagon, no paper strips, no cube and no cube "
                "frames: the 8 slit columns of the mat are a practice value."},
    {"item": "The rhombus and its four triangles (questions 1 to 8 after the rhombus)",
     "printed_solution": "The book never gives the shape of the rhombus.",
     "correct": "The sheet prints it 457 wide by 748 tall (ratio about 1 to 1.64); two equilateral triangles joined "
                "would be 1 to 1.73. The plan reads it as two equilateral triangles joined, so each piece is half of an "
                "equilateral triangle (one right angle, longest side twice the shortest, all sides different). Reasons: "
                "the Try This halves an equilateral triangle and calls the halves scalene; two pieces joined make a "
                "triangle with 2 equal sides; the pictured kite, A and B match. If the printed ratio is meant, two "
                "pieces joined along the longer short side make sides in the ratio 1.92 : 1.92 : 2 (nearly equilateral). "
                "To be confirmed."},
    {"item": "How many different 4-sided shapes can you make (rhombus pieces)",
     "printed_solution": "The book shows three possible shapes (a kite, A and B).",
     "correct": "Joining whole sides, 2 pieces make 4 different four-sided shapes (a kite, a rectangle, 2 parallelograms "
                "that are not rectangles); sliding a piece along a side makes more. The plan says at least 4."},
    {"item": "Use 3 and 4 pieces of the rhombus (questions 7 and 8)",
     "printed_solution": "No answer printed.",
     "correct": "Checked by computer, joining whole sides: 3 pieces make shapes of 3, 4 and 5 sides; 4 pieces make a "
                "rectangle, a triangle, a pentagon and a hexagon, but no square and no octagon (never more than 6 "
                "sides)."},
    {"item": "Regular shapes",
     "printed_solution": "The book says shapes that have equal sides are called regular shapes.",
     "correct": "A rhombus also has equal sides. The plan uses 'regular' only for the equilateral triangle, square, "
                "pentagon, hexagon and octagon the book names."},
    {"item": "Squares and triangles pattern (tessellation patterns)",
     "printed_solution": "No answer printed to 'Are the triangles equilateral? Why or why not?'.",
     "correct": "Read on the dot grid, each triangle has two sides as long as a square's side (about 2.2 grid steps) and "
                "a shorter third side (2 grid steps): two equal sides, so isosceles and not equilateral. At every marked "
                "point 2 squares and 3 triangles meet (the corners add up to a full turn, checked)."},
    {"item": "Which Shape Am I?",
     "printed_solution": "No answer printed.",
     "correct": "(1) Rectangle; (2) Rhombus; (3) Rhombus, Parallelogram; (4) Parallelogram, Rhombus (a rhombus has two "
                "pairs of equal sides, so it is read to fit); (5) Square; (6) all four; (7) Square, Rectangle. A "
                "rhombus, a rectangle and a square have opposite sides equal, so by the book's rule they are "
                "parallelograms too."},
    {"item": "Play with Circles: a four-sided shape other than a rectangle",
     "printed_solution": "No answer printed.",
     "correct": "Always a rectangle (checked for many pairs of diameters). Diameters at right angles give four equal "
                "sides: a square, which the plan calls a special rectangle."},
    {"item": "Let Us Try (the green and yellow design)",
     "printed_solution": "The picture is 21 squares across and 21 down; the dot grid printed beside it has 24 columns "
                         "but only 18 rows of dots.",
     "correct": "The plan describes the whole 21 by 21 design. The design is the same on the left and on the right "
                "(checked); its top and bottom halves are alike but not identical. Sample answer only."},
    {"item": "Weaving questions 2, 3 and 4",
     "printed_solution": "No answers printed.",
     "correct": "Read from the pictures cell by cell (over means the strip colour that shows on top): question 2 has 8 "
                "columns and 8 rows, the two rows alternate; question 3 repeats after 4 rows; question 4 design 1 "
                "(16 columns) repeats after 6 rows, design 2 (11 columns) after 4 rows."},
    {"item": "Cube Connections, question 1 (three views and the net)",
     "printed_solution": "No answer printed.",
     "correct": "The three views can come from one cube only if the cream face with the red cross is on two opposite "
                "faces. The plan uses that reading and gives one net that folds to match (checked by folding). Your net "
                "may differ."},
    {"item": "Cube Connections, question 2 (cube frames)",
     "printed_solution": "No answer printed.",
     "correct": "Read as a square tunnel through each pair of opposite faces, leaving only corner and edge cubes: "
                "3 by 3 by 3 loses 7, 4 by 4 by 4 loses 32, 5 by 5 by 5 loses 81."},
    {"item": "Puzzle (Tanu's shapes)",
     "printed_solution": "No answer printed.",
     "correct": "With 2 squares and 2 triangles, 'the square' is read as one of them in each clue and 'between' as "
                "directly between: circle, square, rectangle, triangle, square, triangle, hexagon is the only "
                "arrangement (checked)."},
    {"item": "Kites by folding",
     "printed_solution": "No answer printed; the corners A and B are only marked on a picture.",
     "correct": "Both corners are read as corners next to the same end of the crease, folded in to it. The kite then "
                "shows 4 triangles: the 2 folded flaps and 2 more under them."},
    {"item": "Circle Designs",
     "printed_solution": "The book says to join 1 to 11, 11 to 2, 2 to 12 'and so on till you reach back at 1', and asks "
                         "how to make a design like the picture of overlapping circles.",
     "correct": "The path has 29 lines (checked). The picture is five circles of one size: one in the middle and four "
                "round it, each centred where two diameters at right angles meet the middle circle (measured on the "
                "picture)."},
    {"item": "Tangram, make the four shapes",
     "printed_solution": "The four outlines are drawn without a scale.",
     "correct": "The plan gives sample answers for shapes of the same proportions (checked by computer): a rectangle "
                "and a parallelogram each from 2 small triangles and the medium triangle, a triangle from the medium "
                "triangle, and the short-top long-bottom shape from the medium triangle and the parallelogram."},
    {"item": "Icosahedron and Dodecahedron",
     "printed_solution": "The blanks have no printed answer.",
     "correct": "The nets on the sheet have 20 triangles and 12 pentagons (counted); 5 and 3 faces meet at a corner and "
                "both solids have 30 edges (faces times sides, halved)."},
    {"item": "Open prompts (patterns to continue, shapes to draw, models to build)",
     "printed_solution": "No single answer.",
     "correct": "The plan gives one reasoned sample answer and says the student's answer may differ."},
    {"item": "Brief: revision video",
     "printed_solution": "The brief asks for an interactive recap or revision video.",
     "correct": "The pipeline has no recap video, so the last topic is a text summary with short concept checks."},
]
ERRATA = []

DESIGN_REFERENCES = [
    {"text": "priority_doc.md (the plan written to the 'Class 5 Mathematics Learning Experience Designer' brief): topic "
             "flow, video types, the 11 tools, the shared visual language and the learning rules decide this "
             "chapter's design.", "url": ""},
    {"text": "docs/01_runbook.md and .claude/skills/lp/SKILL.md: framing intro with a free-try tool, idea topics each "
             "ending in a Practice concept, a Questions topic after every idea topic with a question concept and an "
             "answer concept per book question, and one summary topic.", "url": ""},
]

# The book's own figures that carry mathematics, keyed by authored concept key (one concept image per teaching, hook
# and summary concept where a drawn figure is the maths; the tool concepts are pictured by their tool).
FIGURES = {
    "T1.C1": ["A woven basket close up and a paper mat of crossed blue and yellow strips on a table."],
    "T1B.C1": ["One row of a woven mat of 10 slits with over and under marked: 3 over, 2 under, 3 over, 2 under."],
    "T1B.C2": ["Four rows of a woven mat of 9 slits, each row starting one step later, the fourth row the same as the "
               "first."],
    "T2.C1": ["A square, a rectangle and a pentagon with the sides marked equal or not equal."],
    "T2.C2": ["Four rectangles of one size round a point with no gap, and a fifth that does not fit."],
    "T3.C1": ["A border of 12 tiles, squares and triangles taking turns."],
    "T4.C1": ["A triangle with sides 5, 5 and 3 folded in half."],
    "T4.C2": ["Three triangles: sides 6, 6, 6; sides 7, 5, 4; sides 8, 8, 3."],
    "T5.C1": ["A kite with sides 5, 5, 3, 3 and a parallelogram with sides 5, 3, 5, 3."],
    "T5.C2": ["A rectangle and a slanted parallelogram with sides 8 and 5."],
    "T6.C1": ["The seven tangram pieces sorted: five triangles and two four-sided shapes."],
    "T7.C1": ["A square, a rectangle, a rhombus and a parallelogram with their sides and angles marked."],
    "T8.C1": ["A circle with two diameters and the four ends joined into a rectangle."],
    "T8.C2": ["A circle with 12 points and the path 1, 5, 2, 6, 3, 7 started."],
    "T9.C1": ["Two views of a cube with sun, moon, heart and leaf faces."],
    "T9.C2": ["A 4 by 4 by 4 cube with corner, edge, face and inside cubes in four colours."],
    "T10.C1": ["Five shapes in a line with the four clues."],
    "T11.C1": ["A box with its 6 faces and 8 corners marked."],
    "T11.C2": ["A box with each of its faces ticked and each edge shared by 2 faces."],
    "T12.C1": ["Eight tiles on a craft table: a woven mat, a regular hexagon, three hexagons round a point, a triangle, a "
               "kite, a circle with two diameters, a cube and a box, one for each big idea of the chapter."],
}
