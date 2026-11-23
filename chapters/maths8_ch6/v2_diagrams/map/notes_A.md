# Notes for chunk A (Class 8 Ch 6, cbse_eng_maths8_ch6_v32)

Chunk A = topics M2.S3.T3, M2.S4.T4, M2.S5.T5, M2.S6.T6, M2.S7.T7, M2.S9.T9: 15 units, 29 items (14 pairs and 1 worked example).
Result: required 2 (question C10, solution C11), optional 1 (solution C38), none 26. Validator: errors 0, warnings 0.
Output file: `map/out_A.json`. Builder script (kept outside HERE): scratchpad `build_out_A.py`.

Only one picture in the whole chunk is something a learner needs: the Figure it Out Q1 multiplication grid (book p.7, answers p.25). Everything else is algebra or arithmetic that the text and LaTeX carry fully, and no question of the chunk is given with a figure.

## 1. Judgement calls

- **M2.S3.T3.C10 (question) required, M2.S3.T3.C11 (solution) required.** Book Figure it Out Q1 (printed page 142). The question says "Observe the multiplication grid" and "as shown in the figure": the 10 x 10 table, the outlined 3 x 3 block (rows 3-5, columns 5-7, middle 24 = 4 x 6), its enlarged form 3 x 5 ... 5 x 7 and the empty frame with pq in the middle exist only in the picture (FIG_REFERENCED, DATA_IN_FIGURE, ACTION_ON_FIGURE). The printed answer ("Ans. Observe grid.") is the same frame filled with the nine expressions; the LP solution gives the same nine in words. Rule B2 (filled figure, ANSWER_IS_FIGURE): solution required, `derived_from` = C10.IMG1, same layout, the eight added cells in ANSWER green, pq stays INK. Aspect ratio 16:9 as the brief says (the book picture is about 2:1; the grid is drawn 836 px square on the 1080 px height, the two 3 x 3 frames on the right).
  - The book's yellow header cells and pink corner cell are drawn CELL_FILL, its red frame FOCUS, its black dashed connectors GUIDE (no red in the token table).
  - The question diagram shows exactly what the book gives (grid, block, enlarged example frame, empty pq frame) and nothing of the answer.
- **M2.S9.T9.C38 (solution) optional, not added.** See Borderline 1.
- **M2.S4.T4.C12 worked example none.** See Borderline 2.
- **All other 25 items none.** Questions: `TEXT_SUFFICIENT` (the question gives numbers or expressions and no figure). Solutions: `LATEX_ARITHMETIC` (expansions, identity checks, carry steps, one-line products; the book prints text for every answer except the two pictures above). Teaching images (concept images C2-C4, C12-C16, C31-C34 of this module) are never linked.
- **C6/C7 (two blocks sharing one card).** One decision per side covers both blocks (none): the extra block "both numbers up by 1 / one up, one down" has no figure either. The question text field in the map joins the two block questions with " || ".
- **Figure inventory (20 base figures, none missing, no NEW- figures).** Page 1 has only the chapter-opening art, pages 5, 6 and 24 hold text and equations only. Mapping choices:
  - Equation displays with arrows that a teaching image already shows: P02-annotated_expression-1, -3 and P02-dot_array-2 -> concept image M2.S2.T2.C2.IMG1; P03-annotated_expression-1 -> C3.IMG1; P03-annotated_expression-2 -> C4.IMG1; P04-dot_array-2 -> M2.S4.T4.C12.IMG1; P08-column_addition-1 and P09-step_sequence-1 -> M2.S8.T8.C31.IMG1; P26-column_addition-1 -> M2.S8.T8.C34.IMG1 (accounting only, nothing linked).
  - Displayed equations or letter column-additions with no matching teaching image: `none:LATEX_ARITHMETIC` (P02-annotated_expression-4, P04-annotated_expression-1, P08-column_addition-2, P09-column_addition-2, P26-column_addition-2, P27-column_addition-1, P27-column_addition-2).
  - P07-table-1 is the first use of the grid figure (-> C10 question). The answers page reprints it as P25-table-1 and P25-table-2 (same picture): mapped to the same item C10 (question). P25-table-3 (the filled table) -> C11 (solution).
  - P26-column_addition-2, P27-column_addition-1, P27-column_addition-2 are printed answers to "What could be a general rule ... 101 / 1001 / 10001". The LP has no question for these general rules (it asks 3874 x 101, 89 x 101 ...), so no item exists to attach them to; I used `none:LATEX_ARITHMETIC`. Self-check 0 of the prompt asks that printed-solution pictures map to a solution item, a concept image or SAME_AS_QUESTION_DIAGRAM; for these three that is impossible without an LP question.
- **Sibling consistency.** C28, C22, C24, C20 (expansions) all none; C36, C40, C42 (one-line products) all none; C38 differs only because the book prints a picture for part (ii). Reason stated in the item.

## 2. Borderline

1. **M2.S9.T9.C38 solution (Evaluate 94 x 11 ... 4791256 x 11): optional, not added.** The book answer page 26 prints a hand-style carry layout for part (ii) only ("Try other parts"): digits 4 9 5, two arcs, two circled carry 1s, "x 1 1", a rule, "(4 + 1) 4 4 5", "= 5445", notes "5 + 9 = 14", "9 + 4 = 13 + 1 = 14". Rule B2 says a printed picture answer is `required`; Step C names column arithmetic as LaTeX. I treated it as an arithmetic carry layout (the base inventory also says "LaTeX-able") and chose optional because: the LP steps state every sum and carry of all four parts, teaching images C31 and C34 show the same one-line picture, and one picture would cover only one of four sub-answers. If you want it drawn, it becomes a `required` solution (no question diagram, `derived_from` null) of one layout: INK digits 4 9 5, FOCUS arcs 4-9 and 9-5, circled 1s, ANSWER row (4 + 1) 4 4 5 and "5445". Decision for you.
2. **M2.S4.T4.C12 worked example ("use the four parts"): none.** The four-part rectangle is already the kept teaching image M2.S4.T4.C12.IMG1 of this same concept (book p.4 dot array), the four parts ab, mb, an, mn are named in the steps and every number is in the words. No v3 trigger applies; a new drawing would repeat the teaching image. If you prefer a drawing, spec it as 25 x 32 split into 23 x 27 = 621, 23 x 5 = 115, 2 x 27 = 54, 2 x 5 = 10.
3. **M2.S3.T3.C11 solution: required although the printed answer looks like a plain table.** The nine expressions could be a LaTeX array (LATEX_TABLE), but they complete the empty frame of the question figure, which is `ANSWER_IS_FIGURE` / `ACTION_ON_FIGURE`.
4. **M2.S3.T3.C6/C7 and M2.S5.T5.C17/C18: none.** An area-model rectangle (23 by 27 plus one column; 10 by 10 with a 3 by 4 corner removed twice) would help, but the data is all in words, no printed figure belongs to these questions and teaching images (M2.S2.T2.C2-C3, M2.S4.T4.C13) already show it.
5. **P26-column_addition-1 mapped to concept image C34** (same layout, other number) rather than to an item, because C38's solution is not required.

## 3. LP text issues

(No LP text was edited and no decision changed because of these.)

- **M2.S3.T3.C10** (question): the text says "Observe the multiplication grid" but never says what the grid is; the table exists only in the figure. Suggested sentence: "Observe the $10 \times 10$ multiplication grid below (the cell in row $i$ and column $j$ holds $i \times j$). The $3 \times 3$ frame outlined in it is shown enlarged beside it, next to an empty frame whose middle number is $pq$." The example in the LP omits the middle row $4 \times 5$, $4 \times 6$, $4 \times 7$ (not wrong, just short).
- **Book numbers.** C10 is labelled "Distributive Property, Q1" and C19 "Distributive Property, Q2" but both are Figure it Out Q1 and Q2 (book pp.142-143); C25, C27, C29 are labelled "Figure it Out, Q1/Q2/Q3" but are book Q3, Q4, Q5 (their ncert_refs FiO1.q3, q4, q5 are right). Suggest "Figure it Out, Q1" ... "Q5" for all six.
- **M2.S3.T3.C9** step 1: "which is negative when a is at least $b$": the letter a is not in math mode; suggest "$a$ is at least $b$".
- **M2.S6.T6.C22** last step: "No two of $a^2$, $ab$ and a have the same letter-numbers": suggest "$a$".
- **M2.S7.T7.C28** steps 3 and 6: "So (i): is $...$." and "So (ii): is $...$." have a stray colon; suggest "So (i) is $4a + 5ab + ab^2 - 12b^2 - 3b^3$." and "So (ii) is $4y^2 + 44yz - 5y + 77z - 21$."
- **M2.S5.T5.C20** answer_tex: semicolons are missing after (ii), (iii) and (v): "(ii): $10 + 4a$ (iii): ... (iv): ...; (v): ... (vi): ...". Suggest a semicolon after every part.
- **M2.S4.T4.C12** (worked example): the block has only plain text (`question`, `steps`, `answer`) and no `question_tex` / `steps_tex`, unlike the other blocks; suggest LaTeX versions, e.g. "$23 \times 27 = 621$. Use the four parts to find the product when $23$ grows by $2$ and $27$ grows by $5$."
- No answer in the chunk contradicts the book. Every LP number was recomputed: 644, 648, 51, 3, -28, 104, 42, 800 (increase 179), 27 = 27, (1,6) (2,8) (3,10), 42614, 62458, 1034, 5445, 36069, 52703816, 391274, 8989, 95849, 266096831, 1112111, 963666, 23454522.

## 4. Where the book itself is unclear or slips

- **Chapter p.2 (P02-annotated_expression-4):** "a (b + 1) = ab x [a]" is printed with a multiplication sign; it must be a plus sign (ab + a). Teaching figure only, nothing is drawn from it.
- **Chapter pp.8-9 (P08-column_addition-2, P09-column_addition-2):** the zero digits of the letter layouts are printed as the letter o ("d c b a o", "d c b a o o"); the answers pages print a proper 0 (P26/P27). Teaching figures only.
- **Answers p.24:** the printed answer to "Will the product always increase? Find 3 examples where the product decreases" uses (a - 1)(b - 1) < ab (a = 10, b = 3: 18 < 30), but the question is about (a + 1)(b - 1). The LP solution (C9) answers the question as asked, which is right.
- **Answers pp.26-27:** the printed answers to Evaluate (i) to (iv) and to the 101/1001 questions are partial ("Ans. (ii)", "Try other parts", "(iii)" and "(v)" only); the LP gives all parts.
- **Chapter p.7 vs answers p.25:** the grid figure is the same on both pages; the answers page splits the "enlarged frame" and the "empty frame" visually but they are one figure (kept as one diagram).
