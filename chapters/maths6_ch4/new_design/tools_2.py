# -*- coding: utf-8 -*-
"""Tool specs for module M3 (reading and drawing bar graphs). Doer tools only."""
from topics_common import T

TOOLS = {
    "bar_graph_reader": T(
        "tool_m3s1t7c4", "Bar Graph Reader", "simulation",
        "A bar's length in units times the scale gives the frequency, and totals and differences come from the "
        "readings.",
        "A bar graph with equally spaced guide lines and a scale label such as 1 unit = 100; bars tap to show "
        "their length in units; a question strip; a number entry.",
        ["Read the scale label first.",
         "Tap a bar to see its length in units.",
         "Type the value, total or difference."],
        ["Scale 1 unit = 1 student, Class 2 bar of 5 units (5).",
         "Scale 1 unit = 100 vehicles, bar of 12 units (1200).",
         "Which bar is the longest, and which is the shortest in the absent-students graph? (Class 8 and Class 5)",
         "Add two bars read at 1000 and 800 vehicles (1800).",
         "Population bars 36 and 102 crores: the increase (66).",
         "Scale 1 unit = 10 crores, bar of 8 units (80)."],
        ["Typing the bar's unit length instead of the value shows the scale label beside the bar.",
         "A bar of no height is labelled 0 so the empty class is seen.",
         "A solved card shows units times scale as a short sum."],
        "All six cards are solved.",
        ["scale", "barUnits", "answer", "cardIndex"],
        ["M_BAR_HEIGHT_IS_VALUE", "M_SCALE_UNEQUAL"],
        ["What does one unit of bar length stand for?",
         "Count the units to the top of the bar.",
         "Multiply the units by the scale.",
         "The sum is shown with the bar highlighted and a similar card follows."]),

    "bar_graph_builder": T(
        "tool_m3s2t8c4", "Bar Graph Builder", "manipulative",
        "A scale is chosen to fit the largest value, and each bar's height is its frequency divided by the "
        "scale.",
        "A table of categories and numbers; a scale picker for 1, 2, 4, 5, 10 and 200 per unit; empty axes with "
        "equal gaps and bar slots; bars that drag up to a height; a Check button.",
        ["Pick a scale that fits the largest number.",
         "Drag each bar to its height in units.",
         "Press Check."],
        ["Draw 6, 10, 5, 3, 2 with scale 1 (6, 10, 5, 3, 2 units).",
         "Draw runs 80, 50, 10, 100, 90, 0, 90, 50 with scale 10 (8, 5, 1, 10, 9, 0, 9, 5).",
         "Draw tickets 24, 20, 16, 28 with scale 4 (6, 5, 4, 7).",
         "Draw students 45, 30, 20, 10, 15 with scale 5 (9, 6, 4, 2, 3).",
         "Draw rupees 3000, 3400, 800, 400, 600, 1200 with scale 200 (15, 17, 4, 2, 3, 6).",
         "Find the wrong bar in a graph where a bar does not match its table value."],
        ["A scale that makes a bar run off the paper shows the overflow and asks for a bigger scale.",
         "A bar not starting from zero is rejected with the axis start highlighted.",
         "A solved card shows frequency divided by scale for each bar."],
        "All six cards are solved.",
        ["scale", "heights", "answer", "cardIndex"],
        ["M_BAR_HEIGHT_IS_VALUE", "M_SCALE_UNEQUAL", "M_BAR_WIDTH"],
        ["What is the largest value, and what scale fits it?",
         "Divide each frequency by the scale to find the bar height.",
         "Divide the number for this bar by the scale and drag the bar to that many units.",
         "The heights are filled in and checked, and a similar card follows."]),
}
