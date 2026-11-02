# -*- coding: utf-8 -*-
"""The video_script contract (docs/28_video_script_prompt.md), as constants.

Every chapter's videos are written to this contract and checked by check.py. The numbers here are copied
from the prompt; do not tune them per chapter, except through a chapter's `length_override`, which is used
only where the user's own chapter document sets different lengths (Class 8 Ch1, Teaching Flow v3).
"""
from __future__ import annotations

# Class 6 to 8 Keeko design (user, 28 Oct 2026): `worked` and `theorem` are the concept videos, `exercise` the question
# video, `hook` the chapter opener. There is no recap video and no recap or break part. Keeko (the mascot, no voice)
# raises a hand only at the END of a concept video (the `keeko` part), and sits on screen for the one think-and-tell.
KINDS = ("hook", "worked", "exercise", "theorem", "story")
CONCEPT_KINDS = ("worked", "theorem", "story")        # these end with Keeko's raised hand
PARTS = ("hook", "ground", "idea", "keeko")
ROLES = ("connect objects", "(co)vary objects", "visualise a concept", "visualise a process",
         "symbol sense", "connect to reality", "generalise")
MEANINGS = ("SHOW", "BUILD", "TRACE", "COMPARE", "TRANSFORM", "VARY", "FOCUS", "BREAK", "CONNECT")
REGIONS = ("anchor", "stage", "working")
SHAPES = ("concept", "procedure", "proof", "application")
PLACEMENTS = ("before", "after")
UNLOCKS = ("always", "after_attempt")
BLOCKS = (
    "title_card", "question_pose", "definition_reveal", "compare_two", "wrong_move_break",
    "worked_example_board", "equation_board", "recap_board", "theorem_board", "proof_by_contradiction",
    "counted_array", "number_line_real", "prime_factor_tree", "algebra_tiles", "axes_plot",
    "linear_system_lines", "quadratic_geometric", "ap_staircase", "coordinate_plane", "triangle_figure",
    "similarity_overlay", "quadrilateral_figure", "circle_figure", "circle_sector_area", "heron_triangle",
    "unit_circle_triangle", "height_distance_scene", "solid_3d", "solid_combination", "net_unfold_3d",
    "paint_vs_space", "histogram_ogive", "probability_grid", "joined_cubes",
)

SCRIPT_KEYS = (
    "kind", "chapter", "source", "placement", "unlock", "callback_to", "why", "substitution", "shape",
    "promise", "anchor", "misconception_id", "wrong_answer", "wrong_move", "payoff_line", "final_answer",
    "answer_verified", "terms", "fraction_reading", "names", "hold_back", "never_show", "maths_rules",
    "design", "open_questions", "keeko_end", "beats",
)
# Keeko. A beat's `keeko` is "" (not on screen), "think" (placed on screen for the think-and-tell, nothing else) or
# "raise_hand" (the concept video's closing doubt). `keeko_end` says what the raised hand brings: a misconception or a
# real-life example; it is "" in a hook and an exercise video, which have no raised hand.
KEEKO_BEAT = ("", "think", "raise_hand")
KEEKO_END = ("", "misconception", "real_life")
THINK_PHRASE = "think and tell"
THINK_PAUSE = 3
KEEKO_LINE = "keeko has raised"        # the teacher's line that hands over to the doubt
# Names are placeholders ({{NAME_1}} ... {{NAME_10}}), one token per character across a chapter (name_slots.json).
NAME_TOKEN = r"\{\{NAME_(\d+)\}\}"
NAME_SLOTS_MAX = 10
NAME_SLOTS_FILE = "name_slots.json"
# The idea part is a board solution: given, find, step_1 ... step_n, answer, one line per beat.
IDEA_FIXED = ("given", "find", "answer")
IDEA_STEP = r"step_\d+"
BEAT_KEYS = ("key", "part", "role", "meaning", "region", "on_screen", "marks", "carries_over", "colours",
             "removed", "moves_through", "pause_after", "block", "keeko", "narration")

WPM = 173
WPS = WPM / 60.0

# words and beats per kind (Part 5). Seconds follow from words / WPS plus the pauses.
LIMITS = {
    "hook":     {"words": (55, 130),   "beats": (3, 5),   "seconds": (20, 45)},
    "worked":   {"words": (110, 430),  "beats": (6, 12),  "seconds": (45, 150)},
    "exercise": {"words": (110, 520),  "beats": (6, 12),  "seconds": (45, 180)},
    "theorem":  {"words": (350, 860),  "beats": (8, 16),  "seconds": (120, 300)},
    "story":    {"words": (1000, 1100), "beats": (17, 20), "seconds": (330, 420)},
}
REQUIRED_PARTS = {
    "hook": ("hook",),
    "worked": ("hook", "ground", "idea", "keeko"),
    "exercise": ("hook", "ground", "idea"),
    "theorem": ("hook", "ground", "idea", "keeko"),
    "story": ("hook", "ground", "idea", "keeko"),
}
NEW_TERMS_MAX = {"hook": 1, "worked": 2, "exercise": 2, "story": 3, "theorem": 3}

SENTENCE_MAX = 18
SENTENCE_AVG = (9.0, 12.0)
BEAT_WORDS_MAX = 130
BOOKMARK_GAP_MAX = 28
PART_START_BOOKMARK_WITHIN = 4          # the first bookmark comes within the first 4 spoken words
PAUSE_MAX = 3

BANNED_WORDS = ("just", "simply", "basically", "obviously", "easy", "thus", "hence", "therefore", "points",
                "stars", "score")
BANNED_PHRASES = ("believe in yourself", "you can do it", "level up")
BAD_LINE_STARTS = ("so", "now", "alright", "well", "okay")
# "Say the operation, not the book word" (Part 3). A chapter may allow one of these when it is the chapter's
# own subject word (e.g. "difference" in the integers chapter); "per" is always allowed in "per cent".
BOOK_OPERATION_WORDS = ("product", "difference", "quotient", "per")
BOOK_WORD_SWAPS = ("surmounted by", "brim", "hollowed out", "consecutive", "diametrically opposite",
                   "constituents", "circumscribes", "circumscribe", "tsa", "csa", "it may be noted that")
AMERICAN_SPELLINGS = ("color", "colors", "colored", "center", "centers", "centered", "meter", "meters",
                      "centimeter", "centimeters", "millimeter", "millimeters", "kilometer", "kilometers",
                      "liter", "liters", "math", "favorite", "neighbor", "neighbors", "behavior", "gray",
                      "analyze", "realize", "recognize", "organize")
HINGLISH = ("hai", "nahi", "nahin", "kya", "accha", "achha", "yaar", "arre", "chalo", "matlab", "bhai",
            "bhaiya", "haan", "theek", "thik", "kitna", "kaise", "dekho")
SPEECH_BANNED_CHARS = "0123456789+=×÷%^²³π√<>∠°*/\\|~#@&$€₹"
DASHES = ("–", "—")            # en and em dash: banned anywhere in a plan (upload preflight)
REASON_WORDS = ("because", "since", "as we", "so that", "that means")
DEFINE_WORDS = ("called", "we call", "means", "is named", "the name", "name for", "known as")
MATHS_WORDS_NEAR_A = ("squared", "cubed", "plus", "minus", "times", "equals", "over", "divided")
SYMBOL_ON_SCREEN = "=+×÷^²³√<>∠"

# ---------------------------------------------------------------- photos inside videos
# docs/25 §14 "Photos inside videos" (user rule, 29 Sep 2026). A photo is a Gemini-generated picture of a real
# thing, place or scene, shown for one `connect to reality` beat and then replaced by the drawn schematic. It is
# never a concept image and never carries the maths the child must read. Photos live in a chapter library,
# <chapter>/photos/<id>.json (one file per photo, reused by every video that shares the scene); a beat points at
# one with `"photo": {"id", "placement"}`. Both are optional: a script without photos is unchanged.
OPTIONAL_BEAT_KEYS = ("photo",)
PHOTO_BEAT_KEYS = ("id", "placement")
PHOTO_PLACEMENTS = ("full", "backdrop", "left", "right")
PHOTO_ROLE = "connect to reality"
PHOTO_BLOCKS = ("", "title_card", "question_pose")     # a photo beat carries no maths board
PHOTO_FILE_KEYS = ("id", "subject_type", "subject", "why", "need_basis", "gemini_prompt", "alt_text",
                   "reference", "maths_on_object", "pair_with")
# thing, place, nature, artwork, document: a specific real object (the three tests, every grade).
# scene: a generic real-world setting; Class 3 to 6 by default, Class 7 and 8 on need basis, never Class 9 up.
# person: a real person with an authentic likeness; needs `reference` (no reference, no face).
PHOTO_SUBJECTS = ("thing", "place", "nature", "artwork", "document", "scene", "person")
PHOTO_SCENE_GRADES = {"default": (3, 6), "need_basis": (7, 8)}
PHOTO_PROMPT_MUST = "no text"          # every Gemini prompt says the frame holds no text, numerals or labels
PHOTO_BANNED_CHARS = "0123456789"      # Gemini draws digits badly, and a photo never carries a number
PHOTO_BRANDING = ("ncert", "cbse", "ganita", "prakash", "manjari", "maths mela", "textbook")
PHOTO_NO_LIKENESS = ("baudhayana", "baudhāyana", "brahmagupta", "virahanka", "virahāṅka", "pingala", "piṅgala",
                     "fibonacci", "kautilya", "bhaskara", "bhāskara", "euclid", "pythagoras", "aryabhata",
                     "āryabhaṭa", "hemachandra", "gopala", "chintu", "andrew wiles", "wiles")

# ---------------------------------------------------------------- four script rules (user, 1 Oct 2026, docs/27 rules 35 to 38)
# 1. A video never refers to a tool the student played: it stands on its own and speaks only of the book.
TOOL_REFERENCE = (r"tools?|sandbox|playground|simulator|simulation|slider|free[- ]try|"
                  r"you (?:just )?(?:built|played|dragged)|earlier (?:try|build)")
# 2. The chapter hook shows a picture: one beat with a `photo` (check_plan).
# 3. Nothing outside the textbook: every key of `names` must be in <chapter>/book_rules.json "names", and no
#    word of its "banned_words" (analogies, trivia the book does not print) appears in any text.
BOOK_RULES_FILE = "book_rules.json"
# 4. A theorem video states the theorem: a beat keyed `state` (spoken and on screen), whose narration holds every
#    phrase listed for that script in book_rules.json "theorems".
THEOREM_STATE_BEAT = "state"

