# Chunk B notes - Class 5 Ch 9 "Coconut Farm" (units 18 to 34)

Result: 28 items, required 4 / optional 0 / none 24. Validator: errors 0, warnings 0.
Required = Try It! Q1 (C55 question, C56 solution) and Try It! Q2 (C57 question, C58 solution), nothing else.
Everything else is none (text / LaTeX).

## Borderline

1. **Place value charts, T9 Q2 and Q3 (C37/C38, C39/C40): none, code LATEX_TABLE + HEADER_BOXES_ONLY.**
   The book asks "Now fill the place value chart" (Problem | H | T | O). Two readings are possible: ACTION_ON_FIGURE /
   ANSWER_IS_FIGURE ("filled table") says required; the Step C rules say a plain table of numbers with no colour meaning, and place-value
   header boxes filled with digits, go to a LaTeX array (the audit's "not a diagram" list names both). I followed the Step C rule as written,
   because a LaTeX array shows the chart exactly (there is no colour, arrow or drawing in it). If the user wants these four
   drawn, each pair would be one 4-column table card (question: the three example rows filled and the empty rows; solution: all rows filled,
   `derived_from` the question). Note the headings: the book prints H, T, O; the LP text says Hundreds, Tens, Ones.
2. **Try It! Q1 and Q2: both sides required although the LP text carries every number.** The book question IS the box diagram the learner
   completes (split tree: split the dividend, divide each part, join with the sign; halving chain). The LP question of Q1 even says "The boxes show a plus sign
   ...", which points at a figure the text-only plan lacks. The answer is the completed diagram (step B2, arrangement / filled figure).
   Q2 (halving chains) has no such sentence, but it is the same kind of box diagram in the same Try It! set, so it got the same decision
   (sibling consistency). These are flow diagrams with arrows and operators, not plain tables, which is why they differ from point 1.
3. **One combined picture per side for Try It!.** The LP holds Q1 to Q4 in one concept (C55) and Q5 and Q6 in another (C57), with one
   question card each; the brief allows ONE question diagram and ONE solution diagram per pair. So the four split trees are one 2 x 2 picture
   and the two halving chains one two-row picture. The v3 prompt says a question split into parts gets one diagram per part, but the LP did
   not split them, so the brief's rule won. If the user prefers six separate pictures, the LP would first have to be split into six concepts.
4. **Panel/row numbers are drawn** ((1) to (4), (5), (6)) because the LP solution text refers to the items by these numbers (user decision 3).
5. **C35 (nine blue boxes of divisions): none.** Nine independent facts and the two hints are written in the question text; the boxes carry no
   position, colour or arrow meaning. Codes LATEX_ARITHMETIC + NUMBER_LIST_IN_BOXES. (The pink grid of Let Us Do Q2 is chunk A's.)
6. **Worked examples C41 and C61 (kept teaching images) and C42, C43, C62, C63: none.** They are practice-value arithmetic written as short
   equations; text alone solves them exactly as well. The decision does not depend on the kept teaching images (user decision 5): C41's bar and
   C61's bar are teaching images and stay untouched and unlinked.
7. **Open questions (C51 to C54): none** (OPEN_ENDED); the LP solutions are sample answers written as equations.

## Judgement calls

- **Which figures I claimed.** P03-equation_boxes-2, P03-place_value_table-1 and -2, P05-split_tree-1 to 4, P05-halving_chain-1 and 2.
  Each Try It! figure also has a `NEW-P05-<name>-<n>-sol` entry for its second use (the completed solution picture).
- **Not claimed: the P06/P07 long-division layouts** (P06-long_division-1 and 2, P07-long_division-1 to 3). My T15 worked examples
  (C61 to C63) share the book sections `sf.text`, `sf.estimate`, `sf.discuss`, `ld.rule` with chunk C's units 35 to 40, but they use practice
  values (378 ÷ 6, 861 ÷ 7, 487 ÷ 9) and none of those layouts. Chunk C owns them; if C does not claim them the merge check will show it.
  The pink box "N = D x Q + R" on pdf page 7 is a formula callout, not in the base inventory; I did not add it (chunk C's `ld.relation` unit is the closer owner).
- **NEW figures.** The three purple text panels of the book's examples on pdf page 5 (1248 ÷ 6, 1992 ÷ 4, 128 ÷ 4) were not in the base
  inventory. They hold only worked arithmetic as plain text, so they are `NEW-P05-example-1..3` mapped `none:LATEX_ARITHMETIC`. I also looked at pdf page 6:
  the "Let Us Solve (a) to (h)" list has no figure.
- **Colours.** The book prints the boxes light blue; the spec uses CELL_FILL (house token). Question content INK, solution additions ANSWER green.
- **Blank in the halving label.** The book's "Halve ____" blank is read as the number being halved (84, 42, 72), the reading the LP solution supports.
- **Solution diagrams draw the LP's own splits** (64 = 40 + 24, 265 = 250 + 15, 1560 = 1600 - 40, 4824 = 4800 + 24); the book prints no answers
  and the LP says other splits work too.
- **Book mistakes (user decision 1): none found** in the figures of this chunk. All printed givens (expressions, signs, divisors,
  chart rows) agree with the LP, and every LP answer was recomputed (all 17 solutions are mathematically correct).

## LP text issues

- **M1.S9.T9.C37 / C38 and C39 / C40 (place value charts).** The question text only describes the chart in words. With the decision none (LATEX_TABLE) the table
  itself should be in the text. Suggested for C37: "Now fill the place value chart" followed by a LaTeX array with columns Problem, H, T, O and rows
  `40 \div 10 = | | | 4`, `400 \div 10 = | | 4 | 0`, `4000 \div 10 = | 4 | 0 | 0`, then four empty rows `700 \div 70`, `1400 \div 100`, `220 \div 20`,
  `2200 \div 20`. Suggested for C39: the same array with the six empty rows 110 ÷ 11, 860 ÷ 86, 7500 ÷ 750, 8800 ÷ 88, 2400 ÷ 24, 440 ÷ 22. The solutions (C38, C40)
  likewise: the filled arrays (values are in the `text_alternative` of each item). The book heads the columns H, T, O; the LP says Hundreds, Tens, Ones: pick one.
- **M1.S9.T9.C35 and C36, item (i).** "(i)" is not wrapped in math ($(i)$) while (a) to (h) are. Suggested: `$(i)$: $4000 \div 40 = ...$` in question_tex and steps_tex.
- **M2.S11.T11.C45 to C50 (book numbers).** The LP calls the book's three text boxes "Example 2", "Example 3", "Example 4"; the book prints them as 1, 2, 3.
  This may be on purpose (the LP's own Example 1 is the practice-value worked example C41); if not, `book_number` should read Example 1 to 3.
- **M2.S12.T12.C54 (repeated halving).** The text says "repeated halving works for the divisors 2, 4, 8 and 16", which reads as a complete list. Any power of 2
  works (32, 64, ...). Suggested sentence: "So repeated halving works for the divisors 2, 4, 8, 16 and every other power of 2, such as 32."
- **M2.S13.T13.C57 (Try It! Q2).** The question text does not mention the boxes or arrows (C55's does). With the diagram added this is fine; without it,
  add: "Fill the boxes: each arrow halves the number before it."
- **T10 and T15 worked examples (C41 to C43, C61 to C63).** The question lines end with "(practice values)", which is a build marker rather than text a child should read; consider removing it.

## Book unclear or odd

- Try It! item 3 (1560 ÷ 8): the minus sign in the second row is partly hidden by the page watermark in the picture; it is visible and matches row 1, and the LP question text also says minus for (3).
- Try It! 5 and 6: the book does not say what goes in the blank of "Halve ____"; the reading above is the natural one.
- The book prints no answers section (as the brief says), so none of the diagrams copies a printed answer picture.
