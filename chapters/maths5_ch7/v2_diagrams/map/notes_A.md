# Notes for chunk A (Class 5 Ch 7 "Shapes and Patterns", v4)

Chunk A = M1.S2.T2, M1.S3.T3, M1.S4.T4, M2.S5.T5, M2.S6.T6, M2.S7.T7, M2.S8.T8 (15 units, 25 items).
Result: required 15 (4 question, 10 solution, 1 worked example) / optional 0 / none 10 (6 question, 4 worked example). Validator: errors 0 (5 warnings, all for figures that the book does not print, see 4).

The build script is kept outside the chapter folder (scratchpad `build_A.py`); every weave grid, the 21 x 21 design and every dashed or numbered shape in the specs was read from, or computed against, a 4x render of `eemm107.pdf` (cell colours sampled cell by cell, shapes checked with shapely, overlap regions computed).

## 1. Judgement calls

| Item | Choice | Why |
|---|---|---|
| M1.S3.T3.C6 / C7 (Q2, the 2 over 1 under mat) | Q required, solution required | The question says "this mat": rows 3 to 8 exist only in the picture. The solution figure is the same 8 x 8 mat plus Row labels, a box round Row 1 + Row 2 and "like Row 1 / like Row 2" tags (marks only, `derived_from` the question figure). |
| M1.S3.T3.C8 / C9 (Q3, weave by four rules) | Q none, solution required | The four rules in the text define the whole mat. The book prints the FINISHED mat beside the rules, so that picture is the answer picture (B2 "answer is an arrangement"), not something the learner needs to attempt it. Question figure would give the answer away. |
| M1.S3.T3.C10 / C11 (Q4, two designs) | Q required, solution required | "any of these designs" refers to the two printed designs. Solution figure = the same two designs, rows numbered, the repeating block boxed (6 rows, 4 bands), "same as Row 1" tags. One picture for both designs (the LP has one question, not parts a/b). |
| M1.S4.T4.C12 / C13 (Let Us Try) | Q required, solution required | Q figure = full target design + part-done dot grid; solution = the whole design drawn on the grid (answer colour for the 109 squares the learner adds, 36 given squares unchanged). |
| M2.S5.T5.C15 (worked, rectangles round a point) | required | Same kind of answer as the Find Out parts (shapes round a point), which are all drawn (sibling consistency). New media id is `M2.S5.T5.C15.IMG2` because `IMG1` is the kept teaching image. |
| M2.S6.T6.C17 / C18 (3 pentagons) | Q required, solution required | Q: the given arrangement (book picture). Solution: the same plus a dashed fourth pentagon in WRONG with the overlap shaded. |
| M2.S6.T6.C19 / C20 (octagons) | Q none, solution required | Q: the book prints one sample octagon, no data. Solution: 2 octagons meeting at a point + the square that fills the 90 degree wedge (what the LP steps say). I did NOT draw a dashed third octagon: the LP answer says only "a square fits that gap". |
| M2.S7.T7.C21-C28 (Find Out Q1 to Q4) | Q none x4, solution required x4 | The questions give no figure of their own (learner uses cut-outs). The answer is an arrangement round a point: 6 triangles, 4 squares, 4 squares + a dashed fifth, 3 hexagons. Same decision for all four (sibling consistency). Q1's solution is the book's own "as shown here" picture (hexagon of 6 triangles). |
| M1.S2.T2.C3, C4, M2.S5.T5.C14, M2.S8.T8.C29 (worked) | none | Text carries every datum and the answers are words / counts (tie-breaker). See Borderline. |

Layout and style decisions applied to all weave figures:
- over = MARK_FILL, under = BG (white), with a small "over / under" key at the top-right (a legend is allowed, the book has none). The printed colours (blue, pink, purple, teal) are dropped.
- Two side-by-side over cells of one row are drawn as one bar (vertical line left out) so rows read as strips.
- Weave rows are given as O/U strings in `content.cells_top_to_bottom`; the description repeats them with the run lengths ("2 over, 1 under, ...") so the renderer can check itself.
- Right design of Q4: LP rows "Row 1: 1 over, 3 under" only fit if the LIGHT tile is over, so light = over (MARK_FILL), dark teal = under (BG). Rows of that design are its half-tile bands, as in the LP.
- "Design 1" / "Design 2" headings appear only in the Q4 solution figure (the LP solution names the designs); the question figure has no labels.
- Overlap of a dashed shape (impossible case, WRONG) is shaded in WRONG at 35 percent and the word "overlap" is written (the LP uses that word); the word sits inside the shaded part, or beside it with a leader line when the part is too small.

## 2. Borderline (v3 rules applied as written, nothing flipped because the text has the numbers)

- M1.S2.T2.C4 (worked, shifted rows of a 9-slit mat): none. The LP writes every shifted row slot by slot, so a careful student can follow from text, but a picture of the four rows (kept teaching image shows it) would clearly help. Would be `optional` ("4 rows of 9 cells, Row 4 = Row 1").
- M2.S5.T5.C14 (worked, regular shapes): none. All side lengths are in the text. An optional picture: square 6 cm, rectangle 6 x 4 cm, pentagon 3 cm with sides ticked.
- M2.S8.T8.C29 (worked, border of 12 tiles): none. Optional picture: a row of 12 tiles square, triangle, ... with a dot at each join.
- M1.S2.T2.C3 (worked, describe a 10-slit row in words): none, no picture would be needed at all.
- M1.S3.T3.C8 (Q3 question): none although the book prints a picture next to it (it is the answer picture). If the user prefers to copy the book (question = finished mat, solution = SAME_AS_QUESTION_DIAGRAM), flip C8 to required and C9 to none.
- M1.S3.T3.C7 (Q2 solution) and M1.S3.T3.C11 (Q4 solution): required because they add marks (row labels, copy tags, the repeat box) to the question figure; if the user reads "marks only" as SAME_AS_QUESTION_DIAGRAM these two become none.
- M1.S4.T4.C12 / C13: the print slip and the too-short dot grid are corrected (see 3 and 4).
- M1.S3.T3.C9: draws 16 rows (LP) although the book mat has 17.
- Find Out Q1: the book prints the answer picture right under the question text ("Do you see ... as shown here?"). I treated it as the answer picture (solution), not as a given figure.

## 3. LP text issues (nothing edited)

| Concept | What is wrong or missing | Suggested sentence |
|---|---|---|
| M1.S2.T2.C3, C4; M1.S3.T3.C7 (and C9, C11 steps) | "slits" is used for the places across the mat. In the book a slit is a cut: the 8-column mat has 7 slits. | "A mat is 10 places wide." / "The mat has 8 places across (8 columns)." |
| M1.S3.T3.C6 (Q2 question) | The text never gives the size of the mat (8 columns, 8 rows), which is only in the picture and in the solution. | "The mat is 8 columns wide and has 8 rows." |
| M1.S3.T3.C8 (Q3 question) | The text gives no mat size. The solution assumes 16 rows (4 x 4) and the figure uses 16 columns (the book's mat, which has 17 rows). | "Weave a mat that is 16 columns wide and 16 rows tall." |
| M1.S3.T3.C10 (Q4 question) | "any of these designs" has no description, so text alone says nothing about which designs. | "Look at the two designs: design 1 (purple strips on light blue) and design 2 (teal and light tiles)." |
| M1.S3.T3.C11 (Q4 solution) | Step 1 says "over means the colour of the strip shows on top" but design 2 has no paper colour: the rows only fit if the light tile is over. Rows of design 2 are half-tile bands, which is not said. | "In design 2 a light tile is over and a dark tile is under. A row of design 2 is one half-tile band." |
| M1.S4.T4.C12 / C13 (Let Us Try) | The grid size is not given; the book's dot paper (24 x 17 cells) is too short for the 21-row design. The centre bar (3, 5, 3 yellow squares in the middle three rows) is not mentioned. | "Use grid paper at least 21 squares wide and 21 squares tall." and "In the middle three rows there is a bar of 3, 5 and 3 yellow squares." |
| M2.S5.T5.C15 (worked) | "edge to edge" for rectangles of 6 cm and 4 cm: it does not say that equal edges must meet. | "Turn the rectangles so that equal edges meet: 4 cm against 4 cm and 6 cm against 6 cm." |
| M2.S7.T7.C27 (question_tex) | LaTeX: `$(6$-sided shapes with equal sides)` has the opening bracket inside the maths and the closing one outside. | `regular hexagons ($6$-sided shapes with equal sides)` |
| M2.S5.T5.C14 (worked) | "A regular shape has all its sides equal" follows the book's wording; the usual definition also needs equal angles (the book's rhombus has equal sides but is not regular). | Leave as the book says, or add "and all its angles equal" (the three shapes of this example give the same answer either way). |

## 4. Book unclear or contradicting itself

- Weaving Mats Q3 mat (P02-pattern-2): the printed mat has 16 columns and 17 rows, and a print slip at row 7 column 9 (green where the 4-row rule needs pink). The LP says 16 rows, so the figure draws 16 rows from the four rules; neither the slip nor the 17th row is copied.
- Let Us Try design (P02-pattern-5): row 19 column 11 is printed green. Its mirror (row 3 column 11) is yellow, the centre column alternates yellow on every odd row, and every other row is symmetric, so the figure shows YELLOW there. This is the only change to the printed design.
- Let Us Try dot paper (P02-grid-6): printed 24 x 17 cells; a 21-row design cannot fit. The figure uses a 21 x 21 cell dot grid with the part-done squares in the same top-left positions (they all lie in columns 1 to 21).
- Weaving Mats Q4 right design: the book does not say which tile colour is over; light = over follows the LP rows (see 1).
- Q2 mat: the print has 8 columns and 7 slit lines; the LP calls the 8 places "8 slits" (see 3).
- Find Out hexagon (P03-shape-2): the book draws a hexagon with its 3 diagonals filled purple. The figure draws the 6 triangles with the same outline and numbers them 1 to 6.
- Teaching figures of page 1 (paper folding, weaving a first mat): mapped to `none` (DECORATIVE_ONLY / TEXT_SUFFICIENT); no item of this chunk uses them. They belong to the intro section whose home concept is in this chunk (unit 1 refs `w.make`, `w.describe`), so chunk A claims them.

## 5. Inventory figures NOT claimed by chunk A

- P04-pattern-1 (the hexagon and triangle tessellation, "What shapes have been used in this pattern?") is the given picture of question `tp.two` (chunk B, M2.S9.T9). The LP's `tp.two_shapes_text` ref of C29 points at the same sentence, but the figure belongs to chunk B's question; if chunk B does not claim it, the merged map will flag it.
- P04-grid-2, P05-grid-1, P05-grid-2, P05-shape-3 and all later pages belong to chunks B to E.

## 6. Figures that are printed twice in the plan

Q2 mat, both Q4 designs, the Let Us Try design and its dot grid and the 3 pentagons each appear in a question figure and again in the solution figure. As the brief says, the second use has a `NEW-<base id>-sol` entry in `figure_inventory`.

## 7. Items without a matching base figure (validator warnings, expected)

M2.S5.T5.C15 (worked, rectangles), M2.S6.T6.C20 (2 octagons + square), M2.S7.T7.C24 (4 squares), C26 (4 squares + a dashed fifth), C28 (3 hexagons): the book prints no picture of these arrangements; the figures follow the LP steps.
