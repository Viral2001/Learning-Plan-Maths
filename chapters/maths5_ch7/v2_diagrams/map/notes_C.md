# Chunk C notes (Class 5 Ch 7 "Shapes and Patterns", topics T14 to T20)

Result: 30 items = question 12 required / 0 optional / 1 none; solution 11 required / 1 optional / 1 none; worked example 3 required / 0 optional / 1 none
(required 26, optional 1, none 3). Validator `--chunk C`: errors 0, 3 warnings (C74 and C76 solutions and the C96 worked example have no printed
figure in the book to map; fine).

All geometry in `out_C.json` was computed in code and asserted (areas, side lengths, angles, that the pieces of every shape tile its outline exactly,
that the 17 chords of C96 are distinct and the walk returns to 1).

## Borderline

1. **C65, C73, C75 questions are `required` (rhombus with its 4 pieces).** The book prints no figure with Activities 4, 7 and 8 themselves, but
   the whole activity set works on the cut-out rhombus of p.96 ("Cut out the triangular pieces for the following activities", p.97), and without
   the pieces the question cannot be attempted (tie-breaker). The three questions get the same picture (identical spec, "same as C65.IMG1"). The
   solutions C66, C74, C76 name this diagram in `derived_from` but re-arrange the same pieces (same size) instead of repeating the rhombus layout.
   If the literal rule "no printed figure = no question diagram" is preferred, flip the three questions to `none` (TEXT_SUFFICIENT) and set
   `derived_from` of C66, C74, C76 to null; nothing else changes.
2. **C79 worked example (tangram pieces) is `required`.** The text names and counts the pieces, but "what is special about the angles" can only be
   seen on the pieces. The picture shows the finished sorting (5 triangles under "3 sides", square and parallelogram under "4 sides") with
   right-angle marks and equal-angle arcs. It overlaps in content with the concept image of the same concept; per the 23 Nov decision it is drawn
   anyway and the concept image is not linked. Alternative: `optional`.
3. **C84 solution is `none` (SAME_AS_QUESTION_DIAGRAM) although C82, C86, C88 are required.** (b) angles and (c) sides add marks (right angles and
   equal angles, ticks) that carry the meaning; (a) "same or different" adds no mark, all of it can be read from the question picture. If a picture is
   wanted: the five triangles in a row from small to large plus the square and parallelogram (earlier author's hint); that would not keep the
   question layout.
4. **C83, C85, C87 questions each get a full tangram picture** (identical to C81). The book prints one tangram picture beside Q1 and its parts
   (a), (b), (c); the LP split them into 4 questions, so each part gets its own diagram (prompt section 2). The base inventory marks the picture a
   "teaching figure"; it is treated as the figure the question gives because "Name them" and "same or different" cannot be answered without it.
5. **C94 solution is `optional`, C93 question `none`, C91 worked example `none`.** C93: the 7 statements and the 4 names are in the LP text, the
   book's outlines add nothing. C94: matching answer is a complete list in the text; the arrows of a matching table follow the
   NUMBER_LIST_IN_BOXES rule (optional when the text already gives the answer). A picture (4 shapes with the statement numbers under them) is
   described in the reason. C91: the properties are given in words and a picture of X, Y, Z, W would show their names (the answer).
6. **C95 and C96 worked examples are `required`; their pictures show the finished figure** (rectangle/square in two circles; the full 17-line
   design), because question, steps and answer sit in one block and the steps refer to the drawing. C95 could be argued `none` (a student can draw
   it on paper); C96 could be argued text-only (the walk is arithmetic). I kept both because the drawing is the answer (B2) and the positions of the
   points are only clear in a picture.
7. **C71 question (empty 43 by 12 grid) is `required`** (ACTION_ON_FIGURE: draw on the printed grid). The picture is trivial but it is the figure
   the book gives, and the solution (C72) derives from it.
8. **C77 question is `required`** (corners A and B and the crease exist only in the picture). C78 shows the clean finished kite (book picture has
   hands; not renderable). Colours SET_B (flaps) and SET_A (uncovered triangles) follow the earlier author's hint; the word "flap" is the only text.
9. **Hexagon in C76 (e):** a convex hexagon made of 2 kites joined along their sides of length 1.7321 was chosen (a concave hexagon is also
   possible). Pentagon (d): kite on top of a rectangle (convex).
10. **Tangram tick marks (C88)** sit inside the piece they belong to (short stroke from the midpoint of the side into the piece), because most
    sides are shared with a neighbour piece and a tick across the edge would be ambiguous. Counts compare sides only inside one piece (stated in
    the spec).

## Book mistakes corrected / book unclear (decision 1)

- **Rhombus proportions.** The book's rhombus has its long diagonal about 1.6 times the short one (measured). The diagram uses 1.7321 (pieces with
  legs 1 and 1.7321 and hypotenuse 2, i.e. 30-60-90 triangles) because the LP solutions need it: two pieces make an equilateral triangle, a kite, a
  rectangle and two different parallelograms, and the book's A and B (p.98) have exactly these sides. Recorded in the render_note of C65.
- **Trapezium of C89 (book p.99, last outline).** The printed outline is a hand sketch: top : bottom about 2 : 5, base angles about 50 degrees. The LP
  fills it with the parallelogram and the medium triangle, which makes a trapezium with top : bottom = 1 : 3 and 45 degree base angles (area 4). The
  diagram uses that exact outline so that the pieces fill it. The other three outlines match the book (width : height = 2 : 1). Recorded as
  "CORRECTED" in the render_note of C89 and in the inventory entry P08-shape-6.
- **Kite fold (p.100).** The second book picture (hands holding the half-folded paper) cannot be read as geometry. The solution diagram folds both
  corners from the top-left end of the crease; the book's tip is at the lower right (a mirror/rotation of the same kite).
- **Grid (p.99).** 43 by 12 squares comes from the base inventory (counted by pixel analysis); my own check of the line spacing (18 px over the
  790 px wide frame, 12 rows of 18 px) agrees.
- **Which Shape Am I?** The book has no printed answer; the LP matching was checked by hand and is correct (Square 5, 6, 7; Rectangle 1, 6, 7;
  Rhombus 2, 3, 4, 6; Parallelogram 3, 4, 6).

## LP text issues

(No LP text was changed; decisions were not changed because of them.)

- **M3.S14.T14.C65 (question), also C73 and C75:** the question does not say which pieces to use. Suggested: "Using 2 of the 4 triangular pieces of
  the rhombus, how many different 4-sided shapes (quadrilaterals) can you make?" (C73 already says "3 triangles from the rhombus"; C75 should say
  "all 4 triangular pieces of the rhombus").
- **M3.S14.T14.C67 and C69 (question):** "these two quadrilaterals A and B" is not tied to the picture. Suggested: add "(the two shapes in the picture)"
  after "A and B".
- **M3.S14.T14.C71 (question):** the grid is not described. Suggested: "In the grid of 43 by 12 squares given below, ...". **C72 (solution):** the
  corner numbers count from the bottom left of each drawing but the text does not say where each shape sits on the grid; the figure puts the shapes
  side by side with origins (3,2), (12,2), (23,2), (34,2). Suggested sentence: "Draw each shape on its own part of the grid; Kite 1 starts at (3, 2), Kite 2 at
  (12, 2), Parallelogram 1 at (23, 2) and Parallelogram 2 at (34, 2), and the corners above are counted from these points."
- **M3.S14.T14.C74 (solution, step 5):** "In all, 3 pieces make 13 different shapes: 2 with 3 sides, 5 with 4 sides and 6 with 5 sides" could not be
  reproduced. Joining 3 pieces side to side along whole equal sides (turning and flipping allowed) I count 9 different shapes: 1 with 3 sides,
  3 with 4 sides and 5 with 5 sides. The number depends on what counts as "different" and on whether sliding is allowed. Suggest removing the count
  or re-checking it. (The three shapes drawn in the diagram are verified.)
- **M3.S15.T15.C77 (question):** "corner A" and "corner B" are defined only by the picture. Suggested: "(A is the bottom-left corner and B the top-right
  corner of the square)".
- **M3.S15.T15.C78 (steps 5 and answer):** "the paper under them shows 2 more triangles" - in the folded kite the 2 other triangles are the uncovered
  parts next to the flaps, not under them. Suggested: "the paper that is not covered shows 2 more triangles". Step 3 says "from the same end of the
  crease" but not which end; the figure uses the end that is the kite's pointed tip.
- **M3.S17.T17.C89 (question):** the four outlines are not named. Suggested: "make a slanted parallelogram, a rectangle, a triangle and a four-sided shape
  with a short top and a long bottom".
- **M3.S17.T17.C90 (steps 5):** "put the parallelogram on the left and the medium triangle on the right" does not say how to turn the parallelogram.
  Suggested: "turn the parallelogram so that its short sides are the top and the bottom".
- **M4.S20.T20.C95 (worked example):** the angle between the two diameters of the first drawing is not given; the figure uses 60 degrees (any angle other
  than 90 degrees gives the same rectangle result).
- **M4.S20.T20.C96 (worked example):** the position of point 1 and the direction of numbering are not stated; the figure puts point 1 at the top and
  numbers clockwise (like the book's circle designs).
- No other LP text problems found in chunk C: C66, C68, C70, C72, C76, C86, C88 steps agree with the geometry (all side lengths, angles and joins were
  recomputed).

## Figure inventory notes

- 34 entries: 33 mapped to items, 1 `none:TEXT_SUFFICIENT` (P09-table-1). Each further use of a book picture is a `NEW-<base id>-<suffix>` entry
  (rhombus 3 uses, A and B 4 uses each, grid 2, tangram square 8, the four target outlines 2 uses each).
- Base figures that are claimed here although their section belongs to another chunk: **P05-shape-3** (rhombus; chunk B's section, used by C65, C73,
  C75), **P07-shape-1** (kite, mapped to the kite of the C66 solution; chunk B may map it to its own worked example) and **P10-circle-1** (mapped to
  C95; chunk D's questions may use it too). The merge keeps the first claim and turns the others into NEW- entries.
- P09-procedure-3 (hands illustration) is mapped to the C78 solution: the clean kite diagram replaces it.
