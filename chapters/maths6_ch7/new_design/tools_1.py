# -*- coding: utf-8 -*-
"""Tool specs for module M1 (fractional units, parts of a whole, measuring, the number line). Doer tools only."""
from topics_common import T

TOOLS = {
    "equal_share": T(
        "tool_m1s1t2c1", "Equal Share Roti Dealer", "simulation",
        "When one whole is shared equally among n people, each share is the fractional unit 1/n, so more sharers "
        "means a smaller share.",
        "One round roti of fixed size; a sharer count stepper from 2 to 12; a Cut and Deal button that cuts the roti "
        "into equal pieces and deals one to each child; one share highlighted and labelled 1/n; a rail that always "
        "reads 1 whole.",
        ["Predict which share is bigger before cutting.",
         "Set the number of sharers and press Cut and Deal.",
         "Type the fraction for one share, or pick the bigger of two shares."],
        ["1 roti among 3 children: each share (1/3).",
         "1 kg of rice in 4 equal packets: each packet (1/4 kg).",
         "Which is bigger, 1/5 or 1/9 of the same roti? (1/5)",
         "3 glasses of juice among 4 friends: share each glass, then count (3/4 glass).",
         "A 1/2 kg fish and a 1/4 kg fish together (3/4 kg).",
         "Put in order: quarter, half, three quarters (1/4, 1/2, 3/4)."],
        ["Unequal cuts are not allowed: the tool always cuts equal pieces and shows the rail still reading 1 whole.",
         "A wrong bigger-share pick puts the two shares side by side so the smaller one is seen at once.",
         "A solved card shows the share with its fraction and the count of sharers."],
        "All six cards are solved.",
        ["sharers", "shareLabel", "answer", "cardIndex"],
        ["M_BIG_DENOM", "M_UNEQUAL_PARTS"],
        ["How many people share the one whole?",
         "One whole shared equally among n people gives each the fractional unit 1/n.",
         "Set the sharers to the number in the card and look at one share.",
         "The share is 1 over the number of sharers; the tool shows it and a similar card follows."]),

    "chikki_namer": T(
        "tool_m1s2t3c3", "Chikki Part Namer", "manipulative",
        "A piece is named as a fractional unit of the whole by counting how many equal copies of it fill the whole.",
        "A chikki drawn as 24 small squares, 6 across and 4 down, with a dashed ghost of the whole always behind; one "
        "piece is lifted off; a Stamp button lays copies of that piece across the whole, numbering each copy; a "
        "counter and a fraction read-out.",
        ["Guess how many copies of the piece fill the whole.",
         "Press Stamp to lay copies until the whole is filled.",
         "Type the piece's name as 1 over the count."],
        ["A 1 by 2 rectangle (1/12).", "A strip 1 square across and 4 down (1/6).",
         "A triangle that is half of a 3 by 4 block (1/4).", "A triangle that is half of a 3 by 2 block (1/8).",
         "A single small square (1/24).", "A 3 by 2 rectangle, then the L-shaped rest (1/4 and 3/4)."],
        ["If copies overlap or leave gaps, the tool shows the gap and the piece is not a fractional unit of that "
         "shape count.",
         "A wrong name shows the number of squares in the piece beside 24, the squares in the whole.",
         "A solved card shows the copies numbered across the whole and the fraction 1/n."],
        "All six pieces are named correctly.",
        ["pieceShape", "copiesLaid", "squaresInPiece", "answer", "cardIndex"],
        ["M_COUNT_PIECES", "M_UNEQUAL_PARTS"],
        ["How many small squares make the whole chikki?",
         "Count the squares in the piece; a triangle is half of its rectangle.",
         "Divide 24 by the squares in the piece to count the copies.",
         "The piece is 1 over that count; the copies are shown and a similar piece follows."]),

    "strip_measurer": T(
        "tool_m1s2t4c5", "Folding Strip Builder", "manipulative",
        "A fraction is made by collecting copies of a fractional unit: k copies of 1/n is k/n.",
        "A paper strip one unit long; a Fold button that halves every part or a fold count from 2 to 12; blocks of "
        "one part that drop in from the left, numbered as they land; hollow dashed parts still empty; a read-out "
        "k × 1/n = k/n.",
        ["Fold the strip into equal parts.",
         "Add blocks one at a time from the left.",
         "Type the fraction the blocks make."],
        ["Fold in 2, then in 2 again: name each part (1/4).", "3 blocks of 1/8 (3/8).",
         "Make 1/3, then fold again to make 1/6.", "5 blocks of 1/4: how many wholes and how much more (1 + 1/4).",
         "9 blocks of 1/4 (2 + 1/4).", "7 blocks of 1/2 (7/2, which is 3 + 1/2)."],
        ["Counting fold lines instead of blocks shows the blocks numbered beside the creases, so the difference is "
         "seen.",
         "Past one whole a second strip appears, so 5/4 shows one full strip and one block more.",
         "A solved card shows the addition statement, for example 1/4 + 1/4 + 1/4 = 3 × 1/4 = 3/4."],
        "All six cards are solved.",
        ["parts", "blocks", "wholes", "answer", "cardIndex"],
        ["M_COUNT_PIECES", "M_LESS_THAN_ONE"],
        ["What is one part of the strip called?",
         "Count the blocks laid, not the folds.",
         "Write the count of blocks over the number of equal parts.",
         "The blocks are numbered and the fraction k/n is shown; a similar card follows."]),

    "number_line_marker": T(
        "tool_m2s3t5c7", "Number Line Marker", "manipulative",
        "On the number line the unit from 0 to 1 is cut into equal gaps; the fraction k/n is k gaps of 1/n from 0.",
        "A number line from 0 to 2; a parts stepper from 2 to 10 that cuts every unit into equal gaps, each gap "
        "shaded as a band; a Hop button that hops one gap at a time from 0; a draggable point; a fraction box.",
        ["Choose how many equal parts one unit has.",
         "Hop from 0, counting gaps.",
         "Type the fraction for the point, or tap the line where a fraction belongs."],
        ["Mark 1/2 with each unit in 2 parts.", "Mark 2/3 with each unit in 3 parts.",
         "Write the lengths ending at the 2nd and 4th marks of fifths (2/5, 4/5).",
         "Draw 3/10 and 4/5 (4/5 is at the same point as 8/10).",
         "Halves: the line ending halfway between 1 and 2 (3/2).",
         "Fifths: the four marks between 1 and 2 (6/5, 7/5, 8/5, 9/5)."],
        ["Counting tick marks from 0 shows the marks numbered against the gaps, so the extra count is seen.",
         "A point in the wrong gap is shown with its own fraction beside the target.",
         "A solved card shows the hops as arcs and the fraction under the point."],
        "All six cards are solved.",
        ["partsPerUnit", "hops", "point", "answer", "cardIndex"],
        ["M_TICKS_NOT_GAPS", "M_LESS_THAN_ONE"],
        ["How many equal gaps is 0 to 1 cut into?",
         "The bottom number is the gaps in one unit; the top number is how many gaps from 0.",
         "Hop that many gaps from 0, counting past 1 if needed.",
         "The point is shown with its hops and fraction; a similar card follows."]),
}
