# Class 5 Chapter 3, Angles as Turns: build report (local build, placeholder route)

## 12 Nov 2026: tool phases removed

The tool write-ups no longer have Phase 1, Phase 2 and Phase 3. In `tools_*.py` the three "what the student does" entries are plain steps without a phase label, and the practice cards are named "Card N" or "Challenge" instead of "Phase N, card N". The same text is in the plan's tool_config, and Section C of `priority_doc.md` has one "What the student does" line per tool. Cards, book questions, feedback, hints and everything else are unchanged (the book's questions are still on the tool's cards). DESIGN.md and MEDIA_BRIEF.md still describe the older three-phase format; this note replaces it.


(Text written by the chapter helper and saved here by the lead session, because the helper could not write the file itself. The lead session re-checks every chapter's built plan afterwards.)

## UPDATE 9 Nov 2026 (teacher feedback, version 3)
Requested changes, all applied without redesigning the plan:
- **Topic splits:** "Quarter Turns and Everyday Turns" became two topics, "Halves and Quarters Make a Full Turn" (T2, with Reema's three wheel questions) and "Objects That Turn" (T2B, with the four everyday-object questions and the tool). "Measuring and Drawing Angles" became two topics, "Measuring an Angle" (T5, with Let Us Do Q1 to Q3) and "Drawing an Angle" (T5B, with Let Us Do Q4 and Q5 and the tool).
- **Videos named as requested:** Angles from Turns (Right, Acute and Obtuse Angles; Straight Angle and More Than a Straight Angle), Measuring Turns with a Disc (Measuring Turns in Eighths; Measuring Turns in Sixths and Twelfths) and Which Direction? (Clockwise and Anti-clockwise; Finding the Final Direction After Right-Angle Turns) already had two separate videos each in one topic; they keep one topic and one tool and were renamed. The half-turn remark moved out of the clockwise video into the final-direction video, and that video now opens with a short recap of clockwise.
- **Tools (no tool added):** Statue Turn is full and half turns only (the growing wedge and the "less than or more than a half turn" read-out are removed; no angle names, no fractions of a turn). Turn Disc has three separate stages, eighths, sixths, twelfths, turns only (angle naming removed). Angle Check and Draw has two separated activities, measure first and draw second. Turn and Face is about the final facing direction, with Activity 1 as a short clockwise recap; the creature ticks stay a question card only. Quarter Turn Check has two separated activities (the wheel, then the objects). Where a topic was split, the one tool sits in the second topic.
- **Questions and assets unchanged:** all 31 NCERT questions, answers and working are identical to live v2, and all 80 question and solution card image URLs are identical. Only two concept names changed, because the drawing questions have their own Questions topic: "Let us do: Q4/Ans4" is now "Q1/Ans1" and "Q5/Ans5" is now "Q2/Ans2" (also in the card titles and the [Image: ...] tags of those two answers).
- **Concept ids shift** for everything after the first new topic (the plan numbers concepts in order); the planned file names of concept images and videos follow the new ids. They are all placeholders, none built.
- Counts now: 3 modules, 22 topics (11 authored + 11 Questions topics), 86 concepts, 31 questions, 44 videos (13 teaching, 31 question), 7 tools.

## 1. Chapter and ids
- Class 5, Maths Mela, Ch 3, "Angles as Turns", `textbooks/class-5/eemm103.pdf`, 10 PDF pages = printed pages 32 to 41 (the first PDF page is the unnumbered opener, page 32 by sequence; the next pages carry 33 to 41).
- chapter_id `cbse_eng_maths5_ch3`, chapter_master_id 147, subject_ref_id 80, medium 1, publication 1, phase 2, media_tag c5p. `check_master_id`: MASTER IDS clean.
- `set_version` read the live max version 1 and wrote version 2 (plan_id `cbse_eng_maths5_ch3_v2`): an upload would sit above the live v1.
- Nothing uploaded; no git; nothing touched outside the chapter folder and scratchpad c5ch3. No helper subagents.

## 2. Counts
- 3 modules: M1 Turns and Angles, M2 Measuring Turns, M3 Direction and Revision.
- 19 topics: 9 authored (T1 framing, T1B, T2 to T7, T8 summary) + 10 "Questions:" topics (Statue Game, Reema's Giant Wheel, Everyday Turns, Let us do x3, Angle Measuring Tool, Let Us Think, Which Direction, Fun with Turns).
- 84 concepts: 22 authored (hook, teaching, practice, summary) + 62 question and answer concepts (31 pairs).
- 31 questions: 0 solved examples (the book prints none), 15 exercises, 16 prompts. 25 have a question-card diagram, 26 a solution-card diagram; 18 answers have a second solution card.
- Coverage: 49 ids (17 text, 1 talk, 16 prompt, 15 exercise), 0 problems.
- Videos (placeholders, 44): 13 teaching (1 hook, 12 concept) + 31 question videos. No recap video.
- Tools (7, specs): Statue Turn (free try), Quarter Turn Check, Straw and Fan Angles, Turn Disc, Angle Check and Draw, Minute Hand Turner, Turn and Face.
- Images: 94 placeholders = 14 concept images + 31 question cards + 49 solution cards. 22 media specs (14 images, 8 no-image decisions with reasons).
- Misconceptions: M_SAME_FACING_NO_TURN, M_ARM_LENGTH, M_ACUTE_ADD_ACUTE, M_STRAIGHT_NOT_ANGLE, M_BIGGER_DENOM_TURN, M_CLOCK_FROM_12, M_DIR_SAME_END.

## 3. Gate state
- `build.py --worklist`, `--video-worklist`, `--placeholders`: structure stage OK. Structure, skeleton, objectives, coverage, question layout, solution content, LaTeX and equation problems all 0 (99 chains checked by the repo gate). One advisory: each question is mapped to its question and answer concept (expected).
- `validate_local` after `set_version`: 88 failures, ALL `video_script_rules`. Grouped: 44 "missing keys" (one per placeholder video), 43 "interactive_video_variant is on; a ... video needs at least one interaction_point" (31 exercise, 12 worked), 1 "the chapter hook shows a picture". Expected placeholder messages; no stamp written.
- Independent check (scratchpad numeric_check.py): 2,718 strings of the built plan, authored modules and media specs read; 413 whole-number and fraction chains recomputed with Fraction, 23 comparisons, 39 minute-and-turn facts, 8 compass statements, plus hygiene (dashes, NCERT, page N, Fig., degree words, plural fractions, vulgar fractions, `$$`, odd `$`): 0 problems (the only hit is the source_pdf path in metadata). verify_facts.py recomputes every answer, including angles measured from the page's own line coordinates: ALL OK.
- Every displayed answer is at most 220 characters of LaTeX (longest 214), measured with the real converter.

## 4. Judgement calls and clashes
1. Revision video: the brief asks for one; the pipeline forbids a recap video. T8 is a text summary with short concept checks.
2. One video in the framing topic: T1 holds only the hook and the free-try tool; the first concept video and the opener's statue question are in T1B, so Tool 1 comes before the concept video (reversed once, in the opener).
3. Seven tools, not 9 to 11: the count follows the chapter (10 pages). Reema's wheel and the everyday objects share Tool 2 (both use the quarter turn as a yardstick).
4. Teacher: the book's two "Note for Teachers" boxes are not made into content (no teaching role); the hook shows the call "Statue!" without a teacher. Fun with Turns Q1 says "the teacher tells them the direction": quoted unchanged (a game call).
5. No degrees anywhere (the chapter uses none). book_rules banned_words: degree, protractor, reflex, vertex, complementary, supplementary, radian, coordinate, bearing, perpendicular, parallel. A turn over a half is "more than a straight angle", as the book says.
6. Question kinds: "Can you recognise the child ... Discuss in class" is an answerable prompt (in T1B); "Give examples of real-life situations where you observe turns" stays a talk item in the hook. Let Us Do Q2, Q3, Q5, Q6 each keep all parts in one item.
7. Small wording changes on question cards (listed in DESIGN.md section 3): "she" becomes Reema or Padma and the wheel sentence is repeated on the three Reema cards; "the above objects" names the five objects; the object table is parts (a) to (e); creatures lettered (a) to (d), Fun with Turns rows (a) to (g); Let Us Do (a) keeps only the "use your paper fan" sentence; the sixths question is shortened; the half-of-1/6 card omits the book's answer sentence "This is the same as a 1/12 turn"; Q2 notes that (a) is solved in the book; Q3 names its shapes in words.
8. Pieces in Tools 4 and 5 are only 1/8, 2/8, 1/6, 2/6, 1/12. 1/8 + 1/6 is never written as 7/24 for students; it is classified by comparison with 1/4 and 1/2.
9. Phase 3 is called "Challenge" (students never read NCERT).
10. The hook image shows the before and after statue pictures with no turn name or answer.

## 5. Points the book leaves unclear (reading adopted)
1. Fun with Turns Q1 last row (page 41): "West | right angles clockwise, four 1/2 right angles anti-clockwise | (empty)": the number before "right angles clockwise" is not printed (checked on the image and the text layer). Four 1/2 right angles = 2 right angles anti-clockwise. Adopted: the answer gives the rule (start turned that number minus 2 right angles clockwise) and a sample (3 gives North); the card keeps a blank. Needs the intended number.
2. Statue picture (page 32): B and C both face the front again; the book asks for the child who made a full turn (singular). Adopted: B and C full turn, A (faces away) half turn, D (faces the side) neither.
3. Notebook house A to H (page 35): no key, perspective drawing. Adopted from the red arcs: A obtuse, B right, C acute, D acute, E acute, F right, G right, H obtuse.
4. Let Us Do Q1 (page 38): seven hand-drawn angles, no letters. Adopted: numbered 1 to 7 from the left (4 is the upper of the two in the middle); measured from line coordinates: about 1/12, 1/6, 1/8, 1/6, 1/4, 1/3, 3/8; acute, acute, acute, acute, right, obtuse, obtuse. Says "about".
5. Let Us Do Q2 (d): the arrow goes from the upper right (an eighth from straight up) to a little left of straight down, not a neat fraction. Adopted: about 5/12 = 1/4 + 1/6. (b) 5/8 and (c) 1/8 are exact; (a) 3/8 is printed.
6. Let Us Do Q4: each line has a dot at both ends and the book does not say which end is the corner. Adopted: either end.
7. Let Us Think Q1: the turn direction is not stated. Adopted: the green dashed arrow goes the way a clock moves, so the start is found by turning back the other way (clockwise is named only on page 40).
8. Everyday objects (page 33) table, half turn, full turn, list, and "Try these" (page 40): depend on real objects, no printed answers. Adopted as labelled samples: clothes clip less than 1/4, door more than 1/4, tongs less than 1/4, scissors 1/4, file cover more than 1/4; half turn: door and file cover; full turn: none; objects that turn: door, scissors, clock hand, giant wheel, lid; tap, lid, nut usually anti-clockwise. Each says "your answer may differ".
9. "Can the two acute turns together make another acute turn?": no answer printed. Adopted: sometimes.
10. LUD (c) 5-sided shape: many answers. Adopted: a house shape on a square grid (4 right, 2 up, 2 left and 4 up, 2 left and 4 down, 2 down), checked: 2 right, 2 obtuse, 1 acute angle.
11. Let Us Do Q5, 1/8 + 1/6: classified obtuse by comparison (more than 1/4, less than 1/2).
12. The opener has no printed page number (page 32 by sequence).
13. The opener's QR code is unreadable; nothing is taken from it.

## 6. Kit, sheet and material assumptions
The chapter refers to no kit or cut-out sheet at the end of the book. The student makes every piece (paper fan, straws, tracing-paper discs) by the chapter's own steps. The plan replaces them with on-screen pieces of the sizes the chapter names (circles in 8, 6, 12 equal parts; 1/8, 2/8, 1/6, 2/6, 1/12 pieces). Please confirm on-screen versions are acceptable. Listed in `content.SOLUTION_NOTES`.

## 7. Printed-book errors
The missing number in the last row of the Fun with Turns table. Nothing else: the printed sums (2/8 = 1/4, 4/8 = 1/2, 6/8 = 3/4, 1/4 + 1/8 = 3/8, "a 1/8 turn is half of a quarter turn", "half of a 1/6 turn is a 1/12 turn") are correct.

## 8. Answers the book does not print (worked out by the helper)
Everything in section 5 points 2 to 11, plus: Reema's three blanks (full, half, full); minute-hand questions (Let Us Do Q6: 1/4, 1/2, 3/4, 5, 60, 10, 20, final places 6, 12, 6, 2, 12, 4, 8); gymnasts (acute, right, obtuse, obtuse, straight); the Angle Measuring Tool prompts; Let Us Think (six starting arrows); the four creatures (ladybug and snail clockwise, bee and ant anti-clockwise); Fun with Turns rows (a) to (f) (South, North, East, West, East, South) and Padma (ice cream cart; another way: half turn anti-clockwise); Let Us Do Q3 (a) 1/8 and 1/8, (b) 1/6, 1/3, 1/6, (c) 1/8, 1/3, 1/4.

## 9. Needs a decision from the user
1. The missing number in Fun with Turns Q1, last row.
2. Whether B and C in the statue picture are both meant as the full turn.
3. Confirm the sample answers read from pictures and real objects (house, Let Us Do Q1 and Q2 (d), object table, tap/lid/nut).
4. Whether on-screen pieces may replace the paper fan, straws and tracing-paper discs, and whether seven tools is acceptable.
5. If the brief's revision video is still wanted, it needs an explicit exception.

## 10. Files (all in chapters/maths5_ch3/new_design/)
priority_doc.md, DESIGN.md, content.py, concept_plan.py, topics_1.py (T1, T1B, T2, T3), topics_2.py (T4, T5), topics_3.py (T6, T7, T8), tools_1.py to tools_3.py, media_specs/*.json (22), ch_latex_house.py (Ch 2's module plus one fix: the article "a" before a blank), name_slots.json (Ashutosh, Sahana, Reema, Pragya, Padma; children A to D have no tokens), book_rules.json, chapter.config.json, copied build.py, cleanup_fields.py, server_ids.py, media_placeholders.py (DOC_PURPOSE replaced, 13 videos), media_specs.py, topics_common.py, media_worklist.json, video_worklist.json, question_images_report.json, built cbse_eng_maths5_ch3.json (version 2). Scratchpad (not repo): `/tmp/claude-1506/-root-maths-learning-plan/9dfc46bf-2f90-406d-86af-005a3698a5e2/scratchpad/c5ch3/` with verify_facts.py, numeric_check.py, angle-measuring scripts, media spec generators.
