# Class 7 Ch 6 Number Play - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths7_ch6` v62 (taken from staging). Result: new V2 version v63 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (94 items from 49 units)
{"question": {"required": 8, "none": 36, "optional": 1}, "solution": {"required": 19, "none": 24, "optional": 2}, "worked_example": {"required": 1, "none": 3}}

Optional, NOT added: [('C27', 'solution'), ('C29', 'solution'), ('C35', 'question')]

needs_lp_text_sync: [('C75', 'solution'), ('C79', 'solution'), ('C87', 'question')]

## The 28 diagrams
| id | side | type |
|---|---|---|
| M1.S3.T3.C6.IMG1 | question | people_lineup |
| M1.S3.T3.C7.IMG1 | solution | people_lineup |
| M1.S4.T4.C9.IMG1 | solution | people_lineup |
| M1.S4.T4.C11.IMG1 | solution | people_lineup |
| M1.S4.T4.C13.IMG1 | solution | people_lineup |
| M1.S4.T4.C15.IMG1 | solution | people_lineup |
| M1.S4.T4.C17.IMG1 | solution | people_lineup |
| M1.S4.T4.C19.IMG1 | solution | people_lineup |
| M3.S10.T10.C62.IMG1 | worked example | cell_grid |
| M3.S11.T11.C65.IMG1 | question | cell_grid |
| M3.S11.T11.C66.IMG1 | solution | cell_grid |
| M3.S11.T11.C67.IMG1 | question | cell_grid |
| M3.S11.T11.C68.IMG1 | solution | cell_grid |
| M3.S13.T13.C73.IMG1 | question | cell_grid |
| M3.S13.T13.C74.IMG1 | solution | cell_grid |
| M3.S14.T14.C75.IMG1 | solution | cell_grid |
| M3.S14.T14.C77.IMG1 | solution | cell_grid |
| M3.S14.T14.C79.IMG1 | solution | cell_grid |
| M3.S16.T16.C83.IMG1 | question | cell_grid |
| M3.S16.T16.C84.IMG1 | solution | cell_grid |
| M3.S16.T16.C85.IMG1 | question | cell_grid |
| M3.S16.T16.C87.IMG1 | question | cell_grid |
| M3.S16.T16.C88.IMG1 | solution | cell_grid |
| M3.S16.T16.C90.IMG1 | solution | cell_grid |
| M3.S16.T16.C92.IMG1 | solution | cell_grid |
| M3.S17.T17.C94.IMG1 | solution | cell_grid |
| M3.S19.T19.C98.IMG1 | question | cell_grid |
| M3.S19.T19.C99.IMG1 | solution | cell_grid |

### Chunk A notes (from the decision agent)
# Notes, chunk A (M1.S3.T3 and M1.S4.T4) - Class 7 Ch 6 "Number Play"

Result: 26 items = 13 questions + 13 solutions. Required 8 (1 question, 7 solutions), optional 2 (solutions), none 16. Validator: errors 0, 5 warnings
(the five Figure it Out Q1 (b)-(f) solutions are required but the book prints no picture for them, which is the expected case).

## 1. Judgement calls

1. **M1.S3.T3.C6 (question) = required, although the LP text already gives the heights (1, 5, 3, 6, 2, 7, 4).**
   Why: the book question is "the arrangement shown below" (a picture with empty bubbles) and the LP text says "the line in the figure", so the
   figure is the premise of the question; the 'refer picture' exception does not apply (the book's answer is a filled picture plus a list, not
   "refer picture"). The same picture is also the teaching image M1.S2.T2.C2.IMG2, which is never linked, so the item draws its own.
   A strict reading of the tie-breaker ("could the text alone do it?") would give `none`; I judged the dangling "in the figure" and the picture-first
   book question to outweigh that. If the team wants zero figures here, set it `none` and reword the text (drop "in the figure").
2. **M1.S3.T3.C7 (solution) = required** (printed answer is the same picture with the bubbles filled in: base figure P20), `derived_from` = the
   question diagram. Only the seven bubble digits (0, 0, 1, 0, 3, 0, 3) are new, in ANSWER green.
3. **Figure it Out Q1 (a)-(f), solutions = required, questions = none.** Only (a) has a printed answer picture (p.21); (b)-(f) get the same kind of
   figure by the sibling rule (answer IS an arrangement, B2). No question diagram: the book gives no figure with these questions (the stick-figure
   cut-outs are "at the end of the book", outside the 32 pages), so none is invented (companion note). Each solution figure therefore stands alone
   (`derived_from` null) and draws the whole line-up.
4. **What the figures show.** One scheme for all eight: seven plain stroke-figure children (no faces, single colour, simple glyphs), heights
   64 % to 100 % of the tallest in even 6 % steps (taken from the measured heights of the printed answer on p.21: 64, 70, 76, 82, 88, 94, 100 %),
   a speech bubble above each head, the height rank under each child with the one-word tag "height".
   - I ADDED the rank numerals + "height" so that the figure matches the LP text ("height 5", "Heights 7, 3, 5, 4, 1, 6, 2") and cannot be read as
     child numbers. The book picture itself has no rank numerals; in the unit-1 question they only repeat what the question text states.
   - Colours: unit 1 children and ranks in INK (given), bubble digits in ANSWER (new). Figure it Out Q1: children and rank numerals in ANSWER (the
     answer), bubble digits in INK (the sequence the question gives).
   - Left out on purpose: the book's colours, faces, the 11 ruled lines, the cut-out letters F C B G A D E (not in the LP), and the "Front" arrow
     of the teaching images (the front of the line is the left; the LP steps say "in front"). If the team wants the Front arrow, add one arrow
     labelled Front under the row in all eight specs.
5. **Q1(a) solution figure has bubbles, the book's printed picture has none.** The LP s_figure hint also says "with the speech bubbles above them reading
   0, 1, 1, 2, 4, 1, 5". The bubbles let the learner check each child, and they equal the given sequence (recomputed in code for all six parts).
6. **Figure it Out Q2 (a)-(f): all questions none; solutions (a), (b), (c), (f) none; (d) and (e) optional (not added).** The answers are verdicts
   ("Always / Only sometimes true") or a number, reached by word reasoning; no printed answer picture. (d) and (e) are the only ones whose steps
   give concrete counter-lines (heights 1, 2, 3, 4, 5 and 5, 4, 3, 2, 1; heights 7 .. 1 and 1, 7, 6), so a line-up would clearly help but is not needed
   (the verdict is not an arrangement, so ANSWER_IS_FIGURE does not apply). (a) is the same kind of answer but its counter-case ("the first child
   says 0 whatever the height") has no concrete line, hence `none`; this is the stated reason for the difference between (a) and (d)/(e).
7. **Inventory.** P01-arrangement-1 and P01-arrangement-2 (teaching line-ups opening 6.1) are claimed as `concept_image:M1.S2.T2.C2.IMG1` (both are
   its two panels). P02-arrangement-1 -> question item C6, P20 -> solution item C7, P21 -> solution item C9. No NEW- figure was needed. I checked all
   five against the page pictures (pages 1, 2, 20, 21): colours, order of heights, bubble numbers and the letters F C B G A D E are as the base describes.

## 2. Things in the LP that look wrong or thin

1. **Figure it Out Q1 (a)-(f) question text is only a bare sequence** ("(a): 0, 1, 1, 2, 4, 1, 5"). It never says what to do. The book says "Arrange
   the stick figure cutouts ... or draw a height arrangement such that the sequence reads". The text needs that sentence, at least on (a).
2. **Figure it Out Q2 (a)-(f) question text lacks the task** "Always True, Only Sometimes True, or Never True. Share your reasoning." The answers
   ("Only sometimes true") only make sense with it. Q2(f) is a question, so it is fine.
3. **Wrong wording in M1.S4.T4.C19 (Q1(f)) step 2:** "Each of the last four is shorter than the first three but taller than the others behind them."
   For heights 5, 6, 7, 1, 2, 3, 4 each of the last four is taller than the last-four children standing IN FRONT of it (not behind: those are taller).
   It should read "taller than the children of the last four who stand in front of it" or similar. The answer (heights 5, 6, 7, 1, 2, 3, 4) is correct.
4. **LP numbering differs from the book:** LP "Figure it Out, Q1 to Q6" are book Q1(a)-(f); LP "Q7 to Q12" are book Q2(a)-(f).
5. M1.S4.T4.C26 (Q2(d)) text is shortened ("cannot say 0") from the book's "if ... then they cannot say '0'"; harmless.
6. The old answer cards of C7 and C9 are two each (IMG1, IMG2); the new plan has one diagram per answer concept (IMG1), as the brief says the old cards
   are replaced.
7. Everything else recomputed with the rule "number of children in front (to the left) who are taller": the LP answers of unit 1 and Figure it Out
   Q1 (a)-(f), and the Q2 counter-lines, all agree with the figures I specified; no other contradiction with the book (p.20, p.21) found.

## 3. Where the book itself is unclear

1. Q1(a)'s printed answer (p.21) is a picture of cut-outs labelled F, C, B, G, A, D, E taken "from the cutouts at the back of the book"; those
   cut-outs are not in this 32-page pdf, so the letters cannot be tied to anything else. The picture has no bubbles or numbers.
2. "Try for other subparts": no picture is printed for (b)-(f).
3. The book's p.2 picture (question) is drawn with ranks 1, 5, 3, 6, 2, 7, 4, but its exact head heights were not measured separately; the specs use
   the even 6 % steps measured on p.21 (the order of heights is certain, the exact percentages are approximate, about plus or minus 3 %).
4. The book rule says "children in front"; the picture treats the left side as the front (the printed answer on p.20 reads "From left -> 0, 0, 1, 0, 3, 0, 3").

### Chunk B notes (from the decision agent)
# Notes, chunk B (Class 7 Ch 6 "Number Play", plan cbse_eng_maths7_ch6_v62)

Result: 29 items (14 question, 14 solution, 1 worked example). required 7, optional 1, none 21. Validator: errors 0, warnings 0.
Required diagrams: worked example M3.S10.T10.C62; M3.S11.T11.C65 (q) / C66 (s); C67 (q) / C68 (s); M3.S13.T13.C73 (q) / C74 (s). All are number grids (3 x 3 with circled row and column sums, a 2 x 3 parity grid, a 3 x 3 magic square). Everything else is text or LaTeX.

## 1. Judgement calls

1. **Grid-filling questions are `required` on the question side (C65, C67, C73) and on the solution side (C66, C68, C74).** The LP text of each lists every value, so a strong student could solve from the words alone. I followed the v3 prompt's own precedent (the supercell row, Step B and Step E: "act on a figure: complete" gives Q required, S required, S derived_from Q). The book gives a picture (circled sums, given cells) and the answer is a filled grid (ANSWER_IS_FIGURE), so sibling consistency makes all three pairs the same. If the team wants a leaner plan, the question sides are the ones to drop; the solution sides rest on the printed answer pictures.
2. **Worked example T10.C62** gets ONE diagram: the GIVEN puzzle (4 middle-left, 3 bottom-right, sums 24/15/6 and 12/16/17), placed after the question text. It is not the solved grid, because the example has two valid fillings (both in the LP steps) and a question-position figure must not leak the answer. The book's printed answer to that grid (7 8 9 / 4 6 5 / 1 2 3, figure P24-sum_grid-4) is therefore mapped `none:TEXT_SUFFICIENT` (one diagram slot only).
3. **Kishor question (T6.C35) is `optional`, not `none` and not `required`.** The LP question states "five odd cards" and the answer needs only parity, so the words suffice (tie-breaker). The boxes-and-cards picture would help but already exists as teaching image M2.S5.T5.C32.IMG2 in the topic before (never linked). So no diagram is added; if someone wants one, the spec would be: five empty boxes joined by + and = 30, seven heaps of cards 13, 9, 1, 7, 11, 5, 3 (counts 3, 4, 3, 4, 3, 4, 4 in the book picture).
4. **T9 "parity of the squares in 27 x 13, 42 x 78, 135 x 654" (C55/C56): none.** The book draws no grid for these sizes (the only grid picture, 3 x 4 on p.5, is the teaching figure of Small Squares in Grids, accounted to concept image M2.S8.T8.C51.IMG1). Nothing to draw usefully.
5. **C57/C58 "100th odd number": none.** The LP's `s_figure` hint (two aligned rows, evens above odds) is only two plain number lists; the book prints them as text lines on p.7. `text_alternative` on C58 gives the LaTeX option.
6. **C49/C50 "parity of differences": none.** The LP steps talk about pairs and a left-over dot, but the book prints no picture for this answer (answers are the words Even, Even, Odd, Odd). The dot pictures are teaching images of the earlier topic. A dot-pair figure would be a nicety only.
7. **T13 question figure (C73) shows the centre 5**, as the book figure (p.10, right grid) and the LP's own `q_figure` hint do, although the LP question text says only "1 at the top middle and 9 at the bottom middle". Reason: the question figure shows what the book question gives; 5 is printed in the book picture (Observation 2 says the centre must be 5).
8. **T13 solution figure (C74)** also carries eight circles "15" (3 rows, 3 columns, 2 diagonals, ANSWER green, with two dashed GUIDE lines along the diagonals) because the LP steps verify exactly those sums. They are the only extras beyond the filled square; delete them if a plainer card is preferred (the filled square alone is the minimum).
9. **Figure claims.** I claimed every base figure of book section 6.2 (pp.3-6, 23) and of 6.3 pp.7-10 (including teaching figures of topics T5, T8, T10, T12 that no chunk file owns), plus the printed-answer pictures of pp.24 and 30. Pages 11-13 and the p.25-28 printed answers belong to chunk C. The book's p.25 magic square (P25-magic_square-1) is the printed answer of Figure it Out Q1, which is chunk C's; my T13 solution draws the same square, so I made `NEW-P25-magic_square-1-t13sol` for the second use and left the base id to chunk C. At merge: if chunk C does NOT claim P25-magic_square-1, the base id must be mapped by the merger.
10. Teaching-figure accounting: where a concept image shows the same idea I used `concept_image:` (P03-dot_pattern-3, P04-dot_pattern-1/2 to C32.IMG1 as the closest; this is approximate, not the same picture). Where nothing redraws the figure (P03-dot_pattern-1/-2, P09-grid-2..5, P10-grid-2) I used `none:TEXT_SUFFICIENT`; P06-table-1 is `none:LATEX_TABLE`.
11. Old card ids: T11.C66 has two old cards (IMG1 and IMG2); the answer is one grid, so only C66.IMG1 is kept and replaced. `lp_ids_dropped` stays [] as the brief says; the builder must not leave C66.IMG2 pointing at an old card.

## 2. Things in the LP that look wrong

1. **T6.C39/C40 (End of chapter Q2, 50 loose sheets, can the pages add to 6000) contradicts the book's printed answer.** The book (p.29) says it IS possible (parity of the total is even). The LP says No, using "each sheet adds to 1 less than a multiple of 4, so 50 sheets add to 50 less than a multiple of 4, never a multiple of 4; 6000 is a multiple of 4". The LP is mathematically right: sheet j holds pages 2j-1 and 2j, sum 4j-1, so 50 sheets give 4(sum of j) - 50, which is 2 more than a multiple of 4; 6000 = 4 x 1500. The book's answer is wrong (or answers only the parity step). LP kept as it is; no figure involved.
2. **T11.C67 `question_tex` markup:** `$A 2 \times 3$ grid` puts the word "A" inside math, and `$3$ even $(e)$: numbers` has a stray colon. Similar stray colons after option labels: `$(b)$: an even number...` in T6.C41, `$(a)$: $2$ even...` in T7.C45, `$(a)$: even, $(b)$: even...` in T6.C42 answer, `Only $(a)$: is true.` in T9.C60. Cosmetic, but visible to learners.
3. **T13.C73 question text omits the centre 5** that the book figure shows (1 top-middle, 5 centre, 9 bottom-middle). With the new figure this is covered; without it the text alone leaves 5 to be deduced (Observation 2). Suggest adding "and 5 in the centre" to the text.
4. **T10.C62 is labelled "Example 2"** in the LP text, but the book has no worked example here: it is the right-hand puzzle of "Fill the grids below" (p.7). The LP's two fillings (7,8,9 / 4,6,5 / 1,2,3 and 7,9,8 / 4,5,6 / 1,2,3) were both checked and are valid; the book prints only the first.
5. T9.C58 and T7.C50 solutions rely on dot/pair or two-row pictures that the book does not print for these answers (see calls 5 and 6).
6. T11.C68: the LP's "another answer" (e,o,e / e,o,o) was checked and is valid; only the first (the book's printed one) is drawn.
7. No book-number mismatches found: T6 Q1/Q2/Q5/Q6 and T9 Q10, T11 Q3 match the end-of-chapter Figure it Out numbers on p.18.

## 3. Where the book itself is unclear

- The book prints no answer for the "Try completing it!" magic-square task (p.10); the LP's square (8 1 6 / 3 5 7 / 4 9 2) equals the printed answer of the later Figure it Out Q1 on p.25. Mirror images are also magic squares, so the choice is the book's, not forced.
- Fill-the-grids answer (p.24): "Try to find out other possible ways" is printed, yet only one filling per grid is shown; the left grid has exactly one answer, the right grid has two.
- Loose-sheets answer (p.29): see LP problem 1.
- Kishor puzzle (p.3): the book asks to find which five cards add to 30; the LP turned it into a yes/no. The picture counts (13 x3, 9 x4, 1 x3, 7 x4, 11 x3, 5 x4, 3 x4) were checked on the page picture.
- Inventory doubts: none of the base entries I claim carried an `unclear` note; I checked P03, P07, P09-grid-2, P10-grid-2/3, P18, P24, P30 against the page pictures and found the base descriptions correct.

### Chunk C notes (from the decision agent)
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
