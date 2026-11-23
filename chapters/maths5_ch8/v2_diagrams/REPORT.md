# Class 5 Ch 8 Weight and Capacity - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths5_ch8` v4 (taken from staging). Result: new V2 version v5 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (123 items from 72 units)
{"worked_example": {"none": 17, "required": 3, "optional": 1}, "question": {"none": 42, "required": 9}, "solution": {"none": 40, "required": 10, "optional": 1}}

Optional, NOT added: [('C80', 'worked_example'), ('C125', 'solution')]

needs_lp_text_sync: []

## The 22 diagrams
| id | side | type |
|---|---|---|
| M1.S4.T4.C7.IMG2 | worked example | measurement_scale |
| M1.S4.T4.C8.IMG2 | worked example | measurement_scale |
| M1.S5.T5.C10.IMG1 | question | measurement_scale |
| M1.S5.T5.C11.IMG1 | solution | measurement_scale |
| M2.S6.T6.C12.IMG2 | worked example | number_line |
| M2.S7.T7.C15.IMG1 | question | other |
| M2.S7.T7.C16.IMG1 | solution | other |
| M2.S9.T9.C23.IMG1 | question | number_line |
| M2.S9.T9.C24.IMG1 | solution | number_line |
| M2.S13.T13.C37.IMG1 | question | number_line |
| M2.S13.T13.C38.IMG1 | solution | number_line |
| M2.S13.T13.C43.IMG1 | question | arrow_map |
| M2.S13.T13.C44.IMG1 | solution | arrow_map |
| M2.S22.T22.C84.IMG1 | question | double_number_line |
| M2.S22.T22.C85.IMG1 | solution | double_number_line |
| M2.S22.T22.C86.IMG1 | question | double_number_line |
| M2.S22.T22.C87.IMG1 | solution | double_number_line |
| M2.S22.T22.C89.IMG1 | solution | double_number_line |
| M3.S26.T26.C103.IMG1 | question | measurement_scale |
| M3.S26.T26.C104.IMG1 | solution | measurement_scale |
| M3.S27.T27.C105.IMG1 | question | number_line |
| M3.S27.T27.C106.IMG1 | solution | number_line |

### Chunk A notes (from the decision agent)
# Notes, chunk A (Class 5 Ch 8 "Weight and Capacity", topics M1.S2.T2 to M2.S12.T12)

Result: 18 units, 27 items: required 9 (3 question, 3 solution, 3 worked example), optional 0, none 18. Validator: errors 0, warnings 3 (the three worked-example figures below are LP-authored scales / lines that are not printed in the book, so no base figure maps to them; this is expected).

Required items (media ids):
- M1.S4.T4.C7.IMG2 (worked): scale dial, 5 kg turn, needle on the 3rd mark after 3 kg.
- M1.S4.T4.C8.IMG2 (worked): scale dial, 2 kg turn, 10 gaps between labels, needle on the 7th mark after 1 kg 500 g.
- M1.S5.T5.C10.IMG1 (question) and M1.S5.T5.C11.IMG1 (solution): the six dials (a) to (f); solution derived from the question figure.
- M2.S6.T6.C12.IMG2 (worked): double number line 1, 4, 9, 16 kg with 1,000 g and 9,000 g given.
- M2.S7.T7.C15.IMG1 (question) and M2.S7.T7.C16.IMG1 (solution): two matching columns plus the double number line; solution adds the six joins and the filled blanks.
- M2.S9.T9.C23.IMG1 (question) and M2.S9.T9.C24.IMG1 (solution): 7-tick double number line, then the filled line.

Everything else is none (text / LaTeX), including all of Check! Check!, Example 1 and 2 (Shrenu), Let Us Find 1, the picnic fruits and the weight comparisons, and the worked examples C3, C13, C25, C31, C32, C33.

## 1. Judgement calls

- Six dials of Let Us Do (C10/C11): the LP holds them as ONE question concept, so the pair gets one question figure and one solution figure with the six dials in a 3 x 2 grid (brief rule: at most one diagram per side for a pair). Letters (a) to (f) are drawn because the LP answer refers to the figures by letter (decision 3). The book's answer boxes are not drawn (the blanks are in the question text). The book's red "0" is drawn in INK (the style tokens have no red).
- Needle positions come from the LP marks and agree with the angles measured on the page picture: (a) 6th mark = 54 degrees, (b) 18th = 324, (c) 25th = 150, (d) 26th = 234, (e) 15th = 54, (f) 66th = 237.6. The base inventory doubted (f): the arrow measures about 238.4 degrees (about 662 g); the LP says the 66th mark, 660 g, and 660 g is used.
- C11 solution is `required` although the LP answer is numbers: the steps count marks from 0 and the figure adds the sweep from 0 to the needle and the six readings under the dials (new marks on the given figure, B2 / step E). If the reviewer prefers text only, it would become none with SAME_AS_QUESTION_DIAGRAM.
- Worked examples C7 and C8 (reading a dial): `required` by MEASUREMENT_READING, even though the LP text states the needle position in words; the question figure shows the dial and needle only, no reading. The kept teaching images are not linked (decision 5).
- C8 dial: a medium tick is drawn at the 5th mark of each group of 10 (as the book dials do) so that counting 7 marks is possible; this is drawing convention, not data.
- C12 (worked, double number line): taken as `required` because the question text itself says "Use a double number line with 1 kg and 1,000 g". The figure shows only what is given (1 kg with 1,000 g, 4 kg, 16 kg, 9,000 g) and leaves the three asked values blank; tick order 1, 4, 9, 16 puts the 9 kg tick third. The sibling worked examples C13, C31, C32, C33 do not mention a line or figure, so they are none.
- C15/C16 (match the bags): the two columns are also in the question text, but they are drawn together with the line so that the solution can add the six joining lines on the same layout (the answer is a matching = an arrangement, ANSWER_IS_FIGURE). The two bags on the scales (2 kg / 2000 g) are decoration (P02-scale-1, none:DECORATIVE_ONLY). The book's multiplier blank under the bottom arc is drawn as "×" plus a blank; the solution writes "× 3" there (LP: "× 3 on both lines").
- C23/C24 (Let Us Find 2 conversions): see Borderline. The book line has 9 ticks; the last two carry only blanks, no value is printed and no LP answer uses them, so 7 ticks are drawn in both figures (see section 3).
- Sibling consistency: the three Let Us Do / Let Us Find items that carry a given instrument or line figure (C10, C15, C23) all got a question and a solution figure; the pure conversion and comparison questions (C17, C19, C21, C27, C29) are none on both sides.
- Figure inventory: the 8 page-1 figures, 3 page-2, 5 page-3 and 2 page-4 figures are mapped (dials, matching columns and the two lines to items; the lists, scene pictures and speech bubbles to none). The Milligram dialogue (P05-dialogue-1) and the unit tables (P06-unit_facts-1, P07-table-1) are mapped to the kept teaching images M2.S12.T12.C31.IMG1 and M2.S12.T12.C32.IMG1 because the worked examples C31 and C32 are none (accounting only, nothing linked). Figures used again by a solution diagram are extra NEW-<base id>-sol entries (6 dials, the two page-2 figures, the page-3 line).
- Figures of page 5 and 6 that belong to the later Let Us Find questions (P05-double_number_line-1, P05-dialogue-2, P05-scale-1, P06-table-1, P06-picture_relation-1, P06-scale-1) and the page-7 Grocery Store figures are not claimed here (they belong to the chunk of those questions).

## 2. Borderline

- M1.S3.T3.C5 / C6 (Check! Check!): none / none. The book list has empty tick boxes and the answer is ticks and crosses, so ACTION_ON_FIGURE could be argued. Chosen: the seven item-and-weight lines are a plain list already in the question text (LATEX_TABLE) and the sample answer is seven yes/no marks that the LP states in words; Anu's room is a scene with no numbers (DECORATIVE_ONLY). If a figure is wanted: question = the list with seven empty boxes, solution = ticks on Bed, Rice Bag, Bucket, Water Bottle and crosses on Iron Almirah, Sofa, Refrigerator in ANSWER green.
- M1.S5.T5.C11 solution required (see above).
- M2.S6.T6.C12 worked example required (see above).
- M2.S9.T9.C23 / C24: the double number line is only an aid ("You can use the double number line given below"), so the question can be answered without it. Taken as required because the question text points to a figure that the LP text does not describe and the marks exist only in the picture (FIG_REFERENCED, DATA_IN_FIGURE); the solution fills the line as the LP's check line does. If the reviewer reads the aid as optional, both sides would become none/optional.
- M2.S11.T11.C28 (picnic fruits): "descending order" is a written list of four names, not an arrangement of pictures, so none.
- M2.S8.T8.C17 / C18 (Shrenu): the book's scale shows 3000 g but nobody reads it; the answer is the number 3,500 g, so none.
- Worked examples C13, C25, C31, C32, C33 are none because the rules give no figure for them (pure arithmetic or word problems with every number in the text); the kept teaching images (cells, number line, double line, unit boxes, blocks) are not the reason.

## LP text issues

- M1.S3.T3.C6 step 1: "Use the 1 kg block as a guide" points to a block that is only in the teaching image of an earlier topic. Suggested sentence: "Think of a 1 kg packet of sugar as a guide: a thing that is heavier than the packet must weigh 1 kg or more."
- M1.S5.T5.C10 question text: the dial faces and needle positions are only in the picture (text holds just the blanks). The question cannot be attempted without M1.S5.T5.C10.IMG1; nothing to add if the figure is kept.
- M2.S7.T7.C15 question text: "You can use the double number line given below" with no line in the text; the figure M2.S7.T7.C15.IMG1 supplies it. Same for M2.S9.T9.C23 ("on which some numbers have been marked").
- M2.S9.T9.C24 check line uses only 7 of the book's 9 ticks; the last two ticks are not mentioned (book gives them no values).
- M2.S11.T11.C30 part (c): the solution writes "10 kg 35 g = 10035 g" right after "10,035 g" in the same step (the book prints 10035 g without a comma). Suggested: "10 kg 35 g = 10,035 g" for consistency (question text too: "10,035 g").
- M2.S8.T8.C17 / M2.S8.T8.C19 hold `q_figure` hints (Shrenu with a scale; none for C19) that describe pictures no longer needed; nothing to change in the text.
- M1.S4.T4.C7 and C8 worked examples say "These are practice values" after the question; the figure shows the same values (5 kg turn / 2 kg turn), so no text change is needed.

## 3. Book unclear

- Page 3 Let Us Find 2: the double number line has 9 ticks; ticks 8 and 9 carry blanks only ("___ kg ___ g" above, "___ g" below) at the far right, to the right of 12 kg. No value is printed and none of the answers (a) to (f) belongs there (12,042 g would be 12 kg 42 g, but the book does not say). They are not drawn; this is stated in the figure's render_note. The ticks are not equally spaced in the book (not to scale); equal spacing is used.
- Page 2 double number line: also not to scale in the book; equal spacing used. The red curved arrow "× 1000" runs from 1 kg down to 1,000 g in the book; it is drawn as a straight vertical arrow at the first tick.
- Page 1 dial (f): the needle tip sits between the 650 g long tick and the next short tick (about 238 degrees); read as the 66th mark = 660 g, as the LP does.
- No printed solutions exist in this pdf; every solution figure is built from the LP solution text.
- Book print errors: none found on the pages of this chunk, so decision 1 (correct a print slip) was not needed. (Print style only: "10035 g" without a comma on page 4 and "1000 mg" without a comma on page 5.)

### Chunk B notes (from the decision agent)
# Chunk B notes - Class 5 Ch 8 "Weight and Capacity"

Topics M2.S13.T13 to M2.S17.T17 (units 19-30, book pages 5-8). 22 items: required 4 / optional 0 / none 18. Validator: errors 0, warnings 0.

| Unit | Concept(s) | Question | Solution |
|---|---|---|---|
| 19 | C35 / C36 sugar sachet | none | none |
| 20 | C37 / C38 double number line (mg / g) | REQUIRED `C37.IMG1` | REQUIRED `C38.IMG1` (derived from C37.IMG1) |
| 21 | C39 / C40 goldsmith 10 g 500 mg | none | none |
| 22 | C41 / C42 compare g and mg | none | none |
| 23 | C43 / C44 elephant x 40 whale | REQUIRED `C43.IMG1` | REQUIRED `C44.IMG1` (derived from C43.IMG1) |
| 24 | C45 / C46 kg, quintal, tonne | none | none |
| 25 | C47 / C48 Example 3 ornament | none | none |
| 26 | C49 / C50 King's Weight | none | none |
| 27 | C51 worked, adding weights | none (worked) | |
| 28 | C52 worked, subtracting weights | none (worked) | |
| 29 | C54 / C55 Example 4 rice total | none | none |
| 30 | C56 / C57 Example 5 extra rice | none | none |

Figure inventory: 16 entries (13 base + 3 `NEW-`): 4 mapped to items, 1 to a concept image, 11 to `none:` codes.

## 1. Judgement calls

- **C37 / C38 (double number line), required both sides.** The question says "below", the whole figure is data (which ticks carry which values, where the 4 blanks are) and the learner completes it. The solution is the completed line (B2, ANSWER_IS_FIGURE). Ticks are drawn exactly in proportion to the gram values (x = 0.08 + 0.84 x (g - 1) / 30); the book's ticks are only roughly to scale. The first top label is printed "1000 mg" in the book (no comma, while the rest of that line has commas); I drew "1,000 mg" to match the line and the LP. No arrows are drawn (the book has none). Answers: 5,000 mg, 20 g, 25,000 mg, 31 g (all checked: mg = 1,000 x g on every tick).
- **C43 / C44 (elephant and whale), required both sides.** The book question is "Observe the pictures given below" (FIG_REFERENCED); the 5,000 kg, the x 40 arrow and the blank sit in the picture. The animals are decoration, so the diagram is two captioned boxes ("Elephant", "Whale") with the curved x 40 arrow, no clip-art. The solution fills the whale box with 200,000 kg (5,000 x 40; 200,000 / 40 = 5,000), ACTION_ON_FIGURE, derived from the question figure. See Borderline.
- **Compare tables (C41 / C42).** The book's pink panel is a plain 3-column table, so `LATEX_TABLE`. The solution is six signs plus conversions: kept `none` (a filled plain table of signs is LaTeX, not a diagram). Chunk A's "Comparison between Different Weights" Q2 (cmp1.signs) is the same kind of item and should get the same decision; I did not read it.
- **Column addition and subtraction (C51, C52, C55, C57; base figures P07-column_addition-1/2, P08-column_subtraction-1/2).** v3 Step C lists column addition and subtraction as `LATEX_ARITHMETIC`. The LP steps name every carry and borrow in words, and the T17 solutions do not even use the book's carry-arrow layout (they add kg and g separately, or convert to grams). The kept teaching images C51.IMG1 and C52.IMG1 were not a reason for the decision (user decision 5); the reason is the arithmetic rule. Each item has a `text_alternative` for the LaTeX array.
- **Dialogue bubbles (P05-dialogue-2, P07-dialogue-1, P08-dialogue-1).** Text in a speech bubble with a character: `none:TEXT_SUFFICIENT`. P05-dialogue-2 is also listed in chunk A's T12 refs (`mg.similar`); if A maps it differently, the merge should compare (both are "no diagram").
- **P06-unit_facts-1 ("Did you know?")** is claimed by me as `concept_image:M2.S12.T12.C32.IMG1` because C45 / C46 (Let Us Find Q6) use its facts, and it is also a chunk A figure (`qt.know`). Same meaning in both chunks is expected. P07-table-1 ("From Tiny to Big") is not used by any chunk B unit, so I left it to chunk A (`units.table`).
- **NEW-P05-sachet.** The sugar sachet "SUGAR 5g" beside Let Us Find 1-2 is not in the base inventory; added as `none:DECORATIVE_ONLY` (the 5 g is in the question text).
- **NEW-...-sol figures.** The completed double number line and the completed whale figure are second uses of base figures (the book prints no solutions), so each has its own `NEW-<base id>-sol` entry mapped to the solution item.
- **C47 / C48 (Example 3 ornament).** In the book this is Let Us Find Q3: a bubble with the worked line (4 g = 4,000 mg ...) and a precision balance whose display is unreadable. None.

## 2. LP text issues

- **M2.S13.T13.C37** (question): "Complete the double number line below appropriately." carries no data; everything is in the figure. Fine once the diagram is placed (it is required). If the diagram were ever missing, suggested text: "Complete the double number line. 1 g is 1,000 mg, 12 g is 12,000 mg and the 20,000 mg, 25 g and 31,000 mg marks are given. Find the mg at 5 g, the g at 20,000 mg, the mg at 25 g and the g at 31,000 mg."
- **M2.S13.T13.C43** (question): the text still starts "Observe the pictures given below", then narrates the picture. With the diagram this reads well; without it the lead-in would point at nothing. No change needed with the diagram.
- **M2.S13.T13.C39 ... C45 and M2.S14.T14.C47 (numbering vs the book):** LP "Let Us Find: Q3" (C39, goldsmith) is book Let Us Find Q4; LP Q4 (compare) is book Q5; LP Q5 (whale) is book Q6; LP Q6 (quintals) is book Q7; and the LP's "Example 3: the ornament" (C47) is book Let Us Find Q3. Suggested `book_number` labels: C39 "Let Us Find 4", C41 "Let Us Find 5", C43 "Let Us Find 6", C45 "Let Us Find 7", C47 "Let Us Find 3".
- **M2.S17.T17.C54:** "bought several items" is in the book text too; the question only asks about rice. No change needed.
- **M2.S17.T17.C56** (Example 5 question): "How much extra rice did she buy for household use than for the Pongal festival?" has no numbers of its own; they come from Example 4 (2 kg 500 g and 1 kg 750 g) and appear only in the solution. Suggested sentence: "Rathna bought 2 kg 500 g rice for daily use and 1 kg 750 g for the Pongal festival. How much extra rice did she buy for household use than for the Pongal festival?"
- **M2.S16.T16.C51 / C52:** the practice values (3 kg 600 g + 2 kg 700 g; 5 kg 200 g - 2 kg 800 g) differ from the book's Grocery Store numbers (2 kg 500 g and 1 kg 750 g), as the text says ("These are practice values"). Not an error.
- **M2.S13.T13.C46:** answer says "5 tonne" (singular), following the book's blank "_____ tonne". Consistent with the book; plural "tonnes" is used for 8.

All LP arithmetic in chunk B was recomputed and is correct (C36, C38, C40, C42 a-f, C44, C46, C48, C50, C51, C52, C55, C57).

## 3. Borderline

- **C43 / C44 elephant and whale:** the LP question text already states 5,000 kg and x 40, so a careful student could solve it from text. Kept `required` because the book question is "Observe the pictures", the figure holds the data, and the text still points at the picture (user decision 4: do not flip only because the LP text carries the numbers). The solution side is "complete the blank in the figure"; it adds only one value, so it could be argued `none` (SAME_AS_QUESTION_DIAGRAM). Kept `required` for the Act-on-figure pair (Q required, S required) and to match C37 / C38.
- **C49 / C50 King's Weight picture:** a balance with the king against 10 sacks illustrates "10 times his weight". Judged `DECORATIVE_ONLY` (no numbers in the picture, relation stated in words). A balance figure would be nice but is not needed.
- **C41 / C42 compare:** question `LATEX_TABLE`, solution `none`; a filled table of signs could be read as a "filled figure" under B2, but plain tables stay LaTeX.
- **C51, C52, C55, C57 column work:** `none` under `LATEX_ARITHMETIC` even though the book draws carries and borrows with circles and arrows (HIGHLIGHT_MEANING could be argued). Reason: the LP text spells out each carry and borrow, and LaTeX arrays can show kg | g columns.
- **C35 / C39 / C47 pictures (sachet, precision balance):** decorative, numbers in the text.

## 4. Where the book itself is unclear

- Let Us Find 2: top first label "1000 mg" has no comma; tick spacing is only roughly proportional.
- Example 4 bubble: "So, total rice bought is 4 kg 250." has no unit after 250 (a print slip; the LP says 4 kg 250 g). No diagram uses it.
- Column addition answer row prints "4 [1] 2 5 0" with the carried 1 boxed and crossed; the true answer is 4 kg 250 g (diagram not drawn, so no correction needed).
- King's balance: the beam is not level, so the picture is only a hint of "10 times".
- Precision balance display on page 5 is unreadable.
- No solutions section in this pdf; the LP solution text is the answer used everywhere.

### Chunk C notes (from the decision agent)
# Chunk C notes (Class 5 Ch 8 Weight and Capacity, cbse_eng_maths5_ch8_v4)

Units: 18 (13 pairs, 5 worked), items: 31. Result: required 5 / optional 1 / none 25. Validator: errors 0, one expected warning (see 1.6).
Book pages used (looked at the pictures): page_08 (Let Us Do 1-7), page_09 (More Operations on Weight, Let Us Do 1-2), page_10 (Let Us Do 3-4, Measuring Capacity). This pdf has no printed-solutions section: the LP solution text is the answer.

## 1. Judgement calls

1. **Let Us Do 1-7 (T18, p.8), Example 6/7 (T20), both sides: none.** Word problems with every weight in the text, no figure in the book, working is kg/g or gram arithmetic (LATEX_ARITHMETIC / TEXT_SUFFICIENT). The column pictures on pages 7-8 belong to "The Grocery Store" section (another chunk), not to these questions. All 14 + 4 items get the same decision (sibling consistency), including the borrowing-heavy ones (Q3, Q4, Q6, Q7).
2. **T19 worked examples C72 (6 sacks) and C73 (9 kg 600 g shared), T21 C79 (cost of 4 kg 500 g), T23 C90 (cup and drum): none.** The question gives no figure, the steps are arithmetic or word reasoning, and nothing in the steps points to a picture. The teaching images of these concepts are not linked and did not influence the decision (user rule 5).
3. **T21 C80 "Scaling Both Lines Together": optional (not added).** Step 1 says "Draw a double number line. The top line is plates: 3 and 9. The bottom line is lentils: 240 g and ___ g." and later steps say "the top line", "the bottom line". The question itself gives no figure, so by the companion note no question figure is invented; text carries every number. The figure that would help: double number line, top 3 plates and 9 plates with arrow ×3, bottom 240 g and 720 g with arrow ×3. Not dropped because of the teaching image (M2.S21.T21.C80.IMG1 shows exactly this); dropped because the question gives no figure. See Borderline.
4. **Let Us Do 2 (C84/C85) and Let Us Do 3 (C86/C87): question required, solution required.** The book GIVES a double number line with two blanks (the amount for the larger quantity and the lower multiplier) and the learner completes it (ACTION_ON_FIGURE). The solution completes the same figure (derived_from the question diagram): the new content is `1,000 g` / `₹146` and the lower arrow `×2`, in ANSWER green. The top `×2` is printed by the book in the question, so it stays INK.
5. **Let Us Do 4 (C88/C89): question none, solution required.** The book does not print number lines here; it asks the learner to "make double number lines for (b) and (c)". No given figure, so no question figure (the picture beside the question is a scrap dealer with a cart: decoration). The answer is two drawings (ANSWER_IS_FIGURE). The pair gets ONE solution diagram, so both number lines are in one 16:9 picture, side by side, with the letters (b) and (c) drawn because the LP answer text names the parts by letter (user rule 3); no (a), part (a) is only 16 × 8 = 128. Colours: the numbers the question gives (10 kg, 20 kg, ₹200, 5 kg, 10 kg, ₹30) are INK; the multipliers, both arrows and the results ₹400 and ₹60 are ANSWER green (nothing here is a printed question figure, so the arrows count as added by the solution).
6. **No inventory figure maps to C89.** No book picture exists for it (the book asks the learner to make it), so the validator's one warning is expected ("fine only when the figure is not printed in the book").
7. **Let Us Do 1 table (C82/C83): none, LATEX_TABLE on both sides.** Plain 4-column table of weights and prices; the beige and green column colours are decoration. The filled answer is the same plain table with six totals; the v3 prompt's own example (filled digits table) keeps that as a LaTeX array. `text_alternative` on both items gives the array.
8. **Second uses of a book figure.** The solutions of Let Us Do 2 and 3 reuse the book's number line: entries `NEW-P09-double_number_line-1-sol` and `NEW-P10-double_number_line-1-sol` (base ids stay on the question items).
9. **Figures missing from the base, added as NEW-.** `NEW-P09-dialogue-1` (blue bubble beside the farmer example) and `NEW-P09-dialogue-2` (olive bubble beside the nuts example), both text only, none:TEXT_SUFFICIENT; `NEW-P10-illustration-nitesh` (scrap dealer with cart), none:DECORATIVE_ONLY. The base descriptions of P09-table-1, P09-double_number_line-1 and P10-double_number_line-1 match the page pictures; no corrections needed.
10. **Aspect ratio 16:9 for all five diagrams**, number lines drawn with two ticks and not to scale, as the book prints them (positions in the spec are layout choices, not data).

## 2. Mathematical recheck (all stated values recomputed)

Let Us Do 1: 5+8+12 = 25 kg, 200+900+600 = 1,700 g, total 26 kg 700 g = 26,700 g. Q2: 2,100+3,950 = 6,050 g. Q3: 10,000-4,500 = 5,500 g. Q4: 9,750-3,700 = 6,050 g. Q5: 17,900+12,700 = 30,600 g. Q6: 14,750-10,500 = 4,250 g. Q7: 65,000-42,275 = 22,725; 22,725+52,500 = 75,225 g = 75 kg 225 g. C72: 6 × 2,500 = 15,000 g. C73: 9,600 ÷ 3 = 3,200 g. Ex 6: 4 × 10,500 = 42,000 g. Ex 7: 4,800 ÷ 4 = 1,200 g. C79: 4 × 36 = 144, +18 = 162, 5 × 36 = 180. C80: 240 × 3 = 720. Table: 750, 290, 225, 252, 240, 70 all correct (12 × 60 + 30; 7 × 40 + 10; 5 × 45; 3 × 70 + 6 × 7; 4 × 60; 50 + 4 × 5). Q2 (rice): 500 × 2 = 1,000 g. Q3 (tomatoes): 73 × 2 = 146. Q4: (a) 16 × 8 = 128; (b) 200 × 2 = 400; (c) 30 × 2 = 60. C90: 200 l = 200,000 ml. No contradiction between the LP solutions and the book in this chunk, and no book print slip found.

## 3. LP text issues (not edited, per rule 2)

- **M2.S22.T22.C84 (Let us do: Q2) and C86 (Q3):** the question text does not mention the double number line the book gives and the learner completes. Suggested sentence: "Complete the double number line: 4 people need 500 g, so 8 people need ___ g (both lines are multiplied by the same number)." (C86: "5 kg cost ₹73, so 10 kg cost ₹___.")
- **M2.S22.T22.C82 (Let us do: Q1):** the table is written as a run-on sentence. Suggested: a LaTeX array as in the `text_alternative` of that item (and of C83 for the answer).
- **M2.S22.T22.C88 (Let us do: Q4):** the question text reads "(a) ... (b): 20 kg iron ... (c): 10 kg plastic" with colons after (b) and (c) only. Suggested: "(a) ... (b) ... (c) ..." with the same punctuation for all three; keep "Make double number lines for answering (b) and (c)."
- **M2.S22.T22.C89 (Ans4):** steps (b) and (c) describe the two number lines in words only. Once the diagram is placed before step 1, suggested wording for step 2: "Look at the double number line for (b): the top line goes from 10 kg to 20 kg."
- **M2.S21.T21.C80:** step 1 says "Draw a double number line" and steps 2-5 refer to "the top line" and "the bottom line" with no picture next to the example. Suggested: add "(see the double number line for this concept above)" or keep the picture decision as optional above.
- **M3.S23.T23.C90:** the question "A cup of juice holds 200 ml or 200 l? A drum of water holds 200 ml or 200 l?" is awkward. Suggested: "Which is right for a cup of juice, 200 ml or 200 l? Which is right for a drum of water, 200 ml or 200 l?" Also step 3 ("A drum holds much more than a cup. 200 ml is a small amount, so a drum holds 200 l") is circular; suggested: "A drum holds much more than a cup, and 200 l is much more than 200 ml, so a drum holds 200 l."
- **All worked blocks (C72, C73, C79, C80, C90):** every question ends with "These are practice values." which a learner reads as part of the problem. Suggested: remove it from the question text.
- **T20 titles "Example 6" / "Example 7":** the book prints these as plain "1." and "2." under More Operations on Weight (no example numbers), and the same two book examples are also the base of the T19 teaching concepts C72/C73 (mul.way / div.way), so the farmer's sacks and the nuts box are covered twice with different numbers. Not wrong, only a possible repetition for the reviewer.
- **T21 C79, C80 and T23 C90 have empty ncert_refs.** They are LP teaching examples, not book items; the book numbers given in `ncert_ref` of the items say where the book treats the idea.

## 4. Borderline (applied the v3 rules as written; user rule 4)

- **C84 and C86 question diagrams (required).** A careful student could compute the answer from the text alone, so by the tie-breaker alone they would be none. They are required because the book question is a figure to complete (blank value and blank multiplier on a given number line, ACTION_ON_FIGURE), and the LP's earlier card and `q_figure` note the figure belongs to the question. If the reviewer reads "the question text does not mention a figure" as decisive, the pair becomes: question none, solution required, `derived_from` null.
- **C80 worked example (optional, not added).** Could be read as required (steps ask for a double number line, B2 "the steps describe it in words"). I read it as optional because the question gives no figure and text carries every number. If the user wants it added, spec: double_number_line 16:9 in the layout of C84, top labels `3 plates` / `9 plates`, bottom labels `240 g` / `720 g`, both arrows `×3`, worked-example token after the question text.
- **C82/C83 table (none, LATEX_TABLE).** The filled answer is a table, so B2 "filled figure" could be argued; kept as a LaTeX array because it is a plain table without colour meaning (Step C, and the prompt's own example).
- **C88 question (none).** The book asks the learner to make number lines but gives none: no question figure is invented (companion note); only the solution has one.
- **T18 Q3, Q4, Q6, Q7 solutions (none).** Subtraction with borrowing could use a column picture, but column work is LATEX_ARITHMETIC and the book prints no picture for these questions.

## 5. Where the book itself is unclear

- The Let Us Do 2 and 3 number lines have only two ticks with no scale; the lower arrow label is printed as "×...." and the blank for the larger quantity as ".........." (with "g" or "₹" next to it). The spec draws these as dotted lines and uses no question marks.
- The book gives no answers, so the top arrow of Let Us Do 4 (b) and (c) (×2) and the order of the parts on one picture are taken from the LP solution, not from a printed answer.

### Chunk D notes (from the decision agent)
# Chunk D notes (Class 5 Ch 8 "Weight and Capacity", topics M3.S24.T24 to M3.S32.T32)

Result: 18 units, 32 items: required 4 (C103 q, C104 sol, C105 q, C106 sol), optional 1 (C125 sol), none 27. Validator: errors 0, warnings 0.
Figures claimed: 18 entries = 10 mapped to items (4 beaker groups + 4 "second use" entries for the solution, the double number line + 1 second use) + 8 none.

## 1. Judgement calls

- **C103 / C104 (Big to Small Q3, containers): ONE question diagram and ONE solution diagram for all four groups** (11 beakers on one 16:9 card, 2 x 2 grid like the book), not one per group, because the LP holds it as one question (brief: at most one question and one solution diagram per pair). Beaker heights/widths are not proportional to capacity (the book's are not either). The scale labels are 34 px or larger, so beakers are drawn 210 to 260 px wide and the labels sit inside them.
- **"Group 1:" to "Group 4:" labels are drawn** next to the blanks. The book prints no group labels, but the LP question and the LP solution both refer to "Group 1 ... Group 4", so the picture needs them (decision 3, applied by analogy to numbered groups).
- **C104 solution = required**: the filled totals go on the blank rules of the question figure and the top mark of every beaker is ringed (FOCUS), because the LP solution says a container's capacity is the top mark of its scale. See Borderline.
- **C105 / C106 (Milkman double number line): required on both sides.** The question side: the LP text does not list the ticks; the figure holds all the given values. The solution is the completed line (ANSWER_IS_FIGURE). Ticks are drawn equally spaced and equally long (the book spaces them unevenly, not to scale, and draws the first tick longer so "1 l" and "1000 ml" fit); order, values and blanks are exactly the book's. The book prints "1000 ml" / "2000 ml" without a comma; the LP's "1,000 ml" style is used.
- **Plain tables = text/LaTeX on both sides** (C107/C108 milk table, C118/C119 fuel table), even though each is a table to complete: Step C `LATEX_TABLE` and the Number Play "Counting Numbers" precedent. `text_alternative` gives the LaTeX array content for question and solution.
- **Column addition / subtraction pictures (Example 9 and 10, P13-column_addition-1, P14-column_addition-1, P14-column_subtraction-1) = none, LATEX_ARITHMETIC.** The C116 teaching image (column sums) is not linked and was not the reason.
- **Worked examples C96, C97, C115, C116 = none.** They are practice examples with every quantity in words and arithmetic work; they draw nothing of their own. The existence of the teaching images (C96.IMG1, C97.IMG1, C115.IMG1, C116.IMG1) was not used as a reason (decision 5).
- **C111 (Mary and Daisy) = none, DECORATIVE_ONLY**: the book picture is two girls at a tap with two speech bubbles; both claims are in the LP question text.
- **C125 (Example 10 solution) = optional (not added)**: the book's model "? ... 9 l with an arrow + 5 l 300 ml" would help, but the LaTeX subtraction carries it (Step D example "arrow picture for a sum already written as an expression"). The question side has no given figure (the page-14 pictures are the working), so none.
- **Not inventoried and not added:** the petrol-pump scene on page 12 (pump, car, attendant), the milkman on a bicycle on page 11 and the scrap dealer on page 10 are pure illustration without numbers.
- The figure-inventory entries `NEW-P11-measuring_container-1..4-sol` and `NEW-P11-double_number_line-1-sol` are the second uses (solution cards) of base figures, as the brief asks. The merge should treat them as extra entries, not as new book figures.

## 2. LP text issues

- **M3.S32.T32.C124** (Example 10 question): the text omits the data the question needs, the 5 l 300 ml that Sam put in (it exists only in Example 9 and in the book's arrow picture). The LP solution C125 uses it. Suggested sentence: "After refuelling, Sam found his fuel gauge reading 9 l. Sam had put in 5 l 300 ml of petrol. How much fuel did his bike have before refuelling?" (Also: the question writes "refueling", the steps "refuelling".)
- **M3.S26.T26.C103** (containers question): the question text does not describe the containers at all ("the following containers"); the data is only in the picture and the old q_figure hint. It works once the diagram C103.IMG1 is in. Suggested extra sentence: "Each beaker has a scale; the capacity of a beaker is its top mark. Group 1 to Group 4 are shown in the picture."
- **M3.S27.T27.C105** (milkman): "Complete the double number line" lists none of the given ticks; they live only in the picture C105.IMG1. Suggested: nothing to change once the picture is in, but without it the question cannot be attempted.
- **M3.S24.T24.C93** (tea solution), step 3: broken math delimiters, `$150\text{ ml} ($a practice value; ...` has the opening parenthesis inside the math and the rest outside. Suggested: "Take a cup of about $150\text{ ml}$ (a practice value; cups are not all the same). Two cups hold $2 \times 150 = 300\text{ ml}$." The answer_tex has the same pattern: `$(200\text{ ml}$ of water, ...`. Suggested: "Sample answer: about $300\text{ ml}$ in all (with $200\text{ ml}$ of water and $100\text{ ml}$ of milk). No, $1\text{ l}$ is not needed. Yes, $500\text{ ml}$ is enough. Your answer may differ."
- **M3.S31.T31.C118 / C120**: the LP numbering differs from the book. LP "Let Us Compare Q1" is the book's intro line 1 (Kiran's petrol pump) plus item 2 (the table with (a), (b)); LP Q2 is the book's item 3. Only a numbering remark; the text matches the book.
- **M3.S30.T30.C115 / C116, M3.S25.T25.C96 / C97**: these practice examples have no book source (ncert_refs empty or note only); no text problem found.

All sums, conversions and comparisons in the 14 pair solutions and the 4 worked blocks were recomputed and are right (for example C119: 1,500 + 1,800 + 500 + 96 + 125 = 4,021; C121: 5,600 > 5,400, 10,100 > 1,600, 990 > 909, 3,600 = 3,600, 4,050 < 4,500; C125: 9,000 - 5,300 = 3,700).

## 3. Borderline

- **C104 solution (containers): required, could be none.** Step E lists "figure-based question, numeric answer: S none". Kept required because the printed blanks sit on the figure and the LP solution's key idea (capacity = top mark) is a highlight on the figure that text cannot show (HIGHLIGHT_MEANING). If the user prefers the typical-pair rule, change C104 to none (SAME_AS_QUESTION_DIAGRAM) and drop its four NEW- inventory entries (they would become none:SAME_AS_QUESTION_DIAGRAM).
- **C105 question: required although the book's own line already prints "2000 ml"** (the first question). Kept as the book prints it; the six blanks are the task.
- **C107 / C108 and C118 / C119: tables to complete are none** (LaTeX table) on both sides, although a filled table can count as ANSWER_IS_FIGURE; the plain-table rule was applied as in the Number Play precedent.
- **C125 solution optional** (the arrow model, see above).
- **C92 / C93 tea:** a measuring jug marked 300 ml / 500 ml / 1 l would be a nice picture, but the text carries everything (TEXT_SUFFICIENT, none on both sides).
- **C96, C97, C115, C116 worked examples:** none although each has a teaching image; the picture need was judged on the example itself.

## 4. Where the book itself is unclear

- **Page 11 beaker scales are printed very small.** After enlarging the page 2 times I read: 1 l beaker with "1 l" at the top and "500 ml" at the middle, 4 short ticks in each half (100 ml steps); 500 ml beaker with labelled marks 100 to 500 ml and one short tick between each pair; 100 ml beaker with "100 ml" at the top, "50 ml" at the middle and 4 short ticks in each half. The exact short-tick counts of the 1 l and 100 ml beakers are at the edge of what the print shows (they follow the inventory), but no answer depends on them: capacity is the top mark.
- **Group 1, first beaker:** the "1 l" label is printed left of the scale line, in the other 1 l beakers to the right. The diagram puts every label to the right of its scale line.
- **Double number line (page 11):** the tick spacing is not to scale and does not carry meaning; see Judgement calls.
- No book print slip was found in the figures of this chunk (all values in the pictures agree with the LP solutions), so decision 1 (correct values) was not triggered.

### Chunk E notes (from the decision agent)
# Notes, chunk E (Class 5 Ch 8 "Weight and Capacity")

Units: 67 (worked example M3.S33.T33.C126) and 68-72 (Let Us Solve Q1-Q5, topic M3.S34.T34). Result: 11 items, required 0 / optional 0 / none 11. Validator: errors 0, warnings 0.

I looked at book page 15 (Let Us Solve) in the page picture: it is plain text, no figure of any kind (only the NCERT watermark and the closing line "Use the double number line whenever needed to solve such problems."). The base inventory has no entry on page 15, and the worked example C126 has no printed counterpart in the book. So this chunk claims no inventory figure (`figure_inventory` is empty, `coverage_report` all zeros). The merged-map completeness check is not affected: no base figure belongs to these units. The inventory agents' `unclear` doubts concern figures of other chunks.

## Judgement calls

1. **M3.S33.T33.C126 (worked example, 6 jugs of 1 l 250 ml and 9 l 600 ml into 8 cans): none** (TEXT_SUFFICIENT, LATEX_ARITHMETIC). Every number is in the text, the steps are l/ml multiplication and division, nothing is referred to as a figure, the answer is not a picture. The decision is made on the rules and the tie-breaker, not because the kept teaching image M3.S33.T33.C126.IMG1 already shows the jugs and cans (user decision 5 respected: no REUSES_CONCEPT_IMAGE, no link, teaching image untouched).
2. **Let Us Solve Q1 to Q5, question side: none.** The book prints no figure for any of them and the questions give none, so no question diagram (companion note: never invent a "given" figure). Reason TEXT_SUFFICIENT.
3. **Let Us Solve Q1 to Q5, solution side: none.** Every answer is a number, a name or a price, reached by conversion and arithmetic (LATEX_ARITHMETIC, TEXT_SUFFICIENT). No printed-solutions section exists in this pdf, and the LP answers are text, so the "printed answer is a picture" rule does not fire. Sibling consistency holds: all five pairs get the same decision on both sides.
4. Q2 and Q3 have lettered parts (a), (b), (c): these are sub-questions, not lettered figures. No figure letters are drawn anywhere (no diagrams at all).

## Borderline (applied the v3 rules as written; none flipped for LP-text reasons)

- **C126 worked example.** Could carry a jugs-and-cans picture (a teaching image of exactly that already exists), but no trigger makes the figure necessary and the tie-breaker answer is "a careful student solves it from the text". Kept none.
- **Q1 (Riya vs Aarav).** A side-by-side jugs comparison (Riya 4,000 ml against Aarav 2,250 ml) would be nice, but it only makes the answer prettier: optional at most, and optional is not added. Kept none.
- **Q3 (a) (5 l into 250 ml glasses).** A row of 20 glasses or a double number line would help some learners, and the book's closing line says to use a double number line "whenever needed". But the question gives no figure and the answer is the number 20 by division. Kept none.
- **Q2 (b) (bottle poured into 8 glasses).** A bottle-and-glasses picture would only restate the text. Kept none.

## LP text issues

(Listed only; no decision was changed because of them.)

- **M3.S33.T33.C126**: the question text ends with "These are practice values." This looks like a leftover authoring note, not part of the problem. Suggested: delete that sentence.
- **M3.S33.T33.C126**: the block has only plain `question` / `steps` / `text` (units written as "1 l 250 ml", "6 × 1 l 250 ml") and no `question_tex` / `steps_tex` / `answer_tex`, unlike the Let Us Solve concepts. If a diagram were ever added to this block, its token has no `question_tex` to go into. Suggested: add LaTeX versions, e.g. `$6 \times 1\text{ l}\; 250\text{ ml}$`.
- **M3.S33.T33.C126**: `ncert_refs` is "ls.dnl", which is not a book reference (the book has no printed example of multiplying or dividing capacities; the nearest book items are the weight examples on p.9). No `book_number` either.
- **M3.S34.T34.C130 / C131 (Q2)**: the LP solution step (b) says "each glass is filled to its capacity, so 2,880 ml was poured", but neither the LP question nor the book says the glasses are filled to capacity. Suggested sentence for the question: "Each glass is filled up to its capacity."
- **M3.S34.T34.C128 to C137 (Q1-Q5)**: the book's closing line "Use the double number line whenever needed to solve such problems." is not carried by any of these LP concepts. Suggested: add it once as a hint under Q1 (or as a closing line of the topic).
- **Answer concepts C129, C131, C133, C135, C137**: `item_kind` is "unsolved" although they hold the worked answers. Probably a harmless pipeline label; no change needed for diagrams.
- The question and answer concepts repeat the full question text (answer concept's `question` field). That is the LP design, not an error.

All LP solution arithmetic was recomputed and is right: Q1 4,000 and 2,250 ml, difference 1,750 ml; Q2 8 × 360 = 2,880, + 120 = 3,000, 3 × 40 = 120; Q3 5,000 ÷ 250 = 20, 5,000 − 2,500 = 2,500, 20 × 25 = 500; Q4 8,400 ÷ 7 = 1,200; Q5 8 × 1,075 = 8,600; C126 6 × 1,250 = 7,500 and 9,600 ÷ 8 = 1,200.

## Book unclear

- Let Us Solve Q2: the book does not say whether the 8 glasses are filled to the brim. Part (a) asks the total capacity of 8 glasses and part (b) the initial milk, so the intended reading is "each glass is full" (as the LP solution states). Noted above as an LP text issue.
- No book errors found on page 15 (digits, units and counts match the LP text).
