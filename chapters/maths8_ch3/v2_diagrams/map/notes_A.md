# Notes for chunk A (Class 8 Ch 3 "A Story of Numbers", topics M1.S2.T2 to M2.S11.T11)

Result: 19 units, 31 items. Required 2 (both solution side), optional 1, none 28. Figures claimed 15 (13 base + 2 NEW): 1 to an item, 3 to concept images, 11 none. Validator: errors 0, warnings 1 (expected, see C31 below).

The part of the chapter in this chunk is almost all words: counting methods, number names, Roman numerals. The book has only one answer that is itself a picture (Example (a), Roman addition), so only that one and its sibling (b) get a diagram.

## 1. Judgement calls

| Item | Decision | Why |
|---|---|---|
| M2.S10.T10.C35 (solution, Example (a) CCXXXII + CCCCXIII) | required, `M2.S10.T10.C35.IMG1` | The book prints the answer of this example as a picture: two drawings of the pooled letters with loops (5 C's -> D, 4 X's -> XL, 5 I's -> V = DCXLV). B2: printed answer is a picture, and the loops carry the meaning. Question side none (the question gives only two numerals as text). Drawn as two panels like the book; given letters INK, loops FOCUS, additions ANSWER. `derived_from` null (no question diagram). |
| M2.S9.T9.C31 (solution, part (b) LXXXVII + LXXVIII) | required, `M2.S9.T9.C31.IMG1` | Sibling of (a) in the same NCERT example, same kind of answer (a Roman sum by regrouping). The book prints NO picture for (b) ("Do it yourself now"), so the figure is my design from the LP steps: one row per symbol (C, L, X, V, I from top to bottom), the original letters in INK, each group that is exchanged looped (FOCUS) with an arrow up to the new letter (ANSWER) it becomes: five I's -> V, two V's -> X, five X's -> L, two L's -> C; the left-over C, L, X, V read CLXV. Every count comes from the LP steps (2 L, 5 X, 2 V, 5 I). The base inventory has no figure for it (hence the one validator warning). |
| M1.S3.T3.C8 (solution, stick arithmetic) | optional (not added) | A strip of four stick pictures (join / pair and take away / repeat / group) would clearly help, but the LP's four-line method is complete and the book's printed answer is text only. |
| M1.S2.T2.C4 (worked example, "use Table 1") | none, `LATEX_TABLE` | The item names Table 1, but it is a plain white table of numbers and Roman numerals, so it is a LaTeX array (Step C, plain table). See LP text issues: the table itself is not in the question text. |
| M2.S11.T11.C37 (solution, Hindu vs Roman features) | none, `LATEX_TABLE` | The printed answer is a plain two-column table of words (no colour, no marks). |
| M1.S7.T7.C22 (solution, Gumulgal arithmetic) | none | All four answers are number names in words, as printed in the book. The concept had two old solution cards; that does not make a diagram necessary. |
| M1.S6.T6.C18 (1345 by fives) | none | 1345 / 5 = 269 is arithmetic; drawing 269 symbols helps nobody, and teaching image M1.S5.T5.C15.IMG1 already shows the idea (not linked). |
| Worked examples C3, C13, C14, C23 (cows and sticks, Lebombo bone, Gumulgal names, 2367) | none | Each gives all its data in words and has a teaching image of the same idea (not linked). A drawing of the grouped notches (C13) or of 2367 in landmarks (C23) would show the answer, and a worked-example figure sits after the question text. |
| Open or discussion items (C9/C10, C11/C12, C19/C20, C38/C39) and the word items (C7, C21, C28, C30, C32, C34, C36) | none | `OPEN_ENDED` / `TEXT_SUFFICIENT`; the book gives no figure with them. |
| Printed answers C29, C33 (Roman numerals, products) | none | Text and arithmetic lines (MCCXXII, MMCMXCIX, CCCII, DCCXV; CCL, 25 M's, MMD, LXIII). |

Figure inventory choices (Step 0):
- To concept images (accounting only, nothing linked): P01 (cuneiform strip, p.1; section 3.1 has no unit of its own in the three chunks, so I claimed it because my units are the rest of 3.1) -> `M1.S1.T1.C1.IMG1`; P04 (cows and sticks) -> `M1.S2.T2.C3.IMG1`; P05-table-2 (letters a to z) -> `M1.S2.T2.C4.IMG1`.
- `none:LATEX_TABLE`: P05-table-1, P06-table-1 (Table 1), P09-table-1 (Gumulgal list), P11-table-1 (Roman landmarks), P37-table-1 (printed answer table of Q3).
- `none:NOT_RENDERABLE` (painted art or a real map, and no item of this chunk is built on it): P03 digit-evolution chart, P08 body counting, P09-map, P10 "quickly count" tiles, NEW-P08-bones-1.
- NEW figures I found: NEW-P08-bones-1 (photographs of the Lebombo and Ishango bones, p.8; no notch can be counted) and NEW-P13-daredevil-1 (Daredevil Contest cartoon with the speech bubble "Multiply CCXXXI and MDCCCLII", p.13; decoration, `DECORATIVE_ONLY`).
- Not listed (pure decoration, no mathematical content): the Reema-and-father cartoon (p.1), the person among a heap of mangoes (p.7), the Roman scene (p.11), the girl character (p.10, p.12), the Egyptian mural (p.14).
- P12 base description checked against the page picture: letters (CCXXXII over CCCCXIII), loop contents (5 C's, 4 X's, 5 I's) and labels (D, XL, V, = DCXLV) agree.

## 2. LP text issues

- **M1.S2.T2.C4 (worked example)**: the question says "use Table 1 to write 13 and 18 in Roman symbols" but Table 1 is not in the question text, and the concept text above it lists the symbols in one line ("I, II, III, ... XX (Table 1)") without the numbers they belong to. Suggested sentence for the question: "Table 1 gives the Roman symbols for 1 to 20 in order: I, II, III, IV, V, VI, VII, VIII, IX, X, XI, XII, XIII, XIV, XV, XVI, XVII, XVIII, XIX, XX." (or a LaTeX array with the numbers 1 to 20 above them).
- **Figure it Out numbers in the LP labels do not match the book's** (book numbers in brackets):
  - M1.S3.T3.C7/C8 "The Mechanism of Counting, Q1" = book Figure it Out Q1 (p.7): fine.
  - M1.S4.T4.C9/C10 "Figure it Out, Q1" = book Q2 (p.7); M1.S4.T4.C11/C12 "Figure it Out, Q2" = book Q3 (p.7).
  - M1.S6.T6.C19/C20 "Early Number Systems, Q1" = book Figure it Out Q1 (p.13).
  - M1.S7.T7.C21/C22 "Figure it Out, Q1" = book Q2 (p.13-14).
  - M2.S11.T11.C36/C37 "Figure it Out, Q1" = book Q3 (p.14); M2.S11.T11.C38/C39 "Figure it Out, Q2" = book Q4 (p.14).
  - The same labels ("Figure it out: Q1") repeat across topics (M1.S4.T4.C9, M1.S7.T7.C21, M2.S11.T11.C36), which a learner will see side by side.
- **M1.S7.T7.C22, step (iii)**: the sentence "write the first number two times and then double the result, 4 copies in all" is confusing (the answer 18 ukasar is right: 9 x 4 = 36). Suggested: "ukasar-ukasar is 4, so write the first number 4 times: 16 ukasar and 4 urapon; the 4 urapon make 2 more ukasar, so 18 ukasar."
- **M2.S8.T8.C23 (worked example)**: the LP numeral MMCCCLXVII is right; the book prints MMCCCLXII (missing the V; 2367 = 1000 + 1000 + 100 + 100 + 100 + 50 + 10 + 5 + 1 + 1). No diagram is drawn for this item; if a figure of it is ever drawn it must show MMCCCLXVII.
- **M2.S9.T9.C31 and M2.S10.T10.C35**: the solution figure will sit before step 1. The steps' wording ("Count the symbols ...", "Five I's make one V") fits the figure, so no text change is needed; if the figure is added, "Look at the picture first" is not required.

Checks I did on the LP solutions (all correct): 1345 / 5 = 269; (i) 9 + 7 = 16 = 8 ukasar, (ii) 9 - 6 = 3, (iii) 9 x 4 = 36 = 18 ukasar, (iv) 16 / 4 = 4; MCCXXII, MMCMXCIX, CCCII, DCCXV; 87 + 78 = 165 = CLXV; 5 x 50 = 250 = CCL, 50 x 500 = 25000 (25 M's), 5 x 500 = 2500 = MMD, 7 x 9 = 63 = LXIII; 232 + 413 = 645 = DCXLV.

## 3. Where the book itself is unclear

- The book prints no answer for part (b) (LXXXVII + LXXVIII), nor for the in-text question about 1345 in a system that counts only by 5s, nor for the "Try this" items (own number system, refining it).
- The loops in the book's Example (a) picture touch the neighbouring letter slightly (the third C of row 2); the groups themselves (5 C's, 4 X's, 5 I's) are certain.
- P10 ("quickly count" tiles): the counts of flowers, stairs and grapes cannot be read exactly (the base inventory says about 17, 12 to 14, about 40); not needed, no item uses it.
- P03 digit chart: the historic glyph shapes cannot be transcribed exactly; not needed.
- The book gives Gumulgal names only up to 6 ("ras" for anything larger); Figure it Out C Q2 extends the pattern of counting in twos, and the LP's solution follows that pattern.

## 4. Borderline

- **M2.S9.T9.C31 required** (the only one that could go either way). Reason for required: sibling consistency with (a) in the same example, and the four-step carry is where learners slip. Reason it could be optional: the book prints no picture for (b) and the LP steps carry every count. Flip to `optional` (action `drop_image`) if you prefer picture-only-where-the-book-has-one; the validator then needs the C31 item to be changed and the counts in `meta` adjusted.
- **M2.S10.T10.C35 required**: the LP steps already carry all the counts (decision 4: not flipped to none for that reason); required by B2 because the book's own answer is the picture.
- **M1.S2.T2.C4**: FIG_REFERENCED ("use Table 1") against LATEX_TABLE (plain table). I chose none + LaTeX array; the cost is only the LP text issue above.
- **M1.S3.T3.C8 optional vs none**: a four-picture stick strip would help; nothing in the book needs it.
- **M2.S11.T11.C37**: a filled comparison table could be read as ANSWER_IS_FIGURE; it is a plain table of words with no colour or marks, so none.
- **Worked examples with teaching images** (C3, C13, C14, C23): none, since the figure the example would need is the teaching image, which is never linked and would leak the answer if placed after the question.
- Figures P04, P05-table-2, P01 are mapped to concept images although the match is of idea rather than of the exact book picture (teaching images are redrawn, not copies); P03, P08, P09-map and P10 use `NOT_RENDERABLE` only to say "not drawn, no item needs it", not that an item is blocked.
