# -*- coding: utf-8 -*-
"""Tool specs for T6 and T7 of Class 5 Chapter 3 (Angles as Turns): Minute Hand Turner and Turn and Face. Specs only; the
tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds are labelled practice values. One activity at a
time, one instruction at a time, large controls, Back and Next in the same place, visible progress, Hint, Retry and Reset
always present, immediate specific feedback that is never red. A turn is always told as a part of a full turn: never
degrees."""
from topics_common import T

TOOLS = {
    "minute_hand_turner": T(
        "tool_minute_hand_turner", "Minute Hand Turner", "manipulative",
        "Link the minutes the minute hand moves to the fraction of a full turn it makes: 60 minutes is a full turn, so 15 "
        "minutes is a 1/4 turn, 30 is a 1/2 turn, 45 is a 3/4 turn and 5 minutes is a 1/12 turn, and the hand turns from "
        "the place where it starts.",
        "The clock on the school wall, drawn as a warm 3D isometric scene with soft shadows and gentle animation. The "
        "clock face is large and fills the middle of the screen, with the numbers 1 to 12 and a ring of minute marks, "
        "and a long minute hand. A teal dot marks the starting place of the hand; an orange shaded sweep grows from the "
        "start as the hand turns, and a curved arrow follows the hand in the way a clock moves. An instruction strip at "
        "the top shows one sentence in large type, with progress dots under it. Controls: drag the minute hand the way a "
        "clock moves (it snaps to the 5 minute marks, and a Show single minutes switch adds the minute marks between); "
        "plus 5 and minus 5 minute buttons; a Start at selector that places the starting dot at any number of the clock; "
        "fraction cards, 1/12, 1/6, 1/4, 1/3, 1/2 and 3/4, to tap so that the hand turns that part; answer boxes for the "
        "turn and for the minutes; Check, Hint, Retry (returns the hand to its starting place), Reset (restores the "
        "clock), Back and Next in the same places on every card. Read-outs: moved by a number of minutes; turn as a "
        "fraction of a full turn; the number the hand points at now; and a card number out of 7.",
        ["Look at the minute hand turning from 12 round to 3 in the video. Drag it and "
         "watch the minutes. How many minutes is a full turn of the minute hand?",
         "Move the hand by minutes from different starting places and read the turn, give the "
         "hand a fraction card and read the minutes, and find where the hand stops.",
         "The book's questions about the minute hand: the turn after 15, 30 and 45 minutes, and the "
         "minutes after turns of 1/12, a full circle, 1/6 and 4/12, with the starting place of the hand given each time."],
        ["Card 1 (practice values): start at 12 and move the hand 20 minutes. What turn is it, and where does the "
         "hand stop? Answer: 20 × 3 = 60, so it is a 1/3 turn. The hand stops at 4.",
         "Card 2 (practice values): start at 6 and move the hand 5 minutes. What turn is it? Answer: 60 ÷ 12 = 5, "
         "so 5 minutes is a 1/12 turn. The hand stops at 7.",
         "Card 3 (practice values): start at 2 and move the hand 25 minutes. What turn is it, and where does the "
         "hand stop? Answer: 25 ÷ 5 = 5 pieces of 1/12, so it is a 5/12 turn. The hand starts at the 10 minute mark and "
         "stops at the 35 minute mark, the number 7.",
         "Card 4: tap the fraction card 1/2. How many minutes does the hand move? Answer: 30 minutes, because "
         "30 × 2 = 60.",
         "Card 5 (practice values): start at 8 and move the hand 40 minutes. What turn is it, and where does the "
         "hand stop? Answer: 40 ÷ 5 = 8 pieces of 1/12, so it is an 8/12 turn. The hand starts at the 40 minute mark and "
         "stops at the 20 minute mark, the number 4.",
         "Challenge: 'Guess the measure of turns the minute hand of a clock makes in each of the following "
         "cases. The initial position of the minute hand is given. Draw the final position of the minute hand on the "
         "clock face. Discuss your reasoning in class. (a) When the minute hand moves by 15 minutes, it has made a ___ turn of the circle. (b) When the "
         "minute hand moves by 30 minutes, it has made a ___ turn of the circle. (c) When the minute hand moves by 45 "
         "minutes, it has made a ___ turn of the circle.' The hand starts at 3 in (a), at 6 in (b) and at 9 in (c). "
         "Answer: (a) 1/4 turn, the hand stops at 6; (b) 1/2 turn, it stops at 12; (c) 3/4 turn, it stops at 6.",
         "Challenge: '(d) When the minute hand has turned by 1/12 of a full turn, it has moved by ___ minutes. "
         "(e) When the minute hand has turned a full-circle, it has moved by ___ minutes. (f) When the minute hand has "
         "turned by 1/6 of a full turn, it has moved by ___ minutes. (g) When the minute hand has turned by 4/12 of a "
         "full turn, it has moved by ___ minutes.' The hand starts at 1 in (d), at 12 in (e), at 2 in (f) and at 4 in (g). "
         "Answer: (d) 5 minutes, it stops at 2; (e) 60 minutes, it stops at 12; (f) 10 minutes, it stops at 4; (g) 20 "
         "minutes, it stops at 8."],
        ["As the hand moves, the sweep grows and the read-outs show the minutes moved and the turn as a fraction of a "
         "full turn, for example 15 minutes, a 1/4 turn.",
         "A wrong turn shows a soft amber note, for example: A full turn is 60 minutes. 15 minutes is 15 × 4 = 60, so it is "
         "a 1/4 turn.",
         "The hand always turns from the starting dot, not from 12, and the tool says so, for example: The hand started at "
         "2, so it stops at 7, not at 5.",
         "A fraction card turns the hand that part of a full turn and shows the minutes, for example: 1/12 of 60 minutes "
         "is 5 minutes.",
         "When the hand is back on the starting dot the note says: a full turn, 60 minutes."],
        "The five practice cards are done with the turn and the stopping place read correctly, and the student has answered "
        "all seven parts of the book's minute hand question.",
        ["startNumber", "minutesMoved", "turnFraction", "handPointsAt", "fractionCards", "answerBoxes", "challengeIndex"],
        ["M_CLOCK_FROM_12", "M_BIGGER_DENOM_TURN"],
        ["Where does the minute hand start? Look at the teal dot, not always the 12.",
         "A full turn of the minute hand is 60 minutes. How many minutes is a 1/12 turn? Use that to find the turn or the "
         "minutes.",
         "A 1/12 turn is 5 minutes, a 1/4 turn is 15, a 1/2 turn is 30, a 3/4 turn is 45. Count 5 minute steps for this "
         "card.",
         "Tap plus 5 until the read-out shows the minutes for this card, read the turn, and see which number the hand "
         "points at."]),

    "turn_and_face": T(
        'tool_turn_and_face', 'Turn and Face', 'manipulative',
        'Find the direction faced after turns of right angles. Activity 1 is a short recap of clockwise and anti-clockwise: clockwise is the way the hands of a clock move and anti-clockwise is the other way. Activity 2 is the main work: turn a child on a compass by right angles from a starting direction and read the final direction faced.',
        'A compass painted on the playground ground, drawn as a warm 3D isometric scene with soft shadows and gentle animation. The compass is large in the middle, with North at the top, East on the right, South at the bottom and West on the left, each named on a signboard, and a child stands at the centre and turns on the spot. A small clock sits in the corner with its hand moving the way a clock moves, to show clockwise. Two activity tabs sit at the top, Activity 1: Which way? (a short recap) and Activity 2: Where do I face?; only one is on screen at a time, and Activity 2 opens after Activity 1 is done. An instruction strip at the top shows one sentence in large type, with progress dots under it. Controls: two big buttons, Clockwise and Anti-clockwise, that pick the direction; turn buttons, 1 right angle and 1/2 right angle, that turn the child that much in the picked direction each time they are tapped; Undo, which takes back the last turn; a Start facing selector for North, East, South and West; answer boxes for the ending direction; Check, Hint, Retry (returns the child to the starting direction), Reset (restores the tool), Back and Next in the same places on every card. Read-outs: the turns made so far as a sum of right angles, for example 2 right angles clockwise; the direction faced now; and a card number, Activity 1 card 1 and Activity 2 cards 1 to 6.',
        ['Activity 1, a short recap: look at the arrow turning the way a clock moves. Press Clockwise and watch the child turn one right angle, then press Anti-clockwise and watch the child turn the other way.',
            'Activity 2: turn the child by right angles from different starting directions, clockwise and anti-clockwise, and read the direction faced at the end.',
            'Activity 2: complete the table of directions after turns, and find the place Padma faces after a half turn clockwise and another way to turn to face it.'],
        ['Activity 1, recap, card 1: start facing North. Press Clockwise and turn 1 right angle, then undo, press Anti-clockwise and turn 1 right angle. Which way did the child go each time, and where does each end? Answer: clockwise went the way a clock moves, from North to East; anti-clockwise went the other way, from North to West.',
            'Activity 2, card 1 (practice values): start facing East. Press Clockwise and turn 1 right angle. Which direction do you face? Answer: South. The clockwise order is North, East, South, West.',
            'Activity 2, card 2 (practice values): start facing West. Press Anti-clockwise and turn 3 right angles. Which direction do you face? Answer: North. Anti-clockwise from West the order is South, East, North.',
            'Activity 2, card 3: start facing North and turn a half turn, 2 right angles, clockwise. Then undo and turn a half turn anti-clockwise. Where does each end? Answer: both end facing South. A half turn ends in the same place either way.',
            'Activity 2, card 4: start facing North and turn 1 right angle clockwise, then undo and turn 1 right angle anti-clockwise. Where does each end? Answer: East and West. A quarter turn ends in different places.',
            "Activity 2, card 5: 'The children in a class are playing a game in which the teacher tells them the direction in which they should rotate. Complete the table by filling the direction the children will face on completing the given turns. The starting direction is given in the table.' The seven rows of your maths book are used. Answer: South, North, East, West, East, South, and for the last row the number is not printed, so the rule is shown (if it is 3, North).",
            "Activity 2, card 6: 'Padma is facing the toy shop. What place will she face if she takes a half turn clockwise? What other way can she turn to face the same place?' Answer: Padma faces the ice cream cart, and she can also take a half turn anti-clockwise."],
        ['Each tap turns the child and adds to the sum, for example 2 right angles clockwise, and the direction faced now is shown on the compass.',
            'A wrong ending direction shows a soft amber note, for example: From North, clockwise: East, South. 2 right angles end at South.',
            'Turns of 4 right angles are shown as a full turn with the note: back where you started. 5 right angles are shown as 4 right angles and 1 more.',
            'Half a right angle turns the child half way between two directions, and two of them together make 1 right angle.'],
        'The recap card is done, the four turning cards are done, the table is complete, and the student has named the place Padma faces and another way to turn to it.',
        ['activity',
            'startFacing',
            'turnDirection',
            'turnsSoFar',
            'facingNow',
            'answerBoxes',
            'challengeIndex'],
        ['M_DIR_SAME_END'],
        ['Which way do the hands of a clock go? Clockwise is that way, and anti-clockwise is the other way.',
            'A right angle is a quarter turn, one step round the compass. Clockwise goes North, East, South, West. Count the steps one at a time.',
            'From the starting direction move the number of right angles, one step each, the way the card says. Four steps bring you back.',
            'Pick the direction, tap 1 right angle the number of times for this card, and read the direction faced now.']),
}
