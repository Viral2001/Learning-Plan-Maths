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
