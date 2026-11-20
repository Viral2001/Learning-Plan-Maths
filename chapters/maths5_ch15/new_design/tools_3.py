# -*- coding: utf-8 -*-
"""Tool spec for T7 of Class 5 Chapter 15 (Data Through Pictures): Tool 5 Picture Detective. Spec only; the tool page is
built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. One activity at a time, one instruction at a
time, large controls, Back and Next in the same places, visible progress, Hint, Retry and Reset always present,
immediate specific feedback that is never red (a soft amber note means look again)."""
from topics_common import T

TOOLS = {
    "picture_detective": T(
        "tool_picture_detective", "Picture Detective", "manipulative",
        "Count the children of a picture who have a chosen thing (a cap, glasses, a book, a backpack, or two things "
        "together), compare the counts, compare a count with half of all the children, and use the counts to judge a "
        "statement as true or false. Lighting a group up makes the counting exact, and the counts side by side make "
        "more than and more than half easy to judge.",
        "The photo board of Samaira and Kabir's class newsroom, drawn as a warm, polished educational-game scene with "
        "soft shadows and gentle animation, in soft cream and blue-grey wall tones. The picture of the children is "
        "the largest thing on screen and nothing else competes with it. In the middle of the board is the picture "
        "pinned on the wall: for practice a picture of 10 children with scarves and bags (practice values), "
        "and for the book's question the picture of 17 school children, 9 boys and 8 girls, as in your maths book, with the "
        "girls in a blue pinafore over a cream shirt and the boys in a cream shirt and blue shorts, standing in "
        "two rows with their caps, glasses, books and backpacks drawn clearly. An instruction strip at the top shows "
        "one sentence in large type, with progress dots under it. Under the picture is a row of filter chips: "
        "Girls, Boys, Cap, Glasses, Book and Backpack (in the practice picture the chips are Scarf and Bag). A small "
        "switch called and sits beside the chips. A counter beside the picture shows how many children are lit up, "
        "and a small row of bars beside it keeps one bar for each group already counted, with the number written on "
        "each bar, so that two counts can be compared at a glance. A thin half-way marker can be switched on at half "
        "of the number of children, written next to it. Below this a statement card shows one statement in large "
        "type with two big buttons, TRUE and FALSE. Controls: tap a chip to light up the children who match (they "
        "glow orange and the others fade); tap a second chip while the and switch is on to light up only the "
        "children who match both; tap a lit chip again to switch it off; tap TRUE or FALSE; Check; Hint; Retry, which "
        "clears the highlights and the answer of this card; Reset, which clears all the cards; Back and Next in the "
        "same places on every card. Read-outs: the number of children lit up, the bars of the counted groups with "
        "their numbers, the half-way number, and a card number out of 7. The group being asked about glows bright "
        "tangerine, a right answer turns green, and a look again note is soft amber, never red.",
        ["Look at the group in the video, some children with hats. The instruction "
         "reads: To check a statement, count the children it talks about. Tap a chip and watch the children light up "
         "and the counter show the number, then press Next.",
         "In a practice picture of 10 children with scarves and bags (practice values), tap "
         "Scarf and Bag to count each group, light up both together with and, compare two groups, and use the "
         "half-way marker to judge more than half. Then answer a true or false card about the picture.",
         "In the picture of 17 school children, answer your maths book's eight statements, "
         "TRUE or FALSE, one card at a time, from All girls are wearing glasses to There is no child who has all "
         "three items, a cap, a book and a backpack."],
        ["Card 1 (practice values): the practice picture has 10 children. Tap Scarf and then Bag. How many "
         "children have a scarf, and how many have a bag? Answer: 6 children have a scarf and 5 children have a "
         "bag.",
         "Card 2 (practice values): compare the two counts. True or false: More children have a scarf than "
         "have a bag. Answer: True, because 6 is more than 5.",
         "Card 3 (practice values): switch on and and tap Scarf and Bag together. How many children have "
         "both? Then answer True or False: Some children have a scarf and a bag. Answer: 3 children have both, so "
         "the statement is true, because some means at least one.",
         "Card 4 (practice values): switch on the half-way marker. Half of 10 is 5. True or false: More "
         "than half of the children have a scarf. Answer: True, because 6 is more than 5.",
         "Card 5 (practice values): the same marker. True or false: More than half of the children have a "
         "bag. Answer: False, because 5 is exactly half of 10, and it is not more than half.",
         "Challenge: 'All girls are wearing glasses.' '10 children are wearing caps on their heads.' "
         "'More boys are holding books than girls.' 'More than half of the children are wearing glasses.' Light up "
         "the group each statement talks about, read the counter, and press TRUE or FALSE. Answer: false, true, "
         "false, false. There are 8 girls and 3 of them wear glasses; 10 children wear caps; 7 boys and 7 girls hold "
         "books, the same number; 7 children wear glasses and half of 17 is 8 1/2.",
         "Challenge: 'The number of children holding books is greater than the number of children wearing "
         "caps.' 'The number of boys wearing glasses is greater than the number of girls wearing glasses.' 'Some "
         "children are wearing both glasses and caps.' 'There is no child who has all three items, a cap, a book "
         "and a backpack.' Answer: true, true, true, false. 14 children hold books and 10 wear caps; 4 boys and 3 "
         "girls wear glasses; 6 children wear both; one child, the girl in the back row on the left, has a cap, a "
         "book and a backpack."],
        ["Lighting up a group shows the counter and adds a bar for that group, for example: Cap: 10 children.",
         "With the and switch on, only the children who match both chips light up, and the counter says so, for "
         "example: Cap and Glasses: 6 children.",
         "A wrong TRUE or FALSE slides back with a clue that says what to count, never the answer, for example: Did "
         "you count the girls first? Light up Girls and then Glasses.",
         "A right answer turns the card green and shows the counts that settled it, for example: 7 children wear "
         "glasses and half of 17 is 8 1/2, so 7 is not more than half.",
         "For the statement with some or no child, the tool lights up one matching child as the clue, for example: "
         "Is there a child with a cap, a book and a backpack? Light them up and look."],
        "All the cards are answered correctly, with the practice cards and the eight statements of the picture "
        "judged by counting.",
        ["litChips", "andSwitch", "countedBars", "halfMarker", "statementCards", "challengeIndex"],
        ["M_ONE_LOOK", "M_HALF_ODD"],
        ["What does the statement talk about: girls, boys, caps, glasses, books or backpacks? Count only those "
         "children.",
         "Light up the group with the chip. Read the counter, and then compare it with the other count, or with half "
         "of all the children.",
         "For more than half, find half of all the children first. For some or no child, look for one child who "
         "matches.",
         "Light up the group and read the number. The tool shows the counts that settle this statement, and you "
         "press TRUE or FALSE."]),
}
