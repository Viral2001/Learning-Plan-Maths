# -*- coding: utf-8 -*-
"""Synthetic map for a prepared chapter: EVERY item required (ids = lowest free per concept), written to map/diagram_map.json, then
rollout.build(). Used only to test the builder/renumbering on a chapter before the real agents' maps exist. Removes its output."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rollout as R
c, n = int(sys.argv[1]), int(sys.argv[2])
H = R.here(c, n)
inv = json.load(open(os.path.join(H, "map", "inventory.json"), encoding="utf-8"))
used = {}
def free(cid, kept):
    k = 1
    while "%s.IMG%d" % (cid, k) in kept or "%s.IMG%d" % (cid, k) in used.get(cid, set()):
        k += 1
    used.setdefault(cid, set()).add("%s.IMG%d" % (cid, k))
    return "%s.IMG%d" % (cid, k)
def diag(d=None):
    return {"diagram_type": "other", "aspect_ratio": "16:9", "derived_from": d, "content": {"type": "other"},
            "manim_description": "Draw a square 4 units wide, outline INK.", "visible_text": ["A"], "must_not_show": ["x"], "accuracy_checks": ["a"], "alt_text": "A square."}
def item(cid, role, mid, act, ins, pos, bi=None, d=None):
    x = {"lp_concept_id": cid, "role": role, "decision": "required", "reason_codes": ["DATA_IN_FIGURE"], "reason": "t", "lp_placeholder_action": act,
         "media_id": mid, "manim_scene": "s" + mid, "placeholder": {"token": "{{DIAGRAM:%s}}" % mid, "insert_into": ins, "position": pos}, "diagram": diag(d)}
    if bi is not None:
        x["block_index"] = bi
    return x
items = []
for u in inv:
    if u["kind"] == "pair":
        q, a = u["question_concept"], u["answer_concept"]
        qi = free(q["concept_id"], set(q["kept_image_ids"])); ai = free(a["concept_id"], set(a["kept_image_ids"]))
        items += [item(q["concept_id"], "question", qi, "keep_and_replace_spec", "question_tex", "after_question_text"),
                  item(a["concept_id"], "solution", ai, "keep_and_replace_spec", "steps_tex", "before_first_step", d=qi)]
    elif u["kind"] == "single":
        cid = u["concept_id"]; kept = set(u["kept_image_ids"])
        qi = free(cid, kept); si = free(cid, kept)
        items += [item(cid, "question", qi, "keep_and_replace_spec", "question_tex", "after_question_text", u["block_index"]),
                  item(cid, "solution", si, "keep_and_replace_spec", "steps_tex", "before_first_step", u["block_index"], d=qi)]
    else:
        cid = u["concept_id"]
        items.append(item(cid, "worked_example", free(cid, set(u["kept_image_ids"])), "add_new_image", "question_tex", "after_question_text", u["block_index"]))
json.dump({"meta": {"chapter": "x"}, "items": items}, open(os.path.join(H, "map", "diagram_map.json"), "w", encoding="utf-8"))
plan = R.build(c, n)
meta = json.load(open(os.path.join(H, "meta.json"), encoding="utf-8"))
os.remove(os.path.join(H, "out", plan["plan_id"] + ".json"))
os.remove(os.path.join(H, "map", "diagram_map.json"))
print("selftest ok; synthetic output removed")
