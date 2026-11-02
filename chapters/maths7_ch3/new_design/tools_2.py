# -*- coding: utf-8 -*-
"""Tool specs for module M2 (decimal notation and units) and the number line zoom (T7, T8, T9)."""
from topics_common import T

TOOLS = {
    "place_chart_decimal_writer": T(
        "tool_place_chart_decimal_writer", "Place Chart to Decimal Writer", "manipulative",
        "A decimal is the place value chart written without its headings: each digit sits in a place worth ten times "
        "the place to its right, and the decimal point marks where the units end.",
        "A place chart with columns for Hundreds, Tens, Units, Tenths, Hundredths and Thousandths; digit cards to "
        "drop into the columns; a movable decimal point that sits after the Units column; a read-out that writes the "
        "number and says it aloud as digits after the point.",
        ["Read the quantity and drop each digit into its column.",
         "Put a zero in every empty column between the digits.",
         "Place the decimal point after the Units column and read off the number.",
         "Read it aloud, saying each digit after the point on its own."],
        ["2 ones, 3 tenths and 5 hundredths (2.35).",
         "1 ten and 5 tenths (10.5).",
         "4 ones and 6 hundredths (4.06).",
         "1 hundred, 1 one and 1 hundredth (101.01).",
         "234 tenths (23.4) and 234 hundredths (2.34).",
         "2 1/100, 4 1/10 and 7 7/1000 (2.01, 4.1, 7.007)."],
        ["A missing zero column is shown by reading the number back: 4.6 is 4 ones and 6 tenths, not 6 hundredths.",
         "A point placed at the wrong column is shown by reading the place value of the first digit after it.",
         "A count of tenths dropped as digits in the Units column is flagged by the place headings."],
        "Six quantities are written and read aloud correctly.",
        ["quantity", "digitsPlaced", "zerosAdded", "pointPosition", "readAloud", "cardIndex"],
        ["M_READ_PLACE", "M_TWO_WHOLE"],
        ["Which columns does the quantity use, and which are empty?",
         "Every empty column between two digits needs a zero.",
         "The decimal point goes right after the Units column.",
         "The chart shows the number with the heading of each digit and reads it aloud; a similar card follows."]),

    "exchange_rate_step_counter": T(
        "tool_exchange_rate_step_counter", "Exchange Rate Step Counter", "manipulative",
        "Changing a unit to a smaller or bigger one multiplies or divides by 10, 100 or 1000, so the decimal point "
        "moves right or left by as many places as the exchange rate has zeroes.",
        "A step ladder of units, with millimetre, centimetre, metre and kilometre on one side, milligram, gram and "
        "kilogram on another, and paise and rupee on a third; each step labelled with its exchange rate; a number "
        "card whose decimal point slides left or right as the student climbs a step.",
        ["Choose the starting unit and the unit you want.",
         "Read the exchange rate between the two units.",
         "Climb the steps and slide the decimal point that many places.",
         "Read the new number with its new unit."],
        ["5.6 cm in millimetres (56 mm).",
         "36 cm in metres (0.36 m).",
         "254 g in kilograms (0.254 kg).",
         "250 paise in rupees (2.50 rupees).",
         "1 kilometre in millimetres (1000000 mm).",
         "45 paise for 100000 passengers in rupees (45000 rupees)."],
        ["Climbing the step the wrong way shows the quantity getting bigger when it should get smaller.",
         "A point moved too few places is checked by reading the answer back in the first unit.",
         "Two units mixed in one number are separated by the ladder before they are changed."],
        "Six conversions are made and each is checked by converting back.",
        ["startValue", "startUnit", "targetUnit", "rate", "steps", "pointShift", "cardIndex"],
        ["M_UNIT_SHIFT", "M_POINT_ALIGN"],
        ["Is the new unit smaller or bigger than the old one?",
         "A smaller unit needs more of them, so the number grows; a bigger unit needs fewer.",
         "Count the zeroes in the exchange rate and move the decimal point that many places.",
         "The ladder shows the climb and the shifted number; a similar card follows."]),

    "digit_zoom_locator": T(
        "tool_digit_zoom_locator", "Digit by Digit Zoom Locator", "manipulative",
        "Every digit of a decimal names one more zoom: the units digit picks a gap between two whole numbers, the "
        "tenths digit picks one of 10 equal parts of that gap, the hundredths digit picks one part of that part, "
        "and so on, so any decimal has its own place on the number line.",
        "A number line from 0 to 10 with a zoom window; each zoom opens the chosen gap into 10 equal parts and shows "
        "the new end marks; a decimal card with its digits lit one at a time; a stack of the lines already visited; "
        "a second mode where the student reads a marked point on a given line.",
        ["Read the first digit and zoom into that gap.",
         "Read the next digit and zoom into that tenth of the gap.",
         "Keep zooming until every digit is used, then place the marker.",
         "Switch to a given line and read the decimal at a marked point."],
        ["4.185 (zoom 4 to 5, then 4.1 to 4.2, then 4.18 to 4.19).",
         "9.876 (zoom 9 to 10, then 9.8 to 9.9, then 9.87 to 9.88).",
         "0.407 (zoom 0 to 1, then 0.4 to 0.5, then 0.40 to 0.41).",
         "A point on the line from 5 to 10 that sits 5 parts after 5, with every part half a unit (7.5).",
         "A point 5 parts after 8 on the line from 8 to 8.1 (8.05).",
         "A point on the line from 4.3 to 4.8 that sits 1 part after 4.8 when each part is 0.05 (4.85)."],
        ["A digit zoomed into the wrong gap is shown by the end marks of the new line.",
         "A line where the parts are not tenths is flagged by dividing the end gap by the number of parts.",
         "A reading that ignores the end marks of the line is checked by counting the parts again."],
        "Six decimals are located or read, each through its digit by digit zoom.",
        ["decimal", "zoomLevel", "lineStart", "lineEnd", "partsPerLine", "partChosen", "cardIndex"],
        ["M_LINE_MARKS", "M_TWO_WHOLE"],
        ["Which two whole numbers is the decimal between?",
         "Zoom into that gap: it is cut into 10 equal parts, and the next digit tells which part.",
         "Repeat for the next digit, always opening the part you chose.",
         "The zoom stack shows each line in turn and the marker lands; a similar card follows."]),
}
