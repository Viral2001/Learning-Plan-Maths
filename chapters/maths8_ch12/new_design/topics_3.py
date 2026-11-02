# -*- coding: utf-8 -*-
"""Topics T11 (module M3, projects) and T12 (summary and Hex). Book pp 131 to 134."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T11 Independent data project ================================================
TOPICS.append(TOPIC(
    "T11", "M3", "Your Own Data Story", ["5.2"], "Create",
    "Students plan a data investigation of their own day, collect values, summarise them with a mean and a median, "
    "show them on a strip or a graph, compare with an adult or with a group, and report findings and new questions.",
    "A good investigation asks a clear question, collects data, summarises it with a mean and median, shows it in "
    "a graph, and ends with what we found and what we still wonder.",
    [A("T11.C1", "Plan your own investigation", "Create",
       "Students choose a question about their own day, decide what to record and for how many days, and describe "
       "how they will summarise and show the data.",
       textbook=["Individual project: Make your own activity strip for different days of the week.",
                 "Do you eat and sleep at regular times every day? Typically how long do you spend outdoors?",
                 "Calculate the average time spent per activity. Represent this average day using a strip.",
                 "Similarly, track the activities of any adult at home. Compare your data with theirs."],
       teach=["Predict first: do you eat and sleep at the same time every day? Write your guess before you collect "
              "any data.",
              "Record each activity for several days. For each activity, add the times and divide by the number of "
              "days to get the average. Colour an average day on a strip.",
              "Track an adult at home the same way and compare the two strips."],
       examples=[
           WE("Over 3 days you spend 1.5 hours, 2 hours and 1 hour outdoors. What is the average time outdoors, "
              "and how many boxes is it on a strip?",
              ["Add the three days: 1.5 + 2 + 1 = 4.5 hours.", "Divide by 3: 4.5 ÷ 3 = 1.5 hours.",
               "Each hour is 2 boxes, so 1.5 × 2 = 3 boxes."],
              "1.5 hours a day, which is 3 boxes on the strip")],
       ncert=[], key_terms=["investigation", "average"], misconceptions=["M_MEAN_DATA"], minutes=8),
     A("T11.C2", "A group project: family sleep or school timings", "Create",
       "Students choose one group investigation, either a week of family sleep or the daily timings of Grade 8 "
       "schools, and decide how to combine the data of all members using the mean and median.",
       textbook=["Small group project: Make a group of 3 to 4 members. Do at least one of the following:",
                 "Track daily sleep time of all your family members for a week. Daily sleep time includes night "
                 "sleep, naps, and any sleep during the day. Represent this on strips. Put together the data of all "
                 "your group members. Calculate the average and median sleep time of children, adults, elderly. "
                 "Share your findings and observations.",
                 "When do schools start and end? On a weekday, Manoj's school starts at 9:30 am and ends at 4:30 pm, "
                 "i.e., 7 hours which include class time and breaks. Collect information on the daily timings of "
                 "different schools for Grade 8, including class time and break time. Analyse and present the data "
                 "collected."],
       teach=["Predict first: will the average sleep of children, adults and the elderly in your group be the same?",
              "Group data pools everyone's values, then the mean and the median are found for each age group.",
              "For school timings, a school day of 9:30 am to 4:30 pm is 7 hours. Collect more schools and compare "
              "class time and break time.",
              "Share what you found and what you still wonder."],
       examples=[
           WE("Four children in a group sleep 9, 8.5, 10 and 9 hours. Find the mean and the median sleep time.",
              ["Mean: 9 + 8.5 + 10 + 9 = 36.5, and 36.5 ÷ 4 = 9.125 hours.",
               "Median: in order 8.5, 9, 9, 10; the middle two are 9 and 9.", "(9 + 9) ÷ 2 = 9 hours."],
              "Mean about 9.1 hours, median 9 hours")],
       ncert=[], key_terms=["group data", "median"], minutes=8),
     DOER("T11.C3", "Practice: run your own investigation", "data_project_workspace", "Create",
          "Students enter their own day's data, see the mean, the median and a strip or graph update, compare with "
          "an adult or a group, and write findings and new questions.",
          ["Collect, summarise with a mean and median, show in a graph, then say what you found.",
           "End with at least one new question the data raises."],
          items=[
              FIO("FiO3.q12", "Figure it Out (more on mean and median, question 12)",
                  "Individual project: make your own activity strip for different days of the week. (i) Do you eat "
                  "and sleep at regular times every day? Typically how long do you spend outdoors? (ii) Calculate "
                  "the average time spent per activity and represent this average day using a strip. (iii) Track "
                  "the activities of an adult at home and compare your data with theirs.",
                  ["Record sleeping, eating, studying, outdoors and other activities for several days.",
                   "For each activity add the daily times and divide by the number of days.",
                   "Colour 48 boxes of a strip using these averages, two boxes for each hour.",
                   "Do the same for an adult and compare the two strips."],
                  "A strip of the average day, compared with an adult's strip"),
              FIO("FiO3.q13", "Figure it Out (more on mean and median, question 13)",
                  "Small group project in a group of 3 to 4: do at least one. (i) Track daily sleep of all family "
                  "members for a week, show it on strips, find the average and median sleep of children, adults and "
                  "elderly, and share findings. (ii) Collect the daily timings of different Grade 8 schools, "
                  "including class time and break time, then analyse and present the data.",
                  ["Pick one of the two projects with your group.",
                   "For (i) pool each age group's values, then find the mean by adding and dividing, and the median "
                   "by ordering the values and taking the middle.",
                   "For (ii) list start time, end time and break time for each school, work out total hours, and "
                   "compare.",
                   "Present with a strip or a line graph and say what you found and what you wonder."],
                  "Mean and median for each group, shown in a graph, with findings and new questions")])],
    key_terms=["investigation", "mean", "median"]))

# ============================== T12 Summary and Hex =========================================================
TOPICS.append(TOPIC(
    "T12", "M3", "Summary: Tales by Dots and Lines", ["Summary"], "Remember",
    None,
    "The mean as a balance point, how the mean and median change, line graphs for change over time, and the habit "
    "of asking new questions.",
    [A("T12.C1", "What we found about dots and lines", "Remember",
       "Students restate that the mean balances distances on both sides, how adding values changes the mean and "
       "median, that line graphs show change over time, and that data leads to new questions.",
       textbook=["Last year we looked at mean as a fair-share. Here, we learnt how the sum of the distances of the "
                 "values to its left and right are the same.",
                 "We saw that when values greater than the mean are inserted, the mean increases. When values less "
                 "than the mean are inserted, the mean decreases. Similar phenomena can be observed with the median.",
                 "Line graphs can be used to visualise change over time.",
                 "We saw that examining data can lead to new questions and directions to probe further."],
       teach=["Our opening guess is settled: the mean of two numbers sits halfway between them, and for any data the "
              "distances on the two sides of the mean add up to the same total.",
              "A value above the mean pulls the mean up, a value below pulls it down, and the median moves only when "
              "the middle moves.",
              "Line graphs follow change over time. Still open for you: pick one graph from this chapter and write "
              "two questions it raises."],
       ncert=["summary"], video_focus=["RECAP"], minutes=8),
     A("T12.C2", "Game of Hex", "Apply",
       "Students play a two player game on a hexagon board, aiming to join their two sides in an unbroken chain, "
       "and reflect on the strategy they used.",
       textbook=["Game of Hex. Hex is a two-player strategy game played on a rhombus-shaped board made of hexagonal "
                 "cells, usually of size 11 × 11. Each player is assigned a colour and two opposite sides of the "
                 "board. Players take turns placing a piece of their colour on any empty cell. Once placed, pieces "
                 "can not be moved or removed. The objective is to create an unbroken chain of one's own pieces "
                 "connecting the two assigned sides. The first player to complete such a connection wins the game."],
       teach=["Predict first: can a game of Hex end in a draw? Play a few rounds before you decide.",
              "Each player must join their two sides with an unbroken chain, and blocking the other player also "
              "builds your own chain.",
              "Play with a partner on paper and talk about the moves that helped."],
       examples=[
           WE("On a 3 by 3 Hex board the players fill all 9 cells. Can the game end with neither player joining "
              "their two sides?",
              ["Try filling a small board in every way you can: one colour always joins its two sides.",
               "A wall of one colour that blocks the other side is itself a chain across the board.",
               "So a full board always has exactly one winner."],
              "No; a Hex game can never end in a draw")],
       ncert=["hex"], key_terms=["Hex", "strategy"], enrichment=True, minutes=5)],
    topic_type="summary"))
