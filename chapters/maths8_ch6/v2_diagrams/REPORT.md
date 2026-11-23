# Class 8 Ch 6 We Distribute, Yet Things Multiply - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths8_ch6` v32 (taken from staging). Result: new V2 version v33 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (90 items from 47 units)
{"question": {"none": 32, "required": 9, "optional": 2}, "solution": {"none": 32, "required": 11}, "worked_example": {"none": 3, "required": 1}}

Optional, NOT added: [('C47', 'question'), ('C58', 'question')]

needs_lp_text_sync: []

## The 21 diagrams
| id | side | type |
|---|---|---|
| M2.S3.T3.C10.IMG1 | question | cell_grid |
| M2.S3.T3.C11.IMG1 | solution | cell_grid |
| M2.S9.T9.C38.IMG1 | solution | other |
| M3.S11.T11.C48.IMG1 | solution | mensuration_figure |
| M3.S13.T13.C59.IMG1 | solution | mensuration_figure |
| M4.S19.T19.C87.IMG1 | question | cell_grid |
| M4.S19.T19.C88.IMG1 | solution | cell_grid |
| M4.S21.T21.C102.IMG1 | question | dot_array |
| M4.S21.T21.C103.IMG1 | solution | dot_array |
| M4.S21.T21.C104.IMG1 | question | cell_grid |
| M4.S21.T21.C105.IMG1 | solution | cell_grid |
| M4.S21.T21.C106.IMG1 | question | geometry_figure |
| M4.S21.T21.C108.IMG1 | question | mensuration_figure |
| M4.S21.T21.C109.IMG1 | solution | mensuration_figure |
| M4.S21.T21.C110.IMG1 | question | mensuration_figure |
| M4.S21.T21.C111.IMG1 | solution | mensuration_figure |
| M4.S22.T22.C116.IMG1 | question | mensuration_figure |
| M4.S22.T22.C117.IMG1 | solution | mensuration_figure |
| M4.S22.T22.C118.IMG1 | question | number_pattern |
| M4.S22.T22.C119.IMG1 | solution | number_pattern |
| M5.S23.T23.C121.IMG2 | worked example | dot_array |

### Chunk A notes (from the decision agent)
# Notes for chunk A (Class 8 Ch 6, cbse_eng_maths8_ch6_v32)

Chunk A = topics M2.S3.T3, M2.S4.T4, M2.S5.T5, M2.S6.T6, M2.S7.T7, M2.S9.T9: 15 units, 29 items (14 pairs and 1 worked example).
Result: required 2 (question C10, solution C11), optional 1 (solution C38), none 26. Validator: errors 0, warnings 0.
Output file: `map/out_A.json`. Builder script (kept outside HERE): scratchpad `build_out_A.py`.

Only one picture in the whole chunk is something a learner needs: the Figure it Out Q1 multiplication grid (book p.7, answers p.25). Everything else is algebra or arithmetic that the text and LaTeX carry fully, and no question of the chunk is given with a figure.

## 1. Judgement calls

- **M2.S3.T3.C10 (question) required, M2.S3.T3.C11 (solution) required.** Book Figure it Out Q1 (printed page 142). The question says "Observe the multiplication grid" and "as shown in the figure": the 10 x 10 table, the outlined 3 x 3 block (rows 3-5, columns 5-7, middle 24 = 4 x 6), its enlarged form 3 x 5 ... 5 x 7 and the empty frame with pq in the middle exist only in the picture (FIG_REFERENCED, DATA_IN_FIGURE, ACTION_ON_FIGURE). The printed answer ("Ans. Observe grid.") is the same frame filled with the nine expressions; the LP solution gives the same nine in words. Rule B2 (filled figure, ANSWER_IS_FIGURE): solution required, `derived_from` = C10.IMG1, same layout, the eight added cells in ANSWER green, pq stays INK. Aspect ratio 16:9 as the brief says (the book picture is about 2:1; the grid is drawn 836 px square on the 1080 px height, the two 3 x 3 frames on the right).
  - The book's yellow header cells and pink corner cell are drawn CELL_FILL, its red frame FOCUS, its black dashed connectors GUIDE (no red in the token table).
  - The question diagram shows exactly what the book gives (grid, block, enlarged example frame, empty pq frame) and nothing of the answer.
- **M2.S9.T9.C38 (solution) optional, not added.** See Borderline 1.
- **M2.S4.T4.C12 worked example none.** See Borderline 2.
- **All other 25 items none.** Questions: `TEXT_SUFFICIENT` (the question gives numbers or expressions and no figure). Solutions: `LATEX_ARITHMETIC` (expansions, identity checks, carry steps, one-line products; the book prints text for every answer except the two pictures above). Teaching images (concept images C2-C4, C12-C16, C31-C34 of this module) are never linked.
- **C6/C7 (two blocks sharing one card).** One decision per side covers both blocks (none): the extra block "both numbers up by 1 / one up, one down" has no figure either. The question text field in the map joins the two block questions with " || ".
- **Figure inventory (20 base figures, none missing, no NEW- figures).** Page 1 has only the chapter-opening art, pages 5, 6 and 24 hold text and equations only. Mapping choices:
  - Equation displays with arrows that a teaching image already shows: P02-annotated_expression-1, -3 and P02-dot_array-2 -> concept image M2.S2.T2.C2.IMG1; P03-annotated_expression-1 -> C3.IMG1; P03-annotated_expression-2 -> C4.IMG1; P04-dot_array-2 -> M2.S4.T4.C12.IMG1; P08-column_addition-1 and P09-step_sequence-1 -> M2.S8.T8.C31.IMG1; P26-column_addition-1 -> M2.S8.T8.C34.IMG1 (accounting only, nothing linked).
  - Displayed equations or letter column-additions with no matching teaching image: `none:LATEX_ARITHMETIC` (P02-annotated_expression-4, P04-annotated_expression-1, P08-column_addition-2, P09-column_addition-2, P26-column_addition-2, P27-column_addition-1, P27-column_addition-2).
  - P07-table-1 is the first use of the grid figure (-> C10 question). The answers page reprints it as P25-table-1 and P25-table-2 (same picture): mapped to the same item C10 (question). P25-table-3 (the filled table) -> C11 (solution).
  - P26-column_addition-2, P27-column_addition-1, P27-column_addition-2 are printed answers to "What could be a general rule ... 101 / 1001 / 10001". The LP has no question for these general rules (it asks 3874 x 101, 89 x 101 ...), so no item exists to attach them to; I used `none:LATEX_ARITHMETIC`. Self-check 0 of the prompt asks that printed-solution pictures map to a solution item, a concept image or SAME_AS_QUESTION_DIAGRAM; for these three that is impossible without an LP question.
- **Sibling consistency.** C28, C22, C24, C20 (expansions) all none; C36, C40, C42 (one-line products) all none; C38 differs only because the book prints a picture for part (ii). Reason stated in the item.

## 2. Borderline

1. **M2.S9.T9.C38 solution (Evaluate 94 x 11 ... 4791256 x 11): optional, not added.** The book answer page 26 prints a hand-style carry layout for part (ii) only ("Try other parts"): digits 4 9 5, two arcs, two circled carry 1s, "x 1 1", a rule, "(4 + 1) 4 4 5", "= 5445", notes "5 + 9 = 14", "9 + 4 = 13 + 1 = 14". Rule B2 says a printed picture answer is `required`; Step C names column arithmetic as LaTeX. I treated it as an arithmetic carry layout (the base inventory also says "LaTeX-able") and chose optional because: the LP steps state every sum and carry of all four parts, teaching images C31 and C34 show the same one-line picture, and one picture would cover only one of four sub-answers. If you want it drawn, it becomes a `required` solution (no question diagram, `derived_from` null) of one layout: INK digits 4 9 5, FOCUS arcs 4-9 and 9-5, circled 1s, ANSWER row (4 + 1) 4 4 5 and "5445". Decision for you.
2. **M2.S4.T4.C12 worked example ("use the four parts"): none.** The four-part rectangle is already the kept teaching image M2.S4.T4.C12.IMG1 of this same concept (book p.4 dot array), the four parts ab, mb, an, mn are named in the steps and every number is in the words. No v3 trigger applies; a new drawing would repeat the teaching image. If you prefer a drawing, spec it as 25 x 32 split into 23 x 27 = 621, 23 x 5 = 115, 2 x 27 = 54, 2 x 5 = 10.
3. **M2.S3.T3.C11 solution: required although the printed answer looks like a plain table.** The nine expressions could be a LaTeX array (LATEX_TABLE), but they complete the empty frame of the question figure, which is `ANSWER_IS_FIGURE` / `ACTION_ON_FIGURE`.
4. **M2.S3.T3.C6/C7 and M2.S5.T5.C17/C18: none.** An area-model rectangle (23 by 27 plus one column; 10 by 10 with a 3 by 4 corner removed twice) would help, but the data is all in words, no printed figure belongs to these questions and teaching images (M2.S2.T2.C2-C3, M2.S4.T4.C13) already show it.
5. **P26-column_addition-1 mapped to concept image C34** (same layout, other number) rather than to an item, because C38's solution is not required.

## 3. LP text issues

(No LP text was edited and no decision changed because of these.)

- **M2.S3.T3.C10** (question): the text says "Observe the multiplication grid" but never says what the grid is; the table exists only in the figure. Suggested sentence: "Observe the $10 \times 10$ multiplication grid below (the cell in row $i$ and column $j$ holds $i \times j$). The $3 \times 3$ frame outlined in it is shown enlarged beside it, next to an empty frame whose middle number is $pq$." The example in the LP omits the middle row $4 \times 5$, $4 \times 6$, $4 \times 7$ (not wrong, just short).
- **Book numbers.** C10 is labelled "Distributive Property, Q1" and C19 "Distributive Property, Q2" but both are Figure it Out Q1 and Q2 (book pp.142-143); C25, C27, C29 are labelled "Figure it Out, Q1/Q2/Q3" but are book Q3, Q4, Q5 (their ncert_refs FiO1.q3, q4, q5 are right). Suggest "Figure it Out, Q1" ... "Q5" for all six.
- **M2.S3.T3.C9** step 1: "which is negative when a is at least $b$": the letter a is not in math mode; suggest "$a$ is at least $b$".
- **M2.S6.T6.C22** last step: "No two of $a^2$, $ab$ and a have the same letter-numbers": suggest "$a$".
- **M2.S7.T7.C28** steps 3 and 6: "So (i): is $...$." and "So (ii): is $...$." have a stray colon; suggest "So (i) is $4a + 5ab + ab^2 - 12b^2 - 3b^3$." and "So (ii) is $4y^2 + 44yz - 5y + 77z - 21$."
- **M2.S5.T5.C20** answer_tex: semicolons are missing after (ii), (iii) and (v): "(ii): $10 + 4a$ (iii): ... (iv): ...; (v): ... (vi): ...". Suggest a semicolon after every part.
- **M2.S4.T4.C12** (worked example): the block has only plain text (`question`, `steps`, `answer`) and no `question_tex` / `steps_tex`, unlike the other blocks; suggest LaTeX versions, e.g. "$23 \times 27 = 621$. Use the four parts to find the product when $23$ grows by $2$ and $27$ grows by $5$."
- No answer in the chunk contradicts the book. Every LP number was recomputed: 644, 648, 51, 3, -28, 104, 42, 800 (increase 179), 27 = 27, (1,6) (2,8) (3,10), 42614, 62458, 1034, 5445, 36069, 52703816, 391274, 8989, 95849, 266096831, 1112111, 963666, 23454522.

## 4. Where the book itself is unclear or slips

- **Chapter p.2 (P02-annotated_expression-4):** "a (b + 1) = ab x [a]" is printed with a multiplication sign; it must be a plus sign (ab + a). Teaching figure only, nothing is drawn from it.
- **Chapter pp.8-9 (P08-column_addition-2, P09-column_addition-2):** the zero digits of the letter layouts are printed as the letter o ("d c b a o", "d c b a o o"); the answers pages print a proper 0 (P26/P27). Teaching figures only.
- **Answers p.24:** the printed answer to "Will the product always increase? Find 3 examples where the product decreases" uses (a - 1)(b - 1) < ab (a = 10, b = 3: 18 < 30), but the question is about (a + 1)(b - 1). The LP solution (C9) answers the question as asked, which is right.
- **Answers pp.26-27:** the printed answers to Evaluate (i) to (iv) and to the 101/1001 questions are partial ("Ans. (ii)", "Try other parts", "(iii)" and "(v)" only); the LP gives all parts.
- **Chapter p.7 vs answers p.25:** the grid figure is the same on both pages; the answers page splits the "enlarged frame" and the "empty frame" visually but they are one figure (kept as one diagram).

### Chunk B notes (from the decision agent)
# Chunk B notes (Class 8 Ch 6, cbse_eng_maths8_ch6_v32)

Units: M3.S11.T11, M3.S13.T13, M3.S14.T14, M3.S15.T15, M3.S16.T16, M4.S18.T18 (16 units, 30 items).
Result: required 2 (both solution side) / optional 2 (both question side) / none 26. Validator: errors 0.
Output: `map/out_B.json`. Every number in the two drawn figures was recomputed (see accuracy_checks in the JSON).

## What is drawn, and why only these two

| Item | Decision | Figure |
|---|---|---|
| M3.S11.T11.C48 (solution), Ans1 of The Square of a Sum | required, `M3.S11.T11.C48.IMG1` | Two squares of side 65 side by side: split 60 + 5 (3600, 300, 300, 25) and split 30 + 35 (900, 1050, 1050, 1225), totals 4225. |
| M3.S13.T13.C59 (solution), Ans1 of The Square of a Difference | required, `M3.S13.T13.C59.IMG1` | A square of side 60 holding a square of side 55 (3025) in its corner; the two 5 by 60 strips (300 each) and the 5 by 5 corner (25) marked. |

Reason: both answers are geometric arguments (the book says "Draw the figures and check the area", p.10; and argues 55^2 inside a 60 square, p.11). v3 Step B2 `ANSWER_IS_FIGURE` applies even though the LP steps describe the parts in words. The questions give no figure, so both solution diagrams stand alone (`derived_from` null).

The other 26 items are algebra or arithmetic: expansions, evaluations with an identity, reasoning with a numeric check, the twelve "Mind the Mistake" cards. They stay text/LaTeX.

## Borderline

1. **C47 question and C58 question: optional, not none, not required.** The text carries every number (the splits 60 + 5, 30 + 35; the squares 55 and 60), so a careful student can attempt both without a picture (tie-breaker: it only makes it nicer). The book figures on p.10 and p.11 also carry the part labels (60^2, 60 x 5, ... and -60 x 5, +5 x 5), which are the explanation, i.e. the solution. If the content team wants the question to show a picture anyway, the question figure would be: C47 = the 60 + 5 square with side lengths 60, 5 only; C58 = a 60 square with a 55 square in the corner, labels 60, 55, 5 only (no area labels). Then both solution diagrams could be marked `derived_from` those. I did not add them.
2. **C58 solution drawn although its twin question has no figure.** The book argues 55^2 only geometrically, so the answer is the picture (strips removed twice, corner added back once). Sibling check: the other answers of T13 (99^2/58^2, expansions) are plain evaluations, so they stay `none`, with a "Sibling note" in the reason.
3. **C50, C54 (104^2, 37^2 and (3j + 2k)^2) none although teaching images C46 and C45 draw the same squares.** The questions only ask to expand or evaluate and the book prints no figure for them; a teaching image is never linked.
4. **C64 and C66 worked examples (T14) none.** C64 has a teaching image of two 5 by 5 and two 6 by 6 squares, but that figure is not in the book; the worked example is a numeric check plus a general expansion. C66 is pure arithmetic.
5. **C81 / C82 (the 12 cards) none.** The cards are boxed equations; they match the "Not a diagram" family (list in boxes, equations). The only thing lost is the working lines of the cards, which is an LP text issue (below), not a figure issue.
6. **C73 (Express 100 as a difference of two squares) none, `LATEX_TABLE`.** The book's printed answer is a plain trial table of numbers; the LP solution uses the factor method (50 x 2) instead, and the LP text wins.
7. **Shape of the C48 figure: one card with two squares** (not two images), because the question gives one answer and the brief allows one solution diagram per pair. Strips of the 60 + 5 square are drawn 0.7 of 6.0 (true ratio would be 0.46); `to_scale` is false, as in the book.
8. **C59 figure: dashed full-length rectangles.** The book draws the strips 55 long with a separate darker corner but labels them "60 x 5" and "5 x 60". My spec draws the same cells and adds two dashed FOCUS rectangles of the full 5 by 60 length so that the labelled 300 is visibly 60 long and the overlap is the 5 by 5 corner.
9. **Callout wording uses no minus or plus signs** (book prints -60 x 5, -5 x 60, +5 x 5): the LP solution text carries the removal and the add-back in words, and a sign on a callout next to a positive area would read wrongly. Change if the team wants the book's signs.

## LP text issues (not edited; listed only)

1. **M3.S11.T11.C47** (question): the text never says the 65 square is cut into four parts or that the areas of the parts are wanted, and it omits that the 30 + 35 split should be drawn. Suggested: "A square of side 65 is split as 60 + 5 into a 60 square, a 5 square and two 60 by 5 rectangles. Write the area of each part and add them to find $65^2$. Draw the square again split as $30 + 35$ and check that the area is the same."
2. **M3.S13.T13.C58** (question): "Find $55^2$ from the square of side $60$." does not say where the 55 square sits. Suggested: "A square of side $55$ sits in one corner of a square of side $60$. Use the area of the $60$ square and the strips around the $55$ square to find $55^2$."
3. **M4.S18.T18.C81, extra block (E1), part (a)**: `question_tex` has `\frac{1}{2(10s - 6)} + 3 = 5s`, which prints 1 over 2(10s - 6). Card 7 is one half times (10s - 6). Suggested: `$(a)$: $\frac{1}{2}(10s - 6) + 3 = 5s$`. The plain `question`/`text` also read "1/2(10s − 6)", which is ambiguous; suggested "(1/2)(10s − 6) + 3 = 5s".
4. **M4.S18.T18.C81 (both blocks): the working lines of the cards are missing.** The book cards show, for example, card 1 "−3p(−5p + 2q) = −3p + 5p − 2q = p − 2q", card 2 "= 2x − 1 + 3x + 4 = 5x + 3", card 3 "= (y + 2)^2 = y^2 + 4y + 4", card 6 "= 6ab × 9ac = 54a^2bc", card 7 "= 5s − 3 + 3 = 5s", card 10 "= (x + 2)x + (x + 2)5 = x^2 + 2x + 5x + 10 = x^2 + 7x + 10". The LP lists only the first and last expression, yet the question asks to explain what went wrong. Suggested: add the middle line to each of (a)-(f) in both blocks.
5. **M4.S18.T18.C82, answer_tex and steps_tex (f)**: `$18$abc` should be `$18abc$` (steps step 6 and answer_tex). Also in `answer_tex` the parts run together: `$(a)$: $15p^2 - 6pq (b)$: $5x + 10$; ... $25m^2 + 60mn + 36n^2 (e)$: correct $(f)$: $18$abc`. Suggested: `$(a)$: $15p^2 - 6pq$; $(b)$: $5x + 10$; $(c)$: $3y + 4$; $(d)$: $25m^2 + 60mn + 36n^2$; $(e)$: correct; $(f)$: $18abc$`. The extra block has the same problem: `$(c)$: $5a^3 + 6a^2b + 6ab^2 (d)$: $ab + 4a + 2b + 8$` should be `... 6ab^2$; $(d)$: ...`.
6. **M4.S18.T18.C81 / C82**: part letters (a)-(f) restart in the second block; the book numbers the cards 1 to 12. Suggested: keep the letters but add "cards 1 to 6" and "cards 7 to 12" to the two question texts so the learner can match the book.
7. **M3.S13.T13.C62 (question_tex)**: `(i)` has no colon but `(ii):` and `(iii):` do. Suggested: use `(i):`, `(ii):`, `(iii):` throughout. In **C63 steps_tex** step 5, "so (iii): is" reads wrongly; suggested "so (iii) is".
8. **Book numbers in T16** (`book_number`): "Figure it Out, Q1/Q2/Q3" are the book's Figure it Out Q2, Q3, Q4 on p.14 (the book's Q1 is "Which is greater", which the LP files in T15 C70 as "Squares and Patterns, Q1"). The `ncert_refs` (FiO2.q2, q3, q4) are right; only the displayed numbers are one too low.
9. **M3.S11.T11.C49** says "split 104 and 37 into sums of numbers"; the book hint says "sums or differences". Harmless; the LP solution uses sums for both.

## The book itself (unclear or wrong)

1. **p.28, answer to Figure it Out Q2**: the trial table is printed a | b with the first rows 25 | 125, 36 | 136, 49 | 149 (b = a + 100, "Not a square"), but the last row is printed 676 | 576. The pattern gives a = 576, b = 676; the printed order is a print slip. The base inventory keeps what the book prints; no diagram uses the table, so nothing is corrected in a spec. The column header "Difference" holds the words "Not a square" / "Square" (it is a trial column, not the difference).
2. **p.15, card 6**: the last line is printed "54a2bc" (superscript missing). The LP writes 54a^2bc, which is what the card means.
3. **p.10 and p.11 figures are not to scale** (the 5-wide strips are drawn about one fifth of the side). The specs also say `to_scale` false.
4. **p.11 figure**: the right strip is drawn 55 tall and the bottom strip 55 wide, with the 5 by 5 corner drawn separately, yet the callouts say 60 x 5 and 5 x 60. This is consistent only when read as two overlapping 60 by 5 rectangles; the C59 spec shows that explicitly.
5. **Printed answers are missing** for the questions on p.10 to p.12 (65^2, 104^2, 37^2, (6x + 5)^2, (3j + 2k)^2, 55^2, 99^2, 58^2) and for the p.11 comparison table question; the LP solution is the only source for those.
6. The book also asks for the split 52 + 13 of 65 (p.10, "(52 + 13)^2"); the LP asks only 30 + 35, so the figure draws only those two splits.

### Chunk C notes (from the decision agent)
# Notes, chunk C (Class 8 Ch 6, cbse_eng_maths8_ch6_v32)

Units: M4.S19.T19 (6 pairs), M4.S21.T21 (5 pairs), M4.S22.T22 (4 pairs), M5.S23.T23 (1 worked example) = 31 items.
Result: required 16 (question 8, solution 7, worked example 1), optional 0, none 15. Validator: errors 0, 4 warnings
(C111 caption has 7 whitespace tokens but is one expression; C105, C111 and C117 solutions have no printed solution picture to map).
Figure inventory: 28 base figures claimed (19 to items, 2 to concept images, 7 none).

Item numbers below use the LP's concept ids. The book's question numbers differ from the LP's (see LP text issues).

## 1. Judgement calls

**Required question figures (8 + worked example)**
- C87 calendar: book says "as shown in the figure"; the 2 by 2 square 4, 5 / 11, 12 is outlined and the other squares come from that calendar. Drawn as `cell_grid` (the catalogue lists calendars). The book's "February" banner is a title and is not drawn.
- C102 circles, C104 tiles, C106 Tadang/Yusuf, C108 slanted region (Fig. 1), C110 dashed region, C116 park, C118 patterns: all are figure-based in the book (the data or the region exists only in the picture). Kept required even where the LP text carries expressions or counts (decision 4).
- C121 Coin Conjoin (worked example): the book figure is the 10-coin triangle and its upside-down copy; the worked step "keep the middle block still and move the three corner coins" is only readable on a picture. New id C121.IMG2 (IMG1 is the kept teaching image, never linked). The picture shows both triangles with the 3 moving corner coins marked in both; the rows of the second triangle are shifted down one row so the 7 coins that stay are in the same places in both pictures (checked in code).

**Required solution figures (7)**
- C88 calendar: the printed answer is two small pictures (3, 4 / 10, 11 and the lettered block); both drawn with their diagonals and the products. The question calendar is NOT repeated in the solution card, so `derived_from` (demanded by the validator) means: same cell style, same numbers cut from that calendar, not the same layout. Said in render_note.
- C103 circles: the LP solution reads Step k two ways (square of side k + 1 minus one circle; rectangle k by k + 2). The book prints these as Methods 1 and 4 (p.16, p.17). Drawn at Step 4: left a 5 by 5 square with the missing circle dashed, right six boxes of 4 circles. Methods 2 and 3 are not used by the LP solution.
- C105 tiles: the LP solution reads Step n as a square of side n + 2 with a hole of side n, and as four rows of n plus four corners. Drawn on Step 3 (n = 3, so n + 2 = 5 agrees with the drawing).
- C109 slanted region: three panels (Anusha, Vaishnavi, Aditya), the book's three method sketches p.18-19 redrawn on the question's I figure.
- C111 dashed region: two panels, method 1 (hatched rectangle marked s - r and p - r) and method 2 (whole rectangle, strips pr and sr, corner r squared outlined).
- C117 park: the LP solution adds w + g + 2w + g + w and w + g + w; the figure marks every segment and the two totals, which shows where the 2w comes from.
- C119 patterns: part (i) asks to draw the next figure and the printed answer is Step 4 of each pattern; the card repeats Steps 1 to 3 (question arrangement at a smaller scale) and adds Step 4 in ANSWER green with the totals 36 and 29.

**None (15)**
- T19 C85/86, C89/90, C91/92, C93/94, C95/96 and T22 C112/113, C114/115: plain algebra, selection from written lists, remainders; no figure in the book (`LATEX_ARITHMETIC` / `TEXT_SUFFICIENT`).
- C107 (Tadang solution): `SAME_AS_QUESTION_DIAGRAM`, see Borderline.

**Design choices not fixed by the book**
- Proportions are symbolic. Tadang: m : n = 1 : 3 (book draws m about n / 8, too thin for labels). Fig. 1: x : y = 6 : 1 (book about 5.6 : 1). Dashed region: s : p : r = 7.8 : 6.8 : 2 (book about 3.9 : 3.4 : 1). Park: w = 1.15, g = 3.0 drawing units (book g about 2.6 w); the gap between the plots is exactly 2w. All marked `to_scale: false`. The question numbers p = 6, r = 3.5, s = 9 and x = 8, y = 3 are NOT drawn.
- Colours use the style tokens, not the book's colours: tiles and strips MARK_FILL; hatched regions drawn as INK slanting lines on white (angles read from the book: Fig. 1 up to the right 30 degrees, dashed region steeply down to the right 60 degrees, Tadang 45 degrees down to the right); pattern (a) SET_B, pattern (b) SET_A; plots CELL_FILL.
- Park: the book's squared-paper grid behind the plan is texture, not tied to w or g, and is omitted.
- Letters (a) and (b) are drawn on the two Q11 pattern figures because the LP question and the LP answer refer to the patterns by letter (decision 3). Vertex letters (A to M, P to S) of the book's method sketches are NOT drawn: the LP solution never mentions them. The panel names Anusha, Vaishnavi, Aditya are drawn because the LP solution uses them.
- Pattern step labels are written "Step 1, Step 2, ..." (the book prints plain 1, 2, 3 above the circle and tile figures on p.15 and p.17, and "Step 1..." under the Q11 patterns).
- Coins are drawn as plain coins with an inner ring (the book has photographs of one-rupee coins).

## 2. Borderline (decision 4)

- C106 Tadang question `required`: the LP text is algebra only ("Show that ... are equal") and could be done without the figure, but the book question is "find the area of the shaded region in the figure" and the meaning of m, n and both expressions lives in the picture. Same reasoning for C108 (slanted region). If the team prefers text-only for these two, set both to none.
- C104 tiles question `required` although the LP text gives the counts 8, 12, 16 (the arithmetic pattern alone would give 4n + 4). The book question is figure-based and its point is the several methods of seeing the frame.
- C87 calendar question `required` although a calendar is a table of numbers: kept because the 2 by 2 outline carries meaning (HIGHLIGHT_MEANING) and calendars are listed under cell_grid in the catalogue.
- C107 Tadang solution `none` (SAME_AS_QUESTION_DIAGRAM) but C109 slanted solution `required`. Reason: the book prints no further picture for Tadang/Yusuf (one figure serves both methods), whereas for the slanted region it prints three extra sketches (printed answer is a picture, B2). The LP solution of C107 is pure algebra; a figure with m + n and n - m marked would be an optional enhancement (stated in `text_alternative`). The two items look alike in the LP text, so this is the call most worth confirming.
- C105 tiles solution and C103 circles solution `required` although the book prints no solution picture for tiles (a plain table P29-table-1, mapped `LATEX_TABLE`) and none at all in the answers section for circles: the LP solutions describe groupings of the figure that a student cannot see from the words alone.
- C117 park solution `required`: the 2w of the printed solution is the classic trap and the marks on the plan are the answer to "where does 2w come from".
- C119 solution repeats Steps 1 to 3 at a smaller scale next to the new Step 4 (so the card is `derived_from` the question figure). Showing only Step 4 would also satisfy the printed answer; chosen so the sequence is visible.

## 3. Book mistakes corrected in the specs (decision 1)

- Q11 pattern (a), Step 3 (question page p.21): the picture has 6 cells above the right column and 6 below the left column (27 cells in all, counted from the pixels of the page picture, as the base entry P21-pattern-1 recorded). The formula (y + 2)^2, the printed answer (2 + 3)^2 = 25 and the copy of the same figure on the answers page (p.34: 5 + 15 + 5 cells) all give 25. Drawn with 5 above and 5 below (25 cells); Steps 1 and 2 are as printed (9 and 16). Said in the item's render_note and in the inventory entry (CORRECTED).
- Printed answer of calendar Q4 writes the difference as (a + 7)(a + 1) - (a + 8): the factor a is missing before (a + 8). The LP and the maths give (a + 1)(a + 7) - a(a + 8) = 7. The figure tag shows a(a + 8).
- Base inventory P17-pattern-1 (Method 4): the description says the first k columns sit in one box; the page draws each row of k circles as its own box and the right column as one more box (k + 2 boxes of k circles = 4 x 6 at Step 4). Entry marked CORRECTED.

## 4. LP text issues (not edited; concept id, what is wrong or missing, suggested sentence)

- T19 C85-C96 and T22 C112-C119: `book_number` says "Figure it Out, Q1..Q6" (T19) and "Q1..Q4" (T22) but the book questions are Q2, Q4, Q5, Q6, Q7, Q9 (T19) and Q3, Q8, Q10, Q11 (T22) (the ncert_refs say so). Suggest using the book numbers or dropping the numbers.
- M4.S19.T19.C87: the question never shows the calendar. Suggested: "The figure shows the February calendar with the 2 by 2 square 4, 5 over 11, 12 outlined. Find the products of the numbers lying along each diagonal of a 2 by 2 square, for example 4 x 12 = 48 and 5 x 11 = 55. Do this for other 2 by 2 squares of the calendar."
- M4.S19.T19.C92: `answer_tex` has unbalanced math: `$2 ($or $5$ the other way round)`. Suggested: "difference: remainder $2$ (or $5$ the other way round)".
- M4.S21.T21.C102: the question does not mention the figure or its counts, and drops the book's "draw the next figure". Suggested: "The figure shows Steps 1, 2 and 3 of a pattern of black circles, with 3, 8 and 15 circles. Draw Step 4. Write the number of circles in Step k in two ways, show that they agree, and find the number in Steps 4, 10 and 15."
- M4.S21.T21.C104: the question gives only the counts. Suggested: "The figure shows square tiles forming a square frame round an empty square; Steps 1, 2 and 3 have 8, 12 and 16 tiles. Find the tiles in Step 4, Step 10 and Step n."
- M4.S21.T21.C105: the solution speaks of "a square of side n + 2 with a hole of side n" and "four rows of n plus four corners"; only understandable with the figure (now provided).
- M4.S21.T21.C106: m and n are not defined. Suggested: "In the figure, four equal rectangles m by n surround a shaded square. Tadang finds the area of the shaded square as (m + n)^2 - 4mn and Yusuf as (n - m)^2. Show that the two expressions are equal."
- M4.S21.T21.C108: x, y, the figure and the three names are missing. Suggested: "In Fig. 1 three equal rectangles x by y form a capital I; find the area of the region with the slanting lines. Anusha, Vaishnavi and Aditya get x^2 - xy, x(x + 2y) - 3xy and x(x - y). Verify that the three are equal and find the area for x = 8, y = 3."
- M4.S21.T21.C109: the solution never says where the three expressions come from. Suggested additions: "Anusha: the x by x region between the bars minus the middle bar xy. Vaishnavi: the whole rectangle x by (x + 2y) minus the three rectangles. Aditya: the two side regions are each x by (x - y)/2, so 2 x x(x - y)/2."
- M4.S21.T21.C111: `steps_tex[2]` has broken math: `$(p - r)(s - r) = ps - pr -$ rs $+ r^2$`. Suggested: "$(p - r)(s - r) = ps - pr - rs + r^2$, so both methods agree."
- M4.S22.T22.C116: `question_tex` has "$w ft$." (math mode swallows the space) and "$g^2\text{ sq. ft}$."; it also does not say that the path between the two plots is 2w wide while it is w wide at the outside, which the solution uses. Suggested: "...a walking path $w$ ft. wide round them (2$w$ ft. wide between the two plots, see the figure)...".
- M4.S22.T22.C117: `answer_tex` malformed: `$8w^2 + 8gw sq$. $ft$., that is $8w(w + g)$`. Suggested: "$8w^2 + 8gw$ sq. ft., that is $8w(w + g)$ sq. ft."
- M4.S22.T22.C113: the LP answer (ii) lists m^2 + (m - 1)^2 as well as m^2 + (m + 1)^2; the book prints only the second. The LP is right (m - 1 and m are consecutive); no change needed, noted only.

## 5. Places where the book itself is unclear

- Q10 park: the three horizontal arrows carry no label and the question says the path is w ft wide; only the printed answer (w + g + 2w + g + w) shows that the gap between the plots is 2w. Drawn as printed (two arrows labelled w ft., three unlabelled), the solution figure labels them w, 2w, w.
- Circles (Math Talk) and Tadang/Yusuf, slanted region: the answers section prints no answer; the LP answers follow the lesson text (Methods 1 to 4, Tadang and Yusuf, Anusha/Vaishnavi/Aditya).
- Fig. 1 (slanted region): the caption says "all three rectangles have the same dimensions" while the middle rectangle stands between the two bars (so its length is x and its width y); the picture is only consistent with that reading (figure x wide, x + 2y tall).
- Tadang figure, Fig. 1, dashed region, park: all drawn not to scale in the book; proportions in the specs are illustrative and said so in the specs.
- The calendar on the answers page (p.31) is the same February calendar without the red outline.
