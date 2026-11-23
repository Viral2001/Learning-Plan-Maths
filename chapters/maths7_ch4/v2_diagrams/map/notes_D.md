# Chunk D notes: Class 7 Ch 4, topic M3.S32.T32 "Figure it Out 4.6" (Q1 to Q15)

Result: 30 items (15 pairs): required 9, optional 4, none 17. Validator: errors 0, 1 warning (Q6 solution, see below: the figure is not printed in the book).

| Q | question side | solution side |
|---|---|---|
| 1, 2, 3, 4 | none (no figure given) | none |
| 5 | required (star of paths, 4 empty ovals) | required (printed answer is the filled figure) |
| 6 | none (no figure given) | required (the rough diagram the hint asks for) |
| 7, 8, 9 | none (LaTeX) | none (LaTeX) |
| 10 | none (open ended) | none |
| 11 | required (3 rope pictures) | optional |
| 12 | required (3 matchstick figures) | optional |
| 13 | required (5 coloured signal lights) | optional |
| 14 | required (3 X patterns) | optional |
| 15 | required (4-column grid) | required (printed answer to (d) is the grid with multiples of 3 shaded) |

Media ids are all `<concept id>.IMG1` (no kept images in any of these concepts).

## 1. Judgement calls

- **Q6 solution = required (the one I am least sure of).** The printed answer is text only (22 minutes, 4t + 6), so no B2 rule forces it. I chose required because the book's hint says "Draw a rough diagram to visualise the situation", the typical slip is 3 journeys instead of 4, and the LP's own `s_figure` already describes the drawing; by the tie-breaker the picture changes how correctly the student solves it. Question side is none (the book gives no figure; a question figure would invent one). If you prefer text only, change it to optional/none: nothing else depends on it. The figure carries no totals (no 22, no 4t + 6).
- **Q13 and Q15 question figures = required although the LP text already carries the data.** LP Q13 names the colour order red, yellow, green, yellow, red; LP Q15 lists the first rows. The book, however, gives both as figures (coloured signal lights numbered 1 to 5; a 4-column grid with column numbers), and Q15(d) "observe the positions of multiples of 3" is built on the grid. Following "what the book question GIVES", both are required. If you want the strict "could the text alone do it" reading, Q13 question is the weakest and could drop to optional.
- **Q11 to Q14 solutions = optional (not added); sibling consistency.** These four have the same kind of answer (pattern to formula, text-only printed answers). A solution figure would be nicer (pieces 2, 3, 4 on the ropes; new sticks coloured; positions 1 to 12 coloured; Step 4 with 17 squares) but the LP text is complete. Q15 differs: its printed answer (d) is a picture.
- **Q2 solution = none.** A two-circle Venn picture (champak, marigold, both) would be nice, but the book has none and the text already has a p = 3, q = 4, r = 2 check. Not marked optional so as not to invent a figure the book does not have.
- **Q14 figures drawn without "Step" labels.** The book prints none (the steps are read from the answer: Step 4 = 17). The LP question text says "Step 1 has 5 squares", so the 5, 9, 13 squares identify the steps. Same for Q12 (no step labels in the book).
- **Q12: three figures of 1, 2 and 3 squares** (4, 7, 10 sticks), as in the book. The LP hint `q_figure` says "a row of four squares", which is wrong (see section 2).
- **Q13 colours** use literal hex values for red, yellow and green (the signal colours are the content, not a style token): red #F08060, yellow #FFF59D, green #8FCB8B. All other colours are style tokens.
- **Ropes (Q11)** are drawn as a flat stylised stroke with knots and a FOCUS dashed cut line, not as photographs. Picture 3 is idealised to three parallel layers joined at alternate ends (the book draws it loosely); the 3 crossings are checked on the enlarged page picture and recomputed from the coordinates (1, 2, 3 crossings; 2, 3, 4 pieces).
- **Q15 grid:** the book fades the vertical lines below row 4 (question) and uses dotted lines (answer picture); I use dotted GUIDE lines in both, so the solution keeps exactly the question layout (no gradients allowed). Cells are 2.0 wide and 1.2 tall (the book's are square) to fit the 16:9 card; labels, values and shading are as printed. Shaded cells use MARK_FILL with an ANSWER border; numbers stay INK (the book uses blue).
- **Aspect ratio 16:9 for every figure**, including the near-square grid and the wide rows: the pipeline draws 16:9 cards.
- **Duplicate prints.** The pdf holds every 4.6 figure twice: question part (pdf pages 22 to 25) and answer part (pages 35 to 40). Both base entries are claimed: the answer-part copies (P37-pattern-1, P38-pattern-1, P38-pattern-2, P39-pattern-1, P39-number_grid-1) map to the same question item as the page 22 to 25 copy, and say so in their description. Only P35-flow_diagram-1 and P40-number_grid-1 are printed-answer pictures (solution items).
- **P24-rope_fold-1 description corrected** ("CORRECTED:"): in picture 3 the top knot is on the upper-left side of the cut line, not on its right as the base text says. The crossing counts (1, 2, 3) were confirmed.

## 2. Things in the LP that look wrong or thin

- **Q5 question text is muddled:** "The other paths use the operations multiply by 3, subtract 8, subtract 4 and subtract 4, starting from w + 2 and w − 3, and the missing ovals are to be found." The real figure: inner boxes −5, +3, −8, −4; second boxes ×3, ×4, −4, ×3. Because the question diagram is required, the figure now carries everything; the sentence can stay but is confusing. `q_figure` (hint) is correct.
- **Q12 `q_figure` hint says "A row of four squares ... each square sharing a side with the next one".** The book shows three separate figures with 1, 2 and 3 squares. The question text does not give the numbers 4, 7, 10; they live only in the figure.
- **Q14 vertices answer 16n + 4** (book and LP): it counts 4 vertices per square, but squares on an arm touch at corners, so those corner points are shared. The book's answer is followed as is; "number of vertices" is ambiguous in the book. Not a diagram matter.
- **Answer concepts' `video_media_id` ids point to the next concept's number** (e.g. answer C128 carries `M3.S32.T32.C129.VID1`, Ans5 carries C137.VID1). Probably the id scheme of the video block, not a problem for diagrams, but worth a look if videos ever look misplaced.
- **LP answer forms vs book:** Q7(f) LP "21m − 20n + 5" vs book "5 + 21m − 20n"; Q9(b) LP "18x + 16y − 23" vs book "16y + 18x − 23"; Q9(d) LP "−3a − 3b − 32" vs book "−(3a + 3b + 32)"; Q9(c) LP "10h − 27g + 2" equals the book. All are equal expressions in a different order; I recomputed Q7, Q8, Q9 and Q4, Q6, Q12, Q13, Q14, Q15: all LP values are correct.
- Q1 and Q2 questions in the LP are text only and fine; Q3 snail has no figure in the book.

## 3. Book unclear

- Q14 (pages 24 and 39) and Q12 (pages 24 and 38): no step numbers printed under the figures.
- Q11 picture 3: the folded rope is drawn loosely and small; layer count read at high zoom is 3.
- Q13: the three signal colours carry the meaning on their own (no letters printed); positions 1 to 5 are numbered.
- Q15 (page 25 vs 39): the open end of the grid is drawn as fading lines in the question and dotted lines in the answer picture (page 40); no row numbers anywhere.
- The brief says the pdf has no printed-solutions section, but it does (pages 26 to 41); the LP solution text was followed throughout and agrees with the printed answers.
- Housekeeping: while looking for the chunk file layout I accidentally printed about 60 lines of `map/out_A.json` (meta and the first inventory entry). I did not use it for any decision.
