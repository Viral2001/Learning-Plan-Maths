# -*- coding: utf-8 -*-
"""Tool specs for modules M1 and M2: lift_mover, floor_line, number_line_walker. Doer tools only."""
from topics_common import T

TOOLS = {
    "lift_mover": T(
        "tool_m1s1t3c4", "Lift Mover", "manipulative",
        "A lift's final floor is its starting floor plus the movement, and the plus and minus presses are signed "
        "numbers.",
        "A tall building with floors from +6 down to −5 and a lift on the ground floor; a '+' button and a '−' "
        "button that move the lift one floor each press; a press counter; a Starting Floor + Movement = Target "
        "Floor line that fills in.",
        ["Predict the floor before pressing.",
         "Press '+' or '−' to move the lift.",
         "Read the target floor and the sum that goes with it."],
        ["Start at 0, press '+' 4 times (floor +4).", "Start at +3, press '−' 5 times (floor −2).",
         "Start at −2, press '+' 6 times (floor +4).", "Start at −4, press '−' 2 times (floor −6).",
         "Reach floor −3 from floor +2 (5 presses of '−').", "Go from +5 to −1 and then to +3 (total movement +2)."],
        ["A wrong prediction shows the lift's path floor by floor.",
         "A '−' press from floor 0 lands below the ground, shown in red, so the lift is not stuck at zero.",
         "A solved card shows Starting Floor + Movement = Target Floor with the numbers filled in."],
        "All six cards have the right target floor and sum.",
        ["startFloor", "presses", "targetFloor", "answer", "cardIndex"],
        ["M_BUTTON_ADD_ONLY", "M_NEG_NOTHING", "M_ADD_BIGGER"],
        ["Which button moves the lift up, and which moves it down?",
         "Every '+' press is +1 and every '−' press is −1; the movement is the total.",
         "Count the presses of each button, then add them to the starting floor.",
         "The lift's path is shown floor by floor; a similar card follows."]),

    "floor_line": T(
        "tool_m1s2t4c3", "Floor Line", "manipulative",
        "Moving the lift between two floors needs a movement, and it is the target floor minus the starting floor.",
        "A vertical line of floors from +6 to −6 with two markers, Start and Target, that can be dragged; a "
        "movement arrow between them; a line Target − Start = Movement that fills in; a '<' or '>' sign between "
        "the two floor numbers.",
        ["Drag Start and Target to two floors.",
         "Read the arrow and the movement.",
         "Choose '<' or '>' to compare the two floors."],
        ["Start +2, target −3 (movement −5).", "Start −4, target +1 (movement +5).",
         "Start −2, target −5 (movement −3).", "Compare −3 and −5 (−3 > −5).",
         "Compare −7 and 0 (−7 < 0).", "Find the movement from −6 to +4 (+10)."],
        ["A wrong movement shows the arrow's real length and direction.",
         "Comparing two negatives shows the floor that is higher in the building.",
         "A solved card shows Target − Start = Movement with the numbers filled in."],
        "All six cards are right.",
        ["start", "target", "movement", "answer", "cardIndex"],
        ["M_START_MINUS_TARGET", "M_DISTANCE_ONLY", "M_BIGGER_DIGIT", "M_DEEPER_HIGHER"],
        ["Which floor is higher in the building, and which is lower?",
         "The movement is the target floor minus the starting floor, and its sign shows the direction.",
         "Count the steps from Start to Target and give them a plus if you go up, a minus if you go down.",
         "The arrow shows the movement; a similar card follows."]),

    "number_line_walker": T(
        "tool_m2s1t7c3", "Number Line Walker", "manipulative",
        "On a number line, right is positive and left is negative, and a walk from one number to another is the "
        "movement that makes Start + Movement = Target.",
        "A horizontal number line from −10 to +10 with a walker marker; a drag handle for Start and for Target; "
        "an arrow showing the movement; the sum Start + Movement = Target filling in.",
        ["Predict the movement.",
         "Drag Start and Target to two numbers.",
         "Read the arrow and the sum."],
        ["From 3 to 8 (+5).", "From 9 to 3 (−6).", "From 3 to −2 (−5).", "From −4 to −9 (−5).",
         "From −7 to 2 (+9).", "Place −3, 0, −8 and 4 in order, smallest on the left."],
        ["A wrong movement shows the walker's real path and its length.",
         "A walk to the left is shown in red with a minus sign on the movement.",
         "A solved card shows Start + Movement = Target."],
        "All six cards are solved.",
        ["start", "target", "movement", "answer", "cardIndex"],
        ["M_DISTANCE_ONLY", "M_START_MINUS_TARGET", "M_BIGGER_DIGIT"],
        ["Is the target to the left or to the right of the start?",
         "Right is positive and left is negative; the movement takes the sign of the direction.",
         "Count the steps from the start to the target.",
         "The walker's path is shown with the movement; a similar card follows."]),
}
