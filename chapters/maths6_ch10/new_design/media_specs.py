# -*- coding: utf-8 -*-
"""TEMPLATE - this chapter's IMAGE specs. Copy to media_specs.py and fill in every TODO.

Videos are NOT specified here: every video in this pipeline is a docs/28 script file under
video_scripts/<key>.json, built by core/video_script (see build.py, which calls
core.video_script.plan_hook / node / check directly - no separate video media_specs module,
unlike the older maths7_ch10/maths8_ch9 media_specs.py this file is modelled on, which still
specified videos itself before docs/28 existed).

One IMAGE spec file per concept that needs one, in media_specs/<authored concept key>.json
(e.g. media_specs/T3.C1.json), shaped:

    {"images": [ { <IMAGE_FIELDS...> } ], "image_decisions": [ {"key": ..., "needs_image": bool,
                                                                  "why": "..."} ]}

Every delivered concept carries exactly one image_decision (even "no, because ..."); at most 2
images per concept. Nothing is rendered here - every node is a placeholder with an empty
"image_url" and a "planned_url" build.py fills in from ASSET_BASE.

    python -B media_specs.py --check-all          every media_specs/*.json file, full coverage
    python -B media_specs.py --check <file.json>  one file only

Hard rules enforced below, matching gates/media_content.py's preflight() exactly:
  * no em dash, no en dash anywhere (DASHES = "—–"; use plain commas or "to");
  * minus is U+2212 (−), never an ASCII hyphen, in any mathematical content;
  * no "NCERT", "CBSE", "textbook" or "page <N>" in any STUDENT_FACING field (title, labels,
    generation_prompt, negative_prompt, accuracy_constraints, instructions_for_student) - those
    words are fine in internal-only fields such as "context"/"teaching_notes" (gate's whitelist),
    but keep them out of this file entirely; there is never a reason to type them.
"""
from __future__ import annotations

import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SPEC_DIR = os.path.join(HERE, "media_specs")

# ---------------------------------------------------------------------------
# palette + treatment constants, copied verbatim from the reference chapters
# (maths7_ch10, maths8_ch9, maths8_ch10 new_design media_specs.py) so every chapter's images stay
# visually consistent. Colour-blind-safe (Okabe-Ito): positive/green, negative/vermilion,
# first-thing/teal, second-thing/amber, focus-or-highlight/reddish-purple, construction/grey.
# ---------------------------------------------------------------------------
PALETTE = {
    "positive": "#009E73",      # green
    "negative": "#D55E00",      # vermilion
    "first": "#0072B2",         # teal
    "second": "#E69F00",        # amber
    "focus": "#CC79A7",         # reddish purple
    "construction": "#6B7280",  # grey
    "outline": "#2B2B2B",
    "text": "#1F2937",
}
IMAGE_TREATMENT = (
    "Flat, friendly educational illustration for a {grade_band} maths lesson: plain white "
    "background, thin uniform dark outlines ({outline}), flat fills with no shading and no "
    "gradients, clean sans-serif labels in plain classroom English a child can read aloud. "
    "Colour-blind-safe colours: {positive} for a positive/first idea, {negative} for a "
    "negative/contrasting idea, {first} for a first set or step, {second} for a second set or "
    "step, {focus} for the focus or highlight, {construction} for construction lines and for "
    "anything struck out. 16:9 landscape, 1456 by 816 pixels."
).format(grade_band="Class 6", **PALETTE)
# The user's rule for this chapter: every image explains the concept's ONE main thing, looks good,
# and never looks crowded. These limits are checked by check_file() below.
CLEAN = (
    "Keep it uncluttered: one main idea only, at most three objects or groups, generous white space "
    "around everything, large readable labels, nothing decorative."
)
MAX_LABELS = 6
MAX_LABEL_WORDS = 6
MAX_STRUCTURE_WORDS = 110
HOUSE_REJECTIONS = [
    "any count of objects, cells, ticks or rows that differs from the numbers stated in the spec",
    "any text beyond the listed visible text, or any listed text misspelled or altered",
    "any board name, publisher name, book title, page number or curriculum branding anywhere in "
    "the frame",
    "a hyphen used in place of a minus sign on any labelled number",
]
FLAT_NEGATIVE = (
    "photorealistic rendering, photographic texture, 3D render, studio lighting or depth-of-field "
    "blur; gradients, drop shadows, bevels or glossy highlights; ornamental borders, mascots, "
    "emoji or speech bubbles that carry no information; watermarks, signatures, logos, stock "
    "imagery; garbled or misspelled words, invented digits, duplicated or contradictory labels, "
    "handwriting or script fonts, wording in any script other than English; text cropped at the "
    "edge, labels overlapping the object they name; any board name, publisher name, book title, "
    "page number or curriculum branding anywhere in the frame or on any prop; a hyphen used as a "
    "minus sign"
)

IMAGE_FIELDS = ["key", "title", "purpose", "composition", "exact_structure", "labels", "rejection",
                "takeaway", "description", "context", "teaching_notes"]
DECISION_FIELDS = ["key", "needs_image", "why"]

DASHES = "—–"
BRANDING = re.compile(r"\bNCERT\b|\bCBSE\b|\btextbook\b|\bpage\s+\d+\b", re.IGNORECASE)
HYPHEN_MINUS_SUSPECT = re.compile(r"(?<=\d)-(?=\d)")   # a hyphen glued between two digits


# ---------------------------------------------------------------------------
# authoring helper
# ---------------------------------------------------------------------------
def IMAGE(key, title, purpose, composition, exact_structure, labels, takeaway, *, description="",
           context="", teaching_notes=""):
    """One image spec. `exact_structure` must be specific enough that an independent reviewer could
    count every element from it alone (the "exact structure" the generation_prompt is built from).
    `labels` is the exhaustive list of visible text; the generation_prompt and negative_prompt
    forbid any text outside this list (HOUSE_REJECTIONS / FLAT_NEGATIVE, above)."""
    return {"key": key, "title": title, "purpose": purpose, "composition": composition,
            "exact_structure": exact_structure, "labels": list(labels), "rejection": list(HOUSE_REJECTIONS),
            "takeaway": takeaway, "description": description or purpose, "context": context,
            "teaching_notes": teaching_notes}


def generation_prompt(im):
    """The generation prompt, Ch10-shaped, built from one spec."""
    return ("MATHEMATICAL IMAGE REQUIREMENT\nTeaching purpose: %s\n\nComposition: %s %s %s\n\n"
            "Exact structure: %s\n\nVisible text, exactly and only: %s\n\nTakeaway: %s"
            % (im["purpose"], IMAGE_TREATMENT, CLEAN, im["composition"], im["exact_structure"],
               "; ".join(im["labels"]), im["takeaway"]))


def DECISION(key, needs_image, why):
    return {"key": key, "needs_image": needs_image, "why": why}


# ---------------------------------------------------------------------------
# loading + checks
# ---------------------------------------------------------------------------
def load_all():
    images, decisions = {}, {}
    for p in sorted(glob.glob(os.path.join(SPEC_DIR, "*.json"))):
        with open(p, encoding="utf-8-sig") as f:
            d = json.load(f)
        for im in d.get("images", []):
            images.setdefault(im.get("key"), []).append(im)
        for dc in d.get("image_decisions", []):
            if dc.get("key") in decisions:
                raise SystemExit("duplicate image decision %s in %s" % (dc.get("key"), p))
            decisions[dc["key"]] = dc
    return images, decisions


def _texts(spec):
    out = []
    for f in IMAGE_FIELDS:
        v = spec.get(f)
        if isinstance(v, str):
            out.append(v)
        elif isinstance(v, list):
            out.extend(x for x in v if isinstance(x, str))
    return out


def check_file(path):
    problems = []
    with open(path, encoding="utf-8-sig") as f:
        d = json.load(f)
    for im in d.get("images", []):
        missing = [f for f in ("key", "title", "exact_structure", "labels") if not im.get(f)]
        if missing:
            problems.append("%s: image %r missing %s" % (path, im.get("key"), missing))
        for f in IMAGE_FIELDS:
            if f not in ("context", "teaching_notes", "description") and not im.get(f):
                problems.append("%s: image %r has an empty %s" % (path, im.get("key"), f))
        labels = im.get("labels") or []
        if len(labels) > MAX_LABELS:
            problems.append("%s: image %r has %d labels (max %d, keep it uncluttered)"
                            % (path, im.get("key"), len(labels), MAX_LABELS))
        for lb in labels:
            if len(str(lb).split()) > MAX_LABEL_WORDS:
                problems.append("%s: image %r label too long (max %d words): %r"
                                % (path, im.get("key"), MAX_LABEL_WORDS, lb))
        if len(str(im.get("exact_structure", "")).split()) > MAX_STRUCTURE_WORDS:
            problems.append("%s: image %r exact_structure over %d words (too busy)"
                            % (path, im.get("key"), MAX_STRUCTURE_WORDS))
        want = os.path.splitext(os.path.basename(path))[0] + ".IMG"
        if not str(im.get("key", "")).startswith(want):
            problems.append("%s: image key %r must start with %r" % (path, im.get("key"), want))
        for t in _texts(im):
            if any(ch in t for ch in DASHES):
                problems.append("%s: image %r has an em/en dash: %r" % (path, im.get("key"), t[:80]))
            if BRANDING.search(t):
                problems.append("%s: image %r carries textbook branding: %r" % (path, im.get("key"), t[:80]))
            if HYPHEN_MINUS_SUSPECT.search(t):
                problems.append("%s: image %r may use a hyphen as a minus sign: %r" % (path, im.get("key"), t[:80]))
    for dc in d.get("image_decisions", []):
        if "needs_image" not in dc or not dc.get("why"):
            problems.append("%s: image_decision %r missing needs_image/why" % (path, dc.get("key")))
    return problems


def check_all():
    problems = []
    for p in sorted(glob.glob(os.path.join(SPEC_DIR, "*.json"))):
        problems += check_file(p)
    return problems


# ---------------------------------------------------------------------------
# TODO: a worked example of one media_specs/<key>.json file's content, for reference only (not
# written to disk by this module - copy the shape into media_specs/T2.C1.json etc. by hand or with
# a small per-concept script, the way the reference chapters do).
# ---------------------------------------------------------------------------
EXAMPLE_FILE = {
    "images": [
        IMAGE("T2.C1.IMG1", "TODO image title", "TODO: what teaching job this image does.",
              "TODO: one or two sentences on the overall layout.",
              "TODO: the exhaustive, countable structure - every shape, count and position, specific "
              "enough to regenerate from this text alone.",
              ["TODO", "exhaustive", "list", "of", "visible", "text"],
              "TODO: the one idea the student should take away from looking at it.")],
    "image_decisions": [DECISION("T2.C1", True, "TODO: why this concept needs an image.")],
}


if __name__ == "__main__":
    if "--check-all" in sys.argv:
        problems = check_all()
    else:
        args = [a for a in sys.argv[1:] if a != "--check"]
        problems = []
        for a in args:
            problems += check_file(a)
    print("%d problem(s)" % len(problems))
    for p in problems:
        print("  -", p)
    sys.exit(1 if problems else 0)
