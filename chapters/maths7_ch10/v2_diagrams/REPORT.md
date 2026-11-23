# Class 7 Ch 10 Operations with Integers - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths7_ch10` v69 (taken from staging). Result: new V2 version v70 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (115 items from 75 units)
{"question": {"none": 37, "required": 3}, "solution": {"none": 34, "optional": 4, "required": 2}, "worked_example": {"none": 27, "required": 7, "optional": 1}}

Optional, NOT added: [('C14', 'solution'), ('C32', 'worked_example'), ('C37', 'solution'), ('C120', 'solution'), ('C122', 'solution')]

needs_lp_text_sync: []

## The 12 diagrams
| id | side | type |
|---|---|---|
| M1.S7.T7.C17.IMG1 | question | number_line |
| M2.S10.T10.C30.IMG2 | worked example | integer_tokens |
| M3.S20.T20.C70.IMG2 | worked example | cell_grid |
| M3.S20.T20.C71.IMG2 | worked example | cell_grid |
| M3.S20.T20.C72.IMG1 | worked example | cell_grid |
| M3.S21.T21.C73.IMG1 | question | cell_grid |
| M3.S21.T21.C74.IMG1 | solution | cell_grid |
| M5.S28.T28.C100.IMG2 | worked example | integer_tokens |
| M5.S29.T29.C105.IMG1 | solution | integer_tokens |
| M5.S31.T31.C112.IMG2 | worked example | arrow_map |
| M5.S31.T31.C113.IMG2 | worked example | arrow_map |
| M5.S33.T33.C119.IMG1 | question | arrow_map |

### Chunk A notes (from the decision agent)
# Notes, chunk A (topics M1.S3.T3 to M2.S11.T11), Class 7 Ch 10 Operations with Integers

Result: 29 items = required 2, optional 2, none 25. Validator (`--chunk A`): errors 0, warnings 0. 20 base figures claimed (6 to items, 10 to concept images, 4 none).

Required: `M1.S7.T7.C17.IMG1` (Try This question, three number lines) and `M2.S10.T10.C30.IMG2` (Math Talk token sets, worked example question side).
Optional (not added): `M1.S6.T6.C14` solution, `M2.S10.T10.C32` worked example.

## 1. Judgement calls

1. **Try This (C17/C18), question REQUIRED, solution none.** The question says "from the figures below" and the three figures (a and b arcs from 0, final position P) are the book's given data. The pair gets ONE question diagram, so the three figures are drawn as three stacked strips in one 16:9 card (strips divided by thin GUIDE lines). The figure numbers 1, 2, 3 are NOT drawn (v3: no figure letters/numbers); strips are told apart by top-to-bottom order, which is the order of "Figure 1/2/3" in the LP text. No scale is drawn (the book prints none). The solution only states the conclusion per figure and adds no mark, so `none` with `SAME_AS_QUESTION_DIAGRAM`. Caveat: the LP question text already paraphrases each figure in words, so a text-only reading is possible; I chose required because the book question is about the pictures. If you prefer text only, flip C17 to `none` (the spec is complete in out_A.json).
2. **Math Talk token sets (worked example C30), REQUIRED.** The book gives the sets (a), (b), (c) only as pictures ("the following tokens"), listed in the base inventory as "given in question". v3 draws a lettered/given figure even when a teaching image shows it. This is the one borderline call: concept image `M2.S10.T10.C30.IMG1` sits in the SAME concept and shows the same three sets (plus the value -2 and ringed zero pairs), so the learner will see two pictures of the same sets in that concept. The new figure shows only the given tokens (no value, no rings, no part letters). If you judge this a duplicate, flip C30 to `none` (`TEXT_SUFFICIENT`). Token colours (#6CC24A green, #E8643C red) are not in the style table (it has no green/red token colours); the + and - signs inside the tokens keep them readable without colour. Its media id is IMG2 because IMG1 is the kept concept image.
3. **Teaching-narrative worked examples are all `none`** (C8, C9, C10, C11, C19, C20, C21, C22, C26, C27, C28, C29, C31): their questions are complete in words or symbols, and their book pictures are teaching figures, which the plan already holds as the 18 concept images (C8.IMG1, C10.IMG1, C19.IMG1, C26.IMG1, C28.IMG1, with C20.IMG1 for the 4 - (-12) rows). The prompt (section 2) says teaching figures are not this job. The base figures are accounted as `concept_image:...` (accounting only, nothing linked). Where the neighbouring concept's teaching image is the one that shows the picture (C9, C21, C27, C29) the reason says so.
4. **C26 "Find 4 x 2 with the bag" is `none`** although the book asks "Suppose we put some positive tokens into an empty bag as shown in the figure. How many positives are in the bag now?". The LP restates it as 4 x 2 in symbols (all data in text) and C26.IMG1, in the same concept, shows the four bags. Sibling consistency: C26 to C29 all `none` for the same reason.
5. **C32 (-4 x 2 by adding tokens) is `optional`, not `none`.** The book's picture (8 reds in 4 rows of 2, next to "(-4) x 2") is not in any concept image, so a learner sees no token picture for this example. It would help but the text is complete, so it is not added. This is why C32 differs from C27/C29 (their pictures are shown by C26.IMG1/C28.IMG1).
6. **M1.S6.T6.C14 (Example 1 solution) is `optional`.** One number line with an arc from -4 to 5 labelled 9 would help, but the answer is complete in words and arithmetic and the book draws none. Example 2 (C16) stays `none` (`LATEX_ARITHMETIC`, five pairs of -1).
7. **Rakesh's puzzle (C4/C5) and FiO 2.1 Q1 (C6/C7):** P01-table-1 is a plain table of numbers with no colour meaning, so `none:LATEX_TABLE`; `text_alternative` gives the LaTeX array for C5 (and the 7, 18, 25, -11 row for the second block) and a six-row table for C7. Their questions give no figure.
8. **P03-number_line-1** (coin at 0 with a left and a right arrow) mapped `none:DECORATIVE_ONLY`: it carries no number. **P05-token_key-1** (inline green/red icons) mapped `none:TEXT_SUFFICIENT`.
9. Merge note: P08-token_set-1/2/3 are claimed here for `item:M2.S10.T10.C30 (question)`. Chunk B's FiO 2.2 Q3 ("Try to frame a simple rule...") sits on the same page but does not use these sets; if chunk B also claims them, the meaning must match (item C30) or be a concept-image/none mapping, not a second diagram.

## 2. Things in the LP that look wrong or inconsistent

- **Try This (C17/C18) letter a not in math mode.** In `question_tex` the first letter a is plain ("jump a goes right", three times) while b is `$b$`; in the solution `steps_tex` and `answer_tex` the same happens ("a is positive", "jump a is longer", "a right", "a left"). Should be `$a$` everywhere.
- **Numbering differs from the book** (the LP numbers are its own): M1.S3.T3 "Example 1" is Rakesh's puzzle (not a numbered example in the book, p.1-2); M1.S6.T6 "Example 1" and "Example 2" are the two numbered questions after the carrom model (p.3-4); M2.S11.T11 "Example 1" is the inline question "Similarly find the values of 4 x (-6) and 9 x (-7)" (p.6), not an NCERT example; M1.S9.T9 "Figure it Out, Q1" is end-of-chapter Q4 (pdf page 19, book p.42); M1.S4.T4 "Figure it Out 2.1, Q1" is the unnumbered Figure it Out on pdf page 2.
- **Concept image C20.IMG1 sits in the wrong concept.** It shows 4 - (-12) = 4 + 12 (labels "put in 12 zero pairs, remove 12 reds"...), which is the example of C21; C20's own example is 7 - 18 = 7 + (-18), whose token rows are in C19.IMG1. Consider moving C20.IMG1 to C21 or retitling it.
- **C26 question text drops what the book asks** ("How many positives are in the bag now?" with the bag figure); it is restated as "Find 4 x 2 with the bag." (acceptable, noted only).
- All LP solution arithmetic in this chunk was recomputed and agrees with the book: 18 and 7 (sum 25, difference 11) and 7 and 18 (-11); FiO 2.1 Q1 (a) 18, 9 (b) 8, -4 (c) 5, -5 (d) -5, 5 (e) -4, -3 (f) -10, 3; -4 + 9 = 5; 1, -2, ..., -10 ends at -5; 11 zero pairs for (+7) - (+18) = -11; 4 - (-12) = 16; 4 x 2 = 8, 4 x (-2) = -8, (-4) x 2 = -8, (-4) x (-2) = 8; the three sets each give -8 (8 reds; 16 reds and 8 greens; 24 reds and 16 greens); 5 x 4 with 5 greens and 1 red gives 25 greens, 5 reds, 20 left; 4 x (-6) = -24, 9 x (-7) = -63; end Q4 answer 4. No contradiction between the LP and the book was found.

## 3. Places where the book itself is unclear

- **Try This figures (p.4) have no scale.** The proportions in the diagram are measured from the page picture: figure 1 a : b : |P| is about 135 : 204 : 69 px, that is 2 : 3 : 1 (a right, b left and longer, P left of 0); figure 2 about 162 : 92 : 70 px, that is 7 : 4 : 3 (a right, b left and shorter, P right of 0); figure 3 a and b of equal span, P = 0. The spec uses these as drawing proportions only and prints no number.
- **P02-number_line-2 (p.2)** has no scale either (b is drawn longer than a); only the symbols a, b, P matter. **P02-number_line-1 (p.2)** shows the coin over 4 with an arrow from 4 to 7 while the text starts "To begin with, the coin is at point 0": the picture shows the situation after the first strike.
- The book gives **no figure for the two Math Talk statements** (7 - 18 = 7 + (-18) and 4 - (-12) = 4 + 12); all the token rows for them come from the concept images (made by the earlier author, not from the book).
- Base-inventory descriptions P01 to P09 were checked against the page pictures (pages 1 to 9): all correct, no CORRECTED entry needed. In the P08 sets the top-row reds sit exactly over the greens (zero pairs by alignment, not outlined), which the C30 spec keeps.

### Chunk B notes (from the decision agent)
# Chunk B notes: Class 7 Ch 10 "Operations with Integers" (plan cbse_eng_maths7_ch10_v69)

Chunk B = topics M2.S12.T12, M2.S13.T13, M2.S14.T14, M2.S15.T15, M3.S17.T17, M3.S18.T18, M3.S19.T19, M3.S20.T20
(12 pairs + 8 worked examples = 32 items). Result: required 3 / optional 1 / none 28.

Required: the three worked examples of the Magic Grid (M3.S20.T20.C70, C71, C72). Optional: the solution of T12 Q1 (token method).
Everything else is text/LaTeX. The validator prints one warning (C72, see 1.4): that is expected.

## 1. Judgement calls I was unsure about

1.1 **M2.S12.T12.C37 (solution of Figure it Out 2.2 Q1, "using the token interpretation")**: `optional`, not `required`.
The answer is four numbers (-6, 10, 4, -21) and the LP steps narrate every token move in words. A token-bag picture of the four
parts (3 bags of 2 reds; 5 bags ending with 2 greens each; 4 bags ending with 1 green each; 7 bags of 3 reds each) would help,
and the old solution card even planned one, but under the brief ("typical pair: numeric answer -> S none/optional") it is not needed.
Teaching images C26 and C28 of the token-bag topic already show the method. If the user wants a token picture here, flip it to
`required` (one solution diagram for all four parts, 4 rows of bags; no question diagram because the book gives none).

1.2 **M3.S20.T20.C70 (Magic Grid, the book's example): `required`**, one picture = the grid in its final state
(circles on -6, 14, 20, 18; lines through rows 1, 2, 4 and columns 4, 2, 1; cell 18 on no line). Reasons: DATA_IN_FIGURE (the grid
numbers are not in the question; "-6" occurs twice in the grid), ACTION_ON_FIGURE (steps strike rows and columns), HIGHLIGHT_MEANING
(circles). I did not copy the four-round strip because (a) the teaching image C70.IMG1 of the same concept already is that strip
and (b) the book's own four rounds are identical in print for Rounds 1-3, so the final state IS the book picture (see 3.1).

1.3 **M3.S20.T20.C71 ("Why is the product always -30240? Build the grid from its row and column numbers"): `required`, borderline.**
The figure is a headed multiplication table (row numbers 2, -7, 3, 5; column numbers 4, -2, 6, -3; the 16 book numbers as products;
cells 8 and 14 boxed because the steps use 2 x 4 = 8 and (-7) x (-2) = 14). A careful reviewer could say "plain table -> LaTeX"
(LATEX_TABLE) and make it `optional`; I drew it because the book prints this grid as a figure, the question text contains none of
its numbers, and "build the grid" asks for the grid. Teaching image C71.IMG1 (same table, -42 ringed) is not linked.

1.4 **M3.S20.T20.C72 ("Can you make more such grids?"): `required`.** Open question, but the LP gives one concrete sample grid
(rows 1, -2, 3, -1 by columns 2, 5, -1, 4) row by row in words; B2 says words that describe a filled figure do not replace it and
section 5 rule 4 says to draw the LP's sample answer. Same layout as C71 on purpose. The grid is the LP's own sample, not a book
figure, so no base figure maps to it (validator warning is expected). Product check: 1 x (-2) x 3 x (-1) = 6; 2 x 5 x (-1) x 4 = -40; 6 x (-40) = -240 (LP agrees).

1.5 **M3.S17.T17 Example 2 (mine elevator), both sides `none`.** The book's mine-shaft picture only sets the scene: its levels
(+180 ... -175 m) are never used by the question (3 m/min, one hour or 45 min, start 0 or 15 m), so it is not needed to attempt it.
The solution only states -180 and -120 as numbers and in words. The same scene, with both descents drawn, is the teaching image
M3.S16.T16.C56.IMG1, so the figure is accounted for as `concept_image:` (nothing linked). The old cards planned a vertical line
for question and solution; I judged them "nicer", not needed.

1.6 **M2.S13.T13.C42 and C43 (patterns below zero), `none`.** The book draws the ladders with -3 / +3 arrows, but the LP question
already lists the five given equations in text and the answer is three numbers continuing the list, so a student loses nothing
(tie-breaker). The ladders are the teaching images C42.IMG1 and C43.IMG1 (never linked). Not a "refer picture" case: nothing in the
question points at the figure.

1.7 **C45 (use the times 3 tables) and C47 (swap table), `none`.** Both book tables are plain tables of equations with no colour or
marks (LATEX_TABLE). C45 only needs 7 x 3 = 21 and the sign rule; C47's three blanks are written in the LP question and the facts
it needs (30 x 12 = 360, 14 x -5 = -70) are in the steps. `text_alternative` says how to write the tables if the user wants them.

1.8 **T15 Figure it Out Q12 (arrange in increasing order), solution `none`.** The answer is an ordered list of six numbers,
written as one chain of inequalities. A number line cannot be to scale (-370272 ... 370272 with -1412, 716, 1412 near 0), so it would
add nothing. The old card hint ("six values on a number line") was not followed.

1.9 **Sibling consistency.** Within Figure it Out 2.2 (T12): Q1 solution optional (token method), Q2 and Q3 none (numeric / verbal
answers, different kind). All word problems (T17 Example 1, T18, T19) are none on both sides (numeric answers, nothing printed in the book).

1.10 **Figures I did not claim.** The token sets (a), (b), (c) printed under T12 Q3 (P08-token_set-1..3) are the Math Talk
"Consider the numbers represented by the following tokens" and belong to chunk A (worked example M2.S10.T10.C30, teaching image C30.IMG1);
the old Q3 card hint that attaches them to Q3 is wrong. P09-token_grid-1 ((-4) x 2 block of reds) belongs to M2.S10.T10 (chunk A) as well.

1.11 **Inventory mapping choices.** P14-number_grid-1 (blank given grid) and P14-number_grid-3 (the four-round example) both map to
the C70 item; P15-number_grid-1 maps to the C71 item. Ladders map to concept images C42.IMG1 / C43.IMG1; the mine shaft to C56.IMG1;
the times-3 table and the swap table to `none:LATEX_TABLE`; the three-box procedure flow chart (P14-flowchart-2) to `none:TEXT_SUFFICIENT`
(the three steps are written in words in the LP text of C70; no concept image holds the flow chart).

## 2. Things in the LP that look wrong or thin

2.1 **Book numbers repeat or differ from the book.** T12 C36/C37 are labelled "Figure it Out 2.2, Q1" and so are T14 C49/C50 (the book's
second Figure it Out box, p.10-11, is a single unnumbered question "Find the following products"). T18 C62-C65 are labelled Q1/Q2 but the
`ncert_refs` and the book say Q2 (freezing) and Q3 (cement) on p.16. T15 is labelled Q1/Q2 (book end-of-chapter Q3 and Q12) and T19
Q1/Q2 (book Q6 and Q8). The LP's own numbering restarts per set; nothing breaks, but anything keyed on `book_number` should use `ncert_refs`.

2.2 **T19 C68 question_tex has a stray math span:** `Imagine you'$re$ in a place ...` should read "you're" (it renders "re" in math italics).

2.3 **T17 Example 1 extra question** ("What are the maximum and the minimum possible marks?") does not say that the exam has 50
questions; the solution uses "all 50 answers". The book gives the 50 in the Example 1 statement. Suggest adding "The exam has 50 questions."

2.4 **T17 Example 2** question text omits the setting the book gives (elevator in a mining shaft; positions above the ground positive,
below negative), and the extra items "(a) The same question by Method 2." / "(b) The same question by Method 2." are not standalone.

2.5 **T19 C67 (b)** answers "yes, 5 unanswered (in the 25 question test of (a))": it assumes (b) is the same 25-question test, which the
book does not say. Not a contradiction, but an assumption the student is not told in the question.

2.6 **T20 C70 question** says "circle -6, then 14, then 20, then 18" without positions; -6 appears at row 1 column 4 and row 3 column 2.
Only the steps (and now the figure) say row 1, column 4. Suggest "(row 1, column 4)" in the question text.

2.7 **T20 C72 steps** use "row 1 is 2, 5, -1, 4; Row 2 is -4, ...; row 3 ...; row 4 ..." for the grid lines, while "row numbers" earlier
means the multipliers 1, -2, 3, -1: "row 2" can be read as the row number -2. Suggest "the first row", "the second row", ...

2.8 All sums and products in the LP solutions of this chunk were recomputed and agree with the book/arithmetic: 123 x 456 = 56088;
348 x 1064 = 370272; 348 x 964 = 335472 and the ordering e, a, b, c, f, d; 150 + (-40) = 110; 60 x 3 = 180; 15 - 135 = -120; 32 + 10 x (-5) = -18;
24000 + (-25000) = -1000 and 32000 / 8 = 4000; 15 x 4 = 60 with 10 wrong and 25 questions, 5 x 4 = 20 with 15 wrong; 8 + 4 x (-5) = -12;
(-6) x 14 x 20 x 18 = -30240; (-210) x 144 = -30240.

## 3. Places where the book itself is unclear

3.1 **Magic Grid example (p.14).** The four-round figure does not show the game step by step: Rounds 1, 2 and 3 are printed identically
(all three circles and all six lines already drawn); Round 4 differs only by the circle on 18. I checked the page picture: the base note is right.
Hence C70 draws the one final state.

3.2 **p.15 "Play the same game with the grid below"** prints exactly the same 16 numbers as the p.14 grid (the LP teaching plan of C71 says so too);
the book gives no new grid.

3.3 **Mine shaft (p.13).** The levels are only roughly to scale, and the answer -180 m lies below the deepest labelled level (-175 m); the
elevator car is drawn at about the -125 m level. The picture is scenery here, so nothing in this chunk depends on it.

3.4 The flow chart on p.14 prints "coloumn" (book typo); not used. Tables and patterns print negatives without brackets ("-1 x -3 = 3",
"1 x -3"), unlike the LP, which writes "(-1) x (-3)". This does not touch my three diagrams, whose grids hold bare numbers only.

### Chunk C notes (from the decision agent)
# Notes, chunk C (Class 7 Ch 10, cbse_eng_maths7_ch10_v69)

Result: 30 items (20 units), required 4 / optional 0 / none 26, validator `errors 0` (2 warnings, explained in 1.7).
Required: M3.S21.T21.C73 (question) and C74 (solution), M5.S28.T28.C100 (worked example, new id `C100.IMG2` because `C100.IMG1` is the kept teaching image), M5.S29.T29.C105 (solution).

## 1. Judgement calls

1. **C100 worked example, "Read the rectangle for 4 × (2 + (−3)) two ways": required.** The question refers to the book's token rectangle, and its 4 rows of 2 green and 3 red tokens exist only in the picture (FIG_REFERENCED). The plan already keeps a teaching image of the same rectangle (`M5.S28.T28.C100.IMG1`, with the results written on it). I followed v3 ("a referred figure is drawn even when a teaching image shows it"; the 'refer picture' exception needs an EARLIER topic's image, and here the image sits in the same concept). The new diagram is the plain book figure (braces 4 × (2 + (−3)), 4 × 2, 4 × (−3), no results), so it is not a copy of the teaching image. If you think two near-identical rectangles in one concept is too much, this is the one to drop (set it `optional`).
2. **T21 "Try again" (C73/C74): question AND solution required.** The question says "circle 8, then 14, then 18, then −15" but the LP text does not contain the grid; without the 4 × 4 grid the learner cannot attempt it (DATA_IN_FIGURE + ACTION_ON_FIGURE). Solution = the same grid with the four circles on the diagonal (answer is a marked figure). Question figure = bare grid only (the book circles nothing here); solution `derived_from` the question diagram.
3. **C74 solution figure has no strike lines.** The book's game strikes out the row and column of each circled number. After the fourth circle every row and column is struck, so the lines would cross all 16 numbers and add nothing, and the LP solution never mentions them. I drew circles only and said so in `render_note`. If you want the book's lines, add GUIDE lines through the middle of all 4 rows and 4 columns, numbers on top.
4. **C104/C105 (Try This: −4 × (2 + (−3)) with tokens): question none, solution required.** The question gives no figure (the learner builds the picture), so no question figure was invented. The LP solution describes an arrangement in words (4 rows of 2 reds and 3 greens, 8 zero pairs cancel, 4 greens left), so the picture is the answer (ANSWER_IS_FIGURE). The book prints no answer picture for this Try This. Zero-pair drawing choice: in every row the tokens are R R G G G; an inner dashed box round tokens 2-3 and an outer dashed box round tokens 1-4 give 2 zero pairs per row; the 5th token (green) is the one left over, so the 4 left-over greens form the right-hand column, tagged "= 4". The pairing is my drawing choice; the LP text only says "8 zero pairs cancel; 4 greens are left".
5. **Token colours.** The style table has no colours for positive/negative tokens (ANSWER green and WRONG orange have other meanings). I used TOKEN_POS #5FB36B (green) and TOKEN_NEG #E8744F (orange-red), as in the book's tokens, written into the descriptions. Other chunks that draw tokens should use the same two (merge check).
6. **None, but close calls:** C90 (−1 series; the book's box is a list of equations, the teaching ladder already exists), C91 and C78 (rules in words with examples), T27 Q2 / C97-C98 (3 consecutive numbers: trial products in LaTeX, a number line would not add anything), T24 Q2 / C86-C87 (long bracketed expressions: LaTeX). No `optional` was used; nothing here is "nice to have, not needed" enough to name a picture.
7. **Figure inventory.** Only two entries, because only two printed figures belong to this chunk's units. (a) `NEW-P15-number_grid-1-T21` is a second use of the book's 4 × 4 grid: the base figure `P15-number_grid-1` (and `P14-number_grid-1`) are also in the book section of T20 (C70/C71, chunk B), so I left the base ids to that chunk and used a NEW- id for T21's use, as the brief says for a figure used by two items. If chunk B does not claim `P15-number_grid-1`, the merge will report it unclaimed: then rename my entry to the base id. (b) `P18-integer_tokens-1` is mapped to C100 (question). The two validator warnings are C74 and C105 solutions: required, but no printed book figure maps to them (the book prints no picture of a "Try again" answer or of the Try This answer), which the validator says is fine.

## 2. Things in the LP that look wrong or odd

- **C73 question lacks the grid.** The LP question text only says "circle 8, then 14, then 18, then −15". It depends on the picture, so the diagram is essential; if it were ever dropped, the text would need the 16 numbers.
- **LP question numbering differs from the book.** T23 "Figure it Out 2.2, Q2" is the book's Q4 (ncert ref `FiO_C.Q4`); T24 "Q1" is the book's end-of-chapter Q2 and "Q2" is end Q11; T27 "Q1" is end Q1 parts (b) and (c) only (part (a) is in chunk D, `end.Q1a`), "Q2" is end Q9. Harmless, but the book numbers in the cards will not match the printed book.
- **C77 and C78 have the same concept name as C76** ("Signs of quotients"); C77 is 50 ÷ (−25) and C78 is the summary of rules. Cosmetic.
- **C90 step 3 reads "(−1) × (−1) = 1, so four factors give 1".** It means the running product (−1) times the fourth −1; as written it looks like the two-factor line again. The answer is right.
- **C87 (end Q11):** parts (b) and (c) are not integers as printed (4/81 and 20/81); the LP says so and its arithmetic is right (648, −1215, −300, −1960, 280 all recomputed). Probably a misprint in the book's expressions; nothing to draw.
- All other LP arithmetic in this chunk was recomputed and is correct: 8 × 14 × 18 × 15 = 30240 (and the sign is negative with one negative factor), 25 × (−6) × 12 = −1800 in each order, 5 × (−3) × 4 = −60, (−2) × 7 × (−5) = 70, (−7) × 4 × (−1) = 28, (−2)(−1)(−5)(−3) = 30, (−3)(−2)(−1) = −6, 4 × 5 × 6 = 120, (−2) × 1 = −2 = −8 + 6, (−3) × (−3) = 9 = 15 + (−6), (−4) × 2 + (−4) × (−3) = 4.

## 3. Places where the book itself is unclear

- **p.17 −1 series box prints the five-factor line as "−1 × −1 × −1 × −1 × −1 = 1"**, but the text under it (and the LP, C90) says an odd number of factors gives −1. The LP is right; the book line is a misprint. It is a text box, so no base figure exists for it and none was added.
- **p.14 "Round 1 to Round 4" picture** (chunk B's figure): the three circles and all six lines are already drawn in Rounds 1 to 3, so it does not show the game step by step (the inventory agent noted this). It does not change anything in this chunk; I only checked the page to see how the book draws circles and lines (circles, lines through the middle of rows and columns).
- **p.22 Summary sign-rule table** (`P22-table-1`) is in no unit of this chunk and is not claimed here. Its column 4, rows 5-7 are printed 1, 2, 3 instead of −1, −2, −3 (the inventory agent noted it too). The merge should assign it (probably `none:LATEX_TABLE`) or the merged inventory check will report it unclaimed; same for `P23-game_board-1` (Terhüchü board), which no chunk-C unit touches.
- **p.18 Try This** gives only a hint, no answer picture and no count of rows, so the layout of C105 (4 rows, token order, zero-pair boxes) is derived from the LP solution text, not from the book.

### Chunk D notes (from the decision agent)
# Chunk D notes (Class 7 Ch 10, topics M5.S30.T30, S31.T31, S32.T32, S33.T33, S35.T35, S36.T36)

Result: 13 units, 24 items. Required 3 (worked example C112, worked example C113, question C119), optional 2 (solutions C120 and C122), none 19.
Output: `map/out_D.json`, validator `errors 0, warnings 0`. Five base figures claimed (3 to items, 2 to `none:`).

## 1. Judgement calls

1. **The three machine pictures are drawn (required).** Machine 1 (worked example, C112), Machine 2 (worked example, C113) and the unnumbered machine of Figure it Out Q7 (C119 question).
   - Q7: the book question is "find the operations done by the machine shown below", so the machine is the whole given. The LP text already transcribes all six rows, so a text-only reading is also defensible by the tie-breaker. I chose `required` because the LP text still says "shown below" and nothing is shown, and because the same kind of picture is drawn for C112/C113. **If you want text-only, flip C119 and the two worked examples to `none` (LATEX_TABLE); nothing else depends on them.**
   - C112 / C113 (worked examples): the question text names "Machine 1" / "Machine 2" but gives none of its rows (they appear only in the steps and in the book picture). This is a referred figure, so v3 rule B2 says to draw it even though the concept's teaching image (C112.IMG1, C113.IMG1) shows the completed machine. The figure is the machine as the book prints it: the two dotted circles in every row stay empty, the last star stays empty. The teaching images are not linked.
   - Every machine figure uses the same panel geometry (tall panel centred in the 16:9 card, 6 rows, 18 input squares, 12 empty circles, 5 filled stars, 1 empty star), so the three look like one family.
   - The name plate text ("Machine 1", "Machine 2", "Machine") is the machine's own label as printed in the book, not a caption. If the renderer or the "no titles" rule is read strictly, the plate can be left blank; nothing in the question or solution depends on it.
2. **Example 1 / Example 2 (units 68, 69): none on both sides.** The three inputs are in the question text and the rule was taught in the previous concept. The book's last row adds only those numbers and an empty star. This differs from the worked examples on purpose (there the rows exist only in the picture). The completed last rows (-13, -111) are already teaching images and are never linked.
3. **Q7 solution (C120): optional.** A completed machine (a - b x c in the circles, last star -70) would help, but the answer is an expression and a number, every row is checked in the LP steps, and the book prints no answer picture.
4. **Collatz Q5 (unit 71).** Question none: rule and example chain are in the text; the book's picture is a number chain with a loop-back arrow, i.e. a sequence (v3 Step C: number chains stay LaTeX). Solution optional: a flow picture (the loop 1, -2, -1, 4, 2, 1 with the chains from -21 and -6 joining it, and 13's own 31-number loop apart) would help the "describe the patterns" answer, but it is not needed.
5. **Q16 (unit 73): none on both sides.** The book picture is only three equations with empty boxes; the LP text already writes the boxes. The five filled-in ways for each of (a), (b), (c) are equations (boxes filled with numbers stay LaTeX).
6. **Figure it Out Q1(a), Q13, Q14, Q15, coin examples (units 63-65, 72, 74, 75):** the book prints no figure; pure arithmetic or word reasoning, none on both sides. Figure it Out Q10 (coins) has no picture in the book; a coin picture was not invented.
7. **Sibling consistency inside this chunk:** all arithmetic answers (63, 64, 65, 68, 69, 72, 73, 74, 75) are none; the two optional solutions (C120, C122) are the only ones where a picture would clearly help but text is complete.
8. **Ids:** the worked examples take `.IMG2` because `.IMG1` of their concepts is the kept teaching image. C119 question takes `.IMG1` (its old card is being replaced).

## 2. Things in the LP that look wrong or need care

- **Unit 71 (Collatz) question text prints 32 after 11** (copied from the book); the rule gives -32 and the LP's own solution says so ("The book prints 32 here, but the rule gives -32"). The question text therefore contradicts its solution until a reader gets to step 3. Consider writing -32 in the question, or keeping 32 with a one-line note. No picture was drawn, so the slip is not copied into an image.
- **Numbering and order differ from the book.** In T33 the LP's "Figure it Out, Q1..Q4" are the book's Q7, Q5, Q15, Q16 (and Q7 comes before Q5); in T30 "Q1, Q2, Q3" are the book's Q1(a), Q13, Q14; T36 "Q1" is the book's Q10. The LP holds only Q1(a) in unit 63; Q1(b), (c) sit in unit 57 (chunk C).
- **Unit 70 question text** says "the machine shown below" and then lists all rows. Once the figure is attached, the rows sentence repeats it. Harmless; it can stay for accessibility.
- **Unit 66 steps test only five rows**; the sixth row (-10, -12, -9) is the open row solved in unit 68 (Example 1). Same for unit 67 and unit 69. The figure keeps row 6 with an empty star, as in the book.
- **Unit 67 steps list the rows in a different order** from the book's machine (steps start with 5, 3, 7; the book's first row is 4, 8, -3). Each step names its row by values, so it is unambiguous; the figure follows the book's order.
- **Unit 75 extra block** ("Use lists of multiples to make a total of +4") is an LP-added example, not in the book (the book's own example is +85 with 10 and 5 coins, unit 74). Its arithmetic is right (13 - 9 = 4).
- Everything numeric in this chunk was recomputed and is correct: Q1(a) = -75; Q13 values -531684, -532108, -531137; Q14 = -5382; Q15 maximum 60 and minimum -60 (brute force over all orders and bracketings); Q16 all fifteen fill-ins; coin totals for (a) to (h) including 122 x 13 + 2 x (-9) = 1568; Machine 1 a + b - c, Machine 2 -(a x b) - c, Q7 a - b x c on all five given rows, last rows -13, -111, -70; Collatz chains for -7, -21, -6 and the 31-number loop of 13.

## 3. Where the book itself is unclear

- The Collatz picture (page 19) prints 32 after 11 (print slip; rule gives -32).
- The machines hide their operations by design (empty dotted circles); the book never prints the rule for Machine 2 or for the Q7 machine (this pdf has no printed solutions), so the LP's rules (-(a x b) - c and a - b x c) are the LP's answers, verified against every given row.
- Machine 2's question text sits at the top of page 19 while its picture is on page 18; the Q7 machine plate reads just "MACHINE" with no number and is printed slightly smaller than the two on page 18.
- Base inventory: all five entries I use match the page pictures; no corrections and no NEW- figures. P18-machine-1 is also used (last row) by unit 68 but is claimed once, by the worked example, because unit 68 needs no figure. The summary table, the Terhuchu board and the distributive-token figure are in other chunks' topics and are not claimed here.
