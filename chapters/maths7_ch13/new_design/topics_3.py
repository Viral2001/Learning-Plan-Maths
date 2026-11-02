# -*- coding: utf-8 -*-
"""Topics T9 to T15 (module M3 visualising data, M4 data detective, M5 review). Book sections 5.3, 5.4, the end
questions, the lock puzzle and the summary. Graph readings marked 'about' are estimates read from the figures."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T9 Clustered bar graphs =====================================================
TOPICS.append(TOPIC(
    "T9", "M3", "Clubbing the Columns: Clustered Bar Graphs", ["5.3"], "Analyze",
    "Students read clustered bar graphs by first identifying the organisation, the scale and the patterns, then "
    "inferring from them, for onion prices and rocket launches, and judge which statements the data justifies.",
    "A clustered bar graph puts bars side by side; read the scale first, then infer.",
    [A("T9.C1", "Two column graphs become one clustered graph", "Analyze",
       "Students combine two column graphs of onion prices into one clustered column graph, find its scale, and "
       "compare the two towns month by month from the bar heights.",
       textbook=["5.3 Visualising Data",
                 "We can often understand data more clearly if it is presented as a picture. This is called data "
                 "visualisation. Last year, we saw how to visualise data using graphs. Let us explore visualisation "
                 "further.",
                 "Clubbing the Columns",
                 "Earlier, we looked at the monthly onion prices in Yahapur and Wahapur.",
                 "Two column graphs for this data are given below.",
                 "The two graphs can also be combined into a single graph. We just draw the bars side by side! Verify "
                 "if the data in the table matches the graph below.",
                 "We use different colours to clearly separate the data from the two places. This is called a "
                 "clustered column graph. Since it has two columns in each cluster, we also call it a double column "
                 "graph.",
                 "What is the scale used in this graph?",
                 "The relative heights of the bars tell us where onions are costlier in each month. We can also "
                 "visually estimate the difference by referring to the markings along the vertical line.",
                 "Is it now easier to compare month-wise prices in both places?",
                 "The dots and slanted lines within the bars help people who find difficulty in distinguishing "
                 "colours. It is also useful when things are printed in greyscale (black-and-white)."],
       teach=["Predict first: in which months will the second town's bar be taller?",
              "Read the scale from the vertical line: the guidelines go up by 10, so 1 unit = 10 rupees.",
              "Two bars per month make a cluster; compare the pair, then move to the next month."],
       examples=[
           WE("Draw the onion prices of the two towns as one double column graph with 1 unit = 10 rupees. In which "
              "months is the second town costlier, and by how much in September?",
              ["Put the months in order along the horizontal line, two bars per month.",
               "With 1 unit = 10 rupees, a price of 59 is 59 ÷ 10 = 5.9 units tall.",
               "The second town's bar is taller in April (30 against 28), May (38 against 30), July (42 against 39), "
               "September (53 against 49) and October (60 against 56).",
               "In June the two bars are equal at 35.",
               "In the other 6 months the first town's bar is taller.",
               "In September the difference is 53 − 49 = 4 rupees per kg."],
              "The second town is costlier in 5 months (April, May, July, September and October); in September by 4 "
              "rupees per kg",
              ncert=["5.3.onion_graphs"])],
       key_terms=["clustered column graph", "scale"], misconceptions=["M_SCALE_IGNORE"], minutes=8),
     A("T9.C2", "Rocket launches: identify, then infer", "Analyze",
       "Students read a clustered bar graph of rocket launches by identifying its scale and organisation, then infer "
       "patterns such as which organisations increased every year.",
       textbook=["10…9…8…7…6…5…4…3…2…1…Take Off!",
                 "You might have heard about scientific probes (like Chandrayaan-3 launched in 2023 by ISRO or the "
                 "Voyager-1 launched in 1977 by NASA), observational satellites (like Aryabhata launched in 1975 by "
                 "ISRO or Sputnik-1 launched in 1957 by the Soviet Space program), or about human spaceflights to the "
                 "International Space Station. All space missions are launched using rockets. Look at the graph below "
                 "showing the number of worldwide rocket launches by different organisations.",
                 "Share your observations (you may take the teacher's help to identify the countries these "
                 "organisations belong to).",
                 "Often there is a lot of information in graphs and it may be difficult to understand. We can follow a "
                 "2-step process to simplify making sense of the data in graphs.",
                 "Step 1: Identify what is given. Notice how the graph is organised, what scale is used, and what "
                 "patterns the data shows.",
                 "I wish they had shown guidelines for 5, 10, and 15 along the horizontal line. It would help in "
                 "estimating the smaller numbers.",
                 "For each organisation, the numbers of rocket launches for the years 2021, 2022, and 2023 are shown "
                 "as three adjacent bars. The scale used is 1 unit length = 20 rockets. Notice the numbers at the "
                 "bottom.",
                 "The 'Others' category indicates multiple organisations worldwide that are clubbed together to keep "
                 "the graph short.",
                 "Note that in the double bar graph of onion prices, the months are shown in order, i.e., January to "
                 "December, to observe the change over time, whereas in this case, a change in the order of "
                 "organisations does not affect the meaning.",
                 "Step 2: Infer from what is given. Analyse and interpret each of your observations.",
                 "We can say that the USA, China, and Russia are the leading rocket launching countries in the given "
                 "time period.",
                 "SpaceX launched about twice the number of rockets in 2022 compared to 2021. And it launched about 35 "
                 "more rockets in 2023 compared to 2022.",
                 "The number of rockets launched by Arianespace decreased every year.",
                 "United Launch Alliance launched more rockets in 2022 than in 2021. They launched fewer rockets in "
                 "2023 than in both the years 2022 and 2021.",
                 "Other organisations launched about 25 rockets in 2023."],
       teach=["Predict first: which organisation launched the most, and did it grow every year?",
              "Step 1, identify: three bars per organisation for 2021, 2022 and 2023; 1 unit = 20 rockets.",
              "Step 2, infer: read each pattern and say what it means.",
              "Bar readings are estimates; the graph has no guidelines below 20."],
       examples=[
           WE("From the rocket graph (readings about SpaceX 31, 61, 96; Arianespace 15, 6, 3; ISRO 2, 5, 7; Galactic "
              "Energy 1, 2, 7), which organisations launched more rockets every year, and how did SpaceX change?",
              ["Identify: 1 unit = 20 rockets, three bars per organisation in year order.",
               "SpaceX: 31, 61, 96, so it rose every year; 61 is about twice 31, and 96 − 61 = 35 more in 2023.",
               "Arianespace: 15, 6, 3, so it fell every year.",
               "ISRO: 2, 5, 7 and Galactic Energy: 1, 2, 7 also rose every year.",
               "Rocket Lab (6, 6, 9) and Expace (4, 4, 6) stayed the same once, so they did not rise every year."],
              "SpaceX, ISRO and Galactic Energy increased every year; SpaceX about doubled, then added about 35",
              ncert=["5.3.rockets"])],
       key_terms=["scale", "clustered bar graph"], misconceptions=["M_SCALE_IGNORE"], minutes=10),
     A("T9.C3", "Which rocket statements can the data justify?", "Evaluate",
       "Students test six statements about rocket launches against bar readings, totals and averages, and estimate "
       "the total launches worldwide in one year.",
       textbook=["Identify which of the following statements can be justified using this data.",
                 "(a) All organisations launched more rockets than the previous years.",
                 "(b) Only an organisation from the USA launched more than 50 rockets in a single year.",
                 "(c) The total number of rockets launched by France in all 3 years is less than 40.",
                 "(d) The average number of rockets launched by CASC in these 3 years is around 40.",
                 "(e) ISRO launched more rockets than Galactic Energy in these 3 years.",
                 "(f) Russia launched more than 60 rockets in these 3 years.",
                 "List the organisations that have consistently launched more rockets every year.",
                 "Estimate the total number of rockets launched worldwide in 2023. (a) less than 200 (b) 200 to 400 "
                 "(c) 400 to 600 (d) more than 600",
                 "We may have many questions after looking at the graph. We might wonder why USA launches so many more "
                 "rockets than other countries. Or we might be eager to look at the data from previous and later "
                 "years.",
                 "What are you curious to know after looking at this graph?"],
       teach=["Predict first: which statements will need a total, and which an average?",
              "Read each bar as an estimate, then add or divide.",
              "Arianespace is from France, CASC from China and Roscosmos from Russia."],
       examples=[
           WE("Using the readings CASC 48, 35, 45; Roscosmos 16, 21, 18; Arianespace 15, 6, 3; ISRO 2, 5, 7; Galactic "
              "Energy 1, 2, 7; SpaceX 31, 61, 96, decide which statements (a) to (f) are justified, and estimate the "
              "2023 world total.",
              ["(a) Not justified: Arianespace fell every year, and CASC fell from 48 to 35.",
               "(b) Justified: only SpaceX (USA) passes 50, with 61 and 96; CASC's highest is about 48.",
               "(c) Justified: France's Arianespace total is 15 + 6 + 3 = 24, less than 40.",
               "(d) Justified: CASC total 48 + 35 + 45 = 128, average 128 ÷ 3 ≈ 42.67, around 40.",
               "(e) Justified: ISRO 2 + 5 + 7 = 14 against Galactic Energy 1 + 2 + 7 = 10.",
               "(f) Not justified: Roscosmos 16 + 21 + 18 = 55, less than 60.",
               "2023 bars: 96 + 45 + 18 + 3 + 9 + 3 + 7 + 7 + 6 + 26 = 220, so the answer is (b), 200 to 400."],
              "Justified: (b), (c), (d) and (e); not justified: (a) and (f); 2023 total about 220, option (b)",
              ncert=["5.3.rockets_more"])],
       key_terms=["average", "total"], misconceptions=["M_SCALE_IGNORE", "M_HIGHEST_BEST"], minutes=10),
     DOER("T9.C4", "Practice: read a clustered bar graph", "bar_reader", "Analyze",
          "Students identify the scale and the organisation of a clustered bar graph, read bar values as estimates, "
          "and decide which statements the graph can justify.",
          ["Identify first: what is on each line, and what is the scale?",
           "Read each bar against the guidelines; say 'about'.",
           "Infer only what the bars can show."])]))

# ============================== T10 Daylight =================================================================
TOPICS.append(TOPIC(
    "T10", "M3", "Summer and Winter at the Same Time", ["5.3"], "Analyze",
    "Students convert monthly daylight hours to an average per day, read a clustered bar graph of two cities, and "
    "infer from the opposite patterns where on Earth the cities lie.",
    "Monthly totals divided by days give daylight per day; opposite patterns mean opposite hemispheres.",
    [A("T10.C1", "Daylight per day from monthly totals", "Apply",
       "Students turn monthly daylight hours into an average daylight per day by dividing by the days in each month, "
       "and find the longest and shortest days for two cities.",
       textbook=["Summer and Winter at the Same Time",
                 "The tables below show data related to weather in two cities in different countries. The numbers "
                 "given are in hours. Can you guess what the data might be related to?",
                 "City 1, January to December: 210, 257, 372, 441, 536, 564, 555, 465, 394, 310, 222, 186.",
                 "City 2, January to December: 459, 384, 381, 327, 304, 276, 295, 318, 369, 409, 435, 468.",
                 "The data shows the monthly hours of daylight (i.e., the Sun is at least partly above the horizon) in "
                 "these two cities over the year. Based on this data, a clustered bar graph showing the average "
                 "daylight hours per day in each month is given below. This average is obtained by dividing the "
                 "monthly daylight hours by the number of days in the month."],
       teach=["Predict first: which month will have the longest days in City 1?",
              "June has 30 days, December has 31: daylight per day is the monthly total divided by the days.",
              "A whole day has 24 hours, so no daily value can pass 24."],
       examples=[
           WE("City 1 had 564 hours of daylight in June and 186 in December; City 2 had 276 in June and 468 in "
              "December. Find the daylight per day in each case.",
              ["June has 30 days: City 1 gets 564 ÷ 30 = 18.8 hours a day.",
               "City 2 in June: 276 ÷ 30 = 9.2 hours a day.",
               "December has 31 days: City 1 gets 186 ÷ 31 = 6 hours a day.",
               "City 2 in December: 468 ÷ 31 ≈ 15.1 hours a day.",
               "City 1 has its longest days in June; City 2 has its shortest days in June."],
              "June: City 1 18.8, City 2 9.2 hours a day; December: City 1 6, City 2 about 15.1 hours a day",
              ncert=["5.3.daylight_daily"])],
       key_terms=["average", "daylight"], misconceptions=["M_MEAN_IN_DATA"], minutes=8),
     A("T10.C2", "Reading the daylight graph: two hemispheres", "Analyze",
       "Students read the daylight graph with scale 1 unit = 5 hours, describe how each city's daylight rises and "
       "falls, and infer that the cities lie in opposite hemispheres.",
       textbook=["Let us follow the 2-step process to identify and interpret the information presented.",
                 "Step 1: Identify what is given. Notice how the graph is organised, what scale is used, and what "
                 "patterns the data shows.",
                 "The horizontal line shows the months of the year. The vertical line shows the average daylight hours "
                 "per day, using the scale 1 unit = 5 hours. The month of June has the maximum value for City 1 and the "
                 "minimum value for City 2.",
                 "Step 2: Infer from what is given. Analyse and interpret each of your observations. Share appropriate "
                 "summary and conclusion statements.",
                 "The average number of daylight hours per day in City 1 increases from January, reaching a maximum of "
                 "about 17 to 18 hours in June. It then decreases, reaching a minimum of about 6 hours in December.",
                 "The average number of daylight hours per day in City 2 decreases from January, reaching a minimum of "
                 "about 9 hours in June. It then increases, reaching a maximum of about 15 hours in December.",
                 "The maximum and minimum values in City 1 are more extreme than those of City 2. That is, the maximum "
                 "number of daylight hours per day of City 1 is more than that of City 2, and the minimum number of "
                 "daylight hours per day of City 1 is less than that of City 2.",
                 "In June, City 1 experiences daylight for about 3/4th of the full day (24 hours), whereas during "
                 "December to January, it only experiences daylight for about 1/4th of the full day.",
                 "Does this give some idea of where these two cities are located?",
                 "City 1 and City 2 are located away from the Equator in the Northern and Southern hemispheres, "
                 "respectively. City 1 is Helsinki, Finland, and City 2 is Wellington, New Zealand. These are also shown "
                 "on the map. In June, the Northern Hemisphere is tilted towards the Sun, resulting in longer daylight "
                 "hours; it is summertime here. Meanwhile, the Southern Hemisphere is tilted away from the Sun, leading "
                 "to shorter days; it is winter time here. The inverted seasonal daylight pattern is due to the cities' "
                 "location in opposite hemispheres. The large variation in the data is because they are away from the "
                 "Equator.",
                 "Is there anything more that you wish to explore?",
                 "I got to know that during summer near the poles one can see the Sun even at midnight!! Very "
                 "interesting! If we are there at that time, we can go sightseeing even at midnight!",
                 "The Midnight Sun at Andøya, Norway."],
       teach=["Predict first: if one city has long days in June, what might the other city's June be like?",
              "Identify: months along the bottom, 1 unit = 5 hours up the side.",
              "Infer: opposite patterns mean opposite hemispheres; big swings mean far from the Equator.",
              "The table gives 18.8 hours for City 1 in June; reading the bar by eye gives about 17 to 18."],
       examples=[
           WE("Using daylight per day (City 1: about 6.8 in January, 18.8 in June, 6 in December; City 2: about 14.8 "
              "in January, 9.2 in June, 15.1 in December), describe both patterns and compare them with a full day.",
              ["City 1 rises from January to a maximum in June, then falls to a minimum in December.",
               "City 2 does the opposite: it falls to a minimum in June and rises to a maximum in December.",
               "City 1's range is 18.8 − 6 = 12.8 hours; City 2's is 15.1 − 9.2 = 5.9 hours, so City 1 is more extreme.",
               "A full day is 24 hours: 24 × 3 ÷ 4 = 18, so June daylight in City 1 is about three quarters of the day.",
               "24 ÷ 4 = 6, so December daylight in City 1 is about a quarter of the day.",
               "Opposite patterns point to opposite hemispheres: City 1 is Helsinki, City 2 is Wellington."],
              "City 1 peaks in June and City 2 in December; City 1 swings more (12.8 hours against 5.9), because the "
              "cities lie in opposite hemispheres, far from the Equator",
              ncert=["5.3.daylight_graph", "5.3.midnight_sun"])],
       key_terms=["hemisphere", "scale"], misconceptions=["M_SCALE_IGNORE"], minutes=10),
     DOER("T10.C3", "Practice: from monthly totals to a daily graph", "daylight", "Apply",
          "Students divide monthly daylight totals by the days in each month, draw the daily bars with a chosen scale, "
          "and describe the pattern of each city.",
          ["Divide by the days in that month: 28, 30 or 31.",
           "No day has more than 24 hours.",
           "Opposite patterns point to opposite hemispheres."])]))

# ============================== T11 Cricket and the graph questions =========================================
TOPICS.append(TOPIC(
    "T11", "M3", "All it Takes is a Minute: Runs per Over", ["5.3"], "Analyze",
    "Students read a double bar graph of runs per over with wickets marked, infer who batted first and who won, and "
    "choose scales to draw their own double bar graphs.",
    "The graph's shape tells the match story: overs, runs per over, wickets and where it stopped.",
    [A("T11.C1", "Who batted first? Reading runs per over", "Analyze",
       "Students read runs per over from a double bar graph with scale 1 unit = 5 runs, infer who batted first and who "
       "won from where the bars stop, and explain why the target is hard to read.",
       textbook=["All it Takes is a Minute",
                 "Have you ever missed watching a cricket match? You can catch up in a minute by looking at a graph. "
                 "You might have seen graphs like the following one.",
                 "The horizontal line lists the overs starting from 1, and the vertical line indicates the runs scored "
                 "in each over. The graph shows the number of runs scored per over as a double bar graph, each bar "
                 "corresponding to a team. Let us call them the blue team (denoted by blue) and the red team (denoted by "
                 "red). The scale used for the runs per over is 1 unit = 5 runs. The circles shown on top of the bars "
                 "indicate that a wicket fell in that over.",
                 "Answer the following questions based on the graph:",
                 "1. Can we tell who batted first? Who won the match?",
                 "2. How many runs did the blue team score in over 12?",
                 "3. In which over did the red team score the least number of runs?",
                 "4. Is it easy to tell the target set by the team batting first?"],
       teach=["Predict first: one team's bars stop after over 18. What could that mean?",
              "Read each bar against the guidelines at 5, 10 and 15.",
              "A chasing team stops early only when it reaches the target; a team batting first plays all its overs "
              "unless it is all out."],
       examples=[
           WE("The blue team's bars run through all 20 overs with several wickets; the red team's bars stop after "
              "over 18 with no wicket circles. Who batted first and who won? Read blue's over 12 and red's lowest "
              "over, and say whether the target is easy to find.",
              ["Red stopped after 18 overs without losing all its wickets.",
               "A team batting second stops early only when it reaches the target, so blue batted first and red won.",
               "Estimate from the graph: blue's over 12 bar reaches the 15 guideline (accept 14 to 16), so blue scored about 15 runs in that over.",
               "Red's shortest bar is over 4, an estimate of about 2 runs (accept 1 to 3).",
               "The target is blue's total plus 1, which needs all 20 of blue's bars added, so it is not easy to tell "
               "at a glance."],
              "Blue batted first and red won; estimates: blue scored about 15 in over 12 (accept 14 to 16); red's lowest was "
              "over 4 with about 2 runs (accept 1 to 3); the "
              "target needs 20 bars added, so it is not easy",
              ncert=["5.3.cricket"])],
       key_terms=["double bar graph", "scale"], misconceptions=["M_SCALE_IGNORE"], minutes=8),
     DOER("T11.C2", "Practice: choose a scale and draw", "scale_chooser", "Apply",
          "Students choose a scale that fits the largest value, draw double bar graphs for counted or measured data, "
          "and read the finished graphs to answer questions.",
          ["The largest value must fit on the vertical line.",
           "One unit can stand for 2, 4, 5, 10 or more.",
           "Use a key for the two colours."],
          items=[
              FIO("5.3.FiO3_1", "Figure it Out (graphs), Q1",
                  "The following infographic shows the speeds of a few animals in air, on land, and in water. Can we "
                  "call this graph a bar graph? (a) What is the scale used in this graph? (b) What did you find "
                  "interesting in this infographic? What do you want to explore further? (c) Identify a pair of "
                  "creatures where one's speed is about twice that of the other. (d) Can we say that a sailfish is "
                  "about 4 times faster than a humpback whale? Can we say that a sailfish is the fastest aquatic animal "
                  "in the world?",
                  ["Yes: each animal's length along the speed line stands for its speed, as a bar does.",
                   "(a) The marks go up in equal steps of about 16 kilometres per hour (10 miles per hour each).",
                   "(b) Answers vary; for example, the peregrine falcon dives at about 322 kilometres per hour.",
                   "(c) Falcon 322 and swift about 170 (estimate, accept 160 to 180): 322 ÷ 170 ≈ 1.89, about twice. Sailfish about 109 and flying "
                   "fish about 56: 109 ÷ 56 ≈ 1.95, about twice.",
                   "(d) Estimates from the bars: sailfish about 109 (accept 105 to 113) and humpback whale about 26 (accept 22 to 30): 109 ÷ 26 ≈ 4.19, so yes, about 4 times.",
                   "But only five water animals are shown, so the graph cannot say the sailfish is the fastest in "
                   "the world."],
                  "Yes, it is a bar graph with equal steps of about 16 kilometres per hour; falcon and swift are about "
                  "twice; sailfish is about 4 times the humpback (estimates about 109, accept 105 to 113, and about 26, "
                  "accept 22 to 30; 109 ÷ 26 ≈ 4.19), but fastest in the world cannot be "
                  "told from five animals"),
              FIO("5.3.FiO3_2", "Figure it Out (graphs), Q2",
                  "Preyashi asked her students 'If you were to get a super power to become aquatic (water-borne), "
                  "aerial (air-borne), or spaceborne which one would you choose?'. The responses are shown below. Some "
                  "chose none. Draw a double-bar graph comparing how both grades chose each option. Choose an "
                  "appropriate scale. Grade 5: w, a, a, a, w, n, s, a, n, w, a, a, a, a, a, w, w, s, a, a, n, w, a, a, "
                  "n. Grade 9: n, w, s, a, s, w, s, s, a, a, w, s, s, a, s, a, n, w, s, s, a, w, a, w, a",
                  ["Count each letter: a aerial, w water-borne, s spaceborne, n none.",
                   "Grade 5: aerial 13, water-borne 6, none 4, spaceborne 2 (13 + 6 + 4 + 2 = 25).",
                   "Grade 9: spaceborne 9, aerial 8, water-borne 6, none 2 (9 + 8 + 6 + 2 = 25).",
                   "The largest count is 13, so 1 unit = 2 children fits on a line up to 14.",
                   "Draw two bars for each option, one per grade, with a key.",
                   "Grade 5 chose aerial most; Grade 9 chose spaceborne most."],
                  "Grade 5: a 13, w 6, s 2, n 4; Grade 9: a 8, w 6, s 9, n 2; scale 1 unit = 2 children; Grade 5 "
                  "prefers aerial, Grade 9 spaceborne", tool="scale_chooser"),
              FIO("5.3.FiO3_3", "Figure it Out (graphs), Q3",
                  "The temperature variation over two days in different months in Jodhpur, Rajasthan, is given below. "
                  "Draw a double-bar graph. Use the scale 1 unit = 4°C. Can you guess which two months these days might "
                  "belong to? Times: 12 am, 3 am, 6 am, 9 am, 12 pm, 3 pm, 6 pm, 9 pm. Day 1: 20°C, 18°C, 16°C, 20°C, "
                  "26°C, 34°C, 30°C, 24°C. Day 2: 37°C, 34°C, 30°C, 33°C, 37°C, 43°C, 42°C, 39°C.",
                  ["With 1 unit = 4°C, 20°C is 20 ÷ 4 = 5 units and 43°C is 43 ÷ 4 = 10.75 units.",
                   "Draw two bars at each time, one for each day.",
                   "Day 1 runs from 16°C to 34°C, a range of 34 − 16 = 18°C, mean 188 ÷ 8 = 23.5°C.",
                   "Day 2 runs from 30°C to 43°C, a range of 43 − 30 = 13°C, mean 295 ÷ 8 = 36.875°C.",
                   "Cool nights near 16°C suggest winter, for example December or January.",
                   "Nights above 30°C and an afternoon of 43°C suggest peak summer, for example May or June."],
                  "Day 1 is likely a winter day (December or January) and Day 2 a summer day (May or June)",
                  tool="scale_chooser"),
              FIO("5.3.FiO3_4", "Figure it Out (graphs), Q4",
                  "The following clustered-bar graph shows the number of electric vehicles registered in some states "
                  "every year from 2022 to 2024. (a) The data (rounded-off to thousands) for the states of Gujarat and "
                  "Delhi are given in the table below (Gujarat 69000, 89000, 78000; Delhi 62000, 74000, 81000). Mark the "
                  "corresponding bars on the bar graph. (b) Notice how the graph is organised, what scale is used, and "
                  "what patterns the data shows. (c) How would you describe the change for various states between 2022 "
                  "and 2024? (d) Approximately how many more registrations did Assam get in 2023 compared to 2022? (e) "
                  "How many times more did the registrations in West Bengal increase from 2022 to 2024? (f) Is this "
                  "statement correct: 'There were very few new registrations in Uttarakhand in 2023 and 2024, as the "
                  "increase in the bar lengths is minimal'?",
                  ["(a) The guidelines are at 25000, 50000, 75000 and 100000. Gujarat's 89000 lies between 75000 and "
                   "100000; Delhi's 62000 lies between 50000 and 75000.",
                   "(b) Three bars per state for 2022, 2023 and 2024; 1 unit = 25000 vehicles; most bars grow left to "
                   "right.",
                   "(c) Readings (estimates): Uttarakhand about 15000 to 19000, West Bengal about 10500 to 43000, "
                   "Andhra Pradesh about 29500 to 55000, Odisha about 27500 to 62500, Assam about 40000 to 64500. "
                   "Every state rose, Odisha by the most (62500 − 27500 = 35000); Gujarat rose then fell.",
                   "(d) Assam: about 60000 − 40000 = 20000 more.",
                   "(e) West Bengal: 43000 ÷ 10500 ≈ 4.1, about 4 times.",
                   "(f) Not correct: each bar counts that year's new registrations, about 16500 in 2023 and 19000 in "
                   "2024. Only the growth from year to year was small."],
                  "(d) about 20000 more (e) about 4 times (43000 ÷ 10500 ≈ 4.1) (f) not correct: about 16500 and 19000 "
                  "new registrations were made in those years; only the increase was small")],
          ncert=[], misconceptions=["M_SCALE_IGNORE"])]))

# ============================== T12 Telling tall tales ======================================================
TOPICS.append(TOPIC(
    "T12", "M4", "Telling Tall Tales: Data Detective", ["5.4"], "Evaluate",
    "Students compare height dot plots of two schools, test statements against a table of average heights in India "
    "over thirty years, and find where growth is fastest, deciding what averages can and cannot justify.",
    "Averages describe groups, not every child; test each claim against the table before believing it.",
    [A("T12.C1", "Heights in two schools: what do you notice?", "Analyze",
       "Students compare the mean heights of boys and girls in Grades 6, 7 and 8 at two schools, and explain why one "
       "or two schools cannot settle whether boys or girls are taller.",
       textbook=["5.4 Data Detective",
                 "We put well-formed sentences one after the other to make a beautiful story. In the same way, "
                 "well-organised and well-presented data can tell interesting stories, and can also expose new "
                 "mysteries or help solve mysteries!",
                 "Telling Tall Tales",
                 "Earlier, we saw data of two Grade 5 classrooms with heights of boys and girls in each class. There, "
                 "the average height of girls was more than boys in one class and vice versa in the other class.",
                 "Following are the dot plots of heights of boys (in blue) and girls (in orange) of Grades 6, 7 and 8 "
                 "(in that order) of two different schools. What do you notice? Share your observations.",
                 "School A means: Grade 6 boys 134.8, girls 137.78; Grade 7 boys 141.8, girls 141.83; Grade 8 boys "
                 "149.35, girls 147.81.",
                 "School B means: Grade 6 boys 149.84, girls 150.2; Grade 7 boys 156.14, girls 155.41; Grade 8 boys "
                 "156.14, girls 156.83.",
                 "Looking at this data, you might wonder: 'Why is there a considerable difference in heights in the "
                 "same grades across these two schools?' 'Where are these schools located?' 'How tall are students in "
                 "Grades 6 to 8 in my school?' 'What is the average height of all Grade 6 boys and girls?'",
                 "We see that men are taller than women in general. But what about the heights of boys and girls? Are "
                 "boys taller than girls? Well, just by looking at the data of one or two schools, we cannot generalise "
                 "for all children in our country, or around the world."],
       teach=["Predict first: in which school are the students taller, and does it hold in every grade?",
              "Compare the same grade across schools, then boys with girls in the same grade.",
              "The two School B boys' plots both show 156.14; it may be a repeat in the picture."],
       examples=[
           WE("Using the printed means, compare the two schools grade by grade, and boys with girls in each school.",
              ["Grade 6 boys: 149.84 − 134.8 = 15.04 cm taller in the second school.",
               "Every grade, boys and girls, has a higher mean in the second school.",
               "First school: girls ahead in Grade 6 (137.78 against 134.8), nearly equal in Grade 7 (141.83 against "
               "141.8), boys ahead in Grade 8 (149.35 against 147.81).",
               "Second school: girls ahead in Grades 6 and 8, boys ahead in Grade 7.",
               "The answer to 'boys or girls?' changes with grade and school, so two schools cannot settle it."],
              "The second school is taller in every grade; boys against girls changes from grade to grade, so no "
              "general claim follows",
              ncert=["5.4.tall_tales"])],
       key_terms=["mean", "generalise"], misconceptions=["M_AVERAGE_ALL"], minutes=8),
     A("T12.C2", "Average heights in India: which statements hold?", "Evaluate",
       "Students test six statements about average heights of boys and girls aged 5 to 19 in 1989, 1999, 2009 and "
       "2019 against the table, sorting each as justified, not justified or not decidable.",
       textbook=["Let us look at some data (based on a survey) of the heights of boys and girls of different ages in "
                 "India over time. The following table shows the average heights of boys and girls (in centimeters) "
                 "across ages 5 to 19 in the years 1989, 1999, 2009, and 2019. In each year, the first column shows "
                 "boys' heights and the second column shows girls' heights.",
                 "Spend sufficient time observing the data presented in this table. Share your findings with the class.",
                 "These are some prompts for you to probe: Changes in the heights of boys or girls of a certain age "
                 "from 1989 to 2019. The heights of boys vs. girls at different ages in a particular year. Changes in "
                 "height between successive ages in boys and girls in 2019.",
                 "Which of the following statements can be justified using the data?",
                 "1. The average heights of both boys and girls at every age increased from 1989 to 2019.",
                 "2. The average height of 13-year-old girls in 1989 is more than the average height of 14-year-old "
                 "girls in 2009.",
                 "3. The average height of 15-year-old boys in 2019 is more than the average height of 16-year-old boys "
                 "in 1989.",
                 "4. All girls aged 13 are taller than all girls aged 11.",
                 "5. Throughout the age period 5 to 19, the average boy's height is more than the average girl's "
                 "height.",
                 "6. Boys keep growing even beyond age 19."],
       teach=["Predict first: which statements talk about averages, and which about every single child?",
              "Find the two cells a statement compares, then compare them.",
              "A table of averages cannot prove anything about all individuals, nor about ages it does not show."],
       examples=[
           WE("Test the six statements against the table of average heights.",
              ["1. Justified: at every age both columns are higher in 2019 than in 1989, for example age 19 boys 163.5 "
               "to 166.5 and girls 151.9 to 155.2 (some ages dipped slightly in between, for example boys aged 15, "
               "155.4 to 155.2 from 1989 to 1999).",
               "2. Not justified: 13-year-old girls in 1989 are 143.2, less than 14-year-old girls in 2009 at 148.",
               "3. Justified: 15-year-old boys in 2019 are 159, more than 16-year-old boys in 1989 at 158.9.",
               "4. Not justified: averages say nothing about every girl; some 11-year-olds can be taller than some "
               "13-year-olds.",
               "5. Not justified: girls' averages are higher at ages 11 and 12 in every year, for example 2019 age 11, "
               "138.6 against 137.",
               "6. Not decidable: the table stops at 19; in 2019 boys grew only 166.5 − 166 = 0.5 cm from 18 to 19."],
              "Justified: 1 and 3; not justified: 2, 4 and 5; 6 cannot be decided from the table",
              ncert=["5.4.india_table"])],
       key_terms=["average", "justified"], misconceptions=["M_AVERAGE_ALL"], minutes=12),
     A("T12.C3", "When do children grow fastest? Estimating heights", "Evaluate",
       "Students find the largest yearly growth for boys and girls in 2019, estimate heights for ages 1 to 4 from a "
       "newborn's 50 cm, and project heights for 2029 from the trend.",
       textbook=["In 2019, between which two successive ages from 5 to 19 did boys grow the most? Between which two "
                 "successive ages from 5 to 19 did girls grow most?",
                 "Suppose the average height of a newborn is 50 cm. Estimate the average height of young children of "
                 "ages 1 to 4.",
                 "Based on the trend observed in the table, write your estimates of the heights of boys and girls for "
                 "ages 5 to 19 in the year 2029.",
                 "Whenever you see data or some graph, look closely to know the story it has to say and the mysteries "
                 "it may hold."],
       teach=["Predict first: do girls or boys have their biggest growth year earlier?",
              "Subtract each age's height from the next age's height in the 2019 columns.",
              "For estimates, say what trend you used; any well-reasoned estimate is acceptable."],
       examples=[
           WE("Using the 2019 columns, find the largest growth between successive ages for boys and for girls. Then "
              "estimate heights for ages 1 to 4, and for age 12 in 2029.",
              ["Boys aged 12 to 13: 148.4 − 142.2 = 6.2 cm, the largest jump for boys.",
               "Girls aged 10 to 11: 138.6 − 132.8 = 5.8 cm, the largest jump for girls.",
               "From 50 cm at birth to about 107 cm at age 5 is 107 − 50 = 57 cm, or 57 ÷ 5 = 11.4 cm a year if even.",
               "Babies grow fastest in the first years, so estimates like 75, 87, 95 and 101 cm for ages 1 to 4 fit "
               "better than equal steps.",
               "For 2029, add the 2009 to 2019 change again: boys aged 12, 142.2 + 3.3 = 145.5 cm; girls aged 12, "
               "143.8 + 2.7 = 146.5 cm."],
              "Boys grew most from 12 to 13 (6.2 cm), girls from 10 to 11 (5.8 cm); ages 1 to 4 about 75, 87, 95 and "
              "101 cm (estimates); age 12 in 2029 about 145.5 cm for boys and 146.5 cm for girls",
              ncert=["5.4.india_growth"])],
       key_terms=["growth", "estimate"], misconceptions=["M_AVERAGE_ALL"], minutes=10),
     DOER("T12.C4", "Practice: justified, not justified or cannot tell", "claim_bins", "Evaluate",
          "Students sort statements about a data table into justified, not justified and cannot tell, pointing to the "
          "cells that decide each statement.",
          ["Find the exact cells the statement compares.",
           "Averages describe groups, not every member.",
           "Data cannot speak about ages, places or years it does not include."])]))

# ============================== T13 Zoomed axes and a mean decision ==========================================
TOPICS.append(TOPIC(
    "T13", "M4", "Zoomed Charts and a Mean Decision", ["5.4"], "Evaluate",
    "Students read a chart whose axis starts at 145 cm, explain how a zoomed axis exaggerates differences, judge a "
    "decision built on an average alone, and pull the chapter together in mixed questions.",
    "A zoomed axis enlarges small differences; an average alone can make a poor decision.",
    [A("T13.C1", "A chart that starts at 145 cm", "Evaluate",
       "Students read a chart of average heights of 19 year olds in many countries whose axis starts at 145 cm, and "
       "compare bar lengths with the true heights to see how the zoomed axis exaggerates differences.",
       textbook=["You may want to look at the data of weights. Or you might be curious to see if such patterns are "
                 "present in other countries as well. You might also wonder if humans were much shorter a few "
                 "centuries ago! Also, are people in some countries taller than others? The following visualisation "
                 "shows the change in average heights of 19-year-old boys and girls of different countries from 1989 "
                 "to 2019.",
                 "How is the graph organised? What information is presented?",
                 "What do you find interesting?",
                 "Notice that the vertical line starts from 145 cm, this helps give a closer (zoomed in) look at the "
                 "heights."],
       teach=["Predict first: if one bar looks twice as long as another, is that height twice as big?",
              "Identify: one marker for each group (boys and girls, 1989 and 2019) per country; the axis starts at 145.",
              "A zoomed axis helps see small changes, but lengths no longer compare in the true ratio."],
       examples=[
           WE("On a chart whose axis starts at 145 cm, one marker sits at 165 cm and another at 155 cm. How do their "
              "lengths from the axis compare, and how do the heights compare?",
              ["Length above the axis: 165 − 145 = 20 and 155 − 145 = 10.",
               "So the first looks 20 ÷ 10 = 2 times as tall.",
               "True heights: 165 ÷ 155 ≈ 1.06, only about 6 percent taller.",
               "The zoomed axis makes a 10 cm difference look like doubling.",
               "Always read the values from the axis, not the lengths."],
              "The first looks 2 times as tall, but the true ratio is 165 ÷ 155 ≈ 1.06",
              ncert=["5.4.countries"])],
       key_terms=["axis", "zoomed"], misconceptions=["M_BASELINE"], minutes=8),
     A("T13.C2", "A mean decision: a door for the family", "Evaluate",
       "Students test what happens when a door is built at a family's mean height, count who must bend, and explain why "
       "a decision should use the maximum here rather than the mean.",
       textbook=["A Mean Decision!",
                 "Perhaps using the average height of the family to make the door was not a good idea!",
                 "Look at this picture of the current world's tallest and shortest humans together."],
       teach=["Predict first: if a door is as tall as the family's average height, who will hit their head?",
              "The question decides the measure: a door must fit the tallest, so use the maximum.",
              "The mean of the tallest and the shortest human would describe neither of them."],
       examples=[
           WE("A family's heights are 169, 173, 155, 165, 160 and 164 cm. A door is made at the mean height. Who must "
              "bend, and what height should the door be?",
              ["Total: 169 + 173 + 155 + 165 + 160 + 164 = 986 cm.",
               "Mean: 986 ÷ 6 ≈ 164.33 cm.",
               "Taller than 164.33: 165, 169 and 173, so 3 of the 6 members must bend.",
               "A door must fit everyone, so it must be taller than the maximum, 173 cm, with some room to spare."],
              "3 members must bend; the door should be taller than the maximum, 173 cm",
              ncert=["5.4.mean_decision"])],
       key_terms=["maximum", "decision"], misconceptions=["M_MEAN_ALWAYS"], minutes=6),
     DOER("T13.C3", "Pull it together and do it: the chapter questions", "baseline", "Evaluate",
          "Students answer mixed questions using dot plots, the mean, the median, the range and double bar graphs, "
          "choosing the measure and the picture that suit each question and its data.",
          ["Choose the measure that fits the question.",
           "Read the scale and the starting value of every axis.",
           "Count zeros; leave out missing values."],
          items=[
              FIO("5.4.end1", "Figure it Out (chapter questions), Q1",
                  "The dot plots below show the distribution of the number of pockets on clothing for a group of boys "
                  "and for a group of girls. Based on the dot plots, which of the following statements are true? (a) "
                  "The data varies more for the boys than for the girls. (b) The median number of pockets for the boys "
                  "is more than that for the girls. (c) The mean number of pockets for the girls is more than that for "
                  "the boys. (d) The maximum number of pockets for boys is greater than that for the girls.",
                  ["Boys (12): 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6. Girls (13): 0, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 6.",
                   "(a) Boys' range 6 − 3 = 3; girls' range 6 − 0 = 6. The girls vary more, so false.",
                   "(b) Boys' median (5 + 5) ÷ 2 = 5; girls' median is the 7th value, 4. True.",
                   "(c) Boys' mean 56 ÷ 12 ≈ 4.67; girls' mean 45 ÷ 13 ≈ 3.46. False.",
                   "(d) Both maximums are 6. False."],
                  "Only (b) is true"),
              FIO("5.4.end2", "Figure it Out (chapter questions), Q2",
                  "The following table shows the points scored by each player in four games: A: 14, 16, 10, 10. B: 0, "
                  "8, 6, 4. C: 8, 11, did not play, 13. (a) Find the average number of points scored per game by A. (b) "
                  "To find the mean number of points scored per game by C, would you divide the total points by 3 or by "
                  "4? Why? What about B? (c) Who is the best performer?",
                  ["(a) A: 14 + 16 + 10 + 10 = 50, so 50 ÷ 4 = 12.5 points per game.",
                   "(b) C did not play one game, so divide by 3: 8 + 11 + 13 = 32 and 32 ÷ 3 ≈ 10.67.",
                   "B played all four games; the 0 is a real score, so divide by 4: 18 ÷ 4 = 4.5.",
                   "(c) A has the highest mean, 12.5, so A is the best performer."],
                  "(a) 12.5 (b) C by 3, about 10.67; B by 4, 4.5 (c) A", tool="baseline"),
              FIO("5.4.end3", "Figure it Out (chapter questions), Q3",
                  "The marks (out of 100) obtained by a group of students in a General Knowledge quiz are 85, 76, 90, "
                  "85, 39, 48, 56, 95, 81 and 75. Another group's scores in the same quiz are 68, 59, 73, 86, 47, 79, "
                  "90, 93 and 86. Compare and describe both the groups performance using, mean and median.",
                  ["First group (10): total 730, mean 730 ÷ 10 = 73; sorted, median (76 + 81) ÷ 2 = 78.5; range "
                   "95 − 39 = 56.",
                   "Second group (9): total 681, mean 681 ÷ 9 ≈ 75.67; sorted, the 5th value gives median 79; range "
                   "93 − 47 = 46.",
                   "The second group is a little higher on both mean and median and less spread out.",
                   "In the first group the low scores 39 and 48 pull the mean below the median."],
                  "First group: mean 73, median 78.5; second group: mean ≈ 75.67, median 79; the second group did "
                  "slightly better"),
              FIO("5.4.end4", "Figure it Out (chapter questions), Q4",
                  "Consider this data collected from a survey of a colony. Favourite sport, watching: cricket 1240, "
                  "basketball 470, swimming 510, hockey 430, athletics 250. Participating: cricket 620, basketball 320, "
                  "swimming 320, hockey 250, athletics 105. Choose an appropriate scale and draw a double-bar graph. "
                  "Write down your observations.",
                  ["The largest value is 1240, so 1 unit = 200 people fits on a line up to 1400.",
                   "Cricket watching is 1240 ÷ 200 = 6.2 units; athletics participating is 105 ÷ 200 = 0.525 units.",
                   "Draw a watching bar and a participating bar for each sport, with a key.",
                   "In every sport more people watch than take part.",
                   "Cricket leads both, and 620 ÷ 1240 = 0.5, so half as many play cricket as watch it.",
                   "Watching totals 2900 and participating 1615."],
                  "Scale 1 unit = 200 people; watchers outnumber players in every sport; cricket leads both, with "
                  "players half of watchers"),
              FIO("5.4.end5", "Figure it Out (chapter questions), Q5",
                  "Consider a group of 17 students with the following heights (in cm): 106, 110, 123, 125, 117, 120, "
                  "112, 115, 110, 120, 115, 102, 115, 115, 109, 115, 101. The sports teacher wants to divide the class "
                  "into two groups so that each group has an equal number of students: one group has students with "
                  "height less than a particular height and the other group has students with heights greater than the "
                  "particular height. Suggest a way to do this. Can you guess the age of these students based on the "
                  "tabular data in the 'Telling Tall Tales' section?",
                  ["Sorted: 101, 102, 106, 109, 110, 110, 112, 115, 115, 115, 115, 115, 117, 120, 120, 123, 125.",
                   "The median is the 9th value, 115 cm: 8 students are on each side of it.",
                   "But 5 students are exactly 115 cm: 7 are below 115 and 5 above.",
                   "So split at the median: the 8 shortest in one group, the 8 tallest in the other, and the middle "
                   "student at 115 is left aside or helps; measure the 115 cm students more finely to place them.",
                   "Mean: 1930 ÷ 17 ≈ 113.53 cm, close to 2019 averages for age 6 (113.1 and 112.9).",
                   "So the students are likely about 6 to 7 years old."],
                  "Split at the median, 115 cm, taking care with the 5 students at 115 cm; mean ≈ 113.53 cm suggests "
                  "they are about 6 to 7 years old"),
              FIO("5.4.end6", "Figure it Out (chapter questions), Q6",
                  "Describe the mean and median of heights of your class. You can visualise the heights on a dot "
                  "plot.",
                  ["Sample data for 10 students (cm): 138, 142, 145, 147, 150, 151, 151, 153, 156, 160.",
                   "Total 1493, mean 1493 ÷ 10 = 149.3 cm.",
                   "Ten values, so the median is (150 + 151) ÷ 2 = 150.5 cm.",
                   "Range 160 − 138 = 22 cm; on a dot plot from 135 to 160 most dots sit from 145 to 156.",
                   "With your own class: measure everyone, sort, then find the mean, median and range and draw the "
                   "dot plot."],
                  "For the sample data: mean 149.3 cm, median 150.5 cm, range 22 cm; use the same steps for your own "
                  "class"),
              FIO("5.4.end7", "Figure it Out (chapter questions), Q7",
                  "There are two 7th grade sections at a school. Each section has 15 boys and 15 girls. In one section, "
                  "the mean height of students is 154.2 cm. From this information, what must be true about the mean "
                  "height of students in the other section? (a) The mean height of students in the other section is "
                  "154.2 cm. (b) The mean height of students in the other section is less than 154.2 cm. (c) The mean "
                  "height of students in the other section is more than 154.2 cm. (d) The mean height of students in "
                  "the other section cannot be determined.",
                  ["The mean of one section depends only on that section's heights.",
                   "Having the same numbers of boys and girls does not make the heights the same.",
                   "The two Grade 5 sections earlier had different means (144.5 and 141.21).",
                   "So nothing must be true about the other section's mean."],
                  "(d) It cannot be determined"),
              FIO("5.4.end8", "Figure it Out (chapter questions), Q8",
                  "Standing tall in the storm. (a) Write estimated values for the number of skyscrapers in New York, "
                  "Tokyo, and London. (b) Are the following statements valid? (i) Only 12 cities have more skyscrapers "
                  "than Mumbai. (ii) Only 7 cities have fewer skyscrapers than Mumbai. (iii) The tallest building in "
                  "the world is in Hong Kong.",
                  ["(a) Reading the bars (estimates): New York about 315 (accept 300 to 330), Tokyo about 165 (accept 155 to 180, between Kuala Lumpur 154 and Shanghai 183), London about 28 (accept 20 to 35, below Moscow 46).",
                   "(b)(i) Counting the bars longer than Mumbai's (about 86) gives 12 cities: valid.",
                   "(ii) Counting the bars shorter than Mumbai's gives 7 cities: valid.",
                   "(iii) The chart counts buildings, not their heights, so it cannot tell where the tallest building "
                   "is: not valid from this data."],
                  "(a) estimates about 315 (300 to 330), 165 (155 to 180) and 28 (20 to 35) (b) (i) valid (ii) valid (iii) cannot be judged from the chart",
                  tool="baseline"),
              FIO("5.4.end9", "Figure it Out (chapter questions), Q9",
                  "Estimate and then measure the objects listed in the following table: length of a pen, length of an "
                  "eraser, length of your palm, length of your geometry box, length of your math notebook. Draw a "
                  "double bar graph based on the data. How accurate were your estimates? Find the average difference "
                  "between the estimated and measured values.",
                  ["Sample data (cm), estimate then measure: pen 14 and 15, eraser 5 and 4.5, palm 16 and 17.5, "
                   "geometry box 18 and 16, notebook 25 and 27.",
                   "Positive differences: 1, 0.5, 1.5, 2 and 2.",
                   "Average difference: 7 ÷ 5 = 1.4 cm.",
                   "Draw an estimate bar and a measure bar for each object, scale 1 unit = 5 cm.",
                   "With your own objects: estimate first, measure, take each positive difference, then find their "
                   "mean."],
                  "For the sample data the average difference is 1.4 cm; repeat with your own estimates"),
              FIO("5.4.end10", "Figure it Out (chapter questions), Q10",
                  "Aditi likes solving puzzles. She recently started attempting the 'Easy' level Sudoku puzzles. The "
                  "time she took (in seconds) to solve these puzzles are: 410, 400, 370, 340, 360, 400, 320, 330, 310, "
                  "320, 290, 380, 280, 270, 230, 220, 240. The first nine values correspond to Week 1 and the rest to "
                  "Week 2. (a) Construct a dot plot below showing the data for both weeks. (b) Describe the mean, "
                  "median, and any observations you may have about the data.",
                  ["(a) Use a line from 200 to 420 in steps of 20; one colour for each week.",
                   "Week 1 (9): total 3240, mean 3240 ÷ 9 = 360 seconds; sorted, the 5th value gives median 360; "
                   "range 410 − 310 = 100.",
                   "Week 2 (8): total 2230, mean 2230 ÷ 8 = 278.75 seconds; median (270 + 280) ÷ 2 = 275; range "
                   "380 − 220 = 160.",
                   "(b) She got faster in Week 2 by about 80 seconds on average; the 380 in Week 2 is far from the "
                   "rest."],
                  "Week 1: mean 360 s, median 360 s; Week 2: mean 278.75 s, median 275 s; she became faster"),
              FIO("5.4.end11", "Figure it Out (chapter questions), Q11",
                  "Individual Project: Pick at least one of the following: (a) How Long is a Sentence? Pick any two "
                  "school books from different subjects. Choose any page with a lot of text from each book. (i) Use a dot "
                  "plot to describe how many words the sentences have on each page. (ii) Compare the data of both the "
                  "pages using mean and median. (b) What is in a Name? Write down the names of all of your classmates. "
                  "(i) Find the mean and median name length (number of letters in a name). (ii) Visualise the data and "
                  "describe its variability and central tendency. (iii) Which starting letters are more popular? Which "
                  "are less popular? (iv) What is the median starting letter? What does this say about the number of "
                  "names starting with the letters A to M and N to Z? (v) Plot a double-bar graph showing the number of "
                  "boys' names and girls' names that: start and end with vowels, start with vowels and end with "
                  "consonants, start with consonants and end with vowels, start and end with consonants.",
                  ["(a) Sample: page A sentence lengths 12, 8, 15, 20, 9, 14, 11, 7; page B: 18, 22, 25, 14, 30, 19.",
                   "Page A: total 96, mean 96 ÷ 8 = 12 words; sorted 7, 8, 9, 11, 12, 14, 15, 20, median "
                   "(11 + 12) ÷ 2 = 11.5.",
                   "Page B: total 128, mean 128 ÷ 6 ≈ 21.33 words; sorted 14, 18, 19, 22, 25, 30, median "
                   "(19 + 22) ÷ 2 = 20.5.",
                   "The second page has longer and more varied sentences.",
                   "(b) For names, count the letters in each name, then find the mean, median and a dot plot the same "
                   "way; sort starting letters alphabetically to find the median letter.",
                   "With your own pages or names: collect, sort, compute, plot and compare."],
                  "For the sample pages: page A mean 12, median 11.5; page B mean ≈ 21.33, median 20.5; use the same "
                  "steps on your own data"),
              FIO("5.4.end12", "Figure it Out (chapter questions), Q12",
                  "Individual project (long term): This requires collecting data over 2 weeks or more. In and Out: "
                  "Track how many times you step out of your house in a day. Do this for a month. (i) Describe the "
                  "variability and central tendency of this data. Make a dot plot. (ii) Do you find anything "
                  "interesting about this data? Share your observations. (iii) You can ask any of your family members "
                  "or friends to do this as well.",
                  ["Sample data for 10 days: 3, 2, 4, 1, 0, 5, 3, 2, 6, 4.",
                   "Total 30, mean 30 ÷ 10 = 3 times a day.",
                   "Sorted 0, 1, 2, 2, 3, 3, 4, 4, 5, 6, median (3 + 3) ÷ 2 = 3.",
                   "Range 6 − 0 = 6; a day at home counts as 0, a real value.",
                   "With your own month: record every day, then sort, compute and plot; look for patterns such as "
                   "weekends."],
                  "For the sample: mean 3, median 3, range 6; record your own month and use the same steps"),
              FIO("5.4.end13", "Figure it Out (chapter questions), Q13",
                  "Small-group project: Pick at least one of the following. Make groups of 8 to 10. Collect data "
                  "individually as needed. Put together everyone's data and do the appropriate analysis and "
                  "visualisation. (a) Our heights vs. our family's heights: Collect the heights of your family members. "
                  "(i) Make a dot plot showing heights of just your family members. Describe its variability and "
                  "central tendency. (ii) Make a double-bar graph showing each student's height next to their family's "
                  "mean height. (iii) Look at everyone's data and share your observations. (b) Estimating time: Check "
                  "the time and close your eyes. Open them when you think 1 minute has passed (no counting). Note down "
                  "after how many seconds you opened your eyes. Collect this data for yourself and for your family "
                  "members. Repeat this activity to estimate 3 minutes. (i) Make two dot plots (for 1 minute and 3 "
                  "minutes) showing estimates of just your family members. (ii) Mark these on the respective dot plots. "
                  "Describe its variability and central tendency. (iii) Make a double bar graph showing each family's "
                  "mean 1 minute estimate and mean 3 minute estimate. (iv) Look at everyone's data and share your "
                  "observations.",
                  ["(a) Sample family: 172, 160, 148 and 135 cm. Total 615, mean 615 ÷ 4 = 153.75 cm, median "
                   "(148 + 160) ÷ 2 = 154 cm, range 172 − 135 = 37 cm.",
                   "A student of 148 cm stands next to a family mean of 153.75 cm on the double bar graph.",
                   "(b) Sample 1 minute estimates: 52, 61, 48, 66 seconds, mean 227 ÷ 4 = 56.75 seconds.",
                   "Sample 3 minute estimates: 150, 195, 170, 210 seconds, mean 725 ÷ 4 = 181.25 seconds.",
                   "With your group: pool everyone's data, make the dot plots and bar graphs, and compare families."],
                  "For the samples: family mean 153.75 cm, median 154 cm; mean estimates 56.75 s for 1 minute and "
                  "181.25 s for 3 minutes; repeat with your group's data")],
          ncert=[], misconceptions=["M_ZERO_BLANK", "M_BASELINE", "M_AVERAGE_ALL"])]))

# ============================== T14 Lock puzzle ==============================================================
TOPICS.append(TOPIC(
    "T14", "M5", "Puzzle Time: Connect the Dots", ["Puzzle Time"], "Analyze",
    "Students combine five clues about a three-digit number lock, ruling digits in and out, to find the one code that "
    "fits every clue.",
    "Connect the clues: rule digits out, then place the ones that remain.",
    [A("T14.C1", "Crack the number lock", "Analyze", "",
       textbook=["Connect the Dots…",
                 "A number lock has a 3-digit code. Find the code using the hints below.",
                 "2 6 5: One digit is correct and well placed.",
                 "2 7 1: One digit is correct but wrongly placed.",
                 "0 3 6: Nothing is correct.",
                 "0 6 4: One digit is correct but wrongly placed.",
                 "5 4 2: Two digits are correct but wrongly placed."],
       teach=["Start with the clue that says nothing is correct: it rules out three digits at once.",
              "Then use each remaining clue to fix a digit or a position.",
              "Check the final code against every clue."],
       examples=[
           WE("Find the 3-digit code from the five clues: 265 one right and in place; 271 one right but misplaced; 036 "
              "nothing right; 064 one right but misplaced; 542 two right but misplaced.",
              ["036 rules out 0, 3 and 6.",
               "064 then has only 4 left, so 4 is in the code but not in the last place.",
               "542 says 4 is not in the middle place either, so 4 is first.",
               "265 has one digit in place; 2 cannot be first, so 5 is correct in the last place.",
               "542 has two correct digits, 5 and 4, so 2 is out.",
               "271 then needs 7 or 1 in a new place; only the middle is free, and 7 is already in the middle there, so "
               "1 goes in the middle.",
               "The code is 415; check: it fits all five clues."],
              "The code is 415",
              ncert=["puzzle.lock"])],
       key_terms=["clue"], enrichment=True, minutes=6),
     DOER("T14.C2", "Practice: check the code against every clue", None, "Analyze", "",
          ["A clue with nothing correct removes digits.",
           "Correct but wrongly placed rules out a position.",
           "Check the final code against every clue."],
          enrichment=True)]))

# ============================== T15 Summary ==================================================================
TOPICS.append(TOPIC(
    "T15", "M5", "Summary: Connecting the Dots", ["Summary"], "Remember",
    None,
    "Statistical questions, mean and median, dot plots, outliers, zeros and blanks, clustered bar graphs and testing "
    "claims, in one place.",
    [A("T15.C1", "What the data told us", "Remember",
       "Students restate how dot plots show the minimum, maximum, range and clusters, how the mean and median describe "
       "the centre of data, and how clustered bar graphs compare categories and years.",
       textbook=["Summary",
                 "Dot plots help us get a quick glimpse of the variability of the data: minimum, maximum, range, and "
                 "how data is clustered or spread out.",
                 "The Arithmetic Mean = Sum of all the values in the data ÷ Number of values in the data.",
                 "The Median is the number in the middle of any sorted data. If there are an even number of values, "
                 "then the median is the average of the two middle numbers.",
                 "We can describe and compare data in several ways including by referring to the minimum, maximum, "
                 "total, range, arithmetic mean, and median.",
                 "We learnt how to read and make clustered bar graphs. These graphs can be used to compare and "
                 "visualise values across categories and across time.",
                 "Examining data can lead to new questions and directions to probe further."],
       teach=["Our opening guess is settled: two friends' heights cannot tell how tall people in a place are; we need "
              "many heights, a dot plot, and the mean and median.",
              "Mean: share the total equally. Median: the middle of the sorted values. Outliers move the mean.",
              "Still open for you: collect your class's heights and say which number describes them best, and why."],
       ncert=["summary"], video_focus=["RECAP"], minutes=8)],
    topic_type="summary"))
