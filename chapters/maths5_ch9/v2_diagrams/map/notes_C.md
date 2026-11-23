# Notes, chunk C (Class 5 Ch 9 "Coconut Farm", topics T16 to T22)

Result: 30 items, required 0 / optional 2 / none 28. Validator: errors 0, warnings 0.

## 1. Judgement calls

- **Long division is LaTeX arithmetic.** Every picture in this chunk is a long-division layout (Susie's partial quotients, Sunitha's layout, the partly blank frames) or a column-multiplication frame. Step C lists "long division" under `LATEX_ARITHMETIC`, and the 23 Nov brief says text and LaTeX are the default. The same call was made in Class 5 Ch 4 (column addition and subtraction) and Class 7 Ch 12 (long division). Each `none` item carries a `text_alternative` that says which LaTeX array to write.
- **No question in the chunk gives a figure the text does not carry.** Example 5 to 9 and the oil/husk/tender questions are word problems with all numbers in the text. The book layouts printed under them are the book's solutions. The Let Us Learn to Divide frames (726 / 4, 902 / 16) and the tender-coconut frame (8890 / 35) are restated blank by blank in the LP question text.
- **Solutions.** The pdf has no printed-solutions section. The "printed answer" is the layout printed under each example. Because it is long division, not a picture in the sense of Step B2 (stick-figure line-ups, coloured tables, number lines), I did not apply "printed answer is a picture". No solution adds anything visual that the LP steps lack.
- **Figure claims.** I claimed the 10 base figures of pages 6 to 9 (all `none:LATEX_ARITHMETIC`) and added `NEW-P07-formula_box-1` (the boxed N = D x Q + R, `none:TEXT_SUFFICIENT`). I did not claim P10-*, P11-*, P12-*, P13-* (pages 10 to 13). They are the book's pictures for the examples 62 / 5, 75 / 8, 324 / 3, 136 / 6 and the Let Us Divide frames, which belong to chunk D's units (T23 to T25). My T22 worked examples (C93, C94, C95) use practice values (83 / 6, 412 / 4, 3,648 / 12) and none of those pictures. If the merge wants them claimed here too, the same `none` or item meaning as chunk D's applies.
- **P09-column_multiplication-1** is mapped `none:LATEX_ARITHMETIC` (the H T O heading alone would be `HEADER_BOXES_ONLY`, also true, both are in the item's reason codes).
- **Base descriptions checked against the page pictures** (pp. 6, 7, 8, 9, 10, 11, 14): all ten base entries I claimed are correct (digits, counts of subtractions, coloured digit cells, blank positions). No "CORRECTED:" needed. Page 14 has no picture for Q4 (remainders, C79/C80).

## Borderline

- **C66, C70, C84, C86 (solutions with a printed layout).** Kept `none`. The coloured digit cells above the quotient (9|7, 2|1, 5|4|7, 4|3|1) only mirror the digits of the quotient. A side-by-side drawing of Susie's and Sunitha's layouts would compare the number of steps (6 against 2, 5 against 3), but the LP steps already say it in words ("Sunitha's way takes 2 steps and Susie's way takes 6 steps"). If the user wants a picture here, these four are the first to flip to `required` (type `other`, long-division layout, derived from nothing because the question side has no figure).
- **C71, C73, C89 (question side, partly blank frames).** Kept `none`: ACTION_ON_FIGURE could be argued (the student completes a frame), but the LP question text lists each blank, so the tie-breaker says the text is enough. The completed solution frames (C72, C74, C90) follow the question side (`none`).
- **C87 (blank column-multiplication frame).** Kept `none` (LaTeX array with H T O headings).
- **C93 and C94 (worked examples, `optional`).** Base-ten blocks sharing 83 on 6 plates and 412 on 4 plates would clearly help but are not needed to follow the steps. I decided this on the tie-breaker and the absence of a v3 trigger, not because the same figures already exist as kept teaching images C93.IMG1 and C94.IMG1 (user decision 5). If the user wants an own diagram for each worked example, flip both to `required`, `add_new_image`, `question_tex / after_question_text`, ids `M3.S22.T22.C93.IMG2` and `M3.S22.T22.C94.IMG2`; they would be copies of the two teaching images in content.
- **C81, C95 (worked examples with practice values).** `none` (take-away lines and two-way comparison are arithmetic). C95 has no teaching image.

## 2. LP text issues

- **M2.S16.T16.C66, C70; M2.S20.T20.C84, C86; M2.S21.T21.C90** (field `text`): stale `[Image: ... solution]` and `[Image: ... solution (continued)]` markers sit inside the step text (after step 4 in C66, for example). The old cards are dropped, and nothing replaces them (all `none`), so the builder must strip these markers.
- **M2.S21.T21.C90** (answer): the blanks are listed as "200, 1750, 140 and 4", but the question's blanks come in the order: quotient parts (200 and 4), then 1750, then 140, then the total. Suggested sentence: "The blanks, in order, are $200$, $4$, $1750$ and $140$, and Ibrahim sold $254$ tender coconuts."
- **M2.S21.T21.C91** (question): the number of coconuts is never stated. The question asks for "___ coconuts at ₹20 each" and the solution begins "Ibrahim sold 254 tender coconuts". The number only comes from the previous question. Suggested sentence added to the question: "Ibrahim sold $254$ tender coconuts (from the previous question)."
- **M2.S17.T17.C73** (question): the book frame has one more blank (the remainder 102 under -800) that the LP text does not mention. Not needed to answer; the LP solution gives it ("902 - 800 = 102").
- **M2.S16.T16.C67/C68**: LP is right ("4 bags are needed"); see section 3 for the book's wording.

## 3. Where the book itself is unclear or slips

- Page 6, the bag example: the book ends "So, each person will get 4 bags". It is the number of bags needed, not a quantity per person; the LP already says "4 bags are needed". No figure is involved.
- Page 7, Let Us Learn to Divide, 726 / 4: the frame leaves the first subtrahend (400) and the last subtrahend (4) blank as well as the two quotient parts (80 and 1). The LP question puts all four blanks into words (400, 80, 4, 1), which matches the book frame.
- No arithmetic error or print slip was found in the figures of pages 6 to 9; every layout was recomputed (582 / 6 = 97, 535 / 25 = 21 r 10, 726 / 4 = 181 r 2, 902 / 16 = 56 r 6, 4376 / 8 = 547, 9913 / 23 = 431, 8890 / 35 = 254, 547 x 175 = 95,725).
