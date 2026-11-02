# Media authoring brief: Class 7 Chapter 8, Working with Fractions, Phase 2

Hand this file to whoever authors the chapter's images (and,
separately, the video scripts - see the note at the end). Delete this line and the word TEMPLATE
from the title once filled in.

You write JSON image specs for this chapter's concepts. They are placeholders; nothing is
rendered yet. Work in `chapters/maths7_ch8/new_design/` folder, filling in `media_specs/<key>.json`
next to `media_specs.py`.

## Inputs (read-only)

- `media_worklist.json` - one entry per concept key (`c7h.T2.C2` and so on, written by
  `build.py --worklist`). Use its fields: `key`, `concept_id`, `examples`, `exercises`,
  `video_focus`.
- `content.py`'s `FIGURES` dict - the book's own figures for a concept, keyed by the same authored
  concept key; the starting point for any image that needs one.
- `media_specs.py`'s `EXAMPLE_FILE` - a worked, checked example of one `media_specs/<key>.json`
  file's shape. **Copy its shape exactly**; do not invent new top-level keys.
- The book's own PDF: chapters/maths7_ch8 source PDF (read only). Only look at it if a figure is unclear - never copy its page
  numbers, figure numbers, or any wording from its captions into a spec.

## Output

- **One file per concept**: `media_specs/<key>.json` =
  `{"images": [...], "image_decisions": [...]}`.
- **Write one file at a time**, check it, then move to the next.
  `python -B media_specs.py --check media_specs/<key>.json`

## 1. One image decision per concept - even "no"

Every concept gets exactly one entry in `image_decisions`: `{"key", "needs_image", "why"}`.

- **Needs an image** when a figure carries the mathematics: the concept's `FIGURES` entry, or a
  diagram that makes a reasoning step visible (a number line with jumps, a counted array, a grid,
  a labelled shape). At most 2 images per concept; prefer 1.
- **Does not need one** on a DOER concept whose tool covers the manipulation, and on pure
  discussion/recap concepts. Say why in `why`.

## 2. Each image: one claim, exactly specified

Required fields (see `IMAGE_FIELDS` in `media_specs.py`): `key`, `title`, `purpose`,
`composition`, `exact_structure`, `labels`, `rejection`, `takeaway`, `description`, `context`,
`teaching_notes`.

- `exact_structure` must be specific enough that someone who has never seen the image could count
  every shape, every row, every token from this text alone - this is what the generation prompt is
  built from.
- `labels` is the **exhaustive** list of visible text; nothing else is allowed in the frame.
  Numbers must match the book/concept exactly.
- Tokens, if used, follow the chapter's palette (see `PALETTE`/`IMAGE_TREATMENT` in
  `media_specs.py`): positive green `#009E73` with a white plus sign, negative vermilion `#D55E00`
  with a white minus sign - the sign glyph is always drawn, colour is never the only cue.

## Hard rules, all checked by the machine (`gates/media_content.py`'s `preflight()`, and this
chapter's own `media_specs.py --check-all`)

- **No en dash or em dash anywhere** (`—`/`–`). Use a comma, colon, or the word "to".
- **Minus is U+2212 (−), never an ASCII hyphen**, in any number.
- **No branding, ever**: never write `NCERT`, `CBSE`, `textbook`, or "page `<N>`"/"p. `<N>`" in
  any field this image's student-facing output touches (`title`, `labels`,
  `generation_prompt`/`exact_structure`, `negative_prompt`, `accuracy_constraints`). These words
  are fine only in this brief and in internal-only fields (`context`, `teaching_notes`) - never in
  anything the student sees or that drives what gets drawn. (This mirrors
  `gates/media_content.py`'s own whitelist: `STUDENT_FACING_FIELDS = {"title",
  "instructions_for_student", "generation_prompt", "video_script", "labels",
  "accuracy_constraints", "negative_prompt", "tool_name"}`.)
- **Check every file** with `python -B media_specs.py --check media_specs/<key>.json` and fix
  until it shows 0 problems.
- **Mathematics must be right and match the book.** Recompute anything a figure states.

**When done**, reply in under 80 words: the keys finished, and anything unresolved. Put no spec
content in the reply.

## A note on videos

Videos are **not** briefed here. Every video in this pipeline is a docs/28 script file under
`video_scripts/<key>.json`, written to the `core/video_script` contract (word/beat limits, the
four script rules: no tool references, the hook's one photo, nothing outside the textbook per
`book_rules.json`, and a `state` beat for every theorem video). Brief a video author with
`video_worklist.json` (written by `build.py --video-worklist`) and the project's docs/28 contract
directly, not with this file.
