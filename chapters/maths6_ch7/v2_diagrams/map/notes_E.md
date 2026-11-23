# Notes, chunk E (Class 6 Ch 7 Fractions, topics M3.S21.T21 to M3.S25.T25)

Result: 24 items (14 units). required 1 / optional 1 / none 22. Validator `--chunk E`: errors 0, warnings 0.

I looked at the page pictures of pp.19-27 (chapter) and pp.44-47 (printed answers). The only pictures with maths content in this chunk are the four chikki strips on p.25 and the answer number line on solutions p.47; the rest of the pages are text and the two girl characters.

## 1. Judgement calls

- **M3.S25.T25.C147 (solution) - required.** The printed answer to the p.177 question is a number-line picture (0 to 2 in sevenths, start 4/7, six hops of 1/7, land on 10/7, caption "+ 6/7"). I checked tick positions against the picture (4/7 at tick 5, 1 at tick 8, 10/7 at tick 11, 2 at tick 15). The question gives no number line, so the solution draws the whole line itself, `derived_from` null. Colours: given labels INK, the 10/7 label and dot, the six hops and the caption in ANSWER. The two dots are my own extra marks (not in the book, no data).
- **M3.S25.T25.C146 (question) - none.** The book asks the student to draw the number line, so nothing is given. A blank line would imply a given figure (companion note).
- **M3.S24.T24.C142 (worked example, Meena's chikki) - optional (not added).** The strip model (4 pieces, Meena 2, brother 1, one left) clearly helps and the book teaches by it, but the text and the four steps are complete and the same final picture is already this concept's kept teaching image `M3.S24.T24.C142.IMG1`. If the user wants a diagram per worked example anyway, make it required: one 4-piece bar, pieces 1-2 labelled Meena 1/2 = 2/4, piece 3 brother 1/4, piece 4 left.
- **M3.S25.T25.C144 / C145 (how much chikki is remaining) - none / none.** The book question follows the "Total chikki eaten" strip (p.25, P25-4), but the LP question text already states the 3/4 eaten, and the solution is `4/4 - 3/4 = 1/4`. The book prints no answer for it. Slight tension with C142 being optional: I kept C145 as none because it is a one-line subtraction, not the first visual introduction of adding.
- **T22 chikki and juice questions (C126 to C135) - all none.** Comparisons by common denominator are LaTeX arithmetic. The "1/2 = 4/8 against 5/8" strip is already the teaching image `M3.S21.T21.C120.IMG1` and "3/4 against 7/10" is `M3.S21.T21.C121.IMG1` (neither is linked).
- **T23 ordering questions (C139, C141) - none.** The printed answers are text inequality chains, not drawings, so I did not treat "ascending/descending order" as an arrangement answer (Step B2). A number line would be optional at most; I judged it unnecessary.
- **Figures I did not claim.** The strip pictures on pp.26-27 (P26-fraction_strip-1..4, P27-fraction_strip-1..3: 2/5 + 1/5 and 4/7 + 6/7 examples) belong to the units of topic M3.S26.T26 (Examples 2 and 3), so I left them to the chunk that holds T26. They are in section 7.8 like my units, so please check at merge that exactly that chunk claims them. They are not given figures of my C146 question, which asks for a number line.
- **Figure mapping.** P25-1 (unmarked whole bar) is `none:TEXT_SUFFICIENT`; P25-2, P25-3, P25-4 are `concept_image:M3.S24.T24.C142.IMG1` (accounting only). All four base descriptions matched the picture (pale pieces are the eaten ones, the dark piece is what is left).

## 2. Things in the LP that look wrong or odd

- Book p.19 (not the LP): Mukta says "We must compare 1/7 and 4/7" for the "1 chikki among 2 or 4 chikkis among 7" question. It should be 1/2 and 4/7; the LP (C128/C129) correctly uses 1/2.
- C133 (juice question): the LP solution answers all three parts; the book prints an answer only for part 2 (and reads "Each child's share in group 1 = 4/7", meaning part 2 group 1). The part 1 answer (3/4 > 7/10) comes from the book text on p.171. The LP wins, no conflict in the numbers.
- C122, C123 and C124 are three separate concepts all named "Making the fractional units the same" (cosmetic; each holds one worked example).
- C131 `answer_tex` writes `$2\text{ units}$` and `$4\text{ units}$` with `\text{}` for a plain number plus word; renders fine but is inconsistent with the other items.
- C142's `ncert_refs` is 7.8.q1 for the worked example; its teaching block (block 0 in the plan) also carries the later 2/5 + 1/5 and 4/7 + 6/7 text. Not a problem for this map (the item is none/optional); the unit's `block_index` 0 counts question blocks only, as the rollout script does.
- All fraction arithmetic in the T21, T22 and T23 solutions was recomputed (3/4 = 30/40, 7/10 = 28/40; 4/5 = 36/45, 7/9 = 35/45; 7/9 = 49/63, 17/21 = 51/63; the eight pairs of Q5; Figure it Out Q1 to Q3 conversions to 6, 63, 70, 30, 24, 32 and 60). No errors found; the LP answers agree with the printed ones.

## 3. Places where the book itself is unclear

- p.25 strips: the book never says in words that the pale pieces are the eaten ones; it is read from the arrows ("Meena ate", "Brother ate", "Total chikki eaten") pointing at the pale pieces. This affects the optional C142 figure only.
- Solutions p.47 number line: the picture has no labels on the hops and no 1 3/7 mark; the mixed number is only in the text next to it. The spec follows the picture.
