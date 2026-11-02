# -*- coding: utf-8 -*-
"""Build plan media nodes from video scripts, the same way for every chapter (docs/28).

The node keeps the plan's usual video fields (Part 8) and adds `video_script`, the only field the render
pipeline reads. `interaction_points` are derived from the beats that pause: each video has exactly one, its
think-and-tell (Keeko design, 28 Oct 2026), and the render holds that pause for 3 seconds.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import contract as K  # noqa: E402
from check import spoken, words, sentences  # noqa: E402

KIND_CONTEXT = {
    "hook": "Hook video: it opens the topic with a question and teaches nothing yet. It plays before the concept.",
    "worked": ("Concept video: one solved example from the book, shown after the concept that uses its idea. "
               "It ends when Keeko raises a hand with a doubt."),
    "exercise": ("Question video: one question from the book, solved step by step by the method of the book's "
                 "solved example. It opens only after the student has tried the question."),
    "theorem": ("Concept video: the claim, cases that make it believable, then the proof with a reason for every "
                "step. It ends when Keeko raises a hand with a doubt."),
    "story": "Story video: one of the chapter's big why ideas, told as a story. It ends when Keeko raises a hand.",
}
KIND_STUDENT = {
    "hook": "Watch, and when the video says think and tell, say your answer out loud before you go on.",
    "worked": "When the video says think and tell, say your answer out loud. Then watch how the book's example is solved.",
    "exercise": "Try the question in your notebook first. Then watch; when the video says think and tell, say your answer.",
    "theorem": "When the video says think and tell, guess first. Then follow each step of the proof and its reason.",
    "story": "Watch, and when the video says think and tell, say your answer before it goes on.",
}


def beat_words(b):
    return sum(len(words(spoken(l))) for l in b["narration"])


def duration_seconds(script) -> int:
    total = sum(beat_words(b) for b in script["beats"]) / K.WPS
    total += sum(b.get("pause_after", 0) for b in script["beats"])
    return int(round(total))


def interaction_points(script, video_id):
    """One point per beat that pauses: the video's single think-and-tell. `at_s` is when the beat's narration ends."""
    pts, t = [], 0.0
    kind = script["kind"]
    fa = script.get("final_answer") or {}
    asked = []                       # the questions put so far; the think-and-tell beat answers the latest one
    for b in script["beats"]:
        t += beat_words(b) / K.WPS
        asked += [x for x in sentences(" ".join(spoken(l) for l in b["narration"])) if x.endswith("?")]
        if b.get("pause_after", 0) > 0:
            last = spoken(b["narration"][-1])
            sens = sentences(last)
            prompt = sens[-1] if sens else last
            if asked and prompt.lower().startswith(("think", "stop", "try")):
                prompt = asked[-1]
            answers = kind in ("worked", "exercise") and b["part"] == "hook"
            pts.append({
                "id": f"{video_id}.P{len(pts) + 1}",
                "beat_key": b["key"],
                "at_s": int(round(t)),
                "pause_s": b["pause_after"],
                "type": "say",
                "prompt": prompt,
                "answer": str(fa.get("value", "")) if answers else "",
                "reveal": "after_resume" if answers else "",
                "covers": list(script.get("source", [])) if answers else [],
            })
            t += b["pause_after"]
    return pts


def photo_rows(script, photos, photo_base):
    """The photos this video shows, in beat order, each with its reserved url (docs/25 §14 "Photos inside
    videos"). A photo is generated with Gemini from `gemini_prompt`, uploaded to `planned_url`, and loaded by the
    renderer as an ImageMobject for its beat only; `image_url` stays empty until then."""
    rows = {}
    for b in script.get("beats", []):
        ph = b.get("photo")
        if not isinstance(ph, dict) or ph.get("id") not in (photos or {}):
            continue
        p = photos[ph["id"]]
        r = rows.setdefault(ph["id"], {
            "photo_id": p["id"], "subject_type": p["subject_type"], "subject": p["subject"],
            "alt_text": p["alt_text"], "gemini_prompt": p["gemini_prompt"], "reference": p["reference"],
            "maths_on_object": p["maths_on_object"], "pair_with": p["pair_with"],
            "beats": [], "placement": ph["placement"], "leaves": "at the end of its beat, before any beat with maths",
            "generator": "gemini", "image_url": "", "planned_url": f"{photo_base}/{p['id']}.png",
            "build_status": "placeholder"})
        r["beats"].append(b["key"])
    return list(rows.values())


def video_node(doc, *, video_id, concept_id, chapter_label, planned_url, related_concept_ids=None,
               photos=None, photo_base=""):
    """A plan media node for one authored script file (`doc` = {key, title, description, teaching_notes,
    video_script}). `photos` is the chapter photo library; the node lists the ones its beats show."""
    s = doc["video_script"]
    kind = s["kind"]
    placement_text = {
        "before": "before the concept",
        "after": "after the concept's text" + (", opened only after the student tries the question"
                                                if s["unlock"] == "after_attempt" else ""),
    }[s["placement"]]
    return {
        "id": video_id,
        "type": "video",
        "subtype": "generated",
        "title": doc["title"],
        "context": f"{chapter_label}. {KIND_CONTEXT[kind]} PLACEHOLDER: scripted to docs/28, not rendered yet.",
        "description": doc["description"],
        "concept_id": concept_id,
        "home_concept_id": concept_id,
        "aspect_ratio": "16:9",
        "video_url": "",
        "planned_url": planned_url,
        "video_duration_seconds": str(duration_seconds(s)),
        "teaching_notes": doc["teaching_notes"],
        "instructions_for_student": KIND_STUDENT[kind],
        "related_concept_ids": list(related_concept_ids or []),
        "source_video_walkthrough": {
            "type": kind,
            "title": doc["title"],
            "video_id": video_id,
            "placement": placement_text,
            "unlock": s["unlock"],
            "items": list(s["source"]),
            "intent": s["why"],
            "withheld": "; ".join(s["hold_back"]),
            "source": "video_script",
        },
        "video_role": kind,
        "interactive": True,
        "interaction_points": interaction_points(s, video_id),
        "video_script": s,
        "source_video_key": doc["key"],
        "build_status": "placeholder",
    } | ({"photos": rows} if (rows := photo_rows(s, photos, photo_base)) else {})


def coverage_rows(videos, labels):
    """Plan-level video_coverage: one row per book item a video covers.

    `videos` is a list of (node, item_ids); `labels` maps item_id -> the book's label (e.g. "Example 4")."""
    rows = []
    for node, item_ids in videos:
        for iid in item_ids:
            rows.append({"book_item": labels.get(iid, iid), "item_id": iid, "video_id": node["id"],
                         "kind": node["video_script"]["kind"]})
    return rows


def strip_dashes(text: str) -> str:
    return re.sub(r"\s*[–—]\s*", ", ", text)
