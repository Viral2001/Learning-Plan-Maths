# -*- coding: utf-8 -*-
"""Tool specs for T1 and T2 of Class 5 Chapter 12 (Racing Seconds): the Yoga Clock and the Day Strip. Specs only; the
tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. One activity at a time, one instruction at a time, large controls, Back and
Next in the same place, visible progress, specific feedback, hints, retry and reset. The hour hand is blue, the
minute hand orange and the seconds hand red on every clock of the chapter."""
from topics_common import T

TOOLS = {
    "yoga_clock": T(
        "tool_yoga_clock", "Yoga Clock", "manipulative",
        "Set a Start clock and a Finish clock, read the time on each, and read how much time lies between them from "
        "the shaded stretch that grows when the Finish minute hand moves forward.",
        "Raghav's yoga room, drawn as a warm, polished 3D isometric scene with soft shadows and gentle animation: a "
        "wooden floor, a yoga mat and, on the wall above it, two large analogue wall clocks side by side, named Start "
        "and Finish. The two clocks are the largest things on screen. Each clock has a dark teal rim, a pale face, "
        "every number from 1 to 12, 60 small marks, a blue hour hand and an orange minute hand, and the hour hand "
        "moves a little as the minute hand moves, like a real clock. Under each clock sits a digital read-out, hh:mm, "
        "with a switch beside it that shows a sun for a.m. and a moon for p.m. A pale orange shaded stretch grows on "
        "the Finish clock from the Start position to the Finish position as the student moves the Finish minute hand "
        "forward, and a stretch longer than 1 hour goes round again in a thin outer ring. Below the clocks a time "
        "spent box has two small number boxes, hours and minutes (the hours box can stay empty), with a large number "
        "pad and a Check button. Controls: drag the minute hand of either clock (the hour hand follows), tap the sun "
        "and moon switch of a clock, and type in the time spent box. On the cards where the tool sets the clocks, the "
        "digital read-outs are hidden and the student types the start time, the finish time and the time spent "
        "instead. Fixed controls: Hint, Retry (resets the clocks of this card), Reset (returns both clocks to the "
        "start of the tool), Back and Next in the same places on every card, and 6 progress dots, with a "
        "one-sentence instruction strip at the top and a counter showing the card number out of 6.",
        ["Look at Raghav on his mat with the two wall clocks from the story. Set the "
         "Start clock to where it was when Raghav began and the Finish clock to where it was when he stopped, and say "
         "what you notice.",
         "Set the Start clock and the Finish clock to the times on each card, read the "
         "shaded stretch and the time spent, then read two clocks that the tool sets and type the start time, the "
         "finish time and the time spent (practice values).",
         "Read the two wall clocks of Raghav's yoga from the story, shown with hands only, and "
         "type the start time, the finish time and the time spent."],
        ["Card 1 (practice values): set the Start clock to 07:10 a.m. and the Finish clock to 07:40 a.m., "
         "then read the shaded stretch. How much time is between them? Answer: 30 minutes, because the minute hand "
         "moves from 2 to 8, that is 6 numbers, and 6 × 5 = 30 minutes.",
         "Card 2 (practice values): set the Start clock to 09:35 a.m. and the Finish clock to 10:10 a.m. The "
         "shaded stretch passes the number 12. How much time is between them? Answer: 35 minutes, because 09:35 a.m. "
         "to 10:00 a.m. is 60 − 35 = 25 minutes, 10:00 a.m. to 10:10 a.m. is 10 minutes, and 25 + 10 = 35 minutes.",
         "Card 3 (practice values): set the Start clock to 08:00 a.m. and the Finish clock to 09:15 a.m. The "
         "shaded stretch goes once round and a little more. How much time is between them? Answer: 1 hour 15 "
         "minutes, because 08:00 a.m. to 09:00 a.m. is 1 hour and 09:00 a.m. to 09:15 a.m. is 15 minutes.",
         "Card 4 (practice values): set the Start clock to 06:20 a.m. and the Finish clock to 07:05 a.m. How "
         "much time is between them? Answer: 45 minutes, because 06:20 a.m. to 07:00 a.m. is 60 − 20 = 40 minutes, "
         "07:00 a.m. to 07:05 a.m. is 5 minutes, and 40 + 5 = 45 minutes.",
         "Card 5 (practice values): the tool sets the clocks for an evening. The Start clock has the hour "
         "hand between 7 and 8 and the minute hand on 3. The Finish clock has the hour hand between 7 and 8 and the "
         "minute hand on 11. Switch both to the moon, then type the start time, the finish time and the time spent. "
         "Answer: 07:15 p.m., 07:55 p.m. and 40 minutes, because 3 × 5 = 15, 11 × 5 = 55 and 55 − 15 = 40 minutes.",
         "Challenge: 'Raghav practices yoga in the morning.' The two wall clocks of the story are shown with "
         "hands only: the first has the hour hand between 5 and 6 and the minute hand on 7, and the second has the "
         "hour hand just before 6 and the minute hand on 11. 'At what time did Raghav start practising Yoga? At what "
         "time did he finish? How much time did he spend practising Yoga?' The student reads both clocks and types "
         "the three answers. Answers: 05:35 a.m., 05:55 a.m. and 20 minutes, because 7 × 5 = 35, 11 × 5 = 55 and "
         "55 − 35 = 20 minutes."],
        ["A wrong minute reading gets a soft amber note with the reason, never red. For the story's Start clock: the "
         "minute hand points at 7, so that is 7 × 5 = 35 minutes past.",
         "A wrong hour reading says which hand to look at: the short blue hand shows the hour, and the hour is the "
         "number it has just passed, so between 5 and 6 the hour is 5.",
         "A morning time typed with p.m. gets a note about the switch: the sun means a.m., the morning, and the moon "
         "means p.m., the afternoon or evening.",
         "A solved card shows how the stretch was counted, for example: 09:35 a.m. to 10:00 a.m. is 25 minutes and "
         "10:00 a.m. to 10:10 a.m. is 10 minutes, so 25 + 10 = 35 minutes.",
         "A time spent that mixes up minutes and hours, such as 15 hours for 15 minutes, gets a note to look at the "
         "shaded stretch: if the minute hand has not gone round, the time is less than 1 hour."],
        "All 6 cards are done, the three answers about Raghav's yoga are read correctly from the clocks, and the "
        "last card is finished without a bottom-out hint.",
        ["startMinute", "finishMinute", "startSunMoon", "finishSunMoon", "typedStart", "typedFinish", "typedSpent",
         "cardIndex"],
        ["M_MINUTE_NUMBER", "M_TIME_HUNDRED"],
        ["Which hand tells the hour and which hand tells the minutes? Look at the short blue hand and the long orange "
         "hand.",
         "Each number on the dial is 5 minutes. Count the minutes in fives from 12 to where the long hand points.",
         "Look at the long orange hand on your clock: how many numbers past 12 is it? Multiply that number by 5 to get "
         "the minutes.",
         "Worked step on a practice clock: the short hand is between 8 and 9, so the hour is 8. The long hand is on "
         "4, and 4 × 5 = 20 minutes, so the time is 08:20. Do the same with your clock."]),

    "day_strip": T(
        "tool_day_strip", "Day Strip", "manipulative",
        "Place a time on a strip of the whole day, read it in the 12-hour and in the 24-hour format, and see that a "
        "p.m. time sits 12 hours further along the strip than its morning twin; two markers show the time between "
        "two 24-hour times.",
        "The school notice board, drawn as a warm, polished 3D isometric scene with soft shadows and gentle animation. "
        "A long timetable strip for one whole day is pinned across the board and is the largest thing on screen. The "
        "strip has 24 hour boxes numbered 00 to 23 from left to right, the a.m. side (00 to 11) under a sun and the "
        "p.m. side (12 to 23) under a moon, with the two ends labelled 00:00 and 24:00. Two draggable markers sit on "
        "the strip, named First time and Second time, and each marker has a small analogue clock above it (blue hour "
        "hand, orange minute hand, 60 small marks) that follows the marker. Two read-outs sit under the strip for the "
        "selected marker: the 12-hour read-out, hh:mm a.m. or p.m., and the 24-hour read-out, hh:mm hours. A gap bar "
        "between the two markers shows the time between them in hours and minutes. Controls: drag a marker along the "
        "strip (it snaps to 5 minutes and stays between 01:00 hours and 23:55 hours), tap a read-out to type a time "
        "with a large number pad, a switch named Show the 12 added that draws a +12 bracket over the p.m. side, and a "
        "Check button. On a gap card the 12-hour read-out is hidden, because the gap is read in 24-hour time. For the "
        "book's match question the strip is replaced by two columns of boxes and the student taps a 12-hour time and "
        "then its 24-hour time to draw a line between them. Fixed controls: Hint, Retry (returns the markers of this "
        "card), Reset (clears both markers), Back and Next in the same places on every card, and 7 progress dots, "
        "with a one-sentence instruction strip at the top and a counter showing the card number out of 7.",
        ["Look at the strip with one morning time and one afternoon time marked, each "
         "with its 24-hour name. Drag the marker to each time and read both boxes before you press Check.",
         "Drag the marker to a time and read both boxes, turn on the +12 bracket for a p.m. "
         "time, type the 12-hour time for a given 24-hour time, and put two markers on the strip to read the gap "
         "between them (practice values).",
         "Fill the book's table of the 12-hour and 24-hour formats, match its six pairs, and find "
         "how long Raghu took to reach his Nana ji's house."],
        ["Card 1 (practice values): drag the First marker to 07:45 a.m. and read both boxes. Answer: the "
         "boxes read 07:45 a.m. and 07:45 hours, because a morning time keeps its digits in the 24-hour format.",
         "Card 2 (practice values): drag the First marker to 04:10 p.m. and turn on Show the 12 added. What "
         "does the 24-hour box read? Answer: 16:10 hours, because 4 + 12 = 16 and the minutes stay 10.",
         "Card 3 (practice values): the 24-hour box shows 21:20 hours. Drag the marker to where it goes and "
         "type the 12-hour time. Then do the same for 18:05 hours. Answer: 09:20 p.m., because 21 − 12 = 9 and the "
         "minutes stay 20, and 06:05 p.m., because 18 − 12 = 6 and the minutes stay 05.",
         "Card 4 (practice values): put the First marker at 09:25 hours and the Second marker at 11:50 hours "
         "and read the gap bar. Answer: 2 hours 25 minutes, because 09:25 hours to 11:25 hours is 2 hours and 11:25 "
         "hours to 11:50 hours is 25 minutes.",
         "Card 5 (practice values): put the First marker at 08:40 hours and the Second marker at 11:10 hours "
         "and read the gap bar. Answer: 2 hours 30 minutes, because 08:40 hours to 09:00 hours is 20 minutes, 09:00 "
         "hours to 11:00 hours is 2 hours, 11:00 hours to 11:10 hours is 10 minutes, and 20 + 10 = 30 minutes.",
         "Challenge: 'Fill in the blanks by writing the time in the appropriate format.' The table has the "
         "12-hour format on the left and the 24-hour format on the right: 05:30 a.m. = 05:30 hours; ___ = 08:35 "
         "hours; 11:55 a.m. = ___ hours; 02:30 p.m. = 14:30 hours; 05:30 p.m. = ___ hours; 09:35 p.m. = ___ hours. "
         "Then 'Match the following.' The 12-hour times 06:30 a.m., 08:45 p.m., 11:45 p.m., 04:30 a.m., 07:30 p.m., "
         "01:30 a.m. are matched to the 24-hour times 01:30 hours, 23:45 hours, 06:30 hours, 20:45 hours, 04:30 "
         "hours, 19:30 hours. Answers: 08:35 a.m., 11:55 hours, 17:30 hours and 21:35 hours; 06:30 a.m. with 06:30 "
         "hours, 08:45 p.m. with 20:45 hours, 11:45 p.m. with 23:45 hours, 04:30 a.m. with 04:30 hours, 07:30 p.m. "
         "with 19:30 hours, 01:30 a.m. with 01:30 hours.",
         "Challenge: 'Raghu left his house at 08:00 hours and arrived at his Nana ji's house at 09:05 hours. "
         "How long did he take to reach his house?' Put the markers on the two times and type the answer. Answer: "
         "1 hour 5 minutes, because 08:00 hours to 09:00 hours is 1 hour and 09:00 hours to 09:05 hours is 5 "
         "minutes."],
        ["A wrong 24-hour time for a p.m. time gets a soft amber note with the reason, never red, and the +12 bracket "
         "lights up: for 05:30 p.m., the hour 5 plus 12 is 17, the minutes stay 30, so 17:30 hours.",
         "A morning time shows its twin: the note points to the a.m. side of the strip and shows the same hour box "
         "under the marker, so 07:45 a.m. is 07:45 hours.",
         "A 24-hour time above 12 typed as a morning time gets a note: 21 is more than 12, so the marker is in the "
         "moon side of the strip, and 21 − 12 = 9 gives 09:20 p.m.",
         "A wrong gap shows the hops on the gap bar, to the next whole hour, then whole hours, then the rest, with "
         "the numbers written on the bar.",
         "A gap typed with minutes above 59 gets a note: minutes on a clock never go past 59, so recount with the "
         "hops on the bar."],
        "All 7 cards are done, the table, the six matches and the question about Raghu's trip are correct, and the "
        "last card is finished without a bottom-out hint.",
        ["firstMarker", "secondMarker", "typedTwelveHour", "typedTwentyFourHour", "typedGap", "plusTwelveShown",
         "matchedPairs", "cardIndex"],
        ["M_PM_SAME", "M_MINUTES_OVER_59"],
        ["What does the card ask: a time in the other format, or the time between two times?",
         "For a p.m. time add 12 to the hour, and for a 24-hour time above 12 take 12 away. A morning time keeps its "
         "digits and the minutes never change. For a gap, hop to the next whole hour, then whole hours, then the "
         "rest.",
         "Look at the hour of your time. Is it a morning time or a p.m. time? Then add 12 or take 12 away. For a "
         "gap, say how many minutes reach the next whole hour.",
         "Worked steps on practice times: 03:20 p.m. is a p.m. time, so 3 + 12 = 15 and it is 15:20 hours. For the "
         "gap from 14:30 hours to 16:10 hours: 14:30 hours to 15:00 hours is 30 minutes, 15:00 hours to 16:00 hours "
         "is 1 hour, 16:00 hours to 16:10 hours is 10 minutes, so 1 hour 40 minutes. Do the same with your card."]),
}
