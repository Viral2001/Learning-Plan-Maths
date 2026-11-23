# Notes, chunk E (Class 5 Ch 8 "Weight and Capacity")

Units: 67 (worked example M3.S33.T33.C126) and 68-72 (Let Us Solve Q1-Q5, topic M3.S34.T34). Result: 11 items, required 0 / optional 0 / none 11. Validator: errors 0, warnings 0.

I looked at book page 15 (Let Us Solve) in the page picture: it is plain text, no figure of any kind (only the NCERT watermark and the closing line "Use the double number line whenever needed to solve such problems."). The base inventory has no entry on page 15, and the worked example C126 has no printed counterpart in the book. So this chunk claims no inventory figure (`figure_inventory` is empty, `coverage_report` all zeros). The merged-map completeness check is not affected: no base figure belongs to these units. The inventory agents' `unclear` doubts concern figures of other chunks.

## Judgement calls

1. **M3.S33.T33.C126 (worked example, 6 jugs of 1 l 250 ml and 9 l 600 ml into 8 cans): none** (TEXT_SUFFICIENT, LATEX_ARITHMETIC). Every number is in the text, the steps are l/ml multiplication and division, nothing is referred to as a figure, the answer is not a picture. The decision is made on the rules and the tie-breaker, not because the kept teaching image M3.S33.T33.C126.IMG1 already shows the jugs and cans (user decision 5 respected: no REUSES_CONCEPT_IMAGE, no link, teaching image untouched).
2. **Let Us Solve Q1 to Q5, question side: none.** The book prints no figure for any of them and the questions give none, so no question diagram (companion note: never invent a "given" figure). Reason TEXT_SUFFICIENT.
3. **Let Us Solve Q1 to Q5, solution side: none.** Every answer is a number, a name or a price, reached by conversion and arithmetic (LATEX_ARITHMETIC, TEXT_SUFFICIENT). No printed-solutions section exists in this pdf, and the LP answers are text, so the "printed answer is a picture" rule does not fire. Sibling consistency holds: all five pairs get the same decision on both sides.
4. Q2 and Q3 have lettered parts (a), (b), (c): these are sub-questions, not lettered figures. No figure letters are drawn anywhere (no diagrams at all).

## Borderline (applied the v3 rules as written; none flipped for LP-text reasons)

- **C126 worked example.** Could carry a jugs-and-cans picture (a teaching image of exactly that already exists), but no trigger makes the figure necessary and the tie-breaker answer is "a careful student solves it from the text". Kept none.
- **Q1 (Riya vs Aarav).** A side-by-side jugs comparison (Riya 4,000 ml against Aarav 2,250 ml) would be nice, but it only makes the answer prettier: optional at most, and optional is not added. Kept none.
- **Q3 (a) (5 l into 250 ml glasses).** A row of 20 glasses or a double number line would help some learners, and the book's closing line says to use a double number line "whenever needed". But the question gives no figure and the answer is the number 20 by division. Kept none.
- **Q2 (b) (bottle poured into 8 glasses).** A bottle-and-glasses picture would only restate the text. Kept none.

## LP text issues

(Listed only; no decision was changed because of them.)

- **M3.S33.T33.C126**: the question text ends with "These are practice values." This looks like a leftover authoring note, not part of the problem. Suggested: delete that sentence.
- **M3.S33.T33.C126**: the block has only plain `question` / `steps` / `text` (units written as "1 l 250 ml", "6 × 1 l 250 ml") and no `question_tex` / `steps_tex` / `answer_tex`, unlike the Let Us Solve concepts. If a diagram were ever added to this block, its token has no `question_tex` to go into. Suggested: add LaTeX versions, e.g. `$6 \times 1\text{ l}\; 250\text{ ml}$`.
- **M3.S33.T33.C126**: `ncert_refs` is "ls.dnl", which is not a book reference (the book has no printed example of multiplying or dividing capacities; the nearest book items are the weight examples on p.9). No `book_number` either.
- **M3.S34.T34.C130 / C131 (Q2)**: the LP solution step (b) says "each glass is filled to its capacity, so 2,880 ml was poured", but neither the LP question nor the book says the glasses are filled to capacity. Suggested sentence for the question: "Each glass is filled up to its capacity."
- **M3.S34.T34.C128 to C137 (Q1-Q5)**: the book's closing line "Use the double number line whenever needed to solve such problems." is not carried by any of these LP concepts. Suggested: add it once as a hint under Q1 (or as a closing line of the topic).
- **Answer concepts C129, C131, C133, C135, C137**: `item_kind` is "unsolved" although they hold the worked answers. Probably a harmless pipeline label; no change needed for diagrams.
- The question and answer concepts repeat the full question text (answer concept's `question` field). That is the LP design, not an error.

All LP solution arithmetic was recomputed and is right: Q1 4,000 and 2,250 ml, difference 1,750 ml; Q2 8 × 360 = 2,880, + 120 = 3,000, 3 × 40 = 120; Q3 5,000 ÷ 250 = 20, 5,000 − 2,500 = 2,500, 20 × 25 = 500; Q4 8,400 ÷ 7 = 1,200; Q5 8 × 1,075 = 8,600; C126 6 × 1,250 = 7,500 and 9,600 ÷ 8 = 1,200.

## Book unclear

- Let Us Solve Q2: the book does not say whether the 8 glasses are filled to the brim. Part (a) asks the total capacity of 8 glasses and part (b) the initial milk, so the intended reading is "each glass is full" (as the LP solution states). Noted above as an LP text issue.
- No book errors found on page 15 (digits, units and counts match the LP text).
