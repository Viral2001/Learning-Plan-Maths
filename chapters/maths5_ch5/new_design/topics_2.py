# -*- coding: utf-8 -*-
"""Topics T4 to T7 (T4, T5 and T6 in module M2, T7 in module M3): The Longest Train Journey, The World of Small
Things, Changing Units, and Adding and Subtracting Lengths.
Every teaching concept has one worked example with the plan's own numbers (practice values); every book question is an
FIO item of its topic's DOER, in the book's order."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

TRAIN_FIGURE = ("A table of eight stations with the station number, the name and the distance from Dibrugarh: 9 "
                "Dimapur 306 km; 14 Guwahati 556 km; 22 Jalpaiguri Road 983 km; 34 Bhubaneswar 2,007 km; 40 "
                "Visakhapatnam 2,450 km; 45 Vijayawada JN 2,800 km; 55 Coimbatore JN 3,675 km; 65 Kanniyakumari "
                "4,187 km.")

# ============================== T4 The Longest Train Journey ===============================================
TOPICS.append(TOPIC(
    "T4", "M2", "The Longest Train Journey", ["Longest Train Journey"], "Apply",
    "Students find the length of a route and the distance between two stations from a table of distances from the "
    "start.",
    "All the distances in the table are measured from the start of the route. The distance between two stations is the "
    "bigger distance minus the smaller distance, and the last station's distance is the length of the route.",
    [A("T4.C1", "Distance Between Two Stations", "Apply",
       "Students find the distance between two stations by subtracting their distances from the start of the route.",
       textbook=["The longest train journey in India is by The Vivek Express which runs from Dibrugarh in Assam to "
                 "Kanniyakumari in Tamil Nadu. Look at the stations on the route shown in the table below and answer "
                 "the questions."],
       teach=["Predict first: a train route starts at the first station. Station Q is 340 km from the start and "
              "Station R is 615 km from the start. How far is Station Q from Station R?",
              "Both distances are measured from the same place, the start of the route. The start is at 0 km.",
              "Station Q is 340 km along the route and Station R is 615 km along the route. The part of the route "
              "between them is how much farther along R is than Q.",
              "Subtract the smaller distance from the bigger one: 615 − 340 = 275 km.",
              "Do not add the two distances. Both of them already start at the same place.",
              "The distance of the last station from the start is the length of the whole route.",
              "Rule: the distance between two stations is the bigger distance from the start minus the smaller "
              "distance from the start."],
       examples=[WE("A train leaves the first station. Station Q is 340 km and Station R is 615 km from the first "
                    "station (practice values). How far is Station Q from Station R? How long is the route from the "
                    "first station to Station R?",
                    ["All distances are measured from the first station, which is at 0 km.",
                     "Station Q is at 340 km and Station R is at 615 km.",
                     "Subtract the smaller from the bigger: 615 − 340 = 275 km.",
                     "The route from the first station to Station R is the distance of R from the start: 615 km.",
                     "Check: 340 + 275 = 615."],
                    "Station Q is 275 km from Station R, and the route to Station R is 615 km long")],
       key_terms=["route", "distance from the start", "subtract"], misconceptions=["M_DIST_SUM"], minutes=5),
     DOER("T4.C2", "Practice: Longest Train Journey", None, "Apply",
          "Students find the length of a train journey and the distance between two stations from a table of "
          "distances from the start, and say which two stations are farther apart.",
          ["All distances in the table are measured from Dibrugarh.",
           "The distance between two stations is the bigger distance minus the smaller distance.",
           "The last station's distance is the length of the whole route."],
          items=[FIO("train.q1", "Let Us Do (longest train journey), Q1",
                     "The longest train journey in India is by The Vivek Express which runs from Dibrugarh in Assam "
                     "to Kanniyakumari in Tamil Nadu. Look at the stations on the route shown in the table and "
                     "answer. The total length of the route from Dibrugarh to Kanniyakumari is ___ km.",
                     ["The table gives each station's distance from Dibrugarh, where the route starts at 0 km.",
                      "Kanniyakumari is the last station on the route, 4,187 km from Dibrugarh.",
                      "So the whole route from Dibrugarh to Kanniyakumari is 4,187 km long.",
                      "Check: 4,187 km is the biggest distance in the table, so the last station is the farthest from "
                      "the start."],
                     "4,187 km", kind="exercise", q_figure=TRAIN_FIGURE),
                 FIO("train.q2", "Let Us Do (longest train journey), Q2",
                     "Look at the table of stations on the route of The Vivek Express from Dibrugarh. The distance "
                     "between Vijayawada and Jalpaiguri Road is ___ km.",
                     ["Both stations are measured from Dibrugarh. Vijayawada is 2,800 km and Jalpaiguri Road is "
                      "983 km from Dibrugarh.",
                      "Subtract the smaller distance from the bigger one: 2,800 − 983 = 1,817 km.",
                      "Check: 983 + 1,817 = 2,800."],
                     "1,817 km", kind="exercise", q_figure=TRAIN_FIGURE),
                 FIO("train.q3", "Let Us Do (longest train journey), Q3",
                     "Look at the table of stations on the route of The Vivek Express from Dibrugarh. The distance "
                     "between Vijayawada and Visakhapatnam is ___ km.",
                     ["Vijayawada is 2,800 km and Visakhapatnam is 2,450 km from Dibrugarh.",
                      "Subtract the smaller distance from the bigger one: 2,800 − 2,450 = 350 km.",
                      "Check: 2,450 + 350 = 2,800."],
                     "350 km", kind="exercise", q_figure=TRAIN_FIGURE),
                 FIO("train.q4", "Let Us Do (longest train journey), Q4",
                     "Look at the table of stations on the route of The Vivek Express from Dibrugarh. Which two "
                     "stations are farther apart, Guwahati and Dimapur or Bhubaneswar and Jalpaiguri Road?",
                     ["Find the distance of each pair from the table.",
                      "Guwahati is 556 km and Dimapur is 306 km from Dibrugarh: 556 − 306 = 250 km.",
                      "Bhubaneswar is 2,007 km and Jalpaiguri Road is 983 km from Dibrugarh: 2,007 − 983 = 1,024 km.",
                      "Compare 1,024 and 250: 1,024 km is more.",
                      "So Bhubaneswar and Jalpaiguri Road are farther apart.",
                      "Check: 306 + 250 = 556 and 983 + 1,024 = 2,007."],
                     "Bhubaneswar and Jalpaiguri Road: 1,024 km, against 250 km",
                     kind="exercise", q_figure=TRAIN_FIGURE),
                 FIO("train.q5", "Let Us Do (longest train journey), Q5",
                     "Look at the table of stations on the route of The Vivek Express from Dibrugarh. What is the "
                     "distance between Guwahati and Coimbatore JN?",
                     ["Guwahati is 556 km and Coimbatore JN is 3,675 km from Dibrugarh.",
                      "Subtract the smaller distance from the bigger one: 3,675 − 556 = 3,119 km.",
                      "Check: 556 + 3,119 = 3,675."],
                     "3,119 km", kind="exercise", q_figure=TRAIN_FIGURE)],
          misconceptions=["M_DIST_SUM"])],
    key_terms=["route", "distance from the start", "subtract"]))

# ============================== T5 The World of Small Things ===============================================
TOPICS.append(TOPIC(
    "T5", "M2", "The World of Small Things", ["The World of Small Things", "Let Us Measure", "Let Us Do",
                                               "Let Us Draw"], "Apply",
    "Students use 1 cm = 10 mm to read, measure and draw small lengths in cm and mm.",
    "One centimetre is divided into ten equal parts of 1 mm, so 1 cm = 10 mm. A length in cm and mm is written in mm "
    "by multiplying the cm by 10 and adding the mm.",
    [A("T5.C1", "The Millimetre", "Understand",
       "Students explain that 1 cm is divided into 10 equal parts called millimetres, count the small marks, and "
       "change cm to mm using 1 cm = 10 mm.",
       textbook=["One centimetre is divided into ten equal parts. Each part is called 1 millimetre (mm).",
                 "1 cm = 10 mm",
                 "These small marks between any two centimetre marks help us measure the smaller lengths. Thus, it "
                 "adds to the precision in measurement."],
       teach=["Predict first: a sprout, a small screw and a nail are shorter than most things you measure. How can "
              "you measure them? How many small marks are there between 1 cm and 2 cm on a ruler?",
              "Look at a ruler. Between any two centimetre marks there are 9 small marks. They cut 1 cm into 10 equal "
              "parts.",
              "Each part is called 1 millimetre, written 1 mm. So 1 cm = 10 mm.",
              "The small marks help us measure smaller lengths and give a more exact measurement. A sprout, a small "
              "screw or a nail can be measured with them.",
              "To change cm to mm, multiply by 10: 3 cm = 3 × 10 = 30 mm.",
              "A length of 8 mm is less than 1 cm, because 8 is less than 10.",
              "Rule: 1 cm = 10 mm, so multiply by 10 to change cm to mm."],
       examples=[WE("Sonu's pin is 3 cm long. How many mm is that? A bead is 8 mm wide. Is it more or less than 1 cm? "
                    "(practice values)",
                    ["1 cm = 10 mm, so multiply the cm by 10.",
                     "3 cm = 3 × 10 = 30 mm.",
                     "1 cm = 10 mm, and 8 is less than 10.",
                     "So 8 mm is less than 1 cm.",
                     "Check: 30 mm is 3 groups of 10 mm, which is 3 cm."],
                    "3 cm = 30 mm, and 8 mm is less than 1 cm")],
       ncert=["mm.def", "small.how"], key_terms=["millimetre", "1 cm = 10 mm", "small marks"],
       misconceptions=["M_CM_HUNDRED_MM"], minutes=5),
     A("T5.C2", "Reading and Drawing Lengths in cm and mm", "Apply",
       "Students read a length from a ruler in cm and mm and in mm only, and draw a line of a given length.",
       teach=["Predict first: a line starts at 0 and ends on the 6th small mark after the 4 cm mark. How long is it?",
              "Read the cm first: 4 cm. Then count the small marks after it: 6 small marks are 6 mm. The length is "
              "4 cm 6 mm.",
              "To write it in mm, change the cm to mm and add the rest: 4 cm 6 mm = 4 × 10 + 6 = 46 mm.",
              "To draw a length given in mm, split it into tens and ones. 72 mm is 70 mm + 2 mm = 7 cm 2 mm. Put the "
              "0 of the scale at the start, go to the 7 cm mark, then 2 small marks more.",
              "The same works for any length in mm. 52 mm is 5 cm 2 mm: go to the 5 cm mark and then 2 small marks "
              "more. The tens of mm are cm and the ones are the small marks.",
              "Rule: the tens of mm are cm and the ones are mm, so 46 mm is 4 cm 6 mm."],
       examples=[WE("A line ends on the 6th small mark after the 4 cm mark. Write its length in cm and mm and in mm "
                    "only. Then say how to draw a line of 72 mm (practice values).",
                    ["The line passes the 4 cm mark and ends 6 small marks later. 6 small marks are 6 mm.",
                     "The length is 4 cm 6 mm.",
                     "In mm: 4 cm = 4 × 10 = 40 mm, and 40 + 6 = 46 mm.",
                     "To draw 72 mm, split 72 into tens and ones: 72 = 70 + 2.",
                     "70 mm is 7 cm, so 72 mm = 7 cm 2 mm.",
                     "Put the 0 of the scale at the start of the line, go to the 7 cm mark, then 2 small marks more, "
                     "and mark the end.",
                     "Check: 7 × 10 + 2 = 72 mm."],
                    "4 cm 6 mm = 46 mm, and a line of 72 mm is drawn to 7 cm 2 mm")],
       ncert=["draw.how"], key_terms=["cm and mm", "read", "draw"], misconceptions=["M_CM_HUNDRED_MM"], minutes=5),
     DOER("T5.C3", "Practice: Millimetre Ruler", "millimetre_ruler", "Apply",
          "Students count the small marks between two cm marks on a ruler, measure the lines of a design in cm and "
          "mm, record the length of a sprout in mm, and draw lines of given lengths.",
          ["Between two cm marks there are 9 small marks, and each part is 1 mm.",
           "Read the cm first, then count the small marks for the mm.",
           "To draw a length, go to the cm mark and then count the small marks."],
          items=[FIO("ruler.count", "The World of Small Things: count the marks",
                     "Let us look at the scale. Do you notice the small marks between 1 cm and 2 cm? Count how many "
                     "marks there are between 1 cm and 2 cm.",
                     ["Look at the ruler between the 1 cm mark and the 2 cm mark.",
                      "Count the small marks one by one: 1, 2, 3, 4, 5, 6, 7, 8, 9. There are 9 small marks.",
                      "The 9 marks cut 1 cm into 10 equal parts, and each part is 1 mm.",
                      "Check: 10 parts need 9 cuts, and 10 parts of 1 mm make 1 cm."],
                     "9 small marks", kind="prompt",
                     q_figure="A yellow ruler marked 1 to 7 in centimetres with small marks between the numbers.",
                     s_figure="The part of the ruler from 1 cm to 2 cm with its 9 small marks numbered 1 to 9 and the "
                              "ten equal parts of 1 mm each."),
                 FIO("design.measure", "The World of Small Things: measure the design",
                     "Measure the lines in the design and write their measurements in cm and mm. The design has eight "
                     "lines, each with an empty box beside it. In this question they are numbered from the top of the "
                     "picture to the bottom: (1): the upper left slanting side of the large diamond; (2): the top side "
                     "of the inner rectangle; (3): the right side of the big outer shape; (4): the right side of the "
                     "inner rectangle; (5): the upper left side of the small tilted shape; (6): the lower left side of "
                     "the small tilted shape; (7): the lower left slanting side of the large diamond; (8): the bottom "
                     "side of the big outer shape.",
                     ["Put the 0 of the ruler at one end of a line, keep the ruler along the line, and read where the "
                      "line ends. Read the cm first, then count the small marks. These lengths were measured on the "
                      "picture at its printed size, so your ruler may read 1 mm different.",
                      "(1): 48 mm = 40 mm + 8 mm = 4 cm 8 mm; (2): 35 mm = 30 mm + 5 mm = 3 cm 5 mm.",
                      "(3): 60 mm = 6 cm; (4): 27 mm = 20 mm + 7 mm = 2 cm 7 mm.",
                      "(5): 22 mm = 20 mm + 2 mm = 2 cm 2 mm; (6): 19 mm = 10 mm + 9 mm = 1 cm 9 mm.",
                      "(7): 44 mm = 40 mm + 4 mm = 4 cm 4 mm; (8): 61 mm = 60 mm + 1 mm = 6 cm 1 mm.",
                      "Check: 10 mm = 1 cm, so the tens of mm are the cm."],
                     "Sample answer in mm: (1): 48; (2): 35; (3): 60; (4): 27; (5): 22; (6): 19; (7): 44; (8): 61. "
                     "Your answer may differ by 1 mm.",
                     kind="exercise",
                     q_figure="A design of four nested four sided shapes, a big outer shape, a large diamond inside "
                              "it, a rectangle inside the diamond and a small tilted shape inside the rectangle, with "
                              "an empty box beside eight of the lines.",
                     s_figure="The same design with its eight lines numbered 1 to 8 and each length written in the "
                              "box beside its line in cm and mm."),
                 FIO("sprout.diary", "The World of Small Things: sprout diary",
                     "Soak some seeds of whole moong or black or white chana overnight. Next morning, take them out "
                     "and wrap them in a moist cloth to sprout them. Over the next 4 days, take out one seed each day "
                     "and measure the length of sprout. For ease of measurement, you can either place the seed on a "
                     "paper and mark the length of the sprout, or use a thread to find its length. Fill in the table: "
                     "the length of the sprout in mm on Day 1, Day 2, Day 3 and Day 4.",
                     ["Place a thread along the sprout, straight, and hold the end. Lay the thread against the scale.",
                      "Read the cm and the small marks, and write the length in mm: for example 1 cm 6 mm = 16 mm.",
                      "Practice values for the four days, one seed each day: Day 1: 3 mm; Day 2: 9 mm; Day 3: 16 mm; "
                      "Day 4: 25 mm.",
                      "The sprout grows, so each day's length should be more than the day before: 3 < 9 < 16 < 25."],
                     "Sample answer, practice values: Day 1: 3 mm; Day 2: 9 mm; Day 3: 16 mm; Day 4: 25 mm. Your "
                     "answer may differ.",
                     kind="exercise",
                     q_figure="A table with four rows, Day 1 to Day 4, and an empty box beside each for the length of "
                              "the sprout in mm."),
                 FIO("draw.lines", "The World of Small Things: draw the lines",
                     "Draw lines of the following lengths in your notebook using a scale. (a): 5 cm 5 mm; (b): 3 cm "
                     "6 mm; (c): 8 cm 3 mm; (d): 36 mm; (e): 67 mm.",
                     ["Put the 0 of the scale at the start of the line and mark the end at the length asked.",
                      "(a): 5 cm 5 mm: go to 5 cm and then 5 small marks. In mm that is 5 × 10 + 5 = 55 mm.",
                      "(b): 3 cm 6 mm: go to 3 cm and then 6 small marks. In mm that is 3 × 10 + 6 = 36 mm.",
                      "(c): 8 cm 3 mm: go to 8 cm and then 3 small marks. In mm that is 8 × 10 + 3 = 83 mm.",
                      "(d): 36 mm = 30 mm + 6 mm = 3 cm 6 mm, the same length as (b).",
                      "(e): 67 mm = 60 mm + 7 mm = 6 cm 7 mm: go to 6 cm and then 7 small marks.",
                      "Check: the lines in (b) and (d) are equal, and (c) is the longest of the five."],
                     "(a): 55 mm; (b): 36 mm; (c): 83 mm; (d): 3 cm 6 mm; (e): 6 cm 7 mm",
                     kind="exercise",
                     s_figure="A ruler with five lines drawn from 0 to 5 cm 5 mm, 3 cm 6 mm, 8 cm 3 mm, 3 cm 6 mm and "
                              "6 cm 7 mm.")],
          misconceptions=["M_CM_HUNDRED_MM"])],
    key_terms=["millimetre", "1 cm = 10 mm", "ruler"]))

# ============================== T6 Changing Units ==========================================================
TOPICS.append(TOPIC(
    "T6", "M2", "Changing Units", ["Relationships between Different Units", "Let Us Do"], "Apply",
    "Students change a length between mm, cm, m and km using the multipliers 10, 100 and 1,000, and split a length "
    "into two units.",
    "10 mm = 1 cm, 100 cm = 1 m and 1,000 m = 1 km. From a bigger unit to a smaller unit multiply by 10, 100 or "
    "1,000; from a smaller unit to a bigger unit divide. A length can be split into a part in the bigger unit and a "
    "rest in the smaller unit.",
    [A("T6.C1", "Changing Between mm, cm, m and km", "Apply",
       "Students change lengths between mm and cm, cm and m, and m and km by multiplying or dividing by 10, 100 or "
       "1,000.",
       textbook=["10 mm = 1 cm", "100 cm = 1 m", "1,000 m = 1 km"],
       teach=["Predict first: how many mm are in 6 cm? How many cm are in 9 m? How many m are in 8 km?",
              "Your maths book gives three relationships: 10 mm = 1 cm, 100 cm = 1 m and 1,000 m = 1 km.",
              "A double number line puts the bigger unit on the top line and the smaller unit on the bottom line. The "
              "ticks line up, so one tick shows the same length in two units.",
              "Going down from the top line to the bottom line, multiply: by 10 for cm to mm, by 100 for m to cm and "
              "by 1,000 for km to m.",
              "Going up from the bottom line to the top line, divide by the same number: 4,000 m = 4,000 ÷ 1,000 = "
              "4 km.",
              "Rule: from a bigger unit to a smaller unit multiply by 10, 100 or 1,000, and from a smaller unit to a "
              "bigger unit divide."],
       examples=[WE("Change 6 cm to mm, 9 m to cm and 8 km to m (practice values).",
                    ["Going from a bigger unit to a smaller unit, multiply.",
                     "6 cm to mm: 1 cm = 10 mm, so 6 × 10 = 60 mm.",
                     "9 m to cm: 1 m = 100 cm, so 9 × 100 = 900 cm.",
                     "8 km to m: 1 km = 1,000 m, so 8 × 1,000 = 8,000 m.",
                     "Check by dividing back: 60 ÷ 10 = 6, 900 ÷ 100 = 9 and 8,000 ÷ 1,000 = 8."],
                    "6 cm = 60 mm, 9 m = 900 cm and 8 km = 8,000 m")],
       ncert=["rel.units"], key_terms=["multiply", "divide", "double number line"],
       misconceptions=["M_M_TEN_CM", "M_KM_HUNDRED", "M_CM_HUNDRED_MM"], minutes=6),
     A("T6.C2", "Splitting a Length into Two Units", "Apply",
       "Students write a length in one unit as a length in two units, and a length in two units as one number in "
       "the smaller unit, by splitting it.",
       textbook=["89 mm = 80 mm + 9 mm = 8 cm 9 mm",
                 "5,792 cm = 5,700 cm + 92 cm = 57 m 92 cm"],
       teach=["Predict first: how would you write 7,305 cm in m and cm?",
              "Take out the part that is a whole number of m: 7,305 cm = 7,300 cm + 5 cm. What is left stays in cm.",
              "7,300 cm = 7,300 ÷ 100 = 73 m, so 7,305 cm = 73 m 5 cm.",
              "Your maths book shows the same idea: 89 mm = 80 mm + 9 mm = 8 cm 9 mm, and 5,792 cm = 5,700 cm + 92 cm "
              "= 57 m 92 cm.",
              "To go the other way, change the bigger unit to the smaller unit and add the rest: 3 m 7 cm = 300 cm + "
              "7 cm = 307 cm.",
              "Rule: split off the part that is a whole number of the bigger unit and keep the rest in the smaller "
              "unit."],
       examples=[WE("Write 7,305 cm in m and cm. Then write 3 m 7 cm in cm (practice values).",
                    ["Split 7,305 cm into a part that is whole metres and a rest: 7,305 cm = 7,300 cm + 5 cm.",
                     "Change the metres: 7,300 ÷ 100 = 73, so 7,300 cm = 73 m.",
                     "So 7,305 cm = 73 m 5 cm.",
                     "Now 3 m 7 cm: 3 m = 3 × 100 = 300 cm.",
                     "300 cm + 7 cm = 307 cm, so 3 m 7 cm = 307 cm.",
                     "Check: 73 × 100 + 5 = 7,305."],
                    "7,305 cm = 73 m 5 cm and 3 m 7 cm = 307 cm")],
       ncert=["conv.ex_mm", "conv.ex_cm"], key_terms=["split", "m and cm", "whole number of metres"],
       misconceptions=["M_JOIN_NUMBERS"], minutes=6),
     DOER("T6.C3", "Practice: Double Number Line", "double_number_line", "Apply",
          "Students fill in the numbers and the multipliers on three number lines side by side, and change lengths "
          "between mm, cm, m and km in fourteen conversions.",
          ["Going down from the bigger unit to the smaller unit, multiply by 10, 100 or 1,000.",
           "Going up, divide by the same number.",
           "To split a length, take out the whole number of the bigger unit and keep the rest."],
          items=[FIO("dnl.a", "Let Us Do (double number lines), Q1 (a)",
                     "Fill in the blanks appropriately in the double number line. Top line: 1 cm, 7 cm, 15 cm, ___ cm, "
                     "___ cm, ___ cm, 50 cm. Bottom line: 10 mm, ___ mm, ___ mm, 250 mm, 320 mm, 450 mm, ___ m. Fill "
                     "in the two boxes ×___ as well: the arrow on the top line is ×7 and the arrow from the top line "
                     "to the bottom line is ×10.",
                     ["The top line is in cm and the bottom line is in mm. Going down, multiply by 10, because 1 cm = "
                      "10 mm.",
                      "The arrow ×7 on the top line goes from 1 cm to 7 cm, so the arrow on the bottom line from "
                      "10 mm to the next blank is also ×7: 10 × 7 = 70 mm.",
                      "7 cm = 7 × 10 = 70 mm, and the box on the arrow from the top line to the bottom line is ×10. "
                      "15 cm = 15 × 10 = 150 mm.",
                      "Going up, divide by 10: 250 ÷ 10 = 25 cm, 320 ÷ 10 = 32 cm and 450 ÷ 10 = 45 cm.",
                      "50 cm = 50 × 10 = 500 mm. Your maths book prints m under this tick, but 50 cm is 500 mm, which "
                      "is also half a metre.",
                      "Check: 7 × 10 = 70 and 70 ÷ 10 = 7."],
                     "Top: 25 cm, 32 cm, 45 cm. Bottom: 70 mm, 150 mm, 500 mm. Boxes: ×7, ×10",
                     kind="exercise",
                     q_figure="A double number line with seven ticks: the top line is labelled 1 cm, 7 cm, 15 cm, three "
                              "blank cm and 50 cm, the bottom line is labelled 10 mm, two blank mm, 250 mm, 320 mm, "
                              "450 mm and a blank m, with the arrows ×7 on top, ×10 from 1 cm to 10 mm and two empty "
                              "boxes ×___.",
                     s_figure="The same double number line with every blank filled in and the two boxes showing ×7 "
                              "and ×10."),
                 FIO("dnl.b", "Let Us Do (double number lines), Q1 (b)",
                     "Fill in the blanks appropriately in the double number line. Top line: 1 m, 4 m, 10 m, ___ m, "
                     "___ m, ___ m, 21 m. Bottom line: ___ cm, ___ cm, ___ cm, 1,200 cm, 1,400 cm, 1,700 cm, ___ cm. "
                     "Fill in the two boxes ×___ as well: the arrow on the top line is ×4 and the arrow from the top "
                     "line to the bottom line is ×100.",
                     ["The top line is in m and the bottom line is in cm. Going down, multiply by 100, because 1 m = "
                      "100 cm.",
                      "The arrow ×4 on the top line goes from 1 m to 4 m, so the arrow on the bottom line is also ×4: "
                      "100 × 4 = 400 cm. The box on the arrow from the top line to the bottom line is ×100.",
                      "1 m = 1 × 100 = 100 cm, 10 m = 10 × 100 = 1,000 cm and 21 m = 21 × 100 = 2,100 cm.",
                      "Going up, divide by 100: 1,200 ÷ 100 = 12 m, 1,400 ÷ 100 = 14 m and 1,700 ÷ 100 = 17 m.",
                      "Check: 4 × 100 = 400 and 400 ÷ 100 = 4."],
                     "Top: 12 m, 14 m, 17 m. Bottom: 100 cm, 400 cm, 1,000 cm, 2,100 cm. Boxes: ×4, ×100",
                     kind="exercise",
                     q_figure="A double number line with seven ticks: the top line is labelled 1 m, 4 m, 10 m, three "
                              "blank m and 21 m, the bottom line is labelled three blank cm, 1,200 cm, 1,400 cm, "
                              "1,700 cm and a blank cm, with the arrows ×4 on top, ×100 from 1 m down to the bottom "
                              "line and two empty boxes ×___.",
                     s_figure="The same double number line with every blank filled in and the two boxes showing ×4 "
                              "and ×100."),
                 FIO("dnl.c", "Let Us Do (double number lines), Q1 (c)",
                     "Fill in the blanks appropriately in the double number line. Top line: 1 km, 9 km, 25 km, ___ km, "
                     "___ km, ___ km, 82 km. Bottom line: 1,000 m, ___ m, ___ m, 41,000 m, 55,000 m, 67,000 m, ___ m. "
                     "Fill in the two boxes ×___ as well: the arrow on the top line is ×9 and the arrow from the top "
                     "line to the bottom line is ×1,000.",
                     ["The top line is in km and the bottom line is in m. Going down, multiply by 1,000, because "
                      "1 km = 1,000 m.",
                      "The arrow ×9 on the top line goes from 1 km to 9 km, so the arrow on the bottom line is also "
                      "×9: 1,000 × 9 = 9,000 m. The box on the arrow from the top line to the bottom line is ×1,000.",
                      "25 km = 25 × 1,000 = 25,000 m and 82 km = 82 × 1,000 = 82,000 m.",
                      "Going up, divide by 1,000: 41,000 ÷ 1,000 = 41 km, 55,000 ÷ 1,000 = 55 km and 67,000 ÷ 1,000 "
                      "= 67 km.",
                      "Check: 9 × 1,000 = 9,000 and 9,000 ÷ 1,000 = 9."],
                     "Top: 41 km, 55 km, 67 km. Bottom: 9,000 m, 25,000 m, 82,000 m. Boxes: ×9, ×1,000",
                     kind="exercise",
                     q_figure="A double number line with seven ticks: the top line is labelled 1 km, 9 km, 25 km, three "
                              "blank km and 82 km, the bottom line is labelled 1,000 m, two blank m, 41,000 m, "
                              "55,000 m, 67,000 m and a blank m, with the arrows ×9 on top, ×1,000 from 1 km down to "
                              "the bottom line and two empty boxes ×___.",
                     s_figure="The same double number line with every blank filled in and the two boxes showing ×9 "
                              "and ×1,000."),
                 FIO("conv.mmcm", "Let Us Do (changing units), Q2 (a) to (d)",
                     "Use your understanding from above to fill in the blanks appropriately. (a): 4 cm 5 mm = ___ mm; "
                     "(b): 89 mm = ___ cm ___ mm; (c): 234 cm = ___ mm; (d): 514 mm = ___ cm ___ mm.",
                     ["1 cm = 10 mm. From cm to mm, multiply by 10. From mm to cm and mm, split off the tens.",
                      "(a): 4 cm 5 mm = 4 × 10 + 5 = 45 mm.",
                      "(b): 89 mm = 80 mm + 9 mm = 8 cm 9 mm, as in your maths book.",
                      "(c): 234 cm = 234 × 10 = 2,340 mm.",
                      "(d): 514 mm = 510 mm + 4 mm = 51 cm 4 mm.",
                      "Check (d): 51 × 10 + 4 = 514."],
                     "(a): 45 mm; (b): 8 cm 9 mm; (c): 2,340 mm; (d): 51 cm 4 mm",
                     kind="exercise"),
                 FIO("conv.mcm", "Let Us Do (changing units), Q2 (e) to (i)",
                     "Use your understanding from above to fill in the blanks appropriately. (e): 6 m 34 cm = ___ cm; "
                     "(f): 20 m 12 cm = ___ cm; (g): 397 m = ___ cm; (h): 5,792 cm = ___ m ___ cm; (i): 9,108 cm = "
                     "___ m ___ cm.",
                     ["1 m = 100 cm. From m to cm, multiply by 100. From cm to m and cm, take out the hundreds.",
                      "(e): 6 m 34 cm = 6 × 100 + 34 = 634 cm.",
                      "(f): 20 m 12 cm = 20 × 100 + 12 = 2,012 cm.",
                      "(g): 397 m = 397 × 100 = 39,700 cm.",
                      "(h): 5,792 cm = 5,700 cm + 92 cm = 57 m 92 cm, as in your maths book.",
                      "(i): 9,108 cm = 9,100 cm + 8 cm = 91 m 8 cm.",
                      "Check (i): 91 × 100 + 8 = 9,108."],
                     "(e): 634 cm; (f): 2,012 cm; (g): 39,700 cm; (h): 57 m 92 cm; (i): 91 m 8 cm",
                     kind="exercise"),
                 FIO("conv.kmm", "Let Us Do (changing units), Q2 (j) to (n)",
                     "Use your understanding from above to fill in the blanks appropriately. (j): 34 km = ___ m; (k): "
                     "6,870 m = ___ km ___ m; (l): 10,552 m = ___ km ___ m; (m): 29 km 30 m = ___ m; (n): 32 km 359 m "
                     "= ___ m.",
                     ["1 km = 1,000 m. From km to m, multiply by 1,000. From m to km and m, take out the thousands.",
                      "(j): 34 km = 34 × 1,000 = 34,000 m.",
                      "(k): 6,870 m = 6,000 m + 870 m = 6 km 870 m.",
                      "(l): 10,552 m = 10,000 m + 552 m = 10 km 552 m.",
                      "(m): 29 km 30 m = 29 × 1,000 + 30 = 29,030 m.",
                      "(n): 32 km 359 m = 32 × 1,000 + 359 = 32,359 m.",
                      "Check (l): 10 × 1,000 + 552 = 10,552."],
                     "(j): 34,000 m; (k): 6 km 870 m; (l): 10 km 552 m; (m): 29,030 m; (n): 32,359 m",
                     kind="exercise")],
          misconceptions=["M_M_TEN_CM", "M_KM_HUNDRED", "M_CM_HUNDRED_MM", "M_JOIN_NUMBERS"])],
    key_terms=["multiply", "divide", "multiplier"]))

# ============================== T7 Adding and Subtracting Lengths ==========================================
TOPICS.append(TOPIC(
    "T7", "M3", "Adding and Subtracting Lengths", ["Adding and Subtracting Lengths", "Let Us Do"], "Apply",
    "Students add and subtract lengths given in two units by adding like units, by changing to the smaller unit, or by "
    "regrouping.",
    "Add like units and regroup the smaller unit into the bigger one: 1,100 m is 1 km 100 m. To subtract, change both "
    "lengths to the smaller unit, or regroup 1 m as 100 cm and 1 km as 1,000 m first.",
    [A("T7.C1", "Adding Lengths", "Apply",
       "Students add two lengths given in two units by adding like units, or by changing both to the smaller unit "
       "and adding.",
       teach=["Predict first: Sonu walked 2 km 700 m to the market and 1 km 800 m back by another road. How far did "
              "he walk in all?",
              "Add like units. Add the km: 2 km + 1 km = 3 km. Add the m: 700 m + 800 m = 1,500 m.",
              "1,500 m is more than 1,000 m, so regroup: 1,500 m = 1 km 500 m. Then 3 km + 1 km 500 m = 4 km 500 m.",
              "Or change both to m and add: 2 km 700 m = 2,700 m and 1 km 800 m = 1,800 m, and 2,700 + 1,800 = "
              "4,500 m = 4 km 500 m.",
              "When the numbers are easy, such as 200, 250, 400, 500 or 750, you can add in your head. When they are "
              "not, write the two lengths in a column, one unit in each column, and regroup: 1 km = 1,000 m and "
              "1 m = 100 cm.",
              "Lengths add just like numbers, but each unit keeps its own column.",
              "Rule: add like units, then regroup the smaller unit into the bigger one."],
       examples=[WE("Sonu walked 2 km 700 m to the market and 1 km 800 m back by another road (practice values). How "
                    "far did he walk in all?",
                    ["Add the km: 2 km + 1 km = 3 km.",
                     "Add the m: 700 m + 800 m = 1,500 m.",
                     "Regroup: 1,500 m = 1 km 500 m, because 1,000 m = 1 km.",
                     "Add: 3 km + 1 km 500 m = 4 km 500 m.",
                     "Check in m: 2,700 + 1,800 = 4,500 m = 4 km 500 m."],
                    "4 km 500 m")],
       ncert=["addsub.note"], key_terms=["add", "like units", "regroup"], misconceptions=["M_ADD_ALL"], minutes=6),
     A("T7.C2", "Subtracting Lengths", "Apply",
       "Students subtract one length from another by changing both to the smaller unit or by regrouping a bigger "
       "unit into the smaller one.",
       teach=["Predict first: Shikha has a ribbon 9 m long and cuts off 3 m 40 cm. How much ribbon is left?",
              "Change both lengths to cm: 9 m = 9 × 100 = 900 cm and 3 m 40 cm = 3 × 100 + 40 = 340 cm.",
              "Subtract: 900 − 340 = 560 cm. Change back: 560 cm = 500 cm + 60 cm = 5 m 60 cm.",
              "Or regroup. 9 m has no cm part to take 40 cm from, so regroup 1 m as 100 cm: 9 m = 8 m 100 cm. Then "
              "8 m 100 cm − 3 m 40 cm = 5 m 60 cm.",
              "Always regroup 1 m as 100 cm, not as 10 cm, and 1 km as 1,000 m.",
              "Check by adding: the answer plus the part you took away is the length you started with.",
              "Rule: change both to the smaller unit and subtract, or regroup one bigger unit into the smaller unit "
              "first."],
       examples=[WE("Shikha has a ribbon 9 m long and cuts off 3 m 40 cm (practice values). How much ribbon is left?",
                    ["Change both to cm: 9 m = 9 × 100 = 900 cm.",
                     "3 m 40 cm = 3 × 100 + 40 = 340 cm.",
                     "Subtract: 900 − 340 = 560 cm.",
                     "Change back: 560 cm = 500 cm + 60 cm = 5 m 60 cm.",
                     "Check by regrouping: 9 m = 8 m 100 cm, and 8 m 100 cm − 3 m 40 cm = 5 m 60 cm.",
                     "Check by adding: 340 + 560 = 900 cm."],
                    "5 m 60 cm")],
       key_terms=["subtract", "regroup", "change to the smaller unit"], misconceptions=["M_BORROW_TEN"], minutes=6),
     DOER("T7.C3", "Practice: Length Columns", "length_columns", "Apply",
          "Students add and subtract lengths given in two units in the book's examples and word problems, and find "
          "the bigger of two lengths and their difference.",
          ["Add like units, then regroup the smaller unit into the bigger one.",
           "To subtract, change both lengths to the smaller unit, or regroup first.",
           "Check a subtraction by adding the answer to the part taken away."],
          items=[FIO("add.saji", "Example 1: Saji's walk",
                     "Saji saw on his smartphone that he walked 3 km 450 m in the morning and another 4 km 650 m in "
                     "the evening. How much did he walk in the whole day? How would you solve this problem?",
                     ["Add like units. Add the km: 3 km + 4 km = 7 km.",
                      "Add the m: 450 m + 650 m = 1,100 m = 1 km 100 m.",
                      "Add: 7 km + 1 km 100 m = 8 km 100 m.",
                      "Another way: change both to m and add: 3,450 m + 4,650 m = 8,100 m.",
                      "8,100 m = 8,000 m + 100 m = 8 km 100 m.",
                      "Check: both ways give 8 km 100 m."],
                     "8 km 100 m", kind="example",
                     s_figure="A column addition with a km column and a m column: 3 km 450 m plus 4 km 650 m, a carried "
                              "1 into the km column, and the total 8 km 100 m."),
                 FIO("add.cable", "Example 2: the cable",
                     "Electricians are changing the cables in a house. They need 63 m of cable for this purpose. They "
                     "used 16 m 75 cm cable in the first room. What is the length of the cable left?",
                     ["The two lengths are in m and cm. Change both to cm: 1 m = 100 cm.",
                      "63 m = 63 × 100 = 6,300 cm and 16 m 75 cm = 16 × 100 + 75 = 1,675 cm.",
                      "Subtract: 6,300 − 1,675 = 4,625 cm.",
                      "Change back: 4,625 cm = 4,600 cm + 25 cm = 46 m 25 cm.",
                      "Check by adding: 1,675 + 4,625 = 6,300 cm."],
                     "46 m 25 cm", kind="example",
                     s_figure="A subtraction of 1,675 cm from 6,300 cm in a cm column with the borrowed digits marked, "
                              "and the result 4,625 cm."),
                 FIO("addsub.q1", "Let Us Do (adding and subtracting), Q1 ribbons",
                     "Rani has two red coloured ribbon rolls, one of length 3 m 75 cm and another 2 m 25 cm long. How "
                     "much ribbon does she have?",
                     ["Add like units. Add the m: 3 m + 2 m = 5 m.",
                      "Add the cm: 75 cm + 25 cm = 100 cm = 1 m.",
                      "Add: 5 m + 1 m = 6 m.",
                      "Check in cm: 375 + 225 = 600 cm = 6 m."],
                     "6 m", kind="exercise"),
                 FIO("addsub.q2", "Let Us Do (adding and subtracting), Q2 Bhopal to Sanchi",
                     "The distance from Bhopal to Sanchi is 48 km 700 m. Bhadbhada Ghat waterfall is on the way, and "
                     "17 km 900 m away from Bhopal. How far is Sanchi from the waterfall?",
                     ["Sanchi is 48 km 700 m from Bhopal and the waterfall is 17 km 900 m from Bhopal. Subtract to "
                      "find how far Sanchi is from the waterfall.",
                      "Change both to m: 48 km 700 m = 48 × 1,000 + 700 = 48,700 m and 17 km 900 m = 17 × 1,000 + "
                      "900 = 17,900 m.",
                      "Subtract: 48,700 − 17,900 = 30,800 m.",
                      "Change back: 30,800 m = 30,000 m + 800 m = 30 km 800 m.",
                      "Check by adding: 17,900 + 30,800 = 48,700 m."],
                     "30 km 800 m", kind="exercise"),
                 FIO("addsub.q3", "Let Us Do (adding and subtracting), Q3 Gulmarg Gondola",
                     "Gulmarg Gondola in Gulmarg, Kashmir is the second longest and second highest cable car in the "
                     "world. It is divided into two sections. The first section covers 2 km 300 m and the second "
                     "section covers 2 km 650 m. What is the total distance covered by the cable car?",
                     ["The cable car has two sections. Add the lengths of the two sections.",
                      "Add the km: 2 km + 2 km = 4 km.",
                      "Add the m: 300 m + 650 m = 950 m.",
                      "Add: 4 km + 950 m = 4 km 950 m.",
                      "Check in m: 2,300 + 2,650 = 4,950 m = 4 km 950 m."],
                     "4 km 950 m", kind="exercise"),
                 FIO("addsub.q4a", "Let Us Do (adding and subtracting), Q4 (a) to (d)",
                     "Circle the bigger length and find the difference. (a): 11 mm and 1 cm; (b): 26 mm and 2 cm; "
                     "(c): 20 cm and 201 mm; (d): 1,020 mm and 1 m.",
                     ["Change both lengths to the smaller unit, then compare and subtract.",
                      "(a): 1 cm = 10 mm. 11 mm is more than 10 mm. The difference is 11 − 10 = 1 mm.",
                      "(b): 2 cm = 20 mm. 26 mm is more than 20 mm. The difference is 26 − 20 = 6 mm.",
                      "(c): 20 cm = 200 mm. 201 mm is more than 200 mm. The difference is 201 − 200 = 1 mm.",
                      "(d): 1 m = 1,000 mm. 1,020 mm is more than 1,000 mm. The difference is 1,020 − 1,000 = 20 mm.",
                      "Check: 20 mm = 2 cm, and 1,000 + 20 = 1,020."],
                     "Bigger, difference: (a): 11 mm, 1 mm; (b): 26 mm, 6 mm; (c): 201 mm, 1 mm; (d): 1,020 mm, 20 mm",
                     kind="exercise"),
                 FIO("addsub.q4b", "Let Us Do (adding and subtracting), Q4 (e) to (g)",
                     "Circle the bigger length and find the difference. (e): 2 m and 245 cm; (f): 5,678 m and 6 km; "
                     "(g): 6 km 1,480 m and 7 km 479 m.",
                     ["Change both lengths to the smaller unit, then compare and subtract.",
                      "(e): 2 m = 200 cm. 245 cm is more than 200 cm. The difference is 245 − 200 = 45 cm.",
                      "(f): 6 km = 6,000 m. 6,000 m is more than 5,678 m. The difference is 6,000 − 5,678 = 322 m.",
                      "(g): 6 km 1,480 m = 6,000 + 1,480 = 7,480 m and 7 km 479 m = 7,000 + 479 = 7,479 m. 7,480 m "
                      "is more than 7,479 m, so 6 km 1,480 m is the bigger length. The difference is 7,480 − 7,479 = "
                      "1 m.",
                      "Check: 5,678 + 322 = 6,000."],
                     "Bigger, difference: (e): 245 cm, 45 cm; (f): 6 km, 322 m; (g): 6 km 1,480 m, 1 m",
                     kind="exercise")],
          misconceptions=["M_ADD_ALL", "M_BORROW_TEN"])],
    key_terms=["add", "subtract", "regroup"]))
