# -*- coding: utf-8 -*-
"""Tool specs for modules M3 and M4 (clustered bar graphs, scales, claims and zoomed axes)."""
from topics_common import T

TOOLS = {
    "bar_reader": T(
        "tool_bar_reader", "Clustered Bar Graph Reader", "exploration",
        "A clustered bar graph is read in two steps: identify the organisation and the scale, then infer. Each bar is "
        "read as an estimate against the guidelines, and only what the bars can show is inferred.",
        "A clustered bar graph with three bars per category; a movable reading line that snaps to the guidelines and "
        "shows the value under it; an Identify panel (what is on each line, the scale, the colours); a statement card "
        "with Justified and Not justified buttons.",
        ["Fill the Identify panel: the categories, the years or groups, and the scale.",
         "Slide the reading line to the top of a bar and record the estimate.",
         "Read a statement card and gather the bars it needs.",
         "Press Justified or Not justified and give the reading that decides it."],
        ["Rocket graph: what is the scale? (1 unit = 20 rockets)",
         "Read SpaceX in 2022 (about 61) and say how it compares with 2021 (about twice 31).",
         "Statement: Arianespace launched fewer rockets every year (justified: 15, 6, 3).",
         "Statement: Roscosmos launched more than 60 rockets in the three years (not justified: 55).",
         "Statement: CASC's average is around 40 (justified: 128 ÷ 3 is about 42.67).",
         "Estimate the 2023 world total and choose its range (about 220, so 200 to 400)."],
        ["A reading far from the bar top flashes the nearest two guidelines and their values.",
         "A wrong verdict shows the bars that decide the statement, highlighted with their readings.",
         "A scale entered wrongly shows two guidelines and asks for the gap between them."],
        "The Identify panel is complete and all six cards are decided with the right readings.",
        ["scale", "readingLine", "readings", "card", "verdict"],
        ["M_SCALE_IGNORE", "M_HIGHEST_BEST"],
        ["What does each guideline stand for? Find the gap between two of them.",
         "Which bars does this statement talk about? Read only those.",
         "Add the readings for a total, or divide the total by the number of years for an average.",
         "The deciding bars are read for you and the verdict is shown. A new card follows."]),

    "daylight": T(
        "tool_daylight", "Monthly to Daily Daylight Converter", "exploration",
        "A monthly total becomes an average per day when it is divided by the number of days in that month. Drawing the "
        "daily values for two cities shows opposite patterns, the sign of opposite hemispheres.",
        "A twelve-month table of monthly daylight hours for two cities; a calculator strip that divides by the chosen "
        "number of days; a clustered bar chart that grows as each daily value is entered; a 24-hour bar beside it for "
        "comparison; a pattern panel asking where each city peaks.",
        ["Pick a month and choose its number of days.",
         "Divide the monthly total and enter the daily value for both cities.",
         "Watch the bars grow and compare them with the 24-hour bar.",
         "Name the peak and the lowest month for each city and say what the patterns suggest."],
        ["June, City 1: 564 hours in 30 days gives 18.8 hours a day.",
         "June, City 2: 276 hours in 30 days gives 9.2 hours a day.",
         "December, City 1: 186 hours in 31 days gives 6 hours a day.",
         "February, City 1: 257 hours in 28 days, about 9.18 hours a day.",
         "Which fraction of a 24-hour day is 18 hours? (three quarters)",
         "Both cities complete: where does each peak, and what does that say about where they are?"],
        ["Dividing by the wrong number of days shows the month's calendar with the days counted.",
         "A daily value over 24 is refused, with the 24-hour bar highlighted.",
         "A pattern answer that misses the opposite peaks shows both cities' bars with their peaks circled."],
        "All twelve months are converted for both cities and the peaks are named.",
        ["month", "days", "dailyCity1", "dailyCity2", "peakAnswers"],
        ["M_SCALE_IGNORE", "M_MEAN_IN_DATA"],
        ["How many days does this month have?",
         "Daylight per day is the month's total shared over its days.",
         "Divide the monthly total by 28, 30 or 31, whichever fits the month.",
         "The daily value is filled in for you and its bar is drawn. A new month follows."]),

    "scale_chooser": T(
        "tool_scale_chooser", "Double Bar Graph Scale Chooser", "manipulative",
        "A good scale makes the largest value fit while keeping bars easy to read. Each unit of length can stand for 2, "
        "4, 5, 10, 200 or more, and every bar's length is its value divided by the scale.",
        "A data table for two groups; a scale picker offering several units per length; an empty grid whose vertical "
        "line relabels as the scale changes; draggable bar tops for each category and group; a key for the two colours; "
        "a check panel showing value ÷ scale for each bar.",
        ["Look at the largest value and choose a scale that fits it on the grid.",
         "Drag each bar to its height, using value ÷ scale.",
         "Add the key for the two colours.",
         "Answer the question below the graph from the finished bars."],
        ["Superpower choices, Grade 5 and Grade 9: largest count 13, a scale of 1 unit = 2 children fits.",
         "Jodhpur temperatures at 8 times on two days, scale 1 unit = 4 °C: 43 °C is 10.75 units.",
         "Sports watched and played: largest 1240, a scale of 1 unit = 200 people.",
         "Pen, eraser, palm, box and notebook, estimate and measure, scale 1 unit = 5 cm.",
         "Onion prices in two towns, scale 1 unit = 10 rupees.",
         "Choose a scale for values up to 96 rockets so that the grid has at most 10 lines."],
        ["A scale that makes the tallest bar run off the grid is refused, with the overflowing bar shown.",
         "A bar at the wrong height shows its value ÷ scale beside the bar.",
         "A graph without a key shows the two colours blinking until a key is added."],
        "All six graphs are drawn with a fitting scale and a key, and each question is answered.",
        ["scale", "bars", "keyAdded", "answers"],
        ["M_SCALE_IGNORE"],
        ["What is the largest value? Your vertical line must reach it.",
         "Try a scale where the largest value needs about 5 to 10 units.",
         "Bar length = value ÷ scale; for 43 °C with 1 unit = 4 °C that is 10.75 units.",
         "A scale is chosen and the bars are drawn for you. A new data set follows."]),

    "claim_bins": T(
        "tool_claim_bins", "Justified Claim Sorter", "manipulative",
        "A statement about data is justified only when the data shows it; averages describe groups, not every member; "
        "and data says nothing about cases it does not include. Each claim is decided by pointing to the cells that "
        "settle it.",
        "A table of average heights by age and year; a stack of claim cards; three bins, Justified, Not justified and "
        "Cannot tell; when a card is held, the table cells it mentions can be tapped to highlight them; a reason strip.",
        ["Read the claim and tap the table cells it compares.",
         "Compare the highlighted cells.",
         "Drop the card in Justified, Not justified or Cannot tell.",
         "Pick the reason: the cells show it, the cells contradict it, it is about every individual, or the data does "
         "not cover it."],
        ["13-year-old girls in 1989 are taller on average than 14-year-old girls in 2009 (not justified: 143.2 "
         "against 148).",
         "15-year-old boys in 2019 are taller on average than 16-year-old boys in 1989 (justified: 159 against 158.9).",
         "All girls aged 13 are taller than all girls aged 11 (not justified: averages only).",
         "At every age 5 to 19, boys are taller on average than girls (not justified: ages 11 and 12).",
         "Boys keep growing beyond 19 (cannot tell: the table stops at 19).",
         "Average heights at every age rose from 1989 to 2019 (justified)."],
        ["A card in the wrong bin returns with the deciding cells highlighted.",
         "A right bin with a wrong reason asks for the reason again.",
         "Tapping cells that the claim does not mention shows the claim's words underlined to match."],
        "All six claims are sorted with the right reason.",
        ["card", "highlightedCells", "bin", "reason"],
        ["M_AVERAGE_ALL"],
        ["Which age, which year and which group does the claim talk about?",
         "Find those cells and compare the two numbers.",
         "If the claim is about every child, or about an age not in the table, the averages cannot decide it.",
         "The deciding cells are highlighted and the card is placed for you. A new claim follows."]),

    "baseline": T(
        "tool_baseline", "Zoomed Axis Bar Comparer", "simulation",
        "When an axis starts above zero, bar lengths show differences above the starting value, so a bar can look twice "
        "as long without its value being twice as big. Reading the values from the axis gives the true comparison.",
        "Two bars or markers on a chart with a slider for the axis's starting value; live readouts of each length above "
        "the axis, the length ratio and the true value ratio; a prediction box for how many times taller one looks.",
        ["Predict how many times taller the first bar looks.",
         "Slide the starting value from 0 up to the zoomed value and watch the lengths change.",
         "Compare the length ratio with the true value ratio.",
         "Read the values from the axis and state the true comparison."],
        ["Heights 165 and 155 cm with the axis from 145: looks 2 times, truly about 1.06 times.",
         "The same heights with the axis from 0: looks about 1.06 times.",
         "Heights 160 and 150 cm with the axis from 145: looks 3 times, truly about 1.07 times.",
         "Points 12.5 and 4.5 with the axis from 0: truly about 2.78 times.",
         "Skyscrapers 300 and 86 with the axis from 0: about 3.49 times.",
         "Choose a starting value that makes a 10 cm difference visible but say the true ratio."],
        ["A prediction far from the length ratio shows both lengths measured from the axis.",
         "The true ratio appears beside the length ratio whenever the axis starts above zero.",
         "Moving the axis to 0 shows the honest picture next to the zoomed one."],
        "All six comparisons are predicted and checked, and the true ratio is stated for each.",
        ["axisStart", "values", "lengthRatio", "trueRatio", "prediction"],
        ["M_BASELINE", "M_SCALE_IGNORE"],
        ["Where does the vertical line start?",
         "Measure each bar from where the line starts, not from zero.",
         "The true comparison divides the values themselves, read from the axis.",
         "The lengths and the true ratio are shown for you. A new pair follows."]),
}
