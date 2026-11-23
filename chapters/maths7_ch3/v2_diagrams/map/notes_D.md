# Notes, chunk D (M3.S19.T19, M3.S20.T20, M3.S21.T21, M3.S22.T22)

Result: 29 items = 2 required, 2 optional, 25 none. Validator `--chunk D`: errors 0, warnings 0.
Required: only Figure it Out Q15 (M3.S21.T21.C94): question IMG1, solution IMG2 (solution derived_from IMG1).
Figures claimed (7): P25-table-4, P27-comparison_visual-3, P29-column_arithmetic-1, P30-place_value_addition-1 (all `none:`), P35-addition_boxes-1 and P55-digit_tiles-1 (to C94), P47-table-2 (`none:LATEX_TABLE`). I checked all seven base descriptions against the page pictures: all correct, no CORRECTED entries.

## 1. Judgement calls

- **C78 solution (zero dilemma, printed answer is a table)**: none (`HEADER_BOXES_ONLY` + `LATEX_TABLE`). The printed answer is a place-value table of plain digits with no colour or highlight meaning. v3 lists a place table, with or without digits, as not a diagram. Rule B2 ("printed answer is a picture") was not applied, because that rule is about drawings and arrangements. If the content team wants the table as an image, flip this one; the LaTeX array is in `text_alternative`. The same reasoning maps P25-table-4 (the book's teaching table) to `none:LATEX_TABLE`. C78 question is none: the learner builds the place table, and the book's own table would hand over the working.
- **C80 solution (6.456 vs 6.465)**: `optional`, not added. The book draws a not-to-scale step-by-step zoom picture (P27) for exactly this comparison. The LP text steps are complete, and a place-value table (LaTeX) carries the same information. A zoom picture would only help the "why can we stop" idea. If you want it, it is a number-line zoom 6 -> 6.4 -> 6.45 / 6.46. The question side is none.
- **C88 worked example (75.345 + 86.691, compact form)**: `optional`, not added. The task asks for the compact column addition with carries, which is LaTeX arithmetic. The book's detailed place-value picture (P30, six columns with red circled carries and curved arrows) is the teaching view and the steps already say what each carry means. Same family of decision as C80: a book explanation picture that restates the text steps is optional.
- **C91 (cloth addition)**: both sides none (`LATEX_ARITHMETIC`). The book picture P29 is plain mixed-number and decimal column additions with one small carry. Both are LaTeX arrays (text alternative written).
- **C84 (descending order, four lists)**: solution none. The answer is an ordered list of numbers (a sequence), not an arrangement of objects to draw, so B2's "arrangement" rule does not apply.
- **C85 (digits 1, 4, 0, 8, 6)**: both none. The book gives no boxes for FiO Q5, and the answer is two written numbers. The box frames belong to the Math Talk "closest to 25" example (block M3.S18.T18.C76, another chunk). P28-digit_boxes-1 and P50-digit_tiles-1 are therefore not claimed here.
- **C94 question diagram is required** (the learner must fill a given frame, `DATA_IN_FIGURE` + `ACTION_ON_FIGURE`). The book draws the boxes yellow; the spec uses CELL_FILL (house style). The sum below the line stays blank, as in the book question. The spec uses the frame geometry in box units (1 u = 230 px), identical in both figures, and the solution bounding box is centred on the canvas for both.
- **C94 solution follows the LP, not the book** (see 2.1). Filled digits and the sum row are ANSWER green; frame, dots, plus sign and line stay INK.
- C89 and C96 (estimating a sum / a difference): none. All numbers are in the text, the book shows no figure, and a range line (33 to 35, 6 to 8) would only be decoration.

## 2. Things in the LP that look wrong or thin

1. **C94 answer differs from the book.** Book printed answer (pdf p.55): 9.476 + 1.025 = 10.501 (gap 0.001). LP answer: 0.643 + 9.857 = 10.500 (gap 0). I checked the LP: 3+7=10, 4+5+1=10, 6+8+1=15, 0+9+1=10; digits 0,6,4,3,9,8,5,7 are all different. So the LP answer is correct and better, and it is what the diagram draws.
2. **C85 solution step 2** says "18.046 is 11.954 below 30". The best number with tens digit 1 is 18.640 (11.36 below 30), which is what the video's maths_rules use. The conclusion (40.168, gap 10.168) still holds, but the step text and the video disagree. Suggest changing the step to 18.640 / 11.36.
3. **C92 step (g)** reads "Write 0.03 as 0.03" (nothing is rewritten). It probably meant "0.75 and 0.03 already have two places" or similar.
4. **C78 question text** merges two book questions: the Zero Dilemma discussion ("use a place table to settle Sonu and Zara") and "which is smallest and largest". The book answer for the second is split across pdf p.47 ("largest") and p.48 ("0.002 is the smallest").
5. **C86 and C79** were checked against the book and agree. C79 LP steps say the same as the book answer (4.5 = 4.50 = 04.50, 4.05 = 4.050).
6. The LP numbering of the end-of-chapter questions (Q4, Q5, Q6, Q7, Q15) and FiO Q1 matches the book (book p.75, p.79, p.80).
7. C94 LP media: the unit still lists old card ids IMG1/IMG2/IMG3 (question card plus two solution cards). New ids are IMG1 (question) and IMG2 (solution), as the brief says; the build renumbers them.

## 3. Places where the book is unclear

- Printed answer of the zero-dilemma question is split across two pdf pages (p.47 and p.48), see 2.4.
- The book's printed answer to the Math Talk "closest to 25" example has a 4-box yellow row (8.542), so the digit 1 is unused in that row; this is the book's own picture (chunk C).
- The book gives no printed answer for "Which is larger: 6.456 or 6.465?" (the p.72 picture is its explanation), so C80's solution rests on the LP text only.
- P27's visualisation is explicitly "not to scale", so no exact tick positions can be read from it (one reason it is not added as a diagram).
