# Chunk D notes (Class 7 Ch 9 "Geometric Twins", units 70 to 81)

Topics: M4.S16.T16 (Putting the Rules to Work, 4 worked blocks), M4.S17.T17 (Figure it Out Q1 to Q6, 6 pairs), M5.S18.T18 (summary, Puzzle Time).
Result: 18 items. Required 9, optional 1, none 8. Validator: errors 0, warnings 0.

| Role | required | optional | none |
|---|---|---|---|
| question | 4 (Q3, Q4, Q5, Q6) | 0 | 2 (Q1, Q2) |
| solution | 4 (Q3, Q4, Q5, Q6) | 1 (Q2) | 1 (Q1) |
| worked_example | 1 (Puzzle, C87) | 0 | 5 (C69, C70 x2, C71, C86) |

Pages used (all looked at): 20, 21, 22, 23. The pdf has no printed-solutions section.
Base inventory check: P20-shape-1, P21-shape-1, P21-shape-2, P21-shape-3 and P23-grid-1 were compared with the page pictures (P21-shape-3 at 3x zoom: every angle number, tick group, right-angle square and the 16 inner segments agree). No "CORRECTED" needed.
Inventory entries: 5 base figures claimed by their question items, plus 4 `NEW-<base>-sol` entries (the same book picture used as the base of the solution diagram of Q3, Q4, Q5, Q6; there are no printed solutions, so these are solution re-uses, not new pictures). If the merge prefers no such entries, drop the four NEW- rows and the validator will only warn.

## 1. Judgement calls

- **Q1 (C74/C75) none/none.** No book figure; the answer is three pairings (vertices, sides, angles) read off the letter order. Text is complete. I did not make the solution optional: a picture would only repeat the pairings.
- **Q2 (C76/C77) question none, solution optional (not added).** The book prints only five lists of three equal parts, so no question figure. The LP answer is complete in words (rule, statement, "not guaranteed" for (e)). What would help: one row of five small two-triangle sketches that mark the three given parts and show whether the given angle sits between the two given sides (cases b, d, e). I chose optional rather than required because the answer is not itself a drawing; the LP steps say "sketch it" as advice to the learner, not as part of the answer. The question text is a run-on paragraph; `text_alternative` suggests a LaTeX array of five columns.
- **Q3 (C78/C79) required/required.** Book gives the bow-tie figure with ticks. Solution adds the two pairs of equal angles (one arc each for the vertically opposite angles at O, two arcs each for the alternate angles OAB and ODC): this is steps 2 and 5 of the LP. Kept in the question layout (companion note), not "triangles drawn apart" as the earlier hint s_figure said.
- **Q4 (C80/C81) required/required.** Q4 question is the weakest "required": the text says "ABCD is a square" and a careful learner could sketch it. I kept it required because the book gives the figure with the diagonal AC, the corner order matters for the two statements (ABC with ADC, and ABC with CDA), and Q3, Q5, Q6 (same set, book figure given) are required. If you prefer text-first, set the question to `none` / TEXT_SUFFICIENT and keep the solution; nothing else changes. Solution ticks: ONE tick on each of the four sides (a square has all four sides equal; different ticks on AB, AD and CB, CD would wrongly say AB is not BC), and a lone double tick on the diagonal AC for "the shared side, equal to itself".
- **Q5 (C82/C83) required/required.** Numeric answer (30 and 30), which the prompt's "typical pairs" treat as solution none when it adds nothing. Here the solution does add marks the LP steps use: the radii AB = AC (step 1) and the two 30 degree angles (step 3), and sibling consistency with Q3, Q4, Q6 points the same way. This is the item most likely to be turned to optional if the budget is tight.
- **Q6 (C84/C85) required/required, solution is partial.** The LP answer works only three angles (102 at K, 73 and 73 at the base of the one-tick triangle U-P1-P3) and says the rest come the same way. The solution figure shows exactly those three in ANSWER green, nothing else (no invented numbers). The book asks for all missing angles; the LP gives no full set. DECISION FOR THE USER: keep the three LP values (done), or have the LP solution extended to the full set and the figure redrawn.
- **S16 worked blocks (units 70 to 73) all none.** C69 "first thing to do with three facts", C70 "track-layer", C71 "how many ways": answered in words, no figure given. C70 block 1 (Chintu: AB and CD look the same length): refers to AB and CD but tests an idea (equal length does not prove parallel); the bow-tie is not needed to attempt it. Teaching images (tray and cards, railway lines, three tiles) are untouched and never linked.
- **Unit 80 (C86 summary) none.** Page 22 has no figure.
- **Unit 81 (Puzzle, C87) required, ONE diagram = the given grid only.** The block is a worked-example item (one diagram, token after the question text), so the picture is the learner's canvas: 5 x 5 grid, middle square blocked, no cut lines. A sample partition is not drawn because the LP answer gives no layout ("Other layouts may also work") and a drawn layout would sit before the answer. For the content team, in case a sample answer text is wanted: I searched all ways to cut the 24 white squares along grid lines into six congruent pieces; there are 40, every one uses six L-shaped four-square pieces, and 16 of them are unchanged by a half turn. One that needs no flipping (rows top to bottom, each letter is one piece, # is the blocked square): `ABBBC / ABCCC / AA#DD / EEEFD / EFFFD`. This assumes cuts along grid lines; the book does not say whether diagonal cuts are allowed.
- **Style choice for the blocked square:** the book shows it solid green with a thin red outline; the spec uses MARK_FILL with an INK outline (red is the WRONG token and may not be used here).
- **16:9 for every diagram**, also for the square grid and the circle (the pipeline draws cards 16:9; the figure is centred with margin).

## 2. Things in the LP that look wrong or thin

- Q6 solution (C85): partial answer, see above. Step 3 says "the corner of the rectangle: the two angles there are 56 and 34" without naming the corner (it is A).
- Q5 and Q6 LP steps: division written outside the maths, e.g. `$60$ / $2 = 30$` and `$(180 - 34)$ / $2 = 73$`; subtraction written with a hyphen (`180 - 120`). Cosmetic LaTeX; the figure and answers are right.
- C75 step 1: `A goes with $F$` (the first A is not in maths mode, the others are). Cosmetic.
- Earlier hints (`q_figure` / `s_figure`) are thin or off in places: Q6 hint omits the right-angle square at P2 and says "CDBA" without the unlettered inner dots; Q3 hint wants triangles drawn apart. They were treated as hints only.
- I re-checked every case of Q2 against the LP solution (rules and statements: a SSS DEF, b SAS EFD, c RHS FDE, d AAS DEF, e SSA not guaranteed): all correct. Q3 (SAS, AOB with DOC, then alternate angles OAB = ODC), Q4 (SSS; ABC with CDA by A to C, B to D, C to A) and Q5 (30 each) are also correct.
- C70 teaching text describes the crossing segments (bow-tie) only in words and asks the learner to draw it; its concept image is the railway picture. The first bow-tie figure in the plan is therefore the new Q3 question diagram (C78.IMG1) in the next topic. Nothing to fix; worth knowing when the teaching video is reviewed.
- Chunk-file `block_index` values (0, 0, 1, 0 in S16; 0 and 0 in S18) count question-bearing blocks of a concept, not positions in the LP content list (for example the C70 blocks sit at LP positions 3 and 6). I used the chunk file's values, as the brief says.

## 3. Where the book itself is unclear

- Q6 figure (page 21): the four inner dots have no letters (named P1 to P4 in the spec only, not drawn). Whether R-P1-P3-K is one bent line or one straight line cannot be told; drawn as three pieces (they bend, and the 44 degree mark at P3 needs the bend). R-P2-P4, A-P3-P2 and K-P4-F are drawn exactly straight (the picture is within 1 to 2 percent of straight). The figure is not exactly to scale: the printed angles differ from the angles measured on the picture by up to 3 degrees (for example 68 at V measures 65.2, the angle at K measures 100.8 against 102). The spec uses positions read off the picture, snapped for straightness, and keeps the printed numbers; `to_scale` is false.
- Q5 figure: no dot at the centre A (the book draws none); the spec follows.
- Q3 figure: the book draws C slightly lower than A and D slightly lower than B; the spec makes the figure exactly point-symmetric about O so that OA = OD and OB = OC hold, which keeps the picture believable and the same slant for AB and CD.
- Puzzle: see the cut-line assumption above.
