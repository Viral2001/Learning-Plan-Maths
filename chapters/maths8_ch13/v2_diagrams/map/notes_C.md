# Chunk C notes: Class 8 Ch 13 "Algebra Play" (units 30 to 42, topics T14 to T17)

Result: required 0 / optional 4 / none 19 (23 items: 10 question, 10 solution, 3 worked example). Validator: errors 0, warnings 0.

I looked at page_10 to page_13 as pictures. Pages 11, 12, 13 hold no figure that carries data: page 11 is text and algebra only, page 12 has one decorative farm illustration, page 13 has one decorative Karim and genie illustration. The base inventory has no entry from pages 11 to 13 (its last entry is the page 10 comic strip), so none of the inventory agents' `unclear` doubts belong to this chunk. I checked the page 10 comic strip entry (P10-dialogue_strip-3) against the picture: it is correct.

## Why nothing is required

Every item here is a word problem or an algebra argument. The book gives no figure for any question, and no answer in the LP is a picture, arrangement or drawing. None of the Step B triggers applies, and for each item a careful student loses nothing without a picture (tie-breaker). Question sides are all `none` because a question with no given figure gets no question diagram. Worked examples (C84, C85, C86) are `none` for the same reason: their figure would sit after the question text and so could show only what the question gives, which is nothing visual; their teaching images (C84.IMG1, C85.IMG1, C86.IMG1) stay and are never linked.

## 1. Judgement calls

- **C78 question (book Q2, "In the trick given above ...")** : `none`, TEXT_SUFFICIENT. It points at Mukta's comic strip on page 10, but states the change itself (sum instead of difference) and gives three numeric examples. The earlier author's hint (`q_figure`: "Mukta's trick as four speech bubbles") would make the figure a given, but the question can be attempted without it and the strip is a teaching picture of section 6.6 (the base id belongs to the teaching units of that section). I recorded this second use as `NEW-P10-dialogue_strip-3-C78` (none, TEXT_SUFFICIENT) so that it is accounted for whatever the chunk that holds the base id decides. If the user wants the trick on screen for this question, it would be a question figure of the four speech bubbles with the steps only (no 47 example, since the question does not give it).
- **C81 solution (cyclic sum 111(a + b + c))** : `optional`. A 3 x 3 cyclic table (rows abc, bca, cab, column totals a + b + c) would show "each digit appears once in every place" at a glance. Step 2 says it in words and the sum is in LaTeX, so it is not needed. Not added.
- **C89 solution (shrines) and C101 solution (Karim)** : both `optional`, same decision on purpose (same structure: double, pay, repeat, with the numeric check 7, 14, 6, 12, 4, 8). A strip of ponds/shrines or of three trips round the tree with the coin counts would help, but the LP solution already gives all the numbers as algebra plus a one-line check. Not added. The book prints no figure for the shrines (C88), so there is no question figure for either.
- **C99 solution (fractions 1/3, 4/12, 9/27)** : `optional`. A 6 x 6 dot square in nested L-shapes (1, 3, 5, 7, 9, 11) would show that 7 + 9 + 11 = 27 is three times 1 + 3 + 5 = 9. The LP gives n x n and 4 x n x n in LaTeX. Not added.
- **C79, C83, C91, C93, C95, C97 solutions** : `none` (LATEX_ARITHMETIC). A picture would be at most decoration for equation solving (hens and horses, ages, cows, dosa profit). C91 (all hens, extra legs) could be drawn but the arithmetic 55 x 2 = 110, 150 - 110 = 40, 40 / 2 = 20 is complete.
- **C90 and C100 questions** : `none`. Their book illustrations (page 12 farm, page 13 Karim and genie) are decorative and carry no data; recorded as `NEW-P12-farm-illustration` and `NEW-P13-karim-genie-banyan` (none, DECORATIVE_ONLY) because the base inventory skipped them.

## Borderline

- C81, C89, C99, C101 solutions: optional rather than none (a figure would clearly make the idea visible; the text is already complete). They cost nothing either way because optional is not added.
- C91 solution: none, although the all-hens argument could be drawn as 55 animals with 2 legs each and 20 horses with 2 extra legs. I judged it plain arithmetic.
- C78 question: none, although the question refers to the trick "given above".
- C85 worked example (double and give 5 away, twice): none, while C89 and C101 (same process) are optional on the solution side. The difference is the side: a worked-example figure goes after the question, where nothing visual is given; a solution figure shows the complete final state.

## 2. LP text issues

- **M3.S14.T14.C78** (question and solution): the card names and `book_number` say "Figure it Out, Q1" but the text is book Q2 (the sum of the number and its reverse). Chunk B's C76 already carries book Q1. The same shift applies to C80 (book Q3, labelled Q2) and C82 (book Q4, labelled Q3). The `ncert_refs` (FiOC.q2, q3, q4) are right. Suggested labels: "Figure it Out, Q2", "Q3", "Q4".
- **M3.S17.T17.C90, C92, C94, C96, C98, C100**: labelled "Figure it Out, Q1" to "Q6" but they are book Q6 to Q11 (`ncert_refs` FiOC.q6 to q11 are right). Suggested labels: "Figure it Out, Q6" to "Q11".
- **M3.S14.T14.C78** question: says "In the trick given above" without stating the trick. Missing data for a standalone card. Suggested sentence to add before the question: "Mukta's trick: choose a 2 digit number with different digits, reverse the digits, find the difference of the two numbers, then divide by 9."
- **M3.S16.T16.C88** `answer_tex`: the closing bracket sits inside the maths: "(or any multiple, like $14$ and $16)$". Suggested: "(or any multiple, like $14$ and $16$)".
- **M3.S17.T17.C94** `question_tex`: the pronoun is typeset as maths: "if $I$ gave you". Suggested plain "if I gave you".
- **M3.S17.T17.C96** `question_tex`: "$I$ run a small dosa cart" and "how many dosas should $I$ aim to sell" have the pronoun as maths; "(i):" and "(ii):" have a stray colon that the plain `question` field does not have. Suggested plain "I", and "(i)", "(ii)".
- **M3.S17.T17.C100/C101**: the LP question does not repeat that the genie asks 8 coins per round until the sentence "gives the genie 8 coins"; this is fine. In part (ii) of the solution, "fewer than 7" holds only for the start of 7 coins, while the question asks in general; the sentence already says "here". No change needed.
- All arithmetic in the LP solutions of this chunk was re-checked and holds: 111 = 3 x 37, 123 + 231 + 312 = 666 = 37 x 18 = 3 x 222; 254254 / 7 = 36322, / 11 = 3302, / 13 = 254; t = 6 (14 bicycles); x = 7 stickers; p = 15; x = 7, k = 8 flowers (7, 14, 6, 12, 4, 8); h = 20 horses, 35 hens; d = 6; g = 6, Naina 12; p = 80 and n = 175; 4/12 and 9/27 are one third; Karim 7 coins, 8x - 7c.

## 3. Where the book is unclear

- Nothing in this chunk's pages is unclear or contradicts the LP. The book's Q5 (shrines) lists only the story; the LP's smallest answer 7 flowers and 8 per shrine is the minimum whole-number solution of 8x = 7k and the LP also states that any multiple works, which is mathematically right.
- The book's picture for Q6 (page 12) shows only a handful of horse heads and two hens, not 55 animals, which confirms it is illustration rather than data.
