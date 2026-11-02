# -*- coding: utf-8 -*-
"""Tool specs for module M4 (honest graphs). Doer tools only."""
from topics_common import T

TOOLS = {
    "honest_graph_checker": T(
        "tool_m4s2t10c4", "Honest Graph Checker", "simulation",
        "A decorated graph is honest only if its pictures show the same numbers as the table, so every picture "
        "is checked against the table.",
        "The mountain table beside a plain column graph and a triangle picture; a ruler line that measures "
        "heights and widths; a doubling check; a vertical or horizontal bar chooser.",
        ["Measure the heights with the ruler.",
         "Compare each picture with the table.",
         "Choose honest or misleading, or vertical or horizontal."],
        ["Plain column graph: which mountain is tallest (Everest).",
         "Triangle picture: do taller triangles also get wider (yes, so it misleads about width).",
         "Is Everest twice as tall as Elbrus? Double 5642 (11284, more than 8848, so no).",
         "Heights of the tallest persons in each class: vertical or horizontal bars (vertical).",
         "Lengths of the longest rivers: vertical or horizontal bars (horizontal).",
         "Denali 6194 m and Kilimanjaro 5895 m: how much taller is Denali (299 m)."],
        ["A picture judged honest without a check shows the ruler first and asks for a measurement.",
         "A misleading picture is shown next to the equal-width bars for the same table.",
         "A solved card shows the table value, the picture value and the check."],
        "All six cards are solved.",
        ["picture", "measured", "answer", "cardIndex"],
        ["M_TALLER_WIDER", "M_PICTURE_PROPORTION", "M_ALWAYS_GRAPH"],
        ["What does the table say about each value?",
         "Measure the picture with the ruler and compare it with the table.",
         "Double the smaller value and compare it with the larger one.",
         "The measurement and the comparison are shown, and a similar card follows."]),
}
