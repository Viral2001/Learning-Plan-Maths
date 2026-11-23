# Notes for chunk H (Class 8 Ch 8, topic M4.S19.T19 "Questions: Putting It All Together", Figure it Out Q2 to Q15, units 110 to 123)

Result: 28 items (14 pairs): required 3 / optional 3 / none 22. Validator: errors 0, warnings 0.

| Book Q | Question concept | Question side | Solution side |
|---|---|---|---|
| 2 (match countries) | C178 / C179 | none (NUMBER_LIST_IN_BOXES) | optional, not added |
| 3 (GST) | C180 / C181 | none | none |
| 4 (mice) | C182 / C183 | none | none |
| 5 (35% then 30%) | C184 / C185 | none | none |
| 6 (dot grid, region E) | C186 / C187 | REQUIRED, C186.IMG1 | optional, not added |
| 7 (x% of y) | C188 / C189 | none | none |
| 8 (excursion) | C190 / C191 | none | optional, not added |
| 9 (pencils) | C192 / C193 | none | none |
| 10 (bus fares) | C194 / C195 | none | none |
| 11 (rectangle) | C196 / C197 | none | none |
| 12 (chips label) | C198 / C199 | REQUIRED, C198.IMG1 | none |
| 13 (three shops) | C200 / C201 | none | none |
| 14 (left-handed) | C202 / C203 | none | none |
| 15 (bar graph) | C204 / C205 | REQUIRED, C204.IMG1 | none (SAME_AS_QUESTION_DIAGRAM) |

Figures claimed (4, all checked against the page pictures, all base descriptions correct): P28-match_cards-1 (none:NUMBER_LIST_IN_BOXES), P29-dot_grid-1 (Q6 question), P29-product_label-1 (Q12 question), P30-bar_graph-1 (Q15 question). Nothing new found on pdf pages 28 to 30. The figure printed beside Q7 and Q8 on p.29 is Q6's dot grid.

## Borderline

1. **Q6 solution (C187): optional, not added.** The LP solution only counts squares (64 in all, E is half of a 4 x 4 square = 8). A copy of the question grid with E shaded would help the counting step, but nothing new is drawn and the question figure already names E. I followed Step E ("figure-based question, numeric answer: Q required, S none or optional if the solution splits the shape"). If the user wants a solution picture, it is `derived_from` C186.IMG1: same grid, E filled MARK_FILL, the 64 unit squares faintly drawn in GUIDE.
2. **Q2 solution (C179): optional, not added.** Answer is a matching (arrangement of pairs). The v3 note on NUMBER_LIST_IN_BOXES says the arrows only become a diagram on the solution side and only optional when the written answer already gives it; the LP answer lists all four matches. Also the USA (about 4.2%) has no card to join to, so a drawn matching would leave one country unmatched.
3. **Q2 question (C178): none** although the book has a picture. It is two rows of plain cards with no joining line (a list of boxed values to choose from), and the LP question text lists every card in order.
4. **Q8 solution (C191): optional, not added.** The book's hint says "Drawing a rough diagram can help", but the book draws none and the LP solution is two multiplications (0.6 x 0.4, then x 160). A bar model (100% split 40% / 60%, 60% of the 40% marked = 24%) would be the picture. No question diagram, because the question gives no figure.
5. **Q12 question (C198): required** although the LP bracket "(Label: Potato 70%, ...; net quantity 65 g)" already carries every number. Kept required under decision 4: in the book the data lives only in the picture ("shown in the picture"). Only the label data is drawn (a plain table plus 'Approximate Values' and 'NET QTY: 65 g'); the packet art, plate of chips, barcode and 'Potato Chips' brand text are left out as decoration.
   - I left out the label's own heading 'Nutritional Information' because the brief forbids headings in a picture. It is a one-line change in the spec (add it above the table) if the user wants the label complete.
6. **Q15 question (C204): required** for the same reason (graph reading, LP bracket repeats the values). The chart title, subtitle, source line and 'Data For India' emblem are not drawn (headings/branding rule); the chart's title words survive only as the horizontal axis title 'Ability to use computer (2023)', because without some axis meaning the percentages are unlabelled. Colours: book teal and amber replaced by SET_A and SET_B.
7. **Q15 Male Children bar.** The book prints no number on it (bar measured at about 4.8); LP text says about 5%. Drawn to exactly the 5% gridline and left unlabelled, as in the book. Other bars are drawn at the PRINTED labels; in the book the bars differ from their labels by up to half a unit (Twenties Male ends near 36.5 under "37%", Seniors Female near 1.5 under "2%", Fifties Female near 3.7 under "4%"), which looks like rounding in the original NSS chart. No statement (i) to (vi) depends on this.
8. **Q15 solution (C205): none (SAME_AS_QUESTION_DIAGRAM).** Each statement looks at a different group, so no single complete final picture exists that the question graph does not already show.
9. **Q5, Q11 (and Q9) solutions: none.** A bar model or a before/after rectangle would only make them nicer; the questions give no figure and the working is a single product or algebra line. I did not mark them optional because, unlike Q8, the book does not suggest a diagram.

## LP text issues

- **M4.S19.T19.C178 (Q2 question):** the card list is run together ("13% 8% 18% 10% 1% 35% 2% 2% 0.1%"), fine for the book but hard to read. Suggested: "Options: 13%, 8%, 18%, 10%, 1%, 35%, 2%, 2%, 0.1%."
- **M4.S19.T19.C179 (Q2 answer):** (a) says "about 4.2%" for the USA and then "4% is not among the options", which reads as if the answer were 4%; (b) it contains teacher-facing instructions in a student answer ("tell the student the true value and praise them for spotting it", "The other options are distractors."). Suggested: "USA: 347 million is about 4.2% of 8.2 billion. This is not among the options (and 2% is printed twice), so no card fits the USA; the other cards are distractors."
- **M4.S19.T19.C183 (Q4 answer):** "(iii) and (iv) are the $M_5$ trap." "M5" is an internal module code that means nothing to a student. Suggested: "(iii) and (iv) wrongly add or ignore the percentages; changes of percent multiply, they do not add."
- **M4.S19.T19.C186 (Q6 question):** question_tex contains an editor's bracket "(Dot-grid figure: an 8 x 8 square divided into A ... into D and E.)". Once the diagram is placed this bracket is redundant and reads as a note. It also does not say which triangle is E (D is the upper-left, E the lower-right one). Suggested: delete the bracket and keep "What percentage of area is occupied by the region marked E in the figure?"
- **M4.S19.T19.C187 (Q6 answer):** step 1 "Count squares: the whole is 8 x 8, 64 squares;" ends with a semicolon and step 2 is fine; suggested: "The whole big square is $8 \times 8 = 64$ small squares." and "E is half of a $4 \times 4$ square, so $8$ squares; $\frac{8}{64} = 12.5$%."
- **M4.S19.T19.C190 / C191 (Q8):** the LP answer says "Book data issue: ..." inside the answer; it is a note to the content team, not student text. Suggested: "24% of 160 is 38.4, which is not a whole number of students, so the numbers cannot all be exact; say about 38 and discuss why."
- **M4.S19.T19.C198 (Q12 question):** "(Label: Potato 70%, ...; net quantity 65 g)" is an editor's bracket describing the picture; once the label diagram is placed it is redundant. Suggested: "The percentage of ingredients in a 65 g chips packet is shown in the picture. Find out the weight each ingredient makes up in this packet." (the picture carries the label).
- **M4.S19.T19.C204 (Q15 question):** the long bracket "(Bar graph 'Ability to use computer by age and gender (2023)' - Children: Female 4%, Male about 5%; ... Subtitle: ... Source: ...)" is an editor's description of the graph; redundant after the diagram is placed. Suggested: delete it and keep "Look at the following graph." Also the LP says "Male about 5%" for Children, which the book itself does not print.
- **M4.S19.T19.C205 (Q15 answer):** "(iii) ... Not valid" is stronger than the book supports; the graph only shows percentages, so the statement "cannot be concluded" is the accurate verdict. Suggested: "(iii) cannot be said: the graph shows percentages within each group, not how many people each group has."
- **Duplicated numbering:** each answer's `text` field starts the steps with "$1$." and the question concepts have the book number as a prefix ("$2$. The population ..."); harmless, but the steps_tex of C179 ("Estimate with standard form, then match.") and C189 ("Compute each pair, then generalise with algebra.") are one-line placeholders, not steps. Suggested: write the actual estimate (for example $83$ million $\approx 8.3 \times 10^{7}$, $8.2$ billion $= 8.2 \times 10^{9}$, ratio about $1$%).

## Book unclear or wrong

- **Q2 cards (p.28):** "2%" is printed twice and no card shows 4%, but the USA's share is 347 million / 8.2 billion = 4.23%. The book probably meant 4% for one of the 2% cards. No Q2 diagram is made (see above), so nothing to correct in a spec; if a matching picture is ever drawn, the USA card would join "4%" (corrected value) rather than "2%".
- **Q15 graph (p.30):** the Male Children bar has no printed value, and bar lengths are slightly off the printed labels (see Borderline 7).
- **Q8 (p.29):** 24% of 160 = 38.4 is not a whole number of students; the LP already notes this. No effect on the decision.
- **Q6 (p.28 to 29):** the question is on p.28 and its figure is on the top right of p.29, beside Q7 and Q8 text; the figure is Q6's, not Q7's.
