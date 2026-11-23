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
