# Notes, chunk B (Class 8 Ch 13 "Algebra Play", LP cbse_eng_maths8_ch13_v28)

Units 13 to 29 (topics M2.S6.T6, M2.S7.T7, M2.S8.T8, M3.S10.T10, M3.S11.T11, M3.S12.T12, M3.S13.T13): 32 items.
Result: required 10 (4 question, 6 solution), optional 0, none 22. Validator: errors 0 (5 warnings, all expected: four required
solution figures that the book never prints, and one long visible_text that is an expression).

Required diagrams: C39 Q (three rows of boxes), C38 S, C42 S, C44 S (number pyramids), C51 Q and C52 S (calendar page),
C53 Q and C54 S (shape grid), C55 Q and C56 S (two shape grids).

## 1. Judgement calls

- **Figure ownership.** I claimed every base figure of book sections 6.4, 6.5, 6.6, plus on page 6 the three box rows of Figure it Out Q3
  (P06-box_row-5, -6, -7, used by my C39) and the teaching pyramid P06-number_pyramid-1 (mapped to the existing concept image
  M2.S4.T4.C23.IMG1; chunk A may claim it too, same meaning). Box rows -2, -3, -4 (book Q1, LP C35) and all of pages 2 to 5 are left to chunk A.
- **C39 question (box rows of Figure it Out Q3): required.** The book prints the three bottom rows as boxes, the LP text also lists the numbers.
  Kept required under decision 4. The three rows are stacked (book: side by side) so the 16:9 card is used; order and values unchanged.
  One diagram carries all three cases (a pair gets one question diagram).
- **C38 solution (4-row pyramid of letters), C44 solution (4-row Virahanka-Fibonacci pyramid, part i): required** by the B2 rule "answer is a filled
  figure even if the steps describe it in words". The LP steps build the whole pyramid row by row in words. No question diagram exists (the book
  gives none), so both solution figures stand alone (`derived_from: null`) and show the complete final pyramid; the bottom row (given in the
  question text) is INK, everything above is ANSWER. Part (ii) of C44 (29 rows) cannot be drawn and stays text.
- **C42 solution (3-row pyramid 1, 2, 3 / 3, 5 / 8): required**, clear case (question says "fill in the rest of the pyramid").
- **Siblings in the pyramid set.** C40 (formula on three number rows) and C46 (general n) have no pyramid in their answer, so none; C38, C42, C44 do, so required.
  C37, C41, C43, C45 questions: the book gives no figure, so none.
- **C51 question (August 2025 calendar page): required** (FIG_REFERENCED + DATA_IN_FIGURE). The book gives the calendar page and the block
  6, 7, 13, 14 as a separate 2 x 2 grid beside it, nothing highlighted on the calendar. I reproduced exactly that and left out the book's
  "= 40" (it is the answer to the check). The earlier author's q_figure hint (block marked on the calendar) does not match the book.
- **C52 solution:** same calendar and grid (same positions), plus the answer block 5, 6, 12, 13 (MARK_FILL + ANSWER outline), the checked block
  6, 7, 13, 14 with a dashed FOCUS outline, the book's "= 40" and the answer grid 5, 6 / 12, 13 with "= 36" (the book prints that grid as the answer).
  The two outlines overlap on 6 and 13; no number sits on an outline.
- **C53/C54 and C55/C56 (algebra grids): all four required, one picture per side.** The question figure is what the book prints (shapes and
  empty cells); the solution adds the numbers in the empty cells and a key line "shape = value" (green) under each grid. C55/C56 hold both grids side by side
  in one picture, as in the book (the old LP had two answer cards; the new build has one figure for the pair). The values of the shapes are shown
  as a key, not written into the shapes, so the question grid stays untouched.
- **Shape colours.** The book draws circles red in the first grid and blue in the second, diamonds purple. Style tokens only: square SET_A, circle SET_B
  (one colour for a circle in both grids), diamond FOCUS. The shape still tells the figures apart without colour. No red token exists (WRONG is reserved).
- **Digit boxes (C60, C64, C66 questions; C61, C65, C67 solutions): none, LATEX_ARITHMETIC.** The three empty boxes printed inline (two boxes, times, one box) only mean
  "two digit number times a one digit number", which the LP text already says; the answer 32 x 5 = 160 is arithmetic. `text_alternative` gives the inline
  LaTeX for the blanks. C62/C63 (letter digits proof): none.
- **Mukta's trick (C72, C74, C76 questions): none, REUSES_CONCEPT_IMAGE.** The book's comic strip is the four-step procedure worked on 47; that procedure is already the teaching
  image M3.S12.T12.C68.IMG1 (the comic's characters are decoration). I applied the procedure flow-chart rule: none, no link, no new diagram. Solutions C73, C75, C77: none (arithmetic and algebra lines).
- **C48 worked example (three dates in a column): none.** No figure is given; the working is three algebra lines. The book's Math Talk calendars
  (P08-calendar-1, P08-number_grid-2) are mapped `none:OPEN_ENDED` (open invitation, different shapes from the LP example).
- **C70 worked example (352 and 253, 99): none**, algebra lines; the place-value picture is a teaching image and is never linked.
- Colour of an added top-box outline: the top box of each pyramid has an ANSWER 6 px outline (no fill) so the expression or number the question asks for stands out
  and the green numbers stay legible on white.
- Pyramid and grid coordinates are given in a 1920 x 1080 canvas (y down) in each `manim_description`; every box is positioned over the join of the two boxes below it.

## 2. LP text issues

(Not edited and decisions unchanged, as instructed.)

- **M2.S6.T6.C37, C39, C41, C43, C45 and their answers:** the LP calls them "Figure it Out, Q1" to "Q5", the book numbers are Q2 to Q6. The book's Q1 sits in
  chunk A's C35 labelled "Number Pyramids, Q1", so the LP's "Q1" appears to be reused (C35 and C37 are different questions). Suggest relabelling C37 to C45 as "Figure it Out, Q2" to "Q6".
- **M2.S6.T6.C38 steps_tex step 1:** "Bottom row a, $b$, $c$, $d$." the first letter is outside the maths. Suggest "Bottom row $a$, $b$, $c$, $d$."
- **M2.S6.T6.C46 steps_tex and answer_tex:** "$(2n - 1)th$" puts th inside the maths while C44 uses \text{th}. Suggest "$(2n - 1)\text{th}$" (three places in C46 text, steps, answer).
- **M2.S8.T8.C51 (question):** the question never says which calendar page. Suggest adding "the August 2025 calendar page" (the check block 6, 7, 13, 14 only makes sense on that page).
  Also C52 steps_tex: "Write the block as a, $a + 1$ ..." and "a is $5$" have unwrapped letters; suggest "$a$".
- **M2.S8.T8.C53 (question):** says "three squares make 27 and two circles with a square make 19" but not that each row's last box is the sum of the shapes to its left.
  Suggest: "In a grid, the last box of each row is the sum of the shapes to its left. Row 1 is three squares and ends in 27; row 2 is two circles and a square and ends in 19. Find the square and the circle."
- **M2.S8.T8.C55 (question):** "the last row is blank under every column" and "make a blank" are unclear, and the rule for the bottom row (each box is the sum of the column above it; the corner is the total)
  appears only in the answer (C56 step 6). Suggest: "In each grid the last box of a row is the sum of the shapes to its left; in the last row of Grid 2 each box is the sum of the column above it, and the corner box is the total." and "make an empty box" for "make a blank".
- **M2.S8.T8.C48 (worked example):** "a calendar page" without a month; optional "for example the August 2025 page" so 10, 17, 24 are visibly valid dates.
- **M3.S13.T13.C72, C74, C76 (questions):** all say "Mukta's trick" or "the trick given above" but the LP question text never states the four steps (they are only in the book's comic and in the teaching content of M3.S12.T12.C68).
  Suggest adding: "Mukta's trick: choose a 2-digit number with different digits, reverse the digits, find the difference of the two numbers, divide it by 9."
- **M3.S13.T13.C74 question_tex and C73 steps:** "when a $> b$" and "with $b$ larger than a" have unwrapped letters; suggest "$a > b$" and "larger than $a$".
- C44 step 4 and C46 are mathematically right (place 1 + 2 x 28 = 57; place 2n - 1; n = 3 gives the 5th term 8, n = 4 gives the 7th term 21).
  All other numbers in this chunk were recomputed and match the LP (141, 124, 56; 36 and block 5, 6, 12, 13; sum 40; squares 9 and 5; 11 and 5; 4 and 7 with sums 18, 15, 15, 48; 160; 217; 477; 512 against 504; 27 / 9 = 3; 45 / 9 = 5).

## 3. Borderline

- C39 question required although the LP text lists all numbers (decision 4). The same logic makes C53 and C55 questions required (their shapes live only in the picture) and C51 required.
- C38 and C44 solutions required on the strength of the "filled figure described in words" rule, although the answer asked for is an expression (C38) or a statement (C44).
  If the rule is read as "the answer itself must be a picture", both would be none; C42 stays required either way.
- C54 solution required: the printed answer in the book is a picture (shape equations); the figure adds only the two values as a key. It is the thinnest of the required solutions.
- C60, C61, C64, C65, C66, C67: none although the book prints boxes; read as an inline blank in an expression (LATEX_ARITHMETIC), not a data figure.
- C72, C74, C76 questions: none under the procedure-picture rule; the text "Follow Mukta's trick" is also a FIG_REFERENCED-style pointer. If these should be drawn, one spec (the four steps worked on 47) fits all three.
- C48 worked example: none; a calendar with 10, 17, 24 marked would help but a teaching image of exactly that already exists (M2.S7.T7.C48.IMG1) and is never linked.
- C40 solution: none, no new visual.

## 4. Where the book itself is unclear

- Second grid on p.142 (C55): the picture does not say what the empty bottom row holds (numbers or shapes). The LP solution settles it as column sums with the total in the corner
  (4 + 7 + 7 = 18, 7 + 4 + 4 = 15, 7 + 4 + 4 = 15, total 48); the figure leaves those cells empty in the question and fills them with those numbers in the answer.
- Colour of the circle changes between the two grids (red, then blue); shape size and meaning are unchanged, only colour, so I used one colour per shape.
- The book has no printed solutions, so there is no printed answer figure to check for C38, C42, C44 and C56; those figures follow the LP solution text.
- No book print slip was found in the figures of this chunk (checked: box rows, calendar, 2 x 2 grids, shape grids, digit boxes, comic strip), so no corrected values were needed.
- Base descriptions all matched the page pictures; none needed a CORRECTED note.
