# Class 6 Ch 5 Prime Time (cbse_eng_maths6_ch5, live v69): question layout notes

Spec: `layout_spec.json`. Result of `check`: 71 question concepts in 11 Questions topics (43 existing kept in book order
+ 28 new: 6 example, 0 exercise, 22 prompt), 17 live videos kept (every whole-moved concept brings its own, and each
covers its full question), 11 new videos needed (the questions cut out by block), gates identical to live (structure 40,
video_script_rules 97, skeleton 2, before and after), INTEGRITY clean. One Questions topic is new: the one after
M2.S10.T10 "Co-prime Numbers", because section 5.3 has no Figure it Out and the live plan had no Questions topic there.

## How a book question was recognised here

This edition prints a round icon (the same one on every "Figure it Out" heading, checked on PDF pages 1 to 22) in front
of its in-text questions, and its solutions section (pages 23 to 33 of the extract) answers most of them. The in-text
items counted are the icon-marked ones (every item the solutions section lists is one of them or sits right after one),
plus the six printed "Example:" items and the four "A prime puzzle" grids. Every other question in the running text is narration: the book
answers it in the next line or paragraph ("These would be 3, 6, 9", "Other successful jump sizes are 2, 3, 6, 8 and
12"), or it is an open observation. The plan tags all of them as worked examples with ids like 5.1.q6, so the ids say
nothing about whether the book treats the item as a question. The existing Figure it Out concepts (42 printed items plus
puzzle 4) are all listed with `keep`, in book order.

## New questions

`b2` and `b1` are the worked-example blocks cut out of a teaching concept (new video needed). "whole" is a thin-extra
concept moved with its own video.

| # | New question concept | Book label or quote | Plan source (ref) | Tier | Why it counts |
|---|---|---|---|---|---|
| 1 | Idli-Vada: three pairs up to 60 | "Let us now play the 'idli-vada' game with different pairs of numbers: a. 2 and 5, b. 3 and 7, c. 4 and 6 ... Draw a figure similar to Fig. 5.1 if the game is played up to 60." (5.1) | M1.S2.T2.C4 whole (5.1.q4); video kept | prompt | Icon-marked; the figures are fixed (common multiples 10 to 60, 21 and 42, 12 to 60). Has q_figure and s_figure. See judgement call 2. |
| 2 | Idli-Vada: the other number with 4 | "Which of the following could be the other number: 2, 3, 5, 8, 10?" (nobody says just 'vada', one number is 4) | M1.S2.T2.C6 b2 (5.1.q5); new video | prompt | Icon-marked and answered in the book's key (8). See judgement call 3. |
| 3 | Common Multiples: shaded and circled table | "Look at the table below. What do you notice? ... shaded ... circled ... both shaded and circled? What are these numbers called?" | M1.S2.T2.C5 whole (5.1.q9); video kept | prompt | Icon-marked; key: multiples of 3, multiples of 4, 36 48 60, common multiples. Has q_figure and s_figure. Stays in the Multiples Questions topic (it is about common multiples), although the book prints it after the jump section. |
| 4 | Common Factors: jump sizes for 15 and 30 | "What jump size can reach both 15 and 30? There are multiple jump sizes possible. Try to find them all." | M1.S4.T4.C20 whole (5.1.q8); video kept | prompt | Icon-marked; key: 3 or 5, also 1 and 15. Goes before the Figure it Out box 2 items of the Factors topic. |
| 5 | Prime and Composite: primes from 21 to 30 | "How many prime numbers are there from 21 to 30? How many composite numbers are there from 21 to 30?" | M2.S6.T6.C28 b2 (5.2.q3); new video | prompt | Icon-marked; key: 2 (23, 29) and 8. |
| 6 | Co-prime: where to place the treasures | "Where should Grumpy place the treasures so that Jumpy cannot reach both the treasures?" (5.3) | M2.S10.T10.C45 b2 (5.3.q1); new video | prompt | Icon-marked and listed in the key. See judgement call 4. |
| 7 | Co-prime: which pairs are safe | "Check if these pairs are safe: a. 15 and 39 b. 4 and 15 c. 18 and 29 d. 20 and 55" | M2.S10.T10.C47 b2 (5.3.q2); new video | prompt | Listed in the key (4 and 15, 18 and 29); the plan's answer matches. |
| 8 | Example 1: co-prime pairs 15, 39 and 4, 9 | "Example: As 15 and 39 have 3 as a common factor, they are not co-prime. But 4 and 9 are co-prime." | M2.S10.T10.C46 whole (5.3.ex1); video kept | example | Printed Example. |
| 9 | Co-prime: which pairs are co-prime | "Which of the following pairs of numbers are co-prime? a. 18 and 35 b. 15 and 37 c. 30 and 415 d. 17 and 69 e. 81 and 18" | M2.S10.T10.C48 whole (5.3.q3); video kept | prompt | Icon-marked; key: a, b, d, as in the plan. |
| 10 | Co-prime: first common multiple and the product | "While playing the 'idli-vada' game with different number pairs, Anshu observed ... Find examples for each of the above. How is it related to the number pair being co-prime?" | M2.S10.T10.C49 b2 (5.3.q4); new video | prompt | Icon-marked (Math Talk icon beside it); key gives example pairs and the relation. |
| 11 | Prime Factorisation: where Anshu went wrong | "But where did Anshu go wrong?" (56 = 14 x 4 and 63 = 21 x 3 versus 56 = 7 x 8 and 63 = 9 x 7) | M3.S11.T11.C51 b2 (5.4.q1); new video | prompt | Icon-marked; one definite answer (one factor pair does not list all the factors, so the shared 7 was missed). |
| 12 | Example 2: are 40 and 231 co-prime | "Example: Consider 40 and 231 ..." (5.4) | M3.S13.T13.C66 whole (5.4.ex1); video kept | example | Printed Example. |
| 13 | Example 3: are 242 and 195 co-prime | "Example: Consider 242 and 195 ..." | M3.S13.T13.C67 whole (5.4.ex2); video kept | example | Printed Example. |
| 14 | Example 4: is 168 divisible by 12 | "Example: Is 168 divisible by 12?" | M3.S13.T13.C69 whole (5.4.ex3); video kept | example | Printed Example. |
| 15 | Example 5: is 75 divisible by 21 | "Example: Is 75 divisible by 21?" | M3.S13.T13.C70 whole (5.4.ex4); video kept | example | Printed Example. |
| 16 | Example 6: is 42 divisible by 12 | "Example: Is 42 divisible by 12?" | M3.S13.T13.C71 whole (5.4.ex5); video kept | example | Printed Example. |
| 17 | Divisibility by 10: numbers that end in 0 | "Consider this statement: Numbers that are divisible by 10 are those that end with '0'. Do you agree?" with "Can you now answer if 8560 is divisible by 10?" | M4.S15.T15.C79 whole (5.5.q4 folded into 5.5.q5); video kept | prompt | Icon-marked (Math Talk icon beside it); a yes or no with a reason. See judgement call 5. |
| 18 | Divisibility by 5: numbers that end in 0 or 5 | "Consider this statement: Numbers that are divisible by 5 are those that end with either a '0' or a '5'. Do you agree?" | M4.S15.T15.C81 whole (5.5.q8); video kept | prompt | Icon-marked; see judgement call 5. |
| 19 | Divisibility by 2: numbers that end in even digits | "Consider this statement: Numbers that are divisible by 2 are those that end with '0', '2', '4', '6' or '8'. Do you agree?" and "What are all the multiples of 2 between 399 and 411?" | M4.S15.T15.C83 whole (5.5.q13 folded into 5.5.q12); video kept | prompt | Icon-marked; the multiples line follows it with no icon of its own, so the plan's one block keeps both. |
| 20 | Divisibility by 4: multiples near 330, 1730 and 2030 | "Find numbers between 330 and 340 that are divisible by 4. Also find numbers between 1730 and 1740, and 2030 and 2040 ... What do you observe?" | M4.S17.T17.C88 b2 (5.5.q15 folded into 5.5.q16); new video | prompt | Icon-marked; key lists 332 and 336 and so on. The plan block also holds the "make a list of multiples of 4 from 1 to 200" line that comes just before, hence the fold. |
| 21 | Divisibility by 4: is 8536 divisible | "Is 8536 divisible by 4?" | M4.S17.T17.C89 b2 (5.5.q17); new video | prompt | Icon-marked; key: yes, as 36 is divisible by 4. |
| 22 | Divisibility by 4: the last two digits statements | "Consider these statements: 1. Only the last two digits matter ... 2. ... 3. ... Do you agree? Why or why not?" | M4.S17.T17.C90 whole (5.5.q18); video kept | prompt | Icon-marked; key: yes to all three. |
| 23 | Divisibility by 8: multiples near 120, 1120 and 3120 | "Find numbers between 120 and 140 that are divisible by 8. Also find numbers between 1120 and 1140, and 3120 and 3140 ... What do you observe?" | M4.S19.T19.C95 b2 (5.5.q20); new video | prompt | Icon-marked; key: 128, 136; 1128, 1136; 3128, 3136. |
| 24 | Divisibility by 8: change the last two digits of 8560 | "Change the last two digits of 8560 so that the resulting number is a multiple of 8." | M4.S19.T19.C96 b2 (5.5.q21); new video | prompt | Icon-marked; key gives 8552. Several answers are possible; the plan gives the book's. |
| 25 | Divisibility by 8: the last three digits statements | "Consider these statements: 1. Only the last three digits matter ... Do you agree? Why or why not?" | M4.S19.T19.C97 whole (5.5.q22); video kept | prompt | Icon-marked; key: yes to all three. |
| 26 | Prime Puzzle: puzzle 1 with rows 105, 20, 30 | "Fill the grid with prime numbers only so that the product of each row is the number to the right of the row and the product of each column is the number below the column." (first grid: 105, 20, 30 and 28, 125, 18) | M4.S22.T22.C105 whole (5.6.q4); video kept | prompt | Puzzle with one definite answer. Has q_figure and s_figure. See judgement call 8. |
| 27 | Prime Puzzle: puzzle 2 with rows 8, 105, 70 | the same rule, second grid (8, 105, 70 and 30, 70, 28) | M4.S22.T22.C106 b1 (5.6.q5); new video | prompt | Same. |
| 28 | Prime Puzzle: puzzle 3 with rows 63, 27, 190 | the same rule, third grid (63, 27, 190 and 45, 42, 171) | M4.S22.T22.C107 whole (5.6.q6); video kept | prompt | Same. The fourth grid is the kept concept M4.S23.T23.C109. |

Placement. In each Questions topic the new items sit where the book prints them. In the Multiples topic that is after
Figure it Out box 1 (it is printed on page 108, before the pairs game and the "other number" item) and before box 2.
Everywhere else the in-text items and examples come before the Figure it Out items of the section. The 5.5 Figure it
Out is split by the live plan across three Questions topics (after 10, 5 and 2; after 4; after 8); the in-text items go
in the topic of the divisibility rule they belong to.

## Borderline, not moved

All of these have a plan block that stays inside its teaching concept (or its thin-extra concept stays where it is). None
has the round icon and none is answered in the book's solutions section, except where noted.

- 5.1.q1, 5.1.q2 (C2 b2) "For which numbers should the players say 'idli' ... 'vada'?": the book answers it in the next line.
- 5.1.q3 (C3 b2) "Find out other such numbers that are multiples of both 3 and 5. These numbers are called ____": a blank to fill, but no icon, no key entry, and it is the book's own definition of common multiples. See judgement call 1.
- 5.1.q6 (C18 b2) "Which jump sizes will get Jumpy to land on 24?" and 5.1.q7 (C19 b2) "What jump size should he have chosen?" (14 and 36): the book works both out in the text.
- 5.2.q1 (C26 b2) "How many arrangements are possible?", 5.2.q2 (C27 b2) "How are the rows and columns related to 12?": narration.
- 5.2.q4 (C33 b2) the Sieve steps, 5.2.q5 (C34 b2) "Think how this method works": an activity and a discussion.
- 5.3 thread art "Observe the following thread art ... share and discuss" (icon, Math Talk): discussion, and the plan has no block for it (see Gaps).
- 5.4.q2 (C52 whole) "Try another example: 80 and 63 ... Can we conclude?" : the book answers "we cannot conclude that" straight away.
- 5.4.q3, q4, q5 (C53 b2, C54, C55) "Are they different?" for 3 x 3 x 7, the four trees of 36, "can you explain why 30 = 2 x 3 x 5": answered in the following lines; no icon.
- 5.4.q6, q7, q8 (C56 b2, C57, C58) the 72 = 12 x 6 steps, "multiply and check", "observe how many times": narration.
- 5.4.q9 (C65 b2) "Suppose they have a common factor that is composite ...", 5.4.q10 (C68 b2) "How can we check if one number is divisible by another without long division?": lead-ins answered by the next paragraph.
- 5.5.q1 (C77 b2) "Does 8560 have any factors from 2 to 10? Can you find them?", 5.5.q2 and q3 (C78 whole) "Is 125 a multiple of 10 ... Why or why not?", 5.5.q6 and q7 (C80 b2) "largest number less than 399 divisible by 5, is 8560 divisible by 5?", 5.5.q9 to q11 (C82 b2) "Is 682 divisible by 2? Is 8560 divisible by 2? Why or why not?": guided steps inside the narration, each answered in the book's next line. These are the nearest candidates to promote (they have definite answers but no icon).
- 5.5.q14 (C87 b2) "can we check divisibility by 4 from the last digit?", 5.5.q19 (C94 b2) "Can the last two digits be used for 8?": the book answers both immediately ("It does not work!").
- 5.6.q1 (C102 b2) "Which number looks special to you? Why do you say so?" (Math Talk): open, many valid answers. 5.6.q3 (C104 b2) "Think what the rules can be": the rules are printed on the next line.
- Opening "Idli-Vada Game" story, "Jump Jackpot" rules, "Primes through the Ages", the summary: not questions. The worked sample puzzle (75, 42, 102 / 170, 30, 63 with its solution) is a demonstration.

## Gaps (book questions the plan has no question block for)

- "Make such pictures for the following: a. 15 pegs, thread-gap of 10 b. 10 pegs, thread-gap of 7 c. 14 pegs, thread-gap of 6 d. 8 pegs, thread-gap of 3" (p117): a drawing task. The plan only has the recap-and-tool concept M2.S10.T10.C50 (ref 5.3.q5), no block. No icon.
- "Observe the following thread art ... Is it related to the two numbers being co-prime?" (p116, icon, Math Talk): a discussion with an answer in the pictures; C50 carries ref 5.3.q5 but has no question block.
- "Below are some boxes with four numbers in each box. Within each box try to say how each number is special" (p127, icon, Math Talk): open, many answers; M4.S21.T21.C103 is a recap with ref 5.6.q2 and no block.

No counted book question is missing from the plan otherwise. Every Figure it Out item and every printed Example has a concept or block.

## Judgement calls

1. The icon and the key decide which in-text items count (stricter than the brief's "a blank to fill, a find ... put straight to the reader"). The blank in 5.1.q3 is the one place where the brief's wording and this rule disagree; it is left in teaching because the book never answers it separately and the term is defined by the next figure. To count it, add a prompt entry from M1.S2.T2.C3 block 2 (ref 5.1.q3) before "Idli-Vada: three pairs up to 60".
2. Row 1 (the pairs game) has the icon but no key entry. Counted because the task is definite and the plan block holds the three common-multiple sets, and because Figure it Out 4, which asks the same drawing for 60, is a printed question.
3. Row 2: the plan's answer is "2 and 8 (the book names only 8)". 2 also works (idli for multiples of 2, vada for multiples of 4; every multiple of 4 is a multiple of 2), so it does not contradict the book. The parenthesis "(the book names only 8)" must not be printed on the solution card; reword the answer when the solution is authored.
4. Row 6 is icon-marked and in the key, but the book answers it in the next paragraph (12 and 26 fail, 4 and 9 are safe) and its key entry gives an answer only for the "check these pairs" part. Counted as its own question with the plan's answer "two numbers with no common factor other than 1, e.g. 4 and 9". "Check if these pairs are safe" (row 7) is kept separate because it has its own answer. To fold them, list both blocks in one entry and add canon 5.3.q2 to 5.3.q1.
5. Rows 17, 18, 19, 22 and 25 are "Do you agree?" statements, some with the Math Talk icon. They count because the answer is a definite yes with a reason (the key says yes for 4 and 8; the plan says yes for 10, 5 and 2). Rows 17 to 19 are not in the key. Delete those entries to drop them; nothing else changes.
6. `canon` folds three ids into the printed question that carries the icon: 5.5.q4 into 5.5.q5, 5.5.q13 into 5.5.q12, 5.5.q15 into 5.5.q16. Each pair sits in one plan block.
7. The book's "Example:" items are unnumbered and the plan's ids restart in each section (5.3.ex1, 5.4.ex1 to ex5), so the six are numbered 1 to 6 across the chapter in book order.
8. The four prime-puzzle grids have no icon and no key entry, but each has one answer and the live plan already treats puzzle 4 as a question (M4.S23.T23.C109), so puzzles 1 to 3 go before it. I checked each plan solution by multiplying out its rows and columns against the printed clues (all four are correct). C109's name still carries "puzzle 4, p.128" because a kept concept cannot be renamed here.
9. Figures were also added to five kept concepts whose printed question depends on a picture: Figure it Out box 1 Q4 (the two circles), box 2 Q8 (the blank-labelled circles with 72, 48, 24), 5.2 Q2 and Q3 (the Sieve table) and puzzle 4. The two-circle description lists 6 in the left circle although the printed Fig. 5.1 leaves it out (the plan's own answer for that question says 6 belongs there). The other question concepts are text only.
10. `rename_teach` is empty: no teaching concept is named after a moved example. After the cuts, C106 (Solving harder prime grids) keeps only its teaching plan, image and video; the others keep their text, teaching plan and own video.
