# Notes, chunk D (Class 8 Ch 8 "Fractions in Disguise")

Units: M3.S9.T9 (Examples 1, 2, 3), M3.S10.T10 (four Figure it Out questions), M3.S11.T11 (six worked blocks C97, C98, C99, C101, C102, C104).
Result: 20 items, required 0 / optional 0 / none 20. Validator: errors 0, warnings 0.

Nothing in this chunk needs a drawn diagram under the v3 rules: every figure of the chunk is a plain table or list of numbers, or a teaching figure that already exists as a concept image, and every question and solution is arithmetic or word reasoning. Every `none` item carries reason codes, a one-line reason and, where it helps, a `text_alternative`.

## Figures claimed (6)
- P15-label-1, P15-label-2 (the two badam pack labels), P15-table-1 (table to complete): `none:LATEX_TABLE`. Values re-read on the enlarged page picture: DEF 99, 30, 12, 9 g, total 150 g; Zacni 272, 64, 40, 24 g, total 400 g; table shows only 66% under DEF Sugar.
- P16-flow_diagram-1 (sweater journey): `concept_image:M3.S11.T11.C97.IMG1` (the concept image shows exactly this figure and its price tags).
- P18-bar_model-1 and P18-bar_model-2 (Manisha's two bars): both `concept_image:M3.S11.T11.C101.IMG1` (that one image holds both bars).
- Base descriptions of all six agree with the page pictures; no "CORRECTED" entries.

Figures next to my units that I did NOT claim, because their book section is a unit of chunk E (merge check will see them there): P17-bar_model-1 (Example 4, Kishanlal's percentage profit, C105), P17-bar_model-2 (Example 5, Raghu's rice, C113), P19-receipt-1 (Example 9, "check the bill", C121). If chunk E does not claim them, the merged map will report them as unclaimed.

## Borderline
1. M3.S9.T9.C85 (Example 2 question, KYC table): `none`, LATEX_TABLE + DECORATIVE_ONLY, `needs_lp_text_sync: true`. The data lives only in the book picture, so this is the call most open to challenge. I judged the two labels as plain ingredient/weight lists (no colour, position or arrows carry meaning; the pouch, almonds, barcode and how-to-use strip are decoration), the same kind of thing as the number lists the audit removed, and the table to complete is a plain table like P07/P08/P12. If you want the labels drawn instead, the figure would be one 16:9 `other` diagram with two label cards (DEF and Zacni, ingredient names and grams, total weight line) plus the table with 66% in the DEF Sugar cell, and the solution a derived diagram with the other 7 cells in ANSWER green. Say so and I will write the spec.
2. M3.S9.T9.C86 (Example 2 solution): `none`. A filled percentage table is a numeric table (LATEX_TABLE), not ANSWER_IS_FIGURE. Consistent with the question side.
3. M3.S11.T11.C97 (Kishanlal's profit): `none`. Numbers are in the book text, answer is 430 - 300 = 130, and the sweater journey is this concept's own teaching image (never linked).
4. M3.S11.T11.C98 (crayon box, check my thinking): `none`. Multiple choice in words; the book draws nothing for it; the five-part ₹10 bar is the teaching image C98.IMG1.
5. M3.S11.T11.C102 (Manisha, 50% or 33.33%): `none`. The book draws two bars, but they are teaching figures (concept image C101.IMG1) and the example does not refer to them; the numbers are three simple fractions. An optional two-bar picture (₹250 over ₹500 = 50%, over ₹750 = 33.33%) would help but only repeats C101.IMG1, so I did not mark it optional.
6. M3.S10.T10 (all four pairs): `none` on both sides, consistent with each other (no figure in the book, solutions are one or two lines of arithmetic).

## LP text issues
(No LP text was edited; no decision was changed because of these.)
- M3.S9.T9.C83 (Example 1 question): text is only "Eesha: English or Science?"; the marks are missing. Suggested: "Eesha scored 42 out of 50 in English and 70 out of 80 in Science. She lost only 8 marks in English but 10 in Science, so she thinks she did better in English. Reema says Science, since she scored more marks there. Vishu says the scores cannot be compared because the maximum marks differ. Who is correct?"
- M3.S9.T9.C85 (Example 2 question): text is only "$KYC$ table", with no label data and no table. Suggested: "DEF pack (total 150 g): sugar 99 g, milk solids 30 g, badam powder 12 g, food chemicals 9 g. Zacni pack (total 400 g): sugar 272 g, milk solids 64 g, badam powder 40 g, food chemicals 24 g. Complete the table of percentages (DEF sugar is 66%): which product has the larger share of badam, which the smaller share of food chemicals?" (a LaTeX array for the table is in the item's `text_alternative`). Also KYC should be plain text, not math mode.
- M3.S9.T9.C86 (Example 2 answer): `answer_tex` has "$(6$%)" (the bracket is opened inside the math and closed outside); write "(6%)" as "($6$%)". Values checked: 99/150, 30/150, 12/150, 9/150 = 66, 20, 8, 6; 272/400, 64/400, 40/400, 24/400 = 68, 16, 10, 6; both rows add to 100.
- M3.S9.T9.C87 (Example 3 question): the two statements are missing. Suggested: "(i) The population of this state in 1991 is 165% of that in 1961. (ii) The population of this state has increased by 65% from 1961 to 1991. Do the two statements mean the same thing?"
- M3.S10.T10.C90 (petrol answer): the learner text shows an internal code, "(M_2)" / "(M2)". Suggested: "Option (ii), 40%, is wrong: it takes the new price (₹100) as the base instead of the old price (₹60)." Also "About 66.66%" is 66.67% rounded; the book's option (iv) prints 66.66%, so keep the LP wording but it is a truncation.
- M3.S10.T10.C96 (cameras answer): explains only why (v) is wrong, but (i), (ii), (iv), (v) and (vi) are all wrong. Suggested: "Only (iii). After an 85% fall, 15% is left, so now is 15% of a decade ago. (i) uses 85% as what is left. (ii), (iv), (v) turn the base around: a decade ago was about 667% of now (1/0.15), not 85%, 15% or 185%."
- M3.S11.T11.C97 (Kishanlal's profit): no numbers in the block. Suggested: "Kishanlal buys a sweater at ₹300 (cost price) and sells it at ₹430 (selling price). What is his profit?" and step "430 - 300 = 130".
- M3.S11.T11.C98 (crayon box): the unit's ncert_refs says "1.3.ex5_per_kg", which is Raghu's rice; the crayon question is the unnumbered one on p.17. The block text also holds tutor wording ("How sure are you?" with three emoji, "Act on the diagnosis table.") that reads as a script, not learner text. The option arithmetic is consistent: (a) 37.50 = 50 - 12.50, (b) 40 = 50 / 1.25, (c) 62.50 = 50 + 12.50.
- M3.S11.T11.C99 (Per kg?): the question gives no data. Suggested: "Raghu bought rice at ₹35 per kg and sold 10 kg for ₹300, that is ₹30 per kg. Is the percentage loss per kg the same as the loss on all 10 kg?" LP answer "about 14.29%" is the correct rounding of 5/35 = 50/350 = 14.2857; the book prints 14.28% in Example 5 (see below).
- M3.S11.T11.C101 (gross and net profit): no data in the block. Suggested: "Kishanlal's sales last month were ₹80,000; the goods he sold cost ₹48,000; his other expenses were ₹8,000. Find the gross profit and the net profit." Checked: 32,000 and 24,000.
- M3.S11.T11.C102 (Manisha): no data in the block. Suggested: "Manisha buys a bag of fertiliser at ₹500 and sells it at ₹750. Is her profit 50% or 33.33%? In a month her sales are ₹1,50,000, the goods cost ₹1,00,000 and expenses are ₹5,000: what percent of the monthly revenue is her net profit?" Checked: 250/500 = 50%, 250/750 = 33.33%, 45,000/1,50,000 = 30%.
- M3.S11.T11.C104 (A Bill from Home): the "answer" is a tutor instruction ("Open; the AI checks the student's bill"), not learner text. Worth rewording or hiding.

## Places where the book itself is unclear or inconsistent
- Page 15: the Zacni pack brand is hand-lettered "Zachi", while the table and text say "Zacni". Same product; I kept "Zacni" everywhere.
- Pages 19 and 20: Figure it Out numbering repeats. Page 19 lists questions 1 to 5 and page 20 starts again at 3 (3 to 9), so "3", "4" and "5" each occur twice. The LP book_number "5" is used for both the petrol question (p.19) and the rice question (p.20). I used the page in `ncert_ref` to tell them apart.
- Option (iv) of the petrol question prints 66.66%, the exact value is 66.666...%; the book intends (iv) as the answer.
- Example 5 (chunk E) prints 14.28%; the exact value is 14.2857...%, which rounds to 14.29%, as the LP says.
- Page 16, Example 3: the two derivations sit in two columns split by a vertical rule. This is equations, not a figure, so there is no inventory entry for it.
- Pictures seen but not inventoried (decoration, no mathematical content): badminton player (p.14), the two children with speech bubbles (p.15), the "30% SALE" clothing-store drawing (p.18, discount section, chunk E), the "Try This" icon (p.19).
