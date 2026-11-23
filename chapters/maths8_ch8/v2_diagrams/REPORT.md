# Class 8 Ch 8 Fractions in Disguise - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths8_ch8` v56 (taken from staging). Result: new V2 version v57 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (207 items from 123 units)
{"worked_example": {"none": 37, "optional": 1, "required": 1}, "question": {"required": 10, "none": 73, "optional": 1}, "solution": {"none": 64, "required": 9, "optional": 11}}

Optional, NOT added: [('C34', 'solution'), ('C42', 'solution'), ('C44', 'solution'), ('C46', 'solution'), ('C48', 'solution'), ('C49', 'question'), ('C112', 'solution'), ('C118', 'solution'), ('C139', 'worked_example'), ('C166', 'solution'), ('C179', 'solution'), ('C187', 'solution'), ('C191', 'solution')]

needs_lp_text_sync: []

## The 20 diagrams
| id | side | type |
|---|---|---|
| M1.S3.T3.C8.IMG1 | question | fraction_model |
| M1.S3.T3.C10.IMG1 | question | fraction_model |
| M1.S3.T3.C11.IMG1 | solution | fraction_model |
| M1.S4.T4.C20.IMG1 | question | other |
| M1.S4.T4.C21.IMG1 | solution | other |
| M2.S6.T6.C53.IMG1 | question | number_line |
| M2.S6.T6.C54.IMG1 | solution | number_line |
| M2.S7.T7.C57.IMG1 | question | fraction_model |
| M2.S7.T7.C58.IMG1 | solution | fraction_model |
| M2.S7.T7.C60.IMG1 | solution | fraction_model |
| M3.S12.T12.C106.IMG1 | solution | other |
| M3.S12.T12.C107.IMG1 | question | flow |
| M3.S12.T12.C114.IMG1 | solution | other |
| M3.S12.T12.C116.IMG1 | solution | other |
| M3.S12.T12.C121.IMG1 | question | other |
| M4.S15.T15.C144.IMG1 | solution | cell_grid |
| M4.S18.T18.C177.IMG1 | worked example | cell_grid |
| M4.S19.T19.C186.IMG1 | question | mensuration_figure |
| M4.S19.T19.C198.IMG1 | question | other |
| M4.S19.T19.C204.IMG1 | question | data_graph |

### Chunk A notes (from the decision agent)
# Chunk A notes (Class 8 Ch 8 "Fractions in Disguise", LP cbse_eng_maths8_ch8_v56)

Units: 24 (topics M1.S1.T1, M1.S2.T2, M1.S3.T3, M1.S4.T4, M2.S5.T5) = 32 items.
Result: required 5 (3 question, 2 solution), optional 0, none 27. Validator: errors 0, 2 warnings (the two solution
diagrams C11 and C21 have no printed book picture to map; the pdf has no solutions section, so that is expected).

Diagrams made:
- M1.S3.T3.C8.IMG1 (question, Example 1): the book's page-2 bar model, 4 parts, red for 3, yellow for 1, with the 0 to 4/4 and 0 to 100/100 (25%..100%) scales.
- M1.S3.T3.C10.IMG1 (question) and M1.S3.T3.C11.IMG1 (solution, derived from it): Example 2 Method 3 bar, four empty boxes / the same four boxes filled 20%, 40%, 60%, 80%.
- M1.S4.T4.C20.IMG1 (question) and M1.S4.T4.C21.IMG1 (solution, derived from it): Figure it Out Q4 race line, runners A to D and six option boxes / the four matched boxes outlined and tagged A, B, C, D.

## 1. Judgement calls

- **C8 question = required.** The LP question is only "Yellow paint?". The data (red is 3/4 of the mixture) sits only in the book's bar model, and the book question ("Can you tell what percentage of the colour was made using yellow?") points at that picture. Codes FIG_REFERENCED + DATA_IN_FIGURE. The same picture is the teaching image of M1.S2.T2.C4 (M1.S2.T2.C4.IMG1), but v3 never links a teaching image, so it is drawn again. The 'refer picture' exception does not apply (the book answers the question, it does not just say "refer picture").
- **Colours in the C8 picture.** Red and yellow are paint colours and carry the meaning (no word labels in the book picture), so the spec gives hex values: red #D55E00 (palette vermillion), yellow #F0E442 (palette yellow). They are not style tokens; this is stated in the spec's `render_note`.
- **C10 question = required, C11 solution = required.** ACTION_ON_FIGURE: the student fills four empty boxes; the answer is the filled boxes (ANSWER_IS_FIGURE). The yellow hint speech bubble of the book ("Isn't it the same as finding 2/5 th of 100?") is a hint sentence, so it is not in the diagram. The book's red outline of the whole band is drawn as an INK outline (red carries no meaning there).
- **C20 question = required, C21 solution = required.** The positions of the four runners live only in the picture (DATA_IN_FIGURE). The task is "Match", and the LP answer is a pairing (A 38%, B 55%, C 72%, D 93%), which I treated as a figure answer (B2: answer is an arrangement, even if the steps describe it in words). The solution marks the matched boxes in ANSWER green and tags them with the runner letter; no connector lines (they would cross: A goes to the 3rd box, B to the 1st). The unused options 20% and 84% are left exactly as given (not restyled).
- **Runner positions (C20).** The book gives no numbers. I measured the circle centres on the page picture by pixels: 0.3175, 0.5323, 0.7531, 0.9454 of the Start-to-Finish line; the specs use 0.32, 0.53, 0.75, 0.95 (x = 240 + 1440 x fraction). Nearest-option check: A 32% -> 38% (20% is further), B 53% -> 55%, C 75% -> 72% (84% is further), D 95% -> 93%. This agrees with the LP answer.
- **Plain tables = LaTeX.** The free-hand table (book p.7, P07-table-1) has plain blue cells with no colour meaning, so C25 ("Anything interesting in the table?") and both C26 blocks are none / LATEX_TABLE with a `text_alternative` naming the LaTeX array (header 100, 200, 50, 80, 10, 35, 287; rows 25%, 10%, 20%, 5% (and 40%, 15% for C26)).
- **Figures not claimed.** Section 1.2 pictures P06, P08, P09, P10, P11, P12 and P15, P16 belong to units of the other chunks (Examples 1 to 6 and their Q/A pairs). I claimed only P07-table-1 from 1.2, because my C25/C26 units work on that table. If the merge shows another chunk mapping P07-table-1 differently, it becomes a separate NEW- use; both meanings are the same (a table, LaTeX) so that is harmless.
- **Page 5 cards.** P05-infographic-1 (boy, 60% water) = DECORATIVE_ONLY; P05-infographic-2 (Sun and planets) = TEXT_SUFFICIENT. No unit of this chunk asks anything about them (teaching fact cards, numbers in the caption).
- **Callout boxes not inventoried.** The orange equation boxes (p.1 "3/4 = 6/8 = 30/40 = 75/100", p.4 "9/34 = 26.47 percent ... per mille", p.7 "y/100 x 80") are formulas, not figures, so they are not in the base inventory and I did not add NEW- entries for them.

## 2. Borderline

- **M1.S3.T3.C9 (Example 1 solution) = none (SAME_AS_QUESTION_DIAGRAM + TEXT_SUFFICIENT).** One could argue for a solution figure that brackets the yellow quarter as 25%. The book picture already shows the yellow last quarter against the 25/50/75/100 scale, the answer is a number, and v3 Step E says "figure-based question, numeric answer: Q required, S none". If the reviewer wants it, the spec would be C8.IMG1 plus a bracket under the yellow part labelled 25% in ANSWER, derived_from M1.S3.T3.C8.IMG1.
- **M1.S4.T4.C21 (Q4 solution) = required.** The LP answer text carries every number, so a reviewer could call it none. I kept it required because the answer is a matching drawn on a given picture (ANSWER_IS_FIGURE) and the user's rule is not to flip a required item only because the LP text has the numbers.
- **M1.S1.T1.C1 block 3 (ratio 2 : 3)** is none. A bar of 5 parts would help, but the whole 2 + 3 = 5 is one line of words and the book gives no figure.
- **Diagnostics (C4, C24, C31, "Check my thinking")** are all none (text multiple choice, no book figure).

## 3. LP text issues (not edited, listed only)

- **M1.S3.T3.C8 / C9 (Example 1).** The question text is just "Yellow paint?" and lacks the data. Suggested: "Surya mixes red paint and yellow paint. The red paint makes up 3/4 of the mixture, which is 75%. What percentage of the colour is made with yellow?" (the diagram carries the bar). The solution step "100% - 75%" presupposes the 75%.
- **M1.S3.T3.C10 / C11 (Example 2).** The question text is just "Method 3 boxes" and lacks the task. Suggested: "Surya saves 2/5 of his prize money for a canvas. Fill the four empty boxes with the percentages that go under 1/5, 2/5, 3/5 and 4/5 of the bar."
- **M1.S3.T3.C12 / C13 (Example 3).** The question text "Which variety is more sugary?" lacks the data. Suggested: "Sugar makes up 9/34 of Variety 1 and 13/45 of Variety 2 of a biscuit. Which variety is more sugary?" Also: the book prints 28.88% for Variety 2; 13/45 = 28.888...% which rounds to 28.89%, so the LP's "about 28.89%" is right and the book's value is a cut-off (no diagram is affected).
- **M1.S4.T4.C20 / C21 (FiO Q4).** The question text ends with a bracket that describes the picture: "(Line from Start to Finish with runners A, B, C, D; options 55%, 20%, ...)". With the diagram placed after the question this is a duplicate description; suggest removing it (or keeping only the six options if the build wants them in text).
- **M1.S4.T4.C17 (FiO Q2 solution).** Step 2 reads "Used as the diagnostic above; if already used there, ask for the reason only." That is an instruction to the AI, not a student sentence. Suggest deleting the step.
- **M1.S4.T4.C23 (FiO Q5 solution).** The only step compares 3/11 with 3/10 = 30%, which is correct but never reaches the asked comparison with 61%. Suggested addition: "So 3/11 is less than 30%, which is less than 61%."
- **M2.S5.T5.C25 ("Anything interesting in the table?").** The table itself is not in the text, so the student cannot see what to look at. Suggested: add the completed LaTeX table (rows 25%, 10%, 20%, 5% for 100, 200, 50, 80, 10, 35, 287, values as in the C26 answer) before the question, or write "In the table you just filled in, is there anything interesting?" and place the LaTeX table.
- **M2.S5.T5.C26 blocks 0 and 1.** The two blocks have the identical question, steps and answer text (only example_id differs: free_hand_40 and free_hand_15). Also the question gives the row and column labels in words only. Suggested: keep one block with the LaTeX table, or make block 1 only the 15% row.
- **M2.S5.T5.C27.** Step 1 says "Say a recipe from I2 before computing." "I2" is an internal image code, meaningless to the student. Suggested: "Say a recipe from the building-block picture (50%, 25%, 10%, 5%) before computing."
- **Diagnostic blocks (M1.S2.T2.C4, M2.S5.T5.C24, M2.S5.T5.C31).** The text holds the internal sentence "Act on the diagnosis table." and the answer ("Answer: (b), reason (i)") inside the same text as the question; check that the build shows these only to the AI.
- **M1.S1.T1.C1.** Block 0 of the concept (not a unit) mentions "a bar picture" in the recap; the five worked examples themselves are text and have no picture.

## 4. Book unclear / checked

- All six inventory entries of this chunk were checked against the page pictures (pp. 2, 3, 4, 5, 7); the base descriptions are right. P04's "unclear" (runner positions by eye) is settled by pixel measurement (see above).
- The book's Method 3 figure (p.3) shows the speech bubble under the second box; it is a hint, not part of the data.
- The book has no solutions section in this pdf, so there are no printed-answer pictures; the two solution figures are drawn from the LP solution text.
- Arithmetic re-checked in the LP texts of this chunk: 3/5 = 60%, 7/14 = 50%, 9/20 = 45%, 72/150 = 48%, 1/3 = 33 1/3%, 5/11 = 45.45%; 15/25 = 60%; 15/80 = 18.75%; Q5 (i) to (iv) results; the 7 x 6 mental table values (25%, 10%, 20%, 5%, 40%, 15% of 100, 200, 50, 80, 10, 35, 287); 60% of 30 = 18 and 40% of 50 = 20; 25% of the sum = 60 so the sum is 240. All correct.

### Chunk B notes (from the decision agent)
# Notes, chunk B (topic M2.S6.T6 "Questions: Example", units 25 to 36, 24 items)

Result: required 2 / optional 6 / none 16. Question side: required 1, optional 1, none 10. Solution side: required 1, optional 5, none 6.
Validator: errors 0, warnings 0. Output: `map/out_B.json` (written by a script kept outside HERE).

The only diagrams added are the pair for the Percentages-beyond-100 table and number line (C53 question, C54 solution): the learner must mark nine values on the printed 0% to 400% band, and the LP answer itself says "Mark each on the 0% to 400% diagram". Everything else in this topic is a word problem with a numeric answer, a plain table, or both.

## Borderline

1. C34 (Example 1, solution) - optional, not added. Figure that would help: the book's double scale on p.6 (0, 25%, 50%, 75%, 100% over 0, 30 g, 60 g, 90 g, 120 g, Sugar bar to 25%). Why not required: the LP steps are 25% of 120 and 35% of 95 as arithmetic, and the teaching image M2.S5.T5.C24.IMG1 shows the two biscuit bars. Tie-breaker: a careful student solves it from the text alone.
2. C42 (Example 3, solution) - optional, not added. Figure: the book's 0 to 75 marks over 0 to 1.0 scale with the band to 60 shaded. LP solution is "80% of 75 by fraction, decimal or proportion": one line of arithmetic.
3. C44 (Example 4, solution) - optional, not added. Figure: the ratio bar 2 | 7 with whole 9. The LP steps say "The whole is 9 parts" and the sum 2 + 7 = 9 is trivial; teaching image M2.S5.T5.C30.IMG1 already shows this bar. Closest call of the five: the word "parts" points at a picture. If the user wants it, the figure is the nine-cell bar, 2 cells millet, 7 cells water, drawn to scale (the book draws it off scale, see below).
4. C46 (Example 5, solution) - optional, not added. Figure: the Delhi to Agra bar cut into five 20% pieces (92 km on two, 138 km on three, 230 km whole). The LP steps say "one 20% piece, then the remaining three pieces", which is also a picture-flavoured wording. Teaching image M2.S5.T5.C31.IMG1 shows the same bar.
5. C48 (Example 6, days 1 to 4, solution) - optional, not added. Figure: four bars on a 0 to 5000 / 0% to 100% scale (2000, 3500, 5000, 6000; the last runs 20% past the line). The LP steps give the one rule "sales over 5000, times 100". The book prints these four bars as its explanation and writes the percent under each; the answer is still four numbers.
6. C49 (Example 6, days 5 and 6, QUESTION) - optional, not added. This is the closest call in the chunk: the book prints the two bars with the question (inventory says "given in question"), so I looked hard at making it required. Every number in the figure (target 5000, sales 7800 and 9550) is also in the question words, and 2800 and 4550 are only differences, so the learner loses nothing without it (tie-breaker, Step C TEXT_SUFFICIENT). The same two bars are teaching image M2.S5.T5.C32.IMG1. It is not the Step B2 "refer picture" case (no printed answer), so the text must carry the data: see LP text issues, C49. If the user prefers the book's figure with the question, it is: scale 0 / 5000 / 10,000 over 0% / 100% / 200%, red outline 0 to 5000, green Day 5 to 7800 with arrow "2800", green Day 6 to 9550 with arrow "4550".
7. C50 (Example 6, days 5 and 6, solution) - none. With no question diagram, the solution would only add the labels 156% and 191% at the bar ends: that is the typical "figure question, numeric answer" pair (question figure, no answer picture).
8. Plain tables (C35/C36 free-hand table, C39/C40 FDP table, and the table half of C53/C54) - none, LATEX_TABLE. The book colours the cells blue, but colour carries no meaning, and the answer is the same grid filled with numbers. Sibling decision for all three tables. I gave the LaTeX layout in `text_alternative`.
9. C54 solution is required although the book prints no answer picture: the LP answer instructs the learner to mark all nine values, so the answer IS the marked band (B2). Question diagram = the band with the 90% arrow the book gives; the eight other arrows come only in the solution (ANSWER green), `derived_from` = C53.IMG1. Arrow labels are placed on two rows so 15% / 28.9% (55.6 px apart) and 90% / 110% (80 px apart) do not collide.
10. Base inventory: I added `NEW-P12-bar_model-1-sol` for the second use of the printed band (solution of C54), as the brief says for a figure used by two items. Figures P06, P09-2, P10, P11-5, P11-6 are mapped to the teaching images that show the same quantity (accounting only; if chunk A claims the same figures it should be as concept images, and the table figures P07, P08, P12-table as `none:LATEX_TABLE`).
11. Figure letters (user decision 3): none of my figures carries letters.

## LP text issues

The LP question texts of this topic are one-line stubs that omit the data of the examples. I did not change any decision because of it. For each, the sentence the card needs (suggested):

- M2.S6.T6.C33 (Example 1, Q): "Who ate more sugar?" lacks everything. Suggested: "Madhu ate 120 g of biscuits that have 25% sugar. Madhav ate 95 g of biscuits that have 35% sugar. Who ate more sugar?"
- M2.S6.T6.C35 (free-hand table, Q): "The table (25%, 10%, 20%, 5%, then 40% and 15%) for 100, 200, ..." has no instruction. Suggested: "Without pen and paper, find 25%, 10%, 20%, 5%, then 40% and 15%, of 100, 200, 50, 80, 10, 35 and 287 and write them in the table. The first entry (25% of 100) is 25." Also the book table has only the rows 25%, 10%, 20%, 5%; the rows 40% and 15% come from the later Math Talk prompts (the LP merged them, which is fine, but the hint `q_figure` still says four rows).
- M2.S6.T6.C39 (FDP table, Q): "Complete the FDP table" does not give the table. Suggested: "Complete the table: Per cent 50%, 100%, 25%, 75%, 10%, 1%, 5%, 43%; Fraction (50/100 is given under 50%); Decimal (0.5 is given under 50%)."
- M2.S6.T6.C41 (Example 3, Q): "Zubin's minimum score" lacks the data. Suggested: "The maximum marks in a test are 75. Students who score 80% or above get an A grade. How much should Zubin score at least to get an A grade?"
- M2.S6.T6.C43 (Example 4, Q): "Millet kanji" lacks the data. Suggested: "A millet kanji is made by mixing millet and water in the ratio 2:7. What percentage of the mixture is millet? How much millet is needed to make 500 ml of the mixture?"
- M2.S6.T6.C45 (Example 5, Q): lacks the data. Suggested: "A cyclist cycles from Delhi to Agra and completes 40% of the journey. He has covered 92 km. How many more kilometres does he have to travel to reach Agra?"
- M2.S6.T6.C47 (Example 6, Q): "Days 1 to 4" lacks target and sales. Suggested: "Kishanlal aims at daily sales of at least 5000 rupees. His sales on Days 1 to 4 were 2000, 3500, 5000 and 6000 rupees. What percentage of the target did he achieve on each day?"
- M2.S6.T6.C49 (Example 6, Q): "Days 5 and 6" lacks target and sales, and (because the question diagram is optional and not added) the text must carry them. Suggested: "Kishanlal's daily target is 5000 rupees. On Day 5 his sales were 7800 rupees and on Day 6 they were 9550 rupees. What percentage of the target did he achieve on each day?"
- M2.S6.T6.C51 (Example 6, Q): "Days 7 and 8" lacks the percentages and target. Suggested: "On Day 7 Kishanlal achieved 150% of his 5000-rupee target and on Day 8 he achieved 210% of it. Find the sales on these two days."
- M2.S6.T6.C53 (Example 11, Q): "The fraction and decimal table" lacks the nine percentages and the marking instruction (a diagram token will follow the text). Suggested: "Complete the table of fractions and decimals for 90%, 110%, 200%, 250%, 15%, 173%, 358%, 28.9% and 305%. Then mark their approximate places on the 0% to 400% diagram; 90% is marked for you." The table itself should be a LaTeX array in the question text.
- M2.S6.T6.C55 (Example 7, Q): "Wheat harvest" lacks the data. Suggested: "A farmer harvested 260 kg of wheat last year and 650 kg this year. What percentage of last year's harvest is this year's harvest?"
- M2.S6.T6.C46 (Example 5, solution): the steps give no numbers. Suggested steps: "40% is 92 km, so 20% is 46 km. The remaining 60% is three pieces of 46 km = 138 km."
- M2.S6.T6.C48 (Example 6, solution): suggested step "2000/5000 x 100 = 40%, 3500/5000 x 100 = 70%, 5000/5000 x 100 = 100%, 6000/5000 x 100 = 120%" so the numbers are in the solution.
- M2.S6.T6.C36 (free-hand table, solution): the steps "Row by row, easiest column first;" are not a working; the two hints 40% = 4 x 10% and 15% = 10% + 5% are fine.
- Wrong or clashing book numbers (`book_number`): C37/C38 and C35/C36 are both labelled "Example 2", but the book's Free-hand table is an unnumbered "Try" and Example 2 is the FDP Trio (the 10% question and the FDP table both belong to it); C39/C40 (FDP table) is labelled "Example 4" which clashes with C43/C44 "Example 4: Millet"; C49, C51, C53 are labelled "Example 9", "Example 10", "Example 11" but the book has only Examples 1 to 7 (Days 5 and 6, Days 7 and 8 are parts of Example 6; the table and number line is an unnumbered prompt on p.12). Suggested labels: C35 "Free-hand Computations", C39 "Example 2 (FDP table)", C49 "Example 6 (Days 5 and 6)", C51 "Example 6 (Days 7 and 8)", C53 "Percentages beyond 100: table and number line".

All LP answers were recomputed against the book and are correct (30 g and 33.25 g; the 42 table values; the FDP fractions and decimals; 60 marks; 22.22% / 77.78% / 111.1 ml; 138 km and 230 km; 40%, 70%, 100%, 120%; 156% and 191%; 7500 and 10,500; the nine fractions and decimals of C54; 250% = 2.5 times). No solution contradicts the book.

## Where the book itself is unclear or slips (nothing drawn from these)

- Example 4 ratio bar (P09-bar_model-2, p.9): drawn about 0.29 of the width for the millet part instead of 2/9 = 0.22 (2 : 5 looks like), as the base inventory says; confirmed on the page picture. Not drawn (C44 solution is optional). If it is ever drawn, use the correct 2 : 7 proportion (two cells of nine).
- Example 6 Day 1 and Day 2 bars (P11-bar_model-1, -2, p.11): the green fill ends at about 42% and 74% of the width, while the values are 40% (2000) and 70% (3500). A print slip, not drawn (C48 solution optional); a drawing would use exactly 40% and 70%.
- Days 5 and 6 bars (P11-bar_model-5, -6): the green ends at about 1.54 and 1.89 of the 5000 unit against the true 1.56 and 1.91: within pencil accuracy, a drawing would use the exact values.
- Page 12 band (P12-bar_model-1): the 90% arrow is at 0.9 of the first section as the text needs; nothing unclear. The book prints "(0) (1) (2) (3) (4)" under the percentages, kept.
- Free-hand table (p.7) has only four rows; 40% and 15% are asked in prose below it (see LP text issues).

### Chunk C notes (from the decision agent)
# Notes for chunk C (Class 8 Ch 8 "Fractions in Disguise")

Chunk C = topic M2.S7.T7 (Figure it Out Q1 to Q12, section 1.2, book pp. 12-14) and topic M3.S8.T8 (the three worked blocks of concept C82 "Measuring a change"; the book has no figure for them).
Result: 27 items, required 3 / optional 0 / none 24. Required: Q1 question (C57), Q1 solution (C58), Q2 solution (C60). Validator: errors 0, warnings 3 (see end).

## 1. Judgement calls

- **Q1 question (C57) required, one picture.** The book prints three pairs of bar models (pp. 12-13). The LP keeps Q1 as one concept, so there is one question diagram holding rows (i), (ii), (iii). The three base figures P12-bar_model-2, P12-bar_model-3 and P13-bar_model-1 all map to this one item. I checked all three against the page pictures (5, 10 and 4 cells; right spans of 4, 6 and 3 cells; 20%, 60, 75, 90, 140): the base descriptions are right, no CORRECTED entry needed.
- **Q1 colours.** The book uses pink, orange and green bars. The colours carry no meaning, so all bars are INK.
- **Row labels (i), (ii), (iii) are drawn** in the Q1 figures (decision 3) because the LP answer text refers to "(ii)" and "(iii)". Same for the panel labels (i) to (vi) of the Q2 solution figure: the LP answer (C60) refers to the parts by letter.
- **Q1 solution (C58) required, derived_from C57.IMG1.** The answer is the same bar pairs with the four "?" marks filled in (ANSWER green): (ii) 10% and 54, (iii) 25% and 105. Row (i) is worked out in the book and stays as given. Because the solution figure re-uses the three book figures, the inventory has three second-use entries `NEW-P12-bar_model-2-sol`, `NEW-P12-bar_model-3-sol`, `NEW-P13-bar_model-1-sol` mapped to C58 (solution).
- **Q2 question (C59) none.** The book gives no figure; the learner is told to draw the bar models. A question figure would be invented (companion note).
- **Q2 solution (C60) required, one picture with six panels, derived_from null.** The question explicitly asks for bar models, so the drawn models are the answer to that part (v3 B2, ANSWER_IS_FIGURE), although the LP text only says "Each gets a quick bar sketch". The LP did not split Q2 into parts and a pair gets one solution diagram, so the six models sit in one 2 x 3 grid. The book prints no solutions, so the layout is mine; every number is from the LP solution. Cell choices (to avoid fractions of cells where possible): (i) 4 cells of 25% = 40; (ii) 25 cells of 4% = 10, four cells = 40; (iii) 10 cells of 10% = 36, 6.2 cells shaded; (iv) 7 cells of 20% = 8, five cells = 100%, seven = 140% (matches the LP wording "40 + 16"); (v) 10 cells of 10% = 6 min with a 1% strip (0.06 units wide) shaded; (vi) 10 cells of 10% = 1 kg with 70% of cell 1 shaded. Panels (iii), (v), (vi) need partial shading of a cell; this is stated exactly in the spec.
- **Q3 to Q12, question and solution: all none.** No book figure for any of them (Q10 has only a decorative badminton coach, Q8 only the Math Talk icon). Answers are numbers, symbols or short statements.
- **Worked blocks of C82 (units 49, 50, 51) all none (`no_image`).** Tomatoes (12 / 30 x 100 = 40%) and Footfall (60 / 160 x 100 = 37.5%) have no figure in the book. The bar model of the Rs 30 to Rs 42 rise already exists as the teaching image `M3.S8.T8.C82.IMG1`; it is never linked. Block 2 is the "Check my thinking" multiple-choice item (a shirt falls from Rs 500 to Rs 400, answer 20%): text only, the confidence faces are not a figure.
- **Figures not claimed by chunk C.** P15-label-1, P15-label-2 and P15-table-1 (Know Your Contents, p. 15) sit in topic M3.S8.T8's book pages but are the given figures of the question of unit 53 (M3.S9.T9.C85, chunk D), so I left them to D. P11/P12 Day 7-8 table and bar (P12-table-1, P12-bar_model-1) belong to chunk B (units 34, 35). The badminton coach (p. 14) and the Math Talk icon (p. 13) are decoration and are not in the base inventory; I did not add them.

## 2. LP text issues

(Nothing was edited; each is a suggestion.)

- **M3.S8.T8.C82, block 0 (Tomatoes):** the question is only the word "Tomatoes" and the step "12 over the old price 30." omits the new price. Suggested question: "The price of 1 kg of tomatoes was Rs 30 three years ago and is Rs 42 now. Find the percentage increase." Suggested step: "Increase = 42 - 30 = 12; 12 over the old price 30 gives 12/30 x 100."
- **M3.S8.T8.C82, block 1 (Footfall):** same problem. Suggested question: "The average footfall in a theatre was 160 before COVID and is 100 now. Find the percentage decrease." Suggested step: "Decrease = 160 - 100 = 60; 60 over the old footfall 160 gives 60/160 x 100."
- **M3.S8.T8.C82, block 2 (Check my thinking):** the learner-visible text ends with "Act on the diagnosis table.", an authoring instruction; remove it. The block also has no `steps` / `answer` fields (the answer "(b), reason (ii)" is only inside `text`).
- **M2.S7.T7.C57 (Q1 question):** the question text carries a parenthesis describing the figure ("Pairs of bar models: (i): 5 cells, one cell = 20% ..."). It reads like an authoring note and repeats the new diagram. Suggested question: "1. Find the missing numbers. The first problem has been worked out."
- **M2.S7.T7.C60 (Q2 solution):** the only step is "Each gets a quick bar sketch." and says nothing about what the sketches show. Suggested step (it now follows the six-panel figure): "In each bar, split the whole into equal cells and shade the cells that make the asked share."
- **M2.S7.T7.C66 (Q5 solution), part (iv):** "the $AI$ checks them" is internal wording in a learner answer, and `$AI$` in LaTeX is set as a variable. Suggested: "(iv): Any two questions of the same kind, with their answers, are fine."
- **M2.S7.T7.C78 (Q11 solution):** "The $AI$ uses the current year's figure if the student looks it up." has the same problem. Suggested: "Use the latest world population the student finds; with 8.2 billion (2025) the answer is about 7.4 billion."
- **M2.S7.T7.C67 (Q6 question):** `question_tex` writes "(ii)" without the colon that (i) and (iii) have: "(ii) \underline{...} is 40% of 4." Suggested "(ii):".
- The LP numbers checked out against the mathematics for Q1 to Q12 (for example 29% of 43 = 12.47, 92% of 110 = 101.2, 1% of 168 h = 1.68 h = 100.8 min, shown as "about 101"); no solution contradicts the book.

## 3. Borderline

- Q1 question: kept `required` although the LP question text carries every number (decision 4); the figure is the book's given figure and the learner fills its "?" marks.
- Q2 solution: `required` on the strength of "also draw their bar models"; the LP text alone would not need a figure.
- Q3 (3/4 of 60 ml), Q9 (20% takes 18 days), Q10 (10 : 80 : 10 of 90 minutes), Q12(ii) (40 : 40 : 20 of 2 kg) and the worked blocks Tomatoes and Footfall: a bar model would be natural, but the book draws nothing, the question gives no figure and the numbers are one-step arithmetic, so `none` (tie-breaker). If more pictures are wanted, Q10 and Q3 (solution side) are the first candidates, then the Tomatoes worked example.
- Q4: the book says "Visualising or estimating can help" but gives no figure and the answers are symbols: `none`.
- Q5(iv) and Q7 ("Create such questions", "Make 2 more") are partly open-ended; the closed parts decide, `none`.

## 4. Book unclear

- Nothing contradictory in the Q1 figure. The page images carry the "(c) NCERT not to be republished" watermark; it is not part of any figure.
- This pdf has no printed solutions, so there are no printed-answer pictures; the Q1 and Q2 solution figures are built from the LP solution text.

## Validator warnings (accepted)

- Two `visible_text` strings of the Q2 solution have more than six tokens ("1% = 0.6 min = 36 s", "7% = 0.7 kg = 700 g"): each is one label line of a bar model.
- M2.S7.T7.C60 (solution) has no base-inventory figure mapped, as the figure is not printed in the book.

### Chunk D notes (from the decision agent)
# Notes, chunk D (Class 8 Ch 8 "Fractions in Disguise")

Units: M3.S9.T9 (Examples 1, 2, 3), M3.S10.T10 (four Figure it Out questions), M3.S11.T11 (six worked blocks C97, C98, C99, C101, C102, C104).
Result: 20 items, required 0 / optional 0 / none 20. Validator: errors 0, warnings 0.

Nothing in this chunk needs a drawn diagram under the v3 rules: every figure of the chunk is a plain table or list of numbers, or a teaching figure that already exists as a concept image, and every question and solution is arithmetic or word reasoning. Every `none` item carries reason codes, a one-line reason and, where it helps, a `text_alternative`.

## Figures claimed (6)
- P15-label-1, P15-label-2 (the two badam pack labels), P15-table-1 (table to complete): `none:LATEX_TABLE`. Values re-read on the enlarged page picture: DEF 99, 30, 12, 9 g, total 150 g; Zacni 272, 64, 40, 24 g, total 400 g; table shows only 66% under DEF Sugar.
- P16-flow_diagram-1 (sweater journey): `concept_image:M3.S11.T11.C97.IMG1` (the concept image shows exactly this figure and its price tags).
- P18-bar_model-1 and P18-bar_model-2 (Manisha's two bars): both `concept_image:M3.S11.T11.C101.IMG1` (that one image holds both bars).
- Base descriptions of all six agree with the page pictures; no "CORRECTED" entries.

Figures next to my units that I did NOT claim, because their book section is a unit of chunk E (merge check will see them there): P17-bar_model-1 (Example 4, Kishanlal's percentage profit, C105), P17-bar_model-2 (Example 5, Raghu's rice, C113), P19-receipt-1 (Example 9, "check the bill", C121). If chunk E does not claim them, the merged map will report them as unclaimed.

## Borderline
1. M3.S9.T9.C85 (Example 2 question, KYC table): `none`, LATEX_TABLE + DECORATIVE_ONLY, `needs_lp_text_sync: true`. The data lives only in the book picture, so this is the call most open to challenge. I judged the two labels as plain ingredient/weight lists (no colour, position or arrows carry meaning; the pouch, almonds, barcode and how-to-use strip are decoration), the same kind of thing as the number lists the audit removed, and the table to complete is a plain table like P07/P08/P12. If you want the labels drawn instead, the figure would be one 16:9 `other` diagram with two label cards (DEF and Zacni, ingredient names and grams, total weight line) plus the table with 66% in the DEF Sugar cell, and the solution a derived diagram with the other 7 cells in ANSWER green. Say so and I will write the spec.
2. M3.S9.T9.C86 (Example 2 solution): `none`. A filled percentage table is a numeric table (LATEX_TABLE), not ANSWER_IS_FIGURE. Consistent with the question side.
3. M3.S11.T11.C97 (Kishanlal's profit): `none`. Numbers are in the book text, answer is 430 - 300 = 130, and the sweater journey is this concept's own teaching image (never linked).
4. M3.S11.T11.C98 (crayon box, check my thinking): `none`. Multiple choice in words; the book draws nothing for it; the five-part ₹10 bar is the teaching image C98.IMG1.
5. M3.S11.T11.C102 (Manisha, 50% or 33.33%): `none`. The book draws two bars, but they are teaching figures (concept image C101.IMG1) and the example does not refer to them; the numbers are three simple fractions. An optional two-bar picture (₹250 over ₹500 = 50%, over ₹750 = 33.33%) would help but only repeats C101.IMG1, so I did not mark it optional.
6. M3.S10.T10 (all four pairs): `none` on both sides, consistent with each other (no figure in the book, solutions are one or two lines of arithmetic).

## LP text issues
(No LP text was edited; no decision was changed because of these.)
- M3.S9.T9.C83 (Example 1 question): text is only "Eesha: English or Science?"; the marks are missing. Suggested: "Eesha scored 42 out of 50 in English and 70 out of 80 in Science. She lost only 8 marks in English but 10 in Science, so she thinks she did better in English. Reema says Science, since she scored more marks there. Vishu says the scores cannot be compared because the maximum marks differ. Who is correct?"
- M3.S9.T9.C85 (Example 2 question): text is only "$KYC$ table", with no label data and no table. Suggested: "DEF pack (total 150 g): sugar 99 g, milk solids 30 g, badam powder 12 g, food chemicals 9 g. Zacni pack (total 400 g): sugar 272 g, milk solids 64 g, badam powder 40 g, food chemicals 24 g. Complete the table of percentages (DEF sugar is 66%): which product has the larger share of badam, which the smaller share of food chemicals?" (a LaTeX array for the table is in the item's `text_alternative`). Also KYC should be plain text, not math mode.
- M3.S9.T9.C86 (Example 2 answer): `answer_tex` has "$(6$%)" (the bracket is opened inside the math and closed outside); write "(6%)" as "($6$%)". Values checked: 99/150, 30/150, 12/150, 9/150 = 66, 20, 8, 6; 272/400, 64/400, 40/400, 24/400 = 68, 16, 10, 6; both rows add to 100.
- M3.S9.T9.C87 (Example 3 question): the two statements are missing. Suggested: "(i) The population of this state in 1991 is 165% of that in 1961. (ii) The population of this state has increased by 65% from 1961 to 1991. Do the two statements mean the same thing?"
- M3.S10.T10.C90 (petrol answer): the learner text shows an internal code, "(M_2)" / "(M2)". Suggested: "Option (ii), 40%, is wrong: it takes the new price (₹100) as the base instead of the old price (₹60)." Also "About 66.66%" is 66.67% rounded; the book's option (iv) prints 66.66%, so keep the LP wording but it is a truncation.
- M3.S10.T10.C96 (cameras answer): explains only why (v) is wrong, but (i), (ii), (iv), (v) and (vi) are all wrong. Suggested: "Only (iii). After an 85% fall, 15% is left, so now is 15% of a decade ago. (i) uses 85% as what is left. (ii), (iv), (v) turn the base around: a decade ago was about 667% of now (1/0.15), not 85%, 15% or 185%."
- M3.S11.T11.C97 (Kishanlal's profit): no numbers in the block. Suggested: "Kishanlal buys a sweater at ₹300 (cost price) and sells it at ₹430 (selling price). What is his profit?" and step "430 - 300 = 130".
- M3.S11.T11.C98 (crayon box): the unit's ncert_refs says "1.3.ex5_per_kg", which is Raghu's rice; the crayon question is the unnumbered one on p.17. The block text also holds tutor wording ("How sure are you?" with three emoji, "Act on the diagnosis table.") that reads as a script, not learner text. The option arithmetic is consistent: (a) 37.50 = 50 - 12.50, (b) 40 = 50 / 1.25, (c) 62.50 = 50 + 12.50.
- M3.S11.T11.C99 (Per kg?): the question gives no data. Suggested: "Raghu bought rice at ₹35 per kg and sold 10 kg for ₹300, that is ₹30 per kg. Is the percentage loss per kg the same as the loss on all 10 kg?" LP answer "about 14.29%" is the correct rounding of 5/35 = 50/350 = 14.2857; the book prints 14.28% in Example 5 (see below).
- M3.S11.T11.C101 (gross and net profit): no data in the block. Suggested: "Kishanlal's sales last month were ₹80,000; the goods he sold cost ₹48,000; his other expenses were ₹8,000. Find the gross profit and the net profit." Checked: 32,000 and 24,000.
- M3.S11.T11.C102 (Manisha): no data in the block. Suggested: "Manisha buys a bag of fertiliser at ₹500 and sells it at ₹750. Is her profit 50% or 33.33%? In a month her sales are ₹1,50,000, the goods cost ₹1,00,000 and expenses are ₹5,000: what percent of the monthly revenue is her net profit?" Checked: 250/500 = 50%, 250/750 = 33.33%, 45,000/1,50,000 = 30%.
- M3.S11.T11.C104 (A Bill from Home): the "answer" is a tutor instruction ("Open; the AI checks the student's bill"), not learner text. Worth rewording or hiding.

## Places where the book itself is unclear or inconsistent
- Page 15: the Zacni pack brand is hand-lettered "Zachi", while the table and text say "Zacni". Same product; I kept "Zacni" everywhere.
- Pages 19 and 20: Figure it Out numbering repeats. Page 19 lists questions 1 to 5 and page 20 starts again at 3 (3 to 9), so "3", "4" and "5" each occur twice. The LP book_number "5" is used for both the petrol question (p.19) and the rice question (p.20). I used the page in `ncert_ref` to tell them apart.
- Option (iv) of the petrol question prints 66.66%, the exact value is 66.666...%; the book intends (iv) as the answer.
- Example 5 (chunk E) prints 14.28%; the exact value is 14.2857...%, which rounds to 14.29%, as the LP says.
- Page 16, Example 3: the two derivations sit in two columns split by a vertical rule. This is equations, not a figure, so there is no inventory entry for it.
- Pictures seen but not inventoried (decoration, no mathematical content): badminton player (p.14), the two children with speech bubbles (p.15), the "30% SALE" clothing-store drawing (p.18, discount section, chunk E), the "Try This" icon (p.19).

### Chunk E notes (from the decision agent)
# Chunk E notes: topic M3.S12.T12 "Questions: Example" (units 65-73, 18 items)

Result: required 5 / optional 2 / none 11. Validator: errors 0, one warning (C116, see Borderline: the figure is not printed in the book).

| Unit | Concepts | Question side | Solution side |
|---|---|---|---|
| 65 Kishanlal's profit % (book Ex 4) | C105 / C106 | none | REQUIRED (bar, CP = 100%) |
| 66 Wholesaler and manufacturer | C107 / C108 | REQUIRED (sweater journey) | none |
| 67 Notebooks | C109 / C110 | none | none |
| 68 Crayons | C111 / C112 | none | optional (not added) |
| 69 Raghu's loss % (book Ex 5) | C113 / C114 | none | REQUIRED (bar) |
| 70 Damaged vase (book Ex 6) | C115 / C116 | none | REQUIRED (bar, borderline) |
| 71 Strawberries | C117 / C118 | none | optional (not added) |
| 72 Cooker | C119 / C120 | none | none |
| 73 Is the bill correct? | C121 / C122 | REQUIRED (receipt) | none |

Figures claimed (5): P16-flow_diagram-1 (concept image M3.S11.T11.C97.IMG1), NEW-P16-flow_diagram-1-q (item C107 question), P17-bar_model-1 (C106 solution), P17-bar_model-2 (C114 solution), P19-receipt-1 (C121 question). I checked all four base descriptions against page_16, page_17 and page_19 (zoomed on the receipt and the price tags): they are correct, no CORRECTED entries. P18-bar_model-1/2 (Manisha, teaching figures) are not claimed: no unit of this chunk uses them (chunk D's units 62/63 do). The clothes-shop "SALE 30%" picture on p.18 is decoration (not in the base inventory, skipped per Step 0).

Merge hint: P16, P17-bar_model-1, P17-bar_model-2 and P19-receipt-1 also sit in book sections of chunk D units (59 "Kishanlal's profit", 61 "Per kg?", 64 "A bill from home"). I claim the base ids for my items; if D also uses one of these figures for an item of its own, one of us needs a `NEW-<id>-<suffix>` entry. For P16 I claimed the base id as concept_image C97.IMG1 (the teaching use, same meaning D should give it) and a separate NEW- entry for my question item.

## 1. Judgement calls

- **C107 question, sweater journey: required.** The book's question ("Find the profit percentage of the wholesaler and the manufacturer") has no numbers; the cost and selling prices of the manufacturer (230 / 253) and the wholesaler (253 / 300) exist only in the p.16 picture, and the LP question text is just the title "Wholesaler and manufacturer". DATA_IN_FIGURE plus the tie-breaker (a careful student cannot attempt it from the text). The picture is also teaching image C97.IMG1, but v3 says a teaching image is never linked, so the item gets its own figure. I did not use the 'refer picture' exception (question optional): that exception is for a book answer that only points at a picture, and the book here has no printed answer and the question text carries no data. Figure = boxes and price tags only; the book's illustrations of workers, vans and shoppers are decoration and are left out. All three tags are drawn (the book gives all three), each tag under the arrow leaving the seller it belongs to.
- **C106 and C114 solutions (Examples 4 and 5): required.** The book prints a rough bar with each example as the worked solution (CP = 100%, the profit or loss beyond or inside it). v3 B2: a printed solution picture makes the solution side required; and the picture changes how correctly a student reads "which base": the LP steps "130 over the CP of 300" and "50 over the CP of 350" only say it in words. The question sides have no figure (the book question is text only; the card text of C105 even said "No diagram is needed"), so the solution figures draw the whole bar (derived_from null) with the answer percentage in ANSWER green.
- **Example 4 bar: the book's "?" is not drawn.** The book puts "?" under the 430 line (which would literally be 143.33%, the selling price as a percentage of the cost) while its answer 43.3% belongs to the 130 part. To keep a clean final state without adding a number that is in neither the LP nor the book, the 430 line has no bottom label and the 130 part gets its own ANSWER arrow "43.33%".
- **Example 5 bar: "300" added above the middle line.** The book leaves that line unlabelled above although 300 is in its text; the final-state figure needs it. 100% sits under the 350 line (the cost price is the base), as in the book.
- **Percentage numbers follow the LP.** Example 4: LP 43.33% (book prints 43.3%, one decimal). Example 5: LP 14.29% (book prints 14.28%, see "Book mistakes").
- **C108 (wholesaler / manufacturer solution): none.** Two fractions of numbers that are already on the question figure; the book prints no solution picture. (The LP video draws cost-price bars, but the video is not this job.) Not made optional-with-bars because Examples 4 and 5 have a printed bar and these do not.
- **C122 (bill solution): none.** The check is 9% of 450 twice and a sum; it adds nothing visual. Highlighting the tax lines would only make it nicer (optional at most, not needed).
- **C112 crayons and C118 strawberries solutions: optional, not added.** A bar (CP = 100%, SP = 125% or 88%) would help the reverse-percentage step, but the book prints none and does not ask the student to draw one. C98.IMG1 (a teaching image) already shows the crayon bar.
- **C110 notebooks and C120 cooker: none.** Plain arithmetic, no figure in the book.
- **Question sides of C105, C109, C111, C113, C115, C117, C119: none (TEXT_SUFFICIENT).** The book question of each is text with its numbers in words. The LP question texts are bare titles (see LP text issues): I did not change a decision for that.
- **C121 receipt aspect.** The receipt is a little taller than wide; the pipeline draws 16:9 cards, so the paper (760 x 900 px) is centred on a 1920x1080 card. Bulb logo of the book receipt left out (decorative); the stray full stop after "Price" in the book is not drawn. The receipt's arithmetic is correct (3 x 150 = 450; 9% of 450 = 40.50 twice; 450 + 81 = 531), so no correction needed.
- **Colour use.** House tokens only (book yellow/red replaced by MARK_FILL / INK). In C116 the values the solution works out (2173, 477, 82%) are ANSWER green and the given ones (2650, 18%, 0, 100%) INK; in C106 / C114 only the final percentage is ANSWER.

## Borderline

1. C107 question: required vs optional ('refer picture' exception). Chose required (reasons above).
2. C106 and C114 solutions: required vs none/optional (the bar restates numbers the LP text carries). Chose required per v3 B2 (printed solution picture) and user decision 4.
3. **C116 (vase) solution: required although the book prints no figure.** The book says right after Example 6: "Try making an estimate. Draw a rough diagram depicting the given situation", then shows two methods ("keep 82%" / "subtract 18%"). The answer to that prompt is a drawing (ANSWER_IS_FIGURE) and Examples 4 and 5 directly above have the same kind of bar printed (sibling consistency), so the solution draws that rough bar: buying price 2650 = 100%, loss 18% = 477, selling price 82% = 2173. All numbers are on book p.18 or in the LP solution. If the user would rather draw only what the book prints, flip C116 to optional (action drop_image) and delete its diagram; nothing else depends on it. This is the only required item with no inventory figure behind it (hence the validator warning).
4. C112 / C118 optional (not added) while C116 is required: the difference is the book's explicit "draw a rough diagram" prompt for the vase.
5. C121 solution none vs optional (circle the CGST / SGST lines): chose none.

## 2. Book mistakes (spec shows the corrected value)

- Example 5 (Raghu): the book prints the loss percentage as 14.28% (50/350 = 14.2857..., cut off instead of rounded). The LP says 14.29%, which is right. The base inventory keeps what the book prints (it does not print the percentage inside the picture); the spec, `visible_text` and `manim_description` use 14.29%, and `must_not_show` lists 14.28%.
- Example 4: the book prints 43.3% (rounded to one decimal; 130/300 = 43.33%). Not an error, but the spec uses the LP's 43.33%.

## 3. Places where the book itself is unclear

- Example 4 bar: the "?" under the 430 line (see Judgement calls).
- Shambhavi's notebooks: "200 page notebooks at ₹36 per book ... Find the selling price" means notebooks of 200 pages; it does not say "per notebook" (the LP answer is ₹43.20 per notebook, i.e. 36 x 1.2).
- "Profit margin of 20% / 25%" does not say with respect to what; the chapter's Figure it Out Q1 says "with respect to the cost", and the LP answers follow that.
- The sweater picture's tags are not labelled with whose prices they are; reading them as the seller to the left of each arrow fits the chain (each SP equals the next CP: 253, 300) and the LP's own q_figure text.
- Example 6: the book asks the student to draw a rough diagram but prints none.

## LP text issues (not changed, only listed)

Concept id, what is wrong or missing, suggested sentence.

- **M3.S12.T12.C105** question "Kishanlal's profit %": no data (cost 300, selling price 430). Suggest: "Kishanlal buys a sweater for ₹300 and sells it for ₹430. Find his percentage profit."
- **M3.S12.T12.C106** step "130 over the CP of 300.": does not say where 130 comes from. Suggest: "Profit = ₹430 − ₹300 = ₹130, and the cost price (₹300) is the 100%, so the profit is 130 over 300."
- **M3.S12.T12.C107** question "Wholesaler and manufacturer": no data; everything is in the picture. Suggest: "Use the prices in the picture. Find the profit percentage of the wholesaler and of the manufacturer." (the answer lists wholesaler first, then manufacturer: keep that order.)
- **M3.S12.T12.C108** steps "47 over 253; 23 over 230.": not said which is which or where 47 and 23 come from. Suggest: "Wholesaler: profit 300 − 253 = 47 over the CP 253. Manufacturer: profit 253 − 230 = 23 over the CP 230."
- **M3.S12.T12.C109** question "Notebooks": no data. Suggest: "Shambhavi buys 200-page notebooks at ₹36 each and sells them with a profit margin of 20%. Find the selling price of one notebook."
- **M3.S12.T12.C110** step "36 × 1.2.": Suggest: "20% profit on the cost: selling price = 36 × 1.2 = ₹43.20 per notebook."
- **M3.S12.T12.C111** question "Crayons": no data. Suggest: "Shambhavi sells crayon boxes at ₹50 each with a profit margin of 25% on the cost. At what price did she buy one box from the wholesaler?"
- **M3.S12.T12.C112** step "50 ÷ 1.25.": Suggest: "The selling price ₹50 is 125% of the cost price, so cost price = 50 ÷ 1.25 = ₹40."
- **M3.S12.T12.C113** question "Raghu's loss %": no data. Suggest: "Raghu bought rice at ₹35 per kg and sells 10 kg for ₹300. Find his percentage loss."
- **M3.S12.T12.C114** step "50 over the CP of 350." and the answer text: the step does not show 10 x 35 = 350 and 350 − 300 = 50; the answer carries a parenthetical "(the book shows 14.28%, cut off rather than rounded)" that a learner will read as part of the answer. Suggest: "Cost = 10 × ₹35 = ₹350; loss = ₹350 − ₹300 = ₹50; loss over the CP: 50 over 350." and move the book remark to a teacher note.
- **M3.S12.T12.C115** question "Damaged vase": no data. Suggest: "Shyamala bought a decorative vase for ₹2650. It is slightly damaged and she sells it at a loss of 18%. How much does she get? Try drawing a rough diagram first."
- **M3.S12.T12.C116** step "Keep 82% of 2650, or subtract 18% of it.": Suggest: "Two ways: 82% of 2650 = 0.82 × 2650 = 2173, or 2650 − (18% of 2650 = 477) = 2173."
- **M3.S12.T12.C117** question "Strawberries": no data. Suggest: "Snehal sells strawberries at ₹80 per kg and makes a 12% loss. What was the cost price per kg?"
- **M3.S12.T12.C119** question "Cooker": no data. Suggest: "A cooker with MRP ₹1800 is sold at a 35% discount. What is the selling price? If the cost price was ₹900, what is the percentage profit?"
- **M3.S12.T12.C120** step 2 "profit 270 over 900": does not show 1170 − 900 = 270. Suggest: "Step 2 base is the CP: profit = 1170 − 900 = 270, so 270 over 900."
- **M3.S12.T12.C121** question "Is the bill correct?": the bill exists only in the figure (that is why the figure is required); fine once the figure is added, but "Check if the calculations on the bill are correct." matches the book better.
- **Concept names and book numbers**: C105/C106 are named "Example 4" and C111/C112 also "Example 4"; C107/C108 "Example 2", C109/C110 "Example 3", C117/C118 "Example 7", C119/C120 "Example 8", C121/C122 "Example 9". In the book only Kishanlal (Ex 4), Raghu (Ex 5) and the vase (Ex 6) are numbered; the wholesaler/manufacturer, notebooks, crayons, strawberries, cooker and bill items are unnumbered "?" prompts, and the book's real Examples 7, 8 and 9 (the ₹6000 deposit, the total received, compounding) are later in the chapter (chunk F). The labels clash with those. Suggest names such as "Try this: wholesaler and manufacturer", "Try this: notebooks", "Try this: crayons", "Try this: strawberries", "Try this: cooker", "Try this: the bill".

### Chunk F notes (from the decision agent)
# Notes, chunk F (Class 8 Ch 8 "Fractions in Disguise", plan cbse_eng_maths8_ch8_v56)

Units: M3.S13.T13 (8 pairs, Figure it Out of 1.3), M4.S14.T14 (2 worked blocks: C139, C140), M4.S15.T15 (5 pairs: Example 7, Example 8, Math Talk, Example 10, Example 11). 28 items.

Result: required 1 / optional 1 / none 26. Validator errors 0, warnings 0.

- required: M4.S15.T15.C144 (solution of Example 7), media id `M4.S15.T15.C144.IMG1`, one 16:9 card with both year-by-year tables.
- optional (not added): M4.S14.T14.C139 worked example (book's bar model, 100% to 110%).
- none: all 8 Figure it Out pairs (16 items), C140 check-my-thinking, and the Example 7 question, Example 8, Math Talk, Example 10, Example 11 (both sides).

Pages looked at: 19, 20, 21, 22, 24, 25 (and the p.21 bar diagram at 3x zoom). The Figure it Out pages (19, 20), p.24 and p.25 hold no figure for my items; the only pictures are on p.21 and p.22 (plus p.23, see below).

## 1. Judgement calls

1. **Example 7 solution (C144): required.** The book's worked solution of Example 7 is two annotated year-by-year tables (Option 1 interest paid out; Option 2 interest added back, with x 0.10 and x 1.10 arrows). A filled table that is the answer counts as ANSWER_IS_FIGURE (B2). The LP solution has only "Option 1: 1800 + 6000 / Option 2: x 1.1 three times", so the yearly interest (600, 660, 726) and amounts (6600, 7260) exist only in the picture. Both tables go on ONE card (a pair gets one solution diagram). Teaching image M4.S14.T14.C140.IMG1 shows the same story but is never linked; the item has its own diagram. The two base figures P21-table-1 and P22-table-1 both map to this item.
2. **Example 7 question (C143): none.** The question gives no figure ("a question with no given figure gets no question diagram"), so the solution diagram has `derived_from` null.
3. **Example 8, Math Talk, Example 10, Example 11 solutions: none.** Their printed solutions are two-column arithmetic or formulas in words, not figures. Sibling consistency inside T15: only Example 7's printed solution is a picture, so only that one is drawn.
4. **Figure it Out (T13): all none.** No question has a given figure on p.19-20 and no answer is a picture. Word problems with numbers in the text (TEXT_SUFFICIENT) and arithmetic answers (LATEX_ARITHMETIC).
5. **C140 "Check my thinking": none.** Multiple choice in words and numbers. The concept's teaching image (C140.IMG1) stays untouched.
6. **Figures P23-annotated_expression-1 and -2 claimed by this chunk** (mapped `none:LATEX_ARITHMETIC`). They are the Example 9 expressions on p.23, which sit in concept M4.S14.T14.C141 ("Writing the pattern with letters"). C141 is in my topic T14 but has no question or worked unit in any chunk, so nobody else would claim them. If another chunk also claims them it should use the same meaning (LaTeX lines).
7. **Tags "Option 1" / "Option 2" in the Example 7 diagram.** Rule 4 of section 4 says no headings, but allows tags of at most 3 words that the LP solution text uses; the LP solution says "Option 1" and "Option 2". They are the only text outside the tables. A reviewer who reads the rule more strictly can delete both tags; the column headers ("Interest returned" and "Interest added back") already tell the tables apart.
8. **Colours in the Example 7 diagram.** No question figure exists, so the whole figure is drawn by the solution: table text INK, arrows FOCUS (x 0.10) and SET_A (x 1.10), only the two final totals (7800 and 7986) in ANSWER.

## Borderline

- **C144 required vs LaTeX arrays.** The tables are plain numbers, so a LaTeX array would also work. I kept it as a figure because the printed answer IS this picture and the arrows (x 0.10, x 1.10) carry the idea of "interest grows because the base grows". If the content team prefers arrays, the item becomes `none` (LATEX_TABLE) and the two figures map to `none:LATEX_TABLE`.
- **C139 optional vs none.** The book's rough bar diagram (principal = 100%, interest 10%, amount = 110%) would help, but no Step-B trigger holds: the data is in the steps and answer, the question names no figure, and the figure is a teaching figure with no concept image in the plan. Marked optional (reason says which figure). If it is ever drawn: principal line 6000 (100%), 10% = 600, amount 6600 (110%), long arrow "Amount after 1 year" spanning from 0 to the right-hand line (see section 3).
- **Figure it Out Q3 (company, C127/C128), Q6 (election, C133/C134), Q8 (milkman, C137/C138):** a bar or table picture could help the reader but would only make it nicer; kept none.

## 2. LP text issues

Only listed, nothing changed (decision 2 of 23 Nov).

T13 (Figure it Out):
- **C131 / C132, C133 / C134, C135 / C136, C137 / C138:** the LP copies the book's printed question numbers (3, 4, 6, 7). On p.20 the book restarts numbering at 3 (a print slip: it follows 5, so these are 6, 7, 9, 10 in sequence of the set), so the plan shows "3." twice. Suggested: drop the printed number from `question_tex` or use the corrected 6, 7, 9, 10 (and the book_number fields likewise).
- **The set also has four questions that are not in my units:** printed 5 on p.19 (petrol price rise, 6 options), printed 5 on p.20 (rice inflation 38 to 42), 8 (elephants, p x 1.05) and 9 (cameras, demand fell by 85%). Please check they exist elsewhere in the plan (they do not appear in chunk F).
- **C124 (Ans1):** the steps are only "Profit over cost." Suggested: "Profit = 110 - 75 = 35. Profit margin on cost = 35/75 x 100, about 46.67%."
- **C128 (Ans3):** steps and answer contain teacher-facing text: "Discuss the base first.", "(see 4.4)", "Accept either when the student names the base; a good 4.4 check." Suggested: "Margin on revenue: profit = 25% of 2.5 crore = 0.625 crore, so costs = 2.5 - 0.625 = 1.875 crore. If the margin were taken on cost, cost = 2.5 / 1.25 = 2 crore."
- **C136 (Ans7):** the answer ends "...which is 72; M4". The misconception code "M4" has leaked into learner text. Suggested: "90 / 1.2 = 75 (not 90 - 18 = 72, because 18 is 20% of 90, not of the number)."
- **C138 (Ans8):** the only step is "The topic's one faded multi-step problem (see faded ladder below)." This is not a solution. Suggested: "Buffalo 1 (profit 5%): cost = 80,000 / 1.05, about 76,190. Buffalo 2 (loss 10%): cost = 80,000 / 0.9, about 88,889. Total cost about 1,65,079; total selling price 1,60,000; loss about 5,079, which is about 3.08% of the cost." (checked: 5079.37 / 165079.37 = 3.077%).
- **C125:** `question` says "I am a carpenter", `question_tex` says "You are a carpenter" (small mismatch; the book has "I").

T14:
- **C139 (worked example):** the question text is only "Interest and amount after 1 year"; the data (6000, 10% p.a., 1 year) appears only in the steps. Suggested: "A bank pays 10% p.a. on a fixed deposit. If 6000 rupees is deposited for 1 year, what is the interest and what is the amount after 1 year?"
- **C140 (check my thinking):** the text ends "Act on the diagnosis table." (an internal instruction in learner text). Answer (b) 1100 is right: year-2 interest is 10% of 11,000.

T15:
- **C143 (Example 7 question):** the text is only "Example 7". Missing: "If one deposits 6000 rupees in the bank at 10% p.a., what is the amount after 3 years? Option 1: the interest is paid out every year. Option 2: the interest is added back (compounding)." The rate 10% p.a. appears in neither the question nor the solution text; the diagram shows it (from the book).
- **C144 (Example 7 answer):** "7800 against 7986" has no labels. Suggested: "Option 1 (interest paid out): 7800. Option 2 (compounding): 7986."
- **C145 (Example 8 question):** only "Example 8". Suggested: "What percent is the total amount received of the amount deposited (6000), in both options of Example 7?"
- **C147 / C148:** named "Example 3: Q / Ans" (and book_number "Example 3: Compounding: total interest in both options"), but this is the Math Talk on p.24, not an Example 3 (the book's Example 3 is on p.16). The question text "Math Talk: total interest" lacks the question. Suggested: "What is the formula for the total interest at the end of the maturity period, for each of the two options (without compounding and with compounding)?"
- **C149 (Example 10 question):** only "TV value after 1 year", no data. Suggested: "A TV is bought at 21,000 rupees. After 1 year its value depreciates by 5%. Find the value of the TV after one year."
- **C151 (Example 11 question):** only "Village after 3 decades", no data. Suggested: "The population of a village is reducing by about 10% every decade. If the current population is 1250, what is the expected population after 3 decades?"
- **C152 (Example 11 answer):** "About 911, i.e. around 910" is fine, but the book shows two routes (911.25 without rounding, 912 rounding each step) before saying "around 910"; the LP states only the first.

## 3. Where the book itself is unclear or wrong

- **p.20 numbering:** the Figure it Out set is numbered 1 to 5 on p.19 and then 3 to 9 on p.20 (print slip; see section 2).
- **p.21 bar diagram (P21-bar_model-1):** prints "1000" above the principal line although the principal is 6000 (the text above it says 6000 and 600). The diagram is not drawn (optional item), so nothing is corrected in a spec; the base inventory keeps what the book prints. Also the long arrow "Amount after 1 year" stops short of the "?" line (the base inventory's doubt); it should span 0 to "?". Both points matter only if someone draws it later.
- **p.22 Option 2 table (P22-table-1):** the third year's "726" has no "added back" caption (years 1 and 2 have it). Kept as printed in the Example 7 diagram (stated in its `render_note`). Not a mathematical error.
- **Growth label:** the book writes "x 1.10" on the compounding arrows, the LP writes "x 1.1". The diagram follows the book.
- All inventory descriptions of P21-table-1, P22-table-1, P23-annotated_expression-1/-2 matched the page pictures; none needed "CORRECTED".
- Recomputed in the spec: Option 1 interest 600 x 3 = 1800, total 7800; Option 2 6000 -> 6600 -> 7260 -> 7986, interest 600, 660, 726 (each Ending = Beginning + interest). The LP answers of every unit with a numeric answer were recomputed and are right (46.67%, 712.50, 1.875 crore or 2 crore, 225, 5,17,647, 31.25% and 4 candidates, 75, loss about 5,079, 130% and 133.1%, 19,950, 911.25).

### Chunk G notes (from the decision agent)
# Chunk G notes: Class 8 Ch 8 "Fractions in Disguise" (plan cbse_eng_maths8_ch8_v56)

Topics: M4.S16.T16 (Figure it Out Q1-Q9 of Growth and Compounding, 9 pairs), M4.S17.T17 (Tricky Percentages, 9 worked blocks over C171-C174), M4.S18.T18 (Putting It All Together, 3 worked blocks C175-C177).
30 items: required 1 / optional 1 / none 28. Output: `map/out_G.json`, validator `errors 0, warnings 0`.

Result in one line: the only figure this chunk needs is the Peaceful Knights board (C177). The book prints no figure for Figure it Out Q1-Q9 or for any of the money/percent worked examples; everything else is arithmetic with the numbers in the text.

## Borderline

1. **M4.S18.T18.C177 (Peaceful Knights), required, worked example.**
   - Which picture: a worked example has ONE diagram (after the question text). The book's given figure is an empty board; I drew the board WITH the example's 8 knights placed (final state), because the whole content of the example is the arrangement and an empty board adds nothing a learner cannot picture from "chess board". The v3 solution-figure-first convention supports showing the finished state before the steps. If the user wants the strict "given figure only" reading, the alternative is the same board with no knights (visible_text becomes empty).
   - Board size: see "Book mistakes" below (8 x 8, not the book's 10 x 10).
   - The book's small 5 x 5 knight-move board (P32-chess_board-2) is not drawn: the move rule is written in the book text, so `none:TEXT_SUFFICIENT`. The LP question text does not carry that rule (see LP text issues), so if the LP text is not fixed, that picture is the one a learner would miss.
   - Dark squares are drawn GUIDE grey (the "unused" colour), knights as the glyph U+265E in ANSWER green on light squares. If the renderer cannot print U+265E, a filled ANSWER disc of the same size is the only acceptable fallback.
2. **Example 13 model bars (book p.27: x, 1.5x, 0.75x), items C173 blocks 0-3 and C174, all none.** The figure is a "worked example picture" in the base inventory, but the plan already shows it as teaching image C173.IMG1, so P27-bar_model-1 is mapped `concept_image:M4.S17.T17.C173.IMG1`. No Step-B trigger applies to (i), (ii), (iii), Arun or Surbhi's Twelve Thousand: the numbers (50% margin, 50% discount, 12,000) are in the words and the steps carry x * 1.5 * 0.5 = 0.75x. If the user prefers a diagram per worked example, (i) "No loss?" (C173 block 0) is the item to turn required (three bars x, 1.5x, 0.75x, widths 4 : 6 : 3 units).
3. **M4.S16.T16.C166 (Q7 solution), optional.** A line graph of Rs 1000 over years 0 to 10 (straight line to 2000 at year 10; curve passing 2000 between year 7 and year 8) would clearly help "linear versus exponential" but the LP text answer is complete and the book draws nothing; not added. No other Q1-Q9 solution got this because only Q7 contrasts the two growth types (Q1, Q2, Q5, Q6, Q8, Q9 are plain arithmetic; Q3 and Q4 are text).
4. **Cakely/Cakify (C172 block 0) and 20% or Rs 50 (C171 block 1), none** although teaching images (C172.IMG1 bars, C171.IMG1 graph) exist. Neither is a book figure for the item; the two bakery pictures in the book are shop illustrations (decorative) and the sale question has no picture. Teaching images stay untouched and are never linked.
5. **Q3 (observe anything interesting?), question none (OPEN_ENDED)** and solution none: two sentences comparing 24,000/24,200 and 24,000/24,310.13.
6. **Summary (C176) none.** The two Summary figures (P31-bar_model-1 40% strip, P31-line_diagram-1 principal lines) are recap pictures of the Summary text, mapped `none:TEXT_SUFFICIENT`; the unit's question ("what did we find first?") is a reflection and carries no figure.
7. **P26-comic-1 (Puzzle-Solvers club comic), none:DECORATIVE_ONLY.** It is a teaching comic whose numbers (80%, 100%, 678 members) the LP text does not quote and no item asks about; if the content team wants it in the lesson, that is a teaching image job, not a diagram item.

## Book mistakes (decision 1)

- **Peaceful Knights board.** The book prints a 10 x 10 board (I counted the cell boundaries in the page picture: 10 columns and 10 rows, top-left dark red), with the words "chess board" and "8 knights". A chess board is 8 x 8. The LP answer "the 8 white squares of the first two rows" is true only on an 8 x 8 board (a 10 x 10 board has 10 white squares in two rows), and the LP teaching text says "any 8 x 8 grid" and "up to 32 is possible". The spec therefore draws the 8 x 8 board, top-left dark (as in the book), knights on row 1 columns 2, 4, 6, 8 and row 2 columns 1, 3, 5, 7. The base inventory keeps the printed 10 x 10 (its description is correct for the page); the correction is stated in the item's `reason`, `render_note` and `must_not_show`. This is the one point the user may want to confirm (8 x 8 vs the book's picture).

No printed-answer picture exists (this pdf has no solutions section). No other book slip found in my pages: all printed Figure it Out data matched the LP text, and I recomputed every LP answer in code: 20,000 x 1.2 = 24,000; 20,000 x 1.1^2 = 24,200; 20,000 x 1.05^4 = 24,310.125 (24,310.13, 310.13 more); 50,000 x 0.07 x 3 = 10,500; 50,000 x 1.07^3 - 50,000 = 11,252.15 (752.15 more); Giridhar 12,500 x 0.12 x 3 = 4,500, Raghava 12,500 x 1.1^3 - 12,500 = 4,137.50 (362.50 more); 1.5 x 1.03^3 = 1.639 (about 1.64 crore); 5,06,000 x 1.025^2 = 5,31,616.25; 1.1^7 = 1.949 and 1.1^8 = 2.144 (doubling between year 7 and 8); Example 12: 200 x 0.7 x 0.8 = 112, 200 x 0.5 = 100, single equivalent discount 44%; Example 13: 1.5x x 0.5 = 0.75x (25% loss), x = 16,000, d = 1/3 = 33.33%; Arun 100/120 = 83.33%, 16.67% fewer; Bengaluru 2.5 x 50 lakh = 1.25 crore.

## LP text issues (no LP text was changed; decision 2)

- **M4.S16.T16.C164 (Q6 answer), steps_tex**: "The topic's faded problem (see the faded ladder)." is a pointer, not a solution step. Suggested: "Giridhar (no compounding): $12,500 \times 0.12 \times 3 = 4500$. Raghava (compounded): $12,500 \times 1.1^3 = 16,637.50$, so the interest is $16,637.50 - 12,500 = 4137.50$."
- **M4.S18.T18.C177 (Peaceful Knights), question**: "Place 8 peaceful knights" lacks the board and the rule. Suggested: "Place 8 knights on an 8 x 8 chess board so that no knight attacks another. A knight moves two steps in one direction and one step at right angles to it (an L-shape)." The steps and answer also assume the board colouring; suggested answer wording: "For example, the 8 light squares of the first two rows (row 1: columns 2, 4, 6, 8; row 2: columns 1, 3, 5, 7)."
- **M4.S17.T17.C171 blocks 0 and 1**: the block `question` fields are only titles ("Would you rather?", "20% or Rs 50 off?"); the data sit in the concept's textbook-text block. Suggested block 0: "Option A: deposit Rs 100, get back Rs 300. Option B: deposit Rs 1000, get back Rs 1500. What is the percentage gain of each?" Suggested block 1: "A shop offers 20% off or Rs 50 off on any purchase above Rs 150. Which is better for a bill of (i) Rs 180, (ii) Rs 225, (iii) Rs 300?"
- **M4.S17.T17.C172 block 1 (Check my thinking)**: the `question` field stops at "Compared with the start it is" (no options a/b/c); the options and the answer are in the `text` field only. Suggested: "A price rises by 10% and then falls by 10%. Compared with the start it is (a) the same (b) 1% lower (c) 1% higher."
- **M4.S17.T17.C173 blocks 0-3**: the questions "(i) No loss?", "(ii) Sold for Rs 12,000", "(iii) Break-even discount", "Arun's statement" are fragments that depend on the Example 13 set-up (50% margin, then 50% discount; Ariba has 120% of Arun's marbles) held in another block of the same concept. Suggested prefix for each: "Surbhi marks goods up by 50% and then gives a 50% discount." and, for Arun: "Ariba says she has 120% of the marbles Arun has. What can Arun say about his marbles compared with hers?"
- **M4.S17.T17.C176 (Summary)**: the worked-example answer "The 100%, the base" is fine; the question is a reflection with no data, so nothing is missing.
- **M4.S16.T16.C166 (Q7 answer)**: "just over 7 years (doubled by the end of year 8)" is correct (exact 7.27 years) but a reader could miss that compounding is paid per year; suggested addition: "(after 7 years Rs 1000 has become about Rs 1949; after 8 years about Rs 2144)".

## Places where the book itself is unclear

- Peaceful Knights: 10 x 10 picture versus "chess board" and "8 knights" (above). Note the book gives no answer.
- The comic on p.26: which child speaks which bubble in panels 1-2 is not clear from the bubble tails (the base inventory says the same); irrelevant because the figure is `none`.
- Figure it Out Q7 (Math Talk) asks "how long to double"; the book gives no answer. The LP answer (10 years, just over 7) is mathematically correct; for compounding, "doubled during year 8" is the exact reading.

## Mapping summary (figure_inventory, 6 entries)

| fig_id | mapped_to |
|---|---|
| P26-comic-1 | none:DECORATIVE_ONLY |
| P27-bar_model-1 | concept_image:M4.S17.T17.C173.IMG1 |
| P31-bar_model-1 | none:TEXT_SUFFICIENT |
| P31-line_diagram-1 | none:TEXT_SUFFICIENT |
| P32-chess_board-1 | item:M4.S18.T18.C177 (question) |
| P32-chess_board-2 | none:TEXT_SUFFICIENT |

Figures NOT claimed by chunk G (they sit in the book sections of other chunks): P21/P22 deposit tables and P23 annotated expressions (Examples 7-9, topics M4.S14.T14 / M4.S15.T15, chunk F), P28-P30 end-of-chapter figures (M4.S19.T19). Pages 22-25 of my units (Figure it Out Q1-Q9, Would You Rather) carry no figure of their own.

### Chunk H notes (from the decision agent)
# Notes for chunk H (Class 8 Ch 8, topic M4.S19.T19 "Questions: Putting It All Together", Figure it Out Q2 to Q15, units 110 to 123)

Result: 28 items (14 pairs): required 3 / optional 3 / none 22. Validator: errors 0, warnings 0.

| Book Q | Question concept | Question side | Solution side |
|---|---|---|---|
| 2 (match countries) | C178 / C179 | none (NUMBER_LIST_IN_BOXES) | optional, not added |
| 3 (GST) | C180 / C181 | none | none |
| 4 (mice) | C182 / C183 | none | none |
| 5 (35% then 30%) | C184 / C185 | none | none |
| 6 (dot grid, region E) | C186 / C187 | REQUIRED, C186.IMG1 | optional, not added |
| 7 (x% of y) | C188 / C189 | none | none |
| 8 (excursion) | C190 / C191 | none | optional, not added |
| 9 (pencils) | C192 / C193 | none | none |
| 10 (bus fares) | C194 / C195 | none | none |
| 11 (rectangle) | C196 / C197 | none | none |
| 12 (chips label) | C198 / C199 | REQUIRED, C198.IMG1 | none |
| 13 (three shops) | C200 / C201 | none | none |
| 14 (left-handed) | C202 / C203 | none | none |
| 15 (bar graph) | C204 / C205 | REQUIRED, C204.IMG1 | none (SAME_AS_QUESTION_DIAGRAM) |

Figures claimed (4, all checked against the page pictures, all base descriptions correct): P28-match_cards-1 (none:NUMBER_LIST_IN_BOXES), P29-dot_grid-1 (Q6 question), P29-product_label-1 (Q12 question), P30-bar_graph-1 (Q15 question). Nothing new found on pdf pages 28 to 30. The figure printed beside Q7 and Q8 on p.29 is Q6's dot grid.

## Borderline

1. **Q6 solution (C187): optional, not added.** The LP solution only counts squares (64 in all, E is half of a 4 x 4 square = 8). A copy of the question grid with E shaded would help the counting step, but nothing new is drawn and the question figure already names E. I followed Step E ("figure-based question, numeric answer: Q required, S none or optional if the solution splits the shape"). If the user wants a solution picture, it is `derived_from` C186.IMG1: same grid, E filled MARK_FILL, the 64 unit squares faintly drawn in GUIDE.
2. **Q2 solution (C179): optional, not added.** Answer is a matching (arrangement of pairs). The v3 note on NUMBER_LIST_IN_BOXES says the arrows only become a diagram on the solution side and only optional when the written answer already gives it; the LP answer lists all four matches. Also the USA (about 4.2%) has no card to join to, so a drawn matching would leave one country unmatched.
3. **Q2 question (C178): none** although the book has a picture. It is two rows of plain cards with no joining line (a list of boxed values to choose from), and the LP question text lists every card in order.
4. **Q8 solution (C191): optional, not added.** The book's hint says "Drawing a rough diagram can help", but the book draws none and the LP solution is two multiplications (0.6 x 0.4, then x 160). A bar model (100% split 40% / 60%, 60% of the 40% marked = 24%) would be the picture. No question diagram, because the question gives no figure.
5. **Q12 question (C198): required** although the LP bracket "(Label: Potato 70%, ...; net quantity 65 g)" already carries every number. Kept required under decision 4: in the book the data lives only in the picture ("shown in the picture"). Only the label data is drawn (a plain table plus 'Approximate Values' and 'NET QTY: 65 g'); the packet art, plate of chips, barcode and 'Potato Chips' brand text are left out as decoration.
   - I left out the label's own heading 'Nutritional Information' because the brief forbids headings in a picture. It is a one-line change in the spec (add it above the table) if the user wants the label complete.
6. **Q15 question (C204): required** for the same reason (graph reading, LP bracket repeats the values). The chart title, subtitle, source line and 'Data For India' emblem are not drawn (headings/branding rule); the chart's title words survive only as the horizontal axis title 'Ability to use computer (2023)', because without some axis meaning the percentages are unlabelled. Colours: book teal and amber replaced by SET_A and SET_B.
7. **Q15 Male Children bar.** The book prints no number on it (bar measured at about 4.8); LP text says about 5%. Drawn to exactly the 5% gridline and left unlabelled, as in the book. Other bars are drawn at the PRINTED labels; in the book the bars differ from their labels by up to half a unit (Twenties Male ends near 36.5 under "37%", Seniors Female near 1.5 under "2%", Fifties Female near 3.7 under "4%"), which looks like rounding in the original NSS chart. No statement (i) to (vi) depends on this.
8. **Q15 solution (C205): none (SAME_AS_QUESTION_DIAGRAM).** Each statement looks at a different group, so no single complete final picture exists that the question graph does not already show.
9. **Q5, Q11 (and Q9) solutions: none.** A bar model or a before/after rectangle would only make them nicer; the questions give no figure and the working is a single product or algebra line. I did not mark them optional because, unlike Q8, the book does not suggest a diagram.

## LP text issues

- **M4.S19.T19.C178 (Q2 question):** the card list is run together ("13% 8% 18% 10% 1% 35% 2% 2% 0.1%"), fine for the book but hard to read. Suggested: "Options: 13%, 8%, 18%, 10%, 1%, 35%, 2%, 2%, 0.1%."
- **M4.S19.T19.C179 (Q2 answer):** (a) says "about 4.2%" for the USA and then "4% is not among the options", which reads as if the answer were 4%; (b) it contains teacher-facing instructions in a student answer ("tell the student the true value and praise them for spotting it", "The other options are distractors."). Suggested: "USA: 347 million is about 4.2% of 8.2 billion. This is not among the options (and 2% is printed twice), so no card fits the USA; the other cards are distractors."
- **M4.S19.T19.C183 (Q4 answer):** "(iii) and (iv) are the $M_5$ trap." "M5" is an internal module code that means nothing to a student. Suggested: "(iii) and (iv) wrongly add or ignore the percentages; changes of percent multiply, they do not add."
- **M4.S19.T19.C186 (Q6 question):** question_tex contains an editor's bracket "(Dot-grid figure: an 8 x 8 square divided into A ... into D and E.)". Once the diagram is placed this bracket is redundant and reads as a note. It also does not say which triangle is E (D is the upper-left, E the lower-right one). Suggested: delete the bracket and keep "What percentage of area is occupied by the region marked E in the figure?"
- **M4.S19.T19.C187 (Q6 answer):** step 1 "Count squares: the whole is 8 x 8, 64 squares;" ends with a semicolon and step 2 is fine; suggested: "The whole big square is $8 \times 8 = 64$ small squares." and "E is half of a $4 \times 4$ square, so $8$ squares; $\frac{8}{64} = 12.5$%."
- **M4.S19.T19.C190 / C191 (Q8):** the LP answer says "Book data issue: ..." inside the answer; it is a note to the content team, not student text. Suggested: "24% of 160 is 38.4, which is not a whole number of students, so the numbers cannot all be exact; say about 38 and discuss why."
- **M4.S19.T19.C198 (Q12 question):** "(Label: Potato 70%, ...; net quantity 65 g)" is an editor's bracket describing the picture; once the label diagram is placed it is redundant. Suggested: "The percentage of ingredients in a 65 g chips packet is shown in the picture. Find out the weight each ingredient makes up in this packet." (the picture carries the label).
- **M4.S19.T19.C204 (Q15 question):** the long bracket "(Bar graph 'Ability to use computer by age and gender (2023)' - Children: Female 4%, Male about 5%; ... Subtitle: ... Source: ...)" is an editor's description of the graph; redundant after the diagram is placed. Suggested: delete it and keep "Look at the following graph." Also the LP says "Male about 5%" for Children, which the book itself does not print.
- **M4.S19.T19.C205 (Q15 answer):** "(iii) ... Not valid" is stronger than the book supports; the graph only shows percentages, so the statement "cannot be concluded" is the accurate verdict. Suggested: "(iii) cannot be said: the graph shows percentages within each group, not how many people each group has."
- **Duplicated numbering:** each answer's `text` field starts the steps with "$1$." and the question concepts have the book number as a prefix ("$2$. The population ..."); harmless, but the steps_tex of C179 ("Estimate with standard form, then match.") and C189 ("Compute each pair, then generalise with algebra.") are one-line placeholders, not steps. Suggested: write the actual estimate (for example $83$ million $\approx 8.3 \times 10^{7}$, $8.2$ billion $= 8.2 \times 10^{9}$, ratio about $1$%).

## Book unclear or wrong

- **Q2 cards (p.28):** "2%" is printed twice and no card shows 4%, but the USA's share is 347 million / 8.2 billion = 4.23%. The book probably meant 4% for one of the 2% cards. No Q2 diagram is made (see above), so nothing to correct in a spec; if a matching picture is ever drawn, the USA card would join "4%" (corrected value) rather than "2%".
- **Q15 graph (p.30):** the Male Children bar has no printed value, and bar lengths are slightly off the printed labels (see Borderline 7).
- **Q8 (p.29):** 24% of 160 = 38.4 is not a whole number of students; the LP already notes this. No effect on the decision.
- **Q6 (p.28 to 29):** the question is on p.28 and its figure is on the top right of p.29, beside Q7 and Q8 text; the figure is Q6's, not Q7's.
