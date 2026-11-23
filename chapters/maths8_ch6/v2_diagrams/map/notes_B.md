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
