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
