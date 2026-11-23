# Class 5 Ch 2 Fractions - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths5_ch2` v4 (taken from staging). Result: new V2 version v5 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (99 items from 58 units)
{"worked_example": {"optional": 16, "none": 1}, "question": {"required": 12, "none": 29}, "solution": {"required": 25, "optional": 5, "none": 11}}

Optional, NOT added: [('C3', 'worked_example'), ('C8', 'solution'), ('C9', 'worked_example'), ('C10', 'worked_example'), ('C16', 'worked_example'), ('C17', 'worked_example'), ('C18', 'worked_example'), ('C23', 'solution'), ('C36', 'worked_example'), ('C37', 'worked_example'), ('C49', 'worked_example'), ('C55', 'worked_example'), ('C61', 'worked_example'), ('C62', 'worked_example'), ('C63', 'worked_example'), ('C88', 'solution'), ('C91', 'worked_example'), ('C92', 'worked_example'), ('C93', 'worked_example'), ('C102', 'solution'), ('C104', 'solution')]

needs_lp_text_sync: [('C6', 'solution'), ('C13', 'solution'), ('C15', 'solution'), ('C31', 'solution'), ('C33', 'solution')]

## The 37 diagrams
| id | side | type |
|---|---|---|
| M1.S3.T3.C5.IMG1 | question | fraction_model |
| M1.S3.T3.C6.IMG1 | solution | fraction_model |
| M1.S5.T5.C12.IMG1 | question | fraction_model |
| M1.S5.T5.C13.IMG1 | solution | fraction_model |
| M1.S5.T5.C14.IMG1 | question | fraction_model |
| M1.S5.T5.C15.IMG1 | solution | fraction_model |
| M1.S7.T7.C20.IMG1 | question | fraction_model |
| M1.S7.T7.C21.IMG1 | solution | fraction_model |
| M1.S8.T8.C28.IMG1 | question | fraction_model |
| M1.S8.T8.C29.IMG1 | solution | fraction_model |
| M1.S8.T8.C30.IMG1 | question | fraction_model |
| M1.S8.T8.C31.IMG1 | solution | fraction_model |
| M1.S8.T8.C32.IMG1 | question | fraction_model |
| M1.S8.T8.C33.IMG1 | solution | fraction_model |
| M1.S8.T8.C35.IMG1 | solution | fraction_model |
| M1.S10.T10.C39.IMG1 | question | fraction_model |
| M1.S10.T10.C40.IMG1 | solution | fraction_model |
| M1.S10.T10.C41.IMG1 | question | fraction_model |
| M1.S10.T10.C42.IMG1 | solution | fraction_model |
| M2.S13.T13.C52.IMG1 | solution | fraction_model |
| M2.S16.T16.C58.IMG1 | solution | fraction_model |
| M2.S19.T19.C66.IMG1 | solution | other |
| M2.S19.T19.C68.IMG1 | solution | other |
| M2.S19.T19.C70.IMG1 | solution | other |
| M2.S19.T19.C72.IMG1 | solution | other |
| M2.S19.T19.C74.IMG1 | solution | other |
| M2.S20.T20.C76.IMG1 | solution | other |
| M2.S20.T20.C77.IMG1 | question | number_line |
| M2.S20.T20.C78.IMG1 | solution | number_line |
| M2.S20.T20.C81.IMG1 | question | number_line |
| M2.S20.T20.C82.IMG1 | solution | number_line |
| M2.S21.T21.C86.IMG1 | solution | other |
| M2.S22.T22.C89.IMG1 | question | number_line |
| M2.S22.T22.C90.IMG1 | solution | number_line |
| M3.S24.T24.C96.IMG1 | solution | fraction_model |
| M3.S24.T24.C98.IMG1 | solution | fraction_model |
| M3.S27.T27.C110.IMG1 | solution | other |

### Chunk A notes (from the decision agent)
# Chunk A notes (Class 5 Ch 2 Fractions, topics M1.S2.T2 to M1.S9.T9)

Result: 32 items = 15 required, 10 optional, 7 none. Validator: errors 0 (8 warnings, all "solution diagram has no inventory line of its own": the solution diagrams derive from their question diagram, whose book figure carries the inventory line; C35's four bars are not printed in the book).

Required diagrams (15): C5 Q, C6 S (chocolates); C12 Q, C13 S, C14 Q, C15 S (grids A, B, C); C20 Q, C21 S (strip of 6); C28 Q, C29 S (3x2 grid, Q2 A); C30 Q, C31 S (Q2 B); C32 Q, C33 S (Q2 C); C35 S (four fraction bars).

## 1. Judgement calls

1. **Rule I used.** A diagram is `required` when the item depends on a figure its words do not contain (a book figure carrying the data, or a figure the learner must shade, mark or identify), or when the answer is itself a drawing or arrangement (B2). Items whose words carry all the data and whose answer is a number, sentence or equation are not drawn.
2. **C14 question = blank grids, not the LP hint.** The LP `q_figure` hint draws grids A, B, C already shaded (from Q1). The book prints them blank and the brief says one diagram per item with an identical spec for the same book picture, so C14's question diagram is identical to C12's (render_note "same as M1.S5.T5.C12.IMG1"). The C15 solution adds the equal parts (6, 8 and 4 squares) and the 1/3 outlines on top of blank grids; nothing in the C15 steps needs the Q1 shading.
3. **C15 marked parts.** The LP gives no positions. I outline the bottom two rows (16 squares) of grids B and C and nothing on A. The LP hint said "first 2 rows"; both are correct, the bottom rows sit next to the "1/3" labels. Grid C parts are drawn as 2x2 blocks (4 squares each, 12 parts), so the outlined region is 4 whole parts.
4. **Sample shading positions (needs_lp_text_sync = true on C6, C13, C15, C31, C33).** The LP states counts only. Chosen: C6 top row of each bar (2 and 3 blocks); C13 grid A column 1 (red), grid B row 1 (blue), grid C top-left 2x2 block (yellow); C31 (a) column 1, (b) columns 1-2; C33 (a) columns 1-2, (b) row 1, (c) column 1, (d) first 2 squares of row 1.
5. **Colours red / blue / yellow (C13).** The LP words say red, blue, yellow. The style table has no red or yellow, so the spec gives hex values (red #E03C31, yellow #F4C20D) and uses SET_A for blue. Other shading is MARK_FILL.
6. **Letters.** (a), (b), (c), (d) are drawn in the C30/C31 and C32/C33 pictures and A, B, C in the grid pictures, because both the LP question and the LP answer text refer to the figures by those letters (user decision 3). C28/C29 is one grid: no letters.
7. **C35 solution: bars, four tasks in one picture.** The four tasks (1/6 + 1/12; 1/12 + 1/4 + 1/2; five equal pieces; seven pieces) become four bars of 1440 px, one per task, in task order, each labelled "= 1" (the LP answer ends each sum with 1). I used bars instead of the kit's circles because 1/12 labels do not fit inside a circle wedge at the minimum text size. The LP did not split the tasks into separate items, so one picture is used (the pair gets one solution diagram). The picture has no question diagram: the question gives no figure.
8. **Figure inventory choices.** P02-fraction_model-2 (Gurpreet's circle 1/2 + 1/4 + 1/4) and P04-fraction_model-1 (Sameer's four squares) are teaching figures of unit blocks that I did not draw (worked examples C17, C36); mapped to `concept_image:M1.S6.T6.C17.IMG1` and `concept_image:M1.S9.T9.C36.IMG1`, which carry the same idea but are not the same drawing (said in the descriptions). The grids A, B, C are used by two questions (C12 and C14), so C14 has three `NEW-P01-fraction_grid-<n>-C14q` lines.
9. **C7 question none** although the book prints the chocolates beside it: that picture belongs to C5; C7 is a general question ("When can we say...") with no figure of its own. **C24 question none** although the circle sits above it on the book page: the question is only the equation chain.
10. **No separate diagram for the blank writing box** on p.4 (Let Us Do Q3, "Write or draw your findings"): it is writing space, not a figure, so it is not in the inventory.

## 2. Borderline

- **All 8 worked examples are `optional` (not added):** C3 (roti), C9 (3x7 grid), C10 (6x4 grid, 1/24), C16 (circle in 1/4 and 1/8), C17 (circle 1/2 + 1/4 + 1/8 + 1/8, 1/16), C18 (strip of 20), C36 (bar 4/5 to 8/10), C37 (bars 3/8, 6/16, 9/24). Each is told fully in words (no figure referenced, answer a number or sentence), so by the tie-breaker the picture is not needed, but every one would clearly benefit from a bar, grid or circle; the reason line names the figure. This was NOT decided because a teaching image exists: all eight concepts do keep a teaching image of the same figure (kept_image_ids), and that played no part. If you want them drawn, flip these eight to `required` (`add_new_image`, question_tex / after_question_text) and ask for the specs.
- **C8 solution `optional`:** the answer is a rule; two equal bars of 6 blocks (3 shaded = 1/2, 2 shaded = 1/3) would help but every number is in the words.
- **C23 solution `optional`:** answer is a count (5 pieces); a circle cut into 5 pieces marked 1/5 would help but is not needed. (C35 is `required` because its answer is an arrangement of pieces; C23's is a number.)
- **C30 and C32 questions `required`:** the learner shades on blank 4x2 and 4x3 grids ("shade and check"); the grid size appears only in the picture. Sibling of Q2 A (C28), which is clearly required. Could be argued as optional because the fractions alone give the answer.
- **C21 and C29 solutions `required`:** they add only labels and outlines (groups, 1/6, 1/3) to the given figure; kept required as "act on the given figure" (Step E, Q required and S required).
- **C35 solution `required`:** B2 "answer is an arrangement" read for "Make a whole using ... pieces"; the LP answer writes the pieces as sums only.
- **C25 and C27 solutions `none`:** the answers are equation chains of equivalent fractions (LaTeX), no picture printed or asked for.

## 3. LP text issues

(Nothing in the LP was edited; the suggested sentences would make text and picture agree.)

- **M1.S3.T3.C6, C8, M1.S5.T5.C13, C15, M1.S8.T8.C27, C33, C35:** the `text` fields still carry the old card markers "[Image: ...: solution]" in the middle of the steps and "[Image: ...: solution (continued)]" at the end (the other solution concepts have none). The new solution token must come before step 1; the old markers should be removed by the builder.
- **M1.S3.T3.C6:** the steps do not say which blocks are the group. Suggested sentence after step 3: "In the picture, the top row of each bar is one group: 2 blocks of the small bar and 3 blocks of the big bar."
- **M1.S5.T5.C13:** answer says "Your squares may be in different places" but gives no sample. Suggested: "In the picture, Grid A has the first column shaded red, Grid B the top row blue and Grid C the top-left 2 by 2 block yellow."
- **M1.S5.T5.C14:** the question does not say which grids. Suggested: "Look at Grids A, B and C. Do you see 1/3 in any of the grids? Mark it."
- **M1.S5.T5.C15:** step 3 and 4 say "Mark 2 parts in Grid B" / "Mark 4 parts in Grid C" without saying which. Suggested: "In the picture, the bottom 2 rows of Grid B and of Grid C are marked."
- **M1.S8.T8.C31:** counts only. Suggested: "(a): shade the first column of the grid. (b): shade the first 2 columns."
- **M1.S8.T8.C33:** counts only. Suggested: "(a): the first 2 columns. (b): the first row. (c): the first column. (d): the first 2 squares of the first row."
- **M1.S8.T8.C35:** the answer sentence lists four sums; suggested: "In the picture, the four bars are these four wholes in order."
- **Possible contradiction, C27 vs C17:** C27 says 4/16 "is not on the kit", while the worked example C17 and its teaching image C17.IMG1 use pieces of 1/16 ("a piece of 1/8 can be covered by two pieces of 1/16"). The fraction kit is at the end of the textbook and is not in the 15 pdf pages, so I could not check which pieces exist. One of the two statements is probably wrong.
- **M1.S8.T8.C26 / C27:** the book Q1 is a group kit activity; C27 lists names "on the kit" (1/6, 1/9, 1/12 for 1/3; 1/8, 1/12 for 1/4; 1/10 for 1/5; 1/12 for 1/6): same unverifiable-kit caveat.
- **LP hints versus book:** the `q_figure` hint of C14 shows shaded grids (the book prints them blank); the `s_figure` hint of C15 says "first 2 rows" (I used the bottom 2); the `s_figure` hint of C35 shows one circle for one task (I show all four tasks). Hints were not followed where they disagree with the book or the answer text.

## 4. Book unclear or checked

- Base inventory figures of this chunk were checked against the page pictures (pp.1 to 4): grid sizes (8x6, 3x2, 4x2, 4x3), the chocolate bars (2x2 and 3x3 blocks of equal size), the strip (6 cells, 2 shaded), Gurpreet's circle and Sameer's squares all match the base descriptions. All `unclear` lists of these figures were empty. No `CORRECTED:` needed.
- No book print slips found in the figures of this chunk (no wrong digit, count or sign), so no "book value corrected" case.
- The book's outline colours of the grids (green, blue, pink, orange, purple, red) and the chocolate/paratha textures are decoration; INK outlines and neutral fills are used.
- Book p.1: the captions "Identify 1/2 / 1/3 of the chocolate" ask the learner to mark the part on the bars but the book does not say which blocks; the sample group (top row) is my choice.
- The book gives no printed answers (this pdf has no solutions section), so no printed-answer pictures exist for this chunk; every solution diagram follows the LP solution text.

### Chunk B notes (from the decision agent)
# Chunk B notes (Class 5 Ch 2 Fractions, topics M1.S10.T10 to M2.S18.T18)

Result: 23 items (9 pairs, 5 worked examples). Required 6, optional 5, none 12. Validator errors 0 (2 warnings, explained in 1.7).

Required diagrams (all 16:9, `fraction_model`):

| media_id | item | what it draws |
|---|---|---|
| M1.S10.T10.C39.IMG1 | question | the three printed squares (middle third shaded) with an empty box under each |
| M1.S10.T10.C40.IMG1 | solution | same squares cut into 5, 6, 7 rows, boxes filled 5/15, 6/18, 7/21 (derived_from C39.IMG1) |
| M1.S10.T10.C41.IMG1 | question | four rectangles, rows 2 and 4 of 5 shaded, labels 2/5 and 4/10, two empty fraction slots |
| M1.S10.T10.C42.IMG1 | solution | rectangles 3 and 4 cut into 3 and 4 columns, slots filled 6/15 and 8/20 (derived_from C41.IMG1) |
| M2.S13.T13.C52.IMG1 | solution | chikki slab in 3 strips, Sevi 1/3 and Shami 2/3 ringed (no question diagram, derived_from null) |
| M2.S16.T16.C58.IMG1 | solution | paratha 4/6 and paratha 4/5, loose 1/6 and 1/5 piece, comparison (no question diagram, derived_from null) |

## 1. Judgement calls

1.1 **Worked examples C49, C55, C61, C62, C63 are all `optional` (no image added).** They are LP-written teaching examples (none is a book item), every number is in the text, and no v3 Step B trigger fires. I applied the tie-breaker as written (a careful student can follow each from the text) and did not use the existing teaching images as a reason. Each reason names the figure that would help (C49 two bars of 10 pieces with 3 and 7 shaded; C55 two same-size parathas cut into 4 and 10 pieces; C61 number line 0 to 5 in halves with 9 jumps; C62 11 quarters grouped by 4 and 8 slices grouped by 3; C63 bars of fifths and tenths against the whole). If the user wants them drawn, flipping them to `required` only needs a spec each; C55 and C61 would be the strongest candidates.

1.2 **Example pairs C51/C52 (chikki) and C57/C58 (paratha): question none, solution required.** The LP questions do not point at a figure and give all numbers in words, so a question figure would be a blank slab or a pair of parathas that already shows the comparison (rule: no question figure when the question gives none). The book prints the picture next to the worked answer ("2 pieces of 1/3 are more than 1 piece of 1/3"; "1/6 piece is smaller than 1/5 piece"), so the solution side is required (B2, printed answer rests on a picture). Both solutions draw the whole figure themselves (`derived_from` null).

1.3 **C39/C41 question figures include the empty answer boxes/slots.** The book prints them ("Write them in the boxes below the images"; empty fraction slots under rectangles 3 and 4) and the solution figure fills them in ANSWER green, which keeps the same layout between question and solution. They contain no digit, so nothing leaks.

1.4 **C39 question figure shows only the three given wholes, not Sameer's row of four squares (1/3, 2/6, 3/9, 4/12) from pdf page 4.** The old hint `q_figure` mentioned that row too, but the book question says "the wholes given below", the first four fractions are already in the equation line, and the four squares are the teaching figure of M1.S9.T9 (chunk A: C36 'mk.sameer'). So P04-fraction_model-1 is NOT claimed by chunk B. If the user wants Sameer's row above the three wholes (and in the solution), the figure becomes a two-row picture; say so.

1.5 **Solution of C40 draws only the three pictured wholes (5/15, 6/18, 7/21).** The LP sample answer also gives 8/24 and 12/36, but the book has no picture for those two boxes, so they are not drawn. Likewise C42 does not draw 20/50 and 40/100.

1.6 **Colours.** The book's yellow/lilac shading is replaced by the house tokens: MARK_FILL for shaded cells, ANSWER green for everything the solution adds (new cut lines, new numerals), SET_A / SET_B for the two groups being compared (Sevi / Shami strips; the 4/6 and 4/5 parathas and the loose 1/6 and 1/5 pieces), FOCUS for the ring around Shami's two strips.

1.7 **Warnings (2).** C40 and C42 solutions are required but have no book figure mapped to them: the pdf has no printed-solutions section and the figures are the question figure completed (the base figures P05-1 / P05-2 are mapped to the question items).

1.8 **Figure ownership.** Claimed (9): P05-fraction_model-1 -> item C39 (question); P05-fraction_model-2 -> item C41 (question); P06-fraction_model-1 -> item C52 (solution); P07-fraction_model-1 and -2 -> item C58 (solution, both paratha pictures are drawn in one diagram); P08-number_line-3, P08-number_line-4 -> concept_image C61.IMG1; P10-number_line-3, P10-number_line-4 -> concept_image C62.IMG1. The four number lines are claimed because the teaching text of my concepts C61 (`gt1.nl_halves`) and C62 (`gt1.nl_fourths`) is the sentence printed with them. They are also the book's number lines for Example 3 (Maa, 5 halves) and Example 5 (Dadaji, 9 fourths), which are chunk C items: chunk C may map the same base figures to its own solution items. Needs a merge decision if both chunks keep them (suggest: chunk C draws them for its solutions, chunk B keeps them as teaching figures, give the second use a NEW- id).

1.9 The six required diagrams use `fraction_model` with a full `content` object (pixel coordinates on a 1920 x 1080 canvas). Squares/rectangles are drawn flat; the book's photographic chikki and paratha textures are not reproduced.

## 2. LP text issues

(Not edited; listed only.)

- **M1.S10.T10.C39** (Q1, equivalents of 1/3): the question text says "Sameer has shaded one-third of the figures. He draws horizontal lines to divide the shapes..." but the figures it talks about (page 4: four squares showing 1/3, 2/6, 3/9, 4/12) are not in the question picture, and the figure now added shows the three blank wholes. Suggested sentence: "Sameer shaded one-third of a square. When he cuts it into 2, 3 and 4 equal rows he gets 2/6, 3/9 and 4/12. Divide each of the three wholes below into more equal rows with horizontal lines and write the equivalent fraction in the box under it."
- **M1.S10.T10.C41** (Q2, equivalents of 2/5): the text says "write your fractions below each image", but only the third and fourth rectangles have an empty slot; the first two are labelled 2/5 and 4/10. Suggested sentence: "Write the fraction of the shaded part in the empty box under the third and the fourth picture, then complete the line below."
- **M2.S13.T13.C51/C52** (Example 1, chikki): neither the question nor the solution says which piece of the chikki is Sevi's. The figure assumes the top strip is Sevi's and the other two strips are Shami's. Suggested sentence for the solution, step 1: "The chikki is cut into 3 equal pieces. Sevi ate the top piece, 1 piece of 1/3."
- **M2.S16.T16.C57** (Example 2, paratha): "One child says: I ate 4/6 ... The other says: I ate 4/5 ... Between Sevi and Shami" never says which child is Sevi. In the book the girl (Sevi) says 4/6 and the boy (Shami) says 4/5. Suggested sentence: "Sevi says: I ate 4/6 paratha yesterday evening. Shami says: I ate 4/5 paratha yesterday evening. Can you tell who ate more? Use your fraction kit to find the answer."
- **M2.S18.T18.C61** (worked example, 9 halves): step 5 says "Check on the number line: 9 jumps of 1/2 from 0 land on 9/2", but the worked-example block shows no number line (only the teaching image of the concept does). Suggested sentence: add "(look at the number line in the picture above)" to that step, or draw the number line (see 1.1).

## 3. Borderline

- Worked examples C49, C55, C61, C62, C63: `optional` (see 1.1). These are the calls most likely to be reversed by the user.
- C52 and C58 solutions: `required` although the LP text carries every number (kept as required on purpose, per the 23 Nov decision 4, because the book's printed answer is a picture).
- C51 and C57 questions: `none` although the book prints a picture beside the question (the picture goes with the printed answer, the LP question text does not refer to it).
- C54 and C60 solutions: `none`. The six parts compare plain fractions; the book prints no figure, and six pictures would only restate the numbers. (Sibling check: the other "compare with < >" items of the chunk are all `none`.)
- C46 solution (ticks on (b) and (c)): `none`, a selection written in the answer line, not a drawing.
- C39 question: boxes drawn empty (1.3); Sameer's row not drawn (1.4).

## 4. Book unclear or contradicting

- Which strip of the chikki is Sevi's: the book shows an unmarked slab; the diagram chooses the top strip.
- Page 7: the book prints the fifths paratha on the left and the sixths paratha on the right, but the question lists 4/6 (girl, left) before 4/5 (boy, right). The diagram follows the question order (sixths left, fifths right); the book's dashed rims and the 1/5, 1/6 sector labels are left out.
- Page 7: the book labels only the eaten sectors (4 of 5 and 4 of 6); the other sector(s) are unlabelled with a dashed rim. The diagram shades the 4 eaten sectors and leaves the others white.
- No book print slips found in my figures. (The base inventory descriptions of P05, P06, P07, P08 and P10 were checked against the page pictures and are correct.)
- Page 5 equation line for Q1: three standalone blanks, then a box over 24 and a box over 36 (same as the LP); the book never says what the boxes over 24 and 36 hold, the LP sample answer gives 8/24 and 12/36.

### Chunk C notes (from the decision agent)
# Notes for chunk C (Class 5 Ch 2 "Fractions", live plan cbse_eng_maths5_ch2_v4)

Units: M2.S19.T19 (Examples 3 to 7), M2.S20.T20 (fractions greater than 1, five pairs), M2.S21.T21 (Let Us Do Q1, Q2), M2.S22.T22 (Try This, ants), M3.S23.T23 (three worked examples). 16 units, 29 items.

Result: required 13 (question 3, solution 10), optional 4 (one solution, three worked examples), none 12. Validator: errors 0, 2 warnings (C76 and C86 solutions are required but the book prints no picture for them; see below).

Figures claimed: 21 base figures (all of pages 8 to 12 and the ants of page 15, plus the two teaching circles P13-fraction_model-3 / -4) and 3 `NEW-` entries. The `NEW-` entries are the same book picture used a second time (P09-number_line-3, P11-number_line-1, P15-number_line-2 each draw a question card and a solution card).

## 1. Judgement calls

- **Examples 3 to 7 (C65 to C74), question side `none`, solution side `required`.** The question text gives all the data in words. The book's pictures (pieces, grouped sum, number line, pizza slices) are the worked solution, not a given figure, so they are drawn on the solution card only. Several base figures map to one solution item (for example P08-fraction_model-1, P08-grouped_sum-2, P08-number_line-3 and P08-number_line-4 all map to C66 solution): the pieces row carries the grouped sum (pairs joined, each marked 1 paratha) and the number line carries the jumps.
- **Dadiji's 7 halves (C76 solution) is `required` though the book prints no picture.** Sibling consistency with Example 3 (same kind of answer, grouped half pieces). The LP's own s_figure describes the picture. Pieces only, no number line, because the LP steps do not use a number line there.
- **Two pizzas on the Example 6 solution (C72).** The LP s_figure only describes Raman's share, but the question asks "each of them" and the answer says both have 1 whole pizza, so Raman's and Radhika's whole pizzas are drawn (each 3 slices of 1/3), with one number line 0, 1/3, 2/3, 3/3 = 1.
- **Example 7 solution (C74) number line stops just after 4/3.** The LP hint says "from 0 to 2". The book's line has ticks only to 4/3 and runs far to the right. To avoid unlabelled ticks the card draws ticks 0 to 4/3 only (4 jumps). Easy to change if the user wants 0 to 2.
- **Number-line cards C77/C78 and C81/C82 are not the book's proportions.** C77 keeps the book's 10 ticks per line with 0 under tick 1 and 1 under tick 3 (one step = 1/2). C81: the book's line is about 4.7 units long with 1 at one fifth of the way; the card uses unit 500 px and a line 3.3 units long, so that the 13 quarter labels of the solution fit; the largest amount is 3. Question and solution use identical positions (derived_from).
- **Names only as line labels.** The book's heading "Quantity of Raman's paratha" is reduced to the label "Raman" (heading rule), same for the others.
- **C86 (Let Us Do Q1 solution) is `required`, question `none`.** The question asks the learner to draw parathas and number lines in the notebook; nothing is given, so no question figure (companion note). The LP answer is exactly that drawing, hence `ANSWER_IS_FIGURE`. One card holds the three parts (a), (b), (c) with both fractions each (6 fractions, 9 parathas, 3 number lines). It is dense; the task brief allows one solution diagram per pair, so it is one card. If it is unreadable at 1920 px, split into two cards later.
- **Letters (a), (b), (c) are drawn on C86** because the LP answer text refers to the parts by letter (user decision 3).
- **Ants (C89/C90).** The picture is the data (16 ants of 1/4 cm each end to end), so the question side is `required`. Ants are drawn as one flat grey glyph, 100 px wide, not as clip-art. The solution adds a tick at every 1/4 cm, labels at 1, 2, 3, 4 cm and a bracket over all 16 ants.
- **C80 and C84 (the two "how many parathas were made on this day" solutions) are `none`.** The LP s_figure is a plain table of names and piece counts with a total: `LATEX_TABLE`/`LATEX_ARITHMETIC`, with the table to write in `text_alternative`.
- **Question diagrams are not drawn for the two "day" questions (C79, C83):** the book gives a blank writing box, no figure.
- **P13-fraction_model-3 and -4** (the 4/8 = 1/2 and 3/6 = 1/2 circles, "Comparing Fractions with Reference to 1/2") are claimed here because the concept C92 of my topic carries the ref `rh.pictures`; mapped to `concept_image:M3.S23.T23.C92.IMG1` (accounting only). The other pictures of pages 13 and 14 (P13-fraction_model-1 / -2, P14-fraction_model-3 / -4, the number boxes, the table) belong to the T24/T25 examples and questions of chunk D; I did not claim them. If chunk D also claims P13-fraction_model-3 / -4, the merge should keep one meaning.

## Borderline

- **C88 (Let Us Do Q2, solution) `optional`.** The question's box of 14 loose fractions is `NUMBER_LIST_IN_BOXES` (question `none`, text already lists them). On the solution side the only picture is the same box with 9/4, 9/4, 5/4, 7/3, 13/11, 12/5, 12/8 circled; the LP answer names the seven fractions, so under the v3 rule ("arrows/circles only optional when the text gives the answer") it is not drawn. If the user prefers the circled box, flip to `required` with the 14 fractions at the page positions (box 739 x 204 px, positions read from page 12) and the seven circled in FOCUS. Chunk D's "circle the fractions" questions (Let Us Do Q1/Q2 on page 14) are the same type: they should get the same decision.
- **C91, C92, C93 (worked examples of T23) `optional`.** Questions and steps carry every number and compare top and bottom numbers in words; the teaching images (number line 0, 1, 2 with 3/5 and 10/9; circles with the half line; number line 0, 1/2, 1 with 5/12 and 7/10) exist and are not linked. They are not dropped because the teaching image exists, but because no v3 trigger applies; a picture would show the answer and would not be given data. If the user wants a diagram for each worked example, the figure to draw is named in each item's `reason`.
- **C65 to C74 question side `none` although the book prints a picture beside the question text.** The picture in the book is the worked answer, not a given.
- **C86 as one dense card** (see above).

## 2. LP text issues

- **M2.S19.T19.C73 (Example 7: Q).** The question text "Raman could eat only 2 slices of pizza. So, he gave 1 to Radhika. How much pizza does Radhika have now?" does not say that Radhika already has 3 slices (1 whole pizza) from Example 6, so it cannot be solved from the question alone (the LP solution's first steps supply this). Suggested sentence: "In the family pizza, Radhika ended up with 3 slices of 1/3, that is 1 whole pizza. Raman could eat only 2 of his 3 slices, so he gave 1 slice to Radhika. How much pizza does Radhika have now?"
- **M2.S19.T19.C73 `q_figure` hint and M2.S19.T19.C71 `q_figure` hint.** C73's hint ("three slices as one round pizza and one more slice") describes the answer picture, and C71's hint ("two round pizzas each cut into 3 slices") is not in the book. No question figure is drawn for either; the hints can be ignored or removed.
- **M2.S22.T22.C89 (Try This: Q).** The text says "Use the number line given below" but carries no figure; the figure comes from the diagram C89.IMG1. The question says 16 ants and the book draws 17 (see section 3). The LP is right (16 x 1/4 = 4 cm).
- **M2.S20.T20.C77 and C81.** "Use the number line" / "Use a number line" also point at figures that the diagrams C77.IMG1 / C81.IMG1 supply.
- **M2.S20.T20.C75, C77, C79 (names).** The book itself mixes "Dadiji" and "Dadaji" (page 9: "Dadiji had 7 pieces", then "Dadaji ate 7 pieces"); the LP follows the book. The diagrams use the LP's names (Dadaji on the three lines, Dadiji on the five lines).
- **M3.S23.T23.C91 and C93.** The worked examples have no `ncert_refs`: they are LP-made examples, not from the book (C92 has `rh.pictures`). Nothing wrong, just not traceable to a book page.
- No numeric error found in the LP solutions of this chunk: C66 (5/2 = 2 1/2), C68 (6/2 = 3), C70 (9/4 = 2 1/4), C72 (3 slices each, 1 + 1 = 2 pizzas), C74 (4/3 = 1 1/3), C76 (7/2 = 3 1/2), C78 (3, 3 1/2, 2 1/2), C80 (36/2 = 18, 5 + 6 + 7 + 6 + 7 + 5 = 36), C82 (7/4, 6/4, 8/4, 10/4, 12/4), C84 (9 + 7 + 6 + 8 + 10 + 12 = 52, 52/4 = 13), C86, C88 (7 + 7 = 14), C90 (16/4 = 4), C91 to C93 all recomputed.

## 3. Places where the book is unclear

- **Ants (page 15):** the text says 16 ants, the drawing has 17 (counted twice on the page picture, 17 heads). Per user decision 1 the diagrams draw 16 (the mathematics and the LP say 16); the base inventory keeps what the book prints (17), noted in the figure entry and in the diagram's `render_note`.
- **Example 6 (page 27) shows only Raman's share** ("Raman's slice", "Raman's total share") although the question asks about each member; the card draws both whole pizzas.
- **Example 7 (page 28):** the book's "Radhika's slice" (a single slice) and "Radhika's total share" (whole pizza plus a loose slice) put the earlier 3 slices and the extra one in the same picture without saying so in words; the question text relies on the previous page (see LP text issues).
- **Book number lines end at different places:** Example 3 line ends at 5/2 (page 8), Example 4 at 6/2 with the label printed without "= 3" (page 9), Example 7 at 4/3 (page 12); the long lines on pages 9 and 11 are blank on purpose. The cards follow the LP's labels (6/2 = 3).
- **Parathas are photographs of rounded squares in the book;** the plan's own pictures use round parathas, so the cards draw round parathas and round pizzas as flat shapes (no photographs).

### Chunk D notes (from the decision agent)
# Notes, chunk D (Class 5 Ch 2 Fractions): M3.S24.T24, M3.S25.T25, M3.S26.T26, M3.S27.T27

Result: 15 items, required 3 / optional 2 / none 10. Validator `--chunk D`: errors 0, 1 warning (C110 is required but the book prints no figure for it; expected).

| Item | Decision | Why in one line |
|---|---|---|
| C95 Ex 8 question | none (TEXT_SUFFICIENT) | amounts given as numbers; the book's paratha pictures sit beside the answer bubble |
| C96 Ex 8 solution | **required** `M3.S24.T24.C96.IMG1` | printed answer is the paratha picture: 7/8 (7 of 8 pieces) and 8/6 (one whole + 2 pieces) |
| C97 Ex 9 question | none (TEXT_SUFFICIENT) | same as Ex 8 |
| C98 Ex 9 solution | **required** `M3.S24.T24.C98.IMG1` | printed answer is the paratha picture: 5/8 past the half line, 3/6 exactly half |
| C99 / C100 Let us do (reference to 1) | none / none | no figure in the book; six pairs and six signs in text |
| C101 equal-to-1/2 box | none (NUMBER_LIST_IN_BOXES) | scattered list of fractions, all in the question text |
| C102 solution | optional (not added) | circled box would help; LP answer lists all six fractions |
| C103 less-than-half box | none (NUMBER_LIST_IN_BOXES) | same |
| C104 solution | optional (not added) | same; five fractions listed |
| C105 / C106 table of pairs | none / none (LATEX_TABLE) | plain 2 x 4 table; the signed table is a LaTeX array |
| C107 worked example (relations) | none (TEXT_SUFFICIENT) | plain three-link chain, no figure in the book |
| C109 relations question | none (TEXT_SUFFICIENT) | no figure printed or given |
| C110 relations solution | **required** `M3.S27.T27.C110.IMG1` | family tree: the only brother of father's sister is the father |

## 1. Judgement calls

1. **Example 8 and Example 9 (C95/C96, C97/C98): question none, solution required.** The book prints the paratha pictures right next to the answer bubble ("7/8 is less than 1 and 8/6 is more than 1", "3/6 is half. But 5/8 is more than 1/2"). The speech bubbles (the question) give the amounts as numbers, so the pictures are the printed answer, not a given figure. Solution = the book picture (B2: printed answer is a picture); question has no given figure so none (companion note: no invented question figure). The LP hint `s_figure` for Ex 8 (a number line with a dot each side of 1) was not followed: the LP steps speak of pieces and parathas ("7 pieces of 1/8", "8 pieces of 1/6 make 1 paratha", "1 whole paratha and 2 more pieces"), which is the book picture; the number line already exists as the teaching image M3.S23.T23.C91.IMG1 (never linked).
   - Added to the solution figure: the tags `less than 1` / `more than 1` (Ex 8) and `more than 1/2` / `exactly half` (Ex 9) in ANSWER green, each 3 words or fewer and taken from the LP steps; plus the vertical FOCUS half line through both circles in Ex 9 (LP `s_figure`: "a line across each one at half"). Labels `1/8` and `1/6` are drawn upright, the book rotates them.
   - One diagram draws both book pictures of each example (P13-fraction_model-1 and -2 to C96; P14-fraction_model-3 and -4 to C98).
2. **Boxes of loose fractions to circle (C101/C102, C103/C104).** The book question is "circle the fractions...", a selection from a box with no order or position meaning: Step C `NUMBER_LIST_IN_BOXES`. I read the code's last sentence by analogy: the marks (circles) only become a diagram on the solution side and then only `optional` because the LP answer lists every chosen fraction. So question none, solution optional (not added). See Borderline.
3. **Table of pairs (C105/C106).** Plain table, no colour, no headings: `LATEX_TABLE` on both sides. The solution's "same table with a sign in every pair" is a LaTeX array; the `text_alternative` of C106 gives the filled array (all eight signs checked: 2/9 < 4/7, 11/14 > 7/20, 5/7 > 3/9, 6/7 > 4/10, 9/17 > 3/15, 7/12 > 3/11, 1/3 < 5/9, 3/9 < 4/7).
4. **Relations (C107, C109, C110).** The puzzle "only brother of your father's sister" has a trick (the only brother is the father himself). A family tree changes how correctly the learner follows it (tie-breaker, second clause), so the solution is `required`: tree = Father's sister, Your father (joined by a sibling bracket and a FOCUS arrow "her only brother"), and under him two children "You" and "Brother or sister" (ANSWER). The box "You" is my addition so that "brother or sister of yours" can be read; the LP hint `s_figure` only had the father, his sister and his child. The question has no given figure (book page 15 prints only the sentence), so no question diagram. The worked example C107 (mother's only sister's daughter) is a plain three-link chain with no trick, no figure in the book: none. This is NOT because the concept already has a teaching image (C107.IMG1 stays untouched and is never linked): the rule-based need is just lower than for C110.
5. **Figures not claimed here.** `P13-fraction_model-3` and `-4` (circles 4/8 = 1/2 and 3/6 = 1/2) sit in the book section "Comparing Fractions with Reference to 1/2" but are the teaching pictures of unit 49 (`rh.pictures`, M3.S23.T23, chunk C); `P12-number_box-4` is Let Us Do Q2 on p.12 (M2.S21.T21, chunk C) and `P15-number_line-2` is Try This (M2.S22.T22, chunk C). If chunk C leaves P13-fraction_model-3/-4 unclaimed, the merge must assign them (they are teaching figures; none of my items needs them).
6. **Base inventory check.** I compared every claimed figure with the page pictures (zoomed crops of p.13 and p.14): all seven descriptions are correct (7 labelled eighths with the lower-left sector dashed; 6 + 2 sixths; 5 eighths clockwise from the top radius to the lower-left diagonal; 3 right sixths = exact half; the box and table contents). No `CORRECTED:` entries.

## 2. LP text issues

(No LP text was edited and no decision changed because of these.)

- **M3.S24.T24.C95 and C97 (question text):** the question names "Sevi and Shami" but then says "One child says ... The other says ...", so the learner cannot tell who ate which amount. Suggested: "Sevi says: I ate 7/8 paratha yesterday evening. Shami says: I ate 8/6 paratha yesterday evening." (and for C97: "Sevi says: I ate 5/8 paratha ... Shami says: I ate 3/6 paratha ..."; in the book the girl on the left holds the first amount and the boy on the right the second, but the pictures do not name them).
- **M3.S24.T24.C96 and C98 (solution text):** no sentence refers to the picture that now opens the solution. Suggested first line for C96: "Look at the picture: 7 of the 8 pieces of one paratha, and one whole paratha cut into 6 plus 2 more pieces of the other." For C98: "Look at the picture: the half line cuts the paratha cut into 6 exactly in half; the paratha cut into 8 has 4 pieces on one side of the line and 1 more piece past it."
- **M3.S27.T27.C110 (solution text):** the tree includes a box "You"; step 4 could say "a child of your father is another child in your family: your brother or sister" so that the box makes sense (the answer text "brother or sister" is unchanged).
- **M3.S25.T25 (question names and book numbers):** the concept names run Q2, Q3, Q4 (counting from the "reference to 1" set) while `book_number` says "Let Us Do (reference to 1/2), Q1 / Q2 / Q3" (the book numbers them 1, 2, 3 within that set). Not wrong, but the two numberings differ.
- **Order:** in the book the two box questions (circle equal to 1/2, circle less than half) come BEFORE Example 9 ("Now let us compare fractions using 1/2"); the LP puts Example 9 (topic T24) before them (topic T25). Teaching order is fine in the LP; just not the book's order.

## 3. Borderline

- **C102 and C104 (circled boxes): optional vs required.** Argument for required: ACTION_ON_FIGURE / HIGHLIGHT_MEANING (the answer is the circles on a given box) and the LP's own `s_figure` wanted "the same box with the fractions circled". Argument for none/optional (chosen): the box is a NUMBER_LIST_IN_BOXES and the Step C text says circles only become optional on the solution side when the text already gives the answer; the LP answer lists all chosen fractions, so by the tie-breaker the text alone is exact. If the user prefers the picture, the spec would be: a rounded box with the 10 (or 12) fractions at the book's positions, the six (or five) answers circled in FOCUS. Chunk C's "circle the fractions greater than one" box (p.12) should get the same decision for consistency.
- **C95 and C97 (question side).** The paratha pictures could be read as a given figure of the question; I read them as the printed answer (they sit with the answer bubble) because the amounts are given as numbers. If read the other way, both questions become required and the two solution diagrams would derive from them.
- **C107 worked example (none) against C110 solution (required).** See judgement call 4.
- **C99/C100 (reference to 1).** A number line placing the twelve fractions around 1 would be optional only; text is exact, so none.

## 4. Where the book is unclear

- Fun with Relations (p.15): the book prints no answer. The LP says "brother or sister"; strictly the child of your father may also be you yourself if you are an only child, but "brother or sister" is the usual answer and was kept.
- Book Example 8 and Example 9 bubbles name no children; the names Sevi and Shami appear only in the surrounding text of the section.
- No print slips were found in the figures or printed answers of this chunk, so no book value was corrected.
