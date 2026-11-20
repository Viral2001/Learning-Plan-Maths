# -*- coding: utf-8 -*-
"""Tool spec for T4 of Class 5 Chapter 12 (Racing Seconds): the Seconds Clock. Spec only; the tool page is built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. One
activity at a time, one instruction at a time, large controls, Back and Next in the same place, visible progress,
specific feedback, hints, retry and reset. The hour hand is blue, the minute hand orange and the seconds hand red on
every clock of the chapter."""
from topics_common import T

TOOLS = {
    "seconds_clock": T(
        "tool_seconds_clock", "Seconds Clock", "manipulative",
        "Run the seconds hand, mark where it started, and read how many seconds have passed from the numbers it moved "
        "over, five seconds for each number; then drag the seconds hand to the place where it stops after a given number "
        "of seconds, and see the minute hand step on when the hand goes once round.",
        "The timing board beside the school track, drawn as a warm, polished 3D isometric scene with soft shadows and "
        "gentle animation: a post with one very large analogue clock on it, the largest thing on screen, with a dark "
        "teal rim, a pale face, every number from 1 to 12, 60 small marks, a short blue hour hand, a long orange minute "
        "hand and a thin red seconds hand. A ring of small labels 5, 10, 15, ..., 60 sits just outside the dial, one "
        "label beside each number. A pale copy of the seconds hand, named the start ghost, stays where the run began. A "
        "pale red stretch is shaded round the dial from the start ghost to the seconds hand. A box named Seconds "
        "counted shows the number of seconds, and a small step light beside the minute hand blinks when the seconds "
        "hand passes 12 and the minute hand moves on by one mark. Controls: Go (the seconds hand runs, one mark at a "
        "time, at a slow speed so it can be watched) and Stop, Mark start, a button Run for N seconds on the cards "
        "that say how many seconds, drag the seconds hand with a finger, type a number of seconds with a large number "
        "pad, and Check. On the book's cards two clocks sit side by side, a left clock and a right clock, as in the "
        "pictures, and the student types the seconds taken or drags the missing seconds hand onto the right clock. "
        "Fixed controls: Hint, Retry (returns the hand to the start of this card), Reset (returns the clock to 12), "
        "Back and Next in the same places on every card, and 7 progress dots, with a one-sentence instruction strip at "
        "the top and a counter showing the card number out of 7.",
        ["Look at the seconds hand on 3 and then on 8, as in the video. Press Go and "
         "watch the red hand. Say how many seconds have passed when it stops.",
         "Run the seconds hand and read the seconds taken from the start ghost, run it past 12 "
         "and watch the minute hand step on, and drag the seconds hand to where it stops after a number of seconds "
         "(practice values).",
         "Read the four pairs of clocks of the book and write the seconds taken, then draw the "
         "missing seconds hand on the right clock of the four pairs of the second book box."],
        ["Card 1 (practice values): the seconds hand starts on 12. Press Go and press Stop when the hand is on "
         "3. How many seconds have passed? Answer: 15 seconds, because each number is 5 seconds and 3 × 5 = 15.",
         "Card 2 (practice values): the seconds hand starts on 2. Mark the start, press Go and press Stop on "
         "11. How many seconds? Answer: 45 seconds, because 2 is 10 seconds, 11 is 55 seconds and 55 − 10 = 45.",
         "Card 3 (practice values): the seconds hand starts on 10 and stops on 4, after it has gone past 12. "
         "Watch the step light. How many seconds? Answer: 30 seconds, because from 10 to 12 is 60 − 50 = 10 seconds, "
         "from 12 to 4 is 4 × 5 = 20 seconds, and 10 + 20 = 30 seconds. The minute hand moved on by one mark.",
         "Card 4 (practice values): the seconds hand is on 7. It runs for 40 seconds. Drag the seconds hand to "
         "where it stops and say what the minute hand does. Answer: on 3, because 7 is 35 seconds, 35 + 40 = 75, 75 − "
         "60 = 15 seconds, and 15 ÷ 5 = 3; the hand went past 12 once, so the minute hand moves on by one mark.",
         "Card 5 (practice values): the seconds hand starts on 5. Press Run for 60 seconds. Where does the hand "
         "stop and what happens to the minute hand? Answer: the hand is back on 5 and the minute hand has moved on by "
         "one mark, because one full round is 60 seconds, which is 1 minute.",
         "Challenge: 'Observe the clocks and fill in the blanks.' Four pairs of clocks, each with the seconds "
         "hand on the left clock and on the right clock: 'Rani took ___ seconds to get out of her bed.' (the seconds hand "
         "on 12 and then on 6), 'Raghav took ___ seconds to move from his room to the kitchen.' (on 12 and then on 7), "
         "'Ritu took ___ seconds to pick up a piece of paper from the floor.' (on 9 and then on 12), 'Raghu took ___ seconds "
         "to wash his spoon and plate.' (on 5 both times, with the minute hand one mark on). Answers: 30 seconds, 35 "
         "seconds, 15 seconds and 60 seconds.",
         "Challenge: 'Draw the missing seconds hand on the clocks on the right side.' Four pairs of clocks, the "
         "right clock of each with no seconds hand: 'Raghu took 20 seconds to read a sentence in his book.' (the left "
         "hand on 12), 'Rani took 30 seconds to color a rectangle.' (on 12), 'Raghav took 60 seconds to move from his home "
         "to the garden.' (on 9), 'Ritu took 40 seconds to wash a plate.' (on 11). Answers: the hand on 4, on 6, on 9 "
         "again with the minute hand one mark on, and on 7 with the minute hand one mark on."],
        ["The seconds taken are shown on the stretch as the hand moves, so the student sees the count grow in fives: 5, "
         "10, 15, and the Seconds counted box gives the same number.",
         "A wrong number of seconds gets a soft amber note with the reason, never red: from 9 to 12 the hand passes 3 "
         "numbers, so 3 × 5 = 15 seconds, and the stretch is shaded on the clock.",
         "A hand dragged to the wrong number is not moved back by the tool: the stretch from the start to the dragged "
         "hand is shaded and its seconds are written, and the student sees that they do not match the seconds asked "
         "for.",
         "When the hand goes past 12 the step light blinks and a note says that the minute hand moves on by one mark "
         "each time the seconds hand goes once round, and that 60 seconds is 1 minute.",
         "A hand on the same number at the start and the end gets a note to look at the minute hand: if it has moved on "
         "by one mark, one full round has passed, which is 60 seconds."],
        "All 7 cards are done, the four seconds taken and the four drawn hands of the book are correct, and the last "
        "card is finished without a bottom-out hint.",
        ["startNumber", "endNumber", "secondsRun", "passedTwelve", "minuteSteps", "typedSeconds", "draggedNumber",
         "cardIndex"],
        ["M_ROUND_ZERO", "M_HAND_SUBTRACT", "M_MINUTE_NUMBER"],
        ["Which hand is the seconds hand? It is the thin red hand. Where did it start and where did it stop?",
         "Each number on the dial is 5 seconds. Count the numbers from the start to the stop, and say the seconds in "
         "fives.",
         "Change the start and the stop to seconds, for example 9 is 9 × 5 = 45 seconds. If the hand passed 12, count "
         "to 12 first and then on.",
         "Worked step on a practice clock: the hand goes from 4 to 9. 4 × 5 = 20 seconds and 9 × 5 = 45 seconds, and "
         "45 − 20 = 25 seconds. Do the same with the numbers on your card."]),
}
