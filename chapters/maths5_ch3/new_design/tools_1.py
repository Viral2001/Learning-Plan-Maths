# -*- coding: utf-8 -*-
"""Tool specs for T1, T2 and T3 of Class 5 Chapter 3 (Angles as Turns): Statue Turn (the free try of the intro, right
after the hook), Quarter Turn Check and Straw and Fan Angles. Specs only; the tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds are labelled practice values. One
activity at a time, one instruction at a time, large controls, Back and Next in the same place, visible progress,
Hint, Retry and Reset always present, immediate specific feedback that is never red. A turn is always shown from a fixed
start mark and told as a part of a full turn: never degrees."""
from topics_common import T

TOOLS = {
    "statue_turn": T(
        'tool_statue_turn', 'Statue Turn', 'manipulative',
        'Find out by turning a child on the spot that a full turn brings the child back to the starting position and a half turn leaves the child facing the opposite way. This is the free first try of the chapter, so it asks and shows; the video that follows names the two turns. Only full turns and half turns appear in this tool: no angle names and no fractions of a turn.',
        "The school playground at morning break, drawn as a warm 3D isometric scene with soft shadows and gentle animation. A ring is painted on the ground in the middle, and on it stands a child with one foot fixed on a mark, shown large from a high viewpoint. A teal start arrow is painted on the ground and shows the way the child faced at the start; it never moves. An orange turning arrow follows the child's face. The child's free foot leaves a trace line on the ring, so a full turn draws a complete circle and a half turn draws a half-moon, as with Ashutosh and Sahana in your maths book. An instruction strip at the top shows one sentence in large type, with progress dots under it. Controls: a big Turn button (press and hold to turn the child slowly, or drag the child round); a big STATUE! button that freezes the child; a check row under the child with three buttons, Same way as the start, Opposite way and Neither; three bins, Full turn, Half turn and Neither, for four statue picture cards; a row of explanation cards that click into an answer strip; Check, Hint, Retry (returns the child to the start for this card), Reset (restores the whole tool), Back and Next in the same places on every card. Read-outs: a facing label, Facing now: the same way as the start, the opposite way, or neither; a turn label that says Full turn or Half turn only when the child faces the start way or the opposite way; and a card number out of 6.",
        ['Look at the four children of the story who keep turning around and freeze when Statue is called. Here is one child on a ring with the start arrow on the ground. Press and hold Turn, then press STATUE! to freeze, and look at where the child faces compared with the start arrow.',
            'Turn Ashutosh until he faces the same way as at the start, turn Sahana until she faces the opposite way, freeze a child who faces neither the start way nor the opposite way, and sort four statue picture cards into Full turn, Half turn and Neither.',
            'Answer the question from the story, Can you recognise the child in the picture who has made a full turn? Who has made a half turn? How do you know? Build your answer from the cards. Then give an example of a turn from real life.'],
        ['Card 1: turn Ashutosh until he faces the same way as at the start, then press STATUE!. What has his free foot drawn, and what turn is it? Answer: a complete circle, so it is a full turn. He is back at the starting position.',
            'Card 2: turn Sahana until she faces the opposite way from the start arrow, then press STATUE!. What has her free foot drawn, and what turn is it? Answer: a half-moon, so it is a half turn. She faces the opposite way.',
            'Card 3 (practice values): turn a child until the child faces neither the start way nor the opposite way, and press STATUE!. Is it a full turn, a half turn or neither? Answer: neither. The child does not face the start way and does not face the opposite way.',
            'Card 4 (practice values): sort four statue picture cards into Full turn, Half turn and Neither. Card A faces the start way, card B faces the opposite way, card C faces neither the start way nor the opposite way, card D faces the start way. Answer: A and D go to Full turn, B goes to Half turn, C goes to Neither.',
            "Challenge: 'Can you recognise the child in the picture who has made a full turn? Who has made a half turn? How do you know? Discuss in class.' Look at the statue picture of A, B, C and D, then build your answer from the cards. Answer: A made a half turn, because A faces the opposite way. B and C made a full turn, because they face the way they faced at the start. D faces the side, so D made neither. Cards that fit: Face the same way as the start is a full turn; Face the opposite way is a half turn. Your explanation may use your own words.",
            "Challenge: 'Give examples of real-life situations where you observe turns.' Type or pick your examples. Answer: your own examples, such as a door on its hinge, a tap, a hand of a clock or a giant wheel. Your answers may differ. Next stop: the video that names a full turn and a half turn."],
        ["While the child turns, the turning arrow follows the child's face and the foot trace draws on the ring.",
            'On STATUE! the tool says where the child faces compared with the start arrow: Same way as the start: that is a full turn. Opposite way: that is a half turn.',
            'Pressing STATUE! when the child faces neither the start way nor the opposite way shows a soft amber note: This child does not face the start way or the opposite way. Turn on until it does, or call it Neither.',
            'A statue card dropped in the wrong bin slides back with a clue, for example: Where does this child face compared with the start arrow? A card in the right bin locks in with a soft chime.',
            'An explanation card that fits clicks into the answer strip. A card that does not fit slides back with a clue such as: Does this card compare the child with the start? The tool never shows the full explanation.'],
        "A full turn and a half turn have been made, the four cards are sorted, and the student has built an answer to the opener's question and given an example of a turn.",
        ['childFacing',
            'startMark',
            'footTrace',
            'cardBins',
            'explanationCards',
            'challengeIndex',
            'facingLabel'],
        ['M_SAME_FACING_NO_TURN'],
        ['Look at the start arrow on the ground. Where was the child facing at the start?',
            'Turn the child and watch the turning arrow. Compare where the child faces now with the start arrow: the same way, the opposite way, or neither?',
            'If the child faces the same way as at the start, it is a full turn. If the child faces the opposite way, it is a half turn.',
            'Turn the child until the child faces the start way for a full turn, or the opposite way for a half turn, and press STATUE!. The foot trace shows a complete circle or a half-moon.']),

    "quarter_turn_check": T(
        'tool_quarter_turn_check', 'Quarter Turn Check', 'manipulative',
        'One purpose, the quarter turn as a yardstick, in two clearly separated activities. Activity 1, Halves and quarters (a short recap of the topic before): join half turns and quarter turns on the giant wheel until they make a full turn. Activity 2, Objects that turn: open everyday objects as far as they go and compare their greatest turn with a quarter turn. Activity 2 opens after Activity 1 is done.',
        "The school fair at the edge of the playground, drawn as a warm 3D isometric scene with soft shadows and gentle animation. Two big activity tabs sit at the top, Activity 1: The giant wheel and Activity 2: Objects that turn. Only one activity is on screen at a time, and Activity 2 opens after Activity 1 is done. In Activity 1 the giant wheel fills the scene: its starting seat at the top marked E, large, with a teal start mark at E, an orange curved arrow and a shaded wedge that grow as the wheel turns, and Reema standing beside it. In Activity 2 a wooden table fills the scene with the everyday objects: a clothes clip, a door with a hinge, tongs, scissors and a file cover, each with an opening arm that can be dragged, and a book corner shown as the quarter-turn guide (a square corner marker that sits on the starting arm). An instruction strip at the top shows one sentence in large type, with progress dots under it. Controls in Activity 1: two turn buttons, Half turn and Quarter turn, that turn the wheel that much in the same direction each time they are tapped; Undo, which takes back the last turn; a row of answer cards (a half turn, a full turn). Controls in Activity 2: drag the opening arm as far as it goes (it stops at the object's own limit); a Show guide switch for the quarter-turn guide; three bins, less than a 1/4 turn, 1/4 turn and more than a 1/4 turn, and object cards to drop into them. In both: Check, Hint, Retry (returns the wheel to E or the arm to closed), Reset (restores the activity), Back and Next in the same places on every card. Read-outs: in Activity 1 the turns joined so far as a sum, for example 1/2 + 1/4 = 3/4, the total as a fraction of a full turn, and a note when the seat is back at E; in Activity 2 a note that compares the arm with the guide; and a card number, Activity 1 cards 1 to 3 and Activity 2 cards 1 to 4.",
        ['Activity 1: look at the giant wheel turning from E and coming back to E. Tap Half turn and watch the seat. How many half turns bring the seat back to E? Activity 2: look at the corner of a book beside an open door. Does the door open less than, exactly to or wider than the corner?',
            'Activity 1: join a half turn and two quarter turns, then join three quarter turns and one more. Activity 2: open a practice hinge to the quarter-turn guide, open two more practice hinges, and sort them.',
            "Activity 1: answer Reema's questions about two half turns, two quarter turns and four quarter turns. Activity 2: tick the greatest turn of the clothes clip, the door with hinge, the tongs, the scissors and the file cover."],
        ['Activity 1, card 1 (practice values): tap Half turn once and Quarter turn twice, all in the same direction. What turn is that in all? Answer: 1/2 + 2/4 = 1/2 + 1/2 = 1, a full turn, and the seat is back at E.',
            'Activity 1, card 2 (practice values): tap Quarter turn three times, then once more. What turn is that in all? Answer: 3/4 + 1/4 = 4/4 = 1, a full turn.',
            "Activity 1, card 3: 'A giant wheel makes a full turn when it comes back to the starting position E. Reema takes two half turns in the same direction. It is like a ___ turn. What happens if she takes 2 quarter turns in the same direction? It is like a ___ turn. What happens if she takes 4 quarter turns in the same direction? It is like a ___ turn.' Use the wheel, then pick the answer cards. Answer: a full turn, because 1/2 + 1/2 = 1; a half turn, because 1/4 + 1/4 = 2/4 = 1/2; a full turn, because 4/4 = 1.",
            'Activity 2, card 1 (practice values): switch on the guide and drag the arm of practice hinge H until it meets the guide. What is its turn? Answer: a 1/4 turn.',
            'Activity 2, card 2 (practice values): drag the arms of practice hinges K and L as far as they go. Compare each with the guide. Answer: K opens less than the guide, so less than a 1/4 turn. L opens wider than the guide, so more than a 1/4 turn.',
            'Activity 2, card 3 (practice values): drop the three practice object cards, H, K and L, into the three bins. Answer: H goes to 1/4 turn, K to less than a 1/4 turn, L to more than a 1/4 turn.',
            "Activity 2, card 4: 'What is the maximum possible turn in each of these cases? Check and tick.' Open the clothes clip, the door with hinge, the tongs, the scissors and the file cover as far as they go and drop each into less than a 1/4 turn, 1/4 turn or more than a 1/4 turn. Sample answer: clothes clip, less than a 1/4 turn; door with hinge, more than a 1/4 turn; tongs, less than a 1/4 turn; scissors, a 1/4 turn; file cover, more than a 1/4 turn. Your answer may differ for your own objects."],
        ['Activity 1: each tap turns the wheel and adds to the sum, for example 1/2 + 1/4 = 3/4. When the total reaches 1 the wheel stops with a soft chime and the note: The seat is back at E: a full turn.',
            'Activity 1: a wrong total shows a soft amber note, for example: Two quarter turns are 2/4, which is the same as 1/2. That is a half turn, not a full turn.',
            'Activity 2: when an arm is dragged as far as it goes, the tool shows the wedge it made and says whether it is less than, equal to or more than the guide, for example: This hinge opens wider than the guide: more than a 1/4 turn.',
            'Activity 2: an object card dropped in the wrong bin slides back with a clue, for example: Open it as far as it goes. Is it before, at or after the guide?',
            'An answer card that fits clicks into place. A card that does not fit slides back with a clue. The tool never shows the full answer.'],
        "Activity 1 is done when the wheel has been joined to a full turn in two ways and Reema's three questions are answered. Activity 2 is done when the three practice hinges are sorted and the greatest turn of the five objects is ticked.",
        ['activity',
            'wheelTurns',
            'wheelTotal',
            'armOpening',
            'guideOn',
            'objectBins',
            'answerCards',
            'challengeIndex'],
        ['M_BIGGER_DENOM_TURN',
            'M_ARM_LENGTH'],
        ['Where does the wheel start? Look at E. How far has the seat turned so far?',
            'Join the turns one after another in the same direction. How many quarter turns make a half turn, and how many make a full turn? For an object, open it as far as it goes and compare with the guide.',
            'Two half turns are 1/2 + 1/2 = 1, a full turn. Two quarter turns are 2/4 = 1/2, a half turn. Four quarter turns are 4/4 = 1, a full turn.',
            'Tap the turns for this card one at a time and watch the total reach the answer. For an object, drag the arm to its limit and read the note about the guide.']),

    "straw_fan_angles": T(
        "tool_straw_fan_angles", "Straw and Fan Angles", "manipulative",
        "Turn one arm away from a fixed arm and name the angle the turn makes: acute for less than a quarter turn, right "
        "for a quarter turn, obtuse for more than a quarter and less than a half turn, straight for a half turn, and more "
        "than a straight angle for a turn of 3/4.",
        "Pragya's desk in the classroom corner, drawn as a warm 3D isometric scene with soft shadows and gentle "
        "animation. In the middle, large, a green straw lies fixed along a teal start line and a yellow straw is joined "
        "to it by a paper clip at the corner; the yellow straw turns. A shaded orange wedge between the two straws shows "
        "the turn made. Beside the straws sits a paper fan made of folded green paper with an ice cream stick at each "
        "end; one stick is fixed and the other turns, and the fan opens like the straws. An instruction strip at the top "
        "shows one sentence in large type, with progress dots under it. Controls: drag the yellow straw (or the loose "
        "fan stick) round the clip; a Show guide switch that shows three marks, the quarter turn as a square corner "
        "marker, the half turn as a straight line and the three-quarter turn; an Add a turn button that makes the next "
        "turn start where the last one stopped; a Switch to fan button; five name cards, acute angle, right angle, "
        "obtuse angle, straight angle and more than a straight angle, to tap; Check, Hint, Retry (puts the yellow "
        "straw back on the green one), Reset (restores the straws and the fan), Back and Next in the same places on "
        "every card. Read-outs: the turn in words, less than 1/4, 1/4, between 1/4 and 1/2, 1/2, 3/4; the name of the "
        "angle once the straw stops; and a card number out of 7.",
        ["Look at the green and the yellow straw joined at the clip. Turn the yellow straw "
         "a quarter turn and see the square corner. What angle does the yellow straw make with the green one?",
         "Make a right angle, an acute angle and an obtuse angle with the straw, make a straight "
         "angle with two quarter turns, and turn on to a 3/4 turn.",
         "Use the paper fan to show different acute angles and obtuse angles, then answer whether "
         "two acute turns together can make another acute turn."],
        ["Card 1: turn the yellow straw a quarter turn from the green one and tap the name card. Answer: a "
         "right angle, a square corner.",
         "Card 2: turn the yellow straw less than a quarter turn and tap the name card. Answer: an acute "
         "angle, narrower than a right angle.",
         "Card 3: turn the yellow straw more than a quarter turn but less than a half turn and tap the name "
         "card. Answer: an obtuse angle, wider than a right angle.",
         "Card 4: turn the yellow straw a quarter turn, press Add a turn, and turn it a quarter turn more. "
         "What angle do the two straws make? Answer: 1/4 + 1/4 = 2/4 = 1/2, a half turn: a straight angle, the two "
         "straws lie in one straight line.",
         "Card 5: turn the yellow straw on to a 3/4 turn and tap the name card. Answer: more than a straight "
         "angle, because 3/4 is more than 1/2.",
         "Challenge: 'Use your paper fan to show different acute angles and obtuse angles.' Switch to the fan "
         "and open it to two acute angles and two obtuse angles; the tool names each one. Answer: any opening less "
         "than a quarter turn is acute; any opening more than a quarter turn and less than a half turn is obtuse. Your "
         "answer may differ.",
         "Challenge: 'Make an acute turn with the straws or fan. Continue to make another acute turn. Can the "
         "two acute turns together make another acute turn?' Use Add a turn after the first turn, try two small turns "
         "and then two bigger turns. Answer: sometimes. Two small acute turns together can be acute. Two bigger acute "
         "turns together can make a right angle or an obtuse angle."],
        ["As the straw turns, the wedge grows and the read-out shows the turn in words. When the straw stops, the name "
         "card that fits lights up softly.",
         "A name card that does not fit slides back with a clue, for example: The straw is less than the quarter-turn "
         "mark. Is that wider or narrower than a right angle?",
         "With the guide on, the straw snaps lightly to the quarter-turn mark and the half-turn mark, and the tool says, "
         "for example: This is exactly a quarter turn: a right angle.",
         "After Add a turn the tool shows the two turns joined as a sum, for example 1/4 + 1/4 = 1/2, and names the "
         "angle they make together.",
         "On the fan the same wedge and names appear, and the tool counts how many different acute and obtuse angles "
         "have been shown."],
        "The five practice angles are made and named, the fan shows two acute and two obtuse angles, and the student has "
        "answered the question about two acute turns.",
        ["strawTurn", "turnInWords", "guideOn", "addedTurns", "fanOpening", "nameCards", "challengeIndex"],
        ["M_ARM_LENGTH", "M_ACUTE_ADD_ACUTE", "M_STRAIGHT_NOT_ANGLE"],
        ["Which straw is fixed and which one turns? Look at the green straw and the yellow straw.",
         "Compare the turn with the quarter-turn mark: is the yellow straw before the mark, at the mark or past it? Then "
         "compare it with the half-turn mark.",
         "Less than a quarter turn is acute. Exactly a quarter turn is right. More than a quarter and less than a half "
         "is obtuse. A half turn is a straight angle.",
         "Turn the yellow straw to the mark that fits this card and tap the matching name card. For the two acute "
         "turns, add two small turns and read the total."]),
}
