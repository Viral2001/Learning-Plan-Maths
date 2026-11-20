# -*- coding: utf-8 -*-
"""Topics T1, T1B, T2 and T3 (modules M1: Weaving Patterns and M2: Tiling and Tessellation). The framing intro (the
woven baskets hook and the free Mat Weaver), the idea topic T1B (Describing a Weave), Tiles Around a Point, and
Patterns with More Than One Shape.
Every teaching concept has one worked example with the plan's own numbers; every book question is an FIO item of its
topic's DOER, in the book's order."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Weaving Mats (framing) ==================================================
# The framing topic holds only the hook video and the free-try tool, and no book question. The concept videos and
# the book's weaving questions follow in the idea topic T1B.
TOPICS.append(TOPIC(
    "T1", "M1", "Weaving Mats", ["Weaving Mats"], "Understand",
    "",
    "Woven baskets show different weaving patterns. Try weaving a mat with paper strips, over and under, and look "
    "at the pattern you make.",
    [A("T1.C1", "Weaving Mats", "Understand",
       "",
       textbook=["You may have seen woven baskets of different kinds. If you look closely, you will notice different "
                 "weaving patterns on each basket.",
                 "We will try weaving some mats with paper strips."],
       teach=["Predict first: look closely at three woven baskets. Do you think they all have the same weaving "
              "pattern?",
              "No. If you look closely, you notice a different weaving pattern on each basket.",
              "We will try weaving a mat with paper strips, the way a basket maker weaves a basket.",
              "How would you describe the pattern of a woven mat? Think about it, then weave one on the next "
              "screen."],
       ncert=["w.intro"], key_terms=["weave", "pattern", "mat"],
       video_focus=["HOOK"], enrichment=True, minutes=4),
     DOER("T1.C3", "Mat Weaver: Explore", "mat_weaver", "Understand",
          "",
          ["You saw woven baskets, each with its own weaving pattern.",
           "Weave paper strips over and under the slits of a mat, one strip at a time.",
           "Then say what you see in the first two rows."],
          misconceptions=["M_WEAVE_SAME"], role="try_it", enrichment=True)],
    topic_type="framing", key_terms=["weave", "pattern", "mat"]))

# ============================== T1B Describing a Weave =====================================================
TOPICS.append(TOPIC(
    "T1B", "M1", "Describing a Weave", ["Weaving Mats"], "Apply",
    "Students describe the rows of a weave in words, with counts of over and under steps and the word repeat, and "
    "find the row where the pattern starts to repeat.",
    "A row of a weave is described in words: count the over and under steps, then say repeat. The next row can swap "
    "over and under or move along, and the pattern repeats when a row is the same as Row 1.",
    [A("T1B.C1", "Describing a Weave in Words", "Understand",
       "Students describe one row of a weave in words by counting the over and under steps and saying repeat, and "
       "write the next row by swapping over and under.",
       textbook=["Let us make paper mats. You will need: A coloured paper (30 cm long and 20 cm wide) and eight paper "
                 "strips of two different colours (3 cm wide and longer than 20 cm).",
                 "Fold the coloured paper in half along the longer side.",
                 "Draw vertical lines at equal distances from the closed end and cut slits leaving a gap of 3 cm at "
                 "the top.",
                 "Carefully unfold the paper. There will be no cuts in the paper at the top and the bottom.",
                 "Take one colour strip and weave it across the slits going 1 under and 1 over, and again 1 under "
                 "and 1 over. Repeat it for the first row.",
                 "Take one more strip of another colour and weave it across the slits going 1 over and 1 under, and "
                 "again 1 over and 1 under. Repeat it for the second row.",
                 "Weave all the strips in the same alternating pattern. Neatly fold any extra strip ends behind the "
                 "mat. Your mat is ready!",
                 "We can describe the pattern of the above weave as follows. Row 1: 1 under, 1 over, 1 under, 1 "
                 "over, ... (repeat). Row 2: 1 over, 1 under, 1 over, 1 under, ... (repeat)."],
       teach=["Predict first: a strip goes over, over, over, under, under, and then does the same again. How can you "
              "tell a friend this row in a few words, without saying every slit?",
              "Count the steps that stay together: 3 over, then 2 under. Over means the strip lies on top and "
              "shows. Under means it goes below.",
              "That group comes again and again, so we say repeat. The row is: 3 over, 2 under (repeat).",
              "The next row swaps over and under. Where Row 1 goes over, Row 2 goes under. So Row 2 is: 3 under, "
              "2 over (repeat).",
              "Your maths book weaves a paper mat this way. The slits are cut in a paper 30 cm long, with a gap of "
              "3 cm at the top and the bottom, so the slits are 30 − 3 − 3 = 24 cm long. Eight strips that are 3 cm "
              "wide fill them: 8 × 3 = 24 cm.",
              "Rule: describe a row by counting the over and under steps, then say repeat."],
       examples=[WE("A mat has 10 slits. A strip goes over, over, over, under, under, over, over, over, under, "
                    "under. Describe Row 1 in words. Then describe Row 2, where every strip swaps over and under.",
                    ["Read the strip slit by slit: over, over, over, under, under, over, over, over, under, under. "
                     "Over means the strip lies on top and shows.",
                     "Count the steps that stay together: 3 over, then 2 under.",
                     "The same group comes again, so the row repeats: Row 1: 3 over, 2 under (repeat).",
                     "Row 2 swaps over and under: every over becomes under and every under becomes over.",
                     "So Row 2 goes under, under, under, over, over, under, under, under, over, over: Row 2: 3 under, "
                     "2 over (repeat).",
                     "Check: each group has 3 + 2 = 5 slits, and two groups make 5 + 5 = 10 slits, the whole row."],
                    "Row 1: 3 over, 2 under (repeat). Row 2: 3 under, 2 over (repeat)")],
       ncert=["w.make", "w.describe"], key_terms=["weave", "row", "over", "under", "repeat"],
       misconceptions=["M_WEAVE_SAME"], minutes=6),
     A("T1B.C2", "Rows That Repeat", "Analyze",
       "Students write the rows of a weave until a row is the same as Row 1, and say after how many rows the pattern "
       "repeats.",
       teach=["Predict first: a mat has 9 slits and Row 1 is 1 over, 2 under (repeat). Each next row is the row above "
              "moved one slit to the right. After how many rows will a row look the same as Row 1?",
              "Write Row 1: over, under, under, over, under, under, over, under, under.",
              "Move it one slit to the right. The last step comes round to the front. Row 2 is under, over, under, "
              "under, over, under, under, over, under.",
              "Move it again for Row 3, and again for Row 4. After each move, compare the new row with Row 1.",
              "Row 4 is the same as Row 1, so the rows repeat after 3 rows. Row 5 is the same as Row 2, and Row 6 is "
              "the same as Row 3.",
              "(do not repeat) means: say that step only once, at the start of the row. Row 2 is: 1 under (do not "
              "repeat), 1 over, 2 under (repeat).",
              "Rule: write the rows until a row is the same as Row 1. Then the pattern repeats."],
       examples=[WE("A mat has 9 slits. Row 1 is: 1 over, 2 under (repeat). Each next row is the row above moved one "
                    "slit to the right. Write Row 2 and Row 3 in words, and say after how many rows the rows start "
                    "to repeat.",
                    ["Row 1: 1 over, 2 under (repeat) goes over, under, under, over, under, under, over, under, "
                     "under across the 9 slits.",
                     "Move Row 1 one slit to the right. The last step, under, comes round to the front. Row 2 goes "
                     "under, over, under, under, over, under, under, over, under.",
                     "In words: Row 2: 1 under (do not repeat), 1 over, 2 under (repeat).",
                     "Move again for Row 3: under, under, over, under, under, over, under, under, over.",
                     "In words: Row 3: 2 under, 1 over (repeat).",
                     "Move once more for Row 4: over, under, under, over, under, under, over, under, under. Row 4 is "
                     "the same as Row 1.",
                     "Check: Row 4 matches Row 1, so Rows 4, 5 and 6 are Rows 1, 2 and 3 again, and the rows repeat "
                     "after 3 rows."],
                    "Row 2: 1 under (do not repeat), 1 over, 2 under (repeat). Row 3: 2 under, 1 over (repeat). Row "
                    "4 is the same as Row 1, so the rows repeat after 3 rows")],
       key_terms=["rows", "repeat", "pattern", "weave"],
       misconceptions=["M_WEAVE_RESTART"], minutes=6),
     DOER("T1B.C3", "Practice: Weave Rules", "weave_rules", "Apply",
          "Students build rows of a weave from rules of over and under steps, and find the row where the pattern "
          "starts to repeat.",
          ["Over means the strip lies on top and shows. Under means it goes below.",
           "A row is described by counting the over and under steps, then saying repeat.",
           "The next row can swap over and under, or move along. Write the rows until a row is the same as Row 1."],
          items=[FIO("w.q2", "Weaving Mats: the 2 over, 1 under mat",
                     "Can you figure out how to make this mat? Let us try to understand how this mat is woven by "
                     "looking at the pattern in the first two rows. Row 1: 2 over, 1 under, 2 over, 1 under, ... "
                     "Row 2: 2 under, 1 over, 2 under, 1 over, ... You can use strips of the same colour or 2 "
                     "different colours, one for each row.",
                     ["The mat has 8 slits, and each row is one strip. Over means the strip shows on top.",
                      "Row 1: 2 over, 1 under, 2 over, 1 under, ... goes over, over, under, over, over, under, "
                      "over, over across the 8 slits.",
                      "Row 2: 2 under, 1 over, 2 under, 1 over, ... goes under, under, over, under, under, over, "
                      "under, under.",
                      "Row 2 swaps over and under in Row 1: where Row 1 goes over, Row 2 goes under.",
                      "Go on in the same way: Rows 3, 5 and 7 are like Row 1, and Rows 4, 6 and 8 are like Row 2.",
                      "Weave the 8 strips one by one, with one colour for all rows or two colours.",
                      "Check: Row 1 uses 2 + 1 + 2 + 1 + 2 = 8 slits, and so does Row 2."],
                     "Sample answer: Row 1 goes over, over, under (repeat) and Row 2 swaps it: under, under, over "
                     "(repeat). Odd rows are like Row 1, even rows like Row 2. Your answer may differ.",
                     kind="prompt",
                     q_figure="A woven mat with 8 columns and 8 rows, with wide blue strips lying over cream gaps; "
                              "the first two rows are woven as Row 1 and Row 2 in the question.",
                     s_figure="The same mat with Row 1 and Row 2 marked, showing that the odd rows copy Row 1 and "
                              "the even rows copy Row 2."),
                 FIO("w.q3", "Weaving Mats: weave by four rules",
                     "Try to weave a pattern, using the rules given below. Row 1: 2 over, 1 under, 2 over, 1 under, "
                     "... (repeat). Row 2: 1 under (do not repeat), 3 over, 3 under, 3 over, 3 under, ... "
                     "(repeat). Row 3: 2 under, 1 over, 2 under, ... (repeat). Row 4: 1 over (do not repeat), 3 "
                     "under, 3 over, ... (repeat). Continue weaving in this order.",
                     ["Over means the strip lies on top and shows. Under means it goes below.",
                      "Row 1: 2 over, 1 under, 2 over, 1 under, ... (repeat). The strip goes over, over, under "
                      "again and again.",
                      "Row 2: say 1 under once (do not repeat), then 3 over, 3 under, 3 over, 3 under, ... "
                      "(repeat).",
                      "Row 3: 2 under, 1 over, 2 under, ... (repeat). This swaps over and under in Row 1.",
                      "Row 4: say 1 over once (do not repeat), then 3 under, 3 over, ... (repeat). This swaps over "
                      "and under in Row 2.",
                      "Row 5 follows the first rule again, so it is the same as Row 1. The pattern repeats after 4 "
                      "rows.",
                      "Check: 4 rows repeated 4 times make 4 × 4 = 16 rows, the whole mat."],
                     "Sample answer: Row 1: 2 over, 1 under; Row 2: 1 under, then 3 over, 3 under; Row 3 swaps Row "
                     "1; Row 4 swaps Row 2. Row 5 is Row 1: it repeats after 4 rows. Your answer may differ.",
                     kind="prompt",
                     q_figure="A red and green woven mat with 16 columns and 16 rows.",
                     s_figure="The first 4 rows of the mat, each labelled with its rule, and a mark showing that "
                              "Row 5 is the same as Row 1."),
                 FIO("w.q4", "Weaving Mats: write the steps of a design",
                     "Can you work out the steps for any of these designs and weave the pattern? Write the steps of "
                     "the pattern in your notebook for each row until it starts repeating.",
                     ["Over means the colour of the strip shows on top.",
                      "Design 1, Row 1: 1 under (do not repeat), 3 over, 3 under (repeat).",
                      "Row 2: 3 over, 3 under (repeat).",
                      "Row 3: 2 over (do not repeat), 3 under, 3 over (repeat).",
                      "Row 4: 2 under (do not repeat), 3 over, 3 under (repeat).",
                      "Row 5: 3 under, 3 over (repeat).",
                      "Row 6: 1 over (do not repeat), 3 under, 3 over (repeat).",
                      "Row 7 is the same as Row 1: design 1 repeats after 6 rows.",
                      "Design 2, Row 1: 1 over, 3 under (repeat). Row 2: 2 over (do not repeat), 1 under, 3 over "
                      "(repeat).",
                      "Design 2, Row 3: 1 under, 3 over (repeat). Row 4: 2 under (do not repeat), 1 over, 3 under "
                      "(repeat).",
                      "Check: Row 5 of design 2 is the same as Row 1, so it repeats after 4 rows."],
                     "Sample answer: design 1 repeats after 6 rows (Row 1: 1 under, then 3 over, 3 under, repeat). "
                     "Design 2 repeats after 4 rows. Your answer may differ.",
                     kind="prompt",
                     q_figure="Two woven designs side by side: one in purple over light blue with long purple "
                              "strips, and one in teal and lavender that looks like bricks.",
                     s_figure="The first 6 rows of design 1 drawn as rows of purple and light blue cells, with Row "
                              "7 marked as the same as Row 1."),
                 FIO("w.try", "Let Us Try: complete the design on the grid",
                     "Draw the following pattern on a grid paper. Part of it is done for you. Now, complete the rest "
                     "of the grid to get the full design.",
                     ["The design is a mat 21 squares across and 21 squares down. A yellow square is a strip that "
                      "shows on top.",
                      "Top row: a yellow square sits on every other cell, starting with the first, so there are 11 "
                      "yellow squares and 10 gaps: 11 + 10 = 21.",
                      "The first column and the last column also have a yellow square on every other cell.",
                      "From the top row, the squares then spread in two diagonal lines, like the sides of a "
                      "diamond.",
                      "The left half and the right half of the design match, so draw one half and copy it on the "
                      "other side.",
                      "Check: every row has 21 cells, and the part already drawn on the grid matches your drawing."],
                     "Sample answer: 11 yellow squares on every other cell of the top row, then two diagonal lines "
                     "like a diamond; the left half matches the right half. Your drawing may differ in small "
                     "details.",
                     kind="exercise",
                     q_figure="A green and yellow woven mat of 21 columns and 21 rows, next to a dot grid with the "
                              "top rows already drawn.",
                     s_figure="The dot grid with the whole design drawn: yellow squares on every other cell of the "
                              "top row, then two diagonal lines spreading like a diamond, the left half matching "
                              "the right half.")],
          misconceptions=["M_WEAVE_SAME", "M_WEAVE_RESTART"])],
    key_terms=["weave", "row", "repeat"]))

# ============================== T2 Tiles Around a Point ====================================================
TOPICS.append(TOPIC(
    "T2", "M2", "Tiles Around a Point", ["Tiling and Tessellation"], "Apply",
    "Students say what a regular shape is and tell which regular shapes fill the space round a point with no gap and "
    "no overlap, that is, which ones tessellate.",
    "Shapes that have equal sides are called regular shapes. Shapes fit around a point when their corners fill the "
    "space with no gap and no overlap, and then they tessellate.",
    [A("T2.C1", "Regular Shapes", "Understand",
       "Students sort shapes into regular and not regular by comparing the lengths of their sides, and name a "
       "regular pentagon and a regular octagon.",
       textbook=["We often use tiles of the same shape or a combination of shapes to cover a region.",
                 "You can see pentagons (5-sided figures) in this figure. As all its sides are equal it is a regular "
                 "pentagon.",
                 "Shapes that have equal sides are called regular shapes.",
                 "A regular octagon means a shape with eight equal sides.",
                 "Regular octagons do not tessellate."],
       teach=["Predict first: a square has every side 6 cm and a rectangle is 6 cm by 4 cm. Which one is a regular "
              "shape?",
              "Look at the sides. The square has 4 equal sides, so it is a regular shape. The rectangle has sides "
              "of 6 cm and 4 cm, so its sides are not all equal.",
              "A pentagon is a 5-sided shape. With all 5 sides equal, 3 cm each, it is a regular pentagon.",
              "A regular octagon is a shape with 8 equal sides.",
              "We use tiles of one shape, or of a few shapes, to cover a region. Soon you will see which regular "
              "shapes fit together.",
              "Rule: shapes that have equal sides are called regular shapes."],
       examples=[WE("A square has every side 6 cm. A rectangle is 6 cm by 4 cm. A pentagon has every side 3 cm. Which "
                    "of these shapes are regular shapes?",
                    ["A regular shape has all its sides equal.",
                     "The square: all 4 sides are 6 cm. They are equal, so it is a regular shape.",
                     "The rectangle: 2 sides are 6 cm and 2 sides are 4 cm. They are not all equal, so it is not a "
                     "regular shape.",
                     "The pentagon: all 5 sides are 3 cm. They are equal, so it is a regular pentagon.",
                     "Check: in the square and in the pentagon every side is the same length, but the rectangle has "
                     "a longer pair of sides and a shorter pair."],
                    "The square and the pentagon are regular shapes. The rectangle is not, because its sides are "
                    "not all equal")],
       ncert=["tt.intro", "tt.regular", "tt.octagon"],
       key_terms=["regular shape", "equal sides", "regular pentagon", "regular octagon"], minutes=5),
     A("T2.C2", "Fitting Shapes Around a Point", "Understand",
       "Students decide whether copies of a shape fill the space round a point with no gap and no overlap, and say "
       "that such a shape tessellates.",
       textbook=["Pentagons cannot fill a region without leaving gaps. So, we say that regular pentagons do not "
                 "tessellate.",
                 "Regular triangles when fitted around a point leave no gaps and there is no overlap.",
                 "Triangles with all equal sides are also called equilateral triangles. Therefore, equilateral "
                 "triangles tessellate."],
       teach=["Predict first: you have rectangles of one size, 6 cm by 4 cm, and each has 4 right angle corners. How "
              "many can you fit around a point with no gap and no overlap?",
              "Put one corner of each rectangle on the point. After 4 rectangles the 4 right angle corners fill all "
              "the space round the point.",
              "A 5th rectangle has no room. It would lie over the others. That is an overlap.",
              "Watch for two things when shapes meet at a point: a gap that is left, and an overlap.",
              "Pentagons cannot fill a region without leaving gaps. The gap left is too small for another pentagon, "
              "and a pentagon put there would overlap. So regular pentagons do not tessellate.",
              "Regular triangles fitted around a point leave no gaps and there is no overlap. Triangles with all "
              "equal sides are equilateral triangles. So equilateral triangles tessellate.",
              "Rule: shapes fit around a point when their corners fill the space with no gap and no overlap. If a "
              "gap is left that is too small for another shape, or a shape overlaps, they do not fit."],
       examples=[WE("Rectangles of one size, 6 cm by 4 cm, each have 4 right angle corners. Put one corner of each "
                    "rectangle on a point, edge to edge. How many rectangles fit around the point with no gap and no overlap? Would "
                    "a 5th rectangle fit?",
                    ["Put one corner of the first rectangle on the point. Each corner of a rectangle is a right "
                     "angle.",
                     "Put the second rectangle next to it, edge to edge, with one corner on the point too.",
                     "Go on round the point. After 4 rectangles the 4 right angle corners fill the whole space.",
                     "There is no gap and no overlap, so 4 rectangles fit around the point.",
                     "Try a 5th rectangle. There is no space left, so it would lie over the others. That is an "
                     "overlap.",
                     "Check: 4 corners fill the space exactly, so 3 rectangles would leave a gap and 5 would "
                     "overlap."],
                    "4 rectangles fit around the point with no gap and no overlap, because 4 right angle corners "
                    "fill the space. A 5th would overlap")],
       ncert=["tt.no_pentagon", "tt.triangle"],
       key_terms=["tessellate", "around a point", "gap", "overlap"],
       misconceptions=["M_ALL_REGULAR_TILE", "M_NEARLY_FITS"], minutes=7),
     DOER("T2.C3", "Practice: Fit Around a Point", "fit_around_point", "Apply",
          "Students fit regular triangles, squares, pentagons, hexagons and octagons around a point and say which "
          "fit with no gap and no overlap.",
          ["A regular shape has all its sides equal.",
           "Shapes fit around a point when their corners fill the space with no gap and no overlap.",
           "If the gap left is too small for another shape, or a shape would overlap, they do not fit."],
          items=[FIO("tt.pent4", "Tiling and Tessellation: a fourth pentagon",
                     "We have placed 3 pentagons around a point. Can we fit one more into the empty space?",
                     ["Look at the 3 pentagons that meet at the point. Their corners fill most of the space round "
                      "the point.",
                      "The empty space that is left is smaller than one more pentagon corner.",
                      "A fourth pentagon is too big for the gap. It would lie over its neighbours: an overlap.",
                      "So regular pentagons leave a gap that is too small to use, and they do not tessellate.",
                      "Check: a fourth pentagon would stick out over the others, so the answer is no."],
                     "No. The gap is too small for a fourth pentagon, so it would overlap the others. Regular "
                     "pentagons do not tessellate.",
                     kind="prompt",
                     q_figure="Three regular pentagons placed around a point, with a gap left.",
                     s_figure="The same picture with a dashed fourth pentagon that sticks out over its neighbours, "
                              "showing that it does not fit in the gap."),
                 FIO("fo.triangle", "Find Out: regular triangles around a point",
                     "Can regular triangles fit together at a point without any gap? How many of them fit together?",
                     ["Put one regular triangle with a corner on the point. A regular triangle has all 3 sides "
                      "equal.",
                      "Put the next triangle beside it, edge to edge, with its corner on the point too.",
                      "Go on round the point. After 6 triangles the last one touches the first one: no gap and no "
                      "overlap.",
                      "Check: with only 5 triangles a gap is left, and a 7th triangle would overlap, so exactly 6 "
                      "fit."],
                     "Yes. 6 regular triangles fit together at a point with no gap and no overlap.",
                     kind="prompt"),
                 FIO("fo.square", "Find Out: squares around a point",
                     "Can squares (a regular 4-sided shape) fit together around a point without any gap or overlap? "
                     "Try it out using cutouts of squares. How many squares did you need?",
                     ["Put one square with a corner on the point. A corner of a square is a right angle.",
                      "Put the next square beside it, edge to edge, with its corner on the point too.",
                      "After 4 squares the last one touches the first one. The 4 corners fill the space.",
                      "Check: 3 squares leave a gap and a 5th square would overlap, so exactly 4 are needed."],
                     "Yes. 4 squares fit around a point with no gap and no overlap, because 4 right angle corners "
                     "fill the space.",
                     kind="prompt"),
                 FIO("fo.five", "Find Out: five squares",
                     "Can five squares fit together around a point without any gaps or overlaps? Why or why not?",
                     ["Fit squares round the point one by one. After 4 squares the space is full.",
                      "A fifth square has no room. It would sit on top of the first square: an overlap.",
                      "So five squares cannot fit around a point without an overlap.",
                      "Check: 4 squares fit exactly, and 5 is one more than 4, so there is no room for it."],
                     "No. 4 squares already fill the space round the point, so a fifth square would overlap the "
                     "first one.",
                     kind="prompt"),
                 FIO("fo.hexagon", "Find Out: regular hexagons around a point",
                     "Can regular hexagons (6-sided shapes with equal sides) fit together around a point without "
                     "any gaps or overlaps? Try and see. How many fit together at a point?",
                     ["Put one hexagon with a corner on the point. A regular hexagon has 6 equal sides.",
                      "Put a second hexagon beside it, edge to edge, and then a third.",
                      "After 3 hexagons the third one touches the first one: no gap and no overlap.",
                      "Check: 2 hexagons leave a gap and a 4th hexagon would overlap, so exactly 3 fit."],
                     "Yes. 3 regular hexagons fit together at a point with no gap and no overlap.",
                     kind="prompt"),
                 FIO("tt.oct", "Tiling and Tessellation: regular octagons",
                     "Do regular octagons fit together without any gaps or overlaps? Try drawing the same and "
                     "check.",
                     ["Draw a regular octagon, a shape with 8 equal sides. Draw a second one beside it, edge to "
                      "edge, with a corner on the same point.",
                      "The 2 octagons leave a gap at the point. A third octagon is too big for the gap, so it "
                      "would overlap.",
                      "The gap is just the size of a square corner: 2 octagons and 1 square fill the point.",
                      "So regular octagons alone leave gaps, and they do not tessellate.",
                      "Check: a third octagon corner is bigger than the gap, so it cannot fit."],
                     "No. 2 octagons side by side leave a gap that is too small for a third, so regular octagons do "
                     "not tessellate. A square fits that gap.",
                     kind="prompt",
                     q_figure="A regular octagon.",
                     s_figure="Two regular octagons side by side with a gap at the point between them, and a small "
                              "square that fills the gap exactly.")],
          misconceptions=["M_ALL_REGULAR_TILE", "M_NEARLY_FITS"])],
    key_terms=["regular shape", "tessellate", "point"]))

# ============================== T3 Patterns with More Than One Shape =======================================
TOPICS.append(TOPIC(
    "T3", "M2", "Patterns with More Than One Shape", ["Tiling and Tessellation"], "Analyze",
    "Students list the shapes that meet at a point of a pattern made with two shapes, say whether the same set of "
    "shapes meets at every point, and continue the pattern.",
    "Tiles of two shapes can cover a region when they repeat in the same order. At each meeting point, list the "
    "shapes and compare the lists to see whether the same set of shapes meets everywhere.",
    [A("T3.C1", "Two Shapes Take Turns", "Analyze",
       "Students list the shapes that meet at the joins of a border made of two shapes that take turns, and say "
       "whether the same set of shapes meets at every join.",
       textbook=["Here is a tessellating pattern with more than one shape."],
       teach=["Predict first: a border has 12 tiles in a row: square, triangle, square, triangle, and so on. How many "
              "squares and how many triangles are there?",
              "The tiles take turns, so every second tile is a square: 6 squares and 6 triangles. 6 + 6 = 12.",
              "Look at each join between two neighbours. A square is on one side and a triangle is on the other.",
              "So the same two kinds of shape meet at every join: a square and a triangle.",
              "A pattern with two shapes repeats the shapes in the same order. If the order changes, the shapes at "
              "a join can change too.",
              "Rule: tiles of two shapes can cover a region when they repeat in the same order. At each meeting "
              "point, list the shapes and compare."],
       examples=[WE("A border has 12 tiles in a row. The tiles go square, triangle, square, triangle, and so on. How "
                    "many squares and how many triangles are there, and which shapes meet at every join?",
                    ["The tiles take turns: square, triangle, square, triangle, ... The first tile is a square.",
                     "Every second tile is a square, so there are 12 ÷ 2 = 6 squares.",
                     "The other tiles are triangles: 12 − 6 = 6 triangles.",
                     "Check the count: 6 + 6 = 12 tiles.",
                     "Look at each join between two neighbours. Every join has a square on one side and a triangle "
                     "on the other.",
                     "So the same two kinds of shape meet at every join: a square and a triangle.",
                     "Check: the tiles never put two squares or two triangles side by side, because they take "
                     "turns."],
                    "6 squares and 6 triangles, because 6 + 6 = 12. At every join a square and a triangle meet, "
                    "the same set each time")],
       ncert=["tp.two_shapes_text"], key_terms=["pattern", "meeting point", "same set", "shapes"],
       misconceptions=["M_SAME_SET"], minutes=5),
     DOER("T3.C2", "Practice: Pattern Tiler", "pattern_tiler", "Apply",
          "Students continue a pattern made of two shapes on a dot grid, and list the shapes that meet at a marked "
          "point.",
          ["Tiles of two shapes can cover a region when they repeat in the same order.",
           "At each meeting point, list the shapes that meet and compare the lists.",
           "If the same set of shapes meets at every point, the pattern goes on in the same way."],
          items=[FIO("tp.two", "Tessellation Patterns: shapes in the pattern",
                     "Here is a tessellating pattern with more than one shape. What shapes have been used in this "
                     "pattern? ___, ___.",
                     ["Look at the shapes that repeat in the pattern.",
                      "One shape has 6 equal sides: a regular hexagon.",
                      "The other shape has 3 equal sides: an equilateral triangle.",
                      "At every meeting point 2 hexagons and 2 triangles come together, in the order hexagon, "
                      "triangle, hexagon, triangle.",
                      "Check: no other shape appears anywhere in the pattern."],
                     "Regular hexagons and equilateral triangles.",
                     kind="prompt",
                     q_figure="A pattern of regular hexagons and small equilateral triangles that fills a "
                              "rectangle.",
                     s_figure="One meeting point circled, where a hexagon, a triangle, a hexagon and a triangle "
                              "meet."),
                 FIO("tp.cont1", "Tessellation Patterns: continue the hexagon pattern",
                     "Continue the pattern given below and colour it appropriately.",
                     ["Look at the shapes already drawn: regular hexagons in purple and equilateral triangles in "
                      "yellow.",
                      "The hexagons touch each other only at corners, and a triangle sits on each side of a "
                      "hexagon.",
                      "Add the next hexagon so that it touches the others at corners, and fill the spaces between "
                      "with triangles.",
                      "Colour the hexagons purple and the triangles yellow, as in the start.",
                      "Check: at each meeting point you see 2 hexagons and 2 triangles, the same set every time."],
                     "Sample answer: add hexagons that touch only at corners and fill the spaces with triangles; "
                     "colour hexagons purple and triangles yellow. Your answer may differ.",
                     kind="prompt",
                     q_figure="A dot grid with three regular hexagons and some triangles already drawn.",
                     s_figure="The dot grid with more hexagons in purple and triangles in yellow added in the same "
                              "order."),
                 FIO("tp.oct_sq", "Tessellation Patterns: octagons and squares",
                     "Look at the pattern given below. What shapes are coming together at the marked points? Are "
                     "the same set of shapes coming together at these points? Continue the pattern and colour it "
                     "appropriately.",
                     ["The marked points are the 4 corners of one small square.",
                      "At each marked point, list the shapes that meet: 2 octagons and 1 square.",
                      "Compare the 4 points. Each one has 2 octagons and 1 square, so the same set of shapes comes "
                      "together at every point.",
                      "Continue the pattern: put more octagons edge to edge, and a small square wherever four "
                      "octagons meet.",
                      "Colour the octagons green and the small squares blue, as in the start.",
                      "Check: 2 octagons and 1 square fill the space round a point with no gap and no overlap."],
                     "Sample answer: 2 octagons and 1 square meet at each marked point, the same set every time. "
                     "Continue with octagons and small squares in the same order. Your answer may differ.",
                     kind="prompt",
                     q_figure="Four rows of four regular octagons with a small square between each group of four "
                              "octagons, and four points marked round one small square.",
                     s_figure="The same pattern with a marked point labelled: 2 octagons and 1 square meet there."),
                 FIO("tp.sq_tri_eq", "Tessellation Patterns: are the triangles equilateral",
                     "Here is a tiling pattern made using two different shapes, squares and triangles. Are the "
                     "triangles equilateral? Why or why not?",
                     ["An equilateral triangle has all 3 sides equal. Compare the sides of one triangle by counting "
                      "along the dots.",
                      "Two sides of the triangle are as long as a side of a square, a little more than 2 grid "
                      "steps.",
                      "The third side is shorter. It is exactly 2 grid steps.",
                      "So two sides are equal and the third side is not.",
                      "Check: for an equilateral triangle all 3 sides must be equal, and here the third side is "
                      "shorter."],
                     "No. Two sides of each triangle are as long as a side of a square, and the third side is "
                     "shorter, so the triangles are not equilateral.",
                     kind="prompt",
                     q_figure="On a dot grid, three tilted squares and two triangles joined at their corners.",
                     s_figure="One triangle with its two longer sides marked equal and its shorter side marked "
                              "different."),
                 FIO("tp.sq_tri_pts", "Tessellation Patterns: squares and triangles",
                     "What shapes are coming together at the marked points? Are the same set of shapes coming "
                     "together at these points? Continue the pattern and colour it appropriately.",
                     ["Look at one marked point and name every shape that has a corner there.",
                      "Continue the pattern round the point until no space is left. At the point 2 squares and 3 "
                      "triangles come together.",
                      "Do the same at each of the 5 marked points. Each one has 2 squares and 3 triangles, so the "
                      "same set of shapes comes together at every point.",
                      "Continue the pattern with squares and triangles in the same order, and colour the squares "
                      "purple and the triangles orange, as in the start.",
                      "Check: 2 squares and 3 triangles fill the space round a point with no gap and no overlap."],
                     "Sample answer: 2 squares and 3 triangles meet at every marked point, the same set each time. "
                     "Continue the pattern the same way and colour it. Your answer may differ.",
                     kind="prompt",
                     q_figure="On a dot grid, three tilted squares and two triangles joined at their corners, with "
                              "five points marked.",
                     s_figure="One marked point with the shapes that meet there: 2 squares and 3 triangles."),
                 FIO("tp.create", "Tessellation Patterns: create your own",
                     "Create similar patterns using other cutouts of shapes.",
                     ["Pick two shapes that fit around a point, for example a square and an equilateral triangle "
                      "with sides of the same length.",
                      "Make a row of squares. Above it make a row of triangles, one pointing up, the next pointing "
                      "down, and so on.",
                      "Above the triangles make a row of squares again, moved half a square along, and go on in "
                      "the same order.",
                      "At each point, list the shapes that meet: here 2 squares and 3 triangles.",
                      "Check: the same set of shapes meets at every point, with no gap and no overlap."],
                     "Sample answer: rows of squares and rows of equilateral triangles, one after the other. At "
                     "every point 2 squares and 3 triangles meet. Your answer may differ.",
                     kind="prompt")],
          misconceptions=["M_SAME_SET"])],
    key_terms=["pattern", "shapes", "meeting point"]))
