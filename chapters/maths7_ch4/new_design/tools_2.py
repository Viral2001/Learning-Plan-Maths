# -*- coding: utf-8 -*-
"""Tool specs for the brackets topic and the calendar topic."""
from topics_common import T

TOOLS = {
    "minus_sign_flipper": T(
        "tool_minus_sign_flipper", "Minus Bracket Sign Flipper", "manipulative",
        "A minus sign before a bracket flips the sign of every term inside it, a plus sign leaves them alone, and a "
        "number outside multiplies every term; after that, like terms are gathered.",
        "An expression with a bracket and a sign or number in front; each term inside the bracket is a card with a "
        "sign; a Flip button for a minus sign and a Multiply button for a number; a result line where like terms are "
        "gathered; a number test to compare values.",
        ["Look at what stands in front of the bracket.",
         "Press Flip for a minus sign, or Multiply for a number, and watch every term inside change.",
         "Gather the like terms on the result line.",
         "Test the result against the original with a chosen number."],
        ["(40x + 75y) − (6x + 10y) (34x + 65y).", "23p − 7q − (21p − 9q) (2p + 2q).", "4(x + y) − y (4x + 3y).",
         "5 − (2 − 6z) (3 + 6z).", "2 + (x + 3) (x + 5).", "(6a + 9b − 18) − (9a − 6b + 14) (−3a + 15b − 32)."],
        ["Flipping only the first term inside the bracket is shown with the test values not matching.",
         "A plus sign before the bracket that is flipped by mistake is shown with the values not matching.",
         "A number outside that multiplies only the first term is shown with the unmultiplied terms highlighted."],
        "All six expressions are opened and gathered correctly and each passes the number test.",
        ["bracketTerms", "outsideSign", "result", "testValue", "cardIndex"],
        ["M_BRACKET_SIGN", "M_DISTRIB_FIRST"],
        ["What is in front of the bracket: a plus, a minus or a number?",
         "A minus changes the sign of every term inside. A plus changes nothing. A number multiplies every term.",
         "Write each term with its new sign, then gather the like terms.",
         "Every term inside is changed as the sign says, the like terms are gathered, the test confirms the values, "
         "and a new expression follows."]),

    "grid_shape_prover": T(
        "tool_grid_shape_prover", "Grid Shape General Prover", "simulation",
        "Naming one date a and writing every other date in a shape as a plus or minus a number turns a pattern seen "
        "in examples into a proof for every position on an endless calendar.",
        "An endless calendar grid with seven dates in a row; a movable shape frame; labels for the dates in the "
        "frame as expressions in a; a sum line that adds the expressions; a list of examples sliding the frame to "
        "new places.",
        ["Slide the frame to a few places and add the dates to see the pattern.",
         "Label the centre or the top left date a and fill in the other dates as expressions.",
         "Add the expressions and gather the like terms.",
         "Read what the sum is in terms of a and check it against the examples."],
        ["A 2 by 2 square, diagonal sums (2a + 8).", "A cross of five dates, sum (5a).",
         "A row of three dates, sum (3a).", "A column of three dates, sum (3a).",
         "A 2 by 3 grid, sum of all six dates, with the bottom middle date w.",
         "A shape of your choice with the sum a multiple of one date."],
        ["Writing the date below as a + 1 instead of a + 7 is shown with the frame highlighting the wrong date.",
         "A pattern checked on only two examples is marked as not yet proved.",
         "The expression sum is compared with each example sum to show they agree."],
        "All six shapes have a proved sum written in terms of a and checked on two examples.",
        ["shape", "centre", "labels", "sum", "cardIndex"],
        ["M_LETTER_FIXED"],
        ["What changes when you slide the frame, and what stays the same?",
         "Call one date a. A date to the right is 1 more, a date below is 7 more.",
         "Write every date in the frame as an expression in a and add them.",
         "The dates are labelled in a, the sum is gathered into one expression, and the examples confirm it; a new "
         "shape follows."]),
}
