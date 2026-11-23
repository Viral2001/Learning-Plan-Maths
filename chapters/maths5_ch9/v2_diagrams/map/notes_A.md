# Chunk A notes: Class 5 Ch 9 "Coconut Farm" (topics M1.S2.T2 to M1.S8.T8, book pages 1 to 4)

Result: 30 items = 10 required, 1 optional, 19 none. Validator: `errors 0, warnings 0`.
Required: C6/C7 (Example 1 array question + answer picture), C10/C11 (4 x 8 array, empty count boxes then filled), C12/C13 (x puzzles), C14/C15 (division puzzles), C31/C32 (hexagon puzzle). Everything else is text/LaTeX.

## Figures claimed (14 inventory entries)

- Base figures claimed: P01-array-1 (C6 question), P01-array-2 and P01-array-3 (C7 solution, they are the printed answer picture), P01-array-4 (C10 question), P01-labelled_equation-1 (none: TEXT_SUFFICIENT, the "Division Facts / Notice!" teaching box; it is not a figure of any question), P02-triangle_puzzle-1 (C12 question), P02-triangle_puzzle-2 (C14 question), P02-answer_boxes-1 (none: LATEX_ARITHMETIC, four answer areas for equations), P03-equation_boxes-1 (none: LATEX_ARITHMETIC), P04-hexagon_puzzle-1 (C31 question).
- Second uses (NEW- ids, same book figure drawn again in a solution): NEW-P01-array-4-sol (C11), NEW-P02-triangle_puzzle-1-sol (C13), NEW-P02-triangle_puzzle-2-sol (C15), NEW-P04-hexagon_puzzle-1-sol (C32).
- NOT claimed on purpose: P03-equation_boxes-2, P03-place_value_table-1 and P03-place_value_table-2. They sit in the book section "Patterns in Division and Place Value" (same name as my topic M1.S7.T7), but none of my units uses them: my worked examples C18/C19 use practice values (270, 2700, 70, 700, 7000, 3500) and the figures are the questions of M1.S9.T9 (chunk B). If chunk B does not claim them the merge check will show it.
- All base descriptions I checked against the page pictures (pages 1 to 4) are right. The inventory note on P02-triangle_puzzle-2 ("the 56 circle of puzzle 6 looks slightly grey") is the NCERT watermark crossing the circle, not a different figure.
- The base inventory letters the hexagon boxes differently (D+E=F, A-G=D, C x H=F) from the LP steps (A / B = C, A - D = F, C x E = H, F + G = H), but the structure is the same: top row a / b = c, left column top - middle = bottom, right column top x middle = bottom, bottom row + = .

## Borderline (v3 rules applied as written, user decision 4)

1. **C3 worked example (27 coconuts, 3 rows of 9): optional (not added).** No v3 trigger: the example describes its own array in words (3 rows of 9), nothing is referenced in a figure, the answer is equations; the book prints no picture for it (practice values). The array with its 9 columns and 3 rows outlined would help, and the kept teaching image of this concept already shows exactly that; that image was NOT the reason, the tie-breaker was (a careful student can do it from the text). If the user wants it drawn, it would be the C7-style picture for 3 x 9 (27 coconuts: 9 column groups of 3 and 3 row groups of 9).
2. **C4 worked example (names of dividend, divisor, quotient of 45 / 5 = 9): none.** A labelled equation (arrows to Dividend, Divisor, Quotient) can be written in LaTeX (underbrace); the book's box is a teaching figure. Borderline because the answer is "labels on an equation".
3. **C19 worked example (70, 700, 7000 / 10 on a place value chart): none (HEADER_BOXES_ONLY, LATEX_TABLE).** v3 "not a diagram" list names place value header boxes with digits. The concept image C19.IMG1 stays untouched. If the user wants a chart anyway: Problem | H | T | O rows 70 / 10 = 7, 700 / 10 = 70, 7000 / 10 = 700.
4. **C11 solution (4 x 8 array) is required but only fills the two count boxes and adds the caption 4 x 8 = 32.** The book prints no answer picture here (its answer box is blank lines), so I did not draw the two regroupings as for C7; the LP steps describe the same column and row groups, so a reader could ask for the C7-style picture too (sibling consistency). My reason: the C7 picture is required because the BOOK's printed answer is that picture (B2); C11 has no printed answer picture.
5. **C21 (nine division problems with three red hints)** none: the LP question text already lists all nine problems and the hints; the boxes' positions and arrows carry no meaning (NUMBER_LIST_IN_BOXES idea, coded LATEX_ARITHMETIC).
6. **C13 and C15 sample answers.** The puzzles have many correct answers; I drew exactly the LP's sample answer (C13: 36x2=72, 6x10, 6x8, 4x9, 3x8, 5x8; C15: 108/2, 84/2, 112/2, 54/6, 42/7, 56/8). Nothing in the picture says "sample"; the LP text does ("Sample answer ... Your answer may differ").
7. **C32 solution draws BOTH answers** (two boards side by side), because the LP answer is "yes, two answers" and the question asks "Is there more than one answer?". The LP's own s_figure hint mentions only the first. I verified by brute force over all 8! placements that exactly these two arrangements satisfy A/B=C, A-D=F, C x E=H, F+G=H.
8. **Questions with only words** (C8, C23, C25, C27, C29, C33 and all their answers): none, no figure in the book (the 35 / 1 bubble on p.1 shows a character only).
9. **Layout of the puzzle cards.** The book prints six puzzles in one row; on the 16:9 card they are drawn in two rows of three (reading order unchanged: 72, 60, 48 / 36, 24, 40 and 54, 42, 56 / three with 54, 42, 56 in the left circle). The book colours every puzzle differently (decorative); all use CELL_FILL. The book's puzzle body is a trapezoid, the LP calls them triangles; I drew the book's shape.

## LP text issues (nothing was edited, decisions unchanged)

- **M1.S2.T2.C3, C4, M1.S7.T7.C18, C19 (worked examples):** every question ends with "(practice values)", which reads like an authoring note. Suggested: delete the phrase.
- **M1.S5.T5.C14 / C15 (÷ puzzles), question text:** the order of the circles is not stated. The solution (108 / 2 = 54, 54 / 6 = 9) only works with "left circle ÷ right circle = square". Suggested sentence after "This row has the sign ÷.": "In every triangle, the first (left) circle divided by the second (right) circle gives the number in the square."
- **M1.S5.T5.C12 / C14:** the text calls the shapes "triangles" but the book draws them as a small square on top of a trapezoid with two circles; suggested: "puzzle" or "triangle puzzle" with "square" and "circles" as named.
- **M1.S8.T8.C32 (hexagon solution):** the steps use box names A to H ("A ÷ B = C", "A - D = F", "C x E = H", "F + G = H") but the question does not show those letters, and I do not draw letters in the figure (they are not lettered figures). Suggested sentence at the start of step 1: "Call the top boxes A, B, C from left to right, the two middle boxes D (left) and E (right), and the bottom boxes F, G, H from left to right."
- **M1.S8.T8.C31 (hexagon question):** the text says only "the following boxes"; the figure carries which boxes are joined by which sign. Suggested sentence: "Eight boxes are joined by signs: top row ÷ and =, bottom row + and =, a − under the first top box and a × under the last top box, and the two middle boxes each end a column sum."
- **Old card markers:** the `text` fields of C13, C15, C22, C32, C34 carry "[Image: ... solution]" lines in the middle of the steps and "[Image: ... solution (continued)]" after the answer (two old cards each). For C13, C15, C32 the new token goes before step 1 and these markers must go; C22 and C34 have no diagram (their two old cards are dropped), so their markers must go too.
- **M1.S8.T8.C16/C17:** the book question has (a) 30 x 30 with two division statements; the LP answer gives one statement for (a) (900 / 30 = 30) because both numbers are 30; fine, but the LP question does not say that the two statements can coincide. Optional hint, no change needed.
- All arithmetic of the chunk was rechecked (e.g. 150/3 = 50, 4200/100 = 42, 5500/5 = 1100, 5500/10 = 550, 10 x 1100 = 11000, 1800/18 = 100, 6100/10 = 610): no error found.

## Book issues

- No print slip found in pages 1 to 4 (no wrong digit or missing sign), so nothing was corrected.
- The book's page 4 question 4 has no printed answer and the pdf has no solutions section; the two answers come from the LP and were checked by brute force.
- Page 1: the book's third array (4 rows x 8 columns) is the figure of the question "Write the appropriate multiplication fact ..."; its two empty boxes are meant for the counts (8 above, 4 beside). The lilac box of three blank lines is an answer area and is not drawn.

## Notes for the builder

- Question diagrams never contain the answer (C10 boxes empty; C12 and C14 circles empty except what the book prints; C31 boxes empty).
- Colours: given content INK; everything the solution adds is ANSWER (group outlines, captions, filled numbers).
- All figures are 16:9 cards (1920 x 1080 px coordinates are in the specs). Coconuts are plain circles (CELL_FILL, INK outline), the book's brown coconut art is decorative.
