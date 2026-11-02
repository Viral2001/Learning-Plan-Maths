# -*- coding: utf-8 -*-
"""Tool specs for the first two modules' tenth and hundredth topics (T2, T4, T5)."""
from topics_common import T

TOOLS = {
    "equal_part_scale_splitter": T(
        "tool_equal_part_scale_splitter", "Equal Part Scale Splitter", "manipulative",
        "When a length falls between two whole marks, splitting the unit into 10 equal parts gives tenths, and the "
        "length is read as whole units plus tenths, or as a count of tenths.",
        "A ruler from 0 to 6 units with a unit strip that splits into 2, 4, 5 or 10 equal parts; an object strip "
        "that the student drags along the ruler; two answer boxes, one for the mixed form and one for the count of "
        "tenths; a row of length cards that can be dragged into increasing order.",
        ["Drag the object along the ruler and note the two whole marks it lies between.",
         "Split the unit into 10 equal parts and count the parts after the lower mark.",
         "Write the length as units and tenths, then as a count of tenths.",
         "Drag the length cards into increasing order."],
        ["A bolt ending 3 parts after the 4 mark (4 3/10 or 43/10).",
         "A strip ending 9 parts after the 0 mark (9/10).",
         "A ribbon that is 34 tenths long (3 4/10).",
         "Three straws at 2 7/10, 3 2/10 and 2 4/10 placed in increasing order (2 4/10, 2 7/10, 3 2/10).",
         "Read 4/10, 41/10, 4 1/10 and 41 1/10 and name the two that are equal (41/10 and 4 1/10).",
         "Order 9/10, 1 7/10, 130/10 and 13 1/10 (9/10, 1 7/10, 130/10, 13 1/10)."],
        ["A split into 4 parts is shown beside the split into 10, so the part sizes can be compared.",
         "Reading the parts count as the whole number is flagged: 7 parts after the 2 mark is not 7 units.",
         "A tenths count that does not match the mixed form is shown on the strip, ten parts to each unit."],
        "Six lengths are read in both forms and the last two sets are in the correct order.",
        ["objectLength", "splitCount", "lowerMark", "partsAfter", "mixedForm", "tenthsCount", "cardIndex"],
        ["M_PART_AS_UNIT", "M_BIGGER_DENOMINATOR"],
        ["Which two whole marks is the object between?",
         "Split the unit into 10 equal parts and count the parts after the lower mark.",
         "The length is the lower mark plus that many tenths; ten tenths make one unit, so also count all tenths.",
         "The ruler shows the length in both forms; a similar card follows."]),

    "hundredth_cell_zoom_grid": T(
        "tool_hundredth_cell_zoom_grid", "Hundredth Cell Zoom Grid", "manipulative",
        "Splitting each tenth into 10 equal parts gives hundredths, so a unit has 100 parts and a length can be read "
        "as units, tenths and hundredths, or as a count of hundredths.",
        "A strip of one unit split into 10 tenths; a zoom button that opens any tenth into 10 hundredths; a second "
        "strip for the next unit; a read-out showing units, tenths and hundredths and the same length as a count of "
        "hundredths; four length cards to place on the strips.",
        ["Press the zoom button on the tenth where the length ends.",
         "Count the tenths, then the hundredths after them.",
         "Read the length as units, tenths and hundredths.",
         "Read it again as a count of hundredths."],
        ["A wire ending 4 hundredths after 1 1/10 (1 1/10 4/100, which is 1 14/100 or 114/100).",
         "A paper that is 8 9/10 long, folded in half (4 4/10 5/100).",
         "A length of 55/100 (5 tenths and 5 hundredths).",
         "A length of 202/100 (2 2/100).",
         "Which is longer, 3/10 or 33/100 or 3/100 (33/100 is longest, 3/100 is shortest)?",
         "A ruler reading of 5 37/100."],
        ["A hundredth placed in the tenths column is shown as a part too big: ten hundredths make one tenth.",
         "Counting all the small parts but forgetting the tenths is shown by filling the tenths first.",
         "A correct reading lights the units, tenths and hundredths in three colours."],
        "Six lengths are placed and each is read in both forms.",
        ["lengthHundredths", "zoomedTenth", "unitsRead", "tenthsRead", "hundredthsRead", "cardIndex"],
        ["M_BIGGER_DENOMINATOR", "M_PART_AS_UNIT"],
        ["Which tenth does the length end in?",
         "Zoom into that tenth: it is split into 10 equal hundredths.",
         "Count the whole tenths first, then the hundredths in the tenth you opened.",
         "The strip lights the units, tenths and hundredths and gives the count of hundredths; a similar card follows."]),

    "carry_and_break_bench": T(
        "tool_carry_and_break_bench", "Two Level Carry and Break Bench", "manipulative",
        "Adding and subtracting amounts in units, tenths and hundredths works place by place: ten hundredths regroup "
        "to one tenth and ten tenths to one unit when adding, and one unit breaks into ten tenths and one tenth into "
        "ten hundredths when subtracting.",
        "A bench with three trays for units, tenths and hundredths holding counters for two amounts; buttons to "
        "Combine two trays, Carry ten counters up one tray, and Break one counter down into ten in the tray below; "
        "the matching written column beside the bench.",
        ["Set the two amounts on the bench.",
         "Combine or take away in the hundredths tray first, then tenths, then units.",
         "Carry up or break down when a tray has ten or more, or too few.",
         "Read the answer from the trays and check it against the written column."],
        ["15 3/10 4/100 + 2 6/10 8/100 (18 2/100).",
         "25 9/10 − 6 4/10 7/100 (19 4/10 3/100).",
         "15 3/10 4/100 − 2 6/10 8/100 (12 6/10 6/100).",
         "9 5/10 7/100 + 2 1/10 3/100 (11 7/10).",
         "7 7/100 − 4 4/100 (3 3/100).",
         "12 6/10 2/100 − 9/10 9/100 (11 63/100)."],
        ["Adding the denominators is shown with the counters: ten hundredths still make one tenth.",
         "A missed carry shows ten or more counters left in one tray.",
         "A subtraction that takes the bigger number from the smaller in a tray is blocked until a Break is made."],
        "Six additions and subtractions are finished with every carry and break shown.",
        ["amountA", "amountB", "hundredthsTray", "tenthsTray", "unitsTray", "carries", "breaks", "cardIndex"],
        ["M_ADD_DENOMINATORS", "M_BORROW_ONE", "M_POINT_ALIGN"],
        ["Which tray do you work on first?",
         "Ten counters in a tray make one counter in the next tray up.",
         "If a tray cannot give enough, break one counter from the tray above into ten here.",
         "The bench makes the carry or break and the written column follows; a similar card comes next."]),
}
