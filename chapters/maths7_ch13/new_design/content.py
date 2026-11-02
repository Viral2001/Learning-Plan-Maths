# -*- coding: utf-8 -*-
"""Chapter-level content for Class 7 Chapter 13, Connecting the Dots... (Ganita Prakash Grade 7 Part II, Chapter 5).
Book lines elsewhere are verbatim except: the book's dashes become commas, colons or "to"; minus is U+2212;
a dash that stands for a missing value is written "no entry". Every number was recomputed in Python
(fractions and statistics); where the book prints a slip, the plan teaches the correct value (see ERRATA)."""
from __future__ import annotations

CHAPTER = {
    "grade": 7,
    "label": "Class 7",
    "chapter_no": 13,
    "name": "Connecting the Dots...",
    "book_part": "Ganita Prakash Grade 7 Part II, Chapter 5",
    "source_pdf": "textbooks/class7/gegp205.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Questions and Representative Values",
     "Statistical questions and statements, comparing two batters, and the mean (average) as a fair share that "
     "levels unequal amounts."),
    ("M2", "Describing Data: Dot Plots, Outliers and the Median",
     "Onion prices summarised by maximum, total, range and a dot plot; outliers that pull the mean; the median as "
     "the middle value; comparing groups; and when zero, a blank or an average itself misleads."),
    ("M3", "Visualising Data",
     "Double (clustered) bar graphs with a chosen scale: onion prices, rocket launches, hours of daylight in two "
     "cities and the runs scored in each over of a cricket match."),
    ("M4", "Data Detective",
     "Testing claims about heights against dot plots, a table of average heights and a chart, and seeing why a "
     "decision built on an average alone can go wrong."),
    ("M5", "Review",
     "A lock puzzle that connects clues, and a closing summary of the chapter."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter follows the book's order: questions that expect varied answers, one number that stands "
             "for a group, pictures of data, and claims to test. Every story is a video that stops on a question "
             "the student answers first, and an interactive tool appears only where handling the data is the idea "
             "itself.",
    "points": [
        {"title": "Guess first, then measure",
         "text": "The hook leaves the teacher's two friends, five feet and six feet tall, as an open guess. The words "
                 "statistical question, mean and median arrive only after the student has felt why one value cannot "
                 "settle it."},
        {"title": "One concept, one video",
         "text": "Each idea gets its own topic: concept videos, one per concept, a closing practice concept (with a "
                 "tool where moving the data is the idea), then the book's Figure it Out questions in their own topic, "
                 "one question and one video per concept."},
        {"title": "Mean and median side by side",
         "text": "The mean shares the total equally; the median is the middle of the sorted values. Outliers, zeros "
                 "and blanks show when each one tells the truth about a group."},
        {"title": "Read the picture, then test the claim",
         "text": "Every graph is read with its scale first. Claims are sorted as true, false or not decidable from "
                 "the data, and the reason is always the data itself."},
    ],
}

NCERT_ITEMS = [
    "opening",
    # 5.1
    "5.1.statements", "5.1.questions_def", "5.1.mathtalk_statq",
    # 5.2 representative values
    "5.2.series1", "5.2.series2", "5.2.mathtalk_single", "5.2.mean_def", "5.2.fair_share", "5.2.hibiscus",
    "5.2.history_samamiti",
    "5.2.FiO1_1", "5.2.FiO1_2", "5.2.FiO1_3", "5.2.FiO1_4", "5.2.FiO1_5",
    "5.2.onions_opinions", "5.2.onions_measures", "5.2.dotplot", "5.2.dotplot_questions", "5.2.averages_around",
    "5.2.family_height", "5.2.outlier_def", "5.2.bookworm", "5.2.median_def", "5.2.same_page",
    "5.2.mathtalk_mean_median", "5.2.central_tendency",
    "5.2.grade5_heights", "5.2.minute",
    "5.2.zero_median", "5.2.zero_blank", "5.2.mangoes", "5.2.mean_foot",
    "5.2.FiO2_1", "5.2.FiO2_2", "5.2.FiO2_3", "5.2.FiO2_4", "5.2.FiO2_5", "5.2.FiO2_6", "5.2.FiO2_7",
    # 5.3 visualising
    "5.3.onion_graphs", "5.3.rockets", "5.3.rockets_more", "5.3.daylight_daily", "5.3.daylight_graph",
    "5.3.midnight_sun", "5.3.cricket",
    "5.3.FiO3_1", "5.3.FiO3_2", "5.3.FiO3_3", "5.3.FiO3_4",
    # 5.4 data detective
    "5.4.tall_tales", "5.4.india_table", "5.4.india_growth", "5.4.countries", "5.4.mean_decision",
    "5.4.end1", "5.4.end2", "5.4.end3", "5.4.end4", "5.4.end5", "5.4.end6", "5.4.end7", "5.4.end8", "5.4.end9",
    "5.4.end10", "5.4.end11", "5.4.end12", "5.4.end13",
    "puzzle.lock", "summary",
]

MISCONCEPTIONS = [
    ("M_ONE_ANSWER", "A statistical question has one fixed answer, like a question about one person or one object."),
    ("M_TOTAL_COMPARE", "Groups of different sizes can be compared by their totals."),
    ("M_HIGHEST_BEST", "The single highest value tells who is better or which group is larger."),
    ("M_MEAN_IN_DATA", "The mean must be one of the values in the data."),
    ("M_MEDIAN_UNSORTED", "The median is the middle value of the list as written, without sorting."),
    ("M_EVEN_MEDIAN", "With an even number of values there is no median, or it is either middle value."),
    ("M_OUTLIER_IGNORE", "An outlier changes the mean and the median by the same amount."),
    ("M_ZERO_BLANK", "A zero and a missing value are the same, so both are left out (or both are counted)."),
    ("M_MEAN_ALWAYS", "The mean is always the best single number to describe a group."),
    ("M_SCALE_IGNORE", "Bar heights can be read without checking the scale, or one unit always means one."),
    ("M_AVERAGE_ALL", "If the average of a group is higher, every member of that group is higher."),
    ("M_BASELINE", "On a chart whose axis does not start at zero, bar lengths still compare in the true ratio."),
]

SOLUTION_NOTES = [
    "Shubman's second series: 23 + 7 + 10 + 52 + 18 = 110 runs in 5 matches, and 110 ÷ 5 = 22 runs per match (the "
    "book prints 21). Yashasvi: 26 + 53 + 2 + 15 = 96 runs in 4 matches, 96 ÷ 4 = 24.",
    "Nikhil and Sunil both total 122 seconds in 7 races, so both means are 122 ÷ 7 ≈ 17.43 seconds.",
    "Rintu's 29 date palms: total 1621, mean ≈ 55.9 feet, median 56 feet, 13 trees shorter than the mean.",
    "City 1 daylight in June: 564 ÷ 30 = 18.8 hours a day; the book's picture reading says about 17 to 18.",
    "The lock puzzle has exactly one answer, 415, with or without repeated digits.",
    "Final question 2: team C played 3 games, so its mean is 32 ÷ 3 ≈ 10.67; team B's 0 is a real game, so B's "
    "mean is 18 ÷ 4 = 4.5; team A's mean is 50 ÷ 4 = 12.5.",
]
ERRATA = [
    "Book prints 110 ÷ 5 = 21 for Shubman's second series; the correct value is 22. The plan teaches 22.",
    "Book's Telling Tall Tales dot plots print the same boys' mean, 156.14, for School B Grades 7 and 8; the plan "
    "quotes the printed values and notes the repeat as a possible slip.",
    "Book misspells palm as 'plam' in final question 9; the plan writes palm.",
    "Book says City 1 daylight peaks at about 17 to 18 hours in June; the table gives 564 ÷ 30 = 18.8. The plan "
    "teaches 18.8 and calls the book's figure a reading of the bar.",
    "Book's onion story has Vishal say Wahapur has 3 numbers in the 50s; each town has 2 (Wahapur 53 and 52, "
    "Yahapur 56 and 59). The plan quotes the child's claim and corrects the count.",
    "Book's Grade 5 whole class dot plot prints mean 144.4; the data gives 4046 ÷ 28 = 144.5. The plan teaches 144.5.",
    "Book's minute estimate dot plot prints mean 59.28 for the second group; the data gives 1660 ÷ 28 ≈ 59.29. The "
    "plan teaches 59.29.",
    "Book's cricket graph read bar by bar gives the red team 152 and the blue team 163, which does not fit a red win "
    "after 18 overs; the plan teaches the book's intended reading (red stopped early, so red chased and won) and "
    "does not quote totals.",
    "Book's Grade 5 second section dot plot: the boys' points read 18 dots but the printed mean 142.05 and median 143 "
    "need 19 boys (a second dot at 142 hidden behind the mean line). The plan uses the printed statistics.",
]

DESIGN_REFERENCES = [
    {"text": "docs/25_new_design_learning_plan_playbook.md: framing intro, idea topics ending in a practice concept, "
             "a question topic after each idea topic, and one summary topic; the Class 7 Chapter 10 plan for one "
             "video per concept and one question per concept.", "url": ""},
]

FIGURES = {
    "T5.C2": ["Dot plot of monthly onion prices, axis 10 to 60: Yahapur in green, Wahapur in purple."],
    "T6.C1": ["Two dot plots of family heights on an axis from 115 to 175 cm."],
    "T9.C1": ["Double column graph of monthly onion prices in two towns, scale 1 unit = 10 rupees."],
    "T9.C2": ["Clustered bar graph of rocket launches by ten organisations in 2021, 2022 and 2023, scale 1 unit = 20."],
    "T10.C2": ["Clustered graph of average daily daylight in two cities for each month, scale 1 unit = 5 hours."],
    "T11.C1": ["Runs scored in each over by two teams, scale 1 unit = 5 runs, wickets marked as circles."],
    "T12.C1": ["Dot plots of heights of boys and girls of Grades 6, 7 and 8 in two schools."],
    "T13.C1": ["Chart of average heights of 19 year olds in several countries, 1989 and 2019, axis starting at 145 cm."],
    "T7.C2": ["Dot plots of minute estimates for two groups with mean and median lines."],
    "T8.C4": ["Empty dot plot for the palm tree heights; empty dot plot for newborn weights; dot plots of a second "
              "Grade 5 section with mean and median lines."],
    "T11.C2": ["Infographic of animal top speeds in air, on land and in water; clustered bar graph of electric "
               "vehicle registrations with Gujarat and Delhi left blank."],
    "T13.C3": ["Dot plots of pockets for boys and girls; bar chart of cities with most skyscrapers; empty dot plot "
               "for the puzzle solving times."],
}

# chapter-local (read by build.py): an image a Figure it Out question is read from, by image spec key, and the
# book item it serves. build.py moves the image into that item's concept after QT.apply.
IMAGE_FOR_ITEM = {
    "T8.C4.IMG1": "5.2.FiO2_6",
    "T8.C4.IMG2": "5.2.FiO2_5",
    "T8.C4.IMG3": "5.2.FiO2_3",
    "T11.C2.IMG1": "5.3.FiO3_1",
    "T11.C2.IMG2": "5.3.FiO3_4",
    "T13.C3.IMG1": "5.4.end1",
    "T13.C3.IMG2": "5.4.end8",
    "T13.C3.IMG3": "5.4.end10",
}
