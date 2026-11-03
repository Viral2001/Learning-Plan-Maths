# -*- coding: utf-8 -*-
"""Tool specs for T7 (Tool 4, digit_swap) and T9 (Tool 5, rounding_line). Specs only; the tool pages are built
later. Phase 1 recalls the video idea, Phase 2 is play, Phase 3 is the book's own question with its own values."""
from topics_common import T

TOOLS = {
    "digit_swap": T(
        "tool_digit_swap", "Digit Swap Challenge", "manipulative",
        "Swapping two digits of a number moves each digit into the other digit's place, so each one takes a new "
        "value and the number changes. The student swaps two coaches of a number train, compares the old number "
        "with the new number, and chooses swaps to reach a target.",
        "A warm, colourful 3D and isometric station with one short railway track, soft shadows and gentle "
        "animation. The number train is the largest thing on the screen: each digit of the number is one big coach "
        "on the track, the place name (TTh, Th, H, T, O) is painted under each coach, and the whole number with "
        "its comma is written large above the train. Below the track two number cards sit side by side, Before "
        "and After, with a line that says bigger, smaller or the same and shows the change in value. The task of "
        "the card is one short sentence above the train. Controls, all large: tap a coach to select it (a "
        "selected coach glows and shows 1 or 2), Swap (the two coaches glide past each other), Undo, Reset, "
        "Check, Hint, Back and Next in the same place on every card, and a row of progress dots, one for each of "
        "the 6 cards.",
        ["Phase 1, Recall and get ready: the train shows 6,142 with the place name under each coach; before any "
         "swap the student predicts whether swapping the first two coaches will make the number bigger, smaller or "
         "the same, and then the swap happens.",
         "Phase 2, Play and apply: the student selects two coaches, presses Swap, reads the Before and After "
         "cards, and chooses swaps to make a number bigger, smaller, unchanged, the biggest or the smallest, or to "
         "land in a given range.",
         "Phase 3, Challenge: the book's digit swap question with the numbers 1,478, 10,593 and 48,247, exactly as "
         "the book gives it, shown as a train for each number."],
        ["Play card 1: the train shows 2,614. Swap the coaches 2 and 6 and compare the new number with 2,614. "
         "Answer: 6,214, which is bigger, because 6,214 − 2,614 = 3,600.",
         "Play card 2: the train shows 4,552. Swap the two coaches that hold the digit 5, then swap the coach 4 "
         "with the first coach 5. Answer: the first swap leaves 4,552 as it was, because the two digits are the "
         "same; the second swap gives 5,452, which is bigger.",
         "Play card 3: the train shows 36,172. Make the biggest number you can with one swap, then the smallest. "
         "Answer: biggest 76,132 (swap 3 and 7); smallest 16,372 (swap 3 and 1).",
         "Play card 4: the train shows 52,430. Swap two coaches to make a number between 25,000 and 30,000. "
         "Answer: 25,430 (swap 5 and 2).",
         "Challenge card 1: (a) In the number 1,478, interchanging the digits 7 and 4 gives 1,748. Now, "
         "interchange any two digits in the number 1,478 to make a number that is larger than 5,500. (b) "
         "Interchange two digits of 10,593 to make a number (i) between 11,000 and 15,000 (ii) more than 35,000. "
         "Answer: (a) 7,418 or 8,471; (b)(i) 13,590; (b)(ii) 50,193 or 90,513.",
         "Challenge card 2: (c) Interchange two digits of 48,247 to make a number (i) as small as possible (ii) as "
         "big as possible. Answer: (i) 28,447; (ii) 84,247."],
        ["After every swap the Before and After cards show both numbers with their place chart, and a line says "
         "bigger, smaller or the same together with the change in value, for example 3,600 more.",
         "Two coaches with the same digit show 'These two digits are the same, so the number stays the same.'",
         "A swap that would put 0 at the front shows 'A number cannot start with 0. Try another swap.' and the "
         "coaches slide back.",
         "A swap that does not meet the card shows the new number beside the task, for example 'This number is "
         "30,591. The task needs more than 35,000.', and Undo glows.",
         "A correct swap makes the train glow green and names the swap that was made, such as 'You swapped 5 and "
         "2.' If the card has more than one right swap, it adds 'Another swap also works. Can you find it?'",
         "Reset puts the train back to its first number; Back and Next never lose the work on a finished card."],
        "All 6 cards are done with a correct swap, and the student has made at least one swap that made a number "
        "bigger and one that made a number smaller.",
        ["digits", "selectedCoaches", "originalNumber", "newNumber", "swapCount", "cardIndex", "hintLevel"],
        ["M_SWAP_VALUE"],
        ["Which place must change for the number to get bigger or smaller? Look at the leftmost coaches first.",
         "A bigger digit in a bigger place makes the number bigger. A smaller digit in that place makes it "
         "smaller.",
         "Tap the coach with the digit you want to move and the coach whose place you want to change, press Swap "
         "and read the After card.",
         "To make 7,358 bigger, bring the 8 to the thousands place: swap 7 and 8 to get 8,357. Now try the next "
         "card."]),

    "rounding_line": T(
        "tool_rounding_line", "Rounding Number Line", "manipulative",
        "The nearest ten, hundred or thousand of a number is the neighbouring mark that needs fewer jumps. The "
        "student places a rabbit on a milestone road between two neighbouring marks, counts the jumps to each "
        "mark and chooses the nearer one.",
        "A warm, colourful 3D and isometric countryside with one milestone road, soft shadows and gentle "
        "animation. The target number is the largest text, above the road. The road is a straight path drawn as a "
        "number line: a carrot (the food) at each end shows the two neighbouring tens, hundreds or thousands, a "
        "lit milestone in the middle shows the halfway number, and the student drags a rabbit marker along the "
        "road. Read-outs: under the rabbit the number it stands on, under each carrot the jumps to it (shown once "
        "the rabbit is placed), and a line Nearest: ___ that fills in after the choice. Controls, all large: a "
        "three-button switch Tens, Hundreds and Thousands, tap a carrot to choose it, Check, Hint, Retry, Reset, "
        "Back and Next in the same place on every card, and progress dots, one for each of the 7 cards. Only one "
        "road is shown at a time. Every target is nearer to one carrot than to the other, so no card ever puts the "
        "rabbit on the halfway milestone.",
        ["Phase 1, Recall and get ready: the rabbit stands on a short tens road between two carrots with the "
         "halfway milestone lit; the student points to the carrot that looks nearer, and then the jump counts "
         "appear to confirm it.",
         "Phase 2, Play and apply: the student picks Tens, Hundreds or Thousands, drags the rabbit to the target "
         "number, reads the jumps to the two carrots, taps the nearer carrot, and then repeats on all three roads "
         "for one number.",
         "Phase 3, Challenge: the book's rabbit at 2,346 on the tens, hundreds and thousands roads with its "
         "blanks to fill, then the book's table of nearest tens, hundreds and thousands for 3,176, 4,017, 5,789 "
         "and 8,203."],
        ["Play card 1, nearest ten: the rabbit is at 7,863 and the carrots are at 7,860 and 7,870. Place the "
         "rabbit, read the jumps and choose the nearer carrot. Answer: 7,860, 3 jumps (the other carrot needs 7 "
         "jumps).",
         "Play card 2, nearest ten: the rabbit is at 3,298 and the carrots are at 3,290 and 3,300. Answer: 3,300, "
         "2 jumps (the other carrot needs 8 jumps).",
         "Play card 3, nearest hundred: the rabbit is at 4,618 and the carrots are at 4,600 and 4,700. Answer: "
         "4,600, 18 jumps (the other carrot needs 82 jumps).",
         "Play card 4, three roads for one number: the rabbit is at 8,327. Switch between the Tens, Hundreds and "
         "Thousands roads and choose the nearer carrot on each. Answer: tens 8,330 (3 jumps), hundreds 8,300 (27 "
         "jumps), thousands 8,000 (327 jumps).",
         "Play card 5, one carrot for two numbers: place the rabbit at 6,298 and then at 6,303 on the Tens road. "
         "Answer: both go to 6,300 (2 jumps and 3 jumps), so they have the same nearest ten.",
         "Challenge card 1: The rabbit is at 2,346. Its food has been kept at its neighbouring tens. On which "
         "tens should the rabbit go to get its food, with the least number of steps? Then do the same for the "
         "neighbouring hundreds and the neighbouring thousands: ___ is the nearest ten (hundred, thousand) of "
         "2,346. It will need ___ jumps to reach ___. Answer: 2,350 with 4 jumps; 2,300 with 46 jumps; 2,000 "
         "with 346 jumps.",
         "Challenge card 2: Fill in the boxes appropriately: the nearest tens, nearest hundreds and nearest "
         "thousands of 3,176, 4,017, 5,789 and 8,203. Answer: 3,176: 3,180; 3,200; 3,000. 4,017: 4,020; 4,000; "
         "4,000. 5,789: 5,790; 5,800; 6,000. 8,203: 8,200; 8,200; 8,000."],
        ["Once the rabbit is placed, the jump count appears under each carrot, for example 3 jumps and 7 jumps, and "
         "the carrot with fewer jumps starts to glow.",
         "A carrot that needs more jumps shows both counts with 'This carrot needs more jumps. Which carrot needs "
         "fewer?', and the rabbit stays so the student can try again.",
         "A rabbit placed on a different number from the one on the card slides back with 'The rabbit is at ___. "
         "The card asks for ___.'",
         "A correct choice makes the rabbit hop the jumps one by one with a gentle count, and the nearest number is "
         "written on the milestone.",
         "On the three-roads card the road changes after each correct choice and a small row keeps the nearest "
         "ten, hundred and thousand found so far, so the student can see that the nearest mark can be below or "
         "above the number.",
         "In the table, a box that is not right shows the two neighbours and the jumps to each, so the student "
         "can correct it."],
        "All 7 cards are done correctly, and the student has used the Tens, Hundreds and Thousands roads at least "
        "once.",
        ["target", "road", "rabbitPosition", "jumpsLeft", "jumpsRight", "chosenCarrot", "cardIndex", "hintLevel"],
        ["M_ROUND_UP", "M_NEAR_FAR"],
        ["Which two carrots are at the ends of the road, and which one does the rabbit look closer to?",
         "Count the jumps from the rabbit to each carrot. The carrot with fewer jumps is the nearest.",
         "To count the jumps, subtract: the number the rabbit stands on minus the left carrot, and the right carrot "
         "minus the number the rabbit stands on. Compare the two answers.",
         "For a rabbit at 6,731 on the hundreds road, the carrots are 6,700 and 6,800: 31 jumps to 6,700 and 69 "
         "jumps to 6,800, so the nearest hundred is 6,700. Now try the next card."]),
}
