# -*- coding: utf-8 -*-
"""Topics T1 to T4 (module M1: questions, statements and the mean as a fair share). Book sections 5.1 and 5.2
(first part)."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Framing =================================================================
TOPICS.append(TOPIC(
    "T1", "M1", "Two Friends, Five Feet and Six Feet", ["Chapter opening", "5.1"], "Understand",
    "",
    "Two friends, one 5 feet tall and one 6 feet tall: a guess from experience, and the question of how one number "
    "can speak for a whole group.",
    [A("T1.C1", "Guessing from experience: two friends of different heights", "Remember", "",
       textbook=["5 Connecting the Dots...", "5.1 Of Questions and Statements",
                 "Your teacher tells you that they are meeting two of their childhood friends this evening. One is 5 "
                 "feet tall and the other is 6 feet tall. What is your guess as to each friend's gender based on this "
                 "information?",
                 "You might have guessed that the 5-foot-tall person is a woman and the 6-foot-tall person is a man. "
                 "There is a chance that you are wrong. But experience tells us that 5-foot-tall men and 6-foot-tall "
                 "women are rare. We have seen that, more often, men are taller than women.",
                 "The above is a simple example of statistical thinking."],
       teach=["Make a guess before reading on: which friend is more likely to be a man, and why?",
              "The guess comes from many people we have seen, not from one person. That is statistical thinking.",
              "The guess can be wrong for one person and still be a good guess about most people."],
       ncert=["opening"], key_terms=["statistical thinking"], video_focus=["HOOK"], minutes=4, enrichment=True),
     A("T1.C2", "The question to keep: can one number stand for a group?", "Understand", "",
       teach=["Predict: if you were asked how tall the people in your town are, would one height answer it?",
              "Heights vary from person to person, so the answer has to describe a whole group.",
              "Keep this question in mind: the next topics find numbers that represent a group fairly."],
       enrichment=True)],
    topic_type="framing"))

# ============================== T2 Statements and questions ================================================
TOPICS.append(TOPIC(
    "T2", "M1", "Statistical Statements and Statistical Questions", ["5.1"], "Understand",
    "Students recognise statistical statements as claims built from data, and decide whether a question is a "
    "statistical question by asking whether its answer comes from collecting data that varies.",
    "A statistical statement summarises data in numbers; a statistical question is answered by collecting data that "
    "varies.",
    [A("T2.C1", "Statistical statements around us", "Understand",
       "Students identify statistical statements in everyday speech and explain which data each statement summarises, "
       "such as times, distances, counts or predictions.",
       textbook=["We regularly come across statements like:",
                 "Jemimah's batting has been very consistent over the past year. We can expect a century from her in "
                 "tomorrow's match.",
                 "I take about 15 minutes to cycle from school to home.",
                 "I think my pen might last for 2 more weeks; it is time to get a new one soon.",
                 "The population of their village has reduced by about 100 in the last decade.",
                 "Since I started to eat fruits and vegetables more frequently, I am able to run 2 km more each day.",
                 "David spends about 7 hours daily in the school.",
                 "We call these statistical statements. Simply put, a statistical statement is a claim or summary "
                 "about some phenomenon, expressed in terms of numerical values, proportions, probabilities, or "
                 "predictions."],
       teach=["Predict first: what do the six statements have in common?",
              "Each one sums up many past observations in a number: minutes, weeks, people, kilometres or hours.",
              "The word about appears often, because the data varies from day to day."],
       examples=[
           WE("Read the statement 'I take about 15 minutes to cycle from school to home.' Why is it a statistical "
              "statement, and what data is behind it?",
              ["The rider has cycled home on many days.", "Each day took a slightly different time, for example 13, "
               "16, 15 or 14 minutes.", "The word about tells us the times vary.",
               "The number 15 sums up all those days in one value.",
               "A claim that sums up data in a number is a statistical statement."],
              "It is a statistical statement because 15 minutes sums up many ride times that vary from day to day",
              ncert=["5.1.statements"])],
       key_terms=["statistical statement", "data"], misconceptions=["M_ONE_ANSWER"], minutes=8),
     A("T2.C2", "Which questions are statistical questions?", "Analyze",
       "Students decide which questions are statistical questions, explaining that the answer needs data that varies "
       "and cannot come from one fixed fact or one person's reply.",
       textbook=["A statistical question is a question that can be answered by collecting data. For example, 'How tall "
                 "are Grade 7 students in our school?' is a statistical question. We expect that not all Grade 7 "
                 "students have the same height, but we can collect data, analyse it, and make conclusions about the "
                 "heights that do occur. The question 'Typically, are onions costlier in Yahapur or Wahapur?' is also a "
                 "statistical question. Prices can vary over time. Therefore, answering this question requires us to "
                 "look at data, analyse it, and come to conclusions making suitable statistical statements.",
                 "Which of the following are statistical questions? (a) What is the price of a tennis ball in India? "
                 "(b) How old are the dogs that live on this street? (c) What fraction of the students in your class "
                 "like walking up a hill? (d) Do you like reading? (e) Approximately how many bricks are in this wall? "
                 "(f) Who was the best bowler in the match yesterday? (g) What was the rainfall pattern in Barmer last "
                 "year?",
                 "The term statistics refers to the study of collecting, organising, analysing, interpreting, and "
                 "presenting data. In this chapter, we shall encounter some statistical questions and learn how "
                 "analysing data and graphs can help answer them."],
       teach=["Predict first: is 'How tall is Meena?' a statistical question? Is 'How tall are the children in your "
              "class?'",
              "Test each question: will we need many values that differ from one another?",
              "One person's opinion or one fixed count is not enough to make a question statistical."],
       examples=[
           WE("Which of these are statistical questions? (a) the price of a tennis ball in India (b) the ages of the "
              "dogs on this street (c) the fraction of your class who like walking up a hill (d) Do you like reading? "
              "(e) about how many bricks are in this wall (f) the best bowler in yesterday's match (g) the rainfall "
              "pattern in Barmer last year",
              ["(a) Prices differ between shops and brands, so we collect many prices: statistical.",
               "(b) The dogs have different ages, so we collect each age: statistical.",
               "(c) Each student answers yes or no, and the replies vary: statistical.",
               "(d) This asks one person about themself, so there is one answer: not statistical.",
               "(e) There is one wall and one count to estimate: not statistical.",
               "(f) We compare the wickets and runs of several bowlers, which is data: statistical.",
               "(g) The rainfall changes from day to day and month to month: statistical."],
              "(a), (b), (c), (f) and (g) are statistical questions; (d) and (e) are not",
              ncert=["5.1.questions_def", "5.1.mathtalk_statq"])],
       key_terms=["statistical question", "statistics"], misconceptions=["M_ONE_ANSWER"], minutes=10),
     DOER("T2.C3", "Practice: sort the questions", "stat_question_sorter", "Analyze",
          "Students sort everyday questions into statistical and not statistical, giving for each the data that "
          "would have to be collected or the single fact that answers it.",
          ["A statistical question expects answers that vary.",
           "Its answer comes from collecting and summarising data.",
           "A question about one fixed fact or one person's opinion is not statistical."])]))

# ============================== T3 Two batters ==============================================================
TOPICS.append(TOPIC(
    "T3", "M1", "Who Batted Better? Totals and the Mean", ["5.2"], "Evaluate",
    "Students compare two batters using the highest score, the total and how consistent each is, see why totals "
    "mislead when the numbers of matches differ, and use the mean, or average, as a fair representative value.",
    "Highest score, total and range each tell part of the story; with unequal numbers of matches, the mean compares "
    "fairly.",
    [A("T3.C1", "Comparing two batters: highest score, total and range", "Evaluate",
       "Students compare two batters' runs by the highest score, the total and the range, and judge which comparison "
       "is fairest when both play the same number of matches.",
       textbook=["5.2 Representative Values",
                 "The runs scored by Shubman and Yashasvi in a cricket series are given in the table below. Who do you "
                 "think performed better?",
                 "Shubman: Match 1, 0; Match 2, 17; Match 3, 21; Match 4, 90. Yashasvi: Match 1, 67; Match 2, 55; "
                 "Match 3, 18; Match 4, 35.",
                 "Shreyas says, 'Both their performances are similar since Yashasvi scored more in the first and second "
                 "matches, whereas Shubman scored more in the third and fourth'.",
                 "Vaishnavi says, 'I think Shubman performed better because he scored the highest number of run in a "
                 "match, 90!'.",
                 "Shreyas says, 'No! Yashasvi batted better since the total number of runs he made is 175, while "
                 "Shubman made only 128'.",
                 "Vaishnavi says, 'Oh! Also, Yashasvi's batting is more consistent: the difference between his maximum "
                 "score and minimum score is lower'."],
       teach=["Predict first: who batted better, the one with the single biggest score or the one with more runs "
              "overall?",
              "One big score does not show how the player did in the other matches.",
              "With the same number of matches, the totals compare fairly; the difference between the highest and "
              "lowest score shows consistency."],
       examples=[
           WE("Shubman scored 0, 17, 21 and 90 in four matches. Yashasvi scored 67, 55, 18 and 35. Compare them by "
              "highest score, total and the difference between the highest and lowest scores.",
              ["Highest score: Shubman 90, Yashasvi 67.",
               "Total: Shubman 0 + 17 + 21 + 90 = 128; Yashasvi 67 + 55 + 18 + 35 = 175.",
               "Highest minus lowest: Shubman 90 − 0 = 90; Yashasvi 67 − 18 = 49.",
               "Both played 4 matches, so the totals compare fairly: Yashasvi made 47 more runs.",
               "Yashasvi's smaller difference, 49, shows he was more consistent."],
              "Yashasvi batted better: total 175 against 128, and a smaller spread, 49 against 90",
              ncert=["5.2.series1"])],
       key_terms=["total", "consistent"], misconceptions=["M_HIGHEST_BEST"], minutes=10),
     A("T3.C2", "Unequal matches: the mean as one representative number", "Apply",
       "Students explain why totals mislead when two batters play different numbers of matches, and compute each "
       "batter's mean runs per match to compare them fairly.",
       textbook=["The table below shows the runs scored by these two players in another series. Who do you think "
                 "performed better in this series?",
                 "Shubman: 23, 07, 10, 52, 18. Yashasvi: 26, 53, 02, no entry (did not play), 15.",
                 "Vaishnavi says, 'Here, Shubman performed better since his total is 110 runs, while Yashasvi's total "
                 "is 96 runs'.",
                 "What do you think of Vaishnavi's statement?",
                 "Shreyas says, 'But Yashasvi made 96 runs in 4 matches and Shubman made 110 runs in 5 matches'.",
                 "So, how do we say who performed better? It is often not simple to compare two groups of numbers and "
                 "clearly say that one is better than the other.",
                 "Can a single number act as a representative of a group of numbers? For example, can we represent "
                 "Shubman's or Yashasvi's batting in this series with one number? Discuss.",
                 "We saw one way already, the total of the values in the group! But, if the group sizes are different, "
                 "then the total may not be an appropriate measure to compare.",
                 "In some matches, a player could have scored more and in other matches less. A representative number "
                 "for the group can be found by balancing out these highs and lows. For example, we can add up the runs "
                 "scored in all the matches and divide the total by the number of matches played. We call this value "
                 "the 'average' or 'arithmetic mean' of the given data.",
                 "Here, the average number of runs scored by a player in a match = [Total runs scored by the player in "
                 "all the matches] ÷ [Number of matches played].",
                 "Average number of runs scored by Shubman in a match = 110 ÷ 5 = 22 runs.",
                 "Average number of runs scored by Yashasvi in a match = 96 ÷ 4 = 24 runs.",
                 "In this series, Yashasvi's average number of runs is higher than Shubman's.",
                 "The Average or Arithmetic Mean (A.M.), or simply Mean, is calculated as follows: Mean = (Sum of all "
                 "the values in the data) ÷ (Number of values in the data)."],
       teach=["Predict first: is a bigger total always the better batter when one played an extra match?",
              "Share each total equally over the matches actually played. That balancing value is the mean.",
              "Mean = sum of the values ÷ number of values. A match not played is not counted."],
       examples=[
           WE("In the second series Shubman scored 23, 7, 10, 52 and 18 in 5 matches. Yashasvi scored 26, 53, 2 and 15 "
              "and did not play one match. Who performed better on average?",
              ["Shubman's total: 23 + 7 + 10 + 52 + 18 = 110 runs in 5 matches.",
               "Yashasvi's total: 26 + 53 + 2 + 15 = 96 runs in 4 matches.",
               "The totals come from different numbers of matches, so they do not compare fairly.",
               "Shubman's mean: 110 ÷ 5 = 22 runs per match.",
               "Yashasvi's mean: 96 ÷ 4 = 24 runs per match.",
               "24 is more than 22, so Yashasvi performed better on average."],
              "Yashasvi, with a mean of 24 runs per match against Shubman's 22",
              ncert=["5.2.series2", "5.2.mathtalk_single", "5.2.mean_def"])],
       key_terms=["mean", "average"], misconceptions=["M_TOTAL_COMPARE"], minutes=10),
     DOER("T3.C3", "Practice: compare by the mean", None, "Apply",
          "Students compare two groups of scores with different numbers of values by finding each group's mean, and "
          "explain why the totals alone would mislead.",
          ["The highest score shows one match, not the whole series.",
           "Totals compare fairly only when the groups have the same size.",
           "The mean shares the total equally over the values actually recorded."])]))

# ============================== T4 Fair share ===============================================================
TOPICS.append(TOPIC(
    "T4", "M1", "Average as a Fair Share", ["5.2"], "Apply",
    "Students treat the mean as a fair share, levelling unequal amounts so everyone gets the same, and compute "
    "means for guavas, flowers and bounces, linking them to old Indian words for levelling.",
    "The mean is the equal share you get when the total is levelled out across all the values.",
    [A("T4.C1", "Sharing guavas fairly", "Apply",
       "Students find each member's fair share of guavas in two groups of different sizes by levelling the totals, "
       "and explain why the fair share is the mean.",
       textbook=["Average as Fair-Share",
                 "The average can also be understood as fair-share or equal-share.",
                 "Shreyas and 4 of his friends have collected the following numbers of guavas: 3, 8, 10, 5, and 4. "
                 "Parag and 5 of his friends have collected the following numbers of guavas: 5, 4, 6, 3, 4, and 8. Each "
                 "group will share their guavas equally amongst themselves. In which group will each member get a "
                 "bigger share of guavas?",
                 "To find this out, we first find out how many guavas each group has collected. Then we divide this "
                 "total by the number of people in the group to get each member's share.",
                 "Shreyas's group has collected 3 + 8 + 10 + 5 + 4 = 30 guavas. Each member of Shreyas's group gets "
                 "30 ÷ 5 = 6 guavas.",
                 "Parag's group has collected 5 + 4 + 6 + 3 + 4 + 8 = 30 guavas. Each member of Parag's group gets "
                 "30 ÷ 6 = 5 guavas.",
                 "So, the members of Shreyas's group get 1 more guava each than the members of Parag's group."],
       teach=["Predict first: both groups collected the same number of guavas. Will everyone get the same share?",
              "Picture stacks of guavas. Move guavas from tall stacks to short ones until all stacks are level.",
              "The level height is the fair share, and it equals total ÷ number of people, the mean."],
       examples=[
           WE("Shreyas's group of 5 collected 3, 8, 10, 5 and 4 guavas. Parag's group of 6 collected 5, 4, 6, 3, 4 and "
              "8 guavas. Each group shares equally. In which group does each member get more?",
              ["Shreyas's group: 3 + 8 + 10 + 5 + 4 = 30 guavas.",
               "Fair share: 30 ÷ 5 = 6 guavas each.",
               "Parag's group: 5 + 4 + 6 + 3 + 4 + 8 = 30 guavas.",
               "Fair share: 30 ÷ 6 = 5 guavas each.",
               "Same total, but fewer people share it in Shreyas's group.",
               "Each member of Shreyas's group gets 6 − 5 = 1 guava more."],
              "Shreyas's group: 6 guavas each against 5, so 1 more each",
              ncert=["5.2.fair_share"])],
       key_terms=["fair share", "mean"], misconceptions=["M_TOTAL_COMPARE", "M_MEAN_IN_DATA"], minutes=10),
     A("T4.C2", "Flowers each day: the mean as a level value", "Apply",
       "Students compute the mean number of hibiscus flowers blooming per day, interpret it as the equal daily "
       "number, and connect it to old Indian words meaning levelling.",
       textbook=["Vaishnavi tracks the number of Hibiscus flowers blooming in her garden each day. The data for the "
                 "last few days' is 2, 7, 9, 4, 3. What is the average number of Hibiscus flowers blooming per day in "
                 "Vaishnavi's garden?",
                 "The average = (the total number of Hibiscus flowers bloomed) ÷ (number of days) "
                 "= (2 + 7 + 9 + 4 + 3) ÷ 5 = 5.",
                 "On an average, 5 Hibiscus flowers bloom daily.",
                 "In this case the average tells us the number of flowers blooming each day, if an equal number of "
                 "flowers bloomed daily.",
                 "One of the terms used for the Arithmetic Mean in ancient Indian mathematics is samamiti (mean "
                 "measure): 'sama' means equal. Some terms used for the Arithmetic Mean in Indian texts include: "
                 "samarajju (mean measure of a line segment) by Brahmagupta (628 CE), samīkaraṇa (levelling, "
                 "equalising) by Mahāvīrācārya (850 CE), sāmya (equality, impartiality, equability towards) by Śrīpati "
                 "(1039 CE) and samamiti (mean measure) by Bhāskarācārya (1150 CE) and Gaṇeṣa (1545 CE). The "
                 "terminology shows that ancient Indian scholars perceived the Arithmetic Mean as the 'common' or "
                 "'equalising' value that is a representative measure of a collection of values."],
       teach=["Predict first: the counts were 2, 7, 9, 4 and 3. Guess the level count before adding.",
              "Add the counts and divide by the number of days.",
              "The mean is the count that would bloom each day if every day were the same; it need not be one of the "
              "data values."],
       examples=[
           WE("Vaishnavi counted 2, 7, 9, 4 and 3 hibiscus flowers blooming on five days. Find the mean number of "
              "flowers per day and say what it means.",
              ["Total flowers: 2 + 7 + 9 + 4 + 3 = 25.", "Number of days: 5.", "Mean: 25 ÷ 5 = 5 flowers per day.",
               "If the same number bloomed every day, 5 would bloom each day.",
               "Check by levelling: 9 gives 4 to 2 to make 5 and 6; 7 gives 2 to 3 and 4 gives 1 to 6, so all are "
               "at 5."],
              "5 flowers per day on average",
              ncert=["5.2.hibiscus", "5.2.history_samamiti"])],
       key_terms=["mean", "samamiti"], misconceptions=["M_MEAN_IN_DATA"], minutes=8),
     DOER("T4.C3", "Practice: level the bars", "bar_leveller", "Apply",
          "Students level unequal bars by moving units from tall bars to short ones, read the common level as the "
          "mean, and check it against total divided by count.",
          ["The mean is the fair share: total ÷ number of values.",
           "Levelling moves units without changing the total.",
           "The mean need not be one of the data values."],
          items=[
              FIO("5.2.FiO1_1", "Figure it Out (fair share), Q1",
                  "Shreyas is playing with a bat and a ball, but not cricket. He counts the number of times he can "
                  "bounce the ball on the bat before it falls to the ground. The data for 8 attempts is 6, 2, 9, 5, 4, "
                  "6, 3, 5. Calculate the average number of bounces of the ball that Shreyas is able to make with his "
                  "bat.",
                  ["Add the bounces: 6 + 2 + 9 + 5 + 4 + 6 + 3 + 5 = 40.",
                   "There are 8 attempts.",
                   "Average: 40 ÷ 8 = 5 bounces."],
                  "5 bounces per attempt", tool="bar_leveller"),
              FIO("5.2.FiO1_2", "Figure it Out (fair share), Q2",
                  "Try the activity above on your own. Collect data for 7 or more attempts and find the average.",
                  ["This is a project: you collect your own data.",
                   "Sample data for 7 attempts: 4, 7, 5, 9, 6, 3, 8 bounces.",
                   "Method: add the counts, 4 + 7 + 5 + 9 + 6 + 3 + 8 = 42, and divide by the number of attempts.",
                   "Sample mean: 42 ÷ 7 = 6 bounces.",
                   "With your own data: write each attempt's count, add them, divide by how many attempts you made, "
                   "and compare your average with Shreyas's 5."],
                  "Sample data 4, 7, 5, 9, 6, 3, 8 gives a mean of 6 bounces; your own answer depends on your data",
                  tool="bar_leveller"),
              FIO("5.2.FiO1_3", "Figure it Out (fair share), Q3",
                  "Identify a flowering plant in your neighbourhood. Track the number of flowers that bloom every day "
                  "over a week during its flowering season. What is the average number of flowers that bloomed per "
                  "day?",
                  ["This is a project: you observe a real plant for 7 days.",
                   "Sample data for a jasmine plant: 3, 5, 4, 6, 2, 5, 3 flowers.",
                   "Method: total 3 + 5 + 4 + 6 + 2 + 5 + 3 = 28 flowers over 7 days.",
                   "Sample mean: 28 ÷ 7 = 4 flowers per day.",
                   "With your own data: count the new flowers at the same time each day, record all 7 counts, add "
                   "them and divide by 7."],
                  "Sample data gives 28 ÷ 7 = 4 flowers per day; your own answer depends on your plant"),
              FIO("5.2.FiO1_4", "Figure it Out (fair share), Q4",
                  "Two friends are training to run a 100 m race. Their running times over the past week are given in "
                  "seconds: Nikhil: 17, 18, 17, 16, 19, 17, 18; Sunil: 20, 18, 18, 17, 16, 16, 17. Who on average "
                  "ran quicker?",
                  ["Nikhil's total: 17 + 18 + 17 + 16 + 19 + 17 + 18 = 122 seconds in 7 runs.",
                   "Sunil's total: 20 + 18 + 18 + 17 + 16 + 16 + 17 = 122 seconds in 7 runs.",
                   "Both means: 122 ÷ 7 ≈ 17.43 seconds.",
                   "A smaller time means a quicker run, and the means are equal.",
                   "So on average neither ran quicker; Sunil's times vary more (16 to 20 against 16 to 19)."],
                  "They ran equally quickly on average: both means are 122 ÷ 7 ≈ 17.43 seconds",
                  tool="bar_leveller"),
              FIO("5.2.FiO1_5", "Figure it Out (fair share), Q5",
                  "The enrolment in a school during six consecutive years was as follows: 1555, 1670, 1750, 2013, "
                  "2040, 2126. Find the mean enrolment in the school during this period.",
                  ["Total: 1555 + 1670 + 1750 + 2013 + 2040 + 2126 = 11154.",
                   "Number of years: 6.",
                   "Mean: 11154 ÷ 6 = 1859 students."],
                  "1859 students per year")],
          ncert=[], misconceptions=["M_MEAN_IN_DATA", "M_TOTAL_COMPARE"])]))
