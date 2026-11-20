# -*- coding: utf-8 -*-
"""Topics T4 to T6 (module M2, Bar Graphs): from squares to bars and reading bars (Recording a Day), making a bar graph
(Day in My Life and Whose Index Finger is Longer?), and using a bar graph (Food Wastage in the School Canteen).
Every teaching concept has one worked example with the plan's own numbers (practice values); every book question is an
FIO item of its topic's DOER, in the book's order. Day in My Life and the index finger have no printed data: their
sample answers use the practice values of DESIGN section 4 and say so."""
from topics_common import A, DOER, FIO, TOPIC, WE
from figs import DAY, FINGER_GRAPH, FOOD, MINE_GRAPH, MINE_TABLE

TOPICS = []

# the practice strips of the index finger activity (practice values, DESIGN section 4)
FINGER_SAMPLE = ("Mine 6 cm, Friend 1 with 7 cm, Friend 2 with 5 cm, Friend 3 with 8 cm and Friend 4 with 6 cm")

# ============================== T4 Bar Graphs (M2) ============================================================
TOPICS.append(TOPIC(
    "T4", "M2", "Bar Graphs", ["Recording a Day"], "Understand",
    "Students show a row of squares as a bar graph, name its vertical line, horizontal base and bars, read the height "
    "of each bar and compare two children's bars.",
    "A bar graph stands the squares of each row up as a bar, and the height of a bar is the number it shows. The "
    "vertical line has the numbers, the horizontal base has the activities, and the taller bar is more. The "
    "difference of two heights is how many more.",
    [A("T4.C1", "From Squares to Bars", "Understand",
       "Students show a row of squares as a bar of the same height and name the vertical line, the horizontal base "
       "and the bars of a bar graph.",
       textbook=["One day Raman and Sheela decided to record how they spent their day.",
                 "Raman recorded his daily routine in the table below.",
                 "Sheela recorded her routine in the following manner.",
                 "I have shown the number of hours spent on each activity by a vertical bar.",
                 "Vertical line showing the number of hours",
                 "Horizontal base showing different activities",
                 "The bars show how much time is spent on each activity",
                 "How is Sheela's recording different from Raman's recording? Discuss in class.",
                 "Sheela's way of recording the data is called a bar graph."],
       teach=["Predict first: Kabir records his Saturday with a row of squares for each activity, and one square "
              "stands for 1 hour. Reading has 3 squares, playing has 5 squares and helping at home has 2 squares. If "
              "each row is stood up like a tower, what do we get?",
              "Stand each row up. Reading becomes a tower 3 squares tall, playing a tower 5 squares tall and helping "
              "at home a tower 2 squares tall.",
              "Now fill each tower in as one solid piece. That solid piece is a bar. The height of a bar is the "
              "number of squares in the row it came from.",
              "A recording that shows a bar for each activity is called a bar graph.",
              "A bar graph has three parts. The vertical line shows the number of hours. The horizontal base shows "
              "the different activities. The bars show how much time is spent on each activity.",
              "Every bar has the same width, so only the height tells the number. A wider bar is not a bigger "
              "number.",
              "Think about it: how is Sheela's recording different from Raman's recording? Raman has rows of "
              "separate squares. Sheela has one solid bar for each activity.",
              "Rule: a bar graph stands each row of squares up as a bar, and the height of the bar is the number."],
       examples=[WE("Kabir records his Saturday with rows of squares, and one square stands for 1 hour: reading 3 "
                    "squares, playing 5 squares and helping at home 2 squares (practice values). Stand the rows up "
                    "as bars on a graph whose vertical line is marked 0 to 6. How many hours is that in all?",
                    ["Write the three activities along the horizontal base: reading, playing and helping at home.",
                     "Mark the vertical line 0, 1, 2, 3, 4, 5 and 6 for the number of hours. The tallest row has 5 "
                     "squares, so the line goes past 5.",
                     "Stand the reading row up. It has 3 squares, so the reading bar is 3 high.",
                     "Stand the playing row up. It has 5 squares, so the playing bar is 5 high.",
                     "Stand the helping at home row up. It has 2 squares, so that bar is 2 high.",
                     "Check: each bar is as tall as its row is long, 3, 5 and 2. Add the heights: 3 + 5 + 2 = 10 "
                     "hours in all."],
                    "Bars of height 3, 5 and 2. Kabir spent 3 + 5 + 2 = 10 hours on these three activities")],
       ncert=["day.story", "day.bar", "day.diff"],
       key_terms=["bar graph", "bar", "vertical line", "horizontal base"],
       misconceptions=["M_BAR_WIDTH"], minutes=6),
     A("T4.C2", "Reading and Comparing Bars", "Analyze",
       "Students read the height of each bar on the vertical line and compare two children's bars, saying who has "
       "more, how many more and which activity is the same.",
       teach=["Predict first: Kabir's reading row has 3 squares and Samaira's reading bar is 4 high. Who read for "
              "longer, and by how many hours?",
              "To read a bar, find its top and look straight across to the vertical line. The number there is the "
              "height. Read the height where the top meets the vertical line.",
              "A taller bar is more. Two bars of the same height show the same amount.",
              "To find how many more, take the smaller height from the bigger height. Samaira's 4 and Kabir's 3 give "
              "4 − 3 = 1, so Samaira read for 1 hour more.",
              "Compare the two children activity by activity, and say for each one who has more, how many more, or "
              "that the two are the same.",
              "Rule: read each bar by its height on the vertical line, the taller bar is more, and the difference of "
              "the two heights is how many more."],
       examples=[WE("Kabir's Saturday has rows of squares: reading 3, playing 5 and helping at home 2. Samaira's bar "
                    "graph of her Saturday has bars: reading 4, playing 3 and helping at home 2 (practice values). "
                    "Who spent more time reading, and by how many hours? Who played more, and by how many hours? On "
                    "which activity did they spend the same time?",
                    ["Read Kabir's rows by counting the squares: reading 3, playing 5 and helping at home 2.",
                     "Read Samaira's bars where each top meets the vertical line: reading 4, playing 3 and helping "
                     "at home 2.",
                     "Reading: Samaira 4 hours and Kabir 3 hours. 4 is more than 3, so Samaira read for longer.",
                     "How many hours more? 4 − 3 = 1 hour more.",
                     "Playing: Kabir 5 hours and Samaira 3 hours. Kabir played more, by 5 − 3 = 2 hours.",
                     "Helping at home: Kabir 2 hours and Samaira 2 hours. The two bars are the same height, so the "
                     "time is the same.",
                     "Check: the heights differ for reading, by 1, and for playing, by 2, and are equal only for "
                     "helping at home."],
                    "Samaira read 1 hour more. Kabir played 2 hours more. Helping at home is the same, 2 hours")],
       key_terms=["height", "compare", "bars", "difference"],
       misconceptions=["M_BAR_LABEL"], minutes=5),
     DOER("T4.C3", "Practice: Recording a Day", "squares_to_bars", "Apply",
          "Students use the numbers of Raman's recording and Sheela's recording to say who spends more time, how "
          "many more hours, and whether any activity is the same.",
          ["Stand a row of squares up and you get a bar as tall as the row is long.",
           "Read a bar where its top meets the vertical line.",
           "The taller bar is more, and the difference of two heights is how many more.",
           "Two bars of the same height show the same amount."],
          items=[FIO("day.q1", "Recording a Day: more time sleeping",
                     "Whose daily routine shows more time spent on sleeping? ___",
                     ["Raman's sleeping row has 9 squares. One square stands for 1 hour, so Raman sleeps 9 hours.",
                      "Sheela's sleeping bar reaches 8 on the vertical line, so Sheela sleeps 8 hours.",
                      "Compare the two numbers: 9 hours is more than 8 hours.",
                      "How many more? 9 − 8 = 1, so Raman sleeps 1 hour more.",
                      "Check: Raman's row of 9 squares would stand up as a bar 9 high, which is taller than Sheela's "
                      "bar of height 8."],
                     "Raman (9 hours; Sheela 8 hours)",
                     kind="exercise", q_figure=DAY,
                     s_figure="Raman's sleeping row of 9 squares beside Sheela's sleeping bar of height 8, with "
                              "Raman's longer row marked."),
                 FIO("day.q2", "Recording a Day: more hours in school",
                     "Who spends more hours in the school? ___",
                     ["Raman's school row has 6 squares, so Raman spends 6 hours in school.",
                      "Sheela's school bar reaches 7 on the vertical line, so Sheela spends 7 hours in school.",
                      "Compare the two numbers: 7 hours is more than 6 hours.",
                      "How many more? 7 − 6 = 1, so Sheela spends 1 hour more in school.",
                      "Check: Raman's row of 6 squares would stand up as a bar 6 high, which is shorter than "
                      "Sheela's bar of height 7."],
                     "Sheela (7 hours; Raman 6 hours)",
                     kind="exercise", q_figure=DAY,
                     s_figure="Raman's school row of 6 squares beside Sheela's school bar of height 7, with "
                              "Sheela's taller bar marked."),
                 FIO("day.q3", "Recording a Day: more hours studying",
                     "How many more hours does Sheela spend studying compared to Raman? ___",
                     ["Raman's studying row has 2 squares, so Raman studies 2 hours.",
                      "Sheela's studying bar reaches 4 on the vertical line, so Sheela studies 4 hours.",
                      "Take the smaller number from the bigger number: 4 − 2 = 2.",
                      "Sheela studies 2 hours more than Raman.",
                      "Check: Raman's 2 hours and 2 more hours make Sheela's 4 hours, because 2 + 2 = 4."],
                     "2 hours",
                     kind="exercise", q_figure=DAY,
                     s_figure="Raman's studying row of 2 squares beside Sheela's studying bar of height 4, with the "
                              "2 extra hours of Sheela's bar marked."),
                 FIO("day.q4", "Recording a Day: the same amount of time",
                     "Is there any activity on which they spend the same amount of time? If yes, name the activity "
                     "___",
                     ["Compare the two children activity by activity. Raman's squares give 9, 6, 2, 6 and 1 hours. "
                      "Sheela's bars give 8, 7, 4, 3 and 2 hours.",
                      "Sleeping: 9 and 8. The hours are different.",
                      "Time in school: 6 and 7. The hours are different.",
                      "Studying: 2 and 4. The hours are different.",
                      "Eating and playing: 6 and 3. The hours are different.",
                      "Other activities: 1 and 2. The hours are different.",
                      "Raman has 6 hours for school and 6 hours for eating and playing, but those are two "
                      "activities of one child. The question compares the same activity of both children.",
                      "Check: all five pairs are different, so the answer is No."],
                     "No. The hours are different on all five activities.",
                     kind="exercise", q_figure=DAY,
                     s_figure="Raman's rows and Sheela's bars side by side with the hours of each pair written under "
                              "them, 9 and 8, 6 and 7, 2 and 4, 6 and 3, 1 and 2, and no pair the same."),
                 FIO("day.q5", "Recording a Day: a more balanced routine",
                     "Based on their data, whose routine do you think is more balanced? Why? ___",
                     ["A balanced day gives fair time to each activity, so the hours are not very far apart. Look "
                      "at studying and at eating and playing.",
                      "Raman studies 2 hours and plays 6 hours. The two are far apart: 6 − 2 = 4 hours.",
                      "Sheela studies 4 hours and plays 3 hours. The two are close: 4 − 3 = 1 hour.",
                      "Sheela's studying and playing are closer together, so her routine is more balanced.",
                      "This is a sample answer. Another answer is right if the reason uses the numbers.",
                      "Check: both days add up to 24 hours, 9 + 6 + 2 + 6 + 1 = 24 and 8 + 7 + 4 + 3 + 2 = 24, so "
                      "the two days can be compared fairly."],
                     "Sample answer: Sheela's, because her studying 4 and playing 3 are closer than Raman's 2 and 6. "
                     "Your answer may differ.",
                     kind="exercise", q_figure=DAY,
                     s_figure="Raman's rows and Sheela's bars side by side, with studying 2 and 4 and eating and "
                              "playing 6 and 3 marked, and the hours of each day adding up to 24.")],
          misconceptions=["M_BAR_LABEL", "M_BAR_WIDTH"])],
    key_terms=["bar graph", "bar", "vertical line", "horizontal base", "height"]))

# ============================== T5 Making a Bar Graph (M2) =====================================================
TOPICS.append(TOPIC(
    "T5", "M2", "Making a Bar Graph", ["Day in My Life", "Whose Index Finger is Longer?"], "Apply",
    "Students make a bar graph from a table of numbers and from measured lengths in cm, and say which bar is the "
    "longest and which is the shortest.",
    "To make a bar graph, write the names along the horizontal base, mark equal steps on the vertical line up to at "
    "least the biggest number, and draw each bar up to its number. A bar can also be a real length in cm: the "
    "tallest bar is the longest.",
    [A("T5.C1", "Making a Bar Graph", "Apply",
       "Students make a bar graph from a table of five numbers by writing the names on the base and drawing each "
       "bar up to its number.",
       teach=["Predict first: Kabir's 24 hours are sleeping 8, school 6, studying 3, playing 4 and other 3. How "
              "tall must the vertical line go so that the biggest bar fits, and what goes along the base?",
              "Step 1: write the names of the activities along the horizontal base, one place for each, with equal "
              "spaces.",
              "Step 2: mark equal steps on the vertical line from 0 up to a number at least as big as the biggest "
              "number. The biggest number is 8, so the line must reach 8 or more.",
              "Step 3: draw each bar from the base up to its number. All the bars have the same width.",
              "Step 4: check that every bar's top is at its number and that the numbers add up to 24 hours.",
              "Rule: write the names on the base, mark the vertical line up to at least the biggest number, draw "
              "each bar up to its number, and check the total."],
       examples=[WE("Kabir's 24 hours (practice values): sleeping 8, school 6, studying 3, playing 4 and other 3. "
                    "Make a bar graph of his day.",
                    ["Look at the table. The biggest number is 8, so the vertical line must go up to at least 8. "
                     "Mark it 0 to 9 in equal steps.",
                     "Write the five names along the horizontal base, in equal spaces: sleeping, school, studying, "
                     "playing and other.",
                     "Draw the sleeping bar from the base up to 8.",
                     "Draw the school bar up to 6.",
                     "Draw the studying bar up to 3.",
                     "Draw the playing bar up to 4 and the other bar up to 3.",
                     "Check: every bar has the same width and its top meets its number. The hours add up: "
                     "8 + 6 + 3 + 4 + 3 = 24."],
                    "Five bars of height 8, 6, 3, 4 and 3, and 8 + 6 + 3 + 4 + 3 = 24 hours")],
       key_terms=["bar graph", "horizontal base", "vertical line", "bar"],
       misconceptions=["M_BAR_WIDTH"], minutes=6),
     A("T5.C2", "A Bar Graph of Lengths", "Apply",
       "Students show measured lengths as bars on a graph marked in cm and say which is the longest, which is the "
       "shortest and by how many cm.",
       teach=["Predict first: Samaira tears paper strips as long as three pencils, 9 cm, 6 cm and 4 cm, and stands "
              "them side by side on a graph. Which strip is the longest, and how much longer is it than the "
              "shortest?",
              "On this graph the vertical line is a ruler. It has 1 cm at the foot, then 2 cm, 3 cm and so on. The "
              "height of a bar is the length in cm.",
              "In your maths book you lay a paper strip on a finger, tear off the extra, and paste the strip on the "
              "graph. All the strips have the same width, so only the height tells the length.",
              "The longest strip is the tallest bar and the shortest strip is the shortest bar.",
              "To find how much longer, take the smaller height from the bigger height.",
              "Rule: the height of a bar is the length in cm, the tallest bar is the longest, and the difference of "
              "two heights is how much longer."],
       examples=[WE("Samaira measures three pencils: 9 cm, 6 cm and 4 cm (practice values). Show them as bars on a "
                    "graph marked in cm. Which pencil is the longest and which is the shortest? How much longer is "
                    "the longest than the shortest?",
                    ["Mark the vertical line in cm: 1 cm at the foot, then 2, 3 and so on up to 10.",
                     "Make one strip for each pencil, all of the same width: 9 cm, 6 cm and 4 cm long. Stand them "
                     "side by side on the horizontal base.",
                     "Read the heights where the tops meet the vertical line: 9, 6 and 4.",
                     "The tallest bar is 9 cm, so the longest pencil is 9 cm. The shortest bar is 4 cm.",
                     "How much longer? 9 − 4 = 5 cm longer.",
                     "Check: the shortest, 4 cm, and 5 cm more make the longest, because 4 + 5 = 9."],
                    "Longest 9 cm and shortest 4 cm. The longest is 9 − 4 = 5 cm longer")],
       key_terms=["length", "cm", "longest", "shortest"],
       misconceptions=["M_BAR_WIDTH"], minutes=5),
     DOER("T5.C3", "Practice: Bar Graph Builder", "bar_graph_builder", "Apply",
          "Students record their own 24 hours in a table, draw a bar graph of it, and use a graph of five strips "
          "to find the longest and the smallest index finger.",
          ["Write the names on the horizontal base and mark equal steps on the vertical line.",
           "Draw each bar up to its number, with all bars of the same width.",
           "Check that the numbers add up: a day has 24 hours.",
           "A bar can be a real length in cm, and the tallest bar is the longest."],
          items=[FIO("mine.record", "Day in My Life: record your day",
                     "Record your daily routine (24 hours) in hours and minutes, as necessary. Note the time spent "
                     "on activities like sleeping, studying, playing, eating, and others.",
                     ["Write each activity in a row of the table and the hours next to it. The sample below uses "
                      "practice values and whole hours only.",
                      "Sleeping 9 hours, time in school 5 hours and studying 2 hours.",
                      "Eating 2 hours, playing 3 hours and other activities 3 hours.",
                      "Add the hours of the six rows: 9 + 5 + 2 + 2 + 3 + 3 = 24.",
                      "Check: a whole day has 24 hours, so the six numbers must add up to 24. They do."],
                     "Sample answer (practice values): sleeping 9, school 5, studying 2, eating 2, playing 3, other "
                     "3; total 24 hours. Your answer will differ.",
                     kind="prompt", q_figure=MINE_TABLE,
                     s_figure="The same table filled in with practice values: Sleeping 9, Time in school 5, "
                              "Studying 2, Eating 2, then Playing 3 and Other activities 3 hours in the two empty "
                              "rows."),
                 FIO("mine.graph", "Day in My Life: make a bar graph",
                     "Make a bar graph of the time you spend on different activities in the space given below.",
                     ["Use the table of your day. This sample uses the practice values of the table before: 9, 5, "
                      "2, 2, 3 and 3 hours, all whole hours.",
                      "Write the six names along the horizontal base, one in each place: Sleeping, Time in School, "
                      "Studying, Eating, Playing and Other activities.",
                      "The biggest number is 9, and the vertical line goes from 0 to 9, so the tallest bar just "
                      "fits.",
                      "Draw the sleeping bar up to 9 and the school bar up to 5.",
                      "Draw the studying bar up to 2 and the eating bar up to 2.",
                      "Draw the playing bar up to 3 and the other activities bar up to 3.",
                      "Check: all bars have the same width, every top meets its number, and the numbers still add "
                      "up to 24 hours."],
                     "Sample answer (practice values): six bars of height 9, 5, 2, 2, 3 and 3. Your answer will "
                     "differ.",
                     kind="prompt", q_figure=MINE_GRAPH,
                     s_figure="The graph with six bars standing on the horizontal base (practice values): Sleeping "
                              "9, Time in School 5, Studying 2, Eating 2, Playing 3 and Other activities 3, with the "
                              "sleeping bar just reaching the top mark 9."),
                 FIO("finger.make", "Whose Index Finger is Longer?: the strips",
                     "Cut long paper strips from waste paper. Give one strip (each of the same width) to each of "
                     "your friends. Now, put the paper strip on your index finger and tear off the extra strip "
                     "extending above your fingers. Paste these paper strips along the horizontal line in the given "
                     "bar graph.",
                     ["This is a hands-on activity. The sample below uses practice values, and your friends' strips "
                      "will differ.",
                      "Cut five long strips of the same width, one for you and one for each of four friends.",
                      "Lay a strip on an index finger and tear off the extra part. Do this for each of the five "
                      "fingers.",
                      "The sample strips are: " + FINGER_SAMPLE + ".",
                      "Paste each strip standing up from the horizontal base, in its own place: Mine, then Friend 1 "
                      "to Friend 4. The vertical line has 1 cm marked at the foot, so the top of a strip tells how "
                      "long the strip is.",
                      "Check: the top of each strip meets its length on the vertical line, 6, 7, 5, 8 and 6."],
                     "Sample answer (practice values): strips of 6, 7, 5, 8 and 6 cm for Mine and Friend 1 to 4. "
                     "Your answer will differ.",
                     kind="prompt", q_figure=FINGER_GRAPH,
                     s_figure="The graph with five strips of the same width standing along the horizontal base "
                              "(practice values): " + FINGER_SAMPLE + "."),
                 FIO("finger.q1", "Whose Index Finger is Longer?: the longest",
                     "Whose index finger is the longest? ___",
                     ["Look at your graph of five strips. The sample uses practice values: " + FINGER_SAMPLE + ".",
                      "The tallest bar is the longest index finger, so compare the tops of the bars on the vertical "
                      "line.",
                      "The tops are at 6, 7, 5, 8 and 6. The biggest number is 8.",
                      "The bar that reaches 8 cm belongs to Friend 3.",
                      "Check: 8 is more than 6, 7, 5 and 6, and no other bar reaches 8. Friend 3 has the longest "
                      "index finger."],
                     "Sample answer (practice values): Friend 3. Your answer will differ.",
                     kind="exercise", q_figure=FINGER_GRAPH,
                     s_figure="The graph of the five strips (practice values) with the tallest strip, Friend 3 at "
                              "8 cm, marked."),
                 FIO("finger.q2", "Whose Index Finger is Longer?: its length",
                     "The length of the longest index finger is ___ cm.",
                     ["Use the longest bar of the question before. In the sample it is Friend 3's bar.",
                      "Read where its top meets the vertical line. The foot is marked 1 cm, so each mark is 1 cm.",
                      "The top is at 8, so the length is 8 cm.",
                      "Check: the strip itself, laid along a ruler, is 8 cm long, the same as the height of its "
                      "bar."],
                     "Sample answer (practice values): 8 cm. Your answer will differ.",
                     kind="exercise", q_figure=FINGER_GRAPH,
                     s_figure="The graph of the five strips (practice values) with a line from the top of Friend 3's "
                              "strip across to 8 on the vertical line."),
                 FIO("finger.q3", "Whose Index Finger is Longer?: the smallest",
                     "The smallest index finger is ___ cm long.",
                     ["The smallest index finger is the shortest bar.",
                      "In the sample the tops are at 6, 7, 5, 8 and 6. The smallest number is 5.",
                      "The shortest bar reaches 5, so the smallest index finger is 5 cm long.",
                      "Check: 5 is less than every other number, 6, 7, 8 and 6, so no other bar is as short."],
                     "Sample answer (practice values): 5 cm. Your answer will differ.",
                     kind="exercise", q_figure=FINGER_GRAPH,
                     s_figure="The graph of the five strips (practice values) with the shortest strip, Friend 2 at "
                              "5 cm, marked."),
                 FIO("finger.q4", "Whose Index Finger is Longer?: whose is it",
                     "It belongs to ___.",
                     ["This sentence goes with the question before. It asks whose index finger is the smallest "
                      "one.",
                      "From the question before, the smallest index finger is 5 cm long (practice values).",
                      "Find the bar that reaches 5. It is the bar of Friend 2.",
                      "Check: the bar of Friend 2 is the only one with its top at 5. The other tops are at 6, 7, 8 "
                      "and 6."],
                     "Sample answer (practice values): Friend 2. Your answer will differ.",
                     kind="exercise", q_figure=FINGER_GRAPH,
                     s_figure="The graph of the five strips (practice values) with the strip of Friend 2, the "
                              "smallest at 5 cm, marked and its place name on the horizontal base.")],
          misconceptions=["M_BAR_WIDTH", "M_BAR_LABEL"])],
    key_terms=["bar graph", "horizontal base", "vertical line", "length", "cm"]))

# ============================== T6 Using a Bar Graph (M2) ======================================================
TOPICS.append(TOPIC(
    "T6", "M2", "Using a Bar Graph", ["Food Wastage in the School Canteen"], "Analyze",
    "Students read a bar graph to find the highest, the lowest and the total, use a rule on the total, compare two "
    "days and make a prediction.",
    "The tallest bar is the highest and the shortest bar is the lowest. The total is all the bars added, and a rule "
    "such as 1 kg makes 2 bags is used on the total. To say which day had less, compare two bars. A prediction is a "
    "careful guess from the graph.",
    [A("T6.C1", "Using a Bar Graph: Totals and Predictions", "Analyze",
       "Students find the highest and the lowest bar, add the bars for the total, use a given rule on the total "
       "and make a careful prediction from a bar graph.",
       textbook=["Rani stays in a residential school. Her school's dining hall displays the amount of food wasted "
                 "and the number of children the food could have fed.",
                 "Given below is the data collected over the weekdays for different food items.",
                 "Rani was shocked to see the data. What do you think about food wastage? How can we reduce the "
                 "wastage of food? What can we do with the leftover food?"],
       teach=["Predict first: a class collects old newspapers on five days. Monday 3 kg, Tuesday 6 kg, Wednesday "
              "4 kg, Thursday 5 kg and Friday 2 kg. If 1 kg of newspaper makes 2 paper bags (a practice rule), how "
              "many bags can they make in all?",
              "The tallest bar is the highest: Tuesday, with 6 kg. The shortest bar is the lowest: Friday, with 2 kg.",
              "The total is all the bars added: 3 + 6 + 4 + 5 + 2 = 20 kg.",
              "A rule is used on the total. 1 kg makes 2 bags, so 20 kg make 20 × 2 = 40 bags.",
              "To say which day had less, compare two bars. Monday's bar is 3 and Thursday's bar is 5, so Monday "
              "had less than Thursday.",
              "To predict, look at the graph and make a careful guess, for example that the tallest bar may be the "
              "tallest again next week. A guess can be wrong.",
              "Think about it: what do you think about food wastage? How can we reduce the wastage of food? What can "
              "we do with the leftover food?",
              "Rule: the tallest bar is the highest, the shortest bar is the lowest, the total is all the bars "
              "added, and a rule such as 1 kg makes 2 bags is used on the total."],
       examples=[WE("A class collects old newspapers on five days (practice values): Monday 3 kg, Tuesday 6 kg, "
                    "Wednesday 4 kg, Thursday 5 kg and Friday 2 kg. Find the highest day, the lowest day and the "
                    "total. If 1 kg of newspaper makes 2 paper bags, how many bags can they make?",
                    ["Read each bar: Monday 3 kg, Tuesday 6 kg, Wednesday 4 kg, Thursday 5 kg and Friday 2 kg.",
                     "The tallest bar is Tuesday, so Tuesday is the highest, with 6 kg.",
                     "The shortest bar is Friday, so Friday is the lowest, with 2 kg.",
                     "Add all the bars for the total: 3 + 6 + 4 + 5 + 2 = 20 kg.",
                     "Use the rule on the total. 1 kg makes 2 bags, so the bags are 20 × 2 = 40.",
                     "Check by days: the days make 6, 12, 8, 10 and 4 bags, and 6 + 12 + 8 + 10 + 4 = 40."],
                    "Highest Tuesday (6 kg), lowest Friday (2 kg), total 20 kg, and 20 × 2 = 40 bags")],
       ncert=["food.story", "food.think"],
       key_terms=["bar graph", "total", "highest", "lowest"],
       misconceptions=["M_BAR_LABEL"], minutes=7),
     DOER("T6.C2", "Practice: Food Wastage", None, "Analyze",
          "Students read the food wastage graph to name the highest and the lowest, find the total, use the rule of "
          "3 children for each kg, compare two days and make a prediction.",
          ["The tallest bar is the highest and the shortest bar is the lowest.",
           "The total is all the bars added.",
           "A rule such as 1 kg feeds 3 children is used on the total.",
           "To say which day had less, compare two bars. A prediction is a careful guess from the graph."],
          items=[FIO("food.q1", "Food Wastage in the School Canteen: the highest",
                     "Which food item had the highest amount of wastage? ___",
                     ["Read each bar where its top meets the vertical line: Sandwich 5 kg, Paratha 6 kg, Khichdi "
                      "8 kg, Puri-Sabzi 7 kg and Idli-Sambar 4 kg.",
                      "The highest amount is the tallest bar. The biggest of 5, 6, 8, 7 and 4 is 8.",
                      "The bar that reaches 8 is Khichdi, on Wednesday.",
                      "Check: 8 kg is more than 5, 6, 7 and 4 kg, so no other bar is as tall."],
                     "Khichdi, 8 kg",
                     kind="exercise", q_figure=FOOD,
                     s_figure="The food wastage graph with the tallest bar, Khichdi on Wednesday at 8 kg, marked."),
                 FIO("food.q2", "Food Wastage in the School Canteen: the least",
                     "Which food item had the least amount of wastage? ___",
                     ["Read each bar where its top meets the vertical line: Sandwich 5 kg, Paratha 6 kg, Khichdi "
                      "8 kg, Puri-Sabzi 7 kg and Idli-Sambar 4 kg.",
                      "The least amount is the shortest bar. The smallest of 5, 6, 8, 7 and 4 is 4.",
                      "The bar that reaches 4 is Idli-Sambar, on Friday.",
                      "Check: 4 kg is less than 5, 6, 8 and 7 kg, so no other bar is as short."],
                     "Idli-Sambar, 4 kg",
                     kind="exercise", q_figure=FOOD,
                     s_figure="The food wastage graph with the shortest bar, Idli-Sambar on Friday at 4 kg, marked."),
                 FIO("food.q3", "Food Wastage in the School Canteen: the total",
                     "How much total food wastage was recorded in these days? ___",
                     ["Read the five bars: 5, 6, 8, 7 and 4 kg.",
                      "Add Sandwich and Paratha: 5 + 6 = 11 kg.",
                      "Add Khichdi: 11 + 8 = 19 kg.",
                      "Add Puri-Sabzi: 19 + 7 = 26 kg.",
                      "Add Idli-Sambar: 26 + 4 = 30 kg.",
                      "Check by adding in another order: 4 + 5 + 6 + 7 + 8 = 30."],
                     "30 kg, because 5 + 6 + 8 + 7 + 4 = 30",
                     kind="exercise", q_figure=FOOD,
                     s_figure="The food wastage graph with the five bars 5, 6, 8, 7 and 4 kg and the total 30 kg "
                              "written beside it."),
                 FIO("food.q4", "Food Wastage in the School Canteen: children fed",
                     "If 1 kg of food waste can feed 3 children, how many children could have been fed with the "
                     "total food wasted? ___",
                     ["The total food wasted is 30 kg, from the question before.",
                      "1 kg can feed 3 children, so 30 kg can feed 30 groups of 3 children.",
                      "Multiply: 30 × 3 = 90.",
                      "So 90 children could have been fed.",
                      "Check: 10 kg can feed 10 × 3 = 30 children, and 30 kg is three times 10 kg, so 30 + 30 + 30 "
                      "= 90."],
                     "90 children, because 30 × 3 = 90",
                     kind="exercise", q_figure=FOOD,
                     s_figure="The total 30 kg with an arrow to 90 children and a note that 1 kg feeds 3 children."),
                 FIO("food.q5", "Food Wastage in the School Canteen: a day with less",
                     "___ day had less food wastage than ___ day.",
                     ["Read the days from the graph: Monday 5 kg, Tuesday 6 kg, Wednesday 8 kg, Thursday 7 kg and "
                      "Friday 4 kg.",
                      "Pick two days and compare their bars. Take Friday and Monday: Friday's bar is 4 and "
                      "Monday's bar is 5.",
                      "4 is less than 5, so Friday had less food wastage than Monday.",
                      "Other pairs are right too: Monday and Tuesday (5 is less than 6), Tuesday and Thursday (6 is "
                      "less than 7), Thursday and Wednesday (7 is less than 8).",
                      "Check: the shorter bar is the day with less food wasted, and 5 − 4 = 1, so Friday had 1 kg "
                      "less than Monday."],
                     "Sample answer: Friday had less food wastage than Monday, because 4 kg is less than 5 kg. Your answer may differ.",
                     kind="exercise", q_figure=FOOD,
                     s_figure="The food wastage graph with the Friday bar at 4 kg and the Monday bar at 5 kg marked, "
                              "the shorter Friday bar in a different colour."),
                 FIO("food.q6", "Food Wastage in the School Canteen: a prediction",
                     "If the same food items are to be repeated next week, can you predict which food item is "
                     "likely to be wasted the most?",
                     ["To predict, look at the graph and think about what may happen again. A prediction is a "
                      "careful guess, not a sure fact.",
                      "This week's bars: Sandwich 5 kg, Paratha 6 kg, Khichdi 8 kg, Puri-Sabzi 7 kg and Idli-Sambar "
                      "4 kg.",
                      "Khichdi has the tallest bar, 8 kg, so it was wasted the most this week.",
                      "If the same foods come next week, Khichdi is likely to be wasted the most again.",
                      "A prediction can be wrong. It would be wrong if the children liked the khichdi more next "
                      "week.",
                      "Check: the guess uses the graph. The tallest bar of this week is Khichdi at 8 kg."],
                     "Sample answer: Khichdi, because its bar is the tallest, 8 kg. A prediction is a careful guess "
                     "and can be wrong. Your answer may differ.",
                     kind="exercise", q_figure=FOOD,
                     s_figure="The food wastage graph with the tallest bar, Khichdi at 8 kg, marked as the guess for "
                              "next week.")],
          misconceptions=["M_BAR_LABEL"])],
    key_terms=["bar graph", "total", "highest", "lowest", "prediction"]))
