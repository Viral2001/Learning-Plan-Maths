# -*- coding: utf-8 -*-
"""Tool specs for T5 and T6 of Class 5 Chapter 12 (Racing Seconds): the Time Converter Line and the Time Jumper. Specs
only; the tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. One activity at a time, one
instruction at a time, large controls, Back and Next in the same place, visible progress, specific feedback, hints,
retry and reset. The hour hand is blue, the minute hand orange and the seconds hand red on every clock of the chapter."""
from topics_common import T

TOOLS = {
    "double_number_line": T(
        "tool_double_number_line", "Time Converter Line", "manipulative",
        "Change one unit of time into the next on a double number line: hours into minutes, and minutes into seconds, "
        "where every step multiplies by 60, and back again by finding how many whole groups of 60 fit and what is left.",
        "The school notice board, drawn as a warm, polished 3D isometric scene with soft shadows and gentle animation: a "
        "long strip of paper pinned across the board carries a double number line, the largest thing on screen. The top "
        "line and the bottom line run side by side with aligned ticks, one tick below each tick. A mode switch above "
        "the strip reads Hours and minutes or Minutes and seconds: in the first mode the top line shows hours (0 to 12) "
        "and the bottom line minutes (0 to 720), in the second the top line shows minutes (0 to 25) and the bottom line "
        "seconds (0 to 1500). A bright slider with a handle sits on both lines at once and moves along them, snapping "
        "to a whole number on the top line, with the two numbers it points at shown in two read-out boxes. Curved arrows "
        "named × 60, × 2 and × 5 can be shown above the line with a button Show × 60. Blank ticks show a number box: "
        "tapping a box opens a large number pad. A groups of 60 strip under the bottom line can be switched on: it "
        "cuts the bottom number into whole blocks of 60 and shows the part that is left over as a short block. "
        "Controls: drag the slider, tap the mode switch, tap a blank box and type, tap Show × 60 and the groups of 60 "
        "switch, and tap Check. For a conversion card with hours and minutes, a sentence with blanks sits under the "
        "line, for example 1 hour 10 minutes = ___ minutes, and the student types the blanks. Fixed controls: Hint, "
        "Retry (clears the boxes of this card), Reset (restores the line), Back and Next in the same places on every "
        "card, and 7 progress dots, with a one-sentence instruction strip at the top and a counter showing the card "
        "number out of 7.",
        ["Look at the double number line with 1 hour above 60 minutes and 2 hours "
         "above 120 minutes, as in the video. Slide to 3 hours and read the minutes.",
         "Slide along the line and read the minutes for a number of hours, type the minutes "
         "for hours and minutes together, find the hours and minutes for a number of minutes with the groups of 60 "
         "strip, and then do the same with minutes and seconds (practice values).",
         "Fill the blanks of the book's two double number lines and its conversions, and find the "
         "total time Raghav studied."],
        ["Card 1 (practice values): slide to 5 hours and read the minutes, then slide to 10 hours. Answer: 300 "
         "minutes and 600 minutes, because 5 × 60 = 300 and 10 × 60 = 600.",
         "Card 2 (practice values): type the minutes for 6 hours 40 minutes. Answer: 400 minutes, because 6 × "
         "60 = 360 and 360 + 40 = 400.",
         "Card 3 (practice values): the line shows 470 minutes. Switch on the groups of 60 strip and type the "
         "hours and the minutes. Answer: 7 hours 50 minutes, because 60 × 7 = 420 and 470 − 420 = 50.",
         "Card 4 (practice values): switch to Minutes and seconds, slide to 3 minutes and read the seconds, then "
         "type the seconds for 7 minutes 20 seconds. Answer: 180 seconds, and 440 seconds, because 3 × 60 = 180, 7 × 60 "
         "= 420 and 420 + 20 = 440.",
         "Card 5 (practice values): the line shows 500 seconds. Switch on the groups of 60 strip and type the "
         "minutes and the seconds. Answer: 8 minutes 20 seconds, because 60 × 8 = 480 and 500 − 480 = 20.",
         "Challenge: 'Use the double number line below to complete the conversions.' The line has hours above: "
         "1 hour, ___, 4 hours, 7 hours, ___, 9 hours, ___, ___ and minutes below: 60 minutes, 120 minutes, ___, ___, "
         "480 minutes, ___, 660 minutes, 720 minutes. 'Do as instructed. You can use the above double number line for "
         "the following conversions.' (i) 1 hour 10 minutes = ___ minutes (ii) 2 hours 45 minutes = ___ minutes (iii) 3 "
         "hours 15 minutes = ___ minutes (iv) 4 hours 20 minutes = ___ minutes (v) 75 minutes = ___ hour ___ minutes "
         "(vi) 150 minutes = ___ hours ___ minutes (vii) 220 minutes = ___ hours ___ minutes (viii) 390 minutes = ___ "
         "hours ___ minutes. Answers: hours 2, 8, 11, 12 and minutes 240, 420, 540; (i) 70, (ii) 165, (iii) 195, (iv) "
         "260 minutes; (v) 1 hour 15 minutes, (vi) 2 hours 30 minutes, (vii) 3 hours 40 minutes, (viii) 6 hours 30 "
         "minutes.",
         "Challenge: 'Fill in the blanks in the double number line to complete the conversions.' The line has "
         "minutes above: 1 minute, ___, 5 minutes, 10 minutes, 15 minutes, ___, ___ and seconds below: 60 seconds, 120 "
         "seconds, ___, ___, ___, 1200 seconds, 1500 seconds. Then (i) 320 seconds = ___ minutes ___ seconds (ii) 225 "
         "seconds = ___ minutes ___ seconds (iii) 700 seconds = ___ minutes ___ seconds (iv) 1,000 seconds = ___ minutes "
         "___ seconds (v) 10 minutes 13 seconds = ___ seconds (vi) 4 minutes 8 seconds = ___ seconds (vii) 15 minutes "
         "40 seconds = ___ seconds. And: 'Raghav studies Mathematics, English, Hindi, and The World Around Us subjects. "
         "He took 50 minutes to study each of the subjects. Find the total time taken in hours and minutes. Share your "
         "strategies with your class.' Answers: minutes 2, 20, 25 and seconds 300, 600, 900; (i) 5 minutes 20 seconds, "
         "(ii) 3 minutes 45 seconds, (iii) 11 minutes 40 seconds, (iv) 16 minutes 40 seconds, (v) 613 seconds, (vi) 248 "
         "seconds, (vii) 940 seconds; 3 hours 20 minutes."],
        ["Sliding along the line shows both numbers at once and the arrow × 60: the bottom number is always 60 times the "
         "top number, and the read-out says so, for example 5 hours is 5 × 60 = 300 minutes.",
         "A wrong number in a blank makes the box blink with a soft amber note and the reason, never red: the top number "
         "is 4, so the bottom number is 4 × 60 = 240, not 400. The answer is never typed for the student.",
         "The groups of 60 strip shows why minutes become hours: 470 minutes is 7 blocks of 60 and a short block of 50, "
         "so 7 hours 50 minutes.",
         "A minutes part above 59 in an answer such as 1 hour 75 minutes gets a note: 75 minutes is 1 hour 15 minutes, "
         "so cut the hours out first.",
         "A bottom number made by adding 100 for each hour gets a note: 1 hour is 60 minutes, not 100 minutes, so each "
         "step is 60."],
        "All 7 cards are done, the two double number lines and the conversions of the book are filled correctly, the "
        "total study time is right, and the last card is finished without a bottom-out hint.",
        ["mode", "sliderTop", "sliderBottom", "typedBlanks", "groupsOfSixtyShown", "multiplyArrowShown", "typedHours",
         "typedMinutes", "typedSeconds", "cardIndex"],
        ["M_TIME_HUNDRED"],
        ["Which unit is bigger, and which is smaller? Look at the top line and the bottom line of the strip.",
         "How many of the small unit make one of the bigger unit? Each step along the line goes up by that many.",
         "To go to the smaller unit, multiply by 60. To go to the bigger unit, find how many whole groups of 60 fit and "
         "keep what is left.",
         "Worked step on a practice line: 130 minutes. 60 × 2 = 120 and 130 − 120 = 10, so it is 2 hours 10 minutes. Do "
         "the same with the numbers on your card."]),

    "time_jumper": T(
        "tool_time_jumper", "Time Jumper", "manipulative",
        "Find the time after, or before, a time by hopping along a time line, the hours first and then the minutes up "
        "to the next whole hour, and see the a.m. and p.m. change at 12 noon and a new day begin after midnight.",
        "The school playground, drawn as a warm, polished 3D isometric scene with soft shadows and gentle animation: a "
        "long hopscotch line chalked on the ground is a time line and is the largest thing on screen. The line has a "
        "tall tick for every whole hour and 5 small ticks of 5 minutes between them, with the hours labelled; the "
        "left part of the line has a sun and the label a.m., the right part has a moon and the label p.m., 12 noon "
        "has a bright marker, and after 12 midnight a band named Next day starts. A small flag stands at the start "
        "time and a child's shoe hops from the flag to the landing time. Jump cards sit in a tray under the line: 1 "
        "hour, 30 minutes, 10 minutes, 5 minutes and 1 minute, each with a Forward and a Back side. A read-out beside "
        "the line shows the landing time in the 12-hour format (hh:mm a.m. or p.m.) and a second read-out shows the "
        "24-hour time (hh:mm hours); a small clock with a blue hour hand and an orange minute hand follows the "
        "landing time. Controls: drag a jump card onto the line (the shoe hops by that much and the landing time "
        "updates), tap Undo to take the last jump off, tap Forward or Back to choose the direction of the card, type "
        "the end time with a large number pad, and tap Check. Fixed controls: Hint, Retry (returns the shoe to the "
        "start of this card), Reset (clears every jump), Back and Next in the same places on every card, and 7 "
        "progress dots, with a one-sentence instruction strip at the top and a counter showing the card number out of "
        "7.",
        ["Look at the flag at 03:20 p.m. and one jump of 1 hour, as in the video. Say "
         "where the shoe lands and what is left to add.",
         "Drag jump cards to find the time after a time, then the time before a time, then a "
         "time after that passes 12 noon, and one that passes midnight (practice values).",
         "Solve the book's time problems by hopping and type each time."],
        ["Card 1 (practice values): the flag is at 02:10 p.m. Hop forward 1 hour 35 minutes with an hour card "
         "and minute cards. Where does the shoe land? Answer: 03:45 p.m., because 02:10 p.m. plus 1 hour is 03:10 p.m. "
         "and 03:10 p.m. plus 35 minutes is 03:45 p.m.",
         "Card 2 (practice values): the flag is at 07:50 p.m. Hop back 2 hours 20 minutes. Where does the shoe "
         "land? Answer: 05:30 p.m., because 07:50 p.m. minus 2 hours is 05:50 p.m. and 05:50 p.m. minus 20 minutes is "
         "05:30 p.m.",
         "Card 3 (practice values): the flag is at 11:25 a.m. Hop forward 1 hour 50 minutes and watch 12 noon. "
         "Where does the shoe land? Answer: 01:15 p.m., because 11:25 a.m. plus 1 hour is 12:25 p.m. and 12:25 p.m. "
         "plus 50 minutes is 01:15 p.m. The a.m. changed to p.m. at 12 noon.",
         "Card 4 (practice values): the flag is at 11:10 p.m. Hop forward 3 hours 20 minutes and watch "
         "midnight. Where does the shoe land? Answer: 02:30 a.m. the next day, because 23:10 hours plus 3 hours 20 "
         "minutes is 26:30 hours, and 26 − 24 = 2.",
         "Card 5 (practice values): the flag is at 04:40 p.m. and the shoe has to land on 06:15 p.m. Choose the "
         "jump cards. Answer: 1 hour 35 minutes, for example 20 minutes to 05:00 p.m., 1 hour to 06:00 p.m. and 15 "
         "minutes to 06:15 p.m., and 20 + 15 = 35 minutes.",
         "Challenge: 'Jyoti went to play at 06:15 PM. She came back after 1 hour 45 minutes. At what time did "
         "she reach home?' 'Ragini took 1 hour 10 minutes to do her homework. She finished it at 09:40 PM. What time "
         "did she start?' 'A group of children left for a picnic at 08:30 AM. They returned after 4 hours and 10 "
         "minutes. At what time did they return?' 'Raji started her homework at 06:00 PM. She finished her homework in "
         "1 hour 30 minutes. At what time did she finish?' 'Alya goes out to play at 05:30 PM and comes back after 1 "
         "hour 10 minutes. At what time does she come back?' Answers: 08:00 PM, 08:30 PM, 12:40 PM, 07:30 PM and 06:40 "
         "PM.",
         "Challenge: 'If the lunch break of a school starts at 12:30 PM and ends in 35 minutes, what time will "
         "lunch end?' 'It is 08:35 PM right now. What time will it be after 8 hours and 25 minutes?' Answers: 01:05 PM, "
         "and 05:00 AM the next day, because 20:35 hours plus 8 hours 25 minutes is 29:00 hours and 29 − 24 = 5."],
        ["A jump makes the shoe hop and the landing time update at once, with the 24-hour time beside it, so the student "
         "sees what each hop does.",
         "A wrong end time gets a soft amber note with the reason, never red: from 07:15 PM, 45 minutes reach 08:00 PM, "
         "not 07:60 PM, because minutes on a clock never go past 59.",
         "When the shoe passes 12 noon the a.m. sun changes to the p.m. moon with a short note, and when it passes "
         "midnight the Next day band lights up and the 24-hour read-out goes back to 00:00 hours.",
         "A time typed with the wrong a.m. or p.m. gets a note that points to the sun and moon on the line: after 12 "
         "noon the time is p.m.",
         "A backward hop typed as a forward hop gets a note: the time before is earlier on the line, so the shoe hops "
         "to the left."],
        "All 7 cards are done, the seven time problems of the book are answered correctly, and the last card is "
        "finished without a bottom-out hint.",
        ["startTime", "jumps", "direction", "landingTime", "typedTime", "noonPassed", "midnightPassed", "cardIndex"],
        ["M_MINUTES_OVER_59", "M_PAST_24", "M_NOON_AM"],
        ["Are you finding the time after or the time before? Which way along the line does the shoe hop?",
         "Hop the hours first. Then ask: how many minutes to the next whole hour, and how many minutes are left?",
         "Drag the hour card first, then the minute cards. Check where the shoe lands after the hour card, then add "
         "the minutes that are left.",
         "Worked step on a practice card: 02:45 p.m. plus 1 hour is 03:45 p.m., and 15 minutes reach 04:00 p.m., so "
         "the first jumps are 1 hour and 15 minutes. Do the same with your card."]),
}
