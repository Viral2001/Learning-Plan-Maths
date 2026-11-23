# Notes for chunk F (Class 5 Ch 9 "Coconut Farm"): Mathematical Statements

Topics: M4.S35.T35 (Q1, Q2), M4.S36.T36 (worked example), M4.S37.T37 (Q3 a/b/c, Q4).
Result: 13 items, required 2 / optional 0 / none 11. Validator: errors 0 (10 warnings, all "long visible_text", see 1.8).
Figures claimed: P17-table-1 (Q4 question), NEW-P17-table-1-sol (Q4 solution, second use of the same table),
P17-label_arrows-1 (none:TEXT_SUFFICIENT). Both base figures of page 17 were checked against `book/page_17.png`: the
base descriptions are right (the answer column widths are about 12% / 17% / 10% of the table width, not "about equal").

## 1. Judgement calls

1.1 **Q4 tick table (C171 question, C172 solution): both required.** The book's blank tick table is the thing the
student acts on (tick one cell per row), and the answer IS the ticked table (v3 B2: `ANSWER_IS_FIGURE`,
`ACTION_ON_FIGURE`). The question text does not even name the three columns, so the figure is needed to attempt it.
This is not a "plain table of numbers". The solution is `derived_from` the question diagram (same grid, same positions,
five ticks in ANSWER green). One diagram only for C172 although the old plan had two cards (IMG1 and a "continued" IMG2):
one table, one picture.

1.2 **Row letters (a) to (e) shown in the Q4 picture.** The book's table has no letters, but the LP question and the LP
answer text both refer to the rows as (a) to (e), so by decision 3 the letters are drawn (they are in `visible_text`).
The statement text is the book's own row labels, so it is part of the figure (not question text pasted in).

1.3 **Header fill CELL_FILL, not the book's green.** The book's header is light green; MARK_FILL would suggest "marked
cells", so the neutral CELL_FILL is used. Answer columns are drawn with equal 238 px width for legibility.

1.4 **Q3 (a), (b), (c): all six items none.** The only book picture is the three red margin hints (Always true / Never
true / Sometimes true). They are word labels and would give the answer away in a question figure, so
`P17-label_arrows-1` is `none:TEXT_SUFFICIENT`. The answers are lists of sample equations plus a word, not a picture,
so the solutions are text/LaTeX. Sibling consistency: Q3 (a), (b), (c) get the same decision; Q4's solution differs
because its answer is a ticked table (different kind of answer).

1.5 **Q1 and Q2: none.** Plain equations; the book has no figure for them. (`LATEX_ARITHMETIC`.)

1.6 **T36 worked example (C163, block 0): none (`no_image`).** Three statements tested with numbers, all written in the
steps. The book has no figure for it (its `ncert_refs` is `st.labels`, the margin hints). A grouping picture would only be nice, not needed.

1.7 **Q4 (b) tick = Sometimes** follows the LP ("only for two equal numbers, with whole numbers"). See section 3.

1.8 **Warnings.** The validator warns that the five statement strings in `visible_text` are long (more than 6 words):
they are the table's row labels, drawn as two lines each, so I left them whole.

## Borderline

- **C171 / C172 (Q4 tick table) as required.** A careful student could decide always / sometimes / never from the text
  alone, and the LP text carries every statement and answer. I kept it required because the v3 rules say a printed
  filled/ticked table that is the answer is a figure (`ANSWER_IS_FIGURE`), the question acts on a given figure
  (`ACTION_ON_FIGURE`), and decision 4 says do not flip it to none because the text has the data. If the user prefers
  text, the fallback is a LaTeX array with the five statements and a tick column.
- **C163 worked example:** none, but a three-column picture "always / sometimes / never" would be the natural
  optional figure if the user ever wants one.
- **Row letters in the Q4 picture** (1.2): not in the book's table.

## 2. LP text issues

- **M4.S37.T37.C171 (Q4 question):** the question does not name the three choices, so the text alone does not say
  what the cells are. Suggested sentence: "Tick one cell for each statement: Always True, Sometimes True or Never True."
- **M4.S37.T37.C171 `question_tex`, statement (e):** the quote marks are mixed up with the maths: `‘$0’$`. Suggested:
  `‘$0$’ in the Ones place`.
- **M4.S37.T37.C172 (Q4 answer text):** the sentence "This is the plan's reading with whole numbers." in step (b) is
  internal wording; suggested "Here we use whole numbers only." Also the old `text` field has `[Image: ...]` markers
  in the middle of the steps (after step 2) and one "(continued)" marker at the end; under v3 the one token goes before
  step 1 and both markers go.
- **M4.S37.T37.C165, C167, C169 (Q3 a, b, c):** the book's red hints "Always true" (a), "Never true" (b),
  "Sometimes true" (c) are not in the LP question text. Left out on purpose (they give the answer); if the user wants
  them, e.g. "Hint: this statement is always true."
- **M4.S37.T37.C167, C169:** the questions (b) and (c) start without the Q3 lead-in "Think about the following
  statements and find examples as suggested below." (only (a) carries it). Fine as separate cards, but (b) and (c) read
  better with "Think about this statement:" at the start.
- **M4.S36.T36.C163:** the question says "(practice values)", which is odd for the student; suggested: "Decide if each
  statement is always, sometimes or never true." Also the lead "Worked example:" in `text` is fine.
- Maths in the chunk was re-checked and holds: Q1 values 72/72 T, 14/21 F, 16/16 T, 80/90 F, 35/35 T; Q2 blanks 25, 3,
  7, 72; the Q3 sample equations; Q4 (a) to (e) answers.

## 3. Places where the book itself is unclear

- The pdf has no printed answers, so every answer follows the LP.
- **Q4 (b) "Changing the order of the numbers in subtraction makes no difference."** For whole numbers the two orders
  differ unless the numbers are equal (6 - 6), and 3 - 8 does not exist in whole numbers; so "sometimes true" (LP) is
  defensible, but many teachers would say "never true". The diagram draws the LP's "Sometimes".
- **Q4 (c) "doubling one number and halving the other keeps the product the same"**: always true mathematically (the LP
  uses even starting numbers so halving stays whole).
- **Q3 red hint arrows:** the book does not say whether they are part of the question or a hint to the teacher; treated
  as hints (not drawn).
