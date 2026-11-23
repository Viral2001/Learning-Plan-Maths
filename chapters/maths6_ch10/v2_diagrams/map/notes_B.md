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
