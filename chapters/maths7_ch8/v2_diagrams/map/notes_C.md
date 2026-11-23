# Notes, chunk C (units 43-59), Class 7 Ch 8 "Working with Fractions"

Result: 32 items = required 4 / optional 4 / none 24. Required: worked example Fig. 8.4 (M3.S23.T23.C106.IMG2), practice (a)+(b) question figure (M3.S24.T24.C109.IMG1), Figure it Out Q10 question figure (M3.S25.T25.C111.IMG1), Fig. 8.7 ants question figure (M3.S25.T25.C113.IMG1).

## 1. Judgement calls

1. **Every solution side is optional or none (nothing added).** The four figure questions (practice a/b, Q10, ants) have numeric answers and the book's printed answers (pp.36, 38, 39) are text only, the figure being just repeated. Prompt Step E: "figure-based question, numeric answer: Q required, S none (or optional if the solution splits the shape)". I marked them `optional` and wrote in each `reason` exactly what the solution figure would carry (same layout, ANSWER-green marks): 
   - practice (a)/(b): 1/8 on the corner triangle, 3/8 on the band; 1/4 on the top-left small square, 1/16 on the shaded pair;
   - Q10: bottom-right quarter 1/4, top triangle, shaded piece 3/32 (see LP slip below);
   - ants: 1/2, 1/2; 1/4, 1/4; four 1/16; 1/32, 1/32 on the paths and totals 29/32, 3/32.
   If you want these labelled solution figures, they are cheap to add (derived_from the question diagram).
2. **Example 3 (milk in each cup): nothing drawn.** The book prints a tape strip (P18), but it carries no data beyond the words, so question = none (TEXT_SUFFICIENT); the solution tape (1/4 litre cut in 5, one part 1/20 litre) is `optional`. P18 is mapped `none:TEXT_SUFFICIENT`. Say so if you want it required.
3. **Example 4 (bricks): nothing.** The book has no figure; the LP's "unit square of 25 bricks" hint is the teaching image of an earlier topic (M3.S20.T20.C83.IMG1), never linked.
4. **Worked example M3.S23.T23.C106 (Fig. 8.4): required.** One picture merges Fig. 8.4 (given), the red outline of Fig. 8.5 and the yellow half-triangle of Fig. 8.6, because the LP question describes all three (red quarter, yellow triangle, shaded 3/4 of it). media_id is IMG2 because IMG1 is the kept teaching image. P20-shape-2, P20-shape-3 and P21-shape-1 are mapped to that teaching image (accounting only).
5. **Palette gap:** the style table has no red or yellow token. The "red" quarter is a FOCUS (pink) outline and the "yellow" triangle is SET_B (amber, 45 percent). `needs_lp_text_sync: true` on this item: the question text could say "outlined" / "amber" instead of "red" / "yellow" (or the builder may allow red and yellow for this one figure, your decision).
6. **Practice (a)+(b): ONE question image holds both figures** side by side (left = first block, right = second block) because the brief allows one question diagram per pair; the v3 prompt section 2 would otherwise give each part its own. The figures are drawn exactly as printed (including the lines the LP words do not mention). `needs_lp_text_sync: true`: the second block's text says "a big square is split into four equal squares" but the book's figure (b) leaves the bottom half as one 2:1 rectangle and the top-right square empty.
7. **Q10 apex:** the printed V apex sits a little above the quarter's centre (about 0.47 of the way down); the spec puts it exactly at the centre because the book's answer 3/32 only works there.
8. **Ants figure** is portrait (about 0.87 wide to high) but kept at 16:9 as the pipeline draws cards; the frame is centred at 0.92 of the card height. Paths are MARK_FILL bands with an INK edge, split points FOCUS dots; the book's red labels bars use CELL_FILL.
9. **Figures claimed outside any unit:** P23-grid-1 (Pinch of History text, concept M3.S26.T26.C117, no question item), P27-chessboard-1 and -2 (Puzzle Time queens, concept M4.S29.T29.C123, no question item) and P29-cutout-sheet-1 (Learning Material Sheet, never referred to). No unit of chunk A, B or C covers them, so the merged completeness check would fail otherwise. Mapped `none:TEXT_SUFFICIENT`, `none:OPEN_ENDED` (x2), `none:DECORATIVE_ONLY`. Drop these four entries at merge if another chunk or the orchestrator claims them with the same meaning.
10. Text items (Example 4, 5, Figure it Out Q2-Q8, dramma, coins, Q12) are all plain words / LaTeX arithmetic: none. Q8 (cake) and the coin chain could take a bar or flow picture, but the text is complete.
11. Printed-answer pictures P36-shape-1/2 and P38-shape-1 only repeat the question figures: `none:SAME_AS_QUESTION_DIAGRAM`.

## 2. Things in the LP that look wrong (not edited by me)

- **M3.S22.T22.C92 / C93, Figure it Out Q2(c)(iv):** the LP text reads "5 x 6/3 / (7/9)" (question, question_tex, text, and the copy of the question in the answer concept). The book prints "(iv) 5 x 6". Looks like leaked text from the Q1 table (3 / (7/9)).
- **Book numbers are shifted / duplicated:** T22 items are labelled Q1..Q7 but are book Q2..Q8; T25 "Q1", "Q2" are book Q10, Q11; T28 "Q1" is book Q12. Meanwhile chunk B labels book Q1 (evaluate table) and Q9 (565/465) also "Figure it Out 8.3, Q1", so the label "Figure it Out 8.3, Q1" is used by 5 different items.
- **M3.S25.T25.C112 (Q10 solution) has the wrong geometry in steps 2-3** though the final 3/32 is right. With the V apex at the centre of the quarter the top triangle is 1/4 of the quarter (1/16 of the whole), not "half of it, 1/8"; the shaded piece is half (not 3/4) of the part below the V. Correct chain: 1/4 (quarter) x 3/4 (below the V) x 1/2 (left of the vertical) = 3/32. The LP's product 1/4 x 1/2 x 3/4 gives 3/32 only by commutativity.
- **M3.S24.T24.C109 second block:** "split into four equal squares" does not match the book figure (see call 6). Both blocks carry the same book_number and neither names "figure (a)" / "figure (b)".
- **Stale s_figure hints:** C97 says "four saplings in a row, gaps 3/4 m" (that is chunk B's Tsewang question, not the Sridharacharya sum); C89 describes the 25-brick teaching image; C87, C110, C112, C114 describe solution figures that this run leaves optional.
- **M3.S27.T27.C119:** the LP drops "1 pana = 6 mashakas" from the book's exchange list (harmless); the answer is consistent (1/48 dinar, 1/1440 dinar).
- Arithmetic re-checked and correct: Ex 3 (1/20), Ex 4 (375/2 = 187 1/2), Ex 5 (1 + 2 + 4 + 5 = 12, 1/12 day), Q2 (32, 1/16, 30), Q3 (1/8 kg), Q4 (40), Q5 (200), Q6 (44 km), Q7 (4 2/3), Q8 (1/15), dramma (6/7680 = 1/1280, 1 cowrie), Q12 (1/2, 1/3, 1/5, 1/10, 1/n), ants (29/32 + 3/32 = 1).

## 3. Where the book is unclear

- Fig. 8.4 and practice figure (a) share the same line set (both diagonals, the half-side segment, the quarter with its four small squares); the book never says which lines matter, so all are drawn as printed.
- Practice answer (b) calls the shaded part "the red shaded part" but the page shows orange-brown hatching.
- Fig. 8.7 prints no fractions; the four paths leaving the third point were verified at 4x zoom (2 to Mango, 1 up to the fourth point, 1 long path to Sugarcane).
- The pdf has printed answers on pages 31-39 (the brief says none); I used them only to check that the printed answers of these questions are text.
