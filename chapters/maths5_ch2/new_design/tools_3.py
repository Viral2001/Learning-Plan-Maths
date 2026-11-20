# -*- coding: utf-8 -*-
"""Tool specs for T7 and T8 of Class 5 Chapter 2 (Fractions): Paratha Number Line (Tool 7) and Benchmark Number Line
(Tool 8). Specs only; the tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. One activity at a time, one instruction at a
time, large controls, Back and Next in the same place, visible progress, simple restart, immediate specific feedback,
hints, retry and reset. Raman's family kitchen is the one environment of the chapter."""
from topics_common import T

TOOLS = {
    "paratha_number_line": T(
        "tool_paratha_number_line", "Paratha Number Line", "manipulative",
        "Join pieces of one size into whole parathas along a number line, so that a fraction greater than 1 is read as "
        "a whole number and a part: the bottom number says how many pieces make 1 whole, the groups are the whole "
        "number and the pieces left over are the part.",
        "Raman's family kitchen, drawn as a warm, polished 3D isometric scene with soft shadows and gentle animation. "
        "Raman's father stands at the counter rolling a paratha. In front of him a wooden plate holds pieces of "
        "paratha, all of one size. A number line runs along the edge of the counter from 0 "
        "to 5 with equal marks; it is the largest thing on screen, and the whole numbers 0, 1, 2, 3, 4 and 5 are "
        "labelled in large type. A cut switch with three buttons, Halves, Fourths and Thirds, sets the size of the "
        "pieces on the plate and re-spaces the marks of the line (the Thirds button swaps the paratha for a round "
        "pizza, as in the book). The student drags one piece at a time from the plate and it lands on the next mark "
        "of the line, where a small marker hops to it and the mark shows its fraction label. When enough pieces for "
        "one whole sit together (2 halves, 4 fourths or 3 thirds) an amber ring snaps around them and the label 1 "
        "paratha (1 pizza) appears above the ring. Read-outs: a pieces counter, for example 5 pieces of 1/2; a rings "
        "counter that counts whole parathas; a left-over counter that counts the pieces outside the rings; and a "
        "reading strip that writes the fraction and then the whole number and the part as the student places "
        "pieces, for example 5/2 = 2 + 1/2 = 2 1/2. On the challenge cards two answer boxes, Whole and Part, and a "
        "Check button appear; on one card a Target banner names a mark to reach. On the last card the pieces are "
        "ants, each 1/4 cm long, and the counter edge becomes a ruler in cm. Fixed controls in the same places on "
        "every card: Undo takes back the last piece, Retry clears the line for this card, Reset restores the whole "
        "plate, Hint, Back, Next and progress dots.",
        ["Look at the plate of pieces of 1/2 and drag two of them together to make 1 "
         "whole paratha.",
         "Choose a cut (halves, fourths or thirds), drag the pieces onto the number line one "
         "at a time, watch each group that fills a paratha ring into 1 paratha, and read the fraction and the whole "
         "number and the part.",
         "Use the same plate and number line for the book's questions about Raman, Dadaji and "
         "Baba, and about the 16 ants."],
        ["Card 1 (practice values): choose Halves and drop 3 pieces of 1/2 on the line. How many whole "
         "parathas do the rings show, and what is the total? Answer: 1 ring and 1 piece left over, so 3/2 = 1 + 1/2 "
         "= 1 1/2 parathas.",
         "Card 2 (practice values): choose Halves and drop 10 pieces of 1/2. Answer: 5 rings and no piece "
         "left over, so 10/2 = 5 parathas.",
         "Card 3 (practice values): choose Fourths and drop 13 pieces of 1/4. Answer: 4 + 4 + 4 = 12 pieces "
         "make 3 rings and 1 piece is left over, so 13/4 = 3 + 1/4 = 3 1/4 parathas.",
         "Card 4 (practice values): choose Thirds, the round pizza, and drop 7 slices of 1/3. Answer: "
         "3 + 3 = 6 slices make 2 rings and 1 slice is left over, so 7/3 = 2 + 1/3 = 2 1/3 pizzas.",
         "Card 5 (practice values): choose Fourths and keep dropping pieces of 1/4 until the marker reaches "
         "the Target 3 1/2. How many pieces did you use? Answer: 14 pieces, because 14/4 = 3 + 2/4 = 3 2/4, which is "
         "the same as 3 1/2.",
         "Challenge: 'Raman ate 6 pieces of 1/2 paratha, Dadaji ate 7 pieces of 1/2 paratha and Baba ate 5 "
         "pieces of 1/2 paratha. How many parathas did each of them eat? Use the number line to find the answer.' "
         "Answers: Raman 6/2 = 3 parathas, Dadaji 7/2 = 3 1/2 parathas and Baba 5/2 = 2 1/2 parathas.",
         "Challenge: 'If the length of an ant is 1/4 cm, then what is the total length of 16 such ants "
         "walking in a line? Use the number line given below.' Answer: 16/4 = 4 cm."],
        ["A piece dropped on the line lands on the next mark, the marker hops there and the reading strip grows by one "
         "piece, for example 5 pieces of 1/2 make 5/2.",
         "When the last piece of a group lands, a ring snaps shut and says 1 paratha, the rings counter goes up by 1 "
         "and the left-over counter drops back to 0.",
         "A wrong Whole or Part gives a specific message built from the line, for example: 13 pieces of 1/4: three "
         "full parathas use 12 pieces, 1 piece is left, so 3 1/4. The rings are counted for Whole and the pieces "
         "left over are the Part.",
         "If the student writes 2 1/2 as 2 times 1/2, the strip says: 2 1/2 is 2 whole parathas and 1/2 more, not "
         "2 times 1/2.",
         "If the student stops at the mark 1, the screen says: the line goes on past 1, keep dropping pieces.",
         "On the card with the Target banner the tool shows how many marks are left to the target after every piece "
         "and never shows the number of pieces needed."],
        "All 7 cards are answered correctly, and the last two cards, the book's own questions, are answered without "
        "the bottom-out hint.",
        ["cut", "piecesOnLine", "rings", "leftOver", "readingStrip", "wholeBox", "partBox", "targetMark", "cardIndex"],
        ["M_NO_PAST_ONE", "M_MIXED_TIMES"],
        ["How many pieces of this cut make 1 whole paratha?",
         "Drop the pieces one at a time. Each time a ring snaps shut, that is one more whole paratha. How many rings "
         "can you make?",
         "Count the pieces outside the rings: that is the part. For pieces of 1/4, 4 pieces make a ring, so with 13 "
         "pieces, 4 + 4 + 4 = 12 pieces make 3 rings and 1 piece is left.",
         "The tool rings the pieces for you: for 13 pieces of 1/4 it shows 3 rings and 1 piece left over, so 13/4 = "
         "3 1/4. Then a similar card follows for you to try."]),

    "benchmark_line": T(
        "tool_benchmark_line", "Benchmark Number Line", "manipulative",
        "Place fraction cards against the two fixed signposts 1/2 and 1 to decide whether each fraction is less than, "
        "equal to or more than the signpost, and compare two fractions through the zones they land in.",
        "A shelf in Raman's family kitchen, drawn as a warm, polished 3D isometric scene with soft shadows and gentle "
        "animation. The shelf is a number line from 0 to 2 with equal marks; it is the largest thing on screen, and "
        "the whole numbers 0, 1 and 2 are labelled. Two wooden signposts stand on it: one labelled 1/2 halfway "
        "between 0 and 1, and one labelled 1 at the mark 1. Five landing zones lie along the shelf, each with a name "
        "tag: Less than 1/2, Equal to 1/2, Between 1/2 and 1, Equal to 1 and More than 1. A tray of fraction cards "
        "sits below the shelf; each card is a cut paratha with its fraction written large. A signpost switch, Use 1 "
        "or Use 1/2, lights the zones that matter for the chosen signpost. Under the tray lies a comparison pair "
        "slot: two empty boxes with a sign box between them and two buttons, < and >. The student drags a card onto "
        "a zone or onto the line, or drags two cards into the pair slot and picks the sign. Read-outs: a check "
        "strip that writes the reason in words after every card (for the signpost 1: top number 9, bottom number 10, "
        "so less than 1; for the signpost 1/2: bottom number 22, half of it is 11, top number 9 is less than 11, so "
        "less than 1/2); a small panel that shows the top number, the bottom number and half of the bottom number of "
        "the selected card; and a counter of cards sorted out of the cards on this screen. Fixed controls in the "
        "same places on every card: Check, Hint, Retry which returns the cards of this step, Reset which restores "
        "all cards, Back, Next and progress dots.",
        ["Two fraction cards sit on the shelf, one to the left of the signpost 1 and "
         "one to the right of it. Tap each card and say whether it is less than, equal to or more than 1.",
         "Sort fraction cards against the signpost 1 first and then against the signpost "
         "1/2, read the check that the tool writes, and then drop two cards into the pair slot and compare them by "
         "the zones they landed in.",
         "Use the same shelf and pair slot for the book's comparisons with 1 and with 1/2."],
        ["Card 1 (practice values): choose Use 1 and sort the cards 9/10, 10/10 and 11/10. Answer: 9/10 is "
         "less than 1 (9 is less than 10), 10/10 is equal to 1 and 11/10 is more than 1 (11 is more than 10).",
         "Card 2 (practice values): drop 5/6 and 7/4 into the pair slot and compare them using 1. Answer: "
         "5/6 is less than 1 and 7/4 is more than 1, so 5/6 < 7/4.",
         "Card 3 (practice values): choose Use 1/2 and sort the cards 9/22, 11/22 and 13/22. Answer: half of "
         "22 is 11, so 9/22 is less than 1/2, 11/22 is equal to 1/2 and 13/22 is more than 1/2 (it lands between 1/2 "
         "and 1).",
         "Card 4 (practice values): drop 7/16 and 11/20 into the pair slot and compare them using 1/2. "
         "Answer: half of 16 is 8 and 7 is less than 8, so 7/16 is less than 1/2. Half of 20 is 10 and 11 is more "
         "than 10, so 11/20 is more than 1/2. So 7/16 < 11/20.",
         "Card 5 (practice values): which pair can the signpost 1/2 settle, (i) 5/12 and 9/16 or (ii) 8/17 "
         "and 6/13? Answer: (i). 5/12 is less than 1/2 (half of 12 is 6) and 9/16 is more than 1/2 (half of 16 is "
         "8). In (ii) both are less than 1/2 (half of 17 is 8 1/2 and half of 13 is 6 1/2), so 1/2 cannot decide.",
         "Challenge: 'Compare the following fractions using 1 as a reference. Share your reasoning in the "
         "class. (a) 8/7 ___ 9/15 (b) 13/20 ___ 17/15 (c) 7/6 ___ 8/8 (d) 6/6 ___ 19/12 (e) 12/9 ___ 4/5 "
         "(f) 15/5 ___ 16/4' Answers: (a) > (b) < (c) > (d) < (e) > (f) <. For (f) both are more than 1, so count "
         "the wholes: 15/5 = 3 and 16/4 = 4.",
         "Challenge: 'Compare the following fractions. Where possible, compare the fractions with 1/2. "
         "(a) 2/9 and 4/7 (b) 11/14 and 7/20 (c) 5/7 and 3/9 (d) 6/7 and 4/10 (e) 9/17 and 3/15 (f) 7/12 and 3/11 "
         "(g) 1/3 and 5/9 (h) 3/9 and 4/7' Answers: (a) 2/9 < 4/7 (b) 11/14 > 7/20 (c) 5/7 > 3/9 (d) 6/7 > 4/10 "
         "(e) 9/17 > 3/15 (f) 7/12 > 3/11 (g) 1/3 < 5/9 (h) 3/9 < 4/7."],
        ["A card dropped in the right zone stays there and the check strip writes the reason, for example: 12/9: 12 "
         "is more than 9, so it is more than 1.",
         "A card dropped in a wrong zone slides back, and the strip shows the numbers to compare without naming the "
         "zone, for example: bottom number 22, half of it is 11, top number 9: compare 9 with 11.",
         "A card whose top number is close to half of its bottom number is checked with the half panel, for "
         "example: 5/9: half of 9 is 4 1/2 and 5 is more than 4 1/2, so it is more than 1/2, not equal to it.",
         "In the pair slot the tool first shows the zone of each card and then asks for the sign. A wrong sign gets: "
         "the card whose zone is nearer to 0 is the smaller one.",
         "When both cards land in the same zone the tool says the signpost cannot decide this pair and asks for "
         "another way, for example for 15/5 and 16/4: write each as a number of wholes."],
        "All 7 cards are answered correctly with the reason read from the check strip, and the last two cards, the "
        "book's own questions, are answered without the bottom-out hint.",
        ["signpost", "cardZone", "pairSlots", "signChoice", "checkStrip", "halfPanel", "sortedCount", "cardIndex"],
        ["M_NEAR_HALF", "M_TOP_ONLY", "M_BIGGER_DENOM"],
        ["Which signpost is this card measured against, 1 or 1/2?",
         "For the signpost 1, compare the top number with the bottom number. For the signpost 1/2, find half of the "
         "bottom number and compare the top number with it.",
         "For 9/22: half of 22 is 11, and the top number 9 is less than 11, so 9/22 goes in Less than 1/2.",
         "The tool puts the card in its zone and writes the check, for example: 11/22: half of 22 is 11, so it is "
         "equal to 1/2. Then a similar card follows for you to try."]),
}
