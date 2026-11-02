# -*- coding: utf-8 -*-
"""Tool write-ups (description field) for Class 8 Ch13 'Algebra Play'.

Keyed by tool media id. Applied onto the pulled live plan by apply_tool_descriptions.py.
Plain ASCII, no em or en dashes (media_content preflight rule).
"""

DESCRIPTIONS = {

"M1.S2.T2.C3.2D1": (
"The student opens a small magic stage. On the left is a cup holding the secret starting number x. "
"Beside it is a row of step cards: double it, add a number, halve it, multiply, divide, or subtract the start. "
"Every card has an editable number. The student drags cards into a row to build a Think of a Number trick, "
"types the numbers on the cards, then picks a starting number and presses Run. The value appears after every step.\n\n"
"First the student runs the same trick on two or three different starts and sees whether the endings match. "
"Then the student switches on the trace, which writes what is happening to x after every step. "
"They watch x appear, get doubled, get halved, and in the best tricks vanish at the last step. "
"The student changes one number on a card and sees the final value change, which shows that the number added or taken away decides the ending. "
"A trick whose x does not cancel shows two different endings for two starts, side by side. "
"A trick where x cancels shows a plain number in the trace and is marked as always working.\n\n"
"The six cards ask the student to make a trick end on 3 and then on 5 by choosing one number, to find the final value of tricks that multiply and divide, "
"to test whether a trick that ends by adding the start still works, and finally to invent their own trick of at least four steps that always ends on 7, "
"checked on two starts. Hints move from asking what is left after the halving step, to writing each step with x, to showing that halving 2x plus a number leaves x plus half the number. "
"Through doing, the student learns that a trick is not magic: the letter cancels, and the cancelling is what makes the answer the same for every start."
),

"M1.S2.T2.C7.2D1": (
"The student sits at a decoder desk with a month and day picker on one side and the six steps of the date trick laid out one after another, each showing its running value. "
"Below sit an answer box and a Subtract box that splits what is left into a month part and a day part.\n\n"
"In the first part the student picks a month and a day, runs the six steps, and reads the answer. "
"For month 3 and day 14 they see how the answer is built from the month and day. "
"In the second part the roles swap. A reported answer is typed in, the student subtracts 165, and then splits what is left. "
"The last two digits are the day and the digits before them are the month. "
"The split view shows the digits in two coloured groups so the student can see where each part is hiding.\n\n"
"Every decoded date is checked by running the steps forward and comparing with the reported answer. "
"If the date is wrong, the answer that comes out is shown beside the reported one so the student can see the gap. "
"A month that is too large or a day past 31 is flagged on the split. "
"The cards include answers like 874, 1167 and 1396, one where the day has a zero in front and the student must say why, "
"and one such as 500 that no real date can give. "
"A step editor lets the student change the trick, for example multiply the month by 20, add 3, multiply by 5, add the day, and then find the new number to subtract. "
"Hints ask where the month and day are hiding, then suggest taking away the fixed number the steps add, then name 165. "
"The student learns that every answer has the form 100 times the month, plus 165, plus the day, which is why the date can always be read back."
),

"M2.S3.T3.C14.2D1": (
"The student sees a number pyramid of three or four rows made of boxes. The bottom boxes accept numbers or letters. "
"Any box can be locked as a given, and a Letters switch changes every box into an expression in the bottom row.\n\n"
"Going up, the student types a bottom row such as 2, 7, 5 and watches each row above fill in, every box being the sum of the two below it. "
"Before pressing reveal, the student predicts the top, and a wrong guess shows how many times each bottom box was counted. "
"Going down, the student locks the top and a few other boxes and fills the rest by subtracting. "
"A box filled by adding is marked, and the subtraction that should have been used is shown. "
"With a top of 40 and a bottom row of 10, a blank and 6, the student puts a letter in the blank and solves for it.\n\n"
"With Letters on, a three row pyramid shows the top as a + 2b + c, so the student sees that the middle bottom box feeds both middle boxes and is counted twice. "
"In the four row pyramid with all ones at the bottom, the student predicts the top from a + 3b + 3c + d and checks it. "
"The last card builds a pyramid on 2, 3, 5, 8 and asks whether every box is a Virahanka-Fibonacci number. "
"Hints ask which boxes the top depends on, then suggest counting the paths from each bottom box to the top. "
"A letter answer is checked by putting the value back and rebuilding the pyramid. "
"The student learns that the top of a pyramid can be found without building it, and that going down is an equation with one unknown."
),

"M2.S5.T5.C22.2D1": (
"The student is shown an algebra grid. Each row is made of shapes and ends in a sum. "
"Beside every shape type is a value box. A row turns green when the values typed in make its sum true, and stays red otherwise.\n\n"
"The student first reads all the rows and decides which to solve first. "
"A row with one kind of shape, such as three triangles making 21, gives that shape at once. "
"When a shape is typed into a value box, every row where it appears updates, so the student sees one value shared across the whole grid. "
"This corrects the idea that two squares in different places could be different numbers.\n\n"
"When no row is easy, the student can add two rows. The combined row shows how many times each shape now appears, "
"so rows like two squares with a circle making 23 and two circles with a square making 22 can be joined and divided to free a shape. "
"A row with a wrong sum stays red and the shapes it uses are marked, and a shape value is confirmed only when every row it appears in is true. "
"The six cards move from a single-row start, to two shapes in two rows, to one where the answer of an earlier card is reused to fill the sum of a new row, "
"and end with a grid where the student must also check that the two shapes have different values. "
"Hints ask which row is easiest first, then suggest adding rows so each shape appears the same number of times, then name the division step. "
"The student learns to write each row as an equation, combine rows to remove one unknown, and check an answer in every row."
),

"M2.S5.T5.C23.2D1": (
"The student opens a month calendar with a movable frame. The frame can be a 2 by 2 square, a column of three, a 3 by 3 square or an L shape. "
"The dates inside it can be shown as numbers or as expressions in a, where a is the top left date, together with the sum and its expression.\n\n"
"The student drags the frame across the calendar and watches the sum change while the expression in a stays the same. "
"Looking at a 2 by 2 block, they see that the date to the right is a + 1, the date below is a + 7 and the one diagonal is a + 8, so the sum is 4a + 16. "
"Then the dates are hidden. The student reads only the sum, writes it as an equation in a, and finds the block, for example the four dates for a sum of 64, "
"or the middle date of a 3 by 3 frame with sum 117.\n\n"
"Each answer is checked by placing the frame on the block that was found. "
"A wrong block highlights the date that breaks the plus 1 or plus 7 pattern, and a sum that cannot be made, such as a block running past the end of the month, is flagged. "
"The student also designs a new shape, writes its sum in terms of a and tests it on the calendar, "
"and in the last card changes the calendar to ten columns and sees how the 2 by 2 sum changes. "
"Hints ask what lies directly below any date, then suggest writing every date in terms of a, then show taking 16 away and dividing by 4. "
"The student learns that one expression describes every block of a given shape, and that the sum gives the position away."
),

"M3.S6.T6.C26.2D1": (
"The student sees three digit tiles and a product frame made of two boxes, a times sign and one box. "
"Next to the frame is a table that records every arrangement tried, with its product, grouped by the multiplier.\n\n"
"The student drags the three digits into the frame and reads the product. "
"For digits such as 2, 4 and 6 there are six arrangements, and the student tries them all, watching the table fill. "
"The table pairs the arrangements that share a multiplier and marks the larger product in each pair, "
"so the student can see that with the same multiplier, putting the larger digit in the tens place wins. "
"The student then compares across multipliers, for example 93 times 6 against 63 times 9, and finds that the largest digit works best as the multiplier.\n\n"
"Before the table is complete, the student predicts the arrangement that gives the largest product. "
"A wrong prediction shows the two products side by side with their place value parts, so the student can see which one gained more in the tens. "
"After all six, the largest is highlighted and the rule is written out: largest digit as multiplier, other two in decreasing order. "
"The cards cover 2, 4, 6, then 1, 5, 8, then 3, 6, 9, ask for the smallest product with 2, 7, 9, ask the student to predict first for 4, 5, 6, "
"and finally let them choose three digits and test the rule. "
"Hints ask which box changes the product most, then suggest comparing two arrangements with the same multiplier. "
"The student learns why the rule works, not just what it is."
),

"M3.S8.T8.C31.2D1": (
"The student works in a digit lab with tiles for a two or three digit number, labelled with place values. "
"An operation chooser offers four moves: reverse and subtract, reverse and add, cycle the digits and add, and repeat the digits. "
"Under the chooser are the result and a divide by box.\n\n"
"The student picks digits and an operation, for example 52 reversed and subtracted, and reads the result. "
"Then they try dividing it by a chosen number, such as 9, and see whether it leaves no remainder, and compare the quotient with the digit difference. "
"A divisor that leaves a remainder is shown with the remainder and the place value view of the result. "
"With the place value view switched on, the result is written as a fixed number times a digit expression: "
"reverse and subtract gives 9 times the difference of the digits, reverse and add gives 11 times their sum, "
"adding the two cycles of a three digit number gives 111 times the digit sum, so 37 divides it, "
"and repeating three digits multiplies the number by 1001, which is why 7, 11 and 13 all divide it.\n\n"
"The six cards use 52, 74, 247, 163 and 841, and ask the student to test which of 9 and 11 always divides a number plus its reverse, trying 38 and 61. "
"A correct divisor is confirmed by showing the number times a digit expression. "
"Hints ask which operation is done to the number and its reverse, then suggest writing the number with place values and combining like parts. "
"The student learns that a trick that seems to work for every number works because the letters combine into a fixed factor."
),

"M3.S10.T10.C36.2D1": (
"The student sees a start box, a round panel with a double step and a give step, a counter for the number of rounds, "
"and a trace that shows the amount after each round as a number and as an expression in x.\n\n"
"First the student predicts. If the amount doubles in each round but some is given away, does it always grow? "
"They set a start, an amount to give and a number of rounds, for example 6 coins, give 5, two rounds, "
"write a guess, and press Run. The trace shows the amount after each round. "
"A wrong prediction runs the rounds one at a time and shows where the amounts differ. "
"With start 8 and give 8 in every round, the student sees that the amount never grows, and works out why: it grows only while less is given than is held.\n\n"
"Next the student switches to the x view. Each round doubles the whole expression before the give step takes some away. "
"For double and give 5 for two rounds, the amount is written in terms of x, and setting it equal to what is left becomes an equation. "
"In the reverse task, the student sets a target and searches for the start that reaches it, such as double and give 3 for two rounds ending with 11, or give 4 for three rounds ending with 20. "
"A start that reaches the target is checked by running every round forward. "
"Hints ask what happens in a round and in what order, then suggest following x through the first round, then the second. "
"The student learns to follow a story step by step, in order, and to turn it into an equation."
),

"M3.S10.T10.C38.2D1": (
"The student sees a row of counters for the total number of heads, a small table of two kinds with their legs, wheels or rupees, and a running total. "
"Each tap swaps one counter from the lighter kind to the heavier kind and the total changes. A letter view writes the equation.\n\n"
"The student starts with every counter of the lighter kind, for example 12 hens with 2 legs each, and reads the total, which is too small for 34 legs. "
"Then they swap counters one at a time and watch the total climb. Each swap shows the difference it adds, here 2 legs, "
"so the student can see the same step happening every time. "
"They stop when the total matches the target and read off how many were swapped, which is the number of horses. "
"A total that cannot be reached with whole swaps is flagged with the amount left over, which handles the case of 10 heads and 25 legs.\n\n"
"The cards move through 12 heads and 34 legs, 30 heads and 84 legs, 15 cycles with 38 wheels where bicycles have 2 and tricycles have 3, "
"and 20 coins worth 70 rupees using 2 rupee and 5 rupee coins. In the last card the student lets h be the number of horses, "
"writes the equation from the letter view and solves it. A solution is checked by counting the heads and the total again. "
"Hints ask what the total would be if every counter were the lighter kind, then suggest finding the shortfall and how much one swap adds, then dividing. "
"The student learns that the swapping method and the equation are the same idea: the shortfall divided by what one swap adds."
),
}
