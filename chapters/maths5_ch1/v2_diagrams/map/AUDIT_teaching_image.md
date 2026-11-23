# Audit: teaching-image rule (user decision 23 Nov 2026), Class 5 Ch 1 "We the Travellers - I"

No map file was changed (no backups made). All four chunk files were examined: every `none` or `optional` item whose reason, reason codes or notes mention a teaching image, plus every figure_inventory entry mapped to a concept image, plus a scan of all non-required question and worked-example texts for pointers to a figure ("below", "above", "picture", "table", "chart", "arrow"). The book pdf has no printed solutions, so the LP text was the answer in every case. Validator was not re-run (nothing edited); the earlier state was errors 0.

## Flipped to `required`

None.

## Examined, left as is

Test used for each: if no teaching image existed, would v3 make the item `required` (the question gives a figure, the solution adds something visual or is a figure, the worked example's steps rely on a figure, a lettered or referred figure)? In every case below the answer is no.

- Worked examples whose teaching image shows a digit chart or tokens: C6 (52,525), C10 (34,682), C11 (30,402), C19 (68,519), C20 (60,209), C33 (compare 8,965 / 21,304 and 47,260 / 47,620). The question gives no figure; the chart is header boxes with digits (HEADER_BOXES_ONLY, a LaTeX array). `none`.
- Worked examples that are number chains or word reasoning: C3 (seven ways of travelling), C5 (add 1,000 from 4,150), C24 and C25 (pattern rules), C35 (three numbers between 71,420 and 72,050, open answer), C53, C54, C58, C59 (digit swaps, expanded form), C89, C90, C91, C99. All data is in the question text and the steps are text or LaTeX; the teaching picture shows the solved state. `none`. By contrast C34 (place four numbers on a number line) already has its own `required` diagram, C34.IMG2, so that rule was applied the way it is meant.
- Rabbit worked examples C71, C72, C73: the LP wrote them in words (4,197; 6,731; two sample numbers) with no figure given; the road figure is required only where the book hands it over as the question (C75, C77, C79, already `required` with solution roads C76, C78, C80). Left `none` (notes_C.md Borderline already says the same).
- Worked examples C109 (pairs left alone), C110 (pile of pebbles 2 and 2), C111 (subtract and repeat 2 and 5): reasoning or number chains written in full in the steps; the teaching images (river scene, game states, three subtractions) repeat the text. The book prints no picture for 2 and 5 (its printed chain is for 3 and 7, drawn as the solution figure of C124). `none`.
- C113 (river puzzle, question): the book's river scene is the same scene as teaching image C109.IMG1, but it only illustrates the start of a puzzle whose rules are stated in full in the words (DECORATIVE_ONLY); the solution C114 already carries the full eight-panel figure including a Start panel. Closest call in the chapter; kept `none`.
- C117 (question, `optional`, "each step above"): the 3-and-7 chain is not a teaching image (the teaching chain of C111 is for 2 and 5); the question text lists the four differences. Not a teaching-image case. C116, C84, C94 (`optional` solutions) and C28, C57, C64 (`none` solutions): no teaching image behind them.
- Figures mapped to concept images (P02-table-1 to C6.IMG1, P02-tokens-3 to C5.IMG1, NEW-P09-vehicles-1 to C89.IMG1, P11-scene-1 to C109.IMG1, NEW-P15-dot_pattern-2-teaching to C125.IMG1): no question, solution or worked example needs them except the stable (C125 worked example, C127 question, C129 and C131 questions, all already `required` with their own diagrams).

## Unresolved

None. Nothing surprising: the chapter's `required` items were already drawn without linking any teaching image, and the teaching-image reasons in the `none` items are all secondary to a text-sufficient or plain-table reason.
