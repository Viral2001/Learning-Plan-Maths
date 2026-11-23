# Class 7 Ch 12 Another Peek Beyond the Point - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths7_ch12` v32 (taken from staging). Result: new V2 version v33 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (136 items from 74 units)
{"worked_example": {"none": 12}, "question": {"none": 58, "required": 4}, "solution": {"none": 57, "optional": 3, "required": 2}}

Optional, NOT added: [('C66', 'solution'), ('C77', 'solution'), ('C116', 'solution')]

needs_lp_text_sync: [('C149', 'question')]

## The 6 diagrams
| id | side | type |
|---|---|---|
| M1.S5.T5.C21.IMG1 | question | mensuration_figure |
| M3.S32.T32.C143.IMG1 | question | flow |
| M3.S34.T34.C149.IMG1 | question | number_line |
| M3.S34.T34.C150.IMG1 | solution | number_line |
| M3.S36.T36.C165.IMG1 | question | cell_grid |
| M3.S36.T36.C166.IMG1 | solution | cell_grid |

### Chunk A notes (from the decision agent)
# Chunk A notes: Class 7 Ch 12 "Another Peek Beyond the Point" (v32 -> diagram map)

Chunk A = topics M1.S2.T2, M1.S3.T3, M1.S5.T5, M1.S6.T6, M1.S7.T7, M1.S8.T8, M1.S9.T9, M1.S10.T10 (16 units, 30 items).
Result: required 1 / optional 0 / none 29. Validator: errors 0, warnings 0.
Book pages used: 1 to 7 (all looked at as pictures). There is no printed-solutions section, so the LP solution text was the answer to follow.

## 1. Judgement calls

1. **Example 4 question (M1.S5.T5.C21) = the only required diagram.** The book question is "Find the area of the given rectangle" and the book draws the rectangle with 13.3 cm under the bottom side and 5.7 cm along the left side. The LP question text repeats both lengths, so a student could attempt it from text; I still marked it required because the book question GIVES a figure and the prompt's own typical pair (Step E) is "figure-based question, numeric answer: Q required, S none". If the reviewer wants the stricter tie-breaker ("could a careful student solve it from text alone?"), flip it to none (TEXT_SUFFICIENT); nothing else depends on it. The diagram is drawn exactly to scale (7.0 x 3.0 units = 13.3 : 5.7); the book draws it about 1.9 : 1, not to scale. It shows no area, no working and no vertex letters. Its solution is `none` (SAME_AS_QUESTION_DIAGRAM + LATEX_ARITHMETIC): area is a number and nothing is marked or split.
2. **M1.S3.T3.C9 / C10 (expansion table, p.2): both sides none (LATEX_TABLE).** The book table (Fraction | Expanding the Numerator | Sum of tenths, hundredths, thousandths | Decimals, one solved row 254/1000) is a plain table with no colour meaning, and the LP text already names the three fractions and the form wanted. The only counter-argument is that a filled table is also listed under ANSWER_IS_FIGURE (Step B); I kept text because the LP solution already writes every row out in four steps and the brief says plain tables of numbers stay text/LaTeX. If the user prefers a filled-table picture, the solution side is the one to flip (the table has 4 columns, 3 filled rows, stacked fractions).
3. **Digit-count table (p.4-5, worked example M1.S8.T8.C35): none (LATEX_TABLE).** Plain table of digit counts, bold numbers only, and the LP steps already state every count. The existing kept image M1.S8.T8.C35.IMG1 (10 by 10 grid, tenths times tenths) is a different teaching figure and is untouched, so no new id was created for this concept.
4. **Decimal-places brace figure (p.5) and Example 5 call-out (p.6): none for M1.S9.T9 and M1.S10.T10 solutions.** The answer in each case is a single number found by counting places; the LP steps say "2 + 1 = 3 decimal places" and "1 + 2 = 3" in words. The brace figure is already the teaching image M1.S8.T8.C36.IMG1 (never linked). Sibling check: unit 15 and unit 16 solutions got the same decision.
5. **Hop-arrow rule picture (p.2-3), worked example M1.S2.T2.C5: none.** Not a lettered/referred figure, the LP steps describe the hops in words, and the picture is the teaching image M1.S2.T2.C4.IMG1.
6. **Figure it Out coin stack (M1.S7.T7.C31, book Q5)**: the book draws nothing for the "cylinder of 36 coins"; a stack picture would only decorate, so none.
7. **Sibling consistency**: all five Figure it Out items (book Q1, Q3, Q4, Q5, Q7) and Examples 1 to 3 have the same decision (question none, solution none, text/LaTeX). Example 4 differs only because the book gives a figure there (see 1).
8. **Figures left to other chunks**: P06-table-1 (Situation 1/2/3 table, LP topic M1.S12.T12) and P08-table-1 (Figure it Out Q10 table, LP topic M1.S11.T11) are in the book pages my units touch but belong to those other units, so I did not claim them. If neither chunk claims them the merge check will flag them.

## 2. Things in the LP that look wrong or thin

1. **Figure it Out numbering does not follow the book.** M1.S7.T7 labels its five items "Figure it Out 4.2, Q1 to Q5" but they are book Q1, Q3, Q4, Q5 and Q7 (ncert_refs FiO1, FiO3, FiO4, FiO5, FiO7 are right, `book_number` is not). M1.S11.T11 restarts at "Q1 to Q4" (book Q2, Q6, Q8, Q10) and M1.S13.T13 has another "Q1" (book Q9). The same label "Figure it Out 4.2, Q1" therefore appears three times.
2. **The Jonali-Pallabi game board (p.1) has no question or answer item.** The seven fractions (3/10, 4/100, 67/1000, 457/100, 71/100, 43/100, 9/100) and the six blanks only appear inside the teaching concept M1.S2.T2.C3 (its step 3 lists the answers). Not a diagram problem, but a practice item is missing; I mapped P01-table-1 to `none:LATEX_TABLE` for that reason.
3. **M1.S3.T3.C9 (expansion table)**: the question text does not mention the table or the solved model row (254/1000 = 200/1000 + 50/1000 + 4/1000 = 2/10 + 5/100 + 4/1000, 0.2 + 0.05 + 0.004 = 0.254). The `q_figure` hint describes it, but the LP question text alone gives no model of the layout. The LP solution text matches the book's pattern and all arithmetic checks.
4. **Example 4 question** (M1.S5.T5.C21) says "a rectangle 5.7 cm by 13.3 cm"; the book says "the given rectangle" with the lengths only in the figure. Fine for the LP (text carries the data), noted for the figure decision above.
5. **Arithmetic check of every LP solution of the chunk**: all products, sums and conversions were recomputed and are correct (e.g. 57 x 133 = 7581, 125 x 75 = 9375, 1.45 x 36 = 52.2 mm = 5.22 cm, 6.4 x 50 = 320, 58 x 124 = 7192, 57 x 1335 = 76095). No LP solution contradicts the book.

## 3. Places where the book itself is unclear

1. **Example 4 rectangle is not to scale**: drawn about 1.9 : 1 although 13.3 : 5.7 = 2.33 : 1. My spec draws it to scale.
2. **Digit-count table is split over two pages** (p.4 rows 1-2, p.5 rows 3-4, header not repeated); treated as one table.
3. **Book wording "one-thousands"** in the table header (p.2) is printed that way (should read one-thousandths); the LP uses "thousandths".

### Chunk B notes (from the decision agent)
# Notes for chunk B (Class 7 Ch 12, topics M1.S11.T11 to M2.S22.T22)

Result: 31 items (14 questions, 14 solutions, 3 worked examples). Required 0, optional 2, none 29. Validator: errors 0.
No item in this chunk needs a drawn figure: the book's given figures here are plain tables, a list of equations and long-division sketches, which the v3 rules send to LaTeX.

## 1. Judgement calls

1. **Plain "complete the table" questions, none (LATEX_TABLE), question and solution.** M1.S11.T11.C48/C49 (book Q10, table x 10, x 100, x 1000, P08-table-1) and M2.S16.T16.C60/C61 (the division table, P09-table-1). Step B lists "filled table" under ANSWER_IS_FIGURE, but Step C (LATEX_TABLE) and the prompt's own example ("Complete the table of how many numbers have 1 to 5 digits" -> LaTeX array) send a plain headings-and-numbers table with no colour meaning to LaTeX, and the brief repeats it. The numbers to multiply or divide are in the question text, and the solution steps list every product or quotient, so a careful student loses nothing. If the content team wants these tables as pictures, flip both pairs to required (the cells are given in `figure_inventory` and in each `text_alternative`). Both questions say "complete the table", and the old card was the only place that showed it, so I set `needs_lp_text_sync: true`: the table should be written into the question as a LaTeX array.
2. **M2.S19.T19.C67 (powers of 2 and 5), none (LATEX_ARITHMETIC), sync true.** The book's boxed figure (P21-pattern-1) is two lists of equations with two "= ?". It has no colour or position meaning, so it is a LaTeX array, but the LP question text does not contain the eight known equalities, so the text must carry them (`text_alternative` has the full lists). The solution only adds 0.03125 and 0.00032, which the steps already compute.
3. **Example 7 solution (M2.S18.T18.C66) and Example 8 solution (M2.S22.T22.C77): optional, not added.** Example 7: a bar of 29 m cut 14 m + 14 m + 1 m (the book's bubble picture) would help, but the steps say it in words and the pair has two blocks (29 / 2 and 29 / 4), so one picture would cover only the first. Example 8: the book's final place-value tree (four boxes, each 3 Hundreds, 3 Tens, 1 Ones) would show the equal sharing, but the five LP steps give every regrouping. Both are the only places where the book draws more than LaTeX can; if the content team wants them, they are easy to promote (solution, `steps_tex` / `before_first_step`, no question figure because the questions give none).
4. **Worked example M2.S21.T21.C72 (1325 / 4): none.** The question gives no figure; the book's trees (P13, P14) are working. The same regrouping chain is already the concept image M2.S21.T21.C71.IMG1 (not linked). Kept `none` rather than `optional` for that reason; Example 8 (1324 / 4) is `optional` because no teaching image shows its trees. This is a small asymmetry, stated here on purpose.
5. **Examples 9, 10, 11 solutions: none (LATEX_ARITHMETIC).** Long division is a LaTeX layout (Step C). The book colours the place labels and draws arrows from each row to its place, but the LP steps already name each place ("23 Tens", "50 Tenths", "10 Thousandths"). `text_alternative` gives the rows and labels to write. The three are consistent with each other.
6. **Examples 6 and 7 questions: none (DECORATIVE_ONLY, TEXT_SUFFICIENT).** The pictures are illustrations (a girl cutting a ribbon, two girls with a speech bubble). Every number is in the text.
7. **Worked examples M1.S12.T12.C50 and C51: none.** The book gives no figure for the first; for the second the book's three-situation table (P06-table-1) is a teaching table and the plan keeps it as concept image M1.S12.T12.C51.IMG1. Nothing linked.
8. **Concept-image accounting (no links):** P06-table-1 -> M1.S12.T12.C51.IMG1; P08-ribbon_picture-1 -> M2.S14.T14.C55.IMG1; P13-division_tree-1..3 and P14-division_tree-1..2 -> M2.S21.T21.C71.IMG1 (same 1325 / 4 regrouping chain, a place-value chart rather than trees); P15-long_division-1..4 and P16-long_division-1 -> M2.S21.T21.C73.IMG1 (snapshots of the 237 / 8 long division whose finished form is that image). Figures with no teaching counterpart are `none`: P08-table-1, P09-table-1 (LATEX_TABLE), P09-ribbon_picture-1, P11/P12 trees (TEXT_SUFFICIENT), P16-long_division-2, P17-long_division-1, P21-pattern-1 (LATEX_ARITHMETIC).
9. **No figure of the base inventory was wrong for my chunk.** I checked P08-ribbon_picture-1 (10 squares, counted), P09-ribbon_picture-1 (labels 14m, 14m, 1m, 29m), P09-table-1, the division trees on pages 11 to 14, the long divisions on pages 15 to 17 and P21-pattern-1 against the page pictures. No "CORRECTED" entries.

## 2. Things in the LP that look wrong or thin

1. **LP "Figure it Out" numbers are not the book's.** M1.S11.T11 is labelled Q1 to Q4 but holds book Q2 (4.2.FiO2), Q6 (FiO6), Q8 (FiO8) and Q10 (FiO10); M1.S13.T13 "Q1" is book Q9. Chunk A's labels Q1 to Q5 (book Q1, Q3, Q4, Q5, Q7) collide with these (two different items are both "Figure it Out 4.2, Q1"). The `ncert_refs` are right; only the visible `book_number` labels mislead.
2. **M2.S21.T21.C72 has `ncert_refs: []` at unit level**, although its item says 4.3.ex8_1325, and its concept is named "1324 / 4 and 1325 / 4" while the worked block only does 1325 / 4.
3. **M2.S16.T16.C60 rewrites the book's table.** The book's table has two stray given cells (2.146 under / 100 with a blank first cell, 0.0058 under / 10000 with a blank first cell) and prints no instruction sentence. The LP turns them into "divide 214.6 and 58" (consistent: 214.6 / 100 = 2.146, 58 / 10000 = 0.0058). Fine, but it changes the book task from "find the decimal" to "divide the decimal".
4. **M2.S15.T15.C58 says "another such ribbon" for the 100 pieces**; the book cuts the same 3.9 m ribbon into 100 pieces instead. A harmless rewrite.
5. **M1.S13.T13.C54 step 2** ("0.6 of 7 and 0.7 of 6 are more than half of a number above 2, so more than 1") is correct but loosely worded; step 1 ("both between 0 and 1: less than both") is the same rule as the book.
6. **Dangling "table".** M1.S11.T11.C48 and M2.S16.T16.C60 say "complete the table" and, once the old cards are dropped, no table is shown unless the text adds one (see call 1).
7. Every number in the LP solutions of this chunk was recomputed (products, quotients, decimal places, 1324 / 4 = 331, 1325 / 4 = 331.25, 237 / 8 = 29.625, 9.5 / 4 = 2.375, 0.06 / 5 = 0.012, 1/32 = 0.03125, 1/3125 = 0.00032): all correct. No LP solution contradicts the book.

## 3. Places where the book is unclear

1. **P14-division_tree-2 (page 14):** after "20 Hundredths / 4 = 5 Hundredths" nothing remains, yet the shallow arrow to the loose "2 Tenths" is still drawn (left over from the previous tree).
2. **Minus signs:** Example 8's long divisions print "-12", "-4"; Example 9's print "16", "72", "48" without minus signs; Example 10 and 11 likewise.
3. **P09-ribbon_picture-1 (page 9):** not to scale; the first "14m" part is drawn shorter than the second and the "1m" part is the right-hand end.
4. **P09-table-1 (page 9):** no instruction line; the intended task is read from the blank cells (see 2.3).
5. **Typos in the printed text:** "regrouped" for "regroup" (page 15), "tenths.Each" without a space (page 16), "1 Ones" (pages 11 to 14).
6. **P21-pattern-1 (page 21)** sits under the second Figure it Out of 4.3 but belongs to the Math Talk "What pattern do you observe? Why are 2 and 5 related in this way?", which the LP ties to the 10/3, 1/32, 1/3125 item (4.3.two_five); the LP item merges three book sources (10/3 from page 10, the lists from page 21, and the question about 2 and 5).

### Chunk C notes (from the decision agent)
# Notes, chunk C (Class 7 Ch 12, topics T23, T25, T26, T28, T29)

Result: 32 items, required 0 / optional 1 / none 31. Validator: errors 0, warnings 0.
Reason for zero required: every question and worked example in this chunk is decimal arithmetic (conversion of fractions, long division,
moving the point). I looked at book pages 17 to 21: none of these items has a printed figure, and no printed answer is a picture.

## 1. Judgement calls

- M2.S28.T28.C116 (Q3, 1 / 7, solution) = OPTIONAL. The old card hint (`s_figure`) says "a chain of arrows through the remainders 1, 3, 2, 6, 4, 5
  that returns to 1". That is the book's remainder chain (P19-flow-1) and it already exists as the teaching image C108.IMG1 (never linked in v3).
  The question asks to list the remainders and the LP steps list them all, so the tie-breaker gives "nicer, not needed". v3 section 3 ("a flow-chart
  of a procedure already drawn as a concept image -> none, or optional on the solution side") fits. If you want the picture, this is the only item
  to flip to required. The solution would then be a new diagram C116.IMG1 with the loop 1 -> 3 -> 2 -> 6 -> 4 -> 5 -> back to 1 (derived_from null,
  question has none). Text alternative given in the map: write the chain as LaTeX.
- M2.S28.T28.C118 (Q4, 142857 times 1 to 7, solution) = none, LATEX_TABLE. A column of seven products shows the cycling digits as well as a ring
  would; the ring is the teaching image C109.IMG1. This differs from Q3 on purpose: Q3's answer is a loop that closes (a chain), Q4's is a list.
- Long divisions (T23 Q1 and Q4, T25 both examples, T26 all four, T28 Q1, Q3, Q5): none, LATEX_ARITHMETIC. The v3 list says long division is
  LaTeX/text. The LP steps already say every regrouping in words. If the team later wants stair-case long-division pictures, the items to revisit are
  C85, C91, C96, C98, C100, C112, C116, C120 (solutions) only; no question gives a figure.
- M2.S29.T29.C121 (worked: 128 / 4 and 128 / 0.4): none, TEXT_SUFFICIENT. The number line with the two arcs is already the kept concept image
  C121.IMG1; a worked example never links it and does not need a second copy: three one-line comparisons are complete in text.
- M2.S29.T29.C122 (worked: 12.5 / 2.5, / 1, / 0.5 "and make a table"): none, LATEX_TABLE. The table is a plain 3-row table of numbers
  (divisor, quotient, bigger/equal/smaller than 12.5). Suggested LaTeX array is in the item's text_alternative. The book itself prints no such table
  (Math Talk on p.20 only asks the student to make one), so there is no figure to draw.
- M2.S25.T25.C95 (Example 12, Ravi 126 km in 2.5 h): none. The bar picture is the concept image C92.IMG1 (T24); the book prints no figure for the example.
- M2.S26.T26.C103 (book FiO Q4, blanks in equations): none. The blanks are underlines in `question_tex` (`\underline{\hspace{1.2em}}`), which is
  LaTeX, not a figure. The "box_equation" figures of page 28 are another chunk's.
- Base figures (all three on page 19, section "Does This Ever End?", which only my chunk's questions use):
  - P19-long_division-1 (10 / 3 stair-case) -> concept_image C107.IMG1 (same picture: long division of 10 by 3 with the remainder 1 circled).
  - P19-flow-1 (remainder chain) -> concept_image C108.IMG1 (title "The remainder chain of 1 / 7").
  - P19-long_division-2 (1 / 7 stair-case with three red circles) -> none:LATEX_ARITHMETIC. I did not map it to C108.IMG1 because that image is the
    remainder ring, not the long-division layout; the layout is LaTeX material. I checked all three descriptions against page_19.png: they are right
    (the `unclear` doubt on P19-long_division-2 is only about indentation, which does not matter as nothing is drawn). No "CORRECTED" needed.
  - No other base figure belongs to my units: pages 17 (FiO Q1-4), 18 (Examples 12, 13), 20 and 21 (FiO Q2-5, Dividend/Divisor/Quotient) have none.
    P17-long_division-1 is Example 11 (T22, chunk B) and P21-pattern-1 is the Math Talk box under FiO Q10 (later chunk).

## 2. Things in the LP that look wrong or odd

- Book numbers repeat. The LP labels the second "Figure it Out" set of section 4.3 as Q1 in T20 (book Q1, fractions to decimals), Q1 to Q4 in T26
  (book Q2 to Q5, ncert_refs FiOB2 to FiOB5 are right) and Q1 to Q5 in T30 (book Q6 to Q10). So "Figure it Out 4.3, Q1" appears three times in the
  plan (T20 C69, T23 C84 which is the first set and correct, T26 C99), and T26's labels are off by one against the book. Worth fixing in the
  `book_number` / concept names; not a diagram matter.
- T23 Q2 (C86): the book prints options (i) and (iv) of part (b) both as 4458.75 (book error). The LP question reproduces it and the solution
  explains it; fine, but a reader may think it is a typo of ours.
- T28 Q1 solution (C112) starts at "10 Ones / 3" and skips the book's first step (regroup 1 Ten into 10 Ones); harmless.
- T28 Q2 question text asks "Find 10 / 9 and 100 / 11" but the book's phrase is the closing line of the 10 / 3 box ("Can you find the quotients
  of 10 / 9, and 100 / 11?"); the LP is right.
- T23 and T26 solutions: I recomputed every value (3.6, 103.75, 608.5, 603.375; 381.5 and 445.875; 33, 3.3, 0.33, 0.033; 15.75 down to 0.001575;
  50.4; 3.6 and 36; 20.7166..., 3.768421...; 18.72, 156, 1.2, 0.01872; 1000, 0.1, 10, 0.1, 10, 100; 1.64, 16.4, 164; 1.111..., 9.0909...;
  the 1 / 7 remainders 1, 3, 2, 6, 4, 5; 142857 times 1 to 7; 0.0588235294117647 and its double; 32, 320; 5, 12.5, 25). All agree with the book.

## 3. Where the book itself is unclear

- Only the Q2 (b) options above (duplicate 4458.75).
- Page 21 prints Q5's last sentence as "24.6 / 1.5" with a stray space; the LP reads it as 24.6 divided by 1.5 (quotient 16.4, same as 2.46 / 0.15). Right.

### Chunk D notes (from the decision agent)
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

### Chunk E notes (from the decision agent)
# Chunk E notes (Class 7 Ch 12, units 69 to 74)

Units: worked example M3.S35.T35.C159, and the five pairs of M3.S36.T36 (C161/C162 to C169/C170).
Result: 11 items, required 2 / optional 0 / none 9. Validator: errors 0, warnings 0.
Base figures claimed (all on book page 28): P28-box_equation-1, P28-box_equation-2, P28-box_equation-3 (all none:TEXT_SUFFICIENT),
P28-table-3 (question diagram of C165) and NEW-P28-table-3-sol (second use of the same table, solution diagram of C166).
The other page 28 figures (P28-table-1 and P28-table-2, the conversion boxes of book Q5) and the page 27 number lines belong to chunk D, not to this chunk.
P21-pattern-1 (Math Talk 1/2, 1/(2x2), ...) is not used by any item of this chunk.

## 1. Judgement calls

- **C165 / C166 (book Q9, LP Q3): grid required on both sides. This is the one real judgement call.**
  The book table is a plain table of numbers (the prompt's LATEX_TABLE example is a one-row "complete the table" that stays LaTeX), but here it is a
  two-way grid with a heading row and a heading column, the question talks about "missing cells", and the answer is the completed grid
  (ANSWER_IS_FIGURE, B2: a filled figure is required even when the steps list the rows in words). The catalogue also names multiplication grids as `cell_grid`.
  If the reviewer prefers text, the alternative is a LaTeX array for both sides: question side then needs the three given cells placed in the array.
  Question diagram: given cells only (41, 4.1, 4100). Solution diagram: `derived_from` the question diagram, all 25 cells, the 3 given ones in INK, the 22 added in ANSWER.
  I put no fill in any cell (the book uses pale green) so nothing looks pre-shaded.
- **C161 / C162 (book Q7) and C167 / C168 (book Q10), the "fill the boxes" questions: none on both sides.**
  The book figure is only empty boxes: two boxes per equation in Q7, and the box pattern (two digits, point, one digit) x (one digit, point, one digit) in Q10.
  The LP question text already carries the same pattern as box signs, and the answers are filled equations (82.0 x 5.4 = 442.8 and so on) that LaTeX shows completely.
  Q7 and Q10 got the same decision on purpose (sibling consistency). The tie-breaker says a careful student loses nothing without the picture.
  Not made `optional` because the picture would only repeat the text.
- **C163 / C164 (book Q8) and C169 / C170 (book Q11): none.** No book figure; six divisions or six expressions in text, answers are arithmetic or one chain of letters.
  A number line for the sorted values in Q11 would be a nicety, not needed, so not even `optional`.
- **C159 (worked example "One fact, many answers"): no_image.** Three one-line calculations from 45 x 12 = 540. The teaching image M3.S35.T35.C159.IMG1 already fans out the same fact;
  it is not linked (v3) and the example does not need its own figure, because it names no lettered or referred figure. The example is LP-written, it is not in the book.
- Number style in the Q3 solution grid is the LP's own (410000, no commas), as the LP solution prints it.

## 2. Things in the LP that look off

- **Numbering.** The LP calls these questions "Figure it Out 4.4, Q1 to Q5" but they are book Figure it Out Q7 to Q11 (pages 94 and 95); `ncert_refs` 4.4.end7 to 4.4.end11 and the old card titles ("End of chapter Figure it Out, Q7") say so. Q1 to Q6 of the book are in topic T34 (chunk D). The `book_number` text in T36 is therefore misleading for a learner reading the book. Not changed (outside my files).
- **Q3 solution step 1 wording is ambiguous.** "Each step right in a divides the quotient by 10; the last column multiplies it by 10. Each step down in b multiplies the quotient by 10; the last row divides it by 10."
  True only if the last column and last row are compared with the first column and first row (15170 = 10 x 1517 and 370 = 10 x 37). Compared with the neighbouring column the last step changes the quotient by 10000.
  The final grid in the LP is right: all 25 cells recomputed with Decimal as column heading divided by row heading, and they match the LP rows exactly.
- **Q3 question text lists the data in words** (rows b, columns a, three given equations) and also says "missing cells"; with the figure placed after the question text this is repeated information, harmless. It lines up with the figure: (b=37, a=1517)=41, (b=3.7, a=15.17)=4.1, (b=0.037, a=151.7)=4100.
- **Q2 (book Q8) has (b) and (f) identical** (7.56 / 0.36 = 21). This is in the book itself; the LP solution says "(f) is the same division as (b)". It reads like a printing mistake in the book (something like 7.56 / 36 may have been meant). Left as in the book and the LP.
- Q4 answers were checked by brute force over all 120 digit placements of 2, 4, 5, 8, 0 in the boxes: maximum 82.0 x 5.4 = 442.8, minimum 45.8 x 0.2 = 9.16, 28.0 x 5.4 = 151.2 is above 150, nearest to 100 is 20.5 x 4.8 = 98.4 (next best 102.0), nearest to 5 is the minimum 9.16. All match the LP. Note that (c) has many correct answers; the LP gives one "for example", fine.
- Q5 values recomputed: (a) 230.93, (b) 1952.61, (c) 30.75, (d) 260.04, (e) 245.05, (f) 7.9682; order (f) < (c) < (a) < (e) < (d) < (b) is right.
- C159 numbers recomputed: 4.5 x 1.2 = 5.4, 0.45 x 12 = 5.4, 54 / 1.2 = 45. Right.

## 3. Where the book itself is unclear

- Page 28 prints the Q7 boxes the same size in (a) and (b), so the book does not show how many digits each factor may have (Q7 is open: 1.2 x 2 and 0.6 x 4 are both allowed).
- Q10's boxes show the digit pattern but the book does not say whether 0 may stand in the ones place of a factor. The LP's minimum 45.8 x 0.2 = 9.16 does that (0 in the ones box of the second factor); the LP answers follow the box pattern, so nothing to fix, but a different reading would change (b) and (e).
- The book has no printed solutions in this pdf, so there is no printed answer picture for Q9; the Q3 solution grid is drawn from the LP solution.
