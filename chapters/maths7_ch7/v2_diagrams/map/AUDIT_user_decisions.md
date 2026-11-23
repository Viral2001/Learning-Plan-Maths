# Audit of user decisions (23 Nov 2026), Class 7 Ch 7 "A Tale of Three Intersecting Lines"

Rule 1 (book mistakes): no change needed, every required diagram already draws the correct value.
Rule 2 (figure letters): three changes. Backups: `out_A.json.before_user_decisions`, `out_B.json.before_user_decisions`. Validator after the edits: `--chunk A` errors 0 (the same 4 warnings as before), `--chunk B` errors 0 (the same 3 warnings as before); C not touched.

## Changed
- M1.S5.T5.C14, solution (out_A), Rule 2: "the letters (a) to (e)" were kept out -> letters "(a)" to "(e)" drawn 50 px left of the base's left end of the five triangles (4-4-6, 3-4-5, 1-5-5, 4-6-8, 3.5-3.5-3.5), INK 48 px, at (200,540), (910,540), (1535,540), (321,940), (1201,940). Why: one picture holds five triangles and the LP steps and answer refer to them as $(a)$ to $(e)$. Fields changed: content.elements (5 text elements), manim_description (steps 38 to 42), visible_text, alt_text, must_not_show (the line "the letters (a) to (e)" removed), accuracy_checks, render_note.
- M2.S17.T17.C57, solution (out_B), Rule 2: "part letters (a), (b), (c) not drawn" -> "(a)", "(b)", "(c)" drawn under the base labels of the left, middle and right triangle (INK 48 px, y = 1.2 canvas-cm, x = 2.470, 8.700, 16.975). Why: three triangles in one picture, the LP steps refer to $(a)$, $(b)$, $(c)$. Fields changed: content.labels, manim_description, visible_text, alt_text, must_not_show, accuracy_checks, reason (the phrase "no part letters inside the picture" replaced), render_note.
- M2.S20.T20.C65, solution (out_B), Rule 2: same change, letters at x = 2.750, 8.600, 16.300, y = 1.2 (clear of the base labels at y = 2.33).

## Examined, left as is
- M1.S6.T6.C17 / C18 (two circles, three circles): the LP uses the words "Two circles" / "Three circles"; A, B, C, D are point letters; no figure letters.
- M1.S8.T8.C24, C28, M1.S11.T11.C39, M2.S15.T15.C51, M2.S21.T21.C66, M2.S25.T25.C81, C83: panels, but the LP never refers to them by letter.
- M2.S26.T26.C85: the figure is for part (a) only (the book prints only (a)), so it holds one figure; the LP letters (a) to (d) name question parts. No letters added.
- M3.S32.T32.C115 (three triangles B1, B2, B3): the LP picks angles (30, 45, 70 degrees), not letters. M3.S32.T32.C117 (two isosceles triangles): the LP answer "(i) and (ii)" names the question's cases for the equilateral triangle, the steps name the isosceles ones by words; borderline, left.
- M1.S6.T6.C18 and P28-shape-3: the printed answer relabels the three circles; the diagram keeps the LP's (question's) lettering. P05-construction-1: the book's C is misplaced; the diagram already uses exact coordinates. Fig. 7.4 / M1.S8.T8.C26: sides 15, 10, 30 given by the LP, drawn as a rough impossible triangle on purpose.
- Rounded lengths (3.6, 6.9, 9.8 ...): geometry exact, labels as in the LP.

## Unresolved
- none.
