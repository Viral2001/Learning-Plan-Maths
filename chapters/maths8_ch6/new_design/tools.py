# -*- coding: utf-8 -*-
"""Tool specs for Class 8 Chapter 6 (We Distribute, Yet Things Multiply). One tool per doer that has one, each
used once.

Five are carried over from the live built tools of maths8_ch6_live_v25 (see live_tools.json and build.py's
carry-over step): the spec below is only the local placeholder that build_tool_node needs; build.py replaces each
node with a copy of the live node (new id, concept_id and home_concept_id kept). The sixth, pattern_regrouper, is
new and stays a placeholder until it is built.

Four more new placeholder tools raise the chapter to ten: neighbour_digit_adder (the open doer of Fast
Multiplication) and square_of_difference (the open doer of The Square of a Difference), then two second tools
on teaching concepts whose idea is itself a manipulation, difference_of_squares_slide (T7.C2, cut and slide a
piece) and four_rectangles_square (T9.C2, one area two ways); the last two are attached with A(tool=...)."""
from topics_common import T

TOOLS = {
    "distributive_area": T(
        "tool_c8dm_distributive_area", "Distributive Area", "simulation",
        "A product ab is a rectangle of a rows and b columns; splitting the columns into b and c splits the "
        "rectangle into ab and ac, so a(b + c) = ab + ac, and adding one column adds a whole column of a.",
        "A dot rectangle with a rows and b + c columns, a draggable divider between the b columns and the c "
        "columns, the two part areas and their sum, and number fields for a, b and c.",
        ["Set a, b and c.",
         "Drag the divider and watch the two part areas change while the total stays fixed.",
         "Add one column or one row and read the increase.",
         "Answer a card by writing the two parts."],
        ["Show 23 × 28 as 23 × 27 plus one more column and say the increase.",
         "Increase the rows by 1 instead and say the increase.",
         "Increase both by 1 and find the extra corner dot.",
         "Increase one by 1 and decrease the other by 1 and say whether the product grows.",
         "Find a pair for which that change makes the product smaller.",
         "Write a(b + c) as two parts for a = 7, b = 5, c = 3."],
        ["The divider lights the two parts with their areas written in them.",
         "An answer that adds only c is shown with the missing a − 1 rows of the strip.",
         "The extra corner dot flashes when both numbers grow."],
        "All six cards are done and the both-grow card has been explained with the corner dot.",
        ["a", "b", "c", "divider", "cardIndex"],
        ["M_DISTRIBUTE_FIRST_ONLY", "M_PRODUCT_INCREASE"],
        ["What are the rows and what are the columns of this rectangle?",
         "Split the columns into two groups and find each part separately.",
         "One more column of 23 rows adds 23, so 23 × 28 = 621 + 23 = 644.",
         "The two parts are shown with their areas, and a similar card follows."]),

    "binomial_tiles": T(
        "tool_c8dm_binomial_tiles", "Binomial Tile Multiplier", "simulation",
        "The product (a + m)(b + n) is a rectangle split into four parts, ab, an, mb and mn, one for each pair of "
        "terms; with a minus sign a part is taken away, and like parts are collected into one term.",
        "A rectangle whose sides are split into a and m, and b and n, four coloured regions with their products, a "
        "sign switch for each added piece, and a tray where tiles of the same kind are stacked.",
        ["Choose the two brackets.",
         "Read the four regions and drag each product to the tray.",
         "Stack like tiles and read the simplified expression.",
         "Switch a sign and watch the region become a part taken away."],
        ["Multiply (a + 2)(b + 5) and name all four parts.",
         "Multiply (a − 2)(b + 3) and say which parts are taken away.",
         "Multiply (a − 3)(b − 4) and say why +12 appears.",
         "Multiply (3 + u)(v − 3).",
         "Multiply (a + b)(a + b) and stack the like tiles.",
         "Multiply (4y + 7)(y + 11z − 3) and count the parts before collecting."],
        ["A product with only two parts is shown with the two missing regions lit.",
         "A sign error is shown by the region turning from added to taken away.",
         "Like tiles snap together; unlike tiles refuse to stack."],
        "All six cards are done with every part placed and like tiles collected.",
        ["left", "right", "regions", "tray", "cardIndex"],
        ["M_TWO_TERMS_ONLY", "M_SIGN_DISTRIBUTE", "M_UNLIKE_ADD"],
        ["How many terms are in each bracket, and so how many parts will there be?",
         "Multiply each term of the first bracket by each term of the second.",
         "For (a − 2)(b + 3): ab + 3a − 2b − 6, because (−2) × 3 = −6.",
         "All the parts are shown with their signs, and a similar card follows."]),

    "square_of_sum": T(
        "tool_c8dm_square_of_sum", "Square Of Sum Tiles", "simulation",
        "A square of side a + b is made of a square a², a square b² and two rectangles ab, so (a + b)² = a² + 2ab "
        "+ b², which is more than a² + b² whenever ab is positive.",
        "A square whose side is split into a and b, the four tiles with their areas, a toggle that overlays the "
        "wrong picture a² + b² with its two empty gaps, and number fields for a and b.",
        ["Set a and b.",
         "Drag the four tiles into the big square.",
         "Toggle the wrong picture and see the gaps.",
         "Answer a card by writing the four tile areas."],
        ["Find 65² as (60 + 5)².",
         "Find 104² as (100 + 4)².",
         "Find 37² by splitting 37 into two easy parts.",
         "Show why (a + b)² is bigger than a² + b² for positive a and b.",
         "Expand (6x + 5)².",
         "Expand (3j + 2k)²."],
        ["An answer of a² + b² is shown with the two empty ab gaps.",
         "Each tile prints its own area when placed.",
         "The two rectangles light together to show 2ab."],
        "All six cards are done and the wrong picture has been compared once.",
        ["a", "b", "tiles", "overlay", "cardIndex"],
        ["M_SUM_SQUARE"],
        ["What are the two parts of the side?",
         "The big square is made of two squares and two equal rectangles.",
         "For 104²: 100² + 2 × 100 × 4 + 4² = 10000 + 800 + 16 = 10816.",
         "The four tiles are shown with their areas, and a similar card follows."]),

    "identity_generaliser": T(
        "tool_c8dm_identity_generaliser", "Identity Generaliser", "simulation",
        "A pattern seen in a few numbers becomes a statement about all numbers only when it is written with "
        "letter-numbers and expanded; then it holds for negative integers and fractions too.",
        "A table of number cases for a pattern, a row where the student writes the general statement with a and "
        "b, an expand button, and fields to test any integer or fraction.",
        ["Read the number cases of the pattern.",
         "Write the general statement with letter-numbers.",
         "Expand both sides and compare.",
         "Test the statement with a negative number and a fraction."],
        ["Write the pattern 2(2² + 1²) = 3² + 1² in general.",
         "Write the pattern 9 × 9 − 1 × 1 = 10 × 8 in general.",
         "Expand both sides of 2(a² + b²) = (a + b)² + (a − b)².",
         "Test the difference of squares with a = −5, b = 2.",
         "Test it with a = 1/2, b = 1/3.",
         "Decide which is greater, (a − b)² or (b − a)²."],
        ["A statement that matches only the shown cases is tested with a new case that breaks it.",
         "Both sides expand on screen and like terms are collected.",
         "A fraction test shows the two sides as equal fractions."],
        "All six cards are done and the statement has been tested with a negative and a fraction.",
        ["cases", "statement", "tests", "cardIndex"],
        ["M_DIFF_SQUARE", "M_SUM_SQUARE"],
        ["What stays the same in every line of the pattern?",
         "Call the two numbers a and b and write both sides with them.",
         "(a + b)(a − b) = a² − ab + ba − b² = a² − b².",
         "The general statement is shown, and a similar card follows."]),

    "identity_match_sort": T(
        "tool_c8dm_identity_match_sort", "Identity Match Sort", "simulation",
        "Choosing the right identity speeds a product up: a square of a sum, a square of a difference, a sum times "
        "a difference, or none of these, in which case the distributive property does the work.",
        "A deck of product cards such as 46², 397 × 403 and (3a − 9b)(3a + 9b), and four bins: square of a sum, "
        "square of a difference, sum times difference, none.",
        ["Read a card.",
         "Drop it in the bin of the identity that fits.",
         "Use the identity to finish the product.",
         "Read the reason when a card bounces back."],
        ["Sort 46² and finish it.",
         "Sort 397 × 403 and finish it.",
         "Sort 91² and finish it.",
         "Sort 43 × 45 and finish it.",
         "Sort (p − 1)(p + 11).",
         "Sort (2x − 1/2)² and expand it."],
        ["A card in a wrong bin returns with the shape it needed.",
         "The none bin accepts a product only when no identity fits.",
         "A finished product is checked against direct multiplication."],
        "All six cards are sorted and finished.",
        ["deck", "bins", "cardIndex"],
        ["M_SUM_SQUARE", "M_DIFF_SQUARE"],
        ["Is this a square, or a product of two different brackets?",
         "Two numbers the same distance from a round number make a sum times a difference.",
         "397 × 403 = (400 − 3)(400 + 3) = 160000 − 9 = 159991.",
         "The card is sorted and finished, and a similar card follows."]),

    "pattern_regrouper": T(
        "tool_c8dm_pattern_regrouper", "Pattern Regrouper", "simulation",
        "One growing pattern can be counted in several ways, each giving a different-looking expression, and "
        "every correct way simplifies to the same expression.",
        "A growing pattern of circles or tiles with a step slider, a lasso that groups pieces, the expression each "
        "grouping gives, and a simplify button that reduces each expression.",
        ["Move the step slider and watch the pattern grow.",
         "Lasso the pieces into groups and read the expression.",
         "Try a second grouping.",
         "Simplify both expressions and compare."],
        ["Count the circles in Step 4 two ways.",
         "Write the circles in Step k as (k + 1)² − 1 and simplify.",
         "Write them as k × (k + 2) and simplify.",
         "Count the tiles in Step 10 of the square-tile pattern.",
         "Write the tiles in Step n two ways.",
         "Find the circles in Step 15."],
        ["A grouping that misses or repeats a piece is shown with that piece flashing.",
         "Each correct grouping simplifies to the same expression on screen.",
         "The slider checks an expression against the real count at every step."],
        "All six cards are done with at least two groupings simplified to the same expression.",
        ["step", "groups", "expressions", "cardIndex"],
        ["M_ONE_RIGHT_WAY"],
        ["How does the pattern change from one step to the next?",
         "Group the pieces into a square, rows, or a rectangle, and count each group.",
         "(k + 1)² − 1 = k² + 2k + 1 − 1 = k² + 2k.",
         "Two groupings are shown with the same simplified expression, and a similar card follows."]),

    "neighbour_digit_adder": T(
        "tool_c8dm_neighbour_digit_adder", "Neighbour Digit Adder", "simulation",
        "A number times 11 is the number times 10 plus the number, so a shifted copy of its digits is added to "
        "itself: each column holds a digit and its right-hand neighbour, and a sum of 10 or more carries to the "
        "next column. For 101 the copy slides two places, and for 99 the number is taken away from a hundred times "
        "it.",
        "A number written in digit boxes, a second copy that slides one place or two places to the left under it, "
        "a row for carries, a column by column sum row, a switch for 11, 101 and 99, and a box for the product.",
        ["Type a number into the digit boxes.",
         "Slide the copy to the left by one place.",
         "Add one column at a time, write the digit and place the carry.",
         "Switch to 101 or 99 and see how the copy moves."],
        ["Find 23 × 11 and read which two digits make the middle digit.",
         "Find 68 × 11 and place the carry.",
         "Find 365 × 11 with a carry in two columns.",
         "Find 2718 × 11 in one line.",
         "Find 523 × 101 and say which digits are added.",
         "Find 47 × 99 as 4700 − 47.",
         "Find 623 × 99 as 62300 − 623."],
        ["A column sum with a missing carry is shown with the carry box flashing.",
         "The two digits being added light up in the number and in the copy.",
         "The product is checked against the number times 10 plus the number."],
        "All seven cards are done and the carry has been placed correctly in at least two of them.",
        ["number", "multiplier", "shift", "carries", "cardIndex"],
        ["M_DISTRIBUTE_FIRST_ONLY"],
        ["Which two numbers are added when a number is multiplied by 11, which is 10 + 1?",
         "Write the number and a copy one place to the left, then add the columns from the right.",
         "For 68 × 11: units 8; tens 6 + 8 = 14, write 4 and carry 1; hundreds 6 + 1 = 7, so 748.",
         "The columns are added on screen and the product is shown, and a similar card follows."]),

    "square_of_difference": T(
        "tool_c8dm_square_of_difference", "Square Of Difference Carver", "simulation",
        "A square of side a − b sits in the corner of a square of side a; taking away two strips ab removes the "
        "small b by b corner twice, so it is added back once and (a − b)² = a² − 2ab + b², which is not a² − b².",
        "A big square of side a with an a by b strip on the right and another along the top that can be dragged "
        "away, a shaded b by b corner that is cut twice, a button that adds the corner back, a toggle that shows "
        "the wrong picture a² − b², and number fields for a and b.",
        ["Set a and b.",
         "Drag the two strips off the big square and watch the area left.",
         "Notice the corner that is cut twice and add it back once.",
         "Answer a card by writing the area of the square left."],
        ["Find 55² as (60 − 5)².",
         "For a = 60 and b = 5, find how much less (60 − 5)² is than 60².",
         "Find 99² as (100 − 1)².",
         "Find 58² as (60 − 2)².",
         "Find 197² as (200 − 3)².",
         "Expand (5x − 2)².",
         "Show with a = 10 and b = 3 that (a − b)² is not a² − b²."],
        ["An answer that leaves out the added corner is shown with the b by b corner lit.",
         "Each strip prints its area as it is dragged away.",
         "The wrong picture a² − b² is shown with an L shape that does not fit the square left."],
        "All seven cards are done and the added corner has been explained once.",
        ["a", "b", "strips", "corner", "cardIndex"],
        ["M_DIFF_SQUARE"],
        ["Which big square does the smaller square sit in, and which two strips are cut away?",
         "Take both strips away, then look at the corner that was cut twice.",
         "For 99²: 100² − 100 − 100 + 1 = 10000 − 200 + 1 = 9801.",
         "The carving is shown with every area written in, and a similar card follows."]),

    "difference_of_squares_slide": T(
        "tool_c8dm_difference_of_squares_slide", "Difference Of Squares Slide", "simulation",
        "A square of side a with a b by b square cut from one corner leaves an L shape of area a² − b²; cutting the "
        "L into two strips and sliding one beside the other makes a rectangle with sides a + b and a − b, so "
        "a² − b² = (a + b)(a − b).",
        "A square of side a with a b by b corner cut out, a cutting line the student drags across the L, a strip "
        "that can be turned and slid, the sides of the new rectangle read out live, and number fields for a and b.",
        ["Set a and b.",
         "Drag the cutting line so the L falls into two strips.",
         "Turn one strip and slide it beside the other.",
         "Read the sides of the rectangle and its area."],
        ["Make a rectangle from the L of a = 10 and b = 4 and read its sides.",
         "Do the same for a = 12 and b = 5.",
         "Find 97 × 103 as a difference of two squares.",
         "Find 48 × 52 as a difference of two squares.",
         "Find a and b for a rectangle 16 by 6.",
         "Find 63 × 57 as a difference of two squares.",
         "Find a and b for a rectangle 30 by 4."],
        ["A cut that does not make two matching strips is shown with the two lengths that differ.",
         "The rectangle prints its sides as a + b and a − b as soon as the strips meet.",
         "The area of the L and the area of the rectangle are shown side by side and agree."],
        "All seven cards are done and the rectangle has been built from the L at least once.",
        ["a", "b", "cutLine", "strips", "cardIndex"],
        ["M_DIFF_SQUARE"],
        ["What shape is left when the small square is cut from the corner of the big one?",
         "Cut the L into two strips of the same width and slide one beside the other.",
         "For a = 10 and b = 4 the rectangle is 14 by 6, and 14 × 6 = 84 = 100 − 16.",
         "The strips are shown joined into a rectangle, and a similar card follows."]),

    "four_rectangles_square": T(
        "tool_c8dm_four_rectangles_square", "Four Rectangles Square", "simulation",
        "Four equal m by n rectangles placed round a small square make a big square of side m + n; the small square "
        "has area (m + n)² − 4mn when the rectangles are taken away, and area (n − m)² when its side is read "
        "directly, and the two expressions are equal.",
        "A big square of side m + n made of four m by n rectangles turned round a small square in the middle, "
        "sliders for m and n with n at least m, and the two area read-outs, one by taking away and one by the side of "
        "the small square.",
        ["Set m and n.",
         "Read the area of the small square by taking away the four rectangles.",
         "Read the side of the small square and square it.",
         "Compare the two answers."],
        ["Find the small square for m = 2 and n = 5 both ways.",
         "Find the small square for m = 3 and n = 8 both ways.",
         "Find the small square for m = 4 and n = 6 both ways.",
         "Find n when m = 3 and the small square has area 16.",
         "Set m = n = 5 and say what happens to the small square.",
         "Expand both expressions and check them with m = 1 and n = 6."],
        ["A side read as m + n instead of n − m is shown with the four rectangles lit.",
         "Both areas appear side by side and match for every m and n.",
         "When m equals n the small square shrinks to a point and both areas read 0."],
        "All six cards are done and both expressions have been expanded to the same result.",
        ["m", "n", "areaTakenAway", "areaBySide", "cardIndex"],
        ["M_ONE_RIGHT_WAY"],
        ["Which shape is left in the middle when four equal rectangles are placed round it?",
         "Find its area two ways: take the four rectangles from the big square, or read its side.",
         "For m = 2 and n = 5: 49 − 40 = 9, and the side is 5 − 2 = 3, so 3² = 9.",
         "Both ways are shown with the same answer, and a similar card follows."]),
}
