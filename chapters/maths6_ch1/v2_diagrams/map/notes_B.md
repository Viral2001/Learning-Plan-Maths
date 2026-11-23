# Chunk B notes (Class 6 Ch 1, topics M2.S11.T11 to M3.S16.T16, units 19-37)

Result: 32 items, required 12 / optional 2 / none 18. Validator: errors 0 (2 warnings: C41 and C65 diagrams are not printed in the book, which is fine).
Required: C37, C39, C41, C45 (worked, IMG2), C48, C57, C59, C61, C63, C64 (question), C65, C68 (worked, IMG2).
Optional (not added): C40 question, C42 question.

## 1. Judgement calls

Odd numbers (units 19-22)
- C37 (solution of "Why does this happen forever?") is `required`: the reason is the book's 6 by 6 L-layer picture, and the LP step itself says "a picture of a square grid shows why". It is the same picture as C39 (identical spec, noted in render_note). If the user wants only one copy, make C37 `none` (TEXT_SUFFICIENT); nothing else depends on it.
- C39 required: the printed answer of the partition question is the picture (B2).
- C40 and C42 (questions that say "a similar picture"): `optional`, not added. The question itself gives no figure; the 6 by 6 picture is drawn in the previous solution (C39). Their text_alternative says what to write into the question text. Chose optional over none because "similar to what?" really needs the picture; chose optional over required because the book question gives no figure of its own and the lesson has just shown it.
- C41 required (10 by 10 L-layers, layers 1 to 19): the question asks the learner to draw this picture and the LP answer describes it; the book prints only the 6 by 6 one.
- C43 none (100 by 100 cannot be drawn; the question says "imagine ... or draw partially"). This differs from C41 on purpose (sibling rule): a 10 by 10 grid is drawable, a 100 by 100 one is not. Same reason for C50 (Figure it Out Q2, 100 + ... + 1).
- Layer sizes (1, 3, 5, ...) are written beside each row in ANSWER green on all three L pictures. The book's own picture prints no numbers; the sizes come from the book's line "1 + 3 + 5 + 7 + 9 + 11 = 36" and the LP steps. Drop them if the user wants the printed look.

Adding up and down (units 23-26)
- C44 none (plain sum, teaching image already there). C51, C52 none (plain arithmetic).
- C45 (worked example "diamond of dots") required: the LP text says "(A 6 by 6 grid of dots is shown.)" but no image exists, and the answer is a picture. A worked example has ONE diagram, so it shows the given 6 by 6 grid with the 11 diagonal groups 1, 2, ..., 6, ..., 2, 1 marked (the rows of the tilted grid the steps describe), not the bare grid. Concept already holds a 4 by 4 diamond (IMG1), this is a different picture (6 by 6, groups cut).
- C47 (Figure it Out Q1 question) none: the book prints the plain 6 by 6 grid above it, but that grid is the worked example's picture (C45) and the question names no figure.
- C48 required: printed answer picture SOL15-pattern-1. I redrew the book's four tilted lattices. The book leaves the 16-dot diamond without a label; I added "1+2+3+4+3+2+1 = 16" (the book's own page-7 pattern list has that line). The LP s_figure hint (one 4 by 4 grid) is thinner than the book; I followed the book.

Figure it Out 1.4 Q3 to Q9 (units 29-35)
- Questions C54, C56, C58, C60, C62 none: no figure is given; "explain with a picture" is the answer.
- C57, C59, C61, C63, C65 required. In the book these answers only say "refer Table 2 on page 4", "refer the picture on page 6", "refer picture in Q4 page 5". None of those pictures is a concept image of the LP, so the 'refer picture' exception does not apply and the solution draws the picture. The LP steps give the picture content:
  - C57: triangles of 1, 3, 6, 10 dots, newest row in green.
  - C59: 6-dot staircase triangle plus the turned-over 3-dot staircase triangle = 3 by 3 square. Staircase (right-angled) triangles are needed: apex-up triangles like Table 2's do not fit into a square. The book hint "Try it for isosceles right triangle also" points the same way.
  - C61 (the most uncertain): the book picture is the 1, 2, 4, 8, 16 doubling picture, including a 4D cube drawn in wireframe. I drew a simpler straight-row version of the same idea (rows of 1, 2, 4, 8, 16, 32 dots; after the first dot each new block is a copy of all dots before it, so coloured dots = 1, 3, 7, 15, 31 and +1 for the first dot). `needs_lp_text_sync: true`: LP step 4 ("each new shape is two copies of the one before, so one more than the total so far is the next power") should be reworded to match. If the user prefers the book's wireframe picture, or no picture, make C61 `optional`/`none`.
  - C63: the 19-dot cluster as a centre dot plus six triangles of 3 dots (checked: each triangle's dots are mutually adjacent, 6 x 3 + 1 = 19). Only the 19 cluster is drawn (the LP s_figure says 19), not 7 or 37.
- C64 (question) required: the book prints the cube and the hexagon of dots with this question, and "a picture of a cube" cannot be attempted without them; the LP text has neither. This is the one question side that differs from its siblings (Q4, Q5, Q7 are none) because only here does the book give the pictures. Colours: book yellow/red/blue became SET_B / FOCUS / SET_A (the style tokens have no yellow or red). The cube is drawn isometrically as 3 faces of 4 by 4 squares (I checked the page picture: 1 corner cube + 9 along the three edges + 27 = 37 visible cubes; 16 squares per face).
- C65 required, `derived_from` C64: top part identical to the question diagram, plus a green row of the four hexagonal clusters 1, 7, 19, 37 summing to 64 (layers of the cube). The question diagram keeps its lower third empty on purpose so the solution can add the row without moving anything.
- C66 (question) none, LATEX_TABLE: it refers to Table 1 (plain text table). Needs the table in the LP question text (text_alternative holds it). C67 none, OPEN_ENDED.

Shape sequences (units 36-37)
- C68 required (worked example, IMG2): the example says "Draw the next two", so the answer is a drawing (B2). One picture: triangle, square, pentagon (given, INK) and hexagon, heptagon (drawn, ANSWER green). It nearly repeats the concept's own teaching image (IMG1: five shapes with side counts); the v3 rule says a teaching image never stands in. Drop C68 to `none` if the duplicate is unwanted.
- C69 none: the stack size is given in words and the example asks for the next size and the count, no drawing.

Figure inventory choices
- Base ids claimed: P06-number_pattern-2 and P07-number_pattern-2 (none:LATEX_ARITHMETIC), P07-pattern-1 (item C39 solution), P08-pattern-1 (item C45), P09-solid-1 and P09-pattern-2 (item C64 question), SOL15-pattern-1 (item C48 solution). Chunk A (Example 1, section 1.4) may also claim the first three or four; I used the most standard code (LATEX_ARITHMETIC) so the merge should agree.
- Figures of sections 1.1-1.3 and Table 3 that my printed answers or examples only point at are claimed as NEW-<base id>-<item> (P03 Table 1 for C66; P04 triangular and squares rows for C57/C59; P05 hexagon clusters for C63; P06 doubling picture for C61; P10 regular polygons for C68), so they cannot clash with the other chunks' mapping of the base ids. The base ids P03-table-1, P04-*, P05-pattern-1, P06-pattern-1 should be claimed by chunk A; the Table 3 ids P10-* and P12-shape-1 by chunk C (Figure it Out 1.5 / 1.6). If a base id ends up unclaimed at merge, that is the cause.

## 2. Things in the LP that look wrong

- C36 (question "Why does this happen? Do you think it will happen forever?") does not contain the list of sums it points to. C38, C40, C42 also depend on earlier text ("a square grid", "a similar picture"). The question texts should carry the data (text_alternative fields say what).
- C45's question string is the whole book paragraph (pattern list + "Can you find a similar pictorial explanation? (A 6 by 6 grid of dots is shown.)") and it duplicates FiO Q1 (C47): the same question is asked twice, once as worked example C45 and once as C47, as in the book.
- C54 and C60 question texts end with stray scan fragments: "up) Add the All 1's sequence up up and down) ..." and "sums) 1, 1+2, ... add 1) Add 1 to each". They look like labels of a deleted picture; remove them.
- LP numbering in topic M2.S15.T15: "Figure it Out 1.4, Q1 ... Q7" are the book's Q3 ... Q9 (the ncert_refs say so); topic M2.S13.T13 uses Q1, Q2 correctly. Same book_number "Figure it Out 1.4, Q1/Q2" therefore appears in both topics.
- C55: LP says adding the All 1's sequence up and down gives 1, 3, 5, 7 (odd numbers). The book's printed answer (page 15) writes the sums in a different, muddled way ("1 + (1+1) + (1+1+1) ..." and the up-down form). Followed the LP, as the rules say.
- C61: step 4 is not a real reason (it restates the claim); see the C61 call above.
- C59 says "a triangle of 3 dots turned over"; this only gives a square for staircase triangles (see above).
- Video ids inside items (e.g. M2.S12.T12.C39.VID1 on the answer of unit 19) point to other concepts; ignored as instructed.

## 3. Where the book is unclear

- Table 2 (page 4) triangles are apex-up triangles; they do not fit into a square, yet the printed answer to Figure it Out Q5 sends the learner to Table 2 for the picture (the hint "isosceles right triangle" on page 15 resolves it).
- Q6's answer says "Refer the picture on page 6" (the doubling picture, which is the answer picture of 1.3 Q5), but that picture does not by itself show "one more than the sum is the next power"; the colouring (black original, blue copy) only suggests it.
- Q7's answer says "refer picture in Q.4 page 5" (the hexagonal clusters 1, 7, 19, 37); that picture does not show the six triangles. Q8's answer says "refer Table 2" (the coloured cubes row) although the question itself prints a cube and a hexagon.
- The fourth tilted diamond in the printed answer to Q1 has no label (see C48).
- The 4 by 4 by 4 size of the cube in Q8 is not printed; counted from the face grids (and 1 + 7 + 19 + 37 = 64 confirms it).
