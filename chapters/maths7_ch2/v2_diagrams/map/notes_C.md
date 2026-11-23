# Chunk C notes (Class 7 Ch 2, topics M3.S20.T20 to M3.S23.T23)

Result: 31 items (15 pairs + 1 worked example). Required 2, optional 1, none 28. Validator: errors 0 (one harmless warning: the label "2 × 43 + 2 × 24" has more than 6 words).

## 1. Judgement calls

1. **Example 15 solution (M3.S22.T22.C97) and Example 16 solution (M3.S22.T22.C99): REQUIRED (the only two diagrams in this chunk).**
   The book prints the tray picture (Example 15) and the coloured array (Example 16) with their braces as the worked answer itself:
   per friend vs per item for Example 15, and 3 × 5 + 4 × 5 vs (4 + 3) × 5 for Example 16. The braces and colours carry the meaning of removing the bracket, which LaTeX cannot show reliably.
   The earlier authors' `s_figure` hints also expected these pictures. Same kind of answer in the same example set, so the same decision for both (sibling rule).
   This is the main decision to confirm. Both pictures duplicate the teaching images M3.S21.T21.C91.IMG1 and C92.IMG1. Those stay untouched and are not linked (v3).
   If the user wants no duplicate of a teaching image here, flip both solutions to `none` with `REUSES_CONCEPT_IMAGE` plus `LATEX_ARITHMETIC` (nothing else changes).
   Content notes:
   - The book's photographs are redrawn as flat schematics (trays as rounded boxes; cutlet as a SET_B circle; rasgulla as a white circle; fleur-de-lis replaced by plain dots).
   - The book's two small curved arrows over the left label (Example 15) and the right label (Example 16) are left out: their arrowhead targets are not clear in the printed figure (the inventory agents also flagged this).
   - The Example 16 colours follow the concept image C92 (scouts blue = SET_A, guides amber = SET_B); the book is green (top 3 rows, guides) and yellow (bottom 4 rows, scouts).
   - Given content is INK, SET_A, SET_B; braces and their labels are ANSWER green, because they are what the solution adds.
2. **Example 16 question (C98): OPTIONAL, not added.** The book says "(see the figure below)", but the LP question was rewritten to state every count (4 rows of 5 scouts, 3 rows of 5 guides), so a careful student loses nothing without the picture (tie-breaker). The array without braces would help; it is not needed to attempt. The solution figure draws the whole array itself (`derived_from` null). Example 15's question is `none` (the book's question gives no figure; the tray picture only appears in the explanation).
3. **Worked example C93 (10 × 98 + 3 × 98, 14 × 10 − 6 × 10): NONE.** The two book figures on page 17 (repeated additions of 98 and of 10 with braces and a strike-through) are written lines. LaTeX `\underbrace` says the same, so they are mapped `none:LATEX_ARITHMETIC` and the item is `no_image`. The question gives no figure.
4. **Figure it Out 2.3 Q1 to Q9, Examples 17 and 18, "third friend" and "use the method": all none, both sides.** Plain arithmetic, equalities and reasoning.
   - Q1's empty squares are sign boxes inside lines of text, not a figure. `text_alternative` suggests `\square` and `\underline{\hspace{1.2em}}`, one part per line.
   - Q7 and Q8 are open ended.
   - Example 18: the area picture of the teaching topic (C94.IMG1, a 100 × 25 rectangle) is not in the book and is never linked; the arithmetic is complete in text.
   - "Third friend" (Sangmu in the book, Tanvi in the LP): a three-tray picture is not in the book and would only be decoration.
5. **Base figures claimed (6, all checked against pages 16 and 17):** P16-term_marking-1 and P16-term_marking-4 (terms in ovals) and P17-braced_sum-1 and P17-braced_sum-2 are `none:LATEX_ARITHMETIC`; P16-arrangement-2 maps to the C97 solution and P16-array-3 to the C99 solution. I did not claim P14-table-1 (Tinker the Terms I, belongs to topic M3.S19.T19) or the page-19 figures (belong to topic M3.S24.T24). The base inventory has no entry for the empty sign boxes of FiO 2.3 Q1, and I added none (they are text).

## 2. Things in the LP that look wrong (not fixed here; nothing outside the two output files was edited)

- **M3.S20.T20.C73 (Q1) `question_tex`:** parts (a), (b), (d), (e), (f) run into one paragraph, for example `... \underline{\hspace{1.2em}} (b): ...` with no line break between (a) and (b). The boxes are the plain text `[ ]`, not `\square`. Each part should be on its own line.
- **M3.S20.T20.C74 (Ans1) `answer_tex`:** the `$` signs are unbalanced and the `;` separators are missing in two places: `$(c)$: $- (d)$: $-$, $4$` and `$-$, $- (f)$: $8$, $-$, $3$`. This renders "(c): −(d) ..." with (d) and (f) inside the maths. It should read `$(c)$: $-$; $(d)$: $-$, $4$` and `$(e)$: $-$, $-$; $(f)$: $8$, $-$, $3$`.
- **C77 (Q3) and C79 (Q4):** the question text is as in the book. Q4(b) prints `87 + 46 − 109` three times (an NCERT misprint, also in the book itself); the LP solution explains it as "the same written three times", which is consistent.
- **C84 (Ans6) (a):** the sentence "the right side must add 4 more than the left blank" is muddled (it should say the right blank is 4 more than the left blank, e.g. 423 + 0 = 419 + 4). The stated answer 423 + 419 = 419 + 423 is correct.
- **C82 (Ans5) (c):** correct (−22 − 12 + 10 + 22 = −2 as printed, and −22 − (12 + 10) + 22 = −22).
- **`video_media_id` on the answer concepts (C74, C76, C78, ...):** the ids point to the next concept's video (for example C74 carries `C75.VID1`); these are the stale references the user told me to ignore.
- **C93 worked example:** its text omits the book's printed typo "98 × 10 + 9 × 83 = 98 (10 + 3)", which is good.
- **Names:** the LP uses Meera and Kabir (the book: Lhamo and Norbu), Tanvi (the book: Sangmu) and Meera (the book: Jasoda). The diagrams draw no names.
- **All arithmetic in this chunk was re-checked:** 2 × 67 = 134 and 86 + 48 = 134; 2 × 43 + 24 = 110; 20 + 15 = 35 = 7 × 5; 5 × 4 + 3 = 23; 63 × 18 = 954 + 180 = 1134; 97 × 25 = 2500 − 75 = 2425; 3 × 67 = 201; 95 × 8 = 760; 104 × 15 = 1560; 49 × 50 = 2450; the Q7 value set {10, 6, 4, 0, −4, −6}.

## 3. Where the book itself is unclear

- Page 15, FiO 2.3 Q4(b): the first three expressions are printed identically (`87 + 46 − 109` three times); the book probably meant three reorderings of the same terms. No figure is involved.
- Page 16, the two curved arrows over the labels 2 × (43 + 24) and (4 + 3) × 5: the arrowhead targets are not clear.
- Page 16: the book does not name the colours' groups; green = guides (top 3 rows) and yellow = scouts (bottom 4 rows) follow from the row counts in the text and the braces.
- Page 17: "98 × 10 + 9 × 83 = 98 (10 + 3)" is a printing error in the book (should be 98 × 10 + 98 × 3). It is not in the LP and no figure uses it.
