# Chunk A notes (Class 7 Ch 15 "Finding the Unknown", plan cbse_eng_maths7_ch15_v27)

Chunk A = topics M1.S1.T1, M1.S3.T3, M1.S4.T4, M1.S5.T5, M2.S6.T6 (20 units, 32 items).
Result: required 17 / optional 1 / none 14. Validator: errors 0 (5 warnings, all "required solution diagram with no printed
figure": this pdf has no printed-solutions section, so the five solution figures of the mobiles and sack scales have no base figure).
Output: map/out_A.json. Generator script (kept outside HERE): scratchpad gen_A.py.

## 1. Judgement calls

- **Question figures of the mobile and sack-scale questions (units 5 to 9) are required.** Every one is "find the unknown ... in the
  following cases" on printed Figs 7.1 to 7.12; the hanging structure and pan contents are in the picture and the LP text only
  describes them in words. Not made `none` even though the text is long.
- **Mobile solutions (units 5, 6, 7) required.** The book figure has empty boxes next to each object; filling them is the answer
  (ACTION_ON_FIGURE). The solution figure shows every box filled plus the two side totals (8 | 8, 12 | 12, 4 | 4, 9 | 9, 20 | 20,
  6 | 6, 16 | 16, 10 | 10) as ANSWER tags on the strings, because each LP solution starts with "each side is ...". If the user thinks
  the totals clutter, drop the tags: the filled boxes alone already satisfy the rule.
- **Sack-scale solutions (units 8, 9: C12, C14) required, but this is the most borderline call.** The answer is a number, no box is
  printed, so Step E would say "numeric answer, solution none or optional". I made it required because the solution is a visual
  cancellation (remove equal weights from both pans) and the catalogue rule for `balance_model` is "both pans equal for the answer":
  the figure repeats the two balances with the sack weight written on every sack (10 kg, 14 kg, 7 kg, 15 kg). Alternatives for the
  user: (a) drop to `optional` (then nothing is added); (b) redraw as the reduced balances after cancelling ("sacks alone on one
  pan") with the cancelled items shown dashed in FOCUS: the earlier author's `s_figure` hint describes this; I did not do it because
  it moves/removes given items (rule 5.3) and Sack scale 4 has no room for a dashed copy of 60 sacks.
- **Unit 10 (worked example "frame equations for mobile 6 and mobile 7") required.** The book writes "For the problem in Fig. 7.6 ...
  Fig. 7.7" and the equations are read off the picture; the text alone could be solved, so this is a rule-based call (referred
  figure is drawn, one diagram per item), not a tie-breaker call. Boxes stay empty (the letters e and y are not in the question text).
  It repeats the Mobile 6 and Mobile 7 panels of M1.S3.T3.C9.IMG1.
- **Unit 13 (Q3 "frame equations for mobile 8 and sack scales 1, 2, 3"): question required, solution none.** The question text has no
  data at all, so the figures must be repeated: Mobile 8 plus Sack scales 1 to 3 on one card (16:9 card with the
  mobile on the left). Solution `none`: the answer is four equations in letters (a different kind of answer from units 5 to 9: no box
  to fill), LaTeX is enough.
- **Unit 15 (Figure it Out Q3 blobs): question required, solution optional.** "In the given picture" -> drawn even though a teaching
  image (M1.S4.T4.C17.IMG2) shows a picture of the same problem. The solution is an equation (3b + 4 = 25, b = 7); a picture with the
  3 blobs opened to show 7 dots each would help but is not needed: `optional`, not added.
- **Units 11 and 12 (Jasmine 99 sticks, 200 sticks): same picture, two diagrams.** Both say "this sequence" with no description, so
  both questions get the figure (identical spec; the second says so in `render_note`). Both solutions `none` (equation, parity).
- **Units 16 and 17 (Figure it Out Q16):** question figures required (the pattern shape is not in the LP text), solutions `none`
  for both (siblings): numbers and the rules 3n + 3 and 9n + 4. Position numerals 1, 2, 3 (4) are drawn under each arrangement
  although the book prints none: the LP text numbers the positions ("position number 11"), as the two teaching images already do.
- **Unit 14 ("Frame 5 equations"):** open ended, no figure either side.
- **Units 1 to 4, 18 to 20:** text and LaTeX only. Units 1 to 4 are LP-made ready checks (no book source). Examples 2 to 4 print
  strike-through cancellations: LaTeX `\cancel`, not diagrams.
- **Labels:** "Mobile 1".."Mobile 8" and "Sack scale 1".."Sack scale 4" are drawn as small panel labels because the LP question and
  solution texts use exactly these names ("Mobile 1: each side is 8"); the book's captions "Fig. 7.x" are not drawn. If the user
  treats such labels as headings, delete the label lines from the descriptions and rely on left-to-right order.
- **Object glyphs.** The book illustrations (leaf, bud, flower, star, fish, submarine, book, pencil box, sun, cloud, bolt, crown,
  gem, bread, egg, cross biscuit, donut, watermelon, orange, banana, sacks) carry the data (which object hangs where), so each is
  specified as a simple flat shape with a style-token fill, no clip-art, no hands, no coloured panel backgrounds. Sack and weight
  block sizes are pictorial, not to scale; the 90 and 60 sacks of Sack scale 4 are a 3-sack bundle with a tag, as in the book.
- **Sack scale 3 arrangement.** The book draws a heap; the spec uses a compact stack (3 sacks below, 2 on top; 3 blocks/sacks below,
  1 kg block and a sack on top) so that every sack is countable and the same pan fits the 3-balance card of unit 13.
- **Figure inventory.** 19 base figures belong to the chunk (all of 7.1 pages 1 to 4, Figure it Out Q3 on p.22, Q16 on p.25), plus 7
  `NEW-<base id>-<concept>` entries for second uses of the same book picture (Figs 7.6, 7.7 again in unit 10; the matchstick
  sequence again in unit 12; Figs 7.8 to 7.11 again in unit 13). `P01-mobile_rule-1/2` -> concept image M1.S2.T2.C2.IMG1.
  `P04-annotated_equation-1` (LHS/RHS callouts on 2n + 1 = 99) -> `none:TEXT_SUFFICIENT`: no item of this chunk needs it and no
  teaching image covers it (the merge may want to flag it for the teaching side).
- The base descriptions of all 19 figures were checked against the page pictures: all correct (object counts in the mobiles,
  pan contents, stair rows). Stick counts of the staircase (13, 22, 31, 40) and of the cap pattern (6, 9, 12) were recomputed from
  the cell layout in code.

## 2. Things in the LP that look wrong or thin

- Units 11, 12, 16, 17 (and the old q_figure hints): the question text says "this sequence" / "the first stick pattern" and gives no
  shape for Jasmine and the 200-stick question: without the figure the questions cannot be read. The figure fixes that; no LP
  text change needed, but a text sync is not required either.
- Unit 13: the question text ("frame equations for mobile 8 and sack scales 1, 2 and 3") states no weights; it depends entirely on
  figures from earlier concepts. The "Sack scale 1 to 4" numbering is the LP's (the book calls them Figs 7.9 to 7.12).
- Unit 19 (Example 3): the book prints 135 on p.6 but "132" in the two displayed lines on p.7 (a typo in the book); the LP uses 135,
  which is consistent with 7091 and 7024. LP correct.
- Unit 16(a): "How many squares are in position number 11?" answer 11 counts only squares (the triangular cap is not a square): consistent.
- Mobile 3 of unit 5: the book shows no value for either the book or the pencil box; the answers 4 and 2 come from the LP solution
  (8 / 2 = 4, 4 / 2 = 2) and check out (4 = 2 + 2).
- Teaching image M1.S4.T4.C17.IMG2 (blobs) places the blobs in a row with 2 + 2 dots; the book has a scattered layout with 4 dots in
  the gaps. Same data (3 blobs, 4 dots, 25), only the layout differs. The new question diagram follows the book.

## 3. Places where the book itself is unclear

- Fig 7.1: the dark blue-purple object on the left chain is drawn like a small bud/tulip; the LP calls it "bud". Kept.
- Fig 7.5 shows the crown and 5 gems on the left string and 4 crowns on the right; counted from an enlarged page picture, agrees
  with the LP and with 20 = 5 + 3 x 5 = 4 x 5.
- Figs 7.9 and 7.10 are drawn hanging, Figs 7.11 and 7.12 standing on a fulcrum with an equals sign; the spec draws all four standing.
- The book prints no position numbers on the Figure it Out Q16 patterns; the first figure shows 3 positions, the second 4.
- There is no printed-solutions section in this pdf (solutions_pages null): every solution decision rests on the LP solution text.
