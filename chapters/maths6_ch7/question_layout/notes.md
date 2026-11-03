# Class 6 Ch 7 Fractions (cbse_eng_maths6_ch7, live v29): question layout notes

Spec: `layout_spec.json`. Result of `check`: 70 question concepts in 11 Questions topics (46 existing kept in book order
+ 24 new: 7 example, 0 exercise, 17 prompt), 7 new videos needed (the questions cut out by block), 17 live videos kept
(every whole-moved concept keeps its own video, each covering its whole question), 12 teaching concepts edited. Gates:
structure 0 to 0, coverage 20 to 0, video_script_rules 109 to 106, skeleton 3 to 3, objectives 0 to 0 (no gate worse than
live). No SPEC PROBLEMS.

**INTEGRITY is not clean, and it cannot be made clean by a spec.** The live plan v29 is already broken from
`M3.S19.T19.C95` on: the `media_ids` of every concept from there to the Summary, and the `video_media_id` of their blocks,
use the old numbering (one higher than the concept id, a concept of the topic Adding Fractions was dropped), while the
media nodes in the topics were renumbered; 5 `video_coverage` entries point at ids that do not exist. A no-op spec
(`"topics": []`) prints the same 31 problems in the same five kinds (13 media not named after their concept, 5 blocks
pointing at a missing video, 7 concepts listing missing media, 5 video_coverage entries missing, 1 rendered video url
count 104 expected / 101 found), and this spec prints exactly the same 31 with no extra one. Fixing it needs a repair of
the live plan (re-link `media_ids`, `video_media_id`, `video_coverage` to the node ids), which is outside this task. One
consequence for the spec: nothing from the Questions topics after Adding Fractions is moved whole, because a whole-move
would carry the stale video id and attach the neighbouring question's video. All Figure it Out concepts there are `keep`.

## How a book question was recognised here

The book marks reader questions with a round icon (the one printed on every "Figure it Out" heading; checked on the PDF
pages 152 to 185) and prints answers for them in its solutions section. Counted:

1. a printed "Example:" (7.6 once, 7.8 six times);
2. an in-text question with the icon and a definite answer, which the book also lists in its solutions section;
3. an in-text blank to fill with a definite answer that the next sentence does not already give (7.3 "Do it once more!",
   7.6 "Write them in the boxes", "write down the share of each child"), and the one unanswered question that ends the
   Meena chikki paragraph.

Not counted: a question the book asks and then answers in the very next lines or figure (7.2, 7.3, 7.4, 7.5 lead-ins,
the Jaya and Mukta/Shabnam dialogues), observation and discussion questions, hands-on paper-strip work, and worked
illustrations in the running text that carry no label, no icon and no entry in the book's solutions. The plan tags every
one of these as a worked example with an id like 7.5.ex3, so the ids say nothing about whether the book treats the item
as a question.

## New questions

All 24 sit in the Questions topic of the concept topic they came from, in book order, before or between the existing
Figure it Out items as the book prints them. `Whole` = a thin-extra concept moved with its video; `b2` = the worked-example
block cut out of a teaching concept (new video needed).

| # | New question concept | Book label or quote | Plan source (ref) | Tier | Why it counts |
|---|---|---|---|---|---|
| 1 | Chikki Pieces: are the six pieces equal? | 7.2 "By dividing the whole chikki into 6 equal parts in different ways, we get 1/6 chikki pieces of different shapes. Are they of the same size?" | M1.S4.T4.C12 whole (7.2.q1); video kept | prompt | Icon-marked; book key: yes, same size. Has q_figure. |
| 2 | Folding a Strip: eighths | 7.3 "Do it once more! Fill in the blank boxes." (strip folded into 8 parts) | M1.S6.T6.C18 whole (7.3.q1); video kept | prompt | Blank boxes with one definite answer (1/8 up to 8/8 = 1); not icon-marked and not in the key, counted as a blank to fill. Has figures. |
| 3 | Number Line: blue line in thirds | 7.4 "1. Here, the fractional unit is dividing a length of 1 unit into three equal parts. Write the fraction that gives the length of the blue line" | M1.S8.T8.C27 whole (7.4.q1); video kept | prompt | Numbered, icon-marked group; key 2/3. Has figures. |
| 4 | Number Line: blue lines in fifths | 7.4 "2. Here, a unit is divided into 5 equal parts. Write the fraction that gives the length of the blue lines" | M1.S8.T8.C28 b2 (7.4.q2); new video | prompt | Same group; key 2/5 and 4/5. Has figures. |
| 5 | Number Line: marks in eighths | 7.4 "3. Now, a unit is divided into 8 equal parts. Write the appropriate fractions" | M1.S8.T8.C29 whole (7.4.q3); video kept | prompt | Same group; key 1/8, 2/8, 3/8 and so on. s_figure only. |
| 6 | Fraction Wall: are 1/2 and 3/6 equal? | 7.6 "Answer the following questions after looking at the fraction wall: 1. Are the lengths 1/2 and 3/6 equal?" | M2.S12.T12.C53 whole (7.6.q3); video kept | prompt | Icon-marked, numbered; key yes. Has the wall as q_figure. |
| 7 | Fraction Wall: are 2/3 and 4/6 equivalent? | same list, "2. Are 2/3 and 4/6 equivalent fractions? Why?" | M2.S12.T12.C54 whole (7.6.q4); video kept | prompt | key yes, equal on the wall. |
| 8 | Fraction Wall: sixths that make 1/2 | same list, "3. How many pieces of length 1/6 will make a length of 1/2?" | M2.S12.T12.C55 whole (7.6.q5); video kept | prompt | key 3. |
| 9 | Fraction Wall: sixths that make 1/3 | same list, "4. How many pieces of length 1/6 will make a length of 1/3?" | M2.S12.T12.C56 whole (7.6.q6); video kept | prompt | key 2. |
| 10 | Equivalent Fractions: four more for 1/2 | 7.6 "Find some more fractions equivalent to 1/2. Write them in the boxes here" (four boxes) | M2.S12.T12.C60 b2 (7.6.q9); new video | prompt | Four blank boxes, definite property, answer not given in the text. Placed after the second block of Figure it Out items, where the book prints it. |
| 11 | Equivalent Fractions: rotis shared among children | 7.6 "Equally divide the rotis in the situations shown below and write down the share of each child. Are the shares in each of these cases the same? Why?" | M2.S12.T12.C61 whole (7.6.q10); video kept | prompt | Boxes to fill; answers 2/3, 4/6, 6/9, same. Has figures. |
| 12 | Example 1: Lowest terms of 16/20 | 7.6 "Example: Is the fraction 16/20 in lowest terms? ... reduce 16/20 to lowest terms" | M2.S14.T14.C71 b2 (7.6.ex5); new video | example | Printed Example. |
| 13 | Comparing Fractions: 1 chikki or 5 chikkis | 7.6 "In which group will each child get more chikki? 1 chikki divided between 2 children or 5 chikkis divided among 8 children." | M3.S16.T16.C75 b2 (7.6.ex2); new video | prompt | Icon-marked question put to the reader; the book's dialogue is its working; definite answer (second group). |
| 14 | Comparing Fractions: 1 chikki or 4 chikkis | 7.6 "What about the following groups? In which group will each child get more? 1 chikki divided between 2 children or 4 chikkis divided among 7 children." | M3.S16.T16.C76 whole (7.6.ex3); video kept | prompt | Same, icon-marked; answer second group. |
| 15 | Comparing Fractions: more units, same children | 7.6 "Suppose the number of children is kept the same, but the number of units that are being shared is increased? What can you say about each child's share now? Why?" | M3.S16.T16.C77 whole (7.6.q12); video kept | prompt | Icon-marked and in the key (each child's share is larger). See judgement call 4. |
| 16 | Comparing Fractions: juice for two groups | 7.6 "Now, decide in which of the two groups will each child get a larger share: 1. ... 2. ... Which groups were easier to compare? Why?" | M3.S16.T16.C78 b2 (7.6.q13); new video | prompt | Icon-marked, numbered, in the key (group 1; group 2; the second pair is easier). One block already holds both parts and the "easier" part, so one question. |
| 17 | Adding Fractions: how much chikki is left? | 7.8 "How much of the total chikki is remaining?" (last line of the Meena paragraph) | M3.S18.T18.C88 whole (7.8.q2); video kept | prompt | Put to the reader, answer 1/4 not printed anywhere in the text. |
| 18 | Example 2: Sum of 2/5 and 1/5 | 7.8 "Example: Find the sum of 2/5 and 1/5." | M3.S18.T18.C89 whole (7.8.ex1); video kept | example | Printed Example. s_figure: the strip model. |
| 19 | Example 3: Sum of 4/7 and 6/7 | 7.8 "Example: Find the sum of 4/7 and 6/7." | M3.S18.T18.C90 whole (7.8.ex2); video kept | example | Printed Example. s_figure: the strip model. |
| 20 | Adding Fractions: 4/7 + 6/7 on a number line | 7.8 "Try adding 4/7 + 6/7 using a number line. Do you get the same answer?" | M3.S18.T18.C91 whole (7.8.q3); video kept | prompt | Icon-marked; key: yes, 10/7 = 1 3/7. s_figure only. |
| 21 | Example 4: Sum of 1/4 and 1/3 | 7.8 "Example: Find the sum of 1/4 and 1/3." | M3.S18.T18.C92 b2 (7.8.ex3); new video | example | Printed Example; the teaching concept keeps the text and its plan. |
| 22 | Example 5: Sum of 2/3 and 1/5 | 7.8 "Example: Find the sum of 2/3 and 1/5." | M3.S18.T18.C93 whole (7.8.ex4); video kept | example | Printed Example. |
| 23 | Example 6: Sum of 1/6 and 1/3 | 7.8 "Example: Find the sum of 1/6 and 1/3." | M3.S18.T18.C94 whole (7.8.ex5); video kept | example | Printed Example. |
| 24 | Example 7: Difference of 3/4 and 2/3 | 7.8 "Example: What is 3/4 − 2/3?" | M3.S20.T20.C100 b2 (7.8.ex6); new video | example | Printed Example. Sits between the two blocks of subtraction Figure it Out items, where the book prints it. |

Order inside each Questions topic (the existing Figure it Out concepts are `keep`, in book order): Fractional Units as
Parts of a Whole = row 1, then FiO; Measuring Using Fractional Units = row 2, then FiO Q1 to Q5; Marking Fraction Lengths
= rows 3 to 5, then FiO Q1 to Q5; Equivalent Fractions = rows 6 to 9, FiO Q1 to Q3 (first block), FiO Q1 to Q3 (second
block), rows 10 and 11, FiO Q1 (third block); Fractions in Lowest Terms = row 12, then FiO; Comparing Fractions = rows 13
to 16, then the in-text exercise on pairs and FiO Q1 to Q3; Adding Fractions = rows 17 to 23, then FiO Q1 to Q3;
Subtracting Fractions = FiO Q1 to Q3 (same denominator), row 24, FiO Q1 to Q3 (different denominators). The topics for
7.1, 7.5 and 7.9 are not in the spec and keep their 5, 6 and 3 existing concepts unchanged (no counted question there
is a new one).

Existing kept concepts carrying figures (the printed question depends on a picture): FiO 7.2 Q1 (eight chikki pieces,
C15), FiO 7.3 Q5 (four shaded circles, C25), FiO 7.4 Q1 (s_figure only, C31), Q4 and Q5 (number lines with black lines,
C34, C35), FiO 7.6 second block Q1 (three rotis and four children, C67). Everything else is text-only.

## Borderline, not moved

- 7.0.ex1 opening dialogue (C2 b2) and 7.1.ex1 "Which fraction is greater, 1/5 or 1/9?" (C3 b2): characters ask and answer, no icon.
- 7.1.q1 words for fractions in your home languages (C4): open survey, answers vary.
- 7.2.ex1 "How much of the original chikki is each piece?" (C11 b2) and 7.2.ex2 "What is the fractional unit of chikki shown below?" (C13 b2): no icon, the book answers in the next lines (3/4 and 1/4; 1/3).
- 7.3.ex1, ex2 (C16 b2, C17) folding the strip: answered by the figure; 7.3.ex3 "another example" table of half rotis (C19 b2): narration, its practice is FiO Q1.
- 7.4.ex1 first blue line (C26 b2): box to fill but answered in the next paragraph; it models questions 1 to 3 above.
- 7.5.q1 write down and classify the fractions you marked (C36 b2): depends on what the student marked, no icon, no key. 7.5.q2 "Did you notice something common?" (C37): icon-marked, a discussion answered in the next paragraph.
- 7.5.ex1 to ex6 (C38, C39, C40 b2, C41, C42, C43): 3/2 and 5/2 whole units, "4/3 > 1", 4/3 = 1 + 1/3, 8/3 = 2 + 2/3, 3 + 3/4 = 15/4: demonstrations or dialogue answered in the text; the printed questions on the same ideas are the FiO items.
- 7.6.q1 "What do you observe?" two bullet questions (C51 b2): speech bubble, answered by "1/2 = 2/4 = 4/8" right after. 7.6.q2 check 1/3 and 2/6 with paper strips (C52): hands-on, no icon, no blank, no key.
- 7.6.ex1 one roti among four children and the three facts (C57 b2): narration; FiO Q1 and Q2 are the printed practice.
- 7.6.q7 "if there are 10 children in my group, how many cakes will I need?" (C58): a speech bubble inside the box of FiO Q3, answered on the next page ("So 2/5 = 4/10!"); it stays as an extra of the teaching topic.
- 7.6.q8 "Let us draw and share" (C59): answered in the sentence that follows (1/2 = 2/4 = 3/6). 7.6.q11 relationship between numerator and denominator (C62): observation.
- 7.6.ex6 36/60 in steps (C72), 7.7.q1 "Which is greater, 4/5 or 7/9?" (C80), 7.7.q2 "Let us try this for another pair: 7/9 and 17/21" (C81): worked illustrations in the running text with no label, icon or key entry. The nearest candidates to promote if a later pass wants every worked case as a question.
- 7.6.ex4 3/4 against 7/10 (C79): the book's own working of group 1 of question 16; it stays beside the teaching concept (see judgement call 6).
- 7.8.q1 Meena and her brother eat together (C87 b2): asked and answered by the narrative; 7.8.q4 "what is 6/7 − 4/7?" (C98 b2): worked with strips in the text; 7.8.q5 "Try doing this same exercise using the number line" (C99): no icon, not in the key, the answer is printed just above (contrast with row 20).
- 7.8.q6, q7 "Think! Why did we choose to multiply by 3 / by 4?" (C101, C102): thought-bubble reasoning prompts, not in the key.
- 7.9.q1 "Do you know what a fraction was called in ancient India?" (C110 b2): history, answered in the text.

## Gaps

No counted book question is missing from the plan: every example, icon-marked question and blank above has a block, and
every Figure it Out item has a concept. The only structural problems are the live-plan link damage described at the top
and one cosmetic point: the existing question concept `M3.S17.T17.C83` (the in-text exercise on pairs with the same
fractional units, book page 172) sits in the Comparing Fractions Questions topic, although the book prints it before
Fractions in Lowest Terms; an existing question concept cannot change topic in this engine, so it is kept where it is.

## Judgement calls

1. The criterion above is stricter than "a question put to the reader" for items the book answers in the next sentence,
   and wider than "icon only" for the three blank-box items (rows 2, 10, 11). To drop them, delete those entries; nothing
   else changes. To add the unlabelled worked cases later: 7.6.ex6, 7.7.q1 and 7.7.q2 are thin-extra concepts (C72, C80,
   C81, move whole); 7.8.q1 and 7.8.q4 are blocks (C87 b2, C98 b2).
2. The book's "Example" is unnumbered; the seven are numbered 1 to 7 in book order across the chapter.
3. Rows 13, 14 (the chikki groups) are tier prompt, not example: the book prints no "Example" label, it asks the question
   with the icon and solves it as a Mukta and Shabnam dialogue.
4. Row 15 is phrased "What can you say ... Why? Discuss how your reasoning explains ...". Counted because the book lists
   an answer for it in its solutions (each child's share becomes larger) and the plan block has the steps; a pure
   "discuss" would not count.
5. Row 17 is counted although it has no icon: it is the only unanswered question of the Meena paragraph and the plan
   block (C88) is exactly it.
6. Row 16 is one question holding groups 1 and 2 and the "easier to compare" part (one block, one ref 7.6.q13). The
   book's dialogue that works group 1 (7.6.ex4, C79) was not folded into it: the block already carries the working, and
   C79's video covers only group 1.
7. Row 10's plan answer is one choice of four ("for example 4/8, 5/10, 6/12, 7/14"); any four equivalent fractions are
   right, as the book says for its own FiO 7.6 Q2 and Q3 ("try for other options also").
8. `canon` and `rename_teach` are empty: no moved question needed ids folded (one block or one concept each) and no
   teaching concept is named after a moved example. Several teaching concepts (C28, C60, C71, C75, C78, C92, C100) now hold
   only their text and teaching plan; their own videos stay and still talk through the example that moved out, until the
   question video is made (7 new videos: rows 4, 10, 12, 13, 16, 21, 24).
9. figures: q_figure and s_figure are set only where the printed question depends on a picture (the chikki cuttings, the
   strip and number lines, the fraction wall, the rotis, the circles); descriptions were taken from the PDF pages 154,
   156 to 160, 164, 166, 168 and 176 to 177.
