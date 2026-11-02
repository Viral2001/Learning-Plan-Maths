# -*- coding: utf-8 -*-
"""Tool specs for the matchstick patterns topic."""
from topics_common import T

TOOLS = {
    "pattern_formula_finder": T(
        "tool_pattern_formula_finder", "Pattern Formula Finder", "simulation",
        "A growing pattern has a formula in the step number: a start amount plus the amount added at every step, "
        "counted as one fewer than the step number.",
        "A picture of the first steps of a pattern built from matchsticks or squares; a table of step numbers and "
        "counts; a field for the amount added each step and the start amount; a formula line with the step y; a "
        "check that compares the formula with every step in the table.",
        ["Look at the first steps and fill in the count at each step.",
         "Find how much is added at each step and the count at Step 1.",
         "Build the formula line from the start and the added amounts, then simplify it.",
         "Press Check to compare the formula with every step, then ask for a far step."],
        ["Triangles of matchsticks (2y + 1).", "Squares in a row (3w + 1).", "A rope folded and cut (r + 2).",
         "Growing squares (4n + 1).", "A 4 column grid with the number in row r and column c (4(r − 1) + c).",
         "A pattern of your own with a start and an added amount."],
        ["Using y instead of y − 1 as the number of additions is shown with Step 1 not matching the table.",
         "An unsimplified formula such as 3 + 2 × (y − 1) is accepted and its simplified form is shown beside it.",
         "A formula that fits the first two steps but not the third is marked as not yet proved."],
        "All six patterns have a formula that matches every step and gives the right far step.",
        ["pattern", "start", "added", "formula", "farStep", "cardIndex"],
        ["M_PATTERN_STEP"],
        ["What is the count at Step 1, and what is added to reach the next step?",
         "At Step y, the amount is added one time fewer than y.",
         "Write start plus added times (y − 1), then simplify.",
         "The formula is built from the start and the added amount, simplified and checked on every step, and a "
         "new pattern follows."]),
}
