# Chunk B notes (Class 6 Ch 7 Fractions): topics M1.S9.T9, M1.S10.T10, M1.S11.T11, M1.S12.T12

Result: 27 items = required 17 / optional 1 / none 9. Validator: errors 0, 7 warnings (all expected: solution figures that derive from a question diagram or whose picture is not printed in the book: C34, C43, C45, C47, C51, C55, C57).
Inventory claimed: 13 base figures (11 to items, 2 none), no NEW- figures. Page pictures p.6-10 and p.38-40 were checked; the circles of p.8 and the number lines of p.9-10 were checked on zoomed crops.

## 1. Judgement calls

- **7.3 Q1 (C29/C30), continue the table of 1/2.** Question `optional` (not added): the book's table of half-roti pictures would help, but the LP text already lists all five equations. Solution `none` (LATEX_ARITHMETIC): the printed answer SOL38-table-1 is two plain typeset rows. This differs from Q2 on purpose: Q2's printed answer is a drawn table of quarter pieces, Q1's is not. P07-table-1 (the half-roti table, a teaching figure of 7.3 that sits in chunk A's section) is claimed here as `none:TEXT_SUFFICIENT` because Q1 and Q2 use it; chunk A may map it to a concept image, the merge keeps both uses.
- **7.3 Q2 (C31/C32).** Question `none` (no figure of its own). Solution `required` (B2: printed answer is a picture): 4-column table of 1, 2, 3 and 4 quarter pieces with captions `n × 1/4`. The addition statements are left to the LP text (they would break the 3-word tag rule).
- **7.3 Q3 (C33/C34), 1/3 and 1/6 with a paper strip.** Question `none`. Solution `required` (ANSWER_IS_FIGURE, a folding construction): strip in 3 parts (INK, 1/3 labels), then the same strip in 6 parts (new creases and 1/6 labels in ANSWER). Borderline against the tie-breaker (text could do it); chosen because B2 says a construction answer is drawn even when the steps describe it in words. The book prints NO answer for Q3.
- **7.3 Q4 (C35/C36), 5 × 1/4 and 9 × 1/4.** Question `none` (the learner draws). Solution `required`: both printed answers are pictures. A pair gets only ONE solution diagram in this run, so (a) and (b) are two rows of one card (captions `5 × 1/4`, `9 × 1/4` instead of the letters a. b.). If the build can take IMG2, splitting it into two cards would match the prompt's "one diagram per part" rule better.
- **7.3 Q5 (C37/C38), matching.** Question `required` (the shaded circles exist only in the picture); the picture numbers 1 to 4 are added because the LP text says "picture 1" to "picture 4". Solution `required` (printed answer is a picture): same layout, matching fraction written under each circle in ANSWER with a short arrow. The book's own answer layout (four stacked fraction-arrow-circle rows) was not copied, to keep the solution derived from the question diagram; connector lines were rejected because they would cross.
- **7.4 worked example 1 (C39), IMG2.** `required`: the book gives the blue line only as a picture and asks for its length. The concept's teaching image C39.IMG1 stays untouched and is not linked. Box under the 1/2 tick left empty (the question asks for the length).
- **7.4 q1, q2 and FiO Q4, Q5 (C42-C45, C54-C57).** Question `required` (given number line the learner reads and writes into). Solution `required` (ACTION_ON_FIGURE, v3 pair rule), derived from the question, with the boxes filled in ANSWER. Kept to filled boxes only (no braces) so the four items stay consistent. These solution figures are the most "repeat-like" of the chunk; if the user wants fewer images, they are the first to drop (decision would become SAME_AS_QUESTION_DIAGRAM).
- **7.4 q1 (C42) draws a tick at 5/3.** The book prints ticks at 0, 1/3, 2/3, 1, 4/3, 2 only. The text says each unit is divided into three equal parts, so all thirds are ticked (render_note says so).
- **7.4 q3 (C46/C47), eighths.** Question `none` (no figure in the book). Solution `required`: judgement call, because the printed answer is plain text (1/8, 2/8, 3/8, ...). Drawn because the answer is the labelling of 8 equal marks on a number line and the whole section is about that. Could reasonably be `optional`.
- **FiO 7.4 Q1 (C48/C49).** Question `none` (learner draws). Solution `required`: printed answer is a number line (SOL40-number_line-1). The book's picture shows only labelled ticks (0, 1/10, 3/10, 4/5, 1); I also draw the three lines as bars from 0 because the question says "draw lines" and the LP answer says each goes from 0 to its mark. The 4/5 label sits on the 8th tick (8/10).
- **FiO 7.4 Q2 (C50/C51), five fractions of your choice.** Question `none` (OPEN_ENDED). Solution `required`: the answer is marks on a number line; v3 section 5 rule 4 says draw the LP's sample (1/4, 3/4, 2/3, 5/6, 7/8). Drawn as four stacked rows (quarters, thirds, sixths, eighths) because on one 1200 px line 5/6 and 7/8 would be only 50 px apart. The book prints no answer for Q2. Borderline against OPEN_ENDED.
- **FiO 7.4 Q3 (C52/C53).** Both `none` (think-and-discuss; the answer is one statement).
- Colours: "blue line" = SET_A, "black line" = INK, the number line itself INK (the book uses light grey), shaded sectors MARK_FILL (the book hatches them). All figures are 16:9; positions are given in px so the renderer has nothing to guess.
- Teaching figures P06-strip-1..3 and P07-strip-1 are in 7.3 but belong to chunk A's topics (T7, T8); I did not claim them.

## 2. Things in the LP that look wrong

- **C35/C36 (7.3 Q4):** the question asks to "write an addition statement", but the LP answer only gives `5/4 = 1 + 1/4` and `9/4 = 2 + 1/4`. The book's printed answer has the full statements (`1/4 + 1/4 + 1/4 + 1/4 + 1/4 = 5/4 = 5 times quarter`, and the nine-term one `= 9 times quarter = 2 + 1/4`). The LP text needs the addition statements added; the figure deliberately does not carry them.
- **C37 (7.3 Q5):** the LP question text spells out the number of equal parts of every picture ("picture 1 is cut into 8 equal parts, ..."). That gives away the counting step the book leaves to the learner; once the picture is there the sentence could go.
- **C53 (FiO 7.4 Q3):** the book answers "Uncountable number of fractions", the LP "Infinitely many". LP kept (it is the safer statement: the fractions are infinitely many, but countable). Wording differs from the book.
- **T11 items (C42-C47):** `book_number` is a description ("Number Line: blue line in thirds"), not an NCERT number; they are items 1 to 3 after the worked example on p.159 (book page 9 of the PDF).
- **C54 (FiO 7.4 Q4):** the LP question text already states the answer for the blue line (1/2), as the book does; fine, but the box under 1/2 must be drawn filled in the question figure (it is).
- Printed solutions: p.38 goes from Q2 to "Try Further! Q4" (no Q3), and p.40 goes from Q1 to Q3 (no Q2). The LP answers for FiO 7.3 Q3 and FiO 7.4 Q2 therefore have no printed counterpart.

## 3. Where the book itself is unclear

- p.9, 7.4 item 1: no tick at 5/3 between 4/3 and 2 (a gap of two parts), although the unit is divided in thirds.
- p.38-39, Q4 answers: the single extra quarter is drawn with its right angle at the bottom-left and a faint upper-left outline; orientation read from the page, not important for the meaning.
- p.38, Q2 answer table: the right-hand side of every `=` is left blank in the print; the LP fills it with `n × 1/4`.
- p.39, Q5 answer: the fractions are listed in the order 1/3, 1/5, 1/6, 1/8, while the question row is 1/3, 1/5, 1/8, 1/6.
- p.8, Q5: the fourth circle is a low-resolution scan; it still shows 5 equal sectors (checked on a 2x crop).
