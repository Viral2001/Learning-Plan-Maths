# Class 7 Ch 8 Working with Fractions - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths7_ch8` v35 (taken from staging). Result: new V2 version v36 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (96 items from 59 units)
{"question": {"none": 34, "required": 3}, "solution": {"optional": 7, "none": 25, "required": 5}, "worked_example": {"required": 3, "none": 19}}

Optional, NOT added: [('C8', 'solution'), ('C10', 'solution'), ('C52', 'solution'), ('C87', 'solution'), ('C110', 'solution'), ('C112', 'solution'), ('C114', 'solution')]

needs_lp_text_sync: [('C106', 'worked_example'), ('C109', 'question')]

## The 11 diagrams
| id | side | type |
|---|---|---|
| M1.S6.T6.C26.IMG1 | worked example | fraction_model |
| M1.S6.T6.C28.IMG2 | worked example | fraction_model |
| M1.S7.T7.C31.IMG1 | solution | fraction_model |
| M1.S7.T7.C33.IMG1 | solution | fraction_model |
| M1.S8.T8.C35.IMG1 | solution | fraction_model |
| M1.S10.T10.C42.IMG1 | solution | fraction_model |
| M1.S13.T13.C56.IMG1 | solution | object_row |
| M3.S23.T23.C106.IMG2 | worked example | geometry_figure |
| M3.S24.T24.C109.IMG1 | question | geometry_figure |
| M3.S25.T25.C111.IMG1 | question | geometry_figure |
| M3.S25.T25.C113.IMG1 | question | other |

### Chunk A notes (from the decision agent)
# Chunk A notes (Class 7 Ch 8, units 1-19: M1.S3.T3 to M1.S10.T10)

Result: 32 items. required 6 / optional 2 / none 24. Validator: errors 0, one warning (C42 has no inventory figure because the book prints none, see 1.5).

| role | required | optional | none |
|---|---|---|---|
| question | 0 | 0 | 13 |
| solution | 4 (C31, C33, C35, C42) | 2 (C8, C10) | 7 |
| worked_example | 2 (C26, C28) | 0 | 4 (C36-C39) |

## 1. Judgement calls

1.1 **Four-panel pictures for Figure it Out (C35 = book p.180 Q1, C42 = book p.181 Q2).** Each answer has four sub-answers (a)-(d), and the book prints four separate pictures for Q1 (pp.32-33). The brief says a pair gets at most ONE solution diagram, so each is one 16:9 picture with four unit squares side by side, captioned with the product (no panel letters, no "parts" labels). If the user would rather have four pictures per answer, the pair would need extra media ids (IMG2..IMG4) and the brief changed.
   - The fifth part of Q1, 1/12 x 1/18 = 1/216, is NOT drawn: a 216-cell square is unreadable, the book prints no picture for it and itself calls drawing it "cumbersome" (p.9).
   - Q2 (C42): the book prints no picture ("Draw the figure in the same manner as shown in question 1", p.34). I made the solution `required` for sibling consistency with Q1 (same instruction, same kind of answer). It follows the book's own convention (p.9): rows = denominator of the multiplicand, columns = denominator of the multiplier, band = top rows, product = left columns of the band. All four products were recomputed: 8/15, 2/12 = 1/6, 3/10, 12/30 = 2/5.
   - The question sides of Q1 and Q2 are `none`: they give no figure, the learner is asked to draw.

1.2 **T7 solutions C31 (1/2 x 1/4) and C33 (3/4 x 2/5) are `required`, although the answer is a number.** The LP solution steps themselves shade 1/4 of the unit square, cut it, and count "8 equal parts and 1 shaded" / "5 rows, 4 columns, 20 parts, 2 then 6 shaded". A learner cannot follow those steps without the picture and the book prints it (pp.6-7). The tie-breaker (would the picture change how easily they follow it) says yes. They repeat the two teaching examples (teaching images C25 and C27 show the same figures); v3 forbids linking a teaching image, so each gets its own copy (same layout, solution marks in ANSWER green). Question sides are `none` (no figure is given).

1.3 **Worked example C28 (5/4 x 3/2, Fig. 8.2) is `required` and duplicates the kept teaching image M1.S6.T6.C28.IMG1 in the same card.** v3 says a referenced numbered/lettered figure is drawn even when a teaching image shows it, and a teaching image is never linked. The new image gets id C28.IMG2 (IMG1 is kept). It shows the complete figure the steps read off (12 cells = 3/2, first column of 3 cells highlighted = 3/8). If the user prefers no duplicate inside one card, this is the item to change to `none`.

1.4 **Worked example C26 (area link, Fig. 8.3) is `required`.** The book question names Fig. 8.3 ("what is the length and breadth of the shaded rectangle"); the LP rewrites it as "in the unit square, a shaded rectangle ... 8 such rectangles fill the square" with no figure. Only the one shaded rectangle is drawn, with its sides 1/2 and 1/4 marked (the question gives them); the book's 1/8 arrow (the answer) and its yellow top row are left out. No teaching image shows this figure (C26 has no kept image).

1.5 **Figures mapped to two uses.** P06-fraction_grid-1, P07-fraction_grid-1 and P07-fraction_grid-4 are each claimed twice: the base id maps to the teaching image (accounting) and a `NEW-<id>-sol / -we` entry maps to the item that redraws it (rule: a figure used twice is two entries). Required item C42 has no printed figure at all, hence the validator warning (acceptable, see 1.1).

1.6 **T3 solutions C8 (tortoise, 3 hours) and C10 (Aaron, 2/5 hour) are `optional`.** The book draws a number line for each (p.1, p.3), but the answers are numbers, the LaTeX steps are complete (repeated addition; 3 / 5 then x 2) and the same lines are already teaching images (T1 C1 tortoise path; T2 C4 "3 km cut into fifths", which is exactly C10's picture). Picture only makes it nicer, so not added. Same decision for both (siblings). The earlier author's `s_figure` hints for these two are not followed.

1.7 **T9 worked examples C36 (1/12 x 1/18) and C37 (5/12 x 7/18) are `none`.** C36 literally says "without drawing the unit square"; both have 216-cell grids in the book (pp.9-10), which are only schematic ("18 parts", "12 parts") and are unreadable at card size; teaching images C36.IMG1 (3 x 6) and C37.IMG1 (3 x 5 overlap) already carry the rows-times-columns idea. C38 and C39 (whole number as n/1) are plain arithmetic.

1.8 **T4 (Examples 1, 2) and T5 (Figure it Out Q1-Q5)**: all `none`. No figure in the book, printed answers (pp.31-32) are text. Q4 (Moon, 10 pm + 2 1/2 h) could be a clock or time line but the book gives none and the arithmetic is complete.

1.9 **Figure inventory choices.** P01 is mapped to the nearest teaching image M1.S1.T1.C1.IMG1 (tortoise on a path); that image is the LP's own picture of the situation, not a copy of the book line. P02 and P03 map to M1.S2.T2.C4.IMG1. The pages 1-4 teaching figures belong to topics T1/T2 that have no unit in any chunk, so chunk A claims them (they sit in the book section of the T3 questions, which repeat the same two walks). P10-annotated_expression-2 (12/7 x 5/24, p.10) belongs to T11 (chunk B) and is NOT claimed here.

## 2. Things in the LP or the brief that look wrong

2.1 **Book numbers**: C41/C42 (T10) carry `book_number` "Figure it Out 8.1, Q1" but the question is Q2 of the second Figure it Out set (book p.181). C34/C35 (T8) is Q1 of the second set (p.180). The LP has three topics all labelled "Figure it Out 8.1" with overlapping Q numbers (T5 Q1-Q5 of the first set; T8 Q1; T10 Q2). I put the true book page and number in `ncert_ref`.

2.2 **The brief says the pdf has no printed-solutions section, but pdf pages 31-39 are one** (printed answers, with unit-square pictures on pp.32-33). I used it for the four Q1 pictures and the printed answers.

2.3 **Concept names**: C26 is named "Half of a quarter" but its block is the area-of-a-rectangle link (Fig. 8.3); the half-of-a-quarter teaching image sits in C25. C38 and C39 share the name "Whole numbers as fractions over 1". Unit-level `ncert_refs` are empty for C26 and C39 while their items carry refs (8.1.area_link, 8.1.whole_as_fraction). Cosmetic.

2.4 No LP solution contradicts the book. Every answer was recomputed: 3/4; 6/5 = 1 1/5; 10/3 = 3 1/3; 10; 7/2 and 31/2; 1/8 and 5/8 km; 5/3 and 20/3 l; 5/2 h so 12:30 am; 21/5, 4/3, 54/7, 78/11 with mixed forms 4 1/5, 1 1/3, 7 5/7, 7 1/11; 1/8; 15/8; 3/10; 1/15, 1/12, 1/10, 1/30, 1/216; 8/15, 1/6, 3/10, 2/5; 216; 35/216; 9/4; 12/5.

## 3. Places where the book itself is unclear or wrong

3.1 Figure (b) of the printed answer to Figure it Out Q1 (p.33) says "5 parts" under the grid although it has 4 columns (4 x 3 = 12). Not copied: the new picture has no parts labels.

3.2 p.10 prints "5/12 x 7/8 = (5 x 7)/(12 x 18)": the 7/8 is a misprint for 7/18. The LP has 7/18 (correct).

3.3 p.7 second arrow row says "Divide the multiplicand by 3" for the step that multiplies by 3, and ends in a dangling "=". Book wording, not drawn (accounted as `none:LATEX_ARITHMETIC`).

3.4 Printed answer to Q4 (p.31) reads "10 + 2 + 1/2 = 12 am Or 12:30 am"; the LP's "12:30 am" is the clean form.

3.5 The book's unit squares are drawn as rectangles in some pictures (for example p.33 (c) is 3:2); the new pictures draw every whole as a true square so that rows and columns show the fraction correctly.

### Chunk B notes (from the decision agent)
# Chunk B notes (Class 7 Ch 8, units 20-42)

Result: 32 items = question 0 required / 0 optional / 9 none; solution 1 required / 1 optional / 7 none; worked example 0 / 0 / 14 none. 14 base figures claimed: 0 to items, 2 to the concept image M1.S14.T14.C63.IMG1, 12 `none`. Validator: errors 0, one warning (the required item has no printed book figure, see 1a).

## 1. Judgement calls

a. **M1.S13.T13.C56 (Figure it Out 8.1 Q4, saplings) solution: REQUIRED, the only diagram of the chunk.**
   The book prints no picture; it only hints "Draw a rough diagram with four saplings...". The LP solution's first step is "Draw four saplings in a row: there are 3 gaps between the first and the last". The usual slip is 4 x 3/4, so the picture changes how correctly the student solves it (tie-breaker). Question side `none` (the book gives no figure; no question diagram when none is given). The spec is a row of 4 saplings, three gaps labelled 3/4 m, a bracket 9/4 m in ANSWER green. `derived_from` null. The validator warns that no base figure maps to it; that is true and expected.

b. **M1.S13.T13.C52 (Figure it Out 8.1 Q2, Somu's land) solution: OPTIONAL, not added.** A bar cut into 36 equal parts (road 6, Krishna 15, Bora 10, Somu 5) would show the shares clearly. The subtraction 30/36 - 15/36 - 10/36 = 5/36 in the steps is complete, so it is not needed.

c. **Cancelling and reciprocal "annotated expressions" (P10-ann-2, P11-ann-1, P11-ann-2, P15-ann-1/2, P16-ann-1/2) -> none (LATEX_ARITHMETIC).**
   They are fraction arithmetic with strike-throughs, circles and boxes. The LP steps already say in words which numbers cancel and what they become, and topic T11 has a cancelling tool and videos, T17 has videos and a practice tool. HIGHLIGHT_MEANING was considered (the black pair and the red pair in P11-ann-2), but nothing is lost without the colours because the pairs are named in the text. The LP text uses no `\cancel` anywhere; if the content team wants strike-throughs they can add them in LaTeX.

d. **Dividend / Divisor / Quotient callouts (P14-labelled_expression-3, P16-labelled_expression-3) -> none (TEXT_SUFFICIENT).** They only name the parts of one division. The worked examples C69 and C74 do not need the labels to be solved (C74's steps name "divisor", "dividend" and "reciprocal" in words).

e. **M2.S18.T18 (Figure it Out 8.3 Q1, Evaluate) both sides none, although the printed answer (P37-table-1) is a table.** It is a plain boxed grid: no colour, no meaning in cell position, two empty boxes. B2 "printed answer is a picture" is aimed at arrangements; this is a LATEX_TABLE / NUMBER_LIST_IN_BOXES case. The question text already lists (a) to (j) and the LP solution has all ten results with working.

f. **M1.S14.T14.C63 (order of multiplication, worked) -> none (TEXT_SUFFICIENT + REUSES_CONCEPT_IMAGE).** The picture the example talks about (two unit squares with a 1/8 rectangle, one turned) is already the kept teaching image M1.S14.T14.C63.IMG1 in the same concept (P14-fraction_grid-1/-2 map to it). The example question needs no figure to be solved, and a second copy in the same concept adds nothing. If the reviewer wants an own diagram anyway, the spec would be the same two-square picture: it was not written because the item does not need it.

g. **Three-situations worked examples (C59, C60, C61) -> none.** The book's Situation / Multiplication / Relationship table (P13-table-1, red outline, pink header) is plain text, no colour meaning: LATEX_TABLE. A number line placing the product between or beyond the two numbers would help a little, but the book has none and the text (twentieths for C60) is exact, so nothing is marked optional.

h. **Sibling consistency in Figure it Out 8.1 Q1-Q5:** Q1, Q2, Q3, Q5 solutions are arithmetic, so none (Q2 optional, see b); Q4 differs because its solution step is itself a drawing (see a). The questions are all none (word problems, no given figure).

i. **Practice duplicates:** M1.S12.T12 (12/7 x 5/24) is decided like the worked example C44 (none on both sides).

## 2. Things in the LP that look wrong or odd

- M1.S16.T16.C67/C68 carry `book_number` "Figure it Out 8.3, Q1" but the question is Q9 of the 8.3 Figure it Out (book p.25, answer "(a), (c) and (e)"); the real Q1 is the Evaluate grid in M2.S18.T18.C76/C77, which has the same label. Two different questions are both called "Figure it Out 8.3, Q1".
- M1.S13.T13 labels its five questions "Figure it Out 8.1, Q1" to "Q5"; section 8.1 has three Figure it Out sets (Tenzin, unit squares, and this tank set from book p.11-12), so "Q1" repeats earlier labels. The book prints "Try This" beside part (e) of the tank question; the LP drops it (harmless).
- M1.S13.T13.C55 question text omits the book's hint "[Hint: Draw a rough diagram with four saplings with distance between two saplings as 3/4 m]". The solution step 1 ("Draw four saplings...") assumes it. Consider adding the hint sentence to the question text.
- M1.S12.T12.C47 asks 12/7 x 5/24, the very sum already worked in the teaching concept M1.S11.T11.C43 (book p.10-11). So the "question" repeats the lesson's example.
- M2.S17.T17.C73 ("Find 2/3 / (3/5)") and C74 ("Find 2/3 / (3/5) using the reciprocal") are the same sum with the same answer 10/9, as in the book (p.16 and p.17); two worked examples for one sum.
- No contradiction between LP solutions and the book's printed answers in this chunk (all values rechecked: 7/30, 7/15, 21/40, 49/100, 10/7; 5/6, 5/12, 5/18, 5/36; 36 sq ft; 9/4 m; 600 g against 400 g; the ten quotients; 6 / 22 1/2 for the fill-in-the-blanks). The LP only adds mixed-number forms (1 3/7 hours, 2 1/4 m, 4 1/2, 1 1/9).

## 3. Places where the book is unclear

- The Evaluate grid (book p.24, answers p.37) has two empty boxes (row 2 column 4 and row 3 column 4) and no instruction for them (probably for the student's own sums). The LP lists only the ten given expressions.
- Q4 saplings: the book gives a hint to draw but prints no figure, so the spec follows the LP text (four saplings, three gaps of 3/4 m); no spacing in the book to copy.
- The base description of every figure in this chunk was checked against the page pictures (pages 10, 11, 13, 14, 15, 16, 24, 37): no correction was needed.

### Chunk C notes (from the decision agent)
# Notes, chunk C (units 43-59), Class 7 Ch 8 "Working with Fractions"

Result: 32 items = required 4 / optional 4 / none 24. Required: worked example Fig. 8.4 (M3.S23.T23.C106.IMG2), practice (a)+(b) question figure (M3.S24.T24.C109.IMG1), Figure it Out Q10 question figure (M3.S25.T25.C111.IMG1), Fig. 8.7 ants question figure (M3.S25.T25.C113.IMG1).

## 1. Judgement calls

1. **Every solution side is optional or none (nothing added).** The four figure questions (practice a/b, Q10, ants) have numeric answers and the book's printed answers (pp.36, 38, 39) are text only, the figure being just repeated. Prompt Step E: "figure-based question, numeric answer: Q required, S none (or optional if the solution splits the shape)". I marked them `optional` and wrote in each `reason` exactly what the solution figure would carry (same layout, ANSWER-green marks): 
   - practice (a)/(b): 1/8 on the corner triangle, 3/8 on the band; 1/4 on the top-left small square, 1/16 on the shaded pair;
   - Q10: bottom-right quarter 1/4, top triangle, shaded piece 3/32 (see LP slip below);
   - ants: 1/2, 1/2; 1/4, 1/4; four 1/16; 1/32, 1/32 on the paths and totals 29/32, 3/32.
   If you want these labelled solution figures, they are cheap to add (derived_from the question diagram).
2. **Example 3 (milk in each cup): nothing drawn.** The book prints a tape strip (P18), but it carries no data beyond the words, so question = none (TEXT_SUFFICIENT); the solution tape (1/4 litre cut in 5, one part 1/20 litre) is `optional`. P18 is mapped `none:TEXT_SUFFICIENT`. Say so if you want it required.
3. **Example 4 (bricks): nothing.** The book has no figure; the LP's "unit square of 25 bricks" hint is the teaching image of an earlier topic (M3.S20.T20.C83.IMG1), never linked.
4. **Worked example M3.S23.T23.C106 (Fig. 8.4): required.** One picture merges Fig. 8.4 (given), the red outline of Fig. 8.5 and the yellow half-triangle of Fig. 8.6, because the LP question describes all three (red quarter, yellow triangle, shaded 3/4 of it). media_id is IMG2 because IMG1 is the kept teaching image. P20-shape-2, P20-shape-3 and P21-shape-1 are mapped to that teaching image (accounting only).
5. **Palette gap:** the style table has no red or yellow token. The "red" quarter is a FOCUS (pink) outline and the "yellow" triangle is SET_B (amber, 45 percent). `needs_lp_text_sync: true` on this item: the question text could say "outlined" / "amber" instead of "red" / "yellow" (or the builder may allow red and yellow for this one figure, your decision).
6. **Practice (a)+(b): ONE question image holds both figures** side by side (left = first block, right = second block) because the brief allows one question diagram per pair; the v3 prompt section 2 would otherwise give each part its own. The figures are drawn exactly as printed (including the lines the LP words do not mention). `needs_lp_text_sync: true`: the second block's text says "a big square is split into four equal squares" but the book's figure (b) leaves the bottom half as one 2:1 rectangle and the top-right square empty.
7. **Q10 apex:** the printed V apex sits a little above the quarter's centre (about 0.47 of the way down); the spec puts it exactly at the centre because the book's answer 3/32 only works there.
8. **Ants figure** is portrait (about 0.87 wide to high) but kept at 16:9 as the pipeline draws cards; the frame is centred at 0.92 of the card height. Paths are MARK_FILL bands with an INK edge, split points FOCUS dots; the book's red labels bars use CELL_FILL.
9. **Figures claimed outside any unit:** P23-grid-1 (Pinch of History text, concept M3.S26.T26.C117, no question item), P27-chessboard-1 and -2 (Puzzle Time queens, concept M4.S29.T29.C123, no question item) and P29-cutout-sheet-1 (Learning Material Sheet, never referred to). No unit of chunk A, B or C covers them, so the merged completeness check would fail otherwise. Mapped `none:TEXT_SUFFICIENT`, `none:OPEN_ENDED` (x2), `none:DECORATIVE_ONLY`. Drop these four entries at merge if another chunk or the orchestrator claims them with the same meaning.
10. Text items (Example 4, 5, Figure it Out Q2-Q8, dramma, coins, Q12) are all plain words / LaTeX arithmetic: none. Q8 (cake) and the coin chain could take a bar or flow picture, but the text is complete.
11. Printed-answer pictures P36-shape-1/2 and P38-shape-1 only repeat the question figures: `none:SAME_AS_QUESTION_DIAGRAM`.

## 2. Things in the LP that look wrong (not edited by me)

- **M3.S22.T22.C92 / C93, Figure it Out Q2(c)(iv):** the LP text reads "5 x 6/3 / (7/9)" (question, question_tex, text, and the copy of the question in the answer concept). The book prints "(iv) 5 x 6". Looks like leaked text from the Q1 table (3 / (7/9)).
- **Book numbers are shifted / duplicated:** T22 items are labelled Q1..Q7 but are book Q2..Q8; T25 "Q1", "Q2" are book Q10, Q11; T28 "Q1" is book Q12. Meanwhile chunk B labels book Q1 (evaluate table) and Q9 (565/465) also "Figure it Out 8.3, Q1", so the label "Figure it Out 8.3, Q1" is used by 5 different items.
- **M3.S25.T25.C112 (Q10 solution) has the wrong geometry in steps 2-3** though the final 3/32 is right. With the V apex at the centre of the quarter the top triangle is 1/4 of the quarter (1/16 of the whole), not "half of it, 1/8"; the shaded piece is half (not 3/4) of the part below the V. Correct chain: 1/4 (quarter) x 3/4 (below the V) x 1/2 (left of the vertical) = 3/32. The LP's product 1/4 x 1/2 x 3/4 gives 3/32 only by commutativity.
- **M3.S24.T24.C109 second block:** "split into four equal squares" does not match the book figure (see call 6). Both blocks carry the same book_number and neither names "figure (a)" / "figure (b)".
- **Stale s_figure hints:** C97 says "four saplings in a row, gaps 3/4 m" (that is chunk B's Tsewang question, not the Sridharacharya sum); C89 describes the 25-brick teaching image; C87, C110, C112, C114 describe solution figures that this run leaves optional.
- **M3.S27.T27.C119:** the LP drops "1 pana = 6 mashakas" from the book's exchange list (harmless); the answer is consistent (1/48 dinar, 1/1440 dinar).
- Arithmetic re-checked and correct: Ex 3 (1/20), Ex 4 (375/2 = 187 1/2), Ex 5 (1 + 2 + 4 + 5 = 12, 1/12 day), Q2 (32, 1/16, 30), Q3 (1/8 kg), Q4 (40), Q5 (200), Q6 (44 km), Q7 (4 2/3), Q8 (1/15), dramma (6/7680 = 1/1280, 1 cowrie), Q12 (1/2, 1/3, 1/5, 1/10, 1/n), ants (29/32 + 3/32 = 1).

## 3. Where the book is unclear

- Fig. 8.4 and practice figure (a) share the same line set (both diagonals, the half-side segment, the quarter with its four small squares); the book never says which lines matter, so all are drawn as printed.
- Practice answer (b) calls the shaded part "the red shaded part" but the page shows orange-brown hatching.
- Fig. 8.7 prints no fractions; the four paths leaving the third point were verified at 4x zoom (2 to Mango, 1 up to the fourth point, 1 long path to Sugarcane).
- The pdf has printed answers on pages 31-39 (the brief says none); I used them only to check that the printed answers of these questions are text.
