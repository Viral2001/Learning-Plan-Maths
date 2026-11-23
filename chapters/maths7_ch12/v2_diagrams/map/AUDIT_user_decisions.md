# Audit of the two user decisions (23 Nov 2026), Class 7 Ch 12 "Another Peek Beyond the Point"

Rule 1 = book print slips: the diagram shows the correct value. Rule 2 = figure letters only when the LP answer refers to the figures by letter.
Edited file: `out_D.json` (backup `out_D.json.before_user_decisions`). `out_A.json`, `out_B.json`, `out_C.json`, `out_E.json` unchanged. Validator: D errors 0, warnings 0.

## Changed
- M3.S34.T34.C149, question (FiO 4.4 Q2, two number lines), Rule 2: no letters -> part letters (a) for the upper line and (b) for the lower line, INK 44 px at (140, 340) and (140, 800), left of the lines. Why: the LP question and the LP answer name the parts (a) and (b) ("(a): 3.16; (b): 2.162"). Fields: content.lines, manim_description, visible_text, must_not_show, accuracy_checks, alt_text, render_note.
- M3.S34.T34.C150, solution, Rule 2: same letters (a) and (b) at the same positions, kept identical to the question figure (derived_from C149.IMG1). Same fields.

## Examined, left as is
- M3.S36.T36.C165 / C166 (book Q9 table): single table; the letters a and b are the book's row/column variable names inside the figure, not figure letters. Given cells and all 25 quotients recomputed (41, 4.1, 4100 at the stated positions); no slip.
- M1.S5.T5.C21 (rectangle 13.3 cm by 5.7 cm): single figure, values as in the book and the LP.
- Hidato figures P29-hidato_grid-2 (printed solution shows 39 where 29 belongs, and 16 where 6 belongs) and P30-hidato_grid-2 (37 cells for numbers 1-39): the base inventory records these book mistakes, but the figures are mapped only to concept images (C171.IMG1, C172.IMG1) and no required item draws them. Nothing to correct in this run; flagged because the teaching images are untouched.
- Text-only book slips, nothing drawn: Q2(b) options both 4458.75, duplicate (b) and (f) in Q8, "364.2422 days", "one-thousands" header.

## Unresolved
- None.
