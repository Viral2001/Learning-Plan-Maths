# Notes, chunk A (We the Travellers - I, topics M1.S2.T2 to M2.S12.T12)

Result: 20 units, 28 items. Required 3, optional 0, none 25. Validator: errors 0, one warning (C34 has no printed book figure, expected).
Required: question diagram of C13 (token rows 1 and 2), question diagram of C15 (token rows a to d), worked-example diagram of C34 (number line with four numbers placed).
Figure inventory: 18 base figures claimed (2 to items, 2 to concept images, 14 none). Figures of pp.6-7 that belong to the comparing questions (number cards, number lines, Q4 chart) are not mine (chunk B).

## 1. Judgement calls

- **Token tables, C13 and C15 (question required, solution none).** The book gives the rows as token pictures; the learner counts tokens. Triggers DATA_IN_FIGURE and ACTION_ON_FIGURE. The token counts of C13 row 2 and of C15 (b), (c), (d) are in the picture only (the LP text gives them for C15 (a) only), and the LP solutions work from them ("Check with the tokens", "Two 10,000 tokens make 20,000"). I drew the tokens only, not the whole table: the Number, TTh to O and Number Name cells are a plain table of digits and words (LATEX_TABLE, HEADER_BOXES_ONLY), so the solution (C14, C16) only fills those cells and would repeat the question figure: none, SAME_AS_QUESTION_DIAGRAM. Row labels: numerals 1, 2 in circles (C13, the LP says "Row 1/Row 2") and letters (a) to (d) (C15, the LP answer uses them; the book prints no letters on the rows). Chips use one neutral fill (CELL_FILL) with the printed value, not the book's place colours, to stay in the house palette. Layout rule: tokens of one value form a block, blocks run 10,000 -> 1, two chips per line; C15 (d) has 30 tokens and fits the card (912 px of 1080).
- **Number-line worked example C34 (required).** The example itself says "place ... on a number line with the marks 0 ... 40,000" (place on a line), so it needs its own picture; the teaching image 'Numbers on a number line' is never linked (v3). The figure shows the finished placement (four ANSWER-green points, to scale, 1 px = 25 units), because a worked example's figure is the picture the example needs and its steps follow at once. The id is C34.IMG2 because C34.IMG1 is the kept teaching image.
- **Sequences with blanks (Let Us Do Q1 a to i, C27 to C32; counting strip C8/C9): none.** Number chains: LATEX_ARITHMETIC (Step C: "sequences, number chains") and the brief ("sequences stay text/LaTeX"). Every given value and every blank position is stated in the LP question text; no shading, colour or arrow carries meaning; the 10-box snake of (d) to (i) is only layout. `text_alternative` gives the LaTeX line for each. The jump-arrow chain the old cards showed would be the optional figure, not added.
- **Number | Number Name table of Let Us Do Q2 (C17/C18, C22/C23): none.** Plain two-column table: LATEX_TABLE. One base figure (P06-table-1) serves both pairs: one entry, none.
- **Worked examples C3, C5, C6, C10, C11, C19, C20, C24, C25, C33, C35: none.** Reading or writing a number from its digit chart (header boxes with digits: HEADER_BOXES_ONLY), adding 1,000s, patterns by differences (LATEX_ARITHMETIC), digit and length comparison (TEXT_SUFFICIENT). Each already has a teaching image in the plan (never linked). C35 is open (many answers are right), so none.
- **Teaching figures.** P02-table-1 mapped to concept image C6.IMG1 (it carries the TTh column and the x10 arrows; not an identical picture, accounting only). P02-tokens-3 to C5.IMG1 (same picture). P02-base_ten_blocks-2, P02-tokens-4 (1,380), P02-tokens-5 (9,123): none, TEXT_SUFFICIENT, because no question, solution or worked example uses them and the sentence above each carries the content.
- **p.1 art.** The three opening pictures (bullock cart, cyclist, traffic jam) are decoration (Step 0 skips them) and were not inventoried by the base; I made no NEW- entry for them.
- **Token counts re-checked on the page pictures** (p.3 rows 5 and 6, p.4 rows 1 to 4): they agree with the base inventory and with the LP solutions (11,214, 13,520, 20,000, 45,867, 10,033, 10,458).

## 2. LP text issues

- **M1.S6.T6.C13** (question): says "Fill in the token table" but there is no table in the text, and the tokens of Row 2 are not stated (only its number 10,458), although the solution's last step checks "with the tokens". Suggested sentence: "Fill in the token table, one row at a time. Row 1: the tokens are one 10,000, three 10s and three 1s. Row 2: the tokens are one 10,000, four 100s, five 10s and eight 1s. For each row write the number and its digits under TTh, Th, H, T, O." (The new diagram shows the tokens, so the sentence is optional but removes the hidden dependency.)
- **M1.S6.T6.C15** (question): the token counts of (b), (c), (d) are not stated; (a) is. Suggested: "(b) one 10,000, three 1,000s, five 100s and two 10s; (c) two 10,000s; (d) four 10,000s, five 1,000s, eight 100s, six 10s and seven 1s." Same remark about the missing table.
- **M1.S7.T7.C17 / C18 and M1.S9.T9.C22 / C23** (Let Us Do Q2): the book's table starts with two finished example rows, 8,045 = Eight thousand forty-five and 20,869 = Twenty thousand eight hundred sixty-nine, which the LP omits. Suggested: "For example, 8,045 is Eight thousand forty-five and 20,869 is Twenty thousand eight hundred sixty-nine."
- **M1.S11.T11.C31 / C32:** the letter "(i)" is not in math mode while "(h)" is `$(h)$` (question_tex of C31, steps_tex and answer_tex of C32). Suggested: write `$(i)$`.
- **M1.S4.T4.C8** `q_figure` hint says the boxes are "joined by arrows"; the book strip has no arrows (hint only, no effect now).
- **Old image markers:** the `text` field of every solution concept of this chunk (C9, C14, C16, C18, C23, C28, C30; C32 has none mid-text) still carries `[Image: ... solution]` lines in the middle of the steps and `(continued)` at the end, and the plan has old cards C9.IMG1/IMG2, C14.IMG1/IMG2 and so on. All 8 solutions here are none, so these cards and markers must be dropped (builder, `drop_image`); the new tokens are only C13.IMG1, C15.IMG1 (question side) and C34.IMG2.
- No contradiction found between an LP solution and the book; all LP arithmetic (names, sequences, token sums) was recomputed and is right.

## 3. Book unclear

- p.1: the 9-box strip has no arrows (LP hint says it has).
- p.2: the x10 arrows sit over TTh, Th, H, T and curve left; the page does not say what they connect (read as "one place to the right times 10").
- p.3 row 2: the two 1 tokens are coloured like 100 tokens (a drawing slip, value 1); this row is a teaching row and is not drawn.
- p.3: "You can use the tokens given in the end of the book" (not in this pdf).
- p.6: the two finished rows of the Q2 table are examples but are not labelled as such.
- p.5 (d): 10,900 sits in the 9th box (second box of row 2 running right to left), which agrees with the LP ("five empty boxes, 10,900 and one more empty box").

## Borderline

- Sequences with blanks (C8/C9, C27 to C32, 8 items): none by the explicit "sequences stay text/LaTeX" rule, although the book draws boxes. If you want them drawn, the figure would be an `arrow_map` chain (boxes with the given values, blanks, jump arcs in the solution).
- Token tables: question required, solution none. If you prefer the whole table as the figure (question with the given cells, solution with the filled cells in green), C14 and C16 would become required; I kept tokens only because the digit and name cells are a plain table.
- C34 required (number line with the four numbers placed, shown before the steps); the alternative is none with the steps in text.
- Place-value digit charts in worked examples (C6, C10, C11, C19, C20, C33): none (HEADER_BOXES_ONLY), although each has a coloured teaching image in the plan (never linked).
- C35 none (open answer); a number line with sample numbers would be the optional picture.
