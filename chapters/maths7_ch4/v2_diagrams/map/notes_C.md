# Chunk C notes (Class 7 Ch 4, topics M2.S21.T21 to M3.S31.T31)

Result: 29 items, required 14 / optional 1 / none 14. Validator: errors 0, warnings 0.
Questions: required 8, none 5. Solutions: required 6, optional 1, none 6. Worked examples: none 3.

## 1. Judgement calls (item, choice, why)

The calls most likely to be flipped by the user are the question-side "required" ones, where the LP text restates the data but the book's figure is the activity or carries the arrangement.

- C87 question (Math Talk, 10y - 3 and 10(y - 3)): required. The LP text gives the numbers, but the book task is "fill the two star diagrams" (one box given in each) and the printed answer is the filled diagrams, so the pair is required/required (derived). If the user wants text-first, the question can drop to none and the solution then stands alone (derived_from null); the solution stays required.
- C89/C90 (Mind the Mistake table, three claim blocks): none/none, LATEX_TABLE. The book table and both printed answer tables (pp 31, 32) are plain black text, no colour. All three claim blocks share one card, so one decision.
- C91 question (FiO 4.4 Q1, tile pictures): required, one diagram holding pictures (i), (ii), (iii) left to right (the LP did not split the question into parts). No picture letters are drawn (v3 forbids figure letters); the order is the question's order.
- C92 solution: optional. The printed answer is two text methods; the tiles are only reprinted above it (P29-number_tiles-5/6/7, mapped none:SAME_AS_QUESTION_DIAGRAM). Outlining like terms in matching colours would help, but the steps already say it, so nothing is added.
- C93/C94 (FiO Q2): none/none, pure simplification.
- C97 (make a formula of your own): none, OPEN_ENDED. The book has no figure; a picture of the four model machines would only show the model answer. A LaTeX table of the four input pairs would do.
- C99/C100 and C101/C102 (Formula Detective): all four required. The book figure (rows of Y machines with empty "expression:" lines and empty results) is the object the learner completes (ACTION_ON_FIGURE), and the printed answer for C102 is a picture (P33). C100 got a solution picture by sibling consistency, although the book prints no answer picture for the first machine row (its expression is only in text). C101/C102 each hold two blocks on one card, so each side has ONE diagram with both rows (10 machines in two rows of 5). Solution draws the formula both in the last result box (as the book does) and on the "expression:" line (as the LP steps do).
- C106/C107 (Example 12 saree): none/none. The book picture is six detailed flower motifs, not renderable and decorative; "A, B, C repeat" is in the text. The A B C strip with positions 1 to 9 is already the teaching image of the topic (C103.IMG1, not linked), so the solution gets no new copy (TEXT_SUFFICIENT).
- C108/C109: none/none. Quotient and remainder table is a plain table (LATEX_TABLE).
- C111, C113 (calendar worked examples): none, no figure in the book. C111's square 9, 10, 16, 17 and C113's row a - 1, a, a + 1 are fully in the steps.
- C114 question: none (text gives the four dates and their places); C115 solution: required, the grid a, a + 1 / a + 7, a + 8 with both diagonals marked (ANSWER_IS_FIGURE: the book says the numbers "can be represented as shown in the grid"). The question has no diagram, so this one has derived_from null. The two diagonal lines run 70 px past the grid corners so that the two "2a + 8" tags sit outside the grid.
- C116 question: required (the text lists the five dates, not their places; the shaded plus shape shows which is above, below, left, right, which the proof needs). C117 solution: required (printed answer picture P33-table-1). The solution replaces 8, 14, 15, 16, 22 by a - 7, a - 1, a, a + 1, a + 7 in ANSWER green, exactly as the book's printed answer, on the same grid and shading.
- Matchsticks: C121, C123, C125 questions required (the pattern, 3 sticks at Step 1 and 2 more each step, is only in the picture; the LP texts never describe it). Same spec for the three (one diagram per item). C122 solution none (plain table, LATEX_TABLE), C124 solution none (algebra), C126 solution required: the answer is read from colour (horizontal sticks SET_A, diagonal sticks SET_B, a key, and the counts 1 and 2, 2 and 3, 3 and 4, 4 and 5 under Steps 1 to 4). Step 1 counts are not in the LP steps (it names Steps 2 to 4); they follow the picture and the rule y and y + 1.
- C125 question picture is drawn plain (all sticks INK). I did not copy the book's page 21 "yellow glow" picture: it lights only the inner slanted sticks, the book does not say why, and it has no Step 4.
- Step labels in the matchstick figures are "Step 1" to "Step 4" (the book prints only 1 to 4 under the strips), to match the question text.
- Machines are drawn without the book's gear icon and without the blue/purple/green row colours (decorative). All result boxes use MARK_FILL; the last machine of each row has a wider box so a formula fits, in question and solution alike.

## 2. Anything in the LP that looks wrong

- C93/C94 lettering: the LP has parts (a) to (l) (12 expressions) because it split the book's first line "(a) p + p + p + p, p + p + p + q" into two. The book lettering is (a) to (k) (11 lettered parts, the first holds two expressions), and the printed answer on p 31 groups the answers under six letters (a) to (f). Also the LP label of part (i) is plain text in question_tex, steps_tex and text, while the other labels are written "$(a)$" and so on in math mode.
- C124 (answer to Q2 of matchsticks) carries video_media_id "M3.S31.T31.C125.VID1", which names the concept after it (C125 is the Q3 question concept); the answer concept of Q3 (C126) has no video. Looks like an off-by-one in the video ids.
- C107 step 4 repeats the C positions 3, 6, 9 already given in step 1.
- C121/C123/C125 question texts do not state what the pattern is (3 sticks at Step 1); they only work with the picture. Fine with the new diagram, but the old no-picture version would be unanswerable.
- C116 question text lists the five dates without their places; fine with the diagram.
- C88 order of values: LP replaces y by 2, 10, 0, 7; the book's diagram order (upper left to lower right) is y = 2, 0, 10, 7. The diagram follows the book, the steps follow the LP; both are correct, only the order differs.
- C101 (hint q_figure/s_figure) writes the product machine as "ab + 1"; the book's printed box reads "a x b + 1" and the LP steps say "a x b + 1, written ab + 1". The diagram uses "a x b + 1" (book).
- C100 s_figure hint says the figure shows "2 x 5 - 2 = 8" under each machine; the diagram writes the expression only (the result is in the result box).

## 3. Where the book itself is unclear

- Printed answer row 4 of the Mind the Mistake table (p 31) reads "x + 5" in the "Simplest Form" column, while the question page (p 14) and the LP say "x + y". Corrected answer column reads x - y in both. LP is right.
- Book FiO Q2: question lettering (a) to (k) with two expressions under (a), but answers grouped as (a) to (f) on p 31 (see section 2).
- P21-pattern-1 (matchstick page 21): the yellow glow lights only the inner slanted sticks (checked on an enlarged crop); the text does not say what the glow marks. Not used.
- Page 32 prints "No. of letters [box] no of terms" with a missing glyph; it means "less than or equal to".
- P16-pattern-3 (saree): D, E, F look identical to A, B, C by eye; not pixel-compared. Irrelevant for the diagrams (not drawn).

## 4. Inventory accounting (for the merge)

- Claimed figures: 35 entries (items 20, concept images 3, none 12). Four are extra uses with NEW- ids: NEW-P15-number_machine-1-sol (C100 solution), NEW-P20-pattern-1-C123 and NEW-P20-pattern-1-C125 (the second and third use of the matchstick picture), NEW-P21-pattern-1-C126-sol (C126 solution, orientation colouring).
- Not claimed, belong to other chunks: P29-arrow_diagram-1 and -2 (printed answers of Example 10, chunk B, M2.S20.T20 ex10_u), P12 and P13-pattern-3 (Example 10 and 11, chunk B), P27-table-1, P28-grid-1 and the figures of Figure it Out Q5, Q11 to Q15 (chunk D / end-of-chapter).
- Concept images used for accounting only, nothing linked: M3.S25.T25.C103.IMG1 (saree, P16-pattern-3), M3.S28.T28.C110.IMG1 (2 by 2 calendar square, P18-grid-2), M3.S30.T30.C119.IMG1 (two kinds of matchstick, P21-pattern-1).
- P18-calendar-1 is mapped none:TEXT_SUFFICIENT rather than to a concept image: the teaching image shows only the 2 by 2 square, not the calendar.
