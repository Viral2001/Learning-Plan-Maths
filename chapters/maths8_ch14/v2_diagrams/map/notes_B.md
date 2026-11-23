# Chunk B notes (Class 8 Ch 14 "Area", topics M1.S8.T8 to M2.S15.T15)

Result: 29 items (7 worked examples, 11 questions, 11 solutions): required 23, optional 2, none 4. Inventory: 28 entries (21 map to items, 3 to concept images, 4 to none). Validator: errors 0, warnings 2 (C47 and C49 solution diagrams are not printed in the book, which the validator allows).

Output file: map/out_B.json (built by a script kept outside the chapter folder).

## 1. Judgement calls

**Worked examples (7, all required).** Each shows ONLY what the example gives (question side, token after the question text): C30 rectangle 8 by 6 with both diagonals meeting at O; C31 line l, base BC = 6, distance 4 and three tops on l; C32 line l, B and C 3 cm below, BC = 8, A on l (A is drawn off-centre on purpose, so the answer position is not given away); C41 quadrilateral ABCD with BD = 10 and heights 4 and 3; C42 house-shaped pentagon; C50 parallelogram base 9, height 5; C51 parallelogram 10 by 6 with height 4.8. Vertex letters are drawn only where the LP text uses them (C41 has ABCD; C30, C42, C50, C51 have none, so none are drawn). The kept teaching images of the same figures are not linked (user decision 5).

**Question side.** Required for every question whose book figure is given (C34, C36, C38, C39, C40, C44, C46, C48, C53). C47 (hexagon measurements) and C49 (half-area quadrilateral) have no figure in the book, so the question side is `none` (`OPEN_ENDED` + `TEXT_SUFFICIENT`).

**Solution side.** I made a solution `required` only when it adds a construction, an arrangement, a new line/point or a highlight that carries meaning:
- C38 (adds the midpoint M where DH crosses AB and the lengths s, s/2, 2s and areas s², s²/4 that the steps rely on),
- C39 (adds the median NY and shades the final triangle XMN, marked 1/4),
- C40 (the traced answer itself: reflected tank, straight line, best point, walk),
- C47 (centre joined to the six corners, one triangle with its base and height marked; the question has no figure, so this solution figure stands alone with `derived_from` null),
- C48 (the vertical through the shared point with h1, h2 and the labels L, W),
- C49 (the construction itself: four midpoints joined; sample quadrilateral, `needs_lp_text_sync: true` because the LP names no concrete quadrilateral),
- C54 (the answer picks out (g) as largest and (a) as smallest perimeter: outlined and tagged, HIGHLIGHT_MEANING).
`none`: C35 and C37 (area written two ways on base-height pairs that are already in the question figure, then arithmetic). `optional`: C45 and C46 (the figure with the pieces marked 33 + 33, or 30, 40 and 110, would help; text is complete).

**Colours.** The question speaks of a "red region" and "blue region" (C38). The style table has no red, so red is drawn with the palette vermilion #D55E00 (the WRONG value, used here only as the colour name of the question's red region) and blue with SET_A. This is stated in the item's `render_note`.

**Orientation.** C41 draws BD horizontal (the book's quadrilateral has no numbers and a different slant); C44, C34, C36, C46, C48, C53 follow the book's orientation.

**Teaching figures with no item in this chunk.** P08-shape-3, P08-shape-4, P09-shape-2, P10-shape-1 are proof or teaching steps whose reasoning is carried in words in the LP: mapped `none:TEXT_SUFFICIENT`. P10-shape-3 (B, A, C' in a straight line), P14-dissection-2 and P15-shape-2 are covered by the teaching images of C32, C50 and C51: mapped `concept_image:...` (accounting only). P10-shape-2 (A on l, lower triangle ABC) is the set-up the C32 diagram draws, so it maps to that item. P12-shape-4 (book's plain pentagon) maps to C42 even though the LP uses its own house-shaped pentagon (see section 2).

**C53 grid.** The book's seven parallelograms are not on whole-number slants. I measured them from the page picture (grid 34 x 12, base 5, height 3; shifts of the top side relative to the bottom side: a +0.3, b +1.1, c +2.5, d -0.6, e -1.0, f -2.0, g -2.8; bottom-left x: a 1, b 9, c 18, d 28, e 4, f 14, g 25; row one bottom y = 8, row two bottom y = 2 counting up from the lower grid edge). With these, perimeters are a 16.03 (smallest) up to g 18.21 (largest), which agrees with the LP answer. Letters (a) to (g) are drawn because both the question and the answer text refer to them (user decision 3).

**Book mistakes (decision 1).** I checked every length that is printed or can be recomputed on the pages of this chunk (p.8 Find BY: 3, 5, 4 fit a real triangle; p.11 Q2: 4, 6, 8 fit a 30-60-90 triangle and give BY = 3; p.13 Q1 and Q2). No print slip found, so nothing was corrected.

## 2. LP text issues (not edited, listed only)

- **All singles C38, C39, C40, C46, C47, C48, C49:** the block's `item.book_number` says "Figure it Out, Q1" for every one; the concept names say Q6, Q7, Q8, Q2, Q3, Q4, Q5. Suggested book numbers: "Figure it Out (Triangles), Q6", "... Q7", "... Q8", "Figure it Out (Area of any Polygon), Q2", "... Q3", "... Q4", "... Q5" (I used these in `lp_book_number`).
- **Same seven singles:** the block holds only the sentence "Work through the practice problem. Read the question in the book ..." and has no `question_tex` or `steps_tex`; the real question and steps sit in the Practice blocks of the teaching concepts M1.S8.T8.C33 (blocks 0 to 2) and M2.S11.T11.C43 (blocks 0 to 3). The builder must put the question token and the solution token where the question and steps really are (or the question and steps must be moved into the singles).
- **M2.S13.T13.C46 (and its Practice block):** the text does not say that E is on AB and F is on AD. Suggested sentence: "E is a point on AB and F is a point on AD."
- **M1.S9.T9.C36 / C37:** the text does not say that X lies on BC extended, to the left of B (the figure shows it outside BC). Suggested sentence: "X is the foot of the height from A, on the line BC extended beyond B."
- **M2.S15.T15.C53 / C54:** "all on equal bases between the same two grid lines" is not what the figure shows (row one lies between grid lines 1 and 4, row two between 7 and 10; each parallelogram spans two lines 3 squares apart). Suggested sentence: "all with the same base (5 squares) and the same height (3 squares)."
- **M2.S11.T11.C42:** the LP pentagon (6 by 4 rectangle plus a triangle of height 3) is not the book's pentagon (a plain unlabelled pentagon), and the apex position along the 6 cm side is not given (it does not change the area). Suggested sentence: "... with a triangle of height 3 cm on its 6 cm side, the apex above the middle of that side."
- **M2.S11.T11.C41:** the numbers BD = 10, 4 and 3 are the LP's own (the book figure carries none). Fine for a worked example; noted only because the book picture is unlabelled.
- **M2.S13.T13.C49 (solution):** the text speaks of "the four corners" and "each pair of diagonal triangles" without a concrete quadrilateral; the solution figure uses a sample one (hence `needs_lp_text_sync: true`). Suggested opening: "Take any quadrilateral. Mark the midpoints of its four sides and join them in order."
- **M2.S13.T13.C47 video anchor:** it says "the book's regular hexagon with its centre joined to the six corners", but the book has no figure for this question (p.13 Q3 is text only).

## 3. Borderline (rules applied as written)

- **C30, C41, C42, C50, C51 worked examples:** a careful student could read the numbers from the text, but each is a geometry example whose point is the shape (diagonals, a height on the opposite side of a diagonal, composite pentagon, cut-and-slide, any base). Kept `required` (decisions 4 and 5).
- **C35, C37 solutions `none`:** the solution only adds the value of BY on a figure that already has both heights.
- **C45, C46 solutions `optional`:** rule D (marking piece areas on the given figure). If the user prefers area labels on the pieces, these two would be `required` with `derived_from` the question figure.
- **C38 solution `required` versus C46 solution `optional`:** C38 adds a point and symbolic lengths that the steps need to be understood (DH meets AB at its midpoint); C46 only restates areas of pieces that are already visible.
- **C54 solution `required`:** it would also be defensible as `optional` (the letters already name (g) and (a)); chosen `required` because the answer is a selection among drawn figures (circled smallest / boxed largest).
- **C47 and C49 solutions `required`:** the answer is a construction described only in words (B2: "answer is a construction"), even though the question side has no figure.

## 4. Places where the book itself is unclear

- p.15 Q1 figure: the slants are not whole squares and no numbers are printed; the values above are measured.
- p.12 Q8 map: no scale and no numbers; positions are measured from the page. The reflection in the solution is taken in the near (lower) bank.
- p.8: the altitude AX has no right-angle mark in the picture; one is added because AX is the height to BC.
- p.13 Q3 (hexagon) and Q5 (half-area quadrilateral) have no figure at all; the solution figures are the constructions the LP steps describe.
