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
