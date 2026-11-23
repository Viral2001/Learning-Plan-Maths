# Notes, chunk F (Class 6 Ch 10, plan cbse_eng_maths6_ch10_v91)

Units: Figure it Out 10.4 Q1-Q9 (M4.S41.T41), Figure it Out 10.5 Q1-Q2 (M4.S43.T43), Snakes and Ladders worked example (M4.S44.T44).
Result: 23 items, required 1 / optional 1 / none 21. The validator prints errors 0.

## 1. Judgement calls

- **Q9 question (M4.S41.T41.C214): required.** The question text says only "a particular pattern"; which tokens are positive or negative exists only in the picture (book pdf p.25, reprinted on solutions p.56). Media id `M4.S41.T41.C214.IMG1`. Spec: 15 touching tokens, + + + - - three times (9 positive, 6 negative), then a wavy line curling down. Only 15 of the 100 tokens are drawn, as in the book. The picture carries no number (no 100, no 20) and no grouping marks, so the answer is not given away.
- **Q9 solution (C215): optional, not added.** A copy of the string with three brackets of 5 tokens, each marked +1, would help the "block of 5 = +1" step. The steps say it in words and the question figure already shows the pattern, so I did not make it required. Ask me if you want it required.
- **Token colours.** The book uses green for positive and orange-red for negative. The style table has no token colours. I used MARK_FILL (pale green) for positive and SET_B (amber) for negative, with INK outline and INK signs. The printed + or - sign carries the meaning. WRONG (orange-red) is reserved for wrong cases and ANSWER (green) for solution additions, so I did not use them. If other chunks colour their tokens differently (for example teal and amber like the existing teaching images), the merge may want one palette for all token pictures. The `render_note` says so.
- **Q4 (expressions table): none on both sides, `LATEX_TABLE`.** The question table is a plain 2 x 4 table of expressions. The printed answer (solutions p.55) is a plain black-ruled table of numbers, not a picture in the sense of rule B2. `text_alternative` gives the LaTeX arrays to write.
- **Q1, Q3, Q5, Q6, Q7, Q8: none.** All are in words, equations or number lists. I considered a number line for Q1 and Q3 (marking the integers between, or the impossible dice sums) and a timeline for Q5. All would only make it nicer, and the tie-breaker says none.
- **10.5 Q1 solution: none** (`OPEN_ENDED`, `TEXT_SUFFICIENT`). One picture cannot serve the ten rules. The lift and number-line ideas for 2 + (-3) and 2 - (-3) are already concept images of earlier topics (and are never linked). 10.5 Q2 solution: none (ten sample equations).
- **Snakes and Ladders worked example: none.** The rules are complete in words and the answer is only "play the game". The kept concept image `M4.S44.T44.C224.IMG1` already shows the move idea. The book's board (P30-board-1) is game artwork. Its snakes and ladders overlap and hide numbers, and their ends are only approximately readable, so I mapped it to `none:NOT_RENDERABLE`. The two dice (P30-dice-1) are `DECORATIVE_ONLY`, because the numbers +1 to +6 and -1 to -6 are in the text. If the team wants the board, a plain numbered track (START 0, +1 to +50 and -1 to -50 on a snake path) could be drawn as an optional worked-example figure. Without the snakes and ladders it would be a different picture from the book's.
- **Figures claimed beyond the units' own pages.** The seven Learning Material Sheets figures (P32 to P40: two dot sheets, two squared sheets, tangram, fraction wall, tile sheet) follow chunk F's last topic and belong to no unit, so I claimed them all as `none:DECORATIVE_ONLY`. Nothing in the plan uses them. They are blank or cut-out material. If another chunk also claims them, the meaning is the same.
- **Figures not claimed.** The Figure it Out 10.4 "amazing grid" pictures (P24-grid-1, P24-grid-2, SOL55-grid-1, SOL55-grid-2) belong to the amazing-grid questions, which are chunk E's. I left them.
- **Printed-solution figures of my questions:** SOL55-table-1 (reprint of the Q4 table) is `LATEX_TABLE`. SOL55-table-2 (Q4 answer table) is `LATEX_TABLE`. SOL56-token_string-1 (reprint of the Q9 string) is `SAME_AS_QUESTION_DIAGRAM`, because the question's own figure P25-tokens-1 is the one drawn.

## 2. Things in the LP that look wrong or thin

- **Q4 question text** (M4.S41.T41.C204): it contains the stray build note "(table of $8$ expressions, row $1$ then row $2$)" and invents the letters (a) to (h). The book has no letters, only a table. The solution uses the same letters, so it is consistent, but the parenthetical should go before this reaches learners.
- **Q9 question text** gives no pattern, so the plan depends entirely on the diagram token. If the diagram were ever dropped, the question could not be answered.
- **Q9 solution wording** says "green" and "red" tokens. The new picture shows pale green and amber tokens with +/- signs. Suggest "positive (+) tokens" and "negative (-) tokens", or accept the small colour difference.
- **Q5 (a) and (b)** assume the present year is 2026 and the LP says so in the answer. The book prints only the answer to (c), "-360 BCE". The LP writes "360 BCE", which is the same year. The LP's own work checks out: 2026 - 2200 = -174, which is 175 BCE because there is no year 0.
- **Q6 (c)** The LP and the book agree: 27, 19, [12, 6, 1, -3, -6], -8, -9, -9. The book prints it as "27, 19, ... -8, -9, -9".
- I recomputed the other answers (Q1 lists, Q3 sums: 15 possible and 8 missing, Q4 all eight values, Q7 = -30, Q8 sign rules, the 10.5 Q2 sample equations). All agree with the book's printed answers.
- The book prints no answers for 10.5 Figure it Out Q1 and Q2 (open-ended). The LP's sample answers are the LP's own.

## 3. Places where the book is unclear

- **P30-dice-1:** the third face of the blue (negative) die is partly turned away, so its sign cannot be read ("4" or "-4"). It is not drawn, so it does not matter.
- **P30-board-1:** snake and ladder ends cannot be read exactly; some cell numbers (for example -1, 43, 18) are hidden under the artwork.
- Q9's string: the book draws only 15 tokens and a wavy end for a string of 100. The 100-token pattern (5 repeating, + + + - -) is inferred, as the LP does.
