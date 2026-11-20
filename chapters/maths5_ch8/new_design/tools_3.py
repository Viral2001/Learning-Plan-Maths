# -*- coding: utf-8 -*-
"""Tool spec for T10 of Class 5 Chapter 8 (Weight and Capacity): Measuring Jug (reading container scales, adding capacities,
and changing between l and ml by pouring into a vessel marked only in ml). Spec only; the tool page is built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds are labelled practice values. One activity at a
time, one instruction at a time, large controls, Back and Next in the same place, visible progress, Hint, Retry and Reset
always present, immediate specific feedback that is never red."""
from topics_common import T

TOOLS = {
    "measuring_jug": T(
        "tool_measuring_jug", "Measuring Jug", "manipulative",
        "Read the scale of a container, add the capacities of several containers written in l and ml, and change between l "
        "and ml by pouring into a vessel marked only in ml, so that 2 l is seen as 2,000 ml.",
        "The milkman's corner of Anu's neighbourhood market, drawn as a warm 3D isometric scene with soft shadows and gentle "
        "animation. A table holds three measuring jugs, and they are the largest things on screen: a jug with 1 l at its top "
        "mark and a 500 ml mark halfway up, a jug with 500 ml at its top mark and marks every 100 ml, and a jug with 100 ml at "
        "its top mark and a 50 ml mark. Beside them stand a milk can with a tap and a tall vessel marked in ml only, with marks "
        "every 1,000 ml. An instruction strip at the top shows one sentence in large type, with progress dots under it. "
        "Controls: drag the pouring handle to fill a jug up to a mark (the liquid rises smoothly); tap a mark to read it; pour "
        "a jug into the ml only vessel and read the mark it reaches; a unit chooser l or ml; number boxes l and ml to type a "
        "capacity; Check, Hint, Retry (empties the jugs for this card), Reset (restores all jugs), Back and Next in the same "
        "places on every card. Read-outs: the amount in each jug as the liquid rises, the mark reached in the ml only vessel, "
        "and a card number out of 6.",
        ["Look at the video's jug with its scale and the line of l and ml. Say how many ml are in "
         "1 l, then press Next.",
         "Fill a jug to a mark and read it, read the top mark of a jug, pour a jug and a cup into the "
         "ml only vessel, and type mixed capacities in ml and back (practice values).",
         "Write the capacity of the book's groups of containers, and find the mark for 2 l in a vessel "
         "marked in ml only."],
        ["Card 1 (practice values): fill the 500 ml jug up to the 300 ml mark and read it. Answer: 300 ml; the marks "
         "are every 100 ml, so the 3rd mark is 300 ml.",
         "Card 2 (practice values): read the 1 l jug at its 500 ml mark and say how much is in the jug. Answer: 500 "
         "ml, which is half of 1,000 ml, so the jug is half full.",
         "Card 3 (practice values): pour a 2 l jug and a 250 ml cup into the vessel marked in ml only. Which mark does "
         "the liquid reach? Answer: 2,000 + 250 = 2,250 ml, which is 2 l 250 ml.",
         "Card 4 (practice values): type 3 l 40 ml in ml and 5,030 ml in l and ml. Answer: 3 × 1,000 = 3,000 and the "
         "ml part is 040, so 3,040 ml; 5,030 − 5,000 = 30, so 5 l 30 ml.",
         "Challenge: 'Write the total capacity of the following containers in each blank.' Read the four groups of "
         "containers of your maths book (each container's top mark is its capacity). Answer: group 1 is 1 l 600 ml, group 2 "
         "is 1 l 500 ml, group 3 is 0 l 700 ml, group 4 is 2 l 100 ml, found by adding l with l and ml with ml.",
         "Challenge: 'Bhalerao's family orders 2 l of milk everyday. This family has a vessel marked in ml only. What "
         "mark will you see in the vessel corresponding to 2 l?' Pour 2 l into the vessel and read the mark. Answer: 2 × "
         "1,000 = 2,000 ml."],
        ["The liquid rises to the mark and the read-out says the amount, for example: 300 ml: the 3rd mark of 100 ml each.",
         "A capacity read from the wrong mark gets a clue, for example: This jug has 500 ml at its top. Read the top mark "
         "for its capacity.",
         "In the ml only vessel the tool shows both numbers, for example: 2 l poured. The mark reads 2,000 ml.",
         "A mixed capacity typed in ml with the ml part in the wrong place gets the other value, for example: 3,400 ml is "
         "3 l 400 ml. The ml part 40 takes three places, 040."],
        "All six cards are done, including the book's four groups of containers and the milkman's 2 l, and the student has "
        "read at least one jug and poured into the ml only vessel.",
        ["currentCard", "jugAmounts", "chosenUnit", "vesselMark", "typedL", "typedMl", "groupTotals"],
        ["M_KG_100G", "M_PART_PLACE"],
        ["Which unit is written on the jug, l or ml? Look at the top mark of each jug.",
         "What is the top mark of each jug? That is its capacity. Add the l together and the ml together.",
         "Add the capacities of the jugs in a group, change 1,000 ml to 1 l if you have to, and write the l and the ml.",
         "Fill the jugs of the group one by one and watch the total build up in the read-out under the jugs."]),
}
