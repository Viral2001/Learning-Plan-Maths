# Chunk A notes (Class 6 Ch 8, units 1 to 19: book sections 8.1 and 8.2)

Result: 31 items = required 16 / optional 4 / none 11. Validator: errors 0, 4 warnings (required solution diagrams with no printed book figure behind them: C14, C23, C25, C39).
Questions: required 7 (C9, C13, C15, C22, C24, C33, C38), optional 1 (C31), none 4 (C7, C17, C26, C40).
Solutions: required 8 (C8, C14, C18, C23, C25, C27, C39, C41), optional 3 (C16, C32, C34), none 1 (C10).
Worked examples: required 1 (C2), none 6 (C3, C4, C5, C28, C29, C35).
All specs use a 16:9 canvas of 16 x 9 units (origin at the centre, y up). Concept ids below are written without the M.S.T. prefix where the topic is clear (e.g. C13 = M1.S5.T5.C13).

## 1. Judgement calls

Required (the book gives a figure the learner needs, or the printed/LP answer is a picture):
- **C2 (worked) and C9 (question), Fig. 8.1.** Both items need the five artwork pictures (the learner copies them). Same spec twice (render_note says "same as M1.S2.T2.C2.IMG2"). The book prints the five pictures in three rows; the spec re-arranges them in two rows (3 + 2) to fit a 16:9 card. Sizes read off page 1 (circles about 69 px, concentric outer 65 px, head 67 px), idealised to radius 1.05 units. The C9 solution is `none` (SAME_AS_QUESTION_DIAGRAM): its final state is the same five pictures. If the team prefers a construction picture there (centres and radii), flip it.
- **C13/C14 Wavy Wave.** Question figure = the book's target (shaded half circles). The book's picture has no letters or measures; A, X, B and "8 cm" are written because the question text names them (a question figure may show what the question gives). The solution adds the two compass-tip points (2 cm and 6 cm from A), the 2 cm radii and AX = XB = 4 cm in ANSWER green.
- **C15 (FiO 8.1 Q1) question.** Needs the figure (AB = 8 cm, X, half circle, '?' for radius and AX). The book draws a compass clip-art with a '?' arrow for the unknown opening; I replaced it by a dashed radius of the half circle marked '?' (no clip-art allowed). X is drawn at the middle of AB because the book's picture does (positions only, no value printed).
- **C18, C27, C41 solutions with no question figure** (the questions give none, so they get none): required because the book's printed answer is a picture. They are standalone (`derived_from` null).
- **C22/C23 Person, C24/C25 Eyes.** Question figures are the targets; the solutions are compass constructions, so they show the tip(s) and equal radii. Person: the tip O is drawn at the head's centre (see section 3). Eyes: A above, B below, equal radii A/B to the two corners.
- **C33 question** (dot grid A to D): required. The letters A to D are drawn because the question and the answer use them ('A is a square'); this is not a 'Fig. a.' caption. No counts, no shading (it must not leak the answer).
- **C38/C39 (FiO 8.2 Q1).** Question figure = Fig. 8.3, solution = the same figure on a dot grid with the one-dot diagonal links. The book's printed answer is only a sentence, but the LP answer to 'draw this on dot paper' is a drawing (B2 ANSWER_IS_FIGURE), and it is the same kind of answer as Q3 (printed picture), so both required (sibling rule).
- **C41 (FiO 8.2 Q3) solution.** Copies the book's printed picture (three tilted shapes on an 8 x 9 dot grid). The LP's own example (a diamond with corners 4 dots from its centre) is not drawn.

None / optional (kept in text):
- **C3, C4, C5, C28, C29, C35 (worked examples):** the question gives no figure, or its text already states everything (C29 gives every corner position) and the concept's kept teaching image shows the idea. Fig. 8.3 and Fig. 8.4 are not needed to attempt C28/C29.
- **C7/C8 Think (all points 4 cm from P):** question none (no figure), solution required (printed answer is a picture).
- **C16 solution: optional.** A figure with both half circles, AX = XB = 4 cm and radius 2 cm would help (the LP steps talk about the second half circle that the question figure does not show), but the printed answer is text only and the numbers are complete in the steps.
- **C31/C32 (which is not a name for this square): both optional.** Most borderline call. The LP question text already states S top left, P top right, Q bottom right, R bottom left, so a careful learner loses nothing without the figure; the solution figure (arrow path S-P-Q-R and dashed diagonal QS) would help but the three text steps are complete. If the team wants a figure for every 'this square' question, flip both to required; the spec would be the square with those four letters (question) and the same square with the path and the dashed QS (solution, derived).
- **C34 solution: optional.** Dots counted across and down on each figure would help (it is what the book's Think asks), but the printed answer is text only ('A is a square.') and the LP steps already give widths and heights.
- **C17 (FiO 8.1 Q2) and C40 (FiO 8.2 Q3) questions, C26 question:** no given figure, so none. C26's question points back to the neck of 'A Person' but draws nothing new.

Inventory mapping calls:
- `P01-artwork-1` maps to C2; its second use is the new entry `NEW-P01-artwork-1-C9` (C9 question).
- `P29-construction-1` (Eyes hint, book p.29) maps to `concept_image:M1.S7.T7.C20.IMG1` (that concept image is its teaching counterpart); the C25 diagram is drawn independently. Chunk D owns that book section and may map it differently; please compare at merge. Same for `P04-construction-1` (compass photo of the person's arc, mapped to concept image C19.IMG1) and `P06-shape-2` (Fig. 8.4, mapped to concept image C29.IMG1).
- `P08-dot_grid-1` (A to D grid) is also the figure of the 'Think' unit M2.S15.T15 (chunk B); I took the base id for the first use (C33).
- `P07-shape-1` (square SPQR) is mapped `none:TEXT_SUFFICIENT` because the C31 question diagram is optional (a figure cannot map to a non-required item).
- No `CORRECTED:` entries: the base descriptions of every figure I claim agree with the page pictures (checked the dot counts of A to D: 40 x 11 dots, corner positions confirmed by pixel position; SOL32 grid 8 x 9 confirmed).

## 2. Things that look wrong in the LP

- **C34 (and its question C33) leaks the answer.** The question text says "A is a diamond whose left to right span equals its top to bottom span (about 8 dots each way); B about 6 wide and 8 tall; C about 10 wide and 8 tall; D a small tilted long rectangle". These are exactly the facts the learner is meant to find out from the picture. Better: keep only "four tilted figures A, B, C, D on a dot grid".
- **Wrong book numbers in the LP:** C26/C27 are labelled "Figure it Out 8.1, Q1" but are book Q3 (ncert 8.1.FiO.Q3); C33/C34 are labelled "Figure it Out 8.2, Q1" but are book Q2; C40/C41 are labelled "Figure it Out 8.2, Q2" but are book Q3. (C15, C17, C38 are right.) The concept names say "Figure it out: Q1" for three different questions.
- **C16 step 1** says "the two equal half circles share the 8 cm line", but the question text mentions only the first half circle; the second is only in the book's Wavy Wave picture.
- **C18 and C27 (LP vs book).** LP: one wave = two half circles (or two shallow arcs). Book printed answers: a longer line with four half circles / four shallow arcs (two waves) and a 'central line' caption. I followed the LP (it wins) and noted it in the specs; the printed answers are still the reason these solutions are `required`.
- **C25 text:** "Draw two light horizontal guide lines" and the hint "two horizontal lines drawn lightly" is unclear for one eye. Read as one guide line through the corners of each eye (the book's hint shows a line through the eye and a second line of the same height for the second eye). The answer text 'A and B lie on the line through the middle of the eye, one on each side' and step 2 'tip at B draws the upper curve' agree with A above, B below.
- **C8 s_figure** mentions two points Q and R on the circle with 4 cm lines; neither the LP solution text nor the book's printed answer has them (one radius only). Not drawn.
- **C4 and C5** have the same concept name ("The compass draws the circle: centre and radius") but only C4 carries the kept teaching image.
- **C23 text** says the tip is found 'by trial' above the body; the book's person is drawn with a single tip (see section 3), which the LP does not mention.
- **C2 text:** the C2 question text is a very long verbal description of Fig. 8.1; once the figure is added after the question text, the description could be shortened.

## 3. Where the book itself is unclear

- **Fig. 8.1** has no measures; relative sizes read from the picture (touching and overlapping circles about 69 px, concentric outer 65 px, inner 33 px, mouse head 67 px, ears 33 to 35 px, eyes 16 px, centre distance of the three overlapping circles about 1.55 radii, the X's two segments are slightly unequal). Idealised and symmetric in the spec.
- **A Person (p.190):** the compass photo is not to scale and shows no tip position. Measuring the printed person: head diameter 95 px, body 115.5 px wide, corners 22.5 px above the lowest arc point, neck 40 px; these numbers make the body's arc concentric with the head circle (arc centre and head centre coincide within 2 px, arc radius about 85 px, neck = arc radius minus head radius). So the tip is at the head's centre, 'above the body on the middle line' as the LP says. The spec states this as geometry (tip O = (0, 1.632)); the LP's 'found by trial' is not contradicted.
- **Eyes (p.192):** the pupil is a slightly oval blob (39 x 31 px); the LP says 'filled dark circle', so a circle is specified. Hint A/B positions are only 'approximate; the student estimates' (base inventory); the spec fixes A and B at 3.447 units above and below the eye's corner line (equal distance, sagitta 0.9625, radius 4.41, all consistent).
- **Fig. 8.3 (p.192):** the printed squares sit 0.75 of a square side away horizontally and 0.25 vertically from the rectangle, not equally. The book's answer says 'leave one dot distance diagonally'. The spec uses the dot-grid version in both the question and the answer figure (rectangle 8 x 4, squares 2 x 2, gap 1 diagonal) so that the two figures coincide.
- **Printed answers (p.31):** Q2's wave has four half circles, Q3's has four shallow arcs of height about 0.28 of their width; no measures. The specs choose concrete numbers (L = 10 cm from the LP; chord 6.4 and radius 4.0 for the shallow arcs, which satisfies 'radius bigger than half the chord' and 'smaller than a half circle'; `needs_lp_text_sync` is true for C27, C39, C41 because the LP gives no numbers and the specs pick them, but the numbers are not printed in the figures).
