# -*- coding: utf-8 -*-
"""Topics T4 and T5 (module M2: Measuring Turns). Measuring turns with a disc (the Angle Measuring Tool in eighths,
sixths and twelfths, with Let Us Think), and measuring and drawing angles with the turn pieces (Let Us Do, questions 1 to
5). Every teaching concept has one worked example with the plan's own numbers; every book question is an FIO item of its
topic's DOER, in the book's order. The only pieces are the ones the chapter names: 1/8, 2/8, 1/6, 2/6 and 1/12 of a turn.
A turn is a fraction of a full turn: no degrees anywhere."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T4 Measuring Turns with a Disc =============================================
TOPICS.append(TOPIC(
    "T4", "M2", "Measuring Turns with a Disc", ["Angle Measuring Tool", "Let Us Think"], "Apply",
    "Students show and read turns on a circle cut into 8 equal parts and into 6 equal parts, and find that 2/8 is a "
    "quarter turn, 4/8 a half turn, 6/8 a 3/4 turn and that half of a 1/6 turn is a 1/12 turn.",
    "A circle cut into equal parts is a turning ruler: each part is a fraction of a full turn. 8 parts give eighths, 6 "
    "parts give sixths, and half of a 1/6 part is a 1/12 part.",
    [A("T4.C1", "Measuring Turns in Eighths", "Apply",
       "Students show a turn on a circle folded into 8 equal parts and read it as a fraction of a full turn, such as "
       "2/8 = 1/4 and 4/8 = 1/2.",
       textbook=["Let us make our tool to measure turns.",
                 "Cut out a circle from a tracing paper and fold it to make 8 equal parts.",
                 "Attach a straw to the centre and mark the starting point as shown.",
                 "Now, cut out 1/8 part and 2/8 parts of the circle and paste them on a thicker paper or board. Use "
                 "these as angle measuring tools."],
       teach=["Predict first: a circle is folded into 8 equal parts and a straw turns 2 parts from the starting point. "
              "What fraction of a full turn is that?",
              "Cut a circle from tracing paper and fold it into 8 equal parts. Attach a straw at the centre and mark "
              "the starting point A.",
              "Each part is 1/8 of a full turn. Turn the straw 1 part: a 1/8 turn. Turn it 2 parts: a 2/8 turn.",
              "2 parts are 2/8, the same as 1/4: a quarter turn, a right angle. A 1/8 turn is half of a quarter turn.",
              "4 parts are 4/8, the same as 1/2: a half turn, a straight angle. 6 parts are 6/8, the same as 3/4. "
              "8 parts are 8/8, a full turn.",
              "You can cut out the 1/8 part and the 2/8 part and paste them on a thicker paper or board to use as "
              "angle measuring tools.",
              "Rule: n parts of the 8 make an n/8 turn. 2/8 = 1/4, 4/8 = 1/2, 6/8 = 3/4 and 8/8 is a full turn."],
       examples=[WE("The straw on the circle with 8 equal parts turns 5 parts, and then 2 more parts in the same "
                    "direction. What turn is that, and how much more is needed for a full turn?",
                    ["Each part is a 1/8 turn.",
                     "5 parts and 2 more parts make 5 + 2 = 7 parts.",
                     "7 parts of the 8 make a 7/8 turn.",
                     "A full turn is 8 parts, and 8 − 7 = 1.",
                     "So 1 more part, a 1/8 turn, completes the full turn.",
                     "Check: 5/8 + 2/8 = 7/8, and 7/8 + 1/8 = 8/8 = 1."],
                    "A 7/8 turn; 1 more part, a 1/8 turn, makes a full turn")],
       ncert=["amt.make", "amt.cut"], key_terms=["1/8 turn", "equal parts", "starting point"],
       misconceptions=["M_BIGGER_DENOM_TURN"], minutes=6),
     A("T4.C2", "Measuring Turns in Sixths and Twelfths", "Apply",
       "Students show 1/6 and 2/6 turns on a circle folded into 6 equal parts and show that half of a 1/6 turn is a "
       "1/12 turn.",
       textbook=["Now, cut out a circle from a tracing paper. First, fold the circle in half, and then fold it again "
                 "into 3 equal parts. Attach a straw at the centre of the circle. Mark the starting point.",
                 "Cut out 1/6 part and 2/6 part of the circle. Fold one of the 1/6 parts into half.",
                 "This is the same as a 1/12 turn.",
                 "Paste these parts on a thicker paper or board and you can use them as angle measuring tools."],
       teach=["Predict first: a circle is folded into 6 equal parts. What fraction of a full turn is each part? And "
              "if one part is folded in half, what fraction is each small part?",
              "Fold a circle in half, then fold each half into 3 equal parts. Now it has 2 × 3 = 6 equal parts. "
              "Attach a straw at the centre and mark the starting point.",
              "Each part is a 1/6 turn. Turn the straw 1/6, 2/6, and so on until the full circle: 3/6 is the same as "
              "1/2, and 6/6 is a full turn.",
              "Cut out the 1/6 part and the 2/6 part. Fold one 1/6 part in half. Each half of a 1/6 part is a 1/12 "
              "turn.",
              "Rule: the circle in 6 parts gives 1/6 turns. Half of a 1/6 turn is a 1/12 turn, and 12 of them make a "
              "full turn."],
       examples=[WE("How many 1/12 pieces cover a 1/6 piece, a 2/6 piece and a 3/6 piece?",
                    ["A 1/12 piece is half of a 1/6 piece, so 2 pieces of 1/12 cover a 1/6 piece.",
                     "A 2/6 piece is 2 pieces of 1/6, so it needs 2 × 2 = 4 pieces of 1/12.",
                     "A 3/6 piece is 3 pieces of 1/6, so it needs 3 × 2 = 6 pieces of 1/12.",
                     "Check: 3/6 is the same as 1/2, and 6 pieces of 1/12 make 6/12 = 1/2."],
                    "2 pieces, 4 pieces and 6 pieces of 1/12")],
       ncert=["sixth.make", "sixth.cut"], key_terms=["1/6 turn", "1/12 turn", "equal parts"],
       misconceptions=["M_BIGGER_DENOM_TURN"], minutes=6),
     DOER("T4.C3", "Practice: Turn Disc", "turn_disc", "Apply",
          "Students show and read turns of 1/8, 2/8, 1/4, 3/8, 6/8 and 8/8, of sixths and of 1/12 on a disc, and find the "
          "starting arrow of a given turn.",
          ["On a circle with 8 equal parts, 2/8 = 1/4, 4/8 = 1/2, 6/8 = 3/4 and 8/8 is a full turn.",
           "On a circle with 6 equal parts each part is a 1/6 turn, and half of a 1/6 turn is a 1/12 turn.",
           "To find a starting arrow, turn back from the end arrow by the given part of a full turn."],
          items=[FIO("amt.show", "Angle Measuring Tool: show the turns",
                     "Show a 1/8 turn of the straw. Show a 2/8 turn. Show a 1/4 turn. Show a 3/8 turn.",
                     ["The circle is folded into 8 equal parts. Each part is a 1/8 turn.",
                      "A 1/8 turn is 1 part from the starting point A.",
                      "A 2/8 turn is 2 parts from A.",
                      "A 1/4 turn is the same as 2/8, because 8 ÷ 4 = 2 parts. So it is also 2 parts from A.",
                      "A 3/8 turn is 3 parts from A.",
                      "Check: 1/8, 2/8 and 3/8 move the straw 1, 2 and 3 parts, and 1/4 = 2/8 lands on the same "
                      "place as 2/8."],
                     "1/8: 1 part; 2/8: 2 parts; 1/4: 2 parts, the same as 2/8; 3/8: 3 parts.",
                     kind="prompt",
                     q_figure="A circle folded into 8 equal parts with a straw at the centre and the starting point A "
                              "marked on the edge.",
                     s_figure="The same circle with the straw in four positions, marked 1/8, 2/8, 1/4 and 3/8."),
                 FIO("amt.2of8", "Angle Measuring Tool: eighths and a right angle",
                     "What angle have you made with a 2/8 turn? A 1/8 turn is half of a quarter turn.",
                     ["A 2/8 turn is 2 parts of the 8.",
                      "2/8 = 1/4, because 2 ÷ 2 = 1 and 8 ÷ 2 = 4.",
                      "A 1/4 turn is a quarter turn, and a quarter turn makes a right angle.",
                      "Check: a 1/8 turn is half of a quarter turn, so two 1/8 turns make a quarter turn."],
                     "A right angle, because 2/8 = 1/4 is a quarter turn.",
                     kind="prompt",
                     q_figure="A circle folded into 8 equal parts with a straw at the centre and the starting point A "
                              "marked on the edge.",
                     s_figure="The straw turned 2 parts from A with a square corner marked, and the words 2/8 = 1/4 "
                              "turn."),
                 FIO("amt.4of8", "Angle Measuring Tool: eighths and a straight angle",
                     "What angle have you made with a 4/8 turn?",
                     ["A 4/8 turn is 4 parts of the 8.",
                      "4/8 = 1/2, because 4 ÷ 4 = 1 and 8 ÷ 4 = 2.",
                      "A 1/2 turn is a half turn, and a half turn makes a straight angle.",
                      "Check: 4/8 = 2/8 + 2/8 = 1/4 + 1/4, which is two quarter turns."],
                     "A straight angle, because 4/8 = 1/2 is a half turn.",
                     kind="prompt",
                     q_figure="A circle folded into 8 equal parts with a straw at the centre and the starting point A "
                              "marked on the edge.",
                     s_figure="The straw turned 4 parts from A, pointing the opposite way, and the words 4/8 = 1/2 "
                              "turn."),
                 FIO("amt.continue", "Angle Measuring Tool: three-quarter turn and full turn",
                     "Continue turning by 5/8, 6/8, 7/8, and 8/8. Check when you have completed a 3/4 turn and a "
                     "full turn.",
                     ["Keep turning the straw part by part: 5/8, 6/8, 7/8 and 8/8.",
                      "6/8 = 3/4, because 6 ÷ 2 = 3 and 8 ÷ 2 = 4. So the straw has made a 3/4 turn at 6 parts.",
                      "At 8/8 the straw is back on the starting point A. 8/8 = 1, a full turn.",
                      "Check: 3/4 is 3 quarter turns, and 3 quarters plus 1 more quarter make 4 quarters, a full "
                      "turn."],
                     "6/8 is the 3/4 turn; 8/8 is the full turn.",
                     kind="prompt",
                     q_figure="A circle folded into 8 equal parts with a straw at the centre and the starting point A "
                              "marked on the edge.",
                     s_figure="The straw at 6 parts marked 6/8 = 3/4 turn and back on A after 8 parts marked 8/8 = a "
                              "full turn."),
                 FIO("LUT.Q1", "Let Us Think: Q1",
                     "In the following circles, the end points of 1/2, 1/4, and 1/8 turns are shown. Draw arrows to "
                     "show the starting points.",
                     ["The green dashed arrow in each circle goes the way the hands of a clock move. Each turn goes "
                      "that way from the starting arrow to the red end arrow.",
                      "To find a starting arrow, turn back from the end arrow by the given part of a full turn.",
                      "1/2 turn: turning back half way gives the opposite arrow. End lower right gives start upper "
                      "left. End upper right gives start lower left.",
                      "1/8 turn: turning back half of a quarter turn. End right gives start upper right. End lower "
                      "right gives start right.",
                      "1/4 turn: turning back a quarter turn, a square corner. End upper left gives start lower "
                      "left. End straight down gives start right.",
                      "Check: from each start, turn the given part the clock way and land on the red arrow."],
                     "Top circle, then bottom circle. 1/2: upper left, lower left. 1/8: upper right, right. 1/4: "
                     "lower left, right.",
                     kind="exercise",
                     q_figure="Six circles in three columns headed 1/2 turn, 1/8 turn and 1/4 turn, two circles in "
                              "each column. In each circle a red arrow from the centre shows where the turn ends and "
                              "a green dashed arrow goes the way the hands of a clock move. In the 1/2 column the end "
                              "arrows point to the lower right and to the upper right; in the 1/8 column they point "
                              "to the right and to the lower right; in the 1/4 column they point to the upper left "
                              "and straight down.",
                     s_figure="The six circles with the starting arrow drawn: 1/2 column, upper left and lower left; "
                              "1/8 column, upper right and right; 1/4 column, lower left and right."),
                 FIO("sixth.show", "Angle Measuring Tool: turns in sixths",
                     "Show the turns of the straw equal to 1/6, 2/6, and so on until you complete a full circle.",
                     ["The circle is folded in half, then each half into 3 equal parts: 2 × 3 = 6 equal parts.",
                      "Each part is a 1/6 turn.",
                      "Turn the straw 1 part at a time from the starting point: 1/6, 2/6, 3/6, 4/6, 5/6, 6/6.",
                      "2/6 = 1/3 and 3/6 = 1/2, a half turn, a straight angle. 4/6 = 2/3.",
                      "At 6/6 the straw is back on the starting point: a full turn.",
                      "Check: 6 parts of 1/6 make 6/6 = 1."],
                     "The straw turns 1/6, 2/6, 3/6, 4/6, 5/6 and 6/6; 6/6 is a full turn.",
                     kind="prompt",
                     q_figure="A tracing paper circle folded into 6 equal parts with a straw at the centre and a "
                              "starting point marked.",
                     s_figure="The circle with the straw turned to 1/6, 2/6, 3/6, 4/6, 5/6 and 6/6 of a turn."),
                 FIO("sixth.half", "Angle Measuring Tool: half of one sixth",
                     "Can you guess what turn of the straw will be equal to half of a 1/6 turn?",
                     ["A 1/6 part is folded in half, so it is cut into 2 equal small parts.",
                      "The whole circle has 6 parts of 1/6, and each is cut into 2 small parts: 6 × 2 = 12 small "
                      "parts.",
                      "So each small part is 1 of 12 equal parts: a 1/12 turn.",
                      "Check: 2 small parts make 2/12 = 1/6."],
                     "A 1/12 turn.",
                     kind="prompt",
                     q_figure="A circle with a 1/6 part cut out and one 1/6 part folded in half.",
                     s_figure="A circle in 12 equal parts with one part marked 1/12 turn.")],
          misconceptions=["M_BIGGER_DENOM_TURN"])],
    key_terms=["1/8 turn", "1/6 turn", "1/12 turn", "equal parts"]))

# ============================== T5 Measuring an Angle ======================================================
# 9 Nov 2026 (teacher feedback): the old topic "Measuring and Drawing Angles" is split into two learning topics, one
# idea and one video each. The single tool Angle Check and Draw sits in the second topic: measuring first, drawing second.
TOPICS.append(TOPIC(
    "T5", "M2", "Measuring an Angle", ["Let Us Do"], "Apply",
    "Students measure an angle by laying the turn pieces on it, name it as acute, right or obtuse, and read the turn "
    "an arrow makes.",
    "Lay the pieces side by side from the first line and add their turns to measure an angle, then compare the total "
    "with 1/4 and 1/2 to name it.",
    [A("T5.C1", "Measuring an Angle", "Apply",
       "Students measure an angle by laying turn pieces side by side on it and adding their fractions, and name the "
       "angle as acute, right or obtuse.",
       textbook=["Guess the measures of each of the angles shown below. Then, check using your angle measuring tools. "
                 "You may need to use a combination of measures."],
       teach=["Predict first: an angle is just covered by a 1/6 piece and a 1/12 piece side by side. How much of a "
              "full turn is the angle?",
              "Your angle measuring tools are pieces of a circle: 1/8, 2/8, 1/6, 2/6 and 1/12. Lay the pieces side by "
              "side, starting on the first line of the angle.",
              "Guess first, then check. You may need a combination of pieces.",
              "Add the fractions of the pieces. To add 1/6 and 1/12, use twelfths: a 1/6 piece is 2 pieces of 1/12.",
              "Then name the angle: less than 1/4 turn is acute, exactly 1/4 is right, and between 1/4 and 1/2 is "
              "obtuse.",
              "Rule: lay the pieces side by side from the first line, add their turns, and compare the total with 1/4 "
              "and 1/2."],
       examples=[WE("An angle is covered exactly by one 1/6 piece and one 1/12 piece laid side by side. What turn does "
                    "the angle make, and what kind of angle is it?",
                    ["Lay the 1/6 piece on the angle, starting from the first line, and the 1/12 piece next to it.",
                     "1/6 is 2 pieces of 1/12, so 1/6 = 2/12.",
                     "2/12 + 1/12 = 3/12.",
                     "3/12 = 1/4, because 3 ÷ 3 = 1 and 12 ÷ 3 = 4.",
                     "A 1/4 turn is a right angle.",
                     "Check: 3 pieces of 1/12 make a quarter turn, and 12 pieces make a full turn."],
                    "A 1/4 turn: a right angle")],
       key_terms=["angle", "turn pieces", "right angle"],
       misconceptions=["M_ARM_LENGTH", "M_BIGGER_DENOM_TURN"], minutes=6),
     DOER("T5.C2", "Practice: Measuring Angles", None, "Apply",
          "Students guess and check angles with turn pieces and read the turn an arrow makes.",
          ["Lay the pieces side by side from the first line and add their turns.",
           "Compare the total with 1/4 and 1/2 to name the angle."],
          items=[FIO("LUD2.Q1", "Let Us Do (measuring turns), Q1",
                     "Guess the measures of each of the angles shown below. Then, check using your angle measuring "
                     "tools. You may need to use a combination of measures. Also, state whether each of the angles "
                     "is acute, right, or obtuse.",
                     ["The pieces are 1/8, 2/8 (a 1/4), 1/6, 2/6 (a 1/3) and 1/12. Lay them side by side on each "
                      "angle.",
                      "Angle 1: the narrowest, about one 1/12 piece: about a 1/12 turn. It is less than 1/4, so "
                      "acute.",
                      "Angle 2: one 1/6 piece: a 1/6 turn. Acute.",
                      "Angle 3: one 1/8 piece: a 1/8 turn. Acute.",
                      "Angle 4: about one 1/6 piece: about a 1/6 turn. Acute.",
                      "Angle 5: one 2/8 piece: 2/8 = 1/4, a right angle.",
                      "Angle 6: about one 2/6 piece: about 2/6 = 1/3, more than 1/4 and less than 1/2, so obtuse.",
                      "Angle 7: a 1/8 piece and a 2/8 piece: 1/8 + 2/8 = 3/8, more than 1/4 and less than 1/2, so "
                      "obtuse.",
                      "Check: 1/12, 1/6, 1/8 and 1/6 are each less than 1/4, so those four are acute."],
                     "1: about 1/12, acute; 2: 1/6, acute; 3: 1/8, acute; 4: about 1/6, acute; 5: 1/4, right; "
                     "6: about 1/3, obtuse; 7: 3/8, obtuse.",
                     kind="exercise",
                     q_figure="A dotted grid with seven angles, each made of two lines from one dot and each with an "
                              "empty box beside it. They are numbered 1 to 7 from left to right; angle 4 is the "
                              "upper of the two angles in the middle.",
                     s_figure="The seven angles named: 1/12, 1/6, 1/8, 1/6, 1/4, 1/3 and 3/8 of a turn."),
                 FIO("LUD2.Q2", "Let Us Do (measuring turns), Q2",
                     "Guess the measure of the turns made by the arrow in each of the following cases. Verify with a "
                     "combination of angle measuring tools. (a) 1/4 + 1/8 turn or 3/8 turn (this part is already "
                     "solved in your maths book); (b) ___ turn; (c) ___ turn; (d) ___ turn",
                     ["The arrow turns from a starting arrow to an end arrow, the way the hands of a clock move.",
                      "(a): your maths book gives 1/4 + 1/8 = 2/8 + 1/8 = 3/8 turn.",
                      "(b): from straight up round to the lower left. It passes a half turn at straight down and "
                      "goes 1/8 more: 1/2 + 1/8 = 4/8 + 1/8 = 5/8 turn.",
                      "(c): from straight up to the upper right: half of a quarter turn, a 1/8 turn.",
                      "(d): from the upper right, 1/8 of a turn from straight up, to a little left of straight down. "
                      "Lay a 1/4 piece and a 1/6 piece: about 1/4 + 1/6 = 3/12 + 2/12 = 5/12 turn.",
                      "Check: (d) is a guess. 5/12 is more than 1/3 and less than 1/2, which matches an arrow that "
                      "stops a little short of a half turn."],
                     "(a): 3/8; (b): 5/8; (c): 1/8; (d): about 5/12.",
                     kind="exercise",
                     q_figure="Four circles, each split into four coloured quarters by a vertical and a horizontal "
                              "line, each with a black arrow at the start, a second black arrow where the turn ends "
                              "and a dashed curved arrow between them. In (a) the arrow turns from straight up to the "
                              "lower right. In (b) it turns from straight up round to the lower left. In (c) it turns "
                              "from straight up to the upper right. In (d) it turns from the upper right to straight "
                              "down and a little to the left.",
                     s_figure="The four circles with the turn shaded: (a) 3/8, (b) 5/8, (c) 1/8, (d) about 5/12."),
                 FIO("LUD2.Q3", "Let Us Do (measuring turns), Q3",
                     "Measure each angle in the given shapes. Write the measure of the angles in terms of turns and "
                     "describe whether they are acute, obtuse or right angles. (a) the lines AB and A'B' cross at C "
                     "and B'A joins B' and A; angles marked at B' and A. (b) the four-sided shape D, E, D', E'; "
                     "angles marked at D, E and D'. (c) the four-sided shape F, G, F', G'; angles marked at F, G "
                     "and F'.",
                     ["Lay the pieces on each marked angle.",
                      "(a): the angles at B' and A are each one 1/8 piece: a 1/8 turn each. Acute.",
                      "(b): the angles at D and D' are each one 1/6 piece: a 1/6 turn. Acute. The angle at E is two "
                      "1/6 pieces, a 2/6 piece: 2/6 = 1/3. It is more than 1/4 and less than 1/2: obtuse.",
                      "(c): the angle at F is a 1/8 piece: acute. The angle at G is a 2/6 piece: 1/3, obtuse. The "
                      "angle at F' is a 2/8 piece: 2/8 = 1/4, a right angle.",
                      "Check: the angles in (a) and at F are the same size, and G is the same size as E."],
                     "(a): B' and A are 1/8, acute; (b): D, D' are 1/6, acute, E is 1/3, obtuse; (c): F is 1/8, "
                     "acute, G is 1/3, obtuse, F' is 1/4, right.",
                     kind="exercise",
                     q_figure="Three shapes with marked angles: (a) two lines AB and B'A' cross at C and a line joins "
                              "B' to A, with the angles at B' and A marked; (b) a four-sided shape D, E, D', E' with "
                              "the angles at D, E and D' marked; (c) a four-sided shape F, G, F', G' with the angles "
                              "at F, G and F' marked.",
                     s_figure="The three shapes with each marked angle labelled: (a) B' and A, 1/8; (b) D and D', "
                              "1/6, and E, 1/3; (c) F, 1/8, G, 1/3 and F', 1/4.")],
          misconceptions=["M_ARM_LENGTH", "M_BIGGER_DENOM_TURN"])],
    key_terms=["angle", "turn pieces", "acute", "right", "obtuse"]))

# ============================== T5B Drawing an Angle =======================================================
TOPICS.append(TOPIC(
    "T5B", "M2", "Drawing an Angle", ["Let Us Do"], "Apply",
    "Students draw an angle for a given turn by laying the pieces for that turn from a given line and drawing the "
    "second line along the last piece.",
    "To draw an angle for a turn, lay the pieces for that turn from the given line and draw along the last edge.",
    [A("T5B.C1", "Drawing an Angle", "Apply",
       "Students draw an angle for a given turn by laying the pieces for that turn from a given line and drawing the "
       "second line along the last piece.",
       textbook=["Draw angles for the given measures of turns using the given lines."],
       teach=["Predict first: you have a line and you need an angle of a 1/2 + 1/12 turn. How can you draw it?",
              "Put one end of the line at the centre of the circle pieces. This end is the corner of the angle.",
              "Lay the pieces for the turn one after another, starting from the line. For 1/2 + 1/12, lay a half "
              "turn, then a 1/12 piece.",
              "Draw the second line along the edge of the last piece.",
              "A 1/4 turn gives a right angle, a 1/2 turn gives a straight angle, and a turn of more than 1/2 is more "
              "than a straight angle.",
              "Rule: lay the pieces of the turn from the given line and draw along the last edge."],
       examples=[WE("Draw an angle of a 1/2 + 1/12 turn on a given line. What kind of angle is it?",
                    ["Turn the line a half turn, then 1/12 more, in the same direction.",
                     "1/2 = 6/12, so 1/2 + 1/12 = 6/12 + 1/12 = 7/12.",
                     "A half turn is 6/12, and 7/12 is more than 6/12.",
                     "So the angle is more than a half turn: more than a straight angle.",
                     "Draw the second line along the edge of the 1/12 piece.",
                     "Check: 7 pieces of 1/12 are one piece more than the half turn of 6 pieces."],
                    "A 7/12 turn, more than a straight angle")],
       key_terms=["draw an angle", "turn", "straight angle"],
       misconceptions=["M_STRAIGHT_NOT_ANGLE"], minutes=6),
     DOER("T5B.C2", "Practice: Angle Check and Draw", "angle_check_draw", "Apply",
          "Students measure angles with turn pieces and then draw angles for given turns using the given lines.",
          ["Measuring: lay the pieces side by side from the first line and add their turns.",
           "Drawing: lay the pieces for the turn from the given line and draw along the last edge."],
          items=[FIO("LUD2.Q4", "Let Us Do (measuring turns), Q4",
                     "Draw angles for the given measures of turns using the given lines.",
                     ["Take one end of each line as the corner of the angle. Turn the line by the given part of a "
                      "full turn and draw the second line.",
                      "1/2 turn (vertical line): a half turn. The second line goes the opposite way, so both lines "
                      "lie in one straight line: a straight angle.",
                      "1/4 turn (slanting line): a quarter turn, a square corner. The second line makes a right "
                      "angle with the first. Use the 2/8 piece.",
                      "1/8 turn (vertical line): half of a quarter turn, a narrow acute angle, half of a square "
                      "corner. Use the 1/8 piece.",
                      "1/12 turn (slanting line): half of a 1/6 turn, a very narrow acute angle. Use the 1/12 piece.",
                      "1/4 turn (horizontal line): a quarter turn again, a right angle.",
                      "Check: the 1/8 angle is half of a right angle, and the 1/12 angle is narrower still."],
                     "Sample answer: 1/2: a straight line; 1/4: a square corner, both times; 1/8: half a square "
                     "corner; 1/12: narrower still. Your drawing may differ.",
                     kind="exercise",
                     q_figure="Five lines on a dotted grid, each with a dot at both ends and a label: a vertical line "
                              "with 1/2 turn, a slanting line with 1/4 turn, a vertical line with 1/8 turn, a "
                              "slanting line with 1/12 turn, and a horizontal line with 1/4 turn.",
                     s_figure="The five lines each with a second line drawn from one end: a straight line for 1/2, a "
                              "square corner for each 1/4, half a square corner for 1/8 and a narrow angle for 1/12."),
                 FIO("LUD2.Q5", "Let Us Do (measuring turns), Q5",
                     "Draw the angles formed by the following turns in your notebook. 1/2 turn, 1/4 turn, 2/4 turn, "
                     "1/6 turn, 4/6 turn, 3/12 turn, 1/2 + 1/4 turn, and 1/8 + 1/6 turn.",
                     ["Draw each angle from a line. Turn the line the given part of a full turn.",
                      "1/2 turn: a straight angle.",
                      "1/4 turn: a right angle.",
                      "2/4 turn: 2/4 = 1/2, so it is a straight angle.",
                      "1/6 turn: less than a 1/4 turn, so it is an acute angle.",
                      "4/6 turn: 4/6 is more than 3/6, and 3/6 is 1/2. So it is more than a straight angle.",
                      "3/12 turn: 3/12 = 1/4, a right angle.",
                      "1/2 + 1/4 turn: 2/4 + 1/4 = 3/4, more than 1/2: more than a straight angle.",
                      "1/8 + 1/6 turn: 1/6 is more than 1/8, so the total is more than 1/8 + 1/8 = 2/8 = 1/4. Each "
                      "part is less than 1/4, so the total is less than 1/4 + 1/4 = 1/2. It is more than 1/4 and "
                      "less than 1/2: an obtuse angle.",
                      "Check: 2/4 and 1/2 are the same turn, and 3/12 and 1/4 are the same turn."],
                     "1/2 and 2/4: straight; 1/4 and 3/12: right; 1/6: acute; 4/6 and 1/2 + 1/4: more than "
                     "straight; 1/8 + 1/6: obtuse.",
                     kind="exercise",
                     s_figure="Eight angles drawn with their turns written beside them: 1/2, 1/4, 2/4, 1/6, 4/6, 3/12, "
                              "1/2 + 1/4 and 1/8 + 1/6.")],
          misconceptions=["M_ARM_LENGTH", "M_BIGGER_DENOM_TURN"])],
    key_terms=["draw an angle", "turn", "straight angle"]))
