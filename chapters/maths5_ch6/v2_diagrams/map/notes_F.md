# Chunk F notes: Class 5 Ch 6 "The Dairy Farm", topics M4.S32.T32 to M4.S36.T36 (pdf pages 20 to 22)

Result: 27 items, required 2, optional 3, none 22. Validator: errors 0, warnings 0.

I looked at page_20.png, page_21.png and page_22.png. Pages 20 and 22 print no figure at all (text only). Page 21 has the five figures of the base inventory (four dashed pattern boxes, one number-pairs board). I checked all five base descriptions against the picture: they are right, so none is marked CORRECTED.

Only diagrams made: the number-pairs board.
- M4.S34.T34.C170.IMG1 (question): the 3 x 3 board 8, 35, 75 / 32, 62, 13 / 66, 11, 14 with its 12 joining lines.
- M4.S34.T34.C171.IMG1 (solution, derived_from C170.IMG1): the same board with the pair 11 and 14 (smallest product 154) and the pair 35 and 75 (largest product 2,625) circled.

## 1. Judgement calls

- **C170 question, required.** The LP question text says "Here are some numbers" but lists none, and which neighbours are joined by a line (the "number pairs") is only in the picture. DATA_IN_FIGURE + FIG_REFERENCED.
- **C171 solution, required.** The answer is two circled pairs on that board (HIGHLIGHT_MEANING, ANSWER_IS_FIGURE). I recomputed all 12 products: 280, 2,625, 1,984, 806, 726, 154, 256, 2,112, 2,170, 682, 975, 182. Smallest 154 = 11 x 14, largest 2,625 = 35 x 75, both pairs are joined by a line. Same as the LP.
- **Circle colours.** The old LP hint (s_figure) said green and orange circles. I used the house token FOCUS for both outlines and told the pairs apart with two short tags in ANSWER green, "Smallest: 154" and "Largest: 2,625". These use the words of the LP answer ("Smallest: ... Largest: ...") and stay within the 3-word tag limit.
- **Aspect ratio.** The board is square, not tall, so I kept 16:9 as the brief says; the board sits centred with wide side margins.
- **C159 question (King's Reward Q2), none.** The hint q_figure ("three rows, start coins in the first box, 7 empty boxes") is not in the book: page 20 is plain text. A question with no given figure gets no question diagram.
- **C160 solution, none (LATEX_TABLE).** The working is three growth chains for 7 days. That is a plain table of numbers, so it stays LaTeX. I put the exact LaTeX table content in `text_alternative`.
- **C168 / C169 (pattern boxes), none both sides.** See Borderline.
- **C165, C167 (Multiplication Patterns Q1 a, b), none.** Plain equations, the book has no figure. The relations (half, double, quarter, same) are said in words in the LP steps.
- **Three solutions are `optional`:** C179 (Q3 Republic Day), C183 (Q5, 67 x 68), C185 (Q6, 99 x 99). The figure that would help is named in each `reason`. C183 and C185 are siblings and got the same decision. M4.S27.T27.C134.IMG1 ("One more column, one row less") shows the same idea as a teaching image; per the user's rule 5 that was not used as a reason, and it is never linked.
- **C158, C175, C177, C181 and the four worked/Q1 items**: plain arithmetic or word reasoning, none.

## 2. Borderline (decision 4)

1. **C168 question and C169 solution, the four pattern boxes (P21-pattern-1 to 4): none.** The book prints four dashed boxes of equations with blanks and red hint notes. Every equation is already in the LP question text, and a picture of the boxes would copy the question text (question side) or the answer line (solution side). Equations and sequences are LaTeX by the v3 rule (Step C, LATEX_ARITHMETIC), the same as a fill-in table. Against this: the red notes (5 x 5 = 25 with 2 x 1 = 2 beside 15 x 15, and the H T O digit sources beside 11 x 12 and 11 x 34) are part of what the book gives and sit only in the picture. If you want the book's boxes drawn, the question and the solution (filled blanks in ANSWER green) would both become `required` with `cell_grid` or `other` specs; the numbers are all in the LP text and this note.
2. **C160 solution (King's Reward Q2): none.** A day-by-day filled strip would look nice, but it is a plain table of numbers (LATEX_TABLE). If the user wants it as a picture it would be `required`, derived from no question diagram (the question has none).
3. **C179, C183, C185: optional (not added).** Each would be a sketch of a rows-and-columns block (or the ground seen from above). The text carries every number and the answers are numbers, so they are not needed; they are the three places where a picture would clearly help understanding.
4. **C170 question: required although the LP text carries the question.** The figure is needed because the numbers are not in the LP text at all.

## 3. LP text issues

- **M4.S34.T34.C168 (Q2 patterns, question).** The text lists the equations but drops the book's red hint notes. Suggested sentence to add after the four lists: "Hints from the book: beside 15 × 15 = 225 it writes 5 × 5 = 25 and 2 × 1 = 2; beside 25 × 25 = 625 it writes 5 × 5 = 25 and 3 × 2 = 6; beside 11 × 12 = 132 it writes, under Hundreds, Tens and Ones, 1 × 1, 1 + 2 and 1 × 2; beside 11 × 34 = 374 it writes 1 × 3, 3 + 4 and 1 × 4." The book's four boxes have no letters; (a) to (d) are the LP's own and the LP answer uses the same letters.
- **M4.S34.T34.C170 (number pairs, question).** The text has no numbers and no mention that only boxes joined by a line are a pair ("Here are some numbers. ..."). Fine once the diagram is shown after the question text; for any text-only use, add: "The numbers are 8, 35, 75 in the first row, 32, 62, 13 in the second row and 66, 11, 14 in the third row. Two boxes are a pair only when a line joins them."
- **M4.S34.T34.C159 (King's Reward Q2) q_figure hint** describes a strip of empty boxes that the book does not print. Do not rely on it (no change needed, no diagram was made).
- **M4.S33.T33.C162 (Patterns in Products).** `ncert_refs` is `mp.pairs_def`, but the example is the patterns of book Q2 (b) and (c) (65 × 65 and 11 × 36); the pairs/grid is C170. Probably a wrong tag.
- **Concept names versus book numbers in M4.S34.T34.** The concepts are named Q1, Q2, Q3, Q4 (C164, C166, C168, C170) but the book numbers are Q1 (a), Q1 (b), Q2, Q2 number pairs. Only the names differ; not a problem for the diagrams.
- **M4.S34.T34.C165, first step.** "Solve (a): completely: 16 × 44 = ..." has a stray colon; suggested "Solve (a) completely: 16 × 44 = ...".
- **Number style.** The book prints 1111 × 1111, 4489, 9900 without commas; the LP writes 1,111 × 1,111, 4,489, 9,900. No diagram uses these.
- Hint fields (q_figure, s_figure) are otherwise accurate for C168 and C170 (the board and the two circled pairs); the colour words in C171 s_figure were not followed (see Judgement calls).

## 4. Book unclear

- **King's Reward Q2 (page 20):** "double the number of coins every day for 7 days" does not say whether the start coins count as day 0 or day 1. The LP states its reading (7 multiplications: 640, 6,561, 78,125) and gives the other reading (6 multiplications) in a step. No diagram depends on it.
- **Let Us Solve Q3 (page 22):** the book does not say every row has the same number of students; the LP assumes 41 in each row and says so. No diagram depends on it.
- No book print slips (wrong digit, missing sign, wrong count) found on pages 20 to 22: all printed equations check out (e.g. 35 × 35 = 1,225, 1,234 × 9 + 4 = 11,110, 11 × 82 = 902).
