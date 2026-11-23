# Notes, chunk C (Class 7 Ch 6 Number Play, plan cbse_eng_maths7_ch6_v62)

Result: 39 items = required 13 (4 question, 9 solution) / optional 0 / none 26. Validator: errors 0, warnings 0.
Required: questions C83, C85, C87 (generalised form), C98 (Chautisa Yantra); solutions C75, C77, C79, C84, C88, C90, C92, C94, C99.

## 1. Judgement calls

1. **gFiO Q1, Q2, Q3: question figure = the generalised form, `required` (C83, C85, C87).**
   The book says "using this generalised form" and the LP question texts do not state the form (m + 3, m - 4, ...). I treated it as FIG_REFERENCED / DATA_IN_FIGURE and drew it (three identical specs, `render_note` "same as C83"). The 'refer picture' exception (question `optional`) does not fit: the book's answers here are the answer squares, not "see picture". The other reading: question `optional` / `none` with the form written into the question text (the form is also in teaching image M3.S15.T15.C80.IMG1 and in the text of C80). If the user prefers that, set these 3 question items to `optional` with REUSES_CONCEPT_IMAGE and fix the LP text; the solution diagrams of C84 and C88 are derived_from them and would then be standalone.
2. **C84 (m = 25) keeps the form's expressions (INK) and adds the numbers (ANSWER) in the same cell positions**, so the solution is derived_from the question figure without moving anything. C88 (Q3) is two panels (adding 1, doubling) that reuse the form's cell order. C88 doubles the ORIGINAL form (book (b) and the LP steps), see 2.5.
3. **C75 solution draws all 8 squares** (1 pattern turned 0/1/2/3 quarter turns, and each flipped), because the LP/video answer is "8 magic squares"; the book's one printed square is the first of them. I checked the 8 against the video's list of 8 squares and each adds to 15.
4. **C79 solution draws four squares: 1 to 9, 2 to 10 (add 1), 3 to 11 (add 2), 9 to 17 (add 8).** The book prints only the first two; the 3 to 11 and 9 to 17 squares come from the LP video answer (magic sums 21 and 39).
5. **C99 solution is four panels, not one grid**, because the four groups overlap (7, 13, 12, 8, 9 each sit in two groups) and rings would clash. Every panel reuses the question grid's numbers and cell order; `derived_from` is set, but the layout is a 2 x 2 arrangement of that grid. The LP steps name four groups (corners, centre block, top-left 2 x 2, broken diagonal 12 + 8 + 5 + 9); the earlier author's `s_figure` hint named only three. I drew the four of the LP steps.
6. **C78 (6.3 Q4, "what other operations") is none/none.** Book answer is one sentence and the LP answer a list of operations: no picture, unlike Q1, Q2, Q3, Q5 whose printed answers are squares. The video's example squares would only be "nice". Sibling difference stated in the item.
7. **C86 solution (3m) is none** (SAME_AS_QUESTION_DIAGRAM + LATEX_ARITHMETIC): printed answer is the text 3 x m, steps are algebra. A highlighted top row would only repeat the question.
8. **C109 solution (staircase) is none, LATEX_TABLE.** The book prints the answer as a plain 2-column table (example paths | 1, 7, 15, 10, 1). I did not apply "printed answer is a picture" because the brief says plain tables stay LaTeX; `text_alternative` gives a small LaTeX array if the LP wants the table. If the user wants the printed table drawn, it is the only item where the call is close.
9. **Cryptarithms (worked C116-C118, questions C120, C122, C124) are none, LATEX_ARITHMETIC.** The column layout is expressible as a LaTeX array and is already a teaching image (M5.S24.T24.C114/C115.IMG1). Their base figures map to `none:LATEX_ARITHMETIC` where an item of mine uses them; P17-cryptarithm-2 (K2 + K2 = HMM) is not used by any of my items and maps to the concept image.
10. **Magic-sum tags** under the single squares ("magic sum 18", "magic sum 75", "magic sum 60", "magic sum 0", "line sum 45") are 3-word tags using the LP's words. C92 says "line sum 45" because the LP step says "every line sum ... 45".
11. **Figure claims.** I claimed 6.3 figures from page 11 on (P11 to P13: generalising grid, Chautisa Yantra, history), all 6.4 and 6.5 figures (P14 to P17), and the printed-answer pictures of my units (P18 cryptarithm, P25 to P28, P30 magic square, P31 table, P32 cryptarithm). **Not claimed:** the 6.3 teaching figures of pages 7 to 10 (P07 to P10, chunk B topics T10, T11, T13) and the 2 x 3 parity grid of end Q3 (P18-sum_grid-1, P30-sum_grid-1, P30-sum_grid-2, chunk B's end.FiO3). If chunk B skips P08-grid-3 or P09/P10 grids, the merged check will name them.
    Extra entries I added: NEW-P11-grid-2-sol (the Yantra grid redrawn in the C99 solution), NEW-P27-magic_square-2-q2 and -q3 (the generalised form as the given figure of gFiO Q2 and Q3).
    Photographs not inventoried (as the base rule says): the Chautisa Yantra stone slab (p11) and the Palani pillar (p12).
12. **P25-magic_square-3, P26-magic_square-1/-2** (printed answers of Figure it Out Q3 a, b): the LP has no question item for Q3. P25-3 (start square) and P26-1 (+1 square, same as the Q2 answer) are accounted to concept image M3.S12.T12.C71.IMG1 / to C77's solution; P26-2 (doubled square) maps to `none:TEXT_SUFFICIENT` (the result is only stated in text of concept C71).

## 2. Things in the LP that look wrong

1. `book_number` errors: C75 'Figure it Out, Q1' is right, but C76/C77 (book Q2, ncert_refs also FiO3) say 'Figure it Out, Q1', C78 (book Q4) says Q1 and C79 (book Q5) says Q1. Concept names of C76/C77 say 'Q1 / Ans1'.
2. **C75, C78, C79 are empty blocks**: `question` and `steps` are empty, the card shows only the title ("Figure it Out 6.3, Q1"). The learner never sees the question text. I flagged these `needs_lp_text_sync: true` and gave the question text in `text_alternative`. C79's video id points into another concept (M3.S12.T12.C71.VID1).
3. **C75 answer contradicts the book**: book 'exactly one unique magic square (ignoring rotations and reflections)', LP/video '8 magic squares (1 pattern, turned and flipped)'. Both are true; the LP says both in the video. LP followed.
4. **C83 (gFiO1) question text lacks the form**, and C98 ("Find other groups of four that add to 34") does not name the Yantra grid, so the question is not answerable from its own text. The diagrams fix the data; the text could also name the form / the Chautisa Yantra.
5. **C87 (gFiO3) question text contradicts the LP solution**: the question says "add 1 to every term, then double every term" (one combined change, which would give 2m + 8, 2m - 6, 2m + 4 / ...), but the LP steps (and the book: (a) add 1, (b) double, separately) double the ORIGINAL form (2m + 6, 2m - 8, ...). I followed the LP solution and the book and flagged `needs_lp_text_sync` on the question item (suggest: "(a) Add 1 to every term. (b) Double every term.").
6. **C123 steps_tex[0]** has `$A 2$-digit` (the word A inside math mode); should be `A $2$-digit`. **C125 steps_tex** writes "the $A_0$ part of $TAT$" (renders A with a subscript 0; the plain text says "A0") and "$1 +$ A" (A outside math mode).
7. C121: "only T = 5 works" ignores T = 0 (3 x 0 ends in 0); it is excluded because UT is a 2-digit sum. A short "the sum has 2 digits" would close it.
8. T16 Q3: the book's (a) and (b) are two separate parts; the LP merged them into one item (see 5).
9. T14 has no separate item for book Q3 (increase by 1, double); C77's solution covers only the "add 1" part (pairs with Q2), the doubling appears only as text in concept C71.

## 3. Where the book itself is unclear

- Page 29 (answer key): "144 + 233 = 3779" is a misprint for 377; the LP's 377 is right (C105).
- The answer key pictures for Q3(b) (p26) and gFiO Q3(b) (p28) are cut off at the bottom border in the scan; read as ordinary 3 x 3 tables.
- Navagraha Yantra (p12): Ketu's bottom-left cell prints 19, which breaks that square (it would be 10); nothing of mine draws it.
- The Lo Shu turtle's dot counts (p12) are too small to count; not used.
