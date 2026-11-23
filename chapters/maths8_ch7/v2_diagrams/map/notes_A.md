# Chunk A notes (Class 8 Ch 7 "Proportional Reasoning", cbse_eng_maths8_ch7_v22)

Units: 16 (3 worked, 13 pairs), 29 items: required 6, optional 2 (not added), none 21.
Required: FiO Q4 question (C7), FiO Q5 question + solution (C9, C10), FiO Q7 solution (C12), FiO Q6 question + solution (C26, C27).
Optional (no diagram added): C8 (Q4 solution), C39 (Example 7 solution).
Validator: errors 0, one warning (C12 solution: no printed figure maps to it, fine because the book's answer is "Try yourself").
Generator script (outside HERE): scratchpad `A/build_A.py`.

## 1. Judgement calls

- **The pdf does have a printed-solutions section** (pdf pages 23 to 30, "Page No. 165" onwards), although the brief says it has none. Its pictures for Q4 to Q7 are copies of the question figures (the printed answers are text). I claimed them in my chunk: P24-shape-1 -> `none:SAME_AS_QUESTION_DIAGRAM`; P24-shape-2, P25-pattern-1, P25-pattern-2 -> the solution item whose diagram redraws that figure (C10, C27); P25-human_figures-1 -> `none:DECORATIVE_ONLY`.
- **Base inventory correction.** P25-pattern-2 (wall b) has wrong per-row counts in the base: rows 3 to 5 are not "9 O, 8 G" (row 3 `GGOGOGOGOGOGOGOGO` has 8 O); the right per-row brown counts are 4, 8, 8, 8, 8, 8, 4 (48), grey 13, 9, 9, 9, 9, 9, 13 (71), 119 bricks. The entry starts with "CORRECTED:". The row strings of both walls were checked by pixel sampling of page 8 and match P08-pattern-3 / -4 exactly. All other base entries I claimed agree with the page pictures (P08-shape-1 sizes agree within 2 percent; P08-shape-2 about 163 x 97 px).
- **FiO Q4 (C7), question required.** Five tilted rectangles exist only in the picture. Spec = the book's layout, measured on the page: A 1:3 upright, B 2:3, C 2:5 tilted 35 deg clockwise, D 1:3 tilted 18 deg anticlockwise, E 2:5 tilted 45 deg clockwise. Measured ratios (A 3.07, D 3.03, C 2.54, E 2.55, B 1.50) are tidied to exact 1:3, 2:5, 2:3 so the matching pairs are exactly alike. The figure marks no pair (no leak). Overlap and margin checked in code.
- **FiO Q4 (C8), solution optional (not added).** The LP solution is only a procedure and never names the matching rectangles, and the printed answer does the same. A solution picture (A, D in SET_A and C, E in SET_B) would only be possible once the text names the pairs. See LP text issues.
- **FiO Q5 (C9, C10).** Question required (given rectangle to measure); solution required (answer = the drawn smaller and bigger rectangle, B2 `ANSWER_IS_FIGURE`; the LP gives 6 x 4, 3 x 2, 12 x 8). The rectangle is drawn 3:2 although the book's rectangle measures about 5:3 (162 x 97 px, no lengths printed): the LP solution's example is 6 cm : 4 cm and the LP text wins. Question card draws the rectangle 3.6 x 2.4 units, solution card 2.4 x 1.6 (0.4 units per cm) so that the three rectangles fit in one row; shape and style unchanged (said in both `render_note`s).
- **FiO Q7 (C11, C12).** Question none (`OPEN_ENDED`: the learner measures a friend; the book's three oval figures carry no lengths). Solution required (`ANSWER_IS_FIGURE`, B2 'draw a figure'; stands alone, `derived_from` null): the LP's sample (friend 20 / 60 / 60 / 80 cm, factor 1/10) drawn as a plain front-view figure with head 2, torso 6, arms 6, legs 8 cm marked by two rulers. Parts are plain shapes, no face (rule: no faces/clip-art). Sibling consistency: the other 'draw it' task (Q5) is also required on the solution side. `needs_lp_text_sync` is true because the LP text gives only head and torso (see LP text issues).
- **FiO Q6 walls (C26, C27).** One card per item holds both walls (a above b), because the LP did not split the question and a pair gets one question and one solution diagram. Letters (a), (b) are drawn because the LP question and answer refer to "wall (a)" and "wall (b)" (decision 3). Bricks use figure-specific fills (grey #B9BABB, red #D2232A, brown #BA7B3F, sampled from the page), named in the spec. Solution: the same walls plus a dashed FOCUS outline of one repeating block (bricks 3 to 7 of each row in (a): grey 2+3+4 = 9, red 3+2+1 = 6; bricks 3 to 6 of each row in (b): grey 16, brown 12) and four short ANSWER tags ("9 grey", "6 coloured", "16 grey", "12 coloured"; 2 words each, LP words). The book marks no block; the windows are one valid choice that reproduces the printed counts (checked in code row by row).
- **Worked examples C2, C13, C16: none.** All numbers are in the text; the book's tigers (C2), the 60:40 image (C13) and the three mugs (C16) are teaching figures that exist as concept images (M1.S1.T1.C1.IMG1, M2.S5.T5.C13.IMG1, M2.S5.T5.C16.IMG1) and no question text refers to them. P01 -> concept image M1.S1.T1.C1.IMG1, P07-illustration-1 -> M2.S5.T5.C16.IMG1, P02 table -> `LATEX_TABLE`.
- **Coffee table (C20, C21): none, `LATEX_TABLE` on both sides.** The book's table is plain numbers with an empty last column (no colour or arrangement meaning), the LP lists the five pairs in the question text, and the answer is a filled plain table: Step C wins over `ANSWER_IS_FIGURE`. `text_alternative` gives the LaTeX array to write.
- **Example 7 (C38, C39).** Question none. Solution `optional` (not added): the book's small arrow picture (14:21 to ___ :42 with x 2) covers the first blank only; LaTeX steps already give every factor and result (v3 'arrow picture for an expression already written': optional). P06 -> `none:LATEX_ARITHMETIC`.
- **Plain arithmetic and word items: none** (C5/C6, C18/C19, C22/C23, C24/C25, C28/C29, C34/C35, C36/C37). 'Circle the true statements' (C24) is an action on text statements, not on a figure.

## 2. LP text issues

- **M1.S3.T3.C8** (solution of FiO Q4): never says which rectangles are similar; it also says "width : height", which has no meaning for tilted rectangles. Suggested closing sentence: "Measuring short side : long side gives about 1 : 3 for A and D, about 2 : 5 for C and E and about 2 : 3 for B, so A and D are similar, C and E are similar, and B is similar to none of the others."
- **M1.S4.T4.C10** (solution of FiO Q5): the example "6 cm : 4 cm" does not match the printed rectangle (about 5 : 3 on the page, no lengths printed); the hint `q_figure` of C9 ("6 cm wide and 4 cm high") is likewise an assumption. The spec follows the LP (3:2). Suggested sentence if the learner is to measure the printed rectangle: "Measure the rectangle; it is about 5 cm by 3 cm, so width : height is 5 : 3. A smaller one: 5 x 1/2 = 2.5 and 3 x 1/2 = 1.5; a bigger one: 5 x 2 = 10 and 3 x 2 = 6." (If this is adopted, the diagram numbers must be changed to match.)
- **M1.S4.T4.C12** (solution of FiO Q7): step 3 gives only the scaled head (2 cm) and torso (6 cm), and no step gives torso : arms although the question asks for it. The figure also labels arms 6 cm and legs 8 cm. Suggested sentences: "Torso : arms is 60 : 60, which is 1 : 1." and "60 x 1/10 = 6 cm for the arms and 80 x 1/10 = 8 cm for the legs."
- **M2.S8.T8.C26** (question of FiO Q6): the question text already states the per-row counts of block (a) (2, 3, 4 grey; 3, 2, 1 coloured) and the totals of block (b) (16 and 12), which the book leaves for the learner to find from the picture, and it speaks of "one block" without saying which bricks form a block. Suggested: ask only "In each wall find the ratio of grey bricks to coloured bricks in one repeating block" and keep the counts in the solution (C27). The decision was not changed (decision 2).
- **Book numbers in the LP.** C9/C10 "Figure it Out, Q1" is book Q5 (p.166); C11/C12 "Figure it Out, Q2" is book Q7 (p.167); C26/C27 "Figure it Out, Q2" is book Q6 (p.166); C28/C29 "Figure it Out, Q3" is Q1 of the 7.6 Figure it Out (p.176). C5/C6 also adds image E, which the book question (D only) does not.
- **M2.S6.T6.C21** (coffee solution): "200 : 400 is 1 : 2, so strong." gives no comparison number as the neighbouring lines do. Suggested: "$200 \div 400 = 0.5$, more than $0.43$, so strong."
- **M2.S10.T10.C34/C35** (Example 2): the LP says "18 glasses in all"; the book says "18 more glasses" but then solves 6 : 10 :: 18 : 30, i.e. 18 glasses in all. The LP wording is the consistent one (decision 1: follow the LP); no change needed.

## 3. Places where the book is unclear

- FiO Q4 prints no lengths; the matching pairs (A with D, C with E, B with none) come from measuring the page picture (about +/-3 percent). The printed answer is a method only.
- FiO Q5's rectangle has no lengths; about 5 : 3 by measurement.
- FiO Q6 marks no block; the printed answers (2+3+4 = 9, 3+2+1 = 6; 16, 12) fix only the counts.
- FiO Q7's printed answer is "Try yourself." with no picture.
- Example 2: "18 more glasses" against the modelled 6 : 10 :: 18 : ? (see above).
- Page 1 tiger pictures are not exactly to the table sizes (C about 1.4:1 against 1.5:1; E about 0.91:1 against 1:1): irrelevant here, they are a concept image.
- Book print slips that change a spec value: none found in this chunk (decision 1 not triggered). The printed Q6 answers are correct.

## Borderline

- **M1.S3.T3.C8** solution `optional`: a colour-coded pairs picture would help, but the LP text does not state the pairs.
- **M1.S4.T4.C12** solution `required`: a sample drawing of an open-ended 'draw a figure' answer; arms and legs labels come from LP numbers (60 and 80 cm x 1/10) that the text does not spell out.
- **M2.S8.T8.C26** question `required` even though the LP text carries the counts (decision 4); **C27** solution `required` for the block outlines (the picture changes how clearly the counted bricks can be seen).
- **M1.S4.T4.C10** solution `required` and **C9** question `required`; the 3:2 shape against the book's 5:3 (see section 1).
- **Worked examples C2, C13, C16** `none`: a figure would help but a careful learner loses nothing without it and concept images exist.
- **C20/C21** `none` (`LATEX_TABLE`) although the printed answer is a filled table.
- **M2.S10.T10.C39** solution `optional`: book's arrow picture for the first blank only.
- **C24/C25** `none` ('circle' is an action on text, not on a figure).
- Sibling check: Q4 solution (procedure, optional) against Q5 and Q7 solutions (a drawing, required) differ because the answers differ in kind: Q4 names letters, Q5 and Q7 end in a drawing.
