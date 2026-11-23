# Notes for chunk C (Class 8 Ch 8 "Fractions in Disguise")

Chunk C = topic M2.S7.T7 (Figure it Out Q1 to Q12, section 1.2, book pp. 12-14) and topic M3.S8.T8 (the three worked blocks of concept C82 "Measuring a change"; the book has no figure for them).
Result: 27 items, required 3 / optional 0 / none 24. Required: Q1 question (C57), Q1 solution (C58), Q2 solution (C60). Validator: errors 0, warnings 3 (see end).

## 1. Judgement calls

- **Q1 question (C57) required, one picture.** The book prints three pairs of bar models (pp. 12-13). The LP keeps Q1 as one concept, so there is one question diagram holding rows (i), (ii), (iii). The three base figures P12-bar_model-2, P12-bar_model-3 and P13-bar_model-1 all map to this one item. I checked all three against the page pictures (5, 10 and 4 cells; right spans of 4, 6 and 3 cells; 20%, 60, 75, 90, 140): the base descriptions are right, no CORRECTED entry needed.
- **Q1 colours.** The book uses pink, orange and green bars. The colours carry no meaning, so all bars are INK.
- **Row labels (i), (ii), (iii) are drawn** in the Q1 figures (decision 3) because the LP answer text refers to "(ii)" and "(iii)". Same for the panel labels (i) to (vi) of the Q2 solution figure: the LP answer (C60) refers to the parts by letter.
- **Q1 solution (C58) required, derived_from C57.IMG1.** The answer is the same bar pairs with the four "?" marks filled in (ANSWER green): (ii) 10% and 54, (iii) 25% and 105. Row (i) is worked out in the book and stays as given. Because the solution figure re-uses the three book figures, the inventory has three second-use entries `NEW-P12-bar_model-2-sol`, `NEW-P12-bar_model-3-sol`, `NEW-P13-bar_model-1-sol` mapped to C58 (solution).
- **Q2 question (C59) none.** The book gives no figure; the learner is told to draw the bar models. A question figure would be invented (companion note).
- **Q2 solution (C60) required, one picture with six panels, derived_from null.** The question explicitly asks for bar models, so the drawn models are the answer to that part (v3 B2, ANSWER_IS_FIGURE), although the LP text only says "Each gets a quick bar sketch". The LP did not split Q2 into parts and a pair gets one solution diagram, so the six models sit in one 2 x 3 grid. The book prints no solutions, so the layout is mine; every number is from the LP solution. Cell choices (to avoid fractions of cells where possible): (i) 4 cells of 25% = 40; (ii) 25 cells of 4% = 10, four cells = 40; (iii) 10 cells of 10% = 36, 6.2 cells shaded; (iv) 7 cells of 20% = 8, five cells = 100%, seven = 140% (matches the LP wording "40 + 16"); (v) 10 cells of 10% = 6 min with a 1% strip (0.06 units wide) shaded; (vi) 10 cells of 10% = 1 kg with 70% of cell 1 shaded. Panels (iii), (v), (vi) need partial shading of a cell; this is stated exactly in the spec.
- **Q3 to Q12, question and solution: all none.** No book figure for any of them (Q10 has only a decorative badminton coach, Q8 only the Math Talk icon). Answers are numbers, symbols or short statements.
- **Worked blocks of C82 (units 49, 50, 51) all none (`no_image`).** Tomatoes (12 / 30 x 100 = 40%) and Footfall (60 / 160 x 100 = 37.5%) have no figure in the book. The bar model of the Rs 30 to Rs 42 rise already exists as the teaching image `M3.S8.T8.C82.IMG1`; it is never linked. Block 2 is the "Check my thinking" multiple-choice item (a shirt falls from Rs 500 to Rs 400, answer 20%): text only, the confidence faces are not a figure.
- **Figures not claimed by chunk C.** P15-label-1, P15-label-2 and P15-table-1 (Know Your Contents, p. 15) sit in topic M3.S8.T8's book pages but are the given figures of the question of unit 53 (M3.S9.T9.C85, chunk D), so I left them to D. P11/P12 Day 7-8 table and bar (P12-table-1, P12-bar_model-1) belong to chunk B (units 34, 35). The badminton coach (p. 14) and the Math Talk icon (p. 13) are decoration and are not in the base inventory; I did not add them.

## 2. LP text issues

(Nothing was edited; each is a suggestion.)

- **M3.S8.T8.C82, block 0 (Tomatoes):** the question is only the word "Tomatoes" and the step "12 over the old price 30." omits the new price. Suggested question: "The price of 1 kg of tomatoes was Rs 30 three years ago and is Rs 42 now. Find the percentage increase." Suggested step: "Increase = 42 - 30 = 12; 12 over the old price 30 gives 12/30 x 100."
- **M3.S8.T8.C82, block 1 (Footfall):** same problem. Suggested question: "The average footfall in a theatre was 160 before COVID and is 100 now. Find the percentage decrease." Suggested step: "Decrease = 160 - 100 = 60; 60 over the old footfall 160 gives 60/160 x 100."
- **M3.S8.T8.C82, block 2 (Check my thinking):** the learner-visible text ends with "Act on the diagnosis table.", an authoring instruction; remove it. The block also has no `steps` / `answer` fields (the answer "(b), reason (ii)" is only inside `text`).
- **M2.S7.T7.C57 (Q1 question):** the question text carries a parenthesis describing the figure ("Pairs of bar models: (i): 5 cells, one cell = 20% ..."). It reads like an authoring note and repeats the new diagram. Suggested question: "1. Find the missing numbers. The first problem has been worked out."
- **M2.S7.T7.C60 (Q2 solution):** the only step is "Each gets a quick bar sketch." and says nothing about what the sketches show. Suggested step (it now follows the six-panel figure): "In each bar, split the whole into equal cells and shade the cells that make the asked share."
- **M2.S7.T7.C66 (Q5 solution), part (iv):** "the $AI$ checks them" is internal wording in a learner answer, and `$AI$` in LaTeX is set as a variable. Suggested: "(iv): Any two questions of the same kind, with their answers, are fine."
- **M2.S7.T7.C78 (Q11 solution):** "The $AI$ uses the current year's figure if the student looks it up." has the same problem. Suggested: "Use the latest world population the student finds; with 8.2 billion (2025) the answer is about 7.4 billion."
- **M2.S7.T7.C67 (Q6 question):** `question_tex` writes "(ii)" without the colon that (i) and (iii) have: "(ii) \underline{...} is 40% of 4." Suggested "(ii):".
- The LP numbers checked out against the mathematics for Q1 to Q12 (for example 29% of 43 = 12.47, 92% of 110 = 101.2, 1% of 168 h = 1.68 h = 100.8 min, shown as "about 101"); no solution contradicts the book.

## 3. Borderline

- Q1 question: kept `required` although the LP question text carries every number (decision 4); the figure is the book's given figure and the learner fills its "?" marks.
- Q2 solution: `required` on the strength of "also draw their bar models"; the LP text alone would not need a figure.
- Q3 (3/4 of 60 ml), Q9 (20% takes 18 days), Q10 (10 : 80 : 10 of 90 minutes), Q12(ii) (40 : 40 : 20 of 2 kg) and the worked blocks Tomatoes and Footfall: a bar model would be natural, but the book draws nothing, the question gives no figure and the numbers are one-step arithmetic, so `none` (tie-breaker). If more pictures are wanted, Q10 and Q3 (solution side) are the first candidates, then the Tomatoes worked example.
- Q4: the book says "Visualising or estimating can help" but gives no figure and the answers are symbols: `none`.
- Q5(iv) and Q7 ("Create such questions", "Make 2 more") are partly open-ended; the closed parts decide, `none`.

## 4. Book unclear

- Nothing contradictory in the Q1 figure. The page images carry the "(c) NCERT not to be republished" watermark; it is not part of any figure.
- This pdf has no printed solutions, so there are no printed-answer pictures; the Q1 and Q2 solution figures are built from the LP solution text.

## Validator warnings (accepted)

- Two `visible_text` strings of the Q2 solution have more than six tokens ("1% = 0.6 min = 36 s", "7% = 0.7 kg = 700 g"): each is one label line of a bar model.
- M2.S7.T7.C60 (solution) has no base-inventory figure mapped, as the figure is not printed in the book.
