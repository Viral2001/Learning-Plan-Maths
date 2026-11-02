# -*- coding: utf-8 -*-
"""Tool specs for module M3: token_board, token_taker. Doer tools only."""
from topics_common import T

TOOLS = {
    "token_board": T(
        "tool_m3s1t9c3", "Token Board", "manipulative",
        "A green token and a red token cancel to zero, so a sum is what is left after the zero pairs go.",
        "A board with a green token tray (+1) and a red token tray (−1); a Cancel Pairs button that removes one "
        "green and one red token; a total readout.",
        ["Predict the total.",
         "Drag green and red tokens onto the board.",
         "Press Cancel Pairs and read what is left."],
        ["(+5) + (−3) (+2).", "(+4) + (−7) (−3).", "(−6) + (+6) (0).", "(−5) + (−2) (−7).",
         "(+8) + (−3) + (−4) (+1).", "Show −3 with five tokens (4 red and 1 green)."],
        ["A zero pair that is not cancelled is shown with a dashed link so the cancel is seen.",
         "A wrong total shows the tokens left on the board.",
         "A solved card shows the sum with the zero pairs shaded."],
        "All six cards are right.",
        ["greenCount", "redCount", "pairsCancelled", "answer", "cardIndex"],
        ["M_TOKEN_COUNT", "M_IGNORE_SIGN", "M_ZERO_PAIR_CHANGES"],
        ["What does a green token and a red token make together?",
         "Pair each green token with a red token; pairs make zero.",
         "Count the tokens that have no partner and read their colour.",
         "The zero pairs are shaded; a similar card follows."]),

    "token_taker": T(
        "tool_m3s2t10c4", "Token Taker", "manipulative",
        "To subtract, take tokens away, and when there are not enough of the kind to take, add zero pairs first.",
        "A board of green and red tokens; a Take Away area for the tokens to remove; an Add Zero Pair button that "
        "adds one green and one red token; a total readout.",
        ["Predict the result.",
         "Add zero pairs if tokens are missing.",
         "Drag the tokens to Take Away and read what is left."],
        ["(+5) − (+4) (+1).", "(−7) − (−5) (−2).", "(+5) − (+6) (−1).", "(+4) − (−6) (+10).",
         "(−3) − (+2) (−5).", "(−2) − (−6) (+4)."],
        ["Not enough tokens: the Take Away area shows how many are missing and the button glows.",
         "A zero pair added is shown to leave the total unchanged.",
         "A solved card shows the pairs added and the tokens taken."],
        "All six cards are right.",
        ["greenCount", "redCount", "pairsAdded", "answer", "cardIndex"],
        ["M_ZERO_PAIR_CHANGES", "M_SUB_NEG_SMALLER", "M_SUB_SMALLER"],
        ["Are there enough tokens of the kind you must take away?",
         "If not, add zero pairs; they do not change the total.",
         "Add the number of zero pairs you need, then take the tokens away.",
         "The zero pairs and the taken tokens are shown; a similar card follows."]),
}
