# Notes, chunk A (Class 5 Ch 10 "Symmetrical Designs", topics M1.S2.T2 to M3.S12.T12)

Result: 27 items (17 units): required 24 / optional 0 / none 3. Validator: errors 0, 14 warnings (all "required but no inventory figure maps to it": the figure is not printed in the book, see the list at the end).

Required: 7 worked examples (all of them), 9 questions, 8 solutions. None: T6 solution (C16), T10 Q3 question (C27) and solution (C28).

Worked-example convention used (please confirm): the worked-example token sits after the question text, but the figure shows the worked RESULT (given parts in INK, result marks in ANSWER green), because the example text under it already gives the solution. If you want a "given state only" figure for worked examples instead, the ANSWER marks of C3, C4, C12, C13, C21, C29, C30 must be dropped and C3, C4, C21 would shrink to a plain letter or shape picture.

## 1. Judgement calls

- **T3 Q1 / Q2 questions (C6, C8)**: required. The book prints a row of the letters E N X T K V O under both questions and Q1 says to find the cutouts "by drawing lines of symmetry on the letters". One diagram per item, identical spec (C8 says "same as C6"). Fig ids: `P01-letters-3` for C6, `NEW-P01-letters-3-q2` for C8.
- **T3 Q1 solution (C7)**: dashed lines of symmetry plus a fraction tag under each letter that can be cut out (1/2 for E, T, K, V; 1/4 for X, O; none for N). The tags use the LP answer text. **T3 Q2 solution (C9)**: the same lines without tags (its answer is the three lists). Both are derived from their own question diagram.
- **T4 (C10 / C11)**: the book question sends the learner to the 16 pictures on the page border. The figure draws only the two the question names (diya, boat); the other 14 border pictures are not drawn (they are not named, and the task is open). The solution adds the vertical dashed line on both. Question borderline (see section 3).
- **T5 C12 (pinwheel)**: the pinwheel has blades pointing top / right / bottom / left (a hypotenuse along each axis) so that the LP words "top blade, right blade, bottom blade, left blade" match the picture. Dot offsets from the centre: (-0.15,0.5), (0.5,0.15), (0.15,-0.5), (-0.5,-0.15) = the clockwise quarter-turn rule (x,y) -> (y,-x).
- **T6 question (C15)**: five pinwheels exactly as the book (initial, 1/4, 1/2, 3/4, full turn), same pinwheel shape and dot offsets as C12. I did **not** draw the book's red dashed arrow in the first firki (the question does not use it).
- **T6 solution (C16)**: `none`, `SAME_AS_QUESTION_DIAGRAM`. The answer is "Yes, it looks the same after every turn"; the earlier author's hint was a tick under each picture, which only repeats the word Yes. Sibling check with T7/T8: those solutions add NEW pictures (the turned H, the filled table), so they are required; this one adds nothing new.
- **T7 (C17 / C18)**: the LP turns the book's worked row of the H into a question. Question diagram: the start H only (pink pivot dot at the crossbar centre, dark dots at the two stem tops). Solution diagram: the printed answer row (start, 1/4, 1/2, 3/4, full turn; dashed outline of the upright H behind the two sideways pictures). The book's last cell "Yes, at 1/2 turn" is the answer sentence and is not drawn. Dot positions after each turn were checked against the page picture (right ends at 1/4 turn, bottom ends at 1/2, left ends at 3/4).
- **T8 (C19 / C20)**: question = the book's table with the three letters I, X, Y in the first column and all other cells empty (header row kept: it is part of the table the learner fills, so this is not a HEADER_BOXES_ONLY case, the cells carry letter pictures). Solution = the same table filled: each letter turned 1/4, 1/2, 3/4, full about its pivot dot, last column "Yes, at 1/2 turn" / "Yes, at 1/4 turn" / "No" (values filled in, the book's own cell wording). The row tags (a), (b), (c) are drawn because the LP answer refers to the letters by (a), (b), (c) (user decision 3). The Y turns about the red dot at the bottom of its stem (as the LP's `q_figure` says).
- **T10 Q1 (C23 / C24)**: question = the ten digits with the 1 as a plain bar (the LP solution itself says the 1 is drawn as a bar, so the picture matters). Solution = dashed lines (vertical on 1, 8, 0; horizontal on 1, 3, 8, 0) and a half-turn arrow under 1, 8, 0. The earlier author suggested ticks and stars instead; I drew the actual lines because they show WHY (consistent with the letters of T3).
- **T10 Q2 (C25 / C26)**: question = 11 (two bars) and 1001 (bar, ring, ring, bar). Solution = a vertical dashed line through each number and a half-turn arrow under each.
- **T10 Q3 (C27 / C28)**: both `none` (`OPEN_ENDED`, `TEXT_SUFFICIENT`): no figure is given and the sample answer is a list of numbers. Borderline (section 3).
- **T11 worked C29**: three panels (Start / For 1/2 turn / For 1/4 turn): circle + top triangle, then the bottom triangle added, then the left and right triangles added (ANSWER). Triangle base = height = 0.8, circle diameter 0.9 (the LP gives no sizes; smaller than the diameter so the four triangles of the last panel do not overlap).
- **T11 worked C30**: three squares (Start with the two dashed lines of symmetry, after a 1/2 turn: unchanged, after a 1/4 turn: colours swapped). Orange = SET_B, blue = SET_A.
- **T12 (C32 / C33)**: question = the book's design (centre circle, left and right triangles pointing away, top and bottom triangles pointing at the circle, extra circle at the right tip). Solution = two designs side by side labelled (b) and (c) (the LP answer refers to them by these letters, user decision 3): (b) adds a circle at the left tip + vertical and horizontal dashed lines; (c) four equal arms, each a triangle with its flat side on the centre circle and a circle at its tip, + vertical, horizontal and two diagonal dashed lines. In (c) neighbouring triangles overlap slightly at the corners next to the circle (their bases are 1.3 times the circle's diameter, the book's size); the spec says draw order and keep the outlines.
- **Figure inventory claims**: `P01-fold_steps-1` -> concept image `M1.S1.T1.C1.IMG1` (the A cutting steps). `P01-fold_steps-2` (H cutting steps) and `P02-fold_steps-1` (firki making steps) -> `none:TEXT_SUFFICIENT` (teaching figures; the steps are in the text and no concept image or item of this chunk needs them). The table of p.03 is used three times, so: `P03-table-1` -> C17 question (H start), `NEW-P03-table-1-Hrow` -> C18 solution (the printed H answer row), `NEW-P03-table-1-IXY` -> C19 question (the I, X, Y rows).
- All media ids: a pair item takes `.IMG1` of its own concept (the old cards of the pair are replaced); worked examples take `.IMG2` because `.IMG1` is the kept teaching image of that concept. No teaching image is linked anywhere.

## 2. LP text issues (no LP text was changed; no decision was changed because of them)

| Concept | What is wrong or missing | Suggested sentence |
|---|---|---|
| M1.S4.T4.C10 | The question sends the learner to "the border of the page", which the learner of the plan does not have. | "Look at the pictures: a diya and a paper boat. Use lines of symmetry to make paper cutouts of the diya, the boat and other designs." |
| M2.S5.T5.C13 | Steps give a dot for the Z (top left) but not for the T; the figure draws the T without a dot. | "T: put a dot at the left end of the bar of the T." (then the figure can draw that dot) |
| M2.S6.T6.C15 | The text does not say what the firki looks like or where the dot is (only the figure shows it). | "The firki has four blades and a green dot on one blade." |
| M2.S7.T7.C17 | "Dots have been marked on it" but not where. | "The H has a dot at its centre and a dot at the top of each of its two sides." |
| M2.S8.T8.C19 | "Fill the table" but the text has no table; the dots are not described. | "Fill the table below. Each letter has a dot at its centre (for the Y, at the bottom of its stem) and small dots that show which way it is turned." |
| M2.S9.T9.C21 | The plus sign has four lines of symmetry (vertical, horizontal and two diagonals); the steps name only two. Not wrong, but incomplete. The figure draws only the two named lines. | "The plus sign has a vertical line, a horizontal line and two diagonal lines." (then the figure would draw the diagonals too) |
| M2.S10.T10.C23 and M2.S10.T10.C25 | The question text does not say the digit 1 is drawn as a plain bar (only the solutions say so). | "In this book the digit 1 is drawn as a plain straight bar." |
| M3.S11.T11.C29 | "one triangle above it, pointing up" does not say the triangle touches the circle, and the direction of the turn is not stated in the question. | "A design has a circle in the middle and one triangle above it, with its flat side touching the circle and its point up. Turn it to the right." |
| M3.S12.T12.C32 | The question text says "the design" without describing it. | "The design has a circle in the middle, a triangle on each of its four sides and a second circle at the tip of the right triangle." |

## 3. Borderline

- **Worked examples C3 (M), C4 (B, W, H), C21 (M, S, plus), C13 (Z, T), C12 (pinwheel)**: all required. The LP steps already carry the reasoning in words and the letters are familiar, so a careful student could follow them without a picture; I kept them required because every one asks about a fold line or a turn of a shape (`SPATIAL_GEOMETRY`) and the answer is itself a set of marks or positions on the shapes, and because of decisions 4 and 5. Weakest cases: C3 (the letter M) and C4.
- **T3 Q1 and Q2 questions**: the letters are also named in the text; required because the book prints the row and the symmetry of a letter is a property of its drawn shape.
- **T4 question (C10)**: the task is an open cutting activity; required only because it points at the printed pictures.
- **T6 solution (C16)**: `none` (could be argued `required` with ticks under the five pictures).
- **T10 Q3 (C27, C28)**: `none`; a picture of 69, 38 and 88 with a half-turn arrow and a horizontal line would be possible but the sample answer is a plain list of numbers.
- **T10 Q1 solution (C24)**: lines and half-turn arrows (not ticks and stars); ten digits with up to three marks each is the busiest of the letter/digit pictures.
- **T8 solution (C20)**: the largest spec (3 rows x 4 turned letters + 3 verdict texts). The verdict cell text "Yes, at 1/2 turn" has four words (the book's own wording, "values filled in").
- **T12 solution (C33)**: two designs in one picture; two designs because the LP describes both (b) and (c).

## 4. Where the book is unclear (and what I did)

- **No book print slip** was found in this chunk (no wrong digit, count or sign), so user decision 1 was not needed. The book has no printed solutions section.
- **P02-rotation_sequence-2**: the dot is about 0.5 blade-lengths from the pin; exact distance not measured (the picture only fixes the side of the pin: upper-left, right, below, left). The red dashed arrow in the first firki is unexplained in the text and not drawn.
- **P03-table-1**: the letter in row 2 is a plain vertical bar (read as capital I, as in the LP). The red dot of the Y is "low on the stem": drawn at the bottom end of the stem (the LP's `q_figure` agrees); because the Y has no rotational symmetry the exact pivot does not change the answer. The book colours letters; I draw them all in MARK_FILL with outlines.
- **P01-letters-3 / P03-digits-2**: the book colours every letter and digit differently; drawn in INK only. Whether a letter has a line of symmetry depends on the font (E, K, O); the LP answers follow the book's sans-serif letters.
- **P01-border_shapes-4**: only the diya and the boat are drawn; their outlines were read from a small picture and approximated with simple curves (diya) and a trapezium plus triangle (boat), both exactly mirror-symmetric.
- **P04-pattern-1**: matches the base description (checked against the page picture): triangle base and height about 1.3 times the circle's diameter.

## 5. Required items with no printed book figure (the 14 validator warnings)

Worked examples C3, C4, C12, C13, C21, C29, C30 (the examples are the LP's own, the book prints no figure for them) and the solutions C7, C9, C11, C20, C24, C26, C33 (the book has no printed solutions; their figures are the LP answers drawn).
