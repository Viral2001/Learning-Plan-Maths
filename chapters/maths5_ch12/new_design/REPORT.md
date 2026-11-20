# Class 5 Chapter 12, Racing Seconds: build report (local plan, placeholder route)

## 12 Nov 2026: tool phases removed

The tool write-ups no longer have Phase 1, Phase 2 and Phase 3. In `tools_*.py` the three "what the student does" entries are plain steps without a phase label, and the practice cards are named "Card N" or "Challenge" instead of "Phase N, card N". The same text is in the plan's tool_config, and Section C of `priority_doc.md` has one "What the student does" line per tool. Cards, book questions, feedback, hints and everything else are unchanged (the book's questions are still on the tool's cards). DESIGN.md and MEDIA_BRIEF.md still describe the older three-phase format; this note replaces it.


(Text written by the chapter helper and saved here by the lead session, because the helper could not write the file itself. The lead session re-checks every chapter's built plan afterwards.)

## 1. Ids and files
- Chapter: Racing Seconds, Maths Mela Grade 5, Chapter 12, `textbooks/class-5/eemm112.pdf`. It has 9 PDF pages, printed pages 155 to 163. The first PDF page is the unnumbered opener (page 155 by sequence).
- chapter_id `cbse_eng_maths5_ch12`, chapter_master_id 212, subject_ref_id 80, medium 1, publication 1, phase 2, media tag c5z.
- `core/check_master_id.py` says "MASTER IDS: clean".
- `core/set_version.py` found live max version 1 and wrote version 2, plan_id `cbse_eng_maths5_ch12_v2`. A live v1 exists on staging and v2 would replace it. Nothing was uploaded.
- Files in the chapter folder:
  - Design: priority_doc.md (sections A to F), DESIGN.md.
  - Content: content.py, concept_plan.py, topics_1..4.py, tools_1..3.py, name_slots.json, book_rules.json, chapter.config.json.
  - Media: media_specs/*.json (22 files).
  - Copied from Ch2: build.py, cleanup_fields.py, server_ids.py, media_placeholders.py (new DOC_PURPOSE), media_specs.py, topics_common.py.
  - ch_latex_house.py (adapted from frac_latex_house.py), worklists, question_images_report.json, the built plan.
- Scratch scripts (outside the repo): `/tmp/claude-1506/-root-maths-learning-plan/9dfc46bf-2f90-406d-86af-005a3698a5e2/scratchpad/c5ch12/`: verify_facts.py, check_topics.py, numeric_check.py, gen_media.py and the page crops.

## 2. Counts
- 3 modules; 8 authored topics (1 framing, 6 idea, 1 summary); 18 topics in the built plan (10 are "Questions: ..." topics).
- 94 concepts: 22 authored plus 72 question and answer concepts (36 pairs).
- 36 book questions: 1 example, 31 exercises, 4 prompts. `content.NCERT_ITEMS` has 44 coverage ids.
- 50 video placeholders: 1 hook, 13 concept, 36 question.
- 5 tools, each a spec plus placeholder: Yoga Clock (free try, T1), Day Strip (T2), Seconds Clock (T4), Time Converter Line (T5), Time Jumper (T6).
- 98 image placeholders:
  - 13 concept images: T1.C1, T1B.C1, T2.C1, T2.C2, T3.C1, T4.C1, T4.C2, T5.C1, T5.C2, T6.C1, T6.C2, T6.C3, T7.C1.
  - 36 question cards.
  - 49 solution cards (36 first cards plus 13 second cards).
  - 20 of the 36 question cards carry a diagram.
  - The other 9 authored concepts have a no-image decision with a reason.
- 19 objectives.

## 3. Gate state
- `build.py --placeholders` ends "structure stage OK". Counts: structure 0; equations checked 484, failed 0; coverage 0 (one advisory: each question maps to its question and answer concepts, as on Ch2); skeleton 0; objectives 0; solution_content 0; latex_content 0; question_layout 0; video_script_rules 100.
- `validate_local` (after `set_version`): 100 failures, all `video_script_rules`, no stamp (expected). Grouped by message:
  - 50 "missing keys" (the placeholder videos have no script)
  - 36 "exercise video needs an interaction_point"
  - 13 "worked video needs an interaction_point"
  - 1 "the chapter hook shows a picture"
  - Nothing else fails.
- Numeric check (numeric_check.py plus verify_facts.py): 77 time, duration, conversion and 12/24-hour statements matched and verified by pattern. The one flagged mismatch is a false alarm (a summary sentence cut at a comma). The other 217 sentences with a clock time were read by eye and are correct. Displayed answers are at most 178 LaTeX characters (limit 220).
- Scans of the built plan found no `$$`, no unbalanced `$`, no leftover placeholder letters, no em or en dash, and no NCERT/textbook/page numbers in student text.
- No gate was changed or bypassed.

## 4. Process note
- Helper A did T1, T1B, T2, tools_1.py and 8 media specs; the chapter helper read and checked all of it.
- The launches for helpers B and C were refused by the harness (concurrent subagent limit, "do not retry"). The chapter helper wrote topics_2/3/4.py, tools_2/3.py and 14 media specs itself.

## 5. Points the book leaves unclear, and the reading adopted
(Also in priority_doc.md A6 and `content.SOLUTION_NOTES`.)
1. The opener clocks print no digits. Measured on crops: the first clock has the minute hand on 7 and the hour hand between 5 and 6; the second has the minute hand on 11 and the hour hand just before 6. Read as 05:35 a.m. and 05:55 a.m. (the book says morning), so 20 minutes.
2. Akira, Sunita and Mary are never matched to the children on the winners' stand. The track picture shows four children and the stand three. The answer is "the child on the first stand won, 01:55, 1 minute 55 seconds", with no name.
3. "Raghav" and "Raghu" are both used (pp. 159 and 160). Both are kept as printed, one name slot each.
4. The 24-hour format is never explained in words. The book has two worked rows (05:30 a.m. = 05:30 hours, 02:30 p.m. = 14:30 hours) and a digital clock reading 24:00. The rule is read from them: a.m. keeps its digits, p.m. adds 12 to the hour, minutes never change. No 12:xx a.m. time is used. 12:30 PM and 12:40 PM appear only where the book's own problems need them.
5. Q10 (p. 163), 08:35 PM plus 8 hours 25 minutes, crosses midnight. The answer is 05:00 AM the next day (20:35 + 8:25 = 29:00 hours; the day ends at 24:00; 29 − 24 = 5). The book teaches nothing on crossing noon or midnight, so a short concept, T6.C3, was added because Q6, Q9 and Q10 need it.
6. The seconds-hand pictures are approximate:
   - p. 159 Q3: both minute hands are drawn on 6. Only the seconds hand is read (45 to 60 is 15 seconds).
   - p. 159 Q4: the seconds hand is on 5 in both clocks and the minute hand is one mark on, so 60 seconds.
   - p. 160 Q4: the hand starts on 11 (55 seconds). 55 + 40 = 95, so the new hand is on 7 (35 seconds) and the minute hand should move one mark, but the book draws it on 12.
   - The hour hand of p. 159 Q2 and p. 160 Q2 is drawn on 4, not just before 4.
7. "Seconds or minutes" (p. 157) is an estimate with no printed answers. Reading adopted: seconds for 8 activities, minutes for melting an ice-cube and making a phone call. A student's own estimate for the phone call and for washing hands may differ.
8. The open activities on p. 158 depend on the student. Each has a labelled Sample answer with practice values and "Your answer may differ".
9. "Share your strategies" (p. 155 Q4, p. 162 Q2) has no printed strategy. One reasoned strategy is shown.
10. Q4 (c) on p. 155 does not state the unit. The answer is 2 hours 15 minutes.
11. The double number line blanks are worked out from the equal tick spacing and checked against the label positions. (a) above 2, 8, 11, 12 hours, below 240, 420, 540 minutes. (c) above 2, 20, 25 minutes, below 300, 600, 900 seconds.
12. No kit, sheet or cut-out is used. The lead session's note about the Learning Material Sheets does not apply to this chapter.

## 6. Judgement calls and clashes
- Revision video: the brief asks for one, the pipeline forbids it. T7 is a text summary with short concept checks.
- Framing topic: it holds only the hook and the free-try Yoga Clock. The first concept video and the opener's questions are in T1B. The tool comes before the video (the brief's usual order is reversed). Its Phase 3 asks the opener's Q1 to Q3 as an open challenge.
- Five tools, not the usual 9 to 11. There is no tool for comparing times, seconds versus minutes (done with a real watch and a friend), or the question sets.
- Moves from the book's order:
  - The book's solved example (p. 162 Q3, 08:00 hours to 09:05 hours) sits in the 24-hour topic T2.
  - Let us find out Q6 and Q7 sit with the 24-hour concept.
- p. 162 Q1 (c) is split into two items (the line, and the seven conversions) because the answers and pictures differ. Q1 (a), (b), (c) are separate questions.
- The pipeline's own naming means book Q6 and Q7 appear as "Let us find out: Q1 and Q2" in the second Questions topic. Several topics are called "Questions: Let us do". Nothing is renamed by hand.
- The textbook quote of Zainab and Remo's bubble reads "3 times 60 = 180". The gate reads "3 times 60 = 180" as the false chain "60 = 180", so the quote writes "3 × 60". This is noted in SOLUTION_NOTES. Keeping the verbatim wording would need a gate exception, which is a question for the user.
- Unit abbreviations (min, sec, hr, "1 hours") are written in full everywhere, including the Phase 3 quotes in the tool specs. The LaTeX converter turns "sec." into secant and p.m. into variables. ch_latex_house.py holds clock times back as plain text.
- Each question keeps its own a.m./p.m. or AM/PM style (pp. 155 to 156 versus p. 163).
- Words kept out (book_rules.json): decimals, half past, quarter to, o'clock, days, speed, stopwatch.
- Helper A's two small deviations, accepted:
  - Day Strip card 4 uses 09:25 to 11:50 hours (2 hours 25 minutes) so that T2 stays clear of crossing noon, which T6.C3 teaches.
  - "a.m. half / p.m. half" became "a.m. side / p.m. side".
- The hook image shows two clocks and two mats and no person.
- Practice values are used in every tool Phase 2 and in the plan's own worked examples. They are named as practice values and none repeats a book number.

## 7. Printed-book slips (kept out of the plan's text)
- "fromat" in both headings of the p. 156 table.
- "12–hour" and "24–hour" with an en dash, and "1–20".
- "1 hours 10 minutes" in Q1 (b)(i).
- a.m./p.m. on pp. 155 to 156 but AM/PM on p. 163.
- "practices" then "practising" on p. 155.
- The minute hand is green on p. 159 and orange on pp. 155 and 160 (drawn orange everywhere in the plan).
- Some hour hands do not match their minute hands (p. 159 Q2).

## 8. Answers the book does not print (worked out by the plan)
- Every question except p. 162 Q3 (printed: 1 hour 5 minutes).
- Let us find out Q1 to Q7: the clock readings, 27 minutes, 5 hours, 2 hours 15 minutes, Rani longest and Raghav least, the table and the matches.
- The two School Race questions: 55, 56 and 57 seconds more; the child on stand 1 took 1 minute 55 seconds.
- The ten seconds-or-minutes ticks.
- The open activities (sample answers).
- The eight clock readings: 30, 35, 15 and 60 seconds; hands drawn on 4, 6, 9 and 7.
- The double number line blanks and the 15 conversions.
- Q2: 3 hours 20 minutes.
- Q4 to Q10: 08:00 PM, 08:30 PM, 12:40 PM, 07:30 PM, 06:40 PM, 01:05 PM, 05:00 AM the next day.

## 9. Needs a decision from the user
1. Confirm the opener clock readings (05:35 a.m., 05:55 a.m.) and the seconds-hand readings (section 5, points 1 and 6).
2. Confirm the added T6.C3 concept and the Q10 answer, 05:00 AM the next day.
3. Confirm the seconds-or-minutes estimates.
4. Decide whether a revision video is wanted despite the pipeline rule, and whether 5 tools are enough (for example, whether a Race Podium or Stopwatch tool should be added).
5. Decide on the verbatim "3 times 60" quote.
6. A live v1 of this chapter is on staging. v2 replaces it only when uploaded, and no upload was requested.

## 10. Still placeholder
- Video scripts and videos, tool code, concept images, question images and solution images (all build_status "placeholder").
- solutions.json is not written (the placeholder route, as on Ch2).
- The plan is not stamped.
