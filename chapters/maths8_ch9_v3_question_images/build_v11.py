"""Restructure the live Phase 3 plan NCERT-wise.

    python build_v11.py     build out/<plan id>.json and check it against the live plan

Every numbered Figure it Out question becomes one concept, with its parts and its video, in the
Questions topic that follows its parent topic. In-text questions and examples stay in teach topics.
Asset urls never change, so ids and urls no longer agree after this. That is normal for this plan.
"""
import copy
import json
import os
import re
import sys

from build_v10 import CHAPTER_ID, fetch_live, leaves, next_version

HERE = os.path.dirname(os.path.abspath(__file__))

# Parent topic -> its questions in book order
QUESTION_TOPICS = {
    "M1.S2.T2": ["2.3.FiO1"],
    "M2.S3.T3": ["end.FiO1"],
    "M2.S4.T4": ["2.3.FiO2", "2.3.FiO3"],
    "M3.S6.T6": ["2.4.FiO3", "end.FiO7"],
    "M3.S8.T8": ["2.4.FiO1", "2.4.FiO2", "2.4.FiO4", "end.FiO2", "end.FiO4"],
    "M3.S10.T10": ["2.5.FiO1", "2.5.FiO2", "2.5.FiO3", "end.FiO5", "end.FiO6"],
    "M4.S13.T13": ["end.FiO3", "end.FiO8", "end.FiO9"],
}
EXISTING_QUESTION_TOPICS = {
    "M2.S4.T4": "M2.S5.T5",
    "M3.S6.T6": "M3.S7.T7",
    "M3.S8.T8": "M3.S9.T9",
    "M3.S10.T10": "M3.S11.T11",
    "M4.S13.T13": "M4.S14.T14",
}

# T3 and T4 were swapped in an old build and these pointers kept the numbering from before the swap
SWAPPED = {
    "M2.S3.T3.C14": "M2.S4.T4.C20", "M2.S3.T3.C15": "M2.S4.T4.C21", "M2.S3.T3.C16": "M2.S4.T4.C22",
    "M2.S3.T3.C17": "M2.S4.T4.C23", "M2.S3.T3.C18": "M2.S4.T4.C24", "M2.S3.T3.C19": "M2.S4.T4.C25",
    "M2.S3.T3.C20": "M2.S4.T4.C26", "M2.S4.T4.C21": "M2.S5.T5.C27", "M2.S5.T5.C22": "M2.S3.T3.C14",
    "M2.S5.T5.C23": "M2.S3.T3.C15", "M2.S5.T5.C24": "M2.S3.T3.C16", "M2.S5.T5.C25": "M2.S3.T3.C17",
    "M2.S5.T5.C26": "M2.S3.T3.C18", "M2.S5.T5.C27": "M2.S3.T3.C19",
}
STALE_TOOL = {"M1.S2.T2.C6.2D1": "M1.S2.T2.C5.2D1"}

ID = re.compile(r"^(M\d+\.S\d+(?:\.T\d+(?:\.C\d+)?)?)(\.(?:VID|IMG|2D|3D|SIM)\d+)?(\.P\d+)?$")


def base_ref(ref):
    """'2.4.FiO4ii' -> '2.4.FiO4', 'end.FiO2a' -> 'end.FiO2'."""
    return re.sub(r"(FiO\d+)[a-z]*$", r"\1", ref)


def topics_of(plan):
    return [t for m in plan["modules"] for s in m["segments"] for t in s["topics"]]


def concepts_of(plan):
    return [c for t in topics_of(plan) for c in t["concepts"]]


def unswap(value):
    m = ID.match(value)
    if not m or m.group(1) not in SWAPPED:
        return value
    return SWAPPED[m.group(1)] + (m.group(2) or "") + (m.group(3) or "")


def repair_pointers(plan):
    """Point every stale reference back at its real node. Node ids are the source of truth."""
    # The question images came after the swap, so their ids are already right
    images = {x["id"] for t in topics_of(plan) for x in t["media"] if x.get("image_role")}
    fix = lambda v: v if v in images else STALE_TOOL.get(v, unswap(v))
    for concept in concepts_of(plan):
        for key in ("media_ids", "video_media_ids"):
            if key in concept:
                concept[key] = [fix(v) for v in concept[key]]
        for key in ("walkthrough_video_id", "tool_media_id", "source_tool_ref"):
            if concept.get(key):
                concept[key] = fix(concept[key])
        for block in concept["content"]:
            if block.get("video_media_id"):
                block["video_media_id"] = fix(block["video_media_id"])
    for topic in topics_of(plan):
        for node in topic["media"]:
            node["related_concept_ids"] = [fix(v) for v in node.get("related_concept_ids", [])]
            for point in node.get("interaction_points", []):
                point["id"] = fix(point["id"])
            walk = node.get("source_video_walkthrough")
            if walk and walk.get("video_id"):
                walk["video_id"] = fix(walk["video_id"])
    for row in plan["video_coverage"]:
        row["video_id"] = fix(row["video_id"])
    meta = plan["source_metadata"]
    for item in meta["misconceptions"]:
        item["bites_in"] = list(dict.fromkeys(fix(v) for v in item["bites_in"]))
    for ref, ids in meta["ncert_coverage"].items():
        meta["ncert_coverage"][ref] = [fix(v) for v in ids]


def collect_questions(plan):
    """Lift every book exercise block, grouped by numbered question, with its video and old concept."""
    groups = {}
    for concept in concepts_of(plan):
        keep = []
        for block in concept["content"]:
            if block.get("item_kind") == "exercise":
                groups.setdefault(base_ref(block["exercise_id"]), []).append(block)
            else:
                keep.append(block)
        concept["content"] = keep
    return groups


def question_label(blocks):
    return re.sub(r"\s*\([a-z]+\)$", "", blocks[0]["book_number"])


def build_concept(key, blocks, video, source, tmp_id):
    """A question concept in the shape of the existing exercise concepts."""
    concept = copy.deepcopy(source)
    concept.update({
        "concept_id": tmp_id,
        "concept_kind": "exercise",
        "concept_name": question_label(blocks),
        "ncert_refs": [b["exercise_id"] for b in blocks],
        "content": blocks,
        "source_segment_role": "practice",
        "video_media_ids": [video["id"]],
        "walkthrough_video_id": video["id"],
        "image_decision": {"needed": False, "why": "A question concept: its video works the question."},
    })
    concept["media_ids"] = [video["id"]]
    return concept


def strip_practice(concept):
    """A Practice concept keeps its recap and tool. Its book question has left."""
    tool = concept.get("tool_media_id")
    concept["ncert_refs"] = [r for r in concept["ncert_refs"] if "FiO" not in r]
    concept["video_media_ids"] = []
    concept["walkthrough_video_id"] = None
    concept["image_decision"] = {"needed": False,
                                 "why": "A practice concept: the tool is the visual, so a still image would add nothing."}
    concept["media_ids"] = [m for m in concept["media_ids"] if ".VID" not in m]
    if tool and tool not in concept["media_ids"]:
        concept["media_ids"].append(tool)


def restructure(plan):
    groups = collect_questions(plan)
    planned = [k for keys in QUESTION_TOPICS.values() for k in keys]
    if sorted(planned) != sorted(groups):
        raise SystemExit("Book questions differ: %s" % sorted(set(planned) ^ set(groups)))

    topics = {t["topic_id"]: t for t in topics_of(plan)}
    concepts = {c["concept_id"]: c for c in concepts_of(plan)}
    videos = {}
    for topic in topics_of(plan):
        for node in topic["media"]:
            if node["type"] == "video" and node.get("video_role") == "exercise":
                videos[base_ref(node["serves_items"][0])] = (topic, node)
    if sorted(videos) != sorted(groups):
        raise SystemExit("Question videos differ: %s" % sorted(set(videos) ^ set(groups)))

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

    built = {}
    for key, blocks in groups.items():
        topic, video = videos[key]
        owner = concepts[video["concept_id"]]
        blocks.sort(key=lambda b: b["exercise_id"])
        if owner.get("concept_kind") == "exercise":
            owner["concept_name"] = question_label(blocks)
            owner["ncert_refs"] = [b["exercise_id"] for b in blocks]
            owner["content"] = blocks
            built[key] = owner
        else:
            tmp = "TMP." + key
            built[key] = build_concept(key, blocks, video, owner, tmp)
            strip_practice(owner)
            video["concept_id"] = video["home_concept_id"] = tmp
            add_to_anchors(plan["objectives"], owner["concept_id"], tmp)
            for t in topics_of(plan):
                add_to_anchors(t["learning_objectives"], owner["concept_id"], tmp)
        for block in blocks:
            block["video_media_id"] = video["id"]

    # Keep the ROMAN order of parts, which a plain sort gets wrong
    roman = ["i", "ii", "iii", "iv", "v"]
    for key, concept in built.items():
        parts = concept["content"]
        if len(parts) > 1 and key != "end.FiO2":
            suffix = lambda b: b["exercise_id"][len(key):]
            parts.sort(key=lambda b: roman.index(suffix(b)))
            concept["ncert_refs"] = [b["exercise_id"] for b in parts]

    for parent_id, keys in QUESTION_TOPICS.items():
        qt_id = EXISTING_QUESTION_TOPICS.get(parent_id)
        if qt_id:
            topic = topics[qt_id]
        else:
            topic = add_question_topic(plan, parent_id)
        move_videos(topics, topic, keys, built, videos)
        topic["concepts"] = [built[k] for k in keys]
    set_ncert_coverage(plan, built)
    return built


def add_question_topic(plan, parent_id):
    """A new segment and topic after the parent, in the shape the other Questions topics have."""
    for module in plan["modules"]:
        for i, segment in enumerate(module["segments"]):
            if segment["topics"][0]["topic_id"] != parent_id:
                continue
            new_segment = copy.deepcopy(segment)
            name = "Questions: " + segment["topics"][0]["topic_name"]
            new_segment["segment_id"] = "TMP." + segment["segment_id"]
            new_segment["segment_name"] = name
            topic = new_segment["topics"][0]
            topic.update({"topic_id": "TMP." + parent_id, "topic_name": name, "media": [], "concepts": [],
                          "summary": "", "brief_summary": "", "detailed_summary": "",
                          "key_terms": [], "concept_bullets": []})
            new_segment["summary"] = new_segment["brief_summary"] = ""
            module["segments"].insert(i + 1, new_segment)
            return topic
    raise SystemExit("Parent topic not found: %s" % parent_id)


def move_videos(topics, topic, keys, built, videos):
    media = []
    for key in keys:
        source, video = videos[key]
        if source is not topic:
            source["media"].remove(video)
        else:
            topic["media"].remove(video)
        media.append(video)
    topic["media"] = media + topic["media"]


def set_ncert_coverage(plan, built):
    coverage = plan["source_metadata"]["ncert_coverage"]
    for concept in built.values():
        for ref in concept["ncert_refs"]:
            coverage[ref] = [concept["concept_id"]]


def renumber(plan):
    """Contiguous segment, topic and concept numbers, with every reference rewritten in one pass."""
    ids = {}
    seg_no = topic_no = concept_no = 0
    for m_no, module in enumerate(plan["modules"], 1):
        for segment in module["segments"]:
            seg_no += 1
            seg = "M%d.S%d" % (m_no, seg_no)
            ids[segment["segment_id"]] = seg
            for topic in segment["topics"]:
                topic_no += 1
                tid = "%s.T%d" % (seg, topic_no)
                ids[topic["topic_id"]] = tid
                for concept in topic["concepts"]:
                    concept_no += 1
                    ids[concept["concept_id"]] = "%s.C%d" % (tid, concept_no)
    media = {}
    for topic in topics_of(plan):
        for node in topic["media"]:
            old = ID.match(node["id"])
            media[node["id"]] = ids[node["concept_id"]] + old.group(2)
    ids.update(media)

    def rewrite(value):
        if isinstance(value, dict):
            return {k: rewrite(v) for k, v in value.items()}
        if isinstance(value, list):
            return [rewrite(v) for v in value]
        if isinstance(value, str):
            if value in ids:
                return ids[value]
            m = ID.match(value)
            if m and m.group(3) and m.group(1) + m.group(2) in ids:
                return ids[m.group(1) + m.group(2)] + m.group(3)
            if m or value.startswith("TMP."):
                raise SystemExit("Unknown id: %s" % value)
        return value

    return rewrite(plan), ids


def order_media_ids(plan):
    """Question image, video, solution image: the attempt comes first."""
    for concept in concepts_of(plan):
        if concept.get("concept_kind") != "exercise":
            continue
        ordered = sorted(concept["media_ids"], key=lambda m: ("IMG1" not in m, "VID" not in m))
        concept["media_ids"] = ordered


def check(live, plan, questions=19):
    concepts, topics = concepts_of(plan), topics_of(plan)
    nodes = {x["id"]: x for t in topics for x in t["media"]}
    if len(nodes) != sum(len(t["media"]) for t in topics):
        raise SystemExit("Duplicate media ids")

    exercises = [c for c in concepts if c.get("concept_kind") == "exercise"]
    if len(exercises) != questions:
        raise SystemExit("Expected %d question concepts, got %d" % (questions, len(exercises)))
    refs = [r for c in concepts for r in c["ncert_refs"] if "FiO" in r]
    want = sorted(r for c in concepts_of(live) for r in c["ncert_refs"] if "FiO" in r)
    if sorted(refs) != want or len(set(refs)) != len(refs):
        raise SystemExit("Book refs are lost or repeated")

    for topic in topics:
        questions = topic["topic_name"].startswith("Questions:")
        for concept in topic["concepts"]:
            cid = concept["concept_id"]
            own = {x["id"] for x in topic["media"] if x["concept_id"] == cid}
            is_exercise = concept.get("concept_kind") == "exercise"
            if is_exercise != questions:
                raise SystemExit("Concept in the wrong topic: %s" % cid)
            if not set(m for m in own).issubset(concept["media_ids"]) or \
                    not set(concept["media_ids"]).issubset(nodes):
                raise SystemExit("Pointers wrong: %s %s %s" % (cid, sorted(own), concept["media_ids"]))
            if not set(concept["media_ids"]) - own <= {concept.get("tool_media_id")}:
                raise SystemExit("Foreign media: %s" % cid)
            if concept.get("video_media_ids", []) != [m for m in concept["media_ids"] if ".VID" in m]:
                raise SystemExit("Video list wrong: %s" % cid)
            for block in concept["content"]:
                if block.get("video_media_id") and block["video_media_id"] not in concept["media_ids"]:
                    raise SystemExit("Block video wrong: %s" % cid)
                if block.get("item_kind") == "exercise" and not is_exercise:
                    raise SystemExit("Book question left in teach topic: %s" % cid)
            if is_exercise and len(concept["video_media_ids"]) != 1:
                raise SystemExit("Question without one video: %s" % cid)
        for node in topic["media"]:
            if not node["id"].startswith(topic["topic_id"] + "."):
                raise SystemExit("Node in the wrong topic: %s" % node["id"])
            walk = node.get("source_video_walkthrough")
            if walk and walk.get("video_id") != node["id"]:
                raise SystemExit("Walkthrough wrong: %s" % node["id"])
            for point in node.get("interaction_points", []):
                if not point["id"].startswith(node["id"] + "."):
                    raise SystemExit("Interaction id wrong: %s" % point["id"])

    owners = {r: c for c in concepts for r in c["ncert_refs"]}
    for row in plan["video_coverage"]:
        if row["item_id"] not in nodes.get(row["video_id"], {}).get("serves_items", []):
            raise SystemExit("Coverage video wrong: %s" % row["item_id"])
        if "FiO" in row["item_id"] and row["video_id"] not in owners[row["item_id"]]["media_ids"]:
            raise SystemExit("Coverage wrong: %s" % row["item_id"])

    # Asset urls and every plain text value must survive; only ids and listed fields may change
    def values(p, pat):
        return sorted(v for k, v in leaves(p) if isinstance(v, str) and pat.search(k))
    urls = re.compile(r"(_url|2d_tool_json)$")
    if values(live, urls) != values(plan, urls):
        raise SystemExit("Asset urls changed")
    text = re.compile(r"/(text|publication_text|question|answer|title|description|video_script/.*)$")
    if values(live, text) != values(plan, text):
        raise SystemExit("Text changed")
    if sorted(b.get("exercise_id", "") for c in concepts_of(live) for b in c["content"]) != \
            sorted(b.get("exercise_id", "") for c in concepts for b in c["content"]):
        raise SystemExit("Blocks lost")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    live, live_version = fetch_live()
    version = next_version()
    plan = copy.deepcopy(live)
    repair_pointers(plan)
    restructure(plan)
    plan, ids = renumber(plan)
    order_media_ids(plan)
    plan["version"] = version
    plan["plan_id"] = "%s_v%d" % (CHAPTER_ID, version)
    check(live, plan)
    out = os.path.join(HERE, "out", plan["plan_id"] + ".json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(plan, f, ensure_ascii=False, indent=1)
    with open(os.path.join(HERE, "out", "id_map_v10_v11.json"), "w", encoding="utf-8") as f:
        json.dump(ids, f, indent=1)
    print("live v%d -> v%d: %s" % (live_version, version, out))
    for topic in topics_of(plan):
        print(topic["topic_id"], topic["topic_name"])
        for c in topic["concepts"]:
            if c.get("concept_kind") == "exercise":
                print("    %s %s %s" % (c["concept_id"].rsplit(".", 1)[1], c["concept_name"], len(c["content"])))


if __name__ == "__main__":
    main()
