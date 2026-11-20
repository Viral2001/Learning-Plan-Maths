# -*- coding: utf-8 -*-
"""Topics T5 and T6 (module M3: Changing Units and Solving Time Problems) of Class 5 Chapter 12, Racing Seconds: Hours,
Minutes and Seconds (the two double number lines, with the Time Converter Line tool) and Time Problems (the time
after, the time before, and across 12 noon and midnight, with the Time Jumper tool).
Every teaching concept has one worked example with the plan's own numbers; every book question is an FIO item of its
topic's DOER, in the book's order."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T5 Hours, Minutes and Seconds ==============================================
TOPICS.append(TOPIC(
    "T5", "M3", "Hours, Minutes and Seconds", ["Conversion of Hours to Minutes", "Let Us Do (changing units)"], "Apply",
    "Students change hours to minutes and minutes to hours and minutes, and minutes to seconds and seconds to minutes "
    "and seconds, using a double number line.",
    "1 hour = 60 minutes and 1 minute = 60 seconds. To change a bigger unit to a smaller one, multiply by 60 and add "
    "what is left over. To change a smaller unit to a bigger one, find how many whole groups of 60 fit and keep the "
    "rest. A double number line shows both units side by side.",
    [A("T5.C1", "Hours and Minutes", "Apply",
       "Students change hours and minutes to minutes by multiplying the hours by 60, and change minutes to hours and "
       "minutes by finding the whole groups of 60.",
       textbook=["We know 1 hr = 60 min. So, 2 hr will have 2 × 60 = 120 min.",
                 "This means that 180 min = 3 hr. As 3 hrs = 3 × 60 = 180 min."],
       teach=["Predict first: 5 hours 25 minutes in minutes. Is it more than 300 minutes, or less?",
              "1 hour = 60 minutes. On a double number line the hours are above and the minutes are below, and every "
              "hour is 60 minutes further along.",
              "Zainab: 1 hour is 60 minutes, so 2 hours is 2 × 60 = 120 minutes. Remo goes the other way: 180 minutes "
              "= 3 hours, because 3 × 60 = 180.",
              "Hours and minutes to minutes: change the hours to minutes, then add the minutes. 5 hours 25 minutes is "
              "5 × 60 + 25 = 325 minutes. That is more than 300.",
              "Minutes to hours and minutes: find how many whole groups of 60 fit, and keep what is left. In 370 "
              "minutes, 60 × 6 = 360, so there are 6 hours and 370 − 360 = 10 minutes left.",
              "Rule: hours to minutes, multiply by 60. Minutes to hours, find the whole groups of 60 and keep the "
              "rest."],
       examples=[WE("(a) Change 5 hours 25 minutes to minutes. (b) Change 370 minutes to hours and minutes.",
                    ["(a) 1 hour = 60 minutes, so 5 hours = 5 × 60 = 300 minutes.",
                     "300 + 25 = 325 minutes.",
                     "(b) 60 × 6 = 360 and 60 × 7 = 420. 370 is between them, so there are 6 whole hours.",
                     "370 − 360 = 10 minutes are left.",
                     "So 370 minutes = 6 hours 10 minutes.",
                     "Check: 6 × 60 = 360 and 360 + 10 = 370."],
                    "(a) 325 minutes (b) 6 hours 10 minutes")],
       ncert=["conv.zainab"],
       key_terms=["hours", "minutes", "double number line"],
       misconceptions=["M_TIME_HUNDRED"], minutes=7),
     A("T5.C2", "Minutes and Seconds", "Apply",
       "Students change minutes and seconds to seconds by multiplying the minutes by 60, and change seconds to "
       "minutes and seconds by finding the whole groups of 60.",
       teach=["Predict first: 4 minutes 30 seconds in seconds. Is it more than 240 seconds, or less?",
              "1 minute = 60 seconds. The second double number line has the minutes above and the seconds below. 1 "
              "minute is 60 seconds, so 5 minutes is 5 × 60 = 300 seconds.",
              "Minutes and seconds to seconds: change the minutes to seconds, then add the seconds. 4 minutes 30 "
              "seconds is 4 × 60 + 30 = 270 seconds. That is more than 240.",
              "Seconds to minutes and seconds: find how many whole groups of 60 fit, and keep what is left. In 400 "
              "seconds, 60 × 6 = 360, so there are 6 minutes and 400 − 360 = 40 seconds left.",
              "Rule: minutes to seconds, multiply by 60. Seconds to minutes, find the whole groups of 60 and keep the "
              "rest."],
       examples=[WE("(a) Change 4 minutes 30 seconds to seconds. (b) Change 400 seconds to minutes and seconds.",
                    ["(a) 1 minute = 60 seconds, so 4 minutes = 4 × 60 = 240 seconds.",
                     "240 + 30 = 270 seconds.",
                     "(b) 60 × 6 = 360 and 60 × 7 = 420. 400 is between them, so there are 6 whole minutes.",
                     "400 − 360 = 40 seconds are left.",
                     "So 400 seconds = 6 minutes 40 seconds.",
                     "Check: 6 × 60 = 360 and 360 + 40 = 400."],
                    "(a) 270 seconds (b) 6 minutes 40 seconds")],
       key_terms=["minutes", "seconds", "groups of 60"],
       misconceptions=["M_TIME_HUNDRED"], minutes=6),
     DOER("T5.C3", "Practice: Double Number Line", "double_number_line", "Apply",
          "Students fill the blanks of a double number line, and change hours to minutes, minutes to hours and "
          "minutes, minutes to seconds and seconds to minutes and seconds.",
          ["1 hour = 60 minutes and 1 minute = 60 seconds. On a double number line each step multiplies by 60.",
           "To change to the smaller unit, multiply the bigger unit by 60 and add what is left over.",
           "To change to the bigger unit, find how many whole groups of 60 fit and keep the rest."],
          items=[
              FIO("LUDconv.Q1a", "Let Us Do (changing units), Q1 (a)",
                  "Use the double number line below to complete the conversions. Hours: 1 hour, ___, 4 hours, 7 "
                  "hours, ___, 9 hours, ___, ___. Minutes: 60 minutes, 120 minutes, ___, ___, 480 minutes, ___, 660 "
                  "minutes, 720 minutes.",
                  ["Each tick is one number of hours, and the minutes below it are 60 times as many.",
                   "Above 120 minutes: 120 ÷ 60 = 2 hours. The × 2 arrow joins 1 hour to 2 hours.",
                   "Below 4 hours: 4 × 60 = 240 minutes.",
                   "Below 7 hours: 7 × 60 = 420 minutes.",
                   "Above 480 minutes: 480 ÷ 60 = 8 hours.",
                   "Below 9 hours: 9 × 60 = 540 minutes.",
                   "Above 660 minutes: 660 ÷ 60 = 11 hours. Above 720 minutes: 720 ÷ 60 = 12 hours.",
                   "Check: every number of minutes is 60 times its number of hours."],
                  "Hours: 2, 8, 11, 12. Minutes: 240, 420, 540",
                  q_figure="A double number line with hours above and minutes below and eight ticks: above, 1 hour, a "
                           "blank, 4 hours, 7 hours, a blank, 9 hours, a blank and a blank; below, 60 minutes, 120 "
                           "minutes, a blank, a blank, 480 minutes, a blank, 660 minutes and 720 minutes, with a × 2 "
                           "arrow from the first tick to the second.",
                  s_figure="The same double number line with every blank filled: above 2, 8, 11 and 12 hours, below "
                           "240, 420 and 540 minutes."),
              FIO("LUDconv.Q1b", "Let Us Do (changing units), Q1 (b)",
                  "Do as instructed. You can use the above double number line for the following conversions. (i) 1 "
                  "hour 10 minutes = ___ minutes (ii) 2 hours 45 minutes = ___ minutes (iii) 3 hours 15 minutes = ___ "
                  "minutes (iv) 4 hours 20 minutes = ___ minutes (v) 75 minutes = ___ hour ___ minutes (vi) 150 "
                  "minutes = ___ hours ___ minutes (vii) 220 minutes = ___ hours ___ minutes (viii) 390 minutes = ___ "
                  "hours ___ minutes",
                  ["(i) 1 hour = 60 minutes, so 1 hour 10 minutes is 60 + 10 = 70 minutes.",
                   "(ii) 2 hours = 2 × 60 = 120 minutes, and 120 + 45 = 165 minutes.",
                   "(iii) 3 hours = 3 × 60 = 180 minutes, and 180 + 15 = 195 minutes.",
                   "(iv) 4 hours = 4 × 60 = 240 minutes, and 240 + 20 = 260 minutes.",
                   "(v) 75 minutes: 60 minutes make 1 hour, and 75 − 60 = 15 minutes are left. So 1 hour 15 minutes.",
                   "(vi) 150 minutes: 60 × 2 = 120, and 150 − 120 = 30 minutes are left. So 2 hours 30 minutes.",
                   "(vii) 220 minutes: 60 × 3 = 180, and 220 − 180 = 40 minutes are left. So 3 hours 40 minutes.",
                   "(viii) 390 minutes: 60 × 6 = 360, and 390 − 360 = 30 minutes are left. So 6 hours 30 minutes.",
                   "Check: 3 × 60 + 40 = 220 and 6 × 60 + 30 = 390."],
                  "(i) 70; (ii) 165; (iii) 195; (iv) 260 minutes. (v) 1 hour 15 minutes; (vi) 2 hours 30 minutes; "
                  "(vii) 3 hours 40 minutes; (viii) 6 hours 30 minutes"),
              FIO("LUDconv.Q1c_line", "Let Us Do (changing units), Q1 (c) the line",
                  "Fill in the blanks in the double number line to complete the conversions. Minutes: 1 minute, ___, "
                  "5 minutes, 10 minutes, 15 minutes, ___, ___. Seconds: 60 seconds, 120 seconds, ___, ___, ___, "
                  "1200 seconds, 1500 seconds.",
                  ["Each tick is a number of minutes, and the seconds below it are 60 times as many.",
                   "Above 120 seconds: 120 ÷ 60 = 2 minutes.",
                   "Below 5 minutes: 5 × 60 = 300 seconds. The × 5 arrow joins 1 minute to 5 minutes.",
                   "Below 10 minutes: 10 × 60 = 600 seconds.",
                   "Below 15 minutes: 15 × 60 = 900 seconds.",
                   "Above 1200 seconds: 1200 ÷ 60 = 20 minutes. Above 1500 seconds: 1500 ÷ 60 = 25 minutes.",
                   "Check: 20 × 60 = 1200 and 25 × 60 = 1500."],
                  "Minutes: 2, 20, 25. Seconds: 300, 600, 900",
                  q_figure="A double number line with minutes above and seconds below and seven ticks: above, 1 "
                           "minute, a blank, 5 minutes, 10 minutes, 15 minutes, a blank and a blank; below, 60 "
                           "seconds, 120 seconds, a blank, a blank, a blank, 1200 seconds and 1500 seconds, with a × "
                           "5 arrow from 1 minute to 5 minutes and a × 60 arrow from the minutes to the seconds.",
                  s_figure="The same double number line with every blank filled: above 2, 20 and 25 minutes, below "
                           "300, 600 and 900 seconds."),
              FIO("LUDconv.Q1c_conv", "Let Us Do (changing units), Q1 (c) the conversions",
                  "(i) 320 seconds = ___ minutes ___ seconds (ii) 225 seconds = ___ minutes ___ seconds (iii) 700 "
                  "seconds = ___ minutes ___ seconds (iv) 1,000 seconds = ___ minutes ___ seconds (v) 10 minutes 13 "
                  "seconds = ___ seconds (vi) 4 minutes 8 seconds = ___ seconds (vii) 15 minutes 40 seconds = ___ "
                  "seconds",
                  ["(i) 60 × 5 = 300, and 320 − 300 = 20 seconds are left. So 5 minutes 20 seconds.",
                   "(ii) 60 × 3 = 180, and 225 − 180 = 45 seconds are left. So 3 minutes 45 seconds.",
                   "(iii) 60 × 11 = 660, and 700 − 660 = 40 seconds are left. So 11 minutes 40 seconds.",
                   "(iv) 60 × 16 = 960, and 1,000 − 960 = 40 seconds are left. So 16 minutes 40 seconds.",
                   "(v) 10 × 60 = 600, and 600 + 13 = 613 seconds.",
                   "(vi) 4 × 60 = 240, and 240 + 8 = 248 seconds.",
                   "(vii) 15 × 60 = 900, and 900 + 40 = 940 seconds.",
                   "Check: 16 × 60 = 960 and 960 + 40 = 1,000."],
                  "(i) 5 minutes 20 seconds; (ii) 3 minutes 45 seconds; (iii) 11 minutes 40 seconds; (iv) 16 minutes "
                  "40 seconds; (v) 613; (vi) 248; (vii) 940 seconds"),
              FIO("LUDconv.Q2", "Let Us Do (changing units), Q2",
                  "Raghav studies Mathematics, English, Hindi, and The World Around Us subjects. He took 50 minutes "
                  "to study each of the subjects. Find the total time taken in hours and minutes. Share your "
                  "strategies with your class.",
                  ["There are 4 subjects and each took 50 minutes.",
                   "4 × 50 = 200 minutes.",
                   "60 × 3 = 180 minutes, which is 3 hours, and 200 − 180 = 20 minutes are left.",
                   "So the total time is 3 hours 20 minutes.",
                   "Another strategy: 50 + 50 = 100 minutes is 1 hour 40 minutes for 2 subjects, and 1 hour 40 minutes "
                   "twice is 2 hours 80 minutes, which is 3 hours 20 minutes.",
                   "Check: 3 × 60 + 20 = 200 minutes."],
                  "3 hours 20 minutes. Your strategy may differ"),
          ],
          misconceptions=["M_TIME_HUNDRED"])],
    key_terms=["hours", "minutes", "seconds", "double number line"]))

# ============================== T6 Time Problems ===========================================================
TOPICS.append(TOPIC(
    "T6", "M3", "Time Problems", ["Let Us Do (time problems)"], "Apply",
    "Students find the time after and the time before a given time by adding or taking away hours and then minutes, "
    "and say the new time when the time crosses 12 noon or midnight.",
    "To find the time after a time, add the hours first, then hop to the next whole hour and add the minutes left. To "
    "find the time before, go back the same way. When the time passes 12 noon, a.m. changes to p.m., and a time "
    "above 24:00 hours is in the next day.",
    [A("T6.C1", "Time After", "Apply",
       "Students find the time after a start time by adding the hours first and then the minutes in easy hops, "
       "without writing minutes above 59.",
       teach=["Predict first: Zainab starts painting at 03:20 p.m. and paints for 1 hour 50 minutes. Will she stop "
              "before 05:00 p.m., or after it?",
              "Add the hours first. 03:20 p.m. plus 1 hour is 04:20 p.m.",
              "Then add the minutes in easy hops. From 04:20 p.m. it is 60 − 20 = 40 minutes to 05:00 p.m. 50 − 40 = "
              "10 minutes are left, so go 10 minutes past 05:00 p.m. That is 05:10 p.m., after 05:00 p.m.",
              "Minutes on a clock never go past 59. After 60 minutes the hour goes up by 1, so 04:20 p.m. plus 50 "
              "minutes is not 04:70 p.m.",
              "Do these in your head with hops, not by writing the numbers in columns.",
              "Rule: add the hours, then hop to the next whole hour, then add the minutes left."],
       examples=[WE("Zainab starts painting at 03:20 p.m. and paints for 1 hour 50 minutes. At what time does she "
                    "stop?",
                    ["Add the hours first: 03:20 p.m. plus 1 hour is 04:20 p.m.",
                     "From 04:20 p.m. to 05:00 p.m. is 60 − 20 = 40 minutes.",
                     "50 − 40 = 10 minutes are left to add.",
                     "05:00 p.m. plus 10 minutes is 05:10 p.m.",
                     "So Zainab stops at 05:10 p.m.",
                     "Check by going back: 05:10 p.m. minus 1 hour is 04:10 p.m., and 04:10 p.m. minus 50 minutes is "
                     "03:20 p.m."],
                    "05:10 p.m.")],
       ncert=["note.oral"],
       key_terms=["time after", "hops", "next whole hour"],
       misconceptions=["M_MINUTES_OVER_59"], minutes=6),
     A("T6.C2", "Time Before", "Apply",
       "Students find the start time before a finish time by going back the hours first and then the minutes in easy "
       "hops, and check by going forward.",
       teach=["Predict first: Remo finished reading at 08:15 p.m. after reading for 2 hours 40 minutes. Did he start "
              "before 06:00 p.m., or after it?",
              "Go back the hours first. 08:15 p.m. minus 2 hours is 06:15 p.m.",
              "Then go back the minutes in easy hops. From 06:15 p.m. back to 06:00 p.m. is 15 minutes. 40 − 15 = 25 "
              "minutes are left, so go 25 minutes before 06:00 p.m. That is 05:35 p.m., before 06:00 p.m.",
              "Going back is the same hops the other way round.",
              "Check by going forward: 05:35 p.m. plus 2 hours 40 minutes should give 08:15 p.m.",
              "Rule: go back the hours, then hop back to the whole hour, then go back the minutes left."],
       examples=[WE("Remo finished reading at 08:15 p.m. He read for 2 hours 40 minutes. At what time did he start?",
                    ["Go back the hours first: 08:15 p.m. minus 2 hours is 06:15 p.m.",
                     "From 06:15 p.m. back to 06:00 p.m. is 15 minutes.",
                     "40 − 15 = 25 minutes are left to go back.",
                     "06:00 p.m. minus 25 minutes is 05:35 p.m.",
                     "So Remo started at 05:35 p.m.",
                     "Check by going forward: 05:35 p.m. plus 2 hours is 07:35 p.m., and 07:35 p.m. plus 40 minutes "
                     "is 08:15 p.m."],
                    "05:35 p.m.")],
       key_terms=["time before", "going back", "start time"],
       misconceptions=["M_MINUTES_OVER_59"], minutes=6),
     A("T6.C3", "Crossing Noon and Midnight", "Apply",
       "Students find the time after a start time when the time crosses 12 noon or midnight, using the 24-hour "
       "clock, and say the new time with a.m. or p.m.",
       teach=["Predict first: a bus leaves at 10:40 a.m. and the trip takes 3 hours 30 minutes. Will it arrive in the "
              "morning (a.m.) or in the afternoon (p.m.)?",
              "When the clock goes past 12 noon, the a.m. changes to p.m. This bus passes 12 noon, so it arrives in "
              "the afternoon.",
              "Midnight is the end of the day, 24:00 hours. A new day begins at 00:00 hours.",
              "To cross noon or midnight, change to the 24-hour clock and add there. 10:40 a.m. is 10:40 hours. 10:40 "
              "hours plus 3 hours 30 minutes is 14:10 hours, and 14 − 12 = 2, so it is 02:10 p.m.",
              "If the 24-hour time goes above 24:00 hours, take 24 away. 28:00 hours is 28 − 24 = 4, so it is 04:00 "
              "hours the next day.",
              "Rule: use the 24-hour clock to cross noon and midnight. A time above 24:00 hours is in the next day."],
       examples=[WE("(a) A bus leaves at 10:40 a.m. and the trip takes 3 hours 30 minutes. When does it arrive? (b) A "
                    "train leaves at 10:15 p.m. and the journey takes 5 hours 45 minutes. When does it arrive?",
                    ["(a) 10:40 a.m. is a morning time, so it is 10:40 hours.",
                     "10:40 hours plus 3 hours is 13:40 hours.",
                     "From 13:40 hours to 14:00 hours is 20 minutes, and 30 − 20 = 10 minutes are left, so 14:10 "
                     "hours.",
                     "14 − 12 = 2, so 14:10 hours is 02:10 p.m. The clock passed 12 noon, so a.m. changed to p.m.",
                     "(b) 10:15 p.m. is 10 + 12 = 22, so it is 22:15 hours.",
                     "22:15 hours plus 5 hours is 27:15 hours. 27:15 hours plus 45 minutes is 28:00 hours, because 15 "
                     "+ 45 = 60 minutes make 1 more hour.",
                     "A day ends at 24:00 hours, so take 24 away: 28 − 24 = 4. The train arrives at 04:00 hours, "
                     "which is 04:00 a.m. the next day.",
                     "Check: 10:15 p.m. to midnight is 1 hour 45 minutes, and midnight to 04:00 a.m. is 4 hours. 1 "
                     "hour 45 minutes plus 4 hours is 5 hours 45 minutes."],
                    "(a) 02:10 p.m. (b) 04:00 a.m. the next day")],
       key_terms=["12 noon", "midnight", "24-hour clock", "next day"],
       misconceptions=["M_PAST_24", "M_NOON_AM"], minutes=7),
     DOER("T6.C4", "Practice: Time Jumper", "time_jumper", "Apply",
          "Students find the time after and the time before a given time with hops of hours and minutes, including "
          "across 12 noon and midnight, in the book's time problems.",
          ["To find the time after, add the hours first, then hop to the next whole hour and add the minutes left.",
           "To find the time before, go back the hours first, then hop back to the whole hour and go back the minutes "
           "left.",
           "When the time passes 12 noon, a.m. changes to p.m. A 24-hour time above 24:00 hours is in the next day: "
           "take 24 away."],
          items=[
              FIO("LUDtime.Q4", "Let Us Do (time problems), Q4",
                  "Jyoti went to play at 06:15 PM. She came back after 1 hour 45 minutes. At what time did she reach "
                  "home?",
                  ["Add the hours first: 06:15 PM plus 1 hour is 07:15 PM.",
                   "From 07:15 PM to 08:00 PM is 60 − 15 = 45 minutes, and 45 minutes is all the minutes to add.",
                   "So 07:15 PM plus 45 minutes is 08:00 PM.",
                   "Check by going back: 08:00 PM minus 1 hour is 07:00 PM, and 07:00 PM minus 45 minutes is 06:15 "
                   "PM."],
                  "08:00 PM"),
              FIO("LUDtime.Q5", "Let Us Do (time problems), Q5",
                  "Ragini took 1 hour 10 minutes to do her homework. She finished it at 09:40 PM. What time did she "
                  "start?",
                  ["Go back the hours first: 09:40 PM minus 1 hour is 08:40 PM.",
                   "Go back the 10 minutes: 08:40 PM minus 10 minutes is 08:30 PM.",
                   "So Ragini started at 08:30 PM.",
                   "Check by going forward: 08:30 PM plus 1 hour is 09:30 PM, and 09:30 PM plus 10 minutes is 09:40 "
                   "PM."],
                  "08:30 PM"),
              FIO("LUDtime.Q6", "Let Us Do (time problems), Q6",
                  "A group of children left for a picnic at 08:30 AM. They returned after 4 hours and 10 minutes. At "
                  "what time did they return?",
                  ["Add the hours first: 08:30 AM plus 4 hours is 12:30 PM. The clock passes 12 noon, so AM changes "
                   "to PM.",
                   "Add the 10 minutes: 12:30 PM plus 10 minutes is 12:40 PM.",
                   "So the children returned at 12:40 PM.",
                   "Check in 24-hour time: 08:30 hours plus 4 hours 10 minutes is 12:40 hours, and 12:40 hours is "
                   "12:40 PM."],
                  "12:40 PM"),
              FIO("LUDtime.Q7", "Let Us Do (time problems), Q7",
                  "Raji started her homework at 06:00 PM. She finished her homework in 1 hour 30 minutes. At what "
                  "time did she finish?",
                  ["Add the hours first: 06:00 PM plus 1 hour is 07:00 PM.",
                   "Add the 30 minutes: 07:00 PM plus 30 minutes is 07:30 PM.",
                   "So Raji finished at 07:30 PM.",
                   "Check by going back: 07:30 PM minus 1 hour 30 minutes is 06:00 PM."],
                  "07:30 PM"),
              FIO("LUDtime.Q8", "Let Us Do (time problems), Q8",
                  "Alya goes out to play at 05:30 PM and comes back after 1 hour 10 minutes. At what time does she "
                  "come back?",
                  ["Add the hours first: 05:30 PM plus 1 hour is 06:30 PM.",
                   "Add the 10 minutes: 06:30 PM plus 10 minutes is 06:40 PM.",
                   "So Alya comes back at 06:40 PM.",
                   "Check by going back: 06:40 PM minus 1 hour is 05:40 PM, and 05:40 PM minus 10 minutes is 05:30 "
                   "PM."],
                  "06:40 PM"),
              FIO("LUDtime.Q9", "Let Us Do (time problems), Q9",
                  "If the lunch break of a school starts at 12:30 PM and ends in 35 minutes, what time will lunch "
                  "end?",
                  ["From 12:30 PM to 01:00 PM is 30 minutes.",
                   "35 − 30 = 5 minutes are left to add.",
                   "01:00 PM plus 5 minutes is 01:05 PM. On the 12-hour clock, after 12:59 the time goes to 01:00.",
                   "So the lunch break ends at 01:05 PM.",
                   "Check in 24-hour time: 12:30 hours plus 35 minutes is 13:05 hours, and 13 − 12 = 1, so 01:05 PM."],
                  "01:05 PM"),
              FIO("LUDtime.Q10", "Let Us Do (time problems), Q10",
                  "It is 08:35 PM right now. What time will it be after 8 hours and 25 minutes?",
                  ["08:35 PM is a p.m. time, so add 12 to the hour: 8 + 12 = 20, and it is 20:35 hours.",
                   "Add the 25 minutes first: 20:35 hours plus 25 minutes is 21:00 hours.",
                   "Add the 8 hours: 21:00 hours plus 8 hours is 29:00 hours.",
                   "A day ends at 24:00 hours, so take 24 away: 29 − 24 = 5. The time is 05:00 hours the next day.",
                   "05:00 hours is a morning time, so it is 05:00 AM the next day.",
                   "Check: 08:35 PM to midnight is 3 hours 25 minutes, and midnight to 05:00 AM is 5 hours. 3 hours 25 "
                   "minutes plus 5 hours is 8 hours 25 minutes."],
                  "05:00 AM the next day"),
          ],
          misconceptions=["M_MINUTES_OVER_59", "M_PAST_24", "M_NOON_AM"])],
    key_terms=["time after", "time before", "noon", "midnight"]))
