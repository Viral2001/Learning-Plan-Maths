# Learning-Plan JSON Field Cleanup Guide

How to find and remove unnecessary/leftover fields from an already-built, delivered
`learning_plan_logical.json` (or any `<chapter_id>_v<N>.json`) — the exact procedure used on three
chapters already done this way: one Number/Algebra chapter in the 6-8 band, one theorem chapter in
the 9-10 band, and a second 6-8 band chapter.

Use this to clean any other chapter's plan the same way, and to know when the rule changes.

---

## 1. Why these fields exist at all

This pipeline (`Learning-Plan-Maths/`) has gone through several generations — an older checkout,
a `restructure.py`-style migration for some chapters, and the current `chapter_template/build.py` +
`core/qt.py` generation. Each generation's build-time bookkeeping (locators, role tags, draft-state
flags) sometimes leaked straight into the final delivered plan instead of staying internal. An
external, field-by-field reference doc (a sibling pipeline's schema, used here only as a
sanity-check, not ground truth) and the real upload contract doc agree that a sizeable minority of
fields in a delivered plan are never read by anything downstream — they just ride along in the JSON.

**The only authority that actually matters for *this* pipeline is its own gate code**
(`Learning-Plan-Maths/gates/*.py`) and its own core machinery (`Learning-Plan-Maths/core/*.py`),
not the external reference doc. A field the reference doc doesn't recognize can still be essential
here; the reverse is also true. Every verdict below is backed by `grep`-level evidence — the exact
file and line that reads the field — not by the field's name or by what the reference doc says it
"should" be.

---

## 2. Step 0 — work out which gate family is active (this changes the answer)

Two different rule sets apply depending on the chapter's grade band, because
`gates/gate_runner.py` runs a **different** structural gate depending on it:

| grade_band | Active structural gate | Inactive |
|---|---|---|
| 6-8 (`grade_band` not `"9_10"`, `theorem_chapter` not true) | `gates/skeleton.py` + `gates/objectives.py` | `gates/theorem_variant.py` |
| 9-10 (`grade_band == "9_10"` or `theorem_chapter: true`) | `gates/theorem_variant.py` | `gates/skeleton.py`, `gates/objectives.py` |

`gates/coverage.py`, `gates/video_script_rules.py`, `gates/media_content.py`'s `preflight()`, and
`gates/eqcheck_*` run **regardless of grade band**. `gates/solution_content.py` runs whenever the
chapter's config has `"solutions"` truthy (true for almost every chapter). `gates/question_layout.py`
runs only when `"question_layout": true` (a Class 6-8 convention; Class 9-10 doesn't use it).

**A delivered JSON usually has no `chapter.config.json` sitting next to it**, so detect the band
from the plan itself:
- `root["grade"]` — 6, 7 or 8 → the 6-8 family; 9 or 10 → the theorem family.
- Corroborating signals for the theorem family: concept-level `theorem_id` / `theorem_video_id`
  fields, content `block_kind` values `theorem_statement` / `proof`.
- Corroborating signals for the 6-8 family: topics literally named `"Questions: <topic>"`
  alternating with their teaching topic (the question-layout pattern).

This matters because a handful of fields are read by **one** family and not the other — removing
them is only safe on the side that doesn't read them.

---

## 3. The master field table

Levels follow the plan's own nesting: `modules[] → segments[] → topics[] → concepts[] → content[]`,
plus `objectives[]` (root array) and each topic's `media[]`.

**Status key** — `REMOVE` (safe everywhere, confirmed unread), `REMOVE (6-8 only)` /
`REMOVE (9-10 only)` (grade-band dependent), `RENAME` (the data is real, the field name is wrong),
`NEVER REMOVE` (read by a gate or core module), `CHECK VALUE FIRST` (name alone isn't enough).

### Root level

| Field | Status | Evidence |
|---|---|---|
| `video_coverage` | `REMOVE` *(delivered plan only — see caveat)* | `gates/video_script_rules.py` reads `plan.get("video_coverage")` directly, and that gate **always** runs. Safe to drop only from a plan that will never again be fed through `validate_local.py`/`gate_runner.py` in this pipeline. If the chapter might still be rebuilt or re-validated, keep it. |
| `objective_level` | n/a at root | (it's an `objectives[]` field, see below) |
| `_activate`, `chapter_master_id`, `medium_id`, `phase`, `subject_ref_id`, `source_metadata` | `NEVER REMOVE` | Either server-injected upload-contract fields (the real upload contract doc, outside this pipeline) or pipeline bookkeeping genuinely consumed on import. Not part of this cleanup. |

### `objectives[]`

| Field | Status | Evidence |
|---|---|---|
| `objective_level` | `REMOVE` | Never read anywhere in `gates/` or `core/`; it was only ever written by `core/qt.py`'s own dict literal (removed at the source too). |
| `legacy_id`, `strand` holding the wrong *value* (raw module id / authored key instead of a real strand-code) | Not a removal — a **value** fix, see Appendix B. Leave as-is unless you're doing the full value-correctness pass. |

### `topics[]`

| Field | Status | Evidence |
|---|---|---|
| `estimated_minutes` | `REMOVE` | Not read by any gate. Only ever used transiently (during a live build) to sum into the root `estimated_time`, which is already a fixed number in a delivered plan. |
| `source_content_flow` | `REMOVE` | Not referenced anywhere in `gates/` or `core/`. |
| `ncert_sections` | `RENAME` → `source_topic_ids` | Not gate-read under the old name, but the data (book section numbers) is real. The field reference's name for it is `source_topic_ids`; rename rather than delete. |
| `source_type` | `REMOVE (9-10 only)` / `NEVER REMOVE (6-8)` | `gates/skeleton.py`, `gates/objectives.py`, `gates/question_layout.py` all read `topic.get("source_type")` — none of them run for a theorem chapter. `gates/theorem_variant.py` never reads it. |
| `topic_objective` | `NEVER REMOVE` | Read by `gates/skeleton.py`, `gates/objectives.py`, **and** `gates/theorem_variant.py` (line ~127), plus `gates/gate_runner.py`'s own arithmetic-truth text scan. Needed in both grade bands. |
| `is_enrichment` (topic-level, when present) | `NEVER REMOVE` | `gates/skeleton.py` reads it on the intro/summary topics (6-8). |
| `source_segment_role` | n/a at topic level (it's a concept field) | |

### `concepts[]`

| Field | Status | Evidence |
|---|---|---|
| `tool_media_id` | `REMOVE` | Only ever *mentioned in a docstring* (`gates/theorem_variant.py`'s module doc) — no gate code anywhere actually does `concept.get("tool_media_id")`. The real tool-to-concept link is derived from the tool media node's own `concept_id`. Confirmed safe for both grade bands. |
| `source_tool_ref` | `REMOVE` | Same as above — docstring-only, never read in code. |
| `walkthrough_video_id` | `REMOVE` | Pure `build.py` convenience duplicate of `video_media_ids[0]`; nothing reads it back. |
| `authored_key` | `REMOVE` | A build-time locator (`"T2.C1"` style) consumed only *during* `core/qt.py`'s own algorithm; nothing reads it from the finished plan. |
| `media_key` | `REMOVE` | Not referenced anywhere. |
| `image_decision` | `REMOVE` | An authoring-rationale object from `media_specs.py`'s own bookkeeping; current `build.py` never copies it onto the final concept dict. |
| `source_delivery_mods` | `REMOVE` | Not referenced anywhere. |
| `estimated_minutes` | `REMOVE` | Same reasoning as the topic-level field. |
| `source_segment_role` | `REMOVE (9-10 only)` / `NEVER REMOVE (6-8)` | `gates/skeleton.py` (the "doer"/"hook" concept-role rule) and `gates/objectives.py` read it; `gates/theorem_variant.py` never does. |
| `is_enrichment` | `NEVER REMOVE` | Read by `gates/skeleton.py`/`gates/objectives.py` (6-8) **and** `gates/theorem_variant.py` rule 4 (9-10, line ~319) — needed everywhere. |
| `_is_thin_extra` | `NEVER REMOVE` (when present) | `gates/skeleton.py` reads it via its `thin_extra_field` config entry (6-8). Harmless to keep even on a 9-10 plan that happens to carry it. |
| `enrichment_type`, `media_ids`, `video_media_ids`, `ncert_refs`, `misconceptions`, `source_media` | `NEVER REMOVE` | Not part of this cleanup — these carry real, used content/linkage. |

### `media[]` — type `"image"`

| Field | Status | Evidence |
|---|---|---|
| `regions`, `source_image`, `source_image_key`, `tutor_can_highlight` | `CHECK VALUE FIRST`, then usually `REMOVE` | Never read by any gate or `core/` module **at the image top level**. In every chapter checked so far these were constant/empty filler (`[]`, `""`, or a fixed `{"note": "..."}` dict) — confirmed by diffing distinct values across every image before deleting. **Do not** assume this from the name alone; see §4. |
| `image_role` | `NEVER REMOVE` | `gates/solution_content.py` and `gates/theorem_variant.py` both key off it directly (`"question"` vs `"solution"`). |
| `build_status` | `NEVER REMOVE` | The pipeline's asset-state machine: `core/published_media.py`, `core/qt.py`, `core/solutions/placeholders.py`/`attach.py`, `core/video_script/node.py` all read or branch on it. |
| `planned_url` | `NEVER REMOVE` | `core/qt.py` explicitly freezes/validates it; `core/video_script/node.py`, `core/question_layout_live.py` also depend on it. |
| `render_source` | `NEVER REMOVE` | `gates/solution_content.py` checks `render_source.code_url` directly (confirms the Manim source exists). |
| `serves_item`, `source_media_id`, `reused_in_topics` (seen on some chapters' images) | Leave alone | Not part of the agreed removal list; carry real linkage in at least one chapter checked. |

### `media[]` — type `"2d_tool"`

| Field | Status | Evidence |
|---|---|---|
| `tool_id` (**top-level** media field only) | `REMOVE (9-10 only)` / `NEVER REMOVE (6-8)` | `gates/objectives.py` reads `m.get("tool_id")` to build a tool-name/id dedup set — that gate never runs for a theorem chapter. |
| `tool_name` | `NEVER REMOVE` | `gates/media_content.py`'s STUDENT_FACING text-hygiene scan includes it, and that gate **always** runs (not grade-band gated). `gates/objectives.py` also reads it (6-8). |
| `build_status` | `NEVER REMOVE` | Same asset-state reasoning as images. |
| `related_concept_ids` | Not a removal — should always be `[]` (field reference's own rule: a 2d_tool is never shared). Fix the *value*, don't delete the field, if it's ever non-empty. |
| `tool_config` **internal** keys (`hint_policy`, `values_policy`, and — in at least one chapter — nested `regions`/`tutor_can_highlight`/`tool_id`) | `CHECK VALUE FIRST`, case by case | `tool_config` isn't validated field-by-field by any gate, so trimming it is always technically safe, but only trim what's demonstrably redundant. `hint_policy`/`values_policy` were confirmed **identical, constant text across every single tool in a chapter** before being trimmed (pure boilerplate). The *same field names* nested inside `tool_config` in a different chapter (Class 9 Ch 6) carried **real, per-tool diagram-region data** for most tools — those were left alone. Always check the actual values across every tool before trimming anything inside `tool_config`. |

---

## 4. The one rule that matters more than any table: check the value, not just the name

The single biggest mistake this exercise could make is deleting a field because its *name*
appeared on an earlier chapter's removal list. Two things broke that assumption in practice:

1. **Grade band changes what's gate-read.** `source_type`, `source_segment_role` and the top-level
   `tool_id` are load-bearing for a 6-8 chapter and dead weight for a 9-10 one. Always redo §2's
   detection and re-check the table above per chapter — don't just copy the previous chapter's
   removal list verbatim.
2. **The same field name can hold real data in one place and filler in another.** `regions` /
   `tutor_can_highlight` are always-empty filler at the top level of an `image` node in every
   chapter checked — but the *identical names*, nested one level deeper inside a 2d_tool's
   `tool_config`, held real per-tool diagram-highlight data in the Class 9 Ch 6 file. Before
   deleting anything inside `tool_config`, print the distinct values across every tool in the
   chapter first (`set(json.dumps(t["tool_config"].get(k)) for t in tools)`); only delete if it's
   constant/empty everywhere.

When in doubt, run the one-line check: grep `gates/*.py` for `.get("<field>")` or `["<field>"]` —
not just the field's name in a comment or docstring (several fields, e.g. `tool_media_id` and
`source_tool_ref`, are *mentioned* in a gate's docstring prose but never actually read in its code).

---

## 5. Step-by-step procedure for a new chapter file

1. **Back up the file** (`cp file.json file.json.bak`) before writing anything.
2. **Detect the grade band** (§2): read `root["grade"]`, skim a few topics/concepts for
   `theorem_id`/`theorem_statement` vs `"Questions: "`-prefixed topic names.
3. **Dump the field union** at every level (objectives / modules / segments / topics / concepts /
   each media type) with a small Python script (union of `.keys()` across every instance) — don't
   assume this chapter has exactly the same fields as the last one. New/unfamiliar field names
   should be left alone unless you can find where they're read.
4. **Walk the master table (§3)** against the actual field union, applying the grade-band-specific
   rows from §2.
5. For any field whose name matches something flagged `CHECK VALUE FIRST`, dump its distinct values
   across every instance in the chapter before deciding.
6. **Apply the removals** with a small script (see §6) — never by hand-editing 50k+ lines of JSON.
7. **Verify**: concept/objective counts unchanged, every removed field gone, every declined field
   still present, `json.load()` still parses cleanly.
8. Delete the backup only after verification.

---

## 6. Reusable script template

Adapt the `REMOVE_*` tuples per chapter's grade band (§2/§3) — this is exactly the shape of the
scripts used on the three chapters already done.

```python
# -*- coding: utf-8 -*-
import io, json

PATH = r"<path to the chapter's learning_plan json>"
GRADE_BAND = "6_8"   # or "9_10" - set from root["grade"] / theorem_id signals, see guide section 2

with io.open(PATH, encoding="utf-8") as f:
    d = json.load(f)

all_topics = [t for m in d["modules"] for s in m["segments"] for t in s["topics"]]

# ---- always safe, both grade bands ----
d.pop("video_coverage", None)                       # only on a FINAL delivered plan, see 3. Root
for o in d["objectives"]:
    o.pop("objective_level", None)

REMOVE_CONCEPT_ALWAYS = ("tool_media_id", "source_tool_ref", "walkthrough_video_id",
                         "authored_key", "media_key", "image_decision",
                         "source_delivery_mods", "estimated_minutes")
REMOVE_IMAGE_ALWAYS = ("regions", "source_image", "source_image_key", "tutor_can_highlight")
# ^ check these are actually constant/empty in THIS chapter before trusting this list - see section 4

# ---- grade-band-dependent (6-8 only; theorem_variant.py doesn't read these, so a 9-10 chapter can
#      ALSO remove them - flip this block for a 9-10 chapter) ----
REMOVE_TOPIC_IF_6_8 = ()            # source_type is kept for 6-8 (skeleton.py/objectives.py need it)
REMOVE_CONCEPT_IF_6_8 = ()          # source_segment_role is kept for 6-8
REMOVE_MEDIA_2D_TOOL_IF_6_8 = ()    # tool_id (top-level) is kept for 6-8 (objectives.py needs it)
if GRADE_BAND == "9_10":
    REMOVE_TOPIC_IF_6_8 = ("source_type",)
    REMOVE_CONCEPT_IF_6_8 = ("source_segment_role",)
    REMOVE_MEDIA_2D_TOOL_IF_6_8 = ("tool_id",)

for t in all_topics:
    t.pop("estimated_minutes", None)
    t.pop("source_content_flow", None)
    if "ncert_sections" in t:
        t["source_topic_ids"] = t.pop("ncert_sections")
    for k in REMOVE_TOPIC_IF_6_8:
        t.pop(k, None)
    for c in t.get("concepts", []):
        for k in REMOVE_CONCEPT_ALWAYS + REMOVE_CONCEPT_IF_6_8:
            c.pop(k, None)
    for med in t.get("media", []):
        if med.get("type") == "image":
            for k in REMOVE_IMAGE_ALWAYS:
                med.pop(k, None)
        elif med.get("type") == "2d_tool":
            for k in REMOVE_MEDIA_2D_TOOL_IF_6_8:
                med.pop(k, None)

with io.open(PATH, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=1)
print("patched", PATH)
```

Verification snippet to run after, every time:

```python
topics = [t for m in d["modules"] for s in m["segments"] for t in s["topics"]]
concepts = [c for t in topics for c in t["concepts"]]
print("concepts:", len(concepts), "objectives:", len(d["objectives"]))
print("leftover:", {k for c in concepts for k in
      ("tool_media_id","source_tool_ref","walkthrough_video_id","authored_key","media_key",
       "image_decision","source_delivery_mods") if k in c})
```

---

## Appendix A — what was actually done to the three chapters checked

| | Class 7 Ch 10 | Class 9 Ch 6 | Class 6 Ch 3 |
|---|---|---|---|
| Grade band | 6-8 | **9-10 (theorem)** | 6-8 |
| `video_coverage` removed | yes | yes | yes |
| `objective_level` removed | yes | yes | yes |
| `estimated_minutes`, `source_content_flow` removed | yes | yes | yes |
| `ncert_sections` → `source_topic_ids` | yes | yes | yes |
| `source_type` removed | **no (declined)** | **yes** | no (declined) |
| `source_segment_role` removed | **no (declined)** | **yes** | no (declined) |
| `tool_id` (top-level) removed | **no (declined)** | **yes** | no (declined) |
| `tool_media_id`, `source_tool_ref`, `authored_key`, `media_key`, `walkthrough_video_id` removed | yes (where present) | yes (where present) | yes (where present) |
| Image `regions`/`source_image`/`source_image_key`/`tutor_can_highlight` removed | yes | yes (only `source_image*` were present) | yes |
| `is_enrichment`, `topic_objective`, `image_role`, `build_status`, `planned_url`, `render_source`, `tool_name` | declined everywhere | declined everywhere | declined everywhere |
| Extra: `tool_config.hint_policy`/`values_policy` trimmed (confirmed constant across every tool) | yes | not requested | not requested |
| Extra: nested `tool_config.regions`/`tutor_can_highlight` | n/a | **left alone — real per-tool data** | n/a |

This is exactly why §4 exists: the Class 9 file alone shows three fields flipping from "never
remove" to "remove" purely because of grade band, and one more case where the same field *name*
had to be kept because its *value* was real.

---

## Appendix B — the deeper "wrong values" pass (only done once, on the Class 7 file)

Field removal is the narrow task this guide covers. A second, deeper pass was also done once (on
the Class 7 chapter's plan only) that doesn't delete fields but **corrects their values**
against the field reference's own rules. Only apply this if specifically asked for "fix the wrong
values," not as part of a routine field cleanup:

- `available_content_types` recomputed from the topic's own actual `media[]` (never seeded with a
  non-media `"text"`/`"paragraph"` filler).
- `primary_content_type`/`secondary_content_type`/`tertiary_content_type` recomputed with priority
  `image > video > 2d_tool > 3d_tool` (video is primary only on the chapter's first topic).
- Every `2d_tool.related_concept_ids` forced to `[]`.
- `objectives[].strand`/`legacy_id` recomputed as a real strand-code (e.g. `N1`, `A12`) from a
  module → strand-letter catalog, instead of the raw module id / an authored-key-shaped locator;
  `strand_to_objective_map` rebuilt to match.
- 12 image fields the reference spec expects but the chapter never had (`grounding_quote`,
  `heading`, `heading_style`, `label_style`, `objects`, `scientific_facts`, `composition`,
  `predict_then_reveal`, `enrichment`, `source_figure`, `source_topic_no`, `source_page`) added
  with sensible derived/default values.
- `word_count` added to every topic, computed from its own concepts' text.

These same corrections were also made in the live pipeline code
(`chapter_template/build.py`, `core/qt.py`, `tools_spec/tool_node_builder.py`,
`core/solutions/placeholders.py`/`attach.py`, `gates/media_content.py`) so **future** chapters
built from `chapter_template/` come out correct the first time — see that code's own comments for
the equivalent reasoning file-by-file.

---
---

# Part 2 — Category Naming, Question/Answer Split & LaTeX Conversion Guide

A different, usually earlier-in-the-pipeline transformation from Part 1's field cleanup: turning a
chapter's book questions — however they currently sit in the plan — into the pipeline's real target
shape: `"Questions: <category>"` topics, a question concept paired with an answer concept for every
book item, strict inline-LaTeX display text, and a verified-present worked solution for every single
one. Done in full on:

- Class 6 Ch3 — NCERT "Number Play" (Ganita Prakash), "Figure it Out" box structure, 72 question
  concepts → 144 Q/Ans concepts, 14 "Questions:" topics → 27.
- Class 9 Ch6 — NCERT "Circles" / Heron's formula, numbered "Exercise Set X.Y" structure, already
  split before this pass but missing a required structural field (§8).

Use this to apply the same four-part transformation — naming, split, LaTeX, answer-presence — to any
other chapter. Everything in Part 1 above still applies independently; a chapter may need either
part, or both, or neither.

---

## 1. The real pipeline shape — read the code, don't guess

Before writing one line of a transformation script, read these source files directly. They are the
actual shape the gates validate — not a convention to reverse-engineer from a prior session's own
scratch script. (One such script, written under time pressure for the first chapter done, invented
`_qt_part` instead of the real `qt_part`, and `enrichment_type: "content"` instead of the real
`"enrichment"` — both wrong, caught only once this exact question was dug into properly for the
second chapter. Don't repeat that: read the real source every time, even if an old script "worked".)

- **`core/question_naming.py`** — `classify(label, coverage_id)` → `(category, topic_suffix,
  concept_prefix)`, and `topic_title()` / `concept_title()`. The literal source of the
  `"Questions: <category>"` / `"<category>: Q<n>"` / `"<category>: Ans<n>"` naming convention,
  including the exact category table:

  | category | topic (`"Questions: ..."`) | question concept | answer concept |
  |---|---|---|---|
  | `exercise` | Exercise Set 5.1 | Exercise Set 5.1: Q1 | Exercise Set 5.1: Ans1 |
  | `figure_it_out` | Figure it Out 5.1 (or bare `Figure it Out` if no section number is derivable) | Figure it out: Q1 | Figure it out: Ans1 |
  | `example` | Example | Example 1: Q (no running count — the book's own example number is the whole prefix) | Example 1: Ans |
  | `let_us_do` | Let us do | Let us do: Q1 | Let us do: Ans1 |
  | `other` | the label's own heading | `<heading>`: Q1 | `<heading>`: Ans1 |

- **`core/qt.py`** — the real question/answer split (`_question_answer_blocks`) and the exact
  concept/topic dict shape `apply()` builds. Search for `qt_part`, `is_enrichment`,
  `enrichment_type`, `objective_id: None` — these are non-negotiable field values, not stylistic
  choices.
- **`gates/solution_content.py`** / **`gates/latex_content.py`** / **`gates/question_layout.py`** —
  what is actually validated: media_ids ordering, `image_role`, LaTeX correctness, topic/question
  layout. Read these to know what "correct" means before building toward it.
- **`core/solutions/LATEX_REFERENCE.md`** + **`core/solutions/latex_convert.py`** +
  **`core/solutions/latex_checker.py`** — the LaTeX conversion rules and their implementation /
  safety net (§7).
- **`core/solutions/answer_checker.py`** — standalone trigger for "does every question have a real,
  worked answer" (§8).
- **`Learning-Plan-Maths/chapters/<chapter>/question_layout/layout_spec.json`** (when it exists for
  the target chapter) — the pipeline's own validated, hand-approved ground-truth question grouping
  for that exact chapter. If it exists, cross-check any new grouping plan against it *before* writing
  a transformation script — it caught a wrong assumption (that "Figure it Out" items should always be
  split out from a teaching section's other prompts into their own sub-topic) on the very first
  reconnaissance pass for Class 6 Ch3.

---

## 2. Step 1 — survey the source file's actual shape; don't assume it matches the last chapter

The two chapters done so far had genuinely **different legacy shapes**, and a script written for one
will not directly work on the other:

| | Class 9 Ch6 (before this pass) | Class 6 Ch3 (before this pass) |
|---|---|---|
| Where book questions lived | Mostly in dedicated `"Questions:"/"Examples:"` topics, **plus 4 more embedded inside ordinary teaching topics** (their own `exercise_question` block mixed into a teaching concept's `content`) | Already one concept per book question, each already sitting under its own `"Questions: <Section>"` topic — nothing embedded in teaching topics to extract |
| One concept per question held | `question`/`steps`/`answer` as a single `exercise_question` block | `question`/`steps`/`answer`/`q_figure`/`s_figure` plus `image_media_id`/`video_media_id`/`solution_image_media_id(s)` **all on one combined content block** (`block_kind: "worked_example"`, `item_kind` already set to `figure_it_out`/`prompt`/`unsolved`/`exercise`) |
| Media ownership | Had a **pre-existing off-by-one bug** — a question's own media sometimes belonged, by id, to the *next* concept. Required deriving true ownership via `own_media()` (scan every topic's `media[]`, match by the media object's own `image_role`, never trust the concept's stored `image_media_id` pointer blindly). | Media ownership fields were already internally consistent (`image_role`/`concept_id` on the media object matched the owning concept correctly) — no derivation needed, read `image_media_id`/`video_media_id`/`solution_image_media_id(s)` directly. |
| `qt_part` field | **Never written** (see §8) | N/A — not split yet at the start |

**Before writing any code**, dump the field union for every question-like concept (recognizable by
`item_kind` being set, or `block_kind` in `exercise`/`exercise_question`/a `worked_example` carrying
`item_kind`): `ncert_refs`/`exercise_id`/`coverage_id`, `item_kind`, whether `question`/`steps`/
`answer` are already separate fields or one combined prose blob needing to be split by reading, and
whether `image_media_id`/`video_media_id`/`solution_image_media_id(s)` are trustworthy as stored or
need the `own_media()`-style derivation. Don't assume either answer from the last chapter.

---

## 3. Step 2 — classify every question into its target category/group

Adapt `core/question_naming.py`'s `classify()` to whatever signal the source actually carries. Class
6 Ch3 has no pre-formatted label string (no `"Exercise 5.1, Q3"`-style text to parse) — only
`item_kind` and `ncert_refs`, so the adaptation was:

```python
def classify(item_kind, ref, section_title):
    if item_kind == "figure_it_out":
        num = _section_no(ref)                 # "3.2.FiO1" -> "3.2", via ^(\d+\.\d+)
        suffix = "Figure it Out %s" % num if num else "Figure it Out"
        return "figure_it_out", suffix
    return "other", section_title              # the enclosing teaching section's own title
```

**Group order within a split topic** (when a teaching section's existing `"Questions:"` topic spans
more than one resulting category): the section's own prompts/exercises first, then its own numbered
Figure it Out box, then any unnumbered end-of-chapter Figure-it-Out items placed here — matching the
book's own layout (in-text prompts throughout the section, then its box; the unnumbered ones are
later review questions the original author placed here by *theme*, appended last). A topic whose
concepts span N categories becomes N new topics, each in its own new segment (confirmed: every
segment in this pipeline holds exactly one topic — a 1:1 relationship, not an incidental one).

**Don't assume a "scattered across multiple topics" pattern is a data-entry bug.** Class 6 Ch3's
printed Figure-it-Out box after section 3.7 has 5 questions (1 about digit differences, 1 about
palindromes, 1 about clock times, 1 about Kaprekar's constant, repeated for a 4-part sub-question)
that the *original author* had already placed under 3 *different* teaching topics — Pretty
Palindromic Patterns, Clock and Calendar Numbers, and The Magic Number of Kaprekar — by **theme**,
not by which printed box they came from. The same pattern recurred for the chapter's one
end-of-chapter review box (10 questions, each placed near its most thematically relevant earlier
section). Both were confirmed deliberate and correct by reading the actual source PDF/markdown text,
not assumed. **Check the book source before "fixing" a scattered pattern** — consolidating it would
have been the actual mistake.

---

## 4. Step 3 — split each question into a question concept + an answer concept

Exact field shape (`core/qt.py`'s real template, confirmed field-by-field):

```python
def _base_concept(role):
    return {
        "concept_id": "PLACEHOLDER", "concept_name": None, "content": [],
        "key_terms": [], "objective_id": None, "objective_ids": [],
        "source_segment_role": "practice", "source_media": None, "media_ids": [],
        "ncert_refs": [], "tier": None, "misconceptions": [], "predict_first": "",
        "enrichment_type": "enrichment", "is_enrichment": True,
        "mixed_objective_ids": [], "recap_objective_ids": [],
        "adaptive": {"tier": None, "discovery": False, "hint_ladder": False, "rescue": False,
                     "say": False, "check_my_thinking": False, "added_for_tier": []},
        "qt_part": role,   # "question" or "answer" - NOT "_qt_part", and NEVER stripped before writing
    }
```

- **Question concept**: `question` kept, `steps=[]`, `answer=""`, `text`/`publication_text` =
  `latex_wrap(question)`, `q_figure` carried over if present, `media_ids` = `[question image id]` if
  one exists (role `"question"` media only — never a video, never a solution image).
- **Answer concept**: `question` *kept too* (for context — `core/qt.py`'s own `_question_answer_blocks`
  does this), full `steps`/`answer`, `text`/`publication_text` built by concatenating
  `"%d. %s" % (i, step)` for every step plus an `"Answer: %s" % answer` line, **then running the whole
  block through `latex_wrap()` once** (not wrapping each step separately and prepending a bare `"N."`
  outside it — that leaves the index itself unwrapped, violating the step-numbering rule). `s_figure`
  carried over if present. `media_ids` = `[video id if any] + [solution image id(s)]`, in that order —
  matching `gates/solution_content.py`'s own check exactly: media_ids must end with a solution image
  (`image_role: "solution"`), with any video appearing before it, never after.

**This split must be done by reading and judging, not blind field-copying.** Confirm the question
side really is just the problem as asked (no part of the method or the result folded in) and the
answer side really is the complete working. **When the source has `steps`/`answer` both empty** — an
open "make your own puzzle/card", "do you agree", or reader-estimate item, or a genuinely unsolved
exploration — **author an accurate solution from the question and the chapter's own content before
splitting it. Never hand the answer concept an empty block.** This exact policy is now written into
`core/qt.py`'s `_question_answer_blocks` docstring and cross-referenced from
`math_solutions/skill/references/format-rules.md` rule 9 — read both before doing this on a new
chapter, and see §8 for the dedicated tool that finds every gap automatically.

Class 6 Ch3 had 12 such gaps (open "make your own supercell puzzle", "write other numbers whose
digits add to 14", reader-estimate items like "Gandhinagar to Kohima: about how many km?" and
"how long would it take you to walk across India?") — every one was worked out from first
principles (e.g. the supercells-max-per-row question was answered by proving no two adjacent cells
can both be supercells, so the maximum is `ceil(n/2)`, matching the book's own already-answered
`n=9 → 5` example) and written in the same step-by-step, named-reasoning style as the chapter's own
already-answered neighbours — never a placeholder, never an unverified guess.

---

## 5. Step 4 — global renumbering

Two-pass remap, run in this exact order — **the second pass is not optional**:

1. **Generic pass**: build an old→new id map (every changed `topic_id`, `concept_id`, and media
   object `id`), then substring-substitute it across the *entire* plan (`objectives`, `source_metadata`,
   every topic's `depends_on`/`topic_objective`, every concept's `media_ids` and block-level
   `image_media_id`/`video_media_id`/`solution_image_media_id(s)`). Sort replacement keys longest-first
   and guard with a `(?!\d)` negative lookahead so a shorter key (`...C1`) can't false-positive-match
   as a prefix inside an unrelated longer id (`...C11`).
2. **Explicit per-unit retarget pass, run LAST**: for every media object a freshly built Q/Ans pair
   owns, force its `id`/`concept_id`/`home_concept_id` directly from that pair's own new concept id —
   overriding whatever the generic pass computed. **Why this is required, not belt-and-suspenders**: a
   brand-new topic or concept can land on an id string that happens to collide with an id some
   *different*, unrelated object used to have before renumbering — the generic substring pass has no
   way to know that, and can silently write a wrong-but-plausible-looking id into a freshly built
   object. Keying the final fixup by "this media object's own new owner", not by whatever string
   substitution produced, is the only way to guarantee correctness.

Numbering rules (confirmed against the pristine, pre-transformation file both times):
- `topic_id`: `M<module>.S<n>.T<n>`, sequential, `S` and `T` always equal, counted **once across the
  whole document** — the counter is never reset per module.
- `concept_id`: `<topic_id>.C<n>`, again **one global counter across the whole document**, never
  reset per topic.
- Rebuild `depends_on` as a strict linear chain in final document order.
- Rebuild `segments` 1:1 with topics (confirmed in both chapters: every segment holds exactly one
  topic — treat this as a hard invariant, not a coincidence, when deciding whether splitting a topic
  needs a new segment too — it does, always).

---

## 6. Step 5 — `ncert_coverage` and objectives cleanup

- `source_metadata.ncert_coverage[ref]` must point at **both** the new question and answer concept
  ids. **A ref can already map to more than one concept before you touch anything** — Class 6 Ch3's
  `"3.8.FiO1_cards"` ref was already shared across 4 different question concepts in the pristine
  source. Accumulate every unit sharing a ref, in unit order (`ref -> [q1, a1, q2, a2, ...]`); never
  just overwrite one unit's pair with another's, or the gate-level `ncert_coverage` check will
  silently lose earlier units.
- Objectives: drop any objective whose `anchor` list includes a concept that no longer exists after
  the split. Every Q/Ans concept this transform builds has `objective_id: None` by design (matching
  `core/qt.py`'s own convention — book-question practice concepts are never objective-anchored), so
  an objective anchored *only* to a now-replaced concept is always stale and always dropped. Then
  renumber the kept objectives sequentially (`O1..On`, no gaps — a validator rejecting a hole is the
  usual symptom of skipping this) and fix every cross-reference: `strand_to_objective_map`, each
  concept's `mixed_objective_ids`/`recap_objective_ids`, and every topic's
  `objective_ids`/`learning_objectives`/`segment_objective_ids`.

---

## 7. Step 6 — LaTeX conversion, and the bugs a new chapter will keep finding

`latex_convert.py`'s `latex_wrap()` builds the inline-`$...$` display text from plain `question`/
`steps`/`answer` strings, per `LATEX_REFERENCE.md`'s rules; `latex_checker.py` is the fast, standalone
safety net that scans *already-converted* text for a fixed list of known mistake shapes. Neither is
"done" just because it passed on the last chapter — **every new chapter's own phrasing conventions
have exposed new tokenizer bugs so far, with no exception**:

| Trigger pattern | Wrong output before the fix | Root cause | Fix |
|---|---|---|---|
| `"5-digit numbers"` (digit-hyphen-letter) | `$5-$digit` (hyphen swallowed as a false minus sign) | Only letter-hyphen-letter was recognised as an English compound word | Treat a hyphen as prose whenever the character after it is a letter, regardless of whether the character before it is a letter *or a digit* |
| `"(and than 5347), so choose..."` | `(and than $5347)$` (stray close-paren inside the dollars) | A `)` matching a prose-opened `(` wasn't itself forced back to prose | Track, per `(`, whether it opened a prose aside; its matching `)` inherits that |
| `"Sum: 10001 + 99999 = 1,10,000"` (Indian lakh grouping) | split into `$1$,$10,000$` (two separate math spans) | The digit regex only accepted Western 3-digit comma groups | Accept any `,\d+` run after the first digit group (a comma glued with no space is always one formatted number, either convention) |
| `"To say 2 a child needs..."` (spaced digit, then "a") | `$2 a$` (the article swept into the number's math span) | A digit immediately before "a" was trusted as a coefficient signal even with a space between them | Require the digit be *glued*, `2a`, with no space, before trusting it |
| `"...cover 30 to 40 km a day"` (unit, then "a") | `$40\text{ km} a$` (same mechanism, via the closing `}` of a unit's `\text{}`) | A `}` immediately before "a" was trusted the same way, spaced or not | Require `}` be glued too — a unit's closing brace followed by a *spaced* "a" is always the word "a", never a variable |
| `"Go first and add 2..."` / `"...costing around Rs 60"` | `$Go$` / `$Rs$ 60` wrapped as math | Any word ≤2 letters not already on the stopword list defaults to "math variable" | Add `"go"`/`"rs"` to `_STOPWORDS` |
| `"the 2nd, 4th and 9th cells"` | `$2nd$` (the letter suffix renders in math italics, not upright) | No dedicated ordinal-suffix handling | Match `\d+(st\|nd\|rd\|th)\b` glued and wrap the suffix as `\text{..}`: `$2\text{nd}$` |
| A rhetorical `" - "` used as a dash between two prose clauses | `$- a$` or similar — indistinguishable from subtraction by local context | Fundamental ambiguity, not a tokenizer gap | Don't ask the tokenizer to guess — rewrite with a comma/colon/semicolon/"so"/"since" instead, matching the corpus's own existing convention (it never uses a bare spaced dash this way) |
| A parenthetical aside opening with a bare digit, `"(5 of the 9 cells...)"` | `$8100 (5$` (the `(` merges into the preceding number's math run) | Only a *word* right after `(` triggers the prose-aside detection; a digit doesn't | Known, accepted limit (also seen as `"$(1980$ also takes..."` on book-sourced text) — rephrase to start the aside with a word, or drop the parens, rather than reopening this question generally (a blanket fix risks breaking genuine numeric groupings like `(-5)`) |
| `"150 words per page x 100 pages"` (multiplication written as a bare letter) | `$x 100$` (the letter "x" read as a one-letter variable, swallowing the next number) | Not a tokenizer bug — a style mismatch | Always write `×` (or `\times`), matching the corpus's own established convention; never a bare "x" |

**The mandatory verification loop, every single time** (self-authored text included — see below):

1. Self-test: `python -B latex_convert.py` must still match `LATEX_REFERENCE.md`'s own worked
   examples exactly.
2. Regression: `python -B latex_checker.py <every already-converted chapter's plan.json>` must still
   report 0 issues — a new heuristic tuned only against the chapter that motivated it can silently
   break a *different*, earlier chapter's text.
3. Full manual read: dump and read **every** question/answer in the chapter actually being worked
   on, not a sample. Write the dump to a file with explicit UTF-8 encoding
   (`io.open(path, encoding="utf-8")`) — **not** `print()` to a Windows console, which crashes
   (`cp1252`) on real NCERT content (₹, Δ, π, ...) and can interleave confusingly with buffered
   output when it does.
4. Only once all three pass, apply the fix to the actual data file.

**Hand-authored text is itself a stress test, not a safer shortcut.** Writing the 12 missing Class 6
Ch3 solutions by hand (§4) surfaced four of the bugs in the table above — none of which any
book-sourced content in either chapter had exercised. Run the identical three-step loop on freshly
written prose. And **write new prose in the corpus's own already-established conventions** (`×` not
`x`, `₹` not `Rs`, no rhetorical dashes, no digit-opening parenthetical asides) rather than relying on
the converter to handle a shape the existing content never needed — it's faster and safer to match
house style than to extend the tokenizer for every new way of phrasing the same idea.

---

## 8. Step 7 — verify every question actually has a worked answer

`gates/solution_content.py` already blocks the build on "no solution steps" / "no answer" for any
question concept — this is not new. What's new is a fast, standalone way to find every gap *and*
apply hand-authored fixes in one step: **`core/solutions/answer_checker.py`**.

```
python -B answer_checker.py <plan.json>                      # list every gap
python -B answer_checker.py <plan.json> --write <fills.json> # apply hand-authored fixes, re-wrap LaTeX, save
```

`fills.json`: `{"<concept_id>": {"steps": ["...", ...], "answer": "..."}, ...}` — plain text, same
shape as every other concept's `steps`/`answer`. The tool refuses to write if any gap is left
unfilled, or if `fills.json` names a concept that isn't actually a gap.

**The one real gotcha this tool already caught**: it (and `gates/solution_content.py` itself) decide
"is this concept a question-only half that's *supposed* to have empty steps/answer" by checking
`concept.get("qt_part") == "question"`. Running it against Class 9 Ch6 first reported **all 63**
question concepts as gaps — not because any answer was actually missing, but because that chapter's
concepts, built by an earlier one-off script before `qt_part` was known to be the real convention
(§1), **never had the field at all**. Every "question"-half concept (correctly, by design, holding no
steps/answer) was indistinguishable from a genuine gap once `qt_part` doesn't exist anywhere in the
file. **A 0-gap report is only trustworthy once you've confirmed `qt_part` actually appears on at
least some concepts** — otherwise the check's own skip condition may simply never be firing, and
"all clean" is a false negative, not a real result. (This exact false negative previously produced an
incorrect "Class 9 Ch6 already has zero empty-answer concepts" claim from an earlier, less careful
check in this same project — corrected once this tool was built and actually run.)

Fix for a file missing `qt_part` entirely: it can be patched in reliably from the already-applied
`concept_name` suffix convention (§1's table) — `": Q"`/`": Qn"` → `"question"`, `": Ans"`/`": Ansn"`
→ `"answer"` — for exactly the concepts that match one of those two suffixes; leave every other
(teaching) concept untouched. Verify the counts split evenly (question count == answer count == half
the matched concepts) before writing.

---

## 9. Full procedure for a brand-new chapter

1. Survey the source shape (§2) — don't assume it matches either prior chapter.
2. Classify every question into its target category/group (§3); cross-check against
   `question_layout/layout_spec.json` if one exists for this chapter.
3. Build the question/answer concept pairs (§4) in the real `core/qt.py` field shape — reading each
   one, not copying fields blind; author any genuinely missing solution now, from the question and
   the chapter's own content.
4. Splice the new/split topics into their segments, preserving every other segment's position.
5. Globally renumber (§5): generic substring pass, then the explicit per-unit media retarget pass,
   last.
6. Fix `ncert_coverage` (accumulating per ref) and clean up objectives (§6): drop stale, renumber
   gapless, fix every cross-reference.
7. Apply `latex_wrap()` to every question/steps/answer; run the full three-step verification loop
   (§7) before and after any converter change this chapter's phrasing newly requires.
8. Run `answer_checker.py` (§8) and confirm the 0-gap report is trustworthy (some concepts actually
   carry `qt_part`).
9. Run a structural validation pass: no duplicate topic/concept/media ids, every concept under its
   own topic's id prefix, every `media_ids`/`image_media_id`/`video_media_id`/
   `solution_image_media_id(s)` resolves to a real media object, `ncert_coverage`/objective anchors
   all resolve, concept/topic ids are one gapless global sequence, objective ids are gapless.
10. Write the file only once every one of 7–9 is clean; re-verify independently by reloading the
    written file from disk (don't trust the in-memory state the write script printed).

---

## Appendix C — what was actually done on the two chapters

| | Class 6 Ch3 | Class 9 Ch6 |
|---|---|---|
| Legacy shape | One concept per question already, combined block (§2) | Embedded + dedicated topics, pre-existing media off-by-one bug (§2) |
| Question categories found | `other` (section title) + `figure_it_out` (numbered and bare) | `exercise` (numbered Exercise Set) + `example` |
| "Questions:" topics before → after | 14 → 27 | unchanged structurally by this pass (already split) |
| Question concepts before → after | 72 → 144 (Q/Ans pairs) | 63 pairs already existed (126 concepts) |
| Topics total before → after | 30 → 43 | 19 (unchanged) |
| Objectives before → after | 103 → 58 (45 dropped, stale) | 29 (unchanged — none newly stale) |
| New tokenizer bugs found (§7) | digit-hyphen compounds, prose-paren-close, Indian lakh grouping, spaced-digit/`}`-before-"a", "go"/"rs" stopwords, ordinal `\text{}` | regression-tested against, none new from this chapter's own content |
| Missing-answer gaps found (§8) | 12 (authored by hand, §4) | 0 real gaps, but 63 **false** gaps from a missing `qt_part` field (fixed, §8) |
| `latex_checker.py` final result | 0 issues | 0 issues |
