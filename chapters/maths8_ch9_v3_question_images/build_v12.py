"""Give all 19 question concepts of the live Phase 3 plan their two images.

    python build_v12.py          build out/<plan id>.json and diff it against the live plan
    python build_v12.py assets   also upload every PNG and code file to the bucket

Assets go to image_v4, not image_v3: v11 reused concept ids for other questions, so an old key
such as image_v3/M3.S9.T9.C40.IMG1.png holds a different question from the new id.
Only image nodes, media_ids and image_decision may change. Anything else stops the build.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_v10  # noqa: E402
from build_v10 import CHAPTER_ID, fetch_live, leaves, next_version, node, upload_assets  # noqa: E402

build_v10.DIAGRAMS = {
    "C14": "Two identical squares are each cut along one diagonal, into pieces 1 and 2, and 3 and 4.",
    "C21": "A square has 5 cm marked on two sides and a question mark on one diagonal.",
    "C29": "An upright isosceles right triangle has its equal sides marked and a question mark on the hypotenuse.",
    "C30": "An upright right triangle has hypotenuse 10 and a question mark on each of the other two sides.",
    "C39": "A single square is labelled given square.",
    "C40": "Two squares stand side by side, one of side 7 and one of side 5.",
    "C44": "An upright right triangle has sides 5 cm and 12 cm and a question mark on the hypotenuse.",
    "C45": "An upright right triangle has short side 8 cm, hypotenuse 17 cm and a question mark on the third side.",
    "C46": "An upright right triangle has sides a and b and hypotenuse c.",
    "C47": "Six upright right triangles, (a) to (f), each have two sides marked and a question mark on the third.",
    "C48": "An upright right triangle has sides a and b and hypotenuse c.",
    "C62": "A panel gives the idea from the book and its two worked examples.",
    "C66": "A rectangle with one diagonal has a question mark on each of two sides and on the diagonal.",
    "C71": "A rhombus has its diagonals marked 24 and 70 and a question mark on one side.",
    "C72": "A 5 by 5 grid of dots is shown.",
    "C73": "An equilateral triangle has 6 written on each side.",
}
build_v10.QUESTION_TEXT = {
    "C29": "Find the hypotenuse of an isosceles right triangle with equal sides (i) 3, (ii) 4, (iii) 6, "
           "(iv) 8, (v) 9, with bounds to at least one decimal place.",
    "C46": "Find the missing sidelength of a right triangle, with c the hypotenuse, in five cases: "
           "(i) a = 5, b = 7; (ii) a = 8, b = 12; (iii) a = 9, c = 15; (iv) a = 7, b = 12; "
           "(v) a = 1.5, b = 3.5.",
    "C47": "Find the missing sidelengths in the six right triangles.",
}
WHY = ("A question concept: one image shows the question and its figure for the attempt, "
       "and one shows the worked solution.")


def build(live, version, entries, plan_text, key_dir):
    plan = json.loads(json.dumps(live))
    by_concept = {}
    for e in entries:
        by_concept.setdefault(e["concept_id"], []).append(e)
    done = set()
    for module in plan["modules"]:
        for segment in module["segments"]:
            for topic in segment["topics"]:
                for concept in topic["concepts"]:
                    cid = concept["concept_id"]
                    picks = by_concept.get(cid)
                    if not picks:
                        continue
                    videos = [m for m in concept["media_ids"] if ".VID" in m]
                    extra = [m for m in concept["media_ids"] if ".VID" not in m and ".IMG" not in m]
                    if len(videos) != 1 or extra:
                        raise SystemExit("Unexpected media on %s: %s" % (cid, concept["media_ids"]))
                    media = [m for m in topic["media"] if not m["id"].startswith(cid + ".IMG")]
                    at = next(i for i, m in enumerate(media) if m["id"] == videos[0])
                    first, second = [node(e, plan_text[cid], key_dir) for e in picks]
                    media[at:at + 1] = [first, media[at], second]
                    topic["media"] = media
                    concept["media_ids"] = [first["id"], videos[0], second["id"]]
                    concept["image_decision"] = {"needed": True, "why": WHY}
                    done.add(cid)
    if done != set(by_concept):
        raise SystemExit("Concepts not found: %s" % sorted(set(by_concept) - done))
    plan["version"] = version
    plan["plan_id"] = "%s_v%d" % (CHAPTER_ID, version)
    return plan


def check(live, plan, key_dir, images=38):
    """Non-image nodes and everything outside media_ids and image_decision must be unchanged."""
    def strip(p):
        p = json.loads(json.dumps(p))
        p.pop("version"), p.pop("plan_id")
        kept = {}
        for m in p["modules"]:
            for s in m["segments"]:
                for t in s["topics"]:
                    t["media"] = [x for x in t["media"]
                                  if x["type"] != "image" or not x.get("image_role")]
                    for c in t["concepts"]:
                        kept[c["concept_id"]] = c.pop("media_ids"), c.pop("image_decision", None)
        return p, kept
    old, _ = strip(live)
    new, _ = strip(plan)
    if old != new:
        before, after = dict(leaves(old)), dict(leaves(new))
        bad = [k for k in set(before) | set(after) if before.get(k, "\0") != after.get(k, "\0")]
        raise SystemExit("Unexpected changes: %s" % sorted(bad)[:20])

    roles = [m for mod in plan["modules"] for s in mod["segments"] for t in s["topics"]
             for m in t["media"] if m.get("image_role")]
    live_urls = {m.get("image_url") for mod in live["modules"] for s in mod["segments"]
                 for t in s["topics"] for m in t["media"]}
    if len(roles) != images or any("/" + key_dir + "/" not in m["image_url"] for m in roles):
        raise SystemExit("Image nodes wrong: %d" % len(roles))
    if live_urls & {m["image_url"] for m in roles}:
        raise SystemExit("A new key equals a live key")
    for mod in plan["modules"]:
        for s in mod["segments"]:
            for t in s["topics"]:
                for m in t["media"]:
                    if m.get("image_role") and m["concept_id"] not in [c["concept_id"] for c in t["concepts"]]:
                        raise SystemExit("Image in the wrong topic: %s" % m["id"])
    return len(roles)


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
    count = check(live, plan, key_dir)
    out = os.path.join(HERE, "out", plan["plan_id"] + ".json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(plan, f, ensure_ascii=False, indent=1)
    print("live v%d -> v%d, %d image nodes: %s" % (live_version, version, count, out))

    if "assets" in sys.argv[1:]:
        upload_assets(entries, key_dir)


if __name__ == "__main__":
    main()
