# -*- coding: utf-8 -*-
"""Tool specs for T3 and T4 of Class 5 Chapter 10 (Symmetrical Designs): Symmetry Sorter (the digits and numbers) and
Design Studio (making designs that turn). Specs only; the tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Shapes the plan adds are labelled practice values. One activity at a
time, one instruction at a time, large controls, Back and Next in the same place, visible progress, Hint, Retry and
Reset always present, immediate specific feedback that is never red."""
from topics_common import T

TOOLS = {
    "symmetry_sorter": T(
        "tool_symmetry_sorter", "Symmetry Sorter", "manipulative",
        "Test a letter, a digit or a number with a fold line and with a turn, and sort it into reflection only, turn only, "
        "both, or neither, so that the student sees that the two tests give two different answers and runs both every "
        "time.",
        "Lali's craft table, drawn as a warm 3D isometric scene with soft shadows and gentle animation. A wooden test board "
        "in the middle holds one large card at a time, the largest thing on screen, with a letter, a digit or a number on it. "
        "Beside the board are two testers. The fold tester has two switches, Fold on the vertical line and Fold on the "
        "horizontal line, which draw a dashed line on the card and slide one half over the other so the student sees whether "
        "the halves match. The turn tester is a turn dial with three stops, 1/4, 1/2 and 3/4, which turns the card to the "
        "right and keeps a dashed outline of the starting position. Under the board four trays stand in a row: Reflection "
        "only, Turn only, Both and Neither. A shelf above holds the cards still to be tested. An instruction strip at the "
        "top shows one sentence in large type, with progress dots under it. Controls: tap a card to bring it to the board; "
        "tap a fold switch; tap a stop on the dial; drag the card into a tray; Check, Hint, Retry (returns the card to the "
        "board), Reset (empties the trays), Back and Next in the same places on every card. Read-outs under the board: "
        "Vertical line: halves match or do not match; Horizontal line: halves match or do not match; 1/4 turn, 1/2 turn, "
        "3/4 turn: looks the same or looks different; and the number of cards in each tray.",
        ["Look at the card with the letter M from the video. Press Fold on the vertical line, "
         "then turn it a 1/2 turn. Does M pass the fold test? Does it pass the turn test? Then press Next.",
         "Bring a card to the board, run the fold test and the turn test, and drag the card into the "
         "right tray. Sort the letters C, Z, H and F, one for each tray, and then the letters U and S, the plus sign and the "
         "letter P.",
         "Sort the digits 1 to 0 and answer which have reflection symmetry, rotational symmetry and both; "
         "then test the numbers 11 and 1001; then make 2-, 3- and 4-digit numbers with rotational symmetry, reflection "
         "symmetry or both."],
        ["Card 1 (practice values): the letter C. Run both tests and choose a tray. Answer: the Horizontal fold "
         "matches and no turn makes it look the same, so C goes in Reflection only.",
         "Card 2 (practice values): the letter Z. Run both tests and choose a tray. Answer: no fold matches, but after "
         "a 1/2 turn it looks the same, so Z goes in Turn only.",
         "Card 3 (practice values): the letter H. Run both tests and choose a tray. Answer: the vertical and the "
         "horizontal fold both match and it looks the same after a 1/2 turn, so H goes in Both.",
         "Card 4 (practice values): the letter F. Run both tests and choose a tray. Answer: no fold matches and no "
         "turn makes it look the same, so F goes in Neither.",
         "Card 5 (practice values): sort four cards together: the letter U, the letter S, the plus sign and the "
         "letter P. Answer: U goes in Reflection only, S in Turn only, the plus sign in Both, and P in Neither.",
         "Challenge: 'Find symmetry in the digits.' The digits 1, 2, 3, 4, 5, 6, 7, 8, 9 and 0 are on the shelf, with "
         "the digit 1 drawn as a plain bar. 'Which digit(s) have reflection symmetry? Which digit(s) have rotational symmetry? "
         "Which digit(s) have both rotational and reflection symmetries?' Answer: reflection symmetry: 0, 1, 3, 8. Rotational "
         "symmetry: 0, 1, 8. Both: 0, 1, 8. The digits 6 and 9 turn into each other, so neither looks the same after a 1/2 "
         "turn by itself.",
         "Challenge: 'Now, let us look at the following numbers: 11, 1001. Do these have (a) rotational symmetry, (b) "
         "reflection symmetry or (c) both symmetries?' Then: 'Give examples of 2-, 3-, and 4-digit numbers which have "
         "rotational symmetry, reflection symmetry, or both.' Answer: 11 and 1001 have both symmetries. Sample examples: "
         "rotational symmetry only 69, 619, 6969; reflection symmetry only 38, 383, 3883; both 88, 808, 8118. Your examples "
         "may differ."],
        ["After the two tests the tool shows a soft green message when the tray fits, for example: The halves match on the "
         "horizontal line and the card never looks the same after a turn, so it is Reflection only. A card in the wrong tray "
         "slides back with a clue such as: Run the turn test. Does it look the same after a 1/2 turn?",
         "For the digit 6 the tool says: A 1/2 turn makes the 6 look like a 9, so the 6 does not look the same by itself.",
         "For a number the tool shows the whole number on the board and folds the whole number, not each digit alone.",
         "The tray counts update after every card, so the student can see which group is still empty."],
        "Every practice card is in the right tray, the digits are sorted, the numbers 11 and 1001 are tested, and the student has "
        "made a number for each group.",
        ["cardOnBoard", "foldResult", "turnResult", "trays", "challengeIndex"],
        ["M_BOTH_ALWAYS", "M_SIX_NINE", "M_FLIP_IS_TURN"],
        ["Which test will you run first, the fold test or the turn test? Run both on every card.",
         "Run the fold test on the vertical line, then on the horizontal line. Then turn the card a 1/4, a 1/2 and a 3/4 turn.",
         "Read the two results under the board. Which tray has the fold result and the turn result of this card?",
         "Drag the card to the tray the tool shows. It has the fold result and the turn result written under the board."]),

    "design_studio": T(
        "tool_design_studio", "Design Studio", "manipulative",
        "Add, change and colour parts of a design so that it looks the same after a 1/2 turn and after a 1/4 turn, and find "
        "its lines of symmetry with a fold line, so that the student sees where each part lands after a turn and that "
        "colours count.",
        "Lali's craft table, drawn as a warm 3D isometric scene with soft shadows and gentle animation. A large round design "
        "board with a pin at its centre and four faint guide marks, at the top, right, bottom and left, fills the middle and is "
        "the largest thing on screen. A tray beside it holds 6 light blue squares and 6 pink equilateral triangles with the same "
        "side as the squares, the pieces of the book's sheet of shapes, and circles for the book's design, and two pots of "
        "colour. A turn dial with three stops, 1/4, 1/2 and 3/4, sits in "
        "front of the board. A fold line tool offers four lines, vertical, horizontal and the two diagonals. An instruction "
        "strip at the top shows one sentence in large type, with progress dots under it. Controls: drag a shape from the tray "
        "onto the board; tap a placed shape to turn it a quarter; tap a colour pot and then a part to colour it; choose a "
        "stop on the dial to show faint ghost copies of the design where each part would land after that turn, with a red "
        "outline round any part that has no partner; choose a fold line to show one half folded over the other and whether "
        "the shapes and colours match; Undo, Check, Hint, Retry (clears the design of this card), Reset (empties the board), "
        "Back and Next in the same places on every card. Read-outs: the number of shapes on the board, the turn chosen, and "
        "for each fold line, matches or does not match, with a card number out of 7.",
        ["Look at a circle with one triangle above it (practice values) on the board. Choose "
         "the 1/2 turn and tap the place where the triangle lands, then press Next.",
         "Add shapes so that the design looks the same after a 1/2 turn and then after a 1/4 turn, "
         "colour a strip of two squares and a square cut by its diagonals, and test each design with the turns and the fold "
         "lines.",
         "Do the book's design questions: Making Designs (a) to (d), the two Let Us Think questions and the "
         "reflection question, and the squares and triangles questions, with your own designs sorted into three groups."],
        ["Card 1 (practice values): a circle with one triangle above it, pointing up. Add a shape so that the design "
         "looks the same after a 1/2 turn. Answer: add a triangle below the circle, pointing down. The design then has 2 "
         "triangles and no red outlines after the 1/2 turn.",
         "Card 2 (practice values): from the design of card 1, add shapes so that it looks the same after a 1/4 "
         "turn. Answer: add a triangle on the left, pointing left, and one on the right, pointing right. The design then has "
         "4 triangles and looks the same after 1/4, 1/2, 3/4 and a full turn, which is 4 times.",
         "Card 3 (practice values): a strip of 2 squares side by side. Colour the left square orange and the right "
         "square blue, then test the 1/2 turn. Answer: after a 1/2 turn the orange square lands on the blue square's place, so "
         "the design does not look the same. Colour both squares orange and it does. Colours count.",
         "Card 4 (practice values): a square cut by its two diagonals into 4 triangles. Colour the top and bottom "
         "triangles orange and the left and right triangles blue. Test the turns and the four fold lines. Answer: it looks the "
         "same after a 1/2 turn but not after a 1/4 turn. The vertical and horizontal fold lines match, and the diagonals do "
         "not. It has 2 lines of symmetry.",
         "Challenge: Making Designs. The design is a circle in the middle with a triangle above and below it, each "
         "with its point touching the circle, a triangle on the left and right, each with its flat side touching the circle, "
         "and a second circle at the point of the right triangle. '(a) Does the design have rotational symmetry? Yes/No. (b) "
         "Try to change the design by adding some shape(s) so that the new design looks the same after a 1/2 turn. (c) Now try "
         "to modify or add more shapes so that the new design looks the same after 1/4 turn. (d) Do the new designs have "
         "reflection symmetry? If yes, draw the lines of symmetry.' Answer: (a) No. (b) add a circle at the left tip. (c) make "
         "the four arms equal, with a circle at each tip. (d) yes: 2 lines for (b), 4 lines for (c). Your designs may differ.",
         "Challenge: Let Us Think. 'Does this design look the same after 1/2 turn? Does the design look the same after "
         "1/4 turn?' for the square of four smaller squares, green at the top left and bottom right and pink at the other two. "
         "'Colour the square given in the figure using two colours so that the design looks the same after every 1/4 turn. "
         "How many times does this shape look the same during a full turn?' 'Do these designs have reflection symmetry also? "
         "Draw the line(s) of symmetry.' Then the squares and triangles: 'Make different symmetrical designs by using these two "
         "shapes', the shape of four squares with a triangle at each end of each row, and 'Sort your designs in 3 categories'. "
         "Answer: the green and pink square: 1/2 turn yes, 1/4 turn no, with 2 lines of symmetry, its two diagonals. The "
         "coloured square: alternate the two colours on the 8 triangles, 4 times in a full turn, and no line of symmetry. The "
         "shape of four squares: 2 lines and a 1/2 turn, both symmetries. Sample designs may differ."],
        ["The ghost copies show where each part lands after the chosen turn. A part with no partner gets a red outline and the "
         "tool says: After a 1/2 turn this triangle lands here, and nothing is there. Add a copy of it in that place.",
         "When every part has a partner the tool says in green: Every part lands on a matching part, so the design looks the "
         "same after this turn.",
         "A fold line shows the two halves folded over each other. If a shape or a colour does not match, the tool marks it and "
         "says, for example: Orange lands on blue, so this line is not a line of symmetry.",
         "When a design is finished the tool shows its result for the turns and the lines, and the student sorts it into only "
         "rotational symmetry, only reflection symmetry or both."],
        "Every practice design looks the same after the asked turn, the book's designs are made and tested, and the student has "
        "sorted at least three designs into the three groups.",
        ["boardShapes", "chosenTurn", "ghostCopies", "foldLineResult", "colourPots", "challengeIndex"],
        ["M_COLOUR_IGNORED", "M_HALF_IMPLIES_QUARTER", "M_BOTH_ALWAYS"],
        ["Look at the design. After the turn, where does each part land? Is there a part there already?",
         "Choose the turn on the dial. A red outline shows the place that has no partner. What is missing there?",
         "Put a copy of the missing part in the place with the red outline. Then turn again and check the next part.",
         "Add the part the tool shows in the red outlined place. Every part now has a partner, so the design looks the same "
         "after the turn."]),
}
