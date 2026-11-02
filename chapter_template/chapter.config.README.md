# chapter.config.json - field reference

JSON has no comments, so this file carries the explanation `chapter.config.json.sample` cannot.
Copy the sample to `chapter.config.json` next to your chapter's `build.py` and fill in every field
before the first `python build.py` run. Every field below is read by code that already exists in
this pipeline (cited by file:line) or is a value this template's own `build.py` needs to assemble
the plan; nothing here is decorative.

Do **not** add a `//` comment convention to the real file: `gate_runner.main()` and
`validate_local.py` both load it with plain `json.load`, which raises on a `//` line, so a commented
copy would fail at the first `python build.py` run. This README is the only place comments live.

## Fields actually read by existing pipeline code

| field | type | consumed at | what it does |
|---|---|---|---|
| `chapter_master_id` | int | `validation/validate_local.py:61` (must agree with the plan's own `chapter_master_id`, else validation refuses before it even runs the gates); `core/check_master_id.py` (checked live against `chapterMaster`) | the database key that attaches the plan to the right chapter row. Getting it wrong uploads clean content to the wrong chapter and still answers `success: true` - see `upload/SKILL.md`. |
| `phase` | int, must be `2` | `validation/validate_local.py:64` (must agree with the plan's own `phase`) | this pipeline is Phase-2-only, direct build; no `_V3`, no `to_phase2.py` mirror. `upload/upload_lp.py` refuses any phase other than 2 regardless of what is passed on the command line. |
| `eqcheck` | `"plain"` \| `"signed"` \| `"powers"` | `gates/gate_runner.py:114` (`config.get("eqcheck", "plain")`), which picks the equation-truth checker module (`gates/eqcheck_plain.py` / `eqcheck_signed.py` / `eqcheck_powers.py`) that scans every authored text in the plan | `"plain"` for chapters with no negative numbers or exponents, `"signed"` once integers appear (Class 6 onward touches negatives), `"powers"` once the chapter has exponent laws. |
| `eqcheck_errata` | list of exact chain strings | `gates/gate_runner.py:115,76-102` | exact, deliberately-kept printed-book arithmetic errors to exempt from the equation-truth gate (e.g. a textbook typo the plan quotes verbatim in `textbook_text`). **Never a way to silence a real failure**: `gate_runner.run_eqcheck` fails the build if any entry here is never matched against the plan's own text, so a stale exemption cannot linger unnoticed. Leave empty unless you have a specific, verified printed-book error to carry forward. |

## Fields this template's own `build.py` and `tools_spec` consume

`gates/skeleton.py`, `gates/objectives.py`, `gates/coverage.py`, `gates/video_script_rules.py` and
`gates/theorem_variant.py` are all wired into `gate_runner.run()` now - see that file's module
docstring for exactly which gate family runs for which `grade_band`/`theorem_chapter` value
(`skeleton`/`objectives` for Class 6-8, `theorem_variant` for Class 9/10; `coverage` and
`video_script_rules` always run). `build.py` reads the same keys below so a chapter author has one
config file, not two.

`gate_runner.run()` returns `(errors, counts)`; `counts["warnings"]` holds findings from known,
documented heuristic limitations (own-content word-overlap in `objectives.py`, the "mapped to more
than one concept" informational flag in `coverage.py`, theorem_variant rule 1's "cannot be verified"
note) that `validate_local.py` prints but does not block the stamp on. Everything else in `errors` is
blocking.

| field | type | used for |
|---|---|---|
| `chapter_id` | string, **no `_V3` suffix** | written straight onto `plan["chapter_id"]`; also the `<chapter_id>.json` output filename `build.py` writes. |
| `subject_ref_id` | int | written onto `plan["subject_ref_id"]`; checked live by `core/check_master_id.py` (`CHECKED` tuple) against `chapterMaster."SubjectId"`. |
| `medium_id` | int | written onto `plan["medium_id"]` (every live phase2 plan carries this top-level field; English medium is `1` in every reference chapter read while building this template). |
| `grade` | int | written onto `plan["grade"]`; also used by `gates/media_content.py:101-107`'s asset-url check, which requires every `2d_tool_url`/`image_url`/`video_url` to contain `class_<grade>/` - `build.py` substitutes it into `asset_base_template`. |
| `grade_band` | `"6_8"` \| `"9_10"` | which content rules apply from `docs/` (Class 9 and 10 ban `Fig.`/labelled-figure references and enrichment objectives differently than Class 6 to 8 - see `lp-grade9-ch5-new-design` in project memory); also the default `photo_rule_band` your chapter should pick if you leave that field at its placeholder. |
| `chapter_no` | int | substituted into `asset_base_template`'s `ch_{chapter_no}` segment. |
| `chapter_name` | string | written onto `plan["chapter_name"]`. |
| `media_tag` | short string, e.g. `"c9x"` | the prefix on every media worklist key (`<media_tag>.<topic_key>.D<n>`) and media spec filename, matching the convention in every reference chapter's own `media_specs.py`/`concept_plan.py`. |
| `theorem_chapter` | bool | `gates/gate_runner.py`'s `is_theorem_chapter` check (`grade_band == "9_10" or theorem_chapter`), which decides whether `gates/theorem_variant.py` runs in place of `skeleton.py`/`objectives.py`; also whether `build.py` expects `concept_plan.py`'s concepts to carry a `theorem` block, and whether `book_rules.json`'s `"theorems"` key is required (see `core/video_script/contract.py:124`, `THEOREM_STATE_BEAT`, and `core/video_script/check.py:144-188`, which reads `book_rules.json["theorems"][<script key>]` as the exact phrases a theorem video's `state` beat must say). |
| `idea_topic_concept_range` | `[min, max]`, default `[2, 4]` | `gates/skeleton.py`'s `idea_topic_concept_range` (Class 6-8 only; not read for a `theorem_chapter`) - a topic outside this range of *primary* concepts (thin-extra concepts excluded) is a blocking gate failure, not a warning. Named to match the key `skeleton.py` actually reads - do not call this `concept_count_range`, an earlier draft of this template did and `skeleton.py` silently ignored it. |
| `intro_requires_free_try_tool` | bool, default `true` | `gates/skeleton.py`'s `intro_requires_free_try_tool` - whether the intro topic must carry a second `try_it` concept with its own tool, beyond the hook. The target shape for every new chapter; set `false` only when cloning an older chapter's intro verbatim (`maths6_ch3`/`maths7_ch10` both predate this pattern and ship a hook-only intro). |
| `allow_words` | list of strings, default `[]` | `gates/video_script_rules.py`'s synthetic worklist header - words to exempt from `core/video_script/check.py`'s banned-word scan for this chapter only. Use it for ordinary vocabulary the banned-word list collides with in this chapter's domain (e.g. `"points"` on a circle/geometry chapter, `"difference"`/`"product"` where the banned list's generic-verb entries overlap legitimate maths nouns) - never to hide a genuine scripting-rule violation. |
| `interactive_video_variant` | bool | whether every `exercise`-kind video slot is built with `unlock: "after_attempt"` (the question video unlocks only after the student has attempted the question; each video has exactly one think-and-tell with a 3-second pause, nothing else pauses) versus a plain walkthrough. Passed through to `core/video_script/plan_hook.slot()`'s `unlock`/unlock-override behaviour; also read by `gates/video_script_rules.check_interactive_variant()`. |
| `photo_rule_band` | `"default"` \| `"need_basis"` \| `"none"` | which grades a scene photo (as opposed to a thing/place/document photo) is allowed on, mirroring `core/video_script/contract.py:103-106` (`PHOTO_SCENE_GRADES`: `default` = Class 3-6, `need_basis` = Class 7-8); `"none"` for Class 9-10, where scene photos are not used at all. Real people/characters/named historical figures still follow the three-tests rule in project memory (`lp-photo-rule`) regardless of this field. |
| `asset_base_template` | string with `{grade}`/`{chapter_no}` placeholders | `build.py` calls `.format(grade=..., chapter_no=...)` on this to build `ASSET_BASE`, the prefix every `2d_tool_url`/`video_url`/`image_url`/`planned_url` is built from. **Subject folder is always `mathematics`, never `maths`** - `upload/SKILL.md`'s rule, already baked into the sample's default value. |
| `solutions` | **required**: `true` \| `false` (a missing key stops `build.py`; `"text"` is refused) | `gates/solution_content.py` (registered in `gates/gate_runner.py` when truthy); `chapter_template/build.py` (`core/solutions/{bind,check,attach}.py`) | the default for every new chapter is `true`: each question carries, in its concept, the question + numbered step-by-step solution + `Answer:` (from `solutions.json`, schema `core/solutions/schema.py`) AND a question image and a solution image (`media_ids = [question image, video, solution image]`, the block names both in `image_media_id` / `solution_image_media_id`; Manim scenes in `solution_images/` via `core/solutions/gen_scenes.py`, `render.py`, approved in `core/image_editor`). A question with no `solutions.json` entry, placeholder working, a missing solution image, or two questions in one concept fails the build. `false` only when the user explicitly wants a chapter without solutions. Chapters that predate `solutions.json` keep their own `build.py` and config and are unaffected. |

## Not included here on purpose

`version` and `plan_id` are deliberately absent: `core/set_version.py` sets them by asking the live
server for the chapter's current max version, and must run *after* `build.py` and *before*
`validation/validate_local.py` (see `validation/STAMP_FORMAT.md`'s required order). Putting a version
number in this config would invite someone to skip that live check.
