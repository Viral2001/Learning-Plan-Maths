# Chunk B notes (Class 6 Ch 5 "Prime Time", plan v75)

Result: 20 items, required 3 / optional 0 / none 17. All three required items are worked examples
(M2.S8.T8.C45, M2.S8.T8.C46, M2.S11.T11.C57). Validator (`--chunk B`): errors 0, warnings 0.
Media ids: `M2.S8.T8.C45.IMG2`, `M2.S8.T8.C46.IMG2`, `M2.S11.T11.C57.IMG2` (IMG1 of each concept is a kept teaching image).

Figures claimed (Step 0): P06-arrangement-1 (to C45), NEW-P06-arrangement-1-C46 (second use of P06, to C46),
P07-number_grid-1 (to C57). I did not claim the other figures of book section 5.1 (P01-P05) or the printed-answer
pictures (SOL23, SOL25, SOL33): they belong to units of other chunks. I looked at pdf pages 5, 6, 7, 8, 9 and the
printed solutions on pages 24-27: the solutions of my units contain no picture. The base descriptions of P06 and P07
match the page pictures (no correction needed). P07 is also used by Figure it Out 5.2 Q2/Q3 (chunk C): at merge it is
the same book picture; I took the base id for the first use in LP order (C57 comes first).

## 1. Judgement calls

- **C45 (worked, "Packing figs")**: required. The answer to "think and find out the different ways" is a set of
  arrangements (ANSWER_IS_FIGURE, B2), so I draw the book's picture: three orange rectangles of 12 (12 rows x 1, 6 rows x 2,
  4 rows x 3) and one blue row of 7 (1 x 7), laid out exactly as printed (tops of the three 12-rectangles level, Anshu's row
  on the bottom line, right edge of the row under the right edge of the 3 x 4 block). No labels, as in the book. The picture
  shows the answer inside a worked example, which is fine because the example shows its answer anyway. Kept teaching image
  C45.IMG1 (3 x 4 dots + row of 7) shows only one 12-arrangement, so it does not replace this one.
- **C46 (worked, "Rows and columns are factors")**: required, FIG_REFERENCED: "each of the arrangements" can only be read
  from the picture. Identical spec to C45 (rule: one diagram per item), including Anshu's row of 7 because it is part of
  the printed picture. No row/column counts are written; the learner has to count them.
- **C57 (worked, sieve)**: required. The book prints only the FINISHED 10 x 10 table (25 primes circled, 75 cells crossed),
  so the diagram is the finished state (not a blank grid, not a step-by-step series: the worked example has one diagram only).
  Colours: circles ANSWER green (as the book), crosses GUIDE grey instead of the book's red because WRONG is reserved for wrong
  cases. Every number printed in the cells is drawn (visible_text = 1..100). Counts recomputed in code: 25 primes, 75 crossed,
  per row 4, 4, 2, 2, 3, 2, 2, 3, 2, 1.
- **C58 (worked, "Why the sieve works")**: none (TEXT_SUFFICIENT), not optional. The question points at the written steps, the
  answer is reasoning in words, and the finished grid sits in the example directly before. If the user wants the grid repeated
  here (so the learner can watch each step), it would be a copy of the C57 diagram: change to required with the same spec.
- **C49/C50 (21 to 30)**: none/none. No figure in the book (only a bullet icon), the range is in the words, the answer is a
  count. The row of 21..30 already exists as the teaching image of the topic (C47.IMG1), which is not linked.
- **C42, C44 (common factors)**: none. A factor Venn diagram would only be extra; the printed answers are plain text.
- **C43 (treasures on 28 and 70)**: none. The book draws no number line here; the jump idea is taught by the 5.1 concept images.
- **C56**: the answer concept still has two old cards (IMG1, IMG2); both are dropped (five True/False sentences, no picture).
- Sibling check: C51-C56 (Figure it Out 5.2 Q1, Q4, Q9) all none; C37-C44 (Figure it Out 5.1) all none; the two worked examples of
  T8 are both required.

## 2. Things in the LP that look wrong or thin

- Questions C37, C41 and C55 (and the matching answer concepts) repeat the statements twice: the text ends with a second
  copy such as "(a): Number less than 40, a factor is 7, digit sum 8; (b): ..." / "(a): 20 and 28; (b): ...". The same text
  appears in `question_tex` and `text`. Not touched here (no diagram effect), but worth a text clean-up.
- C56 `answer_tex`: "a True, $b$ False, $c$ False, $d$ False, $e$ True" mixes plain "a" with maths-mode letters and lacks the
  "(a)" form the steps use.
- C44 solution step is only "Common factors of 28 and 70." with the answer 1, 2, 7, 14: it does not show the factor lists
  (28: 1, 2, 4, 7, 14, 28; 70: 1, 2, 5, 7, 10, 14, 35, 70). Facts checked, answer is right. A text line would help (see the
  item's `text_alternative`).
- LP numbering differs from the book: T7 "Q1..Q4" are the book's Figure it Out 5.1 Q2, Q3, Q4, Q7 (the book's Q1, Q5, Q6 sit in
  T3); T10 "Q1..Q3" are the book's Figure it Out 5.2 Q1, Q4, Q9. The LP's own `book_number` and `ncert_refs` already point to the
  right book questions; I used both in `ncert_ref`.
- Every LP answer in this chunk matches the book's printed answer (35, 45; 6; the four common-factor sets; 1, 2, 7, 14;
  2 primes and 8 composites; No; 23 and 37; T, F, F, F, T; 25 primes up to 100). I recomputed each.

## 3. Places where the book is unclear

- P06: the left edge of Anshu's purple row sits a few pixels right of the left edge of the 2 x 6 block in print; I aligned
  both on the same line (x = 3) and said so in `render_note`. The picture has no labels and the question text does not say
  which rectangle is which; the book's own sentences (12 = 2 x 6, "7 x 1 or 1 x 7") fix the reading rows x columns.
- P07: a few crossed cells (30, 49, 91, 94) show one diagonal stroke in print instead of a full X; the diagram draws a full X on
  all 75 crossed cells (base inventory checked this by pixel analysis).
- The figure in the book is the finished state, while the surrounding text describes steps 1 to 5; the book prints no
  intermediate stage, so none is drawn.
