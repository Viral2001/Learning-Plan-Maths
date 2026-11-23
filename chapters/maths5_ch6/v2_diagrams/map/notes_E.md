# Notes for chunk E (Class 5 Ch 6 "The Dairy Farm"), written by the chunk E agent

Chunk E = topics M3.S25.T25, M3.S26.T26, M4.S27.T27, M4.S28.T28, M4.S29.T29, M4.S30.T30, M4.S31.T31 (19 units, 32 items).
Result: required 12 / optional 1 / none 19; validator errors 0 (8 warnings: 6 are long visible_text strings that are the book's own cell texts, 2 say that C134 and C145 have no base figure because those two worked examples are written by the LP and not printed in the book).

Required: 
- Let Us Do Q1 box set: C136 (question) and C137 (solution).
- Let Us Do Q4 base-ten arrays: C142 (question) and C143 (solution).
- Let Us Think Q1 coloured digit boxes: C147/C148 (a to c), C149/C150 (d to f), C151/C152 (g to i), question and solution each.
- Worked examples: C134 (array of squares, id IMG2 because IMG1 is the kept teaching image) and C145 (digit-box frame).
Optional (not added): C154 (Let Us Think Q2 matching lines, solution side).
None: all ten "Check, Check!" items (T26), C121, C133, C144, C155, Let Us Do Q2 and Q3 (four items), Let Us Think Q2 question (C153).

## 1. Judgement calls

| Item | Choice | Why |
|---|---|---|
| T26 "Check, Check!" a to e, both sides (10 items) | all `none` | Each child's solution is a column layout of plain numbers; every number is in the LP question text and the steps. v3 "Not a diagram": column arithmetic is LaTeX (`LATEX_ARITHMETIC`). Same decision for all five (sibling rule). The question figure of (e) (Asher) is a place value table with header boxes T Th, Th, H, T, O filled with digits plus carry circles and crossed-out carries: `HEADER_BOXES_ONLY` says "boxes filled with digits -> LaTeX array". The carry marks do not decide what the student must check (the missing zeros). The solution of (e) (corrected rows 1,878; 12,520; 187,800) is the same kind of arithmetic. |
| C136 / C137 Let Us Do Q1 | question `required`, solution `required` (derived) | The question talks about "the one given at the top of each box" and the answer is positional ("the second", "both", "the first and the third"): box and cell structure carries the question; the solution selects cells (11 shaded, 6 white). Letters (a) to (h) are shown because the LP answer refers to boxes by letter (decision 3). |
| C138/C139 Q2, C140/C141 Q3 | `none` | Q2 nine plain products (the book has no figure); Q3 open-ended. |
| C142 / C143 Let Us Do Q4 | both `required` | The book prints three base-ten arrays (17 × 23, 17 × 24 with a blue column, 18 × 23 with a blue row); the question asks which amount is added by looking at them. The solution adds the tags "add 17" and "add 23" on the blue strips (words from the LP steps). |
| C147-C152 Let Us Think Q1 (a)-(i), six items | all `required` | Book question: "coloured boxes... the same colour indicates the same number" needs the frames (FIG_REFERENCED / HIGHLIGHT_MEANING). Solutions are the same frames filled in with ONE sample per frame taken from the LP's own check lines (11 × 3 = 33, 148 × 3 = 444, 1,111 × 3 = 3,333; 24 × 5 = 120, 110 × 5 = 550, 2,222 × 5 = 11,110; 202 × 9 = 1,818, 857 × 7 = 5,999). For (i) the LP says there is no answer: the frame is drawn as printed with the tag "no digits fit" (the LP's words) in WRONG. Letters shown (decision 3). |
| C153 question | `none`, `NUMBER_LIST_IN_BOXES` | Plain two-column list, no colour or arrow in the question. |
| C154 solution | `optional` (not added) | v3 section 3 says arrows between listed numbers are only `optional` when the text answer is complete; the LP answer lists the five matches. The picture that would help is written in the item's reason. |
| C121, C133, C144, C155 worked examples | `none` | All text/arithmetic. C155 is a plain day-by-day table (3, 6, 12, 24, 48 and 1, 3, 9, 27, 81): `LATEX_TABLE`. |
| Number style | LP style in the figures | The book prints the top cells of Let Us Do Q1 as "1001 × 5" and "1999 × 2" but "1,000 × 6", "2,000 × 2 - 4"; the LP text writes 1,001 and 1,999, so the figure follows the LP (the card shows text and picture together). Minus drawn as the minus sign. |
| Puzzle colours | fixed hex values in the specs | The box colours in the digit puzzles are the book's data (same colour = same digit), so they cannot be style tokens: BLACK = INK, ORANGE #F28E2B, PURPLE #A66BBE, BLUE #2F6DB5, GREEN #6AAB3C, RED #D93A2B, BROWN #7A5230. Digits entered by the solution are ANSWER green #009E73, which is close to the puzzle green outline: the render step should keep the outline thick (5 px) and the entered digits bold. |
| Figure inventory | one NEW- entry per second use | The base figures of the box set, arrays and digit boxes are mapped to the question item; each is claimed again as `NEW-<base id>-sol` for the solution item that redraws it (32 entries: 26 to items, 6 none). The two LP-written worked-example figures (C134, C145) are not in the book and have no inventory entry. |

## 2. Borderline (v3 rules applied as written)

- **C145 (worked example, digit puzzle "two black boxes x 6")**: `required`. The LP text describes the boxes in words, so a careful student could solve it from the text; I drew it because box colour (same colour = same digit) is the whole rule of the example and the same kind of frame is required for the book's Let Us Think questions. If the user prefers "text carries it", flip to `none` (`TEXT_SUFFICIENT`).
- **C134 (worked example, "Grow from a Known Product")**: `required` with its own figure (media id IMG2, IMG1 is the kept teaching image). The steps start "Picture 7 rows of 14 squares" and argue only from the added column, the removed row and the ten added rows. Panels A and B repeat the teaching image by design (decision 5); panel C (17 × 14) is not in the teaching image.
- **C143 (Let Us Do Q4, solution)**: `required` although the book's question figure already shows the blue strips; the solution adds only the two tags "add 17" and "add 23" (the answer to "17 or 23?"). A reviewer who thinks this only repeats the question figure can switch it to `none` (`SAME_AS_QUESTION_DIAGRAM`). The LP steps also take a column and a row away for (c) and (d); the book's pictures show only the added strips, so only those are tagged.
- **T30 Let Us Think solutions**: the answer to "find the possible values" is a list of digits, drawn as one sample filled frame per frame (the LP's check line). (d) has ten answers and (f) has two (2,222 and 3,332); the figure shows one sample each and says so in `render_note`.
- **C131 / C132 (Asher, T26 e)**: `none` on both sides; the table with carries could also be argued as `required` (HIGHLIGHT_MEANING). Chosen `none` because of the explicit `HEADER_BOXES_ONLY` rule and sibling consistency with (a) to (d).
- **C154**: `optional` (matching lines), not `required` (ANSWER_IS_FIGURE), because of the explicit `NUMBER_LIST_IN_BOXES` rule.
- **C155**: a growth chart would be an alternative to the table; kept as LaTeX table (`none`).

## 3. LP text issues (not edited; suggested sentences)

- **M4.S28.T28.C142** (Let Us Do Q4 question): the text never mentions the three arrays of squares, although the answer talks about "the new column" and "the new row". Suggested: "Look at the three arrays of squares: 17 rows of 23, 17 rows of 24 and 18 rows of 23. The blue squares are the ones added to the first array."
- **M4.S28.T28.C136** (Let Us Do Q1 question): the text runs the problems together ("(a): 12 × 17: 11 × 18, 6 × 34"); the meaning of "and" (plus) is only explained in the solution. Suggested: "Each box has one problem on top and problems below it. Here 'and' means plus. In each box find which problems below give the same answer as the one on top." The top cells read 1,001 and 1,999 in the LP but 1001 and 1999 in the book (both fine).
- **M4.S30.T30.C147** (Let Us Think (a) to (c)): the text does not say that the answer boxes all have the same colour. Suggested: "In each problem the boxes of the answer are all orange, so they hold one digit; the black boxes can hold any digits."
- **M4.S30.T30.C151** (g to i): "(h): red, green, purple × purple" and "(i): ... × green" do not say that the multiplier is ONE box. Suggested: "(h): a three-digit number (red, green, purple) times a one-digit number (purple) gives 5,999." and the same for (i) with the multiplier green.
- **M4.S30.T30.C150** (steps for (e)): "the top number is 11 and blue" is garbled. Suggested: "the top number is 11 followed by the blue digit".
- **M4.S30.T30.C152** (steps for (i)): "puzzle (i): has no answer" has a stray colon. Suggested: "so puzzle (i) has no answer."
- **Numbering**: the LP names the concepts of Let Us Think Q1 "Q1", "Q2", "Q3" (parts a to c, d to f, g to i) and the book's Q2 "Q4" (C153/C154); the book has only Q1 (a to i) and Q2. Only the labels are affected (book_number fields are right).
- **M4.S31.T31.C155** (The King's Reward): the LP example (two chests, 3 coins doubling and 1 coin tripling for 4 days) is a smaller invented version; the book's task is three choices over 7 days (5 coins x2, 3 coins x3, 1 coin x5: 640, 6,561 and 78,125 coins). No item in chunk E asks the book's own question; check whether another chunk or the LP covers it.
- **M3.S26.T26.C131** (Asher): the book's total 5,018 does not equal the sum of its own rows (5,008); the LP treats this as one of Asher's errors (also true for Pankaj: 92 + 115 = 207, printed 135). It is read as intended, because the exercise is "find the errors".

## 4. Places where the book is unclear

- **Let Us Think Q1 (i)** (red, green, purple × green = 2,000): no digits fit (checked in code over every three-digit number), so the printed colours are probably a print slip. The question figure keeps them as printed; the solution frame is drawn as printed with the tag "no digits fit".
- **Book answers**: the pdf has no printed solutions; every answer comes from the LP steps. No book print slip changed a value in a figure (decision 1 did not apply): the figures only show given digits and the LP's own sample answers.
- **P16-written_method-5** (Asher): the red crossed-out "1" between the T and O digits of each row is read as a carry that was struck out; its meaning is not explained in the chapter text. It is not drawn (question side `none`).
- **P19-digit_boxes-4** (g): the answer row is wider than the top row and starts left of the first top box; read as one extra place on the left (four answer boxes against three top boxes), as in a vertical multiplication.
- Base inventory descriptions were checked against the page pictures (p.16 to p.19); no correction was needed.
