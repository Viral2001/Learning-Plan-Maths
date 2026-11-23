# Chunk A notes (Class 5 Ch 15, topics M1.S2.T2 to M1.S7.T7)

Result: 18 units, 32 items. required 15 / optional 8 / none 9. Validator: errors 0, 5 warnings (all five are required items whose figure is not printed in the book: worked examples C15, C16, C26 and the two sample-answer pictographs C25, C37).

Required: question C5 (notebook), C18, C20, C22, C24 (shop pictograph), C28, C30, C32, C34, C36 (two-wheelers pictograph); solution C25 (scale 10) and C37 (scale 6); worked examples C15, C16, C26.

## 1. Judgement calls

- **Child TV Reporter table (P02) is LaTeX, not a picture.** It is a plain 2-column table of words and numbers (`LATEX_TABLE`). So Q1 draws only the notebook of 35 bubbles (P01); Q2 to Q5 (C7, C9, C11, C13) are `none` with the filled table as `text_alternative` and `needs_lp_text_sync: true`; their solutions (C8, C10, C12, C14) are `none` (they only read cells of that table; a box round the cells can be written in LaTeX).
- **Notebook (P01).** Drawn as 35 speech bubbles on a notebook page; the children's faces and the spiral rings are decoration and left out. The book's bubble order is scattered, so a clean 5 x 7 layout is used. I counted the bubbles myself on the page picture: 1/2 hr 9, 1 hr 13, 1 1/2 hr 7, 2 hr 3, 2 1/2 hr 3 (total 35), the same as the base inventory and the LP. Only the tally is exact.
- **Pictograph questions get one diagram per item** (4 shop, 5 two-wheelers), identical specs (`render_note` says "same as <first id>"). The key is drawn as in the book: a key box above the table for the shop, in the table header for the two-wheelers.
- **Pictograph numeric solutions are `optional`** (C19, C21, C23, C29, C31, C33, C35). They only read rows, multiply, add or subtract. What would help is the question pictograph with the row outlined / row values at the row ends / the difference between two rows, but the text already gives every number (tie-breaker and Step D "row totals beside a grid"). Not added.
- **Pictograph solutions that draw a new picture are `required`** (C25 scale 10 with 4, 5, 6 icons; C37 scale 6 with 4, 2, 6 icons), `derived_from` the question diagram (same frame and positions; new key text and icons in ANSWER green). Only the one sample answer of the LP is drawn (the LP also mentions scale 2 for the shop and scales 1, 2, 4, 12 for the two-wheelers; those stay text).
- **Worked example C15 (stationery shop)**: required, a pictograph with 1 icon = 5 items, Pens 2, Pencils 4, Erasers 7 icons (ANSWER green icons; the example asks to show the numbers as a pictograph). The teaching image C15.IMG1 shows the same idea but is not linked; the new id is C15.IMG2.
- **Worked example C16 (fruit stall)**: required, ONE diagram with two pictographs one above the other (scale 6: 2, 3, 5 icons; scale 3: 4, 6, 10 icons), because the LP answer lists both scales that fit. The scale 4 that does not fit is not drawn. New id C16.IMG2.
- **Worked example C26 (samosas)**: required (GRAPH_CHART, reading a pictograph) although every number is in the text. The pictograph is the figure being read; drawn in INK (it is given), no row values and no totals (30, 70, 20, 120 are the results of the steps). New id C26.IMG2.
- **Worked example C3 (12 reading hours)**: `none`. The 12 answers are in the text and the result is a plain 3-row count table: LaTeX array (`text_alternative` holds it). A teaching image of the same table exists but that was not the reason.
- Inventory: P03 and P04-pictograph-1 are used by several items, so the base id goes to the first use and `NEW-<base>-C<nn>` to each further question that draws it. Solution diagrams that redraw the same picture (C25, C37) are sample answers, not book figures, and have no inventory entry (hence the warnings).

## 2. LP text issues

- **M1.S3.T3.C5 (Q1)**: the question text never gives the table rows. Suggested: add the empty table as LaTeX with the rows 1/2 hour, 1 hour, 1 1/2 hour, 2 hours, More than 2 hours and a blank No. of Children column (the array is in the item's `text_alternative`).
- **M1.S3.T3.C7, C9, C11, C13 (Q2 to Q5)**: the questions say nothing of the data they need; the student must read the table filled in Q1. Suggested: add the filled table as LaTeX (1/2 hour 9, 1 hour 13, 1 1/2 hour 7, 2 hours 3, More than 2 hours 3), or the sentence "Use the table you filled in the first question." Without this the dropped old cards leave these questions with no data.
- **M1.S7.T7.C28**: "passing her house" has no "her" in the question; suggested "passing Deepti's house".
- **M1.S7.T7.C29 and later two-wheeler solutions**: step 1 of C29 says "Icon box"; in the book the key sits in the table header (the shop pictograph has a real icon box). Suggested "Key" for the two-wheelers.
- **M1.S7.T7.C37 step 5**: "The scales 1, 2, 4 and 12 fit too" leaves out 3 (the book's scale) and 6 (the one drawn); fine as "too" but could read "The scales 1, 2, 3, 4, 6 and 12 all fit."
- **Solution `text` fields (all pair answers)** still hold old markers such as "[Image: ...: solution]" and "[Image: ...: solution (continued)]" in the middle of the steps; they should be removed when the new token goes before step 1.

## 3. Borderline

- Q2 to Q5 of Child TV Reporter question side `none` (plain table to LaTeX). An alternative reading is `required` (FIG_REFERENCED: "Look at the table"), a plain filled table as a picture. I followed `LATEX_TABLE`; this only works if the LP text sync is done.
- Q1 question draws the notebook only; the empty table is LaTeX. An alternative is one picture with the notebook and the empty table side by side (and a solution picture with the counts filled in).
- C6 solution `optional` (notebook bubbles coloured by answer value would help counting 35 bubbles).
- All seven pictograph numeric solutions `optional` (see above); the old plan had a picture for each. If the team wants "outline + value" solution pictures, these seven flip to `required` with `derived_from` the question diagram.
- C26 worked example `required` although the numbers are in the text; C3 worked example `none`.
- C16 holds two pictographs in one picture (could be split in two).
- Question side of C24 and C36 ("choose another scale") `required`: the data to re-scale lives only in the book pictograph.

## 4. Book unclear or wrong

- No print error found in the pictures of pages 1 to 4 (counts 8/10/12 icons on page 3, 8/4/12 scooters on page 4, 35 bubbles on page 1).
- The book prints "No. of Children" blank on page 2 and never gives the filled table; the LP's counts (9, 13, 7, 3, 3) come from the notebook tally and agree with the page picture.
- The key of the shop pictograph is a separate box above the table and the table has no scale inside it; the two-wheeler key is inside the header. The diagrams keep both placements.
