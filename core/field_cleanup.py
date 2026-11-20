# -*- coding: utf-8 -*-
"""Field cleanup of a built or live plan (docs/karan-MD/LEARNING_PLAN_FIELD_CLEANUP_AND_LATEX 1.md, Part 1).

Generic copy of chapters/maths5_ch1/new_design/cleanup_fields.py, so any Class 6-8 chapter can use it
(core/qa_split_live.py calls it first). Class 6-8 is the 6-8 band (grade_band "6_8"): the gates that read
source_type, source_segment_role and a tool node's tool_id (gates/skeleton.py, gates/objectives.py,
gates/question_layout.py) are active, so those fields STAY.

Removed, because no gate or core module reads them from a finished plan (the guide's section 3, checked
against gates/ and core/ by grep, not by name):
  objective  objective_level
  topic      estimated_minutes, source_content_flow; ncert_sections is RENAMED source_topic_ids
  concept    tool_media_id, source_tool_ref, walkthrough_video_id, authored_key, media_key, image_decision,
             source_delivery_mods, estimated_minutes
  image      regions, source_image, source_image_key, tutor_can_highlight - only when every image of the
             chapter carries the same empty value for the field (the guide's section 4: values, not names)
KEPT on purpose: video_coverage (gates/video_script_rules.py reads it), is_enrichment, topic_objective,
image_role, build_status, planned_url, render_source, tool_name, tool_id, source_type, source_segment_role,
_is_thin_extra, qt_part.

clean(plan, grade_band) edits the plan in place and returns {field: how many removed}.
"""
from __future__ import annotations

import json

CONCEPT_ALWAYS = ("tool_media_id", "source_tool_ref", "walkthrough_video_id", "authored_key", "media_key",
                  "image_decision", "source_delivery_mods", "estimated_minutes")
TOPIC_ALWAYS = ("estimated_minutes", "source_content_flow")
IMAGE_IF_EMPTY = ("regions", "source_image", "source_image_key", "tutor_can_highlight")


def _topics(plan):
    return [t for m in plan.get("modules") or [] for s in m.get("segments") or [] for t in s.get("topics") or []]


def _is_empty(v):
    return v in (None, "", [], {}) or (isinstance(v, dict) and set(v) <= {"note"})


def clean(plan, grade_band="6_8"):
    removed = {}

    def drop(d, key, tag):
        if key in d:
            del d[key]
            removed[tag] = removed.get(tag, 0) + 1

    topics = _topics(plan)
    for o in plan.get("objectives") or []:
        drop(o, "objective_level", "objective.objective_level")
    for t in topics:
        for k in TOPIC_ALWAYS:
            drop(t, k, "topic.%s" % k)
        if "ncert_sections" in t:
            t.setdefault("source_topic_ids", t.pop("ncert_sections"))
            t.pop("ncert_sections", None)
            removed["topic.ncert_sections->source_topic_ids"] = removed.get(
                "topic.ncert_sections->source_topic_ids", 0) + 1
        if grade_band == "9_10":
            drop(t, "source_type", "topic.source_type")
        for c in t.get("concepts") or []:
            for k in CONCEPT_ALWAYS:
                drop(c, k, "concept.%s" % k)
            if grade_band == "9_10":
                drop(c, "source_segment_role", "concept.source_segment_role")
    images = [x for t in topics for x in t.get("media") or [] if x.get("type") == "image"]
    for k in IMAGE_IF_EMPTY:
        values = {json.dumps(x[k], sort_keys=True) for x in images if k in x}
        if values and all(_is_empty(json.loads(v)) for v in values):
            for x in images:
                drop(x, k, "image.%s" % k)
    if grade_band == "9_10":
        for t in topics:
            for x in t.get("media") or []:
                if x.get("type") == "2d_tool":
                    drop(x, "tool_id", "tool.tool_id")
    return removed
