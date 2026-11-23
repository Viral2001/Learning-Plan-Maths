# Chunk B notes (Class 6 Ch 8, topics T15, T16, T18, T19, T20, T22, T23; units 20 to 36)

Result: 28 items = required 8 / optional 7 / none 13. Validator: errors 0, warnings 2 (C56 and C79, see 0).

Required diagrams (media ids): M2.S15.T15.C42.IMG1 (Think figure A to D), M2.S16.T16.C44.IMG2 (finished square PQRS), M2.S18.T18.C51.IMG1
(rectangle 4 by 6), M2.S18.T18.C53.IMG1 (rectangle 10 by 2), M2.S19.T19.C56.IMG2 (rectangle 7 by 4), M2.S22.T22.C75.IMG1 (two-panel squares
solution), M2.S23.T23.C78.IMG1 and M2.S23.T23.C79.IMG1 (square within a rectangle, question and solution).

## 0. Bookkeeping the merge needs to know
- `NEW-P08-dot_grid-1-T15` is the SECOND use of base figure `P08-dot_grid-1` (the dot strip with A to D). The first use is chunk A's "identify the
  squares in this collection" question. I did NOT claim the base id itself. If chunk A leaves that figure without a required item, nobody claims
  the base id and the merged check will flag it; the specs of the two items must also be identical (mine: 40 x 11 dots, corners
  A (5,1)(9,5)(5,9)(1,5), B (15,1)(18,5)(15,9)(12,5), C (26,1)(31,5)(26,9)(21,5), D (36,3)(38,4)(36,8)(34,7), letters under columns 5, 15, 26, 36;
  all checked against the page picture by pixel position).
- Two required items have no inventory figure (validator warning, expected): C56 (the plain rectangle 7 by 4 is not printed as such; the book's
  8.4 pictures all carry X and Y) and C79 (the book prints no answer picture for Construct 1).
- Inventory mappings I chose: the six STEP 1 to 5 pictures of the square (P09-1..3, P10-1..3) and the four 8.4 X-Y pictures (P11-1..4) are teaching
  pictures with nothing for an item to link, so `none:TEXT_SUFFICIENT`; P10-construction-4 (STEP 6, finished square) became the diagram of C44;
  P13-shape-1 and P14-shape-1 (three squares, rough diagram of ACDF) are the two panels of C75's solution diagram; P15-shape-1 is C78's question
  diagram; the six tables are plain tables (`none:LATEX_TABLE`).

## 1. Judgement calls
1. T15 Think (C42/C43): question REQUIRED (the text says "in the above figure"; the data is only in the dots); solution OPTIONAL. The printed answer
   is "Yes, the position of the points on the grid paper makes it possible" and the LP steps are a complete method. A copy of figure A with 4 across
   and 4 down marked on each side would help, but the LP steps give no numbers, so a drawn count would also need a text change. Could be flipped to required.
2. C44 (square of side 6 cm) and C56 (rectangle 7 by 4) are REQUIRED although the same concept already holds a teaching image of the finished
   figure (kept image C44.IMG1 / C56.IMG1). Reason: the answer of each worked example is a constructed figure (v3: ANSWER_IS_FIGURE; same decision as the
   Construct Q1/Q2 rectangles whose printed answers are pictures), and v3 says a teaching image is never linked. The new diagrams differ a little from the
   teaching images (all four sides labelled, all four right angles marked, no arcs). If the user does not want a second copy of a figure that sits in the same
   concept, both can be flipped to none.
3. C45 ("why PS is 6 cm") and C46 ("RS and angles R, S"): NONE. Both are answered by the properties of a square and every fact is in the text. The book
   prints a figure beside C46 (STEP 6), but it adds nothing the text lacks, and C44's figure is the same square.
4. T18 Q1 and Q2: question none (no figure is given, a blank rectangle would imply one), solution REQUIRED because the printed answers are pictures.
   T18 Q3 solution OPTIONAL: the printed answer is the word "No"; a picture of perpendiculars staying the same distance apart would help, but a teaching image of that idea exists.
5. T19 C57 (Math Talk about closest and farthest) is OPTIONAL: a discussion question with no figure attached to it and a complete text answer. A picture
   of rectangle ABCD with X on AD, Y on BC and a dashed XY is the figure that would help. This is the T19/T20 call most likely to be flipped, because the
   book builds 8.4 on four pictures of exactly that rectangle. C58 is NONE (it compares two lengths stated in words).
6. T20 (Rectangle Exploration, four pairs): only the printed answers decide, and none of them is a picture (two plain tables, "XY = AB; ABYX is a
   rectangle", "equal to AC or BD"), so: Q1 question optional, Q1 solution none (plain table plus arithmetic), Q2 both none (plain tables), Q3 question and
   solution optional (rectangle with X, Y level and the four-sided figure ABYX shaded would help), Q4 question none (it names the diagonals in words) and Q4
   solution optional (X at A, Y at C, diagonal AC, sqrt(65) cm). The Q3 pair is the best candidate to become required if the user wants a picture here.
7. T22 (rectangle that divides into three squares / into two squares): question NONE (the LP text describes the target in words and no longer says
   "as shown in the figure"), solution REQUIRED. The pair holds two blocks on one card, so there is ONE solution diagram with two panels (top: 9 cm by 3 cm
   in three squares of side 3 cm, no vertex letters because the LP letters only the first square; bottom: ACDF 8 cm by 4 cm with ABEF, BCDE, the book's 7 equal-side ticks, 4 cm and 8 cm).
8. T23 Q2 (A Square within a Rectangle): question REQUIRED because the LP text still says "as shown in the figure" (the bracket after it does not replace the reference),
   solution REQUIRED and `derived_from` the question figure (adds the 4 cm side and the 2 cm gaps). This differs from T22 only because T22's text has no figure reference.
   T23 Q1 is NONE for both sides (numbers only).
9. Colours: where the question has no figure, the solution diagram stands alone; outlines and measure labels are INK, the right-angle marks and equal-side ticks (the checks the
   solution adds) are ANSWER green. All diagrams are 16:9 cards, drawn to scale.
10. The book's printed answer pictures for Construct Q1 and Q2 show right-angle marks at two corners and compass arcs at the top corners. The LP answers state four right angles
    and the LP steps do not mention arcs, so my figures show all four right angles and no arcs.

## 2. Things in the LP that look wrong or thin
- T20 questions C62, C64, C66 and C68 never say that X lies on side AD and Y on side BC; they only give distances from A and B. Flagged `needs_lp_text_sync` with the sentence to add
  ("X is a point on side AD and Y is a point on side BC.").
- C62's question text repeats the three cases twice (the "XY = ___ centimetres ___ millimetres" sentences and then an a) b) c) list), and C64's text has the cases as prose and again as (1) (2) (3).
- C42's `q_figure` hint says "A, B and C are diamonds of different widths and heights"; in the book A is a square standing on a corner (8 dots across, 8 down), B is 6 by 8 and C is 10 by 8,
  D is a 2-by-1 / 2-by-4 rectangle. The question text itself does not describe the figure, and the LP solution steps contain no numbers.
- C44's answer already states "RS = 6 cm and angle R = angle S = 90 degrees", which is exactly C46's question.
- C45, C46, C57, the second block of T22 and C78 (A Square within a Rectangle) have no printed answer in the book (checked pdf pages 31 to 38); the LP answers are authored. I recomputed them:
  C63 (a) sqrt(49 + 6.25) = 7.43 -> 7 cm 4 mm, (c) sqrt(53) = 7.28 -> 7 cm 3 mm; C69 sqrt(65) = 8.06 -> 8 cm 1 mm; C79 (8 - 4) / 2 = 2; C77 4 is not 2 x 2.5 and 7 is not 3 x 2; C75 AC = 4 + 4 = 8.
  All agree with the book where the book has an answer (7.4, 7, 7.3 cm; 7 cm throughout).
- C75's first block lists the construction with letters A, B, C, D only for the first square (AB, AD, BC) and then "the total length is 9 cm", so the labels of the finished 9 cm rectangle are not defined; the diagram leaves them out.

## 3. Places where the book is unclear or contradicts itself
- Square construction, pages 9 and 10: STEP 3 puts S above P, but STEPs 4, 5 and 6 print R above P and S above Q. That reads P, Q, S, R round the square, and the Think box on page 7 says PQSR is NOT a valid name.
  The LP steps and my figure use S above P and R above Q.
- Page 11 pictures: the first matches the case "X 5 mm from A, Y 3 cm from B" (Y is 1 cm above C), but the second shows X 1 cm and Y 2 cm from the top, which is none of the three listed cases, the third is X = D, Y = B and the fourth X = A, Y = B.
- Solutions page 34, question table: the second column reads 5 cm, 1 cm, 4 cm, which looks like a printing slip (the chapter page 13 has 5 mm, 1 cm, 1 cm 5 mm and the printed answer table uses those values).
- Page 15 Construct 1 picture is not to scale (about 2.2 : 1, side parts about 2.4 cm instead of 2 cm); the page 13 three-squares picture is also slightly wide (parts 1.08 times as wide as tall). Both are drawn exactly to scale here.
- Math Talk (page 12) and "Explore: Can the rectangle now be completed?" (page 14) have no printed answer.
