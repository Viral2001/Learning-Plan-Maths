# Notes, chunk D (units 51-68), Class 7 Ch 12 "Another Peek Beyond the Point"

Result: 32 items. Required 2 (FiO 4.4 Q2 question and solution), optional 1 (C143 question), none 29. Validator: errors 0, warnings 0.

## 1. Judgement calls

- **FiO 4.4 Q2 (C149 / C150), the only diagrams in this chunk.** The LP keeps (a) and (b) in one concept, so each side gets ONE diagram with the two number lines stacked (as the book prints them), 16:9. Question figure: only what the book gives (end labels 3.1, 3.2, 2.15, 2.17; arrow over tick 7 of 11; tick 6 medium; no value at the arrow). Solution figure: `derived_from` the question figure, adds in ANSWER the values 3.16 and 2.162 and one gap bracket (0.01, 0.002; both numbers are in the LP steps). I did NOT label the middle ticks (3.15 / 2.16): the LP states 2.16 but not 3.15, and they are steps, not the final answer. The arrow is drawn in FOCUS (pointer) in both figures; the book draws it black. Checked on the page picture (zoomed): 11 ticks per line, end ticks long, tick 6 medium, arrow over tick 7, so "6th mark after 3.1 / 2.15" is right.
- **Q2 solution required**, not "none": the answer is a reading placed at the arrow (ACTION_ON_FIGURE / MEASUREMENT_READING), and the earlier author's `s_figure` hint says the same.
- **C143 question (Try This, 10,000 years) is optional, not none.** The text says "this final scheme" without stating it; in the book that is the three-question flow chart on p.25 (already concept image C138.IMG1, never linked). Same idea as the 'refer picture' rule: no diagram, the data goes into the text (`text_alternative` has the sentence, `needs_lp_text_sync` true). The sibling questions C139 and C141 state their rule in the question text, so they are none. The worked example C137 is none because a worked example is read together with its steps, and the steps spell out the four kinds of year.
- **C135 / C137 / C134 worked examples: none.** Year table (p.23) is a plain table and the flow charts are teaching figures; the items only need arithmetic. Figure accounting: P25-flow-1 maps to concept image C138.IMG1 and P23-table-1 to C135.IMG1 (the concept image shows only the first four of the table's eight years). P23-flow-1 and P24-flow-1 (the first two stages of the same procedure chart) are `none:REUSES_CONCEPT_IMAGE`; no concept image shows exactly them.
- **Q5 (conversions): none, LATEX_TABLE** for both book tables (facts box, six blanks); the LP question text already carries them. Filled answers stay a text line list; sibling consistency with the plain-table rule.
- **Q3 bananas and Q4 books: none.** Q3's fruit-shop picture is illustration with no numbers. Q4 has no book figure, and a shelf bar would only restate 2.5 cm, 80 books, 160 cm.
- **P21-pattern-1** (Math Talk table of 1/2^n and 1/5^n, printed under FiO 4.3 Q10 on p.87) is NOT claimed here: none of my units uses it; the LP puts it in M2.S19.T19.C67 (chunk B).
- **Second use of the two number lines.** The base ids are mapped to the question item; the solution figure's use is entered as `NEW-P27-number_line-1-sol` and `NEW-P27-number_line-2-sol` (two entries for a figure used by two items).
- **Decoration not inventoried (Step 0):** p.22 Earth/finish-flag art and calendar-makers cartoon, the cartoons on pp.24-26 and the Try This characters, p.27 fruit-shop picture.

## 2. Things in the LP that look wrong or thin

- **C144 step 6** says dropping leap days "for example no leap day in years divisible by 4000" fixes about 3 days per 10,000 years. In years 1 to 10,000 only 4000 and 8000 qualify (2 days; 2.5 on average). The text "about 3" is loose; "2 days" or "about 2.5" would be exact. Not a diagram matter.
- **C149 question text** describes the figure in words ("a number line from 3.1 to 3.2 split into 10 equal parts, with the arrow at the 6th mark after 3.1"). Once the figure is placed this repeats the picture, and the letters (a) and (b) have no counterpart in the figure (figure rules forbid letters). Suggest "(a) upper number line, (b) lower number line" in the text (flagged with `needs_lp_text_sync` on the question item).
- **Book numbers repeat across topics:** T30's items carry "Figure it Out 4.3, Q1" to "Q5" but they are the book's FiO 4.3 Q6 to Q10 (p.87); the same labels "Figure it Out 4.3, Q1/Q2/..." also appear in T23 and T26. T34 (4.4 Q1-Q6) is correct; chunk E's T36 "Q1-Q5" are book Q7-Q11.
- **C145 "Which pack is cheaper?"** is an LP-made example (no book ref); numbers check (40 / 250 = 0.16, 27 / 150 = 0.18).
- **C155 Q5, step 5** uses "9.02 x 1000 = 9020" for metres to millimetres without saying 1 m = 100 cm and 1 cm = 10 mm; correct but one fact shorter than the question's own facts list.
- All other LP solutions in this chunk were recomputed and are correct (e.g. 2425 x 366 = 887550, 7575 x 365 = 2764875, sum 3652425; 521/28 = 18.607...; 241/14 = 17.2142857...).

## 3. Book unclear

- p.27 (printed p.93): the Try This bullet says the Earth completes a revolution "in exactly 364.2422 days" (should be 365.2422). It is in no item of this chunk and the LP does not copy it.
- The number lines of FiO 4.4 Q2 carry no (a) / (b) letters; the LP's order (a) upper, (b) lower follows the book's top-to-bottom order.
