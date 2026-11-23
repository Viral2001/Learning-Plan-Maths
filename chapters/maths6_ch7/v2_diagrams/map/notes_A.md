# Chunk A notes (Class 6 Ch 7 Fractions, topics M1.S2.T2 to M1.S8.T8)

Result: 24 items = required 8 (question 3, solution 3, worked 2), optional 1, none 15. Validator: errors 0, warnings 3 (the three
required solutions C20, C22, C28 have no printed answer picture to claim; the printed answers of 7.1, 7.2 are text only, and the
7.3 "Do it once more" boxes have no printed answer).
Inventory: 20 base figures claimed (13 to items, 6 to concept images, 1 none). All base descriptions were checked against the page
pictures (pages 1, 4, 5, 6, 7): no correction was needed.

## 1. Judgement calls

| Item | Choice | Why |
|---|---|---|
| T2 C2 (roti, 2 and 4 children) | none, TEXT_SUFFICIENT + DECORATIVE_ONLY | all numbers are in the question; the book picture only illustrates the sharing and is the teaching image C2.IMG1 |
| T2 C3 (1/5 or 1/9) | none | the book prints no picture |
| T2 C4 (words for fractions) | none, OPEN_ENDED | discussion activity |
| T3 FiO 7.1 Q1 to Q5, questions and solutions | all none | the book prints no figure for any of them; printed answers are numbers or a list of fractions. Q3 (3 glasses among 4) and Q4 (two fish) would be nice with a picture, but the tie-breaker says text is enough. Q5's answer is an ordered list, kept as LaTeX |
| T4 C16 (chikki broken into 2 pieces) | worked example, required, id C16.IMG2 | the book says "A picture of the chikki broken into 2 pieces is shown below"; the learner counts squares of the L-piece and the 3 x 2 rectangle on the 24-square grid. Shown without the dashed halving guides, the arrow and the 1/4 box (they give the answer), because a worked-example diagram sits after the question and a question figure shows only what is given. A worked example has only this one diagram, so the "halve it both ways" idea stays in the steps and in the teaching image C16.IMG1 |
| T4 C17 (fractional unit of one strip) | worked example, required, id C17.IMG2 | the book asks "of chikki shown below"; whole chikki with its two cut lines next to the one strip. No 1/3 box |
| T5 Math Talk (six equal pieces) | pair: question required, solution required | the two ways of cutting (six 2 x 2 rectangles, six slanted triangles) exist only in the picture; the answer "same size" is visual. Both cuttings are ONE diagram (a pair gets one question diagram), laid out like book p.4 with the separate piece and a plain 1/6 label beside each. The solution shades one piece of each cutting (the top-left 2 x 2 block, and the triangle (0,0),(0,4),(2,4) of the first strip, the same shape as the separate piece) and tags both "4 squares", the words of the LP solution |
| T6 FiO 7.2 Q1 (pieces a to h) | pair: question required, solution required | the eight shapes on small squares are the data; act-on-figure (fill each box). Solution fills the boxes with the fractions, tags each piece with its square count (LP steps 2) and draws the rectangle that each triangle is half of as a dashed GUIDE outline (LP step 2 "a triangle is half of its rectangle") |
| T6 letters | the figure carries "(a)" to "(h)" | the LP question and answer name the pieces (a) to (h); without letters the answers cannot be matched. This goes against the prompt's "no figure letters like a. / b." line, which is meant for figure captions. DECISION FOR THE USER: keep, or drop the letters (then the answers must be matched by position: row 1 a to d, row 2 e to h) |
| T7 C23 (fold a strip in two) | none, TEXT_SUFFICIENT | answer is one line; book strip pictures are teaching figures covered by C23.IMG1 |
| T7 C24 (fold again, four parts) | optional (not added) | the strip with braces 1/4, 2/4, 3/4, 4/4 (book p.6) would help, but the question gives no figure and the steps give each length in words. There is no concept image for it. Kept `optional`, not `none`, because it is the one figure of chunk A that clearly helps without being asked for. Not made `required` because the book question gives no figure and does not say "shown below" |
| T7 C25 (halves as additions) | none, LATEX_ARITHMETIC | the answer is five addition statements (LaTeX); the half-roti table is the teaching figure C25.IMG1 |
| T8 Q1 (fold into eighths, fill the boxes) | pair: question required, solution required | the book figure (8-part strip, eight nested braces, blank boxes) is what "fill in the blank boxes" is done on (ACTION_ON_FIGURE); the solution is the same figure with every box filled. The LP text alone would also work ("k x 1/8 = ___"), so this is the closest call of the chunk: if the user wants fewer figures, T8 is the first to turn into `optional`. Difference from C24 (optional): C24 is a teaching illustration with nothing to act on, T8 is an activity figure with boxes. Diagram type `other` (nothing in the catalogue fits a strip with nested braces) |

Other calls:
- P04-shape-1 (the plain whole chikki) is mapped to concept image M1.S4.T4.C16.IMG1 (a whole 6 x 4 chikki is the base of that image); it is a teaching figure and no item needs it separately.
- P06-strip-1 and -2 are mapped to concept image M1.S7.T7.C23.IMG1; P06-strip-3 (four parts) has no concept image and is `none:TEXT_SUFFICIENT` because C24 is optional.
- The pie-chart art at the top of page 1 (chapter-opening decoration) was not inventoried (decoration).
- Chikki pieces are drawn flat with CELL_FILL and GUIDE small-square lines (no peanut texture, per the flat-2D rule); the shaded pieces of the solutions use MARK_FILL; cut lines are dashed INK.
- The solution figures are `derived_from` their question figure with the same coordinates; additions are described by position so that the renderer can reuse the question scene.
- Units: each spec states its own coordinate system (origin top-left, x right, y down, 1 unit = one small square; for the strip figure 1 unit = a third of one eighth part). The renderer scales one factor to fit the 16:9 card.

## 2. Things in the LP that look wrong or thin

- T5 C19 question: "slanted cuts into 6 pieces including triangles". In the book the second cutting gives six right triangles (each 2 x 4 strip is cut along its diagonal), so every piece is a triangle. Not wrong, but "including" suggests a mix; the figure follows the book.
- T8 C27 question: the LP says "Fold the strip once more so it has 8 equal parts" and lists a blank for every row, including "2 x 1/8 = ___". The book prints no box after "2 times 1/8", and leaves the LEFT boxes of rows 3, 5 and 7 blank too ("fill in the blank boxes" includes writing "3 times 1/8"). The LP answer keeps that pattern for odd rows only ("3 x 1/8 = 3/8", "5 x 1/8 = 5/8", "7 x 1/8 = 7/8", the even rows just "2/8", "4/8", "6/8"). The figure follows the LP question text (labels given in every row, one blank value box per row); if the LP is later synced to the book, rows 3, 5, 7 would show a blank label box. The question text also lacks the book's own instruction "Do it once more!".
- T2 C4 `concept_name` is "Fractional units: more sharers, smaller share", the name of C3, though C4 is the "words for fractions in your language" activity; the unit's `ncert_refs` for C4 and C24 are empty while their items carry 7.1.q1 and 7.3.ex2. T7 C23 and C24 share the concept name "Folding a strip into halves, quarters and eighths". Cosmetic.
- T6 C22 step 3 lists five divisions (12, 4, 8, 6, 24) for eight pieces; correct, since pieces with equal counts repeat. The printed answer (book p.38) agrees with the LP: 1/12, 1/4, 1/8, 1/6, 1/8, 1/6, 1/24, 1/24.
- T3 C14/C15 (Q5) and the "Find out and discuss" activity: in the book the activity sits between Q4 and Q5; the LP puts it before Q1 as a worked block (C4). Only an ordering note; no effect on the diagrams.

## 3. Places where the book itself is unclear

- Book p.7: "2 times 1/8" has no "=" box, rows 3, 5 and 7 have a blank label box, rows 4 and 6 have a boxed label, row 1 has a single box with no label. Resolved as in section 2.
- Book p.4: the cut lines of the two six-piece cuttings are dashed or dotted lines running past the chikki. They are drawn here only slightly past it (0.4 unit). The slanted cuts were read from the page picture: from the top at column boundary 0, 2, 4 to the bottom at 2, 4, 6 (confirmed in the zoomed picture, together with the vertical dotted cuts at 2 and 4).
- Book p.5 FiO: the pieces are printed at slightly different heights and some start higher than the letter (f). The figure puts all pieces on one baseline, centred in their column; the shapes and sizes are exactly the book's (b, c, f, h are right or isosceles triangles with the stated legs and the right angle at the bottom-left; e is an L with its extra square on the upper right).
- The book answer boxes of 7.2 (empty squares) become empty rectangles 1.6 x 1.0 so that "1/12" or "1/24" fits when the solution fills them.
