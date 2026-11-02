# -*- coding: utf-8 -*-
"""Topics T5 to T8 (module M2: dot plots, outliers, the median, comparing groups, zeros and blanks).
Book section 5.2 (second part)."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T5 Know your onions ========================================================
TOPICS.append(TOPIC(
    "T5", "M2", "Know Your Onions: Describing Data with a Dot Plot", ["5.2"], "Analyze",
    "Students describe and compare two towns' monthly onion prices using the maximum, minimum, total, range and "
    "mean, and draw and read a dot plot to see how the data is spread and clustered.",
    "Minimum, maximum, total, range and mean each describe data; a dot plot shows the spread at a glance.",
    [A("T5.C1", "Five ways to compare onion prices", "Analyze",
       "Students compare the monthly onion prices of two towns by highest price, total, month-by-month counts, range "
       "and mean, and judge what each comparison shows.",
       textbook=["Know Your Onions!",
                 "The table shows the monthly price of onions, in rupees per kilogram (kg), at two towns. Where are "
                 "onions costlier, according to you?",
                 "Yahapur, January to December: 25, 24, 26, 28, 30, 35, 39, 43, 49, 56, 59, 44.",
                 "Wahapur, January to December: 19, 17, 23, 30, 38, 35, 42, 39, 53, 60, 52, 42.",
                 "Khushboo: 'I think Wahapur is costlier because it has the highest price of ₹60.'",
                 "Nafisa: 'I added the prices of all months in each location. Yahapur's total is 458, whereas "
                 "Wahapur's total is 450.'",
                 "Vishal: 'Wahapur is costlier since it has 3 numbers in the 50s'.",
                 "Sampat: 'I compared the prices in each month in both locations. Prices in Yahapur are higher for 6 "
                 "months, prices in Wahapur are higher for 5 months, and the prices are the same for 1 month. So, I "
                 "feel Yahapur is costlier.'",
                 "Jithin: 'I noticed that the difference between the highest and lowest prices in Yahapur is "
                 "59 − 24 = 35, and in Wahapur it is 60 − 17 = 43.'",
                 "Data can be described and compared by referring to its minimum value, maximum value, the average "
                 "value, the sum total of all its values, and the difference between the maximum and minimum values.",
                 "Can you think of any other ways to compare the data?",
                 "Find the average price of onions at Yahapur and Wahapur."],
       teach=["Predict first: which town would you call costlier, and which number made you decide?",
              "Check each child's claim against the table. Vishal's count needs care: each town has 2 prices in the "
              "50s (Yahapur 56 and 59, Wahapur 53 and 52), so that comparison is a tie.",
              "The difference between the maximum and minimum is called the range.",
              "Both towns have 12 months, so the totals compare fairly, and so do the means."],
       examples=[
           WE("Compare the onion prices of Yahapur and Wahapur by the highest price, the total, the range and the "
              "mean. Which town is costlier?",
              ["Highest price: Yahapur 59, Wahapur 60.",
               "Totals: Yahapur 458, Wahapur 450.",
               "Range: Yahapur 59 − 24 = 35; Wahapur 60 − 17 = 43.",
               "Mean: Yahapur 458 ÷ 12 ≈ 38.17 rupees per kg; Wahapur 450 ÷ 12 = 37.5 rupees per kg.",
               "Month by month, Yahapur is higher in 6 months and Wahapur in 5, with 1 month equal.",
               "Wahapur has the single highest price, but Yahapur has the higher total and mean, and its prices vary "
               "less."],
              "Yahapur is a little costlier on average: mean ≈ 38.17 against 37.5 rupees per kg",
              ncert=["5.2.onions_opinions", "5.2.onions_measures"])],
       key_terms=["range", "maximum", "minimum"], misconceptions=["M_HIGHEST_BEST"], minutes=10),
     A("T5.C2", "Drawing the onion prices as a dot plot", "Analyze",
       "Students build a dot plot of the onion prices, read off clusters, spread and extreme values, and explain what "
       "the dot plot keeps and what it loses from the table.",
       textbook=["To study data, we can visualise it in multiple ways. One way is shown below; it is called a dot plot. "
                 "Dot plots show data points as dots on a line, helping us visualise variability and patterns in data. "
                 "In the following figure, each dot represents the monthly price of onions.",
                 "The prices in Yahapur are in green and those in Wahapur are in purple. The horizontal line shows the "
                 "prices from 10 to 60 (instead of starting from 0 as there are no values from 0 to 10 or above 60). "
                 "The dots on the vertical line give the number of occurrences of a data value. Notice the equal "
                 "spacing between the units along the horizontal as well as the vertical lines.",
                 "Does this visualisation capture all the data presented in the tables earlier?",
                 "Looking at it, can we tell the price of onions in Yahapur in the month of January?",
                 "This method of presentation orders or sorts the data, but it loses the original (month-wise) "
                 "sequence of the values. However, it allows us to group the data however we wish, just as Vishal did. "
                 "For instance, there are 2 data values between 11 and 20 for Wahapur, while Yahapur has none.",
                 "This representation makes it easier to observe the variation in the data: where and how the data is "
                 "clustered or spread out. We can easily see that the prices in Wahapur are more spread out than those "
                 "in Yahapur. It is also easy to spot the highest and lowest values.",
                 "We can also use the average as one of the ways to compare the prices at these two places.",
                 "A statement such as, 'The price of onions is ₹35 per kilo', may not trigger any further questions. "
                 "But looking at variations in data, like the prices of onions over a year in Yahapur and Wahapur, can "
                 "spark one's curiosity. For example, one might be curious to know more about the two locations.",
                 "You might wonder: Do the seasons affect the price of onions? How much do onion prices vary across "
                 "shops in the same area? What other commodities might have similar patterns? How do the price "
                 "fluctuations impact farmers, consumers, and the industry? Where are these two locations? Are they "
                 "close to each other or far apart? What are the factors that determine the price of onions?",
                 "What else do you wonder about? You can discuss questions that you are curious about with your peers, "
                 "teachers, or family members to find answers.",
                 "Observing and trying to make sense of data can reveal interesting things. It can also trigger our "
                 "curiosity in different directions."],
       teach=["Predict first: if every price becomes a dot on a number line, which town's dots will spread wider?",
              "Draw a line from 10 to 60 with equal spacing. Stack a dot above each price; equal prices stack up.",
              "A dot plot shows spread and clusters, but it hides which month each price belongs to."],
       examples=[
           WE("Draw the 24 onion prices as a dot plot on a line from 10 to 60. What can it show, and what can it not "
              "show?",
              ["Mark 10, 20, 30, 40, 50 and 60 at equal spaces.",
               "Put one dot for each price; repeated prices stack. Wahapur's two 42s make a stack of 2, and 39 has one "
               "dot from each town.",
               "Wahapur has 2 prices between 11 and 20 (17 and 19); Yahapur has none.",
               "Wahapur's dots run from 17 to 60, a range of 43; Yahapur's run from 24 to 59, a range of 35.",
               "So Wahapur's prices are more spread out.",
               "The plot cannot tell us January's price, because the months are lost when the data is sorted."],
              "The dot plot shows spread, clusters and extremes (Wahapur is more spread out), but not which month "
              "each price belongs to",
              ncert=["5.2.dotplot", "5.2.dotplot_questions"])],
       key_terms=["dot plot", "variability"], misconceptions=["M_HIGHEST_BEST"], minutes=10),
     A("T5.C3", "Averages around us", "Understand", "",
       textbook=["Averages Around Us",
                 "The Arithmetic Mean is frequently used in statistics, mathematics, experimental sciences, economics, "
                 "sociology, sports, biology and diverse disciplines as a representative of data. It is popular partly "
                 "because the definition of the arithmetic mean is simple and easy to understand. Some statements "
                 "involving averages in different scenarios are shown below:",
                 "Wheat yield averages 4.7 tonnes per hectare in Punjab vs. 2.9 tonnes per hectare in Bihar.",
                 "3126 is the average number of Indian long films released annually between 2017 and 2024.",
                 "My scooty's average mileage this year is about 45 kilometres per litre.",
                 "An average Indian citizen generates 0.45 kg of waste per day.",
                 "The average rainfall per day in Jharkhand in the month of July is 37.2 mm.",
                 "Smartphone users check their phone 58 times a day on average."],
       teach=["For each statement, name the data that was added up and what it was divided by.",
              "Rainfall per day in July: the total July rainfall shared equally over its 31 days."],
       ncert=["5.2.averages_around"], key_terms=["average"], enrichment=True, minutes=4),
     DOER("T5.C4", "Practice: build a dot plot", "dot_plot_builder", "Analyze",
          "Students place data values as stacked dots on a number line, choose the start and end of the line, and "
          "read the range, clusters and extremes from the finished dot plot.",
          ["Equal spacing on the line; equal values stack upward.",
           "The range is maximum minus minimum.",
           "A dot plot sorts the data and loses the original order."])]))

# ============================== T6 Outliers and the median ==================================================
TOPICS.append(TOPIC(
    "T6", "M2", "Outliers and the Median", ["5.2"], "Analyze",
    "Students find the mean and median of data with and without an outlier, see that an outlier pulls the mean "
    "towards it while the median barely moves, and describe the centre of data using both measures.",
    "An outlier drags the mean; the median, the middle of the sorted data, stays steady.",
    [A("T6.C1", "Heights of two families: mean, median and an outlier", "Analyze",
       "Students compute the mean and median heights of two families, identify the outlier, and compare how the mean "
       "and median change when the outlier is removed.",
       textbook=["Outliers and Medians",
                 "Does the average always give a reasonable summary of the values in a collection? If not, what is an "
                 "alternative? Let us find out.",
                 "Height of a Family",
                 "The heights of the family members of Yaangba and Poovizhi are as follows:",
                 "Yaangba's family: 169 cm, 173 cm, 155 cm, 165 cm, 160 cm, 164 cm.",
                 "Poovizhi's family: 170 cm, 173 cm, 165 cm, 118 cm, 175 cm.",
                 "Find the average height of each family. Can we say that Yaangba's family is taller than Poovizhi's "
                 "family?",
                 "The average height of Poovizhi's family (160.2 cm) is less than that of Yaangba's family (164.3 cm). "
                 "Although most members in Poovizhi's family are taller, their family's average height is less because "
                 "one child is much younger and not as tall as the rest of the family. Their average height, 160.2 cm, "
                 "is less than the heights of 4 out of 5 members. Here, the average doesn't seem to represent the data "
                 "very well.",
                 "Can you think of any other number that can represent the data better?",
                 "One way is to sort the data and pick the number in the middle. This number is called the Median.",
                 "To find the median height of Poovizhi's family, we first sort the heights: 118, 165, 170, 173, 175.",
                 "The middle number in this sorted data is 170. Therefore, the median height is 170 cm.",
                 "Let us find the median height of Yaangba's family. Sorting the heights, we get 155, 160, 164, 165, "
                 "169, 173.",
                 "Since the median is the number in the middle, it will have an equal number of values less than it and "
                 "greater than it. This data does not have a single middle number because it has an even number of "
                 "values (6). In such cases, we take the average of the two middle numbers in the sorted data. "
                 "Therefore, the median height of Yaangba's family is (164 + 165) ÷ 2 = 164.5 cm.",
                 "In this case, does the median represent the heights of the families better than the average?",
                 "In Poovizhi's family, the height of the youngest child is quite different from the heights of the "
                 "rest of the family. We call such a value an outlier. Outliers are values which significantly deviate "
                 "from the rest of the values in the data.",
                 "Notice how the mean and the median are close to each other in Yaangba's data, in the absence of any "
                 "outlier.",
                 "In Poovizhi's data, because of the outlier, the mean is much lower than the median.",
                 "Find the mean and median in Poovizhi's data without the outlier value 118. What change do you "
                 "notice?"],
       teach=["Predict first: which family is taller? Then look again at the 118 cm child.",
              "Sort the values first. The median is the middle value; with an even count, it is the mean of the two "
              "middle values.",
              "A value far from the rest is called an outlier. It pulls the mean towards itself."],
       examples=[
           WE("Find the mean and the median height of Yaangba's family (169, 173, 155, 165, 160, 164 cm) and of "
              "Poovizhi's family (170, 173, 165, 118, 175 cm). Which number represents each family better?",
              ["Yaangba: total 169 + 173 + 155 + 165 + 160 + 164 = 986, mean 986 ÷ 6 ≈ 164.33 cm.",
               "Sorted: 155, 160, 164, 165, 169, 173. Six values, so the median is (164 + 165) ÷ 2 = 164.5 cm.",
               "Poovizhi: total 170 + 173 + 165 + 118 + 175 = 801, mean 801 ÷ 5 = 160.2 cm.",
               "Sorted: 118, 165, 170, 173, 175. The middle value is 170, so the median is 170 cm.",
               "In Poovizhi's family 4 of the 5 members are taller than the mean, because 118 pulls it down.",
               "The median, 170 cm, represents Poovizhi's family better; for Yaangba both are close."],
              "Yaangba: mean ≈ 164.33 cm, median 164.5 cm; Poovizhi: mean 160.2 cm, median 170 cm, and the median "
              "represents Poovizhi's family better",
              ncert=["5.2.family_height", "5.2.median_def"]),
           WE("Find the mean and median of Poovizhi's family without the outlier 118 cm. What changes?",
              ["Without 118 the heights are 165, 170, 173, 175.",
               "Total: 165 + 170 + 173 + 175 = 683, so the mean is 683 ÷ 4 = 170.75 cm.",
               "Four values, so the median is (170 + 173) ÷ 2 = 171.5 cm.",
               "The mean jumps from 160.2 to 170.75, a change of 10.55 cm.",
               "The median moves only from 170 to 171.5, a change of 1.5 cm."],
              "Mean 170.75 cm and median 171.5 cm: the mean rises a lot, the median hardly moves",
              ncert=["5.2.outlier_def"])],
       key_terms=["median", "outlier"], misconceptions=["M_MEDIAN_UNSORTED", "M_EVEN_MEDIAN", "M_OUTLIER_IGNORE"],
       minutes=12),
     A("T6.C2", "Short stories read: an outlier at the top", "Analyze",
       "Students predict and then compute the mean and median of stories read, mark them on a dot plot, and explain "
       "how the high outlier 40 affects each measure.",
       textbook=["Are you a bookworm?",
                 "After the summer vacation, a class teacher asked his class how many short stories they had read. "
                 "Each student answered the number of stories read on a piece of paper, as shown below. Find the mean "
                 "and median number of short stories read. Before calculating them, can you guess whether the mean will "
                 "be less than or greater than the median?",
                 "The papers read: 6, 8, 5, 15, 3, 0, 2, 7, 12, 40, 10, 5, 0, 8, 1.",
                 "Mark the data, the mean, and the median on the dot plot below.",
                 "The median value 6 means that half of the class members have read 6 or more stories.",
                 "Which of the values would you consider an outlier?",
                 "Find the mean and median in the absence of the outlier. What change do you notice?",
                 "The average may not always be an appropriate representative of data that has outliers. A very high "
                 "or a very low outlier can significantly impact the sum, thus affecting the average. For example, the "
                 "118 cm height in Poovizhi's family is an outlier at the lower end of the data. And the count of 40 "
                 "short stories read is an outlier at the higher end of the data. In these cases, we saw that the "
                 "median was not affected much by the outliers."],
       teach=["Predict first: with one student at 40, will the mean be above or below the median?",
              "Sort the 15 values; the 8th is the median.",
              "A high outlier lifts the mean above the median."],
       examples=[
           WE("Fifteen students read 6, 8, 5, 15, 3, 0, 2, 7, 12, 40, 10, 5, 0, 8 and 1 short stories. Find the mean "
              "and median, then find them again without the outlier.",
              ["Sorted: 0, 0, 1, 2, 3, 5, 5, 6, 7, 8, 8, 10, 12, 15, 40.",
               "Total: 122, so the mean is 122 ÷ 15 ≈ 8.13 stories.",
               "There are 15 values, so the median is the 8th value, 6 stories.",
               "40 is far above the rest, so it is the outlier; the mean is above the median.",
               "Without 40: total 82 in 14 values, mean 82 ÷ 14 ≈ 5.86 stories.",
               "Median of 14 values: (5 + 6) ÷ 2 = 5.5 stories.",
               "The mean fell by about 2.27, but the median moved only by 0.5."],
              "Mean ≈ 8.13 and median 6; without 40, mean ≈ 5.86 and median 5.5",
              ncert=["5.2.bookworm"])],
       key_terms=["median", "outlier"], misconceptions=["M_OUTLIER_IGNORE", "M_MEDIAN_UNSORTED"], minutes=10),
     A("T6.C3", "Newspaper pages: when mean and median are close", "Analyze",
       "Students find the mean and median newspaper pages, then compare three data sets to explain where the mean "
       "sits relative to the median when outliers are low, high or absent.",
       textbook=["Are We on the Same Page?",
                 "Do you read newspapers? Have you noticed how many pages a newspaper has on different days of the "
                 "week; is it the same or different?",
                 "The list below shows the number of pages for a particular newspaper from Monday to Sunday: 16, 18, "
                 "20, 22, 26, 16, 10.",
                 "Mark the data, the mean, and the median on the dot plot below.",
                 "In the three examples we considered (the heights, short-stories, and newspaper pages) observe the "
                 "variability in data when: (a) the mean and median are close to each other (b) the mean and median are "
                 "comparatively far apart, with mean < median (c) the mean and median are comparatively far apart, "
                 "with mean > median",
                 "When the data is more balanced or uniformly spread out the mean, and the median appear to be close to "
                 "each other. When the outlier is on the lower end, the mean appears to shift in that direction, i.e., "
                 "mean < median. When the outlier is on the higher end, the mean appears to shift in that direction, "
                 "i.e., mean > median.",
                 "Discuss the effect on the mean and median when outliers are present on both sides. You may take some "
                 "example data to examine and explain this.",
                 "Mean and Median are called measures of central tendency, i.e., the tendency of the values to pile up "
                 "around a particular value. In other words, they represent the 'centre' of the data."],
       teach=["Predict first: are these page counts balanced, or is there an outlier?",
              "Balanced data: mean and median close. Low outlier: mean below median. High outlier: mean above median.",
              "Outliers on both sides can cancel: for 2, 20, 21, 22, 23, 24, 45 the mean is 157 ÷ 7 ≈ 22.43 and the "
              "median is 22.",
              "Mean and median are measures of central tendency: they describe the centre of the data."],
       examples=[
           WE("A newspaper had 16, 18, 20, 22, 26, 16 and 10 pages from Monday to Sunday. Find the mean and median "
              "and compare with the family heights and the stories read.",
              ["Total: 16 + 18 + 20 + 22 + 26 + 16 + 10 = 128 pages.",
               "Mean: 128 ÷ 7 ≈ 18.29 pages.",
               "Sorted: 10, 16, 16, 18, 20, 22, 26, so the median is the 4th value, 18 pages.",
               "Mean and median are close: the data is fairly balanced (like Yaangba's family).",
               "Poovizhi's family has a low outlier, so mean < median (160.2 < 170).",
               "The stories have a high outlier, so mean > median (8.13 > 6)."],
              "Mean ≈ 18.29 pages and median 18 pages, which are close because the data is balanced",
              ncert=["5.2.same_page", "5.2.mathtalk_mean_median", "5.2.central_tendency"])],
       key_terms=["central tendency", "median"], misconceptions=["M_OUTLIER_IGNORE"], minutes=10),
     DOER("T6.C4", "Practice: drag the outlier", "outlier_race", "Analyze",
          "Students drag one value far from the rest of a data set and watch the mean and the median move, then "
          "predict which measure will move further for new data.",
          ["Sort before finding the median; with an even count use the mean of the two middle values.",
           "An outlier pulls the mean towards it.",
           "The median changes little when one value becomes extreme."])]))

# ============================== T7 Ends and essence =========================================================
TOPICS.append(TOPIC(
    "T7", "M2", "Of Ends and the Essence: Comparing Groups", ["5.2"], "Evaluate",
    "Students compare groups using the minimum, maximum, mean and median from dot plots, for heights of boys and "
    "girls and for estimates of one minute, and state careful conclusions that describe the group, not every member.",
    "Extremes show the variability; the mean and median show the centre; together they describe a group fairly.",
    [A("T7.C1", "How tall is your class? Boys, girls and the whole class", "Evaluate",
       "Students compare the heights of boys and girls in a class using extremes, means and medians from dot plots, "
       "and count how many students are taller than the class mean.",
       textbook=["Of Ends and the Essence",
                 "As we have just seen, the mean and the median can give different perspectives on the data. As part of "
                 "analysing data, it can also be valuable to look at the variability in the given data, i.e., its "
                 "extremes (minimum and maximum values).",
                 "How Tall is Your Class?",
                 "Suppose you are asked the question, 'How tall is your class?' What would you say?",
                 "The table below shows the heights of students in a Grade 5 class in centimetres.",
                 "Boys: 147, 135, 130, 154, 128, 135, 134, 158, 155, 146, 146, 142, 140, 141, 144, 145, 150",
                 "Girls: 143, 136, 150, 144, 154, 140, 145, 148, 156, 150, 150",
                 "We can visualise the data using a dot plot, identify the ends and patterns, and look at the "
                 "variability. We can also find the measures of central tendency. The dot plot for the whole class, "
                 "followed by the dot plots for boys and girls, respectively, are shown. The mean and the median are "
                 "also shown for each collection.",
                 "Whole class: mean 144.5, median 145. Boys: mean 142.94, median 144. Girls: mean 146.9, median 148.",
                 "What can we infer from the dot plots and the central tendency measures?",
                 "The following points can help answer the question of how tall the class is.",
                 "The boys' heights are more spread out and are between 128 and 158. The girls' heights lie between 136 "
                 "and 156. Both the tallest and shortest in the class are boys.",
                 "Yet, the boys' average height is less than the whole class average, and also less than the girls' "
                 "average height. We can say girls are taller than boys in this class. Of course, this doesn't mean "
                 "every girl is taller than every boy!",
                 "For boys' heights, mean < median (142.94 < 144) indicating a small influence of values on the lower "
                 "side. For girls' heights too, mean < median (146.9 < 148) indicating a small influence of values on "
                 "the lower side.",
                 "How many students are taller than the class' average height?",
                 "How many boys are taller than the class' average height?"],
       teach=["Predict first: who is taller in this class, boys or girls? Is every girl taller than every boy?",
              "Read the extremes first: boys 128 to 158, girls 136 to 156.",
              "Then read the centre: girls have the higher mean and median, but the ranges overlap.",
              "The whole class mean is 4046 ÷ 28 = 144.5 cm."],
       examples=[
           WE("A Grade 5 class has 17 boys and 11 girls with the heights in the table. Compare boys and girls, and "
              "count the students, and the boys, taller than the class mean.",
              ["Boys: 128 to 158 cm, total 2430, mean 2430 ÷ 17 ≈ 142.94 cm, median 144 cm.",
               "Girls: 136 to 156 cm, total 1616, mean 1616 ÷ 11 ≈ 146.91 cm, median 148 cm.",
               "Whole class: total 4046, mean 4046 ÷ 28 = 144.5 cm, median 145 cm.",
               "Girls have the higher mean and median, so girls are taller in this class on the whole.",
               "But the tallest (158) and the shortest (128) are both boys, so not every girl is taller.",
               "Heights above 144.5: 8 boys (145, 146, 146, 147, 150, 154, 155, 158) and 7 girls, 15 students in "
               "all."],
              "Girls are taller on the whole (mean ≈ 146.91 against 142.94); 15 students, of whom 8 are boys, are "
              "taller than the class mean of 144.5 cm",
              ncert=["5.2.grade5_heights"])],
       key_terms=["minimum", "maximum"], misconceptions=["M_AVERAGE_ALL"], minutes=10),
     A("T7.C2", "How long is a minute? Two groups compared", "Evaluate",
       "Students compare two groups' estimates of one minute using the range, mean, median and how many estimates "
       "fall close to 60 seconds, and decide which group did better.",
       textbook=["How long is a minute?",
                 "Two groups of children were asked to estimate the length of 1 minute. They start by closing their "
                 "eyes and then open when they think 1 minute has passed. Of course, they are not supposed to count "
                 "while their eyes are closed. The dot plots below show after how many seconds the children opened "
                 "their eyes.",
                 "Discuss how well both the groups fared at this activity. Describe and compare the variability in data "
                 "and their central tendency.",
                 "Group A: mean 58.21, median 60. Group B: mean 59.29, median 59.5."],
       teach=["Predict first: is the group whose mean is closest to 60 the group that estimated best?",
              "Look at the ends: how far from 60 did the extreme estimates go?",
              "Count how many estimates landed within 5 seconds of 60."],
       examples=[
           WE("The first group's 33 estimates run from 42 to 68 seconds, with mean ≈ 58.21 and median 60. The second "
              "group's 28 estimates run from 47 to 71 seconds, with mean ≈ 59.29 and median 59.5. Which group fared "
              "better?",
              ["First group: range 68 − 42 = 26 seconds; 20 of the 33 estimates are from 55 to 65 seconds.",
               "Second group: range 71 − 47 = 24 seconds; 19 of the 28 estimates are from 55 to 65 seconds.",
               "Both means are a little below 60, so on average both groups opened their eyes a little early.",
               "The first group's median is exactly 60, but a few very early estimates (42, 45, 46) pull its mean down.",
               "The second group's mean, 59.29, is closer to 60, and a larger share of its estimates (19 of 28) are "
               "within 5 seconds."],
              "Both groups did well; the second group was slightly better, with mean ≈ 59.29 closer to 60 and a "
              "smaller range of 24 seconds",
              ncert=["5.2.minute"])],
       key_terms=["range", "median"], misconceptions=["M_MEAN_ALWAYS"], minutes=10),
     DOER("T7.C3", "Practice: describe and compare two groups", None, "Evaluate",
          "Students describe two groups using their minimum, maximum, range, mean and median, and write one careful "
          "comparison statement that holds for the groups but not for every member.",
          ["Read the extremes before the centre.",
           "A higher mean for a group does not make every member higher.",
           "Count values near a target to judge how well a group did."])]))

# ============================== T8 Zero, blank and the mean =================================================
TOPICS.append(TOPIC(
    "T8", "M2", "Zero, No Value and Choosing the Data", ["5.2"], "Evaluate",
    "Students decide whether a zero counts as a value and a missing value does not, choose which values belong in a "
    "mean or median, and explain how a team can have median zero runs yet a large total.",
    "A zero is a real value; a missing value is not counted; choose the data that fits the question before averaging.",
    [A("T8.C1", "Zero median runs, yet a big total", "Analyze",
       "Students explain how a cricket team can have median zero runs per player but a large total, by sorting the "
       "scores and computing the mean runs per player.",
       textbook=["Zero Median Runs Scored!",
                 "In yesterday's match, the median runs scored by England's players was 0, and yet the team scored 407 "
                 "for the loss of 10 wickets.",
                 "In a cricket match, can a team's median runs scored by a player be 0 but the team's total score be "
                 "407/10?",
                 "The players' scores in that innings: 19, 0, 0, 22, 158, 0, 184, 5, 0, 0, 0, with 19 extras.",
                 "Accounting for the extras, the average runs scored by a player in this innings is "
                 "(407 − 19) ÷ 11 = 35.27."],
       teach=["Predict first: can most players score 0 while the team scores over 400?",
              "Sort the eleven scores. If six or more are 0, the middle score is 0.",
              "The mean uses every run, so two huge scores lift it far above the median."],
       examples=[
           WE("England's eleven batters scored 19, 0, 0, 22, 158, 0, 184, 5, 0, 0, 0, and the team made 407 including "
              "19 extras. Find the median and the mean runs per player.",
              ["Sorted: 0, 0, 0, 0, 0, 0, 5, 19, 22, 158, 184.",
               "There are 11 scores, so the median is the 6th score, which is 0.",
               "Runs by batters: 407 − 19 = 388.",
               "Mean: 388 ÷ 11 ≈ 35.27 runs per player.",
               "Two big scores, 158 and 184, make up most of the total, so the mean is far above the median."],
              "Median 0 runs, mean ≈ 35.27 runs per player",
              ncert=["5.2.zero_median"])],
       key_terms=["median", "mean"], misconceptions=["M_MEAN_ALWAYS"], minutes=8),
     A("T8.C2", "Zero runs or did not play?", "Apply",
       "Students separate a score of zero from a match not played, count only the matches played, and compute the "
       "mean runs per match correctly.",
       textbook=["Zero vs. No value",
                 "Suppose a player scores 57, 13, 0, 84, no entry (did not play), 51, 27 in a series. Notice that the "
                 "player played Match 3 and scored 0 runs whereas the player did not play Match 5. So, we consider the "
                 "total number of matches to be 6 and not 7.",
                 "We calculate their average runs scored per match as (57 + 13 + 0 + 84 + 51 + 27) ÷ 6."],
       teach=["Predict first: should the mean be divided by 7 or by 6?",
              "A zero is a real score from a match played, so it counts.",
              "A match not played has no value, so it is left out of both the total and the count."],
       examples=[
           WE("A player scores 57, 13, 0, 84, did not play, 51 and 27 in a series of seven matches. Find the mean runs "
              "per match.",
              ["The 0 is a match played, so it counts as a value.",
               "The match not played has no value, so leave it out.",
               "Matches played: 6.",
               "Total: 57 + 13 + 0 + 84 + 51 + 27 = 232.",
               "Mean: 232 ÷ 6 ≈ 38.67 runs per match.",
               "Dividing by 7 would give about 33.14, which is wrong because one match was not played."],
              "232 ÷ 6 ≈ 38.67 runs per match",
              ncert=["5.2.zero_blank"])],
       key_terms=["missing value", "zero"], misconceptions=["M_ZERO_BLANK"], minutes=8),
     A("T8.C3", "Mangoes in season, and a mean foot", "Evaluate",
       "Students choose which months belong in the mango data, compare the mean and median with and without the "
       "off-season zeros, and recognise an old rod as a mean of sixteen feet.",
       textbook=["Sita has a mango tree in her backyard. The number of mangoes the tree gave every month over the last "
                 "year, from January to December, is 0, 0, 8, 24, 41, 16, 5, 0, 0, 0, 0, 0 respectively. If we want to "
                 "find the mean or median number of mangoes per month, it would be appropriate to consider only the "
                 "(summer) months when mangoes are expected to grow.",
                 "A Mean Foot",
                 "In the early 1500s in Europe, the basic unit of land measurement was the rod, defined as 16 feet "
                 "long. At that time, a foot meant the length of a human foot! But foot sizes vary, so whose foot could "
                 "they measure? To solve this, 16 adult males were asked to stand in a line, toe to heel, and the length "
                 "of that line was considered the 16-foot rod. After the rod was determined, it was split into 16 equal "
                 "sections, each representing the measure of a single foot. In essence, this was the arithmetic mean of "
                 "the 16 individual feet, even though the term 'mean' was not mentioned anywhere.",
                 "Jacob Kobel's depiction of the determination of 1 foot."],
       teach=["Predict first: is the median of the twelve months a fair picture of the mango tree?",
              "Ask what the question is about. For mangoes per month in season, use only the season's months.",
              "The rod story: one line of 16 feet split into 16 equal parts is total ÷ 16, the mean foot."],
       examples=[
           WE("Sita's mango tree gave 0, 0, 8, 24, 41, 16, 5, 0, 0, 0, 0, 0 mangoes from January to December. Find "
              "the mean and median for all twelve months and for the five summer months.",
              ["Total: 8 + 24 + 41 + 16 + 5 = 94 mangoes.",
               "All twelve months: mean 94 ÷ 12 ≈ 7.83; seven zeros, so the median is 0.",
               "Summer months only (March to July): 8, 24, 41, 16, 5.",
               "Mean: 94 ÷ 5 = 18.8 mangoes per month.",
               "Sorted: 5, 8, 16, 24, 41, so the median is 16 mangoes.",
               "The off-season zeros are not failed harvests, so the summer figures describe the tree better."],
              "All year: mean ≈ 7.83, median 0; in season: mean 18.8, median 16 mangoes per month",
              ncert=["5.2.mangoes", "5.2.mean_foot"])],
       key_terms=["mean", "median"], misconceptions=["M_ZERO_BLANK"], minutes=8),
     DOER("T8.C4", "Practice: count it or leave it out", "zero_blank", "Evaluate",
          "Students decide for each entry whether it is a real zero, a missing value or out of season, choose the "
          "right count to divide by, and compute the mean and median.",
          ["A zero is a value; a missing entry is not.",
           "Only the values that answer the question belong in the data.",
           "Sort before finding the median."],
          items=[
              FIO("5.2.FiO2_1", "Figure it Out (mean and median), Q1",
                  "Find the median of onion prices in Yahapur and Wahapur.",
                  ["Yahapur sorted: 24, 25, 26, 28, 30, 35, 39, 43, 44, 49, 56, 59.",
                   "Twelve values, so the median is the mean of the 6th and 7th: (35 + 39) ÷ 2 = 37.",
                   "Wahapur sorted: 17, 19, 23, 30, 35, 38, 39, 42, 42, 52, 53, 60.",
                   "Median: (38 + 39) ÷ 2 = 38.5.",
                   "So Wahapur has the higher median, though Yahapur has the higher mean (≈ 38.17 against 37.5)."],
                  "Yahapur 37 rupees per kg, Wahapur 38.5 rupees per kg", tool="zero_blank"),
              FIO("5.2.FiO2_2", "Figure it Out (mean and median), Q2",
                  "Sanskruti asked her class how many domestic animals and pets each had at home. Some of the students "
                  "were absent. The data values are 0, 1, 0, 4, 8, 0, 0, 2, 1, 1, 5, 3, 4, 0, 0, no entry, 10, 25, 2, "
                  "no entry, 2, 4. Find the mean and median. How would you describe this data?",
                  ["The two no entry values are absent students, so leave them out; the zeros stay.",
                   "That leaves 20 values with total 72.",
                   "Mean: 72 ÷ 20 = 3.6 animals.",
                   "Sorted: 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 5, 8, 10, 25.",
                   "Median: (2 + 2) ÷ 2 = 2 animals.",
                   "Most students have 0 to 5 animals; 25 is a high outlier, so the mean is above the median.",
                   "Without 25: mean 47 ÷ 19 ≈ 2.47, median still 2."],
                  "Mean 3.6 and median 2; most have few animals, and the outlier 25 pulls the mean up",
                  tool="zero_blank"),
              FIO("5.2.FiO2_3", "Figure it Out (mean and median), Q3",
                  "Rintu takes care of a date-palm tree farm in Habra. The heights of the trees (in feet) in his farm "
                  "are given as: 50, 45, 43, 52, 61, 63, 46, 55, 60, 55, 59, 56, 56, 49, 54, 65, 66, 51, 44, 58, 60, "
                  "54, 52, 57, 61, 62, 60, 60, 67. Fill the dot plot, and mark the mean and median. How would you "
                  "describe the heights of these palm trees? Can you think of quicker ways to find the mean? How many "
                  "trees are shorter than the average height?",
                  ["There are 29 trees, from 43 to 67 feet; the dots cluster from 50 to 62, with a stack of 4 at 60.",
                   "Total: 1621 feet, so the mean is 1621 ÷ 29 ≈ 55.9 feet.",
                   "Sorted, the 15th value is the median: 56 feet.",
                   "Quicker mean: take 55 as a guess. The differences from 55 add up to 26, so the mean is "
                   "55 + 26 ÷ 29 ≈ 55.9 feet.",
                   "Trees shorter than 55.9 feet: 43, 44, 45, 46, 49, 50, 51, 52, 52, 54, 54, 55, 55, which is 13 "
                   "trees.",
                   "Mean and median are close, so the heights are fairly balanced with no strong outlier."],
                  "Mean ≈ 55.9 feet, median 56 feet; 13 trees are shorter than the mean"),
              FIO("5.2.FiO2_4", "Figure it Out (mean and median), Q4",
                  "The daily water usage from a tap was measured. The usage in litres for the first few days are: 5.6, "
                  "8, 3.09, 12.9, 6.5, 12.1, 11.3, 20.5, 7.4. (a) Can the mean or median daily usage lie between 25 and "
                  "30? Justify your claim using the meaning of mean and median. (b) Can the mean or median be lesser "
                  "than the minimum value or greater than the maximum value in a data?",
                  ["The smallest value is 3.09 and the largest is 20.5.",
                   "(a) The mean is a fair share: levelling never lifts every value above the largest, so the mean is at "
                   "most 20.5. The median is one of the middle values, so it is at most 20.5 too. Neither can lie "
                   "between 25 and 30.",
                   "Check: total 87.39, mean 87.39 ÷ 9 ≈ 9.71 litres; sorted, the 5th value gives median 8 litres.",
                   "(b) No. Levelling moves amounts between values, so the level stays between the smallest and the "
                   "largest; the median is a middle value of the sorted data."],
                  "(a) No: mean ≈ 9.71 litres and median 8 litres, both between 3.09 and 20.5 (b) No, never"),
              FIO("5.2.FiO2_5", "Figure it Out (mean and median), Q5",
                  "The weights of a few newborn babies are given in kgs. Boys: 3.5, 4.1, 2.6, 3.2, 3.4, 3.8. Girls: "
                  "4.0, 3.1, 3.4, 3.7, 2.5, 3.4. Fill the dot plot provided below. Analyse and compare this data.",
                  ["Boys: total 20.6, mean 20.6 ÷ 6 ≈ 3.43 kg; sorted 2.6, 3.2, 3.4, 3.5, 3.8, 4.1, median "
                   "(3.4 + 3.5) ÷ 2 = 3.45 kg; range 4.1 − 2.6 = 1.5 kg.",
                   "Girls: total 20.1, mean 20.1 ÷ 6 = 3.35 kg; sorted 2.5, 3.1, 3.4, 3.4, 3.7, 4.0, median 3.4 kg; "
                   "range 4.0 − 2.5 = 1.5 kg.",
                   "Both groups have the same range, and the dots overlap a lot.",
                   "The boys' mean and median are slightly higher, by under 0.1 kg."],
                  "Boys: mean ≈ 3.43 kg, median 3.45 kg; girls: mean 3.35 kg, median 3.4 kg; same spread, boys slightly "
                  "heavier on average"),
              FIO("5.2.FiO2_6", "Figure it Out (mean and median), Q6",
                  "The dot plots of heights of another section of Grade 5 students of the same school are shown below "
                  "(whole class: mean 141.21, median 142.5; boys: mean 142.05, median 143; girls: mean 140.14, median "
                  "140). Can you share your observations? What can we infer from the dot plots and the central "
                  "tendency measures? Compare the heights of the two sections. Share your observations.",
                  ["In this section the boys have the higher mean (142.05 against 140.14) and median (143 against 140).",
                   "The girls range from 126 to 158 cm and the boys from 130 to 148 cm, so the girls are more spread "
                   "out, with both the shortest and the tallest student.",
                   "In the first section the girls were taller on average (146.91 against 142.94).",
                   "Comparing sections: the first section's class mean, 144.5 cm, is higher than this section's 141.21 "
                   "cm.",
                   "Two sections give opposite answers, so we cannot say boys or girls of this age are taller in "
                   "general."],
                  "In this section boys are taller on average; in the first section girls were; the first section is "
                  "taller overall (mean 144.5 against 141.21 cm), so no general claim about boys and girls follows"),
              FIO("5.2.FiO2_7", "Figure it Out (mean and median), Q7",
                  "The weights of some sumo wrestlers and ballet dancers are: Sumo wrestlers: 295.2 kg, 250.7 kg, "
                  "234.1 kg, 221.0 kg, 200.9 kg. Ballet dancers: 40.3 kg, 37.6 kg, 38.8 kg, 45.5 kg, 44.1 kg, 48.2 kg. "
                  "Approximately how many times heavier is a sumo wrestler compared to a ballet dancer?",
                  ["Sumo total: 1201.9 kg, mean 1201.9 ÷ 5 ≈ 240.38 kg.",
                   "Ballet total: 254.5 kg, mean 254.5 ÷ 6 ≈ 42.42 kg.",
                   "Compare the means: 240.38 ÷ 42.42 ≈ 5.67.",
                   "So a typical sumo wrestler is about 6 times as heavy as a typical ballet dancer."],
                  "About 6 times (240.38 ÷ 42.42 ≈ 5.67)")],
          ncert=[], misconceptions=["M_ZERO_BLANK", "M_MEDIAN_UNSORTED"])]))
