# Class 5 Ch 5 Far and Near - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths5_ch5` v4 (taken from staging). Result: new V2 version v5 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (111 items from 65 units)
{"worked_example": {"none": 15, "required": 2, "optional": 2}, "question": {"none": 29, "required": 17}, "solution": {"none": 29, "required": 16, "optional": 1}}

Optional, NOT added: [('C11', 'solution'), ('C38', 'worked_example'), ('C51', 'worked_example')]

needs_lp_text_sync: []

## The 35 diagrams
| id | side | type |
|---|---|---|
| M1.S4.T4.C8.IMG1 | question | number_line |
| M1.S4.T4.C9.IMG1 | solution | number_line |
| M1.S6.T6.C17.IMG1 | question | object_row |
| M1.S6.T6.C18.IMG1 | solution | object_row |
| M1.S6.T6.C19.IMG1 | question | object_row |
| M1.S6.T6.C20.IMG1 | solution | object_row |
| M1.S6.T6.C21.IMG1 | question | object_row |
| M1.S6.T6.C22.IMG1 | solution | object_row |
| M1.S6.T6.C23.IMG1 | question | object_row |
| M1.S6.T6.C24.IMG1 | solution | object_row |
| M2.S7.T7.C26.IMG2 | worked example | number_line |
| M2.S9.T9.C33.IMG1 | solution | number_line |
| M2.S9.T9.C35.IMG1 | solution | number_line |
| M2.S11.T11.C40.IMG1 | question | cell_grid |
| M2.S11.T11.C42.IMG1 | question | cell_grid |
| M2.S11.T11.C44.IMG1 | question | cell_grid |
| M2.S11.T11.C46.IMG1 | question | cell_grid |
| M2.S11.T11.C48.IMG1 | question | cell_grid |
| M2.S13.T13.C53.IMG1 | question | measurement_scale |
| M2.S13.T13.C54.IMG1 | solution | measurement_scale |
| M2.S13.T13.C55.IMG1 | question | geometry_figure |
| M2.S13.T13.C56.IMG1 | solution | geometry_figure |
| M2.S13.T13.C60.IMG1 | solution | measurement_scale |
| M2.S15.T15.C64.IMG1 | question | number_line |
| M2.S15.T15.C65.IMG1 | solution | number_line |
| M2.S15.T15.C66.IMG1 | question | number_line |
| M2.S15.T15.C67.IMG1 | solution | number_line |
| M2.S15.T15.C68.IMG1 | question | number_line |
| M2.S15.T15.C69.IMG1 | solution | number_line |
| M3.S21.T21.C101.IMG1 | question | number_line |
| M3.S21.T21.C102.IMG1 | solution | number_line |
| M3.S25.T25.C118.IMG1 | solution | measurement_scale |
| M3.S27.T27.C121.IMG2 | worked example | cell_grid |
| M3.S28.T28.C123.IMG1 | question | cell_grid |
| M3.S28.T28.C124.IMG1 | solution | cell_grid |

### Chunk A notes (from the decision agent)
# Chunk A notes (Class 5 Ch 5 "Far and Near", units 1-19, topics M1.S2.T2 to M2.S9.T9)

Result: 32 items = required 13 / optional 1 / none 18. Validator `--chunk A`: errors 0, 3 warnings (C26, C33, C35 are required but their figure is not printed in the book: expected).

Required (13): C8 q and C9 s (sari double number line), C17/C19/C21/C23 q and C18/C20/C22/C24 s (six tallest statues), C26 worked (flags on a 2 km track), C33 s and C35 s (water stations, children on the 3 km race).
Optional (1, not added): C11 s (lines joining the two columns of the sari match).
Media ids: all `<cid>.IMG1`, except C26 = `M2.S7.T7.C26.IMG2` (IMG1 is the kept teaching image).

## 1. Judgement calls and Borderline

Borderline (v3 rules applied as written, user decision 4):

- **C18, C20, C22, C24 (Let Us Compare Q2 a-d, solutions): all four required.** (b), (c), (d) pick out statues of the picture (HIGHLIGHT_MEANING, ANSWER_IS_FIGURE: two statues circled with their gap, a stacked second copy for the doubling). (a) is the weakest: its answer is one number (89 m), and the typical "figure question, numeric answer" pair is Q required / S none. I kept it required because the solution adds a visible mark (highlighted pair + the 89 m gap) and the four parts are one NCERT question set with the same kind of solution figure (sibling consistency). If the user wants fewer images, C18 is the one to drop (`drop_image`, reason SAME_AS_QUESTION_DIAGRAM).
- **Statues drawn as plain columns, not as statues.** The book picture is six sculpture illustrations; the figure carries only names and heights, so each statue becomes a plain rectangle to the book's own scale (checked on the page picture: heights are proportional to the printed metres within 3 percent). Scale 3.9 px per metre; the 2 m gap between Liberty (93) and Motherland Calls (91) is only 8 px, so (b) draws a small bracket and the label beside it.
- **C33, C35 (Kilometre Race Q1, Q2, solutions): required** as ANSWER_IS_FIGURE: the question asks where objects are to be placed along a 3 km track, so the answer is a placement (numbered stations/children on a line from Start to Finish). This is a judgement: the positions are also fully written in the steps, so a stricter reading (tie-breaker: text alone is enough) would make them optional. The book prints no figure for the race, so the question sides are `none` (companion note: do not invent a question figure) and the solutions draw the whole track (`derived_from` null). The LP's `q_figure` hint ("a straight race track of 3 km") describes a picture that is not in the book.
- **C37 (Kilometre Race Q3, solution): none.** Sibling reason: its answer is a count (60 flags, 30 red and 30 blue) and the question does not ask for positions; a picture of 60 flags would be overcrowded and only repeat the arithmetic. Q1 and Q2 ask for positions.
- **C26 (worked example, flags on a 2 km track): required** (same kind of answer as C33/C35: placement of flags along a track). A kept teaching image C26.IMG1 already shows the same track; per user decision 5 it is not a reason to drop and it is not linked. The picture shows the complete final placement. The other five worked examples (C3, C4, C12, C13, C25) are `none`: their steps are pure arithmetic or word reasoning with no figure given (LATEX_ARITHMETIC / TEXT_SUFFICIENT); their teaching images stay.
- **C10 q / C11 s (match the 204 cm... lengths): q none (LATEX_TABLE), s optional.** The book gives a plain 2-column list and asks "find which measures represent the same sari": it does not say join. The answer is five written equalities. A figure with lines joining the two columns would help but is not needed. (The LP `s_figure` hint describes such lines.)
- **C6/C7 (Let Us Find table), C30/C31 (rope table): none** (LATEX_TABLE / TEXT_SUFFICIENT). The question text already lists every row; the filled rope table is plain numbers. If a LaTeX table is wanted, `text_alternative` says what to write.
- **C28/C29 (Measuring Long Distances Let Us Do): none** (OPEN_ENDED). The four tool pictures carry no numbers (added to the inventory as NEW-P03-tools-pictures, DECORATIVE_ONLY). A line "home - tea shop 120 m - school gate 400 m - temple 1,600 m" would help the sample answer but the values are practice values only.
- **C15/C16 (Let Us Compare Q1): none**, the book has no picture for the five rods.
- **C8/C9 (sari double number line): required both**, S derived_from Q. The ticks are drawn exactly to scale for 1, 2, 4, 5, 7 m (the book is only roughly proportional: 72, 146, 71, 145 px gaps measured on the page picture, i.e. 72 px per metre).

Figure inventory choices:
- Base figures claimed (all in my chunk): P01-table-1, P01-double_number_line-2, P02-table-1, P02-labelled_picture-2, P03-table-1. Later uses of a figure by another item are `NEW-<base id>-<suffix>` entries: NEW-P01-double_number_line-2-sol (solution C9), NEW-P02-labelled_picture-2-q2b/q2c/q2d (questions C19, C21, C23) and NEW-P02-labelled_picture-2-sol-q2a..q2d (solutions C18, C20, C22, C24). NEW-P03-tools-pictures is a figure missing from the base (none:DECORATIVE_ONLY).
- No figure is mapped to a concept image: user decision 5 says an item that needs a figure draws its own.
- I checked the `unclear` doubts of the inventory against the page pictures: the double-number-line tick spacing (proportional, see above) and the statue heights (proportional, see above). No base description needed a CORRECTED note.

Book mistakes (user decision 1): none found in this chunk's pictures or printed numbers.

## 2. LP text issues (user decision 2: no text edited, no decision changed because of them)

- **M1.S4.T4.C8** (question): the text lists the labels but not the two arrows, ×2 (100 cm to the first blank) and ×100 (1 m to 100 cm), which only the figure carries; the solution C9 refers to both arrows. Suggested sentence to add (only if the figure is ever missing): "The arrow ×100 goes from 1 m to 100 cm and the arrow ×2 goes from 100 cm to the first blank."
- **M1.S6.T6.C17, C19, C21, C23** (Let Us Compare Q2 a-d, questions): each says only "Look at the picture of some of the world's tallest statues" and carries none of the six names and heights, so the question cannot be solved without the figure. Suggested sentence: "The heights are: Statue of Unity, India, 182 m; Spring Temple Buddha, China, 128 m; Guanyin of Nanshan, China, 108 m; Statue of Liberty, USA, 93 m; The Motherland Calls, Russia, 91 m; Christ the Redeemer, Brazil, 38 m."
- **M2.S9.T9.C32, C34, C36** (Kilometre Race Q1-Q3): the LP hint `q_figure` says "a straight race track of 3 km from the starting point to the finish line"; the book has no such figure (pdf p.4 is text only). No question diagram is made.
- **M2.S9.T9.C33, C35**: the solutions count a station / a child at the finish line (6 stations at 500 m ... 3 km, 10 children at 300 m ... 3,000 m). The book's question does not say whether the finish line counts; the LP choice is followed and drawn.
- **Stale image markers in `text`** of answer concepts, e.g. C7 ("[Image: Let Us Find: Ans1: solution]" after step 6 and "(continued)" at the end), C9, C11 and the other answer concepts: they mark the old card positions in the middle of the steps and after the answer. With the v3 rule (solution token first, before step 1) the old markers must be removed or replaced when the builder writes the new token.
- **M2.S8.T8.C29**: all numbers are practice values (125 steps for 100 m, one step 80 cm): the arithmetic checks (10,000 / 125 = 80; 12,000 / 80 = 150; 40,000 / 80 = 500; 160,000 / 80 = 2,000), no change needed; mentioned only because the question text is the book's open activity.

All other LP solutions in this chunk were recomputed and agree with the book's question and with themselves (Let Us Compare Q1 a-e, Q2 a-d, rope table, race Q1-Q3, sari match, worked examples).

## 3. Where the book itself is unclear

- Kilometre Race: whether the station / child at the 3 km finish line is counted (see above). The LP counts it.
- Double number line (p.1): the tick spacing is only roughly proportional in the print; drawn exactly to scale here. The `×100` arrow runs from the m line (bottom) up to the cm line (top).
- Statue heights (pdf p.2): the names and heights are taken exactly as printed (Statue of Unity 182, Spring Temple Buddha 128, Guanyin of Nanshan 108, Statue of Liberty 93, The Motherland Calls 91, Christ the Redeemer 38); not checked against outside sources.
- Let Us Compare (pdf p.2): "Ritika is comparing the lengths of different rods" has no picture of rods in the book.

### Chunk B notes (from the decision agent)
# Chunk B notes (Class 5 Ch 5 "Far and Near": topics M2.S10.T10 to M2.S14.T14)

Result: 23 items = required 10 / optional 2 / none 11. Validator: errors 0, one warning (C60 solution has no base figure, which is right: the book prints no picture of the drawn lines).

| Role | required | optional | none |
|---|---|---|---|
| question | 7 (C40, C42, C44, C46, C48, C53, C55) | 0 | 2 (C57, C59) |
| solution | 3 (C54, C56, C60) | 0 | 6 (C41, C43, C45, C47, C49, C58) |
| worked_example | 0 | 2 (C38, C51) | 3 (C50, C61, C62) |

## 1. Judgement calls (what I chose and why)

Borderline (as the user asked, listed under one heading):

### Borderline
1. **T11 Q1-Q5 (C40, C42, C44, C46, C48): the station table is `required` on the question side, 5 identical diagrams.** The table is a plain 3-column table of numbers (a LATEX_TABLE candidate), but every question says "look at the stations ... shown in the table" and NONE of the distances is in the question text (only in the book table and the LP hint field `q_figure`). The tie-breaker (could a careful student solve it from the text alone?) is "no", so FIG_REFERENCED + DATA_IN_FIGURE apply. Per the run rules the same book picture gets one diagram per item (identical spec; Q2-Q5 say "same as M2.S11.T11.C40.IMG1"). If the content team would rather put a LaTeX array into `question_tex`, these five can simply be switched to `none` / LATEX_TABLE (the spec is a full cell grid of 8 rows x 3 columns).
2. **T11 solutions (C41, C43, C45, C47, C49): `none` (SAME_AS_QUESTION_DIAGRAM, TEXT_SUFFICIENT).** The LP steps already name the two distances taken from the table and do one subtraction, or read the last row (Q1). Highlighting the rows used would be only a nicety (optional at most), so not added. Sibling consistency: all five treated alike.
3. **T10.C38 worked example: `optional`.** All numbers are in words (Q 340 km, R 615 km); steps are one subtraction. A route line 0 / 340 / 615 km would help but is not needed to follow it. (A teaching image of this exact route already exists; that is not the reason for the decision.) Flip to required if the team wants a figure for every distance example: spec would be a route line with three marked stations and the 275 km gap in ANSWER green.
4. **T12.C51 worked example (ruler line 4 cm 6 mm, draw 72 mm): `optional`.** The reading is given in words ("6th small mark after the 4 cm mark"); 72 mm is a calculation. A ruler would help but nothing must be read from it. Flip to required if the team wants a ruler for every ruler example: one ruler 0 to 8 cm with a line ending on the 6th small mark after 4 cm (do not draw the 72 mm line, it is the answer of the second part).
5. **T12.C50 (pin 3 cm = 30 mm, bead 8 mm), T14.C61 (6 cm, 9 m, 8 km), T14.C62 (7,305 cm, 3 m 7 cm): `none`.** Pure conversions given in words, no figure referred to (LATEX_ARITHMETIC / TEXT_SUFFICIENT). The teaching images (cm over mm, three double number lines, split bar) stay as teaching images.
6. **T13.Q3 sprout table (C57 question, C58 solution): both `none` (LATEX_TABLE, OPEN_ENDED).** The question names Day 1-4 and mm in words; the book table is a plain two-column table with empty cells for the learner's own measurement. The LP solution's "sample answer" (3, 9, 16, 25 mm) is a filled plain table, which I treat as LaTeX rather than ANSWER_IS_FIGURE because it has no colour meaning and is an open answer. `text_alternative` holds the array. If the team reads "filled table = ANSWER_IS_FIGURE", C58 would become required with a 2 x 5 cell grid.
7. **T13.Q1 solution (C54) is `required`.** The LP steps count the 9 small marks "one by one"; the figure is the same ruler with the nine marks numbered 1 to 9 in ANSWER green and a FOCUS bracket under 1 cm to 2 cm. Counting on the figure is an action on the figure (Q required, S required, derived from Q).
8. **T13.Q4 (C59/C60): question `none`, solution `required`.** The question gives only five lengths in words (no figure given: no question diagram). The answer to "draw lines of these lengths using a scale" is the drawn lines (ANSWER_IS_FIGURE), so the solution draws one ruler 0-9 cm and five lines from 0 with GUIDE dashes to the scale. Letters (a)-(e) are drawn because the LP answer refers to the lines by letter (user decision 3).
9. **T13.Q2 solution values are written in mm only** ("48", "35", ... plus the legend "in mm"), not "4 cm 8 mm". The LP's own answer line is "Sample answer in mm: (1): 48; ..."; the cm-and-mm form stays in the LP steps. Reason: at the 34 px minimum text size "4 cm 8 mm" does not fit the small boxes and cannot fit the tiny box (6) at all. Tags "(1)" to "(8)" are drawn in both figures because the LP answer text refers to the lines by number.

Other choices:
- Ruler and design are drawn with CELL_FILL / white because the style tokens have no yellow; the book's ruler is yellow and its boxes are blue (boxes use FOCUS).
- Design geometry (C55/C56): I measured the 16 corners on the page 5 picture (page image 990 px = 211 mm, 4.69 px per mm at printed size) and fitted them so that every corner of an inner shape lies on a side of the shape around it AND the eight numbered lines come out at exactly the LP's lengths: 48.00, 35.00, 60.00, 27.00, 22.00, 19.00, 44.00, 61.00 mm. The raw measurement was 48.1, 35.0, 59.8, 27.0, 21.9, 19.3, 44.0, 60.7 mm, so the LP's sample answer agrees with the book picture. Box (4) is drawn 12.2 mm long instead of 14.5 mm because the book's box touches the diamond; box (6) keeps the book's small size (8.0 x 4.2 mm).
- Aspect ratio 16:9 for everything (the pipeline's card); the long ruler strips are therefore small relative to the card but still above the minimum text size.
- Inventory: P05-ruler-2 (1 cm = 10 mm teaching figure) is mapped to concept image M2.S12.T12.C50.IMG1 (accounting only). P05-ruler-1 and P05-shape-3 are mapped to their question diagrams; their solution uses are `NEW-P05-ruler-1-sol` and `NEW-P05-shape-3-sol`. Further uses of the station table are `NEW-P04-table-1-q2` to `-q5`. P06-table-1 is `none:LATEX_TABLE`; P06-relation_box-2 is a text-only box `none:TEXT_SUFFICIENT`. The sprout / screws / nail pictures on page 5 are decoration and are not in the base inventory.
- The 'Practice' concepts C39, C52, C63 are not units of this chunk and were not touched.

## 2. LP text issues

(Not edited, only listed, as decided.)
- **M2.S11.T11.C40, C42, C44, C46, C48 (questions):** the text says "shown in the table" but gives none of the data. The diagram now supplies the table. Alternative: add a LaTeX array to `question_tex` (header Station number | Name of the station | Distance from Dibrugarh, then the 8 rows 9 Dimapur 306 km, 14 Guwahati 556 km, 22 Jalpaiguri Road 983 km, 34 Bhubaneswar 2,007 km, 40 Visakhapatnam 2,450 km, 45 Vijayawada JN 2,800 km, 55 Coimbatore JN 3,675 km, 65 Kanniyakumari 4,187 km).
- **M2.S11.T11.C48 / C49:** "Coimbatore $JN$" is set in maths italic in `question_tex` and `steps_tex`; JN is a name, suggest plain text (or `\text{JN}`). The other rows write "Vijayawada JN" in plain text.
- **M2.S10.T10.C38:** the first block (textbook text) says "Look at the stations on the route shown in the table below and answer the questions", but no table is attached to C38 (the table is only in the T11 questions). Suggested sentence: "Look at the stations on the route in the table in the questions that follow."
- **M2.S13.T13.C55 (question):** the text says the lines "are numbered from the top of the picture to the bottom", which is only roughly true: line (5) (upper left side of the small tilted shape) sits higher than (3) and (4). The book prints no numbers. Suggested sentence: "The eight boxes are numbered (1) to (8) in the picture." (The diagram now prints these tags.)
- **M2.S13.T13.C55 / C56 (design):** the LP calls the inner shape a "rectangle" and the second shape a "diamond"; in the book picture they are not exact (inner shape sides 35.0 / 27.0 / 34.7 / 28.9 mm; diamond sides 48.0 / 44.9 / 41.2 / 44.0 mm). Harmless for the measuring, but the words 'nearly a rectangle' would be more exact.
- **M2.S13.T13.C56 (solution step 1):** "These lengths were measured on the picture at its printed size, so your ruler may read 1 mm different." On a screen the learner cannot measure at printed size. Suggested sentence: "Measure the design in your book, or check your numbers against these lengths; they may differ by 1 mm."
- **M2.S13.T13.C57 (question):** says "Fill in the table" but no table is in the text. Suggested: add a LaTeX array with the header "Number of days | Length of the sprout (in mm)" and rows Day 1 to Day 4 with empty right cells.
- **M2.S13.T13.C59 / C60:** the LP numbers the five lengths (a) to (e); the book prints 1 to 5. The diagram uses the LP's letters. The book's follow-up "How did you draw lines of lengths 36 mm and 67 mm? Share your thoughts in class." is not in the LP (not a diagram matter).

LP arithmetic checked: C38 615 - 340 = 275; C41 4,187; C43 2,800 - 983 = 1,817; C45 2,800 - 2,450 = 350; C47 556 - 306 = 250 and 2,007 - 983 = 1,024; C49 3,675 - 556 = 3,119; C54 9 marks; C58 3 < 9 < 16 < 25; C60 55, 36, 83, 36 mm, 6 cm 7 mm; C61 60, 900, 8,000; C62 7,305 = 73 m 5 cm, 307 cm. All correct, no contradiction with the book.

## 3. Places where the book is unclear

- Page 5 design: eight boxes stand beside sixteen lines; which line a box measures is shown only by closeness (no arrows). I followed the LP's list. The box beside the diamond's right corner and the rectangle's right side (LP line 4) touches the diamond line in the book.
- Page 5 ruler: the left edge is the 0 mark (0 is not printed) and the right edge is at about 8.03 cm (no numeral). The book's ruler picture is drawn about twice life size, so its "cm" is not a real centimetre of the page; this does not matter for counting marks.
- The printed size of the design depends on the printing (4.69 px per mm was taken from the 990-px page image of a 211 mm wide page). The LP's lengths agree with that scale to within 0.3 mm.
- No printed solutions section exists in this pdf; all solution diagrams follow the LP solution text.

### Chunk C notes (from the decision agent)
# Notes, chunk C (Class 5 Ch 5 "Far and Near", cbse_eng_maths5_ch5_v4)

Units: M2.S15.T15 (Let us do: Q1 to Q6), M3.S16.T16 (Adding and Subtracting Lengths, 2 worked), M3.S17.T17 (Examples 1 and 2), M3.S18.T18 (Let us do: Q1 to Q5), M3.S19.T19 (Multiplying and Dividing Lengths, 3 worked).
Result: 31 items, required 6 / optional 0 / none 25. Validator: errors 0, warnings 0.

## 1. Judgement calls

- **Required (6 items): Let Us Do Q1 (a), (b), (c) double number lines, question and solution** (M2.S15.T15.C64/C65, C66/C67, C68/C69). The book gives each as a double number line with 7 ticks and four arrows; the picture alone shows which labels are given or blank and which two arrow boxes are printed (x7 / x4 / x9 on top, x10 / x100 / x1,000 on the left) and which two are empty (right arrow and bottom arrow). The learner fills the blanks, so the question side is `FIG_REFERENCED + DATA_IN_FIGURE + ACTION_ON_FIGURE`. The solution is the completed line (`ANSWER_IS_FIGURE`), `derived_from` the question figure, added values in ANSWER green.
- **Which empty box is which.** From the LP steps and the arithmetic: the right-hand arrow (top tick 2 down to bottom tick 2) is the unit-change multiplier (x10, x100, x1,000); the arrow under the bottom line (bottom tick 1 to tick 2) repeats the top multiplier (x7, x4, x9). The LP answer line "Boxes: x7, x10" does not say which box gets which; I follow the LP steps ("the arrow on the bottom line ... is also x7", "the box on the arrow from the top line to the bottom line is x10").
- **Letters (a), (b), (c) are not drawn** (user decision 3): each figure is its own item and the LP answer text never refers to a figure by letter.
- **Book print slip, Q1 (a), corrected in the specs (user decision 1).** The book prints the unit "m" after the last blank of the bottom line (under the 50 cm tick). The bottom line is in mm and 50 cm = 500 mm (the LP solution step 5 says the same). Both the question figure (blank followed by "mm") and the solution figure ("500 mm") use mm. Page 7 of the book, figure (a); the base inventory still records what the book prints.
- **Tick spacing is equal** in the specs. The book's ticks are unevenly spaced (not to scale) and the spacing carries no meaning.
- **Q2 to Q6 conversions (T15 C70 to C75): none.** Plain fill-in-the-blank conversions, no book figure; the red hints beside (b) and (h) are text callouts and I did not list them as figures.
- **Saji (C79/C80) and cable (C81/C82): none on both sides.** The question sides give no figure (word problems). The book's column addition and subtraction pictures are the worked answer; I mapped all four base figures (P08-column_addition-1 and -2, P09-column_subtraction-1 and -2) to `none:LATEX_ARITHMETIC` (the v3 NONE rules name column addition and subtraction, and header boxes km/m or cm filled with digits are `HEADER_BOXES_ONLY`). The LP steps state every carry and regroup.
- **Let us do: Q1 to Q5 of T18: none.** Word problems and a list of length pairs; the book's only picture here is a photograph of the Gulmarg cable car (decoration, so not a base figure; it is not a NEW- entry).
- **Worked examples C76, C77, C93, C94, C95: none.** Practice values (not in the book), no figure referenced by the question, all numbers in the steps. I decided on the rules, not because a teaching image already exists (user decision 5 would forbid that reason).
- **P11-double_number_line-1 (page 11, cloth price, "Multiplying and Dividing Lengths") is NOT claimed in this chunk.** It is the given figure of the questions M3.S21.T21 (md.line, C101/C102) in chunk D, and none of my units use it (T19 holds only practice-value worked examples). If the merge needs it from two chunks, the meaning should be `item:M3.S21.T21.C101 (question)`.
- Inventory: 10 entries = 3 base figures (P07 a, b, c) mapped to the question items, 3 `NEW-P07-double_number_line-N-sol` entries mapped to the solution items (the same book figure is used a second time, as the filled answer), 4 column figures mapped `none:LATEX_ARITHMETIC`. All base descriptions were checked against pages 7, 8 and 9 of the book: they match (the m-for-mm slip is noted above); no "CORRECTED:" entries.

## 2. LP text issues

- **M2.S15.T15.C64 (question, Q1 (a)), also C65's `question` copy:** the last bottom-line blank is written `___ m` in `question`, `question_tex` and `text`. It should be `___ mm` (50 cm = 500 mm). Suggested: "Bottom line: 10 mm, ___ mm, ___ mm, 250 mm, 320 mm, 450 mm, ___ mm." (The solution step 5 already says "Your maths book prints m under this tick, but 50 cm is 500 mm", so it can stay or be shortened.)
- **M2.S15.T15.C64, C66, C68 (question and the copy in C65, C67, C69):** "Fill in the two boxes x___ as well: the arrow on the top line is x7 and the arrow from the top line to the bottom line is x10." does not say that x7 and x10 are already printed and which two boxes are empty. Suggested for (a): "The top arrow is x7 and the left arrow is x10. Fill in the two empty boxes x___ as well: the right arrow from 7 cm down to the bottom line, and the arrow along the bottom line." (for (b) use x4 and x100, for (c) x9 and x1,000).
- **M2.S15.T15.C65, C67, C69 (`answer` / `answer_tex`):** "Boxes: x7, x10" (and "x4, x100", "x9, x1,000") does not say which box is which. Suggested for (a): "Boxes: x10 on the arrow from 7 cm down to 70 mm, and x7 on the bottom-line arrow from 10 mm to 70 mm."
- **M2.S15.T15.C72, C73:** item (i) is written "(i): ..." without the `$...$` that (e) to (h) use (`$(e)$`). Formatting only.
- **LP numbering differs from the book's:** LP "Let us do: Q4, Q5, Q6" (T15) are the book's Q2 (a) to (d), (e) to (i), (j) to (n); LP "Q1 to Q3" are Q1 (a) to (c). In T18, LP "Q4" and "Q5" are the book's Q4 (a) to (d) and Q4 (e) to (g). The `book_number` fields are right; only the concept names differ.
- **M3.S17.T17.C79:** the book's "Share your thoughts in class" is left out; harmless.
- **M3.S17.T17.C80 and C82 (answers with the column picture removed):** the LP `s_figure` hints describe a column picture ("a carried 1 into the km column", "the borrowed digits marked"); with the decision none the LaTeX steps must carry this. They do (regroup 1,100 m = 1 km 100 m; 63 m = 6,300 cm). If the column layout is wanted as LaTeX, the text alternatives are in the items.
- No wrong arithmetic found: I recomputed every LP answer of T15 to T19 (3 m 75 cm + 2 m 25 cm = 6 m; 48,700 - 17,900 = 30,800 m; 2,300 + 2,650 = 4,950 m; Q4 differences 1, 6, 1, 20 mm and 45 cm, 322 m, 1 m; 6,300 - 1,675 = 4,625; 12 x 240 = 2,880; 18,900 / 3 = 6,300; 90 / 3 = 30).

## 3. Borderline

- **Q1 (a), (b), (c) question side, required** although the LP text lists all numbers (user decision 4): kept because the book gives a figure and the learner acts on it.
- **C80 and C82 solutions (Saji and cable column pictures), none.** The reader could argue "printed answer is a picture" (Step B2) or `HIGHLIGHT_MEANING` (circled carries, struck digits). I followed the explicit NONE rules (column addition and subtraction = LaTeX; header boxes with digits = not an image). These are the first items to flip to required if the team wants the book's regroup pictures. If flipped, the picture would be a column layout with header boxes km | m (or cm / m | cm), the carry oval, struck digits and the red notes, and P08-column_addition-1/-2, P09-column_subtraction-1/-2 would map to those solution items.
- **C76 worked example (2 km 700 m + 1 km 800 m), none** by the same rule: a column addition. Its kept teaching image shows a column layout, but that is not the reason.
- **C95 worked example "Price of a Length: Double Number Line", none.** The question does not reference a figure and the arithmetic is in the steps; a double number line (3 m, 6 m, 9 m over Rs 90, 180, 270, arrow x3) would clearly help. This is the item most likely to be wanted as required. (The kept teaching image C95.IMG1 shows exactly that; not the reason for none.)
- **C77 worked example (ribbon cut), none.** A tape model would only repeat the steps.
- **C85 Bhopal, waterfall and Sanchi, none.** A route strip with three marked points would not change how the learner solves it.
- **C89 and C91 (Q4 "circle the bigger length"), none.** The circling is done on a plain list of pairs and the LP answer names the bigger length.

## 4. Where the book itself is unclear

- Q1 (a): the printed unit "m" under the 50 cm tick (a print slip, see above).
- Q1: the four arrows and the two empty "x__" boxes are not named in the book; their values come from the arithmetic (the right arrow changes the unit, the bottom arrow repeats the top multiplier).
- Page 9, second cable picture: the left half has an empty result row and the right half the filled one; the regrouped "1" of 100 cm sits in the first cm column with nothing under it in the second row (the base figure notes this). Not drawn (none).
- Page 8, Saji's first picture: the result row prints six characters over four digit columns (7, boxed 1, 1, struck boxed 1, 0, 0); the role of each is read from the arrows only. Not drawn (none).

### Chunk D notes (from the decision agent)
# Notes for chunk D (Class 5 Ch 5 "Far and Near", topics M3.S20.T20 to M3.S28.T28)

Result: 25 items, required 6 / optional 0 / none 19. Validator: errors 0, one warning (C121, see below).

Required: C101 question + C102 solution (double number line), C118 solution (inch ruler), C121 worked example (3 x 3 sign grid), C123 question + C124 solution (4 x 4 sign grid).

## 1. Judgement calls

- **C101 / C102 double number line (p.67).** Both required. The book prints only THREE multiplier boxes (the long right arrow from 10 m down to the second rupee tick has none); the LP text says "the four boxes" and its solution fills four (x2, x20, x2, x20), and the page 7 double number lines have four. Per the user's decision 1 the specs show FOUR boxes. The book's tick spacing is not to scale; the spec uses equal spacing. The decorative shopping bags are left out.
- **C118 inch ruler (solution only).** The base inventory calls P12-ruler-3 a "teaching figure", but it is the book's answer to the question (bracket of 1 inch ending at 2 cm 5 mm), so by B2 (printed answer is a picture) the solution is required and the figure is mapped to the solution item. The question has no given figure ("look at YOUR ruler"), so the question side is none and the solution diagram has `derived_from` null. I added a "0" numeral that the book does not print (the LP step says to put the 0 of the scale at the start), and the tags "2 cm" and "5 mm" (words of the LP step, 2 words each) next to the book's "1 inch" bracket.
- **C121 worked example, 3 x 3 sign grid.** Required, with its own figure although the kept teaching image C121.IMG1 shows the same grid (user rule 5). A worked example carries ONE picture after the question text, so it draws the GIVEN grid (three signs on the main diagonal). The filled grid stays in the steps and answer. media id is C121.IMG2 (IMG1 is the kept image). This grid is an LP practice grid, not a book figure, so no inventory figure maps to it (hence the validator warning, which is fine for a figure not printed in the book).
- **C123 / C124 Try This.** Both required (given grid; answer is the filled grid). The question figure is the plain book grid (no box dividers). The solution grid is the LP's grid; I checked it: every row, every column and each of the four 2 x 2 corner boxes holds the four signs once, and the five given signs sit where the book prints them.
- **S20, S21 Q3 and Q4 (shirts, bags, Anita, road).** All none: word problems with every number in the text, and the printed working is plain arithmetic (LATEX_ARITHMETIC). The book's cloth-rolls photo and sari-border picture are decoration; I added them to the inventory as NEW- figures mapped to DECORATIVE_ONLY.
- **S23 Let Us Estimate Q1 to Q3 and S26 Measure Your Height.** None on both sides: open questions about the learner's own neighbourhood or class, no given figure, and the sample answers (practice values) are a number or a short method. The two book pictures on p.68 (house with three stacked children, pole with ladder) and the child at the wall scale on p.69 carry no data and no question refers to them; mapped to DECORATIVE_ONLY.
- **Inventory:** the solution diagrams C102 and C124 are second uses of P11-double_number_line-1 and P13-grid-2, entered as `NEW-<base id>-sol` as the brief asks; P12-ruler-3 maps to its solution item (not to a concept image).

## 2. Anything in the LP that looks wrong

- The cards of the old answer concepts C102, C114, C120 and C124 have two images each and the solution `text` has "[Image: ...]" markers in the middle of the steps and at the end; the new single token goes before step 1 (the builder handles this).
- C112 (tree estimate): stacking friends on each other's shoulders gives a little less than the sum of their heights, but the LP treats it as 8 x 150 cm; fine as a practice model (the book's own house picture stacks children the same way).
- C124 steps_tex and answer_tex: stray spaces before commas and full stops after \times and \div (for example "$\times$ ." and "row $1 \div$ , $-$"); formatting only.
- All other numbers checked and correct: C98 (36 m), C100 (₹20), C102 (₹200, ₹400, ₹800, 100 m), C104 (10 m, ₹500), C106 (2 km 100 m), C115 (54 inches, 2 feet 6 inches), C118 (25 mm), C120 (51, 55, 53), C121 and C124 grids.

## 3. Where the book itself is unclear or slips

- p.67 double number line: three multiplier boxes printed, four needed (see above); tick spacing not to scale.
- p.69 Try This: "each 4 x 4 box" is a print slip (the picture is one 4 x 4 grid); the LP's "2 x 2 box" is right and is followed in the spec.
- p.69 Try This: the book does not mark the four 2 x 2 boxes; a reader could take "each 2 x 2 box" to mean any 2 x 2 window, but only the four corner boxes hold the four signs in the LP's answer.
- The pdf has no printed solutions, so the filled figures come from the LP solutions.

## Borderline

- **C107 worked example (estimating with a door).** none (TEXT_SUFFICIENT): every number is in the text and no figure is referred to. A wall with two doors stacked would help, and the kept teaching image C107.IMG1 shows it. If you want the example illustrated, flip to required: a wall about 4 m high, a door about 2 m high beside it, two doors stacked reaching the top.
- **C110, C112, C114 (sample answers of Let Us Estimate).** none: practice-value numbers are in the text. A stack-of-references picture (5 floors of 3 m; 8 friends of 1 m 50 cm; a rope lowered into a well) would only make them nicer.
- **C119 question (child at a wall scale).** none: the picture is an illustration of the activity; the LP's `q_figure` hint was not followed because the question gives no data in a figure.
- **C120 solution.** none: three heights changed to inches and compared; a bar picture would be nicer, not needed.
- **C104 solution (Anita).** none: a strip of 500 cm cut into 10 pieces of 50 cm is possible, but it is division written in LaTeX.
- **C115 worked example (feet and inches).** none: arithmetic; the teaching image C115.IMG1 stays.
- **C121 worked example.** required but draws the given grid only, not the filled one (one picture per worked example, placed after the question).

## LP text issues

- **M3.S28.T28.C123**: the text says "each row and column and each 2 x 2 box" without saying which boxes. Suggested sentence: "...such that each row, each column and each of the four 2 x 2 corner boxes (top left, top right, bottom left, bottom right) does not repeat the sign."
- **M3.S28.T28.C124**: formatting nits in steps_tex, answer_tex and text (spaces before commas and full stops after \times and \div, see section 2).
- **M3.S21.T21.C101**: the text asks for "the four boxes" and does not say where they are; the figure carries them (above the top line, left arrow, below the bottom line, right arrow). If the figure is ever not shown, suggest adding: "The four boxes are on the arrow from 5 m to 10 m, the arrow from 5 m down to ₹100, the arrow from ₹100 to the next amount, and the arrow from 10 m down to the second amount."
- **M3.S25.T25.C118**: step 1 mentions an inch scale on the other ruler edge, but the figure (as in the book) shows a cm ruler with a 1 inch bracket beneath it and no inch scale; no change needed, noted for the reviewer.
- **M3.S26.T26.C119**: `q_figure` describes a wall chart picture that the plan does not draw (decision none); nothing in the question text depends on it.
