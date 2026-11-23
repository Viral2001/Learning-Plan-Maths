# Class 5 Ch 9 Coconut Farm - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths5_ch9` v4 (taken from staging). Result: new V2 version v5 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (160 items from 90 units)
{"worked_example": {"optional": 4, "none": 16}, "question": {"required": 12, "none": 58}, "solution": {"required": 12, "none": 56, "optional": 2}}

Optional, NOT added: [('C3', 'worked_example'), ('C93', 'worked_example'), ('C94', 'worked_example'), ('C123', 'worked_example'), ('C142', 'solution'), ('C146', 'solution')]

needs_lp_text_sync: []

## The 24 diagrams
| id | side | type |
|---|---|---|
| M1.S3.T3.C6.IMG1 | question | dot_array |
| M1.S3.T3.C7.IMG1 | solution | dot_array |
| M1.S4.T4.C10.IMG1 | question | dot_array |
| M1.S4.T4.C11.IMG1 | solution | dot_array |
| M1.S5.T5.C12.IMG1 | question | other |
| M1.S5.T5.C13.IMG1 | solution | other |
| M1.S5.T5.C14.IMG1 | question | other |
| M1.S5.T5.C15.IMG1 | solution | other |
| M1.S8.T8.C31.IMG1 | question | other |
| M1.S8.T8.C32.IMG1 | solution | other |
| M2.S13.T13.C55.IMG1 | question | flow |
| M2.S13.T13.C56.IMG1 | solution | flow |
| M2.S13.T13.C57.IMG1 | question | flow |
| M2.S13.T13.C58.IMG1 | solution | flow |
| M3.S23.T23.C97.IMG1 | question | place_value_model |
| M3.S23.T23.C98.IMG1 | solution | place_value_model |
| M3.S23.T23.C99.IMG1 | question | place_value_model |
| M3.S23.T23.C100.IMG1 | solution | place_value_model |
| M3.S23.T23.C101.IMG1 | question | place_value_model |
| M3.S23.T23.C102.IMG1 | solution | place_value_model |
| M3.S23.T23.C104.IMG1 | solution | place_value_model |
| M3.S30.T30.C141.IMG1 | question | other |
| M4.S37.T37.C171.IMG1 | question | cell_grid |
| M4.S37.T37.C172.IMG1 | solution | cell_grid |

### Chunk A notes (from the decision agent)
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

### Chunk B notes (from the decision agent)
# Chunk B notes - Class 5 Ch 9 "Coconut Farm" (units 18 to 34)

Result: 28 items, required 4 / optional 0 / none 24. Validator: errors 0, warnings 0.
Required = Try It! Q1 (C55 question, C56 solution) and Try It! Q2 (C57 question, C58 solution), nothing else.
Everything else is none (text / LaTeX).

## Borderline

1. **Place value charts, T9 Q2 and Q3 (C37/C38, C39/C40): none, code LATEX_TABLE + HEADER_BOXES_ONLY.**
   The book asks "Now fill the place value chart" (Problem | H | T | O). Two readings are possible: ACTION_ON_FIGURE /
   ANSWER_IS_FIGURE ("filled table") says required; the Step C rules say a plain table of numbers with no colour meaning, and place-value
   header boxes filled with digits, go to a LaTeX array (the audit's "not a diagram" list names both). I followed the Step C rule as written,
   because a LaTeX array shows the chart exactly (there is no colour, arrow or drawing in it). If the user wants these four
   drawn, each pair would be one 4-column table card (question: the three example rows filled and the empty rows; solution: all rows filled,
   `derived_from` the question). Note the headings: the book prints H, T, O; the LP text says Hundreds, Tens, Ones.
2. **Try It! Q1 and Q2: both sides required although the LP text carries every number.** The book question IS the box diagram the learner
   completes (split tree: split the dividend, divide each part, join with the sign; halving chain). The LP question of Q1 even says "The boxes show a plus sign
   ...", which points at a figure the text-only plan lacks. The answer is the completed diagram (step B2, arrangement / filled figure).
   Q2 (halving chains) has no such sentence, but it is the same kind of box diagram in the same Try It! set, so it got the same decision
   (sibling consistency). These are flow diagrams with arrows and operators, not plain tables, which is why they differ from point 1.
3. **One combined picture per side for Try It!.** The LP holds Q1 to Q4 in one concept (C55) and Q5 and Q6 in another (C57), with one
   question card each; the brief allows ONE question diagram and ONE solution diagram per pair. So the four split trees are one 2 x 2 picture
   and the two halving chains one two-row picture. The v3 prompt says a question split into parts gets one diagram per part, but the LP did
   not split them, so the brief's rule won. If the user prefers six separate pictures, the LP would first have to be split into six concepts.
4. **Panel/row numbers are drawn** ((1) to (4), (5), (6)) because the LP solution text refers to the items by these numbers (user decision 3).
5. **C35 (nine blue boxes of divisions): none.** Nine independent facts and the two hints are written in the question text; the boxes carry no
   position, colour or arrow meaning. Codes LATEX_ARITHMETIC + NUMBER_LIST_IN_BOXES. (The pink grid of Let Us Do Q2 is chunk A's.)
6. **Worked examples C41 and C61 (kept teaching images) and C42, C43, C62, C63: none.** They are practice-value arithmetic written as short
   equations; text alone solves them exactly as well. The decision does not depend on the kept teaching images (user decision 5): C41's bar and
   C61's bar are teaching images and stay untouched and unlinked.
7. **Open questions (C51 to C54): none** (OPEN_ENDED); the LP solutions are sample answers written as equations.

## Judgement calls

- **Which figures I claimed.** P03-equation_boxes-2, P03-place_value_table-1 and -2, P05-split_tree-1 to 4, P05-halving_chain-1 and 2.
  Each Try It! figure also has a `NEW-P05-<name>-<n>-sol` entry for its second use (the completed solution picture).
- **Not claimed: the P06/P07 long-division layouts** (P06-long_division-1 and 2, P07-long_division-1 to 3). My T15 worked examples
  (C61 to C63) share the book sections `sf.text`, `sf.estimate`, `sf.discuss`, `ld.rule` with chunk C's units 35 to 40, but they use practice
  values (378 ÷ 6, 861 ÷ 7, 487 ÷ 9) and none of those layouts. Chunk C owns them; if C does not claim them the merge check will show it.
  The pink box "N = D x Q + R" on pdf page 7 is a formula callout, not in the base inventory; I did not add it (chunk C's `ld.relation` unit is the closer owner).
- **NEW figures.** The three purple text panels of the book's examples on pdf page 5 (1248 ÷ 6, 1992 ÷ 4, 128 ÷ 4) were not in the base
  inventory. They hold only worked arithmetic as plain text, so they are `NEW-P05-example-1..3` mapped `none:LATEX_ARITHMETIC`. I also looked at pdf page 6:
  the "Let Us Solve (a) to (h)" list has no figure.
- **Colours.** The book prints the boxes light blue; the spec uses CELL_FILL (house token). Question content INK, solution additions ANSWER green.
- **Blank in the halving label.** The book's "Halve ____" blank is read as the number being halved (84, 42, 72), the reading the LP solution supports.
- **Solution diagrams draw the LP's own splits** (64 = 40 + 24, 265 = 250 + 15, 1560 = 1600 - 40, 4824 = 4800 + 24); the book prints no answers
  and the LP says other splits work too.
- **Book mistakes (user decision 1): none found** in the figures of this chunk. All printed givens (expressions, signs, divisors,
  chart rows) agree with the LP, and every LP answer was recomputed (all 17 solutions are mathematically correct).

## LP text issues

- **M1.S9.T9.C37 / C38 and C39 / C40 (place value charts).** The question text only describes the chart in words. With the decision none (LATEX_TABLE) the table
  itself should be in the text. Suggested for C37: "Now fill the place value chart" followed by a LaTeX array with columns Problem, H, T, O and rows
  `40 \div 10 = | | | 4`, `400 \div 10 = | | 4 | 0`, `4000 \div 10 = | 4 | 0 | 0`, then four empty rows `700 \div 70`, `1400 \div 100`, `220 \div 20`,
  `2200 \div 20`. Suggested for C39: the same array with the six empty rows 110 ÷ 11, 860 ÷ 86, 7500 ÷ 750, 8800 ÷ 88, 2400 ÷ 24, 440 ÷ 22. The solutions (C38, C40)
  likewise: the filled arrays (values are in the `text_alternative` of each item). The book heads the columns H, T, O; the LP says Hundreds, Tens, Ones: pick one.
- **M1.S9.T9.C35 and C36, item (i).** "(i)" is not wrapped in math ($(i)$) while (a) to (h) are. Suggested: `$(i)$: $4000 \div 40 = ...$` in question_tex and steps_tex.
- **M2.S11.T11.C45 to C50 (book numbers).** The LP calls the book's three text boxes "Example 2", "Example 3", "Example 4"; the book prints them as 1, 2, 3.
  This may be on purpose (the LP's own Example 1 is the practice-value worked example C41); if not, `book_number` should read Example 1 to 3.
- **M2.S12.T12.C54 (repeated halving).** The text says "repeated halving works for the divisors 2, 4, 8 and 16", which reads as a complete list. Any power of 2
  works (32, 64, ...). Suggested sentence: "So repeated halving works for the divisors 2, 4, 8, 16 and every other power of 2, such as 32."
- **M2.S13.T13.C57 (Try It! Q2).** The question text does not mention the boxes or arrows (C55's does). With the diagram added this is fine; without it,
  add: "Fill the boxes: each arrow halves the number before it."
- **T10 and T15 worked examples (C41 to C43, C61 to C63).** The question lines end with "(practice values)", which is a build marker rather than text a child should read; consider removing it.

## Book unclear or odd

- Try It! item 3 (1560 ÷ 8): the minus sign in the second row is partly hidden by the page watermark in the picture; it is visible and matches row 1, and the LP question text also says minus for (3).
- Try It! 5 and 6: the book does not say what goes in the blank of "Halve ____"; the reading above is the natural one.
- The book prints no answers section (as the brief says), so none of the diagrams copies a printed answer picture.

### Chunk C notes (from the decision agent)
# Notes, chunk C (Class 5 Ch 9 "Coconut Farm", topics T16 to T22)

Result: 30 items, required 0 / optional 2 / none 28. Validator: errors 0, warnings 0.

## 1. Judgement calls

- **Long division is LaTeX arithmetic.** Every picture in this chunk is a long-division layout (Susie's partial quotients, Sunitha's layout, the partly blank frames) or a column-multiplication frame. Step C lists "long division" under `LATEX_ARITHMETIC`, and the 23 Nov brief says text and LaTeX are the default. The same call was made in Class 5 Ch 4 (column addition and subtraction) and Class 7 Ch 12 (long division). Each `none` item carries a `text_alternative` that says which LaTeX array to write.
- **No question in the chunk gives a figure the text does not carry.** Example 5 to 9 and the oil/husk/tender questions are word problems with all numbers in the text. The book layouts printed under them are the book's solutions. The Let Us Learn to Divide frames (726 / 4, 902 / 16) and the tender-coconut frame (8890 / 35) are restated blank by blank in the LP question text.
- **Solutions.** The pdf has no printed-solutions section. The "printed answer" is the layout printed under each example. Because it is long division, not a picture in the sense of Step B2 (stick-figure line-ups, coloured tables, number lines), I did not apply "printed answer is a picture". No solution adds anything visual that the LP steps lack.
- **Figure claims.** I claimed the 10 base figures of pages 6 to 9 (all `none:LATEX_ARITHMETIC`) and added `NEW-P07-formula_box-1` (the boxed N = D x Q + R, `none:TEXT_SUFFICIENT`). I did not claim P10-*, P11-*, P12-*, P13-* (pages 10 to 13). They are the book's pictures for the examples 62 / 5, 75 / 8, 324 / 3, 136 / 6 and the Let Us Divide frames, which belong to chunk D's units (T23 to T25). My T22 worked examples (C93, C94, C95) use practice values (83 / 6, 412 / 4, 3,648 / 12) and none of those pictures. If the merge wants them claimed here too, the same `none` or item meaning as chunk D's applies.
- **P09-column_multiplication-1** is mapped `none:LATEX_ARITHMETIC` (the H T O heading alone would be `HEADER_BOXES_ONLY`, also true, both are in the item's reason codes).
- **Base descriptions checked against the page pictures** (pp. 6, 7, 8, 9, 10, 11, 14): all ten base entries I claimed are correct (digits, counts of subtractions, coloured digit cells, blank positions). No "CORRECTED:" needed. Page 14 has no picture for Q4 (remainders, C79/C80).

## Borderline

- **C66, C70, C84, C86 (solutions with a printed layout).** Kept `none`. The coloured digit cells above the quotient (9|7, 2|1, 5|4|7, 4|3|1) only mirror the digits of the quotient. A side-by-side drawing of Susie's and Sunitha's layouts would compare the number of steps (6 against 2, 5 against 3), but the LP steps already say it in words ("Sunitha's way takes 2 steps and Susie's way takes 6 steps"). If the user wants a picture here, these four are the first to flip to `required` (type `other`, long-division layout, derived from nothing because the question side has no figure).
- **C71, C73, C89 (question side, partly blank frames).** Kept `none`: ACTION_ON_FIGURE could be argued (the student completes a frame), but the LP question text lists each blank, so the tie-breaker says the text is enough. The completed solution frames (C72, C74, C90) follow the question side (`none`).
- **C87 (blank column-multiplication frame).** Kept `none` (LaTeX array with H T O headings).
- **C93 and C94 (worked examples, `optional`).** Base-ten blocks sharing 83 on 6 plates and 412 on 4 plates would clearly help but are not needed to follow the steps. I decided this on the tie-breaker and the absence of a v3 trigger, not because the same figures already exist as kept teaching images C93.IMG1 and C94.IMG1 (user decision 5). If the user wants an own diagram for each worked example, flip both to `required`, `add_new_image`, `question_tex / after_question_text`, ids `M3.S22.T22.C93.IMG2` and `M3.S22.T22.C94.IMG2`; they would be copies of the two teaching images in content.
- **C81, C95 (worked examples with practice values).** `none` (take-away lines and two-way comparison are arithmetic). C95 has no teaching image.

## 2. LP text issues

- **M2.S16.T16.C66, C70; M2.S20.T20.C84, C86; M2.S21.T21.C90** (field `text`): stale `[Image: ... solution]` and `[Image: ... solution (continued)]` markers sit inside the step text (after step 4 in C66, for example). The old cards are dropped, and nothing replaces them (all `none`), so the builder must strip these markers.
- **M2.S21.T21.C90** (answer): the blanks are listed as "200, 1750, 140 and 4", but the question's blanks come in the order: quotient parts (200 and 4), then 1750, then 140, then the total. Suggested sentence: "The blanks, in order, are $200$, $4$, $1750$ and $140$, and Ibrahim sold $254$ tender coconuts."
- **M2.S21.T21.C91** (question): the number of coconuts is never stated. The question asks for "___ coconuts at ₹20 each" and the solution begins "Ibrahim sold 254 tender coconuts". The number only comes from the previous question. Suggested sentence added to the question: "Ibrahim sold $254$ tender coconuts (from the previous question)."
- **M2.S17.T17.C73** (question): the book frame has one more blank (the remainder 102 under -800) that the LP text does not mention. Not needed to answer; the LP solution gives it ("902 - 800 = 102").
- **M2.S16.T16.C67/C68**: LP is right ("4 bags are needed"); see section 3 for the book's wording.

## 3. Where the book itself is unclear or slips

- Page 6, the bag example: the book ends "So, each person will get 4 bags". It is the number of bags needed, not a quantity per person; the LP already says "4 bags are needed". No figure is involved.
- Page 7, Let Us Learn to Divide, 726 / 4: the frame leaves the first subtrahend (400) and the last subtrahend (4) blank as well as the two quotient parts (80 and 1). The LP question puts all four blanks into words (400, 80, 4, 1), which matches the book frame.
- No arithmetic error or print slip was found in the figures of pages 6 to 9; every layout was recomputed (582 / 6 = 97, 535 / 25 = 21 r 10, 726 / 4 = 181 r 2, 902 / 16 = 56 r 6, 4376 / 8 = 547, 9913 / 23 = 431, 8890 / 35 = 254, 547 x 175 = 95,725).

### Chunk D notes (from the decision agent)
# Notes for chunk D (Class 5 Ch 9 "Coconut Farm", topics M3.S23.T23 to M3.S29.T29, units 52 to 67)

Result: 29 items = required 7 / optional 1 / none 21. Validator: errors 0, one warning (the Example 13 solution figure is not printed in the book, so no inventory figure maps to it; expected).

Required diagrams (all 16:9, base-ten blocks or place-value chips):

| Item | Diagram |
|---|---|
| C97 question | 62 as 6 ten-rods + 2 squares, 5 empty parts |
| C98 solution | 5 parts of 1 rod + 2 squares (12), remainder 2 |
| C99 question | 75 as 7 ten-rods + 5 squares, 8 empty parts |
| C100 solution | 8 parts of 9 squares, remainder 3 |
| C101 question | 324 as chips 3 x 100, 2 x 10, 4 x 1, 3 empty parts |
| C102 solution | 3 parts of 1 hundred chip, 0 tens, 8 one chips (108) |
| C104 solution | 6 parts of 2 ten chips + 2 one chips (22), remainder 4 (stands alone, derived_from null) |

## 1. Judgement calls

- **C97, C99, C101 questions (required).** The book prints the blocks/chips beside each example and the question card narrates them ("the following way", "this", "Divide into 3 equal parts"). The question figure shows only the given state (the number as blocks/chips and the empty equal parts). Red notes, outlines around single rods (they show the sharing) and every answer element are left out. For C97 the book's picture mixes start and end state; the question diagram takes only the start.
- **C98, C100, C102 solutions (required).** Same kind of answer in all four examples: equal sharing of place-value material (ANSWER_IS_FIGURE, B2 sibling rule). Each is `derived_from` its question diagram (same layout, new content in ANSWER green). C98 follows the book's printed end state. For C100 and C102 the book prints no end state (only the start state); the final state follows the LP solution text.
- **C103 question none, C104 solution required.** Example 13 (136 / 6) has no model picture in the book and the card gives none, so no question figure is invented (companion note). The solution is required for sibling consistency with examples 10 to 12 and draws the final state alone. The book's only picture for it is the long division (LaTeX).
- **Let Us Divide (a) to (d), 8 items, all none (LATEX_ARITHMETIC, HEADER_BOXES_ONLY).** v3 sends long division and plain place-value header boxes (Th H T O) to LaTeX. The LP text already gives every number and blank. A `text_alternative` per item says which LaTeX layout to write. Printed answers are filled arithmetic layouts, not pictures. All four letters get the same decision.
- **Let Us Do Q1 (C115/C116) none.** Ten digit-box frames = long-division skeletons; the LP text lists every frame with its blanks. The answers are numbers. I did not make one combined 10-frame picture.
- **C123 optional (not added).** A picture of 94 coconuts as 11 bags of 8 + 6 left (+ the 12th bag) would help show what the remainder means, but the text is complete.
- **C124 none (LATEX_TABLE).** The "bill" is a plain table of numbers with the example's own practice values.
- **C125, C105/C106, C117/C118, C119 to C122 none.** Word or arithmetic items with no figure in the book.
- **Figure letters (decision 3).** No letters drawn anywhere. The three question diagrams are single figures; the (a) to (d) layouts are none.
- **Teaching images (decision 5).** The plan's concept images in this part (C93.IMG1 "8 tens and 3 ones among 6 plates", C94.IMG1 "412 among 4 plates") show different numbers and are in topic T22. Nothing is linked to them. The 7 diagrams are drawn fresh.
- **Figure accounting.**
  - 25 base figures claimed: P10-base_ten_blocks-1/2, P10-long_division-1/2, P11-place_value_chips-1, P11-long_division-1/2, P12-long_division-1..6, P13-long_division-1/2, P13-division_frame-1..10.
  - 3 NEW- second-use entries: NEW-P10-base_ten_blocks-1-sol, NEW-P10-base_ten_blocks-2-sol and NEW-P11-place_value_chips-1-sol, for the solution diagrams.
  - Result: 6 mapped to items, 22 mapped none, 0 mapped to concept images.
  - **P16-table-1 (Vegetable Market table) not claimed.** My C124 uses its own practice values and does not use the book table. The pair vm.table is another chunk's. If both chunks claim it at merge, `none:LATEX_TABLE` would be my meaning for the plain table.
  - The riddle box on p.13 (girl illustration) is not in the base inventory; it is decoration, so I did not add a NEW- entry.
- Base descriptions were checked against pages 10 to 13: all 25 are correct, and the `unclear` lists were empty. I checked especially the ten frames (frame 7 reads `50 ) 1 0 0 [ ] ( [ ] 0`, as inventoried).

### Borderline (decision 4, v3 applied as written)

1. Question side of C97, C99, C101: the numbers are all in the text, so a strict "attempt" test could say none; I kept them required because the book prints the figure with the question and the question text points at it. If the user prefers, these three can drop to `optional`; the three solution diagrams would then need `derived_from: null` and would be redrawn as standalone figures.
2. Solutions C100 and C102 (and C104): required although the book prints no end-state picture; justified by the sibling rule and the LP's own s_figure hints for 10 to 12. If unwanted, C104 is the weakest (no figure at all in the book).
3. Let Us Divide (a) to (d), Let Us Do Q1, Let Us Solve 1 to 12: none by the v3 long-division rule although the book asks to complete a drawn layout. This is the biggest call (8 + 2 items). If the content team wants those layouts as pictures, they would be `other` diagrams of the two layouts per part.
4. C123 optional (not added).

## 2. LP text issues (not edited; suggestions only)

- **Example numbering.** C97/C98 to C103/C104 (book numbers "Example 10 to 13"): the book prints no "Example n" labels; its four examples are numbered 1 to 4 inside "Division Using Place Value". The LP's chapter-wide numbering is the LP author's, not the book's.
- **M3.S23.T23.C97 (question).** "She shows the following way of doing division using place value." The "following way" (blocks and long division) is not in the text. Suggested: "Look at the blocks: 6 tens and 2 ones. Divide 62 into 5 equal parts."
- **M3.S23.T23.C101 and C103 (questions).** The question text already contains the worked steps and results that the solution repeats ("24 Ones ÷ 3 = 8 Ones", "Total 13 Tens"), so the question gives the answer away and the question and solution cards duplicate text. Suggested questions: "324 ÷ 3: divide 324 into 3 equal parts. 324 = 3 Hundreds + 2 Tens + 4 Ones." and "136 ÷ 6: divide 136 into 6 equal parts. 136 = 1 Hundred + 3 Tens + 6 Ones."
- **M3.S24.T24.C105 (question).** "Look at the problems above" does not name them. Suggested: "Look at the four divisions 62 ÷ 5, 75 ÷ 8, 324 ÷ 3 and 136 ÷ 6."
- **M3.S25.T25.C107 (question, part a).** In the book the right-hand place-value layout of (a) is fully filled and is the model for (b) to (d). The LP gives only the quotient digits "1, 1, 7, 2", not the rows (7 - 6 = 1, 10, 43, 12), so the learner never sees the model. Suggested: add the filled layout as LaTeX, or its rows (the text_alternative on C107/C108 gives them).
- **C107, C109, C111, C113 (questions).** The two layouts (partial quotients; place value with Th H T O and the labelled rows) are only described in sentences. Suggested: write them as LaTeX layouts (text_alternative gives the layouts).
- **M3.S26.T26.C115 (question).** The part letter "(i)" is not wrapped in `$...$` like the other letters (formatting). The ten frames are written as prose; an explicit list is clearer.
- **M3.S29.T29.C123 (worked example).** Learner-visible "(practice values)", and two sub-questions with no context. Suggested: "Susie and Sunitha have 94 coconuts. (a) They pack them in bags of 8. How many bags do they need? (b) They share the 94 coconuts equally among 8 customers. How many does each customer get?"
- **M3.S29.T29.C124 (worked example).** Three sub-questions in one sentence, no bill shown, and missing data: "the quantity for a total of ₹990" does not say the price is the same ₹18 per kg (the solution uses 18). Also "(practice values)" shows to the learner. Suggested: "A bill: onions, ₹18 for 1 kg, 45 kg sold. (a) Find the total amount. (b) At ₹18 for 1 kg, how many kg give a total of ₹990? (c) 36 kg of another item cost ₹1260 in all. What is the cost of 1 kg?"
- **M3.S29.T29.C125 (worked example).** "(practice values)" in learner text.
- Solutions C106, C108, C110, C112, C114, C116, C118, C120, C122, C123 to C125: all arithmetic re-computed and correct (quotients, remainders, N = D x Q + R, the place-value digit strings, and all ten Let Us Do answers incl. (e) 848 / 868 and (g) 88 / 44 / 22 / 11). C118 step 1 assumes the first clue is an exact division; the second clue (x 2 = 420) fixes 210 anyway.

## 3. Where the book is unclear

- Let Us Divide (c) and (d), right layouts: pairs of empty brackets `(          )` appear to the right of the rows. They look like slots for place labels such as (Tens), (Ones). The book never says; the LP does not use them.
- Let Us Divide (b), right layout: the ones row prints `0___` (a blank after the 0), which is a slot for the digit 5 brought down; the quotient row has its tens digit 0 printed, thousands/hundreds/ones blank.
- Let Us Divide (b) to (d) start the right layout at the Hundreds row (30 hundreds, 28 hundreds, 98 hundreds), so the Thousands row is not drawn although the quotient has a Th slot; the LP solution adds a Thousands line (0 each) to match the four quotient digits.
- No printed solutions section in this pdf; the LP solution text was followed throughout. No print slips (wrong digit, wrong count) were found in the figures of this chunk, so no CORRECTED value was needed.

### Chunk E notes (from the decision agent)
# Chunk E notes (Class 5 Ch 9 "Coconut Farm", cbse_eng_maths5_ch9_v4)

Topics: M3.S30.T30 (Let Us Solve, word problems), M3.S31.T31 (Vegetable Market), M3.S32.T32 (How the Quotient Changes), M3.S33.T33 (Let Us Solve, relations), M4.S34.T34 (True or False Statements).
Result: 16 units, 30 items. Questions: required 1 / none 13. Solutions: optional 2 / none 12. Worked examples: none 2. Validator: errors 0, warnings 0.
Book pages used (all looked at): p.8 (word problems Q1-Q4, no figure), p.14 (Q1-Q3 word problems, Q5 panels A, B, C), p.15 (Q6 map, Q7, Q8 bookshelf), p.16 (Vegetable Market table), p.17 (checked for T34).

## Figures claimed (6)
- P14-equation_panels-1/2/3 -> none:LATEX_ARITHMETIC (plain equation lists, answer is numbers).
- P15-map-1 -> item:M3.S30.T30.C141 (question): the only diagram of the chunk, media id `M3.S30.T30.C141.IMG1`.
- P15-object_picture-1 -> none:DECORATIVE_ONLY (bookshelf illustration).
- P16-table-1 -> none:LATEX_TABLE (Vegetable Market table).
- Not claimed on purpose: P17-table-1 (Q4 tick table) and P17-label_arrows-1 (Q3 red margin notes). They belong to the questions `st.q4` and `st.labels`, which are units of chunk F. My T34 unit is the definition sentence `st.def` ("a true sentence is one where both sides of the '=' sign have the same value") and has no picture. The base inventory gives both figures the section name "Mathematical Statements", which is also the section of my T34 unit, so chunk F must claim them (merge check).
- The 20 other base figures of pages 1-13 are other chunks'. P16-table-1 may also be touched by chunk D (worked example C124 "Missing Numbers in a Bill", refs vm.text / vm.info): I gave it `none:LATEX_TABLE`, the meaning the v3 prompt gives a plain table.
- No NEW- figure found. Base descriptions of my six figures were checked against the page pictures and are correct; the `unclear` doubts are answered in the figure descriptions (map arrowheads: 576Km two heads, 344Km a head at Ratnagiri and one near Mumbai, 232Km a head at Goa; tiny blue icons on the route are buildings, decoration; B (c) and (e) really are printed the same).

## Judgement calls
1. C141 question (cycle rally, book p.15 Q6): `required`, DATA_IN_FIGURE. Part (b) needs 232 km (Ratnagiri to Goa), which the book prints only in the map and the LP question text omits. A real map cannot be drawn faithfully (NOT_RENDERABLE), so the spec is a schematic route strip: Mumbai - Ratnagiri - Goa laid flat left to right, to scale (344 : 232), with the three printed distances 344 km, 232 km, 576 km as brackets. It shows nothing the question does not give (no 48 km, 58 km, days). Diagram type `other` (nothing in the catalogue fits a route with three stops; a number line would have to print 0 / 344 / 576 ticks that the book does not give). Aspect 16:9 although the book map is portrait: the pipeline draws 16:9 cards, so the route is laid horizontally. The book's blue/red/purple arrow colours are replaced by the tokens SET_A (344 km), SET_B (232 km) and INK (576 km).
2. C142 solution (cycle rally): `optional`, not added. The solution splits 232 km into 4 days of 58 km and 576 km into 12 days of 48 km, which a route strip could show, but the answer is two numbers (48 km, 58 km), not a picture, and the steps carry all of it (Step E: figure-based question, numeric answer, solution at most optional). If you want it added, it would be `derived_from` M3.S30.T30.C141.IMG1 with the day split in ANSWER green.
3. C145 question (bookshelf, book p.15 Q8): `none`, DECORATIVE_ONLY. The picture shows the assembled bookshelf (4 long and 4 + 4 = 8 short panels, no clips or screws) and every number the question needs is in the text.
4. C146 solution (bookshelf): `optional`, not added. A row of the five parts with the bookshelves each allows (66, 38, 150, 30, 87) and the 30 circled would help the "scarcest part" idea, but the steps list all five numbers and say the smallest is 30. HIGHLIGHT_MEANING is in the required list ("circled smallest"), but the LP solution does not use a circle and the smallest value is fully stated in words, so I did not treat the circle as something LaTeX cannot show.
5. C147 / C148 (Vegetable Market table): both `none`, LATEX_TABLE. The table is plain (headings and numbers; only the header row has a light fill, no colour meaning). The v3 prompt's own example "Complete the table of how many numbers have 1 to 5 digits" is a LaTeX array with no image. The completed table of C148 is the same table with five numbers filled in. This is the call most likely to be questioned: see Borderline and LP text issues.
6. C132 solution (Sofia's notes): `none`, LATEX_TABLE. The six combinations are a two-column table of numbers; real banknote pictures would be NOT_RENDERABLE and the book gives none.
7. C151-C156 (relations A, B, C): all six sides `none`, LATEX_ARITHMETIC (same decision for all three parts, as required by the sibling rule). An arrow picture of "doubled / halved" would at most be optional because the reason is already written in each step.
8. C149 (How the Quotient Changes) and C157 (Both Sides of the Equal Sign) worked examples: `none` / `no_image`. Equations and words; no book figure belongs to them.
9. All pure word-problem pairs (C127-C140, C143/C144): `none`; the book page has no figure for Q1-Q4 (p.8), p.14 Q1-Q3 or p.15 Q7.

## Borderline
- C141 question: required, but the figure is a schematic redraw of a real map (see 1).
- C142 solution and C146 solution: optional (not added) rather than required (see 2 and 4).
- C145 question: bookshelf picture dropped as decoration (see 3). It does show the 4 long and 8 short panels of the list, so a reviewer could call it `optional`.
- C147 question and C148 solution: plain table kept as LaTeX instead of an image (see 5). If the table should be a picture, C147 would be `required` (DATA_IN_FIGURE, ACTION_ON_FIGURE) and C148 `required` derived from it; the spec would be a `cell_grid` with the 5 x 6 table and the five blanks (question) / the five filled values in ANSWER green (solution).
- C132 solution: table of combinations kept as LaTeX.
- C151/C153/C155 and solutions: kept as LaTeX equations.

## LP text issues
1. **M3.S31.T31.C147 (Vegetable Market, question).** The question text is only "His naughty grandson has erased some numbers from his record book. Help Munshi Lal complete the table." The table itself (the data of the question) is not in `question`, `question_tex` or `text`; it exists only in the old question card. With the decision `none` / LATEX_TABLE, the table must be written into the question text (item has `needs_lp_text_sync: true`). Suggested sentence plus table, in LaTeX (KaTeX has no `\multicolumn`, so the last row puts the label in the Vegetable column):
   "Munshi Lal's record book for one Saturday is below. Some numbers are erased. Help Munshi Lal complete the table."
   `\begin{array}{|c|l|c|c|c|} \hline \text{S.No.} & \text{Vegetable} & \text{Cost of 1 kg} & \text{Quantity supplied (in kg)} & \text{Total amount} \\ \hline 1 & \text{Radish} & ₹26 & 78 & ₹\underline{\hspace{2em}} \\ \hline 2 & \text{Potato} & ₹20 & \underline{\hspace{2em}} & ₹2{,}240 \\ \hline 3 & \text{Cabbage} & ₹32 & 56 & ₹\underline{\hspace{2em}} \\ \hline 4 & \text{Green peas} & \underline{\hspace{2em}} & 125 & ₹3{,}125 \\ \hline & \text{Total money earned through the sale} & & & \underline{\hspace{2em}} \\ \hline \end{array}`
   (The text of Vegetable Market in the book calls the Peas price column blank and the total row blank: five blanks in all.)
2. **M3.S31.T31.C148 (Vegetable Market, solution).** The steps and the answer line give every value, but no table. Suggest adding the completed table as the first line of the steps: Radish ₹26, 78, ₹2,028; Potato ₹20, 112, ₹2,240; Cabbage ₹32, 56, ₹1,792; Green peas ₹25, 125, ₹3,125; total ₹9,185. (Arithmetic checked: 26 x 78 = 2,028; 2,240 / 20 = 112; 32 x 56 = 1,792; 3,125 / 125 = 25; 2,028 + 2,240 + 1,792 + 3,125 = 9,185.)
3. **M3.S30.T30.C141 (cycle rally, question).** The text has no 344 km / 232 km and does not say that Ratnagiri lies on the way, yet part (b) and the solution ("the map shows 344 km ... and 232 km") rely on them. They are carried by the new question diagram. If you want the text to be complete without the picture, suggested sentence: "On the route, Ratnagiri is 344 km from Mumbai and 232 km from Goa." (344 + 232 = 576, which matches the 576 km.)
4. **M3.S30.T30.C146 (bookshelves, solution).** Steps say "264 / 4 = 66 shelves", "38 shelves", "150 shelves", "30 shelves", "87 shelves" and "the smallest number is 30" while the question's long panels are the shelves of one bookshelf (4 per bookshelf). Suggested wording: "66 bookshelves", "38 bookshelves", and so on, and the sentence "The carpenter can only make as many bookshelves as the scarcest part allows." The numbers themselves are right (264/4 = 66; 306/8 = 38 r 2; 2400/16 = 150; 120/4 = 30; 2800/32 = 87 r 16).
5. **M3.S33.T33.C154 (relations B, solution).** The book prints (c) and (e) as the same 384 / 8, and (f) as 86 / 2, which does not follow from 192 / 4 by doubling or halving. The LP already handles it (answers (e) 48 as (c), (f) 43, and mentions 96 / 2 = 48). If the content team confirms a misprint in the book, the likely intent of (f) is 96 / 2 = 48 (both numbers of 192 / 4 halved); the intent of (e) is not known (a guess is 384 / 16 = 24 or 96 / 4 = 24). Nothing in the diagram specs depends on it.
6. **M3.S30.T30.C132 (Sofia, solution).** Step 1 says "Let the ₹50 notes be a few, from 0 to 10"; suggest "any whole number from 0 to 10". The list of six ways includes 0 notes of ₹50 and 1 note of ₹20 with 10 notes of ₹50; the last step already says the book does not say whether both kinds must be used (if both are needed there are five ways). Arithmetic is right (5a + 2b = 52 gives a = 0, 2, 4, 6, 8, 10).
7. **LP numbering vs the book (no action needed for diagrams).** The LP names the second set Q5-Q10 (C135, C137, C139, C141, C143, C145) while the book numbers them p.14 Q1, Q2, Q3, p.15 Q6, Q7, Q8; Q1-Q4 of p.8 are LP Q1-Q4. The book's p.14 Q4 (six divisions with remainders) and p.8 Q5 are in other topics, not in this chunk.
8. **Arithmetic re-checked, no errors found** in: C128 (250 = 6 x 41 + 4, 250 = 8 x 31 + 2), C130 (342 = 41 x 8 + 14), C134 (417 / 3 = 139), C136 (475 = 45 x 10 + 25; 11 = 2 x 5 + 1), C138 (4,600 / 23 = 200), C140 (15 x 8 / 6 / 4 = 5), C142 (576 / 12 = 48; 232 / 4 = 58), C144 (all values), C152, C154, C156 (all quotients), worked examples C149 and C157.

## Where the book itself is unclear
- Book p.14 Q5 panel B: (c) and (e) are printed identically (384 / 8); (f) 86 / 2 breaks the pattern (see LP text issue 5).
- Book p.15 Q6: the map is a picture only; the question text never says that the 344 km and 232 km are printed in it. The route runs along the coast, so a straight-line reading is not meant, and "Assume that they cover the distance evenly" is the only rule for the daily distance.
- Book p.8 Q3 (Sofia): does not say whether both kinds of note must be used.
- Book p.8 Q1 and p.15 Q7, Q8 are open-ended ("Explain your answer", "Identify the missing information", "Discuss your thoughts"): the LP gives a sample answer or practice values; no printed solutions exist in this pdf.
- Book p.17 box 1 (T34): the examples of "true sentence" in the LP worked example C157 are the LP's own practice values (6 x 5 = 20 + 10, 18 / 3 = 2 x 4, 9 x 4 = ___ + 16), not the book's Q1/Q2 statements.

### Chunk F notes (from the decision agent)
# Notes for chunk F (Class 5 Ch 9 "Coconut Farm"): Mathematical Statements

Topics: M4.S35.T35 (Q1, Q2), M4.S36.T36 (worked example), M4.S37.T37 (Q3 a/b/c, Q4).
Result: 13 items, required 2 / optional 0 / none 11. Validator: errors 0 (10 warnings, all "long visible_text", see 1.8).
Figures claimed: P17-table-1 (Q4 question), NEW-P17-table-1-sol (Q4 solution, second use of the same table),
P17-label_arrows-1 (none:TEXT_SUFFICIENT). Both base figures of page 17 were checked against `book/page_17.png`: the
base descriptions are right (the answer column widths are about 12% / 17% / 10% of the table width, not "about equal").

## 1. Judgement calls

1.1 **Q4 tick table (C171 question, C172 solution): both required.** The book's blank tick table is the thing the
student acts on (tick one cell per row), and the answer IS the ticked table (v3 B2: `ANSWER_IS_FIGURE`,
`ACTION_ON_FIGURE`). The question text does not even name the three columns, so the figure is needed to attempt it.
This is not a "plain table of numbers". The solution is `derived_from` the question diagram (same grid, same positions,
five ticks in ANSWER green). One diagram only for C172 although the old plan had two cards (IMG1 and a "continued" IMG2):
one table, one picture.

1.2 **Row letters (a) to (e) shown in the Q4 picture.** The book's table has no letters, but the LP question and the LP
answer text both refer to the rows as (a) to (e), so by decision 3 the letters are drawn (they are in `visible_text`).
The statement text is the book's own row labels, so it is part of the figure (not question text pasted in).

1.3 **Header fill CELL_FILL, not the book's green.** The book's header is light green; MARK_FILL would suggest "marked
cells", so the neutral CELL_FILL is used. Answer columns are drawn with equal 238 px width for legibility.

1.4 **Q3 (a), (b), (c): all six items none.** The only book picture is the three red margin hints (Always true / Never
true / Sometimes true). They are word labels and would give the answer away in a question figure, so
`P17-label_arrows-1` is `none:TEXT_SUFFICIENT`. The answers are lists of sample equations plus a word, not a picture,
so the solutions are text/LaTeX. Sibling consistency: Q3 (a), (b), (c) get the same decision; Q4's solution differs
because its answer is a ticked table (different kind of answer).

1.5 **Q1 and Q2: none.** Plain equations; the book has no figure for them. (`LATEX_ARITHMETIC`.)

1.6 **T36 worked example (C163, block 0): none (`no_image`).** Three statements tested with numbers, all written in the
steps. The book has no figure for it (its `ncert_refs` is `st.labels`, the margin hints). A grouping picture would only be nice, not needed.

1.7 **Q4 (b) tick = Sometimes** follows the LP ("only for two equal numbers, with whole numbers"). See section 3.

1.8 **Warnings.** The validator warns that the five statement strings in `visible_text` are long (more than 6 words):
they are the table's row labels, drawn as two lines each, so I left them whole.

## Borderline

- **C171 / C172 (Q4 tick table) as required.** A careful student could decide always / sometimes / never from the text
  alone, and the LP text carries every statement and answer. I kept it required because the v3 rules say a printed
  filled/ticked table that is the answer is a figure (`ANSWER_IS_FIGURE`), the question acts on a given figure
  (`ACTION_ON_FIGURE`), and decision 4 says do not flip it to none because the text has the data. If the user prefers
  text, the fallback is a LaTeX array with the five statements and a tick column.
- **C163 worked example:** none, but a three-column picture "always / sometimes / never" would be the natural
  optional figure if the user ever wants one.
- **Row letters in the Q4 picture** (1.2): not in the book's table.

## 2. LP text issues

- **M4.S37.T37.C171 (Q4 question):** the question does not name the three choices, so the text alone does not say
  what the cells are. Suggested sentence: "Tick one cell for each statement: Always True, Sometimes True or Never True."
- **M4.S37.T37.C171 `question_tex`, statement (e):** the quote marks are mixed up with the maths: `‘$0’$`. Suggested:
  `‘$0$’ in the Ones place`.
- **M4.S37.T37.C172 (Q4 answer text):** the sentence "This is the plan's reading with whole numbers." in step (b) is
  internal wording; suggested "Here we use whole numbers only." Also the old `text` field has `[Image: ...]` markers
  in the middle of the steps (after step 2) and one "(continued)" marker at the end; under v3 the one token goes before
  step 1 and both markers go.
- **M4.S37.T37.C165, C167, C169 (Q3 a, b, c):** the book's red hints "Always true" (a), "Never true" (b),
  "Sometimes true" (c) are not in the LP question text. Left out on purpose (they give the answer); if the user wants
  them, e.g. "Hint: this statement is always true."
- **M4.S37.T37.C167, C169:** the questions (b) and (c) start without the Q3 lead-in "Think about the following
  statements and find examples as suggested below." (only (a) carries it). Fine as separate cards, but (b) and (c) read
  better with "Think about this statement:" at the start.
- **M4.S36.T36.C163:** the question says "(practice values)", which is odd for the student; suggested: "Decide if each
  statement is always, sometimes or never true." Also the lead "Worked example:" in `text` is fine.
- Maths in the chunk was re-checked and holds: Q1 values 72/72 T, 14/21 F, 16/16 T, 80/90 F, 35/35 T; Q2 blanks 25, 3,
  7, 72; the Q3 sample equations; Q4 (a) to (e) answers.

## 3. Places where the book itself is unclear

- The pdf has no printed answers, so every answer follows the LP.
- **Q4 (b) "Changing the order of the numbers in subtraction makes no difference."** For whole numbers the two orders
  differ unless the numbers are equal (6 - 6), and 3 - 8 does not exist in whole numbers; so "sometimes true" (LP) is
  defensible, but many teachers would say "never true". The diagram draws the LP's "Sometimes".
- **Q4 (c) "doubling one number and halving the other keeps the product the same"**: always true mathematically (the LP
  uses even starting numbers so halving stays whole).
- **Q3 red hint arrows:** the book does not say whether they are part of the question or a hint to the teacher; treated
  as hints (not drawn).
