# Notes, chunk C (Class 7 Ch 9 "Geometric Twins", topics T11 to T15)

Result: 29 items, required 16 / optional 4 / none 9. Validator: errors 0, 6 warnings (all "required but no base figure maps to it": the item's figure is not printed in the book, see 1.7).
Counts by role: worked_example 6 / 4 / 7, question 6 / 0 / 0, solution 4 / 0 / 2 (required / optional / none).

I checked every base figure of the chunk against the page pictures (pages 12 to 20): all 18 descriptions are correct, none needed a CORRECTED note. The `unclear` doubts in the base inventory are only about photograph details (triangle counts in the Louvre, dome, rangoli, bridge pictures); those pictures are not redrawn, so they do not matter here.

## 1. Judgement calls

1.1 Rule I used for solution figures (pairs). A solution figure is required when the solution adds NEW equal-part marks to the question's figure and the argument stands on them; it is none when the solution only reads values already on the figure, or only does arithmetic.
- Required: C51 (vertically opposite angles at O, result AB = CD), C55 (alternate angles from DC parallel to AB, facing angles at O, OC = OA, OD = OB), C57 (shared side BC highlighted, angles BAC and BDC matched), C59 (whole angles ABC and DCB from two parts each, angles BAC and CDB, AB = DC, OB = OC, OA = OD).
- None, C53 (the 47 degree pair): everything the solution uses (7 cm, 5 cm, 47 degrees at B and at Z) is already printed on the question figure; it only matches letters. `SAME_AS_QUESTION_DIAGRAM`. This breaks sibling consistency inside the set on purpose, the reason says why.
- None, C68 (isosceles, 80 degrees): a figure question with a numeric answer, the Step E typical pair (question required, solution none). The steps are 180 - 80 = 100 and 100 / 2 = 50; no new relation is drawn. If the team wants the 50 / 50 / 80 triangle as a picture, it is a one-line change (same triangle, two values in ANSWER).

1.2 C52 question (47 degree pair) is required although its text gives every number. The book prints the pair as a figure (an exact mirror pair), which corner sits where decides the order of the letters the question asks for, and the other four questions of the set are required. Tie-breaker says "changes how correctly they solve it".

1.3 Worked-example constructions are required: ASA (C46 block 0), RHS (C60 blocks 0 and 1), altitude (C63 block 0), equilateral by construction (C64 block 1). B2 says a construction answer is a drawing even when the steps are words. They show the finished construction (given parts INK, produced parts ANSWER); the worked example has one slot after the question text, so one finished figure.
- C60 blocks 0 and 1 both get a figure although the teaching image C60.IMG1 already shows the RHS half: v3 never links a teaching image, and the two blocks need different pictures (block 0 triangle PQR; block 1 the line carried below the base with P' and the mirror triangle).
- C64 block 0 (equilateral reasoning) is optional, not required: pure reasoning, no construction, a careful student can follow the text. Its two book pictures (P18-shape-2 and P18-shape-3) are mapped none:TEXT_SUFFICIENT. If the team prefers a labelled equilateral triangle there, add one figure: ticks on all three sides, one arc at each corner.

1.4 C48 block 0 (AAS, the book's Fig. 1.2): I draw the QUESTION state of Fig. 1.2 (35, 75, 4 cm; the unknown angles at B and Y show "?"). The second book picture, with 70 degrees filled in (P15-shape-2), has no slot of its own, so it is mapped none:TEXT_SUFFICIENT (the values are in LP step 3).

1.5 C63 block 0 (altitude): the figure shows the altitude AD, the foot D and the right angle, with the two ticks; I left the 80 degree mark off. The altitude passes exactly through the place where "80 degrees" is written, the argument does not use it, and the book's own picture (P18-shape-1) leaves it off too. P17-shape-1 (the same triangle with 80 degrees and no altitude) is the question figure of C67, so it is mapped there.

1.6 Check questions that point at a teaching image (C47 "this crossing", C48 block 1 "this card", C64 block 2 "this sign", C65 block 1 "the bridge"): I treated them like the v3 'refer picture' case. C47, C48 block 1, C64 block 2 are `optional` (FIG_REFERENCED + REUSES_CONCEPT_IMAGE), no figure, and `text_alternative` gives the sentence that should carry the data (`needs_lp_text_sync: true`). C65 block 1 is `none` because the bridge is a photograph (NOT_RENDERABLE). C65 block 0 ("the five pictures") is `none`: four photographs and a rangoli design cannot be faked; the teaching image "Twins in the world" shows all five, so the five base figures are accounted to `concept_image:M4.S14.T14.C65.IMG1`.
The yes/no Chintu questions (C48 block 2, C60 block 2, C63 block 1), the torch-beam question (C46 block 1) and the "name the conditions" block (C61) are none, TEXT_SUFFICIENT.

1.7 Figures with no base figure: C46 block 0 (ASA construction), C64 block 1 (equilateral construction) and the four required solution figures have no printed picture in the book (the pdf has no solutions section and the book only says "construct"), so the validator warns "no inventory figure maps to it". That is expected. C60 block 1's figure continues P16-construction-1 and is mapped to it.

1.8 C59 solution: the book does not letter the crossing point of AC and DB, but the LP solution names O, so the solution figure letters it (in ANSWER). AC = DB is stated in the LP text but is NOT drawn as a mark: a tick pair on the long diagonals would sit on the same segments as the OA = OD and OB = OC ticks and be read as them. It follows from those ticks, and the render_note says so.

1.9 Arc and tick conventions in the solution figures (new equal parts in ANSWER, distinct counts per pair): midpoint figure one arc each at O, three ticks on AB and CD; FIO2 one arc (alternate DCO and BAO), two arcs (CDO and ABO), three arcs at O (COD and AOB), two ticks on OC and OA, three ticks on OD and OB (the given ticks on DC and AB stay one tick); FIO3 three arcs at A and D, BC highlighted with a FOCUS stroke; FIO4 one large arc over each whole angle, three small arcs at A and D, one tick on AB and DC, two on OB and OC, three on OA and OD.

1.10 Coordinates. The 47 degree pair and the AAS, ASA, RHS, equilateral and isosceles figures are drawn to scale from the given numbers (I recomputed every length and angle: 7 / 5 / 47 degrees, 35 + 75 + 70 = 180, AB = 5 sin30 / sin100 = 2.539 for the ASA construction, PQ = 3 for 4-5, apex 80 degrees with base about 1.68 times the height). The four geometry-proof figures (midpoint, parallel lines, kite, crossing lines) are NOT to scale (the book gives no lengths); they are drawn as exact symmetric figures so that every given equal mark is true, with proportions taken from the page pictures.

1.11 The base figure P12-shape-1 (the SSA pair PQR and PQS at the top of page 12) belongs to chunk B (concept C44 "The gate that lands twice"); I did not claim it.

## 2. Things in the LP that look wrong or thin

2.1 C67 question text: "Use that fact to find angle B and angle C when the angle at A is 80 degrees." It never says AB = AC or names the triangle; only the tick marks of the figure carry the equal sides, and "that fact" points back at the previous block. I flagged `needs_lp_text_sync` and gave the text to add ("Triangle ABC has AB = AC and the angle at A is 80 degrees ...").
2.2 Dangling references to teaching images: C47 block 0 ("You met this crossing earlier ... here"), C48 block 1 ("this card"), C64 block 2 ("this sign"), C65 block 1 ("Look at the bridge"), C65 block 0 ("each of the five pictures"). The question text lacks the data that only the picture carries; text sync is proposed for the first four (see `text_alternative`).
2.3 C67 / C68: the LP's `s_figure` hint says the solution figure has an altitude with 50 degrees at B and C, but the LP steps never use an altitude (they use the angle sum). I followed the steps.
2.4 C59 (FIO4) solution goes beyond the book: the book's question is only "Identify the equal parts in the following figure"; the LP asks to show angle ABC = angle DCB and adds an "Extra step": angle OBC = angle OCB so OB = OC. That uses "equal angles give equal sides", the converse of what the chapter proves (it only shows equal sides give equal angles). Mathematically true but not taught here; the teacher may want to cut or label it.
2.5 Numbering: the LP names the five questions of topic T12 "Q1 to Q5", but only Q2 to Q5 are the book's Figure it Out 1 to 4; "Q1" is the in-text midpoint question of page 12 (its `ncert_refs` is p12.midpoint, so no wrong number is stored).
2.6 C63 block 0 and C67 ask about the same 80 degree isosceles triangle (the block answers "angle B = angle C", C67 gives 50 degrees). Not an error, but the same picture appears twice (one figure per item, as the rules say).
2.7 C60 block 0 step 5 says PQ comes out as 3 cm: correct (Pythagoras), but it is not in the book; I drew and labelled it in ANSWER.
2.8 The LP uses a 5 cm base for the equilateral construction (C64 block 1); the book gives no length ("Verify this by construction"). Harmless; the figure follows the LP.

## 3. Where the book itself is unclear

3.1 Book Figure it Out question 2 (page 13 text, figure on page 14): the arrowhead-and-tick marks differ in order on the two sides (arrowhead then tick on DC, tick then arrowhead on AB). One arrowhead and one tick on each is what is meant; my spec uses the same order on both.
3.2 The book's triangles are not to scale (for the 47 degree pair, AB drawn about 1.5 times BC rather than 1.4); my figure is to scale from the numbers.
3.3 The in-text isosceles question on page 17 prints "angle A = 80" without a degree sign; the picture has 80 degrees.
3.4 The ASA text (page 12) and the equilateral "Verify this by construction" (page 19) print no figure at all; the LP steps are the only source for those two constructions.
3.5 The book's figure for the downward extension of the RHS arc (page 17 text) is missing; page 16's figure shows the line l with an arrow only upward. The LP step text (second landing at P') is the only source for it.
