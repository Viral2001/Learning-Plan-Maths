# Chunk D notes (Class 7 Ch 10, topics M5.S30.T30, S31.T31, S32.T32, S33.T33, S35.T35, S36.T36)

Result: 13 units, 24 items. Required 3 (worked example C112, worked example C113, question C119), optional 2 (solutions C120 and C122), none 19.
Output: `map/out_D.json`, validator `errors 0, warnings 0`. Five base figures claimed (3 to items, 2 to `none:`).

## 1. Judgement calls

1. **The three machine pictures are drawn (required).** Machine 1 (worked example, C112), Machine 2 (worked example, C113) and the unnumbered machine of Figure it Out Q7 (C119 question).
   - Q7: the book question is "find the operations done by the machine shown below", so the machine is the whole given. The LP text already transcribes all six rows, so a text-only reading is also defensible by the tie-breaker. I chose `required` because the LP text still says "shown below" and nothing is shown, and because the same kind of picture is drawn for C112/C113. **If you want text-only, flip C119 and the two worked examples to `none` (LATEX_TABLE); nothing else depends on them.**
   - C112 / C113 (worked examples): the question text names "Machine 1" / "Machine 2" but gives none of its rows (they appear only in the steps and in the book picture). This is a referred figure, so v3 rule B2 says to draw it even though the concept's teaching image (C112.IMG1, C113.IMG1) shows the completed machine. The figure is the machine as the book prints it: the two dotted circles in every row stay empty, the last star stays empty. The teaching images are not linked.
   - Every machine figure uses the same panel geometry (tall panel centred in the 16:9 card, 6 rows, 18 input squares, 12 empty circles, 5 filled stars, 1 empty star), so the three look like one family.
   - The name plate text ("Machine 1", "Machine 2", "Machine") is the machine's own label as printed in the book, not a caption. If the renderer or the "no titles" rule is read strictly, the plate can be left blank; nothing in the question or solution depends on it.
2. **Example 1 / Example 2 (units 68, 69): none on both sides.** The three inputs are in the question text and the rule was taught in the previous concept. The book's last row adds only those numbers and an empty star. This differs from the worked examples on purpose (there the rows exist only in the picture). The completed last rows (-13, -111) are already teaching images and are never linked.
3. **Q7 solution (C120): optional.** A completed machine (a - b x c in the circles, last star -70) would help, but the answer is an expression and a number, every row is checked in the LP steps, and the book prints no answer picture.
4. **Collatz Q5 (unit 71).** Question none: rule and example chain are in the text; the book's picture is a number chain with a loop-back arrow, i.e. a sequence (v3 Step C: number chains stay LaTeX). Solution optional: a flow picture (the loop 1, -2, -1, 4, 2, 1 with the chains from -21 and -6 joining it, and 13's own 31-number loop apart) would help the "describe the patterns" answer, but it is not needed.
5. **Q16 (unit 73): none on both sides.** The book picture is only three equations with empty boxes; the LP text already writes the boxes. The five filled-in ways for each of (a), (b), (c) are equations (boxes filled with numbers stay LaTeX).
6. **Figure it Out Q1(a), Q13, Q14, Q15, coin examples (units 63-65, 72, 74, 75):** the book prints no figure; pure arithmetic or word reasoning, none on both sides. Figure it Out Q10 (coins) has no picture in the book; a coin picture was not invented.
7. **Sibling consistency inside this chunk:** all arithmetic answers (63, 64, 65, 68, 69, 72, 73, 74, 75) are none; the two optional solutions (C120, C122) are the only ones where a picture would clearly help but text is complete.
8. **Ids:** the worked examples take `.IMG2` because `.IMG1` of their concepts is the kept teaching image. C119 question takes `.IMG1` (its old card is being replaced).

## 2. Things in the LP that look wrong or need care

- **Unit 71 (Collatz) question text prints 32 after 11** (copied from the book); the rule gives -32 and the LP's own solution says so ("The book prints 32 here, but the rule gives -32"). The question text therefore contradicts its solution until a reader gets to step 3. Consider writing -32 in the question, or keeping 32 with a one-line note. No picture was drawn, so the slip is not copied into an image.
- **Numbering and order differ from the book.** In T33 the LP's "Figure it Out, Q1..Q4" are the book's Q7, Q5, Q15, Q16 (and Q7 comes before Q5); in T30 "Q1, Q2, Q3" are the book's Q1(a), Q13, Q14; T36 "Q1" is the book's Q10. The LP holds only Q1(a) in unit 63; Q1(b), (c) sit in unit 57 (chunk C).
- **Unit 70 question text** says "the machine shown below" and then lists all rows. Once the figure is attached, the rows sentence repeats it. Harmless; it can stay for accessibility.
- **Unit 66 steps test only five rows**; the sixth row (-10, -12, -9) is the open row solved in unit 68 (Example 1). Same for unit 67 and unit 69. The figure keeps row 6 with an empty star, as in the book.
- **Unit 67 steps list the rows in a different order** from the book's machine (steps start with 5, 3, 7; the book's first row is 4, 8, -3). Each step names its row by values, so it is unambiguous; the figure follows the book's order.
- **Unit 75 extra block** ("Use lists of multiples to make a total of +4") is an LP-added example, not in the book (the book's own example is +85 with 10 and 5 coins, unit 74). Its arithmetic is right (13 - 9 = 4).
- Everything numeric in this chunk was recomputed and is correct: Q1(a) = -75; Q13 values -531684, -532108, -531137; Q14 = -5382; Q15 maximum 60 and minimum -60 (brute force over all orders and bracketings); Q16 all fifteen fill-ins; coin totals for (a) to (h) including 122 x 13 + 2 x (-9) = 1568; Machine 1 a + b - c, Machine 2 -(a x b) - c, Q7 a - b x c on all five given rows, last rows -13, -111, -70; Collatz chains for -7, -21, -6 and the 31-number loop of 13.

## 3. Where the book itself is unclear

- The Collatz picture (page 19) prints 32 after 11 (print slip; rule gives -32).
- The machines hide their operations by design (empty dotted circles); the book never prints the rule for Machine 2 or for the Q7 machine (this pdf has no printed solutions), so the LP's rules (-(a x b) - c and a - b x c) are the LP's answers, verified against every given row.
- Machine 2's question text sits at the top of page 19 while its picture is on page 18; the Q7 machine plate reads just "MACHINE" with no number and is printed slightly smaller than the two on page 18.
- Base inventory: all five entries I use match the page pictures; no corrections and no NEW- figures. P18-machine-1 is also used (last row) by unit 68 but is claimed once, by the worked example, because unit 68 needs no figure. The summary table, the Terhuchu board and the distributive-token figure are in other chunks' topics and are not claimed here.
