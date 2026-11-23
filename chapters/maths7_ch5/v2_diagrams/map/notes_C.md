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
