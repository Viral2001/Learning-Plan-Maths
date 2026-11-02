# -*- coding: utf-8 -*-
"""Tool specs for the cancelling, size and division topics T5 to T7."""
from topics_common import T

TOOLS = {
    "cancel_then_multiply": T(
        "tool_cancel_then_multiply", "Cancel Then Multiply", "manipulative",
        "Before multiplying two fractions, divide a numerator and a denominator by a factor they share; the product "
        "is then already in lowest form.",
        "Two fractions side by side with the numerators on top and the denominators below; any numerator can be "
        "linked to any denominator; the shared factor is shown and the pair is divided by it; the remaining numbers "
        "are multiplied at the end.",
        ["Predict which pairs of numbers share a factor.",
         "Link a numerator and a denominator and divide both by their common factor.",
         "Repeat until no pair shares a factor.",
         "Multiply what is left and read the lowest form."],
        ["12/7 × 5/24 (cancel 12 and 24, product 5/14).",
         "14/15 × 25/42 (cancel 14 with 42 and 25 with 15, product 5/9).",
         "15/4 × 48/5 (cancel 15 with 5 and 48 with 4, product 36).",
         "9/10 × 25/27 (product 5/6).",
         "8/21 × 14/16 (product 1/3).",
         "Find a pair where nothing cancels."],
        ["A link between a numerator and a denominator with no common factor is refused with the factors listed.",
         "A link between two numerators is refused, since only a top and a bottom can cancel.",
         "The final product is checked against multiplying straight across."],
        "Five products are found by cancelling and one pair with nothing to cancel is found.",
        ["leftNumerator", "leftDenominator", "rightNumerator", "rightDenominator", "links", "product", "cardIndex"],
        ["M_CANCEL_SAME_FRACTION", "M_ADD_ACROSS"],
        ["Which number on top shares a factor with a number below?",
         "List the factors of a numerator and of a denominator in the other fraction.",
         "Divide both linked numbers by the biggest factor they share.",
         "The link shows the factor; multiply what is left to see the lowest form."]),
    "product_size_predictor": T(
        "tool_product_size_predictor", "Product Size Predictor", "simulation",
        "Whether a product is greater or smaller than each number multiplied depends only on whether each number is "
        "below 1 or above 1.",
        "Two number lines from 0 to 6; a slider for each factor, with fractions; a marker for each factor and a "
        "marker for the product; labels say whether the product is greater or smaller than each factor and than 1.",
        ["Predict where the product will land.",
         "Move each slider to a fraction.",
         "Read where the product lands against both factors.",
         "State the rule for the region each factor is in."],
        ["Two numbers above 1, such as 4/3 and 4.",
         "Two numbers between 0 and 1, such as 3/4 and 2/5.",
         "One number between 0 and 1 and one above 1, such as 3/4 and 5.",
         "A number and 1 (the product equals the other number).",
         "565/465 and 707/676 (both above 1).",
         "Find a pair whose product is smaller than both."],
        ["The product marker is compared with both factor markers and with 1.",
         "A prediction that multiplication always makes bigger is tested with a pair between 0 and 1.",
         "The rule is stated by the student for each region before a new pair is offered."],
        "Five pairs are predicted correctly and a pair smaller than both is found.",
        ["firstFactor", "secondFactor", "product", "comparison", "cardIndex"],
        ["M_MULT_BIGGER"],
        ["Is each factor below 1 or above 1?",
         "A factor below 1 shrinks the other number; a factor above 1 grows it.",
         "Compare the product with each factor, then with 1.",
         "The three markers show the answer; a similar pair follows."]),
    "reciprocal_flipper": T(
        "tool_reciprocal_flipper", "Reciprocal Flipper", "manipulative",
        "To divide by a fraction, turn the divisor over to get its reciprocal and multiply the dividend by it; a "
        "fraction times its reciprocal is 1.",
        "A division a/b ÷ c/d with the dividend and the divisor as cards; a flip control that turns the divisor into "
        "its reciprocal and changes the sign to a multiplication; a check line that multiplies the divisor by its "
        "reciprocal to show 1; the product is written with cancelling and as a mixed fraction.",
        ["Predict the reciprocal of the divisor.",
         "Flip the divisor card and watch the division turn into a multiplication.",
         "Cancel common factors and multiply.",
         "Check that the quotient times the divisor gives the dividend."],
        ["1 ÷ (2/3) (3/2).",
         "3 ÷ (2/3) (9/2).",
         "1/5 ÷ (1/2) (2/5).",
         "2/3 ÷ (3/5) (10/9).",
         "3 2/3 ÷ 1 3/8 (change mixed fractions first, 8/3).",
         "Find a divisor whose reciprocal is the same number."],
        ["Flipping the dividend is shown to give a wrong check line.",
         "Flipping both fractions is shown to leave the answer unchecked.",
         "A mixed fraction is changed to a fraction before the flip."],
        "Five divisions are done by flipping the divisor and one self-reciprocal number is found.",
        ["dividend", "divisor", "flipped", "quotient", "checkProduct", "cardIndex"],
        ["M_FLIP_DIVIDEND", "M_FLIP_BOTH"],
        ["Which of the two fractions do we turn over?",
         "Turn over the divisor, the fraction after the division sign.",
         "Change the sign to a multiplication and multiply the dividend by the flipped divisor.",
         "The check line shows divisor times quotient; a similar division follows."]),
}
