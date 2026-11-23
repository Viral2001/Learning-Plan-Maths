# Chunk F notes (Class 6 Ch 5 "Prime Time", live plan cbse_eng_maths6_ch5_v75)

Units: M4.S27.T27 to M4.S33.T33 (15 units, 27 items). Result: required 9 / optional 0 / none 18. Validator: errors 0, 4 warnings
(the four prime-puzzle solution diagrams have no printed book figure: the book prints no answers for 5.6, so the warning is expected).

Decisions in short
- Only the prime-puzzle material is drawn: the T32 worked example (1 diagram) and the four T33 puzzles (4 question + 4 solution diagrams).
- FiO 5.5 Q1, Q2, Q5, Q6, Q7 and the Divisibility by 8 items (q19 to q22) are text/LaTeX on both sides: the book prints no figure for any of them
  and every printed answer is text.
- T31 Special numbers (5.6.q1): none.
- All 15 puzzle diagrams use the house tokens (grid cells BG with INK outline, six clue cells MARK_FILL, filled primes in ANSWER green), 16:9.

## 1. Judgement calls

1. M4.S31.T31.C179 worked example (5.6.q1, the box 9, 16, 25, 43): none (NUMBER_LIST_IN_BOXES + OPEN_ENDED). The LP question text already lists the four
   numbers, position in the box means nothing, and the task is open-ended. The same box is the kept teaching image C179.IMG1 (never linked), so base figure
   P20-cell_grid-1 is accounted as `concept_image:M4.S31.T31.C179.IMG1`. A reviewer who wants the box drawn would have to call it `optional`, not required.
2. M4.S32.T32.C181 worked example (5.6.q3, "the figure on the left shows the puzzle ... on the right the solution"): required. The LP text names none of the numbers,
   so the learner cannot attempt "what can the rules be?" without the pictures. One worked item takes one diagram, so the left (empty) and right (solved) book
   figures are drawn side by side in ONE 16:9 image; both book figures map to this item (two inventory entries, P21-product_puzzle-5 and -6). The right figure is
   in INK (it is given in the book), not ANSWER green. media_id is `M4.S32.T32.C181.IMG2` because C181.IMG1 is a kept teaching image. That kept image is a
   different 2 by 2 puzzle (6, 10 / 10, 6), not the book's 3 by 3 figure, so it does not stand in for the book figure.
3. M4.S33.T33 puzzles 1 to 4: question and solution required for all four (sibling consistency). The LP text gives every clue number, so a very strict reading
   could say "text is enough", but the task is to FILL a given grid whose layout (row clue to the right of each row, column clue below each column, no corner cell)
   defines the puzzle, and the answer is the completed grid (ANSWER_IS_FIGURE). Solution diagrams are derived_from the question diagrams. Puzzle 2 (8, 105, 70 / 30, 70, 28)
   is also the kept teaching image C182.IMG1; it still gets its own question and solution diagrams (v3: a teaching image is never linked).
4. Four Math Talk boxes on pdf page 21 (5.6.q2: 5, 7, 12, 35 / 3, 8, 11, 24 / 27, 3, 123, 31 / 17, 27, 44, 65): the LP has no unit for them (see 2.5). The four
   base figures P21-cell_grid-1 to -4 are accounted as `none:NUMBER_LIST_IN_BOXES` (open-ended, positions carry no meaning).
5. FiO 5.5 Q3 and Q4 (and the printed answer table SOL33-table-1, remainders for 78 ... 2345) sit in chunk E (M4.S24.T24); SOL33-table-1 is the printed answer of Q4, so
   it is not claimed here. If both chunks claim it, the plain table should mean `none:LATEX_TABLE`.
6. FiO 5.5 Q5 (14560): the LP answer is "5 and 8" (the book's). 8 and 10 would also be a correct pair (8 covers 2, 4, 8; 10 covers 2, 5, 10), so "what could those two numbers be" has more
   than one answer. Not a diagram matter; left as is.

## 2. Things in the LP that look wrong or odd

1. M4.S27.T27.C159 (Q1): the question text repeats both parts: "(a) ... (b) ... (a) ... (b) ..." (question and question_tex). Part (a) is repeated word for word.
2. M4.S29.T29.C171 (Q3 statements): question text repeats the three statements in a short form after the long form ("1) Only the last three digits matter 2) If last three digits divisible by 8 then number is 3) ...").
3. M4.S27.T27.C162 (FiO Q2): the LP answer 8888 and 2112 is right (8888 / 4 = 2222, 2112 / 4 = 528; palindromes abba need 10b + a divisible by 4 with a even). The book's printed answers 9999 and 1001 are
   odd numbers, so the LP is right and the book is wrong (the LP already says so).
4. Book numbers are not the LP numbers: T30's three questions are labelled "Figure it Out 5.5, Q1, Q2, Q3" (book_number) but ncert_refs say 5.5.FiO.Q5, Q6, Q7 and the book numbers are 5, 6, 7 (pdf page 20).
   T27 is labelled Q1 and Q2 and matches the book. The T29 items (q20 to q22) are unnumbered bullet questions in the book, labelled by topic in the LP.
5. Content missing from the LP: the Math Talk of four boxes (5.6.q2, pdf page 21, text: "Below are some boxes with four numbers in each box. Within each box try to say how each number is special compared to the rest ...") is not
   in any unit (T31 stops at C180 "Practice: Special reasons", a recap).
6. M4.S32.T32.C181 (worked example): the question text refers to "the figure on the left" and "the figure on the right" but states none of their numbers; the steps say "Rule (given next in the book)". The diagram fixes the missing data;
   no text sync is needed, but the later FiO text should not repeat the figure's numbers differently.
7. M4.S28.T28.C165 teaching plan says "8560 itself works" (560 = 8 x 70), while the book answer and C170 give 8552. Both are multiples of 8 (8552 = 8 x 1069); 8552 is the one that actually changes the last two digits. Not a diagram issue.

## 3. Where the book itself is unclear

1. The base inventory descriptions of all figures of this chunk (P20-cell_grid-1, P21-cell_grid-1 to -4, P21-product_puzzle-5 to -8, P22-product_puzzle-1 and -2) were checked against the page pictures (pdf pages 20, 21, 22) and are correct.
2. The book prints no solution for any 5.6 puzzle (the solutions section ends at 5.5), so the four completed grids come from the LP. Each was recomputed: all row and column products match the clues, all entries are prime, and each puzzle has a unique solution.
   Checked products: puzzle 1 rows 105, 20, 30 / cols 28, 125, 18 (grid 7 5 3 / 2 5 2 / 2 5 3); puzzle 2 rows 8, 105, 70 / cols 30, 70, 28 (2 2 2 / 3 5 7 / 5 7 2); puzzle 3 rows 63, 27, 190 / cols 45, 42, 171 (3 7 3 / 3 3 3 / 5 2 19); puzzle 4 rows 343, 66, 44 / cols 28, 154, 231 (7 7 7 / 2 11 3 / 2 2 11).
3. The book colours the nine grid cells pale mint and the clue cells orange-yellow; the diagrams swap them for the house tokens (grid cells white, clue cells MARK_FILL), as the style table requires.
