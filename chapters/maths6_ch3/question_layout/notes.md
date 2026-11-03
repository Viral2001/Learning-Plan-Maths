# Class 6 Ch 3 Number Play (cbse_eng_maths6_ch3, live v106): question layout notes

Spec: `layout_spec.json`. Result of `check`: 92 question concepts in 14 Questions topics (59 existing kept in book order
+ 33 new: 0 example, 6 exercise, 27 prompt), 33 new videos needed, 0 videos folded, 33 teaching concepts edited, gates
identical to live (structure 1, coverage 17 to 0, video_script_rules 120, skeleton 11, objectives 48), INTEGRITY clean.
Two Questions topics are new (after "Counting with Place Value" and after "Mental Math: Building Numbers"); the other
twelve already exist and all their concepts are listed with `keep`, reordered to the book's order.

## How a book question was recognised here

Class 8 shape: the existing Questions topics hold objective-carrying concepts (all 59 are kept), and every teaching
and practice concept carries an objective and an image, so nothing moves whole; every new question is a block cut out
(`block`), with no video yet. The chapter prints no labelled "Example", so no example-tier question exists. The book
prints the answers of its in-text questions in a solutions section (3.1 to 3.12); that list, plus "is something left
for the reader to do" (a blank, a "find", a "make"), decided the in-text items. Items the book prints already worked
and only asks the reader to observe were left in teaching (see Borderline). The plan's blocks for the moved items use
the book's own numbers; the plan's own teaching examples (new numbers) all stay.

## New questions

Plan source is `concept block` (C<n> is the live concept id inside its topic, b<i> the content block). Every new
question has `keep_video_of: null`. Placement: the in-text items first, then the section's kept Figure it Out items,
except where the book prints them the other way round (Try This in 3.2 after Figure it Out 1 to 10; the 3.8 cards in
their printed order between the kept cards).

| # | New question | Book label or quote | Plan source (ref) | Tier | Why it counts |
|---|---|---|---|---|---|
| 1 | Try This (Supercells in a Grid): complete Table 2 | 3.2 Try This "Complete Table 2 with 5-digit numbers whose digits are 1, 0, 6, 3, 9 ... The biggest number in the table is ___, the smallest even ..., the smallest greater than 50,000 ..., put commas" | M1.S4.T4.C14 b4 (3.2.table2; canon folds table2_biggest, table2_smallest_even, table2_over_50000, commas) | prompt | in the book's solutions; the plan's table, 96,310 / 10,396 / 60,193 match the book's. Four blanks of one printed question folded into one. Has q_figure and s_figure. |
| 2 | Number Line: place nine numbers | 3.3 "Let's see if we can place some numbers in their appropriate positions on the number line" (2180 and 2754 drawn, nine to place) | M1.S6.T6.C26 b6 (3.3.place_numbers) | prompt | in the book's solutions; the plan's order of the eleven numbers matches. Has figures. |
| 3 | Counting Numbers: how many have 1 to 5 digits | 3.4 "Find out how many numbers have two digits, three digits, four digits, and five digits" (table, 9 given) | M2.S8.T8.C34 b6 (3.4.digit_counts) | prompt | in the book's solutions (9, 90, 900, 9000, 90,000). Has figures. |
| 4 | Digit Detectives: counting the digit 7 | 3.4 "Among the numbers 1 to 100, how many times will the digit 7 occur? Among the numbers 1 to 1000 ...?" | M2.S8.T8.C35 b4 (3.4.detective_1000; canon folds detective_100) | prompt | in the book's solutions (20, 300). One printed question with two parts; the block asks 1 to 1000 and its answer line also gives the 20. |
| 5 | Palindromes: all 3-digit ones from 1, 2, 3 | 3.5 "Write all possible 3-digit palindromes using these digits" | M2.S11.T11.C45 b8 (3.5.all_123) | prompt | in the book's solutions; the nine numbers match. |
| 6 | Puzzle Time: the 5-digit palindrome | 3.5 Puzzle time "I am a 5-digit palindrome. I am an odd number. My t digit is double of my u digit. My h digit is double of my t digit. Who am I?" | M2.S11.T11.C50 b2 (3.5.puzzle) | prompt | in the book's solutions (12421, in words). The clues sit in a text block that cannot move, so q_figure carries them. |
| 7 | Kaprekar: the 3-digit routine from 321 | 3.6 "Carry out these same steps with a few 3-digit numbers. What number will start repeating?" | M3.S15.T15.C58 b8 (3.6.three_digit) | prompt | in the book's solutions, which work 321 to 495; the plan's block is the same working. q_figure draws the steps and the question. |
| 8 | Mental Math: make 28,000 | 3.8 "Draw arrows from the middle to the numbers on the sides to obtain the desired sums" (side number 28,000) | M3.S17.T17.C66 b6 (3.8.side_targets) | prompt | one of the six blank side numbers left to the reader; the plan's working uses the printed middle numbers. |
| 9 | Mental Math: make 63,000 | same figure, side number 63,000 | M3.S17.T17.C72 b0 (T9.D0.E3) | prompt | as row 8. |
| 10 | Mental Math: make 61,600 | same figure, side number 61,600 | M3.S17.T17.C74 b0 (T9.D0.E1) | prompt | as row 8. |
| 11 | Mental Math: make 19,500 | same figure, side number 19,500 | M3.S17.T17.C71 b0 (T9.D0.E4) | prompt | as row 8. |
| 12 | Mental Math: make 31,000 | same figure, side number 31,000 | M3.S17.T17.C73 b0 (T9.D0.E2) | prompt | as row 8. |
| 13 | Mental Math: make 20,900 | same figure, side number 20,900 | M3.S17.T17.C70 b0 (T9.D0.E5) | prompt | as row 8. |
| 14 | Mental Math: make 14,000 | 3.8 "What about 14,000, 15,000 and 16,000? Yes, it is possible. Explore how." | M3.S17.T17.C69 b0 (T9.D0.E6) | prompt | in the book's solutions (1500 × 8 + 400 × 5); the plan's working is identical. |
| 15 | Mental Math: make 15,000 | same sentence | M3.S17.T17.C68 b0 (T9.D0.E7) | prompt | in the book's solutions (13,000 + 400 × 5). |
| 16 | Mental Math: make 16,000 | same sentence | M3.S17.T17.C67 b0 (T9.D0.E8) | prompt | in the book's solutions (1500 × 8 + 400 × 10). |
| 17 | Mental Math: add and subtract to make 45,000 | 3.8 Adding and Subtracting "45,000 = " (boxes 40,000, 7000, 300, 1500, 12,000, 800) | M3.S17.T17.C75 b2 (3.8.add_subtract) | prompt | a blank to fill, left to the reader; the example 39,800 is the book's. |
| 18 | Mental Math: add and subtract to make 5900 | "5,900 = " | M3.S17.T17.C78 b0 (T9.D1.E1) | prompt | as row 17. |
| 19 | Mental Math: add and subtract to make 17,500 | "17,500 = " | M3.S17.T17.C77 b0 (T9.D1.E2) | prompt | as row 17. |
| 20 | Mental Math: add and subtract to make 21,400 | "21,400 = " | M3.S17.T17.C76 b0 (T9.D1.E3) | prompt | as row 17. |
| 21 | 5-digit + 5-digit giving a 5-digit sum more than 90,250. | 3.8 Figure it Out 1, card 1 | M3.S18.T18.C80 b8 (3.8.FiO1_cards) | exercise | Figure it Out card; the book's solution 45,000 + 45,400 is the plan's. Named like the kept cards. |
| 22 | 5-digit + 3-digit giving a 6-digit sum. | Figure it Out 1, card 2 | M3.S18.T18.C85 b0 (T10.D0.E1) | exercise | the book gives 99,999 + 999; the plan's block is the same. |
| 23 | 5-digit − 5-digit giving a difference less than 56,503. | Figure it Out 1, card 6 | M3.S18.T18.C84 b0 (T10.D0.E5) | exercise | the book gives 80,000 − 50,000; same. |
| 24 | 5-digit − 3-digit giving a 4-digit difference. | Figure it Out 1, card 7 | M3.S18.T18.C83 b0 (T10.D0.E6) | exercise | the book gives 10,000 − 999; same. |
| 25 | 5-digit − 4-digit giving a 4-digit difference. | Figure it Out 1, card 8 | M3.S18.T18.C82 b0 (T10.D0.E7) | exercise | the book gives 12,000 − 2,500; same. |
| 26 | 5-digit − 5-digit giving a 3-digit difference. | Figure it Out 1, card 9 | M3.S18.T18.C81 b0 (T10.D0.E8) | exercise | the book gives 50,999 − 50,000; same. |
| 27 | Number Patterns: figure a, rows of 40s and 50s | 3.9 "Find out the sum of the numbers in each of the below figures", figure a | M3.S20.T20.C99 b5 (3.9.fig_a) | prompt | a sum left to the reader; the plan's 980 checks against the printed figure. Has figures. |
| 28 | Number Patterns: figure b, dice showing 1 or 5 | figure b | M3.S20.T20.C101 b0 (T11.D0.E1, canon to 3.9.fig_b) | prompt | 144 checks against the printed 8 by 8 grid (five 2 by 2 blocks of 5s). Has figures. |
| 29 | Number Patterns: figure c, cards of 32 and 64 | figure c | M3.S20.T20.C100 b0 (T11.D0.E2, canon to 3.9.fig_c) | prompt | 2048 checks against the printed figure. Has figures. |
| 30 | Number Patterns: figure d, a 7 by 5 grid of dice | figure d | M3.S20.T20.C102 b1 (3.9.fig_d) | prompt | 123 checks against the printed figure (counted on the PDF). Has figures. |
| 31 | Number Patterns: figure e, the hexagon of 15, 25 and 35 | figure e | M3.S20.T20.C104 b0 (T11.D1.E1, canon to 3.9.fig_e) | prompt | 1650 (22 of each number, counted from the page text). Has figures. |
| 32 | Number Patterns: figure f, rings of circles | figure f | M3.S20.T20.C103 b0 (T11.D1.E2, canon to 3.9.fig_f) | prompt | 7250 (1 × 1000, 4 × 500, 8 × 250, 18 × 125, counted from the page text). Has figures. |
| 33 | Game of 21: the winning pattern | 3.12 Game #1 "Which player can always win if they play correctly? What is the pattern of numbers that the winning player should say?" | M4.S26.T26.C124 b6 (3.12.game1; canon folds game1_strategy) | prompt | icon-marked, one definite answer (1, 5, 9, 13, 17, 21; the first player). |

Kept as they are (59, in book order): 3.1 Q1 to Q7; 3.2 Figure it Out 1, 2, 3 and 4, 5, 6, 7, 8, 9, 10 (the live order
had Q8 and Q9 before Q5 to Q7), then the new Try This, then end-of-chapter Q1; 3.3 lines a to d and end Q3 (after the new
placing question); 3.4 Q1 (a), (b), (c), (d) then Q2 and Q3 (live order had (a) fourth); 3.7 Q2; 3.7 Q3; 3.7 Q1 (a) to (d),
Q4 and end Q2 (after the new 321 question); the 3.8 cards 4 + 4, 5 + 5 = 6 digits, 18,500 and 91,500 (interleaved with the
six new cards in the printed card order), make your own, Q2 a to e, end Q6; end Q7; end Q8 then Q9 (live had Q9 first);
the nine estimation concepts (live had Sheetal, items 5 and 7, before items 1 to 4 and 6); end Q10 after the new Game of 21.
`q_figure` and `s_figure` were added to kept concepts only where the printed question depends on a picture the PDF
shows: 3.1 Q3 (the first line of children), 3.2 Q1, Q2, Q3 and Q4 (the supercell rows), Q8 and Q9 (solution row only: the
printed question has no table), end Q1 (the 3 by 3 grid), and the four number lines of 3.3. All figure sentences were
checked against the PDF pages.

Renames through `rename_teach` (kept question concepts whose names carried a book exercise number, which would reach the
image titles; the structure gate refuses "page N" and these were the only names with book numbering): Figure it Out 3.2
Q5, Q6, Q7, Q10 to "Supercells: most in rows of 2 to 7 cells", "Supercells: a row with none", "Supercells: the largest
and the smallest number", "Supercells: make your own puzzle"; Figure it Out 3.4 Q1 (a) to "Digit Sum 14: write other
numbers"; Figure it Out 3.8 Q1 (make_own) to "Digit Cards: make your own card"; End of chapter Q8 to "Collatz: why powers
of 2 reach 1"; Estimation 3.11 items 1, 2, 3, 4, 6 to "Estimation: words in your maths book / students who come by
bus / fruit custard for 5 people / Gandhinagar to Kohima / walking across India". No teaching concept is renamed.
Other kept names (question text, some cut with "...") are unchanged. The live structure gate still reports 1 problem
(the video script of the words-in-your-maths-book video), the same before and after.

## Borderline, not moved

- Reverse-and-add additions 34 + 43, 29 + 92, 48 + 84 + 132 + 231, 76 + 67 + 143 + 341 (3.5, p61 figure): the book prints
  them already worked and only says "look at these additions, try to figure out what is happening". The plan's blocks
  (C46 b4, C47, C48, C49, "Example 1 to 4: <start number>") have only the start number as their question. Not in the
  book's solutions. They stay in teaching with their videos. To count them, add four prompt entries to topic M2.S11.T11.
- Kaprekar 6382 (3.6, p63 figure, "Pick any 4-digit number ... say 6382 ... What happens if we continue doing this?"):
  printed as a worked figure and not in the book's solutions; the plan's C57 b12 stays. The closest call after the
  additions above.
- Plan-authored examples with their own context: C2 b7 (heights 120, 138, 125 cm), C53 b3 (is 10/02/2001 a palindromic
  date?), C54 (will the 2025 calendar be reused: 2031), C107 b8 (check the rule on sequence a). The book's own questions
  these sit next to are listed under Gaps.
- Math Talk and discussion: "List five situations where numbers are used" (p55), "What do you think these numbers mean?"
  (p55), "Why are some numbers coloured? Discuss." (3.2), "Do you see how these sequences were formed?" (3.10), "Share
  and discuss in class the different methods" (3.9), "Observe the figure. What can you say about the numbers and the
  lines drawn?" (3.8), "Could you find examples for all the cases? ... Make other such questions" (3.8, inside the
  kept make-your-own concept), "Make your own variations of this game" (3.12), "Make some estimation questions"
  (3.11, inside the kept Sheetal concept via est7).
- Explore: "Take different 4-digit numbers ... check with your friends" (3.6): open, the result is stated in the next
  sentence.
- 3.2 Table 1 (8632 is greater than its neighbours): a statement, nothing asked.

## Gaps (book questions the plan has no movable block for)

All of these have the content only in teaching text blocks (no block kind the engine can cut), so none could be moved.

- 3.3 "Put a circle around the smallest number and a box around the largest number in each of the sequences above":
  C27 b4 (3.3.circle_box), text only.
- 3.4 Figure it Out 2 "Find out the digit sums of all the numbers from 40 to 70": C38 b0 to b3, text only. The kept
  C44 carries the ref 3.4.FiO2 but its block covers only Q3 (123 to 789).
- 3.5 Explore "Will reversing and adding ... always give a palindrome?" (answer yes): C46 b2, text only.
- 3.7 "Try and find out all possible times on a 12-hour clock of each of these types": C52 b3 to b6, text only.
- 3.7 Manish "Find some other dates of this form" and Meghana "Find all possible dates of this form": C53 b0 to b2, text only.
  The book's printed answer 01/02/2001 is not a palindromic date by the plan's own check (01022001 reversed is 10022010),
  so even with a block it would need the book's answer checked first.
- 3.7 "Will any year's calendar repeat again after some years?" (answer yes): C53 b5 to b8, text only; the plan's specific
  2025 example (C54) stays in teaching.
- 3.8 "Can we make 1,000 ... Why not?" and "What thousands cannot be made?": C66 b8 to b10, text only (the 14,000, 15,000
  and 16,000 parts are rows 14 to 16).
- 3.10 "Make some more Collatz sequences ... Do you always reach 1? Do you believe the conjecture?": C107 b10, C108 b6, text only.
- 3.11 Figure it Out 1 to 3 (steps to walk, blinks or breaths, objects around you): C112 b5 to b7, text only; the kept
  C115 is tagged with 3.11.FiO1 to FiO3 but holds the Paromita example.
- 3.12 Game #2 (race to 99): "Which player can always win? What is the pattern?": C125 b1 to b2, text only (3.12.game2).

## Judgement calls

1. One concept per item, not per printed task. The book prints the six side numbers of the 3.8 arrow figure, the four
   add-and-subtract blanks, the ten cards of Figure it Out 3.8 Q1 and the six figures of 3.9 each as ONE task. The plan
   already carries one concept (and one video) per card, line or part for every Figure it Out in this chapter (the kept
   cards, the lines a to d, Q2 a to e), and has one block per target and per figure, so the new questions follow that
   split. The brief's other rule (a multi-part question stays one concept) would fold them: for the three Mental Math
   groups, list their blocks in one entry and `canon` the T9 ids; the six 3.9 figures cannot share one card.
2. The arrow targets and the four add and subtract blanks are not in the book's solutions and carry no icon; they are
   counted because they are blanks or "make" tasks left to the reader, with the plan holding a block for each.
3. Thin-extra concepts carry objectives (O61, O62, O64, O78, O79), so none could move whole: their blocks were cut. That
   leaves 20 concepts with no content blocks but with their own video, objective and name: C67 to C74, C76 to C78 (Mental
   Math), C81 to C85 (digit counts) and C100, C101, C103, C104 (3.9). Their live videos are rendered; the new questions
   have none. A later pass can pair each new question with its orphaned video (the question text of each is the same
   target) or retire the empty concepts.
4. Several plan blocks have a very short `question` (Make 28,000.; Start with 321.; Find the number and write it in
   words.; One way to complete Table 2, and three questions about it.). The spec cannot edit block text, so the figure
   sentence of those questions carries what the card needs (the middle boxes, the steps and question, the clues, the
   instruction and the three blanks). Text of the blocks themselves should be tidied before the cards are authored.
5. Refs: each question has one ref. Where the plan gave a block its own T-id (T9, T10, T11) that id is used, except the
   four 3.9 figures, folded by `canon` to their book ids 3.9.fig_b, fig_c, fig_e, fig_f; 3.8.FiO1_cards (shared with the
   kept cards) is used for the first new card.
6. FiO 3.7 Q4 (kept, C64): the plan says 7 rounds (with 0558 as the smallest number in round 2) and its own teacher note
   says the book's solutions give 8; left as it is.
7. The kept Figure it Out 3.2 Q10 (make your own supercell puzzle) and 3.8 Q1 make-your-own are open tasks, but they are
   existing question concepts and the engine keeps every one.
8. The new Questions topic after "Counting with Place Value" holds both 3.4 in-text questions; the Digit Sums questions
   (Figure it Out 3.4) stay in their own existing topic after "Digit Sums".
