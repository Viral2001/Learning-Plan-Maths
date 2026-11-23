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
