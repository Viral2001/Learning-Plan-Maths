# -*- coding: utf-8 -*-
"""Topics T3 and T4 (module M2: A New Unit, Seconds) of Class 5 Chapter 12, Racing Seconds: Minutes and Seconds (the
School Race, choosing seconds or minutes, and the book's open activities with no tool) and The Seconds Hand (reading
and drawing the seconds hand, with the Seconds Clock tool).
Every teaching concept has one worked example with the plan's own numbers; every book question is an FIO item of its
topic's DOER, in the book's order."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T3 Minutes and Seconds =====================================================
TOPICS.append(TOPIC(
    "T3", "M2", "Minutes and Seconds", ["School Race", "Let Us Do (seconds or minutes)", "Let Us Find"], "Apply",
    "Students read a race time in minutes and seconds, say which race time is the least, and choose seconds or "
    "minutes for an activity.",
    "A minute is split into 60 seconds, so seconds show small differences in time, like the differences in a race. A "
    "race time such as 01:55 is 1 minute 55 seconds, and the least time wins. An activity that is over in less than "
    "1 minute is measured in seconds, and a longer one in minutes.",
    [A("T3.C1", "A Smaller Unit: Seconds", "Understand",
       "Students read a race time such as 01:48 as minutes and seconds, change 1 minute and some seconds to seconds, "
       "and say which of two race times is the least.",
       textbook=["Akira, Sunita, and Mary are participating in a 200 m walking race.",
                 "Do you notice the use of a new unit seconds in the picture?",
                 "1 min = 60 seconds",
                 "In situations like a race, seconds help us observe small differences in time taken by "
                 "participants."],
       teach=["Predict first: two runners both finish a race in 1 minute and a few seconds. Can a clock that shows only "
              "minutes tell which of them won?",
              "No. Minutes are too big to show a small difference. So we use a smaller unit, the second.",
              "1 minute = 60 seconds. A race time such as 01:48 is read as minutes first, then seconds: 1 minute 48 "
              "seconds.",
              "If two runners both took 1 minute, compare the extra seconds. The runner with the least time wins, so "
              "the smaller number of seconds wins.",
              "On the winners' stand, the child with the least time stands first, the child with the next least time "
              "stands second, and the child with the next least time stands third.",
              "Rule: 1 minute = 60 seconds. In a race the least time wins."],
       examples=[WE("In a race, Remo's time is 01:48 and Zainab's time is 01:52, in minutes and seconds. Read each "
                    "time. Who won, and by how many seconds? Change Remo's time to seconds.",
                    ["01:48 means 1 minute 48 seconds. 01:52 means 1 minute 52 seconds.",
                     "Both took 1 minute, so compare the seconds. 48 is less than 52.",
                     "The least time wins, so Remo won.",
                     "52 − 48 = 4 seconds, so Remo won by 4 seconds.",
                     "1 minute = 60 seconds, so 1 minute 48 seconds = 60 + 48 = 108 seconds.",
                     "Check: Zainab's 1 minute 52 seconds is 60 + 52 = 112 seconds, and 112 − 108 = 4 seconds."],
                    "Remo won by 4 seconds. His time, 1 minute 48 seconds, is 108 seconds")],
       ncert=["school.race", "school.unit", "note.podium"],
       key_terms=["seconds", "minute", "race time"],
       misconceptions=["M_BIGGER_TIME_WINS", "M_SMALL_NUMBER_SMALL_UNIT", "M_TIME_HUNDRED"], minutes=6),
     A("T3.C2", "Seconds or Minutes?", "Understand",
       "Students choose seconds or minutes as the unit for an activity by asking whether it is over in less than 1 "
       "minute, and say why.",
       teach=["Predict first: would you measure blinking your eyes in seconds or in minutes? And melting an "
              "ice-cube?",
              "1 minute is 60 seconds. Blinking is over in a moment, far less than 1 minute, so use seconds. Melting "
              "an ice-cube takes much longer than 1 minute, so use minutes.",
              "Ask one question: is it over in less than 1 minute? If yes, use seconds. If it takes longer than 1 "
              "minute, use minutes.",
              "This is an estimate, so your answer may be a little different from a friend's answer.",
              "Rule: less than 1 minute, use seconds. More than 1 minute, use minutes."],
       examples=[WE("Choose seconds or minutes for each activity: (a) tying a shoelace (b) boiling an egg (c) saying "
                    "your name.",
                    ["Ask: is it over in less than 1 minute?",
                     "(a) Tying a shoelace is over in less than 1 minute, so the unit is seconds.",
                     "(b) Boiling an egg takes much longer than 1 minute, so the unit is minutes.",
                     "(c) Saying your name is over in less than 1 minute, so the unit is seconds.",
                     "Check: 1 minute is 60 seconds, and only boiling an egg takes longer than 60 seconds."],
                    "(a) seconds (b) minutes (c) seconds")],
       key_terms=["seconds", "minutes", "estimate"],
       misconceptions=["M_SMALL_NUMBER_SMALL_UNIT"], minutes=5),
     DOER("T3.C3", "Practice: Seconds and Minutes", None, "Apply",
          "Students read the times on the winners' stand in minutes and seconds, name the child who won the race, and "
          "estimate whether an activity takes seconds or minutes.",
          ["1 minute = 60 seconds. A race time such as 01:55 is 1 minute 55 seconds.",
           "In a race the least time wins: with the same minutes, the smaller seconds win.",
           "If an activity is over in less than 1 minute, use seconds. If it takes longer, use minutes."],
          items=[
              FIO("sec.more", "School Race: how much more than 1 minute",
                  "Akira, Sunita, and Mary are participating in a 200 m walking race. Each participant took 1 minute "
                  "but how much more?",
                  ["The three boards on the winners' stand read 01:55, 01:56 and 01:57. These are minutes and "
                   "seconds.",
                   "01:55 is 1 minute 55 seconds, so the child on stand 1 took 55 seconds more than 1 minute.",
                   "01:56 is 1 minute 56 seconds, so the child on stand 2 took 56 seconds more.",
                   "01:57 is 1 minute 57 seconds, so the child on stand 3 took 57 seconds more.",
                   "Check: 60 + 55 = 115, 60 + 56 = 116 and 60 + 57 = 117 seconds in all."],
                  "55, 56 and 57 seconds more than 1 minute, for the children on stands 1, 2 and 3",
                  kind="prompt",
                  q_figure="A winners' stand with three children on the places 2, 1 and 3, and boards under them "
                           "reading 01:56, 01:55 and 01:57 with the words Min. Sec.",
                  s_figure="The same stand with the boards read as 1 minute and 55, 56 and 57 seconds, drawn as a "
                           "bar of 60 seconds with a short bar of 55, 56 and 57 seconds after it."),
              FIO("sec.winner", "School Race: who won",
                  "Identify the child who won the race. How much time did the child take?",
                  ["The boards on the winners' stand read 01:55, 01:56 and 01:57. All three children took 1 minute "
                   "and some seconds.",
                   "In a race the least time wins. Compare the seconds: 55 is less than 56 and 56 is less than 57.",
                   "So the child on stand 1 won. The picture does not say which child is Akira, Sunita or Mary, so "
                   "we say the child on stand 1.",
                   "01:55 means 1 minute 55 seconds. 60 + 55 = 115 seconds.",
                   "Check: the child on stand 1 has the least time, and stand 1 is the first place."],
                  "The child on stand 1 won, in 1 minute 55 seconds (01:55)",
                  kind="prompt",
                  q_figure="A winners' stand with three children on the places 2, 1 and 3, and boards under them "
                           "reading 01:56, 01:55 and 01:57 with the words Min. Sec.",
                  s_figure="The same stand with the child on stand 1 marked as the winner and the board 01:55 read "
                           "as 1 minute 55 seconds."),
              FIO("LUDunit", "Let Us Do (seconds or minutes)",
                  "Estimate whether you would take seconds or minutes to complete the following activities. Tick the "
                  "appropriate cell. Activities: blinking of eyes; switching on and switching off the lights; "
                  "counting from 1 to 20; filling a glass from the tap; melting of an ice-cube; making a phone call; "
                  "sitting down on the floor; drinking a glass of water; snapping fingers; washing hands.",
                  ["The rule: if an activity is over in less than 1 minute, tick Seconds. If it takes longer than 1 "
                   "minute, tick Minutes. This is an estimate.",
                   "Blinking of eyes is over in a moment: Seconds.",
                   "Switching on and switching off the lights: Seconds.",
                   "Counting from 1 to 20: Seconds.",
                   "Filling a glass from the tap: Seconds.",
                   "Melting of an ice-cube takes much longer than 1 minute: Minutes.",
                   "Making a phone call usually takes more than 1 minute: Minutes.",
                   "Sitting down on the floor, drinking a glass of water, snapping fingers and washing hands are each "
                   "over in less than 1 minute: Seconds.",
                   "Check: 8 activities are in Seconds and 2 are in Minutes. This is a sample answer: your own "
                   "estimate may differ, for example for washing hands."],
                  "Sample answer. Seconds: eyes, lights, counting, tap, sitting, water, fingers, hands. Minutes: "
                  "ice-cube, phone call. Your answer may differ",
                  q_figure="A table with the heads Activity, Seconds and Minutes and ten rows, one for each "
                           "activity, with the Seconds and Minutes cells empty.",
                  s_figure="The same table with the Seconds cell ticked in eight rows and the Minutes cell ticked "
                           "for melting of an ice-cube and making a phone call."),
              FIO("list.events", "Seconds and Minutes: events in a few seconds",
                  "List events other than the ones listed above that you can do or that can happen in less than a "
                  "minute or in a few seconds.",
                  ["Look for things that are over before the seconds hand goes once round the clock.",
                   "Things you can do: clapping 5 times, tying a shoelace, closing a door, saying your name.",
                   "Things that happen: a bell ringing once, a ball dropping to the floor.",
                   "Check each one: is it over in less than 1 minute? If yes, keep it on the list.",
                   "Sample answer: clapping 5 times, tying a shoelace, closing a door, saying your name, a bell "
                   "ringing once. Your answer may differ."],
                  "Sample answer: clapping 5 times, tying a shoelace, closing a door, saying your name. Your answer "
                  "may differ",
                  kind="prompt"),
              FIO("est.verify", "Seconds and Minutes: estimate and verify",
                  "Estimate and verify how many of these you can do in a minute. Activities: number of balloons "
                  "blown; number of push-ups; number of breaths; number of hops on one leg.",
                  ["For each activity, first write your estimate: how many you think you can do in 1 minute.",
                   "Ask a friend to watch the seconds hand. Start when it is on 12 and stop when it is on 12 again. "
                   "That is 60 seconds, 1 minute.",
                   "Do the activity and count. Write the number you counted as the actual number.",
                   "Compare the actual number with your estimate. Was it close?",
                   "Sample answer (practice values): balloons estimated 3, actual 2; push-ups estimated 20, actual "
                   "15; breaths estimated 20, actual 18; hops estimated 40, actual 32.",
                   "Check: the practice values are only an example. Your answer may differ."],
                  "Sample answer (practice values), estimated and actual: balloons 3, 2; push-ups 20, 15; breaths 20, "
                  "18; hops 40, 32. Your answer may differ",
                  kind="prompt",
                  q_figure="A table with the heads Activity, Estimated Number and Actual Number and four rows: number "
                           "of balloons blown, number of push-ups, number of breaths and number of hops on one leg, "
                           "with the number cells empty."),
              FIO("LF.Q1", "Let Us Find: skipping the rope in 10 seconds",
                  "Find out the number of times you can skip the rope in 10 seconds.",
                  ["Ask a friend to watch the seconds hand. Begin when it is on 12 and stop when it is on 2.",
                   "From 12 to 2 is 2 × 5 = 10 seconds.",
                   "Count how many times you skip in that time.",
                   "Sample answer (practice values): 14 skips in 10 seconds.",
                   "In 1 minute there are 6 times 10 seconds, so you would skip about 14 × 6 = 84 times.",
                   "Check: 10 × 6 = 60, so 6 times 10 seconds is 1 minute. Your answer may differ."],
                  "Sample answer (practice values): 14 skips in 10 seconds. Your answer may differ",
                  kind="exercise"),
              FIO("LF.Q2", "Let Us Find: writing the word FRIEND",
                  "How long does it take you to write the word FRIEND?",
                  ["Ask a friend to watch the seconds hand. Start writing when it is on 12.",
                   "When you finish the last letter, look at where the seconds hand is.",
                   "Each number on the dial is 5 seconds. Sample answer (practice values): the hand is on 1, so 1 × "
                   "5 = 5 seconds.",
                   "The time is less than 1 minute, so say it in seconds.",
                   "Check: your answer may differ, because everyone writes at their own speed."],
                  "Sample answer (practice values): 5 seconds. Your answer may differ",
                  kind="exercise"),
              FIO("LF.Q3", "Let Us Find: running 100 m",
                  "How long does it take you to run 100 m?",
                  ["Mark a start line and a finish line 100 m apart. Ask a friend to watch the seconds hand.",
                   "Start when the hand is on 12 and stop when you cross the finish line.",
                   "Sample answer (practice values): the hand went from 12 to 5, so 5 × 5 = 25 seconds.",
                   "If the hand goes past 12 again, one full round is 1 minute. For example, one full round and 10 "
                   "more seconds is 1 minute 10 seconds.",
                   "Check: 25 seconds is less than 1 minute, so say it in seconds. Your answer may differ."],
                  "Sample answer (practice values): 25 seconds. Your answer may differ",
                  kind="exercise"),
          ],
          misconceptions=["M_BIGGER_TIME_WINS", "M_SMALL_NUMBER_SMALL_UNIT"])],
    key_terms=["seconds", "minutes", "race"]))

# ============================== T4 The Seconds Hand ========================================================
TOPICS.append(TOPIC(
    "T4", "M2", "The Seconds Hand", ["Let Us Do (the seconds hand)"], "Apply",
    "Students read the seconds hand to find how many seconds an activity took, and draw the seconds hand where it "
    "stops after a given number of seconds.",
    "The thin red hand is the seconds hand. Each number on the dial is 5 seconds and one full round is 60 seconds, "
    "which moves the minute hand on by one mark. To find the seconds taken, count from the start number to the end "
    "number, past 12 if the hand goes past it. To draw the hand, change the seconds into steps of 5 and count on.",
    [A("T4.C1", "Reading the Seconds Hand", "Apply",
       "Students read the seconds hand on two clocks to find the seconds taken, counting past 12 when the hand goes "
       "round, and say what happens to the minute hand.",
       teach=["Predict first: the thin red hand starts on 3 and stops on 8. Have more than 20 seconds passed, or "
              "fewer?",
              "The thin red hand is the seconds hand. It goes once round the clock in 60 seconds. Each number on the "
              "dial is 5 seconds, so 3 is 15 seconds and 8 is 40 seconds.",
              "From 3 to 8: 40 − 15 = 25 seconds. That is more than 20 seconds.",
              "When the seconds hand has gone once round, the minute hand moves on by one mark. 60 movements of the "
              "seconds hand make the minute hand move on by one minute.",
              "If the hand goes past 12, count to 12 first and then on. From 8 to 2 is 20 seconds to reach 12 and 10 "
              "seconds more. Do not take 2 from 8.",
              "Rule: each number is 5 seconds. Count from the start to the end, past 12 if you must."],
       examples=[WE("Remo timed himself tying his shoe. (a) The seconds hand started on 3 and stopped on 8. How many "
                    "seconds did he take? (b) On another try it started on 8 and stopped on 2. How many seconds?",
                    ["(a) Each number on the dial is 5 seconds. The start, 3, is 3 × 5 = 15 seconds. The stop, 8, is "
                     "8 × 5 = 40 seconds.",
                     "40 − 15 = 25 seconds.",
                     "(b) The start, 8, is 8 × 5 = 40 seconds. From 8 to 12 is 60 − 40 = 20 seconds.",
                     "From 12 to 2 is 2 × 5 = 10 seconds.",
                     "20 + 10 = 30 seconds.",
                     "Check: 40 seconds and 30 more is 70 seconds, and 70 − 60 = 10, which is the number 2."],
                    "(a) 25 seconds (b) 30 seconds")],
       ncert=["note.hand"],
       key_terms=["seconds hand", "minute hand", "full round"],
       misconceptions=["M_HAND_SUBTRACT", "M_ROUND_ZERO", "M_MINUTE_NUMBER"], minutes=6),
     A("T4.C2", "Drawing the Seconds Hand", "Apply",
       "Students draw the seconds hand where it stops after a given number of seconds by changing the seconds into "
       "steps of 5, and say when the minute hand moves on.",
       teach=["Predict first: the seconds hand is on 10 and runs for 25 seconds. Will it stop before 12, or will it "
              "go past 12?",
              "10 is 50 seconds. 50 + 25 = 75 seconds, which is more than 60, so the hand goes past 12.",
              "Change the seconds into steps of 5: 25 ÷ 5 = 5 steps. Count 5 numbers on from 10: 11, 12, 1, 2, 3. The "
              "hand stops on 3.",
              "The hand went past 12 once, so the minute hand has moved on by one mark.",
              "60 seconds is one full round. The hand is back on the same number, and the minute hand has moved on by "
              "one mark. So the same number at the start and the end does not mean that no time has passed.",
              "Rule: change the seconds into steps of 5 and count on from the start. Past 12, the minute hand moves "
              "on."],
       examples=[WE("The seconds hand is on 10. It runs for 25 seconds. Where does it stop, and what happens to the "
                    "minute hand?",
                    ["The hand starts on 10. Each number is 5 seconds, so 10 is 10 × 5 = 50 seconds.",
                     "50 + 25 = 75 seconds.",
                     "75 is more than 60, so the hand has gone past 12 once. 75 − 60 = 15 seconds.",
                     "15 seconds is 15 ÷ 5 = 3, so the hand stops on 3.",
                     "The hand went past 12 once, so the minute hand has moved on by one mark.",
                     "Check: from 10 to 12 is 10 seconds and from 12 to 3 is 15 seconds, and 10 + 15 = 25 seconds."],
                    "The seconds hand stops on 3, and the minute hand moves on by one mark")],
       key_terms=["seconds hand", "steps of 5", "full round"],
       misconceptions=["M_ROUND_ZERO", "M_HAND_SUBTRACT"], minutes=6),
     DOER("T4.C3", "Practice: Seconds Clock", "seconds_clock", "Apply",
          "Students read the seconds hand on pairs of clocks to find the seconds taken, and draw the missing seconds "
          "hand after a given number of seconds.",
          ["Each number on the dial is 5 seconds. One full round of the seconds hand is 60 seconds.",
           "To find the seconds taken, count from the start number to the end number, past 12 if the hand goes past "
           "it.",
           "To draw the hand, change the seconds into steps of 5 and count on from the start. When the hand has gone "
           "past 12, the minute hand has moved on by one mark."],
          items=[
              FIO("LUDsec.Q1", "Let Us Do (reading the seconds hand), Q1",
                  "Observe the clocks and fill in the blanks. Rani took ___ seconds to get out of her bed.",
                  ["The seconds hand is the thin red hand. In the left clock it is on 12, which is 0 seconds.",
                   "In the right clock it is on 6, which is 6 × 5 = 30 seconds.",
                   "30 − 0 = 30 seconds.",
                   "Check: from 12 to 6 is 6 numbers of 5 seconds each, 6 × 5 = 30 seconds."],
                  "30 seconds",
                  q_figure="Two clocks side by side, both with the hour hand between 6 and 7 and the minute hand on "
                           "9, the seconds hand on 12 in the left clock and on 6 in the right clock.",
                  s_figure="The two clocks with the stretch of the seconds hand from 12 to 6 shaded and labelled 30 "
                           "seconds."),
              FIO("LUDsec.Q2", "Let Us Do (reading the seconds hand), Q2",
                  "Observe the clocks and fill in the blanks. Raghav took ___ seconds to move from his room to the "
                  "kitchen.",
                  ["In the left clock the seconds hand is on 12, which is 0 seconds.",
                   "In the right clock it is on 7, which is 7 × 5 = 35 seconds.",
                   "35 − 0 = 35 seconds.",
                   "Check: count the numbers from 12 to 7 in fives: 5, 10, 15, 20, 25, 30, 35."],
                  "35 seconds",
                  q_figure="Two clocks side by side, both with the hour hand on 4 and the minute hand on 9, the "
                           "seconds hand on 12 in the left clock and on 7 in the right clock.",
                  s_figure="The two clocks with the stretch of the seconds hand from 12 to 7 shaded and labelled 35 "
                           "seconds."),
              FIO("LUDsec.Q3", "Let Us Do (reading the seconds hand), Q3",
                  "Observe the clocks and fill in the blanks. Ritu took ___ seconds to pick up a piece of paper from "
                  "the floor.",
                  ["In the left clock the seconds hand is on 9, which is 9 × 5 = 45 seconds.",
                   "In the right clock it is on 12, which is 60 seconds. The hand has gone on to 12.",
                   "From 9 to 12 is 60 − 45 = 15 seconds.",
                   "Check: from 9 to 12 is 3 numbers, 3 × 5 = 15 seconds."],
                  "15 seconds",
                  q_figure="Two clocks side by side, both with the hour hand between 5 and 6 and the minute hand on "
                           "6, the seconds hand on 9 in the left clock and on 12 in the right clock.",
                  s_figure="The two clocks with the stretch of the seconds hand from 9 to 12 shaded and labelled 15 "
                           "seconds."),
              FIO("LUDsec.Q4", "Let Us Do (reading the seconds hand), Q4",
                  "Observe the clocks and fill in the blanks. Raghu took ___ seconds to wash his spoon and plate.",
                  ["The seconds hand is on 5 in both clocks, which is 5 × 5 = 25 seconds.",
                   "The minute hand in the right clock has moved on by one mark since the left clock.",
                   "So the seconds hand went once round the clock and came back to 5. One full round is 60 seconds.",
                   "Check: 60 movements of the seconds hand make the minute hand move on by one minute, and 1 minute "
                   "is 60 seconds."],
                  "60 seconds (1 minute)",
                  q_figure="Two clocks side by side, both with the hour hand on 6 and the seconds hand on 5, the "
                           "minute hand on 12 in the left clock and one mark past 12 in the right clock.",
                  s_figure="The two clocks with a full round of the seconds hand shaded and labelled 60 seconds, and "
                           "an arrow showing the minute hand moved on by one mark."),
              FIO("LUDdraw.Q1", "Let Us Do (drawing the seconds hand), Q1",
                  "Draw the missing seconds hand on the clock on the right side. Raghu took 20 seconds to read a "
                  "sentence in his book.",
                  ["The seconds hand in the left clock is on 12, which is 0 seconds.",
                   "20 seconds later is 20 ÷ 5 = 4 numbers on.",
                   "Count on from 12: 1, 2, 3, 4. Draw the seconds hand on 4.",
                   "Check: 4 × 5 = 20 seconds."],
                  "Draw the seconds hand on 4",
                  q_figure="Two clocks side by side, both with the hour hand between 6 and 7 and the minute hand on "
                           "9, the left clock with its seconds hand on 12 and the right clock with no seconds hand.",
                  s_figure="The right clock with its seconds hand drawn on 4 and the stretch from 12 to 4 shaded and "
                           "labelled 20 seconds."),
              FIO("LUDdraw.Q2", "Let Us Do (drawing the seconds hand), Q2",
                  "Draw the missing seconds hand on the clock on the right side. Rani took 30 seconds to colour a "
                  "rectangle.",
                  ["The seconds hand in the left clock is on 12, which is 0 seconds.",
                   "30 seconds later is 30 ÷ 5 = 6 numbers on.",
                   "Count on from 12 to 6. Draw the seconds hand on 6.",
                   "Check: 6 × 5 = 30 seconds."],
                  "Draw the seconds hand on 6",
                  q_figure="Two clocks side by side, both with the hour hand on 4 and the minute hand on 9, the left "
                           "clock with its seconds hand on 12 and the right clock with no seconds hand.",
                  s_figure="The right clock with its seconds hand drawn on 6 and the stretch from 12 to 6 shaded and "
                           "labelled 30 seconds."),
              FIO("LUDdraw.Q3", "Let Us Do (drawing the seconds hand), Q3",
                  "Draw the missing seconds hand on the clock on the right side. Raghav took 60 seconds to move from "
                  "his home to the garden.",
                  ["The seconds hand in the left clock is on 9, which is 9 × 5 = 45 seconds.",
                   "45 + 60 = 105 seconds.",
                   "105 − 60 = 45 seconds, which is the number 9 again. Draw the seconds hand on 9.",
                   "60 seconds is one full round, so the minute hand has moved on by one mark. In the right clock the "
                   "minute hand is a little past where it was.",
                   "Check: one full round of the seconds hand is 60 seconds."],
                  "Draw the seconds hand on 9 again; the minute hand has moved on by one mark",
                  q_figure="Two clocks side by side, both with the hour hand between 5 and 6, the left clock with the "
                           "minute hand on 6 and the seconds hand on 9, and the right clock with the minute hand a "
                           "little past 6 and no seconds hand.",
                  s_figure="The right clock with its seconds hand drawn on 9 again and a full round shaded and "
                           "labelled 60 seconds."),
              FIO("LUDdraw.Q4", "Let Us Do (drawing the seconds hand), Q4",
                  "Draw the missing seconds hand on the clock on the right side. Ritu took 40 seconds to wash a "
                  "plate.",
                  ["The seconds hand in the left clock is on 11, which is 11 × 5 = 55 seconds.",
                   "55 + 40 = 95 seconds.",
                   "95 is more than 60, so the hand has gone past 12. 95 − 60 = 35 seconds.",
                   "35 ÷ 5 = 7, so draw the seconds hand on 7.",
                   "The hand went past 12 once, so the minute hand has moved on by one mark.",
                   "Check: from 11 to 12 is 5 seconds and from 12 to 7 is 35 seconds, and 5 + 35 = 40 seconds."],
                  "Draw the seconds hand on 7; the minute hand has moved on by one mark",
                  q_figure="Two clocks side by side, both with the hour hand on 6 and the minute hand on 12, the left "
                           "clock with its seconds hand on 11 and the right clock with no seconds hand.",
                  s_figure="The right clock with its seconds hand drawn on 7 and the stretch from 11 round past 12 to "
                           "7 shaded and labelled 40 seconds."),
          ],
          misconceptions=["M_ROUND_ZERO", "M_HAND_SUBTRACT", "M_MINUTE_NUMBER"])],
    key_terms=["seconds hand", "seconds", "clock"]))
