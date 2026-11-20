# -*- coding: utf-8 -*-
"""Topics T6 (module M2), T7 and T8 (module M3): The Minute Hand Turns, Which Direction? (with Fun with Turns) and the
chapter revision (a summary topic, no video). Every teaching concept has one worked example with the plan's own numbers;
every book question is an FIO item of its topic's DOER, in the book's order. A turn is a fraction of a full turn: no
degrees anywhere."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T6 The Minute Hand Turns ===================================================
TOPICS.append(TOPIC(
    "T6", "M2", "The Minute Hand Turns", ["Let Us Do, question 6"], "Apply",
    "Students find the turn a minute hand makes from the minutes it moves, and the minutes from the turn, and mark "
    "where the hand stops.",
    "The minute hand makes a full turn in 60 minutes. So 15 minutes is a 1/4 turn, 30 minutes a 1/2 turn, 45 minutes a "
    "3/4 turn, and 5 minutes a 1/12 turn. The hand turns from the place where it starts.",
    [A("T6.C1", "Minutes and Turns of the Minute Hand", "Apply",
       "Students find the turn the minute hand makes from the minutes it moves, find the minutes from the turn, and "
       "say where the hand stops.",
       teach=["Predict first: the minute hand moves for 15 minutes. What part of a full turn has it made?",
              "The minute hand makes a full turn in 60 minutes. It comes back to where it started.",
              "A 1/12 turn is 60 ÷ 12 = 5 minutes. So going from one number of the clock to the next is a 1/12 turn.",
              "15 minutes is a 1/4 turn, because 15 × 4 = 60. 30 minutes is a 1/2 turn, 45 minutes is a 3/4 turn and "
              "60 minutes is a full turn.",
              "The hand turns from where it starts, not always from 12. To find where it stops, move it the minutes "
              "the way a clock moves from its starting place.",
              "Rule: 60 minutes is a full turn, 5 minutes is a 1/12 turn, and the hand turns from where it starts."],
       examples=[WE("The minute hand starts at the number 2 and moves 25 minutes. What turn does it make, and where "
                    "does it stop?",
                    ["The hand starts at 2, which is the 10 minute mark, because 2 × 5 = 10.",
                     "A 1/12 turn is 5 minutes. 25 minutes is 25 ÷ 5 = 5 of these.",
                     "So the turn is 5/12 of a full turn.",
                     "The hand stops at the 10 + 25 = 35 minute mark.",
                     "35 ÷ 5 = 7, so the hand stops at the number 7.",
                     "Check: from 2 to 7 is 5 numbers, and each step from one number to the next is a 1/12 turn, so "
                     "the turn is 5/12."],
                    "A 5/12 turn; the hand stops at 7")],
       key_terms=["minute hand", "full turn", "minutes"],
       misconceptions=["M_CLOCK_FROM_12"], minutes=6),
     DOER("T6.C2", "Practice: Minute Hand Turner", "minute_hand_turner", "Apply",
          "Students find the turn or the minutes for each movement of the minute hand and mark where the hand stops.",
          ["A full turn of the minute hand is 60 minutes.",
           "A 1/12 turn is 5 minutes.",
           "The hand turns from the place where it starts."],
          items=[FIO("LUD2.Q6", "Let Us Do (minute hand), Q6",
                     "Guess the measure of turns the minute hand of a clock makes in each of the following cases. "
                     "The initial position of the minute hand is given. Draw the final position of the minute hand "
                     "on the clock face. Discuss your reasoning in class. (a) When the minute hand moves by 15 "
                     "minutes, it has made a ___ turn of the circle. (b) When the minute hand moves by 30 minutes, "
                     "it has made a ___ turn of the circle. (c) When the minute hand moves by 45 minutes, it has "
                     "made a ___ turn of the circle. (d) When the minute hand has turned by 1/12 of a full turn, it "
                     "has moved by ___ minutes. (e) When the minute hand has turned a full-circle, it has moved by "
                     "___ minutes. (f) When the minute hand has turned by 1/6 of a full turn, it has moved by ___ "
                     "minutes. (g) When the minute hand has turned by 4/12 of a full turn, it has moved by ___ "
                     "minutes.",
                     ["A full turn of the minute hand is 60 minutes. A 1/12 turn is 5 minutes.",
                      "(a): 15 minutes: 15 × 4 = 60, so it is a 1/4 turn. The hand starts at 3 and stops at 6.",
                      "(b): 30 minutes: 30 × 2 = 60, so it is a 1/2 turn. From 6 the hand stops at 12.",
                      "(c): 45 minutes: 3 × 15 = 45, so it is 3 quarter turns, a 3/4 turn. From 9 the hand stops at "
                      "6.",
                      "(d): a 1/12 turn is 60 ÷ 12 = 5 minutes. From 1 the hand stops at 2.",
                      "(e): a full circle is 60 minutes. The hand starts and stops at 12.",
                      "(f): a 1/6 turn is 60 ÷ 6 = 10 minutes. From 2 the hand stops at 4.",
                      "(g): a 4/12 turn is 4 × 5 = 20 minutes, because one 1/12 turn is 60 ÷ 12 = 5 minutes. From 4 "
                      "the hand stops at 8.",
                      "Check: 4/12 is the same as 1/3, and 20 × 3 = 60."],
                     "(a): 1/4; (b): 1/2; (c): 3/4; (d): 5; (e): 60; (f): 10; (g): 20.",
                     kind="exercise",
                     q_figure="Seven clock faces, one for each part, with the minute hand at its starting place: (a) "
                              "at 3, (b) at 6, (c) at 9, (d) at 1, (e) at 12, (f) at 2, (g) at 4.",
                     s_figure="The same seven clocks with the final place of the minute hand drawn: (a) at 6, (b) at "
                              "12, (c) at 6, (d) at 2, (e) at 12, (f) at 4, (g) at 8.")],
          misconceptions=["M_CLOCK_FROM_12"])],
    key_terms=["minute hand", "full turn", "minutes"]))

# ============================== T7 Which Direction? ========================================================
TOPICS.append(TOPIC(
    "T7", "M3", "Which Direction?", ["Which direction?", "Fun with Turns"], "Apply",
    "Students tell whether a turn is clockwise or anti-clockwise, and find the direction faced after turns of right "
    "angles from North, East, South or West.",
    "The way the hands of a clock move is clockwise, and the opposite way is anti-clockwise. On a compass, each right "
    "angle is a quarter turn, and four right angles bring you back to where you started.",
    [A("T7.C1", "Clockwise and Anti-clockwise", "Understand",
       "Students tell whether a turn is clockwise or anti-clockwise by comparing it with the way the hands of a clock "
       "move.",
       textbook=["The direction in which the hands of the clock move is called clockwise movement. The opposite "
                 "movement is called anti-clockwise movement."],
       teach=["Predict first: an arrow points down and makes a quarter turn to point left. Is it turning the way the "
              "hands of a clock move?",
              "The hands of a clock move round from 12 to 1 to 2 and on. The direction in which the hands of a clock "
              "move is called clockwise movement.",
              "The opposite movement is called anti-clockwise movement.",
              "Find the turn on the clock face. From 6 to 9 is the way a clock moves, so it is clockwise. From 9 to 6 "
              "is the other way, so it is anti-clockwise.",
              "Rule: with the hands of a clock is clockwise, and against them is anti-clockwise."],
       examples=[WE("An arrow points down. It makes a quarter turn and now points left. Is the turn clockwise or "
                    "anti-clockwise?",
                    ["Think of the arrow as a clock hand pointing at 6, straight down.",
                     "Left is the 9 on a clock.",
                     "A clock hand goes from 6 to 7, 8 and 9. That is the way a clock moves.",
                     "So the turn is clockwise.",
                     "Check: the other way from 6 is 5, 4 and 3, which points right, not left."],
                    "Clockwise")],
       ncert=["dir.def"], key_terms=["clockwise", "anti-clockwise", "direction"],
       minutes=5),
     A("T7.C2", "Finding the Final Direction After Right-Angle Turns", "Apply",
       "Students find the direction faced after turns of right angles, clockwise or anti-clockwise, from North, East, "
       "South or West.",
       teach=["Predict first: you face West and turn 3 right angles anti-clockwise. Which direction do you face?",
              "The four directions are North at the top, East on the right, South at the bottom and West on the left. "
              "A right angle is a quarter turn.",
              "Recap: clockwise goes North, East, South, West, North, and so on. Anti-clockwise goes the other way: "
              "North, West, South, East, North.",
              "Count the right angles one by one. Two right angles are a half turn. Four right angles are a full "
              "turn and bring you back to where you started.",
              "A half turn ends in the same place either way, but a quarter turn does not.",
              "A 1/2 right angle is half of a right angle. Two of them make 1 right angle.",
              "Rule: count the right angles in the turn, move that many directions clockwise or anti-clockwise, and "
              "four right angles bring you back."],
       examples=[WE("Padma faces West and turns 3 right angles anti-clockwise. Which direction does she face?",
                    ["Anti-clockwise from West, the order is West, South, East, North.",
                     "1 right angle anti-clockwise: South.",
                     "2 right angles: East.",
                     "3 right angles: North.",
                     "So she faces North.",
                     "Check: 3 right angles anti-clockwise is the same as 1 right angle clockwise, because 3 + 1 = 4. "
                     "West turned 1 right angle clockwise is North."],
                    "North")],
       key_terms=["right angle", "direction", "clockwise", "anti-clockwise"],
       misconceptions=["M_DIR_SAME_END"], minutes=6),
     DOER("T7.C3", "Practice: Turn and Face", "turn_and_face", "Apply",
          "Students tick the direction of a quarter turn, fill in the ending direction after turns of right angles, and "
          "find the place faced after a half turn.",
          ["Clockwise is the way the hands of a clock move. The opposite is anti-clockwise.",
           "Clockwise goes North, East, South, West. A right angle is a quarter turn, one step.",
           "Four right angles are a full turn and two right angles are a half turn."],
          items=[FIO("dir.creatures", "Which Direction: four creatures",
                     "The creatures below have made a quarter turn once. Tick the direction in which they have "
                     "moved. (a) ladybug (Clockwise/Anti-clockwise); (b) snail (Clockwise/Anti-clockwise); (c) bee "
                     "(Clockwise/Anti-clockwise); (d) ant (Clockwise/Anti-clockwise)",
                     ["Clockwise is the way the hands of a clock move. Think of the creature's face as a clock hand.",
                      "(a): the ladybug faces left, the 9, then up, the 12. 9 to 12 is the way a clock moves: "
                      "clockwise.",
                      "(b): the snail's head is down, the 6, then left, the 9. 6 to 9 is clockwise.",
                      "(c): the bee faces left, the 9, then down, the 6. 9 to 6 is against the clock: anti-clockwise.",
                      "(d): the ant faces up, the 12, then left, the 9. 12 to 9 is against the clock: "
                      "anti-clockwise.",
                      "Check: each creature made 1 quarter turn, which is 3 numbers on the clock."],
                     "(a): clockwise; (b): clockwise; (c): anti-clockwise; (d): anti-clockwise.",
                     kind="prompt",
                     q_figure="Four boxes, each with a creature before and after a quarter turn and an arrow between: "
                              "a ladybug faces left, then up; a snail has its head down, then to the left; a bee "
                              "faces left, then down; an ant faces up, then left.",
                     s_figure="The four boxes with the answer ticked: ladybug clockwise, snail clockwise, bee "
                              "anti-clockwise, ant anti-clockwise."),
                 FIO("dir.try", "Which Direction: tap, lid and nut",
                     "Observe the direction of movement while opening a tap, unscrewing a lid or loosening a nut. "
                     "Do they move clockwise or anti-clockwise?",
                     ["Turn a real tap, lid or nut the way it opens, and watch which way it goes.",
                      "To open a tap, unscrew a lid or loosen a nut, the usual turn is anti-clockwise.",
                      "To close a tap, screw on a lid or tighten a nut, the usual turn is clockwise.",
                      "Check: opening and closing are opposite turns, so one is clockwise and the other is "
                      "anti-clockwise."],
                     "Sample answer: usually anti-clockwise for all three. Your tap may differ.",
                     kind="prompt"),
                 FIO("FWT.Q1", "Fun with Turns: Q1",
                     "The children in a class are playing a game in which the teacher tells them the direction in "
                     "which they should rotate. Complete the table by filling the direction the children will face "
                     "on completing the given turns. The starting direction is given in the table. (a) North, two "
                     "right angles clockwise; (b) South, two right angles anti-clockwise; (c) East, four right angles "
                     "anti-clockwise; (d) West, four right angles clockwise; (e) North, 5 right angles clockwise; (f) "
                     "South, 3 right angles clockwise, 1/2 right angle clockwise, 1/2 right angle clockwise; (g) "
                     "West, ___ right angles clockwise, four 1/2 right angles anti-clockwise",
                     ["The directions go clockwise: North, East, South, West. A right angle is a quarter turn, one "
                      "step.",
                      "(a): North, 2 right angles clockwise: East, then South. It ends at South.",
                      "(b): South, 2 right angles anti-clockwise: East, then North. It ends at North.",
                      "(c): East, 4 right angles anti-clockwise: a full turn, back at East.",
                      "(d): West, 4 right angles clockwise: a full turn, back at West.",
                      "(e): North, 5 right angles clockwise: 4 of them are a full turn, and 5 − 4 = 1 more takes it "
                      "to East.",
                      "(f): South, 3 + 1/2 + 1/2 = 4 right angles clockwise: a full turn, back at South.",
                      "(g): West. Four 1/2 right angles are 2 right angles anti-clockwise. The number before "
                      "'right angles clockwise' is not printed in your maths book. The end is West turned that "
                      "number minus 2 right angles clockwise. Sample: if it is 3, then 3 − 2 = 1 right angle "
                      "clockwise, and West ends at North.",
                      "Check: (c), (d) and (f) are full turns, so they end where they started."],
                     "(a): South; (b): North; (c): East; (d): West; (e): East; (f): South; (g): the number is not "
                     "printed; if it is 3, North.",
                     kind="exercise",
                     q_figure="A compass with North at the top, East on the right, South at the bottom and West on "
                              "the left, and a table with seven rows of starting direction and turns; the ending "
                              "direction column is empty.",
                     s_figure="The table filled in: South, North, East, West, East, South, and the sample for the "
                              "last row."),
                 FIO("FWT.Q2", "Fun with Turns: Q2",
                     "Padma is facing the toy shop. What place will she face if she takes a half turn clockwise?",
                     ["A half turn is 2 quarter turns.",
                      "Padma faces the toy shop. On her right are the parking sign and the guard, on her left is the "
                      "bookstall, and behind her is the ice cream cart.",
                      "Clockwise, the first quarter turn takes her to face the parking sign.",
                      "The second quarter turn takes her to face the ice cream cart.",
                      "Check: a half turn makes her face the opposite way from the toy shop, and the ice cream cart "
                      "is behind her."],
                     "The ice cream cart.",
                     kind="exercise",
                     q_figure="A street seen from behind Padma, who faces the toy shop. A bookstall is on her left, a "
                              "parking sign and a guard are on her right, and an ice cream cart is behind her.",
                     s_figure="The same street with a curved arrow marked half turn from the toy shop to the ice "
                              "cream cart."),
                 FIO("FWT.Q2b", "Fun with Turns: Q2 another way",
                     "What other way can Padma turn to face the same place?",
                     ["A half turn anti-clockwise is also 2 quarter turns.",
                      "Anti-clockwise, the first quarter turn takes Padma to face the bookstall on her left.",
                      "The second quarter turn takes her to face the ice cream cart.",
                      "So a half turn either way ends at the ice cream cart.",
                      "Check: a half turn clockwise and a half turn anti-clockwise both make her face the opposite "
                      "way."],
                     "A half turn anti-clockwise, 2 quarter turns the other way.",
                     kind="exercise",
                     q_figure="A street seen from behind Padma, who faces the toy shop. A bookstall is on her left, a "
                              "parking sign and a guard are on her right, and an ice cream cart is behind her.",
                     s_figure="The same street with a curved arrow marked half turn anti-clockwise from the toy shop "
                              "to the ice cream cart.")],
          misconceptions=["M_DIR_SAME_END"])],
    key_terms=["clockwise", "anti-clockwise", "right angle", "direction"]))

# ============================== T8 Chapter Revision: Angles as Turns (summary) =============================
TOPICS.append(TOPIC(
    "T8", "M3", "Chapter Revision: Angles as Turns", ["Whole chapter"], "Understand",
    "",
    "A revision of the whole playground of turns: full and half turns, halves and quarters, angle names, eighths, "
    "sixths and twelfths, the minute hand, and clockwise and anti-clockwise.",
    [A("T8.C1", "Chapter Revision: Angles as Turns", "Understand",
       "",
       teach=["Predict first: you have walked all round the playground of turns. Can you say one idea from each stop? "
              "Read the lines below and tick each idea you remembered.",
              "Full turn and half turn: a full turn brings you back to the starting position, and a half turn leaves "
              "you facing the opposite way.",
              "Check: Sahana turns until her back is to the door. Is it a full turn or a half turn? A half turn.",
              "Halves and quarters: 2 half turns make a full turn, 2 quarter turns make a half turn, and 4 quarter "
              "turns make a full turn.",
              "Check: 1 half turn and 2 quarter turns make 1/2 + 2/4 = 1/2 + 1/2 = 1, a full turn.",
              "Everyday objects turn only so far. Compare the greatest turn with a quarter turn: less, equal or more.",
              "Angles arise from turns: a 1/4 turn is a right angle, less than a 1/4 turn is an acute angle, more "
              "than a 1/4 turn and less than a 1/2 turn is an obtuse angle, and a 1/2 turn is a straight angle. A "
              "3/4 turn is more than a straight angle.",
              "Check: a turn of 1/3 is more than 1/4 and less than 1/2. Which kind of angle is it? An obtuse angle.",
              "Measuring turns: a circle in 8 parts gives 1/8 turns, with 2/8 = 1/4, 4/8 = 1/2 and 6/8 = 3/4. A "
              "circle in 6 parts gives 1/6 turns, and half of a 1/6 turn is a 1/12 turn.",
              "Check: how many 1/8 pieces make a quarter turn? 2 pieces, because 2/8 = 1/4.",
              "Measuring angles: lay the pieces side by side and add their turns. 1/6 + 1/12 = 2/12 + 1/12 = 3/12 = "
              "1/4, a right angle.",
              "The minute hand makes a full turn in 60 minutes, so 15 minutes is a 1/4 turn and 5 minutes is a 1/12 "
              "turn.",
              "Check: the minute hand moves 20 minutes. What turn is that? 20 × 3 = 60, so it is a 1/3 turn.",
              "Clockwise is the way the hands of a clock move. The opposite is anti-clockwise.",
              "Check: you face East and turn 2 right angles clockwise. Which direction do you face? East, then "
              "South, then West: you face West."],
       ncert=["summary"], key_terms=["full turn", "angle", "clockwise"], minutes=6,
       enrichment=True)],
    topic_type="summary"))
