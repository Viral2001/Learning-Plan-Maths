# Chunk B notes (Class 7 Ch 15 "Finding the Unknown", topics M2.S7.T7 to M2.S12.T12, units 21-36)

Result: 27 items (11 questions, 11 solutions, 5 worked examples): required 0, optional 0, none 27. Validator: errors 0, warnings 0.
Nothing in this chunk needs a drawn diagram. The chunk is equation solving (trial and error, "do the same to both sides", moving a term across); every item is an equation, arithmetic or a plain list of numbers that LaTeX carries. The only figures printed in the book for these units are the machine strips (Chapter Exercises Q4, Q5) and two boxed comparison tables (p.10).

## 1. Judgement calls

1. Machine questions: M2.S7.T7.C44 (Q4 a), C46 (Q4 b), C48 (Q5), question side = none (TEXT_SUFFICIENT + REUSES_CONCEPT_IMAGE). This is the one real decision in the chunk.
   - Why none: the LP question text already states each machine completely in words, with the sample line (12 -> 15 -> 60 -> 55; 12 -> 36 and 15 -> 21) and the outputs (43 and 75; 63 and 227; 5 and -11). By the tie-breaker a careful student loses nothing without the strips. The v3 Step B2 "refer picture" case does not apply (the LP text names no figure).
   - The same strips already exist as teaching images of the previous topic: M2.S6.T6.C37.IMG1 (Chain Machines: Q4 a strips and the two Q5 machines) and M2.S6.T6.C37.IMG2 (Two-Path Machine: Q4 b). They are never linked (v3), and the v3 prompt's own "not a diagram" list says a procedure flow already drawn as a concept image is none with REUSES_CONCEPT_IMAGE.
   - If the user wants a machine strip next to each question anyway, the three questions are the ones to flip to required (diagram_type arrow_map / flow, 16:9; Q4 a = the 12-example strip plus the two "?" strips for 43 and 75; Q4 b = the two-path loop with the 12 example plus "?" for 63 and 227; Q5 = two strips). The solutions would then be derived_from the question diagrams with the inputs 9 / 17, 33 / 115, 45 / -3 in ANSWER green.
2. Machine solutions (C45, C47, C49) = none: the answer is two numbers; the LP steps undo the operations in order and check. A filled strip would only repeat the chain (the task rules say a solution diagram needs something visual added or a picture answer). Not optional either: the text is complete.
3. Trial-and-error tables (C39: n = 5, 10, 30, 40, 50, 49 giving 11, 21, 61, 81, 101, 99; C41: x = 1, 2, 3 giving 1, 6, 11) = none with LATEX_TABLE. Plain two-column numbers; a LaTeX array can be added in the LP text (text_alternative says what).
4. Example 1 (C51): the book crosses out + 88 and - 88 on the left. That is text with a strike mark, so none (LATEX_ARITHMETIC); write it with \cancel. Same for the crossed-out 5s in the check of 5x - 4 = 7 (C52). Both are listed in the inventory as NEW-P06-ex1-cancel and NEW-P08-check-cancel, mapped none:LATEX_ARITHMETIC. The base inventory did not list them.
5. Book p.10 boxed comparisons (C64 and C65 worked examples, base P10-table-1 and P10-table-2) = none, LATEX_TABLE: two columns of plain equation lines, no colour, shading or arrows (checked on the page picture). The LP steps already give both ways as text; a two-column LaTeX array in the LP text would keep the side-by-side layout (text_alternative says how).
6. M2.S11.T11.C62/C63 (frame an equation with no solution): question OPEN_ENDED + TEXT_SUFFICIENT, solution LATEX_ARITHMETIC + OPEN_ENDED. The sample answer x + 4 = x + 5 is an equation and a two-line argument.
7. All figures that the machine questions use are mapped `concept_image:M2.S6.T6.C37.IMG1` or `...IMG2` in the figure inventory (accounting only). If another chunk claims the same base figures with a different meaning, take this mapping as the sound one: P22-machine-1/2/3 and P23-machine-4/5 are in IMG1, P23-machine-1/2/3 are in IMG2.
8. Base figure P04-annotated_equation-1 (LHS / RHS callouts on 2n + 1 = 99, book p.4) is not claimed here: it is a teaching figure of section 7.1, and the T7 question C38 does not use it (it only asks to solve 2n + 1 = 99). It belongs to the chunk that owns the equation-introduction topic.

## 2. LP checks (everything recomputed, nothing wrong found)

Arithmetic in all LP solutions was recomputed and agrees with the book and the printed figures:
- C39: 2 x 5 + 1 = 11, 2 x 10 + 1 = 21, 2 x 30 + 1 = 61, 2 x 40 + 1 = 81, 2 x 50 + 1 = 101, 2 x 49 + 1 = 99.
- C41: 5 x 1 - 4 = 1, 5 x 2 - 4 = 6, 5 x 3 - 4 = 11; x = 2.2 gives 5 x 2.2 - 4 = 7 (and 11/5 = 2.2, the value C52 finds).
- C43: 5 x 9 - 8 = 37; 37 - (33 - 31) = 35; -3 x (-11 + (-4)) = -3 x (-15) = 45.
- C45: 4(9 + 3) - 5 = 43 and 4(17 + 3) - 5 = 75. C47: 3 x 33 - 36 = 63 and 3 x 115 - 118 = 227. C49: 45 / 3 / 3 = 5 and -3 - 4 - 4 = -11.
- C51: 13353 - 88 = 13265 (and 14593 - 1459 + 145 - 14 = 13265). C52: 11/5 check. C53: 11 x 6 - 5 = 61. C57: 6 x 7 + 7 = 49 = 4 x 7 + 21.
- C59: 3 x 15 - 10 = 35; 5 x 0 = 3 x 0; 3 x 10 - 7 = 23 = 2 x 10 + 3. C61: m = -10 gives -24 on both sides; 90 / 15 = 6. C63: x + 4 = x + 5 gives 4 = 5. C64 to C66: y = 6, y = 7, u = 90 all check.

Small things in the LP (no change made, nothing to fix before diagrams):
- Book numbers "Chapter Exercises, Q1 (a)" etc. for T7 C42/C43 and Q4 / Q5 are the end-of-chapter Figure it Out items on book pp.22-23 (they are labelled "Figure it Out", not "Chapter Exercises", in the book). The ids end.FiO1a etc. are right.
- Units C58 to C61 split the book's Figure it Out Q1 (a) to (e) over two concepts; the book numbers (a) to (e) are right.
- M2.S7.T7.C38: the item's example_id "E0" sits on a question item (ordinary).

## 3. Book unclear or odd

- Book p.23, Q5, first machine: the output box prints "+5" (a plus sign before the 5), while the second machine prints "-11". The LP, the arithmetic (45 / 3 / 3 = 5) and the teaching image all use 5. Not a diagram issue; the LP wins.
- This pdf has no printed-solutions section: the LP solution text was the answer to follow, and it agrees with every question's text.
