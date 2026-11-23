# Chunk C notes: Class 8 Ch 10 "Proportional Reasoning-2" (plan cbse_eng_maths8_ch10_v35)

Units: M3.S18.T18 "Questions: Figure it Out 3.6" (9 pairs, LP Q1 to Q9) and M3.S19.T19 "Summary" (concept C90, 4 worked blocks).
Result: 22 items, required 0 / optional 1 / none 21. Validator: errors 0, warnings 0.

I read pages 13, 14 and 15 of the book as pictures. The only pictures that belong to this chunk are the two scene illustrations on page 14 (Q10 and Q11); the page-13 donut charts and the page-14 pie chart are book Q4 and Q5, whose LP items are in chunk B (M2.S11.T11.C44 and C46), so I did not claim them. None of the 18 base-inventory figures belongs to this chunk, so `figure_inventory` holds only two figures I found myself.

## 1. Judgement calls

- **Why nothing is required.** No question in this chunk gives a figure the learner needs. There is no "in the figure" wording, no data that lives only in a picture, no act-on-figure task, and every answer is a number or a sentence. All book data are in the text. The v3 triggers (FIG_REFERENCED, DATA_IN_FIGURE, ACTION_ON_FIGURE, ANSWER_IS_FIGURE and so on) never apply, and the tie-breaker answers "yes, a careful student can solve it from the text".
- **Book Q10 picture (tank filled by two pumps) and Q11 picture (toys on a conveyor).** Both are scene illustrations with no numbers or labels, so they are `none:DECORATIVE_ONLY`. They are recorded as `NEW-P14-pumps-tank-Q10` and `NEW-P14-toy-conveyor-Q11` because the base inventory skipped them as decoration. Q10's picture shows two pumps but does not show which is small or large; the toy count in Q11 (8 toys in the picture) has no link to 42 machines, 63 days or 54 days.
- **C85 solution (Q7, two pumps together): `optional`, not added.** A tank bar cut into 6 equal parts would show why 1/3 + 1/2 = 5/6 (small pump 2 parts an hour, large pump 3 parts an hour, together 5 of 6 parts). The LP already writes the fractions in LaTeX and the answer is a number, so by the tie-breaker this is "nicer", not needed. It is the only item that I did not set to none; it differs from its siblings because its steps involve fraction addition, not a single multiplication or division.
- **C81 solution (chairs, 25 rows of 12 into rows of 20): `none`.** The words "arrangement" and "rearranged" could suggest ANSWER_IS_FIGURE, but the answer asked for is a count (15 rows), not a drawn arrangement. A 25 x 12 versus 15 x 20 grid would be 300 dots and teaches nothing the line `25 x 12 = 300, 300 / 20 = 15` does not.
- **Sibling consistency.** All inverse-proportion word problems (C75, C77, C81, C83, C87, C89) have the same decision (none, LATEX_ARITHMETIC), and both direct-proportion ones (C73, C79) too. C85 is the one exception, with the reason above.
- **Summary block 0 ("match each statement to an example"): `none`.** The match is already a four-line list in the LP steps (statement then example with numbers). The book's Summary page is text only. A matching-arrows picture would be decoration.
- **Summary block 3 (girl 150 cm at 12 years, height at 24): `none`.** Pure reasoning in words; a growth graph would need data the book does not give (the LP itself says it "would need real growth data").
- **Drop actions.** Every pair item has an old card id (`...IMG1`) in the plan that these `none` decisions drop (action `drop_image`); the four worked items have no card (`no_image`). `coverage_report.lp_ids_dropped` is left empty as the brief says.

### Borderline

- C75 and C77 (water tank, painters): the inverse relation could be shown as a "work rectangle" (20 x 6 = 30 x 4 family-days; 3 x 4 = 4 x 3 worker-days). That is a nice teaching picture but no v3 rule asks for it; none.
- C81 (chairs): see above; none.
- C85 solution: optional (see above).
- Summary block 0: matching picture would only make it nicer; none.

## 2. LP text issues

(No LP text was changed and no decision was altered because of these.)

1. **Book numbers repeat across topics (C72 to C89).** The questions of topic M3.S18.T18 are labelled "Figure it Out 3.6, Q1" to "Q9", but the same labels are used again in M3.S15.T15 (Q1 to Q3: inverse tables, fill cells, which pairs) and in M2.S11.T11 (Q1, Q2: sleep charts, transport pie chart). The `ncert_refs` give the real position in the book's second Figure it Out 3.6 set (pdf pages 13 and 14): C72/C73 = book Q2 (FiOb2), C74/C75 = Q3 (FiOb3), C76/C77 = Q6 (FiOb6), C78/C79 = Q7 (FiOb7), C80/C81 = Q8 (FiOb8), C82/C83 = Q9 (FiOb9), C84/C85 = Q10 (FiOb10), C86/C87 = Q11 (FiOb11), C88/C89 = Q12 (FiOb12). Suggested labels: "Figure it Out 3.6 (second set), Q2" and so on, using those book numbers (or one running LP number per topic).
2. **M3.S19.T19.C90 block 0 (E0): the question does not list the statements.** It says "Match each summary statement to an example from the chapter." but the four statements are only implied by the steps. Suggested question: "Match each of the four summary statements (many-term ratios, dividing a whole, direct proportion, inverse proportion) to an example from the chapter."
3. **M3.S19.T19.C90, blocks 1 to 3 (E1 to E3) are authored examples** (item_kind "authored") with no ncert_refs, while block 0 carries summary.1 to summary.4. Nothing is wrong with the numbers; just note that E1 to E3 are not from the book.

Checked and correct: every number in C73, C75, C77, C79, C81, C83, C85, C87, C89 and in the four Summary blocks was recomputed (120 / 24 = 5 and 5 x 20 = 100; 20 x 6 = 120, 120 / 30 = 4; 3 x 4 = 12, 12 / 4 = 3; 6 / 2 = 3 and 3 x 5 = 15; 25 x 12 = 300, 300 / 20 = 15; 8 x 45 = 360, 360 / 9 = 40; 1/3 + 1/2 = 5/6, 1 / (5/6) = 6/5 = 1.2 hours = 1 hour 12 minutes; 42 x 63 = 2646, 2646 / 54 = 49; 60 x 2 = 120, 120 / 80 = 1.5; 60 / 3 = 20 and 20 x 7 = 140; 6 x 10 = 60, 60 / 4 = 15; summary examples 110 / 5.5 = 20, 4500 / 5 = 18000 / 20 = 900, 20 x 4 = 10 x 8 = 80).

## 3. Where the book itself is unclear

- The book has no printed-solutions section in this pdf, so every answer comes from the LP solution text.
- Q10 picture: the two pumps look different (one bare pipe, one with a motor) but nothing says which is the "small" and which the "large" pump; the picture is not used.
- Q11: the text says "a given number of toys" and the picture shows a short row of 8 toys; the number is not meant to be counted.
- Q12 has no picture of its own: the toy conveyor on page 14 sits between Q11 and Q12 but belongs to Q11 (it is beside Q11's text).
