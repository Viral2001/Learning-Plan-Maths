# Class 6 Ch 8 Playing with Constructions - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths6_ch8` v47 (taken from staging). Result: new V2 version v48 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (106 items from 65 units)
{"worked_example": {"required": 4, "none": 17, "optional": 3}, "question": {"none": 25, "required": 11, "optional": 5}, "solution": {"required": 26, "none": 7, "optional": 8}}

Optional, NOT added: [('C16', 'solution'), ('C31', 'question'), ('C32', 'solution'), ('C34', 'solution'), ('C43', 'solution'), ('C55', 'solution'), ('C57', 'worked_example'), ('C62', 'question'), ('C66', 'question'), ('C67', 'solution'), ('C69', 'solution'), ('C93', 'worked_example'), ('C100', 'solution'), ('C127', 'worked_example'), ('C132', 'question'), ('C136', 'question')]

needs_lp_text_sync: [('C27', 'solution'), ('C39', 'solution'), ('C41', 'solution')]

## The 41 diagrams
| id | side | type |
|---|---|---|
| M1.S2.T2.C2.IMG2 | worked example | geometry_figure |
| M1.S3.T3.C8.IMG1 | solution | geometry_figure |
| M1.S3.T3.C9.IMG1 | question | geometry_figure |
| M1.S5.T5.C13.IMG1 | question | geometry_figure |
| M1.S5.T5.C14.IMG1 | solution | construction |
| M1.S6.T6.C15.IMG1 | question | geometry_figure |
| M1.S6.T6.C18.IMG1 | solution | geometry_figure |
| M1.S8.T8.C22.IMG1 | question | geometry_figure |
| M1.S8.T8.C23.IMG1 | solution | construction |
| M1.S8.T8.C24.IMG1 | question | geometry_figure |
| M1.S8.T8.C25.IMG1 | solution | construction |
| M1.S9.T9.C27.IMG1 | solution | geometry_figure |
| M2.S12.T12.C33.IMG1 | question | geometry_figure |
| M2.S14.T14.C38.IMG1 | question | geometry_figure |
| M2.S14.T14.C39.IMG1 | solution | geometry_figure |
| M2.S14.T14.C41.IMG1 | solution | geometry_figure |
| M2.S15.T15.C42.IMG1 | question | geometry_figure |
| M2.S16.T16.C44.IMG2 | worked example | construction |
| M2.S18.T18.C51.IMG1 | solution | construction |
| M2.S18.T18.C53.IMG1 | solution | construction |
| M2.S19.T19.C56.IMG2 | worked example | construction |
| M2.S22.T22.C75.IMG1 | solution | construction |
| M2.S23.T23.C78.IMG1 | question | geometry_figure |
| M2.S23.T23.C79.IMG1 | solution | geometry_figure |
| M2.S25.T25.C83.IMG1 | solution | geometry_figure |
| M2.S25.T25.C84.IMG1 | question | cell_grid |
| M2.S25.T25.C87.IMG1 | solution | construction |
| M2.S25.T25.C89.IMG1 | solution | construction |
| M2.S25.T25.C91.IMG1 | solution | construction |
| M3.S26.T26.C94.IMG1 | worked example | geometry_figure |
| M3.S30.T30.C109.IMG1 | solution | geometry_figure |
| M3.S31.T31.C111.IMG1 | solution | geometry_figure |
| M3.S31.T31.C113.IMG1 | solution | geometry_figure |
| M3.S33.T33.C121.IMG1 | solution | construction |
| M3.S34.T34.C123.IMG1 | solution | construction |
| M3.S34.T34.C125.IMG1 | solution | construction |
| M4.S36.T36.C130.IMG1 | question | geometry_figure |
| M4.S36.T36.C131.IMG1 | solution | construction |
| M4.S37.T37.C133.IMG1 | solution | construction |
| M4.S39.T39.C137.IMG1 | solution | other |
| M4.S39.T39.C139.IMG1 | solution | construction |

### Chunk A notes (from the decision agent)
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

### Chunk B notes (from the decision agent)
# Chunk B notes (Class 6 Ch 8, topics T15, T16, T18, T19, T20, T22, T23; units 20 to 36)

Result: 28 items = required 8 / optional 7 / none 13. Validator: errors 0, warnings 2 (C56 and C79, see 0).

Required diagrams (media ids): M2.S15.T15.C42.IMG1 (Think figure A to D), M2.S16.T16.C44.IMG2 (finished square PQRS), M2.S18.T18.C51.IMG1
(rectangle 4 by 6), M2.S18.T18.C53.IMG1 (rectangle 10 by 2), M2.S19.T19.C56.IMG2 (rectangle 7 by 4), M2.S22.T22.C75.IMG1 (two-panel squares
solution), M2.S23.T23.C78.IMG1 and M2.S23.T23.C79.IMG1 (square within a rectangle, question and solution).

## 0. Bookkeeping the merge needs to know
- `NEW-P08-dot_grid-1-T15` is the SECOND use of base figure `P08-dot_grid-1` (the dot strip with A to D). The first use is chunk A's "identify the
  squares in this collection" question. I did NOT claim the base id itself. If chunk A leaves that figure without a required item, nobody claims
  the base id and the merged check will flag it; the specs of the two items must also be identical (mine: 40 x 11 dots, corners
  A (5,1)(9,5)(5,9)(1,5), B (15,1)(18,5)(15,9)(12,5), C (26,1)(31,5)(26,9)(21,5), D (36,3)(38,4)(36,8)(34,7), letters under columns 5, 15, 26, 36;
  all checked against the page picture by pixel position).
- Two required items have no inventory figure (validator warning, expected): C56 (the plain rectangle 7 by 4 is not printed as such; the book's
  8.4 pictures all carry X and Y) and C79 (the book prints no answer picture for Construct 1).
- Inventory mappings I chose: the six STEP 1 to 5 pictures of the square (P09-1..3, P10-1..3) and the four 8.4 X-Y pictures (P11-1..4) are teaching
  pictures with nothing for an item to link, so `none:TEXT_SUFFICIENT`; P10-construction-4 (STEP 6, finished square) became the diagram of C44;
  P13-shape-1 and P14-shape-1 (three squares, rough diagram of ACDF) are the two panels of C75's solution diagram; P15-shape-1 is C78's question
  diagram; the six tables are plain tables (`none:LATEX_TABLE`).

## 1. Judgement calls
1. T15 Think (C42/C43): question REQUIRED (the text says "in the above figure"; the data is only in the dots); solution OPTIONAL. The printed answer
   is "Yes, the position of the points on the grid paper makes it possible" and the LP steps are a complete method. A copy of figure A with 4 across
   and 4 down marked on each side would help, but the LP steps give no numbers, so a drawn count would also need a text change. Could be flipped to required.
2. C44 (square of side 6 cm) and C56 (rectangle 7 by 4) are REQUIRED although the same concept already holds a teaching image of the finished
   figure (kept image C44.IMG1 / C56.IMG1). Reason: the answer of each worked example is a constructed figure (v3: ANSWER_IS_FIGURE; same decision as the
   Construct Q1/Q2 rectangles whose printed answers are pictures), and v3 says a teaching image is never linked. The new diagrams differ a little from the
   teaching images (all four sides labelled, all four right angles marked, no arcs). If the user does not want a second copy of a figure that sits in the same
   concept, both can be flipped to none.
3. C45 ("why PS is 6 cm") and C46 ("RS and angles R, S"): NONE. Both are answered by the properties of a square and every fact is in the text. The book
   prints a figure beside C46 (STEP 6), but it adds nothing the text lacks, and C44's figure is the same square.
4. T18 Q1 and Q2: question none (no figure is given, a blank rectangle would imply one), solution REQUIRED because the printed answers are pictures.
   T18 Q3 solution OPTIONAL: the printed answer is the word "No"; a picture of perpendiculars staying the same distance apart would help, but a teaching image of that idea exists.
5. T19 C57 (Math Talk about closest and farthest) is OPTIONAL: a discussion question with no figure attached to it and a complete text answer. A picture
   of rectangle ABCD with X on AD, Y on BC and a dashed XY is the figure that would help. This is the T19/T20 call most likely to be flipped, because the
   book builds 8.4 on four pictures of exactly that rectangle. C58 is NONE (it compares two lengths stated in words).
6. T20 (Rectangle Exploration, four pairs): only the printed answers decide, and none of them is a picture (two plain tables, "XY = AB; ABYX is a
   rectangle", "equal to AC or BD"), so: Q1 question optional, Q1 solution none (plain table plus arithmetic), Q2 both none (plain tables), Q3 question and
   solution optional (rectangle with X, Y level and the four-sided figure ABYX shaded would help), Q4 question none (it names the diagonals in words) and Q4
   solution optional (X at A, Y at C, diagonal AC, sqrt(65) cm). The Q3 pair is the best candidate to become required if the user wants a picture here.
7. T22 (rectangle that divides into three squares / into two squares): question NONE (the LP text describes the target in words and no longer says
   "as shown in the figure"), solution REQUIRED. The pair holds two blocks on one card, so there is ONE solution diagram with two panels (top: 9 cm by 3 cm
   in three squares of side 3 cm, no vertex letters because the LP letters only the first square; bottom: ACDF 8 cm by 4 cm with ABEF, BCDE, the book's 7 equal-side ticks, 4 cm and 8 cm).
8. T23 Q2 (A Square within a Rectangle): question REQUIRED because the LP text still says "as shown in the figure" (the bracket after it does not replace the reference),
   solution REQUIRED and `derived_from` the question figure (adds the 4 cm side and the 2 cm gaps). This differs from T22 only because T22's text has no figure reference.
   T23 Q1 is NONE for both sides (numbers only).
9. Colours: where the question has no figure, the solution diagram stands alone; outlines and measure labels are INK, the right-angle marks and equal-side ticks (the checks the
   solution adds) are ANSWER green. All diagrams are 16:9 cards, drawn to scale.
10. The book's printed answer pictures for Construct Q1 and Q2 show right-angle marks at two corners and compass arcs at the top corners. The LP answers state four right angles
    and the LP steps do not mention arcs, so my figures show all four right angles and no arcs.

## 2. Things in the LP that look wrong or thin
- T20 questions C62, C64, C66 and C68 never say that X lies on side AD and Y on side BC; they only give distances from A and B. Flagged `needs_lp_text_sync` with the sentence to add
  ("X is a point on side AD and Y is a point on side BC.").
- C62's question text repeats the three cases twice (the "XY = ___ centimetres ___ millimetres" sentences and then an a) b) c) list), and C64's text has the cases as prose and again as (1) (2) (3).
- C42's `q_figure` hint says "A, B and C are diamonds of different widths and heights"; in the book A is a square standing on a corner (8 dots across, 8 down), B is 6 by 8 and C is 10 by 8,
  D is a 2-by-1 / 2-by-4 rectangle. The question text itself does not describe the figure, and the LP solution steps contain no numbers.
- C44's answer already states "RS = 6 cm and angle R = angle S = 90 degrees", which is exactly C46's question.
- C45, C46, C57, the second block of T22 and C78 (A Square within a Rectangle) have no printed answer in the book (checked pdf pages 31 to 38); the LP answers are authored. I recomputed them:
  C63 (a) sqrt(49 + 6.25) = 7.43 -> 7 cm 4 mm, (c) sqrt(53) = 7.28 -> 7 cm 3 mm; C69 sqrt(65) = 8.06 -> 8 cm 1 mm; C79 (8 - 4) / 2 = 2; C77 4 is not 2 x 2.5 and 7 is not 3 x 2; C75 AC = 4 + 4 = 8.
  All agree with the book where the book has an answer (7.4, 7, 7.3 cm; 7 cm throughout).
- C75's first block lists the construction with letters A, B, C, D only for the first square (AB, AD, BC) and then "the total length is 9 cm", so the labels of the finished 9 cm rectangle are not defined; the diagram leaves them out.

## 3. Places where the book is unclear or contradicts itself
- Square construction, pages 9 and 10: STEP 3 puts S above P, but STEPs 4, 5 and 6 print R above P and S above Q. That reads P, Q, S, R round the square, and the Think box on page 7 says PQSR is NOT a valid name.
  The LP steps and my figure use S above P and R above Q.
- Page 11 pictures: the first matches the case "X 5 mm from A, Y 3 cm from B" (Y is 1 cm above C), but the second shows X 1 cm and Y 2 cm from the top, which is none of the three listed cases, the third is X = D, Y = B and the fourth X = A, Y = B.
- Solutions page 34, question table: the second column reads 5 cm, 1 cm, 4 cm, which looks like a printing slip (the chapter page 13 has 5 mm, 1 cm, 1 cm 5 mm and the printed answer table uses those values).
- Page 15 Construct 1 picture is not to scale (about 2.2 : 1, side parts about 2.4 cm instead of 2 cm); the page 13 three-squares picture is also slightly wide (parts 1.08 times as wide as tall). Both are drawn exactly to scale here.
- Math Talk (page 12) and "Explore: Can the rectangle now be completed?" (page 14) have no printed answer.

### Chunk C notes (from the decision agent)
# Notes for chunk C (Class 6 Ch 8, plan cbse_eng_maths6_ch8_v47)

Units 37 to 56: M2.S25.T25, M3.S26.T26 to M3.S32.T32. 31 items: required 9, optional 2, none 20. Validator: errors 0, warnings 0.

Required (all `keep_and_replace_spec` except C94 `add_new_image`):

| item | media_id | what it draws |
|---|---|---|
| C83 solution | M2.S25.T25.C83.IMG1 | the two staircases of squares (4-4-4 and 7-5-3), one card |
| C84 question | M2.S25.T25.C84.IMG1 | the Shadings figure (4 by 4, 11 hatched diagonal cells, plain 2 by 2 block, plain unit square) |
| C87 solution | M2.S25.T25.C87.IMG1 | square, both diagonals (GUIDE), circle at the crossing (ANSWER) |
| C89 solution | M2.S25.T25.C89.IMG1 | 2 by 2 squares, diagonals of each, four equal circles |
| C91 solution | M2.S25.T25.C91.IMG1 | 8 cm square, four inward arcs (radius 8 cm), the four outside compass points |
| C94 worked | M3.S26.T26.C94.IMG1 | rectangle PQRS, both diagonals, the eight angles lettered a to h (no values) |
| C109 solution | M3.S30.T30.C109.IMG1 | finished rectangle ABCD, diagonal AC, 60 and 30 degrees at A and C |
| C111 solution | M3.S31.T31.C111.IMG1 | finished rectangle, 50 and 40 degrees (printed answer is a picture) |
| C113 solution | M3.S31.T31.C113.IMG1 | finished square, four 45 degree marks, ticks (printed answer is a picture) |

Optional (not added): C93 worked (figure with the letters c, d, g, h), C100 solution (square with one diagonal and 45 + 45).

## 1. Judgement calls

1. **8.4 Construct 2, 4, 5, 6 (C82, C86, C88, C90): question `none`, solution `required`.** The LP question text fixes each figure completely (sizes, staircase corners; a square with a circular hole at its centre; 2 by 2 with four centred holes; 8 cm square with four inward arcs, corner to corner). A careful student loses nothing without the picture, so the tie-breaker says none. The answer is a construction (B2, ANSWER_IS_FIGURE), so the solution figure is drawn standalone (question has no figure, `derived_from` null), and it carries the construction marks the steps only describe (diagonals that find the centres, compass points). This mirrors Number Play 3.1 (word question, figure answer). **If the user wants the book's target picture on every "Construct this" question, the four question sides would become required (the book does print a picture for each); only Construct 3 needs it to attempt, so I kept them none.**
2. **8.4 Construct 3, Shadings (C84 question required, C85 solution none).** The LP words ("some halved by diagonals ... a plain larger square in a corner") cannot fix the figure; the book's picture IS the task, so the question is required (FIG_REFERENCED + DATA_IN_FIGURE). The solution would only repeat that picture (the LP steps add no mark or number), so `SAME_AS_QUESTION_DIAGRAM`. This breaks the sibling pattern of item 1 on purpose, for that reason.
3. **C91 (curves) sample answer.** The solution figure follows the LP's own sample (compass 8 cm, tip 8 cm from both ends of the side, dip 1.072 cm, which the LP rounds to "about 1 cm"). The book's printed picture has deeper arcs (about 0.21 to 0.24 of the side, about 1.7 to 1.9 cm, which is a 90 degree arc of radius side/sqrt(2) = 5.66 cm). The book gives no radius and no printed answer for Construct 6, so the LP wins. I included the short crossing arcs because LP step 3 talks about them. **Needs the user's eye: should the solution use the book picture's deeper arcs instead (then the LP steps and answer text would need a new radius)?**
3b. The compass points of C91 are 6.928 cm outside each side, so the 8 cm square fills only about a third of the card height and the 1.07 cm dip is about 36 px at card size; legible but small. The figure is drawn to scale.
4. **C94 required, C93 optional.** C94 asks which of the eight lettered angles are equal; the answer (d = e = a = h, c = f = g = b) only has meaning on the book's lettered picture, and the LP needs 40 words of text to describe where each letter sits (DATA_IN_FIGURE). C93 uses the same picture but only asks "are g and h equal? are c and d equal?"; the answer does not depend on which is which, so the picture is not needed to attempt (optional, mentioned so the user can promote it; if promoted it is the same spec as C94 with the note "same as C94"). The figure for C94 is not coloured by equal groups (that would leak the answer).
5. **C92, C97 worked (diagonals equal; square) none.** The learner draws and measures; the answer is a statement. The same picture is already the teaching image of the concept (C92.IMG1, C97.IMG1); a duplicate adds nothing.
6. **C106 worked (60 + 30) none.** 90 - 60 = 30 from the rule that angle A is 90 degrees; the book's Step 3 picture is a construction step, not data.
7. **C109 (Example 2, rectangle with 60 and 30 degrees): solution required, standalone; question none** (the book question has no figure; the rough diagram sits in the solution). Only the complete final state is drawn (v3), not the book's step pictures. I added the angles at C (60 on the CD side, 30 on the CB side) because the question speaks of "opposite angles", the printed answers of FiO Q1 and Q2 mark both ends, and they follow from alternate angles; the book marks only A. I used the exact 60 degree proportion (BC = AB x 1.732); the book's rough diagram is not to scale. Right-angle marks at B and D only (the corners the diagonal does not split), equal-side ticks because the LP check says AB = CD, AD = BC.
8. **C111, C113 (FiO Q1, Q2): solution required, question none.** The printed answers are pictures (B2). Same layout as C109 for consistency. Left out of the printed pictures: the "Arbitrary Length" label (not a measure; the LP says any length), the arrows, and the compass arc at D (the LP method uses a perpendicular at C). For Q2 I mark the right angle at B and D (the printed one marks B only) so the three rectangle figures match.
9. **C115 to C118 (Construct 2, side 5 cm and diagonal 7 cm) all none.** The questions are answered in words and the concepts already have teaching images of these steps (C114.IMG1 arc from D, C116.IMG1 corner B on line l, C118.IMG1 checking the rectangle). The rough diagram and Step 1 are not needed to attempt C115. These book step pictures are accounted as concept images (P22-construction-2 -> C116.IMG1, P24-construction-1 -> C114.IMG1, P24-construction-2 -> C118.IMG1) or none:TEXT_SUFFICIENT.
10. **C100 optional, C102 and C104 none.** C100: the printed answer is a sentence; a square with one diagonal and 45 + 45 would help but the teaching images C96.IMG1 and C97.IMG1 already show it. C101/C103 are Math Talk discussions (OPEN_ENDED); their answers are text.
11. **Solution diagrams are standalone (no `derived_from`)** because the only required question diagram (C84) has a `none` solution.
12. **Figure accounting overlaps with chunk D.** The Construct 2 solution pictures (P22-shape-1, P22-construction-1/2, P23-construction-1, P24-construction-1/2) can also be used by D for Example 3 (the same construction as a practice pair, C120/C121). Here they are mapped only by their use in chunk C; D may map P24-construction-2 or P22-shape-1 to its own solution item. The merge should compare these.

## 2. Things in the LP that look wrong or weak

- **C84 / C85 (Shadings).** The question text is too vague to build the figure (needs the picture) and never mentions the plain unit square (row 4, column 3). The solution steps say "Draw the diagonals in the small squares. Shade one triangle in each", but two of the 13 cells are plain (the 2 by 2 block and one unit square): 11 of the small squares carry a diagonal and hatching, not all.
- **C90 / C91.** "This is a square with 8 cm sidelengths" is a leftover of the book picture; the LP could say "Draw a square with 8 cm sides". The answer_tex "dips about 1 cm" is arithmetically right for radius 8 cm (1.072 cm) but the book's own picture is deeper (see call 3).
- **C93.** Uses the letters c, d, g, h without saying where they are (the book defines them by the picture). C94 does define them.
- **C94 steps.** "The four angles next to the long sides come out equal: d, e, a, h" is right only when PQ and SR are the long sides (as in the 6 by 4 example). In a rectangle taller than wide the roles swap. The LP never says PQ is the long side. The figure drawn for C94 has PQ as the longer side (about 1.7 : 1, like the book).
- **C115.** The answer says "the base CD" but the question text never introduces C and D (the book's rough diagram does).
- **C116.** The answer relies on "the diagonal DB = 7 cm" which the question text does not say; the question mentions line l and point B with no picture. C117 mentions "line l" without saying it is perpendicular to DC at C. Both rely on the teaching image and the preceding blocks.
- **Naming.** The LP calls the 8.5 end-of-section tasks "Figure it Out 8.5, Q1/Q2"; the book prints them under the heading "Construct" (p.211, and "Construct" in the printed solutions p.35). The LP's "Example 2" and "Example 3" are the book's "Construct 1" and "Construct 2" of section 8.5. Harmless but may confuse a reader checking the book.
- **C101/C102.** The answer adds "cut each other into equal halves" (true, but nowhere in the book's questions); fine.

## 3. Where the book itself is unclear

- **Construct 6 (curves, p.17):** no radius, no compass-tip position, no printed answer in the solutions section (only Construct 4 has a one-sentence answer; Constructs 2, 3, 5, 6 of 8.4 have none). The arc depth of the picture was measured from the page (about 0.21 to 0.24 of the side).
- **Construct 3 (Shadings, p.16):** the hatch-line count per triangle is not countable exactly (about 9); 9 is used. No measurement is printed ("choose measurements of your choice").
- **Construct 1 rough diagram (p.19):** not to scale (height about 1.5 times the width instead of 1.73) and marks the right angle at D only, while the Step 4 picture (p.21) marks it at B only.
- **Construct 2 pictures (p.22-24):** the rectangle is lettered A top-left, B top-right, C bottom-right, D bottom-left (Construct 1 and the printed answers on p.35 use A bottom-left instead); the Step 3 circle is not to scale (radius about 1.2 times DC, not 1.4); point B is not lettered in the Step 3 pictures.
- **Printed answers p.35 (Construct Q1, Q2):** right-angle marks differ (none in Q1, one at B in Q2), only Q2 has equal-side ticks, and both carry construction marks (arrows along the top line and up from C, a compass arc at D) that belong to a compass method the LP does not use.
- **Solutions numbering:** the solutions heading "Page no. 201, Q.4 Square with a Hole" refers to chapter page 203 (Construct 4); the page numbers in the solutions section are the book's own and do not match the pdf pages.

### Chunk D notes (from the decision agent)
# Chunk D notes (Class 6 Ch 8, units 57-65)

Result: required 8 (7 solutions + the house question), optional 3, none 5. Validator: errors 0, warnings 0.
Script that wrote out_D.json (kept outside HERE): scratchpad `c6ch8_D/gen_out_D.py`.

## 1. Judgement calls

1. **Questions with no given figure get no figure (C120, C122, C124, C138).** The three rectangle questions and the "four equal sides" question give lengths or a yes/no in words and the book prints no figure with them. Decision `none` (TEXT_SUFFICIENT). Their solutions are required (printed answer is a picture, B2) and stand alone (`derived_from` null).
2. **Solution figure = complete final state, not the book's step pictures.** The book walks through 8.5 Construct 2 and the house in steps (base only, base + l, circle, arc, ...). Those are intermediate states, so the single solution figure shows the finished figure plus the one short construction arc the LP steps mention. The step pictures are accounted for as `none:TEXT_SUFFICIENT` (P22-construction-1/2, P23-construction-1, P25-construction-1, P26-construction-1, P30-shape-1) or as the teaching image that already shows the idea (P24-construction-1 -> T32.C114.IMG1, P27-construction-1 -> T35.C126.IMG1, P28-construction-1 -> T35.C128.IMG1, P29-construction-1 -> T7.C20.IMG1).
3. **Overlap with chunk C (please reconcile at merge).** Pages 22-24 (the book's solved example 2 of 8.5) are the section of both my T33 and chunk C's T32 teaching blocks (C115 to C118). Figures claimed by both: P22-shape-1, P22-construction-1, P22-construction-2, P23-construction-1, P24-construction-1, P24-construction-2. My meaning: P22-shape-1 and P24-construction-2 (rough and finished rectangle) -> my solution item C121; P24-construction-1 -> concept image T32.C114.IMG1; the other three -> none (intermediate step). If chunk C turns the finished-rectangle picture into its own item (the T32.C118 block), mine becomes the second use and should be `NEW-P24-construction-2-<suffix>`.
4. **House question (C130) required, solution (C131) required with `derived_from`.** The book prints the house with "Recreate this figure" (p.25); the arc B-C sags downward with centre A, which the LP words do not say. The question figure is exactly what the book gives (no construction arcs). The solution adds only the two ANSWER arcs of radius 5 cm from B and from C that cross at A (the idea of the section), same layout and positions.
5. **Bigger house (C132) is `optional`, not required.** The book prints no figure with FiO 8.6 Q1; "a bigger house" points back to Example 4's house, which sits two cards earlier and is a teaching image of an earlier topic (T35.C128.IMG1). Not added; **text sync needed** (see section 2). Its solution (C133) is required: the printed answer is the 7 cm house picture; it is drawn standalone with the same two crossing arcs as Example 4 (sibling consistency).
6. **Artwork question (C136) is `optional`, same logic as 5.** It points at three Artwork figures printed in section 8.1, not here. One composite picture is not given by the question, so none is added.
7. **Artwork solution (C137): one composite picture** with the three printed answer drawings (Person left, Wavy Wave top right, Eyes bottom right), because a pair gets at most one solution diagram. I followed the LP text where it differs from the printed answer: equal half circles for the wave (the print is hatched and drawn as tall half-ellipses, almost certainly stretched), no hatching, a plain square body for the person (as the LP and print say), round pupils. Wave size taken from section 8.1 (central line 8 cm, two half circles of radius 2). Eye size chosen (tips 6 apart, two arcs of radius 5, lens 2 tall, pupil radius 0.75) because the book gives no eye dimensions; the picture is to look like the print, not to carry numbers.
8. **Rhombus (C139):** drawn as the LP builds it (A at the origin, angle 60 degrees, D found by two arcs), which is the book's own hint picture. The printed answer is an unlabelled diamond standing on a vertex (same shape, turned). The 60 degree label is the LP's own example angle ("for example 60 degrees").
9. **Worked blocks in T35.** C126 (circles meet, how far from B and C): `none`, all data in words and the same card already shows the teaching image. C127 (was it necessary to draw two full circles): `optional`, a picture of the two short arcs crossing at A would help but the text answer is complete; text alternative written.
10. **Computed side lengths shown on the rectangles** ("4.9 cm", "6.9 cm", "6.3 cm") in ANSWER green: the LP answers state them (about 4.9, 6.9, 6.3); recomputed as sqrt(7^2-5^2) = 4.899, sqrt(8^2-4^2) = 6.928, sqrt(7^2-3^2) = 6.325.
11. **Aspect ratios:** the house (5 cm and 7 cm) and the two tall rectangles (4 x 6.9 and 3 x 6.3) are clearly tall, so `3:4`; the rest 16:9. The pipeline's 16:9 card will centre them.

## 2. Things in the LP that look wrong or thin

- **Question numbers in the LP do not match the book.** T34 is "Figure it Out 8.5, Q1/Q2" but the book numbers are Construct Q3/Q4 (ncert_refs say Q3/Q4, correct). T37 "Figure it Out 8.6, Q1" is right (book Q1). T39 C136 is labelled "Figure it Out 8.6, Q1" and C138 "Q2", but the book numbers are Q2 and Q3 (ncert_refs say Q2/Q3, correct); C136 also repeats C132's concept name "Figure it out: Q1".
- **C132 (bigger house) text lacks the house.** The question says only "a bigger house in which all the sides are 7 cm". Suggested text (needs_lp_text_sync): "Construct a bigger house like the one in Example 4 (a square body with a door, a roof whose two sides equal the body sides, and a curved arc from B to C with centre at the roof point A), in which all the sides are 7 cm."
- **C130 question text (house)** describes the arc only as "a curved arc from B to C"; the figure shows it sagging below the line BC. The required figure carries that.
- **C137 answer** says the person's body is "a 4 cm by 4 cm square body in the book's solution", but the Artwork person of section 8.1 has a body whose top is a downward arc. The question asks to recreate the Artwork figures, the printed answer shows a plain square. The picture follows the printed answer and the LP.
- **C137 answer says "half circles" for the wave**, the printed answer is hatched half-ellipses. Picture uses half circles (LP wins).
- **Concept names:** C126 and C127 are both named "Where two circles meet"; unit 57 is called "Example 3" while the book numbers it solved example 2 (ncert_ref 8.5.ex2 is right).
- C121/C123/C125 `s_figure` hints are fine; C131's `s_figure` ("circles around B and C crossing at A") is thinner than the LP steps, which use arcs; I followed the steps.
- All LP numbers checked: 4.9, 6.9, 6.3 (sides); BC = DE = 5 so triangle ABC is equilateral; 7 cm house door 2 x 3 as printed.

## 3. Where the book is unclear

- **The printed house on p.25 is not to scale:** the arc sags about 0.22 of BC, the exact value for centre A and radius 5 is 0.134 (0.67 cm), and the door looks about 1.3 by 1.7 cm. The figures are drawn from the stated measures, not copied from the print.
- **Step 3 circle (p.23)** is drawn with radius about 1.2 x DC instead of 1.4 x DC and B is not lettered; not copied.
- **Door position:** the book gives only the door's size; centred on DE as printed (gaps 2.0 in the 5 cm house, 2.5 in the 7 cm house).
- **Person neck length** is not labelled (about 2 cm by scale), eye proportions are not given (see 1.7).
- **Rhombus printed answer** has no letters or angles; the 60 / 120 degrees are read from its proportions.
- **Solutions p.36:** the rectangle heights are not labelled; taken as sqrt(8^2-4^2) and sqrt(7^2-3^2), which match the print's proportions (1.72 and 2.1 times the base).
