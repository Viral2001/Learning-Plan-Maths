# -*- coding: utf-8 -*-
"""Tool specs for T1 and T2 of Class 5 Chapter 9 (Coconut Farm): Coconut Array (the free try of the intro, right after the
hook) and Place Value Shifter. Specs only; the tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds are labelled practice values. One
activity at a time, one instruction at a time, large controls, Back and Next in the same place, visible progress,
Hint, Retry and Reset always present, immediate specific feedback that is never red."""
from topics_common import T

TOOLS = {
    "coconut_array": T(
        "tool_coconut_array", "Coconut Array", "manipulative",
        "Build an array of coconuts with a chosen number of rows and columns and read the multiplication fact and the two "
        "division facts that go with it: the same coconuts split into equal groups by the columns, or by the rows. This is "
        "the free first try of the chapter, so it asks and shows; the videos that follow name the facts.",
        "The packing shed table on Susie and Sunitha's coconut farm in Kerala, drawn as a warm 3D isometric scene with soft "
        "shadows and gentle animation. A wooden coconut tray fills the middle of the screen and is the largest thing on it: "
        "it shows coconuts in rows and columns, up to 9 rows and 9 columns. An instruction strip at the top shows one "
        "sentence in large type, with progress dots under it. Above the tray is a Columns stepper with a plus and a minus "
        "button, and beside the tray a Rows stepper. Below the tray is a fact board with three lines: rows × columns = "
        "total, total ÷ columns = rows, and total ÷ rows = columns, with empty slots for number cards, and two buttons, "
        "Groups by columns and Groups by rows, that outline the groups on the tray in two colours. A sentence under the "
        "tray reads, for example, 35 split into 7 groups has 5 in each group. Controls: tap plus or minus on a stepper to "
        "add or remove a row or a column; tap a Groups button to outline the groups; drag number cards onto the slots of "
        "the fact board; Check, Hint, Retry (clears the fact board of this card), Reset (an empty tray), Back and Next in "
        "the same places on every card. Read-outs: the number of rows, the number of columns, the number of coconuts in "
        "all, the number of groups and the number in each group, and a card number out of 7.",
        ["Look at the array of 5 rows of 7 coconuts from the story on the coconut tray. "
         "Count the rows, count the coconuts in each row, and say how many coconuts there are in all. Then press Next.",
         "Build arrays with the steppers, read the multiplication fact, outline the groups by "
         "columns and by rows to read the two division facts, fill a fact board for an array that is given, and build a "
         "row of one.",
         "Write the two division facts for the array of the story, using its multiplication fact, and "
         "then write the multiplication fact and two division facts for the array of 4 rows of 8 that the tray shows."],
        ["Card 1 (practice values): build 4 rows of 6 coconuts with the steppers. How many coconuts are there? "
         "Write the multiplication fact. Answer: 24 coconuts, 4 × 6 = 24.",
         "Card 2: press Groups by columns and then Groups by rows. Write the two division facts. Answer: by "
         "columns there are 6 groups with 4 in each group, so 24 ÷ 6 = 4; by rows there are 4 groups with 6 in each group, "
         "so 24 ÷ 4 = 6.",
         "Card 3 (practice values): build 3 rows of 8 coconuts. Is the total the same as before? Write the three "
         "facts. Answer: 3 × 8 = 24, the same 24 coconuts in a different array, and the division facts are 24 ÷ 8 = 3 and "
         "24 ÷ 3 = 8.",
         "Card 4 (practice values): the tray shows 6 rows of 5 coconuts. Fill the fact board with one "
         "multiplication fact and two division facts. Answer: 6 × 5 = 30, 30 ÷ 5 = 6 and 30 ÷ 6 = 5.",
         "Card 5 (practice values): build 1 row of 9 coconuts. Write the facts and say what 9 ÷ 1 is. Answer: "
         "1 × 9 = 9, 9 ÷ 9 = 1 and 9 ÷ 1 = 9. Dividing by 1 gives the same number.",
         "Challenge: 'Observe the following array of coconuts. Write two division facts using the given "
         "multiplication fact.' The tray shows 5 rows of 7 coconuts and the fact 5 × 7 = 35. Answer: 35 ÷ 7 = 5, because "
         "35 split into 7 groups has 5 in each group; and 35 ÷ 5 = 7, because 35 split into 5 groups has 7 in each group.",
         "Challenge: 'Write the appropriate multiplication fact for the array shown below. Write two division "
         "facts that follow from the multiplication fact.' The tray shows 4 rows of 8 coconuts. Answer: 4 × 8 = 32, "
         "32 ÷ 8 = 4 and 32 ÷ 4 = 8. Next stop: the videos name the two division facts."],
        ["A tap on plus adds a row or a column and the coconut count in all changes at once, for example 4 rows of 6 is "
         "24 coconuts in all.",
         "When Groups by columns is pressed the tool outlines the columns and says, for example: 24 split into 6 groups "
         "has 4 in each group, so 24 ÷ 6 = 4.",
         "When Groups by rows is pressed the tool outlines the rows and says, for example: 24 split into 4 groups has 6 "
         "in each group, so 24 ÷ 4 = 6.",
         "A number card dropped in the wrong slot slides back with a clue, such as: Which number is the total of all the "
         "coconuts? A card in the right slot locks in with a soft chime.",
         "A fact that mixes up the numbers gets a soft amber note, for example: The total 24 is the number being split, so "
         "it comes first in a division fact."],
        "The student has built the arrays of the cards, written the multiplication fact and both division facts for each, "
        "and has written the facts for the two arrays of the story and of 4 rows of 8.",
        ["rows", "columns", "groupsShown", "factBoard", "challengeIndex"],
        ["M_DIV_COMMUTES", "M_DIV_SHRINKS"],
        ["Count the rows and count the coconuts in each row. How many coconuts are there in all?",
         "Split the coconuts into equal groups: one group for each column, or one group for each row. Press a Groups "
         "button and see.",
         "The total is the number being split. Write the total, then the sign ÷, then the number of groups, then the "
         "number in each group.",
         "For 5 rows of 7: 35 split into 7 groups has 5 in each group, so 35 ÷ 7 = 5. The other fact uses the 5 rows: "
         "35 ÷ 5 = 7."]),

    "place_value_shifter": T(
        "tool_place_value_shifter", "Place Value Shifter", "manipulative",
        "Divide tens, hundreds and thousands by 10, by 100 and by a one-digit number using a table fact, and see on a "
        "place value chart that one more zero in the dividend gives one more zero in the quotient and that dividing by 10 "
        "slides every digit one place to the right.",
        "A chart board on the wall of the packing shed on Susie and Sunitha's coconut farm, drawn as a warm 3D isometric "
        "scene with soft shadows and gentle animation. The place value chart is the largest thing on screen: four columns, "
        "Thousands (green), Hundreds (orange), Tens (blue) and Ones (pink), with digit tiles that slide between the "
        "columns. An instruction strip at the top shows one sentence in large type, with progress dots under it. Above the "
        "chart is the division of the card, for example 280 ÷ 4, and a Divide by dial with the choices 10, 100 and a "
        "one-digit number. Below the chart is a bundles row that groups the number into bundles of ten or of a hundred, "
        "and a read-out line, for example 28 tens split into groups of 4 gives 7 tens. A pattern strip on the right "
        "stacks the rows already done. Controls: drag a digit tile one place to the right or the left; turn the Divide by "
        "dial; tap Show bundles; type the quotient into the answer box or into the chart; Check, Hint, Retry (clears the "
        "chart of this card), Reset (empties the chart and the pattern strip), Back and Next in the same places on every "
        "card. Read-outs: the dividend, the divisor, the number of bundles, the quotient, and a card number out of 7.",
        ["The chart shows 150 as 15 tens. Say how many groups of 3 are in 15, and what that "
         "means for 150. Then press Next.",
         "Divide tens and hundreds with a table fact and the bundles, slide the digits right to "
         "divide by 10 and by 100, divide a number by the same number with zeros added, and fill the chart for new "
         "divisions.",
         "Solve the book's nine divisions and notice the patterns, then fill the book's two place value "
         "charts."],
        ["Card 1 (practice values): 280 ÷ 4. The chart shows 28 tens. Answer: 28 ÷ 4 = 7, so 28 tens split into "
         "groups of 4 gives 7 tens, and 280 ÷ 4 = 70.",
         "Card 2 (practice values): 2400 ÷ 8. The chart shows 24 hundreds. Answer: 24 ÷ 8 = 3, so 3 hundreds, and "
         "2400 ÷ 8 = 300.",
         "Card 3 (practice values): divide 6000 by 10 and then by 100 by sliding the digit 6. Answer: 6000 ÷ 10 = "
         "600, the 6 slides from the thousands to the hundreds; 6000 ÷ 100 = 60, it slides two places to the tens.",
         "Card 4 (practice values): divide 9100 by 91 and 910 by 91. Answer: 9100 ÷ 91 = 100 because 91 × 100 = "
         "9100, and 910 ÷ 91 = 10 because 91 × 10 = 910.",
         "Card 5 (practice values): fill the chart for 3000 ÷ 10 and 5000 ÷ 100. Answer: 3000 ÷ 10 = 300 with 3 in "
         "the hundreds, 0 in the tens and 0 in the ones; 5000 ÷ 100 = 50 with 5 in the tens and 0 in the ones.",
         "Challenge: 'Solve the following division problems. Notice the patterns and discuss in class.' 150 ÷ 3, "
         "80 ÷ 4, 500 ÷ 5, 100 ÷ 10, 300 ÷ 100, 500 ÷ 50, 200 ÷ 20, 440 ÷ 44, 630 ÷ 63, with the hints how many groups of 3 "
         "are in 150, 5 × ___ = 500 and 44 × ___ = 440. Answer: 50, 20, 100, 10, 3, 10, 10, 10, 10.",
         "Challenge: 'Now fill the place value chart.' First chart: 700 ÷ 70, 1400 ÷ 100, 220 ÷ 20 and 2200 ÷ 20 "
         "(the rows 40 ÷ 10, 400 ÷ 10 and 4000 ÷ 10 are filled in as examples). Second chart: 110 ÷ 11, 860 ÷ 86, 7500 ÷ "
         "750, 8800 ÷ 88, 2400 ÷ 24 and 440 ÷ 22. Answer: first chart 10, 14, 11, 110; second chart 10, 10, 10, 100, 100, "
         "20, each written as digits in the hundreds, tens and ones columns. Next stop: the mental strategies for division."],
        ["A digit tile that slides one place to the right shows the new number at once, for example 40 ÷ 10 = 4: the 4 moved "
         "from the tens to the ones.",
         "With Show bundles on, the tool groups the number into bundles and says, for example: 28 tens split into groups "
         "of 4 gives 7 tens, which is 70.",
         "A quotient with the wrong number of zeros gets a soft amber note, for example: 2400 is 24 hundreds, so the answer "
         "is 3 hundreds, not 3 tens.",
         "The pattern strip stacks the rows, 70 ÷ 10 = 7, 700 ÷ 10 = 70 and so on, so the student sees one more zero in the "
         "dividend and one more zero in the quotient.",
         "A digit placed in the wrong column slides back with a clue such as: Which place is this digit in now? A digit in "
         "the right column locks in."],
        "The student has divided with table facts and bundles, slid digits to divide by 10 and 100, solved the book's nine "
        "divisions and filled both place value charts.",
        ["dividend", "divisor", "bundlesShown", "chartDigits", "patternRows", "challengeIndex"],
        ["M_ZEROS_LOST"],
        ["Look at the number on the chart. How many tens or hundreds is it?",
         "Use the table fact for the digits that are left, then put the tens or the hundreds back.",
         "For a division by 10, slide every digit one place to the right. For a division by 100, slide it two places.",
         "For 280 ÷ 4: 280 is 28 tens, 28 ÷ 4 = 7, so the answer is 7 tens, which is 70."]),
}
