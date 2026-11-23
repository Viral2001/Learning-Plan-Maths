# Class 8 Ch 1 A Square and A Cube - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths8_ch1` v45 (taken from staging). Result: new V2 version v46 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (81 items from 46 units)
{"worked_example": {"none": 10, "required": 1}, "question": {"none": 33, "required": 2}, "solution": {"none": 30, "required": 2, "optional": 3}}

Optional, NOT added: [('C65', 'solution'), ('C81', 'solution'), ('C93', 'solution')]

needs_lp_text_sync: []

## The 5 diagrams
| id | side | type |
|---|---|---|
| M2.S10.T10.C41.IMG1 | question | dot_array |
| M2.S10.T10.C42.IMG1 | solution | dot_array |
| M2.S15.T15.C64.IMG1 | question | tiling |
| M3.S21.T21.C95.IMG1 | solution | number_pattern |
| M4.S25.T25.C113.IMG2 | worked example | cell_row |

### Chunk A notes (from the decision agent)
# Notes, chunk A (Class 8 Ch 1 "A Square and A Cube", plan cbse_eng_maths8_ch1_v45)

Result: 31 items (18 units: 5 worked examples, 13 question/answer pairs). Required 2, optional 0, none 29. Validator: errors 0 (7 warnings, all "long visible_text" for the dot-square captions such as '6 + 10 = 16 = 4²', which are the book's own captions).

The only required diagrams are the triangular-number question and its solution:
- `M2.S10.T10.C41` question, `M2.S10.T10.C41.IMG1`: the book figure on chapter p.7 (three dot squares 2x2, 3x3, 4x4 cut into 1+3, 3+6, 6+10 by a staircase, captions, then the EMPTY fourth square and EMPTY caption box).
- `M2.S10.T10.C42` solution, `M2.S10.T10.C42.IMG1` (derived_from C41.IMG1): same row, fourth square filled with 5x5 = 25 dots cut into 10 + 15, caption '10 + 15 = 25 = 5²' in ANSWER green.

Everything else is text/LaTeX: factor lists, arithmetic, number chains, a plain fill-in table, typeset equations, multiple-choice questions.

Note: the brief says this pdf has no printed-solutions section. It does: pdf pages 19 to 22 print the answers. For chunk A every printed answer is a number, a list or typeset equations (checked on pages 19 to 21); none is a picture. The LP solution text still wins where used.

## 1. Judgement calls

- C41/C42 required. The LP question text is numeric ("Add the next pair of consecutive triangular numbers after 6 and 10 ..."), but the book question is "Can you see any relation between triangular numbers and square numbers? Extend the pattern shown and draw the next term." The pattern exists only as the picture, and the book's answer is a drawing. I followed the book (FIG_REFERENCED, ACTION_ON_FIGURE, DATA_IN_FIGURE on the question; ANSWER_IS_FIGURE on the solution; the LP's own `q_figure` / `s_figure` hints agree that a figure was meant). The question figure keeps the fourth slot empty, exactly as printed, so it does not leak the answer. The row of single triangles 1, 3, 6, 10, 15 on the same page is a separate teaching figure and is not drawn here.
- Solution figure content: the book prints no answer for this question, so slot 4 is the pattern continued (the staircase rule of slots 1 to 3) and agrees with the LP solution (10 + 15 = 25 = 5²). The 10-dot group is the upper-right triangle and the 15-dot group the lower-left, as in slots 1 to 3.
- Inventory entry `NEW-P07-dot_pattern-3-sol` is the second use of the p.7 figure (the completed slot 4); it is not printed in the book, I added it so the required solution has an inventory figure.
- The captions are drawn as in the book (plain text under slots 1 to 3, the empty rectangle under slot 4 at caption level). The spec gives layout in dot-pitch units and says "scale to 92% of the card width"; with the 16:9 card the figure is wide and short, so there is empty space above and below.
- Concept-image mappings are accounting only and some are approximate: P06-dot_pattern-1 (visual proof panels) and P05-dot_pattern-3 both map to C25.IMG1; P07-dot_pattern-2 (triangles 1, 3, 6, 10, 15) maps to C37.IMG1 (the closest, a 5x5 square cut into 15 and 10); P02 boxes map to C2.IMG1 and C3.IMG1. Nothing is linked to any teaching image.
- P04-table-1 (squares of the first 30 numbers) and P07-table-1 (ten blocks of 100) are "given in question" but are plain fill-in tables, mapped `none:LATEX_TABLE`. No LP item in chunk A uses P04-table-1 as a figure; the LP question C39 does not ask for the ten-block table.
- Sibling consistency: the four Figure it Out items (Q2 = C23/C24, Q3 = C31/C32, Q7 = C43/C44, Q8 = C33/C34) are all none/none; all "last digit" and "zeros" questions (C17 to C24) are none/none.

## 2. Borderline

Apply the v3 rules as written; these are the calls where a reviewer might want the other answer:
- `M2.S10.T10.C41` / `C42`: required although the LP text carries all the numbers (see above).
- `M1.S3.T3.C8` / `C9` (which lockers stay open): none. The printed answer is the list 1, 4, 9, ..., 100; the 10x10 locker grid (C4.IMG1) is a teaching image and would only make the list nicer.
- `M1.S3.T3.C6` / `C7` (factors of 36): none. The book prints no answer picture; the pairs are LaTeX equations.
- `M2.S6.T6.C25` worked (sum of the first 8 odd numbers): none. An 8x8 dot square built from L shapes would help but the rule n² = sum is stated in the text and the 6x6 teaching image C25.IMG1 exists. Could be `optional` if the reviewer wants the figure.
- `M2.S6.T6.C26` worked (subtract odd numbers from 38): none. The book prints it as a chain of subtractions on a cream band; number chains are LaTeX.
- `M2.S8.T8.C33` / `C34` (pattern, Figure it Out Q8): none. The book's pattern and its printed answer are typeset equations with bold underline on the three filled numbers (21, 90, 91), not a drawn picture.
- `M2.S10.T10.C39` (blocks of 100): none. The book's ten-block table is a plain fill-in table.
- `M2.S9.T9.C35` worked (numbers between 25 and 36): none. The number line is a teaching image (C35.IMG1).
- `M2.S4.T4.C12` worked (areas for sides 6, 3/5, 2.5): none; three squarings.
- `M1.S2.T2.C2` worked (locker 12): none.

## 3. LP text issues

Not edited and no decision changed because of them (user decision 2).
- `M2.S7.T7.C31` (question) and its echo in `C32`: option (v) reads "15625 + 512" but the book prints "15625 + 51²" (superscript 2; pdf p.10 and p.20). Suggested: "(v): $15625 + 51^2$". The separators are also uneven: "(ii): $15625 + 26^2$ (iii): ..." has no semicolon before (iii). The LP answer (iv) 15625 + 251 is right.
- `M2.S10.T10.C41` (question): it never mentions the dot pictures, although the book question and the required diagram do. Suggested: "Look at the pictures: $1 + 3 = 4 = 2^2$, $3 + 6 = 9 = 3^2$ and $6 + 10 = 16 = 4^2$. Draw the next term: add the next pair of consecutive triangular numbers after $6$ and $10$ and check that the sum is a square." Its `q_figure` hint is also wrong: it says the picture shows triangles of 1, 3, 6 and 10 dots with the sums beside them; the question picture is the three dot SQUARES each cut into two triangles.
- `M2.S10.T10.C42` (solution): the steps never refer to the picture. Suggested first step (after the figure): "The $5 \times 5$ square of dots splits into a triangle of $10$ dots and a triangle of $15$ dots."
- `M2.S10.T10.C39` (question): the LP asks only for the squares between 101 and 200 and the largest square below 1000. The book asks to enter the number of squares in each of ten blocks of 100 (1-100 ... 901-1000) first. If full coverage of the book question is wanted, add: "Complete the table of the number of squares in each block of $100$, from $1$-$100$ to $901$-$1000$." (a LaTeX table).
- `M2.S5.T5.C24` (answer): `answer_tex` is "(ii): $108^2$ and (iii) $292^2$" (a colon after (ii) only). Suggested: "(ii) $108^2$ and (iii) $292^2$". The question text of C23 also has "(i): ... (iv): ..." with colons; harmless.
- `M2.S8.T8.C33` / `C34`: `book_number` is "Figure it Out, Q1" but the book's number is Figure it Out Q8 (ncert_ref `FiO1.q8`). The other Figure it Out items of this chunk are labelled "Square Numbers, Q2/Q3/Q7", so the same exercise carries two label styles; only the ids matter for the build.
- Mathematical checks (all hold): C2 12 has 6 factors; C7 36 has 9 factors; C12 (3/5)² = 9/25, 2.5² = 6.25; C18 31² = 961, 39² = 1521; C20 34² = 1156; C22 3000² = 9000000 (6 zeros); C24 and the book agree on 108², 292²; C25 1+3+...+15 = 64; C26 chain ends 2 - 13 = -11; C30 71 and 1296; C32 251 and 15876; C34 16+25+400 = 441 = 21² and 81+100+8100 = 8281 = 91²; C40 121, 144, 169, 196 and 31² = 961 < 1000 < 32² = 1024; C44 2 x 16 = 32, 2 x 99 = 198. No LP solution contradicts the book's printed answer.

## 4. Where the book is unclear

- Chapter p.7: the fourth slot of the triangular-number figure is an empty square (about the size of a 5x5 array at the same dot pitch) with an empty rectangle for the equation; the book prints no label or answer for it. The 5x5, 10 + 15 = 25 = 5² reading follows the pattern and the LP solution.
- Chapter p.4: column 3 of the table of squares has 8 empty cells (23² to 30²) with no printed labels; irrelevant to the decisions (LaTeX table, no LP item).
- P03-grid-2 (chapter p.3): no caption; checked on the page picture, it is a 5 x 5 grid of unit squares (6 + 6 lines), presumably the 5 x 5 = 25 square of the table.
- No print slips found in the book pictures or printed answers used by chunk A, so no "corrected value" is used in any spec.

### Chunk B notes (from the decision agent)
# Chunk B notes (Class 8 Ch 1, units 19 to 35)

Result: 30 items = required 1 / optional 2 / none 27 (question: 1 / 0 / 12, solution: 0 / 2 / 11, worked example: 0 / 0 / 4). Validator: errors 0, warnings 0.
The only required diagram is the Figure it Out Q9 tile picture, question side of `M2.S15.T15.C64` (media id `M2.S15.T15.C64.IMG1`, type `tiling`, 16:9).
Reason: the book prints a figure for no other question of this chunk; every other item is words, arithmetic or a plain list, so LaTeX and text carry it.

## Borderline

1. `M2.S15.T15.C64` question (FiO1 Q9, tile picture): `required`. The LP text states "9 rows of 9 tiles ... 5 by 5 tiny squares", so a text-only student could count 81 x 25, but the book question is "How many tiny squares are there in the following picture?", so the picture is the thing counted. Kept `required` under user decision 4.
2. `M2.S15.T15.C65` solution: `optional` (not added). The answer is a number. A figure repeating the tile picture with the 9 by 9 tiles and one 5 by 5 tile marked would be the Step D "row totals beside a grid" case. It would not repeat the question figure exactly, so I did not use `SAME_AS_QUESTION_DIAGRAM` alone (both codes are given).
3. `M3.S19.T19.C80` question (cubes of edge 2, 3, 4): `none`. The book draws a 2 x 2 x 2 cube beside its own version of the question (`P11-solid-4`, listed as "given in question" in the base), but the LP question gives only the three edges in words and the tie-breaker answer is yes (a careful student solves it from the text). A question picture of three cubes cut into unit cubes would also nearly hand over the counts.
4. `M3.S19.T19.C81` solution: `optional` (not added). Three cubes of edge 2, 3 and 4 in layers of 4, 9 and 16 unit cubes would be the natural picture and the book draws the edge 3 and edge 4 cubes, but the steps already state the layers and the answers are numbers. If the user wants it, a `solid_3d` spec is easy (oblique drawing, three separated layers, counts 4, 9, 16 only in the solution colours). The edge 3 and edge 4 cubes are teaching images C79.IMG1 and C76.IMG1, which are never linked.
5. Square-root answers that "pin down" a root with a number line in the teaching image (`M2.S16.T16.C66` worked, `M2.S17.T17.C71`, `C73`): `none`. The book prints no figure for them and the steps are inequalities and products; the number lines exist as teaching images C66.IMG1, C67.IMG1 and C68.IMG1. Decided for sibling consistency with the rest of T11 to T17.
6. Prime-factor solutions (`C57`, `C59`, `C61`, `C63`): all `none` (`LATEX_ARITHMETIC`). The grouping brackets (2 x 3 x 3) x (2 x 3 x 3) are written in the steps and the book prints them as text. Same decision on all four, as the prime-factor pairs are siblings.
7. `M2.S11.T11.C45` worked example (square of area 64): `none`. No picture in the book; the square of side 8 is teaching image C45.IMG1.
8. `M2.S11.T11.C47` worked example (81 down to 0): `none`. The book's yellow band (`P08-number_chain-1`) is nine plain subtractions, no arrows or highlights, so `LATEX_ARITHMETIC`.

## Choices in the Q9 spec

- Panel colour: the printed panel is dark green, which the style tokens do not have. The spec uses `MARK_FILL` for the panel, white tiles and `INK` lattice lines so each of the 25 cells in a tile can be counted.
- The figure is nearly square (about 597 x 595 px in the book); it is centred in the 16:9 card (panel 8.32 x 8.32 units on a 16 x 9 canvas), as the pipeline draws 16:9 cards.
- Layout recomputed: tile (row r, column c) is a diamond when r + c is even. Odd rows start with a diamond: 5 x 5 = 25 diamonds in rows 1, 3, 5, 7, 9 and 4 x 4 = 16 in rows 2, 4, 6, 8, so 41 diamonds and 40 upright tiles, 81 tiles. 81 x 25 = 2025 = 3^4 x 5^2 = 45^2. The total is not written on the figure.
- Geometry recomputed: pitch 0.88, diamond side 0.62 (half-diagonal 0.4384 < 0.44), upright side 0.66; the panel's inner margin of 0.2 units keeps the edge diamonds off the panel edge; the last tile centre is at x = 11.52 and y = 0.98.

## Book mistakes (user decision 1)

- Tile picture (FiO1 Q9, pdf p.11): what the book page prints. The diamonds show a full 5 x 5 lattice (I counted 5 cells from the left corner to the top corner). The upright tiles show only 2 x 2, 2 x 3 or 3 x 3 cells with unequal widths, with lines at about 20, 40 and 80 percent of the side. Those positions belong to a 5 x 5 lattice (lines at 20, 40, 60, 80 percent), so the page raster has dropped the thin lines (an aliasing loss in the PDF image, not a print design). The base inventory counted 1241 white cells and says it is unconfirmed. The spec draws every tile as 5 x 5 because the LP question and solution state it (2025 = 45^2, the theme of the chapter) and the diamonds show it. The base inventory entry keeps what the page prints, with a description starting "CORRECTED:". Checked by zooming the page image at 10 times.
- No other print slip found in the pages used by this chunk.

## LP text issues

No LP text was changed. All sums in the LP solutions were recomputed and hold (21^2 = 441 to 24^2 = 576, 324 = 2 x 2 x 3^4 = 18^2, 156 = 2 x 2 x 3 x 13, 1156 = 34^2, 2800 = 2^4 x 5^2 x 7, 180 and 900 for 4, 9, 10, 9408 = 2^6 x 3 x 7^2 and 28224 = 168^2, 2025 = 45^2, 44^2 = 1936 and 45^2 = 2025, 225 and 256 with gaps 6 and 25, 121 and 144, 2025 and 2116, 1024 and 1089, 8, 27, 64, 125 to 729, 99^3 = 970299). Cosmetic and labelling issues only:

| Concept id | What is wrong | Suggested sentence |
|---|---|---|
| `M2.S15.T15.C62`, `C63` | `book_number` says "Figure it Out, Q1" but this is NCERT Figure it Out (1.1) Q6 (9408). Other items in the same plan use the true number ("Square Numbers, Q4", "Q5", "Q1"). | "Figure it Out, Q6" (or "Square Numbers, Q6") |
| `M2.S15.T15.C64`, `C65` | `book_number` says "Figure it Out, Q2" but this is NCERT Q9 (tile picture). | "Figure it Out, Q9" (or "Square Numbers, Q9") |
| `M3.S19.T19.C81` | `answer_tex` is `$8$, $27$ and $64\text{ unit}$ cubes`: the word "unit" is inside the math part and "cubes" outside. | `$8$, $27$ and $64$ unit cubes` |
| `M3.S19.T19.C80` | `question_tex` has `$4\text{ units}$`: the unit is inside the math part. | "cubes of edge $2$, $3$ and $4$ units" |
| `M2.S17.T17.C74`, `C75` | Stray colons after the part labels: "(i): $2032$; (ii): ..." and the answer "(i): $2032$, (ii): $2048$ and (iii) $1027$" (the third label has no colon). | "(i) $2032$ (ii) $2048$ (iii) $1027$ (iv) $1089$" and "(i) $2032$, (ii) $2048$ and (iii) $1027$ are not perfect squares; $1089 = 33^2$" |
| `M3.S19.T19.C84`, `C85` | Same stray colons: "(i): The cube ...", and "(i): False: ..." with a double colon in every step. | "(i) False: odd x odd x odd is odd, for example $3^3 = 27$." |
| `M2.S11.T11.C45` (worked example) | Text says "the square roots of 64 are 8 and -8" and uses sqrt as the positive root in the last line; fine mathematically. It follows the book's p.8 sentence "Thus sqrt(64) = +-8" even though the same page then says "we shall only consider the positive square root" and the Summary prints sqrt(9) = 3. Not a LP mistake. Listed so the content team knows the book itself is inconsistent here. | no change needed |

Nothing is missing from a question that only a figure carries: the LP text of `M2.S15.T15.C64` states all the data of the tile picture (9 rows of 9, 5 by 5 per tile), so the picture is a repeat of data for counting, not a source of hidden numbers.

## Where the book itself is unclear

- FiO1 Q9 picture, see "Book mistakes". The book prints no answer to Q9: the "Ans." pages (pdf p.19 to 22) cover Q1 to Q8 of the first Figure it Out and then go to the cubes, so 2025 cannot be cross-checked with the book.
- The brief says this pdf has no printed-solutions section; in fact pdf pages 19 to 22 hold NCERT "Ans." lines (checked: answers to FiO1 Q1 to Q8, FiO2 Q1 to Q5 are short numerical answers with no pictures except P21-pattern-1, which belongs to chunk A). They match the LP answers of this chunk: Q4 21 m, Q5 900, Q6 "3; 168", Q1 (i)(ii)(iii), FiO2 Q3 five times False.
- The book says "Aribam says 250 ... is approximately 16. We also know it is less than 16" (p.10); the LP says "closer to 16", which agrees.

## Base-inventory accounting for this chunk (7 figures)

| fig_id | mapped_to | why |
|---|---|---|
| P08-number_chain-1 | none:LATEX_ARITHMETIC | nine plain subtractions, no marks |
| P11-tile_pattern-2 | item:M2.S15.T15.C64 (question) | the only required diagram |
| P11-solid-3 | none:TEXT_SUFFICIENT | one unit cube, illustrates the word "cube" |
| P11-solid-4 | none:TEXT_SUFFICIENT | 2 x 2 x 2 cube beside the book's version of the question; LP question gives the edges in words |
| P12-solid-1 | concept_image:M3.S18.T18.C79.IMG1 | edge 3 cube in layers (teaching) |
| P12-solid-2 | concept_image:M3.S18.T18.C76.IMG1 | edge 4 cube in 4 layers of 16 (teaching) |
| P12-table-3 | none:LATEX_TABLE | plain table of 1^3 to 20^3, row colours are decoration |

If another chunk also claims one of these base figures, the same meaning applies. Base figures of other sections (pages 2 to 7, 11 Q8, 14, 15, 18, 21) were left to the other chunks.

### Chunk C notes (from the decision agent)
# Chunk C notes (Class 8 Ch 1, plan cbse_eng_maths8_ch1_v45)

Units 36 to 46 (topics M3.S21.T21, M3.S23.T23, M3.S24.T24, M4.S25.T25): 9 question/answer pairs and 2 worked examples = 20 items.
Result: required 2, optional 1, none 17. Validator: errors 0, warnings 0.

| Item | Decision | Media id |
|---|---|---|
| M3.S21.T21.C95 (solution, difference tower of the cubes) | required | M3.S21.T21.C95.IMG1 |
| M4.S25.T25.C113 (worked example, finished row of square pairs) | required | M4.S25.T25.C113.IMG2 (IMG1 is the kept teaching image) |
| M3.S21.T21.C93 (solution, 91 to 109) | optional (not added) | none |
| all other 17 items | none | none |

## Figure accounting (7 base figures claimed)

- P14-number_pattern-1 (the six pattern lines + the 91..109 sum): none:LATEX_ARITHMETIC. Plain typeset equations, no colour or boxes.
- P15-table-1 (prime factorisation table, number and its cube): none:LATEX_TABLE. Teaching table, used by no item.
- P15-number_pattern-2 (difference tower of the squares): none:TEXT_SUFFICIENT. Teaching figure used by no item; the cubes version is concept image C88.IMG1.
- P15-number_pattern-3 (row of cubes with arrows, levels blank): mapped to item C95 (solution). The row and arrows become the top of the complete tower.
- P18-pattern-1 (3 6 10 15 1 and its four sums): concept_image:M4.S25.T25.C113.IMG1.
- P18-box_row-1 (17 empty boxes): mapped to the worked example in C113.
- P18-box_circle-1 (ring of boxes): none:OPEN_ENDED. Open challenge, not an LP item.
- Not claimed on purpose: P21-pattern-1 (printed answer of Figure it Out Q8 of section 1.1) belongs to the unit of FiO1 Q8 (chunk A, unit 14); P11/P12 figures belong to chunk B.
- Page pictures checked: p13 (only equations and a Ramanujan-Hardy cartoon), p14, p15, p16 (text only), p17, p18, p21, p22. Not inventoried, on purpose (photographs/cartoons, Step 0 skips them): the cartoon on p13, the Babylonian clay-tablet photo on p15, the children and owl on p18.
- The base descriptions I checked were right. I counted the pink ring by pixel analysis: 28 boxes (32 pink components, four are watermark-split fragments of boxes already counted); the yellow row has 17.

## 1. Judgement calls

1. **C94/C95 successive differences of the cubes.** The book prints a figure with the question (the row 1 8 27 64 125 216 with a curved arrow between neighbours, levels blank). The LP question already names the six cubes, so the figure carries nothing the student needs to attempt it: question none (TEXT_SUFFICIENT). The solution is the filled difference tower (the book's own structure, drawn for squares on the same page); the position of each difference between its two parents and the equal row at level 3 are the finding, so it is required (B2: answer is an arrangement). It stands alone (derived_from null) because the question has no diagram. Colours: cubes INK, computed differences ANSWER, arrows GUIDE, dashed FOCUS box round the three 6s (the LP says the differences are constant, 6, at level 3). Row labels 'Cubes', 'Level 1', 'Level 2', 'Level 3' are category labels (the LP steps use 'Level 1:' etc.). No '...' after 216 because the LP stops at 216.
2. **M4.S25.T25.C113 worked example (square pairs).** The book gives a row of 17 empty boxes; the example's answer is that row filled. I drew the finished row (16, 9, 7, 2, 14, 11, 5, 4, 12, 13, 3, 6, 10, 15, 1, 8, 17) with the 16 neighbour sums under it in ANSWER green (the LP step 3 lists exactly these sums). Cells 1 and 17 (16 and 17) have a FOCUS outline because LP step 1 says they go at the two ends. Empty boxes alone would be a blank figure (companion note: worse than none). The token follows the v3 worked-example rule (question_tex, after_question_text), so the learner sees the end state before the steps.
3. **C93 solution (91 to 109): optional, not added.** A picture of the ten odd numbers with the five outside pairs each marked 200 would help the check step. The four LP steps carry every number, so nothing is added.
4. **Cube-root and Figure it Out items (C101 to C110).** Sibling consistency: all are prime-factor lines or number guesses, so all stay text. The grouping pictures for 3375, 729 and 1323 exist as concept images (C98, C99, C100) and are never linked.
5. **C112 worked example (varga, ghana, mula).** Words only; the three words are concept image C112.IMG1. No diagram.
6. **Unit 36 (4104).** Arithmetic only, no figure. No diagram on either side.
7. **Note on the brief:** it says the pdf has no printed-solutions section, but pages 19 to 22 hold printed answers (all text in my chunk). They agree with the LP: Q1 30 and 22, Q2 7, Q4 11/17/23/32, Q5 (i), cube roots 4/8/9, 91..109 sum 10^3 = 1000.

## 2. LP text issues

- **M3.S21.T21.C92 (question 91 to 109).** The question says 'using the cube pattern' but does not print the pattern. A learner who skipped the teaching page cannot use it. Suggested sentence to add after the question: "Recall the pattern: $1 = 1^3$, $3 + 5 = 2^3$, $7 + 9 + 11 = 3^3$, $13 + 15 + 17 + 19 = 4^3$, $21 + 23 + 25 + 27 + 29 = 5^3$, $31 + 33 + 35 + 37 + 39 + 41 = 6^3$."
- **M3.S21.T21.C90 (4104).** The book's Try This asks for 4104 and 13832; the LP covers only 4104. Suggested extra question or sentence: "Show that $13832 = 2^3 + 24^3 = 18^3 + 20^3$" (2^3 + 24^3 = 8 + 13824 = 13832; 18^3 + 20^3 = 5832 + 8000 = 13832).
- **M4.S25.T25.C113 (worked example).** Step 2 starts "Start 16, 9, 7, ..." but the list is the whole row of 17 numbers, not a start. Suggested: "One arrangement is 16, 9, 7, 2, 14, 11, 5, 4, 12, 13, 3, 6, 10, 15, 1, 8, 17 (its reverse also works)." The book's other questions on the page (more than one way, why not; the 1 to 32 circle) are not in the LP.
- **Book numbering in the LP.** C107 and C109 are labelled 'Figure it Out, Q1' and 'Q2' but are the book's Figure it Out Q2 and Q4 (ncert_refs FiO2.q2 and FiO2.q4); C96 'Cubic Numbers, Q5' and C105 'Cubic Numbers, Q1' use the book's own numbers. The book's Q3 (true or false) is in another chunk.
- **Concept image C113.IMG1** (accounting only) shows 3, 6, 10, 15 with 9, 16, 25; the book's example is 3, 6, 10, 15, 1 with 9, 16, 25, 16. Not an LP text issue, but the teaching image is one number and one sum short.

## 3. Borderline

- C95 solution **required** (filled difference tower) while the question is **none**. A reviewer may prefer the question to be required as well (book figure to be completed: ACTION_ON_FIGURE). I kept it none because the figure repeats the numbers already in the question text.
- C113 worked example **required**. The answer is a list of 17 numbers that the LP already writes out; I applied B2 (answer is an arrangement / filled figure) as written and did not flip it to none.
- C93 solution **optional** rather than none (the pairing check would benefit from a picture but is complete in text).
- P14-number_pattern-1 is **none** (LATEX_ARITHMETIC): a typeset pattern, no colour or boxes.

## 4. Book unclear or wrong

- **Square Pairs circle (p.18):** the text asks for the numbers 1 to 32 in a circle, but the printed ring has 28 boxes (counted twice, by eye and by pixel analysis). The circle is open-ended and not an LP item, so nothing is drawn and the discrepancy changes no spec. (Decision 1 would apply if it were drawn: 32 would be the value the mathematics needs.)
- The book's P15 difference tower for squares stops after Level 2 with '...'; the cubes row has no printed levels. Both are teaching/blank figures; the spec fills the cubes tower from the LP numbers only.
- No printed answer exists in the book for the successive-differences question or for the Puzzle Time; the LP solution is followed (levels 7, 19, 37, 61, 91 / 12, 18, 24, 30 / 6, 6, 6 and the 17-number row were recomputed: all correct).
