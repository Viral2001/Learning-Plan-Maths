# Class 7 Ch 13 "Connecting the Dots..." (cbse_eng_maths7_ch13, live v31): question layout notes

Spec: `layout_spec.json`. Book text `gegp205` (Part II chapter 5), printed pages 97 to 135.

## READ FIRST: the check cannot go clean, for a reason the spec cannot fix

`check` ends with `INTEGRITY: 9 problem(s)` and `GATES WORSE THAN LIVE: {'structure_problems': (0, 8)}`. All of it is one cause,
and it is there with an EMPTY spec too (tested: `"topics": []` gives the identical 9 and 8):

- 8 existing Figure it Out concepts already carry a concept image `<concept id>.IMG1` (a plain "image" node, no
  `image_role`, status placeholder, e.g. the empty dot plot of FiO2 Q3). `placeholders.add` then creates the question
  card with the same id `<concept id>.IMG1`, so the plan gets a duplicate media id (gate "structure: duplicate media id")
  and the concept's media list no longer starts with a question card ("question image must be first").
- The 8 concepts (live ids): M2.S10.T10.C35, C37, C38 (FiO2 Q3, Q5, Q6), M3.S14.T14.C49, C52 (FiO3 Q1, Q4),
  M4.S17.T17.C60, C67, C69 (FiO4 Q1, Q8, Q10).
- The spec has no lever for it: `keep` is the only way to keep them, `whole` is refused for a concept with an image,
  and cutting their block with `block` would drop their live video. I did not touch the engine.
- What is needed is an engine change in `core/solutions/placeholders.py` (retire or re-id a non-card `IMG1` of a question
  concept, since the new `q_figure` replaces it). To make that lossless I gave those 8 concepts a `q_figure` that matches
  the live image description (and an `s_figure` where the answer is a drawn graph).
- Everything else is clean: `SPEC PROBLEMS` empty, coverage 0, objectives 0, skeleton 3 and video_script_rules 59 are the
  same as live, and the only 8 structure problems are the duplicate ids above.

## Result of `check`

43 question concepts in 10 Questions topics: 29 existing kept in book order (FiO1 5, FiO2 7, FiO3 4, FiO4 13) plus 14 new,
all tier prompt (0 example, 0 exercise). 13 new videos needed; 1 live video kept (C22, moved whole); 0 folded. 13 teaching
concepts lose one block. Six Questions topics are new (the 4 live ones, after Average as a Fair Share, Zero No Value and
Choosing the Data, All it Takes is a Minute and Zoomed Charts, stay): they follow Statistical Statements and Statistical
Questions, Outliers and the Median, Of Ends and the Essence, Clubbing the Columns, Telling Tall Tales and Puzzle Time.
Nothing moves out of Who Batted Better, Know Your Onions or Summer and Winter at the Same Time, so they get no Questions
topic. The framing and summary topics are left alone.

The chapter has no printed "Example" and every Figure it Out item is already a concept, so the new questions are all
in-text "?" prompts. No `canon` is needed (no printed question was split across ids) and `rename_teach` is empty: no
concept name carries a page number, an exercise number or the name of a moved example (checked every name; "Newspaper
pages: when mean and median are close" has no digit after "pages", and none of the new names has one).

## How a book question was recognised here

In this edition a round orange "?" icon sits beside the lines the book puts to the reader (it is also printed next to
Figure it Out and next to some Math Talk). I located every icon on the PDF (pages 98 to 128) and read each one against
its text, then decided by substance as the brief says: a definite answer, and a plan block with that question's numbers,
steps and answer. The icon alone did not decide: many "?" lines are opinions or discussion. A plan block whose question
is the plan's own consolidation of a narrated passage stays in teaching.

## New questions (every plan source is a `worked_example` block, `b2`; all have `keep_video_of: null` except row 5)

| # | New question concept | Book label or quote (printed page) | Plan source (ref) | Tier | Why it counts |
|---|---|---|---|---|---|
| 1 | Statistical Questions: sorting the seven | p98 "Which of the following are statistical questions? (a) tennis ball ... (g) rainfall pattern in Barmer" | M1.S2.T2.C4 b2 (5.1.mathtalk_statq) | prompt | seven-part sort, one definite answer per part; the block lists the same seven. Ref 5.1.questions_def (the definition) stays on C4. See judgement call 7. |
| 2 | Fair Share: guavas in two groups | p100 "... In which group will each member get a bigger share of guavas?" | M1.S4.T4.C9 b2 (5.2.fair_share) | prompt | "?" icon, same numbers, definite answer (6 against 5, printed in the book). |
| 3 | Fair Share: hibiscus flowers per day | p100 "... What is the average number of Hibiscus flowers blooming per day in Vaishnavi's garden?" | M1.S4.T4.C10 b2 (5.2.hibiscus) | prompt | "?" icon, answer 5 (printed). Ref 5.2.history_samamiti stays on C10. |
| 4 | Heights of a Family: mean and median | p105 "Find the average height of each family. Can we say that Yaangba's family is taller than Poovizhi's?" and p106 "does the median represent the heights of the families better than the average?" | M2.S7.T7.C21 b2 (5.2.family_height) | prompt | two "?" questions on one data set; the block has both, with the book's numbers (164.3 and 160.2, medians 164.5 and 170). Ref 5.2.median_def stays on C21. |
| 5 | Heights of a Family: without the outlier | p107 "Find the mean and median in Poovizhi's data without the outlier value 118. What change do you notice?" | M2.S7.T7.C22, whole (5.2.outlier_def); video kept | prompt | "?" icon; C22 is a thin-extra single block with its own video and moves whole. q_figure gives the five heights because the plan's question text does not. |
| 6 | Bookworm: mean and median of stories read | p107 "Are you a bookworm? ... Find the mean and median number of short stories read" and p108 "Find the mean and median in the absence of the outlier. What change do you notice?" | M2.S7.T7.C23 b2 (5.2.bookworm) | prompt | two "?" lines, one block. The 15 values were checked against the printed slips (median 6, as the book says). |
| 7 | Newspaper Pages: mean and median of the week | p108 "... 16, 18, 20, 22, 26, 16, 10. Mark the data, the mean, and the median on the dot plot below." | M2.S7.T7.C24 b2 (5.2.same_page) | prompt | "?" icon, definite answers (about 18.29 and 18). Refs mathtalk_mean_median and central_tendency stay on C24 (discussion). |
| 8 | How Tall is Your Class: students above the mean | p110 "How many students are taller than the class' average height? How many boys are taller than the class' average height?" | M2.S8.T8.C26 b2 (5.2.grade5_heights) | prompt | two "?" lines with definite counts (15 and 8, recounted from the table); the block also carries the boys against girls comparison that precedes them. See judgement call 5. |
| 9 | Rocket Launches: organisations that grew every year | p118 "List the organisations that have consistently launched more rockets every year." | M3.S11.T11.C41 b2 (5.3.rockets) | prompt | "?" icon, definite list (SpaceX, ISRO, Galactic Energy; checked on the printed graph). |
| 10 | Rocket Launches: justified statements and the 2023 total | p118 "Identify which of the following statements can be justified using this data (a) to (f)" and "Estimate the total number of rockets launched worldwide in 2023 (a) to (d)" | M3.S11.T11.C42 b2 (5.3.rockets_more) | prompt | two "?" lines in one plan block, so one concept and one ref. The block's question omits the statements and options, so q_figure carries them. See judgement call 6. |
| 11 | Runs per Over: four questions on the graph | p122 "Answer the following questions based on the graph: 1 ... 4" | M3.S13.T13.C47 b2 (5.3.cricket) | prompt | numbered questions, one block, definite answers (read off the printed graph: blue batted first, red won; blue 15 in over 12; red lowest in over 4; the target needs all 20 bars). Placed before FiO3. |
| 12 | Heights in India: which statements are justified | p127 "Which of the following statements can be justified using the data? 1 to 6" | M4.S15.T15.C54 b2 (5.4.india_table) | prompt | definite verdict per statement (recomputed from the table). The block's question omits the statements, so q_figure carries them. |
| 13 | Heights in India: growth and estimates | p128 "In 2019, between which two successive ages ... did boys grow the most? ... girls?", "Estimate the average height of young children of ages 1 to 4", "write your estimates ... in the year 2029" | M4.S15.T15.C55 b2 (5.4.india_growth) | prompt | three "?" lines in one block; the first has a definite answer (boys 12 to 13, 6.2 cm; girls 10 to 11, 5.8 cm, rechecked). See judgement call 4. |
| 14 | Number Lock: find the code | p135 "A number lock has a 3-digit code. Find the code using the hints below." | M5.S18.T18.C73 b2 (puzzle.lock) | prompt | a puzzle with one definite answer. The five clues in the block match the printed ones; the code 415 satisfies all five. C73 keeps its text, teaching plan, image and video. |

Placement: every new question comes before the Figure it Out items of its topic and in the order the book prints them,
except the two rocket questions (judgement call 6).

## Borderline, not moved

- Opening guess (p97) "What is your guess as to each friend's gender?": no icon, answered in the next sentence, and the plan holds it only in the framing topic, which the engine cannot use.
- Series 1 (p98) "Who do you think performed better?": "?" icon but an opinion; the book gives three children three answers and no verdict. C6 b2 ("Yashasvi batted better") is the plan's own conclusion, so it stays in teaching.
- Series 2 (p99) "Who do you think performed better in this series?", "What do you think of Vaishnavi's statement?", "Can a single number act as a representative ...? Discuss.": discussion. C7 b2 is the plan's mean computation. Note the book prints Shubman's mean as 110 ÷ 5 = 21; it is 22, as the plan has it.
- Know Your Onions (p101) "Where are onions costlier, according to you?" and (p102) "Can you think of any other ways to compare the data?": opinion and open. C17 b2 is the plan's five-measure comparison with its own verdict ("Yahapur"), which the book never gives.
- "What else do you wonder about?" (p104), "What are you curious to know ...?" (p118), "Is there anything more that you wish to explore?" (p121): open.
- Dot plot (C18 b2): the book draws the plot itself; the plan's "draw it" task is its own. Its two yes/no checks are under Gaps.
- Averages Around Us (p104 to 105): statements, no question.
- Variability of three examples (p108) and "Discuss the effect on the mean and median when outliers are present on both sides" (p109, Math Talk): reading and discussion, no single answer.
- "What can we infer from the dot plots and the central tendency measures?" (p110): its content (boys against girls) rides inside moved question 8.
- "How long is a minute?" "Discuss how well both the groups fared" (p110, Math Talk): discussion. C27 b2 ("the second group was slightly better") is the plan's own conclusion.
- Zero Median Runs Scored (p111) "can a team's median runs ... be 0 but the team's total score be 407/10?": no icon, and the plan answers it with batting scores of its own invention (19, 0, 0, 22, 158, ...) that the book does not give, so C29 b2 stays as a plan example.
- Zero vs No value, Sita's mangoes, A Mean Foot (p111 to 112): the book narrates the working and puts no question to the reader; C30 b2 and C31 b2 are plan-authored questions on that narration.
- Rockets "Share your observations" and the Step 2 instructions "Analyse and interpret each of your observations" (p116, p117, p119): open instructions. The same for "Share appropriate summary and conclusion statements" and "Does this give some idea of where these two cities are located?" (p119, p120); C44 b2 (divide the monthly hours by the days) and C45 b2 (the book's inference bullets) stay in teaching.
- Telling Tall Tales (p125) "What do you notice?", "Spend sufficient time observing the data ... Share your findings" (p127), "How is the graph organised? ... What do you find interesting?" (p128): open. C53 b2 is the plan's own comparison, C57 b2 uses numbers of its own (165 cm and 155 cm), C58 b2 builds a question on a picture that carries none.
- FiO items that are activities or projects (FiO1 Q2, Q3, FiO4 Q6, Q9, Q11 to Q13) stay as the existing concepts they are: the engine never drops them.

## Gaps (counted book questions the plan has no matching block for)

- p103 "Does this visualisation capture all the data presented in the tables earlier?" and "Looking at it, can we tell the price of onions in Yahapur in the month of January?" (two "?" icons, answers no and no): the answer sits only as the last step of C18 b2 (ref 5.2.dotplot_questions), whose question is a draw-the-plot task the book does not set.
- p104 "Find the average price of onions at Yahapur and Wahapur." ("?" icon, definite): the plan has it only as step 4 of C17 b2 (refs onions_opinions, onions_measures), a comparison by four measures.
- p115 "What is the scale used in this graph?" and "Is it now easier to compare month-wise prices in both places?" (clustered column graph, "?" icons): C40 b2 asks the student to draw the graph with 1 unit = 10 rupees instead; the printed questions have no block.

## Judgement calls

1. The engine problem at the top: spec complete, check not clean, nothing outside the two output files edited.
2. Thirteen teaching concepts lose their only worked example (C4, C9, C10, C21, C23, C24, C26, C41, C42, C47, C54, C55, C73). They keep their text, teaching plan, objective, image and live video; those videos still walk through the example that is now a question, and the 13 new questions have no video yet. Nine teaching concepts (C9, C23, C26, C41, C42, C47, C54, C55, C73) end with no ref of their own, as in the earlier chapters; coverage stays complete because the new question concepts carry the refs.
3. Question 5 moves C22 whole with its video; it moves out of the teaching topic and its refs leave C21. The question-4 and question-5 split follows the two separate "?" lines on p105 and p107.
4. C55's block covers three printed questions but narrows the 2029 estimate to one age (12), where the book asks for ages 5 to 19, and its estimates for ages 1 to 4 (75, 87, 95, 101) are approximate. Moved because the first printed question is definite and fully answered; the estimates are not a single answer, so treat them as a guide.
5. C26: the plan's class mean is 144.5 (4046 ÷ 28 = 144.5 exactly); the book prints 144.4. The counts (15 students, 8 boys) are the same either way.
6. The two rocket blocks cannot follow the book's exact order (statements, then the list, then the estimate) because the statements and the estimate share one block. I put the list first (it is the easier reading task and C41 comes before C42 in the lesson), then statements and estimate.
7. C4 (f) "Who was the best bowler in the match yesterday?" is counted statistical by the plan. This repository holds no answer key for the chapter, so I could not compare it with the book; it is the one verdict I could not check.
8. q_figure was written for questions whose printed form depends on a graph, table, dot plot, picture or on text the plan block omits (C22 data, C42 statements, C54 statements). It states only what the question gives. The two heights tables (rows 12 and 13, 15 columns by 8) are named, not copied, because they are in the book. s_figure is set where the working is a drawn graph or plot (rows 6, 7, 11, 14 and the kept items FiO2 Q3, Q5, FiO3 Q2, Q3, Q4, FiO4 Q4, Q10).
9. The 8 kept concepts that already have a live figure carry a q_figure that reproduces what that figure shows (checked against the PDF, e.g. FiO4 Q8 leaves New York, Tokyo and London unlabelled, FiO4 Q10's axis runs 220 to 400 as printed).
