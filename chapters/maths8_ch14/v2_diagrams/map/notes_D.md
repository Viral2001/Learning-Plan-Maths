# Chunk D notes (Class 8 Ch 14 "Area")

Units: M2.S22.T22 (Figure it Out Q4-Q8 of the trapezium set), M3.S23.T23.C85 (worked example, km2), M3.S24.T24 (Areas in Real Life: 3 pairs + 4 singles).
Result: 25 items: required 8 (solutions of Q4, Q5, Q6, Q7, Q8; questions of Q5, Q7, Q8), optional 0, none 17. Validator: errors 0, 2 warnings (Q4 and Q6 solution diagrams have no printed book figure, as expected).

## Borderline
- **C79 (Q5) solution, required.** The book's question figure already draws the whole construction (dashed rectangle EFGH). The solution diagram only adds the four shaded congruent corner triangles AHI, DGI, BEJ, CFJ (the LP steps rest on them). Could be `SAME_AS_QUESTION_DIAGRAM` if the team wants fewer images.
- **C81 (Q7) solution, required.** Adds the three missing radii (so six equal triangles are visible) and colours the three pieces; the LP steps count 3, 1 and 2 triangles. No counts are printed in the picture (a number inside one small triangle would look like a count for that triangle only).
- **C82 (Q8) solution, required.** Adds the shaded triangles ZYA and BXA and the equal-angle arcs (single arcs at A, double arcs at Y and X). Same kind of answer as Q5, so the same decision.
- **C78 (Q4) and C80 (Q6) solutions, required** although the question side has no figure (word questions): the printed/LP answer is a dissection (Q4) and a constructed trapezium (Q6), Step B2 `ANSWER_IS_FIGURE`. No question diagram for either.
- **C78 (Q4) solution is one card with two panels** (cut and moved pieces on the left, finished rectangle on the right). Letters a, b, h come from the LP text; the drawing uses a = 4, b = 8, h = 4 only as proportions and prints no numbers.
- **C80 (Q6) solution:** the LP gives parallel sides 8 cm, 16 cm and height 12 cm only. I drew an isosceles trapezium (slant is my choice, any slant gives area 144); the 12 by 12 rectangle of the LP steps is not drawn.
- **C90 (pair Q2, "1 in² to square centimetres"), solution none.** The book's picture of two squares (1 in and 2.54 cm sides, base figure P23-shape-3) is the book's teaching explanation inside the section text; the pdf has no printed-solutions section and the question itself gives no figure. I mapped the figure to the teaching image C84.IMG1 (accounting). If the team counts that picture as a printed answer (Step B2), C90 solution becomes required: two equal squares, left "1 in" by "1 in", right "2.54 cm" by "2.54 cm", area labels "1 in²" and "6.4516 cm²". Sibling C93 (1 ft² = 144 in², no book figure) stays none either way.
- **C88 (A4 sheet) solution none:** a 3-by-4 layout of sheets would be nice to see, but all numbers are in text and the teaching image C83.IMG1 already shows it. Not even `optional`.
- **C85 worked example none:** an 8 m by 6 m classroom rectangle is not needed for 8 × 6 = 48 and 1000000 ÷ 48 (kept teaching image C85.IMG1 shows the km2 square).
- **C95 / C96 (largest / smallest city):** open research tasks, none on both sides (the video's empty city/area table is a plain table).

## LP text issues
- **C78, C79, C80, C81, C82:** `book_number` says "Figure it Out, Q1" for all five; they are Q4, Q5, Q6, Q7, Q8 of the trapezium Figure it Out (the LP's own ncert_refs say FiO5.q4 to q8). **C93, C94, C95, C96:** `book_number` says "Areas in Real Life, Q1" for all four; they are in-text questions 2 to 5. The pair C91/C92 (the quotient 161.29 ÷ 6.4516) also carries "Areas in Real Life, Q1". Metadata only.
- **C78 (Q4):** the LP steps use a, b and h without defining them. Suggested sentence at the start of the steps: "Let the parallel sides be a (top) and b (bottom) and the height h."
- **C79 (Q5):** the question text does not say that I and J are the midpoints of AD and BC; the book shows this only by dots and tick marks in the figure. Suggested sentence: "In the figure, I and J are the midpoints of the slanting sides AD and BC, and EFGH is a rectangle."
- **C81 (Q7):** the question says "as shown" but the LP text carries no figure; the new question diagram supplies it (no text change needed once the token is placed).
- **C87 (A4 sheet):** the question does not state the sidelengths that the solution uses. Suggested sentence: "An A4 sheet has sidelengths 21 cm and 29.7 cm." Also "3 rows of 4 sheets" is the LP's own concrete choice; the book leaves the table to the learner.
- **C89 (conversions):** the question does not give "1 in = 2.54 cm", which every step uses. Suggested sentence: "(1 in = 2.54 cm)". The LP also keeps only 5 in and 11.43 cm of the book's four lengths (5 in, 7.4 in, 5.08 cm, 11.43 cm).
- **C94 (times bigger):** the question speaks of "your village/town/city" and "your school" but the solution computes with an example (school ground 100 m by 80 m, town 10 km²) that the question does not state. Suggested sentence: "For example, take a school ground of 100 m by 80 m and a town of 10 km²."
- **C85 (worked example):** "1000000" and "20833" are written without separators while the book prints "43,560"; minor style point.

## Book unclear / book vs base inventory
- **Q5 figure (P22-shape-5):** the base inventory calls the trapezium isosceles. The page picture shows it is not (A is about 2 units right of D, B about 4 units left of C; the two overhangs differ), which is why a rectangle EFGH is needed through the midpoints I and J of both sides. Corrected in the inventory entry and drawn not isosceles. That I and J are midpoints is shown only by the dots and the tick marks, not by the text.
- **Q8 figure (P23-shape-2):** no measures printed. In the book drawing XB equals ZY (as the proof needs). My drawing keeps the same relations but is a little taller (height 4 against about 2.5 in the book) so the card is better filled; spec is `to_scale: false`.
- **Q7 figure (P23-shape-1):** the book shows no centre and no letters; the base description matches the page picture.
- **No book mistake found** in the pages of this chunk (print slips): the printed numbers I used (2.54, 6.4516, 161.29 ÷ 6.4516 = 25, 21 × 29.7 = 623.7) all check.

## Inventory and merge notes
- Figures claimed (9): P22-shape-5 and its second use NEW-P22-shape-5-sol, P23-shape-1 and NEW-P23-shape-1-sol, P23-shape-2 and NEW-P23-shape-2-sol (6 to items); P23-shape-3 to teaching image M3.S23.T23.C84.IMG1 (1); P26-table-1 and P28-grid-1 as `none:OPEN_ENDED` (2).
- **P26-table-1 and P28-grid-1** are the blank Learning Material Sheets after the last section; they belong to no unit of any chunk, so I claimed them here to keep the merged inventory complete. If another chunk also claims them the merge keeps both as separate uses; they can simply be dropped from this file if that is unwanted.
- P22-shape-1 to 4 (Q3, areas of four figures) belong to chunk C (C76) and P21-shape-* to chunk C; not claimed here.
- Media ids: single-diagram solutions C78.IMG1 and C80.IMG1; question and solution pairs C79.IMG1/IMG2, C81.IMG1/IMG2, C82.IMG1/IMG2; the build renumbers them in media-list order as usual.
