# -*- coding: utf-8 -*-
"""Topics T10 to T13 (modules M3 and M4: expressions that describe patterns, and the summary). Book section 4.6."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T10 Saree border =============================================================
TOPICS.append(TOPIC(
    "T10", "M3", "Patterns in a Saree Border", ["4.6"], "Apply",
    "Students write an expression for the positions where each design of a saree border appears, and use the "
    "remainder on division by 3 to name the design at any position.",
    "A design that repeats every third position appears at positions given by an expression in n, and the remainder "
    "on dividing a position by 3 tells which design is there.",
    [A("T10.C1", "Where does each design appear?", "Apply",
       "Students write the position of the nth appearance of designs C, B and A as 3n, 3n − 1 and 3n − 2, and explain "
       "why B and A sit one and two places before a multiple of 3.",
       textbook=["Algebraic Expressions to Describe Patterns",
                 "Example 12: Somjit noticed a repeating pattern along the border of a saree. The designs are A B C D "
                 "E F. Somjit wonders if there is a way to describe all the positions where the (i) Design A occurs, "
                 "(ii) Design B occurs, and (iii) Design C occurs.",
                 "Let us start with design C. It appears for the first time at position 3, the second time at "
                 "position 6. Where would design C appear for the nth time?",
                 "We can see that this design appears in positions that are multiples of 3. So the nth occurrence of "
                 "Design C will be at position 3n. Similarly, find the formula that gives the position where the "
                 "other Designs appear for the nth time.",
                 "The positions where B occurs are 2, 5, 8, 11, 14, and so on. We can see that the position of the "
                 "nth appearance of Design B is one less than the position at which Design C appears for the nth "
                 "time. Thus, the nth occurrence of Design B is at position 3n − 1. Similarly, the expression "
                 "describing the position at which the design A appears for the nth time is 3n − 2."],
       teach=["Predict first: the border repeats three designs A, B, C again and again. At which positions does C "
              "appear, and what is the tenth one?",
              "C sits at the multiples of 3, so the nth C is at position 3n.",
              "B comes just before each C, so B is at 3n − 1, and A is two before each C, at 3n − 2.",
              "Check with n = 1, 2, 3: A at 1, 4, 7; B at 2, 5, 8; C at 3, 6, 9."],
       examples=[
           WE("The border repeats A, B, C. Write the position of the nth appearance of C, B and A, and list the first "
              "three positions of each.",
              ["C first appears at position 3 and then 6, 9, so the nth C is at 3n.",
               "B is one place before C, so the nth B is at 3n − 1: for n = 1, 2, 3 the positions are 2, 5, 8.",
               "A is two places before C, so the nth A is at 3n − 2: for n = 1, 2, 3 the positions are 1, 4, 7.",
               "For n = 1, 2, 3 the C positions are 3, 6, 9."],
              "C at 3n, B at 3n − 1, A at 3n − 2", ncert=["4.6.saree_pos"])],
       key_terms=["position", "repeating pattern"], minutes=10),
     A("T10.C2", "Which design is at position 122?", "Apply",
       "Students divide a position number by 3, read the remainder, and decide which design appears at positions "
       "99, 122 and 148.",
       textbook=["Given a position number can we find out the design that appears there? Which Design appears at "
                 "Position 122?",
                 "If the position is a multiple of 3, then clearly we have Design C. As seen earlier, if the "
                 "position is one less than a multiple of 3, it has Design B, and if it is 2 less than a multiple of "
                 "3, then it has Design A.",
                 "Can the remainder obtained by dividing the position number by 3 be used for this? Observe the "
                 "table below. Position 99: quotient 33, remainder 0. Position 122: quotient 40, remainder 2. "
                 "Position 148: quotient 49, remainder 1.",
                 "Use this to find what design appears at positions 99, 122, and 148."],
       teach=["Predict first: at position 122, is it a multiple of 3, one less than a multiple, or two less?",
              "Divide by 3. Remainder 0 means a multiple of 3, so C. Remainder 2 means one less than the next "
              "multiple, so B. Remainder 1 means two less than the next multiple, so A.",
              "Check: 3 × 41 = 123, and 122 is one less, so B."],
       examples=[
           WE("Find the design at positions 99, 122 and 148 by dividing each position by 3.",
              ["99 ÷ 3: quotient 33, remainder 0. A multiple of 3, so Design C.",
               "122 ÷ 3: quotient 40, remainder 2. 3 × 41 = 123 and 122 is one less, so Design B.",
               "148 ÷ 3: quotient 49, remainder 1. 3 × 50 = 150 and 148 is two less, so Design A."],
              "Position 99 is C, position 122 is B, position 148 is A", ncert=["4.6.saree_design"])],
       key_terms=["remainder"], misconceptions=["M_REMAINDER_DESIGN"], minutes=10),
     DOER("T10.C3", "Practice: name the design at a position", None, "Apply",
          "Students find the design at a given position from the remainder on division by 3, and give the position of "
          "the nth appearance of each design.",
          ["Divide the position by 3 and read the remainder.",
           "Remainder 0 gives C, 2 gives B, 1 gives A.",
           "The nth C is at 3n, the nth B at 3n − 1, the nth A at 3n − 2."])]))

# ============================== T11 Calendar =================================================================
TOPICS.append(TOPIC(
    "T11", "M3", "Patterns in a Calendar", ["4.6"], "Analyze",
    "Students notice that diagonal sums in a 2 by 2 calendar square are equal, prove it for every square by naming "
    "the top left number a, and prove that a cross shape of five dates always adds to five times the centre.",
    "Naming one date a and writing the other dates as a plus or minus a number lets an expression prove a pattern for "
    "every square or shape on an endless calendar.",
    [A("T11.C1", "Diagonal sums in a 2 by 2 square", "Analyze",
       "Students find that the diagonal sums of a marked 2 by 2 square are equal, write the other three dates in "
       "terms of the top left date a, and prove that both sums are 2a + 8.",
       textbook=["Patterns in a Calendar",
                 "Here is the calendar of November 2024. Consider 2 × 2 squares, as marked in the calendar. The "
                 "numbers in this square show an interesting property.",
                 "Let us take the marked 2 × 2 square, and consider the numbers lying on the diagonals; 12 and 20; "
                 "13 and 19. Find their sums; 12 + 20, 13 + 19. What do you observe? They are equal.",
                 "Let us extend the numbers in the calendar beyond 30, creating endless rows. Will the diagonal sums "
                 "be equal in every 2 × 2 square in this endless grid? How can we be sure?",
                 "To be sure of this we cannot check with all 2 × 2 squares as there are an unlimited number of "
                 "them. Let us consider a 2 × 2 square. Its top left number can be any number. Let us call it 'a'.",
                 "Given that we know the top left number, how do we find the other numbers in this 2 × 2 square? As "
                 "we have been doing, first let us describe the other numbers in words. The number to the right of "
                 "'a' will be 1 more than it. The number below 'a' will be 7 more than it. The number diagonal to "
                 "'a' will be 8 more than it.",
                 "So the other numbers in the 2 × 2 square can be represented as a, a + 1, a + 7, a + 8. Let us find "
                 "the diagonal sums; a + (a + 8), and (a + 1) + (a + 7). Let us simplify them.",
                 "Since the terms can be added in any order, the brackets can be opened. a + (a + 8) = a + a + 8 = "
                 "2a + 8. (a + 1) + (a + 7) = a + 1 + a + 7 = a + a + 1 + 7 = 2a + 8.",
                 "We see that both diagonal sums are equal to 2a + 8 (8 more than 2 times a). Verify this expression "
                 "for diagonal sums by considering any 2 × 2 square and taking its top left number to be 'a'. Thus, "
                 "we have shown that diagonal sums are equal for any value of a, i.e., for any 2 × 2 square!"],
       teach=["Predict first: in the marked square with 12, 13, 19 and 20, add each diagonal. What do you see, and "
              "will it happen in every square?",
              "A calendar row has 7 dates, so the date to the right is 1 more, the date below is 7 more, and the "
              "date diagonally below is 8 more.",
              "Name the top left date a and write the square as a, a + 1, a + 7, a + 8.",
              "Both diagonal sums simplify to 2a + 8, so they are equal for every a."],
       examples=[
           WE("In the calendar square with 12, 13 on the top and 19, 20 below, add the two diagonals, then show that "
              "the diagonal sums are equal for every 2 by 2 square by calling the top left date a.",
              ["Diagonals: 12 + 20 = 32 and 13 + 19 = 32. They are equal.",
               "A week has 7 days, so with top left a: right is a + 1, below is a + 7, diagonal is a + 8.",
               "First diagonal: a + (a + 8) = a + a + 8 = 2a + 8.",
               "Second diagonal: (a + 1) + (a + 7) = a + a + 1 + 7 = 2a + 8.",
               "Both equal 2a + 8, for every a. Check with a = 12: 2 × 12 + 8 = 32."],
              "Both diagonal sums are 2a + 8; for the marked square both are 32", ncert=["4.6.cal_diag"]),
           WE("Check the expression 2a + 8 on another square whose top left date is 9, and say why a table of examples "
              "is not enough to be sure.",
              ["With a = 9 the square is 9, 10, 16, 17.", "Diagonals: 9 + 17 = 26 and 10 + 16 = 26.",
               "2a + 8 = 2 × 9 + 8 = 26. It matches.",
               "There are unlimited squares on an endless calendar, so checking some cannot show all. The "
               "expression with a covers every square at once."],
              "26 for both diagonals when a = 9, and the expression proves it for all squares",
              ncert=["4.6.cal_verify"])],
       key_terms=["diagonal"], minutes=14),
     A("T11.C2", "A cross of five dates: sum is five times the centre", "Analyze",
       "Students add the five dates in a cross shape on the calendar, see that the sum is 5 times the centre, and "
       "prove it for every cross by naming the centre a.",
       textbook=["Consider a set of numbers from the calendar (having endless rows) forming under the following "
                 "shape: one number on top, three in the middle row and one below, 8; 14, 15, 16; 22. Find the sum of "
                 "all the numbers. Compare it with the number in the centre: 15. Repeat this for another set of "
                 "numbers that forms this shape. What do you observe?",
                 "We see that the total sum is always 5 times the number in the centre. Will this always happen? How "
                 "do you show this? [Hint: Consider a general set of numbers that forms this shape. Take the number "
                 "at the centre to be 'a'. Express the other numbers in terms of 'a'.]",
                 "Math Talk: Find other shapes for which the sum of the numbers within the figure is always a "
                 "multiple of one of the numbers.",
                 "This problem is an example that shows the power of algebraic modelling in verifying whether a "
                 "pattern will always hold."],
       teach=["Predict first: add 8, 14, 15, 16 and 22. How does the total compare with the centre 15?",
              "Take the centre as a. The date above is 7 less, the date below is 7 more, left is 1 less and right is "
              "1 more.",
              "The five dates are a − 7, a − 1, a, a + 1, a + 7, and their sum is 5a.",
              "Math Talk: other shapes work too, for example a plus shape or a row of three dates, when the dates "
              "are balanced round a centre."],
       examples=[
           WE("Add the cross of dates 8, 14, 15, 16, 22 and compare with the centre, then prove the pattern for any "
              "cross with centre a.",
              ["8 + 14 + 15 + 16 + 22 = 75, and 5 × 15 = 75. The sum is 5 times the centre.",
               "With centre a: above is a − 7, left is a − 1, right is a + 1, below is a + 7.",
               "Sum = (a − 7) + (a − 1) + a + (a + 1) + (a + 7).",
               "Group the terms: 5a + (−7 − 1 + 1 + 7) = 5a + 0 = 5a.",
               "So the sum is 5 times the centre for every cross."],
              "75 for the marked cross, and 5a for every cross with centre a", ncert=["4.6.cal_cross"]),
           WE("Find another shape on the calendar whose sum is a multiple of one of its numbers: a row of three dates "
              "with the middle date a.",
              ["The row is a − 1, a, a + 1.", "Sum = (a − 1) + a + (a + 1) = 3a + (−1 + 1) = 3a.",
               "So the sum of three dates in a row is 3 times the middle date.",
               "Check with 14, 15, 16: 14 + 15 + 16 = 45 and 3 × 15 = 45.",
               "Other balanced shapes, such as a column of three dates, also give multiples of the centre."],
              "3a for a row of three dates with middle a; 45 for 14, 15, 16 (open ended: other shapes possible)",
              ncert=["4.6.cal_talk"])],
       key_terms=["algebraic modelling"], minutes=12),
     DOER("T11.C3", "Practice: prove it with a letter-number", "grid_shape_prover", "Analyze",
          "Students choose a shape on an endless calendar, name its centre a, write the other dates in terms of a, "
          "and show that the sum is always a multiple of a number in the shape.",
          ["Name one date a and write the others as a plus or minus a number.",
           "A date to the right is a + 1, below is a + 7.",
           "Add the expressions, group the like terms and read the result."])]))

# ============================== T12 Matchstick patterns ======================================================
TOPICS.append(TOPIC(
    "T12", "M3", "Matchstick Patterns", ["4.6"], "Apply",
    "Students find the number of matchsticks at any step of a growing pattern from the 2 added at each step, write "
    "the formula 2y + 1, check two forms are equal by simplifying, and split the count by orientation.",
    "A pattern that adds the same amount at each step has a formula in the step number, and two formulas for the same "
    "pattern are equal when they simplify to the same expression.",
    [A("T12.C1", "How many matchsticks in Step y?", "Apply",
       "Students count matchsticks in a growing triangle pattern, use the 2 added at each step to reach far steps, and "
       "write the formula 3 + 2 × (y − 1) and its simplified form 2y + 1.",
       textbook=["Matchstick Patterns",
                 "Look at the picture below. It is a pattern using matchsticks. Can you identify what the pattern "
                 "is? We can see that Step 1 has 1 triangle, Step 2 has 2 triangles, Step 3 has 3 triangles, and so on.",
                 "Can you tell how many matchsticks there will be in the next step, Step 5? It is 11. You can also "
                 "draw this and see. How many matchsticks will there be in Step 33, Step 84, and Step 108? Of course, "
                 "we can draw and count, but is there a quicker way to find the answers using the pattern present "
                 "here?",
                 "What is the general rule to find the number of matchsticks in the next step? We can see that at "
                 "each step 2 matchsticks are placed to get the next one, i.e., the number of matchsticks increases "
                 "by 2 every time. Step number 1 to 6: matchsticks 3, 5, 7, 9, 11, 13.",
                 "Think of a way to use this to find out the number of matchsticks in Step 33 (without continuing to "
                 "write the numbers). As each time 2 matchsticks are being added, finding out how many 2s will be "
                 "added in Step 33 will help. Step 2 is 3 + 2, Step 3 is 3 + 2 + 2, Step 4 is 3 + 2 + 2 + 2.",
                 "The number of matchsticks needed to make 33 triangles (Step 33) is ___. Similarly, find the number "
                 "of matchsticks needed for Step 84 and Step 108.",
                 "What could be an expression describing the rule/formula to find out the number of matchsticks at "
                 "any step? The pattern is such that in Step 10, nine 2s and an added 3 (3 + 2 × 9) gives the number "
                 "of matchsticks; in Step 11, ten 2s and an added 3 (3 + 2 × 10) gives the number of matchsticks. "
                 "For step y, what is the expression? It is: one less than y (i.e. y − 1) 2s and a 3. Therefore, the "
                 "expression is 3 + 2 × (y − 1). This expression gives the number of matchsticks in Step y.",
                 "You might have already noticed that there is a 2 in the first step also, 3 = 1 + 2. Using this, the "
                 "expression we get is 2y + 1. Does the above expression also give the number of matchsticks at each "
                 "step correctly? Are these expressions the same? We can check by simplifying the expression "
                 "3 + 2 × (y − 1). 3 + 2 × (y − 1) = 3 + 2y − 2 = 2y + 1. Both expressions are the same."],
       teach=["Predict first: Step 1 has 3 matchsticks, Step 2 has 5, Step 3 has 7. How many in Step 5, and in Step "
              "33 without drawing?",
              "Each step adds 2 matchsticks, so Step 33 is 3 plus thirty-two 2s.",
              "For Step y there are (y − 1) 2s added to the 3, which gives 3 + 2 × (y − 1).",
              "Simplify: 3 + 2y − 2 = 2y + 1. The two formulas are the same."],
       examples=[
           WE("Find the number of matchsticks in Step 5, Step 33, Step 84 and Step 108, using the 2 added at each step.",
              ["The counts 3, 5, 7, 9, 11, 13 grow by 2 each step, so Step 5 has 11.",
               "Step 33: thirty-two 2s are added to 3, so 3 + 2 × 32 = 3 + 64 = 67.",
               "Step 84: 3 + 2 × 83 = 3 + 166 = 169.", "Step 108: 3 + 2 × 107 = 3 + 214 = 217."],
              "Step 5: 11, Step 33: 67, Step 84: 169, Step 108: 217", ncert=["4.6.match_far"]),
           WE("Write a formula for the matchsticks in Step y in two ways, and show they are equal by simplifying.",
              ["In Step y there is a 3 and (y − 1) 2s added, so the count is 3 + 2 × (y − 1).",
               "Since Step 1 is 3 = 1 + 2, the count can also be seen as 2y + 1.",
               "Simplify the first form: 3 + 2 × (y − 1) = 3 + 2y − 2 = 2y + 1.",
               "Both forms are the same. Check Step 33: 2 × 33 + 1 = 67."],
              "3 + 2 × (y − 1) = 2y + 1", ncert=["4.6.match_formula"])],
       key_terms=["formula", "step"], misconceptions=["M_PATTERN_STEP"], minutes=14),
     A("T12.C2", "Counting by orientation: horizontal and diagonal", "Apply",
       "Students count horizontal and diagonal matchsticks at each step separately, write an expression for each in "
       "terms of y, and check that the two add up to 2y + 1.",
       textbook=["There is a different way to count, or see the pattern. Let us take a look at the picture again.",
                 "Matchsticks are placed in two orientations: (a) horizontal ones at the top and bottom, and (b) the "
                 "ones placed diagonally in the middle. For example, in step 2 there are 2 matchsticks placed "
                 "horizontally and 3 matchsticks placed diagonally.",
                 "What are these numbers in Step 3 and Step 4? How does the number of matchsticks change in each "
                 "orientation as the steps increase? Write an expression for the number of matchsticks at Step 'y' "
                 "in each orientation. Do the two expressions add up to 2y + 1?"],
       teach=["Predict first: in Step 2 there are 2 horizontal and 3 diagonal matchsticks. What about Step 3 and "
              "Step 4?",
              "Horizontal ones are y in Step y, diagonal ones are y + 1.",
              "Add the two expressions: y + (y + 1) = 2y + 1, the same formula as before."],
       examples=[
           WE("Count the horizontal and diagonal matchsticks in Steps 2, 3 and 4, then write an expression for each "
              "orientation in Step y and add them.",
              ["Step 2: 2 horizontal and 3 diagonal. Step 3: 3 horizontal and 4 diagonal. Step 4: 4 horizontal and 5 "
               "diagonal.",
               "The horizontal count equals the step number, so it is y.",
               "The diagonal count is one more than the step number, so it is y + 1.",
               "Total = y + (y + 1) = 2y + 1.",
               "Check Step 4: 4 + 5 = 9, and 2 × 4 + 1 = 9."],
              "Horizontal y, diagonal y + 1, and together 2y + 1", ncert=["4.6.match_orient"])],
       key_terms=["orientation"], minutes=10),
     DOER("T12.C3", "Practice: find the formula of a pattern", "pattern_formula_finder", "Apply",
          "Students find the formula for a growing pattern from its first steps, simplify it, and use it for far "
          "steps and for other questions about simplifying, adding, subtracting and describing expressions.",
          ["Find how much is added at each step.",
           "Write the count at Step y and simplify it.",
           "Check the formula against the first few steps."],
          items=[
              FIO("4.6.FiO_1", "Figure it Out (patterns), Q1",
                  "One plate of Jowar roti costs 30 rupees and one plate of Pulao costs 20 rupees. If x plates of "
                  "Jowar roti and y plates of pulao were ordered in a day, which expression(s) describe the total "
                  "amount in rupees earned that day? (a) 30x + 20y (b) (30 + 20) × (x + y) (c) 20x + 30y "
                  "(d) (30 + 20) × x + y (e) 30x − 20y",
                  ["The Jowar roti brings in 30 rupees for each of x plates, so 30x.",
                   "The pulao brings in 20 rupees for each of y plates, so 20y.",
                   "The total earned is the sum 30x + 20y, option (a).",
                   "Option (b) charges 50 for every plate of either kind; (c) swaps the prices; (d) adds only y once; "
                   "(e) subtracts. Check with x = 1 and y = 1: 30 + 20 = 50 for (a), but (b) gives 100 and (e) gives "
                   "10."],
                  "(a) 30x + 20y"),
              FIO("4.6.FiO_2", "Figure it Out (patterns), Q2",
                  "Pushpita sells two types of flowers on Independence day: champak and marigold. p customers only "
                  "bought champak, q customers only bought marigold, and r customers bought both. On the same day, "
                  "she gave away a tiny national flag to every customer. How many flags did she give away that day? "
                  "(a) p + q + r (b) p + q + 2r (c) 2 × (p + q + r) (d) p + q + r + 2 (e) p + q + r + 1 "
                  "(f) 2 × (p + q)",
                  ["Every customer gets one flag, whatever they bought.",
                   "The customers are p who bought only champak, q who bought only marigold, and r who bought both.",
                   "A customer who bought both is still one customer, so r is counted once.",
                   "Flags = p + q + r, option (a).",
                   "Check with p = 3, q = 4, r = 2: 9 customers, and p + q + r = 9, while p + q + 2r would be 11."],
                  "(a) p + q + r"),
              FIO("4.6.FiO_3", "Figure it Out (patterns), Q3",
                  "A snail is trying to climb along the wall of a deep well. During the day it climbs up u cm and "
                  "during the night it slowly slips down d cm. This happens for 10 days and 10 nights. "
                  "(a) Write an expression describing how far away the snail is from its starting position. "
                  "(b) What can we say about the snail's movement if d > u?",
                  ["(a) In one day and night the snail moves u − d cm.",
                   "For 10 days and 10 nights the distance is 10 × (u − d) = 10(u − d) cm.",
                   "(b) If d > u, then u − d is negative, so every day and night ends lower than it began.",
                   "The snail slips down more than it climbs, so it never reaches the top."],
                  "(a) 10(u − d) cm (b) it slips down more than it climbs, so it never reaches the top"),
              FIO("4.6.FiO_4", "Figure it Out (patterns), Q4",
                  "Radha is preparing for a cycling race and practices daily. The first week she cycles 5 km every "
                  "day. Every week she increases the daily distance cycled by z km. How many kilometres would Radha "
                  "have cycled after 3 weeks?",
                  ["Week 1: 5 km a day for 7 days is 5 × 7 = 35 km.",
                   "Week 2: the daily distance is 5 + z, so (5 + z) × 7 = 35 + 7z km.",
                   "Week 3: the daily distance is 5 + 2z, so (5 + 2z) × 7 = 35 + 14z km.",
                   "Total = 35 + (35 + 7z) + (35 + 14z) = 105 + 21z km."],
                  "105 + 21z km"),
              FIO("4.6.FiO_5", "Figure it Out (patterns), Q5",
                  "A figure shows ovals that hold expressions and boxes that hold operations, joined by paths. Along "
                  "one path the expression w + 2 becomes 4w + 20. Fill in the missing blanks on the remaining paths. "
                  "The other paths use the operations multiply by 3, subtract 8, subtract 4 and subtract 4, "
                  "starting from w + 2 and w − 3, and the missing ovals are to be found.",
                  ["Given path: w + 2, add 3 gives w + 5, then multiply by 4 gives 4w + 20.",
                   "Multiply w − 3 by 3: 3(w − 3) = 3w − 9.",
                   "From w + 2, subtract 8 gives w − 6, then subtract 4 gives w − 10.",
                   "From w + 2, subtract 4 gives w − 2, then multiply by 3 gives 3w − 6."],
                  "3w − 9; w − 6 then w − 10; w − 2 then 3w − 6"),
              FIO("4.6.FiO_6", "Figure it Out (patterns), Q6",
                  "A local train from Yahapur to Vahapur stops at three stations at equal distances along the way. "
                  "The time taken in minutes to travel from one station to the next station is the same and is "
                  "denoted by t. The train stops for 2 minutes at each of the three stations. (a) If t = 4, what is "
                  "the time taken to travel from Yahapur to Vahapur? (b) What is the algebraic expression for the "
                  "time taken to travel from Yahapur to Vahapur? [Hint: Draw a rough diagram to visualise the "
                  "situation]",
                  ["Three stations in between make four equal journeys: Yahapur to station 1, 1 to 2, 2 to 3, 3 to "
                   "Vahapur.",
                   "Travel time is 4 × t, and the stops are 3 × 2 = 6 minutes.",
                   "(a) With t = 4: 4 × 4 + 6 = 16 + 6 = 22 minutes.",
                   "(b) The expression is 4t + 6 minutes."],
                  "(a) 22 minutes (b) 4t + 6 minutes"),
              FIO("4.6.FiO_7", "Figure it Out (patterns), Q7",
                  "Simplify the following expressions: (a) 3a + 9b − 6 + 8a − 4b − 7a + 16 (b) 3(3a − 3b) − 8a − 4b "
                  "− 16 (c) 2(2x − 3) + 8x + 12 (d) 8x − (2x − 3) + 12 (e) 8h − (5 + 7h) + 9 "
                  "(f) 23 + 4(6m − 3n) − 8n − 3m − 18",
                  ["(a) a terms: 3a + 8a − 7a = 4a. b terms: 9b − 4b = 5b. Numbers: −6 + 16 = 10. So 4a + 5b + 10.",
                   "(b) 9a − 9b − 8a − 4b − 16 = a − 13b − 16.",
                   "(c) 4x − 6 + 8x + 12 = 12x + 6.", "(d) 8x − 2x + 3 + 12 = 6x + 15.",
                   "(e) 8h − 5 − 7h + 9 = h + 4.",
                   "(f) 23 + 24m − 12n − 8n − 3m − 18 = 21m − 20n + 5."],
                  "(a) 4a + 5b + 10 (b) a − 13b − 16 (c) 12x + 6 (d) 6x + 15 (e) h + 4 (f) 21m − 20n + 5"),
              FIO("4.6.FiO_8", "Figure it Out (patterns), Q8",
                  "Add the expressions given below: (a) 4d − 7c + 9 and 8c − 11 + 9d (b) −6f + 19 − 8s and −23 + "
                  "13f + 12s (c) 8d − 14c + 9 and 16c − (11 + 9d) (d) 6f − 20 + 8s and 23 − 13f − 12s "
                  "(e) 13m − 12n and 12n − 13m (f) −26m + 24n and 26m − 24n",
                  ["(a) d terms 4d + 9d = 13d, c terms −7c + 8c = c, numbers 9 − 11 = −2. So 13d + c − 2.",
                   "(b) f terms −6f + 13f = 7f, s terms −8s + 12s = 4s, numbers 19 − 23 = −4. So 7f + 4s − 4.",
                   "(c) Open the bracket: 16c − 11 − 9d. Then d terms 8d − 9d = −d, c terms −14c + 16c = 2c, numbers "
                   "9 − 11 = −2. So 2c − d − 2.",
                   "(d) f terms 6f − 13f = −7f, s terms 8s − 12s = −4s, numbers −20 + 23 = 3. So −7f − 4s + 3.",
                   "(e) 13m − 13m = 0 and −12n + 12n = 0, so 0.", "(f) −26m + 26m = 0 and 24n − 24n = 0, so 0."],
                  "(a) 13d + c − 2 (b) 7f + 4s − 4 (c) 2c − d − 2 (d) −7f − 4s + 3 (e) 0 (f) 0"),
              FIO("4.6.FiO_9", "Figure it Out (patterns), Q9",
                  "Subtract the expressions given below: (a) 9a − 6b + 14 from 6a + 9b − 18 (b) −15x + 13 − 9y from "
                  "7y − 10 + 3x (c) 17g + 9 − 7h from 11 − 10g + 3h (d) 9a − 6b + 14 from 6a − (9b + 18) "
                  "(e) 10x + 2 + 10y from −3y + 8 − 3x (f) 8g + 4h − 10 from 7h − 8g + 20",
                  ["Subtracting A from B means B − (A), and the bracket changes every sign in A.",
                   "(a) (6a + 9b − 18) − (9a − 6b + 14) = −3a + 15b − 32.",
                   "(b) (7y − 10 + 3x) − (−15x + 13 − 9y) = 18x + 16y − 23.",
                   "(c) (11 − 10g + 3h) − (17g + 9 − 7h) = 10h − 27g + 2.",
                   "(d) (6a − 9b − 18) − (9a − 6b + 14) = −3a − 3b − 32.",
                   "(e) (−3y + 8 − 3x) − (10x + 2 + 10y) = −13x − 13y + 6.",
                   "(f) (7h − 8g + 20) − (8g + 4h − 10) = 3h − 16g + 30."],
                  "(a) −3a + 15b − 32 (b) 18x + 16y − 23 (c) 10h − 27g + 2 (d) −3a − 3b − 32 (e) −13x − 13y + 6 "
                  "(f) 3h − 16g + 30"),
              FIO("4.6.FiO_10", "Figure it Out (patterns), Q10",
                  "Describe situations corresponding to the following algebraic expressions: (a) 8x + 3y "
                  "(b) 15x − 2x",
                  ["Open ended. Any sensible story with the right quantities works.",
                   "(a) A fruit seller sells mangoes at 8 rupees each and bananas at 3 rupees each. A customer buys "
                   "x mangoes and y bananas. The total cost is 8x + 3y rupees.",
                   "(b) A packet has 15 pencils and each pencil costs x rupees. Two pencils from the packet are not "
                   "sold. The amount received is 15x − 2x = 13x rupees."],
                  "Open ended. Model answers: (a) x mangoes at 8 rupees and y bananas at 3 rupees (b) a packet of 15 "
                  "pencils at x rupees with 2 unsold, giving 13x rupees"),
              FIO("4.6.FiO_11", "Figure it Out (patterns), Q11",
                  "Imagine a straight rope. If it is cut once as shown in the picture, we get 2 pieces. If the rope "
                  "is folded once and then cut as shown, we get 3 pieces. Observe the pattern and find the number of "
                  "pieces if the rope is folded 10 times and cut. What is the expression for the number of pieces "
                  "when the rope is folded r times and cut?",
                  ["With no fold, one cut gives 2 pieces. One fold and a cut gives 3 pieces.",
                   "Each extra fold adds one more piece, so the pieces are the number of folds plus 2.",
                   "Folded 10 times: 10 + 2 = 12 pieces.", "Folded r times: r + 2 pieces."],
                  "12 pieces for 10 folds, and r + 2 pieces for r folds", tool="pattern_formula_finder"),
              FIO("4.6.FiO_12", "Figure it Out (patterns), Q12",
                  "Look at the matchstick pattern of squares in a row. Observe and identify the pattern. How many "
                  "matchsticks are required to make 10 such squares? How many are required to make w squares?",
                  ["One square needs 4 matchsticks. Each new square joined to the row adds 3 matchsticks.",
                   "For 10 squares: 4 + 3 × 9 = 4 + 27 = 31 matchsticks.",
                   "For w squares: 4 + 3 × (w − 1) = 4 + 3w − 3 = 3w + 1 matchsticks.",
                   "Check w = 10: 3 × 10 + 1 = 31."],
                  "31 matchsticks for 10 squares, and 4 + 3(w − 1) = 3w + 1 for w squares",
                  tool="pattern_formula_finder"),
              FIO("4.6.FiO_13", "Figure it Out (patterns), Q13",
                  "Have you noticed how the colours change in a traffic signal? The sequence of colour changes "
                  "repeats red, yellow, green, yellow, then red again. Find the colour at positions 90, 190, and "
                  "343. Write expressions to describe the positions for each colour.",
                  ["The cycle has 4 positions: red at 1, yellow at 2, green at 3, yellow at 4, then it repeats.",
                   "Divide each position by 4. Remainder 2 or 0 means yellow, remainder 1 means red, remainder 3 "
                   "means green.",
                   "90 ÷ 4 leaves remainder 2, so yellow. 190 ÷ 4 leaves remainder 2, so yellow. 343 ÷ 4 leaves "
                   "remainder 3, so green.",
                   "Red is at 4n − 3, yellow is at 2n (every even position), green is at 4n − 1."],
                  "Positions 90 and 190 are yellow, 343 is green; red at 4n − 3, yellow at 2n, green at 4n − 1"),
              FIO("4.6.FiO_14", "Figure it Out (patterns), Q14",
                  "Observe the pattern of squares that grows with each step: Step 1 has 5 squares, and each step "
                  "adds 4 squares. How many squares will be there in Step 4, Step 10, Step 50? Write a general "
                  "formula. How would the formula change if we want to count the number of vertices of all the "
                  "squares?",
                  ["Step 1 has 5 squares and each step adds 4, so Step n has 5 + (n − 1) × 4 squares.",
                   "Simplify: 5 + 4n − 4 = 4n + 1.",
                   "Step 4: 4 × 4 + 1 = 17. Step 10: 4 × 10 + 1 = 41. Step 50: 4 × 50 + 1 = 201.",
                   "Each square has 4 vertices, so vertices = 4 × (4n + 1) = 16n + 4."],
                  "17, 41 and 201 squares; the formula is 4n + 1; vertices 16n + 4",
                  tool="pattern_formula_finder"),
              FIO("4.6.FiO_15", "Figure it Out (patterns), Q15",
                  "Numbers are written in a particular sequence in this endless 4-column grid: row 1 holds 1, 2, 3, "
                  "4; row 2 holds 5, 6, 7, 8; and so on. (a) Give expressions to generate all the numbers in a given "
                  "column (1, 2, 3, 4). (b) In which row and column will the following numbers appear: (i) 124 "
                  "(ii) 147 (iii) 201 (c) What number appears in row r and column c? (d) Observe the positions of "
                  "multiples of 3. Do you see any pattern in it? List other patterns that you see.",
                  ["(a) Row r starts after r − 1 full rows of 4 numbers. Column 1: 4(r − 1) + 1, column 2: "
                   "4(r − 1) + 2, column 3: 4(r − 1) + 3, column 4: 4(r − 1) + 4.",
                   "(b) 124 ÷ 4 leaves remainder 0, so 124 = 4 × 30 + 4, giving r − 1 = 30 and c = 4: row 31, column "
                   "4. 147 = 4 × 36 + 3: row 37, column 3. 201 = 4 × 50 + 1: row 51, column 1.",
                   "(c) The number in row r and column c is 4(r − 1) + c.",
                   "(d) Multiples of 3 fall in the columns 3, 2, 1, 4, then repeat 3, 2, 1, 4.",
                   "Other patterns: every number in column 4 is a multiple of 4; even numbers appear only in "
                   "columns 2 and 4; odd numbers appear only in columns 1 and 3."],
                  "(a) 4(r − 1) + c for column c (b) 124 at row 31 column 4, 147 at row 37 column 3, 201 at row 51 "
                  "column 1 (c) 4(r − 1) + c (d) multiples of 3 follow the columns 3, 2, 1, 4 repeating; column 4 "
                  "holds multiples of 4; even numbers sit in columns 2 and 4; odd numbers in columns 1 and 3")],
          ncert=["4.6.FiO_%d" % i for i in range(1, 16)], misconceptions=["M_PATTERN_STEP"])]))

# ============================== T13 Summary ==================================================================
TOPICS.append(TOPIC(
    "T13", "M4", "Summary: Expressions using Letter-Numbers", ["Summary"], "Remember",
    None,
    "One short expression for every order of laddus, letter-numbers, simplest forms, and patterns that expressions "
    "can prove.",
    [A("T13.C1", "What letter-numbers let us say", "Remember",
       "Students restate how letter-numbers and expressions describe relationships, how like terms are added to reach "
       "simplest forms, and how expressions model and prove patterns.",
       textbook=["Summary",
                 "Algebraic expressions are used in formulas to model patterns and mathematical relationships "
                 "between quantities, and to make predictions.",
                 "Algebraic expressions use not only numbers but also letter-numbers. The rules for manipulating "
                 "arithmetic expressions also apply to algebraic expressions. These rules can be used to reduce "
                 "algebraic expressions to their simplest forms."],
       teach=["Our opening question is settled: a letter-number for the changing number of coconuts and another for "
              "the kilograms of jaggery give one short rule for any order.",
              "Like terms add into one term; unlike terms stay apart; a minus sign before a bracket changes the "
              "sign of every term inside.",
              "Patterns such as the saree border, the calendar and the matchsticks have formulas, and an expression "
              "can prove a pattern for every case at once.",
              "Still open for you: invent a rule of your own, write it as an expression, and challenge a friend to "
              "find it."],
       ncert=["summary"], video_focus=["RECAP"], minutes=8)],
    topic_type="summary"))
