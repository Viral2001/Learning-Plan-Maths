# Chunk A notes (Class 6 Ch 1, cbse_eng_maths6_ch1_v84)

Chunk A = topics M1.S1.T1, M1.S2.T2, M1.S3.T3, M1.S4.T4, M2.S5.T5, M2.S6.T6, M2.S7.T7, M2.S8.T8, M2.S10.T10 (18 units, 28 items).
Result: required 10 / optional 1 / none 17. Validator: errors 0, warnings 2 (C15 and C26 are required but no printed book figure exists for them; fine).
The generator script is outside HERE: `/tmp/claude-1506/-root-maths-learning-plan/546c0a55-f920-40d7-a2bc-1439e8909fdd/scratchpad/c6ch1_chunkA_work/gen_A.py`.

## Decisions at a glance

| Unit | Item | Decision | Why in one line |
|---|---|---|---|
| 1 | C1 worked (Sun) | none | word reasoning |
| 2, 3 | FiO 1.1 Q1, Q2 (q and sol) | none, none | open discussion |
| 4, 5, 6 | C7, C8, C9 worked | none | numbers are in the text; the steps are arithmetic |
| 7 | FiO 1.2 Q1 question | none (LATEX_TABLE, needs text sync) | Table 1 is a plain text table |
| 7 | FiO 1.2 Q1 solution | none | rules in words |
| 8 | FiO 1.2 Q2 | none, none | list in the text; answers are sums |
| 9 | C15 worked (3, 6, 9 dots) | required (C15.IMG2) | answer IS the three dot pictures |
| 10 | C16 worked (triangle of 4 rows) | required (C16.IMG2) | "why triangular" is the stacking of 1, 2, 3, 4 dots |
| 11 | FiO 1.3 Q1 question (Table 2) | required (C18.IMG1) | Table 2 is referenced and lives only in the picture |
| 11 | FiO 1.3 Q1 solution | required (C19.IMG1, derived_from C18.IMG1) | sixth picture of all seven sequences |
| 12 | FiO 1.3 Q2 question | none | question gives no figure |
| 12 | FiO 1.3 Q2 solution | required (C21.IMG1) | book answer is "refer Table 2"; shows triangle 10, square 16, cube 64 |
| 13 | C22 worked (10 dots two ways) | required (C22.IMG2) | answer IS the two arrangements |
| 14 | C23 worked (hexagon cluster 7 + 12) | optional (not added) | all numbers given; picture would help only |
| 15 | FiO 1.3 Q3 question | none | question gives no figure |
| 15 | FiO 1.3 Q3 solution | required (C26.IMG1) | 36 dots as an 8-row triangle and a 6 by 6 square |
| 16 | FiO 1.3 Q4 question | required (C27.IMG1) | the book shows four hexagon clusters 1, 7, 19, 37 |
| 16 | FiO 1.3 Q4 solution | required (C28.IMG1, derived_from C27.IMG1) | adds the 61-dot cluster |
| 17 | FiO 1.3 Q5 question | none | open "can you think of a picture" |
| 17 | FiO 1.3 Q5 solution | required (C30.IMG1) | printed answer IS a picture (powers of 2 and 3) |
| 18 | Example 1 (odd sums), q and sol | none, none | typeset sums only |

Sibling check for FiO 1.3: all five solutions are required (every answer is a drawing); the two questions that print a figure (Q1 Table 2, Q4 clusters) are required, the three that give none (Q2, Q3, Q5) have no question diagram.

## 1. Judgement calls I was unsure about

1. **Table 1 (FiO 1.2 Q1) stays text.** The question refers to "Table 1" and the LP question text does not contain it, so the learner cannot answer without it. I still chose `none` / LATEX_TABLE because Table 1 is a plain table of ten sequences with names (no colour, no picture inside), and the brief says plain tables stay LaTeX. This needs an LP text sync (`needs_lp_text_sync: true`, the full LaTeX content is in `text_alternative`). If the team prefers a picture of Table 1 instead, the item would become required.
2. **Worked examples C15, C16, C22 are required although each concept already holds a teaching image of the same idea** (C15.IMG1 dots that add columns, C16.IMG1 stack of dots, C22.IMG1 triangle beside rectangle). v3 says a teaching image is never linked and an item that needs its figure gets its own diagram, and in each of these three the answer IS the drawing (draw 3, 6, 9; why triangular; show 10 two ways). The user may judge this a near-duplicate of the teaching image and prefer `none`; the figures are small and cheap.
3. **C16 (triangle of 4 rows) is the borderline one.** Its count (1 + 2 + 3 + 4 = 10) is in the text, but "why is it called triangular" is answered only by the stacking shape. Required (ANSWER_IS_FIGURE).
4. **C23 (hexagon cluster 7 + 12 = 19) is optional, not required.** Every number needed is in the question and the answer is 7 + 12. A picture of a centre dot with a ring of 6 and a ring of 12 would help; it is not added. This differs from C16 on purpose: C16's answer has a visual part, C23's does not.
5. **FiO 1.3 Q2 solution (C21) is required although the printed answer only says "Refer Table 2, page 4, and check for yourself".** The answer is the shape of the arrangement (triangle, square, cube), a picture pointer; I treated it like a printed-answer picture. The question side is `none` (no figure given, and Table 2 is not a concept image of the plan, so the 'refer picture' `optional` rule does not apply). I drew n = 4 for all three (triangle of 4 rows = 10, 4 by 4 dots = 16, 4 by 4 by 4 blocks = 64) so the three shapes are parallel; the old hint `s_figure` names a 3 by 3 by 3 cube of 27.
6. **FiO 1.3 Q3 solution (C26)**: the book answer says "Refer Table 2 and draw" but Table 2 stops at 15 and 25 and never shows 36. The picture follows the LP solution: triangle of 8 rows (1 + ... + 8 = 36) and a 6 by 6 square.
7. **FiO 1.3 Q1 (Table 2) uses one common frame for the question and the solution.** The solution adds a sixth column; the question keeps that slot empty so that "same size, same positions" holds. The card is therefore wider than the five pictures need (the same is true of FiO 1.3 Q4: the fifth cluster slot is empty in the question). If the team prefers each card filled, the solution would be drawn at a smaller scale; I kept the strict rule.
8. **Table 2 is dense** (7 rows, 35 pictures; 42 in the solution) on a 16:9 card. It fits at about 24 px per dot pitch with labels at the minimum text height; the 6 by 6 by 6 cube has 17 px cells. Dots are INK and cube faces CELL_FILL, not the book's row colours (style tokens).
9. **FiO 1.3 Q5 solution (C30) is one card with two rows (powers of 2, powers of 3)**, because a pair gets one solution diagram. The 32 picture of the printed answer is left out (the LP steps stop at 16). Powers of 3: every triangle points right so each picture is visibly three copies of the previous one (the book draws its 3-picture apex-up and its 27-picture as three diagonal blocks side by side; mine is three 9-pictures shifted diagonally, the same dot-and-line structure).
10. **Hexagon clusters (FiO 1.3 Q4)**: the solution shows the whole fifth cluster (61 dots) in ANSWER green rather than colouring the outer ring of 24 only.
11. **Unit 18 (Example 1, odd sums)**: both sides `none`. The picture that explains it ("A picture can explain it") belongs to the units after it (T11, chunk B).

## 2. Things in the LP that look wrong

1. FiO 1.2 Q1 question (M1.S4.T4.C11): the text says "Table 1" but the table is not in the text (see call 1).
2. T8 pairs carry wrong book numbers: the question and answer concepts of M2.S8.T8.C25/C26, C27/C28, C29/C30 say "Figure it Out 1.3, Q1 / Q2 / Q3" and are named "Figure it out: Q1 / Q2 / Q3", but their `ncert_refs` and the book say Q3, Q4, Q5. (T6, which holds Q1 and Q2, is numbered correctly.)
3. FiO 1.3 Q4 question text (C27) contains the stand-in sentence "(Pictures of dot clusters labelled 1, 7, 19, 37.)"; once the diagram follows the question text this phrase is redundant and could go. The numbers 1, 7, 19, 37 then appear only in the picture labels.
4. FiO 1.3 Q1 (C19) answer: the book prints no answer for this question (the printed solutions of section 1.3 start at Q.2); the LP solution (sixth pictures) is the only source. It is correct (11, 12, 21, 36, 216).
5. FiO 1.3 Q5 answer_tex (C30) says "(the solutions add 32)" while the steps stop at 16; harmless, but the figure stops at 16 for powers of 2 and at 27 for powers of 3.
6. Sums checked and correct: Q2 next terms (all ten sequences), unit 4 to 6 worked examples, unit 10, 13, 14 counts, unit 16 (37 + 24 = 61), unit 15 (1 + ... + 8 = 36).
7. Old image/video ids inside item fields are stale (as warned) and were ignored.

## 3. Places where the book is unclear

1. Table 2 (page 4): the triangles for 6 and 15 are a little unevenly spaced in print; read as regular triangles with rows 1, 2, 3, ...
2. Odd numbers row of Table 2: the top row of each picture is left-aligned above the bottom row (verified on the picture): 3 = 1 + 2, 5 = 2 + 3, 7 = 3 + 4, 9 = 4 + 5; the sixth picture (11) is 5 + 6 by the same rule.
3. Printed answer of FiO 1.3 Q5: the 3-picture is drawn apex-up, the 9-picture with right-pointing triangles; the 27 uses perspective with three diagonal blocks. The number of connecting lines in the 27 and in the 16 and 32 pictures was not counted line by line in the base inventory; the specs here follow the "three copies, matching dots joined" and "copy and join" construction (the LP says the same).
4. Printed answer of FiO 1.3 Q4 is only "61"; the picture is not in the printed solutions.
5. Hexagon clusters (page 5): dots touch with thick outlines; the 37 cluster is slightly irregular in print. Row counts 2, 3, 2 / 3, 4, 5, 4, 3 / 4, 5, 6, 7, 6, 5, 4 were checked on the picture.

## 4. Figure claims and possible overlap with other chunks

* Claimed here: P03-table-1 (none, LATEX_TABLE); P04-pattern-1 to P04-pattern-6 and P04-solid-7 (item C18 question, Table 2); P05-pattern-1 (item C27 question); P06-pattern-1, SOL14-pattern-1, SOL14-pattern-2 (item C30 solution); P06-number_pattern-2 (none, LATEX_ARITHMETIC: the odd-sums list is typeset lines in the Example 1 question text).
* Five NEW entries record further uses of base figures inside other chunk-A items: NEW-P04-pattern-5-C16, NEW-P04-pattern-5-C22, NEW-P04-rows-C21, NEW-P04-table2-C19, NEW-P05-pattern-1-C28.
* NOT claimed (left to chunk B, where their questions are): P07-pattern-1 (the 6 by 6 dot square split into odd groups, the answer of 1.4 'how can we partition', units 19 to 22), P07-number_pattern-2, P08-pattern-1, P09-solid-1, P09-pattern-2, SOL15-pattern-1. If chunk B does not claim P07-pattern-1 it will show up unclaimed at the merge.
* Possible duplicate claims at merge: P06-pattern-1 (powers of 2 picture) is also what FiO 1.4 Q6 ("Refer the picture on page 6", chunk B) points at; I took the base id for the first use in LP order (the C30 solution), so chunk B should use a NEW- id or `none`. P06-number_pattern-2 may also be claimed by chunk B; I used the same meaning (LaTeX arithmetic) a second claim should use. The Table 2 rows are also referred to by FiO 1.4 Q4, Q5 and Q7 ("refer Table 2"); I claimed them for the 1.3 Q1 question diagram.
