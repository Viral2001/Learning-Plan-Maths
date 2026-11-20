# -*- coding: utf-8 -*-
"""Tool specs for T8, T9 and T10 of Class 5 Chapter 9 (Coconut Farm): Quotient Change, Equal Balance and Always, Sometimes,
Never. Specs only; the tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds are labelled practice values. One activity at a time,
one instruction at a time, large controls, Back and Next in the same place, visible progress, Hint, Retry and Reset always
present, immediate specific feedback that is never red."""
from topics_common import T

TOOLS = {
    "quotient_change": T(
        "tool_quotient_change", "Quotient Change", "manipulative",
        "Predict how the quotient changes when the dividend or the divisor is doubled or halved, or both, using a rectangle "
        "whose area is the dividend and whose sides are the divisor and the quotient, and use a known division to write "
        "related divisions.",
        "A notice board on the wall of the packing shed on Susie and Sunitha's coconut farm, drawn as a warm 3D isometric scene "
        "with soft shadows and gentle animation. A plot of coconut trees drawn as a rectangle is the largest thing on screen: "
        "its area is the dividend N, one side is the divisor D and the other side is the quotient Q, each labelled with its "
        "number. An instruction strip at the top shows one sentence in large type, with progress dots under it. Four buttons "
        "sit under the rectangle: Double the dividend, Halve the dividend, Double the divisor and Halve the divisor. Each "
        "press redraws the rectangle and shows the new division. A prediction card asks if the quotient will be more, less "
        "or the same, and a related list on the right stores each new division. Controls: tap a change button; tap more, "
        "less or the same; type the new quotient; Check, Hint, Retry (restores the start rectangle of this card), Reset "
        "(clears the related list), Back and Next in the same places on every card. Read-outs: the dividend, the divisor, "
        "the quotient and the area line N = D × Q, and a card number out of 7.",
        ["The rectangle shows 240 ÷ 12 = 20 (practice values). Say what the area is and what "
         "the two sides are. Then press Next.",
         "Change the dividend or the divisor of a known division, predict the quotient, then check "
         "it on the rectangle, and change both at once.",
         "Use the book's known division of part A to find the other divisions of part A, and then those of "
         "parts B and C."],
        ["Card 1 (practice values): double the dividend of 240 ÷ 12 = 20. Answer: 480 ÷ 12 = 40. The area doubled and "
         "one side stayed, so the quotient doubled.",
         "Card 2 (practice values): halve the dividend of 240 ÷ 12 = 20. Answer: 120 ÷ 12 = 10. The quotient is "
         "halved.",
         "Card 3 (practice values): double the divisor of 240 ÷ 12 = 20. Answer: 240 ÷ 24 = 10. The area stayed and "
         "one side doubled, so the quotient is halved.",
         "Card 4 (practice values): halve the divisor of 240 ÷ 12 = 20. Answer: 240 ÷ 6 = 40. The quotient doubles.",
         "Card 5 (practice values): double both the dividend and the divisor of 240 ÷ 12 = 20. Answer: 480 ÷ 24 = "
         "20. The quotient is the same.",
         "Challenge: 'Find the solutions for part A. Observe the relations between the quotient, divisor and "
         "dividend and use it to answer parts B and C.' Part A: 340 ÷ 34 = 10, 340 ÷ 17, 680 ÷ 17, 680 ÷ 34, 170 ÷ 17 and "
         "680 ÷ 68. Answer: 10, 20, 40, 20, 10, 10.",
         "Challenge: part B: 192 ÷ 4 = 48, 192 ÷ 8, 384 ÷ 8, 384 ÷ 4, 384 ÷ 8 and 86 ÷ 2; part C: 352 ÷ 11 = 32, 704 ÷ "
         "22, 704 ÷ 11, 352 ÷ 22 and 1,408 ÷ 44. Answer: part B 48, 24, 48, 96, 48, 43 (86 ÷ 2 is plain division, it does not "
         "follow from 192 ÷ 4); part C 32, 32, 64, 16, 32. Next stop: mathematical statements."],
        ["After a change the rectangle is redrawn and the tool says, for example: The dividend doubled and the divisor stayed, "
         "so the quotient doubled: 480 ÷ 12 = 40.",
         "A wrong prediction gets a soft amber note, for example: The divisor doubled, so each group is twice as big and there "
         "are half as many groups.",
         "When both numbers change by the same amount the tool says: Both doubled, so the quotient is the same.",
         "The related list stores each division, for example 240 ÷ 12 = 20, 480 ÷ 12 = 40, so the student can see the family.",
         "A quotient typed wrongly slides back with a clue such as: Check by multiplying the divisor and the quotient."],
        "The student has changed the dividend and the divisor of the cards, predicted and checked each quotient, and has "
        "found the related divisions of parts A, B and C.",
        ["dividend", "divisor", "quotient", "relatedList", "prediction", "challengeIndex"],
        ["M_DIVISOR_DOUBLE"],
        ["Look at the rectangle. Which number changed, the dividend or the divisor?",
         "The area is the dividend. If one side stays the same, the other side changes the same way as the area.",
         "If the divisor changes and the dividend stays, the quotient changes the other way round. If both change by the same "
         "amount, the quotient stays.",
         "For 240 ÷ 24: the divisor doubled and the dividend stayed, so the quotient is halved, 20 becomes 10."]),

    "equal_balance": T(
        "tool_equal_balance", "Equal Balance", "manipulative",
        "Find the value of both sides of an equal sign on a balance to decide if a statement is true, and complete a "
        "statement by making both sides the same.",
        "The market scale at the stall on Susie and Sunitha's coconut farm, drawn as a warm 3D isometric scene with soft "
        "shadows and gentle animation. A balance with a left pan and a right pan is the largest thing on screen. Number and "
        "operation cards make a side, for example 3 × 8 on one pan and 20 + 4 on the other, and a value read-out sits above "
        "each pan. An instruction strip at the top shows one sentence in large type, with progress dots under it. When the "
        "two values are equal the beam is level and glows green, when they differ the beam tips toward the bigger side. A "
        "blank slot on one side holds a missing number. Under the balance are two tags, True and False. Controls: drag "
        "cards to the pans; type a number into the blank slot; tap True or False; Check, Hint, Retry (clears the pans), "
        "Reset (restores the starting card), Back and Next in the same places on every card. Read-outs: the value of each "
        "side, whether the beam is level, and a card number out of 7.",
        ["The balance shows 6 × 5 on the left and 20 + 10 on the right, level (practice "
         "values). Find the value of each side. Then press Next.",
         "Put a statement on the balance, find the value of both sides, decide if it is true or "
         "false, and complete a statement by typing the missing number.",
         "Decide if the book's five statements are true or false, and complete the book's four "
         "statements so that they are true."],
        ["Card 1 (practice values): 3 × 8 and 20 + 4. Answer: both sides are 24, the beam is level, so the statement "
         "is true.",
         "Card 2 (practice values): 40 − 9 and 5 × 7. Answer: the left side is 31 and the right side is 35, the beam "
         "tips to the right, so the statement is false.",
         "Card 3 (practice values): 56 ÷ 7 and 4 × 2. Answer: both sides are 8, so the statement is true.",
         "Card 4 (practice values): complete 9 × 4 = ___ + 16. Answer: the left side is 36, so the blank is 36 − 16 "
         "= 20. Check: 20 + 16 = 36.",
         "Card 5 (practice values): complete ___ ÷ 6 = 18 ÷ 3. Answer: the right side is 6, so the blank divided by "
         "6 must be 6, and the blank is 6 × 6 = 36.",
         "Challenge: 'Find out whether the following statements are True (T) or False (F). A true sentence is one "
         "where both sides of the = sign have the same value.' The five statements put these on the left and right of the "
         "equal sign: (a) 8 × 9 and 70 + 2, (b) 20 − 6 and 7 × 3, (c) 48 ÷ 3 and 4 × 4, (d) 89 − 9 and 90 + 0, (e) 25 + 10 and "
         "45 − 10. Answer: (a) T, (b) F, (c) T, (d) F, (e) T.",
         "Challenge: 'Complete the following statements such that they are true.' (a) 7 × 6 equals a blank plus 17, "
         "(b) 87 + 6 equals a blank times 31, (c) 63 plus a blank equals 74 − 4, (d) a blank divided by 9 equals 16 ÷ 2. "
         "Answer: (a) 25, (b) 3, (c) 7, (d) 72. Next stop: always, sometimes or never true."],
        ["When the values are equal the beam levels and the tool says, for example: Both sides are 24, so the statement is "
         "true.",
         "When the values differ the beam tips and the tool says, for example: The left side is 31 and the right side is 35, "
         "so the statement is false.",
         "A blank filled with a wrong number tips the beam and says: The two sides are not the same yet. What number makes "
         "this side 36?",
         "A card dropped on the wrong pan slides back with a clue such as: Which side does this card belong to?",
         "Each side shows its value as soon as its cards are in place, so the student always sees what is being compared."],
        "The student has found the value of both sides for every card, decided if each statement is true or false, and "
        "completed the book's four statements.",
        ["leftSide", "rightSide", "blankValue", "beamState", "challengeIndex"],
        ["M_EQUAL_ANSWER"],
        ["Look at the statement. What are the two sides of the equal sign?",
         "Find the value of the left side, then find the value of the right side.",
         "If both values are the same, the statement is true. If a number is missing, make the side with the blank have the "
         "same value as the other side.",
         "For 9 × 4 = ___ + 16: the left side is 36, so the blank is 36 − 16 = 20."]),

    "always_never": T(
        "tool_always_never", "Always, Sometimes, Never", "manipulative",
        "Test a statement with number examples and decide if it is always true, sometimes true or never true, knowing that one "
        "example that fails shows it is not always true.",
        "Three baskets on the market stall at Susie and Sunitha's coconut farm, drawn as a warm 3D isometric scene with soft "
        "shadows and gentle animation. The baskets are labelled Always true, Sometimes true and Never true and are the "
        "largest things on screen. A statement card sits above them. An instruction strip at the top shows one sentence in "
        "large type, with progress dots under it. A tray of number cards, from 1 to 20, lets the student pick a number to "
        "test, and a result strip shows each test as works or does not work, with the sum or product worked out. Controls: "
        "tap a number card to test it; drag the statement card into a basket; Check, Hint, Retry (clears the tests of this "
        "card), Reset (restores the statement), Back and Next in the same places on every card. Read-outs: the numbers "
        "tested, how many work and how many fail, and a card number out of 7.",
        ["The statement is 'Adding 4 to an even number gives an even number' (practice "
         "values). Test it with three numbers and say what you see. Then press Next.",
         "Test each statement with several numbers, watch the works and does not work count, and "
         "drop the statement into the right basket.",
         "Test the book's three statements and give the examples the book asks for, then place the "
         "book's five statements in the right baskets."],
        ["Card 1 (practice values): 'Adding 2 to an even number gives an even number.' Answer: 4 + 2 = 6, 10 + 2 = "
         "12 and 16 + 2 = 18 are all even, none fails, so it is always true.",
         "Card 2 (practice values): 'Adding 1 to an even number gives an even number.' Answer: 4 + 1 = 5 and 10 + 1 = "
         "11 are odd, none works, so it is never true.",
         "Card 3 (practice values): 'Multiplying a number by 3 gives an even number.' Answer: 3 × 4 = 12 is even and "
         "3 × 5 = 15 is odd, some work and some fail, so it is sometimes true.",
         "Card 4 (practice values): 'Doubling a number gives an even number.' Answer: 2 × 3 = 6, 2 × 7 = 14 and 2 × "
         "10 = 20 are all even, none fails, so it is always true.",
         "Card 5 (practice values): 'Adding 3 to an odd number gives an even number.' Answer: 5 + 3 = 8, 7 + 3 = 10 "
         "and 9 + 3 = 12 are all even, none fails, so it is always true.",
         "Challenge: 'Think about the following statements and find examples as suggested below.' (a) 'When two odd "
         "numbers are added, the sum is even.' Find 5 examples. Can you find an example to show it can be false? (b) "
         "'Multiplying a number by 2 can give an odd number.' Give some examples. Can you find any? (c) 'Halving a number "
         "always leads to an even number.' Give 3 examples. Can you find 3 examples when this is not true? Answer: (a) "
         "always true, for example 1 + 3 = 4 and 9 + 9 = 18, no example is false; (b) never true, 2 × 3 = 6 and 2 × 5 = 10 are "
         "even; (c) sometimes true, half of 8 is 4 but half of 6 is 3.",
         "Challenge: 'Tick in the appropriate cell for the following statements.' (a) Adding 10 to a number gives a "
         "multiple of ten. (b) Changing the order of the numbers in subtraction makes no difference. (c) In multiplication, "
         "doubling one number and halving the other keeps the product the same. (d) Multiplication by an odd number gives an "
         "even number. (e) Multiplying a number by 5 leads to numbers which have 0 in the Ones place. Answer: (a) sometimes, "
         "(b) sometimes, only for two equal numbers, (c) always, (d) sometimes, (e) sometimes. Next stop: the revision of "
         "the chapter."],
        ["Each tested number is added to the result strip with its working, for example: 6 is even and 6 + 2 = 8 is even, it "
         "works.",
         "When a number fails the tool says: This one does not work. One example that fails is enough to show the statement "
         "is not always true.",
         "When all the tests work the tool asks: Can you find a number that fails? Try an odd number or a big number.",
         "A statement dropped in the wrong basket slides back with a clue such as: Did every number you tested work?",
         "The works and fail counts update after each test, so the student sees which basket fits."],
        "The student has tested every statement with several numbers, sorted the statements of the cards and the book into the "
        "right baskets, and given the examples the book asks for.",
        ["statement", "testedNumbers", "worksCount", "failCount", "baskets", "challengeIndex"],
        ["M_ONE_EXAMPLE", "M_HALF_EVEN", "M_SUB_ORDER"],
        ["Read the statement. Pick a small number and test it.",
         "Test a few more numbers, an odd number and an even number. Count how many work and how many fail.",
         "If every number works, try to find one that fails. If none works, try to find one that works.",
         "For 'Multiplying a number by 3 gives an even number': 3 × 4 = 12 works, 3 × 5 = 15 fails, so some work and some "
         "fail: sometimes true."]),
}
