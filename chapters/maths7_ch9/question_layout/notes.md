# Class 7 Ch 9 Geometric Twins (cbse_eng_maths7_ch9, live v59): question layout notes

Spec: `layout_spec.json`. Checked with `core/question_layout_live.py`.

**Media links are not broken, so the work went ahead.** Every concept that lists media lists only nodes named after itself, and the live integrity baseline reports nothing but the three "question image first" messages that the placeholders fix. One quirk is left as it is: four question concepts hold no media of their own (live C12 "Figure it Out 4", the first parts of C46 and C47, and C48), and the question blocks in them point at the video of the teaching concept next door (C9, C41, C43, C44), which serves those items in `video_coverage`. The engine keeps those pointers; the "needs a new video" count below does not include those four concepts.

## Result of `check`

22 question concepts in 6 Questions topics (4 existing, 2 new: after "Writing the Match Down" and after "Equal Sides, Equal Angles"). The engine reports 20 as new (13 parts split out of the 5 live multi-question concepts, 7 cut from teaching blocks) plus 2 kept. Tiers of the 20: 16 exercise, 4 prompt, 0 example (the book prints no labelled Example). 15 new videos needed; 3 live videos kept on the first part of a split (C11, C24, C33) and marked "needs refresh" because they cover several questions; 4 concepts have no video of their own (see above). 6 teaching concepts lose a block (C19 two, C20, C21, C30, C37, C42). Gates: coverage 15 to 0, skeleton 8 to 3, structure 0, video_script_rules 31 and objectives 2 unchanged. `INTEGRITY: clean`, no "GATES WORSE THAN LIVE" line.

## Which items count here

The book puts the "?" icon next to every in-text question (checked on PDF pages 1 to 21), so the icon decides nothing. I counted (a) all 18 Figure it Out items and (b) in-text problems that are stand-alone, on a printed figure, with a definite answer that the plan block works out. I did not count the in-text steps that build a rule or definition (SSS, SAS, SSA, ASA, AAS, RHS, AAA, isosceles, equilateral, the correspondence convention): they are the spine of their teaching concepts, are answered by the next sentence, and several are "construct and find out" tasks.

## New questions cut out of teaching concepts (7)

All have `keep_video_of: null`.

| Topic | New question concept | Book label or quote | Plan source (ref) | Tier | Why it counts |
|---|---|---|---|---|---|
| Writing the Match | Writing the Match: a pair in the rectangle | "Can you identify a pair of congruent triangles below? Why are they congruent?" (Fig 1.1, rectangle ABCD cut along BD) | M2.S6.T6.C19 b2 (p7.rect_pair) | prompt | Stand-alone figure question, definite answer (SSS, BD shared); plan tags the block `question`. |
| Writing the Match | Writing the Match: the right correspondence | "Can they be the following? A-C, B-B, D-D ... Identify the correct correspondence of vertices and express the congruence" | M2.S6.T6.C19 b3 (p8.correspondence) | prompt | Definite answer (A-C, B-D, D-B, triangle ABD congruent to CDB); block tagged `question`. Kept apart from the first because it asks something new about the same figure. |
| Writing the Match | Writing the Match: HEN and BIG | Figure it Out 1 (p8): "Suppose triangle HEN is congruent to triangle BIG. List all the other correct ways of expressing this congruence." | M2.S6.T6.C20 b0 (p8.FIO1), the exercise block of the Practice concept | exercise | Figure it Out item; the practice concept keeps its recap, watch-fors and tool. |
| Two Triangles Apart | Two Triangles Apart: the kite ABCD | Figure it Out 3 (p9): "AB = AD, CB = CD. Can you identify any pair of congruent triangles? ... Does AC divide the angles at A and C into two equal parts?" | M2.S7.T7.C21 b3 (p8.FIO3) | exercise | Figure it Out item with a printed figure. |
| Two Angles and a Side | Two Angles and a Side: the midpoint figure | p12: "In the figure, Point O is the midpoint of AD and BC. What can one say about the lengths AB and CD?" | M3.S10.T10.C30 b2 (p12.midpoint) | prompt | Stand-alone problem on a printed figure, worked in the book's next page; an application of SAS, not a rule being built. Placed first, before the section's Figure it Out. |
| Equal Sides, Equal Angles | Equal Sides: finding angles B and C | p18: "Can you use this fact to find angle B and angle C?" (isosceles, angle A = 80 degrees) | M4.S13.T13.C37 b4 (p18.isosceles_use) | prompt | A "find ..." put to the reader, definite answer (50 degrees each), and the book never prints it. The derivation block (b3) stays in teaching. |
| Putting the Rules to Work | Rules at Work: AB parallel to CD | Figure it Out 3 (p20): "It is given that OB = OC, and OA = OD. Show that AB is parallel to CD." | M4.S14.T14.C42 b3 (p20.FIO3) | exercise | Figure it Out item with a printed figure. |

## Existing question concepts, split or kept (15)

Splits replace the live concept in place; the first part keeps its video (refresh) and objective, later parts are enrichment concepts with no video. Names are page-free and number-free (see Judgement calls). All tier exercise.

| Topic | Live concept | Result |
|---|---|---|
| What Would You Measure? | C11 "Figure it Out 1, 2, 3" | split into: the two V-shaped figures (FIO 1, keeps video), which pairs are congruent (FIO 2), copying a circle and a rectangle (FIO 3) |
| What Would You Measure? | C12 "Figure it Out 4" | kept, renamed "What to Measure: three arms from a point" (FIO 4) |
| Pulling Two Triangles Apart | C24 "Figure it Out 2, 4" | split into: RED and JAM (FIO 2, keeps video), the arrowhead (FIO 4); the new kite question (FIO 3) goes before them |
| Two Angles and a Side | C33 "Figure it Out 1, 2, 3, 4" | split into: the 47 degree pair (keeps video), parallel lines AB and CD, the shared side BC, crossing lines AC and DB |
| Putting the Rules to Work | C46 "Figure it Out 1, 2" | split into: AIR and FLY (no video of its own), five cases of three facts |
| Putting the Rules to Work | C47 "Figure it Out 4, 5" | split into: the square ABCD (no video of its own), the centre of the circle |
| Putting the Rules to Work | C48 "Figure it Out 6" | kept, renamed "Rules at Work: the missing angles" |

Order in the last Questions topic is the book's: FIO 1, 2 (C46), 3 (new), 4, 5 (C47), 6 (C48). `q_figure` and `s_figure` are on every item whose printed question depends on a figure (checked against PDF pages 3, 4, 8, 9, 12 to 14, 17, 18, 20, 21), and on none that is text only for the question card (FIO 3 of the first set, HEN and BIG, and AIR and FLY have `s_figure` only).

## Borderline, not moved

- p1 "How do we do it?" and "Can we take some measurements ...?": framing discussion, no block.
- p1 "Are the arm lengths AB and BC sufficient ...?", p2 "Would it help to take any other measurement?" and "Can you draw the symbol if AB = 4 cm, BC = 8 cm, angle ABC = 80 degrees?" (p1.signboard, p2.angle, C4 b3 and b4): the opening discovery, answered by the next lines. The drawing task is the nearest candidate to promote (C4 b4).
- p3 "If both symbols have the same arm lengths, can it be concluded they are congruent?" (p3.arms, C8 b2): answered in the next sentence; spine of C8.
- p2 definition and p3 turned or flipped pairs (p2.definition, p3.moved_pairs): statements.
- p5 "Do you agree with Meera?" (p5.meera): prediction; the plan's own answer says so. p5 "Is this information sufficient ...? can you do so?" (p5.sss_468) and p6 "Examine whether triangle ABE and triangle ABF are congruent" (p6.abe_abf): the steps that establish SSS.
- p6 "Which vertices of triangle XYZ and triangle ABC should we overlap? Are there other ways?" (p6.overlap, C17 b3): introduces the correspondence convention; first half answered in the next sentence. Candidate to promote. p7 "incorrect to write triangle ACB congruent to XYZ" (p7.record), p8 "Verify by superimposing paper cutouts" (hands-on, merged into p8.correspondence in the plan), p8 free parts (p8.free_parts): statements or hands-on.
- AAA (p9.aaa), SAS (p10.sas), SSA (p10.ssa), ASA (p12.asa), RHS (p16.rhs, p17.arc): "construct and find out" steps whose result is the rule; several compare with classmates. AAS (p14.aas, C31 b3, "Are the triangles congruent? Give a reason") is a worked check with numbers (angle B = angle Y = 70 degrees, then ASA); the nearest of these to promote.
- p17 five conditions (p17.five_conditions): a list. p17 isosceles derivation (p17.isosceles, C37 b3), p18 equilateral (p18.equilateral, p19.equilateral_check, "Verify this by construction"): derivations.
- p20 "Describe the congruent triangles you see in each picture" (p20.world): open observation.
- p23 "Expression Engineer!" (p23.puzzle, in "Practice: Six Congruent Pieces", C50): a puzzle whose own answer says other layouts may work, and it sits in the Summary topic, which the engine cannot use as a source.

## Gaps

None. All 18 Figure it Out items (4 + 4 + 4 + 6) have a plan block, and the plan holds no block for any other counted book question.

## Judgement calls

1. **Names and `rename_teach`.** Every live question concept was named after the book's exercise numbers ("Figure it Out 1, 2, 3" and so on), and the new image placeholders take their titles from concept names ("<name>: question"). So all 22 question concepts now have a page-free, number-free name of the form `<Topic short>: <subject>`. The 13 split parts and 7 new questions are named in the spec; the two concepts that are kept, C12 and C48, are renamed through `rename_teach`. No teaching concept is named after a moved question, so `rename_teach` holds nothing else.
2. **Kite first in "Questions: Pulling Two Triangles Apart".** The book order is FIO 2, 3, 4, but a split replaces its concept in place and cannot straddle another question, and C24 holds FIO 2 and 4. I put FIO 3 (the kite, taught in C21) before the two. The alternative is FIO 2, 4, 3.
3. **FIO 1 of the second set** is cut from the Practice concept of "Writing the Match Down" and so lands in that topic's new Questions topic, although the book prints it with FIO 2 to 4. The plan itself places it there.
4. **Two rectangle questions, not one.** p7.rect_pair and p8.correspondence are two printed questions with two answers on one figure, so they stay two concepts, one ref each.
5. **The midpoint question is a prompt, not an example**, because it carries no "Example" label in the book (no labelled example exists in this chapter). It is the one in-text item moved from a block tagged `inline`; the rule for it is in "Which items count here".
6. **"Equal Sides: finding angles B and C"** is the weakest new item: its block says "Use that fact to find ...", so the question card must restate the isosceles fact it refers to. To drop it, delete the last entry of topic M4.S13.T13 (the topic then needs no Questions topic) and nothing else changes.
7. **FIO 4 of the first set**: the block says "each of the three pairs", but the printed figure shows one figure and two pairs of figures (PDF page 4). The kept concept cannot be dropped, so `q_figure` follows the book (two pairs); the question text itself should be corrected when the question card is written.
8. **FIO 6**: the plan works three instances (102, 73, 73 degrees, the 56 + 34 corner check) and says the rest come the same way; the figure has more missing angles. The solution card must work them all.
9. **Leading labels in block text.** The first block of C11, C12, C24, C33, C46, C47 and C48 has `text` and `publication_text` that begin with the old concept name ("Figure it Out 1, 2, 3: ..."). The engine does not rewrite block text, so those prefixes (book exercise numbers, no page numbers) should be dropped when the question cards are written.
10. After a block is cut, the teaching concepts keep their text, teaching plan, tool and video; the cut question has no video yet. The live teaching videos of C19, C21, C30, C37 and C42 still talk about the cut items.
