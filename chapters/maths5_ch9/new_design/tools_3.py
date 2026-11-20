# -*- coding: utf-8 -*-
"""Tool spec for T6 of Class 5 Chapter 9 (Coconut Farm): Regroup and Share. Spec only; the tool page is built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds are labelled practice values. One activity at a time,
one instruction at a time, large controls, Back and Next in the same place, visible progress, Hint, Retry and Reset always
present, immediate specific feedback that is never red."""
from topics_common import T

TOOLS = {
    "regroup_and_share": T(
        "tool_regroup_and_share", "Regroup and Share", "manipulative",
        "Divide by place value with blocks: share each place equally among the plates, regroup what is left into the next "
        "place, and write the quotient with a 0 in any place that cannot be shared.",
        "The packing shed table on Susie and Sunitha's coconut farm, drawn as a warm 3D isometric scene with soft shadows and "
        "gentle animation. A tray of base ten blocks is the largest thing on screen: flat blocks for hundreds (orange), rods "
        "for tens (blue) and small cubes for ones (pink), as the book colours them. Beside the tray stand 2 to 9 empty plates, "
        "one for each equal part, and a remainder tray. An instruction strip at the top shows one sentence in large type, "
        "with progress dots under it. A strip under the plates has the columns thousands, hundreds, tens and ones for the "
        "quotient digits, and the long-division record of the book fills in beside it step by step. Controls: press Share "
        "for a place to deal that place's blocks to the plates one by one; press Regroup to break one hundred into 10 tens "
        "or one ten into 10 ones; drag a block to a plate or to the remainder tray; type a digit into the strip; Check, "
        "Hint, Retry (restores the blocks of this card), Reset (clears the table), Back and Next in the same places on every "
        "card. Read-outs: the dividend, the divisor, the blocks left in each place, the quotient digits so far, and a card "
        "number out of 7.",
        ["The table shows 83 candies as 8 tens and 3 ones and 6 plates (practice values). "
         "Say if the 8 tens can be shared among 6 plates without breaking a ten. Then press Next.",
         "Share the blocks of each place among the plates, regroup what is left into the next "
         "place, write 0 where a place cannot be shared, and predict how many digits the quotient will have.",
         "Solve the book's four divisions by place value, 62 ÷ 5, 75 ÷ 8, 324 ÷ 3 and 136 ÷ 6, and "
         "answer the book's question about the number of digits of the quotient."],
        ["Card 1 (practice values): 94 ÷ 4. Answer: 9 tens shared among 4 plates gives 2 tens each and 1 ten left; "
         "regroup it into 10 ones, with the 4 ones that is 14 ones; 14 ones shared among 4 gives 3 ones each, because 4 × 3 "
         "= 12, and 2 left. Quotient 23, remainder 2, and 94 = 4 × 23 + 2.",
         "Card 2 (practice values): 57 ÷ 9. Answer: 5 tens cannot be shared among 9 plates, so write 0 tens; "
         "regroup into 57 ones; 57 ones shared among 9 gives 6 ones each, because 9 × 6 = 54, and 3 left. Quotient 6, "
         "remainder 3, and 57 = 9 × 6 + 3.",
         "Card 3 (practice values): 245 ÷ 5. Answer: 2 hundreds cannot be shared among 5 plates, so write 0 hundreds; "
         "regroup into 24 tens; 24 tens shared among 5 gives 4 tens each, because 5 × 4 = 20, and 4 tens left; regroup "
         "into 40 ones, with the 5 ones that is 45 ones; 45 ones shared among 5 gives 9 each. Quotient 49.",
         "Card 4 (practice values): 618 ÷ 6. Answer: 6 hundreds shared among 6 plates gives 1 hundred each; 1 ten "
         "cannot be shared among 6, so write 0 tens; regroup it into 10 ones, with the 8 ones that is 18 ones; 18 ones "
         "shared among 6 gives 3 each. Quotient 103.",
         "Card 5 (practice values): predict the number of digits before sharing. Answer: 856 ÷ 4 has the first "
         "digit 8, which is at least 4, so the quotient has 3 digits, and it is 214; 356 ÷ 4 has the first digit 3, which "
         "is less than 4, so the quotient has 2 digits, and it is 89.",
         "Challenge: 'Sunitha's mother has 62 candies to be distributed equally among 5 children. How many candies "
         "would each child get?' and '75 ÷ 8: Divide 75 into 8 equal parts. Can we divide this into 8 equal parts without "
         "breaking them? What can we do?' Answer: 62 ÷ 5: each child gets 12 candies and 2 are left; 75 ÷ 8: each part is "
         "9 and 3 are left, after regrouping the 7 tens into ones.",
         "Challenge: '324 ÷ 3: Divide 324 into 3 equal parts.' and '136 ÷ 6: Divide 136 into 6 equal parts.', then "
         "'Can you tell just by looking at the divisor and dividend, how many digits the quotient would have?' Answer: "
         "324 ÷ 3 = 108, with a 0 in the tens place; 136 ÷ 6: quotient 22, remainder 4. With a one-digit divisor the "
         "quotient has as many digits as the dividend if the first digit is at least the divisor, and one digit fewer if "
         "it is less. Next stop: word problems."],
        ["Pressing Share for a place deals the blocks of that place to the plates one by one and says, for example: 9 tens "
         "shared among 4 plates is 2 tens each, and 1 ten is left.",
         "When a place cannot be shared the tool says: 2 tens cannot be shared among 3 plates, so each plate gets 0 tens. "
         "Write 0.",
         "Pressing Regroup breaks one block into ten smaller blocks with a short animation and says, for example: 1 ten is "
         "10 ones.",
         "The long-division record of the book fills in beside the blocks, one line for each place, so the student sees how "
         "the blocks and the numbers match.",
         "A digit typed in the wrong place slides back with a clue such as: Which place were you sharing when you got this "
         "digit?"],
        "The student has shared and regrouped the blocks of every card, written the quotient digits with a 0 where a place "
        "could not be shared, and has solved the book's four divisions.",
        ["dividend", "divisor", "blocksPerPlace", "platesShare", "quotientDigits", "challengeIndex"],
        ["M_ZERO_SKIPPED", "M_DIGITS_SAME"],
        ["Look at the biggest place of the number. Can every plate get at least one block of that place?",
         "Share the blocks of this place. If some are left, regroup them into the next place and share again.",
         "If a place cannot be shared at all, write 0 in the quotient for that place and regroup everything into the next "
         "place.",
         "For 94 ÷ 4: share 9 tens, 2 each and 1 ten left; regroup it into 10 ones, 14 ones in all; share 14 ones, 3 each "
         "and 2 left. The answer is 23, remainder 2."]),
}
