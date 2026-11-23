# Chunk E notes (Class 7 Ch 3, cbse_eng_maths7_ch3_v44)

Units: M3.S23.T23 (C98-C102), M3.S25.T25 (C105-C107), M4.S26.T26 (C108-C111), M4.S27.T27 (C113, C114). 14 units, 22 items.
Result: required 1 / optional 0 / none 21. Validator: errors 0, one expected warning (the one required item has no printed book figure).

## 1. Judgement calls

- **M3.S23.T23.C99 solution (Try This, 84.691 - 77.345): REQUIRED** (ANSWER_IS_FIGURE + HIGHLIGHT_MEANING). The book asks the learner to "write the detailed place value computation ... and its compact form". The expected answer is a drawn layout (digit x place value cells, regrouping arrows and circles, plus the compact column), the same kind of figure the book draws for 75.345 + 86.691 (pdf p.30). The LP steps only describe it in words, so B2 applies. The book prints NO answer for this Try This (pdf pp.50-51 jump from Math Talk to Figure it Out Q1), so the figure is built from the LP steps. The question side is `none` (the question gives no figure; the "place value form" is the answer). Media id `M3.S23.T23.C99.IMG1` (solution only, nothing else in the concept).
  - Layout I chose: left block with 4 rows (minuend by place, minuend regrouped 7x10 / 14x1 / 6x1/10 / 8x1/100 / 11x1/1000, subtrahend with minus sign, rule, difference 0 / 7 / 3 / 4 / 6), two FOCUS arrows (8 tens -> units, 9 hundredths -> thousandths), two FOCUS circles on 14 x 1 and 11 x 1/1000; right block with the compact form (crossed 8 and 9, small 7, 8, 1, 1, result 7.346). Numbers recomputed: 70 + 14 + 0.6 + 0.08 + 0.011 = 84.691; 7.346 + 77.345 = 84.691.
  - Dependency on chunk D: the book figure for the SUM (P30-place_value_addition-1, 75.345 + 86.691) belongs to D's worked example M3.S20.T20.C88 (ncert ref 3.7.detail_add) and is NOT claimed here. If D marks C88 `none`, the C99 figure is still justified on its own (the answer is a drawn layout), but D and E would then be inconsistent for the same book picture style: worth a look at merge. If D draws it, the two figures should share one look (cell text "d x place value", arrows and circles in FOCUS).
- **M3.S23.T23.C98 (cloth subtraction)**: none on both sides (TEXT_SUFFICIENT / LATEX_ARITHMETIC). The book's picture (P29-column_arithmetic-2) is a worked column subtraction before/after regrouping; that is arithmetic, not a diagram. Its addition twin (P29-column_arithmetic-1, chunk D C91) should get the same decision.
- **C100 (FiO Q2), C101 (end Q8), C102 (end Q9), C105-C107 (sequences)**: question and solution `none`. No figure in the book for any of them; the printed answers (pdf pp.51-54) are plain text. Sequences and number chains are LaTeX. The Q1 sums (chunk D) are the sibling of Q2: same decision expected.
- **C110 (bus and door)**: `none`. The book's comic (P32-comic-1, pdf p.32) is an illustration; every number is in the text. A strip of an hour cut into 10 parts of 6 minutes would help a little, but it is not in the book and the text carries it, so I did not make it `optional`.
- **C113 / C114 (history)**: `none`. P33-notation-1/-2 are inline typographic marks inside the sentences (a tiny vertical mark over a digit string, a small superscript 2 over 36), not separate pictures, and neither question uses them. I kept the base entries (not CORRECTED) but wrote in the description that they are inline.
- No `optional` anywhere: nothing "would clearly help" beyond the text.

## 2. Things in the LP that look wrong or thin

- **C99 question text** says "in the place value form and in the compact form" but never says what the place value form looks like; the book defines it only through its figure for the sum (owned by D's C88). The video/solution text should name the form (for example "each digit written as digit x place value") so the question stands alone. Not changed (out of scope).
- **C107 (end Q10)**: the book prints the question as "5.5, 6.4, 6.39, 7.29, 7.28, 6.18, 6.17" (pdf p.34, a misprint) but its printed answer (pdf p.54) re-prints it as "8.18, 8.17" and answers 9.07, 9.06. The LP uses 8.18, 8.17: correct, and the steps agree (7.28 + 0.9 = 8.18, 8.17 + 0.9 = 9.07, minus 0.01 = 9.06).
- **C109**: the LP says 22300 x 0.453 is "about 10102 kg" (exact 10101.9). Fine. "a little less than half of 22300" is true (half is 11150) but 10102 is about 45 percent; the book says "about half". Not wrong, only loose.
- **C113**: the LP says 950 CE "is in the 900s" (true, the 10th century) and puts it after the 8th century: correct.
- **C106 solution cards** list (h) in a truncated description only; the LP answer text itself is complete (all eight lines correct: recomputed (a) 4.55, 4.60, 4.65; (c) 10.89, 11.00, 11.11; (e) 11.2, 12.1, 13.0; (f) 4.85, 4.80, 4.75; (g) 10.95, 10.45, 9.95; (h) 26.0, 22.5, 19.0).
- Arithmetic of the other solutions rechecked and correct: C98 0.8; C100 (a) 3.3, (b) 9.2, (c) 5.9, (d) 0.802, (e) 16.95, (f) 16.405, (g) 0.81, (h) 5.749; C101 12.24 then 12.76; C102 1.25.
- C110/C111/C113/C114 LP text matches the book (bus 4:30 p.m., door 2 ft 6 inches, overs 5 5/6, 1,000.5 written 1 000,5).

## 3. Places where the book is unclear

- The book gives no printed solution for Try This (pdf p.30, "Write the detailed place value computation for 84.691 - 77.345, and its compact form"), so the exact drawing of the regrouping (where the borrowed amounts go) is my reconstruction in the style of the sum figure; the numbers follow the LP steps exactly.
- The book's question 10 misprint (6.18, 6.17 against 8.18, 8.17), described above.
- The book's compact subtraction in 3.7 (pdf p.29) writes the borrow as a small digit above the crossed digit and a small 1 in front of the receiving digit; I copied that style for the compact block.
