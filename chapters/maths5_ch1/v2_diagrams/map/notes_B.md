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
