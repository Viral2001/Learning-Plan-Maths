# -*- coding: utf-8 -*-
"""Run every gate family that applies to a built plan, chosen off its chapter.config.json.

Generalized from the three reference build.py's check() functions (maths6_ch3, maths7_ch10,
maths8_ch9). Every gate family in the approved plan is wired in:

    errors, counts = run(plan, config)

`plan` is the built plan dict (already in Phase 2 shape - no _V3, phase: 2).
`config` is the chapter.config.json dict (needs at least "eqcheck": "plain"|"signed"|"powers").

question_layout runs only when config has a truthy `question_layout` (the "Questions: <topic>" layout: every
book question in its own concept right after its concept topic; see gates/question_layout.py).
coverage/video_script_rules always run (plan-shape and video-contract checks that hold
regardless of grade band). solution_content runs only when config has `solutions` (true/"images"/"text":
every question block has its steps and answer, and by default the media_ids order question image, video,
solution image). skeleton/objectives are Class 6-8 "idea topic + QT" specific - their
source_type classification (framing/instructional-exploration/question_topic-or-exercise/summary)
and "last concept is the doer with one tool" rule were verified by hand against a live Class 9/10
theorem chapter (maths9_ch5) and produce dozens of structural false positives there (missing
topic_objective on theorem/EOC topics whose source_type this classifier doesn't recognise, "no
doer concept" on topics that were never meant to have one) - so they run only when
`grade_band` is NOT "9_10". theorem_variant is their Class 9/10 replacement (it already covers
the equivalent ground: enrichment-no-objective, theorem-objective-names-statement, EOC-topic
placement) and runs only when config says this is a theorem chapter (`grade_band == "9_10"` or
`theorem_chapter` truthy).

## Blocking errors vs advisory warnings

`run()` returns `(errors, counts)`. `errors` is what `validation/validate_local.py` gates the
stamp on - a plan with any entry here must not be stamped or uploaded. `counts["warnings"]` is a
second, non-blocking list, but each pattern only earned that status by actually firing on a real,
already-live, accepted reference plan during parity testing (6ch3/7ch10/8ch9/9ch5/9ch6) - a
heuristic's own docstring calling it "shallow" was not, by itself, enough to exempt it. One
candidate marker ("topic objective covers", from `objectives.py`'s topic-level word-overlap
check) never fired on any reference chapter and was left blocking for that reason: no evidence
it is a necessary exemption, so it stays a real gate until a genuine false positive is found.
`validate_local.py` prints warnings but a nonempty `counts["warnings"]` never blocks the stamp.
The patterns that did earn advisory status, each named in its own gate module's docstring as a
deliberately shallow/partial check:
  - `objectives.py`: "shares no key term with its own concept" (own-content word-overlap
    heuristic - fired on 8ch9, a clean reference chapter).
  - `coverage.py`: "mapped to more than one concept" (that module's own docstring calls this an
    informational count for a human to judge, not necessarily a defect - fired on 6ch3/9ch5/9ch6,
    all on deliberately double-touched book items, e.g. a theorem and its converse sharing one
    tool, or a theorem's statement and proof concepts both citing the same Th<n> id).
  - `theorem_variant.py`: "cannot be verified for it" (rule 1's explicit "confirm this is an
    intentional pedagogy choice" finding, for a theorem with no standalone statement moment -
    fired on 9ch5/9ch6).
Every other message from every gate family is blocking, including the two gates' *other* checks
(a missing objective, a bad word count, a banned verb, a real skeleton/theorem-rule violation)
which stay exactly as strict as before - only these three specific, named heuristics moved.

    python -B gate_runner.py <plan.json> <chapter.config.json>
"""
from __future__ import annotations

import io
import json
import sys

from . import (coverage, media_content, objectives, question_layout, skeleton, solution_content, theorem_variant,
               video_script_rules)

EQCHECK_MODULES = {}

# See the module docstring's "Blocking errors vs advisory warnings" section: a gate message
# containing any of these substrings is downgraded to counts["warnings"] instead of blocking the
# stamp. Each one is named, by the exact substring, in the gate module that produces it.
ADVISORY_MARKERS = (
    "shares no key term with its own concept",
    "mapped to more than one concept",
    "cannot be verified for it",
)


def _is_advisory(message):
    return any(marker in message for marker in ADVISORY_MARKERS)


def _eqcheck_module(name):
    if name not in EQCHECK_MODULES:
        if name == "plain":
            from . import eqcheck_plain as mod
        elif name == "signed":
            from . import eqcheck_signed as mod
        elif name == "powers":
            from . import eqcheck_powers as mod
        else:
            raise ValueError("unknown eqcheck variant %r (expected plain/signed/powers)" % name)
        EQCHECK_MODULES[name] = mod
    return EQCHECK_MODULES[name]


def walk_topics(plan):
    for module in plan.get("modules") or []:
        for segment in module.get("segments") or []:
            for topic in segment.get("topics") or []:
                yield topic


def _topic_tools(topic):
    return [x for x in topic.get("media") or [] if x.get("type") == "2d_tool"] \
        + [c["tool_spec"] for c in topic.get("concepts") or [] if c.get("tool_spec")]


def _authored_texts(plan):
    """Every string the gate should scan for false arithmetic: content blocks, objectives, tool specs."""
    texts = []
    for topic in walk_topics(plan):
        for concept in topic.get("concepts") or []:
            for block in concept.get("content") or []:
                for field in ("text", "question", "answer"):
                    v = block.get(field)
                    if isinstance(v, str):
                        texts.append(v)
                for step in block.get("steps") or []:
                    if isinstance(step, str):
                        texts.append(step)
        if topic.get("topic_objective"):
            texts.append(topic["topic_objective"].get("objective_text", ""))
        for tool in _topic_tools(topic):
            if tool.get("tool_config"):
                texts.append(json.dumps(tool["tool_config"], ensure_ascii=False))
    for obj in plan.get("objectives") or []:
        texts.append(obj.get("objective_text", ""))
    return texts


def run_eqcheck(plan, variant, errata=None):
    """errata: exact chain strings to skip - a known, deliberately-kept printed-book error
    (e.g. maths7_ch10's content.py `K.ERRATA = ["-1 x -1 x -1 x -1 x -1 = 1"]`), never a way
    to silence a real gate failure. Each one must be used by the plan; an entry that matches
    nothing is itself an error, so a stale exemption can't linger unnoticed."""
    mod = _eqcheck_module(variant)
    errata = set(errata or [])
    used = set()
    errors, n = [], 0
    for text in _authored_texts(plan):
        if variant == "plain":
            fails, checked = mod.arithmetic_in_text(text)
        else:
            fails, checked = mod.false_equations(text), mod.count_checked(text)
        n += checked
        for s in fails:
            # eqcheck_plain's failures are the bare chain; eqcheck_signed/powers append
            # "  ->  [evaluated sides]" to it - match by prefix so one errata entry (the
            # authored chain text) works against either shape.
            hit = next((e for e in errata if s == e or s.startswith(e + "  ->")), None)
            if hit:
                used.add(hit)
                continue
            errors.append("false equation: %s" % s)
    errors += ["errata entry never matched (remove it from config): %s" % s
               for s in errata - used]
    return errors, n


def run(plan, config):
    """(errors, counts) - errors is a flat list of blocking strings; counts is a dict of per-gate
    tallies, plus counts["warnings"] (a flat list of non-blocking, advisory strings - see the
    module docstring's "Blocking errors vs advisory warnings" section)."""
    errors = []
    warnings = []
    counts = {}

    structure_problems = media_content.preflight(plan)
    errors += ["structure: %s" % p for p in structure_problems]
    counts["structure_problems"] = len(structure_problems)

    variant = config.get("eqcheck", "plain")
    eq_errors, n_eq = run_eqcheck(plan, variant, config.get("eqcheck_errata"))
    errors += eq_errors
    counts["equations_checked"] = n_eq
    counts["equations_failed"] = len(eq_errors)

    is_theorem_chapter = config.get("grade_band") == "9_10" or config.get("theorem_chapter")

    gate_families = [("coverage", coverage), ("video_script_rules", video_script_rules)]
    if is_theorem_chapter:
        gate_families.append(("theorem_variant", theorem_variant))
    else:
        gate_families += [("skeleton", skeleton), ("objectives", objectives)]
    if config.get("solutions"):
        gate_families.append(("solution_content", solution_content))
    if config.get("question_layout"):
        gate_families.append(("question_layout", question_layout))

    for name, mod in gate_families:
        gate_messages = ["%s: %s" % (name, e) for e in mod.check(plan, config)]
        gate_errors = [m for m in gate_messages if not _is_advisory(m)]
        gate_warnings = [m for m in gate_messages if _is_advisory(m)]
        errors += gate_errors
        warnings += gate_warnings
        counts["%s_problems" % name] = len(gate_errors)
        if gate_warnings:
            counts["%s_warnings" % name] = len(gate_warnings)

    counts["warnings"] = warnings
    return errors, counts


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    plan = json.load(open(sys.argv[1], encoding="utf-8"))
    config = json.load(open(sys.argv[2], encoding="utf-8"))
    errors, counts = run(plan, config)
    warnings = counts.pop("warnings", [])
    print("counts:", counts)
    if warnings:
        print("%d ADVISORY WARNING(S) (non-blocking):" % len(warnings))
        for w in warnings:
            print("  ~", w)
    if errors:
        print("%d GATE FAILURE(S):" % len(errors))
        for e in errors:
            print("  -", e)
        return 1
    print("all gates passed (blocking)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
