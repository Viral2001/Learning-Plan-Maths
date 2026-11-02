# -*- coding: utf-8 -*-
"""Tool specs for module M1 and the start of M2 (the lakh ruler, the comma ladder, the trading board)."""
from topics_common import T

TOOLS = {
    "lakh_benchmark": T(
        "tool_lakh_benchmark", "Lakh Ruler", "manipulative",
        "A number can be placed on a ruler marked at one lakh; the gap to the mark is found by subtracting the smaller "
        "from the larger, and the change between two numbers is the larger minus the smaller.",
        "A horizontal ruler from 0 to 2,00,000 with a bold mark at 1,00,000; a draggable pointer with a number box; a "
        "gap bar that grows between the pointer and the mark and says less than or more than one lakh; a second pointer "
        "for finding the change between two numbers.",
        ["Predict whether the number is below or above one lakh, then drag the pointer to it.",
         "Read the gap bar and type how far the number is from one lakh.",
         "Add a second pointer and type the change between the two numbers.",
         "Press Check to see the subtraction written out."],
        ["Place 75,000 and find how much less than one lakh it is (25,000).",
         "Place 1,06,000 and find how much more than one lakh it is (6,000).",
         "Place both and find the change from 75,000 to 1,06,000 (31,000).",
         "Place 99,500 and find the gap to one lakh (500).",
         "Place 1,25,000 and find the gap to one lakh (25,000).",
         "Place 36,500 and 1,09,500 and find which is closer to one lakh (1,09,500, gap 9,500)."],
        ["A wrong gap shows the subtraction with the larger number first, so the order is clear.",
         "A pointer on the wrong side of the mark turns the gap bar to the other colour and names less than or more "
         "than.",
         "A correct answer shows the subtraction in a line, for example 1,00,000 minus 75,000."],
        "All six placements are done with the right gap or change.",
        ["pointerA", "pointerB", "gap", "side", "change", "cardIndex"],
        ["M_LAKH_ZEROS", "M_LAKH_SMALL"],
        ["Is the number to the left or to the right of the one lakh mark?",
         "The gap is the larger number minus the smaller number.",
         "Subtract the number on the left of the mark from 1,00,000, or 1,00,000 from the number on the right.",
         "The subtraction is shown with the answer, and a new number follows."]),

    "comma_ladder": T(
        "tool_comma_ladder", "Comma Ladder", "manipulative",
        "Commas mark groups of digits from the right: thousands, then lakhs, then crores in the Indian system. Placing "
        "commas first makes a long number easy to read and to write in words.",
        "A row of digit boxes for a number up to 10 digits; a ladder of place names under it (ones, tens, hundreds, "
        "thousands, ten thousands, lakhs, ten lakhs, crores, ten crores, arabs); comma markers the student drags; a words "
        "line that fills as the commas are placed.",
        ["Predict where the first comma will go.",
         "Drag the comma markers between the digit boxes, from the right.",
         "Read the words line that fills in and fix any wrong group.",
         "Switch to numerals: type a number written in words and see the digits and commas."],
        ["Place commas in 4,50,678 and read it (four lakh fifty thousand six hundred seventy eight).",
         "Place commas in 27,05,300 (twenty seven lakh five thousand three hundred).",
         "Place commas in 3,08,00,000 (three crore eight lakh).",
         "Write 90,00,500 in words (ninety lakh five hundred).",
         "Write twelve lakh six thousand ten in numerals (12,06,010).",
         "Place commas in 1,00,00,00,000 and read it (one arab)."],
        ["A comma in the wrong place shakes and the correct group size, 3 first and then 2, is shown.",
         "A group read in the wrong place name is flagged with the place ladder highlighted.",
         "A zero group is skipped in the words line, with a note that nothing is said for it."],
        "All six numbers are placed and read correctly.",
        ["digits", "commas", "wordsLine", "mode", "cardIndex"],
        ["M_COMMA_PLACE", "M_LAKH_ZEROS"],
        ["How many digits are in the first group from the right?",
         "In the Indian system the first group from the right has 3 digits and every group after has 2.",
         "Drag the first comma after 3 digits and the next after 2 more.",
         "The commas are placed, the words line is read aloud and a new number follows."]),

    "trading_board": T(
        "tool_trading_board", "Trading Board", "manipulative",
        "Ten presses of a button can be traded for one press of the next bigger button, so the same number can be made in "
        "many ways, and every way gives an expression that adds to the number.",
        "A board with columns for the buttons plus one, plus ten, plus hundred, plus thousand, plus ten thousand and "
        "plus lakh; counters in each column; a trade arrow between neighbouring columns; an expression line that updates "
        "as counters move; a total box that must match the target.",
        ["Predict how many presses each button needs to reach the target.",
         "Place counters in the columns to reach the target.",
         "Trade one counter for ten in the column to its right, or ten for one in the column to its left.",
         "Read the expression line and press Check to confirm it adds to the target."],
        ["8300 in two ways (8 thousands and 3 hundreds, or 83 hundreds).",
         "40629 in two ways.", "56354 in two ways.", "66666 in two ways.",
         "367813 in two ways.", "997 using 34 presses (trade one hundred for ten tens)."],
        ["A trade that is not ten for one is refused with the exchange rate shown.",
         "A total that does not match the target is highlighted with how far it is.",
         "A correct way is added to a list of ways with its expression and its press count."],
        "Two different ways with correct expressions are found for each of the six numbers.",
        ["target", "counters", "expression", "total", "pressCount", "waysFound", "cardIndex"],
        ["M_BUTTON_ONE_WAY"],
        ["Which button has the biggest value that fits into the target?",
         "Trade one counter for ten counters of the next smaller button.",
         "Check that the expression still adds to the target.",
         "One trade is done for you and the expression is shown; a new number follows."]),
}
