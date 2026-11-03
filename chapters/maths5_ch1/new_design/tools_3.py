# -*- coding: utf-8 -*-
"""Tool spec for T10 (module M3): Transport Explorer (doc Tool 6). Specs only; the tool page is built later.
Every distance shown is the book's; every vehicle size is the book's; the few other numbers are labelled practice
values. The tool never adds a speed, a fare or a time of its own."""
from topics_common import T

TOOLS = {
    "transport_explorer": T(
        "tool_transport_explorer", "Transport Explorer", "manipulative",
        "Read the book's own numbers for travel and use them: how far a means of travel goes in one hour (from 3 to "
        "5 km on foot to at least 28,000 km by spacecraft), how many digits that distance has, how far it goes in "
        "several hours (the distance in one hour times the hours), and how many vehicles a group needs (the people "
        "divided by the people one vehicle carries).",
        "One clean, warm, colourful route map in a polished educational-game look: a 3D isometric landscape with soft "
        "shadows, clear shapes and gentle animation, where a winding route runs from a Start flag to a Finish flag "
        "across fields, a river bank and a sea shore. Nothing else is drawn: no crowds, no shops, no decoration off "
        "the route. The largest element is the distance card in the middle of the screen, with its numbers in very "
        "large type. A row of eight large vehicle buttons runs along the bottom, each with a picture and a name: Foot, "
        "Horseback, Cycle, Motorbike, Train, Ship, Aircraft, Spacecraft. "
        "Every control and read-out: (1) the eight vehicle buttons, one selected at a time; choosing one moves that "
        "vehicle a short way along the route. (2) The distance card, for example 'In 1 hour: 40 to 60 km', and for the "
        "spacecraft 'In 1 hour: at least 28,000 km'. (3) Digit chips under the card, one for each number on it, such "
        "as '2 digits', with the digits coloured by place. (4) An Hours stepper with minus and plus buttons from 1 to "
        "4 hours and a Go button: the vehicle hops along the route once for each hour, every hop the same length, and "
        "a working line shows each end of the range times the hours, for example '10 × 3 = 30'. The label 'same "
        "distance every hour (practice)' sits beside it. The Hours stepper is greyed out for the spacecraft because "
        "the book gives only a minimum. (5) A group panel: a crowd drawn in groups of ten, a 'People' read-out, the "
        "'People in one vehicle' read-out taken from the book's list (bicycle 2, autorickshaw 3, car 4, big car 6, "
        "tempo traveller 10, boat 20, minibus 25, aeroplane 180), a Load button that fills one vehicle at a time, a "
        "'Vehicles used' counter and a 'People left' counter. (6) An answer box that opens on a challenge card, with "
        "a Check button. (7) Hint, Undo and Reset buttons, a progress strip of dots with one dot for each card, Back "
        "and Next buttons in the same bottom corners on every card, and a Restart button. Only the controls the "
        "current card needs are shown.",
        ["Phase 1, Recall and get ready: a cycle, a train and a spacecraft wait at the Start flag. Tap each one and "
         "read its card: the distance in one hour and how many digits it has.",
         "Phase 2, Play and apply: tap a vehicle and read its card, find the means whose card holds a given "
         "distance, set the hours and watch the vehicle hop the same distance each hour while the card shows the "
         "multiplication, and load a group of people into one kind of vehicle to count the vehicles.",
         "Phase 3, Challenge: the book's own questions, unchanged: the cyclist who covers 15 km in one hour (how far "
         "in 4 hours), and the school of 461 girls and 439 boys with the eight vehicles from the bicycle (2) to the "
         "aeroplane (180)."],
        ["Card 1 (Phase 2, read): Tap Foot, then Spacecraft. How many digits does the number on each card have? "
         "Answer: foot, 3 to 5 km, 1 digit; spacecraft, at least 28,000 km, 5 digits.",
         "Card 2 (Phase 2, find the means): Practice value: a traveller covers 30 km in one hour. Tap the vehicles "
         "and find the one whose card holds 30. Answer: the ship, 25 to 45 km, because 25 is less than 30 and 30 is "
         "less than 45; every other card misses 30.",
         "Card 3 (Phase 2, hours): Pick Horseback and set 3 hours. Fill in both ends of the range for 3 hours, with "
         "the same distance every hour (practice). Answer: 10 × 3 = 30 and 15 × 3 = 45, so 30 to 45 km.",
         "Card 4 (Phase 2, vehicles): Practice value: a group of 120 people. Load them into boats (20 each) and then "
         "into tempo travellers (10 each). How many of each, and which needs fewer? Answer: 120 ÷ 20 = 6 boats and "
         "120 ÷ 10 = 12 tempo travellers; the boat carries more people, so fewer boats are needed.",
         "Card 5 (Phase 3, the book's question): A cyclist can cover 15 km in one hour. How much distance will she "
         "cover in 4 hours, if she maintains the same speed? Answer: 15 + 15 + 15 + 15 = 60, so 15 × 4 = 60 km.",
         "Card 6 (Phase 3, the book's question): A school has 461 girls and 439 boys. How many vehicles are needed "
         "for all of them to go on a trip using the following modes of travel? The numbers in the bracket indicate "
         "the number of people that can travel in one vehicle. (a) Bicycle (2) (b) Autorickshaw (3) (c) Car (4) "
         "(d) Big car (6) (e) Tempo traveller (10) (f) Boat (20) (g) Minibus (25) (h) Aeroplane (180). Answer: "
         "461 + 439 = 900 people; 450, 300, 225, 150, 90, 45, 36 and 5 vehicles."],
        ["A right answer turns the card green with a tick, and the vehicle drives to the Finish flag. The working "
         "appears in one line, for example 10 × 3 = 30.",
         "A distance that is not in the chosen range shows the range beside it and says whether the distance is less "
         "than the first number or more than the last number.",
         "A wrong number of digits lights up the digits of the number one by one and counts them aloud.",
         "A wrong number of hours or vehicles shows the hops or the loaded vehicles on the route and the people still "
         "left, so the student sees what is missing.",
         "Each hour of the journey stays on the route as a hop of the same length, so the total is seen being "
         "built."],
        "Every card is done and the student has opened at least five of the eight vehicle cards.",
        ["vehicle", "hours", "group", "loaded", "cardIndex"],
        [],
        ["Which card is open, and what does it show: a range or a minimum?",
         "For many hours, take the distance in one hour as many times as the number of hours. For vehicles, divide "
         "the people by the people in one vehicle.",
         "A distance fits a range when it is at least the first number and at most the last number. To check "
         "vehicles, multiply the vehicles by the people in one.",
         "Worked step: horseback, 10 to 15 km, 2 hours: 10 × 2 = 20 and 15 × 2 = 30, so 20 to 30 km. For the cyclist "
         "and the school the same step is shown with their own numbers, then a similar card follows."]),
}
