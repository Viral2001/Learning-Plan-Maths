# Audit of user decisions (23 Nov 2026), Class 7 Ch 2 "Arithmetic Expressions"

Rule 1 (book mistakes): no change needed, every required diagram already draws the correct value.
Rule 2 (figure letters): one change. Backup: `out_D.json.before_user_decisions`. Validator after the edit: `--chunk D` errors 0, warnings 0 (A, B, C not touched).

## Changed
- M3.S24.T24.C114, question (out_D), Rule 2: captions "(I)" and "(II)" were NOT drawn -> now drawn under the left (3 by 3) and right (4 by 4) picture (bold INK, 0.5 units, centres (-3.125, -2.8) and (2.8, -2.8); clear of the pictures and inside the card). Why: one picture holds two lettered figures and the LP question and answer refer to them as "Picture $I$" / "Picture $II$". Judgement: the Roman labels (I), (II) are treated as figure letters, as in the book's own captions. Fields changed: content.captions (new), manim_description, visible_text, alt_text, must_not_show (the line "captions (I) and (II) under the pictures" removed), accuracy_checks, render_note. The solution C115 is optional and not added; if added it must derive from this figure and inherit the captions.

## Examined, left as is
- M1.S6.T6.C19 solution (Example 3): the book labels both braces 24 although Raja's brace also covers the extra circle; the diagram already labels Kabir's brace 25 and Farhan's 24 (LP text), render_note records it. Panels are not lettered in the LP.
- M1.S6.T6.C17 solution (Example 2): picture not to scale in the book (Joy's bar longer); the diagram draws equal bars, only labels carry values. No letters.
- M2.S15.T15.C53 / C54 (Example 11): two arrangements in one picture, the LP calls them "one arrangement" / "another" / "first" / "second", no letters; values recomputed (13 and 16).
- M2.S16.T16.C59 / C60 (window): single figure for part (c); the LP letters (a)-(c) name question parts, not figures. Values recomputed (2 x 3 + 6 x 2 + 7 x 5 = 53).
- M3.S19.T19.C72 (grid of 10 cards): LP differs from the book (54 + (-16) asked, -87 + (-16) given); diagram follows the LP; all ten sums recomputed and correct; the LP refers to no card by letter.
- M3.S22.T22.C97 / C99 and M2.S11.T11.C33: single figures, values recomputed (134 and 35).
- Book slips in none items only (Q4(b) printed three times, "Q1(e) minus sign missing", Q3 and Q6 answers): no diagram involved.

## Unresolved
- none.
