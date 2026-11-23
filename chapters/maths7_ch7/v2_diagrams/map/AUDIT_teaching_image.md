# Audit of the teaching-image rule (user decision 23 Nov 2026), Class 7 Ch 7 "A Tale of Three Intersecting Lines"

Rule: a question, solution or worked example that needs a figure gets its own diagram even when a kept teaching image shows the same figure. Chunks A, B, C read (notes, `reason` / `reason_codes` of every none and optional item, all figure_inventory entries mapped to a concept image, LP text in `in_*.json`). No file changed (no backup made); validator A, B, C errors 0 (same warnings as before).

Kept teaching images exist only on worked-example units: C20, C42 (chunk A), C51, C66 (B, both already required with own IMG2), C107, C108, C118 (C; C118 already required with IMG2). So the only candidates are the four worked examples below.

## Flipped

- none.

## Examined, left as is

- M1.S7.T7.C20 (worked, optional, tent / tree / pole): every length (30 m, 20 m, 25 m) is in the question, the steps are the sums 20 + 25 = 45 and 30 < 45; the teaching image C20.IMG1 is a scene (tent, tree, pole, direct and roundabout path), not a lengths diagram. A labelled triangle would help, not needed (Step D optional). Without the teaching image the call would be the same.
- M1.S13.T13.C42 (worked, optional, touch / miss / cross): the radii and the base 8 are in the text and each case is decided by the sums 8, 7, 11 compared with 8; the steps never refer to a figure. Teaching image C42.IMG1 shows the three cases with the sums. Borderline: if the user wants three panels (radii 3 and 5, 2 and 5, 5 and 6 on AB = 8) it is a worked-example item `M1.S13.T13.C42.IMG2` (IMG1 is the kept image), `geometry_figure`, derived from nothing; flip is a single edit.
- M3.S31.T31.C107 and C108 (worked, none): the side triples / angle triples are all in the question text, the answer is a name; a picture would only show the answer (TEXT_SUFFICIENT). Teaching images (tick-mark triangles, sorting by angles) stay.
- M2.S28.T28.C96 (solution, optional): numeric answer on a given figure whose own question diagram (C95) is required; Step E precedent is Q required, S none or optional (SAME_AS_QUESTION_DIAGRAM). The teaching image of C91 was only named as an aside.
- M2.S26.T26.C89 (solution, none): numeric answer (65 each) on a given figure, printed answer repeats the question figure.
- M1.S14.T14 and M2.S23.T23 items (C45 to C50, C71 to C76): inequalities and plain tables, no figure.
- M2.S25.T25.C82 (question, optional) and M2.S17.T17.C59 (solution, optional): not teaching-image based (the figure would only help; the answer of C59 is a statement).
- Inventory entries mapped to a concept image (P03-1 to C4.IMG1, P04-3 to C8.IMG1, P07 to C20.IMG1, P10 to C35.IMG1, P12 and P13 to C42.IMG1, P16-2 to C60.IMG1, P22-2 to C97.IMG1, P25 to C107.IMG1, P27-2 to C118.IMG1): the items that need the same figure already have their own diagram (C7, C12, C24, C28, C39, C55, C63, C118) or no LP item uses it.

## Unresolved

- None (C42 above is the one borderline).
