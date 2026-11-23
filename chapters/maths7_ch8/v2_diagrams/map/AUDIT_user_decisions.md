# Audit of the two user decisions (23 Nov 2026), Class 7 Ch 8 "Working with Fractions"

Rule 1 = book print slips: the diagram shows the correct value. Rule 2 = figure letters only when the LP answer refers to the figures by letter.
Edited file: `out_A.json` (backup `out_A.json.before_user_decisions`). `out_B.json` and `out_C.json` unchanged. Validator: A errors 0 (same single warning as before).

## Changed
- M1.S8.T8.C35, solution, Rule 2: no letters -> part letters (a) (b) (c) (d) in INK above the four unit squares (x = 270, 730, 1190, 1650; y = 185). Why: the LP steps and answer name the parts "(a): ... (b): ... (c): ... (d): ...". Fields: content.panels, manim_description, visible_text, must_not_show, accuracy_checks, alt_text, render_note.
- M1.S10.T10.C42, solution, Rule 2: no letters -> part letters (a) (b) (c) (d) above the four squares, same positions. Why: the LP steps and answer name the parts (a) to (d). Same fields as C35.
- figure_inventory P33-area_model-1 (out_A), Rule 1: description now starts "CORRECTED:". Why: base inventory records the book's "5 parts" label under figure (b) (4 columns drawn); the picture of C35 does not copy the misprint (no parts labels). Item C35 itself needed no change beyond the letters (its render_note already says the misprint is not drawn).

## Examined, left as is
- M3.S24.T24.C109 question (practice figures (a) and (b), book p.193, answers p.36): Rule 1: both printed figures recomputed, no slip. (a) band between the diagonal and its parallel = 1/2 - 1/8 = 3/8 (shoelace 0.375); (b) two corner triangles of the diamond = 2 x 1/8 x 1/4 = 1/16. The answers 3/8 and 1/16 match the figures. Rule 2: the LP answer (C110 steps and answers) never names the figures (a)/(b), so the spec correctly shows no letters. The mismatch "split into four equal squares" (LP) vs the book's lower 2:1 rectangle is an LP text issue, already `needs_lp_text_sync`, not a book slip.
- M3.S25.T25.C111 question (Q10): the book's V apex sits slightly above the quarter's centre; the spec already puts it at the centre (the value 3/32 needs it); the base inventory calls this a reading, not a print slip. No change.
- M3.S25.T25.C113 (ants), M3.S23.T23.C106 (Fig. 8.4), M1.S6.T6.C26, C28, M1.S7.T7.C31, C33, M1.S13.T13.C56: single figures with no lettered parts; arithmetic of C26, C28, C31, C33, C56 rechecked, no slip found.
- Text-only slips, nothing drawn: P07-flow_diagram-3 ("Divide the multiplicand by 3" and dangling "=", mapped none) and p.10 "7/8" for 7/18 (annotated expression, none).
- M3.S25.T25.C112 solution (wrong geometry in LP steps 2-3): an LP text issue, not a book slip; not touched.

## Unresolved
- None.
