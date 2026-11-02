---
name: restructure-std10-lp
description: Restructure a phase-1 Class 10 maths learning plan into the Class 9 Ch5 shape (md review doc first, then JSON). Use when asked to restructure, rebuild or convert a Std 10 chapter plan (e.g. "do std 10 chapter 4"). Everything stays local; never uploads.
---

# Restructure a Std 10 chapter plan

Work folder: `C:\Users\DELL\Desktop\maths_new_design_pipeline\docs\Yash_9&10\` (one folder `std10_ch<N>` per chapter; tools in `tools\`). Rules source: `docs\04_class9_10_variant.md`. Reference shape: `std9_ch5`. Run Python as `python -I -X utf8`. **Local only: never upload, never edit files outside the work folder.**

## Inputs
- Old plan: `C:\Users\DELL\Downloads\Yash_Doc\` — ch1 `learning_plan.json`, ch2 `(1)`, ch3 `(2)`, ch4 `(3)`, ch5 `(4)`, ch6 `(5)`, ch7 `(6)`, ch8 `(7)`, ch9 `(8)`, ch10 `(9)`, ch11 `(10)`, ch12 `(11)`, ch13 `(12)`. Copy to `std10_ch<N>\learning_plan_std10_chap<N>_version1.json`.
- Textbook PDF `jemh1<NN>.pdf` (read with pymupdf) into `std10_ch<N>\textbook_*.pdf`.

## Standing decisions (do not re-ask)
1. No tools: all old tool media are held, never attached.
2. Exercise-question videos are held; each question concept gets one hint-free placeholder image spec (`solution_status: to_author`, empty steps/answer).
3. One concept per question, in textbook order, no grouping. Name `<Set name>, Q<n>`; separate sub-parts become `<Set name>, Q<n> (<roman>)`, each keeping the parent's objectives. Sub-parts that build on each other stay one concept (note under the topic).
4. Questions topic opens with one line `Objectives for this set: ...`; exercise-question concepts are `exercise` with `attempt_first: true`.
5. Nothing deleted: media/objectives that leave go to Appendix B / "not carried" notes. Identity: attached + held = old media total.
6. No Fig./Table/Theorem/Example/Exercise/Section/Chapter numbers or scaffolding labels in student-facing text; book numbers only in review prose.
7. Keep old→new id mapping (Appendix C). Enrichment concepts carry no objectives; every objective anchors on a non-enrichment concept.
8. Figure questions: Media line keeps "the book's own ... figure" (builder key); new image shows the statement only, no hints/working/answer.
9. Theorem ids `TH1..`: a `try` gets a new id; an adjacent `prove` shares it.
10. No concept may be left without media. A non-question concept with no re-homed asset gets `Media: new image spec "<Title>" — <what is drawn>` (builder makes a placeholder image; try concepts show the setup only, never the result). Question concepts never get a video.

## Procedure
1. Set up the chapter folder; read old plan + PDF; list exercises, question and sub-part counts.
2. Write `maths10_ch<N>_representative_lp.md` (format below). Subagents may draft; give them the decisions above.
3. **HARD STOP**: show the user the md summary (counts, judgement calls, loose media fits) and wait for approval. Do not build JSON before that.
4. Add the chapter to `tools\chapter_config.json`: `exercises` (book exercise numbers in order), `examples` (concept number → `"<N>.ex<k>"`), optional `topic_map` (old topic → new topic, needed when Appendix C has no table).
5. `python -I -X utf8 tools\build_std10_lp.py <N>` → `learning_plan_std10_chap<N>_version2.json` (`_activate: false`).
6. `python -I -X utf8 tools\check_std10_lp.py <N>`: must show `problems: none` and `0` leak hits. Fix the md, rebuild, recheck.
7. Report counts, files, drafted decisions, flagged items. Do not upload.

## md format (parsed by the builder)
`# M<k> · name` modules; `## T<n> · name` topics (suffix "(hook)" for hook); `### C<n> · name` concepts with meta line(s); `[tag]` lines followed by `>` quotes. Accepted tags: textbook_text, theorem_statement, predict, enrichment, method_statement, teach, question, worked solution, remark, summary_points, plus review-only `figure note` (skipped). Unknown tags raise. `Media:` lines use `old T<n> <suffix>`. Appendix A objectives table `| ID | Bloom | Objective | Old ID |`; Appendix B held assets (tools / question videos / other); Appendix C old topic → new concepts. C-ids continuous. Question concept names must match `^(.+), Q(\d+)(?: \(([ivxlc]+)\))?$`.

## Known gotchas
- Heredocs mangle `"\n"` in Python source; use the Edit tool.
- Media titles keep the book label in `old_title`; check for `clean_title` leftovers.
- New objectives take the next free id at the end; never renumber.
