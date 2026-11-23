# Class 8 Ch 4 Quadrilaterals - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths8_ch4` v29 (taken from staging). Result: new V2 version v30 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (81 items from 46 units)
{"worked_example": {"required": 7, "none": 2, "optional": 2}, "question": {"none": 26, "required": 9}, "solution": {"required": 31, "none": 4}}

Optional, NOT added: [('C103', 'worked_example'), ('C110', 'worked_example')]

needs_lp_text_sync: [('C12', 'solution')]

## The 47 diagrams
| id | side | type |
|---|---|---|
| M2.S2.T2.C3.IMG2 | worked example | geometry_figure |
| M2.S2.T2.C5.IMG2 | worked example | geometry_figure |
| M2.S3.T3.C8.IMG1 | solution | geometry_figure |
| M2.S3.T3.C10.IMG1 | solution | geometry_figure |
| M2.S3.T3.C12.IMG1 | solution | construction |
| M2.S4.T4.C14.IMG1 | solution | geometry_figure |
| M2.S6.T6.C19.IMG1 | solution | geometry_figure |
| M2.S6.T6.C21.IMG1 | solution | geometry_figure |
| M2.S6.T6.C22.IMG1 | question | geometry_figure |
| M2.S6.T6.C23.IMG1 | solution | geometry_figure |
| M2.S7.T7.C25.IMG1 | solution | geometry_figure |
| M2.S7.T7.C26.IMG1 | question | geometry_figure |
| M2.S7.T7.C27.IMG1 | solution | geometry_figure |
| M2.S9.T9.C32.IMG1 | question | geometry_figure |
| M2.S9.T9.C35.IMG1 | solution | construction |
| M2.S9.T9.C36.IMG1 | question | geometry_figure |
| M2.S9.T9.C37.IMG1 | solution | geometry_figure |
| M2.S9.T9.C39.IMG1 | solution | geometry_figure |
| M2.S10.T10.C41.IMG1 | solution | construction |
| M2.S10.T10.C42.IMG1 | question | geometry_figure |
| M2.S10.T10.C43.IMG1 | solution | geometry_figure |
| M3.S12.T12.C49.IMG1 | question | geometry_figure |
| M3.S12.T12.C50.IMG1 | solution | geometry_figure |
| M4.S14.T14.C56.IMG1 | solution | construction |
| M4.S14.T14.C58.IMG1 | solution | geometry_figure |
| M4.S14.T14.C60.IMG1 | solution | geometry_figure |
| M4.S14.T14.C62.IMG1 | solution | geometry_figure |
| M4.S15.T15.C63.IMG2 | worked example | geometry_figure |
| M4.S16.T16.C66.IMG1 | solution | construction |
| M4.S17.T17.C69.IMG2 | worked example | geometry_figure |
| M4.S18.T18.C72.IMG1 | solution | construction |
| M4.S18.T18.C74.IMG1 | solution | geometry_figure |
| M4.S18.T18.C75.IMG1 | question | geometry_figure |
| M4.S18.T18.C76.IMG1 | solution | geometry_figure |
| M4.S19.T19.C78.IMG1 | solution | construction |
| M5.S21.T21.C84.IMG1 | solution | geometry_figure |
| M5.S21.T21.C86.IMG1 | solution | geometry_figure |
| M5.S21.T21.C88.IMG1 | solution | geometry_figure |
| M5.S21.T21.C90.IMG1 | solution | geometry_figure |
| M5.S23.T23.C93.IMG1 | question | geometry_figure |
| M5.S23.T23.C94.IMG1 | solution | geometry_figure |
| M5.S23.T23.C96.IMG1 | solution | construction |
| M5.S24.T24.C97.IMG2 | worked example | geometry_figure |
| M5.S24.T24.C98.IMG2 | worked example | geometry_figure |
| M5.S25.T25.C100.IMG1 | question | geometry_figure |
| M5.S25.T25.C101.IMG1 | solution | geometry_figure |
| M5.S26.T26.C104.IMG2 | worked example | other |

### Chunk A notes (from the decision agent)
# Chunk A notes - Class 8 Ch 4 "Quadrilaterals" (plan cbse_eng_maths8_ch4_v29)

Result: 32 items (17 units). Required 21 / optional 0 / none 11.
By role: question 5 required / 10 none; solution 14 required / 1 none; worked example 2 required / 0 none.
Validator: `errors 0`, 3 warnings (required items with no printed book figure: C25, C35, C37; see below).
Every required diagram was also drawn from its own coordinates into a throw-away preview (outside HERE) to check label collisions, arc positions and every angle / length claimed in `accuracy_checks` (all asserted in code).

## 1. Judgement calls

Rule of thumb used for the question side: a question picture only where the book gives a figure WITH the question (inventory `shown_as: given in question`: FiO Q1 rectangles, FiO3 Q5, FiO3 Q7, the four quadrilaterals, the square with its diagonal). Proofs, constructions and "how do we" questions with no given figure get no question picture; the solution gets a picture where its answer is a figure or where the proof is about triangles / transversal angles that must be seen (SPATIAL_GEOMETRY).

- **Worked example M2.S2.T2.C3** (rectangle, AC = 8 cm): required, shows only what is given (rectangle ABCD, both diagonals crossing at O, AC = 8 cm). Layout from book Fig. 2; the letter O comes from the LP text. media id C3.IMG2 because C3.IMG1 is the kept teaching image.
- **Worked example M2.S2.T2.C5** (40 degrees): required, only the given: two equal diagonals (ticks), top angle 40 degrees, ends joined, letters A-D and O as in the book's x-figure. Diagonal length 8 is a drawing choice, not printed.
- **C7/C8 carpenter**: question none, solution required. The question has no figure of its own (book Fig. 1 / Fig. 2 are lesson figures that already draw the strips as diagonals, which is step 1 of the solution). Solution = book Deduction 1 figure (triangles ADC and DAB shaded SET_A / SET_B, right angles, equal sides, common side, both diagonals 8 cm).
- **C9/C10 (60 degrees)**: question none, solution required: the printed answer is the figure with all angles filled in (book p.5). Corner values 60 / 30 and the four angles at O, right-angle squares at the four corners.
- **C11/C12 (draw with diagonals 8 cm)**: question none (drawing task, no figure in the book). Solution required: the book prints the construction for case (i), 30 degrees, only. I drew exactly that case with the LP's lettering (AC first, then B and D on the 30 degree line) and set `needs_lp_text_sync` (the LP text does not say which case is shown).
- **C13/C14 (sticks and thread)**: question none, solution required (printed answer picture). Only O is lettered (the LP steps name no stick ends); the thread is drawn round all four ends and all four corners carry a right-angle mark (LP: "each corner"), the book marks only one corner.
- **C18/C19, C20/C21 (proofs)**: question none, solution required (shaded triangles BAD / DCB with BD common; transversal AD with two 90 degree angles and the parallel marks). The questions would only show a plain rectangle, which presupposes the conclusion.
- **C22/C23 (FiO Q1)**: both required. The figure holds both rectangles side by side in one card with captions (i) and (ii) (the LP answer refers to them as (i) and (ii)). O is printed on both rectangles because the LP question text names O (the book prints O only on the answers page, and only for (ii)). Solution is derived from the question diagram and marks every corner and O angle of both rectangles.
- **C24/C25 (definition)**: question none; solution required: the counterexample is a drawing (slanted parallelogram, angles 60, 120, 60, 120; the LP gives the angles as data for a picture, rule B2). Side ratio 6 : 3 is a drawing choice and is not printed; no letters.
- **C26/C27 (PAIR and RODS)**: both required, to_scale false. RI is not given anywhere and the book says "figures shown are merely indicative"; RI = 7 (not printed) reproduces the book picture (O about one unit below A, D slightly below line RI).
- **C32/C33 (four quadrilaterals)**: question required (book gives the figures; LP restates the lengths in words), solution none (SAME_AS_QUESTION_DIAGRAM: it would only repeat the figures with the words rectangle / square). No (i)-(iv) captions, because the LP text names the figures by their sides. All four share one scale; tilts re-measured on the page: 10 degrees clockwise, 5, 19 degrees anticlockwise, 0 (the base inventory said 3-4 degrees for (ii)).
- **C34/C35 (square with diagonal 8 cm)**: question none; solution required (the answer is a construction); the book prints no picture for this in-chapter task, so the figure follows the LP steps (diagonal AC, perpendicular through O, B and D at 4 cm, four "4 cm" labels).
- **C36/C37**: question required (book p.12 figure, reduced to the two angles the LP asks: DAC and DCA, each an arc with "?"). Solution derived: "?" becomes 45 degrees in ANSWER green. I did not mark the other two halves (CAB, ACB) because the LP asks only for DAC and DCA.
- **C38/C39 (circle, APML)**: question none, solution required. The base inventory lists the circle picture (P32-shape-1) as "given in question"; the question page (p.13, Q3) has no figure, the picture sits on the answers page with APML already joined, so it is the answer's picture (entry marked CORRECTED).
- **C40/C41 (square, diagonal 6 cm)**: question none; solution required (printed construction). The LP steps say arcs from A and B with the compass open "more than 3 cm", then a 3 cm arc from O; the book's picture has the arcs crossing exactly at C and D. The figure follows the LP: arcs of radius 4.5 (not printed) from A and B cross at distance 3.354 from O, then 3 cm arcs from O mark C and D.
- **C42/C43 (square in a square)**: both required. One 16:9 card holds both book figures (a) and (b); no (a)/(b) captions because the LP answer text does not refer to them by letter. The vertices of (b) are 1.1 along a 5-unit side (0.22, estimated from the page, flagged by the inventory), always in the same direction round. Solution: four corner triangles shaded MARK_FILL in both squares, ticks, eight 45 degree angles and the right angles at the midpoints of (a), equal-distance bars on (b).
- Page 1 (five chapter-opening figures, topic M1.S1.T1) belongs to no chunk, so chunk A accounts for them (concept image M1.S1.T1.C1.IMG1). Whoever merges: if another chunk also claims them, give them the same meaning.
- Answers-page reprints (P31-shape-1/2, P36-shape-1, P37-shape-1/2) are mapped to the solution item built on them, because the printed answer is a list of values under the same picture.

## 2. LP text issues

- **M2.S3.T3.C11** (question_tex and text): stray colons: "(i) $30^\circ$ (ii): $40^\circ$ (iii): $90^\circ$ (iv): $140^\circ$". Suggested: "... intersect at an angle of (i) $30^\circ$ (ii) $40^\circ$ (iii) $90^\circ$ (iv) $140^\circ$." (the plain `question` field is right).
- **M2.S3.T3.C12**: the steps are written for all four angles but the only picture is for 30 degrees. Suggested extra sentence at the end of step 1: "The figure shows case (i), 30 degrees; (ii), (iii) and (iv) are drawn the same way."
- **M2.S3.T3.C10**: step 1 uses "the four angles at $O$" and triangles AOB, AOD without ever saying that the diagonals AC and BD meet at O (the question does not name O either). Suggested: start step 1 with "The diagonals $AC$ and $BD$ meet at $O$."
- **M2.S6.T6.C23**: the angle list and the steps leave out angle DBC = 60 degrees in rectangle (i) (the book's printed answer leaves it out as well). The figure marks it (90 - 30). Suggested: add "$\angle DBC = 60$" after "$\angle ACB = 60$" in step 3.
- **M2.S10.T10.C42**: the question text drops the book's "as shown in Figure (b)", yet the question picture carries the book's two figures. Suggested ending: "... lie on the sides of the outer square, as in the second square of the picture."
- **M2.S2.T2.C5** (worked example): the text names no vertices, the figure carries A, B, C, D and O (as the book's x-figure does); only O is used by the steps. Harmless, but the letters A-D could be dropped from the spec if the text is kept as it is.
- **LP numbering**: `book_number` restarts per topic ("Figure it Out, Q1" is book FiO Q4 for C13, Q5 for C24; Q1/Q2 in topics T10 are FiO3 Q6 / Q7; C26 is FiO3 Q5). The `ncert_refs` carry the true numbers (FiO1.q4, FiO1.q5, FiO3.q5, FiO3.q6, FiO3.q7), so nothing was changed.

## 3. Borderline

- **C7 (carpenter), C9 (60 degrees), C18, C20 questions: none.** The book's text points to a lesson figure for each ("as shown in Fig. 1", "as shown in the figure to the right", "Join BD", the plain rectangle of p.9) but the LP question is self-contained and the picture would either give away step 1 (C7, C18) or only repeat the words (C9, C20). If the content team wants a question picture for these, the figures to use are book Fig. 1 / Fig. 2 (C7), the p.4 figure with 60 degrees marked (C9), the p.8 rectangle with four right-angle marks (C18), the p.9 rectangle (C20).
- **C3 and C5 worked examples: required.** Each question picture is simple (rectangle with O and 8 cm; two diagonals with 40 degrees); required because the steps refer to triangles and angles at O that the learner must see.
- **C24/C25 solution: required.** The counterexample is a drawing but the book prints no picture for it (its text answer is only "No").
- **C32 question required, C33 solution none.** The LP text carries all four size pairs, but the book question is "in the quadrilaterals below"; the solution would only add the words rectangle and square.
- **C34/C35, C40/C41 solutions: required** although C34 has no printed picture (construction answers).
- **C37 marks only the two angles asked** (DAC, DCA), not all four halves of the right angles.

## 4. Places where the book is unclear or the base inventory was off

- The brief says the pdf has no printed-solutions section; pages 31-39 do (answers to the Figure it Out sets). Used for the answer pictures; the LP solution text still wins.
- P32-shape-1 (circle with APML): answer picture, not a question figure (corrected in the inventory entry).
- P09-shape-3 (figure (ii) of the four quadrilaterals): turn is about 5 degrees anticlockwise, not 3-4 (re-measured); the sizes on the page are to scale (about 47 px per cm for all four).
- P31-shape-2: the figure marks 110 degrees at the top (QOR) while the printed answer lists POS = 110 degrees; they are vertically opposite and equal, no conflict.
- FiO3 Q5 (P26-shape-3 / P36-shape-1): RI is never given; O sits "a short way below A" (about 1 unit when PR = 5). Drawing choice RI = 7, not printed.
- FiO1 Q2 answer (P31-construction-3): the book names the first diagonal AB with C, D on the line and the figure ADBC; the LP names AC first with B, D on the line and the figure ABCD. The picture follows the LP letters.
- FiO3 Q6 answer (P36-construction-1): the 3 cm lengths are not printed and the arcs cross exactly at C and D; the figure follows the LP's two-arc description (see C40/C41 above).
- FiO3 Q7 (P27-shape-2, P37-shape-2): the 0.22 position of the inner square's vertices is an estimate from the page picture; no value is printed. The printed answer (p.37) labels the angles of figure (a) 1-8 and leaves the outer angles at X unnumbered; the solution figure marks all eight 45 degree angles.
- The printed answer text on p.37 has the typo "UXWN is square" for UXWV; no diagram prints it, so no value or label changed.
- Book print slips that change a value: none found in this chunk.

### Chunk B notes (from the decision agent)
# Chunk B notes (Class 8 Ch 4 Quadrilaterals, cbse_eng_maths8_ch4_v29)

Units: 14 (3 worked examples, 11 question/answer pairs) = 25 items. Result: required 12, optional 2, none 11. Validator: errors 0, one warning (below).

Required diagrams (media ids): C49.IMG1 (question) and C50.IMG1 (solution) of M3.S12.T12; M4.S14.T14 C56, C58, C60, C62 (solutions); M4.S16.T16.C66 (solution); M4.S18.T18 C72, C74 (solutions) and C75.IMG1 (question) with C76.IMG1 (solution); M4.S19.T19.C78 (solution). Every solution whose question has a diagram is `derived_from` it (C50 from C49, C76 from C75); the others stand alone because the question gives no figure.

Validator warning (accepted): M4.S18.T18.C76 solution has no inventory figure mapped to it. The book's printed answers to FiO Q1 are text lines beside a repeated copy of the question figures (P33-shape-1 to 4, mapped `none:SAME_AS_QUESTION_DIAGRAM`); the final state with all angles marked is not printed anywhere.

## 1. Judgement calls

- **Questions with no printed figure get no question diagram** (C47, C55, C57, C59, C61, C65, C71, C73, C77): the question gives its data in words; companion note: do not invent a question figure. For the construction questions (C55, C65, C71, C77) and the angle/side deductions (C57, C59, C73) the figure appears only on the solution side.
- **Construction answers are required** (C56, C66, C72, C78): the answer is a drawing (B2, ANSWER_IS_FIGURE); for C66 and C78 the book's printed answer is a picture as well. Colours: given measures and the skeleton in INK, the finished sides and the points the solution adds in ANSWER, construction extensions/compass arcs in GUIDE.
- **Angle/side deductions are required on the solution side** (C58, C60, C74): the LP steps argue with parallel sides, transversals, a diagonal and equal-angle arcs, and the book answers each deduction with a filled picture (P17-shape-2 for C58, P17-shape-1 filled with 4 cm and 5 cm for C60, P19-shape-3 for C74). Without the figure the steps cannot be followed. C60 uses single arcs for the opposite angles A and C and double arcs for the alternate angles ADB and CBD, like the book's Deduction 7 figure (no colour fills, no 'Common Side' words).
- **C58 shows no side lengths** although the book's picture has 4 cm and 5 cm: the LP question only gives angle A.
- **C74 adds the 130 degree labels at B and D** (outer arcs over the two 65 degree arcs); the book's picture marks only 50 and 65, but the LP answer is 50, 130, 50, 130. The 130 labels sit on the diagonal on a BG rectangle just outside the outer arcs.
- **C62 (Q9)**: the LP solution uses diagonal BD and ticks AB = CD, AD = CB; the book's printed answer uses diagonal AC and numbered angles 1 to 4. The LP is followed; no numbers are drawn. The arrowheads (parallel marks) in ANSWER green show the conclusion.
- **C50 (Q10 answer)**: the book numbers the six triangle angles 1 to 6; the LP solution never uses those numbers, so the spec draws BD and the equal small arcs without numbers.
- **C75/C76**: one question card gets one diagram, so the four given figures are one picture with four panels, letters (i) to (iv) shown because the LP text refers to the figures by those letters (decision 3). In (iii) and (iv) the added half of the bisected angle is drawn with an equal arc and no label, and the whole angle is labelled on the diagonal.
- **Orientation/labels follow the LP, not the book's printed answers**: C66 (book names the figure ACBD, LP has diagonals AC = 7 and BD = 5), C78 (book ADBC), C62. In C66 the LP does not say which of B, D lies on the 140 degree arm; D is placed on the arm that makes 140 degrees with OC.
- **Figure accounting choices**: teaching figures are mapped to the nearest existing concept image (accounting only, nothing linked): P14-shape-2 to M4.S13.T13.C51.IMG1; P16-shape-1/2 to C52.IMG1; P18-shape-1 to C63.IMG1; P18-construction-2 (step 1 of the rhombus, an intermediate state) to M4.S17.T17.C67.IMG1; P19-shape-1/2/4/5 and P20-shape-1 to C68.IMG1; P21-shape-1 to C69.IMG1; the three Venn diagrams P15-venn_diagram-1, P20-venn-2, P20-venn-3 to M5.S26.T26.C104.IMG1 (the family rings; chunk C owns that image). P15-shape-2 and P15-construction-3 (both the 4, 5, 30 construction) are claimed by C56 (solution); P18-construction-3 (final step of the 50 degree rhombus) by C72.
- Printed copies of question figures on the solutions pages (P33-shape-1 to 4, P38-shape-2) are `none:SAME_AS_QUESTION_DIAGRAM`.

## 2. Borderline

- **C57, C59, C73 questions (none)**: the book shows the parallelogram/rhombus beside the deduction, but the LP question names the shape and gives all data in the text and refers to no figure. If you want a question figure for these, the specs would be: parallelogram ABCD with angle A = 30 (C57); parallelogram ABCD with AB = 4 cm and AD = 5 cm (C59); rhombus ABCD with angle A = 50 (C73).
- **C57, C59, C73 solutions (required)**: could be argued `optional` because the answers are numbers; kept required because the book's own answer is the filled figure and the steps rely on it.
- **M4.S15.T15.C63 and M4.S17.T17.C69 worked examples (optional, not added)**: the figure (parallelogram EASY with diagonals AY, ES at O, 10 cm and 6 cm; rhombus GAME with diagonals GM, EA at O, 8 cm and 6 cm) would clearly help, but the question names every point and length and exactly this figure is the concept's own teaching image (C63.IMG1, C69.IMG1), which stays. Flip to required if you want a drawn copy; the spec would copy that figure with the lengths and no answer halves.
- **M3.S11.T11.C44 worked example (none)**: three numbers, no figure, arithmetic working.
- **C75 question (required)**: the LP text carries every number, but the book gives the four figures with the question and the arrow/tick marks carry meaning (decision 4: kept required).
- **C48 solution (none)**: 360 - 270 = 90 needs no picture; a rectangle would only repeat the sentence.
- **C49 question**: the reflex arc at D and the shape come only from the figure; the LP text adds "one corner that caves in".

## 3. LP text issues

- **M3.S12.T12.C49** (question): the text does not say which corner caves in; the figure (and the book) caves in at D. Suggested: "(The quadrilateral $ABCD$ has one corner, $D$, that caves in.)"
- **M3.S12.T12.C50** (solution): the steps name neither the diagonal nor the triangles, so the figure's labels have no text to match. Suggested step 1: "Draw the diagonal $BD$ from the caved-in corner $D$ to the opposite corner $B$; it lies inside the figure." Step 2: "It splits $ABCD$ into triangles $ABD$ and $CBD$, each with angles adding up to $180$." Step 3: "At $D$, $\angle ADB$ and $\angle BDC$ together make the reflex angle of $ABCD$."
- **M4.S14.T14.C58** (solution): step 4 "$\angle C + \angle D = 180$" has no reason. Suggested: "$AD \parallel BC$ with transversal $CD$, so $\angle C + \angle D = 180$ and $\angle C = 180 - 150 = 30$."
- **M4.S14.T14.C60** (solution): step 6 is hard to follow. Suggested: "$\triangle ABD \cong \triangle CBD$ would match $A$ with $C$, $B$ with $B$ and $D$ with $D$, so it would make $AB = CB$; but $AB = 4\text{ cm}$ and $CB = 5\text{ cm}$."
- **M4.S16.T16.C66** (solution): steps 2 and 3 do not say which end of the line is B or D. Suggested step 3: "On it mark $D$ on the arm that makes the $140^\circ$ angle with $OC$, and $B$ on the opposite side of $O$, with $OB = OD = 2.5\text{ cm}$, so $BD = 5\text{ cm}$."
- **M4.S18.T18.C75 / C76**: inconsistent punctuation: the question has "(i): Parallelogram ..." in `question_tex` but "(i) Parallelogram ..." in `question`; the steps mix "(i):" with "(ii)". Suggested: use "(i)", "(ii)", "(iii)", "(iv)" with no colon everywhere.
- **M4.S19.T19.C77 / C78**: `book_number` is "Figure it Out, Q1" but the item is Figure it Out (p.102) Q3, and the sibling pairs of the same exercise say "Parallelograms and Rhombuses, Q1/Q2". Suggested: "Parallelograms and Rhombuses, Q3". The C77/C78 items also lack the `ncert_refs`/`example_id` that the other pairs carry.
- **M3.S12.T12.C47 / M4.S14.T14.C55 / C57 / C59 / C73 and others**: `book_number` is a description ("Quadrilateral Angles: find the fourth angle", "Parallelograms: construct with 4 cm, 5 cm and 30°") rather than a book question number; nothing to fix for diagrams.

## 4. Book unclear or different from the base inventory

- **P38-shape-2** (base entry): says C is lower than A. On the page picture (and on p.27) C is slightly higher than A. Corrected in the inventory entry; the spec follows the picture.
- **P33-construction-1** (printed answer to FiO Q2): the label "7 cm" sits under OB only, although AB (the whole segment) is 7 cm; the 140 degree arc is drawn between OB and the upper-left arm OC. The spec labels the four halves (3.5, 3.5, 2.5, 2.5) as the concept image C64 does.
- **P21-shape-2/3** (FiO Q1 (i), (ii)): the book labels 40 and 110 but draws about 47 and 108 degrees; the spec draws the labelled angles exactly. **P21-shape-4** layout was checked against page_21.png (X top-left, W top-right, U bottom-left, V bottom-right).
- **P18-shape-1** (EASY figure): the marks on EA and YS are unclear in the base inventory; not needed (mapped to a concept image).
- **P19-shape-3**: the book writes 65 on four arcs and 50 at A and C but does not mark 130 at B and D; the spec adds them (LP answer).
- No print slip that changes a drawn value was found in the printed answers of this chunk (P33/P34/P38 answers agree with the LP).

### Chunk C notes (from the decision agent)
# Chunk C notes: Class 8 Ch 4 "Quadrilaterals" (v29, v3 diagram rules)

Chunk C = topics M5.S21.T21, M5.S23.T23, M5.S24.T24, M5.S25.T25, M5.S26.T26, M5.S27.T27, M6.S28.T28 (15 units, 24 items).
Result: **required 12 / optional 2 / none 10** (question 2 / 0 / 7, solution 7 / 0 / 2, worked example 3 / 2 / 1). Validator: errors 0, one warning (C94 solution has no base figure of its own: it is the question kite plus marks).

| Unit (concept) | Question side | Solution side | Why |
|---|---|---|---|
| T21 C83/C84 geoboard bands | none | **required** (square + rhombus, 2 panels) | word question, figure answer |
| T21 C85/C86 triangle 8, 8, 6 | none | **required** (rhombus, parallelogram, kite) | word question, figure answer; book prints two of the three |
| T21 C87/C88 triangle 6, 9, 12 | none | **required** (six panels) | word question, figure answer; LP lists six results |
| T21 C89/C90 two equilateral triangles of 4 cm | none (book gives no figure) | **required** (rhombus ABCD) | printed answer is a picture |
| T23 C93/C94 kite proof | **required** (book figure, ticks) | **required** (marks added, derived) | book says "In the kite ..." on a figure |
| T23 C95/C96 kite from diagonals 6 and 8 | none | **required** (construction) | printed answer is a construction picture |
| T24 C97 worked: trapezium PQRS | **required** (given state, `?`) | - | book figure of PQRS, transversal angles |
| T24 C98 worked: isosceles trapezium UVWX | **required** (given state, `?`) | - | book figure of UVWX, parallel + equal sides |
| T25 C100/C101 trapeziums (i), (ii) | **required** | **required** (all angles, derived) | book gives both figures; printed answers are pictures |
| T26 C102 worked: names of a square | none | - | no figure, answer is a list of words |
| T26 C103 worked: diagonals give a rhombus | optional (not added) | - | LP-written example, no book figure |
| T26 C104 worked: Venn diagram | **required** (finished Venn) | - | printed answer is a Venn diagram |
| T27 C105/C106 four equal sides + 90 degrees | none | none | word reasoning, no figure anywhere |
| T27 C107/C108 true/false statements | none | none | word reasoning, no figure anywhere |
| T28 C110 worked: Which Quad? | optional (not added) | - | fold puzzle described fully in words |

New media ids (12): C84.IMG1, C86.IMG1, C88.IMG1, C90.IMG1, C93.IMG1, C94.IMG1, C96.IMG1, C97.IMG2, C98.IMG2, C100.IMG1, C101.IMG1, C104.IMG2 (the worked examples C97, C98, C104 keep their teaching image as IMG1, which is never linked).

## 1. Judgement calls

1. **Question side none for the activity questions (C83, C85, C87).** The book prints a geoboard picture and pictures of the two cut-out triangles, but every number is in the text (and the LP restates them), so a careful student loses nothing. The answers are arrangements, so the solution side is required (v3 Step E "word question, figure answer").
2. **C86 shows three panels, not four.** Step 4 of the LP answer (two equilateral triangles of 8 cm give a rhombus) gives the same shape as the first panel (rhombus with four 8 cm sides), so a fourth panel would repeat it. The book's Joining Triangles 1 pictures (P23-shape-1/2) are mapped none/TEXT_SUFFICIENT for the same reason.
3. **C88 solution has six panels** in one 16:9 card (top row the three parallelograms, bottom row the three kites, joined along the 6, 9, 12 sides). Each panel is scaled separately to its cell; shapes were turned to the smallest bounding box so they fit. Side labels are plain numbers (cm), as in the LP steps. The two kites joined along the 6 and 9 sides cave in at a corner (reflex angle 2 x 104.5 = 209 degrees), the one along the 12 side is convex: this was recomputed from the coordinates, the LP statement is right.
4. **C84 solution (geoboard).** The answer is a name, but the result of "join the ends" is a drawing; the figure shows the square (4 cm and 4 cm) and the rhombus (4 cm and 2 + 4 + 2 = 8 cm) with the 2 cm extensions in FOCUS. The base figures P22-geoboard-1/2 are mapped to this solution item because their bands are redrawn in it.
5. **C94 solution (kite proof).** Required although it derives from the question figure, because it adds what is proved: right angles at O, AO = OC, equal angles at B (one arc) and D (two arcs), triangles AOB and COB shaded in two colours with common side BO (as the LP s_figure says). Only the two lower right angles (AOB, COB) are marked, the ones the steps use. The arcs are trimmed 4 degrees short of BD so they read as two arcs.
6. **C97, C98 (worked trapezium examples) draw the given state only** (angles given, `?` for the asked ones, no dropped lines), because a worked-example figure sits after the question text. The perpendiculars XY and WZ of C98 are part of the working and are not drawn.
7. **C97 orientation.** The book draws PQ short on top; the LP example has angles P = 70 and Q = 55 (acute), so PQ is drawn as the longer bottom side (P bottom left, Q bottom right, R top right, S top left). Angles are drawn true.
8. **C100/C101 captions "(i)" and "(ii)"** are kept in the picture (decision 3): the LP question and answer refer to the two figures as (i) and (ii). No vertex letters (the LP uses none). Figure (ii) is drawn upright; the book prints it tilted by about 20 degrees, the shape is the same.
9. **C96 orientation.** B (2 cm from O) on top, D (6 cm from O) below, as in the book's printed answer (short upper part, long lower part). Letters follow the LP (A, B, C, D, O), not the book (P, Q, R, S, T). Equal-side ticks: AO = OC one tick, BA = BC two, DA = DC three.
10. **C104 Venn diagram.** One diagram for the worked example: the question gives no figure, the answer is the figure, so the finished diagram is drawn (three ellipses: parallelograms, kites, rectangles; the lens of kites and parallelograms is the rhombuses, the part of the rectangle ellipse inside the lens is the squares). Same structure as the book's printed answer (page 35) and its summary picture (page 29). The teaching image C104.IMG1 shows similar rings but is never linked.
11. **Inventory mapping choices.** P29-venn-1 (summary Venn) is claimed as concept_image:M6.S28.T28.C109.IMG1 (the Summary topic's own image, "the families nest"); C104.IMG1 would be the other possible choice. P35-shape-1/2 are the question figures printed again on the answers page, mapped to the question item. P30-paper_fold-4 is the unfolded sheet = concept image C110.IMG1. I did not claim the figures of Figure it Out Q5, Q6, Q7 (chunk A units) and Q9, Q10 (chunk B units), nor the page 31-33 answers pictures of other chapters' questions.
12. **Colours.** Solution figures with no question figure draw the outline in INK and what the answer states (angles, side labels, names) in ANSWER; derived solutions (C94, C101) keep the question figure in INK and add in ANSWER.

## 2. LP text issues (no decision was changed because of these)

- **M5.S21.T21.C83 / C84, band length.** The question says "rubber bands of 4 cm"; the book prints no length. Its picture shows a 9 x 9 peg board, bands 4 gaps long, and the extended band 6 gaps long (one gap added at each end), and the book says "extend by 2 cm", which would make one gap 2 cm, the bands 8 cm and the extended band 12 cm. The LP numbers (4 cm, extended to 8 cm) are consistent with each other and give the same shapes (square, then rhombus); the diagrams use the LP numbers. Suggested sentence if the picture should match: "Two rubber bands of 8 cm cross at right angles at their midpoints ... one band is extended by 2 cm at each end (to 12 cm)."
- **M5.S21.T21.C85 / C86, equilateral case.** The question text covers only the 8, 8, 6 triangle, but step 4 and the answer also give two equilateral triangles of 8 cm. Suggested question: "Join two copies of the triangle with sides 8 cm, 8 cm and 6 cm in different ways and name the quadrilaterals. Then join two equilateral triangles of side 8 cm and name the quadrilateral."
- **Degree signs missing.** Angle values are written as bare numbers in the steps of C90 ("$60$", "$60 + 120 + 60 + 120 = 360$"), C94 ("$180$", "$90$"), C97 and C98 and C103 (plain "90", "115"), C101 ("$180 - 105 = 75$"), C106, C108 ("$360 - 270 = 90$"). Suggested: write $60^\circ$, $180^\circ$ etc.
- **M5.S23.T23.C93 / C94.** The question asks only that BD bisects angle ABC, but step 2 and the answer also state angle ADC (the book asks for both). Suggested question: "Show that BD bisects $\angle ABC$ and $\angle ADC$, and that BD is perpendicular to AC with AO = OC."
- **M5.S25.T25.C100.** (a) The old q_figure hint says 135 and 105 degrees are at the ends of "the longer lower side"; in the book they are at the ends of the shorter (bottom) parallel side, the longer one is on top. The diagram follows the book. (b) Text (ii) "An isosceles trapezium with an angle of 100 degrees" does not say where the angle is; the solution assumes it is next to the shorter parallel side (the only place an obtuse angle can be). Suggested: "(ii): An isosceles trapezium in which an angle next to the shorter parallel side is $100^\circ$."
- **M5.S24.T24.C98.** Steps use the points Y and Z, which neither the question nor step 1 introduces. Suggested step 1: "Draw XY and WZ perpendicular to UV, meeting UV at Y and Z; XWZY is a rectangle, so XY = WZ."
- **M5.S27.T27.C106.** The question asks for reasoning "as well as by construction and measurement"; the steps give only the reasoning. Suggested extra step: "Check by construction: draw a rhombus of side 5 cm with one angle of $90^\circ$; measuring gives four right angles, so it is a square."
- **M5.S26.T26.C104.** The answer (ii) "Yes, a square" is right and differs from the book (see section 4). The `text` starts with an internal label "Figure it Out (kites and trapeziums, question 4):" which a learner should not see if the text is shown as is.
- **M6.S28.T28.C110.** The question merges the book's questions 4 and 6 and leaves out question 5 (the nested creases), which appears only as step 4. No change needed, noted for completeness.

## 3. Borderline

- **C93 question required, C103 optional.** Both are proofs about a quadrilateral with diagonals meeting at O. C93 is required because the book itself prints the figure ("In the kite, show that the diagonal BD ...", ticks give the equal sides); C103 is an LP-written example with no book figure and the text names every point, so it is optional (figure that would help: ABCD with the diagonals crossing at O at a right angle, OA = OC and OB = OD marked). If the content team wants proofs drawn regardless of a book figure, C103 would be the quadrilateral with those marks (the same layout as D6, without shading).
- **C97, C98 required although the LP text carries all numbers** and the concepts have a teaching image of the same trapezium: the book gives the figure (page 25) and the angle relations (co-interior angles, equal base angles) are read off the figure; decision 4 applied.
- **C110 optional.** A fold puzzle whose question is complete in words; a picture of the quarter-folded sheet with the slanting crease would help, but the LP gives no numbers or positions to draw, and the opened sheet is already the teaching image.
- **C102 none.** The five family names of a square are a list of words; the teaching image already shows them.
- **C106 / C108 none.** Word reasoning; the book's printed answers have no figure. A rhombus with one right angle (C106) would be optional-grade at most.
- **C83, C85, C87 question none** although the book prints pictures of the activity (see judgement call 1).
- **C84 solution required** for an answer that is a name; kept because "join the ends" produces the figure the reasoning is about and the sibling activities (C86, C88) are required.
- **C94 solution required** although it adds marks to the question figure rather than a new figure (see judgement call 5).
- **C104 required** although concept image C104.IMG1 shows similar family rings; v3 never links a teaching image and the book's answer is a figure.
- **C88 density.** Six panels with 24 side labels in one card is the densest figure of the chunk; the bounding boxes of all labels were checked for overlap in a preview, none overlaps an outline.

## 4. Book unclear or wrong

- **Wrong (followed the LP, as the maths requires):** the printed answer to Figure it Out (page 107) **Q4 (ii)** says "No", but a square is both a kite and a rectangle (the book's own Venn picture puts the squares in the overlap of kite and rectangle); the LP says "Yes, a square". The printed reason for **Q11 (i)** ("In a square the diagonals are also perpendicular") is not the reason the statement is false (equal bisecting diagonals give a rectangle, which need not be a square); the LP gives the right reason.
- **Incomplete:** the printed answer to Q3 (ii) gives angles A and B = 80 degrees but not angle C = 100 degrees; the LP and the diagram give all four angles.
- **Unclear:** the geoboard length (see LP text issues); the book does not say how many ways the 8, 8, 6 and 6, 9, 12 triangles can be joined and prints answers pictures only for Figure it Out, so the five results of C88 not printed in the book come from the LP steps. The book prints the 6, 9, 12 kite (page 24) and the 8, 8, 6 rhombus and parallelogram (page 23) only.
- **Picture differences, not mistakes:** the summary Venn (page 29, with the trapezium oval) and the Q4 answer Venn (page 35) draw the rectangle ellipse a little differently; both show the same relations. The Q2 answer kite (page 34) has its short upper part about 0.44 of the lower part with no numbers; the LP fixes OB = 2 cm, OD = 6 cm, used in the diagram.

## 5. How the specs were produced

The specs were built by scripts kept outside the chapter folder (`/tmp/claude-1506/-root-maths-learning-plan/546c0a55-f920-40d7-a2bc-1439e8909fdd/scratchpad/c8ch4_chunkC/`: `lib.py`, `diagrams.py`, `build_out_C.py`, previews in `prev/`). Every angle, side length, parallel/equal relation and region of the Venn diagram was recomputed from the coordinates in code (67 checks) before the text was written, and label boxes were checked against outlines. The `content` object of each diagram lists polygons, segments, ticks, parallel marks, right-angle marks, angle arcs, ellipses and labels with canvas coordinates (16 x 9 card, origin at the centre, y up, 120 px per unit).
