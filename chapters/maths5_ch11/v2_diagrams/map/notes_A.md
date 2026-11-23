# Chunk A notes - Class 5 Ch 11 "Grandmother's Quilt" (topics M1.S2.T2 to M1.S8.T8)

Result: 15 units, 25 items. Required 21 (8 question, 8 solution, 5 worked example), optional 1, none 3. Validator: errors 0, 5 warnings
(the five worked examples have no book figure to map: their pictures are the LP's own, not printed in the book).
The map is `map/out_A.json`. It was written by a script kept outside the chapter folder.

Decision table (LP order):

| Concept | Role | Decision | Figure |
|---|---|---|---|
| M1.S2.T2.C3 | worked | required (IMG2) | regular pentagon mat, every side 7 cm |
| M1.S3.T3.C5 | question | required | quilt 15 x 10 patches + three lace reels |
| M1.S3.T3.C6 | solution | required | same, border traced, sides 15, 10, 15, 10, green reel boxed |
| M1.S3.T3.C7 | question | required | same as C5 (identical spec) |
| M1.S3.T3.C8 | solution | required | border coloured: long sides red (30), short sides blue (20) |
| M1.S4.T4.C9 | question | required | pentagon (a) 4 cm + hourglass (b) 5 cm |
| M1.S4.T4.C10 | solution | required | every side labelled |
| M1.S5.T5.C11 | worked | required (IMG2) | tray of 12 squares and tray of 6 circles with gaps |
| M1.S5.T5.C12 | worked | required (IMG2) | tray of 24 squares and the same tray of 48 triangles |
| M1.S6.T6.C14 | question | required | rug 15 x 6 patches |
| M1.S6.T6.C15 | solution | required | rug with 15 and 6 marked, one row boxed |
| M1.S6.T6.C16 | question | required | four table tops (1 to 4) |
| M1.S6.T6.C17 | solution | required | four table tops, gaps of Table 2 tinted |
| M1.S6.T6.C18 | question | required | same as C16 (identical spec) |
| M1.S6.T6.C19 | solution | required | four table tops with 5 x 2, 4 x 2, 3 x 4 and 20, 8, 12 |
| M1.S6.T6.C20 | question | none | TEXT_SUFFICIENT |
| M1.S6.T6.C21 | solution | required (stand-alone) | Table 2 alone with gaps tinted |
| M1.S6.T6.C22 | question | required | same as C16 (identical spec) |
| M1.S6.T6.C23 | solution | none | TEXT_SUFFICIENT |
| M1.S6.T6.C24 | question | none | OPEN_ENDED |
| M1.S6.T6.C25 | solution | optional | 6 notebooks on a 60 x 30 table top (not added) |
| M1.S7.T7.C26 | question | required | desk grid 9 x 6 with three tiles |
| M1.S7.T7.C27 | solution | required | desk covered by 6 big squares = 12 red triangles |
| M1.S8.T8.C28 | worked | required (IMG2) | mat P 7 x 2 and mat Q 4 x 4 |
| M1.S8.T8.C29 | worked | required (IMG2) | triangle on a 1 cm grid, 6 whole + 4 half squares |

## 1. Judgement calls

1. **Worked examples (C3, C11, C12, C28, C29) all required.** The LP's steps narrate a drawn arrangement (add the 5 sides of a mat, gaps between circles, rows of squares,
   lay one mat on the other, count whole and half squares), and decision 5 says a teaching image of the same concept is no reason to drop the example's own diagram. They
   take the ids `<concept>.IMG2` because IMG1 of each concept is a kept teaching image. No inventory figure maps to them (the pictures are the LP's, not the book's).
2. **Quilt (C5 to C8).** The 15 columns and 10 rows are not printed in the book; I counted them on the page picture (15 in the yellow row, 10 coloured rows) and they match the
   LP solution (15 + 10 + 15 + 10). The question figure shows only the quilt and the three reels (no side counts). The book colours the rows and adds a pink frill; both are
   decorative, so patches are plain CELL_FILL and the border is the outline of the patch field (the LP counts patch sides; the inventory flagged the rim-or-patches doubt).
   C7 is the same figure as C5 (said in `render_note`). C8 draws the LP's sample answer (30 red + 20 blue); the LP's second split (25 + 25) is not drawn.
3. **Hourglass (C9/C10).** Drawn not to scale, as the book does: with two parallel horizontal sides the crossing sides can never be as short as the horizontal ones, so four
   equal sides cannot be drawn. I picked a squat shape (horizontal sides 360, crossing sides about 469). The crossing point is not a corner. (a) and (b) are drawn because
   the question and the LP answer refer to the shapes by letter (decision 3), although the book picture has no letters.
4. **The four tables.** The book prints "Table 1" to "Table 4"; the check script forbids the word Table in `visible_text`, so each top carries only its digit 1 to 4.
   The tops are drawn in a 2 x 2 layout (reading order 1, 2 / 3, 4) with equal 640 x 280 tops. WRONG (orange) is used for the gaps of Table 2 because the solution shows the
   "does not tile" case. C16, C18, C22 questions get an identical figure (one per item, as the brief says).
5. **C20 question (Do circles tile?) none, C21 solution required.** The question text neither gives nor names Table 2; a careful student answers from the words. The
   solution's own steps start "Look at Table 2", so its figure stands alone (Table 2, gaps tinted, `derived_from` null). If the question text is changed to "Look at Table 2",
   the question would need the Table 2 picture.
6. **C19 solution required, C23 solution none.** C19's steps work out columns x rows and doubling, which the figure shows (5 x 2, 4 x 2, 3 x 4 and 20, 8, 12). C23 only restates
   the three counts with a unit word, so a second picture would repeat C19's.
7. **C25 optional.** The answer is "all four, because every one is a rectangle"; the notebook example is a sample with numbers in the text. The picture that would help:
   a 60 cm by 30 cm table top covered by 6 notebooks of 20 cm by 15 cm, 3 across and 2 down. Not added.
8. **Desk solution (C27).** Only part (b) gets a picture: 6 big squares of 3 x 3, each cut into 2 red triangles. The three loose sample tiles of the question are not
   repeated, because the question's red triangle starts one row below the top edge and cannot belong to a tiling of 3 x 3 squares; keeping it would contradict the
   tiling. Parts (a) (108 green triangles) and (c) (54 blue squares) stay in the text.
9. **Colours named by the question** (lace reels red / green / blue, desk tiles blue / green / red) are explicit hex values in the specs, not style tokens (the token table
   has no red or tile green): lace #D7263D, #2E9E4F, #1F78D1; desk red #D93A3A, green #3DA35D, blue = SET_A. Rug patches yellow #F6D743, red #E8664A.
10. **C29 triangle.** The LP gives only the counts. I used a right-angled triangle with legs of 4 squares: it has exactly 6 whole squares and 4 half squares (area 8 =
    1/2 x 4 x 4). Whole squares MARK_FILL, half squares SET_B, with a two-word key.
11. **Figure claims.** I claim P01-pattern-1, P01-objects-2, P01-shape-3, P01-shape-4, P02-pattern-1, P02-tiling-2 to -5, P03-grid-1 (10 base figures). Every further
    use is a `NEW-<base>-<concept><q|s>` entry, so 37 entries in all, each mapped to a required item. I did NOT claim **P03-shape-2** (rectangles A, B, C) and
    **P04-grid-1** (the same on a grid, with the unit-square key): they are drawn for the questions cmp.largest / cmp.ab_bc / cmp.ac / cmp.grid, which are units of chunk B.
    My units 14 and 15 are the LP's own pictures (mats P and Q, triangle on a grid). If chunk B does not claim them, the merged map will show them as unclaimed.

## Borderline

- **C3, C12, C28 (worked, required).** The text carries every number; only the steps' wording ("add all 5 sides", "4 rows of 6, cut corner to corner", "lay Q on P") points at a
  picture. They are the weakest of the five; if the team wants worked examples drawn only when the text says "drawn / shown", set these three to `none`. C11 (gaps must be
  seen) and C29 ("is drawn on a grid", whole and half squares told apart on the picture) are firmer.
- **C15 (rug solution) and C19 (tables solution) add only count labels** (15 and 6; 5 x 2 etc. and totals). Under Step D ("row totals beside a grid") these are close to
  `optional`; I kept them required because the LP's steps are exactly those counts and the figure ties them to the picture.
- **C10 (all sides labelled)** is also a label-only solution figure; kept required because the question figure labels one side of each shape and the hourglass sides are
  hard to count.
- **C6 (border traced)** required; the border outline is the core idea of the chapter.
- **C20 / C21 / C23 / C25** as in section 1 (5 to 7).
- **Same figure three times (C16, C18, C22).** One figure per item, identical specs; the build can render it once and copy it.

## 2. LP text issues (nothing was edited)

- **M1.S3.T3.C5 and C7 (questions):** the text never says how long one patch side is, yet the solution counts "one unit of lace for each patch side". Suggested sentence: "Each side
  of a patch is 1 unit long."
- **M1.S3.T3.C7 (question):** starts "She decides ..." with no antecedent once the question is shown alone. Suggested: "Grandmother decides to use two different coloured laces for
  the same quilt. How much lace of each kind will be needed to cover the entire border?"
- **M1.S4.T4.C9 (question) / C10 (solution):** the number of sides (5 and 4) exists only in the picture. In C10 step (b) add: "The two lines cross in the middle, but the crossing
  point is not a corner, so this shape has 4 sides."
- **M1.S6.T6.C16, C18, C22 (questions) and C17, C19, C21 (solutions):** they speak of "Table 1", "Table 2", "Table 3", "Table 4" but no text introduces the four tables. Suggested
  sentence for C16: "The picture shows four tables: Table 1, Table 2, Table 3 and Table 4." (The diagram numbers the tops 1 to 4.)
- **M1.S6.T6.C20 (question):** the solution begins "Look at Table 2" but the question does not mention it. Suggested: "Look at Table 2. Do circles tile? Can we use them to cover a region?"
- **M1.S6.T6.C24 (question):** the LP writes "Maths books"; the book says "Maths textbooks" (minor).
- No place where an LP solution contradicts the book: the tile counts (20, 8, 12), rug 15 x 6 = 90, quilt 15 and 10, desk 9 x 6 = 54, red triangle = 9 green triangles were all
  checked against the page pictures and the arithmetic.

## 3. Where the book itself is unclear

- The quilt has no printed numbers; the border could be the edge of the patch field or the outer pink frill (the LP counts patches, so the patch field).
- The hourglass in Let Us Do 1 is drawn with crossing sides about 1.7 times as long as the horizontal ones although all sides are said to be equal; no drawing of that shape can
  have four equal sides (see section 1, item 3). No print slip (wrong digit or count) was found in any figure of this chunk, so decision 1 was not needed.
- The book's question "Do circles tile?" is not tied to Table 2 anywhere on the page; the LP solution ties it.
- The four table tops are about equal in the book but their cells are drawn only roughly square; Table 1's cells (5 x 2) are nearly square, Table 4's rectangles about 3 times as
  wide as tall. My 128 x 140 cells of Table 1 and 213 x 70 of Table 4 keep those proportions.
- The desk figure prints no sizes; the red triangle's legs (3 squares) and the green triangle's (1 square) are read from the grid. The red triangle starts one row below the top edge.
- The book has no printed-solutions section for this chapter, so every answer picture here follows the LP solution text.
