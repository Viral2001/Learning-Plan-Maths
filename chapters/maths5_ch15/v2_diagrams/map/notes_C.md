# Notes, chunk C (Class 5 Ch 15, Data Through Pictures)

Units: M2.S14.T14 (Food Wastage questions Q1 to Q6, 6 pairs), M3.S15.T15 (worked example C82, 1 item) and M3.S16.T16 (True or False statements 1 to 8, 8 pairs).
Result: 29 items, required 27 (14 questions, 12 solutions, 1 worked example), optional 1, none 1. Validator: errors 0, 1 warning (see "Inventory" below).

## Borderline

1. **M3.S15.T15.C82 worked example: required (own diagram M3.S15.T15.C82.IMG2).** The text says "A picture shows 9 children (practice values)" and gives all counts in words (4 hats, 5 flags, 2 both). By the tie-breaker alone this could be `none`. I applied v3 as written (FIG_REFERENCED, the whole topic is "reading a picture") and the user's rules 4 and 5 of 23 Nov: the same arrangement is the kept teaching image C82.IMG1, it is not linked, the item gets its own picture. The picture is the arrangement of that teaching image (children 1-2 hat + flag, 3-4 hat, 5-7 flag, 8-9 neither). If the user prefers `none` for this item, only this entry changes.
2. **Food Wastage solution Q3 (M2.S14.T14.C75): optional (not added).** Numeric answer by arithmetic (5 + 6 + 8 + 7 + 4 = 30) from a given figure: Step E "figure-based question, numeric answer: Q required, S none (or optional)". A graph copy with the five readings and the total would help a little (Step D, totals beside a figure).
3. **Food Wastage solution Q4 (M2.S14.T14.C77): none (LATEX_ARITHMETIC).** 30 x 3 = 90 does not touch the graph. Kept `none` rather than `optional` because the figure would be an arrow picture, not the graph.
4. **Food Wastage solutions Q1, Q2, Q5, Q6: required.** The answer is a bar (or two bars) of the graph: "boxed largest / circled smallest" is the named HIGHLIGHT_MEANING case. Each also writes the five readings above the bars (LP step 1 reads them). Q6 is a prediction (sample answer) but its answer is the tallest bar with the reason "its bar is the tallest", so it gets the same mark as Q1 (sibling consistency). Q5 boxes Monday and Friday, the pair the LP sample answer uses.
5. **True or False solutions, all 8 required.** Every solution counts a group of children in a picture of 17; the figure rings every counted child (HIGHLIGHT_MEANING), so the learner can check each count. The LP text carries the counts (user's rule 4: not flipped to none for that reason). Sibling consistency: all eight get a figure.
6. **T/F statement 5 solution (books 14 vs caps 10):** only the 14 book holders are ringed (as the LP step counts), the 10 caps are not ringed again (they are ringed in the solution of statement 2 and are visible as caps on the glyphs). A second ring style would crowd 14 of 17 children.
7. **T/F statement 1 solution:** only the 3 girls with glasses are ringed. The LP's "for example, the girl in the front row with a cap and no glasses" is not marked because two front-row girls fit it (see LP text issues).
8. **Solution key tags** ("3 girls", "10 children", "7 boys" / "7 girls", "7 children", "14 children", "4 boys" / "3 girls", "6 children", "1 child") use only words and numbers of the LP solution text, at most 3 words, in ANSWER green, beside a sample ring.
9. **Colours in the people pictures.** The book shows red caps and blue clothes; the style tokens have no red and WRONG is reserved, so caps are SET_B (amber), books SET_A (blue), backpacks GUIDE (grey), clothes CELL_FILL / MARK_FILL. Rings are FOCUS. Boys' rings solid, girls' rings dashed where two groups are compared (a key tells which).
10. **People are drawn as flat glyphs, not as the book's illustration.** I rejected NOT_RENDERABLE: the figure's information (who wears what) is fully carried by the glyph attributes, and no statement needs faces or art. Every child's attributes are listed in `content` and in `manim_description`, and the counts are asserted in the generator.
11. **Worked example picture:** the nine children alternate pinafore / shorts only as decoration; no statement uses gender. Hats are drawn as the cap shape.
12. **Same book picture or graph used by several items:** one diagram per item, identical spec (render_note says "same as ..."). Their inventory entries are `P08-bar_graph-1` / `P09-arrangement-1` for the first use and `NEW-<id>-q<n>` for each further question use.

## Book mistakes (user's decision 1)

None found. The book prints no answers (no solutions section). Checked against the page pictures and a zoom of page 9:
- Page 8 graph: bars 5, 6, 8, 7, 4 (Sandwich/Mon, Paratha/Tue, Khichdi/Wed, Puri-Sabzi/Thu, Idli-Sambar/Fri), each top on a gridline. Total 30. The base inventory entry P08-bar_graph-1 is correct.
- Page 9 picture: 17 children (9 back, 8 front), 8 girls, 9 boys, caps 10 (5 + 5), glasses 7 (girls 3, boys 4), 14 children with a book (9 + 5; girls 7, boys 7; front child 6 holds two books), 4 backpacks, only back child 1 has cap + book + backpack, cap + glasses 6. The base entry P09-arrangement-1 is correct; every LP count (C85 to C99) agrees with it.
- Page 7 notice board (not used by any item): "13 kg could have fed 25 people" is about 2 people per kg, while question 4 says 1 kg feeds 3 children. As printed; not a slip I corrected, because no item reads the board.

## LP text issues

- **M2.S14.T14.C70, C72, C74, C76, C78, C80 (Food Wastage Q1 to Q6):** the question text never mentions the graph and gives no data; it only works with the picture. Suggested opening sentence for each: "Look at the Food Wastage bar graph." (C70: "Look at the Food Wastage bar graph. Which food item had the highest amount of wastage? ___"). Q4 (C76) uses the total of Q3, so "Use the total wastage from the bar graph." fits there.
- **M3.S16.T16.C85 (True or False answer 1), step 4:** "the girl in the front row with a cap and no glasses" fits two girls (front row 3rd and 6th). Suggested: "For example, the third girl from the left in the front row has a cap and no glasses."
- **M3.S15.T15.C82 worked example:** the question does not say which children have hats or flags (only the counts); the new diagram shows it. Optional sentence if the author wants the text to match the picture: "The first two children have a hat and a flag, the next two a hat only, the next three a flag only and the last two neither."
- **M2.S14.T14.C79 and C81 (also M3.S16.T16.C99):** the old `text` field has "[Image: ...]" lines inside the steps and after the answer, and the concepts list two old solution cards (IMG1, IMG2). The new plan has one solution diagram per answer (IMG1) before step 1; the build must drop the old slots (nothing to change in the step wording).
- **M3.S16.T16.C92, C94, C96, C98 (statements 5 to 8):** `q_figure` hint missing (the first four have it). Hint only, nothing to fix.
- The question texts of M3.S16.T16 use "the picture" with no picture in the text; this is fixed by the new question diagrams (no wording change needed).

## Places where the book is unclear

- Gender of back-row child 3 (cap, glasses, short hair; lower body hidden by the front row). The LP counts him as a boy (boys with glasses back row 3, 7, 8), and the face and hair agree. If he were a girl, statements 1 and 6 would change (4 of 9 girls, 3 boys with glasses). Kept as the LP has it.
- The order of back-row and front-row children is read from the picture where children overlap; every attribute used by a statement was checked child by child on the zoom.

## Inventory (Step 0) and the warning

- P07-notice_board-1 -> none:DECORATIVE_ONLY (story set-up; no item reads 13 or 25). Chunk B's topic T13 covers the same book section and may claim it too; the meaning is the same.
- P08-bar_graph-1 -> Q1 question diagram; NEW-P08-bar_graph-1-q2..q6 -> the other five question diagrams; NEW-P08-bar_graph-1-s1, s2, s5, s6 -> the four solution diagrams that redraw the graph with marks.
- P09-arrangement-1 -> statement 1 question diagram; NEW-P09-arrangement-1-q2..q8 -> the other seven question diagrams; NEW-P09-arrangement-1-s1..s8 -> the eight solution diagrams (the same picture with rings).
- P09-table-1 (the eight statements with tick boxes) -> none:TEXT_SUFFICIENT: the statements are the question text of the eight LP questions; the tick boxes are the learner's answer.
- Validator warning: M3.S15.T15.C82 worked example has no inventory figure because its nine-children practice picture is not printed in the book (it is the LP's own practice picture).
- Kept teaching image M3.S15.T15.C82.IMG1 (nine children) is not linked and not touched; the worked example's diagram is C82.IMG2.
