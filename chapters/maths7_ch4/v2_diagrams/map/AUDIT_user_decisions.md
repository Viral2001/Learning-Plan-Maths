# Audit of user decisions (23 Nov 2026), Class 7 Ch 4 "Expressions using Letter-Numbers"

Rule 1 (book mistakes): no change needed, every required diagram already draws the correct value.
Rule 2 (figure letters): one change. Backup: `out_C.json.before_user_decisions`. Validator after the edit: `--chunk C` errors 0, warnings 0 (A, B, D not touched).

## Changed
- M2.S22.T22.C91, question (out_C), Rule 2: "no letters drawn" -> captions "(i)", "(ii)", "(iii)" drawn under picture 1 (centre (280, 625)), picture 2 ((892, 890)) and picture 3 ((1572, 890)), bold INK 44 px. Why: one picture holds the three pictures and the LP question and answer refer to them as "Picture (i)", "(ii)", "(iii)" ("(i): ... (ii): ... (iii): ..."). Fields changed: content.captions (new), manim_description, visible_text, alt_text, must_not_show, accuracy_checks, render_note. The solution C92 is optional and not added.

## Examined, left as is
- M1.S8.T8.C35 / C36 (calendar and grid): the book calendar's weekdays are one day off the real November 2024 (1st on Saturday), but the title is not drawn, so the picture shows no wrong value; left as printed (no correction is forced). The LP refers to no figure by letter.
- M2.S20.T20.C83 / C84 (two stars 5u, 5 + u): values recomputed (55, 40, 10, 25 and 16, 13, 7, 10); no letters in the LP.
- M2.S21.T21.C87 / C88 (stars 10y - 3, 10(y - 3)): values recomputed (17, -3, 97, 67 and -10, -30, 70, 40); order of the arrows follows the book, only the order differs from the LP; no letters.
- M2.S24.T24.C99 to C102 (machines): values recomputed (2a - b gives 8, 15, 7, 10; a + b - 2 gives 5, 7, 18, 18; a x b + 1 gives 5, 1, 7 and 31); "a x b + 1" equals the LP's "ab + 1"; the letters a, b are inputs, not figure letters.
- M3.S29.T29.C115 to C117 (calendar diagonals and cross): sums 32 and 75 recomputed; no letters.
- M3.S31.T31.C121, C123, C125, C126 (matchsticks), M3.S32.T32.C135, C136, C138 (Q5, Q6), C155, C156 (Q15 grid): single figure each, values consistent with the LP.
- M3.S32.T32.C147, C149, C151, C153 (Q11 ropes, Q12 squares, Q13 lights, Q14 X patterns): three figures in some, but the LP never refers to them by letter or number, so none added.
- M2.S14.T14.C59/C60, M2.S15.T15.C63/C64 and M2.S20.T20.C85: single figures; no letters in the LP.
- Book slips in none items (Mind the Mistake row 4 "x + 5" against "x + y"): no diagram involved.

## Unresolved
- none.
