# Notes, chunk A (Class 8 Ch 14 Area, units 1-17, topics M1.S2.T2 to M1.S7.T7)

Result: 30 items = required 24 / optional 3 / none 3 (question: 11 required, 2 none; solution: 10 required, 3 optional; worked example: 3 required, 1 none).
Validator `--chunk A`: errors 0, warnings 3 (C5 worked example, C27 and C28 solutions: required, but the book prints no figure for them).
Figure inventory: 34 entries = 27 mapped to items, 6 to concept images, 1 none. The 10 `NEW-<base id>-sol` entries are the second use of a printed book figure that a solution redraws with the answers added.

## 1. Judgement calls

1. **C4 (worked, strip 10 x 1 vs rectangle 5 x 4): none. C5 (worked, square vs zigzag): required.** C4 is plain rectangles fixed by their sidelengths and four short calculations. C5's zigzag is a shape that words do not fix, and the book asks that the example be "visually clear", so the example is a picture. The book prints no zigzag, so I chose a staircase of 9 unit squares (rows from the bottom 2, 2, 2, 2, 1 squares); any chain whose squares share only consecutive edges has perimeter 20 (checked: 9 x 4 - 2 x 8 = 20).
2. **Question side = required when the book question gives a figure that carries data or geometry, even though the LP text repeats the numbers** (user rule 4): C7 (rangoli rectangles), C9 (rectangle with diagonal), C26 (isosceles SUB). Also C11, C13, C14, C15, C16, C17, C22, C24 (book figures), and worked C19, C20.
3. **Solutions: required when the solution adds new geometry, fills in unknowns, highlights what the steps talk about, or the answer is a drawing**: C12 (missing sides filled in), C13 (strips), C14 (p, q, overlap), C15 (8 bend squares), C16 (doubled square), C17 (rearranged pieces), C23 (shaded half), C26 (equal bases and areas), C27 and C28 (constructions). **Optional (not added)** where the solution only repeats the question figure and adds numbers or colour: C8, C10, C25; the reason names the figure that would help.
4. **Letters.** (i), (ii) shown in C11/C12 and (i), (ii), (iii) in C24 because the LP answer text refers to the parts by those letters (user rule 3). Not shown in C13: its (i)-(iii) are question parts, not lettered figures. The point letters A-H, X, Y, S, U, E, B etc. are part of the book figures and the LP text uses them.
5. **One diagram per side.** C11/C12: figures (i) and (ii) side by side in one card. C13: the main path figure plus the three moved drawings of part (iii) in one card (the solution repeats the three unchanged because it is derived from the question). C24: the three triangles in one card.
6. **C14 question** marks "14 m" and "12 m" on the plot (the question text gives them; the book drawing leaves them off) and draws both paths equally wide as the book does (1 m each, not labelled). The solution adds p, q and the overlap square.
7. **C26 question** writes "24 sq. units" on SEB (the question text gives it; the book picture carries no number). The solution adds double ticks on UE and EB, 24 sq. units on SUE, and 48 sq. units for the whole triangle.
8. **C23 question** keeps the altitude XY and the right angle because the book's Fig. 7.1 prints them; the LP solution says "Drop the altitude XY" (see LP text issues).
9. **C17**: the two lines are drawn exactly through the centre, as the LP video requires (the book's lines cross within about 2% of the centre). Solution colours the four pieces (SET_A, SET_B, MARK_FILL, FOCUS) so the rearrangement can be followed without labels; coordinates of the four turned pieces and the hole are in the spec (hole side 3, larger square side 8.544, area 73 - 9 = 64).
10. **C15 solution** highlights the 8 bend squares only; the book hint figure (L tube arms 5 and 5 beside a straight tube '?') is not drawn, mapped `none:TEXT_SUFFICIENT` because step 1 states it in one sentence. The book draws the straight tube as 10 units although the answer is 9, so drawing it from the book would mislead.
11. **C27 solution** draws only the first method (extend AB to E, join E to D); the "another way" with a cut along a diagonal is not drawn. **C28 solution** follows the LP steps (midpoint line, perpendiculars) and the LP video's split of the top triangle along its height; letters M and N come from the video rules (the LP steps say "the midpoints"). Question sides of C27 and C28 are none: the book gives no figure.
12. **Derived solutions with a second figure (C16, C17)**: the left panel repeats the question picture smaller and shifted left to make room; cuts, ticks and labels are identical (said in `render_note`).
13. **Inventory mapping.** P01-shape-1 and P01-dissection-2 (topic M1.S1.T1, no unit in any chunk) are claimed here as accounting only, mapped to concept image M1.S1.T1.C1.IMG1; if another chunk also claims them it must use the same meaning. P06-shape-1 and -2 (teaching comparisons XDC vs YDC / YBC) map to concept image C18.IMG1 (same half-rectangle idea; that image is Fig. 7.1, not these two); P06-shape-4 and P07-shape-1 map to concept image C19.IMG1; P07-shape-2 maps to the item that draws it (worked example C19), per user rule 5.
14. **Media ids.** C5, C19, C20 take `.IMG2` because `.IMG1` is a kept teaching image. C27 and C28 solutions take `.IMG1` (no question diagram).

## Borderline (user rule 4)

- C7 question and C9 question: required although the LP text states every number (book figure carries the data).
- C26 question: required although the text states every fact.
- C8, C10, C25 solutions: optional, not added (figure only repeats the question figure plus numbers).
- C23 solution (shaded half) and C26 solution (equal halves) and C15 solution (bend highlight) and C16 solution (doubled square): required although the arithmetic or argument is complete in text; kept because each adds a geometric fact the steps refer to.
- C5 worked example: required (shape not fixed by words); C4: none.
- C19 worked example: required (base, perpendicular height and the later 'outer rectangle' are only meaningful with a picture); a teaching image of the same idea exists and is not linked.

## 2. LP text issues (no LP text was changed)

- **M1.S3.T3.C11** `question_tex`, part (ii): `$A 29\text{ m}^2$ piece` puts the article "A" inside the maths. Suggested: "(ii): A $29\text{ m}^2$ piece and an $11\text{ m}^2$ piece ...".
- **M1.S3.T3.C11** (and C12 `question`): figure (i) is called "a plus shaped figure"; the book figure is four rectangles round one common corner (a pinwheel). Suggested: "four rectangles arranged round one common corner like a pinwheel".
- **M1.S3.T3.C11**, part (ii): the text does not say that the 11 m² piece sits beside the 29 m² piece or that the bold outline encloses the 29 m² piece and the piece below it only for the area 50 m². Suggested: "The bold outline encloses the 29 m² piece and the piece below it; together they have area 50 m². The 11 m² piece is beside the 29 m² piece."
- **M1.S4.T4.C13 to C17** and **M1.S7.T7.C26 to C28**: `item.book_number` is "Figure it Out, Q1" for every one; the concept names say Q2..Q6 (Rectangles and Squares) and Q3..Q5 (Triangles). Suggested: "Figure it Out (Rectangles and Squares), Q2" ... "Q6" and "Figure it Out (Triangles), Q3" ... "Q5". Also these blocks only say "Read the question in the book"; the actual question sits in the Practice blocks of M1.S2.T2.C6 (blocks 0-4) and M1.S5.T5.C21 (blocks 0-2).
- **M1.S2.T2.C5** (worked): "a thin zigzag made of 9 unit squares joined edge to edge in one line with bends" does not fix the shape. Suggested: "a staircase of 9 unit squares: the squares go right, up, right, up and so on, each sharing a full side with the next".
- **M1.S4.T4.C14** (lp_text question): "A plot has sides 14 m and 12 m with a crosspath." Suggested: "A rectangular plot 14 m by 12 m has two paths crossing it, one along each pair of sides, each running right across the plot from one side to the opposite side."
- **M1.S4.T4.C16** (lp_text question): "A square is divided into regions 1, 2 and 3" does not say how. Suggested: "A square is cut by one diagonal and by a line from a corner to the midpoint of that diagonal into regions 1, 2 and 3: regions 1 and 2 are the two small triangles on one side of the diagonal and region 3 is the half of the square on the other side."
- **M1.S4.T4.C17** steps 1 and 2: "two perpendicular lines through the square that are not parallel to its sides; the 4 pieces are congruent" is only true when the lines pass through the centre, and "the long edges run round the outside" disagrees with the video ("the two equal edges", length 4.27 for a side-8 square, which are not the longest edges). Suggested: step 1 "Draw two perpendicular lines through the centre of the square that are not parallel to its sides"; step 2 "Turn the pieces so that each right angle points outward and the two equal edges that met at the centre run round the outside".
- **M1.S6.T6.C23** step 1: "Drop the altitude XY to DC" while the book's Fig. 7.1 (and the question picture) already shows XY. Suggested: "The altitude XY (from X, perpendicular to DC) splits the rectangle into two rectangles."
- **M1.S7.T7.C28** step 3: "Cut off the two small top triangles and turn each into the gap below it" - the two top triangles exist only after the top triangle AMN is cut along its height. Suggested: "Cut off the top triangle AMN, cut it along its height from A into two right triangles, and turn each half round into the gap beside the slanted side of the lower part."
- **M1.S4.T4.C15** (lp_text): the lengths 20, 20, 20, 15, 15, 10, 10, 5, 5 are in order from the outer end inwards; suggested to say so: "listed from the outer end of the tube inwards".

No print slip was found in the book (no wrong digit, missing sign or count) in the pages of this chunk, so nothing was corrected under user rule 1; the specs use true values where the book drawing is only schematic (spiral tube width 1 instead of the printed 0.84; lower piece of FiO1 Q1 (ii) drawn at 84/29 = 2.897 m, the book draws about 2.67 m).

## 3. Where the book is unclear

- **FiO1 Q1 (ii), "Area = 50 m²"**: the curved arrow starts at the lower blank piece, but the LP (and the drawn proportions: widths 7.25 and 2.75, lower piece about 2.7-2.9 m) treat 50 m² as the whole bold block (29 m² piece plus the piece below it). Followed the LP.
- **FiO2 Q1 (i) "4 cm" and (ii) "5cm"**: printed near E and near NF, not along the whole base. The to-scale drawing (BE 1.2 of 4; EF 5, DN 3.2) and the LP show they mark the whole bases BC and EF; drawn with dimension arrows along BC and EF.
- **FiO1 Q4 hint figure**: the straight tube is drawn about 10 units tall while the answer is 9; not drawn.
- **FiO1 Q3**: path widths not given; the book draws equal widths; strips not centred exactly (47% to 53%). Drawn centred, 1 m each.
- **FiO1 Q2**: the three moved drawings are approximate; margins taken as (2, 2, 2, 2), (3 left, 1 right, 1 top, 3 bottom) and (2 left, 2 right, 3 top, 1 bottom) in a 20 x 14 outer rectangle with a 16 x 10 inner one; the book does not say how far the park may move.
- **FiO1 Q5**: the book does not state which half of the square the numbers 1, 2, 3 sit in beyond the picture; taken from the picture (1 left triangle, 2 top triangle, 3 the lower-right half).
- **C5 zigzag and C27/C28 proportions**: the book gives no figure; the layout and the 4:3 and 8:6 proportions are chosen (no numbers drawn in C27 and C28).
