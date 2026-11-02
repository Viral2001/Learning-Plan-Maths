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
