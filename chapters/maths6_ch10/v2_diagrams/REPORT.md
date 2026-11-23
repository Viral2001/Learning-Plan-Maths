# Class 6 Ch 10 The Other Side of Zero - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths6_ch10` v91 (taken from staging). Result: new V2 version v92 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (179 items from 95 units)
{"worked_example": {"required": 5, "none": 6}, "question": {"none": 63, "required": 20, "optional": 1}, "solution": {"none": 51, "required": 22, "optional": 11}}

Optional, NOT added: [('C38', 'solution'), ('C55', 'question'), ('C104', 'solution'), ('C115', 'solution'), ('C135', 'solution'), ('C137', 'solution'), ('C160', 'solution'), ('C162', 'solution'), ('C177', 'solution'), ('C190', 'solution'), ('C192', 'solution'), ('C215', 'solution')]

needs_lp_text_sync: [('C191', 'question')]

## The 47 diagrams
| id | side | type |
|---|---|---|
| M1.S2.T2.C2.IMG2 | worked example | other |
| M1.S2.T2.C3.IMG2 | worked example | other |
| M1.S3.T3.C8.IMG1 | question | other |
| M1.S3.T3.C9.IMG1 | solution | other |
| M1.S5.T5.C24.IMG1 | question | arrow_map |
| M1.S5.T5.C25.IMG1 | solution | arrow_map |
| M1.S8.T8.C37.IMG1 | question | other |
| M1.S9.T9.C45.IMG1 | question | number_line |
| M1.S9.T9.C46.IMG1 | solution | number_line |
| M1.S9.T9.C47.IMG1 | question | number_line |
| M1.S9.T9.C48.IMG1 | solution | number_line |
| M2.S19.T19.C80.IMG1 | solution | number_line |
| M2.S19.T19.C82.IMG1 | solution | number_line |
| M2.S19.T19.C84.IMG1 | solution | number_line |
| M2.S20.T20.C85.IMG1 | question | number_line |
| M2.S20.T20.C86.IMG1 | solution | number_line |
| M2.S22.T22.C97.IMG1 | question | number_line |
| M2.S22.T22.C98.IMG1 | solution | number_line |
| M2.S22.T22.C99.IMG1 | question | number_line |
| M2.S22.T22.C100.IMG1 | solution | number_line |
| M2.S23.T23.C106.IMG1 | solution | number_line |
| M3.S25.T25.C111.IMG1 | solution | integer_tokens |
| M3.S26.T26.C113.IMG1 | solution | integer_tokens |
| M3.S27.T27.C116.IMG1 | question | integer_tokens |
| M3.S27.T27.C117.IMG1 | solution | integer_tokens |
| M3.S29.T29.C123.IMG1 | solution | integer_tokens |
| M3.S29.T29.C125.IMG1 | solution | integer_tokens |
| M3.S29.T29.C127.IMG1 | solution | integer_tokens |
| M3.S29.T29.C129.IMG1 | solution | integer_tokens |
| M3.S30.T30.C131.IMG1 | solution | integer_tokens |
| M3.S34.T34.C157.IMG1 | worked example | measurement_scale |
| M3.S35.T35.C159.IMG1 | question | other |
| M3.S35.T35.C161.IMG1 | question | other |
| M3.S35.T35.C163.IMG1 | question | other |
| M4.S36.T36.C173.IMG2 | worked example | cell_grid |
| M4.S37.T37.C176.IMG1 | question | cell_grid |
| M4.S37.T37.C178.IMG1 | question | cell_grid |
| M4.S37.T37.C179.IMG1 | solution | cell_grid |
| M4.S37.T37.C180.IMG1 | question | cell_grid |
| M4.S37.T37.C181.IMG1 | solution | cell_grid |
| M4.S37.T37.C182.IMG1 | question | cell_grid |
| M4.S37.T37.C185.IMG1 | solution | cell_grid |
| M4.S38.T38.C186.IMG2 | worked example | cell_grid |
| M4.S39.T39.C189.IMG1 | question | cell_grid |
| M4.S39.T39.C191.IMG1 | question | cell_grid |
| M4.S39.T39.C193.IMG1 | question | cell_grid |
| M4.S41.T41.C214.IMG1 | question | integer_tokens |

### Chunk A notes (from the decision agent)
# Chunk A notes (Class 6 Ch 10, plan cbse_eng_maths6_ch10_v91)

Result: 31 items (17 units: 3 worked examples, 14 pairs). Required 7, optional 1, none 23. Validator: errors 0, warnings 0.

Required diagrams (all drawn from book pictures, nothing invented):
- M1.S2.T2.C2.IMG2 (worked "Observe the floors") and M1.S2.T2.C3.IMG2 (worked "Can you spot the lift?"): the Building of Fun of pdf p.2 with the lift. Identical spec, two items.
- M1.S3.T3.C8.IMG1 (question) and M1.S3.T3.C9.IMG1 (solution, derived from C8): "Number all the floors": the lift-less tower of pdf p.3, then the same tower with the floor numbers +6 to -5.
- M1.S5.T5.C24.IMG1 (question) and M1.S5.T5.C25.IMG1 (solution, derived from C24): "Connect the inverses".
- M1.S8.T8.C37.IMG1 (question): the tower of pdf p.5 for "Who is on the lowest floor?".

## 1. Judgement calls

1. **Worked examples C2 and C3 are `required`, C4 is `none`.** C2 asks which shops are below ground and what is on the ground floor; C3 asks "Can you spot the lift?". Both can be answered only from the picture (the text names no shop and no lift position). The kept teaching images of these concepts (C2.IMG1 plain floor rows, C3.IMG1 a lift diagram) are different pictures and are never linked. C4 ("The ground floor is called Floor 0. Can you see why?") is a reasoning sentence, so `TEXT_SUFFICIENT`.
2. **M1.S3.T3.C6/C7 (four floors up, three down) are none/none.** The tower is on the same page, but the question and the printed answer (`+ + + +` or +4, `- - -` or -3) are text.
3. **Numbering question: both sides required.** Q: the order of the 12 shops and the ground line live only in the figure (FIG_REFERENCED, ACTION_ON_FIGURE). S: the answer is the numbered figure (Step B2, "answer is an arrangement / filled figure", even though the printed answer on sol p.44 is a text list).
4. **C37 (lowest floor) question is `required`.** The LP question text only says Art Centre = +2; the learner reads the floors of the Sports Centre, Cinema and Toys from the tower the book draws beside the text on pdf p.5. This is a figure the book GIVES.
5. **C38 (lowest floor) solution is `optional`, not added.** The printed answer is text only (Binnu; +2, +5, -3, -1) and the LP steps already state every floor number. A tower with Art Centre +2, Sports +5, Cinema -3, Toys -1 marked and Cinema circled would be nicer, but it is not needed (tie-breaker: only nicer). This is consistent with sibling logic: the numbering solution (C9) is `required` because its answer IS the figure; this one's answer is four numbers and a name.
6. **C14/C15 (Food Court +2) are none/none.** Book p.245 prints no figure for this question and there is no printed answer. The question gives the start (+1) and the movement (+2) in words; the same idea already exists as a teaching image (M1.S4.T4.C10.IMG1), which is never linked. Same for Gurmit (C16/C17), Basant (C18/C19, C20/C21).
7. **Figure it Out 10.1 sets (C26-C33) are all none/none**, sibling-consistent: Q1 to Q4 are arithmetic with no figure (LATEX_ARITHMETIC), Q3 is open-ended (OPEN_ENDED).
8. **Matching figure (C24/C25).** Question diagram shows the eight circled numbers with the one given line (-7 to +7) in INK; solution draws the complete final state: the given line stays INK, the three new lines (+5 to -5, -8 to +8, +9 to -9) are ANSWER green. The printed answer picture on sol p.46 (four lines, no circles) is the B2 trigger. `diagram_type` is `arrow_map` with `arrowheads: false` because the lines are plain connectors (no catalogue type for matching lines). Circles are kept in the solution to match the question figure.
9. **SOL45-matching-1** (the question reprinted on sol p.45 with the same single line) is mapped `none:SAME_AS_QUESTION_DIAGRAM`; the chapter figure P05-matching-1 is the one that becomes the question diagram. **SOL46-matching-1** becomes the solution diagram. The page picture of pdf p.5 shows the example line, so the base inventory's doubt on SOL45 is answered: the chapter page does draw it.
10. **Figure inventory entries for second uses.** The tower is used by several items, so: `P02-building-1` (C2 question), `NEW-P02-building-1-C3` (C3 question), `P03-building-1` (C8 question), `NEW-P03-building-1-C9` (C9 solution; same tower plus the numbers), `P05-building-1` (C37 question; this one is its own base figure). The `NEW-` ids are second uses of an existing base picture, not new pictures.
11. **Aspect ratio 16:9 for the tower** although the figure is tall: house-card rule. The tower is centred on a 16 x 9 card (12 rows of 0.60 = 7.20 high); the solution numbers sit left of the tower in the free space.
12. **Lift drawing.** The lift is a plain narrow rectangle with a panel of one + and one minus button at the top, no label and no tick marks. The book's small pink ticks are left out (count unreadable, no mathematics). The lift is not labelled so that C3's question ("spot the lift") is not answered by the picture.
13. **Sign names.** The LP and the picture use the signs (Books, Toys); the book's text and printed answer say "Book Store", "Toy Store". The figures use the sign names (Space, Sports, Ice Cream, Books, Art Centre, Food Court, Welcome Hall, Toys, Video Games, Cinema, Ghost House, Dinosaur), as the LP solution of C9 does.

## 2. Things in the LP that look wrong or thin

- **C14 `q_figure` and C15 `s_figure`** describe a building picture and a lift arrow "from the Food Court to the Books floor"; book p.245 has no such figure. The same `q_figure` text (a tower with no numbers) also sits on C8 and C37, where it is right (the book does print the tower there).
- **C37 question text** does not give the order of the floors; it relies on the tower. If the figure is not shown, the question cannot be done (Sports Centre, Cinema, Toys). It is why the figure is `required`.
- **C9 steps** are fuller than the printed answer (sol p.44 stops at -2 Video Game and calls the +3 floor "Book Store"); the LP wins, as the brief says.
- **C38/C37** use "Toys Store" while the printed solution says "Toys Shop" and the sign says "Toys". Harmless.
- **Numbering of Figure it Out items:** the LP calls the set on pdf p.5 (C32/C33) "Figure it Out 10.1, Q4" and its ncert_ref `10.1.FiO2.Q1`; the book prints it as a separate, unnumbered "Figure it out" with a to d, and the printed solutions label it only "Q.". Cosmetic.
- **C30 vs C31:** the question side says "if you start at Floor +2", the answer-side copy of the question says "if I start" (book wording). Cosmetic.
- Answer-side concepts repeat the question text by design; no other duplicated text found.

## 3. Places where the book is unclear

- **Lift ticks** on pdf p.2: small pink ticks along the shaft; count not readable. Left out.
- **Printed answer picture on sol p.46:** the line ends touch or overlap the printed numbers and no circles are drawn; the pairs themselves are clear (+5/-5, -7/+7, -8/+8, +9/-9). Endpoints in the spec are computed (centre to centre, clipped at the circles).
- **Floor count of the tower** is 12 shop levels with the Welcome Hall dome standing for the ground floor; the book picture on pdf p.2 draws the ground line as a slab at the dome's base, the simplified tower of p.3 and p.5 draws it under "Welcome hall". The spec follows the p.3/p.5 tower for all of them: ground line directly under Welcome Hall.

## 4. For the merge

- Base figures I did NOT claim (they belong to units of other chunks): P06-number_line-1, SOL46-compare_boxes-1, SOL46-compare_boxes-2, SOL47-number_line-1 (Figure it Out 10.1 Q1 to Q4 of pdf p.6, topic M1.S9.T9, chunk B); further figures of pdf pages 9 and later (other chunks).
- **P01-pattern-1 and P01-number_line-1 (chapter introduction, pdf p.1) belong to no unit of any chunk** (M1.S1.T1 has no question unit). Nobody may claim them; the merge will need to map them (they are intro art and an empty number ray, e.g. `none:DECORATIVE_ONLY` / `none:TEXT_SUFFICIENT`).

### Chunk B notes (from the decision agent)
# Chunk B notes (Class 6 Ch 10 "The Other Side of Zero", plan cbse_eng_maths6_ch10_v91)

Result: 29 items, required 4 / optional 1 / none 24. Validator (`--chunk B`): errors 0, warnings 0.
Output: `map/out_B.json`.

Items: M1.S9.T9 (Figure it Out 10.1, book p.247, Q1 to Q4), M2.S11.T11 (two prompts), M2.S12.T12 (Examples 2, 3, 4), M2.S13.T13 (FiO p.249),
M2.S14.T14 (two worked blocks), M2.S15.T15 (FiO p.251), M2.S16.T16 (Example 6), M2.S17.T17 (q15), M2.S18.T18 (worked block C76).

## 1. Judgement calls

1. Q3 and Q4 of Figure it Out 10.1 (M1.S9.T9.C45/C46 and C47/C48) are the only required diagrams. The book prints ONE vertical line
   (pdf p.6) for both questions, so the two question diagrams carry an identical spec (Q4's says "same as M1.S9.T9.C45.IMG1").
   I counted the ticks myself on the page picture: 25 ticks, tick 1 = A = -12, B tick 4, C tick 7, D tick 12 = -1, tick 13 = 0, E tick 14 = +1,
   F tick 15, G tick 19, H tick 24, tick 25 unlabelled. Value of tick n = n - 13, which gives B -9, C -6, F +2, G +6, H +11, the same as the LP answer.
2. Q4 question figure keeps the letters B, C, F, G, H, because the book prints them on the line even though Q4 does not use them. Leaving them out
   would change the book figure; the question figure rule says "exactly what the source prints".
3. Q3 solution is `required`, although its answer is numeric: the printed answer is a picture of the line (solutions p.47), the LP steps count ticks, and the
   complete final state (every floor numbered) is a visual the text cannot give. It is `derived_from` the Q3 question diagram. Q4 solution is `required`
   (the answer is four marked points), derived from the Q4 question diagram. Sibling consistency holds: both questions and both solutions are drawn.
4. The printed answer picture (solutions p.47) is a different, shorter line: +8 at the top to -12, 21 ticks. It cannot show F or H (+11 is off the line).
   The solution diagrams follow the QUESTION line (25 ticks, reaches +11 at tick 24), as the same-layout rule asks. The book's purple letters P, Q, R, S (and the LP's
   "P = -7, Q = -4, R = +3, S = -10") are kept; they do not continue the letters A to H, which the companion note would otherwise ask for. Book and LP win.
5. Tall figure on a 16:9 card: the line is drawn 1080 px high with 38 px between ticks and sits in the middle of the card; the sides stay empty. The aspect ratio
   field says 16:9 because the pipeline draws diagrams as 16:9 cards. Letters E and F (ticks 14 and 15) and the new letters S/P/R next to B/C/F sit one tick (38 px) apart, as in the book.
6. M2.S11.T11.C55 (Art Centre to Sports Centre) question is `optional`, not `none`, and not `required`. The book prints NO figure with it (pdf p.7), so the
   rule "required only if the book question gives the figure" is not met; the floors (Art Centre +2, Sports Centre +5) were fixed earlier in the plan. A stack of the
   12 shop signs of the Building of Fun (Space, Sports, Ice Cream, Books, Art Centre, Food Court, Welcome Hall, ground line, Toys, Video Games, Cinema, Ghost House,
   Dinosaur) would clearly help the learner count 3 floors, so I flagged it. Not added. If the user wants it drawn, this is the one item to change (it would then be a
   new question diagram; the solution stays text).
7. Questions that look like they point at a lift or mine but give no data in a figure are `none`: FiO p.251 ("check your answers by thinking about the movement in the mineshaft"),
   Example 6, q15 ("drawing or imagining a lift") and the Math Talk about the infinite lift (M2.S18.T18.C76). The infinite-lift scale (+1000 to -1000) and the mine picture are
   teaching figures; the plan already holds teaching images for them (M2.S14.T14.C65.IMG1, C66.IMG1, M2.S18.T18.C76.IMG1), which are never linked.
8. Examples 2, 3, 4 and Example 6 solutions: a short floor line would be pretty, but all numbers are in the text and the book prints no answer picture, so `none` for all four
   (same decision, so no sibling break). Same for the ten expressions of p.249 and the seven of p.251.
9. Figures left to other chunks: P11-number_line-2, P12-number_line-1, P12-number_line-2 (the 5 to 9, 9 to 3, 3 to -2 number lines) and P12-number_line-3 belong to the questions of
   topics M2.S19 / M2.S20 (chunk C). They sit in the book section "Back to the number line", which my unit M2.S18.T18 also names, but my unit (C76) uses only P11-number_line-1. If the merge
   shows nobody claimed them, give them to the chunk that holds q18 to q20 and FiO6.
10. Concept-image accounting (no linking): P09-mine-1 -> M2.S14.T14.C65.IMG1, P10-number_line-1 (infinite lift scale) -> M2.S14.T14.C66.IMG1, P11-number_line-1 -> M2.S18.T18.C76.IMG1.
    The building figures P02/P03/P05 are used by chunk A's items and are not claimed here.

## 2. Things in the LP that look wrong or odd

- Three different book question sets are all labelled `book_number` "Figure it Out 10.1, Q1": M1.S9.T9.C41 (p.247, compare floors), M2.S13.T13.C63 (p.249, Target - Start expressions)
  and M2.S15.T15.C70 (p.251, mine expressions). Only `ncert_refs` (FiO3, FiO4, FiO5) tells them apart.
- M2.S12.T12 "Example 2/3/4" are the book's "More examples a, b, c" on p.249, not numbered examples in the book. The book has no printed answer for them; the LP wrote its own steps (correct).
- Unit M2.S14.T14.C68 has `ncert_refs` [] on the unit but `10.1.q16` on its item (harmless mismatch).
- The printed solution (solutions p.48) answers the first Math Talk ("did you notice that subtracting a negative ...?") with "Yes. The infinite lift reminds us of a number line", which is the answer of the
  second Math Talk. The LP separates them correctly (C68: rule about subtracting a negative; C76: the lift is a number line). No change needed.
- Figure it Out 10.1 Q1 (d): +6 against -6, but the Building of Fun has floors -5 to +6, so floor -6 does not exist in that building. It is the book's own question; the LP step says Floor -6 is
  below the ground, which is fine for the comparison.
- All LP answers in this chunk were recomputed and match the book print: Q1 (< < < > > <), Q2 (> > > > < >), 15-5/100-10/74-34 = 10/90/40, FiO p.249 (-3, -2, +3, +2, +7, -1, -3, 0, -2, +6),
  FiO p.251 (+160, -240, +250, -150, -160, +160, -240), Example 6 (+2200), q15 (-155, +160, +160, +230, +230, +101, +101, +3000), mine sums (+100, -145, +90, -130).

## 3. Where the book is unclear

- The mine text (p.250) says the mine runs from -200 to +180, but the lowest level printed on the picture is -175 m. No item of this chunk needs the picture, so nothing was affected.
- The Q3/Q4 line on pdf p.6 has one tick above H (tick 25) with no letter and no number; on the printed answer line the top is +8. The book never says what tick 25 stands for (by the rule it is +12); the figure leaves it unlabelled.
- Q3 answer printed in the book gives F = +2 and H = +11 only as text; the printed picture does not show them. The solution diagram draws them on the question line.

### Chunk C notes (from the decision agent)
# Chunk C notes (Class 6 Ch 10, topics T19 T20 T22 T23 T25 T26 T27)

Result: 32 items = required 14 (question 4, solution 10) / optional 2 (both solution) / none 16. Validator: errors 0, warnings 0.
Required: C80 C82 C84 (hop pictures), C85+C86 (FiO Q1 line + marks), C97+C98 and C99+C100 (Examples 7 and 8, unmarked lines), C106, C111, C113 (solutions only), C116+C117 (token sets).
Optional (not added): C104, C115.

## 1. Judgement calls

- **T19 Q1-Q3 (C79/C81/C83): question none, solution required, no `derived_from`.** The start and target are in the words, and the only book picture (number line with the hop arcs) is the answer, so the question gives no figure of its own (companion note: do not invent a question figure). The solution figure is the book's picture (hops), plus a step-count label ("4 steps", "6 steps", "5 steps") that the LP solution text uses. Alternative if the user wants a bare line on the question side: add an empty 0-10 line for C79/C81 and an empty -10..10 line for C83 (the question would then need `required` and the solutions `derived_from` them).
- **FiO 10.1 Q2 (C87/C88): none.** Three empty boxes already sit in the question text; the printed answer is text (-7, -3, -1). The marked line is C86's figure. **Q3 (C89/C90): none** (word reasoning "why", printed answer is text); a -3..3 line with 2, -3, -2, 3 marked would only make it nicer. **Q4 (C91/C92): none** (six plain calculations).
- **Examples 7 and 8 questions (C97, C99): required.** The data is also in the words, so this is the closest call in the chunk. I chose required because the text says "the unmarked number line shows ..." / "the following UNL shows ...": the figure is the thing being read (only 0 and +85 marked, the -60 arrow; -100, 0, +250 with a boxed "?"). Without it the sentence points at nothing. If the reviewer prefers text-first, the fallback is question none and solutions standing alone.
- **Example 7 question figure leaves +25 unmarked** (the book prints +25 on the same picture as the answer reveal). The arrow end is still drawn to scale (12 px per unit), only the tick and label are left out. The solution adds the +25 tick/label in ANSWER.
- **T23 Q1 solution (C104): optional.** Printed answer is four numbers; LP steps (b)-(d) are arithmetic. Four small unmarked lines would show what the question asks the student to draw, but that is four pictures for one block. **Question (C103): none** (no given figure).
- **T23 Q2 (C105/C106): question none, solution required.** The book's picture (page 14) shows only the long -5 arrow (the first method). The LP solution also gives the second method (2 to 0 is -2, 0 to -3 is -3), so the solution figure draws the long arrow plus the two short arrows under it. The two short arrows are not in the book picture; they follow the LP solution and its `s_figure` hint.
- **T25/T26 (C110-C113): question none, solution required.** The book's pictures on page 15 show the already-cancelled state (grey crosses), i.e. they are the worked answer. The question gives the counts in words and no starting picture. The LP hint `q_figure` for C112 ("five green tokens in one row and eight red below") describes a starting state the book does not print, so I did not use it.
- **T27 Q1 (C114/C115): question none, solution optional.** Printed answer is four numbers (not a picture) and the question has four parts; token rows for all four would be a combined picture. This does not break sibling consistency with T25/T26, whose printed answer IS the cancelled picture. Token rows for (c) and (d) would help most (5 pairs and 2 pairs cancelled).
- **T27 Q2 (C116/C117): required/required, ONE picture for both sets** (left set = part a, right set = part b). The LP keeps both parts in one concept and the brief allows one question and one solution diagram per concept, so the book's two separate figures (P16-token_set-1/-2) are drawn side by side. The book's letters "a." and "b." are NOT drawn (rule: no figure letters); the counts in the question text (3 and 5; 6 and 3) tell the sets apart. If the merge step prefers one picture per part, split into IMG1/IMG2 per set.
- **Token colours.** The style table has no green/red, so positive tokens are SET_A (blue) and negative tokens SET_B (amber); crosses and result labels are ANSWER. The book and the T24 teaching images (C107/C108) say green/red, while C119/C120 say teal/amber, so the plan is already mixed. The question texts of this chunk use no colour words, so nothing contradicts the picture. Worth one decision before drawing.
- **Result labels in the token solutions** (+2, -3, -2, +3) are the "short numeric annotations" allowed in a solution diagram; they match the LP answers (+2, -3, Floor -2, Floor +3).
- **Number style.** Minus is the true minus sign (U+2212). Plain integers on the -10..10 lines and 0..10 ray (as in the book); plus signs on the unmarked lines (+85, +25, +250) as the book prints them.
- **Figure inventory choices.** Each figure used by two items is two entries (base id for the first use, `NEW-<id>-sol` for the solution use): P13-number_line-2, P13-number_line-3, P16-token_set-1, P16-token_set-2. P13-number_line-1 (a line with only the 0 tick) is a teaching figure, `none:TEXT_SUFFICIENT`, because the sentence beside it says the same. The reprints on solutions page 50 (SOL50-token_set-1/-2) are `none:SAME_AS_QUESTION_DIAGRAM` (drawn once in C116). SOL49-answer_boxes-1 and a NEW- entry for the matching boxes on chapter page 12 are `none:TEXT_SUFFICIENT`. P11-number_line-1 (the infinite lift turned into the -10..10 line) sits in the book section of both T18 and T19; I mapped it to `concept_image:M2.S18.T18.C76.IMG1` ("Lift on its side"). Chunk B, which holds T18, may claim it too; the meaning should match at merge. The T21 and T24 teaching topics have no units in any chunk, so their page-13 and page-15 figures are claimed here.

## 2. Things in the LP that look wrong or thin

- C97 `question_tex` / `text` read "The unmarked number line shows the addition problem 85 + (-60) = ?" but the LP `question` still has "(UNL)". With no figure the sentence points at nothing; the new question diagram fixes it. Same for C99 ("The following UNL shows ...").
- C116 `text` says "Cancel the zero pairs in the following two sets of tokens ... (a): 3 positive tokens and 5 negative tokens; (b): 6 positive ..." The sets are described in words and the picture is also given; no conflict, just redundancy.
- C106 step 2 writes (-2) + (-3) = -5 while the book writes -3 + (-2) = -5 (same value; LP `answer` uses the book's order).
- C87 depends on the student's own marks from Q1; the LP answer is a sample (-7, -3, -1) taken from the Q1 sample answer.
- C105 `q_figure` hint ("a number line with the points -3, 0 and 2 marked") describes the book's picture, which already includes the -5 arrow (the answer); not used as a question figure.
- Page numbers: the LP `book_number` strings ("Figure it Out 10.1, Q1" etc.) repeat across several Figure it Out sets of section 10.1; `ncert_refs` (e.g. 10.1.FiO6.Q1) tell them apart.

## 3. Where the book itself is unclear

- Solutions page 49: the page text lists "< < <" next to the three answer boxes of FiO Q2, but the picture shows only three empty boxes. Treated as blanks.
- Solutions page 48 (SOL48-number_line-1): the base inventory doubted whether the line is broken around the dots. I checked the picture: the dots have a small gap around them; this does not matter because the solution figure draws dots over a continuous line.
- Page 14: the -3, 0, 2 picture sits beside the "Use unmarked number lines" list (T23 Q1) but belongs to the paragraph "start at 2, go to -3" (T23 Q2).
- The book prints the hop pictures (page 11-12) with arcs and no labels; the chapter text gives the answers only in the sentence below ("4 steps", "6 steps backward", "-5").
- Printed solutions never draw the cancelled token sets for FiO 10.2 Q2 (page 50 reprints the uncancelled sets and answers in text); the crosses in C117 follow the LP solution.
- Base-inventory descriptions for every figure I claimed were checked against the page pictures (11-16, 48-50); all were correct.

### Chunk D notes (from the decision agent)
# Chunk D notes (Class 6 Ch 10, topics T29, T30, T32, T33, T34)

Result: 32 items (17 units). Required 6 (5 solution figures + 1 worked-example figure), optional 2, none 24. Validator: errors 0, warnings 0.
Required media ids: C123.IMG1, C125.IMG1, C127.IMG1, C129.IMG1 (Examples 2 to 5), C131.IMG1 (Figure it Out Q1), M3.S34.T34.C157.IMG1 (thermometers).

## 1. Judgement calls

1. Examples 2 to 5 (units 50 to 53): question side none, solution side required.
   - The questions give only numbers in words (5 and 4, 7 and 5, 5 and 6, 4 and 6), so a student loses nothing without a question figure. The book's own picture for Examples 2 and 3 is the finished take-away (struck tokens), which is the answer, so it goes on the solution side.
   - For Examples 4 and 5 the book also prints a starting picture (5 positives; 4 positives). It only repeats a number stated in the text, so those two base figures (P16-token_set-5, P17-tokens-2) are mapped none:TEXT_SUFFICIENT. A reviewer who wants "everything the book draws" could instead make these four questions required (row of 5 / 7 / 5 / 4 tokens, nothing struck).
   - Solution figures show the complete final state (struck tokens, extra zero pairs in place), as the companion note asks. The same three examples are also teaching images in topic T28 (C118 to C120) and are re-asked here; per v3 the teaching images are not linked, so each solution has its own figure. This repeats a picture the learner has just seen: a content decision for the user if repetition is a concern.
   - P17-tokens-3 (Example 5, 10 over 6 before the take-away) is mapped to the C129 solution item: that exact arrangement is redrawn inside the final figure.
2. Figure it Out 10.2 Q1 (unit 54): the printed answers are six token pictures (B2), so the solution is required. The LP keeps parts a to f in ONE block, and the brief allows one solution diagram per pair, so it is ONE six-panel picture (2 columns x 3 rows, order a b / c d / e f). The panels carry no part letters (v3 forbids them); each panel has its expression and result as a caption so that it can be matched to the part. Captions use the LP result style "= +3" (the book prints "= (+3)") and leave out the book's extra "= (-8) + (+4)" step of parts b and c. If the user wants one picture per part (the v3 rule "never one combined picture"), the LP block must first be split into six pairs.
3. Siblings in the 10.2 Figure it Out boxes: Q1 (printed answers are pictures) is required. Q2 "Complete the subtractions" (answers are numbers, no mention of tokens) is none. Q3 and Q4 (second box, Q4 says "using tokens") are optional only, because the book's printed answers there are numbers only (-8 with five zero pairs; -13, +15, -14, -19, +10, -9). Q4 has the same instruction as Q1 but a different kind of printed answer, so I did not promote it; if the user wants Q4 treated like Q1 it would be a second six-panel token figure (a to f: 3 neg + 10 pairs, 8 pos + 7 pairs, 5 neg + 9 pairs, 9 neg + 10 pairs, 6 pos + 4 pairs, 2 neg + 7 pairs). THIS IS THE ONE CALL WORTH A USER DECISION.
4. Credits and debits (units 58 to 61) and Figure it Out 10.3 (units 62 to 64): all none. The book prints no figure anywhere; every answer is one line of arithmetic (LATEX_ARITHMETIC) or sentences (Q3 open-ended). The teaching images C138 (credit bar) and C139 (balance line 130 to -20) exist but are never linked; a number line for 130 - 150 = -20 would only be nicer, so not even optional.
5. Unit 65 (the "find out" temperature question): none, OPEN_ENDED (a local fact to look up, no figure).
6. Unit 66 (two thermometers showing 40 and 15 degrees C): required. The question says "Look at the two thermometers", the data (scale continuing to -20, the two levels) lives only in the picture. Concept image C156.IMG1 is a different picture (one vertical scale with 0 and -3) and is not linked. One figure holds both thermometers (two base figures P21-thermometer-1 and P21-thermometer-2 map to the same item). Tall figure placed on the 16:9 card.
7. Token colour convention for the whole chunk: positive token = MARK_FILL disc with INK plus, negative token = SET_B disc with INK minus, struck-out = one INK slash (lower-left to upper-right). The book uses green and orange-red, so MARK_FILL (light green) and SET_B (orange) stay close to it. The slash is INK, not ANSWER green: green on the orange tokens would be hard to see, and there is no question figure to tell "given" from "added". Other chunks that draw tokens (units 46 to 49) should use the same convention so the chapter looks the same.
8. Thermometer details: labels -10 and -20 are INK (the book prints them in red; red is not a style token), liquid is SET_B, no reading labels (the readings are in the question text), right thermometer drawn at exactly 15 (see section 3).

## 2. Things in the LP that look wrong or odd

- C126 and C128 (Examples 4 and 5, question concepts) put the whole method into the question text ("put out an extra zero pair ... now we can take out 6 positives"; "we put down 6 zero pairs ... now we can take away 6 negatives"), so the question already gives away the method the solution then repeats. Not wrong, but the question side reads like a solution.
- Numbering: the LP calls the second 10.2 Figure it Out box Q3 and Q4 (book_number "Figure it Out 10.2, Q3/Q4", ncert refs FiO3.Q1 / FiO3.Q2), while the book and the printed solutions number that box Q1 and Q2 again (printed "Page No. 259 Q.1, Q.2"). Matching by text, not by number, was needed.
- Unit 65: item ncert_refs list both 10.3.q5 and 10.3.q6, but the block only holds the q5 "find out" question; q6 (thermometers) is the next unit (66), whose unit-level ncert_refs is empty (only its item says 10.3.q6).
- C131 (Q1 answers): the LP answer text gives only the values; the printed book answers also show for (b) and (c) the equivalent step "(-8) - (-4) = (-8) + (+4)". The LP steps for (d), (e), (f) match the printed pictures exactly (3, 2, 4 zero pairs).
- All arithmetic in the units was rechecked and is correct: Examples 5-4=1, -7+5=-2, 5-6=-1, 4+6=10; Q1 +3, -4, -5, -3, +2, +4; Q2 +2, -3, +2, -5, +5, -12; Q3 -8; Q4 -13, +15, -14, -19, +10, -9; bank 160, 130, -20, 180; FiO 10.3 Q1 120 - 150 = -30; Q2 255 and 256 - 255 = 1.

## 3. Where the book is unclear or inconsistent

- Right thermometer (p.21 / p.262): the book text and the LP say 15 degrees C, but the red column in the printed picture ends at about 16 (first minor tick under the 20 mark is 18, the next 16). Drawn at 15; said in render_note.
- Figure it Out Q1(f) printed answer picture (solutions p.51): 6 negatives over 4 positives with NO slashes, unlike (a) to (e). Whether it is a book defect or a copy defect cannot be told; the figure strikes the 6 negatives as the LP step says.
- Q1(e) printed answer is split by the page break (7 struck negatives at the bottom of solutions p.50, the 2 positives and the equation at the top of p.51). Treated as one picture.
- Example 4 in the book is spread over two pages (start state on p.257, finished state on p.258); Example 5 over one page in three pictures. One finished-state figure per example is drawn.
- The book's thermometer ticks are dense; the base inventory says 4 minor ticks between labelled values (2 degrees each), which I checked on a zoomed crop and used.

### Chunk E notes (from the decision agent)
# Chunk E notes (Class 6 Ch 10, topics M3.S35.T35, M4.S36.T36, M4.S37.T37, M4.S38.T38, M4.S39.T39)

Result: 32 items = 15 required (10 question, 3 solution, 2 worked example), 5 optional (all solutions), 12 none. Validator: errors 0, 1 warning (T37 C185 solution is a made-up sample puzzle, not a book figure, so no inventory figure maps to it; expected).
Figure inventory: 30 entries (19 base figures claimed + 11 `NEW-` entries for further uses of one picture), 0 concept images, unmapped 0.

## 1. Judgement calls

1. **Same picture, one diagram per item.** Cross-section chart x3 (T35 Q1, Q2, Q3), second hollow grid x2 (T36 worked example C173 and T37 Q1), the three Q2 grids x2 (T37 Q2 and Q4), the orange/blue grids x2 (T39 Q2 and Q3). Each is a separate required item with an identical spec and a "same as <id>" render_note; further uses are `NEW-<base id>-<suffix>` inventory entries.
2. **Question that points back at a figure printed elsewhere = required, not `none`.** T37 Q1 ("the second grid above", no numbers in the text), T37 Q3 ("the last grid above"), T37 Q4 ("which other grids", no data in the text), T39 Q1 ("Try afresh": the 16 numbers of the game grid are not in the question), T39 Q3 ("these grids"). Reason: the learner cannot attempt them without the picture (tie-breaker); none of them meets the full 'refer picture' rule of Step B2 (that rule needs the book's answer to only point at a picture and the very same picture to be a concept image). The alternative for T39 Q1 would be `optional` + a text sentence (`needs_lp_text_sync`); I chose the diagram because the T38 teaching image (3, -5, 7, -6 circled) is a play of the game, not the plain grid. Please confirm.
3. **T37 Q4 and T39 Q3 are discussion questions** (reasoning in words), yet their questions are `required` because "these/other grids" is unanswerable without seeing the grids; their solutions are `none` / `none` (reasoning is text; the new sample grid of T39 Q3 is a plain number grid = LaTeX array).
4. **Solutions.** Required only where the answer IS a filled grid or puzzle: T37 Q2 (printed answer is a picture; derived from the question diagram), T37 Q3 (LP sample filling, derived), T37 Q5 (sample puzzle, no question diagram so `derived_from` null; clues INK, numbers to find ANSWER green). Optional (not added, reason names the figure that would help): T35 Q1 (leader lines with heights), T35 Q2 (ring on A and D), T37 Q1 (the four sums beside the grid, the Step D example), T39 Q1 and Q2 (one sample try circled and struck). T35 Q3 = none (answer is two letter sequences). T35 Q4, Q5, Q6 = none (words / open). T35 Q7 solution = none (`LATEX_TABLE`): the printed answer is a plain ruled 2-column table, not lines drawn between columns, although the LP's `s_figure` speaks of "joined by lines".
5. **T35 Q7 question = none** (`LATEX_TABLE`): two plain unmatched one-column tables, both lists already in the question text.
6. **T36 worked example (C173) = required** although the text lists every number: the whole idea is the hollow square and its four sides, the book prints it as a figure, the same grid is a required question figure in T37 Q1, and the teaching image of the concept shows only the top row (never linked). The diagram shows the given cells only, no sums.
7. **T38 worked example (C186) = required, four-panel strip** (the book's four step pictures: -1, then 9, then -7, then -2, each with its row and column struck). The book colours each ring-and-line pair differently; here rings are FOCUS and lines GUIDE (no token for four pairs). One 16:9 card holds four 400 px grids (cell 100 px, number 44 px). The plain starting grid (P23-grid-4) is panel 1 without marks, so it maps to the same item; the flow chart (P23-flowchart-1) = `TEXT_SUFFICIENT` (the LP's own three step lines).
8. **Cross-section frame.** The book frame ends at 1500 and its dot A sits just under that edge (about 1450). To make A readable as the printed +1500 I extended the frame to +1800 and put A on the 1500 line. All seven heights follow the printed answers (A +1500, B -500, C +300, D -1200, E +1200, F -200, G +100); the curve shape is traced from the page picture (48 control points, PCHIP). A preview of the curve was checked against `page_20.png`.
9. **Labels "Border sum +4 / -2 / -4" and "Border sum 0".** The book prints them as italic captions; the prompt lists captions under "never". I kept them as short (3-word) labels because the target sum is given data that decides each grid, and the LP text states it too. No grid letters A/B/C are drawn (the book has none; the LP text uses them, the border-sum labels identify the grids in the same left-to-right order).
10. **Minus sign.** All diagrams use the LP's U+2212 minus; the book prints a plain hyphen or en dash. The orange/blue colours are carried by SET_B / SET_A cell outlines (the LP text calls them Grid 1 orange, Grid 2 blue).
11. **Not claimed here:** P21-thermometer-1/2 (40 C and 15 C thermometers) belong to M3.S34.T34 / unit 66 (chunk D, "Look at the two thermometers showing 40 and 15"); the other chunk has to claim them.

## 2. Things in the LP that look wrong or thin

- **T39 Q2 (C191 and C192) question text** lists each grid twice ("Grid 1 (orange): 7 10 13 16 / ... Grid 2 (blue): ... Grid 1) Play on ... Grid 2) Play on ..."): duplicated, and with the diagram in place the data lines can be dropped.
- **Orange grid, row 4 column 2.** Book and LP both have -7, but with -7 the sum is not constant (e.g. circling -7 (row 4, column 2), 16, 4 and -11 (row 3, column 1) gives 2, not -8). The printed answer -8 and the LP tries (7, 1, -5, -11 and 16, 4, -8, -20) only work for **-17**. The LP tries happen to avoid that cell. I drew -7 as printed (rule: never invent a number) and flagged it in the render_note of C191 and C193. Decision needed from the user: keep -7 or correct to -17 in the picture and the LP text.
- **T37 Q2 solution (C179).** The LP's sample for Grid A is -10, 8, 6 / 5, -5 / 9, -8, 3; the book prints -10, 10, 4 / 5, -5 / 9, -10, 5. Both satisfy border sum +4; LP wins (diagram follows the LP). Grids B and C equal the book.
- **T37 Q3 solution (C181).** The LP `s_figure` says "two different complete fillings" but the LP steps and answer give one (p = -2, r = -3). Only that one is drawn; it equals the printed Q2 third-grid answer.
- **T37 Q1, Q3, Q4 and T39 Q1, Q3 question texts** rely on a figure for their data (see judgement call 2). Texts left as they are; the diagram supplies it.
- **Book numbering clash:** T37 items are "Figure it Out 10.4, Q1-Q5" (hollow grids) and T39 items "Figure it Out 10.4, Q1-Q3" (amazing grid): same label, different sets (the book prints two separate Figure it Out boxes; a third is T41).
- **T35 Q6** answer_tex reads "Open-ended research question (e.g. ...)", fine as a sample but the book prints no answer for it.
- **T38 C187 teaching text** (not my unit, noted for the reader) says rows 2 to 4 are "5 less / 2 less / 10 less" than row 1; these match the grid (row 2 = row 1 - 5, row 3 = row 1 - 2, row 4 = row 1 - 10), no problem.

## 3. Where the book is unclear

- Cross-section heights are not printed in the question; the printed answers are "approximate" and the picture reads A about 1450, C about 275, G about 110, B about -520, F about -210 (see judgement call 8).
- Orange grid -7 vs -17 (above).
- The book's amazing-grid example is four pictures with four colours; the colour of each ring-and-line pair has no stated meaning, only the circled numbers (-1, 9, -7, -2) and their sum -1 are stated.
- The solutions page prints Q2 grid answers as plain ruled grids with the caption "Border sum +4" etc.; the printed answer of FiO 10.4 Q3 is just "Think of other ways" after the Q2 grids (no separate Q3 picture).

### Chunk F notes (from the decision agent)
# Notes, chunk F (Class 6 Ch 10, plan cbse_eng_maths6_ch10_v91)

Units: Figure it Out 10.4 Q1-Q9 (M4.S41.T41), Figure it Out 10.5 Q1-Q2 (M4.S43.T43), Snakes and Ladders worked example (M4.S44.T44).
Result: 23 items, required 1 / optional 1 / none 21. The validator prints errors 0.

## 1. Judgement calls

- **Q9 question (M4.S41.T41.C214): required.** The question text says only "a particular pattern"; which tokens are positive or negative exists only in the picture (book pdf p.25, reprinted on solutions p.56). Media id `M4.S41.T41.C214.IMG1`. Spec: 15 touching tokens, + + + - - three times (9 positive, 6 negative), then a wavy line curling down. Only 15 of the 100 tokens are drawn, as in the book. The picture carries no number (no 100, no 20) and no grouping marks, so the answer is not given away.
- **Q9 solution (C215): optional, not added.** A copy of the string with three brackets of 5 tokens, each marked +1, would help the "block of 5 = +1" step. The steps say it in words and the question figure already shows the pattern, so I did not make it required. Ask me if you want it required.
- **Token colours.** The book uses green for positive and orange-red for negative. The style table has no token colours. I used MARK_FILL (pale green) for positive and SET_B (amber) for negative, with INK outline and INK signs. The printed + or - sign carries the meaning. WRONG (orange-red) is reserved for wrong cases and ANSWER (green) for solution additions, so I did not use them. If other chunks colour their tokens differently (for example teal and amber like the existing teaching images), the merge may want one palette for all token pictures. The `render_note` says so.
- **Q4 (expressions table): none on both sides, `LATEX_TABLE`.** The question table is a plain 2 x 4 table of expressions. The printed answer (solutions p.55) is a plain black-ruled table of numbers, not a picture in the sense of rule B2. `text_alternative` gives the LaTeX arrays to write.
- **Q1, Q3, Q5, Q6, Q7, Q8: none.** All are in words, equations or number lists. I considered a number line for Q1 and Q3 (marking the integers between, or the impossible dice sums) and a timeline for Q5. All would only make it nicer, and the tie-breaker says none.
- **10.5 Q1 solution: none** (`OPEN_ENDED`, `TEXT_SUFFICIENT`). One picture cannot serve the ten rules. The lift and number-line ideas for 2 + (-3) and 2 - (-3) are already concept images of earlier topics (and are never linked). 10.5 Q2 solution: none (ten sample equations).
- **Snakes and Ladders worked example: none.** The rules are complete in words and the answer is only "play the game". The kept concept image `M4.S44.T44.C224.IMG1` already shows the move idea. The book's board (P30-board-1) is game artwork. Its snakes and ladders overlap and hide numbers, and their ends are only approximately readable, so I mapped it to `none:NOT_RENDERABLE`. The two dice (P30-dice-1) are `DECORATIVE_ONLY`, because the numbers +1 to +6 and -1 to -6 are in the text. If the team wants the board, a plain numbered track (START 0, +1 to +50 and -1 to -50 on a snake path) could be drawn as an optional worked-example figure. Without the snakes and ladders it would be a different picture from the book's.
- **Figures claimed beyond the units' own pages.** The seven Learning Material Sheets figures (P32 to P40: two dot sheets, two squared sheets, tangram, fraction wall, tile sheet) follow chunk F's last topic and belong to no unit, so I claimed them all as `none:DECORATIVE_ONLY`. Nothing in the plan uses them. They are blank or cut-out material. If another chunk also claims them, the meaning is the same.
- **Figures not claimed.** The Figure it Out 10.4 "amazing grid" pictures (P24-grid-1, P24-grid-2, SOL55-grid-1, SOL55-grid-2) belong to the amazing-grid questions, which are chunk E's. I left them.
- **Printed-solution figures of my questions:** SOL55-table-1 (reprint of the Q4 table) is `LATEX_TABLE`. SOL55-table-2 (Q4 answer table) is `LATEX_TABLE`. SOL56-token_string-1 (reprint of the Q9 string) is `SAME_AS_QUESTION_DIAGRAM`, because the question's own figure P25-tokens-1 is the one drawn.

## 2. Things in the LP that look wrong or thin

- **Q4 question text** (M4.S41.T41.C204): it contains the stray build note "(table of $8$ expressions, row $1$ then row $2$)" and invents the letters (a) to (h). The book has no letters, only a table. The solution uses the same letters, so it is consistent, but the parenthetical should go before this reaches learners.
- **Q9 question text** gives no pattern, so the plan depends entirely on the diagram token. If the diagram were ever dropped, the question could not be answered.
- **Q9 solution wording** says "green" and "red" tokens. The new picture shows pale green and amber tokens with +/- signs. Suggest "positive (+) tokens" and "negative (-) tokens", or accept the small colour difference.
- **Q5 (a) and (b)** assume the present year is 2026 and the LP says so in the answer. The book prints only the answer to (c), "-360 BCE". The LP writes "360 BCE", which is the same year. The LP's own work checks out: 2026 - 2200 = -174, which is 175 BCE because there is no year 0.
- **Q6 (c)** The LP and the book agree: 27, 19, [12, 6, 1, -3, -6], -8, -9, -9. The book prints it as "27, 19, ... -8, -9, -9".
- I recomputed the other answers (Q1 lists, Q3 sums: 15 possible and 8 missing, Q4 all eight values, Q7 = -30, Q8 sign rules, the 10.5 Q2 sample equations). All agree with the book's printed answers.
- The book prints no answers for 10.5 Figure it Out Q1 and Q2 (open-ended). The LP's sample answers are the LP's own.

## 3. Places where the book is unclear

- **P30-dice-1:** the third face of the blue (negative) die is partly turned away, so its sign cannot be read ("4" or "-4"). It is not drawn, so it does not matter.
- **P30-board-1:** snake and ladder ends cannot be read exactly; some cell numbers (for example -1, 43, 18) are hidden under the artwork.
- Q9's string: the book draws only 15 tokens and a wavy end for a string of 100. The 100-token pattern (5 repeating, + + + - -) is inferred, as the LP does.
