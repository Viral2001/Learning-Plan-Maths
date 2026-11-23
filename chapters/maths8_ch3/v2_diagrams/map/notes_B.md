# Notes for chunk B (Class 8 Ch 3, topics M2.S12.T12 to M2.S21.T21)

Result: 30 items (18 units): required 17 / optional 1 / none 12. Validator: errors 0, warnings 0.

| role | required | optional | none |
|---|---|---|---|
| question (12) | 6 (C45, C50, C65, C67, C69, C71) | 0 | 6 (C43, C52, C54, C56, C58, C73) |
| solution (12) | 7 (C44, C51, C59, C66, C68, C70, C72) | 0 | 5 (C46, C53, C55, C57, C74) |
| worked_example (6) | 4 (C40, C47, C61, C62) | 1 (C41) | 1 (C48) |

All 57 base figures of this chunk are claimed (37 to items, 4 to concept images, 16 none). Figures of chunk A (P37-table-1) and chunk C (P23 onward, P42-mesopotamian_numeral-1..5) are not claimed here.

Media ids: the worked examples C40, C47, C61, C62 use `.IMG2` because `.IMG1` is a kept teaching image; every pair item uses `.IMG1`.

## 1. Judgement calls

- **Worked example "write X in Egyptian / base-5 numerals" (C40 = 2153, C47 = 89): required, ANSWER_IS_FIGURE.** The answer is a drawn numeral and the LP steps only describe it in words. The book's own pictures of this kind are 324 (page 15) and 143 (page 16); the LP examples use other numbers and those numbers are drawn. For C47 the teaching image C47.IMG1 already shows the same numeral (3 hexagons, 2 squares, 4 triangles); by the v3 rule the teaching image is never linked, so the example gets its own diagram, which duplicates that content.
- **C43 / C44 (Figure it Out p.62 Q1, "represent 10458, 1023, 2660, 784, 1111, 70707").** Question: none. The book question gives no figure; the symbol row on page 15 is teaching content and the LP `q_figure` hint ("the table of Egyptian symbols") is not a given figure. Solution: required. The printed answers (P37-egyptian_numeral-1..6) are six drawn numerals; one figure holds all six, each beside its number.
- **C45 / C46 (p.62 Q2, "what numbers do these numerals stand for").** Question required: the book gives two drawn numerals and the question says "these numerals". The LP text lists the counts in words, but per the 23 Nov decision that does not turn a figure the book gives into none. One figure holds (i) and (ii), with the labels (i) and (ii) drawn because the LP answer refers to the numerals by those labels. Solution none (SAME_AS_QUESTION_DIAGRAM + LATEX_ARITHMETIC): the answers 276 and 4322 are plain sums already in the LP steps.
- **C50 / C51 (p.63 Q1, "using the symbols in Table 2").** Table 2 is the base-5 symbol row of page 16 (the page prints no title; the question names it). A named table is drawn on the first item that shows it (v3 B2), so the question is required and shows the table only (six columns: label with the power of 5 above, shape below). The solution keeps the table in the same place and adds the five answer numerals below it in ANSWER (derived_from the question figure). No concept image of the chapter shows this table (T15 images are C47, C48, C49).
- **C52-C57 (zero cannot be represented, base-7 landmarks, "10 or more of a symbol")**: none/none. Word reasoning and powers of 7 / n; the book prints no pictures for them.
- **C58 / C59 (create a base-4 system, numbers 1 to 16).** Question: none (OPEN_ENDED, no figure). Solution: required, the printed answer is a picture (page 42). The answer is open, so the sample in the LP solution is drawn: dot = 1, stick = 4, square = 16. The book's sample uses an L-corner, a bold triangle and a square; the LP wins (the structure of all 16 entries is the same: sticks first, then dots; checked entry by entry against the book).
- **C61 (landmark times landmark), required.** The question asks for the products "in Egyptian numerals" and the answers are single symbols (lotus, tadpole, tadpole, arrow in base 5), so the answer is drawn symbols; the book draws its in-text products and their printed answers as pictures (pages 19-21, 40-41). The figure draws four product rows (the three Egyptian products are among the book's: coil x heel, lotus x coil, coil x lotus; the fourth row is the LP's own base-5 check, hexagon x circle = arrow) with the values printed under each symbol.
- **C62 (multiply by 10), required (borderline, see below).** The book works this example with symbol numerals (p.20 derivation (ii), p.21 "Now find" (i), printed answer p.41), and the result is a numeral whose symbols move up one landmark. The figure shows 121 x heel = 1210 and 522 x heel = 5220 in symbols.
- **C65 / C66 (Example 1, 87 + 78).** Question: required, the book gives the two numerals as a picture (page 17). Solution: required, the answer is the drawn sum; only the final state is drawn (the book's regrouping pictures are intermediate steps). See the print slip in section 4.
- **C67 / C68 (p.65 Q1 (i) and (ii)).** One figure holds both sums (the LP keeps them in one concept), labelled (i) and (ii) because the LP answer uses those labels. The book joins the numerals with the word "and"; the LP question writes "+", so a plus sign is drawn. Solution: one result numeral under each part.
- **C69 / C70 (counting board, 2907 + 43).** Question: required, the numbers exist only as counters on the board (page 22 left board). Solution: required, the board after the counters are brought together (page 22 right board: 2 counters on the 1000 line, one above and 4 on the 100 line, one above the 10 line, none on the 1 line, value 2950, all on the left of the partition). The book colours the board yellow, the counters red and adds two characters; those are decoration, replaced by the house style (counters filled INK in the question, ANSWER in the solution because all of them are the sum).
- **C71 / C72 (p.65 Q2, base-5 sum).** Question required (the book gives the two numerals as shape pictures, one line); solution required (the printed answer is the 14-shape row). The LP text lists the counts in words; kept required per the 23 Nov decision.
- **C73 / C74 (rule for multiplying by 5 in base 5)**: none/none, the answer is a rule in words and the book prints no picture.
- **Question cards of derived pairs are top-heavy.** Where a solution figure derives from a question figure (C50 to C51, C65 to C66, C67 to C68, C69 to C70, C71 to C72) the given part keeps its exact position and size and the answer is added below it in ANSWER, so the lower part of the question card is empty on purpose. This is stated in each `render_note`.
- **Glyphs.** The book's Egyptian symbols are hand-drawn. Every spec carries the same glyph key (stroke, heel, coil, lotus, finger; base-5 triangle, square, hexagon, circle, wave, arrow) with sizes and pitches, and `content` lists every glyph as [symbol, x, y, colour, scale], so nothing is left to the renderer's guess. Outlines follow the book's page 15 and 16 symbol rows; the book never names the Egyptian glyphs (it calls the second one an arch), the names heel, coil, lotus, finger, tadpole are the LP's. The hexagon is point-up/point-down (flat sides left and right), as printed on page 16.
- Layout was checked in code (every glyph and text inside a 0.45 margin, no overlaps) and a rough preview of all 17 figures was drawn once to look at the arrangement.

## Borderline

- **C62 required vs C41 optional.** Both examples give their numerals in words in the LP. C62 is required because the book itself works that example with drawn symbol numerals (the figure the book gives is the data and the answer picture); C41 ("An Egyptian numeral shows 3 lotuses, 4 heels and 6 strokes") is the LP's own example with no book figure and a teaching image of the concept that shows the numeral, so a picture would help but is not needed (optional, not added). If the team prefers one rule for both, C41 could be made required with a single 3 lotuses / 4 heels / 6 strokes numeral; it is not done here because no book figure exists for it.
- **C45, C67, C71 questions** stay required although the LP text carries the counts (decision 4 of 23 Nov).
- **C61** is required although the LP steps already write 1000, 100000 and 3125 as numbers: the question asks for the answer in Egyptian numerals.
- **C40 and C47** are required although the LP steps describe the symbol counts in words (the answer is the picture).
- **C46 none.** A figure annotated with the place values (200, 70, 6 ...) would be possible, but it would only repeat the question figure.
- **C43 question none, C50 question required.** The first has no named figure although the symbols are needed to attempt it; the second names Table 2. This follows the "named table" rule of v3 B2 literally.
- **C48 none.** The teaching image of the concept (base-3 landmarks) shows what a picture could show; the answer is numbers only.

## LP text issues

(Not edited; listed for the user.)

1. **M2.S16.T16.C50, M2.S17.T17.C52, M2.S17.T17.C54, M2.S21.T21.C71, M2.S21.T21.C73 (question_tex / text).** "base$-5$", "base$-7$" are written with the hyphen inside the dollar signs, so the LaTeX shows a minus sign: "base -5 system". In C54 the second occurrence is written "base-$n$" (correct). Suggested: "base-$5$ system", "base-$7$ system", "base-$n$ system" (or plain "base-5").
2. **M2.S16.T16.C50 (question).** "using the symbols in Table $2$" refers to a table that is nowhere in the LP text, and the solution C51 uses the names triangle, square, hexagon, circle, wave without defining them. The diagram supplies the table. Suggested sentence if the text should stand alone: "Table 2: triangle $= 1$, square $= 5$, hexagon $= 25$, circle $= 125$, wave $= 625$, arrow $= 3125$."
3. **M2.S20.T20.C69 (question).** "Add $2907$ and $43$ on the counting board." says nothing about the board. Suggested: "On the counting board, a counter on a line is worth that line's value and a counter in the gap above a line is worth 5 times it. Put $2907$ on the left of the partition and $43$ on the right, then find the sum."
4. **M2.S20.T20.C70, step 1.** "$2907$ has $2$ counters on the thousands line, $9$ on the hundreds line (one above it for $5$ and $4$ on it), none for tens and $7$ for ones" reads as 9 counters on the hundreds line and 7 on the ones line; what is meant is 9 hundreds and 7 ones. Suggested: "$2907$ has $2$ counters on the thousands line, $9$ hundreds (one counter above the hundreds line for $500$ and $4$ on the line for $400$), no tens, and $7$ ones (one counter above the ones line for $5$ and $2$ on it); $43$ has $4$ tens and $3$ ones."
5. **Book numbers.** The LP restarts the "Figure it Out" numbers in each topic, so they do not match the book: C45/C46 "Figure it Out, Q1" is the book's page 62 Q2 (ncert_ref FiOD.q2 is right); C52-C55 "Q1", "Q2" are the book's page 63 Q2, Q3; C56-C59 "Q3", "Q4" are the book's page 69-70 Q1, Q2; C71/C72 "Q1" is the book's page 65 Q2; C73/C74 "Q2" is the book's page 70 Q3. Only the labels differ; the questions themselves are the right ones.
6. **M2.S13.T13.C43 `q_figure` hint** ("the table of Egyptian symbols") and **M2.S12.T12.C41**: the book question has no figure; nothing to change in the text, only the hint is wrong.

## 3. Other things in the LP

- The solution text of C66 is right (15 strokes, 5 left over, 165); the book's picture is the one that is wrong (section 4).
- C72's check "182 + 412 = 594" and C68's checks (9608 + 507 = 10115, 1080 + 46 = 1126) were recomputed and are right; so are C40 (2153), C47 (89 = 3 x 25 + 2 x 5 + 4), C61 (25 x 125 = 3125), C62 (1210, 5220), C44 and C51 (all eleven numerals recounted against the printed answers on pages 37-38, which agree with the LP).
- No solution text contradicts the book except where noted (C59 symbols, C66 stroke count).

## 4. Where the book itself is unclear or wrong

- **Print slip, pages 17 and 18 (Example 1, 87 + 78).** The regrouping pictures draw 16 strokes (rows 3, 3, 3, 3, 3, 1) and end with 6 strokes (value 166); the two addends hold 7 + 8 = 15 strokes, the text above the picture says 15, the LP says 5 strokes are left (165). The printed solution (page 39, Figure it Out Q1 (i)) draws 15 strokes correctly. The C66 diagram shows the correct 5 strokes; the base inventory entries P17-egyptian_addition-2 and P18-egyptian_addition-1 keep what the book prints and carry a note.
- Page 20, derivation (i): a small stray mark crosses the first multiplication sign (print artefact, as the inventory notes).
- Page 22: the second counting board has no caption; it matches 2907 + 43 = 2950 and the LP.
- Page 41: the printed answer of the last product (finger x man) is the text 10^10 (no symbol exists); the LP does not carry that product.
- Page 16: the symbol row is not titled "Table 2" on the page; the question names it.
- Glyph outlines of lotus, finger and tadpole are described, not measured (the inventory says the same).

## 5. Figure mapping notes

- Printed-answer pages repeat several questions as pictures (P38-egyptian_numeral-1/2, P39-egyptian_addition-1, P40-egyptian_addition-1, P40-base5_addition-1, P40-egyptian_product-1/3, P41-egyptian_product-2/4): mapped none:SAME_AS_QUESTION_DIAGRAM (the chapter-page figure is the one that is drawn).
- In-text products and derivations of "Advantages of a Base-n System" (pages 19-21, answers 40-41) are not separate LP items; the LP carries them as the worked examples C61 and C62, so those figures are mapped to those items (question side of a worked example) with a note saying which parts the LP draws. P20-symbol_derivation-1 (2 coils x heel) and P41-egyptian_numeral-6 (lotus-heel x heel) are not carried by the LP: none:TEXT_SUFFICIENT.
- Teaching figures: P14-pebble_groups-1 and P15-symbol_row-1 are accounted to concept image C40.IMG1, P16-pebble_groups-1 to C49.IMG1, the blackboard panel P19-egyptian_addition-1 to C60.IMG1 (closest images, accounting only, nothing linked); P17/P18 inline symbols, the Hindu and base-5 blackboard panels and the 3426 abacus (P21-abacus-1) are none:TEXT_SUFFICIENT because no LP question or answer uses them.
- The Egyptian painting on page 14 (scenery) is decoration and is not in the base inventory.
