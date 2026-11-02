# -*- coding: utf-8 -*-
"""Tool specs for modules M1 and M2 (multiples, factors, primes). Doer tools only."""
from topics_common import T

TOOLS = {
    "idli_vada": T(
        "tool_m1s1t2c4", "Idli-Vada Caller", "simulation",
        "Idli is said at multiples of one number, vada at multiples of the other, and idli-vada at the numbers that "
        "are both: the common multiples.",
        "A ring of numbered children from 1 to 60; two steppers pick the idli number and the vada number, each from "
        "2 to 12; a Play button calls the game; idli numbers glow orange, vada numbers glow green, both glow gold; a "
        "tally of each call.",
        ["Predict the first gold number before pressing Play.",
         "Choose the two numbers and press Play.",
         "Type the first idli-vada number or the count of gold numbers."],
        ["Idli 3 and vada 5: first idli-vada number (15).",
         "Idli 4 and vada 6: first idli-vada number (12).",
         "Idli 2 and vada 5 up to 60: how many idli-vada calls (6).",
         "Idli 3 and vada 7: first idli-vada number (21).",
         "Choose two numbers so that nobody ever says just vada (idli 4 and vada 8, or similar).",
         "Choose two numbers below 10 whose first idli-vada is after 50 (7 and 8, or similar)."],
        ["A gold number is always in both lists, so the tool shows the two multiples side by side.",
         "A wrong first number is checked against the glowing numbers one by one.",
         "A solved card shows the list of gold numbers as multiples of the first one."],
        "All six cards are solved.",
        ["idliNumber", "vadaNumber", "goldNumbers", "answer", "cardIndex"],
        ["M_ONLY_FIRST_COMMON", "M_MULTIPLE_FACTOR"],
        ["Which numbers does each child call? Read the colours.",
         "The idli-vada numbers are the numbers that are in both lists.",
         "Press Play and look at the first gold number.",
         "The first gold number is shown and the rest of the gold numbers follow it; a similar card comes next."]),

    "jump_jackpot": T(
        "tool_m1s1t3c3", "Jump Jackpot", "simulation",
        "A jump size reaches a treasure only if it is a factor of the treasure number, and it reaches two treasures "
        "only if it is a common factor.",
        "A number line from 0 to 72; one or two treasure markers placed by steppers; a jump size stepper from 1 to "
        "36; a Jump button that moves Jumpy by the chosen size; landing spots marked; a list of jump sizes that have "
        "worked.",
        ["Place the treasures.",
         "Choose a jump size and press Jump until Jumpy passes the treasures.",
         "List every jump size that reaches the treasures."],
        ["One treasure on 24: all the jump sizes (1, 2, 3, 4, 6, 8, 12, 24).",
         "Treasures on 14 and 36: jump sizes that reach both (1, 2).",
         "Treasures on 15 and 30: jump sizes that reach both (1, 3, 5, 15).",
         "Treasures on 28 and 70: jump sizes that reach both (1, 2, 7, 14).",
         "Treasures on 20 and 28: jump sizes that reach both (1, 2, 4).",
         "Treasures on 12 and 18: the biggest jump size that reaches both (6)."],
        ["Jumpy's landing spots are shown, so a jump that misses a treasure is seen at once.",
         "A missing jump size is shown as a path that lands on one treasure but jumps over the other.",
         "A solved card lists the jump sizes in order with the factor pairs of each treasure."],
        "All six cards are solved.",
        ["treasureA", "treasureB", "jumpSize", "foundSizes", "cardIndex"],
        ["M_FACTORS_MISS_ENDS", "M_MULTIPLE_FACTOR"],
        ["Where does Jumpy land with this jump size?",
         "A jump size works if it divides the treasure number exactly; check 1 and the number itself too.",
         "Try each jump size from 1 upward and mark the ones that land on the treasure.",
         "The working sizes are shown on the line; a similar card follows."]),

    "factor_rect": T(
        "tool_m2s1t4c4", "Rectangle Maker", "manipulative",
        "A number is arranged in rows and columns of dots; the number of ways is the number of factor pairs, and a "
        "prime has only one way.",
        "A tray of dot counters with a stepper from 2 to 60; a Make Rectangles button that lays out every rectangle "
        "of rows by columns; each rectangle labelled with its rows and columns; a count of the factors; a coloured "
        "tag reading prime, composite or neither.",
        ["Guess how many rectangles the number makes.",
         "Choose the number and press Make Rectangles.",
         "Type the factors or tag the number."],
        ["12 dots: list all the factors (1, 2, 3, 4, 6, 12).",
         "7 dots: how many rectangles (1, so 7 is prime).",
         "18 dots: how many factors (6).",
         "1 dot: prime, composite or neither (neither).",
         "Find a number below 30 with exactly 2 factors that is even (2).",
         "Find all the primes from 21 to 30 (23 and 29)."],
        ["Each rectangle is drawn, so a missed factor pair shows as a missing shape.",
         "A wrong tag shows the count of factors beside the rule: exactly two factors means prime.",
         "A solved card shows the rectangles and the factor count together."],
        "All six cards are solved.",
        ["number", "rectangles", "factorCount", "answer", "cardIndex"],
        ["M_ONE_IS_PRIME", "M_ALL_EVEN_COMPOSITE", "M_FACTORS_MISS_ENDS"],
        ["How many rows and how many columns can the dots make?",
         "Each pair of rows and columns multiplies to the number, so both are factors.",
         "Try rows 1, 2, 3 and so on in turn; stop when the columns become smaller than the rows.",
         "The rectangles are shown with their factors; a similar card follows."]),

    "sieve": T(
        "tool_m2s1t5c3", "Eratosthenes Sieve", "simulation",
        "Crossing out the multiples of each circled number leaves only the primes.",
        "A 10 by 10 grid of numbers from 1 to 100; a Next step button that circles the next uncrossed number and "
        "crosses out its multiples; circled numbers are green and crossed out numbers are grey; a counter of primes "
        "found so far.",
        ["Predict the next circled number before pressing Next step.",
         "Press Next step and watch the multiples go.",
         "Tap a number to say prime or composite."],
        ["After circling 2 and 3, which is the next number to circle (5).",
         "How many primes are there from 1 to 30 (10).",
         "How many primes are there from 1 to 100 (25).",
         "Which number is crossed out by 7 but not by 2, 3 or 5 (49).",
         "Find all the twin primes up to 30 (3 and 5, 5 and 7, 11 and 13, 17 and 19).",
         "Which is the largest prime below 100 (97)."],
        ["The multiples being crossed out are flashed, so a missed one is seen.",
         "A wrong tap on a crossed-out number shows the circled number that removed it.",
         "A solved card shows the primes found in order."],
        "All six cards are solved.",
        ["currentPrime", "crossedOut", "circled", "answer", "cardIndex"],
        ["M_SIEVE_MAGIC", "M_ODD_MEANS_PRIME", "M_ONE_IS_PRIME"],
        ["Which number is the first one left uncrossed?",
         "The first uncrossed number is prime; cross out its multiples.",
         "Circle it, cross out its multiples, and look for the next uncrossed number.",
         "The tool does the next step and shows why the number is prime; a similar card follows."]),
}
