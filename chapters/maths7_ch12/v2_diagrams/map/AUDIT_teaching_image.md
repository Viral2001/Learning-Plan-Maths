# Audit of the teaching-image rule (user decision 23 Nov 2026), Class 7 Ch 12 "Another Peek Beyond the Point"

Rule: a question, solution or worked example that needs a figure gets its OWN diagram (`required`), even when a kept teaching (concept) image shows the same figure. Test used for every candidate: if no teaching image existed, would v3 (Steps B, B2, C, E; tie-breaker) make the item `required`?

Edited: `out_D.json` only (backup `out_D.json.before_teaching_image_rule`; `.before_user_decisions` untouched). Validator: `--chunk D` errors 0, warnings 0. `out_A`, `out_B`, `out_C`, `out_E` unchanged.

## Flipped to required (1)
- M3.S32.T32.C143, question, `M3.S32.T32.C143.IMG1` (was optional, `needs_lp_text_sync` removed with its `text_alternative`): the leap-year flow chart (divisible by 400, then 100, then 4; results 366, 365, 366, 365 days), question side only. Codes `FIG_REFERENCED` + `DATA_IN_FIGURE`: "this final scheme" is not stated in the question text, so the rule lives only in the figure. Pair solution C144 stays `none` (its steps state the rule and the arithmetic). Inventory: `P25-flow-1` moved from `concept_image:M3.S31.T31.C138.IMG1` to `item:M3.S32.T32.C143 (question)`; `coverage_report` updated (mapped_to_items 5, mapped_to_concept_images 1, new_media_ids_created adds C143.IMG1) and `meta.counts_by_role_and_decision`; a line added to `meta.notes`.

## Examined, left as is
- M2.S28.T28.C116 solution (optional, remainder chain 1, 3, 2, 6, 4, 5 of 1 / 7; the book chain P19-flow-1 is concept image C108.IMG1): the answer is a list of remainders and quotient digits, a number chain for LaTeX (Step C `LATEX_ARITHMETIC`); without the teaching image it would stay `optional`. C118 (seven products): a list.
- M1.S2.T2.C5, M1.S6.T6.C23, M1.S9.T9.C39 (hop arrows, quarter pieces, brace picture): data and steps are in the words. M1.S8.T8.C35 and M1.S3.T3.C10 (plain tables): `LATEX_TABLE`.
- M1.S12.T12.C50, C51 (no figure in the book; the three-situation table is a plain table), M2.S15.T15.C58 (ribbon illustration, every number in the text, `DECORATIVE_ONLY`), M2.S21.T21.C72 (place-value chain written in the steps), M2.S22.T22.C79 (long division is LaTeX), M2.S26.T26.C100, M2.S28.T28.C111, C115 (long division), M2.S29.T29.C121 (three one-line comparisons).
- M3.S31.T31.C134, C135, C137 (arithmetic on numbers in the text), M3.S32.T32.C141 (rule and periods are stated in the question), M3.S33.T33.C145, M3.S35.T35.C159, M3.S36.T36.C167 (the box pattern is written in the question).
- Inventory: P23-table-1, P23-flow-1, P24-flow-1 (earlier stages of the leap-year scheme, `REUSES_CONCEPT_IMAGE`) and the Hidato grids (topic with no question unit) unchanged.

## Unresolved
- M3.S32.T32.C143 is the closest call of the four chapters. The earlier author kept it `optional` as a refer-picture analogue (data goes into the question text). It was flipped because this chapter's PDF has no printed answers, so the Step B2 'refer picture' exception (the book's answer points at a picture) cannot apply, and the rule in the question is not in the text. If the user prefers the text route, restore `out_D.json.before_teaching_image_rule` (then the rule sentence must be added to the question text).
