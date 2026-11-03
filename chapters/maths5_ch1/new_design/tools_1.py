# -*- coding: utf-8 -*-
"""Tool specs for T1, T3 and T4 of Class 5 Chapter 1 (We the Travellers - I): Travel Explorer (the free try of the
intro), Number Reading Challenge and Number Construction. Specs only; the tool pages are built later.

Each tool follows the chapter's three phases: Phase 1 recalls the video idea, Phase 2 is play with the book's numbers,
Phase 3 is the book's own question used with its own values. One activity at a time, one instruction at a time, large
controls, Back and Next in the same place, visible progress, simple restart, immediate specific feedback, hints, retry
and reset."""
from topics_common import T

TOOLS = {
    "travel_explorer": T(
        "tool_travel_explorer", "Travel Explorer", "manipulative",
        "Explore earlier ways of travelling one at a time and sort them into long ago and about a hundred years ago, so "
        "the travel story of the chapter is clear before the number lessons begin. The tour ends with an open "
        "question about how many vehicles there are in a state, which hands over to big numbers.",
        "A warm storybook village by a wide river, drawn as a polished 3D isometric scene with soft shadows and "
        "gentle animation: a dirt road with a bullock cart under trees, a wooden boat and a sailing ship on the "
        "river, a footpath, and an old train on a track at the edge of the village. One scene only, no crowd. A row "
        "of seven large mode cards runs along the bottom: On foot, Animals, Boat, Sailing ship, Bullock cart, Train "
        "and Car. Only one card is active at a time. Tapping a card plays a short use animation in the middle of "
        "the scene (a walker crossing the village, animals pulling and carrying, the boat drifting over the river, "
        "the ship sailing, the bullock cart rolling, the train moving along the track, a car on the road) and shows "
        "one short sentence from the chapter's opening story in a large caption box. When Animals is active, three "
        "large chips appear: Animals used for travelling (bullocks, horses, donkeys, mules, elephants), Hilly and "
        "snow-covered regions (yaks, dogs, reindeer) and Deserts (camels). A time strip across the top has two "
        "labelled bays, Thousands of years ago and About a hundred years ago, and the student drags a mode card "
        "into a bay. A counter shows how many of the 7 cards are sorted. Fixed controls: Back and Next in the same "
        "places on every card, a Replay button for the animation, a Hint button, a Restart button and progress dots.",
        ["Phase 1, Recall and get ready: look at the village and the river and tap the one way of travelling you "
         "think is the oldest.",
         "Phase 2, Play and apply: select one way of travelling at a time, watch it in use, read its short sentence "
         "and drag its card into Thousands of years ago or About a hundred years ago.",
         "Phase 3, Challenge: answer the opening questions of the chapter about your own last long trip, and the open "
         "question about how many vehicles there are in your state."],
        ["Phase 2, card 1: tap On foot and watch the walker. How did people travel long distances thousands of years "
         "ago when they had no animal and no boat? Answer: on foot.",
         "Phase 2, card 2: open Animals and tap each group. Which animals does the story name for hilly and "
         "snow-covered regions, and which for deserts? Answer: yaks, dogs and reindeer in hilly and snow-covered "
         "regions, and camels in deserts.",
         "Phase 2, card 3: tap Boat and Bullock cart. Which was invented first? Answer: the boat, because boats were "
         "probably the first form of transport humans invented, much before bullock carts.",
         "Phase 2, card 4: drag each of the 7 cards into a bay. Answer: Thousands of years ago holds On foot, "
         "Animals, Boat and Sailing ship (4 cards). About a hundred years ago holds Bullock cart, Train and Car "
         "(3 cards).",
         "Phase 2, card 5: read the counter. How many ways of travelling are sorted in all? Answer: 4 + 3 = 7.",
         "Phase 3, Challenge: 'When was the last time you went on a long trip? Where did you go? How did you "
         "travel? What was the duration of your trip? How much distance did you cover?' Ask the elders who went "
         "with you, then tap the card that shows how you travelled. Your answer is your own.",
         "Phase 3, Challenge: 'Do you know how many vehicles are currently there in your state?' Guess whether the "
         "number has 4 digits, 5 digits or more. Your guess may differ. Next stop: how do we write a number as big "
         "as ten thousand?"],
        ["Tapping a mode card lights it up, plays its short animation and shows one sentence from the story. Only one "
         "card is active at a time.",
         "A card dropped in the right bay locks in with a soft chime and a tick. A card dropped in the wrong bay "
         "slides back and shows the story's sentence that places it, for example: About a hundred years ago there "
         "were animal-drawn carts, cars and trains.",
         "The counter shows at once how many of the 7 cards are sorted.",
         "The two open questions at the end are never marked wrong: the screen says Your answer may differ and shows "
         "Next."],
        "All 7 cards are sorted, the two open questions have been answered once, and the student has pressed Next at "
        "the end of the tour.",
        ["selectedMode", "animalGroup", "bayOfCard", "sortedCount", "challengeIndex", "tripAnswer"],
        [],
        ["What is the card asking: a way of travelling, a group of animals or the time?",
         "Tap a card and read its one sentence. Look for the words thousands of years ago or about a hundred years "
         "ago.",
         "The story says boats and ships were built long ago, and animal-drawn carts, cars and trains were there "
         "about a hundred years ago.",
         "Put On foot, Animals, Boat and Sailing ship in Thousands of years ago, and Bullock cart, Train and Car in "
         "About a hundred years ago."]),

    "number_reading": T(
        "tool_number_reading", "Number Reading Challenge", "manipulative",
        "Read numbers beyond ten thousand by matching the numeral, the number name and the place value tokens: say "
        "the part before the comma and add thousand, then the hundreds, tens and ones, and skip every place that "
        "holds 0.",
        "A large, readable railway station destination board in a warm 3D station scene with soft shadows and "
        "gentle animation. The board shows ONE numeral at a time in very large type with its comma; it is the "
        "largest thing on screen. Under the board sit three clear panels: a place value chart with the columns TTh, "
        "Th, H, T and O, a tray of place value token pictures in the book's colours (10,000 purple, 1,000 green, 100 "
        "orange, 10 blue, 1 pink), and a number name strip with empty slots. Below them is a tray of number name word "
        "cards (for example Ten, Thirteen, Forty-five, thousand, hundred, one, twenty, twenty-four, five, "
        "sixty-seven). Controls: drag a word card into a slot of the name strip, tap a slot to take its card out, a "
        "Check button, a Show tokens button that fills the chart and the token tray for the numeral, a Hear it button "
        "that says the name aloud, Back and Next in the same places on every card, a Hint button, a Reset button and "
        "progress dots. Read-outs: the chart digits light up one column at a time as the matching words are placed, "
        "and a counter shows the card number out of 7.",
        ["Phase 1, Recall and get ready: the board shows one 10,000 token and one 1 token. Say aloud the number they "
         "make before you touch anything.",
         "Phase 2, Play and apply: for each numeral on the board, drag the word cards into the name strip, then press "
         "Show tokens and match the numeral, the name, the chart and the tokens.",
         "Phase 3, Challenge: write the number name for each number of the Number to Name rows in your maths book, "
         "using the same board."],
        ["Phase 2, card 1: the board shows 10,001. Build its name. Answer: Ten thousand one (tokens: one 10,000 and "
         "one 1).",
         "Phase 2, card 2: the board shows 10,010. Build its name. Answer: Ten thousand ten. The Th, H and O places "
         "hold 0 and are not said.",
         "Phase 2, card 3: the board shows the tokens one 10,000, two 10s and four 1s. Tap the numeral that matches "
         "and build its name. Answer: 10,024, Ten thousand twenty-four.",
         "Phase 2, card 4: the board shows 13,520. Build its name. Answer: Thirteen thousand five hundred twenty "
         "(tokens: one 10,000, three 1,000s, five 100s and two 10s).",
         "Phase 2, card 5: the board shows 45,867. Build its name. Answer: Forty-five thousand eight hundred "
         "sixty-seven (tokens: four 10,000s, five 1,000s, eight 100s, six 10s and seven 1s).",
         "Phase 3, Challenge: 'Fill in the blanks appropriately. Use commas as required.' Write the number name for "
         "7,209; 10,599; 13,579; 45,045. Answers: Seven thousand two hundred nine; Ten thousand five hundred "
         "ninety-nine; Thirteen thousand five hundred seventy-nine; Forty-five thousand forty-five.",
         "Phase 3, Challenge: 'Fill in the blanks appropriately. Use commas as required.' Write the number name for "
         "39,593; 50,005; 26,050; 81,200. Answers: Thirty-nine thousand five hundred ninety-three; Fifty thousand "
         "five; Twenty-six thousand fifty; Eighty-one thousand two hundred."],
        ["A word card dropped in the right slot snaps in and lights the matching column of the chart and the matching "
         "tokens. A card in a wrong slot springs back and the column that it should name blinks.",
         "A place that holds 0 stays dark and a small note says there is no word for a zero place.",
         "When the name is complete the board reads it aloud with a short pause at the comma.",
         "A name that is not right points to the part before the comma as the first thing to check, and never shows "
         "the full name."],
        "All 7 cards are matched with their numeral, name and tokens, and the last two cards are built correctly "
        "without a hint.",
        ["numeral", "nameSlots", "chartDigits", "tokenTray", "cardIndex"],
        ["M_ZERO_NAME", "M_TT_COLUMN", "M_COMMA_PLACE"],
        ["Which part of the number comes before the comma? Read that part first.",
         "Say the part before the comma and add the word thousand. Then say the hundreds, tens and ones.",
         "Look for the places that hold 0. You do not say those places.",
         "For 10,010: drag Ten thousand, then ten. The Th, H and O places hold 0, so they get no word."]),

    "number_construction": T(
        "tool_number_construction", "Number Construction", "manipulative",
        "Build a number from its name by dropping digit tiles into the TTh, Th, H, T and O slots of a ticket, with a "
        "0 in every place the name skips.",
        "A ticket-printing counter in a warm 3D ticket office with soft shadows and gentle animation. A big blank "
        "ticket lies on the counter with five large slots labelled TTh, Th, H, T and O and a comma gap before the "
        "last three slots; the slots and the number name are the largest things on screen. The number name sits on a "
        "strip above the ticket in large type (for example Ten thousand ten). A tray of digit tiles 0 to 9 sits "
        "below. Controls: drag a digit tile into a slot, tap a slot to clear it, a Print ticket button that checks "
        "the ticket, a Read it back button that shows how the ticket reads as a name, Back and Next in the same "
        "places on every card, a Hint button, a Reset button and progress dots. Read-outs: the worth of each placed "
        "digit under its slot (for example a 3 in the T slot reads 30), the ticket number with its comma, and a "
        "counter of the card number out of 7.",
        ["Phase 1, Recall and get ready: the empty ticket shows TTh, Th, H, T and O. Tap each slot and say what a 1 "
         "in it is worth: 10,000, 1,000, 100, 10 and 1.",
         "Phase 2, Play and apply: read the number name on the strip, drag digit tiles into the slots, put 0 in every "
         "place the name skips, press Print ticket and compare the ticket with the name.",
         "Phase 3, Challenge: write the number for each name of the Name to Number rows in your maths book, using the "
         "same counter."],
        ["Phase 2, card 1: Ten thousand thirty-three. Answer: 10,033 (TTh 1, Th 0, H 0, T 3, O 3).",
         "Phase 2, card 2: Ten thousand four hundred fifty-eight. Answer: 10,458 (TTh 1, Th 0, H 4, T 5, O 8).",
         "Phase 2, card 3: Thirteen thousand five hundred twenty. Answer: 13,520 (the 0 goes in the O slot).",
         "Phase 2, card 4: Twenty thousand. Answer: 20,000 (TTh 2 and a 0 in each of the other four slots).",
         "Phase 2, card 5: Forty-five thousand eight hundred sixty-seven. Answer: 45,867 (TTh 4, Th 5, H 8, T 6, "
         "O 7).",
         "Phase 3, Challenge: 'Fill in the blanks appropriately. Use commas as required.' Write the number for Ten "
         "thousand seven hundred forty-three; Ten thousand ten; Fifty-six thousand four hundred ninety-one. "
         "Answers: 10,743; 10,010; 56,491.",
         "Phase 3, Challenge: 'Fill in the blanks appropriately. Use commas as required.' Write the number for "
         "Ninety thousand nine; Twenty-three thousand two hundred thirty; Thirty-six thousand one. Answers: "
         "90,009; 23,230; 36,001."],
        ["A digit tile in a slot shows its worth under it, for example a 3 in the T slot reads 30.",
         "Pressing Print ticket with an empty slot makes the slot blink and says this place needs a digit, use 0 if "
         "the name skips it.",
         "A ticket that does not match the name shows the name that the ticket reads as, next to the name asked for, "
         "so the student sees the difference without being told the digit.",
         "A correct ticket prints with a stamp and the comma in place before the last three digits."],
        "All 7 tickets are printed correctly.",
        ["nameStrip", "slots", "tileTray", "ticketStatus", "cardIndex"],
        ["M_ZERO_NAME", "M_COMMA_PLACE", "M_TT_COLUMN"],
        ["Which word in the name tells you where the thousands end?",
         "The digits before the word thousand go in TTh and Th. The digits after it go in H, T and O.",
         "Which places does the name skip? Those places need a 0.",
         "For Ten thousand ten: drop 1, 0, 0, 1, 0 into TTh, Th, H, T and O."]),
}
