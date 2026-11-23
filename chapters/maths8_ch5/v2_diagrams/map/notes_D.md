# Notes, chunk D (Class 8 Ch 5 "Number Play", live plan cbse_eng_maths8_ch5_v36)

Chunk D = M2.S26.T26, M2.S27.T27, M2.S28.T28, M2.S29.T29, M3.S31.T31, M3.S32.T32, M3.S33.T33.
Result: 33 items (15 question, 15 solution, 3 worked example): **required 0 / optional 1 / none 32**. Validator: errors 0, warnings 0.
No new media id is created and no LP id is dropped (`new_media_ids_created` and `lp_ids_dropped` are empty).

Why nothing is required: this chunk is the divisibility-puzzle part of the chapter (Figure it Out Q5/Q8/Q10, Digital Roots, Digits in Disguise, Q15, Navakankari). The book prints no figure with any question or answer here, except (a) the column-addition layout of the four addition cryptarithms (typeset arithmetic, so LaTeX by the v3 "column addition" rule) and (b) decorative art. Every question states what it gives in words, every answer is numbers or reasoning.

Figures claimed (12, all `none` or a concept image, none maps to an item):
- P19-illustration-1, P30-illustration-2 (Digital Root Club cartoon, page art and its reprint beside the riddle answer): `none:DECORATIVE_ONLY`.
- P20-cryptarithm-1..4 (the four addition cryptarithms given in the question) and P31-cryptarithm-1..4 (the same four reprinted on the answer page, letters not replaced by digits): `none:LATEX_ARITHMETIC`. The P31 reprints are not `SAME_AS_QUESTION_DIAGRAM` because the question side has no diagram either.
- P30-table-1 (printed answer of the "add 11" question: two columns of equations 10 -> 1+0 = 1 ... 120 -> 3): `none:LATEX_ARITHMETIC`.
- P24-board-1 (Navakankari board with 9 + 9 pawns): `concept_image:M3.S33.T33.C152.IMG1` (accounting only, the board-and-goal teaching image already in the plan).
- Not claimed on purpose: P23-venn-1..4 and P37-venn-1..4 belong to Figure it Out Q16 (FiO4.q16 = M1.S12.T12.C44, another chunk). P17/P18/P29 (shortcut for 11, divisibility table) belong to the 5.2 shortcut topics (another chunk). Cartoon characters (Guna, Anshu, the owl and the children on the Puzzle Time page) are pure decoration (Step 0 skips them), so no `NEW-` figure was added.

All base descriptions of the figures above were checked against the page pictures (pp.19, 20, 24, 30, 31); they are right. Only the P19 picture got extra words in its inventory description (see "Book unclear").

## 1. Judgement calls

- **Addition cryptarithms C139/C140 (book p.20 (i)-(iv), reprinted p.31):** question `none` (LATEX_ARITHMETIC, TEXT_SUFFICIENT). The LP question already writes each puzzle as an equation, and the v3 prompt sends column addition to LaTeX. Solution `none`: the printed answer is only text ("A = 7, B = 9" ...) and the LP answer is solved sums written in LaTeX. `text_alternative` on both tells the text side to use a LaTeX array column addition.
- **Multiplication cryptarithms C141-C150:** all `none`, one-line equations, no figure in the book. Same decision for every one of them (sibling consistency inside Digits in Disguise and FiO Q15).
- **C129 solution (FiO3.q2, "add 11"):** the book's printed answer sits in two columns under a vertical rule, which looks like a table picture, but it is plain equations (10 -> 1+0 = 1 ...). Judged text/LaTeX. The LP answer uses a different start (5, 16, 27, 38, 49, 60 instead of 10, 21, 32 ...); the LP wins and is right (roots 5, 7, 9, 2, 4, 6).
- **C117 and C119 (worked examples):** `none`. Number chains and two plain sequences; the teaching images of both concepts (reduction chain, 7-4-1 ring) stay as they are and are never linked.
- **C122/C123 (600 to 700):** `none` on both sides. The solution is three lists of eleven numbers; a number line would only repeat what the list says, and the root-5 "+9" picture already exists as a teaching image (M2.S27.T27.C118.IMG1).
- **C124/C125 (riddle):** `none`. The Digital Root Club cartoon beside the riddle is decorative; the answer is one number.
- **Open questions (C113, C115, C128, C132):** question side `none` (OPEN_ENDED, TEXT_SUFFICIENT); the solutions draw nothing because there is no figure to give.
- **Book numbering vs LP numbering:** the LP calls M2.S26.T26's questions "Figure it Out, Q1-Q3", M2.S29.T29's "Q1-Q3" and M3.S32.T32's "Q1", while the book numbers are 5.3 FiO Q5, Q8, Q10; digital-root FiO Q2, Q3, Q4; 5.3 FiO Q15. I matched items to the book by their text, not by the LP number.

## Borderline

1. **C139 / C140** (addition cryptarithms in the book's column layout): none, but a reviewer could argue ANSWER_IS_FIGURE (a solved column addition). I applied the v3 rule as written (column addition is LaTeX). If the user wants pictures here, it is four question figures (one per puzzle) plus solved columns, which also would hit C148.
2. **C148** (six solved multiplications): none, same reasoning.
3. **C152 Navakankari worked example:** `optional` rather than `none`. A small picture (three connected board points on one line, two partner pawns on the first two, the third empty, my blocking pawn in ANSWER green) would clearly help, but the scenario is stated fully in words and the answer is one move, so by the tie-breaker the text is enough. Not added.
4. **C129 solution:** the printed answer looks like a two-column table (see above); judged text.
5. **C117, C119, C122/C123, C125, C127:** a teaching picture exists for each concept, which is never linked. Their decision does not rest on that; each is text/LaTeX because the content is plain numbers.

## 2. LP text issues

No LP text was edited. Each item below: concept id, what is wrong or missing, suggested sentence.

- **M2.S26.T26.C112** (steps_tex step 4, answer_tex, text): the LaTeX is cut in the middle of each pair, so it will render oddly: `gives $(1$, $0)$`, `($a$, $b) = (1$, $0)$, $(2$, $8)$ ...`. Suggested: "$a + b = 1$ with $b$ even gives $(a, b) = (1, 0)$; $a + b = 10$ with $b$ even gives $(2, 8)$, $(4, 6)$, $(6, 4)$, $(8, 2)$." and answer "$(a, b) = (1, 0), (2, 8), (4, 6), (6, 4), (8, 2)$".
- **M3.S31.T31.C139** (question_tex): `$A_1 + 1B = B_0$` writes the digits as subscripts (A with a small 1), which reads like indexed variables, not the two-digit numbers A1, 1B, B0. Suggested: "Solve the cryptarithm $A1 + 1B = B0$ (each of A1, 1B and B0 is a 2-digit number)." Same slip in **M3.S31.T31.C147** (`$L_2N \times 2 = 2NP$`, should be `$L2N \times 2 = 2NP$`, three digits L, 2, N) and in **M3.S32.T32.C150** step 4 (`$5O_5 \times 5$`, should be `$5O5 \times 5$`).
- **M3.S32.T32.C150** (step 3): the math is split by the bracket: `so $W$ is $5 (W$ cannot be $0$ as a first digit).` Suggested: "so $W$ is $5$ ($W$ cannot be $0$ as a first digit)."
- **M3.S31.T31.C139 / C140** (second block): the LP labels the other three puzzles (i), (ii), (iii) (AB + 37 = 6A, ON + ON + ON = PO, QR + QR + QR = PRR); in the book they are (ii), (iii), (iv) because A1 + 1B = B0 is (i). Suggested: relabel them (ii), (iii), (iv) in the question and in the answer lines.
- **M2.S28.T28.C124 / C125** (riddle, missing data): the book asks "What's my number? What's my name?" and its answer gives both the number and its name in the Indian system ("11,11,11,111, Eleven crore eleven lakh eleven thousand one hundred eleven"). The LP question stops at "solve the riddle" and the answer gives only 111111111. Suggested: add "What is the number, and how do we read it?" to the question, and to the answer "$111111111$, read as eleven crore eleven lakh eleven thousand one hundred eleven ($11,11,11,111$)".
- **M2.S29.T29.C133** (step 1, weak example): 10 (even, root 1), 11 (odd, root 2), 12 (even, root 3) all show the parity of the root flipping, which does not show "no fixed link". Suggested: "$10$ and $20$ are both even, but their digital roots are $1$ (odd) and $2$ (even); so the parity of a number does not decide the parity of its digital root."
- **M3.S31.T31.C148** (missing eliminations): (v) lists P = 2, 3, 4 with Q = 1 but never says why P = 1 and P = 5 to 8 are out. Suggested: "$P = 1$ would make $P$ and $Q$ the same digit, and $P = 5, 6, 7, 8$ give $605, 726, 847, 968$, whose first digit is not $P$." In (i), after "$T = 0$" add "$3 \times U$ must end in $U$, so $U = 5$ (since $U \ne T$)".
- **M3.S31.T31.C146** (steps 3 and 4): $6 \times E$ ending in $Y$ also allows $E = Y$ ($E = 0$ for $Y = 0$, $E = 2$ for $Y = 2$, $E = 4$ for $Y = 4$); the LP names only $E = 5$, $7$, $9$ for those. Suggested: add "(the other choice $E = Y$ would use one digit for two letters)".
- **Labels:** "Figure it out: Q1" is the name of three different concepts (M2.S26.T26.C111, M2.S29.T29.C128, M3.S32.T32.C149), and M2.S28.T28.C126 is named "Digital Roots: Q3" while its `book_number` is "Digital Roots, Q1". The text of each question is right; only the labels collide. Suggested: use the book's own numbers (5.3 FiO Q5, Q8, Q10, Q15; digital-root FiO Q1 to Q4).
- **M3.S33.T33.C152** (worked example): "your partner completes a line of three next turn" is a placing-phase situation, while the book's rules (p.24, rule 2) describe lines being made by moving pawns after all are placed (rule 1 only talks about placing). The LP answer is consistent with rule 3 (a completed line removes a pawn). Suggested: begin the question with "While you are still placing pawns, ..." if the content team wants it to follow the standard game; otherwise leave as is.

## 3. Places where the book itself is unclear

- The brief says the pdf has no printed-solutions section, but pdf pages 25 to 37 are printed answers ("Page No. 122" onward). I used them only to cross-check the LP answers; the LP text was followed throughout.
- **Digital Root Club picture (p.19, reprinted p.30):** the members' numbers are 10000000, 100, 10584, 37, 1000, 1 and the people kept out are 1001 and 110. If the club is "digital root 1", then 10584 (digit sum 18, root 9) does not belong, so the art is inconsistent. It is decorative and no item uses it, so nothing changes. The exact number of zeros in 10000000 (about seven) is also unclear.
- **Printed answers with fewer solutions than the LP** (the LP is mathematically right and wins): ON + ON + ON = PO has three solutions (17, 24, 31 giving 51, 72, 93), the book prints one (N = 1, O = 3, P = 9); L2N x 2 = 2NP has 124 x 2 = 248 and 125 x 2 = 250, the book prints one (L = 1, N = 5, P = 0); PP x QQ = PRP has 22 x 11 = 242, 33 x 11 = 363, 44 x 11 = 484, the book prints P = 2, Q = 1, R = 4 only. I recomputed every solved sum of C140, C142, C144, C146, C148 and C150 and all hold.
- Print slips in the answers: "hudred" for "hundred" (riddle answer, p.30). The book's example 40000001 (FiO Q1, digital roots) is a valid 8-digit number with root 5; the LP uses 10000004, also valid.
- All figures in this chunk are text-based or decorative, so no book picture needed a corrected value (user decision 1 never applied).
