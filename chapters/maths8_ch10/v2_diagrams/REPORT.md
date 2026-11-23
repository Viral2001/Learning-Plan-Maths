# Class 8 Ch 10 Proportional Reasoning-2 - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths8_ch10` v35 (taken from staging). Result: new V2 version v36 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (84 items from 56 units)
{"worked_example": {"none": 24, "required": 4}, "question": {"none": 26, "required": 2}, "solution": {"none": 20, "required": 6, "optional": 2}}

Optional, NOT added: [('C32', 'solution'), ('C85', 'solution')]

needs_lp_text_sync: []

## The 12 diagrams
| id | side | type |
|---|---|---|
| M1.S2.T2.C6.IMG1 | worked example | other |
| M1.S5.T5.C19.IMG1 | solution | geometry_figure |
| M2.S6.T6.C23.IMG1 | worked example | geometry_figure |
| M2.S9.T9.C33.IMG2 | worked example | data_graph |
| M2.S9.T9.C36.IMG1 | worked example | construction |
| M2.S10.T10.C39.IMG1 | solution | data_graph |
| M2.S10.T10.C41.IMG1 | solution | data_graph |
| M2.S10.T10.C43.IMG1 | solution | data_graph |
| M2.S11.T11.C44.IMG1 | question | data_graph |
| M2.S11.T11.C45.IMG1 | solution | data_graph |
| M2.S11.T11.C46.IMG1 | question | data_graph |
| M2.S11.T11.C47.IMG1 | solution | data_graph |

### Chunk A notes (from the decision agent)
# Notes for chunk A (Class 8 Ch 10, sections 3.1 to 3.4, units 1-23)

Result: 30 items = required 3 (2 worked examples + 1 solution), optional 1, none 26. Validator: errors 0, one warning (C19 solution is required but no base figure maps to it: the book prints no solutions and no figure for Q4, so that is expected).

Figure inventory for this chunk (4 base figures): P01 -> none:TEXT_SUFFICIENT, P02 -> item M1.S2.T2.C6, P05 -> concept image M2.S6.T6.C20.IMG1, P06-shape-1 -> item M2.S6.T6.C23. The pie chart, table and construction figures of 3.5 on pages 6-8 belong to chunk B. The children grinding spices on page 3 is decoration and is not in the base inventory.

## 1. Judgement calls

- **M1.S2.T2.C6 (map, worked example): required, schematic.** The question says "Using the map" and the learner must measure, but the LP shows no map. The book map is an OpenStreetMap-style physical map; rule NOT_RENDERABLE says do not fake a real map. I kept `required` (FIG_REFERENCED, DATA_IN_FIGURE) and specified a schematic that draws only what the question needs: the 13 city markers at their measured positions, the lat/long frame ticks, compass rose, legend, sea names, "RF = 1 : 60,00,000" and "Map not to scale". Coastline, terrain, roads and Sri Lanka are NOT drawn (listed in `must_not_show` and `render_note`). Marker positions come from pixel centroids on the page picture; the printed ticks are Web-Mercator and the lon/lat I computed agree with real coordinates to about 0.1 degrees (Bengaluru-Chennai 290 km, Mangaluru-Chennai 589 km by great circle; the LP says 290 and 587). The drawing's Mangaluru-Chennai / Bengaluru-Chennai length ratio is 2.02, the LP's 4.9 / 2.4 cm is 2.04. DECISION NEEDED FROM THE USER: schematic city map (as specified) or supply the scan of the book map and set this item to none.
- **M2.S6.T6.C23 (Example 5, worked example): required.** The answer is a constructed, lettered triangle ABC (20, 60, 100) and the steps use A, B, C (B2: answer is a construction; lettered figure drawn even when a teaching image shows it). The teaching image M2.S6.T6.C22.IMG1 shows the same triangle and is not linked. As a worked example the token goes after the question text, so the finished triangle is visible there; this is how the brief defines a worked example's single diagram.
- **M1.S5.T5.C19 (Figure it Out Q4 solution): required, question none.** "Construct a triangle with sides 3 : 4 : 5" has a drawn answer (B2). The question gives no figure, so no question diagram (companion note) and `derived_from` is null. The figure draws the two triangles the LP names (3, 4, 5 cm and 6, 8, 10 cm), to scale, both right-angled by geometry; the right angle is not marked because the LP text does not mention it. Outline in ANSWER, fill MARK_FILL (the whole figure is added by the solution).
- **M2.S8.T8.C32 (Figure it Out Q5 solution): optional.** The answer is a reason (1 + 3 = 4 < 5), not a drawing, so it is not the same kind of answer as Q4. A segment picture (5 units against 1 + 3 laid end to end, gap of 1) would help but is not needed. Not added.
- **Question sides of C14, C16, C18, C25, C27, C29, C31: none.** The book gives no figure for any of them; no blank question figure is invented.
- **M2.S6.T6.C21 (Example 3, 110 units of concrete): none.** The book's picture (heaps with arrows 1, 1.5, 3) repeats only the numbers already in the text, and it is already the concept image M2.S6.T6.C20.IMG1 (accounting only, not linked). No trigger of Step B applies.

## Borderline (v3 rules applied as written; nothing flipped because the LP text carries the numbers)

- **M1.S2.T2.C2 block 0 (idli, P01 cross-multiplication arcs): none** (TEXT_SUFFICIENT). The arcs only show which pairs are multiplied (6 with 2, 3 with 4) and the LP steps write both products. Could be optional ("makes the cross visible"); either way no image is added. The figure is a teaching figure that is not among the plan's 11 concept images.
- **M1.S2.T2.C4 (Map Making Activity, 1 : 50): none** (OPEN_ENDED). A 16 cm by 12 cm rectangle with a 3 cm desk would only make it nicer; object positions are not given.
- **M1.S2.T2.C3 (what RF 1 : 60,00,000 means): none.** The concept image C3.IMG1 already shows map distance, road and scale bar; the printed map is used only by the distance question.
- **M2.S8.T8.C32 optional vs none vs required:** see above; a reason-only answer, not a drawing.
- **C6 map: required vs none (NOT_RENDERABLE):** see above.

## 2. LP text issues (concept id, what is wrong or missing, suggested sentence). Nothing was edited.

- **M1.S2.T2.C6** question says "Using the map" but the LP has no picture; the new diagram supplies it. Suggested: "Use the map of South India shown above (RF = 1 : 60,00,000, marked 'Map not to scale') ..." and in step 2 "On the page" -> "On the printed map in the book".
- **M1.S3.T3.C12** "What is the total volume of this purple paint?" has no numbers and the step "4 + 6 + 10 = 20" is unexplained. Suggested: "In Example 1, Yasmin's purple paint has 4 litres of red, 6 litres of blue and 10 litres of white. What is the total volume of this purple paint?"
- **M1.S4.T4.C14 / C15** the question never says what the four terms of 8 : 4 : 2 : 1 are, yet the answer names coriander, toor dal and fenugreek. Suggested: "Viswanath's spice mix uses 8 spoons of coriander seeds, 4 red chillies, 2 spoons of toor dal and 1 spoon of fenugreek seeds (8 : 4 : 2 : 1). Puneet has only 2 red chillies. How much of the other ingredients should he use ...?"
- **book_number labels are duplicated or shifted.** M1.S5.T5.C16/C17 say "Figure it Out 3.4, Q1" but are book Q2 (library); M1.S5.T5.C18/C19 say Q2 but are book Q4; M2.S8.T8.C27/C28 say Q1 (book Q1, correct); C29/C30 say Q2 but are book Q3; C31/C32 say Q3 but are book Q5. So "Q1" appears on two different questions. Suggested labels: C16/C17 "Figure it Out 3.4, Q2", C18/C19 "Q4", C27/C28 "Q1", C29/C30 "Q3", C31/C32 "Q5". The `ncert_refs` (FiO2, FiO4, FiO1, FiO3, FiO5) are right. The concept names "Figure it out: Q1/Ans1" are duplicated across M1.S5.T5 and M2.S8.T8 too, and the five exercise questions are split across two topics in an order different from the book.
- **M2.S7.T7.C25** `question_tex`: "How many $ml$ of each make $50\text{ ml}$?" sets the first unit in math italics. Suggested: "How many $\text{ml}$ of each make $50\text{ ml}$?"
- **M1.S2.T2.C5** steps use "290 km" without saying which pair; the question says "the same two pairs of cities". Suggested: add "(for example Bengaluru to Chennai, about 290 km)".
- **M1.S5.T5.C19** step 1 says "construct it with a ruler and compass" but gives no construction steps; the new figure shows the finished triangles only.
- **M2.S6.T6.C20** carries the concept image C20.IMG1 (the 110-units split of Example 3) although its own example is "Divide 12 in the ratio 2 : 1"; Example 3 is C21. Not an error for this run, only a placement oddity.

## 3. Where the book itself is unclear

- The page-2 map is marked "Map not to scale" and is printed at about half the stated scale (LP step 4). The picture cannot confirm the printed centimetres; the LP's 2.4 cm and 4.9 cm are consistent with the measured 2.02 length ratio.
- The book spells the city "Vishakapatnam"; the diagram keeps the book's spelling.
- Figure it Out Q4 ("construct a triangle with sidelengths in the ratio 3 : 4 : 5") has no figure and this pdf has no printed solutions, so the 3-4-5 / 6-8-10 triangles come from the LP solution only.
- Example 5's figure shows the triangle only (no side lengths); its proportions agree with 20, 60, 100 (AB = 100, AC = 87.9, BC = 34.7 by the sine rule).
- No book print slips (wrong digit, missing sign, wrong count) were found in the figures of this chunk, so nothing had to be corrected under the user's decision 1.

### Chunk B notes (from the decision agent)
# Chunk B notes - Class 8 Ch 10 "Proportional Reasoning-2" (lp cbse_eng_maths8_ch10_v35)

Chunk B = topics M2.S9.T9, M2.S10.T10, M2.S11.T11, M3.S12.T12, M3.S13.T13, M3.S14.T14, M3.S15.T15, M3.S16.T16, M3.S17.T17.
32 items (8 worked-example blocks, 12 question/answer pairs). Result: required 8, optional 0, none 24. Validator: errors 0, 3 warnings (the three FiO 3.5 pie-chart solutions are required but the book prints no figure for them, which the validator says is fine).

Required diagrams (all 16:9, flat, exact proportions):

| media_id | item | what it draws |
|---|---|---|
| M2.S9.T9.C36.IMG1 | worked example "Construct the pie chart for the grades" | finished construction: circle, centre A, radii AB-AF, angles 108/90/72/54/36, slices coloured and labelled Grade A-E |
| M2.S10.T10.C39.IMG1 | solution FiO 3.5 Q1 | pie chart summer 90, rainy 120, winter 150 |
| M2.S10.T10.C41.IMG1 | solution FiO 3.5 Q2 | pie chart Entertainment 180, Sports 90, News 54, Information 36 |
| M2.S10.T10.C43.IMG1 | solution FiO 3.5 Q3 | pie chart of the LP's sample class of 40 (54, 36, 18, 54, 72, 72, 54) |
| M2.S11.T11.C44.IMG1 | question (book 3.6 FiO set b, Q4) | eight 24-hour rings (giraffe ... bat), dark share only |
| M2.S11.T11.C45.IMG1 | solution of the same | same rings with hours 2.5 ... 20 in the holes (derived_from C44) |
| M2.S11.T11.C46.IMG1 | question (book 3.6 FiO set b, Q5) | transport pie chart, Car angle unmarked |
| M2.S11.T11.C47.IMG1 | solution of the same | same chart plus Car 30 in ANSWER green (derived_from C46) |

## 1. Judgement calls

- **C33 worked ("How do we mark the different slices of the pie chart?") = none (TEXT_SUFFICIENT).** The book's grade pie chart (p.60) is the figure it refers to, but the answer is a method in words and every count (12 : 10 : 8 : 6 : 4) is in the steps; the finished chart is already the teaching image C35.IMG1. See Borderline.
- **C34, C35 worked = none.** Pure arithmetic (HCF 2, 6+5+4+3+2 = 20, 18 per part). C35's answer is a list of angles, not a drawing.
- **C36 worked = required (ANSWER_IS_FIGURE).** One picture stands for the book's four construction panels (p.61-62: steps 1-2, 3-4, 5-6, 7); P07-construction-1 and P08-construction-1 are earlier stages of it and are mapped to this item. It shows the final state: letters A-F (the steps name them), the five angles, and all five slices coloured and labelled. The book's step-7 panel colours only A (green) and B (yellow); C, D, E are left blank there. I coloured all five because the LP step 7 says "colour and label each slice with its grade". Hues follow the book (A green, B yellow, C blue, D pink, E orange) as light tints.
- **FiO 3.5 Q1-Q3 (T10): question none, solution required for all three (sibling consistency).** The question gives no figure; the answer is a drawn pie chart. Q3's given table (7 subject headings, empty row) is a plain table (LATEX_TABLE). Q3's solution draws the LP's own sample class (counts 6, 4, 2, 6, 8, 8, 6, sum 40). The pies run anticlockwise from a radius pointing right, in the order the LP names the slices, as in the chapter's construction.
- **C44 (sleep rings) question = required, C45 solution = required.** The rings carry all the data (no numbers in the book). The book puts a sleeping-animal sketch in each hole; sketches are decorative clip-art and not drawn. A name label under each ring takes their place, in the LP question's order (giraffe, elephant, human, dog / cat, squirrel, python, bat). No key is drawn on the question figure (the book has none).
- **Sleep ring angles: exact, not measured.** The base inventory measured the book's rings at about 43, 56, 117, 152, 191, 223, 271, 302 degrees. The LP answer (2.5, 3.5, 8, 10.5, 13, 15, 18, 20 hours) gives 37.5, 52.5, 120, 157.5, 195, 225, 270, 300 degrees (hours x 15). The two differ by up to about 6 degrees (giraffe 43 vs 37.5, dog 152 vs 157.5), which is print approximation, not a slip in a digit; by decision 1 the spec draws the exact values. Dark = SET_A, light = SET_B; the dark arc starts at 12 o'clock and runs anticlockwise, as in the book.
- **C46 (transport pie) question = required, C47 solution = required.** The book says "Study the pie chart" and all four parts are read from it, so the question figure is given data even though the LP text repeats the angles. The Car angle is not printed in the book (30 degrees = 360 - 90 - 120 - 60 - 60); the picture's radii confirm 30. The two 60 degree labels belong to Cycle (left) and Two-wheeler (below-right), checked on the page picture. Slice order clockwise from 12 o'clock is Bus, Two-wheeler, Car, Cycle, Walk. The book writes "Two-" / "wheeler" on two lines; the spec keeps that.
- **T12 worked C50, C51 = none.** The speed-time table (p.63) and the bracket-factor table (p.64) are the teaching image C49.IMG1; both base figures are accounted to it, never linked. The factors and the product 90 are written in the steps.
- **T13, T14, T15 Q3, T17 pairs = none/none.** Word problems with no book figure; solutions are arithmetic or a sentence.
- **T15 Q1 (three x-y tables) and Q2 (fill the empty cells) = none/none (LATEX_TABLE).** Plain tables of numbers, every number also in the text. Q2's answer is the same plain table with blanks filled, which is exactly the prompt's own example of a completed plain table (none, LATEX_TABLE).
- **T16 worked C64, C66 = none.** Arithmetic (pump-hours; fractions of work). The teaching images C63.IMG1 and C65.IMG1 exist but are never linked, and these blocks do not need a figure by the tie-breaker; the book has none.
- **Inventory accounting.** P06-pie_chart-1 -> concept_image C35.IMG1 (the same chart redrawn with angles, from a radius pointing right, as a teaching image); P09-table-2 and P10-annotated_table-1 -> concept_image C49.IMG1; P13 and P14 each used twice (question and solution), so the second use is NEW-P13-donut_chart-1-sol and NEW-P14-pie_chart-1-sol; the six plain tables are LATEX_TABLE. All 14 base figures of this chunk plus the two NEW- second uses = 16 entries, unmapped 0. No base description needed a "CORRECTED:" (all 14 checked against the page pictures, including the doubts in `unclear`).
- **Decorative pictures not inventoried** (as the base does): the motorcycle and car illustration on p.9. The pump, toy and tank pictures on p.68 belong to the end-of-chapter questions (not this chunk).

## 2. Borderline (decision 4: v3 rules applied as written)

- **C33 worked: none vs optional/required.** The text points at "the pie chart" (a figure reference), but nothing is lost without it. If you want the book's grade pie chart on this block, it would be the 5-slice chart with counts 12, 10, 8, 6, 4 and no angles (book p.60).
- **C47 solution: required although it adds one label.** The only addition to the question figure is the Car slice mark 30 degrees (v3 "new marks"). The alternative is none with SAME_AS_QUESTION_DIAGRAM. I did not add highlights for the answers to (i) (Bus) or (iv) (Cycle and Two-wheeler): four sub-questions share one figure.
- **C59/C60 and C57/C58 (tables): none.** Could be read as ANSWER_IS_FIGURE (filled table) but the v3 prompt's own example makes a completed plain table LATEX_TABLE.
- **C42 question: none.** The book gives an empty table to fill (act-on-figure reading), but it is a plain table with only column headings.
- **C36: one picture for four book panels, with grade names, angles and point letters together** (about 16 text items). Checked in code that every label box lies inside its slice or outside the circle without overlaps. If it looks too busy, the grade names are the first thing to drop.
- **C45: required** (answer is the labelled rings). The alternative would be to leave the hours to text; I followed "printed answer is a picture".
- **C66, C69, C71 and C54 (work-and-time and bricks examples): none** although two teaching images show similar ideas; by the rules those are never linked and the items are fully text/arithmetic.

## 3. LP text issues (not edited; suggested fixes)

- **M2.S9.T9.C33** (teaching text): "pie charts like the one shown in the figure" but this concept's own image is the halving bars (C33.IMG1); the pie chart appears only on a later card (C35.IMG1). Suggested: "(the finished pie chart is on the card after this)" or move the sentence.
- **M2.S9.T9.C36** worked question "Construct the pie chart for the grades." gives no data. Suggested: "Construct the pie chart for grades A to E with 12, 10, 8, 6 and 4 students (angles 108°, 90°, 72°, 54°, 36°)."
- **M2.S11.T11.C44** question text does not say which part of a ring is the time asleep (the book does not either); only the solution says so. Suggested sentence: "In each ring the dark part shows the hours asleep in a 24-hour day."
- **Wrong or duplicate book numbers.** C44/C45 are labelled "Figure it Out 3.6, Q1" but are the book's second 3.6 set, Q4; C46/C47 "Q2" is book Q5; C57-C60 "Q1", "Q2" are the first 3.6 set (p.65) Q1, Q2; C61/C62 "Q3" is the second set's Q1 (taps). So "Figure it Out 3.6, Q1" appears for two different book questions (C44 and C57). Suggested: "Figure it Out 3.6 (second set), Q4 / Q5 / Q1" for C44, C46, C61 and "(first set)" for C57, C59.
- **M2.S10.T10.C43** is built on a sample class invented by the LP (counts 6, 4, 2, 6, 8, 8, 6 for a class of 40). Fine, but the question text says "your class"; the solution text already says "this model uses a sample class of 40", so no change needed, just noted.
- No contradictions between LP solutions and the book. All sums and products were recomputed: 360 - 90 - 120 = 150; 3.6 x 50/25/15/10 = 180/90/54/36; 54+36+18+54+72+72+54 = 360 and 6+4+2+6+8+8+6 = 40; 108+90+72+54+36 = 360; 360 - 90 - 120 - 60 - 60 = 30; 18 x 12 = 216; products 800, 800, 312.5, 128 and 450; 2 x 18 / 4 = 9; 80 x 15 / 100 = 12; 20 x 4 / 10 = 8; 5 x 4 = 20; 1.5 / 18 = 5 / 60 = 1/12; 3/5 hour = 36 minutes.

## 4. Places where the book is unclear or inconsistent

- The sleep-ring picture prints no key (which colour is "asleep"), no numbers and no animal names; the animals are identified from the sketches (the child is called "human" by the LP). The shares are drawn slightly off the exact hours values (see above).
- The pie chart construction's step-7 panel leaves slices C, D, E blank and unlabelled.
- The two pie charts in 3.5 use different starting radii: the intro chart (p.60) starts slices at 12 o'clock and goes anticlockwise (A, B, C, D, E); the construction (p.61-62) starts at the radius AB pointing right (3 o'clock) and also goes anticlockwise. Both are anticlockwise; the C36 diagram follows the construction panels, the FiO 3.5 solution pies follow the construction direction.
- The book's Q5 pie chart (p.68) does not print the Car angle; it is the remainder, 30 degrees.
- There is no printed-solutions section in this pdf, so the three FiO 3.5 solution pie charts have no book picture to copy; they are drawn from the LP numbers.

### Chunk C notes (from the decision agent)
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
