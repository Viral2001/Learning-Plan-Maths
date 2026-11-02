# -*- coding: utf-8 -*-
"""Chapter-skeleton gate: the topic sequence and tool placement a new-design chapter must have.

Generalized from the hand-rolled skeleton checks in three System-B build.py's check() functions
(maths6_ch3, maths7_ch10, maths8_ch9). All three plans share one shape once you look past the
field-name drift between chapters:

  * topic["source_type"] (not the coarse topic["topic_type"], which just says
    framing/instructional/summary everywhere) is what actually distinguishes an idea topic from
    a question topic - both come back as topic_type "instructional". The three chapters spell
    the idea-topic value identically ("instructional/exploration") but disagree on the
    question-topic spelling ("question_topic" in maths6_ch3, "exercise" in maths7_ch10/maths8_ch9),
    so that set is configurable.
  * topic["is_enrichment"] is True on exactly the topics that get no topic_objective: the intro
    and every question topic. False on idea topics and the summary. This is the one field that
    agrees across all three chapters, so it backs the "no topic_objective" check directly rather
    than re-deriving it from source_type.
  * The intro's free-try tool (a second "try_it" concept holding one 2d_tool, after the "hook"
    concept) only exists in maths8_ch9; maths6_ch3/maths7_ch10 ship a hook-only intro with no
    tool at all. The task that commissioned this gate wants the free-try tool as the target shape
    going forward, so it is required by default (`intro_requires_free_try_tool`); running this
    gate against the two older chapters will therefore flag a real, expected gap - that is
    signal, not a bug in the gate.
  * The "last concept of an idea topic is the pull-it-together/doer concept with the one tool"
    rule is universal, but the concept-name prefix that announces it is not: "Pull it together
    and do it: " in maths6_ch3/maths7_ch10, "Practice: " in maths8_ch9. Both are accepted by
    default; a future chapter can add its own via config.
  * The 2-4 concept-count range only ever applied to "primary" concepts. maths7_ch10 tags extra
    concepts folded into a topic (an additional worked example, say) with "_is_thin_extra": True,
    and its own check() explicitly excludes them before counting; maths6_ch3/maths8_ch9 never
    produce that field at all, so excluding it is a no-op there. Skipped by `thin_extra_field`
    when a concept has the field set True; set the config key to None to count every concept.

    python -B skeleton.py <plan.json> [chapter.config.json]
"""
from __future__ import annotations

import io
import json
import sys

from .media_content import walk_topics

DEFAULTS = {
    "framing_source_type": "framing",
    "summary_source_type": "summary",
    "idea_source_type": "instructional/exploration",
    "qt_source_types": ("question_topic", "exercise"),
    "hook_role": "hook",
    "try_it_role": "try_it",
    "doer_role": "doer",
    "intro_requires_free_try_tool": True,
    "intro_requires_handover": True,
    "idea_topic_concept_range": (2, 4),
    "doer_name_prefixes": ("pull it together and do it:", "practice:"),
    "qt_item_ref_field": "ncert_refs",
    "qt_must_follow_idea_topic": True,
    "thin_extra_field": "_is_thin_extra",
    # True lets an idea topic's doer carry no tool (0 or 1, never more): for a chapter that keeps tools
    # only where the manipulation is the concept, so its tool count stays below its idea-topic count.
    "doer_tool_optional": False,
}


def _cfg(config, key):
    return (config or {}).get(key, DEFAULTS[key])


def _tools(topic):
    return [m for m in topic.get("media") or [] if m.get("type") == "2d_tool"]


def _tool_on(topic, concept_id):
    """The 2d_tool media node(s) attached to one concept of this topic, by its concept_id."""
    return [m for m in _tools(topic) if m.get("concept_id") == concept_id]


def check(plan, config=None):
    """Return a list of problem strings; empty means clean. `config` is the chapter.config.json
    dict (or None for every default above)."""
    problems = []
    topics = list(walk_topics(plan))
    if not topics:
        return ["no topics at all"]

    framing_t = _cfg(config, "framing_source_type")
    summary_t = _cfg(config, "summary_source_type")
    idea_t = _cfg(config, "idea_source_type")
    qt_types = set(_cfg(config, "qt_source_types"))
    hook_role = _cfg(config, "hook_role")
    try_it_role = _cfg(config, "try_it_role")
    doer_role = _cfg(config, "doer_role")
    lo, hi = _cfg(config, "idea_topic_concept_range")
    prefixes = tuple(p.lower() for p in _cfg(config, "doer_name_prefixes"))
    ref_field = _cfg(config, "qt_item_ref_field")
    thin_field = _cfg(config, "thin_extra_field")

    # ---- intro: first topic, hook (+ free-try/handover), enrichment, no topic_objective ----
    intro = topics[0]
    if intro.get("source_type") != framing_t:
        problems.append("intro: topic[0].source_type is %r, want %r" % (intro.get("source_type"), framing_t))
    if not intro.get("is_enrichment"):
        problems.append("intro: must be is_enrichment True")
    if intro.get("topic_objective"):
        problems.append("intro: must carry no topic_objective (enrichment topics never get one)")
    intro_concepts = intro.get("concepts") or []
    if not intro_concepts or intro_concepts[0].get("source_segment_role") != hook_role \
            or not intro_concepts[0].get("is_enrichment"):
        problems.append("intro: first concept must be the %r hook, is_enrichment True" % hook_role)
    if _cfg(config, "intro_requires_free_try_tool"):
        try_concepts = [c for c in intro_concepts if c.get("source_segment_role") == try_it_role]
        if not try_concepts:
            problems.append("intro: no %r free-try concept (config intro_requires_free_try_tool=True)"
                            % try_it_role)
        else:
            tc = try_concepts[0]
            tools = _tool_on(intro, tc.get("concept_id"))
            if not tc.get("is_enrichment"):
                problems.append("intro: the %r concept must be is_enrichment True" % try_it_role)
            if len(tools) != 1:
                problems.append("intro: the %r concept needs exactly 1 tool, found %d"
                                % (try_it_role, len(tools)))
        if _cfg(config, "intro_requires_handover") and intro_concepts:
            hook = intro_concepts[0]
            hook_media_ids = set(hook.get("media_ids") or [])
            hook_videos = [m for m in intro.get("media") or []
                           if m.get("type") == "video" and (m.get("id") in hook_media_ids
                                                              or m.get("concept_id") == hook.get("concept_id"))]
            for v in hook_videos:
                points = v.get("interaction_points") or []
                if not points:
                    continue
                last = points[-1]
                if last.get("type") != "open" or not last.get("handover"):
                    problems.append("intro: the hook video must end on an open question with a handover "
                                    "to the free-try tool")

    # ---- summary: last topic, no tool ----
    tail = topics[-1]
    if tail.get("source_type") != summary_t:
        problems.append("summary: topic[-1].source_type is %r, want %r" % (tail.get("source_type"), summary_t))
    if _tools(tail):
        problems.append("%s: the summary topic must carry no tool" % tail.get("topic_id"))
    if tail.get("topic_objective"):
        problems.append("%s: the summary topic must carry no topic_objective" % tail.get("topic_id"))

    # ---- every topic strictly between intro and summary ----
    for i, t in enumerate(topics):
        if t is intro or t is tail:
            continue
        tid = t.get("topic_id")
        source_type = t.get("source_type")

        if source_type in qt_types:
            if _tools(t):
                problems.append("%s: a question topic must carry no tool" % tid)
            if t.get("topic_objective"):
                problems.append("%s: a question topic must carry no topic_objective" % tid)
            concepts = t.get("concepts") or []
            if not concepts:
                problems.append("%s: question topic has no concepts" % tid)
            for c in concepts:
                refs = c.get(ref_field) or []
                if len(refs) != 1:
                    problems.append("%s: %s maps to %d exercise/FIO item(s) via %s (want exactly 1)"
                                    % (tid, c.get("concept_id"), len(refs), ref_field))
            if _cfg(config, "qt_must_follow_idea_topic"):
                prev = topics[i - 1] if i > 0 else None
                if prev is None or prev.get("source_type") != idea_t:
                    problems.append("%s: a question topic must come immediately after its idea topic "
                                    "(previous topic's source_type is %r)" % (tid, prev and prev.get("source_type")))
            continue

        if source_type != idea_t:
            # Not framing/summary/qt/idea: an unrecognised topic kind. Flag it rather than
            # silently skipping, since it means either new vocabulary this config hasn't been
            # taught yet, or a genuinely malformed topic.
            problems.append("%s: source_type %r is none of framing/summary/%s/idea (%r)"
                            % (tid, source_type, "|".join(sorted(qt_types)), idea_t))
            continue

        concepts = t.get("concepts") or []
        primary = [c for c in concepts if not (thin_field and c.get(thin_field))]
        if not lo <= len(primary) <= hi:
            problems.append("%s: %d primary concept(s) (keep %d to %d)" % (tid, len(primary), lo, hi))
        if not t.get("topic_objective"):
            problems.append("%s: idea topic is missing its topic_objective" % tid)
        if not concepts:
            continue
        last = concepts[-1]
        if last.get("source_segment_role") != doer_role:
            problems.append("%s: the last concept must be the %r concept" % (tid, doer_role))
        tools = _tool_on(t, last.get("concept_id"))
        if _cfg(config, "doer_tool_optional"):
            if len(tools) > 1:
                problems.append("%s: the last concept carries %d tools (at most 1)" % (tid, len(tools)))
        elif len(tools) != 1:
            problems.append("%s: the last concept needs exactly 1 tool attached, found %d"
                            % (tid, len(tools)))
        name = (last.get("concept_name") or "").strip().lower()
        if prefixes and not any(name.startswith(p) for p in prefixes):
            problems.append("%s: the last concept's name does not open with any of %r"
                            % (tid, _cfg(config, "doer_name_prefixes")))
        earlier_doers = [c for c in concepts[:-1] if c.get("source_segment_role") == doer_role]
        if earlier_doers:
            problems.append("%s: a %r concept appears before the last concept" % (tid, doer_role))

    return problems


# ------------------------------------------------------------------ self-test
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    plan = json.load(io.open(sys.argv[1], encoding="utf-8"))
    cfg = json.load(io.open(sys.argv[2], encoding="utf-8")) if len(sys.argv) > 2 else {}
    problems = check(plan, cfg)
    print("%s: %d problem(s)" % (sys.argv[1], len(problems)))
    for p in problems:
        print("  -", p)
