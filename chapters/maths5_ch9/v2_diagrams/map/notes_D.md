# Notes for chunk D (Class 5 Ch 9 "Coconut Farm", topics M3.S23.T23 to M3.S29.T29, units 52 to 67)

Result: 29 items = required 7 / optional 1 / none 21. Validator: errors 0, one warning (the Example 13 solution figure is not printed in the book, so no inventory figure maps to it; expected).

Required diagrams (all 16:9, base-ten blocks or place-value chips):

| Item | Diagram |
|---|---|
| C97 question | 62 as 6 ten-rods + 2 squares, 5 empty parts |
| C98 solution | 5 parts of 1 rod + 2 squares (12), remainder 2 |
| C99 question | 75 as 7 ten-rods + 5 squares, 8 empty parts |
| C100 solution | 8 parts of 9 squares, remainder 3 |
| C101 question | 324 as chips 3 x 100, 2 x 10, 4 x 1, 3 empty parts |
| C102 solution | 3 parts of 1 hundred chip, 0 tens, 8 one chips (108) |
| C104 solution | 6 parts of 2 ten chips + 2 one chips (22), remainder 4 (stands alone, derived_from null) |

## 1. Judgement calls

- **C97, C99, C101 questions (required).** The book prints the blocks/chips beside each example and the question card narrates them ("the following way", "this", "Divide into 3 equal parts"). The question figure shows only the given state (the number as blocks/chips and the empty equal parts). Red notes, outlines around single rods (they show the sharing) and every answer element are left out. For C97 the book's picture mixes start and end state; the question diagram takes only the start.
- **C98, C100, C102 solutions (required).** Same kind of answer in all four examples: equal sharing of place-value material (ANSWER_IS_FIGURE, B2 sibling rule). Each is `derived_from` its question diagram (same layout, new content in ANSWER green). C98 follows the book's printed end state. For C100 and C102 the book prints no end state (only the start state); the final state follows the LP solution text.
- **C103 question none, C104 solution required.** Example 13 (136 / 6) has no model picture in the book and the card gives none, so no question figure is invented (companion note). The solution is required for sibling consistency with examples 10 to 12 and draws the final state alone. The book's only picture for it is the long division (LaTeX).
- **Let Us Divide (a) to (d), 8 items, all none (LATEX_ARITHMETIC, HEADER_BOXES_ONLY).** v3 sends long division and plain place-value header boxes (Th H T O) to LaTeX. The LP text already gives every number and blank. A `text_alternative` per item says which LaTeX layout to write. Printed answers are filled arithmetic layouts, not pictures. All four letters get the same decision.
- **Let Us Do Q1 (C115/C116) none.** Ten digit-box frames = long-division skeletons; the LP text lists every frame with its blanks. The answers are numbers. I did not make one combined 10-frame picture.
- **C123 optional (not added).** A picture of 94 coconuts as 11 bags of 8 + 6 left (+ the 12th bag) would help show what the remainder means, but the text is complete.
- **C124 none (LATEX_TABLE).** The "bill" is a plain table of numbers with the example's own practice values.
- **C125, C105/C106, C117/C118, C119 to C122 none.** Word or arithmetic items with no figure in the book.
- **Figure letters (decision 3).** No letters drawn anywhere. The three question diagrams are single figures; the (a) to (d) layouts are none.
- **Teaching images (decision 5).** The plan's concept images in this part (C93.IMG1 "8 tens and 3 ones among 6 plates", C94.IMG1 "412 among 4 plates") show different numbers and are in topic T22. Nothing is linked to them. The 7 diagrams are drawn fresh.
- **Figure accounting.**
  - 25 base figures claimed: P10-base_ten_blocks-1/2, P10-long_division-1/2, P11-place_value_chips-1, P11-long_division-1/2, P12-long_division-1..6, P13-long_division-1/2, P13-division_frame-1..10.
  - 3 NEW- second-use entries: NEW-P10-base_ten_blocks-1-sol, NEW-P10-base_ten_blocks-2-sol and NEW-P11-place_value_chips-1-sol, for the solution diagrams.
  - Result: 6 mapped to items, 22 mapped none, 0 mapped to concept images.
  - **P16-table-1 (Vegetable Market table) not claimed.** My C124 uses its own practice values and does not use the book table. The pair vm.table is another chunk's. If both chunks claim it at merge, `none:LATEX_TABLE` would be my meaning for the plain table.
  - The riddle box on p.13 (girl illustration) is not in the base inventory; it is decoration, so I did not add a NEW- entry.
- Base descriptions were checked against pages 10 to 13: all 25 are correct, and the `unclear` lists were empty. I checked especially the ten frames (frame 7 reads `50 ) 1 0 0 [ ] ( [ ] 0`, as inventoried).

### Borderline (decision 4, v3 applied as written)

1. Question side of C97, C99, C101: the numbers are all in the text, so a strict "attempt" test could say none; I kept them required because the book prints the figure with the question and the question text points at it. If the user prefers, these three can drop to `optional`; the three solution diagrams would then need `derived_from: null` and would be redrawn as standalone figures.
2. Solutions C100 and C102 (and C104): required although the book prints no end-state picture; justified by the sibling rule and the LP's own s_figure hints for 10 to 12. If unwanted, C104 is the weakest (no figure at all in the book).
3. Let Us Divide (a) to (d), Let Us Do Q1, Let Us Solve 1 to 12: none by the v3 long-division rule although the book asks to complete a drawn layout. This is the biggest call (8 + 2 items). If the content team wants those layouts as pictures, they would be `other` diagrams of the two layouts per part.
4. C123 optional (not added).

## 2. LP text issues (not edited; suggestions only)

- **Example numbering.** C97/C98 to C103/C104 (book numbers "Example 10 to 13"): the book prints no "Example n" labels; its four examples are numbered 1 to 4 inside "Division Using Place Value". The LP's chapter-wide numbering is the LP author's, not the book's.
- **M3.S23.T23.C97 (question).** "She shows the following way of doing division using place value." The "following way" (blocks and long division) is not in the text. Suggested: "Look at the blocks: 6 tens and 2 ones. Divide 62 into 5 equal parts."
- **M3.S23.T23.C101 and C103 (questions).** The question text already contains the worked steps and results that the solution repeats ("24 Ones ÷ 3 = 8 Ones", "Total 13 Tens"), so the question gives the answer away and the question and solution cards duplicate text. Suggested questions: "324 ÷ 3: divide 324 into 3 equal parts. 324 = 3 Hundreds + 2 Tens + 4 Ones." and "136 ÷ 6: divide 136 into 6 equal parts. 136 = 1 Hundred + 3 Tens + 6 Ones."
- **M3.S24.T24.C105 (question).** "Look at the problems above" does not name them. Suggested: "Look at the four divisions 62 ÷ 5, 75 ÷ 8, 324 ÷ 3 and 136 ÷ 6."
- **M3.S25.T25.C107 (question, part a).** In the book the right-hand place-value layout of (a) is fully filled and is the model for (b) to (d). The LP gives only the quotient digits "1, 1, 7, 2", not the rows (7 - 6 = 1, 10, 43, 12), so the learner never sees the model. Suggested: add the filled layout as LaTeX, or its rows (the text_alternative on C107/C108 gives them).
- **C107, C109, C111, C113 (questions).** The two layouts (partial quotients; place value with Th H T O and the labelled rows) are only described in sentences. Suggested: write them as LaTeX layouts (text_alternative gives the layouts).
- **M3.S26.T26.C115 (question).** The part letter "(i)" is not wrapped in `$...$` like the other letters (formatting). The ten frames are written as prose; an explicit list is clearer.
- **M3.S29.T29.C123 (worked example).** Learner-visible "(practice values)", and two sub-questions with no context. Suggested: "Susie and Sunitha have 94 coconuts. (a) They pack them in bags of 8. How many bags do they need? (b) They share the 94 coconuts equally among 8 customers. How many does each customer get?"
- **M3.S29.T29.C124 (worked example).** Three sub-questions in one sentence, no bill shown, and missing data: "the quantity for a total of ₹990" does not say the price is the same ₹18 per kg (the solution uses 18). Also "(practice values)" shows to the learner. Suggested: "A bill: onions, ₹18 for 1 kg, 45 kg sold. (a) Find the total amount. (b) At ₹18 for 1 kg, how many kg give a total of ₹990? (c) 36 kg of another item cost ₹1260 in all. What is the cost of 1 kg?"
- **M3.S29.T29.C125 (worked example).** "(practice values)" in learner text.
- Solutions C106, C108, C110, C112, C114, C116, C118, C120, C122, C123 to C125: all arithmetic re-computed and correct (quotients, remainders, N = D x Q + R, the place-value digit strings, and all ten Let Us Do answers incl. (e) 848 / 868 and (g) 88 / 44 / 22 / 11). C118 step 1 assumes the first clue is an exact division; the second clue (x 2 = 420) fixes 210 anyway.

## 3. Where the book is unclear

- Let Us Divide (c) and (d), right layouts: pairs of empty brackets `(          )` appear to the right of the rows. They look like slots for place labels such as (Tens), (Ones). The book never says; the LP does not use them.
- Let Us Divide (b), right layout: the ones row prints `0___` (a blank after the 0), which is a slot for the digit 5 brought down; the quotient row has its tens digit 0 printed, thousands/hundreds/ones blank.
- Let Us Divide (b) to (d) start the right layout at the Hundreds row (30 hundreds, 28 hundreds, 98 hundreds), so the Thousands row is not drawn although the quotient has a Th slot; the LP solution adds a Thousands line (0 each) to match the four quotient digits.
- No printed solutions section in this pdf; the LP solution text was followed throughout. No print slips (wrong digit, wrong count) were found in the figures of this chunk, so no CORRECTED value was needed.
