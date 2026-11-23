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
