# -*- coding: utf-8 -*-
"""Tool specs for modules M2 and M3 (stories to expressions, signs after a bracket, sharing a multiplier)."""
from topics_common import T

TOOLS = {
    "story_expression": T(
        "tool_story_expression", "Story to Expression", "manipulative",
        "A story turns into an expression when each group of equal things becomes a times term, each extra or loss "
        "becomes a separate signed term, and the terms are added.",
        "A short picture story on the left; on the right empty term slots with a sign chooser before each; number "
        "chips to drop in; a value strip that works out each term and the total; a reverse mode where an expression "
        "is given and the student picks the story that fits.",
        ["Read the story and spot the equal groups and the extras.",
         "Build one term for each part, with its sign.",
         "Check the value strip against the story.",
         "In reverse mode, pick the story that matches a given expression."],
        ["Four plates of 23 rupees each and a 5 rupee tip (4 × 23 + 5 = 97).",
         "Packets of 2 kg made from 100 kg and 4 packets already there (4 + 100 ÷ 2 = 54).",
         "Six full groups of 5 and 3 left over (6 × 5 + 3 = 33).",
         "Reverse: 5 × 12 − 6 (five packets of 12 and 6 eaten).",
         "Reverse: 4 × 9 + 2 × 6 (four boxes of 9 and two bags of 6).",
         "A shop with 89 items, 21 more arriving and 10 sold (89 + 21 − 10 = 100)."],
        ["A term with the wrong sign is highlighted against the sentence in the story that gives the sign.",
         "A times term is checked against the group count in the picture.",
         "In reverse mode the wrong story is replayed to show which term it does not match."],
        "All six stories and expressions are matched with the value correct.",
        ["storyIndex", "terms", "signs", "values", "total", "mode"],
        ["M_TERM_PRODUCT", "M_LEFT_TO_RIGHT"],
        ["What is repeated in the story, and what is added or taken once?",
         "Each repeated group is one times term; each extra or loss is one more term with its sign.",
         "Check the number in each term against the picture.",
         "The terms are built in place with their signs and values, and the total is shown; a new story follows."]),

    "bracket_sign": T(
        "tool_bracket_sign", "Bracket Signs", "manipulative",
        "A bracket after a plus sign can be dropped with the signs unchanged, a bracket after a minus sign flips every "
        "sign inside it, and the reason is what the bracket means: taking away a whole group.",
        "An expression with one bracket on a strip; a drop bracket button; tokens inside the bracket that turn over when "
        "a minus precedes it; a value check strip showing the value before and after removing the bracket; a fix it "
        "mode where a wrongly opened bracket is repaired.",
        ["Predict the signs that will appear when the bracket opens.",
         "Press drop bracket and watch the tokens and the signs.",
         "Compare the value before and after.",
         "Repair a bracket that was opened wrongly."],
        ["28 + (35 − 10) (signs stay, value 53).",
         "200 − (40 + 3) (signs flip, value 157).",
         "500 − (250 − 100) (signs flip, value 350).",
         "14 − (12 + 10) (value −8).",
         "Fix it: 500 − (250 − 100) opened as 500 − 250 − 100 (value 150, should be 350).",
         "Fix it: 27 − (8 − 3) opened as 27 − 8 − 3 (should be 27 − 8 + 3)."],
        ["After a minus, tokens that fail to flip are circled and the value check strip disagrees.",
         "After a plus, a flip is flagged because the value strip stops matching.",
         "A correct opening shows equal values before and after."],
        "All six brackets are opened or repaired and the before and after values match.",
        ["expression", "precedingSign", "tokens", "valueBefore", "valueAfter", "mode"],
        ["M_MINUS_BRACKET", "M_BRACKET_IGNORED"],
        ["Which sign comes right before the bracket?",
         "After a plus, nothing changes. After a minus, every sign inside turns over.",
         "Work out both forms and see whether the two values agree.",
         "The bracket opens with the right signs and the two values are shown equal; a new expression follows."]),

    "array_sharer": T(
        "tool_array_sharer", "Array Sharer", "manipulative",
        "A number multiplying a bracket multiplies every term inside it: a block of equal rows splits into two blocks "
        "or two blocks join, and the count stays the same.",
        "A grid of equal rows with a divider line that can sit anywhere; the two parts are coloured and labelled with "
        "their own times terms; the bracket form and the opened form are written under the grid; a difference mode that "
        "takes a coloured part away.",
        ["Drag the divider to split the rows into two parts.",
         "Read the two times terms and the bracket form together.",
         "Switch to difference mode and take a part away.",
         "Gather a common multiplier back into a bracket."],
        ["4 rows of 5 and 3 rows of 5 join into 7 rows of 5 (4 × 5 + 3 × 5 = (4 + 3) × 5 = 35).",
         "2 friends each with 43 and 24 (2 × (43 + 24) = 2 × 43 + 2 × 24 = 134).",
         "Split 6 columns of 8 into 4 and 2 columns (6 × 8 = 4 × 8 + 2 × 8 = 48).",
         "Difference mode: 14 rows of 10, take away 6 rows (14 × 10 − 6 × 10 = 8 × 10 = 80).",
         "Use 100 − 3 for 97 (97 × 25 = 100 × 25 − 3 × 25 = 2425).",
         "Gather: 9 × 12 + 9 × 8 into 9 × (12 + 8) = 180."],
        ["A split whose two parts do not join back to the whole is flagged.",
         "A multiplier applied to only one part is flagged with the count that goes missing.",
         "The bracket form and the opened form always show equal totals."],
        "All six arrangements are split or gathered and the totals agree.",
        ["rows", "columns", "dividerPosition", "terms", "bracketForm", "mode"],
        ["M_MULT_ONE_TERM"],
        ["How many equal rows or columns are there, and where does the divider sit?",
         "Each part gets its own times term, with the same multiplier.",
         "Add or take away the two parts and compare with the bracket form.",
         "The two parts, the bracket form and the opened form are shown with equal totals; a new grid follows."]),
}
