# -*- coding: utf-8 -*-
"""Part 1 + Part 2 of docs/karan-MD/LEARNING_PLAN_FIELD_CLEANUP_AND_LATEX 1.md, applied to an ALREADY-LIVE
Class 6-8 plan (the question-layout shape: a "Questions: <topic>" topic after each concept topic, one concept per
printed question holding question + steps + answer + its images and video in ONE concept).

    python -B -X utf8 core/qa_split_live.py --key maths7_ch10 --src <live plan.json>  [--out DIR]

What it does, in this order (each step is the guide's, section numbers in brackets):
  0. tool descriptions: chapters/<key>/lp_qa_latex/tool_descriptions.py, if present, are written onto the 2d_tool nodes
     (keyed by the tool's id in the SOURCE plan; renumbering carries them along).
  1. Part 1 field cleanup (core/field_cleanup.py).
  2. every question concept of every "Questions:" topic becomes a QUESTION concept (qt_part "question": the question
     card only) + an ANSWER concept (qt_part "answer": the video and the solution card(s)) [Part 2, section 4];
     the questions of one teaching topic are grouped by category into "Questions: <category>" topics
     (core/question_naming.py) [section 3]; every Q/A block's displayed text is strict inline LaTeX
     (core/solutions/latex_convert.py, with question_tex / steps_tex / answer_tex beside it) [section 7].
  3. one global renumbering of topic / segment / concept / media ids [section 5]. URLs are NEVER touched: every
     planned_url / image_url / video_url / 2d_tool_url / code_url stays exactly as it is, so a file already made or
     reserved under it is still found. Image ids are numbered IMG1.. down each concept (what the LP2 upload
     endpoint expects, see chapters/maths5_ch1/new_design/server_ids.py).
  4. ncert_coverage points at both the question and the answer concept; objectives anchored only to a replaced
     question concept are dropped and the rest renumbered gap-free [section 6].
  5. checks: structure, latex_checker, answer_checker (gaps), the gate families, before/after.

Hand fixes live in chapters/<key>/lp_qa_latex/edits.json so a run can always be repeated from the source plan:
    {"<old concept id>#<question block index>": {"question": "...", "steps": ["..."], "answer": "..."}}
(a missing solution for a question that has none, or a LaTeX-friendlier wording of one that converts badly).
"""
from __future__ import annotations

import argparse
import copy
import io
import json
import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(_HERE)
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from core import field_cleanup                              # noqa: E402
from core import question_naming as QN                      # noqa: E402
from core.solutions import latex_convert as LC              # noqa: E402
from core.solutions import latex_house as LH                # noqa: E402

QT_TYPES = ("exercise", "question_topic")
QUESTION_KINDS = ("exercise", "exercise_question")
TOKEN = re.compile(r"(?<![/\w])\bM\d+\.S\d+\.T\d+(?:\.C\d+(?:\.[A-Za-z0-9]+)?)?")
MEDIA_ID = re.compile(r"^(M\d+\.S\d+\.T\d+\.C\d+)\.(.+)$")
TOOL_LINK_KEYS = ("related_concept_ids", "reused_in_topics", "reused_in_concepts")
Q_ONLY_EXTRAS = ("q_figure", "related_tool", "book_icon", "starred", "question_type")
COMMON_FIELDS = ("block_kind", "item_kind", "book_kind", "coverage_id", "exercise_id", "ncert_refs", "book_number",
                 "example_id")
DROP_FROM_ANSWER = ("text", "publication_text", "image_media_id", "video_media_id", "solution_image_media_id",
                    "solution_image_media_ids", "question_tex", "steps_tex", "answer_tex") + Q_ONLY_EXTRAS
BUCKET = "https://media.singularity-learn.com/"


# ------------------------------------------------------------------------------------------------ small helpers
def topics_of(plan):
    return [t for m in plan["modules"] for s in m["segments"] for t in s["topics"]]


def is_qt(t):
    return t.get("source_type") in QT_TYPES or (t.get("topic_name") or "").startswith("Questions:")


def is_qblock(b):
    return isinstance(b, dict) and (b.get("block_kind") in QUESTION_KINDS
                                    or (b.get("block_kind") == "worked_example" and bool(b.get("item_kind"))))


def qblocks(c):
    return [b for b in c.get("content") or [] if is_qblock(b)]


def section_no(cov):
    return QN._section_no(cov)


def cov_of(b):
    return b.get("coverage_id") or next(iter(b.get("ncert_refs") or []), None)


# ------------------------------------------------------------------------------------------------ classification
_EX_NUM_LABEL = re.compile(r"^\s*Example\s*(\d+)\b\s*[:.\-]?\s*(.*)$", re.I)
_EX_NUM_COV = re.compile(r"(?:^|[._])[Ee]x(?:ample)?(\d+)\b")


def classify_unit(blocks, parent_name, example_seq):
    """(category, topic_suffix, concept_prefix, canonical label maker) for one question concept, from its first
    block. The live labels (book_number) are free text written by hand, so this works from item_kind, the book
    label and the coverage id; anything it does not recognise falls in the 'other' category named after the
    teaching topic (the guide, section 3), which keeps today's "Questions: <topic>" name."""
    b = blocks[0]
    label = (b.get("book_number") or "").strip()
    low = label.lower()
    kind = b.get("item_kind")
    cov = cov_of(b)
    if kind == "figure_it_out" or "figure it out" in low:
        sec = section_no(cov)
        suffix = "Figure it Out %s" % sec if sec else "Figure it Out"
        return "figure_it_out", suffix, "Figure it out", None
    m = QN._EXERCISE_RE.match(label)
    if m:
        name = "Exercise Set %s" % m.group(1)
        return "exercise", name, name, m.group(1)
    if kind == "example" or b.get("book_kind") == "example" or _EX_NUM_LABEL.match(label):
        n = None
        mm = _EX_NUM_LABEL.match(label)
        if mm:
            n = mm.group(1)
        if n is None:
            mc = _EX_NUM_COV.search(cov or "")
            if mc:
                n = mc.group(1)
        if n is None:
            n = str(example_seq)
        return "example", "Example", "Example %s" % n, n
    if QN._LET_US_DO_RE.match(label):
        return "let_us_do", "Let us do", "Let us do", None
    return "other", parent_name, parent_name, None


def canonical_label(category, suffix, seq, example_n, old_label):
    """The book_number written on a Q/A block so that core/question_naming.classify() (which gates/question_layout.py
    runs over the first block of a Questions topic) lands on the category this block was given."""
    if category == "figure_it_out":
        sec = suffix[len("Figure it Out"):].strip()
        return "Figure it Out %s, Q%d" % (sec, seq) if sec else "Figure it Out, Q%d" % seq
    if category == "exercise":
        return "%s, Q%d" % (suffix.replace("Exercise Set", "Exercise"), seq)
    if category == "example":
        title = _EX_NUM_LABEL.sub(lambda m: m.group(2), old_label or "").strip()
        return "Example %s: %s" % (example_n, title) if title else "Example %s" % example_n
    if category == "let_us_do":
        return "Let us do, Q%d" % seq
    return old_label or ("%s, Q%d" % (suffix, seq))


# ------------------------------------------------------------------------------------------------ LaTeX
def tex_fields(question, steps, answer, phrases=None):
    """(question_tex, steps_tex, answer_tex, text): text is the numbered working + 'Answer:' converted in ONE
    latex_wrap pass (the step index becomes its own $N$ span); steps_tex / answer_tex are the same lines with the
    index and the 'Answer: ' label taken off, so the concept text visibly contains them (gates/solution_content.py).
    The strings go through core/solutions/latex_house.py first (part labels, blanks)."""
    H = lambda x: LH.house(x, phrases)                                   # noqa: E731
    fb = LH.fix_blanks
    qtex = fb(LC.latex_wrap(H(question))) if question else ""
    steps = [H(s) for s in steps if isinstance(s, str) and s.strip()]
    answer = H((answer or "").strip())
    if not steps and not answer:
        return qtex, [], "", ""
    whole = LC.wrap_steps_and_answer(steps, answer)
    lines = whole.split("\n")
    want = len(steps) + (1 if answer else 0)
    steps_tex, answer_tex = [], ""
    ok = len(lines) == want
    if ok:
        for i, line in enumerate(lines[:len(steps)], 1):
            pre = "$%d$. " % i
            if not line.startswith(pre):
                ok = False
                break
            steps_tex.append(line[len(pre):])
        if ok and answer:
            if not lines[-1].startswith("Answer: "):
                ok = False
            else:
                answer_tex = lines[-1][len("Answer: "):]
    if not ok:                                    # a step holding a newline, or an unexpected shape: per-step
        steps_tex = [LC.latex_wrap(s) for s in steps]
        answer_tex = LC.latex_wrap(answer)
        lines = ["$%d$. %s" % (i, s) for i, s in enumerate(steps_tex, 1)]
        if answer_tex:
            lines.append("Answer: %s" % answer_tex)
        whole = "\n".join(lines)
    steps_tex = [fb(x) for x in steps_tex]
    return qtex, steps_tex, fb(answer_tex), fb(whole)


# ------------------------------------------------------------------------------------------------ the transform
class Transform:
    def __init__(self, src, key, descriptions=None, edits=None):
        self.src = src
        self.key = key
        self.descriptions = descriptions or {}
        self.edits = edits or {}
        self.report = {"key": key, "notes": [], "gaps": [], "multi_block_units": [], "passthrough": [],
                       "foreign_media": [], "dropped_objectives": [], "unnumbered_check": [], "categories": {},
                       "label_canonicalised": 0}

    def note(self, msg):
        self.report["notes"].append(msg)

    # ----------------------------------------------------------------------------------------------- run
    def run(self):
        plan = copy.deepcopy(self.src)
        self.apply_descriptions(plan)
        self.report["cleanup"] = field_cleanup.clean(plan, "6_8")
        self.plan = plan
        self.index_media()
        entries = self.layout()
        self.assign_ids(entries)
        new = self.build(entries)
        self.finish(new)
        return new

    # ----------------------------------------------------------------------------------------------- step 0
    def apply_descriptions(self, plan):
        applied, missing = 0, []
        seen = set()
        for t in topics_of(plan):
            for md in t.get("media") or []:
                if md.get("type") != "2d_tool":
                    continue
                d = self.descriptions.get(md["id"])
                if d:
                    md["description"] = d
                    applied += 1
                    seen.add(md["id"])
                else:
                    missing.append(md["id"])
        extra = sorted(set(self.descriptions) - seen)
        self.report["tool_descriptions"] = {"applied": applied, "tools_without": missing, "unknown_keys": extra}

    # ----------------------------------------------------------------------------------------------- media index
    def index_media(self):
        self.node = {}                 # old media id -> node
        self.node_topic = {}           # old media id -> topic
        self.by_concept = {}           # old concept id -> [old media ids] in file order
        for t in topics_of(self.plan):
            for md in t.get("media") or []:
                self.node[md["id"]] = md
                self.node_topic[md["id"]] = t
                self.by_concept.setdefault(md.get("concept_id"), []).append(md["id"])

    # ----------------------------------------------------------------------------------------------- layout
    def layout(self):
        """Entries in document order: ("topic", mid, seg, topic) for a kept topic, ("run", mid, [segs], [topics])
        for a run of consecutive Questions topics inside one module."""
        entries = []
        for m in self.plan["modules"]:
            run = None
            for seg in m["segments"]:
                for t in seg["topics"]:
                    if is_qt(t):
                        if run is None:
                            run = ["run", m["module_id"], [], []]
                            entries.append(run)
                        run[2].append(seg)
                        run[3].append(t)
                    else:
                        run = None
                        entries.append(["topic", m["module_id"], seg, t])
        return entries

    # ----------------------------------------------------------------------------------------------- ids
    def assign_ids(self, entries):
        self.tid_map, self.cid_map, self.media_map = {}, {}, {}
        self.split_old = set()
        self.units_by_old = {}
        self.A2Q = {}
        T = C = 0
        parent_name = None
        for e in entries:
            mid = e[1]
            if e[0] == "topic":
                T += 1
                t = e[3]
                new_tid = "%s.S%d.T%d" % (mid, T, T)
                self.tid_map[t["topic_id"]] = new_tid
                e.append(new_tid)
                for c in t["concepts"]:
                    C += 1
                    self.cid_map[c["concept_id"]] = "%s.C%d" % (new_tid, C)
                parent_name = t["topic_name"]
                continue
            # a run of Questions topics: group its concepts into category topics
            units = []
            example_seq = 0
            for t in e[3]:
                for c in t["concepts"]:
                    bl = qblocks(c)
                    if not bl:
                        units.append({"c": c, "t": t, "cls": None, "blocks": bl})
                        continue
                    cat, suffix, prefix, n = classify_unit(bl, parent_name or "Questions", example_seq + 1)
                    if cat == "example":
                        example_seq += 1
                    # a stub (a question block with no question text at all, left by the layout rollout) is grouped by
                    # its label but NOT split: there is nothing to put on a question card or to solve
                    stub = not (bl[0].get("question") or "").strip()
                    units.append({"c": c, "t": t, "cls": (cat, suffix, prefix, n), "blocks": bl, "stub": stub})
            groups, order = {}, []
            last_key = None
            for u in units:
                if u["cls"] is None:                       # no question block at all: stays with the group before it
                    key = last_key or ("other", parent_name or "Questions")
                else:
                    key = (u["cls"][0], u["cls"][1])
                if u["cls"] is None or u.get("stub"):
                    u["passthrough"] = True
                    self.report["passthrough"].append(u["c"]["concept_id"])
                last_key = key
                if key not in groups:
                    groups[key] = []
                    order.append(key)
                groups[key].append(u)
            specs = []
            for key in order:
                T += 1
                new_tid = "%s.S%d.T%d" % (mid, T, T)
                spec = {"cat": key[0], "suffix": key[1], "tid": new_tid, "units": groups[key]}
                seq = 0
                for u in groups[key]:
                    if u.get("passthrough"):
                        C += 1
                        u["pcid"] = "%s.C%d" % (new_tid, C)
                        self.cid_map[u["c"]["concept_id"]] = u["pcid"]
                        continue
                    seq += 1
                    u["seq"] = seq
                    C += 1
                    u["qcid"] = "%s.C%d" % (new_tid, C)
                    C += 1
                    u["acid"] = "%s.C%d" % (new_tid, C)
                    oc = u["c"]["concept_id"]
                    self.split_old.add(oc)
                    self.cid_map[oc] = u["acid"]
                    self.units_by_old[oc] = u
                    self.A2Q[u["acid"]] = u["qcid"]
                    self.assign_media(u)
                specs.append(spec)
                self.report["categories"][key[0]] = self.report["categories"].get(key[0], 0) + len(groups[key])
            for t in e[3]:
                self.tid_map[t["topic_id"]] = specs[0]["tid"]
            e.append(specs)
        # media of every kept concept follows its concept
        for oid, md in self.node.items():
            if oid in self.media_map:
                continue
            oc = md.get("concept_id")
            if oc in self.cid_map and oc not in self.split_old:
                mm = MEDIA_ID.match(oid)
                suffix = mm.group(2) if mm else None
                if suffix:
                    self.media_map[oid] = "%s.%s" % (self.cid_map[oc], suffix)

    def assign_media(self, u):
        oc = u["c"]["concept_id"]
        owned = [self.node[i] for i in self.by_concept.get(oc, [])]
        q_imgs = [n for n in owned if n.get("type") == "image" and n.get("image_role") == "question"]
        a_vids = [n for n in owned if n.get("type") == "video"]
        a_imgs = [n for n in owned if n.get("type") == "image" and n.get("image_role") != "question"]
        others = [n for n in owned if n.get("type") not in ("image", "video")]
        u["q_nodes"], u["a_vids"], u["a_imgs"], u["a_other"] = q_imgs, a_vids, a_imgs, others
        for k, n in enumerate(q_imgs, 1):
            self.media_map[n["id"]] = "%s.IMG%d" % (u["qcid"], k)
        for k, n in enumerate(a_vids, 1):
            self.media_map[n["id"]] = "%s.VID%d" % (u["acid"], k)
        for k, n in enumerate(a_imgs, 1):
            self.media_map[n["id"]] = "%s.IMG%d" % (u["acid"], k)
            if n.get("image_role") != "solution":
                self.note("%s: image %s has role %r in the source, set to 'solution'" % (oc, n["id"], n.get("image_role")))
        for n in others:
            mm = MEDIA_ID.match(n["id"])
            self.media_map[n["id"]] = "%s.%s" % (u["acid"], mm.group(2) if mm else n["id"])
            self.note("%s: %s node %s owned by a question concept, moved to its answer concept"
                      % (oc, n.get("type"), n["id"]))
        for i in u["c"].get("media_ids") or []:
            if i in self.node and self.node[i].get("concept_id") != oc:
                self.report["foreign_media"].append("%s -> %s (owned by %s)" % (oc, i, self.node[i].get("concept_id")))

    # ----------------------------------------------------------------------------------------------- rewrite
    def rw(self, o):
        """Deep copy of `o` with every old topic / concept / media token replaced by its new id. Strings that are urls
        and tokens that sit inside a url are left alone (urls never change)."""
        tm, cm, mm = self.tid_map, self.cid_map, self.media_map

        def sub(m):
            tok = m.group(0)
            return mm.get(tok) or cm.get(tok) or tm.get(tok) or tok

        def walk(x):
            if isinstance(x, dict):
                tool = x.get("type") == "2d_tool"
                return {k: (copy.deepcopy(v) if (tool and k in TOOL_LINK_KEYS) else walk(v)) for k, v in x.items()}
            if isinstance(x, list):
                return [walk(v) for v in x]
            if isinstance(x, str):
                if x.startswith("http"):
                    return x
                return TOKEN.sub(sub, x)
            return x
        return walk(o)

    # ----------------------------------------------------------------------------------------------- build
    def build(self, entries):
        src = self.src
        new = {k: copy.deepcopy(v) for k, v in self.plan.items() if k not in ("modules", "objectives",
                                                                                "source_metadata", "video_coverage",
                                                                                "strand_to_objective_map")}
        modules = []
        for m in self.plan["modules"]:
            mm = {k: copy.deepcopy(v) for k, v in m.items() if k != "segments"}
            mm["segments"] = []
            modules.append(mm)
        mod_by = {m["module_id"]: m for m in modules}
        seg_template = None
        prev_tid = None
        for e in entries:
            mid = e[1]
            if e[0] == "topic":
                seg, t = e[2], e[3]
                new_tid = e[4]
                nt = self.rw(t)
                nt["topic_id"] = new_tid
                nt["depends_on"] = [prev_tid] if prev_tid else []
                ns = {k: copy.deepcopy(v) for k, v in seg.items() if k != "topics"}
                ns["segment_id"] = new_tid.rsplit(".T", 1)[0]
                ns["topics"] = [nt]
                mod_by[mid]["segments"].append(ns)
                prev_tid = new_tid
                seg_template = seg_template or seg
                continue
            specs = e[4]
            for spec in specs:
                nt = self.build_q_topic(e, spec)
                nt["depends_on"] = [prev_tid] if prev_tid else []
                tpl = e[2][0]
                ns = {k: copy.deepcopy(v) for k, v in tpl.items() if k != "topics"}
                ns["segment_id"] = spec["tid"].rsplit(".T", 1)[0]
                ns["segment_name"] = nt["topic_name"]
                ns["summary"] = ns["brief_summary"] = ns["detailed_summary"] = nt["summary"]
                ns["segment_objective_ids"] = []
                ns["topics"] = [nt]
                mod_by[mid]["segments"].append(ns)
                prev_tid = spec["tid"]
        new["modules"] = modules
        # root parts that carry ids
        new["video_coverage"] = self.rw(self.plan.get("video_coverage", []))
        new["source_metadata"] = self.rw(self.plan.get("source_metadata", {}))
        self.new_objectives(new)
        self.fix_tool_links(new)
        self.fix_coverage(new)
        return new

    # ---- a "Questions: <category>" topic
    def build_q_topic(self, e, spec):
        run_topics = e[3]
        tpl = copy.deepcopy(run_topics[0])
        suffix = spec["suffix"]
        concepts, media = [], []
        for u in spec["units"]:
            if u.get("passthrough"):
                c = self.rw(u["c"])
                c["concept_id"] = u["pcid"]
                if u.get("cls"):                       # a stub: grouped by its label, so the label must say so
                    cat, sfx, _p, n = u["cls"]
                    for b in c["content"]:
                        if is_qblock(b):
                            b["book_number"] = canonical_label(cat, sfx, 1, n, b.get("book_number"))
                concepts.append(c)
                for oid in self.by_concept.get(u["c"]["concept_id"], []):
                    n = self.rw(self.node[oid])
                    n["concept_id"] = n["home_concept_id"] = u["pcid"]
                    media.append(n)
                continue
            q, a, nodes = self.build_pair(u)
            concepts.extend([q, a])
            media.extend(nodes)
        types = []
        for n in media:
            if n.get("type") not in types:
                types.append(n.get("type"))
        order = [t for t in ("image", "video", "2d_tool", "3d_tool") if t in types]
        nt = {k: v for k, v in tpl.items() if k not in ("concepts", "media")}
        nt.update({
            "topic_id": spec["tid"], "topic_name": QN.topic_title(suffix), "topic_type": "instructional",
            "summary": "Practise: %s." % suffix, "brief_summary": "Practise: %s." % suffix,
            "detailed_summary": "Practise: %s." % suffix, "original_chunk": "Practise: %s." % suffix,
            "publication_chunk": "Practise: %s." % suffix, "concept_bullets": [c["concept_name"] for c in concepts],
            "topic_objective": None, "objective_ids": [], "learning_objectives": [], "is_enrichment": True,
            "topic_category": "enrichment", "source_type": self.q_source_type(tpl),
            "available_content_types": order,
            "primary_content_type": order[0] if order else None,
            "secondary_content_type": order[1] if len(order) > 1 else None,
            "tertiary_content_type": order[2] if len(order) > 2 else None,
            "concepts": concepts, "media": media,
        })
        return nt

    @staticmethod
    def q_source_type(tpl):
        """A Questions topic is typed "exercise" (or "question_topic"). A summary-typed one (the layout rollout left a few
        after the summary topic so that the summary stays last) keeps "summary"; anything else a chapter had typed it as
        (an idea topic's "instructional/exploration", "practice") was a mistake of the older shape and becomes "exercise"."""
        st = tpl.get("source_type")
        return st if st in QT_TYPES or st in ("summary", "framing") else "exercise"

    # ---- the question concept and the answer concept of one book question
    def build_pair(self, u):
        oc = u["c"]["concept_id"]
        cat, suffix, prefix, example_n = u["cls"]
        qname = QN.concept_title(cat, prefix, u["seq"], role="question")
        aname = QN.concept_title(cat, prefix, u["seq"], role="answer")
        # media nodes, rewritten, with the owner set from the split
        q_nodes, a_nodes = [], []
        for n in u["q_nodes"]:
            x = self.rw(n)
            x["concept_id"] = x["home_concept_id"] = u["qcid"]
            q_nodes.append(x)
        for n in u["a_vids"] + u["a_imgs"] + u["a_other"]:
            x = self.rw(n)
            x["concept_id"] = x["home_concept_id"] = u["acid"]
            if x.get("type") == "image" and x.get("image_role") != "solution":
                x["image_role"] = "solution"          # an answer concept's images are its solution cards
            a_nodes.append(x)
        q_ids = [x["id"] for x in q_nodes]
        vids = [x["id"] for x in a_nodes if x.get("type") == "video"]
        sol = [x["id"] for x in a_nodes if x.get("type") == "image"]
        a_media = vids + sol + [x["id"] for x in a_nodes if x.get("type") not in ("video", "image")]
        refs = []
        for r in (u["c"].get("ncert_refs") or []):
            if r not in refs:
                refs.append(r)
        q_blocks, a_blocks = [], []
        qblks = [b for b in u["c"]["content"] if is_qblock(b)]
        other = [b for b in u["c"]["content"] if not is_qblock(b)]
        if len(qblks) > 1:
            self.report["multi_block_units"].append("%s (%d questions)" % (oc, len(qblks)))
        for i, b in enumerate(qblks):
            b = self.rw(b)
            ed = self.edits.get("%s#%d" % (oc, i)) or {}
            question = ed.get("question", b.get("question") or "")
            steps = list(ed.get("steps", b.get("steps") or []))
            answer = ed.get("answer", b.get("answer") or "")
            if any(re.match(r"^\s*(\d+[.)]|Step\s*\d+)", s) for s in steps if isinstance(s, str)):
                self.report["unnumbered_check"].append("%s#%d: a step already starts with its own number" % (oc, i))
            qtex, steps_tex, answer_tex, text = tex_fields(question, steps, answer, self.edits.get("_phrases"))
            old_label = b.get("book_number") or ""
            label = canonical_label(cat, suffix, u["seq"], example_n, old_label)
            if label != old_label:
                self.report["label_canonicalised"] += 1
            common = {k: b[k] for k in COMMON_FIELDS if k in b}
            common["book_number"] = label
            qb = dict(common, type="paragraph", question=question, steps=[], answer="", text=qtex,
                      publication_text=qtex)
            if qtex:
                qb["question_tex"] = qtex
            for k in Q_ONLY_EXTRAS:
                if k in b:
                    qb[k] = b[k]
            if q_ids:
                qb["image_media_id"] = q_ids[0]
            ab = {k: v for k, v in b.items() if k not in DROP_FROM_ANSWER}
            ab.update(common)
            ab.update({"type": "paragraph", "question": question, "steps": steps, "answer": answer,
                       "text": text, "publication_text": text})
            if steps_tex:
                ab["steps_tex"] = steps_tex
            if answer_tex:
                ab["answer_tex"] = answer_tex
            if b.get("s_figure"):
                ab["s_figure"] = b["s_figure"]
            if vids:
                ab["video_media_id"] = vids[0]
            if sol:
                ab["solution_image_media_id"] = sol[0]
                if len(sol) > 1:
                    ab["solution_image_media_ids"] = list(sol)
            q_blocks.append(qb)
            a_blocks.append(ab)
            self.report.setdefault("units", []).append({"key": "%s#%d" % (oc, i), "q": u["qcid"], "a": u["acid"],
                                                         "name": aname})
            if not [s for s in steps if isinstance(s, str) and s.strip()] or not (answer or "").strip():
                self.report["gaps"].append({"key": "%s#%d" % (oc, i), "concept": aname, "question": question,
                                            "has_steps": bool(steps), "has_answer": bool((answer or "").strip())})
        adaptive = {"tier": None, "discovery": False, "hint_ladder": False, "rescue": False, "say": False,
                    "check_my_thinking": False, "added_for_tier": []}
        base = {"key_terms": [], "objective_id": None, "objective_ids": [], "source_segment_role": "practice",
                "ncert_refs": refs, "tier": None, "misconceptions": [], "predict_first": "",
                "enrichment_type": "enrichment", "is_enrichment": True, "mixed_objective_ids": [],
                "recap_objective_ids": [], "adaptive": adaptive}
        qc = dict(base, concept_id=u["qcid"], concept_name=qname, content=[self.rw(b) for b in other] + q_blocks,
                  source_media=None, media_ids=list(q_ids), qt_part="question")
        qc["adaptive"] = dict(adaptive)
        ac = dict(base, concept_id=u["acid"], concept_name=aname, content=a_blocks,
                  source_media="video" if vids else None, media_ids=list(a_media), qt_part="answer")
        ac["adaptive"] = dict(adaptive)
        ac["ncert_refs"] = list(refs)
        if vids:
            ac["video_media_ids"] = list(vids)
        return qc, ac, q_nodes + a_nodes

    # ----------------------------------------------------------------------------------------------- objectives
    def new_objectives(self, new):
        objs = self.plan.get("objectives") or []
        keep, drop = [], []
        for o in objs:
            anchors = list(o.get("anchor") or [])
            gone = [a for a in anchors if a in self.split_old]
            if anchors and len(gone) == len(anchors):
                drop.append(o)
            else:
                if gone:
                    self.note("objective %s keeps %d anchor(s), %d replaced anchor(s) removed"
                              % (o.get("objective_id"), len(anchors) - len(gone), len(gone)))
                    o = dict(o, anchor=[a for a in anchors if a not in self.split_old])
                keep.append(o)
        self.report["dropped_objectives"] = [{"id": o.get("objective_id"), "text": o.get("objective_text"),
                                              "anchor": o.get("anchor")} for o in drop]
        omap = {o["objective_id"]: "O%d" % i for i, o in enumerate(keep, 1)}
        dropped_ids = {o["objective_id"] for o in drop}
        out = []
        for o in keep:
            x = self.rw(o)
            x["objective_id"] = omap[o["objective_id"]]
            out.append(x)
        new["objectives"] = out
        sm = {}
        for k, v in (self.plan.get("strand_to_objective_map") or {}).items():
            if v in omap:
                sm[k] = omap[v]
        new["strand_to_objective_map"] = sm

        def remap(lst):
            return [omap[i] for i in lst if i in omap]
        stray = 0
        for t in topics_of(new):
            if t.get("objective_ids"):
                before = len(t["objective_ids"])
                t["objective_ids"] = remap(t["objective_ids"])
                stray += before - len(t["objective_ids"])
            if isinstance(t.get("learning_objectives"), list):
                t["learning_objectives"] = [omap.get(i, i) if isinstance(i, str) and re.fullmatch(r"O\d+", i) else i
                                            for i in t["learning_objectives"]
                                            if not (isinstance(i, str) and i in dropped_ids)]
            for c in t["concepts"]:
                if c.get("objective_id"):
                    if c["objective_id"] in omap:
                        c["objective_id"] = omap[c["objective_id"]]
                    else:
                        c["objective_id"] = None
                        stray += 1
                for k in ("objective_ids", "mixed_objective_ids", "recap_objective_ids"):
                    if c.get(k):
                        before = len(c[k])
                        c[k] = remap(c[k])
                        stray += before - len(c[k])
        for m in new["modules"]:
            for s in m["segments"]:
                if s.get("segment_objective_ids"):
                    s["segment_objective_ids"] = remap(s["segment_objective_ids"])
        # a kept topic's topic_objective is text, not an id; nothing to remap
        if stray:
            self.note("%d reference(s) to a dropped objective removed from kept concepts/topics" % stray)

    # ----------------------------------------------------------------------------------------------- tool links
    def fix_tool_links(self, new):
        """related_concept_ids / reused_in_concepts / reused_in_topics of a 2d_tool node, written by hand from the SOURCE
        node: a link to a replaced question concept points at its QUESTION concept (where the student attempts it)."""
        old_q_topics = {t["topic_id"] for t in topics_of(self.plan) if is_qt(t)}
        topic_of_cid = {c["concept_id"]: t["topic_id"] for t in topics_of(new) for c in t["concepts"]}
        for t in topics_of(new):
            for n in t.get("media") or []:
                if n.get("type") != "2d_tool":
                    continue
        # the source node of each new tool node
        inv = {v: k for k, v in self.media_map.items()}
        for t in topics_of(new):
            for n in t.get("media") or []:
                if n.get("type") != "2d_tool":
                    continue
                old = self.node.get(inv.get(n["id"], ""))
                if old is None:
                    continue

                def cmap(c):
                    if c in self.units_by_old:
                        return self.units_by_old[c]["qcid"]
                    return self.cid_map.get(c, c)
                if "related_concept_ids" in old:
                    n["related_concept_ids"] = list(dict.fromkeys(cmap(c) for c in old["related_concept_ids"] or []))
                if "reused_in_concepts" in old:
                    n["reused_in_concepts"] = list(dict.fromkeys(cmap(c) for c in old["reused_in_concepts"] or []))
                if "reused_in_topics" in old:
                    tops = []
                    for tid in old["reused_in_topics"] or []:
                        if tid in old_q_topics:
                            for c in n.get("related_concept_ids") or []:
                                if c in topic_of_cid and topic_of_cid[c] not in tops:
                                    tops.append(topic_of_cid[c])
                            if self.tid_map.get(tid) and self.tid_map[tid] not in tops and not n.get("related_concept_ids"):
                                tops.append(self.tid_map[tid])
                        else:
                            tops.append(self.tid_map.get(tid, tid))
                    n["reused_in_topics"] = list(dict.fromkeys(tops))

    # ----------------------------------------------------------------------------------------------- coverage
    def fix_coverage(self, new):
        cov = (new.get("source_metadata") or {}).get("ncert_coverage")
        if not isinstance(cov, dict):
            return
        for ref, cids in list(cov.items()):
            if not isinstance(cids, list):
                continue
            out = []
            for c in cids:
                if c in self.A2Q.values():
                    pass
                if c in self.A2Q and self.A2Q[c] not in out:
                    out.append(self.A2Q[c])
                if c not in out:
                    out.append(c)
            cov[ref] = out

    # ----------------------------------------------------------------------------------------------- finish
    def finish(self, new):
        ver = int(self.src.get("version") or 0) + 1
        cid = self.src.get("chapter_id") or ("cbse_eng_%s" % self.key)
        new["version"] = ver
        new["plan_id"] = "%s_v%d" % (cid, ver)
        topics = topics_of(new)
        sm = new.get("source_metadata") or {}
        stats = sm.get("summary_stats")
        if isinstance(stats, dict):
            media = [n for t in topics for n in t.get("media") or []]
            qcs = [c for t in topics for c in t["concepts"] if c.get("qt_part")]
            upd = {"topics": len(topics), "concepts": sum(len(t["concepts"]) for t in topics),
                   "objectives": len(new["objectives"]), "tools": sum(1 for n in media if n.get("type") == "2d_tool"),
                   "images": sum(1 for n in media if n.get("type") == "image"),
                   "videos": sum(1 for n in media if n.get("type") == "video"),
                   "question_topics": sum(1 for t in topics if is_qt(t)),
                   "question_concepts": sum(1 for c in qcs if c["qt_part"] == "question")}
            for k, v in upd.items():
                if k in stats:
                    stats[k] = v
        sm["qa_split"] = {"from": "%s_v%s" % (cid, self.src.get("version")),
                          "note": "Part 1 field cleanup, Part 2 question/answer split, LaTeX; ids renumbered, urls unchanged."}
        new["source_metadata"] = sm
        self.report["ids"] = {"topics": len(topics), "concepts": sum(len(t["concepts"]) for t in topics)}


# ------------------------------------------------------------------------------------------------ checks
def structural_problems(new, old, edits=None):
    """Everything the guide's step 9 lists, plus the Q/A pairing."""
    P = []
    topics = topics_of(new)
    tids = [t["topic_id"] for t in topics]
    if len(set(tids)) != len(tids):
        P.append("duplicate topic ids")
    sids = [s["segment_id"] for m in new["modules"] for s in m["segments"]]
    if len(set(sids)) != len(sids):
        P.append("duplicate segment ids")
    for m in new["modules"]:
        for s in m["segments"]:
            if len(s["topics"]) != 1:
                P.append("segment %s holds %d topics" % (s["segment_id"], len(s["topics"])))
    for i, t in enumerate(topics, 1):
        mid = t["topic_id"].split(".")[0]
        if t["topic_id"] != "%s.S%d.T%d" % (mid, i, i):
            P.append("topic id %s is not sequential (position %d)" % (t["topic_id"], i))
    cids = [c["concept_id"] for t in topics for c in t["concepts"]]
    if len(set(cids)) != len(cids):
        P.append("duplicate concept ids")
    for n, c in enumerate(cids, 1):
        if not c.endswith(".C%d" % n):
            P.append("concept id %s is not the %dth in document order" % (c, n))
            break
    for t in topics:
        for c in t["concepts"]:
            if not c["concept_id"].startswith(t["topic_id"] + ".C"):
                P.append("%s sits under %s" % (c["concept_id"], t["topic_id"]))
    media = {}
    for t in topics:
        for n in t.get("media") or []:
            if n["id"] in media:
                P.append("duplicate media id %s" % n["id"])
            media[n["id"]] = (t, n)
    cid_set = set(cids)
    for oid, (t, n) in media.items():
        if n.get("concept_id") not in cid_set:
            P.append("media %s names an unknown concept %s" % (oid, n.get("concept_id")))
        mm = MEDIA_ID.match(oid)
        if mm and mm.group(1) != n.get("concept_id"):
            P.append("media %s is not under its own concept %s" % (oid, n.get("concept_id")))
    img_seq = {}
    for t in topics:
        for c in t["concepts"]:
            for i in c.get("media_ids") or []:
                if i not in media:
                    P.append("%s lists media %s that does not exist" % (c["concept_id"], i))
            for b in c.get("content") or []:
                if isinstance(b, dict):
                    for k in ("image_media_id", "video_media_id", "solution_image_media_id"):
                        if b.get(k) and b[k] not in media:
                            P.append("%s block %s -> %s does not exist" % (c["concept_id"], k, b[k]))
                    for i in b.get("solution_image_media_ids") or []:
                        if i not in media:
                            P.append("%s block solution_image_media_ids -> %s does not exist" % (c["concept_id"], i))
    for oid, (t, n) in media.items():
        if n.get("type") == "image":
            mm = re.search(r"\.IMG(\d+)$", oid)
            if mm:
                img_seq.setdefault(n.get("concept_id"), []).append(int(mm.group(1)))
    for cid, seq in img_seq.items():
        if seq != list(range(1, len(seq) + 1)):
            P.append("images of %s are not IMG1..IMGn in list order: %s" % (cid, seq))
    # Q/A pairing
    flat = [c for t in topics for c in t["concepts"]]
    for i, c in enumerate(flat):
        if c.get("qt_part") == "question":
            nxt = flat[i + 1] if i + 1 < len(flat) else None
            if not nxt or nxt.get("qt_part") != "answer":
                P.append("%s is a question concept with no answer concept after it" % c["concept_id"])
        if c.get("qt_part") == "answer":
            prv = flat[i - 1] if i else None
            if not prv or prv.get("qt_part") != "question":
                P.append("%s is an answer concept with no question concept before it" % c["concept_id"])
    # coverage + objectives
    cov = (new.get("source_metadata") or {}).get("ncert_coverage") or {}
    for ref, lst in cov.items():
        for c in lst if isinstance(lst, list) else []:
            if c not in cid_set:
                P.append("ncert_coverage[%s] -> %s does not exist" % (ref, c))
    onums = [o["objective_id"] for o in new["objectives"]]
    if onums != ["O%d" % i for i in range(1, len(onums) + 1)]:
        P.append("objective ids are not O1..On gap-free")
    for o in new["objectives"]:
        for a in o.get("anchor") or []:
            if a not in cid_set:
                P.append("objective %s anchors %s which does not exist" % (o["objective_id"], a))
        if o.get("home_topic_id") and o["home_topic_id"] not in set(tids):
            P.append("objective %s home topic %s does not exist" % (o["objective_id"], o["home_topic_id"]))
    oset = set(onums)
    for t in topics:
        for c in t["concepts"]:
            for k in ("objective_id",):
                if c.get(k) and c[k] not in oset:
                    P.append("%s %s -> %s does not exist" % (c["concept_id"], k, c[k]))
            for k in ("objective_ids", "mixed_objective_ids", "recap_objective_ids"):
                for i in c.get(k) or []:
                    if i not in oset:
                        P.append("%s %s -> %s does not exist" % (c["concept_id"], k, i))
    old_media = {n["id"] for t in topics_of(old) for n in t.get("media") or []}
    dang_old = sum(1 for vc in old.get("video_coverage") or [] if vc.get("video_id") not in old_media)
    dang_new = [vc.get("video_id") for vc in new.get("video_coverage") or [] if vc.get("video_id") not in media]
    if len(dang_new) > dang_old:
        P.append("video_coverage names %d video(s) that do not exist (the source had %d): %s"
                 % (len(dang_new), dang_old, dang_new[:3]))
    # nothing lost: every old question appears once as Q and once as A
    def oq(plan):
        out = []
        for t in topics_of(plan):
            if is_qt(t):
                for c in t["concepts"]:
                    for i, b in enumerate(qblocks(c)):
                        ed = (edits or {}).get("%s#%d" % (c["concept_id"], i)) or {}
                        out.append(ed.get("question", b.get("question")))
        return out
    old_q = oq(old)
    new_q = [b.get("question") for c in flat if c.get("qt_part") == "question" for b in c["content"] if is_qblock(b)]
    new_a = [b.get("question") for c in flat if c.get("qt_part") == "answer" for b in c["content"] if is_qblock(b)]
    # passthrough concepts keep their blocks
    pt = [b.get("question") for t in topics_of(new) for c in t["concepts"] if not c.get("qt_part") and is_qt(t)
          for b in qblocks(c)]
    if sorted(map(str, old_q)) != sorted(map(str, new_q + pt)):
        P.append("question set changed: %d old vs %d new" % (len(old_q), len(new_q) + len(pt)))
    if sorted(map(str, new_q)) != sorted(map(str, new_a)):
        P.append("question and answer concepts do not hold the same questions")
    # urls frozen
    def urls(plan):
        out = {}
        for t in topics_of(plan):
            for n in t.get("media") or []:
                out[n["id"]] = tuple(str(n.get(k)) for k in ("planned_url", "image_url", "video_url", "2d_tool_url"))
        return sorted(v for v in out.values())
    if urls(old) != urls(new):
        P.append("the set of media urls changed")
    return P


def latex_problems(new):
    from core.solutions import latex_checker
    out = []
    for t in topics_of(new):
        for c in t["concepts"]:
            if not c.get("qt_part"):
                continue
            for b in c["content"]:
                for f in ("text", "publication_text"):
                    s = b.get(f)
                    if isinstance(s, str) and s:
                        for issue in latex_checker.check(s):
                            out.append("%s/%s: %s: %s | %s" % (c["concept_id"], f, issue.kind, issue.message,
                                                              s[:160].replace("\n", " / ")))
    return out


def gate_problems(plan, cfg):
    from gates import gate_runner
    errors, counts = gate_runner.run(plan, cfg)
    return list(errors), list((counts or {}).get("warnings") or [])


def norm(msg):
    """A gate message with the ids and the minus sign normalised (the converter writes "-" for U+2212), so the same
    problem reads the same before and after. Numbers stay: a different false equation is a different problem."""
    m = TOKEN.sub("<id>", msg).replace("\u2212", "-")
    m = re.sub(r"still holds book question\(s\) \[.*?\]", "still holds book question(s) [..]", m)
    m = re.sub(r"media_ids needs the question video.*", "media_ids needs the question video", m)
    m = re.sub(r"\bO\d+\b", "O#", m)
    return m[:200]


def gate_delta(old_plan, new_plan, cfg):
    """Gate families run on the source and on the result with the strict config (solutions + question_layout). A
    problem is NEW when its normalised text did not occur before. How many times it occurs is not compared: a question
    now sits in two concepts (the question card and the answer), so every message about its text appears twice."""
    cfg2 = dict(cfg, solutions=True, question_layout=True)
    eo, wo = gate_problems(old_plan, cfg2)
    en, wn = gate_problems(new_plan, cfg2)
    so = {norm(x) for x in eo}
    new_kinds = sorted({norm(x) for x in en} - so)
    return {"errors_before": len(eo), "errors_after": len(en), "warnings_before": len(wo), "warnings_after": len(wn),
            "worse": {k: [1, 1] for k in new_kinds}, "after_samples": en[:25]}


def load_config(repo, key, plan):
    p = os.path.join(repo, "chapters", key, "new_design", "chapter.config.json")
    if os.path.exists(p):
        with io.open(p, encoding="utf-8") as f:
            return json.load(f)
    return {"chapter_id": plan.get("chapter_id"), "phase": 2, "grade": plan.get("grade"), "grade_band": "6_8",
            "chapter_no": plan.get("unit_number"), "chapter_name": plan.get("chapter_name"),
            "theorem_chapter": False, "eqcheck": "plain"}


def load_descriptions(path):
    if not os.path.exists(path):
        return {}
    ns = {}
    with io.open(path, encoding="utf-8") as f:
        exec(compile(f.read(), path, "exec"), ns)
    return ns.get("DESCRIPTIONS") or {}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--key", required=True, help="chapter folder, e.g. maths7_ch10")
    ap.add_argument("--src", required=True, help="the live plan json (the active version)")
    ap.add_argument("--out", help="output folder (default chapters/<key>/lp_qa_latex)")
    ap.add_argument("--no-gates", action="store_true")
    a = ap.parse_args(argv)
    out = a.out or os.path.join(_ROOT, "chapters", a.key, "lp_qa_latex")
    os.makedirs(out, exist_ok=True)
    with io.open(a.src, encoding="utf-8") as f:
        src = json.load(f)
    desc = load_descriptions(os.path.join(out, "tool_descriptions.py"))
    edits = {}
    ep = os.path.join(out, "edits.json")
    if os.path.exists(ep):
        with io.open(ep, encoding="utf-8") as f:
            edits = json.load(f)
    tr = Transform(src, a.key, desc, edits)
    new = tr.run()
    rep = tr.report
    rep["source_version"] = src.get("version")
    rep["new_version"] = new["version"]
    rep["structural"] = structural_problems(new, tr.plan, edits)
    rep["latex_issues"] = latex_problems(new)
    from core.solutions import answer_checker
    answer_ids = {c["concept_id"] for t in topics_of(new) for c in t["concepts"] if c.get("qt_part") == "answer"}
    allgaps = answer_checker.find_gaps(new)
    rep["answer_gaps"] = [{"concept": g.concept_id, "topic": g.topic_name, "missing": g.missing, "q": g.question[:200]}
                          for g in allgaps if g.concept_id in answer_ids]
    rep["stubs"] = [g.concept_id for g in allgaps if g.concept_id not in answer_ids]
    try:
        from gates import media_content
        rep["preflight_before"] = media_content.preflight(src)
        rep["preflight_after"] = media_content.preflight(new)
    except Exception as ex:          # pragma: no cover
        rep["preflight_error"] = repr(ex)
    if not a.no_gates:
        try:
            cfg = load_config(_ROOT, a.key, src)
            rep["gates"] = gate_delta(src, new, cfg)
        except Exception as ex:      # pragma: no cover
            rep["gates_error"] = repr(ex)
    # the tool write-ups in the user's "Tool Name / Tool Description" format, for review (the plan carries them in `description`)
    md = []
    for t in topics_of(new):
        for n in t.get("media") or []:
            if n.get("type") == "2d_tool":
                md.append("Tool Name: %s\n\nTool Description:\n\n%s\n\n(tool id %s, concept %s, topic: %s)\n"
                          % (n.get("tool_name") or n.get("title"), n.get("description") or "(none)", n["id"],
                             n.get("concept_id"), t.get("topic_name")))
    with io.open(os.path.join(out, "TOOL_DESCRIPTIONS.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("# %s - tool descriptions (%d tools)\n\n%s" % (a.key, len(md), "\n---\n\n".join(md)))
    name = "cbse_eng_%s.json" % a.key
    with io.open(os.path.join(out, name), "w", encoding="utf-8", newline="\n") as f:
        json.dump(new, f, ensure_ascii=False, indent=1)
    with io.open(os.path.join(out, "report.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(rep, f, ensure_ascii=False, indent=1)
    topics = topics_of(new)
    n_q = sum(1 for t in topics for c in t["concepts"] if c.get("qt_part") == "question")
    print("%s: v%s -> v%s | topics %d | concepts %d | Q/A pairs %d | objectives %d (dropped %d) | gaps %d | stubs %d | "
          "latex %d | structural %d | cats %s" % (
              a.key, rep["source_version"], rep["new_version"], len(topics), rep["ids"]["concepts"], n_q,
              len(new["objectives"]), len(rep["dropped_objectives"]), len(rep["answer_gaps"]), len(rep["stubs"]),
              len(rep["latex_issues"]), len(rep["structural"]), rep["categories"]))
    if rep["structural"]:
        for p in rep["structural"][:12]:
            print("  STRUCT:", p)
    g = rep.get("gates")
    if g:
        print("  gates: errors %d -> %d, worse: %s" % (g["errors_before"], g["errors_after"], g["worse"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
