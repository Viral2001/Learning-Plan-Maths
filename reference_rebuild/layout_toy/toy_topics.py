# The TOOLS and TOPICS of the layout toy. run_smoke.py puts the authoring helpers of
# chapter_template/concept_plan.py.template (WE, FIO, A, DOER, TOPIC, T) above this text, so the toy always
# runs against the helpers a real chapter gets.

_HINTS = ["What does the line show?", "Which way is a negative move?",
          "Try the move and read where the coin stops.", "A negative move goes left: start plus the move."]


def _tool(tool_id, title):
    return T(tool_id, title, "manipulative",
             "Dragging a coin along a number line shows that adding a negative number moves it left.",
             "A number line from −5 to 5 with a coin and a slider that sets the move.",
             ["Predict where the coin stops.", "Drag the slider to set the move.", "Read the stop.",
              "Compare with the prediction."],
             ["Start at 2, move −3.", "Start at 0, move −4.", "Start at −1, move 5.",
              "Start at 3, move −3.", "Start at −2, move −2."],
             ["A wrong stop still lets the coin move.", "A solved card shows the start, the move and the stop."],
             "The student has predicted and checked at least three stops.",
             ["start", "move", "cardIndex"], ["M_TOY_1"], _HINTS)


TOOLS = {"tool_a": _tool("tool_toy_moves", "Moves on a Line"),
         "tool_b": _tool("tool_toy_takeaway", "Take Away on a Line")}

TOPICS = []

TOPICS.append(TOPIC(
    "T1", "M1", "A Coin on a Line", ["Opening"], "Understand", "",
    "The student predicts where a coin lands when it moves left.",
    [A("T1.C1", "Opening Hook", "Remember", "",
       textbook=["A coin sits at 2 on a number line."],
       teach=["Ask: if it moves 3 to the left, where does it stop?"],
       ncert=["opening"], key_terms=["coin"], video_focus=["HOOK"], minutes=5, enrichment=True)],
    topic_type="framing"))

TOPICS.append(TOPIC(
    "T2", "M1", "Adding on a Number Line", ["2.1"], "Apply",
    "Find where a coin stops by adding a negative move to its start on a number line.",
    "Moves to the right are positive, moves to the left are negative; the stop is start plus move.",
    [A("T2.C1", "Moving Right and Left", "Apply",
       "The student adds a negative number to a start by moving left on the line.",
       textbook=["A move to the right is positive and a move to the left is negative."],
       teach=["Predict the stop before computing it.", "Add the move to the start."],
       examples=[WE("Start at 2 and move 3 to the left. Where do you stop?",
                    ["The move is −3.", "2 + (−3) = −1."], "−1")],
       key_terms=["start", "move"], misconceptions=["M_TOY_1"], minutes=12),
     DOER("T2.C2", "Practice: Moves on a Line", "tool_a", "Apply",
          "The student confirms with the tool that adding a negative number moves the coin left.",
          ["A negative move goes left.", "The stop is the start plus the move."],
          items=[
              FIO("2.1.ex1", "Example 1", "A coin is at 4. It moves 7 units to the left. Where does it stop?",
                  ["A move to the left is negative, so the move is −7.", "4 + (−7) = −3."],
                  "−3", kind="example",
                  q_figure="A number line from −5 to 5 with 0 marked and the coin at 4.",
                  s_figure="The same line with a jump of 7 to the left from 4 and the coin at −3."),
              FIO("2.1.try1", "Try This (2.1)", "Which is larger, −2 or −5?",
                  ["−2 is to the right of −5 on the line.", "A number further right is larger."],
                  "−2", kind="prompt"),
              FIO("2.1.FiO1", "Figure it Out (2.1), Q1",
                  "Find: (a) 3 + (−8) (b) −4 + (−5) (c) −7 + 7 (d) 0 + (−9) (e) 10 + (−10) "
                  "(f) −6 + 2 (g) 5 + (−1) (h) −3 + (−3)",
                  ["Adding a negative number moves left.", "(a) 3 + (−8) = −5.", "(b) −4 + (−5) = −9.",
                   "(c) −7 + 7 = 0.", "(d) 0 + (−9) = −9.", "(e) 10 + (−10) = 0.",
                   "(f) −6 + 2 = −4.", "(g) 5 + (−1) = 4.", "(h) −3 + (−3) = −6.",
                   "A number and its opposite add to 0."],
                  "(a) −5 (b) −9 (c) 0 (d) −9 (e) 0 (f) −4 (g) 4 (h) −6",
                  kind="exercise")])],
    topic_type="instructional"))

TOPICS.append(TOPIC(
    "T3", "M1", "Taking Away on a Number Line", ["2.2"], "Apply",
    "Subtract a negative number by adding its opposite.",
    "Taking away a negative number is the same as adding the opposite.",
    [A("T3.C1", "Taking Away a Negative", "Apply",
       "The student subtracts a negative number on a number line by changing the take away into an add of the opposite.",
       textbook=["Taking away a number is the same as adding its opposite."],
       teach=["Predict the result before computing it.", "Change the take away into an add."],
       examples=[WE("Find 6 − (−2).", ["Taking away −2 is adding 2.", "6 + 2 = 8."], "8")],
       key_terms=["opposite"], misconceptions=["M_TOY_1"], minutes=12),
     DOER("T3.C2", "Practice: Take Away on a Line", "tool_b", "Apply",
          "The student confirms with the tool that taking away a negative number gives the same result as adding its opposite, on several cards.",
          ["Taking away a negative number adds its opposite."],
          items=[
              FIO("2.2.FiO1", "Figure it Out (2.2), Q1", "Find 5 − (−3).",
                  ["Taking away −3 is adding 3.", "5 + 3 = 8."], "8", kind="exercise")])],
    topic_type="instructional"))

TOPICS.append(TOPIC(
    "T4", "M1", "What We Found", ["Summary"], "Understand", "",
    "Adding a negative number moves left; taking away a negative number adds.",
    [A("T4.C1", "Recap", "Understand", "",
       teach=["Adding a negative moves left; taking away a negative adds."],
       video_focus=["RECAP"], minutes=4, enrichment=True)],
    topic_type="summary"))
