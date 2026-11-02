# -*- coding: utf-8 -*-
"""HTML for one docs/28 video node, shared by every chapter's plan render."""
from __future__ import annotations

import html
import re

from check import spoken


def e(s):
    return html.escape(str(s))


def render_video(x):
    s = x.get("video_script") or {}
    pts = {p["beat_key"]: p for p in x.get("interaction_points", [])}
    rows = []
    for b in s.get("beats", []):
        say = "<br>".join(e(spoken(l)) for l in b["narration"])
        keeko = {"think": "Keeko on screen (placed, thinking)", "raise_hand": "Keeko raises a hand"}.get(b.get("keeko"), "")
        if keeko:
            say += f"<div class='cp'>{e(keeko)}</div>"
        marks = "; ".join(f"{k}: {v}" for k, v in b["marks"].items())
        p = pts.get(b["key"])
        pause = ""
        if b.get("pause_after"):
            pause = (f"<div class='cp'>⏸ pause {b['pause_after']} s"
                     + (f", the player waits: {e(p['prompt'])}" if p else "")
                     + (f" <i>(answer after: {e(p['answer'])})</i>" if p and p.get("answer") else "")
                     + (f" <i>Then: {e(p['handover'])}</i>" if p and p.get("handover") else "") + "</div>")
        rows.append(f"<tr><td><span class='kind'>{e(b['part'])}</span><br><span class='cid'>{e(b['meaning'])}</span></td>"
                    f"<td>{say}{pause}</td><td class='sub' style='font-size:.8rem'>{e(b['on_screen'])}"
                    f"<br><i>{e(marks)}</i></td></tr>")
    fa = s.get("final_answer") or {}
    head = (f"<div class='media m-video'><h4>▶ {e(x['title'])} <span class='cid'>{e(s.get('kind', ''))} · "
            f"{e(x['video_duration_seconds'])} s · {len(x.get('interaction_points', []))} think-and-tell · {e(x['id'])}</span></h4>"
            f"<div class='sub'>{e(x['description'])}</div>"
            f"<div class='sub'>Covers: {e(', '.join(s.get('source', [])))}"
            + (f" · Answer: <b>{e(fa.get('value', ''))}</b>" if fa.get("value") else "")
            + (" · <b>opens after the student tries</b>" if s.get("unlock") == "after_attempt" else "") + "</div>")
    for ph in x.get("photos", []):
        head += (f"<div class='sub'>📷 Photo ({e(ph['subject_type'])}, beats {e(', '.join(ph['beats']))}, "
                 f"{e(ph['placement'])}): {e(ph['subject'])}"
                 + (f" · paired with: {e(ph['pair_with'])}" if ph.get("pair_with") else "")
                 + f"<br><i>Gemini: {e(ph['gemini_prompt'])}</i></div>")
    return (head + f"<details><summary>{len(rows)} beats</summary><div class='tbl'><table>"
            "<tr><th>Part</th><th>Narration</th><th>On screen</th></tr>" + "".join(rows) + "</table></div></details></div>")
