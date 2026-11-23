# Chunk A notes - Class 5 Ch 6 "The Dairy Farm" (topics M1.S2.T2 to M2.S8.T8)

Result: 18 units, 31 items. Required 16 (questions 5, solutions 6, worked examples 5), optional 1, none 14. Validator `--chunk A`: errors 0, warnings 6 (see "Validator warnings").
Figures: all 21 base figures of book pages 1 to 5 are claimed (13 to items, 8 to `none:`), plus 4 `NEW-...-sol` entries for solution redraws of the same book figure (units 2, 3, 4, 8). No `concept_image:` mapping: the five teaching images of this chunk (C3, C15, C21, C22, C36) show LP-authored pictures, not book figures.

Required diagrams (media ids):
- Worked examples: M1.S2.T2.C3.IMG2 (36 pouches turned), M1.S4.T4.C15.IMG2 (tray 7x12 turned), M1.S6.T6.C21.IMG2 (place value board 37), M1.S6.T6.C22.IMG2 (counting board 60 x 70), M2.S8.T8.C36.IMG2 (6 x 14 split).
- Questions: C5.IMG1 (shapes), C7.IMG1 (digit frame), C9.IMG1 (pouches), C13.IMG1 (number and operation grid), C17.IMG1 (packet arrays).
- Solutions: C6.IMG1, C8.IMG1, C10.IMG1, C18.IMG1 (derived from their question diagrams), C12.IMG1 (number chart with marks, stands alone), C31.IMG1 (place value board for x 1,000, stands alone).

## 1. Judgement calls I was unsure about

### Borderline (v3 rules applied as written; none flipped to none only because the LP text has the numbers)
- C3 worked example (36 pouches): `required`. The question says "turn the picture of the groups of 4" and no picture is in the text. The diagram shows 9 rows of 4 and the turned 4 rows of 9 with a turn arrow. It duplicates the kept teaching image C3.IMG1 on purpose (user decision 5).
- C15 worked example (tray 7 rows of 12 turned): `required`, borderline. Every number is in the text; drawn because turning the tray is a spatial idea and it is the sibling of C3. Spec = 7x12 and 12x7 arrays with "Groups" / "Group size" brackets, no totals.
- C36 worked example (6 rows of 14 split into 10 and 4): `required`, borderline. The array cut into a block of 10 columns and a block of 4 columns is the whole point of the example. If you prefer, this one and C15 can go to `optional` without touching anything else.
- Worked examples C21 and C22 are `required` without doubt: the questions say "Show how the digits of 37 move on the place value board" and "The counting board shows 60 x 70".
- C17 question (packet arrays, book page 3): `required`, borderline. "Arranged in the following ways" points at the arrays and the pattern is seen in the turned arrays, but the LP text already lists every expression. Pairs (a) and (b) show the letters (the LP answer uses them); the two big arrays have no letter (the book prints none; its letters run a, b, e, f, g). (e), (f), (g) are text boxes in the book, no picture.
- C18 solution (same arrays): `required`, borderline. It adds the totals (6, 40, 78) and the 10 + 3 split of the big arrays that the LP steps use (6 x 10 + 6 x 3, 10 x 6 + 3 x 6). The answers for (e), (f), (g) stay text because the book has no picture for them.
- C11 question (Which number am I, number chart): `optional` (not added). The book prints a plain, unmarked 0 to 99 chart as a working aid; all eight clues are in the text, so the question can be attempted without it. If you want the chart on the question side, change it to `required` and give the solution `derived_from` = the question diagram (the chart without marks); the spec of the chart is already in C12.IMG1.
- C12 solution: `required`, standalone (`derived_from` null) because the question side has no diagram: 18, 27, 36, 45 shaded, 27, 36, 45 crossed out in WRONG, 18 circled in FOCUS. WRONG is used because the LP solution itself shows these numbers being ruled out.
- C31 solution (multiplying by 1,000): `required`, borderline. The LP solution explains the rule on "the place value board" (every digit moves three places left) and the board is not given in the question. The question (C30) is `none`: the book's 2 and 5 green 1,000 tokens only illustrate "2 thousand" and "5 thousand" and have none for 10 and 20. If you judge the board "only nicer", set C31 to `optional`.
- C14 solution (Make your own numbers): `none`. The sample answer is a list of equations and is open-ended; the question grid is the figure. I verified the LP claims by brute force: with two different numbers and one operation, 0 and 19 cannot be made; only 11, 16, 17 and 18 have one way; 0 = (100 / 25) - 4 and 25 - (10 - 4) = 19 are right.
- Units 13, 14, 16, 17 (place value tables, Problem / Th / H / T / O or TTh ... O): all eight items `none` (`LATEX_TABLE`, `HEADER_BOXES_ONLY`). Header boxes with or without digits are a LaTeX array by the v3 list; the book's six problem cards (underlined digits) and the red "notice the underlined numbers" margin note are arithmetic (`LATEX_ARITHMETIC`). Sibling consistency kept across the four question sets.
- Units 9 and 12: `none` / `none` (no printed picture, words and equations only).
- The same-number-two-items rule: the shape set, digit frame, pouches and arrays are each drawn twice (question and solution) with the same layout, solution `derived_from` the question.

### Choices inside the specs
- Colours: only the shape fills of Let Us Think Q1 are hex values outside the style tokens (#7BA7D9 rectangle, #F48CAE circle, #D8BCDC triangle, #FDB35A diamond, #B5D58A pentagon, #FFDE92 parallelogram, #A7DDF5 half-disc, white notched shape). They copy the book because colour plus shape is each shape's identity; every shape is also unique by outline. Everything else uses tokens only.
- C13 (grid): the book colours the four operation buttons; the colours mean nothing, so CELL_FILL is used.
- C9/C10 (pouches): letters (a) to (d) are drawn because the LP answer uses them (decision 3), though the book prints none. The question figure has no equations (they are in the LP text); the solution adds group outlines and the tags 30 x 2 (INK, it is the example given with the question), 20 x 3, 6 x 10, 5 x 12 (ANSWER).
- C5/C6 (shapes): letters (a) to (f) are drawn because the LP steps use them. The solution draws the LP sample set (pentagon 1, parallelogram 2, rectangle 3, circle 4, diamond 6, half-disc 8, white shape 9, triangle 12). I checked it: all six sentences hold and (f) is 8 x 3 = 24 = 2 x 12. The LP says other sets fit and "5 in all": confirmed (5 sets with all eight numbers different; 108 if shapes may share a number).
- C12: the 0 to 99 chart is square; it is drawn on the 16:9 card with white space left and right (not tall, so no other ratio).
- Numbers inside the shapes sit on small white chips so the green ANSWER text stays readable on every shape colour.
- Coordinates in the specs are on a 1920 x 1080 canvas; arrays are exact counts, so the renderer should compute positions from the stated tile sizes and gaps.

## 2. LP text issues
Not edited, no decision changed because of them.

- M1.S3.T3.C7 (Let Us Think Q2): the question text does not say that the frame is "a two-digit number times a one-digit number" (three boxes); only the picture and solution step 1 say so. Suggested sentence: "Use the frame: a two-digit number times a one-digit number, with three boxes for the digits."
- M1.S3.T3.C11 (Q4): the question text has no number chart, but solution step 1 says "Use the number chart". Suggested sentence for the question: "Use the number chart from 0 to 99 (10 rows of 10)." or add the chart as a LaTeX array (the question diagram is `optional`, not added).
- M1.S3.T3.C11 / C12: clues (d) "I am an odd number" and (g) "My ones digit is even" cannot both be true, so no number fits all eight clues. The LP says exactly that (18 fits all but (d)). If (d) read "even", 18 would be the single answer; it may be a print slip in the book. Nothing to change in the LP; flagged for the teacher.
- M1.S3.T3.C9 (Q3): the question text gives (a) to (d) but the book prints no letters on the pictures. Suggested sentence: "The four pictures are lettered (a) to (d) in the order printed."
- M1.S3.T3.C13 (Q5): the nine numbers and four signs of the grid are only in the picture (now drawn). Optional sentence for the text: "The grid has the numbers 100, 25, 5, 10, 2, 36, 12, 4 and 3 and the signs -, x, +, ÷."
- M1.S5.T5.C17 (order of numbers): the text names (a), (b), "the two big arrays", (e), (f), (g); the book prints no letters c) and d). Fine as it is; the diagram follows the book.
- M1.S7.T7.C26 (Q2): the question text lists the table row "700 x 8 =" and the box "700 x 4 =" without saying they differ; only the solution (step 6) says so. Suggested sentence in the question: "The table row says 700 x 8 and the box says 700 x 4: do both."
- M1.S7.T7.C24 and C25: letters (a) to (h) are wrapped in LaTeX ($(a)$) but "(i)" is plain text, in the question and in step 9 of the answer. Suggested: write $(i)$ like the others.
- M1.S7.T7.C31 (multiplying by 1,000): step 3 speaks of "the place value board" that no text defines; the new diagram supplies it (nothing to edit if the diagram is kept).
- M1.S2.T2.C3, M1.S4.T4.C15, M2.S8.T8.C36: the worked examples use their own numbers (36 pouches, 7 x 12, 6 x 14) and have no book ref. Not wrong, just LP-authored; the book's own figures on those pages are 6 x 13 and 13 x 6 (page 3) and 18 x 5 (page 5).

## 3. Places where the book itself is unclear or wrong
- Page 4, Q2: the place value table row says "700 x 8 =" while the card above says "700 x 4 = _,_ 00". A print inconsistency. The LP solves both (2,800 and 5,600). No diagram is drawn for it (LaTeX table), so decision 1 changed no spec.
- Page 2, Q4: clues (d) and (g) contradict each other (see above).
- Page 2, Q5: the book does not say whether the same number may be used twice; the LP assumes two different numbers.
- Page 1, Q1: the book does not say whether different shapes may stand for the same number; the LP assumes different numbers.
- Page 3: the arrays have letters a), b), e), f), g) but none for the big pair; the pouches of Q3 (pages 1-2) have no letters at all.
- Base inventory fix: P01-shape_equations-1 says the white shape is a tall block with side tabs; in the picture the central block is wider than tall (about 3:2) with a small tab at mid-height on each side. The inventory entry starts with "CORRECTED:".
- Page 5, "Many Ways to Multiply": the figure P05-coloured_boxes-3 (18 in a blue box times 5 in a green box, children's strategies as text) belongs to the book section of topic M2.S8.T8, but the LP worked example there is 6 x 14. I mapped it to `none:TEXT_SUFFICIENT`; another chunk could claim the same figure for a nearby topic.

## Validator warnings (6, all expected)
`required but no inventory figure maps to it` for C3, C15, C21, C22, C36 (worked examples) and C31 (solution): their pictures are LP-authored and not printed in the book, so there is no base figure to map.
