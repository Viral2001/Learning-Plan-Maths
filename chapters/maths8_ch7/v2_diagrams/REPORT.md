# Class 8 Ch 7 Proportional Reasoning - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths8_ch7` v22 (taken from staging). Result: new V2 version v23 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (96 items from 52 units)
{"worked_example": {"none": 7, "required": 1}, "question": {"none": 40, "required": 4}, "solution": {"none": 36, "optional": 3, "required": 5}}

Optional, NOT added: [('C8', 'solution'), ('C39', 'solution'), ('C93', 'solution')]

needs_lp_text_sync: [('C12', 'solution')]

## The 10 diagrams
| id | side | type |
|---|---|---|
| M1.S3.T3.C7.IMG1 | question | geometry_figure |
| M1.S4.T4.C9.IMG1 | question | geometry_figure |
| M1.S4.T4.C10.IMG1 | solution | geometry_figure |
| M1.S4.T4.C12.IMG1 | solution | other |
| M2.S8.T8.C26.IMG1 | question | other |
| M2.S8.T8.C27.IMG1 | solution | other |
| M2.S11.T11.C43.IMG1 | solution | mensuration_figure |
| M3.S16.T16.C60.IMG1 | question | mensuration_figure |
| M3.S16.T16.C61.IMG1 | solution | mensuration_figure |
| M5.S31.T31.C120.IMG2 | worked example | cell_row |

### Chunk A notes (from the decision agent)
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

### Chunk B notes (from the decision agent)
# Notes, chunk B (Class 8 Ch 7 "Proportional Reasoning", live plan cbse_eng_maths8_ch7_v22)

Result: 29 items (14 pairs + 1 worked example). required 3 / optional 0 / none 26. Validator: errors 0, one warning (see 3 below).

The three diagrams:
- `M3.S16.T16.C60.IMG1` question, `M3.S16.T16.C61.IMG1` solution: the mason's house plan (book Figure it Out 2, second set, Q2).
- `M2.S11.T11.C43.IMG1` solution only: the two drawn rectangles of Example 5 (blackboard ratio).

Figure inventory: only two base figures belong to this chunk: `P13-shape-1` (question picture, mapped to C60 question) and `P26-shape-1` (the same plan reprinted on the printed-answers page, mapped to C61 solution). Both base descriptions were checked against the page pictures and are right. The other figures on pages 5-13 belong to other chunks (Example 7 arrow diagram, coffee table, FiO Q4-Q7 pictures: chunk A; shampoo table and Puneeth's motorcycle: chunk C). Pages 5, 6, 7, 9, 10, 11, 12, 13, 18, 19, 23, 26, 28, 29 were looked at as pictures; pages 17-19 hold a crane-and-girl illustration for FiO4 Q4, which is chunk C's and decorative.

## 1. Judgement calls

- **C60 question (mason): required.** "the shape shown in the diagram" (FIG_REFERENCED); the layout and the five labels (12, 15, 9, 9, 6 ft) exist only in the picture.
- **C61 solution (mason): required, derived_from C60.IMG1.** The picture alone marks 5 of the 10 wall lengths that the printed sum 12+12+12+15+9+15+9+9+9+6 = 108 uses. The solution figure adds the other 5 (inner wall 12, right edge 12, top of the left room 9, bottom of the right room 15, left side of the small room 9) in ANSWER green, and keeps the 5 given labels in INK. It does not show the total. I did not use SAME_AS_QUESTION_DIAGRAM because the solution does add visual content (borderline, see below).
- **P26-shape-1 mapped to the C61 solution item** (not to `none:SAME_AS_QUESTION_DIAGRAM`): the reprint on the answers page carries no new marks, but it is the picture the solution figure is built on. If the merger prefers, `none:SAME_AS_QUESTION_DIAGRAM` would be an equally sound reading; the decisions for the items do not change.
- **Small room drawn 9 ft high (book prints about 8 ft).** The book's picture draws the small rectangle about 8 ft high (about 121 px against 15.3 px per ft; page 26: 65 px against 8.2 px per ft) but labels it 9 ft, and the printed answer uses 9 twice for it. Following the user's decision 1, the spec draws the plan to the labelled scale (24 x 12 ft, small room 6 x 9 ft). The base inventory still records what the book prints.
- **C43 solution (Example 5, blackboard rectangle): required (ANSWER_IS_FIGURE).** The question asks to draw a rectangle in the ratio of the blackboard, the LP answer is a drawing (3 cm by 1 cm, or 9 cm by 3 cm), and the steps only describe it in words (Step B2, "answer is a filled figure / drawing, even if the steps describe it in words"; Step E "word question, figure answer: Q none, S required"). The figure shows the two sample rectangles from the LP step 3, outlined in ANSWER green on one baseline, to one scale (ratio 3 : 1 each). The question side (C42) is `none` (OPEN_ENDED, TEXT_SUFFICIENT): the learner measures their own board and the book gives no figure, so no question figure is invented. Sibling in chunk A: FiO1 Q5 ("draw a smaller and a bigger rectangle with the same ratio") has the same kind of answer; I did not read chunk A, but for consistency it should be treated the same way.
- **Worked example C49 (cross multiplication and Aryabhata's rule): none.** Arithmetic only; the book has no picture there. The kept teaching image `M3.S13.T13.C49.IMG1` stays and is never linked.
- **Examples 8, 9, 6 and all Figure it Out word problems: none.** Examples 8 and 9 and Example 6 have a teaching image each (C48, C50, C70), never linked; the problems are word problems with all numbers in the text, and the solutions are LaTeX arithmetic (Step C). I considered a double number line for FiO4 Q9 (tap) and a bus picture for FiO4 Q2, and kept both as text: a careful student loses nothing without them (tie-breaker), and no v3 rule triggers.
- **No `optional` items.** I found no figure that "would clearly help" beyond the text, so optional is 0.

## 2. Borderline

- `M3.S16.T16.C61` solution (mason): required because it adds five labels the question figure lacks; it would be `none` (SAME_AS_QUESTION_DIAGRAM) if only the picture were repeated.
- `M2.S11.T11.C43` solution (Example 5): required because the answer is a drawing; a reader could say a student can draw it from the sizes given in text. Kept required under the rule as written.
- `M3.S13.T13.C49` worked example: none; a crossing-arrows picture of ad = bc could help, but it already exists as a teaching image and the rule forbids linking it.
- FiO1 Q2 and Q3, Examples 4, 8, 9, 6: none by the Step C tests (word or arithmetic only).

## 3. Validator warning

- `M2.S11.T11.C43` (solution) is required but no base-inventory figure maps to it: correct, the book prints no picture for Example 5 (and no printed answer); the figure is the LP answer's own drawing.

## 4. LP text issues (not edited, listed only)

- `M3.S16.T16.C61` (mason, solution step 1): the sum "12 + 12 + 12 + 15 + 9 + 15 + 9 + 9 + 9 + 6 = 108 ft" does not say which wall each term is. Suggested sentence: "Walls: left $12$, inner $12$, right $12$; top $9 + 15$; bottom $9 + 15$; small room left $9$, right $9$, bottom $6$, so $12 + 12 + 12 + 9 + 15 + 9 + 15 + 9 + 9 + 6 = 108\text{ ft}$." (same ten numbers, in an order that follows the figure).
- `M3.S16.T16.C60` (mason, question): the text lists the five printed lengths but the learner needs the picture for the rest; once the token is inserted after the question text this is fine. The book's own sentences "He needs to construct both the outer walls and the inner wall that separates two rooms" were merged into one sentence.
- `M3.S16.T16.C62` (buses, question): LP says "This year we have 204 students" (as the chapter page 18 does); the book's printed answer (page 28) reads "204 students and teachers". Suggested question sentence: "This year we have $204$ students and teachers." (the numbers in the LP answer already treat 204 as the number of people).
- `M3.S16.T16.C64` (Lilavati, question): `question` keeps "O expert businessman! tell me quickly" while `question_tex` has "expert businessman! tell us quickly": the two fields differ from each other and from the book ("O expert businessman! tell me quickly").
- `M2.S11.T11.C40` (Example 4): `question` says "my school" and `question_tex` says "our school" (book: "my school"); the two fields differ.
- `M3.S18.T18.C73` (Example 6): the question ends "...when Neelima is 12?", the book also asks "Would it remain the same?". The answer steps (step 4) answer it. Suggested sentence: add "Does the ratio stay the same?" to the question.
- `lp_book_number` values are LP-internal, not the book's numbers: C46 "Figure it Out, Q1" is book FiO1 Q3; C60 "Figure it Out, Q1" is book FiO2 Q2; C64, C66, C68 "Q3, Q4, Q5" are book FiO4 Q5, Q7, Q9; C44 reads "Ratios and Proportions, Q2" (book FiO1 Q2). Items were found by their text.
- `M3.S13.T13.C49`: the worked example uses 120 : 15 :: 80 : 10 taken from Example 8; the book has no such separate example, so this is an LP-made worked example (fine, listed for completeness).

## 5. Where the book itself is unclear

- Page 13 / page 26 mason picture: only five lengths are printed; the other five are implied by the printed answer, not by labels. The small room is drawn about 8 ft high but labelled 9 ft (see 1).
- Page 28 printed answer to FiO4 Q2: "x = 34/9" (3.78 buses) is printed without the working; the LP gives 204 / 54 about 3.78, which agrees.
- The printed answer to FiO4 Q9 (tap) shows only "300 seconds or 5 minutes"; the LP steps (10 L = 10000 mL, factor 20) fill the gap and are correct (20 x 15 = 300).
- Recomputed and found correct: 5 : 170 = 1 : 34; 12 : 360 = 1 : 30; 360 : 120 = 3 : 1; 8 : 18, 12 : 27, 16 : 36; 18 : 24 = 3 : 4, 12 : 16, 20 : 80/3, 27 : 36; 120 x 10 = 15 x 80 = 1200; 15 x 2/3 = 10; 240 x 90 / 150 = 144; 940000000 / 52 = 18076923.08; 108 ft and 1450 x 108 / 10 = 15660; 162 / 3 = 54, 4 x 54 = 216, 216 - 204 = 12; 2.5 x 9 x 7 / 3 = 52.5; 37 / 2 = 18.5; 10000 / 500 = 20, 20 x 15 = 300 s = 5 min; 3 : 30 = 1 : 10, 12 : 39 = 4 : 13.

### Chunk C notes (from the decision agent)
# Notes for chunk C (Class 8 Ch 7, topics M3.S19.T19 to M5.S31.T31)

Result: 38 items = 1 required, 1 optional, 36 none. Validator: errors 0, warnings 0.
Required: `M5.S31.T31.C120.IMG2` (Binairo worked example). Optional (not added): solution of `M4.S25.T25.C93`.

## 1. Judgement calls

- **Almost everything is none.** Every other pair or worked example in this chunk is a word problem or proportion arithmetic (speed and time, age, ploughing, tea prices, city crowding, sharing in a ratio, paint, idli, crane, coin, manure, land price, unit and temperature conversion). The book prints no figure for any of these questions or for their answers (the "Ans." pages 23 to 30 are text only; I looked at the page pictures). The answers are numbers, amounts or ratios, not drawings.
- **M3.S21.T21.C82 (shampoo worked example): none, LATEX_TABLE.** The book's Activity 2 table is a plain banded table with no colour meaning, and the question sentence already lists the four sizes and prices. `text_alternative` holds the LaTeX array to write if the content team wants the table.
- **M4.S25.T25.C92 / C93 (Activity 3, share 12 in 3 : 1 and 42 in 4 : 3).**
  - Question: none. The question gives no figure. The children-and-seeds picture is an illustration (a heap of 12 seeds, no numbers) and the three pink circles (3 + 9, 8 + 4, 2 + 10) are open examples, not the ratios asked.
  - Solution: **optional**, not added. The book's two flow diagrams (P15 for 12, P16 for 42) are in-chapter teaching figures, and the 42 one already has the teaching image `M4.S24.T24.C88.IMG1`. The LP steps carry every number and the answer is two pairs of numbers, not an arrangement. A single card with both trees side by side (whole 12 -> 3 : 1 x 3 -> 9 : 3, whole 42 -> 4 : 3 x 6 -> 24 : 18) would be the figure to add if the user wants it.
- **M4.S27.T27.C108 (crane).** The book's crane-and-girl picture on p.176 is a joke illustration with no measures on it. Question and solution are none. The picture was missing from the base inventory, so it is added as `NEW-P18-crane-girl` (none, DECORATIVE_ONLY).
- **M4.S29.T29.C115 (manure, plot 200 ft by 500 ft).** none. A rectangle with two side lengths would add nothing the sentence does not already say; the teaching image C114 is not linked.
- **M5.S31.T31.C120 (Binairo): required.** See Borderline.
- **Figure inventory (13 entries).** Items 2 (both book Binairo example grids, mapped to the worked item), concept image 1 (P16, the 42-counter teaching image), none 10 (P13 table LATEX_TABLE; P14 children DECORATIVE_ONLY; P14 pink circles OPEN_ENDED; P15 TEXT_SUFFICIENT; three Binairo practice grids OPEN_ENDED; two blank Dot Grid sheets OPEN_ENDED; the crane picture DECORATIVE_ONLY). I claimed the Dot Grid pages 21 and 22 because they follow the Binairo Puzzle Time page that belongs to my last unit; if another chunk also claims them, give them the same meaning (none:OPEN_ENDED, a blank drawing aid that no question refers to).
- **Base descriptions checked against the pictures.** P13 table, P14 (the circles were re-counted on a zoomed crop: 3 + 9, 8 + 4, 2 + 10 confirmed), P15, P16, P20 (all five grids, cell by cell) and P21 (14 x 22 dots) were right. No "CORRECTED:" entry was needed.
- **Book mistakes (user decision 1):** none found in the figures or printed answers of this chunk. The book's Harmain answer (x years later, x + 1 : x + 5 = 1 : 2, x = 3, age 4) and the LP's (x = her age, x : (x + 4) = 1 : 2, x = 4) reach the same age; the LP is right and was left alone.

## 2. LP text issues

(No LP text was edited and no decision was changed because of these.)

- `M5.S31.T31.C120` (worked example, step 3): "The fourth cell next to a vertical pair would make three verticals if cells 3, 4 and 5 were all vertical" is muddled: cells 3 and 5 are not a pair, cell 4 sits between them. Suggested sentence: "If cell 4 were vertical, cells 3, 4 and 5 would be three verticals in a row, so cell 4 is horizontal."
- `M5.S31.T31.C120` (question): the cells are never numbered, yet steps and answer say "third cell", "cell 4", "cell 6". Suggested addition: "Number the cells 1 to 6 from the left." (The diagram prints position numbers 1 to 6 under the cells for this reason.)
- `M5.S31.T31.C120` (book coverage): the book's Binairo page has a 6 x 6 solved example and three 6 x 6 practice puzzles (P20 grids 3, 4, 5). The LP keeps only a one-row example and its textbook block ends "Solve the following Binairo puzzles." with no puzzle given. Suggested: add the three practice grids as question items (each would be required: DATA_IN_FIGURE and ACTION_ON_FIGURE, with the given cells listed in the inventory descriptions of P20-binairo_grid-3/-4/-5), or drop that sentence.
- `M4.S25.T25.C92` (question) and C93 (steps): the steps say "Partner: 3 x 3 = 9; you: 1 x 3 = 3", but the question never mentions a partner or which share is whose. Suggested sentence: "Share 12 counters between you and your partner in the ratio 3 : 1 (partner : you), and then 42 counters in the ratio 4 : 3."
- Book-number labels differ from the book's own numbering (the LP's own numbering is used for the cards, the `ncert_refs` are right):
  - `M3.S20.T20.C79/C80` "Figure it Out, Q1" is the book's 7.6 Q11 (tractor).
  - `M4.S27.T27.C100/C101` "Figure it Out, Q1" is the book's 7.5 Q2; C102/C103 "Q2" is Q3; C104/C105 "Q3" is Q4; C106/C107 "Q4" is Q5 (the book's 7.5 Q1 is C94 "Ratio Sharing, Q1").
  - `M4.S27.T27.C108/C109` "Figure it Out, Q5" is the book's 7.6 Q4 (crane); C110/C111 "Q6" is Q12 (coin).
  - `M4.S30.T30.C117/C118` "Figure it Out, Q1" is the book's 7.6 Q10 (land price).
  Suggested: label them with the book's numbers (7.5 Q2, Q3, Q4, Q5; 7.6 Q11, Q4, Q12, Q10).
- `M3.S21.T21.C82` (worked example): the book's Activity 2 asks whether price is proportional to volume; the LP question asks "Which size gives the cheapest shampoo per mL?" and the answer says the sachet (about Rs 0.33 per mL) is cheapest. The arithmetic is right (2/6, 154/180, 276/340, 540/1000), only the question differs from the book's. No change needed unless the team wants the book's wording.
- Arithmetic of every pair in the chunk was re-computed and matches the LP text: 100 / 75 = 4/3 h = 1 h 20 min; 20 x 6 = 120 h and 20 x 1.5 = 30 h; 30000000 / 1484 = 20216 and 20000000 / 550 = 36364 (rounded); 12 / 4 = 3 rounds, 42 / 7 = 6; 4500 / 5 = 900; 4000 / 4 = 1000; 5 : 2 :: 30 : 12; 240 / 6 = 40; 40 / 8 = 5 and 15 : 45 = 1 : 3; 3 : 13; 4/10 of 155 = 62; 7.74 x 3 / 4 = 5.805 g, Rs 5.26 + Rs 2.59 = Rs 7.85; 1e9 / 43560 = 22956.8; 3.6e9 / 43560 = 82645.

## Borderline

- **`M5.S31.T31.C120` Binairo worked example, required.** Against: the question describes the row completely in words and the LP answer "H H V H V V" is a text string, so a careful student could solve it from the text alone (tie-breaker). For: the answer is an arrangement of drawn horizontal and vertical bars, rule B2 says an arrangement answer is drawn even when the steps describe it in words, and the steps point at cells by number. I kept it `required` (user decision 4, rules as written). The teaching image C120.IMG1 shows nearly the same row but is kept and never linked, and the id is `C120.IMG2` because IMG1 is kept.
  - Which state the single diagram shows: I drew the **complete final row** (given cells 1, 2, 5 in INK with a dashed FOCUS outline as in the book's solved example, found cells 3, 4, 6 in ANSWER green), because the worked-example figure sits before the steps and the answer is the arrangement. The alternative is the given state only (cells 3, 4, 6 blank), which would not draw the arrangement answer. If the user prefers the given-state row, change the three found cells to blank and drop the ANSWER colour; the id and placement stay the same.
- **`M4.S25.T25.C93` solution, optional rather than none.** The book does draw the method for this very activity (P15, P16), so the figure "would help"; but the steps carry all numbers and the answer is not an arrangement, so it is not required. Nothing is added either way.
- **`M3.S21.T21.C82`, none.** A bar or card picture of price per mL would be pleasant, but the book's figure is a plain table and the teaching image C82.IMG1 already shows the four sizes and the unit prices.
- **Sibling check (B2).** The five 7.5 Figure it Out items (C94, C100, C102, C104, C106) and the Examples 11 and 12 (C96, C98) all have text/number answers and are all none, as is every 7.6 Figure it Out item. No sibling is drawn.
- **P20 Binairo mapping.** Both book example grids (Puzzle and Solution) are mapped to the one worked item because its row is the one-row version of that example. The practice grids are mapped to none:OPEN_ENDED only because no LP item uses them (no code says "no LP item"); see LP text issues.

## 3. Book unclear or odd

- The book's Binairo pages (p.20) show a 6 x 6 solved example, not the one-row example the LP uses; the LP's row (H H _ _ V _ -> H H V H V V) is not printed in the book. It is unique under the book's rules (the other fill, V then H in cells 4 and 6, gives three verticals in cells 3 to 5).
- The book's answer to Figure it Out 7.6 Q4 (crane) gives only "4/10 x your height" with no number, so no figure could carry a value; the LP adds the example 150 cm -> 60 cm.
- The book's Q5 answer in 7.5 (bucket of orange paint) is "3 : 13" with the fractions 3/8 and 13/8; the LP says the same.
- The book's 7.5 Activity 3 pink circles (3 + 9, 8 + 4, 2 + 10) do not show the ratios discussed in the text (6 : 6, 5 : 7, 3 : 1); they only illustrate "different ways".
