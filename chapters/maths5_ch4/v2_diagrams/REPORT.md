# Class 5 Ch 4 We the Travellers - II - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths5_ch4` v5 (taken from staging). Result: new V2 version v6 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (130 items from 73 units)
{"worked_example": {"required": 3, "none": 11, "optional": 2}, "question": {"required": 15, "none": 42}, "solution": {"required": 13, "none": 39, "optional": 5}}

Optional, NOT added: [('C43', 'worked_example'), ('C46', 'solution'), ('C120', 'solution'), ('C125', 'worked_example'), ('C128', 'solution'), ('C130', 'solution'), ('C132', 'solution')]

needs_lp_text_sync: []

## The 31 diagrams
| id | side | type |
|---|---|---|
| M1.S2.T2.C3.IMG2 | worked example | other |
| M1.S3.T3.C5.IMG1 | question | other |
| M1.S3.T3.C6.IMG1 | solution | other |
| M1.S3.T3.C7.IMG1 | question | other |
| M1.S3.T3.C8.IMG1 | solution | other |
| M1.S3.T3.C9.IMG1 | question | other |
| M1.S3.T3.C10.IMG1 | solution | other |
| M1.S3.T3.C11.IMG1 | question | other |
| M1.S3.T3.C12.IMG1 | solution | other |
| M2.S14.T14.C37.IMG1 | question | number_pattern |
| M2.S14.T14.C39.IMG1 | question | number_pattern |
| M2.S19.T19.C59.IMG1 | question | arrow_map |
| M3.S26.T26.C86.IMG1 | solution | other |
| M3.S27.T27.C87.IMG1 | question | other |
| M3.S27.T27.C88.IMG1 | solution | other |
| M3.S30.T30.C105.IMG2 | worked example | cell_grid |
| M3.S31.T31.C107.IMG1 | question | cell_grid |
| M3.S31.T31.C108.IMG1 | solution | cell_grid |
| M3.S31.T31.C109.IMG1 | question | cell_grid |
| M3.S31.T31.C110.IMG1 | solution | cell_grid |
| M3.S31.T31.C111.IMG1 | question | cell_grid |
| M3.S31.T31.C112.IMG1 | solution | cell_grid |
| M3.S31.T31.C113.IMG1 | question | cell_grid |
| M3.S31.T31.C114.IMG1 | solution | cell_grid |
| M3.S31.T31.C115.IMG1 | question | cell_grid |
| M3.S31.T31.C116.IMG1 | solution | cell_grid |
| M4.S32.T32.C117.IMG2 | worked example | dot_array |
| M4.S33.T33.C121.IMG1 | question | dot_array |
| M4.S33.T33.C122.IMG1 | solution | dot_array |
| M4.S33.T33.C123.IMG1 | question | dot_array |
| M4.S33.T33.C124.IMG1 | solution | dot_array |

### Chunk A notes (from the decision agent)
# Notes, chunk A (Class 5 Ch 4 "We the Travellers - II", topics M1.S2.T2 to M2.S13.T13)

Result: 17 units, 29 items. Required 8 (question 4, solution 4), optional 0, none 21 (worked 5, question 8, solution 8). Validator: errors 0, 4 warnings (the four solution diagrams of Making Sums Equal have no base figure, because the book prints no solution pictures).

## 1. Judgement calls

1. **Making Sums Equal (a) to (d), units M1.S3.T3.C5/C6, C7/C8, C9/C10, C11/C12: question required, solution required.**
   - Question: the book gives each puzzle as a figure (two groups of number cards with their sums) and the learner acts on it by interchanging cards (ACTION_ON_FIGURE, DATA_IN_FIGURE). The LP question text repeats the numbers, which is why this is Borderline (see section 4), but the figure is what the book question gives.
   - Solution: the answer is an arrangement, the two groups after the swap, with equal sums (ANSWER_IS_FIGURE). The LP steps only describe it in words (Step B2). Same decision for all four puzzles (sibling consistency).
   - The solution diagram is derived from the question diagram (same layout), changed cards and both sums in ANSWER green, plus an ANSWER double arrow joining the two swapped cards.
   - The figure carries the labels "Group 1" and "Group 2" above the columns. The book prints no such labels, but the question text names the groups and the LP solution says "group 1 is now ...", so they are category labels the figure needs. If the team does not want them, remove them from `visible_text` and the description.
   - (a) question diagram also carries the book's hint arrow joining the 2 of Group 1 and the 5 of Group 2 (it is printed in the book figure, and LP solution step 2 says "The hint swaps 2 and 5"). The red italic hint note is not drawn. The (a) solution diagram does not carry the hint arrow, because that swap is the wrong one; it shows the real swap, 2 and 3.
   - (b): the LP also names the swap of 7 and 11. Only the first swap (5 and 9) is drawn. (c) and (d): the LP gives a sample answer (two swaps); the figure draws the LP's own swaps (11/13 with 15/17, and 77/81 with 78/82). I recomputed all sums: 19/21, 39/47, 68/76, 314/330 before; 20/20, 43/43, 72/72, 322/322 after.
2. **Place-value (H-T-O, T-O) tables: none.** The book draws the lorry example (28 + 75), 49 + 89, the minibus subtraction (65 - 18) and 82 - 37 inside blue place-value tables with ovals, carries and struck digits. I treated these as LaTeX arithmetic and header boxes with digits (Step C: LATEX_ARITHMETIC, HEADER_BOXES_ONLY; "Not a diagram" list), because every carry and regroup is stated in the LP steps and a column addition or subtraction can be written as a LaTeX array. See Borderline.
3. **All worked examples (T2, T4, T7, T9, T13): none.** Practice values, all numbers in the text, the plan's own teaching image already shows each one (never linked). No book figure belongs to any of them except the T13 boxes (see 5).
4. **Questions that are only sums or fill-in-the-blanks** (Let Us Solve adding, Relationship Q1 and Q2, subtraction Q2 to 9): none, no book figure. Relationship Q2 has four dashed answer boxes in the book; they only hold the given sentence and blank lines, so I added `NEW-P03-answer_boxes-1` mapped to none:TEXT_SUFFICIENT.
5. **Base figures P04-number_boxes-1 and P04-pattern-1.** P04-number_boxes-1 (examples of consecutive numbers in four boxes) is none:NUMBER_LIST_IN_BOXES. P04-pattern-1 (the three boxes of sums of 2, 3 and 4 consecutive numbers) sits in the book section of my worked unit M2.S13.T13 (ncert ref cons.boxes) so I claimed it, as the teaching figure (`concept_image:M2.S13.T13.C35.IMG1`, accounting only). It is also the given figure of questions M2.S14.T14.C37 and C39 (chunk B, "in each of the boxes above"). A validator cannot let me map it to a chunk-B item, so at merge the item mapping from chunk B should win; if chunk B maps it to a question item, my entry for it should be dropped.
6. **Figure descriptions checked against the page pictures (pages 1 to 4):** all inventory entries of my chunk match the pictures; no CORRECTED entries needed.

## 2. LP text issues

- **M1.S2.T2.C3** (worked, step 5): "...group 1 becomes 18 and group 2 becomes 20, and the gap is still 2." The gap was 4 before this swap and is 2 after it, so "still" is wrong (checked: swapping 6 and 7 gives 2 + 7 + 9 = 18 and 4 + 6 + 10 = 20). Suggested sentence: "They differ by 1, so group 1 becomes 18 and group 2 becomes 20, and the gap is now 2, not 0."
- **M1.S3.T3.C5** (question text): omits the book's hint (an arrow between 2 and 5 and the note "Think what will happen to the sums if we interchange 2 and 5?"), but the solution C6 step 2 starts "The hint swaps 2 and 5". Suggested sentence to add to the question: "A hint arrow joins the 2 of group 1 and the 5 of group 2: think what happens to the sums if we interchange 2 and 5."
- **M1.S3.T3.C8** (`answer_tex` and the Answer line of `text`): broken LaTeX: `Swap $5$ and $9 ($or $7$ and $11)$: ...`. Suggested: "Swap $5$ and $9$ (or $7$ and $11$): both groups add up to $43$. This takes $1$ move."
- **M1.S3.T3.C10** (step 2): the list of pairs that differ by 2 is incomplete: "11 and 13, 15 and 17, 19 and 21, and 23 and 25" leaves out the pairs with the Group 2 number smaller. Suggested sentence: "The pairs that differ by $2$ are $11$ and $13$, $13$ and $15$, $15$ and $17$, $17$ and $19$, $19$ and $21$, $21$ and $23$, and $23$ and $25$. Every other pair differs by $6$ or more." (The conclusion, no pair differs by 4, is true: every difference is 2 plus a multiple of 4.)
- **M1.S10.T10.C28** (`answer_tex`): gives one sentence per part while the steps give two for (a) and (b) (two subtractions) and two for (c) and (d). Suggested: "Sample answer: $(a)$: $242 - 164 = 78$ and $242 - 78 = 164$; $(b)$: $1,301 - 839 = 462$ and $1,301 - 462 = 839$; $(c)$: $784 + 137 = 921$ and $921 - 784 = 137$; $(d)$: $590 + 234 = 824$ and $824 - 590 = 234$. Your answer may differ."
- **M1.S11.T11.C29** (`q_figure` hint only): says "A bar from 18 litres to 65 litres"; the book shows two boxes (18 l and 65 l) joined by a curved arrow. No diagram is made for this item, so only the hint is wrong.
- All other solution arithmetic in this chunk was recomputed and is correct (T4, T5 lorry 103, T6 138, T7 152 and 93, T8 six sums, T9, T10, T11 47, T12 45 and the eight differences, T13 33, 36, 39).

## 3. Where the book itself is unclear

- Page 3, the minibus table prints the note "Regroup, 1 Tens = 10 Ones" ("Tens" should be "Ten"); a print slip. No diagram of mine uses it.
- Page 2, the lorry table: the ones cell of the answer row reads a boxed, struck "1" followed by 3 (the regrouped 1 shown inside the answer row, answer 103). Print quirk, not drawn.
- Page 1 puzzle (a): the red curved arrow of the hint note ends at or just above the first box of Group 1 (inventory "unclear"); it carries no number and is not drawn.
- This pdf has no printed-solutions section; every solution diagram of this chunk follows the LP solution text.

## 4. Borderline

- **Making Sums Equal question side (units M1.S3.T3.C5, C7, C9, C11), required.** All numbers and sums are also in the LP question text, so a reviewer could call these none (TEXT_SUFFICIENT). I kept them required because the book gives the puzzle as a figure that the learner acts on and the solution figure is derived from it. If the team prefers text-only questions, set the four question items to none and make the four solution diagrams stand alone (`derived_from` null).
- **Place-value tables (units M1.S5.T5 solution C16, M1.S6.T6 C17 and C18, M1.S11.T11 solution C30, M1.S12.T12 C31 and C32), none.** The book prints regroup marks (circled carries, struck digits) which a reviewer could read as HIGHLIGHT_MEANING or "printed answer is a picture". I followed the explicit v3 rules (column addition and subtraction are LaTeX, header boxes with digits are not a diagram). These items are the first to become required if the team decides otherwise.
- **Minibus question (M1.S11.T11.C29), none.** The book's two boxes joined by a curved arrow with a question mark would be an optional model of "fuel filled = jump from 18 to 65"; the text carries both readings.
- **Worked example M1.S2.T2.C3, none.** A picture of two groups of cards with a swap would suit it, but all the numbers are in the text and the teaching image already shows it.

### Chunk B notes (from the decision agent)
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

### Chunk C notes (from the decision agent)
# Chunk C notes (Class 5 Ch 4, plan cbse_eng_maths5_ch4_v5)

Result: 32 items (15 pairs + 2 worked examples). Required 3, optional 0, none 29. Validator: errors 0, warnings 0.

Required (all three belong to the "Quick Sums and Differences" method picture of the book, p.11):
- M3.S26.T26.C86 solution (Sukanta, 32 + ___ = 100): the book's only worked answer is the picture 32 + 67 = 99, +1, 32 + 68 = 100. The question has no figure in the book, so no question diagram and `derived_from` is null.
- M3.S27.T27.C87 question (59 + ___ = 100): the book gives the same figure with two empty ovals to fill ("Try this method for the number 59").
- M3.S27.T27.C88 solution: the same figure with 40 and 41 in the ovals (ANSWER green), `derived_from` C87.IMG1.

All three use one layout: two column additions side by side, a joining arrow, and a +1 curved arrow from the left oval to the right oval (diagram_type `other`, spec complete, 16:9).

Inventory (base figures of this chunk): P10-route_diagram-1 -> none:TEXT_SUFFICIENT; P11-method_pair-1 -> C86 solution; P11-method_pair-2 -> C87 question. I added one NEW entry, `NEW-P11-method_pair-2-sol`, for the second use of the 59 figure (C88 solution). I checked all three base descriptions against the page pictures (p.10, p.11): accurate, no correction needed. The grids on p.12 and the table on p.15 are in the book sections near my units but belong to other chunks' units (grids = M3.S30/S31, table = M4.S42), so I did not claim them.

## Judgement calls

1. Colours of the method figure. The book draws the ovals and the +1 arc in lilac; FOCUS (#CC79A7) is the nearest token, so ovals, +1 arc and "+1" label are FOCUS in all three figures. Digits the solution adds are ANSWER green. In C86 (no question figure) the solution adds 67, 68 and 99; the top number 32 and the target 100 given in the question stay INK. In C87/C88 the book prints 99 and 100 in the question figure, so they stay INK (the question figure therefore shows "99", exactly as printed).
2. C85 (Sukanta question): none. The book prints only the equation on p.10; Piku's picture is on p.11 and answers it. A question with no given figure gets no question diagram.
3. C87 question is `required` (ACTION_ON_FIGURE, FIG_REFERENCED), although a student could do 59 + 41 from the text. The book gives the figure to be completed and says "Try this method", so the figure is the way to attempt it (user decision 4: not flipped to none).
4. C89-C96 (877/666/4,103/5,555; 180/760/400; subtract 9 or 99; get 9 or 99): none. The book prints no figure for them, only equations with blanks, and the answers are numbers. Sibling consistency with C87/C88: the book prints the method picture only for 32 (answer) and 59 (given), so this is a stated difference, not an oversight.
5. Journey/word problems (C71-C82), palindrome lists (C99-C104): none. Column arithmetic and lists stay LaTeX/text.
6. The old two-card solutions (C74, C76, C90, C92, C94, C104 each had IMG1 and IMG2) all become `drop_image`. Their `text` fields still hold two "[Image: ...]" markers each (one after a middle step, one "(continued)" after the answer); the builder must drop those markers.

## Borderline

- M2.S23.T23.C71 (Mary, question): the book gives a route sketch (Delhi top left, Varanasi, Kolkata bottom right, with 1,275 / 2,645 / 3,275). I chose none (TEXT_SUFFICIENT): every amount and the order of the trip are in the question text, no v3 trigger applies (no "in the figure", data not only in the picture). If the user wants the book figure, it would be a route line Kolkata -> Varanasi -> Delhi with the three spending amounts; ask and I will write the spec.
- M2.S23.T23.C72 (Mary, solution): none (LATEX_ARITHMETIC). A running-balance route (12,540 -> 9,265 -> 14,165 -> 11,520 -> 10,245) would be optional at best and only repeats the LaTeX lines.
- M3.S25.T25.C83 (worked example, Quick Sums and Differences with Round Numbers): none. The example is practice values (46 + ___, 358 + ___, 52 - 9, 215 - 99) with no figure in the book; two kept teaching images already show the method and are not linked (not the reason: no v3 trigger applies). It has the same kind of answer as C86, but the example has only one image slot and four parts, so one picture would be overcrowded.
- M3.S28.T28.C97 (worked example, palindromes): none. Reading 2,442 from both ends and listing 303, 313, 323, 333 is plain text.
- M3.S27.T27.C90 (877 + ___ ...): the digit-by-digit "make nine" pairing could be drawn, but the book gives no figure here and the answer is numbers only (see judgement call 4).
- M3.S27.T27.C94 (subtract 9 or 99): a number-line hop would help but is optional at most; the LP carries every step.

## LP text issues

- M3.S27.T27.C87 (question): "Try this method for the number 59." never says what the method is, and the ovals of the figure carry it. Suggested: "Use Piku's method: make 9 in each place, then add 1. Fill the two ovals. 59 + ___ = 100."
- M3.S27.T27.C89 (question): "Now, use this method to solve the following." names no method. Suggested: "Now, use the make-9-then-add-1 method to solve the following."
- M3.S27.T27.C95 (question): "Now, use the above solutions to find answers to the following problems. Do not calculate again." points at the answers of C93 without naming them. Suggested: "Use your answers to the question about taking away 9 or 99. Do not calculate again."
- M3.S27.T27.C96 (steps_tex, first step): broken math delimiters, `$9 ($or $99)$`. Suggested: "...so the blank is the first number minus $9$ (or minus $99$)." The same string should be checked in the `text` field.
- M3.S29.T29.C104 (steps_tex, first step): `$A 5$ digit number` has the letter A inside the math. Suggested: "A $5$ digit number between $25,000$ and $27,000$ ...".
- M3.S27.T27.C92 (steps_tex, step 4): "The last nine is 9, and adding 1 makes it carry." is unclear. Suggested: "The units digit 0 needs 9 to make 9, so the blank ends in 9, and adding 1 makes it carry."
- M3.S25.T25.C83 and M3.S28.T28.C97 (worked example question text): the learner-facing question ends with "(practice values)". Suggested: delete that bracket from the learner text (it is a note for the author).
- LP numbering differs from the book's: C71/C73/C75 are called Q1/Q2/Q3 in the LP but are book Q2/Q3/Q4 (p.10); C77/C79/C81 "Let us do Q1/Q2/Q3" are book Let Us Do Q3/Q4/Q5 (p.15). C85's book note says "blanks" in the book (one blank is printed). Only the labels differ; the questions match the book text.
- All LP answers were recomputed (Mary 10,245; council 68,878 and 1,622 left; truck 6,525 and 1,725; Ambrish 62,873 and 29,502 more; factory 31,300; Virat/Sachin 34,357; 32 + 68; 59 + 41; 123, 334, 5,897, 4,445; 820, 240, 600; 58, 74, 135, 88, 148, 664; 23, 47, 778, 567; palindromes 10 / 12 / 20). No arithmetic error found.

## Book unclear or noteworthy

- p.10 route figure of Mary: no arrowheads or start mark. The amounts at each stop are the spending of the leg that starts there (Kolkata 3,275 on the way to Varanasi; Varanasi 2,645 for the ticket to Delhi; Delhi 1,275 for souvenirs); the start 12,540 and the gift 4,900 are not drawn. A market photograph beside the figure is decoration (not inventoried).
- p.11 Piku figure (32): the book prints the "+1" arc, the ovals and the digits 67 and 68 in lilac and the sums in black; the digits are letter-spaced and "100" has three places, one to the left of the "+" column. The red note "Do you think this method will always work?" is not part of the figure and is excluded.
- The book has no printed-solutions section, so the only printed "answer" picture in this chunk is Piku's figure for 32.
- No print mistake (wrong digit, missing sign) found in this chunk's questions or figures.

### Chunk D notes (from the decision agent)
# Chunk D notes (Class 5 Ch 4 "We the Travellers - II", topics M3.S30.T30 to M4.S42.T42, book pdf pages 12 to 15)

Result: 22 units, 38 items. Required 16 (7 question, 7 solution, 2 worked example), optional 5, none 17. Validator: errors 0, 2 warnings (the two worked examples C105 and C117 have required diagrams that are not printed book figures: the LP's own 2 by 2 grids and its 14/15 counters).

All base figures of this chunk were checked against the page pictures (page_12 to page_15): P12-grid-1 to 5 (labels read from the picture and they match, including the three small grids), P13-dot_pairs-1 (9 + 9) and P13-dot_pairs-2 (12 + 11, the 12th top counter unpaired), P14-table-1 and P15-table-1. No base description needed a CORRECTED note. No figure was missing from the base. The pdf has no printed-solutions section, so every solution figure follows the LP sample answer (I recomputed every grid in code against its inc/dec labels).

## 1. Judgement calls

- Grids (C107 to C116): question side required for all five (ACTION_ON_FIGURE + DATA_IN_FIGURE: the learner fills the empty labelled grid the book prints), solution side required (ANSWER_IS_FIGURE, derived_from the question figure, numbers in ANSWER green). Same decision for all five (sibling consistency), also for the plain all-inc and all-dec grids where the LP text already names the conditions. Sample answers are the LP's (many grids work). I re-checked them: 1,2,3/4,5,6/7,8,9; 9,8,7/6,5,4/3,2,1; 3,2,1/6,5,4/9,8,7; 8,6,1/7,5,2/3,4,9; 1,6,8/2,5,7/9,4,3 all satisfy their labels.
- Worked example C105 (2 by 2 grids): required. The single diagram of a worked example sits after the question text, but the answer of the example is the pair of filled grids, so I draw the FINISHED state (labels INK, numbers ANSWER). A blank labelled pair would only repeat the kept teaching image. If you prefer the "given only" state (blank cells), say so.
- Worked example C117 (14 and 15 counters in pairs): required (the answer is an arrangement, described only in words). The picture draws 14 as 7 pairs and 15 as 7 pairs plus one ringed counter, with pair outlines in ANSWER.
- C121/C122 (add 2 to 18) and C123/C124 (add 2 to 23): question figure = the book picture (required, "Observe the given arrangement"), solution figure = the changed arrangement (20 counters 10/10; 25 counters 13/12), the two added counters in ANSWER green. For 23 the book does not say where the new counters go; I put the new pair in column 12 and the left-over counter (ringed, FOCUS) slides one place right to column 13, so "the same 1 counter is still left over" is visible. That is the only given part that moves between question and solution figure (render_note says so).
- The captions "Paired arrangement for 18/23" are not drawn (the LP question text carries them).
- Kept teaching images are never linked; items C105 and C117 get their own diagrams although a teaching image shows the same idea (user decision 5). No REUSES_CONCEPT_IMAGE anywhere.
- Figure inventory: the book picture is mapped to the question item, and the same picture drawn again for the solution is a second entry `NEW-<base id>-sol` mapped to the solution item (7 NEW entries). Counts: 16 figures, 14 to items, 2 none (the tables), 0 concept images.

## Borderline (v3 rules applied as written, listed so you can flip them)

- C119 (circle the even numbers): question none (a plain list of 12 lettered numbers, no figure in the book), solution optional (a picture of the 12 numbers with 498, 724, 100, 846 and 222 ringed would help, but the LP answer lists them). Not added.
- C125 (worked, join 14+8, 9+13, 7+10) and the solutions C128, C130, C132 (Q3 a, b, c: sums of even/odd numbers): optional. Reason: the book says only "you may use the paired arrangement"; a counter picture of one chosen pair would help the explanation, the answers are sums and a rule in text. The same decision for all four. Not added.
- C133 (coins worked example) and C135/C136 (Jincy's coins): none. The answers are coin sums in LaTeX and no coin figure is printed in the book. A coin-mat picture would be "nicer" only.
- Torch items C137, C139/C140, C141/C142: none (parity argument in words; the kept teaching image already shows presses 1 to 8).
- C143 (worked, reading tables): none; all the data is in the question text and the kept teaching images are not linked.
- C145 and C147 (the two tables): none with LATEX_TABLE (plain tables, no colour meaning; the blue header of P15 is decoration). BUT the LP question text does not contain either table, see LP text issues. I did not change the decision (decision 2); `needs_lp_text_sync` is true and `text_alternative` carries the array content.
- C146, C148: none (answers are subtractions in text/LaTeX).

## 2. LP text issues

- **M4.S41.T41.C145** (question): says "Read the table and answer the questions that follow" but the table is not in the question text or LaTeX (only the old card showed it). With the old card dropped the learner has no data. Suggested: add to the question text a LaTeX array with columns Mountain | Height (in metres) | Climbed in the year and these rows: Mount Kanchenjunga (India and Nepal border) 8,586 2022; Mount Everest (Nepal-China border) 8,848 2013; Mount Makalu (China-Nepal border) 8,485 2019; Mount Lhotse (Tibet-Nepal border) 8,516 2018; Mount Kilimanjaro (Africa) 5,895 2016; Mount Elbrus (Russia) 5,642 2017; Mount Annapurna I (Nepal) 8,091 2021.
- **M4.S42.T42.C147** (question): "For each district, find out if the number of certificates were sufficient?" has no table and no story (the book: a Math Metric Mela where certificates were printed per district). Suggested: "A Math Metric Mela was held and every student was to get a certificate. The table shows the certificates printed and the students who attended." plus a LaTeX array District | Certificates Printed | Students Attended with rows Chittoor, A.P. 18,225 18,104; Jaunpur, U.P. 19,043 19,265; Raigad, Maharashtra 20,863 19,974.
- **M3.S31.T31.C109** (question): "This time, fill the grid such that each row and column has numbers in decreasing (dec) order." has no "3 by 3" and no "numbers 1 to 9, each once" (it relies on the previous question). Suggested: "In a $3 \times 3$ grid, arrange the numbers $1$ to $9$ such that each row and each column has numbers in a decreasing (dec) order. Each number should be used only once."
- **M4.S33.T33.C119** (question) and **C120** (steps): items (a) to (h) are written `$(a)$` but (i), (j), (k), (l) are plain "(i)"; make them `$(i)$`, `$(j)$`, `$(k)$`, `$(l)$` (also in C120's answer_tex for "(i): $846$").
- **M4.S33.T33.C124** (step 1): "(a row of $12$ and a row of $11)$" has the closing bracket inside the math; suggested "(a row of $12$ and a row of $11$)".
- **M4.S33.T33.C121 and C123** (question): the sentence "Paired arrangement for $18$" is the book's picture caption and reads as a loose phrase once the picture is a separate figure. Suggested: "The picture shows $18$ counters in two rows of $9$, each counter paired with the one below it." (and "twelve counters above eleven, the last top counter has no partner" for 23).
- Naming only (not read by the learner): concept names "Let Us Think and Solve (grids): Q1 to Q5" are the five grids of book Q2 (the book's Q1 is the palindrome question, topic T28); "Even and Odd Numbers: Q2/Q3" (T33) are the 18 and the 23 picture of book Q2; "Q1 to Q3" in T35 are book Q3 (a), (b), (c); "Let Us Think: Q1/Q2" in T37/T39 are book Let Us Think Q1 and Q2; T41 "Q1" is book Q3 (Mountain climbing).

LP maths I re-checked and found right: the 11 combinations of Jincy's coins (4 + 5 + 2, total 51 rupees available, 38 payable), the 4 ways of the coin worked example, all subtraction answers in C143, C146 and C148, the parity sample sums in C128, C130 and C132.

## 3. Places where the book is unclear

- Page 12: the pdf text layer lists the labels of the three small grids in a scrambled order; I took the labels from the picture (grid 3: rows dec, dec, dec / columns inc, inc, inc; grid 4: rows dec, dec, inc / columns dec, dec, inc; grid 5: rows inc, inc, dec / columns inc, dec, dec). The book says "numbers (1 to 9)" for the small grids and "each number only once" only in the first sentence; I read it as applying to all.
- Page 12 grids: "each row and column has numbers in increasing order" is read as rows left to right and columns top to bottom (the LP does the same). Many fillings are correct; the diagrams draw the LP's sample.
- Page 13, Q2: the book does not say where the 2 added counters go. Drawn as described above (new pair at the end of the old pairs).
- Page 13, Q1: the book prints no answer; no printed-solutions section exists in this pdf.
