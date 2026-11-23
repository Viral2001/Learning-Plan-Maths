# Notes, chunk A (Class 8 Ch 9, topics M1.S2.T2, M2.S3.T3, M2.S4.T4, M2.S5.T5)

Result: 29 items (17 worked examples, 6 question/answer pairs = 12 items). Required 13 (worked 9, question 2, solution 2), optional 0, none 16 (worked 8, question 4, solution 4). Validator: errors 0, one warning (C34 solution has no printed book figure to claim: the book has no solutions section).

| concept | role | decision | media id | reason codes |
|---|---|---|---|---|
| M1.S2.T2.C3 | worked_example | none | - | TEXT_SUFFICIENT |
| M1.S2.T2.C4 | worked_example | required | M1.S2.T2.C4.IMG1 | ANSWER_IS_FIGURE, SPATIAL_GEOMETRY |
| M1.S2.T2.C5 | worked_example | required | M1.S2.T2.C5.IMG3 | FIG_REFERENCED, SPATIAL_GEOMETRY |
| M1.S2.T2.C6 | worked_example | required | M1.S2.T2.C6.IMG1 | FIG_REFERENCED, DATA_IN_FIGURE, ANSWER_IS_FIGURE |
| M1.S2.T2.C7 | worked_example | required | M1.S2.T2.C7.IMG1 | FIG_REFERENCED, DATA_IN_FIGURE |
| M1.S2.T2.C8 | worked_example | required | M1.S2.T2.C8.IMG1 | FIG_REFERENCED, SPATIAL_GEOMETRY |
| M1.S2.T2.C9 | worked_example | required | M1.S2.T2.C9.IMG1 | FIG_REFERENCED, SPATIAL_GEOMETRY |
| M1.S2.T2.C10 | worked_example | required | M1.S2.T2.C10.IMG3 | FIG_REFERENCED, HIGHLIGHT_MEANING |
| M1.S2.T2.C11 | worked_example | required | M1.S2.T2.C11.IMG1 | FIG_REFERENCED, SPATIAL_GEOMETRY |
| M1.S2.T2.C12 | worked_example | none | - | TEXT_SUFFICIENT |
| M2.S3.T3.C14 | worked_example | required | M2.S3.T3.C14.IMG2 | FIG_REFERENCED, SPATIAL_GEOMETRY |
| M2.S3.T3.C16 | worked_example | none | - | LATEX_ARITHMETIC, TEXT_SUFFICIENT |
| M2.S3.T3.C17 | worked_example | none | - | LATEX_ARITHMETIC |
| M2.S3.T3.C18 | worked_example | none | - | LATEX_ARITHMETIC |
| M2.S3.T3.C19 | worked_example | none | - | TEXT_SUFFICIENT, LATEX_ARITHMETIC |
| M2.S4.T4.C22 | worked_example | none | - | LATEX_ARITHMETIC, LATEX_TABLE |
| M2.S4.T4.C25 | worked_example | none | - | TEXT_SUFFICIENT, LATEX_ARITHMETIC |
| M2.S5.T5.C27 | question | required | M2.S5.T5.C27.IMG1 | DATA_IN_FIGURE, SPATIAL_GEOMETRY |
| M2.S5.T5.C28 | solution | required | M2.S5.T5.C28.IMG1 | FIG_REFERENCED, ANSWER_IS_FIGURE |
| M2.S5.T5.C29 | question | none | - | TEXT_SUFFICIENT |
| M2.S5.T5.C30 | solution | none | - | LATEX_ARITHMETIC, TEXT_SUFFICIENT |
| M2.S5.T5.C31 | question | none | - | TEXT_SUFFICIENT |
| M2.S5.T5.C32 | solution | none | - | LATEX_ARITHMETIC |
| M2.S5.T5.C33 | question | required | M2.S5.T5.C33.IMG1 | FIG_REFERENCED, DATA_IN_FIGURE, ACTION_ON_FIGURE |
| M2.S5.T5.C34 | solution | required | M2.S5.T5.C34.IMG1 | ANSWER_IS_FIGURE, SPATIAL_GEOMETRY |
| M2.S5.T5.C35 | question | none | - | TEXT_SUFFICIENT |
| M2.S5.T5.C36 | solution | none | - | LATEX_ARITHMETIC |
| M2.S5.T5.C37 | question | none | - | TEXT_SUFFICIENT |
| M2.S5.T5.C38 | solution | none | - | LATEX_ARITHMETIC |

## 1. Judgement calls

**Worked-example policy (applies to C4 to C14).** A worked example has ONE diagram, placed after the question text, and the steps follow straight away. So the diagram shows the whole figure the steps use: the given part in INK, whatever the steps add (diagonal, extended lines, second triangle, arrangement) in ANSWER green; numeric answers (triangle counts 2/4/8, areas, the fraction one half) are never printed on it, they stay in the text. Reason: a figure showing only the given square would be useless for C4, C5, C10.

**C4 (Where does Baudhayana build the double square?), required, ANSWER_IS_FIGURE.** The verbal answer is "on the diagonal", but the steps describe a construction, and Step B2 says a construction answer is drawn even when the steps describe it in words. Teaching image C3.IMG2 shows the same picture but is never linked, so the item gets its own. If you prefer text-first here, flipping C4 to none costs nothing else in the map.

**C3 and C12, none (TEXT_SUFFICIENT).** C3 is a word problem with all numbers in the text and its picture is teaching image C3.IMG1; C12 asks for a fraction and a count and the book gives no figure with that question (its fold picture belongs to C11). A square folded into 4 equal small squares would help C12 but is not needed (not marked optional, to keep to "prefer none").

**C5 and C9 share one diagram.** Same book picture (base P02-construction-2), so identical specs; C9 says "same as C5" in render_note. No 45-degree arcs are drawn for C9 although its steps talk about 45 degrees: the book's picture has none and the one-picture-one-spec rule applies. If you want them, add arcs labelled 45 at both ends of the diagonal (at (0,2) between the diagonal and the horizontal line, and between the horizontal line and the left upper side of the dotted square, and the same at (2,0) with the vertical line).

**C6.** The diagram shows the finished arrangement (pieces 5-8 on the four sides of Square 1 give a tilted square of 8 triangles against 4), with the piece numbers of the book's p.3 picture. The book and the LP do not say which of 5, 6, 7, 8 goes on which side: the spec uses 5 left, 6 top, 7 right, 8 bottom (any order gives the same outline). Flagged `needs_lp_text_sync: true`.

**C7.** The counted shapes (quarter square, diamond, whole square, and the three result shapes) get MARK_FILL; the book only uses heavy outlines. Counts are not printed (they are the answer). Same picture as teaching image C5.IMG2 (never linked).

**C10 and C11.** C10 shades the inside tilted square (MARK_FILL) so "the smaller inside square" can be identified; C11 is clean geometry of the folded paper with the book's letters (P bottom, Q right, R top, S left); fold arrows and paper texture of the book are left out. The "centre" has no letter in the LP text so it gets none.

**C14.** Lettered figure of the book's General Solution. The generic a and c are written, no numbers; the scale a = 2 is only the drawing scale (stated in render_note). Teaching image C14.IMG1 has the same geometry but is never linked, so C14 gets C14.IMG2.

**Q1 (C27 question, C28 solution).** Question: the book's triangle with 1, 1 and ? (required, see Borderline). Solution: the triangle P-E-R of the question sits at the same place and scale, everything added is ANSWER; the root-two label replaces the question mark; the tags '1 square unit' and '2 square units' use the LP solution's own words (at most 3 words), placed beside the figure with FOCUS pointers so they do not crowd the figure.

**Q4 (C33 question, C34 solution).** Question: the book's two cut squares with pieces 1 to 4 (the pieces are drawn 0.15 unit apart to show the cut, as in the book). Solution: the four same pieces rearranged with the right angles meeting at the centre; `derived_from` is the question diagram (same pieces, numbers and style) although the positions necessarily change because the answer IS the rearrangement. The assignment of pieces to quadrants (1 upper-right, 2 upper-left, 3 lower-left, 4 lower-right) is mine; flagged `needs_lp_text_sync: true`.

**Pairs Q2, Q3, Q5, Q6 (C29-C32, C35-C38), none.** No book figure with any of these questions; the answers are arithmetic, lists of last digits, or numeric chains. Q5's five parts (i)-(v) share one card and get the same decision for all (sibling consistency).

**C16, C17, C18, C19, C22, C25, none.** Examples 1 and 2 and the check have no figure of their own in the book; C19 ("diagonal of a square with side 5 cm") has no book figure; C22's book boxes are plain lists of squares of decimals whose red pairs are already described in words in the LP steps (text_alternative gives the LaTeX array); C25 is algebra and prime counting.

**Inventory mapping.** Base figures that are teaching figures and also the source of a worked example's own diagram have two entries: the base id for the teaching use (concept_image) and a `NEW-<base id>-<concept>` entry for the item's diagram (P02-construction-1/-2, P03-construction-1, P04-construction-3, P04-paper_cutout-4, P05-construction-2, P08-construction-1). P01-shape-1 and P04-shape-1 (plain given squares with two ticks, no data) are none:TEXT_SUFFICIENT. P04-construction-2 (dotted inscribed square) is accounted by concept image C10.IMG1, P05-shape-3 and P05-construction-2 by C20.IMG1 and P06-table-1 by C21.IMG1 (these three rely on the concept-image descriptions, whose last sentences are cut off in concept_images.json). P06-digit_boxes-2 (row of boxes ending in 6) is none:LATEX_ARITHMETIC (HEADER_BOXES_ONLY would also fit).

## Borderline (decision 4)

- **M2.S5.T5.C27 (Q1 question) required.** The LP text already says "equal sides are 1 unit", so the tie-breaker alone would give none. Kept required because the book question gives this triangle with the lengths marked on its sides (DATA_IN_FIGURE, SPATIAL_GEOMETRY) and decision 4 says not to flip for the numbers being in the text. If flipped, C28 loses its `derived_from` (it would stand alone), nothing else changes.
- **M1.S2.T2.C4** required although the answer is one short phrase (see above).
- **C5, C8, C9, C10** required because the questions point at "the dotted square", "these small triangles", "the smaller inside square" without any other description; a reviewer who wants fewer pictures could treat C9 as the first to drop (same picture as C5).
- **C3, C12, C30** none although a small picture could help (2x2 copies, folded square, nested squares of area 1, 2, 4).
- **C16, C18** examples stay none although the General Solution figure (C14) exists; they are numeric.

## 2. LP text issues (no LP text was edited)

- **M1.S2.T2.C6** question/steps: the pieces 5-8 are placed "against one side of Square 1" without saying which side each piece takes; "Square 1" and "Square 2" exist only in the book's picture. Suggested sentence: "Place piece 5 on the left side of Square 1, piece 6 on the top, piece 7 on the right and piece 8 on the bottom (any order gives the same shape)."
- **M1.S2.T2.C7** question: "Adding more lines gives a sequence of squares" does not say which squares. Suggested: "On the same grid of 8 small triangles look at the small square, the tilted square and the big square. How many small triangles make each of these squares?"
- **M1.S2.T2.C8** question: "All these small triangles" has nothing for "these" to point at. Suggested: "In the figure of the square on the diagonal with the extra east-west and north-south lines (8 small triangles in all), all the small triangles are congruent. Can you explain why?"
- **M1.S2.T2.C9** question: "the dotted square" is not introduced. Suggested: "the dotted square built on the diagonal of the original square".
- **M1.S2.T2.C11** question: P, Q, R, S are used before they are placed (step 1 says they are midpoints). Suggested: "P, Q, R and S are the midpoints of the bottom, right, top and left sides of the paper." The centre of the paper has no name; steps 2, 3 and 7 say "the centre".
- **M2.S3.T3.C14** steps: P, Q, R, S, U, V are used without saying which triangle is meant or where U and V are. Suggested first line: "Let PQS be the isosceles right triangle with the right angle at P, PS = PQ = a and hypotenuse SQ = c; R is the fourth corner of the square PQRS, and SQVU is the square on SQ, with U above R and V to the right of R."
- **M2.S5.T5.C28** steps: "the unit square PEAR", "ER" and "REST" are used without a description of where P, E, A, R, T, S are. Suggested: "Name the triangle PER with the right angle at P (PR = PE = 1); A is the fourth corner of the unit square PEAR; T is directly above A and S directly to the right of A, so REST is the square on ER."
- **M2.S5.T5.C33** question: "pieces 1 and 2, and 3 and 4" without saying which triangle is which. Suggested: "(in the book's picture pieces 1 and 3 are the lower-left triangles and pieces 2 and 4 the upper-right triangles)".
- **M2.S5.T5.C34** answer: "put the four right-angle corners together at the centre" does not say which piece goes where; suggested: "for example piece 1 upper right, 2 upper left, 3 lower left, 4 lower right".
- **M2.S3.T3.C19** `book_number` reads "Chapter Exercises, Q1" while the book heading at the end of section 2.7 is "Figure it Out", Q1 (p.52). Not wrong, only the label.
- No LP/book numeric contradictions found. All sums, squares and bounds were re-computed (1.1^2 to 1.415^2 of p.6; 4.2^2/4.3^2 for 18, 5.6^2/5.7^2 for 32, 8.4^2/8.5^2 for 72, 11.3^2/11.4^2 for 128, 12.7^2/12.8^2 for 162, 7.07^2/7.08^2 for 50).

## 3. Where the book itself is unclear or a base description was wrong

- **Base P02-construction-2 (corrected in my entries, "CORRECTED:").** The base says the original square holds 2 of the dotted square's 4 triangles. Only ONE of them is inside the original square (the half above the diagonal); the other half of the original square (below the diagonal) lies outside the dotted square. Matches the LP step "the original holds 2 triangles, the dotted square 4" only when the outside half is counted for the original.
- **Book mistakes:** none found in the figures of this chunk (decision 1 not needed).
- **p.3 paper picture:** says "place pieces 5, 6, 7, 8 around Square 1" but not which side each takes (see C6).
- **p.7 Figure it Out Q1 picture:** the gap between the two pieces of each square is drawn but its width is not given; the spec uses a shift of 0.15 unit up and right.
- **No printed solutions section:** C28 and C34 diagrams are built from the LP solution text (the book's p.5 figure covers C28's squares; nothing in the book shows the answer of Q4).
- **Printed-figure letters:** the book's p.2 and p.4 figures carry no letters while the teaching images (A, B, C, ...) do; the worked-example specs follow the book and the LP text (no letters in C4-C10).
