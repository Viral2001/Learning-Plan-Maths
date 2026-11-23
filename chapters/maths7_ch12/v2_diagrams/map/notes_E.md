# Chunk E notes (Class 7 Ch 12, units 69 to 74)

Units: worked example M3.S35.T35.C159, and the five pairs of M3.S36.T36 (C161/C162 to C169/C170).
Result: 11 items, required 2 / optional 0 / none 9. Validator: errors 0, warnings 0.
Base figures claimed (all on book page 28): P28-box_equation-1, P28-box_equation-2, P28-box_equation-3 (all none:TEXT_SUFFICIENT),
P28-table-3 (question diagram of C165) and NEW-P28-table-3-sol (second use of the same table, solution diagram of C166).
The other page 28 figures (P28-table-1 and P28-table-2, the conversion boxes of book Q5) and the page 27 number lines belong to chunk D, not to this chunk.
P21-pattern-1 (Math Talk 1/2, 1/(2x2), ...) is not used by any item of this chunk.

## 1. Judgement calls

- **C165 / C166 (book Q9, LP Q3): grid required on both sides. This is the one real judgement call.**
  The book table is a plain table of numbers (the prompt's LATEX_TABLE example is a one-row "complete the table" that stays LaTeX), but here it is a
  two-way grid with a heading row and a heading column, the question talks about "missing cells", and the answer is the completed grid
  (ANSWER_IS_FIGURE, B2: a filled figure is required even when the steps list the rows in words). The catalogue also names multiplication grids as `cell_grid`.
  If the reviewer prefers text, the alternative is a LaTeX array for both sides: question side then needs the three given cells placed in the array.
  Question diagram: given cells only (41, 4.1, 4100). Solution diagram: `derived_from` the question diagram, all 25 cells, the 3 given ones in INK, the 22 added in ANSWER.
  I put no fill in any cell (the book uses pale green) so nothing looks pre-shaded.
- **C161 / C162 (book Q7) and C167 / C168 (book Q10), the "fill the boxes" questions: none on both sides.**
  The book figure is only empty boxes: two boxes per equation in Q7, and the box pattern (two digits, point, one digit) x (one digit, point, one digit) in Q10.
  The LP question text already carries the same pattern as box signs, and the answers are filled equations (82.0 x 5.4 = 442.8 and so on) that LaTeX shows completely.
  Q7 and Q10 got the same decision on purpose (sibling consistency). The tie-breaker says a careful student loses nothing without the picture.
  Not made `optional` because the picture would only repeat the text.
- **C163 / C164 (book Q8) and C169 / C170 (book Q11): none.** No book figure; six divisions or six expressions in text, answers are arithmetic or one chain of letters.
  A number line for the sorted values in Q11 would be a nicety, not needed, so not even `optional`.
- **C159 (worked example "One fact, many answers"): no_image.** Three one-line calculations from 45 x 12 = 540. The teaching image M3.S35.T35.C159.IMG1 already fans out the same fact;
  it is not linked (v3) and the example does not need its own figure, because it names no lettered or referred figure. The example is LP-written, it is not in the book.
- Number style in the Q3 solution grid is the LP's own (410000, no commas), as the LP solution prints it.

## 2. Things in the LP that look off

- **Numbering.** The LP calls these questions "Figure it Out 4.4, Q1 to Q5" but they are book Figure it Out Q7 to Q11 (pages 94 and 95); `ncert_refs` 4.4.end7 to 4.4.end11 and the old card titles ("End of chapter Figure it Out, Q7") say so. Q1 to Q6 of the book are in topic T34 (chunk D). The `book_number` text in T36 is therefore misleading for a learner reading the book. Not changed (outside my files).
- **Q3 solution step 1 wording is ambiguous.** "Each step right in a divides the quotient by 10; the last column multiplies it by 10. Each step down in b multiplies the quotient by 10; the last row divides it by 10."
  True only if the last column and last row are compared with the first column and first row (15170 = 10 x 1517 and 370 = 10 x 37). Compared with the neighbouring column the last step changes the quotient by 10000.
  The final grid in the LP is right: all 25 cells recomputed with Decimal as column heading divided by row heading, and they match the LP rows exactly.
- **Q3 question text lists the data in words** (rows b, columns a, three given equations) and also says "missing cells"; with the figure placed after the question text this is repeated information, harmless. It lines up with the figure: (b=37, a=1517)=41, (b=3.7, a=15.17)=4.1, (b=0.037, a=151.7)=4100.
- **Q2 (book Q8) has (b) and (f) identical** (7.56 / 0.36 = 21). This is in the book itself; the LP solution says "(f) is the same division as (b)". It reads like a printing mistake in the book (something like 7.56 / 36 may have been meant). Left as in the book and the LP.
- Q4 answers were checked by brute force over all 120 digit placements of 2, 4, 5, 8, 0 in the boxes: maximum 82.0 x 5.4 = 442.8, minimum 45.8 x 0.2 = 9.16, 28.0 x 5.4 = 151.2 is above 150, nearest to 100 is 20.5 x 4.8 = 98.4 (next best 102.0), nearest to 5 is the minimum 9.16. All match the LP. Note that (c) has many correct answers; the LP gives one "for example", fine.
- Q5 values recomputed: (a) 230.93, (b) 1952.61, (c) 30.75, (d) 260.04, (e) 245.05, (f) 7.9682; order (f) < (c) < (a) < (e) < (d) < (b) is right.
- C159 numbers recomputed: 4.5 x 1.2 = 5.4, 0.45 x 12 = 5.4, 54 / 1.2 = 45. Right.

## 3. Where the book itself is unclear

- Page 28 prints the Q7 boxes the same size in (a) and (b), so the book does not show how many digits each factor may have (Q7 is open: 1.2 x 2 and 0.6 x 4 are both allowed).
- Q10's boxes show the digit pattern but the book does not say whether 0 may stand in the ones place of a factor. The LP's minimum 45.8 x 0.2 = 9.16 does that (0 in the ones box of the second factor); the LP answers follow the box pattern, so nothing to fix, but a different reading would change (b) and (e).
- The book has no printed solutions in this pdf, so there is no printed answer picture for Q9; the Q3 solution grid is drawn from the LP solution.
