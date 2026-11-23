# Notes for chunk C (Class 6 Ch 6, topics M2.S18.T18, M2.S19.T19, M2.S21.T21, M3.S22.T22, M3.S23.T23)

Result: 22 units, 37 items: required 18 (8 question, 9 solution, 1 worked example), optional 5 (all solution side, not added), none 14. Validator: errors 0, 3 warnings (the three required items whose figure is not printed in the book: C82, C108 block 3, C113).

## 1. Judgement calls

Combined pictures (forced by "one question diagram and one solution diagram per pair")
- C89/C90 (five figures on the grid): ONE picture with all five outlines on the book's shared 24 by 21 grid. The figures carry NO letters (prompt section 4 forbids figure letters). The LP text calls them "first ... fifth", which matches reading order (top row left to right: 3 figures, bottom row left to right: 2 figures). If the team prefers letters a to e in the picture, the LP text should be switched to "figure a ... e" and the spec changed.
- C106/C107 (area mazes b, c, d): ONE picture with three drawings left to right (second, third, fourth maze), no letters. Each keeps the book's printed numbers and the shaded unknown. Splitting the card into three concepts would give three cleaner pictures; not done here (the brief says one diagram per pair).

Question diagrams that differ on purpose from the book picture
- C87 (grid ABCD): the book also prints F, the grid line EF and green/orange shading of AFED and BFEC. The LP solution introduces F and EF as its own first step ("Drop a line from E straight down to F"), so F, EF and the shading are in the SOLUTION diagram only. The question diagram keeps the grid, A B C D E, blue triangle BAD (SET_A) and red triangle ABE (FOCUS). If you want the book picture exactly, move F/EF/shading into the question diagram.
- C93 (new square): the book's dashed arrow (new square pointing at the corner cell that gives "stays 24") is left out; the LP question does not say "as shown" and the arrow would give away one of the three answers. The loose square is kept, outside the grid. The grid is cropped to 9 by 8 cells.
- Colours that are named in the text map to the nearest token: blue = SET_A, yellow = SET_B (it is amber), red = FOCUS (it is pink). Rooms/shapes have no fills except where the book colours something that the text names or marks an unknown (MARK_FILL).
- C98/C100 plans: only the printed labels are drawn, blanks as underscores; Utility and Entrance labels of Sharan's plan are written horizontally (the book rotates them).

Solution side
- C82 (rectangles of area 24): REQUIRED, ANSWER_IS_FIGURE (the task is "make as many rectangles as you can", the answer is the set of rectangles). Only the area-24 set is drawn (four rectangles, perimeters 50, 28, 22, 20, greatest and least marked). The area-32 set (E1) and the general prediction (E2) stay as text, since a pair gets one solution diagram.
- C84 (diagonal cut): OPTIONAL, not added. The text (6 x 4 = 24, 24 / 2 = 12) is complete and the teaching image C78.IMG1 already shows the idea. The question has no figure in the book, so no question diagram.
- C86 (blue rectangle / yellow triangle): REQUIRED. The solution argues from the picture; the figure adds two dashed 4 by 3 rectangles around the halves of the yellow triangle, right-angle marks and a half mark in each of the four triangles.
- C88 (grid): REQUIRED, because the solution adds point F, the line EF and the areas 6 and 4 that do not exist in the question figure (prompt Step E would call this "optional if the solution splits the shape"; I chose required because the new point makes the LP steps unfollowable without it). The three totals sit in a small key to the right so they do not collide with the grid.
- C90 (five figures): REQUIRED. The dividing lines and the five areas are the answer (the book prints only the numbers).
- C92 (nine unit squares): REQUIRED: the printed answer to "make a figure with a perimeter of 18" is a picture (SOL26-shape-1). The diagram draws the LP's three arrangements (3 by 3 = 12, row of 9 = 20, row of 7 with 2 on its left end = 18) from the LP's own s_figure. The 18-unit figure is NOT the printed picture (that one has rows 2, 4, 3); both are valid, LP wins. The book's second teaching figure P17-shape-2 (C shape, perimeter 20) is not drawn: no question or answer of the chunk shows it; I mapped it to none:TEXT_SUFFICIENT because it is not a plan concept image and no other chunk has a topic on page 17.
- C94 (square attached): REQUIRED, ANSWER_IS_FIGURE + ACTION_ON_FIGURE: three new squares (flat side 26, corner touching 2 sides 24, slot touching 3 sides 22) with the perimeter written in each. The loose square of the question diagram is not repeated. Checked by code: base figure perimeter 24; new squares give 26, 24, 22 and do not touch each other.
- C99/C101 (houses): REQUIRED, the answer is the completed plan. The solution diagram also gets the missing outer dimension (35 ft / 25 ft) and the total 1,050 sq ft because the card's second item asks for the whole area.
- C103 (compare houses) OPTIONAL: two outlines 35 x 30 and 42 x 25 on one scale would help, but 1050 against 1050 and 130 against 134 are complete in text.
- C105, C107 (area mazes) OPTIONAL: the printed answers are numbers; a maze with the derived sides filled in would help but only restates the question figure with values. Same decision for all four mazes (sibling consistency), question side required.
- C113 (shapes A and B) REQUIRED: "draw two such shapes" has a drawn answer; the LP's pair (A = 18 x 1, B = 5 x 4) is drawn to scale with area and perimeter tags. Question side none (no given figure).
- C115 (folded square) OPTIONAL: a square cut into two 10 x 5 rectangles with the new edges marked would help; the numeric example in text is complete.
- C111 (lawn): none, pure arithmetic. C110 question none: the book prints no figure.

Worked examples in M3.S22.T22.C108
- block 3 (book Q7, rectangle 12 x 8 with a half-area rectangle inside): REQUIRED, add_new_image: the example is a drawing task whose answer is the pair of rectangles; the book only says "draw the rectangles accordingly". The picture shows the finished drawing (outer 12 x 8, inner 8 x 6 from the LP step), so the token after the question text shows the answer before the steps: that is how the worked-example slot works in v3, but say so if the team does not want the answer visible there.
- block 4 (book Q6, border on your own page): none, OPEN_ENDED. The answer depends on the child's page ("never quote one perimeter"); no fixed figure. This is the only "draw" item left without a picture; the reason is that no size is fixed.
- blocks 0, 1, 2 (book Q1, Q2, Q3): none, arithmetic, no printed figure. C79 block 0 (conclusion sentence) and C109 (summary): none, text.

Inventory accounting
- P13-pattern-1/2 (circles in the rectangle, concept image M2.S15.T15.C71.IMG1) are claimed by chunk B (units p13.circle, p13.why_squares), not here. SOL24-shape-1 (Deep Dive) belongs to chunk A.
- Where a solution diagram redraws a book picture I added a `NEW-<base id>-sol` entry (11 entries) so the figure count per use is honest.

## 2. Things in the LP that look wrong or thin

- C114 question text (M3.S23.T23.C114) lacks the four statements a to d of the book; the answer ("the perimeters added are 1 1/2 times the square's") makes no sense to a learner who has never seen the options. The LP text needs the four statements (text sync, not an image matter).
- C99 vs the printed solution: the LP gives the hall as an L shape of 265 sq ft (20 x 12 = 240 plus a 5 x 5 strip under the toilet = 25); the printed solution says 240. The book's own plan does draw the L shape and 225 + 50 + 180 + 180 + 45 + 265 + 60 + 45 = 1050 = 35 x 30 confirms the LP. LP wins; drawn as L shape with 265.
- The unit ncert_refs are loose: C110's unit lists p21.q4 and p21.q7, C112's lists p21.q5 and p21.q6, but the cards hold q4 and q5 only; q7 and q6 are worked blocks of C108 (their video ids point to T23 videos C111 and C113). Harmless, but the numbering is confusing: LP "Pulling It Together Q1, Q2, Q3" are book Q4, Q5, Q8; book Q1, Q2, Q3, Q7, Q6 are worked blocks.
- C83 hint q_figure ("a rectangle with one diagonal") describes a figure the book does not print; the book question has no figure.
- C85/C86: the plan's own teaching note (C78) records a doubt that the book's answer list says "triangle = half of the rectangle". Measured on the printed picture the yellow triangle has the same height and twice the width of the blue rectangle, so the areas are equal; the LP solution (same area) and my diagrams follow the figure.
- The book's text extraction of page 18 puts "(15 ft x __ ft)" under Hall; in the picture it belongs to the Small Bedroom (Hall has only "Area = __").
- C98 solution step 6: the sentence "gap of 5 ft by 5 ft under the toilet also belongs to the hall" is right, but the diagram label for that part is just "5 × 5".

## 3. Where the book itself is unclear

- p13 "Let's Explore" (rectangles of area 24): no figure is printed and the printed solutions (pdf p.26) give no answer at all under "Let's Explore! Page No. 141". The LP answer (four rectangles, 50/28/22/20; 66/36/24 for 32) is the LP's own and checks out.
- p14 blue rectangle and yellow triangle: no numbers. Sizes are measured from the picture (rectangle about 4:3, triangle base about twice the width, equal height).
- p16 figures a to e: no lengths printed; corners read from the page picture on the 24 x 21 grid and checked: shoelace areas 24, 30, 48, 16, 12 match the printed answers and the LP pieces add to them.
- p17 tricky grid: the arrow tip lies between cells; read as pointing at the cell right of the vertical bar's neighbour in the horizontal bar (the corner cell). The loose square is drawn slightly off the grid in the book.
- p18/p19 plans: only "30 ft" (Charan) and "42 ft" (Sharan) are printed; every other length is measured from the picture (about 17.6 px and 16.55 px per ft) and agrees exactly with the LP's derived sizes (checked: the rooms tile the plot with no gap or overlap, 1050 sq ft each).
- p20 maze c: the printed 6 cm arrow is visibly shorter than 6/15 of the 15 cm arrow, so the book picture is not to scale. The diagram uses the sizes the printed numbers imply (widths 4, 7, 12; heights 4, 6, 5; total 15).
- Printed solutions: Q6 of "Pulling It Together" (the border) has no printed answer (pdf p.29 goes from Q5 to Q7).
