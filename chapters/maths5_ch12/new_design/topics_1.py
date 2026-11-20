# -*- coding: utf-8 -*-
"""Topics T1, T1B and T2 (module M1: Clock Time, Time Elapsed and Two Ways to Write the Time) of Class 5 Chapter 12,
Racing Seconds. The framing intro (Raghav's morning yoga hook and the free Yoga Clock), the short idea topic T1B (how
long did it take: time elapsed and comparing times taken, with the opener's Let us find out Q1 to Q5), and T2 (12-hour
and 24-hour time, with Let us find out Q6, Q7 and the solved example about Raghu's trip).
Every teaching concept has one worked example with the plan's own numbers; every book question is an FIO item of its
topic's DOER, in the book's order."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Raghav's Morning Yoga (framing) =========================================
# The framing topic holds only the hook video and the free-try tool, and no book question. The concept video and the
# opener's questions follow in the short idea topic T1B.
TOPICS.append(TOPIC(
    "T1", "M1", "Raghav's Morning Yoga", ["Chapter opening"], "Understand",
    "",
    "Raghav practices yoga in the morning. He looks at the wall clock when he starts and again when he finishes. Try "
    "the two clocks and find out how much time went by.",
    [A("T1.C1", "Raghav's Morning Yoga", "Understand",
       "",
       textbook=["Raghav practices yoga in the morning."],
       teach=["Predict first: Raghav looks at the wall clock when he starts his yoga and again when he finishes. Will "
              "the hands of the clock be in the same places both times?",
              "Raghav practices yoga in the morning.",
              "Before he begins, he stands on his mat and looks at the wall clock. When he finishes, he sits on the "
              "mat and looks at the clock again.",
              "The hands are in different places on the two clocks. How much time went by? Think about it, then try it "
              "with two clocks on the next screen."],
       ncert=["open.story"], key_terms=["clock", "time", "yoga"],
       video_focus=["HOOK"], enrichment=True, minutes=4),
     DOER("T1.C3", "Yoga Clock: Explore", "yoga_clock", "Understand",
          "",
          ["Raghav looked at the wall clock before his yoga and again after it.",
           "Set a Start clock and a Finish clock, read both times and see how much time lies between them.",
           "The short blue hand shows the hour. The long orange hand shows the minutes."],
          misconceptions=["M_MINUTE_NUMBER"], role="try_it", enrichment=True)],
    topic_type="framing", key_terms=["clock", "time", "yoga"]))

# ============================== T1B How Long Did It Take? ==================================================
TOPICS.append(TOPIC(
    "T1B", "M1", "How Long Did It Take?", ["Let us find out"], "Apply",
    "Students find the time between two clock times in hours and minutes, and compare times taken to say which is the "
    "longest and which is the least.",
    "To find how long it took, start at the earlier time and count up to the later time in easy hops: to the next "
    "whole hour, then whole hours, then the rest of the minutes. To compare times taken, compare the hours first and, "
    "if the hours are the same, compare the minutes.",
    [A("T1B.C1", "Time Elapsed Between Two Times", "Apply",
       "Students find the time elapsed between two clock times by counting up in easy hops, and say it in hours and "
       "minutes.",
       teach=["Predict first: Remo began reading at 03:10 p.m. and stopped at 03:50 p.m. Did he read for more than 1 "
              "hour or for less than 1 hour?",
              "Less than 1 hour. Both times are in the same hour, 3, so take the smaller minutes from the bigger "
              "minutes: 50 − 10 = 40 minutes.",
              "To read a clock: the short blue hand shows the hour and the long orange hand shows the minutes. Each "
              "number on the dial is 5 minutes, so the minute hand on 4 means 4 × 5 = 20 minutes, not 4 minutes.",
              "Same minutes: count the hours. 02:20 p.m. to 06:20 p.m. is 6 − 2 = 4 hours.",
              "Different hours and minutes: hop to the next whole hour, then hop whole hours, then add the rest. 1 "
              "hour is 60 minutes, so 10:35 a.m. to 11:00 a.m. is 60 − 35 = 25 minutes. You can also hop whole hours "
              "first and then the rest.",
              "Rule: start at the earlier time and count up to the later time in easy hops."],
       examples=[WE("Zainab started colouring at 04:25 p.m. and stopped at 05:10 p.m. (a) How long did she colour? "
                    "Then: (b) How long is it from 07:20 a.m. to 10:50 a.m.?",
                    ["(a) Hop to the next whole hour. 04:25 p.m. to 05:00 p.m. is 60 − 25 = 35 minutes.",
                     "05:00 p.m. to 05:10 p.m. is 10 minutes.",
                     "35 + 10 = 45 minutes, so Zainab coloured for 45 minutes.",
                     "(b) Hop whole hours first. 07:20 a.m. to 10:20 a.m. is 10 − 7 = 3 hours.",
                     "10:20 a.m. to 10:50 a.m. is 50 − 20 = 30 minutes.",
                     "So the time from 07:20 a.m. to 10:50 a.m. is 3 hours 30 minutes.",
                     "Check: 07:20 a.m. plus 3 hours is 10:20 a.m., and 10:20 a.m. plus 30 minutes is 10:50 a.m."],
                    "(a) 45 minutes (b) 3 hours 30 minutes")],
       key_terms=["time elapsed", "minute hand", "hour hand"],
       misconceptions=["M_MINUTE_NUMBER", "M_TIME_HUNDRED"], minutes=6),
     A("T1B.C2", "Comparing Times Taken", "Apply",
       "Students compare times taken that are given in hours and minutes, and say which is the longest and which is "
       "the least.",
       teach=["Predict first: Akira took 1 hour 55 minutes and Sunita took 2 hours 5 minutes to paint a picture. Who "
              "took longer?",
              "Sunita took longer. Look at the hours first: Sunita has 2 hours and Akira has only 1 hour. The minutes "
              "only matter when the hours are the same.",
              "Check in minutes: 1 hour 55 minutes is 60 + 55 = 115 minutes and 2 hours 5 minutes is 120 + 5 = 125 "
              "minutes. 125 is more than 115.",
              "When the hours are the same, compare the minutes: 2 hours 10 minutes is less than 2 hours 40 minutes, "
              "because 10 is less than 40.",
              "Rule: compare the hours first. If the hours are the same, compare the minutes. The longest time is the "
              "biggest and the least time is the smallest."],
       examples=[WE("Zainab took 1 hour 50 minutes, Remo took 1 hour 25 minutes and Mary took 2 hours 5 minutes to "
                    "finish a puzzle. Who took the longest time and who took the least?",
                    ["Compare the hours first. Zainab has 1 hour, Remo has 1 hour and Mary has 2 hours.",
                     "Mary has the most hours, so Mary took the longest time.",
                     "Zainab and Remo have the same hours, so compare their minutes.",
                     "25 minutes is less than 50 minutes, so Remo took less time than Zainab. Remo took the least "
                     "time.",
                     "Check in minutes: Zainab 60 + 50 = 110, Remo 60 + 25 = 85 and Mary 120 + 5 = 125.",
                     "125 is the most and 85 is the least, so Mary is the longest and Remo is the least."],
                    "Mary took the longest time and Remo took the least time")],
       key_terms=["compare", "longest", "least", "times taken"],
       misconceptions=["M_MINUTES_FIRST"], minutes=5),
     DOER("T1B.C3", "Practice: How Long Did It Take?", None, "Apply",
          "Students read two clocks to find the start time, the finish time and how long Raghav took, find how long it "
          "is between two times, and compare times taken in hours and minutes.",
          ["Read a clock like this: the short hand shows the hour and the long hand shows the minutes, 5 minutes for "
           "each number.",
           "To find the time elapsed, count up from the earlier time to the later time in easy hops: to the next whole "
           "hour, then whole hours, then the rest.",
           "To compare times taken, compare the hours first and then the minutes."],
          items=[FIO("LFO.Q1", "Let us find out: Raghav's start time",
                     "Raghav practices yoga in the morning. At what time did Raghav start practising Yoga? ___",
                     ["Look at the first clock. The short blue hand is between 5 and 6, so the hour is 5.",
                      "The long orange hand is on 7. Each number on the dial is 5 minutes.",
                      "7 × 5 = 35 minutes.",
                      "The time is 05:35. Raghav practices yoga in the morning, so it is a.m.",
                      "Check: the hour hand is between 5 and 6, so the time is after 05:00 and before 06:00, and "
                      "05:35 is in that stretch."],
                     "05:35 a.m.",
                     q_figure="Two wall clocks hang above Raghav's yoga mat: the first has the hour hand between 5 and "
                              "6 and the minute hand on 7, and the second has the hour hand just before 6 and the "
                              "minute hand on 11.",
                     s_figure="The first wall clock with the minute hand on 7 marked 7 × 5 = 35 minutes and the hour "
                              "hand between 5 and 6, and the time 05:35 a.m. written under it."),
                 FIO("LFO.Q2", "Let us find out: Raghav's finish time",
                     "Raghav practices yoga in the morning. At what time did he finish? ___",
                     ["Look at the second clock. The short blue hand is just before 6, so the hour is 5.",
                      "The long orange hand is on 11. Each number on the dial is 5 minutes.",
                      "11 × 5 = 55 minutes.",
                      "The time is 05:55. It is the morning, so it is a.m.",
                      "Check: 55 minutes is 5 minutes short of 60, so the time is 5 minutes before 06:00, and the "
                      "hour hand is almost on 6."],
                     "05:55 a.m.",
                     q_figure="Two wall clocks hang above Raghav's yoga mat: the first has the hour hand between 5 and "
                              "6 and the minute hand on 7, and the second has the hour hand just before 6 and the "
                              "minute hand on 11.",
                     s_figure="The second wall clock with the minute hand on 11 marked 11 × 5 = 55 minutes and the "
                              "hour hand just before 6, and the time 05:55 a.m. written under it."),
                 FIO("LFO.Q3", "Let us find out: time spent on yoga",
                     "Raghav practices yoga in the morning. How much time did he spend practising Yoga? ___",
                     ["Raghav started at 05:35 a.m. and finished at 05:55 a.m.",
                      "Both times are in the same hour, 5, so take the smaller minutes from the bigger minutes.",
                      "55 − 35 = 20 minutes.",
                      "So Raghav spent 20 minutes on yoga.",
                      "Check: 05:35 a.m. plus 20 minutes is 05:55 a.m., because 35 + 20 = 55."],
                     "20 minutes",
                     q_figure="Two wall clocks hang above Raghav's yoga mat: the first has the hour hand between 5 and "
                              "6 and the minute hand on 7, and the second has the hour hand just before 6 and the "
                              "minute hand on 11.",
                     s_figure="Both wall clocks side by side with 05:35 a.m. and 05:55 a.m. written under them, and "
                              "the stretch between the two minute hands shaded and labelled 20 minutes."),
                 FIO("LFO.Q4", "Let us find out: time elapsed",
                     "Find the time elapsed between the given time periods. Share your strategies. (a) 01:15 p.m. to "
                     "01:42 p.m.? (b) 03:18 p.m. to 08:18 p.m.? (c) 09:15 a.m. to 11:30 a.m.?",
                     ["(a) Both times are in the same hour, 1, so take the smaller minutes from the bigger minutes.",
                      "42 − 15 = 27 minutes.",
                      "(b) The minutes are the same, 18, so count the hours.",
                      "8 − 3 = 5 hours.",
                      "(c) Hop whole hours first. 09:15 a.m. to 11:15 a.m. is 11 − 9 = 2 hours.",
                      "11:15 a.m. to 11:30 a.m. is 30 − 15 = 15 minutes, so the answer to part (c) is 2 hours 15 minutes.",
                      "Share your strategy: you can hop to the next whole hour, or count the hours first. Another "
                      "strategy may also work.",
                      "Check: 01:15 p.m. plus 27 minutes is 01:42 p.m., 03:18 p.m. plus 5 hours is 08:18 p.m., and "
                      "09:15 a.m. plus 2 hours 15 minutes is 11:30 a.m."],
                     "(a) 27 minutes (b) 5 hours (c) 2 hours 15 minutes. Your strategy may differ.",
                     s_figure="Three time lines: 01:15 p.m. to 01:42 p.m. with one hop of 27 minutes, 03:18 p.m. to "
                              "08:18 p.m. with one hop of 5 hours, and 09:15 a.m. to 11:30 a.m. with a hop of 2 hours "
                              "and a hop of 15 minutes."),
                 FIO("LFO.Q5", "Let us find out: time taken to paint a picture",
                     "The table below shows the time taken by 3 children to paint a picture. Raghav: 1 hour 20 "
                     "minutes. Rani: 2 hours 10 minutes. Ritu: 1 hour 35 minutes. (a) Who took the longest time? "
                     "(b) Who took the least time?",
                     ["Compare the hours first. Raghav has 1 hour, Rani has 2 hours and Ritu has 1 hour.",
                      "Rani has the most hours, so Rani took the longest time.",
                      "Raghav and Ritu both have 1 hour, so compare their minutes.",
                      "20 minutes is less than 35 minutes, so Raghav took the least time.",
                      "Check in minutes: Raghav 60 + 20 = 80, Rani 120 + 10 = 130 and Ritu 60 + 35 = 95. The most is "
                      "130 (Rani) and the least is 80 (Raghav)."],
                     "(a) Rani, 2 hours 10 minutes (b) Raghav, 1 hour 20 minutes",
                     q_figure="A table with the heads Name and Time Taken and three rows: Raghav 1 hour 20 minutes, "
                              "Rani 2 hours 10 minutes and Ritu 1 hour 35 minutes.",
                     s_figure="The same table with Rani's row marked longest and Raghav's row marked least, and the "
                              "times in minutes, 80, 130 and 95, written beside the rows.")],
          misconceptions=["M_MINUTE_NUMBER", "M_TIME_HUNDRED", "M_MINUTES_FIRST"])],
    key_terms=["time elapsed", "times taken", "compare"]))

# ============================== T2 12-Hour and 24-Hour Time ================================================
TOPICS.append(TOPIC(
    "T2", "M1", "12-Hour and 24-Hour Time", ["Let us find out", "Let Us Do (time between two 24-hour times)"], "Apply",
    "Students write a time in the 12-hour format and in the 24-hour format, both ways, and find how long it is "
    "between two 24-hour times.",
    "A day has 24 hours. The 12-hour clock goes round twice and says a.m. or p.m. The 24-hour format counts once from "
    "00:00 to 24:00 and says hours. A morning time keeps its digits, a p.m. time adds 12 to the hour, and the minutes "
    "never change. To find the time between two 24-hour times, hop to the next whole hour, then whole hours, then "
    "the rest.",
    [A("T2.C1", "Two Ways to Write the Time", "Apply",
       "Students write a time in the 12-hour format and in the 24-hour format, changing it both ways.",
       teach=["Predict first: a day has 24 hours, but a 12-hour clock only counts up to 12. How does it tell 05:30 in "
              "the morning from 05:30 in the evening?",
              "It adds a.m. or p.m. A day has 24 hours, so the 12-hour clock goes round twice. The first round is the "
              "morning (a.m.). The second round is the afternoon and evening (p.m.).",
              "The 24-hour format counts once, from 00:00 to 24:00. It does not use a.m. or p.m. It writes the word "
              "hours after the time.",
              "A morning time keeps its digits: 05:30 a.m. is 05:30 hours.",
              "For a p.m. time, add 12 to the hour: 02:30 p.m. is 2 + 12 = 14, so it is 14:30 hours.",
              "The minutes never change. To go back from a 24-hour time above 12, take 12 away from the hour.",
              "Rule: a morning time keeps its digits. For a p.m. time, add 12 to the hour. The minutes stay the "
              "same."],
       examples=[WE("(a) Write 07:45 p.m. in the 24-hour format. (b) Write 16:20 hours in the 12-hour format.",
                    ["(a) 07:45 p.m. is a p.m. time, so add 12 to the hour.",
                     "7 + 12 = 19.",
                     "The minutes stay 45, so 07:45 p.m. is 19:45 hours.",
                     "(b) 16 is more than 12, so it is a p.m. time. Take 12 away from the hour.",
                     "16 − 12 = 4.",
                     "The minutes stay 20, so 16:20 hours is 04:20 p.m.",
                     "Check: going back, 4 + 12 = 16 and 19 − 12 = 7, so both answers match."],
                    "(a) 19:45 hours (b) 04:20 p.m.")],
       key_terms=["12-hour format", "24-hour format", "a.m.", "p.m."],
       misconceptions=["M_PM_SAME"], minutes=6),
     A("T2.C2", "Time Between in 24-Hour Time", "Apply",
       "Students find how long it is between two 24-hour times by hopping to the next whole hour, then whole hours, "
       "then the rest, and say it in hours and minutes.",
       teach=["Predict first: Raghu's art class starts at 15:20 hours and ends at 17:05 hours. Is it longer than 2 "
              "hours or shorter than 2 hours?",
              "Shorter. With 24-hour times there is no a.m. or p.m. to keep track of, so just count up from the "
              "earlier time to the later time.",
              "Hop to the next whole hour: 15:20 hours to 16:00 hours is 60 − 20 = 40 minutes.",
              "Hop whole hours: 16:00 hours to 17:00 hours is 17 − 16 = 1 hour.",
              "Add the rest: 17:00 hours to 17:05 hours is 5 minutes. 40 + 5 = 45 minutes, so the class lasts 1 hour "
              "45 minutes. That is shorter than 2 hours.",
              "Hop in your head instead of subtracting in columns, because an hour has 60 minutes and not 100.",
              "Rule: go to the next whole hour, add the whole hours, then add the rest of the minutes."],
       examples=[WE("A drawing class starts at 13:40 hours and ends at 16:15 hours. How long does it last?",
                    ["13:40 hours to 14:00 hours is 60 − 40 = 20 minutes.",
                     "14:00 hours to 16:00 hours is 16 − 14 = 2 hours.",
                     "16:00 hours to 16:15 hours is 15 minutes.",
                     "20 + 15 = 35 minutes.",
                     "So the drawing class lasts 2 hours 35 minutes.",
                     "Check: 13:40 hours plus 2 hours is 15:40 hours, and 15:40 hours plus 35 minutes is 16:15 "
                     "hours."],
                    "2 hours 35 minutes")],
       key_terms=["24-hour time", "next whole hour", "time between"],
       misconceptions=["M_MINUTES_OVER_59", "M_PM_SAME"], minutes=6),
     DOER("T2.C3", "Practice: Clock Formats", "day_strip", "Apply",
          "Students write times in the 12-hour and 24-hour formats, match them, and find the time between two "
          "24-hour times.",
          ["A morning time keeps its digits in the 24-hour format. A p.m. time adds 12 to the hour. The minutes never "
           "change.",
           "To go back from a 24-hour time above 12 to a p.m. time, take 12 away from the hour.",
           "To find the time between two 24-hour times, hop to the next whole hour, then whole hours, then the rest."],
          items=[FIO("LFO.Q6", "Let us find out: the 12-hour and 24-hour table",
                     "Fill in the blanks by writing the time in the appropriate format. 12-hour format and 24-hour "
                     "format: 05:30 a.m. = 05:30 hours; ___ = 08:35 hours; 11:55 a.m. = ___ hours; 02:30 p.m. = 14:30 "
                     "hours; 05:30 p.m. = ___ hours; 09:35 p.m. = ___ hours.",
                     ["The rule: a morning time keeps its digits, and a p.m. time adds 12 to the hour. The minutes "
                      "never change.",
                      "Second row: 08 is less than 12, so 08:35 hours is a morning time, 08:35 a.m.",
                      "Third row: 11:55 a.m. is a morning time, so it keeps its digits: 11:55 hours.",
                      "Fifth row: 05:30 p.m. is a p.m. time, so add 12 to the hour. 5 + 12 = 17, so it is 17:30 "
                      "hours.",
                      "Sixth row: 09:35 p.m. is a p.m. time, so add 12 to the hour. 9 + 12 = 21, so it is 21:35 "
                      "hours.",
                      "Check: going back, 17 − 12 = 5 and 21 − 12 = 9, so 17:30 hours is 05:30 p.m. and 21:35 hours "
                      "is 09:35 p.m."],
                     "Second row: 08:35 a.m. Third row: 11:55 hours. Fifth row: 17:30 hours. Sixth row: 21:35 hours.",
                     q_figure="A table with the heads 12-hour format and 24-hour format and a small digital clock "
                              "reading 24:00 above the second column, with six rows: 05:30 a.m. and 05:30 hours, a "
                              "blank and 08:35 hours, 11:55 a.m. and a blank, 02:30 p.m. and 14:30 hours, 05:30 p.m. "
                              "and a blank, 09:35 p.m. and a blank.",
                     s_figure="The same table with every blank filled in: 08:35 a.m., 11:55 hours, 17:30 hours and "
                              "21:35 hours."),
                 FIO("LFO.Q7", "Let us find out: match the formats",
                     "Match the following. 12-hour format: 06:30 a.m., 08:45 p.m., 11:45 p.m., 04:30 a.m., 07:30 p.m., "
                     "01:30 a.m. 24-hour format: 01:30 hours, 23:45 hours, 06:30 hours, 20:45 hours, 04:30 hours, "
                     "19:30 hours.",
                     ["The rule: a morning time keeps its digits, and a p.m. time adds 12 to the hour.",
                      "06:30 a.m. is a morning time, so it keeps its digits: 06:30 hours.",
                      "04:30 a.m. is a morning time, so it keeps its digits: 04:30 hours.",
                      "01:30 a.m. is a morning time, so it keeps its digits: 01:30 hours.",
                      "08:45 p.m. is a p.m. time. 8 + 12 = 20, so it is 20:45 hours.",
                      "11:45 p.m. is a p.m. time. 11 + 12 = 23, so it is 23:45 hours.",
                      "07:30 p.m. is a p.m. time. 7 + 12 = 19, so it is 19:30 hours.",
                      "Check: all six pairs are different, and every 24-hour time in the list is used once."],
                     "06:30 a.m. with 06:30 hours; 08:45 p.m. with 20:45 hours; 11:45 p.m. with 23:45 hours; "
                     "04:30 a.m. with 04:30 hours; 07:30 p.m. with 19:30 hours; 01:30 a.m. with 01:30 hours",
                     q_figure="Two columns of six boxes: the 12-hour format column holds 06:30 a.m., 08:45 p.m., "
                              "11:45 p.m., 04:30 a.m., 07:30 p.m. and 01:30 a.m., and the 24-hour format column holds "
                              "01:30 hours, 23:45 hours, 06:30 hours, 20:45 hours, 04:30 hours and 19:30 hours.",
                     s_figure="The same two columns with six lines, each joining a 12-hour time to its 24-hour time, "
                              "for example 08:45 p.m. to 20:45 hours."),
                 FIO("ex.nana", "Example 1: Raghu's trip to his Nana ji's house",
                     "Raghu left his house at 08:00 hours and arrived at his Nana ji's house at 09:05 hours. How long "
                     "did he take to reach his house?",
                     ["Raghu left at 08:00 hours and arrived at 09:05 hours.",
                      "08:00 hours to 09:00 hours is 1 hour.",
                      "09:00 hours to 09:05 hours is 5 minutes.",
                      "So Raghu took 1 hour 5 minutes to reach his Nana ji's house.",
                      "Check: 08:00 hours plus 1 hour is 09:00 hours, and 09:00 hours plus 5 minutes is 09:05 hours."],
                     "1 hour 5 minutes",
                     kind="example",
                     s_figure="A time line from 08:00 hours to 09:05 hours with a hop of 1 hour to 09:00 hours and a "
                              "hop of 5 minutes to 09:05 hours.")],
          misconceptions=["M_PM_SAME", "M_MINUTES_OVER_59"])],
    key_terms=["12-hour format", "24-hour format", "time between"]))
