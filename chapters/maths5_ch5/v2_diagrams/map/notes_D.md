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
