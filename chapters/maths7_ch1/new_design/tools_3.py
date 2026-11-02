# -*- coding: utf-8 -*-
"""Tool specs for modules M5 and M6 (halve and double, digit count predictor, matchstick builder)."""
from topics_common import T

TOOLS = {
    "halve_double": T(
        "tool_halve_double", "Halve and Double", "manipulative",
        "Halving one factor and doubling another keeps the product the same, and pairing factors that make 10, 100 or "
        "1000 turns a long product into a single power of ten.",
        "A product line of factors as cards; a halve button and a double button that act on two chosen cards; a pair "
        "button that merges two cards when their product is a power of ten; a running product box that stays equal.",
        ["Predict which factors can pair to a power of ten.",
         "Choose a card and press halve, then choose another and press double.",
         "Pair cards whose product is 10, 100 or 1000.",
         "Read the final product when only one card remains."],
        ["2 × 1768 × 50 (1,76,800).", "72 × 125 (9000).", "125 × 40 × 8 × 25 (10,00,000).",
         "25 × 12 and 25 × 240 (300 and 6000).", "250 × 120 and 2500 × 12 (30,000 each).",
         "Find two numbers with the product 12,00,00,000."],
        ["A halve on an odd card is refused with a note to halve another card.",
         "A pair that does not make a power of ten is separated again with its product shown.",
         "The running product box shows the same value after every move so the idea of keeping it equal is seen."],
        "All six products are found by regrouping and the running product is the same at every step.",
        ["cards", "pairs", "runningProduct", "moves", "cardIndex"],
        ["M_SHORTCUT_ORDER"],
        ["Which two factors make 10, 100 or 1000 when multiplied?",
         "Halve one factor and double another if that helps a pair form.",
         "Pair the factors and multiply the pairs.",
         "The pairs are joined and the product is read as a number with zeros; a new product follows."]),

    "digit_count_predictor": T(
        "tool_digit_count_predictor", "Digit Count Predictor", "manipulative",
        "An m-digit number times an n-digit number has m plus n digits or one fewer, and the smallest and largest numbers of "
        "those lengths show both cases.",
        "Two digit-count pickers for the factors; a predicted digit count the student sets; the smallest product and "
        "the largest product computed from the smallest and largest numbers of those lengths and shown with their digit "
        "counts; a free multiply box to test more pairs.",
        ["Predict the digit counts of the product before the tool shows it.",
         "Pick the digit counts of the two numbers.",
         "Read the digit counts of the smallest and largest products.",
         "Try your own pair of numbers in the multiply box."],
        ["2-digit times 2-digit (3 or 4 digits).", "3-digit times 3-digit (5 or 6 digits).",
         "4-digit times 2-digit (5 or 6 digits).", "5-digit times 5-digit (9 or 10 digits).",
         "8-digit times 3-digit (10 or 11 digits).", "12-digit times 13-digit (24 or 25 digits)."],
        ["A prediction with the wrong count shows the smallest product beside it.",
         "A tested pair that lies between the smallest and the largest is placed on a bar between them.",
         "A correct answer states the rule with the two digit counts added."],
        "All six digit-count pairs are predicted correctly.",
        ["digitsA", "digitsB", "predictedLow", "predictedHigh", "smallestProduct", "largestProduct", "cardIndex"],
        ["M_DIGIT_PRODUCT"],
        ["Which numbers give the smallest product and the largest product?",
         "Count the digits of the smallest product and of the largest product.",
         "Compare with the sum of the two digit counts.",
         "The smallest and largest products are shown with their digits, and the rule is read out; a new pair follows."]),

    "matchstick_builder": T(
        "tool_matchstick_builder", "Matchstick Builder", "manipulative",
        "Each digit takes a fixed number of sticks, so the stick count of a number is the total for its digits; adding or "
        "moving sticks changes one digit into another.",
        "A calculator-style display of a number built from sticks; a stick counter; a palette of digits with their stick "
        "counts; tap a stick to remove it or add it; a total box that says how many sticks are in use.",
        ["Predict the number of sticks needed for a number.",
         "Build the number from sticks and read the stick counter.",
         "Add or move sticks to make a bigger number.",
         "Compare the result with the target stick count."],
        ["5108 (20 sticks).", "42,019 (23 sticks).", "42,019 plus two sticks to make a bigger number.",
         "63,890 with four sticks moved to make a bigger number.",
         "A number with exactly 24 sticks.", "The biggest and the smallest number with 24 sticks."],
        ["A digit shape that is not valid is shaken and the nearest valid digit is shown.",
         "The stick counter shows the count after every move.",
         "A correct bigger number is added to a list with its stick count."],
        "All six builds are done with the stick counts right.",
        ["digits", "sticks", "stickCount", "target", "foundNumbers", "cardIndex"],
        ["M_PRESS_COUNT"],
        ["How many sticks does each digit need?",
         "Add up the sticks for all the digits.",
         "To make a bigger number, change digits near the front first.",
         "The best number is shown with its sticks counted; a new puzzle follows."]),
}
