# -*- coding: utf-8 -*-
"""Tool specs for Class 8 Chapter 5 (Number Play). Ten tools, each used once, only where handling the numbers is the
idea itself. Three of them (the rule bench, the combined divisibility trap and the digit puzzle solver) are carried
over from the live plan: build.py swaps their placeholder node for the live node listed in live_tools.json, so the
specs below only describe them for the plan and the worklists. The other seven (the sign flip board, the nines and
ones blocks, the pairs dot grid, the claim tester, the remainder rows, the excess and shortfall board and the digital
root dial) are new placeholders."""
from topics_common import T

TOOLS = {
    "sign_flip_board": T(
        "tool_sign_flip_board", "Sign Flip Board: Parity of Signed Sums", "manipulative",
        "Placing plus and minus signs between numbers gives many results, but switching one sign changes the result by "
        "twice that number, so every result has the same parity.",
        "A row of four number cards with a sign switch in each gap. The result and its parity show live; a history list "
        "keeps every expression tried, and a change meter shows how much the last switch moved the result.",
        ["Choose four numbers, or four consecutive numbers.",
         "Switch any sign and watch the result and the change meter.",
         "Predict the parity before revealing the result.",
         "Fill the tree of all eight expressions."],
        ["For 3, 4, 5, 6 list all eight expressions and their results.",
         "Switch +4 to −4 in 3 + 4 − 5 − 6: predict the change, then check.",
         "Choose four consecutive numbers of your own: which three results always appear?",
         "Choose 2, 7, 4, 9: will any expression be even?",
         "Add a fifth card: does every result still share one parity?",
         "Find four numbers whose eight results are all odd."],
        ["A wrong parity prediction shows the change meter: twice the switched number.",
         "A tree with a missing branch is highlighted until all eight expressions are listed.",
         "Each result is checked against the parity of the all plus sum."],
        "All six cards are done with each parity predicted before the reveal.",
        ["cards", "signs", "history", "prediction", "cardIndex"],
        ["M_SIGN_PARITY", "M_NEG_NOT_EVEN"],
        ["What happens to the result when one sign switches?",
         "Compare the result before and after a switch: how far apart are they?",
         "Switching +b to −b takes b away twice, so the result moves by 2b.",
         "The change is shown as twice the number, the parity is matched, and a new card follows."]),

    "divisibility_rule_bench": T(
        "tool_divisibility_rule_bench", "Divisibility Rule Bench", "manipulative",
        "A number is a sum of place values. Every place value from tens upward is a multiple of 10 and 2 and 5, from "
        "hundreds upward a multiple of 4, from thousands upward a multiple of 8, so only the last one, two or three "
        "digits decide divisibility by these numbers.",
        "A number split into place value blocks. Choosing a divisor shades the blocks that are already multiples of it "
        "and leaves only the digits that decide divisibility.",
        ["Type a number and choose a divisor: 2, 4, 5, 8 or 10.",
         "See which place values are shaded as multiples of the divisor.",
         "Test only the unshaded digits and predict the answer.",
         "Check the prediction by dividing."],
        ["4075: which digits decide divisibility by 10 and by 5?",
         "3716: decide divisibility by 2 and by 4.",
         "51240: is it divisible by 8? Which digits do you need?",
         "Why is 100 a multiple of 4 but 10 is not?",
         "Make a five digit number divisible by 8 but not by 16.",
         "Explain why the shortcut for 4 looks at two digits."],
        ["A prediction based on the wrong digits shows the unshaded blocks again.",
         "Each place value block states which divisors it is a multiple of.",
         "The division is shown after each prediction."],
        "All six cards are done with each prediction explained by place value.",
        ["number", "divisor", "shadedPlaces", "prediction", "cardIndex"],
        ["M_LAST_DIGIT_9"],
        ["Which place values are multiples of the divisor?",
         "Write the number as a sum of place values.",
         "For 4, every place from hundreds upward is a multiple of 4, so test the last two digits.",
         "The deciding digits are highlighted with their division, and a new card follows."]),

    "nines_blocks": T(
        "tool_nines_blocks", "Nines and Ones: Remainders by 9", "manipulative",
        "Each place value is a block of nines plus one: 10 is 9 + 1, 100 is 99 + 1, 1000 is 999 + 1. The nines divide "
        "exactly by 9, so the ones left over, one for each unit of each digit, add up to the digit sum and give the "
        "remainder on division by 9 or 3.",
        "A number shown as place value blocks. Splitting a block separates its nines from its single one; the loose "
        "ones gather in a tray where groups of nine can be removed until the remainder is left.",
        ["Type a number and split each block into nines and ones.",
         "Gather the loose ones in the tray and remove groups of nine.",
         "Read the remainder and compare it with the digit sum.",
         "Switch the divisor to 3 and repeat."],
        ["427: split the blocks and find the remainder on division by 9.",
         "7309: how many loose ones are there, and what is left after removing nines?",
         "99009: why are there no loose ones left?",
         "Make a number with remainder 5 on division by 9.",
         "Is 123456 divisible by 3? Use the tray.",
         "Why is 109 not divisible by 9 even though it ends in 9?"],
        ["A wrong remainder shows the tray with the groups of nine still to remove.",
         "Each split block shows its nines and its one.",
         "The digit sum is shown next to the tray after each card."],
        "All six cards are done with each remainder found from the tray.",
        ["number", "splitBlocks", "trayOnes", "divisor", "cardIndex"],
        ["M_LAST_DIGIT_9"],
        ["What is left over when 10 or 100 is divided by 9?",
         "Split each block: how many loose ones does each digit give?",
         "The loose ones add up to the digit sum; take away nines from that.",
         "The remainder is shown from the tray, and a new card follows."]),

    "combined_divisibility_trap": T(
        "tool_combined_divisibility_trap", "Combined Divisibility Trap", "manipulative",
        "Passing two divisibility tests shows divisibility by their product only when the two divisors share no common "
        "factor, as with 2 and 3 for 6, or 3 and 8 for 24. 12 passes the tests for 4 and 6 but is not divisible by 24.",
        "Two test gates side by side. A number passes through both gates and a third gate checks the product; a number "
        "that passes both but fails the product is caught in the trap.",
        ["Choose two divisors and a number.",
         "Run the number through both gates and the product gate.",
         "Find numbers that fall into the trap.",
         "Change the pair of divisors until no number can be trapped."],
        ["Test 38, 225, 186 and 64 for 2 and 3, then for 6.",
         "Find a number divisible by 4 and 6 but not by 24.",
         "Does testing 3 and 8 ever let a number fool the 24 gate?",
         "Which pair of tests works for 36: 4 and 9, or 6 and 6?",
         "Find a pair of tests that works for 45.",
         "Explain with prime factors why 4 and 6 fail for 24."],
        ["A trapped number shows its prime factors next to those of the product.",
         "A pair that shares a factor is flagged with the shared factor.",
         "The LCM of the two divisors is shown after each card."],
        "All six cards are done with each trap explained by common factors.",
        ["divisorA", "divisorB", "number", "trapped", "cardIndex"],
        ["M_PRODUCT_RULE"],
        ["Do the two divisors share a factor?",
         "Compare the product with the LCM of the two divisors.",
         "4 and 6 share the factor 2, so passing both only shows divisibility by 12.",
         "The trapped number is shown with its prime factors, and a new card follows."]),

    "digit_puzzle_solver": T(
        "tool_digit_puzzle_solver", "Digit Puzzle Solver", "manipulative",
        "In a cryptarithm each letter is one digit, different letters are different digits, and a leading digit is "
        "never 0. Sizes of products, units digits and carries narrow the choices until one or a few solutions remain.",
        "A cryptarithm in columns with a digit tray. Dragging a digit onto a letter fills every copy of that letter; "
        "clashes and leading zeros are flagged, and a carry row shows each column's carry.",
        ["Choose a puzzle.",
         "Drag digits onto letters, starting with the most restricted letter.",
         "Watch the carries and the clash warnings.",
         "Check the finished puzzle and look for a second solution."],
        ["A1 + 1B = B0", "AB + 37 = 6A", "PQ × 8 = RS", "GH × H = 9K", "BYE × 6 = RAY",
         "JK × 6 = KKK", "WOW × 5 = MEOW"],
        ["A clash between two letters with the same digit is flagged.",
         "A leading zero is flagged.",
         "A product with too many digits shows the size check."],
        "All seven puzzles are solved with every solution found.",
        ["puzzle", "assignments", "carries", "cardIndex"],
        ["M_CRYPT_SAME"],
        ["Which letter has the fewest possible digits?",
         "Use the size of the product or the units digit to narrow the choices.",
         "In PQ × 8 = RS the product has two digits, so PQ is at most 12.",
         "The solution is filled in with each step explained, and a new puzzle follows."]),

    "pairs_dot_grid": T(
        "tool_pairs_dot_grid", "Dot Grid: Pairs of Even Numbers", "manipulative",
        "Dots laid out in rows of four show every even number is either full rows (4p) or full rows and 2 left over "
        "(4p + 2). Two numbers join into full rows when the leftovers add up to 4, so the sum of two even numbers is a "
        "multiple of 4 only when both are the same type.",
        "A dot grid with four columns and two number stacks side by side. Each number fills rows of four and shows its "
        "leftover dots; a join button slides the second stack under the first, and a read-out shows the full rows, the "
        "leftover dots and the remainder on division by 4.",
        ["Choose two even numbers.",
         "Lay each number out in rows of four and mark its leftover dots.",
         "Predict whether the joined stack has full rows only before pressing join.",
         "Join the stacks and read the leftover dots and the remainder."],
        ["Lay out 12 and 16 and join them: how many full rows and how many leftover dots?",
         "Lay out 6 and 10: what happens to the two leftover pairs when the stacks join?",
         "Lay out 4 and 6: how many dots are left after joining?",
         "Sort 18, 22, 36 and 42 into the forms 4p and 4p + 2.",
         "Find two even numbers that add to 30: which two types are they?",
         "Join 6 and 10, then join 14 to the result: how many leftover dots are there, and what remainder does the sum leave?"],
        ["A prediction of full rows when a leftover pair remains shows the two loose dots at the bottom of the grid.",
         "Two leftover pairs that join are highlighted as they form one new full row.",
         "Each number is labelled 4p or 4p + 2 as soon as it is laid out."],
        "All six cards are done with each prediction made before the join.",
        ["firstNumber", "secondNumber", "leftoverDots", "prediction", "cardIndex"],
        ["M_EVEN_SUM_4"],
        ["How many dots are left over when each number fills rows of four?",
         "Compare the leftover dots of the two numbers: do they make a whole row together?",
         "Two leftover pairs of 2 make 4 dots, which is one more full row.",
         "The joined stack is shown with its leftover dots and remainder, and a new card follows."]),

    "claim_tester": T(
        "tool_claim_tester", "Claim Tester: Always, Sometimes or Never", "manipulative",
        "A claim about multiples is always true only when a reason covers every number, sometimes true when one number "
        "fits and another does not, and never true when no number can fit. One number that breaks a claim is enough to "
        "stop it being always true, but many numbers that fit prove nothing.",
        "A claim card at the top and a number picker below it. Each number tried is placed in a ledger as a fit or a "
        "break, and a verdict tray with three slots holds always, sometimes and never. The tray opens only after the "
        "ledger holds a reason or an example of each kind that the verdict needs.",
        ["Read the claim and choose numbers that fit its words.",
         "Place each trial in the ledger as a fit or a break.",
         "Try to break the claim before trusting it.",
         "Drop the claim into the verdict tray and state the reason."],
        ["The sum of two even numbers is a multiple of 3.",
         "The sum of a multiple of 6 and a multiple of 9 is a multiple of 3.",
         "The sum of a multiple of 6 and a multiple of 3 is a multiple of 9.",
         "If two numbers are not divisible by 6, then their sum is not divisible by 6.",
         "When you add an odd number to an even number you get a multiple of 6.",
         "A number divisible by both 6 and 4 is divisible by 24."],
        ["A verdict of always with a break in the ledger shows that number next to the claim.",
         "A verdict of sometimes with no break or no fit in the ledger asks for the missing kind of number.",
         "A verdict of never with a fit in the ledger shows that number next to the claim."],
        "All six claims are sorted with each verdict supported by the ledger.",
        ["claim", "trials", "ledger", "verdict", "cardIndex"],
        ["M_EXAMPLES_PROVE", "M_PRODUCT_RULE"],
        ["Which numbers does the claim talk about?",
         "Try small numbers first, then look for one that breaks the claim.",
         "Write the numbers as multiples, such as 6a and 9b, and look for a common factor.",
         "The verdict is shown with its fitting and breaking numbers, and a new claim follows."]),

    "remainder_rows": T(
        "tool_remainder_rows", "Remainder Rows: Sums and Conditions", "manipulative",
        "A number with remainder r on division by d is full rows of d dots and r dots left over. When numbers are "
        "added or subtracted only the leftovers matter, and a number that meets several remainder conditions at once "
        "repeats every LCM of the divisors.",
        "A dot grid with a row length that can be set from 2 to 7. A number is laid out in full rows with its leftover "
        "dots marked; two numbers can be joined or one taken from the other, and the leftover dots regroup into a new "
        "row when they reach the row length. A strip of numbers can be sieved for up to three remainder conditions.",
        ["Choose a row length and a number.",
         "Read the full rows and the leftover dots.",
         "Join or take away a second number and predict the leftover dots.",
         "Sieve a strip of numbers for two or three remainder conditions at once."],
        ["Rows of 5: 17 leaves 2 and 24 leaves 4. What remainders do 17 + 24 and 24 − 17 leave?",
         "Rows of 7: 661 leaves 3 and 4779 leaves 5. What remainders do 4779 + 661 and 4779 − 661 leave?",
         "Sieve 2 to 60 for remainder 2 on division by 3 and by 4: list the first four numbers.",
         "Join two numbers that each leave 2 on division by 6, then join a third such number: what remains?",
         "Rows of 5 with 3 left over: do the numbers match 5k + 3 or 3k + 5?",
         "Sieve 1 to 99 for remainder 1 on division by 2, 3 and 5: which number that passes is also a multiple of 7?"],
        ["A wrong prediction shows the leftover dots of both numbers joined before they regroup.",
         "Leftover dots that reach the row length are circled as they form a new full row.",
         "A sieve shows the repeat length of the numbers that pass every condition."],
        "All six cards are done with each remainder predicted before the join.",
        ["rowLength", "firstNumber", "secondNumber", "leftoverDots", "sieveConditions", "cardIndex"],
        ["M_REMAINDER_FORM"],
        ["How many dots are left over when the number fills rows of the given length?",
         "Join only the leftover dots of the two numbers and regroup them into rows.",
         "5 leftover dots and 3 leftover dots make 8 in rows of 7, which is one full row and 1 left.",
         "The leftover dots are shown regrouped with the remainder, and a new card follows."]),

    "excess_shortfall_board": T(
        "tool_excess_shortfall_board", "Excess and Shortfall Board: Remainders by 11", "manipulative",
        "Place values alternate between one more and one less than a multiple of 11, starting with 1 for the units. The "
        "digits in the one more places add to the excess, the digits in the one less places add to the shortfall, and "
        "excess minus shortfall gives the remainder on division by 11.",
        "A number in digit cells with each place marked as one more or one less. Each digit slides into an excess pan "
        "or a shortfall pan, the two totals and their difference show live, and a dial shows the remainder from 0 to "
        "10.",
        ["Type a number and read the marks on its places.",
         "Slide each digit into the excess pan or the shortfall pan.",
         "Predict the remainder from excess minus shortfall.",
         "Reveal the dial and compare the remainder with the division."],
        ["462: slide the digits and decide whether 11 divides it.",
         "481: find excess minus shortfall and the remainder on division by 11.",
         "5529: find the remainder on division by 11.",
         "90904: is the number divisible by 11, and what is the difference?",
         "320185: the difference is negative, so what is the remainder?",
         "Find the missing tens digit of 4?2 so that 11 divides it."],
        ["A digit in the wrong pan is shown with its place mark of one more or one less.",
         "A negative difference is shown on the dial as a count back from 11.",
         "The remainder is checked against the division after each card."],
        "All six cards are done with each remainder predicted before the dial is revealed.",
        ["number", "excessPan", "shortfallPan", "difference", "prediction", "cardIndex"],
        ["M_ELEVEN_SUM"],
        ["Which places are one more than a multiple of 11 and which are one less?",
         "Count the units digit as one more and alternate to the left.",
         "Add the digits in the one more places, add those in the one less places, and subtract.",
         "The pans are filled, the difference is turned into a remainder, and a new card follows."]),

    "digital_root_dial": T(
        "tool_digital_root_dial", "Digital Root Dial", "manipulative",
        "The digital root is what is left when digits are added again and again, and it equals the remainder on "
        "division by 9 with 9 in place of 0. Adding a number moves the root forward round a dial of nine places by the "
        "root of that number, and multiples of 9 do not move it.",
        "A dial with the numbers 1 to 9 round it and a pointer for the digital root. A number can be typed in and its "
        "digits folded step by step; a step button adds a chosen number, and the pointer jumps by that number's root. "
        "A trail records each stop.",
        ["Type a number and fold its digits until one digit is left.",
         "Choose a number to add and predict where the pointer lands.",
         "Step several times and read the trail.",
         "Compare the dial with the remainder on division by 9."],
        ["Fold 489710 to its digital root.",
         "Fold 4581: where does the pointer stop, and what does that say about 9?",
         "Start at 5 and add 11 five times: list the digital roots.",
         "List the digital roots of 4, 8, 12 up to 36, the multiples of 4.",
         "List the digital roots of 7, 13, 19, 25 and 31, which are one more than multiples of 6.",
         "Find the digital root of 9a + 36b + 13 for any whole numbers a and b."],
        ["A wrong landing place shows the root of the added number and the steps round the dial.",
         "A number whose digits fold to 9 is marked as a multiple of 9, not as 0.",
         "The remainder on division by 9 is shown beside the root after each card."],
        "All six cards are done with each landing place predicted before the step.",
        ["number", "pointer", "trail", "addend", "prediction", "cardIndex"],
        ["M_DIGITAL_ROOT_ZERO"],
        ["What is the digital root of the number you add?",
         "Move the pointer forward by that many places, and go back to 1 after 9.",
         "11 has digital root 2, so each addition moves the pointer 2 places round the dial.",
         "The pointer jumps and the trail is filled in, and a new card follows."]),
}
