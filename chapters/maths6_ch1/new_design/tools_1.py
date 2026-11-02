# -*- coding: utf-8 -*-
"""Tool specs for module M1 (number sequences): sequence_rule_finder. Doer tools only."""
from topics_common import T

TOOLS = {
    "sequence_rule_finder": T(
        "tool_m1s3t3c4", "Sequence Rule Finder", "manipulative",
        "A number sequence follows a rule, and a rule is right only if it fits every term shown.",
        "A strip of the first six terms of a sequence with the next three boxes empty; a rule picker (add a number, "
        "add a growing number, multiply, add the two before); a Test button that checks the rule on each term.",
        ["Predict the rule before picking it.",
         "Pick a rule and press Test.",
         "Type the next three terms."],
        ["1, 3, 5, 7, 9, 11 (add 2; 13, 15, 17).",
         "1, 3, 6, 10, 15, 21 (add 2, 3, 4, 5, 6; 28, 36, 45).",
         "1, 4, 9, 16, 25, 36 (squares; 49, 64, 81).",
         "1, 2, 3, 5, 8, 13 (add the two before; 21, 34, 55).",
         "1, 2, 4, 8, 16, 32 (multiply by 2; 64, 128, 256).",
         "1, 3, 9, 27, 81, 243 (multiply by 3; 729, 2187, 6561)."],
        ["A rule that fits only the first two terms is tested on all six, and the term where it fails is marked.",
         "A wrong next term shows the rule applied once to the last term.",
         "A solved card shows the rule written under each jump."],
        "All six sequences have the right rule and next three terms.",
        ["terms", "rule", "answer", "cardIndex"],
        ["M_ADD_SAME_ONLY", "M_RULE_FROM_TWO", "M_POWERS_ADD"],
        ["Look at how each term changes from the one before.",
         "Try add, add a growing number, multiply, or add the two before, and press Test.",
         "Find the jump between the last two terms and apply the rule once.",
         "The rule is shown under each jump and the next terms are filled; a similar sequence follows."]),
}
