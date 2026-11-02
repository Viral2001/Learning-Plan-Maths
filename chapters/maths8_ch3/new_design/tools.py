# -*- coding: utf-8 -*-
"""Tool specs for Class 8 Chapter 3 (A Story of Numbers). Nine tools, each used once at a practice concept.
roman_builder, base_builder, abacus, stick_matcher, gumulgal_builder, egypt_board and base60_board are new
specs. zero_breaker and system_sorter are placeholders: build.py
swaps the node built from each for a copy of the live v29 node named in live_tools.json (Zero Placeholder Breaker
and Numeral System Sorter), so their specs describe those live tools."""
from topics_common import T

TOOLS = {
    "roman_builder": T(
        "tool_m2s1t4c5", "Roman Numeral Builder", "simulation",
        "A Roman numeral groups a number into landmark numbers 1, 5, 10, 50, 100, 500, 1000, largest first, and adds "
        "their values. A smaller symbol written before a larger one is subtracted, so IV is 4 and XC is 90.",
        "A target number at the top, a tray of landmark tiles I, V, X, L, C, D and M, a build row where tiles are "
        "placed left to right, and a running total under the row that updates as each tile is placed.",
        ["Read the target number and split it into thousands, hundreds, tens and ones.",
         "Drag landmark tiles into the build row, largest first.",
         "Use a subtractive pair such as CM, XC or IV where four of a symbol would be needed.",
         "Check the running total against the target and read the finished numeral back."],
        ["Build 1222 from landmark tiles.",
         "Build 2999 using subtractive pairs.",
         "Build 302 and 715.",
         "Read MMCCCLXVII back as a number.",
         "Add CCXXXII and CCCCXIII by joining tiles and regrouping.",
         "Which is greater, CDXC or CCCC? Build both and compare totals."],
        ["A wrong total shows each tile's value under it, so the stray tile is easy to see.",
         "Four of the same tile in a row is flagged and the subtractive pair is suggested.",
         "A subtractive pair that the Romans did not use, such as IC, is rejected with the reason."],
        "All six cards are done with each built numeral matching its target.",
        ["target", "tiles", "runningTotal", "cardIndex"],
        ["M_ROMAN_PLACE", "M_ROMAN_ADD_DIGITS"],
        ["Which landmark numbers fit inside the target?",
         "Start with the largest landmark that fits and take it away.",
         "Repeat with what is left, using a pair like XC where four symbols would be needed.",
         "The numeral is built tile by tile with the total shown, then a new card follows."]),

    "base_builder": T(
        "tool_m2s1t6c3", "Base Grouping Builder", "simulation",
        "In a base-n system every n of one landmark are traded for one of the next landmark, so the landmarks are 1, "
        "n, n², n³ and so on, and no landmark is used n or more times.",
        "A base selector (2 to 10), a pile of loose unit counters, and a row of landmark bins labelled 1, n, n², n³. "
        "Grouping n counters in one bin fuses them into one counter in the next bin. A readout shows the number as "
        "counts of each landmark.",
        ["Choose the base and read the landmark numbers it gives.",
         "Pour the target number of unit counters into the 1s bin.",
         "Group n counters at a time and push each group into the next bin.",
         "Stop when every bin holds fewer than n counters, and read the counts."],
        ["In base 5, group 89 counters and read the counts.",
         "In base 5, show 15, 50 and 137.",
         "In base 3, group 50 counters.",
         "In base 2, group 19 counters.",
         "In base 5, show 651: which bin needs the wave?",
         "Why can no bin keep 5 counters in base 5?"],
        ["A bin holding n or more counters glows and asks for a group to be made.",
         "A wrong read shows each bin's count times its landmark and the total.",
         "Changing the base resets the bins and shows the new landmarks."],
        "All six cards are done with every bin below the base.",
        ["base", "bins", "target", "cardIndex"],
        ["M_BASE_TEN_ONLY", "M_TEN_SYMBOLS_OK"],
        ["What are the landmark numbers in this base?",
         "How many counters make one counter in the next bin?",
         "Keep grouping until every bin has fewer than the base.",
         "The counters are grouped and the counts read out, then a new card follows."]),

    "abacus": T(
        "tool_m2s1t7c5", "Column Regrouping Board", "simulation",
        "Adding on a counting board puts counters for both numbers in the same columns; 10 counters in a column are "
        "traded for 1 in the next column, so adding in a base needs only regrouping. Multiplying by 10 moves every "
        "counter one column to the left.",
        "A board with columns for 1s, 10s, 100s, 1000s and 10000s, two colours of counters for the two numbers, and "
        "a regroup button that trades 10 counters in a column for one in the next.",
        ["Place counters for the first number in the columns.",
         "Place counters for the second number in a second colour.",
         "Trade every 10 counters in a column for 1 in the column to the left.",
         "Read the sum from the columns, and try multiplying by 10 by shifting every counter left."],
        ["Show 3426 on the board.",
         "Add 87 and 78 and regroup.",
         "Add 9608 and 507.",
         "Add 1080 and 46.",
         "Multiply 522 by 10 by shifting the counters.",
         "Why does the sum never need more than 9 counters in a column?"],
        ["A column with 10 or more counters is highlighted until it is regrouped.",
         "A wrong reading shows the count in each column times its landmark.",
         "A shift that misses a column is undone with the column named."],
        "All six cards are done with every column holding at most 9 counters.",
        ["columns", "addendA", "addendB", "cardIndex"],
        ["M_TEN_SYMBOLS_OK", "M_LANDMARK_PRODUCT"],
        ["Which column does each digit go in?",
         "Count the counters in each column after both numbers are placed.",
         "Trade 10 counters in a column for 1 in the next column.",
         "The counters are regrouped and the sum read off, then a new card follows."]),

    "zero_breaker": T(
        "tool_m4s1t5c10", "Zero Placeholder Breaker", "simulation",
        "In a place value system the place of a digit gives its value, so an empty place must be held open. Leaving "
        "a column empty removes it and every digit to its left loses a place; a 0 holds the place and adds nothing.",
        "A row of labelled place value columns with a digit tile tray beneath, a readout of the number the board "
        "actually reads, and a short number line under the readout.",
        ["Read the number the class meant to write.",
         "Place digit tiles in the columns, leaving a column empty where there is no digit.",
         "Read what the board actually shows when the empty column collapses.",
         "Put a 0 tile in the empty column and read the board again."],
        ["Write 305 with the tens column left empty: what does the board read?",
         "Put a 0 in the tens column and read 305 again.",
         "Write 5072: which column needs a 0?",
         "Write 4000: are the trailing zeros needed?",
         "Does 7 need a zero anywhere?",
         "Write 2005 and say how many zeros hold places."],
        ["A collapsed board shows the meant number and the read number on the number line.",
         "A missing 0 tile is pointed to by the column it should fill.",
         "A 0 placed before the first digit is shown to change nothing."],
        "All six cards are done with every board reading the number that was meant.",
        ["columns", "meant", "reads", "cardIndex"],
        ["M_BLANK_NOTHING", "M_ZERO_NOTHING"],
        ["Which columns lie between the first digit and the last?",
         "Is any of those columns empty?",
         "An empty column collapses: put a 0 there to hold it open.",
         "The 0 is placed and the board reads the meant number, then a new card follows."]),

    "system_sorter": T(
        "tool_m1s2t2c2", "Numeral System Sorter", "simulation",
        "Numeral systems differ in two independent ways: whether a symbol's place decides its value, and whether a "
        "symbol holds an empty place. Column arithmetic needs both, which is why the Hindu system makes long addition "
        "easy.",
        "A sorting table with a two by two grid: positional or not across the top, a zero symbol or not down the side. "
        "Cards show the same number written in different systems and are dropped into a cell.",
        ["Read the number written on the card in its own system.",
         "Decide whether place decides value in that system.",
         "Decide whether it has a symbol for an empty place.",
         "Drop the card into its cell and say which property helps column addition."],
        ["Sort a Roman numeral card.",
         "Sort an Egyptian numeral card.",
         "Sort a Mesopotamian numeral with a blank.",
         "Sort a Mayan numeral with a shell.",
         "Sort a Chinese rod numeral.",
         "Sort a Hindu numeral and say why column addition is easiest there."],
        ["A card in the wrong cell shows the same symbol in two places to test the positional property.",
         "A wrong zero call shows a number with an empty place in that system.",
         "Changing the system is shown to change the writing and never the quantity."],
        "All six cards are sorted with a reason given for each.",
        ["cards", "grid", "cardIndex"],
        ["M_POSITION_SAME", "M_ZERO_NOTHING"],
        ["Does the same symbol mean different amounts in different places?",
         "How would this system write a number with an empty place?",
         "Positional and a zero symbol are separate questions: answer both.",
         "The card is placed in its cell with the reason shown, then a new card follows."]),

    "stick_matcher": T(
        "tool_m1s1t2c4", "Stick Matching Board", "simulation",
        "Counting without number names is a one-to-one mapping: every object is paired with exactly one stick, and "
        "the sticks left without a partner show what is missing, who has more and how many more are needed. Adding, "
        "subtracting, multiplying and dividing sticks are joining, pairing off, repeating and sharing out.",
        "A herd of cows in a row, a pile of sticks beside it, and a second herd or pile for comparing. A stick is "
        "dragged onto a cow to pair them, and a pair is drawn as a line. Unpaired cows and sticks glow, and no "
        "number is printed anywhere until the student has made the pairing.",
        ["Look at the two collections and predict which has more before pairing anything.",
         "Drag one stick onto each cow, never two sticks onto one cow.",
         "Look at what is left without a partner and say what it means.",
         "Join, pair off, repeat or share out piles of sticks to carry out an operation."],
        ["In the morning 8 sticks are kept, one for each cow. In the evening 6 cows return and each takes out one "
         "stick. How many cows are still missing?",
         "Herd A has 9 cows and herd B has 6 cows. Pair them: which herd has more, and how many more cows does the "
         "other need to match it?",
         "Two herds each have 7 cows. Pair them and say what is left over.",
         "Add a pile of 4 sticks and a pile of 5 sticks by joining them. How many sticks are in the joined pile?",
         "Subtract 3 sticks from a pile of 8 by pairing and taking away the pairs. How many sticks are left?",
         "Multiply by repeating a pile of 3 sticks once for each of 4 sticks. How many sticks are there in all?",
         "Divide a pile of 13 sticks into groups of 4. How many full groups are there and how many sticks are left?"],
        ["A stick dropped on a cow that already has one is returned with the message that each cow gets one stick.",
         "Unpaired sticks and cows glow so the leftover can be seen before any number is said.",
         "A wrong answer shows the pairing again with the leftover sticks counted off one at a time."],
        "All seven cards are done with every pairing one to one and the leftover read correctly.",
        ["cows", "sticks", "pairs", "cardIndex"],
        ["M_COUNT_NEEDS_NAMES", "M_SYSTEM_ENDLESS"],
        ["Which collection has an object with no partner yet?",
         "Pair one stick with one cow and see what is left over.",
         "Count only the unpaired ones: they answer the question.",
         "The pairing is completed and the leftover is shown, then a new card follows."]),

    "gumulgal_builder": T(
        "tool_m1s1t3c4", "Gumulgal Name Builder", "simulation",
        "The Gumulgal counted in twos: ukasar is 2 and urapon is 1, so a number name is as many ukasars as fit and "
        "one urapon if 1 is left over. Counting in groups of one size shortens a long row of marks, and the same "
        "word can be repeated to extend the names past 6.",
        "Two tiles, ukasar worth 2 and urapon worth 1, a name row where tiles are placed left to right, and a "
        "count strip under the row that shows how many objects the name stands for once the row is complete.",
        ["Read the number the card asks for and split it into twos and at most one extra one.",
         "Drag ukasar tiles into the name row, then an urapon tile if one is left over.",
         "Read a finished name back by counting 2 for each ukasar and 1 for each urapon.",
         "Join or take away tiles to add and subtract numbers written in names."],
        ["Build the name for 3.",
         "Build the names for 5 and 6.",
         "Try to build 7 with the original Gumulgal words and say what the Gumulgal would call it.",
         "Read ukasar-ukasar-ukasar-ukasar-urapon as a number.",
         "Extend the names to build 9 and 12.",
         "Add ukasar-ukasar-ukasar-ukasar-urapon and ukasar-ukasar-ukasar-urapon, and say how many times ukasar is "
         "written in the answer.",
         "Subtract ukasar-ukasar-ukasar from ukasar-ukasar-ukasar-ukasar-urapon."],
        ["A name with two urapons in a row is flagged because two 1s make one ukasar.",
         "A wrong name shows its tiles counted as 2s and 1s next to the number that was asked for.",
         "A name for a number above 6 in the original system is shown as ras, and the extended name is offered."],
        "All seven cards are done with every name matching its number.",
        ["tiles", "target", "nameRow", "cardIndex"],
        ["M_BASE_TEN_ONLY"],
        ["How many twos fit in the number on the card?",
         "Use ukasar for each 2, and add urapon only if 1 is left over.",
         "Check by counting 2 for each ukasar and 1 for each urapon.",
         "The tiles are placed and the count shown, then a new card follows."]),

    "egypt_board": T(
        "tool_m2s1t5c3", "Egyptian Symbol Board", "simulation",
        "An Egyptian numeral is a count of each landmark symbol: stroke 1, heel 10, coil 100, lotus 1000, finger "
        "10000. A symbol keeps its value wherever it is drawn, no symbol is drawn 10 or more times, and ten of one "
        "symbol are traded for one of the next.",
        "A tray of landmark symbols with their values, a drawing area where symbols are dropped in any order, a "
        "count under each symbol, and a running total. Ten of one symbol in the drawing area glow and offer a trade "
        "for the next symbol.",
        ["Read the number and split it into thousands, hundreds, tens and ones.",
         "Drag the right number of each symbol into the drawing area.",
         "Trade ten of a symbol for one of the next symbol when ten appear.",
         "Read a drawn numeral back by adding the values of all its symbols."],
        ["Draw 324.",
         "Draw 2153.",
         "Draw 1023: which landmark has no symbols?",
         "Draw 10458.",
         "Read 2 coils, 7 heels and 6 strokes as a number.",
         "Read 4 lotuses, 3 coils, 2 heels and 2 strokes as a number.",
         "Drop 12 heels and trade until no symbol is drawn 10 times. What numeral is left?"],
        ["Ten or more of one symbol glow until the trade is made.",
         "Moving the symbols around is shown to leave the total unchanged.",
         "A wrong total shows each symbol's count times its value added up."],
        "All seven cards are done with no symbol drawn 10 or more times and every total matching its card.",
        ["symbols", "counts", "total", "cardIndex"],
        ["M_TEN_SYMBOLS_OK"],
        ["Which landmark symbols fit inside the number?",
         "Take as many of the largest symbol as fit, then move down to the next.",
         "Add the values of the symbols to check the total against the card.",
         "The symbols are placed and the total shown, then a new card follows."]),

    "base60_board": T(
        "tool_m3s1t8c4", "Base 60 Place Board", "simulation",
        "In the Mesopotamian system the numbers are grouped in powers of 60, so the places are 1s, 60s and 3600s, "
        "each count is from 1 to 59, and the position of a count tells its landmark. An empty place was left blank, "
        "and 60 of one landmark are regrouped into one of the next.",
        "Three place columns labelled 1s, 60s and 3600s with the landmark symbols hidden, a count box in each "
        "column, a total readout, and a regroup button that trades 60 in a column for 1 in the column to its left.",
        ["Predict how many 3600s, 60s and 1s the number holds.",
         "Set the count in each column, leaving a column empty when it has no count.",
         "Regroup any column whose count reaches 60.",
         "Read the places left to right with a bar between them and check the total."],
        ["Show 63 on the board.",
         "Show 132 on the board.",
         "Show 200 on the board.",
         "Show 60: which place stays empty?",
         "Show 3605: which place stays empty?",
         "Show 7530 on the board.",
         "Regroup 2 | 75 | 10 so that no count is 60 or more, and check that the total is still 11710."],
        ["A count of 60 or more glows until it is regrouped.",
         "An empty place that is removed shows the numeral sliding left and reading a smaller number.",
         "A wrong total shows each count times its place value added up."],
        "All seven cards are done with every count from 1 to 59 and every total matching its card.",
        ["columns", "counts", "total", "cardIndex"],
        ["M_POSITION_SAME", "M_BLANK_NOTHING", "M_TEN_SYMBOLS_OK"],
        ["Which landmarks are 1, 60 and 3600, and how many of the biggest one fit?",
         "Take as many 3600s as fit, then as many 60s, and what is left is the 1s.",
         "Check that no column holds 60 or more, and leave a column empty if it has nothing.",
         "The counts are set and the total shown, then a new card follows."]),
}
