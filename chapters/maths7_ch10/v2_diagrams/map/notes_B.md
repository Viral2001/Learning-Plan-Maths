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
