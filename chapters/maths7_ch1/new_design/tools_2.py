# -*- coding: utf-8 -*-
"""Tool specs for modules M2 to M4 (fewest presses, the system converter, the rounding line)."""
from topics_common import T

TOOLS = {
    "fewest_presses": T(
        "tool_fewest_presses", "Fewest Presses", "manipulative",
        "To make a number with the fewest button presses, press each button once for each unit of its digit; the total "
        "presses equal the digit sum, and no button other than the biggest is pressed ten or more times.",
        "A calculator with plus one, plus ten, plus hundred, plus thousand, plus ten thousand and plus lakh buttons; "
        "a press counter for each button; a target number; a total press counter; a Trade helper that swaps ten presses "
        "for one on the next button.",
        ["Predict the fewest presses before pressing.",
         "Press the buttons to reach the target.",
         "Use the Trade helper to swap ten presses for one press of the next button.",
         "Compare the press total with the sum of the digits of the target."],
        ["8300 (11 presses).", "40629 (21 presses).", "56354 (23 presses).", "66666 (30 presses).",
         "367813 (28 presses).", "5072 starting from a 23 press way (14 presses)."],
        ["A button pressed ten or more times is flagged with the swap that saves nine presses.",
         "The total shows beside the digit sum so the match is seen.",
         "A way that is not the fewest is accepted but marked with how many more presses it uses."],
        "All six targets are reached with the fewest presses and the match with the digit sum is noticed.",
        ["target", "pressesByButton", "totalPresses", "digitSum", "cardIndex"],
        ["M_FEWEST_BIG", "M_BUTTON_ONE_WAY"],
        ["Which digit of the target tells how many presses one button needs?",
         "Ten presses of one button can be swapped for one press of the next button.",
         "Make each button's presses a single digit from 0 to 9.",
         "The presses are set to the digits of the number and the total is shown; a new target follows."]),

    "system_converter": T(
        "tool_system_converter", "System Converter", "manipulative",
        "The same number is grouped 3-2-2 in the Indian system and 3-3-3 in the international system; lakh, crore and arab "
        "match ten lakh equal one million and a hundred crore equal one billion.",
        "A digit row for a number up to 10 digits shown twice, once with Indian commas and once with international commas; "
        "two words lines that fill as the digits are typed; a conversion strip that shows lakhs and crores beside "
        "millions and billions; a compare mode with a less than, equal to or greater than selector.",
        ["Predict the commas in both systems.",
         "Type or choose a number and read both words lines.",
         "Use the conversion strip to turn lakhs and crores into millions and billions.",
         "In compare mode, change both amounts to the same unit before choosing the sign."],
        ["4050678 named in both systems.", "48121620 named in both systems.", "20022002 named in both systems.",
         "246813579 named in both systems.", "345000543 named in both systems.",
         "1020304050 named in both systems."],
        ["A wrong comma group shows the 3-2-2 or 3-3-3 pattern for that system.",
         "A wrong unit in a words line is highlighted next to the place ladder.",
         "In compare mode a sign chosen before converting is held back until both amounts use one unit."],
        "All six numbers are grouped and named correctly in both systems.",
        ["digits", "indianCommas", "internationalCommas", "indianWords", "internationalWords", "compareSign",
         "cardIndex"],
        ["M_COMMA_PLACE", "M_COMPARE_UNITS"],
        ["How are the digits grouped from the right in each system?",
         "The Indian system uses 3 digits then 2 each time; the international system uses 3 each time.",
         "Name each group with its place word: thousand, lakh, crore or arab; thousand, million or billion.",
         "Both systems are shown with their names and a new number follows."]),

    "rounding_line": T(
        "tool_rounding_line", "Rounding Line", "manipulative",
        "A large number lies between two neighbours at each place; it rounds to the closer neighbour, and a number exactly "
        "halfway rounds up. The digit just right of the place decides.",
        "A number line showing a number between two neighbours, with a zoom control for thousand, ten thousand, lakh, ten "
        "lakh and crore; a highlight on the digit to the right of the chosen place; a nearest neighbour box the student "
        "fills; a table that collects the five nearest neighbours.",
        ["Predict which neighbour is closer before choosing a place.",
         "Pick a place and zoom the line to the two neighbours around the number.",
         "Type the nearest neighbour and check it.",
         "Fill the table of the five nearest neighbours."],
        ["6,72,85,183 (five neighbours).", "3,87,69,957 (five neighbours).", "29,05,32,481 (five neighbours).",
         "76,068 to the nearest thousand and ten thousand.", "A number halfway between two neighbours.",
         "A number within 500 of 5,00,00,000 (all five neighbours the same)."],
        ["A neighbour on the wrong side is marked and the distance to each neighbour is shown.",
         "A tie at the halfway point states the round up rule.",
         "A correct answer shows the digit to its right that decided it."],
        "All six numbers have their neighbours right and the halfway rule used.",
        ["number", "place", "lowerNeighbour", "upperNeighbour", "chosen", "table", "cardIndex"],
        ["M_ROUND_PLACE"],
        ["Which place are you rounding to, and which digit is just to its right?",
         "If that digit is 5 or more, round up; if it is less than 5, round down.",
         "Keep the digits up to the place and fill the rest with zeros.",
         "The two neighbours are shown with the distances and the nearer one is chosen; a new number follows."]),
}
