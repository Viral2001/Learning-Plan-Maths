# -*- coding: utf-8 -*-
"""Add the two image PLACEHOLDERS every question concept needs (nothing is drawn or rendered here).

    python -I -X utf8 add_question_images.py        (reads and rewrites cbse_eng_maths7_ch10.json in place)

Per question concept, in this media order:   IMG1 question image, VID1 video (if it has one),
                                             IMG2 solution image, IMG3 solution image, continued (long working only)

* IMG1: the question card. It carries a diagram only when the question needs one (the figure sentence is in
  the node description and in the concept's image_decision); it never shows working, answer or hint.
* IMG2: the solution card, numbered working and a highlighted answer.
* IMG3: only when the working is too long for one card: the same card carried on, ending in the answer.
  "Too long" = more than MAX_LINES wrapped lines of working (estimated from the steps in the plan; the final
  authored solution decides at the next stage, when a placeholder can be added or dropped).
Nodes copy core/solutions/attach.node (same fields, same asset folder `solution_image_v1`, same Manim
render_source), with build_status "placeholder" and no PNG or code behind the urls yet.
"""
import io
import json
import math
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
PLAN = os.path.join(HERE, "cbse_eng_maths7_ch10.json")
CONFIG = os.path.join(HERE, "chapter.config.json")
BUCKET_PREFIX = "https://media.singularity-learn.com/learning_plan_assets/"
HINT = re.compile(r"\s*\[Hint:.*?\]", re.S)

MAX_LINES = 8            # wrapped lines of working that one solution card holds
CHARS_PLAIN = 90         # characters per line on a full-width card
CHARS_WITH_FIGURE = 58   # ... on a card that shares the frame with a diagram

KEY = "A key shows a green token as +1 and a red token as -1."
KEY = KEY.replace("-1", "−1")
MACHINE_Q = ("A machine box with three number inputs on the left and one output on the right, with the example "
             "rows of inputs and outputs shown with the question and the output of the last row left blank.")

# concept name -> (question-card diagram or None, solution-card diagram or None).  Question-card text must hold
# nothing but what the question gives (gates/solution_content.py rejects hint-shaped words on it).
FIG = {
    "Rakesh's Puzzle": (None, "A table of guesses with columns first number, second number, sum and difference."),
    "Figure it Out (section 2.1)": (None, None),
    "Carrom Coin Integers, Q1": (
        "A number line with 0 marked, an arrow for the first movement of −4 drawn from 0, and the final "
        "position P = 5 marked; the second movement is left undrawn.",
        "The same number line with the second movement drawn from −4 to 5 and labelled."),
    "Carrom Coin Integers, Q2": (None, "A running total of the ten movements drawn as jumps on a number line."),
    "Carrom Coin Integers, Try This": (
        "Three number-line figures, each with 0, an arrow a from 0, an arrow b from the end of a, and the final "
        "position P marked, with no values written.",
        "The three figures with the direction and size of a and b read off and compared."),
    "End of chapter Figure it Out, Q4": (None, None),
    "Token Bag: 4 × (−6) and 9 × (−7)": (
        "An empty token bag. " + KEY, "Groups of red tokens placed into the bag, 4 times and 9 times."),
    "Figure it Out (multiplication), Q1": (
        KEY, "Token groups placed into or taken out of the bag for each product."),
    "Figure it Out (multiplication), Q2": (None, None),
    "Figure it Out (multiplication), Q3": (
        "Three token sets labelled (a), (b) and (c), each made of green and red tokens. " + KEY,
        "Each token set placed into the bag 4 times, with the tokens counted."),
    "Figure it Out (products)": (None, None),
    "End of chapter Figure it Out, Q3": (None, None),
    "End of chapter Figure it Out, Q12": (None, "The six values placed in order on a number line."),
    "Example 1: Mala's exam marks": (None, None),
    "Example 2: the mine elevator": (
        "A vertical number line for the mine shaft: ground level 0, positions above the ground positive, positions "
        "below the ground negative, and the elevator cage at the top.",
        "The same line with the elevator's end position marked for part (a) and for part (b)."),
    "Figure it Out (division), Q2": (None, None),
    "Figure it Out (division), Q3": (None, None),
    "End of chapter Figure it Out, Q6": (None, None),
    "End of chapter Figure it Out, Q8": (None, None),
    "A Magic Grid of Integers: try again": (
        "The 4 by 4 grid of integers drawn as a table.",
        "The grid with one number circled in each row and each column, and the circled numbers multiplied."),
    "Figure it Out (division), Q1": (None, None),
    "Figure it Out (division), Q4": (None, None),
    "End of chapter Figure it Out, Q2": (None, None),
    "End of chapter Figure it Out, Q11": (None, None),
    "Many Factors: 25 × (−6) × 12 in every order": (None, None),
    "End of chapter Figure it Out, Q1 (b) and (c)": (None, None),
    "End of chapter Figure it Out, Q9": (None, None),
    "Distributive Property: (−2) × (4 + (−3))": (None, None),
    "Distributive Property, Try This: −4 × (2 + (−3))": (
        KEY, "A rectangle of tokens with 4 rows, each row holding the tokens for 2 and for −3, split into two blocks."),
    "End of chapter Figure it Out, Q1 (a)": (None, None),
    "End of chapter Figure it Out, Q13": (None, None),
    "End of chapter Figure it Out, Q14": (None, None),
    "Pick the Pattern: Machine 1": (MACHINE_Q, "The machine box with its rule written on it and the last output filled in."),
    "Pick the Pattern: Machine 2": (MACHINE_Q, "The machine box with its rule written on it and the last output filled in."),
    "End of chapter Figure it Out, Q7": (MACHINE_Q, "The machine box with its rule written on it."),
    "End of chapter Figure it Out, Q5": (
        "The example sequence of the modified Collatz rule drawn as a chain of boxes joined by arrows.",
        "Chains for the starting numbers −21 and −6 drawn the same way."),
    "End of chapter Figure it Out, Q15": (None, None),
    "End of chapter Figure it Out, Q16": (None, None),
    "Pibs: paying +85 with +13 and −9 coins": (None, "Two rows of coins: ten of +13 and five of −9."),
    "End of chapter Figure it Out, Q10": (None, "A table of multiples of 13 and of 9 for the totals asked."),
}


def clean(s):
    return re.sub(r"\s+", " ", HINT.sub("", s or "")).strip()


def stem_of(cov):
    stem = re.sub(r"[^0-9A-Za-z]+", "_", cov).strip("_")
    return "c" + stem if stem[:1].isdigit() else stem


def main():
    plan = json.load(io.open(PLAN, encoding="utf-8"))
    cfg = json.load(io.open(CONFIG, encoding="utf-8"))
    base = cfg["asset_base_template"].format(grade=cfg["grade"], chapter_no=cfg["chapter_no"])
    key_dir = "%s/solution_image_v1" % base[len(BUCKET_PREFIX):].rstrip("/")

    def url(folder, name):
        return "%s%s/%s" % (BUCKET_PREFIX, folder, name)

    def node(cid, n, role, title, desc, scene, part, parts, nname):
        iid = "%s.IMG%d" % (cid, n)
        u = url(key_dir, iid + ".png")
        rs = {"engine": "manim", "scene": scene, "code_url": url(key_dir + "/code", iid + ".py"),
              "style_url": url(key_dir + "/code", "_style.py")}
        if parts > 1:
            rs["part"], rs["parts"] = part, parts
        if role == "question":
            instr = "Try this question yourself before you watch the video."
            notes = "Let the student attempt this before showing the video or the solution image."
        else:
            instr = ("Compare this with your own working, step by step." if part == 1 else
                     "This card carries on from the previous solution card; compare the rest of your working.")
            notes = "Show only after the student has attempted the question."
        return {"id": iid, "type": "image", "subtype": "illustration", "title": title, "image_url": u,
                "planned_url": u, "image_role": role, "render_source": rs, "concept_id": cid,
                "home_concept_id": cid, "related_concept_ids": [], "image_category": "concept",
                "image_dimensions": "1920x1080", "aspect_ratio": "16:9", "build_status": "placeholder",
                "context": "%s image for %s. PLACEHOLDER: specified, not generated yet." % (
                    "Question" if role == "question" else "Solution", nname),
                "description": " ".join(desc.split()), "instructions_for_student": instr, "teaching_notes": notes,
                "labels": [], "regions": [], "tutor_can_highlight": [], "accuracy_constraints": "",
                "generation_prompt": "", "negative_prompt": "",
                "source_image": {"note": "Rendered from Manim code; see render_source."}, "source_image_key": ""}

    report, added = [], 0
    for m in plan["modules"]:
        for s in m["segments"]:
            for t in s["topics"]:
                if t.get("source_type") != "exercise":
                    continue
                old = {x["id"]: x for x in t["media"]}
                media = []
                for c in t["concepts"]:
                    name, cid = c["concept_name"], c["concept_id"]
                    if name not in FIG:
                        raise SystemExit("no figure plan for question concept %r" % name)
                    qfig, sfig = FIG[name]
                    blocks = c["content"]
                    steps = [x for b in blocks for x in (b.get("steps") or []) if isinstance(x, str)]
                    per = CHARS_WITH_FIGURE if sfig else CHARS_PLAIN
                    lines = [max(1, math.ceil(len(x) / per)) for x in steps]
                    split = sum(lines) > MAX_LINES
                    k, run = len(steps), 0
                    if split:
                        for i, ln in enumerate(lines):
                            if run + ln > MAX_LINES and i > 0:
                                k = i
                                break
                            run += ln
                        else:
                            k = max(1, len(steps) // 2)
                        k = min(max(k, 1), len(steps) - 1)
                    qs = []
                    for b in blocks:
                        q = clean(b.get("question"))
                        if q and q not in qs and not re.search(r"\bsame question\b", q):
                            qs.append(q)
                    answers = []
                    for b in blocks:
                        x = clean(b.get("answer"))
                        if x and x not in answers:
                            answers.append(x)
                    answers = [x for x in answers if not any(x != y and x in y for y in answers)]
                    ans = " / ".join(answers)[:220]
                    cov = (c.get("ncert_refs") or [name])[0]
                    stem = stem_of(cov)
                    parts = 2 if split else 1
                    n_q = node(cid, 1, "question", "%s: question" % name,
                               "Question card: %s %s Only the question and its figure are shown." % (
                                   " ".join(qs), qfig if qfig else "No diagram is needed; the question text only."),
                               stem + "_q", 1, 1, name)
                    if split:
                        d2 = ("Solution card, part 1 of 2: numbered working, steps 1 to %d, with the working carried on "
                              "to the next card. %s" % (k, ("Diagram: " + sfig) if sfig else ""))
                        d3 = ("Solution card, part 2 of 2: numbered working, steps %d to %d, and a highlighted answer: %s"
                              % (k + 1, len(steps), ans))
                    else:
                        d2 = "Solution card with numbered working steps and a highlighted answer: %s %s" % (
                            ans, ("Diagram: " + sfig) if sfig else "")
                    n_s = node(cid, 2, "solution", "%s: solution" % name, d2, stem + "_sol", 1, parts, name)
                    nodes = [n_q]
                    ids = [n_q["id"]]
                    vids = [i for i in (c.get("media_ids") or []) if ".VID" in i]
                    for v in vids:
                        nodes.append(old[v])
                        ids.append(v)
                    nodes.append(n_s)
                    ids.append(n_s["id"])
                    sol_ids = [n_s["id"]]
                    if split:
                        n_c = node(cid, 3, "solution", "%s: solution (continued)" % name, d3, stem + "_sol2", 2, 2, name)
                        nodes.append(n_c)
                        ids.append(n_c["id"])
                        sol_ids.append(n_c["id"])
                    media.extend(nodes)
                    added += 2 + (1 if split else 0)
                    c["media_ids"] = ids
                    c["image_decision"] = {
                        "needed": True,
                        "why": "A question concept: one image shows the question%s for the attempt, and %s the worked solution."
                               % (" and its figure" if qfig else "", "two images carry" if split else "one shows"),
                        "question_diagram": qfig, "solution_diagram": sfig,
                        "solution_images": parts, "engine": "manim (LaTeX text)"}
                    for b in blocks:
                        b["image_media_id"] = n_q["id"]
                        b["solution_image_media_id"] = sol_ids[0]
                        if split:
                            b["solution_image_media_ids"] = list(sol_ids)
                        else:
                            b.pop("solution_image_media_ids", None)
                    report.append({"concept_id": cid, "question": name, "question_diagram": bool(qfig),
                                   "solution_diagram": bool(sfig), "steps": len(steps), "est_lines": sum(lines),
                                   "solution_images": parts, "has_video": bool(vids)})
                t["media"] = media
                types = set(t.get("available_content_types") or []) | {"image"}
                t["available_content_types"] = sorted(types)
                t["secondary_content_type"] = "image"

    media_all = [x for mo in plan["modules"] for s in mo["segments"] for t in s["topics"] for x in t.get("media", [])]
    ss = plan["source_metadata"]["summary_stats"]
    ss["images"] = sum(1 for x in media_all if x["type"] == "image")
    ss["question_images"] = sum(1 for r in report)
    ss["solution_images"] = sum(r["solution_images"] for r in report)
    note = plan["source_metadata"].get("media_note", "")
    tag = (" Every question concept also carries a question image and a solution image (a second solution image when "
           "the working is long), specified as placeholders: Manim scenes with LaTeX text, not rendered yet.")
    if tag not in note:
        plan["source_metadata"]["media_note"] = note + tag
    plan["source_metadata"]["restructure"]["question_images"] = {
        "question_images": len(report), "solution_images": ss["solution_images"],
        "with_continuation_image": sum(1 for r in report if r["solution_images"] == 2),
        "with_question_diagram": sum(1 for r in report if r["question_diagram"]),
        "max_lines_per_solution_card": MAX_LINES, "status": "placeholders only"}
    with io.open(PLAN, "w", encoding="utf-8") as f:
        json.dump(plan, f, ensure_ascii=False, indent=1)
    with io.open(os.path.join(HERE, "question_images_report.json"), "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=1)
    print("question concepts: %d | image placeholders added: %d | with continuation: %d | question diagrams: %d" % (
        len(report), added, sum(1 for r in report if r["solution_images"] == 2),
        sum(1 for r in report if r["question_diagram"])))


if __name__ == "__main__":
    main()
