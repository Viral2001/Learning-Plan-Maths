# 01. Runbook: building one chapter, start to finish

This is the authoritative order. It follows `validation/STAMP_FORMAT.md`
exactly where that file states an order (steps 8-11 below) - nothing here
contradicts it. (A step-ordering note in the older checkout's docs/27 §7
puts validation before upload in a different sequence than this pipeline's
own `SKILL.md`/`STAMP_FORMAT.md`; follow this pipeline's own docs, since
that older note describes a different pipeline's upload flow.)

## 1. Get the chapter_master_id

Confirm the grade/chapter mapping and its master id before writing anything.
Check `upload/chapter_master_ids.md` for the last known value, then confirm
it live:

```bash
python core/check_master_id.py <existing-or-draft-plan.json>
```

For a brand-new chapter with no plan yet, ask for the issued id rather than
guessing - a wrong id attaches good content to the wrong chapter and still
reports success. Watch for the Grade 7/8 Part II numbering traps documented
in `upload/chapter_master_ids.md`.

## 2. Copy chapter_template

Clone `chapter_template/` into the new chapter's folder. It carries the
`build.py` shape, `media_specs/`, and `video_scripts/`. Fill in the
chapter's own `chapter.config.json` (at minimum `chapter_master_id`,
`phase: 2`, and `eqcheck`: `plain`/`signed`/`powers`).

## 3. Author content

Write the chapter's own content modules (concepts, tool specs, media specs)
against the book. This is the bulk of the work and has no single script -
see `chapter_template/` and `tools_spec/` for the shape each piece must
take.

## 4. If rebuilding over a live chapter: pull published-asset pins first

Before the first full build, so the builder has pin files to read:

```bash
python core/published_media.py pull <chapter_id> <version> <plan.json> published_images.json
python core/published_media.py pull-tools <chapter_id> <version> <plan.json> published_tools.json
```

Skip this for a brand-new chapter with nothing live yet.

## 5. Run build.py's worklist passes

Chapter `build.py` scripts typically run in worklist-generating passes
before authoring is complete (e.g. emitting `video_worklist.json` /
`media_worklist.json` for the video/image authors to work against). Follow
the chapter's own `build.py --help` or its top-of-file docstring for what
passes it exposes; this varies more per chapter than any other step.

## 6. Author video scripts

Using the chapter's `video_worklist.json`, write one `video_scripts/<key>.json`
per planned video, following `core/video_script/AUTHOR_BRIEF.md` and the
schema in `docs/02_video_script_schema.md`. Check every file as you write it
with `core/video_script/check.py`.

The format is the Keeko design (28 Oct 2026), the same one all Class 6-8
reference chapters were migrated to: a concept video (`worked`/`theorem`) ends
with Keeko raising a hand (a misconception or a real-life link); `hook` and
`exercise` videos have no Keeko; every video has exactly one think-and-tell
(3-second pause); there is no recap video or recap line. Write character names
as `{{NAME_n}}` tokens (n up to 10, one character = one token for the whole
chapter), list them in `name_slots.json` (start from
`chapter_template/name_slots.json.sample`), then run
`python -B core/video_script/fill_names.py chapters/<chapter>/new_design` to
fill the five final names (the token form is kept in `video_scripts_tokens/`).
An exercise video names, in `callback_to`, the solved example whose method it
uses (`method_from` in the worklist). Its solution beats must agree with the
item's `solutions.json` entry.

## 6b. Author the question solutions (always: `chapter.config.json` has `"solutions": true`)

This step is not optional for a new chapter: `build.py` stops if the config has no `"solutions"` key, and
stops again if any question has no `solutions.json` entry. Every question ends up with the question plus its
numbered step-by-step solution and `Answer:` in the concept, AND a question image and a solution image.

Before any solution exists, `python -B build.py --placeholders` builds the plan with the question layout (one
"Questions: <category>" topic per book category after every concept topic - Exercise Set / Figure it Out /
Example / Let us do / other, `core/question_naming.py` - one concept per book question: solved examples, exercises
and answerable prompts) and a question image, a solution image and, for a long working, a second solution image
on every question as placeholders; it prints `structure stage OK` when every gate that can pass without video
scripts passes, and writes `question_images_report.json`. Review the structure there first. Everything below
then fills the placeholders in.

Every question gets its board-format solution, written once in `solutions.json` and used three times:
the plan's `steps`/`answer`, the video worklist items, and a question image plus a solution image
(LaTeX + Manim). Schema and field rules: `core/solutions/schema.py`; the writing rules are
`math_solutions/skill/references/format-rules.md` (name the formula, one operation per line, values
before squaring, highlighted answer, a common-mistake note, a figure that matches the question and does
not give the answer away). Start from `chapter_template/solutions.json.sample`. Write LaTeX with the
Write tool or an editor, not a shell heredoc (a lost backslash turns `\times` into a tab; `check.py`
reports it). Figure labels are math mode: write `6\,\text{cm}`.

1. `python -B build.py --solution-worklist` lists the exercise items that have no `solutions.json` entry
   yet (with whatever steps and answer `content.py` already holds). Add one entry per item; the key is the
   item's coverage id (`cov`). Class 9/10: the key is the question id `<exercise>.Q<n>[.<part>]`.
2. `python -B core/solutions/gen_scenes.py <new_design>` writes `solution_images/` (one question scene and
   one solution scene per question, `manifest.json`, `plan_text.json`). With `"solution_continuation": true` in
   the config, a working longer than one card gets a second scene `<stem>_sol2.py` (manifest entries with `part`
   1 and 2; the first card is cut after `cut` steps, the second numbers on from there and carries the check, the
   answer box and the common-mistake note); `"cards"` / `"cut"` in a solutions.json entry override the automatic
   split. An existing scene file is kept
   (it may hold a teacher's edits from the editor); `--force` regenerates and resets it to draft.
3. `python -B core/solutions/render.py <new_design>` renders the missing PNGs (Manim, interpreter from
   `MANIM_PYTHON` in `.env`). An image that touches the frame edge is reported as a failure.
4. Open `python core/image_editor/server.py <new_design>/solution_images`, look at each card, edit the code
   if needed, Render, Approve. Images stay `draft` until approved.
5. `python -B core/solutions/check.py <new_design>` (build.py runs it too and stops on errors): schema, scene
   files, answer box and common-mistake note present, no hint word or answer number on a question card.
6. `build.py` writes the working and answer into the plan, adds the two image nodes and sets
   `media_ids = [question image, video, solution image]` on each question concept. The `solution_content`
   gate checks the result; the equation-truth gate checks the arithmetic in the steps.
7. Upload the images with `python -B core/solutions/attach.py <new_design> upload` (approved ones only;
   `--include-draft` to override), then continue with step 9 onward. Ask before the first real upload.

Class 9/10 (`docs/Yash_9&10/tools/build_std10_lp.py`) reads `std10_ch<N>/solutions.json` and
`std10_ch<N>/solution_images/` the same way: a covered question gets `solution_status: "authored"`, its
numbered steps and `Answer:` in the block text, and both image ids on the block. A question with no entry
stops the build (`--allow-stubs` writes a review-only draft that `check_std10_lp.py` flags). Question
videos are held for Class 10, so set `"solutions_video": false` in its config.

## 7. Run build.py's full build, including gates and QT

Run the chapter's `build.py` to assemble the final plan dict and write
`<chapter_id>.json`. A chapter's `build.py` is expected to, internally:

- call `gates/gate_runner.run()` (or an equivalent direct call into the gate
  modules) and refuse to write a broken plan;
- call `core/qt.py`'s `apply()` after assembly, to insert question-topic
  siblings - **check whether this chapter's `build.py` already does this**
  before running `qt.py` again by hand; it is a library call made from
  inside the build, not a separate step a human normally runs;
- call `core/published_media.py`'s `pin_images`/`pin_tools` (library calls,
  not CLI) on the assembled plan, if step 4 produced pin files, so published
  assets survive the rebuild.

If you are not sure a given chapter's `build.py` already does one of these,
read its own source before re-running the equivalent step by hand - running
QT insertion or asset pinning twice on the same plan will not produce the
same plan.

## 8. Pin rendered videos, if rebuilding over live assets

Only if this chapter is being rebuilt over a chapter that already has
rendered (not placeholder) videos live. This step changes the plan's bytes,
so it must run **before** `set_version.py`, same as pulling image/tool pins
had to happen before the build:

```bash
python core/published_media.py pin-videos <chapter_id> <version> <plan.json>
```

## 9. core/set_version.py

Sets the plan's final `version` and `plan_id`, reading the live max version
off the server so the local counter is never trusted alone:

```bash
python core/set_version.py <plan.json>
```

This must run **before** validation (step 10), because the stamp validation
writes has to hash the plan's FINAL bytes.

## 10. validation/validate_local.py

```bash
python validation/validate_local.py <plan.json>
```

Runs every wired-in gate family exactly as the plan sits on disk. On zero
errors, writes `<plan.json>.stamp.json` next to it, hashing the plan's own
bytes and the config's own bytes - a later edit of either invalidates the
stamp. On any error, removes a stale stamp if one exists and exits 1. See
`validation/STAMP_FORMAT.md` for the full field list and the staleness rules
(a stamp older than 24h, or one that no longer matches the file's bytes, is
treated as absent).

## 11. upload/upload_lp.py --dry-run

```bash
python upload/upload_lp.py <plan.json> --dry-run
```

There is no separate server-side "validate without uploading" endpoint -
this is confirmed absent from `upload/SKILL.md`. `--dry-run` is the closest
thing: it checks the stamp, runs the structural preflight, and prints what
would be sent, sending nothing. Always run this before the real upload so
the chapter_master_id/phase/shape can be read before anything goes out.

## 12. upload/upload_lp.py

```bash
python upload/upload_lp.py <plan.json>
```

Refuses to run (even with `--skip-preflight`) unless the stamp from step 10
is fresh and agrees with the exact bytes and phase being sent. Reads
`chapter_master_id` and `phase` from the plan itself by default (both are
form fields the endpoint does not read from the JSON); pass
`--chapter-master-id` only to assert the id you expect, never to override
it. `activate=true` is the default.

## 13. upload/verify_uploaded.py

```bash
python upload/verify_uploaded.py <plan.json>
```

Read-only: re-derives the verdict from the database rather than trusting the
upload's own JSON reply - exactly one active version for the chapter, and
the stored blob equal to the file leaf for leaf (`_activate` excepted, which
`?activate=true` sets). Requires this pipeline's own `.env`
(`DATABASE_URL`); if that is not filled in, say so rather than implying a
verification that did not happen.
