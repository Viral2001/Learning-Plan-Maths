# Class 7 Ch 14 Constructions and Tilings - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths7_ch14` v39 (taken from staging). Result: new V2 version v40 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (74 items from 41 units)
{"worked_example": {"required": 7, "none": 1}, "question": {"none": 22, "required": 11}, "solution": {"required": 29, "none": 4}}

Optional, NOT added: []

needs_lp_text_sync: [('C27', 'solution'), ('C39', 'solution'), ('C43', 'solution')]

## The 47 diagrams
| id | side | type |
|---|---|---|
| M1.S2.T2.C4.IMG2 | worked example | geometry_figure |
| M1.S3.T3.C8.IMG1 | solution | construction |
| M1.S3.T3.C10.IMG1 | solution | geometry_figure |
| M1.S4.T4.C11.IMG2 | worked example | construction |
| M1.S5.T5.C14.IMG1 | solution | construction |
| M1.S5.T5.C16.IMG1 | solution | construction |
| M1.S5.T5.C18.IMG1 | solution | construction |
| M1.S7.T7.C22.IMG1 | solution | construction |
| M2.S8.T8.C23.IMG2 | worked example | construction |
| M2.S8.T8.C24.IMG2 | worked example | construction |
| M2.S9.T9.C27.IMG1 | solution | construction |
| M2.S9.T9.C28.IMG1 | question | construction |
| M2.S9.T9.C29.IMG1 | solution | construction |
| M2.S9.T9.C32.IMG1 | question | construction |
| M2.S9.T9.C33.IMG1 | solution | construction |
| M2.S11.T11.C36.IMG1 | question | construction |
| M2.S11.T11.C37.IMG1 | solution | construction |
| M2.S12.T12.C39.IMG1 | solution | construction |
| M2.S13.T13.C40.IMG2 | worked example | construction |
| M2.S14.T14.C43.IMG1 | solution | construction |
| M3.S15.T15.C44.IMG2 | worked example | geometry_figure |
| M3.S16.T16.C50.IMG1 | question | geometry_figure |
| M3.S16.T16.C51.IMG1 | solution | geometry_figure |
| M3.S17.T17.C53.IMG2 | worked example | construction |
| M3.S18.T18.C56.IMG1 | solution | construction |
| M3.S18.T18.C58.IMG1 | solution | construction |
| M3.S18.T18.C60.IMG1 | solution | construction |
| M3.S20.T20.C65.IMG1 | solution | construction |
| M3.S20.T20.C66.IMG1 | question | geometry_figure |
| M3.S20.T20.C67.IMG1 | solution | geometry_figure |
| M3.S21.T21.C69.IMG1 | solution | construction |
| M4.S23.T23.C74.IMG1 | question | tiling |
| M4.S23.T23.C75.IMG1 | solution | tiling |
| M4.S23.T23.C77.IMG1 | solution | tiling |
| M4.S23.T23.C81.IMG1 | solution | tiling |
| M4.S23.T23.C83.IMG1 | solution | tiling |
| M4.S25.T25.C89.IMG1 | question | tiling |
| M4.S25.T25.C90.IMG1 | solution | tiling |
| M4.S25.T25.C91.IMG1 | question | tiling |
| M4.S25.T25.C92.IMG1 | solution | tiling |
| M4.S25.T25.C93.IMG1 | question | tiling |
| M4.S25.T25.C94.IMG1 | solution | cell_grid |
| M4.S25.T25.C96.IMG1 | solution | cell_grid |
| M4.S26.T26.C97.IMG1 | question | tiling |
| M4.S26.T26.C98.IMG1 | solution | tiling |
| M4.S26.T26.C99.IMG1 | question | tiling |
| M4.S26.T26.C100.IMG1 | solution | cell_grid |

### Chunk A notes (from the decision agent)
# Notes, chunk A (Class 7 Ch 14 "Constructions and Tilings", plan cbse_eng_maths7_ch14_v39)

Result: 32 items = required 21 / optional 0 / none 11. Question: 3 required, 10 none. Solution: 12 required, 1 none. Worked example: 6 required.
All 49 base figures of book pages 1 to 16 are claimed here; validator `--chunk A`: errors 0 (9 warnings: required solution figures that are not printed in the book, which is expected because this pdf has no solutions section).

## 1. Judgement calls

Worked examples (units 1, 4, 9, 10, 17, 19 = M1.S2.T2.C4, M1.S4.T4.C11, M2.S8.T8.C23, M2.S8.T8.C24, M2.S13.T13.C40, M3.S15.T15.C44)
- All six are `required`. Their one slot is "the picture the example needs": the given state for a proof (C4, C44) and the finished construction for a construction (C11, C23, C40, C24). All six duplicate the kept teaching image of the same concept (C4.IMG1, C11.IMG1, C23.IMG1, C24.IMG1, C40.IMG1, C44.IMG1) on purpose: v3 says a teaching image is never linked and each item that needs a figure gets its own. If the content team thinks the teaching image already does the job, these six are the first to downgrade.
- C44 (six triangles round O) is the weakest: the arithmetic (6 x 60 = 360) is solvable from text. It is required only because the book question says "as in Fig. 6.12" (numbered figure referred to; v3 rule), although the LP question text does not name the figure. Could be `none` if the LP text is treated as the source.
- C24 (eight-petal design): the picture combines the book's Fig. 6.5 (petals), its supporting lines and the 45 degree angle the example finds. The kept teaching image shows only lines and angles.
- C4: figure shows only the given state (AX = AY = BX = BY ticks, AB meets XY at O), no right-angle mark, because the right angle is what is proved.

Pairs, solution side
- Constructions (units 2, 5, 6, 7, 8): solution `required` (B2: answer is a drawing, even though the steps are words). Units 5, 6, 7 (Figure it Out Q1 to Q3 of the perpendicular bisector) have the same decision on purpose (sibling consistency), although their final answers are "No / No / Yes" with a justification, because the LP answer starts from a drawn construction (different radii) and the justification points at its letters.
- Unit 3 (P equidistant from X and Y): solution `required` as SPATIAL_GEOMETRY (the proof names P, B, O and four triangles). This is the most arguable "required": a content team that wants text-only proofs would make it `optional`/`none`.
- Units 11, 16, 18 (draw four angles and bisect / copy them / draw four pairs of parallel lines): solution `required`, one 16:9 card with four panels in a 2 by 2 grid. The LP gives only kinds (small acute, right angle, large acute, obtuse; four orientations; across / up and down / two slanting), no sizes, so sizes are chosen and `needs_lp_text_sync` is true on these three: U11 uses 40, 90, 75, 125 degrees; U16 uses 50, 60, 40, 80 degrees in the book's four orientations (V with vertex at the bottom, opening left, narrow angle at lower right, vertex at top left); U18 uses m at 0, 90, 20, -35 degrees and l at 55 degrees to m. Letters repeat in the four panels. A single 2 by 2 card is busy (24 to 36 labels); if it renders badly, split into IMG1/IMG2 or drop to one panel.
- Unit 13 (other angles by bisection, 65.5 degrees): both sides `none` (arithmetic and divisibility reasoning).

Pairs, question side
- Units 2, 3, 5, 6, 7, 8, 11, 13, 16, 18: `none`: the learner draws their own segment, line or angles; a bare segment XY or line with O carries no data (no question figure when nothing is given).
- Unit 16 (copy four angles): the book prints four sample angles under the question (P12-angle-1). I treated the picture as an illustration of "different orientations" (the text asks the learner to construct their own angles), so the question is `none`; the picture is mapped to the solution item because the solution figure re-draws those four orientations beside their copies. Alternative reading: the four angles are given and should be a question figure.
- Unit 15 (copy an angle) is `required` although unit 16 is `none`, on purpose: the LP text of unit 15 says "an angle with vertex A is drawn ... a ray from a point X", so the angle and the labels A and X exist only in the figure; the text of unit 16 is self-contained.
- Unit 12 (arcs on the other side): `required`, the book says "as shown in the figure" and the position of C (far side of O, outside the angle) and of the line through O is spatial. The LP text describes it in words, so this one is arguable. Solution derived from it (adds AC, BC dashed, the extension to D, equal angle arcs at O).
- Unit 14 (square with four petals): question `required` (the book says "Construct the following figure" and the target exists only in the picture), solution derived from it (shading, side midpoints, midlines, centre). The four semicircles coincide with the arcs of the question figure, so the solution adds nothing in arcs; the new marks are the shading, four midpoints, two dashed midlines and the centre dot.

Figure inventory
- Pages 1 to 16 all claimed here, including figures in teaching topics that have no unit (M1.S1.T1, M1.S6.T6, M2.S10.T10: mapped to the concept images of those topics). Page 17 figures (P17-shape-1 the 70 degree gap figure, P17-shape-2 the 60/120 line) are not claimed: the gap-angle question (unit 20) is chunk B's.
- Book figures whose questions are NOT in the LP (no item can use them) are mapped `none:TEXT_SUFFICIENT` with a note in their description: P05-design-1 (Figure it Out Q4, recreate the four-petal design), P07-construction-1 (Fig. 6.4, rope construction), P10-design-2 and P10-shape-1 (Fig. 6.6, Figure it Out Q2 of copying an angle), P13-design-1 (eight-pointed star), P14-shape-1, P14-construction-1, P15-shape-1, P15-construction-1 (arches), P16-shape-1, P16-shape-2 (pentagon and hexagon of the Try This). There is no reason code for "no LP item"; TEXT_SUFFICIENT is the closest. If the content team adds those questions later they will need figures.
- Decorative: P03-design-1/2/3 (eyes of other shapes), P04-instrument-1 (compass and ruler), P07-illustration-1 (hands with rope): DECORATIVE_ONLY.
- Base descriptions were checked against the page pictures for every figure with doubts (P04-instrument-1, P07-illustration-1, P10-design-1, P10-angle-1, P12-angle-1, P13-design-1, P14-shape-1, P15-shape-1): all agree with the pictures; no CORRECTED entries. Sizes read off the pictures (45 degrees at A, about 50 degrees for XOY, arc radius half the side in the petal square) are estimates.

Geometry used in the specs (all coordinates computed so lengths and angles hold; each diagram states a frame to fit to a 16:9 card, same frame for question and solution of a derived pair)
- U1 AXBY: AX = AY = BX = BY = 5.378. U2 eye: R = 5, A = (0, 3), B = (0, -3), XY = 8. U3: P = (0, 2) on AB. U4: XY = 9, radius 5.6. U5: r = 4.2, s = 5.6 (XY = 7). U6: r = 4.2, s = 5.2. U7: r = 4.2, s = 5.6, P off the bisector. U8: OX = OY = 2.2, radius 3.6. U9: 50 degrees, OA = OB = 3.4, AC = BC = 3.6. U10: petal tip 3.4, half-width 0.55, arc radius 2.90. U12: 50 degrees, OA = OB = 2.2, CA = CB = 4.5. U14: side 6.4, radius 3.2. U15: 45 degrees, radius 2.2, BC = ZY = 1.684. U17: l at 50 degrees, radius 2.2, CD = FE = 1.859. U19: circumradius 3.6.
- Right-angle marks are placed at the upper-left (angle AOX), as the LP says angle AOX = 90 degrees; the book's Fig. 6.3 puts it at the right.

## 2. Things in the LP that look wrong or thin

- Book numbers in M2.S9.T9 are off: the LP's "Figure it Out 6.1, Q2" is the book's angle-bisection Figure it Out Q3 (arcs on the other side), the LP's "Q3" is the book's Q4 (65.5 degrees) and the LP's "Q4" is the book's Q6 (petals in a square); the `ncert_refs` (FiO_ab3, FiO_ab4, FiO_ab6) carry the right numbers. The book's Q2 (construct Fig. 6.5) is the worked example C24, Q5 (rope bisector) is not in the LP.
- Several book questions are absent from the LP: rope questions (page 7, Q1 justify AB in Fig. 6.4, Q2 90 degrees with a rope), angle bisection Q5 (rope), copy-an-angle Q2 (construct Fig. 6.6), parallel lines Q2 (the star), arches (pages 14 to 16), four-petal design (page 5, Q4). Intentional or not, the figures of these are unclaimed by any item.
- M1.S5.T5.C14 step 4 uses the point O (where AB meets XY) without ever naming it.
- M1.S3.T3.C10 (unit 3): the proof pairs P with B and shows PB is the perpendicular bisector, so P lies on AB; the figure therefore shows the conclusion (P on AB). Step 1 says "if P is on the same side as A"; the figure puts P between O and A.
- M2.S9.T9.C31 step 3: "Every angle made this way, doubled enough times, becomes a whole multiple of 45 degrees" is true (it becomes a multiple of 180 degrees), but a reader may find it abrupt; "131 is not divisible by 3 or by 5" is correct (45 = 9 x 5, 131 is prime). 65.5 may be a deliberate near-miss of 67.5 (= 45 + 22.5).

## 3. Where the book itself is unclear

- Angle sizes are never printed: the angle at A (Step figures of copying an angle) looks like 45 degrees, XOY (bisection steps) about 50 degrees, the four sample angles of copy Q1 about 40, 55, 30 and 75 degrees. The specs fix 45 and 50 degrees and say so in `render_note`; the four sample angles are given different sizes (50, 60, 40, 80) so their labels fit.
- Fig. 6.6 (five sectors) has no printed angle (about 60 degrees); not used by any item.
- Whether the petals in Fig. 6.5 overlap near the centre: the picture shows them crossing near O; the spec draws them so (tip 3.4, half-width 0.55).
- "Figure it Out Q1" picture of four angles (copy an angle) could be read as given angles to copy or as an illustration of orientations (see unit 16 above).

### Chunk B notes (from the decision agent)
# Notes, chunk B (Class 7 Ch 14, topics M3.S16.T16, M3.S17.T17, M3.S18.T18, M3.S20.T20, M3.S21.T21, M4.S23.T23)

Result: 15 units (14 pairs, 1 worked example), 29 items: required 15 (3 question, 11 solution, 1 worked example), optional 0, none 14. Validator: errors 0, 7 warnings (required items whose figure is not printed in the book: C51, C56, C65, C67, C69, C77, C83).

Figures claimed: 30. All figures of book pages 17-23 that belong to topics of this chunk or to teaching topics with no chunk (M3.S19.T19, M4.S22.T22): 9 to items, 2 to concept images, 19 to none. P16-shape-3 (Fig. 6.12) and P17-shape-1 (the gap figure) are also claimed because questions C50 and C48 use them; chunk A may claim the same two, and the merge will then keep one as a separate NEW- use. The pentagon/hexagon "Try This" pictures (P16-shape-1, P16-shape-2) are left to chunk A (page 16, topic M3.S15.T15). P23-grid-2, P23-grid-3, P24-grid-1 and P24-tiling-2 are left to chunk C (its questions use them).

## 1. Judgement calls

- **C48 question (gap angle, 70 degree angle): none.** The book says "Consider this figure", but the question text already gives all six angles, the gap angle AOI and the 70 degrees, and a careful student loses nothing without the fan of triangles (tie-breaker). The same picture is the teaching image M3.S15.T15.C45.IMG1, so P17-shape-1 is accounted to that concept image. The 'refer picture' rule (question optional) does not apply as written because the book has no printed answer that points at a picture; the outcome (no diagram, no link) is the same.
- **C49 solution: none** (arithmetic: 310, 50, 70 > 50). The LP hint figure (gap labelled 50 degrees, 70 degree wedge) would only repeat numbers.
- **C50 question (Fig. 6.12): required, borderline.** The text names A to F and O, but the lettering order and the three lines through O are only in the figure, and the book itself says "In Fig. 6.12 ...". Sibling to C66 (labelled star). Alternative: none, with the text carrying "A at the top, B to F clockwise".
- **C51 solution: required.** It adds the six 60 degree marks at O (the steps are built on them) and derives from C50. Alternative: none (the steps are words and sums).
- **C53 worked example (120 degrees): required**, one picture of the finished construction, placed after the question text as the rules demand; it also shows the 60 degrees on the left of AD (step 6), which is the book's P17-shape-2 pair. The concept already holds the teaching image C53.IMG1 (hexagon, side 4 cm), so this diagram takes IMG2. I drew the dashed line AC (GUIDE) although the steps only say "then angle CAB = 60 degrees" and "join A and D": the two 60 degree marks need AC.
- **Constructions C56, C58, C60, C65, C69: solution required (ANSWER_IS_FIGURE), question none** (no given figure in the book; for C69 the learner draws their own line and point). All five stand alone (derived_from null), colours: given line, A and P in INK; construction arcs, radii and helper lines in GUIDE; everything the solution adds in ANSWER.
- **C56 (circle method) draws the six radii as dashed GUIDE** and a 60 degree mark at AOB, because the steps use the equilateral triangle OAB and six 60 degree angles round O. It draws six cut arcs, the sixth (centre F) landing on A, as the LP says.
- **C60 (120 degrees at each corner)** draws the construction arcs at B, C, D and E only (the LP constructs there; FA is just joined). Every angle is labelled 120 degrees and every side ticked, with "5 cm" on AB, as the LP's last step says all sides are 5 cm and all angles 120 degrees. Each constructed corner shows the main arc (radius 100 px) and two cut arcs 60 degrees apart.
- **C65 (30 and 15 degrees): ONE solution diagram for both blocks** (the 30 degree answer and the extra 15 degree item share the answer concept; the brief allows one solution diagram per pair). It shows the 60 degree ray AC (GUIDE), the 30 degree ray AD and the 15 degree ray AF (ANSWER), the point E where AD meets the first arc, and the bisecting arcs for D and for F. If the team wants one picture per angle, the unit would need a second solution id.
- **C69 (perpendicular from P): sample instance chosen** (P is 2.4 units above l, 1 unit right of O, all arcs of radius 3 units, so Q is the mirror image of P and 1.8^2 + 2.4^2 = 3^2). The LP text has only letters (P, X, Y, Q, O, l), so no LP text sync is needed. I added dashed PX, PY, QX, QY with equal-length ticks (one tick on PX, PY; two on QX, QY) because step 5 uses the congruent triangles PXQ and PYQ.
- **C66 question (labelled star): required.** The question names the outer points and the inner corners but their positions are only in the book's hint figure (P19-shape-2); the picture changes how correctly the learner can follow the argument. The plain outline star (P19-shape-1) belongs to the book task "Construct the following 6-pointed star", which is not an LP item; it is accounted to the teaching image C62.IMG1.
- **C67 solution: required, ALL marks drawn** (six shaded point triangles, three 60 degree marks in each, a 120 degree mark at each hexagon corner: 18 + 6 = 24 values, written at 34 px). The LP only works through triangle AGH and says "the same reasoning works for the other five points", so a figure that marks only AGH was the alternative; I chose the complete final state (companion note). It is dense but the preview at 1920 x 1080 shows every value fits inside its triangle.
- **Tiling, C74 question: required, borderline.** "Show one way" is an action on the grid the book prints with the question (4 rows, 6 columns) and with the two tile positions; the LP question text does not say which of the two numbers is rows. The question figure is the empty grid plus the two sample tiles (what the book prints). Alternative: none. **C75 solution** derives from it and keeps the sample tiles at the same positions.
- **C76 (4 x 7) and C78 (5 x 7) questions: none**, because the book prints no figure for them (the LP hint `q_figure` describes a grid and a tile that the book does not show). **C77 solution: required** (the answer is an arrangement of 14 vertical tiles). **C79 and C85 solutions: none** (no tiling exists; parity arguments are text).
- **C80, C82 questions: none; C81 and C83 solutions: required**, same decision for the same kind of answer (a strategy with a concrete example grid). C81 draws the LP's example (6 rows x 4 columns, 3 vertical tiles per column, 12 tiles), C83 the LP's example (3 rows x 4 columns, 2 horizontal tiles per row, 6 tiles). The book's own picture for the "both even" case is the general m x n strategy with dotted lines; it is the book's answer, so it goes to the solution side.
- **Figures with no LP item** (claimed as none): the Figure it Out designs of pages 19-20 (inflexed arc, flower, hexagon in a circle, ring of six circles, the 24-triangle pattern, the optical illusion, the star inside a hexagon) and all tangram pictures of pages 20-21. The LP has no question for them. Codes: TEXT_SUFFICIENT (no item uses them) and OPEN_ENDED for the optical illusion.
- Coordinates are px on a 1920 x 1080 canvas; every geometric fact (equal sides, angles, arc intersections, tile counts) is asserted in the build script, and each figure was previewed once outside the repository to check that labels do not hit lines. Question and solution diagrams of the three derived pairs use the same code and the same coordinates.

## 2. Things in the LP that look wrong or thin

- **C68/C69 book number**: the LP says "Figure it Out 6.1, Q1" but in the book this is Figure it Out Q4 on page 20 (the Try This about a perpendicular from a point outside a line); the book's Q1 on those pages is the set of constructions (a) to (e).
- **The LP has no questions** for the Figure it Out constructions of pages 19-20 (Q1 (a)-(e), Q2 optical illusion, Q3 star in a hexagon) nor for the tangram pages 20-21 (Figure it Out with 10 silhouettes). Not a diagram problem, but those book exercises are missing from the plan.
- **C60 step 5**: "The angles of a regular hexagon add to 6 x 120 = 720 degrees, and FA comes out 5 cm" asserts the closing side instead of explaining it; the figure simply draws the closed hexagon.
- **C75 solution**: the LP says 12 vertical tiles, the book's "Here is one way" picture uses horizontal tiles in columns 1-2 and 5-6 and vertical tiles in columns 3-4. Both are valid; the LP wins and is drawn.
- **C76 and C78 `q_figure` hints** describe figures the book does not print.
- **C65**: the old answer concept carried two cards (IMG1, IMG2) for the 30 and 15 degree blocks; this map gives the pair one solution diagram (IMG1), so the builder has to handle the old IMG2 card of C65 (and likewise C56, C58, C60, C67 and C69, which also had IMG1 and IMG2 cards) like any other replaced card.

## 3. Places where the book is unclear

- The book prints no solutions section; all answers follow the LP.
- Page 17: the fan of triangles is not to scale and its side lengths are only roughly readable (the base inventory says the same); the LP text carries all the numbers.
- Fig. 6.12 labels the centre O just below and to the right of the centre point; the diagram puts the O label in the sector between OC and OD, 70 px from the centre.
- Page 22: the book hatches the grid squares and shows the tiling as green lines through the tiles; the diagrams use plain squares and shaded tiles outlined in ANSWER green.

### Chunk C notes (from the decision agent)
# Notes, chunk C (Class 7 Ch 14, topics M4.S25.T25, M4.S26.T26, M4.S27.T27)

Result: 13 items, required 11 / optional 0 / none 2. Validator: errors 0, one warning (T25 Ans4 has no printed book figure, expected).

## 1. Judgement calls

1. **T25 Q1, Q2, Q3 question figures: required.** The LP text already describes each 5 x 3 region in words ("top right square removed", "middle of the second row", "middle of the top row"), so a strict reading of the tie-breaker could say `none`. I chose `required` because the book gives each region as a picture (p.23, p.23, Fig. 6.13 on p.24), the task is spatial (the learner has to place tiles on it), and Q2 refers to "the following region" and Q3 to a lettered figure (Fig. 6.13, which v3 says is drawn even if a teaching image shows it). Teaching image M4.S24.T24.C86 already shows the Q1 region (with its tiling), but it is never linked, so Q1 still gets its own plain-region figure. If the user prefers text-first, Q1 and Q2 question figures are the two to demote to `none`; the solution figures do not depend on them except for `derived_from`.
2. **T25 Q4 (colour_another) question: none.** The book gives no figure for "use this idea to find another unit square...". No question figure is invented (companion note). Its solution is `required` and stands alone (`derived_from` null).
3. **Colouring solutions required (T25 Ans3, Ans4, FiO Ans2).** The proof is a colour pattern, which LaTeX cannot show reliably (`HIGHLIGHT_MEANING`); Ans3 is also the action the question asks for ("Colour it like a chessboard"). FiO Q2 is the borderline one (its answer is "no", with the argument in words and numbers); I kept it `required` for sibling consistency with Ans3/Ans4 (same kind of colouring answer) and because the key fact, that both removed corners are the same colour, is only visible in the picture. If one of these three is demoted, demote all three.
3b. **Tilings required (T25 Ans1, Ans2, FiO Ans1).** The answer is an arrangement of tiles (`ANSWER_IS_FIGURE`), even though the steps list the tiles in words.
4. **Worked example C101 (squares, triangles, hexagons tile the plane): none** (`TEXT_SUFFICIENT`, `LATEX_ARITHMETIC`). The example is angle arithmetic at one corner and gives no figure of its own; the three tilings are the teaching image of the same concept (M4.S27.T27.C101.IMG1) and are not linked. A picture of the three corners "would help but is not needed" (that is `optional`, not added); I used `none` because the teaching image already shows exactly that.
5. **Hatching replaced by plain CELL_FILL.** The book hatches every region square. Hatching is not in the style tokens and, more importantly, a missing square inside a region (Q2) would read as a white square among white squares without a fill. Regions are CELL_FILL with INK outlines; removed squares are simply not drawn. Tiles in solutions are MARK_FILL pieces with an ANSWER outline, inset 0.1 units, on top of the squares. All strokes 3 px (style rule: uniform 2 to 3 px).
6. **Chessboard colours.** White squares reuse CELL_FILL (the question figure's fill, reads as white), black squares INK. Rule: white if row + column is even, black if odd (white corners). Legend counts ("8 white", "6 black" etc.) are in ANSWER and use words the LP solution uses; they are the only text besides the FiO labels.
7. **FiO labels "Region to be tiled" and "Tile".** These two italic labels are printed beside the book's figures and are the only way to tell the two objects apart, so I kept them as category labels (allowed by the brief). If the reviewer reads them as captions, drop them from `visible_text` and the descriptions of C97, C98, C99, C100; nothing else changes.
8. **FiO Ans2 sample tile.** The solution figure keeps the question layout and recolours the sample tile white over black, matching LP step 4 ("each tile covers one white and one black square").
9. **Q4 solution example.** The dashed FOCUS outline marks row 2, column 1, the LP's own example; the other six black squares are shown by the black fill only.
10. **Honeycomb photograph (p.27).** Missing from the base inventory; added as `NEW-P27-honeycomb-photo`, mapped to concept image M4.S27.T27.C102.IMG1 (accounting only).
11. **Fig. 6.14** (p.24): first use = teaching figure, mapped to concept image M4.S24.T24.C87.IMG1; its black-and-white region panel is redrawn as the solution figure of T25 Q3, entered as `NEW-P24-tiling-2-sol`. Same pattern for the five other "second use" entries `NEW-...-sol` (region redrawn with the LP's tiling or colouring).
12. **Figures with no item:** P26-tiling-4 (Escher-style example a) `TEXT_SUFFICIENT`; P26-tiling-5 (hat tiling b), P27-tiling-1 and -2 (Escher artwork c, d) `NOT_RENDERABLE`.

## 2. Things in the LP that look wrong or thin

- **T25 Q4 question text (C95)** says "Use the colouring to find another unit square...", but the question never states the colouring convention. The solution depends on "white corners" (row + column odd is black). The `q_figure` hint ("a grid ... coloured like a chessboard with white corners") describes a figure the book does not give. Suggest adding "Colour the 5 x 3 grid like a chessboard with white corners" to the question text (`text_alternative` of the item says this).
- **T25 Q4 answer:** "Removing any black square leaves 8 white and 6 black, which no set of tiles can cover" is right and sufficient; removing a white square leaves 7 and 7 and is not decided by this argument. The LP does not claim otherwise. Fine.
- **Old card ids** (C92.IMG2, C94.IMG2, C96.IMG2, C98.IMG2, C100.IMG2) are being replaced; the new ids are all `<concept>.IMG1`, so there is no collision.
- Every tiling and colouring in the LP solutions was re-checked in code while building the map: Ans1 (1 + 3 + 3 = 7 tiles covering the 14 squares), Ans2 (4 + 3 = 7 tiles, tile list covers the 14 squares exactly), FiO Ans1 (four L tiles cover the 12 squares, each tile an L inside a 2 x 2 block), colour counts 8 / 6 (Ans3), 8 / 7 (Ans4), 32 / 30 (FiO Ans2). All agree with the LP text; no contradiction found.
- The book has no printed solutions section, so nothing could be cross-checked against printed answers.

## 3. Places where the book is unclear

- Row 1, column 2 of the Q2 region (P23-grid-3) is hatched more faintly in print; it is part of the region (the picture shows 14 squares).
- In Fig. 6.14 the plain horizontal tile has only its left square hatched; a printing quirk, not redrawn (the Fig. 6.14 tiles panel is not used).
- The page picture of FiO Q1 and Q2 matches the base inventory exactly (12 and 62 squares). Triangle patch (23 triangles) and hexagon patch (12 hexagons in columns 2, 3, 2, 3, 2) were re-counted and are correct; they are accounting only.
