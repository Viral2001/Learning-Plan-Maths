# -*- coding: utf-8 -*-
"""Tool specs for modules M3 and M4 (comparing, adding, subtracting, the unit fraction puzzle). Doer tools only."""
from topics_common import T

TOOLS = {
    "fraction_comparator": T(
        "tool_m3s4t8c12", "Fraction Comparator", "manipulative",
        "Two fractions are compared by rewriting them in the same fractional unit and then comparing how many units "
        "each has.",
        "Two bars of the same whole, one per fraction; a common-unit stepper that re-cuts both bars into the same "
        "number of equal cells, allowed only at a common multiple of the denominators; shading runs from the left "
        "and an edge line shows which reaches further; a >, < or = picker.",
        ["Predict which fraction is greater.",
         "Re-cut both bars into a common unit.",
         "Pick >, < or =, or drag the fractions into order."],
        ["4/5 and 7/9 (4/5 > 7/9, since 36/45 > 35/45).", "3/4 and 7/10 (3/4 > 7/10).",
         "8/3 and 5/2 (8/3 > 5/2).", "9/4 and 5/2 (9/4 < 5/2).",
         "Order 7/10, 11/15, 2/5 from smallest (2/5, 7/10, 11/15).",
         "Order 3/4, 12/5, 7/12, 5/4 from largest (12/5, 5/4, 3/4, 7/12)."],
        ["Comparing only the numerators is answered by showing the two bars cut into different units.",
         "A common unit that is not a common multiple is refused: the cells do not line up.",
         "A solved card shows both fractions in the common unit and the sign between them."],
        "All six cards are solved.",
        ["fracA", "fracB", "commonUnit", "answer", "cardIndex"],
        ["M_COMPARE_PARTS", "M_BIG_DENOM"],
        ["Are the two fractions in the same fractional unit?",
         "Find a common multiple of the two denominators.",
         "Rewrite both with that denominator and compare the numerators.",
         "Both are shown in the common unit with the sign; a similar card follows."]),

    "unit_adder": T(
        "tool_m4s5t9c14", "Fraction Bar Combiner: Adding", "manipulative",
        "Fractions are added by first writing them in the same fractional unit and then counting the units together "
        "(Brahmagupta's method).",
        "Two bars of the same whole above a result bar; a common-unit stepper that re-cuts all three; the shaded "
        "units of both bars slide into the result bar and are numbered as they land; a result box with a lowest "
        "terms check.",
        ["Re-cut both bars into the same unit if needed.",
         "Slide the units into the result bar.",
         "Type the sum, in lowest terms or as a mixed number."],
        ["2/5 + 1/5 (3/5).", "4/7 + 6/7 (10/7 = 1 3/7).", "1/4 + 1/3 (7/12).", "2/3 + 1/5 (13/15).",
         "1/6 + 1/3 (1/2).", "2/3 + 3/4 litres of paint (17/12 = 1 5/12 litres)."],
        ["Adding tops and adding bottoms, such as 1/2 + 1/3 making 2/5, is shown with the result bar smaller than 1/2 "
         "alone.",
         "Units of different sizes will not slide into one bar until a common unit is chosen.",
         "A solved card shows the units numbered in the result bar and the sum."],
        "All six cards are solved.",
        ["fracA", "fracB", "commonUnit", "sum", "cardIndex"],
        ["M_ADD_TOPS_BOTTOMS", "M_SAME_UNIT_ONLY"],
        ["Are the pieces of the two fractions the same size?",
         "Use a common multiple of the denominators as the new unit.",
         "Rewrite both fractions, then add the numerators and keep the denominator.",
         "The equal-unit bars and the sum are shown; a similar card follows."]),

    "unit_subtractor": T(
        "tool_m4s5t9c15", "Fraction Bar Combiner: Subtracting", "manipulative",
        "Fractions are subtracted by first writing them in the same fractional unit and then taking away that many "
        "units (Brahmagupta's method).",
        "One bar of the same whole showing the first fraction; a common-unit stepper that re-cuts it and the "
        "fraction to be taken away; a Remove button that lifts away units one at a time, numbered; a result box "
        "with a lowest terms check.",
        ["Re-cut into a common unit if needed.",
         "Remove the units of the second fraction.",
         "Type what is left, in lowest terms."],
        ["6/7 − 4/7 (2/7).", "5/8 − 3/8 (2/8 = 1/4).", "3/4 − 2/3 (1/12).", "5/6 − 4/9 (7/18).",
         "7/10 − 1/2 km walked (1/5 km).", "10/3 − 13/4 minutes (1/12 minute)."],
        ["Subtracting tops and subtracting bottoms is answered by showing the units of different sizes.",
         "Removing before the units match is refused: the pieces do not fit.",
         "A solved card shows the units left over and the difference."],
        "All six cards are solved.",
        ["fracA", "fracB", "commonUnit", "difference", "cardIndex"],
        ["M_SUB_TOPS_BOTTOMS", "M_SAME_UNIT_ONLY"],
        ["Are the pieces of the two fractions the same size?",
         "Use a common multiple of the denominators as the new unit.",
         "Rewrite both, subtract the numerators and keep the denominator.",
         "The units taken away and the units left are shown; a similar card follows."]),

    "unit_fraction_puzzle": T(
        "tool_c6f_unit_fraction_puzzle", "Unit Fraction Puzzle", "game",
        "One whole can be split into different fractional units: three different units add to 1 in only one way, "
        "four different units in six ways.",
        "A circle of one whole; a tray of unit fraction tiles 1/2 to 1/42; dragging a tile onto the circle fills a "
        "sector of that size; a running sum in a common unit; a found-solutions board.",
        ["Predict which units could fit together.",
         "Drag different unit tiles onto the circle.",
         "Press Check when the circle is full."],
        ["Fill the circle with two different units (not possible).", "Fill it with three different units "
         "(1/2 + 1/3 + 1/6).", "With 1/2 and 1/3 placed, find the third (1/6).",
         "Find four different units starting 1/2, 1/4 (1/6 + 1/12, or 1/5 + 1/20).",
         "Find four starting 1/2, 1/3 (for example 1/7 + 1/42).", "Find all six ways with four units."],
        ["An overfull circle shows the overlap and the sum past 1.",
         "Repeating a unit is refused, since the units must be different.",
         "A solved card adds the solution to the board with its sum in a common unit."],
        "Three cards are solved, or the student stops after the six-ways card.",
        ["tilesPlaced", "sum", "solutionsFound", "cardIndex"],
        ["M_ADD_TOPS_BOTTOMS", "M_BIG_DENOM"],
        ["What is the largest fractional unit?",
         "Start with 1/2, then see how much of the circle is left.",
         "Write the remainder in a common unit and look for a unit fraction that fits.",
         "One solution is shown filled in; a similar card follows."]),
}
