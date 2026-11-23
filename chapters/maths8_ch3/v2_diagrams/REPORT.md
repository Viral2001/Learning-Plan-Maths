# Class 8 Ch 3 A Story of Numbers - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths8_ch3` v36 (taken from staging). Result: new V2 version v37 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (82 items from 52 units)
{"worked_example": {"none": 13, "required": 6, "optional": 3}, "question": {"none": 24, "required": 6}, "solution": {"optional": 1, "none": 17, "required": 12}}

Optional, NOT added: [('C8', 'solution'), ('C41', 'worked_example'), ('C81', 'worked_example'), ('C82', 'worked_example')]

needs_lp_text_sync: []

## The 24 diagrams
| id | side | type |
|---|---|---|
| M2.S9.T9.C31.IMG1 | solution | other |
| M2.S10.T10.C35.IMG1 | solution | other |
| M2.S12.T12.C40.IMG2 | worked example | other |
| M2.S13.T13.C44.IMG1 | solution | other |
| M2.S14.T14.C45.IMG1 | question | other |
| M2.S15.T15.C47.IMG2 | worked example | other |
| M2.S16.T16.C50.IMG1 | question | other |
| M2.S16.T16.C51.IMG1 | solution | other |
| M2.S17.T17.C59.IMG1 | solution | other |
| M2.S18.T18.C61.IMG2 | worked example | other |
| M2.S18.T18.C62.IMG2 | worked example | other |
| M2.S19.T19.C65.IMG1 | question | other |
| M2.S19.T19.C66.IMG1 | solution | other |
| M2.S20.T20.C67.IMG1 | question | other |
| M2.S20.T20.C68.IMG1 | solution | other |
| M2.S20.T20.C69.IMG1 | question | place_value_model |
| M2.S20.T20.C70.IMG1 | solution | place_value_model |
| M2.S21.T21.C71.IMG1 | question | other |
| M2.S21.T21.C72.IMG1 | solution | other |
| M3.S22.T22.C75.IMG2 | worked example | other |
| M3.S23.T23.C80.IMG1 | solution | other |
| M3.S24.T24.C84.IMG2 | worked example | other |
| M3.S25.T25.C87.IMG1 | solution | other |
| M3.S25.T25.C89.IMG1 | solution | other |

### Chunk A notes (from the decision agent)
# Notes for chunk A (Class 8 Ch 3 "A Story of Numbers", topics M1.S2.T2 to M2.S11.T11)

Result: 19 units, 31 items. Required 2 (both solution side), optional 1, none 28. Figures claimed 15 (13 base + 2 NEW): 1 to an item, 3 to concept images, 11 none. Validator: errors 0, warnings 1 (expected, see C31 below).

The part of the chapter in this chunk is almost all words: counting methods, number names, Roman numerals. The book has only one answer that is itself a picture (Example (a), Roman addition), so only that one and its sibling (b) get a diagram.

## 1. Judgement calls

| Item | Decision | Why |
|---|---|---|
| M2.S10.T10.C35 (solution, Example (a) CCXXXII + CCCCXIII) | required, `M2.S10.T10.C35.IMG1` | The book prints the answer of this example as a picture: two drawings of the pooled letters with loops (5 C's -> D, 4 X's -> XL, 5 I's -> V = DCXLV). B2: printed answer is a picture, and the loops carry the meaning. Question side none (the question gives only two numerals as text). Drawn as two panels like the book; given letters INK, loops FOCUS, additions ANSWER. `derived_from` null (no question diagram). |
| M2.S9.T9.C31 (solution, part (b) LXXXVII + LXXVIII) | required, `M2.S9.T9.C31.IMG1` | Sibling of (a) in the same NCERT example, same kind of answer (a Roman sum by regrouping). The book prints NO picture for (b) ("Do it yourself now"), so the figure is my design from the LP steps: one row per symbol (C, L, X, V, I from top to bottom), the original letters in INK, each group that is exchanged looped (FOCUS) with an arrow up to the new letter (ANSWER) it becomes: five I's -> V, two V's -> X, five X's -> L, two L's -> C; the left-over C, L, X, V read CLXV. Every count comes from the LP steps (2 L, 5 X, 2 V, 5 I). The base inventory has no figure for it (hence the one validator warning). |
| M1.S3.T3.C8 (solution, stick arithmetic) | optional (not added) | A strip of four stick pictures (join / pair and take away / repeat / group) would clearly help, but the LP's four-line method is complete and the book's printed answer is text only. |
| M1.S2.T2.C4 (worked example, "use Table 1") | none, `LATEX_TABLE` | The item names Table 1, but it is a plain white table of numbers and Roman numerals, so it is a LaTeX array (Step C, plain table). See LP text issues: the table itself is not in the question text. |
| M2.S11.T11.C37 (solution, Hindu vs Roman features) | none, `LATEX_TABLE` | The printed answer is a plain two-column table of words (no colour, no marks). |
| M1.S7.T7.C22 (solution, Gumulgal arithmetic) | none | All four answers are number names in words, as printed in the book. The concept had two old solution cards; that does not make a diagram necessary. |
| M1.S6.T6.C18 (1345 by fives) | none | 1345 / 5 = 269 is arithmetic; drawing 269 symbols helps nobody, and teaching image M1.S5.T5.C15.IMG1 already shows the idea (not linked). |
| Worked examples C3, C13, C14, C23 (cows and sticks, Lebombo bone, Gumulgal names, 2367) | none | Each gives all its data in words and has a teaching image of the same idea (not linked). A drawing of the grouped notches (C13) or of 2367 in landmarks (C23) would show the answer, and a worked-example figure sits after the question text. |
| Open or discussion items (C9/C10, C11/C12, C19/C20, C38/C39) and the word items (C7, C21, C28, C30, C32, C34, C36) | none | `OPEN_ENDED` / `TEXT_SUFFICIENT`; the book gives no figure with them. |
| Printed answers C29, C33 (Roman numerals, products) | none | Text and arithmetic lines (MCCXXII, MMCMXCIX, CCCII, DCCXV; CCL, 25 M's, MMD, LXIII). |

Figure inventory choices (Step 0):
- To concept images (accounting only, nothing linked): P01 (cuneiform strip, p.1; section 3.1 has no unit of its own in the three chunks, so I claimed it because my units are the rest of 3.1) -> `M1.S1.T1.C1.IMG1`; P04 (cows and sticks) -> `M1.S2.T2.C3.IMG1`; P05-table-2 (letters a to z) -> `M1.S2.T2.C4.IMG1`.
- `none:LATEX_TABLE`: P05-table-1, P06-table-1 (Table 1), P09-table-1 (Gumulgal list), P11-table-1 (Roman landmarks), P37-table-1 (printed answer table of Q3).
- `none:NOT_RENDERABLE` (painted art or a real map, and no item of this chunk is built on it): P03 digit-evolution chart, P08 body counting, P09-map, P10 "quickly count" tiles, NEW-P08-bones-1.
- NEW figures I found: NEW-P08-bones-1 (photographs of the Lebombo and Ishango bones, p.8; no notch can be counted) and NEW-P13-daredevil-1 (Daredevil Contest cartoon with the speech bubble "Multiply CCXXXI and MDCCCLII", p.13; decoration, `DECORATIVE_ONLY`).
- Not listed (pure decoration, no mathematical content): the Reema-and-father cartoon (p.1), the person among a heap of mangoes (p.7), the Roman scene (p.11), the girl character (p.10, p.12), the Egyptian mural (p.14).
- P12 base description checked against the page picture: letters (CCXXXII over CCCCXIII), loop contents (5 C's, 4 X's, 5 I's) and labels (D, XL, V, = DCXLV) agree.

## 2. LP text issues

- **M1.S2.T2.C4 (worked example)**: the question says "use Table 1 to write 13 and 18 in Roman symbols" but Table 1 is not in the question text, and the concept text above it lists the symbols in one line ("I, II, III, ... XX (Table 1)") without the numbers they belong to. Suggested sentence for the question: "Table 1 gives the Roman symbols for 1 to 20 in order: I, II, III, IV, V, VI, VII, VIII, IX, X, XI, XII, XIII, XIV, XV, XVI, XVII, XVIII, XIX, XX." (or a LaTeX array with the numbers 1 to 20 above them).
- **Figure it Out numbers in the LP labels do not match the book's** (book numbers in brackets):
  - M1.S3.T3.C7/C8 "The Mechanism of Counting, Q1" = book Figure it Out Q1 (p.7): fine.
  - M1.S4.T4.C9/C10 "Figure it Out, Q1" = book Q2 (p.7); M1.S4.T4.C11/C12 "Figure it Out, Q2" = book Q3 (p.7).
  - M1.S6.T6.C19/C20 "Early Number Systems, Q1" = book Figure it Out Q1 (p.13).
  - M1.S7.T7.C21/C22 "Figure it Out, Q1" = book Q2 (p.13-14).
  - M2.S11.T11.C36/C37 "Figure it Out, Q1" = book Q3 (p.14); M2.S11.T11.C38/C39 "Figure it Out, Q2" = book Q4 (p.14).
  - The same labels ("Figure it out: Q1") repeat across topics (M1.S4.T4.C9, M1.S7.T7.C21, M2.S11.T11.C36), which a learner will see side by side.
- **M1.S7.T7.C22, step (iii)**: the sentence "write the first number two times and then double the result, 4 copies in all" is confusing (the answer 18 ukasar is right: 9 x 4 = 36). Suggested: "ukasar-ukasar is 4, so write the first number 4 times: 16 ukasar and 4 urapon; the 4 urapon make 2 more ukasar, so 18 ukasar."
- **M2.S8.T8.C23 (worked example)**: the LP numeral MMCCCLXVII is right; the book prints MMCCCLXII (missing the V; 2367 = 1000 + 1000 + 100 + 100 + 100 + 50 + 10 + 5 + 1 + 1). No diagram is drawn for this item; if a figure of it is ever drawn it must show MMCCCLXVII.
- **M2.S9.T9.C31 and M2.S10.T10.C35**: the solution figure will sit before step 1. The steps' wording ("Count the symbols ...", "Five I's make one V") fits the figure, so no text change is needed; if the figure is added, "Look at the picture first" is not required.

Checks I did on the LP solutions (all correct): 1345 / 5 = 269; (i) 9 + 7 = 16 = 8 ukasar, (ii) 9 - 6 = 3, (iii) 9 x 4 = 36 = 18 ukasar, (iv) 16 / 4 = 4; MCCXXII, MMCMXCIX, CCCII, DCCXV; 87 + 78 = 165 = CLXV; 5 x 50 = 250 = CCL, 50 x 500 = 25000 (25 M's), 5 x 500 = 2500 = MMD, 7 x 9 = 63 = LXIII; 232 + 413 = 645 = DCXLV.

## 3. Where the book itself is unclear

- The book prints no answer for part (b) (LXXXVII + LXXVIII), nor for the in-text question about 1345 in a system that counts only by 5s, nor for the "Try this" items (own number system, refining it).
- The loops in the book's Example (a) picture touch the neighbouring letter slightly (the third C of row 2); the groups themselves (5 C's, 4 X's, 5 I's) are certain.
- P10 ("quickly count" tiles): the counts of flowers, stairs and grapes cannot be read exactly (the base inventory says about 17, 12 to 14, about 40); not needed, no item uses it.
- P03 digit chart: the historic glyph shapes cannot be transcribed exactly; not needed.
- The book gives Gumulgal names only up to 6 ("ras" for anything larger); Figure it Out C Q2 extends the pattern of counting in twos, and the LP's solution follows that pattern.

## 4. Borderline

- **M2.S9.T9.C31 required** (the only one that could go either way). Reason for required: sibling consistency with (a) in the same example, and the four-step carry is where learners slip. Reason it could be optional: the book prints no picture for (b) and the LP steps carry every count. Flip to `optional` (action `drop_image`) if you prefer picture-only-where-the-book-has-one; the validator then needs the C31 item to be changed and the counts in `meta` adjusted.
- **M2.S10.T10.C35 required**: the LP steps already carry all the counts (decision 4: not flipped to none for that reason); required by B2 because the book's own answer is the picture.
- **M1.S2.T2.C4**: FIG_REFERENCED ("use Table 1") against LATEX_TABLE (plain table). I chose none + LaTeX array; the cost is only the LP text issue above.
- **M1.S3.T3.C8 optional vs none**: a four-picture stick strip would help; nothing in the book needs it.
- **M2.S11.T11.C37**: a filled comparison table could be read as ANSWER_IS_FIGURE; it is a plain table of words with no colour or marks, so none.
- **Worked examples with teaching images** (C3, C13, C14, C23): none, since the figure the example would need is the teaching image, which is never linked and would leak the answer if placed after the question.
- Figures P04, P05-table-2, P01 are mapped to concept images although the match is of idea rather than of the exact book picture (teaching images are redrawn, not copies); P03, P08, P09-map and P10 use `NOT_RENDERABLE` only to say "not drawn, no item needs it", not that an item is blocked.

### Chunk B notes (from the decision agent)
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

### Chunk C notes (from the decision agent)
# Chunk C notes (Class 8 Ch 3, topics M3.S22.T22 to M3.S28.T28)

Result: 21 items = 5 required (C75 worked, C80 solution, C84 worked, C87 solution, C89 solution), 2 optional (C81, C82 worked), 14 none. Validator: errors 0, 1 warning (C84 has no printed book figure, as expected: the book has no 5072 numeral). 30 base figures claimed (12 to items, 8 to concept images, 10 none).

Reminder on the brief: it says the pdf has no printed-solutions section. It does: pdf pages 35-46 are the printed answers. They were used for C80 (p.42), C87 (pp.43-44), C89 (p.44) and C95 (pp.44-45).

## 1. Judgement calls

- **No question side needs a diagram.** No book question of this chunk gives a figure (the Mayan and Chinese symbol tables are teaching figures on pdf pages 28 and 30). The `q_figure` hints on C86 and C88 describe symbol tables that are not part of the question, so the question items are `none` (C79, C86, C88, C94, C96, C98).
- **C80 (Mesopotamian Q1 solution), required.** Printed answer is a picture, so B2 applies. One picture for all five numerals, in 3600s / 60s / 1s columns, with the row labels (i) to (v) because the LP steps use them. The LP answer is the compact form (1 | 3, 2 | 12, 3 | 20, 1 | blank, 1 | blank | 5); the book prints the older form with a landmark diamond between the groups. The LP wins (brief rule), so the picture follows the LP. The two blank places that the LP names (1s place in (iv), 60s place in (v)) are marked with a dashed FOCUS box; the leading empty 3600s cells in rows (i) to (iv) are left plain.
- **C75 (worked, 4000 in own symbols), required.** The question asks for the written form with our own symbols; that is a drawing of wedges, chevrons and landmark diamonds (the book draws the same kind of numeral for 640 and 7530 on p.25). The two book numerals P25-numeral-1 and -2 are mapped to this item with a description saying the LP uses 4000 instead of 640 and 7530. This is a stretch of "it becomes that item's diagram"; the alternative is `none` for those two figures. Please keep or change at merge.
- **C84 (worked, 5072 in rod numerals), required.** The answer is the rod drawing ("5 heng, a blank, 7 heng, 2 zong"). Rod shapes follow the table on pdf page 30. Blank hundreds place shown with a dashed FOCUS box.
- **C87 (Mayan Q solution), required.** Four numerals in one picture, with place rows 360 / 20 / 1. No letters (i) to (iv) because the LP steps are numbered 1 to 4 and do not use letters (user decision 3). Number labels 77, 100, 361, 721 are drawn.
- **C89 (Chinese Q1 solution), required.** The printed answer is a picture (41 with an arrow to four vertical rods, a gap, one rod). The LP only says "5 rods in a row". I draw the book's picture with the slightly wider gap before the fifth rod (about 1.75 times the rod spacing, measured on the page picture), no tens/units labels.
- **C95 (Q2 solution), none, LATEX_TABLE.** The printed answer is a plain bordered table of text (Number / Base-2 / Gumulgal, rows 1 to 8), so it stays a LaTeX table (v3 rule), not a picture.
- **C77, none.** "Using our numerals for each place" gives plain digits 1 | 2 | 5 and the answer is text. This differs from C75 on purpose: C75 asks for the written form in the lesson's own wedge/chevron symbols (a drawing), C77 asks for digits.
- **Figure mapping.** Teaching figures with a matching teaching idea in `concept_images.json` were mapped to that concept image (P25-table-1 to C77, P26-table-1 to C81, P28-numeral-1 and P28-place_value_table-1 to C82, P30-numeral-1 and P30-place_value_table-1 to C84, P31 to C90, the summary board P32 to C100). These are accounting links only; nothing is linked. Inline glyphs, the symbol rows and the symbol tables with no matching teaching image are `none:TEXT_SUFFICIENT`. The world map P33-map-1 is `none:NOT_RENDERABLE` (no question works on it). I claimed P32-summary_board-1 and P33-map-1 because C91 cites "3.4.evolution_ideas" and "3.4.map", and no other chunk covers topic T29.

## Borderline

- **C81 (two wedges, gap, five wedges) and C82 (Mayan numeral: two dots, three dots, one bar), both `optional`.** Both questions describe the numeral completely in words and the answer is a number (125 or 7205; 785), so the tie-breaker says text is enough. A picture of the numeral would clearly help and the book shows the same idea (ambiguity table p.26; Mayan numeral p.28), so I did not choose a plain `none`. Neither is added to the plan. If you want them drawn they are easy upgrades: C81 = two wedges, a wide gap, five wedges (3 over 2); C82 = three rows stacked: 2 dots (360s), 3 dots (20s), 1 bar (1s).
- **C75 required vs C77 / C76 none**, see above (answer is a drawing in C75 only).
- **C89**: only five vertical lines, but the printed answer is a picture and the rule says solution required; kept required under user decision 4.
- **C84**: required although the LP text carries "5 heng, a blank, 7 heng, 2 zong"; kept required under user decision 4.
- **C90** (4072 as digits in places): a filled place value row is `none` (LaTeX) by the HEADER_BOXES_ONLY / LATEX_TABLE rule, even though a teaching image shows it.

## LP text issues

- **M3.S23.T23.C80**, `answer_tex`: the semicolon between (iv) and (v) is missing: "(iv): $1$ | blank (v): $1$ | blank | $5$". Suggested: "(iv): $1$ | blank; (v): $1$ | blank | $5$".
- **M3.S23.T23.C80**, step (iv): "written 1 followed by a blank" cannot be seen in a numeral (a trailing blank is invisible; it looks like the numeral for 1, which is the ambiguity of the next section). Suggested: "(iv): 60 = (1) x 60, so the 1s place is empty: written 1, with the empty 1s place after it (marked in the picture)."
- **M3.S23.T23.C80**: the LP gives the compact form (1 | 3 ...) while the book's printed answer draws the older form with a landmark diamond. Not an error, but the two differ; the diagram follows the LP.
- **M3.S28.T28.C96**, `question_tex`: "hadn'$t$ been invented" has a stray math wrapper around the t. Suggested: "hadn't been invented".
- **M3.S27.T27.C94 / C95 and M3.S28.T28.C98**: "base$-2$", "base$-10$" are set in math mode (the minus becomes a math minus sign). Suggested plain text "base-2", "base-10" like the book.
- **M3.S27.T27.C95**: the LP answer does not carry the comparison table of the book answer (Number, Base-2 system with ur = 0 and uk = 1, Gumulgal system, rows 1 to 8). Suggested: add that table as a LaTeX array. The step "the Gumulgal ... stopped at 6" is true of the chapter text, but the book answer extends the Gumulgal column to 7 (uk-uk-uk-ur) and 8 (uk-uk-uk-uk) by the same counting-by-2 rule; a short clause such as "(the book answer continues the Gumulgal names to 8 by adding words)" would remove the apparent conflict (optional).
- **M3.S25.T25.C89**, step 3: "$2$ then $3 (23)$", "$3$ then $2 (32)$": the bracketed number is inside the same math group. Suggested: "$2$ then $3$ ($23$)", "$3$ then $2$ ($32$)".
- **M3.S28.T28.C99**, step 3: "$25 = (1) \times 25 + (0) \times 5 + 0$". Suggested: "$25 = (1) \times 5^2 + (0) \times 5 + (0) \times 1$" (the book writes it this way).
- **M3.S22.T22.C75**: ncert_refs cite meso_640 and meso_7530 but the example is 4000; the step "written as 1 with the 3600 symbol, 6 with the 60 symbol, and 40" has no numeral shown anywhere except in the new diagram. Fine once the diagram is added; no text change needed.
- **M3.S26.T26.C92**: `ncert_refs` is empty (an LP-made example, no book source). Not an error.
- **Book numbers**: the LP numbering differs from the book for the last Figure it Out set: C88 "Place Value, Q1" is book Q1; C94 "Place Value, Q2" is book Q2; C96 "Figure it Out, Q1" is book Q3; C98 "Figure it Out, Q2" is book Q4. The one book set is split over three topics with restarted numbering.

## Book unclear or book slips (base inventory records what the book prints)

- **p.24, numeral for 59:** six chevron heads are printed with nine wedges (that would read 69); 50 has 5 heads and 40 has 4. A print slip. No item diagram uses the 59 numeral.
- **p.28, Mayan reading panel:** the expansion prints "(3) x 10" for the shell band, but the shell means (0) x 1; the total 4 x 360 + 11 x 20 = 1660 is right. Not used in any item diagram.
- **p.29:** the inline symbol printed after the word "dot" is the shell, not a dot. Print slip, no diagram affected.
- **p.42 printed answer (Mesopotamian Q1):** correct values, but printed in the older diamond form (see C80). (iv) 60 is printed as a wedge and the 60 diamond, so 60 and 1 are told apart by the diamond only.
- **p.44 printed answer (41 with zong rods):** the book picture shows the four-plus-one grouping with a visible gap; the book's own text then says the numeral could be read as 23, 32 or 122 if there is no significant space. The LP adds "as 5" and "122"; fine.
- **pp.44-45 table:** continues over two pages with the header repeated; the base inventory already records this as one figure.
