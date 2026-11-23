# Class 5 Ch 10 Symmetrical Designs - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths5_ch10` v4 (taken from staging). Result: new V2 version v5 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (49 items from 29 units)
{"worked_example": {"required": 9}, "question": {"required": 16, "none": 4}, "solution": {"required": 16, "none": 3, "optional": 1}}

Optional, NOT added: [('C35', 'solution')]

needs_lp_text_sync: [('C53', 'question'), ('C56', 'solution')]

## The 41 diagrams
| id | side | type |
|---|---|---|
| M1.S2.T2.C3.IMG2 | worked example | symmetry_figure |
| M1.S2.T2.C4.IMG2 | worked example | symmetry_figure |
| M1.S3.T3.C6.IMG1 | question | symmetry_figure |
| M1.S3.T3.C7.IMG1 | solution | symmetry_figure |
| M1.S3.T3.C8.IMG1 | question | symmetry_figure |
| M1.S3.T3.C9.IMG1 | solution | symmetry_figure |
| M1.S4.T4.C10.IMG1 | question | symmetry_figure |
| M1.S4.T4.C11.IMG1 | solution | symmetry_figure |
| M2.S5.T5.C12.IMG2 | worked example | symmetry_figure |
| M2.S5.T5.C13.IMG2 | worked example | symmetry_figure |
| M2.S6.T6.C15.IMG1 | question | symmetry_figure |
| M2.S7.T7.C17.IMG1 | question | symmetry_figure |
| M2.S7.T7.C18.IMG1 | solution | symmetry_figure |
| M2.S8.T8.C19.IMG1 | question | symmetry_figure |
| M2.S8.T8.C20.IMG1 | solution | symmetry_figure |
| M2.S9.T9.C21.IMG2 | worked example | symmetry_figure |
| M2.S10.T10.C23.IMG1 | question | symmetry_figure |
| M2.S10.T10.C24.IMG1 | solution | symmetry_figure |
| M2.S10.T10.C25.IMG1 | question | symmetry_figure |
| M2.S10.T10.C26.IMG1 | solution | symmetry_figure |
| M3.S11.T11.C29.IMG2 | worked example | symmetry_figure |
| M3.S11.T11.C30.IMG2 | worked example | symmetry_figure |
| M3.S12.T12.C32.IMG1 | question | symmetry_figure |
| M3.S12.T12.C33.IMG1 | solution | symmetry_figure |
| M3.S13.T13.C34.IMG1 | question | cell_grid |
| M3.S13.T13.C36.IMG1 | question | symmetry_figure |
| M3.S13.T13.C37.IMG1 | solution | symmetry_figure |
| M3.S13.T13.C38.IMG1 | question | symmetry_figure |
| M3.S13.T13.C39.IMG1 | solution | symmetry_figure |
| M3.S14.T14.C41.IMG1 | solution | tiling |
| M3.S14.T14.C42.IMG1 | question | symmetry_figure |
| M3.S14.T14.C43.IMG1 | solution | symmetry_figure |
| M3.S14.T14.C45.IMG1 | solution | tiling |
| M3.S15.T15.C46.IMG2 | worked example | symmetry_figure |
| M3.S15.T15.C47.IMG2 | worked example | symmetry_figure |
| M3.S16.T16.C49.IMG1 | question | other |
| M3.S16.T16.C50.IMG1 | solution | other |
| M3.S17.T17.C51.IMG1 | question | symmetry_figure |
| M3.S18.T18.C53.IMG1 | question | other |
| M3.S18.T18.C54.IMG1 | solution | other |
| M3.S19.T19.C56.IMG1 | solution | symmetry_figure |

### Chunk A notes (from the decision agent)
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

### Chunk B notes (from the decision agent)
# Notes, chunk B (Class 5 Ch 10 "Symmetrical Designs", topics M3.S13.T13 to M3.S19.T19)

Result: 22 items, required 17 / optional 1 / none 4, validator errors 0 (10 warnings: required solution or worked-example figures that are not printed in the book, which the validator allows).
Required: questions C34, C36, C38, C42, C49, C51, C53; solutions C37, C39, C41, C43, C45, C50, C54, C56; worked examples C46, C47.
Optional (not added): C35 solution. None: C40, C44, C55 questions; C52 solution.
Every drawn shape was checked by computation (shapely) on the exact coordinates in the specs: the 19 border shapes, the three designs of squares and triangles, the 4-square shape. All symmetry facts the LP states hold for the drawn shapes.

## Borderline

- **M3.S13.T13.C35 (Let Us Think Q1, solution): optional, not added.** Figure-based question with a Yes/No answer; the LP steps name every colour cell by cell, so text carries it ("typical pair": Q required, S none). Figures that would help: the square after a 1/2 turn (identical) and after a 1/4 turn (green and pink swapped). If the user wants them drawn, flip to required and derive it from C34.IMG1.
- **M3.S17.T17.C52 (design B, solution): none.** The question figure already shows the 4 hearts and both dashed lines (the book draws them); the answer is two words. Only a turn arrow would be new. Sibling check: C35 and C52 are the same kind of answer (figure given, short fill-in) and are treated alike (nothing drawn); C35 is `optional` because the turned pictures carry new information, C52 is `none` because they would not.
- **M3.S15.T15.C46 and C47 (worked examples): required, one diagram each.** The book has no figure for these LP-authored examples. C46: the answer to "what does the whole print look like" IS a drawing (ANSWER_IS_FIGURE), so the single diagram shows the given half print, an arrow, and the whole print with the copied half in ANSWER green. This shows the answer before the steps (a worked example is not a test), the alternative would be to draw the half print only. C47: SPATIAL_GEOMETRY, the print (flower at the top, the same flower turned a half turn at the bottom). Per the 23 Nov decision both get their own diagram although the kept teaching images show the same pictures; media ids C46.IMG2 and C47.IMG2 (IMG1 is the kept teaching image).
- **M3.S16.T16.C49 / C50 (matching blocks to prints): required, but the book shows PHOTOGRAPHS** of carved wooden blocks. The rule list has NOT_RENDERABLE for photographs; I kept it required because the question cannot be attempted without the blocks and prints (FIG_REFERENCED / DATA_IN_FIGURE / ACTION_ON_FIGURE all hold). The spec asks for flat line-art glyphs that keep each block's identifying shape and its exact half print (drop, lotus, rosette, fan, plant; halves cut on the vertical middle line, sides checked on the page picture). If the team prefers the real photographs cropped from the book (page 5, tiles (i)-(v) and (a)-(e)), the layout and the lines of the solution stay as specified. Decide before drawing.
- **M3.S14.T14.C41, C45 and M3.S19.T19.C56 (open sample answers): required.** The questions are open ("make your own designs", "create patterns"), but the LP solution gives a concrete sample (three designs; a block printed 4 times at quarter turns), and the answer is an arrangement (Step B2, ANSWER_IS_FIGURE). The questions C40, C44, C55 get no diagram (no given figure). C41 and C45 draw the same three designs (C45 regrouped under the three category titles the LP uses, exactly as in C41). C56: the LP only says "a simple shape", so I chose a drop-shaped print so that each quarter turn is visible; `needs_lp_text_sync: true` (the LP text could say "a drop shape").
- **M3.S13.T13.C38 (Let Us Think Q3, question): required, two designs.** The book says only "these designs" (the 2 x 2 square above and the square the student colours). The LP's own figure hint shows both designs, so the question figure shows the green-pink square and the orange-blue square, the latter coloured as in the LP solution of the previous question (orange first, going clockwise from the top of the vertical line). Strictly the second design is the answer of the previous question, not given by the book. Alternative: draw only the green-pink square on the question side.
- **M3.S18.T18.C53 / C54 (19 border shapes): required.** Numbers 1 to 19 are shown next to the shapes in BOTH figures because the LP solution refers to "Shape 13" etc. (see LP text issues). Layout: the book border is a page frame (5 shapes on the top, 5 on the right, 4 at the bottom, 5 on the left); the diagram uses a 7 x 5 ring (7, 3, 6, 3 shapes) so that it fits a 16:9 card; the order round the ring is unchanged. Solution marks differ in shape (tick, star) and colour (ANSWER green, SET_A blue).
- **M3.S14.T14.C42 / C43:** the triangles of the 4-square shape are drawn as printed (base 1.8, height 1.8, not equilateral); the LP calls them just "triangles", while C40/C41 talk about equilateral triangles (those are the cut-outs).
- **Colours:** green, pink, blue and sand of the designs are the book's own colours (explicit hex values, since the style tokens have no pink or sand). In the orange-blue square the fills use SET_B and SET_A (the LP names the colours) instead of ANSWER green.
- **Figure claims:** P05-photo_pair-2 (block and print photographs) and P06-photo_pair-1 (design A print) are teaching figures that no LP item draws; mapped to none (DECORATIVE_ONLY, TEXT_SUFFICIENT). Design A (4 leaf motifs at quarter turns) is the book's own example; the LP's worked example C47 replaces it with a two-stamp flower, and no LP item asks about design A. The two NEW- entries are the second uses of P04-pattern-2 and P04-grid-3 in the question of C38.

## LP text issues

- **M3.S18.T18.C53 (question):** the text does not say that the shapes are numbered; the solution (C54) uses "Shape 1 ... Shape 19". Suggested sentence after the question: "The shapes are numbered 1 to 19 round the border, starting at the top-left corner and going to the right."
- **M3.S13.T13.C38 (question):** "Do these designs" does not say which designs. Suggested: "Look at the green and pink square and at the orange and blue square you coloured. Do these designs have reflection symmetry also? Draw the lines of symmetry."
- **M3.S19.T19.C55 (question):** "Some are shown below." but no picture follows in the LP (decision none). Suggested: "Create symmetrical patterns and designs using vegetable blocks, for example a cut ladyfinger or a carved potato."
- **M3.S14.T14.C40 (question):** "These are provided at the end of the book." the LP has no such pieces. Suggested: "Cut out squares and equilateral triangles of paper, all with the same side length."
- **M3.S14.T14.C41, C45, M3.S19.T19.C56 (solutions):** the closing sentences repeat each other ("Sample answer: ... Your answer may differ." appears as a step and again in the answer line). Suggested: keep one of the two.
- **M3.S18.T18.C54:** the steps for shape 4 and shape 9 say "drawn nearly even"; the diagram draws them exactly regular (see the book notes below). Shape 15 "with a square corner" is true (right angle between the two shorter sides, checked on the drawn coordinates).

## Book unclear or different from the base inventory

- Page 4, "How many times does this shape look the same during a full turn?" could refer to the 2 x 2 square above (answer 2: after a 1/2 turn and the full turn) or to the coloured square (answer 4, the LP's reading). Followed the LP.
- Page 4, "Do these designs have reflection symmetry also?": the designs are not named (see LP issue above).
- Page 6, border shapes (checked against the picture, base descriptions corrected in `figure_inventory`):
  - shape 3 is not a regular hexagon: its width and height are about equal (a regular one is wider than tall), so it has 2 lines and a half turn, as the LP says;
  - shape 7: the rhombus is tilted about 9 degrees (base said untilted); its diagonals are perpendicular;
  - shape 9: a ring of 10 triangular tips in 5 mirror pairs, drawn slightly uneven; drawn regular with 5 lines and a 1/5 turn as the LP says;
  - shape 4: the top arm is a little shorter than the other two (drawn equal, LP: 3 lines);
  - shape 5: the corner triangles cut off about 0.36 of each side (drawn exactly one third, so the middle is a regular hexagon);
  - shape 14: the grey triangle is about 8 percent larger than the yellow one (kept);
  - shape 16: two equal isosceles triangles (apex angle about 55 degrees) meeting at their apex along one common axis, so 2 lines and a half turn (the LP's answer), not a scalene bow-tie.
- Page 5, block printing prints: (a) and (c) show the RIGHT half of their block (straight edge on the left), (b), (d), (e) the LEFT half (straight edge on the right). The base inventory had this right.
- The pdf has no printed-solutions section; every answer follows the LP solution text. No LP solution contradicts the book.
- The book's design A (page 6) shows 4 leaf motifs and a filled-in sentence; it has no question, so nothing was drawn for it.
