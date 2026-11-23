# Class 8 Ch 13 Algebra Play - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths8_ch13` v28 (taken from staging). Result: new V2 version v29 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (78 items from 42 units)
{"worked_example": {"none": 6}, "question": {"none": 25, "required": 11}, "solution": {"none": 21, "required": 11, "optional": 4}}

Optional, NOT added: [('C81', 'solution'), ('C89', 'solution'), ('C99', 'solution'), ('C101', 'solution')]

needs_lp_text_sync: []

## The 22 diagrams
| id | side | type |
|---|---|---|
| M2.S5.T5.C25.IMG1 | question | other |
| M2.S5.T5.C26.IMG1 | solution | other |
| M2.S5.T5.C27.IMG1 | question | other |
| M2.S5.T5.C28.IMG1 | solution | other |
| M2.S5.T5.C29.IMG1 | question | other |
| M2.S5.T5.C30.IMG1 | solution | other |
| M2.S5.T5.C31.IMG1 | question | other |
| M2.S5.T5.C32.IMG1 | solution | other |
| M2.S5.T5.C34.IMG1 | solution | other |
| M2.S6.T6.C38.IMG1 | solution | other |
| M2.S6.T6.C39.IMG1 | question | other |
| M2.S6.T6.C42.IMG1 | solution | other |
| M2.S6.T6.C44.IMG1 | solution | other |
| M2.S8.T8.C51.IMG1 | question | cell_grid |
| M2.S8.T8.C52.IMG1 | solution | cell_grid |
| M2.S8.T8.C53.IMG1 | question | cell_grid |
| M2.S8.T8.C54.IMG1 | solution | cell_grid |
| M2.S8.T8.C55.IMG1 | question | cell_grid |
| M2.S8.T8.C56.IMG1 | solution | cell_grid |
| M3.S13.T13.C72.IMG1 | question | flow |
| M3.S13.T13.C74.IMG1 | question | flow |
| M3.S13.T13.C76.IMG1 | question | flow |

### Chunk A notes (from the decision agent)
# Chunk A notes: Class 8 Ch 13 "Algebra Play" (cbse_eng_maths8_ch13_v28)

Units: M1.S2.T2 (1 worked example), M1.S3.T3 (5 pairs, Think of a Number Q1-Q5), M2.S5.T5 (6 pairs, Number Pyramids Q1-Q5 and Figure it Out Q1).
Result: 23 items, required 9, optional 0, none 14, validator errors 0 (2 warnings, explained under "Validator warnings").
Pictures checked: pdf pages 1 to 6 (page_01 to page_06.png). Page 1 has no figure (QR code and chapter art only). All base descriptions of my figures matched the pictures; no CORRECTED entry was needed.

## Decisions at a glance

| Unit / concept | Question | Solution |
|---|---|---|
| M1.S2.T2.C6 worked (change the steps) | none (TEXT_SUFFICIENT) | - |
| T3 Q1 C8/C9, Q2 C10/C11 | none | none (LATEX_ARITHMETIC) |
| T3 Q3 C12/C13, Q4 C14/C15, Q5 C16/C17 (date trick) | none | none (LATEX_ARITHMETIC) |
| T5 Q1 C25/C26 (three pyramids 6 2 / 3 4 3 / 5 4 5 0) | required, C25.IMG1 | required, C26.IMG1 (from C25.IMG1) |
| T5 Q2 C27/C28 (10 / 4 ? / 1 ? ?) | required, C27.IMG1 | required, C28.IMG1 (from C27.IMG1) |
| T5 Q3 C29/C30 (60 / ? ? / 12 ? 8) | required, C29.IMG1 | required, C30.IMG1 (from C29.IMG1) |
| T5 Q4 C31/C32 (three 4-row pyramids) | required, C31.IMG1 | required, C32.IMG1 (from C31.IMG1) |
| T5 Q5 C33/C34 (top from a, b, c) | none | required, C34.IMG1 (stands alone, derived_from null) |
| T5 Q6 C35/C36 (Figure it Out Q1, box rows) | none | none |

Diagram type for all nine: `other` with `layout: number_pyramid` (the catalogue has no pyramid type); every box has its centre coordinates in `content`, so the renderer has nothing to guess. Canvas 16 x 9 units (1 unit = 120 px).

## Borderline

1. **T5 Q1, Q2, Q3, Q4 question diagrams (required).** The LP text carries the bottom rows and where the blanks are, so a careful student could attempt from text. I kept them `required` (ACTION_ON_FIGURE + DATA_IN_FIGURE) because the book question IS the picture (it prints only pyramids with ? or empty boxes, and the student completes them), and because the filled pyramid is the answer (ANSWER_IS_FIGURE) and the four pairs are siblings. Per decision 4 not flipped to none. Q2 (10 / 4 ? / 1 ? ?) is also the book's teaching example and concept image M2.S4.T4.C19.IMG1 covers its steps; the item still draws its own given-state picture (v3: a concept image is never linked).
2. **T5 Q5 (C33 / C34).** Question `none`: the book prints no empty pyramid for this; the figure it prints on page 6 is the finished a + 2b + c pyramid, which is the answer. The question names the bottom row a, b, c in words, and the companion note says not to invent a question figure. Solution `required` (printed answer is a pyramid, B2): ONE diagram holding two pyramids side by side, the letter pyramid (a + 2b + c / a + b, b + c / a, b, c) and the numeric one the LP answer uses (23 / 10 13 / 1 9 4). Given bottom rows in INK, everything the solution adds in ANSWER green. Sibling note: Q1 to Q4 have a question figure, Q5 does not, because the book gives none.
3. **T5 Q6 / Figure it Out Q1 (C35 / C36), both none.** The book draws each case as a plain row of three boxes (4 13 8, 7 11 3, 10 14 25). The answer is one number per case and no pyramid is built, so the boxes carry nothing the text lacks (NUMBER_LIST_IN_BOXES, TEXT_SUFFICIENT; solution LATEX_ARITHMETIC). If the user wants the boxes drawn it is a one-picture addition; I did not add it.
4. **Date trick (C12/C13, C14/C15, C16/C17) and worked C6, all none.** The book shows the date trick only as the Shubham and Mukta comic strip (P02-dialogue_strip-1). I treated it as a procedure plus a number chain (26/01, 1 x 5 = 5, 5 + 6 = 11, 11 x 4 = 44, 44 + 9 = 53, 53 x 5 = 265, 265 + 26 = 291) with characters as decoration, i.e. number chains go to LaTeX (LATEX_ARITHMETIC), not a printed answer picture. If the user reads the strip as a "printed answer is a picture" case, the three solutions (C13, C15, C17) and possibly C12 would turn required with a `flow` style chain; they are the only place where this call could go the other way. C14, C16 follow C12 for sibling consistency. No concept image shows the strip, so no REUSES_CONCEPT_IMAGE.
5. **P05-number_pyramid-6** (the two-row lead-in a + b / a b): mapped `none:TEXT_SUFFICIENT`. No item uses it and no concept image shows exactly it (C23 shows the three-row version).
6. **Question marks versus empty boxes.** The book prints "?" in the unknown boxes of the page-4 pyramids (Q1, Q2, Q3 figures) and leaves them empty on page 5 (Q4 figures). I followed the book per figure.
7. **Letters in the Q3 solution.** The LP steps name the unknown boxes a, b, c, but the figure is not a lettered figure; the solution diagram shows the final numbers (32, 28, 20) only, as the book's filled pyramid does. Decision 3 (figure letters) does not apply to box names.
8. **One picture per side for Q1 and Q4** (brief: at most one question and one solution diagram per pair). Q1 holds the three pyramids in one picture, Q4 the three four-row pyramids (both LP blocks E0 and E1 of C31/C32).
9. **Figure accounting.** Teaching figures keep the base id with `concept_image:` (P03 -> C18, P04 steps -> C19, P05-1 -> C20, P06-1 -> C23). Where an item draws the same figure itself I added a `NEW-` entry for the second use (NEW-P03-number_pyramid-1-q5sol, NEW-P04-number_pyramid_steps-5-final, NEW-P06-number_pyramid-1-q5sol). P04-number_pyramid-4 and P04-number_pyramid-6 are labelled "teaching"/"given in question" in the base; both are the given state of Q2 / Q3, so they map to those question items. The page-4 pyramids 1 to 3 all map to C25 (question), the page-5 pyramids 3 to 5 to C31 (question). I did not claim P06-box_row-5, -6, -7 (Figure it Out Q3): that question is a unit of chunk B.

## Validator warnings (not errors)

C26 and C32 solution diagrams have no inventory figure mapped: the book prints no solution for these two (Q1 and Q4 fill-ups), the LP solution values are drawn. Fine per the validator message.

## LP text issues

- **M1.S3.T3.C12 (Q3), C14 (Q4), C16 (Q5):** the question text says "follows the steps" / "running the trick forward" / "the date trick" but never lists the six steps; in the book they appear only inside the comic strip. A student working the question alone cannot know them. Suggested sentence to add to each: "The steps are: think of a date, multiply the month by 5, add 6, multiply by 4, add 9, multiply by 5, add the day."
- **M2.S5.T5.C25 question_tex:** "bottom rows $6$, $2$ and $3$, $4$, $3$ and $5$, $4$, $5$, $0$" runs the three rows together. Suggested: "Fill three pyramids with bottom rows (i) $6$, $2$ (ii) $3$, $4$, $3$ (iii) $5$, $4$, $5$, $0$." Same grouping problem in **M2.S5.T5.C35** ("4, 13, 8 and 7, 11, 3 and 10, 14, 25"): suggested "(i) $4$, $13$, $8$ (ii) $7$, $11$, $3$ (iii) $10$, $14$, $25$."
- **M2.S5.T5.C27:** "middle row 4 and a blank, and bottom row 1 and two blanks" does not say the blank is to the right of the 4 / 1. Suggested: "the middle row has $4$ on the left and a blank on the right, the bottom row has $1$ on the left and two blanks".
- **M2.S5.T5.C33 question_tex:** "bottom row a, $b$, $c$" has the first letter outside math mode (reads as the article "a"). Suggested: "bottom row $a$, $b$, $c$".
- **M2.S5.T5.C30 steps_tex[3]:** "so $c$ is $20$, a is $32$ and $b$ is $28$": "a" is outside math mode. Suggested: "$a$ is $32$".
- **M2.S5.T5.C32 (extra block, answer_tex):** "First: bottom 5, 14, 7, 2 and top 70. Second: bottom 3, 5, 5, 2 with rows 8, 10, 7 and 18, 17" labels the book's second and third pyramids "First" and "Second", while its own steps call them "Second pyramid" and "Third pyramid". Suggested: "Second pyramid: bottom $5$, $14$, $7$, $2$ and top $70$. Third pyramid: bottom $3$, $5$, $5$, $2$ with rows $8$, $10$, $7$ and $18$, $17$." The old plan also holds two solution cards for this concept (C32.IMG1, C32.IMG2); the new map gives one solution diagram, M2.S5.T5.C32.IMG1, so the builder must not reuse the old C32.IMG2.
- All other LP answers recomputed and agree with the mathematics (pyramid sums, 1390 - 165 = 1225, 1269 - 165 = 1104, 394 - 165 = 229, 296 - 165 = 131, 4 + 26 + 8 = 38, 7 + 22 + 3 = 32, 10 + 28 + 25 = 63, the Q4 values 9, 1 / 14, 2 / 5, 2). No solution contradicts the book.

## Book unclear or inconsistent

- The pdf has no printed solutions; every solution value comes from the LP and was recomputed.
- Page 4 uses "?" for unknown pyramid boxes, page 5 uses empty boxes (see Borderline 6).
- The step picture on page 4 colours found numbers blue (6, 3) and red (the last 3); the Q2 solution diagram uses ANSWER green for all new numbers, as the v3 style demands.
- The page-6 pyramid has wider bottom boxes than the earlier pyramids (it must hold a + 2b + c); in the Q5 solution figure both pyramids use the same wide boxes (2.4 x 1.3 units) so the letter and number pyramids match.

### Chunk B notes (from the decision agent)
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

### Chunk C notes (from the decision agent)
# Chunk C notes: Class 8 Ch 13 "Algebra Play" (units 30 to 42, topics T14 to T17)

Result: required 0 / optional 4 / none 19 (23 items: 10 question, 10 solution, 3 worked example). Validator: errors 0, warnings 0.

I looked at page_10 to page_13 as pictures. Pages 11, 12, 13 hold no figure that carries data: page 11 is text and algebra only, page 12 has one decorative farm illustration, page 13 has one decorative Karim and genie illustration. The base inventory has no entry from pages 11 to 13 (its last entry is the page 10 comic strip), so none of the inventory agents' `unclear` doubts belong to this chunk. I checked the page 10 comic strip entry (P10-dialogue_strip-3) against the picture: it is correct.

## Why nothing is required

Every item here is a word problem or an algebra argument. The book gives no figure for any question, and no answer in the LP is a picture, arrangement or drawing. None of the Step B triggers applies, and for each item a careful student loses nothing without a picture (tie-breaker). Question sides are all `none` because a question with no given figure gets no question diagram. Worked examples (C84, C85, C86) are `none` for the same reason: their figure would sit after the question text and so could show only what the question gives, which is nothing visual; their teaching images (C84.IMG1, C85.IMG1, C86.IMG1) stay and are never linked.

## 1. Judgement calls

- **C78 question (book Q2, "In the trick given above ...")** : `none`, TEXT_SUFFICIENT. It points at Mukta's comic strip on page 10, but states the change itself (sum instead of difference) and gives three numeric examples. The earlier author's hint (`q_figure`: "Mukta's trick as four speech bubbles") would make the figure a given, but the question can be attempted without it and the strip is a teaching picture of section 6.6 (the base id belongs to the teaching units of that section). I recorded this second use as `NEW-P10-dialogue_strip-3-C78` (none, TEXT_SUFFICIENT) so that it is accounted for whatever the chunk that holds the base id decides. If the user wants the trick on screen for this question, it would be a question figure of the four speech bubbles with the steps only (no 47 example, since the question does not give it).
- **C81 solution (cyclic sum 111(a + b + c))** : `optional`. A 3 x 3 cyclic table (rows abc, bca, cab, column totals a + b + c) would show "each digit appears once in every place" at a glance. Step 2 says it in words and the sum is in LaTeX, so it is not needed. Not added.
- **C89 solution (shrines) and C101 solution (Karim)** : both `optional`, same decision on purpose (same structure: double, pay, repeat, with the numeric check 7, 14, 6, 12, 4, 8). A strip of ponds/shrines or of three trips round the tree with the coin counts would help, but the LP solution already gives all the numbers as algebra plus a one-line check. Not added. The book prints no figure for the shrines (C88), so there is no question figure for either.
- **C99 solution (fractions 1/3, 4/12, 9/27)** : `optional`. A 6 x 6 dot square in nested L-shapes (1, 3, 5, 7, 9, 11) would show that 7 + 9 + 11 = 27 is three times 1 + 3 + 5 = 9. The LP gives n x n and 4 x n x n in LaTeX. Not added.
- **C79, C83, C91, C93, C95, C97 solutions** : `none` (LATEX_ARITHMETIC). A picture would be at most decoration for equation solving (hens and horses, ages, cows, dosa profit). C91 (all hens, extra legs) could be drawn but the arithmetic 55 x 2 = 110, 150 - 110 = 40, 40 / 2 = 20 is complete.
- **C90 and C100 questions** : `none`. Their book illustrations (page 12 farm, page 13 Karim and genie) are decorative and carry no data; recorded as `NEW-P12-farm-illustration` and `NEW-P13-karim-genie-banyan` (none, DECORATIVE_ONLY) because the base inventory skipped them.

## Borderline

- C81, C89, C99, C101 solutions: optional rather than none (a figure would clearly make the idea visible; the text is already complete). They cost nothing either way because optional is not added.
- C91 solution: none, although the all-hens argument could be drawn as 55 animals with 2 legs each and 20 horses with 2 extra legs. I judged it plain arithmetic.
- C78 question: none, although the question refers to the trick "given above".
- C85 worked example (double and give 5 away, twice): none, while C89 and C101 (same process) are optional on the solution side. The difference is the side: a worked-example figure goes after the question, where nothing visual is given; a solution figure shows the complete final state.

## 2. LP text issues

- **M3.S14.T14.C78** (question and solution): the card names and `book_number` say "Figure it Out, Q1" but the text is book Q2 (the sum of the number and its reverse). Chunk B's C76 already carries book Q1. The same shift applies to C80 (book Q3, labelled Q2) and C82 (book Q4, labelled Q3). The `ncert_refs` (FiOC.q2, q3, q4) are right. Suggested labels: "Figure it Out, Q2", "Q3", "Q4".
- **M3.S17.T17.C90, C92, C94, C96, C98, C100**: labelled "Figure it Out, Q1" to "Q6" but they are book Q6 to Q11 (`ncert_refs` FiOC.q6 to q11 are right). Suggested labels: "Figure it Out, Q6" to "Q11".
- **M3.S14.T14.C78** question: says "In the trick given above" without stating the trick. Missing data for a standalone card. Suggested sentence to add before the question: "Mukta's trick: choose a 2 digit number with different digits, reverse the digits, find the difference of the two numbers, then divide by 9."
- **M3.S16.T16.C88** `answer_tex`: the closing bracket sits inside the maths: "(or any multiple, like $14$ and $16)$". Suggested: "(or any multiple, like $14$ and $16$)".
- **M3.S17.T17.C94** `question_tex`: the pronoun is typeset as maths: "if $I$ gave you". Suggested plain "if I gave you".
- **M3.S17.T17.C96** `question_tex`: "$I$ run a small dosa cart" and "how many dosas should $I$ aim to sell" have the pronoun as maths; "(i):" and "(ii):" have a stray colon that the plain `question` field does not have. Suggested plain "I", and "(i)", "(ii)".
- **M3.S17.T17.C100/C101**: the LP question does not repeat that the genie asks 8 coins per round until the sentence "gives the genie 8 coins"; this is fine. In part (ii) of the solution, "fewer than 7" holds only for the start of 7 coins, while the question asks in general; the sentence already says "here". No change needed.
- All arithmetic in the LP solutions of this chunk was re-checked and holds: 111 = 3 x 37, 123 + 231 + 312 = 666 = 37 x 18 = 3 x 222; 254254 / 7 = 36322, / 11 = 3302, / 13 = 254; t = 6 (14 bicycles); x = 7 stickers; p = 15; x = 7, k = 8 flowers (7, 14, 6, 12, 4, 8); h = 20 horses, 35 hens; d = 6; g = 6, Naina 12; p = 80 and n = 175; 4/12 and 9/27 are one third; Karim 7 coins, 8x - 7c.

## 3. Where the book is unclear

- Nothing in this chunk's pages is unclear or contradicts the LP. The book's Q5 (shrines) lists only the story; the LP's smallest answer 7 flowers and 8 per shrine is the minimum whole-number solution of 8x = 7k and the LP also states that any multiple works, which is mathematically right.
- The book's picture for Q6 (page 12) shows only a handful of horse heads and two hens, not 55 animals, which confirms it is illustration rather than data.
