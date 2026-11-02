# -*- coding: utf-8 -*-
"""Topics T5 to T8 (module M3: products, divisibility and puzzles; summary). Book sections 6.5, 6.6, pp 142 to 147."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T5 The largest product =====================================================
TOPICS.append(TOPIC(
    "T5", "M3", "The Largest Product", ["6.5"], "Analyze",
    "Students list the six ways to place three digits in a two digit by one digit product, compare them in pairs "
    "to find the largest product, and prove with letter-numbers that the largest digit should be the multiplier.",
    "With digits p < q < r the largest product is qp × r: the largest digit multiplies, and the other two digits "
    "form the multiplicand in decreasing order.",
    [A("T5.C1", "Six ways to place three digits", "Analyze",
       "Students list the six ways to place the digits 2, 3 and 5 in a two digit by one digit product, compare the "
       "products in pairs, and find the largest product.",
       textbook=["6.5 The Largest Product",
                 "Fill the digits 2, 3, and 5 in a two digit number times a one digit number, using each digit once. "
                 "What is the largest product possible?",
                 "Let us approach this problem systematically. There are six ways to place three digits: We can fill "
                 "the first box with 2, 3 or 5. For each of these choices, we have 2 ways of filling the remaining 2 "
                 "digits. The six options are 23 × 5, 25 × 3, 32 × 5, 35 × 2, 52 × 3, 53 × 2.",
                 "How do we find the largest product among these six options?",
                 "We can group them in pairs where the multiplier is the same. 35 × 2 and 53 × 2. 25 × 3 and 52 × 3. "
                 "23 × 5 and 32 × 5.",
                 "In each pair, the one with the larger multiplicand generates the larger product, so we can reduce the "
                 "comparison to these three expressions. 53 × 2. 52 × 3. 32 × 5.",
                 "It is clear that 52 × 3 is bigger than 53 × 2, so we only need to compare 52 × 3 and 32 × 5. Let us "
                 "expand these. 32 × 5 = (3 × 10 × 5) + (2 × 5). 52 × 3 = (5 × 10 × 3) + (2 × 3).",
                 "The first terms in both expressions are the same. The second term shows that 32 × 5 is larger, and "
                 "hence the largest of the six possible products we can form with 2, 3 and 5."],
       teach=["Predict first: should the 5 go in the tens place or be the multiplier?",
              "List all six placements: three choices for the first box, then two for the next.",
              "Pair the products with the same multiplier and keep the larger one of each pair.",
              "Compare 52 × 3 and 32 × 5 by place value: both have 150 from the tens, and the ones part decides."],
       examples=[
           WE("Place the digits 2, 3 and 5 to make the largest two digit by one digit product.",
              ["The six options are 23 × 5, 25 × 3, 32 × 5, 35 × 2, 52 × 3 and 53 × 2.",
               "In each pair with the same multiplier keep the larger: 53 × 2, 52 × 3 and 32 × 5.",
               "53 × 2 = 106, 52 × 3 = 156 and 32 × 5 = 160.",
               "By place value: 32 × 5 = 150 + 10 and 52 × 3 = 150 + 6, so 32 × 5 wins."],
              "32 × 5 = 160 is the largest product",
              ncert=["6.5.digits235", "6.5.six_pairs"])],
       key_terms=["product", "multiplier", "multiplicand"], misconceptions=["M_BIG_TENS"], minutes=10),
     A("T5.C2", "Why the largest digit should multiply", "Analyze",
       "Students write the six products for digits p < q < r with letters, compare them in pairs, and show that "
       "qp × r is always the largest product.",
       textbook=["In this case, we used the largest digit as the multiplier. The other two digits were arranged in "
                 "decreasing order to form the multiplicand. Will this always be the case? Let us find out using "
                 "algebra.",
                 "Suppose p, q, and r are the three digits such that p < q < r.",
                 "As before, we have six possible products, which we group by the multiplier: qr × p, rq × p; pr × q, "
                 "rp × q; pq × r, qp × r.",
                 "In each pair, the multiplicand with the larger tens digit forms the larger product. So we have three "
                 "products to compare: rq × p, rp × q, qp × r.",
                 "Since q > p, we can see that rp × q is bigger than rq × p. This leaves us with a comparison between "
                 "qp × r and rp × q. If we expand these, we get qp × r = (10 × q × r) + (p × r), rp × q = "
                 "(10 × r × q) + (p × q).",
                 "Once again, the first term is the same in both expressions. Since r > q the second term of the first "
                 "expression is larger, so the largest product is qp × r. This matches our earlier observation that the "
                 "largest digit should be the multiplier and the other two digits should be arranged in decreasing "
                 "order to form the multiplicand."],
       teach=["Predict first: does the rule from 2, 3 and 5 work for any three different digits?",
              "With p < q < r, pair the products by multiplier and keep rq × p, rp × q and qp × r.",
              "rp × q beats rq × p: expanded, both have the ones part p × q, and 10 × r × q is larger than 10 × r × p.",
              "Expanding qp × r and rp × q, both have 10 × q × r; the ones parts are p × r and p × q, and r is larger."],
       examples=[
           WE("Show that qp × r is the largest product for digits p < q < r, and check it with the digits 4, 6 and 8.",
              ["Keep the larger of each pair: rq × p, rp × q and qp × r.",
               "Expand: rp × q is 10 × r × q plus p × q, and rq × p is 10 × r × p plus q × p. The ones parts match "
               "and q > p, so rp × q is bigger.",
               "Expand: qp × r is 10 × q × r plus p × r, and rp × q is 10 × r × q plus p × q.",
               "The tens parts match and p × r is bigger than p × q, so qp × r is the largest.",
               "Check with 4, 6, 8: 64 × 8 = 512 and 84 × 6 = 504, so 64 × 8 wins."],
              "qp × r is always the largest; for 4, 6 and 8 it is 64 × 8 = 512",
              ncert=["6.5.general"])],
       key_terms=["product", "multiplier", "multiplicand"], misconceptions=["M_BIG_TENS"], minutes=10),
     DOER("T5.C3", "Practice: build the largest product", "digit_arranger", "Apply",
          "Students place three given digits to make the largest two digit by one digit product, using the largest "
          "digit as multiplier, and check against the next best placement.",
          ["Largest digit as the multiplier.",
           "The other two digits in decreasing order form the two digit number."],
          items=[
              FIO("FiOB.q1", "Figure it Out (the largest product, question 1)",
                  "Fill the digits 1, 3, and 7 in a two digit number times a one digit number to make the largest "
                  "product possible.",
                  ["Use the largest digit, 7, as the multiplier.",
                   "Arrange 3 and 1 in decreasing order: 31.",
                   "31 × 7 = 217.",
                   "Check the next best: 71 × 3 = 213, which is smaller."],
                  "31 × 7 = 217"),
              FIO("FiOB.q2", "Figure it Out (the largest product, question 2)",
                  "Fill the digits 3, 5, and 9 in a two digit number times a one digit number to make the largest "
                  "product possible.",
                  ["Use the largest digit, 9, as the multiplier.",
                   "Arrange 5 and 3 in decreasing order: 53.",
                   "53 × 9 = 477.",
                   "Check the next best: 93 × 5 = 465, which is smaller."],
                  "53 × 9 = 477")],
          misconceptions=["M_BIG_TENS"])],
    key_terms=["product", "multiplier", "multiplicand"]))

# ============================== T6 Decoding divisibility tricks ===========================================
TOPICS.append(TOPIC(
    "T6", "M3", "Decoding Divisibility Tricks", ["6.6"], "Analyze",
    "Students explain with place value why reversing a two digit number and subtracting always gives a multiple of "
    "9, handle the case where the first digit is larger, and use the same algebra to decode sum, cycle and repeat "
    "tricks.",
    "Writing ab as 10a + b turns a trick into algebra: reverse and subtract gives 9 times the digit difference, "
    "reverse and add gives 11 times the digit sum.",
    [A("T6.C1", "Reverse and subtract: why 9 divides", "Analyze",
       "Students follow the reverse and subtract trick with two digit numbers, write the numbers as 10a + b and "
       "10b + a, and show that the difference is 9 times the digit difference.",
       textbook=["6.6 Decoding Divisibility Tricks",
                 "It is now Mukta's turn to show a mathematics trick to Shubham.",
                 "Mukta: Choose a 2 digit number of different digits and don't reveal it! Reverse the digits to get "
                 "another number. Find their difference. Divide the result by 9. There won't be any remainder.",
                 "Shubham thinks of 47, reverses it to 74, finds 74 − 47 = 27, and 27 ÷ 9 = 3. Shubham: Yes, you are "
                 "right. But how did you know?",
                 "If we choose other 2 digit numbers, and follow the steps, will there always be no remainder?",
                 "Let's try to understand how Mukta's trick works. Suppose the two digit number is ab. When it is "
                 "reversed, the new number is ba.",
                 "If b > a, then ba > ab. So, the difference is (10b + a) − (10a + b) = 10b − b − 10a + a = 9b − 9a = "
                 "9 (b − a).",
                 "The difference is divisible by 9."],
       teach=["Predict first: will 9 divide the difference for every two digit number you pick?",
              "Try 47: 74 − 47 = 27, and 27 ÷ 9 = 3. Try 25: 52 − 25 = 27 again. Try 18: 81 − 18 = 63.",
              "With digits a and b the number is 10a + b and its reverse is 10b + a.",
              "Their difference is 9b − 9a, which is 9 times (b − a), so 9 always divides it."],
       examples=[
           WE("Shubham picks 47. Follow Mukta's trick, then show with letters why 9 always divides the difference.",
              ["Reverse 47 to get 74. The difference is 74 − 47 = 27, and 27 ÷ 9 = 3 with no remainder.",
               "Write the number as 10a + b and the reverse as 10b + a, with b larger than a.",
               "The difference is 10b + a − 10a − b, which is 9b − 9a, or 9 times (b − a).",
               "For 47 the digit difference is 7 − 4 = 3, which is the quotient."],
              "The difference is always 9 times the difference of the digits",
              ncert=["6.6.mukta_trick", "6.6.always"])],
       key_terms=["place value", "reverse", "divisible"], misconceptions=["M_DIFF_ORDER"], minutes=10),
     A("T6.C1x", "When the first digit is bigger", "Analyze",
       "Students redo the reverse and subtract algebra when the first digit is larger and show the difference is "
       "9 times (a − b), so the trick still works.",
       textbook=["Can you work out what happens if a > b?"],
       teach=["Predict first: if the reversed number is smaller, does the trick break?",
              "Subtract the smaller number from the larger one, as before.",
              "Now the difference is (10a + b) − (10b + a), which is 9 times (a − b)."],
       examples=[
           WE("Take 83, whose first digit is bigger. Follow the trick and show what happens with letters when a > b.",
              ["Reverse 83 to get 38. The difference is 83 − 38 = 45, and 45 ÷ 9 = 5.",
               "With a > b, subtract the reverse from the number: 10a + b − 10b − a.",
               "That is 9a − 9b, which is 9 times (a − b).",
               "For 83, the digit difference is 8 − 3 = 5, which is the quotient again."],
              "The difference is 9 times (a − b), so 9 still divides it",
              ncert=["6.6.a_gt_b"])],
       key_terms=["reverse", "divisible"], misconceptions=["M_DIFF_ORDER"], minutes=6, thin=True),
     A("T6.C2", "Place value builds new divisibility tricks", "Create",
       "Students write a three digit number as 100a + 10b + c, reverse it and subtract, and explain why the result "
       "is always divisible by 99.",
       teach=["Predict first: if you reverse a three digit number and subtract, which number always divides the "
              "result?",
              "Any number can be written in place value form, which turns a trick into an expression.",
              "Simplify the expression and look for a common factor: that factor is the divisibility rule.",
              "Use the same idea for adding reversed numbers or repeating digits."],
       examples=[
           WE("Take 352, reverse it to 253 and subtract. Show with letters why 99 always divides the difference of a "
              "three digit number and its reverse.",
              ["352 − 253 = 99, and 99 ÷ 99 = 1.",
               "Write abc as 100a + 10b + c and its reverse as 100c + 10b + a, with a larger than c.",
               "The difference is 100a + c − 100c − a, the tens cancel, which is 99a − 99c.",
               "That is 99 times (a − c), so 99 always divides it. For 352, the difference of the outer digits is "
               "3 − 2 = 1."],
              "The difference is 99 times the difference of the first and last digits",
              ncert=[])],
       key_terms=["place value", "divisible", "factor"], minutes=8),
     DOER("T6.C3", "Practice: decode the divisibility tricks", "digit_lab", "Analyze",
          "Students find the quotient in the reverse and subtract trick, and use place value to explain sum, cycling "
          "and repeating tricks that give multiples of 11, 37 and 1001.",
          ["A two digit number ab is 10a + b; a three digit number abc is 100a + 10b + c.",
           "Simplify, then look for the common factor."],
          items=[
              FIO("FiOC.q1", "Figure it Out (divisibility tricks, question 1)",
                  "In the trick given above, what is the quotient when you divide by 9? Is there a relationship "
                  "between the two numbers and the quotient?",
                  ["The difference is 9 times the difference of the digits.",
                   "So dividing by 9 leaves the difference of the two digits.",
                   "For 47 and 74: 27 ÷ 9 = 3, and 7 − 4 = 3."],
                  "The quotient is the difference between the two digits of the number"),
              FIO("FiOC.q2", "Figure it Out (divisibility tricks, question 2)",
                  "In the trick given above, instead of finding the difference of the two 2 digit numbers, find their "
                  "sum. What will happen? For example: 31 + 13 = 44, 28 + 82 = 110, 12 + 21 = 33. Observe that all "
                  "these numbers are divisible by 11. Is this always true? Can we justify this claim using algebra?",
                  ["The number is 10a + b and the reverse is 10b + a.",
                   "The sum is 11a + 11b, which is 11 times (a + b).",
                   "So the sum is always divisible by 11, and the quotient is the digit sum: 44 ÷ 11 = 4 and 3 + 1 = 4."],
                  "Yes, always: the sum is 11 times the sum of the digits"),
              FIO("FiOC.q3", "Figure it Out (divisibility tricks, question 3)",
                  "Consider any 3 digit number, say abc (100a + 10b + c). Make two other 3 digit numbers from these "
                  "digits by cycling these digits around, yielding bca and cab. Now add the three numbers. Using "
                  "algebra, justify that the sum is always divisible by 37. Will it also always be divisible by 3? "
                  "(Hint: Look at some multiples of 37.)",
                  ["abc is 100a + 10b + c, bca is 100b + 10c + a and cab is 100c + 10a + b.",
                   "Each digit appears once as hundreds, once as tens and once as ones, so the sum is 111a + 111b + 111c.",
                   "That is 111 times (a + b + c), and 111 = 3 × 37.",
                   "Check with 123: 123 + 231 + 312 = 666, and 666 ÷ 37 = 18, 666 ÷ 3 = 222."],
                  "The sum is 111 times (a + b + c); since 111 = 3 × 37 it is always divisible by 37 and by 3"),
              FIO("FiOC.q4", "Figure it Out (divisibility tricks, question 4)",
                  "Consider any 3 digit number, say abc. Make it a 6 digit number by repeating the digits, that is "
                  "abcabc. Divide this number by 7, then by 11, and finally by 13. What do you get? Try this with "
                  "other numbers. Figure out why it works. (Hint: Multiply 7, 11 and 13.)",
                  ["Try 254: 254254 ÷ 7 = 36322, then 36322 ÷ 11 = 3302, then 3302 ÷ 13 = 254.",
                   "Repeating the digits means abc × 1000 + abc, which is abc × 1001.",
                   "And 7 × 11 × 13 = 1001, so dividing by 7, 11 and 13 divides by 1001."],
                  "You get back the original 3 digit number, because abcabc is abc × 1001 and 1001 = 7 × 11 × 13")],
          misconceptions=["M_DIFF_ORDER"])],
    key_terms=["place value", "divisible", "reverse"]))

# ============================== T7 Puzzles with letter-numbers ============================================
TOPICS.append(TOPIC(
    "T7", "M3", "Puzzles Solved with Letter-Numbers", ["6.6"], "Apply",
    "Students turn word puzzles into equations with a letter-number, undo chains of doubling and giving away, and "
    "model profit as income minus costs, then solve and check each puzzle in its story.",
    "Name the unknown with a letter, follow the story step by step to build an equation, solve it, and put the "
    "answer back into the story to check it.",
    [A("T7.C1", "Turn a story into an equation", "Apply",
       "Students name the unknown in a counting puzzle with a letter-number, write an equation from the story, solve "
       "it, and also solve it by reasoning without letters.",
       teach=["Predict first: if all the cycles were bicycles, how many wheels would there be?",
              "Name one unknown with a letter and write the other in terms of it.",
              "Build the equation from the total, solve it, and put the answer back into the story.",
              "Without letters: start from a guess where all are of one kind and fix the difference."],
       examples=[
           WE("A stand has 20 cycles, some bicycles and some tricycles, with 46 wheels in all. How many of each?",
              ["Let t be the number of tricycles, so there are 20 − t bicycles.",
               "Wheels: 3t + 2(20 − t) = 46, so t + 40 = 46 and t is 6.",
               "There are 6 tricycles and 14 bicycles. Check: 3 × 6 + 2 × 14 = 18 + 28 = 46.",
               "Without letters: 20 bicycles would have 40 wheels; each tricycle adds 1 more, and 46 − 40 = 6."],
              "6 tricycles and 14 bicycles",
              ncert=[])],
       key_terms=["equation", "letter-number", "story"], misconceptions=["M_STORY_ORDER"], minutes=10),
     A("T7.C2", "Undo a chain of doubling and giving away", "Apply",
       "Students follow a starting amount through rounds of doubling and giving away with a letter-number, set the "
       "final expression equal to what is left, and solve for the start.",
       teach=["Predict first: if the amount doubles each round but some is given away, does it always grow?",
              "Follow x through each round: double it, then subtract what is given.",
              "Set the final expression equal to what is left and solve.",
              "Check by running the rounds forward from the answer."],
       examples=[
           WE("Asha has some stickers. She doubles them and gives away 5, then doubles again and gives away 5. She has "
              "13 left. How many did she start with?",
              ["Let x be the start. After round one she has 2x − 5.",
               "After round two she has 2(2x − 5) − 5, which is 4x − 15.",
               "So 4x − 15 = 13, which gives 4x = 28 and x is 7.",
               "Check: 7 × 2 = 14, then 14 − 5 = 9, then 9 × 2 = 18, then 18 − 5 = 13."],
              "She started with 7 stickers",
              ncert=[])],
       key_terms=["doubling", "expression"], misconceptions=["M_STORY_ORDER"], minutes=10,
       tool="rounds_machine"),
     A("T7.C3", "Profit is income minus costs", "Apply",
       "Students write the profit of a small stall as income minus fixed and per item costs, and solve for the price "
       "or the number of items that gives a target profit.",
       teach=["Predict first: is profit the price minus the cost of one item?",
              "Income is price times items sold. Costs are the fixed rent plus the cost of each item made.",
              "Profit is income minus all the costs. Set it equal to the target and solve."],
       examples=[
           WE("A lemonade stall pays rent of ₹200 a day, and each glass costs ₹5 to make. If 60 glasses are sold, what "
              "price per glass gives a profit of ₹400?",
              ["Let the price be p rupees. Income is 60p.",
               "Costs: rent 200 and making 60 × 5 = 300.",
               "Profit: 60p − 300 − 200 = 400, so 60p = 900 and p is 15.",
               "Check: 60 × 15 = 900, and 900 − 300 − 200 = 400."],
              "₹15 per glass",
              ncert=[])],
       key_terms=["profit", "income", "costs"], misconceptions=["M_PROFIT_PRICE"], minutes=8),
     DOER("T7.C4", "Practice: solve the puzzles", "swap_counter", "Apply",
          "Students model each puzzle with a letter-number, solve it, check the answer in the story, and explain "
          "patterns such as the fractions built from odd numbers.",
          ["Name the unknown, follow the story to an equation, solve, and check.",
           "For doubling rounds, follow x through every round before setting up the equation."],
          items=[
              FIO("FiOC.q5", "Figure it Out (divisibility tricks, question 5)",
                  "There are 3 shrines, each with a magical pond in the front. If anyone dips flowers into these "
                  "magical ponds, the number of flowers doubles. A person has some flowers. He dips them all in the "
                  "first pond and then places some flowers in shrine 1. Next, he dips the remaining flowers in the "
                  "second pond and places some flowers in shrine 2. Finally, he dips the remaining flowers in the third "
                  "pond and then places them all in shrine 3. If he placed an equal number of flowers in each shrine, "
                  "how many flowers did he start with? How many flowers did he place in each shrine?",
                  ["Let x be the start and k the flowers placed in each shrine.",
                   "After the first pond and shrine: 2x − k. After the second: 2(2x − k) − k, which is 4x − 3k.",
                   "The third pond doubles it to 8x − 6k, and all of it goes into shrine 3, so 8x − 6k = k and 8x = 7k.",
                   "The smallest whole numbers are x = 7 and k = 8. Check: 14 − 8 = 6, then 12 − 8 = 4, then 8.",
                   "Any multiple also works, such as 14 flowers with 16 in each shrine."],
                  "He started with 7 flowers and placed 8 in each shrine (or any multiple, like 14 and 16)"),
              FIO("FiOC.q6", "Figure it Out (divisibility tricks, question 6)",
                  "A farm has some horses and hens. The total number of heads of these animals is 55 and the total "
                  "number of legs is 150. How many horses and how many hens are on the farm? Can you solve this "
                  "without letter-numbers? (Hint: If all the 55 animals were hens, then how many legs would there be? "
                  "Using the difference between this number and 150, can you find the number of horses?)",
                  ["Let h be the horses, so there are 55 − h hens.",
                   "Legs: 4h + 2(55 − h) = 150, so 2h + 110 = 150 and h is 20.",
                   "Without letters: 55 hens would have 110 legs. 150 − 110 = 40 legs are extra, and each horse adds 2, "
                   "so 40 ÷ 2 = 20 horses.",
                   "Hens: 55 − 20 = 35. Check: 4 × 20 + 2 × 35 = 80 + 70 = 150."],
                  "20 horses and 35 hens"),
              FIO("FiOC.q7", "Figure it Out (divisibility tricks, question 7)",
                  "A mother is 5 times her daughter's age. In 6 years' time, the mother will be 3 times her daughter's "
                  "age. How old is the daughter now?",
                  ["Let the daughter be d years old, so the mother is 5d.",
                   "In 6 years: 5d + 6 = 3(d + 6), which is 3d + 18.",
                   "So 2d = 12 and d is 6.",
                   "Check: the mother is 30 now; in 6 years 36 = 3 × 12."],
                  "The daughter is 6 years old"),
              FIO("FiOC.q8", "Figure it Out (divisibility tricks, question 8)",
                  "Two friends, Gauri and Naina, are cowherds. One day, they pass each other on the road with their "
                  "cows. Gauri says to Naina, \"You have twice as many cows as I do\". Naina says, \"That's true, but "
                  "if I gave you three of my cows, we would each have the same number of cows\". How many cows do "
                  "Gauri and Naina have?",
                  ["Let Gauri have g cows, so Naina has 2g.",
                   "If Naina gives 3: 2g − 3 = g + 3, so g is 6.",
                   "Naina has 12. Check: 12 − 3 = 9 and 6 + 3 = 9."],
                  "Gauri has 6 cows and Naina has 12"),
              FIO("FiOC.q9", "Figure it Out (divisibility tricks, question 9)",
                  "I run a small dosa cart and my expenses are as follows: rent for the dosa cart is ₹5000 per day; "
                  "the cost of making one dosa (including all the ingredients and fuel) is ₹10. (i) If I can sell 100 "
                  "dosas a day, what should be the selling price of my dosa to make a profit of ₹2000? (ii) If my "
                  "customers are willing to pay only ₹50 for a dosa, how many dosas should I aim to sell in a day to "
                  "make a profit of ₹2000?",
                  ["(i) Let the price be p. Income 100p; costs 5000 + 100 × 10 = 6000.",
                   "100p − 6000 = 2000, so 100p = 8000 and p is 80.",
                   "(ii) Let n dosas be sold. Each earns 50 − 10 = 40 after its own cost.",
                   "40n − 5000 = 2000, so 40n = 7000 and n is 175. Check: 175 × 40 = 7000."],
                  "(i) ₹80 per dosa (ii) 175 dosas a day"),
              FIO("FiOC.q10", "Figure it Out (divisibility tricks, question 10)",
                  "Evaluate the following sequence of fractions: 1 ÷ 3, (1 + 3) ÷ (5 + 7), (1 + 3 + 5) ÷ (7 + 9 + 11). "
                  "What do you observe? Can you explain why this happens? (Hint: Recall what you know about the sum of "
                  "the first n odd numbers.)",
                  ["(1 + 3) ÷ (5 + 7) = 4 ÷ 12, which is one third.",
                   "(1 + 3 + 5) ÷ (7 + 9 + 11) = 9 ÷ 27, which is one third again.",
                   "The first n odd numbers add up to n × n, and the first 2n odd numbers add up to 4 × n × n.",
                   "So the next n odd numbers add up to 4 × n × n minus n × n, which is 3 × n × n, three times the "
                   "top."],
                  "Every fraction equals one third, because the bottom sum is always three times the top sum"),
              FIO("FiOC.q11", "Figure it Out (divisibility tricks, question 11)",
                  "Karim and the Genie. Each time Karim goes around the banyan tree, the coins in his pocket double, "
                  "and then he gives the genie 8 coins. After the third round the coins doubled, and he was left with "
                  "only 8 coins, exactly the number he owed the genie. (i) How many coins did Karim initially have? "
                  "(ii) For what cost per round should Karim agree to the deal, if he wants to increase the number of "
                  "coins he has? (iii) Through its magical powers, the genie knows the number of coins that Karim has. "
                  "How should the genie set the cost per round so that it gets all of Karim's coins?",
                  ["(i) Let x be the start. After one round 2x − 8, after two rounds 4x − 24.",
                   "The third doubling gives 8x − 48, which is 8, so 8x = 56 and x is 7.",
                   "Check: 7, then 14 − 8 = 6, then 12 − 8 = 4, then 8, all given to the genie.",
                   "(ii) With cost c, one round turns x into 2x − c, which is more than x only when c is less than x. "
                   "So Karim should agree only if the cost is less than the coins he starts with, here fewer than 7.",
                   "(iii) After three rounds he has 8x − 7c. For this to be 0, the genie sets c to 8x ÷ 7. For 7 coins "
                   "that is 8 per round, exactly the genie's trick."],
                  "(i) 7 coins (ii) a cost per round less than his coins, fewer than 7 (iii) 8 ÷ 7 of his starting "
                  "coins per round, which is 8 when he starts with 7")],
          misconceptions=["M_STORY_ORDER", "M_PROFIT_PRICE"])],
    key_terms=["equation", "letter-number", "puzzle"]))

# ============================== T8 Summary ================================================================
TOPICS.append(TOPIC(
    "T8", "M3", "Summary: Algebra Play", ["Summary"], "Remember",
    None,
    "Algebra models number games, justifies why tricks always work, and solves pyramids, grids, product, "
    "divisibility and story puzzles.",
    [A("T8.C1", "What algebra did in this chapter", "Remember",
       "Students restate how letter-numbers explained the tricks, pyramids, grids, largest products, divisibility "
       "tricks and puzzles of the chapter, and how to invent new ones.",
       textbook=["Algebra is very useful in modeling and understanding numerical scenarios. Because of this, it occurs "
                 "in almost all areas of mathematics, science and beyond.",
                 "Algebra is an indispensable tool in justifying mathematical statements.",
                 "We applied algebra to analyse 'Think of a Number' tricks, number pyramids, grids, ways of forming "
                 "numbers using given digits to maximise certain products, divisibility tricks, and various other "
                 "problems."],
       teach=["Our opening question is settled: the add 3, double, take away 6, halve trick always gives your number "
              "back, because with x it becomes x + 3, then 2x + 6, then 2x, then x.",
              "A letter-number turns a pattern seen in a few cases into a statement true for every case.",
              "Still open for you: invent a trick, a pyramid or a puzzle and use a letter to show why it works."],
       ncert=["summary"], video_focus=["RECAP"], minutes=8)],
    topic_type="summary"))
