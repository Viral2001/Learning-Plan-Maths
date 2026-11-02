# -*- coding: utf-8 -*-
"""Tool specs for the division sizes and the problem topics T8 to T10."""
from topics_common import T

TOOLS = {
    "quotient_size_predictor": T(
        "tool_quotient_size_predictor", "Quotient Size Predictor", "simulation",
        "Dividing by a number above 1 gives a quotient smaller than the dividend; dividing by a number between 0 "
        "and 1 gives a quotient greater than the dividend.",
        "A number line from 0 to 30; a slider for the dividend and a slider for the divisor, with fractions; "
        "markers for the dividend and the quotient; a line showing how many divisors fit in the dividend; labels "
        "say whether the quotient is greater or smaller than the dividend.",
        ["Predict whether the quotient will be bigger or smaller than the dividend.",
         "Set the dividend and the divisor.",
         "See how many divisor-sized pieces fit in the dividend.",
         "Read the quotient and say which region the divisor was in."],
        ["6 ÷ 3 (2, smaller).",
         "6 ÷ (1/4) (24, greater).",
         "1/8 ÷ (1/4) (1/2, greater).",
         "9 ÷ (3/2) (6, smaller).",
         "9 ÷ (2/3) (27/2, greater).",
         "Find a divisor that leaves the quotient equal to the dividend."],
        ["The pieces that fit are counted against the quotient shown.",
         "A prediction that division always shrinks is tested with a divisor between 0 and 1.",
         "The divisor 1 is explained as the case where nothing changes."],
        "Five quotients are predicted correctly and the divisor that leaves the dividend unchanged is found.",
        ["dividend", "divisor", "quotient", "piecesThatFit", "comparison", "cardIndex"],
        ["M_DIV_SMALLER"],
        ["Is the divisor above 1 or between 0 and 1?",
         "A divisor above 1 gives fewer pieces than the dividend; a divisor below 1 gives more.",
         "Count how many divisor-sized pieces fit in the dividend.",
         "The pieces are drawn on the line; a similar pair follows."]),
    "operation_chooser": T(
        "tool_operation_chooser", "Multiply or Divide Chooser", "manipulative",
        "A story about sharing or fitting becomes a multiplication with a missing number; the unknown is found by "
        "dividing, which is multiplying by the reciprocal.",
        "A story card; a box for the missing quantity; a choice of four expressions; the story is shown as "
        "(number of things) × (size of each) = total with one part missing; the chosen expression is evaluated step "
        "by step.",
        ["Read the story and find which quantity is missing.",
         "Write it as a multiplication with a gap.",
         "Pick the expression that finds the gap.",
         "Evaluate it with the reciprocal and check against the story."],
        ["8 m of lace, 1/4 m for each bag: how many bags (8 ÷ (1/4) = 32).",
         "1/2 m of ribbon for 8 badges: each badge (1/2 ÷ 8 = 1/16 m).",
         "5 kg of flour, 1/6 kg for each loaf: how many loaves (5 ÷ (1/6) = 30).",
         "5 cups of tea share 1/4 litre of milk (1/4 ÷ 5 = 1/20 litre).",
         "1/5 of a cake shared by 3 friends (1/5 ÷ 3 = 1/15).",
         "Write a story of your own for 3/4 ÷ 3."],
        ["A chosen expression is tested against the story by putting the answer back in the multiplication.",
         "A reversed division is shown to give an answer that does not fit.",
         "The size of the answer is compared with the story."],
        "Five stories are matched to an expression and one story is written.",
        ["story", "missingPart", "chosenExpression", "evaluated", "check", "cardIndex"],
        ["M_WRONG_OPERATION"],
        ["Which number in the story is the total and which is one share?",
         "Write (number of shares) × (size of one share) = total with the missing one as a gap.",
         "Divide the total by the known part, using the reciprocal.",
         "The gap box shows the missing part; the next story is similar."]),
    "fraction_splitter": T(
        "tool_fraction_splitter", "Fraction of a Fraction Splitter", "manipulative",
        "A part of a part is found by multiplying the fractions at each step; the pieces of one whole always add up "
        "to 1.",
        "A whole square, or a whole group of ants, that can be split step by step: choose a piece and cut it into "
        "equal parts or take a fraction of it; each step shows the fraction of the original whole as a product; a "
        "total bar shows the pieces adding to 1.",
        ["Predict the fraction of the whole for the piece you will make.",
         "Take a piece and split it or take a fraction of it.",
         "Read the fraction of the original whole as a product.",
         "Check that all the pieces together make 1."],
        ["Take 1/4 of the square, then 1/2 of that (1/8).",
         "Take 3/4 of that 1/8 (3/32).",
         "A path of ants that splits in half twice (1/4).",
         "The ant colony in four stages, mango share (29/32).",
         "The ant colony, sugarcane share (3/32).",
         "Make your own piece of 3/16 of the whole."],
        ["The fraction shown is compared with the product the student wrote.",
         "A fraction taken of the whole instead of the piece is shown on the square.",
         "The total bar must reach 1 before the card closes."],
        "Five parts of a whole are found, including both shares of the ant colony, and one custom piece is made.",
        ["pieces", "currentPiece", "fractionOfWhole", "total", "cardIndex"],
        ["M_FRACTION_OF_WHOLE"],
        ["Which piece are you taking a fraction of, the whole or a part?",
         "Multiply the fraction of this step by the fraction of the piece before it.",
         "Keep multiplying down the path and write the result as one fraction.",
         "The total bar shows what is left; a similar split follows."]),
}
