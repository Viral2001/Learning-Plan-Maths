# Notes, chunk C (Class 5 Ch 11 "Grandmother's Quilt")

Topics: M2.S16.T16, M2.S17.T17, M2.S18.T18, M2.S19.T19, M2.S20.T20, M3.S21.T21, M3.S22.T22. 15 units, 27 items.
Result: required 13 (5 question, 6 solution, 2 worked example) / optional 0 / none 14. Validator: errors 0, 3 warnings (C65, C77, C87 are
required but their figure is not printed in the book, which the validator says is fine).
Kept teaching images (C76.IMG1, C77.IMG1, C87.IMG1) are untouched and never linked; C77 and C87 therefore use IMG2.

## 1. Judgement calls

- **C64 / C65 (draw two rectangles of perimeter 26 and 18).** Question none (OPEN_ENDED: the book gives no figure). Solution required
  (ANSWER_IS_FIGURE: the task is a drawing). One picture holds the four sample rectangles of the LP (8x5, 10x3 / 6x3, 7x2), to scale,
  side lengths in ANSWER green, letters (a) and (b) shown because the LP answer refers to (a) and (b) (user decision 3). Perimeters are not written.
- **C66 / C67 (classroom floor).** none / none. A sketch of the sample 8 m by 6 m floor would be optional, not added.
- **C68 / C69 (five shapes on the 1 cm grid, book p.11).** Both required. Positions of rectangles, letters and arrows follow the book
  (checked on page 11: grid 15 columns x 22 rows; rectangles (a) c3-8 r2-7, (b) c11-14 r2-8, (c) c3-14 r11-14, (d) c4-6 r17-19, (e) c9-14 r17-21).
  Aspect 15:22 (clearly tall figure). Question keeps the ten blanks '____ cm'; the solution only replaces the blanks by the lengths in
  ANSWER green (LP s_figure). Areas and perimeters stay in the text.
- **C70 / C71 (6 rows of 4 patches, book p.9).** Question required (the shape and the coloured top row and left column exist only in the
  picture). Solution required: it completes the colouring (15 added patches, ANSWER outline) and adds the counts 6 and 4. The words
  'Breadth' and 'Length' are drawn where the book prints them. 24 is not written (the block is fully shaded, text on it would be unreadable).
- **C72 / C73 (square of side 5).** none / none (TEXT_SUFFICIENT, LATEX_ARITHMETIC): "a square whose sides are 5 units long" is complete in words.
- **C74 / C75 (check the earlier examples).** none / none. The seven earlier figures are shown with their own questions; one recap picture
  would repeat them. I checked the LP's numbers against the book pictures: rectangles A, B, C = 3x4, 2x4, 2x5; gardens 2x5 and 4x3; mats 5x2 and 4x3. All agree.
- **C76 worked (lawn 72 square m, length 9 m).** none (TEXT_SUFFICIENT). **C77 worked (20 cm wide, height marked 5 cm and 7 cm).** Required
  (FIG_REFERENCED, DATA_IN_FIGURE: "marked in two parts", and the solution talks about the upper and the lower part). Figure shows only what the
  question gives: 20 cm, the dotted dividing line, 5 cm above it and 7 cm below it; no 12 cm, no area. Id M2.S19.T19.C77.IMG2.
- **C79 / C80 (objects table, book p.12).** none / none, LATEX_TABLE: a plain table with names and blanks. `text_alternative` gives the LaTeX arrays.
- **C81-C84 (field 42x34, garden 64/16).** none for all four, no figure in the book.
- **C85 / C86 (figure 32 cm, 6 cm, 12 cm, book p.12).** Both required. The three dotted lines are drawn as printed (horizontal one from the left edge to the
  right-hand vertical one; verticals at one quarter and three quarters of the width), without numbers. The rectangle is drawn to the marked sizes
  32 : 18 (the printed picture is not to scale). Solution adds one ANSWER arrow 'on the left side, 18 cm' (LP s_figure). The area 576 is not written.
- **C87 worked (L of 5 tiles).** Required (SPATIAL_GEOMETRY): the example counts the outer edges tile by tile and talks about 'the end of the top row' and 'the corner where the
  two arms meet'. Figure: the 5 tiles and one '1' for the side of a tile; the 12 edges are not marked (that would give the answer). Id C87.IMG2.
- **C89 / C90 (book Let Us Play step 3).** The book prints one picture with the '1' on the edges and '=10'. Following the companion rule, the question figure
  has the 4 tiles and a single '1' (the tile side), and the solution figure marks every outer edge and writes '= 10'.
  The single unit label sits above the top edge of the first tile of the top row, so that it is still an outer edge in the solution figure (and in C92).
- **C91 / C92 (book Let Us Play steps 4 and 5).** The LP q_figure says '5 tiles with a die showing 6'. I read it as the 5-tile figure of step 4 plus the die of
  step 5 (6 dots, drawn flat). The solution is the 11-tile figure with the 24 edge labels and '= 24' (die and given tiles unchanged, the 6 added tiles with ANSWER outlines).
- **Label geometry in the tile figures.** Edge labels sit 0.3 tile above or below, and 0.26 tile left or right of their edges, so that labels at inner corners never overlap
  (checked by script: no label box overlaps another label or a tile).

Figure inventory choices
- P10-shape-2 (square 5 cm): none:TEXT_SUFFICIENT, because C72 is none. P10-shape-1 (rectangle 6 cm x 4 cm, perimeter formula) is not mine: it illustrates the
  rectangle perimeter text of T15 (chunk B). If chunk B maps P10-shape-2 to a concept image there will be a duplicate with a different mapped_to at merge: decide there.
- P13-objects-1 (tile pile and die): none:DECORATIVE_ONLY. P13-pattern-2 (die 4 and an L of 4 tiles, 'arrange them as you like'): none:OPEN_ENDED.
- P13-pattern-3 -> C89 question, P13-pattern-4 -> C91 question (tile arrangement), P13-pattern-5 -> C92 solution. A figure that two items draw gets a NEW- entry for the second use
  (NEW-P09-pattern-2-sol, NEW-P11-grid-1-sol, NEW-P12-shape-2-sol, NEW-P13-pattern-3-sol).
- The earlier figures that C74/C75 refer to (P03-shape-2, P04-grid-1, P04-grid-2, P06-shape-1) are not claimed here; they belong to the chunks of their own questions.

## 2. LP text issues

- **M3.S22.T22.C89** question 'Find the perimeter of the tiles.': the tile side is not given in words (only the figure says 1). Suggested: "Each side of a tile is 1. Find the perimeter of the tiles."
- **M3.S22.T22.C91** question: neither the starting figure nor the die is named ("the same figure"). Suggested: "Look at the 5 tiles and the die, which shows 6. Take turns and add tiles to the same figure till the perimeter becomes 24. The one who makes the perimeter 24 wins the game."
  Also the solution (C92) step 1 starts from the 4 tiles of the earlier step, while the question figure shows the 5-tile figure of step 4: either start step 1 from the 5 tiles ("perimeter 12") or let the question say the figure was made in the earlier steps.
- **M2.S17.T17.C72** question says 'sides are 5 units long' but the solution answers in 'square cm' and 'cm'. Suggested: "a square whose sides are $5\text{ cm}$ long" (the book's picture is marked 5 cm).
- **M2.S17.T17.C71** solution: "The length of one side is 6 and the other side is 4, so Area = Length x Breadth = 6 cm x 4 cm" does not say which is which, while the book picture puts 'Breadth' beside the 6-patch side
  and 'Length' under the 4-patch side. Suggested: "The breadth is 6 (6 rows) and the length is 4 (4 patches in a row), so Area = Length x Breadth = 4 cm x 6 cm = 24 square cm."
- **M2.S19.T19.C77** worked example: "Its height is marked in two parts, 5 cm and 7 cm" does not say which part is on top, the solution does ("upper part 20 x 5, lower part 20 x 7"). Suggested: "...in two parts, 5 cm at the top and 7 cm below it."
- **M3.S22.T22.C90** solution counts 3 + 1 + 2 + 2 + 2 = 10 (step 5 includes the right edge of the lower tile); this is right, and it is the edge the book forgot to label (section 4). No change needed.
- **M2.S18.T18.C75** lists seven rectangles; the first Example (6 x 4 = 24 patches) is also an earlier rectangle and is not listed (not wrong, just not covered).

## 3. Borderline

- C71 solution required (adds the filling and the counts) rather than none / SAME_AS_QUESTION_DIAGRAM. The question figure already shows the empty cells, so one could call it repeating.
- C69 solution required (the filled lengths); C86 solution required (only the 18 cm arrow is new).
- C72 / C73 none although the book prints a square picture next to the example (a teaching figure; the words carry everything).
- C74 / C75 none although the question says "go back to the previous examples" (figures live with their own questions).
- C76 none (lawn) against C77 required (side marked in parts): C76 is a plain word problem, C77 refers to a marked figure.
- C87 worked required although the L is described in words: the counting is easier and safer on a picture (tie-breaker); the kept teaching image shows the same tiles but is not linked.
- C65 required even though the learner's own answer will differ; the LP gives a concrete sample, so the figure draws exactly that sample.
- C79 / C80 none: a filled table could also be read as ANSWER_IS_FIGURE, but it is a plain table (LATEX_TABLE).
- C91 question required with the die showing 6: the die roll is random in the real game, but the book (step 5) and the LP q_figure both give it.

## 4. Book unclear or wrong

- **Print slip (corrected in the diagram):** book p.13 step 3 prints '1' on only 9 of the 10 outer edges of the L of 4 tiles (the right edge of the lower-left tile is unlabelled) and then '=10'.
  C90.IMG1 marks all 10. Steps 4 (12 labels, '=12') and 5 (24 labels, '=24') are complete.
- p.9: the picture puts 'Breadth' beside the 6-patch side and 'Length' under the 4-patch side, while the text says "6 is the length of one side and 4 is the length of the non-equal side".
  The formula box (6 cm x 4 cm) is the same product either way; the diagram copies the picture's placement. On p.10 'Length' is the horizontal 6 cm side, the opposite use.
- p.12 Q6: the dotted lines cut the outline into four regions, only 32, 6 and 12 are marked, and the page does not say which regions form 'the figure'. The LP (and the diagram) treat the whole outline as one 32 x 18 rectangle (area 576 square cm).
  The printed picture is not to scale (about 2.2 : 1 against 32 : 18).
- p.11 Q2: positions of the measuring arrows were read from the picture; the inventory says they are approximate by half a cell. The diagram centres each arrow on its row or column line.
- p.10: the text says 'a square whose sides are 5 units long', the picture and the formulas say cm.
