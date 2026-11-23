# Chunk C notes (Class 8 Ch 9, topics M3.S9.T9, M3.S10.T10, M3.S11.T11)

Result: 21 units, 31 items. Required 2 / optional 1 / none 28. Validator `--chunk C`: errors 0, one warning (C57 has a required solution figure with no book figure behind it, which is expected: the book prints no picture for that question).

| Role | required | optional | none |
|---|---|---|---|
| question | 1 (C60) | 0 | 9 |
| solution | 1 (C57) | 1 (C88) | 8 |
| worked_example | 0 | 0 | 11 |

## Figures claimed (Step 0)

Only ONE base figure belongs to this chunk: `P21-shape-1` (Chapter Exercises Q2, triangle (a), right angle marked, sides 7 and 9, third side unlabelled) -> `item:M3.S9.T9.C60 (question)`. I checked the base description against `book/page_21.png`: it is correct (right angle bottom-left, "7" on the left side, "9" under the bottom side, tilted about 10 degrees anticlockwise, no "?" on the third side). No correction needed.

Figures I did NOT claim, so the merge does not get a clash (the merge check needs them claimed by chunk B):
- `P21-shape-2` to `P21-shape-6` (triangles (b) to (f)): the LP puts parts (b)-(f) of Chapter Exercises Q2 in `M3.S8.T8.C55` blocks 5-9 (chunk B), not in C60. The unit's `ncert_refs` list all six parts only because of how the pair was collected; its text is part (a) only.
- `P15-shape-1` (the 3 cm / 4 cm / "?" triangle of the teaching text "Using Baudhayana's Theorem"): belongs to `M3.S8.T8.C53` (chunk B, concept image C53.IMG1 shows the same triangle with 5 cm).
- Pages 16, 17 and 18 (section 2.5) have no figure at all (checked on the three page pictures); page 21 has no figure for Q4, Q5, Q6 either.

## Decisions in short
- C60 question: required. C61 solution: none. C57 solution: required (a construction). C56, C58, C62 and all T11 questions: none (no given figure). T10: all 11 worked examples none (arithmetic and algebra; the book shows only equations). C88 solution: optional (not added).

## Borderline (v3 rules applied as written, user decision 4)
1. **C60 question (Chapter Exercises Q2 (a)) - required although the LP text carries 7 and 9.** The book gives a drawing (right angle marked, two labels, the third side blank); "in the following right triangles" refers to it. Kept required (FIG_REFERENCED, DATA_IN_FIGURE, SPATIAL_GEOMETRY). The figure follows the book: no "?" on the third side.
2. **C61 solution - none with SAME_AS_QUESTION_DIAGRAM.** The only addition would be the label sqrt(130) on the hypotenuse. Step E "typical pairs" (figure-based question, numeric answer: Q required, S none) and the tie-breaker (a careful student follows the text equally well) give none. It could be argued as required (value filled in on the figure). **Cross-chunk consistency:** parts (b)-(f) of the same question sit in chunk B (`M3.S8.T8.C55` blocks 5-9); their solutions should get the same decision as C61. If the merge reviewer wants the answer written on every triangle, C61 flips to required with `derived_from` = `M3.S9.T9.C60.IMG1` and the label `sqrt(130)` at about (4.244, 5.024) in ANSWER green (the coordinates are in the C60 spec).
3. **C57 solution (Figure it Out Q2, 8 cm side and 17 cm hypotenuse) - required.** The question has no figure but tells the student to draw the triangle and measure, and solution step 1 is that construction (side 8, right angle at one end, arc 17 from the other end, third side about 15). The figure draws the finished construction (arc in GUIDE, 15 cm in ANSWER green), `derived_from` null because the question has no figure. Reason codes SPATIAL_GEOMETRY + ANSWER_IS_FIGURE. Argument for none: the final answer is a number and the drawing is the student's own work. Chose required because Step B2 says a construction described in words still gets its picture. **Cross-chunk consistency:** Figure it Out Q1 (5 cm and 12 cm, "first draw the right-angled triangle ... and measure") sits in chunk B (`M3.S8.T8.C55` block 0); if its LP solution also describes a drawing, the same decision should apply.
4. **C88 solution (Chapter Exercises Q6, rectangles with integer diagonals) - optional, not added.** A rectangle with one diagonal (sides a, b, diagonal c) would help step 1, but the answer is a list of five triples carried by text and LaTeX.
5. **C73 (why (n - 1)^2 + (2n - 1) = n^2) - none.** The L-shape picture already exists as the teaching image `M3.S10.T10.C73.IMG1` (kept, never linked). The book itself shows only equations here, so no figure is invented.
6. **C65 (pattern among (3,4,5), (6,8,10), ...) and C70 (scaled versions) - none.** Plain lists of numbers; a LaTeX array does the job (LATEX_TABLE for C70). `text_alternative` says what to write.
7. **Q4 (i) pair (C58/C59) - none/none.** The question is symbolic (a = 5, b = 7), no figure in the book, the solution is arithmetic and two decimal bounds.

## LP text issues
- **M3.S9.T9.C60** (question, "Chapter Exercises, Q2 (a)"): the text says "Find the missing sidelengths in the following right triangles:" but lists only part (a) (plural "triangles"). Parts (b)-(f) are separate blocks in `M3.S8.T8.C55`; the same NCERT question is split over two topics (T9 for (a), T8 for (b)-(f)). Suggested sentence for C60: "Find the missing sidelength in this right triangle: the sides at the right angle are 7 and 9." Also the same for **C58** (Q4 (i) here, (ii)-(v) in `M3.S8.T8.C55` blocks 1-4): "Find the missing sidelength when a = 5 and b = 7."
- **M3.S9.T9.C58** `question_tex` / `text`: "Let a, $b$ and $c$ ..." the first letter is outside math mode. Suggested: "Let $a$, $b$ and $c$ denote the lengths of the sides of a right triangle, with $c$ the hypotenuse. Find the missing sidelength when $a = 5$, $b = 7$." Also "(i):" has a stray colon.
- **M3.S9.T9.C60**: `question_tex` has "$(a)$:" with a stray colon before the description.
- **M3.S9.T9.C63** `steps_tex[1]`: "so $c$ is more than a." The letter a is plain text; suggest "$a$". Same for "more than a" in the plain `steps`.
- **M3.S11.T11.C77** `question_tex` / `text`: "Is $(3k$, $4k$, $5k) a$ Baudhayana triple ..." has the closing bracket and the word "a" inside the last math segment. Suggested: "Is $(3k, 4k, 5k)$ a Baudhayana triple for every positive integer $k$?"
- **M3.S11.T11.C80** `steps_tex`, `answer_tex`, `text`: triples are written as "$(7$, $24$, $25)$" (brackets and numbers split over three math segments). Suggested: "$(7, 24, 25)$" and so on.
- **M3.S11.T11.C84** `steps_tex` and `answer_tex`: same split-bracket style "$(8$, $15$, $17)$". Suggested: "$(8, 15, 17)$".
- **M3.S11.T11.C86** `steps_tex[0]`: "greatest common factor of a, $b$ and $c$" - the first "a" is plain text. Suggested: "of $a$, $b$ and $c$". `steps_tex[2]` writes "$(\frac{a}{f}$, $\frac{b}{f}$, $\frac{c}{f})$": suggested "$\left(\frac{a}{f}, \frac{b}{f}, \frac{c}{f}\right)$".
- **M3.S11.T11.C88** `answer_tex`: "$6$ by $8 (10)$" mixes math and text brackets; suggested "$6$ by $8$ (diagonal $10$)" and the same for the other pairs.
- **M3.S9.T9.C57** `steps_tex[0]`: "the third side measures about $15\text{ cm}$" is right for a measurement; step 4 gives the exact 15 (17^2 - 8^2 = 225). No change needed, but the figure shows "15 cm" and the spec says so.
- Book numbers are fine (Q2, Q4 (i) in Figure it Out of section 2.4; Triples Q1-Q3 of section 2.5; Chapter Exercises Q2 (a), Q4, Q5, Q6). `M3.S10.T10.C64` to `C75` have no `book_number` (they are in-text worked examples), as expected.
- Maths re-checked (all hold): 17^2 - 8^2 = 225 = 15^2; 5^2 + 7^2 = 74 with 8.6^2 = 73.96 and 8.7^2 = 75.69; 7^2 + 9^2 = 130 with 11.4^2 = 129.96 and 11.5^2 = 132.25; 15^2 + 36^2 = 39^2; the six triples up to 20; the scaled lists of C70; the five odd-square triples of C80 (7,24,25), (9,40,41), (11,60,61), (13,84,85), (15,112,113); the three examples of C84 and their gaps; the five rectangles of C88.
- No concept in this chunk has a "refer picture" answer; no concept image is linked anywhere.

## Places where the book is unclear
- The six triangles of Chapter Exercises Q2 are "not to a common scale or orientation" (base inventory note) the book prints no `?` on the missing side, and every triangle carries a right-angle mark. For (a) I follow the printed picture: the tilt (about 10 degrees) and the proportion 7 : 9 are kept; the third side stays blank.
- Figure it Out Q2 of section 2.4 says "try drawing the triangle and measuring". The book shows no picture and prints no answers; the answer 15 cm comes from the LP solution (and the maths).
- The book's page 15 figure for the 3 cm / 4 cm triangle has no right-angle mark (base inventory note); it is not in this chunk.
