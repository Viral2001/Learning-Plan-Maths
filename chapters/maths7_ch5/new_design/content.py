# -*- coding: utf-8 -*-
"""Chapter-level content for Class 7 Chapter 5, Parallel and Intersecting Lines (Ganita Prakash Grade 7 Part I,
Chapter 5). Book lines elsewhere are verbatim except: the book's dashes become commas, colons or "to"; minus is
U+2212; "Note to the Teacher" boxes are reworded as "Note:" so no banned word appears."""
from __future__ import annotations

CHAPTER = {
    "grade": 7,
    "label": "Class 7",
    "chapter_no": 5,
    "name": "Parallel and Intersecting Lines",
    "book_part": "Ganita Prakash Grade 7 Part I, Chapter 5",
    "source_pdf": "textbooks/class7/gegp105.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Lines That Meet",
     "A square of folded paper shows lines that meet and lines that do not. Two lines that cross make four angles: "
     "linear pairs add to a straight angle and vertically opposite angles are equal, proved by reasoning. Measuring "
     "and reasoning are told apart, and lines that cross at a right angle are perpendicular."),
    ("M2", "Lines That Never Meet",
     "Parallel lines are lines in one plane that never meet however far they run. They are spotted in pictures, in "
     "paper folds and on dot paper, and marked with arrow marks and a square for a right angle."),
    ("M3", "A Line Across Two Lines",
     "A transversal across two lines makes eight angles with at most four different measures. Corresponding angles "
     "are named, equal corresponding angles are drawn and shown to give parallel lines, and parallel lines are "
     "shown to give equal corresponding angles."),
    ("M4", "Drawing Parallel Lines",
     "Parallel lines are drawn with a ruler and a set square by sliding, and a line parallel to a given line is "
     "made through a given point, with tools and by paper folding."),
    ("M5", "Alternate and Interior Angles",
     "Alternate angles are equal when the lines are parallel, and interior angles on the same side add to a "
     "straight angle. Both are proved from corresponding angles and used to find unknown angles, test for parallel "
     "lines and work in a four-sided figure and in zig-zag figures."),
    ("M6", "Illusions and Summary",
     "Lines that look bent although they are parallel, and a closing summary of the chapter."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter follows the book's own order: lines that meet, lines that never meet, a line across two "
             "lines, drawing parallel lines, and the angle rules that follow. Every rule is reached by reasoning "
             "from one earlier fact, so an angle fact is never a thing to memorise.",
    "points": [
        {"title": "Try first, name later",
         "text": "The hook video leaves two folded-paper lines open: do they meet if they are drawn longer? The "
                 "words intersect, perpendicular and parallel arrive only after the student has looked at lines."},
        {"title": "Reasoning and measuring are told apart",
         "text": "Every angle fact is first met by measuring, then justified from a straight angle being 180 "
                 "degrees. A measured pair may be a degree or two off, and the plan says why."},
        {"title": "One chain of reasons",
         "text": "Linear pairs prove vertically opposite angles; corresponding angles decide parallel lines; "
                 "corresponding plus vertically opposite give alternate angles; corresponding plus a linear pair "
                 "give interior angles on the same side."},
        {"title": "Concept, then practice, topic by topic",
         "text": "Each idea gets its own topic with one video per concept and a practice concept at the end; "
                 "interactive tools appear only where handling the angles is the idea. The book's questions follow "
                 "in their own topic, one question and one video per concept."},
    ],
}

NCERT_ITEMS = [
    # 5.1 Across the Line
    "5.1.fold_lines", "5.1.plane", "5.1.intersect", "5.1.two_points", "5.1.act1", "5.1.a120", "5.1.proof",
    "5.1.pairs_named", "5.1.FiO1", "5.1.measure_geom",
    # 5.2 Perpendicular Lines
    "5.2.perp_q", "5.2.perp_def",
    # 5.3 Between Lines
    "5.3.fig55", "5.3.extend", "5.3.parallel_def", "5.3.classroom", "5.3.fig56", "5.3.same_plane",
    # 5.4 Parallel and Perpendicular Lines in Paper Folding
    "5.4.act2_edges", "5.4.act2_counts", "5.4.act2_diag", "5.4.fig58", "5.4.notation",
    "5.4.FiO1", "5.4.FiO2", "5.4.FiO3", "5.4.FiO4", "5.4.FiO5", "5.4.dot_note",
    # 5.5 Transversals
    "5.5.transversal", "5.5.eight", "5.5.five", "5.5.max4",
    # 5.6 Corresponding Angles
    "5.6.corr", "5.6.act3", "5.6.corr_rule", "5.6.act4", "5.6.act5", "5.6.nonparallel",
    # 5.7 Drawing Parallel Lines
    "5.7.set_square", "5.7.long_side", "5.7.nec_suff", "5.7.FiO1", "5.7.fold_parallel", "5.7.why_parallel",
    # 5.8 Alternate Angles
    "5.8.alt", "5.8.act6", "5.8.ex1", "5.8.ex2", "5.8.ex3", "5.8.interior", "5.8.ex4",
    "5.8.FiO1", "5.8.FiO2", "5.8.FiO3", "5.8.FiO4", "5.8.FiO5", "5.8.FiO6",
    # 5.9 Parallel Illusions
    "5.9.illusions", "summary",
]

MISCONCEPTIONS = [
    ("M_LOOKS_PARALLEL", "Two lines that look parallel in a picture are parallel, and two lines that look as if they "
                         "lean towards each other must be about to meet; judging by eye is enough."),
    ("M_MEASURE_EXACT", "A measured value with a protractor is exact, so a linear pair that measures 182 degrees "
                        "means the rule of 180 degrees is wrong."),
    ("M_ADJACENT_EQUAL", "Angles next to each other at a crossing are equal, or opposite angles add to 180 degrees."),
    ("M_ARM_LENGTH", "An angle with longer arms is a bigger angle."),
    ("M_PERP_TILT", "Perpendicular lines must be one vertical and one horizontal."),
    ("M_CORR_ANY", "Corresponding angles are equal for any two lines cut by a transversal."),
    ("M_ALT_SUM", "Alternate angles add up to 180 degrees."),
    ("M_INTERIOR_EQUAL", "Interior angles on the same side of the transversal are equal."),
    ("M_PARALLEL_SAME_PLANE", "Two lines that never meet are parallel, even if they lie in different planes."),
    ("M_ONE_FOLD", "Each fold of a sheet adds just one more parallel line, so the counts grow by two."),
    ("M_WRONG_PAIR", "The wrong pair of angles is used: an angle from a different transversal, or the two angles of "
                     "a linear pair, is treated as a corresponding pair."),
]

SOLUTION_NOTES = [
    "Activity 2 (folding a sheet horizontally): the plan counts the two edges as well as the creases, which gives 3, "
    "5 and 9 parallel lines after one, two and three folds, that is 2 times itself n times, plus 1. The book's "
    "printed answer says the pattern is 2n + 1, which would give 3, 5, 7; the counts 3, 5, 9 that the same answer "
    "gives for the first three folds fit 2 to the power n, plus 1, which is what is taught here.",
    "The in-text prompts that depend on a picture (the segments in the picture of meeting and crossing segments, "
    "the leaning pair, the nine segments and the two lines near each other) are described in words with the angle "
    "measured from the printed figure, and are worded as 'about'.",
    "Figure it Out (parallel and perpendicular lines) Q3 and Q4 and the dot-paper Q1 ask the student to draw; the "
    "solutions describe each drawing step by step with the dot positions, since no figure can be handed back.",
    "Figure it Out (angles) Q1: ten small figures a to j. Each question text names the given angle, where the "
    "unknown angle sits and which angles are distractors (for e, h, i and j the figure shows extra angles that "
    "are not needed).",
    "Figure it Out (angles) Q5: the printed answer x = y = 125 degrees agrees with the working here (x is "
    "180 degrees minus the alternate angle of 55 degrees, and y is its corresponding angle).",
    "The corresponding angles of the three lines a, b and c in Figure it Out Q5 (dot paper) are measured from the "
    "printed figure, so they are written as 'about 30, 29 and 33 degrees'; the book's key says c is parallel to a.",
]
ERRATA = []

DESIGN_REFERENCES = [
    {"text": "docs/25_new_design_learning_plan_playbook.md: framing intro, idea topics ending in "
             "a practice concept, a question topic after each idea topic, and one summary topic; the Class 7 "
             "Chapter 10 plan for one video per concept and one question per concept.", "url": ""},
]

FIGURES = {
    "T1.C1": ["A square sheet of paper folded in different ways, with pencil lines drawn along the creases."],
    "T2.C1": ["Two lines crossing at a point with the four angles a, b, c and d marked."],
    "T4.C1": ["Pairs of line segments: two sharing an endpoint, two crossing off-centre, two crossing at their "
              "midpoints, one pair leaning slightly towards each other and one pair running side by side."],
    "T4.C2": ["Nine line segments a to i on a grid; some vertical, some horizontal, two pairs on the diagonals."],
    "T6.C1": ["A transversal t crossing two lines l and m, with the eight angles numbered 1 to 8."],
    "T7.C1": ["Line l, a transversal t meeting l at X, and a second line m through Y on t with equal corresponding "
              "angles of sixty degrees."],
    "T8.C1": ["A ruler along line l and a set square sliding along it, with two lines drawn at right angles to l."],
    "T9.C1": ["A transversal across two parallel lines with the angles a to h marked; f and d are alternate angles."],
    "T10.C2": ["A four-sided figure ABCD with its diagonal AC: AB parallel to CD and AD parallel to BC."],
    "T11.C1": ["Three line drawings that make parallel lines look bent: radiating spokes across straight lines, "
               "short slanted strokes in a brick pattern, and a pair of lines through a burst of spokes."],
}

# Hook slot extras (build.py passes these into the hook's worklist slot).
HOOK_HANDOVER = ("Try it: fold a sheet of paper a few times, draw a pencil line along two creases, and decide "
                 "whether they would meet if you drew them much longer. Keep your answer for the next topic.")
HOOK_NOTE = ("The hook leaves the folded-paper question open. Do not say that any pair meets or does not meet; "
             "the words intersect and parallel are settled in the next topics.")

# Words the narration may need that are hard for a Class 7 reader; the script author defines or avoids them.
HARD_WORDS = ["intersect", "transversal", "perpendicular", "parallel", "vertically opposite", "corresponding",
              "alternate", "interior", "linear pair", "protractor", "set square"]
