# Chunk E notes: Class 5 Ch 7, topic M4.S28.T28 "Questions: Icosahedron and Dodecahedron"

Result: 12 items (6 pairs, concepts C124 to C135). Required 6 (questions C124, C126, C128, C130; solutions C129, C135), optional 0, none 6. Validator: errors 0, one warning (C135 solution has no printed book figure behind it, which is expected: the cube frame is the LP sample answer).

## 1. Judgement calls

- **One book picture, four question diagrams.** The only printed picture of the two solids (pdf page 12, dodecahedron on the left, icosahedron on the right) belongs to questions Q1 to Q4 of the page. Each of C124, C126, C128, C130 gets its own identical diagram (render_note "same as M4.S28.T28.C124.IMG1"). In figure_inventory the base ids P12-solid-1 and P12-solid-2 are mapped to C124; the further uses are NEW-P12-solid-1-C126 / -C128 / -C130 and NEW-P12-solid-2-C126 / -C128 / -C130; the solution figure of C129 redraws both solids, so NEW-P12-solid-1-C129sol and NEW-P12-solid-2-C129sol.
- **Names added under the solids.** The book prints no labels, but Q2, Q3 and Q4 ask separately about the icosahedron and the dodecahedron, so a learner must know which solid is which. I put the two names (from the question text) under the solids. I kept the book's left/right order (dodecahedron left) although the question text lists the icosahedron first.
- **Drawing style.** The book shades the faces violet and pink in alternating tones. Colour carries no meaning here (and "do all faces look the same" must not be confused by colour), so all visible faces are one neutral CELL_FILL, edges INK, hidden edges dashed GUIDE (as the book also draws them dashed, so that edges can be counted without missing any). The solids are exact orthographic views along a 5-fold axis (dodecahedron, front pentagon pointing down, ten-sided outline) and a 3-fold axis (icosahedron, front triangle pointing down, hexagonal outline). The book's picture is slightly perspective; the views are the same orientation. Full vertex, edge and face lists are in the spec so the renderer guesses nothing.
- **Q1 question required.** The book's Q1 says to count faces (and the line after it tells the learner to make models from nets). The LP question has no model, so the picture is what the learner counts on.
- **Q1, Q2, Q4 solutions none.** Q1: counts 20 and 12, but only 10 and 6 faces are visible in any one view, so a figure could not show the whole count and would only repeat the question figure. Q2: the answer is words (triangle, pentagon, yes). Q4: the solution is arithmetic (20 x 3 = 60, 12 x 5 = 60, halve).
- **Q3 solution required.** The solution picks a vertex and ticks the faces that touch it: a visible, local mark. The figure rings one vertex per solid (icosahedron V2, a vertex of the front triangle, 5 faces; dodecahedron V4, a vertex of the front pentagon, 3 faces), shades those faces MARK_FILL, numbers them clockwise from the top in ANSWER green, and adds the tags "5 faces" and "3 faces" (LP uses the same words). Only one vertex is marked in each solid; the LP's "a different vertex: again 5 / 3" cannot be shown without overlapping shaded faces, and it is covered by the accuracy check that every vertex has the same count (5 on all 12 icosahedron vertices, 3 on all 20 dodecahedron vertices). I chose vertices whose faces are all visible (the book's top vertex of the icosahedron has only 3 of its 5 faces visible in this view).
- **Q5 question none, solution none.** The question gives no figure (OPEN_ENDED). The sample answer is a cube and a dice; all counts are in the text. A cube with one corner marked would only make it nicer, so I did not make it optional either.
- **Q6 question none.** The book prints three straw-and-clay models under the question. The question never refers to them and asks nothing about them ("Which shapes did you make?"): they illustrate the activity (OPEN_ENDED). I counted them from the page picture: left model, blue balls, 6 balls and 12 straws (octahedron frame); middle model, green balls, 6 balls and 9 straws (triangular prism frame); right model, pink balls, 10 balls and 15 straws (pentagonal prism frame). All three are mapped none:OPEN_ENDED and are not drawn.
- **Q6 solution required.** The LP sample answer is an object the learner builds (cube frame, 12 straws, 8 balls of clay, 3 straws at each ball), i.e. a construction (B2 ANSWER_IS_FIGURE). The question has no given figure, so the solution draws it whole (derived_from null). Cabinet-style oblique cube, 9 visible straws solid, the 3 straws at the hidden back corner dashed GUIDE, 8 balls MARK_FILL, and a legend "12 straws" / "8 balls" in ANSWER (both strings are LP words, 2 words each).
- **Placeholders.** All ids are IMG1 (no kept images in any of the 12 concepts). Question tokens question_tex / after_question_text, solution tokens steps_tex / before_first_step. The Q3 solution is derived_from M4.S28.T28.C128.IMG1.

## 2. Borderline

- C125 (Ans1), C127 (Ans2), C131 (Ans4): none (no new visual content). C129 (Ans3): required (vertex marking), as explained above. Sibling-consistency reason is stated in C129's `reason`.
- C133 (Ans5): none, a cube with one corner marked would be nicer, not needed.
- C134 (Q6): none (OPEN_ENDED), although the book prints three models next to the question; C135: required (the sample answer is a built model).
- C124 (Q1): required although the LP text names no picture.
- Book picture colours not copied (neutral fill), see section 1.

## 3. LP text issues

- **M4.S28.T28.C124 (Q1)**: the question text does not mention the solids or the picture, but the learner needs to see them. Suggested sentence added after the question: "Look at the picture of the two solids." (The book also says "Use the nets provided at the end of the book to make icosahedron and dodecahedron models"; the LP leaves it out.)
- **M4.S28.T28.C126, C128, C130 (Q2, Q3, Q4)**: same gap; suggested: "Look at the picture of the icosahedron and the dodecahedron." Without it the blanks "Icosahedron: ___ Dodecahedron: ___" have nothing to refer to.
- **M4.S28.T28.C125 (Ans1)**: steps 1 and 2 say "ticking each face once", but a single picture shows only 10 of the 20 icosahedron faces and 6 of the 12 dodecahedron faces. Suggested: add "Turn the solid, or use your paper model, to count the faces at the back too."
- **M4.S28.T28.C129 (Ans3)**: step 1 and step 3 can point at the figure: "Pick one vertex, the one ringed in the picture, ..." so the figure and the text match.
- **M4.S28.T28.C135 (Ans6)**: nothing wrong, but the three models the book shows are never named in the LP; optional sentence: "The book shows an octahedron frame (6 balls, 12 straws), a triangular prism frame (6 balls, 9 straws) and a pentagonal prism frame (10 balls, 15 straws)."
- All numbers in the LP solutions were checked and are mathematically correct: icosahedron 20 triangles, 5 at each vertex, 30 edges; dodecahedron 12 pentagons, 3 at each vertex, 30 edges; 20 x 3 = 60 and 12 x 5 = 60; cube 6 faces, 8 corners, 12 edges, 3 faces at a corner; 8 x 3 = 24 = 12 x 2.

## 4. Where the book is unclear

- The pdf has no printed-solutions section, so the LP solution text is the only answer.
- The picture on page 12 has no labels; which solid is which is only clear from the shapes (and from the questions' wording). The names in the diagram are an addition from the question text.
- The picture is slightly perspective and shaded in violet and pink; the drawing is not an exact projection, but its orientation (pentagon face towards the viewer for the dodecahedron, triangle face towards the viewer and a vertex at the top for the icosahedron) matches the axis views used in the spec.
- The base inventory entry for the icosahedron says "a top vertex at the centre top where 5 triangles meet"; in the page picture only 3 of those 5 faces are visible there (the others are at the back). I did not change the base entry, but the Q3 solution marks a vertex of the front triangle instead, where all 5 faces are visible.
- The three straw models are unlabelled and not asked about; their ball and straw counts are in section 1.
