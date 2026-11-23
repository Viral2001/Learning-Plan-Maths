# Audit: teaching-image rule (user decision 5, 23 Nov 2026), Class 5 Ch 4 "We the Travellers - II"

Backup before the edit: `out_A.json.before_teaching_image_rule`. Validator after the edit: chunk A errors 0 (5 warnings, all "required but no inventory figure maps to it": the book prints no such figure). Chunks B, C and D were read for consistency only and not edited.

## Flipped items
- M1.S2.T2.C3, worked_example, M1.S2.T2.C3.IMG2 (was none, TEXT_SUFFICIENT): the answer is the arrangement after one swap (Group 1 = 4, 6, 9 and Group 2 = 2, 7, 10, both sums 19), the same kind of answer as the four Making Sums Equal solutions (ANSWER_IS_FIGURE, v3 B2); finished-state card figure in the style of M1.S3.T3.C6.IMG1 with three cards per group.

## Other change (inventory accounting)
- Removed the figure_inventory entry `P04-pattern-1` (was `concept_image:M2.S13.T13.C35.IMG1`) from out_A: the book figure (boxes of sums of 2, 3 and 4 consecutive numbers) is the given figure of M2.S14.T14.C37 and C39 and chunk B already maps it to those items (user decision 5: map to the item that draws it, not to a concept image). Without this, the merge would keep chunk A's entry under the base id and demote chunk B's use to `NEW-P04-pattern-1-B`. coverage_report updated (11 figures, 4 items, 0 concept images, 7 none). Chunk A's own notes (notes_A.md section 1.5) had already asked for this.

## Examined, left as is
- M1.S4.T4.C13 (worked, 67 + 58): column addition with regrouping is LATEX_ARITHMETIC and the sibling lorry example (C16) is none; no figure given or needed without the chart image.
- M1.S7.T7.C19 (worked, 54 + 98 and 63 + 30): plain arithmetic, no book figure, answer is numbers; at most optional (hop picture), not required.
- M1.S9.T9.C23 (worked, whole/parts sentences and 72 - 38 with check): number sentences and column subtraction, all text/LaTeX, answer is numbers.
- M2.S13.T13.C35 (worked, sums of 3 consecutive numbers from 10, 11, 12): every sum and difference is in the steps, answer is numbers; the book boxes are the figure of the next topic's questions, not of this example.
- All question and solution items of chunk A that are none (M1.S5.T5 to M1.S12.T12): none for other reasons (LATEX_ARITHMETIC, HEADER_BOXES_ONLY, TEXT_SUFFICIENT), not because of a teaching image.
- Chunks B, C, D, consistency only: their none/optional worked examples and solutions (B C43, C46, C69, C47; C C83, C97, C100; D C125, C133, C137, C143 and the optional solutions) are text-first for their own reasons and say the teaching image is not the reason; D's required worked examples C105 and C117 follow the same ANSWER_IS_FIGURE logic as the flip of C3. No change needed.

## Unresolved
- notes_A.md (not edited, outside the brief) still lists M1.S2.T2.C3 as "none" under Borderline and counts "Required 8 / none 21"; the out_A.json meta note is updated (9 required, 20 none).
- The flipped C3 figure is not a book picture, so no inventory entry maps to it (validator warning only).
