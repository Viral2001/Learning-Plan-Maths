# Class 7 Ch 11 Finding Common Ground (cbse_eng_maths7_ch11, live v25, book file gegp203): question layout notes

Spec: `layout_spec.json`. Result of `check`: 54 question concepts in 16 Questions topics (21 existing Figure it Out concepts
kept in book order + 33 new: 7 example, 26 prompt, 0 exercise). 24 new videos needed, 9 live videos kept (2 of them cover
only part of their question: Jump Jackpot and Idli-Vada). No book question is a gap among the counted ones (see Gaps for
two small items). Gates identical to live (structure 38, video_script_rules 72, skeleton 9), `INTEGRITY: clean`.

Nine Questions topics are new (after the teaching topics Introducing HCF, Rice Bags, Jump Jackpot, Prime Factorisation,
Toran, Sweet Shop and Idli-Vada, Doubling and Common Multipliers, Common Division, HCF x LCM). Seven already existed
(Factors from Prime Factorisation, HCF from Common Subparts, HCF by Minimum, LCM from Prime Factorisation, Patterns,
Applying Part One and Part Two); their Figure it Out concepts are kept after the new items, which is where the book puts
them (examples and in-text questions come before the section's Figure it Out). The 21 kept concepts are every printed
Figure it Out question of the chapter (1 + 1 + 2 + 1 + 3 + 13); none is missing from the plan.

## How a book question was recognised here

I checked the PDF (pages 47 to 64). In this edition the round "?" icon sits beside each Example, each Figure it Out heading
and each question put to the reader; "Try This" and "Math Talk" stickers sit beside some of them. Rule used:

* Counted: a question that carries the "?" or Try This icon, has a definite answer, and for which the plan has a block asking
  it with the book's own numbers. Also a plain direct request without an icon ("How many tiles ...?", "Does such a number
  exist?", "Try finding the prime factorisation of 1200") whose answer the book does not print.
* Not counted: a rhetorical lead-in with no icon that the book answers in its next sentence; the plan's own examples (own
  numbers); a plan block that asks something other than what the book asks.
* Narration inside an Example ("How many 2s should the LCM contain?", "Is 2 x 3 x 5 x 7 also a common multiple?") is a
  step of that Example, not a question of its own.

## New questions

b2 is the worked_example block of a teaching concept; "whole" means the thin-extra concept (one block, own video) moves with
its node. Placement: each goes first in the Questions topic of the topic it came from, in book order, before the kept Figure it Out.

| Topic | New question | Book label or quote | Plan source (ref) | Tier | Why it counts |
|---|---|---|---|---|---|
| Introducing HCF | Tile Problem: the largest square tile | 3.1 opening "What size tiles should she buy?" (? icon; room 12 ft by 16 ft) | M1.S2.T2.C3 b2 (3.1.tile_largest); new video | prompt | "?" question, definite answer (4 ft); the framing topic's opener retells it but cannot be a source. |
| Introducing HCF | Tile Problem: how many 4 ft tiles | "How many tiles of this size should she purchase?" | M1.S2.T2.C4 b2 (3.1.tile_count); new video | prompt | direct "how many" question, answer (12) not printed. The block also names the HCF; ref hcf_def stays on C4. |
| Introducing HCF | Try This (Tiles): fractional tile sides | Try This "What if Sameeksha did not insist on ... a whole number of feet ... Would the answer change?" | M1.S2.T2.C5 whole (3.1.tile_fraction); video kept | prompt | Try This icon, definite answer (no, still 4 ft). Thin-extra, one block. |
| Rice Bags | Rice Bags: the greatest equal bag weight | Lekhana, 84 kg and 108 kg, "what should the weight of each bag be?" | M1.S3.T3.C7 b2 (3.1.rice); new video | prompt | "?" question, answer 12 kg. See judgement call 4. |
| Jump Jackpot | Jump Jackpot: the longest jump on two numbers | "Find the longest jump size ... (a) 14 and 30 (b) 7 and 11 (c) 30 and 50 (d) 28 and 42" | M1.S4.T4.C9 b2 (jump_a, jump_b) + C10 whole (jump_c, jump_d); canon to jump_a; video of C10 kept | prompt | one printed question with four parts, "?" icon. C10's video covers (c) and (d) only, so refresh. |
| Jump Jackpot | Jump Jackpot: longest jump and the HCF | "Is the longest jump size for the numbers the same as their HCF? Explain why it is so." | M1.S4.T4.C11 b2 (3.1.jump_hcf); new video | prompt | its own "?" icon; definite answer (yes) with the reason. |
| Prime Factorisation | Division Method: prime factorisation of 1200 | "Try finding the prime factorisation of 1200 using the method above." | M1.S6.T6.C17 whole (3.1.pf_division); video kept | prompt | direct request, answer not printed. Thin-extra, one block. |
| Factors from Prime Factorisation | Factors from Primes: is 28 a factor of 840 | "Is 2 x 2 x 7 = 28 a factor of 840? ... what should it be multiplied by? ... is 2 x 7 = 14 ... 2 x 2 x 2 ... 3 x 3 x 3 a factor?" (five "?" icons) | M1.S7.T7.C19 b2 (3.1.f840); new video | prompt | one running question on the same number; 14, 8 and 27 are put to the reader with "Why or why not?". |
| Factors from Prime Factorisation | Factors from Primes: all the factors of 225 | "Find the factors of 225 using prime factorisation." | M1.S7.T7.C20 b2 (3.1.f225); new video | prompt | "?" icon, definite list. The follow-up "Check that all the factors of 225 occur in this list" is part of it. |
| HCF from Common Subparts | Example 1: Common factors of 45 and 75 | Example 1 | M1.S9.T9.C24 b2 (3.1.ex1); new video | example | labelled Example, same numbers. |
| HCF from Common Subparts | Example 2: Common factors of 112 and 84 | Example 2 | M1.S9.T9.C25 b2 (3.1.ex2); new video | example | labelled Example, same numbers. |
| HCF from Common Subparts | Example 3: Common factors of 96 and 275 | Example 3 | M1.S9.T9.C26 b2 (3.1.ex3); new video | example | labelled Example, same numbers. |
| HCF by Minimum | Example 4: HCF of 30 and 72 | Example 4 | M1.S11.T11.C29 b2 (3.1.ex4); new video | example | labelled Example, same numbers. |
| HCF by Minimum | Example 5: HCF of 225 and 750 | Example 5 | M1.S11.T11.C30 b2 (3.1.ex5); new video | example | labelled Example, same numbers. |
| Toran | Toran: the shortest length both can make | 3.2 opening "what is the smallest possible length, the torans could be? ... shortest toran that they can both make?" | M2.S13.T13.C35 b2 (3.2.toran); new video | prompt | "?" icon, answer 24 cm. |
| Toran | Toran: is there a largest common multiple | "What about the largest common multiple? Does such a number exist?" | M2.S13.T13.C36 b2 (3.2.toran_largest); new video | prompt | direct yes/no question, answer (no) not printed in the book. |
| Sweet Shop and Idli-Vada | Gajak Shop: days until free gajak again | "When is the next time she would be able to get free gajak ...? (Answer in number of days.)" | M2.S14.T14.C38 b2 (3.2.sweet); new video | prompt | "?" icon, answer 70. |
| Sweet Shop and Idli-Vada | Idli-Vada: the first number called for four pairs | "Find the first number for which 'idli-vada' will be called out: (a) 4 and 6 (b) 7 and 11 (c) 14 and 30 (d) 15 and 55. Is the answer always the LCM of the two numbers? Explain." | M2.S14.T14.C39 b2 (idli_a, idli_b) + C40 whole (idli_c, idli_d, idli_lcm); canon to idli_a; video of C40 kept | prompt | one printed question, "?" icon. C40's video covers (c), (d) and the LCM remark, so refresh. |
| LCM from Prime Factorisation | Example 6: LCM of 14 and 35 | Example 6 | M2.S15.T15.C42 b2 (3.2.ex6); new video | example | labelled Example. Ref lcm_intro (36 and 648) stays on C42. |
| LCM from Prime Factorisation | Example 7: LCM of 96 and 360 | Example 7 | M2.S15.T15.C43 b2 (3.2.ex7); new video | example | labelled Example, same numbers. |
| Patterns in HCF and LCM | Patterns in HCF: pairs where the HCF is one number | "Find more such number pairs where the HCF is one of the two numbers. How can we describe such pairs of numbers?" | M3.S17.T17.C46 b2 (3.3.pattern_hcf); new video | prompt | "?" icon; the description (one number is a factor of the other) is definite. See judgement call 6. |
| Patterns in HCF and LCM | Patterns in HCF: the other number for m and 7k | "(a) if m is a number, what could be the other number? (b) if 7k is a number ...?" | M3.S17.T17.C47 whole (3.3.pattern_algebra); video kept | prompt | "?" icon, definite answers. Thin-extra, one block. |
| Doubling and Common Multipliers | Doubling: HCF of 270 and 50 and their doubles | "What happens to the HCF of two numbers if both numbers are doubled? ... Are you able to see why the HCF will also double?" | M3.S19.T19.C53 b2 (3.3.double); new video | prompt | "?" icon, definite answer (it doubles) on the book's own 270 and 50. See judgement call 2. |
| Doubling and Common Multipliers | Common Multipliers: HCF of 14 x 6 and 14 x 9 | "Consider the following two multiples of 14: 14 x 6, 14 x 9. What is their HCF?" | M3.S19.T19.C54 b2 (3.3.multiples14); new video | prompt | "?" icon, answer 42. Ref common_mult belongs to the next question. |
| Doubling and Common Multipliers | Common Multipliers: four more pairs | "Find their HCF: (a) 18 x 10, 18 x 15 (b) 10 x 38, 10 x 21 (c) 5 x 13, 5 x 20 (d) 12 x 16, 12 x 20. In which of these cases is the HCF the same as the common multiplier?" | M3.S19.T19.C55 whole (3.3.common_mult); video kept | prompt | "?" icon, definite answers (90, 10, 5, 48). Thin-extra, one block. |
| Common Division Method | Common Division: HCF of 84 and 180 | "How do we use this to find the HCF of 84 and 180? Explore." | M3.S20.T20.C57 b2 (3.3.div_explore); new video | prompt | "?" icon with a hint, answer 12. q_figure is the ladder the book prints. |
| Common Division Method | Common Division: HCF of 300, 150 and 630, 770 | "Find the HCF in the following cases." (two printed ladders) | M3.S20.T20.C58 whole (3.3.div_hcf); video kept | prompt | "?" icon, definite answers (150 and 70). Thin-extra, one block. |
| Common Division Method | Common Division: bigger divisors for two pairs | Try This "You can try this method for these pairs of numbers. (a) 90 and 150 (b) 84 and 132" | M3.S20.T20.C60 b2 (3.3.try_pairs); new video | prompt | Try This icon, definite answers. Ref guna_anshu (the narrated method) stays on C60. |
| HCF x LCM = Product | HCF and LCM Property: LCM against the product | "Which is greater, the LCM of two numbers or their product? ... try to reason or prove why the LCM is never greater" | M3.S21.T21.C62 b2 (3.3.lcm_vs_product); new video | prompt | "?" icons, definite answer (never greater, equal when co-prime). See judgement call 2. |
| HCF x LCM = Product | HCF and LCM Property: 105 and 95 | "Consider the numbers 105 and 95. Find their LCM." with the product 105 x 95 = LCM x 5 | M3.S21.T21.C63 b2 (3.3.hcf_lcm_105_95); new video | prompt | "?" icon, same numbers. See judgement call 4. |
| HCF x LCM = Product | HCF and LCM Property: three more pairs | "Explore whether the LCM is a factor of the product: (a) 45, 105 (b) 275, 352 (c) 222, 370" | M3.S21.T21.C64 whole (3.3.hcf_lcm_try); video kept | prompt | "?" icon, definite answers (15, 11, 74). Thin-extra, one block. |
| HCF x LCM = Product | HCF and LCM Property: why the product rule holds | "Why does this happen? Can you give an explanation or proof?" (Try This, with a hint) | M3.S21.T21.C65 b2 (3.3.hcf_lcm_why); new video | prompt | Try This icon; the plan block answers it with the book's hint on 12 and 18. See judgement call 2. |
| HCF x LCM = Product | HCF and LCM Property: three numbers | "Explore whether this property holds when 3 numbers are considered." (Try This) | M3.S21.T21.C66 whole (3.3.three_numbers); video kept | prompt | Try This icon, definite answer (no, counter-example 4, 6, 10). See judgement call 2. |

Kept as they are (21, in book order after the new ones of their topic): Figure it Out (listing factors); (common factors and
HCF); (HCF) Q1, Q2; (LCM); (patterns) Q1 to Q3; End of chapter Figure it Out Q1 to Q7 and Q8 to Q13 (the last six sit in
the existing Questions topic after Applying Part Two, which needs no entry). Only End of chapter Q1 carries `q_figure`
and `s_figure` (the two rows of coloured stars, checked on the PDF); the others are text only.

Figures set on new questions: the 16 ft by 12 ft room cut into 4 ft tiles (s_figure), the toran strip rows (s_figure),
the stacked factorisations with the common subparts ringed for Examples 1, 2, 4 and 5 (s_figure), and the division
ladders for the two Common Division questions (q_figure and s_figure). The other new questions are text only.

## Borderline, not moved

- "Can this process be simplified? Can it be made more reliable?" (3.1), "How do we directly find the HCF without listing all the factors?" and "How do we find the LCM of two numbers using their prime factors?": rhetorical lead-ins with a "?" icon but no answer to give; no block.
- 90 = 3 x 3 x 2 x 5 and "Will these all lead to the same prime factors?" (C15 b2, 3.1.pf_90): no icon, the book answers in the next sentence ("Remarkably, ... always the same").
- "Can you write the prime factorisation of 105 and 30 using these two figures?" (C16 b2, 3.1.pf_trees): no icon; the book prints both factorisations in the division layout straight below.
- Anshu's claim "The larger a number is, the longer its prime factorisation will be. What do you think?" (C21 b2, 3.1.anshu_claim): no icon, and the book gives the counter-example 96 and 121 in the next sentence.
- "Why are these the LCMs? [Hint ...]" (C59 b2, 3.3.div_lcm): the book prints the two LCM expressions and asks only why; the plan block asks to compute them, so it is not the printed question. Stays in teaching.
- "Can you see why this works?" after Guna and Anshu (p. 62): discussion with no block.
- "Which calculation is easier to carry out?" (1200, 40 x 30 = 5 x 8 x 5 x 6): discussion, no block.
- Plan-authored examples with their own numbers stay: C13 primes 1, 2, 9, 13, 21, 29; C31 HCF of 36, 60, 84 (the book only says the method extends to more numbers); C48 pairs 8 and 10 and the rest (the printed items are the kept Figure it Out Q1); bells, ribbons, 2 x 2 x 3 x 5 and 2 x 3 x 3 x 7 (C68 to C70); remainders, cat and mouse, 1/6 + 1/4 (C79 to C81); chapter review (C89, C90).
- Mystery Colours "Try to decode the colour scheme ... Share your observations" and the History/summary boxes: open or not questions.

## Gaps (book questions the plan has no block for)

- Mystery Colours, "colour the page numbers from 101 to 110" (last page): C92 and C93 hold text only, no worked-example block. The task is picture-based.
- "Why are these the LCMs?" (3.3, with its hint): no block answers it (C59's block only computes the LCMs).

## Judgement calls

1. Items with the "?" icon that the book then solves in its own text (tile, gajak, 14 x 6 and 14 x 9, 105 and 95, factors of 225, 28 and 840) are counted, following the Class 7 Ch 8 precedent that the "?" icon marks a question put to the reader. To treat them as teaching, delete the entry; nothing else changes.
2. Four "explore or explain" items are counted although the plan answers them on its own chosen numbers: doubling (book numbers 270 and 50), LCM against the product (6, 8, 7, 9), why the rule holds (12 and 18) and three numbers (4, 6, 10). Each has a "?" icon (two also Try This) and a definite answer. To drop them, delete their four entries (C53, C62, C65, C66); they then stay in their teaching concepts, and C66 stays as its own thin-extra concept with its video.
3. `canon` folds only sub-ids of one printed question: jump_b, jump_c, jump_d into jump_a and idli_b, idli_c, idli_d, idli_lcm into idli_a. Ids such as hcf_def, lcm_intro and guna_anshu are definitions or narrated methods and stay on their teaching concepts.
4. The plan blocks sometimes ask more than the printed question: the rice block also counts the bags (16, the book asks only the weight), and the 105 and 95 block also asks the HCF and the check (the book asks the LCM, then the multiplier). They are moved as the printed question they retell.
5. The plan answers agree with the book everywhere checked (tile 4 ft, rice 12 kg, jumps 2, 1, 10, 14, idli-vada 12, 77, 210, 165, 14 x 6 and 14 x 9 gives 42, 105 and 95 gives 5 and 1995, and the rest).
6. "Find more such number pairs" is open-ended; it is counted because the printed follow-up "How can we describe such pairs?" has one definite answer, which the block gives.
7. Fifteen teaching concepts end with no coverage ref (their ref moved with the question): C3, C7, C11, C19, C20, C24 to C26, C29, C35, C36, C38, C43, C53, C62 in the live numbering. Gates are unchanged. Each keeps its text, teaching plan and own video; those videos still walk through the moved question.
8. `rename_teach` is empty: no teaching concept is named after a moved example, and no new name equals an existing concept name.
9. The two Jump Jackpot and Idli-Vada questions keep a video that covers only the later parts, so those two need a refresh as well as the 24 new videos.
