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
