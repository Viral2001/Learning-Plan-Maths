# Notes, chunk A (Class 8 Ch 1 "A Square and A Cube", plan cbse_eng_maths8_ch1_v45)

Result: 31 items (18 units: 5 worked examples, 13 question/answer pairs). Required 2, optional 0, none 29. Validator: errors 0 (7 warnings, all "long visible_text" for the dot-square captions such as '6 + 10 = 16 = 4²', which are the book's own captions).

The only required diagrams are the triangular-number question and its solution:
- `M2.S10.T10.C41` question, `M2.S10.T10.C41.IMG1`: the book figure on chapter p.7 (three dot squares 2x2, 3x3, 4x4 cut into 1+3, 3+6, 6+10 by a staircase, captions, then the EMPTY fourth square and EMPTY caption box).
- `M2.S10.T10.C42` solution, `M2.S10.T10.C42.IMG1` (derived_from C41.IMG1): same row, fourth square filled with 5x5 = 25 dots cut into 10 + 15, caption '10 + 15 = 25 = 5²' in ANSWER green.

Everything else is text/LaTeX: factor lists, arithmetic, number chains, a plain fill-in table, typeset equations, multiple-choice questions.

Note: the brief says this pdf has no printed-solutions section. It does: pdf pages 19 to 22 print the answers. For chunk A every printed answer is a number, a list or typeset equations (checked on pages 19 to 21); none is a picture. The LP solution text still wins where used.

## 1. Judgement calls

- C41/C42 required. The LP question text is numeric ("Add the next pair of consecutive triangular numbers after 6 and 10 ..."), but the book question is "Can you see any relation between triangular numbers and square numbers? Extend the pattern shown and draw the next term." The pattern exists only as the picture, and the book's answer is a drawing. I followed the book (FIG_REFERENCED, ACTION_ON_FIGURE, DATA_IN_FIGURE on the question; ANSWER_IS_FIGURE on the solution; the LP's own `q_figure` / `s_figure` hints agree that a figure was meant). The question figure keeps the fourth slot empty, exactly as printed, so it does not leak the answer. The row of single triangles 1, 3, 6, 10, 15 on the same page is a separate teaching figure and is not drawn here.
- Solution figure content: the book prints no answer for this question, so slot 4 is the pattern continued (the staircase rule of slots 1 to 3) and agrees with the LP solution (10 + 15 = 25 = 5²). The 10-dot group is the upper-right triangle and the 15-dot group the lower-left, as in slots 1 to 3.
- Inventory entry `NEW-P07-dot_pattern-3-sol` is the second use of the p.7 figure (the completed slot 4); it is not printed in the book, I added it so the required solution has an inventory figure.
- The captions are drawn as in the book (plain text under slots 1 to 3, the empty rectangle under slot 4 at caption level). The spec gives layout in dot-pitch units and says "scale to 92% of the card width"; with the 16:9 card the figure is wide and short, so there is empty space above and below.
- Concept-image mappings are accounting only and some are approximate: P06-dot_pattern-1 (visual proof panels) and P05-dot_pattern-3 both map to C25.IMG1; P07-dot_pattern-2 (triangles 1, 3, 6, 10, 15) maps to C37.IMG1 (the closest, a 5x5 square cut into 15 and 10); P02 boxes map to C2.IMG1 and C3.IMG1. Nothing is linked to any teaching image.
- P04-table-1 (squares of the first 30 numbers) and P07-table-1 (ten blocks of 100) are "given in question" but are plain fill-in tables, mapped `none:LATEX_TABLE`. No LP item in chunk A uses P04-table-1 as a figure; the LP question C39 does not ask for the ten-block table.
- Sibling consistency: the four Figure it Out items (Q2 = C23/C24, Q3 = C31/C32, Q7 = C43/C44, Q8 = C33/C34) are all none/none; all "last digit" and "zeros" questions (C17 to C24) are none/none.

## 2. Borderline

Apply the v3 rules as written; these are the calls where a reviewer might want the other answer:
- `M2.S10.T10.C41` / `C42`: required although the LP text carries all the numbers (see above).
- `M1.S3.T3.C8` / `C9` (which lockers stay open): none. The printed answer is the list 1, 4, 9, ..., 100; the 10x10 locker grid (C4.IMG1) is a teaching image and would only make the list nicer.
- `M1.S3.T3.C6` / `C7` (factors of 36): none. The book prints no answer picture; the pairs are LaTeX equations.
- `M2.S6.T6.C25` worked (sum of the first 8 odd numbers): none. An 8x8 dot square built from L shapes would help but the rule n² = sum is stated in the text and the 6x6 teaching image C25.IMG1 exists. Could be `optional` if the reviewer wants the figure.
- `M2.S6.T6.C26` worked (subtract odd numbers from 38): none. The book prints it as a chain of subtractions on a cream band; number chains are LaTeX.
- `M2.S8.T8.C33` / `C34` (pattern, Figure it Out Q8): none. The book's pattern and its printed answer are typeset equations with bold underline on the three filled numbers (21, 90, 91), not a drawn picture.
- `M2.S10.T10.C39` (blocks of 100): none. The book's ten-block table is a plain fill-in table.
- `M2.S9.T9.C35` worked (numbers between 25 and 36): none. The number line is a teaching image (C35.IMG1).
- `M2.S4.T4.C12` worked (areas for sides 6, 3/5, 2.5): none; three squarings.
- `M1.S2.T2.C2` worked (locker 12): none.

## 3. LP text issues

Not edited and no decision changed because of them (user decision 2).
- `M2.S7.T7.C31` (question) and its echo in `C32`: option (v) reads "15625 + 512" but the book prints "15625 + 51²" (superscript 2; pdf p.10 and p.20). Suggested: "(v): $15625 + 51^2$". The separators are also uneven: "(ii): $15625 + 26^2$ (iii): ..." has no semicolon before (iii). The LP answer (iv) 15625 + 251 is right.
- `M2.S10.T10.C41` (question): it never mentions the dot pictures, although the book question and the required diagram do. Suggested: "Look at the pictures: $1 + 3 = 4 = 2^2$, $3 + 6 = 9 = 3^2$ and $6 + 10 = 16 = 4^2$. Draw the next term: add the next pair of consecutive triangular numbers after $6$ and $10$ and check that the sum is a square." Its `q_figure` hint is also wrong: it says the picture shows triangles of 1, 3, 6 and 10 dots with the sums beside them; the question picture is the three dot SQUARES each cut into two triangles.
- `M2.S10.T10.C42` (solution): the steps never refer to the picture. Suggested first step (after the figure): "The $5 \times 5$ square of dots splits into a triangle of $10$ dots and a triangle of $15$ dots."
- `M2.S10.T10.C39` (question): the LP asks only for the squares between 101 and 200 and the largest square below 1000. The book asks to enter the number of squares in each of ten blocks of 100 (1-100 ... 901-1000) first. If full coverage of the book question is wanted, add: "Complete the table of the number of squares in each block of $100$, from $1$-$100$ to $901$-$1000$." (a LaTeX table).
- `M2.S5.T5.C24` (answer): `answer_tex` is "(ii): $108^2$ and (iii) $292^2$" (a colon after (ii) only). Suggested: "(ii) $108^2$ and (iii) $292^2$". The question text of C23 also has "(i): ... (iv): ..." with colons; harmless.
- `M2.S8.T8.C33` / `C34`: `book_number` is "Figure it Out, Q1" but the book's number is Figure it Out Q8 (ncert_ref `FiO1.q8`). The other Figure it Out items of this chunk are labelled "Square Numbers, Q2/Q3/Q7", so the same exercise carries two label styles; only the ids matter for the build.
- Mathematical checks (all hold): C2 12 has 6 factors; C7 36 has 9 factors; C12 (3/5)² = 9/25, 2.5² = 6.25; C18 31² = 961, 39² = 1521; C20 34² = 1156; C22 3000² = 9000000 (6 zeros); C24 and the book agree on 108², 292²; C25 1+3+...+15 = 64; C26 chain ends 2 - 13 = -11; C30 71 and 1296; C32 251 and 15876; C34 16+25+400 = 441 = 21² and 81+100+8100 = 8281 = 91²; C40 121, 144, 169, 196 and 31² = 961 < 1000 < 32² = 1024; C44 2 x 16 = 32, 2 x 99 = 198. No LP solution contradicts the book's printed answer.

## 4. Where the book is unclear

- Chapter p.7: the fourth slot of the triangular-number figure is an empty square (about the size of a 5x5 array at the same dot pitch) with an empty rectangle for the equation; the book prints no label or answer for it. The 5x5, 10 + 15 = 25 = 5² reading follows the pattern and the LP solution.
- Chapter p.4: column 3 of the table of squares has 8 empty cells (23² to 30²) with no printed labels; irrelevant to the decisions (LaTeX table, no LP item).
- P03-grid-2 (chapter p.3): no caption; checked on the page picture, it is a 5 x 5 grid of unit squares (6 + 6 lines), presumably the 5 x 5 = 25 square of the table.
- No print slips found in the book pictures or printed answers used by chunk A, so no "corrected value" is used in any spec.
