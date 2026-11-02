# Tool spec guide

## "Spec + placeholder" vs. the Tools/_core HTML system

This pipeline builds 2d_tool media nodes **spec + placeholder** style, the way
`maths7_ch10/new_design` and `maths8_ch9/new_design` build theirs: `tool_config` on the node
carries the *complete teaching spec* for the tool (its idea, what is on screen, every control,
every challenge, the feedback rules, the hint ladder) but the tool's actual `.tsx`/HTML is **not**
built yet. `2d_tool_url` points at a reserved, not-yet-live path, and the node's `build_status` is
`"placeholder"`. A separate build pass (not part of this pipeline) later reads `tool_config` and
implements the real interactive tool at that url.

This is deliberately **not** the `maths6_ch3/new_design/Tools/_core` system, where every tool
ships as real, working standalone HTML/tsx *before* the plan is built, and the plan's media node
just points at that already-live file. Do not bring `Tools/_core`'s machinery (its shared runtime,
its per-tool React/tsx scaffolding) into a chapter built from this template - if a chapter truly
needs tools-as-live-HTML, that is a different pipeline shape, not this one.

## The tool_config / tool_questions shape

A tool spec is built with `concept_plan.py.template`'s `T()` helper and stored in its `TOOLS` dict,
keyed by the name a `DOER()` concept's `tool` field names. `tool_node_builder.build_tool_node()`
turns one of these specs into the actual plan node.

```python
# in concept_plan.py (chapter-specific)
TOOLS = {
    "integer_number_line": T(
        "tool_integer_number_line",                  # tool_id (used in the asset path)
        "Integer Number Line",                        # title (student-facing)
        "manipulative",                                # subtype
        "Dragging a counter onto a signed position on the number line.",   # idea
        "A number line from -10 to 10 and one draggable counter with a live read-out of its "
        "position.",                                   # screen
        ["Predict which side of 0 the target is on.", "Drag the counter there.",
         "Read the number the counter landed on."],     # student_does
        ["Place the counter at 3.", "Place the counter at -4.", "Place the counter at 0.",
         "Place the counter at -10.", "Place the counter at 10."],   # challenges (5 to 7)
        ["A wrong placement snaps back with a gentle shake, no number shown.",
         "A correct placement turns the counter green and shows the signed value."],  # feedback
        "all 5 challenges are placed correctly.",       # done_when
        ["counterPosition", "challengeIndex"],           # shared_state
        ["M_SIGN_CONFUSION_1"],                          # misconceptions (ids from content.py)
        ["Which number does the challenge name?",         # hints: orienting
         "Count from 0 in the sign the number has.",       # strategic
         "Move the counter one step at a time toward the target.",  # specific
         "The counter belongs on -4; place it there."]),   # bottom-out
}
```

`T()` asserts 5-7 challenges and exactly 4 hints (orienting, strategic, specific, bottom-out) -
these are the hint-ladder and challenge-count conventions already used by every reference chapter
this template was built from.

`tool_questions` passed to `build_tool_node()` is usually just `spec["challenges"]` (the list of
things the student is asked to do) - `gates/media_content.py`'s `preflight()` requires every
`2d_tool` node to carry `tool_questions` either on itself or on the node named by its
`tool_config["same_as"]`, so two concepts can share one tool's question set without duplicating it.

## Using it from a chapter's concept_plan.py / build.py

1. In `concept_plan.py`, add one `TOOLS["<key>"] = T(...)` entry per tool, and set a `DOER()`
   concept's `tool="<key>"` to attach it.
2. `build.py` (already wired, do not change it per chapter) looks up `CP.TOOLS[concept["tool"]]`
   for every `kind="doer"` concept and calls `tool_node_builder.build_tool_node(...)`, passing:
   - `tool_2d_url` built from the chapter's own `ASSET_BASE` (never hand-typed - see the rule below)
   - `grade` from `chapter.config.json`, so a wrong `ASSET_BASE` substitution is caught immediately
     instead of at `validate_local.py` time.
3. The resulting node is appended to that concept's topic's `media` list and the concept's
   `available_content_types` gains `"2d_tool"`.

Never attach more than one tool to a topic (tool-pruning policy, project memory
`lp-tool-pruning-policy`): keep a tool only where the manipulation genuinely **is** the concept.

## The asset-upload-side rule (repeated from `upload/SKILL.md`)

- The subject folder in every asset path is **always `mathematics`**, never `maths`
  (`chapter.config.json.sample`'s `asset_base_template` already has this baked in - do not
  "correct" it back to `maths` for a chapter that happens to live under a `maths learning plan/`
  folder on disk; the GCS path and the local folder name are unrelated).
- The `2d_tool_url` a chapter uploads is **always read off the plan's own `2d_tool_url`** field,
  never reconstructed from `grade + subject + chapter_no` at upload time - reconstructing it is how
  a stale or mistyped path silently uploads content that answers `success: true` to the wrong
  place. `tool_node_builder.build_tool_node()` takes `tool_2d_url` as an explicit argument for
  exactly this reason: the caller must pass the one true URL, not have this module guess it.
