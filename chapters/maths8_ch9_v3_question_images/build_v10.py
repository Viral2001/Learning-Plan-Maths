"""Add the 24 question images to the live Phase 3 plan.

    python build_v10.py          build out/<plan id>.json and diff it against the live plan
    python build_v10.py assets   also upload every PNG and code file to the bucket

The plan is fetched live, not read from an old file, because others work on this chapter.
Only image nodes, media_ids and image_decision may change. Anything else stops the build.
"""
import json
import os
import re
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "core", "image_editor"))
import bucket  # noqa: E402

CHAPTER_ID = "cbse_eng_maths8_ch9_V3"
API = "https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/chapter/" + CHAPTER_ID

DIAGRAMS = {
    "C27": "An upright right triangle has hypotenuse 10 and a question mark on each of the other two sides.",
    "C36": "Two squares stand side by side, one of side 7 and one of side 5.",
    "C40": "An upright right triangle has short side 8 cm, hypotenuse 17 cm and a question mark on the third side.",
    "C41": "An upright right triangle has a = 5, b = 7 and c = ? on the hypotenuse.",
    "C42": "An upright right triangle has sides 7 and 9 at the right angle and a question mark on the hypotenuse.",
    "C43": "An upright right triangle has sides a and b and hypotenuse c.",
    "C60": "A rectangle with one diagonal has a question mark on each of two sides and on the diagonal.",
    "C65": "A 5 by 5 grid of dots is shown.",
    "C66": "An equilateral triangle has 6 written on each side.",
}
QUESTION_TEXT = {
    "C41": "Find the missing sidelength of a right triangle when a = 5 and b = 7, with c the hypotenuse.",
    "C42": "Find the missing sidelength in the following right triangle.",
}


def fetch_live():
    with urllib.request.urlopen(API, timeout=60) as r:
        data = json.load(r)["data"]
    plan = data["plan"]["planJson"]
    return (json.loads(plan) if isinstance(plan, str) else plan), data["plan"]["version"]


def next_version():
    with urllib.request.urlopen(API + "/versions", timeout=60) as r:
        return max(v["version"] for v in json.load(r)["data"]) + 1


def node(entry, plan_text, key_dir):
    short, role = entry["concept_short"], entry["role"]
    name = plan_text["name"]
    url = bucket.public_url(key_dir, entry["id"] + ".png")
    if role == "question":
        question = QUESTION_TEXT.get(short) or re.sub(r"\s*\[Hint:.*?\]", "", plan_text["q"], flags=re.S)
        text = "Question card: %s %s No working or answer is shown." % (question, DIAGRAMS.get(short, ""))
        instruction = "Try this question yourself before you open the solution."
        notes = "Let the student attempt this before showing the video or the solution image."
    else:
        text = "Solution card with numbered working steps and a highlighted answer: %s." % plan_text["ans"].rstrip(".")
        instruction = "Compare this with your own working, step by step."
        notes = "Show only after the student has attempted the question."
    return {
        "id": entry["id"],
        "type": "image",
        "subtype": "illustration",
        "title": "%s: %s" % (name, role),
        "image_url": url,
        "planned_url": url,
        "image_role": role,
        "render_source": {
            "engine": "manim",
            "scene": entry["scene_class"],
            "code_url": bucket.public_url(key_dir + "/code", entry["id"] + ".py"),
            "style_url": bucket.public_url(key_dir + "/code", "_style.py"),
        },
        "concept_id": entry["concept_id"],
        "home_concept_id": entry["concept_id"],
        "related_concept_ids": [],
        "image_category": "concept",
        "image_dimensions": "1920x1080",
        "aspect_ratio": "16:9",
        "build_status": "built",
        "context": "%s image for %s." % (role.capitalize(), name),
        "description": " ".join(text.split()),
        "instructions_for_student": instruction,
        "teaching_notes": notes,
        "labels": [],
        "regions": [],
        "tutor_can_highlight": [],
        "accuracy_constraints": "",
        "generation_prompt": "",
        "negative_prompt": "",
        "source_image": {"note": "Rendered from Manim code; see render_source."},
        "source_image_key": "",
    }


def build(live, version, entries, plan_text, key_dir):
    plan = json.loads(json.dumps(live))
    by_concept = {}
    for e in entries:
        by_concept.setdefault(e["concept_id"], []).append(e)
    done = set()
    for module in plan["modules"]:
        for segment in module["segments"]:
            for topic in segment["topics"]:
                for concept in topic.get("concepts", []):
                    picks = by_concept.get(concept["concept_id"])
                    if not picks:
                        continue
                    if any(m["id"] == e["id"] for e in picks for m in topic["media"]):
                        raise SystemExit("Already in the plan: %s" % concept["concept_id"])
                    topic["media"].extend(node(e, plan_text[e["concept_id"]], key_dir) for e in picks)
                    concept["media_ids"] = [e["id"] for e in picks] + concept["media_ids"]
                    concept["image_decision"] = {
                        "needed": True,
                        "why": "A question concept: one image shows the question and its figure "
                               "for the attempt, and one shows the worked solution.",
                    }
                    done.add(concept["concept_id"])
    if done != set(by_concept):
        raise SystemExit("Concepts not found: %s" % sorted(set(by_concept) - done))
    plan["version"] = version
    plan["plan_id"] = "%s_v%d" % (CHAPTER_ID, version)
    return plan


def leaves(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from leaves(v, path + "/" + k)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from leaves(v, "%s/%d" % (path, i))
    else:
        yield path, obj


def check_diff(live, plan):
    """Every changed leaf must be one of the planned additions."""
    old, new = dict(leaves(live)), dict(leaves(plan))
    allowed = re.compile(r"^/(version|plan_id)$|/media/\d+/|/media_ids/\d+$|/image_decision/")
    bad = [p for p in set(old) | set(new)
           if old.get(p, "\0") != new.get(p, "\0") and not allowed.search(p)]
    if bad:
        raise SystemExit("Unexpected changes: %s" % sorted(bad)[:20])

    # Existing media must survive untouched, in order, at the front of each list
    def media(p):
        return {t["topic_id"]: t["media"] for m in p["modules"] for s in m["segments"]
                for t in s["topics"]}
    before, after = media(live), media(plan)
    for topic_id, items in before.items():
        if after[topic_id][:len(items)] != items:
            raise SystemExit("Existing media changed in %s" % topic_id)
    return sum(len(after[t]) - len(before[t]) for t in before)


def upload_assets(entries, key_dir):
    pngs = [(e["id"] + ".png", open(os.path.join(HERE, "png", e["id"] + ".png"), "rb").read())
            for e in entries]
    codes = [(e["id"] + ".py", open(os.path.join(HERE, "scenes", e["scene_file"]), "rb").read())
             for e in entries]
    codes.append(("_style.py", open(os.path.join(HERE, "_style.py"), "rb").read()))
    bucket.upload(key_dir, pngs)
    bucket.upload(key_dir + "/code", codes)
    print("bucket ok: %d png, %d code files" % (len(pngs), len(codes)))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    with open(os.path.join(HERE, "manifest.json"), encoding="utf-8") as f:
        manifest = json.load(f)
    with open(os.path.join(HERE, "plan_text.json"), encoding="utf-8") as f:
        plan_text = json.load(f)
    entries, key_dir = manifest["images"], manifest["key_dir"]

    live, live_version = fetch_live()
    version = next_version()
    plan = build(live, version, entries, plan_text, key_dir)
    added = check_diff(live, plan)
    os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    out = os.path.join(HERE, "out", plan["plan_id"] + ".json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(plan, f, ensure_ascii=False, indent=1)
    print("live v%d -> v%d, %d image nodes added: %s" % (live_version, version, added, out))

    if "assets" in sys.argv[1:]:
        upload_assets(entries, key_dir)


if __name__ == "__main__":
    main()
