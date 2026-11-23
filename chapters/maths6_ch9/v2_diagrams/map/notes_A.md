# Chunk A notes (Class 6 Ch 9 Symmetry, topics T2 to T9, plan cbse_eng_maths6_ch9_v34)

Result: 31 items, required 21 / optional 4 / none 6, validator errors 0, warnings 0.
Required: worked C2, C10; questions C5, C7, C17, C19, C21, C32, C34, C36; solutions C6, C8, C18, C20, C22, C24, C26, C31, C33, C35, C37.
Optional (not added, a figure would help): solution C14 (square with 4 dashed lines), question C15 (rectangle with a diagonal), solution C16 (two cut triangles), worked example C27 (square ABCD with its vertical line).
None: worked C3 (photos) and C9; questions C13, C23, C25, C30.

## 1. Judgement calls

- **Worked C2 (triangle and puzzle, book Figure (a) and (b))**: required. The puzzle's bumps and holes, and the circle colours of the triangle, exist only in the picture; lettered figures are drawn even though teaching image C2.IMG1 shows a simplified version (not linked). New id `M1.S2.T2.C2.IMG2` because IMG1 is the kept teaching image. One diagram holds both panels, no letters drawn.
- **Worked C3 (Taj Mahal, Gopuram, clouds)**: none, `NOT_RENDERABLE` (photographs). The plan already has teaching image C3.IMG1 (outline of the Taj Mahal and a cloud). The Taj Mahal photo is accounted to that concept image, the Gopuram photo as `none:NOT_RENDERABLE`.
- **Q1 (C5/C6)**: question required, because the text points to the "pictures at the start of the chapter" and the LP never shows them (the concept image M1.S1.T1.C1.IMG1 has a different set, with a windmill and no flower, and is never linked). The solution is required although the printed answer is text only: the answer gives line counts (flower 6, rangoli 4, butterfly 1) and where the lines run is only visible in the picture; this keeps sibling consistency with Q2, Q6, Q7 where the printed answer draws the lines. This is the weakest "required" of the chunk; drop the solution figure if the user prefers text only.
- **Q1 pictures** are simplified flat redrawings of photographs and illustrations (butterfly, cloud). The rangoli is drawn with identical ornaments on all four sides so that the 4 lines in the answer are exact (see section 3).
- **Q2 (C7/C8)**: both required. Shapes 3 and 5 (no line) are repeated in the solution figure without a line.
- **C9 (fold the square four ways)**: none: the question gives no figure and teaching image C9.IMG1 already shows the four fold lines.
- **C13/C14 and C15/C16** (T5 prompts): question C13 none, solution C14 optional; question C15 optional, solution C16 optional. Reason: the shapes (square, rectangle) are described in words, the printed answers are text, and teaching images C9.IMG1 and C11.IMG1 already show the pictures.
- **Q6 (C17/C18)**: the LP keeps parts (a), (b), (c) in one concept, so one question diagram (tilted square, 8-pointed star, triangle, hexagon in a 2 x 2 layout) and one solution diagram (21 dashed lines).
- **Q7 (C19/C20)**: one diagram with 8 figures (4 rhombus clusters and 4 red grid figures).
- **Q8 kolam (C21/C22)**: spec built from a computed layout (7 stars of 6 rhombi, 6 outer and 6 inner rhombi, all side 1); a code check confirms the vertex set is mapped to itself by the 6 lines.
- **Q9 and Q10 (C23/C24, C25/C26)**: question none (nothing is given), solution required and stands alone (`derived_from` null) because the answer is a drawing. Q10 draws the first example of each part from the LP text: semicircle (1 line), ellipse (2), square with four semicircular bumps (4).
- **Worked C10 (three figures)**: required (question side, given figures only, no lines). The Koch outline is the Koch snowflake after 2 iterations (48 sides), fitted to the page picture with a vertex error of about 2.5 percent of its radius; the 25.25 degree rotation is part of the spec.
- **Worked C27 (square ABCD, vertical line)**: optional; the question text gives the corners in words and teaching image C27.IMG1 shows it.
- **T8 (C30/C31)**: question none (the same square is given in words); solution required because the answer is where labelled corners go after two reflections (arrangement of labels): two squares, mirror line, circles on A and C (they stay), double arrows for the swapping pairs.
- **T9 (Q11, Q12, Q13)**: one diagram of six panels each; panel (a) of Q11 (done for you) is part of the given figure and is repeated unchanged in the solution. Added mirror parts are ANSWER green dashed lines (as the book's dashed completion), lines of symmetry in Q13 are FOCUS dashed and the added segments ANSWER solid.
- **Colours**: the LP question text names "blue line", "red shape", "red outline", "yellow flower", "green looped design". The style tokens have no red, so the book's red `#C0392B` (and `#0B6B3A`, `#F2D43A` for the green knot and the yellow flower) are used only where the text names the colour; blue mirror lines use SET_A. Convention for all figures: given lines INK, lines of symmetry FOCUS dashed, everything else added by the solution ANSWER.
- **Panel letters**: rule says no figure letters in images, so the multi-panel figures (Q6, Q7, Q11, Q12, Q13, C2, Q1, Q2) have no panel letters; the panels follow the reading order of the LP question text. If the user wants small panel letters for the six-panel grid questions, that is a rule exception.
- **Grid figures**: lattice coordinates (x from the left border, y from the TOP border, y grows downward) are read from the page pictures with a pixel check; every mirror image and every completion is computed in code, and all completions agree with the printed answers (pp. 32 and 33).
- **Layout**: 16:9 cards for every figure; multi-panel cards use 3 x 2 or 2 x 4 layouts. The figure sizes were checked against the 1920 x 1080 canvas so nothing overlaps.

## 2. Problems in the LP

1. **Worked C10, wrong answer (needs the user's decision)**: the LP answer says "Figure 2 (the six-petal yellow flower): no line of symmetry (it only has rotational symmetry)". The page picture is mirror symmetric: a pixel comparison of the picture against its reflection in the six lines through the centre and the petals gives about 98.6 percent agreement, the same as for a 60 degree turn, and the book text says all three figures "also have multiple lines of symmetry". The correct answer is 6 lines (like the Koch figure, 6 lines, and the knot, 4 lines). Teaching image M1.S4.T4.C10.IMG1 repeats the error (labels "6 lines / 0 lines / 4 lines", description "twisted six-petal flower with none"). The diagram I specify shows only the given figures, so it is not affected.
2. **Rangoli (Q1)**: the LP/book answer says 4 lines. In the page picture the ornaments on the sides are a pair of teardrops with a line (top and bottom) and a single teardrop with two dashes (left and right), so the diagonals are not exact mirror lines. The spec draws identical ornaments on all four sides.
3. **LP book numbers**: T6 items are labelled "Figure it Out 9.1, Q1 to Q5" but are book Q6 to Q10; T9 items are labelled "Q1 to Q3" but are book Q11 to Q13 (the `ncert_refs` 9.1.FiO2.Q6 to Q13 are right).
4. **Duplicated question text**: many `question_tex` strings repeat the part list twice (for example C7, C17, C19, C21, C23, C25, C32, C34: "(a): ... (b): ..." then the same parts again in short form). Cosmetic, but the parts are listed twice to the learner.
5. **C15 q_figure** says the rectangle has a diagonal drawn dashed; the book picture has a dotted horizontal midline (see section 3).
6. **C37 answer text** says the completions are "closed shapes (four-sided or five-sided)"; the printed completions are a crossing quadrilateral (panel 1), a pentagon (2), a hexagon (3), a pentagon (4), a concave dart (5) and a pentagon (6). Not a conflict for the picture, only for the sentence.
7. **C35 answer text** describes (c) to (f) loosely ("cross-like stepped shape", "butterfly-like shape"); the diagram follows the printed pictures.
8. **Q1 question (C5)** refers to "the pictures at the start of the chapter" without giving them, so the question diagram is needed.
9. **C31 question** says "For the same square ABCD" but the LP has no earlier square figure in that concept; the corner positions are given in words, so the question needs no figure.
10. Base figure inventory corrections (marked `CORRECTED:` in the map): P05-shape-1 (Koch snowflake after 2 iterations, 48 sides, not "about 18 spikes in 3 groups of 6"), P05-shape-2 (petals are symmetric lenses with radial axes, not twisted), P05-shape-4 (horizontal midline, kept as the base noted).

## 3. Where the book is unclear or contradicts itself

- **P05-shape-4**: the text asks about the diagonal, the picture shows a horizontal dotted midline. No question diagram is made (optional); the optional figure would draw the diagonal.
- **Rangoli** (see above): printed picture versus the book's answer of 4 lines.
- **Kolam dots**: the book draws a dot on most but not all star tips; the spec puts a dot on every tip so the pattern is exactly symmetric.
- **Puzzle pieces (C2)**: the knob and socket positions are read from the picture and are approximate (fractions of a piece); the property that matters is that the left and right halves are not mirror images.
- **Q12(b)**: the notch coordinates (apex 2.3, ends 3.3 and 4.7) are not lattice points and are measured from the picture.
- **Q11(e)**: the question page draws the blue horizontal line over the full width, the printed answer from column line 1; the spec follows the question page.
- **Q13 grids**: the book's dot spacing is about 9 percent smaller vertically than horizontally; the spec uses equal spacing, the lattice coordinates are unchanged.
- **Photographs** (clouds, Taj Mahal, Gopuram) and the chapter-opening illustrations (butterfly, rangoli, pinwheel, flower) cannot be reproduced exactly; Q1 uses simplified flat redrawings.
- **Koch figure**: fitted to the page picture (about 2.5 percent radius error), not traced.
