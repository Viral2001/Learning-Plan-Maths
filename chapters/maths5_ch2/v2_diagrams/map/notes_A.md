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
