# -*- coding: utf-8 -*-
"""Fill the {{NAME_n}} placeholders of a chapter's video scripts with the five final names.

    python -B core/video_script/fill_names.py chapters/maths6_ch5/new_design [...more folders]
    python -B core/video_script/fill_names.py --all

The placeholder form of every script is kept in <new_design>/video_scripts_tokens/ (written once, never
overwritten), so a re-run always starts from the placeholders. The chapter's mapping goes to
<new_design>/name_assign.json (token -> name). A chapter has up to 10 characters but only 5 names exist, so the
mapping is a colouring: two characters that appear in the same video never get the same name, a character the
book calls male is given Laksh when the video allows, and the busiest characters are spread over different names.
"""
from __future__ import annotations

import glob
import json
import re
import shutil
import sys
from pathlib import Path

TOKEN = re.compile(r"\{\{NAME_(\d+)\}\}")
HERE = Path(__file__).parent


def load_names():
    return json.loads((HERE / "final_names.json").read_text(encoding="utf-8"))["names"]


def assign(nd: Path, scripts: dict[str, str]):
    names = load_names()
    slots = json.loads((nd / "name_slots.json").read_text(encoding="utf-8"))
    uses, together = {}, {}
    for text in scripts.values():
        toks = sorted(set(TOKEN.findall(text)), key=int)
        for t in toks:
            uses["{{NAME_%s}}" % t] = uses.get("{{NAME_%s}}" % t, 0) + len(re.findall(r"\{\{NAME_%s\}\}" % t, text))
            together.setdefault("{{NAME_%s}}" % t, set()).update("{{NAME_%s}}" % u for u in toks if u != t)
    order = sorted(uses, key=lambda t: (-uses[t], t))
    load = {n["name"]: 0 for n in names}
    out = {}
    for tok in order:
        hint = (slots.get(tok) or {}).get("gender_hint", "")
        taken = {out[o] for o in together[tok] if o in out}
        free = [n for n in names if n["name"] not in taken]
        if not free:
            raise SystemExit(f"{nd}: {tok} meets more than {len(names)} other characters in one video")
        if hint:
            fit = [n for n in free if n["gender"] == hint]
            free = fit or free
        elif any(n["gender"] != "male" for n in free):
            free = [n for n in free if n["gender"] != "male"] or free  # an unstated character is not made male
        pick = min(free, key=lambda n: (load[n["name"]], [x["name"] for x in names].index(n["name"])))
        out[tok] = pick["name"]
        load[pick["name"]] += uses[tok]
    return out


def fill(nd: Path):
    vs, back = nd / "video_scripts", nd / "video_scripts_tokens"
    if not back.exists():
        shutil.copytree(vs, back)
    scripts = {p.name: p.read_text(encoding="utf-8") for p in sorted(back.glob("*.json"))}
    mapping = assign(nd, scripts)
    (nd / "name_assign.json").write_text(json.dumps(mapping, ensure_ascii=False, indent=1), encoding="utf-8")
    n = 0
    for name, text in scripts.items():
        new = TOKEN.sub(lambda m: mapping["{{NAME_%s}}" % m.group(1)], text)
        n += new != text
        (vs / name).write_text(new, encoding="utf-8")
    return len(mapping), n


if __name__ == "__main__":
    args = sys.argv[1:]
    if args == ["--all"]:
        args = sorted(glob.glob("chapters/maths[678]_ch*/new_design"))
    for a in args:
        k, n = fill(Path(a))
        print(f"{a}: {k} characters, {n} scripts filled")
