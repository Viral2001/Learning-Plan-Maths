# Chunk B notes (Class 6 Ch 6, units 19 to 38)

Result: 32 items, required 13 (6 question, 5 solution, 2 worked example), optional 0, none 19. Validator: errors 0, 5 warnings (the five required solution diagrams have no printed book picture to map to, which is expected: they are new final-state figures).

Checks I ran in code: the corner lists of the four dot-grid shapes reproduce the printed answers (8s+2d, 4s+6d, 12s+6d, 18s+6d for perimeter; 4, 9, 10, 11 for area, whole and half squares 3+2, 6+6, 7+6, 8+6 exactly as the LP solution says); the arrangements b, c, d have outline perimeters 28, 28, 26 and the 22 cm answer arrangement has 22; figure a of Q4 has area 28 and figure b has area 9, and my cuts tile each exactly (8+6+6+8, 5+2+2).

## 1. Judgement calls

- U19 (C41 block 0, perimeter of equilateral triangle ABC): none, TEXT_SUFFICIENT. The book's triangle has no lengths or marks, only A, B, C. The picture I considered as optional is a triangle with its equal sides marked; I did not call it "clearly helps".
- U20 (similarity of square and triangle): none, a word question.
- U21 (Akshi/Toshi triangle): question required. The book prints the triangle already coloured (top and left sides red, slanting side blue) in the question itself, so the question diagram carries that colouring (SET_B straight, SET_A slanted; the house palette has no red). Solution none, SAME_AS_QUESTION_DIAGRAM: it would only add the words 6s + 3d. This differs from U22 on purpose: in Q2 the book prints each shape in one colour, so the solution's straight/slanted colouring is new.
- U22 (four shapes, straight and diagonal units): question and solution both required. Solution marks every edge run in the two colours and writes the four results; counting 8 to 18 units from words alone is error-prone.
- U23 (regular polygons): question none (OPEN_ENDED, no figure in the book); solution none (the answer is a rule in words plus 6 x 5 = 30). A labelled hexagon would be "nice", not needed.
- U24 (T10 worked example, "this long strip"): required. I treated "this long strip" as a reference to the book's lettered arrangement a, and arrangements b, c, d are drawn in U25, so a is drawn too (sibling rule). I did not draw the uncut chit (4 cm by 6 cm with a dashed cut): the question text gives its size, the cut and the join.
- U25 (arrangements b, c, d): question required, solution required (join highlighted with its length, perimeters 28, 28, 26 under each). The diagram shows only the book's labels (2 cm, 2 cm, 2 cm, 3 cm); no letters b, c, d (the LP solution says "the L shape", "the T shape", "the last arrangement", which matches the left-to-right order).
- U26 (22 cm puzzle): question required although the book prints no figure beside it. Reason: "the two pieces" only means something through the book's cut chit and the question text never says they are each 6 cm by 2 cm (see section 2). The diagram is the two separate pieces with their sizes, nothing arranged. Flagged `needs_lp_text_sync`. Solution required (the answer IS an arrangement): the pieces slid so they touch along 5 cm. I chose horizontal pieces, lower one 1 cm to the right (outline 22); any arrangement with a 5 cm join is correct, the LP only says "slide one piece along the other".
- U27 to U32: none for all (text-only examples and questions, arithmetic answers). The book prints no figure for Example 3, Example 4 or Figure it Out Q1 to Q3.
- U33 (Q4, splitting figures a and b): the LP keeps Q4 as one question with one card, so ONE diagram holds both figures (left staircase, right arch). Solution required (ACTION_ON_FIGURE): dashed cuts and the area of each rectangle, with the cuts the LP describes.
- U34 (T15 worked example, "guess which has the larger area"): required. The learner cannot guess without the two outlines. They are freehand, so I traced them from the page (colour-segmented, simplified: 37 control points for the smooth curve, 17 corners for the jagged one) and kept their near-equal areas (curved about 1.1 times the spiky one). I considered NOT_RENDERABLE and rejected it: the guess needs "a curvy blob and a spiky leaf of about the same size", not an exact outline.
- U35 (four counting rules): none, the book gives the rules in words only.
- U36 (circle of diameter 3 on a graph sheet): none, OPEN_ENDED. The student draws it; no figure, no printed answer, and the count depends on the placement (section 2).
- U37 (why not circles): none, TEXT_SUFFICIENT + REUSES_CONCEPT_IMAGE. A "why" question; counts 42 and 44 are in the text; the same concept keeps the teaching image of the two packings (never linked).
- U38 (Counting Squares Q1): question required (same figure as U22's question, "same as M1.S9.T9.C45.IMG1"); solution required: whole squares shaded green, half squares orange, areas written. Same reason as U22 (solution adds exactly the counted squares).
- Colours: SET_B (orange) stands for the book's red straight units and SET_A (blue) for its blue slanted units, in U21, U22 and the key of U22/U38. Piece fill is CELL_FILL (the book's pale yellow has no token). All diagrams are 16:9; the 23 by 7 dot grid and the three arrangements are wide strips scaled to the card width.
- Inventory choices: P08-shape-1 (the uncut chit) is mapped to U26's question because that diagram shows the chit's two halves; P11-tangram-1 is used by no LP item (the LP leaves the tangram Figure it Out out) and sits between my units p.10 and p.12, so I claimed it as none:OPEN_ENDED only so it is accounted for. If chunk C or the merge already claims it, keep either.

## 2. Things in the LP that look wrong or thin

- M1.S11.T11.C51 and C53 (Split and Rejoin Q1, Q2): the question texts do not give the piece size (6 cm by 2 cm); it lives only in the earlier worked example and the book figure. Suggest adding "each 6 cm by 2 cm" to both question texts. For Q2 my question diagram carries the sizes and the item is flagged `needs_lp_text_sync`.
- M2.S14.T14.C64 and C66: the book order is Q1 garden width, Q2 tiling cost, Q3 coconut grove. The LP names C64 "Q2" (it is the coconut grove, book Q3) and C66 "Q3" (it is the tiling cost, ncert_ref p10.q2, book Q2), and C66's `book_number` says "Covering a Region, Q3" for the book's Q2. The LP order (coconut first, then tiling) is not the book order. Harmless for images; matters if anything is matched by number.
- M2.S14.T14.C69 solution text says "Figure a" and "Figure b"; my diagram has no letters (figure letters are never drawn). Suggest "the staircase figure (left)" and "the arch figure (right)" in that text, or leave as is, since the shapes are described.
- M2.S15.T15.C71 block 0 (circle of diameter 3): the LP answer "about 7 square units" is not forced by the half-square rule. I counted: centred on a grid point gives 4, centred in a cell gives 9, other placements give 6, 7 or 8. The true area is pi x 1.5^2 = 7.07. The book prints no answer for this Let's Explore. Worth rewording as "about 7 (it depends where you place the circle; the true area is about 7.07)".
- M2.S15.T15.C70 block 0 ("guess which is larger"): the LP answer "A guess, settled by counting squares" does not say which is larger; on the page the curved outline is slightly larger (about 1.1 times). Information only.
- The printed solutions (pdf pages 23 to 29) have NO answer for the whole "Split and rejoin" page (arrangement a 28 cm, b, c, d, the 22 cm puzzle). The LP values 28, 28, 26 and "join along 5 cm" are therefore the LP's own; I checked them geometrically and they are right.
- M1.S9.T9.C44 (Q1 solution): the LP reasons by laying a straight unit on a slanted unit; the printed answer reasons "a diagonal of a square is longer than its side". Same conclusion, no conflict.

## 3. Where the book itself is unclear

- P08-shape-1 (the chit) draws a thin wedge-shaped notch beside the dashed cut line, apparently the cut being started; its size is not given. Not drawn.
- Arrangements b, c, d print no piece lengths (only 2 cm, 2 cm, 2 cm and 3 cm); the 6 cm lengths are inferred from the proportions and from the 6 cm by 4 cm chit.
- Figure a of Q4 prints eight labels; two sides (top 2, right 4) are unlabelled and follow from the others (bottom 3 + 4 = top 2 + 3 + 2 = 7; left 4 + 2 + 1 = right 4 + 3 = 7). The question diagram leaves them unlabelled, as printed.
- The freehand shapes of p.140 have no measures at all; any redraw is approximate.
- P11 tangram: eight questions on the printed page, none of them in the LP.
