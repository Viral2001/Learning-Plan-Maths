# Audit of the teaching-image rule (user decision 23 Nov 2026): Class 8 Ch 9, chunks A to D

Result: no item flipped. No out_*.json of this chapter was edited (so no `.before_teaching_image_rule` backup exists here). All four chunks still validate with errors 0.

Chunks A, B and D were already written to the v3 rule that a teaching image is never linked (C4, C5, C9, C10, C11, C14, C40, C41, C42, C43 and the lotus items are required although a teaching image shows the same figure), so only the items below cite a teaching image in a `none` decision.

## Flipped
(none)

## Examined, left as is
Test used: if no teaching image existed, would v3 (Steps B, B2, C, E) make the item required? In every case below the answer is no, so the teaching image was not the reason.
- M1.S2.T2.C3 (worked, double the side): every number is in the question (side 1 doubled, areas 1 and 4), the steps are arithmetic, the question points at no figure. Same kind as C12 (half the side), which is none without any teaching image (sibling consistency).
- M2.S4.T4.C22 (worked, closer bounds for root 2): the book's three dashed boxes are plain lists of squares of decimals (LATEX_TABLE); the red pairs are already in the steps.
- M3.S6.T6.C39 (worked, squares of areas 9 and 16): authored example with no book figure; the teaching image C39.IMG1 shows the general arrangement (Area A, Area B), not this 3-4-5 figure, so it never stood in for one. Numbers are in the text, steps are arithmetic.
- M3.S7.T7.C47 (question side of the equal-squares pair): the question gives no figure (it points back to a method on an earlier page); a question with no given figure gets no question diagram. The solution C48 is already required.
- M3.S8.T8.C54 (worked, ladder example, blocks 0 to 3): authored, no book figure, all numbers in the text, arithmetic steps. Block 1 is `optional` for its own reason (a turned triangle would only help), not the teaching image.
- M3.S10.T10.C73 (worked, why (n-1)^2 + (2n-1) = n^2): the book prints only equations here; the L-shape picture exists only as the teaching image, no book figure is referred to, steps are arithmetic.

## Unresolved
- M3.S8.T8.C53 (worked, 3 cm and 4 cm triangle): the book prints a triangle with 3 cm, 4 cm and '?' beside the 'make a triangle' instruction, as it does for M2.S5.T5.C27 (required in chunk A). Left none because the LP question is self-contained and the text tells the learner to draw it; the chunk B note already lists 'required (given picture)' as the alternative. If the user wants it, one diagram M3.S8.T8.C53.IMG2 (kept image is C53.IMG1) with the 3 cm / 4 cm / ? triangle would do.
