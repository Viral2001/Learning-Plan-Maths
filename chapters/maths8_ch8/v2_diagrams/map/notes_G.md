# Chunk G notes: Class 8 Ch 8 "Fractions in Disguise" (plan cbse_eng_maths8_ch8_v56)

Topics: M4.S16.T16 (Figure it Out Q1-Q9 of Growth and Compounding, 9 pairs), M4.S17.T17 (Tricky Percentages, 9 worked blocks over C171-C174), M4.S18.T18 (Putting It All Together, 3 worked blocks C175-C177).
30 items: required 1 / optional 1 / none 28. Output: `map/out_G.json`, validator `errors 0, warnings 0`.

Result in one line: the only figure this chunk needs is the Peaceful Knights board (C177). The book prints no figure for Figure it Out Q1-Q9 or for any of the money/percent worked examples; everything else is arithmetic with the numbers in the text.

## Borderline

1. **M4.S18.T18.C177 (Peaceful Knights), required, worked example.**
   - Which picture: a worked example has ONE diagram (after the question text). The book's given figure is an empty board; I drew the board WITH the example's 8 knights placed (final state), because the whole content of the example is the arrangement and an empty board adds nothing a learner cannot picture from "chess board". The v3 solution-figure-first convention supports showing the finished state before the steps. If the user wants the strict "given figure only" reading, the alternative is the same board with no knights (visible_text becomes empty).
   - Board size: see "Book mistakes" below (8 x 8, not the book's 10 x 10).
   - The book's small 5 x 5 knight-move board (P32-chess_board-2) is not drawn: the move rule is written in the book text, so `none:TEXT_SUFFICIENT`. The LP question text does not carry that rule (see LP text issues), so if the LP text is not fixed, that picture is the one a learner would miss.
   - Dark squares are drawn GUIDE grey (the "unused" colour), knights as the glyph U+265E in ANSWER green on light squares. If the renderer cannot print U+265E, a filled ANSWER disc of the same size is the only acceptable fallback.
2. **Example 13 model bars (book p.27: x, 1.5x, 0.75x), items C173 blocks 0-3 and C174, all none.** The figure is a "worked example picture" in the base inventory, but the plan already shows it as teaching image C173.IMG1, so P27-bar_model-1 is mapped `concept_image:M4.S17.T17.C173.IMG1`. No Step-B trigger applies to (i), (ii), (iii), Arun or Surbhi's Twelve Thousand: the numbers (50% margin, 50% discount, 12,000) are in the words and the steps carry x * 1.5 * 0.5 = 0.75x. If the user prefers a diagram per worked example, (i) "No loss?" (C173 block 0) is the item to turn required (three bars x, 1.5x, 0.75x, widths 4 : 6 : 3 units).
3. **M4.S16.T16.C166 (Q7 solution), optional.** A line graph of Rs 1000 over years 0 to 10 (straight line to 2000 at year 10; curve passing 2000 between year 7 and year 8) would clearly help "linear versus exponential" but the LP text answer is complete and the book draws nothing; not added. No other Q1-Q9 solution got this because only Q7 contrasts the two growth types (Q1, Q2, Q5, Q6, Q8, Q9 are plain arithmetic; Q3 and Q4 are text).
4. **Cakely/Cakify (C172 block 0) and 20% or Rs 50 (C171 block 1), none** although teaching images (C172.IMG1 bars, C171.IMG1 graph) exist. Neither is a book figure for the item; the two bakery pictures in the book are shop illustrations (decorative) and the sale question has no picture. Teaching images stay untouched and are never linked.
5. **Q3 (observe anything interesting?), question none (OPEN_ENDED)** and solution none: two sentences comparing 24,000/24,200 and 24,000/24,310.13.
6. **Summary (C176) none.** The two Summary figures (P31-bar_model-1 40% strip, P31-line_diagram-1 principal lines) are recap pictures of the Summary text, mapped `none:TEXT_SUFFICIENT`; the unit's question ("what did we find first?") is a reflection and carries no figure.
7. **P26-comic-1 (Puzzle-Solvers club comic), none:DECORATIVE_ONLY.** It is a teaching comic whose numbers (80%, 100%, 678 members) the LP text does not quote and no item asks about; if the content team wants it in the lesson, that is a teaching image job, not a diagram item.

## Book mistakes (decision 1)

- **Peaceful Knights board.** The book prints a 10 x 10 board (I counted the cell boundaries in the page picture: 10 columns and 10 rows, top-left dark red), with the words "chess board" and "8 knights". A chess board is 8 x 8. The LP answer "the 8 white squares of the first two rows" is true only on an 8 x 8 board (a 10 x 10 board has 10 white squares in two rows), and the LP teaching text says "any 8 x 8 grid" and "up to 32 is possible". The spec therefore draws the 8 x 8 board, top-left dark (as in the book), knights on row 1 columns 2, 4, 6, 8 and row 2 columns 1, 3, 5, 7. The base inventory keeps the printed 10 x 10 (its description is correct for the page); the correction is stated in the item's `reason`, `render_note` and `must_not_show`. This is the one point the user may want to confirm (8 x 8 vs the book's picture).

No printed-answer picture exists (this pdf has no solutions section). No other book slip found in my pages: all printed Figure it Out data matched the LP text, and I recomputed every LP answer in code: 20,000 x 1.2 = 24,000; 20,000 x 1.1^2 = 24,200; 20,000 x 1.05^4 = 24,310.125 (24,310.13, 310.13 more); 50,000 x 0.07 x 3 = 10,500; 50,000 x 1.07^3 - 50,000 = 11,252.15 (752.15 more); Giridhar 12,500 x 0.12 x 3 = 4,500, Raghava 12,500 x 1.1^3 - 12,500 = 4,137.50 (362.50 more); 1.5 x 1.03^3 = 1.639 (about 1.64 crore); 5,06,000 x 1.025^2 = 5,31,616.25; 1.1^7 = 1.949 and 1.1^8 = 2.144 (doubling between year 7 and 8); Example 12: 200 x 0.7 x 0.8 = 112, 200 x 0.5 = 100, single equivalent discount 44%; Example 13: 1.5x x 0.5 = 0.75x (25% loss), x = 16,000, d = 1/3 = 33.33%; Arun 100/120 = 83.33%, 16.67% fewer; Bengaluru 2.5 x 50 lakh = 1.25 crore.

## LP text issues (no LP text was changed; decision 2)

- **M4.S16.T16.C164 (Q6 answer), steps_tex**: "The topic's faded problem (see the faded ladder)." is a pointer, not a solution step. Suggested: "Giridhar (no compounding): $12,500 \times 0.12 \times 3 = 4500$. Raghava (compounded): $12,500 \times 1.1^3 = 16,637.50$, so the interest is $16,637.50 - 12,500 = 4137.50$."
- **M4.S18.T18.C177 (Peaceful Knights), question**: "Place 8 peaceful knights" lacks the board and the rule. Suggested: "Place 8 knights on an 8 x 8 chess board so that no knight attacks another. A knight moves two steps in one direction and one step at right angles to it (an L-shape)." The steps and answer also assume the board colouring; suggested answer wording: "For example, the 8 light squares of the first two rows (row 1: columns 2, 4, 6, 8; row 2: columns 1, 3, 5, 7)."
- **M4.S17.T17.C171 blocks 0 and 1**: the block `question` fields are only titles ("Would you rather?", "20% or Rs 50 off?"); the data sit in the concept's textbook-text block. Suggested block 0: "Option A: deposit Rs 100, get back Rs 300. Option B: deposit Rs 1000, get back Rs 1500. What is the percentage gain of each?" Suggested block 1: "A shop offers 20% off or Rs 50 off on any purchase above Rs 150. Which is better for a bill of (i) Rs 180, (ii) Rs 225, (iii) Rs 300?"
- **M4.S17.T17.C172 block 1 (Check my thinking)**: the `question` field stops at "Compared with the start it is" (no options a/b/c); the options and the answer are in the `text` field only. Suggested: "A price rises by 10% and then falls by 10%. Compared with the start it is (a) the same (b) 1% lower (c) 1% higher."
- **M4.S17.T17.C173 blocks 0-3**: the questions "(i) No loss?", "(ii) Sold for Rs 12,000", "(iii) Break-even discount", "Arun's statement" are fragments that depend on the Example 13 set-up (50% margin, then 50% discount; Ariba has 120% of Arun's marbles) held in another block of the same concept. Suggested prefix for each: "Surbhi marks goods up by 50% and then gives a 50% discount." and, for Arun: "Ariba says she has 120% of the marbles Arun has. What can Arun say about his marbles compared with hers?"
- **M4.S17.T17.C176 (Summary)**: the worked-example answer "The 100%, the base" is fine; the question is a reflection with no data, so nothing is missing.
- **M4.S16.T16.C166 (Q7 answer)**: "just over 7 years (doubled by the end of year 8)" is correct (exact 7.27 years) but a reader could miss that compounding is paid per year; suggested addition: "(after 7 years Rs 1000 has become about Rs 1949; after 8 years about Rs 2144)".

## Places where the book itself is unclear

- Peaceful Knights: 10 x 10 picture versus "chess board" and "8 knights" (above). Note the book gives no answer.
- The comic on p.26: which child speaks which bubble in panels 1-2 is not clear from the bubble tails (the base inventory says the same); irrelevant because the figure is `none`.
- Figure it Out Q7 (Math Talk) asks "how long to double"; the book gives no answer. The LP answer (10 years, just over 7) is mathematically correct; for compounding, "doubled during year 8" is the exact reading.

## Mapping summary (figure_inventory, 6 entries)

| fig_id | mapped_to |
|---|---|
| P26-comic-1 | none:DECORATIVE_ONLY |
| P27-bar_model-1 | concept_image:M4.S17.T17.C173.IMG1 |
| P31-bar_model-1 | none:TEXT_SUFFICIENT |
| P31-line_diagram-1 | none:TEXT_SUFFICIENT |
| P32-chess_board-1 | item:M4.S18.T18.C177 (question) |
| P32-chess_board-2 | none:TEXT_SUFFICIENT |

Figures NOT claimed by chunk G (they sit in the book sections of other chunks): P21/P22 deposit tables and P23 annotated expressions (Examples 7-9, topics M4.S14.T14 / M4.S15.T15, chunk F), P28-P30 end-of-chapter figures (M4.S19.T19). Pages 22-25 of my units (Figure it Out Q1-Q9, Would You Rather) carry no figure of their own.
