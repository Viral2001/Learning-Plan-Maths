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
