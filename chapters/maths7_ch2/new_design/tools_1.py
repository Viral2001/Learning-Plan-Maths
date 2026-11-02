# -*- coding: utf-8 -*-
"""Tool specs for modules M1 and M2 (comparing by gap, splitting into terms, reordering terms)."""
from topics_common import T

TOOLS = {
    "gap_comparer": T(
        "tool_gap_comparer", "Gap Comparer", "manipulative",
        "Two expressions can be compared by looking at how their numbers differ, without working either out: a bigger "
        "number being added gives a bigger value, a bigger number being taken away gives a smaller one.",
        "Two expressions side by side with each changed number highlighted; beside each changed number a small arrow "
        "showing whether it went up or down; a balance beam that tips toward the expression with the larger value; "
        "three buttons for less than, equal to and greater than; a Check by working out switch that stays locked "
        "until the student has committed to a choice.",
        ["Look at which numbers differ between the two expressions and by how much.",
         "Decide whether each change makes its expression bigger or smaller.",
         "Press less than, equal to or greater than before checking.",
         "Switch on Check by working out to see both values."],
        ["57 + 30 and 56 + 31 (equal, one more here and one less there).",
         "200 − 45 and 200 − 47 (the second takes away more, so it is smaller).",
         "18 × 6 and 18 × 7 (the second has one more lot of 18, so it is bigger).",
         "91 − 35 + 12 and 91 − 35 + 14 (the second is two more).",
         "40 + 25 and 41 + 24 (equal)."],
        ["A choice with no reason shown is accepted but asks which number changed and how.",
         "A wrong choice shows the highlighted change and the direction arrows again before the next try.",
         "A correct choice shows both values only after the student has committed."],
        "All five pairs are compared and each choice is committed before checking.",
        ["pairIndex", "changedNumbers", "directions", "choice", "checkOn"],
        ["M_EVALUATE_TO_COMPARE", "M_BIGGER_NUMBERS"],
        ["Which numbers are different in the two expressions?",
         "Ask whether each changed number is added or taken away, and whether it went up or down.",
         "Work out how much bigger or smaller each side becomes because of its change.",
         "The two changes are shown with arrows and the effect on each side; the choice is then confirmed and a new "
         "pair follows."]),

    "term_splitter": T(
        "tool_term_splitter", "Term Splitter", "manipulative",
        "An expression is a sum of terms: each term carries the sign in front of it, brackets and multiplications "
        "stay inside a term, and the terms are worked out one at a time.",
        "An expression written on a long strip; cut marks sit before each plus or minus that is not inside a bracket; "
        "dragging a cut splits the strip into labelled term cards that show their signs; each card has a value slot; "
        "a total slot at the end.",
        ["Predict where the expression should be cut into terms.",
         "Drag the cuts to the signs that separate terms; a sign inside a bracket refuses to cut.",
         "Type the value of each term card with its sign.",
         "Add the card values to get the value of the expression."],
        ["30 + 5 × 4 (terms 30 and 5 × 4, value 50).",
         "100 − (15 + 56) (terms 100 and −(15 + 56), value 29).",
         "13 − 2 + 6 (terms 13, −2 and 6, value 17).",
         "2 − 10 + 4 × 6 (terms 2, −10 and 4 × 6, value 16).",
         "5 × (3 + 2) + 7 × 8 + 3 (three terms, value 84).",
         "40 − 6 × 3 + 12 ÷ 4 (terms 40, −6 × 3 and 12 ÷ 4, value 25)."],
        ["A cut inside a bracket is refused with the bracket highlighted and the reason shown.",
         "A term card that loses its sign is flagged with the sign circled.",
         "The total slot opens only when every card has its correct value."],
        "All six expressions are split and evaluated by terms.",
        ["expression", "cuts", "termCards", "termValues", "total"],
        ["M_TERM_SIGN", "M_LEFT_TO_RIGHT", "M_TERM_PRODUCT"],
        ["Which signs separate the terms, and which sit inside a bracket?",
         "Cut before every plus or minus that is outside brackets, and keep the sign with the number after it.",
         "Work out each card by itself first, then add the card values.",
         "The cuts are shown in place, each card is filled with its signed value and the total is added; a new "
         "expression follows."]),

    "hop_reorder_line": T(
        "tool_hop_reorder_line", "Hop and Reorder", "manipulative",
        "Terms of a sum can be reordered and regrouped without changing the value as long as each term travels with "
        "its sign, and a good order makes the sum easy to add.",
        "A number line with a runner that hops once for each term; term cards in a row below, draggable into any order; "
        "bracket handles to group neighbouring cards; a running total that updates after each hop; a home mark showing "
        "the final position.",
        ["Predict the final position before moving any card.",
         "Drag the term cards into a new order and group two with a bracket.",
         "Watch the runner hop and see that the final position stays put.",
         "Find an order that is quick to add."],
        ["6 + (−4) and (−4) + 6 (final position 2 both ways).",
         "(−7) + 10 + (−11) (final position −8 in any order).",
         "47 + 18 + (−47) (group 47 and −47 first, value 18).",
         "25 + 38 + 75 (group 25 and 75 first, value 138).",
         "12 − 5 reordered as terms 12 and −5, then the card for 5 dragged without its sign (value jumps to −7 and is "
         "flagged).",
         "Five terms chosen by the student rearranged to a quick order."],
        ["A card dragged away from its sign is flagged and snaps back with the sign.",
         "The final position is shown in a fixed colour so that any reorder visibly lands on it.",
         "A quick order that groups cancelling or round terms is praised."],
        "All six cards are rearranged with the final position unchanged and kept to its sign.",
        ["cards", "order", "groups", "runningTotal", "finalPosition"],
        ["M_SWAP_ANYTHING", "M_TERM_SIGN"],
        ["Where will the runner finish for this order?",
         "Keep each sign with its number and move the whole card.",
         "Look for two cards that cancel or make a round number and group them first.",
         "The best order is shown with the grouped pair, the running total and the same final position; a new "
         "card set follows."]),
}
