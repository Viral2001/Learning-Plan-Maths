# Class 8 Ch 8 "Fractions in Disguise" (cbse_eng_maths8_ch8, live v54): question layout notes

The live plan's concept-to-media links are intact (every concept's media ids have a node that names that concept, and `check` with an empty spec prints `INTEGRITY: clean`), so the layout was authored.

Result of `check`: 84 question concepts in 6 Questions topics (32 new + 52 kept); tiers of the new ones: 17 example, 0 exercise, 15 prompt. 21 new videos needed: 11 new questions are whole-moved single-block concepts and keep their rendered video, the other 21 are cut out by block. `INTEGRITY: clean`. Gates: structure 0 / 0, coverage 16 -> 0, video_script_rules 99 / 99, skeleton 46 -> 45, objectives 33 / 33, so nothing is worse than live.

## HELD BACK: "Percentages That Trick You" (M4.S12.T12) has no Questions topic and gets none

The live plan has a Questions topic after every concept topic except this one (T14 is attached to the Summary and stays as it is). A new Questions topic is built by the engine as a copy of this chapter's own first one, which is typed instructional/exploration, so the skeleton and objectives gates read it as an idea topic and flag it (no topic_objective, last concept not a doer, 5 concepts instead of 2 to 4). With the entry below added, `check` prints `skeleton_problems (46, 50)` and `objectives_problems (33, 34)` and the line `GATES WORSE THAN LIVE`, so the entry is NOT in `layout_spec.json`. Five book questions therefore stay in the teaching concepts of T12 (C80, C81, C82). Everything else in the spec is valid with this entry added (37 new: 19 example, 18 prompt, 26 new videos; INTEGRITY clean). To use it, append this to `topics` of the spec if a new Questions topic of this type is acceptable:

```json
{"teach_topic": "M4.S12.T12", "questions": [
 {"name": "Would You Rather: percentage gain of each option", "tier": "prompt", "refs": ["1.3.would_you_rather"], "from": [{"concept": "M4.S12.T12.C80", "block": 3}], "keep_video_of": null, "q_figure": null, "s_figure": null},
 {"name": "Discount Choice: 20% off or ₹50 off", "tier": "prompt", "refs": ["1.3.discount_choice"], "from": [{"concept": "M4.S12.T12.C80", "block": 4}], "keep_video_of": null, "q_figure": null, "s_figure": null},
 {"name": "Example 12: Cakely or Cakify", "tier": "example", "refs": ["1.3.ex12"], "from": [{"concept": "M4.S12.T12.C81", "block": 4}], "keep_video_of": null, "q_figure": null, "s_figure": null},
 {"name": "Example 13: Surbhi's cookware mishap", "tier": "example", "refs": ["1.3.ex13"], "from": [{"concept": "M4.S12.T12.C82", "block": 3}, {"concept": "M4.S12.T12.C82", "block": 4}, {"concept": "M4.S12.T12.C82", "block": 5}], "keep_video_of": null, "q_figure": null, "s_figure": null},
 {"name": "Try This (Tricky Percentages): Ariba and Arun", "tier": "prompt", "refs": ["1.3.ariba_arun"], "from": [{"concept": "M4.S12.T12.C82", "block": 6}], "keep_video_of": null, "q_figure": null, "s_figure": null}
]}
```

Why each counts: p25 "What is the percentage gain each option gives?" (200% and 50%); p26 "20% discount or ₹50 discount ... (i) ₹180 (ii) ₹225 (iii) ₹300" (definite choice for each bill); p26 Example 12 (Cakely or Cakify); p27 Example 13 (i), (ii), (iii) is one printed question, so its three blocks are one concept (all three already carry ref ex13); p27 Try This, Ariba and Arun (definite answer). C83 "Surbhi's Twelve Thousand" (ref ex13_ii) is the plan's own full-wording copy of Example 13 (ii) and is left in teaching; the engine cannot fold a duplicate.

## Layout

Book order of each Questions topic: in-text questions and examples first, then the section's Figure it Out items, except where the book prints them otherwise (see Judgement calls 3 and 4). Every concept topic except T12 already has its Questions topic, so no Questions topic is created; the new questions go in the existing ones and the kept concepts are listed (all `keep`, in book order) so the engine does not append them in the live order. Concepts that carry an objective cannot move whole, so every new question taken from a teaching concept with an objective is cut out by block.

## New questions (32)

Plan source is `live concept id` + block index (b3 = fourth block); "whole" means a single-block enrichment concept moved with its rendered video (`keep_video_of` set). All others have `keep_video_of: null`. Page numbers are the book's printed pages.

| Topic | New question | Book label or quote | Plan source | Tier | Why it counts |
|---|---|---|---|---|---|
| A Percentage Is a Fraction in Disguise | Fraction to Percentage: the yellow share of the paint | p2 "Can you tell what percentage of the colour was made using yellow?" (after Example 1) | M1.S2.T2.C4 b4 (ref ex1_yellow) | prompt | in-text "?" question, answer 25%. |
| A Percentage Is a Fraction in Disguise | Fraction to Percentage: filling in Method 3 | p3 "Try completing Method 3 by filling the boxes." | M1.S2.T2.C4 b5 (ref ex2_method3) | prompt | fill the four boxes of the bar (20%, 40%, 60%, 80%). Has q_figure and s_figure. |
| A Percentage Is a Fraction in Disguise | Why Percentages: which biscuit is more sugary | p4 "Sugar makes up 9/34 of Variety 1 and 13/45 of Variety 2. Which variety is more sugary?" | M1.S2.T2.C6 b3 (ref why_percent) | prompt | in-text question, definite answer (Variety 2). Placed after Figure it Out 5 because the book prints it there. |
| Taking a Percentage of Something Real | Example 1: Who ate more sugar | Example 1 (p6) Madhu 25% of 120 g, Madhav 35% of 95 g | M2.S4.T4.C13 b4 | example | printed Example; 30 g against 33.25 g. |
| Taking a Percentage of Something Real | Free-hand Computations: filling the mental table | p7 to p8 "Calculate (without pen and paper) the indicated percentages of the values in the table", then 40% and 15% | M2.S4.T4.C15 b0 (ref free_hand_table) | prompt | task with a definite table of answers. The plan holds it as three identical blocks (ids free_hand_table, _40, _15); only b0 is cut (Judgement call 2). Has q_figure and s_figure. |
| Taking a Percentage of Something Real | Example 2: Decimal multiplier for 10% | Example 2 (p8) "to find 10% of a quantity, what decimal value should be multiplied?" | M2.S4.T4.C18 whole (ref ex2) | example | the answerable part of printed Example 2 (0.1); single-block enrichment concept moved with its video. |
| Taking a Percentage of Something Real | FDP Trio: completing the table | p8 "Complete the following table" (percent, fraction, decimal for 50%, 100%, 25%, 75%, 10%, 1%, 5%, 43%) | M2.S4.T4.C17 b3 (ref fdp_table) | prompt | definite entries. Has q_figure and s_figure. |
| Taking a Percentage of Something Real | Example 3: Zubin's A grade score | Example 3 (p8) 80% of 75 | M2.S4.T4.C20 b3 | example | printed Example, answer 60. |
| Taking a Percentage of Something Real | Example 4: Millet in the kanji mixture | Example 4 (p9) millet : water = 2 : 7, 500 ml | M2.S4.T4.C21 whole (ref ex4) | example | printed Example; single block with its video. |
| Taking a Percentage of Something Real | Example 5: Cycling from Delhi to Agra | Example 5 (p10) 40% of the journey is 92 km | M2.S4.T4.C22 b4 | example | printed Example, answer 138 km. |
| Taking a Percentage of Something Real | Example 6: Kishanlal's daily sales target | Example 6 (p10 to p11) sales of 2000, 3500, then 5000 and 6000 against a target of 5000 | M2.S4.T4.C23 b3 | example | printed Example; the block holds days 1 to 4 (40%, 70%, 100%, 120%). |
| Taking a Percentage of Something Real | Percentages Past 100: Days 5 and 6 | p11 "On Days 5 and 6 his sales were ₹7800 and ₹9550. Calculate the percentage of the target achieved" | M2.S4.T4.C24 whole (ref ex6_days_5_6) | prompt | in-text question, 156% and 191%. |
| Taking a Percentage of Something Real | Percentages Past 100: Days 7 and 8 | p12 "On Day 7 he achieved 150% ... Day 8 210% ... Find the sales made on these days" | M2.S4.T4.C25 whole (ref ex6_days_7_8) | prompt | in-text question, ₹7500 and ₹10,500. |
| Taking a Percentage of Something Real | Percentages Past 100: table and number line | p12 "Complete the table below. Mark the approximate locations in the following diagram" | M2.S4.T4.C26 whole (ref table_beyond_100) | prompt | nine definite entries. Has q_figure and s_figure. |
| Taking a Percentage of Something Real | Example 7: The wheat harvest | Example 7 (p12) 260 kg then 650 kg | M2.S4.T4.C23 b4 | example | printed Example, 250%. |
| Using Percentages to Compare and to Measure Change | Example 1: Eesha's English and Science scores | Example 1 (p14) 42 out of 50, 70 out of 80 | M3.S6.T6.C39 b3 | example | printed Example (84% against 87.5%). |
| Using Percentages to Compare and to Measure Change | Example 2: Reading the badam drink labels | Example 2 (p15) Know Your Contents, "Complete this table", "Check if the percentages of each product add up to 100" | M3.S6.T6.C40 whole (ref ex2) | example | printed Example; the plan's table values match the labels on the page (99, 30, 12, 9 of 150; 272, 64, 40, 24 of 400). Has q_figure and s_figure. |
| Using Percentages to Compare and to Measure Change | Example 3: Same meaning in two statements | Example 3 (p16) 165% of the 1961 population against an increase of 65% | M3.S6.T6.C41 b6 | example | printed Example, answer yes (both 1.65p). |
| Buying, Selling and the Price You Compare Against | Example 4: Kishanlal's percentage profit | Example 4 (p17) sweater bought at ₹300, sold at ₹430 | M3.S8.T8.C47 b4 | example | printed Example, about 43.3%. |
| Buying, Selling and the Price You Compare Against | Profit Percentage: the wholesaler and the manufacturer | p17 "Find the profit percentage of the wholesaler and the manufacturer." | M3.S8.T8.C48 whole (ref ex4_others) | prompt | direct instruction with a definite answer (18.58% and 10%) read off the p16 picture. Has q_figure. |
| Buying, Selling and the Price You Compare Against | Profit Margin: Shambhavi's notebooks | p17 "She procures 200 page notebooks at ₹36 per book. She sells them with a profit margin of 20%. Find the selling price." | M3.S8.T8.C49 whole (ref shambhavi_notebooks) | prompt | in-text question, ₹43.20. |
| Buying, Selling and the Price You Compare Against | Profit Margin: Shambhavi's crayon boxes | p17 "She sells crayon boxes at ₹50 per box with a profit margin of 25%. How much did Shambhavi buy them from the wholesaler?" | M3.S8.T8.C50 whole (ref shambhavi_crayons) | prompt | in-text question, ₹40. |
| Buying, Selling and the Price You Compare Against | Example 5: Raghu's old rice | Example 5 (p17) 10 kg bought at ₹35 per kg, sold for ₹300 | M3.S8.T8.C51 b0 (ref ex5) | example | printed Example; the per-kg follow-up is left (Judgement call 2). |
| Buying, Selling and the Price You Compare Against | Example 6: Shyamala's damaged vase | Example 6 (p17 to p18) ₹2650, loss of 18% | M3.S8.T8.C52 b3 | example | printed Example, ₹2173. |
| Buying, Selling and the Price You Compare Against | Selling at a Loss: Snehal's strawberries | p18 "He sells some of his stock at ₹80 per kg with a 12% loss. What is the cost price?" | M3.S8.T8.C53 whole (ref strawberries) | prompt | in-text question, about ₹90.91. |
| Buying, Selling and the Price You Compare Against | Discounts: the cooker at 35% off | p18 "A utensil store is offering a 35% discount on the cooker with an MRP ₹1800. What is the selling price? If the cost price was ₹900, what is the percentage profit?" | M3.S8.T8.C52 b4 (ref cooker) | prompt | in-text question, ₹1170 and 30%. |
| Buying, Selling and the Price You Compare Against | Taxes: checking the bill | p19 "Check if the calculations are correct in the bill shown." | M3.S8.T8.C56 b3 | prompt | definite answer (yes: ₹40.50 twice, total ₹531). Has q_figure. |
| Money That Grows, and Money That Shrinks | Example 7: Depositing ₹6000 for 3 years | Example 7 (p21 to p22) both FD options | M4.S10.T10.C67 b4 | example | printed Example, ₹7800 against ₹7986. |
| Money That Grows, and Money That Shrinks | Example 8: Total received versus deposited | Example 8 (p22) "What percent is the total amount received with respect to the amount deposited in both the options?" | M4.S10.T10.C68 whole (ref ex8) | example | printed Example, 130% and 133.1%; single block with its video. |
| Money That Grows, and Money That Shrinks | Compounding: total interest in both options | p24 (Math Talk) "What would be the formula for each of the two options?" for the total interest | M4.S10.T10.C69 b3 (ref math_talk_interest) | prompt | question with a definite answer (p r t and p(1 + r)^t − p). The block also carries ref ex9, which stays on the teaching concept (Gaps). |
| Money That Grows, and Money That Shrinks | Example 10: TV value after 1 year | Example 10 (p25) ₹21,000 depreciating by 5% | M4.S10.T10.C70 b3 | example | printed Example, ₹19,950. |
| Money That Grows, and Money That Shrinks | Example 11: A village after 3 decades | Example 11 (p25) 1250 falling 10% every decade | M4.S10.T10.C70 b4 | example | printed Example, about 910. |

Kept as they are (52 question concepts, in book order): FIO 1.1 Q1 to Q5 (after the two new in-text ones, before the biscuit question); 1.2 Q1 to Q12 (after the new ones; the live plan had Q1 last); 1.3 compare-and-change Q5, Q8, Q11, Q12; 1.3 buy-and-sell Q1, Q2, Q3, Q4, Q6, Q7, Q9, Q10 (the live plan had Q3 and Q7 last); 1.3 compounding Q1 to Q9, interleaved with the new questions the way the book prints them; and the 14 end-of-chapter concepts (T14), which are attached to the Summary and untouched. Kept concepts carrying figures: 1.1 Q4 (race line, q_figure), 1.2 Q1 (three bar-model pairs, q_figure and s_figure) and 1.2 Q2 ("also draw their bar models", s_figure).

## Borderline, not moved

- p1 "Do you know what the symbol '%' means?": rhetorical; the answer is the definition printed right after it (C3 b3, ref intro). Stays in teaching.
- "Two more equivalent forms of 40%" (C5 b3): the plan's own teaching example (new number); not the book's Example 3.
- p4 "why choose 100? Why not 10, 50, 1000, or 43? Think." (C7 b0): why-question, no single answer.
- p7 "How did you find these values? ... Do you find anything interesting in the table?" and the 20%, 5%, 25% relationship (C14 b3): Math Talk discussion.
- p8 "mentally calculate 75%, 90%, 70%, 55%. How would you do it? Discuss." (C16, Math Talk): methods discussion, not a single answer.
- p8 Activity "How Close Can You Get?" (C19): a game for pairs with no definite answer.
- p15 to p16 tomato (₹30 to ₹42) and footfall (160 to 100) percentage change (C41 b4, b5): worked illustrations of the definition, not put to the reader.
- p17 Kishanlal's profit of ₹130 (C46 b3), p18 gross and net profit (C54 b3) and Manisha's 50% against 33.33% (C55): worked illustrations of statements, not questions.
- p17 "Could we have just calculated the loss percentage per kg instead? Would it be the same?" (C51 b1, ref ex5_per_kg): a reflective yes/no question; left so the concept is not emptied (Judgement call 2).
- p19 "You may share any bills you have at home with the class" (C57, Try This): open sharing.
- p21 "What do you understand by this statement? What is the 'p.a.'?" and the ₹6000 at 10% illustration (C66 b3): discussion plus an illustration.
- p24 Decline Math Talk (bike value factors): discussion, no block.
- Chapter opener sentences, "Percentages Around Us", the history of per cent, Summary and Peaceful Knights: statements, history and a puzzle in the Summary topic (the engine cannot use a Summary as a source; the end-of-chapter FiO 1 in C84 stays there).

## Gaps (book questions the plan has no question block for)

- Example 1 (p1 to p2), 3/4 of the paint is red, what percentage: ref 1.1.ex1 sits on C4, but its working is only in the textbook text and guided discovery; no worked_example block.
- Example 2 (p2), 2/5 of the prize money as a percentage: ref 1.1.ex2, same.
- Example 3 (p3), express 24% as a fraction: ref 1.1.ex3 on C5; the only worked example there is the plan's own 40% one.
- Example 9 (p23), the amount for t years, without and with compounding: ref 1.3.ex9 on C69; the derivation is only in text. The block "Math Talk: total interest" answers the Math Talk, which was moved.

## Judgement calls

1. T12 is held back (see the top of this file) because a new Questions topic typed like this chapter's own makes the skeleton and objectives gates worse than live. Its five questions are ready in the block above.
2. Two multi-block enrichment concepts were not emptied. The engine keeps a concept even when every block is cut out, and it cannot drop it, so cutting all blocks would leave a teaching concept with a video and no content. C15 "Fill the Mental Table" holds the same table three times (ids free_hand_table, free_hand_40, free_hand_15, identical question and answer): b0 is the question, b1 and b2 stay. C51 "Raghu's Old Rice" holds Example 5 and its per-kg follow-up: only Example 5 is cut and the follow-up stays (it also reads as a reflective question). If the engine can drop emptied concepts later, both leftovers can move (the three free-hand blocks would then be one question with the ids folded by `canon`; the per-kg block would fold into Example 5 with `canon` {"1.3.ex5_per_kg": "1.3.ex5"}).
3. Book order was followed where it differs from "in-text first, Figure it Out last": in 1.1 the biscuit question is printed after Figure it Out 5, so it comes after Q5; in the compounding section Figure it Out 1 to 3 follow Examples 7 and 8, the Math Talk formula question sits between Q3 and Q4, and Examples 10 and 11 (Decline) come after Q9. The kept concepts were re-listed in book order where the live order was not (1.2 Q1 first; buy-and-sell Q3 and Q7 in place).
4. In the live plan Figure it Out 1.3 is split across two Questions topics (items 5, 8, 11, 12 after "compare and change"; the rest after "buy and sell"); that split is the plan's own and is kept. The book prints the second page of those items numbered 3 to 9 (a misnumbering), and the plan's block text repeats it, while the concept names follow the plan's own 1 to 12 sequence (Q6, Q7, Q9 ...); nothing was renamed.
5. Tier calls: the printed Examples are `example`; "Example 2: Decimal multiplier for 10%" is `example` because the plan ties it to ref ex2 even though what is asked is the in-text follow-up. The yellow-paint, Method 3, biscuit, free-hand, table, "find the profit percentage", notebooks, crayons, strawberries, cooker, bill and Math Talk formula questions are `prompt`. No new `exercise`: all Figure it Out items already exist as question concepts.
6. Example 6 is built from the block "Days 1 to 4" only. The follow-ups for days 5 and 6, days 7 and 8 and the table are separate in-text requests with their own plan blocks and videos, so each is its own question.
7. The Math Talk icon was not treated as decisive: the formula question (p24) counts because it has a definite answer and the plan has a block; the discussion-only Math Talks (p7, p8) do not.
8. One kept concept is pure discussion ("Do you observe anything interesting in the solutions of the two questions above? Share and discuss", 1.3 Figure it Out 3 of the compounding set, C73 live), and 1.2 Q8 (the bull and the fodder, Math Talk) is largely open; the engine never drops an existing question concept, so both stay.
9. Plan values that differ from the book's printing: Example 5's loss is "about 14.29%" in the plan against 14.28% in the book (the plan's own note says the book cuts off rather than rounds); Example 4's 43.3% is "about 43.33%". Both are the same value, so nothing was withheld. All other plan answers of the moved blocks were checked against the book and its figures (KYC labels, the p16 price chain, the p19 bill) and agree.
10. `canon` is empty: every new question is one block (or one whole concept) with one id. `rename_teach` is empty: no teaching concept is named after a moved example (the whole-moved concepts take their new names), and no kept concept name carries "page N" (the structure gate reports 0 problems before and after); the kept names ("FIO 1.1 Q1", "Q5", "FIO 3", "9" and the like) are the chapter's existing style.
11. Figures (q_figure and s_figure) are set only where the printed question depends on a picture or table: Method 3 bar, the free-hand table, the FDP table, the past-100 table and number line, the badam labels, the sweater price chain, the bill, and kept 1.1 Q4, 1.2 Q1 and Q2. The q_figure sentences hold only what the page gives (values, labels, empty boxes) and none of the results.
