# 00. Overview

## "New design" methodology

A "new design" chapter is one plan JSON, hand-built by a chapter-specific
`build.py` against the book's own content, and checked by a shared gate
library before it goes anywhere near the database. This pipeline calls that
**System B**: a per-chapter builder plus shared gates, as opposed to **System
A** (`pipeline/build_chapter.py` / `conform_to_software_schema.py` in the
older checkout, which mechanically reshapes an existing plan to fit a
software schema). System A is explicitly not used here and must never be run
on a plan this pipeline produced - it was built for a different generation
of plans and will silently mangle one of these.

Concretely, System B means:

1. A chapter gets its own folder, cloned from `chapter_template/`, with its
   own `build.py`, its own authored content modules, and its own
   `chapter.config.json` (which gate variant, which errata, if any).
2. `build.py` assembles one Phase 2 plan dict from that authored content -
   modules, segments, topics, concepts, media, objectives - and writes it to
   disk as `<chapter_id>.json`.
3. Every gate family in `gates/` runs against the result, first from inside
   `build.py` itself (so a build fails loudly rather than writing a broken
   file), again from `validation/validate_local.py` (which is what actually
   gates the upload).

There is no intermediate "Phase 3" plan and no `_V3` chapter anywhere in this
pipeline. See the README for why.

## The shared gate families

`gates/gate_runner.py` is the single entry point (`run(plan, config) ->
(errors, counts)`) that every other gate-aware script calls, so there is one
source of truth for "did this plan pass." As of this writing it wires in:

- **`media_content.py`** - structural/delivery gate: the breaks the upload
  API itself will accept without complaint. Enum-valid media types, no
  duplicate media ids, no retired `tool_2d` spelling, no em/en dashes,
  contiguous segment/topic/concept ids, every topic carrying
  `available_content_types`, every tool carrying a filled `2d_tool_url` and
  `tool_config.tool_questions`, every asset url under the plan's own
  `class_<grade>`, and no textbook branding in any student-facing field.
- **`eqcheck_plain.py` / `eqcheck_signed.py` / `eqcheck_powers.py`** -
  arithmetic-truth gates on every authored string in the plan (content
  blocks, objectives, tool configs). One variant per chapter, chosen by
  `chapter.config.json`'s `"eqcheck"` key: `plain` for non-negative,
  power/root-free chapters, `signed` for any chapter with negative numbers
  (the superset - also understands powers/roots), `powers` for powers/roots
  without negatives. A known, deliberately-kept printed-book error is
  exempted by exact chain text via `chapter.config.json`'s `eqcheck_errata`,
  and the gate itself fails if an exemption is never matched - a stale
  exemption can't linger silently.

Also wired into `gate_runner.run()`, branched by `grade_band`/`theorem_chapter`
(see `gates/gate_runner.py`'s own module docstring for the exact condition):

- **`skeleton.py`** - the plan's structural skeleton: module/segment/topic/
  concept nesting, framing and summary topics present and in the right
  place, the shape every chapter must share regardless of content. Runs for
  Class 6-8 chapters only - its source_type vocabulary and "idea topic ends
  in a doer concept" rule don't hold for Class 9/10's theorem shape.
- **`objectives.py`** - the two required objective levels (topic objective +
  per-concept objective), one objective per concept with no gaps, enrichment
  concepts carrying no objective. Same Class 6-8-only scope as `skeleton.py`.
- **`coverage.py`** - 100% content coverage of the book: every printed
  example, exercise and Figure-it-Out item traceable to a concept. Always
  runs, every grade band.
- **`video_script_rules.py`** - the mechanical half of the video-script
  contract (see `docs/02`): lengths, bookmarks, banned words, kind-specific
  structure, book-number stripping. Always runs, every grade band.
- **`theorem_variant.py`** - the Class 9/10 theorem-chapter rules that are
  mechanically checkable (see `docs/04`, rules 1-8). Runs in place of
  `skeleton.py`/`objectives.py` whenever `grade_band == "9_10"` or
  `theorem_chapter` is true.

`gate_runner.run(plan, config)` returns `(errors, counts)`. `errors` is what
`validation/validate_local.py` gates the stamp on. `counts["warnings"]` is a
second, non-blocking list, but a message only qualifies by actually firing
on a real, already-live reference chapter during parity testing - an
own-content word-overlap check in `objectives.py` (fired on `maths8_ch9`),
an informational "mapped to more than one concept" count in `coverage.py`
(fired on `maths6_ch3`/`maths9_ch5`/`maths9_ch6`, all deliberate double
mappings), and a "cannot be verified" note in `theorem_variant.py`'s rule 1
(fired on `maths9_ch5`/`maths9_ch6`) - real signal for a human to read, not
something the stamp should ever block on. A sibling heuristic in
`objectives.py` ("topic objective covers") never fired on any reference
chapter and was left blocking for exactly that reason - its own docstring
calling it shallow was not, on its own, grounds to exempt it. Every other
message from every gate is blocking. Read `gates/gate_runner.py` itself for
the exact, current wiring and the exact set of advisory message patterns.

## QT pass (question-topic insertion)

`core/qt.py` is a build-time step, not a CLI tool: a chapter's `build.py`
calls `qt.apply(plan, vslots_all, media_tag, strand_map)` after assembling
the plan, to insert one "Practise: <topic>" sibling topic directly after
every instructional topic that carries exercise video slots. One QT concept
per exercise item; the worked-example block for that item moves out of the
teaching concept and into the new QT concept; videos and media stay where
they are, just re-pointed. The chapter is renumbered (S#/T#/C# all reassigned
in document order) and objectives rebuilt to match - `qt.apply` returns the
old-id-to-new-id map so a caller can re-key its pin files
(`qt.remap_pin_file`, run once, only when QT is first turned on for a chapter
that already has pin files).

## Question layout (Class 6-8)

With `"question_layout": true` in `chapter.config.json` (the sample and `lp_start.py` set it for Class 6-8) the
chapter reads

    concept topic -> one "Questions: <category>" topic per book category found there -> next concept topic -> ...

and each Questions topic holds, for every book question of its own category, in the book's order, **two
sibling concepts**: a question concept (just the question) and an answer concept (the working, the answer
and the video) - every solved example printed in the book, every Figure it Out / exercise question and every
answerable in-text prompt (a Try This with an answer, "answer the following", a blank to fill). Math Talk
discussion prompts are not questions and stay in the teaching text. The author writes each as an `FIO(...,
kind="example" | "exercise" | "prompt")` item in the topic's DOER; `build.py` calls `qt.apply(...,
enrichment_qt=True, topic_prefix="Questions")`, which moves the item out of the teaching topic and splits it.
A concept topic keeps only the plan's own teaching examples (`WE`, with their own numbers).

`core/question_naming.py` names the topic and both concepts from the item's own printed book label (`FIO`'s
`book` argument), by category:

    category        topic                           question concept       answer concept
    exercise        Questions: Exercise Set 5.1      Exercise Set 5.1: Q1   Exercise Set 5.1: Ans1
    figure_it_out   Questions: Figure it Out 5.1      Figure it out: Q1     Figure it out: Ans1
    example         Questions: Example               Example 1: Q          Example 1: Ans
    let_us_do       Questions: Let us do             Let us do: Q1         Let us do: Ans1
    other           Questions: <the label's heading> <heading>: Q1         <heading>: Ans1

A teaching topic whose questions span more than one category gets one Questions topic per category, in book
order, immediately after the teaching topic and after each other - never one topic mixing categories.
`gates/skeleton.py` and `gates/question_layout.py` both allow a run of several Questions topics after one
teaching topic for exactly this reason. "example" concepts keep the book's own example number in the title
itself and need no running count; every other category counts "Q1"/"Ans1", "Q2"/"Ans2", ... in book order
within its own topic. This naming and splitting is chapter_template's own (`topic_prefix="Questions"`); other,
older per-chapter build scripts (`own_video`/`keep_first`/`name_fn`, no `topic_prefix`) keep one concept per
question, untouched. `core/question_layout_live.py` (retrofitting an already-live chapter) picks up the
category-based topic name automatically when every question under one Questions topic happens to share a
category, but does not split a mixed topic or split a question into two concepts - that engine's concept
names are still typed by the author directly, in this same convention
(`core/question_layout_AUTHOR_BRIEF.md`).

The question concept carries only its question card, as a placeholder from the first build:

    media_ids = [IMG1 question card]

The answer concept carries the video and the solution card(s):

    media_ids = [VID1 video (if authored yet), IMG1 solution card (, IMG2 solution continued)]

The question card shows the question and, only when the question needs one, a diagram (`q_figure`); the
solution card is the numbered working and highlighted answer (`s_figure` for a diagram); a second solution
card exists only when the working is too long for one (`core/solutions/layout.py`: more than
`question_image_max_lines`, default 8, wrapped lines; the chapter must set `solution_continuation`).
`core/solutions/placeholders.py` writes these nodes (`build_status: "placeholder"`, reserved urls - the
bucket file is always `<coverage stem>.IMG1/2/3.png` regardless of which concept the card lives on, so the
numbering a chapter author sees in the plan still runs IMG1 (question), IMG2, IMG3 (answer) even though IMG1
is now on a different concept than IMG2/IMG3 - Manim scene names, the diagram sentence in the description),
`build.py --placeholders` builds the plan at this stage with no `solutions.json` yet, and `gen_scenes.py` /
`render.py` / `attach.attach` later replace a placeholder with the real card, a second scene `<stem>_sol2.py`
for a continued working. The answer box and the common-mistake note sit on the last solution card only.

**Displayed text is LaTeX once a question has a solutions.json entry.** solutions.json already authors
`question_tex`/`given`/`find`/`method`/`steps`/`answer_tex` as prose with inline maths in `$...$`
(`core/solutions/schema.py`); `bind.fill()` sets these, unflattened, as `question_tex`/`steps_tex`/`answer_tex`
alongside the plain `question`/`steps`/`answer` it has always set (from `schema.plan_fields`, which flattens
the same LaTeX to plain text) - `gates/eqcheck_*` keep reading the plain fields, unaffected. The question and
answer concepts' own displayed text (`chapter_template/build.py`, `core/qt.py`) is built from the `_tex` fields
when present, so the student reads the maths as `$...$` LaTeX instead; a question with no solutions.json entry
yet stays plain text. When the working spans two solution cards, the answer concept's text is tagged
`[Image: <title>]` right after the steps shown on each card (`core/solutions/layout.py:tagged_text`, called by
`placeholders.py` and by `attach.py` once the real cards and their titles exist) - a single-card answer needs
no tag.

`gates/question_layout.py` checks the order and naming of the topics, that no book question is left in a concept
topic, and (from the kinds in `content.NCERT_ITEMS`) that every example / exercise / prompt is in a Questions
topic; `gates/solution_content.py` checks the cards. `reference_rebuild/layout_toy/run_smoke.py` is the
end-to-end test of all of this. Chapters built before the layout keep their own config and are unaffected.

The inserted topic is written straight as `topic_type: "instructional"`,
because this pipeline's Phase 2 API has never accepted `"question_topic"` as
a `topic_type` and there is no later patch step to demote it (unlike the
older checkout's approach). `source_type`/`topic_category` stay
`"question_topic"`/`"practice"` so a gate or a human can still tell a QT
topic apart from a taught one without relying on `topic_type`.

## Published-asset pinning

`core/published_media.py` keeps a rebuild from silently deleting live
assets. A builder always writes a fresh image/tool node as a placeholder
(`image_url: ""`, no `2d_tool_url`); if the live chapter already has built
images or tools, uploading that placeholder-shaped rebuild takes every
picture or tool off the page while still answering `success: true`. So:

- `pull` / `pull-tools` (CLI, run **before** the build) fetch the live
  chapter's built image/tool nodes into a local pin file
  (`published_images.json` / a tools pin file), matched by media id.
- `pin_images(plan, path)` / `pin_tools(plan, path)` (library calls `build.py`
  makes on the assembled plan) swap each local placeholder node for its
  pinned published node, keeping only `id`/`concept_id`/`home_concept_id`
  local.
- `pin_videos` (CLI, run **after** `set_version.py`, exactly where
  `STAMP_FORMAT.md` orders it) patches rendered video urls from the live
  version directly into the plan file on disk, since rendered videos have
  sometimes been patched straight into a live blob without ever existing in
  a local file.

See `docs/01_runbook.md` for exactly where each of these sits in the build
order, and `validation/STAMP_FORMAT.md` for why the order is non-negotiable.
