# Audit of the two user decisions (23 Nov 2026), Class 7 Ch 10 "Operations with Integers"

Rule 1 = book print slips: the diagram shows the correct value. Rule 2 = figure letters only when the LP answer refers to the figures by letter.
Edited file: `out_A.json` (backup `out_A.json.before_user_decisions`). `out_B.json`, `out_C.json`, `out_D.json` unchanged. Validator: A errors 0, warnings 0.

## Changed
- M2.S10.T10.C30, worked_example (Math Talk token sets), Rule 2: no letters -> part letters (a) (b) (c) in INK to the left of the three token sets, top to bottom (centres (-4.5, 3), (-4.5, 0), (-4.5, -3)). Why: the LP worked-example steps answer "(a) 8 reds ... (b) 16 reds and 8 greens ... (c) 24 reds and 16 greens". Fields: content.sets, manim_description, visible_text (18 signs + 3 letters), must_not_show, accuracy_checks, alt_text, render_note.

## Examined, left as is
- Collatz chain, p.19 (printed 32, rule gives -32): figure P19-flow-1 is mapped `none:LATEX_ARITHMETIC` and no diagram of the chapter draws it (Q5 question none, solution optional and not added); the inventory description already records the slip. Rule 1 needs no change.
- Summary sign-rule table, p.22 (column 4, rows 5-7 printed 1, 2, 3 for -1, -2, -3): P22-table-1 is mapped `none:LATEX_TABLE`, not drawn. No change.
- Magic Grid and "Try again" grids (C70, C71, C72, C73, C74): all 16 numbers recomputed as row number x column number; circles on 8, 14, 18, -15 and -6, 14, 20, 18 each multiply to -30240. The book's Rounds 1-3 are printed identically; the spec draws the final state only (not a wrong value).
- Machine figures C112, C113, C119: every given row recomputed against the rules a + b - c, -(a x b) - c, a - b x c; all rows consistent.
- Token rectangles C100, C105 (4 rows of 2 and 3 tokens): match the LP steps. Single figures, no letters.
- M1.S7.T7.C17 (Try This): see Unresolved.

## Unresolved
- M1.S7.T7.C17 question (three stacked number lines): the book numbers them Figure 1, 2, 3 and the LP question and answer refer to "Figure 1 / 2 / 3" (numerals, not letters). The spec draws no numerals (strips are told apart by top-to-bottom order). Rule 2 as worded covers letters; I did not extend it to numerals. If the numerals should be treated like letters, add 1, 2, 3 to the left of the three strips (same edit as C30).
