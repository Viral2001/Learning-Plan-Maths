# Audit: teaching-image rule (user decision 23 Nov 2026), Class 8 Ch 13 "Algebra Play"

Files edited: `map/out_B.json` only (backup `map/out_B.json.before_teaching_image_rule`). `out_A.json` and `out_C.json` were examined and not changed. Validator: chunk A errors 0, chunk B errors 0 (11 warnings, all the usual kind: long visible_text, solution figures the book never prints), chunk C errors 0.

## Flipped to `required` (3, all question side, chunk B)

- M3.S13.T13.C72, question, M3.S13.T13.C72.IMG1: Mukta's four steps as a left-to-right flow (FIG_REFERENCED, DATA_IN_FIGURE).
- M3.S13.T13.C74, question, M3.S13.T13.C74.IMG1: same specification (render_note "same as M3.S13.T13.C72.IMG1").
- M3.S13.T13.C76, question, M3.S13.T13.C76.IMG1: same specification.

Why: the three questions say "Follow Mukta's trick", "Follow the trick" and "In the trick given above", and the LP question text never lists the four steps (they exist only in the book's comic strip on p.10 and in the teaching concept C68). Without the teaching image M3.S12.T12.C68.IMG1 the only reason for `none` (the v3 "procedure flow-chart already a concept image" rule) disappears, and FIG_REFERENCED applies: the learner needs the figure to attempt the question. The figure shows only what the question gives: the four steps (choose a 2-digit number of different digits, reverse the digits, take their difference, divide the result by 9) in four boxes joined by three arrows. It does not show the chain on 47 (74, 74 - 47 = 27, 27 / 9 = 3: that is the answer to C72, and C74 uses 83), the characters, or the letters. The book's "Find their difference." is drawn as "Take their difference" so that no instruction word "Find" stands in a figure. Solutions C73, C75, C77 stay `none` (not a teaching-image case, see below).

Inventory: base figure P10-dialogue_strip-3 moved from `concept_image:M3.S12.T12.C68.IMG1` to `item:M3.S13.T13.C72 (question)`; new entries NEW-P10-dialogue_strip-3-C74 and NEW-P10-dialogue_strip-3-C76 (items C74, C76) and NEW-P10-dialogue_strip-3-teaching (`concept_image:M3.S12.T12.C68.IMG1`, accounting only, the way chunk D of Class 5 Ch 1 records a teaching use). coverage_report: 21 figures, 13 to items, 3 to concept images, 5 none; counts: question required 7 / none 8.

## Examined, left as is

- M3.S13.T13.C73, C75, C77 (solutions of the above): arithmetic and algebra lines (74 - 47 = 27, 10b + a - 10a - b = 9(b - a), ...); the book has no printed answer picture; `none` was never about the teaching image.
- M3.S14.T14.C78 (question, chunk C): refers to "the trick given above" but states the change itself (sum instead of difference) and three numeric examples, so a careful student can attempt it from the text (tie-breaker). Kept `none`, TEXT_SUFFICIENT. Borderline: see Unresolved.
- M3.S12.T12.C70 (worked example, 352 and 253): the question gives no figure and the steps are algebra lines; the place-value teaching image is not needed to follow them. `none`.
- M2.S7.T7.C48 (worked example, three dates in a column): the question gives no calendar, the working is three algebra lines; the calendar picture would be an extra (optional at most). `none`.
- M3.S15.T15.C84, C85, C86 (worked examples: cycles, stickers, lemonade stall): word problems with every number in the text and steps in algebra; the solved pictures are teaching illustrations, not a figure the example relies on. `none`.
- M1.S2.T2.C6 (worked example, new steps): text and LaTeX chain, no figure in the book. `none`.
- Figures mapped to concept images (pyramids P03, P04 steps, P05, P06; 2 x 2 letter grid P07-grid-3): every item that needs a pyramid or grid already has its own `required` diagram (C25 to C32, C34, C38, C42, C44, C51 to C56); no item needs the letter grid. Nothing to flip.
- M2.S5.T5.C33 (question) and C35/C36: `none` because the book gives no empty pyramid / only a plain row of boxes, not because of C23.IMG1.
- Chunk C optional solutions C81, C89, C99, C101: no teaching image exists for these figures; they stay `optional` (not added) for the reasons in notes_C.md.
- Date-trick items C12 to C17 (chunk A): no teaching image shows the strip, so they are outside this rule.

## Unresolved

- Date-trick comic (chunk A: C12, C14, C16 questions, C13, C15, C17 solutions, all `none`) is the same kind of figure as Mukta's comic (a comic strip carrying a procedure that the LP question text does not list). C72/C74/C76 are now `required` and C12/C14/C16 are `none`. I did not touch them (no teaching image was the reason; notes_A.md Borderline 4 already flags this). If sibling consistency is wanted, C12, C14, C16 would need a six-step flow (month x 5, + 6, x 4, + 9, x 5, + day).
- C78: if the user wants every "trick given above" question to carry the four-step figure, C78 would be a fourth identical flip (media id M3.S14.T14.C78.IMG1, derived spec as C72).
- `map/notes_B.md` still describes C72/C74/C76 as `none` (left untouched on purpose; this file supersedes it for those three items).
