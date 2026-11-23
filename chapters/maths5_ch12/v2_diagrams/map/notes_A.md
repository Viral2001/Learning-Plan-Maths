# Notes for chunk A (Class 5 Ch 12 "Racing Seconds")

Chunk A = 19 units (6 worked examples, 13 pairs), 32 items: required 9 (5 question, 4 solution), optional 6 (2 worked, 4 solution), none 17.
Validator: errors 0; 4 warnings, all of the kind "required solution, no book figure maps to it" (the clock and winners'-stand solutions are
not printed in the book, so this is expected). The pdf has no printed-solutions section, so every solution decision follows the LP steps.

## What is drawn

- Raghav's two wall clocks (book p.1): question diagrams for Q1, Q2, Q3 (C6, C8, C10; identical specification, three images), solution
  diagrams for Q1 and Q2 (C7: first clock marked, 05:35 a.m.; C9: second clock marked, 05:55 a.m.).
- School Race winners' stand (book p.2): question diagrams for both School Race questions (C28, C30; identical), solution diagrams C29
  (a tag "55 / 56 / 57 seconds more" under each stand) and C31 (winner on stand 1 circled, board 01:55 boxed, "1 minute 55 seconds").
- Hands on the clocks are computed from the times (35 min = 210 deg, 55 min = 330 deg, hour hand 5 x 30 + minutes x 0.5 = 167.5 and
  177.5 deg). The book draws the hour hands only roughly; the specification uses the exact angles (agrees with the LP: "between 5 and 6"
  and "just before 6"). Hand colours follow the LP words: short blue hand = SET_A, long orange hand = SET_B.

## Judgement calls (unsure items)

1. C6/C8/C10 captions "Before yoga" / "After yoga" under the two clocks. The book tells the learner which clock is the start and which is
   the finish only through Raghav's pose (standing, then sitting). The diagram has no people, and the LP question text does not mention the
   clocks at all, so without a caption the question would be ambiguous. The prompt lists "captions" as not allowed, but these are
   category labels the figure needs (the concept image M1.S1.T1.C1.IMG1 uses the same two labels). Easy to remove if the content team
   disagrees; the solutions say "first / second clock".
2. Podium pictograms (C28 to C31). The children are decoration, but the LP solutions speak of "the child on stand 1". I drew one
   faceless grey pictogram per block (people_lineup rule "simple glyphs only") and no names, faces, medals or track. Without them the
   figure would still be complete (blocks 1, 2, 3 with boards).
3. C11 (Q3 solution) is `none` although Q1 and Q2 solutions are `required`: the Q3 LP steps are the subtraction 55 - 35 = 20 and never refer to
   the clocks; the old hint (a shaded 20-minute stretch on the dials) is not in the LP text. Different kind of answer (duration, not a reading).
4. C29 solution `required`: the answer is one value per stand and the text can only say "stand 1, 2, 3"; the three ANSWER tags are the
   content. C31 `required`: the answer is a position (the winner), marked with FOCUS marks.
5. Tags in the solution diagrams ("55 seconds more", "1 minute 55 seconds", "05:35 a.m.") use the LP's own words; the longest has two
   words and two numbers.
6. Same book picture, one diagram per item: C6/C8/C10 are one specification written three times (media ids M1.S3.T3.C6.IMG1, C8.IMG1,
   C10.IMG1); C28/C30 likewise. Their figure_inventory rows are P01-clock-1 + NEW-P01-clock-1-q2/-q3 and P02-podium-1 + NEW-P02-podium-1-q2.
7. P01-podium-1 (chapter-opening art that repeats the p.2 podium): nothing in any chunk uses it as a figure; I claimed it
   `none:DECORATIVE_ONLY` and said in its description that the same picture is drawn for C28/C30. The merge may find that another chunk
   claims it too; the meaning is the same.
8. P02-digital_clock-1 (24:00 digital clock in the Q6 table header): `none:DECORATIVE_ONLY`.

## Borderline

- C7, C9 (clock-reading solutions) `required`; C11 `none` (see 3). If the content team wants fewer diagrams, C7 and C9 are the ones that could
  become `none` (SAME_AS_QUESTION_DIAGRAM) without breaking anything else.
- C22 (Q7 matching solution) `optional`, not `required`: six lines joining two columns of times is an arrangement (ANSWER_IS_FIGURE), but
  the LP answer lists all six pairs and the question lists are plain numbers in boxes (NUMBER_LIST_IN_BOXES says "optional if the expression
  already gives the answer"). If the user wants the matching drawn, C22 becomes required: two columns of six times (the printed order) with
  six ANSWER lines.
- Optional (not added): C3 (time line 04:25 p.m. to 05:10 p.m.), C17 (time line 13:40 to 16:15 hours), C13 (three time lines for Q4),
  C24 (time line 08:00 to 09:05 hours), C15 (Q5 table with a minutes column and longest / least marked), C22 (above). They only make the
  text nicer; none is needed to attempt or to follow the steps. The teaching images already in the plan show some of these time lines, but
  that was not the reason for the decision.
- Tables with blanks or ticks (Q6 C19/C20, Let Us Do C32/C33, estimate and verify C36/C37) are `none` with LATEX_TABLE: plain tables,
  no colour meaning, the same call as the Number Play precedent in the prompt ("complete the table" is LATEX_TABLE). A tick is a LaTeX symbol.
- Worked examples C4, C16, C25, C26 `none` (word comparison, arithmetic, word choice).

## LP text issues (nothing was edited)

- M1.S3.T3.C6, C8, C10 (Let us find out Q1 to Q3): the question text never mentions the clocks, and gives no time. Suggested sentence to add
  before the question: "Two clocks show the time before Raghav's yoga (first clock) and after his yoga (second clock)."
- M2.S8.T8.C28 and C30 (School Race): the question text does not give the three times (01:55, 01:56, 01:57) that exist only in the picture.
  Suggested sentence: "On the winners' stand the boards show 01:55 on stand 1, 01:56 on stand 2 and 01:57 on stand 3, in minutes and seconds."
  The names Akira, Sunita and Mary cannot be matched to stands (the book does not say; C31 already states this).
- M1.S3.T3.C14 (Q5): the text says "The table below shows ..." but the table is not in the text (the data is written as a sentence). With the
  diagram `none`, the table must be written in the text: suggested "Name | Time Taken: Raghav | 1 hour 20 minutes; Rani | 2 hours 10 minutes;
  Ritu | 1 hour 35 minutes".
- M1.S5.T5.C19 (Q6): the table wording "12-hour format and 24-hour format: 05:30 a.m. = 05:30 hours; ..." reads as equations; with `none` the
  question needs the LaTeX table of text_alternative so the blanks are visible as rows.
- M1.S5.T5.C21 (Q7): the two lists are in the printed order inside one sentence; with `none` they should be two lists or a two-column
  table so the learner can see the columns.
- M2.S9.T9.C32 (Let Us Do): the book table has Seconds and Minutes columns to tick; the LP text lists only the activities. With `none` the
  table (or "answer Seconds or Minutes for each activity") needs to be in the text.
- M2.S10.T10.C35: `answer_tex` lists four sample events, step 5 lists five ("a bell ringing once" is added) and step 3 also mentions "a ball dropping
  to the floor". Harmless for a sample answer, but the answer line and step 5 do not match.
- M1.S6.T6.C23 (Nana ji): "How long did he take to reach his house?" is the book's own wording (it means Nana ji's house); the LP copied it.
  Suggested: "How long did he take to reach his Nana ji's house?"
- M1.S3.T3.C13 and M1.S4.T4.C17 etc.: no mistakes found in the arithmetic of any chunk-A LP solution (27 min, 5 h, 2 h 15 min; 80, 130, 95
  min; 19:45 hours, 04:20 p.m.; 2 h 35 min; 08:35 a.m., 11:55, 17:30, 21:35; 20:45, 23:45, 19:30, 06:30, 04:30, 01:30; 108 s, 4 s; 115, 116,
  117 s; 8 and 2 ticks) - all recomputed.

## Book unclear / book slips

- The page picture of p.1 matches the base description of P01-clock-1; the hour hands are drawn only roughly (left about 5.5 hours, right
  about 6); the readings 05:35 and 05:55 come from the minute hands. No correction needed.
- The book does not say which podium child is Akira, Sunita or Mary (the boards have no names).
- Print slip: the Q6 table header prints "fromat" for "format". The table is `none` (LaTeX), so nothing is drawn with the slip.
- The book's Q3 on p.8 ("How long did he take to reach his house?", Nana ji) means Nana ji's house; its own answer sits in a speech bubble
  (1 hour 5 minutes) with no figure.
- No book mistake needed correcting in any diagram specification (decision 1 of the user did not apply).
