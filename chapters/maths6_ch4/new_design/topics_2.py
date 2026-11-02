# -*- coding: utf-8 -*-
"""Topics T7 and T8 (module M3: bar graphs). Book sections 4.3 and 4.4 up to Imran's expenditure."""
from topics_common import A, DOER, TOPIC, book, fio, we

TOPICS = []
H44 = "Chapter box and Teacher's Note (end of 4.4)"

# ============================== T7 Reading bar graphs (4.3) ==================================================
TOPICS.append(TOPIC(
    "T7", "M3", "Reading Bar Graphs", ["4.3"], "Apply",
    "Students read the length of a bar against the equally spaced lines and its scale, find the highest and "
    "the lowest, and work out totals and differences from a bar graph.",
    "In a bar graph the length of each bar, read with the scale, gives the frequency; the longest bar is the "
    "most and the shortest bar is the least.",
    [A("T7.C1", "Reading a bar graph: students absent in each class", "Understand",
       "Students read the height of each bar against the equally spaced lines, find how many students were "
       "absent in a class, and name the class with the most and the class with none absent.",
       textbook=book("4.3", None, stop=4) + book("4.3", None, start=5, stop=7),
       teach=["Predict first: Lakhanpal's absent-students data was a pictograph. If the same data is drawn as "
              "bars, what tells you the number for Class 2?",
              "Each bar stands for one class, and its height against the equally spaced lines gives the "
              "number absent: Class 2 has 5.",
              "The tallest bar is Class 8, with 7 absent. A bar with no height, Class 5, means nobody was "
              "absent.",
              "Bars of the same width and equal gaps make the heights fair to compare."],
       examples=[we("4.3.q1"), we("4.3.q2"), we("4.3.q3")],
       key_terms=["bar graph", "bar"], misconceptions=["M_BAR_WIDTH", "M_BAR_HEIGHT_IS_VALUE"], minutes=10),
     A("T7.C2", "The scale on a bigger graph: traffic at a crossing", "Apply",
       "Students read a horizontal bar graph where one unit of length is 100 vehicles, find the busiest and the "
       "quietest hour, and add two bars read from the graph.",
       textbook=book("4.3", None, start=7, stop=10),
       teach=["Predict first: a bar for 7 to 8 a.m. is 12 units long. Are 12 vehicles passing?",
              "Read the scale first: one unit of length stands for 100 vehicles, so 12 units are 1200 vehicles.",
              "The longest bar is 7 to 8 a.m. with 1200 vehicles, and the shortest is 6 to 7 a.m. with about "
              "150.",
              "To add two hours, add the two readings: 1000 + 800 = 1800 vehicles between 8 and 10 a.m."],
       video_focus=["SCALE"], key_terms=["scale", "unit length"],
       misconceptions=["M_BAR_HEIGHT_IS_VALUE"], minutes=10),
     A("T7.C3", "Reading growth: the population of India", "Apply",
       "Students read a bar graph in crores with one unit of length for 10 crores, and find the increase over "
       "fifty years and in each decade by subtracting readings.",
       textbook=book("4.3", None, start=15, stop=16),
       teach=["Predict first: the population bars rise from 1951 to 2001. By how much did the population "
              "grow, and in which decade did it grow most?",
              "Read each bar with the scale: 36, 44, 54, 68, 84 and 102 crores.",
              "The growth over fifty years is 102 − 36 = 66 crores.",
              "The growth in each decade is the difference of two neighbouring bars: 8, 10, 14, 16 and 18 "
              "crores, so the last decade grew most."],
       examples=[we("4.3.ex1")],
       key_terms=["scale", "difference"], misconceptions=["M_BAR_HEIGHT_IS_VALUE"], minutes=10),
     DOER("T7.C4", "Pull it together and do it: Bar Graph Reader", "bar_graph_reader", "Apply",
          "Students read the scale on the tool, read bar lengths as numbers, and answer questions about the "
          "most, the least, totals and differences.",
          ["Read the scale: what does one unit of bar length stand for?",
           "Bar length in units times the scale gives the frequency.",
           "Totals add the readings; differences subtract them."],
          items=[fio("4.3.FiO.Q1"), fio("4.3.FiO.Q2"), fio("4.3.FiO.Q3"), fio("4.3.FiO.Q4")],
          misconceptions=["M_BAR_HEIGHT_IS_VALUE", "M_SCALE_UNEQUAL"])]))

# ============================== T8 Drawing a bar graph (4.4) =================================================
TOPICS.append(TOPIC(
    "T8", "M3", "Drawing a Bar Graph", ["4.4"], "Apply",
    "Students draw a bar graph from a frequency table by choosing a scale that fits the largest value, "
    "dividing each frequency by the scale to get the bar heights, and reading the finished graph.",
    "To draw a bar graph, choose a scale, divide each frequency by it to get the bar height in units, and "
    "draw bars of equal width with equal gaps from zero.",
    [A("T8.C1", "Drawing the sweets graph: axes, scale and bars", "Apply",
       "Students draw the two lines, write the categories with equal spacing, choose the scale 1 unit for 1 "
       "student, and draw each bar as high as its frequency.",
       textbook=book("4.4", None, start=1, stop=6),
       teach=["Predict first: Shri Nilesh's table says jalebi 6, gulab jamun 9, gujiya 13, barfi 3, rasgulla "
              "7. How tall should the barfi bar be?",
              "Draw a horizontal line for the sweets, equally spaced, and a vertical line for the number of "
              "students.",
              "Choose the scale: 1 unit length for 1 student, so jalebi gets a bar of 6 units and barfi 3 "
              "units.",
              "Draw every bar with the same width and the same gap, starting from zero."],
       video_focus=["DRAW"], key_terms=["bar graph", "scale"],
       misconceptions=["M_BAR_WIDTH", "M_SCALE_UNEQUAL"], minutes=10),
     A("T8.C2", "Choosing a scale: Smriti's runs", "Apply",
       "Students choose the scale 1 unit length = 10 runs for scores from 0 to 100, and divide each score by "
       "10 to get the bar heights.",
       textbook=book("4.4", None, start=6, stop=9),
       teach=["Predict first: Smriti's scores run from 0 to 100. Should one unit of the bar stand for 1 run?",
              "That would need 100 steps, which is tedious. Choose 1 unit length = 10 runs instead.",
              "Divide each score by 10: 80 gives 8 units, 50 gives 5 units, 10 gives 1 unit and 100 gives 10 "
              "units.",
              "A score of 0 has a bar of no height."],
       examples=[we("4.4.ex1")],
       key_terms=["scale", "unit length"], misconceptions=["M_BAR_HEIGHT_IS_VALUE", "M_SCALE_UNEQUAL"],
       minutes=10),
     A("T8.C3", "Imran's family spending: draw it and read it", "Analyze",
       "Students draw a bar graph of a family budget with 1 unit length = ₹ 200, and use it to find the most "
       "and second most spent items and to compare amounts.",
       textbook=book("4.4", None, start=9, stop=16) + book("4.4", None, start=17, stop=18),
       teach=["Predict first: the amounts run from ₹ 400 to ₹ 3400. What scale makes all six bars fit?",
              "Take 1 unit length = ₹ 200 and write ₹ 200, ₹ 400, ... along the vertical line, starting from "
              "zero.",
              "House rent 3000 ÷ 200 gives 15 units and food 3400 ÷ 200 gives 17 units.",
              "Read the finished graph: the longest bar is food and the second longest is house rent."],
       examples=[we("4.4.ex2"), we("4.4.q1"), we("4.4.q2"), we("4.4.q3")],
       key_terms=["scale", "bar graph"], misconceptions=["M_BAR_HEIGHT_IS_VALUE", "M_SCALE_UNEQUAL"],
       minutes=12),
     DOER("T8.C4", "Pull it together and do it: Bar Graph Builder", "bar_graph_builder", "Create",
          "Students pick a scale on the tool, drag each bar to its height, label the axes, and read totals and "
          "comparisons off the graph they made.",
          ["Pick a scale that fits the largest value.",
           "Frequency divided by the scale gives the bar height in units.",
           "Bars have equal width and equal gaps, and the axis starts at zero."],
          items=[fio("4.4.FiO.Q1"),
                 fio("4.4.FiO.Q2", steps=[
                     "Vidisha has 24 tickets in 6 units, and 24 ÷ 6 gives 4 tickets per unit; check Jabalpur: "
                     "5 × 4 = 20",
                     "Sagar 16 ÷ 4 gives 4 units",
                     "Seoni 16 ÷ 4 gives 4 units, so its bar is correct",
                     "Indore 28 ÷ 4 gives 7 units, so its bar is too short and must be redrawn"]),
                 fio("4.4.FiO.Q9"),
                 fio("4.4.FiO.Q10", question="Saplings planted in the first week of July (bar graph): Monday 50, "
                     "Tuesday 40, Wednesday 30, Thursday 40, Friday 50, Saturday 60, Sunday 40. a. The total "
                     "number of saplings planted on Wednesday and Thursday is ___. b. The total number planted "
                     "during the whole week is ___. c. The greatest number were planted on ___ and the least on "
                     "___. Why do you think that is the case? Why were more saplings planted on certain days "
                     "and fewer on others? What are the possible explanations? How could you check them?"),
                 fio("4.4.FiO.Q11", steps=[
                     "Compare each bar with the table value",
                     "The bars for 2006, 2010, 2014 and 2018 do not match the table values 1400, 1700, 2200 "
                     "and 3000",
                     "The bar for 2022 matches 3700, so only 2006, 2010, 2014 and 2018 must be redrawn"])],
          misconceptions=["M_BAR_HEIGHT_IS_VALUE", "M_SCALE_UNEQUAL"])]))
