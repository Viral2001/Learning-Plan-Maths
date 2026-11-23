# Class 7 Ch 1 Large Numbers Around Us - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths7_ch1` v30 (taken from staging). Result: new V2 version v31 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (119 items from 64 units)
{"question": {"required": 4, "none": 51}, "solution": {"required": 2, "none": 46, "optional": 7}, "worked_example": {"none": 7, "required": 2}}

Optional, NOT added: [('C20', 'solution'), ('C77', 'solution'), ('C82', 'solution'), ('C84', 'solution'), ('C97', 'solution'), ('C138', 'solution'), ('C164', 'solution')]

needs_lp_text_sync: []

## The 8 diagrams
| id | side | type |
|---|---|---|
| M1.S3.T3.C6.IMG1 | question | arrow_map |
| M1.S3.T3.C7.IMG1 | solution | arrow_map |
| M1.S6.T6.C19.IMG1 | question | other |
| M6.S35.T35.C147.IMG1 | question | cell_grid |
| M6.S35.T35.C148.IMG1 | solution | cell_grid |
| M6.S36.T36.C159.IMG2 | worked example | other |
| M6.S36.T36.C160.IMG2 | worked example | other |
| M6.S37.T37.C163.IMG1 | question | other |

### Chunk A notes (from the decision agent)
# Chunk A notes (Class 7 Ch 1, plan cbse_eng_maths7_ch1_v30)

Result: 32 items. Required 3 (C6 question, C7 solution, C19 question), optional 1 (C20 solution, not added), none 28. Validator: errors 0, warnings 0.

## 1. Judgement calls

1. **Plain press-count tables are LaTeX, not images (C41/C42 Creative Chitti, C50/C51 Systematic Sippy).**
   The book tables (P06-table-1, P07-table-1) and the printed answer table (P26-table-1, printed answers page 3) are plain black or red grids of whole numbers: rows are the seven buttons, columns are the ways, blank means 0 presses. No colour carries meaning (the pink pills in the book are styling). Run rule: "plain tables of numbers stay text/LaTeX" (`LATEX_TABLE`). I did consider the B2 line "printed answer is a picture, solution required". I read it as meant for stick-figure line-ups and coloured tables, not a plain numeric table that a LaTeX array reproduces exactly. Each `none` item carries a `text_alternative` with the array to write. **If the user wants these as pictures, flip C42 (solution) and C51 (solution) first; C41/C50 questions already state the counts in the text.**
   The printed answer table has three columns (5/_/7/2, 4/10/7/2, 1/40/6/12), not the two ways printed in the question; the LP answer uses column 3 (4, 10, 7, 2).

2. **C6/C7 ladder (Climbing to One Lakh) is required on both sides.** The book question is "fill in the boxes given below" on a ladder with +1 arrows (`ACTION_ON_FIGURE`); the filled ladder is the answer (`ANSWER_IS_FIGURE`). The text alone would also work (tie-breaker), so this is the most borderline of the three required items; it follows the "complete a given figure" trigger.
   **The question diagram leaves the last box empty.** The book prints 1,00,000 in the last box already, but the LP question asks the learner to give "the smallest 6-digit number" (and the LP solution derives 1,00,000 as its last step). To avoid showing an answer the LP asks for, the question figure has only 999 filled. If the LP text is later changed to give 1,00,000, the last box should be filled in INK (render_note says so).
   The book caption "1,00,000 is read as One Lakh" is not drawn (captions are not allowed).

3. **C19 Somu: question required, solution optional.** The LP text says "The picture shows 10 floors" and the book data (10 floors, the 0 to 500 m scale with the statue and the waterfall) is only in the pictures, so the question side is required (`FIG_REFERENCED`, `DATA_IN_FIGURE`). The answers are numbers with the arithmetic in the steps (typical pair "figure-based question, numeric answer: Q required, S none/optional"), so the solution is `optional` (not added). The figure that would help is written in the reason: the scale with Somu's building as a 40 m bar and the gaps 140 m and 410 m marked in ANSWER green. **Alternative if the user prefers fewer images: C19 question `none` and remove "The picture shows 10 floors." from the LP question text.**
   Drawing decisions for the C19 figure: two panels. The left panel is a zoom of the building as 10 equal cells (so the floor count can be counted) with one floor bracketed "4 m" (given in the question). The right panel is the 0 to 500 m scale with a bar for the Statue of Unity (180 m) and one for the Kunchikal waterfall (450 m), both numbers from the LP. The building's own height (40 m) is the answer, so it is not labelled or drawn as a bar in the question figure. Somu himself is not drawn: at the zoomed scale he would be 17 px tall, and his height (1 m) is in the text. The book's cartoon statue and waterfall are not reproduced (plain bars with names).

4. **C8/C9 (days in 100 years) and all Figure it Out 1.1/1.2 questions: none.** Numbers are in the text, arithmetic is in the steps. For C9 a number line comparing 36,500 / 73,000 / 1,09,500 with 1,00,000 would be nice but is not needed (marked `none`, not `optional`, because the steps state every gap).

5. **Land of Tens Q1-Q3 (C32, C34, C36), Chitti Q2 (C43), Sippy mascots.** The calculator pictures are mascots with one labelled button; the labels are already in the text (`DECORATIVE_ONLY`). Question side `none`, all three alike (sibling consistency).

6. **Figures claimed beyond the units' own items.** `P06-calculator-1` (Creative Chitti mascot, intro of Land of Tens Q4) and `P07-calculator-1` (Sippy mascot) sit in the 1.2 text between my units (topics T11 and T14); no other chunk has a unit there, so I claimed them as `none:DECORATIVE_ONLY` (another chunk that claims them should give the same meaning). `P02-pattern-2` (zigzag chain) is claimed as `none:LATEX_ARITHMETIC`.
   Two extra inventory entries use the NEW- scheme because one book figure serves two uses: `NEW-P02-pattern-1-sol` (the filled ladder, solution use of P02-pattern-1) and `NEW-P03-building-1-teaching` (accounting for the teaching image `M1.S5.T5.C16.IMG1`).

7. **Base descriptions checked against the page pictures.** I checked every base entry of my chunk against pages 2, 3, 5, 6, 7 and 26. All are correct as written (10 boxes and 9 arrows in the zigzag; 10 balcony floors with Somu on the top balcony; lines at the 200 and 500 labels with a pink strip near 60; calculators with the listed buttons; table cell values). No entry needed "CORRECTED:".

8. **Optional count.** Only C20 is optional. The answer-side `none` items whose figure "would be nice" are not marked optional, per "prefer none".

## 2. Things in the LP that look wrong or odd

- **C6 question text vs the book:** the book prints 1,00,000 as given in the last box; the LP asks the learner to give it (see above). Pick one: either drop "and the smallest 6-digit number" from the LP text, or keep it as is (current choice).
- **The zigzag chain of the book page 2** (boxes 99,995, 99,996, blank, 99,998, then six more blanks; the sequence runs 99,995 ... 1,00,004) belongs to the same "fill in the boxes" instruction but is **not in the LP at all** (no question or solution mentions 99,997 / 99,999 / 1,00,001 ... 1,00,004). The content team may want a question for it; if added, it is a plain sequence (LaTeX).
- **C19/C20 question text** says "The picture shows 10 floors" and "Statue of Unity (180 m)", "waterfall (450 m)". The book picture draws the statue's reference line at the 200 label and the waterfall at 500, and its pink strip for Somu's building near 60 m (not 40 m). The LP numbers (180, 450, 40) are consistent with the book text and printed answers (40 m, 140 m, 410 m, about 113 floors), so I used them.
- **LP hint `q_figure` for C19** says Somu stands "at its door"; the book picture has him on the top balcony. Hints were not used for the drawing.
- **C20 step 5** ("The statue is 180 / 40 = 4.5 times the building") is not in the printed answers (the book text says "close to 4 times"). Not wrong, only an addition.
- **Book printed answer for Figure it Out 1.2 Q1 (e) is wrong:** its second way "(36 x 10000) + (78 x 1000) + (13 x 1)" equals 4,38,013, not 3,67,813. The LP's second way for (e), (36 x 10000) + (7 x 1000) + (8 x 100) + (1 x 10) + (3 x 1) = 3,67,813, is correct and is the one to keep.
- **C37 step 9** begins "(i):" without math mode (the other steps use `$(a)$:`). Cosmetic. The LP text for C36's question also writes `(i)` outside math mode.
- **C44 step 4** reads "digit sum must be 30 - 9 = 21 or 30 - 18 = 12 or 3"; the last item should read "30 - 27 = 3". The results (largest 993, smallest 102) are right and match the printed answers; I re-derived both (digit sums 21 and 3, each trade adds 9 presses).
- **Systematic Sippy table (book p.7)** has a +10,00,000 row although Sippy's calculator has only six buttons up to +1,00,000 (and the text lists no +10,00,000). The LP question already ignores that row.

## 3. Places where the book itself is unclear

- The scale picture on p.3 (lines at 200 and 500 vs text 180 and 450; pink strip near 60 m for a 40 m building; statue "close to 4 times the height of Somu's building" while 180 / 40 = 4.5).
- Whether the plain base of the building (the door strip under the tenth balcony) counts as an eleventh floor. The text and answers (10 floors, 40 m) say ten.
- The printed answer table for the "different way to get 5072" shows three ways while the question's own table showed two; the printed headers of the extra columns are blank.
- The book's answer to the zigzag chain is not printed at all.

### Chunk B notes (from the decision agent)
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

### Chunk C notes (from the decision agent)
# Notes for chunk C (Class 7 Ch 1, cbse_eng_maths7_ch1_v30)

Units: M5.S27.T27, M5.S28.T28, M5.S30.T30, M5.S32.T32, M6.S34.T34 (12 pair units, 24 items).
Result: required 0 / optional 1 / none 23. Validator: errors 0, warnings 0.

## 1. Judgement calls

- No diagram is required anywhere in this chunk. Every question is arithmetic, a digit-count table or word reasoning; no question
  gives a figure that carries data, and no solution (LP steps or printed answer) is a picture, an arrangement or a construction.
  I checked the page pictures 13 to 19 and the printed-answer pages 32 to 34.
- M5.S27.T27.C97 (solution, "why times 5 = times 10 then halve"): `optional`, not added. A picture of 8 groups of 10 dots split
  into 8 groups of 5 would make the "why" visible. The five text steps are complete and the book's own answer is one line
  ("10 / 2 is the same as 5"), so the tie-breaker says text is enough. If the content team wants one picture in this chunk, this is
  the candidate. Its question side is `none`: the Math Talk gives no figure (the strike-through workings on pp.13-14 belong to the
  worked example, chunk B).
- M5.S30.T30 Q1 (four boxes of products, C106/C107): `none` / `none`, LATEX_ARITHMETIC. The four bordered boxes (P14-pattern-1 to -4)
  are three plain multiplications each with the result blank; the borders carry no meaning. The filled boxes are equations and
  sequences. Text alternative written in the items (four aligned LaTeX blocks).
- M5.S30.T30 Q3 (digit-count table, C110/C111): `none` / `none`, LATEX_TABLE. This is the one place where a v3 trigger could be
  read the other way: the printed answer (P34-table-1) is "a filled table" (ANSWER_IS_FIGURE lists "filled table"), and the question
  figure (P15-table-1) holds the four given rows. I followed Step C and the run rule that plain tables of numbers stay LaTeX: the
  table is words and numbers only, no colour, no position or arrow meaning, 7 rows by 4 cells. I set `needs_lp_text_sync: true` on the
  question (see 2). If the user prefers a drawn boxed table, both sides would become `required` (question = 7-row table with three
  blank result pairs, solution derived from it with 9/10, 10/11, 24/25 in ANSWER green).
- Fascinating Facts (C115 to C118) and Did You Ever Wonder (C123 to C130): the banners and the ships picture are page art
  (DECORATIVE_ONLY); all numbers are in the question text. Solutions are LATEX_ARITHMETIC. The Moon and Sun items could have a
  distance bar or number line, but the text steps give exactly the same information, so `none`.
- Sibling consistency: Figure it Out 1.5 Q1 and Q2 (C98/C99, C100/C101) both `none` / `none`; the two Fascinating Facts pairs
  and the four Did You Ever Wonder pairs are all `none` / `none`.
- Figures not claimed here: P13-cancellation_working-1 (Roxie, 116 x 5) and P14-cancellation_working-1 (Estu, 824 x 25) sit in the
  book section "A Multiplication Shortcut" but belong to the worked example M5.S26.T26.C93 (unit 35, chunk B). Chunk B must claim
  them; the merge will show an unclaimed base figure if it does not.
- Five figures missing from the base inventory are listed with NEW- ids and `none:DECORATIVE_ONLY`: NEW-P17-amazon-banner,
  NEW-P17-train-map, NEW-P18-whale-banner, NEW-P18-plastic-banner (each carries one of the Fascinating Facts expressions),
  NEW-P19-ships-picture (Mumbai crowd and Titanic-style ships). The base listed only the first two fact banners (P16).
- Base descriptions checked against the pictures: P14-pattern-1 to -4, P15-table-1 (28 boxes, 6 empty) and P34-table-1 (3 rows, 12
  boxes, answers 9/10, 10/11, 24/25), P16-fact_card-1 and -2 are all correct; no "CORRECTED:" needed.

## 2. Things in the LP that look wrong or thin

- M5.S30.T30.C110 (question, digit-count table): the LP text says "Fill in the table: 5-digit times 5-digit, 8-digit times 3-digit and
  12-digit times 13-digit" but does not give the four rows the book prints as given (1-digit x 1-digit = 1-digit or 2-digit, 2-digit
  x 1-digit = 2-digit or 3-digit, 2-digit x 2-digit = 3-digit or 4-digit, 3-digit x 3-digit = 5-digit or 6-digit). Only the
  `q_figure` hint carries them. Since there is no picture, the LP question should contain the table as a LaTeX array (text
  alternative in the item).
- The LP's M5.S30.T30.C108 solution proves the 2-digit bound with 99 x 99 = 9801, while the book's Roxie argues with 100 x 100 =
  10,000. Both are correct; the LP differs from the book on purpose. Not a fault.
- Printed answers: the book has no printed answer for the Mumbai buses and ships question, nor for the Moon question (C123/C124,
  C125/C126). The LP solutions are LP-authored; I recomputed them: 1,00,000 x 50 = 50,00,000; 5000 x 2500 = 1,25,00,000;
  1,25,00,000 - 1,24,42,373 = 57,627; 100 x 365 = 36,500; x 10 = 3,65,000; 3,84,400 - 3,65,000 = 19,400. All correct (leap years
  ignored, as the book does).
- All other LP numbers were recomputed and agree with the book: FiO 1.5 Q1 (1,76,800; 9000; 10,00,000), Q2 (300; 6000; 30,000;
  30,000; 1200 x 1,00,000 = 12,00,00,000), product patterns (121; 12,321; 12,34,321; 12,34,54,321; 4026; 4,40,226; 4,44,02,226;
  4,44,40,22,226; 15; 1155; 1,11,555; 1,11,15,555; 10,201 to 10,816), Fascinating Facts (4,75,000; 14,70,00,000; 40,00,00,000;
  9,300; 1,50,000; 40,00,00,000), Sun (1,47,000 days, about 402.7 years; the book says about 403), sheets 500 kg, babies 3,60,000,
  coins 86,400.
- C115/C116 step 4 supposes "50 years" for Purandaradasa (an LP assumption; the book gives no number). C116 steps 4 and 5 answer
  the speech-bubble and Earth-Sun side remarks of the book, not the question as worded; fine as extra.
- The brief says the pdf has no printed-solutions section. It does: pdf pages 24 to 38 are printed answers ("Page No. n"), and the
  base inventory already uses them (P26 to P37). `meta.json` has `solutions_pages: null`, which looks wrong for this pdf.

## 3. Places where the book itself is unclear

- Book digit-count table row 4 reads "3-digit x 3-digit = 5-digit or 6-digit" as printed; this is mathematically right (100 x 100 =
  10,000; 999 x 999 = 9,98,001) and matches the printed answer rule (m + n - 1 or m + n digits).
- Roxie's reasoning (p.15) says the product of 2-digit numbers is "less than 10,000" using 100 x 100; it is a loose bound (the
  largest is 99 x 99 = 9801). Not a figure matter.
- The printed answers for Figure it Out 1.5 Q2(a) to (d) stop at "= 100 x 3" and so on without the final value; the LP gives the
  final values. The printed answer for Q1 stops at "= 100 x 1768", "= 9 x 1000", "= 1000 x 1000" likewise.

### Chunk D notes (from the decision agent)
# Chunk D notes (Class 7 Ch 1, plan cbse_eng_maths7_ch1_v30)

Units: Figure it Out 1.6 Q1-Q14 (M6.S35.T35, units 48-61), Toothpick Digits worked examples C159 and C160 (M6.S36.T36, units 62-63), 24-sticks question pair (M6.S37.T37, unit 64). 32 items: required 5 / optional 2 / none 25. Validator: errors 0, warnings 0.

Required diagrams:

| Item | Media id | What it draws |
|---|---|---|
| Q9 question (C147) | M6.S35.T35.C147.IMG1 | 7 empty boxes over 5 empty boxes, right-aligned |
| Q9 solution (C148) | M6.S35.T35.C148.IMG1 | the same boxes twice, filled for the largest sum and for the smallest difference |
| C159 worked example | M6.S36.T36.C159.IMG2 | the book's p.23 digit strip 0-9 in sticks |
| C160 worked example | M6.S36.T36.C160.IMG2 | same strip, identical spec |
| C163 question (24 sticks) | M6.S37.T37.C163.IMG1 | same strip, identical spec |

## 1. Judgement calls

1. **Q9 solution holds both answers in one figure.** The item carries one media id, so the two finished arrangements (largest sum, smallest difference) are stacked in one picture, each under a short tag ("Largest sum", "Smallest difference", words the LP steps use). If the team wants one picture per part, the item would need two media ids (the validator allows one). Q9 question: required although the LP text describes the layout in words, because the book says "each box below" and the learner fills the boxes (FIG_REFERENCED, ACTION_ON_FIGURE); the printed answer is a picture, so the solution is required (sibling consistency).
2. **The stick-digit strip on three items (C159, C160, C163).** The only text fact the book gives is "the digit 7 needs three sticks"; the shape and stick count of every other digit exist only in the strip, so counting sticks, moving four sticks and "exactly 24 sticks" cannot be attempted without it (DATA_IN_FIGURE). The existing teaching images of C159 and C160 show only 42,019 and 63,890, not the strip, and are never linked. Per the brief, one diagram per item with an identical spec. C160 is the weakest of the three (the previous card already showed the strip); drop it if only one strip is wanted.
3. **The strip has no stick counts and no number built of sticks.** It shows only the ten digits with a numeral under each, so the counting in the example stays the learner's job. Drawn as two rows of five (0-4 over 5-9) instead of the book's single strip so that the 16:9 card is used and the sticks are large; reading order is kept.
4. **The digit 7 has three sticks.** The page picture draws the 7 with four bars (an extra upper-left bar); the book text says three, and the LP solutions only work with three (42,019 to 42,078 adds two sticks; 1 to 7 adds one). The diagram follows the text and says so in `render_note` (also flagged by the inventory agent).
5. **Optional, not added:** (a) Q4 solution (a picture of the 20 digits with the struck ones crossed would help, but the steps name the struck digits and the printed answer is the number only); (b) 24-sticks solution (2008 and twelve 1s drawn in sticks and counted to 24; the answer is numeric, the steps carry the counts, the book has no printed answer picture). I judged the stick drawings "nicer", not needed, once the question carries the strip. If the team reads "make a number with sticks" as a drawing answer, (b) becomes required with `derived_from` the strip.
6. **None by rule:** Q1-Q3, Q5-Q8, Q10-Q14 (text and LaTeX). Q7: the book draws no calculator on p.20. Q10: the seven cards are plain numbers in the text (NUMBER_LIST_IN_BOXES). Q12-Q14: the birds on p.21 are decoration and every datum is in the text. Q11: the Statue of Unity is not drawn. Q6: the LP answer card had two images in the old plan; a pure digit-count argument, no figure.
7. **Page 19 Titanic picture** (section 1.5, before "Figure it Out") is an illustration and belongs to another chunk; not claimed.

## 2. Things in the LP that look wrong or thin

- **Q9(a): the LP and the book disagree, and the LP is right.** The book's printed picture (top 9 9 8 8 7 7 6, bottom 6 5 5 4 4) gives 99,88,776 + 65,544 = 1,00,54,320. That is a valid use of the cards but not the largest sum. The LP's 99,87,654 + 87,654 = 1,00,75,308 is larger and is the maximum (greedy by place value: places 10^6 and 10^5 take one digit each, the rest two each). The solution diagram follows the LP. Q9(b) (11,22,334 and 99,887, difference 10,22,447) is the same as the book and correct.
- **Q2:** the LP says 61 letters for 77,77,777; the book's printed answer says 60. I recounted: seventy(7) seven(5) lakhs(5) seventy(7) seven(5) thousand(8) seven(5) hundred(7) seventy(7) seven(5) = 61. A brute-force check of all 7-digit numbers also gives maximum 61, reached by 81 numbers, smallest 73,73,373, as the LP step says. The LP is right.
- **Q3:** the book's example (987654312) does not meet the condition for every swap and it does not count; the LP (only 12,34,56,789) is right. **LP text inconsistency:** the plain `steps` and `answer` fields write "1,23,45,67,89" (wrong Indian grouping), while `steps_tex`, `answer_tex` and `text` write "12,34,56,789" (correct). The plain fields should be fixed.
- **Q6(c):** the LP says 13,495; the book prints 13995. Counting fives by computer gives the 5000th five in 13,495, so the LP is right. Q6(a) 3 in 370 and Q6(b) 1,85,185 are right.
- **Q10:** the LP gives exact results for (a)-(d) (checked: 13000 x 20 - 150000 = 1,10,000; 70000 x 5 - 150000 = 2,00,000; 150000 + ((4000 + 300) x 20) x 5 = 5,80,000; (13000 + 70000) x (20 - 5) = 12,45,000, each card used once) and 20,91,000 for (e), 200 away. The book only shows closer attempts ((a) 1,13,000, (d) 12,44,500). The LP question text leaves out the book's worked sample for (a) (4000 x (20 + 5) + 13000 = 1,13,000), which is fine because the LP's own (a) is exact.
- **Q12:** the LP question says "cross an ocean" (as in the book's answer page); the book's question page says "the Pacific Ocean". Trivial.
- **Q14:** the question depends on Somu's building being 40 m (from an earlier topic); the question text does not state it, only solution step 1 does. The book's printed answer writes "10,000 - 12,000 m" for aeroplanes in one place while the question says 12,800; the LP uses 12,800 (correct, 12,800 / 40 = 320).
- **C159 and C160 numbers checked by a stick-segment script:** 42,019 plus exactly two sticks gives exactly 42,049, 42,078, 42,818, 42,879, 48,019, 92,019 (the LP's list; the LP's extra 1,42,019 adds a new digit 1). All five numbers the LP gives for moving four sticks of 63,890 are real four-stick moves, and 99,985 is the biggest five-digit number reachable by moving four sticks. Placing a 1 in 4,2,0,1,9: the five numbers and the biggest 4,21,019 are right.
- **C164:** biggest 24-stick number = twelve 1s, 1,11,11,11,11,111 (12 x 2 = 24); smallest 2008 (5 + 6 + 6 + 7 = 24; three digits hold at most 21 sticks, and 1 as first digit leaves 22). Both right.

## 3. Where the book is unclear

- **Solutions pages exist.** The brief says the pdf has no printed-solutions section, but pdf pages 24-38 are printed answers; the only pictures among them for my chunk are the two Q9 arrangements (p.36, p.37).
- **P20 (Q9 boxes):** the page does not say which row is the larger number or which operation goes with which row; the 7-digit over 5-digit reading is taken from the box counts and the right alignment. Colours: peach (top) and lavender (bottom) in the book, mapped to the SET_B and SET_A outlines on white.
- **P23 digit strip:** the 7 has four bars in the picture but three sticks in the text (see 1.4). The book prints no answers for the toothpick puzzles and no pictures for them.
- **Q5:** the book's answer page has no printed answer for Q5 (question 5 is skipped between Q4 and Q6); the LP answer ("no such pair found") was not re-derived here.
