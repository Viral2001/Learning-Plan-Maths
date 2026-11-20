# -*- coding: utf-8 -*-
"""Tool specs for T3, T4 and T5 of Class 5 Chapter 13 (Animal Jumps): Jump Together, Trail Jumper and Number Sorter.
Specs only; the tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds are labelled practice values. One activity at a
time, one instruction at a time, large controls, Back and Next in the same place, visible progress, Hint, Retry and
Reset always present, immediate specific feedback that is never red."""
from topics_common import T

TOOLS = {
    "jump_together": T(
        "tool_jump_together", "Jump Together", "manipulative",
        "Two animals jump from 0 with different jump sizes. The stones both of them land on are the common multiples "
        "of the two jump sizes, the first of them is the first common multiple, and the others are its multiples.",
        "A long line of numbered stepping stones across a jungle stream, from 0 to 60, drawn as a warm 3D isometric "
        "scene with soft shadows and gentle animation. The stone line is the largest thing on screen and sits in two "
        "rows, 0 to 30 above and 31 to 60 below, with the numbers large and clear. A Road button switches the line to "
        "the winding cobbled road of 65 stones numbered 0 to 64, with the food at its end, as in your maths book. "
        "Robby the rabbit (blue) and Deeku the deer (orange) stand on stone 0. Each has a jump dial with a plus and a "
        "minus (a jump size from 2 to 12) and a small arrow that shows one hop. A stone an animal lands on gets its "
        "mark, a blue ring for Robby and an orange diamond for Deeku, so a stone both land on shows both marks and "
        "glows gold. Under the line are three lists: Robby lands on, Deeku lands on, and Both land on. An "
        "instruction strip at the top shows one sentence in large type, with progress dots under it. Controls: the "
        "two jump dials; Jump (one hop each, so the student can follow every landing); Run (all hops to the end of the "
        "line); Lists (writes the multiples of each jump size beside the line, the second way to find the same "
        "numbers); a tap on a gold stone to mark the first common multiple; Road; Check, Hint, Retry (clears the "
        "hops), Reset (returns the jump sizes of this card), Back and Next in the same places on every card. "
        "Read-outs: the two jump sizes, the three lists, the first common multiple, and a card number out of 6.",
        ["Look at Robby and Deeku from the video, each jumping from 0 with their own "
         "jump size. Set the two jump sizes you are given and press Jump once to see where each lands.",
         "Press Jump or Run, watch where each animal lands, tap the gold stones that both land "
         "on, open the lists to see the same numbers written down, and notice the first common multiple and how far "
         "apart the gold stones are (practice values).",
         "Use the stones for the book's own questions: more common multiples of 3 and 4, a few "
         "more for 4 and 6, five common multiples of nine pairs of numbers, and Robby and Deeku on the cobbled road "
         "to the food."],
        ["Card 1 (practice values): Robby jumps 2 and Deeku jumps 3. Press Run to 30 and tap the gold stones. "
         "Answer: both land on 6, 12, 18, 24 and 30. The first common multiple is 6, because 2 × 3 = 6.",
         "Card 2 (practice values): Robby jumps 5 and Deeku jumps 10. Press Run to 60. Answer: both land on "
         "10, 20, 30, 40, 50 and 60, exactly the stones Deeku lands on, because 10 is a multiple of 5. The first common "
         "multiple is 10.",
         "Card 3 (practice values): Robby jumps 4 and Deeku jumps 10. Press Run to 60. Answer: both land on "
         "20, 40 and 60. The first common multiple is 20, and each gold stone is 20 after the one before.",
         "Card 4 (practice values): Robby jumps 6 and Deeku jumps 9. Say the first common multiple before you "
         "run, then check it by pressing Run. Answer: 18, because 6 × 3 = 18 and 9 × 2 = 18. The gold stones are 18, 36 "
         "and 54.",
         "Challenge: '12 is the first common multiple of 3 and 4. What are some other common multiples of 3 "
         "and 4? You can continue the number line or take help from the times tables of 3 and 4.' Then: 'Let us write "
         "the multiples of two numbers, 4 and 6. Multiples of 4: 4, 8, 12, 16, ... Multiples of 6: 6, 12, 18, ... 12 "
         "and 24 are two of the common multiples of 4 and 6. List a few more.' Then: 'Find 5 common multiples of the "
         "following pairs of numbers.' (a) 2 and 3 (b) 5 and 8 (c) 2 and 4 (d) 3 and 9 (e) 5 and 10 (f) 9 and 12 (g) 8 "
         "and 12 (h) 6 and 8 (i) 6 and 9. Answer: 3 and 4: 24, 36, 48, 60. 4 and 6: 36, 48, 60, 72. The first common "
         "multiples of the nine pairs are 6, 40, 4, 9, 10, 36, 24, 24 and 18, and the other four come by adding the "
         "first one again each time. Your answers may differ.",
         "Challenge: 'Food is available at the end of a cobbled road. Robby, the rabbit, takes a jump of 4 "
         "each time. Deeku, the deer, takes a jump of 6 each time. They both start at 0. Will both Robby and Deeku "
         "reach the food? Who will reach first? How do you know? Explain your answer.' Press Road, set the jumps and "
         "press Run. Answer: no, only Robby reaches the food, at stone 64: 64 = 4 × 16, but Deeku lands on 60 and then "
         "66, because 6 × 10 = 60 and 6 × 11 = 66. Robby is first. Both land together on 12, 24, 36, 48 and 60."],
        ["Each hop lands with a mark and the tool says where, for example: Robby lands on 8, the 2nd multiple of 4. A "
         "stone both land on glows gold and the tool says: Both land on 12. It is a common multiple of 3 and 4.",
         "When the student taps a gold stone as the first common multiple, the tool checks that no gold stone comes "
         "before it, and says, for example: 12 is the first stone both land on.",
         "A tap on a stone only one animal lands on shows a soft amber note: Only Robby lands here. Deeku jumps from 6 "
         "to 12 and skips 10.",
         "Lists writes the multiples of each jump size beside the line and rings the numbers that are in both lists, "
         "so the two ways show the same numbers.",
         "On the Road, an animal that jumps past the end of the road shows its last landing and the next one, for "
         "example: Deeku lands on 60 and then on 66, past the end."],
        "The student has found the gold stones for each practice pair, named the first common multiple, answered the "
        "book's questions on 3 and 4, 4 and 6 and the nine pairs, and decided who reaches the food on the road.",
        ["jumpSizeRobby", "jumpSizeDeeku", "landings", "goldStones", "roadMode", "challengeIndex"],
        ["M_CM_ONLY_PRODUCT", "M_FIRST_ONLY", "M_CF_CM_MIX"],
        ["What does each animal do? Each jumps the same number of steps every time from 0. Which stones does it land "
         "on?",
         "Find the stones where both animals land. Run the hops, or write the multiples of both jump sizes and look "
         "for the numbers in both lists.",
         "Robby jumps 3 and Deeku jumps 4. List 3, 6, 9, 12, 15, ... and 4, 8, 12, 16, ... Which numbers are in both "
         "lists?",
         "Both lists have 12, then 24, then 36. 12 is the first common multiple of 3 and 4, and each next one is 12 "
         "more. Now try your own pair the same way."]),

    "trail_jumper": T(
        "tool_trail_jumper", "Trail Jumper", "manipulative",
        "Pick a jump size and see which places on Mowgli's trail the jumps land on: a jump size lands on a number when "
        "it is a factor of the number, and a jump size that lands on every number of a list is a common factor of the "
        "list.",
        "Mowgli's winding jungle trail of 61 numbered stones from 0 to 60, drawn as a warm 3D isometric scene with soft "
        "shadows and gentle animation. The trail is the largest thing on screen. Mowgli sits on stone 0. The friends "
        "from your maths book live beside their stones: the ant at 4, the spider at 9, the frog at 12, the bird at 14, "
        "Kaa the snake at 21, Sher Khan the tiger at 25, Baloo the bear at 30, Akela the wolf at 35, the deer at 39, "
        "the rabbit at 50 and the monkey at 57. An instruction strip at the top shows one sentence in large type, with "
        "progress dots under it. A jump size dial with a plus and a minus (1 to 30) sets Mowgli's jump. Controls: Go "
        "(Mowgli hops from 0, leaving a footprint on every stone he lands on; a friend he lands on lights up with a "
        "name tag); Pick numbers (tap two or more stones, or type numbers, as targets; the tool then tries the jump "
        "size and marks each target with a green tick if Mowgli lands on it, or a soft amber skipped with the two "
        "stones he lands on either side); Clear targets; a common factors board that collects, as chips in order, "
        "every jump size the student has tried that lands on all the targets; Check, Hint, Retry (clears the "
        "footprints and the targets), Reset (returns the trail), Back and Next in the same places on every card. "
        "Read-outs: the jump size, the numbers landed on, the friends met, the common factors board, and a card number "
        "out of 6.",
        ["Look at Mowgli's jumps from the video, landing on 4, 8, 12 and so on. Set a "
         "jump size on the dial and press Go to see where he lands.",
         "Try jump sizes on the trail and read which friends he meets; pick numbers of your "
         "own and find the jump sizes that reach all of them; collect those jump sizes on the common factors board "
         "(practice values for the picked numbers).",
         "Use the trail for the book's own questions: Mowgli jumps by 2, 3, 5 and 10 steps; the "
         "common factors of 24 and 36; of 12 and 13; the numbers reached by jumps of 4; and the common factors of "
         "nine pairs of numbers."],
        ["Card 1 (practice values): Mowgli jumps 6. Press Go. Which friends does he meet? Answer: the frog (12) "
         "and Baloo (30), because 12 = 6 × 2 and 30 = 6 × 5. He jumps over the others.",
         "Card 2 (practice values): Mowgli jumps 7. Which friends does he meet? Answer: the bird (14), Kaa "
         "(21) and Akela (35), because 14 = 7 × 2, 21 = 7 × 3 and 35 = 7 × 5.",
         "Card 3 (practice values): pick the numbers 20 and 30 and find every jump size that reaches both. "
         "Answer: 1, 2, 5 and 10. A jump of 4 reaches 20 but skips 30 (it lands on 28 and then 32). A jump of 3 reaches "
         "30 but skips 20 (it lands on 18 and then 21).",
         "Card 4 (practice values): pick the numbers 15 and 16. Try every jump size from 2 to 16. Answer: none "
         "of them reaches both. Only a jump of 1 reaches both, so the only common factor of 15 and 16 is 1.",
         "Challenge: 'Which of his friends will he be able to visit, if he jumps by 2 steps starting from 0?' "
         "Then: 'Which of his friends will he be able to meet if he jumps by 3 steps?' 'Which numbers will he touch if "
         "he jumps by 5 steps?' 'Which numbers will he touch if he jumps by 10 steps?' Answer: jumps of 2 meet the ant "
         "(4), frog (12), bird (14), Baloo (30) and rabbit (50). Jumps of 3 meet the spider (9), frog (12), Kaa (21), "
         "Baloo (30), deer (39) and monkey (57). Jumps of 5 touch 5, 10, ..., 60 and meet Sher Khan (25), Baloo (30), "
         "Akela (35) and the rabbit (50). Jumps of 10 touch 10, 20, 30, 40, 50 and 60 and meet Baloo (30) and the rabbit "
         "(50).",
         "Challenge: 'Let us find some common factors of the numbers 24 and 36. Note that all jumps in the "
         "following questions start from 0.' Parts (a) to (f) as in your maths book. Then: 'What are the common factors "
         "of 12 and 13?', 'Find which of the following numbers can be reached by jumps of 4 steps?' (0, 10, 16, 27, 36, "
         "48) and 'Find the common factors of the following pairs of numbers.' (a) 12 and 16 (b) 8 and 12 (c) 4 and 16 "
         "(d) 2 and 9 (e) 3 and 5 (f) 12 and 15 (g) 20 and 5 (h) 9 and 21 (i) 6 and 27. Answer: for 24 and 36, jumps of "
         "2, 3 and 4 reach both, the other jumps are 1, 6 and 12, and the six common factors are 1, 2, 3, 4, 6 and 12. "
         "12 and 13 have only 1. Jumps of 4 reach 16, 36 and 48. The pairs have the common factors 1, 2, 4; 1, 2, 4; "
         "1, 2, 4; 1; 1; 1, 3; 1, 5; 1, 3; and 1, 3."],
        ["Go makes Mowgli hop and the tool says where he lands, for example: He lands on 12, 4 jumps of 3. A friend "
         "he lands on lights up with a name tag.",
         "A picked number that Mowgli lands on gets a green tick and the tool says, for example: 30 = 5 × 6, so a jump "
         "of 5 lands on 30.",
         "A picked number that he skips gets a soft amber note, for example: 4 does not land on 30. He lands on 28 and "
         "then on 32.",
         "The common factors board keeps each jump size that reaches all the picked numbers. The tool does not fill it "
         "for the student; it only says how many more may be hidden, for example: There are 2 more jump sizes.",
         "For two numbers with only one common jump size the tool says: Only a jump of 1 reaches both. A jump of 1 "
         "lands on every number."],
        "The student has tried jump sizes on the trail for each practice card, collected the common factors of the "
        "picked numbers, and answered the book's questions on the friends, on 24 and 36, on 12 and 13, on the jumps of "
        "4 and on the nine pairs.",
        ["jumpSize", "landings", "friendsMet", "targets", "commonFactorsBoard", "challengeIndex"],
        ["M_JUMP_NEAR", "M_CF_BIGGEST_ONLY", "M_CF_CM_MIX"],
        ["What does a jump of this size do? Mowgli lands on the same number of steps every time from 0. Which stones "
         "does he land on?",
         "To reach a number, a whole number of jumps must make it exactly. Is the number in the list of landings, or "
         "does he skip it?",
         "For 24 and 36, try jump sizes 2, 3 and 4. Does each of them land on 24, and does each land on 36?",
         "2 lands on 24 (2 × 12) and on 36 (2 × 18). 3 lands on both (3 × 8 and 3 × 12). 4 lands on both (4 × 6 and "
         "4 × 9). So 2, 3 and 4 are common factors. Now try 6 and 12, then 1."]),

    "number_sorter": T(
        "tool_number_sorter", "Number Sorter", "manipulative",
        "Sort numbers into three overlapping circles by whether 2, 5 and 10 are factors of them, and find that no "
        "number goes in the circle for 10 only, because a number divisible by 10 is divisible by 2 and by 5.",
        "A jungle pond clearing with three overlapping circles of floating lily rings, drawn as a warm 3D isometric "
        "scene with soft shadows and gentle animation: a pink circle labelled divisible only by 2, a purple circle "
        "labelled divisible only by 5 and a blue circle labelled divisible only by 10, with the middle where all three "
        "meet labelled divisible by 2, 5 and 10. The circles are the largest thing on screen. Number cards, "
        "green leaf-shaped tags like the ones in your maths book, wait in a row along the bottom. A jump tester beside "
        "the circles has three small lights labelled 2, 5 and 10: when a card is picked up, each light turns green if "
        "a jump of that size lands exactly on the number and stays amber if it skips it, and the tool writes one line "
        "such as 45 ÷ 5 = 9, exactly. An instruction strip at the top shows one sentence in large type, with progress "
        "dots under it. Controls: drag a card into a circle or into the middle; tap a card to run the jump tester; "
        "Check, Hint, Retry (returns the cards of this card), Reset, Back and Next in the same places on every card. A "
        "card dropped in the wrong place slides back with a clue. Read-outs: how many cards are in each region, the "
        "three lights, and a card number out of 5.",
        ["Remember from the video that a number is divisible by 2, 5 or 10 when that "
         "number is one of its factors. Tap a card and read the three lights.",
         "Test cards with the jump tester and drop each one in the right circle; then try to "
         "find a card for the circle for 10 only (practice values).",
         "Sort the book's fifteen number cards into numbers divisible by 2 only, by 5 only, by 10 "
         "only and by 2, 5 and 10."],
        ["Card 1 (practice values): sort the cards 14, 15 and 20. Answer: 14 is divisible by 2 only, because 14 ÷ 2 = "
         "7. 15 is divisible by 5 only, because 15 ÷ 5 = 3. 20 is divisible by 2, 5 and 10, because 20 ÷ 2 = 10, 20 ÷ 5 = 4 and "
         "20 ÷ 10 = 2.",
         "Card 2 (practice values): sort the cards 12, 25, 40, 18, 65 and 100. Answer: 12 and 18 are divisible "
         "by 2 only, 25 and 65 are divisible by 5 only, and 40 and 100 are divisible by 2, 5 and 10.",
         "Card 3 (practice values): find three numbers up to 60 that go in the middle. Answer: any three of "
         "10, 20, 30, 40, 50 and 60. Each is a multiple of 10.",
         "Card 4 (practice values): try to find a card for the circle for 10 only. Test 10, 20, 30 and 40. "
         "Answer: there is none. Each of them is divisible by 10 and also by 2 and by 5, so it goes in the middle. "
         "10 = 2 × 5.",
         "Challenge: 'Sort the following numbers into those that are (a) divisible by 2 only (b) divisible by "
         "5 only (c) divisible by 10 only (d) divisible by 2, 5, and 10.' The cards are 90, 22, 38, 30, 75, 45, 66, 78, "
         "62, 40, 84, 56, 25, 95 and 55. Answer: (a) 22, 38, 66, 78, 62, 84, 56; (b) 75, 45, 25, 95, 55; (c) none; (d) "
         "90, 30, 40."],
        ["Tapping a card runs the jump tester: each light turns green if a jump of that size lands exactly, and the "
         "tool writes one line such as 90 ÷ 10 = 9, exactly.",
         "A card dropped in the wrong region slides back with a clue, for example: 45 is divisible by 5, but a jump of "
         "2 skips it (44 then 46). Check the lights.",
         "A card dropped in the circle for 10 only slides back with: A number divisible by 10 is also divisible by 2 "
         "and by 5, because 10 = 2 × 5. It goes in the middle.",
         "A card in the right region locks in with a soft chime and the count of that region goes up.",
         "When every card is placed the tool says how many are in each region, for example: 7 in 2 only, 5 in 5 only, "
         "3 in the middle and none in 10 only."],
        "The student has sorted every practice card and all fifteen of the book's cards, and found that the circle for "
        "10 only stays empty.",
        ["cards", "regionOfCard", "jumpLights", "challengeIndex"],
        ["M_TEN_ONLY", "M_FACTOR_MULTIPLE"],
        ["What does divisible by 2 mean? A number is divisible by 2 when 2 divides it exactly. Does it also divide by "
         "5 or by 10?",
         "Tap the card and read the three lights. Green means that jump size lands on the number exactly.",
         "For 45, check 2, then 5, then 10. Which lights turn green?",
         "45 ÷ 5 = 9, exactly, so the 5 light is green. 45 ÷ 2 and 45 ÷ 10 are not exact, so those lights stay amber. "
         "So 45 goes in the circle for 5 only. Now try the next card."]),
}
