# Class 8 Ch 5 Number Play - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths8_ch5` v36 (taken from staging). Result: new V2 version v37 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (125 items from 73 units)
{"worked_example": {"none": 18, "optional": 2, "required": 1}, "question": {"none": 50, "required": 2}, "solution": {"none": 49, "required": 2, "optional": 1}}

Optional, NOT added: [('C79', 'solution'), ('C95', 'worked_example'), ('C152', 'worked_example')]

needs_lp_text_sync: []

## The 5 diagrams
| id | side | type |
|---|---|---|
| M1.S8.T8.C25.IMG1 | question | dot_array |
| M1.S12.T12.C44.IMG1 | question | other |
| M1.S12.T12.C45.IMG1 | solution | other |
| M1.S15.T15.C59.IMG1 | solution | dot_array |
| M2.S24.T24.C106.IMG2 | worked example | cell_grid |

### Chunk A notes (from the decision agent)
# Notes, chunk A (Class 8 Ch 5 Number Play, topics M1.S2.T2 to M1.S11.T11)

Result: 29 items, required 1 / optional 0 / none 28. Validator: errors 0, warnings 0. Base figures claimed: 25
(1 item, 10 concept images, 14 none).

Book pages used: pp.1-11 (teaching text, tables, dot pictures), pp.21-22 (end-of-chapter Figure it Out Q3 and Q9) and the
printed-answer pages pp.25, 26, 32, 34. All page pictures were looked at; the answer pages carry no figure.

## 1. Judgement calls I was unsure about

- **M1.S8.T8.C25 question: required** (`FIG_REFERENCED`, `DATA_IN_FIGURE`; media id `M1.S8.T8.C25.IMG1`). The book task (p.6-7) says
  "Look at the following expressions and the visualisation. Write the corresponding explanation and examples." and prints the
  dot picture (blue p rows of 4 + yellow q rows of 4 with 2 over = stack, long arrow "(p + q) rows with a remainder 2") in the
  third table row. This is the only item of the chunk whose book question gives a figure that matters. The picture is not a
  concept image (the teaching image `M1.S7.T7.C24.IMG1` uses 4 + 6 = 10), and no concept image is linked anyway. The label
  "with a remainder 2" is printed in the book's own figure, so it is part of what the question gives. I re-flowed the book's
  two-line arrangement into one line for the 16:9 card (content unchanged); coordinates are in the spec.
- **M1.S8.T8.C26 solution: none** (`SAME_AS_QUESTION_DIAGRAM`). The book's picture is already complete; the LP solution adds
  algebra and three number examples in text, nothing new to draw. Therefore no `derived_from` pair either.
- **All worked examples of the chunk (C2, C4, C5, C16, C22, C23, C29, C30, C32): none.** They are arithmetic or algebra with
  no figure given. For C22, C23, C29, C30 and C32 the book's dot rectangles are teaching figures and the plan already carries
  them as teaching images (kept, never linked), so a second picture would only duplicate them.
- **Cards of expressions (C18 and C20 questions): none** (`NUMBER_LIST_IN_BOXES`). The book prints the expressions in boxes;
  nothing but the expressions is in them. Same decision for both (sibling rule).
- **Teaching figures with no matching concept image** (P06-dot_array-2, P08-dot_array-2, P08-dot_array-4, P09-dot_array-2):
  mapped `none:TEXT_SUFFICIENT`, because their content is carried by the algebra and numbers of the worked examples. They are not
  decoration, I only had no better code; a different code would be fine with me.
- **P04-tree_diagram-1** (the lettered a, b, c, d tree) is mapped to the numeric tree's concept image `M1.S2.T2.C3.IMG1`
  (same shape, 3 4 5 6 instead of a b c d), for accounting only.
- **Decorative characters not inventoried** (as the base does): the owl boxes on p.4 and the boy with the speech bubble on p.10.
  Their words ("Can I write an even and an odd number as 2n and 2n+1 instead?") are in the LP text.

## LP text issues

- **M1.S8.T8.C25 (question) and M1.S8.T8.C26 (solution):** the question text never mentions the dot picture that the book gives
  ("Look at the following expressions and the visualisation"), yet the solution says "The full rows stack up and 2 dots are always
  left over", which only makes sense with the picture (or the teaching image of the previous topic). Suggested question sentence,
  to be placed before "write the explanation and examples": "Look at the expressions 4p + (4q + 2) = 4p + 4q + 2 = 4(p + q) + 2 and
  at the picture below, where p rows of 4 dots are joined to q rows of 4 dots and 2 more dots."
- **M1.S6.T6.C20 (question):** the book's list of algebraic expressions has nine cards; the LP lists eight (x^2 + 2 is left to the
  worked example C16, where it is handled). Suggested: either add "x^2 + 2" to the question list and a line to C21, or leave as is
  because C16 covers it.
- **M1.S11.T11.C36 (question_tex):** brackets are written "(i):", "(ii):" etc. with a colon, the plain `question` field and the
  book write "(i)" without it. Cosmetic.
- **LP book numbers differ from the book's:** C11 says "Figure it Out, Q1" (book: Figure it Out Q2 on p.11); C13 says "Figure it
  Out, Q2" (book: end-of-chapter Q9, p.22); C9 and C36 say "Multiples and Remainders, Q1 / Q3" (book: Figure it Out Q1 / Q3 on
  p.11); C27 says "Figure it Out, Q1" (book: end-of-chapter Q3, p.21). These are the LP's own labels; I found the items by text.
- No wrong number was found in any LP solution of this chunk: I re-added every sum, factorisation and example (for example the
  eight signed sums of 3, 4, 5, 6 and the claim that 0, -2, -4 appear for every four consecutive numbers, a - (a+1) - (a+2) + (a+3)
  = 0 and so on).

## 3. Where the book itself is unclear

- p.8, P08-dot_array-2: the staircase boundary between regions p and q is hard to read in print (the base inventory says the same).
  No item uses it.
- Printed answer p.25, Q3 (ii): "30 is not divisible by both 18 and 9" is a wording slip for "by neither"; the LP uses 10, no problem.
- The brief says the pdf has no printed-solutions section; it does (answers on pp.25-37, headed "Page No. ..."). I used them
  to check the Figure it Out items; they agree with the LP solutions (Q1 7-10; Q2 p - 1 to p - 4; Q3 sometimes/sometimes/sometimes/
  always/sometimes; end-of-chapter Q3 m + n even; Q9 5p - 4, 5p - 2, 5p + 2, 5p + 4).
- No book print mistake that changes a spec value was found, so decision 1 (corrected values) did not apply.

## Borderline

- **M1.S3.T3.C8 solution (the eight signed expressions): none.** A completed sign tree with all eight results next to its leaves
  would be a faithful answer picture (the book says "You can use the diagram below to systematically list all the possibilities
  ... write the result next to it"). I kept it as LaTeX arithmetic because the answer is a list of eight sums and the tree is
  already the teaching image `M1.S2.T2.C3.IMG1`. If you want it drawn, it is a `number_pattern` tree: 3, two 4s, four 5s, eight 6s,
  leaves = the eight expressions with values 18, 6, 8, -4, 10, -2, 0, -12 (tree order +++, ++-, +-+, +--, -++, -+-, --+, ---).
- **M1.S6.T6.C19 and C21 solutions: none.** Could be the eight cards with the four even ones in ANSWER green; judged not needed
  (the answer is a verdict with a parity reason, not a drawing).
- **M1.S7.T7.C22 worked example: none.** Six dot arrays in rows of four (4, 12, 36 fill rows; 18, 22, 42 leave 2 over) would help
  but duplicate teaching image `M1.S7.T7.C22.IMG1`.
- **M1.S8.T8.C25 question: required** is itself the closest call of the chunk (the algebra alone is enough to attempt the task);
  I followed the book's own wording "and the visualisation" and decision 4 (no flipping to none because the LP text has the algebra).

### Chunk B notes (from the decision agent)
# Notes for chunk B (Class 8 Ch 5 "Number Play", plan cbse_eng_maths8_ch5_v36)

Chunk B = topics M1.S12.T12, M1.S13.T13, M1.S14.T14, M1.S15.T15, M2.S16.T16, M2.S17.T17: 14 pairs + 4 worked examples = 32 items.
Result: required 3 / optional 0 / none 29. Validator (`--chunk B`): errors 0, one expected warning (see "Q7 solution" below).

| Item | Decision | Media id |
|---|---|---|
| M1.S12.T12.C44 question (book Q16, four Venn options) | required | M1.S12.T12.C44.IMG1 |
| M1.S12.T12.C45 solution (Venn (iv) alone, with 4, 8, 32 placed) | required, derived_from C44.IMG1 | M1.S12.T12.C45.IMG1 |
| M1.S15.T15.C59 solution (book Q7 "show visually", dot rows) | required, derived_from null | M1.S15.T15.C59.IMG1 |
| every other item | none | - |

The worked-example units (C47, C48, C68, C69) are all `none`. Their kept teaching images (`C47.IMG1`, `C48.IMG1`, `C68.IMG1`, `C69.IMG1`) stay and are never linked.

## Borderline

1. **M1.S12.T12.C45 (Q16 solution) - required.** The book's printed answer is only "Ans. (iv)", and (iv) is already one panel of the question figure, so a plain copy of panel (iv) would be `SAME_AS_QUESTION_DIAGRAM` (none). I chose `required` (`ANSWER_IS_FIGURE`, the answer IS a Venn picture, B2) and made the figure add something: panel (iv) alone at 1.9x with the three example numbers that LP step 3 uses placed in their regions (4 in the outer set only, 8 in the middle ring, 32 in the innermost set), in ANSWER green. If the reviewer reads the rule strictly, the alternative is `none` / `SAME_AS_QUESTION_DIAGRAM` for this one item. The old LP author's hint (`s_figure`) also said "Diagram (iv) alone". `derived_from` = the question figure; note the solution is one panel of it, not the 2 x 2 layout.
2. **M1.S15.T15.C59 (Q7 solution) - required, and the question C58 - none.** The question says "Show the solution both algebraically and visually", the book's printed answer gives only the algebra and "For visual method refer P. 120 of the textbook", and LP step 4 describes the visual in words ("rows of 7 dots with 5 and 3 dots left over; the leftovers join to make a full row and 1 more, or 5 minus 3 leaves 2"). A word description of a dot picture does not replace the picture (B2, `ANSWER_IS_FIGURE`). The question side gives all its data in words and the book prints no figure with it, so no question figure (rule: no question figure when the question gives none). This is not the 'refer picture' case of B2: the question's data is not in a picture, and the picture the answer points to (7-wide dot rows for 7k, pdf page 9 / book p.120, base figures P09-dot_array-4/5) does not show remainders, so the solution draws its own figure (`derived_from` null).
3. **Worked examples C47 and C48 - none** although the book's What Remains? section has dot pictures and each concept already has a teaching image. The worked examples are plain remainder arithmetic and a short list of numbers; nothing asks the student to use a figure, and a teaching image is never linked. Tie-breaker: a careful student solves them exactly as well from the text. Same reasoning for C68 and C69 (place-value sums).
4. **Possible but not added:** C55 (pebbles, a number line of 31, 61, 91 with a divisible-by-7 check), C65 (the 12-periodic triples 2-3-4, 14-15-16), C67 (a table of remainder triples) and C51 (value table of 5k + 3 and 5k - 2) could each be drawn, but all of them are plain tables or number lists that the text carries (`LATEX_TABLE` / `TEXT_SUFFICIENT`). I gave C51 and C67 an optional LaTeX array in `text_alternative`.
5. **Venn colours.** The book tints the options differently (for example (i) blue, yellow, green but (iii) and (iv) in other greens/blues). The spec colours by set (4 = SET_A, 8 = SET_B, 32 = MARK_FILL) in every panel, so a colour always means the same set. Geometry, order of nesting and arrow targets are as printed.
6. **Figure letters.** Roman numerals (i) to (iv) are drawn in the Q16 question figure and (iv) in the solution figure because the LP answer says "Diagram (iv)" (decision 3). In the Q7 figure the panels are marked (i) and (ii) because LP steps 2 and 3 use "(i):" and "(ii):".

## Figure inventory (12 entries)

- `P23-venn_diagram-1..4` (the four given options, chapter p.23 = pdf page 23) -> `item:M1.S12.T12.C44 (question)`.
- `P37-venn-4` (the option printed again on the solutions page under "Ans. (iv)") -> `item:M1.S12.T12.C45 (solution)`.
- `P37-venn-1..3` (reprints of the options (i), (ii), (iii) on the solutions page) -> `none:SAME_AS_QUESTION_DIAGRAM` (the solution shows only (iv); these three are the same drawings as the question figure's panels).
- `P10-dot_array-1`, `P10-table-2`, `P11-table-1` (What Remains?: 5k + 3 as rows of 5, the values table, the 5k - 2 table) -> `concept_image:M1.S13.T13.C46.IMG1` (accounting only; plain tables / teaching picture).
- `NEW-P11-pebble-pot` (the pot character with pebbles beside the Q5 riddle on pdf page 11, missing from the base) -> `none:DECORATIVE_ONLY`.
- All base descriptions I used were checked against the page pictures (pdf pages 10, 11, 22, 23, 37); I found no wrong description. The base doubt on `P37-venn-2` (which set the yellow ellipse stands for) is real: the book draws option (ii) with the "Multiples of 8" arrow starting inside the overlap and the "Multiples of 32" arrow at the right ellipse, so the option is deliberately inconsistent (two ellipses for three sets). I drew it as printed.
- The solution M1.S15.T15.C59 has no inventory figure (the book prints no figure for it; it only points to P. 120), hence the one validator warning "required but no inventory figure maps to it". I did not claim P09-dot_array-4/5: they lie in the book section of chunk A.

## LP text issues

(No LP text was changed and no decision depends on these.)

- M1.S12.T12.C38, question_tex: `don'$t$` puts the letter t in math mode. Suggested: "other multiples of $11$ don't remain multiples of $11$ when doubled."
- M1.S12.T12.C40, question_tex: "(i): ... (ii): ..." have a colon after each numeral (the book prints "(i) ..."). M1.S12.T12.C41: step 5 "so (iv): is never true" and answer_tex "(i): always (ii): always (iii): always (iv): never" carry the same stray colon. Suggested: "so (iv) is never true" and "(i) always, (ii) always, (iii) always, (iv) never".
- M1.S12.T12.C44, question_tex: the question does not name the four options although the LP answer says "Diagram (iv)". Suggested sentence: "Which of the four Venn diagrams (i) to (iv) shown below captures the relationship between the multiples of $4$, $8$, and $32$?" (the figure is placed after the question text).
- M1.S14.T14.C51, answer_tex: `$5k + 3 (k$ from $0)$ and $5k - 2 (k$ from $1)$` has math mode opened and closed in the wrong places. Suggested: "$5k + 3$ (with $k$ from $0$) and $5k - 2$ (with $k$ from $1$); the other four do not work".
- M1.S14.T14.C50, question_tex: the six expressions have no numerals (i) to (vi) although the book numbers them (i) to (vi); the answer text does not refer to them by number, so this is cosmetic. The book prints (iii) as the fraction 3k over 5; the LP writes `3k \div 5` (same value).
- M1.S15.T15.C54 and M1.S15.T15.C62: the pronoun is typeset as `$I$` (math italic) and the contractions as `won'$t$` (C54). Suggested: plain "I take", "I hold", "won't".
- M1.S15.T15.C59, steps: the picture is a part of the solution (placed before step 1); step 4 begins "Visually:". Suggested: "Visually (see the picture above):" so the learner knows the figure belongs to this step. The m and n of step 1 are the row counts written on the figure.
- Numbering: the LP's `book_number` labels do not match the book. T12 "Figure it Out, Q1 to Q4" are the end-of-chapter questions Q11, Q12, Q14, Q16; T15 "Figure it Out, Q1 to Q7" are section-5.1 Figure it Out Q5, Q6, Q7, Q8 (FiO1) followed by end-of-chapter Q2, Q7 and Q13 (FiO4); T14 C52 "Multiples and Remainders, Q4" is section-5.1 Figure it Out Q4. Not a diagram matter; suggested only if the numbers are shown to students.
- Missing data: none found. Every number a required figure needs is in the question, the LP solution or the book (Q7: 661 leaves 3, 4779 leaves 5, divisor 7).

## The book itself

- Q16 option (ii) is internally inconsistent by design (see above); drawn as printed.
- Q7 printed answer: "For visual method refer P. 120 of the textbook". Book page 120 (pdf page 9) shows rows of 7 dots labelled "k rows" for 7k, but no remainder picture, so the pointer is vague. I took the visual from LP step 4 and drew it in the book's dot-row style.
- pdf page 11 carries the pebbles picture (pot character) that the base inventory skipped; added as `NEW-P11-pebble-pot`.
- Book mistakes needing a corrected value: none found in my chunk's figures.

## Geometry self-checks done in code (builder kept outside HERE)

- Q16: every arrow start lies in the region its label names; in (iii) and (iv) each shape is wholly inside the previous one (360-point check); in (i) 4 and 32 do not touch, 4-8 and 8-32 overlap; in the solution figure 4, 8, 32 sit in the outer set only, the middle set only and the innermost set respectively.
- Q7: 661 = 7 x 94 + 3, 4779 = 7 x 682 + 5, 4779 + 661 = 5440 = 7 x 777 + 1, 4779 - 661 = 4118 = 7 x 588 + 2; the figure shows 5 + 3 = 8 = 7 + 1 loose dots (5 SET_A + 2 SET_B in the full row, 1 SET_B left) and 5 - 3 = 2.
- A rough picture drawn from each spec was looked at for overlaps (label crowding, arrow ends, ring touching the box); the Q7 ring and the vertical arrows were moved after that look.

### Chunk C notes (from the decision agent)
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

### Chunk D notes (from the decision agent)
# Notes, chunk D (Class 8 Ch 5 "Number Play", live plan cbse_eng_maths8_ch5_v36)

Chunk D = M2.S26.T26, M2.S27.T27, M2.S28.T28, M2.S29.T29, M3.S31.T31, M3.S32.T32, M3.S33.T33.
Result: 33 items (15 question, 15 solution, 3 worked example): **required 0 / optional 1 / none 32**. Validator: errors 0, warnings 0.
No new media id is created and no LP id is dropped (`new_media_ids_created` and `lp_ids_dropped` are empty).

Why nothing is required: this chunk is the divisibility-puzzle part of the chapter (Figure it Out Q5/Q8/Q10, Digital Roots, Digits in Disguise, Q15, Navakankari). The book prints no figure with any question or answer here, except (a) the column-addition layout of the four addition cryptarithms (typeset arithmetic, so LaTeX by the v3 "column addition" rule) and (b) decorative art. Every question states what it gives in words, every answer is numbers or reasoning.

Figures claimed (12, all `none` or a concept image, none maps to an item):
- P19-illustration-1, P30-illustration-2 (Digital Root Club cartoon, page art and its reprint beside the riddle answer): `none:DECORATIVE_ONLY`.
- P20-cryptarithm-1..4 (the four addition cryptarithms given in the question) and P31-cryptarithm-1..4 (the same four reprinted on the answer page, letters not replaced by digits): `none:LATEX_ARITHMETIC`. The P31 reprints are not `SAME_AS_QUESTION_DIAGRAM` because the question side has no diagram either.
- P30-table-1 (printed answer of the "add 11" question: two columns of equations 10 -> 1+0 = 1 ... 120 -> 3): `none:LATEX_ARITHMETIC`.
- P24-board-1 (Navakankari board with 9 + 9 pawns): `concept_image:M3.S33.T33.C152.IMG1` (accounting only, the board-and-goal teaching image already in the plan).
- Not claimed on purpose: P23-venn-1..4 and P37-venn-1..4 belong to Figure it Out Q16 (FiO4.q16 = M1.S12.T12.C44, another chunk). P17/P18/P29 (shortcut for 11, divisibility table) belong to the 5.2 shortcut topics (another chunk). Cartoon characters (Guna, Anshu, the owl and the children on the Puzzle Time page) are pure decoration (Step 0 skips them), so no `NEW-` figure was added.

All base descriptions of the figures above were checked against the page pictures (pp.19, 20, 24, 30, 31); they are right. Only the P19 picture got extra words in its inventory description (see "Book unclear").

## 1. Judgement calls

- **Addition cryptarithms C139/C140 (book p.20 (i)-(iv), reprinted p.31):** question `none` (LATEX_ARITHMETIC, TEXT_SUFFICIENT). The LP question already writes each puzzle as an equation, and the v3 prompt sends column addition to LaTeX. Solution `none`: the printed answer is only text ("A = 7, B = 9" ...) and the LP answer is solved sums written in LaTeX. `text_alternative` on both tells the text side to use a LaTeX array column addition.
- **Multiplication cryptarithms C141-C150:** all `none`, one-line equations, no figure in the book. Same decision for every one of them (sibling consistency inside Digits in Disguise and FiO Q15).
- **C129 solution (FiO3.q2, "add 11"):** the book's printed answer sits in two columns under a vertical rule, which looks like a table picture, but it is plain equations (10 -> 1+0 = 1 ...). Judged text/LaTeX. The LP answer uses a different start (5, 16, 27, 38, 49, 60 instead of 10, 21, 32 ...); the LP wins and is right (roots 5, 7, 9, 2, 4, 6).
- **C117 and C119 (worked examples):** `none`. Number chains and two plain sequences; the teaching images of both concepts (reduction chain, 7-4-1 ring) stay as they are and are never linked.
- **C122/C123 (600 to 700):** `none` on both sides. The solution is three lists of eleven numbers; a number line would only repeat what the list says, and the root-5 "+9" picture already exists as a teaching image (M2.S27.T27.C118.IMG1).
- **C124/C125 (riddle):** `none`. The Digital Root Club cartoon beside the riddle is decorative; the answer is one number.
- **Open questions (C113, C115, C128, C132):** question side `none` (OPEN_ENDED, TEXT_SUFFICIENT); the solutions draw nothing because there is no figure to give.
- **Book numbering vs LP numbering:** the LP calls M2.S26.T26's questions "Figure it Out, Q1-Q3", M2.S29.T29's "Q1-Q3" and M3.S32.T32's "Q1", while the book numbers are 5.3 FiO Q5, Q8, Q10; digital-root FiO Q2, Q3, Q4; 5.3 FiO Q15. I matched items to the book by their text, not by the LP number.

## Borderline

1. **C139 / C140** (addition cryptarithms in the book's column layout): none, but a reviewer could argue ANSWER_IS_FIGURE (a solved column addition). I applied the v3 rule as written (column addition is LaTeX). If the user wants pictures here, it is four question figures (one per puzzle) plus solved columns, which also would hit C148.
2. **C148** (six solved multiplications): none, same reasoning.
3. **C152 Navakankari worked example:** `optional` rather than `none`. A small picture (three connected board points on one line, two partner pawns on the first two, the third empty, my blocking pawn in ANSWER green) would clearly help, but the scenario is stated fully in words and the answer is one move, so by the tie-breaker the text is enough. Not added.
4. **C129 solution:** the printed answer looks like a two-column table (see above); judged text.
5. **C117, C119, C122/C123, C125, C127:** a teaching picture exists for each concept, which is never linked. Their decision does not rest on that; each is text/LaTeX because the content is plain numbers.

## 2. LP text issues

No LP text was edited. Each item below: concept id, what is wrong or missing, suggested sentence.

- **M2.S26.T26.C112** (steps_tex step 4, answer_tex, text): the LaTeX is cut in the middle of each pair, so it will render oddly: `gives $(1$, $0)$`, `($a$, $b) = (1$, $0)$, $(2$, $8)$ ...`. Suggested: "$a + b = 1$ with $b$ even gives $(a, b) = (1, 0)$; $a + b = 10$ with $b$ even gives $(2, 8)$, $(4, 6)$, $(6, 4)$, $(8, 2)$." and answer "$(a, b) = (1, 0), (2, 8), (4, 6), (6, 4), (8, 2)$".
- **M3.S31.T31.C139** (question_tex): `$A_1 + 1B = B_0$` writes the digits as subscripts (A with a small 1), which reads like indexed variables, not the two-digit numbers A1, 1B, B0. Suggested: "Solve the cryptarithm $A1 + 1B = B0$ (each of A1, 1B and B0 is a 2-digit number)." Same slip in **M3.S31.T31.C147** (`$L_2N \times 2 = 2NP$`, should be `$L2N \times 2 = 2NP$`, three digits L, 2, N) and in **M3.S32.T32.C150** step 4 (`$5O_5 \times 5$`, should be `$5O5 \times 5$`).
- **M3.S32.T32.C150** (step 3): the math is split by the bracket: `so $W$ is $5 (W$ cannot be $0$ as a first digit).` Suggested: "so $W$ is $5$ ($W$ cannot be $0$ as a first digit)."
- **M3.S31.T31.C139 / C140** (second block): the LP labels the other three puzzles (i), (ii), (iii) (AB + 37 = 6A, ON + ON + ON = PO, QR + QR + QR = PRR); in the book they are (ii), (iii), (iv) because A1 + 1B = B0 is (i). Suggested: relabel them (ii), (iii), (iv) in the question and in the answer lines.
- **M2.S28.T28.C124 / C125** (riddle, missing data): the book asks "What's my number? What's my name?" and its answer gives both the number and its name in the Indian system ("11,11,11,111, Eleven crore eleven lakh eleven thousand one hundred eleven"). The LP question stops at "solve the riddle" and the answer gives only 111111111. Suggested: add "What is the number, and how do we read it?" to the question, and to the answer "$111111111$, read as eleven crore eleven lakh eleven thousand one hundred eleven ($11,11,11,111$)".
- **M2.S29.T29.C133** (step 1, weak example): 10 (even, root 1), 11 (odd, root 2), 12 (even, root 3) all show the parity of the root flipping, which does not show "no fixed link". Suggested: "$10$ and $20$ are both even, but their digital roots are $1$ (odd) and $2$ (even); so the parity of a number does not decide the parity of its digital root."
- **M3.S31.T31.C148** (missing eliminations): (v) lists P = 2, 3, 4 with Q = 1 but never says why P = 1 and P = 5 to 8 are out. Suggested: "$P = 1$ would make $P$ and $Q$ the same digit, and $P = 5, 6, 7, 8$ give $605, 726, 847, 968$, whose first digit is not $P$." In (i), after "$T = 0$" add "$3 \times U$ must end in $U$, so $U = 5$ (since $U \ne T$)".
- **M3.S31.T31.C146** (steps 3 and 4): $6 \times E$ ending in $Y$ also allows $E = Y$ ($E = 0$ for $Y = 0$, $E = 2$ for $Y = 2$, $E = 4$ for $Y = 4$); the LP names only $E = 5$, $7$, $9$ for those. Suggested: add "(the other choice $E = Y$ would use one digit for two letters)".
- **Labels:** "Figure it out: Q1" is the name of three different concepts (M2.S26.T26.C111, M2.S29.T29.C128, M3.S32.T32.C149), and M2.S28.T28.C126 is named "Digital Roots: Q3" while its `book_number` is "Digital Roots, Q1". The text of each question is right; only the labels collide. Suggested: use the book's own numbers (5.3 FiO Q5, Q8, Q10, Q15; digital-root FiO Q1 to Q4).
- **M3.S33.T33.C152** (worked example): "your partner completes a line of three next turn" is a placing-phase situation, while the book's rules (p.24, rule 2) describe lines being made by moving pawns after all are placed (rule 1 only talks about placing). The LP answer is consistent with rule 3 (a completed line removes a pawn). Suggested: begin the question with "While you are still placing pawns, ..." if the content team wants it to follow the standard game; otherwise leave as is.

## 3. Places where the book itself is unclear

- The brief says the pdf has no printed-solutions section, but pdf pages 25 to 37 are printed answers ("Page No. 122" onward). I used them only to cross-check the LP answers; the LP text was followed throughout.
- **Digital Root Club picture (p.19, reprinted p.30):** the members' numbers are 10000000, 100, 10584, 37, 1000, 1 and the people kept out are 1001 and 110. If the club is "digital root 1", then 10584 (digit sum 18, root 9) does not belong, so the art is inconsistent. It is decorative and no item uses it, so nothing changes. The exact number of zeros in 10000000 (about seven) is also unclear.
- **Printed answers with fewer solutions than the LP** (the LP is mathematically right and wins): ON + ON + ON = PO has three solutions (17, 24, 31 giving 51, 72, 93), the book prints one (N = 1, O = 3, P = 9); L2N x 2 = 2NP has 124 x 2 = 248 and 125 x 2 = 250, the book prints one (L = 1, N = 5, P = 0); PP x QQ = PRP has 22 x 11 = 242, 33 x 11 = 363, 44 x 11 = 484, the book prints P = 2, Q = 1, R = 4 only. I recomputed every solved sum of C140, C142, C144, C146, C148 and C150 and all hold.
- Print slips in the answers: "hudred" for "hundred" (riddle answer, p.30). The book's example 40000001 (FiO Q1, digital roots) is a valid 8-digit number with root 5; the LP uses 10000004, also valid.
- All figures in this chunk are text-based or decorative, so no book picture needed a corrected value (user decision 1 never applied).
