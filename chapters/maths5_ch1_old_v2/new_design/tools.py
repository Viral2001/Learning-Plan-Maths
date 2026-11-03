# -*- coding: utf-8 -*-
"""Tool specs for Class 5 Chapter 1 (We the Travellers - I). Ten tools, each used once, all built to the Class 5 brief:
the student does the action (builds and rearranges numbers, compares values, places markers on number lines, completes
patterns, solves problems) and the screen answers at once. Specs only; the tool pages are built later."""
from topics_common import T

BRIEF = ("Class 5 tool brief: interactive and doer-based, the student performs actions and does not only watch. The "
         "student can build and rearrange numbers, compare values, place markers on number lines, complete patterns "
         "and solve problems. Colourful, clear and engaging: number cards, place value tokens, number lines, arrows, "
         "visual counters and real-life travel illustrations, all of which can be selected, moved, changed or "
         "arranged. A simple uncluttered layout with one prominent main visual and only the controls that are needed. "
         "Immediate visual feedback: numbers update, markers move and correct arrangements are highlighted. Hints and "
         "feedback help the student discover the answer and never reveal it. Hands-on, visually engaging and "
         "conceptually clear.")


def _t(*a):
    spec = T(*a)
    spec["design_brief"] = BRIEF
    return spec


TOOLS = {
    "odometer_reader": _t(
        "tool_odometer_reader", "Odometer Reader: How Far Did the Vehicle Go?", "manipulative",
        "A vehicle's odometer shows the distance covered as a number. Each wheel is one place, and when the ones wheel "
        "passes 9 it turns back to 0 and pushes the next wheel on by one. A free try before the lesson: turn the "
        "wheels, read the number, and feel why ten thousand needs a fifth wheel.",
        "A colourful dashboard of a bus with an odometer of five wheels labelled O, T, H, Th, TTh, a Drive button that "
        "adds kilometres in steps of 1, 10, 100 or 1,000, and a plain readout that shows the number with a comma "
        "under the wheels.",
        ["Press Drive and watch the wheels turn from 0 up.",
         "Choose a step of 1, 10, 100 or 1,000 and press Drive again.",
         "Turn any wheel by hand to make a number you are asked for.",
         "Read the number under the wheels and say it aloud."],
        ["Drive the bus from 0 to 999 and watch the wheels; what happens to the tens wheel?",
         "Add 1 to 999. What do the three wheels do?",
         "Drive in steps of 1,000 from 0 until the wheels cannot show the number in four places.",
         "Set the odometer to read 4,305 by turning the wheels.",
         "Set it to read 12,214.",
         "The bus is at 9,998. How many more kilometres until the fifth wheel moves?"],
        ["Each wheel shows its digit in a large number with a colour per place, and the comma appears in the readout "
         "once the Th wheel has a digit.",
         "A wheel that passes 9 flashes and moves the wheel on its left by one, and the arrow between them lights up.",
         "A set that is not the number asked for shows the number the wheels now read, beside the target."],
        "Every card is done and the student has seen the fifth wheel move at 10,000.",
        ["wheels", "step", "reading", "target", "cardIndex"],
        ["M_TT_COLUMN"],
        ["Which wheel moves first when you press Drive?",
         "When the ones wheel shows 9 and moves again, what does the tens wheel do?",
         "Ten of one wheel make one of the next wheel on the left.",
         "Watch the arrow between the wheels: 9 and one more makes the wheel go to 0 and the next wheel moves by 1."]),

    "ten_thousand_builder": _t(
        "tool_ten_thousand_builder", "Ten-Thousand Builder: Drop Tokens and Regroup", "manipulative",
        "Ten tokens of one place regroup into one token of the next place. Dropping thousand tokens one by one shows "
        "that ten of them become one ten thousand token and that the number needs the TTh column.",
        "A place value chart with columns TTh, Th, H, T, O, a tray of 1, 10, 100, 1,000 and 10,000 tokens, a Regroup "
        "button, and a number readout with commas under the chart.",
        ["Drag tokens from the tray into a column.",
         "When a column holds ten tokens, press Regroup and watch the ten become one token in the column on the left.",
         "Read the number under the chart.",
         "Remove or add tokens to change the number."],
        ["Drop thousand tokens one at a time from 1,000 to 9,000.",
         "Drop the tenth thousand token. What happens?",
         "Build 10,000 using the fewest tokens.",
         "Build 12,000 and say how many TTh and Th tokens it has.",
         "Build 1,380 with the fewest tokens and read it with a comma.",
         "Build 9,123, then add one more thousand token."],
        ["A tenth token in any column makes the column glow and offers Regroup; after Regroup the new token drops "
         "into the next column.",
         "The readout adds a comma only when the number reaches 1,000, and a zero holds every empty column.",
         "A build that does not match the target shows the number it makes beside the target."],
        "Every card is done with the chart showing the target number.",
        ["tokens", "regroup", "readout", "target", "cardIndex"],
        ["M_TT_COLUMN", "M_COMMA_PLACE"],
        ["Which column holds the thousand tokens?",
         "What happens in the chart when a column holds ten tokens?",
         "Ten thousand tokens make one ten thousand token in the TTh column.",
         "Press Regroup on the Th column: the ten tokens become one in TTh, and the Th column shows 0."]),

    "token_table_builder": _t(
        "tool_token_table_builder", "Token Table Builder: Make It, Write It, Name It", "manipulative",
        "A five-digit number is built from tokens, written in the chart with commas and named by reading the "
        "thousands part first, then hundreds, tens and ones.",
        "A tray of 1, 10, 100, 1,000 and 10,000 tokens, a work area, a filled TTh Th H T O chart that updates as "
        "tokens are dropped, a comma readout, and a name strip where the student arranges word cards such as "
        "Ten, thousand, four, hundred, fifty and eight.",
        ["Drag tokens into the work area to build a number.",
         "Watch the chart and the readout update and check that every digit is in its place.",
         "Arrange the word cards to name the number.",
         "Press Check to see which part is right and which part needs a second look."],
        ["Build 10,024 with tokens and name it.",
         "Build 10,458 and arrange its name.",
         "Build 11,214 and fill the chart.",
         "Build 13,520 and name it.",
         "A number name is shown: Forty-five thousand eight hundred sixty-seven. Build it from tokens.",
         "Build 50,005 and place a zero token in every column that is empty."],
        ["The chart colours each column the colour of its token, and a column with no token shows a bold zero.",
         "A name card in the wrong place springs back with the part of the number it should name highlighted.",
         "A number built correctly is celebrated, and the same number shown as an expanded sum appears below."],
        "Every card is done with the number, the chart and the name all matching.",
        ["tokens", "chart", "readout", "wordCards", "cardIndex"],
        ["M_ZERO_NAME", "M_COMMA_PLACE"],
        ["Which tokens make the thousands part of the number?",
         "Read the thousands part first, then the hundreds, tens and ones.",
         "Put the tokens of the thousands part first and name that part before the hundreds.",
         "For 10,458, the thousands part is ten thousand; the word cards then follow with four hundred and fifty-eight."]),

    "pattern_rule_finder": _t(
        "tool_pattern_rule_finder", "Pattern Rule Finder: What Is the Jump?", "manipulative",
        "A pattern of numbers has a rule. Jumping from one number to the next on a number line shows how much is added "
        "or taken away each time, and the same jump gives the next numbers.",
        "A row of number cards with blanks, a number line that shows an arrow for each jump, a jump-size dial, and a "
        "Test the rule button that fills the blanks with the chosen jump.",
        ["Look at two neighbouring cards and drag the dial to the jump between them.",
         "Press Test the rule and watch the arrow jumps fill the blanks.",
         "Check that every card in the row now follows the rule.",
         "Change the rule and see which cards no longer fit."],
        ["Sequence 456, 567, 678: find the jump and fill four blanks.",
         "Sequence 1,050, blank, 3,150, 4,200: find the jump and the missing card.",
         "Sequence 5,501, 6,401, 7,301: find the jump and fill two blanks.",
         "Sequence 10,100, 10,200, 10,300 continuing to 10,900.",
         "Sequence 10,992, 10,993: find the jump.",
         "Sequence 73,005, 72,004: is the rule add or subtract, and how much?"],
        ["Each correct jump draws an arrow in the colour of its rule; a wrong jump shows the two cards that do not "
         "match.",
         "A blank filled by the rule turns green and keeps the arrow behind it.",
         "A rule that adds when the cards fall is shown as an arrow pointing the wrong way."],
        "Every sequence is completed and the rule is named in words.",
        ["cards", "jump", "direction", "arrows", "cardIndex"],
        ["M_DIGIT_DIFF"],
        ["How far apart are the first two cards?",
         "Is the next card bigger or smaller than the one before?",
         "Subtract the smaller neighbouring card from the bigger and try that jump on the next pair.",
         "The jump between the first two cards is shown; test it on the third and fourth cards."]),

    "compare_chart": _t(
        "tool_compare_chart", "Compare Chart: Which Number Is Greater?", "manipulative",
        "To compare two numbers, first count their digits, and if the digits are equal compare place by place from "
        "the left. A bigger first digit does not make a bigger number when the other number has more digits.",
        "A two-row place value chart (TTh to O) with a digit card for each cell, a number line below that shows both "
        "numbers as markers, and greater than, less than and equal to sign cards to drag between the numbers.",
        ["Type or drag digit cards into each row.",
         "Look at the number of digits first, then at each place from the left.",
         "Drag the greater than or less than sign between the numbers.",
         "Drag the numbers into order along the line."],
        ["Compare 9,990 and 49,014: count the digits first.",
         "Compare 56,987 and 67,543.",
         "Compare 89,999 and 90,000.",
         "Compare 40,347 and 40,473 place by place.",
         "Arrange 40,347, 34,407, 40,473 and 34,740 in increasing order.",
         "Arrange the six prices 90,000, 89,999, 94,983, 49,900, 93,743 and 39,999 in ascending order."],
        ["The first place where the digits differ glows, and the number with the bigger digit there lights up.",
         "A number with more digits slides further along the number line and a note says so.",
         "A sign dropped the wrong way flips and shows the two numbers with the gap between them."],
        "Every card is done with signs and order correct.",
        ["rowA", "rowB", "sign", "markers", "cardIndex"],
        ["M_FIRST_DIGIT"],
        ["How many digits does each number have?",
         "If both have the same digits, which is the first place where they differ?",
         "Compare the leftmost digits that differ; the bigger digit there gives the bigger number.",
         "For 9,990 and 49,014: 49,014 has five digits and 9,990 has four, so 49,014 is greater."]),

    "number_line_placer": _t(
        "tool_number_line_placer", "Number Line Placer: Where Does It Go?", "manipulative",
        "A number line shows how far a number is from 0. Marking a number between two benchmark numbers by reading its "
        "place values tells us where on the line it sits.",
        "A long number line with benchmark ticks at 0, 20,000, 40,000, 60,000 and 80,000, number cards to drag onto "
        "the line, a zoom bar that shows the line between two ticks in finer steps, and a ruler of place values "
        "under the chosen number.",
        ["Drag a number card to the place on the line where you think it belongs.",
         "Zoom into the part of the line between two ticks to place it more exactly.",
         "Press Check to see the number's true position and how far off the marker was.",
         "Move the marker again until it sits on the number."],
        ["Place 40,347 and 40,473: which is to the right?",
         "Place 34,407 and 34,740 between 20,000 and 40,000.",
         "Place 73,404 and 74,430 between 60,000 and 80,000.",
         "Place 47,340 and 18,926 and say which tick each is nearest to.",
         "Place all eight numbers and read them from left to right.",
         "Find a number between 23,568 and 24,234 and place it."],
        ["A correctly placed marker locks in with a tick mark and the number printed above.",
         "A marker placed too far shows an arrow back towards the true place, never the exact spot.",
         "When the line is zoomed, the ticks update to the new step and the cards already on the line stay."],
        "Every card is done with all markers on their true places.",
        ["markers", "zoom", "target", "order", "cardIndex"],
        ["M_FIRST_DIGIT"],
        ["Between which two ticks does the number sit?",
         "Look at the thousands and ten thousands digits to decide which two ticks.",
         "Zoom into the stretch between those ticks and use the hundreds digit to place it.",
         "Between 40,000 and 60,000, the number 47,340 sits just over a third of the way along."]),

    "rabbit_rounder": _t(
        "tool_rabbit_rounder", "Rabbit Rounder: Hop to the Nearest Food", "manipulative",
        "The nearest ten, hundred or thousand of a number is the neighbouring one with the fewest jumps away. When a "
        "number is halfway between two neighbours, it goes to the bigger one.",
        "A number line with a rabbit at a number, two food bowls at its neighbouring tens, hundreds or thousands, a "
        "Tens, Hundreds, Thousands switch, a jump counter that counts ones as the rabbit hops, and a table to fill "
        "with the nearest tens, hundreds and thousands.",
        ["Choose Tens, Hundreds or Thousands.",
         "Drag the rabbit to the food bowl it should go to, and count the jumps.",
         "Type the nearest number in the table row.",
         "Move the rabbit to a new number and try again."],
        ["Rabbit at 2,346: nearest ten, and the jumps needed.",
         "Rabbit at 2,346: nearest hundred.",
         "Rabbit at 2,346: nearest thousand.",
         "Fill the table row for 3,176, 4,017, 5,789 and 8,203.",
         "Put the rabbit on 2,345 and decide where it goes.",
         "Find a number whose nearest ten, hundred and thousand are all the same."],
        ["The two food bowls light up with a jump count under each, and the nearer one glows once the rabbit is "
         "placed.",
         "A rabbit sent to the farther bowl shows the extra jumps it would need.",
         "A number exactly halfway shows both bowls the same distance away and a note about the rule."],
        "Every row of the table and every card is done.",
        ["rabbit", "unit", "bowls", "table", "cardIndex"],
        ["M_ROUND_UP", "M_HALFWAY"],
        ["Which two neighbours is the rabbit between?",
         "Count the jumps to each neighbour and compare.",
         "Look at the digit one place to the right of the place you are rounding to.",
         "From 2,346, the jump to 2,350 is 4 and to 2,340 is 6, so 2,350 is nearer."]),

    "vehicle_loader": _t(
        "tool_vehicle_loader", "Vehicle Loader: How Many Vehicles?", "manipulative",
        "To carry a group of people, divide the number of people by the number each vehicle carries. When there is a "
        "remainder, one more vehicle is needed for the people left over.",
        "A crowd of 900 people shown in groups of 10, a row of eight vehicles (bicycle 2, autorickshaw 3, car 4, big "
        "car 6, tempo traveller 10, boat 20, minibus 25, aeroplane 180), a Load button that fills a chosen vehicle "
        "with people and a counter of vehicles used.",
        ["Choose a vehicle type.",
         "Press Load to fill one vehicle and watch the number of people left.",
         "Keep loading until nobody is left, or use the Fill all button after estimating.",
         "Write the number of vehicles and say whether any seat is empty."],
        ["Cyclist: 15 km in one hour, how far in 4 hours? Loader shows 4 hops of 15.",
         "900 people with bicycles (2 each): how many?",
         "900 people with autorickshaws (3 each).",
         "900 people with cars (4 each) and with big cars (6 each).",
         "900 people with tempo travellers, boats and minibuses.",
         "900 people with aeroplanes (180 each): how many, and are all seats full?"],
        ["Each loaded vehicle drops one token on a tally and the people left count down.",
         "A last vehicle that is not full is shown with empty seats in a lighter colour.",
         "A wrong number of vehicles shows how many people are still left standing."],
        "Every card is done and the student has used at least five vehicle types.",
        ["vehicle", "loaded", "left", "tally", "cardIndex"],
        ["M_ROUND_UP"],
        ["How many people can one vehicle carry?",
         "How many times can that number be taken out of 900 before nobody is left?",
         "Divide 900 by the number each vehicle carries; if some people are left, one more vehicle is needed.",
         "For minibuses: 900 divided by 25 is 36, and all seats are full."]),

    "digit_difference_machine": _t(
        "tool_digit_difference_machine", "Digit Difference Machine: Why Always 9?", "manipulative",
        "Take two different digits, make the two two-digit numbers, subtract the smaller from the bigger and repeat. "
        "The difference of the numbers is 9 times the difference of the digits, so every step gives a multiple of 9 "
        "and the machine always ends at 9.",
        "A machine with two digit slots, an automatic maker of the two numbers, a subtraction panel that shows the "
        "bigger and smaller number, a next-step feed that reuses the two digits of the answer, and a table that "
        "records digits, digit difference and number difference for each run.",
        ["Choose two different digits in the slots.",
         "Press Make numbers and read the two numbers formed.",
         "Press Subtract and look at the difference.",
         "Repeat with the two digits of the answer until one digit is left, then add the run to the table."],
        ["Run the machine on 3 and 7 and follow it to the end.",
         "Run it on 1 and 9, then on 2 and 8.",
         "Run it on 4 and 5. What do you notice about the first step?",
         "Find two digits whose difference of numbers is 27.",
         "Extend the table: choose digits whose digit difference is 2, 3, 5 and 7.",
         "Find the digits that give the longest run before reaching a one-digit answer."],
        ["Each difference is shown with its digit sum or digit gap, and the multiples of 9 glow in the table.",
         "A run that ends in one digit stamps the digit and adds a row to the table.",
         "A pair of equal digits is turned back with a note that the digits must be different."],
        "Every card is done and at least five rows are in the table.",
        ["digits", "numbers", "difference", "table", "cardIndex"],
        ["M_DIGIT_DIFF"],
        ["What do you notice about the differences in the table so far?",
         "Look at the digit difference and the number difference side by side.",
         "Compare the number difference with the digit difference: how many times bigger is it?",
         "For 7 and 3: the digits differ by 4, and 73 minus 37 is 36, which is 9 times 4."]),

    "square_stable": _t(
        "tool_square_stable", "Square Stable: Five on Every Side", "manipulative",
        "In a square ring of horses, a horse at a corner is counted on two sides. With 5 horses counted on each side, "
        "20 counted means fewer real horses when corners hold horses.",
        "A square stable drawn as a ring of 24 spots (4 corners and 5 spots between the corners on every side) with a "
        "tray of horse tokens, side counters for the four sides, and a total counter that counts every horse once.",
        ["Drag horse tokens to spots on the ring.",
         "Read the four side counters and the total.",
         "Move horses to corners or to side spots and watch the counters change.",
         "Press Check to see whether every side shows 5."],
        ["Place 19 horses so that every side shows 5.",
         "Count the horses one by one and find the caretaker's mistake.",
         "Place 18 horses so that every side shows 5.",
         "Try 17 horses with 5 on every side.",
         "Try 16 horses with 5 on every side.",
         "Try 15 horses with 5 on every side. What happens?"],
        ["A horse on a corner lights both its sides, and each side counter goes up by one.",
         "Side counters that read 5 turn green; the total counter shows the real number of horses.",
         "A try that cannot work is shown with the side that stays short in a warning colour."],
        "Every card is done with the stable arranged for 19, 18, 17 and 16.",
        ["horses", "sideCounters", "total", "cornerHorses", "cardIndex"],
        ["M_CORNER_TWICE"],
        ["How many sides does a horse at a corner help?",
         "Count the horses along each side, including the corner horses, and find the total another way.",
         "Add the four side counts, then subtract the horses that were counted on two sides.",
         "With 5 on each side the sides add to 20; each corner horse is counted twice, so 20 minus the corner horses "
         "is the real number."]),
}
