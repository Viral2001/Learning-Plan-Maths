# Chunk D notes (Class 5 Ch 4 "We the Travellers - II", topics M3.S30.T30 to M4.S42.T42, book pdf pages 12 to 15)

Result: 22 units, 38 items. Required 16 (7 question, 7 solution, 2 worked example), optional 5, none 17. Validator: errors 0, 2 warnings (the two worked examples C105 and C117 have required diagrams that are not printed book figures: the LP's own 2 by 2 grids and its 14/15 counters).

All base figures of this chunk were checked against the page pictures (page_12 to page_15): P12-grid-1 to 5 (labels read from the picture and they match, including the three small grids), P13-dot_pairs-1 (9 + 9) and P13-dot_pairs-2 (12 + 11, the 12th top counter unpaired), P14-table-1 and P15-table-1. No base description needed a CORRECTED note. No figure was missing from the base. The pdf has no printed-solutions section, so every solution figure follows the LP sample answer (I recomputed every grid in code against its inc/dec labels).

## 1. Judgement calls

- Grids (C107 to C116): question side required for all five (ACTION_ON_FIGURE + DATA_IN_FIGURE: the learner fills the empty labelled grid the book prints), solution side required (ANSWER_IS_FIGURE, derived_from the question figure, numbers in ANSWER green). Same decision for all five (sibling consistency), also for the plain all-inc and all-dec grids where the LP text already names the conditions. Sample answers are the LP's (many grids work). I re-checked them: 1,2,3/4,5,6/7,8,9; 9,8,7/6,5,4/3,2,1; 3,2,1/6,5,4/9,8,7; 8,6,1/7,5,2/3,4,9; 1,6,8/2,5,7/9,4,3 all satisfy their labels.
- Worked example C105 (2 by 2 grids): required. The single diagram of a worked example sits after the question text, but the answer of the example is the pair of filled grids, so I draw the FINISHED state (labels INK, numbers ANSWER). A blank labelled pair would only repeat the kept teaching image. If you prefer the "given only" state (blank cells), say so.
- Worked example C117 (14 and 15 counters in pairs): required (the answer is an arrangement, described only in words). The picture draws 14 as 7 pairs and 15 as 7 pairs plus one ringed counter, with pair outlines in ANSWER.
- C121/C122 (add 2 to 18) and C123/C124 (add 2 to 23): question figure = the book picture (required, "Observe the given arrangement"), solution figure = the changed arrangement (20 counters 10/10; 25 counters 13/12), the two added counters in ANSWER green. For 23 the book does not say where the new counters go; I put the new pair in column 12 and the left-over counter (ringed, FOCUS) slides one place right to column 13, so "the same 1 counter is still left over" is visible. That is the only given part that moves between question and solution figure (render_note says so).
- The captions "Paired arrangement for 18/23" are not drawn (the LP question text carries them).
- Kept teaching images are never linked; items C105 and C117 get their own diagrams although a teaching image shows the same idea (user decision 5). No REUSES_CONCEPT_IMAGE anywhere.
- Figure inventory: the book picture is mapped to the question item, and the same picture drawn again for the solution is a second entry `NEW-<base id>-sol` mapped to the solution item (7 NEW entries). Counts: 16 figures, 14 to items, 2 none (the tables), 0 concept images.

## Borderline (v3 rules applied as written, listed so you can flip them)

- C119 (circle the even numbers): question none (a plain list of 12 lettered numbers, no figure in the book), solution optional (a picture of the 12 numbers with 498, 724, 100, 846 and 222 ringed would help, but the LP answer lists them). Not added.
- C125 (worked, join 14+8, 9+13, 7+10) and the solutions C128, C130, C132 (Q3 a, b, c: sums of even/odd numbers): optional. Reason: the book says only "you may use the paired arrangement"; a counter picture of one chosen pair would help the explanation, the answers are sums and a rule in text. The same decision for all four. Not added.
- C133 (coins worked example) and C135/C136 (Jincy's coins): none. The answers are coin sums in LaTeX and no coin figure is printed in the book. A coin-mat picture would be "nicer" only.
- Torch items C137, C139/C140, C141/C142: none (parity argument in words; the kept teaching image already shows presses 1 to 8).
- C143 (worked, reading tables): none; all the data is in the question text and the kept teaching images are not linked.
- C145 and C147 (the two tables): none with LATEX_TABLE (plain tables, no colour meaning; the blue header of P15 is decoration). BUT the LP question text does not contain either table, see LP text issues. I did not change the decision (decision 2); `needs_lp_text_sync` is true and `text_alternative` carries the array content.
- C146, C148: none (answers are subtractions in text/LaTeX).

## 2. LP text issues

- **M4.S41.T41.C145** (question): says "Read the table and answer the questions that follow" but the table is not in the question text or LaTeX (only the old card showed it). With the old card dropped the learner has no data. Suggested: add to the question text a LaTeX array with columns Mountain | Height (in metres) | Climbed in the year and these rows: Mount Kanchenjunga (India and Nepal border) 8,586 2022; Mount Everest (Nepal-China border) 8,848 2013; Mount Makalu (China-Nepal border) 8,485 2019; Mount Lhotse (Tibet-Nepal border) 8,516 2018; Mount Kilimanjaro (Africa) 5,895 2016; Mount Elbrus (Russia) 5,642 2017; Mount Annapurna I (Nepal) 8,091 2021.
- **M4.S42.T42.C147** (question): "For each district, find out if the number of certificates were sufficient?" has no table and no story (the book: a Math Metric Mela where certificates were printed per district). Suggested: "A Math Metric Mela was held and every student was to get a certificate. The table shows the certificates printed and the students who attended." plus a LaTeX array District | Certificates Printed | Students Attended with rows Chittoor, A.P. 18,225 18,104; Jaunpur, U.P. 19,043 19,265; Raigad, Maharashtra 20,863 19,974.
- **M3.S31.T31.C109** (question): "This time, fill the grid such that each row and column has numbers in decreasing (dec) order." has no "3 by 3" and no "numbers 1 to 9, each once" (it relies on the previous question). Suggested: "In a $3 \times 3$ grid, arrange the numbers $1$ to $9$ such that each row and each column has numbers in a decreasing (dec) order. Each number should be used only once."
- **M4.S33.T33.C119** (question) and **C120** (steps): items (a) to (h) are written `$(a)$` but (i), (j), (k), (l) are plain "(i)"; make them `$(i)$`, `$(j)$`, `$(k)$`, `$(l)$` (also in C120's answer_tex for "(i): $846$").
- **M4.S33.T33.C124** (step 1): "(a row of $12$ and a row of $11)$" has the closing bracket inside the math; suggested "(a row of $12$ and a row of $11$)".
- **M4.S33.T33.C121 and C123** (question): the sentence "Paired arrangement for $18$" is the book's picture caption and reads as a loose phrase once the picture is a separate figure. Suggested: "The picture shows $18$ counters in two rows of $9$, each counter paired with the one below it." (and "twelve counters above eleven, the last top counter has no partner" for 23).
- Naming only (not read by the learner): concept names "Let Us Think and Solve (grids): Q1 to Q5" are the five grids of book Q2 (the book's Q1 is the palindrome question, topic T28); "Even and Odd Numbers: Q2/Q3" (T33) are the 18 and the 23 picture of book Q2; "Q1 to Q3" in T35 are book Q3 (a), (b), (c); "Let Us Think: Q1/Q2" in T37/T39 are book Let Us Think Q1 and Q2; T41 "Q1" is book Q3 (Mountain climbing).

LP maths I re-checked and found right: the 11 combinations of Jincy's coins (4 + 5 + 2, total 51 rupees available, 38 payable), the 4 ways of the coin worked example, all subtraction answers in C143, C146 and C148, the parity sample sums in C128, C130 and C132.

## 3. Places where the book is unclear

- Page 12: the pdf text layer lists the labels of the three small grids in a scrambled order; I took the labels from the picture (grid 3: rows dec, dec, dec / columns inc, inc, inc; grid 4: rows dec, dec, inc / columns dec, dec, inc; grid 5: rows inc, inc, dec / columns inc, dec, dec). The book says "numbers (1 to 9)" for the small grids and "each number only once" only in the first sentence; I read it as applying to all.
- Page 12 grids: "each row and column has numbers in increasing order" is read as rows left to right and columns top to bottom (the LP does the same). Many fillings are correct; the diagrams draw the LP's sample.
- Page 13, Q2: the book does not say where the 2 added counters go. Drawn as described above (new pair at the end of the old pairs).
- Page 13, Q1: the book prints no answer; no printed-solutions section exists in this pdf.
