# -*- coding: utf-8 -*-
"""Tool specs for T4 and T5 of Class 5 Chapter 3 (Angles as Turns): Turn Disc and Angle Check and Draw. Specs only; the
tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds are labelled practice values. The only pieces are
the ones the chapter names: 1/8, 2/8 (a 1/4), 1/6, 2/6 (a 1/3) and 1/12 of a turn. One activity at a time, one
instruction at a time, large controls, Back and Next in the same place, visible progress, Hint, Retry and Reset always
present, immediate specific feedback that is never red. A turn is always told as a part of a full turn: never degrees."""
from topics_common import T

TOOLS = {
    "turn_disc": T(
        'tool_turn_disc', 'Turn Disc', 'manipulative',
        'Measure turns on a disc cut into equal parts, one division at a time: Stage 1 eighths, Stage 2 sixths, Stage 3 twelfths. A turn is always told as a part of a full turn. A stage opens only after the one before is done, and the divisions are never mixed on one disc.',
        'A craft table in the classroom, drawn as a warm 3D isometric scene with soft shadows and gentle animation. In the middle, large, lies the tracing-paper disc with fold lines, a straw fixed at its centre and the starting point A marked on the edge, as in your maths book. A teal start mark sits at A and never moves; an orange curved arrow and a shaded wedge grow from A as the straw turns. Three stage tabs sit at the top, Stage 1: Eighths, Stage 2: Sixths and Stage 3: Twelfths; a stage opens when the one before is done, and each stage shows its own disc: 8 equal parts, 6 equal parts or 12 equal parts. An instruction strip at the top shows one sentence in large type, with progress dots under it. Controls: drag the straw round (it snaps to the fold lines) or press the plus and minus buttons to move it one part at a time; a Show equal names button that writes the equal fractions for the turn (for example 2/8 = 1/4); in Stage 3, a place to drag the 1/12 pieces onto a 1/6 piece; Check, Hint, Retry (puts the straw back on A), Reset (restores the stage), Back and Next in the same places on every card. Read-outs: parts moved out of the parts in the whole, for example 3 of 8 parts; the turn as a fraction, for example 3/8 turn; the equal names when shown; a note, a full turn, when the straw is back on A; and a card number within the stage.',
        ['Stage 1: look at the disc in 8 equal parts with the straw on A, as in the video. Move the straw one part. What fraction of a full turn is that?',
            'Stage 1 (eighths): turn the straw 3 parts and find the quarter turn. Stage 2 (sixths): turn 3 parts of the 6 and read the half turn. Stage 3 (twelfths): lay 1/12 pieces on a 1/6 piece.',
            "The book's items with the disc: Stage 1 shows the turns 1/8, 2/8, 1/4 and 3/8 and then continues to 5/8, 6/8, 7/8 and 8/8; Stage 2 shows the turns 1/6, 2/6 and so on until the full circle; Stage 3 guesses the turn equal to half of a 1/6 turn."],
        ['Stage 1, card 1 (practice values): with 8 equal parts, turn the straw 3 parts. What turn is it? Answer: a 3/8 turn.',
            'Stage 1, card 2: show a quarter turn on the disc of 8 parts. How many parts is it? Answer: 2 parts, because 8 ÷ 4 = 2, so 2/8 = 1/4.',
            "Stage 1: 'Show a 1/8 turn of the straw. Show a 2/8 turn. Show a 1/4 turn. Show a 3/8 turn.' Then: 'Continue turning by 5/8, 6/8, 7/8, and 8/8. Check when you have completed a 3/4 turn and a full turn.' Answer: 1/8 is 1 part, 2/8 is 2 parts, 1/4 is 2 parts (the same as 2/8), 3/8 is 3 parts. The 3/4 turn is reached at 6/8 and the full turn at 8/8, when the straw is back on A.",
            'Stage 2, card 1: on the disc of 6 equal parts, turn the straw 3 parts. What turn is it? Answer: a 3/6 turn, which is the same as 1/2: a half turn.',
            "Stage 2: 'Show the turns of the straw equal to 1/6, 2/6, and so on until you complete a full circle.' Answer: the straw turns 1/6, 2/6, 3/6, 4/6, 5/6 and 6/6; 6/6 is a full turn, back on A.",
            'Stage 3, card 1: switch to 12 equal parts and lay two 1/12 pieces on a 1/6 piece. How many pieces of 1/12 cover a 1/6 piece? Answer: 2 pieces, because a 1/12 piece is half of a 1/6 piece.',
            "Stage 3: 'Can you guess what turn of the straw will be equal to half of a 1/6 turn? This is the same as a 1/12 turn.' Fold a 1/6 piece in half on the 6-part disc, then check on the 12-part disc. Answer: a 1/12 turn, because 6 × 2 = 12 small parts make the full circle."],
        ['The straw moves one fold line at a time, and the read-out says how many parts it has moved out of the parts in the whole, for example 3 of 8 parts, and the turn as a fraction, 3/8 turn.',
            'Show equal names writes the same turn in other ways, for example: 2/8 = 1/4. The tool says why: 2 ÷ 2 = 1 and 8 ÷ 2 = 4.',
            'A wrong answer shows a soft amber note, for example: A quarter turn is 2 parts of 8, not 4. 4 parts is 4/8, which is a half turn.',
            'When the straw is at 2/8, 4/8 or 6/8 the tool names the turn it matches: 2/8 is the 1/4 turn, 4/8 the 1/2 turn and 6/8 the 3/4 turn. At 8/8 the straw is back on A and the note says: a full turn.',
            'In Stage 3 the tool shows the 1/12 piece laid on the 1/6 piece and counts how many fit.'],
        'Stage 1, Stage 2 and Stage 3 are done: turns made on the 8, 6 and 12 part discs, 2/8 = 1/4, 4/8 = 1/2 and 6/8 = 3/4 found, the full turn completed, and half of a 1/6 turn found to be a 1/12 turn.',
        ['stage',
            'strawPartsMoved',
            'turnFraction',
            'equalNames',
            'wedgePieces',
            'challengeIndex'],
        ['M_BIGGER_DENOM_TURN'],
        ['How many equal parts does the disc have? Look at the fold lines and the start point A.',
            'Move the straw one part at a time from A and count the parts. A bigger number of parts means each part is a smaller turn.',
            'The turn is the number of parts moved over the number of parts in the whole. 2 parts of 8 is 2/8, which is the same as 1/4.',
            'Press plus until the read-out shows the parts for this card, then press Show equal names to read the turn.']),

    "angle_check_draw": T(
        'tool_angle_check_draw', 'Angle Check and Draw', 'manipulative',
        'One purpose, the size of an angle as a turn, in two clearly separated activities. Activity 1, Measure (first): guess the turn an angle makes and check it by laying the turn pieces side by side on it, name the angle as acute, right or obtuse, and read the turn an arrow makes. Activity 2, Draw (second): draw a second line to make an angle for a given turn. Activity 2 opens after Activity 1 is done.',
        'A craft table with dotted paper, drawn as a warm 3D isometric scene with soft shadows and gentle animation. Two big activity tabs sit at the top, Activity 1: Measure and Activity 2: Draw; only one activity is on screen at a time, and Activity 2 opens after Activity 1 is done. In the middle, large, is a sheet of dotted paper. In Activity 1 an angle is drawn on it from a dot, two lines meeting at the corner. In Activity 2 a given line with a dot at each end is drawn on it. At the side lies a tray of five wedge pieces cut from the tracing-paper circle, each with its fraction written on it: 1/8, 2/8 (also marked 1/4), 1/6, 2/6 (also marked 1/3) and 1/12, which are the angle measuring tools of your maths book. An instruction strip at the top shows one sentence in large type, with progress dots under it. Controls in Activity 1: a guess box with number buttons to type a guess such as 1/6; drag a wedge piece into the angle (it snaps with its point at the corner and its first edge on the first line; the next piece snaps after it); tap a piece to take it back; three name cards, acute, right and obtuse, to tap. Controls in Activity 2: plus and minus buttons that turn a second line by one piece at a time from the given line, and a Draw button that fixes the line. In both: Check, Hint, Retry (clears the pieces or the line on this card), Reset (restores the activity), Undo, Back and Next in the same places on every card. Read-outs: the pieces laid so far as a sum, for example 1/6 + 1/12; the total as a fraction of a full turn, for example 3/12 = 1/4; in Activity 1 the angle name once it fits; and a card number, Activity 1 cards 1 to 4 and Activity 2 cards 1 to 3.',
        ['Activity 1: look at the angle covered by a 1/6 piece and a 1/12 piece from the video. Guess how much of a full turn it is, then lay the pieces on it to check.',
            'Activity 1 (Measure): guess and check two practice angles and read the turn an arrow makes between two arrows. Activity 2 (Draw): draw second lines for a 1/6 turn and for a 1/2 + 1/12 turn.',
            "Activity 1: guess and check the book's seven angles and say whether each is acute, right or obtuse. Activity 2: draw the book's angles for the given turns using the given lines."],
        ['Activity 1, card 1 (practice values): an angle is covered by a 1/4 piece and a 1/12 piece. Guess, then check. What turn is it, and what kind of angle? Answer: 1/4 + 1/12 = 3/12 + 1/12 = 4/12 = 1/3, more than 1/4 and less than 1/2: obtuse.',
            'Activity 1, card 2 (practice values): an angle is covered by two 1/8 pieces. What turn is it, and what kind of angle? Answer: 1/8 + 1/8 = 2/8 = 1/4: a right angle.',
            'Activity 1, card 3 (practice values): an arrow turns from straight up, through straight down, and then a 1/6 piece more, in the same direction. What turn has it made? Answer: 1/2 + 1/6 = 3/6 + 1/6 = 4/6, more than a half turn.',
            "Activity 1, card 4: 'Guess the measures of each of the angles shown below. Then, check using your angle measuring tools. You may need to use a combination of measures. Also, state whether each of the angles is acute, right, or obtuse.' Use the seven angles of your maths book. Answer: about 1/12, 1/6, 1/8, about 1/6, 1/4, about 1/3 and 3/8, named acute, acute, acute, acute, right, obtuse and obtuse.",
            'Activity 2, card 1: draw a second line on the given line so that the angle is a 1/6 turn. Answer: one 1/6 piece from the given line. It is less than a 1/4, so it is acute.',
            'Activity 2, card 2 (practice values): draw a second line so that the angle is a 1/2 + 1/12 turn. Answer: 1/2 + 1/12 = 6/12 + 1/12 = 7/12, more than a half turn, so more than a straight angle.',
            "Activity 2, card 3: 'Draw angles for the given measures of turns using the given lines.' Use the five lines of your maths book, each with the turn written beside it: 1/2, 1/4, 1/8, 1/12 and 1/4. Answer: 1/2 gives a straight line, each 1/4 gives a square corner, 1/8 gives half a square corner and 1/12 a narrower angle. Either end of the line can be the corner."],
        ['Activity 1: laying a piece shows the sum so far, for example 1/6 + 1/12, and the total as a fraction of a full turn. When the pieces fill the angle exactly the tool says: The pieces fit.',
            'Activity 1: if the pieces are too few or too many a soft amber note says so, for example: There is a gap of one 1/12 piece, or: The pieces go past the second line.',
            'Activity 1: the total is compared with 1/4 and 1/2 and the angle is named, for example: 4/12 is more than 1/4 and less than 1/2: obtuse.',
            'Activity 2: the second line turns piece by piece and the shaded wedge grows; Draw fixes it and the tool checks the total against the turn asked.',
            'A guess that is close is accepted with the note: Your guess is near. The pieces say it is exactly 1/6.'],
        'Activity 1 is done when the practice angles are checked, the arrow turn is read, and the seven angles of the book are guessed and checked. Activity 2 is done when the two second lines are drawn and the five angles of the book are drawn.',
        ['activity',
            'angleOnSheet',
            'guess',
            'piecesLaid',
            'totalTurn',
            'nameCards',
            'drawLine',
            'challengeIndex'],
        ['M_ARM_LENGTH',
            'M_BIGGER_DENOM_TURN'],
        ['Which piece looks about as wide as the angle? Guess first, then check.',
            'Lay the pieces side by side from the first line of the angle. Start with the biggest piece that fits inside and see how much is left.',
            'Add the fractions of the pieces, using twelfths if you need to: a 1/6 piece is 2 pieces of 1/12. Compare the total with 1/4 and 1/2.',
            'Lay the next piece for this card and read the total. For drawing, turn the second line piece by piece and press Draw.']),
}
