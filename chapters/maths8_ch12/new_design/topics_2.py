# -*- coding: utf-8 -*-
"""Topics T6 to T10 (module M2: visualising and interpreting data). Book section 5.2, pp 116 to 132.
Every value read off a graph is approximate and worded that way."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T6 Line graphs: Kerala and Punjab ===========================================
TOPICS.append(TOPIC(
    "T6", "M2", "Line Graphs: Temperature in Two States", ["5.2"], "Apply",
    "Students recognise that a line graph shows change over time, read what is given in a line graph before "
    "saying what it means, summarise the trends of two series, and plot a line graph from a table.",
    "A line graph joins points taken over time; first read the axes, scale and marks, then say what the lines show.",
    [A("T6.C1", "From clustered columns to a line graph", "Understand",
       "Students compare a clustered column graph and a line graph of the same monthly temperatures and explain "
       "why a line graph suits data across time.",
       textbook=["5.2 Visualising and Interpreting Data",
                 "So far we have learnt how to read and make pictographs, bar graphs, clustered-bar graphs, and dot "
                 "plots. We now examine some more ways of visualising data.",
                 "The following figure is a clustered-column graph that shows the monthly maximum temperature in "
                 "Kerala and Punjab in 2023. Now, observe the following graph. Do both these graphs represent the "
                 "same information?",
                 "We call such a graph made up of lines a line graph. Line graphs are generally used to visualise "
                 "data across time.",
                 "How do we get the maximum temperature over a month in a state? There could be a few weather "
                 "stations across the state that regularly track the local temperature. We can get the monthly "
                 "maximum temperature by looking at the maximum value among all the values recorded across the state."],
       teach=["Predict first: a clustered column graph and a line graph both show the 2023 monthly highest "
              "temperatures of Kerala and Punjab. Do they hold the same information?",
              "Yes. Each month's point sits at the top of the matching column, and the lines join those points in "
              "order of the months.",
              "A line graph is made for data across time, because the joining line shows how the value goes up, "
              "down or stays flat from one month to the next.",
              "A state's monthly maximum is the largest value recorded across its weather stations that month."],
       examples=[
           WE("Kerala's April column reaches about 33 degrees and its July column about 29 degrees. Where do these "
              "two months sit on the line graph, and what does the line between them show?",
              ["Each month's point sits at the top of its column: April at about 33, July at about 29.",
               "The line joins the points in month order, so from April to July it slopes down.",
               "The drop is about 33 − 29 = 4 degrees."],
              "April's point is at about 33 and July's at about 29; the line slopes down by about 4 degrees")],
       ncert=["5.2.intro", "5.2.temp_compare"], key_terms=["line graph", "time"], misconceptions=["M_AXIS"],
       minutes=8),
     A("T6.C2", "Two steps: what is given, then what it says", "Analyze",
       "Students read a line graph in two steps, naming the axes, the scale and the marks first, then writing "
       "summary statements about the trend of each line.",
       textbook=["To identify and interpret the information presented, let us follow a two-step process.",
                 "Step 1: Identify what is given. Notice how the graph is organised, what scale is used, and what "
                 "patterns the data shows. The data for each month for a city is marked and connected by lines to "
                 "show the change over time. Kerala's data is shown using blue circle marks connected by blue lines "
                 "and Punjab's data is shown in red. The horizontal line shows the months of the year. The vertical "
                 "line shows the temperature in degrees Celsius.",
                 "The different shape markers help in easily distinguishing if the graph is printed in greyscale, or "
                 "for people who find it difficult to distinguish colour.",
                 "Step 2: Infer and interpret from what is given. In Punjab, the monthly maximum temperature "
                 "increases from January to June, reaching a high of 38 degrees. Then, it reduces to just under 35 "
                 "degrees in July, stays mostly flat till September, and then falls continuously till December, "
                 "reaching about 23 degrees. January has the lowest, about 19 degrees.",
                 "Kerala's trend is different: it stays mostly flat throughout the year. The peak is around 33 "
                 "degrees in April and the lowest point is around 29 degrees in July. In short, the temperature in "
                 "Punjab varies more, reaching colder and warmer temperatures than in Kerala."],
       teach=["Predict first: which state would you expect to have a flat line over the year, the one near the sea "
              "in the south or the one in the north? Say why before you look.",
              "Step one, what is given: months run along the bottom, temperature in degrees Celsius runs up the side, "
              "blue circles for Kerala, red for Punjab.",
              "Step two, what it says: Punjab climbs from about 19 degrees in January to 38 degrees in June, dips just "
              "under 35 in July and falls to about 23 degrees by December. Kerala stays between about 29 and 33.",
              "Punjab varies more than Kerala. Each such finding is a statement the graph supports."],
       examples=[
           WE("Read Punjab's line: what is the rise from its lowest month to its highest month?",
              ["Punjab's lowest monthly maximum is about 19 degrees, in January.",
               "Its highest is about 38 degrees, in June.", "The rise is 38 − 19 = 19 degrees."],
              "About 19 degrees, much more than Kerala's rise of about 33 − 29 = 4 degrees",
              ncert=["5.2.temp_step1", "5.2.temp_step2"])],
       key_terms=["scale", "trend", "interpret"], misconceptions=["M_AXIS"], minutes=10),
     A("T6.C3", "Questions a graph raises", "Evaluate",
       "Students pose follow up questions from a graph, such as why trends differ, which other states look "
       "similar, and what monthly minimum temperatures would show.",
       textbook=["This can trigger questions in different directions, some of which can be answered using data. "
                 "Here are some directions to think about:",
                 "Why are the trends so distinct in these two states? What factors determine a region's temperature?",
                 "You might be curious to look at the trends of a few other states. Are there other types of trends "
                 "that states exhibit?",
                 "Which states show trends similar to Punjab's? Is there anything common between these states?",
                 "What would a plot of the monthly minimum temperatures for these states look like? What thoughts or "
                 "questions occur to you?",
                 "When we try to understand how the data is collected or produced, we gain a clearer idea of its "
                 "scope. It also helps us identify any limitations, such as bias or missing information."],
       teach=["Predict first: if you drew the monthly lowest temperatures for the same two states, would the "
              "pattern look like the highest ones?",
              "A graph answers some questions and raises many more. Which could be answered with more data, and which "
              "need a reason, such as distance from the sea?",
              "Knowing how the data was collected tells us how far to trust it."],
       examples=[
           WE("Punjab's line rises about 19 degrees in a year and Kerala's only about 4. Write one question more data "
              "could answer and one that needs a reason.",
              ["The gap in the rise is about 19 − 4 = 15 degrees.",
               "A data question: which other states rise by more than 15 degrees in a year?",
               "A reason question: why does the sea near Kerala keep its temperature so steady?"],
              "One data question, such as other states' rises, and one reason question, such as the effect of the sea")],
       ncert=["5.2.temp_questions"], key_terms=["question", "limitation"], enrichment=True, minutes=6),
     DOER("T6.C4", "Practice: plot it as a line graph", "line_graph_builder", "Apply",
          "Students enter or drag points from a table onto a labelled grid, join them in order, pick a scale that "
          "fits the values, and describe the shape of each line.",
          ["Label the axes, pick the scale, plot each point, join in order.",
           "Two lines on one grid need different marks or colours and a key."],
          items=[
              FIO("FiO2.q1", "Figure it Out (visualising data, question 1)",
                  "The average number of customers visiting a shop and actually purchasing items over the week is "
                  "given: Mon to Sun visiting 16, 19, 10, 14, 20, 22, 35 and purchasing 10, 8, 7, 11, 12, 16, 26. "
                  "Visualise this data on a line graph.",
                  ["Put the days Mon to Sun along the bottom and the number of customers up the side from 0 to 40 in "
                   "steps of 5.",
                   "Plot visiting: (Mon, 16), (Tue, 19), (Wed, 10), (Thu, 14), (Fri, 20), (Sat, 22), (Sun, 35) and join them.",
                   "Plot purchasing: (Mon, 10), (Tue, 8), (Wed, 7), (Thu, 11), (Fri, 12), (Sat, 16), (Sun, 26) with a "
                   "different mark and join them.",
                   "Both lines rise towards the weekend, and the purchasing line stays below the visiting line every day."],
                  "Two lines on one grid; both peak on Sunday, purchasing stays below visiting"),
              FIO("FiO3.q9", "Figure it Out (more on mean and median, question 9)",
                  "A table gives the retail price in rupees of iodised salt in January over 10 years, 2016 to 2025, "
                  "for Andaman and Nicobar Islands, Assam, Gujarat, Mizoram, Uttar Pradesh and West Bengal. (i) Show "
                  "any 3 states as a line graph with a suitable scale. (ii) What do you find interesting? "
                  "(iii) Compare the price variation in Gujarat and Uttar Pradesh. (iv) In which state did the "
                  "price rise the most from 2016 to 2025? (v) What are you curious to explore further?",
                  ["(i) Years 2016 to 2025 along the bottom; prices from 0 to 30 rupees up the side in steps of 5, "
                   "with one line per state.",
                   "(iii) Gujarat stays near 14 to 15 rupees for most years and jumps to 19.2 only in 2025. Uttar "
                   "Pradesh climbs steadily from 16.15 to 26.9 and then dips to 24.81, so it varies much more.",
                   "(iv) Rise from 2016 to 2025: Andaman and Nicobar Islands 20.99 − 16 = 4.99, Assam 12.35 − 6 = 6.35, "
                   "Gujarat 19.2 − 16.5 = 2.7, Mizoram 29.8 − 20 = 9.8, Uttar Pradesh 24.81 − 16.15 = 8.66, West "
                   "Bengal 23.99 − 9.47 = 14.52. The biggest rise is in West Bengal.",
                   "(ii) and (v) are open: for example, why West Bengal's price rose from 9.47 to 23.99, and whether "
                   "the same happens with other food items."],
                  "West Bengal rose the most, by about 14.52 rupees; Gujarat varied less than Uttar Pradesh")])],
    key_terms=["line graph", "scale", "trend"]))

# ============================== T7 Reading line graphs: space objects =======================================
TOPICS.append(TOPIC(
    "T7", "M2", "Reading Line Graphs: Objects in Space", ["5.2"], "Analyze",
    "Students read a multi series line graph with the two step method, judge which inferences are valid, compare "
    "steepness to compare change, find a doubling, and explain why a line graph beats a crowded column graph.",
    "Steeper means faster change, lines of countries need not add to the world line, and an inference is valid only "
    "if the graph supports it.",
    [A("T7.C1", "Step 1 and 2 on a busy graph", "Analyze",
       "Students identify the given axes, scale and series on a graph of objects launched into space, and write "
       "valid summary statements, noting what is not shown.",
       textbook=["Space Jam: A Traffic Problem in the Future? Take a look at the line graph showing the annual "
                 "number of objects launched into space. What could be the possible method used to derive this data? "
                 "Discuss.",
                 "Step 1: Identify what is given. Notice how the graph is organised, what scale is used, and what "
                 "patterns the data shows.",
                 "Step 2: Infer from and interpret what is given. In 2024, the worldwide count is around 2800, "
                 "whereas in 2023, it was around 2900. We can say that 2023 saw the highest number of objects "
                 "launched into space worldwide, assuming the trend before 2012 was decreasing.",
                 "The counts of the three countries don't add up to the worldwide count. Therefore, we can infer "
                 "that the counts of other countries are not shown in this visualisation."],
       teach=["Predict first: the graph has lines for the World, the United States, China and Russia. If you add the "
              "three countries, do you get the World line?",
              "Step one: years 2012 to 2024 along the bottom, number of objects up the side to 3000. Four lines.",
              "Step two: the World line peaks in 2023 near 2900 and is a little lower in 2024, near 2850. The "
              "countries add up to much less than the World line, so other countries launch objects that are not shown."],
       examples=[
           WE("In 2024 the World line is about 2850, the United States about 2250, China about 280 and Russia about "
              "120. Do the three countries make up the World count?",
              ["Add the three countries: 2250 + 280 + 120 = 2650.",
               "Compare with the World: 2850 − 2650 = 200.",
               "About 200 objects came from countries the graph does not show."],
              "No; about 200 objects come from other countries that are not shown")],
       ncert=["5.2.space_method", "5.2.space_steps"], key_terms=["world", "series", "infer"],
       misconceptions=["M_LINE_COUNTRIES"], minutes=10),
     A("T7.C2", "Steeper means a bigger change", "Analyze",
       "Students compare changes between years by the steepness of line segments, judge whether given statements "
       "are valid inferences, and find two consecutive years where the count doubled.",
       textbook=["For the USA, the increase from 2022 to 2023 is more than from 2023 to 2024. We can say this by "
                 "looking at how steep the line segments are: the steeper the line is, the greater the increase.",
                 "Which of the following statements are valid inferences? From 2012 till 2024, the worldwide count of "
                 "space object launches increased every year. USA is a major contributor in the years 2022 to 24, "
                 "launching about three fourths of the worldwide count. Nepal did not launch any object in the "
                 "period 2012 to 24. The combined count of object launches by China and Russia in 2024 is about 400.",
                 "Identify two consecutive years where the worldwide count increased by 2 times or more."],
       teach=["Predict first: between which two years is the United States line steeper, 2022 to 2023 or 2023 to 2024?",
              "2022 to 2023 rises from about 1950 to 2230, which is about 280. 2023 to 2024 rises only about 30, so it is "
              "less steep.",
              "Test each claim against the graph: the World line fell in 2018 and in 2024, so it did not rise every "
              "year. The United States is about 2250 of 2850, close to three fourths. Nepal is simply not shown. "
              "China about 290 plus Russia about 120 is about 400.",
              "A doubling: 2016 to 2017 goes from about 230 to 480, and 2019 to 2020 goes from about 600 to 1270."],
       examples=[
           WE("Use the World line to find two consecutive years where the count at least doubled.",
              ["In 2016 the World count is about 230 and in 2017 about 480.", "480 ÷ 230 ≈ 2.1, so it doubled.",
               "In 2019 it is about 600 and in 2020 about 1270.", "1270 ÷ 600 ≈ 2.1, so it doubled again."],
              "2016 to 2017 and 2019 to 2020", ncert=["5.2.space_double"])],
       key_terms=["steepness", "valid inference", "double"], misconceptions=["M_LINE_CAUSE"], minutes=10),
     A("T7.C3", "Why a line graph here", "Evaluate",
       "Students count how many bars a clustered column graph of the same data would need and explain why the line "
       "graph is clearer for changes over time.",
       textbook=["Imagine the same data being shown as a clustered column graph. There would be 13 clusters, one for "
                 "each year, and within each cluster, 4 columns, making a total of 52 bars! Such a graph would look "
                 "crowded and difficult to read, making it hard to interpret the trends clearly.",
                 "A line graph, on the other hand, is better suited for illustrating changes over time. By "
                 "connecting data points with line segments, it provides a clear visual representation of trends and "
                 "variations, allowing the reader to easily track how a parameter evolves across different years."],
       teach=["Predict first: 13 years and 4 series as columns. How many bars is that?",
              "13 × 4 = 52 bars, crowded and hard to follow.",
              "Four lines show the same story lightly, and the eye follows the trend from year to year."],
       examples=[
           WE("How many bars would a clustered column graph of the space data need?",
              ["The years 2012 to 2024 make 13 clusters.", "Each cluster has 4 columns.", "13 × 4 = 52."],
              "52 bars", ncert=["5.2.space_why_line", "5.2.space_valid"])],
       key_terms=["clustered column", "trend"], minutes=6),
     DOER("T7.C4", "Practice: ask the graph questions", "graph_interpreter", "Analyze",
          "Students read values at marked points on several line graphs, compare steepness, test statements as valid "
          "or not valid, and write one summary statement for each graph.",
          ["Read the axes and scale first, then the shape.",
           "A statement is valid only if the graph supports it, and a missing series says nothing."],
          items=[
              FIO("FiO2.q3", "Figure it Out (visualising data, question 2 of the second set)",
                  "A line graph shows the number of births in every month in India over a time period. (i) What are "
                  "your observations? (ii) About how many births in July 2017? (iii) What time period does the graph "
                  "capture? (iv) Compare the births in January of 2018, 2019 and 2020. (v) Estimate the births in "
                  "the year 2019.",
                  ["(i) Observe the shape: a jagged line with a repeating rise and fall each year, and one sharp "
                   "fall in a particular stretch. Say each observation in a sentence, such as: the line is highest "
                   "in the middle months.",
                   "(ii) Find July 2017 on the bottom axis, go up to the line and read across to the side scale. "
                   "Give the value as about a number, not exact.",
                   "(iii) Read the first and last months labelled on the bottom axis.",
                   "(iv) Read the three January points and compare their heights.",
                   "(v) Read the 12 monthly values for 2019 and add them, or use the typical month times 12."],
                  "Answers are read off the graph and given as approximate values"),
              FIO("FiO3.q10", "Figure it Out (more on mean and median, question 10)",
                  "Referring to the graph of the primary source of lighting in rural and urban homes, which "
                  "statements are valid and why? (i) In 1983 most rural homes used kerosene and most urban homes "
                  "electricity. (ii) Kerosene use has decreased over time in both rural and urban areas. (iii) In "
                  "the year 2000, 10% of urban households used electricity. (iv) In 2023 there were no power cuts.",
                  ["Read the two lines for kerosene and two for electricity, for rural and urban, in each year.",
                   "(i) Valid if the rural kerosene line is above half in 1983 and the urban electricity line is "
                   "above half.",
                   "(ii) Valid if both kerosene lines slope down over the years.",
                   "(iii) Check the urban electricity line at 2000. It is far higher than 10%, so this is not valid.",
                   "(iv) The graph shows the main source of lighting, not power cuts, so it cannot support this."],
                  "Check (i) and (ii) against the lines; (iii) is not valid; (iv) is not supported by the graph"),
              FIO("FiO3.q11", "Figure it Out (more on mean and median, question 11)",
                  "A line graph shows the average daily time rural and urban kids spend on hobbies and games by age. "
                  "(i) How long do children aged 10 in urban areas spend each day? (ii) At what age do rural kids "
                  "spend 1.5 hours? Choose from 8, 10, 12, 14 and 18 years. (iii) Are these correct? (a) The "
                  "average time at age 15 is twice that at age 10. (b) All rural kids aged 15 spend at least 1 "
                  "hour a day.",
                  ["(i) Find age 10 on the bottom axis, go up to the urban line and read across.",
                   "(ii) Find 1.5 hours on the side scale, go across to the rural line and read the age below it.",
                   "(iii) (a) Divide the age 15 value by the age 10 value and see if it is about 2. (b) The graph "
                   "gives an average, so it says nothing about every child: not correct."],
                  "Read from the graph; (b) cannot be concluded because it is an average")])],
    key_terms=["line graph", "steepness", "inference"]))

# ============================== T8 Catch the pattern in rain ================================================
TOPICS.append(TOPIC(
    "T8", "M2", "Catch the Pattern in Rain", ["5.2"], "Analyze",
    "Students explain how monthly average rainfall is compiled, place six cities on a map of India, identify peak "
    "and low months from the lines, link them to the coast and the monsoon, and read similar yearly patterns in "
    "other data.",
    "A monthly average is taken over many years; west coast cities peak in June to August, Rameswaram and Chennai in "
    "October to December, and January to March is dry for all six.",
    [A("T8.C1", "How the monthly average rainfall is made", "Understand",
       "Students describe how rainfall collected over several years in a city is averaged for each month, and "
       "say what the value for June stands for.",
       textbook=["Catch the (Pattern in) Rain. The following graphs show monthly average rainfall data of a few cities.",
                 "What could be the possible method to compile this data?",
                 "This data shows the monthly average rainfall in 6 cities. This means rainfall data is collected over "
                 "a few years in every city. The total rainfall in a month, say June, across years is averaged to get "
                 "the monthly average rainfall in June in a city."],
       teach=["Predict first: how would you get one number for June in Udupi when every year's June is different?",
              "Collect the June rainfall of several years. Add them and divide by the number of years.",
              "Do the same for every month. The line is then the typical year, not any one real year."],
       examples=[
           WE("Suppose a town's June rainfall over 4 years was 820, 900, 760 and 920 millimetres. What is its "
              "monthly average rainfall for June?",
              ["Add the four Junes: 820 + 900 + 760 + 920 = 3400.",
               "Divide by the number of years: 3400 ÷ 4 = 850."],
              "850 millimetres, the typical June, not any one real June")],
       ncert=["5.2.rain_method"], key_terms=["monthly average", "rainfall"], minutes=6),
     A("T8.C2", "Peaks, dry months and the coasts", "Analyze",
       "Students mark the six cities on a map, find each city's peak and low months, and relate rainfall timing to "
       "the west and the east coast.",
       textbook=["Mark these cities on a map of India. What is common to how they are grouped in the graphs? Share "
                 "your observations and inferences about the graphs.",
                 "Kovalam, Udupi, and Mumbai are along the west coast. Rameswaram, Chennai, and Puri are along the "
                 "east coast. It appears that regions along the west coast receive more rain.",
                 "Identify the peak months and low months of rainfall for each city.",
                 "Udupi, Mumbai, and Kovalam have peak rainfall during June to August. Rameswaram gets most of its rain "
                 "during October to December. Chennai starts getting rain from June onwards, which peaks in "
                 "November, and continues till December. Puri, although on the east coast, gets its peak rainfall "
                 "during July to September. January to March are dry months for all the cities. Rameswaram receives "
                 "very little rain from January to September."],
       teach=["Predict first: on a map of India, which coast would you expect to be wetter in June to August, west "
              "or east?",
              "Three graphs group the west coast cities, Kovalam, Udupi and Mumbai. Their peaks are in June to "
              "August, with Udupi the highest, near 880 millimetres in July.",
              "The east coast group peaks later, Rameswaram and Chennai in October to December, but Puri peaks in "
              "July to September. January to March is dry for all six cities.",
              "So the coast alone does not decide the month; the winds do, which brings the monsoons."],
       examples=[
           WE("Name the peak months for Udupi, Rameswaram and Puri and say whether each is on the west or east coast.",
              ["Udupi is on the west coast, with a peak in June to August.",
               "Rameswaram is on the east coast, with a peak in October to December.",
               "Puri is on the east coast, with a peak in July to September."],
              "Udupi June to August (west); Rameswaram October to December (east); Puri July to September (east)",
              ncert=["5.2.rain_map", "5.2.rain_peaks"])],
       key_terms=["peak", "coast", "dry months"], misconceptions=["M_COAST"], minutes=10),
     A("T8.C3", "Two monsoons", "Remember",
       "Students find out which regions the south west and north east monsoons bring rain to and when, and connect "
       "it to the rain peaks seen in the graphs.",
       textbook=["Read about the south-west monsoon and north-east monsoon and which regions come under the "
                 "influence of these and when."],
       teach=["Predict first: why might Rameswaram and Chennai peak in November while Mumbai peaks in July?",
              "The south west monsoon brings rain to the west coast from June to September. The north east monsoon "
              "brings rain to the south east coast in October to December.",
              "Look up the regions each one reaches, then check them against the six graphs."],
       examples=[
           WE("Mumbai's rain peaks in July and Chennai's in November. Which monsoon brings each peak?",
              ["The south west monsoon reaches the west coast from June to September, which covers July.",
               "The north east monsoon reaches the south east coast in October to December, which covers November.",
               "So Mumbai's peak comes from the south west monsoon and Chennai's from the north east monsoon."],
              "Mumbai: south west monsoon; Chennai: north east monsoon")],
       ncert=["5.2.rain_monsoon"], key_terms=["monsoon"], enrichment=True, minutes=5),
     DOER("T8.C4", "Practice: compare cities on the map", "rain_map_compare", "Analyze",
          "Students place cities on a map of India, switch their rainfall lines on and off, mark peak and low "
          "months, and group the cities by when they get their rain.",
          ["Peak month is the highest point of the line; dry months are the lowest.",
           "Compare lines on the same scale before saying one city gets more."],
          items=[
              FIO("FiO2.q2", "Figure it Out (visualising data, question 2)",
                  "The average number of days of rainfall in each month is given for Mangaluru, New Delhi, Port Blair "
                  "and Rameswaram. (i) What could be the method? (ii) Mark Mangaluru, Port Blair and Rameswaram on "
                  "the graph. (iii) Fill in the New Delhi row from its line. (iv) Which city has the most rainy days "
                  "a year, and which the fewest? (v) When is the rainy season in New Delhi and Rameswaram?",
                  ["(i) Count the rainy days of each month over several years and average them.",
                   "(ii) Plot each month's number of days, rounded to the nearest whole number, and join the points.",
                   "(iii) Read New Delhi's line: about 1.3, 1.5, 1.5, 1.1, 1.5, 3.8, 9.7, 9.7, 4, 1, 0.3, 1 days.",
                   "(iv) Yearly rainy days: Mangaluru 0.1 + 0 + 0.1 + 1.8 + 6.2 + 24.1 + 27.7 + 24.5 + 14 + 8.8 + 3.9 + "
                   "0.9 = 112.1; Port Blair 125.8; Rameswaram 42.3; New Delhi about 36.",
                   "Port Blair has the most rainy days and New Delhi the fewest.",
                   "(v) New Delhi's rainy season is July and August, with about 10 days a month. Rameswaram's is "
                   "October to December, with 8 to 10 days a month."],
                  "Most: Port Blair; fewest: New Delhi (about 36 days); New Delhi July to August; Rameswaram October to December"),
              FIO("FiO3.q14", "Figure it Out (more on mean and median, question 14)",
                  "Graphs show sunrise and sunset times across the year at 4 locations in India. Which lines are "
                  "sunrise and which are sunset? (i) At which place does the sun rise earliest in January, and about "
                  "how long is the day there? (ii) Which place has the longest day over the year? (iii) What do "
                  "you find interesting?",
                  ["Sunrise is the lower line in the morning and sunset the upper line in the evening, since "
                   "sunrise is earlier in the day.",
                   "(i) Find the lowest sunrise value in January across the four places. Day length is sunset "
                   "minus sunrise, about 10 to 11 hours.",
                   "(ii) The place where the gap between the sunset and sunrise lines is widest over the year.",
                   "(iii) Each line repeats a smooth up and down pattern every year."],
                  "Read the values from the graph and give them as approximate"),
              FIO("FiO3.q15", "Figure it Out (more on mean and median, question 15)",
                  "A graph shows moonrise and moonset times over a month. (i) On what dates were amavasya (new moon) "
                  "and purnima (full moon)? (ii) What do you notice? What do you wonder?",
                  ["On new moon day the moon rises and sets about with the sun, so moonrise is in the morning and "
                   "moonset in the evening.",
                   "On full moon day the moon rises about when the sun sets, so moonrise is in the evening and moonset in the morning.",
                   "Look for those dates on the graph. Each moon time shifts about 50 minutes later every day.",
                   "(ii) is open: for example, why the moon is not in the sky at the same time every day."],
                  "Dates are read from the graph where moonrise is near sunrise (new moon) and near sunset (full moon)")])],
    key_terms=["rainfall", "peak", "coast"]))

# ============================== T9 Infographics =============================================================
TOPICS.append(TOPIC(
    "T9", "M2", "Infographics: Rice or Wheat?", ["5.2"], "Analyze",
    "Students read a colour coded map where each state shows the difference between rice and wheat eaten per "
    "person, find the states preferring each, name balanced states, estimate a hidden value from its neighbours, and "
    "ask questions the map raises.",
    "A value from minus 100 to plus 100 shows rice minus wheat preference: plus 100 means mostly rice, not only rice.",
    [A("T9.C1", "Reading the colour scale", "Understand",
       "Students read the colour scale that maps the difference between rice and wheat eating from minus 100 to "
       "plus 100, and explain what a value of plus 100 means.",
       textbook=["Infographics. In Grade 6, we saw an example of how infographics can be used to communicate "
                 "information and insights more clearly and quickly in a visually appealing way. Take a look at the "
                 "following infographic. Are you able to understand the information presented here?",
                 "This infographic compares the preference between rice and wheat in different states. The colour "
                 "scale at the top right indicates how to interpret the different shades in terms of preferences.",
                 "The difference between the per capita consumption of rice and wheat is mapped to values between "
                 "−100 and +100. A value of +100 doesn't mean that the state doesn't consume wheat at all. It means "
                 "that this state prefers mostly rice and the difference between per capita rice and wheat consumption "
                 "is the highest.",
                 "Isn't it interesting how there is a clear geographical split in preferences of rice vs. wheat "
                 "shown by the red line?"],
       teach=["Predict first: on a map of India, where would you expect people to prefer rice, and where wheat?",
              "Each state has one number between −100 and +100. A positive number means rice is preferred, a "
              "negative number means wheat is preferred, near zero means about equal.",
              "+100 does not mean no wheat is eaten. It means the gap between rice and wheat is the largest possible.",
              "The red line on the map splits the rice states from the wheat states."],
       examples=[
           WE("On the scale, Punjab is −78 and Bihar is close to 0. What does each value say about rice and wheat?",
              ["A negative value means wheat is preferred, so Punjab leans strongly to wheat.",
               "Punjab is 78 steps from 0, close to the wheat end at −100.",
               "A value near 0 means the two are eaten in about equal amounts, so Bihar is balanced."],
              "Punjab strongly prefers wheat; Bihar is about balanced")],
       ncert=["5.2.info_intro", "5.2.info_scale"], key_terms=["infographic", "scale", "preference"],
       misconceptions=["M_INFOG_100"], minutes=8),
     A("T9.C2", "Top states, balanced states, a hidden state", "Analyze",
       "Students list the five states most preferring rice and wheat, name some balanced states, and estimate the "
       "hidden value for Karnataka from the values of its neighbours.",
       textbook=["Share your observations. Based on this infographic, answer the following:",
                 "The value of Karnataka is hidden. Can you guess what it could be?",
                 "Which are the top 5 states where rice is the most popular?",
                 "Which are the top 5 states where wheat is the most popular?",
                 "List a few states where the preference between rice and wheat is more or less balanced."],
       teach=["Predict first: Karnataka's value is hidden. Its neighbours are Goa, Kerala, Tamil Nadu, Andhra "
              "Pradesh and Maharashtra. Before looking at the neighbours, would you guess rice or wheat?",
              "Top rice states read from the map are Manipur about +100, Nagaland +99, Mizoram +97, Tripura +96 and "
              "Meghalaya +95. Top wheat states are Rajasthan about −93, Haryana −81, Punjab −78, Madhya Pradesh −60 "
              "and Delhi −45.",
              "States near zero, such as Bihar, are balanced.",
              "Karnataka's neighbours Goa +57, Kerala +79, Tamil Nadu +85 and Andhra Pradesh +92 lean to rice, while "
              "Maharashtra is −15. A reasonable guess is a rice leaning value, roughly +60 to +80."],
       examples=[
           WE("Use the neighbours' values to guess Karnataka's value: Goa +57, Kerala +79, Tamil Nadu +85, Andhra "
              "Pradesh +92, Maharashtra −15.",
              ["Four of the five neighbours are strongly rice.",
               "Maharashtra is slightly towards wheat.",
               "The average of the five is (57 + 79 + 85 + 92 − 15) ÷ 5 = 298 ÷ 5 = 59.6.",
               "Karnataka is probably a little above or around this, so about +60 to +80."],
              "A rice leaning value of about +60 to +80, an estimate", ncert=["5.2.info_questions"])],
       key_terms=["top five", "balanced", "estimate"], minutes=10),
     A("T9.C3", "What does the map make you wonder?", "Evaluate",
       "Students pose questions the infographic raises, such as what the rice states have in common and whether "
       "preferences were the same 100 years ago.",
       textbook=["I wonder if there is anything common in all the states preferring rice or states preferring wheat.",
                 "I want to know if the preferences were similar even 100 years ago."],
       teach=["Predict first: what might the rice states share, such as rainfall or river water?",
              "A map shows a pattern; to explain it we need more data, such as rainfall or the crops that grow there.",
              "Write one question that the map raises and say what data would help answer it."],
       examples=[
           WE("Manipur is about +100 and Rajasthan about −93. How far apart are they on the scale, and what data "
              "could explain the gap?",
              ["The distance is 100 − (−93) = 193 steps on the scale.",
               "That is almost the whole scale of 200 steps.",
               "Rainfall data for the two states could help explain it, since rice needs much more water."],
              "193 steps apart; rainfall data could help explain the gap")],
       ncert=["5.2.info_wonder"], key_terms=["question", "pattern"], enrichment=True, minutes=5),
     DOER("T9.C4", "Practice: read the rice and wheat map", "infographic_map", "Analyze",
          "Students tap states to read their values, rank the top five on each side, drag a threshold to find "
          "balanced states, and place a guess for a hidden state before it is revealed.",
          ["Positive is rice, negative is wheat, near zero is balanced.",
           "A hidden value can be estimated from its neighbours, but it stays an estimate."])],
    key_terms=["infographic", "preference", "scale"]))

# ============================== T10 Strips and sleep ========================================================
TOPICS.append(TOPIC(
    "T10", "M2", "What Can a Strip Say? Sleepy-Deepy", ["5.2"], "Analyze",
    "Students read a day from a colour strip of 48 half hour boxes, guess which day of the week it is and when a "
    "long movie happened, make a strip of their own, and read a full and a zoomed line graph of sleep over age.",
    "A strip stores a whole day in 48 boxes of 30 minutes each; a line graph with many close points looks smooth, "
    "and zooming in shows detail.",
    [A("T10.C1", "Reading Manoj's strips", "Analyze",
       "Students match colours to activities with the key, work out the time of an activity from the box count, "
       "and infer which day of the week a strip shows and when a long movie happened.",
       textbook=["What can a Strip Say? Manoj has an interesting hobby. He makes note of what he does throughout the "
                 "day. He records his activities by colouring a strip of paper with 48 boxes, marking time in 30 "
                 "minute intervals from midnight to midnight.",
                 "He has recorded five types of activities for three different days of the week on three coloured "
                 "strips: sleeping, eating, meeting friends, hobbies, media, time with family, attending classes, "
                 "studying and homework, showering and getting dressed, yoga or exercise, and travelling.",
                 "Look at the three coloured strips carefully. What activity does each colour stand for?",
                 "The three strips correspond to the days Friday to Sunday in some order. Which day do you think each "
                 "strip represents?",
                 "On one of these days, he went out with friends to watch a long movie. When do you think this happened?",
                 "At what time does his school break for lunch? What more can the strips tell us?"],
       teach=["Predict first: 48 boxes of 30 minutes cover a whole day. How many boxes make one hour, and what time "
              "does box 19 start?",
              "2 boxes make an hour, so 48 boxes make 24 hours. Box 19 starts after 18 boxes, which is 9 hours "
              "after midnight, at 9:00 am.",
              "Use the key to see which colour is which activity. A strip with a long block of the class colour "
              "and a travel colour before and after is a school day, and the strip with a long unbroken block of "
              "the friends and media colour is the movie day.",
              "Compare the three strips: when he wakes up, how long he sleeps, how much time goes to meals."],
       examples=[
           WE("Manoj's school runs from 9:30 am to 4:30 pm. How many boxes of his strip does the school block cover, "
              "and which box does it start at?",
              ["From 9:30 am to 4:30 pm is 7 hours.", "Each hour is 2 boxes, so the block is 7 × 2 = 14 boxes.",
               "9:30 am is 9 hours 30 minutes after midnight, which is 19 boxes, so the block starts at box 20."],
              "14 boxes, starting at box 20", ncert=["5.2.strip_intro", "5.2.strip_questions"])],
       key_terms=["strip", "activity", "interval"], misconceptions=["M_STRIP_SAME"], minutes=10),
     A("T10.C2", "Your strip: a weekday, a holiday, an adult", "Create",
       "Students sketch how their own weekday strip and a holiday strip would look, and compare them with an "
       "adult's strip, naming what is similar and different.",
       textbook=["What would your strip for a weekday look like? How similar or different is it to Manoj's?",
                 "What would a strip of your typical day during your vacation look like? How similar or different "
                 "would it look?",
                 "What would a strip for any of the adults in your family look like? Make a strip of a day for any "
                 "adult at home. Compare your strip with theirs. What do you find interesting?"],
       teach=["Predict first: would your weekday strip have a longer sleep block or a shorter one than Manoj's?",
              "Colour 48 boxes for your own day, using the same colours for the same activities.",
              "Compare it with the strip of an adult at home and note what is alike and what is different."],
       examples=[
           WE("You sleep 8 hours on a weekday and 10 hours on a holiday. How many boxes of sleep does each strip "
              "have, and how many more on the holiday?",
              ["Each hour is 2 boxes.", "Weekday: 8 × 2 = 16 boxes. Holiday: 10 × 2 = 20 boxes.",
               "The holiday strip has 20 − 16 = 4 more boxes of sleep."],
              "16 boxes and 20 boxes; 4 more boxes, which is 2 more hours, on the holiday")],
       ncert=["5.2.strip_own", "5.2.strip_adult"], key_terms=["strip", "compare"], minutes=8),
     A("T10.C3", "Sleepy-Deepy: a full graph and a zoomed graph", "Analyze",
       "Students read a smooth line graph of sleep time over age, say why 80 points look like a curve, and "
       "compare the full graph with the zoomed one.",
       textbook=["Data Story: Sleepy-Deepy. Isn't it amusing that there are animals that sleep as little as 2 hours "
                 "per day and animals that sleep as much as 20 hours per day? Humans typically sleep for about 7 to 9 "
                 "hours a day. The amount of sleep people need depends on age, living conditions, lifestyle among "
                 "other factors.",
                 "The line graphs below show typical sleep durations of Indians across ages 6 to 75. The second picture "
                 "is a zoomed-in version of the first picture. Share your observations on this graph.",
                 "Unlike the earlier graphs that were made up of a few connected line segments, this line graph looks "
                 "like a smooth curve because it contains 80 data points that are placed very close to each other. "
                 "Representing the same data using a column graph would require 70 columns, making the graph look "
                 "cluttered and heavy.",
                 "From the graph we can see that the average sleep time for 6-year olds is about 9.5 hours per day. "
                 "The daily sleep time decreases as we grow through teenage years and step into adulthood, touching "
                 "about 8 hours a day between ages 30 and 50. After 50, the daily sleep time increases, reaching "
                 "about 8.5 hours.",
                 "You might wonder why newborns and infants sleep for so long. Do people in different countries "
                 "sleep differently? Do animals also exhibit such patterns in sleep durations across age?"],
       teach=["Predict first: at which age would you expect the most sleep per day, and at which age the least?",
              "Step one: age 6 to 75 along the bottom, hours of sleep up the side. Step two: about 9.5 hours at "
              "6, falling to about 8 hours between 30 and 50, then rising to about 8.5 hours.",
              "The zoomed graph stretches the sleep scale so small changes are easy to see, but the same data looks "
              "steeper, so check the scale before judging how big a change is.",
              "80 close points make a smooth curve. Columns would need 70 bars, so the line graph is lighter."],
       examples=[
           WE("About how much more sleep does a 6 year old get than a person aged between 30 and 50?",
              ["At age 6 the graph reads about 9.5 hours.", "Between ages 30 and 50 it reads about 8 hours.",
               "9.5 − 8 = 1.5 hours more."],
              "About 1.5 hours more a day", ncert=["5.2.sleep_intro", "5.2.sleep_observe", "5.2.sleep_smooth",
                                                    "5.2.sleep_why"])],
       key_terms=["sleep", "zoomed", "smooth curve"], misconceptions=["M_SMOOTH", "M_AXIS"], minutes=10),
     DOER("T10.C4", "Practice: paint a day on a strip", "activity_strip", "Create",
          "Students colour the 48 boxes of a strip with a key, read off the hours spent on each activity, and "
          "compare two strips box by box.",
          ["Two boxes make an hour, and 48 boxes make a day.",
           "The same colour always means the same activity within one strip key."])],
    key_terms=["strip", "sleep", "line graph"]))
