# Notes for chunk C (Class 6 Ch 8, plan cbse_eng_maths6_ch8_v47)

Units 37 to 56: M2.S25.T25, M3.S26.T26 to M3.S32.T32. 31 items: required 9, optional 2, none 20. Validator: errors 0, warnings 0.

Required (all `keep_and_replace_spec` except C94 `add_new_image`):

| item | media_id | what it draws |
|---|---|---|
| C83 solution | M2.S25.T25.C83.IMG1 | the two staircases of squares (4-4-4 and 7-5-3), one card |
| C84 question | M2.S25.T25.C84.IMG1 | the Shadings figure (4 by 4, 11 hatched diagonal cells, plain 2 by 2 block, plain unit square) |
| C87 solution | M2.S25.T25.C87.IMG1 | square, both diagonals (GUIDE), circle at the crossing (ANSWER) |
| C89 solution | M2.S25.T25.C89.IMG1 | 2 by 2 squares, diagonals of each, four equal circles |
| C91 solution | M2.S25.T25.C91.IMG1 | 8 cm square, four inward arcs (radius 8 cm), the four outside compass points |
| C94 worked | M3.S26.T26.C94.IMG1 | rectangle PQRS, both diagonals, the eight angles lettered a to h (no values) |
| C109 solution | M3.S30.T30.C109.IMG1 | finished rectangle ABCD, diagonal AC, 60 and 30 degrees at A and C |
| C111 solution | M3.S31.T31.C111.IMG1 | finished rectangle, 50 and 40 degrees (printed answer is a picture) |
| C113 solution | M3.S31.T31.C113.IMG1 | finished square, four 45 degree marks, ticks (printed answer is a picture) |

Optional (not added): C93 worked (figure with the letters c, d, g, h), C100 solution (square with one diagonal and 45 + 45).

## 1. Judgement calls

1. **8.4 Construct 2, 4, 5, 6 (C82, C86, C88, C90): question `none`, solution `required`.** The LP question text fixes each figure completely (sizes, staircase corners; a square with a circular hole at its centre; 2 by 2 with four centred holes; 8 cm square with four inward arcs, corner to corner). A careful student loses nothing without the picture, so the tie-breaker says none. The answer is a construction (B2, ANSWER_IS_FIGURE), so the solution figure is drawn standalone (question has no figure, `derived_from` null), and it carries the construction marks the steps only describe (diagonals that find the centres, compass points). This mirrors Number Play 3.1 (word question, figure answer). **If the user wants the book's target picture on every "Construct this" question, the four question sides would become required (the book does print a picture for each); only Construct 3 needs it to attempt, so I kept them none.**
2. **8.4 Construct 3, Shadings (C84 question required, C85 solution none).** The LP words ("some halved by diagonals ... a plain larger square in a corner") cannot fix the figure; the book's picture IS the task, so the question is required (FIG_REFERENCED + DATA_IN_FIGURE). The solution would only repeat that picture (the LP steps add no mark or number), so `SAME_AS_QUESTION_DIAGRAM`. This breaks the sibling pattern of item 1 on purpose, for that reason.
3. **C91 (curves) sample answer.** The solution figure follows the LP's own sample (compass 8 cm, tip 8 cm from both ends of the side, dip 1.072 cm, which the LP rounds to "about 1 cm"). The book's printed picture has deeper arcs (about 0.21 to 0.24 of the side, about 1.7 to 1.9 cm, which is a 90 degree arc of radius side/sqrt(2) = 5.66 cm). The book gives no radius and no printed answer for Construct 6, so the LP wins. I included the short crossing arcs because LP step 3 talks about them. **Needs the user's eye: should the solution use the book picture's deeper arcs instead (then the LP steps and answer text would need a new radius)?**
3b. The compass points of C91 are 6.928 cm outside each side, so the 8 cm square fills only about a third of the card height and the 1.07 cm dip is about 36 px at card size; legible but small. The figure is drawn to scale.
4. **C94 required, C93 optional.** C94 asks which of the eight lettered angles are equal; the answer (d = e = a = h, c = f = g = b) only has meaning on the book's lettered picture, and the LP needs 40 words of text to describe where each letter sits (DATA_IN_FIGURE). C93 uses the same picture but only asks "are g and h equal? are c and d equal?"; the answer does not depend on which is which, so the picture is not needed to attempt (optional, mentioned so the user can promote it; if promoted it is the same spec as C94 with the note "same as C94"). The figure for C94 is not coloured by equal groups (that would leak the answer).
5. **C92, C97 worked (diagonals equal; square) none.** The learner draws and measures; the answer is a statement. The same picture is already the teaching image of the concept (C92.IMG1, C97.IMG1); a duplicate adds nothing.
6. **C106 worked (60 + 30) none.** 90 - 60 = 30 from the rule that angle A is 90 degrees; the book's Step 3 picture is a construction step, not data.
7. **C109 (Example 2, rectangle with 60 and 30 degrees): solution required, standalone; question none** (the book question has no figure; the rough diagram sits in the solution). Only the complete final state is drawn (v3), not the book's step pictures. I added the angles at C (60 on the CD side, 30 on the CB side) because the question speaks of "opposite angles", the printed answers of FiO Q1 and Q2 mark both ends, and they follow from alternate angles; the book marks only A. I used the exact 60 degree proportion (BC = AB x 1.732); the book's rough diagram is not to scale. Right-angle marks at B and D only (the corners the diagonal does not split), equal-side ticks because the LP check says AB = CD, AD = BC.
8. **C111, C113 (FiO Q1, Q2): solution required, question none.** The printed answers are pictures (B2). Same layout as C109 for consistency. Left out of the printed pictures: the "Arbitrary Length" label (not a measure; the LP says any length), the arrows, and the compass arc at D (the LP method uses a perpendicular at C). For Q2 I mark the right angle at B and D (the printed one marks B only) so the three rectangle figures match.
9. **C115 to C118 (Construct 2, side 5 cm and diagonal 7 cm) all none.** The questions are answered in words and the concepts already have teaching images of these steps (C114.IMG1 arc from D, C116.IMG1 corner B on line l, C118.IMG1 checking the rectangle). The rough diagram and Step 1 are not needed to attempt C115. These book step pictures are accounted as concept images (P22-construction-2 -> C116.IMG1, P24-construction-1 -> C114.IMG1, P24-construction-2 -> C118.IMG1) or none:TEXT_SUFFICIENT.
10. **C100 optional, C102 and C104 none.** C100: the printed answer is a sentence; a square with one diagonal and 45 + 45 would help but the teaching images C96.IMG1 and C97.IMG1 already show it. C101/C103 are Math Talk discussions (OPEN_ENDED); their answers are text.
11. **Solution diagrams are standalone (no `derived_from`)** because the only required question diagram (C84) has a `none` solution.
12. **Figure accounting overlaps with chunk D.** The Construct 2 solution pictures (P22-shape-1, P22-construction-1/2, P23-construction-1, P24-construction-1/2) can also be used by D for Example 3 (the same construction as a practice pair, C120/C121). Here they are mapped only by their use in chunk C; D may map P24-construction-2 or P22-shape-1 to its own solution item. The merge should compare these.

## 2. Things in the LP that look wrong or weak

- **C84 / C85 (Shadings).** The question text is too vague to build the figure (needs the picture) and never mentions the plain unit square (row 4, column 3). The solution steps say "Draw the diagonals in the small squares. Shade one triangle in each", but two of the 13 cells are plain (the 2 by 2 block and one unit square): 11 of the small squares carry a diagonal and hatching, not all.
- **C90 / C91.** "This is a square with 8 cm sidelengths" is a leftover of the book picture; the LP could say "Draw a square with 8 cm sides". The answer_tex "dips about 1 cm" is arithmetically right for radius 8 cm (1.072 cm) but the book's own picture is deeper (see call 3).
- **C93.** Uses the letters c, d, g, h without saying where they are (the book defines them by the picture). C94 does define them.
- **C94 steps.** "The four angles next to the long sides come out equal: d, e, a, h" is right only when PQ and SR are the long sides (as in the 6 by 4 example). In a rectangle taller than wide the roles swap. The LP never says PQ is the long side. The figure drawn for C94 has PQ as the longer side (about 1.7 : 1, like the book).
- **C115.** The answer says "the base CD" but the question text never introduces C and D (the book's rough diagram does).
- **C116.** The answer relies on "the diagonal DB = 7 cm" which the question text does not say; the question mentions line l and point B with no picture. C117 mentions "line l" without saying it is perpendicular to DC at C. Both rely on the teaching image and the preceding blocks.
- **Naming.** The LP calls the 8.5 end-of-section tasks "Figure it Out 8.5, Q1/Q2"; the book prints them under the heading "Construct" (p.211, and "Construct" in the printed solutions p.35). The LP's "Example 2" and "Example 3" are the book's "Construct 1" and "Construct 2" of section 8.5. Harmless but may confuse a reader checking the book.
- **C101/C102.** The answer adds "cut each other into equal halves" (true, but nowhere in the book's questions); fine.

## 3. Where the book itself is unclear

- **Construct 6 (curves, p.17):** no radius, no compass-tip position, no printed answer in the solutions section (only Construct 4 has a one-sentence answer; Constructs 2, 3, 5, 6 of 8.4 have none). The arc depth of the picture was measured from the page (about 0.21 to 0.24 of the side).
- **Construct 3 (Shadings, p.16):** the hatch-line count per triangle is not countable exactly (about 9); 9 is used. No measurement is printed ("choose measurements of your choice").
- **Construct 1 rough diagram (p.19):** not to scale (height about 1.5 times the width instead of 1.73) and marks the right angle at D only, while the Step 4 picture (p.21) marks it at B only.
- **Construct 2 pictures (p.22-24):** the rectangle is lettered A top-left, B top-right, C bottom-right, D bottom-left (Construct 1 and the printed answers on p.35 use A bottom-left instead); the Step 3 circle is not to scale (radius about 1.2 times DC, not 1.4); point B is not lettered in the Step 3 pictures.
- **Printed answers p.35 (Construct Q1, Q2):** right-angle marks differ (none in Q1, one at B in Q2), only Q2 has equal-side ticks, and both carry construction marks (arrows along the top line and up from C, a compass arc at D) that belong to a compass method the LP does not use.
- **Solutions numbering:** the solutions heading "Page no. 201, Q.4 Square with a Hole" refers to chapter page 203 (Construct 4); the page numbers in the solutions section are the book's own and do not match the pdf pages.
