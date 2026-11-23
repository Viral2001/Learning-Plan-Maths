# Audit of the teaching-image rule (user decision of 23 Nov 2026): Class 7 Ch 15, Finding the Unknown

Scope: chunks A, B, C, D, E. Every `none` / `optional` item whose reason, codes or notes mention a teaching image, and every figure_inventory entry mapped to a concept image, was read against the LP text and the book page. No file was changed (no backup needed); validator results are those of the earlier run.

Test used: if no teaching image existed, would v3 make the item `required` (the learner needs the figure to attempt it: data or instruction only in the figure; a referred or lettered figure; the answer is a figure; the steps rely on the figure)? All data in the item text, a plain table, a text-only answer, or a picture that would only repeat the text -> left as it is.

## Flipped

None.

## Examined, left as is

- M2.S7.T7.C44, C46, C48 questions none (the one real call of the chapter; borderline, kept under rule 3): the book prints a machine strip with each (Chapter Exercises Q4 a, Q4 b, Q5), but the LP question text describes each machine completely (the operations, the sample line 12 -> 15 -> 60 -> 55 and 12 -> 36 / 15 -> 21, the outputs 43 and 75, 63 and 227, 5 and -11). All data are in the text, so a careful student loses nothing and a strip would only repeat the chain (`optional` at most, not added), with or without the teaching images M2.S6.T6.C37.IMG1 and IMG2. If the user wants a strip beside each question anyway, these three are the ones to flip (arrow_map / flow, 16:9; solutions C45, C47, C49 would then derive from them with 9 / 17, 33 / 115, 45 / -3). Base figures P22-machine-1..3, P23-machine-1..5.
- M2.S7.T7.C45, C47, C49 solutions none: two numbers reached by undoing the operations; no question diagram to derive from.
- M3.S20.T20.C120 worked_example none (kept): "follow the book's two chains"; the steps write both chains out line by line, so the teaching image M3.S20.T20.C120.IMG1 (the chain ladders) is not what makes the text sufficient. The sibling C123 / C124 (Chains Going Up) already has its own diagrams because its question text carries no chain.
- M1.S5.T5.C27 solution optional, M3.S14.T14.C79, C81 worked examples optional, M3.S15.T15.C86, M3.S16.T16.C94 and C98 solutions optional: the figure would help but the text is complete; none of these reasons is a teaching image.
- M1.S1.T1.C1 worked examples, T5 solutions C19, C21, C23, C29, C31, chunk C and chunk E arithmetic and equation items: text and LaTeX.
- The question figures of the mobile, sack-scale, blob, matchstick, board, T-tile, grill and triangle items already have their own diagrams although teaching images (C2, C3, C15, C17, C67, C78, C82) show the same figures.

## Unresolved

None.
