# Class 7 Ch 7 A Tale of Three Intersecting Lines - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths7_ch7` v61 (taken from staging). Result: new V2 version v62 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (88 items from 49 units)
{"question": {"none": 32, "required": 6, "optional": 1}, "solution": {"required": 25, "none": 12, "optional": 2}, "worked_example": {"required": 4, "optional": 2, "none": 4}}

Optional, NOT added: [('C20', 'worked_example'), ('C42', 'worked_example'), ('C59', 'solution'), ('C82', 'question'), ('C96', 'solution')]

needs_lp_text_sync: [('C15', 'question'), ('C95', 'question')]

## The 35 diagrams
| id | side | type |
|---|---|---|
| M1.S3.T3.C7.IMG1 | solution | construction |
| M1.S4.T4.C9.IMG1 | worked example | construction |
| M1.S5.T5.C12.IMG1 | solution | construction |
| M1.S5.T5.C14.IMG1 | solution | geometry_figure |
| M1.S6.T6.C15.IMG1 | question | geometry_figure |
| M1.S6.T6.C16.IMG1 | solution | geometry_figure |
| M1.S6.T6.C17.IMG1 | question | geometry_figure |
| M1.S6.T6.C18.IMG1 | solution | geometry_figure |
| M1.S8.T8.C24.IMG1 | solution | construction |
| M1.S8.T8.C26.IMG1 | solution | geometry_figure |
| M1.S8.T8.C28.IMG1 | solution | construction |
| M1.S11.T11.C39.IMG1 | solution | geometry_figure |
| M2.S15.T15.C51.IMG2 | worked example | geometry_figure |
| M2.S16.T16.C55.IMG1 | solution | geometry_figure |
| M2.S17.T17.C57.IMG1 | solution | geometry_figure |
| M2.S19.T19.C63.IMG1 | solution | geometry_figure |
| M2.S20.T20.C65.IMG1 | solution | geometry_figure |
| M2.S21.T21.C66.IMG2 | worked example | geometry_figure |
| M2.S22.T22.C69.IMG1 | question | geometry_figure |
| M2.S22.T22.C70.IMG1 | solution | geometry_figure |
| M2.S25.T25.C81.IMG1 | solution | geometry_figure |
| M2.S25.T25.C83.IMG1 | solution | geometry_figure |
| M2.S26.T26.C85.IMG1 | solution | geometry_figure |
| M2.S26.T26.C88.IMG1 | question | geometry_figure |
| M2.S28.T28.C94.IMG1 | solution | geometry_figure |
| M2.S28.T28.C95.IMG1 | question | geometry_figure |
| M3.S30.T30.C101.IMG1 | question | geometry_figure |
| M3.S30.T30.C102.IMG1 | solution | geometry_figure |
| M3.S30.T30.C104.IMG1 | solution | construction |
| M3.S30.T30.C106.IMG1 | solution | geometry_figure |
| M3.S32.T32.C111.IMG1 | solution | construction |
| M3.S32.T32.C113.IMG1 | solution | construction |
| M3.S32.T32.C115.IMG1 | solution | geometry_figure |
| M3.S32.T32.C117.IMG1 | solution | geometry_figure |
| M4.S33.T33.C118.IMG2 | worked example | solid_3d |

### Chunk A notes (from the decision agent)
# Notes, chunk A (Class 7 Ch 7, topics M1.S3.T3 to M1.S13.T13)

Result: 31 items (13 pairs, 5 worked examples): required 12 (2 question, 9 solution, 1 worked example), optional 2 (worked examples, not added), none 17. Validator: errors 0, 4 warnings (required items whose figure is not printed in the book: C9, C14, C24, C28).

Figures claimed: all base figures of book pages 1-13 (P01 to P13, 22 figures) and the three printed-answer pictures of Figure it Out 7.2 on page 28 (P28-shape-1/2/3). P01, P02 and the equilateral-triangle figures of page 3 belong to teaching topics (M1.S1, M1.S2) that have no chunk, so they are claimed here; the merge should not find them unclaimed. Mapping: 10 to items, 10 to concept images (teaching figures, accounting only), 5 to none:TEXT_SUFFICIENT (intermediate construction steps and the naming/ruler-trial pictures).

## 1. Judgement calls

- **C15 question (circle with its centre): required.** The figure is trivial (a circle and a dot), but the book prints it beside the question, the learner acts on it (marks points, joins them: ACTION_ON_FIGURE), the printed answer is a picture, and sibling Q2 is required. Alternative: `none` with the LP text carrying the whole figure. Because the question text says "some points are marked on the circle" while the figure marks only the centre, the item has `needs_lp_text_sync: true` and a text_alternative.
- **C17 question: one card for both book pictures** (two circles; three circles), side by side, because the LP holds the question as one item. The solution card C18 keeps the same layout (`derived_from` C17.IMG1).
- **C14 (five triangles): one solution card with all five**, drawn to one scale, equal sides ticked, no construction arcs (arcs for five triangles would drown the figure). The triangle 1, 5, 5 is drawn with its 1 cm side as the base (the LP says "a very short base"), the other four with their longest side as the base. If the team prefers one card per triangle, this unit would need five solution ids.
- **C16 solution** shows the printed answer (circle, centre O, P, Q, OP = OQ) and also the LP's third point R halfway between P and Q (RP = RQ). The equilateral special case (PQ = radius) is only in the text.
- **C18 solution** draws segment CD as well, so the isosceles triangles ACD and BCD of the LP solution are visible. The other crossing points of the three-circle picture are not drawn or lettered (the LP names none).
- **C9 worked example (4, 4, 6): required.** Its answer is a construction and the steps lean on it ("they cross at C"). The placeholder sits after the question text as the rules demand, but the card shows the finished construction (it is the example's own picture, the steps are right below). The concept has no teaching image.
- **C20 (tent, tree, pole) and C42 (touch, miss, cross) worked examples: optional, not added.** What would help: a triangle labelled 30 m, 20 m, 25 m (C20); three pairs of circles on AB = 8 cm with radii 3 and 5, 2 and 5, 5 and 6 (C42). Both are decided by arithmetic and their concepts already hold a teaching image of the scene.
- **C24 and C28 (arcs that fall short): required**, the question asks what happens to the arcs / to verify by construction, and the answer is the failed construction itself. The part of the base that neither arc reaches (1 cm) is drawn in FOCUS. Both decisions are the same by sibling consistency. The existing concept image M1.S7.T7.C19.IMG1 shows the 8 cm case; it is not linked and C24 draws its own.
- **C26 solution (rough triangle): required** for FIG_REFERENCED: the solution talks about the paths BC, BA + AC, and so on, but A, B and C are defined nowhere in the LP text. The sketch (book Fig. 7.4) fixes AB = 15 cm, BC = 10 cm, CA = 30 cm and is `to_scale: false` (such a triangle cannot exist).
- **C38 question: none** (the book gives no figure with "picture the circles"); **C39 solution: required** (book Fig. 7.5, drawn to scale with AX = XB = 4 cm). P10-shape-1 (circle of radius 4 at A with AX and AB marked) is accounted to the concept image C35.IMG1 because the final figure of C39 already contains all its content.
- **None by rule:** C30, C32, C34, C41 (answers are sums and comparisons, the book's printed answers on pp.29-31 are text only), C36 and C43 (numeric checks and a three-step procedure; C43 has no flow-chart image to repeat), and every question that gives no figure (C6, C11, C13, C23, C25, C27, C29, C31, C33, C38, C40).
- **Colour rule used for stand-alone solution figures** (no question diagram to derive from): the base and every given length in INK, construction arcs in GUIDE, the lines, points and letters the solution adds in ANSWER, the uncovered gap in FOCUS.
- Coordinates are in px on a 1920 x 1080 canvas, and every label sits at a stated position; each figure was previewed once outside the repository to check that labels do not hit lines.

## 2. Things in the LP that look wrong or thin

- **C6 question** names AC and BC ("explain why AC and BC are both 4 cm") without saying that AB is the base and C the third corner. Added as an optional text fix (the question gets no figure).
- **C15 question** says "some points are marked on the circle", the book figure marks only the centre.
- **C14 solution** step 2 says "draw the longest side as the base", but step 3 describes (c) 1, 5, 5 as "isosceles, with a very short base".
- **C25/C26**: the question does not name A, B, C; the solution uses them (see C26 above).
- **C17/C18**: the letter C is a centre in the three-circle picture and a crossing point in the two-circle picture. This follows the LP; the figure keeps it as is.
- C20 numbers (30 m, 20 m, 25 m) are the LP's own, the book gives no lengths for the tent, tree and pole picture.

## 3. Places where the book is unclear or differs from the brief

- The brief says the pdf has no printed-solutions section, but pdf pages 28-34 are a short printed-answers section ("Page No. 150 ..."). Only page 28 holds pictures that belong to this chunk (Figure it Out 7.2 Q1 and Q2). The answers for pp.29-31 are text only.
- **Printed answer of Q2, second picture (P28-shape-3)** relabels the three circles (C at the top crossing, D at the lower crossing, which is also the third centre) while the question's picture has the centres A, B, C. The LP solution keeps the question's lettering, and so does the diagram.
- **P05-construction-1** (the 4, 5, 6 triangle, p.5) is not to scale: C is drawn slightly left of A, but it must be 0.625 cm to the right of A (and 4.961 cm above AB). The diagram uses exact coordinates.
- **Fig. 7.4** (10, 15, 30) is a sketch of an impossible triangle (the drawn sides satisfy the triangle inequality). Kept rough on purpose.
- **Fig. 7.5**: the hand-drawn overlap of the circles is wider than the true 1 cm lens (4 + 5 - 8). The diagram is to scale.
- Figure it Out 7.2 Q1 ends with "Try more" in the printed answer; the answer is open-ended, the diagram shows the single example the LP gives.

### Chunk B notes (from the decision agent)
# Notes for chunk B (Class 7 Ch 7, plan cbse_eng_maths7_ch7_v61)

Result: 30 items (16 units) -> required 10 / optional 2 / none 18. Validator: `errors 0`, 3 warnings (all expected, see 1.9).

Required (10): worked C51 (IMG2), solution C55, solution C57, solution C63, solution C65, worked C66 (IMG2), question C69, solution C70, solution C81, solution C83.
Optional, not added (2): solution C59, question C82.

## 1. Judgement calls

1.1 **Construction questions: question none, solution required (5 pairs).** 5-4-45 (C54/C55), Figure it Out SAS Q1 (C56/C57), ASA 45-5-80 (C62/C63), Figure it Out ASA Q1 (C64/C65), 60/70 on bases 5 and 7 cm (C80/C81). The book gives only measurements (no printed figure), so no question figure ("don't invent a question figure"); the built triangle is the answer, so the solution figure is required (B2, ANSWER_IS_FIGURE) and stands alone (`derived_from` null). The five are decided alike (sibling consistency).

1.2 **Three-triangle cards (C57, C65).** The LP keeps parts (a), (b), (c) in one concept, so each pair gets ONE solution diagram: three triangles in a row, left to right in the order of (a), (b), (c). The part letters (a)/(b)/(c) are not drawn (prompt section 4: no figure letters); each triangle is identified by its own given numbers. Each triangle is drawn to its own scale (stated in `scale_note`, `to_scale: false`) because three triangles on one common scale cannot keep 48 px labels legible on a 16:9 card (the 75-5-75 triangle is 9.3 cm tall, the 25-3-60 triangle is only 1.1 cm tall). Coordinates, arc radii and label centres were placed by a script and checked on a preview render (no label touches a line or another label).

1.3 **C65: the side lengths are not drawn.** The LP steps also give the other two sides (a: 9.7 and 9.7, b: 2.6 and 1.3, c: 10.4 and 6, I recomputed all of them: correct), but the LP's own figure note lists only the third angles (30, 95, 30), and six more length labels would crowd the card. If the user wants them, the spec has room only if the card is split into three. The sibling C57 does draw the third side because the LP's final answer is that side.

1.4 **Vertex letters A, B, C are drawn in every construction figure** (C55, C57, C63, C65, C81) even where the LP text of that item has no letters (C65, C81): they follow the book's construction convention (triangle ABC, base AB). In C81 the sides AC and BC carry no length (neither the question nor the LP solution gives them).

1.5 **Worked example C51 (included angle) required.** Question text is complete in words, so a strict reading could say TEXT_SUFFICIENT. I chose required because the whole example is about WHERE the 30 degree wedge sits (between the 6 cm and 5 cm sides, or at the far end of the 6 cm side) and the book itself draws this (p.15). Two-panel figure, both panels at 1.1 canvas-cm per cm; panel 1 is the book's middle triangle, panel 2 is the question's own "what if". The teaching image C51.IMG1 (4 cm, 60 degrees, 3 cm) is not linked. If the user prefers text only, flip it to `optional` (no other change needed).

1.6 **Worked example C66 (two big angles never meet) required** for the same reason: 90/90 (right-angle squares) and 100/95 (arms leaning outward) are spatial. The teaching image C66.IMG1 shows only the 90/90 case and is not linked. No vertex letters (the example's text has none).

1.7 **C69 question required, C70 solution required (derived).** The book gives this as a figure (p.17, "angle B marked in the figure"); the LP text does not say which way the arm from A leans, so the figure carries data. The arm is not named l in the question figure (the LP question never names it; the LP solution says "call the line along this arm l"), so l and m appear only in the solution figure. The book's extra fan of rays from B (p.18) is not drawn: only the limiting line m and the 140 degree angle (LP solution).

1.8 **Optional (not added):** C59 solution (SAS Math Talk: no triangle at 180 degrees or more): a picture of the two sides lying on one line would help, but the answer is a statement and the book's printed answer (p.31) has no picture. C82 question (find A from B = 50, C = 70 degrees): both angles are in the text and the learner can sketch the triangle, so the book's triangle is optional there; the solution figure (C83, line XY, alternate angles, 60 degrees) draws the whole triangle itself.

1.9 **The 3 validator warnings** (C57, C65, C81 "required but no inventory figure maps to it") are expected: the book prints no figure for those answers (no printed answer for Figure it Out SAS Q1 and ASA Q1, no figure in the 60/70 exploration), so there is no base figure to claim.

1.10 **Figure inventory mapping.** 12 base figures claimed (7 to items, 1 concept image, 4 none). Teaching figures from which an item diagram is drawn are mapped to that item, not to the concept image: P15-shape-1 (-> C51 worked), P17-shape-1 (-> C66 worked), P15-construction-3 (-> C55 solution), P16-construction-3 (-> C63 solution), P19-shape-2 (-> C83 solution). P16-construction-2 is the same finished triangle as P16-construction-3 and is mapped to the concept image C60.IMG1. P15-construction-2 (intermediate stage) is not drawn (the final state is, TEXT_SUFFICIENT); P16-shape-1 (three teaching examples whose numbers are in the C60 text) and P19-shape-1 (triangle with 50 and 70 degrees, question side optional) are TEXT_SUFFICIENT; P32-table-1 is a plain text table (LATEX_TABLE). If another chunk also claims P19-shape-2 / P19-shape-1 (angle-sum topics S24/S26) the meaning is the same: the figure becomes the solution figure of C83; the plain triangle is optional on the question side.
   Corrected base description: P15-construction-3 (see `figure_inventory`): C is above a point about 56% along AB, and AC is about 0.83 of AB in the picture (base note said 0.7 and "above the left-middle").

1.11 **Rounded values.** The LP writes "about 3.6 cm / 6.9 / 3.5 / 9.8 / 6.0 / 4.3"; the figures draw the geometry exactly and label the rounded value (exact: 3.566, 6.865, 3.518, 9.849, 6.011, 4.316).

1.12 **None items.** C45-C50 (triangle-inequality Figure it Out), C71-C76 (angle pairs) are text, LaTeX arithmetic or a plain table. Figure it Out Q3 (C49/C50) answers are ranges (99 to 101, 0 to 10, 4 to 10); a number line was considered and left as text (tie-breaker).

## 2. Things in the LP that look wrong or thin

2.1 **M2.S17.T17.C59 (Math Talk, two sides and the included angle), step 3** says that for 4 cm, 210 degrees, 6 cm "the angle on the other side is less than 180 degrees and the picture is the same as a smaller angle", yet the answer is "no triangle". Those two statements contradict each other (a reflex 210 degree angle leaves a 150 degree angle on the other side, which does make a triangle). The book's answer only says an included angle of 180 degrees or more gives no triangle. Suggest rewording to the book's statement.

2.2 **Book numbers.** The LP calls the SAS Math Talk (C58/C59) "Figure it Out, Q2"; in the book (p.16) it is a Math Talk after Figure it Out Q1. Same for C75/C76 ("Figure it Out, Q3" is an unnumbered "?" question on p.18 after Figure it Out Q2).

2.3 **C71/C72 (angles 30, 70, 54, 144).** The book's printed answer table (p.32) ends each "possible" cell with "Find the third angle in each case"; the LP question and solution drop that follow-up (and the LP's example angles differ from the book's, all valid; LP kept).

2.4 **C54/C55 and C62/C63 `book_number`** are descriptive strings ("Two Sides and the Angle: construct 5 cm, 45 and 4 cm") rather than book numbers (they are worked examples in the book, p.15 and p.16).

2.5 **Worked units C51 and C66** have no `book_number`; `lp_book_number` is null in the map.

## 3. Where the book itself is unclear

3.1 P17-shape-2 (p.17): the text says "angle B (marked in the figure)" but nothing is marked at B in that figure; the arc at B appears only in the next figure (p.18).

3.2 The book's small ASA picture on p.16 (P16-construction-2) is flatter than the stated angles (the angle at A looks about 34 degrees, not 45); the figure drawn here is to scale.

3.3 The book has no printed solutions for the two construction Figure it Outs (SAS Q1 p.16, ASA Q1 p.17), nor for the 60 and 70 degree exploration; the third sides and angles were recomputed (cosine rule, sine rule) and agree with the LP everywhere.

3.4 Page 31's printed answer to the SAS Math Talk says "greater than or equal to 180 degrees"; the LP adds 0 degrees (arm on top of the base). Both fine.

## 4. Working files (outside HERE)

Generator and preview renders are in the session scratchpad `.../scratchpad/c7ch7_B_v2/` (`build_out.py`, `figs.py`, `geo.py`, `prev/*.png`); nothing else was written under HERE except `map/out_B.json` and this file.

### Chunk C notes (from the decision agent)
# Notes for chunk C (Class 7 Ch 7, v61): M2.S26.T26, M2.S28.T28, M3.S30.T30, M3.S31.T31, M3.S32.T32, M4.S33.T33

Result: 27 items, required 13 / optional 1 / none 13. Validator: errors 0, 4 warnings (T32 solutions C111, C113, C115, C117 are required but the book prints no figure for them; this is expected, the figure is the finished construction the LP describes).

## 1. Judgement calls I was unsure about

| Item | Choice | Why / what to check |
|---|---|---|
| M2.S26.T26.C85 (FiO Q1 solution) | required, figure for part (a) only | The book's printed answer is a picture (page 33, 'Process for (a) is given'). The LP solution covers (a) to (d) but one pair gets one solution figure; (b) to (d) have numeric answers only in the book. If you want the figure to say it is part (a), that is a text-sync matter, not a drawing one. Question side is `none`: the book page 20 gives no figure with Q1. |
| M2.S26.T26.C89 (FiO Q3 solution) | none (SAME_AS_QUESTION_DIAGRAM + TEXT_SUFFICIENT) | Numeric answer (65° each). The printed-answers page only repeats the question figure and prints the answer as text. Question side is required (the book gives the triangle with 50° and the equal-angle arcs). |
| M2.S28.T28.C96 (exterior angle solution) | optional (not added) | Figure-based question, numeric answer (Step E: Q required, S none). A labelled figure with A 50°, B 60°, angle ACB 70°, angle ACD 110° would help the 'what do you notice' step, but every value is in the LP steps. The teaching image C91 already shows this. Upgrade to required only if you want it. |
| M2.S28.T28.C95 (exterior angle question) | required | The LP question names angle ACD but never says D lies on BC extended beyond C; the book's figure carries that and marks the exterior angle. Drawn to scale for the first case (50°, 60°, 70°), no numbers printed, so the second case (35°, 45°) uses the same labelled figure and is not to scale. `needs_lp_text_sync` is set: the question text should say 'BC is extended to D' (optional). |
| M2.S28.T28.C94 (angle sum proof solution) | required | The proof is the figure (line XY through A parallel to BC, equal alternate angles). Redrawn from Fig. 7.7 with SET_A / SET_B / MARK_FILL plus one / two / three arcs so the equal pairs can be told apart without colour. No numbers. The question side is `none`: the prompt gives no figure. |
| Paper-fold picture (P21-paper_fold-2) and the paper-fold step of C94 and C102 | not drawn (`none:TEXT_SUFFICIENT`) | One solution figure per pair, and the parallel-line figure is the proof. The fold is a physical activity the LP describes in words; a fold-sequence figure would be a second diagram. Say if you want it added as a second image later. |
| M3.S30.T30.C101 (obtuse altitude question) | required | The book gives this triangle ('What would the altitude from A to BC be in this triangle?'), the student acts on it, and the position of A relative to B is what puts the foot outside. |
| M3.S30.T30.C105 (right-angle question) | none, but C106 solution required | Sibling difference on purpose: for C101 the book GIVES a triangle; for C105 the book's right triangle (page 169) is the printed answer to 'Visualise such a triangle and draw a rough diagram', not a given figure, and the LP question already says 'right angle at B'. The solution draws the right triangle with AB and BC highlighted and the third altitude inside. |
| M3.S30.T30.C104 (set square solution) | required, type `construction` | Final state of the book's Steps 1 to 3 (page 169): ruler, set square at A, altitude AD with the right angle at D. Ruler and set square are plain GUIDE outlines, not the book's teal clip-art. Step 1's picture is an intermediate state: `none:TEXT_SUFFICIENT`. |
| M3.S32.T32.C111, C113, C115, C117 (constructions) | all four solutions required, all four questions none | Same answer type (a construction), so the same decision. The questions give no figure. The solution figure is the finished construction. C111 shows the two compass arcs in GUIDE because the LP solution names them; C113 shows both 140° and the outside 40°. |
| M3.S32.T32.C115 | the three vertices are named B1, B2, B3 | The LP uses 'B' for every triangle. Three triangles on one base need three names; the LP text does not use B1 to B3. 1 cm is drawn as 2 units so the nine angle labels do not collide. Triangles are drawn in SET_A, SET_B and ANSWER so each arc and label can be matched to its triangle. |
| M3.S32.T32.C117 | no vertex letters, hypotenuse and base unlabelled | The LP names no vertices for these two triangles, and gives no length for the slanting side (4 x sqrt 2 = 5.66 cm) or the base (8.66 cm). Not inventing numbers. |
| M3.S31.T31.C107, C108 (worked examples) | none | All numbers are in the question text and the answers are names, so a picture would only show the answer. The existing teaching images stay. |
| M4.S33.T33.C118 (spider worked example) | required, media id `C118.IMG2` (IMG1 is the kept teaching image) | The book gives the box with the spider's corner and the marked far corner; the LP adds 6, 4 and 3 cm. The picture is the closed box in oblique projection with 'start' and 'end' opposite corners and the three lengths; no path (that would give the answer). The two-faces-laid-flat picture is the teaching image C118.IMG1 and is not linked. |

Figures I claimed that are not in a unit's own section: P22-shape-2 (Fig. 7.8) and P23-shape-1 (altitudes BE and CF) sit in book section 7.4 next to my T30 units but belong to the teaching topic M3.S29 (no unit). I claimed them so the merged coverage check can close: P22-shape-2 -> concept image M3.S29.T29.C97.IMG1; P23-shape-1 -> `none:TEXT_SUFFICIENT` (no question uses it, no concept image shows it). The base entry P23-shape-2 holds two drawings: the left one is the T30.C101 question figure, the right one is a second entry `NEW-P23-shape-2-sol` for the C102 solution.

All geometry in the specs was computed and asserted in a script (angles, lengths, perpendicularity, label positions): e.g. FiO Q1(a) A=(8.09,5.88) gives 36°, 72°, 72°; Q3 apex 50° gives 65° base angles; T32 Q1 AD = 4.8 exactly (BD 3.6, DC 1.4); T32 Q2 TD = 7 sin 40° = 4.4995 (LP says about 4.5); T32 Q3 right angles at B1, B2, B3 verified; box edges and opposite corners verified.

## 2. Things in the LP that look wrong or thin

- M2.S28.T28.C95 (question): 'Find angle ACD, if angle A = 50° and angle B = 60°' does not say where D is. Everything else is correct (110°, then 80°, exterior angle = sum of the two opposite angles).
- M2.S26.T26 and M3.S32.T32 both have the book number 'Figure it Out, Q1' ... Q4 (two different Figure it Out sets); the mapping to the book is by text and is right (angle-sum set on page 165, types-of-triangles set on pages 170 to 171).
- The `q_figure` hints on C101 and C105 and the `s_figure` hints are consistent with the book, except that C105's hint describes a figure the book does not give with the question (see the table).
- M3.S30.T30.C102 step 5 (paper fold) and M2.S28.T28.C94 step 5 are text only; consistent with the book's 'Altitudes Using Paper Folding' and fold picture, no contradiction.
- M3.S32.T32.C115: LP steps say 'the arms cross at B' for each choice; with three triangles on one base the figure needs three names (B1 to B3), so the LP text and the figure use different labels. Optional text sync.
- M4.S33.T33.C118: the book's puzzle gives no sizes; the LP's 6 x 4 x 3 box is its own. The LP numbers check out: diagonals sqrt(36+49)=9.22, sqrt(16+81)=9.85, sqrt(9+100)=10.44; edges 6+4+3=13.

## 3. Where the book itself is unclear

- The pdf has partial printed answers on pages 28 to 34 (book pages 150 to 165), although the run brief says it has none. They cover the first angle-sum Figure it Out (my T26) on pages 33 and 34; there are no printed answers for the Altitudes questions or for the types-of-triangles Figure it Out.
- Page 33: the printed answer for Q1(a) draws line XY with arrowheads at both ends (the chapter's own Fig. 7.6 and 7.7 draw dots at X and Y). The spec follows the printed-answer picture (arrowheads, no dots) because that is what this figure replaces; the proof figure of T28 (C94) uses dots at X and Y as Fig. 7.7 does.
- Page 23: the book's right-hand drawing (altitude outside) has no right-angle mark at D; the LP solution says 'the foot D', so I add the mark.
- Page 27: the box in the Puzzle Time picture is open at the front and carries no dimensions; the spec uses a closed wireframe box with the LP's dimensions.
- Page 24: the book calls the third altitude nothing; the LP does not name the foot of the altitude from B, so it has no letter in C106.
