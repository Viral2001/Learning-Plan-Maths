# Notes, chunk A (Class 7 Ch 7, topics M1.S3.T3 to M1.S13.T13)

Result: 31 items (13 pairs, 5 worked examples): required 12 (2 question, 9 solution, 1 worked example), optional 2 (worked examples, not added), none 17. Validator: errors 0, 4 warnings (required items whose figure is not printed in the book: C9, C14, C24, C28).

Figures claimed: all base figures of book pages 1-13 (P01 to P13, 22 figures) and the three printed-answer pictures of Figure it Out 7.2 on page 28 (P28-shape-1/2/3). P01, P02 and the equilateral-triangle figures of page 3 belong to teaching topics (M1.S1, M1.S2) that have no chunk, so they are claimed here; the merge should not find them unclaimed. Mapping: 10 to items, 10 to concept images (teaching figures, accounting only), 5 to none:TEXT_SUFFICIENT (intermediate construction steps and the naming/ruler-trial pictures).

## 1. Judgement calls

- **C15 question (circle with its centre): required.** The figure is trivial (a circle and a dot), but the book prints it beside the question, the learner acts on it (marks points, joins them: ACTION_ON_FIGURE), the printed answer is a picture, and sibling Q2 is required. Alternative: `none` with the LP text carrying the whole figure. Because the question text says "some points are marked on the circle" while the figure marks only the centre, the item has `needs_lp_text_sync: true` and a text_alternative.
- **C17 question: one card for both book pictures** (two circles; three circles), side by side, because the LP holds the question as one item. The solution card C18 keeps the same layout (`derived_from` C17.IMG1).
- **C14 (five triangles): one solution card with all five**, drawn to one scale, equal sides ticked, no construction arcs (arcs for five triangles would drown the figure). The triangle 1, 5, 5 is drawn with its 1 cm side as the base (the LP says "a very short base"), the other four with their longest side as the base. If the team prefers one card per triangle, this unit would need five solution ids.
- **C16 solution** shows the printed answer (circle, centre O, P, Q, OP = OQ) and also the LP's third point R halfway between P and Q (RP = RQ). The equilateral special case (PQ = radius) is only in the text.
- **C18 solution** draws segment CD as well, so the isosceles triangles ACD and BCD of the LP solution are visible. The other crossing points of the three-circle picture are not drawn or lettered (the LP names none).
- **C9 worked example (4, 4, 6): required.** Its answer is a construction and the steps lean on it ("they cross at C"). The placeholder sits after the question text as the rules demand, but the card shows the finished construction (it is the example's own picture, the steps are right below). The concept has no teaching image.
- **C20 (tent, tree, pole) and C42 (touch, miss, cross) worked examples: optional, not added.** What would help: a triangle labelled 30 m, 20 m, 25 m (C20); three pairs of circles on AB = 8 cm with radii 3 and 5, 2 and 5, 5 and 6 (C42). Both are decided by arithmetic and their concepts already hold a teaching image of the scene.
- **C24 and C28 (arcs that fall short): required**, the question asks what happens to the arcs / to verify by construction, and the answer is the failed construction itself. The part of the base that neither arc reaches (1 cm) is drawn in FOCUS. Both decisions are the same by sibling consistency. The existing concept image M1.S7.T7.C19.IMG1 shows the 8 cm case; it is not linked and C24 draws its own.
- **C26 solution (rough triangle): required** for FIG_REFERENCED: the solution talks about the paths BC, BA + AC, and so on, but A, B and C are defined nowhere in the LP text. The sketch (book Fig. 7.4) fixes AB = 15 cm, BC = 10 cm, CA = 30 cm and is `to_scale: false` (such a triangle cannot exist).
- **C38 question: none** (the book gives no figure with "picture the circles"); **C39 solution: required** (book Fig. 7.5, drawn to scale with AX = XB = 4 cm). P10-shape-1 (circle of radius 4 at A with AX and AB marked) is accounted to the concept image C35.IMG1 because the final figure of C39 already contains all its content.
- **None by rule:** C30, C32, C34, C41 (answers are sums and comparisons, the book's printed answers on pp.29-31 are text only), C36 and C43 (numeric checks and a three-step procedure; C43 has no flow-chart image to repeat), and every question that gives no figure (C6, C11, C13, C23, C25, C27, C29, C31, C33, C38, C40).
- **Colour rule used for stand-alone solution figures** (no question diagram to derive from): the base and every given length in INK, construction arcs in GUIDE, the lines, points and letters the solution adds in ANSWER, the uncovered gap in FOCUS.
- Coordinates are in px on a 1920 x 1080 canvas, and every label sits at a stated position; each figure was previewed once outside the repository to check that labels do not hit lines.

## 2. Things in the LP that look wrong or thin

- **C6 question** names AC and BC ("explain why AC and BC are both 4 cm") without saying that AB is the base and C the third corner. Added as an optional text fix (the question gets no figure).
- **C15 question** says "some points are marked on the circle", the book figure marks only the centre.
- **C14 solution** step 2 says "draw the longest side as the base", but step 3 describes (c) 1, 5, 5 as "isosceles, with a very short base".
- **C25/C26**: the question does not name A, B, C; the solution uses them (see C26 above).
- **C17/C18**: the letter C is a centre in the three-circle picture and a crossing point in the two-circle picture. This follows the LP; the figure keeps it as is.
- C20 numbers (30 m, 20 m, 25 m) are the LP's own, the book gives no lengths for the tent, tree and pole picture.

## 3. Places where the book is unclear or differs from the brief

- The brief says the pdf has no printed-solutions section, but pdf pages 28-34 are a short printed-answers section ("Page No. 150 ..."). Only page 28 holds pictures that belong to this chunk (Figure it Out 7.2 Q1 and Q2). The answers for pp.29-31 are text only.
- **Printed answer of Q2, second picture (P28-shape-3)** relabels the three circles (C at the top crossing, D at the lower crossing, which is also the third centre) while the question's picture has the centres A, B, C. The LP solution keeps the question's lettering, and so does the diagram.
- **P05-construction-1** (the 4, 5, 6 triangle, p.5) is not to scale: C is drawn slightly left of A, but it must be 0.625 cm to the right of A (and 4.961 cm above AB). The diagram uses exact coordinates.
- **Fig. 7.4** (10, 15, 30) is a sketch of an impossible triangle (the drawn sides satisfy the triangle inequality). Kept rough on purpose.
- **Fig. 7.5**: the hand-drawn overlap of the circles is wider than the true 1 cm lens (4 + 5 - 8). The diagram is to scale.
- Figure it Out 7.2 Q1 ends with "Try more" in the printed answer; the answer is open-ended, the diagram shows the single example the LP gives.
