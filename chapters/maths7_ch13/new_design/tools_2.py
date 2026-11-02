# -*- coding: utf-8 -*-
"""Tool specs for module M2 (dot plots, outliers and the median, zeros and blanks)."""
from topics_common import T

TOOLS = {
    "dot_plot_builder": T(
        "tool_dot_plot_builder", "Stacking Dot Plot Builder", "manipulative",
        "A dot plot puts every value on an equally spaced number line and stacks equal values, so the spread, the "
        "clusters and the extremes are visible at a glance, while the original order of the data is lost.",
        "A data strip of value chips at the top; a number line below whose start, end and step the student sets; chips "
        "dropped on the line become stacked dots; a readout panel for minimum, maximum and range that the student fills "
        "in; a toggle to show a second data set in a second colour.",
        ["Choose a start and end for the line that cover every value, with equal steps.",
         "Drag each chip to its place on the line; equal values stack upward.",
         "Read the minimum, maximum and range and type them into the readout.",
         "Turn on the second data set and say which one is more spread out."],
        ["Onion prices in the first town: 25, 24, 26, 28, 30, 35, 39, 43, 49, 56, 59, 44 (range 35).",
         "Onion prices in the second town: 19, 17, 23, 30, 38, 35, 42, 39, 53, 60, 52, 42 (range 43).",
         "Both towns together: which town has values between 11 and 20? (only the second, 17 and 19)",
         "Newspaper pages 16, 18, 20, 22, 26, 16, 10 on a line from 10 to 30 (range 16).",
         "Newborn weights 3.5, 4.1, 2.6, 3.2, 3.4, 3.8 on a line in steps of 0.1 (range 1.5).",
         "Stories read 6, 8, 5, 15, 3, 0, 2, 7, 12, 40, 10, 5, 0, 8, 1: spot the value far from the rest (40)."],
        ["A line with uneven steps is refused with the gaps highlighted, because equal spacing is what makes the "
         "picture fair.",
         "A chip dropped at the wrong place slides back to the strip with its value enlarged.",
         "A wrong range shows the two end dots joined by a bracket labelled maximum minus minimum."],
        "All six data sets are plotted correctly and each readout is right.",
        ["lineStart", "lineEnd", "step", "dots", "readout", "secondSetOn"],
        ["M_HIGHEST_BEST"],
        ["Which is the smallest value and which is the largest? Your line must reach both.",
         "Put the chips in order first; equal values go on top of each other.",
         "The range is the largest value minus the smallest value.",
         "The dots are placed for you and the range bracket is drawn. A new data set follows."]),

    "outlier_race": T(
        "tool_outlier_race", "Outlier Pull Mean Median Tracker", "simulation",
        "When one value moves far from the rest, the mean is pulled towards it because every unit counts in the total, "
        "while the median, the middle of the sorted values, hardly moves.",
        "A dot plot of a small data set with one draggable highlighted dot; two markers under the line, a triangle for "
        "the mean and a diamond for the median, that move live; a trail showing how far each marker has travelled; a "
        "prediction panel asking which marker will move further before the drag.",
        ["Predict which marker, mean or median, will move further when the highlighted dot is dragged.",
         "Drag the highlighted dot far to the right or left and watch both markers.",
         "Compare the two trails with the prediction.",
         "Remove the outlier and record the new mean and median."],
        ["Family heights 170, 173, 165, 175 and a fifth value dragged down to 118 (mean 160.2, median 170).",
         "Stories read with the top value dragged from 15 up to 40 (mean about 8.13, median 6).",
         "Newspaper pages 16, 18, 20, 22, 26, 16, 10: drag 26 to 60 and back.",
         "Seven values 20, 21, 22, 23, 24 with two dots dragged out to 2 and 45 on both sides (mean about 22.43, "
         "median 22).",
         "Even count: heights 155, 160, 164, 165, 169, 173, with 173 dragged to 200 (median stays 164.5).",
         "Predict, then check: palm heights with one tree dragged to 100 feet."],
        ["A wrong prediction replays the drag slowly with both trail lengths labelled.",
         "When the median does change, the sorted list appears with the middle value boxed to show why.",
         "Removing the outlier shows the before and after mean and median side by side."],
        "All six cases are predicted and checked, and the student states which measure resists the outlier.",
        ["values", "dragIndex", "mean", "median", "prediction", "trails"],
        ["M_OUTLIER_IGNORE", "M_MEDIAN_UNSORTED", "M_EVEN_MEDIAN"],
        ["Which marker uses every value in its calculation?",
         "Does the middle of the sorted list change when the end value moves further away?",
         "The mean is the total divided by the count, so a bigger value makes a bigger total.",
         "The trails show that the mean moved further than the median. A new case follows."]),

    "zero_blank": T(
        "tool_zero_blank", "Zero or Missing Entry Sorter", "manipulative",
        "A zero is a real value and counts in the total and the count; a missing entry, or a value outside what the "
        "question asks about, is left out of both. Choosing the data before averaging changes the mean and the median.",
        "A row of data tiles, some showing 0 and some showing no entry; each tile can be tagged Count it or Leave it out; "
        "a live panel showing the total, the count, the mean and the sorted list with the median boxed; a question "
        "banner saying what the data should describe.",
        ["Read the question banner: what is the data supposed to describe?",
         "Tag each tile Count it or Leave it out.",
         "Check the count the panel divides by, then the mean.",
         "Sort the counted values and find the median."],
        ["Runs 57, 13, 0, 84, no entry, 51, 27: divide by 6, mean about 38.67.",
         "Batters 19, 0, 0, 22, 158, 0, 184, 5, 0, 0, 0: median 0, mean about 35.27.",
         "Mangoes per month in season from 0, 0, 8, 24, 41, 16, 5, 0, 0, 0, 0, 0: count only the five summer months, "
         "mean 18.8, median 16.",
         "Pets with two absent students marked no entry: 20 values, mean 3.6, median 2.",
         "Game points 0, 8, 6, 4 where the 0 is a game played: mean 4.5.",
         "Game points 8, 11, did not play, 13: divide by 3, mean about 10.67."],
        ["A zero tagged Leave it out returns with the note that the player did play and scored 0.",
         "A no entry tagged Count it shows the count growing wrongly and the mean falling.",
         "For the mango case, the banner's words in season are highlighted when an off-season zero is counted."],
        "All six cases are tagged correctly and the mean and median match.",
        ["tiles", "tags", "total", "count", "mean", "median"],
        ["M_ZERO_BLANK"],
        ["Did this entry come from something that happened, or from nothing at all?",
         "A zero is a real result; a missing entry has no value to add.",
         "Divide by the number of tiles tagged Count it, not by the number of tiles.",
         "The tiles are tagged for you, and the mean uses only the counted values. A new case follows."]),
}
