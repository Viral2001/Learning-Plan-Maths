# Chunk B notes (Class 5 Ch 4, topics M2.S14.T14 to M2.S22.T22)

Result: 31 items (17 units). Required 3, optional 2, none 26. Validator: errors 0 (16 warnings, all "long visible_text" for the equation lines such as `1 + 2 + 3 + 4 = 10`; they are single strings that the validator counts by spaces).

Required diagrams (all question side, no solution diagram in this chunk):
- M2.S14.T14.C37.IMG1 and M2.S14.T14.C39.IMG1: the three boxes of consecutive sums (book p.45), same spec twice.
- M2.S19.T19.C59.IMG1: the road-trip route (book p.48), drawn as a schematic route, not as the map of India.

## 1. Judgement calls

- **T14 Q1 and Q2 (C37, C39) required.** The LP text says "in each of the boxes above" and never lists the sums, so the data lives only in the figure (FIG_REFERENCED, DATA_IN_FIGURE). The box headings ("Sum of 2 consecutive numbers" ...) are the boxes' own category labels in the book; I kept them in `visible_text` so that "each box" can be told apart. Book colours replaced by house tokens (CELL_FILL boxes, INK text), no arrows, no parity marks (nothing solved).
- **T19 Q2 road trip (C59) required, drawn as a route diagram.** The four distances and the leg each belongs to exist only in the book's map. A real map of India with photographs cannot be drawn faithfully (NOT_RENDERABLE), but the data can: five cities, four arrows, four distances. I added arrowheads (the book has none) because the question text gives the order of the trip. Which distance sits on which leg is read from the label positions on the book map (the inventory agent flagged this too) and agrees with the LP solution: Delhi-Mumbai 1,600 km, Mumbai-Goa 590 km, Goa-Hyderabad 670 km, Hyderabad-Puri 1,055 km. The total 3,915 km is not drawn (it is the answer).
- **C60 (road trip solution) none.** It would only repeat the route diagram; the LP steps already add the legs in order.
- **T14 solutions C38, C40 none.** The answers are reasoning sentences; the LP steps list every sum, its parity and every difference. A solution figure would only be the question boxes with odd/even tags or +2/+3/+4 arrows (SAME_AS_QUESTION_DIAGRAM). Q3 (C41, C42) has no figure and a numeric answer: none/none.
- **Place-value charts are not images.** The book's worked solutions of Examples 3 to 6 are Th/H/T/O (or TTh/Th/H/T/O) column calculations with carry or regroup marks. v3 lists column addition/subtraction as LaTeX arithmetic and place-value header boxes with digits as HEADER_BOXES_ONLY (the Number Play audit counted these among its four needless images). `text_alternative` on C50, C52, C54, C56 and the T17 worked example says what the LaTeX array should hold. The LP steps already narrate every regroup in words.
- **T17 worked example (C47) none.** Two column calculations with practice values; the plan's kept teaching images (C47.IMG1, IMG2) are not linked and not used as a reason.
- **Example 3 and Example 5 questions (C49, C53) none.** Every number is in the LP question text; the book's maps only illustrate the route (DECORATIVE_ONLY). Examples 4 and 6 have no figure at all.
- **T22 worked example (C69) none.** Word problems with all amounts in the text and chains of plain sums; the book's route diagram for Mary (p.50) belongs to chunk C.
- **T19 Q1, Q3, T20 Q1, T21 Q1, Q2** (C57-C68 except C59, C60): lists of sums or subtractions and a "find two numbers" question, all data in the text: none, TEXT_SUFFICIENT / LATEX_ARITHMETIC. C62 has `text_alternative` for a LaTeX table of the ten pair sums.
- **Figure accounting.** P04-pattern-1 is also the book figure of the previous topic's 'cons.boxes' (chunk A). I claimed the base id for the Q1 question (first of my two uses) and `NEW-P04-pattern-1-q2` for the Q2 question. If chunk A also claims `P04-pattern-1`, the merger should keep one entry for the base id and give the other uses NEW- ids. I did not claim `P04-number_boxes-1` (teaching figure of 'cons.def', chunk A). P05-pattern-1 (the arc pattern) is mapped to `concept_image:M2.S15.T15.C43.IMG1` (accounting only; its idea is that image's pair-the-ends picture with practice values).

## 2. Borderline

1. **T15 worked example C43 and T16 solution C46: optional, not added.** An arc picture (ends paired inward, each pair marked with its total) would help, but the sums are already written as expressions in the steps (v3 Step D: an arrow picture for a sum written as an expression). C43 already has the kept teaching image C43.IMG1 showing the same idea for 41 to 45; I did not use that as the reason. If the user wants these drawn, the specs are in the reasons: run 41-45 with arcs 41-45 = 86, 42-44 = 86, 43 alone; run 52-55 with arcs 52-55 = 107, 53-54 = 107; and the four runs of C45.
2. **T16 question C45 none.** "Notice how the sums of 3, 4 and 5 consecutive numbers are related to the numbers being added" points back at the book's arc-pattern figure (P05-pattern-1, which is the teaching figure of the previous topic), but all four runs to add are in the text and the book has no printed answer that merely points at a picture, so the 'refer picture' rule does not apply. A careful student can solve it from the text.
3. **Place-value chart solutions (C50, C52, C54, C56) and T17 worked example (C47) none.** Could be argued as HIGHLIGHT_MEANING (circled regroup marks, struck digits). I followed the explicit v3 lines (LATEX_ARITHMETIC, HEADER_BOXES_ONLY). Sibling consistency: all four examples and the worked example get the same decision.
4. **T14 C38, C40 none** (parity tags / difference arrows only annotate the given boxes, see above).
5. **C59 required with a schematic route** instead of NOT_RENDERABLE (see above).
6. **C49, C53 none** while a part-whole line (total, part, remaining part) would be a nice optional picture; not needed to solve.

## 3. LP text issues

- **M2.S14.T14.C37 and M2.S14.T14.C39 (question text):** "In each of the boxes above ..." and "... in each box?" depend completely on the figure; the LP text never states the sums. With the required diagram this is fine; if the text must also stand alone, add: "The boxes show: sums of 2 consecutive numbers 3, 5, 7, 9; sums of 3 consecutive numbers 6, 9, 12, 15; sums of 4 consecutive numbers 10, 14, 18, 22."
- **M2.S19.T19.C59 (question text):** "Look at the distances marked on the map" while the four distances only exist in the figure. Suggested extra sentence if wanted: "The legs are Delhi to Mumbai 1,600 km, Mumbai to Goa 590 km, Goa to Hyderabad 670 km and Hyderabad to Puri 1,055 km."
- **M2.S14.T14.C38 and M2.S16.T16.C46 (answer `text` field):** the plain `text` of the answer still carries `[Image: ...: solution]` and `[Image: ...: solution (continued)]` markers from the old cards, placed inside the steps (after step 5 of C38, after step 3 of C46) and at the end. Neither item gets a solution diagram now, so the build must drop these markers (and, for every other concept in the chunk, the old card markers in `text`).
- **M2.S21.T21.C65, C66, C67, C68:** the label "(i)" is written without math mode while (a) to (h) are `$(a)$` ... `$(h)$` (question_tex, steps_tex, answer_tex). Suggest `$(i)$`.
- **M2.S21.T21.C66, step (i):** "put the 1 in a new place on the left. The sum is 1,05,050" does not name the place (lakhs) and switches to the Indian grouping `1,05,050` while the rest of the chapter has no 6-digit number. Suggested sentence: "Ten thousands: 5 + 5 = 10, so write 0 and put the 1 in the lakhs place. The sum is 1,05,050."
- **M2.S14.T14 and M2.S16.T16:** concept names repeat ("Sums of Consecutive Numbers: Q1/Ans1" in both topics); cosmetic.
- All other LP numbers were recomputed (sums, differences, regroups, the ten pair sums of C62, the closest pairs): no arithmetic error found in this chunk.

## 4. Where the book itself is unclear or wrong

- **p.46 (book page 46, pdf page 5): the North-South Corridor map prints "1885 km" on the upper arc**, while the text on the same page and the next page say 1,855 km (1,855 + 1,862 = 3,717). A print slip. No diagram is drawn there (C49 none); if one is added later it must show 1,855 km. The LP follows 1,855.
- **p.48 (pdf 7) road-trip map:** no arrowheads and no leg-end markers; the distance-to-leg assignment is inferred from the label positions (agrees with the LP).
- **p.56 (pdf 15) Let Us Do:** the letters are printed (a)(b)(c) | (d)(e)(f) | (f)(g)(h) in both the Add and the Subtract lists, so (f) appears twice and the lists have nine items under eight letters. The LP re-letters them (a) to (i) in the printed order; I follow the LP.
- **p.49 (pdf 8):** the blue label on the sea map is "2700 km" without the comma the text uses (2,700 km). **p.50 (pdf 9):** the printed answer row of 15,150 - 10,228 starts with a 0 (04,922); the LP writes 4,922.
- **Inventory checks:** I compared P04-pattern-1, P05-pattern-1 (arc labels 4, 6, 8 / 5, 7, 9 / 5, 7, 9 / 6, 8, 10 / 6, 8, 10 each equal the sum of the two numbers the arc joins), P05-map-1, P06-place_value_table-1 and -2, P06-aligned_addition-1, P07-map-1, P08-map-1, P08-place_value_table-1, P09-place_value_table-1 and P09-aligned_subtraction-1 with the page pictures: all base descriptions are correct, no "CORRECTED:" needed.
