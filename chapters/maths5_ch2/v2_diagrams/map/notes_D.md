# Notes, chunk D (Class 5 Ch 2 Fractions): M3.S24.T24, M3.S25.T25, M3.S26.T26, M3.S27.T27

Result: 15 items, required 3 / optional 2 / none 10. Validator `--chunk D`: errors 0, 1 warning (C110 is required but the book prints no figure for it; expected).

| Item | Decision | Why in one line |
|---|---|---|
| C95 Ex 8 question | none (TEXT_SUFFICIENT) | amounts given as numbers; the book's paratha pictures sit beside the answer bubble |
| C96 Ex 8 solution | **required** `M3.S24.T24.C96.IMG1` | printed answer is the paratha picture: 7/8 (7 of 8 pieces) and 8/6 (one whole + 2 pieces) |
| C97 Ex 9 question | none (TEXT_SUFFICIENT) | same as Ex 8 |
| C98 Ex 9 solution | **required** `M3.S24.T24.C98.IMG1` | printed answer is the paratha picture: 5/8 past the half line, 3/6 exactly half |
| C99 / C100 Let us do (reference to 1) | none / none | no figure in the book; six pairs and six signs in text |
| C101 equal-to-1/2 box | none (NUMBER_LIST_IN_BOXES) | scattered list of fractions, all in the question text |
| C102 solution | optional (not added) | circled box would help; LP answer lists all six fractions |
| C103 less-than-half box | none (NUMBER_LIST_IN_BOXES) | same |
| C104 solution | optional (not added) | same; five fractions listed |
| C105 / C106 table of pairs | none / none (LATEX_TABLE) | plain 2 x 4 table; the signed table is a LaTeX array |
| C107 worked example (relations) | none (TEXT_SUFFICIENT) | plain three-link chain, no figure in the book |
| C109 relations question | none (TEXT_SUFFICIENT) | no figure printed or given |
| C110 relations solution | **required** `M3.S27.T27.C110.IMG1` | family tree: the only brother of father's sister is the father |

## 1. Judgement calls

1. **Example 8 and Example 9 (C95/C96, C97/C98): question none, solution required.** The book prints the paratha pictures right next to the answer bubble ("7/8 is less than 1 and 8/6 is more than 1", "3/6 is half. But 5/8 is more than 1/2"). The speech bubbles (the question) give the amounts as numbers, so the pictures are the printed answer, not a given figure. Solution = the book picture (B2: printed answer is a picture); question has no given figure so none (companion note: no invented question figure). The LP hint `s_figure` for Ex 8 (a number line with a dot each side of 1) was not followed: the LP steps speak of pieces and parathas ("7 pieces of 1/8", "8 pieces of 1/6 make 1 paratha", "1 whole paratha and 2 more pieces"), which is the book picture; the number line already exists as the teaching image M3.S23.T23.C91.IMG1 (never linked).
   - Added to the solution figure: the tags `less than 1` / `more than 1` (Ex 8) and `more than 1/2` / `exactly half` (Ex 9) in ANSWER green, each 3 words or fewer and taken from the LP steps; plus the vertical FOCUS half line through both circles in Ex 9 (LP `s_figure`: "a line across each one at half"). Labels `1/8` and `1/6` are drawn upright, the book rotates them.
   - One diagram draws both book pictures of each example (P13-fraction_model-1 and -2 to C96; P14-fraction_model-3 and -4 to C98).
2. **Boxes of loose fractions to circle (C101/C102, C103/C104).** The book question is "circle the fractions...", a selection from a box with no order or position meaning: Step C `NUMBER_LIST_IN_BOXES`. I read the code's last sentence by analogy: the marks (circles) only become a diagram on the solution side and then only `optional` because the LP answer lists every chosen fraction. So question none, solution optional (not added). See Borderline.
3. **Table of pairs (C105/C106).** Plain table, no colour, no headings: `LATEX_TABLE` on both sides. The solution's "same table with a sign in every pair" is a LaTeX array; the `text_alternative` of C106 gives the filled array (all eight signs checked: 2/9 < 4/7, 11/14 > 7/20, 5/7 > 3/9, 6/7 > 4/10, 9/17 > 3/15, 7/12 > 3/11, 1/3 < 5/9, 3/9 < 4/7).
4. **Relations (C107, C109, C110).** The puzzle "only brother of your father's sister" has a trick (the only brother is the father himself). A family tree changes how correctly the learner follows it (tie-breaker, second clause), so the solution is `required`: tree = Father's sister, Your father (joined by a sibling bracket and a FOCUS arrow "her only brother"), and under him two children "You" and "Brother or sister" (ANSWER). The box "You" is my addition so that "brother or sister of yours" can be read; the LP hint `s_figure` only had the father, his sister and his child. The question has no given figure (book page 15 prints only the sentence), so no question diagram. The worked example C107 (mother's only sister's daughter) is a plain three-link chain with no trick, no figure in the book: none. This is NOT because the concept already has a teaching image (C107.IMG1 stays untouched and is never linked): the rule-based need is just lower than for C110.
5. **Figures not claimed here.** `P13-fraction_model-3` and `-4` (circles 4/8 = 1/2 and 3/6 = 1/2) sit in the book section "Comparing Fractions with Reference to 1/2" but are the teaching pictures of unit 49 (`rh.pictures`, M3.S23.T23, chunk C); `P12-number_box-4` is Let Us Do Q2 on p.12 (M2.S21.T21, chunk C) and `P15-number_line-2` is Try This (M2.S22.T22, chunk C). If chunk C leaves P13-fraction_model-3/-4 unclaimed, the merge must assign them (they are teaching figures; none of my items needs them).
6. **Base inventory check.** I compared every claimed figure with the page pictures (zoomed crops of p.13 and p.14): all seven descriptions are correct (7 labelled eighths with the lower-left sector dashed; 6 + 2 sixths; 5 eighths clockwise from the top radius to the lower-left diagonal; 3 right sixths = exact half; the box and table contents). No `CORRECTED:` entries.

## 2. LP text issues

(No LP text was edited and no decision changed because of these.)

- **M3.S24.T24.C95 and C97 (question text):** the question names "Sevi and Shami" but then says "One child says ... The other says ...", so the learner cannot tell who ate which amount. Suggested: "Sevi says: I ate 7/8 paratha yesterday evening. Shami says: I ate 8/6 paratha yesterday evening." (and for C97: "Sevi says: I ate 5/8 paratha ... Shami says: I ate 3/6 paratha ..."; in the book the girl on the left holds the first amount and the boy on the right the second, but the pictures do not name them).
- **M3.S24.T24.C96 and C98 (solution text):** no sentence refers to the picture that now opens the solution. Suggested first line for C96: "Look at the picture: 7 of the 8 pieces of one paratha, and one whole paratha cut into 6 plus 2 more pieces of the other." For C98: "Look at the picture: the half line cuts the paratha cut into 6 exactly in half; the paratha cut into 8 has 4 pieces on one side of the line and 1 more piece past it."
- **M3.S27.T27.C110 (solution text):** the tree includes a box "You"; step 4 could say "a child of your father is another child in your family: your brother or sister" so that the box makes sense (the answer text "brother or sister" is unchanged).
- **M3.S25.T25 (question names and book numbers):** the concept names run Q2, Q3, Q4 (counting from the "reference to 1" set) while `book_number` says "Let Us Do (reference to 1/2), Q1 / Q2 / Q3" (the book numbers them 1, 2, 3 within that set). Not wrong, but the two numberings differ.
- **Order:** in the book the two box questions (circle equal to 1/2, circle less than half) come BEFORE Example 9 ("Now let us compare fractions using 1/2"); the LP puts Example 9 (topic T24) before them (topic T25). Teaching order is fine in the LP; just not the book's order.

## 3. Borderline

- **C102 and C104 (circled boxes): optional vs required.** Argument for required: ACTION_ON_FIGURE / HIGHLIGHT_MEANING (the answer is the circles on a given box) and the LP's own `s_figure` wanted "the same box with the fractions circled". Argument for none/optional (chosen): the box is a NUMBER_LIST_IN_BOXES and the Step C text says circles only become optional on the solution side when the text already gives the answer; the LP answer lists all chosen fractions, so by the tie-breaker the text alone is exact. If the user prefers the picture, the spec would be: a rounded box with the 10 (or 12) fractions at the book's positions, the six (or five) answers circled in FOCUS. Chunk C's "circle the fractions greater than one" box (p.12) should get the same decision for consistency.
- **C95 and C97 (question side).** The paratha pictures could be read as a given figure of the question; I read them as the printed answer (they sit with the answer bubble) because the amounts are given as numbers. If read the other way, both questions become required and the two solution diagrams would derive from them.
- **C107 worked example (none) against C110 solution (required).** See judgement call 4.
- **C99/C100 (reference to 1).** A number line placing the twelve fractions around 1 would be optional only; text is exact, so none.

## 4. Where the book is unclear

- Fun with Relations (p.15): the book prints no answer. The LP says "brother or sister"; strictly the child of your father may also be you yourself if you are an only child, but "brother or sister" is the usual answer and was kept.
- Book Example 8 and Example 9 bubbles name no children; the names Sevi and Shami appear only in the surrounding text of the section.
- No print slips were found in the figures or printed answers of this chunk, so no book value was corrected.
