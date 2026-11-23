# Chunk B notes: Class 7 Ch 1 "Large Numbers Around Us" (topics T16 to T21, T23 to T26)

Result: 31 items (13 question, 13 solution, 5 worked example): required 0, optional 3, none 28. Validator: errors 0, warnings 0.
No diagram image is added in this chunk. Everything in these pages is text, a plain table, an equation working or a comic strip.

## 1. Judgement calls

1. **Population table (T24 worked example, T25 Q1 and Q2): LaTeX table, not an image. Needs your decision.**
   The 20-city table (book p.12-13, base figure P12-table-1) is a plain table of numbers, so the rule `LATEX_TABLE` applies (the prompt's own example: a plain table goes to a LaTeX array). It is also 20 rows by 4 columns, too tall for a 16:9 card at a readable size.
   The catch: the LP question text of T25 Q1 (C89) and Q2 (C91) does NOT contain the table, so as the plan stands the learner cannot attempt them. I set `needs_lp_text_sync: true` on both question items and wrote the instruction in `text_alternative` (a LaTeX array, columns Rank | City | Population (2011) | Population (2001), 20 rows as in P12-table-1). If you would rather have one picture of the table per question card, those two items would become `required` (diagram type `cell_grid`, two blocks of ten ranks side by side).
   The worked example C85 ("What the table shows") is `none` without a text sync: its concept already keeps the teaching image C85.IMG1 (four cities, Kolkata outlined), and the steps only mention Mumbai, New Delhi, Chennai and Kolkata, all in that image.
2. **Printed answer tables are LaTeX, not pictures.** T19 Q1 solution (P29-table-1 and P30-table-1: numerals and number names in both systems) and T21 Q1 solution (P31-table-1 and P31-table-2: five nearest neighbours of each number) are plain black-grid tables with no colour meaning. Rule B2 "printed answer is a picture" is aimed at line-ups, shaded grids, constructions; a plain text table falls under `LATEX_TABLE`. Both are `none` with a `text_alternative` for the LaTeX array. The LP `steps_tex` already carries every cell.
3. **Three solutions are `optional` (not added):** T21 Q2 (C77, the interval 4,99,99,500 to 5,00,00,499 around 5,00,00,000), T23 Q1 (C82, sum 8,82,810 between 8,00,000 and 9,00,000) and T23 Q2 (C84, difference 9,73,108 between 9,00,000 and 10,00,000). A number line would help but the LP steps give every distance in LaTeX. The question sides have no given figure, so they are `none`.
4. **T25 Q2 solution (nearly doubled) is `none`.** A 2001-against-2011 bar graph would be nicer, but the book draws none and the doubling check is complete in the steps. I did not mark it optional because the graph would be new data work, not a figure the book or the LP points to.
5. **T17 C58 (two comma patterns) is `none`.** A strip showing 12345678 grouped 3-2-2-2 against 3-3-3 would be nice, but the steps already name every group. The book's numeral table (P08-table-1) is a plain table, `LATEX_TABLE`.
6. **Comic strips (P09, P10) are `none:DECORATIVE_ONLY`.** They open section 1.4 and ask "What do you think of this conversation?" (a discussion). No LP item uses them; the numbers in the speech bubbles (1 lakh, 99,999) are also in the chapter text.
7. **P11-table-1 (nearest neighbours of 6,72,85,183) is `none:LATEX_TABLE`, not the concept image C71.** C71.IMG1 is a number line for the nearest-thousand row only; the table has five rows. It is a worked model, not data of T21 Q1.
8. **T26 C93 (A Multiplication Shortcut) is `none:LATEX_ARITHMETIC`.** The two book workings (P13- and P14-cancellation_working-1) are fraction chains with struck-through numbers; \cancel in LaTeX can reproduce them if wanted.
9. **P07-calculator-1 and P07-table-1 (Systematic Sippy, book p.7) are not claimed by this chunk.** They sit on the page of T16 but belong to T14 and T15 (chunk A: "Systematic Sippy and the Crore", C48 and C50). The merge check (every base figure claimed) will show whether chunk A claimed them. My T16 items do not need them (Q1 gives its five numbers in the text; the printed answers are text lines).

## 2. Things in the LP that look wrong or thin

- **T16 Q1 (C52) lacks the Sippy button list.** The question says "For the numbers in the previous exercise" and gives the five numbers, but nowhere states that Systematic Sippy has only +1, +10, +100, +1,000, +10,000 and +1,00,000. The answer needs the +1,00,000 button (367813 = 3 x 1,00,000 + ...). Suggest one sentence in the question text; I put it in `text_alternative` but did not set `needs_lp_text_sync` (the context may be given by the T14/T15 teaching concepts before it).
- **T25 Q1 and Q2 question texts do not carry the table** (see 1.1). Also, Q1 merges the book's Q3 (Pune) and Q4 (biggest increase); Q2 merges the book's Q5 (almost doubled) and Q6 (Patna to Mumbai). Fine, but the book numbering in `book_number` is the LP's own.
- **Book answer page (p.28) labels the last item of Figure it Out 1.2 Q1 as "(f) 367813"**; the question has (a) to (e). The LP correctly uses (e).
- **Book's printed answers (p.29) write "Four Millions Fifty Thousand ..." and "Twenty millions twenty two thousand and two".** The LP uses the correct singular "million" and the Indian/American words as in steps_tex (LP wins).
- **No printed answers in the book for T23 (estimating sums and differences), T21 Q2 (five equal neighbours) and T20's worked example "round up or down" beyond p.30.** The LP text is its own; I recomputed it: 4,63,128 + 4,19,682 = 8,82,810; distances 17,190 (Estu) and 82,810 (Roxie); 14,63,128 - 4,90,020 = 9,73,108; distances 26,892 (Roxie) and 73,108 (Estu); 8,83,128 = 4,63,128 + 4,20,000; count 5,00,00,499 - 4,99,99,500 + 1 = 1000. All correct.
- **T25 answers recomputed and correct:** Pune 31,15,431 - 25,38,473 = 5,76,958; Bengaluru 84,25,970 - 43,01,326 = 41,24,644; Hyderabad 31,72,487; Ahmedabad 20,50,500; Surat 20,33,962; Mumbai / Patna = 1,24,42,373 / 16,84,222 = 7.39 (rounded).
- **T21 Q1 answer rows recomputed and correct** for both numbers (thousand, ten thousand, lakh, ten lakh, crore), and match the book's p.31 tables.
- **T26 worked example:** the LP steps multiply by 10 (or 100) first and then halve (or divide by 4); the book works the other way round (halve first: 116/2 = 58, then x 10). Both are correct and give 580 and 20,600; just not the same order as the book figure.

## 3. Where the book itself is unclear

- The brief and `meta.json` say the pdf has no printed-solutions section, but pdf pages 24-38 are one ("Page No. N" headings). I used it for the printed-answer pictures (pages 28 to 32).
- The book's Sippy table (p.7) has a +10,00,000 row although Systematic Sippy's own buttons stop at +1,00,000 (the base inventory notes it too). Not used by any chunk-B item.
- P12-table-1 is split by the page break (ranks 1-14 on p.12, 15-20 on p.13, header not repeated). Read as one table.
- The comic on p.10 never states the joke (139 rounded off to 100, the police number); the LP does not use the strips.
