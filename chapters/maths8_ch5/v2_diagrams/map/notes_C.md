# Notes, chunk C (Class 8 Ch 5 "Number Play", topics M2.S18.T18 to M2.S25.T25)

Result: 31 items (5 worked, 13 pairs): required 1, optional 2, none 28. Validator: errors 0, warnings 0.
Book pages used: pdf 13-19 (book p.124-130), pdf 21-22 (end-of-chapter Figure it Out), pdf 28-29 (printed answers). I looked at the picture of every one of those pages.
Every number in the LP steps of my 31 items was recomputed in code (remainders, digit sums, 11 x 29107 + 8 = 320185, 11 x 29827 + 8 = 328105, the four 3p7q8 pairs divisible by 44, 288, 6003, 4302 to 4392 = 11 multiples, all 90 cells of the table). All agree with the LP and with the book's printed answers.

## 1. Judgement calls and Borderline

**Borderline (v3 rules applied as written, user decision 4)**

1. **M2.S24.T24.C106 (worked example, the 10 x 9 Yes/No divisibility table): REQUIRED, the only diagram of the chunk.**
   - Why drawn: the book's printed answer to this question is the completed table (P29-table-1, "printed answer picture"), and the question gives a table to complete (P18-table-2). Step B2 says a printed answer that is a picture overrides text-first, and ANSWER_IS_FIGURE names a "filled table". The LP can only give the answer as ten lines of nine Yes/No words, where the column of each answer is lost.
   - Against: Step C `LATEX_TABLE` (plain table, no colour meaning) and the prompt's example of a fill-in count table that stays LaTeX. That example is a 5-entry table; this one has 90 position-dependent cells.
   - The single worked-example diagram shows the finished table (128 row corrected, see section 3). media_id `M2.S24.T24.C106.IMG2` (IMG1 is the kept teaching image of the concept; the build renumbers).
   - If the team prefers LaTeX: change this item to `none` / `LATEX_TABLE` and write the table as a LaTeX array with header "Number | Divisible by 2 3 4 5 6 8 9 10 11". Nothing else in the map depends on it, except that P18-table-2 and P29-table-1 would then become `none:LATEX_TABLE`.
2. **M2.S19.T19.C79 (solution of "remainders of 427 and 7309"): OPTIONAL, not added.** The book prints tile pictures for both answers (P13-tile_model-2/3 for 427, P14-tile_model-2 for 7309). The answer is a pair of numbers, the LP gives four complete equation steps, and teaching images C74.IMG1, C75.IMG1, C77.IMG1 already carry the model. The tie-breaker says a careful student loses nothing, so it is not required; it is optional (not `none`) because the book does print a picture for exactly this explanation. If the team wants it drawn, it needs ONE solution diagram, and the 427 and 7309 pictures would have to be combined or one of them dropped (a solution has at most one). The question side C78 stays `none`: the question gives only the two numbers.
3. **M2.S21.T21.C95 (worked example, 320185 excess and shortfall): OPTIONAL, not added.** The book's three pictures (P17-dot_model-1/2/3) colour digits 2, 1, 5 green and 3, 0, 8 red and end with 8 green circles over 11 red ones. This is the Step D case "grouping by colour for a sum already written", and the LP steps name every place and sum. Teaching image C95.IMG1 stays. If the team promotes it to required, draw the corrected labels (section 3, point 2).
4. **Number-line ideas, kept `none`**: C87 (closest multiple of 9 to 6000: marks 5994, 6000, 6003 with distances 6 and 3) and C89 (4302 to 4392 in steps of 9) would only make the answers nicer; the printed answers are plain numbers (6003, 11).
5. **C110 (prime factorisations of 12 and 24, LCM 12 and 24)**: word reasoning in products; teaching image C105.IMG1 draws the factor tiles. `none`. The book prints no picture.

**Sibling consistency**
- All Figure it Out items of this chunk (C84 to C93, C102/C103) and the in-text question pairs without a printed picture (C80/81, C98/99, C100/101, C107/108, C109/110) are `none` on both sides: a number or a word reasoning, no figure given, no figure printed in the answer.
- Optional (not none) only where the book prints a picture for that item's own explanation: C79 and C95. C99 (462) has no printed picture for its answer, so it is `none`.

**Figure accounting (14 base figures, all claimed)**
- Teaching pictures are accounted to the teaching image that shows the same idea (accounting only, nothing is linked): P13-tile_model-2 and P14-tile_model-1 to C74.IMG1; P13-tile_model-3 to C77.IMG1; P14-tile_model-2 to C75.IMG1; P16-table-1 to C94.IMG1; P17-table-1 and P17-dot_model-1/2/3 to C95.IMG1; P18-table-1 to C96.IMG1. The match is by idea, not pixel for pixel (P14-tile_model-1 also shows 999 and 9999, P16-table-1 also shows tens and thousands).
- P13-tile_model-1 (two blue 99|1 and three green 9|1 tile pairs, no labels): `none:TEXT_SUFFICIENT`. Its meaning is not stated in the book (the text beside it only says 99 is divisible by 9 and 109 is not) and it does not draw 99 or 109, so I did not map it to a teaching image.
- P14-annotated_equation-3 (equation chain with two underlines): `none:LATEX_ARITHMETIC`.
- P18-table-2 and P29-table-1 both map to `item:M2.S24.T24.C106 (question)`, the one worked-example item (the validator's candidate list for a worked item uses the role `question`).
- P19-illustration-1 (Digital Roots club cartoon) is on page 19 but belongs to the Digital Roots topic (M2.S27.T27), not to my chunk; I did not claim it.

## 2. LP text issues

(Not edited; no decision was changed because of them.)

- **M2.S20.T20.C92** (`question_tex`, `text`): "If $I$ reverse its digits" has the pronoun I in math italics. Suggested sentence: `Sreelatha says, "I have a number that is divisible by $9$. If I reverse its digits, it will still be divisible by $9$".`
- **M2.S25.T25.C110** (`steps_tex` step 2, `text`): "needs three $2s$" renders as 2 times s. Suggested: `needs three $2$s` (or "three 2's").
- **M2.S23.T23.C103** (`steps_tex` step 4, `answer_tex`, `text`): math delimiters are misplaced, e.g. `gives $(7$, $0)$, $(5$, $2)$, ...` and `($p$, $q) = (7$, $0)$, ...`. Suggested step 4: `$p + q = 18$ needs $p = q = 9$, which is odd; $p + q = 7$ with $q$ even gives $(p, q) = (7, 0), (5, 2), (3, 4), (1, 6)$.` Suggested `answer_tex`: `$(p, q) = (7, 0), (5, 2), (3, 4), (1, 6)$`. (The plain `answer` is fine.)
- **M2.S22.T22.C101** (`answer_tex`, `text`): "(v): divisible (vi): divisible" lacks a separator. Suggested: `(v): divisible; (vi): divisible`.
- **M2.S24.T24.C106** (`text`): the opening repeats itself: "Checking Divisibility Quickly: fill the table: Fill in the following table: for each of ...". Suggested: `Checking Divisibility Quickly: Fill in the following table: for each of 128, 990, ...`. The ten answer lines have no column labels; the new diagram supplies them, so no text change is needed for the diagram.
- **Book numbering in the LP (`book_number` / concept names)**:
  - C82 says "Multiples of Nine, Q1"; the book has no such heading, it is Figure it Out Q1 on book p.126. Suggested: `Figure it Out, Q1`.
  - C84, C86, C88 say Q1, Q2, Q3; in the book they are Q2, Q3, Q4 of the same set (book p.126). Suggested: `Figure it Out, Q2`, `Q3`, `Q4`.
  - C90 and C92 say Q4 and Q5; in the book they are Q1 and Q4 of the end-of-chapter Figure it Out on book p.132. Suggested: `Figure it Out (p.132), Q1` and `Q4`.
  - C102 says Q1; in the book it is Q6 on book p.133. Suggested: `Figure it Out (p.133), Q6`.
- **C80/C81**: the book gives only the four statements; the test numbers 7309 and 4581 are the LP's own choice (4581 = 9 x 509). Not an error, noted so nobody looks for 4581 in the book.
- **C76**: the test number 123456 is the LP's own (the book only names 15, 33, 87). Not an error.

## 3. Places where the book is unclear or wrong

1. **P18-table-2 (question table, pdf p.18):** the pre-filled 128 row prints "No" under 4. The printed answer (pdf p.29), the LP and the mathematics all say Yes (128 = 4 x 32). Per user decision 1 the C106 diagram shows **Yes**; the inventory entry keeps what the book prints.
2. **P17-dot_model-2 and the text under the 3-step table (pdf p.17):**
   - The shortfall tree labels read "3 x 10,000" and "0 x 100". The three blocks are labelled 9091, and 11 x 9091 = 100001, so they stand for lakhs: it should read "3 x 1,00,000". The digit 0 of 320185 is in the thousands place, so "0 x 100" should read "0 x 1000". (The excess tree "2 x 10,000", "1 x 100", "5 x 1" is correct.)
   - The sentence below the table says "the number 3,28,105 is 3 short of or 8 more than a multiple of 11" while the example is 320185 (328105 is the next example). The LP correctly uses 320185 for the first example and 328105 for the second.
   - Nothing is drawn from it (C95 is optional), so this only matters if the team promotes C95.
3. **P13-tile_model-1 (pdf p.13):** no caption or labels; the text does not say what it shows. I read it as a preview of the "99 + 1 / 9 + 1" tile model.
4. **P17-dot_model-2 strips:** I could not count reliably whether each of the eight strips shows 11 or 12 round marks (the inventory agent also flagged it). Irrelevant to any decision.
5. **Printed answers:** this pdf prints answers only for the Figure it Out sets, the "Zero" answer and the six remainders for 11, and the table. There is no printed answer for 427, 7309, the four statements, 462, the divisibility by 6 and 24 questions. The LP solution text is the answer for those; it is mathematically correct.
