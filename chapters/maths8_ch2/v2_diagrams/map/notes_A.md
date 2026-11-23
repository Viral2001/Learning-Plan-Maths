# Chunk A notes: Class 8 Ch 2 "Power Play" (plan cbse_eng_maths8_ch2_v35)

Units: 17 (3 worked examples, 14 pairs) = 31 items. Result: required 2 / optional 0 / none 29. Validator: errors 0, warnings 0.
Only the Stones that Shine tree needs a diagram: question M3.S8.T8.C32 (media M3.S8.T8.C32.IMG1) and solution M3.S8.T8.C33 (M3.S8.T8.C33.IMG1, derived_from the question figure).

Note on the brief: it says the pdf has no printed-solutions section. It does: pdf pages 30 to 38 are the NCERT answers (Page No. 22 ... 45). I read them against my units. All of their answers are text; none has a picture (the only answer pictures in the pdf are P33 and P34, which belong to other chunks). The LP solution text was still the one followed.

## Judgement calls

1. M3.S8.T8.C32 question (required). The LP text says only "In the story, find ...". The story's branching (king, 3 daughters, 3 baskets each, 3 keys each, 3 rooms each) is what the book's tree shows (P05), and the learner counts the rooms from it, so FIG_REFERENCED + DATA_IN_FIGURE. The tree stops at the rooms level; the tables, necklaces and diamonds of the story are not in the book's picture and are not drawn. I checked the base description against a zoomed crop of page 5: 3 keys under each of the 9 baskets (27 keys), each key has 3 prongs (27 fork icons x 3 = 81 rooms). The base `unclear` doubt (is an icon one room or three) is settled by the picture: one icon = 3 prongs = 3 rooms.
2. M3.S8.T8.C33 solution (required). The solution counts level by level (3, 9, 27, 81). The complete final state is the same tree with those four counts in ANSWER green, before step 1. The 2187 diamonds come from the text, not from the picture. Used two inventory entries for the one book tree: P05-tree_diagram-1 (question) and NEW-P05-tree_diagram-1-sol (solution).
3. Diagram type `other` (a plain branching tree; the catalogue has no tree type that fits). Layout is given by unit coordinates (x formulas: rooms x = k, keys 3j-1, baskets 9i-4, daughters 27d-13, King 41) so the renderer cannot guess; all positions were recomputed in code (each parent is at the mean x of its 3 children).
4. The book's tree has coloured panels, daughter faces, baskets and keys as pictures. The spec uses plain circles and squares (no cartoon art), because the figure rule allows only what carries the maths.
5. Plain Fold/Thickness tables (P02-table-1 to 4, P03-table-1 to 3) are all LATEX_TABLE, siblings of each other. P03-table-4 (coloured header, x1024 table) is mapped to concept image M1.S2.T2.C4.IMG1 (same idea, accounting only).
6. Factorisation items (C17/C18 the 32400 item, C21/C22, C23/C24) are all `none` for the same reason (number chains = LATEX_ARITHMETIC), so the siblings agree. The book's division ladder (P04) is a worked-example teaching picture; mapped none:LATEX_ARITHMETIC.
7. Figure it Out items (C21 = book FiO Q1, C23 = Q2, C25 = Q3, C40 = Q4 of the second set, C42 = Q10): all have text answers in the book too, all `none`.
8. Book figures P06-brace_diagram-1 and P06-table-2 are teaching working; mapped to concept images M3.S7.T7.C27.IMG1 and M3.S7.T7.C29.IMG1 (accounting only, nothing linked).
9. Not added to the inventory (decoration, Step 0): the Burj Khalifa picture on page 2, the king-and-daughters art on page 5, the paper-stack art and children on page 2, the two banknote photographs on page 26 (they belong to the "Pinch of History" text, other chunk).

## LP text issues

- M1.S3.T3.C8 (question): says "using the thickness table", but the table is not in the question text and the concept image C2.IMG1 shows only the first doublings. Suggested: add the table as a LaTeX array (folds 1 to 17, and fold 0 = 0.001 cm, fold 20 = about 1048.5 cm), or at least the values the solution uses: "Fold 3 = 0.008 cm, fold 4 = 0.016 cm, fold 5 = 0.032 cm, fold 7 = 0.128 cm, fold 0 = 0.001 cm, fold 10 = 1.024 cm, fold 20 = about 1048.5 cm."
- M3.S8.T8.C32 (question): "In the story" but the story is not stated. The figure covers king to rooms only, so the rest must be in the text. Suggested: "A king had three daughters. Each daughter got three baskets, each basket had three keys, each key opens three rooms, each room has three tables, each table has three necklaces and each necklace has three diamonds. Find the number of rooms and the number of diamonds." (The book words it as a verse: "Each room had tables - one, two, three, with three bright necklaces on each ... each necklace had three diamonds".)
- M1.S3.T3.C6 (question) and M1.S2.T2.C3 (worked): "starting from about 10.4 m after 20 folds" does not give the LP's own values: 10.4 x 2 = 20.8, then 41.6, 83.2, 166.4, 332.8, whereas the steps say 21, 42, 84, 168, 336. Those come from the exact 10.485 m (1048.576 cm), which C9 uses as "about 1048.5 cm". Suggested: "about 10.5 m (10.485 m)" in C6 and C3, or keep the book's "about 10.4 m" and say "values are rounded from 10.485 m".
- Book numbers: M2.S6.T6.C23 ("Figure it Out, Q1") is book FiO Q2 (648, 405, 540, 3600); M2.S6.T6.C25 ("Q2") is book FiO Q3; M3.S9.T9.C42 ("Figure it Out, Q1") is book FiO (second set) Q10. Two different questions are both labelled "Figure it Out, Q1". Suggested labels: "Figure it Out, Q2 (first set)", "Q3 (first set)", "Q10 (second set)". M3.S8.T8.C40 "Power Play, Q4" is book Q4 of the second set (correct).
- M2.S5.T5.C21 (question_tex): the sub-part separators are uneven: "(i): ...; (ii): ... (iii) ... (iv): ...; (v): ... (vi) ...". Suggested: one style, e.g. "(i) ... (ii) ... (iii) ...".
- M3.S8.T8.C35 and C37, C39, C41 (the plain `question` field): the exponents are spelled out ("p⁴ × p to the power 6", "4 to the power 6"). Suggested: use the symbols as in `question_tex` ("p⁴ × p⁶", "4⁶", "(2⁵)²", "q⁴⁶").
- No wrong answers found: I recomputed all LP numbers of the 17 units (thickness values from 21 m to 703687 km, ratio checks 4, 8, 1024, 2^10 v, 12 and 64, 32400 = 2^4 x 5^2 x 3^4, 648, 405, 540, 3600, the six values 2000 ... -32000000, 2187 = 81 x 27 = 9 x 243, 512, 78125, 4096 both ways, 1024, the power-of-a-power forms, the sixth powers 729 and 4096). All hold.

## Borderline

- C6/C7 (fill the thickness table, folds 21 to 45): `none` via LATEX_TABLE for both sides. The answer is a filled 25-row table, so ANSWER_IS_FIGURE could be argued, but the table is plain numbers with no colour meaning, and the tie-breaker (a careful student loses nothing with a LaTeX array) says text. If the user wants it as a picture, C7 solution is the place (derived_from none, since the question side stays none).
- C8 question: the book question depends on the plain thickness table (FIG_REFERENCED could be argued, "cannot be answered without it"). Kept `none` because the LATEX_TABLE rule delivers a plain table as text, but this item needs the LP text issue above fixed to be answerable.
- C33 solution: `required` because the counts are written on the tree and the solution is built on them. It could be argued `none` (SAME_AS_QUESTION_DIAGRAM + numbers in text). Kept required: the picture shows the final state with the new marks.
- C17/C18, C23/C24 factorisation ladders: a prime ladder would help, but the divisions are a number chain already in the steps (v3: LATEX_ARITHMETIC). Not made `optional` so that no ladder is requested for the four sub-parts of C24.
- C3 worked example: a height scale (670 m against 830 m, 10.7 km against 11 km) would be nice, but the plan already has it as teaching image C3.IMG1 (never linked), so `none`.

## Book doubts

- Page 2 and page 3: fold 20 is printed "about 10.4 m", the exact value is 10.4858 m (the book truncates). The LP mixes "about 10.4 m" (C3, C6) and "about 1048.5 cm" (C9).
- Page 3, table "Times increased by", row 2: "10.485 m - 1.024 cm = about 10.474 m". Exactly 10.485 m - 0.01024 m = 10.4748 m, so the book truncates instead of rounding (10.475). Not drawn (teaching table).
- Page 5, under the tree the book prints 3 x 3 = 9, 9 x 3 = 27, 27 x 3 = 81 and a fourth line 81 x 3 = 243. The fourth line is not a rooms count (the rooms are 81 = 3^4); 243 = 3^5 is the stepping stone to the diamonds (9 x 243 = 2187). The diagram follows the four levels only (3, 9, 27, 81).
- Page 5, tree picture: the picture shows rooms as 27 fork-like icons of 3 prongs; the book never says one prong is one room. The text (3^4 = 81 rooms) fixes it.
- Page 35, FiO Q4 (i): the printed reason says it holds "for numbers that have powers as 6" (n^6 = (n^2)^3 = (n^3)^2); the LP uses the counter-example 8 against 64. Same verdict (only sometimes true); the LP wins.
