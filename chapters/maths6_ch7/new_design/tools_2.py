# -*- coding: utf-8 -*-
"""Tool specs for module M2 (fractions greater than one, equivalent fractions, lowest terms). Doer tools only."""
from topics_common import T

TOOLS = {
    "mixed_builder": T(
        "tool_m2s3t6c8", "Mixed Number Builder", "manipulative",
        "A fraction greater than one is grouped into whole units and a leftover fractional part, and a mixed number "
        "is ungrouped back into a fraction.",
        "A number line from 0 to 10 with each unit cut into n equal gaps; a Hop button that hops 1/n at a time from "
        "0; every full unit filled turns into a solid whole block; a two-way read-out fraction and whole + part.",
        ["Predict how many wholes the fraction holds.",
         "Hop the units and watch full wholes group together.",
         "Type the mixed number, or type the fraction for a given mixed number."],
        ["How many wholes in 7/2? (3, since 7/2 = 3 + 1/2)", "Write 8/3 as a mixed number (2 2/3).",
         "Write 11/5 as a mixed number (2 1/5).", "Write 19/6 as a mixed number (3 1/6).",
         "Write 3 + 3/4 as a fraction (15/4).", "Write 2 3/11 as a fraction (25/11).",
         "Is 8/4 a mixed number? (No, it is exactly 2.)"],
        ["Reading 2 1/2 as 2 × 1/2 is answered by showing 2 full wholes and one half block on the line.",
         "A wrong whole count shows the hops grouped n at a time with the leftover hops counted.",
         "A solved card shows both forms side by side, for example 8/3 = 2 + 2/3 = 2 2/3."],
        "All seven cards are solved.",
        ["unitParts", "hops", "wholes", "leftover", "answer", "cardIndex"],
        ["M_MIXED_PRODUCT", "M_LESS_THAN_ONE"],
        ["How many parts make one whole here?",
         "Group the units in fives, threes or whatever the denominator is: each group is one whole.",
         "Divide the numerator by the denominator: the quotient is the wholes, the remainder is the part.",
         "The grouping is shown with wholes and the leftover; a similar card follows."]),

    "fraction_wall": T(
        "tool_m3s4t7c10", "Fraction Wall", "manipulative",
        "Two fractions are equivalent when they reach the same length on the same whole, even though they are "
        "written with different numbers; multiplying the numerator and the denominator by the same number keeps the "
        "length.",
        "A fraction wall, rows from 1 whole down to tenths and twelfths, all the same length and flush at 0; tap "
        "cells to shade a run from the left; a vertical line drops from the end of each run; a shared line prints "
        "both names, for example 1/2 = 3/6.",
        ["Predict whether two fractions reach the same length.",
         "Shade a run in two rows.",
         "Type a missing number, or say equal or not equal."],
        ["Are 1/2 and 2/4 equal? Are 2/4 and 4/8? (Yes, yes)", "How many sixths make 1/2? (3)",
         "Are 2/3 and 4/6 equivalent? (Yes)", "Write two fractions equal to 2/6 (1/3, 3/9 or 4/12).",
         "Fill in 5/4 = ?/8 (10).", "Fill in 4/3 = 12/? (9).", "Write as many as you can equal to 4/6."],
        ["Adding the same number to top and bottom, such as 2/3 to 3/4, is shown with two lines that do not meet.",
         "A run in the wrong row shows its own line beside the target line.",
         "A solved card shows the shared line with both fractions written on it."],
        "All seven cards are solved.",
        ["rowA", "runA", "rowB", "runB", "answer", "cardIndex"],
        ["M_EQUIV_ADD", "M_EQUIV_DIFFERENT"],
        ["Do the two runs have to be on the same whole?",
         "Equal fractions end on the same vertical line of the wall.",
         "Multiply the numerator and the denominator by the same number, then check the line.",
         "The two runs are shown ending on one line, with both names; a similar card follows."]),

    "fraction_reducer": T(
        "tool_c6f_fraction_reducer", "Fraction Reducer", "manipulative",
        "A fraction is in lowest terms when its numerator and denominator have no common factor except 1; dividing "
        "both by a common factor keeps the fraction equal.",
        "A large fraction card; a row of divisor buttons 2, 3, 5, 7 and a custom divisor box; each press divides "
        "top and bottom together and logs the step; a strip below that stays the same length after every step; a "
        "Done button.",
        ["Spot a common factor of the top and bottom.",
         "Press a divisor to divide both, as many times as needed.",
         "Press Done when no common factor except 1 is left."],
        ["16/20 (4/5).", "36/60, in steps and then in one go (3/5).", "17/51 (1/3).", "64/144 (4/9).",
         "126/147 (6/7).", "525/112 (75/16)."],
        ["A divisor that does not divide both is refused, showing the remainder.",
         "Pressing Done too early shows the common factor that is left, for example 18/30 still shares 6.",
         "A solved card shows the steps and the strip of the same length, with the one-go divisor, the HCF."],
        "All six cards are reduced fully.",
        ["numerator", "denominator", "steps", "done", "cardIndex"],
        ["M_LOWEST_PARTIAL", "M_EQUIV_DIFFERENT"],
        ["What does lowest terms mean?",
         "Find a number that divides both the numerator and the denominator.",
         "Try 2, then 3, then 5 and 7 until none divides both.",
         "The divisions are shown step by step to lowest terms; a similar card follows."]),
}
