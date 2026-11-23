# Audit of Class 7 Ch 5 against the two user decisions of 23 Nov 2026

Chunks A, B, C read (notes, base inventories, `out_*.json`, LP text in `source/cbse_eng_maths7_ch5_v52.json`, book pages 18-20). Only `out_C.json` (3 items) and one `figure_inventory` description in `out_A.json` were edited; `out_B.json` is untouched. Backups: `out_A.json.before_user_decisions`, `out_C.json.before_user_decisions`. Validator after the edits: A errors 0, B errors 0, C errors 0. No decision, `lp_placeholder_action`, `placeholder` or media id was changed.

## Changed items

| concept id | role | rule | old -> new | why |
|---|---|---|---|---|
| M5.S24.T24.C83 | question | 2 | ten panels without letters -> each panel carries an upright tag (a) ... (j) in its corner (`content.panels[].panel_letter`, `manim_description`, `visible_text`, `must_not_show`, `alt_text`, one `accuracy_checks` line, `render_note`) | The LP answer C84 refers to the figures by letter in every step ("(a): ...", "(b): ...", up to "(j)"). Tag positions were searched so that each tag keeps 14 px clear of every line, arc and label and stays inside its cell. Tags are upright, the unknown angle labels a° to j° stay italic. |
| M5.S24.T24.C85 | question | 2 | four panels without numbers -> tags (i), (ii), (iii), (iv) | The LP answer C86 goes "(i): ... (ii): ... (iii): ... (iv): ...". Roman numerals treated like letters (same enumerator of a lettered/numbered figure set). |
| M5.S24.T24.C87 | question | 2 | two panels without numbers -> tags (i), (ii) | The LP answer C88 goes "(i): ... (ii): ...". Same reading as C85. |
| figure_inventory P26-dot_lines-2 (out_A, for item M2.S11.T11.C36) | - | 1 (documentation only) | description now starts with "CORRECTED:" and says the book's fourth red segment (1 across, 1 up) is not exactly perpendicular and is left out | The base inventory records the slip ("not exactly perpendicular ... drawn as printed"). The solution figure of C36 already leaves the segment out (the LP wins) and its `render_note` already says so; only the inventory line lacked the marker. No diagram content changed. |

The solutions of Q1, Q2, Q3 (C84, C86, C88) stay `none` (SAME_AS_QUESTION_DIAGRAM), so there is no solution diagram to keep consistent.

## Examined, left as is

Rule 1 (book slips)
- Fig. 5.14 (C46 worked example, C48 question): the book and the LP text only say "t intersects lines l and m"; they never say parallel, and the answer (at most four distinct angles) does not depend on it. The figure is a general pair (l at -5, m at +5 degrees, converging). Not a slip; no parallel marks, as the spec says.
- Fig. 5.25 (C70/C71), Fig. 5.26 (C72/C73), Fig. 5.28 (C79/C80), also Fig. 5.19 (C51), Fig. 5.18 solution (C55), Fig. 5.29 (C81/C82): checked from the coordinates, l and m (and every parallel-marked pair) have exactly the same direction and carry parallel marks. The "slope" in the notes is a common tilt, not a convergence, so nothing is drawn wrong. Fig. 5.27 (C74/C75) and the C52 figure are not parallel on purpose (the LP says so).
- C38 (Fig. 5.11 answer): the LP differs from the printed answer (arrow counts on shape 2; second right angle at (5, 6) in shape 3). The diagram already follows the LP, the angle at (5, 6) is a real right angle (flat edge and upright edge), and the `render_note` records the difference. Not a book slip.
- C19 (Fig. 5.5): the book prints 115.3 and the picture measures 114.3; drawn at the printed 115.3 already. C33/C34 (Fig. 5.8): the book sketch has c and r not exactly parallel; drawn parallel already. C63 (Fig. 5.24, fourth panel): book marks one right angle, LP two; drawn with both (LP wins).
- C83 (j): printed 27, 97 and 124 agree by arithmetic (124 = 97 + 27) although the book's slopes do not; drawn at the printed values. C85 (iii): drawn at 110 and 75 so that 110 - 35 = 75 holds. Printed answers of Q1 to Q6 (pages 32-34) all agree with the LP answers and with the diagram values (every degree value in the 51 required diagrams was compared with the LP question and solution text: no diagram value is foreign to the LP text, except given values carried from the question into its solution; values that only the text carries, C19 60 and 80, C21 2.5, C43 29/30/33, C52 10, are absent from the figures by design).
- C30 (optional, no diagram): the book answer "2n + 1" gives 7 for n = 3, while the LP counts 3, 5, 9, 17. Text only, nothing drawn.
- LP-text issues that are not diagram slips (diagram follows the book picture, already flagged in the notes): C41 "13 by 13" (picture 13 by 14), C89 "rays go up" (figure: down), C22 "about four lengths" (figure: 3.2 beyond the ends), C84/C83 "corresponding" for (a) (figure: alternate).

Rule 2 (figure letters)
- One picture with several lettered or numbered figures: only C83, C85, C87 (done above). Nothing else in chunks A, B, C combines several figures in one card.
- C37/C38 (Fig. 5.11): five shapes in one drawing, named "Shape 1" to "Shape 5" only in the LP text (corners given as coordinates); the book labels none of them and they are not (a), (b) figures. Left without numbers (borderline: the LP answer does say "Shape 1: ..."; if the user wants 1 to 5 drawn, it is the same change as C83).
- C23/C24 (Fig. 5.6), C41/C42 (Fig. 5.12), C33/C34 (creases a, b, c, p, q, r), C7/C9 (angles a to d): the letters are labels of lines or angles inside ONE figure, already drawn.
- No item shows panel letters that the LP answer never uses.

Chunk A C8, C10, C24: decisions untouched (as asked); no rule changes them.

## Unresolved

- M2.S11.T11.C43 (Fig. 5.13, question): in the book picture line c is not exactly parallel to line a (about 29 against 30 degrees with the steep line, line b 33). The LP keeps these as "about 30, 29, 33" and its answer says c is parallel because the angles are "about equal", so no corrected value is forced by the LP or by arithmetic; drawn as measured. If the user wants c exactly parallel to a, the LP text (29) would have to change as well.
