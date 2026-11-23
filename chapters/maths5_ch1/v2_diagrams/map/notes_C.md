# Notes for chunk C (Class 5 Ch 1, topics T18 to T25)

Result: 29 items = required 6 / optional 2 / none 21. Question: 3 required, 8 none. Solution: 3 required, 2 optional, 6 none. Worked example: 7 none. Validator: errors 0, warnings 0. Output: `map/out_C.json`.

The only drawn figures are the three rabbit roads of the book (tens p.7, hundreds p.8, thousands p.8), each as a question road (C75, C77, C79) and a solution road with jump arrows (C76, C78, C80).

## 1. Judgement calls

- **C75, C77, C79 (rabbit questions) question = required.** The book hands these over as pictures ("Its location is given in the pictures below"): the carrots, the halfway tick (2,345 / 2,350 / 2,500) and the rabbit's exact spot live in the road figure. The LP question text repeats the two end numbers, but under the user's rule 4 I did not flip them to none for that. Positions are drawn to scale (checked on the page pictures: 2,346 at 60% / 46% / 34.6% of the road, the halfway tick at 50%).
- **Rabbit pose.** In the book the rabbit is drawn mid-jump facing the nearer carrot (right on p.7, left on both p.8 roads). A question figure must not give the answer, so the question figures draw it standing and facing front with no motion lines. The solution figure keeps the same rabbit and adds the arrows. The rabbit and the carrots are plain flat icons without faces: they are the question's own objects (the rabbit's position is the data). If you want an even plainer figure (a dot instead of a rabbit), that is a one-line change in the three question specs and the three derived solution specs.
- **C76, C78, C80 (rabbit solutions) = required.** The LP solution compares both jump counts (4 and 6; 46 and 54; 346 and 654). The figure adds new marks (two jump arrows with counts, a ring round the nearest carrot, the tag "nearest ten / hundred / thousand"), which is the "solution adds something visual: new marks, a highlighted part" case of Step E. All three have `derived_from` their question figure; the tags use only words the LP solution uses ("jumps", "nearest ten").
- **C71, C72, C73 (T18 worked examples) = none.** Their questions name no figure and give every number in words (4,190 / 4,200 and 3 / 7 jumps; 6,700 / 6,800 / 6,000 / 7,000; the two sample pairs), and each concept already carries a teaching image of the same road (not linked). A text-complete worked example gets no diagram of its own (no repetition). Same logic for C89, C90, C91 and C99.
- **C81 / C82 (the table) = none, LATEX_TABLE both sides.** Plain four-column table of numbers with no colour or position meaning; the filled answer is the same table with 12 numbers. B2 lists "filled table" under ANSWER_IS_FIGURE, but the explicit rule for plain tables ("Plain tables of numbers ... stay LaTeX") is more specific, so I followed it. See Borderline.
- **C83 question none / C84 solution optional.** The four numbers of Let Us Think Q1 are a plain list to choose from (NUMBER_LIST_IN_BOXES). The rule says the circles in the answer only make an optional figure when the text already gives the answer, and the LP answer names 7,030 and 6,999. Optional, so no image is added.
- **C85/C86 and C87/C88 (Let Us Think Q2, Q3) = none.** Open "think and write" tasks; the LP sample answers are pairs of numbers fully stated in the steps. Number lines would be nicer, but they are not needed (Q2 would need three scales). Q2 and Q3 have the same decision as each other. Q1's solution is optional because its answer is a selection from a printed list, a different kind of answer.
- **C93 to C102 (Let Us Do vehicles, books).** The book prints no figure for the cyclist, the school-bus question or the 200-page book (page 10 is text only). So the three question sides are none and no question figure is invented, although the LP hint `q_figure` describes one. Solutions: C94 (cyclist) optional (a 0 to 60 km line with four 15 km hops would help but the sum is already complete), C96 / C98 / C102 none (division and multiplication; 450 groups of 2 cannot be drawn faithfully).
- **Figure inventory.** Base figures P07-number_line-3, P08-number_line-1, P08-number_line-2 are the question figures of C75, C77, C79. For each solution figure I added `NEW-<base id>-sol` (second use of the same road). P08-table-3 is `none:LATEX_TABLE`; P08-number_list-4 is `none:NUMBER_LIST_IN_BOXES`. I added `NEW-P09-vehicles-1` (the page-9 collage of eight vehicles, missing from the base because it is decoration) mapped to the teaching image `M3.S22.T22.C89.IMG1`, which shows the same eight modes. I checked the base descriptions of the five base figures against the page pictures: all correct.

## 2. LP text issues

(Nothing was edited and no decision was changed because of these.)

- **M2.S20.T20.C81**: the question text says "Fill in the boxes appropriately" but carries no table, so there are no boxes to fill. Suggested: add a LaTeX array to the question text, header `Number | Nearest Tens | Nearest Hundreds | Nearest Thousands`, rows 3,176; 4,017; 5,789; 8,203, three blank cells each.
- **M2.S20.T20.C82**: the answer is one run of text (12 numbers). Suggested: show it as the same LaTeX array filled in (3,176: 3,180 / 3,200 / 3,000; 4,017: 4,020 / 4,000 / 4,000; 5,789: 5,790 / 5,800 / 6,000; 8,203: 8,200 / 8,200 / 8,000).
- **M2.S19.T19.C75, M2.S20.T20.C77, M2.S20.T20.C79**: the question text never points at the road figure that is now added. Suggested closing sentence: "Look at the road in the picture: the rabbit and the two carrots." (The figure also shows the halfway tick, which the text does not mention.)
- **M3.S23.T23.C93, C95, C97 and M3.S25.T25.C101** carry `q_figure` hints (a road with four stretches, a school group beside four vehicles, an open book with labels) and C94 / C96 / C98 / C102 carry `s_figure` hints that are not figures of the book. Not used.
- **M3.S23.T23.C97** is named "Let us do: Q3" in the LP but is part (e) to (h) of the book's Let Us Do Q2 (book_number is right). Cosmetic.
- **M2.S21.T21.C88 (b)**: "7,970 is 70 jumps from 7,900" states the distance to the farther neighbour (7,970 is only 30 jumps from 8,000); the conclusion (nearest hundred 8,000) is right. Suggested: add "and 30 jumps from 8,000" for clarity.
- All sums, counts and answers of the 29 items were recomputed (4,197, 6,731, 5,380 / 5,420, 7,997 / 8,002; 46 / 54; 346 / 654; the 12-cell table; 7,126 / 7,835 / 7,030 / 6,999; the sample pairs of Q2 and Q3; 15 x 4; 461 + 439 = 900 and the eight divisions; 120 / 4 and 120 / 6; 100 x 40; 200 x 50): no arithmetic mistake found. No book print slip was found in this chunk, so nothing had to be corrected in a spec.

## 3. Where the book is unclear

- The book prints no solutions section; the printed text under the Example 1 picture (p.7) gives "2,350 ... 4 jumps" and the two p.8 rabbit items are blanks only. The LP solution (46 / 54 and 346 / 654) is mathematically right and is followed.
- The p.8 hundreds picture puts the 2,346 label higher than the others because 2,346 and 2,350 are only 4 units (58 px at this scale) apart; the spec keeps that staggered layout.
- Page 10 prints the speed list and the vehicle seat list as plain text; there is no figure, so the concept images of T22 and T24 are accounted for as teaching images only.

## Borderline

- **C76 / C78 / C80 solutions required**: the answer is words and numbers, but the jump arrows with the ring are exactly the added visual of Step E. Typical-pair table (Step E) would also allow "Q required, S none". I chose required because the arrows are what "jumps" means in the book and the LP solution is built on them.
- **C71 / C72 / C73 worked examples none**: the same rabbit scene is a required figure in T19 / T20, but there the book gives it as the question; here the LP wrote the examples in words and each concept already has its teaching image. Could be flipped if the content team wants a figure on every rabbit example.
- **C81 / C82 table none**: the "filled table" wording of ANSWER_IS_FIGURE versus the plain-table rule.
- **C84 optional, C94 optional, C86 / C88 none**: the picture would help a little in each, none is needed.
- **Rabbit and carrot icons** in a diagram image (the "no clip-art" rule): kept as plain flat icons because they are the objects of the question; the must_not_show list says so.
