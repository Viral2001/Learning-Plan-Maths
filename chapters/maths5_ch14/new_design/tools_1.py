# -*- coding: utf-8 -*-
"""Tool specs for T1 and T2 of Class 5 Chapter 14 (Maps and Locations): Face the Rising Sun (the free try of the intro,
right after the hook) and Direction Clues. Specs only; the tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds are labelled practice values. One
activity at a time, one instruction at a time, large controls, Back and Next in the same place, visible progress,
Hint, Retry and Reset always present, immediate specific feedback that is never red."""
from topics_common import T

TOOLS = {
    "sun_compass": T(
        "tool_sun_compass", "Face the Rising Sun", "manipulative",
        "Find east by turning Manu on the screen until the rising Sun is in front of him, then read the direction of his "
        "left hand, his right hand and behind him from that one fact. This is the free first try of the chapter, so it "
        "asks and shows; the video that follows names the rule.",
        "The sunrise field board on the trip desk, drawn as a warm 3D isometric scene with soft shadows and gentle "
        "animation. A round green hill field fills the middle of the board and is the largest thing on screen. Manu, the "
        "boy of your maths book, stands in the middle of the field, seen from behind, with both arms stretched out to "
        "the sides. At the start the rising Sun is on his right. The rising Sun is a large bright disc fixed low on the "
        "horizon above the soft hills, and it never moves when Manu turns. A small arrow grows from his chest to show "
        "where he faces, and an arrow grows from each hand, one from his left hand and one from his right hand. Four "
        "empty tag slots sit at the end of the front arrow, the left hand arrow, the right hand arrow and behind him, "
        "and they turn with him. A tray under the field holds four word tags: North, East, South and West. An "
        "instruction strip at the top shows one sentence in large type, with seven progress dots under it. The compass "
        "card, a small square card with N at the top, E in red on the right, S at the bottom and W on the left as in "
        "your maths book, stays hidden until the practice cards are done and then shows in the top right corner. Controls: Turn "
        "left and Turn right (a quarter turn each, with a gentle animation); tap a word tag and then tap a slot to put "
        "the tag there, and tap a tag that is in a slot to take it out; Check; Hint; Retry (clears the tags of this "
        "card); Reset (returns Manu to his starting turn and clears all the tags); Back and Next in the same places on "
        "every card. Read-outs: a line Where is the Sun now? that says in front of Manu, on his left, on his right or "
        "behind him, a count of the quarter turns made, and a card number out of 7.",
        ["Look at the picture of the story again: the Siberian Crane that flies all the "
         "way from Siberia, the four little chicks of the poem that fly from east to west and from north to south, and "
         "Manu standing on the hill with his arms stretched out. Read the line: Human beings also keep track of "
         "directions. One of the ways is by facing the rising Sun. Then turn Manu until he faces the rising Sun, and "
         "press Next.",
         "Turn Manu until the Sun is in front of him and tag that direction, tag the "
         "direction of his left hand and of his right hand, turn him to face north (practice values) and tag the hands "
         "again, turn him back to the Sun and tag the direction behind him, then open the compass card and compare.",
         "Manu's own lines from your maths book, unchanged, as an open challenge: Manu is facing "
         "the rising Sun. That direction is ___. His left hand is pointing in the ___ direction. His right hand is "
         "pointing in the ___ direction. Then: which way is west? Fill the tags and read what the tool shows. The video "
         "that follows names the rule."],
        ["Card 1: turn Manu until the rising Sun is straight in front of him. Which direction tag goes in "
         "front of him? Answer: East, because the Sun rises in the east.",
         "Card 2: with Manu facing the Sun, tag his left hand and his right hand. Answer: North for his left "
         "hand and South for his right hand.",
         "Card 3 (practice values): turn Manu to face north, one quarter turn to the left from the Sun. Which "
         "direction does his right hand point to, and which his left hand? Answer: his right hand points to the East "
         "and his left hand to the West. The Sun is on his right now, and his hands point in other directions than "
         "before, so a hand does not always point the same way.",
         "Card 4: turn Manu back to face the rising Sun, one quarter turn to the right, and tag the direction "
         "behind him. Answer: West, which is opposite to East.",
         "Card 5: open the compass card and compare. Manu faces East, so on the card he looks to the right. "
         "Which tags match the card? Answer: all four. East is in front of him on the right of the card, North is at "
         "the top on his left hand, South is at the bottom on his right hand and West is on the left behind him.",
         "Challenge: 'Manu is facing the rising Sun. That direction is ___. His left hand is pointing in the "
         "___ direction. His right hand is pointing in the ___ direction.' Turn Manu to the Sun and fill the three "
         "tags. Answer: East, North, South.",
         "Challenge: 'which way is west?' Tag the direction that is neither in front of Manu nor on a hand. "
         "Answer: West is behind Manu, opposite to the rising Sun. Next stop: the rule that names the four "
         "directions."],
        ["Turn left and Turn right move Manu a quarter turn each time. The Sun stays where it is, so the line Where is "
         "the Sun now? changes as he turns, for example from on his right to in front of him.",
         "When the Sun is not in front of Manu on card 1 the tool says: The Sun is not in front of Manu yet. Turn him "
         "again.",
         "When he faces the Sun the tool says: Manu faces the rising Sun, so the tag in front of him is East. The "
         "slot lights up soft green when its tag is right.",
         "A wrong tag shows a soft amber note and never a red cross, for example: Look again. Face the Sun yourself "
         "and stretch out your left arm. Which direction does it point to? The tool names the right tag only after "
         "the second try.",
         "After card 3 the tool says: Manu faces north, so his left hand points West now. A hand does not always "
         "point the same way. It depends on which way Manu faces.",
         "The last card is an open challenge: the tool shows what the tags say and lets the student change them, and the "
         "video that follows names the rule."],
        "Manu has been turned to the rising Sun, the tags East, North, South and West have been placed for his front, "
        "his left hand, his right hand and behind him, the compass card has been opened and compared, and the two "
        "questions from your maths book have been answered with the tags.",
        ["manuTurn", "slotTags", "compassCardOpen", "quarterTurnsMade", "challengeIndex"],
        ["M_LEFT_WEST"],
        ["Where is the Sun on the screen? Turn Manu until the Sun is straight in front of him.",
         "The Sun rises in the east. When Manu faces the Sun, he faces east. Now think about his hands: which side is "
         "each hand on?",
         "Manu faces east. Face the Sun yourself and stretch out your left arm: it points north. Then stretch out your "
         "right arm: it points south.",
         "The tool turns Manu to the Sun and puts East in front of him, North on his left hand, South on his right "
         "hand and West behind him. Then a similar card follows for you to try."]),

    "direction_clues": T(
        "tool_direction_clues", "Direction Clues", "manipulative",
        "The direction of a thing depends on what it is said from. Moving a compass cross onto the lake, onto a "
        "playground thing and onto the girl shows which things are north, south, east and west of that place, and "
        "colouring and placing tents turns direction clues into actions.",
        "Three boards on the trip desk, drawn as a warm 3D isometric scene with soft shadows and gentle animation. The "
        "main board shows the bird-watching camp seen from above, as in your maths book: a grey road that curves from the "
        "top down to the bottom left, a lake with four ducks in the lower middle, four white tents with small red flags "
        "(one on the left of the road, one near the top on the right of the road, one just above the lake and one below "
        "the lake) and many green and yellow trees. The camp is the largest thing on screen. Two more boards slide in "
        "when a card needs them: the girl's room as in your maths book, with the girl, the window, the bed, the cupboard "
        "and the bedside table, and a small playground with a swing at the top left, a slide at the top right, a "
        "sandpit at the bottom left and a seesaw at the bottom right (practice values). The compass card, a small "
        "square card with N at the top, E in red on the right, S at the bottom and W on the left, sits in the top right "
        "corner of every board. A movable compass cross, a small round card with two diagonal lines through its centre, "
        "splits the picture around it into four zones: north above, south below, east on the right and west on the "
        "left. When the cross rests on a thing, the four zones are tinted softly and each zone shows its letter at the "
        "edge. An instruction strip at the top shows one sentence in large type, with seven progress dots under it, and "
        "a clue strip under it shows the clue being worked on. A pen tray holds a blue, a green, a purple and a yellow "
        "pen, and one spare tent waits beside the camp board. On the room board a small tray holds the word tags North, "
        "East, South and West, and a notes card with four lines, East, West, North and South, takes the names of "
        "things in the student's own room. Controls: drag the compass cross onto a thing; tap a thing to read its zone; "
        "tap a tent and then a pen to colour it, and tap the tent again to clear its colour; drag the spare tent onto "
        "the board; drag a word tag next to a name in the room list; type on the notes card; Check; Hint; Retry (clears "
        "the colours, tags or tent of this card); Reset (restores the board); Back and Next in the same places on every "
        "card. Read-outs: a zone line that says, after a tap, which zone of the cross the tapped thing is in, for example "
        "The slide is in the east zone of the cross; a count of tents coloured out of 4; and a card number out of 7.",
        ["Look at the compass card and remember: facing the rising Sun is facing east, "
         "and on every picture N is at the top. Put the compass cross on the lake. Which tent is to its north?",
         "With the cross on the lake, name the tent to its north and the tent to its south; on "
         "the playground (practice values) put the cross on the swing and find the thing to its east, on the sandpit "
         "and find the thing to its north, and on the slide and find where the swing is from it.",
         "Your maths book's own items, unchanged. Bird Watching: colour the tents with the four "
         "clues (the tent to the west of the road is blue, the tent closest to the lake is green, the tent north of the "
         "green tent is purple, the tent south of the lake is yellow) and draw a tent to the east of the lake. Map of a "
         "Room: write the directions of the window, the bed, the cupboard and the bedside table in relation to the "
         "girl, make a drawing of your room, and write the names of the things placed in the east, west, north and "
         "south."],
        ["Card 1: put the compass cross on the lake. Which tent is to the north of the lake and which tent is to "
         "the south of it? Answer: the tent just above the lake is to its north and the tent below the lake is to its "
         "south.",
         "Card 2 (practice values): on the playground board put the cross on the swing. Which thing is east of "
         "the swing? Then put the cross on the sandpit. Which thing is north of the sandpit? Answer: the slide is east "
         "of the swing, and the swing is north of the sandpit.",
         "Card 3 (practice values): put the cross on the slide. In which direction is the swing from the "
         "slide? Answer: west. The slide is east of the swing, so the swing is west of the slide. Seen from the other "
         "thing, the direction is the opposite one.",
         "Challenge: 'Children are at a bird-watching camp. Read the clues and colour the tents in the camp "
         "accordingly. The tent to the west of the road is blue. The tent closest to the lake is green. The tent north "
         "of the green tent is purple. The tent south of the lake is yellow.' Answer: blue is the tent on the left of "
         "the road, green is the tent just above the lake, purple is the tent above the green tent near the top, and "
         "yellow is the tent below the lake.",
         "Challenge: 'Now, draw a tent to the east of the lake.' Drag the spare tent onto the board. Answer: "
         "sample answer, the tent goes on the ground to the right of the lake. Any place to the right of the lake is "
         "right. Your answer may differ.",
         "Challenge: 'Write the directions of the following in relation to the girl. Window ___ Bed ___ "
         "Cupboard ___ Bedside table ___' Drag the tags next to the names. Answer: sample answer, window north, bed "
         "east, cupboard west, bedside table south. The cupboard and the bedside table sit between two directions, so "
         "we name the nearest one. Your answer may differ.",
         "Challenge: 'Make a drawing of your room and locate the direction in which different things have "
         "been placed in relation to you standing at the centre of the room. Make the direction arrow for your room.' "
         "Then: 'Write the names of the things that are placed in the following directions. East ___ West ___ North "
         "___ South ___' Draw on paper, then type the names on the notes card. Answer: sample answer, in a sample "
         "room the bed is in the east, the cupboard in the west, the window in the north and the door in the south. "
         "To find north in your own room, face the rising Sun, which is east: north is on your left hand. Your answer "
         "may differ."],
        ["When the cross rests on a thing the four zones tint and the zone line says where a tapped thing is, for "
         "example: The slide is in the east zone of the cross. The swing is in the west zone of the cross when the cross "
         "is on the slide.",
         "A tent coloured to a clue clicks in with a soft chime and the clue strip says why, for example: The tent "
         "closest to the lake is the one just above it. That tent is green.",
         "A wrong colour shows a soft amber note and never a red cross, for example: Which tent is west of the road? "
         "West is to the left on the picture. The tool names the right tent only after the second try.",
         "A tag dropped next to a name in the room list is read at once, for example: The window is on the back wall, "
         "above the girl: north. A tag between two directions gets the note: This thing sits between two directions. "
         "Name the nearest one.",
         "The spare tent turns green when it stands to the right of the lake, with the note: This tent is east of the "
         "lake. A tent anywhere else slides back with: East is to the right on the picture.",
         "Open items, the tent to the east of the lake, the room list, the drawing and the names, are never marked "
         "wrong: the tool says Your answer may differ and offers Next."],
        "The compass cross has been moved onto the lake, onto a playground thing and onto the slide with the zones read "
        "correctly, the four tents are coloured by the four clues, a tent stands to the east of the lake, the room list "
        "has a direction for each thing, and the notes card has a name for each of the four directions.",
        ["crossPosition", "tentColours", "spareTentPosition", "roomTags", "notesCard", "activeBoard",
         "challengeIndex"],
        ["M_SAME_DIRECTION"],
        ["Where is the compass cross now? Which thing is it resting on?",
         "Which zone is the thing in? Above the cross is north, below is south, on the right is east and on the left is "
         "west.",
         "Find the thing the clue talks about, rest the cross on it, and look at which tent lies in the zone the clue "
         "names.",
         "The tool colours the first tent for you: the tent closest to the lake, just above it, turns green. Then a "
         "similar clue follows for you to try."]),
}
