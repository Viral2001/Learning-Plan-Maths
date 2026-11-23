# Audit of user decisions (23 Nov 2026), Class 7 Ch 1 "Large Numbers Around Us"

Rule 1 (book mistakes: diagram shows the correct value): no change needed, every required diagram already draws the correct value.
Rule 2 (figure letters): one change. Backup of the edited file: `out_D.json.before_user_decisions`. Validator after the edit: `--chunk D` errors 0, warnings 0 (A, B, C not touched).

## Changed
- M6.S35.T35.C148, solution (out_D), Rule 2: the two group tags "Largest sum" / "Smallest difference" -> "(a) Largest sum" / "(b) Smallest difference". Why: one picture holds the two finished arrangements for parts (a) and (b), and the LP steps and answer ("$(a)$: ... $(b)$: ...", answer_tex "(a): 1,00,75,308; (b): 10,22,447") refer to them by letter. Fields changed: content.groups[].tag, content.added_parts, manim_description, visible_text, alt_text, must_not_show, accuracy_checks, render_note.

## Examined, left as is
- M1.S6.T6.C19 question (Somu): the book picture draws its reference lines at the 200 and 500 labels and a pink strip near 60 m; the diagram already draws the Statue of Unity at 180 m and the waterfall at 450 m (values of the LP text and the printed answers) and no building bar; render_note says so. No letters.
- M1.S3.T3.C6 / C7 (ladder): the book prints 1,00,000 in the last box, the LP asks the learner for it, so the question leaves it empty; not a print slip. No letters.
- M6.S36.T36.C159, C160 and M6.S37.T37.C163 (digit strip): the book picture draws the 7 with four bars, the text and the LP solutions need three; the diagram already draws three sticks (accuracy check "the digit 7 has exactly 3 sticks"), render_note records the slip.
- M6.S35.T35.C148 Q9(a): the book's printed arrangement (99,88,776 + 65,544) is valid but not the largest sum; the diagram already draws the LP arrangement (recomputed: 99,87,654 + 87,654 = 1,00,75,308; (b) 11,22,334 - 99,887 = 10,22,447).
- M6.S35.T35.C147 question: one layout, no lettered figures.
- Book slips that are only in text or in none items (no diagram involved): FiO 1.2 Q1(e) printed second way (4,38,013 not 3,67,813), Q2 letter count (61 not 60), Q6(c) (13,495 not 13995), the printed answer table of the press-count questions.
- All other required items (C147 question, C159/C160/C163 strip, C6/C7): single figure each, no letters needed.

## Unresolved
- none.
