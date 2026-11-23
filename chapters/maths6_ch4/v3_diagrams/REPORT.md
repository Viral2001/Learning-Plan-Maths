# Class 6 Ch 4 Data Handling and Presentation - V3 diagrams, 23 Nov 2026

Source: live V2 `cbse_eng_maths6_ch4` v85 (active, untouched, verified identical before and after). Output: `out/cbse_eng_maths6_ch4_V3_v1.json` = chapter `cbse_eng_maths6_ch4_V3`, phase 3, version 1, master id 188 (same as V2). **UPLOADED to staging 23 Nov 2026 as ACTIVE v1**: the V3 chapter did not exist (versions call returned 404); posting a plan with the new chapter_id CREATED it (the server accepted it). Stamp skipped (phase 3). Read back identical. Rules: `spec/` v3 (the edited files from docs/karan-MD). Same recipe as Class 6 Ch 3 and Class 8 Ch 11 (see their folders).

## Result
- 92 old question/solution card placeholders removed (all `placeholder`, none built); 34 DIAGRAM placeholders added (23 question, 2 worked example, 9 solution), titled `DIAGRAM · <label> question|solution figure`, token `{{DIAGRAM:<id>}}`, full spec in `diagram_spec`. Nothing rendered (placeholders + spec only). 113 images -> 55; 59 videos, 6 tools, 21 concept images unchanged (all of them are still placeholders in V2: nothing in this chapter was built yet); no block links a teaching image.
- 96 items from 50 units (46 question/answer pairs, 4 worked-example blocks). Figure inventory (Step 0): 63 figures (54 from the 44 book pages + 9 NEW- entries: a second or third use of one picture needs its own entry), unmapped 0.
- Optional, NOT added (user rule): C118 (solution of the Everest/Elbrus question).
- `needs_lp_text_sync` (the figure carries data the LP text states or hides; text not changed): C16 question (the tally table text states the three blanks' answers), C40, C42, C55 questions (the LP parentheses give the figure's data, in C42 and C55 even parts of the answer).

## The 34 diagrams
| id | side | type | token goes into |
|---|---|---|---|
| M1.S2.T2.C3.IMG2 | worked example | other | question_tex / after_question_text |
| M1.S3.T3.C7.IMG1 | question | other | question_tex / after_question_text |
| M1.S5.T5.C16.IMG1 | question | data_graph | question_tex / after_question_text |
| M1.S5.T5.C17.IMG1 | solution | data_graph | steps_tex / before_first_step |
| M1.S5.T5.C18.IMG1 | question | data_graph | question_tex / after_question_text |
| M2.S9.T9.C36.IMG1 | question | data_graph | question_tex / after_question_text |
| M2.S9.T9.C38.IMG1 | question | data_graph | question_tex / after_question_text |
| M2.S10.T10.C40.IMG1 | question | data_graph | question_tex / after_question_text |
| M2.S11.T11.C42.IMG1 | question | data_graph | question_tex / after_question_text |
| M2.S13.T13.C47.IMG1 | question | data_graph | question_tex / after_question_text |
| M2.S14.T14.C50.IMG1 | solution | data_graph | steps_tex / before_first_step |
| M3.S16.T16.C55.IMG1 | question | data_graph | question_tex / after_question_text |
| M3.S16.T16.C57.IMG1 | question | data_graph | question_tex / after_question_text |
| M3.S16.T16.C59.IMG1 | question | data_graph | question_tex / after_question_text |
| M3.S17.T17.C61.IMG1 | question | data_graph | question_tex / after_question_text |
| M3.S18.T18.C69.IMG1 | question | data_graph | question_tex / after_question_text |
| M3.S20.T20.C76.IMG1 | solution | data_graph | steps_tex / before_first_step |
| M3.S20.T20.C78.IMG1 | solution | data_graph | steps_tex / before_first_step |
| M3.S21.T21.C79.IMG1 | question | data_graph | question_tex / after_question_text |
| M3.S21.T21.C81.IMG1 | question | data_graph | question_tex / after_question_text |
| M3.S21.T21.C83.IMG1 | question | data_graph | question_tex / after_question_text |
| M3.S22.T22.C86.IMG1 | solution | data_graph | steps_tex / before_first_step |
| M3.S22.T22.C87.IMG1 | question | data_graph | question_tex / after_question_text |
| M3.S22.T22.C88.IMG1 | solution | data_graph | steps_tex / before_first_step |
| M3.S22.T22.C90.IMG1 | solution | data_graph | steps_tex / before_first_step |
| M3.S22.T22.C91.IMG1 | question | data_graph | question_tex / after_question_text |
| M3.S22.T22.C93.IMG1 | question | data_graph | question_tex / after_question_text |
| M3.S22.T22.C94.IMG1 | solution | data_graph | steps_tex / before_first_step |
| M4.S24.T24.C97.IMG1 | question | cell_grid | question_tex / after_question_text |
| M4.S24.T24.C103.IMG1 | question | data_graph | question_tex / after_question_text |
| M4.S24.T24.C105.IMG1 | question | data_graph | question_tex / after_question_text |
| M4.S24.T24.C108.IMG1 | solution | data_graph | steps_tex / before_first_step |
| M4.S25.T25.C110.IMG2 | worked example | data_graph | question_tex / after_question_text |
| M4.S26.T26.C117.IMG1 | question | other | question_tex / after_question_text |

## Structure facts
- Pairs only (no single-concept items). C117/C118 (Everest/Elbrus, 'Pretty Pictures and Honest Graphs' Q3) hold TWO blocks each that shared ONE card: the question diagram C117.IMG1 is linked on both blocks (token in the first); the solution C118 is optional so both links were dropped. `inventory.py` keeps the second block in `extra_items`, `build_v3.py` keeps every old link of a shared card.
- The same book picture used by several items gets one diagram per item (v3: a teaching image is never linked, `derived_from` is only for solutions): C79/C81/C83 (Imran's graph), C55/C57/C59 (absent-students graph), C36/C38 (modes of travel) are identical; render once, copy.
- Diagram ratio: the agents wrote 16:9 for every diagram (the user's 21 Nov image rule); the v3 prompt text still says 'by content'.
- My own checks: bar values and symbol counts recomputed against the LP text (C86 6,10,5,3,2; C90 45,30,20,10,15 = heights 9,6,4,2,3; C91 50,40,30,40,50,60,40; C103 6,5,8,3,6; C105 24,18,20,14,10,16,12,6 girls; C108 18,36,12,48,18,24 dogs = 3,6,2,8,3,4 symbols of 6; C36 4,5,11,3,7 = 30), and the 50-entry list of C97 (13 bike, 6 car, 4 bus, 8 auto rickshaw, 8 bicycle, 2 bullock cart, 9 scooter), which two independent agents counted the same.

## Judgement calls the user may want to flip
- C12 (Pari's tick/cross boxes, printed answer is four marked boxes): none (TEXT_SUFFICIENT); under a literal B2 reading it would be a required solution diagram.
- C98 (frequency table, printed answer is a picture of a plain table) and C102: none (LATEX_TABLE, plain tables win over B2).
- C47 (Math Talk 'such a pictograph'): required, because the key (smiley = 10, half smileys) is not in the LP text.
- C97 (Chinu's 50-entry list): required (the LP text says 'see figure' and the question would have no data), although a plain table of words usually is LaTeX.
- Reading-graph questions are required although the LP text repeats the values (C40, C42, C55, C61, C69, C79-C83, C91, C103, C105): the skill is reading the graph; five of them flagged, the others are the same call.
- C110 (triangle infographic worked example) is the closest call of the infographic items; Q3 (C117) draws only the infographic, not the column graph it also mentions.

## Things in the LP / book that look wrong (not changed)
- Duplicated text: C11, C16, C23, C29, C31, C97, C99, C103, C105, C107 repeat their (a)-(f) sub-question list twice inside `question_tex` (and the answer concepts' `question`).
- C2 says 'Navya is showing the list:' but no list appears (the C2 and C3 concept images are stand-ins: circles and dots). C13/C14 textbook text carries stray Figure it Out Q4 / Q2 text. C49 `book_number` says Q1 but it is Figure it Out 4.2 Q2. LP 'Figure it Out 4.4' numbers restart at Q1 in module 4 (book Q3-Q8; M3 Q3-Q5 = book Q9-Q11): two titles read 'Q4 question figure' (C91, C103) and two 'Q5 question figure' (C93, C105); the media ids are unique.
- C18's LP hint says the sweets table is completed, the book's table still has the three blanks (followed the LP). C107's `q_figure` mentions a table of Mudhol dogs, the book gives a line of text. The book prints no answer for the die question (C100), the class survey (FiO 4.1 Q3) and the traffic Q2-Q4.
- Book vs book: Kilimanjaro 5892 m on p.32 against 5895 m everywhere else (drew 5895); 'Kosciuszko' vs 'Koscuiszko' (followed the LP); the printed graphs differ slightly from their own tables (traffic 9-10 drawn ~820 vs 800, tigers bars, Imran's graph, Monday saplings ~52 vs 50): the diagrams use the table values and say so in `render_note`.
- The tigers graph (C93/C94): the book prints no values; the wrong bars were read from the page (2022 = 3700 correct, the other four drawn at 2200, 2900, 1500, 800), only the pattern of which bars are wrong is certain.

## Upload
`upload_v3.py out/cbse_eng_maths6_ch4_V3_v1.json --go` (reuses upload_lp.post() with chapter_master_id=188, phase=3; needs the user's OK; a 404 on the versions call is treated as 'no versions'). V3 chapter created by this upload; nothing to back up.


## Images for all 55 image nodes (23 Nov 2026, user's request: "make all images, use gemini wherever needed")
- All 55 were drawn (21 teaching images + 34 DIAGRAM nodes), in code, in Image-Pipeline-Maths `workspace/hand-specs/maths6_ch4_v3_images/` (`kit.py`, `render.py`, `verify.py`, `m_*.py`, `fruit.py`, `delivered_images.json`). PNGs: `png/` here and `generated images/NCERT/cbse_eng_maths6_ch4_V3_v1/`. Every picture is 1456 x 816 on the house card (logo, faint watermark). Teaching images carry the plain title banner (the node's title; user's choice), the 34 diagrams follow the diagram rule (no banner, drawing enlarged to fill the card, a question and its solution on one transform). Only C1 uses Gemini (apple, banana, mango in natural colours, user's choice); everything else is exact code.
- Uploaded to staging as ACTIVE **v1, in place** (no new version): every `image_url` is `.../ch_4/image_v3/<id>.png`, `build_status` `built`, the PLACEHOLDER sentence gone from `context`, `description` rewritten from each picture (5 corrected by hand). The nodes' brief fields were NOT changed (the pass cannot): the 34 diagram nodes still say `image_dimensions` 1920x1080 / 1920x1440 / 1920x768 (the pictures are 1456x816; the user chose to leave the size fields alone), and the teaching nodes' generation / negative prompts still say no logo, no watermark, no title.
- Checks: every count, value and ratio the specs state is asserted in the drawing code; verify.py (size, logo, card, watermark, layout, words = visible_text, a solution redraws its question). The image pass's read held one picture, C52 (it counted 11 blocks; the picture has 12), pushed with --accept after counting from the pixels.
- Spec oddities drawn as written, for the LP side: C21's example (10 cards) differs from the concept's book text (27 numbers); C117's Koscuiszko label is wider than the spec's canvas; C87 draws Indore 4.4 units (LP text: about 4.5); C50's spec says the RIGHT half of the kite, the picture draws the left half in the slot like every other half symbol; C45's key has no 'half smiley = 5' (the spec's visible text only has 'half = 5').
