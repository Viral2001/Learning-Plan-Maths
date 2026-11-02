# -*- coding: utf-8 -*-
"""Tool specs for module M1 (letter-numbers and expressions) and the like-terms topic."""
from topics_common import T

TOOLS = {
    "words_assembler": T(
        "tool_words_assembler", "Words to Expression Assembler", "manipulative",
        "A situation told in words becomes an expression when each changing quantity gets a letter-number and the "
        "operations are placed in the order the story says.",
        "A short story card at the top; a tray of letter-number tiles and operation tiles; an assembly line where the "
        "student builds the expression; a test panel that replaces the letters by chosen numbers and compares with the "
        "story.",
        ["Read the story and name each changing quantity with a letter-number.",
         "Drag tiles into the assembly line to build the expression.",
         "Press Test, choose numbers for the letters, and see if the story gives the same value.",
         "Fix the line if the values differ, then go to the next story."],
        ["Plates of two kinds at different prices (30x + 20y).", "Bags of two sizes with a fixed number of sweets each.",
         "A number that is 5 more than d and a number that is 4 less than d.",
         "Hours worked at one rate plus a fixed bonus.", "Pages read each day for d days plus 10 more.",
         "Money left after buying n pens at a fixed price."],
        ["Joining the digits of a number and a letter, such as 20 and k as 20k, is shown as a product, and the test "
         "values show it does not match a sum.",
         "Swapped prices give a different test value, with the story's value shown beside it.",
         "A correct expression written in a different order is accepted."],
        "All six stories have an expression that matches the story on every test.",
        ["story", "tray", "line", "testValues", "cardIndex"],
        ["M_JOIN_DIGITS", "M_LETTER_FIXED"],
        ["What changes in this story, and what stays the same?",
         "Say the value in words first, then put the letter-number where the changing quantity goes.",
         "Which operation joins the two parts: sum, product, or less than?",
         "The tiles are placed one by one to match the story, the test confirms it, and a new story follows."]),

    "letter_slot_loader": T(
        "tool_letter_slot_loader", "Letter Slot Loader", "manipulative",
        "Replacing a letter-number by a number means loading that number into every slot where the letter stands, then "
        "working the expression by the usual order of operations.",
        "An expression card with a slot under every letter-number; a number dial for each letter; a working strip "
        "showing the expression with numbers loaded; a value display.",
        ["Choose the number for the letter-number on the dial.",
         "Watch the number load into every slot of the expression.",
         "Work the expression in order and type the value.",
         "Change the dial and see the value change."],
        ["7k with k = 4 (28).", "5m + 3 with m = 2 (13).", "10 − a with a = −4 (14).", "3(m + 1) with m = −6 (−15).",
         "3s − 2 with s = 7 (19).", "2r + 1 with r = 8 (17)."],
        ["Joining digits, such as 7 and 4 read as 74 for 7k, is shown as a product with the right value beside it.",
         "A missed bracket round a negative number gives a different value, shown beside the correct one.",
         "Doing addition before multiplication in 5m + 3 is flagged with the correct order highlighted."],
        "All six cards have the right value, and the same expression gives different values for different numbers.",
        ["expression", "letterValue", "slots", "value", "cardIndex"],
        ["M_JOIN_DIGITS", "M_ORDER_OPS", "M_SIGN_VALUE"],
        ["Which letter-numbers are in the expression, and how many slots does each have?",
         "Put the number in every slot, with brackets round a negative number.",
         "Multiply before you add, and work inside the brackets first.",
         "The number is loaded into each slot, the expression is worked step by step to its value, and a new card follows."]),

    "like_term_gatherer": T(
        "tool_like_term_gatherer", "Like Term Gatherer and Equality Tester", "manipulative",
        "Terms that share the same letter-numbers can be gathered and added into one term, and the gathered "
        "expression is checked equal to the original by comparing values for several numbers.",
        "An expression made of coloured term cards; bins labelled by letter-number; a button to add each bin into one "
        "term; an equality tester with a number dial that shows both expressions' values side by side.",
        ["Drag each term card into the bin that has its letter-number.",
         "Add the numbers in front of the cards in each bin to get one term per bin.",
         "Use the equality tester with three different numbers to compare the original and the gathered expression.",
         "Say if the result can be simplified further."],
        ["5c + 3c + 10c (18c).", "4d + 6d + d (11d).", "18c + 11d (already simplest).", "12n − 4n (8n).",
         "3p + 2q + p − q (4p + q).", "6a − 2b − a + 5b + 3 (5a + 3b + 3)."],
        ["Putting terms with different letter-numbers in one bin is refused, with the two letters shown.",
         "Adding 3a and 2b into 5 is shown with the tester: the values differ for most numbers.",
         "A card with no number in front is read as 1 times the letter-number."],
        "All six expressions are gathered into the simplest form and each passes the equality tester.",
        ["terms", "bins", "result", "testValue", "cardIndex"],
        ["M_UNLIKE_ADD"],
        ["Which terms have the same letter-numbers?",
         "Put like terms in one bin and add the numbers in front of them.",
         "A term such as d has the number 1 in front. Terms with different letters stay in separate bins.",
         "The terms are gathered into bins, each bin is added, the tester confirms the values match, and a new "
         "expression follows."]),
}
