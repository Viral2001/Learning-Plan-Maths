# -*- coding: utf-8 -*-
"""Tool specs for T1, T2 and T3 of Class 5 Chapter 5 (Far and Near): Unit Picker (the free try of the intro, right after
the hook), Length Bars and Kilometre Track. Specs only; the tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds are labelled practice values. One
activity at a time, one instruction at a time, large controls, Back and Next in the same place, visible progress,
Hint, Retry and Reset always present, immediate specific feedback that is never red."""
from topics_common import T

TOOLS = {
    "unit_picker": T(
        "tool_unit_picker", "Unit Picker", "manipulative",
        "Choose cm or m for a length by comparing the number with the size of the thing: a pencil of 17 is 17 cm, "
        "because 17 m would be longer than a classroom. This is the free first try of the chapter, so it asks and "
        "shows; the videos that follow name the rule.",
        "The long cloth table of the village weaving centre, drawn as a warm 3D isometric scene with soft shadows and "
        "gentle animation, with a measuring tape running along the top of the wall. A picture card of a thing (a "
        "pencil, a classroom door, a school bus, a postage stamp, a handkerchief) stands on the table as the largest "
        "object on screen, with a number tag beside it, for example 17. Under the card are two unit tags, cm and m, to "
        "drag onto the number tag. A tape strip along the wall draws the length as a bar for the chosen unit, with a "
        "1 m mark and a 1 cm mark always shown, so a wrong unit makes the bar run far past the picture or shrink to a "
        "dot. An instruction strip at the top shows one sentence in large type, with progress dots under it. Controls: "
        "drag the cm tag or the m tag onto the number tag; tap the tag again to take it off; in the rule card, drag the "
        "unit cards cm and m into two gaps; answer tags for the book's questions; Check, Hint, Retry (takes the tag off this card), "
        "Reset (returns all cards), Back and Next in the same places on every card. Read-outs: the number with its unit "
        "under the picture, the bar on the wall tape, and a card number out of 7.",
        ["Look at Shikha with her cm tape and Sonu with his m tape from the story, and "
         "the table with a handkerchief and a sari on it. Tap the tape you would use for the handkerchief, then press "
         "Next.",
         "Drop the cm tag or the m tag on the number of each picture card, look at the bar on "
         "the wall tape, and keep the unit that gives a sensible length; then finish the rule for short things and long "
         "things.",
         "Answer your maths book's own question, Identify the appropriate units for measuring each "
         "of the following, for the height of India Gate, the length of a handkerchief, the depth of a well, the length "
         "of a mobile phone, the length of an elephant's trunk and the distance between two buttons on a shirt."],
        ["Card 1 (practice values): a pencil with the number 17. Drop m, then cm, and watch the bar. Answer: "
         "cm, because 17 cm fits the pencil and 17 m would be longer than a classroom.",
         "Card 2 (practice values): a classroom door with the number 2. Answer: m, because a door is taller "
         "than a child, so 2 m fits, and 2 cm is a tiny length.",
         "Card 3 (practice values): a school bus with the number 9. Answer: m, because a bus is long and 9 cm "
         "would be shorter than a pencil.",
         "Card 4 (practice values): a postage stamp with the number 3. Answer: cm, because a stamp is tiny and "
         "3 m would be longer than a door.",
         "Card 5: finish the rule with the unit cards. Short things are measured in ___ and long things in "
         "___. Answer: cm, then m.",
         "Challenge: 'Identify the appropriate units for measuring each of the following.' (a) the height of "
         "India Gate is 42, (b) the length of a handkerchief is 40, (c) the depth of a well is 50. Choose m or cm for "
         "each. Answer: 42 m, 40 cm and 50 m.",
         "Challenge: (d) the length of a mobile phone is 13, (e) the length of an elephant's trunk is 2, (f) "
         "the distance between two buttons on a shirt is 5. Choose m or cm for each. Answer: 13 cm, 2 m and 5 cm. Next "
         "stop: how one length has two names."],
        ["A tag dropped on a number draws a bar on the wall tape. If the bar runs far past the picture, the tool says, "
         "for example: 17 m is longer than a classroom, but a pencil is small. Try the other tag.",
         "If the bar shrinks to a dot, the tool says, for example: 2 cm is a tiny length, but a door is tall. Try the "
         "other tag.",
         "A tag that fits locks in with a soft chime and the bar turns green, with the words: 17 cm fits the pencil.",
         "In the book's questions the bar is drawn after the student has chosen a unit, and the tool says whether the length is "
         "sensible, in the same plain words.",
         "A wrong rule card slides back with a clue such as: Think of a pencil. Is it short or long?"],
        "All four picture cards have the right tag, the rule is finished, and all six lengths of Let Us Find have a "
        "unit.",
        ["chosenUnit", "currentCard", "barOnTape", "ruleCards", "challengeIndex"],
        ["M_UNIT_ANY"],
        ["How big is the thing? Could you hold it in your hand, or is it as long as a room?",
         "Try both tags and look at the bar on the wall tape. Which one fits the picture?",
         "A short thing such as a pencil is measured in cm, and a long thing such as a bus is measured in m. Which is "
         "this thing?",
         "The tool drops the right tag on this card: cm for a thing that fits in your hand, m for a thing as long as a "
         "room or longer."]),

    "length_bars": T(
        "tool_length_bars", "Length Bars", "manipulative",
        "Compare two lengths given in different units by changing both to one unit, and read the difference as the gap "
        "between two bars on one tape. A doubled bar helps find the length that doubles to a given length.",
        "The weaving centre's long wall tape in cm, drawn as a warm 3D isometric scene with soft shadows and gentle "
        "animation, with rods and lengths of cloth hung along it. Two bars sit on one tape, drawn to scale, and they are "
        "the largest things on screen; each bar has a length card in its own units, for example 4 m 3 cm. A Change to "
        "cm button under each card shows the working, for example 4 × 100 + 3 = 403, and the card turns into cm. A sign "
        "box between the bars takes the signs <, = and >. A gap marker appears between the ends of the bars and shows "
        "the difference when both are in cm. A Double button stretches a bar to twice its length. In the statue stage "
        "the six statues of your maths book stand as bars on one base line (182 m, 128 m, 108 m, 93 m, 91 m and 38 m), "
        "and tapping two statues puts their bars side by side with the gap. An instruction strip at the top shows one "
        "sentence in large type with progress dots under it. Controls: Change to cm on each card; drag a sign into the "
        "sign box; tap two statues; Double; type an answer into a box; Check, Hint, Retry (clears the sign and the "
        "conversion of this card), Reset (restores all bars), Back and Next in the same places on every card. "
        "Read-outs: each length in its own units and in cm, the gap in cm, and a card number out of 7.",
        ["Look at two bars on one tape, one length written in m and cm and the other in "
         "cm. Say what must be done before the bars can be compared, then press Next.",
         "Change both lengths to cm, drop the sign <, = or > between the bars, read the gap as "
         "the difference, double a bar and find the bar of the same length.",
         "Answer your maths book's own questions: Ritika's five comparisons with the signs <, = and "
         ">, and the four questions about the world's tallest statues."],
        ["Card 1 (practice values): compare 4 m 3 cm and 430 cm. Change both to cm and drop a sign. Answer: "
         "4 m 3 cm = 4 × 100 + 3 = 403 cm, and 403 < 430, so 4 m 3 cm < 430 cm.",
         "Card 2 (practice values): compare 3 m 20 cm and 300 cm + 20 cm. Answer: 3 m 20 cm = 320 cm and "
         "300 cm + 20 cm = 320 cm, so they are equal.",
         "Card 3 (practice values): find the gap between 3 m 45 cm and 290 cm. Answer: 3 m 45 cm = 345 cm and "
         "345 − 290 = 55 cm.",
         "Card 4 (practice values): double a bar of 85 cm and find which of the bars 60 cm, 170 cm and 255 cm "
         "is the same length as the doubled bar. Answer: 85 × 2 = 170 cm, so the bar of 170 cm.",
         "Card 5 (practice values): put three bars in order from the shortest to the longest after changing "
         "them to cm: 2 m 5 cm, 190 cm and 2 m 50 cm. Answer: 2 m 5 cm = 205 cm and 2 m 50 cm = 250 cm, so the order is "
         "190 cm, 2 m 5 cm, 2 m 50 cm.",
         "Challenge: 'Ritika is comparing the lengths of different rods. Compare them using <, =, > signs.' "
         "(a) 456 cm and 5 m; (b) 55 cm + 200 cm and 200 cm + 54 cm; (c) 6 m 5 cm and 6 m 50 cm; (d) 2 m 150 cm and 3 m "
         "50 cm; (e) 238 cm and 138 cm + 1 m. Answer: (a) <; (b) >; (c) <; (d) =; (e) =.",
         "Challenge: the world's tallest statues, with the heights 182 m, 128 m, 108 m, 93 m, 91 m and 38 m: "
         "(a) the difference between the height of the tallest statue and the Statue of Liberty; (b) the statues whose "
         "heights have the least difference; (c) the statues whose heights have the largest difference; (d) the statue "
         "whose height doubled is the height of the Statue of Unity. Answer: (a) 182 − 93 = 89 m; (b) the Statue of "
         "Liberty and The Motherland Calls, 2 m; (c) the Statue of Unity and Christ the Redeemer, 144 m; (d) The "
         "Motherland Calls, 91 m."],
        ["Change to cm shows the working on the card, for example 4 × 100 + 3 = 403, and the bar redraws in cm. If the "
         "two lengths are still in different units, the tool says: Change both to the same unit first.",
         "A sign dropped in the sign box is checked against the two numbers in cm and the tool says why, for example: "
         "403 is less than 430, so the sign is <.",
         "The gap marker shows the difference in cm only when both bars are in cm, and the tool says: The difference is "
         "the longer bar minus the shorter bar.",
         "The Double button stretches a bar, and a bar of the same length lights up in green; if none matches, the tool "
         "says: Halve the long bar to find the short one.",
         "In the statue stage, two tapped statues show their heights side by side and the gap, and the tool says "
         "whether the gap is the least or the largest only after the student has tried the pairs."],
        "All five practice cards are solved, the five rod comparisons have signs, and the four statue questions are "
        "answered.",
        ["leftLength", "rightLength", "unitShown", "signChosen", "gapShown", "doubledBar", "statuePair",
         "challengeIndex"],
        ["M_BIGGER_NUMBER", "M_JOIN_NUMBERS"],
        ["Are the two lengths in the same unit? What must you do before you compare them?",
         "Change both to cm, the smaller unit. 1 m is how many cm?",
         "Change the m by multiplying by 100 and add the cm that are left. Then compare the two numbers.",
         "The tool shows both lengths in cm. Compare the two numbers: the bigger number is the longer length."]),

    "kilometre_track": T(
        "tool_kilometre_track", "Kilometre Track", "manipulative",
        "See 1 km as 1,000 m and find how many equal ropes or stops fit along a distance and where they stand: the "
        "number of pieces is the distance divided by the length of one piece.",
        "The road outside the weaving centre, drawn as a long straight strip in a warm 3D isometric scene with soft "
        "shadows and gentle animation, with a kilometre scale along it marked every 100 m. The track strip is the "
        "largest object on screen, 1 km long in the rope stage and 3 km long in the race stage. A rope tray holds rope "
        "pieces of a chosen length (1,000 m, 100 m, 10 m, 200 m, 500 m, 250 m and the practice lengths), and a rope "
        "snaps end to end onto the track where the last one stopped. A stop tray holds stop markers: a water cup, a "
        "child, a red flag and a blue flag, and an interval box takes a length in m; Place stops puts a marker at every "
        "interval from the start, and a list beside the track shows the positions from the start in m and in km. An "
        "instruction strip at the top shows one sentence in large type with progress dots under it. Controls: pick a "
        "rope length and drag ropes onto the track; pick an interval and a marker and tap Place stops; Undo; type an "
        "answer into a box; Check, Hint, Retry (clears the track being worked), Reset (restores both tracks), Back and "
        "Next in the same places on every card. Read-outs: ropes placed, the metres filled out of 1,000 m, the number of "
        "stops, and the list of positions.",
        ["Look at the 2 km track from the video with a flag after every 400 m. Say how "
         "many metres are in 2 km, then press Next.",
         "Fill the 1 km track with ropes of one length and count them, place stops at an "
         "interval on a longer track and read their positions, and see that a smaller interval gives more stops.",
         "Answer your maths book's own questions: how many ropes of each length make 1 km, and the "
         "Kilometre Race with its water stations, its children and its flags."],
        ["Card 1 (practice values): fill the 1 km track with ropes of 125 m. How many ropes? Answer: 8 ropes, "
         "because 1,000 ÷ 125 = 8.",
         "Card 2 (practice values): fill the 1 km track with ropes of 50 m. How many ropes? Answer: 20 ropes, "
         "because 1,000 ÷ 50 = 20.",
         "Card 3 (practice values): on a 2 km track place a marker after every 250 m and read the positions. "
         "Answer: 2,000 ÷ 250 = 8 markers, at 250 m, 500 m, 750 m, 1 km, 1 km 250 m, 1 km 500 m, 1 km 750 m and 2 km.",
         "Card 4 (practice values): on the same 2 km track compare an interval of 400 m with an interval of "
         "200 m. Answer: 5 stops for 400 m and 10 stops for 200 m, because 2,000 ÷ 400 = 5 and 2,000 ÷ 200 = 10. A "
         "smaller interval gives more stops.",
         "Card 5: drag a marker to 1 km 500 m on the track and type its position in m. Answer: 1,500 m, "
         "because 1 × 1,000 + 500 = 1,500.",
         "Challenge: 'Ropes of different lengths are used to make 1 km.' How many ropes of 100 m, 10 m, 200 m, "
         "500 m and 250 m make 1 km? Answer: 10, 100, 5, 2 and 4 ropes.",
         "Challenge: 'Sheena and Jennifer are helping to organise a 3 km race.' Water stations after every "
         "500 m: how many, and where? Children at an interval of 300 m: how many, and where? Red and blue flags "
         "alternately at every 50 m: how many? Answer: 6 water stations at 500 m, 1 km, 1 km 500 m, 2 km, 2 km 500 m "
         "and 3 km; 10 children at every 300 m from 300 m to 3,000 m; 60 flags, 30 red and 30 blue."],
        ["Each rope snaps onto the track where the last rope stopped and the counter shows the metres filled, for "
         "example 4 ropes of 250 m fill 1,000 m, which is 1 km.",
         "If the ropes run past the end of the track, the tool says: The track is only 1,000 m long. Take a rope away.",
         "Place stops puts a marker at every interval from the start and lists the positions, and the tool says, for "
         "example: 3,000 ÷ 500 = 6, so there are 6 stops.",
         "If the student places a stop at the start line, the tool says: Here the first stop is after the first "
         "interval, not at the start line. Try again.",
         "A wrong count slides back with a clue such as: How many pieces of that length fit in the whole distance?"],
        "All five practice cards are solved, the five ropes of the rope table are counted and the three questions of the "
        "Kilometre Race are answered.",
        ["ropeLength", "ropesPlaced", "trackLength", "interval", "markerType", "stopPositions", "challengeIndex"],
        ["M_KM_HUNDRED", "M_STOP_COUNT"],
        ["How many metres are in the whole distance? Change km to m first.",
         "How long is one piece? How many pieces of that length fill the whole distance?",
         "Divide the whole distance in m by the length of one piece. The stops stand at 1, 2, 3 and so on times the "
         "length of one piece.",
         "The tool fills the track piece by piece and counts them for you: the number of pieces is the answer."]),
}
