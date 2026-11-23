# Chunk D notes (Class 5 Ch 6, The Dairy Farm): Let us do, Dairy Cooperative, Examples 6-8, Let Us Solve (second set)

Units: 17 (15 pairs, 2 worked examples) = 32 items. Result: required 8, optional 0, none 24 (question 2 / 0 / 13, solution 5 / 0 / 10, worked example 1 / 0 / 1).
Required diagrams: C88 (question) and C89 (solution) Nida boxes; C105 worked example (carries frame); C108, C110, C112 solutions of Examples 6, 7, 8; C117 (question) and C118 (solution) of Let Us Solve Q3.
Validator: errors 0, one warning (C105 required but no inventory figure maps to it: the figure is the LP's own example 176 x 24, not a book picture).

## 1. Judgement calls

- **C88 / C89 (Let Us Do Q1, Nida): question required, solution required.** The book prints four blank area tables to be completed (ACTION_ON_FIGURE), so the question gets one card with the four blank tables (2 x 2, letters (a) to (d) shown because the LP answer refers to (a), (b), (c), (d)). The solution is the same layout filled (ANSWER_IS_FIGURE), `derived_from` the question diagram. The book prints no solutions for this pdf; the numbers come from the LP steps and were recomputed (312, 747, 1,876, 1,961).
- **Same four tables, second use.** The solution diagram redraws the four base tables, so the base ids P10-area_table-7..10 map to the question and the same figures appear again as NEW-P10-area_table-7-sol .. 10-sol mapped to the solution. Same pattern for the three frames of Q3 (NEW-P15-written_method-1..3-sol).
- **C90, C92 (Kanti, John) and C91, C93: none.** The book gives no figure for Let Us Do Q2 and Q3 and prints no solution picture. The answers are plain vertical lines (LATEX_ARITHMETIC) that the LP already states line by line. A LaTeX array is suggested in `text_alternative`.
- **C94 / C95 (cinema): none both sides.** The book's cinema picture is decorative (perspective view, numbers in the text, base figure P11-illustration-1 mapped to none:DECORATIVE_ONLY). The old s_figure hint on C95 (a seating plan with 48 seats marked) was not adopted: the book does not say where the first 48 people sit, so any plan would invent positions.
- **C96 to C103 (cricket, bulbs, rice, library): none both sides.** Word problems, no figure in the book, numbers in the words, arithmetic in LaTeX.
- **C104 worked example (235 x 4 place by place): none.** Plain lines 20, 120, 800 and their sum, no carries, circles or colours. See Borderline.
- **C105 worked example (176 x 24 with carries): required (own diagram, id C105.IMG2).** The kept teaching image C105.IMG1 shows the same example as a ledger; under the user's decision 5 it does not stop the worked example from getting its own diagram. The frame follows the book's pictures of Mili's father's method (carries circled above the number, struck carry digits in the row, a plain leading digit for the last carry). The teaching image is not linked or edited.
- **C107, C109, C111 (Examples 6, 7, 8 question side): none.** The book's pictures beside them (women pouring milk, a Gir cow, three ghee jars) are decorative (three NEW- inventory entries mapped to none:DECORATIVE_ONLY); the numbers are in the question text.
- **C108, C110, C112 (Example solutions): required, one card per solution with two panels.** The book prints each worked answer as two pictures: the expanded working with colour-matched digits (P12/P13/P14-written_method-1) and Mili's father's frame (written_method-2). A pair may have only one solution diagram, so both pictures are drawn in ONE 16:9 card: expanded working on the left, frame on the right. Colours of matched digits are kept because the Example 8 question asks what the same coloured digits mean and the LP answer explains them (blue = SET_A, red = FOCUS, orange = SET_B). The book's long red notes and the "Remember!" box are not drawn (LP step text, and over the 3-word tag limit).
- **C113 to C116, C119, C120 (Let Us Solve Q1, Q2 and the second part of Q3): none.** No figure is given in the book for these. See Borderline for the Nida and Mili's father answers.
- **C117 / C118 (Let Us Solve Q3, three frames): question required, solution required.** The book prints three frames with circles and boxes to be completed. The question card shows them as printed (one row, same scale). The solution completes every printed slot and adds the sum rows from the LP steps.
- **Frame conventions used in every frame.** A carry is circled above the digit it enters and also written struck in a dotted box in its row (the book's picture of Examples 6 and 7 and the frames of Q3 do this); the last carry out of the leading digit is a plain digit in the next column. Row 1 circles and boxes are FOCUS, row 2 SET_A, row 3 SET_B; given digits INK, added digits ANSWER. No arrows are drawn.
- **Printed boxes of the Q3 frames follow the method.** Row slots were derived from the digits and carries of each row (a script cross-checked every row value and sum), because the base description says slot alignment is approximate. Frame (ii) row 2 starts with a small box that sits where a + goes; the solution writes + in it.
- **Added in the solution of Q3 (ii):** the heading T Th above position 1 (the sum 11,830 needs a ten thousands digit; the printed frame has no such column), a sum row, and a second upper carry circle above the tens digit of 455 (the book prints only one upper circle but the carry 1 from 2 x 5 = 10 has to go somewhere; its dotted box is printed). All are named in the item's accuracy checks.
- **Number style.** The LP's comma style is used (1,359 and 5,889; the book prints 1359, 4530, 5889 without commas in Example 7). Headings use the book's "T Th".

## 2. Borderline (v3 rules applied as written; user may flip)

- **C104 worked example** (none): a Th H T O layout of the partial products 20, 120, 800 would help but a LaTeX array carries it. Flipping to optional/required needs a short spec only.
- **C105 worked example** (required): the steps also state every carry in words; the figure is kept because the carry positions are the point of the example and a teaching image of the same example is kept (decision 5).
- **C114 (Let Us Solve Q1 like Nida, 5 problems)** (none): the book gives no table here, so there is no printed blank table to complete; the cells, column sums and totals are in the LP steps. Five filled Nida boxes (as for Let Us Do Q1) would help. Sibling difference to C88/C89 is the printed blank tables.
- **C91, C93, C116 (Kanti and John lines)** (none): lines like those of the teaching image C78 could be drawn; they are vertical arithmetic, so LaTeX.
- **C120 (Let Us Solve Q3 second part, nine products)** (none): no frame is printed for (a) to (i); nine more frames would repeat one layout. The first part of the same NCERT question (C118) is required because the book prints frames to complete.
- **C88 / C89**: the blank boxes could also be seen as a LaTeX table; kept required because the book gives them as a figure to complete (ACTION_ON_FIGURE).
- **C95** (none): a seat plan of 8 rows of 12 seats would help but needs an invented position for the first 48 people.

## 3. LP text issues (no LP text was changed)

- **M3.S21.T21.C88 (question).** The text never mentions the tables that the figure shows. Suggested sentence: "Use a table like Nida's for each problem: write the digits of the first number across the top, the digits of the second number down the side, a row for the column sums and one last cell for the total."
- **M3.S24.T24.C117 (question).** The text names the frames but not what is to be completed. Suggested sentence: "Complete each frame: write every carry in its circle and the digits of every row in the boxes, then write the product."
- **M3.S24.T24.C117 / C118.** The text says the first two frames have columns thousands to ones, but the sum of frame (ii) is 11,830 (five digits) and the book prints no sum row. Suggested sentence for C118: "The sum 11,830 has a digit in the ten thousands place, so write it one place to the left of the thousands."
- **M3.S24.T24.C118 (steps for (ii) row 2).** Gives only "2 x 455 = 910, so the row is 9,100". The figure shows the carries of the method. Suggested sentence: "(ii): row 2. Write a 0 first. 2 x 5 = 10, write 0 and carry 1. 2 x 5 = 10, and 10 + 1 = 11, write 1 and carry 1. 2 x 4 = 8, and 8 + 1 = 9, write 9. Row 2 is 9,100."
- **M3.S24.T24.C118 (steps for (iii) row 2).** "0 x 143 = 0, so the row is 0" while the book prints four boxes for that row. The figure shows 0 0 0 0. Suggested sentence: "(iii): the row for 0 tens is all zeros: 0 0 0 0."
- **M3.S24.T24.C118 (frame (ii) circle above Th).** The book prints a circle above Th; the figure puts the last carry 2 (6 x 4 + 3 = 27) in it. Suggested sentence in (ii) row 1: "6 x 4 = 24, and 24 + 3 = 27, write 7 and put the 2 in the thousands place."
- **M3.S23.T23.C112 (steps).** The LP explains the blue and red digits but not the orange ones that the book also prints (the 10 of 10,000 and the 1 of 1,400). Suggested sentence: "The orange digits are 10 thousands and 1 thousand: 10 + 1 = 11 thousands."
- **M3.S21.T21.C95 / old s_figure hint.** The old hint describes a seating plan with 48 seats marked; the book gives no positions. Nothing to change in the text; the hint should not be reused.
- **Hint wording.** The old q_figure of C88 says tables of two-digit multipliers have "2 columns and 2 rows"; the printed tables have 3 columns and 5 rows (headings and sums rows included).

## 4. Book: mistakes and unclear places

- **Example 8 note, page 83.** The red note "2 Tens x 574 = 2 x 3,740" is a print slip: 574 x 10 = 5,740, so it should read 2 x 5,740 (the LP already says this in step 7). The note is not drawn; the diagram uses the correct row 11,480. The base inventory records what the book prints.
- **Example 8 frame, page 83.** The book strikes the leading carry digits too (a struck 2 between Th and H in row 1, a struck 1 between T Th and Th in row 2). Examples 6 and 7 do not. The spec follows Examples 6 and 7 for all frames (leading carry plain), which also matches the LP steps ("Write 28").
- **Example 8 green circle.** The book's green circle (row 2 carry 1) sits half a column left of the H column; the spec puts it above H.
- **Example 7 expanded working, page 82.** The book prints 1359, 4530, 5889 without commas, 1,200 with a comma in the blue box. The LP style is used.
- **Let Us Solve Q3 frames, page 84.** The slots are not aligned to the headings in the book (the boxes are offset by about half a column, frame (ii) row 2 has a small extra box at the left) and no frame has a sum row. Frame (iii) prints its dotted 3 and 2 without a slash, frame (ii) prints its 3 struck. The question figure keeps the printed state; the solution slashes every dotted box that holds a digit.
- **Frame (i) of Q3, page 84.** The frame has one circle (above T) and no answer boxes at all; the solution adds the product row 7 2 5 4.
- **Cinema picture, page 80.** Rows and seats cannot be counted in the perspective view; the numbers (8 rows, 12 seats) are in the text, so the picture is decorative.
- **Let Us Do Q4(a), page 80.** "If 3 more rows get filled" does not say whether the rows were empty; the LP reads them as 3 new full rows (84 people) and says so in step 5. Left as is.

## 5. Base inventory checks

All base figures of chunk D were checked against the page pictures (pages 10 to 15); no description needed a CORRECTED prefix. The doubt on P11-illustration-1 (not countable) is confirmed: decorative. The doubts on P12/P13/P14/P15 slot positions are handled by deriving the slots from the method (section 1). Four pictures missing from the base are added as NEW- entries mapped to none:DECORATIVE_ONLY (women with milk cans p.12, Gir cow p.13, ghee jars p.14); the characters Mili and her father (p.12) are not recorded (decoration).
Figure bookkeeping: 24 inventory entries = 20 mapped to items (4 table figures + 4 second-use table entries, 6 written-method figures of Examples 6-8, 3 Q3 frames + 3 second-use frame entries), 0 to concept images, 4 none (the cinema picture and three NEW- decorative pictures).
