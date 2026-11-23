# Class 7 Ch 4 Expressions using Letter-Numbers - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths7_ch4` v41 (taken from staging). Result: new V2 version v42 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (120 items from 62 units)
{"question": {"none": 39, "required": 19}, "solution": {"none": 39, "required": 13, "optional": 6}, "worked_example": {"none": 4}}

Optional, NOT added: [('C40', 'solution'), ('C92', 'solution'), ('C148', 'solution'), ('C150', 'solution'), ('C152', 'solution'), ('C154', 'solution')]

needs_lp_text_sync: []

## The 32 diagrams
| id | side | type |
|---|---|---|
| M1.S8.T8.C35.IMG1 | question | cell_grid |
| M1.S8.T8.C36.IMG1 | solution | cell_grid |
| M2.S14.T14.C59.IMG1 | question | mensuration_figure |
| M2.S14.T14.C60.IMG1 | solution | mensuration_figure |
| M2.S15.T15.C63.IMG1 | question | mensuration_figure |
| M2.S15.T15.C64.IMG1 | solution | mensuration_figure |
| M2.S20.T20.C83.IMG1 | question | arrow_map |
| M2.S20.T20.C84.IMG1 | solution | arrow_map |
| M2.S20.T20.C85.IMG1 | question | number_pattern |
| M2.S21.T21.C87.IMG1 | question | arrow_map |
| M2.S21.T21.C88.IMG1 | solution | arrow_map |
| M2.S22.T22.C91.IMG1 | question | number_pattern |
| M2.S24.T24.C99.IMG1 | question | other |
| M2.S24.T24.C100.IMG1 | solution | other |
| M2.S24.T24.C101.IMG1 | question | other |
| M2.S24.T24.C102.IMG1 | solution | other |
| M3.S29.T29.C115.IMG1 | solution | cell_grid |
| M3.S29.T29.C116.IMG1 | question | cell_grid |
| M3.S29.T29.C117.IMG1 | solution | cell_grid |
| M3.S31.T31.C121.IMG1 | question | number_pattern |
| M3.S31.T31.C123.IMG1 | question | number_pattern |
| M3.S31.T31.C125.IMG1 | question | number_pattern |
| M3.S31.T31.C126.IMG1 | solution | number_pattern |
| M3.S32.T32.C135.IMG1 | question | flow |
| M3.S32.T32.C136.IMG1 | solution | flow |
| M3.S32.T32.C138.IMG1 | solution | other |
| M3.S32.T32.C147.IMG1 | question | other |
| M3.S32.T32.C149.IMG1 | question | number_pattern |
| M3.S32.T32.C151.IMG1 | question | object_row |
| M3.S32.T32.C153.IMG1 | question | number_pattern |
| M3.S32.T32.C155.IMG1 | question | cell_grid |
| M3.S32.T32.C156.IMG1 | solution | cell_grid |

### Chunk A notes (from the decision agent)
# Chunk A notes (Class 7 Ch 4, plan cbse_eng_maths7_ch4_v41)

Units: 15 pairs (30 items) in topics M1.S3.T3, M1.S4.T4, M1.S6.T6, M1.S7.T7, M1.S8.T8, M1.S10.T10.
Result: required 2 (Figure it Out 4.1 Q7 question and solution), optional 1 (solution of M1.S10.T10.C40), none 27. Figures claimed: 12 (3 to items, 1 to a concept image, 8 none). Validator: errors 0, warnings 0.

## 1. Judgement calls

1. **Figure it Out 4.1 Q3 (C27 question, C28 solution) kept as LaTeX, not a diagram.** The book's table (and its printed answer, P27) is a plain table of counts, letters and expressions; the red in the printed answer only marks what was filled in. The prompt's own example ("Complete the table of how many numbers have 1 to 5 digits" -> none, LATEX_TABLE) and the brief ("plain tables ... stay text/LaTeX") point the same way, and the LP steps already give every row. The other reading is B2 "printed answer is a picture / filled table -> required (ANSWER_IS_FIGURE)". If the user wants the filled table drawn, change both sides of C27/C28 to required (derived_from question), 4 columns x 4 rows as in P27. The `text_alternative` of C27 and C28 holds the LaTeX array to write.
2. **Figure it Out 4.1 Q7 (C35 question, C36 solution): required both.** Question figure = what the book gives, side by side: the calendar with the outlined block 12, 13, 14 / 19, 20, 21 (P05-calendar-1) and the blank 2 x 3 grid with only `w - 1` and `w` filled (P05-grid-2). The LP question text names only the bottom middle `w`; the given bottom-left `w - 1` and the "blank cells" exist only in the figure, so the question needs it (FIG_REFERENCED, DATA_IN_FIGURE, ACTION_ON_FIGURE). Solution figure = the completed grid (printed answer P28 shows the grid alone) with the four new labels in ANSWER green; the calendar is repeated unchanged so the solution keeps the question figure's layout (`derived_from` rule). Alternative if a leaner picture is preferred: draw the grid alone on both sides and drop the calendar (then P05-calendar-1 becomes none:DECORATIVE_ONLY or TEXT_SUFFICIENT).
   - The book's calendar title "November 2024" is NOT drawn (headings are not allowed in diagrams). Also the weekdays in the book's picture are one day off the real November 2024 (the book puts the 1st on Saturday; 1 Nov 2024 was a Friday). The picture is internally consistent (1 on Sat, 12 on Wed), so I kept the printed arrangement and dropped the title instead of "fixing" it. Said in the spec's `render_note`.
3. **Unit 15 (M1.S10.T10, Revisiting Arithmetic) solution: `optional`, not added.** The book prints two pictures inside its 4.2 teaching text: boxed terms with two crossing curved arrows for 83 + 28 - 13 + 32 (P06-1), and two rows-of-boxes methods for 68 - (18 + 13) (P06-2, P06-3). The LP steps write the same grouping with brackets, so the picture would only be nicer (prompt Step D: "an arrow picture for a sum that is already written as an expression"). Also the pair is allowed ONE solution diagram while the card holds three expression groups. The three P06 figures are therefore mapped none:LATEX_ARITHMETIC. The question side is none (LATEX_ARITHMETIC). If the user wants them, they would be a separate "boxed terms + arrows" diagram per group, which the one-diagram-per-side rule does not allow on this card.
4. **Example 2, Parthiv's Ls (C8 question, C9 solution): none/none.** The text gives every number needed (2 sticks per L; 5, 7, 45, n Ls), so Fig. 4.2 (1, 2, 3 Ls) is not needed to attempt it and the answer is numbers and 2 x n. P02-pattern-1 is accounted as the teaching figure of that idea: concept image M1.S2.T2.C4.IMG1 (it shows 3 Ls with a brace; accounting only, nothing linked). If the user would rather treat Fig. 4.2 as "needs its own figure because the book says 'as shown in Figure 4.2'", it would be an `object_row` of 1, 2, 3 Ls, but the LP question does not refer to the figure.
5. **Fig. 4.1 (Aftab/Shabnam table, P01) -> none:LATEX_TABLE** on the Example 1 solution (C7); text_alternative holds the array. The Example 1 question and the age-from-Shabnam pair (C10/C11) have no figure.
6. **Example 3 table (P03-table-1) -> none:LATEX_TABLE** (on C20); **term boxes (P03-term_boxes-2) -> none:TEXT_SUFFICIENT** (on C22; two boxes around c x 35 and j x 60 carry no extra meaning, `\boxed{}` possible).
7. **Word-only items kept none even where a picture would be pleasant:** Example 4 square (C17/C18; a labelled square is already concept image M1.S5.T5.C13.IMG1, and the book prints no figure there), Figure it Out Q1 (regular triangle, pentagon, hexagon, C23/C24: the book prints no figure; three polygons marked `a` would be a nicety, not a need), Q2 (joined pipes), Q4 (mill options), Q5 (phrases), Q6 (open-ended situations; reason OPEN_ENDED). No `optional` was used for these, to keep to "prefer none".
8. **Sibling consistency:** Q3 table and Q7 grid are the only two figure-like answers in 4.1; Q3 went LaTeX because it is a plain table, Q7 went diagram because the answer is a cell arrangement of letter-expressions in a calendar grid. If the user overrules item 1, Q3 becomes a required pair as well.

## 2. Things in the LP that look off

- **Figure it Out Q3 (C27):** the LP question text states the worked row's counts ("Row 2 is 6, 4 and 3 notes"), but the book leaves those three count cells blank and gives only `6 x 100 + 4 x 20 + 3 x 5 = 695`; the learner has to read the counts off the expression (the printed answer fills 6, 4, 3). The LP question text also does not show the table, only describes it in words. Content is consistent with the printed answer.
- **Figure it Out Q7 (C35):** the question text names only the bottom middle `w`; the bottom-left `w - 1` and the calendar picture appear only in the figure (now supplied by the required diagram). Worth adding "the bottom left cell is w - 1" to the text if the figure were ever dropped.
- **Example 1 (C6):** the book's own first question uses Aftab's age 18 (and 10 -> 13 as a lead-in); the LP asks for the value at 23 (the book's later "If a is 23"). Harmless.
- **Brief vs PDF:** the brief says the PDF has no printed-solutions section, but pages 26 onwards hold printed answers ("Ans:"), including the picture answers P27 (Q3 table) and P28 (Q7 grid). The LP solutions were followed, as instructed; they agree with these printed answers (Q3: 430, 695, 880 + 5z, 100x + 20y + 5z; Q7: w-8, w-7, w-6 / w-1, w, w+1; Q1: 3a, 5a, 6a; Q2: 20 + k; Q4: (d); Q5: d + 5, d - 4, 13d - 2, 2d - 13; Example 3 second part: 820).
- All arithmetic in the LP solutions of this chunk was recomputed and is right: 10, 14, 90; 17; 350 + 300 = 650; 28; 280 + 540 = 820; 245 + 240 = 485; 430, 695, 880 + 5z; 10 + 8 x 3 = 34; 3, 82, 100; 130, 40; 56, 37 (both ways).
- `book_number` labels in the LP ("Age Rule: ...", "Laddu Order: ...") are LP names, not book numbers; the book's items sit in Examples 1 to 4 and Figure it Out 4.1.

## 3. Where the book itself is unclear

- The calendar picture (Q7): title "November 2024" but weekdays shifted by one day against the real month (see 2.2 above).
- The Q3 table: three blank count cells in row 2 while the last cell is filled (intentional in the book; the learner reads the counts from the expression).
- Q7 grid in the printed answer: the letter `w` is italic in the bottom-left and bottom-middle cells and upright elsewhere (typesetting only). The diagram uses an italic `w` throughout, as the question figure.
- Base inventory descriptions P01 to P06, P27, P28 were checked against the page pictures: all correct (P27: red = filled in; P05 calendar highlights exactly 12-14 and 19-21; Sat = 1).

### Chunk B notes (from the decision agent)
# Chunk B notes (Class 7 Ch 4, units 16-31)

Result: 31 items = 7 required (4 question, 3 solution), 0 optional, 24 none. Validator: errors 0, warnings 0.
Diagrams: Example 6 first part (C59 q, C60 sol), Example 6 second part (C63 q, C64 sol), Example 10 (C83 q, C84 sol), Example 11 (C85 q).

## 1. Judgement calls

- **Example 6 first part, C59 (question required).** The LP question already states the heights, widths and even the areas 4v and 3v in words, so a text-only reading is possible. I made it required because the book question is "split into two smaller rectangles *as shown*" and the whole point of the example is the area model; it also matches its lettered sibling C63. If you want text-only, flip C59 and C60 to none (TEXT_SUFFICIENT); the question figure only repeats the numbers in the text.
- **Example 6 solutions, C60 and C64 (solution required).** The solution adds visual content to the figure (part areas, the widths 4 + 3 = 7 or 12 - 4 = 8, the shaded piece AEFD, 4n, 8n) so the two ways can be seen on it; the book prints no answer picture. Both are kept the same (sibling consistency). Weakest of my seven: an `optional` reading is defensible ("figure would help but the text is complete"). Both are derived_from their question diagram.
- **Example 10, C83 and C84 (both required).** Clear: the book asks to fill the blanks of two arrow diagrams, and the printed answer (page 29) is the two filled diagrams. Each item gets ONE 16:9 picture that holds both stars side by side (the brief allows one diagram per side). The book's red/blue arrow-label colours are dropped (all INK; they carry no meaning).
- **Example 11, C85 (question required, solution none).** The LP question describes the tile picture in words, but the book question is "the sum of the numbers in the picture" and the three ways (rows, like terms, upper half) read off the layout. The same picture is the teaching image M2.S19.T19.C80.IMG1 of the earlier topic T19; per v3 it is not linked and the item gets its own diagram. The solution only restates the picture with three expressions, so SAME_AS_QUESTION_DIAGRAM (a colour-grouped copy would be a nicety, not needed).
- **Unit 20 worked example, C53 (none).** Text gives l and b; the book's own picture is an empty rectangle (l and b appear only in text), and the concept already keeps its labelled teaching image C53.IMG1 which is never linked. A second identical rectangle in the same card would only duplicate it. P07-shape-2 is mapped to that concept image (accounting only). Other chunks' worked examples inside teaching concepts may be decided differently; I did not coordinate.
- **Plain tables, none.** Example 5 table (P08-table-1, used by C57 and C61) and the two Example 7 tables (P10-table-2/3, C69) are plain tables with the numbers already in the LP question text: LATEX_TABLE. `text_alternative` says which LaTeX array to write if the tables are wanted.
- **Mind the Mistake cards, none (C51).** Nine rounded boxes with one claim each, position carries no meaning, all nine claims are in the three LP blocks: NUMBER_LIST_IN_BOXES / TEXT_SUFFICIENT. The earlier author's `s_figure` hint (nine corrected cards) is not followed: the book prints no answer picture for these cards, and the LP answer is text. Consistent with the later Mind the Mistake table (plain table, none).
- **No question figure invented.** C45-C50, C71-C78 have no book figure and stay none on both sides.
- **NEW- inventory entries.** `NEW-P09-shape-1-sol` and `NEW-P10-shape-1-sol` are the second uses (solution diagrams) of the two Example 6 book pictures, per the "a figure used by two items is two entries" rule. They exist only in this chunk; the merger can keep or drop them (dropping needs C60/C64 to stay claimed by something, otherwise the only effect is a 'required but no inventory figure' warning).
- **Not claimed here (belong to chunk C, unit 32/34):** P13-arrow_diagram-1/2 and P29-arrow_diagram-3/4 (Math Talk 10y - 3 versus 10(y - 3)), P29-number_tiles-5/6/7 and P14-pattern-1/2/3 (Figure it Out Q1). All other base figures of pages 7-13 and the answers on page 29 for Example 10 are claimed.

Geometry choices stated in the specs: Example 6 widths drawn 4 : 3 and the second figure drawn AB 12 : AE 8 : EB 4 (drawn 9 : 6 : 3); the heights v and n are not to scale (the book draws them freely). Colour: question content INK, solution additions ANSWER green, shaded piece AEFD MARK_FILL, tile squares MARK_FILL and circles CELL_FILL.

## 2. Things in the LP that look wrong or thin

- **M1.S12.T12.C52, block E2, claim 7**: "The claim 2 likely subtracts the numbers 3 and 1 before multiplying." Subtracting first and then multiplying by 2 gives 2 x (3 - 1) = 4, which is the correct value. The claimed 2 comes from 3 - 1 with the factors 2 left out. Suggest: "likely subtracts 3 and 1 and forgets the 2s".
- **C52, block E2, claim 9**: "The claim 4 likely drops the sign of the bracket" - 5 - 3 - 6 = -4, so the claim matches only in size; wording is loose (e.g. "likely subtracts 3 and 6 separately and loses the sign").
- **M2.S20.T20.C83 question text** ("Replace u by 11, 8, 2 and 5 in 5u and in 5 + u ...") does not tell the learner to fill the boxes of the two diagrams, and does not mention that the book gives the u = 2 case (10 and 7) as the example. With the diagram placed after the text this works, but a sentence "fill the boxes of the two diagrams; the u = 2 values are given" would help (LP text sync, not flagged as required).
- **M2.S14.T14.C57 (Example 5 question)** covers only the pencil part of the book question; the eraser part and the total are in M2.S15.T15.C61. Fine, but C57 is therefore shown without the eraser row of the book table.
- **C59** states "areas 4v and 3v" in the question; the book gives them after the figure as part of the explanation. The question figure follows the book (only v, 4, 3), the solution figure adds the areas.
- **Item numbering**: the LP `book_number` strings are descriptive titles, not NCERT numbers; `ncert_ref` in the map is built as "Section <4.3|4.4> - <title>".

## 3. Where the book is unclear

- Page 10 figure (rectangle ABCD): the printed dashed line sits at about 70 % of AB although AE : AB = 8 : 12 = 66.7 %; the label 12 is printed left of the middle of the AB arrow although the arrow spans A to B. I drew the exact proportions and put 12 in the middle.
- Page 9 figure: part widths 4 and 3 are drawn about 4 : 3 (left about 163 px, right about 130 px); height v is arbitrary. The book's grey fill and the callout bubble ("Another way of seeing the distributive property") are left out.
- Page 7 (before 4.4): the book draws an empty rectangle with no labels; l and b are introduced only in the text of the next page (so that figure is a teaching figure, see C53).
- The brief says the PDF has no printed-solutions section, but pages 26-41 do hold printed answers; the only one used here is page 29 (Example 10, the two filled diagrams). The 5u and 5 + u values (55, 10, 40, 25; 16, 7, 13, 10) match the LP solution text.

### Chunk C notes (from the decision agent)
# Chunk C notes (Class 7 Ch 4, topics M2.S21.T21 to M3.S31.T31)

Result: 29 items, required 14 / optional 1 / none 14. Validator: errors 0, warnings 0.
Questions: required 8, none 5. Solutions: required 6, optional 1, none 6. Worked examples: none 3.

## 1. Judgement calls (item, choice, why)

The calls most likely to be flipped by the user are the question-side "required" ones, where the LP text restates the data but the book's figure is the activity or carries the arrangement.

- C87 question (Math Talk, 10y - 3 and 10(y - 3)): required. The LP text gives the numbers, but the book task is "fill the two star diagrams" (one box given in each) and the printed answer is the filled diagrams, so the pair is required/required (derived). If the user wants text-first, the question can drop to none and the solution then stands alone (derived_from null); the solution stays required.
- C89/C90 (Mind the Mistake table, three claim blocks): none/none, LATEX_TABLE. The book table and both printed answer tables (pp 31, 32) are plain black text, no colour. All three claim blocks share one card, so one decision.
- C91 question (FiO 4.4 Q1, tile pictures): required, one diagram holding pictures (i), (ii), (iii) left to right (the LP did not split the question into parts). No picture letters are drawn (v3 forbids figure letters); the order is the question's order.
- C92 solution: optional. The printed answer is two text methods; the tiles are only reprinted above it (P29-number_tiles-5/6/7, mapped none:SAME_AS_QUESTION_DIAGRAM). Outlining like terms in matching colours would help, but the steps already say it, so nothing is added.
- C93/C94 (FiO Q2): none/none, pure simplification.
- C97 (make a formula of your own): none, OPEN_ENDED. The book has no figure; a picture of the four model machines would only show the model answer. A LaTeX table of the four input pairs would do.
- C99/C100 and C101/C102 (Formula Detective): all four required. The book figure (rows of Y machines with empty "expression:" lines and empty results) is the object the learner completes (ACTION_ON_FIGURE), and the printed answer for C102 is a picture (P33). C100 got a solution picture by sibling consistency, although the book prints no answer picture for the first machine row (its expression is only in text). C101/C102 each hold two blocks on one card, so each side has ONE diagram with both rows (10 machines in two rows of 5). Solution draws the formula both in the last result box (as the book does) and on the "expression:" line (as the LP steps do).
- C106/C107 (Example 12 saree): none/none. The book picture is six detailed flower motifs, not renderable and decorative; "A, B, C repeat" is in the text. The A B C strip with positions 1 to 9 is already the teaching image of the topic (C103.IMG1, not linked), so the solution gets no new copy (TEXT_SUFFICIENT).
- C108/C109: none/none. Quotient and remainder table is a plain table (LATEX_TABLE).
- C111, C113 (calendar worked examples): none, no figure in the book. C111's square 9, 10, 16, 17 and C113's row a - 1, a, a + 1 are fully in the steps.
- C114 question: none (text gives the four dates and their places); C115 solution: required, the grid a, a + 1 / a + 7, a + 8 with both diagonals marked (ANSWER_IS_FIGURE: the book says the numbers "can be represented as shown in the grid"). The question has no diagram, so this one has derived_from null. The two diagonal lines run 70 px past the grid corners so that the two "2a + 8" tags sit outside the grid.
- C116 question: required (the text lists the five dates, not their places; the shaded plus shape shows which is above, below, left, right, which the proof needs). C117 solution: required (printed answer picture P33-table-1). The solution replaces 8, 14, 15, 16, 22 by a - 7, a - 1, a, a + 1, a + 7 in ANSWER green, exactly as the book's printed answer, on the same grid and shading.
- Matchsticks: C121, C123, C125 questions required (the pattern, 3 sticks at Step 1 and 2 more each step, is only in the picture; the LP texts never describe it). Same spec for the three (one diagram per item). C122 solution none (plain table, LATEX_TABLE), C124 solution none (algebra), C126 solution required: the answer is read from colour (horizontal sticks SET_A, diagonal sticks SET_B, a key, and the counts 1 and 2, 2 and 3, 3 and 4, 4 and 5 under Steps 1 to 4). Step 1 counts are not in the LP steps (it names Steps 2 to 4); they follow the picture and the rule y and y + 1.
- C125 question picture is drawn plain (all sticks INK). I did not copy the book's page 21 "yellow glow" picture: it lights only the inner slanted sticks, the book does not say why, and it has no Step 4.
- Step labels in the matchstick figures are "Step 1" to "Step 4" (the book prints only 1 to 4 under the strips), to match the question text.
- Machines are drawn without the book's gear icon and without the blue/purple/green row colours (decorative). All result boxes use MARK_FILL; the last machine of each row has a wider box so a formula fits, in question and solution alike.

## 2. Anything in the LP that looks wrong

- C93/C94 lettering: the LP has parts (a) to (l) (12 expressions) because it split the book's first line "(a) p + p + p + p, p + p + p + q" into two. The book lettering is (a) to (k) (11 lettered parts, the first holds two expressions), and the printed answer on p 31 groups the answers under six letters (a) to (f). Also the LP label of part (i) is plain text in question_tex, steps_tex and text, while the other labels are written "$(a)$" and so on in math mode.
- C124 (answer to Q2 of matchsticks) carries video_media_id "M3.S31.T31.C125.VID1", which names the concept after it (C125 is the Q3 question concept); the answer concept of Q3 (C126) has no video. Looks like an off-by-one in the video ids.
- C107 step 4 repeats the C positions 3, 6, 9 already given in step 1.
- C121/C123/C125 question texts do not state what the pattern is (3 sticks at Step 1); they only work with the picture. Fine with the new diagram, but the old no-picture version would be unanswerable.
- C116 question text lists the five dates without their places; fine with the diagram.
- C88 order of values: LP replaces y by 2, 10, 0, 7; the book's diagram order (upper left to lower right) is y = 2, 0, 10, 7. The diagram follows the book, the steps follow the LP; both are correct, only the order differs.
- C101 (hint q_figure/s_figure) writes the product machine as "ab + 1"; the book's printed box reads "a x b + 1" and the LP steps say "a x b + 1, written ab + 1". The diagram uses "a x b + 1" (book).
- C100 s_figure hint says the figure shows "2 x 5 - 2 = 8" under each machine; the diagram writes the expression only (the result is in the result box).

## 3. Where the book itself is unclear

- Printed answer row 4 of the Mind the Mistake table (p 31) reads "x + 5" in the "Simplest Form" column, while the question page (p 14) and the LP say "x + y". Corrected answer column reads x - y in both. LP is right.
- Book FiO Q2: question lettering (a) to (k) with two expressions under (a), but answers grouped as (a) to (f) on p 31 (see section 2).
- P21-pattern-1 (matchstick page 21): the yellow glow lights only the inner slanted sticks (checked on an enlarged crop); the text does not say what the glow marks. Not used.
- Page 32 prints "No. of letters [box] no of terms" with a missing glyph; it means "less than or equal to".
- P16-pattern-3 (saree): D, E, F look identical to A, B, C by eye; not pixel-compared. Irrelevant for the diagrams (not drawn).

## 4. Inventory accounting (for the merge)

- Claimed figures: 35 entries (items 20, concept images 3, none 12). Four are extra uses with NEW- ids: NEW-P15-number_machine-1-sol (C100 solution), NEW-P20-pattern-1-C123 and NEW-P20-pattern-1-C125 (the second and third use of the matchstick picture), NEW-P21-pattern-1-C126-sol (C126 solution, orientation colouring).
- Not claimed, belong to other chunks: P29-arrow_diagram-1 and -2 (printed answers of Example 10, chunk B, M2.S20.T20 ex10_u), P12 and P13-pattern-3 (Example 10 and 11, chunk B), P27-table-1, P28-grid-1 and the figures of Figure it Out Q5, Q11 to Q15 (chunk D / end-of-chapter).
- Concept images used for accounting only, nothing linked: M3.S25.T25.C103.IMG1 (saree, P16-pattern-3), M3.S28.T28.C110.IMG1 (2 by 2 calendar square, P18-grid-2), M3.S30.T30.C119.IMG1 (two kinds of matchstick, P21-pattern-1).
- P18-calendar-1 is mapped none:TEXT_SUFFICIENT rather than to a concept image: the teaching image shows only the 2 by 2 square, not the calendar.

### Chunk D notes (from the decision agent)
# Chunk D notes: Class 7 Ch 4, topic M3.S32.T32 "Figure it Out 4.6" (Q1 to Q15)

Result: 30 items (15 pairs): required 9, optional 4, none 17. Validator: errors 0, 1 warning (Q6 solution, see below: the figure is not printed in the book).

| Q | question side | solution side |
|---|---|---|
| 1, 2, 3, 4 | none (no figure given) | none |
| 5 | required (star of paths, 4 empty ovals) | required (printed answer is the filled figure) |
| 6 | none (no figure given) | required (the rough diagram the hint asks for) |
| 7, 8, 9 | none (LaTeX) | none (LaTeX) |
| 10 | none (open ended) | none |
| 11 | required (3 rope pictures) | optional |
| 12 | required (3 matchstick figures) | optional |
| 13 | required (5 coloured signal lights) | optional |
| 14 | required (3 X patterns) | optional |
| 15 | required (4-column grid) | required (printed answer to (d) is the grid with multiples of 3 shaded) |

Media ids are all `<concept id>.IMG1` (no kept images in any of these concepts).

## 1. Judgement calls

- **Q6 solution = required (the one I am least sure of).** The printed answer is text only (22 minutes, 4t + 6), so no B2 rule forces it. I chose required because the book's hint says "Draw a rough diagram to visualise the situation", the typical slip is 3 journeys instead of 4, and the LP's own `s_figure` already describes the drawing; by the tie-breaker the picture changes how correctly the student solves it. Question side is none (the book gives no figure; a question figure would invent one). If you prefer text only, change it to optional/none: nothing else depends on it. The figure carries no totals (no 22, no 4t + 6).
- **Q13 and Q15 question figures = required although the LP text already carries the data.** LP Q13 names the colour order red, yellow, green, yellow, red; LP Q15 lists the first rows. The book, however, gives both as figures (coloured signal lights numbered 1 to 5; a 4-column grid with column numbers), and Q15(d) "observe the positions of multiples of 3" is built on the grid. Following "what the book question GIVES", both are required. If you want the strict "could the text alone do it" reading, Q13 question is the weakest and could drop to optional.
- **Q11 to Q14 solutions = optional (not added); sibling consistency.** These four have the same kind of answer (pattern to formula, text-only printed answers). A solution figure would be nicer (pieces 2, 3, 4 on the ropes; new sticks coloured; positions 1 to 12 coloured; Step 4 with 17 squares) but the LP text is complete. Q15 differs: its printed answer (d) is a picture.
- **Q2 solution = none.** A two-circle Venn picture (champak, marigold, both) would be nice, but the book has none and the text already has a p = 3, q = 4, r = 2 check. Not marked optional so as not to invent a figure the book does not have.
- **Q14 figures drawn without "Step" labels.** The book prints none (the steps are read from the answer: Step 4 = 17). The LP question text says "Step 1 has 5 squares", so the 5, 9, 13 squares identify the steps. Same for Q12 (no step labels in the book).
- **Q12: three figures of 1, 2 and 3 squares** (4, 7, 10 sticks), as in the book. The LP hint `q_figure` says "a row of four squares", which is wrong (see section 2).
- **Q13 colours** use literal hex values for red, yellow and green (the signal colours are the content, not a style token): red #F08060, yellow #FFF59D, green #8FCB8B. All other colours are style tokens.
- **Ropes (Q11)** are drawn as a flat stylised stroke with knots and a FOCUS dashed cut line, not as photographs. Picture 3 is idealised to three parallel layers joined at alternate ends (the book draws it loosely); the 3 crossings are checked on the enlarged page picture and recomputed from the coordinates (1, 2, 3 crossings; 2, 3, 4 pieces).
- **Q15 grid:** the book fades the vertical lines below row 4 (question) and uses dotted lines (answer picture); I use dotted GUIDE lines in both, so the solution keeps exactly the question layout (no gradients allowed). Cells are 2.0 wide and 1.2 tall (the book's are square) to fit the 16:9 card; labels, values and shading are as printed. Shaded cells use MARK_FILL with an ANSWER border; numbers stay INK (the book uses blue).
- **Aspect ratio 16:9 for every figure**, including the near-square grid and the wide rows: the pipeline draws 16:9 cards.
- **Duplicate prints.** The pdf holds every 4.6 figure twice: question part (pdf pages 22 to 25) and answer part (pages 35 to 40). Both base entries are claimed: the answer-part copies (P37-pattern-1, P38-pattern-1, P38-pattern-2, P39-pattern-1, P39-number_grid-1) map to the same question item as the page 22 to 25 copy, and say so in their description. Only P35-flow_diagram-1 and P40-number_grid-1 are printed-answer pictures (solution items).
- **P24-rope_fold-1 description corrected** ("CORRECTED:"): in picture 3 the top knot is on the upper-left side of the cut line, not on its right as the base text says. The crossing counts (1, 2, 3) were confirmed.

## 2. Things in the LP that look wrong or thin

- **Q5 question text is muddled:** "The other paths use the operations multiply by 3, subtract 8, subtract 4 and subtract 4, starting from w + 2 and w − 3, and the missing ovals are to be found." The real figure: inner boxes −5, +3, −8, −4; second boxes ×3, ×4, −4, ×3. Because the question diagram is required, the figure now carries everything; the sentence can stay but is confusing. `q_figure` (hint) is correct.
- **Q12 `q_figure` hint says "A row of four squares ... each square sharing a side with the next one".** The book shows three separate figures with 1, 2 and 3 squares. The question text does not give the numbers 4, 7, 10; they live only in the figure.
- **Q14 vertices answer 16n + 4** (book and LP): it counts 4 vertices per square, but squares on an arm touch at corners, so those corner points are shared. The book's answer is followed as is; "number of vertices" is ambiguous in the book. Not a diagram matter.
- **Answer concepts' `video_media_id` ids point to the next concept's number** (e.g. answer C128 carries `M3.S32.T32.C129.VID1`, Ans5 carries C137.VID1). Probably the id scheme of the video block, not a problem for diagrams, but worth a look if videos ever look misplaced.
- **LP answer forms vs book:** Q7(f) LP "21m − 20n + 5" vs book "5 + 21m − 20n"; Q9(b) LP "18x + 16y − 23" vs book "16y + 18x − 23"; Q9(d) LP "−3a − 3b − 32" vs book "−(3a + 3b + 32)"; Q9(c) LP "10h − 27g + 2" equals the book. All are equal expressions in a different order; I recomputed Q7, Q8, Q9 and Q4, Q6, Q12, Q13, Q14, Q15: all LP values are correct.
- Q1 and Q2 questions in the LP are text only and fine; Q3 snail has no figure in the book.

## 3. Book unclear

- Q14 (pages 24 and 39) and Q12 (pages 24 and 38): no step numbers printed under the figures.
- Q11 picture 3: the folded rope is drawn loosely and small; layer count read at high zoom is 3.
- Q13: the three signal colours carry the meaning on their own (no letters printed); positions 1 to 5 are numbered.
- Q15 (page 25 vs 39): the open end of the grid is drawn as fading lines in the question and dotted lines in the answer picture (page 40); no row numbers anywhere.
- The brief says the pdf has no printed-solutions section, but it does (pages 26 to 41); the LP solution text was followed throughout and agrees with the printed answers.
- Housekeeping: while looking for the chunk file layout I accidentally printed about 60 lines of `map/out_A.json` (meta and the first inventory entry). I did not use it for any decision.
