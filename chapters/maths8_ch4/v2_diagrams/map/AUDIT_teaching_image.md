# Audit: teaching-image rule (user decision 23 Nov 2026), Class 8 Ch 4 "Quadrilaterals", chunks A, B, C

Test applied to every none/optional item that cites a teaching image (or whose figure is a concept image): would v3 (Steps B, B2, C, E) make it `required` if no teaching image existed? Only chunk B was edited (backup `out_B.json.before_teaching_image_rule`); validator `--chunk B`: errors 0 (one old warning, C76, unchanged).

## Flipped
- M4.S15.T15.C63, worked_example, M4.S15.T15.C63.IMG2: parallelogram EASY with diagonals AY = 10 cm and ES = 6 cm crossing at O, given state only (the book prints this figure with Deduction 8; steps use triangles AOE, YOS and alternate angles).
- M4.S17.T17.C69, worked_example, M4.S17.T17.C69.IMG2: rhombus GAME with diagonals GM = 8 cm and EA = 6 cm crossing at O, given state only, no right-angle mark (the book prints this figure with Deduction 10; steps use triangles GEO, MEO).

Both were `optional` only because the figure "is already the concept's own teaching image"; sibling worked examples C3, C5 (chunk A) and C97, C98 (chunk C), where the book also prints the figure, are already `required`. Drawn to scale (checked in code: lengths, midpoints, parallel/equal sides, label boxes against lines). Because the LP lengths decide the shape, the EASY figure leans the other way from the book's (the book draws AY shorter than ES); noted in `render_note`. figure_inventory P18-shape-1 and P21-shape-1 moved from `concept_image:` to `item:... (question)`; coverage_report and meta counts updated (chunk B now required 14 / optional 0 / none 11).

## Examined, left as is
- M3.S11.T11.C44 (worked, quadrilateral angle sum): three numbers, no figure anywhere, arithmetic working; the split quadrilateral only illustrates a general rule.
- M5.S26.T26.C102 (worked, names of a square): no figure given, the answer is a list of words.
- M2.S3.T3.C9, M2.S6.T6.C20 (questions): the book's picture is a lesson figure, not given with the question; all data is in the words and a student can sketch it (reason is not the teaching image).
- M2.S3.T3.C7, M2.S6.T6.C18 (questions): the lesson picture would give away step 1 of the solution.
- M3.S12.T12.C48 (solution): 360 - 270 = 90, a rectangle would only repeat the sentence.

## Unresolved (judgement left to the user, nothing changed)
- M6.S28.T28.C110 (worked, folded sheet, `optional`): the question is fully in words, no numbers or positions; the book's step pictures are accounted `none:TEXT_SUFFICIENT`, only the opened sheet is the teaching image. Left optional because the answer is a name and a fold instruction, not a drawing; flip if the user wants every paper-fold puzzle drawn.
- M5.S26.T26.C103 (worked, diagonals bisecting at 90 degrees make a rhombus, `optional`): its reason is "LP-written, no book figure", not the teaching image (C103.IMG1 shows the same figure). Its steps rely on the figure like C63 and C69, so it is the one sibling that now differs; flip if the user wants a drawing for every worked proof regardless of a book figure.
