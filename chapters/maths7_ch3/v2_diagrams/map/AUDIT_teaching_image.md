# Audit 2: the teaching-image rule (user decision 23 Nov 2026), Class 7 Ch 3 "A Peek Beyond the Point"

Candidates looked at: every `none` / `optional` item of out_A to out_E whose reason, codes or notes mention a teaching / concept image, the twelve concept images and the four worked units with a kept image (C3, C4, C21, C35). Edited: out_A only. Backup: `out_A.json.before_teaching_image_rule`. Validator after the edit: `--chunk A` errors 0, warnings 0 (B, C, D, E not touched).

## Flipped
- M1.S2.T2.C3, worked_example, M1.S2.T2.C3.IMG2: two screws (ends at 2.7 and 3.2 cm) above a ruler marked in tenths, no length written (MEASUREMENT_READING, DATA_IN_FIGURE); same reading skill and ruler style as the required C8 / C26 questions of the chunk.
- M1.S6.T6.C21, worked_example, M1.S6.T6.C21.IMG2: the wire above the 0 to 1 2/10 scale with hundredth ticks, ending 4 hundredth ticks after the 1 1/10 mark (DATA_IN_FIGURE: what a "small part" is and where the 1 1/10 mark sits are shown only on the scale); the three written forms are the answer and are not drawn.
- Inventory moved with them: P02-ruler_measurement-1 and P09-ruler_measurement-2 from `concept_image:` to `item:... (question)`; P02-ruler_measurement-2 (the second screw) from `none:TEXT_SUFFICIENT` to `item:M1.S2.T2.C3 (question)` because the C3 diagram now draws it. Coverage and counts updated (worked_example required 1 to 3, optional 3 to 1).

## Examined, left as is
- M1.S2.T2.C4 worked (3 4/10 = 34/10): a conversion of a length stated in words; the book picture adds nothing the text lacks (TEXT_SUFFICIENT), so the teaching image was not the reason.
- M2.S10.T10.C35 worked (ladder 1000 ... 1/1000): the answer is a number sequence (LATEX_ARITHMETIC) and the question gives no figure; the "divide by ten" strips are teaching figures.
- M2.S11.T11.C38 solution: counts of steps of ten, arithmetic; the printed answer is not a figure.
- M3.S17.T17.C69 question (make the zoom lines): the learner draws them, the book gives no figure, so no question figure; the solution C69 is already required.
- M3.S19.T19.C82 question and solution, C83: no figure in the book, the answer is a one-line result; the number-line teaching image C75.IMG1 was not the reason.
- M2.S12.T12.C40 worked, M2.S13.T13.C44, M3.S19.T19.C78: place-value tables with digits only are HEADER_BOXES_ONLY / LATEX_TABLE in v3 (not a diagram), independent of the teaching image C41.IMG1.
- M2.S13.T13.C45 question, M3.S19.T19.C78 question: the book's place table is the learner's own working, not a given figure.
- Optional for reasons that do not rest on a teaching image (untouched): C17 question (hand picture), C22 worked (mark on blank scales), C34 worked, C32 solution, C80 solution, C88 worked.
- No 'refer picture' item exists in this chapter.

## Unresolved
- none
