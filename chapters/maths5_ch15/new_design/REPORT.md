# Class 5 Chapter 15, Data Through Pictures: local build, placeholder route

## 12 Nov 2026: tool phases removed

The tool write-ups no longer have Phase 1, Phase 2 and Phase 3. In `tools_*.py` the three "what the student does" entries are plain steps without a phase label, and the practice cards are named "Card N" or "Challenge" instead of "Phase N, card N". The same text is in the plan's tool_config, and Section C of `priority_doc.md` has one "What the student does" line per tool. Cards, book questions, feedback, hints and everything else are unchanged (the book's questions are still on the tool's cards). DESIGN.md and MEDIA_BRIEF.md still describe the older three-phase format; this note replaces it.


(Text written by the chapter helper and saved here by the lead session, because the helper could not write the file itself. The lead session re-checks every chapter's built plan afterwards.)

Nothing was uploaded, no git, nothing touched outside `chapters/maths5_ch15/new_design/` and the helper's scratchpad c5ch15/. Three helpers were used (topics and tools of M1; topics and tools of M2; the 20 image specs). The chapter helper wrote M3 (T7, T8, Tool 5), content.py, concept_plan.py, figs.py, config, priority_doc.md, DESIGN.md, and read and checked every helper file.

## 1. Ids
- Class 5 Ch 15, `textbooks/class-5/eemm115.pdf`. The file has 22 PDF pages but the chapter is PDF pages 1 to 9 = printed 179 (unnumbered opener) to 187. Pages 10 to 22 are Notes pages and the book's Learning Material Sheets.
- chapter_id `cbse_eng_maths5_ch15`, master id 209, subject 80, medium 1, publication 1, phase 2, media tag c5u. `check_master_id`: "MASTER IDS: clean".
- `set_version` found live max version 3 and wrote version 4 (plan_id `cbse_eng_maths5_ch15_v4`). A live Ch 15 already exists.

## 2. Counts
- 3 modules (M1 Recording Data and Pictographs, M2 Bar Graphs, M3 Reading a Picture and Revision); 17 topics (9 teaching: T1 framing, T1B, T2 to T7, T8 summary; plus 8 "Questions:" topics); 100 concepts (20 teaching, 40 question, 40 answer); 17 objectives.
- Coverage 54 ids, all attached: 10 text, 4 talk, 40 questions = 0 examples (the chapter prints no solved example), 26 exercises, 14 prompts. 40 question cards carry a diagram; 56 solution cards (16 with a second card).
- Videos 51 placeholders: 1 hook, 10 concept (T1B.C1, T2.C1, T2.C2, T3.C1, T4.C1, T4.C2, T5.C1, T5.C2, T6.C1, T7.C1), 40 question videos. No recap or puzzle video.
- Tools 5: Reporter's Notebook (free try after the hook), Pictograph Maker, Squares to Bars, Bar Graph Builder, Picture Detective.
- Image placeholders 108 = 12 concept images (T1.C1, T1B.C1, T2.C1, T2.C2, T3.C1, T4.C1, T4.C2, T5.C1, T5.C2, T6.C1, T7.C1, T8.C1) + 40 question cards + 56 solution cards; 8 Practice or free-try concepts have a reasoned no-image decision.
- Scratch scripts: scratchpad/c5ch15/verify_facts.py, check_numbers.py, scan_plan.py.

## 3. Gate state
- `build.py --placeholders`: "structure stage OK". structure 0, equations checked 392 / failed 0, coverage 0, skeleton 0, objectives 0, solution_content 0, latex_content 0, question_layout 0, video_script_rules 102 (expected). One advisory: "40 items mapped to more than one concept" (question + answer concept, by design).
- `validate_local`: 102 failures, ALL `video_script_rules`, nothing else, no stamp. Families: 51 "missing keys" (one per video, no script yet), 40 "exercise video needs an interaction_point", 10 "worked video needs an interaction_point", 1 "chapter hook shows a picture".
- Independent numeric check (check_numbers.py): 333 facts, 0 problems (every chain with fractions and mixed numbers, every "X is more/less than Y", every remainder statement, each question's answer against verify_facts, answer lengths under 150 characters, steps at most 8, kinds, 54/54 ids attached). A scan of 8,951 strings of the built plan: no `$$`, odd `$`, dash, vulgar fractions, "NCERT", "textbook", "page N", "Fig.", or stray one-letter maths span.

## 4. Judgement calls and clashes
1. Revision video: the pipeline has none, so T8 is a text summary with short checks.
2. Opener order: the framing topic holds the hook and the free-try tool; the concept video and the opener's questions follow in T1B.
3. Five tools, not 9 to 11, following the chapter. None for Comparing with a Pictograph (same step as Tool 2) or Using a Bar Graph (reading bars is Tool 3; the rest is adding, a rule, a prediction). The paper-strip activity is physical; Tool 4 takes the measured lengths.
4. "Fill the table" is a coverage item of its own (tv.table, a prompt) because the book prints only an empty table; its wording is the plan's. So the pipeline's Q numbers in "Child TV Reporter" are one ahead of the book's (students never see book numbers).
5. True or False is eight questions, one per statement, each with its own count. The dash in statement 8 is written with commas.
6. Kinds: no label starts "Example". Numbered lists are exercise; activities and the eight statements are prompt.
7. "Suggest some ways to him" is the Predict-first line of "One Icon for Many Items"; three other discuss prompts are single talk lines in teach concepts.
8. Practice values (worked examples and tool Phase 2, all labelled): 12 reading hours; stationery 10, 20, 35; fruit 12, 18, 30; samosas 3, 7, 2 icons of 10; Kabir's Saturday 3, 5, 2 against Samaira 4, 3, 2; Kabir's day 8, 6, 3, 4, 3; pencils 9, 6, 4 cm; newspapers 3, 6, 4, 5, 2 kg with a practice rule of 2 bags per kg; a picture of 9 children. None repeats a book question's number set. Helpers added two more labelled sets (Kabir's week 3, 4, 1; a ready pictograph of 9, 11, 6 icons).
9. Words kept out: tally, frequency, average, mean, median, mode, range, axis, line graph, pie chart, half or part icons. Book words only. Listed in book_rules.json (video check).
10. A scale must fit every number (no part icons, not taught).
11. The hook image shows the two reporters and five friends with five different answers, not the 35-bubble notebook, and no counts.
12. Image-spec helper choices: T4.C1 rows ordered Helping at home, Playing, Reading so the arrows do not cross; captions added to four images ("The 12 answers", "Stationery shop", "Samosas sold at the snack stall", "The class newsroom wall").
13. Tool 4's sheet goes to 10 (the book's blank Day in My Life graph goes to 9).
14. Gate and converter quirks (nothing changed): the equation gate reads "3 icons × 5 = 15" as "5 = 15" and misreads a chain after an opening bracket (worded around). The LaTeX converter turned "TV" into a maths variable and blank + cm into an italic unit; ch_latex_house.py fixes both. Question for the user only if the gate should change: the "icons × 5 = 15" reading looks like a false positive.

## 5. Kits and sheets (IMPORTANT, found by this helper)
The back of this PDF holds the book's Learning Material Sheets (PDF pages 10 and 11 are blank Notes; 12 dotted grid; 13 Fractions Kit; 15 Tessellation and Shapes; 17 Number Tokens; 19 nets of an icosahedron and a dodecahedron; 21 dot grid; 22 graph paper; 14, 16, 18, 20 blank backs). This chapter refers to none of them, so no kit assumption is made here.
For Chapter 2: page 13's Fractions Kit has 12 round pieces: 1, 1/2, 1/3, 1/4, 1/5, 1/6, 1/7, 1/8, 1/9, 1/10, 1/11, 1/12. The Ch 2 plan (already on staging as v2) said the kit was not supplied and used only 1/2, 1/3, 1/4, 1/5, 1/6, 1/8 and 1/12 (missing 1/7, 1/9, 1/10, 1/11). The lead session confirmed the kit page by eye. Ch 2 needs a revision (see the lead summary).

## 6. Points the book leaves unclear, with the reading adopted
1. Notebook counts are not printed. Counted twice at 4.5 times zoom (total = the book's 35): 1/2 hr 9, 1 hr 13, 1 1/2 hr 7, 2 hr 3, 2 1/2 hr 3; the three 2 1/2 hr go in "More than 2 hours".
2. "More than half an hour" = rows after 1/2 hour: 13 + 7 + 3 + 3 = 26. "Less than two hours" = 9 + 13 + 7 = 29. The row 2 hours is not less than two hours.
3. Whose Index Finger is Longer? has no data: a sample of practice values (Mine 6 cm, Friend 1 7, Friend 2 5, Friend 3 8, Friend 4 6; five strips because the page has five places).
4. Day in My Life has no data and says "hours and minutes" while the graph is in whole hours 0 to 9: a sample in whole hours (9 + 5 + 2 + 2 + 3 + 3 = 24), blank rows used for Playing and Other activities. Part-hours on a graph are not taught.
5. Raman's table of squares is not called a pictograph in the book; used as a row of icons (1 square = 1 hour), the bridge to bars. His "Time spent sleeping" and Sheela's "Sleeping" are read as the same five activities.
6. Recording a Day Q4: No, all five activities differ (9 6 2 6 1 against 8 7 4 3 2). Q5 is an opinion; the sample is Sheela's (study 4 and play 3 are closer than 2 and 6).
7. Food Wastage Q5 and Q6: samples (Friday less than Monday, 4 kg and 5 kg; Khichdi again), said to be guesses from the graph.
8. Notice board (13 kg could have fed 25 people) against Q4 (1 kg feeds 3 children): different rates (13 × 3 = 39). The plan uses Q4's rule (30 kg gives 90) and no notice-board number. To confirm.
9. True or False counts, read at 5 to 9 times zoom: 17 children (8 girls, 9 boys), 10 caps, 7 pairs of glasses, 14 books, 4 backpacks, 6 with cap and glasses; one child (back row, left girl) has cap, book and backpack. Boys and girls are read from uniform and hair; some back-row children are partly hidden. Statement 3 (7 boys, 7 girls hold books: False) and 6 (4 boys, 3 girls wear glasses: True) depend on this. To confirm against the original artwork.
10. "Choose your scale" (two places) are open notebook prompts with one sample each (scale 10 for 40, 50, 60; scale 6 for 24, 12, 36).
11. The opener's QR code is unreadable; nothing is taken from it.

## 7. Printed-book errors
- Table heading on printed page 182: "Activites" (typo); written correctly.
- Notice board rate against Q4 (see 6.8).
- Statement 8 is printed with a dash; written with commas.
- The book prints no answer for any question.

## 8. Answers the book does not print (all worked out by the helper)
All 40 questions: notebook table 9, 13, 7, 3, 3 and its four questions (26, 29, 3, False); shop (40, 50, 150) and a sample scale; two-wheelers (Friday; 72; 12; 24) and a sample scale; Raman and Sheela (Raman; Sheela; 2 hours; No; sample opinion); Day in My Life and index fingers (samples of practice values); food graph (Khichdi; Idli-Sambar; 30 kg; 90 children; two samples); the eight statements (False, True, False, False, True, True, True, False). Sources: verify_facts.py and DESIGN.md section 4.

## 9. Decisions needed
1. Confirm the notebook counts (6.1) and the True or False picture reading (6.9), especially boys and girls for statements 3 and 6.
2. Confirm the Q4 rule against the notice board (6.8).
3. A live v3 exists; decide how v4 relates to it (`core/published_media.py pull` is needed before any upload). Nothing was done.
4. Whether a revision video is wanted (needs an explicit pipeline exception).
5. Use the Fractions Kit sheet on page 13 of this PDF to correct the Chapter 2 plan's kit assumptions (done by eye by the lead session: the kit has every piece from 1/2 to 1/12).
