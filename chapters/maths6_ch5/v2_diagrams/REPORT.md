# Class 6 Ch 5 Prime Time - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths6_ch5` v75 (taken from staging). Result: new V2 version v76 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (167 items from 96 units)
{"worked_example": {"none": 19, "required": 6}, "question": {"none": 61, "required": 10}, "solution": {"none": 62, "required": 7, "optional": 2}}

Optional, NOT added: [('C61', 'solution'), ('C63', 'solution')]

needs_lp_text_sync: []

## The 23 diagrams
| id | side | type |
|---|---|---|
| M1.S3.T3.C12.IMG1 | question | other |
| M1.S3.T3.C13.IMG1 | solution | other |
| M1.S3.T3.C20.IMG1 | question | other |
| M1.S3.T3.C21.IMG1 | solution | other |
| M1.S4.T4.C26.IMG1 | question | other |
| M1.S4.T4.C27.IMG1 | solution | other |
| M1.S4.T4.C30.IMG1 | question | cell_grid |
| M2.S8.T8.C45.IMG2 | worked example | cell_grid |
| M2.S8.T8.C46.IMG2 | worked example | cell_grid |
| M2.S11.T11.C57.IMG2 | worked example | cell_grid |
| M2.S12.T12.C60.IMG1 | question | cell_grid |
| M2.S12.T12.C62.IMG1 | question | cell_grid |
| M3.S16.T16.C95.IMG1 | worked example | factor_tree |
| M3.S16.T16.C96.IMG1 | worked example | solid_3d |
| M4.S32.T32.C181.IMG2 | worked example | cell_grid |
| M4.S33.T33.C184.IMG1 | question | cell_grid |
| M4.S33.T33.C185.IMG1 | solution | cell_grid |
| M4.S33.T33.C186.IMG1 | question | cell_grid |
| M4.S33.T33.C187.IMG1 | solution | cell_grid |
| M4.S33.T33.C188.IMG1 | question | cell_grid |
| M4.S33.T33.C189.IMG1 | solution | cell_grid |
| M4.S33.T33.C190.IMG1 | question | cell_grid |
| M4.S33.T33.C191.IMG1 | solution | cell_grid |

### Chunk A notes (from the decision agent)
# Chunk A notes (Class 6 Ch 5 "Prime Time", plan cbse_eng_maths6_ch5_v75)

Result: 18 units, 32 items. Required 7 (questions C12, C20, C26, C30; solutions C13, C21, C27), optional 0, none 25. Validator: errors 0, one expected warning (C27, the printed book has no answer picture for it).

Figures claimed (8): P01 (none, decorative ring), P02 (C12 question), NEW-P02-venn_diagram-1-C26 (C26 question, second use of Fig. 5.1), P03 (concept image C32.IMG1), P04 (C30 question), P05 (C20 question), SOL23 (C13 solution), SOL25 (C21 solution). The other base figures of chapter pages 1-5 and solutions pages 23-25 are all in this list; P06 onward belong to other chunks.

## 1. Judgement calls

1. **Fig. 5.1 has 6 added (C12 and C26 question diagrams).** The printed figure leaves 6 out of the left circle (a print slip; the LP solution C13 says "6 belongs there"). The diagram includes it so that every multiple of 3 up to 30 is shown. The inventory entry starts with "CORRECTED:". If you want the figure exactly as printed, delete 6 from the spec (row 1 of the left region would then be 3, 9, 12 and the solution's row 1 stays 3, 6, 9, 12).
2. **Tidy rows instead of the book's scattered numbers.** The numbers of Fig. 5.1 are placed in rows (the printed answer, SOL23, uses rows too). The question figure fills only the upper rows, so that the solution figure (game till 60) adds its green numbers below without moving any given number (v3 rule: the solution is the question figure plus the answer). Circle outlines use SET_A / SET_B instead of the book's green.
3. **C26 question (Draw a figure similar to Fig. 5.1 for 2 and 5, 3 and 7, 4 and 6): required.** The question names Fig. 5.1 and the LP text does not describe it, so the learner needs it; it is the same book picture as C12, so the spec is identical ("same as M1.S3.T3.C12.IMG1"). The other choice would be `none`; I did not take it because "similar to Fig. 5.1" is meaningless without the picture.
4. **C27 solution: three Venn diagrams on ONE 16:9 card (82 numbers).** The answer is three figures, but a pair gets one solution diagram and the validator rejects a second item. Layout: panel A (2 and 5, 36 numbers) on the left half, B (3 and 7, 26 numbers) top right, C (4 and 6, 20 numbers) bottom right, no panel letters. Text is 34 to 36 px; every number box was checked in code to lie inside its region with an 8 px margin. It is dense: if the render looks cramped, the clean fix is three parts (IMG2, IMG3), which needs a change of the one-diagram rule. `derived_from` names C26.IMG1 only because the validator demands it; the circle style, colours, labels and arrow are the same, the layout is not (three panels). No printed answer exists for this task in the book, so no base figure maps here.
5. **C21 solution (Q8): sample answer 3 and 8 from the LP**, not the book's 3 and 4. With 3 and 4 the overlap would also hold 12, 36, 60, but the question's overlap shows only 72, 48, 24. Left-only = 21 multiples of 3 up to 72, right-only = 6 multiples of 8 up to 72 (8, 16, 32, 40, 56, 64). The book's arrows from each circle to its blank label are replaced by a label directly above its circle.
6. **C20 question (Q8): required**, because the blank labels and the overlap numbers 72, 48, 24 are only in the picture and the task is to fill the empty regions.
7. **C30 question (shaded and circled table): required** although the LP question text repeats the shaded and circled numbers in brackets. The book gives the table as a picture and asks to look at it; shading and circles carry the meaning (HIGHLIGHT_MEANING). **C31 solution: none** (SAME_AS_QUESTION_DIAGRAM): 36, 48, 60 are already the cells that are both shaded and circled in the question figure, and the answers are words. A copy with FOCUS outlines on those three cells would be only nicer, so not optional.
8. **Worked examples C32 and C33 (jump sizes): none.** The numbers are listed in the steps. P03 (book's jump-arc number line, six jump sizes) is a teaching figure: mapped to concept image M1.S5.T5.C32.IMG1, which draws only the jump of 4 on it. If the content team wants the full six-jump line it is a teaching-image job, not part of this run.
9. **Worked examples C2 and C3: none.** P01 (chapter-opening ring of children with bubbles) is mapped `none:DECORATIVE_ONLY`; the plan's C2 teaching image is a hops number line, a different figure.
10. **Text only (none, TEXT_SUFFICIENT or LATEX_ARITHMETIC):** Figure it Out Q1 to Q3 (C6 to C11), Q5 to Q7 (C14 to C19), Q9, Q10 (C22 to C25), the other-number-with-4 pair (C28/C29) and the 15-and-30 pair (C35/C36). Their book answers are words or numbers, no figure is printed.
11. **diagram_type `other`** for the Venn diagrams (not in the section 7 catalogue); the table uses `cell_grid`. Figure letters (a, b, c) and the caption "Fig. 5.1" are not drawn.

## 2. Things in the LP that look wrong

- **Duplicated sub-questions.** C8 and C9 (Q2) list "(a) ... (b) ... (c) ..." twice (long wording, then short wording). C26 and C27 (the three pairs) and C30 and C31 (the table) do the same: the question text is followed by a second copy of the parts ("a) 2 and 5 up to 60 ...", "1) Is there anything common ..."). C12, C20, C26 and C30 also carry a bracketed description of the figure; once the diagram is in place these descriptions are redundant (the C30 one even lists the shaded and circled numbers, i.e. the data of the picture).
- **Broken LaTeX in C20** (`question_tex` and `text`): `$\underline{\hspace{1.2em}}’$` has the typographic closing quote inside the maths.
- **Book numbers.** The LP calls the second Figure it Out box Q5 to Q10, but the book restarts at Q1 on page 110 (the LP's Q5 is the book's Q1, Q6 is Q5, Q7 is Q6, Q8 is Q8, Q9 is Q9, Q10 is Q10; the book's Q2, Q3, Q4, Q7 are not in this chunk). The `ncert_refs` are right (5.1.FiO2.Qn), only `book_number` differs.
- **C27 answer text** says "Venn figures as in the parts"; there are no parts in the LP, so the text relies on the new picture. It should say the figures are above.
- **C13 answer text** says the printed Fig. 5.1 leaves out 6, which is right; with the new question diagram (6 added) the sentence still reads correctly because it speaks of the printed book.
- **C29** adds the pair 2 and 4 that the book does not name (the book says only 8). The LP is right: every multiple of 4 is a multiple of 2, so nobody says "vada" alone.
- **C19** adds the pair 7 and 9 (first idli-vada at 63); the book names 7, 8 and 8, 9 only. Checked: the three pairs below 10 whose first common multiple exceeds 50 are exactly (7, 8), (7, 9), (8, 9).
- All arithmetic of the 18 units was rechecked and holds (150; 30, 18, 6; 300, 180, 60; 320, 360, 400; 360; 2520; 10, 21, 12; 1, 3, 5, 15).

## 3. Where the book itself is unclear

- Fig. 5.1 (chapter p.2) omits 6 from the left circle.
- The printed answer to Q4 uses singular labels "Multiple of 3 / Multiple of 5" and its left-only list is the 16 numbers 3 to 57; it matches the LP.
- The printed answer to Q8 (solutions p.25): the Venn picture is not in the pdf (only the labels "Multiples of 3" and "Multiples of 4" and "Think of some more."), and the pair 3 and 4 is inconsistent with the question's overlap (see 1.5).
- The task "Draw a figure similar to Fig. 5.1 ... 2 and 5, 3 and 7, 4 and 6" has no printed answer in the solutions pdf; the figures are derived from the question (multiples up to 60, left = smaller number, as the task says).
- The jump-arc number line on p.3 prints no colour key; the plan's teaching image is the only guide to which colour is which jump.

### Chunk B notes (from the decision agent)
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

### Chunk C notes (from the decision agent)
# Chunk C notes: Class 6 Ch 5 "Prime Time" (topics M2.S12.T12, M2.S14.T14, M2.S15.T15)

Result: 14 units, 28 items. Required 2 (question side of FiO 5.2 LP Q1 and Q2), optional 2 (their solutions), none 24. Validator: errors 0, warnings 0.
Output: `map/out_C.json` (written by a script kept outside HERE).

## 1. Judgement calls

1. **FiO 5.2 LP Q1 (C60) and LP Q2 (C62): question diagram required (the finished Sieve table).**
   Q1 says "Look at the list of primes till 100", Q2 says "the table on the previous page". The list is only the book's p.113 table, so the learner cannot attempt either question without it (FIG_REFERENCED, DATA_IN_FIGURE, HIGHLIGHT_MEANING).
   - This is NOT the "refer picture" case of Step B2. The printed answer is plain text, and the plan has no concept image of the full table (`M2.S11.T11.C57.IMG1` shows only 1 to 10 in a row). So the question is required, not optional.
   - Each item gets its own diagram with the identical spec (C62 says "same as M2.S12.T12.C60.IMG1" in `render_note`).
   - The figure is exactly what the book prints: 10 x 10 cells, 25 primes circled (FOCUS), the other 75 cells (1 and the 74 composites) crossed with a full X (GUIDE, behind the INK number). It states no row counts and no differences. I checked the book table by pixel count: every prime cell has green and no red, every non-prime cell has red strokes.
   - Aspect ratio 16:9 although the grid is square: the pipeline draws 16:9 cards. The spec fixes the grid at about 940 px high on a 1920 x 1080 canvas, so each cell is about 94 px and the digits stay at least 34 px high. The book has no row labels (even though the question says "decades"), and none are drawn, as the companion note requires.

2. **Solutions of C60 / C62: `optional`, not `none`, not `required`.**
   The LP text already gives everything (the two pairs and differences; the ten row counts and the least / most decades), and the printed answers are text. A marked copy of the same table (pairs 2, 3 and 89, 97 for Q1; a count beside each row for Q2) would help, which is the tie-breaker's "nicer" band. So optional, and nothing is added.
   Sibling consistency: both are answers read off the same table, so both get the same decision.

3. **Other FiO 5.2 items (C64 to C76) all `none`.**
   - C64 (pairs with sum a multiple of 5), C66 (13/31 type pairs), C68 (seven consecutive composites), C70 (twin primes), C72 (product of three distinct primes), C74 (digits 2, 4, 5), C76 (doubling and adding 1): word or arithmetic questions with no figure in the book; the answers are lists or equations (TEXT_SUFFICIENT or LATEX_ARITHMETIC).
   - C69 solution (89 and 97 are primes, 90 to 96 are between them): a strip 89 to 97 would be a nicety only. No question figure exists to derive from, so I did not make it optional.

4. **Co-prime practice (C82 to C89) and Example 1 (C90, C91): all `none`.**
   - The book prints no figure with any of them, and no printed answer is a picture. The plan's concept images (4 and 9, 15 and 39, number line of 3 and 5) are teaching figures and are not linked (v3 rule).
   - C82 (where to put the treasures) and C88 (Math Talk on the first common multiple) are open-ended; reason codes include OPEN_ENDED.

5. **Figure inventory claims (6 entries).**
   - `P07-number_grid-1` goes to item C60 (question) and `NEW-P07-number_grid-1-b` to item C62 (question): a figure used by two items is two entries.
   - Merge note: chunk B (Sieve topic T11) may also claim `P07-number_grid-1`, as a teaching figure. If B gives it a different meaning (for example a concept image or none), keep one entry for the base id and rename mine to `NEW-` ids. My two items stay required either way, because they need their own figure.
   - `P10-thread_art-1` to `-4` (Math Talk "Co-prime art", p.10): no question, solution or worked-example item of the plan carries them. The plan covers this Math Talk with the tool "Thread Art Co-prime Check" (`M2.S13.T13.C81.2D1`). Topic T13 has no units, and its book section 5.3 has units only in my chunk, so I claimed them here as `none:OPEN_ENDED`. If another chunk claims them too, the meaning is the same.
   - I checked the four base descriptions against the page 10 picture (12 pegs gap 4 triangle; 13 pegs gap 3 ring; 16 pegs 8-point star on the even pegs; 24 pegs square on 24, 6, 12, 18): correct, no "CORRECTED:" needed.

## 2. Things in the LP that look wrong or thin

- **Book numbers:** T12 labels its questions "Figure it Out 5.2, Q1 to Q9". The book numbers are Q2, Q3, Q5, Q6, Q7, Q8, Q10, Q11, Q12 (book Q1, Q4, Q9 are in topic T10). Also the `ncert_refs` ("5.2.FiO.Q2" and so on) follow the book, so LP Q1 and the ref Q2 differ.
- **C62 text:** "in the table on the previous page" is a page reference from the book. In the LP the table will be the diagram right under the question, so it should read "in the table above" (not changed by me; the item is not marked for text sync).
- **C84 / C85 / C86 / C87 text:** the parts are listed twice. `question_tex` has "(a): 15 and 39, (b): 4 and 15, ...; (a): 15 and 39; (b): 4 and 15; ..." and the plain `question` has "a. 15 and 39, b. ... a) 15 and 39 b) ...". The same duplication is in the question line of the solution concepts. A reader sees every pair twice.
- **LaTeX misuse of the word co-prime:** `$co$-prime` in C86, C87, C88, C90, C91 (the word "co" set as math italics). In C90 it is worse: `$39 co$-prime` puts "co" inside the math with the number 39. In C87 `answer_tex` is "a, $b$ and $d$ are $co$-prime", which mixes plain "a" with math "b" and "d".
- **Broken LaTeX around pairs:** `answer_tex` of C65 is `$(2$, $3)$, $(3$, $7)$, $(2$, $13)$` and of C89 `$(3$, $5)$ ...`: the brackets are split across the math segments.
- **C61 / C67 / C71 / C77:** `steps_tex` repeats `answer_tex` word for word (one line only), so the "steps" add nothing.
- **C73 (three distinct primes):** the steps list the factorisations of 45, 60, 91 and 330 without saying why each is rejected, and never factorise 105 (only the answer line does). 60 = 2 x 2 x 3 x 5 has three different prime factors, so a learner may think it qualifies; the missing line is "2 is repeated, so 60 is not a product of exactly three distinct primes". Not a diagram matter.
- **C83 (where to place the treasures):** the book prints no answer for this prompt (its printed answer on p.28 is for "Check if these pairs are safe"). The LP's "e.g. 4 and 9" comes from the paragraph on p.115. Fine, but it is the LP's own answer.

## 3. Where the book itself is unclear

- The p.113 table prints some crosses as a single diagonal stroke (30, 49, 91, 94). That is a print artefact: every non-prime cell does carry red strokes. The spec draws a full X on every crossed cell.
- The question speaks of "decades" and "rows" but the book table has no row labels.
- Co-prime art (p.10): the peg count and gap of diagrams 3 and 4 are not printed (read from the picture as 16 pegs gap 6 and 24 pegs gap 6), and the exact chords of diagram 2 cannot all be traced. None of this affects an item of this chunk.

### Chunk D notes (from the decision agent)
# Chunk D notes (Class 6 Ch 5 "Prime Time", topics T16 to T20, units 45-64)

Result: 31 items = 9 worked + 11 question + 11 solution. Required 2 (both worked examples), optional 0, none 29. Validator `--chunk D`: errors 0, warnings 0.

Figures in this part of the book: only two. I checked every page picture used (pdf pages 11-16 and the printed answers on pdf pages 29-30). Pages 11, 14, 15, 16 and the answer pages hold text only; the page 11 characters are not in the picture. The two base figures are right (counts and texts checked against the pictures), so nothing is marked "CORRECTED" and nothing is `NEW-`.

## 1. Judgement calls

1. **M3.S16.T16.C95 (36 broken four ways): required, factor tree (P12-factor_tree-1).** This is the closest call. The text alone is enough to compute 2 x 2 x 3 x 3 = 36, so a "text only" reading is possible (tie-breaker). I chose required because the question says "in all four cases" and "multiply back ... in all four cases", while the LP text names only the four first splits (2x18, 3x12, 4x9, 6x6). The four finished chains (3x3x2x2, 2x3x2x3 and so on) exist only in the book's tree. If the user wants fewer images, this is the one to drop (then `none` with TEXT_SUFFICIENT and the text must list the four chains). The figure is the whole printed tree, question side (worked example), nothing solved. No teaching image shows it.
2. **M3.S16.T16.C96 (cuboid, "Using this diagram"): required, solid_3d (P13-solid-1).** Clear case: the question points at the figure. The book colours the faces red, yellow and green; the colours carry no meaning, so I used tokens: front CELL_FILL, top MARK_FILL, right SET_B at 30 percent opacity (the renderer must support the opacity; if not, use a light amber tint). No labels are drawn (the book prints none); 3, 2 and 5 are said in the LP solution steps. 16:9 card with the cuboid centred; coordinates are given for a 1920 x 1080 canvas.
3. **Teaching images kept, nothing linked:** C94.IMG1 (same primes), C97.IMG1 (join the prime factors), C113.IMG1 (80 and 63 dots), C114.IMG1 (48 includes 12). The matching worked examples are `none` (the book has no picture for them; the text and LaTeX carry everything). Not coded REUSES_CONCEPT_IMAGE because that code is for the 'refer picture' case only.
4. **Figure it Out 5.4 Q1-Q5 (T18), all ten items `none`.** Questions are words or lists of numbers; printed answers (page 29-30) are product lines in text, not pictures. Sibling consistency: all five pairs get the same decision. A factor tree for Q4 (a, b, c) or Q1 would be a nice extra but is not needed (optional at most; not added).
5. **Example 2-6 pairs (T20, 10 items) `none`.** Both prime factorisations are given in the question; the answers are comparisons of prime lists in words. An "included / not included" picture (for 42 and 12, 75 and 21) would help a little but the text states it exactly (optional at most; not added).
6. **T17 Anshu dialogue (C101/C102) `none`.** A dialogue question with the factorisations in the text.

## 2. Things in the LP that look wrong

- **C101 question_tex / text (and C102, C116-C125 text):** the LaTeX is broken around "co-prime": `Are $56$ and $63 co$-prime?` puts "co" inside the maths of 63, and `$co$-prime` elsewhere sets "co" in maths italics. Plain text "co-prime" outside the dollar signs would be right.
- **C109 (Figure it Out Q4) and C111 (Q5):** question, question_tex and text list the parts twice (`(a): 56 x 25; (b): 108 x 75; (c): 1000 x 81; (a): ...; (b): ...; (c): ...`, and for Q5 `(a) three different prime numbers? (b) four different prime numbers? (a) three ... (b) four ...`). The same duplicate sits in the answer concepts' `question`. It looks like a scrape that took the part list from two places. The parts should appear once.
- **C104 (Q1 answer):** `answer_tex` writes 729 as `(six $3s$)` and 1024 as `$1024 =$ ten $2s$ multiplied` while `steps_tex` writes both products out in full. The numbers are right (729 = 3^6, 1024 = 2^10) but the style is not consistent; `$3s$` and `$2s$` put the plural s inside maths. Same `$3s$` in C105 question_tex ("two $3s$").
- **C96, C99, C113, C114:** `steps` and `answer` hold the same paragraph (steps has a single entry equal to the answer), so the solution text is shown twice for these worked examples.
- **C96 text** (cuboid): the question depends on the figure ("Using this diagram"), so the token placed after the question text is essential; without it the question has no figure.
- All arithmetic in the LP was recomputed and is correct: 80, 63, 36 = 2x2x3x3, 72 = 2x2x2x3x3 (8 x 9), 64 = 2^6, 104 = 2^3 x 13, 105, 243 = 3^5, 320 = 2^6 x 5, 141 = 3 x 47, 1728 = 2^6 x 3^3, 729 = 3^6, 1024 = 2^10, 1331 = 11^3, 1000, 198, 1955 = 5 x 17 x 23, 56x25, 108x75, 1000x81, 30, 210, 168 = 12 x 14, 75 vs 21 (7), 42 vs 12 (2 twice vs once).
- Outside my chunk (for the merger): printed answer page 30, Q.1 (second Figure it Out set) labels the fourth part "c. Yes" instead of "d. Yes"; and printed answer Q.2 a-d are fractions. That set is T21 (chunk E).

## 3. Places where the book itself is unclear

- The book's tree on p.118 has two identical last boxes in column 4 (2x3x2x3 twice, the last box adds nothing). I kept both, as printed, and said so in `render_note`.
- The cuboid has no printed dimensions; the numbers 3, 2, 5 come from counting the squares on the three faces (checked on an enlarged crop: front 3x2, top 3x5, right 5x2) and from the LP solution text, which agrees.

### Chunk E notes (from the decision agent)
# Notes, chunk E (M3.S21.T21, M4.S22.T22 to M4.S26.T26)

Result: required 0 / optional 0 / none 29 (12 question, 12 solution, 5 worked example). Validator: errors 0, warnings 0.

I looked at the page pictures of pdf pages 16 to 20 (book pp. 122 to 126) and solutions pages 30, 31 and 33. They hold no figure that belongs to this chunk: only text, Math Talk icons and the remainders table. The 2 x 2 "special numbers" box on page 20 is section 5.6 (not this chunk).

## 1. Judgement calls

1. **Remainders table (M4.S24.T24.C148, the printed answer of book Figure it Out 5.5 Q4; base figure SOL33-table-1).**
   The printed answer is a plain black-and-white 4 x 8 table with no shading or highlight. I chose `none` with `LATEX_TABLE`, not a required picture. Reasons:
   - the v3 Step C rule names a plain table of numbers as LaTeX;
   - the LP steps already hold all 21 remainders (I recomputed them: they match the printed table);
   - the question side has no figure.
   Against this, Step B2 lists "filled table" under `ANSWER_IS_FIGURE`. If the user wants the book's table drawn as a picture, flip C148 to `required` (question has none, so `derived_from` null, token `steps_tex` / `before_first_step`). A LaTeX array is given in `text_alternative`.
2. **Worked examples C134, C135, C136, C137 (T22) and C149 (T25): `no_image`.** The book prints no figure for any of them and the steps are complete in words or sequences. The teaching images C134.IMG1, C136.IMG1, C137.IMG1 and C149.IMG1 stay as they are and are not linked. Pictures I considered and rejected as "only nicer": a tick-grid for 2 to 10 beside 8560, a number line showing 125 between 120 and 130.
3. **T26 Q1 ("list the multiples of 4 from 1 to 200").** A 1 to 200 grid with multiples shaded would help pattern-spotting, but the book prints none, the question gives no figure and the LP answer only needs six numbers. Left as text.
4. **Sibling consistency.** All five "Figure it Out" and Math Talk style answer sets in this chunk (5.4 Q1 to Q4, 5.5 Q3 and Q4, T23, T26) are word or arithmetic answers, so all take the same decision (`none`).
5. **No new figures.** I added no `NEW-` figure; nothing else on these pages carries mathematical content.

## 2. Things in the LP that look wrong or thin

- **Duplicated sub-parts in the question text.** `question_tex` and `text` of M3.S21.T21.C126, C128 and M4.S24.T24.C145, C147 list the parts (a) to (d) / (a), (b) / (a) to (c) twice (the prose version, then the "a)" version). Same in M4.S26.T26.C157 (the three statements, then a second, truncated copy: "If last two digits divisible by 4 then number is", "...then last two digits are"). Worth cleaning in the text, nothing for a diagram.
- **LP numbering vs the book.** T24 is titled "Figure it Out 5.5" with `book_number` "Q1" and "Q2", but they are the book's Q3 (sum of evens / odds, `ncert_refs` 5.5.FiO.Q3) and Q4 (remainders, 5.5.FiO.Q4). Book Q1, Q2, Q5, Q6, Q7 of that set are in other topics (chunk F).
- **Descriptive `book_number` on T23 and T26 questions** ("Divisibility by 10: numbers that end in 0", "Divisibility by 4: multiples near 330, 1730 and 2030", and so on): these are not book numbers; they are Math Talk / margin questions of 5.5 (pp. 123 to 124).
- **M4.S26.T26.C154 `answer_tex` is cut off:** "A number is a multiple of 4 when the number formed by its last two digits is." The same ending is in `answer`. It should end "...is a multiple of 4" (the printed book answer has no list or rule at all for this question).
- **M4.S26.T26.C153 asks for the list of multiples of 4 from 1 to 200** but the LP answer gives only the three ranges (332 and 336; 1732 and 1736; 2032 and 2036). The book's answer page does not give the 1 to 200 list either. Not a diagram matter.
- **M3.S21.T21.C133 (Guna, "any two primes co-prime?").** The LP is more careful than the book: it adds that a prime with itself (3 and 3) is not co-prime. The book's printed answer is only "Yes, for example 2, 3; 3, 11". The LP wins, as the brief says.
- **Arithmetic checked (all agree with the LP):** every factorisation in 5.4 Q1, Q2 (225 = 3x3x5x5, 27 = 3x3x3, 96 = 2^5 x 3, 24 = 2^3 x 3, 999 = 3x3x3x37, 99 = 3x3x11, 343 = 7^3, 216 = 2^3 x 3^3, 57 = 3x19, 85 = 5x17, 121 = 11^2, 1331 = 11^3); 8560 divisible by 2, 4, 5, 8, 10 and not by 3, 6, 7, 9; 395 as the largest multiple of 5 below 399; multiples of 2 from 400 to 410 (six numbers); 8536 / 4 = 2134; 124, 364, 4028 all multiples of 4; the 21 remainders of the table.

## 3. Places where the book itself is unclear

- Solutions p.30, Figure it Out 5.4 Q1: the printed labels read a, b, c, **c** (the last one, 343 and 216 "Yes", should be d). The LP uses (d).
- Solutions p.30, Q2: the printed answers are a Yes/No followed by a fraction (first number's factorisation over the second's) with no sentence saying "divisible"; the LP spells this out in steps.
- Solutions p.31, Q4: the printed answer "Yes, for example 2, 3; 3, 11 (Try other examples)" is silent on the same-prime case (see above).
- Solutions p.33, Q4: the table header says "Numbers" and "a) / b) / c) Remainder when divided by ..."; the question statement itself says "(a) 10, (b) 5, (c) 2" on p.126 and "i) 10, ii) 5, iii) 2" in the solutions: same content, two labelling styles.

### Chunk F notes (from the decision agent)
# Chunk F notes (Class 6 Ch 5 "Prime Time", live plan cbse_eng_maths6_ch5_v75)

Units: M4.S27.T27 to M4.S33.T33 (15 units, 27 items). Result: required 9 / optional 0 / none 18. Validator: errors 0, 4 warnings
(the four prime-puzzle solution diagrams have no printed book figure: the book prints no answers for 5.6, so the warning is expected).

Decisions in short
- Only the prime-puzzle material is drawn: the T32 worked example (1 diagram) and the four T33 puzzles (4 question + 4 solution diagrams).
- FiO 5.5 Q1, Q2, Q5, Q6, Q7 and the Divisibility by 8 items (q19 to q22) are text/LaTeX on both sides: the book prints no figure for any of them
  and every printed answer is text.
- T31 Special numbers (5.6.q1): none.
- All 15 puzzle diagrams use the house tokens (grid cells BG with INK outline, six clue cells MARK_FILL, filled primes in ANSWER green), 16:9.

## 1. Judgement calls

1. M4.S31.T31.C179 worked example (5.6.q1, the box 9, 16, 25, 43): none (NUMBER_LIST_IN_BOXES + OPEN_ENDED). The LP question text already lists the four
   numbers, position in the box means nothing, and the task is open-ended. The same box is the kept teaching image C179.IMG1 (never linked), so base figure
   P20-cell_grid-1 is accounted as `concept_image:M4.S31.T31.C179.IMG1`. A reviewer who wants the box drawn would have to call it `optional`, not required.
2. M4.S32.T32.C181 worked example (5.6.q3, "the figure on the left shows the puzzle ... on the right the solution"): required. The LP text names none of the numbers,
   so the learner cannot attempt "what can the rules be?" without the pictures. One worked item takes one diagram, so the left (empty) and right (solved) book
   figures are drawn side by side in ONE 16:9 image; both book figures map to this item (two inventory entries, P21-product_puzzle-5 and -6). The right figure is
   in INK (it is given in the book), not ANSWER green. media_id is `M4.S32.T32.C181.IMG2` because C181.IMG1 is a kept teaching image. That kept image is a
   different 2 by 2 puzzle (6, 10 / 10, 6), not the book's 3 by 3 figure, so it does not stand in for the book figure.
3. M4.S33.T33 puzzles 1 to 4: question and solution required for all four (sibling consistency). The LP text gives every clue number, so a very strict reading
   could say "text is enough", but the task is to FILL a given grid whose layout (row clue to the right of each row, column clue below each column, no corner cell)
   defines the puzzle, and the answer is the completed grid (ANSWER_IS_FIGURE). Solution diagrams are derived_from the question diagrams. Puzzle 2 (8, 105, 70 / 30, 70, 28)
   is also the kept teaching image C182.IMG1; it still gets its own question and solution diagrams (v3: a teaching image is never linked).
4. Four Math Talk boxes on pdf page 21 (5.6.q2: 5, 7, 12, 35 / 3, 8, 11, 24 / 27, 3, 123, 31 / 17, 27, 44, 65): the LP has no unit for them (see 2.5). The four
   base figures P21-cell_grid-1 to -4 are accounted as `none:NUMBER_LIST_IN_BOXES` (open-ended, positions carry no meaning).
5. FiO 5.5 Q3 and Q4 (and the printed answer table SOL33-table-1, remainders for 78 ... 2345) sit in chunk E (M4.S24.T24); SOL33-table-1 is the printed answer of Q4, so
   it is not claimed here. If both chunks claim it, the plain table should mean `none:LATEX_TABLE`.
6. FiO 5.5 Q5 (14560): the LP answer is "5 and 8" (the book's). 8 and 10 would also be a correct pair (8 covers 2, 4, 8; 10 covers 2, 5, 10), so "what could those two numbers be" has more
   than one answer. Not a diagram matter; left as is.

## 2. Things in the LP that look wrong or odd

1. M4.S27.T27.C159 (Q1): the question text repeats both parts: "(a) ... (b) ... (a) ... (b) ..." (question and question_tex). Part (a) is repeated word for word.
2. M4.S29.T29.C171 (Q3 statements): question text repeats the three statements in a short form after the long form ("1) Only the last three digits matter 2) If last three digits divisible by 8 then number is 3) ...").
3. M4.S27.T27.C162 (FiO Q2): the LP answer 8888 and 2112 is right (8888 / 4 = 2222, 2112 / 4 = 528; palindromes abba need 10b + a divisible by 4 with a even). The book's printed answers 9999 and 1001 are
   odd numbers, so the LP is right and the book is wrong (the LP already says so).
4. Book numbers are not the LP numbers: T30's three questions are labelled "Figure it Out 5.5, Q1, Q2, Q3" (book_number) but ncert_refs say 5.5.FiO.Q5, Q6, Q7 and the book numbers are 5, 6, 7 (pdf page 20).
   T27 is labelled Q1 and Q2 and matches the book. The T29 items (q20 to q22) are unnumbered bullet questions in the book, labelled by topic in the LP.
5. Content missing from the LP: the Math Talk of four boxes (5.6.q2, pdf page 21, text: "Below are some boxes with four numbers in each box. Within each box try to say how each number is special compared to the rest ...") is not
   in any unit (T31 stops at C180 "Practice: Special reasons", a recap).
6. M4.S32.T32.C181 (worked example): the question text refers to "the figure on the left" and "the figure on the right" but states none of their numbers; the steps say "Rule (given next in the book)". The diagram fixes the missing data;
   no text sync is needed, but the later FiO text should not repeat the figure's numbers differently.
7. M4.S28.T28.C165 teaching plan says "8560 itself works" (560 = 8 x 70), while the book answer and C170 give 8552. Both are multiples of 8 (8552 = 8 x 1069); 8552 is the one that actually changes the last two digits. Not a diagram issue.

## 3. Where the book itself is unclear

1. The base inventory descriptions of all figures of this chunk (P20-cell_grid-1, P21-cell_grid-1 to -4, P21-product_puzzle-5 to -8, P22-product_puzzle-1 and -2) were checked against the page pictures (pdf pages 20, 21, 22) and are correct.
2. The book prints no solution for any 5.6 puzzle (the solutions section ends at 5.5), so the four completed grids come from the LP. Each was recomputed: all row and column products match the clues, all entries are prime, and each puzzle has a unique solution.
   Checked products: puzzle 1 rows 105, 20, 30 / cols 28, 125, 18 (grid 7 5 3 / 2 5 2 / 2 5 3); puzzle 2 rows 8, 105, 70 / cols 30, 70, 28 (2 2 2 / 3 5 7 / 5 7 2); puzzle 3 rows 63, 27, 190 / cols 45, 42, 171 (3 7 3 / 3 3 3 / 5 2 19); puzzle 4 rows 343, 66, 44 / cols 28, 154, 231 (7 7 7 / 2 11 3 / 2 2 11).
3. The book colours the nine grid cells pale mint and the clue cells orange-yellow; the diagrams swap them for the house tokens (grid cells white, clue cells MARK_FILL), as the style table requires.
