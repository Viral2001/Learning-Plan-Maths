# Notes for chunk B (Class 5 Ch 11 "Grandmother's Quilt", plan cbse_eng_maths5_ch11_v4)

Chunk B = topics M1.S9.T9 (Comparing Shapes), M1.S10.T10 (Let Us Do, square grid), M2.S11.T11 (worked examples, area and perimeter differ),
M2.S12.T12 (Let Us Do: mats, same area, a less than b), M2.S13.T13 (Trisha), M2.S14.T14 (Let Us Explore), M2.S15.T15 (formulas).
18 units, 31 items: **required 23 / optional 3 / none 5** (question 12/0/1, solution 8/3/2, worked example 3/0/2). Validator: errors 0, 2 warnings
(C45 and C46 have no book figure, as expected). Output: `map/out_B.json`. No book pdf solutions exist; the LP solution text was the answer in every case.

Method: every book figure of pages 3 to 10 was checked square by square against the page pictures (page_03 to page_10). All base-inventory descriptions of my figures
were correct (grid sizes, cells, labels); no "CORRECTED" entry was needed. All areas, perimeters and counts used in the specs were recomputed from cell lists by script
(LUE shapes, the 18-square shapes, mats, Trisha, the triangle's 6 whole + 6 half squares, the 16/20/34 and 25/21/9 examples): every value agrees with the LP solution.

## 1. Judgement calls

- **One diagram per item, identical specs.** The plain rectangles A, B, C (page 3) are the question figure of C31, C33 and C35 (identical spec, `render_note` says "same as"). Q4 (C37) gets the book's grid
  figure with the key. Solutions of Q1 (C32) and Q3 (C36) draw the grid over the rectangles and add counts; same layout as the grid of Q4.
- **T9 solutions.** C32 and C36 required: the question figure has no grid, and "how will you find out" is answered by putting the rectangles on a square grid and counting
  (arrangement answer, B2). C34 required: the answer is "B laid on A and B laid on C" (an overlay arrangement); its layout is two overlay panels, so it is not the same row as the question
  figure (`derived_from` is set, `render_note` explains). C38 optional (not added): the grid is already in the question figure and only the counts 12, 8, 10 would be added (Step D).
- **C36:** all three rectangles stay in place (same layout), but only A (12) and C (10) get a count, because the LP solution compares only those two.
- **C35 question:** the question names A and C only, but the book prints the three rectangles together, so the figure shows all three (identical to C31).
- **C37 key:** the book's key under the grid ("1 unit" with a unit square, "Area = 1 unit square") is part of the printed figure and is kept in the question figure. The solutions of C32/C36 add a short key "1 unit square".
- **C39 gardens:** the book hides most grid lines inside the green gardens; the grid is drawn over them so that the squares can be counted (the question says "on the square grid"). The pale strip is drawn as a pale column of the grid (CELL_FILL).
- **C40 optional** (same reasoning as C38: grid and gardens are in the question figure, the solution only numbers squares / adds 10 and 12).
- **C41 palm:** question required (the text says "the square grid given below" and the learner acts on it): an empty 15 x 18 grid with "1 cm". C42 none (the answer is the learner's own palm; the LP gives
  only practice counts and no outline, so a traced palm would be invented: `OPEN_ENDED` + `NOT_RENDERABLE`). C43 (leaves) question none: the book prints no figure of its own for it (its grid is the one under the previous question).
  C44 none.
- **T11 worked examples C45, C46 required; T15 C60 required, C61 and C62 none.** See Borderline. They get their own diagram although a teaching image exists in the concept (decision 5). Media ids are IMG2 because IMG1 is the kept teaching image.
  The worked-example diagram shows only what the question gives (side lengths of the rectangles / 5 rows of 8 patches and the 1 cm patch); no areas or perimeters.
- **C48 / C49 mats:** the book's outlines are 4 to 9 px bigger than a whole number of patches (outline stroke); the exact 5 x 2 and 4 x 3 patch multiples are drawn (they agree with the LP solution). (a) and (b) are drawn because the LP answer speaks of "mat (a)" and "mat (b)" (decision 3).
  The solution adds the remaining patches (ANSWER lines) and the counts 5, 2, 4, 3.
- **C50 / C51:** letter "(a)" of the book is not drawn (the LP answer says only "the given shape"; decision 3). The "1 cm" label is kept at the top-right square as in the book. The LP's "18 by 1" strip is drawn upright (1 column x 18 rows) because the grid is only 15 columns wide
  (see LP text issues). Perimeter tags: 22 cm (given shape), 18 cm (6 by 3), 38 cm (strip), 18 cm (4 by 4 block with 2 squares).
- **C52 / C53:** letters (a) and (b) are drawn (the LP answer refers to them). The book's hand-jagged slanted sides are drawn straight through the grid corners (6,3)-(9,6) and (12,3)-(9,6). The solution marks the triangle's 6 whole squares with filled dots and the 6 half squares with rings, with a key
  ("6 whole squares", "6 half squares") and the tag "9 unit squares" under (a). The sampled count agrees with the LP: row 4 has 4 whole, row 5 has 2, row 6 has 0; 2 half squares in each of rows 4 to 6.
- **C54 Trisha:** the figure has no text (the book prints no label). The book's right rectangle is cut into only 6 pieces; it is drawn as 3 x 4 whole unit squares (the size the LP solution uses). C55 optional: the solution only adds area and perimeter numbers (all in the text).
- **C56 / C57 (Let Us Explore 1):** the book prints the six shapes in two stacked grid blocks (end of page 6, top of page 7). The LP has one question with one diagram, so the blocks are joined into one 14 x 15 grid (second block shifted down 6 rows), shapes at their book positions. P06-grid-3 and P07-grid-1 both map to C56.
  Shape (e) is 8 squares in the book (not 12) and is the odd one out, not a print slip. The solution ticks (a), (b), (c), (d), (f) and writes area and perimeter beside every shape (including (e), whose numbers are in the LP steps).
- **C58 / C59 (Let Us Explore 2):** same decisions as C56 / C57. The LP says "Tick these" for both groups (12 cm: (a), (b); 16 cm: (c), (d), (e)), so all five shapes get a tick and the perimeter written beside them tells the groups apart.
  Two cells of (c) are darker pink in the book (an artwork effect); drawn in one colour.
- **Colours.** The book's colours (yellow, pink, purple, lime, light green, pink) are decoration; the specs use style tokens: shaded cells MARK_FILL, A SET_B, B MARK_FILL, C CELL_FILL, the two shapes to compare in C52 SET_A / SET_B, the given orange patch SET_B.
- **Figure inventory.** 14 base figures plus 8 `NEW-...` entries: second uses of P03-shape-2 (C33, C35 questions, C34 solution), of P04-grid-1 (C32 and C36 solutions), and the solution figures of C49, C51, C53, C57, C59
  that redraw a book figure with added marks. P10-shape-1 and P10-shape-2 (teaching figures: 6 x 4 rectangle, 5 x 5 square) map to the teaching images of C61 and C62 (those two worked examples are text-only). P09-pattern-2 maps to the C60 worked example (the LP changed its numbers, see below).

## 2. LP text issues (not edited, decision 2)

- **M2.S12.T12.C51**, steps_tex[2] and text: "`$A 6$ by $3$ rectangle has ...`" has the article "A" inside the maths. Suggested: "A $6$ by $3$ rectangle has $6 \times 3 = 18$ squares and perimeter $6 + 3 + 6 + 3 = 18\text{ cm}$."
- **M2.S13.T13.C55**, steps_tex[4] and text: "`$A 1$ by $8$ rectangle ... $A 3$ by $3$ square`" same slip. Suggested: "A $1$ by $8$ rectangle has area $1 \times 8 = 8$ and perimeter $1 + 8 + 1 + 8 = 18$. A $3$ by $3$ square has area $3 \times 3 = 9$ and perimeter $3 + 3 + 3 + 3 = 12$."
- **M2.S12.T12.C51**: the "18 by 1" strip is longer than the grid printed in the book (15 columns wide). Suggested sentence: "A thin strip standing up, $1$ square wide and $18$ squares tall (the grid is only $15$ squares wide), has $18 \times 1 = 18$ squares and perimeter $18 + 1 + 18 + 1 = 38\text{ cm}$."
- **M2.S12.T12.C48** (question): the size of one patch is not given in the book or in the question; the solution (C49 step 1) assumes "$1\text{ cm}$ by $1\text{ cm}$". Suggested sentence in the question: "Each small square patch is $1\text{ cm}$ by $1\text{ cm}$."
- **M1.S10.T10.C43** (question): "Put them on a square grid" gives no grid; the grid (15 x 18 squares of 1 cm) is printed only under the previous question. Suggested: "Put them on the square grid of $1\text{ cm}$ squares above and find their area."
- **M1.S9.T9.C34 steps_tex[1], C36 steps_tex[5], C38 steps_tex[1] and [5]** (and C38 answer_tex): the letter A is written outside the maths ("So A covers more", "count A row by row", "A covers $3$ columns", "Yes. A covers ...") while B and C are in `$...$`; make it `$A$`.
- **M1.S9.T9.C32, C36, C38 answer_tex:** "`$12\text{ unit}$ squares`" splits "unit squares" between maths and text; suggested "$12$ unit squares".
- **M2.S14.T14.C59**: the question "Tick the shapes with the same perimeter" has two groups (12 cm and 16 cm) and the answer ticks all five. Suggested answer sentence: "Tick $(a)$ and $(b)$ (perimeter $12\text{ cm}$) as one pair, and $(c)$, $(d)$, $(e)$ (perimeter $16\text{ cm}$) as another."
- **M2.S15.T15.C60**: the book's own example is 6 rows of 4 patches (24 patches, 6 x 4 cm), the LP example is 5 rows of 8 patches (not an error, a deliberate change); the diagram follows the LP. Likewise the LP's C61 (11 x 4) and C62 (7) replace the book's 6 x 4 and 5 x 5 teaching figures.
- Question texts of C31, C33, C35 carry no data of the rectangles (their proportions live only in the figure), which is why the figure is required. Nothing else was found missing; every LP solution number I recomputed was correct.

## 3. Where the book is unclear

- The book prints no number beside the rectangles A, B, C of page 3; the 3:4, 2:4, 2:5 proportions were measured from the picture (unit about 39.5 px) and agree with the grid picture on page 4.
- The mats of page 6 have no grid and no stated patch size (1 cm is the LP's assumption); the counts 5 x 2 and 4 x 3 come from the patch size.
- Trisha's right rectangle (page 6) is cut into 6 uneven pieces; its size 3 x 4 units was measured, not counted square by square.
- The triangle (b) of page 9 has hand-jagged slanted sides; they pass through grid corners.
- The book's question "Tick the shapes with the same perimeter" (Let Us Explore 2) does not say how many groups to tick.
- The book has no printed solutions section; the LP solutions were followed.
- Book text slip (not used anywhere): "of the size give below" (page 6, should be "given").
- No book picture is wrong (no print slip needing a corrected value, decision 1).

## 4. Borderline

- **C41 question (empty palm grid): required** (`FIG_REFERENCED`, "the square grid given below", the learner acts on it). It could be `none`: a blank grid is a thin figure, and a learner cannot really trace a palm on a screen image.
- **C45, C46, C60 required; C61, C62 none.** In all five the LP text carries every number, so the tie-breaker alone would give `none`. I made C45 (three rectangles of 16 unit squares) and C46 (three rectangles of border 20) required because the example *is* the visual comparison of three shapes,
  and C60 because the book's own example is a picture of patches in rows and the LP's steps count by rows (decisions 4 and 5: not flipped to none only because the text has the numbers). C61 (one rectangle 11 cm by 4 cm) and C62 (one square 7 cm) are one plain labelled shape each: `TEXT_SUFFICIENT`.
  If you want all five alike, either add C61 and C62 (a rectangle labelled 11 cm and 4 cm, a square labelled 7 cm) or drop C45, C46 and C60.
- **C38, C40, C55 optional (not added)** versus C32, C36, C49, C51, C53, C57, C59 required: the first three would only add numbers (counts, areas, perimeters) beside a figure the question already shows; in the required ones the solution adds the grid, the patches, new shapes, marks or ticks.
  C32 and C36 and C38 would look nearly alike; C38 is the odd one because the grid is already in its question figure.
- **C34 required** (overlay of B on A and on C): it is an arrangement answer, but the text states the result completely; drop it if you think words are enough.
- **C42 none, C43 none, C44 none:** open answers of the learner's own palm/leaves; a sample palm outline would be invented.
- **C57 and C59 solutions** carry tags (area, perimeter) beside every shape as well as ticks; the tags could be dropped if only the ticks are wanted.
- **Same figure three times (C31, C33, C35 questions)** and near-identical grid solutions (C32, C36): kept as one diagram per item, as the brief says.
