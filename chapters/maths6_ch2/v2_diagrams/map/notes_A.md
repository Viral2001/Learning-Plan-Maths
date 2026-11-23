# Chunk A notes (Class 6 Ch 2, topics M1.S2.T2, M1.S3.T3, M1.S4.T4, M1.S5.T5, M1.S6.T6)

Result: 23 items = required 10 / optional 1 / none 12. Validator: errors 0, one expected warning (see 1.9).
Required: C3, C5, C24 (worked); C10, C12, C16, C18, C27 (question); C15, C28 (solution).

## 1. Judgement calls

1.1 Worked examples with a numbered book figure (C3 = Fig. 2.1, C5 = Fig. 2.2): `required`, although the same picture is already a
teaching image of the concept. Reason: the question text itself cites the figure and v3 Step B2 says a referred figure is drawn even when a
teaching image shows it. Ids are IMG2 (IMG1 is the kept teaching image). Both diagrams show only what the book figure gives (no "shortest"
highlight on the straight route, no segment name).

1.2 C2 (crease, no figure number in the text, hands-on) is `none` while C3 and C5 are `required`: C2 cites no figure and the answer is
just "Yes"; C3 and C5 cite Fig. 2.1 / 2.2. If the team prefers "every example with a book picture gets a diagram", C2 would become required
(paper rectangle with crease AB) and C6 (torch, no book figure) would stay none.

1.3 C6 (torch beam) `none`: LP-written example, no book figure, fully described in words; the plan's ray image already exists.

1.4 FiO 2.4 Q1 (Rihan / Sheetal): question `none` (book gives no figure, so none is invented). Solution `optional`: the answer is words, but a
picture of one point with a fan of lines beside two points with one line would clearly help. Not added. Promote to required only if the team wants
that picture; it would then need a new spec (point with 5 lines through it, two points with one line).

1.5 Solutions of Q2, Q3, Q5, Q6 (C11, C13, C17, C19) `none` with SAME_AS_QUESTION_DIAGRAM: all four answers only name things in the given figure
and add no mark (sibling consistency: same kind of answer, same decision). A reviewer could ask for a coloured/labelled copy of the figure
(for example NB highlighted in Q3); I judged that "nicer", not needed.

1.6 FiO 2.4 Q4: question `none` (no figure given, learner draws). Solution `required` (printed answer is four pictures, LP answer only describes
them): ONE diagram with four panels in a 2 x 2 grid (a, b / c, d), because a pair gets one solution diagram. Panel letters (a)-(d) are not drawn
(v3 section 4 forbids figure letters); the panels are self-identifying by their point letters and follow the question order. Strokes and dots are
ANSWER green, letters INK (the whole figure is the answer; no question diagram exists, derived_from null).
Deliberate differences from the printed pictures: (i) dots drawn at every labelled point (printed pictures have none); (ii) in (b) XY is drawn as a
RAY (dot at X, arrowhead only on the Y side) because question and LP say ray, while the printed picture gives XY an arrowhead at X as well.

1.7 C21, C22, C23, C25 (compass, scissors, spectacles / wallet / stapler / boxes, "these angles") `none`, NOT_RENDERABLE: the book pictures are
real-object pictures that manim cannot draw faithfully, and the LP text already names legs / blades / hinge. If the user wants those pictures in
the plan they need real or AI object images, not manim diagrams (decision for the user).
C25: "these angles" refers to the object pictures of the previous bullet (C23); I did not substitute Fig. 2.9 because the question does not give it.

1.8 C24 (Case 1 vs Case 2), C27 / C28 (six cases): the book pictures are a girl opening a book; the mathematical content is the opening of the cover.
I drew schematic pictures: horizontal arm = pages, turned arm = cover, thin FOCUS turn arc with arrowhead in place of the red arrow of the book picture,
captions Case 1..Case 6, no hinge dot and no word in the question figure (the learner is asked to mark arms and vertex). The book prints no sizes; the
openings 40, 130, 180, 210, 290, 340 degrees are my by-eye reading of the page picture (Case 1 cover just lifted, Case 2 cover opened to the left,
Case 3 book flat, Case 4 cover hanging below the pages, Case 5 and 6 cover folded back). Only the increasing order is printed in the book text
("Cases 4, 5 and 6 are successively larger"). Cases 4-6 pass the straight position (reflex), so their arcs are longer than a half circle; the arc
direction is what keeps them from looking smaller than Case 1. C24 uses exactly the Case 1 and Case 2 pictures of C27 (render_note says so).
Please have the renderer check that the label positions listed in C28 (generated with a collision check against arms and arcs) look clean.
C28 marks ALL six cases (question says "each of these cases"): ANSWER dot on the hinge, ANSWER halo behind both arms, the words vertex / arm.

1.9 Warning on C28: no base-inventory figure maps to the solution item because the book prints no answer picture for the six cases (the figure
P05-illustration_set-3 is already claimed for the question side of C24 and, under a NEW id, for the question side of C27).

1.10 Figure claims that are not items:
- Section 2.1 figures P01-photo_set-1 (object tips, DECORATIVE_ONLY) and P01-points-2 (dots Z, P, T, TEXT_SUFFICIENT) are claimed here because
  topic M1.S2.T2 is the only topic carrying section 2.1 (M1.S1.T1 "Bends and Turns" has no book figure).
- P03-photo_set-1 (lighthouse / torch / sun) DECORATIVE_ONLY.
- P02-shape-1 -> concept_image M1.S2.T2.C2.IMG1; P03-ray-2 (Fig. 2.3) -> concept_image M1.S3.T3.C6.IMG1 (ray with start point and a second point);
  P05-angle-2 (Fig. 2.8, arms and vertex) -> concept_image M1.S5.T5.C20.IMG1. These are accounting only, nothing is linked.
- P06-angle-1 (Fig. 2.9, turn of a ray) -> none:TEXT_SUFFICIENT: the plan has no teaching image of it and no item of this chunk needs it.
  (The content team may want a teaching image for it; not part of this job.)
- Inventory doubts checked against the page pictures: all agree with the base entries (Fig. 2.5 opening is 45 degrees; Fig. 2.4 has no dots; Fig. 2.6
  upward ray has no letter; SOL44 (b) has an arrowhead at X). No CORRECTED entry needed.

## 2. Things in the LP that look wrong

2.1 Question texts that give the answer away or duplicate it (now that figures exist the parentheses are redundant and should go):
- C10 (Q2): "(Fig. 2.4 is a zig-zag path L-M-P-Q-R: L to M, M to P, P to Q, Q to R.)" states the four segments the learner must name.
- C12 (Q3): "(from T one ray goes up-right through A; another goes right through N and then B)" gives the rays.
- C16 (Q5): "(a line passes through D, E, O, B; a ray from O goes through C; ...)" gives the line and rays.
- C21, C22: the question already says "the vertex is the point where the two arms are joined".
2.2 Duplicated text inside question_tex: C8/C9 (the two Rihan / Sheetal questions appear twice), C10, C12, C14/C15, C16, C18/C19 (the (a)/(b)/(c)/(d) parts are
listed twice, once as the book wording and once as a short paraphrase). C14's question_tex repeats (a)-(d) with two different wordings.
2.3 C25: "Do you see how these angles are formed ..." has no referent in the LP (the book's referent is the object pictures of C23); C23's own
text lists the objects, so C25 should name them.
2.4 C27 / C28 carry book_number "Angle: arms and vertex in six cases", which is not an NCERT number (the question is an inline prompt on pp. 17-18 of the book).
2.5 C28 s_figure hint says the answer marks "one of the pictures"; the question asks about each of the six cases, so all six are marked.
2.6 C17 step 3 "Rays start at O or E etc." is vague (answer: rays OC, OB, OE, OD); the LP answers for Q5 match the book. The book adds "(OB; OC are also
possible)" for segments and "Try for other rays": the LP lists only the five / four of the printed answer.
2.7 C6 (torch) has no ncert_refs: it is an LP-written example (book only shows a torch picture as a model of a ray, P03-photo_set-1).
2.8 Concepts C20-C23 share the same concept_name "Arms and vertex in everyday things" (C20 is a teaching concept with its own image, not in this chunk).

## 3. Where the book itself is unclear

3.1 Fig. 2.4 prints only the letters at the joints, no dots, although the question speaks of "five marked points" (dots are drawn in the diagram).
3.2 Fig. 2.6: the ray from O going up has no letter, so it cannot be named; the printed answer names only OC, OB, OE, OD.
3.3 Printed Q4(b) draws XY with arrowheads at both ends (a line), while the question calls XY a ray. Printed Q4(a): P and Q are letters at the line ends, no dots.
3.4 Vidya's six pictures: no angle sizes; the red arrows / circles show the turn, and Cases 4-6 turn the cover past the flat position.
3.5 Fig. 2.1: the fourth route is the jagged edge of the leaf-shaped sheet; the exact bends of routes 2 and 4 are not meaningful, only that the straight
route is the shortest of four.
3.6 The book gives no printed answer for the bullets of section 2.5 (compass, scissors, objects, six cases), so nothing in the solutions pages is claimed for them.
