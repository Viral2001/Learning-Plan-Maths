# Chunk C notes (Class 6 Ch 2 "Lines and Angles", units 37-51)

Result: 28 items, required 14 (questions 6, solutions 6, worked examples 2), optional 2, none 12. Validator: errors 0, warnings 0.
Output: `map/out_C.json`. All coordinates in the specs are card units on a 16 x 9 card (origin bottom-left, y up). Every pair shares one layout between its question and solution diagram. All diagrams are 16:9 (the rotated protractor is tall, but it is centred and the solution writes its values to the right).

## 1. Judgement calls

| Item | Choice | Why |
|---|---|---|
| C66 (straight angle, fold) | none | The LP text names the straight angle AOB and ray OC; nothing is lost without the picture. |
| C67 (its answer) | **optional** (not added) | A picture of the opened sheet with crease OC and two equal angles would help, but the steps and answer are complete in text, and the teaching image M2.S12.T12.C62.IMG1 already shows the idea (and may not be linked). |
| C77 (slanting crease + perpendicular crease, answer) | **optional** (not added) | Same kind of answer as C67 (a paper-fold result), so the same decision. A figure with the two creases and four right-angle marks would help; the answer "four right angles, each 1/4 turn" is complete in text and part (b) is open-ended. |
| C68/C69, C70/C71, C76, C82, C84/C85 | none | No given figure (open-ended / observation / why-question) or one-line answers. |
| C72/C73 (dot grids, straight angle) | required / required | Both grids exist only in the picture; the answer is the set of dots (3 left, 2 right) and a line. One card holds both grids (a pair gets one question diagram). |
| C74/C75 (dot grids, right angle) | required / required | Question card has THREE grids: the two question grids plus the printed Hint grid (C, A, B on one diagonal), because the question text names point C only in that hint picture. The solution leaves the hint grid unchanged, adds the perpendicular line, the 5 + 4 answer dots and a right-angle mark at A in each question grid. |
| C78 worked example (classification box) | required (`add_new_image`, id C78.IMG2) | The example refers to "three groups as shown"; the box of 17 angles is the book figure. The teaching image C78.IMG1 is a different picture (three single angles) and is not linked. |
| C80 (identify angle types in the previous figures) | required, same spec as C78.IMG2 | "The previous figures" = the box on the same book page (printed right above this question). Straight angles are NOT in the box (see section 2). |
| C81 | none | The answer names the group of each angle; a picture would only repeat C80's. |
| C83 (printed answer: sample acute/obtuse angles) | required, `derived_from` null | Printed answer is a picture (5 acute + 4 obtuse); the question gives no figure, so the solution draws the whole thing. Openings measured by eye from the printed picture (+-2 degrees). |
| C86/C87 (acute angles in triangle figures) | required / required | C86: the three given figures. C87: "what will be the next figure" is part of the answer, so the 4th figure (10 small triangles) is drawn in ANSWER green with the counts 3, 12, 21, 30 under the four figures. The question card deliberately leaves slot 4 empty so nothing moves between question and solution. The 4th figure is not printed in the book: it is built by the book's own rule (the small central triangle is cut by joining its side midpoints), which gives 1, 4, 7, 10 triangles. |
| C91/C92 (180 and 90 degrees) | none / none | The words and the arithmetic (360/2, 180/2) carry everything. The LP hints (`q_figure`, `s_figure`) describe the book's fan pictures, but those are the teaching figures of topic M3.S17.T17 (concept image C88.IMG1). |
| C93/C94 (ten cut circles) | required / required | Question: the circles with one small arc each. Solution: the measure under each circle (360, 180, 120, 90, 72, 60, 45, 40, 36, 30). Placed under the circles because a 30 or 36 degree sector cannot hold the number inside. |
| C95 worked example (two scales on a protractor) | required (`add_new_image`, id C95.IMG2) | The question is about the printed numbers on the protractor. The teaching image C95.IMG1 (two coloured scales) stays in the concept and is not linked, so the example gets its own plain drawing like the book (38 numbers, 181 ticks, 17 fan lines). |
| C99/C100 (read KAL, WAL, TAK) | required / required | The sideways protractor with rays K, L, W, T exists only in the picture. Ray bearings 40, 10, -40, -80 degrees (measured from the page, rounded to the long ticks) so that 30, 50 and 120 hold exactly. The solution adds three arcs inside the white centre cut-out and the three values as a short list at the right (the busy scale rings leave no room for labels). |

Other points:
- Sibling consistency: both paper-fold answers (C67, C77) are optional; the three "mark dots/numbers on the given figure" pairs (C73/C75, C94, C100) are all required; the two "number-only" answers (C69, C92) and the "named groups" answer (C81) are none.
- Figure inventory: a figure used by two items is two entries (base id first, `NEW-<base id>-<suffix>` second). The solution diagrams that redraw the question figure got `NEW-...-sol` entries; C80 re-uses the box as `NEW-P19-angle_set-1-fio`.
- Teaching figures claimed here for accounting only (other chunks may claim the same base ids, so please compare at merge): P16-angle_set-1 and P16-paper_fold-2 -> concept_image C62.IMG1; P21-straight_angle-2, P21-angle_fan-3, P21-right_angle-4, P21-angle_fan-5 -> concept_image C88.IMG1; P24-protractor-2 -> C96.IMG1; P25-protractor-1 -> C97.IMG1; P20-circle-2, P20-protractor-3, P21-angle_fan-1, P23-protractor-1 -> `none:TEXT_SUFFICIENT` (teaching figures with no concept image, used by no question or answer).
- The set squares with speech bubbles on pdf p.17 are decoration and have no inventory entry (as in the base).
- I checked every base description of my figures against the page pictures: all correct (the p.19 box counts 6 + 5 + 6, circle counts, grid positions, protractor facts). Only the SOL48 opening sizes differ slightly from the base (measured 60/57/60/58/23 and 128/146/111/135 degrees instead of 60/60/60/60/22 and 130/148/113/135); noted in those entries.

## 2. Things in the LP that look wrong or need a text sync

1. Figure descriptions are written into the question text. Once the picture follows the question text they are duplicates and should be removed from `question_tex` (and from the copy of the question inside the solution concept): C72/C73 and C74/C75 ("(Two dot grids of 7 columns by 6 rows. Left grid: A at row 3, column 4 ...)" and the trailing "left grid) Join A so that AB ..."), C86/C87 ("(Figures: (i) one triangle; ...)" and the trailing "i) Acute angles in the first figure ..."), C78 ("(a box with three columns of angle drawings)"), C99/C100 ("a) ∠KAL b) ∠WAL c) ∠TAK" repeated at the end).
2. C74/C75 text says "(Same two grids as $Q_2$.)": it points at another question by number; with the new card it should simply be dropped.
3. C76/C77: "(a) How many right angles? Justify. (b) Describe how you folded the paper." is written twice in the question text.
4. C80/C81: the LP answer says "Straight angles appear in Fig. 2.11 and the folded-paper figures", but the question figure (the box) has no straight angle, and the book prints no answer for this question. The learner has to look back at the earlier straight-angle topic (M2.S12.T12) for those. The question text only says "in the previous figures": consider naming the box ("in the three groups of angles above").
5. Book numbers: `Figure it Out 2.8, Q1` is used for two different questions (C70 on book p.29 and C80 on book p.31); the book restarts the numbering in each Figure it Out set. Several T13/T18 items carry descriptive strings instead of book numbers.
6. The printed solutions (pdf pp.43-53) have no printed answer for: 2.8 Figure it Out set 1 Q1, Q2, Q3; set 2 Q1; 2.9 question on the straight/right angle measures and the circle question. The LP answers there are the LP's own. I re-derived them from the pictures: C73 left 3 dots (columns 1-3), right 2 dots; C75 left 5 dots (2 above + 3 below), right 4 dots; C87 gives 3, 12, 21, 30 (matches the book's "thirty" for the next figure and the 3n+1 pattern); C94 360/n for each circle; C100 30, 50, 120 (matches the book's printed answer).
7. C99: the LP question text carries the book's worked part ("∠KAL = 30°") and the follow-up about counting in 5s and 10s, so part (a) is given away in the text, as in the book; the question figure itself shows no values.

## 3. Where the book itself is unclear

- p.19 box: the three groups are not labelled and no angle sizes are printed; the openings in the spec (41, 26, 86, 73, 37, 10 / five exact right angles / 151, 122, 118, 149, 99, 143) were measured from the page picture (+-2 degrees). The left-column angle of 86 degrees and the right-column angle of 99 degrees are close to a right angle in the book too; kept as printed.
- p.18 Q3: the two grids are the same as in Q2 and the hint grid is a third picture; the printed solutions give no answer, so "all the different ways" is the LP's count (every grid dot on the line, either side of A).
- p.20: the 4th triangle figure is not printed (see above).
- p.22: the small marking arcs of circles 6 to 10 are tiny; read from the picture as: circle 6 top sector (60 to 120), circles 7 to 10 the second sector above the horizontal (45-90, 40-80, 36-72, 30-60). The sector width (and so the answer) is the same wherever the arc sits.
- p.23: the sideways protractor is unlabelled; which end carries 0 follows the book's text ("the rightmost point of the base" when the protractor stands upright), which puts 0 at the bottom end of the left edge. The four rays were measured at about 40, 10, -40 and -80 degrees from the horizontal.
- Solutions p.48: the printed sample angles have no measures; the spec uses rounded measured values.
