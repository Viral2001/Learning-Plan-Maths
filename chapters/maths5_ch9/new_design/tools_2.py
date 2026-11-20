# -*- coding: utf-8 -*-
"""Tool specs for T3 and T4 of Class 5 Chapter 9 (Coconut Farm): Smart Splitter and Take Away Groups. Specs only; the tool
pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds are labelled practice values. One activity at a time,
one instruction at a time, large controls, Back and Next in the same place, visible progress, Hint, Retry and Reset always
present, immediate specific feedback that is never red."""
from topics_common import T

TOOLS = {
    "smart_splitter": T(
        "tool_smart_splitter", "Smart Splitter", "manipulative",
        "Divide in the head by cutting the dividend into convenient parts, a sum or a difference, dividing each part and "
        "putting the answers together, and by halving again and again for the divisors 4 and 8. Choosing where to cut the "
        "number is the whole strategy.",
        "The tally board in the packing shed on Susie and Sunitha's coconut farm, drawn as a warm 3D isometric scene with "
        "soft shadows and gentle animation. A long number bar for the dividend is the largest thing on screen, with its "
        "number written on it. An instruction strip at the top shows one sentence in large type, with progress dots under "
        "it. A cutter with a handle slides along the bar to set the cut, and a Plus and Minus switch decides if the number "
        "is cut into two parts that add up to it or is a round bar with a small piece taken off. Under the cut are two "
        "small bars for the two parts, each with a divisor dial and an empty box for its quotient, and an answer slot "
        "where the two quotients are put together. For halving there is a chain of boxes with a Halve button between them. "
        "Controls: drag the cutter; tap Plus or Minus; type each part divided by the divisor; tap Halve to fill the next "
        "box; type the final answer; Check, Hint, Retry (clears the cut of this card), Reset (returns the whole bar), Back "
        "and Next in the same places on every card. Read-outs: the dividend, the divisor, the two parts and a line that "
        "shows whether the parts give the dividend again, and a card number out of 7.",
        ["Look at the bar for 2856 from the video, cut into 2800 and 56 (practice values). "
         "Say why 7 divides both parts easily. Then press Next.",
         "Cut a number where the divisor divides both parts easily, with a plus split or a minus "
         "split, divide each part and put the answers together; then halve a number two and three times.",
         "Fill the book's boxes for the divisions of Try It!, first the four with the split boxes and "
         "then the two with the halving boxes."],
        ["Card 1 (practice values): 3,654 ÷ 6 with a plus split. Answer: 3,654 = 3,600 + 54, 3,600 ÷ 6 = 600 and "
         "54 ÷ 6 = 9, so 600 + 9 = 609. Check: 6 × 609 = 3,654.",
         "Card 2 (practice values): 1,484 ÷ 7 with a plus split. Answer: 1,484 = 1,400 + 84, 1,400 ÷ 7 = 200 and "
         "84 ÷ 7 = 12, so 200 + 12 = 212. Check: 7 × 212 = 1,484.",
         "Card 3 (practice values): 4,995 ÷ 5 with a minus split. Answer: 4,995 = 5,000 − 5, 5,000 ÷ 5 = 1,000 "
         "and 5 ÷ 5 = 1, so 1,000 − 1 = 999. Check: 5 × 999 = 4,995.",
         "Card 4 (practice values): 392 ÷ 4 by halving twice. Answer: half of 392 is 196 and half of 196 is 98, "
         "so 392 ÷ 4 = 98. Check: 4 × 98 = 392.",
         "Card 5 (practice values): 520 ÷ 8 by halving three times. Answer: 260, 130 and 65, so 520 ÷ 8 = 65. "
         "Check: 8 × 65 = 520.",
         "Challenge: 'Try It!' with the split boxes: 64 ÷ 4, 265 ÷ 5, 1560 ÷ 8 and 4824 ÷ 24 (a plus sign in the "
         "first, second and fourth, a minus sign in the third). Answer: for example 64 = 40 + 24 gives 10 + 6 = 16; 265 = "
         "250 + 15 gives 50 + 3 = 53; 1560 = 1600 − 40 gives 200 − 5 = 195; 4824 = 4800 + 24 gives 200 + 1 = 201. Other "
         "splits may also be right.",
         "Challenge: 'Try It!' with the halving boxes: 168 ÷ 8 with the boxes Halve 168, Halve ___ and Halve ___, "
         "and 144 ÷ 4 with the boxes Halve 144 and Halve ___. Answer: 168, 84, 42, 21, so 168 ÷ 8 = 21; and 144, 72, 36, so "
         "144 ÷ 4 = 36. Next stop: Susie's farm."],
        ["A cut at a place where the divisor does not divide a part gets a soft amber note, for example: 7 does not divide "
         "2855 easily. Slide the cutter to 2800.",
         "When both parts are divided the tool joins the answers and says, for example: 400 and 8 together make 408, and 7 × "
         "408 = 2856.",
         "In minus mode the tool shows the round bar with a small piece taken off, and says: 5,000 is 5 more than 4,995, so "
         "take the share of 5 away at the end.",
         "Each press of Halve fills the next box and shows the half, for example half of 392 is 196.",
         "A part divided wrongly slides back with a clue such as: Check by multiplying. What times 6 is 3,600?"],
        "The student has cut and divided the numbers of the cards by splitting and by halving, and has filled the book's "
        "boxes for Try It!.",
        ["dividend", "divisor", "cutPosition", "mode", "halvingChain", "challengeIndex"],
        ["M_BAD_SPLIT", "M_ROUND_WRONG"],
        ["Look at the number. Is there a round number close to it that the divisor divides easily?",
         "Cut the number into two parts. Both parts should be easy to divide by the divisor, or one part is round and the "
         "other is small.",
         "Divide each part by the divisor, then add the answers if you split with a plus, or take one answer from the other "
         "if you split with a minus.",
         "For 2856 ÷ 7: cut at 2800 and 56, 2800 ÷ 7 = 400 and 56 ÷ 7 = 8, so the answer is 400 + 8 = 408."]),

    "take_away_groups": T(
        "tool_take_away_groups", "Take Away Groups", "manipulative",
        "Divide by taking away groups of the divisor from a pile again and again, record the groups taken away as partial "
        "quotients, see that a group that is too big cannot be taken away, read what is left as the remainder, and check "
        "the division with N = D × Q + R.",
        "A pile of coconuts at the packing shed on Susie and Sunitha's farm, drawn as a warm 3D isometric scene with soft "
        "shadows and gentle animation. The pile and its number are the largest things on screen, with a row of empty bags "
        "beside it. An instruction strip at the top shows one sentence in large type, with progress dots under it. Three "
        "take-away buttons sit under the pile: Take 100 groups, Take 10 groups and Take 1 group, each of the divisor; "
        "pressing one removes that many groups of coconuts from the pile and the number left changes at once. The book's "
        "layout fills in on the right, one subtraction under another, with the group counts added up along the top, for "
        "example 100 + 80 + 1. A remainder counter shows what is left, and an N = D × Q + R board below has slots for D, "
        "Q and R. An estimate bar above the pile asks if the answer is less than 100 or between 100 and 200. Controls: "
        "tap a take-away button; tap Undo; set the estimate; type D, Q and R into the board; Check, Hint, Retry (restores "
        "the pile of this card), Reset (a new pile), Back and Next in the same places on every card. Read-outs: the "
        "dividend, the divisor, the coconuts left, the groups taken so far, and a card number out of 7.",
        ["Look at the pile of 378 coconuts and the bags of 6 from the video (practice "
         "values). Say how many groups of 6 you could take away first. Then press Next.",
         "Take away groups from a pile, try a group that is too big and see why it cannot be "
         "taken, estimate first and take the biggest groups that fit, divide by a two-digit number, and write the "
         "remainder rule.",
         "Fill the blanks of the book's two divisions, 726 ÷ 4 and 902 ÷ 16, and answer the book's "
         "questions about N = D × Q + R."],
        ["Card 1 (practice values): 456 ÷ 6 in two takes. Answer: take 70 groups, 6 × 70 = 420 and 456 − 420 = 36; "
         "take 6 groups, 6 × 6 = 36 and 36 − 36 = 0. 70 + 6 = 76. Check: 6 × 76 = 456.",
         "Card 2 (practice values): 509 ÷ 7. Try Take 100 groups first. Answer: 7 × 100 = 700 is more than 509, "
         "so it is too big. Take 70 groups: 7 × 70 = 490 and 509 − 490 = 19. Take 2 groups: 7 × 2 = 14 and 19 − 14 = 5. "
         "Quotient 72, remainder 5.",
         "Card 3 (practice values): estimate 845 ÷ 5 first, then divide. Answer: 5 × 100 = 500 is less than 845 "
         "and 5 × 200 = 1000 is more, so the answer is between 100 and 200. Take 100 groups: 845 − 500 = 345. Take 60 "
         "groups: 345 − 300 = 45. Take 9 groups: 45 − 45 = 0. 100 + 60 + 9 = 169. Check: 5 × 169 = 845.",
         "Card 4 (practice values): 372 ÷ 12 with a two-digit divisor. Answer: take 30 groups, 12 × 30 = 360 and "
         "372 − 360 = 12; take 1 group, 12 − 12 = 0. 30 + 1 = 31. Check: 12 × 31 = 372.",
         "Card 5 (practice values): write the remainder rule for 509 ÷ 7. Answer: D = 7, Q = 72, R = 5, so "
         "509 = 7 × 72 + 5, and the remainder 5 is less than the divisor 7.",
         "Challenge: 'Let Us Learn to Divide' 726 ÷ 4: the quotient parts are 100 + ___ + ___, take away ___ "
         "first and 326 is left, take away 320 and 6 is left, take away ___ and 2 is left. 'Could we have written 200 "
         "here?' Answer: the blanks are 400, 80, 4 and 1, so 100 + 80 + 1 = 181 with remainder 2; 200 is too big because 4 "
         "× 200 = 800 is more than 726.",
         "Challenge: 902 ÷ 16: the quotient parts are ___ + 6, take away 800, then 96, and 6 is left. 'What "
         "should we write here so that we get a number close to 902 but less than it? Could we have multiplied 16 by a "
         "larger tens?' Then the book's questions, with the equal sign of the book written in words: 'Is 726 the same as 4 × 181? "
         "Yes/No. So, 726 is 4 × 181 plus ___. Is 902 the same as 16 × 56? Yes/No. So, 902 is 16 × 56 plus ___.' Answer: the blank is 50, so quotient 56 and remainder 6; 16 × 60 = 960 is more than 902. No and "
         "No: 726 = 4 × 181 + 2 and 902 = 16 × 56 + 6, so N = D × Q + R. Next stop: the coconut oil."],
        ["A group that is too big stays in the pile and the tool says, for example: 700 is more than the 509 coconuts left. "
         "Take away a smaller group.",
         "After each take-away the layout shows the subtraction and the number left, for example 509 − 490 = 19.",
         "When nothing is left the tool adds the groups, for example 70 + 6 = 76, and shows 6 × 76 = 456.",
         "When some coconuts are left that are fewer than the divisor, the tool says: 5 is less than 7, so no more groups "
         "of 7 can be taken. 5 is the remainder.",
         "A wrong D, Q or R on the board slides back with a clue such as: The remainder must be less than the divisor."],
        "The student has divided the numbers of the cards by taking away groups, found each quotient and remainder, written "
        "N = D × Q + R, and filled the book's two divisions.",
        ["dividend", "divisor", "pileLeft", "groupsTaken", "estimate", "ndqrBoard", "challengeIndex"],
        ["M_TOO_BIG_GROUP", "M_REMAINDER_BIG"],
        ["Look at the pile and the divisor. How many groups of the divisor could you take away at once?",
         "Take the biggest group that fits, hundreds of groups first, then tens, then ones.",
         "Take away the group, write down how many groups you took, and look at how many coconuts are left. Repeat.",
         "For 456 ÷ 6: take 70 groups, 456 − 420 = 36 are left; take 6 groups, nothing is left. 70 + 6 = 76."]),
}
