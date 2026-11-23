# Class 8 Ch 12 Tales by Dots and Lines - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths8_ch12` v24 (taken from staging). Result: new V2 version v25 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (99 items from 61 units)
{"worked_example": {"none": 18, "required": 4, "optional": 1}, "question": {"none": 25, "required": 13}, "solution": {"none": 28, "required": 6, "optional": 4}}

Optional, NOT added: [('C17', 'solution'), ('C20', 'solution'), ('C68', 'solution'), ('C78', 'solution'), ('C98', 'worked_example')]

needs_lp_text_sync: [('C62', 'solution'), ('C79', 'question')]

## The 23 diagrams
| id | side | type |
|---|---|---|
| M1.S4.T4.C15.IMG1 | question | data_graph |
| M1.S4.T4.C15.IMG2 | solution | data_graph |
| M1.S4.T4.C17.IMG1 | question | data_graph |
| M1.S4.T4.C18.IMG1 | solution | cell_grid |
| M1.S4.T4.C20.IMG1 | question | data_graph |
| M1.S11.T11.C47.IMG1 | question | data_graph |
| M1.S13.T13.C51.IMG2 | worked example | cell_grid |
| M1.S13.T13.C52.IMG2 | worked example | cell_grid |
| M1.S14.T14.C54.IMG1 | question | cell_grid |
| M1.S14.T14.C55.IMG1 | solution | cell_grid |
| M2.S15.T15.C57.IMG2 | worked example | data_graph |
| M2.S16.T16.C61.IMG1 | solution | data_graph |
| M2.S17.T17.C62.IMG1 | solution | data_graph |
| M2.S19.T19.C67.IMG1 | question | data_graph |
| M2.S19.T19.C69.IMG1 | question | data_graph |
| M2.S20.T20.C71.IMG1 | question | data_graph |
| M2.S20.T20.C72.IMG1 | question | data_graph |
| M2.S22.T22.C77.IMG1 | question | data_graph |
| M2.S22.T22.C79.IMG1 | question | data_graph |
| M2.S22.T22.C80.IMG1 | solution | data_graph |
| M2.S23.T23.C81.IMG1 | question | data_graph |
| M2.S23.T23.C82.IMG1 | question | data_graph |
| M2.S25.T25.C89.IMG2 | worked example | data_graph |

### Chunk A notes (from the decision agent)
# Notes, chunk A (topics M1.S2.T2 to M1.S7.T7), Class 8 Ch 12 "Tales by Dots and Lines"

Result: 29 items from 17 units. Required 5 (Q2 question + solution, Q4 question, More Q1 solution, More Q7 question), optional 2 (Q4 solution, More Q7 solution), none 22. Validator `--chunk A`: errors 0, warnings 0.

Required diagrams and media ids:
- M1.S4.T4.C15.IMG1 (Figure it Out Q2, the dot plot with the missing dot) and M1.S4.T4.C15.IMG2 (the same plot with the dot at 16, derived_from IMG1)
- M1.S4.T4.C17.IMG1 (Figure it Out Q4, the three album dot plots A, B, C)
- M1.S4.T4.C18.IMG1 (More Q1 solution, two filled 3 by 3 grids with the line totals 30; the question has no figure)
- M1.S4.T4.C20.IMG1 (More Q7, the dot plot of 25 values)

## 1. Judgement calls

- **Worked examples C2, C3, C4, C5 (T2) and C21 (T5): all `none` (TEXT_SUFFICIENT).** Every number is in the LP steps, and each concept already keeps its own teaching picture (C2.IMG1, C3.IMG1, C4.IMG1, C5.IMG1, C21.IMG1) that shows the same dot plot. In the book these pictures are teaching figures ("illustrated below"), not figures attached to a boxed worked example; the LP turned the prose into worked examples. A drawn copy would duplicate the kept concept image. Listed under Borderline.
- **Q2 (C15) question required, solution required.** The book gives the dot plot with the mean line at 9 and asks to mark the missing dot, so the plot is needed to attempt it (ACTION_ON_FIGURE) and the answer is a drawn dot (ANSWER_IS_FIGURE). The solution adds only the dot at 16 in ANSWER green; the distance check (5 + 2 + 1 + 1 = 9 and 2 + 7 = 9) stays in the LP steps.
- **Q4 (C17) question required.** The LP question gives no song lengths for albums B and C; they exist only in the book's picture. All three plots are drawn on the same 0 to 7.5 axis. I positioned the quarter values (5.25, 5.75, 0.75, 3.75, 4.25) by zooming into the page: they sit halfway between the half-unit grid lines, and plot A adds to 39, so the mean 5.57 confirms it. Letters A, B, C are drawn because the LP answer says "Album A" (decision 3). The book's small empty answer boxes beside the letters are not drawn.
- **Q4 and More Q7 solutions `optional`, not added.** Both answers are numbers worked out in text (39 / 7 = 5.57; 443 / 25 = 17.72). A mean line on the plot would help, but it would add numbers the LP does not state (means of B and C are not in the LP; the 17.72 line is in the LP, but the answer is not a picture). Sibling consistency: the two dot-plot questions with a numeric answer get the same decision.
- **More Q7 (C20) question required, drawn as dots.** The LP question lists the counts, but the book question points at "the data shown in the dot plot below" (decision 4: not flipped to none because the LP carries the numbers). The book prints blue x marks and no grid; I specified dots (the LP says "dots") and no grid, and say so in `render_note`.
- **More Q1 (C18) question `none`, solution required.** The book's picture is an empty 3 by 3 grid with no number; the LP question already says "a 3 by 3 grid". A blank grid carries nothing and the companion note says a blank image is worse than none. The solution's answer is itself a filled grid, so it is required (ANSWER_IS_FIGURE) and stands alone (derived_from null). It shows both grids of the LP steps: (i) 7, 12, 11 / 14, 10, 6 / 9, 8, 13 and (ii) the same grid reflected in its main diagonal (7, 14, 9 / 12, 10, 8 / 11, 6, 13), with the six changed cells shaded MARK_FILL and the 16 line totals of 30. Labels (i) and (ii) are shown because the LP steps refer to part (ii). Every row, column and diagonal sum was recomputed for both grids (all 30; the nine numbers of (i) are distinct; six cells differ).
- **Kushti example (C25/C26): `none`.** The book's picture (P07-notebook_list-1) is a handwritten list of nine numbers with a smudge and a circled "Avg 39.2"; the LP question lists all nine weights and the mean, so the list goes in text (NUMBER_LIST_IN_BOXES). Coconut example (C27/C28): the only picture is three palm trees (decoration).
- **T3 pairs (C9 to C14), T4 C16 and C19, T7 pair: all `none`.** Arithmetic, algebra or word questions; the book prints no figure, except C9 where the book's two hint dot plots are covered by concept image C6.IMG1.
- **Figures of book pages 1 to 7 are claimed in this chunk.** Topic T1 has no unit in any chunk, but T2's first paragraph (C2 block 0) carries the prompts of pages 1 to 3, so I claimed all 26 base figures of pages 1 to 7. The "Calculate and mark the mean" and "Mark the mean" plots (P01-dot_plot-2..5, P02-dot_plot-1..4) and the explore plot (P04-dot_plot-1) are `none:OPEN_ENDED` because the LP has no item for them. One extra entry, `NEW-P11-dot_plot-2-sol`, accounts for the Q2 solution figure (not printed: this pdf has no solutions section).
- **Concept-image accounting** (no link): P01-1 to C1.IMG1; P02-7 to C2.IMG1; P02-8 to C3.IMG1; P03-3 to C4.IMG1; P04-3, P04-4, P05-1 to C6.IMG1; P06-2 to C21.IMG1.
- **T9 note for the merge:** the teaching topic M1.S9.T9 (frequencies, book p.8) has no unit either, and is in none of the three chunk lists in meta.json. Its figures (P08-table-1, P08-dot_plot-2, P08-table-3 and maybe P09-table-1) are not claimed here; whoever merges should check they are claimed by chunk B.

## 2. LP text issues

- **M1.S3.T3.C9 / C10 (Relatively Unchanged).** The question asks for the mean, the mean after adding 10 and the mean after doubling, but the solution also works "every value minus 1" and the answer says "6.18 after subtracting 1". Suggested question sentence: "...then the mean when every value is increased by 10, when every value is decreased by 1, and when every value is doubled." (The book's own "reduce every value by 1" plot is applied to the +10 data, mean 16.18; the LP applies it to the original data, 6.18. Both are correct.)
- **M1.S3.T3.C11 / C12.** Subscripts are missing in LaTeX: `$x1$, $x2$, … $xn$` should be `$x_1$, $x_2$, \ldots, $x_n$`, and in the question `mean is a` should be `mean is $a$`.
- **M1.S4.T4.C16 (Q3, shoes).** The answer says "option (d)" but the question text does not list the options (a) to (g) of the book. Suggested addition to the question: "(a) 174.2 cm (b) 126.2 cm (c) 150.2 cm (d) 149.2 cm (e) 151.2 cm (f) None of the above (g) Insufficient information".
- **M1.S4.T4.C17 (Q4, albums).** The question text gives no data for albums B and C (they are only in the picture), so it depends on the figure; the plan's video metadata also has `final_answer.spoken` = "album eigh" (should be "album A").
- **M1.S4.T4.C15 to C20 (the six Figure it Out singles): wrong `book_number`.** All six carry "Figure it Out, Q1"; the correct numbers are Q2, Q3, Q4 (chapter-end part 5.1) and Q1, Q5, Q7 (the second Figure it Out, "More on Mean and Median"). The concept names ("Mean and Median, Q2", "More on Mean and Median, Q1", ...) are right.
- **M1.S5.T5.C21 (worked example, median).** The question gives only "a data set has median 8", not the data. The book's data is 4, 7, 8, 12, 14 (median 8); including 11 gives 4, 7, 8, 11, 12, 14. Suggested sentence: "The data 4, 7, 8, 12, 14 has median 8. Include the value 11 and find the new median."
- **M1.S2.T2.C2 block 0.** The paragraph says "Calculate and mark the mean of each collection of data below" and "Mark the mean for the collections below", but none of the eight collections (book p.1 and p.2) is given in the LP text, so the sentence points at nothing. Suggested: either list the data (6, 7, 8 / 3, 6, 9 / 2, 4, 9 / 4, 11, 15 / 11, 13, 17, 19 / 5, 6, 15, 16 / 10, 10, 11, 17 / 3, 5, 10, 12) or drop the sentence.
- **M1.S2.T2.C2 (worked example).** The LP tries 13 and 11 as other centres; the book's picture uses 12.5 and 11. Both are mathematically right; the LP numbers are the ones the text uses.
- **Small LaTeX slips:** M1.S7.T7.C30 `$41s$` should read `$41$s` (or "the two $41$s"); M1.S3.T3.C13 question uses `(i):` with a colon.
- Arithmetic of every LP solution in this chunk was recomputed and is correct (349, 392, 43; 384, 381, 25.4; 61 / 5 = 12.2; 66 / 6 = 11; 79 / 11 = 7.18; 1275, 2500; 443 / 25 = 17.72; the grids; the median 41).

## 3. Where the book itself is unclear

- P02-dot_plot-8 (mean 7.5) uses the data 2, 6, 10, 12, while the unmarked "Mark the mean" plot above it (P02-dot_plot-4) uses 3, 5, 10, 12; both have mean 7.5. The base inventory already noted this.
- The book gives the quarter dot positions of Figure it Out Q4 only by position between grid lines; confirmed by the zoomed pictures and by the mean of plot A.
- Book print slips: none found in the figures of this chunk (the book axis of Q2 runs a little past 16, to about 17, which the spec follows).

## Borderline

- **Worked examples C2, C3, C4, C21 and C5 (none).** The book prints a dot plot that mirrors each example (P02-dot_plot-7, P02-dot_plot-8, P03-dot_plot-3, P06-dot_plot-2; for C5 the book uses other data), and a distance-arrow dot plot would be the natural picture. I chose `none` because the LP text carries every number and the kept concept image of the same concept shows the figure. If the user wants them, the specs would be: C2 dots 10, 10, 11, 17 with the mean line at 12 and arrows 2, 2, 1 | 5; C3 dots 2, 6, 10, 12 with the line at 7.5 and arrows 5.5, 1.5 | 2.5, 4.5; C4 the before and after plots of 5, 5, 10, 24 with 17 added (11 to 12.2); C21 dots 4, 7, 8, 12, 14 and the new 11 (median 8 to 9.5).
- **Q4 and More Q7 solutions (optional, not added).** See section 1.
- **More Q1 question (none).** Empty 3 by 3 grid in the book, no data in it (ACTION_ON_FIGURE could be argued for "fill the grid").
- **Kushti question C25 (none).** The book's notebook picture is referred to ("as shown") but the LP text carries every weight; a handwritten list of numbers is a plain list.
- **More Q7 question (required)** although the LP lists the counts, per decision 4.

### Chunk B notes (from the decision agent)
# Notes for chunk B (Class 8 Ch 12 "Tales by Dots and Lines", plan cbse_eng_maths8_ch12_v24)

Chunk B = topics M1.S8.T8 (nine Figure it Out singles), M1.S10.T10 (two family-size examples), M1.S11.T11 (FiO1 Q10), M1.S12.T12 (FiO1 Q11), M1.S13.T13 (two spreadsheet worked examples), M1.S14.T14 (spreadsheet cells pair). 30 items: required 3 / optional 0 / none 27. Validator: errors 0, warnings 0.

Required diagrams:
- `M1.S11.T11.C47.IMG1` (question): dot plot of cycle rides, 42 dots, stack heights 3, 1, 4, 7, 7, 5, 4, 6, 3, 0, 2 at values 0 to 10.
- `M1.S14.T14.C54.IMG1` (question): spreadsheet snapshot, columns A to H, rows 1 to 8.
- `M1.S14.T14.C55.IMG1` (solution, derived from C54.IMG1): the same grid with E5 and B3:G3 highlighted.

## 1. Judgement calls

- **FiO1 Q10 question (C47): required.** The LP question text gives no counts (only "four students rode twice"); every count lives only in the dot plot. I re-counted the plot on `page_13.png` (zoomed): 3, 1, 4, 7, 7, 5, 4, 6, 3, 0, 2 = 42 dots; this agrees with the LP solution (42 students, 193 rides, mean about 4.6, median 4) and with the question's "four students rode twice".
- **Axis labels of the Q10 plot.** The book labels only 0, 2, 4, 6, 8, 10. I label every whole number 0 to 10 so the odd columns (1, 3, 5, 7, 9) can be read. No values were invented. The dots use SET_A blue instead of the book's teal.
- **FiO1 Q10 solution (C48): none** (`LATEX_ARITHMETIC`, `SAME_AS_QUESTION_DIAGRAM`). The LP solution lists every count read from the plot and then only does arithmetic and judges statements; it marks nothing on the figure and the book has no printed answer.
- **Family-size examples (C43 to C46): all none.** The book's Number / Frequency tables (vertical and horizontal) are plain tables (`LATEX_TABLE`); the question text already carries the values. The solutions are arithmetic and running totals.
- **Book dot plot P08-dot_plot-2 accounted as the teaching image `M1.S9.T9.C40.IMG1`** (title "Every family counted: the mean is 5.22", dots plus the balance point). It is a figure beside the working, not an answer picture, so no item diagram. Note the book slip below.
- **FiO1 Q11 (C49): none both sides.** The book table is a plain two-row table (`LATEX_TABLE`), the dartboard drawing is decoration (not in the base inventory, not added).
- **FiO1 Q6 to Q9 and FiO3 Q2, Q3, Q4, Q6, Q8 (C31 to C39): none both sides.** I looked at pages 13, 25, 26 and 27: none of these questions has a printed figure (the 3 x 3 grid on p.25 belongs to FiO3 Q1 and the dot plot on p.26 to FiO3 Q7, both in another chunk). FiO3 Q3 and Q4 print the row with blanks as text, not as drawn boxes, so no `NUMBER_LIST_IN_BOXES` / picture.
- **FiO3 Q2 (C35):** open-ended ("give two examples"); the LP gives sample lists in text. No picture.
- **Spreadsheet worked examples C51, C52: none** (`TEXT_SUFFICIENT`). Marks, sums and the formulas are in the text; concept images `C51.IMG1` (=SUM(B3:G3)) and `C52.IMG1` (=AVERAGE(B7:D7)) already show them and a teaching image is never linked. See Borderline.
- **Spreadsheet cells question (C54): required** (`FIG_REFERENCED`, `DATA_IN_FIGURE`): the question names no marks or labels in words; Farooq's row, the Maths column and Nagesh's row exist only in the snapshot.
- **Spreadsheet cells solution (C55): required** (`HIGHLIGHT_MEANING`). See Borderline. No text is added (no "E5" or "B3:G3" label drawn): the answer is shown by tinting the cell, the range and the column letters / row numbers that give the address. Given text stays INK; only fills and FOCUS outlines are added.
- **Column headings of the spreadsheet** are drawn as printed on p.10: Odia(R1), Telugu(R2), English(R3), Maths, Social, Science, Total. The LP text writes them without (R1) etc. A few cells are bold in the book screenshot (Ratna, Farooq, G2 = 37, D3 = 48) with no meaning; I draw everything regular so nothing looks highlighted. The book crop leaves the bottom border of row 8 open; closed in the redraw.
- **Inventory entries:** the P10 picture is used twice (question and solution), so the solution gets `NEW-P10-spreadsheet-1-sol`. P09-table-1 (the 22-row marks table, teaching figure) is `none:LATEX_TABLE`: no item of this chunk uses more than its first seven rows, which the snapshot shows.

## 2. Borderline

- **C55 (spreadsheet solution) required vs none/optional.** The answer is a cell address and a range, not a number. Step E lists "a highlighted part" as something visual a solution may add, and the figure ties the address E5 to column E and row 5, which is the point of the question. The text alone does carry the whole answer, so a stricter reading gives `optional`/`none`. Kept `required` per decision 4 (v3 rules as written).
- **C51 and C52 (spreadsheet worked examples) none vs required.** The cell addresses B3:G3 and B7:D7 are not given in the worked-example question; they come from the teaching text of C50 and the concept images. A reader could ask for a spreadsheet picture here (`DATA_IN_FIGURE`). I chose none because the text/LaTeX default holds, the concept images already show these exact formulas, and the two examples are kept consistent.
- **C48 (Q10 solution) none vs optional.** A dot plot with the mean 4.6 and the median 4 marked would be a nice extra, but the LP solution does not refer to marks on the figure.
- **C44 (Example 1 solution):** the book prints the family-size dot plot beside the working. Called none because the plot is already the teaching image of C40 and the arithmetic needs nothing from it.

## 3. LP text issues

- **M1.S8.T8.C31 to C39 (all nine):** `item.book_number` is "Figure it Out, Q1" for every block, but the questions are FiO1 Q6, Q7, Q8, Q9 and FiO3 Q2, Q3, Q4, Q6, Q8 (the LP's own `lp_text` and card titles say the right numbers). Suggested: "Figure it Out, Q6", "Q7", ..., "Q8".
- **M1.S8.T8.C38 (FiO3 Q6):** the question drops the book's answer options (a) to (d) of parts (i), (ii) and (iii), but the LP solution (i) says "The others claim too much", which points at options the learner cannot see. Suggested: add to part (i) "(a) The average height of the class will increase as there are 2 new values. (b) The average height will remain the same. (c) The heights of the new students have to be measured to find out the new average height. (d) The heights of everyone in the class have to be measured again."; for (ii) and (iii) add the book's four options "will remain the same / will increase / will decrease / the information is not sufficient".
- **M1.S8.T8.C35 (FiO3 Q2):** "Give two examples" for each condition, but (iv) gives one concrete list plus "All six values equal also works" (no numbers) and (v) gives only one list. The LP's video uses 5, 5, 5, 5, 5, 5 for (iv) and 1, 1, 1, 1, 1, 7 (median 1, mean 2) for (v). Suggested: "(iv) ... also 5, 5, 5, 5, 5, 5 (mean 5, median 5)" and "(v) ... also 1, 1, 1, 1, 1, 7 (median 1, mean 2)".
- **M1.S10.T10.C43 and C45 (family-size examples):** the table is given only as a run-on sentence ("size 3, 4, ... occurs 3, 11, ... times"). Suggested: write it as a LaTeX table (row Number 3 to 10, row Frequency 3, 11, 9, 7, 3, 1, 1, 1) after the question.
- **M1.S11.T11.C47 (FiO1 Q10 question):** the counts exist only in the figure and the text has no pointer such as "the dot plot below". Suggested: "The number of times students rode their cycles in a week is shown in the dot plot below." The question text also has stray colons after the part labels ("(i): Find ...", "$(a)$: Everyone ...").
- **M1.S11.T11.C48 (FiO1 Q10 solution):** step (iii)(b) justifies "Almost everyone used their cycle a few times" with "39 of 42 rode at least once", which does not match "a few times". The plot gives 38 of 42 who rode two or more times. Suggested: "(b) is valid: 38 of 42 rode two or more times." Step (iii)(c) says someone who rode 8 or 10 times "must have ridden twice on a day"; this needs "a week has 7 days". Suggested: "...in a week of 7 days must have ridden at least twice on some day."
- **M1.S13.T13.C51 and C52 (worked examples):** the questions do not say where the marks sit; the formulas =SUM(B3:G3) and =AVERAGE(B7:D7) need the addresses. Suggested for C51: "Nagesh's marks are in row 3, columns B to G of the spreadsheet." For C52: "Gowri's marks in Odia, Telugu and English are in row 7, columns B, C and D."
- **M1.S14.T14.C54 (spreadsheet cells question):** the text never mentions the spreadsheet picture, yet the marks, names and column / row labels are only in it. Suggested: "Look at the spreadsheet of Sudhakar's class marks shown below." The LP's `q_figure` writes the headings as Odia, Telugu, English, Social; the book prints Odia(R1), Telugu(R2), English(R3), Social.
- **M1.S12.T12.C49 (FiO1 Q11):** the data is written as comma lists; a LaTeX table would read better (suggested array in `text_alternative` of each item).
- Checked and correct: all arithmetic in C31 to C39, C43 to C46, C48, C49, C51, C52, C55 (totals 24, 83, 70, 2010, 68, 39, 188, 193, 473; means 5.22, 4.6, 7.6, 150.22; medians 5, 4, 8).

## 4. Book mistakes and unclear places

- **Print slip, pdf p.8 (family-size dot plot, P08-dot_plot-2):** the plot shows 6 dots at size 6 and 2 dots at size 7 (34 dots), but the table says 7 and 3 (36 students, which the book's own working uses: 6 x 7 and 7 x 3). The correct plot has 7 dots at 6 and 3 dots at 7. The plot is a teaching image (`M1.S9.T9.C40.IMG1`, not this chunk's items), so no spec of mine draws it; whoever renders or reviews that concept image should use the table's counts (3, 11, 9, 7, 3, 1, 1, 1).
- **Spreadsheet snapshot, pdf p.10 and p.11:** headings printed as Odia(R1), Telugu(R2), English(R3) (probably first, second and third language) while the table on p.9 prints Odia, Telugu, English and "Social Science". Bold cells and the cut-off bottom border of row 8 are screenshot artefacts. The p.11 snapshot also shows a tiny "250 x" tooltip above H3 (not needed).
- **FiO1 Q10 (p.13):** the page text and the figure agree with the LP counts; the odd columns have no axis labels in the book (see judgement calls). Statement (iii)(b) "a few times" is vague in the book itself.
- **FiO1 Q10 (e)** continues on p.14; the dot plot is on p.13 only.
- **The book has no printed solutions section**, so the LP solution text was the answer followed everywhere.

### Chunk C notes (from the decision agent)
# Notes, chunk C (Class 8 Ch 12 "Tales by Dots and Lines", topics M2.S15.T15 to M3.S29.T29)

Result: 28 units, 40 items. Required 13, optional 3, none 24. Validator `--chunk C`: errors 0, warnings 2 (C61 and C62 solution graphs are not printed in the book, so no inventory figure maps to them; the validator says that is fine).

Required diagrams (13):
- Worked: C57 (Kerala and Punjab line graph), C89 (sleep against age curve).
- Question side: C67 (space graph), C69 (births graph), C71 (rural and urban lighting graphs), C72 (hobbies curves), C77 (two rainfall graphs), C79 (rainy-days grid with the New Delhi line), C81 (sunrise and sunset graphs), C82 (moonrise and moonset graph).
- Solution side: C61 (customers line graph), C62 (salt prices line graph), C80 (rainy-days graph completed, derived from C79).

Every other worked example in the chunk is arithmetic or words with all data in the text (none); the two open projects (C94/C95, C96) are none (OPEN_ENDED).

How the numbers in the graph specs were obtained: every data value was read from the page pictures by locating the gridlines and markers/lines by colour and converting pixel positions to values, then compared with the base inventory (the base readings agree within the stated tolerance) and with the readings the LP solutions state. Where the LP states a reading (Punjab 19 and 38, Kerala 33 and 29, World 230, 480, 600, 1270, 2850, US 2250, China 280, Russia 120, New Delhi's twelve values) the spec uses exactly the LP number. Tolerances are written in each item's `render_note`.

## Borderline

1. **C56** (worked, "where do April 33 and July 29 sit on the line graph"): none. Both values are in the question, the answer is a slope and a difference of 4. A picture of two points would only illustrate; if the user wants every line-graph worked example drawn, C56 and C58 would be the first to add.
2. **C83** (worked, Punjab -78 and Bihar close to 0 on the rice-wheat scale): none. The steps spell out what sign and size mean. The scale itself exists only in the book infographic (a colour bar from -100 "Mostly Wheat" to +100 "Mostly Rice"). If the user prefers it drawn: a number line -100, -50, 0, +50, +100 with the printed captions and markers at -78 and 0 would do.
3. **C84 / C85** (worked): none (arithmetic; C84 would need the real map, NOT_RENDERABLE).
4. **C87** (worked, school 9:30 am to 4:30 pm = 14 boxes from box 20): none. Pure arithmetic on the two-boxes-an-hour rule; the question does not read Manoj's printed strips.
5. **C68 and C78** (solutions): `optional`, not added. C68 answer = two year pairs (2016 to 2017, 2019 to 2020) and C78 answer = three peak-month ranges; all numbers are in the steps. The same graph with those segments or months highlighted would help (a v3 Step E "highlighted part"), but the book question only asks to identify them. If the user wants them, they derive from C67 and C77 and are easy to add: World segments in ANSWER with the readings 230, 480, 600, 1270; the peak months of Udupi, Rameswaram and Puri circled.
6. **C70, C71, C72, C81, C82 solutions**: none (SAME_AS_QUESTION_DIAGRAM). The LP solutions only say how to read the given graph and mark nothing (and give no concrete readings, see LP text issues). Kept consistent with each other.
7. **C98** (worked, Hex 3 by 3, "can the game end with neither player joining?"): `optional`. A 3 by 3 board with the red top and bottom and blue left and right sides would help, but the question gives no figure (the book gives only 11 by 11 boards) and states size and rule. SPATIAL_GEOMETRY would justify `required`; I applied "no question figure when the question gives none".
8. **C94/C95 and C96** (own strip, group project): none, OPEN_ENDED. The answer is a strip or graph made from the child's own timings; any picture would invent data. A v3 reader could also call C95 `ANSWER_IS_FIGURE` (the answer is a 48-box strip); if so a sample strip is needed and then `needs_lp_text_sync` must be true.
9. **C57**: required although the LP question is a worked example with a concept image of the same graph already in the plan; the question gives no Punjab value, so the graph is data, not decoration. The figure shows both states because the book graph does and the answer compares with Kerala's rise; no minimum or maximum is marked.
10. **C77**: both rainfall graphs (6 lines) in one 16:9 picture (a pair gets one question diagram). The coast is blank in the book, so no coast word is drawn (the question asks for it).
11. **C79/C80**: the New Delhi line is drawn unlabelled in the book; the spec adds a legend entry "New Delhi" because part (iii) names it. Rounded values for the three added lines use half up for the .5 values (24.5, 15.5, 2.5); the LP only says "nearest whole number". The three added lines share ANSWER green and are told apart by marker shape and legend (v3: solution content in ANSWER).
12. **Colour choice for several lines**: the palette has only SET_A / SET_B for two groups. For graphs with 3 or 4 lines (C62, C67, C77) the specs use SET_A, SET_B, INK, GUIDE or ANSWER plus different marker shapes and direct names; in C62 West Bengal (the largest rise) is in ANSWER.

## Judgement calls

- **C61 and C62 solution = a drawn line graph** (ANSWER_IS_FIGURE) although the steps describe it in words; the questions carry no figure, so `derived_from` is null and the solution draws the whole figure. C62's three states (Gujarat, Uttar Pradesh, West Bengal) are my choice because steps (iii) and (iv) of the LP solution use exactly these; `needs_lp_text_sync` is true on that item.
- **C62 question** is none (the 10 by 6 table is plain numbers, LATEX_TABLE) even though the LP question text does not contain the table yet (see LP text issues).
- **C69**: the graph covers Apr 2017 to Mar 2020 (36 dots; the first dot lies three months before the "Jul 2017" gridline, the last two months after "Jan 2020"). The LP's card hint says "Jul 2017 to about mid 2020"; the spec uses the picture. Question numbering: the book prints this question as "2" a second time; it is Q3.
- **C71**: vertex years of the lines are not printed; read from the tick spacing as about 1983, 1992, 2001, 2012, 2023 (+/-1 year). Percentages read to about +/-2 points. At the year 2000 the urban electricity line reads about 90 (statement (iii) says 10).
- **C72**: only "1h" and "2h" are labelled on the book's time axis (no 0h label); kept as printed. The rural curve is hidden behind the urban one from about age 20.
- **C81**: the book does not say which line is sunrise (the question asks it), so no line is labelled; the lower line of each place is the sunrise. Srinagar's Sept sunrise marker is hidden behind Kanyakumari's (read as about 06:15).
- **C82**: moonrise has no point on date 21, moonset none on date 6; the lines are not joined across the gap. Readings +/-10 minutes.
- **C89**: book print slip corrected (see Book unclear). The curve is drawn from age 6 to 75 as the book text says (the picture starts a little before age 6 and runs to about 80).
- **Figure mapping**: P14-bar_graph-2 and P16 and P23 and P24-line_graph-1 and P32-board-1/2 are teaching figures (concept_image accounting only). P22 map = NOT_RENDERABLE. The p.20 graph is used twice (question C79 = P20-line_graph-1, solution C80 = NEW-P20-line_graph-1-sol). P24-line_graph-2 (zoomed) is the picture behind C89's diagram, P24-line_graph-1 is accounted as the teaching image. P32-board-3 (empty 11 by 11 board for play) = none:OPEN_ENDED.
- The base inventory descriptions matched the page pictures in every figure of this chunk; no `CORRECTED:` entry was needed.

## LP text issues

(Not edited; suggestions only.)

1. **M2.S17.T17.C62** (single, book Q9). (a) The block text is empty ("read the question in the book"); the real question is in the Practice block M2.S15.T15.C59 and does not contain the table. Suggested: add the LaTeX table of the book (columns Andaman and Nicobar Islands, Assam, Gujarat, Mizoram, Uttar Pradesh, West Bengal; rows 2016 to 2025: 16, 6, 16.5, 20, 16.15, 9.47 / 12, 12, 14.75, 20, 16.97, 11.65 / 12, 12, 14.75, 22, 16.18, 11.63 / 12, 12, 14.75, 22, 18.24, 11.43 / 13.88, 12, 13, 20, 18.96, 11.11 / 18.22, 15, 14.45, 22, 20.63, 12.79 / 18.73, 14, 14.28, 25, 21.3, 16.14 / 20.63, 12.02, 14.54, 27.65, 25.39, 18.43 / 19.73, 13.72, 14.8, 29.03, 26.9, 21.66 / 20.99, 12.35, 19.2, 29.8, 24.81, 23.99). (b) Step (i) does not name the 3 states. Suggested: "(i) Choose Gujarat, Uttar Pradesh and West Bengal: years 2016 to 2025 along the bottom, prices from 0 to 30 rupees up the side in steps of 5, one line per state."
2. **Wrong book numbers on the six singles**: M2.S17.T17.C62, M2.S20.T20.C71, M2.S20.T20.C72, M2.S23.T23.C81, M2.S23.T23.C82, M3.S28.T28.C96 all carry `book_number` "Figure it Out, Q1"; the book numbers are Q9, Q10, Q11, Q14, Q15, Q13. Their block text says "read the question in the book" and the real question text sits in Practice blocks of other concepts (M2.S15.T15.C59, M2.S18.T18.C66, M2.S21.T21.C76, M3.S26.T26.C93).
3. **M2.S19.T19.C67**: the question says "the World line" but not which graph. Suggested: "Use the World line of the graph of objects launched into space (2012 to 2024) to find two consecutive years where the count at least doubled."
4. **M2.S19.T19.C69 / C70** (births). The solution gives no value. Step (i) says "one sharp fall in a particular stretch", which the graph does not show (the real pattern: a rise to about 2 million in August to October each year, a fall to about 1.5 million by February to April with a small zig-zag in March). Step (iii) tells to read the first and last labelled months (Jul 2017, Jan 2020) but the line runs from April 2017 to March 2020. Suggested answers: "(ii) about 1.75 million (1.8 million); (iii) April 2017 to March 2020, 36 months; (iv) January 2018 about 1.67 million, January 2019 about 1.75 million, January 2020 about 1.77 million, so each January is a little higher; (v) the 12 monthly values of 2019 add to about 21.4 million (about 1.8 million a month)."
5. **M2.S20.T20.C71** (lighting). Steps leave (i) and (ii) as "check against the lines". Suggested: "(i) Valid: in 1983 rural kerosene is about 84% and urban electricity about 64%, both a majority. (ii) Valid: kerosene falls from about 84% to about 0% in rural homes and from about 34% to about 0% in urban homes. (iii) Not valid: in 2000 about 90% of urban households used electricity; about 10% used kerosene. (iv) Not supported: the graph shows the main source of lighting, not power cuts."
6. **M2.S20.T20.C72** (hobbies). No concrete answers. Suggested: "(i) about 2.1 hours; (ii) about 14 years, option (d); (iii)(a) not correct: the urban reading at 15 (about 1.1 hours) is about half the reading at 10 (about 2.1 hours), and the rural readings (about 1.3 and 2.4) also halve; (b) cannot be concluded: the graph shows an average."
7. **M2.S22.T22.C79 / C80** (rainy days). The question text omits the table (rows Mangaluru, Port Blair, Rameswaram with values, and the New Delhi row blank): suggested LaTeX array with the book values and an empty New Delhi row. Step (ii) should say "round half up" (24.5, 15.5 and 2.5 are halves). Checked and correct: the sums 112.1, 125.8, 42.3 and "about 36" (36.4), the rainy seasons.
8. **M2.S23.T23.C81 / C82** (sunrise, moon). No readings. Suggested C81: "The lower line of each place is sunrise, the upper line sunset. (i) Kibithu: sunrise about 05:55 and sunset about 16:30, a day of about 10 hours 35 minutes. (ii) Srinagar in June: sunset about 19:45 and sunrise about 05:20, about 14 hours 25 minutes, longer than Kibithu (13 h 55 min), Ghuar Moti (13 h 35 min) or Kanyakumari (12 h 35 min)." Suggested C82: "(i) Amavasya about the 28th or 29th (moonrise about 06:10 to 07:00, moonset about 17:00 to 18:00); purnima about the 13th or 14th (moonrise about 17:25 to 18:25, moonset about 06:40 to 07:30). The times shift 30 to 65 minutes later each day" (the step says about 50 minutes).
9. **M2.S24.T24.C83**: "Bihar is close to 0": the infographic prints +3 (the last digit hides under the red line); fine, but if the exact value is wanted write "about +3".
10. Checked with no problem: C56 to C58 numbers, C63 (2250 + 280 + 120 = 2650; 2850 - 2650 = 200), C65 (13 x 4 = 52), C73 (3400 / 4 = 850), C84 (298 / 5 = 59.6), C85 (193), C87 (box 20 to box 33), C88, C91, C92.

## Book unclear or slips

- **p.24 zoomed sleep graph**: ten equally spaced gridlines are labelled 12.0, 11.5, 11.0, 10.5, 9.5, 9.0, 8.5, 8.0, 7.5, 7.0; the label 10.0 is missing, so the top four labels are 0.5 too high. The lower six are right (the curve is lowest at 8.0 in both pictures and about 9.7 at the left edge in the unzoomed one). Corrected in the C89 spec (axis 7.0 to 10.0, curve about 9.5 at age 6, matching the book text).
- p.21: the second question is printed as "2" again (it is Q3).
- p.23: the text says "five types of activities" and then lists six (i) to (vi); no colour key is printed for the strips.
- p.18 and p.19: the rainfall graph titles have a blank for the coast name ("along the ______ Coast").
- p.22: Bihar's value is partly covered by the red line (+3 or +3x); the LP says close to 0.
- p.17 text says 2800 (2024) and 2900 (2023); the graph reads about 2850 and 2905.
- p.28 Q11: only 1h and 2h are labelled on the time axis; the rural curve is hidden behind the urban curve from about age 20. Q10: the vertex years of the lines are not printed.
- p.30 Q14: the graph does not mark sunrise and sunset (the question asks); Srinagar's September sunrise point hides behind Kanyakumari's. Q15: no new-moon or full-moon dates are marked (the question asks).
- p.24 text: "ages 6 to 75", "80 data points", "70 columns" do not agree with each other or with the picture (curve from about age 5 to about 80).
