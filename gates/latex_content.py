# -*- coding: utf-8 -*-
"""LaTeX content gate: every concept's displayed text is free of the known LaTeX-authoring
mistakes core/solutions/latex_checker.py catches - whether the text came from
core/solutions/latex_convert.py or was hand-authored per core/solutions/LATEX_REFERENCE.md.

Runs whenever chapter.config.json has a truthy `"solutions"` (the same condition
gates/solution_content.py uses - LaTeX only appears in `text`/`publication_text` once an item's
steps/answer have been authored with inline `$...$` math).

Two severities, matching core/solutions/latex_checker.py's own fixable/flag-only split:
  - fixable (an exponent swallowing a fraction, a command glued to the next letter, a doubled
    \\text{\\text{}}, a lone paren wrapped on its own, a split roman-numeral label): these are
    unambiguously wrong regardless of context, so they block the stamp like any other gate error.
  - flag-only (a bare unit letter that might be a variable, the same letter wrapped in some
    places but not others, an unbalanced $ count): these need a human's judgement call, so they
    are downgraded to advisory warnings the same way gates/objectives.py's and gates/coverage.py's
    own shallow heuristics are (see gates/gate_runner.py's "Blocking errors vs advisory warnings"
    and its ADVISORY_MARKERS list - this gate's flag messages end in the marker string below).

    python -B latex_content.py <plan.json> <chapter.config.json>
"""
from __future__ import annotations

import json
import sys

try:
    from ..core.solutions import latex_checker
except ImportError:                      # run as a script, or package-relative import unavailable
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "core", "solutions"))
    import latex_checker

# the exact substring gate_runner.py's ADVISORY_MARKERS must include for this gate's flag-only
# issues to be downgraded to non-blocking warnings instead of failing the stamp.
ADVISORY_MARKER = "needs a human check, not auto-fixable"

TEXT_FIELDS = ("text", "publication_text")


def walk_topics(plan):
    for module in plan.get("modules") or []:
        for segment in module.get("segments") or []:
            for topic in segment.get("topics") or []:
                yield topic


def check(plan, config=None):
    if not (config or {}).get("solutions"):
        return []
    problems = []
    for topic in walk_topics(plan):
        for concept in topic.get("concepts") or []:
            cid = concept["concept_id"]
            for block in concept.get("content") or []:
                for field in TEXT_FIELDS:
                    text = block.get(field)
                    if not isinstance(text, str) or not text:
                        continue
                    for issue in latex_checker.check(text):
                        tag = "" if issue.fixable else (" (%s)" % ADVISORY_MARKER)
                        problems.append("%s/%s: %s: %s%s" % (cid, field, issue.kind, issue.message, tag))
    return problems


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    plan = json.load(open(sys.argv[1], encoding="utf-8"))
    config = json.load(open(sys.argv[2], encoding="utf-8"))
    problems = check(plan, config)
    for p in problems:
        print("-", p)
    print("%d problem(s)" % len(problems))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
