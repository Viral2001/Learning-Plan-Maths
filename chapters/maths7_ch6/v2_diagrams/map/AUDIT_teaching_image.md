# Audit of the teaching-image rule (user decision 23 Nov 2026), Class 7 Ch 6 "Number Play"

Rule: a question, solution or worked example that needs a figure gets its own diagram even when a kept teaching image shows the same figure. Chunks A, B, C read (notes, `reason` / `reason_codes` of every none and optional item, all figure_inventory entries mapped to a concept image, LP text in `in_*.json`). No file changed (no backup made); validator A, B, C errors 0.

No unit of this chapter has a kept (non-card) teaching image (`kept_image_ids` is empty on every unit), so no item was set to none or optional because a kept image of its own concept shows the figure. The teaching images (M1.S2.T2.C2/C4, M2.S5.T5.C32, M2.S8.T8.C51, M3.S10 to S12) sit in earlier teaching topics and are only mentioned as the place where a nicety figure already exists.

## Flipped

- none.

## Examined, left as is

- M1.S4.T4.C27 and C29 (solutions of Q2 (d), (e), optional): the answer is a verdict ("Only sometimes true") reached by word reasoning, the two counter-lines are in the steps as heights, the printed answer has no picture. Not an arrangement answer (ANSWER_IS_FIGURE does not apply); teaching image M1.S2.T2.C4.IMG1 is only named as the place the idea is drawn. Tie-breaker: text is as good.
- M2.S6.T6.C35 (question, optional, Kishor's five odd cards): the LP question is a yes/no on parity ("five odd cards", total 30) and is solvable from the words; the book's boxes-and-cards picture (teaching image M2.S5.T5.C32.IMG2) would carry the card values 13, 9, 1, 7, 11, 5, 3, which the LP question does not use and the answer (sum of five odd numbers is odd) does not need. No Step B trigger (FIG_REFERENCED needs the figure to answer, DATA_IN_FIGURE the data only in the picture, ACTION_ON_FIGURE an act on it). The book's printed solution is text, so the 'refer picture' exception does not apply either.
- M2.S7.T7.C45 / C46 and C49 / C50 (parity questions with dot pictures in the teaching topic): book prints no figure with the question or the answer; words only.
- M2.S9.T9.C55 / C56 (grids 27 x 13, 42 x 78, 135 x 654): sizes are in the words; the 3 x 4 grid (teaching image M2.S8.T8.C51.IMG1) is not a figure of these questions.
- M4.S23.T23.C113 (solution, none): positions and one check, LATEX_ARITHMETIC; the parity-pattern teaching image (M4.S22.T22.C110.IMG1) is not what the answer needs.
- M5.S24.T24 worked examples C116, C117, C118 and questions C120, C122, C124 (cryptarithms, none): a column addition with letters is LATEX_ARITHMETIC (Step C: column addition goes to a LaTeX array); the stacked-sum teaching images C114 / C115 were only a side remark.
- M4.S21.T21.C109 (solution, plain LaTeX table), magic-square items C75 / C76 / C78 / C79 / C89 / C91 / C93 (questions with no given figure) and every other none item: none for reasons unrelated to a teaching image (no figure given, plain table, arithmetic, open-ended).
- Inventory entries mapped to a concept image (P01, P03, P04, P05, P23, P07, P08, P09, P10, P11, P12, P13, P15, P16, P17, P25 grids and pictures): for each, the items that need the same figure already carry their own diagram (C6, C7, C65 to C68, C73, C74, C83, C84, C85, C87, C88, C98, C99), or no LP item uses the figure.

## Unresolved

- None.
