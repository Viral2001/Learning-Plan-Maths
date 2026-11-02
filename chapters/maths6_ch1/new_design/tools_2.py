# -*- coding: utf-8 -*-
"""Tool specs for module M2 (dot pictures and relations among sequences): dot_picture_builder, odd_sum_builder,
updown_builder, sequence_relations_lab. Doer tools only."""
from topics_common import T

TOOLS = {
    "dot_picture_builder": T(
        "tool_m2s1t4c3", "Dot Picture Builder", "manipulative",
        "A number sequence is drawn with dots or blocks, and the picture grows by the same rule each time.",
        "A dot board with the first five pictures of a sequence shown; a picture-number stepper; Add Dots and Add "
        "Layer buttons; a live count under the picture.",
        ["Predict the next picture before adding.",
         "Press Add Dots or Add Layer to grow the picture.",
         "Type the number the picture shows."],
        ["Counting numbers: the sixth picture (6).",
         "Odd numbers: the sixth picture (11).",
         "Triangular numbers: the sixth picture (21).",
         "Square numbers: the sixth picture (36).",
         "Cube numbers: the sixth picture (216).",
         "Even numbers: the sixth picture, two rows of 6 (12)."],
        ["A picture that is not a triangle, square or cube is marked with the missing dots.",
         "A wrong count shows the dots numbered one by one.",
         "A solved card shows the new dots in a different colour from the old ones."],
        "All six pictures are built and counted.",
        ["sequence", "pictureNo", "dots", "answer", "cardIndex"],
        ["M_NAMES_ARBITRARY", "M_ALL_ONES_NO_PATTERN"],
        ["What does each new picture add to the last one?",
         "Look at how many dots were added between pictures 4 and 5.",
         "Add one more row, layer or ring in the same way and count.",
         "The new dots are shown in colour and counted; a similar picture follows."]),

    "odd_sum_builder": T(
        "tool_m2s3t6c3", "Odd Number L-Shape Builder", "manipulative",
        "The first n odd numbers add up to n × n, because L-shapes of 1, 3, 5, 7, ... dots wrap into a square "
        "grid.",
        "A square dot grid anchored at one corner; a Wrap Next L button that adds one L-shape in a new colour; a "
        "running sum under the grid; a size chooser for 4 by 4 up to 10 by 10.",
        ["Predict the sum before wrapping the next L.",
         "Press Wrap Next L, one layer at a time.",
         "Type the sum of the first odd numbers."],
        ["1 + 3 + 5 (9).", "1 + 3 + 5 + 7 (16).", "The first 6 odd numbers (36).",
         "The first 8 odd numbers (64).", "The first 10 odd numbers (100).",
         "The first 100 odd numbers, by imagining the grid (10000)."],
        ["An L-shape with the wrong number of dots does not fit, and the gap or overlap is shown.",
         "A wrong sum shows the side length of the grid beside the count of layers.",
         "A solved card shows the sum written as the grid side times itself."],
        "All six sums are found.",
        ["gridSize", "layers", "sum", "answer", "cardIndex"],
        ["M_ODD_SUM_ODD", "M_PICTURE_ONE_SIZE", "M_CHECK_FEW"],
        ["How many layers have been wrapped so far?",
         "Count the layers: that is also the side of the square.",
         "Multiply the side by itself.",
         "The grid is shown with its side counted; a similar sum follows."]),

    "updown_builder": T(
        "tool_m2s4t7c3", "Diamond Dot Builder", "manipulative",
        "Adding the counting numbers up to n and back down gives n × n, because the diamond of dots is an n by n "
        "grid seen along its diagonals.",
        "A diamond of dot rows, with a stepper for n from 1 to 10; a Show Grid button that tilts the diamond into "
        "a square grid; a row-by-row sum written beside the diamond.",
        ["Predict the total before tilting.",
         "Set n and read the rows 1, 2, up to n, and back down.",
         "Press Show Grid and type the total."],
        ["1 + 2 + 1 (4).", "1 + 2 + 3 + 2 + 1 (9).", "1 + 2 + 3 + 4 + 3 + 2 + 1 (16).",
         "Up to 7 and back down (49).", "Up to 10 and back down (100).",
         "Up to 100 and back down, by imagining (10000)."],
        ["A diamond with a missing row is marked, and the sum shows the row that is left out.",
         "A wrong total shows the grid side n beside the total.",
         "A solved card shows the diamond tilted into an n by n grid."],
        "All six totals are found.",
        ["n", "rows", "total", "answer", "cardIndex"],
        ["M_UP_DOWN_DOUBLE", "M_PICTURE_ONE_SIZE"],
        ["How many dots are in the middle row?",
         "The middle row is n; the grid is n by n.",
         "Multiply n by itself.",
         "The diamond is tilted into the grid and counted; a similar sum follows."]),

    "sequence_relations_lab": T(
        "tool_m2s5t8c3", "Sequence Relations Lab", "simulation",
        "Running totals and sums of neighbours turn one sequence into another, and the first terms show which.",
        "Two strips of terms, a source above and a result below; a Source picker (All 1s, counting, triangular, "
        "powers of 2, hexagonal); an Operation picker (running total, add neighbours, times 6 plus 1); a Name It "
        "box.",
        ["Predict the result before pressing Apply.",
         "Pick a source and an operation and press Apply.",
         "Name the sequence that appears."],
        ["All 1s, running total (counting numbers).",
         "Counting numbers, running total (triangular numbers).",
         "Triangular numbers, add neighbours (square numbers).",
         "Powers of 2, running total, then add 1 (powers of 2).",
         "Triangular numbers, times 6 plus 1 (hexagonal numbers).",
         "Hexagonal numbers, running total (cube numbers)."],
        ["A result with only the first term matching is not accepted; the tool shows the next terms to compare.",
         "A wrong name puts the result beside Table 1 for matching.",
         "A solved card shows the first five terms of both strips."],
        "All six relations are named.",
        ["source", "operation", "result", "answer", "cardIndex"],
        ["M_RUNNING_SAME", "M_PAIRS_SAME", "M_CHECK_FEW"],
        ["What does the operation do to each term?",
         "Compare the result strip with the sequences in Table 1.",
         "Check the first five terms of the result against one sequence.",
         "The result is lined up against the matching sequence; a similar relation follows."]),
}
