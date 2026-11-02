# -*- coding: utf-8 -*-
"""Tool specs for module M3 (comparing, adding and subtracting decimals): T10, T11, T12."""
from topics_common import T

TOOLS = {
    "place_by_place_comparator": T(
        "tool_place_by_place_comparator", "Place by Place Comparator", "manipulative",
        "Two decimals are compared by lining up their places and reading from the left: the first place where the "
        "digits differ decides which is greater, and zeroes at the end of the decimal part change nothing.",
        "Two number cards set on a shared place chart with columns from Tens to Thousandths; a glowing marker that "
        "moves left to right along the columns; a verdict box; a closeness meter showing the gap between each "
        "decimal and a target number.",
        ["Drop both numbers on the chart so their decimal points line up.",
         "Move the marker from the left until the digits differ.",
         "Say which number is greater and why.",
         "Switch to closeness mode and find the number nearest to the target."],
        ["6.456 and 6.465 (6.465 is greater).",
         "1.009 and 1.090 (1.090 is greater).",
         "3.81 and 13.800 (13.800 is greater).",
         "0.2, 0.20 and 0.200 (all equal).",
         "Closest to 1 among 0.9, 1.1, 1.01 and 1.11 (1.01).",
         "Closest to 4 among 3.56, 3.65 and 3.099 (3.65)."],
        ["Comparing the digits after the point as whole numbers is shown on the chart: 0.9 is 9 tenths, "
         "while 0.12 is 1 tenth and 2 hundredths.",
         "A longer decimal chosen as greater is tested by padding the shorter one with zeroes.",
         "A closeness answer chosen by first digit is checked on the closeness meter."],
        "Six comparisons and closeness questions are answered with the deciding place named.",
        ["numberA", "numberB", "deciderPlace", "verdict", "target", "gapA", "gapB", "cardIndex"],
        ["M_MORE_DIGITS_BIGGER", "M_RIGHT_ZERO", "M_TWO_WHOLE", "M_FIRST_DIGIT"],
        ["Are the points lined up, and which digit comes first on the left?",
         "Compare place by place from the left and stop at the first place where the digits differ.",
         "That place decides: the bigger digit there means the greater number.",
         "The marker stops at the deciding column and the verdict is shown; a similar card follows."]),

    "point_aligned_addition_column": T(
        "tool_point_aligned_addition_column", "Point Aligned Addition Column", "manipulative",
        "Decimals are added like whole numbers once their decimal points are in one vertical line, so that tenths "
        "are added to tenths, hundredths to hundredths, and each ten in a place carries to the place on its left.",
        "A vertical addition frame with a fixed decimal point column; digit tiles for two addends that snap into "
        "place columns; carry boxes above each column; an estimate bar that shows the sum of the whole number parts "
        "and that sum plus 2.",
        ["Predict the sum: write the whole number parts and their total.",
         "Snap the two numbers into the frame with the points lined up.",
         "Add column by column from the right, carrying when a column reaches ten.",
         "Check the sum lies in the estimate range."],
        ["2.7 + 3.5 (6.2).",
         "75.345 + 86.691 (162.036).",
         "18 + 8.8 (26.8).",
         "9.01 + 9.10 (18.11).",
         "0.934 + 0.6 (1.534).",
         "6.236 + 0.487 (6.723)."],
        ["Numbers lined up at the right end instead of the point are flagged by the tile columns.",
         "A missed carry is shown by a column that holds ten or more.",
         "A sum outside the estimate range is highlighted against the estimate bar."],
        "Six sums are done with the points lined up and every carry shown.",
        ["addendA", "addendB", "carries", "estimateLow", "estimateHigh", "sum", "cardIndex"],
        ["M_POINT_ALIGN", "M_EST_RANGE"],
        ["Are the decimal points one under the other?",
         "Start at the smallest place on the right and carry any ten to the next place.",
         "Add tenths to tenths and hundredths to hundredths; the point stays where it was.",
         "The column adds step by step and the carries are drawn; a similar card follows."]),

    "zero_filled_subtraction_column": T(
        "tool_zero_filled_subtraction_column", "Zero Filled Subtraction Column", "manipulative",
        "Decimals are subtracted like whole numbers once the points are lined up and the shorter number is filled "
        "with zeroes on the right, because a zero at the end of a decimal changes nothing.",
        "A vertical subtraction frame with a fixed decimal point column; digit tiles for the two numbers; ghost "
        "zero tiles that fill the shorter number; borrow arrows between neighbouring places; an estimate bar for the "
        "range the difference must lie in.",
        ["Predict the difference from the whole number parts.",
         "Line up the points and fill the shorter number with zero tiles.",
         "Subtract from the right, borrowing from the next place when a digit is too small.",
         "Check the difference lies in the estimate range."],
        ["3.5 − 2.7 (0.8).",
         "84.691 − 77.345 (7.346).",
         "17 − 16.198 (0.802).",
         "17 − 0.05 (16.95).",
         "34.505 − 18.1 (16.405).",
         "9.9 − 9.09 (0.81)."],
        ["Subtracting the smaller digit from the larger in each place is shown by the borrow arrows.",
         "A missing zero tile in the shorter number is shown as a gap in the column.",
         "A difference outside the estimate range is highlighted against the estimate bar."],
        "Six differences are found with every borrow drawn and the range check passed.",
        ["minuend", "subtrahend", "zerosFilled", "borrows", "estimateLow", "estimateHigh", "difference", "cardIndex"],
        ["M_POINT_ALIGN", "M_BORROW_ONE", "M_RIGHT_ZERO"],
        ["Are the points in one line, and does the lower number have as many places as the upper?",
         "Fill the short number with zeroes, then start from the right.",
         "If a digit is too small, borrow one from the left; it becomes ten in this place.",
         "The column shows each borrow and the digits subtract; a similar card follows."]),
}
