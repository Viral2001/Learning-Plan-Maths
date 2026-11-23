# Chunk C notes (Class 8 Ch 3, topics M3.S22.T22 to M3.S28.T28)

Result: 21 items = 5 required (C75 worked, C80 solution, C84 worked, C87 solution, C89 solution), 2 optional (C81, C82 worked), 14 none. Validator: errors 0, 1 warning (C84 has no printed book figure, as expected: the book has no 5072 numeral). 30 base figures claimed (12 to items, 8 to concept images, 10 none).

Reminder on the brief: it says the pdf has no printed-solutions section. It does: pdf pages 35-46 are the printed answers. They were used for C80 (p.42), C87 (pp.43-44), C89 (p.44) and C95 (pp.44-45).

## 1. Judgement calls

- **No question side needs a diagram.** No book question of this chunk gives a figure (the Mayan and Chinese symbol tables are teaching figures on pdf pages 28 and 30). The `q_figure` hints on C86 and C88 describe symbol tables that are not part of the question, so the question items are `none` (C79, C86, C88, C94, C96, C98).
- **C80 (Mesopotamian Q1 solution), required.** Printed answer is a picture, so B2 applies. One picture for all five numerals, in 3600s / 60s / 1s columns, with the row labels (i) to (v) because the LP steps use them. The LP answer is the compact form (1 | 3, 2 | 12, 3 | 20, 1 | blank, 1 | blank | 5); the book prints the older form with a landmark diamond between the groups. The LP wins (brief rule), so the picture follows the LP. The two blank places that the LP names (1s place in (iv), 60s place in (v)) are marked with a dashed FOCUS box; the leading empty 3600s cells in rows (i) to (iv) are left plain.
- **C75 (worked, 4000 in own symbols), required.** The question asks for the written form with our own symbols; that is a drawing of wedges, chevrons and landmark diamonds (the book draws the same kind of numeral for 640 and 7530 on p.25). The two book numerals P25-numeral-1 and -2 are mapped to this item with a description saying the LP uses 4000 instead of 640 and 7530. This is a stretch of "it becomes that item's diagram"; the alternative is `none` for those two figures. Please keep or change at merge.
- **C84 (worked, 5072 in rod numerals), required.** The answer is the rod drawing ("5 heng, a blank, 7 heng, 2 zong"). Rod shapes follow the table on pdf page 30. Blank hundreds place shown with a dashed FOCUS box.
- **C87 (Mayan Q solution), required.** Four numerals in one picture, with place rows 360 / 20 / 1. No letters (i) to (iv) because the LP steps are numbered 1 to 4 and do not use letters (user decision 3). Number labels 77, 100, 361, 721 are drawn.
- **C89 (Chinese Q1 solution), required.** The printed answer is a picture (41 with an arrow to four vertical rods, a gap, one rod). The LP only says "5 rods in a row". I draw the book's picture with the slightly wider gap before the fifth rod (about 1.75 times the rod spacing, measured on the page picture), no tens/units labels.
- **C95 (Q2 solution), none, LATEX_TABLE.** The printed answer is a plain bordered table of text (Number / Base-2 / Gumulgal, rows 1 to 8), so it stays a LaTeX table (v3 rule), not a picture.
- **C77, none.** "Using our numerals for each place" gives plain digits 1 | 2 | 5 and the answer is text. This differs from C75 on purpose: C75 asks for the written form in the lesson's own wedge/chevron symbols (a drawing), C77 asks for digits.
- **Figure mapping.** Teaching figures with a matching teaching idea in `concept_images.json` were mapped to that concept image (P25-table-1 to C77, P26-table-1 to C81, P28-numeral-1 and P28-place_value_table-1 to C82, P30-numeral-1 and P30-place_value_table-1 to C84, P31 to C90, the summary board P32 to C100). These are accounting links only; nothing is linked. Inline glyphs, the symbol rows and the symbol tables with no matching teaching image are `none:TEXT_SUFFICIENT`. The world map P33-map-1 is `none:NOT_RENDERABLE` (no question works on it). I claimed P32-summary_board-1 and P33-map-1 because C91 cites "3.4.evolution_ideas" and "3.4.map", and no other chunk covers topic T29.

## Borderline

- **C81 (two wedges, gap, five wedges) and C82 (Mayan numeral: two dots, three dots, one bar), both `optional`.** Both questions describe the numeral completely in words and the answer is a number (125 or 7205; 785), so the tie-breaker says text is enough. A picture of the numeral would clearly help and the book shows the same idea (ambiguity table p.26; Mayan numeral p.28), so I did not choose a plain `none`. Neither is added to the plan. If you want them drawn they are easy upgrades: C81 = two wedges, a wide gap, five wedges (3 over 2); C82 = three rows stacked: 2 dots (360s), 3 dots (20s), 1 bar (1s).
- **C75 required vs C77 / C76 none**, see above (answer is a drawing in C75 only).
- **C89**: only five vertical lines, but the printed answer is a picture and the rule says solution required; kept required under user decision 4.
- **C84**: required although the LP text carries "5 heng, a blank, 7 heng, 2 zong"; kept required under user decision 4.
- **C90** (4072 as digits in places): a filled place value row is `none` (LaTeX) by the HEADER_BOXES_ONLY / LATEX_TABLE rule, even though a teaching image shows it.

## LP text issues

- **M3.S23.T23.C80**, `answer_tex`: the semicolon between (iv) and (v) is missing: "(iv): $1$ | blank (v): $1$ | blank | $5$". Suggested: "(iv): $1$ | blank; (v): $1$ | blank | $5$".
- **M3.S23.T23.C80**, step (iv): "written 1 followed by a blank" cannot be seen in a numeral (a trailing blank is invisible; it looks like the numeral for 1, which is the ambiguity of the next section). Suggested: "(iv): 60 = (1) x 60, so the 1s place is empty: written 1, with the empty 1s place after it (marked in the picture)."
- **M3.S23.T23.C80**: the LP gives the compact form (1 | 3 ...) while the book's printed answer draws the older form with a landmark diamond. Not an error, but the two differ; the diagram follows the LP.
- **M3.S28.T28.C96**, `question_tex`: "hadn'$t$ been invented" has a stray math wrapper around the t. Suggested: "hadn't been invented".
- **M3.S27.T27.C94 / C95 and M3.S28.T28.C98**: "base$-2$", "base$-10$" are set in math mode (the minus becomes a math minus sign). Suggested plain text "base-2", "base-10" like the book.
- **M3.S27.T27.C95**: the LP answer does not carry the comparison table of the book answer (Number, Base-2 system with ur = 0 and uk = 1, Gumulgal system, rows 1 to 8). Suggested: add that table as a LaTeX array. The step "the Gumulgal ... stopped at 6" is true of the chapter text, but the book answer extends the Gumulgal column to 7 (uk-uk-uk-ur) and 8 (uk-uk-uk-uk) by the same counting-by-2 rule; a short clause such as "(the book answer continues the Gumulgal names to 8 by adding words)" would remove the apparent conflict (optional).
- **M3.S25.T25.C89**, step 3: "$2$ then $3 (23)$", "$3$ then $2 (32)$": the bracketed number is inside the same math group. Suggested: "$2$ then $3$ ($23$)", "$3$ then $2$ ($32$)".
- **M3.S28.T28.C99**, step 3: "$25 = (1) \times 25 + (0) \times 5 + 0$". Suggested: "$25 = (1) \times 5^2 + (0) \times 5 + (0) \times 1$" (the book writes it this way).
- **M3.S22.T22.C75**: ncert_refs cite meso_640 and meso_7530 but the example is 4000; the step "written as 1 with the 3600 symbol, 6 with the 60 symbol, and 40" has no numeral shown anywhere except in the new diagram. Fine once the diagram is added; no text change needed.
- **M3.S26.T26.C92**: `ncert_refs` is empty (an LP-made example, no book source). Not an error.
- **Book numbers**: the LP numbering differs from the book for the last Figure it Out set: C88 "Place Value, Q1" is book Q1; C94 "Place Value, Q2" is book Q2; C96 "Figure it Out, Q1" is book Q3; C98 "Figure it Out, Q2" is book Q4. The one book set is split over three topics with restarted numbering.

## Book unclear or book slips (base inventory records what the book prints)

- **p.24, numeral for 59:** six chevron heads are printed with nine wedges (that would read 69); 50 has 5 heads and 40 has 4. A print slip. No item diagram uses the 59 numeral.
- **p.28, Mayan reading panel:** the expansion prints "(3) x 10" for the shell band, but the shell means (0) x 1; the total 4 x 360 + 11 x 20 = 1660 is right. Not used in any item diagram.
- **p.29:** the inline symbol printed after the word "dot" is the shell, not a dot. Print slip, no diagram affected.
- **p.42 printed answer (Mesopotamian Q1):** correct values, but printed in the older diamond form (see C80). (iv) 60 is printed as a wedge and the 60 diamond, so 60 and 1 are told apart by the diamond only.
- **p.44 printed answer (41 with zong rods):** the book picture shows the four-plus-one grouping with a visible gap; the book's own text then says the numeral could be read as 23, 32 or 122 if there is no significant space. The LP adds "as 5" and "122"; fine.
- **pp.44-45 table:** continues over two pages with the header repeated; the base inventory already records this as one figure.
