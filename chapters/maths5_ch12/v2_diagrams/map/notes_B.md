# Chunk B notes - Class 5 Ch 12 "Racing Seconds" (topics M2.S11.T11, M2.S12.T12, M2.S13.T13, M3.S14.T14)

Result: 26 items (14 units): required 14 / optional 0 / none 12. Validator: errors 0, 6 warnings (all "required but no inventory figure maps to it": the two T12 worked examples and the four T13 draw-the-hand solutions; their figures are not printed in the book, so that is expected).

Figures claimed from the base inventory: P05-clock-1..4 and P06-clock-1..4 (all eight map to the question item of T13 C47, C49, C51, C53, C55, C57, C59, C61). The double number lines P07-number_line-1 and P08-number_line-1 sit in chunk C's T15 questions (Let Us Do Q1), so they are NOT claimed here; T14's worked examples do not use them. The pictures on p.158 (girl skipping, children running) and the Zainab/Remo speech bubbles on p.161 are decoration and are not in the base inventory; nothing was added.

I checked every base description of P05/P06 against the page pictures (enlarged crops). All eight are correct as descriptions of what the book prints; the `unclear` doubts are confirmed as drawing inaccuracies in the book (see "Book mistakes" below).

## 1. Judgement calls

- **T11 Let Us Find Q1-Q3 (C38-C43): all six items `none`.** The book gives no figure; the child times a real activity on a real clock, and the LP sample answers are the child's own readings ("your answer may differ"). Codes OPEN_ENDED + TEXT_SUFFICIENT. MEASUREMENT_READING was not used because the reading is taken on the child's own watch, not on a printed dial.
- **T12 C44 and C45 (worked examples on the seconds hand): `required`.** Their own diagrams (media ids `...C44.IMG2` and `...C45.IMG2`, because IMG1 is the kept teaching image of each concept). Reasoning: the whole example is about reading a seconds dial, part (b) of C44 crosses 12, and C45's answer is a dial position; the dial changes how easily the child sees the stretch. User decision 5 is followed: the kept teaching images are not linked and are not the reason for any decision.
  - C44: ONE image holds both parts (a worked example has one diagram): two dials labelled (a) and (b), each with a grey dashed start hand, a red stop hand and a clockwise arrow from start to stop. No seconds value is written. Letters are shown because the LP steps refer to the parts by letter.
  - C45: ONE dial with the starting hand on 10 only. The stop position (3) is the answer and is not drawn. The question also asks about the minute hand but gives it no position, so no hour or minute hand is drawn (nothing invented).
- **T13 observe-the-clocks questions (C47, C49, C51, C53): question `required`, solution `none` (SAME_AS_QUESTION_DIAGRAM).** The answer is a number read off the same two dials; the printed pdf has no answer section; the LP solution adds no new mark. Sibling consistency: all four solutions are `none`.
- **T13 draw-the-missing-hand questions (C55, C57, C59, C61): question `required` and solution `required`** (ANSWER_IS_FIGURE, derived_from the question diagram). The solution figure is the same two clocks with ONE added seconds hand in ANSWER green on the right clock (4, 6, 9 and 7). No sweep, no label.
- **T14 C63 and C64 (hours-minutes, minutes-seconds conversions): `none`** (LATEX_ARITHMETIC, TEXT_SUFFICIENT). Pure multiply/add/subtract; the kept teaching images (double number lines) stay and are not linked.
- **Colour of the seconds hand.** The LP solution for C48 says "the thin red hand", and the book draws it red. Style tokens have no red (WRONG is vermilion and reserved), so given seconds hands are drawn in `#D62828` (stated in `manim_description` and `content.hand_styles`); hour and minute hands are INK, thick, with different lengths; hands added by a solution are ANSWER green as the prompt says.
- **Hour hand at exact 3:45 in Q2 (observe) and draw Q2.** The book draws the hour hand at about 117 degrees (a little nearer 4 than it should be); the spec uses 112.5 degrees (exactly 3 3/4). Drawn hour hands everywhere use (hour + minute mark / 60) x 30.
- **Diagram type.** `measurement_scale` (clock face is listed there) for all clock figures; aspect 16:9 for all.

## 2. Book mistakes corrected in the specs (user decision 1)

The base inventory keeps what the book prints; the specs show the corrected value.
- **Observe Q3 (P05-clock-3, C51).** The book draws the minute hand exactly on 6 on BOTH clocks, but the seconds hand goes 45 s to 60 s, which completes a minute (5:30 and 45 s to 5:31 and 0 s). Spec: right clock minute hand at 186 degrees (31 minutes, one mark past 6). Same convention as the book's own Q4 and Q7. The LP solution does not mention the minute hand here, so the answer text is unaffected. If you prefer the exact book picture, change the right clock's minute hand to 180 degrees.
- **Draw Q4 (P06-clock-4, C61/C62).** The book draws the right clock's minute hand on 12, but the LP solution (and 55 s + 40 s = 95 s) says the minute hand has moved on by one mark. Spec: right clock minute hand at 6 degrees (one mark past 12), both in the question figure and in the solution figure.
- Observe Q2 / draw Q2: hour hand drawn exactly at 3:45 (see above); not a print slip, a drawing inaccuracy.

## 3. LP text issues (no LP text was edited; no decision changed because of them)

- **M2.S13.T13.C60 and C62 (solution `text` field):** the `text` still contains the old card markers "[Image: Let us do: Ans7: solution]", "[Image: ... (continued)]" (and the same for Ans8) between the steps, because these answers had two cards (IMG1, IMG2). The new plan has ONE solution diagram per answer, placed before the first step. Suggested: remove both marker lines from `text` (the build should regenerate `text` from the steps) so no stray marker is left.
- **M2.S13.T13.C51 (Ritu, observe Q3), steps_tex:** suggested extra sentence after step 2 so the picture and the words agree: "The minute hand in the right clock has also moved on by one mark, because the seconds hand has just finished a minute."
- **M2.S13.T13.C55, C57, C59, C61 (questions):** the question text does not say that the LEFT clock shows the starting time of the activity; the figure carries it. No change needed if the question figure is always shown; suggested sentence if you want the text to stand alone: "The clock on the left shows when the activity began."
- **M2.S13.T13.C47, C49, C51, C53 (questions):** same point: "The clock on the left shows the start and the clock on the right shows the end."
- **M2.S12.T12.C45 (worked example):** the question asks "what happens to the minute hand?" but gives no minute-hand position; the answer ("moves on by one mark") works without one. Fine; mentioned because the picture shows a seconds hand only.
- `q_figure` / `s_figure` hints in the units are not LP text; for the record, C49's hint "hour hand on 4" and C61's hint "minute hand on 12" on both clocks differ from the specs for the reasons in section 2.
- Book numbering: the LP calls the draw-the-hand questions "Let us do: Q5 to Q8" (concepts C55-C61) but the book numbers them 1-4 on p.160, and the `book_number` fields say "Q1..Q4 (drawing the seconds hand)". Consistent enough; just a note for anyone matching by number.

## 4. Borderline (applied the v3 rules as written; none flipped for LP text carrying the numbers)

1. **T12 C44 and C45 `required`** although the data are in the question text: the dial is the subject (MEASUREMENT_READING) and (b) crosses 12; judged that the picture changes how correctly and how easily the child solves it. If you read the tie-breaker more strictly ("text alone is enough") these two become `none` with TEXT_SUFFICIENT; they are the only required items that rest on that judgement.
2. **T13 observe solutions `none`.** A shaded sweep from start to stop (labelled 30 / 35 / 15 / 60 seconds) would be a nicety, and it is the same kind of addition for all four, so all four stay `none`. Q4 (the full round, 60 seconds) is the one where a picture helps most; kept `none` for sibling consistency. If you want it, Q4 is the candidate for `optional`/`required`.
3. **T11 Let Us Find solutions `none`.** Sample answers mention hand positions; open activity, no figure in the book.
4. **T14 worked examples `none`.** A double number line would help the idea, but it is the job of the kept teaching image; the question itself is arithmetic.
5. **Minute-hand corrections** (observe Q3, draw Q4): see section 2. Borderline between "drawing inaccuracy" and "print slip".

## 5. Places where the book itself is unclear

- p.158 / p.159-160: the minute and hour hand positions are only approximately right in several clocks (hour hands about 4 degrees off, minute hand on a mark instead of between marks). The spec uses the minute-mark convention: minute hand at (minutes) x 6 degrees, hour hand at (hour + minutes/60) x 30 degrees.
- p.160 draw Q3: the right clock's minute hand "just past 6" is drawn at about one mark; the spec uses exactly one mark (186 degrees). The hour hand there is a hair further on than the left (165.5 vs 165 degrees), as in the book.
- The book has no printed solutions section; every solution figure is derived from the LP steps.
