# Class 5 Ch 12 Racing Seconds - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths5_ch12` v4 (taken from staging). Result: new V2 version v5 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (85 items from 49 units)
{"worked_example": {"optional": 2, "none": 9, "required": 2}, "question": {"required": 15, "none": 21}, "solution": {"required": 10, "none": 22, "optional": 4}}

Optional, NOT added: [('C3', 'worked_example'), ('C13', 'solution'), ('C15', 'solution'), ('C17', 'worked_example'), ('C22', 'solution'), ('C24', 'solution')]

needs_lp_text_sync: []

## The 27 diagrams
| id | side | type |
|---|---|---|
| M1.S3.T3.C6.IMG1 | question | measurement_scale |
| M1.S3.T3.C7.IMG1 | solution | measurement_scale |
| M1.S3.T3.C8.IMG1 | question | measurement_scale |
| M1.S3.T3.C9.IMG1 | solution | measurement_scale |
| M1.S3.T3.C10.IMG1 | question | measurement_scale |
| M2.S8.T8.C28.IMG1 | question | other |
| M2.S8.T8.C29.IMG1 | solution | other |
| M2.S8.T8.C30.IMG1 | question | other |
| M2.S8.T8.C31.IMG1 | solution | other |
| M2.S12.T12.C44.IMG2 | worked example | measurement_scale |
| M2.S12.T12.C45.IMG2 | worked example | measurement_scale |
| M2.S13.T13.C47.IMG1 | question | measurement_scale |
| M2.S13.T13.C49.IMG1 | question | measurement_scale |
| M2.S13.T13.C51.IMG1 | question | measurement_scale |
| M2.S13.T13.C53.IMG1 | question | measurement_scale |
| M2.S13.T13.C55.IMG1 | question | measurement_scale |
| M2.S13.T13.C56.IMG1 | solution | measurement_scale |
| M2.S13.T13.C57.IMG1 | question | measurement_scale |
| M2.S13.T13.C58.IMG1 | solution | measurement_scale |
| M2.S13.T13.C59.IMG1 | question | measurement_scale |
| M2.S13.T13.C60.IMG1 | solution | measurement_scale |
| M2.S13.T13.C61.IMG1 | question | measurement_scale |
| M2.S13.T13.C62.IMG1 | solution | measurement_scale |
| M3.S15.T15.C66.IMG1 | question | number_line |
| M3.S15.T15.C67.IMG1 | solution | number_line |
| M3.S15.T15.C70.IMG1 | question | number_line |
| M3.S15.T15.C71.IMG1 | solution | number_line |

### Chunk A notes (from the decision agent)
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

### Chunk B notes (from the decision agent)
# Chunk B notes - Class 5 Ch 12 "Racing Seconds" (topics M2.S11.T11, M2.S12.T12, M2.S13.T13, M3.S14.T14)

Result: 26 items (14 units): required 14 / optional 0 / none 12. Validator: errors 0, 6 warnings (all "required but no inventory figure maps to it": the two T12 worked examples and the four T13 draw-the-hand solutions; their figures are not printed in the book, so that is expected).

Figures claimed from the base inventory: P05-clock-1..4 and P06-clock-1..4 (all eight map to the question item of T13 C47, C49, C51, C53, C55, C57, C59, C61). The double number lines P07-number_line-1 and P08-number_line-1 sit in chunk C's T15 questions (Let Us Do Q1), so they are NOT claimed here; T14's worked examples do not use them. The pictures on p.158 (girl skipping, children running) and the Zainab/Remo speech bubbles on p.161 are decoration and are not in the base inventory; nothing was added.

I checked every base description of P05/P06 against the page pictures (enlarged crops). All eight are correct as descriptions of what the book prints; the `unclear` doubts are confirmed as drawing inaccuracies in the book (see "Book mistakes" below).

## 1. Judgement calls

- **T11 Let Us Find Q1-Q3 (C38-C43): all six items `none`.** The book gives no figure; the child times a real activity on a real clock, and the LP sample answers are the child's own readings ("your answer may differ"). Codes OPEN_ENDED + TEXT_SUFFICIENT. MEASUREMENT_READING was not used because the reading is taken on the child's own watch, not on a printed dial.
- **T12 C44 and C45 (worked examples on the seconds hand): `required`.** Their own diagrams (media ids `...C44.IMG2` and `...C45.IMG2`, because IMG1 is the kept teaching image of each concept). Reasoning: the whole example is about reading a seconds dial, part (b) of C44 crosses 12, and C45's answer is a dial position; the dial changes how easily the child sees the stretch. User decision 5 is followed: the kept teaching images are not linked and are not the reason for any decision.
  - C44: ONE image holds both parts (a worked example has one diagram): two dials labelled (a) and (b), each with a grey dashed start hand, a red stop hand and a clockwise arrow from start to stop. No seconds value is written. Letters are shown because the LP steps refer to the parts by letter.
  - C45: ONE dial with the starting hand on 10 only. The stop position (3) is the answer and is not drawn. The question also asks about the minute hand but gives it no position, so no hour or minute hand is drawn (nothing invented).
- **T13 observe-the-clocks questions (C47, C49, C51, C53): question `required`, solution `none` (SAME_AS_QUESTION_DIAGRAM).** The answer is a number read off the same two dials; the printed pdf has no answer section; the LP solution adds no new mark. Sibling consistency: all four solutions are `none`.
- **T13 draw-the-missing-hand questions (C55, C57, C59, C61): question `required` and solution `required`** (ANSWER_IS_FIGURE, derived_from the question diagram). The solution figure is the same two clocks with ONE added seconds hand in ANSWER green on the right clock (4, 6, 9 and 7). No sweep, no label.
- **T14 C63 and C64 (hours-minutes, minutes-seconds conversions): `none`** (LATEX_ARITHMETIC, TEXT_SUFFICIENT). Pure multiply/add/subtract; the kept teaching images (double number lines) stay and are not linked.
- **Colour of the seconds hand.** The LP solution for C48 says "the thin red hand", and the book draws it red. Style tokens have no red (WRONG is vermilion and reserved), so given seconds hands are drawn in `#D62828` (stated in `manim_description` and `content.hand_styles`); hour and minute hands are INK, thick, with different lengths; hands added by a solution are ANSWER green as the prompt says.
- **Hour hand at exact 3:45 in Q2 (observe) and draw Q2.** The book draws the hour hand at about 117 degrees (a little nearer 4 than it should be); the spec uses 112.5 degrees (exactly 3 3/4). Drawn hour hands everywhere use (hour + minute mark / 60) x 30.
- **Diagram type.** `measurement_scale` (clock face is listed there) for all clock figures; aspect 16:9 for all.

## 2. Book mistakes corrected in the specs (user decision 1)

The base inventory keeps what the book prints; the specs show the corrected value.
- **Observe Q3 (P05-clock-3, C51).** The book draws the minute hand exactly on 6 on BOTH clocks, but the seconds hand goes 45 s to 60 s, which completes a minute (5:30 and 45 s to 5:31 and 0 s). Spec: right clock minute hand at 186 degrees (31 minutes, one mark past 6). Same convention as the book's own Q4 and Q7. The LP solution does not mention the minute hand here, so the answer text is unaffected. If you prefer the exact book picture, change the right clock's minute hand to 180 degrees.
- **Draw Q4 (P06-clock-4, C61/C62).** The book draws the right clock's minute hand on 12, but the LP solution (and 55 s + 40 s = 95 s) says the minute hand has moved on by one mark. Spec: right clock minute hand at 6 degrees (one mark past 12), both in the question figure and in the solution figure.
- Observe Q2 / draw Q2: hour hand drawn exactly at 3:45 (see above); not a print slip, a drawing inaccuracy.

## 3. LP text issues (no LP text was edited; no decision changed because of them)

- **M2.S13.T13.C60 and C62 (solution `text` field):** the `text` still contains the old card markers "[Image: Let us do: Ans7: solution]", "[Image: ... (continued)]" (and the same for Ans8) between the steps, because these answers had two cards (IMG1, IMG2). The new plan has ONE solution diagram per answer, placed before the first step. Suggested: remove both marker lines from `text` (the build should regenerate `text` from the steps) so no stray marker is left.
- **M2.S13.T13.C51 (Ritu, observe Q3), steps_tex:** suggested extra sentence after step 2 so the picture and the words agree: "The minute hand in the right clock has also moved on by one mark, because the seconds hand has just finished a minute."
- **M2.S13.T13.C55, C57, C59, C61 (questions):** the question text does not say that the LEFT clock shows the starting time of the activity; the figure carries it. No change needed if the question figure is always shown; suggested sentence if you want the text to stand alone: "The clock on the left shows when the activity began."
- **M2.S13.T13.C47, C49, C51, C53 (questions):** same point: "The clock on the left shows the start and the clock on the right shows the end."
- **M2.S12.T12.C45 (worked example):** the question asks "what happens to the minute hand?" but gives no minute-hand position; the answer ("moves on by one mark") works without one. Fine; mentioned because the picture shows a seconds hand only.
- `q_figure` / `s_figure` hints in the units are not LP text; for the record, C49's hint "hour hand on 4" and C61's hint "minute hand on 12" on both clocks differ from the specs for the reasons in section 2.
- Book numbering: the LP calls the draw-the-hand questions "Let us do: Q5 to Q8" (concepts C55-C61) but the book numbers them 1-4 on p.160, and the `book_number` fields say "Q1..Q4 (drawing the seconds hand)". Consistent enough; just a note for anyone matching by number.

## 4. Borderline (applied the v3 rules as written; none flipped for LP text carrying the numbers)

1. **T12 C44 and C45 `required`** although the data are in the question text: the dial is the subject (MEASUREMENT_READING) and (b) crosses 12; judged that the picture changes how correctly and how easily the child solves it. If you read the tie-breaker more strictly ("text alone is enough") these two become `none` with TEXT_SUFFICIENT; they are the only required items that rest on that judgement.
2. **T13 observe solutions `none`.** A shaded sweep from start to stop (labelled 30 / 35 / 15 / 60 seconds) would be a nicety, and it is the same kind of addition for all four, so all four stay `none`. Q4 (the full round, 60 seconds) is the one where a picture helps most; kept `none` for sibling consistency. If you want it, Q4 is the candidate for `optional`/`required`.
3. **T11 Let Us Find solutions `none`.** Sample answers mention hand positions; open activity, no figure in the book.
4. **T14 worked examples `none`.** A double number line would help the idea, but it is the job of the kept teaching image; the question itself is arithmetic.
5. **Minute-hand corrections** (observe Q3, draw Q4): see section 2. Borderline between "drawing inaccuracy" and "print slip".

## 5. Places where the book itself is unclear

- p.158 / p.159-160: the minute and hour hand positions are only approximately right in several clocks (hour hands about 4 degrees off, minute hand on a mark instead of between marks). The spec uses the minute-mark convention: minute hand at (minutes) x 6 degrees, hour hand at (hour + minutes/60) x 30 degrees.
- p.160 draw Q3: the right clock's minute hand "just past 6" is drawn at about one mark; the spec uses exactly one mark (186 degrees). The hour hand there is a hair further on than the left (165.5 vs 165 degrees), as in the book.
- The book has no printed solutions section; every solution figure is derived from the LP steps.

### Chunk C notes (from the decision agent)
# Notes for chunk C (Racing Seconds, cbse_eng_maths5_ch12_v4)

Units: M3.S15.T15 (Let us do, conversions: Q1a, Q1b, Q1c line, Q1c conversions, Q2), M3.S16.T16 (3 worked examples), M3.S17.T17 (Let us do, time problems Q4 to Q10).
Result: 27 items, required 4 / optional 0 / none 23. Validator: errors 0, warnings 0.

Required (all four are the book's two double number lines, redrawn to scale on a 1920 x 1080 card):
- C66.IMG1 question and C67.IMG1 solution: Q1(a), hours over minutes (book p.7, P07-number_line-1).
- C70.IMG1 question and C71.IMG1 solution: Q1(c) the line, minutes over seconds (book p.8, P08-number_line-1).
- The solution figures are the same picture with the blanks filled in ANSWER green; each is `derived_from` its question figure.
- The solution use of each book picture has its own inventory entry (`NEW-P07-number_line-1-sol`, `NEW-P08-number_line-1-sol`), as the brief asks for a figure used twice.

## 1. Judgement calls

- **C66 / C70 question side required.** The tick positions (not equally spaced: 1, 2, 4, 7, 8, 9, 11, 12 hr and 1, 2, 5, 10, 15, 20, 25 min), the arrows and which labels are blank live only in the picture, and the learner fills the blanks on it (DATA_IN_FIGURE, ACTION_ON_FIGURE, FIG_REFERENCED).
- **C67 / C71 solution side required.** The answer is the filled number line (ANSWER_IS_FIGURE); the LP `s_figure` says the same.
- **Arrows kept exactly as the book prints them.** Q1(a): only the top arrow is labelled (x 2); the tall left arrow and the bottom arrow carry no text. Q1(c): top x 5, left x 60, bottom arrow unlabelled. I did not add labels in the solution, because the LP solution names only the "x 2" and "x 5" arrows (and says "60 times as many" in words).
- **Labels use the book's abbreviations** (hr, min, sec) and no commas (1200 sec, 1500 sec), as printed. The LP text writes "hour(s)", "minutes", "seconds".
- **Question text list vs picture.** The LP question text lists the labels in tick order and so matches the book, but the figure also fixes the unequal tick spacing, so the figure is not redundant.
- **C68 / C69 (Q1b conversions) none.** Plain conversions with all numbers in the words; the book only says the Q1(a) line "can" be used. The number line is not needed to attempt it and the solution never marks it. Sibling rule: same kind as Q1(c) conversions (C72 / C73) which are also none.
- **C72 / C73 (Q1c conversions) none.** Seven arithmetic conversions, no printed figure. The base inventory has no figure for them. The book's tinted boxes holding the (i) to (viii) lists on pp.7 and 8 are the question text itself, not a figure, so they are not in the inventory.
- **C74 / C75 (Q2, 4 x 50 minutes) none.** Word problem, no picture in the book.
- **C80 to C93 (time problems Q4 to Q10) none, both sides, all seven alike.** Word problems with every number in the text; the book has no picture for any of them and the answers are clock times, not drawings (sibling consistency kept: all seven pairs get the same decision).
- **Book Q3 (08:00 to 09:05, Nana ji) is not in this chunk** (it is chunk A's `ex.nana` unit); I did not claim its speech-bubble picture.
- **Page 7 speech bubbles (Zainab and Remo) and page 8 Raghu speech bubble** are character art with text; they are teaching or decoration for other units, not claimed here.

## Borderline

- **C76, C77, C78 worked examples (time after, time before, crossing noon and midnight): none.** A time line would help, and each concept already has a kept teaching time line (C76.IMG1, C77.IMG1, C78.IMG1, never linked). Judged on its own, no v3 trigger applies: no figure is referenced, nothing is read from a picture, the answer is a time, and a careful student can solve each from the text (tie-breaker). If the team wants a time line on the worked example itself, the three could be switched to required and the existing teaching time lines used as the spec (the C78 one would need two panels, a bus across noon and a train across midnight).
- **C68 Q1b question** says "You can use the above double number line". I read this as an optional help, not a reference the question cannot be answered without. If the team wants the line repeated here, it would be a second copy of C66.IMG1 (a repeat is the only change).
- **C69 solution** could draw a few of the answers on the number line, but the LP solution never uses the line, so none.

## 2. LP text issues

- **M3.S15.T15.C68 (Q1b question text):** "You can use the above double number line" - in the LP the number line sits two cards earlier (C66 / C67), not directly above. Suggested sentence: "Do as instructed. You can use the double number line of the previous question for the following conversions." (Only a wording point; no decision depends on it.)
- **M3.S15.T15.C66 / C70 (question text):** the text lists the labels in tick order but says nothing of the arrows or that the ticks are not evenly spaced; the figure carries that. If the figure were ever missing the learner could not place the blanks. No change needed once the diagram is in.
- **M3.S15.T15.C67 steps:** step 2 says "The x 2 arrow joins 1 hour to 2 hours", which matches the figure; no step names the unlabelled left and bottom arrows. Not an error.
- **M3.S15.T15.C71 steps:** "The x 5 arrow joins 1 minute to 5 minutes" matches the figure. Fine.
- I recomputed every LP answer in this chunk: Q1a (2, 8, 11, 12 hr; 240, 420, 540 min), Q1b (70, 165, 195, 260 min; 1 h 15, 2 h 30, 3 h 40, 6 h 30), Q1c line (2, 20, 25 min; 300, 600, 900 sec), Q1c conversions (5 min 20 sec, 3 min 45 sec, 11 min 40 sec, 16 min 40 sec, 613, 248, 940 sec), Q2 (3 h 20 min), worked examples (05:10 p.m., 05:35 p.m., 02:10 p.m., 04:00 a.m. next day) and Q4 to Q10 (08:00 PM, 08:30 PM, 12:40 PM, 07:30 PM, 06:40 PM, 01:05 PM, 05:00 AM next day). All are correct and agree with the book text. No missing data found.

## 3. Where the book itself is unclear

- **No print slip** in the two number lines (checked tick by tick against the page pictures: labels, blanks and arrows match the base descriptions). Decision 1 (book mistakes) therefore changed nothing.
- **Book Q1(b)(i) prints "1 hours 10 minutes"** (grammar slip, not a number). The LP already writes "1 hour".
- **Book Q1(a) picture:** the line runs a little past the 12 hr tick (right end at about 12.7 hr) and the zero end is unlabelled; I kept both (end dots at 130 and 1840 px, zero not labelled). The left arrow starts at the "1 hr" label and ends on the bottom line; the book does not say what it means, the LP does not mention it; I kept it unlabelled.
- **Book Q1(c) picture:** the two long ticks (1 min and 5 min) are drawn long so their labels can stand in a higher or lower row; the bottom arrow (60 sec to the blank under 5 min) has no label although it is also a x 5 step. Kept as printed.
- **Book Q1(c) has seven ticks but the "___ min" and "120 sec" labels sit close to the 1 min long tick** in the book; in the redraw they start 12 px to the right of it (x=244) so the label does not touch the tick.
- **Layout is a redraw**: the exact pixel positions in the spec come from the book's proportions (ticks to scale) re-fitted to a 16:9 card, not copied from the page picture. The renderer may nudge the arc shapes if an arc touches a label; the tick positions, label rows and values must not change.
