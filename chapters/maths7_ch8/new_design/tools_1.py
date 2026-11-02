# -*- coding: utf-8 -*-
"""Tool specs for the multiplication topics T2 and T3."""
from topics_common import T

TOOLS = {
    "fraction_distance_strip": T(
        "tool_fraction_distance_strip", "Fraction of a Journey Strip", "manipulative",
        "A fraction of an hour covers that fraction of the distance in one hour: cut the distance of one hour into "
        "equal parts by the denominator, then take as many parts as the numerator.",
        "A strip for the distance in 1 hour, with a whole number of kilometres from 1 to 8; a slider for the time as "
        "a fraction with a denominator from 2 to 8 and a numerator from 1 to 8; the strip is cut into equal parts "
        "and the chosen parts are shaded; the product is written beside it as a fraction and as a mixed fraction.",
        ["Predict whether the distance is more or less than the distance in one hour.",
         "Set the distance for one hour and the time fraction.",
         "Watch the strip cut into equal parts and the numerator's worth of parts shaded.",
         "Read the total distance and check it against the prediction."],
        ["3 km in 1 hour, time 1/5 hour (3/5 km).",
         "3 km in 1 hour, time 2/5 hour (6/5 km).",
         "5 km in 1 hour, time 3/4 hour (15/4 km).",
         "7 km in 1 hour, time 1/2 hour (7/2 km).",
         "Set the time to 5/4 hour and say why the strip needs a second strip.",
         "Find two different times that give the same distance for 6 km in 1 hour."],
        ["Each time is checked against the number of parts shaded.",
         "A prediction that ignores whether the time is below or above 1 hour is questioned.",
         "A numerator bigger than the denominator adds a second strip."],
        "Five distances are found and the strip is used to explain a time above 1 hour.",
        ["distancePerHour", "timeNumerator", "timeDenominator", "partsShaded", "totalDistance", "cardIndex"],
        ["M_WHOLE_ONLY_TOP"],
        ["Is the time more or less than 1 hour?",
         "Cut the strip into as many equal parts as the denominator of the time.",
         "Shade as many of those parts as the numerator and write them as a fraction of a kilometre.",
         "The strip shows the parts; the next time has a different denominator."]),
    "unit_square_product": T(
        "tool_unit_square_product", "Unit Square Product Maker", "manipulative",
        "To find a fraction of a fraction, cut the unit square into rows for one denominator and columns for the "
        "other; the shaded parts over all the parts is the product.",
        "A unit square with sliders for two fractions, each with a denominator from 2 to 8 and a numerator up to the "
        "denominator; the first fraction shades columns, the second shades rows; the overlap is coloured; counters "
        "show the number of overlap parts, the number of all parts and the product as a fraction.",
        ["Predict the number of equal parts the unit square will have.",
         "Set the first fraction and see its columns shaded.",
         "Set the second fraction and see its rows shaded; the overlap is the product.",
         "Read the product and write it as numerator and denominator."],
        ["1/3 × 1/5 (15 parts, 1 shaded).",
         "1/4 × 1/3 (12 parts, 1 shaded).",
         "1/5 × 1/2 (10 parts, 1 shaded).",
         "2/3 × 4/5 (15 parts, 8 shaded).",
         "3/4 × 2/5 (20 parts, 6 shaded).",
         "Explain why 1/12 × 1/18 has 216 parts, without drawing."],
        ["The overlap is counted part by part against the product written.",
         "A product written by adding the numerators or denominators is shown not to match the overlap.",
         "The largest case is asked as a prediction first."],
        "Five products are found from the overlap and the 216 parts of 1/12 × 1/18 are explained.",
        ["firstNumerator", "firstDenominator", "secondNumerator", "secondDenominator", "overlapParts", "allParts",
         "cardIndex"],
        ["M_ADD_ACROSS"],
        ["How many rows and how many columns will the unit square have?",
         "The number of rows is one denominator and the number of columns is the other denominator.",
         "Count the overlap parts for the top and all the parts for the bottom.",
         "The overlap and the total are on the counters; a similar pair follows."]),
}
