# -*- coding: utf-8 -*-
"""Topics T1 to T5 (module M1: line symmetry). Book section 9.1 and the chapter opening."""
from topics_common import A, DOER, TOPIC, BOOK_TEXT, book, fio, we

TOPICS = []
H_MORE = "Figures with more than one line of symmetry"
H_REFL = "Reflection"
H_GEN = "Generating shapes having lines of symmetry"
OPEN = BOOK_TEXT["extra_inv_A.json"]["opening"]["textbook_lines"]

# ============================== T1 Chapter opening ===========================================================
TOPICS.append(TOPIC(
    "T1", "M1", "Looking for Repeats Around Us", ["Chapter opening"], "Understand",
    "",
    "A flower, a butterfly, a rangoli and a pinwheel all repeat a part in a definite pattern, and a cloud does not.",
    [A("T1.C1", "Which pictures repeat a pattern?", "Remember", "",
       textbook=OPEN[:3] + OPEN[6:8],
       teach=["Look at a flower, a butterfly, a rangoli and a pinwheel. Before reading on, guess: what do they "
              "share that a cloud does not?",
              "Each one has a part that comes back again in a fixed pattern. A cloud has no such repeat.",
              "When a part of a figure repeats in a definite pattern we say the figure is symmetrical."],
       ncert=["opening"], key_terms=["symmetry", "pattern"], video_focus=["HOOK"], minutes=4, enrichment=True)],
    topic_type="framing"))

# ============================== T2 Line of symmetry (9.1) ====================================================
TOPICS.append(TOPIC(
    "T2", "M1", "Mirror Halves and the Line of Symmetry", ["9.1"], "Understand",
    "Students use a fold to decide whether a line cuts a figure into mirror halves, and name such a line as a line "
    "of symmetry.",
    "A line that folds a figure into two parts that exactly overlap is a line of symmetry.",
    [A("T2.C1", "Mirror halves: the fold test", "Understand",
       "Students fold a figure along a dotted line, decide whether the two halves overlap exactly, and call such "
       "halves mirror halves.",
       textbook=book("9.1", stop=2),
       teach=["Predict first: a blue triangle has a dotted line down its middle. If you fold along the line, will "
              "one half cover the other?",
              "Fold it: the two halves overlap exactly, so they are mirror halves.",
              "Four puzzle pieces with a dotted line through the middle look balanced, but folding shows the left "
              "half does not fit over the right half, so they are not mirror halves."],
       examples=[we("9.1.q4")],
       key_terms=["mirror halves", "fold"], misconceptions=["M_BALANCED", "M_HALVES_ANY"], minutes=8),
     A("T2.C2", "The line of symmetry", "Understand",
       "Students define a line of symmetry as a line that cuts a figure into two parts that overlap exactly when "
       "folded, and name the vertical line of symmetry of a building.",
       textbook=book("9.1", start=2, stop=3) + OPEN[8:],
       teach=["Predict first: the Taj Mahal and the Gopuram both look the same on the left and the right. Where "
              "would a fold go?",
              "A line that cuts a figure into two parts that exactly overlap when folded is called a line of "
              "symmetry.",
              "Both buildings fold along a vertical line down the middle, so that line is a line of symmetry."],
       examples=[we("9.1.q3")],
       key_terms=["line of symmetry", "symmetrical"], misconceptions=["M_BALANCED"], minutes=8),
     DOER("T2.C3", "Pull it together and do it: Fold and Find Lines", "fold_finder", "Apply",
          "Students fold a figure on the tool along a chosen line, check whether the halves overlap, and list the "
          "lines of symmetry the figure has, including none.",
          ["A line of symmetry makes the two parts overlap exactly when folded.",
           "A figure can have one line of symmetry, several, or none.",
           "Look at the fold, not at whether the figure looks balanced."],
          items=[fio("9.1.FiO1.Q1"), fio("9.1.FiO1.Q2")],
          misconceptions=["M_BALANCED", "M_EVERY_LINE"])]))

# ============================== T3 More than one line (9.1) ==================================================
TOPICS.append(TOPIC(
    "T3", "M1", "Many Lines of Symmetry", ["9.1"], "Apply",
    "Students find every line of symmetry of a figure by trying vertical, horizontal and diagonal folds, and "
    "count the lines of standard shapes.",
    "A figure can have several lines of symmetry; try every fold and count those whose halves overlap.",
    [A("T3.C1", "Folding a square four ways", "Apply",
       "Students fold a square vertically, horizontally and along both diagonals, and conclude that a square has "
       "exactly 4 lines of symmetry.",
       textbook=book("9.1", H_MORE, stop=8),
       teach=["Predict first: does a square have only one line of symmetry? How many folds do you think work?",
              "Fold it in half vertically, then horizontally: two lines of symmetry.",
              "Fold along one diagonal and then the other: two more lines, in all 4.",
              "No other fold makes the two halves overlap, so the square has exactly 4 lines of symmetry."],
       examples=[we("9.1.q5"), we("9.1.q6")],
       key_terms=["line of symmetry", "diagonal"], misconceptions=["M_ONE_LINE"], minutes=10),
     A("T3.C2", "Finding all the lines of a figure", "Apply",
       "Students list all the lines of symmetry of a design by trying every direction, and say when a design has "
       "no line at all.",
       textbook=book("9.1", H_MORE, start=8, stop=9),
       teach=["Predict first: a snowflake-like ring, a twisted six-petal flower and a four-loop design. Which has "
              "the most lines, and which has none?",
              "Try vertical, horizontal and slanted folds on each design, and count the folds where the halves "
              "overlap.",
              "The ring has 6 lines and the four-loop design has 4 lines. The twisted flower matches no mirror "
              "image, so it has no line of symmetry."],
       examples=[we("9.1.q7")],
       key_terms=["line of symmetry"], misconceptions=["M_EVERY_LINE", "M_NO_LINE_NO_SYM"], minutes=10),
     A("T3.C3", "Is the diagonal of a rectangle a line of symmetry?", "Analyze",
       "Students test the diagonal of a rectangle that is not a square by folding, and explain why the two "
       "triangles do not overlap.",
       textbook=book("9.1", H_MORE, start=9),
       teach=["Predict first: the diagonal of a square is a line of symmetry. Is the diagonal of a long rectangle "
              "one too?",
              "Fold the rectangle along its diagonal: the two triangles are equal in size, but one corner sticks "
              "out past the other.",
              "Equal halves are not enough. The halves must overlap exactly, so a rectangle that is not a square "
              "has only 2 lines of symmetry, the vertical and the horizontal."],
       examples=[we("9.1.q8")],
       key_terms=["diagonal", "rectangle"], misconceptions=["M_DIAGONAL_RECT", "M_HALVES_ANY"], minutes=8),
     DOER("T3.C4", "Pull it together and do it: Count the Lines", None, "Apply",
          "Students count the lines of symmetry of squares, stars, regular shapes and kolam patterns, and draw "
          "triangles and curved figures with a given number of lines.",
          ["Try vertical, horizontal and diagonal folds on every figure.",
           "An equilateral triangle has 3 lines, a square 4 and a regular hexagon 6.",
           "A triangle can have 0, 1 or 3 lines of symmetry, never exactly 2."],
          items=[fio("9.1.FiO2.Q6"), fio("9.1.FiO2.Q7"), fio("9.1.FiO2.Q8"), fio("9.1.FiO2.Q9"),
                 fio("9.1.FiO2.Q10")],
          misconceptions=["M_ONE_LINE", "M_DIAGONAL_RECT", "M_EVERY_LINE"])]))

# ============================== T4 Reflection (9.1) ==========================================================
TOPICS.append(TOPIC(
    "T4", "M1", "Reflection Symmetry", ["9.1"], "Apply",
    "Students follow where the corners of a square go when it is reflected in a line of symmetry, and complete a "
    "figure so that a given line is its line of symmetry.",
    "Reflecting in a line of symmetry swaps each point with its mirror partner on the other side.",
    [A("T4.C1", "Reflecting a square in its vertical line", "Apply",
       "Students state where corners A, B, C and D of a square go when it is reflected in the vertical line of "
       "symmetry.",
       textbook=book("9.1", H_REFL, stop=2),
       teach=["Predict first: a square ABCD is reflected in its vertical line. Where does corner A go?",
              "Corners B and C on the right move to the left, into the places held by A and D.",
              "Corners A and D move to the right, into the places held by B and C. Each corner swaps with its "
              "mirror partner."],
       examples=[we("9.1.q9")],
       key_terms=["reflection", "line of symmetry"], misconceptions=["M_REFLECT_STAYS"], minutes=8),
     A("T4.C2", "Reflecting in a diagonal and in the horizontal line", "Apply",
       "Students find where the corners of a square go for a reflection in a diagonal and in the horizontal "
       "line, and say which corners stay fixed.",
       textbook=book("9.1", H_REFL, start=2),
       teach=["Predict first: reflect the square in the diagonal from A to C. Which corners stay where they are?",
              "A and C lie on the line, so they stay, and B and D swap places.",
              "In the horizontal line of symmetry, A swaps with D and B swaps with C.",
              "A figure that has a line or lines of symmetry is also said to have reflection symmetry."],
       examples=[we("9.1.q10")],
       key_terms=["reflection symmetry"], misconceptions=["M_REFLECT_STAYS"], minutes=8),
     DOER("T4.C3", "Pull it together and do it: Mirror Completer", "mirror_completer", "Apply",
          "Students reflect each point of a half-figure in a given mirror line and complete the figure so "
          "that the line, or both lines, are lines of symmetry.",
          ["Every point and its mirror partner are the same distance from the line, on opposite sides.",
           "Points on the line stay where they are.",
           "With two lines, reflect in the first and then reflect the whole figure in the second."],
          items=[fio("9.1.FiO2.Q11"), fio("9.1.FiO2.Q12"), fio("9.1.FiO2.Q13")],
          misconceptions=["M_REFLECT_STAYS"])]))

# ============================== T5 Making symmetric shapes (9.1) =============================================
TOPICS.append(TOPIC(
    "T5", "M1", "Making Symmetric Shapes: Ink, Folds and Cuts", ["9.1"], "Apply",
    "Students make symmetric shapes by ink blots, folding and cutting, and find the fold lines from a pattern of "
    "holes or cuts.",
    "A fold is a line of symmetry: anything marked or cut on a folded sheet appears twice or more, mirrored, "
    "when the sheet is opened.",
    [A("T5.C1", "Ink Blot Devils", "Apply",
       "Students make an ink blot on one half of a folded sheet and name the crease as the line of symmetry of "
       "the pattern.",
       textbook=book("9.1", H_GEN, stop=9),
       teach=["Predict first: a few ink drops on one half of a folded sheet. What will you see when you press and "
              "open it?",
              "The blot appears on both sides of the crease, a mirror copy of itself. The crease is the line of "
              "symmetry.",
              "A random blot usually has no other line of symmetry."],
       examples=[we("9.1.q11")],
       key_terms=["crease", "line of symmetry"], misconceptions=["M_BALANCED"], minutes=6),
     A("T5.C2", "Folding and cutting paper", "Apply",
       "Students predict the opened shape after a cut on a folded sheet, and identify the fold as the line of "
       "symmetry of the opened shape.",
       textbook=book("9.1", H_GEN, start=9, stop=14),
       teach=["Predict first: a folded sheet has a cut along a dotted line. What will the opened paper look like?",
              "Open the fold: the cut appears on both sides, the second a mirror image of the first.",
              "The fold line is a line of symmetry of the opened shape."],
       examples=[we("9.1.q12")],
       key_terms=["fold", "cut"], misconceptions=["M_CUT_SAME"], minutes=8),
     A("T5.C3", "Intricate paper cut-outs", "Apply",
       "Students fold a strip several times, cut a pattern, and find the lines of symmetry of the repeating "
       "design.",
       textbook=book("9.1", H_GEN, start=14),
       teach=["Predict first: if you fold a strip three times and cut once, how many copies of the cut appear?",
              "Each fold doubles the copies: one fold gives 2, two folds give 4, three folds give 8.",
              "Every fold line becomes a line of symmetry of the opened design."],
       examples=[we("9.1.q13")],
       key_terms=["fold", "repeating design"], misconceptions=["M_CUT_SAME"], minutes=8),
     DOER("T5.C4", "Pull it together and do it: Punch and Unfold", "punch_unfold", "Apply",
          "Students punch or cut a folded sheet on the tool, unfold it, and find the fold lines that match a given "
          "pattern of holes or a given opened shape.",
          ["The fold line is halfway between each pair of matching holes, at right angles to the line joining them.",
           "Each fold doubles the number of holes or cuts.",
           "To get a shape, fold so that its lines of symmetry sit on the folds."],
          items=[fio("9.1.FiO2.Q1"), fio("9.1.FiO2.Q2"), fio("9.1.FiO2.Q3"), fio("9.1.FiO2.Q4"),
                 fio("9.1.FiO2.Q5")],
          misconceptions=["M_CUT_SAME"])]))
