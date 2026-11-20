# -*- coding: utf-8 -*-
"""Topics T1, T1B, T2, T2B and T3 (module M1: Turns and Angles). The framing intro (the statue game hook and the free Statue
Turn), the short idea topic T1B (Full Turn and Half Turn with the statue question), the two topics Halves and Quarters
Make a Full Turn (T2) and Objects That Turn (T2B), and Angles from Turns.
Every teaching concept has one worked example with the plan's own numbers; every book question is an FIO item of its
topic's DOER, in the book's order. A turn is always a fraction of a full turn: no degrees anywhere."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 The Statue Game (framing) ================================================
# The framing topic holds only the hook video and the free-try tool, and no book question. The concept video and the
# opener's question follow in the short idea topic T1B.
TOPICS.append(TOPIC(
    "T1", "M1", "The Statue Game", ["Chapter opening"], "Understand",
    "",
    "Four children play Statue: they keep turning around and freeze when Statue is called. Try turning a child on the "
    "spot and see where the child faces.",
    [A("T1.C1", "The Statue Game", "Understand",
       "",
       textbook=["Let us play Statue. Keep turning around ...", "STATUE!",
                 "Give examples of real-life situations where you observe turns."],
       teach=["Predict first: four children are playing Statue. They keep turning around, and when Statue is called "
              "they freeze. Will all four be facing the same way?",
              "Four children, A, B, C and D, stand in a row on the playground. They are playing Statue.",
              "They keep turning around. Then someone calls Statue, and every child freezes where they are.",
              "Look at the four children now. They are not all facing the same way. Some turned a lot and some turned "
              "a little, but every one of them turned.",
              "Can you tell which child has made a full turn and which has made a half turn?",
              "Where do you see turns in real life? Think of one example, then try the Statue Turn tool on the next "
              "screen."],
       ncert=["open.story", "open.examples"], key_terms=["turn", "full turn", "half turn"],
       video_focus=["HOOK"], enrichment=True, minutes=4),
     DOER("T1.C3", "Statue Turn: Explore", "statue_turn", "Understand",
          "",
          ["Four children play Statue. They keep turning around and freeze when Statue is called.",
           "Ashutosh and Sahana turn at one spot on the ground, each with one foot fixed.",
           "Turn the child, call Statue, and look at where the child faces compared with the start."],
          misconceptions=["M_SAME_FACING_NO_TURN"], role="try_it", enrichment=True)],
    topic_type="framing", key_terms=["turn", "full turn", "half turn"]))

# ============================== T1B Full Turn and Half Turn ================================================
TOPICS.append(TOPIC(
    "T1B", "M1", "Full Turn and Half Turn", ["Chapter opening"], "Understand",
    "Students name a turn as a full turn or a half turn by comparing where someone faces with where they faced at the "
    "start, and use this to answer the question about the children in the statue game.",
    "A full turn brings you back to the starting position. A half turn leaves you facing the opposite way.",
    [A("T1B.C1", "Full Turn and Half Turn", "Understand",
       "Students name a turn as a full turn or a half turn by comparing where something faces with where it faced at "
       "the start.",
       textbook=["Ashutosh and Sahana are making circles, each having one foot fixed and rotating at one spot on the "
                 "ground.",
                 "Ashutosh made a complete circle by making a full turn. Sahana is making a half-moon shape with a "
                 "half turn.",
                 "The minute hand makes a full turn when it comes back to the initial position."],
       teach=["Predict first: Sahana stands on one spot with one foot fixed and turns until she faces the same way as "
              "at the start. How much has she turned?",
              "She has made a full turn. Her free foot drew a complete circle on the ground, and she is back at the "
              "starting position.",
              "If she turns only until she faces the opposite way, her free foot draws a half-moon shape. That is a "
              "half turn.",
              "The minute hand of a clock makes a full turn too. It makes a full turn when it comes back to the "
              "initial position.",
              "Rule: a full turn brings you back to where you started. A half turn leaves you facing the opposite "
              "way."],
       examples=[WE("Sahana stands on one spot facing the classroom door, with one foot fixed. (a) She turns until she "
                    "faces the door again. What turn is it? (b) She starts again and turns until her back is to the "
                    "door. What turn is it?",
                    ["The start: Sahana faces the door.",
                     "(a): She turns and faces the door again. She is back at the starting position, so it is a full "
                     "turn. Her free foot has drawn a complete circle.",
                     "(b): She turns until her back is to the door. She faces the opposite way, so it is a half "
                     "turn. Her free foot has drawn a half-moon.",
                     "Check: a full turn ends where it began, and a half turn ends facing the other way."],
                    "(a): a full turn; (b): a half turn")],
       ncert=["open.circles", "open.minute"], key_terms=["full turn", "half turn", "starting position"],
       misconceptions=["M_SAME_FACING_NO_TURN"], minutes=5),
     DOER("T1B.C2", "Practice: The Statue Game", None, "Understand",
          "Students name which child in the statue game made a full turn and which made a half turn, and explain the "
          "answer by comparing each child with the start.",
          ["A full turn brings you back to the starting position.",
           "A half turn leaves you facing the opposite way.",
           "Compare where each child faces now with where the child faced at the start."],
          items=[FIO("open.statue", "Statue Game: full turn and half turn",
                     "Can you recognise the child in the picture who has made a full turn? Who has made a half turn? "
                     "How do you know? Discuss in class.",
                     ["In the first picture all four children face the front. That is the starting position.",
                      "A full turn brings a child back to the starting position, so the child faces the front again.",
                      "B and C face the front again, so B and C have made a full turn.",
                      "A half turn leaves a child facing the opposite way. A faces away from the front, so A has made "
                      "a half turn.",
                      "D faces the side, so D has made neither a full turn nor a half turn.",
                      "Check: B and C face the same way as at the start, and A faces the opposite way."],
                     "A made a half turn, because A faces the opposite way. B and C made a full turn, because they "
                     "face the way they faced at the start.",
                     kind="prompt",
                     q_figure="Two pictures of four children, A, B, C and D, standing in a row. In the first picture "
                              "all four face the front. In the second picture, after the call STATUE, A faces away, B "
                              "and C face the front and D faces the side.",
                     s_figure="The second picture with A marked half turn, B and C marked full turn and D marked "
                              "neither.")],
          misconceptions=["M_SAME_FACING_NO_TURN"])],
    key_terms=["full turn", "half turn", "starting position"]))

# ============================== T2 Halves and Quarters Make a Full Turn ====================================
# 9 Nov 2026 (teacher feedback): the old topic "Quarter Turns and Everyday Turns" is split into two learning topics,
# one idea and one video each. The single tool Quarter Turn Check sits in the second topic with two separated activities.
TOPICS.append(TOPIC(
    "T2", "M1", "Halves and Quarters Make a Full Turn", ["Giant wheel"], "Apply",
    "Students find the turn made when half turns and quarter turns are joined in the same direction.",
    "Two half turns, or four quarter turns, make a full turn, and two quarter turns make a half turn.",
    [A("T2.C1", "Halves and Quarters Make a Full Turn", "Apply",
       "Students find the turn made when half turns and quarter turns are joined in the same direction.",
       textbook=["A giant wheel makes a full turn when it comes back to the starting position E."],
       teach=["Predict first: a seat on the giant wheel takes a half turn and then another half turn in the same "
              "direction. Where is the seat now?",
              "A giant wheel makes a full turn when it comes back to the starting position E.",
              "A half turn takes the seat half way round. Another half turn in the same direction takes it the rest "
              "of the way, back to E. Two half turns make a full turn.",
              "A quarter turn is 1/4 of a full turn. Four quarter turns make 4/4, a full turn. Two quarter turns make "
              "2/4, which is the same as 1/2: a half turn.",
              "Rule: 2 half turns make 1 full turn, 4 quarter turns make 1 full turn, and 2 quarter turns make 1 half "
              "turn."],
       examples=[WE("A seat on the giant wheel takes 1 half turn and then 2 quarter turns, all in the same direction. "
                    "What turn is that in all?",
                    ["A half turn is 1/2 of a full turn. Two quarter turns are 2/4, which is 1/2.",
                     "In all: 1/2 + 2/4 = 1/2 + 1/2 = 2/2 = 1.",
                     "1 is a full turn, so the seat is back at the starting position E.",
                     "Check: 1 half turn is 2 quarter turns, so the seat made 2 + 2 = 4 quarter turns, and 4 quarter "
                     "turns make a full turn."],
                    "A full turn, so the seat is back at E")],
       ncert=["turn.wheel"], key_terms=["quarter turn", "half turn", "full turn"],
       misconceptions=["M_BIGGER_DENOM_TURN"], minutes=5),
     DOER("T2.C2", "Practice: Halves and Quarters of a Turn", None, "Apply",
          "Students find the turn made when half turns and quarter turns are joined in the same direction on the "
          "giant wheel.",
          ["Two half turns, or four quarter turns, make a full turn.",
           "Two quarter turns make a half turn."],
          items=[FIO("reema.half", "Reema's Giant Wheel: two half turns",
                     "A giant wheel makes a full turn when it comes back to the starting position E. Reema takes two "
                     "half turns in the same direction. It is like a ___ turn.",
                     ["A half turn is 1/2 of a full turn.",
                      "Two half turns in the same direction: 1/2 + 1/2 = 2/2 = 1.",
                      "1 is a full turn, so the seat is back at the starting position E.",
                      "Check: the first half turn takes the seat half way round and the second takes it the rest of "
                      "the way."],
                     "A full turn, because 1/2 + 1/2 = 1.",
                     kind="prompt",
                     q_figure="A giant wheel with a seat at the top marked E, and Reema standing beside it.",
                     s_figure="The wheel with two half turns drawn as two curved arrows, the seat back at E, and the "
                              "words 1/2 + 1/2 = 1 full turn."),
                 FIO("reema.quarter2", "Reema's Giant Wheel: two quarter turns",
                     "A giant wheel makes a full turn when it comes back to the starting position E. What happens if "
                     "Reema takes 2 quarter turns in the same direction? It is like a ___ turn.",
                     ["A quarter turn is 1/4 of a full turn.",
                      "Two quarter turns in the same direction: 1/4 + 1/4 = 2/4.",
                      "2/4 is the same as 1/2, because 2 ÷ 2 = 1 and 4 ÷ 2 = 2.",
                      "So two quarter turns are a half turn.",
                      "Check: two quarter turns take the seat half way round, and a half turn is half way round."],
                     "A half turn, because 1/4 + 1/4 = 2/4 = 1/2.",
                     kind="prompt",
                     q_figure="A giant wheel with a seat at the top marked E, and Reema standing beside it.",
                     s_figure="The wheel with two quarter turns drawn as two curved arrows, the seat at the bottom, "
                              "and the words 1/4 + 1/4 = 1/2."),
                 FIO("reema.quarter4", "Reema's Giant Wheel: four quarter turns",
                     "A giant wheel makes a full turn when it comes back to the starting position E. What happens if "
                     "Reema takes 4 quarter turns in the same direction? It is like a ___ turn.",
                     ["Four quarter turns in the same direction: 1/4 + 1/4 + 1/4 + 1/4 = 4/4.",
                      "4/4 = 1, so it is a full turn.",
                      "The seat is back at the starting position E.",
                      "Check: two quarter turns make a half turn, and two half turns make a full turn, so four "
                      "quarter turns make a full turn."],
                     "A full turn, because 4/4 = 1.",
                     kind="prompt",
                     q_figure="A giant wheel with a seat at the top marked E, and Reema standing beside it.",
                     s_figure="The wheel with four quarter turns drawn as four curved arrows, the seat back at E, and "
                              "the words 4 quarter turns = 1 full turn.")],
          misconceptions=["M_BIGGER_DENOM_TURN"])],
    key_terms=["quarter turn", "half turn", "full turn"]))

# ============================== T2B Objects That Turn ======================================================
TOPICS.append(TOPIC(
    "T2B", "M1", "Objects That Turn", ["Everyday objects"], "Apply",
    "Students compare the greatest turn of an everyday object with a quarter turn and say whether it is less than, "
    "equal to or more than a quarter turn.",
    "An everyday object can turn only so far. Its greatest turn can be compared with a quarter turn: less, equal or "
    "more.",
    [A("T2B.C1", "Objects That Turn", "Understand",
       "Students compare the greatest turn of an object with a quarter turn and say whether it is less than, equal to "
       "or more than a quarter turn.",
       teach=["Predict first: a door opens on its hinge. Can it turn more than a quarter turn?",
              "Many everyday things turn: a tap, a door on its hinge, a clothes clip, tongs, scissors, a file cover.",
              "Each one can turn only so far. The greatest turn it can make is its maximum turn.",
              "To check, use a quarter turn as a guide. A quarter turn makes a square corner, like the corner of a "
              "book. Open the object as far as it goes and compare it with the corner.",
              "If it opens less than the corner, it turns less than a 1/4 turn. If it opens exactly to the corner, it "
              "turns a 1/4 turn. If it opens wider than the corner, it turns more than a 1/4 turn.",
              "Rule: compare the greatest turn of an object with a quarter turn: less, equal or more."],
       examples=[WE("Three practice hinges, P, Q and R, are opened as far as they go (a practice picture). P opens "
                    "exactly to the corner of a book. Q opens less than the corner. R opens wider than the corner. "
                    "Compare the greatest turn of each with a quarter turn.",
                    ["The corner of a book is a quarter turn, so it is the guide.",
                     "P opens exactly to the corner: its greatest turn is a 1/4 turn.",
                     "Q opens less than the corner: its greatest turn is less than a 1/4 turn.",
                     "R opens wider than the corner: its greatest turn is more than a 1/4 turn.",
                     "Check: all three hinges were compared with the same guide, the corner of a book."],
                    "P: a 1/4 turn; Q: less than a 1/4 turn; R: more than a 1/4 turn")],
       key_terms=["quarter turn", "greatest turn", "everyday objects"],
       misconceptions=["M_ARM_LENGTH"], minutes=5),
     DOER("T2B.C2", "Practice: Quarter Turn Check", "quarter_turn_check", "Apply",
          "Students join half turns and quarter turns on the wheel, and tick whether the greatest turn of an object is "
          "less than, equal to or more than a 1/4 turn.",
          ["Recap: two half turns, or four quarter turns, make a full turn.",
           "Compare the greatest turn of an object with a quarter turn: less, equal or more."],
          items=[FIO("objects.list", "Everyday Turns: objects that turn",
                     "Write some of the everyday objects that involve turns. For example, taps, ___, ___, ___, ___, "
                     "and ___.",
                     ["Think of things that turn on a spot or on a hinge.",
                      "From your maths book: a tap, a door on its hinge, a clothes clip, tongs, scissors, a file "
                      "cover, a clock hand, a giant wheel, a lid, a nut.",
                      "Pick five of them to write after taps.",
                      "Check: each one swings or spins round a fixed point."],
                     "Sample answer: door, scissors, clock hand, giant wheel, lid. Your answer may differ.",
                     kind="prompt"),
                 FIO("objects.table", "Everyday Turns: the greatest turn",
                     "What is the maximum possible turn in each of these cases? Check and tick: less than a 1/4 turn, "
                     "1/4 turn, or more than a 1/4 turn. (a) Clothes clip; (b) Door with hinge; (c) Tongs; (d) Scissors; "
                     "(e) File cover",
                     ["Use a quarter turn, the corner of a book, as the guide. Open each object as far as it goes and "
                      "compare.",
                      "(a): the clothes clip opens only a little, less than the corner: less than a 1/4 turn.",
                      "(b): the door with hinge swings wider than the corner: more than a 1/4 turn.",
                      "(c): the tongs open less than the corner: less than a 1/4 turn.",
                      "(d): the scissors open about to the corner: a 1/4 turn.",
                      "(e): the file cover opens wider than the corner, even flat: more than a 1/4 turn.",
                      "Check: these are sample ticks for common objects. Your own objects may differ a little, so "
                      "check them with the corner of a book."],
                     "Sample answer: (a): less than 1/4; (b): more than 1/4; (c): less than 1/4; (d): 1/4; "
                     "(e): more than 1/4. Your answer may differ.",
                     kind="prompt",
                     q_figure="A table with five rows, clothes clip, door with hinge, tongs, scissors and file cover, "
                              "and three empty columns headed less than a 1/4 turn, 1/4 turn and more than a 1/4 "
                              "turn."),
                 FIO("objects.half", "Everyday Turns: half turn objects",
                     "Do any of the objects in the table (clothes clip, door with hinge, tongs, scissors, file cover) "
                     "make a half turn? Write their names.",
                     ["A half turn is two quarter turns, so the arm and the start lie in one straight line.",
                      "A door can swing open until it is flat against the wall: a half turn.",
                      "A file cover can open until it lies flat on the table: a half turn.",
                      "A clothes clip, tongs and scissors cannot open that far.",
                      "Check: only the objects that open flat make a half turn."],
                     "Sample answer: the door with hinge and the file cover. Your answer may differ.",
                     kind="prompt"),
                 FIO("objects.full", "Everyday Turns: full turn objects",
                     "Do any of the objects in the table (clothes clip, door with hinge, tongs, scissors, file cover) "
                     "make a full turn? Write their names.",
                     ["A full turn brings the object back to where it started.",
                      "A hinge stops when the door, the cover or the blades meet each other or the wall. It cannot "
                      "go all the way round.",
                      "The clothes clip, the door, the tongs, the scissors and the file cover all stop before a full "
                      "turn.",
                      "Check: none of the five turns round and round like a wheel."],
                     "Sample answer: none of the five. Your answer may differ.",
                     kind="prompt")],
          misconceptions=["M_ARM_LENGTH"])],
    key_terms=["quarter turn", "greatest turn", "everyday objects"]))

# ============================== T3 Angles from Turns =======================================================
TOPICS.append(TOPIC(
    "T3", "M1", "Angles from Turns", ["Pragya's straws", "Paper fan", "Let Us Do"], "Understand",
    "Students show and name right, acute, obtuse and straight angles as turns of a straw or a paper fan, and say when a "
    "turn is more than a straight angle.",
    "An angle arises when something turns. A quarter turn makes a right angle, less than a quarter turn an acute angle, "
    "more than a quarter and less than a half turn an obtuse angle, and a half turn a straight angle.",
    [A("T3.C1", "Right, Acute and Obtuse Angles", "Understand",
       "Students name a turn from a fixed straw as a right, acute or obtuse angle by comparing it with a quarter turn.",
       textbook=["Pragya joined a green and yellow straw with paper clips. She holds the green straw steady and turns "
                 "the yellow straw around. Observe different turns of the yellow straw.",
                 "I made a quarter (1/4) of a full turn, so it looks like a right angle.",
                 "I made less than a quarter turn, so it looks like an acute angle.",
                 "Now I made more than a quarter turn, but less than a half turn. That looks like an obtuse angle.",
                 "Angles arise in situations that involve a turn.",
                 "Making a paper fan. Take a rectangular paper, fold every 2 cm as shown in the picture. Paste ice "
                 "cream sticks as shown below to create a paper fan."],
       teach=["Predict first: Pragya holds a green straw steady and turns a yellow straw a quarter turn. What does "
              "the corner between the two straws look like?",
              "Pragya joined a green and a yellow straw with a paper clip. She holds the green straw steady and turns "
              "the yellow straw around.",
              "A quarter turn, 1/4 of a full turn, makes a right angle. It looks like the corner of a book.",
              "Less than a quarter turn makes an acute angle. It is narrower than a right angle.",
              "More than a quarter turn but less than a half turn makes an obtuse angle. It is wider than a right "
              "angle.",
              "Angles arise in situations that involve a turn. A paper fan, made from folded paper and two ice cream "
              "sticks, shows the same angles when it opens.",
              "Rule: a 1/4 turn is a right angle, less than a 1/4 turn is an acute angle, and more than a 1/4 turn "
              "but less than a 1/2 turn is an obtuse angle."],
       examples=[WE("Pragya opens her paper fan to three places. At X the two end sticks make exactly a quarter turn. "
                    "At Y they make a little less than a quarter turn. At Z they make more than a quarter turn but "
                    "less than a half turn. Name the angle at X, at Y and at Z.",
                    ["The guide is a quarter turn, a square corner.",
                     "X is exactly a quarter turn: a right angle.",
                     "Y is less than a quarter turn: an acute angle.",
                     "Z is more than a quarter turn and less than a half turn: an obtuse angle.",
                     "Check: X, Y and Z were all compared with the same quarter turn."],
                    "X: a right angle; Y: an acute angle; Z: an obtuse angle")],
       ncert=["straws.setup", "angles.names", "angles.arise", "fan.make"],
       key_terms=["right angle", "acute angle", "obtuse angle", "quarter turn"],
       misconceptions=["M_ARM_LENGTH"], minutes=6),
     A("T3.C2", "Straight Angle and More Than a Straight Angle", "Understand",
       "Students name a half turn as a straight angle and a turn of 3/4 as more than a straight angle.",
       textbook=["I made two quarter turns. I wonder what it is called?", "It is a straight angle.",
                 "Let us look at the turns made by the paper fan, keeping one side fixed.",
                 "This shows a 1/4 turn, or a right angle.", "This shows a 1/2 turn, or a straight angle.",
                 "This shows a 3/4 turn, which is more than a straight angle."],
       teach=["Predict first: Pragya turns the yellow straw a quarter turn, then another quarter turn the same way. "
              "What do the two straws look like now?",
              "Two quarter turns make a half turn: 1/4 + 1/4 = 2/4 = 1/2. The two straws lie in one straight line. "
              "This angle is called a straight angle.",
              "A 3/4 turn is more than a half turn, so it is more than a straight angle.",
              "A full turn brings the straw back to where it started.",
              "The paper fan shows them all with one side fixed: a full turn, a 1/2 turn (a straight angle), a 1/4 "
              "turn (a right angle), less than a 1/4 turn (an acute angle), and between a 1/4 and a 1/2 turn (an "
              "obtuse angle).",
              "Rule: a 1/2 turn is a straight angle, and a 3/4 turn is more than a straight angle."],
       examples=[WE("Pragya's paper fan opens by a half turn and then by one more quarter turn in the same direction. "
                    "What turn is that in all, and how does it compare with a straight angle?",
                    ["A half turn is 1/2 and a quarter turn is 1/4. 1/2 is the same as 2/4.",
                     "In all: 2/4 + 1/4 = 3/4.",
                     "A straight angle is a 1/2 turn, which is 2/4. 3/4 is more than 2/4.",
                     "So the turn is 3/4, more than a straight angle.",
                     "Check: 3 quarter turns are one quarter turn short of a full turn."],
                    "A 3/4 turn, more than a straight angle")],
       ncert=["angles.straight", "fan.table", "fan.circles"],
       key_terms=["straight angle", "half turn", "3/4 turn"],
       misconceptions=["M_STRAIGHT_NOT_ANGLE"], minutes=6),
     DOER("T3.C3", "Practice: Straw and Fan Angles", "straw_fan_angles", "Understand",
          "Students show acute and obtuse angles with a turning fan, and name right, acute, obtuse and straight angles in "
          "pictures.",
          ["A 1/4 turn is a right angle, less than a 1/4 turn is acute, and more than a 1/4 and less than a 1/2 turn "
           "is obtuse.",
           "A 1/2 turn is a straight angle.",
           "Compare each angle with a quarter turn, a square corner."],
          items=[FIO("LUDa.fan", "Let Us Do (angles), (a)",
                     "Use your paper fan to show different acute angles and obtuse angles.",
                     ["Hold one stick of the fan still. This is the starting line.",
                      "Open the fan a little, less than a quarter turn: an acute angle.",
                      "Open it to a quarter turn, a square corner: a right angle.",
                      "Open it a bit more, more than a quarter turn but less than a half turn: an obtuse angle.",
                      "Check: each angle was compared with a quarter turn."],
                     "Sample answer: less than a 1/4 turn is acute; between a 1/4 and a 1/2 turn is obtuse. Your "
                     "answer may differ.",
                     kind="exercise",
                     q_figure="A paper fan of folded green paper with an ice cream stick at each end, opened at three "
                              "different widths.",
                     s_figure="The fan opened to less than a quarter turn, a quarter turn and between a quarter and "
                              "a half turn, each angle marked with a red arc."),
                 FIO("fan.acute2", "Let Us Do (angles), (a) two acute turns",
                     "Make an acute turn with the straws or fan. Continue to make another acute turn. Can the two "
                     "acute turns together make another acute turn?",
                     ["An acute turn is less than a quarter turn.",
                      "Make two small acute turns, one after the other. Together they can still be less than a "
                      "quarter turn: acute.",
                      "Make two bigger turns that are each almost a quarter turn. Together they are more than a "
                      "quarter turn, so the angle can be obtuse.",
                      "Two acute turns can also add up to exactly a quarter turn: a right angle.",
                      "So it depends on how big each turn is."],
                     "Sometimes. Two small acute turns together can be acute; two bigger ones can make a right angle "
                     "or an obtuse angle.",
                     kind="exercise",
                     q_figure="A green straw held steady and a yellow straw joined to it, turned once and then turned "
                              "again.",
                     s_figure="Two examples: two small acute turns that together are still acute, and two bigger "
                              "acute turns that together make an obtuse angle."),
                 FIO("LUDb.house", "Let Us Do (angles), (b)",
                     "You might have built houses using the hard covers of notebooks or cardboard pieces. Look at the "
                     "angles marked in the house. What angles are you able to see in this house? Write your answers "
                     "as right, acute or obtuse angle. A: ___; B: ___; C: ___; D: ___; E: ___; F: ___; G: ___; H: ___",
                     ["Compare each marked angle with a quarter turn, a square corner.",
                      "A: the roof books open wider than a square corner: obtuse.",
                      "B: a book standing on a flat book makes a square corner: right.",
                      "C: the two leaning books meet in a narrow point: acute.",
                      "D: the leaning book against the upright book is narrower than a square corner: acute.",
                      "E: the leaning book meets the upright book in a narrow angle: acute.",
                      "F: an upright book on the flat book: right.",
                      "G: an upright book on the flat book: right.",
                      "H: the leaning book meets the flat book in a wide angle: obtuse.",
                      "Check: 3 right angles, 3 acute angles and 2 obtuse angles make 3 + 3 + 2 = 8 angles, one for "
                      "each letter."],
                     "A: obtuse; B: right; C: acute; D: acute; E: acute; F: right; G: right; H: obtuse.",
                     kind="exercise",
                     q_figure="A house built from notebook covers, with eight angles marked by red arcs and labelled "
                              "A to H.",
                     s_figure="The same house with each angle named: A obtuse, B right, C acute, D acute, E acute, F "
                              "right, G right, H obtuse."),
                 FIO("LUDc.pentagon", "Let Us Do (angles), (c)",
                     "Make a 5-sided shape with 2 right angles, 2 obtuse angles, and 1 acute angle in your notebook.",
                     ["Use square paper. Start at the bottom left corner.",
                      "Draw a line 4 squares to the right, then a line 2 squares up.",
                      "Draw a slanting line 2 squares left and 4 squares up.",
                      "Draw a slanting line 2 squares left and 4 squares down.",
                      "Draw a line 2 squares down, back to the start. The shape has 5 sides.",
                      "The two bottom corners are right angles.",
                      "The two corners where the walls meet the roof are wider than a right angle: obtuse.",
                      "The top point is narrower than a right angle: acute.",
                      "Check: 2 right angles, 2 obtuse angles and 1 acute angle make 2 + 2 + 1 = 5 angles, one for "
                      "each of the 5 sides."],
                     "Sample answer: a house shape with 2 right angles, 2 obtuse angles and 1 acute angle. Your "
                     "shape may differ.",
                     kind="exercise",
                     s_figure="A five-sided house shape drawn on a square grid with its two right angles, two obtuse "
                              "angles and one acute angle marked."),
                 FIO("LUDd.gymnasts", "Let Us Do (angles), (d)",
                     "Look at the angle formation between the legs of these gymnasts. Identify whether the angles "
                     "are acute, obtuse, right or straight.",
                     ["Compare each angle between the legs with a quarter turn.",
                      "Top picture: narrower than a square corner: acute.",
                      "Second picture: exactly a square corner: right.",
                      "Third picture: wider than a square corner but not a straight line: obtuse.",
                      "Fourth picture: wider still, nearly a straight line, but not straight: obtuse.",
                      "Fifth picture: the legs are in one straight line, a half turn: straight.",
                      "Check: the angles grow from picture to picture, from acute to straight."],
                     "Top to bottom: acute, right, obtuse, obtuse, straight.",
                     kind="exercise",
                     q_figure="Five pictures of a gymnast with the legs apart, in a column, each beside an empty box "
                              "and a drawing of the angle between the legs.",
                     s_figure="The five angles named: acute, right, obtuse, obtuse, straight.")],
          misconceptions=["M_ARM_LENGTH", "M_ACUTE_ADD_ACUTE", "M_STRAIGHT_NOT_ANGLE"])],
    key_terms=["angle", "right angle", "acute angle", "obtuse angle", "straight angle"]))
