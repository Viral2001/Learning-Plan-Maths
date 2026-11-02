# -*- coding: utf-8 -*-
"""Chapter-level content for Class 8 Chapter 14, Area (Ganita Prakash Grade 8 Part II, Chapter 7, pp 148 to 171).
Book lines elsewhere are verbatim except: the book's dashes become commas, colons or "to"; minus is U+2212;
the book's stacked one half is written 1/2. Lengths read off the book's grid figures are counted squares."""
from __future__ import annotations

CHAPTER = {
    "grade": 8,
    "label": "Class 8",
    "chapter_no": 14,
    "name": "Area",
    "book_part": "Ganita Prakash Grade 8 Part II, Chapter 7",
    "source_pdf": "textbooks/class8/hegp207.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Rectangles, Squares and Triangles",
     "Area counts unit squares, so a rectangle is length times width and perimeter cannot stand in for area. A "
     "triangle is half of a rectangle on the same base and height, and that one formula finds altitudes, splits "
     "shapes into equal parts and explains triangles between parallel lines."),
    ("M2", "Polygons and Special Quadrilaterals",
     "Any polygon cuts into triangles. Cutting and rearranging (dissection) turns a parallelogram into a rectangle, "
     "a rhombus into a rectangle built on its diagonals, and two copies of a trapezium into a parallelogram, giving "
     "a formula for each."),
    ("M3", "Areas Around Us",
     "Real objects are measured in square centimetres, square inches, square feet, acres and square kilometres. "
     "Students convert between units, estimate the areas of tables, rooms, schools and towns, and close with a summary."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter follows the book's own order: rectangles first, then triangles as half rectangles, then "
             "every other shape cut into rectangles and triangles. Each formula is earned by a cut and a rearrange "
             "before it is used, and each is checked on a figure the student can count.",
    "points": [
        {"title": "Predict, then check",
         "text": "Each idea opens with a guess: which rectangle needs more powder, which triangle is bigger, will the "
                 "area change when the shape slides. The video or the interactive step then checks the guess."},
        {"title": "Cut and rearrange",
         "text": "Dissection is the engine of the chapter. A parallelogram, a rhombus and a trapezium are each cut "
                 "and moved into a rectangle or parallelogram of the same area before any formula is written."},
        {"title": "Height is perpendicular",
         "text": "Every formula uses a height that meets the base at a right angle, never a slanting side. Obtuse "
                 "triangles and slanting trapeziums are handled by subtracting or adding pieces."},
        {"title": "Tools only where the moving is the idea",
         "text": "Four interactive tools, each used once: stretching rectangles, sliding a triangle's top vertex, "
                 "cutting a parallelogram and joining two trapeziums. Other topics are taught by worked examples."},
    ],
}

NCERT_ITEMS = [
    # 7.1 Rectangle and Squares (pp 148 to 150)
    "7.1.four_parts", "7.1.mt_creative",
    "7.1.rangoli", "7.1.rect_formula", "7.1.units", "7.1.diag_triangle",
    "7.1.perim_why", "7.1.perim_same", "7.1.perim_find_rects", "7.1.mt_perim_shapes",
    # Figure it Out, rectangles and squares (questions 1 to 6)
    "FiO1.q1", "FiO1.q2", "FiO1.q3", "FiO1.q4", "FiO1.q5", "FiO1.q6",
    # Triangles (pp 153 to 154)
    "tri.xdc_ydc", "tri.xdc_ybc", "tri.fig_xdc", "tri.measure", "tri.outer_rect", "tri.formula", "tri.obtuse",
    # Some applications of the area formula (pp 155 to 157)
    "app.find_by", "app.diag_four", "app.median", "app.parallel_area", "app.parallel_perim", "app.reflect",
    "app.mt_bisector",
    # Figure it Out, triangles (questions 1 to 8)
    "FiO2.q1", "FiO2.q2", "FiO2.q3", "FiO2.q4", "FiO2.q5", "FiO2.q6", "FiO2.q7", "FiO2.q8",
    # Area of any polygon (p 159)
    "poly.quad", "poly.pentagon", "poly.any",
    # Figure it Out, area of any polygon (questions 1 to 5) and the closing line
    "FiO3.q1", "FiO3.q2", "FiO3.q3", "FiO3.q4", "FiO3.q5", "poly.special",
    # Parallelogram (pp 161 to 162)
    "para.method", "para.fit", "para.dissection", "para.formula", "para.other_base", "para.cut_cz",
    # Figure it Out, parallelograms (questions 1 to 9)
    "FiO4.q1", "FiO4.q2", "FiO4.q3", "FiO4.q4", "FiO4.q5", "FiO4.q6", "FiO4.q7", "FiO4.q8", "FiO4.q9",
    # Rhombus (pp 164 to 166)
    "rhom.dissect", "rhom.sides", "rhom.triangles", "rhom.simplify",
    # Trapezium and two copies of the trapezium (pp 166 to 169)
    "trap.grid", "trap.wxyz", "trap.formula", "trap.obtuse", "trap.approach1", "trap.approach2", "trap.mt_any",
    "trap.two_copies", "trap.quad_type",
    # Figure it Out, rhombus and trapezium (questions 1 to 8)
    "FiO5.q1", "FiO5.q2", "FiO5.q3", "FiO5.q4", "FiO5.q5", "FiO5.q6", "FiO5.q7", "FiO5.q8",
    # Areas in real life (pp 170 to 171)
    "rl.a4", "rl.tabletop", "rl.to_cm", "rl.to_inch", "rl.sq_in", "rl.ten_sq_in", "rl.convert", "rl.quotient",
    "rl.classroom", "rl.sq_ft", "rl.school", "rl.local_unit", "rl.village", "rl.km2", "rl.times_bigger",
    "rl.largest_city", "rl.smallest_city",
    "summary",
]

MISCONCEPTIONS = [
    ("M_PERIM_AREA", "A shape with a longer boundary must cover more area."),
    ("M_EQUAL_SHAPE", "Parts of equal area must have the same shape."),
    ("M_TRI_FULL", "Triangle area is taken as base × height, forgetting the half."),
    ("M_SLANT_HEIGHT", "The slanting side of a triangle or parallelogram is its height."),
    ("M_OUTSIDE_HEIGHT", "A triangle whose height falls outside it has no height, so the formula fails."),
    ("M_TOP_VERTEX", "Moving the top vertex of a triangle along a parallel line changes its area."),
    ("M_RECT_PARA", "A parallelogram with the same sides as a rectangle has the same area."),
    ("M_RHOMBUS_DIAG", "The area of a rhombus is the full product of its diagonals."),
    ("M_TRAP_ONE_SIDE", "The area of a trapezium uses only the longer parallel side times the height."),
    ("M_UNIT_SQUARE", "Converting square units uses the same factor as the length units (1 square inch is 2.54 square centimetres)."),
    ("M_SCALE_AREA", "Doubling the side of a square doubles its area."),
]

SOLUTION_NOTES = [
    "Figure it Out (rectangles and squares) question 1 (ii): the 50 square metre label is read as the area of the "
    "bold outlined rectangle (the 29 square metre piece plus the piece below it), giving a lower height of 84/29, "
    "about 2.9 m.",
    "Figure it Out (rectangles and squares) question 4: the spiral's labelled lengths are outer lengths, so each of "
    "the 8 bends is counted twice and the area is 120 − 8 = 112 square units, as the book's bent tube hint shows.",
    "Grid figures (parallelograms, trapeziums) are read by counting squares on the book's grid.",
]
ERRATA = []

DESIGN_REFERENCES = [
    {"text": "docs/25_new_design_learning_plan_playbook.md: framing intro, idea topics each ending in a practice "
             "concept, a question topic after each idea topic, and one summary topic.", "url": ""},
]

FIGURES = {}
