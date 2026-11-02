"""Move the four worked book examples into Questions topics, each as its own concept with two images.

    python build_v13.py          build out/<plan id>.json and check it against the live plan
    python build_v13.py assets   also upload every PNG and code file to the bucket

The worked block and its video move. Book text, predict, teaching and watch_for stay in the teach
concept, and so does any teach image. Concept ids shift, so an old key under image_v4 would hold a
different question from the new id: all 46 images go to image_v5, and image_v4 stays for v12.
The first run keeps the old files in scenes_v12 and png_v12, then renames them to the new ids.
"""
import copy
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_v10  # noqa: E402
import build_v11  # noqa: E402
import build_v12  # noqa: E402
import mk_manifest  # noqa: E402
from build_v10 import CHAPTER_ID, fetch_live, next_version, upload_assets  # noqa: E402
from build_v11 import concepts_of, renumber, topics_of  # noqa: E402

LIVE_VERSION = 12
QUESTIONS = 23
IMAGES = 46

# Source concept -> (Questions topic it joins, concept name). Book order within the topic.
# The book numbers only the first two, so the others carry their book heading and no number.
EXAMPLES = [
    ("M2.S4.T4.C17", "M2.S5.T5", "Isosceles Right Triangles, Example 1"),
    ("M2.S4.T4.C19", "M2.S5.T5", "Isosceles Right Triangles, Example 2"),
    ("M3.S10.T10.C41", "M3.S11.T11", "Using Baudhāyana's Theorem, Worked Example"),
    ("M4.S15.T15.C69", "M4.S16.T16", "A Problem from Bhāskarāchārya's Līlāvatī, Worked Example"),
]
WHOLE = "M2.S4.T4.C19"  # Holds nothing but its example, so the concept itself moves
C17_WHY = ("No figure carries this mathematics: the concept is the rule applied as arithmetic in two "
           "directions. The figure behind the rule is the image of the previous concept, and the book's "
           "two examples are worked in the Questions topic.")
DIAGRAMS = {
    "M2.S4.T4.C17": "An upright isosceles right triangle has equal sides 12 and a question mark on the hypotenuse.",
    "M2.S4.T4.C19": "An upright isosceles right triangle has hypotenuse √72 and a question mark on each equal side.",
    "M3.S10.T10.C41": "An upright right triangle has shorter sides 3 cm and 4 cm and a question mark on the hypotenuse.",
    "M4.S15.T15.C69": "A lake in section: a lotus stands 1 unit above the water, then bends to touch the water "
                      "3 units away. The depth is marked with a question mark.",
}


def example_block(concept):
    blocks = [b for b in concept["content"] if b.get("item_kind") == "example"]
    if len(blocks) != 1:
        raise SystemExit("Expected one example in %s" % concept["concept_id"])
    return blocks[0]


def add_to_anchors(obj, old, new):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == "anchor" and old in value:
                value.insert(value.index(old) + 1, new)
            else:
                add_to_anchors(value, old, new)
    elif isinstance(obj, list):
        for value in obj:
            add_to_anchors(value, old, new)


def restructure(plan):
    topics = {t["topic_id"]: t for t in topics_of(plan)}
    concepts = {c["concept_id"]: c for c in concepts_of(plan)}
    moved, tmp_of, homes = {}, {}, []
    for source_id, target_id, name in EXAMPLES:
        source = concepts[source_id]
        home = next(t for t in topics_of(plan) if source in t["concepts"])
        video_id = source["video_media_ids"][0]
        video = next(x for x in home["media"] if x["id"] == video_id)
        block = example_block(source)
        refs = block["ncert_refs"]
        block["book_number"] = name

        if source_id == WHOLE:
            concept = source
            home["concepts"].remove(source)
            concept["predict_first"] = ""
            tmp_id = source_id
        else:
            tmp_id = "TMP." + source_id
            concept = copy.deepcopy(source)
            concept["concept_id"] = tmp_id
            source["content"] = [b for b in source["content"] if b is not block]
            source["ncert_refs"] = [r for r in source["ncert_refs"] if r not in refs]
            source["video_media_ids"] = []
            source["walkthrough_video_id"] = None
            source["media_ids"] = [m for m in source["media_ids"] if m != video_id]
            video["concept_id"] = video["home_concept_id"] = tmp_id
            add_to_anchors(plan["objectives"], source_id, tmp_id)
            for t in topics_of(plan):
                add_to_anchors(t["learning_objectives"], source_id, tmp_id)
        concept.update({
            "concept_kind": "exercise",
            "concept_name": name,
            "ncert_refs": list(refs),
            "content": [block],
            "source_segment_role": "practice",
            "media_ids": [video_id],
        })
        home["media"].remove(video)
        homes.append(home)
        moved.setdefault(target_id, []).append((concept, video))
        tmp_of[source_id] = tmp_id
        for ref in refs:
            plan["source_metadata"]["ncert_coverage"][ref] = [tmp_id]

    for target_id, items in moved.items():
        topic = topics[target_id]
        topic["concepts"] = [c for c, _ in items] + topic["concepts"]
        topic["media"] = [v for _, v in items] + topic["media"]
    concepts["M2.S4.T4.C17"]["image_decision"]["why"] = C17_WHY

    # A topic whose only video left stops offering video
    for topic in homes:
        if not any(x["type"] == "video" for x in topic["media"]):
            topic["available_content_types"].remove("video")
            topic["secondary_content_type"], topic["tertiary_content_type"] = "image", "paragraph"
    return tmp_of


def check_examples(plan, new_ids):
    owners = {r: c for c in concepts_of(plan) for r in c["ncert_refs"]}
    for source_id, target_id, name in EXAMPLES:
        cid = new_ids[source_id]
        concept = next(c for c in concepts_of(plan) if c["concept_id"] == cid)
        topic = next(t for t in topics_of(plan) if concept in t["concepts"])
        if not topic["topic_name"].startswith("Questions:") or concept["concept_name"] != name:
            raise SystemExit("Example misplaced: %s" % cid)
        kinds = [b.get("item_kind") for b in concept["content"]]
        if kinds != ["example"] or topic["concepts"].index(concept) > 1:
            raise SystemExit("Example content wrong: %s" % cid)
        for ref in concept["ncert_refs"]:
            if owners[ref] is not concept or plan["source_metadata"]["ncert_coverage"][ref] != [cid]:
                raise SystemExit("Ref wrong: %s" % ref)
    for concept in concepts_of(plan):
        if concept.get("concept_kind") != "exercise":
            if any(b.get("item_kind") == "example" for b in concept["content"]):
                raise SystemExit("Example left in teach topic: %s" % concept["concept_id"])
    for row in plan["video_coverage"]:
        owner = owners.get(row["item_id"])
        if owner and owner.get("concept_kind") == "exercise" and row["video_id"] not in owner["media_ids"]:
            raise SystemExit("Coverage wrong: %s" % row["item_id"])


def short(cid):
    return cid.rsplit(".", 1)[1]


def move_files(ids):
    """Rename scenes and PNGs to the new ids, once. Old copies stay for v12."""
    path = os.path.join(HERE, "manifest.json")
    with open(path, encoding="utf-8") as f:
        manifest = json.load(f)
    if not manifest["key_dir"].endswith("image_v4"):
        return
    for name in ("scenes", "png"):
        shutil.copytree(os.path.join(HERE, name), os.path.join(HERE, name + "_v12"))
    entries = manifest["images"]
    # New names can equal old ones, so read everything first and delete before writing
    scenes = {}
    for e in entries:
        file = os.path.join(HERE, "scenes", e["scene_file"])
        with open(file, encoding="utf-8") as f:
            scenes[e["id"]] = f.read()
    pngs = {}
    for e in entries:
        file = os.path.join(HERE, "png", e["id"] + ".png")
        with open(file, "rb") as f:
            pngs[e["id"]] = f.read()
    for e in entries:
        os.remove(os.path.join(HERE, "scenes", e["scene_file"]))
        os.remove(os.path.join(HERE, "png", e["id"] + ".png"))
    for e in entries:
        old_short, tag = e["concept_short"], e["scene_file"][:-3].rsplit("_", 1)[1]
        new_id = ids[e["id"]]
        new_short = short(ids[e["concept_id"]])
        name = "%s_%s" % (new_short, tag)
        code, n = re.subn(r"\bclass %s_%s\(" % (old_short, tag), "class %s(" % name, scenes[e["id"]])
        if n != 1:
            raise SystemExit("Scene class not found: %s" % e["id"])
        with open(os.path.join(HERE, "scenes", name + ".py"), "w", encoding="utf-8", newline="\n") as f:
            f.write(code)
        with open(os.path.join(HERE, "png", new_id + ".png"), "wb") as f:
            f.write(pngs[e["id"]])
        e["id"] = new_id
    with open(path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=1)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    live, live_version = fetch_live()
    if live_version != LIVE_VERSION:
        raise SystemExit("Live is v%d, this build moves v%d" % (live_version, LIVE_VERSION))
    version = next_version()

    plan = copy.deepcopy(live)
    tmp_of = restructure(plan)
    plan, ids = renumber(plan)
    build_v11.order_media_ids(plan)
    build_v11.check(live, plan, QUESTIONS)
    new_ids = {source: ids[tmp] for source, tmp in tmp_of.items()}
    check_examples(plan, new_ids)

    move_files(ids)
    mk_manifest.write(plan, version)
    with open(os.path.join(HERE, "manifest.json"), encoding="utf-8") as f:
        manifest = json.load(f)
    with open(os.path.join(HERE, "plan_text.json"), encoding="utf-8") as f:
        plan_text = json.load(f)
    entries, key_dir = manifest["images"], manifest["key_dir"]

    def new_short(old):
        return next(short(new) for o, new in ids.items() if o.endswith("." + old) and ".C" in o)

    build_v10.DIAGRAMS = {new_short(k): v for k, v in build_v10.DIAGRAMS.items()}
    build_v10.QUESTION_TEXT = {new_short(k): v for k, v in build_v10.QUESTION_TEXT.items()}
    build_v10.DIAGRAMS.update({short(new_ids[k]): v for k, v in DIAGRAMS.items()})

    final = build_v12.build(plan, version, entries, plan_text, key_dir)
    count = build_v12.check(plan, final, key_dir, IMAGES)
    out = os.path.join(HERE, "out", final["plan_id"] + ".json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(final, f, ensure_ascii=False, indent=1)
    with open(os.path.join(HERE, "out", "id_map_v12_v13.json"), "w", encoding="utf-8") as f:
        json.dump(ids, f, indent=1)
    print("live v%d -> v%d, %d image nodes: %s" % (live_version, version, count, out))
    for source, new in new_ids.items():
        print("  %s -> %s" % (source, new))

    if "assets" in sys.argv[1:]:
        upload_assets(entries, key_dir)


if __name__ == "__main__":
    main()
