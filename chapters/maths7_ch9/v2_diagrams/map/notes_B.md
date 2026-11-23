# Notes for chunk B (Class 7 Ch 9, Geometric Twins): topics M2.S6.T6, M2.S7.T7, M2.S8.T8, M2.S9.T9, M3.S10.T10

Result: 28 items = required 14 (question 5, solution 5, worked example 4) / optional 2 / none 12. Validator: errors 0, 1 warning (C43 worked example: required, no printed book figure, which is allowed).
All diagrams are 16:9 geometry figures (the AAA strip is wide, about 18 by 3 units; its angle labels are 0.4 high).

## 1. Judgement calls I was unsure about

Question side
- M2.S7.T7.C27 (Q1, rectangle cut along BD): REQUIRED, but borderline. The LP text describes the rectangle in words (a careful pupil could draw it), but the book prints Fig. 1.1 with the question ("below") and the answer is read off it (triangles ABD / CDB, opposite sides, shared BD). If the user wants text-first, switch C27 to none (TEXT_SUFFICIENT); C28 would then stand alone (it already draws everything).
- M2.S9.T9.C38 (RED and JAM): REQUIRED, but borderline for the same reason: every length is in the LP text, yet the book gives the two triangles as a figure and the corner matching (R between the 3.5 and 6 sides, so J) is worked on the picture. Kept required for sibling consistency with the kite and arrowhead questions of the same set.
- M2.S7.T7.C29 (Q2, correspondence): REQUIRED because the LP text never says which triangles (see 2). The picture is the same Fig. 1.1 as C27 (identical spec; the book's two-column table P08-table-1 is plain text, LATEX_TABLE, and is not drawn).
- M2.S9.T9.C36 (kite) and C40 (arrowhead): required; the figure carries which segments exist (dashed AC, no BD; DE drawn, no FG) and the tick marks.
- M2.S7.T7.C31 / C32 (HEN, BIG): none / none. No figure anywhere; the answer is five written statements (LaTeX list given in text_alternative).

Solution side
- C28, C30, C37, C39, C41 required: the chapter's method is "pull apart, mark what you know, count"; the LP solutions all start by pulling the figure apart and then mark equal sides, so the pulled-apart pair with its marks is the final state. Given ticks stay INK, ticks added by the solution are ANSWER. Each solution has derived_from = its question figure.
- C30 and C39 (the answer IS a correspondence): the LP hint says "corresponding vertices joined by lines". In this layout lines would run through the neighbouring triangle (I checked: no translation of one triangle makes all three joins clear of both), so the three matching corner pairs get matching dot colours instead (SET_A blue, SET_B amber, FOCUS pink). The ticks keep the figure readable without colour. If the reviewer prefers joining lines, the spec must change to curved connectors.
- The pulled-apart rectangle (C28, C30) keeps the orientation of Fig. 1.1 and just moves the halves apart (the unmarked paper cut-outs on p.8 look like this).

Worked examples (single diagram, token after the question text)
- C23 block 0: required (the example is worked on the p.6 picture; bars are the data). The picture is redrawn so that the ONE-bar side is the SHORTEST, as the LP steps say; in the book picture the two-bar side AB is the shortest (see 3).
- C42 block 0 (AAA), C43 block 0 (SAS), C44 block 0 (SSA): required as ANSWER_IS_FIGURE, the same way earlier chapters treated "construct / draw" examples (Class 8 Ch 11 C39, Class 6 Ch 8 C44): the single figure is the finished picture, even though its token sits after the question text. C42 is the book's own printed answer picture (three triangles 30/70/80); C44 is the finished construction (arc cuts l at R and S); C43 has no book figure, drawn to scale from the LP numbers (BC = 3.006 recomputed).
- Teaching images C23.IMG1, C42.IMG1, C44.IMG1 are never linked; the new figures have their own ids (IMG2).
- C25 block 0 (builder, "the middle one") and C33 block 0 (Chintu and the arrowhead): OPTIONAL, not added. C25: a plain two-room plan would help but the kept image C25.IMG2 is exactly that. C33: all data are in the words; the arrowhead picture is drawn at C40.
- C43 block 1 ("each of these", hinged objects): none, DECORATIVE_ONLY (the objects are illustrations in the kept image C43.IMG1).
- All check-my-thinking MCQ blocks (C23 b1, C24 b2, C42 b1, C43 b2, C44 b1) and the word blocks (C24 b0, b1, C34 b0, b1): none, TEXT_SUFFICIENT.

Inventory bookkeeping
- P07-diagram-1 (colour-coded congruence statement with arrows) is mapped to concept_image M2.S6.T6.C24.IMG1 (that image holds the same statements with arrows); nothing linked.
- The four SSA figures P11-shape-1, P11-construction-1, P11-construction-2, P12-shape-1 are all claimed by the single C44 construction figure (it contains each of them: the 6/4/30 measurements, line l, the arc, R and S, both triangles).
- Second uses of the same printed picture are NEW-entries: NEW-P07-shape-1-C29, NEW-P08-cutout-1-C30, NEW-P09-shape-1-C37, NEW-P08-shape-1-C39, NEW-P09-shape-2-C41. P08-cutout-1 (the unmarked paper halves) is mapped to the two rectangle solutions.
- I did not claim P12-shape-2 (O the midpoint of AD and BC, p.12): it belongs to chunk C's section (T11/T12, p12.midpoint). P05-construction-1 belongs to chunk A.
- I checked all my base descriptions against the page pictures (tick counts on pp.6 and 9 enlarged); they are correct. P06-shape-1 description is kept and extended with the shortest-side remark (starts without CORRECTED because the facts are right).

## 2. Things in the LP that look wrong

- M2.S7.T7.C29 (Q2): the question text "Can the correspondence be A with C, B with B, D with D? ..." does not say which triangles (ABD and CDB cut from rectangle ABCD along BD). The card cannot stand alone; the figure carries it. Suggest starting the question with "In rectangle ABCD cut along the diagonal BD, ..." (text sync needed; I did not set needs_lp_text_sync).
- Referents that exist only in a kept picture or nowhere: C25 block 0 "the middle one" (floor-plan image C25.IMG2); C43 block 1 "each of these" (hinged objects, image C43.IMG1); C34 block 1 "this sheet" (image C34.IMG1); C33 block 0 "the arrowhead" appears before its first picture (the arrowhead is first drawn at T9 Q3 = C40).
- C23: the LP steps say the one-bar side is the shortest, the two-bar side the middle one, the three-bar side the longest; the book picture on p.6 does not agree (see 3). The LP text is followed.
- ncert_refs page numbers in the LP: the kite (LP "Q1", book Figure it Out Q3) and the arrowhead (book Q4) are on p.9 but the LP refs say p8.FIO3 and p8.FIO4; RED/JAM (book Q2) is on p.8 (p8.FIO2 correct). The LP order of the T9 questions (kite, RED/JAM, arrowhead) is book Q3, Q2, Q4.
- Numbers I recomputed and found correct: C43 BC = sqrt(36 + 25 - 60 cos 30) = 3.006; C44 arc cuts l at 2.55 and 7.84 from P, distance from Q to l = 6 sin 30 = 3; C39 answer "EDR with AMJ, DRE with MJA" (cyclic shifts, consistent); C41 "FED with GED" is consistent; C30 pairs A-C, B-D, D-B agree with AB = CD, AD = CB, BD = DB; C32 lists all six orders of HEN/BIG.

## 3. Places where the book itself is unclear

- p.6 triangles ABC / XYZ: the picture is not to scale. AC (one tick) is about 118 px, AB (two ticks) about 87 px, CB (three ticks) about 170 px, so the two-tick side is the shortest. The LP text says one bar = shortest; the redrawn figure uses 3.0 / 3.6 / 5.0 (one / two / three bars) to match the LP, with the corner positions of the book.
- p.8 RED: drawn right-angled at E, but a 3.5-5-6 triangle has about 88 degrees there (and JAM has about 91 degrees at A on the page). Both are drawn exactly from the lengths here (to scale, 1 unit = 1 cm), JAM turned about 62 degrees as in the book.
- p.12 PQS: S is drawn slightly left of Q (angle at Q looks 90 degrees or less); the true angle PQS is about 101 degrees (R and S computed exactly in the figure).
- p.10 SSA statement uses ABC and XYZ (AB = 6, AC = 4, angle B = 30) while the figures p.11-12 use P, Q, R (PQ = 6, RQ = 4, angle P = 30). Same configuration after renaming (A to Q, B to P, C to R); the LP follows the figures.
- p.11 rough sketch: a short dash on PQ is a printing artefact, not a tick.
- The book has no figure for the SAS case (p.10) and no printed solutions section; the SAS figure and all solution figures come from the LP text.
