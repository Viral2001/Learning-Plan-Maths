# -*- coding: utf-8 -*-
"""Self-test of the Keeko-design checker: an inline reference video must pass, and broken copies must fail.

    python -B core/video_script/test_video_script.py
"""
from __future__ import annotations

import copy
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from check import check_script, check_photo, check_beat_photos  # noqa: E402
import node  # noqa: E402


def beat(key, part, say, on_screen, marks, *, role="visualise a process", meaning="SHOW", pause=0, keeko="", **kw):
    b = {"key": key, "part": part, "role": role, "meaning": meaning, "region": "stage", "on_screen": on_screen,
         "marks": marks, "carries_over": [], "colours": "plain", "removed": "nothing", "moves_through": "plain",
         "pause_after": pause, "block": "", "keeko": keeko, "narration": say}
    b.update(kw)
    return b


def reference():
    """A concept (worked) video: hook with the one think-and-tell, ground, a board solution, Keeko's misconception."""
    beats = [
        beat("hook_scene", "hook",
             ["<bookmark mark='scene'/>This is a question from your book about {{NAME_1}} and a rectangular park.",
              "<bookmark mark='sides'/>The park is eight metres long and five metres wide.",
              "<bookmark mark='ask'/>{{NAME_1}} wants to walk once around the edge of the park.",
              "How far will the walk be?"],
             "title card, the park drawn as a rectangle with its two sides", {"scene": "title card arrives",
             "sides": "the length and the breadth are written on the sides", "ask": "the edge glows"},
             role="connect objects", block="title_card"),
        beat("think", "hook", ["<bookmark mark='think'/>Think and tell."], "the question stays on the board",
             {"think": "Keeko sits at the corner of the board"}, pause=3, keeko="think", meaning="FOCUS"),
        beat("ground", "ground",
             ["<bookmark mark='edge'/>The distance round the edge of a shape is called its perimeter.",
              "<bookmark mark='pairs'/>A rectangle has two long sides and two short sides.",
              "Each pair of equal sides has to be counted twice."],
             "the rectangle with the four sides coloured in two pairs",
             {"edge": "the whole edge lights up", "pairs": "the two pairs get two colours"},
             meaning="BUILD", role="visualise a concept"),
        beat("given", "idea", ["<bookmark mark='given'/>Given, the length is eight metres and the breadth is five metres."],
             "Given: length 8 m, breadth 5 m", {"given": "the two numbers are written"}, meaning="SHOW",
             region="working"),
        beat("find", "idea", ["<bookmark mark='find'/>We have to find the perimeter of the park."],
             "To find: perimeter", {"find": "the word perimeter is written"}, meaning="FOCUS", region="working"),
        beat("step_1", "idea",
             ["<bookmark mark='add'/>Step one, add the length and the breadth, because they are two sides that meet.",
              "Eight plus five gives thirteen."],
             "length + breadth = 8 + 5", {"add": "the two numbers join with a plus sign"}, meaning="BUILD",
             region="working"),
        beat("step_2", "idea",
             ["<bookmark mark='double'/>Step two, double that sum, because the other two sides repeat these two.",
              "Two times thirteen is the whole way round."],
             "perimeter = 2 times the sum", {"double": "the sum is doubled"}, meaning="TRANSFORM", region="working"),
        beat("answer", "idea",
             ["<bookmark mark='ans'/>The perimeter is twenty six centimetres.",
              "{{NAME_1}} walks twenty six metres in one round."],
             "Answer: 26 m", {"ans": "the answer is boxed"}, meaning="SHOW", region="working"),
        beat("hand", "keeko",
             ["<bookmark mark='hand'/>Keeko has raised a hand. Let us check the doubt and solve it."],
             "Keeko with a raised hand", {"hand": "Keeko raises a hand"}, keeko="raise_hand", meaning="FOCUS"),
        beat("doubt", "keeko",
             ["<bookmark mark='doubt'/>Keeko thinks the perimeter is thirteen metres, after adding eight and five.",
              "<bookmark mark='fix'/>But that is only the length and the breadth, which is half the walk.",
              "The other two sides must be counted too, so we double it."],
             "13 m crossed out, the two missing sides drawn in", {"doubt": "13 m appears", "fix": "the missing sides glow"},
             meaning="BREAK"),
    ]
    return {
        "kind": "worked", "chapter": "ncert6:ch1:test", "source": ["Perimeter of a rectangle"], "placement": "after",
        "unlock": "always", "callback_to": "", "why": "A learner sees why the sum of two sides is doubled.",
        "substitution": "numbers of the book's own park question", "shape": "procedure",
        "promise": "", "anchor": "the rectangular park of the book", "misconception_id": "perimeter_half",
        "wrong_answer": "thirteen metres", "wrong_move": "adds length and breadth and stops",
        "payoff_line": "The perimeter is twenty six centimetres.",
        "final_answer": {"value": "26 m", "spoken": "twenty six metres", "units": "m"}, "answer_verified": True,
        "terms": ["perimeter"], "fraction_reading": "", "names": {"{{NAME_1}}": "the child who walks round the park"},
        "hold_back": ["26"], "never_show": [], "maths_rules": ["8 + 5 = 13", "2 x 13 = 26", "perimeter = 2 x (l + b)"],
        "design": "One park, one rectangle, two colours for the two pairs of sides.", "open_questions": [],
        "keeko_end": "misconception", "beats": beats,
    }


def main():
    ref = reference()
    chapter = {"chapter_id": "ncert6:ch1:test"}
    ctx = {"kind": "worked", "key": "k", "answer": "26 m"}
    errs = check_script(ref, ctx, chapter)
    fails = 0
    if errs:
        fails += 1
        print("FAIL reference example:")
        for e in errs:
            print("   ", e)
    else:
        print("ok   reference example passes")

    def broken(name, mutate, expect, c=None, x=None):
        nonlocal fails
        s = copy.deepcopy(ref)
        mutate(s)
        e = check_script(s, x or ctx, c or chapter)
        hit = [m for m in e if expect in m]
        if hit:
            print(f"ok   {name}: {hit[0]}")
        else:
            fails += 1
            print(f"FAIL {name}: expected {expect!r}, got {e}")

    def beat_of(s, key):
        return next(b for b in s["beats"] if b["key"] == key)

    broken("digit in speech", lambda s: beat_of(s, "step_1")["narration"].__setitem__(1, "8 plus five gives thirteen."), "cannot read")
    broken("banned word", lambda s: beat_of(s, "step_1")["narration"].__setitem__(1, "Just add them and you get thirteen."), "banned word 'just'")
    broken("line start", lambda s: beat_of(s, "step_1")["narration"].__setitem__(1, "So eight plus five gives thirteen."), "no line starts")
    broken("mark without bookmark", lambda s: beat_of(s, "given")["marks"].__setitem__("extra", "something"), "marks without bookmarks")
    broken("answer on screen early", lambda s: beat_of(s, "step_2").__setitem__("on_screen", "26 m is written"), "on screen before the reveal")
    broken("letter a", lambda s: beat_of(s, "ground")["narration"].append("Call the first side a squared."), "eigh")
    broken("exercise word", lambda s: beat_of(s, "ground")["narration"].append("This exercise wants the sides."), "never say 'exercise'")
    broken("dash", lambda s: s.__setitem__("design", "One idea — two colours."), "dash")
    broken("book number spoken", lambda s: beat_of(s, "hook_scene")["narration"].__setitem__(0, "<bookmark mark='scene'/>This is example three in your book."), "book numbering")
    broken("wrong final answer", lambda s: s["final_answer"].__setitem__("value", "31 m"), "does not match")
    # Keeko design
    broken("chintu is gone", lambda s: s.__setitem__("anchor", "Chintu in the park"), "Chintu is gone")
    broken("bracket tag", lambda s: beat_of(s, "ground")["narration"].append("[aside] I think so."), "no brackets")
    broken("no think and tell", lambda s: beat_of(s, "think")["narration"].__setitem__(0, "<bookmark mark='think'/>Say it aloud."), "exactly one 'Think and tell.'")
    broken("two think and tell", lambda s: beat_of(s, "ground")["narration"].append("Think and tell."), "exactly one 'Think and tell.'")
    broken("think pause", lambda s: beat_of(s, "think").__setitem__("pause_after", 2), "pause_after 3")
    broken("extra pause", lambda s: beat_of(s, "ground").__setitem__("pause_after", 2), "only pause")
    broken("keeko mark on the wrong beat", lambda s: beat_of(s, "ground").__setitem__("keeko", "think"), "only that beat")
    broken("no raised hand", lambda s: beat_of(s, "hand").__setitem__("keeko", ""), "exactly one raise_hand")
    broken("raised hand line", lambda s: beat_of(s, "hand").__setitem__("narration", ["<bookmark mark='hand'/>There is a doubt to check."]), "Keeko has raised a hand")
    broken("no keeko_end", lambda s: s.__setitem__("keeko_end", ""), "ends with Keeko's raised hand")
    broken("real life keeps no wrong idea", lambda s: s.__setitem__("keeko_end", "real_life"), "so misconception_id is an empty string")
    broken("wrong idea said early", lambda s: beat_of(s, "ground")["narration"].append("Some say thirteen metres."), "first said in the keeko part")
    broken("wrong idea not Keeko's", lambda s: beat_of(s, "doubt")["narration"].__setitem__(0, "<bookmark mark='doubt'/>The perimeter is thirteen metres, after adding eight and five."), "Keeko's doubt")
    broken("recap word", lambda s: beat_of(s, "doubt")["narration"].append("A quick recap follows."), "no recap")
    broken("your turn", lambda s: beat_of(s, "doubt")["narration"].append("Your turn now."), "no recap")
    broken("recap part", lambda s: beat_of(s, "doubt").__setitem__("part", "recap"), "part 'recap'")
    broken("idea order", lambda s: beat_of(s, "find").__setitem__("key", "found"), "board solution")
    broken("late payoff", lambda s: beat_of(s, "step_2")["narration"].append("The perimeter is twenty six centimetres."), "answer beat")
    broken("hook has no hand", lambda s: s.__setitem__("kind", "hook"), "a hook")
    broken("exercise has no hand", lambda s: s.update(kind="exercise", unlock="after_attempt"), "has no raised hand")
    broken("exercise holds no misconception", lambda s: s.update(kind="exercise", unlock="after_attempt", keeko_end=""), "holds no misconception")
    broken("callback needs method", lambda s: s.update(kind="exercise", unlock="after_attempt", keeko_end="", wrong_answer="", wrong_move="", misconception_id="", callback_to=""),
           "names the solved example", x={"kind": "exercise", "key": "k", "method_from": ["w1"]})
    broken("real life only in keeko part", lambda s: beat_of(s, "ground").__setitem__("role", "connect to reality"), "connect to reality")

    # name placeholders
    broken("name outside the slots", lambda s: beat_of(s, "answer")["narration"].append("{{NAME_11}} agrees."), "outside 1 to 10")
    broken("name not declared", lambda s: s.__setitem__("names", {}), "names must list exactly")
    slots = {"{{NAME_1}}": {"original": "Rakesh", "role": "walks round the park"}}
    broken("book name in the text", lambda s: beat_of(s, "answer")["narration"].append("Rakesh smiles."), "must be its placeholder",
           c=dict(chapter, book_rules={"name_slots": slots}))
    broken("slot missing", lambda s: beat_of(s, "answer")["narration"].append("{{NAME_2}} agrees."), "not in this chapter's",
           c=dict(chapter, book_rules={"name_slots": slots}))

    # node: one think-and-tell point per video
    doc = {"key": "t", "title": "How far is the walk?", "description": "d", "teaching_notes": "n", "video_script": ref}
    n = node.video_node(doc, video_id="M1.S1.T1.C1.VID1", concept_id="M1.S1.T1.C1", chapter_label="Test", planned_url="u")
    pts = n["interaction_points"]
    ok = len(pts) == 1 and pts[0]["type"] == "say" and pts[0]["answer"] == "26 m" and "How far" in pts[0]["prompt"]
    print(f"ok   node: {n['video_duration_seconds']} s, one think-and-tell point at {pts[0]['at_s']} s" if ok
          else f"FAIL node points: {pts}")
    fails += not ok

    # photos inside videos: a library entry, a keeko beat that shows it, and what must fail
    good = {"id": "ph_park", "subject_type": "place", "subject": "a rectangular public park seen from above",
            "why": "the real thing Keeko's doubt is about", "need_basis": "",
            "gemini_prompt": "Documentary photo of a rectangular public park with a walking path. No text, "
                             "no numerals, no signs or labels anywhere in the frame.",
            "alt_text": "A rectangular park", "reference": "", "maths_on_object": False, "pair_with": ""}
    lib = {"ph_park": good}
    s = copy.deepcopy(ref)
    kb = beat_of(s, "doubt")
    kb["role"] = "connect to reality"
    kb["photo"] = {"id": "ph_park", "placement": "backdrop"}
    kb["block"] = "question_pose"
    kb["on_screen"] = "a photo of the park sits behind as a backdrop and fades at the end of the beat; " + kb["on_screen"]
    e = check_script(s, ctx, dict(chapter, photos=lib))
    print("ok   photo on a keeko reality beat" if not e else f"FAIL photo on a keeko reality beat: {e}")
    fails += bool(e)
    s2 = copy.deepcopy(s)
    hb = beat_of(s2, "ground")
    hb.update(photo={"id": "ph_park", "placement": "backdrop"}, role="connect to reality", block="question_pose",
              on_screen="a photo fades at the end of the beat")
    e = check_beat_photos(s2, lib)
    print("ok   photo outside hook and keeko" if any("only in the hook or the keeko part" in x for x in e)
          else f"FAIL photo outside hook and keeko: {e}")
    fails += not any("only in the hook or the keeko part" in x for x in e)

    def photo_broken(name, change, grade, expect):
        nonlocal fails
        p = copy.deepcopy(good)
        change(p)
        errs = check_photo(p, grade)
        hit = any(expect in x for x in errs)
        print(f"ok   {name}" if hit else f"FAIL {name}: expected {expect!r}, got {errs}")
        fails += not hit

    photo_broken("scene in Class 9", lambda p: p.update(subject_type="scene"), 9, "never a photo in Class 9")
    photo_broken("digit in prompt", lambda p: p.__setitem__("gemini_prompt", good["gemini_prompt"] + " Five of 5 trees."), 6, "holds a digit")
    photo_broken("prompt without no text", lambda p: p.__setitem__("gemini_prompt", "A park."), 6, "no text")
    photo_broken("person without reference", lambda p: p.update(subject_type="person", subject="D. R. Kaprekar"), 6, "needs a reference")
    photo_broken("map", lambda p: p.update(subject_type="place", subject="a map of India"), 6, "map is never")
    photo_broken("branding", lambda p: p.__setitem__("alt_text", "the NCERT park"), 6, "branding")
    print("ALL OK" if not fails else f"{fails} FAILURES")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
