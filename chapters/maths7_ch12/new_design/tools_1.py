# -*- coding: utf-8 -*-
"""Tool specs for module M1 (multiplying decimals)."""
from topics_common import T

TOOLS = {
    "decimal_place_counter": T(
        "tool_decimal_place_counter", "Decimal Place Count Multiplier", "manipulative",
        "To multiply two decimals, multiply the numbers with the points removed, then give the product as many "
        "decimal places as the two numbers have together, because the denominators 10, 100 and 1000 multiply.",
        "Two number cards with their decimal points as draggable dots; under each card a fraction strip showing the "
        "number over 10, 100 or 1000; a whole-number product bar; a product card whose decimal point the student "
        "drags into place; a place counter that adds the decimal places of the two cards.",
        ["Predict roughly how big the product is before multiplying.",
         "Remove the points and multiply the whole numbers.",
         "Count the decimal places in each card and add them.",
         "Drag the decimal point into the product, writing zeroes in front if the digits run out."],
        ["27.34 × 6 (164.04).", "4.23 × 3.7 (15.651).", "0.432 × 0.23 (0.09936).",
         "Given 18 × 12 = 216, find 0.18 × 0.12 (0.0216).", "56.50 × 2.250 against 56.5 × 2.25 (127.125 both).",
         "0.306 × 1000 (306)."],
        ["A point placed with the wrong number of places shows the fraction strip product, for example "
         "432/1000 × 23/100 = 9936/100000.",
         "A product with a missing front zero is flagged: 0.9936 is ten times too big.",
         "A size check compares the product with a rounded estimate, for example 4 × 4 = 16 near 15.651."],
        "Six products are placed correctly, each with its decimal places counted.",
        ["cardA", "cardB", "wholeProduct", "placesA", "placesB", "pointPosition", "cardIndex"],
        ["M_POINT_ALIGN", "M_TRAILING_ZERO", "M_MISSING_ZERO"],
        ["How many digits come after the point in each number?",
         "Multiply without the points, then add the two counts of decimal places.",
         "Count that many digits from the right of the whole-number product and place the point.",
         "The fraction strip shows the product over 10, 100 or 1000 and the point is placed; a similar card follows."]),

    "product_size_predictor": T(
        "tool_product_size_predictor", "Factor Size Product Predictor", "simulation",
        "Multiplying by a number greater than 1 enlarges a number; multiplying by a number between 0 and 1 shrinks it. "
        "So the size of a product can be predicted before it is found.",
        "A number line from 0 to 10 with a zoom into 0 to 1; two sliders set the numbers; three bins labelled greater "
        "than both, between the two, less than both; a check that shows the product as a marker on the line.",
        ["Place each multiplication card in a bin before multiplying.",
         "Say whether the product is less than 1.",
         "Press Check to see the product on the number line.",
         "Move a slider across 1 and watch the product switch bins."],
        ["7 × 0.6 (4.2, between).", "0.7 × 0.6 (0.42, less than both).", "0.7 × 6 (4.2, between).",
         "0.07 × 0.06 (0.0042, less than both).", "3.4 × 6.5 (22.1, greater than both).",
         "0.75 × 5 (3.75, between)."],
        ["A card in the wrong bin replays the product as a part of a number: 0.6 of 7 is less than 7.",
         "A wrong less-than-1 claim shows both numbers against 1 on the line.",
         "A correct prediction is confirmed by the marker landing inside the chosen bin."],
        "All six cards are binned correctly and each less-than-1 question is answered.",
        ["numA", "numB", "chosenBin", "lessThanOne", "product", "cardIndex"],
        ["M_PRODUCT_BIGGER"],
        ["Is each number greater than 1, or between 0 and 1?",
         "Both above 1 makes the product bigger than both; both below 1 makes it smaller than both.",
         "One of each puts the product between the two numbers.",
         "The product is shown on the line with both numbers; a similar card follows."]),
}
