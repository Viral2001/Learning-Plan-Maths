# -*- coding: utf-8 -*-
"""Tool specs for module M4 (divisibility tests and the prime puzzle)."""
from topics_common import T

TOOLS = {
    "digit_lens": T(
        "tool_m4s1t9c4", "Last Digit Lens", "simulation",
        "A number is divisible by 10, 5 or 2 when its last digit says so, and the lens shows the last digit without "
        "any division.",
        "A number box; a lens that highlights only the last digit; three test lights for 10, 5 and 2 that turn "
        "green or stay off; a Check by division button that shows the remainders for comparison.",
        ["Type a number.",
         "Predict which lights come on from the last digit.",
         "Press Check by division."],
        ["8560: which of 10, 5 and 2 divide it (all three).",
         "125: which of 10, 5 and 2 divide it (5 only).",
         "682: which of 10, 5 and 2 divide it (2 only).",
         "173: which of 10, 5 and 2 divide it (none).",
         "Find the largest number below 399 divisible by 5 (395).",
         "Remainders of 2345 on dividing by 10, 5 and 2 (5, 0 and 1)."],
        ["The lens shows the last digit and the rule for each light in a word.",
         "A wrong prediction shows the remainder from the division.",
         "A solved card shows the last digit and the three lights."],
        "All six cards are solved.",
        ["number", "lastDigit", "lights", "answer", "cardIndex"],
        ["M_FIVE_ONLY_ENDS_FIVE"],
        ["Which digit does the lens show?",
         "The last digit alone decides 10, 5 and 2.",
         "Check whether it is 0, whether it is 0 or 5, and whether it is even.",
         "The lights are lit and the remainders shown; a similar card follows."]),

    "digit_lens_48": T(
        "tool_m4s2t10c4", "Last Two and Three Digits", "simulation",
        "Divisibility by 4 depends on the last two digits and divisibility by 8 on the last three.",
        "A number box; a lens that grows from the last two digits to the last three; two test lights for 4 and 8; "
        "a Check by division button; a list of the multiples of 4 and 8 in the lens window.",
        ["Type a number.",
         "Slide the lens to two or three digits and read the number in it.",
         "Predict the lights, then press Check by division."],
        ["8536: is it divisible by 4 (yes, 36 is).",
         "1732 and 1736: which is divisible by 4 (both).",
         "8560: change the last two digits to make a multiple of 8 (8552).",
         "1128: is it divisible by 8 (yes, 128 is).",
         "Find the largest 4-digit palindrome divisible by 4 (8888).",
         "2024 to 2099: how many leap years (19)."],
        ["The lens window shows the number being tested and the nearest multiples.",
         "A wrong prediction shows why: the digits beyond the lens are multiples of 100 or 1000.",
         "A solved card shows the digits used and the light."],
        "All six cards are solved.",
        ["number", "lensDigits", "lights", "answer", "cardIndex"],
        ["M_LAST_DIGIT_FOR_4", "M_LAST_TWO_FOR_8"],
        ["How many digits does the lens show?",
         "For 4 look at the last two digits; for 8 look at the last three.",
         "Divide only the number in the lens by 4 or by 8.",
         "The lens number and the answer are shown; a similar card follows."]),

    "prime_grid": T(
        "tool_m4s3t13c3", "Prime Grid Puzzle", "simulation",
        "A grid of primes is filled so that each row and each column multiplies to the number beside it, using prime "
        "factorisation of the clue.",
        "A 3 by 3 grid with row products on the right and column products below; a prime keypad of 2, 3, 5, 7, 11, "
        "13, 17, 19; tiles drop into cells; a product read-out for each row and column; green when it matches.",
        ["Break a clue into primes.",
         "Drop prime tiles into cells.",
         "Match every row and column product."],
        ["A row of 30: three primes in any order (2, 3 and 5).",
         "A row of 27: three primes (3, 3 and 3).",
         "A row of 8: three primes (2, 2 and 2).",
         "A column of 105: three primes (3, 5 and 7).",
         "Complete a whole 3 by 3 puzzle with all clues given.",
         "Check your grid by multiplying rows and columns."],
        ["A product that does not match is shown beside the clue.",
         "A non-prime tile is refused and the keypad reminds that only primes are allowed.",
         "A solved puzzle shows every row and column product."],
        "All six puzzles are solved.",
        ["cells", "rowClues", "colClues", "answer", "cardIndex"],
        ["M_ORDER_MATTERS", "M_STOP_AT_COMPOSITE"],
        ["Which primes multiply to the clue?",
         "Break the clue into primes; each cell holds one prime of its row and column.",
         "Start with the clue that has the fewest prime factors.",
         "The row is filled and the column products are checked; a similar puzzle follows."]),
}
