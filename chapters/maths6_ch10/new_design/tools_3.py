# -*- coding: utf-8 -*-
"""Tool specs for module M4: border_grid, snakes_ladders. Doer tools only."""
from topics_common import T

TOOLS = {
    "border_grid": T(
        "tool_m4s1t13c3", "Border Grid", "manipulative",
        "The two rows and two columns on the border of the grid all add to the same border sum.",
        "A 3x3 grid with the centre blank; number tiles that can be placed in the empty cells; four sum readouts, "
        "one for each side; a target border sum.",
        ["Predict a missing number.",
         "Tap a cell and set its number.",
         "Read the four side sums."],
        ["Grid 4, −1, −3 / −3, _, 1 / −1, −1, 2: find the border sum (0).",
         "Grid 5, −3, −5 / 0, _, −5 / −8, −2, 7: find the border sum (−3).",
         "Fill a grid for border sum +4.", "Fill a grid for border sum −2.",
         "Fill a grid for border sum −4 in two different ways.",
         "Make a grid of your own and read its border sum."],
        ["A side that does not match the border sum is shown in red with its sum.",
         "A side with the right sum turns green.",
         "A solved card shows all four sums equal to the border sum."],
        "All six cards have four equal sums.",
        ["cells", "borderSum", "sideSums", "answer", "cardIndex"],
        ["M_GRID_CHOICE", "M_IGNORE_SIGN"],
        ["Which sides does the blank cell belong to?",
         "Each side must add to the border sum.",
         "Border sum minus the two known numbers on that side gives the blank.",
         "The correct number is shown; a similar card follows."]),

    "snakes_ladders": T(
        "tool_m4s2t17c2", "Integer Snakes and Ladders", "simulation",
        "Each roll gives a positive and a negative number, and adding or subtracting them in either order gives "
        "a move towards +50 or −50.",
        "A board from −50 to +50 with snakes, ladders and two pawns; a pair of dice, one with +1 to +6 and one "
        "with −1 to −6; buttons for the sum, the first minus the second and the second minus the first.",
        ["Roll the dice.",
         "Choose add or subtract.",
         "Watch the pawn move."],
        ["Roll +4 and −5: choose the move that goes furthest from 0 (9 or −9).",
         "Roll +3 and −2: choose the move that stays near 0.",
         "Roll +6 and −1: list the three results.", "Play to a ladder or snake.",
         "Play a full game to +50 or −50."],
        ["A chosen result is shown as a sum so the move can be checked.",
         "A snake or a ladder shows the new square.",
         "A finished game shows the number of moves taken."],
        "A full game has been finished.",
        ["dice", "choice", "pawnPosition", "answer", "cardIndex"],
        ["M_DIE_CHOICE"],
        ["Which two numbers did you roll?",
         "You may add them or subtract them, in either order.",
         "A positive result moves towards +50 and a negative result towards −50.",
         "The three results are shown; a similar roll follows."]),
}
