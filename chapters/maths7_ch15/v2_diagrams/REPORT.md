# Class 7 Ch 15 Finding the Unknown - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths7_ch15` v27 (taken from staging). Result: new V2 version v28 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (154 items from 89 units)
{"worked_example": {"none": 20, "required": 2, "optional": 2}, "question": {"required": 16, "none": 49}, "solution": {"required": 8, "none": 53, "optional": 4}}

Optional, NOT added: [('C27', 'solution'), ('C79', 'worked_example'), ('C81', 'worked_example'), ('C86', 'solution'), ('C94', 'solution'), ('C98', 'solution')]

needs_lp_text_sync: [('C124', 'solution')]

## The 26 diagrams
| id | side | type |
|---|---|---|
| M1.S3.T3.C5.IMG1 | question | balance_model |
| M1.S3.T3.C6.IMG1 | solution | balance_model |
| M1.S3.T3.C7.IMG1 | question | balance_model |
| M1.S3.T3.C8.IMG1 | solution | balance_model |
| M1.S3.T3.C9.IMG1 | question | balance_model |
| M1.S3.T3.C10.IMG1 | solution | balance_model |
| M1.S3.T3.C11.IMG1 | question | balance_model |
| M1.S3.T3.C12.IMG1 | solution | balance_model |
| M1.S3.T3.C13.IMG1 | question | balance_model |
| M1.S3.T3.C14.IMG1 | solution | balance_model |
| M1.S4.T4.C16.IMG1 | worked example | balance_model |
| M1.S5.T5.C18.IMG1 | question | number_pattern |
| M1.S5.T5.C20.IMG1 | question | number_pattern |
| M1.S5.T5.C22.IMG1 | question | balance_model |
| M1.S5.T5.C26.IMG1 | question | dot_array |
| M1.S5.T5.C28.IMG1 | question | number_pattern |
| M1.S5.T5.C30.IMG1 | question | number_pattern |
| M2.S13.T13.C76.IMG1 | question | arrow_map |
| M2.S13.T13.C77.IMG1 | solution | arrow_map |
| M3.S15.T15.C83.IMG1 | question | other |
| M3.S15.T15.C84.IMG1 | solution | other |
| M3.S16.T16.C93.IMG1 | question | mensuration_figure |
| M3.S16.T16.C97.IMG1 | question | geometry_figure |
| M3.S21.T21.C123.IMG1 | question | flow |
| M3.S21.T21.C124.IMG1 | solution | flow |
| M4.S25.T25.C158.IMG1 | worked example | cell_grid |

### Chunk A notes (from the decision agent)
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

### Chunk B notes (from the decision agent)
# Chunk B notes (Class 7 Ch 15 "Finding the Unknown", topics M2.S7.T7 to M2.S12.T12, units 21-36)

Result: 27 items (11 questions, 11 solutions, 5 worked examples): required 0, optional 0, none 27. Validator: errors 0, warnings 0.
Nothing in this chunk needs a drawn diagram. The chunk is equation solving (trial and error, "do the same to both sides", moving a term across); every item is an equation, arithmetic or a plain list of numbers that LaTeX carries. The only figures printed in the book for these units are the machine strips (Chapter Exercises Q4, Q5) and two boxed comparison tables (p.10).

## 1. Judgement calls

1. Machine questions: M2.S7.T7.C44 (Q4 a), C46 (Q4 b), C48 (Q5), question side = none (TEXT_SUFFICIENT + REUSES_CONCEPT_IMAGE). This is the one real decision in the chunk.
   - Why none: the LP question text already states each machine completely in words, with the sample line (12 -> 15 -> 60 -> 55; 12 -> 36 and 15 -> 21) and the outputs (43 and 75; 63 and 227; 5 and -11). By the tie-breaker a careful student loses nothing without the strips. The v3 Step B2 "refer picture" case does not apply (the LP text names no figure).
   - The same strips already exist as teaching images of the previous topic: M2.S6.T6.C37.IMG1 (Chain Machines: Q4 a strips and the two Q5 machines) and M2.S6.T6.C37.IMG2 (Two-Path Machine: Q4 b). They are never linked (v3), and the v3 prompt's own "not a diagram" list says a procedure flow already drawn as a concept image is none with REUSES_CONCEPT_IMAGE.
   - If the user wants a machine strip next to each question anyway, the three questions are the ones to flip to required (diagram_type arrow_map / flow, 16:9; Q4 a = the 12-example strip plus the two "?" strips for 43 and 75; Q4 b = the two-path loop with the 12 example plus "?" for 63 and 227; Q5 = two strips). The solutions would then be derived_from the question diagrams with the inputs 9 / 17, 33 / 115, 45 / -3 in ANSWER green.
2. Machine solutions (C45, C47, C49) = none: the answer is two numbers; the LP steps undo the operations in order and check. A filled strip would only repeat the chain (the task rules say a solution diagram needs something visual added or a picture answer). Not optional either: the text is complete.
3. Trial-and-error tables (C39: n = 5, 10, 30, 40, 50, 49 giving 11, 21, 61, 81, 101, 99; C41: x = 1, 2, 3 giving 1, 6, 11) = none with LATEX_TABLE. Plain two-column numbers; a LaTeX array can be added in the LP text (text_alternative says what).
4. Example 1 (C51): the book crosses out + 88 and - 88 on the left. That is text with a strike mark, so none (LATEX_ARITHMETIC); write it with \cancel. Same for the crossed-out 5s in the check of 5x - 4 = 7 (C52). Both are listed in the inventory as NEW-P06-ex1-cancel and NEW-P08-check-cancel, mapped none:LATEX_ARITHMETIC. The base inventory did not list them.
5. Book p.10 boxed comparisons (C64 and C65 worked examples, base P10-table-1 and P10-table-2) = none, LATEX_TABLE: two columns of plain equation lines, no colour, shading or arrows (checked on the page picture). The LP steps already give both ways as text; a two-column LaTeX array in the LP text would keep the side-by-side layout (text_alternative says how).
6. M2.S11.T11.C62/C63 (frame an equation with no solution): question OPEN_ENDED + TEXT_SUFFICIENT, solution LATEX_ARITHMETIC + OPEN_ENDED. The sample answer x + 4 = x + 5 is an equation and a two-line argument.
7. All figures that the machine questions use are mapped `concept_image:M2.S6.T6.C37.IMG1` or `...IMG2` in the figure inventory (accounting only). If another chunk claims the same base figures with a different meaning, take this mapping as the sound one: P22-machine-1/2/3 and P23-machine-4/5 are in IMG1, P23-machine-1/2/3 are in IMG2.
8. Base figure P04-annotated_equation-1 (LHS / RHS callouts on 2n + 1 = 99, book p.4) is not claimed here: it is a teaching figure of section 7.1, and the T7 question C38 does not use it (it only asks to solve 2n + 1 = 99). It belongs to the chunk that owns the equation-introduction topic.

## 2. LP checks (everything recomputed, nothing wrong found)

Arithmetic in all LP solutions was recomputed and agrees with the book and the printed figures:
- C39: 2 x 5 + 1 = 11, 2 x 10 + 1 = 21, 2 x 30 + 1 = 61, 2 x 40 + 1 = 81, 2 x 50 + 1 = 101, 2 x 49 + 1 = 99.
- C41: 5 x 1 - 4 = 1, 5 x 2 - 4 = 6, 5 x 3 - 4 = 11; x = 2.2 gives 5 x 2.2 - 4 = 7 (and 11/5 = 2.2, the value C52 finds).
- C43: 5 x 9 - 8 = 37; 37 - (33 - 31) = 35; -3 x (-11 + (-4)) = -3 x (-15) = 45.
- C45: 4(9 + 3) - 5 = 43 and 4(17 + 3) - 5 = 75. C47: 3 x 33 - 36 = 63 and 3 x 115 - 118 = 227. C49: 45 / 3 / 3 = 5 and -3 - 4 - 4 = -11.
- C51: 13353 - 88 = 13265 (and 14593 - 1459 + 145 - 14 = 13265). C52: 11/5 check. C53: 11 x 6 - 5 = 61. C57: 6 x 7 + 7 = 49 = 4 x 7 + 21.
- C59: 3 x 15 - 10 = 35; 5 x 0 = 3 x 0; 3 x 10 - 7 = 23 = 2 x 10 + 3. C61: m = -10 gives -24 on both sides; 90 / 15 = 6. C63: x + 4 = x + 5 gives 4 = 5. C64 to C66: y = 6, y = 7, u = 90 all check.

Small things in the LP (no change made, nothing to fix before diagrams):
- Book numbers "Chapter Exercises, Q1 (a)" etc. for T7 C42/C43 and Q4 / Q5 are the end-of-chapter Figure it Out items on book pp.22-23 (they are labelled "Figure it Out", not "Chapter Exercises", in the book). The ids end.FiO1a etc. are right.
- Units C58 to C61 split the book's Figure it Out Q1 (a) to (e) over two concepts; the book numbers (a) to (e) are right.
- M2.S7.T7.C38: the item's example_id "E0" sits on a question item (ordinary).

## 3. Book unclear or odd

- Book p.23, Q5, first machine: the output box prints "+5" (a plus sign before the 5), while the second machine prints "-11". The LP, the arithmetic (45 / 3 / 3 = 5) and the teaching image all use 5. Not a diagram issue; the LP wins.
- This pdf has no printed-solutions section: the LP solution text was the answer to follow, and it agrees with every question's text.

### Chunk C notes (from the decision agent)
# Notes, chunk C (units 37-52: M2.S13.T13, M3.S14.T14, M3.S15.T15, M3.S16.T16)

Result: 30 items, required 6, optional 5, none 19. Validator: errors 0 (10 warnings, all "long visible_text" on equation strings that cannot be shortened).

Required: C76 + C77 (Q19 path puzzle, question + solution), C83 + C84 (Example 7 tiles, question + solution), C93 (Q8 window grill, question), C97 (Q12 two triangles, question).
Optional (NOT added): C79 (Example 8 worked), C81 (Example 12 worked), C86 (Example 9 solution), C94 (Q8 solution), C98 (Q12 solution).

## 1. Judgement calls

- **Q19 path puzzle (C76 / C77).**
  - Question `required`. A concept image of the same board exists (M2.S12.T12.C67.IMG1), but the 'refer picture' rule does not apply: the book question itself prints the board, and the LP text lists the 11 boxes but not one of the 22 arrow labels, so the puzzle cannot be attempted without the figure.
  - Solution `required` (answer = the coloured path, B2). It draws the whole board again, derived from the question figure, and adds the 10 coloured boxes, the 9 newly coloured arrows (the arrow 4 is already coloured in the book) and each box's solved value (all in ANSWER green, 3 words at most).
  - Aspect ratio 3:4 (the book prints the board portrait; in a 16:9 card the text would be tiny).
  - The START box and the arrow 4 are coloured in the question figure because the book prints them coloured.
  - Path checked equation by equation: x = 3, 21, 1, 2, 8, 13, m = -10, k = 4, x = 4, n = -13/25; each arrow label equals the answer of the box it leaves; the box -7 = 11 - 3x (x = 6) is the only box off the path.
  - Added an extra inventory entry `NEW-P26-path_puzzle-1-sol` for the second use of the board (solution item).
- **Example 7 tiles (C83 / C84).**
  - Question `required` although the LP text gives the counts 4, 7, 10, 13: the T shape (top row of 2n + 1 with a stem of n under the middle tile) is only in the picture, and the book says "as shown below". The figure is the book's own Steps 1-3 (plain outlines), so it does not show the Step 4 that the LP text mentions.
  - Solution `required`: the book's printed method for this example is a picture (Method 1 = three arms of n tiles and one centre tile) and the LP solution starts "three arms of k tiles and one centre tile".
  - Drawn: Steps 1-4 with arms shaded, centre tile outlined, counts and the sums 1+1+1+1 = 4 ... 4+4+4+1 = 13. The Step k column and Method 2 (P11-tile_pattern-3) are not drawn: the LP follows Method 1 only and 3k + 1 is already text.
  - The tile size must shrink (64 px to 48 px) so Step 4 fits; positions of Steps 1-3 keep order and shape only, not pixel positions (said in `render_note`). Step 4 is new, so it is in ANSWER green.
- **Example 8 (C79), Example 12 (C81), Example 9 solution (C86): all `optional`.**
  - Example 8 (Fatima's rough diagram: ovals "Snack cost" and "Delivery cost" pointing at 25 x [box] + 50) and Example 9 (two rows of ovals Jahnavi / Sunita meeting at "Equal") only label expressions that the LP steps already carry as LaTeX, which is the Step D example of an optional arrow picture. Same decision for both (sibling consistency).
  - Example 12's dot boxes (Suresh's box next to Ramesh's box plus a dashed 30) show "y + 30" as quantities; helpful, but the LP steps state it in words and an equation. If you want one worked-example picture in this chunk, this is the best candidate.
  - Example 9's question side is `none` (word problem, all numbers in the text).
- **Q8 window grill (C93 / C94).**
  - Question `required`: the book question hangs on the picture, and the LP text itself starts "The figure shows". It is a figure-based question with a numeric answer, so the solution is `optional` (Step E): the answer is 3 cm from 3 + 3 + 5 x 2 + 6g = 34, fully in the LP steps.
  - Drawn schematic, not to scale, gaps taller than rods as in the book, and the unknown gap shown as `?` (a gap drawn exactly 3 cm tall would leak the answer).
- **Q12 triangles (C97 / C98).**
  - Question `required` ("these triangles"; the angle letters live at the corners and the equal sides are shown by ticks); both triangles are in ONE figure (one question diagram per item). Solution `optional` for the same reason as Q8 (numeric answers fully in the LP steps).
  - The shapes are drawn with the real answer angles (50, 65, 65 and 60, 50, 70 degrees, checked from the vertex coordinates) so the picture never contradicts the solution, while the numbers themselves are not printed.
- **Sibling checks.** Q2 (a)-(g) and Q18 (a)-(h): plain equations, all `none`. FiO2, FiO6, FiO7, FiO9, FiO20: word problems with every number in the text, `none` (banknotes for FiO2 would be NOT_RENDERABLE anyway). Q8 and Q12 solutions are treated alike (both optional).
- **Teaching images are never linked.** Four of my figures also exist as teaching images (C67.IMG1 board, C78.IMG1 T-tiles Steps 1-4, C82.IMG1 grill, C82.IMG2 triangles); the items get their own diagrams.

## 2. Things in the LP that look off

- **C76 question text** lists the 11 boxes and says "follow the arrow that carries its answer" but gives no arrow label and no adjacency: the question is not solvable from the text; the figure is mandatory (hence `required`).
- **C83 question** gives counts for Steps 1 to 4, but the book picture shows only Steps 1-3 (plain, uncoloured).
- **C93 question text** says the borders are 3 cm "at the top and at the bottom" and that all five rods are 2 cm. The book picture labels only the top border (3 cm) and one inner rod (2 cm); the other measures are the LP author's reading (consistent: 3 + 3 + 10 + 18 = 34). The picture follows the LP text for the bottom border and keeps the book's single 2 cm mark.
- **C97 question text** says both base angles of the first triangle are y + 15. The book labels only the right base angle and shows equal sides by ticks (the student is meant to notice the equal base angles); the LP text gives that away. The figure labels both, following the LP text.
- I recomputed every LP solution of this chunk (Q2 a-g, Q18 a-h, Q19, Examples 7, 8, 9, 12, FiO2, 6, 7, 8, 9, 12, 20): no arithmetic or answer error found. The video id is shared by all blocks of a pair (fine).
- Plain-text `question` of the multi-part pairs joins several blocks of one card; the pair still gets at most one diagram per side (all none here).

## 3. Places where the book is unclear

- **Q19 board (p.26):** the arrowheads are partly hidden by notches in the cream boxes and read as double-headed; the label (not the head) says which box an arrow leaves. The arrow between 2x + 5 = 3(x - 1) and 30 = 4 - 50n (column 3, rows 3-4) has no number. The label "+ 4" between -4 = 16 - 5k and 2x - 9 = 3 - x is printed with a plus sign. Which two boxes each diagonal joins was read from position (corner box to the centre-column box of the next row); the LP solution agrees with that reading for every arrow used.
- **Q8 grill (p.24):** not to scale; the small bracket arrow heads at the right are tiny; the unlabelled bracket sits on the 5th of the 6 gaps; the bottom border and the other rods carry no label.
- **Q12 (p.24):** the left base angle of the first triangle is unlabelled in the book; the figure is not to scale (the book's first triangle is much narrower than the 50-65-65 answer).
- **This pdf has no printed-solutions section**, so the LP solution text is the only answer followed; no printed-answer picture exists for this chunk (the Example 7 "Method" pictures are the nearest thing).
- Decoration left out of the inventory: the photograph of two boys playing marbles (Example 12 page) and the flower box, shutters and bricks of the grill picture.

### Chunk D notes (from the decision agent)
# Chunk D notes (Class 7 Ch 15, plan cbse_eng_maths7_ch15_v27)

Units: T18 (Ex10, Ex11), T19 (Riyaz rule, Figure it Out Q3, Q4, Q5, Q15, Q17), T20 (chains worked block), T21 (Q1 chains going up, Q1, Q6 a-e, Q10, Q13), T22 (Ex13), T23 (mistake worked block). 16 units, 30 items.
Result: required 2 (T21 Q1 question figure + its solution figure), optional 0, none 28. Validator: errors 0, warnings 0.

## 1. Judgement calls

1. **M3.S21.T21.C123 / C124 (Chains Going Up) - drawn, question AND solution.** The question says "for each chain" and "each equation", but the LP text never writes the chains; they exist only in the book figure (p.17) and the old q_figure hint. The learner cannot attempt it without them, so the question is `required` (FIG_REFERENCED, DATA_IN_FIGURE) with its own diagram = exactly the book's two top-to-bottom chains and downward operations (nothing of the answer). The teaching image M3.S20.T20.C120.IMG1 is never linked. The refer-picture exception (question `optional`) was NOT used because its condition is that the book's *answer* points at a picture; here the question itself points at the figure. If you prefer that route instead: make the question `optional` (REUSES_CONCEPT_IMAGE) and write the two chains into the question text; the solution figure would stay as is (derived_from null).
   The solution is `required` (ANSWER_IS_FIGURE): the answer is the two chains read bottom to top, so the same layout gets green upward arrows with the inverse operations beside each downward arrow. Labels use the book's participle wording ("Subtracting 6") on both the downward and upward arrows so they look alike; the LP steps say "subtract 6".
2. **M3.S20.T20.C120 (worked block, same chains) - none.** The chains are already the teaching image of this very concept and the block's steps write both chains out line by line, so this is the "procedure flow-chart already a concept image" case (REUSES_CONCEPT_IMAGE) and the tie-breaker says text is enough. This looks different from T21 Q1 on purpose: T21 Q1's text carries no chain at all.
3. **Ex10 (C105) and Ex11 (C107) solutions - none.** The book's printed solutions are a plain three-column layout of equation steps (p.14) and a plain Steps | Expression table with decorative orange fill (p.15). No colour, arrow or drawing carries meaning, and the LP already has the steps as numbered LaTeX lines. text_alternative on C107 offers an optional LaTeX array.
4. **Word problems (Q3 digits, Q4 brick, Q5, Q15 giraffe, Q17) - none on both sides.** All numbers are in the sentences, the book (p.18, p.25) gives no picture, and each answer is one equation. A balance picture for the brick/giraffe/quarter problems would only illustrate; same decision on all five (sibling consistency).
5. **"Write equations" questions (T21 Q1 x = -2, Q13 u = 6) and Ex13 story - none.** Open-ended, the sample answer is a list of equations in LaTeX; same decision on both (sibling consistency). Ex13 (story for 100x + 75 = 250): the book draws nothing.
6. **Q6 (a)-(e) (C127/C128) - none.** Five symbolic one-liners sharing one pair; no figure.
7. **T23 worked block (C135) - none.** Plain equation lines. An `optional` balance picture ("moves that tip the balance") was considered and not added: it would only illustrate.
8. **Figures NOT claimed here:** P18-worked_steps-1..6 and P19-worked_steps-1..3 (the nine boxes of 7.3). They are the given figures of the 7.3 questions (7.3.M1..M9, chunk E); T23 is only the intro block and its example is the LP's own (2x + 3 = 11), not one of the nine boxes. Whoever merges: they must be claimed by chunk E. Likewise P24-worked_steps-1..3 (Q11) is chunk E's (end.FiO11), P24-dimension_diagram-1 and Q12 triangles are chunk C's.
9. **Inventory entries:** P14-table-1 (none:LATEX_ARITHMETIC), P15-table-1 (none:LATEX_TABLE), P17-flow_chart-1 (concept_image:M3.S20.T20.C120.IMG1, first use), NEW-P17-flow_chart-1-q (item C123 question, second use), NEW-P17-flow_chart-1-sol (item C124 solution, third use; the upward arrows are not printed in the book). All three base descriptions checked against the page pictures: correct.
10. The two boys (Riyaz and Akash) picture on p.15 is decoration and is not in the base inventory; I did not add it (base rule: skip characters).

## 2. Things in the LP that look wrong or thin

- **C123 question text** names "each chain" and "each equation" but never states the chains. Now covered by the figure; if the figure were ever dropped, the text must carry both chains.
- **C124 step 2** writes the second equation of chain 1 as `-1 - y = -6`; the book (and the question figure) write `-y - 1 = -6`. Same expression. The solution figure keeps the book's form (a given part is not restyled); `needs_lp_text_sync: true` is set so the text can be aligned to `-y - 1 = -6` if you want exact agreement.
- **C110 question**: `question` says "Who am I?" (book wording) but `question_tex` and `text` say "Which number is this?". Two different wordings of the same item.
- **C127/C128**: the LP packs the five parts (a)-(e) of Q6 into ONE question card and ONE solution card (with extra_items). Fine for the decision (none), but they cannot get separate figures if that were ever needed.
- **C134** (Ex13): the LP's story solves to Rs 1.75 for one plate of snacks (100 plates for Rs 175). The book only suggests the story and does not solve it; the price is odd but not wrong.
- **C135** (T23): the worked example is the LP's own and does not match any of the nine boxes in the book (box 1 is 4x + 6 = 10 solved as 4x = 10 + 6). Fine as a teaching example.
- Topic names: "Questions: Example" (T18, T22) and "Many Roads to One Answer" (T19) group items loosely (Ex11 follow-up, Figure it Out Q3-Q5, end Q15 and Q17); and "Unknowns Everywhere" is an LP label, the book heading on p.18 is "Figure it Out". Book numbers Q1, Q3-Q6 (p.18) and Q10, Q13, Q15, Q17 (p.24-25) are right.

## 3. Where the book is unclear

- The book has no printed-solutions section (solutions_pages null), so the LP solution text is the only answer; nothing contradicted the LP on arithmetic (all sums in C105-C132 recomputed and hold: Ex10 x = 21 three ways, Ex11 x = 7, rule start = final / 4 + 1, 258, 2 kg, 12, 5 m, 4, 26/12/3/11/-5, 96 and 48, sample equations check).
- Page 17 Math Talk joins two questions (form the chain bottom to top; compare operations) with a third (value of the unknown without calculating); the LP merges all three into T21 Q1, so the solution figure answers the first two and the text answers the third (every equation has y = 5).
- Chain labels are printed with participles ("Multiplying by -1", "Adding y"); typography of the last node "y = 5" (upright y) differs from the others (italic): ignored.
- Layout note for the renderer: the widest labels ("Multiplying by -1", 17 characters) at 38 px fit with about 0.5 unit to spare on the 16 by 9 canvas; if one would cross the edge reduce the tag font, never below 34 px.

### Chunk E notes (from the decision agent)
# Chunk E notes (Class 7 Ch 15, topics M3.S24.T24, M4.S25.T25, M4.S26.T26, M4.S27.T27, M4.S28.T28)

Result: 35 items (21 units): required 1 / optional 0 / none 34. Validator `--chunk E`: errors 0, warnings 0.
The one required diagram is the ancient Indian notation table of the worked example `M4.S25.T25.C158` (`M4.S25.T25.C158.IMG1`).
Everything else in this chunk is equation chains, word problems and algebra: text and LaTeX.

## Borderline

1. **M4.S25.T25.C158 worked example (ancient Indian notation), REQUIRED.** The LP steps and answer carry every word of the notation
   ("yā 2 rū 8 with a dot over the 8", "yā 3 rū 4 above yā 2 rū 8"), so a strict "text carries all" reading gives `none`. I chose `required`
   (ANSWER_IS_FIGURE + HIGHLIGHT_MEANING) because the answer IS the notation table (a filled table), a dot over a digit is a mark that
   carries meaning (a negative number) and cannot be shown reliably in plain text, and "the two sides one below the other" is a layout.
   No concept image shows this table (`concept_images.json` has nothing for M4.S25), and teaching images are never linked anyway.
   Spec: 4 x 2 table, header "Modern" / "Ancient Indian" (the book's column labels, shortened), three body rows, one drawn dot over the 8
   of body row 2 only, the lower 8 of body row 3 has no dot; the book's three bracketed notes are left out (the steps carry that wording).
2. **Q11 (a) (C156 / C157), `none`.** In the book, part (a) has red slashes through the 6 of 6x and of 66 and an "11" above 66. That only
   shows how line 2 ("x + 9 = 11") arises, and line 2 is in the LP text; the LP solution also says "6x and 66 were divided by 6, but 9 was not".
   A careful student loses nothing, so `none` (LATEX_ARITHMETIC). Same decision for (b) and (c) (sibling rule). If the team wants the slashes
   kept, this is the one question to flip.
3. **Mend the Mistake boxes 1 to 9 (C138 to C155), question side `none`.** The printed boxes are in the book's inventory as "worked_steps
   given in question". They are chains of equations (LATEX_ARITHMETIC, explicitly a Step C case); the peach fill and the number badge carry no
   meaning and every line is already in the LP text. Solution side `none` too: the answer is the named mistake plus corrected equations, and the
   book has no printed answer picture. All nine boxes and Q11 (a)(b)(c) get the same decision.
4. **Summary block 4, the magic trick (C170, block 4), `none`.** A flow strip of the operations (x, then x2, +10, /2, -x, +3, giving 8) would only make it nicer (the book has
   no such figure; the only picture on p.27 is a group of children, decoration), so I did not even mark it `optional`.
5. **Cut-out sheets (P28 tangram, P30 / P32 / P34 dot paper), `none:OPEN_ENDED`.** No question, example or LP item refers to them. I claimed them
   here because they sit after the Summary (the last book section of my chunk) and no other chunk has an end section. Another chunk could claim the
   same figures with `DECORATIVE_ONLY`; any `none:` code means the same thing (no diagram, no link). The four blank cut pages (29, 31, 33, 35) carry only the
   scissors line and are not in the base inventory.
6. **P18 / P19 boxes claimed here.** Chunk D owns the teaching topic M3.S23.T23 (same book section 7.3) and may claim these nine figures too; I mapped
   them all `none:LATEX_ARITHMETIC`, which is the natural code, so a duplicate should compare equal.

## LP text issues

(No LP text was edited; suggestions only.)

- **C138, C140, C142, C144, C146, C148, C150, C152, C154 (boxes 1 to 9) and C156 (Q11 a, b, c): the steps are packed on one line.** The question_tex
  joins the printed lines with semicolons ("Box 1: 4x + 6 = 10; 4x = 10 + 6; 4x = 16; x = 4. ..."), but the solutions say "line 2", "line 3",
  "the last line", "line 5", which is hard to find in a run-on sentence. Suggested form (box 1):
  `Box $1$ (each line is one step):` followed by
  `\begin{array}{l} 4x + 6 = 10 \\ 4x = 10 + 6 \\ 4x = 16 \\ x = 4 \end{array}`, one array per box, and for Q11 one array per part (a), (b), (c).
  This is also why no picture is needed: a one-step-per-line array reproduces the book's box.
- **C143 (box 3 solution), wording.** "Mistake in line 2: the factor 2 was taken away by subtracting 2, and only from one term." The student's line 2 is
  `v - 4 = 6 - 2` (2v became v, and 2 was subtracted from the right side only). Suggested sentence: "Mistake in line 2: the 2 in 2v multiplies v, so it cannot
  be removed by subtracting 2 from the right side; either divide the whole of both sides by 2, or move -4 first."
- **C158 (ancient notation) steps, step 3 and 4.** The dot is only described in words. Suggested for step 4: "... written as yā 3 rū 4 with yā 2 rū 8 below it
  (this 8 is positive, so it has no dot): the two sides one below the other." (With the new diagram this is also visible.) If the team prefers text only,
  `yā\ 2\ r\bar{u}\ \dot{8}` in LaTeX does give a dot over the 8.
- **C160 step 4.** "the same as in Jahnavi and Sunita's savings" refers to Example 9 (m = 7, p.13-14); correct, but the learner may not remember it. Optional
  suggestion: "... m = 7, the same answer as Example 9 (Jahnavi and Sunita's savings)."
- **C170 blocks 0 to 3** are authored examples with no book number (`lp_book_number` null). Nothing wrong; noted because the items have no book reference.

Checked and found correct (recomputed): boxes 1 to 9 solutions (x = 1, z = 1/4, v = 5, z = -3, w = 26/11, x = -13/3, q = 21/8, x = 5/2, y = -3/16, each with the
LP check), Q11 (a) x = 19/2, (b) no mistake y = 6/7, (c) x = -13/5 with check -77/5 on both sides, Example 16 (100, both sides 900), Q1 of the Pinch of History
(2 and 10, checks 14 and 24), 2x + 3 = 4x + 5 (x = -1), Bakhshali (a = 4, 4 + 8 + 24 + 96 = 132), Summary examples (12, 4, 6, 12) and the magic trick (always 8, own trick always 4).

## Book unclear or misprinted

- **Box 8, line 2 (p.19):** the book prints `-6v - 8x = 14`, a stray letter v. The mathematics (and the LP) read `-6 - 8x = 14`. No diagram is drawn from it, so
  nothing is corrected in a picture; the base inventory records what the book prints and my figure entry says so.
- **Example 16 (p.20), line 2 of the solution:** the book prints `300 + 6x + (100) = 10x`. It should read `300 + 6x + 100 = 10x` (add 100 to both sides). The LP
  text ("Add 100 to both sides") is right.
- **Q11 (a) (p.24):** the red slash marks sit on the 6 of 6x and on the second 6 of 66 with "11" above; it is a hand-marked annotation, not a printed step, so
  I did not use it (see Borderline 2).
- **Pages 29, 31, 33, 35** are blank cut sheets (only the scissors line), and pages 30, 32, 34 are identical dot paper; the base inventory lists p.30, 32, 34 and
  the tangram p.28, and I claimed those four.
