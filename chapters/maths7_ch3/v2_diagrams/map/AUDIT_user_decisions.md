# Audit of user decisions (23 Nov 2026), Class 7 Ch 3 "A Peek Beyond the Point"

Rule 1 (book mistakes): no change needed, every required diagram already draws the correct value.
Rule 2 (figure letters): one change. Backup: `out_C.json.before_user_decisions`. Validator after the edit: `--chunk C` errors 0, warnings 1 (the same "C66 solution has no printed figure" warning as before); A, B, D, E not touched.

## Changed
- M3.S17.T17.C69, solution (out_C), Rule 2: "No (a)/(b) letters" -> letters "(a)" above the left zoom chain (9.876) and "(b)" above the right chain (0.407) (INK 44 px, left edges x=100 and x=1040, centred y=70, clear of the divider). Why: one picture holds the two chains and the LP steps and answer refer to them as "(a) 9.876" and "(b) 0.407". Fields changed: content.group_letters (new), manim_description, visible_text, alt_text, must_not_show (caption line reworded), accuracy_checks, render_note.

## Examined, left as is
- M1.S2.T2.C5 (USB cable, hand, box, leaf): the LP question and answer give USB 4 8/10, hand 1 6/10, box 2 3/10, leaf 3 9/10; the book picture reads about 1 3/10 (hand), 2 8/10 (box, vertical ruler) and 11 (leaf), and the book prints no answer for it. The diagram draws the LP values (bars at 4.8, 1.6, 2.3, 3.9 of the stated scales). The LP values are fixed by the question text, so nothing forces a different drawing; whether the LP numbers or the picture are meant is a content-owner matter (already in notes_A), not a diagram change.
- M1.S7.T7.C26 question: the book prints the first label of the fourth ruler as 4 9/10 (misprint); the diagram already draws 8 9/10 (row 4 labels 8 9/10, 9, 9 1/10 ...), render_note and figure_inventory record it.
- M1.S7.T7.C25 question / solution: labels as printed in the book question; the printed answer page has "99 over 10" under the 0.99 pointer, the diagram draws 99/100; box values 55, 155, 174, 202, 240 hundredths match the LP.
- M1.S7.T7.C24, C8: single figures, no letters.
- M3.S17.T17.C67: the LP says there is a long tick at 5.2, the book picture has none; the diagram follows the LP (render_note says so); A to D are point letters named in the LP.
- M3.S17.T17.C68: the question picture holds the book's Figures (a) and (b), but the LP question and answer never refer to them by letter (they say "4.185" and "'?'"), so no letters, as drawn.
- M3.S17.T17.C66, C70, C71, C72: no figure letters; box letters a to h are named in the LP.
- M3.S18.T18.C76: the book answer shows 8.542 in the yellow row (digit 1 missing); the diagram draws the LP's 8.5421.
- M3.S21.T21.C94: the book answer (9.476 + 1.025 = 10.501) is not the best; the diagram draws the LP answer 0.643 + 9.857 = 10.500 (column sums 3+7, 4+5+1, 6+8+1, 0+9+1 checked).
- M3.S23.T23.C99: no printed book figure, single figure.
- Book slips in none items (population table split, place-value table row h "2 1/10", FiO Q10 misprint): no diagram involved.

## Unresolved
- none.
