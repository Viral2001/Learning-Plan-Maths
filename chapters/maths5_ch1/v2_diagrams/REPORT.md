# Class 5 Ch 1 We the Travellers - I - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths5_ch1` v6 (taken from staging). Result: new V2 version v7 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (117 items from 72 units)
{"worked_example": {"none": 25, "required": 2}, "question": {"none": 34, "required": 10, "optional": 1}, "solution": {"none": 32, "required": 10, "optional": 3}}

Optional, NOT added: [('C84', 'solution'), ('C94', 'solution'), ('C116', 'solution'), ('C117', 'question')]

needs_lp_text_sync: []

## The 22 diagrams
| id | side | type |
|---|---|---|
| M1.S6.T6.C13.IMG1 | question | place_value_model |
| M1.S6.T6.C15.IMG1 | question | place_value_model |
| M2.S12.T12.C34.IMG2 | worked example | number_line |
| M2.S13.T13.C37.IMG1 | question | number_line |
| M2.S13.T13.C38.IMG1 | solution | number_line |
| M2.S13.T13.C39.IMG1 | question | number_line |
| M2.S13.T13.C40.IMG1 | solution | number_line |
| M2.S19.T19.C75.IMG1 | question | number_line |
| M2.S19.T19.C76.IMG1 | solution | number_line |
| M2.S20.T20.C77.IMG1 | question | number_line |
| M2.S20.T20.C78.IMG1 | solution | number_line |
| M2.S20.T20.C79.IMG1 | question | number_line |
| M2.S20.T20.C80.IMG1 | solution | number_line |
| M3.S28.T28.C114.IMG1 | solution | other |
| M3.S29.T29.C124.IMG1 | solution | other |
| M3.S30.T30.C125.IMG2 | worked example | dot_array |
| M3.S31.T31.C127.IMG1 | question | dot_array |
| M3.S31.T31.C128.IMG1 | solution | dot_array |
| M3.S31.T31.C129.IMG1 | question | dot_array |
| M3.S31.T31.C130.IMG1 | solution | dot_array |
| M3.S31.T31.C131.IMG1 | question | dot_array |
| M3.S31.T31.C132.IMG1 | solution | dot_array |

### Chunk A notes (from the decision agent)
# Notes, chunk A (We the Travellers - I, topics M1.S2.T2 to M2.S12.T12)

Result: 20 units, 28 items. Required 3, optional 0, none 25. Validator: errors 0, one warning (C34 has no printed book figure, expected).
Required: question diagram of C13 (token rows 1 and 2), question diagram of C15 (token rows a to d), worked-example diagram of C34 (number line with four numbers placed).
Figure inventory: 18 base figures claimed (2 to items, 2 to concept images, 14 none). Figures of pp.6-7 that belong to the comparing questions (number cards, number lines, Q4 chart) are not mine (chunk B).

## 1. Judgement calls

- **Token tables, C13 and C15 (question required, solution none).** The book gives the rows as token pictures; the learner counts tokens. Triggers DATA_IN_FIGURE and ACTION_ON_FIGURE. The token counts of C13 row 2 and of C15 (b), (c), (d) are in the picture only (the LP text gives them for C15 (a) only), and the LP solutions work from them ("Check with the tokens", "Two 10,000 tokens make 20,000"). I drew the tokens only, not the whole table: the Number, TTh to O and Number Name cells are a plain table of digits and words (LATEX_TABLE, HEADER_BOXES_ONLY), so the solution (C14, C16) only fills those cells and would repeat the question figure: none, SAME_AS_QUESTION_DIAGRAM. Row labels: numerals 1, 2 in circles (C13, the LP says "Row 1/Row 2") and letters (a) to (d) (C15, the LP answer uses them; the book prints no letters on the rows). Chips use one neutral fill (CELL_FILL) with the printed value, not the book's place colours, to stay in the house palette. Layout rule: tokens of one value form a block, blocks run 10,000 -> 1, two chips per line; C15 (d) has 30 tokens and fits the card (912 px of 1080).
- **Number-line worked example C34 (required).** The example itself says "place ... on a number line with the marks 0 ... 40,000" (place on a line), so it needs its own picture; the teaching image 'Numbers on a number line' is never linked (v3). The figure shows the finished placement (four ANSWER-green points, to scale, 1 px = 25 units), because a worked example's figure is the picture the example needs and its steps follow at once. The id is C34.IMG2 because C34.IMG1 is the kept teaching image.
- **Sequences with blanks (Let Us Do Q1 a to i, C27 to C32; counting strip C8/C9): none.** Number chains: LATEX_ARITHMETIC (Step C: "sequences, number chains") and the brief ("sequences stay text/LaTeX"). Every given value and every blank position is stated in the LP question text; no shading, colour or arrow carries meaning; the 10-box snake of (d) to (i) is only layout. `text_alternative` gives the LaTeX line for each. The jump-arrow chain the old cards showed would be the optional figure, not added.
- **Number | Number Name table of Let Us Do Q2 (C17/C18, C22/C23): none.** Plain two-column table: LATEX_TABLE. One base figure (P06-table-1) serves both pairs: one entry, none.
- **Worked examples C3, C5, C6, C10, C11, C19, C20, C24, C25, C33, C35: none.** Reading or writing a number from its digit chart (header boxes with digits: HEADER_BOXES_ONLY), adding 1,000s, patterns by differences (LATEX_ARITHMETIC), digit and length comparison (TEXT_SUFFICIENT). Each already has a teaching image in the plan (never linked). C35 is open (many answers are right), so none.
- **Teaching figures.** P02-table-1 mapped to concept image C6.IMG1 (it carries the TTh column and the x10 arrows; not an identical picture, accounting only). P02-tokens-3 to C5.IMG1 (same picture). P02-base_ten_blocks-2, P02-tokens-4 (1,380), P02-tokens-5 (9,123): none, TEXT_SUFFICIENT, because no question, solution or worked example uses them and the sentence above each carries the content.
- **p.1 art.** The three opening pictures (bullock cart, cyclist, traffic jam) are decoration (Step 0 skips them) and were not inventoried by the base; I made no NEW- entry for them.
- **Token counts re-checked on the page pictures** (p.3 rows 5 and 6, p.4 rows 1 to 4): they agree with the base inventory and with the LP solutions (11,214, 13,520, 20,000, 45,867, 10,033, 10,458).

## 2. LP text issues

- **M1.S6.T6.C13** (question): says "Fill in the token table" but there is no table in the text, and the tokens of Row 2 are not stated (only its number 10,458), although the solution's last step checks "with the tokens". Suggested sentence: "Fill in the token table, one row at a time. Row 1: the tokens are one 10,000, three 10s and three 1s. Row 2: the tokens are one 10,000, four 100s, five 10s and eight 1s. For each row write the number and its digits under TTh, Th, H, T, O." (The new diagram shows the tokens, so the sentence is optional but removes the hidden dependency.)
- **M1.S6.T6.C15** (question): the token counts of (b), (c), (d) are not stated; (a) is. Suggested: "(b) one 10,000, three 1,000s, five 100s and two 10s; (c) two 10,000s; (d) four 10,000s, five 1,000s, eight 100s, six 10s and seven 1s." Same remark about the missing table.
- **M1.S7.T7.C17 / C18 and M1.S9.T9.C22 / C23** (Let Us Do Q2): the book's table starts with two finished example rows, 8,045 = Eight thousand forty-five and 20,869 = Twenty thousand eight hundred sixty-nine, which the LP omits. Suggested: "For example, 8,045 is Eight thousand forty-five and 20,869 is Twenty thousand eight hundred sixty-nine."
- **M1.S11.T11.C31 / C32:** the letter "(i)" is not in math mode while "(h)" is `$(h)$` (question_tex of C31, steps_tex and answer_tex of C32). Suggested: write `$(i)$`.
- **M1.S4.T4.C8** `q_figure` hint says the boxes are "joined by arrows"; the book strip has no arrows (hint only, no effect now).
- **Old image markers:** the `text` field of every solution concept of this chunk (C9, C14, C16, C18, C23, C28, C30; C32 has none mid-text) still carries `[Image: ... solution]` lines in the middle of the steps and `(continued)` at the end, and the plan has old cards C9.IMG1/IMG2, C14.IMG1/IMG2 and so on. All 8 solutions here are none, so these cards and markers must be dropped (builder, `drop_image`); the new tokens are only C13.IMG1, C15.IMG1 (question side) and C34.IMG2.
- No contradiction found between an LP solution and the book; all LP arithmetic (names, sequences, token sums) was recomputed and is right.

## 3. Book unclear

- p.1: the 9-box strip has no arrows (LP hint says it has).
- p.2: the x10 arrows sit over TTh, Th, H, T and curve left; the page does not say what they connect (read as "one place to the right times 10").
- p.3 row 2: the two 1 tokens are coloured like 100 tokens (a drawing slip, value 1); this row is a teaching row and is not drawn.
- p.3: "You can use the tokens given in the end of the book" (not in this pdf).
- p.6: the two finished rows of the Q2 table are examples but are not labelled as such.
- p.5 (d): 10,900 sits in the 9th box (second box of row 2 running right to left), which agrees with the LP ("five empty boxes, 10,900 and one more empty box").

## Borderline

- Sequences with blanks (C8/C9, C27 to C32, 8 items): none by the explicit "sequences stay text/LaTeX" rule, although the book draws boxes. If you want them drawn, the figure would be an `arrow_map` chain (boxes with the given values, blanks, jump arcs in the solution).
- Token tables: question required, solution none. If you prefer the whole table as the figure (question with the given cells, solution with the filled cells in green), C14 and C16 would become required; I kept tokens only because the digit and name cells are a plain table.
- C34 required (number line with the four numbers placed, shown before the steps); the alternative is none with the steps in text.
- Place-value digit charts in worked examples (C6, C10, C11, C19, C20, C33): none (HEADER_BOXES_ONLY), although each has a coloured teaching image in the plan (never linked).
- C35 none (open answer); a number line with sample numbers would be the optional picture.

### Chunk B notes (from the decision agent)
# Chunk B notes: Class 5 Ch 1 "We the Travellers - I" (cbse_eng_maths5_ch1_v6)

Topics: M2.S13.T13, M2.S14.T14, M2.S15.T15, M2.S16.T16, M2.S17.T17 (18 units, 32 items).
Result: required 4 (C37 q, C38 sol, C39 q, C40 sol), optional 0, none 28. Validator: errors 0, warnings 0.
Output: `map/out_B.json`. Figures: 11 inventory entries (8 to items, 3 none, 0 concept images).

## What was drawn and why

Only two book questions of this chunk give a figure the learner works on:

- **Let Us Do Q3 (C37 / C38)**: eight number cards plus the 0 to 80,000 number line (base figures P06-number_cards-2 and P06-number_line-3, one combined diagram). The solution places the eight numbers on the line (LP step 7), so the solution figure shows the cards in increasing order, each joined to its exact scaled position.
- **Let Us Do Q4 (C39 / C40)**: ten-tick number line with seven blank label boxes plus the place value chart for 9,990 and 49,014 (P07-number_line-1, P07-table-2, one combined diagram). The solution fills the seven boxes (15,000 to 45,000), marks 9,990 and 49,014 on the line and outlines the empty TTh cell.

Every other item in the chunk has no figure in the book (plain word questions, fill-in lines, arithmetic) or only a plain table / a text note, so it stays text or LaTeX. The four worked examples (C53, C54, C58, C59) have no book figure; their numbers are all in the text and each already has a teaching image (not linked).

## Judgement calls

- **C37 question required.** The numbers are all in the text and the book says the number line is optional ("if required"), but the LP text says "use the number line below" and the scale (0 to 80,000, 20,000 a tick) exists only in the figure. Treated as FIG_REFERENCED + DATA_IN_FIGURE, same as the sibling Q4 (which must be a figure). Cards are drawn too because the book draws them as part of the figure.
- **C38 solution required.** The answer itself is a list, but LP step 7 and the LP's own `s_figure` place the eight numbers on the line. I drew the cards in the answer order (the arrangement is the answer, so they change slot) and joined them to the line with non-crossing ANSWER lines. Given parts (line, ticks, labels, slot positions) are unchanged.
- **C48 and C50 (other ordering answers) none.** Same answer type as C38 (ordered list) but the question gives no number line to place the numbers on, so sibling consistency is explained in the reasons.
- **C42 and C44 none (not optional).** Sample answers to "write 5 numbers between ..."; text carries it. A number line with the two bounds and the five numbers would be a pleasant extra, not needed.
- **C49 / C50 none (LATEX_TABLE).** P14-table-1 is a plain table with a blue header; no colour meaning. Question and solution both stay text; `text_alternative` gives the LaTeX array rows.
- **C57 none.** Five sub-parts and nine answer numbers; one picture per part would be five figures and every swap is already in the steps.
- **C64, C68 none.** The book's red hint notes ("90 Tens is 900, so remaining 83 will be Ones", "3 Tens is 30, 90 Tens in 900, and 700 Tens in 7000") are text with an arrow, no drawing (mapped none:TEXT_SUFFICIENT).
- **One diagram holds both book pictures** for Q3 and for Q4 (the pair gets one question and one solution diagram).
- **Dots on the Q3 solution line.** 34,407/34,740 are only 6.75 px apart and 40,347/40,473 only 2.55 px apart on a 1,620 px line, so their dots touch. I kept every dot at its exact scale position (to_scale true) and let the card-to-dot lines carry the distinction. If the renderer finds this too crowded, the alternative is to enlarge the line, not to move dots.
- **Dots on the Q4 solution line.** 9,990 is 0.32 px left of the 10,000 tick when to scale, so the dot covers the tick; 49,014 is 31.55 px left of the 50,000 tick. Both dots labelled above with a pointer line.
- **Figure letters.** None of my figures is lettered; the Q5 digit-swap parts and Q8/Q9 parts (a) to (h) have no figure, so no letters are drawn.

## Borderline

1. C37 question: required, though the numbers are in the text and the line is "if required" (see above). Alternative reading: none with TEXT_SUFFICIENT.
2. C38 solution: required, though the answer is a text list. Alternative reading: none.
3. C42 / C44: none; optional number line possible.
4. C57: none; optional digit-swap arrows possible.
5. C48 / C50: none while C38 is required (explained by whether the question gives a line to place numbers on).
6. Worked examples C53, C54, C58, C59: none (teaching images already cover them; never linked).

## LP text issues

- **M2.S13.T13.C49 (question) and C50 (solution).** The question says "The following table shows the population of some towns" but the table is only written inline ("Town 1: 65,232, Town 2: ..."); there is no table. Suggested: add a LaTeX table after the question sentence: columns Town, Population; rows Town 1 65,232; Town 2 53,231; Town 3 56,380; Town 4 51,336; Town 5 45,858; Town 6 66,540. In the solution, an ordered table or the existing sentence is fine.
- **M2.S17.T17.C68 (solution, step (a)).** The book's note "3 Tens is 30, 90 Tens in 900, and 700 Tens in 7000" is not in the LP. Suggested sentence for step (a): "793 Tens is 700 Tens + 90 Tens + 3 Tens, which is 7,000 + 900 + 30 = 7,930, so 793 notes of ₹10 make ₹7,930."
- **M2.S17.T17.C62, C64, C68, step 1.** The text "(a): is done: ..." reads awkwardly. Suggested: "(a) is already done for you: ...". Same in C64 step 1 ("(a): is done: 90 Tens is 900 ...") and C68 step 1.
- **Numbering.** Concept names restart at "Let us do: Q1 / Ans1" in T13, T15 and T17, but the book numbers are different (T13: book Q3, Q4 of the first set and Q1 to Q6 of the second set; T17: book Q7, Q8, Q9). The `book_number` field carries the right numbers; the names only matter if learners see them.
- **M2.S13.T13.C37 (question).** The text says "the numbers below" and "the number line below"; both exist only in the figure (the number line) or the text (the numbers). Nothing to change if the diagram is built; if it were dropped, the scale 0 to 80,000 would have to be written in the text.

## Book is unclear or has a slip

- Page 15, hint under Q9(d): the book prints "(Hint: Observe the answer of (iii))" but the parts are lettered (a) to (h); (c) is meant. The LP already says (c). No diagram uses it.
- Page 6, Q3: a thin horizontal rule below the number line is a page rule, not part of the figure (not drawn).
- Page 14, Q6 prints "all 0? ." (stray punctuation after the blank line). Text only.
- Page 7, Q4: the line has arrowheads at both ends but no 0; the first mark is 5,000 and marks are 5,000 apart, consistent with the labels 10,000 and 50,000 (tick 10 = 50,000). No contradiction. The red italic note and arrow beside the chart ("You can use this place value chart to compare the numbers") are instruction text and are not drawn.
- The base descriptions of all eleven figures of this chunk were checked against the page pictures (pages 6, 7, 14, 15) and are correct; none needed "CORRECTED:". The inventory has no entry for the bold price line of Q6 (page 13) and the green worked line "700 + 80 + 3" of Q7 (page 14); both are plain text, not figures, so no NEW- figure was added for them.

## Figure accounting

- P06-number_cards-2, P06-number_line-3 -> item C37 (question); second use in the solution -> NEW-P06-number_cards-2-sol, NEW-P06-number_line-3-sol -> item C38 (solution).
- P07-number_line-1, P07-table-2 -> item C39 (question); second use -> NEW-P07-number_line-1-sol, NEW-P07-table-2-sol -> item C40 (solution).
- P14-table-1 -> none:LATEX_TABLE (C49 and C50). P14-callout-2 -> none:TEXT_SUFFICIENT (C63/C64). P15-callout-1 -> none:TEXT_SUFFICIENT (C67/C68).
- Not in my chunk (left to others): P05 sequences, P06-table-1, P07-number_line-3, P08 figures, P11 to P13 puzzle figures, P15-dot_pattern-2, P16 frames.

### Chunk C notes (from the decision agent)
# Notes for chunk C (Class 5 Ch 1, topics T18 to T25)

Result: 29 items = required 6 / optional 2 / none 21. Question: 3 required, 8 none. Solution: 3 required, 2 optional, 6 none. Worked example: 7 none. Validator: errors 0, warnings 0. Output: `map/out_C.json`.

The only drawn figures are the three rabbit roads of the book (tens p.7, hundreds p.8, thousands p.8), each as a question road (C75, C77, C79) and a solution road with jump arrows (C76, C78, C80).

## 1. Judgement calls

- **C75, C77, C79 (rabbit questions) question = required.** The book hands these over as pictures ("Its location is given in the pictures below"): the carrots, the halfway tick (2,345 / 2,350 / 2,500) and the rabbit's exact spot live in the road figure. The LP question text repeats the two end numbers, but under the user's rule 4 I did not flip them to none for that. Positions are drawn to scale (checked on the page pictures: 2,346 at 60% / 46% / 34.6% of the road, the halfway tick at 50%).
- **Rabbit pose.** In the book the rabbit is drawn mid-jump facing the nearer carrot (right on p.7, left on both p.8 roads). A question figure must not give the answer, so the question figures draw it standing and facing front with no motion lines. The solution figure keeps the same rabbit and adds the arrows. The rabbit and the carrots are plain flat icons without faces: they are the question's own objects (the rabbit's position is the data). If you want an even plainer figure (a dot instead of a rabbit), that is a one-line change in the three question specs and the three derived solution specs.
- **C76, C78, C80 (rabbit solutions) = required.** The LP solution compares both jump counts (4 and 6; 46 and 54; 346 and 654). The figure adds new marks (two jump arrows with counts, a ring round the nearest carrot, the tag "nearest ten / hundred / thousand"), which is the "solution adds something visual: new marks, a highlighted part" case of Step E. All three have `derived_from` their question figure; the tags use only words the LP solution uses ("jumps", "nearest ten").
- **C71, C72, C73 (T18 worked examples) = none.** Their questions name no figure and give every number in words (4,190 / 4,200 and 3 / 7 jumps; 6,700 / 6,800 / 6,000 / 7,000; the two sample pairs), and each concept already carries a teaching image of the same road (not linked). A text-complete worked example gets no diagram of its own (no repetition). Same logic for C89, C90, C91 and C99.
- **C81 / C82 (the table) = none, LATEX_TABLE both sides.** Plain four-column table of numbers with no colour or position meaning; the filled answer is the same table with 12 numbers. B2 lists "filled table" under ANSWER_IS_FIGURE, but the explicit rule for plain tables ("Plain tables of numbers ... stay LaTeX") is more specific, so I followed it. See Borderline.
- **C83 question none / C84 solution optional.** The four numbers of Let Us Think Q1 are a plain list to choose from (NUMBER_LIST_IN_BOXES). The rule says the circles in the answer only make an optional figure when the text already gives the answer, and the LP answer names 7,030 and 6,999. Optional, so no image is added.
- **C85/C86 and C87/C88 (Let Us Think Q2, Q3) = none.** Open "think and write" tasks; the LP sample answers are pairs of numbers fully stated in the steps. Number lines would be nicer, but they are not needed (Q2 would need three scales). Q2 and Q3 have the same decision as each other. Q1's solution is optional because its answer is a selection from a printed list, a different kind of answer.
- **C93 to C102 (Let Us Do vehicles, books).** The book prints no figure for the cyclist, the school-bus question or the 200-page book (page 10 is text only). So the three question sides are none and no question figure is invented, although the LP hint `q_figure` describes one. Solutions: C94 (cyclist) optional (a 0 to 60 km line with four 15 km hops would help but the sum is already complete), C96 / C98 / C102 none (division and multiplication; 450 groups of 2 cannot be drawn faithfully).
- **Figure inventory.** Base figures P07-number_line-3, P08-number_line-1, P08-number_line-2 are the question figures of C75, C77, C79. For each solution figure I added `NEW-<base id>-sol` (second use of the same road). P08-table-3 is `none:LATEX_TABLE`; P08-number_list-4 is `none:NUMBER_LIST_IN_BOXES`. I added `NEW-P09-vehicles-1` (the page-9 collage of eight vehicles, missing from the base because it is decoration) mapped to the teaching image `M3.S22.T22.C89.IMG1`, which shows the same eight modes. I checked the base descriptions of the five base figures against the page pictures: all correct.

## 2. LP text issues

(Nothing was edited and no decision was changed because of these.)

- **M2.S20.T20.C81**: the question text says "Fill in the boxes appropriately" but carries no table, so there are no boxes to fill. Suggested: add a LaTeX array to the question text, header `Number | Nearest Tens | Nearest Hundreds | Nearest Thousands`, rows 3,176; 4,017; 5,789; 8,203, three blank cells each.
- **M2.S20.T20.C82**: the answer is one run of text (12 numbers). Suggested: show it as the same LaTeX array filled in (3,176: 3,180 / 3,200 / 3,000; 4,017: 4,020 / 4,000 / 4,000; 5,789: 5,790 / 5,800 / 6,000; 8,203: 8,200 / 8,200 / 8,000).
- **M2.S19.T19.C75, M2.S20.T20.C77, M2.S20.T20.C79**: the question text never points at the road figure that is now added. Suggested closing sentence: "Look at the road in the picture: the rabbit and the two carrots." (The figure also shows the halfway tick, which the text does not mention.)
- **M3.S23.T23.C93, C95, C97 and M3.S25.T25.C101** carry `q_figure` hints (a road with four stretches, a school group beside four vehicles, an open book with labels) and C94 / C96 / C98 / C102 carry `s_figure` hints that are not figures of the book. Not used.
- **M3.S23.T23.C97** is named "Let us do: Q3" in the LP but is part (e) to (h) of the book's Let Us Do Q2 (book_number is right). Cosmetic.
- **M2.S21.T21.C88 (b)**: "7,970 is 70 jumps from 7,900" states the distance to the farther neighbour (7,970 is only 30 jumps from 8,000); the conclusion (nearest hundred 8,000) is right. Suggested: add "and 30 jumps from 8,000" for clarity.
- All sums, counts and answers of the 29 items were recomputed (4,197, 6,731, 5,380 / 5,420, 7,997 / 8,002; 46 / 54; 346 / 654; the 12-cell table; 7,126 / 7,835 / 7,030 / 6,999; the sample pairs of Q2 and Q3; 15 x 4; 461 + 439 = 900 and the eight divisions; 120 / 4 and 120 / 6; 100 x 40; 200 x 50): no arithmetic mistake found. No book print slip was found in this chunk, so nothing had to be corrected in a spec.

## 3. Where the book is unclear

- The book prints no solutions section; the printed text under the Example 1 picture (p.7) gives "2,350 ... 4 jumps" and the two p.8 rabbit items are blanks only. The LP solution (46 / 54 and 346 / 654) is mathematically right and is followed.
- The p.8 hundreds picture puts the 2,346 label higher than the others because 2,346 and 2,350 are only 4 units (58 px at this scale) apart; the spec keeps that staggered layout.
- Page 10 prints the speed list and the vehicle seat list as plain text; there is no figure, so the concept images of T22 and T24 are accounted for as teaching images only.

## Borderline

- **C76 / C78 / C80 solutions required**: the answer is words and numbers, but the jump arrows with the ring are exactly the added visual of Step E. Typical-pair table (Step E) would also allow "Q required, S none". I chose required because the arrows are what "jumps" means in the book and the LP solution is built on them.
- **C71 / C72 / C73 worked examples none**: the same rabbit scene is a required figure in T19 / T20, but there the book gives it as the question; here the LP wrote the examples in words and each concept already has its teaching image. Could be flipped if the content team wants a figure on every rabbit example.
- **C81 / C82 table none**: the "filled table" wording of ANSWER_IS_FIGURE versus the plain-table rule.
- **C84 optional, C94 optional, C86 / C88 none**: the picture would help a little in each, none is needed.
- **Rabbit and carrot icons** in a diagram image (the "no clip-art" rule): kept as plain flat icons because they are the objects of the question; the must_not_show list says so.

### Chunk D notes (from the decision agent)
# Notes, chunk D (topics M3.S26.T26 to M3.S31.T31)

Result: 28 items = required 9 (question 3, solution 5, worked example 1), optional 2, none 17. Validator: errors 0, warnings 5.
The 5 warnings are required items whose figure is not printed in the book (C114, C125, C128, C130, C132): expected.

Required (media ids):
- M3.S28.T28.C114 solution: river crossing, 8 panels (Start, Trip 1 to Trip 7). No question diagram, so it stands alone.
- M3.S29.T29.C124 solution: Mira's chain 73-37, 63-36, 72-27, 54-45 (the book's printed answer picture). No question diagram, stands alone.
- M3.S30.T30.C125 worked example (IMG2, IMG1 is the kept teaching image): 12 children around a square, corners shaded.
- M3.S31.T31.C127 question (book's stable with 19 horses) and C128 solution (derived: 5 on each side, corner horse circled, 19 horses).
- M3.S31.T31.C129 question (empty stable) and C130 solution (derived: 18 horses).
- M3.S31.T31.C131 question (empty stable, identical to C129's) and C132 solution (derived: 16 horses).

Optional (not added): C116 solution (strip of pebble piles), C117 question (the chain picture the book calls "each step above").

I checked every base-inventory figure of this chunk against the page pictures (pages 11, 12, 13, 15, 16): all descriptions are right (7 pebbles per stack, the stable's 19 horses and side sums 5/5/5/5, the table's four rows, the four subtractions, the two empty frames). The only `unclear` entry (P11, boat in the middle of the river) does not matter for any decision. The decorative train picture on page 11 (Sanju, Mira and an adult) is not in the base and carries no mathematics, so I added no entry.

## Borderline

- **C125 worked example, required (SPATIAL_GEOMETRY, HIGHLIGHT_MEANING).** The text gives every number, so a text-only reading is possible. I kept it required because the lesson (a corner child stands on two sides, so the side counts add to 16, not 12) is about where 12 children stand around a square; the learner has to see the ring and its corners. The figure shows only what the question gives (no 4, 12 or 16, no brackets). If you want it dropped, set it to `none` with TEXT_SUFFICIENT; nothing else depends on it.
- **C114 solution, required (ANSWER_IS_FIGURE, DATA_IN_FIGURE).** The LP answer is a list of seven trips in words. I treated it as an arrangement answer (B2): who is on which bank after each trip, and that the boatman is never away from a lion-and-sheep or sheep-and-grass pair, is what the picture shows. Sibling check against the pebble game (C116, optional): there the states are two numbers already written as numbers, here they are who stands where.
- **C124 solution, required (printed answer is a picture).** The LP steps carry every number, but the book prints the answer to Example 1 as the four-column chain (P12-subtraction_chain-3), so B2 makes it required. Per decision 4 not flipped to none.
- **C111 worked example (same chain for 2 and 5), none (LATEX_ARITHMETIC, REUSES_CONCEPT_IMAGE).** The book prints no picture for 2 and 5, and the same chain is already the kept teaching image of that concept, so it was not drawn. If sibling consistency with C124 is wanted, C111 could be made required with the same layout (digits 2, 5: 52-25=27, 72-27=45, 54-45=9).
- **C109, C110 worked examples, none.** Reasoning about pairs / moves on piles, all in the words; C110's game-state flow is already the kept teaching image.
- **C113 question and C115 question, none (DECORATIVE_ONLY) although the book has a picture.** The river scene and the two stacks of pebbles only illustrate numbers and rules the question states in words. The river scene is the same as teaching image C109.IMG1 (accounting only, never linked).
- **C119 question and C120 solution, none (LATEX_TABLE) although C120's answer is a filled table.** Plain numbers, headings, no colour meaning: LaTeX array (brief: plain tables stay LaTeX). The earlier hint that the book table has four empty rows is wrong: the book prints four filled rows only.
- **C117 question, optional.** The book says "each step above" (the 3-and-7 chain); the LP text already lists 36, 27, 45 and 9, so the question can be attempted without the picture. The chain is drawn once, as C124's solution figure.
- **C129 and C131 questions, required (ACTION_ON_FIGURE).** The empty stable is what the book gives for arranging horses; the 12-stall structure (4+4+2+2, corners shared) is not stated in the text. The book prints two identical frames on page 16; each question gets one, with the same spec (C131 says "same as C129").
- **C123 question, none.** The book's picture P12-steps-2 is the three steps joined to the example by arrows; every word is in the LP question text.
- **C103 to C108, C118, C121, C122:** open or arithmetic-only, none.

## Judgement calls

- **P15 stable counted twice.** The base figure P15-dot_pattern-2 is the picture of the question C127 (becomes its diagram) and also the story picture that exists as teaching image C125.IMG1. Base id maps to `item:M3.S31.T31.C127 (question)`; the teaching use is accounted as `NEW-P15-dot_pattern-2-teaching` -> `concept_image:M3.S30.T30.C125.IMG1`. Nothing is linked to the teaching image.
- **P11 river scene** maps to `concept_image:M3.S27.T27.C109.IMG1` (same scene, already a teaching image); C113 itself is none.
- **C114 strip.** The earlier hint said seven pictures; I added a Start panel (the LP says "At the start ...") so the eight panels read as a complete sequence. Labels used are only words the LP uses: Start, Trip 1 ... Trip 7, lion, sheep, grass, boatman. Left bank = near bank, right bank = far bank (by the Start panel); no bank names are drawn. The outlined chip (FOCUS) is who crossed in that trip; Trip 2 and Trip 6 outline the boatman (crosses alone). All 8 states were checked in code (no unsafe pair left without the boatman).
- **C124 colours.** Column 1 (73 - 37 = 36) is what the question gives (INK); columns 2 to 4 and the arrows are the solution (ANSWER). Nothing else is drawn.
- **Stable pictures.** Question figures show only what the book prints (C127: dots only, no 5s, no total; C129/C131: empty ring). Dot placement inside a stall is one fixed pattern per count (1 centre, 2 diagonal, 3 triangle), not copied from the book where the pairs sit side by side or diagonal; only the count per stall carries meaning. Horses in question figure C127 are SET_A; horses added by a solution (C130, C132) are ANSWER (rule: given INK, added ANSWER). Corner horses are circled (FOCUS) in every solution figure because the explanations are about corner horses counted on two sides.
- **C130** draws the LP's sample arrangement (1 horse top-left, 1 bottom-right, 2 in each of the 8 middle stalls). The LP says "your arrangement may differ".
- **C132** draws the LP's final state (16 horses). The middle stalls follow "2 then 1 going clockwise from each corner", which gives the LP's top side as 1 + 2 + 1 + 1 and the other sides the same by rotation. The second arrangement in the LP steps (3, 2, 3, 2 horses in the corner stalls, 10 horses) is not drawn: one solution diagram per item.
- **Totals in solution figures** are written as "19 horses", "18 horses", "16 horses" (two words, taken from the LP text).
- **Aspect ratio** 16:9 everywhere (the pipeline draws 16:9 cards), also for the chain and the stable.

## LP text issues

| Concept id | What is wrong or missing | Suggested sentence |
|---|---|---|
| M3.S31.T31.C127 (question) | The text never gives the horses' arrangement; only the book picture does. The figure carries it, but if the figure is ever dropped the question cannot be done. | "The stable is a square ring of 12 stalls. The horses stand like this: top row from the left 1, 2, 2, 0; left middle stalls from the top 1 and 3; right middle stalls from the top 2 and 3; bottom row from the left 0, 2, 3, 0." |
| M3.S31.T31.C129 and C131 (question) | The text says "square stable" but not that it is a ring of 12 stalls with shared corners. | "The stable is a square ring of 12 stalls: 4 along the top, 4 along the bottom and 2 on the left and on the right. A horse in a corner stall is on two sides." |
| M3.S31.T31.C132 (solution) | The answer "2 more horses" is one reading. The LP's own steps show that with the corner stalls crowded (3, 2, 3, 2) only 10 horses are left with 5 on every side, i.e. up to 8 more could be stolen. The book prints no number. Steps 8 and 9 also contain a sentence addressed to the author ("The book does not print a number for this, so this is one way to read the question"), which does not belong in a learner-facing solution. | Decide the intended answer. If "2 more" stays: "He can steal 2 more horses, leaving 16 with one horse in each corner stall. With fewer horses the corner stalls must be crowded, for example 3, 2, 3, 2 horses in the corners and 10 horses in all, and the king would notice." Remove the author-addressed sentence. |
| M3.S31.T31.C132 (solution) | Step 6 says "The other three sides are the same" without saying in which direction 2 and 1 run. | "Going clockwise from each corner, the two middle stalls hold 2 and then 1." |
| M3.S28.T28.C119 (item hint `q_figure`, not student text) | The hint says four empty rows follow the table; the book prints four filled rows only. | Not a student-text issue; fix or ignore the hint. |

## Book unclear or inexact

- Page 15: the dots inside a stall are drawn side by side, diagonal or in a triangle without meaning; only the count per stall matters (checked: 19 in all, each side 5).
- Page 16: the two empty stables are unlabelled; which one belongs to "arrange the 18 horses" and which to "how many more" is by position (left, right) only.
- Page 16: "How many more horses can the thief steal before the king notices something is wrong?" has no printed answer and no stated limit (see C132 above).
- Page 12 and page 13: the book has no printed solutions section; the LP solution text is the answer followed. Nothing in the LP contradicted the book in this chunk (all sums, counts and chains in the LP solutions for C104 to C132 were recomputed and are right).

## Book mistakes (decision 1)

None found in this chunk; nothing corrected. Figure letters (decision 3): the chunk has no lettered figures, none drawn.
