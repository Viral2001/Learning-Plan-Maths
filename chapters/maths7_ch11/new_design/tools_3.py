# -*- coding: utf-8 -*-
"""Tool specs for modules M3 and M4 (patterns, procedures, applications, review, puzzle)."""
from topics_common import T

TOOLS = {
    "pattern_explorer": T(
        "tool_pattern_explorer", "Pattern Explorer", "simulation",
        "Pairs of a chosen type, such as consecutive, even, odd, multiple or co-prime, show the same HCF or LCM "
        "behaviour again and again; a general statement is a claim that survives many examples.",
        "A pair-type picker; a generator that makes pairs of that type; a table with columns for the two numbers, HCF, "
        "LCM and product; a claim box for the student's general statement.",
        ["Pick a pair type and generate several pairs.",
         "Fill the table with HCF and LCM for each pair.",
         "Look for what stays the same and write a general statement.",
         "Test the statement on new pairs, including one that tries to break it."],
        ["Consecutive even numbers (HCF 2).", "Consecutive odd numbers (HCF 1).", "Consecutive numbers (HCF 1).",
         "Co-prime pairs (HCF 1, LCM the product).", "One number a factor of the other (HCF the smaller, LCM the "
         "larger).", "Two multiples of 3 (LCM a multiple of 3)."],
        ["A statement that fails for a generated pair is answered with that counter-example.",
         "A statement true for every pair shown is accepted, and the tool asks for a reason using common factors.",
         "A reason that mentions the difference of the numbers or the shared primes is marked as complete."],
        "All six pair types are done with a true statement for each.",
        ["pairType", "pairs", "hcfs", "lcms", "claim", "cardIndex"],
        ["M_COPRIME_ONE_FACTOR", "M_LCM_PRODUCT"],
        ["Try three or four pairs of this type. What do their HCFs look like?",
         "Write the HCF and LCM for each pair and compare the columns.",
         "Ask what a common factor of both numbers must also divide, for example their difference.",
         "The pairs are listed, the repeating value is highlighted and the statement is written with a reason; a new "
         "type follows."]),

    "common_multiplier": T(
        "tool_common_multiplier", "Common Multiplier Lab", "simulation",
        "When both numbers are multiplied by the same number, the HCF is multiplied by it too; the HCF equals that "
        "multiplier only when the remaining factors are co-prime.",
        "A base pair of numbers; a multiplier slider; the scaled pair with prime factorisations; an HCF readout for the "
        "base pair and the scaled pair; a co-prime indicator for the remaining factors.",
        ["Choose a base pair and a multiplier.",
         "Read the HCF of the base pair and of the scaled pair and compare them.",
         "Check whether the remaining factors are co-prime and see if the HCF equals the multiplier.",
         "Predict the HCF before pressing Show."],
        ["Double 270 and 50 (HCF 10 to 20).", "14 × 6 and 14 × 9 (HCF 42).", "18 × 10 and 18 × 15 (HCF 90).",
         "10 × 38 and 10 × 21 (HCF 10).", "5 × 13 and 5 × 20 (HCF 5).", "12 × 16 and 12 × 20 (HCF 48)."],
        ["A prediction that equals the multiplier is checked against the HCF of the remaining factors.",
         "When the remaining factors are co-prime the tool confirms the HCF equals the multiplier.",
         "When they are not, the extra common factor is shown and multiplied in."],
        "All six cards are done with the HCF correct and the co-prime check correct.",
        ["basePair", "multiplier", "scaledPair", "hcfBase", "hcfScaled", "coprime", "cardIndex"],
        ["M_COPRIME_ONE_FACTOR", "M_HCF_BIG"],
        ["Write both numbers as the multiplier times another number.",
         "Find the HCF of the two other numbers.",
         "The HCF is the multiplier times the HCF of the other two numbers.",
         "The other two numbers' HCF is found and multiplied by the multiplier; it equals the multiplier only when "
         "that HCF is 1."]),

    "division_ladder": T(
        "tool_division_ladder", "Division Ladder", "manipulative",
        "Dividing both numbers by any common factor, row after row, until the two numbers are co-prime gives the HCF "
        "as the product of the divisors and the LCM as the divisors times the last row.",
        "Two numbers at the top; a ladder of rows; a divisor box beside each row; the two quotients written in the next "
        "row; a co-prime check; HCF and LCM slots that fill from the ladder.",
        ["Enter any common divisor for the current row.",
         "Check the two quotients that fill the next row.",
         "Stop when the last two numbers are co-prime.",
         "Multiply the divisors for the HCF, then the divisors with the last row for the LCM."],
        ["84 and 180 (HCF 12, LCM 1260).", "300 and 150 (HCF 150, LCM 300).", "630 and 770 (HCF 70, LCM 6930).",
         "90 and 150 (HCF 30, LCM 450).", "84 and 132 (HCF 12, LCM 924).", "56 and 84 (HCF 28, LCM 168)."],
        ["A divisor that does not divide both numbers is rejected with the failed division shown.",
         "Stopping while the last row still shares a factor is flagged with that factor.",
         "Giving only the last row as the answer is flagged: the answer is the product of the divisors."],
        "All six pairs are done with the ladder, HCF and LCM correct.",
        ["numA", "numB", "rows", "divisors", "lastRow", "hcf", "lcm", "cardIndex"],
        ["M_PROCEDURE"],
        ["Which number divides both of these exactly?",
         "Divide both by a common factor and look at the new row. Do they still share a factor?",
         "Keep going until the last two numbers share nothing, then multiply the divisors for the HCF.",
         "The divisors are multiplied for the HCF and then with the last row for the LCM; a new pair follows."]),

    "product_checker": T(
        "tool_product_checker", "Product Checker", "simulation",
        "For two numbers the HCF times the LCM equals the product, because each prime's smaller count goes to the HCF "
        "and larger count to the LCM; for three numbers this fails.",
        "Two number cards; a prime split showing which copies go to the HCF and which to the LCM; a balance comparing "
        "HCF × LCM with the product; a switch to three numbers.",
        ["Enter or pick two numbers and find their HCF and LCM.",
         "Compare HCF × LCM with the product on the balance.",
         "Use the rule to find a missing value from the other three.",
         "Switch to three numbers and test whether the balance still holds."],
        ["105 and 95 (HCF 5, LCM 1995, product 9975).", "45 and 105 (HCF 15, LCM 315).",
         "275 and 352 (HCF 11, LCM 8800).", "222 and 370 (HCF 74, LCM 1110).",
         "Missing LCM: HCF 6, numbers 12 and 18 (LCM 36).", "Three numbers 4, 6, 10 (120 against 240)."],
        ["A balance that tips shows which side is larger and by how much.",
         "A missing value is checked by multiplying back and comparing with the product.",
         "For three numbers the tool shows the middle prime counts that the minimum and maximum leave out."],
        "All six cards are done with the balance and the missing value correct.",
        ["numA", "numB", "hcf", "lcm", "product", "mode", "cardIndex"],
        ["M_LCM_PRODUCT", "M_PROCEDURE"],
        ["Find the prime factorisation of each number first.",
         "Write the HCF and the LCM and multiply them.",
         "Compare the result with the product of the two numbers.",
         "The HCF and the LCM are multiplied and set beside the product; for three numbers the two sides differ."]),

    "hcf_or_lcm": T(
        "tool_hcf_or_lcm", "HCF or LCM Decider", "simulation",
        "A story that splits things into equal parts asks for the HCF, and a story where repeating events line up asks "
        "for the LCM; once chosen, the value is computed from prime factorisations.",
        "A story card; two big buttons HCF and LCM; a prime factorisation workspace; an answer box; a story check that "
        "reads the answer back in context.",
        ["Read the story and decide whether it asks for the HCF or the LCM.",
         "Factorise the numbers and compute the chosen value.",
         "Type the answer and read it back in the story.",
         "Ask for a hint if stuck."],
        ["Blue stars in two repeating rows (16th star).", "Prime factor forms: multiple or factor (No, No).",
         "HCF and LCM in prime form (21 and 97020).", "HCF 1 and LCM 66 (for example 6 and 11).",
         "Cows through 3, 5 and 7 gates under 200 (105 cows).", "Cubes in a 12 by 18 by 36 box (6, 3, 2 cm)."],
        ["Choosing the wrong one explains the cue in the story, for example equal parts or meeting again.",
         "An answer that is correct but not in the story's unit is asked to be restated with the unit.",
         "A correct answer is checked by substituting back into the story."],
        "All six stories are done with the right choice and value.",
        ["storyIndex", "choice", "factorisations", "answer", "cardIndex"],
        ["M_HCF_BIG", "M_LCM_PRODUCT"],
        ["Is the story cutting into equal parts, or waiting for things to line up?",
         "Equal parts means HCF, and lining up means LCM. Pick one.",
         "Write the prime factorisations and take minimum or maximum counts.",
         "The choice is named, the value is computed from the primes and read back in the story; a new story follows."]),

    "lcm_applier": T(
        "tool_lcm_applier", "Remainders, Chases and Fractions", "simulation",
        "Divisibility by several numbers is a multiple of their LCM, a chase is solved by the gain per leap, and an LCM "
        "denominator makes fractions easy to add.",
        "A problem card with a working area; for remainder problems a list of multiples of the LCM with remainders "
        "filled in; for chases a number line with two runners; for fractions a bar model over the LCM.",
        ["Read the problem and decide which idea it uses.",
         "Work through the LCM list, the leap gain or the common denominator.",
         "Type the answer and check it in the story."],
        ["Divisible by 3, 4, 5, 7 and remainder 10 by 11 (2100).", "Fire in the Mountain options (72 and 36).",
         "LCM of two primes (greater than both).", "Dog and rabbit with 150 ft head start (75 leaps).",
         "Smallest multiple of 1 to 10 except 7 (360).", "Mahaviracharya's fraction sum (1)."],
        ["A multiple of the LCM that fails the remainder test is shown with its actual remainder.",
         "A leap count is checked by the distances travelled by both animals.",
         "A fraction sum is checked by rewriting every fraction over the LCM."],
        "All six problems are done with the answer correct and checked.",
        ["problemIndex", "lcm", "multiples", "gain", "answer", "cardIndex"],
        ["M_LCM_PRODUCT", "M_LCM_BIG"],
        ["What repeating pattern or common amount is in this problem?",
         "Find the LCM, the gain per leap or the common denominator.",
         "Test the multiples one by one, or divide the head start by the gain.",
         "The LCM or the gain is computed and the answer is checked against the story; a new problem follows."]),

    "chapter_practice": T(
        "tool_chapter_practice", "Chapter Practice", "simulation",
        "Questions from the whole chapter mix common factors, primes, HCF, LCM, patterns, the division ladder and "
        "applications, so the student must choose the idea and then the method.",
        "A question card with a progress bar; an answer area suited to each question; a hint button; a final short "
        "challenge card.",
        ["Read the question and choose the idea first.",
         "Pick a method that suits the numbers and solve.",
         "Check the answer using the product rule or by dividing.",
         "Finish with the challenge card."],
        ["Tile the 12 ft by 16 ft room: largest tile (4 ft).", "Two bells at 12 and 18 minutes (36 minutes).",
         "HCF and LCM of 42 and 70 (14 and 210).", "Tell the HCF of 7 and 21 and of 12 and 13 (7 and 1).",
         "Use the ladder on 56 and 84 (HCF 28, LCM 168).", "Challenge: check HCF × LCM for 45 and 75 (15 × 225 = "
         "3375)."],
        ["A wrong idea is explained with the cue in the story.",
         "A wrong value points to the step in the prime factorisation or ladder where it went off.",
         "A correct answer is confirmed with a quick check."],
        "All six questions are answered correctly and the challenge is attempted.",
        ["questionIndex", "idea", "method", "answer", "attempts"],
        ["M_HCF_BIG", "M_LCM_PRODUCT", "M_MIN_MAX"],
        ["Is this about splitting into equal parts or about things lining up?",
         "Pick prime factorisation or the ladder and start writing.",
         "Take minimum counts for the HCF or maximum counts for the LCM.",
         "The idea and method are named, the value is computed and checked; the next question follows."]),

    "colour_decoder": T(
        "tool_colour_decoder", "Colour Decoder", "exploration",
        "Each ring is split into arcs, one for each prime in the number's prime factorisation, so the rings can be "
        "decoded and extended by checking them against the factorisations.",
        "A grid of ring designs for the numbers 1 to 100; a zoom view of one ring; a colour legend that the student "
        "fills in by matching rings to prime factorisations; a drawing area for new rings.",
        ["Tap rings for 2, 3, 5 and 7 and note their colours.",
         "Compare rings for 4, 6, 8, 9 and 12 with their prime factorisations.",
         "Fill in the legend and test it on a new number.",
         "Colour the rings for a few numbers beyond 100."],
        ["Match the single colour rings to the primes 2, 3, 5 and 7.", "Decode 4, 6 and 9.",
         "Decode 12 and 30.", "Find which numbers have the same number of arcs as 12.",
         "Predict the ring for 64 and 81.", "Draw rings for 101 and 102."],
        ["A legend entry that does not fit a known ring is highlighted with that ring.",
         "A correct legend entry is tested automatically on another number.",
         "A drawn ring is checked against the prime factorisation of its number."],
        "The legend is filled and the rings for the new numbers are drawn correctly.",
        ["legend", "selectedNumber", "drawn", "cardIndex"],
        ["M_ORDER"],
        ["How many arcs does the ring of a prime number have?",
         "Compare a number and its prime factorisation, arc by arc.",
         "Give each prime its own colour and test it on another number.",
         "The legend is shown with each prime's colour and tested on a new number."]),
}
