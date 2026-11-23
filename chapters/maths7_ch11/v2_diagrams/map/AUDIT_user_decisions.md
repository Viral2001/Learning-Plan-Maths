# Audit of the two user decisions (23 Nov 2026), Class 7 Ch 11 "Finding Common Ground"

Rule 1 = book print slips: the diagram shows the correct value. Rule 2 = figure letters only when the LP answer refers to the figures by letter.
Edited file: `out_C.json` (backup `out_C.json.before_user_decisions`). `out_A.json`, `out_B.json`, `out_D.json` unchanged. Validator: C errors 0 (same warnings as before: long visible_text strings, no book figure for C118).

## Changed
- M3.S33.T33.C118, solution (HCF and LCM by bigger divisors), Rule 2: no letters -> part letters (a) above the left ladder (90 and 150) and (b) above the right ladder (84 and 132), INK 56 px at (587, 220) and (1347, 220). Why: the LP answer reads "(a): HCF = 30, LCM = 450; (b): HCF = 12, LCM = 924". Fields: content.ladders, manim_description, visible_text, must_not_show, accuracy_checks, alt_text, render_note. The question side C117 is `none`, so no pair partner to align.

## Examined, left as is
- Rule 2, other combined pictures: M1.S9.T9.C26 (ladders for 105 and 30), M3.S31.T31.C104 (270/50 and 540/100), M3.S32.T32.C110 (ladders 300/150 and 630/770), M3.S33.T33.C115 / C116 (same two ladders), M3.S37.T37.C137 / C138 (two rows of stars). The LP steps and answers name the parts by their numbers or "row one / row two", never by letter, so no letters are right.
- Rule 1: no drawn figure copies a print slip. M3.S32.T32.C110 follows the LP (ladder stops at 9, 11; the book divides once more by 3 to 3, 11, same LCM 6930): a difference of method, not a slip. All ladders, factorisations and star positions recomputed.
- Jump Jackpot M1.S7.T7.C19/C20 and idli-vada M2.S23.T23.C76/C77: the answers use "(a) ... (d)", but both pairs are decision `none` (no diagram), so Rule 2 does not apply.

## Unresolved
- None.
