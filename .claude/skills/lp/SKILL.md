---
name: lp
description: Build a Phase 2 maths learning plan for one chapter (Class 6-10) from the textbook PDF. Use as `/lp <chapter>, <path to the book pdf>, <teacher instruction (optional)>`, e.g. "/lp class 7 ch 3, C:\books\gemh103.pdf, use cricket examples". Scaffolds the chapter, authors concepts, video scripts, images and solutions, runs every gate and stops with a validated plan. Never uploads.
argument-hint: <chapter>, <book pdf path>, <teacher instruction (optional)>
---

# /lp: one chapter, start to finish

Pipeline root: the folder holding `core/`, `gates/`, `chapter_template/` (this repo). Run Python as `python -I -X utf8`.
**Local only: never upload, never push a chapter, never touch the database writes. `set_version.py` and `check_master_id.py` only read.**
Read first, in this order: `docs/01_runbook.md` (the build order), `docs/00_overview.md`, `chapter_template/chapter.config.README.md`; Class 9/10 also `docs/04_class9_10_variant.md` (it wins where it differs).

## 0. Arguments

`$ARGUMENTS` is `<chapter>, <book pdf>, <teacher instruction>`. Chapter forms: `class 7 ch 3`, `7.3`, `maths7_ch3`, `class 8 part 2 ch 1`. Class 7 / Class 8 Part II chapters are filed after Part I (Part II Ch N = ch(8+N) for Class 7, ch(7+N) for Class 8); the script applies this.
The instruction is optional and free text ("keep it short", "use cricket examples", "skip the enrichment"). It is the teacher's wish for this chapter, not a licence to break a hard rule (steps 4 and 8).

## 1. Scaffold (deterministic)

```bash
python -I -X utf8 core/lp_start.py --raw "$ARGUMENTS"
```

It parses the chapter, resolves the folder `chapters/maths<G>_ch<N>/new_design/` and the last-known master id, copies `chapter_template/`, fills `chapter.config.json`, cuts the chapter out of the book into `book/` (`chapter.pdf`, `pages.json`, `chapter_text.md`, `outline.json`, `page_NNN.png`) and writes `lp_brief.md` + `lp_state.json`. Exit 2 means it needs something from the user; relay the message and stop:
- wrong book or part, or `could not find where chapter N starts` -> ask for the page range and re-run with `--pages A-B`.
- master id / subject_ref_id unknown -> ask the user (add `--master-id N --subject-ref-id M`). A wrong id uploads good content to the wrong chapter.
- folder already has files -> ask before `--force` (it only overwrites scaffold files, never deletes yours).

Open `lp_brief.md` and settle every FLAG. If a Class 10 chapter already has `docs/Yash_9&10/std10_ch<N>`, ask which flow to use (this one, or `/restructure-std10-lp`). **Always open `book/page_001.png`** and confirm the chapter title and the page range; a noisy text layer (flagged) means every number and sign must be checked against the page PNGs.

## 2. Study the pattern (do not skip)

Read one finished chapter of the same class end to end (Class 6-8), files in this order: `chapter.config.json`, `content.py`, `concept_plan.py` (+ `topics_*.py`), `media_specs/`, `video_scripts/`. References: Class 6 `chapters/maths6_ch3` (or `maths6_ch6`); Class 7 `maths7_ch11`; Class 8 `maths8_ch12` or `maths8_ch7`; Class 9/10 `docs/04_class9_10_variant.md` and the finished plan `docs/Yash_9&10/std9_ch5/reference_std9_chap5_circles.json` (no chapter folder of that kind exists yet, so build from the template and check the plan against that JSON's shape). Then read the whole chapter in `book/chapter_text.md`, and look at the PNG of every page with a figure, table or diagram.

## 3. Author the content

Fill `content.py` (identity, `MODULES`, `CHAPTER_APPROACH`, `NCERT_ITEMS` = **every** book example, Try This / Figure it Out item and exercise question as a coverage id, `MISCONCEPTIONS`, `FIGURES`, errata) and `concept_plan.py` (modules -> segments -> topics -> concepts, tool specs). The hard rules:
- 100% of the book: every example and question is a coverage id attached to a concept (`gates/coverage.py`). Nothing invented that the book does not teach; unsolved examples use the book's own method.
- Shape: hook first, then idea topics of 2-4 primary concepts, a framing/intro with the free-try tool, a summary last (Class 6-8: `gates/skeleton.py`; Class 9/10: `gates/theorem_variant.py`: tool at every theorem, end-of-chapter exercises as their own topic of exactly 2 concepts just before the Summary).
- **One video per concept.** A second worked example becomes its own thin-extra concept (same name, enrichment, no objective). Questions live in their own "Questions: <topic>" topics, one concept and one video per question, named with the book label ("More on Mean and Median, Q12"); `core/qt.py` does the insertion.
- **Tools only where needed**, about 10 per chapter (9 to 11; 20 is too many, 3 is too few), each used in one place; set `doer_tool_optional: true` in the config. A tool is a spec + placeholder (`tools_spec/TOOL_SPEC_GUIDE.md`) unless the user asks for it built.
- **Images only where a drawn figure is the maths**: first example of a teach concept and the hook; not every concept, not practice questions, not doers. Each one goes in `media_specs/<key>.json` with `image_decisions` giving a `why` for every concept.
- Enrichment concepts carry no objective. Every objective is checkable and anchors on a non-enrichment concept.
- Text hygiene (`gates/media_content.py`): no em or en dash (minus is U+2212), no "NCERT" / "textbook" / "page N" / "Fig." / exercise numbers in anything the student reads, asset urls under `class_<grade>/mathematics/`.
- Arithmetic must be true (`gates/eqcheck_*`); a printed-book error is kept only through `eqcheck_errata`.
- Use subagents for the bulk (one per module or topic group), but give each the rules above, the reference chapter and the teacher instruction, and read what comes back yourself.

Apply the **teacher instruction** inside these rules. Where it clashes with one (for example "skip the exercises" against 100% coverage, or "add a tool to every concept" against the tool budget) do not decide silently: list it in the approval summary below.

## 4. HARD STOP: show the plan, wait for approval

Before any media, video or solution work, run `python -B build.py --worklist` (it must already assemble) and show the user: chapter name and ids, modules / topics / concept counts, the number of questions (every one will carry solution text + question image + solution image: say so; each becomes its own concept with its own video in a "Figure it Out" topic, so questions = question concepts = videos for them: state that count), tools (names, where), images (where), how the teacher instruction was applied, every clash or judgement call, and every book error found. Wait for approval. Do not author videos before it.

## 5. Media, videos, solutions (runbook steps 5, 6, 6b)

1. `python -B build.py --worklist` -> author `media_specs/<key>.json` for each entry (image specs; see `MEDIA_BRIEF.md`).
2. `python -B build.py --video-worklist` -> one `video_scripts/<key>.json` per slot, written by the rules in `core/video_script/AUTHOR_BRIEF.md` and `docs/02_video_script_schema.md`: Keeko format, `{{NAME_n}}` placeholders (list them in `name_slots.json`), Keeko only at the end of concept videos, exactly one think-and-tell with a 3-second pause, no recap, board-format solutions, book fidelity (same objects, colours, people). Check them with `python -B core/video_script/check.py --worklist video_worklist.json --dir video_scripts`, then fill the five final names from the repo root with `python -B core/video_script/fill_names.py chapters/maths<G>_ch<N>/new_design`.
3. **Solutions, always** (`"solutions": true` is in the config and build.py stops without it). Every question concept ends up with BOTH: the question and its step-by-step solution (numbered steps + answer) in the concept content, AND a question image (IMG1) and a solution image (IMG2). `python -B build.py --solution-worklist`, author `solutions.json` for every item with the **Write tool, never a shell heredoc** (backslashes get eaten), then `python -B core/solutions/gen_scenes.py .`, `render.py .`, `check.py .`. The user approves images in `core/image_editor`; they stay `draft` until then. Rules: `math_solutions/skill/references/format-rules.md`. Only an explicit "no solutions for this chapter" from the user allows `"solutions": false`; a teacher instruction like "keep it short" does not.
4. Parallelise the video and solution authoring with subagents in batches; each reports the checker output, not just "done".

## 6. Build and gate

`python -B build.py` assembles `<chapter_id>.json` and runs every gate; fix the content, never the gate, until it prints zero errors. A gate that seems wrong is a question for the user.

## 7. Version, validate, dry-run (stop here)

```bash
python -I -X utf8 core/check_master_id.py <plan.json>      # read-only: id, subject, medium against the live row
python -I -X utf8 core/set_version.py <plan.json>          # reads the live max version, then writes version/plan_id
python -I -X utf8 validation/validate_local.py <plan.json> # zero errors -> <plan>.stamp.json
python -I -X utf8 upload/upload_lp.py <plan.json> --dry-run
```

If `.env` / `DATABASE_URL` is missing the first two cannot run: say so and stop rather than implying they passed. Rebuilding over a chapter that is already live also needs `core/published_media.py pull` first (runbook step 4) so built assets are not replaced by placeholders.

## 8. Report

Say plainly what exists and what does not: files written, gate result, stamp status, counts (concepts, videos, tools, images, questions; and `questions with solution text + IMG1 + IMG2 = X of Y`, with how many of those images are still `draft` awaiting approval), what is still placeholder (tool code, image PNGs, rendered videos), every judgement call, and how the teacher instruction was handled. **Upload only if the user then asks for it** (use the `upload` skill; staging first, ask before anything else). Never claim a check passed that did not run.
