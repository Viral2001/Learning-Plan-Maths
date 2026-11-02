# maths_new_design_pipeline

Builds, validates and uploads a CBSE Class 6-10 maths "new design" chapter: a
per-chapter `build.py` that writes one Phase 2 learning-plan JSON, checked by a
shared gate library before anything reaches the database.

This is a standalone pipeline. It does not import from, write to, or assume
the layout of `lp_pipeline` (the older checkout this one was distilled from).
Reference material taken from there is condensed into `docs/`; nothing here
depends on that repo existing on disk.

## Who this is for

Whoever is authoring or rebuilding one chapter at a time: writing its
concepts and tool specs, running its gates, writing its video scripts, and
pushing the result to staging.

## The one hard rule

**No upload without a passing `validation/validate_local.py` run.**
`upload/upload_lp.py` refuses to POST a plan unless a fresh `<plan>.stamp.json`
sits next to it, written by `validate_local.py` on a zero-error gate run, with
a sha256 that matches the plan's current bytes. `--skip-preflight` relaxes the
separate structural preflight only - it does **not** bypass the stamp check.
There is no way to upload an unvalidated plan short of editing the uploader
itself.

## This pipeline is Phase-2-only

Every plan built and uploaded here is written directly in Phase 2 shape:
`phase: 2`, the chapter's own plain `chapter_id`. There is no `_V3` chapter,
no `to_phase2.py` mirror step, and no later patch that promotes or demotes a
plan between phases. The convention the original repo's authors call
`_V3`/"Phase 3" (build a parallel chapter, then copy it into Phase 2
unchanged) is deliberately not used here - `build.py` writes the final,
uploadable plan the first time.

## Folder layout

| Folder | Holds |
|---|---|
| `core/` | Shared machinery: `config.py` (credentials/DB), `qt.py` (question-topic insertion), `set_version.py` (version/plan_id), `published_media.py` (asset pinning), `check_master_id.py` (live id check), `video_script/` (the video script contract, checker and render helpers; Keeko format, `{{NAME_n}}` tokens filled by `fill_names.py`), `solutions/` (question solutions in `solutions.json` and their LaTeX + Manim images) |
| `gates/` | The shared gate library: `gate_runner.py` plus one module per gate family (`media_content.py`, `eqcheck_plain.py`/`eqcheck_signed.py`/`eqcheck_powers.py`, and the skeleton/objectives/coverage/video_script_rules/theorem_variant families as they land) |
| `chapter_template/` | The scaffold a new chapter is cloned from: a `build.py` shape, `media_specs/`, `video_scripts/` |
| `tools_spec/` | The shared shape for an un-built tool left as a spec rather than a built `.tsx` |
| `validation/` | `validate_local.py`, the local gate runner that writes the upload stamp; `STAMP_FORMAT.md` |
| `upload/` | `upload_lp.py`, `upload_tool.py`, `verify_uploaded.py`, `SKILL.md`, `chapter_master_ids.md` |
| `docs/` | This onboarding set: `00_overview.md`, `01_runbook.md`, `02_video_script_schema.md`, `03_known_master_ids.md`, `04_class9_10_variant.md` |

## Quickstart

**One command:** in Claude Code, from this folder, `/lp <chapter>, <path to the book pdf>, <teacher instruction (optional)>`
(for example `/lp class 7 ch 3, C:ooks\gemh103.pdf, use cricket examples`). The skill is
`.claude/skills/lp/SKILL.md`; its first step is `core/lp_start.py`, which scaffolds the chapter folder and cuts the chapter
out of the book. It stops at a validated local plan and never uploads.

By hand:

Read `docs/01_runbook.md` for the exact build order, start to finish. Read
`docs/00_overview.md` first if you want the shape of the system before the
steps.
