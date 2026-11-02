"""Writes manifest.json and plan_text.json for the question concepts of the live plan.
Keeps any status already set, so approved images stay approved."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_v10 import fetch_live

HERE = os.path.dirname(os.path.abspath(__file__))
KEY_DIR = "V2/cbse/cbse/english/class_8/mathematics/ch_9/image_v5"


def part_of(block, name):
    """The '(i)' at the end of a multi-part block's book number, or ''."""
    tail = block["book_number"].replace(name, "", 1).strip()
    return tail


def text_of(concept):
    blocks = [b for b in concept["content"] if b.get("item_kind") in ("exercise", "example")]
    name = concept["concept_name"]
    if len(blocks) == 1:
        b = blocks[0]
        return {"name": name, "q": b["question"], "steps": b["steps"], "ans": b["answer"]}
    tails = [part_of(b, name) for b in blocks]
    # Parts repeat the same stem; keep it once
    questions = [b["question"] for b in blocks]
    stem = os.path.commonprefix(questions)
    stem = stem[:stem.rfind(": ") + 2] if ": " in stem else ""
    return {
        "name": name,
        "q": questions[0] + " " + " ".join(q[len(stem):] for q in questions[1:]),
        "steps": ["%s %s" % (t, s) for t, b in zip(tails, blocks) for s in b["steps"]],
        "ans": "; ".join("%s %s" % (t, b["answer"]) for t, b in zip(tails, blocks)),
    }


def write(live, version):
    path = os.path.join(HERE, "manifest.json")
    old = {}
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            old = {e["id"]: e.get("status") for e in json.load(f)["images"]}
    images, plan_text = [], {}
    for module in live["modules"]:
        for segment in module["segments"]:
            for topic in segment["topics"]:
                for concept in topic["concepts"]:
                    if concept.get("concept_kind") != "exercise":
                        continue
                    cid = concept["concept_id"]
                    short = cid.rsplit(".", 1)[1]
                    plan_text[cid] = text_of(concept)
                    for n, role, tag in ((1, "question", "q"), (2, "solution", "sol")):
                        iid = "%s.IMG%d" % (cid, n)
                        images.append({"id": iid, "concept_id": cid, "concept_short": short,
                                       "role": role, "scene_file": "%s_%s.py" % (short, tag),
                                       "scene_class": "%s_%s" % (short, tag),
                                       "status": old.get(iid) or "draft"})
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"key_dir": KEY_DIR, "images": images}, f, indent=1)
    with open(os.path.join(HERE, "plan_text.json"), "w", encoding="utf-8") as f:
        json.dump(plan_text, f, ensure_ascii=False, indent=1)
    print("live v%d: %d concepts, %d images" % (version, len(plan_text), len(images)))


if __name__ == "__main__":
    write(*fetch_live())
