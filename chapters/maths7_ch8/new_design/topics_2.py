# -*- coding: utf-8 -*-
"""Topics T5 to T8. T5 and T6 finish module M1 (cancelling, size of a product); T7 and T8 are module M2 (division)."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T5 Cancelling common factors ===================================================
TOPICS.append(TOPIC(
    "T5", "M1", "Cancelling Common Factors", ["8.1"], "Apply",
    "Students divide a numerator and a denominator by a common factor before multiplying, so the product comes out "
    "in its lowest form.",
    "Before multiplying fractions, divide any numerator and any denominator by a factor they share; the product is "
    "then already in lowest form.",
    [A("T5.C1", "Cancel first, then multiply", "Apply",
       "Students multiply 12/7 by 5/24 and 14/15 by 25/42 by cancelling common factors of a numerator and a "
       "denominator before multiplying.",
       textbook=["Multiplication of Fractions, Simplifying to Lowest Form",
                 "Multiply the following fractions and express the product in its lowest form: 12/7 × 5/24.",
                 "Instead of multiplying the numerators (12 and 5) and denominators (7 and 24) first and then "
                 "simplifying, we could do the following: 12/7 × 5/24 = (12 × 5)/(7 × 24).",
                 "We see that both the circled numbers have a common factor of 12. We know that a fraction remains "
                 "the same when the numerator and denominator are divided by the common factor. In this case, we "
                 "can divide them by 12: (12 × 5)/(7 × 24) = (1 × 5)/(7 × 2) = 5/14.",
                 "Let us use the same technique to do one more multiplication. 14/15 × 25/42 = (14 × 25)/(15 × 42) "
                 "= (1 × 5)/(3 × 3) = 5/9.",
                 "When multiplying fractions, we can first divide the numerator and denominator by their common "
                 "factors before multiplying the numerators and denominators. This is called cancelling the common "
                 "factors."],
       teach=["Predict first: will the product of 12/7 and 5/24 be in lowest form after multiplying straight across?",
              "The numerator 12 and the denominator 24 share the factor 12, so divide both by 12.",
              "A fraction stays the same when its top and bottom are divided by a common factor.",
              "Cancelling first keeps the numbers small and leaves the product in lowest form."],
       examples=[
           WE("Multiply 12/7 × 5/24 and give the product in its lowest form.",
              ["Write 12/7 × 5/24 = (12 × 5)/(7 × 24).",
               "12 and 24 have the common factor 12; divide both by 12: 12 becomes 1 and 24 becomes 2.",
               "(1 × 5)/(7 × 2) = 5/14."],
              "5/14", ncert=["8.1.cancel1"]),
           WE("Multiply 14/15 × 25/42 and give the product in its lowest form.",
              ["Write 14/15 × 25/42 = (14 × 25)/(15 × 42).",
               "14 and 42 share the factor 14: 14 becomes 1 and 42 becomes 3.",
               "25 and 15 share the factor 5: 25 becomes 5 and 15 becomes 3.",
               "(1 × 5)/(3 × 3) = 5/9."],
              "5/9", ncert=["8.1.cancel2"])],
       key_terms=["cancelling", "common factor", "lowest form"], misconceptions=["M_CANCEL_SAME_FRACTION"],
       minutes=10),
     A("T5.C2", "Apavartana in a very old book", "Remember", "",
       textbook=["A Pinch of History",
                 "In India, the process of reducing a fraction to its lowest terms, known as apavartana, is so well "
                 "known that it finds mention even in a non-mathematical work. A Jaina scholar Umasvati used it as "
                 "a simile in a philosophical work."],
       teach=["Reducing a fraction to its lowest terms was called apavartana in India.",
              "It was so well known that a Jaina scholar, Umasvati, used it as a comparison in a book of philosophy.",
              "Cancelling common factors is the same idea at work inside a multiplication."],
       ncert=["8.1.history_apavartana"], key_terms=["apavartana"], enrichment=True, minutes=3),
     DOER("T5.C3", "Practice: cancel and multiply", "cancel_then_multiply", "Apply",
          "Students multiply fractions and mixed fractions in tank, land, area, saplings and weight problems, "
          "cancelling common factors where they help.",
          ["Find a numerator and a denominator that share a factor and divide both by it.",
           "Then multiply the numerators and multiply the denominators.",
           "Change a mixed fraction to a fraction before multiplying."],
          items=[
              FIO("8.1.FiOC1", "Figure it Out (cancelling), Q1",
                  "A water tank is filled from a tap. If the tap is open for 1 hour, 7/10 of the tank gets filled. "
                  "How much of the tank is filled if the tap is open for (a) 1/3 hour (b) 2/3 hour (c) 3/4 hour "
                  "(d) 7/10 hour (e) For the tank to be full, how long should the tap be running?",
                  ["In 1 hour 7/10 of the tank fills, so in a fraction of an hour multiply 7/10 by that fraction.",
                   "(a) 1/3 × 7/10 = 7/30.",
                   "(b) 2/3 × 7/10 = 14/30 = 7/15.",
                   "(c) 3/4 × 7/10 = 21/40.",
                   "(d) 7/10 × 7/10 = 49/100.",
                   "(e) The full tank is 1 whole: 1 ÷ (7/10) = 10/7 hours, which is 1 3/7 hours."],
                  "(a) 7/30 (b) 7/15 (c) 21/40 (d) 49/100 (e) 10/7 hours, that is 1 3/7 hours",
                  tool="cancel_then_multiply"),
              FIO("8.1.FiOC2", "Figure it Out (cancelling), Q2",
                  "The government has taken 1/6 of Somu's land to build a road. What part of the land remains with "
                  "Somu now? She gives half of the remaining part of the land to her daughter Krishna and 1/3 of it "
                  "to her son Bora. After giving them their shares, she keeps the remaining land for herself. "
                  "(a) What part of the original land did Krishna get? (b) What part of the original land did Bora "
                  "get? (c) What part of the original land did Somu keep for herself?",
                  ["Land remaining after the road: 1 − 1/6 = 5/6.",
                   "(a) Krishna gets 1/2 × 5/6 = 5/12.",
                   "(b) Bora gets 1/3 × 5/6 = 5/18.",
                   "(c) Somu keeps what is left of the 5/6 after both gifts: 5/6 − 5/12 − 5/18 = 30/36 − 15/36 − "
                   "10/36 = 5/36."],
                  "5/6 remains; (a) 5/12 (b) 5/18 (c) 5/36"),
              FIO("8.1.FiOC3", "Figure it Out (cancelling), Q3",
                  "Find the area of a rectangle of sides 3 3/4 ft and 9 3/5 ft.",
                  ["Change both to fractions: 3 3/4 = 15/4 and 9 3/5 = 48/5.",
                   "Area = 15/4 × 48/5.",
                   "Cancel 15 with 5 (3 and 1) and 48 with 4 (12 and 1): 3 × 12 = 36."],
                  "36 square feet"),
              FIO("8.1.FiOC4", "Figure it Out (cancelling), Q4",
                  "Tsewang plants four saplings in a row in his garden. The distance between two saplings is 3/4 m. "
                  "Find the distance between the first and last sapling.",
                  ["Draw four saplings in a row: there are 3 gaps between the first and the last.",
                   "Distance = 3 × 3/4 = 9/4 m, which is 2 1/4 m."],
                  "9/4 m, that is 2 1/4 m"),
              FIO("8.1.FiOC5", "Figure it Out (cancelling), Q5",
                  "Which is heavier: 12/15 of 500 grams or 3/20 of 4 kg?",
                  ["12/15 of 500 g = 12/15 × 500 = 400 g.",
                   "3/20 of 4 kg = 3/20 × 4000 g = 600 g, after changing kilograms to grams.",
                   "600 g is more than 400 g."],
                  "3/20 of 4 kg is heavier: it is 600 g against 400 g"),
          ])]))

# ============================== T6 Is the product always greater ===============================================
TOPICS.append(TOPIC(
    "T6", "M1", "Is the Product Always Greater?", ["8.1"], "Analyze",
    "Students predict whether a product of two numbers is greater than or smaller than the numbers multiplied, "
    "from whether each number is below or above 1, and see that the order of multiplication does not matter.",
    "Multiplying by a number between 0 and 1 gives a smaller result, multiplying by a number above 1 gives a "
    "greater result, and the order of the factors never matters.",
    [A("T6.C1", "Three situations", "Analyze",
       "Students compare the product with both numbers when both are above 1, when both are between 0 and 1, and "
       "when one is above 1 and one between 0 and 1.",
       textbook=["Is the Product Always Greater than the Numbers Multiplied?",
                 "Since, we know that when a number is multiplied by 1, the product remains unchanged, we will look "
                 "at multiplying pairs of numbers where neither of them is 1.",
                 "When we multiply two counting numbers greater than 1, say 3 and 5, the product is greater than "
                 "both the numbers being multiplied. 3 × 5 = 15.",
                 "But what happens when we multiply 1/4 and 8? 1/4 × 8 = 2. The product, 2, is greater than 1/4, "
                 "but less than 8.",
                 "What happens when we multiply 3/4 and 2/5? 3/4 × 2/5 = 6/20. Let us compare this product 6/20 with "
                 "the numbers 3/4 and 2/5. For this, let us express 3/4 as 15/20 and 2/5 as 8/20. From this we can "
                 "see that the product is less than both the numbers.",
                 "Situation 1: both numbers are greater than 1 (e.g., 4/3 × 4). The product (16/3) is greater than "
                 "both the numbers.",
                 "Situation 2: both numbers are between 0 and 1 (e.g., 3/4 × 2/5). The product (3/10) is less than "
                 "both the numbers.",
                 "Situation 3: one number is between 0 and 1, and one number is greater than 1 (e.g., 3/4 × 5). "
                 "The product (15/4) is less than the number greater than 1 and greater than the number between 0 "
                 "and 1."],
       teach=["Predict first: when does multiplying make a number bigger, and when smaller?",
              "Both numbers above 1: the product is greater than both.",
              "Both numbers between 0 and 1: the product is less than both, because you take a part of a part.",
              "One above 1 and one between 0 and 1: the product lies between the two numbers."],
       examples=[
           WE("Multiply 4/3 × 4 and compare the product with both numbers.",
              ["Both 4/3 and 4 are greater than 1.",
               "4/3 × 4 = 16/3, which is 5 1/3.",
               "5 1/3 is greater than 4/3 and greater than 4."],
              "16/3, greater than both numbers", ncert=["8.1.size_sit1"]),
           WE("Multiply 3/4 × 2/5 and compare the product with both numbers.",
              ["Both numbers are between 0 and 1.",
               "3/4 × 2/5 = 6/20 = 3/10.",
               "As twentieths, 3/4 is 15/20 and 2/5 is 8/20, while the product is 6/20.",
               "6/20 is less than both 15/20 and 8/20."],
              "3/10, less than both numbers", ncert=["8.1.size_sit2"]),
           WE("Multiply 3/4 × 5 and compare the product with both numbers.",
              ["3/4 is between 0 and 1 and 5 is greater than 1.",
               "3/4 × 5 = 15/4, which is 3 3/4.",
               "3 3/4 is less than 5 and greater than 3/4."],
              "15/4, less than 5 and greater than 3/4", ncert=["8.1.size_sit3"])],
       key_terms=["product"], misconceptions=["M_MULT_BIGGER"], minutes=10),
     A("T6.C2", "The conclusion about multiplying", "Analyze",
       "Students complete the rule: multiplying by a number between 0 and 1 gives a product less than the other "
       "number, and multiplying by a number above 1 gives a product greater than the other number.",
       textbook=["Create more such examples for each situation and observe the relationship between the product "
                 "and the numbers being multiplied. What can you conclude about the relationship between the "
                 "numbers multiplied and the product? Fill in the blanks:",
                 "When one of the numbers being multiplied is between 0 and 1, the product is ____ "
                 "(greater/less) than the other number.",
                 "When one of the numbers being multiplied is greater than 1, the product is ____ (greater/less) "
                 "than the other number."],
       teach=["Predict first: if you multiply 8 by a number between 0 and 1, does 8 grow or shrink?",
              "Between 0 and 1: the product is less than the other number.",
              "Greater than 1: the product is greater than the other number.",
              "Test it with new pairs, for example 2/3 × 9 and 5/2 × 1/3."],
       examples=[
           WE("Use 2/3 × 9 and 5/2 × 9 to fill in the blanks: when one number is between 0 and 1, the product is "
              "(greater/less) than the other number; when one number is greater than 1, the product is "
              "(greater/less) than the other number.",
              ["2/3 × 9 = 6, and 2/3 is between 0 and 1: the product 6 is less than the other number 9.",
               "5/2 × 9 = 45/2 = 22 1/2, and 5/2 is greater than 1: the product is greater than 9.",
               "So: between 0 and 1, the product is less than the other number; greater than 1, the product is "
               "greater than the other number."],
              "less when a number is between 0 and 1; greater when a number is greater than 1",
              ncert=["8.1.size_conclude"])],
       key_terms=["product"], misconceptions=["M_MULT_BIGGER"], minutes=8),
     A("T6.C3", "Does the order of multiplication matter?", "Understand",
       "Students see that 1/2 × 1/4 and 1/4 × 1/2 are equal, because a rectangle keeps its area when length and "
       "breadth swap, and that a/b × c/d = c/d × a/b.",
       textbook=["Order of Multiplication",
                 "We know that 1/2 × 1/4 = 1/8. Now, what is 1/4 × 1/2? That is 1/8 too.",
                 "In general, note that the area of a rectangle remains the same even if the length and breadth are "
                 "interchanged. The order of multiplication does not matter. Thus, a/b × c/d = c/d × a/b.",
                 "This can also be seen from Brahmagupta's formula for multiplying fractions."],
       teach=["Predict first: is half of a quarter the same as a quarter of a half?",
              "A rectangle 1/2 by 1/4 turns into a rectangle 1/4 by 1/2, with the same area 1/8.",
              "Brahmagupta's formula shows it too: (a × c)/(b × d) is the same as (c × a)/(d × b)."],
       examples=[
           WE("Find 1/2 × 1/4 and 1/4 × 1/2 and compare them.",
              ["1/2 × 1/4 = (1 × 1)/(2 × 4) = 1/8.",
               "1/4 × 1/2 = (1 × 1)/(4 × 2) = 1/8.",
               "A rectangle with sides 1/2 and 1/4 has the same area as one with sides 1/4 and 1/2.",
               "So the order of multiplication does not matter."],
              "both are 1/8", ncert=["8.1.order"])],
       key_terms=["area"], misconceptions=[], minutes=6),
     DOER("T6.C4", "Practice: will the product be greater or smaller?", "product_size_predictor", "Analyze",
          "Students decide from the sizes of two fractions alone whether a product is greater or smaller than each "
          "of them.",
          ["Is each number above 1 or between 0 and 1?",
           "Above 1 grows the other number, between 0 and 1 shrinks it.",
           "Compare the product with 1 as well."],
          items=[
              FIO("8.3.FiOD9", "Figure it Out (problems with fractions), Q9",
                  "Choose the option(s) describing the product of (565/465 × 707/676): (a) greater than 565/465 "
                  "(b) less than 565/465 (c) greater than 707/676 (d) less than 707/676 (e) greater than 1 "
                  "(f) less than 1",
                  ["565/465 is greater than 1 because 565 is more than 465.",
                   "707/676 is greater than 1 because 707 is more than 676.",
                   "Both numbers are above 1, so the product is greater than both of them and greater than 1.",
                   "So (a), (c) and (e) are correct."],
                  "(a), (c) and (e)",
                  tool="product_size_predictor"),
          ])]))

# ============================== T7 Dividing fractions with reciprocals =========================================
TOPICS.append(TOPIC(
    "T7", "M2", "Dividing Fractions with Reciprocals", ["8.2"], "Apply",
    "Students restate a division as a multiplication with a missing number, find the reciprocal of a divisor, and "
    "divide fractions by multiplying the dividend by the reciprocal of the divisor.",
    "To divide by a fraction, multiply by its reciprocal: a/b ÷ c/d = a/b × d/c.",
    [A("T7.C1", "Division as a multiplication with a missing number", "Understand",
       "Students restate 12 ÷ 4 as 4 × ? = 12, and find 1 ÷ (2/3) and 3 ÷ (2/3) by asking what to multiply 2/3 by.",
       textbook=["8.2 Division of Fractions",
                 "What is 12 ÷ 4? You know this already. But can this problem be restated as a multiplication "
                 "problem? What should be multiplied by 4 to get 12? That is, 4 × ? = 12. 12 ÷ 4 = 3 (dividend ÷ "
                 "divisor = quotient).",
                 "We can use this technique of converting division into multiplication problems to divide "
                 "fractions.",
                 "What is 1 ÷ (2/3)? Let us rewrite this as a multiplication problem: 2/3 × ? = 1. What should be "
                 "multiplied by 2/3 to get the product 1? If we somehow cancel out the 2 and the 3, we are left "
                 "with 1. So, 1 ÷ (2/3) = 3/2. Check: 2/3 × 3/2 = 1.",
                 "Let us try another problem: 3 ÷ (2/3). This is the same as 2/3 × ? = 3. Can you find the answer? We "
                 "know what to multiply 2/3 by to get 1. We just need to multiply that by 3 to get 3. So, "
                 "3 ÷ (2/3) = 3/2 × 3 = 9/2."],
       teach=["Predict first: will 12 ÷ 4 and 4 × ? = 12 have the same answer?",
              "The three names: dividend ÷ divisor = quotient. So 12 ÷ 4 = 3 and 4 × 3 = 12.",
              "For 1 ÷ (2/3), ask 2/3 × ? = 1. The answer 3/2 swaps the top and bottom of 2/3.",
              "For 3 ÷ (2/3), take the number that gives 1 and multiply it by 3 more."],
       examples=[
           WE("Find 12 ÷ 4 by asking 4 × ? = 12.",
              ["Restate as a multiplication: 4 × ? = 12.",
               "4 × 3 = 12.",
               "So 12 ÷ 4 = 3."],
              "3", ncert=["8.2.twelve_by_four"]),
           WE("Find 1 ÷ (2/3) by asking 2/3 × ? = 1.",
              ["Rewrite as 2/3 × ? = 1.",
               "Cancelling the 2 and the 3 means multiplying by 3/2.",
               "2/3 × 3/2 = 1, so 1 ÷ (2/3) = 3/2."],
              "3/2, that is 1 1/2", ncert=["8.2.one_by_twothirds"]),
           WE("Find 3 ÷ (2/3) by asking 2/3 × ? = 3.",
              ["We know 2/3 × 3/2 = 1.",
               "To get 3 instead of 1, multiply that by 3: 2/3 × 3/2 × 3 = 3.",
               "So 3 ÷ (2/3) = 3/2 × 3 = 9/2."],
              "9/2, that is 4 1/2", ncert=["8.2.three_by_twothirds"])],
       key_terms=["dividend", "divisor", "quotient"], misconceptions=["M_DIV_SMALLER"], minutes=10),
     A("T7.C2", "A fraction divided by a fraction", "Apply",
       "Students find 1/5 ÷ (1/2) and 2/3 ÷ (3/5) by writing a missing multiplication and using the number that gives "
       "1 first.",
       textbook=["What is 1/5 ÷ (1/2)? Rewriting it as a multiplication problem, we have 1/2 × ? = 1/5. How do we "
                 "solve this? 1/2 × 2 = 1, then 1/2 × 2 × 1/5 = 1/5. So, 1/5 ÷ (1/2) = 2 × 1/5 = 2/5.",
                 "What is 2/3 ÷ (3/5)? Rewriting this as multiplication, we have 3/5 × ? = 2/3. How will we solve "
                 "this? 3/5 × 5/3 × 2/3 = 2/3. So, 2/3 ÷ (3/5) = 5/3 × 2/3 = 10/9."],
       teach=["Predict first: is 1/5 ÷ (1/2) greater than 1/5 or less?",
              "First find what turns the divisor into 1: for 1/2 it is 2.",
              "Then multiply that by the dividend: 2 × 1/5 = 2/5.",
              "The same two steps work for 2/3 ÷ (3/5): the number that gives 1 is 5/3, and 5/3 × 2/3 = 10/9."],
       examples=[
           WE("Find 1/5 ÷ (1/2).",
              ["Rewrite as 1/2 × ? = 1/5.",
               "1/2 × 2 = 1, so first multiply by 2, then by 1/5: 1/2 × 2 × 1/5 = 1/5.",
               "So 1/5 ÷ (1/2) = 2 × 1/5 = 2/5."],
              "2/5", ncert=["8.2.fifth_by_half"]),
           WE("Find 2/3 ÷ (3/5).",
              ["Rewrite as 3/5 × ? = 2/3.",
               "3/5 × 5/3 = 1, so multiply by 5/3 and then by 2/3.",
               "So 2/3 ÷ (3/5) = 5/3 × 2/3 = 10/9."],
              "10/9, that is 1 1/9", ncert=["8.2.twothirds_by_threefifths"])],
       key_terms=["divisor", "dividend"], misconceptions=["M_FLIP_DIVIDEND"], minutes=10),
     A("T7.C3", "The reciprocal and Brahmagupta's rule", "Apply",
       "Students state that the reciprocal of a/b is b/a, that a fraction times its reciprocal is 1, and divide by "
       "multiplying the dividend by the reciprocal of the divisor, as Brahmagupta stated in 628 CE.",
       textbook=["Discussion",
                 "In each of the division problems above, observe how we found the answer. Can we frame a rule that "
                 "tells us how to divide two fractions? Let us consider the previous problem.",
                 "In every division problem we have a dividend, divisor and quotient. The technique we have been "
                 "using to get the quotient is: 1. First, find the number which gives 1 when multiplied by the "
                 "divisor. We see that the resulting number is a fraction whose numerator is the divisor's "
                 "denominator and denominator is the divisor's numerator. For the divisor 3/5 this fraction is 5/3. "
                 "We call 5/3 the reciprocal of 3/5. When we multiply a fraction by its reciprocal, we get 1. So, "
                 "the first step in our technique is to find the divisor's reciprocal.",
                 "2. We then multiply the dividend with this reciprocal to get the quotient.",
                 "Summarising, to divide two fractions: find the reciprocal of the divisor; multiply this by the "
                 "dividend to get the quotient. So, a/b ÷ c/d = d/c × a/b = (d × a)/(c × b). This can be rewritten "
                 "as: a/b ÷ c/d = a/b × d/c = (a × d)/(b × c).",
                 "As with methods and formulas for addition, subtraction, and multiplication of fractions that you "
                 "learnt earlier, this method and formula for division of fractions, in this general form, was "
                 "first explicitly stated by Brahmagupta in his Brāhmasphuṭasiddhānta (628 CE).",
                 "So, to evaluate, for example, 2/3 ÷ (3/5) using Brahmagupta's formula above, we write: "
                 "2/3 ÷ (3/5) = 2/3 × 5/3 = (2 × 5)/(3 × 3) = 10/9."],
       teach=["Predict first: what is the reciprocal of 3/5?",
              "The reciprocal of a/b is b/a; a fraction times its reciprocal is 1.",
              "To divide: take the reciprocal of the divisor and multiply it by the dividend.",
              "a/b ÷ c/d = a/b × d/c = (a × d)/(b × c)."],
       examples=[
           WE("Find 2/3 ÷ (3/5) using the reciprocal.",
              ["The divisor is 3/5, so its reciprocal is 5/3.",
               "Multiply the dividend by the reciprocal: 2/3 × 5/3.",
               "(2 × 5)/(3 × 3) = 10/9."],
              "10/9, that is 1 1/9", ncert=["8.2.rule_reciprocal", "8.2.brahmagupta_div"])],
       key_terms=["reciprocal", "Brahmagupta"], misconceptions=["M_FLIP_DIVIDEND", "M_FLIP_BOTH"], minutes=10),
     DOER("T7.C4", "Practice: divide with the reciprocal", "reciprocal_flipper", "Apply",
          "Students divide fractions, whole numbers and mixed fractions by multiplying by the reciprocal of the "
          "divisor.",
          ["Write the reciprocal of the divisor.",
           "Multiply the dividend by it, cancelling common factors first.",
           "Change mixed fractions to fractions before dividing."],
          items=[
              FIO("8.3.FiOD1", "Figure it Out (problems with fractions), Q1",
                  "Evaluate the following: (a) 3 ÷ (7/9) (b) 14/4 ÷ 2 (c) 2/3 ÷ (2/3) (d) 14/6 ÷ (7/3) (e) 4/3 ÷ (3/4) "
                  "(f) 7/4 ÷ (1/7) (g) 8/2 ÷ (4/15) (h) 1/5 ÷ (1/9) (i) 1/6 ÷ (11/12) (j) 3 2/3 ÷ 1 3/8",
                  ["(a) 3 × 9/7 = 27/7.",
                   "(b) 14/4 × 1/2 = 7/4.",
                   "(c) 2/3 × 3/2 = 1.",
                   "(d) 14/6 × 3/7 = 1.",
                   "(e) 4/3 × 4/3 = 16/9.",
                   "(f) 7/4 × 7 = 49/4.",
                   "(g) 8/2 is 4, and 4 × 15/4 = 15.",
                   "(h) 1/5 × 9 = 9/5.",
                   "(i) 1/6 × 12/11 = 2/11.",
                   "(j) 3 2/3 = 11/3 and 1 3/8 = 11/8, so 11/3 × 8/11 = 8/3, which is 2 2/3."],
                  "(a) 27/7 (b) 7/4 (c) 1 (d) 1 (e) 16/9 (f) 49/4 (g) 15 (h) 9/5 (i) 2/11 (j) 8/3, that is 2 2/3",
                  tool="reciprocal_flipper"),
          ])]))

# ============================== T8 Dividend, divisor and quotient ==============================================
TOPICS.append(TOPIC(
    "T8", "M2", "Dividend, Divisor and Quotient", ["8.2"], "Analyze",
    "Students predict whether a quotient is less than or greater than the dividend from the size of the divisor, "
    "and relate the divisor and the quotient.",
    "Dividing by a number above 1 gives a smaller quotient; dividing by a number between 0 and 1 gives a greater "
    "quotient.",
    [A("T8.C1", "When the quotient is bigger than the dividend", "Analyze",
       "Students compare quotients with dividends in 6 ÷ 3, 6 ÷ (1/4) and 1/8 ÷ (1/4).",
       textbook=["Dividend, Divisor and the Quotient",
                 "When we divide two whole numbers, say 6 ÷ 3, we get the quotient 2. Here the quotient is less than "
                 "the dividend. 6 ÷ 3 = 2, 2 < 6.",
                 "But what happens when we divide 6 by 1/4? 6 ÷ (1/4) = 24. Here the quotient is greater than the "
                 "dividend!",
                 "What happens when we divide 1/8 by 1/4? 1/8 ÷ (1/4) = 1/2. Here too the quotient is greater than "
                 "the dividend."],
       teach=["Predict first: can dividing a number ever make it larger?",
              "6 ÷ 3 = 2, which is less than 6, because the divisor 3 is above 1.",
              "6 ÷ (1/4) = 24 asks how many quarters fit in 6, and quarters are small, so there are many.",
              "1/8 ÷ (1/4) = 1/2, again more than 1/8."],
       examples=[
           WE("Find 6 ÷ 3 and 6 ÷ (1/4) and compare each quotient with the dividend.",
              ["6 ÷ 3 = 2, and 2 is less than 6.",
               "6 ÷ (1/4) = 6 × 4 = 24, and 24 is greater than 6.",
               "The divisor 3 is above 1; the divisor 1/4 is between 0 and 1."],
              "2 is less than 6; 24 is greater than 6", ncert=["8.2.sizes"]),
           WE("Find 1/8 ÷ (1/4) and compare the quotient with the dividend.",
              ["1/8 ÷ (1/4) = 1/8 × 4 = 4/8 = 1/2.",
               "1/2 is greater than 1/8."],
              "1/2, greater than 1/8", ncert=["8.2.sizes"])],
       key_terms=["dividend", "divisor", "quotient"], misconceptions=["M_DIV_SMALLER"], minutes=8),
     A("T8.C2", "Using what we know about multiplication", "Analyze",
       "Students decide when the quotient is less than the dividend by seeing division as multiplication by the "
       "reciprocal of the divisor.",
       textbook=["When do you think the quotient is less than the dividend and when is it greater than the dividend? "
                 "Is there a similar relationship between the divisor and the quotient?",
                 "Use your understanding of such relationships in multiplication to answer the questions above."],
       teach=["Predict first: dividing by 2 is the same as multiplying by what?",
              "Dividing by a divisor means multiplying the dividend by its reciprocal.",
              "Divisor above 1: the reciprocal is between 0 and 1, so the quotient is less than the dividend.",
              "Divisor between 0 and 1: the reciprocal is above 1, so the quotient is greater than the dividend.",
              "For the same dividend, a bigger divisor gives a smaller quotient."],
       examples=[
           WE("Without finding the quotients, say which of 9 ÷ (3/2), 9 ÷ (2/3) and 9 ÷ 1 is largest and which is "
              "smallest, and then check.",
              ["9 ÷ (3/2): the divisor is above 1, so the quotient is less than 9.",
               "9 ÷ (2/3): the divisor is between 0 and 1, so the quotient is greater than 9.",
               "Check: 9 ÷ (3/2) = 9 × 2/3 = 6, and 9 ÷ (2/3) = 9 × 3/2 = 27/2.",
               "The smaller the divisor, the greater the quotient."],
              "9 ÷ (2/3) = 27/2 is largest, 9 ÷ (3/2) = 6 is smallest", ncert=["8.2.sizes_talk"])],
       key_terms=["reciprocal", "quotient"], misconceptions=["M_DIV_SMALLER"], minutes=8),
     DOER("T8.C3", "Practice: greater or smaller quotient?", "quotient_size_predictor", "Analyze",
          "Students predict the size of a quotient from the size of the divisor, then check by dividing.",
          ["Is the divisor above 1 or between 0 and 1?",
           "Predict whether the quotient is greater or less than the dividend.",
           "Check by multiplying with the reciprocal."],
          items=[])]))
