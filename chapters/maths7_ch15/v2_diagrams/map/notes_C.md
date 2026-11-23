# Notes, chunk C (units 37-52: M2.S13.T13, M3.S14.T14, M3.S15.T15, M3.S16.T16)

Result: 30 items, required 6, optional 5, none 19. Validator: errors 0 (10 warnings, all "long visible_text" on equation strings that cannot be shortened).

Required: C76 + C77 (Q19 path puzzle, question + solution), C83 + C84 (Example 7 tiles, question + solution), C93 (Q8 window grill, question), C97 (Q12 two triangles, question).
Optional (NOT added): C79 (Example 8 worked), C81 (Example 12 worked), C86 (Example 9 solution), C94 (Q8 solution), C98 (Q12 solution).

## 1. Judgement calls

- **Q19 path puzzle (C76 / C77).**
  - Question `required`. A concept image of the same board exists (M2.S12.T12.C67.IMG1), but the 'refer picture' rule does not apply: the book question itself prints the board, and the LP text lists the 11 boxes but not one of the 22 arrow labels, so the puzzle cannot be attempted without the figure.
  - Solution `required` (answer = the coloured path, B2). It draws the whole board again, derived from the question figure, and adds the 10 coloured boxes, the 9 newly coloured arrows (the arrow 4 is already coloured in the book) and each box's solved value (all in ANSWER green, 3 words at most).
  - Aspect ratio 3:4 (the book prints the board portrait; in a 16:9 card the text would be tiny).
  - The START box and the arrow 4 are coloured in the question figure because the book prints them coloured.
  - Path checked equation by equation: x = 3, 21, 1, 2, 8, 13, m = -10, k = 4, x = 4, n = -13/25; each arrow label equals the answer of the box it leaves; the box -7 = 11 - 3x (x = 6) is the only box off the path.
  - Added an extra inventory entry `NEW-P26-path_puzzle-1-sol` for the second use of the board (solution item).
- **Example 7 tiles (C83 / C84).**
  - Question `required` although the LP text gives the counts 4, 7, 10, 13: the T shape (top row of 2n + 1 with a stem of n under the middle tile) is only in the picture, and the book says "as shown below". The figure is the book's own Steps 1-3 (plain outlines), so it does not show the Step 4 that the LP text mentions.
  - Solution `required`: the book's printed method for this example is a picture (Method 1 = three arms of n tiles and one centre tile) and the LP solution starts "three arms of k tiles and one centre tile".
  - Drawn: Steps 1-4 with arms shaded, centre tile outlined, counts and the sums 1+1+1+1 = 4 ... 4+4+4+1 = 13. The Step k column and Method 2 (P11-tile_pattern-3) are not drawn: the LP follows Method 1 only and 3k + 1 is already text.
  - The tile size must shrink (64 px to 48 px) so Step 4 fits; positions of Steps 1-3 keep order and shape only, not pixel positions (said in `render_note`). Step 4 is new, so it is in ANSWER green.
- **Example 8 (C79), Example 12 (C81), Example 9 solution (C86): all `optional`.**
  - Example 8 (Fatima's rough diagram: ovals "Snack cost" and "Delivery cost" pointing at 25 x [box] + 50) and Example 9 (two rows of ovals Jahnavi / Sunita meeting at "Equal") only label expressions that the LP steps already carry as LaTeX, which is the Step D example of an optional arrow picture. Same decision for both (sibling consistency).
  - Example 12's dot boxes (Suresh's box next to Ramesh's box plus a dashed 30) show "y + 30" as quantities; helpful, but the LP steps state it in words and an equation. If you want one worked-example picture in this chunk, this is the best candidate.
  - Example 9's question side is `none` (word problem, all numbers in the text).
- **Q8 window grill (C93 / C94).**
  - Question `required`: the book question hangs on the picture, and the LP text itself starts "The figure shows". It is a figure-based question with a numeric answer, so the solution is `optional` (Step E): the answer is 3 cm from 3 + 3 + 5 x 2 + 6g = 34, fully in the LP steps.
  - Drawn schematic, not to scale, gaps taller than rods as in the book, and the unknown gap shown as `?` (a gap drawn exactly 3 cm tall would leak the answer).
- **Q12 triangles (C97 / C98).**
  - Question `required` ("these triangles"; the angle letters live at the corners and the equal sides are shown by ticks); both triangles are in ONE figure (one question diagram per item). Solution `optional` for the same reason as Q8 (numeric answers fully in the LP steps).
  - The shapes are drawn with the real answer angles (50, 65, 65 and 60, 50, 70 degrees, checked from the vertex coordinates) so the picture never contradicts the solution, while the numbers themselves are not printed.
- **Sibling checks.** Q2 (a)-(g) and Q18 (a)-(h): plain equations, all `none`. FiO2, FiO6, FiO7, FiO9, FiO20: word problems with every number in the text, `none` (banknotes for FiO2 would be NOT_RENDERABLE anyway). Q8 and Q12 solutions are treated alike (both optional).
- **Teaching images are never linked.** Four of my figures also exist as teaching images (C67.IMG1 board, C78.IMG1 T-tiles Steps 1-4, C82.IMG1 grill, C82.IMG2 triangles); the items get their own diagrams.

## 2. Things in the LP that look off

- **C76 question text** lists the 11 boxes and says "follow the arrow that carries its answer" but gives no arrow label and no adjacency: the question is not solvable from the text; the figure is mandatory (hence `required`).
- **C83 question** gives counts for Steps 1 to 4, but the book picture shows only Steps 1-3 (plain, uncoloured).
- **C93 question text** says the borders are 3 cm "at the top and at the bottom" and that all five rods are 2 cm. The book picture labels only the top border (3 cm) and one inner rod (2 cm); the other measures are the LP author's reading (consistent: 3 + 3 + 10 + 18 = 34). The picture follows the LP text for the bottom border and keeps the book's single 2 cm mark.
- **C97 question text** says both base angles of the first triangle are y + 15. The book labels only the right base angle and shows equal sides by ticks (the student is meant to notice the equal base angles); the LP text gives that away. The figure labels both, following the LP text.
- I recomputed every LP solution of this chunk (Q2 a-g, Q18 a-h, Q19, Examples 7, 8, 9, 12, FiO2, 6, 7, 8, 9, 12, 20): no arithmetic or answer error found. The video id is shared by all blocks of a pair (fine).
- Plain-text `question` of the multi-part pairs joins several blocks of one card; the pair still gets at most one diagram per side (all none here).

## 3. Places where the book is unclear

- **Q19 board (p.26):** the arrowheads are partly hidden by notches in the cream boxes and read as double-headed; the label (not the head) says which box an arrow leaves. The arrow between 2x + 5 = 3(x - 1) and 30 = 4 - 50n (column 3, rows 3-4) has no number. The label "+ 4" between -4 = 16 - 5k and 2x - 9 = 3 - x is printed with a plus sign. Which two boxes each diagonal joins was read from position (corner box to the centre-column box of the next row); the LP solution agrees with that reading for every arrow used.
- **Q8 grill (p.24):** not to scale; the small bracket arrow heads at the right are tiny; the unlabelled bracket sits on the 5th of the 6 gaps; the bottom border and the other rods carry no label.
- **Q12 (p.24):** the left base angle of the first triangle is unlabelled in the book; the figure is not to scale (the book's first triangle is much narrower than the 50-65-65 answer).
- **This pdf has no printed-solutions section**, so the LP solution text is the only answer followed; no printed-answer picture exists for this chunk (the Example 7 "Method" pictures are the nearest thing).
- Decoration left out of the inventory: the photograph of two boys playing marbles (Example 12 page) and the flower box, shutters and bricks of the grill picture.
