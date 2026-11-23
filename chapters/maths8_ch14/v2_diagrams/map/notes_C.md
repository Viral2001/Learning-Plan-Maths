# Chunk C notes (Class 8 Ch 14 "Area", units 36-51)

Result: 28 items = required 16 / optional 1 / none 11; validator `errors 0`, 4 warnings (solution diagrams of C58, C59, C61, C68 have no printed book figure behind them, which is expected). Figure inventory: 27 entries (25 base figures + 2 second-use entries `NEW-P17-shape-1-sol`, `NEW-P19-shape_on_grid-1-sol`), 22 mapped to items, 2 to the concept image M2.S20.T20.C70.IMG1, 3 to `none:TEXT_SUFFICIENT`.

Required diagrams (16): questions C55, C56, C57, C60, C74, C76; solutions C58, C59, C60, C61, C68, C75; worked examples C63, C64, C71, C72. Solutions of C60 (IMG2) and C75 are `derived_from` their question diagrams. Worked examples take IMG2 because IMG1 is the kept teaching image.

## 1. Judgement calls

- **One combined picture for a multi-part question.** C55 (four parallelograms), C74 (trapeziums ABCD and WXYZ) and C76 (four trapeziums) each get one question diagram, because the LP keeps them as one block/card and the brief allows one question diagram per unit. C55 and C76 are laid out 2 by 2 as in the book.
- **Panel letters.** (i) to (iv) are drawn in C55 and C76 because the LP answer text refers to (i) ... (iv) (user decision 3). C74/C75 draw only vertex letters (the book prints them).
- **Unlabelled sides in C55 (iii) and (iv).** The book prints only one side and the perpendicular to it. Drawn as a parallelogram whose horizontal sides are 5 cm in (iii) (it comes out as a rhombus, as the book's picture nearly is) and 4.5 cm in (iv); both satisfy the printed lengths exactly (distance 4.8 and 4.4 checked). No length is printed on those sides.
- **C56 (QN).** With SR = 12, QM = 6, PS = 7.6 the foot N is only 0.23 cm from S, so N and S almost touch (QN is nearly equal to QS). The book draws N about 0.6 cm from S. I kept the exact geometry and told the renderer to offset the letters N and S.
- **C57 question.** The book prints the rectangle and the parallelogram on the same base under the question as the picture of its hint. Drawn as printed; the lean is set so the slanting side is exactly 4 (horizontal lean 2, height 2*sqrt(3) = 3.464). No height or area is printed.
- **C58, C59, C61, C68 (no figure in the book).** Question side is `none`. The solution diagram uses a chosen triangle/rectangle in drawing units (C58 triangle base 6, height 4; C59 base 8, height 6; C61 l = 4, w = 3; C68 L = 8, W = 3, the video's own check values). Only the letters the LP/video use (l, w, 2l; L, W, L/2, 2W) or the words the LP steps use (base, height, half the height, Method 1/2) are printed; no numbers.
- **C58.** One diagram holds both methods (Method 1 on the left; Method 2 as parallelogram and then rectangle on the right), because one solution diagram per unit is allowed. Method 2 follows the video: half turn about the midpoint of AC, cut along the height AD, slide the left triangle.
- **C59.** Drawn from the video and the LP answer/last step (cut at half the height, turn the two top pieces about D and E, rectangle on the whole base with half the height). See LP text issue 3 below.
- **C60 solution.** The triangle keeps the same canvas position and scale as in the question diagram (left part of the canvas) and the rectangle is added on the right, so the question figure sits left of centre. The moved piece is ADC turned over, placed against ADB along the hypotenuse (LP step 2).
- **C63, C64, C71, C72 (worked examples).** The diagram of a worked example shows the picture the example needs, so C63 shows the finished dissection (rhombus beside the 12 by 4 rectangle) and C72 the finished parallelogram. Areas (48, 30, 40, 54, 108) are never printed. Each gets its own diagram although teaching images exist (decision 5); none is linked. C63 draws the long diagonal horizontal so the rectangle is 12 wide and 4 tall (the book stands the rhombus on a corner).
- **C71.** The height is drawn from B so its foot lies on DC (the book draws it from A to a point F left of D). The sideways lean of 2 cm (A at x = -2) is a drawing choice; BG ends at G with DG = 6 = AB and GC = 4 (shown in ANSWER green, derived in the steps).
- **C72.** Trapezium bottom 11, top 7, lean 2; copy by half turn about the midpoint of the common side; the parallelogram has base 18 on both sides and height 6.
- **C74 question figure.** Drawn as the book prints it: ABCD with M and the solid BM, WXYZ with M, N and dashed WM, XN, on a 20 by 6 grid. The LP question text names M and N only for WXYZ (the ABCD solution introduces BM as a step); I followed the printed picture.
- **C75 solution.** `required`: the pieces (square 16 and triangle 4; triangle 4, rectangle 20, triangle 4) shaded and numbered are the visual part of "break into figures" (ACTION_ON_FIGURE). Totals 20 and 28 stay in the text.
- **C76 (i).** The tilted trapezium is a right trapezium (the 16 ft side is perpendicular to both parallel sides). The book's dashed 16 ft line lies along the bottom side, so it is drawn as a dashed line 0.6 ft inside that side, with the right-angle square at its start. Each panel has its own scale so the four fit one 16:9 card.
- **Figure inventory choices.** P19-shape-2 and P19-shape-3 (trapezium WXYZ teaching figures) map to the concept image C70.IMG1 (accounting only). P20-shape-2 (Approach 1), P21-shape-2 (6-sided figure) and P21-shape-4 (u, v proof) are teaching figures no item of this plan draws: `none:TEXT_SUFFICIENT`. Several base figures can map to one item (e.g. four to C55, three to C72). The solution diagrams of C60 and C75 reuse a book figure, so each has a `NEW-...-sol` entry.
- **Book numbers.** `lp_book_number` is copied from the LP; the correct book numbers are in `ncert_ref`.

## 2. LP text issues

1. **Wrong book numbers.** M2.S16.T16.C55 ... C62 all say "Figure it Out, Q1"; the book numbers are Q2 to Q9 of the parallelogram set (pdf p.16-17). M2.S19.T19.C68 says "Figure it Out, Q1"; it is Q2 of the set after the trapezium section (pdf p.22). Suggested: "Figure it Out (parallelograms), Q2" ... "Q9"; "Figure it Out (rhombus and trapezium), Q2".
2. **M2.S16.T16.C60** (Q7): the question names triangles ADB and ADC but never defines A, B, C, D (the book's figure does). Suggested sentence: "In isosceles triangle ABC, AD is the altitude from A to the base BC (D lies on BC)."
3. **M2.S16.T16.C59** (Q6): step 2 "Drop perpendiculars from these midpoints to the base" and step 3 "Cut off the two small top pieces" do not match the method in the video, the answer and step 4. The video cuts the top triangle by the perpendicular from the apex to the line joining the midpoints and turns its two halves about the midpoints. Suggested step 2: "Drop the perpendicular from the top vertex to the line joining the midpoints; this cuts the small top triangle into two right triangles." (Perpendiculars from the midpoints to the base belong to another method, which gives a rectangle of half the base and the full height.) The diagram follows the video and the answer.
4. **M2.S16.T16.C61** (Q8): the steps speak of "length" and "width"; the diagram prints l, w and 2l (as in the video). Suggested: "Cut the rectangle (length l, width w) along a diagonal ..." and "base 2l, height w".
5. **M2.S20.T20.C71**: "Use Approach 2" is the book's label and the steps use G, ABGD and BGC without saying where G is. Suggested sentence: "Draw BG parallel to AD, meeting DC at G; the trapezium is the parallelogram ABGD plus the triangle BGC."
6. **M2.S21.T21.C74** (question concept): (a) the book's grid figure holds a third trapezium, the isosceles SPQR (ST = 2, TU = 6, UR = 2 squares, so PQ = 6, SR = 10, height 3), which the LP leaves out. Suggested extra question text: "Trapezium SPQR on the grid has PQ = 6 units, SR = 10 units and height 3 units, with ST = 2 and UR = 2." and solution: "Rectangle PQUT: 6 x 3 = 18. Each end triangle: 1/2 x 2 x 3 = 3. Total 18 + 3 + 3 = 24, and 1/2 x 3 x (6 + 10) = 24." (b) the text does not say that M and N are the feet of the perpendiculars from W and X to ZY; suggested: "where M and N are the feet of the perpendiculars from W and X to ZY." (c) for ABCD the text does not mention M, which the printed figure shows and the solution uses.
7. **M2.S16.T16.C55**: the book figure (ii) also carries a diagonal that plays no part; harmless, but the text could say "(ii) base 5 cm, height 3 cm (the diagonal drawn is not needed)".
8. **M2.S20.T20.C72**: "Use two copies" does not say how; suggested: "Join the trapezium to a copy of itself turned by a half turn along a slanted side, to make a parallelogram."

No solution contradicts the book's figures; all LP arithmetic was rechecked (28, 15, 24, 8.8; QN = 72 / 7.6 = 9.47; 150; 48; 30; 40; 54; 20 and 28; 136, 420, 100, 120).

## 3. Borderline (decisions applied as written; flip if you disagree)

- C55 question, C56 question, C74 question, C76 question: `required` although the LP text carries the numbers (the book question refers to printed figures).
- C57 question `required` (the book prints the same-base figure with the hint) while C57 solution is `none` (it only states "height < 4", which the question figure already shows).
- C62 solution `optional` (a picture of the triangle beside the square with its height marked would help; the three text steps are complete; the question has no book figure). C62 question `none`.
- C58, C59, C61, C68 solutions `required` (ANSWER_IS_FIGURE: the answer is a dissection or construction described only in words); their question sides are `none` because the book gives no figure.
- C60 solution `required` (arrangement of two triangles into a rectangle).
- C63 and C64 worked examples `required` (the dissection of a rhombus and the split into two triangles are spatial, and the book draws both).
- C71 and C72 worked examples `required` (the construction BG and the two-copy parallelogram are the point of the example).
- C75 solution `required` (shaded pieces with areas); C55, C56, C77 solutions `none`.

## 4. Where the book itself is unclear

- The squared-grid figure on p.19 prints no numbers; all side lengths are counted from the grid (checked on an enlarged picture).
- Q2 (iii) and (iv): the other side length is not printed and the printed picture is not exact (the book's (iii) is almost a rhombus with a smaller lean than 5 and 4.8 allow).
- Q3: the printed N is a little farther from S than the exact geometry allows (see judgement calls).
- FiO5 Q3 (i): the dashed 16 ft line nearly coincides with the bottom side, so the figure is a right trapezium; no right-angle mark is printed at the bottom vertex.
- This PDF has no printed solutions; for Q5, Q6, Q8 and FiO5 Q2 the methods come from the LP steps and the videos.
