# Chunk B notes (Class 8 Ch 9, topics M3.S6.T6, M3.S7.T7, M3.S8.T8; units 24 to 47)

Result: 27 items = worked_example 21 (required 9, optional 1, none 11), question 3 (none 3), solution 3 (required 3). Validator: errors 0, warnings 2 (see "Validator warnings").
Required media ids: C40.IMG3, C41.IMG1, C42.IMG1, C43.IMG2, C48.IMG1, C50.IMG1, C52.IMG1, C55.IMG1 to IMG5 (block 5 to 9).
Generator script (kept outside HERE): `/tmp/claude-1506/-root-maths-learning-plan/546c0a55-f920-40d7-a2bc-1439e8909fdd/scratchpad/gen_B.py`; every coordinate, area, angle and length in the specs is asserted in code.

## 1. Judgement calls

**Worked units carry one diagram.** All T6 and T8 units are `worked` (question + steps in one block), so each has at most one diagram, placed after the question text. For C40 to C43 that single picture is the figure the example needs (pieces, angles, or the cut and rearranged paper), not a question-state picture and a separate answer picture.

**Geometry of the dissection (C40, C41, C42, C43).** The book draws the joined squares with a about two thirds of b. I used a = 2, b = 3 for all four, so b - a = 1, the cut/foot point is (3, 0) and the figure points are: left (0,2), top (2,5), right (5,3), bottom (3,0). Pieces: T (0,2),(2,2),(2,5); U (2,5),(2,3),(5,3); V (0,2),(2,2),(2,3),(5,3),(3,0); W (0,2),(0,0),(3,0); X (3,0),(5,0),(5,3). I checked this against the page 44 picture (T, U, V, W, X positions, thin lines at x = 2 and x = 3) and against the angle figure: the four x arcs (33.69 degrees) and four 90 - x arcs (56.31 degrees) fall exactly where the book prints them. Areas: T, U, W, X = 3 each, V = 7, T + U + V = V + W + X = 13 = 4 + 9.

**C39 (areas 9 and 16): none.** Authored numeric example, no book figure, numbers are in the text, steps are arithmetic. The generic picture is the teaching image C39.IMG1. P09-shape-2 (the book's opening question picture with '?') is not what the LP asks (it uses the numbers 9 and 16).

**C40, C41, C42: required (FIG_REFERENCED).** The questions and steps speak of T, U, V, W, X and "this new 4-sided figure"; none of that exists without the figure. Drawn although concept images C40.IMG1 and C40.IMG2 show the same pieces (v3: teaching images are never linked, a lettered figure is drawn). C40 = pieces with labels a, b, b - a (book page 44 right panel); C41 = two panels T+U+V and W+V+X with an arrow (book page 45 top, no a/b labels there, none drawn); C42 = the angle figure with 8 arcs, 2 right-angle marks, edge labels, plus W and X letters (the LP solution names W and X; the book's angle figure has none, I added them in spots that touch nothing).

**C43 (paper): required (ANSWER_IS_FIGURE + ACTION_ON_FIGURE).** The activity ends in an arrangement of pieces. One picture, two panels: the joined squares with the two cuts of length c, an arrow, and the three pieces rearranged into the tilted square of side c. The pieces keep their colours of origin (small square MARK_FILL, large square SET_B). The rearranged regions are computed exactly (quarter turn anticlockwise of the left triangle about (0,2), clockwise of the right triangle about (5,3)); region areas add to 13, the small-square regions to 4 and the large-square regions to 9. This repeats what teaching image C43.IMG1 shows; kept as required because v3 says a teaching image is never linked and the answer is an arrangement. See Borderline.

**C45 (state the theorem): none.** A statement and a history; no figure given in the book for it; P14-construction-1/-2 are teaching figures leading to the theorem.

**T7 pairs.** All three questions: none (no figure given by the book, so no question diagram, as the rule says). All three solutions: required, drawn with `derived_from: null` because no question figure exists.
- C48 (same-size squares): square with its diagonal, shaded half (right triangle with both sides a), tilted square on the diagonal with its dashed centre lines (4 triangles against 2). Follows the LP `s_figure` hint and the book's page 8 figure. No area labels, no vertex letters (the LP solution has none).
- C50 (triple and five times): ONE picture with two panels (a pair gets one solution diagram). Left: given square with diagonal d, right triangle with legs a and d, square on the hypotenuse (3a squared). Right: right triangle with legs a and 2a, square on the hypotenuse (5a squared). a = 2: hypotenuse squares 12 and 20 (computed).
- C52 (difference of squares 5 and 7): right triangle with legs 5 and b = sqrt(24), hypotenuse 7, the compass arc (GUIDE), and the square on the third side labelled "24 square units" (the LP's own phrase, 3 words).

**T8 (missing sides).**
- C53 (3 cm, 4 cm): none (book text gives the data; its triangle only restates it). C54 blocks 0, 2, 3: none (arithmetic). C54 block 1 ("turned on its corner"): optional, not added; the picture that would help is a triangle with the right angle at the top, 7 and 24 at it, "?" on the bottom side.
- C55 blocks 0 to 4 (Q1 and Q4 (ii) to (v)): none (no book figure; a pair of numbers, or "draw it yourself").
- C55 blocks 5 to 9 = book Chapter Exercise Q2 (b) to (f): required. The book gives these only as six printed triangles ("the following right triangles"), the data is in the pictures. Each block gets its own triangle, drawn to true scale (the book is not to scale) in the book's orientation, the missing side marked "?" (allowed in a question figure; the book leaves it blank). Triangles: (b) legs 4 and 10; (c) legs 9 (missing) and 40, hypotenuse 41, right angle at the far left; (d) legs 10 and 10 (missing), hypotenuse sqrt(200) level at the bottom, right angle at the top; (e) legs 10 and sqrt(150), hypotenuse missing; (f) legs 27 and 36 (missing), hypotenuse 45. Perpendicularity and hypotenuse lengths asserted in code.

**Inventory choices.** P12-construction-1, P12-construction-2, P13-construction-1, P13-paper_cutout-2/-3/-4 and P21-shape-2 to -6 map to the items that draw them (even where a concept image also shows the figure). P10-construction-1 maps to concept image C39.IMG1. P09-shape-1, P09-shape-2, P10-construction-2, P11-construction-1/-2/-3, P14-construction-1/-2 and P15-shape-1 are `none:TEXT_SUFFICIENT` (teaching steps or figures restating text; no item needs them). `NEW-P08-construction-1-C48` is the second use of the page 8 picture (square, diagonal, square on the diagonal) by the C48 solution; its base entry belongs to chunk A's section 2.3. P21-shape-1 (triangle (a), 7 and 9) belongs to chunk C (unit 50) and is not claimed here; P21-grid-1 belongs to chunk D.

**Validator warnings (expected).** C50 and C52 solutions are required but no base figure maps to them: the book prints no picture for Figure it Out Q3 or Chapter Exercise Q7.

## 2. LP text issues

- **M3.S6.T6.C40, C41, C42**: the question and steps use T, U, V, W, X (and "the 4-sided figure T + U + V") without ever defining them; they exist only in the figure. Suggested sentence for the question or the first step: "Two squares of sides a and b are joined; T, U, W and X are four congruent right triangles with perpendicular sides a and b, and V is the five-sided middle piece."
- **M3.S6.T6.C42**: steps 2 and 3 name W and X but the book's angle figure has no piece letters. The diagram I specified shows W and X. If you prefer a text fix: "W is the lower-left triangle and X the lower-right triangle."
- **M3.S6.T6.C43**: step 5 says "turn each right triangle a quarter turn" without a direction. Suggested: "turn the left triangle a quarter turn anticlockwise about the top-left corner of the small square, and the right triangle a quarter turn clockwise about the top-right corner of the large square." The question also should say which square is larger: "(a < b)".
- **M3.S6.T6.C45**, step 5: "Baudhayana (c. 800 BCE)" is not in this chapter's text (page 15 gives only Pythagoras c. 500 BCE and "a couple hundred years" earlier). Not wrong, but a date from outside the book.
- **M3.S8.T8.C55 blocks 5 to 9**: the question text describes each printed triangle in words ("a thin tilted right triangle with sides 4 and 10 at the right angle"); once the diagram is placed after the question these phrases are redundant; keep or trim.
- **M3.S8.T8.C55 blocks 1 to 4 and 5 to 9 versus T9**: the same book question sets are split across topics: Q4 (i) is in T9 (C58/C59, whose `ncert_refs` list (i) to (v) but whose only item is (i)) while Q4 (ii) to (v) are practice blocks here; Q2 (a) is in T9 (C60/C61) while Q2 (b) to (f) are practice blocks here. The blocks also point at T9 videos (`M3.S9.T9.C59.VID1`, `M3.S9.T9.C61.VID1`). Not a diagram problem, but chunk C should give Q2 (a) the same decision as (b) to (f): question figure required.
- **M3.S7.T7.C47**: the question refers to "the earlier method" with no figure or link; fine as text.
- No other number, step or answer in the 27 items contradicts the book; I recomputed every sum, square and bounding interval of the T8 blocks (13, 12, 25, 10, 13, 81, 100, 250, 1296 and the decimal bounds) and all agree.

## 3. Borderline

- **M3.S7.T7.C48 solution (required).** The answer is a geometric argument rather than a literal drawing. The question says "Can you see why", the argument is about the diagonal and the square on it, and the LP carries an `s_figure` hint. I kept it required (SPATIAL_GEOMETRY, HIGHLIGHT_MEANING); the alternative is none.
- **M3.S6.T6.C43 (required).** The diagram repeats the teaching image C43.IMG1. Kept because the answer is an arrangement and v3 never links a teaching image. Alternative: optional or none.
- **M3.S6.T6.C41 (required).** Same pieces as concept image C40.IMG2; required because the steps cite the lettered pieces.
- **M3.S8.T8.C53 (none).** The book prints a 3 cm, 4 cm, "?" triangle next to the text, but the text already gives 3 cm and 4 cm and says "draw it"; text sufficient. Alternative: required (given picture).
- **M3.S8.T8.C55 blocks 5 to 9 (required).** The LP text carries the numbers, but the book gives them only in the pictures; kept required as decided (not flipped because the text carries the numbers).
- **M3.S8.T8.C55 block 0 (none)** (draw it yourself) and **blocks 1 to 4 (none)** (pairs of numbers). **M3.S8.T8.C54 block 1 (optional)**: the turned triangle is the one example of the four where a figure clearly helps; kept out of the plan as optional.
- **M3.S6.T6.C39 (none)**: a picture of squares 9, 16, 25 on the 3-4-5 triangle would be nice; teaching image C39.IMG1 shows the arrangement.
- **T7 questions (none)** although all three solutions are drawn: the book gives no figure with these questions, so no question figure is invented.

## 4. Where the book itself is unclear or differs from the base inventory

- **P12-construction-2 (page 44, angle figure):** the base description says the horizontal segment of length a is labelled "a"; the page picture shows no label there. I followed the picture and wrote "CORRECTED" in the inventory entry. All eight arcs, the two right-angle marks and the other labels match the description.
- The book draws the joined squares "not to scale" (a about two thirds of b); I fixed a = 2, b = 3 (stated in each spec) so every coordinate is exact.
- **P21 triangles (page 21):** the book is not to scale and leaves the missing side unlabelled; mine are to scale, the missing side carries "?". Triangle (d) is printed with a slightly tilted hypotenuse; drawn level (the right angle stays at the top).
- No printed digit, count or minus sign needed correcting (decision 1 did not apply to this chunk).
