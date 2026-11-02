# -*- coding: utf-8 -*-
"""Tool specs for modules M2 and M3 (co-primes, prime factorisation)."""
from topics_common import T

TOOLS = {
    "thread_art": T(
        "tool_m2s2t6c4", "Thread Art Co-prime Check", "simulation",
        "A thread tied to every gap-th peg of a circle reaches every peg exactly when the number of pegs and the gap "
        "are co-prime.",
        "A circle of pegs with a stepper for the number of pegs from 6 to 24 and a stepper for the thread gap from 1 "
        "to 12; a Draw button that ties the thread peg by peg; pegs reached turn gold; a read-out of the pegs "
        "reached and a co-prime tick.",
        ["Predict whether the thread reaches every peg.",
         "Choose the pegs and the gap and press Draw.",
         "Say co-prime or not for the pair."],
        ["12 pegs, gap 4: does the thread reach every peg (no, 12 and 4 share 4).",
         "13 pegs, gap 4: does the thread reach every peg (yes, 13 and 4 are co-prime).",
         "12 pegs, gap 5: every peg or not (every peg).",
         "Find a gap below 12 for 12 pegs that reaches every peg (5, 7 or 11).",
         "10 pegs, gap 4: how many pegs are reached (5).",
         "Which of 18 and 35, 15 and 37, 30 and 415 are co-prime (18 and 35, 15 and 37)."],
        ["Pegs missed stay grey so the missed pegs show the common factor.",
         "A wrong co-prime answer shows the common factor of the two numbers.",
         "A solved card shows the pegs reached and the co-prime tick."],
        "All six cards are solved.",
        ["pegs", "gap", "reached", "answer", "cardIndex"],
        ["M_COPRIME_BOTH_PRIME", "M_ONE_PAIR_ENOUGH"],
        ["Which pegs does the thread touch?",
         "The thread reaches every peg when the two numbers have no common factor other than 1.",
         "List the factors of both numbers and look for one besides 1.",
         "The common factor is shown and the pegs it misses; a similar card follows."]),

    "factor_tree": T(
        "tool_m3s1t7c4", "Factor Tree Builder", "manipulative",
        "Breaking a number into two factors again and again ends in the same primes whichever way it is split.",
        "A number at the top of a tree; a Split button that asks for two factors whose product is the number; prime "
        "leaves turn green and composite ones stay open; a bar of the primes found so far written in increasing "
        "order.",
        ["Choose a way to split the number.",
         "Keep splitting every open leaf until all are green.",
         "Read off the prime factorisation."],
        ["72: build a tree and write its prime factorisation (2 × 2 × 2 × 3 × 3).",
         "72: build a different tree and compare the leaves (same primes).",
         "64: write the prime factorisation (2 × 2 × 2 × 2 × 2 × 2).",
         "105: write the prime factorisation (3 × 5 × 7).",
         "A number with one 2, two 3s and one 11 (198).",
         "Three primes below 30 whose product is 1955 (5, 17 and 23)."],
        ["A split that does not multiply to the number is turned back with the product shown.",
         "A composite leaf left open shows its factors waiting.",
         "A solved card puts two different trees side by side with the same primes."],
        "All six cards are solved.",
        ["rootNumber", "splits", "leaves", "answer", "cardIndex"],
        ["M_TREE_DIFFERENT", "M_STOP_AT_COMPOSITE", "M_ORDER_MATTERS"],
        ["Which two numbers multiply to the number on this leaf?",
         "Split every composite leaf; stop only when every leaf is prime.",
         "Start with the smallest prime that divides the number.",
         "The tree is finished for you and the primes are read out in order; a similar card follows."]),

    "prime_compare": T(
        "tool_m3s2t8c3", "Factorisation Compare", "simulation",
        "Writing two numbers as products of primes shows at once whether they share a prime factor, and whether the "
        "primes of one are all inside the other.",
        "Two number boxes with prime factorisations shown as rows of coloured tiles, one colour per prime; the tiles "
        "line up row against row; a shared primes marker; two verdicts, co-prime or not and divisible or not.",
        ["Type two numbers.",
         "Match the tiles and look for shared colours.",
         "Say co-prime or not, and divisible or not."],
        ["56 and 63: co-prime (no).",
         "40 and 231: co-prime (yes).",
         "168 and 12: is 168 divisible by 12 (yes).",
         "75 and 21: is 75 divisible by 21 (no).",
         "42 and 12: is 42 divisible by 12 (no).",
         "30 and 45: co-prime and divisible (no and no)."],
        ["Shared tiles are highlighted so the common prime is seen.",
         "For divisibility, the tiles of the smaller number that find no match are shown in red.",
         "A solved card shows both verdicts with the tiles."],
        "All six cards are solved.",
        ["numberA", "numberB", "tilesA", "tilesB", "answer"],
        ["M_SHARED_PRIME_DIVIDES", "M_COPRIME_BOTH_PRIME"],
        ["What colours do the two rows share?",
         "No shared prime means co-prime; every prime of the smaller inside the bigger means divisible.",
         "Count each prime in both rows and compare the counts.",
         "The tiles are matched and the verdicts are read out; a similar card follows."]),
}
