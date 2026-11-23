# Chunk C notes (M3.S17.T17, M3.S18.T18, M3.S19.T19): Figure it Out 1.5, 1.6 example and worked example, Figure it Out 1.6

Result: 16 items = required 8 (7 questions, 1 solution) / optional 2 / none 6. Validator: errors 0, warnings 0.
The generator script and a quick bounding-box layout check (every shape and text inside the canvas, nothing overlapping) are in the scratchpad, not in HERE.

## 1. Judgement calls

1. **Table 3 is one picture in the book, used by 7 questions.** Each question gets its OWN diagram (v3 rule: one per item).
   - 1.5 Q1 (C71) and 1.5 Q2 (C73): the whole of Table 3 (five rows), identical spec (C73 says "same as M3.S17.T17.C71.IMG1").
   - 1.6 Q1 to Q5 (C78, C80, C82, C84, C86): only the row the question names, drawn larger and alone (row-name boxes left out; the question names the sequence).
   - Why required: the question points at Table 3 (FIG_REFERENCED) and the shapes exist only in the picture (DATA_IN_FIGURE). A student cannot count sides, lines, squares, triangles or segments from the words.
   - Layout: 16:9 card, five horizontal bands with a label box on the left, a sixth column on the right left empty so the 1.5 Q2 answer can add one shape per row without moving anything. Coordinates are in the spec.
2. **Colours.** The book prints the 8 regular polygons in 8 colours and K-graph dots in red; colour carries no meaning there, so the spec uses CELL_FILL for polygons and INK dots. Row frames (dotted), the cream panel and the watermark are left out.
3. **1.5 Q1 solution: none.** The answer is five number sequences (text in the LP and in the book). A picture with counts under every shape would only repeat the question figure.
4. **1.5 Q2 solution: REQUIRED (ANSWER_IS_FIGURE), the one solution diagram of this chunk.** The question asks to redraw the sequences and draw the next shape; the answer is those drawings. The book prints no answer for Q2 at all, the LP gives an "open ended, typical" answer. Per prompt section 5 rule 4 the figure draws the LP's own sample: an 11-sided polygon (one more side than the decagon), K7 (21 segments), 6 by 6 squares (36), a 6-row stacked triangle (36), Koch stage 5 (3 x 4^5 = 3072 segments). Everything given stays INK; the five new shapes are ANSWER green at the end of each row (derived_from C73.IMG1). The Koch stage 5 looks almost the same as stage 4 at this size, which is also what the LP says ("the segments become very tiny"). **If the user prefers text only for open-ended answers, change C74 to none (TEXT_SUFFICIENT).**
5. **1.6 solutions (sibling consistency).** The five answers are all "number sequence plus a reason". Q1, Q3, Q5 are none: the reason is already visible in the question figure (names and corners, n by n grids, the speed bump). Q2 and Q4 are optional (NOT added): the reason there is made of marks the question figure does not carry (the lines each new point adds: 1, 2, 3, 4, 5; the rows of 1, 3, 5, 7, 9 triangles). A green-highlight version would be nice but the text already says it. Printed answers (pdf p.16-17) are text only.
6. **Worked examples: none for both.**
   - C75 (sides of regular polygons): the LP block is a statement (3, 4, ..., 10 and the shape names); the text carries it, the concept already has its own teaching picture (not linked, only 3 to 6 sides), and the Regular Polygons row with names is drawn for 1.5 and 1.6 (T17 comes before T18).
   - C76 (matchsticks, row of 5 triangles): a word problem with no given figure; a question figure would invent one (and would show the answer, 11 sticks). The concept already has its own teaching picture of exactly this row.
   If the user wants a figure in either, the natural ones are: C75 the 8 polygons labelled with 3 to 10 (same as the 1.6 Q1 diagram plus side counts); C76 triangles built up with new sticks in green.
7. **Koch speed bump (P12-shape-1).** The book prints no lengths. I measured the page picture at 8x zoom: flat part, two slanted sides, flat part are all about 170 px, so it is the standard Koch bump (four equal segments, equilateral triangle on the middle third). That is also what the book's answer requires (3, 12, 48 = x 4 each time). The 1.6 Q5 diagram has a top strip: segment, arrow, speed bump (the arrow is mine, it only stands for "is replaced by"), then the five stages. The Koch outlines must be generated in code from the rule (counts 3, 12, 48, 192, 768; stage 0 triangle points left and stage 1 is a six-pointed star with points left and right, as in the book).
8. **Figure ids.** Table 3 is five base entries (rows) of the inventory. Each row is claimed by the base id for its first use in this chunk (the whole-table figure of C71) and by `NEW-<base id>-fio2q`, `-fio2sol`, `-fio16q` for the other three uses; P12-shape-1 is claimed by C86. 21 entries, all `item:`. No `concept_image:` mapping: the inventory calls Table 3 a "teaching figure", but the 18 concept images do not show it (C68 and C69 of T16 are different, partial pictures, and are not in my units).
9. **Possible merge conflict with chunk B.** Table 3 is on the book pages of section 1.5, which chunk B's topic T16 also covers. If chunk B maps the P10-* base ids to a concept image (or none), the merge step will report a conflict. Resolution: keep the base id with chunk B's meaning and rename chunk C's first-use entries to `NEW-<base id>-fio1q` (item `M3.S17.T17.C71 (question)`).

## 2. Things in the LP that look wrong

- **C71 / C72 question text** (1.5 Q1): "...in Table 3? Regular Polygons) Pattern? Complete Graphs) Pattern? Stacked Squares) Pattern? ..." has stray sub-question fragments ("Regular Polygons)" etc.), and the table itself is not in the text. The diagram supplies the table; the stray fragments should be cleaned in the LP (a), b), c)... or removed).
- **C72 answer, Koch line:** `steps_tex` lists four terms (3, 3 x 4, 3 x 4 x 4, 3 x 4 x 4 x 4) but `answer_tex` and the table have five stages (the fifth is 3 x 4 x 4 x 4 x 4 = 768). The book's printed answer has five terms.
- **C85 (1.6 Q4):** the LP reasons "rows hold 1, 3, 5, 7, 9 little triangles, odd numbers add up to squares", while the book prints "1, 4, 9, 16, 25 = 1, 1+2+1, 1+2+3+2+1, ... (adding up and down)". Both end at the square numbers; the LP's row count is the correct one for the picture (row r has 2r - 1 little triangles, checked on the page picture). LP wins; the diagram agrees with the LP.
- **C86 (1.6 Q5) question text** drops the small inline drawings of the segment and the speed bump, so the sentence "replaces each line segment by a 'speed bump'" has nothing to point at; only the figure carries it. It also says "not shown in Table 1" (this is the book's own wording, correct).
- **C75 question** is a statement, not a question ("The number of sides ... is given by ..."): it is the book's Example text copied as a worked-example question.
- **C76 (matchsticks)** has no book source (`ncert_refs` empty); it is an LP-made example.
- Stale ids inside item fields (video and card ids that do not exist) were ignored, as instructed.
- LP book numbers match the book (Figure it Out 1.5 Q1, Q2; 1.6 Q1 to Q5).

## 3. Where the book itself is unclear

- The speed bump has no printed lengths (see call 7).
- K6 is printed small and its crossing diagonals cannot be counted one by one; the 15 segments follow from "every pair joined" (and from the printed answer 1, 3, 6, 10, 15).
- Koch stages 4 and 5 look almost identical at printed size; 192 and 768 come from the printed solution, and the picture is generated from the rule.
- The book prints no answer for 1.5 Q2, and the printed answer of 1.5 Q1 is bare sequences (no picture), so no printed-answer figure belongs to this chunk (pdf pages 16 and 17 were looked at).
- Shape sizes: the book draws Table 3 on a portrait page; here it is re-laid out on a 16:9 card (small shapes of about 0.7 to 1.0 units in a 9-unit-high card). If the renderer finds the stacked triangles too small, the first thing to give up is the row-label boxes.
