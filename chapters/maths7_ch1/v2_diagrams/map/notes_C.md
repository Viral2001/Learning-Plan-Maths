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
