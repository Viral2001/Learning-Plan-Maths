# Class 7 Ch 5 Parallel and Intersecting Lines - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths7_ch5` v52 (taken from staging). Result: new V2 version v53 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (70 items from 39 units)
{"worked_example": {"optional": 2, "none": 1, "required": 5}, "question": {"required": 25, "none": 6}, "solution": {"required": 22, "optional": 5, "none": 4}}

Optional, NOT added: [('C3', 'worked_example'), ('C5', 'worked_example'), ('C10', 'solution'), ('C20', 'solution'), ('C30', 'solution'), ('C44', 'solution'), ('C49', 'solution')]

needs_lp_text_sync: [('C33', 'question'), ('C40', 'solution'), ('C41', 'question')]

## The 52 diagrams
| id | side | type |
|---|---|---|
| M1.S3.T3.C7.IMG1 | question | geometry_figure |
| M1.S3.T3.C8.IMG1 | solution | geometry_figure |
| M1.S4.T4.C9.IMG1 | question | geometry_figure |
| M1.S6.T6.C15.IMG1 | solution | geometry_figure |
| M2.S8.T8.C19.IMG1 | question | geometry_figure |
| M2.S8.T8.C21.IMG1 | question | geometry_figure |
| M2.S8.T8.C22.IMG1 | solution | geometry_figure |
| M2.S8.T8.C23.IMG1 | question | geometry_figure |
| M2.S8.T8.C24.IMG1 | solution | geometry_figure |
| M2.S9.T9.C27.IMG1 | worked example | geometry_figure |
| M2.S10.T10.C32.IMG1 | solution | geometry_figure |
| M2.S10.T10.C33.IMG1 | question | geometry_figure |
| M2.S10.T10.C34.IMG1 | solution | geometry_figure |
| M2.S11.T11.C35.IMG1 | question | geometry_figure |
| M2.S11.T11.C36.IMG1 | solution | geometry_figure |
| M2.S11.T11.C37.IMG1 | question | geometry_figure |
| M2.S11.T11.C38.IMG1 | solution | geometry_figure |
| M2.S11.T11.C40.IMG1 | solution | geometry_figure |
| M2.S11.T11.C41.IMG1 | question | geometry_figure |
| M2.S11.T11.C42.IMG1 | solution | geometry_figure |
| M2.S11.T11.C43.IMG1 | question | geometry_figure |
| M3.S12.T12.C46.IMG2 | worked example | geometry_figure |
| M3.S13.T13.C48.IMG1 | question | geometry_figure |
| M3.S14.T14.C51.IMG2 | worked example | geometry_figure |
| M3.S14.T14.C52.IMG1 | worked example | geometry_figure |
| M3.S15.T15.C54.IMG1 | question | geometry_figure |
| M3.S15.T15.C55.IMG1 | solution | geometry_figure |
| M4.S17.T17.C59.IMG1 | solution | geometry_figure |
| M4.S17.T17.C61.IMG1 | solution | geometry_figure |
| M4.S17.T17.C62.IMG1 | question | other |
| M4.S17.T17.C63.IMG1 | solution | other |
| M4.S18.T18.C64.IMG1 | question | construction |
| M4.S18.T18.C65.IMG1 | solution | construction |
| M5.S20.T20.C70.IMG1 | question | geometry_figure |
| M5.S20.T20.C71.IMG1 | solution | geometry_figure |
| M5.S21.T21.C72.IMG1 | question | geometry_figure |
| M5.S21.T21.C73.IMG1 | solution | geometry_figure |
| M5.S21.T21.C74.IMG1 | question | geometry_figure |
| M5.S21.T21.C75.IMG1 | solution | geometry_figure |
| M5.S23.T23.C79.IMG1 | question | geometry_figure |
| M5.S23.T23.C80.IMG1 | solution | geometry_figure |
| M5.S23.T23.C81.IMG1 | question | geometry_figure |
| M5.S23.T23.C82.IMG1 | solution | geometry_figure |
| M5.S24.T24.C83.IMG1 | question | geometry_figure |
| M5.S24.T24.C85.IMG1 | question | geometry_figure |
| M5.S24.T24.C87.IMG1 | question | geometry_figure |
| M5.S24.T24.C89.IMG1 | question | geometry_figure |
| M5.S24.T24.C90.IMG1 | solution | geometry_figure |
| M5.S24.T24.C91.IMG1 | question | geometry_figure |
| M5.S24.T24.C93.IMG1 | question | geometry_figure |
| M5.S24.T24.C94.IMG1 | solution | geometry_figure |
| M6.S25.T25.C95.IMG2 | worked example | other |

### Chunk A notes (from the decision agent)
# Notes for chunk A (Class 7 Ch 5, sections 5.1 to 5.4, topics M1.S2.T2 to M2.S11.T11)

Result: 18 units, 32 items. Required 21 (questions 10, solutions 10, worked example 1), optional 6, none 5. Validator: errors 0, one warning (M2.S10.T10.C32 solution has no base figure because the book prints no picture for that answer; allowed).

How the numbers were made: every dot, endpoint and shape corner was measured from the page pictures (dot detection on the page PNGs, overlay checks on Fig. 5.6, Fig. 5.12 and Fig. 5.13). Angles, parallel pairs, crossings, perpendicular corners and counts in the specs were recomputed in a script kept outside HERE (scratchpad `c7ch5A/build_out_A.py`). The pdf does have a printed-answers section after the chapter (pdf pages 22 to 34, "Page No. ..."), although the brief says it has none; I used its answer pictures (pages 26 to 29).

## 1. Judgement calls

- **M1.S2.T2.C3 and C5 (worked, optional).** Both examples are invented (63/117 pairs; a = 35), the book prints no figure for them, and the text gives the angle names and values in order. Rule used: a question or worked-example figure is required only when the book supplies a figure the learner needs; otherwise it would be an invented figure. A crossing would help, so `optional`, not added.
- **M1.S3.T3 (a = 120, Fig. 5.2).** Question required (the book question is about the lettered Fig. 5.2). Solution also required, which is borderline: the answer is numeric, but it fills three new values (b = 60, c = 120, d = 60) at their places on the crossing, so I treated it as a filled figure (B2). With a stricter reading this solution (C8) would become optional, like C20 and C44.
- **M1.S4.T4 (Fig. 5.3 lists).** Question required. Solution `optional`: the printed answer is a text table, and the four linear pairs overlap (each angle is in two of them), so one figure cannot mark them cleanly. The book's red/black arcs (a, c red; b, d black) are drawn all INK in the question figure, because colouring the pairs would give the answer away.
- **M2.S8.T8.C23/C24 (Fig. 5.6) vs M1.S4.T4.C10.** The answer to Fig. 5.6 is four disjoint groups (a, h, i; c and g; d and f; b and e), so colouring them on the figure is clean, and I made the solution required (HIGHLIGHT_MEANING). The Fig. 5.3 answer is an identification too but with overlapping pairs, hence optional. Say if you want both treated the same way.
- **M1.S6.T6 (all four angles equal).** Question has no figure (none). The solution is required: the book's question is "Can you draw a pair of intersecting lines...", answered by Fig. 5.4 (tilted pair, one square). The LP rewrote the question as "find each angle and name the lines", and its steps end on "perpendicular, however tilted", so I draw the tilted pair with one square and 90° in each angle. Stand-alone figure (derived_from null).
- **M2.S8.T8.C19 (Fig. 5.5, five pairs) and C21 (ST, UV, OP, QR).** Both questions are about Fig. 5.5. C19 gets all ten segments with the 115.3° arc (the book figure), C21 gets only ST/UV and OP/QR at the same coordinates ("two more pairs are drawn"), on a wider canvas that leaves room for the solution extensions. Given numbers that only the LP text carries (60°, 80° at X and Y; 30°, 29°, 33° in Q5) are not put on the question figures, as in the book.
- **M2.S8.T8.C20 (solution of C19), optional.** The 60° and 80° are already in the question text, and the answer is one sentence per pair; a copy with two arcs would only write given numbers on the figure. The same reason makes **M2.S11.T11.C44 (Fig. 5.13 answer) optional**. A drawn midpoint tick was rejected: X lies only 0.37 units from the midpoint of CD in the picture, so ticks would suggest X is the midpoint.
- **M2.S8.T8.C22 (solution of C21), required.** The answer is a construction: ST and UV extended with dashed lines to their meeting point K, OP and QR extended and staying apart. Geometry is from the picture (UV rises 2.4° more steeply than ST, so K lies 3.2 segment lengths beyond T, 4.2 from S). The LP says "about four lengths beyond the ends"; the figure gives about three beyond the ends (about four from the start). The drawing follows the figure.
- **M2.S9.T9.C27 (worked, notation).** Required. The concept has no teaching image and the example's answer is a marked drawing. For a worked example the one diagram sits before the steps, so it shows the finished marking (one arrow on each flat line, two on each slanting line, a square at the right angle, no "90°" text). This leaks the answer of the example's question, deliberately, because the steps follow immediately; an unmarked drawing would leave the steps without anything to point at. If you prefer the unmarked drawing, drop the added ANSWER marks. The LP says the upright line "crosses a flat line"; it is drawn crossing the lower flat line only.
- **M2.S10.T10.C29/C30 vs C31/C32 (Activity 2).** Questions: none (no figure is given in the LP text). C30 optional (answer is the pattern 3, 5, 9, 17; a row of four creased squares would help, the first three squares are the teaching image of the earlier topic). C32 required: the answer is a fold (which corner, where the crease lies), so it is drawn: crease from (0, -3) to (3, 0) on a sheet of side 6, perpendicular bisector of the corner-to-centre segment, with the two right-angle squares and arrow marks that carry the LP's argument.
- **M2.S10.T10.C33/C34 (Fig. 5.8).** One figure: the last stage (folded sheet, lower-left panel of the book picture), drawn to scale on a sheet of side 8 (flap legs 2). The book sketch is not to scale and in it c and r are not exactly parallel; here a and p are upright, b and q flat, c and r both direction (1, -1). Earlier stages are in the question text and not repeated. `needs_lp_text_sync` is true on C33 (see 2).
- **M2.S11.T11.C35/C36 (Fig. 5.10).** The book prints 6 columns at equal spacing as one sheet (checked by dot detection: spacing 62 px, no gap; the base note for P26 claiming a gap is corrected in the inventory). The LP calls the left and right 3 columns "two grids". I kept the book's equal spacing. In the solution the perpendicular for the 2-across-3-down segment is not drawn, as the LP says; the book's printed answer draws a fourth segment that is not exactly perpendicular. The 2-across-2-down perpendicular is drawn in full through the middle dot (the LP says "segments of 2 across and 2 down"); the book draws only its lower half.
- **M2.S11.T11.C37/C38 (Fig. 5.11).** Solution follows the LP text, which differs from the printed answer in two places: LP puts the single arrow on the flat sides of shape 2 (book: double there); LP counts two right angles in shape 3, at (7, 8) and at (5, 6) (book marks only (7, 8)). The (5, 6) angle lies outside the hexagon, between its flat and upright edges; the square is drawn there. Seven squares and 30 chevrons on 18 marked edges, all recomputed from the vertices.
- **M2.S11.T11.C39/C40 (Q3).** Question none: this pdf prints no dot paper under Q3 (page 8 ends with the question text, page 9 starts with Q4), and an empty grid would only imply a given figure. Solution required: the printed answer is a picture. The LP gives only the kinds of sets (flat, upright, leaning), so I drew the book's printed sample (four pairs) in ANSWER green and set `needs_lp_text_sync` true so the text can say "pairs".
- **M2.S11.T11.C41/C42 (Fig. 5.12).** Segments of the answer are the book's printed red lines (checked parallel by steps). Several are longer than the given segment (for example the parallel to e is 2 across 6 down, the given e is 1 across 3 down): same steps repeated, not the same length. `needs_lp_text_sync` true on C41 (13 by 14, see 2).
- **Aspect ratio.** 16:9 for line figures; 1:1 for the square sheets (C32, C33/C34) and the 12 by 12 and 13 by 14 grids (C37/C38, C40, C41/C42), because a 16:9 card would shrink them. Change to 16:9 if the pipeline insists on 16:9 cards.
- **Inventory.** The 30 base figures of pages 1 to 9 and 22 to 29 are all claimed, plus 5 `NEW-` entries for second uses (solution figures of C8, C22, C24, C34 and question 2 of Fig. 5.5). Reprints of chapter figures on the printed-answer pages are `none:SAME_AS_QUESTION_DIAGRAM` (P22-intersecting_lines-1, P23, P25, P26-dot_lines-1, P27-grid_shapes-1, P28-dot_lines-2, P29-dot_lines-2); the reprint of Fig. 5.7 (P24) is mapped to the same concept image as the original. P01 (Fig. 5.1, section 5.1 topic M1.S1.T1, which has no question unit) is claimed here as `concept_image:M1.S1.T1.C1.IMG1` so the merged map does not lose it; the two photo panels of p.5 are NOT_RENDERABLE and the artwork DECORATIVE_ONLY.

## 2. Things in the LP that look wrong

- **C33 (Q3 of 5.4, Fig. 5.8).** The text says the sheet is "folded in the middle both ways" and the corners are folded "onto a centre crease". The book (and the answer: a and p lie on parallel lines, b and q are perpendicular to them) has only upright creases at one quarter, one half and three quarters; the corners are folded onto the first and third creases, not the centre one. Flagged `needs_lp_text_sync`.
- **C41 (Fig. 5.12).** "13 dots by 13 dots": the picture has 13 columns by 14 rows (the parallel to h needs row 13). Flagged `needs_lp_text_sync`.
- **C35/C36 (Fig. 5.10).** "Two grids": the book prints one evenly spaced 6-by-4 sheet. The claim that the perpendicular of 2 across 3 down cannot be drawn only holds if each group of 3 columns is a separate grid; on the whole sheet a 3-across-2-up segment would fit elsewhere.
- **C37/C38.** Differences from the printed answer listed above (shape 2 arrow counts, shape 3 right angle at (5, 6)).
- **C22.** "About four lengths of the segment beyond the ends": measured 3.2 beyond T and 3.1 beyond V (4.2 and 4.1 from S and U).
- **C14/C15.** Question rewritten from "can you draw..." to "find each angle..."; the answer is still the book's drawing.
- **C7, C9.** The LP text dropped the explicit "in Fig. 5.2" / "in Fig. 5.3"; the figures are needed all the same (the book question is about them).
- **C19.** Says five pairs are drawn but gives data for three; ST/UV and OP/QR are answered in the next question (C21). Not an error, only two questions on one figure.
- **C32.** "Fold the corner that is not on the diagonal": a square has two such corners; the figure uses (3, -3).
- **C30.** The LP count 3, 5, 9, 17 is right (2^n + 1 with the two edges); the book's printed answer says "the pattern is 2n + 1", which gives 7 for n = 3, not 9. The book is wrong here, the LP is fine.

## 3. Places where the book itself is unclear

- Fig. 5.5 is a loose scatter with no scale: all coordinates are measured; whether X and Y are exact midpoints is not stated (X is 61 percent along AB and 56 percent along CD, Y 55 and 46 percent), and 115.3° measures 114.3° on the picture (G moved by under 0.1 units to make it exact).
- Fig. 5.8: the sketch is not to scale and its flaps are not exactly isosceles; right-hand panel of the last row is too small to read, the left-hand one is used.
- Q3 of Figure it Out: no dot paper printed.
- Fig. 5.13: the steep segment has no letter; b and c were told apart by label position, and the measured angles with the steep line (30.3°, 29.0°, 32.9°) match the LP's 30°, 29°, 33°.
- Fig. 5.6: label positions of g and f were checked against an overlay of the segment coordinates; the segments themselves are certain.
- The book prints no answer at all for the Fig. 5.5 questions, and its answer to the fold-parallel-to-diagonal activity is text only (no picture).

### Chunk B notes (from the decision agent)
# Notes for chunk B (units 19-32: topics T12, T13, T14, T15, T17, T18, T20, T21, T23; book sections 5.5 to 5.8)

Result: 25 items = required 22 / optional 1 / none 2. Validator: errors 0, warnings 0.
Required: 3 worked examples (C46, C51, C52), 9 question diagrams, 10 solution diagrams. All figures are drawn to scale and every angle value in them was recomputed from the coordinates (see each item's `accuracy_checks`). Scripts are in the scratchpad, not in HERE.

## 1. Judgement calls

1. **Rule used for geometry items.** A question or worked example that works with named or numbered angles or points of a given configuration (Fig. 5.14, 5.17, 5.19, 5.23 to 5.29) gets its figure, even when the LP wording describes the corners in words ("a is top left ..."). The v3 table gives "transversal angles" as its own example of SPATIAL_GEOMETRY, and the letters/numbers mean nothing without the picture. A question that gives no figure and asks the learner to draw (set-square questions) gets no question figure.
2. **T13 Q1 (C48, "can all eight angles differ?") = required, T13 solution (C49) = optional.** The book prints Fig. 5.14 with the question and the LP text only restates it. The solution would only colour the four opposite pairs that the steps already list, and the printed answer is words only, so it is `optional` (figure that would help: Fig. 5.14 with the pairs 1-3, 2-4, 5-7, 6-8 in matching colours). Everything else in chunk B whose solution adds numbers or marks on the figure is `required`.
3. **C46 worked example (corresponding angles of 2, 3, 4) = required.** The text says "in the transversal figure" and gives only "1 and 5 in the same corner". Which corner holds 2, 3, 4 is only in the figure. The figure shows the numbering only (no answer pairs, no colours). The same picture is C48's question diagram (identical spec, `render_note` says "same as").
4. **C51 worked example (a = 65 degrees) = required.** The text names a and b and the arrow marks. The figure is Fig. 5.19 with a = 65 degrees at l and an unmarked b at m. The LP text does not say which of the four angles at l is a; I put a in the upper-right corner as the book does. The answer (65, 65, 115, 115) does not depend on the corner. Existing teaching image C51.IMG1 is not linked; the example gets its own C51.IMG2.
5. **C52 worked example (lines leaning 10 degrees apart) = required.** "m leans 10 degrees more towards t than l does" and "on the matching side" can hardly be read without a picture. Drawn: l at 0 degrees, m at +10 degrees, t at +30 degrees, so the upper-right corners are 30 degrees at l and 20 degrees at m. "The matching side" is not named in the LP, so I chose the upper-right corner. The second position of t (50 and 40 degrees) is not drawn (question side shows only what is given). This is the item I was least sure about: it could also be `optional`, because all four numbers are in the text.
6. **T17 Q1 and Q2 (set square, 90 and 45 degrees) = none on the question side, required on the solution side.** The book gives no figure with these questions (Fig. 5.21 and 5.22 only show how to do it), and the learner draws the lines. The solution is a drawing (ANSWER_IS_FIGURE): l, the two lines and the marked corresponding angles. The two siblings have the same decision. The ruler and set square clip art is not redrawn.
7. **T17 Q3 (folding) and FiO 5.7 Q1 = question figure required.** Both give a line (crease) l and a point A to act on, so both have the question figure (sibling consistency). Their solutions are required and `derived_from` the question diagram.
8. **FiO 5.7 Q1 solution.** The printed answer is a clip-art picture (ruler plus set square sliding to A). Only the final line through A with parallel marks is drawn; the tools are left out (decorative clip art, and the set square would not fit the layout). The steps describe the method in text.
9. **Parallel marks.** Added on l and m wherever the question says the lines are parallel (Fig. 5.25, 5.28, and the Activity 3 solution, Fig. 5.18), although the book omits them there. Not drawn when the lines are not parallel (Fig. 5.14, 5.20-type C52, Fig. 5.27).
10. **Highlighting in solutions.** C75 (Example 2) shades the corresponding pair b and f; C80 (Example 3) shades the interior pair 3 and 6. Both use MARK_FILL (no extra words). C63 marks both right angles (see section 3, point 3).
11. **Figure inventory choices.** 20 base figures plus 5 `NEW-` entries for second uses (the solution diagram of Fig. 5.25 to 5.29). A reprint on the printed-answers page maps to the same item as its original (P30-construction_given-2 with P14-construction_given-1; P30-transversal_figure-1 is the T13 question figure while P10 is used for the worked example of C46). Fig. 5.15 and 5.16 (early steps of Activity 3) map to the concept image C50.IMG1 that shows the finished construction. The teaching images themselves are never linked.
12. **Media ids.** C46 and C51 keep their teaching image IMG1, so the worked-example diagrams are IMG2. Every other id is IMG1 (kept lists are empty).

## 2. Things in the LP that look wrong or thin

- **Video ids that point to another concept.** The answer item of C61 (T17 Q2) carries `video_media_id` "M4.S17.T17.C62.VID1" and the answer item of C65 (FiO 5.7 Q1) carries "M4.S18.T18.C66.VID1" (concept numbers C62 and C66, not C61 and C65). Probably a video concept placed after the answer, but worth a check in the build.
- **C46 worked-example text** gives "1 and 5 in the same corner" but not the direction of numbering. The figure fixes it (clockwise from top-left), no text change needed.
- **C51 text** does not say in which corner a lies (see 1.4); **C52 text** says "on the matching side" without naming the corner (see 1.5).
- **Example 4 (C81/C82).** The LP asks for DAB as well as CAB, ABC and BCD (the book asks only for the last three). DAB = 120 is an intermediate step of the book's solution; the solution figure marks it, which is consistent with the LP text.
- **FiO 5.7 Q1 (C65) step 6** ("the set square did not turn ... corresponding angles are equal") is an LP addition that the book's printed answer does not have. Not wrong.
- **LP text of T13 Q1 (C48/C49)** is long only because it describes the figure in words; with the figure drawn nothing has to change (no text sync needed).
- The solution `steps_tex` of every required item still start with step 1 as normal text; the builder puts the token before it.

## 3. Places where the book itself is unclear

1. **The pdf does have printed answers** (pages 22 to 34), although the brief says the pdf has none. I used the pictures on pages 30 and 31 (reprint of Fig. 5.14, reprint of Fig. 5.23, the ruler-and-set-square answer picture, the reprint of Fig. 5.24) and the answer text; where the LP and the book answer agree there was nothing to choose.
2. **Fig. 5.24 (folding) is inconsistent between panels**: A is at about 85 percent of the width in the second panel but on the vertical crease t at about 70 percent in the third and fourth panels. One position (70 percent) is used in the question and solution figures so that t can pass through A.
3. **Fig. 5.24, fourth panel** marks only the right angle where t crosses l; the LP solution says t crosses both l and m at 90 degrees, so both right angles are marked (the LP wins).
4. **Fig. 5.18** (Activity 3, step 4) shows no parallel marks although the text says the lines look parallel; the solution figure adds them because the LP solution ends with "So l and m are parallel".
5. **Fig. 5.21 and 5.22** are clip art with tilted rulers; the drawn lines do not look exactly 90 degrees (5.21) or 45 degrees (5.22). The figures I specify are exact and clean (right-angle squares, arcs with the values the LP gives).
6. **Fig. 5.25, 5.28** carry no parallel marks although the text says "parallel"; **Fig. 5.25** shows l and m with a slight slope, **Fig. 5.14** shows l and m converging (not parallel). Reproduced as printed (slopes), with marks added only where the text states parallel.
7. **Fig. 5.20** (Activity 5) is two non-parallel lines with no transversal; no item gives the learner this exact figure, so it is only the base of the C52 worked-example figure.
8. **Fig. 5.26 numbering**: the printed numbers sit left, top, right and bottom of each crossing (not at the four corners as in Fig. 5.14, 5.17, 5.28). The LP text agrees with this reading (2 corresponds to 6, 6 and 8 are opposite, 5 and 6 are a linear pair). The figure keeps the book's left/top/right/bottom placement and its angles (135 degrees top and bottom, 45 degrees left and right).

### Chunk C notes (from the decision agent)
# Chunk C notes (Class 7 Ch 5, Figure it Out 5.8 Q1-Q6 and Parallel Illusions)

Result: 13 items, required 8 (Q1-Q6 question side, Q4 solution, Q6 solution), optional 1 (worked example C95), none 4 (solutions of Q1, Q2, Q3, Q5). Validator: errors 0, 2 warnings (see 2.7).
Figures claimed: 41 (19 to items, 1 to the concept image of C95, 21 none).

## 1. Judgement calls

1.1 One card for several figures (Q1, Q2, Q3). The question of Q1 holds ten figures (a)-(j), Q2 four, Q3 two, all in ONE block and ONE card per pair side (run brief: at most one question diagram and one solution diagram per pair). So each question gets one 16:9 card holding all its figures: Q1 as a 4 x 3 grid (panels i and j centred in the last row), Q2 as 2 x 2, Q3 as 1 x 2. Labels are 34 px (the minimum), so Q1 is dense (panels about 350 x 300 px). Panel letters (a)-(j) are NOT drawn: the unknown angle carries its own letter a to j. If the user prefers two cards for Q1 (a-e, f-j), the pair would need a second media id: not allowed by this run's rule, so left as one.

1.2 Solutions of Q1, Q2, Q3, Q5 = none (SAME_AS_QUESTION_DIAGRAM). The printed answers are plain numbers for angles already marked with their letters in the question figures (the book's solution pages (pp. 32-34) only reprint the question figures and give the answer as text). Q4 and Q6 solutions = required because they add things the question figure does not have: Q4 marks the three unmarked angles at E (45, 57, 78); Q6 draws the two helper lines through N and O (the book's hint) and the angles 40, 56, 56, 52 and 108. Weak spot: a few LP steps use an angle that is not marked in the question figure (Q1 (j) "the corresponding angle of 97", Q2 (ii) "the corresponding angle of 62", Q2 (iii) "the rest of the 110 is 75"). I kept `none` ("prefer none"); if the user wants these explained visually, the solution cards of Q1 and Q2 could be filled-in copies of the question cards (derived_from Q1/Q2).

1.3 Worked example "Lines that look bent" (C95) = optional, no image. The text already describes the picture (two upright lines through a burst of spokes) and the teaching image of the same concept (C95.IMG1, left panel "Looks bent") shows exactly this illusion; the question can be answered from the text. The figure that would help is the first book illusion (8 lines through a centre, two thin upright parallel lines). Not lettered, so the "lettered figure is always drawn" rule does not apply. To flip: make it required with a `geometry_figure`/`other` spec (8 thick lines through one point at 22.5 degree steps, two thin vertical lines, one a little left and one a little right of the centre).

1.4 Illusions 2 and 3 of the book (p.20): not used by the LP. P20-illusion-4 (dense black strokes) = none:NOT_RENDERABLE; P20-illusion-5 (radiating lines + two horizontals) = none:OPEN_ENDED (the book's open question "What causes these illusions?"). P20-illusion-3 = concept_image:M6.S25.T25.C95.IMG1 (accounting only).

1.5 Geometry is redrawn to the printed numbers, not to the book's pictures. The book figures are not to scale, and a diagram must not contradict its marks. Every arc in my specs is drawn at exactly the value printed (given) or the answer (unknown, label shows the letter only). Changes against the book pictures: (a) drawn 48 (book picture about 55); (b) 52; (d) 99/81; (e) 97/83/69; (g) 122/58 at 32 degrees; (i) 70/54/56 (line 2 at 56); (j) the printed 27, 97 and 124 cannot all hold with the slopes the book draws (parallels about 54 degrees): with the parallels at 45 degrees the transversals are at -38 and -11 degrees, which gives 27 = 38 - 11, 97 = 180 - 38 - 45 and 124 = 180 - 11 - 45, so (j) is drawn that way; Q2 (iii) the two crossing lines at 110 and 75 degrees (book draws the second almost vertical) so that 110 - 35 = 75 holds exactly; Q4 the lines at 102 and 45 degrees through E; Q5 the slanted line at 35 degrees; Q6 parallels leaning at 95 degrees. Line lengths and label positions follow the book approximately.

1.6 Q6 arcs at N (96) and at O (a/108) are drawn larger than the book's (radius 20 and 18 units) so that the solution figure can put small green arcs inside them; the same arcs and label positions are used in question and solution (derived_from Q6).

1.7 The three Q1 panels where the book prints more marks than the LP text mentions are drawn as the book prints them: (c) shows 99 and 81 (LP text names only 99), (d) shows 81 and 99 (LP text names only 81), (g) shows 58, 122, 122, 58 at the right line.

1.8 Sibling rule: Q1, Q2, Q3, Q5 solutions all none; Q4, Q6 required, each with the reason in `reason`.

## 2. Things in the LP that look wrong

2.1 Q1 (a): text and solution say 48 and a are CORRESPONDING angles. In the book figure they are ALTERNATE interior angles (48 is inside the strip on the right of the transversal at the upper line, a is inside the strip on the left at the lower line). The value a = 48 is right; the word should be "alternate angles" (the LP solution step and the question text both).

2.2 Q4: the question text says "the rays EH and EF go up from E on one side". In the book figure H and F are BELOW the lower line, so the rays go down from E. The order G, H, F, D is right. Suggest "go down from E".

2.3 Q3 (i): text and solution say "a right angle is split into 65 and x". In the figure x is the angle at the lower left, vertically opposite to the 25 degree part (90 - 65) of the right angle, not the part itself; y (at the upper line, 155) is the supplement of that 25. Values 25 and 155 are right; the wording "linear pair with x" holds only through the vertically opposite angle.

2.4 Q3 (ii): the text says "two lines cross above a lower line", but the figure has two horizontal parallel lines and the two lines meet exactly on the UPPER one. The answer 78 - 53 = 25 is right.

2.5 Q2 (i): "angle a is its interior partner on the same side" of the 42 degree angle: the 42 is above the upper line; a + 42 = 180 holds through the vertically opposite angle at the upper line. Value 138 right.

2.6 Answer concepts carry `video_media_id` numbered after the NEXT concept: C84 -> M5.S24.T24.C85.VID1, C86 -> C87.VID1, C88 -> C89.VID1, C90 -> C91.VID1, C92 -> C93.VID1, C94 -> C95.VID1, while C85, C87, C89, C91, C93, C95 are the next question concepts (C95 is the Parallel Illusions concept in another topic). Looks like an off-by-one id scheme for the videos; harmless for diagrams (media ids .VIDn vs .IMGn) but worth a look.

2.7 Validator warnings: M5.S24.T24.C90 and M5.S24.T24.C94 (solutions of Q4 and Q6) are required but no printed figure maps to them: the book prints no answer picture (pp. 33-34 reprint the question figures with text answers), so these two figures are new, built from the LP solution text.

## 3. Where the book itself is unclear

3.1 The book's figures are not to scale (see 1.5); in (j) the printed angles are mutually inconsistent with the drawn slopes. The numbers were followed.

3.2 Q5: the text says EA is perpendicular to AB, but no right-angle square is drawn at A (the horizontal line ACE is simply drawn across the three vertical lines). The spec draws no square; x and y do not depend on it. The letter F is a loose letter near the bottom of the right line (no dot).

3.3 Q4: the book marks only 78 at K and 45 at B; the angles GEH, HEF, FED are named only by letters, which is why the solution figure marks them.

3.4 Q1 (c) and (d): the book prints the pair 99/81 once above and once below; the LP text mentions only one of them each time (see 1.7).

3.5 Page 20 prints three illusions under "Parallel Illusions"; the LP block covers the first only.
