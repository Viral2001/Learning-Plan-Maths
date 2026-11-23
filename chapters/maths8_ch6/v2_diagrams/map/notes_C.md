# Notes, chunk C (Class 8 Ch 6, cbse_eng_maths8_ch6_v32)

Units: M4.S19.T19 (6 pairs), M4.S21.T21 (5 pairs), M4.S22.T22 (4 pairs), M5.S23.T23 (1 worked example) = 31 items.
Result: required 16 (question 8, solution 7, worked example 1), optional 0, none 15. Validator: errors 0, 4 warnings
(C111 caption has 7 whitespace tokens but is one expression; C105, C111 and C117 solutions have no printed solution picture to map).
Figure inventory: 28 base figures claimed (19 to items, 2 to concept images, 7 none).

Item numbers below use the LP's concept ids. The book's question numbers differ from the LP's (see LP text issues).

## 1. Judgement calls

**Required question figures (8 + worked example)**
- C87 calendar: book says "as shown in the figure"; the 2 by 2 square 4, 5 / 11, 12 is outlined and the other squares come from that calendar. Drawn as `cell_grid` (the catalogue lists calendars). The book's "February" banner is a title and is not drawn.
- C102 circles, C104 tiles, C106 Tadang/Yusuf, C108 slanted region (Fig. 1), C110 dashed region, C116 park, C118 patterns: all are figure-based in the book (the data or the region exists only in the picture). Kept required even where the LP text carries expressions or counts (decision 4).
- C121 Coin Conjoin (worked example): the book figure is the 10-coin triangle and its upside-down copy; the worked step "keep the middle block still and move the three corner coins" is only readable on a picture. New id C121.IMG2 (IMG1 is the kept teaching image, never linked). The picture shows both triangles with the 3 moving corner coins marked in both; the rows of the second triangle are shifted down one row so the 7 coins that stay are in the same places in both pictures (checked in code).

**Required solution figures (7)**
- C88 calendar: the printed answer is two small pictures (3, 4 / 10, 11 and the lettered block); both drawn with their diagonals and the products. The question calendar is NOT repeated in the solution card, so `derived_from` (demanded by the validator) means: same cell style, same numbers cut from that calendar, not the same layout. Said in render_note.
- C103 circles: the LP solution reads Step k two ways (square of side k + 1 minus one circle; rectangle k by k + 2). The book prints these as Methods 1 and 4 (p.16, p.17). Drawn at Step 4: left a 5 by 5 square with the missing circle dashed, right six boxes of 4 circles. Methods 2 and 3 are not used by the LP solution.
- C105 tiles: the LP solution reads Step n as a square of side n + 2 with a hole of side n, and as four rows of n plus four corners. Drawn on Step 3 (n = 3, so n + 2 = 5 agrees with the drawing).
- C109 slanted region: three panels (Anusha, Vaishnavi, Aditya), the book's three method sketches p.18-19 redrawn on the question's I figure.
- C111 dashed region: two panels, method 1 (hatched rectangle marked s - r and p - r) and method 2 (whole rectangle, strips pr and sr, corner r squared outlined).
- C117 park: the LP solution adds w + g + 2w + g + w and w + g + w; the figure marks every segment and the two totals, which shows where the 2w comes from.
- C119 patterns: part (i) asks to draw the next figure and the printed answer is Step 4 of each pattern; the card repeats Steps 1 to 3 (question arrangement at a smaller scale) and adds Step 4 in ANSWER green with the totals 36 and 29.

**None (15)**
- T19 C85/86, C89/90, C91/92, C93/94, C95/96 and T22 C112/113, C114/115: plain algebra, selection from written lists, remainders; no figure in the book (`LATEX_ARITHMETIC` / `TEXT_SUFFICIENT`).
- C107 (Tadang solution): `SAME_AS_QUESTION_DIAGRAM`, see Borderline.

**Design choices not fixed by the book**
- Proportions are symbolic. Tadang: m : n = 1 : 3 (book draws m about n / 8, too thin for labels). Fig. 1: x : y = 6 : 1 (book about 5.6 : 1). Dashed region: s : p : r = 7.8 : 6.8 : 2 (book about 3.9 : 3.4 : 1). Park: w = 1.15, g = 3.0 drawing units (book g about 2.6 w); the gap between the plots is exactly 2w. All marked `to_scale: false`. The question numbers p = 6, r = 3.5, s = 9 and x = 8, y = 3 are NOT drawn.
- Colours use the style tokens, not the book's colours: tiles and strips MARK_FILL; hatched regions drawn as INK slanting lines on white (angles read from the book: Fig. 1 up to the right 30 degrees, dashed region steeply down to the right 60 degrees, Tadang 45 degrees down to the right); pattern (a) SET_B, pattern (b) SET_A; plots CELL_FILL.
- Park: the book's squared-paper grid behind the plan is texture, not tied to w or g, and is omitted.
- Letters (a) and (b) are drawn on the two Q11 pattern figures because the LP question and the LP answer refer to the patterns by letter (decision 3). Vertex letters (A to M, P to S) of the book's method sketches are NOT drawn: the LP solution never mentions them. The panel names Anusha, Vaishnavi, Aditya are drawn because the LP solution uses them.
- Pattern step labels are written "Step 1, Step 2, ..." (the book prints plain 1, 2, 3 above the circle and tile figures on p.15 and p.17, and "Step 1..." under the Q11 patterns).
- Coins are drawn as plain coins with an inner ring (the book has photographs of one-rupee coins).

## 2. Borderline (decision 4)

- C106 Tadang question `required`: the LP text is algebra only ("Show that ... are equal") and could be done without the figure, but the book question is "find the area of the shaded region in the figure" and the meaning of m, n and both expressions lives in the picture. Same reasoning for C108 (slanted region). If the team prefers text-only for these two, set both to none.
- C104 tiles question `required` although the LP text gives the counts 8, 12, 16 (the arithmetic pattern alone would give 4n + 4). The book question is figure-based and its point is the several methods of seeing the frame.
- C87 calendar question `required` although a calendar is a table of numbers: kept because the 2 by 2 outline carries meaning (HIGHLIGHT_MEANING) and calendars are listed under cell_grid in the catalogue.
- C107 Tadang solution `none` (SAME_AS_QUESTION_DIAGRAM) but C109 slanted solution `required`. Reason: the book prints no further picture for Tadang/Yusuf (one figure serves both methods), whereas for the slanted region it prints three extra sketches (printed answer is a picture, B2). The LP solution of C107 is pure algebra; a figure with m + n and n - m marked would be an optional enhancement (stated in `text_alternative`). The two items look alike in the LP text, so this is the call most worth confirming.
- C105 tiles solution and C103 circles solution `required` although the book prints no solution picture for tiles (a plain table P29-table-1, mapped `LATEX_TABLE`) and none at all in the answers section for circles: the LP solutions describe groupings of the figure that a student cannot see from the words alone.
- C117 park solution `required`: the 2w of the printed solution is the classic trap and the marks on the plan are the answer to "where does 2w come from".
- C119 solution repeats Steps 1 to 3 at a smaller scale next to the new Step 4 (so the card is `derived_from` the question figure). Showing only Step 4 would also satisfy the printed answer; chosen so the sequence is visible.

## 3. Book mistakes corrected in the specs (decision 1)

- Q11 pattern (a), Step 3 (question page p.21): the picture has 6 cells above the right column and 6 below the left column (27 cells in all, counted from the pixels of the page picture, as the base entry P21-pattern-1 recorded). The formula (y + 2)^2, the printed answer (2 + 3)^2 = 25 and the copy of the same figure on the answers page (p.34: 5 + 15 + 5 cells) all give 25. Drawn with 5 above and 5 below (25 cells); Steps 1 and 2 are as printed (9 and 16). Said in the item's render_note and in the inventory entry (CORRECTED).
- Printed answer of calendar Q4 writes the difference as (a + 7)(a + 1) - (a + 8): the factor a is missing before (a + 8). The LP and the maths give (a + 1)(a + 7) - a(a + 8) = 7. The figure tag shows a(a + 8).
- Base inventory P17-pattern-1 (Method 4): the description says the first k columns sit in one box; the page draws each row of k circles as its own box and the right column as one more box (k + 2 boxes of k circles = 4 x 6 at Step 4). Entry marked CORRECTED.

## 4. LP text issues (not edited; concept id, what is wrong or missing, suggested sentence)

- T19 C85-C96 and T22 C112-C119: `book_number` says "Figure it Out, Q1..Q6" (T19) and "Q1..Q4" (T22) but the book questions are Q2, Q4, Q5, Q6, Q7, Q9 (T19) and Q3, Q8, Q10, Q11 (T22) (the ncert_refs say so). Suggest using the book numbers or dropping the numbers.
- M4.S19.T19.C87: the question never shows the calendar. Suggested: "The figure shows the February calendar with the 2 by 2 square 4, 5 over 11, 12 outlined. Find the products of the numbers lying along each diagonal of a 2 by 2 square, for example 4 x 12 = 48 and 5 x 11 = 55. Do this for other 2 by 2 squares of the calendar."
- M4.S19.T19.C92: `answer_tex` has unbalanced math: `$2 ($or $5$ the other way round)`. Suggested: "difference: remainder $2$ (or $5$ the other way round)".
- M4.S21.T21.C102: the question does not mention the figure or its counts, and drops the book's "draw the next figure". Suggested: "The figure shows Steps 1, 2 and 3 of a pattern of black circles, with 3, 8 and 15 circles. Draw Step 4. Write the number of circles in Step k in two ways, show that they agree, and find the number in Steps 4, 10 and 15."
- M4.S21.T21.C104: the question gives only the counts. Suggested: "The figure shows square tiles forming a square frame round an empty square; Steps 1, 2 and 3 have 8, 12 and 16 tiles. Find the tiles in Step 4, Step 10 and Step n."
- M4.S21.T21.C105: the solution speaks of "a square of side n + 2 with a hole of side n" and "four rows of n plus four corners"; only understandable with the figure (now provided).
- M4.S21.T21.C106: m and n are not defined. Suggested: "In the figure, four equal rectangles m by n surround a shaded square. Tadang finds the area of the shaded square as (m + n)^2 - 4mn and Yusuf as (n - m)^2. Show that the two expressions are equal."
- M4.S21.T21.C108: x, y, the figure and the three names are missing. Suggested: "In Fig. 1 three equal rectangles x by y form a capital I; find the area of the region with the slanting lines. Anusha, Vaishnavi and Aditya get x^2 - xy, x(x + 2y) - 3xy and x(x - y). Verify that the three are equal and find the area for x = 8, y = 3."
- M4.S21.T21.C109: the solution never says where the three expressions come from. Suggested additions: "Anusha: the x by x region between the bars minus the middle bar xy. Vaishnavi: the whole rectangle x by (x + 2y) minus the three rectangles. Aditya: the two side regions are each x by (x - y)/2, so 2 x x(x - y)/2."
- M4.S21.T21.C111: `steps_tex[2]` has broken math: `$(p - r)(s - r) = ps - pr -$ rs $+ r^2$`. Suggested: "$(p - r)(s - r) = ps - pr - rs + r^2$, so both methods agree."
- M4.S22.T22.C116: `question_tex` has "$w ft$." (math mode swallows the space) and "$g^2\text{ sq. ft}$."; it also does not say that the path between the two plots is 2w wide while it is w wide at the outside, which the solution uses. Suggested: "...a walking path $w$ ft. wide round them (2$w$ ft. wide between the two plots, see the figure)...".
- M4.S22.T22.C117: `answer_tex` malformed: `$8w^2 + 8gw sq$. $ft$., that is $8w(w + g)$`. Suggested: "$8w^2 + 8gw$ sq. ft., that is $8w(w + g)$ sq. ft."
- M4.S22.T22.C113: the LP answer (ii) lists m^2 + (m - 1)^2 as well as m^2 + (m + 1)^2; the book prints only the second. The LP is right (m - 1 and m are consecutive); no change needed, noted only.

## 5. Places where the book itself is unclear

- Q10 park: the three horizontal arrows carry no label and the question says the path is w ft wide; only the printed answer (w + g + 2w + g + w) shows that the gap between the plots is 2w. Drawn as printed (two arrows labelled w ft., three unlabelled), the solution figure labels them w, 2w, w.
- Circles (Math Talk) and Tadang/Yusuf, slanted region: the answers section prints no answer; the LP answers follow the lesson text (Methods 1 to 4, Tadang and Yusuf, Anusha/Vaishnavi/Aditya).
- Fig. 1 (slanted region): the caption says "all three rectangles have the same dimensions" while the middle rectangle stands between the two bars (so its length is x and its width y); the picture is only consistent with that reading (figure x wide, x + 2y tall).
- Tadang figure, Fig. 1, dashed region, park: all drawn not to scale in the book; proportions in the specs are illustrative and said so in the specs.
- The calendar on the answers page (p.31) is the same February calendar without the red outline.
