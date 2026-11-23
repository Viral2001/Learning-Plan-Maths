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
