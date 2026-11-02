# -*- coding: utf-8 -*-
"""Tool specs for module M2 (dividing decimals)."""
from topics_common import T

TOOLS = {
    "point_shifter": T(
        "tool_point_shifter", "Decimal Column Drop Chart", "manipulative",
        "Dividing by 10, 100 or 1000 moves every digit to a place one tenth, one hundredth or one thousandth as big, "
        "so the decimal point moves left by as many places as the divisor has zeroes.",
        "A place value chart from Thousands to Ten-thousandths; digit tiles for the dividend; buttons ÷ 10, ÷ 100, "
        "÷ 1000 and ÷ 10000; the student slides the tiles right across the chart; zero tiles fill empty places.",
        ["Predict the quotient before sliding.",
         "Count the zeroes in the divisor.",
         "Slide the digit tiles that many places to the right in the chart, so the point moves left.",
         "Add zero tiles in front when places are empty."],
        ["21.1 ÷ 10, 100, 1000, 10000 (2.11, 0.211, 0.0211, 0.00211).",
         "0.13 ÷ 10, 100, 1000, 10000 (0.013, 0.0013, 0.00013, 0.000013).",
         "214.6 ÷ 10, 100, 1000, 10000 (21.46, 2.146, 0.2146, 0.02146).",
         "58 ÷ 10, 100, 1000, 10000 (5.8, 0.58, 0.058, 0.0058).",
         "3.9 cm in metres (0.039 m)."],
        ["Tiles slid the wrong way show the result as a multiplication instead.",
         "A missing zero tile is flagged by reading the number aloud by place value.",
         "A correct row is checked by multiplying back by the divisor."],
        "Four rows of the table are complete and the ribbon length is converted.",
        ["dividend", "divisor", "shift", "zerosAdded", "rowIndex"],
        ["M_POINT_WRONG_WAY", "M_MISSING_ZERO"],
        ["Is the quotient bigger or smaller than the dividend?",
         "Each zero in the divisor moves the point one place left.",
         "Count the zeroes and move the point that many places; fill gaps with zeroes.",
         "The chart shows every digit one place, two places or three places lower; a similar row follows."]),

    "regrouping_tray": T(
        "tool_regrouping_tray", "Regrouping Tray Long Division", "manipulative",
        "In long division a remainder in the Ones is regrouped into Tenths, the Tenths into Hundredths and so on, so the "
        "division carries on past the Ones; the decimal point in the quotient appears when Ones become Tenths.",
        "Place value blocks (Hundreds, Tens, Ones, Tenths, Hundredths, Thousandths) and a set of equal groups; a "
        "Regroup button breaks one block into 10 of the next smaller size; the long division written step by step "
        "beside the tray.",
        ["Share the largest blocks first among the groups.",
         "Regroup what is left into the next smaller blocks and share again.",
         "Mark the decimal point in the quotient when Ones are regrouped into Tenths.",
         "Stop when nothing is left over."],
        ["1325 ÷ 4 (331.25).", "14.4 ÷ 4 (3.6).", "415 ÷ 4 (103.75).", "1217 ÷ 2 (608.5).",
         "4827 ÷ 8 (603.375).", "0.06 ÷ 5 (0.012)."],
        ["Stopping with a remainder in the Ones prompts a Regroup.",
         "A quotient point placed in the wrong spot is shown against the blocks in each group.",
         "A missing zero place holder is shown as an empty Tenths column in each group."],
        "All six divisions are shared out with no blocks left over.",
        ["dividend", "divisor", "groups", "leftover", "quotientDigits", "pointPlaced", "cardIndex"],
        ["M_REMAINDER_STOP", "M_POINT_IN_QUOTIENT", "M_MISSING_ZERO"],
        ["How many blocks of the largest size can each group get?",
         "Whatever is left is regrouped into blocks one tenth as big.",
         "Regroup the leftover Ones into Tenths and write the decimal point in the quotient.",
         "The tray shares the next blocks and shows the long division line; a similar card follows."]),

    "divisor_clearer": T(
        "tool_divisor_clearer", "Same Stretch Divisor Clearer", "manipulative",
        "Multiplying the dividend and the divisor by the same 10, 100 or 1000 does not change the quotient, so a "
        "decimal divisor can be turned into a whole number before dividing.",
        "A fraction frame with the dividend on top and the divisor below; a × 10 button that multiplies top and bottom "
        "together; a lock that refuses to multiply only one of them; a long division panel once the divisor is whole.",
        ["Predict whether the quotient is bigger or smaller than the dividend.",
         "Press × 10 until the divisor is a whole number.",
         "Divide the new whole-number pair by long division.",
         "Check by multiplying the quotient by the original divisor."],
        ["12.6 ÷ 0.25 (50.4).", "46.8 ÷ 1.3 (36).", "2 ÷ 5 (0.4).", "13 ÷ 4 (3.25).",
         "12.43 ÷ 0.6 (20.71666...).", "1.872 ÷ 0.1 (18.72)."],
        ["Multiplying only the divisor is blocked with a reminder that the fraction would change.",
         "Each press of × 10 shows the new fraction equal to the old one.",
         "A quotient that fails the check is shown against the original division."],
        "Six divisions are cleared and solved, each with a check.",
        ["dividend", "divisor", "scale", "quotient", "checked", "cardIndex"],
        ["M_DIVISOR_ONLY", "M_QUOTIENT_SMALLER"],
        ["Is the divisor a whole number yet?",
         "Multiply the dividend and the divisor by the same 10 or 100.",
         "Use the power of 10 that clears every decimal place in the divisor, then divide.",
         "The cleared division and its long division are shown; a similar card follows."]),

    "remainder_cycle_tracker": T(
        "tool_remainder_cycle_tracker", "Remainder Cycle Tracker", "simulation",
        "In a long division by a whole number every remainder is less than the divisor, so a remainder must repeat "
        "within that many steps, and the quotient digits then repeat for ever.",
        "A long division that runs one step per tap; a ring of slots numbered 0 up to one less than the divisor; each "
        "new remainder lights its slot; a repeat lights the ring and the repeating digits are underlined.",
        ["Predict whether the division will end.",
         "Tap to run one step and note the remainder.",
         "Watch for a remainder that has already lit up.",
         "Name the block of digits that repeats."],
        ["10 ÷ 3 (3.333..., remainder 1 repeats).", "10 ÷ 9 (1.111...).", "100 ÷ 11 (9.0909...).",
         "1 ÷ 7 (0.142857 repeating, remainders 1, 3, 2, 6, 4, 5).", "1 ÷ 17 (sixteen repeating digits).",
         "13 ÷ 4 (3.25, ends with remainder 0)."],
        ["A claim that a division ends is tested by running to the first repeat or to remainder 0.",
         "A remainder equal to or bigger than the divisor is flagged as a missed quotient digit.",
         "The first repeated remainder is highlighted with the step where it first appeared."],
        "Each division is classed as ending or repeating, with its repeating block named.",
        ["dividend", "divisor", "remainders", "digits", "repeatAt", "ends", "cardIndex"],
        ["M_EVERY_DIVISION_ENDS", "M_REMAINDER_STOP"],
        ["What remainders are possible when dividing by this number?",
         "If a remainder comes back, the same steps follow again.",
         "Keep dividing and list the remainders until one repeats or one is 0.",
         "The remainder ring shows the repeat and the repeating digits; a similar card follows."]),

    "quotient_size_predictor": T(
        "tool_quotient_size_predictor", "Divisor Size Quotient Predictor", "simulation",
        "Dividing by a number greater than 1 gives a quotient smaller than the dividend; dividing by a number between 0 "
        "and 1 gives a quotient bigger than the dividend.",
        "A dividend bar; a divisor slider from 0.1 to 10 with 1 marked; the quotient bar redrawn as the slider moves; "
        "bins labelled quotient bigger than dividend, equal, smaller.",
        ["Bin each card before dividing.",
         "Move the divisor across 1 and watch the quotient bar.",
         "Press Check to see the quotient.",
         "Explain the bin with how many divisors fit into the dividend."],
        ["128 ÷ 4 (32, smaller).", "128 ÷ 0.4 (320, bigger).", "2.4 ÷ 0.003 (800, bigger).",
         "1.872 ÷ 0.1 (18.72, bigger).", "15.6 ÷ 0.1 (156, bigger).", "12.5 ÷ 2.5 (5, smaller)."],
        ["A wrong bin replays the division as how many divisors fit inside the dividend.",
         "A quotient bar that crosses the dividend bar is pointed out as the divisor passes 1.",
         "A correct bin is confirmed with the quotient value."],
        "Six cards are binned correctly with the quotient checked.",
        ["dividend", "divisor", "chosenBin", "quotient", "cardIndex"],
        ["M_QUOTIENT_SMALLER"],
        ["Is the divisor greater than 1 or less than 1?",
         "Count how many of the divisor fit into the dividend.",
         "A divisor below 1 fits more times than the dividend itself.",
         "The bars show the quotient against the dividend; a similar card follows."]),
}
