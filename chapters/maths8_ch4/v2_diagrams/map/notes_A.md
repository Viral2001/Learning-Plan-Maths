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
