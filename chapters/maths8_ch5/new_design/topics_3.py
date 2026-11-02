# -*- coding: utf-8 -*-
"""Topics T7 to T11 (module M2): why the shortcuts for 10, 5, 2, 4 and 8 work, the shortcuts for 9 and 3, the
shortcut for 11, divisibility by 6 and 24, and digital roots. Book section 5.2, pp 123 to 131, with the second and
third Figure it Out sets and the related questions of the last set."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

FIO2 = "multiples of nine"
FIO3 = "digital roots"
FIO4 = "number play"

# ============================== T7 Place value and the old shortcuts ========================================
TOPICS.append(TOPIC(
    "T7", "M2", "Why the Shortcuts for 10, 5, 2, 4 and 8 Work", ["5.2"], "Understand",
    "Students write a number as a sum of place values and use it to explain why only the last one, two or three "
    "digits decide divisibility by 10, 5, 2, 4 and 8.",
    "A number dcba is 1000d + 100c + 10b + a. Every place value from tens upward is a multiple of 10, 5 and 2, from "
    "hundreds upward a multiple of 4, and from thousands upward a multiple of 8, so only the remaining digits matter.",
    [A("T7.C1", "A number as a sum of place values", "Understand",
       "Students write a number in the general form 1000d + 100c + 10b + a and explain why it is divisible by 10 "
       "exactly when its units digit is 0.",
       textbook=["5.2 Checking Divisibility Quickly",
                 "Earlier, you have learnt shortcuts to check whether a given number, written in the Indian number "
                 "system is divisible by 2, 4, 5, 8, and 10. Let us revisit them.",
                 "Divisibility by 10, 5, and 2: If the units digit of a number is '0', then it is divisible by 10. Let "
                 "us understand why this works through algebra.",
                 "Any number can be written in general as ...dcba, where the letter-numbers a, b, c and d represent "
                 "the units, tens, hundreds and thousands digit, respectively, and so on. As a sum of place values, "
                 "this number is ... + 1000d + 100c + 10b + a. (For example, in the number 4075, d = 4, c = 0, b = 7, "
                 "and a = 5.)",
                 "We know that each place value, with the exception of the units place, is a multiple of 10. So, 10b, "
                 "100c, ... all will be multiples of 10. Hence, the number will be divisible by 10 if and only if the "
                 "units digit a is 0."],
       teach=["Predict first: 4070 and 4075 differ only in the last digit. Which is divisible by 10, and why does "
              "nothing else matter?",
              "Write the number as a sum of place values: 1000d + 100c + 10b + a.",
              "Every term except a is a multiple of 10, so the whole number is a multiple of 10 exactly when a is."],
       examples=[
           WE("Write 4075 and 4070 as sums of place values and decide which is divisible by 10.",
              ["4075 = 4 × 1000 + 0 × 100 + 7 × 10 + 5.",
               "4 × 1000, 0 × 100 and 7 × 10 are multiples of 10; only the units digit 5 is left over.",
               "4070 = 4 × 1000 + 0 × 100 + 7 × 10 + 0, so nothing is left over."],
              "4070 is divisible by 10 and 4075 is not; only the units digit decides",
              ncert=["5.2.place_value_10"])],
       key_terms=["place value", "divisible", "units digit"], misconceptions=["M_LAST_DIGIT_9"], minutes=8),
     A("T7.C2", "Why the shortcuts for 5 and 2 work", "Understand",
       "Students explain with place values why the units digit alone decides divisibility by 5 and by 2.",
       textbook=["Similarly, explain using algebra why the divisibility shortcuts for 5, 2, 4, and 8 work."],
       teach=["Predict first: why do we look only at the units digit to test for 5 and for 2?",
              "10 is 5 × 2, so 10b, 100c, 1000d and every higher place value are multiples of both 5 and 2.",
              "So the number is divisible by 5 exactly when a is 0 or 5, and by 2 exactly when a is even."],
       examples=[
           WE("Use place values to decide whether 3716 and 4075 are divisible by 5 and by 2.",
              ["3716 = 3 × 1000 + 7 × 100 + 1 × 10 + 6, and every term except 6 is a multiple of 10.",
               "6 is even but not 0 or 5, so 3716 is divisible by 2 and not by 5.",
               "4075 = 4 × 1000 + 7 × 10 + 5, and only the units digit 5 is left to test.",
               "5 is a multiple of 5 but odd, so 4075 is divisible by 5 and not by 2."],
              "3716 is divisible by 2 only; 4075 is divisible by 5 only",
              ncert=["5.2.explain_5_2"])],
       key_terms=["place value", "units digit"], minutes=8),
     DOER("T7.C3", "Practice: the rule bench for 4 and 8", "divisibility_rule_bench", "Apply",
          "Students use the rule bench to shade place values that are multiples of 4 or 8 and explain why the last two "
          "or three digits decide divisibility by 4 and 8.",
          ["Every place value from tens upward is a multiple of 10, 5 and 2.",
           "100 is a multiple of 4 and 1000 is a multiple of 8."],
          items=[
              FIO("5.2.explain_4_8", "Checking Divisibility Quickly: the shortcuts for 4 and 8",
                  "Explain using algebra why the divisibility shortcuts for 4 and 8 work. Use them to test 3716 for 4 "
                  "and 51240 for 8.",
                  ["100 = 4 × 25, so 100c, 1000d and every higher place value are multiples of 4.",
                   "So a number is divisible by 4 exactly when its last two digits, 10b + a, form a multiple of 4.",
                   "1000 = 8 × 125, so 1000d and every higher place value are multiples of 8, and the last three "
                   "digits decide divisibility by 8.",
                   "3716 ends in 16, which is 4 × 4, so 3716 is divisible by 4.",
                   "51240 ends in 240, which is 8 × 30, so 51240 is divisible by 8."],
                  "4 needs the last two digits and 8 the last three; 3716 is divisible by 4 and 51240 by 8")],
          misconceptions=["M_LAST_DIGIT_9"])],
    key_terms=["place value", "divisible"]))

# ============================== T8 Shortcuts for 9 and 3 ===================================================
TOPICS.append(TOPIC(
    "T8", "M2", "Shortcuts for 9 and 3", ["5.2"], "Analyze",
    "Students explain why every place value leaves remainder 1 on division by 9 and by 3, use the digit sum to find "
    "remainders and test divisibility, and judge statements about the shortcut.",
    "10 is 9 + 1, 100 is 99 + 1, 1000 is 999 + 1, so every digit leaves itself as a remainder on division by 9. A "
    "number is divisible by 9 if and only if its digit sum is, and the same holds for 3.",
    [A("T8.C1", "Numbers made of nines and zeros", "Understand",
       "Students explain why any number made only of the digits 9 and 0 is divisible by 9, and why the units digit "
       "alone cannot test for 9.",
       textbook=["A Shortcut for Divisibility by 9",
                 "Can you say, without actually calculating, which of these numbers are divisible by 9: 999, 909, 900, "
                 "90, 990? All of them.",
                 "Can we say that any number made up of only the digits '0' and '9', in any order, will always be "
                 "divisible by 9?",
                 "Yes, if each digit is either 0 or 9, then each term in its expanded form will be 9 × or 0 × a place "
                 "value. This means each term will be a multiple of 9, for example, "
                 "99009 = 9 × 10000 + 9 × 1000 + 0 × 100 + 0 × 10 + 9 × 1.",
                 "But this shortcut alone cannot identify all the multiples of 9. Unlike the numbers 2, 5, and 10, we "
                 "cannot identify the multiples of 9 by just looking at the unit's digit. 99 and 109 are two numbers "
                 "with 9 as the units digit; but 99 is divisible by 9, while 109 is not."],
       teach=["Predict first: which of 999, 909, 900, 90 and 990 are divisible by 9?",
              "Each term of the expanded form is 9 times a place value or 0, so each term is a multiple of 9.",
              "The units digit is not enough: 99 and 109 both end in 9, but only 99 is a multiple of 9."],
       examples=[
           WE("Explain why 99009 is divisible by 9, and why 109 is not even though it ends in 9.",
              ["99009 = 9 × 10000 + 9 × 1000 + 0 × 100 + 0 × 10 + 9 × 1.",
               "Every term is 9 times a place value or zero, so the sum is a multiple of 9.",
               "109 = 99 + 10, and 10 = 9 + 1, so 109 is 1 more than a multiple of 9."],
              "99009 is a multiple of 9; 109 leaves remainder 1, so a units digit of 9 proves nothing",
              ncert=["5.2.nine_intro"])],
       key_terms=["place value", "divisible", "multiple of 9"], misconceptions=["M_LAST_DIGIT_9"], minutes=8),
     A("T8.C2", "Each place value leaves remainder 1", "Analyze",
       "Students show that every place value is one more than a multiple of 9, and add the digits to find the "
       "remainder of a number on division by 9.",
       textbook=["Is 10 divisible by 9? If not, what is the remainder?",
                 "Check the divisibility of other multiples of 10 (10, 20, 30, ...) by 9. You will notice that for any "
                 "multiple of 10, the remainder is the same as the number of tens.",
                 "Similarly, look at the remainder when the multiples of 100 (100, 200, 300, ...) are divided by 9. What "
                 "do you notice? The remainder is the same as the number of hundreds for any multiple of 100.",
                 "Using this observation, find the remainder when 427 is divided by 9.",
                 "We see that 427 has 4 hundreds; thus, its corresponding remainder (upon division by 9) would be 4. "
                 "427 has 2 tens, and its corresponding remainder would be 2. We have 7 units also remaining. Adding "
                 "all the remainders, we get 4 + 2 + 7 = 13. We can make one more group of 9 with 13, leaving a "
                 "remainder of 4. Therefore, 427 ÷ 9 gives a remainder of 4.",
                 "Will this work with bigger numbers? You can see that this is true for any place value: 1 = 0 + 1, "
                 "10 = 9 + 1, 100 = 99 + 1, 1000 = 999 + 1, 10000 = 9999 + 1, and so on. Each digit thus denotes the "
                 "remainder when the corresponding place value is divided by 9.",
                 "For example, to find the remainder of 7309 when divided by 9, we can just add all the digits, "
                 "7 + 3 + 0 + 9, to get 19.",
                 "7 × 1000 + 3 × 100 + 0 × 10 + 9 × 1 = (7 × 999 + 3 × 99 + 0 × 9 + 9 × 0) + (7 + 3 + 0 + 9). The "
                 "first part is a multiple of 9, so we need to just consider the second part.",
                 "This means that the number 7309 is 19 more than some multiple of 9. The digits 1 and 9 can further "
                 "be added to get 1 + 9 = 10. Now, we can say that 7309 is 10 more than a multiple of 9. And repeating "
                 "this step for the number 10, we get the remainder to be 1 + 0 = 1, meaning 7309 is 1 more than a "
                 "multiple of 9. Therefore, 7309 ÷ 9 gives a remainder of 1.",
                 "A number is divisible by 9 if and only if the sum of its digits is divisible by 9. Also, we can add "
                 "the digits of a number repeatedly till a single digit is obtained. This single digit is the remainder "
                 "when the number is divided by 9."],
       teach=["Predict first: what remainder does 10 leave on division by 9? What about 20, 30 and 400?",
              "Each place value is a block of nines plus a single one, so each digit leaves itself as a remainder.",
              "Add the leftovers, the digits, and take away nines until fewer than 9 remain.",
              "A number is divisible by 9 exactly when its digit sum is. A digit sum of exactly 9 means the remainder "
              "is 0."],
       examples=[
           WE("Find the remainders of 427 and 7309 on division by 9 without dividing.",
              ["427 = 4 × 99 + 2 × 9 + 4 + 2 + 7, so the leftovers are 4, 2 and 7.",
               "4 + 2 + 7 = 13, and 13 = 9 + 4, so 427 leaves remainder 4.",
               "7309 = 7 × 999 + 3 × 99 + 7 + 3 + 0 + 9, so the leftovers add to 19.",
               "19 = 9 + 10 and 10 = 9 + 1, so 7309 leaves remainder 1."],
              "427 leaves remainder 4 and 7309 leaves remainder 1",
              ncert=["5.2.nine_tens", "5.2.nine_427", "5.2.nine_bigger"])],
       key_terms=["remainder", "digit sum", "place value"], misconceptions=["M_LAST_DIGIT_9"], minutes=12),
     A("T8.C2x", "Which statements about the shortcut are correct?", "Evaluate",
       "Students judge four statements linking a number's divisibility by 9 with its digit sum, and see that all four "
       "follow from the if and only if rule.",
       textbook=["Look at each of the following statements. Which are correct and why?",
                 "(i) If a number is divisible by 9, then the sum of its digits is divisible by 9. (ii) If the sum of "
                 "the digits of a number is divisible by 9, then the number is divisible by 9. (iii) If a number is not "
                 "divisible by 9, then the sum of its digits is not divisible by 9. (iv) If the sum of the digits of a "
                 "number is not divisible by 9, then the number is not divisible by 9.",
                 "Learning maths is not just about knowing some shortcuts and following procedures but about "
                 "understanding 'why' something works."],
       teach=["Predict first: are all four statements true, or only some?",
              "A number and its digit sum always leave the same remainder on division by 9.",
              "So if one is divisible by 9, so is the other, and if one is not, neither is the other."],
       examples=[
           WE("Test the four statements with 7309 and 4581, then decide which are correct.",
              ["7309 has digit sum 19, and both leave remainder 1: neither is divisible by 9.",
               "4581 has digit sum 18, and both leave remainder 0: both are divisible by 9.",
               "A number and its digit sum always leave the same remainder, so they are divisible by 9 together or "
               "not at all."],
              "All four statements are correct",
              ncert=["5.2.nine_statements"])],
       key_terms=["digit sum", "divisible"], minutes=6, thin=True),
     A("T8.C3", "The shortcut for 3", "Apply",
       "Students explain that every place value also leaves remainder 1 on division by 3, and use the digit sum to "
       "test divisibility by 3.",
       textbook=["A Shortcut for Divisibility by 3",
                 "We know that all the multiples of 9 are also multiples of 3. That is, if a number is divisible by 9, "
                 "it will also be divisible by 3. However, there are other multiples of 3 that are not multiples of 9, "
                 "for example, 15, 33, and 87.",
                 "The shortcut to find the divisibility by 3 is similar to the method for 9. A number is divisible by 3 "
                 "if the sum of its digits is divisible by 3. Explore the remainders when powers of 10 are divided by 3. "
                 "Explain why this method works."],
       teach=["Predict first: what remainder do 10, 100 and 1000 leave on division by 3?",
              "9, 99 and 999 are multiples of 3, so 10, 100 and 1000 are each 1 more than a multiple of 3.",
              "So a number and its digit sum leave the same remainder on division by 3."],
       examples=[
           WE("Explain why 87 is divisible by 3 but not by 9, and test 123456 for divisibility by 3.",
              ["87 = 8 × 9 + 8 + 7, so 87 leaves the same remainder as 8 + 7 = 15.",
               "15 is a multiple of 3 but not of 9, so 87 is divisible by 3 but not by 9.",
               "123456 has digit sum 1 + 2 + 3 + 4 + 5 + 6 = 21, and 21 = 3 × 7.",
               "So 123456 is divisible by 3."],
              "87 is divisible by 3 but not by 9; 123456 is divisible by 3",
              ncert=["5.2.three"])],
       key_terms=["digit sum", "multiple of 3"], minutes=8),
     DOER("T8.C4", "Practice: nines, threes and digit sums", "nines_blocks", "Apply",
          "Students split numbers into nines and ones to test divisibility by 9, find multiples of 9 with given "
          "properties, and explain why shuffling the digits keeps a multiple of 9.",
          ["Every place value is a multiple of 9 plus 1, so a number leaves the same remainder as its digit sum.",
           "A number is divisible by 9 if and only if its digit sum is divisible by 9."],
          items=[
              FIO("FiO2.q1", "Figure it Out (%s, question 1)" % FIO2,
                  "Find, without dividing, whether the following numbers are divisible by 9. (i) 123 (ii) 405 "
                  "(iii) 8888 (iv) 93547 (v) 358095",
                  ["(i) 1 + 2 + 3 = 6, not a multiple of 9.",
                   "(ii) 4 + 0 + 5 = 9, a multiple of 9.",
                   "(iii) 8 + 8 + 8 + 8 = 32, not a multiple of 9.",
                   "(iv) 9 + 3 + 5 + 4 + 7 = 28, not a multiple of 9.",
                   "(v) 3 + 5 + 8 + 0 + 9 + 5 = 30, not a multiple of 9."],
                  "Only 405 is divisible by 9"),
              FIO("FiO2.q2", "Figure it Out (%s, question 2)" % FIO2,
                  "Find the smallest multiple of 9 with no odd digits.",
                  ["The digit sum must be a multiple of 9, and even digits always add to an even number, so it must be "
                   "18 or more.",
                   "Two even digits add to at most 16, so the number needs three digits.",
                   "The smallest hundreds digit is 2, and the other two digits must then add to 16: 8 and 8.",
                   "Check: 2 + 8 + 8 = 18."],
                  "288"),
              FIO("FiO2.q3", "Figure it Out (%s, question 3)" % FIO2,
                  "Find the multiple of 9 that is closest to the number 6000.",
                  ["6000 has digit sum 6, so it is 6 more than a multiple of 9: 5994.",
                   "So the next multiple of 9 is 5994 + 9 = 6003, which is only 3 more than 6000.",
                   "6003 is 3 away and 5994 is 6 away."],
                  "6003"),
              FIO("FiO2.q4", "Figure it Out (%s, question 4)" % FIO2,
                  "How many multiples of 9 are there between the numbers 4300 and 4400?",
                  ["4300 has digit sum 7, so the first multiple of 9 after it is 4300 + 2 = 4302.",
                   "4400 has digit sum 8, so the last multiple of 9 before it is 4400 − 8 = 4392.",
                   "From 4302 to 4392 is 90, which is 10 steps of 9, so there are 11 multiples."],
                  "11 multiples of 9 (4302 to 4392)"),
              FIO("FiO4.q1", "Figure it Out (%s, question 1)" % FIO4,
                  "If 31z5 is a multiple of 9, where z is a digit, what is the value of z? Explain why there are two "
                  "answers to this problem.",
                  ["The digit sum is 3 + 1 + z + 5, which is 9 + z.",
                   "9 + z must be a multiple of 9, so z is 0 or 9, since z is a single digit.",
                   "3105 and 3195 both have digit sums that are multiples of 9, and the next case, z = 18, is not a "
                   "digit."],
                  "z = 0 or z = 9 (3105 and 3195); two answers because 0 and 9 both keep the digit sum a multiple of 9"),
              FIO("FiO4.q4", "Figure it Out (%s, question 4)" % FIO4,
                  "Sreelatha says, \"I have a number that is divisible by 9. If I reverse its digits, it will still be "
                  "divisible by 9\". (i) Examine if her conjecture is true for any multiple of 9. (ii) Are any other "
                  "digit shuffles possible such that the number formed is still a multiple of 9?",
                  ["(i) Reversing the digits keeps the same digits, so the digit sum stays the same.",
                   "The digit sum of a multiple of 9 is a multiple of 9, so the reversed number is also a multiple of 9: "
                   "468 is 9 × 52 and 864 is 9 × 96.",
                   "(ii) Any shuffle keeps the same digit sum, so every shuffle is still a multiple of 9: 648 is 9 × 72."],
                  "(i) True for every multiple of 9 (ii) Yes, every shuffle of the digits is still a multiple of 9")],
          misconceptions=["M_LAST_DIGIT_9"])],
    key_terms=["digit sum", "remainder", "multiple of 9", "multiple of 3"]))

# ============================== T9 Shortcut for 11 =========================================================
TOPICS.append(TOPIC(
    "T9", "M2", "A Shortcut for 11", ["5.2"], "Analyze",
    "Students show that place values are alternately one more and one less than a multiple of 11, and use the excess "
    "minus shortfall, or alternating signs, to test divisibility by 11 and find remainders.",
    "1, 100, 10000, ... are one more than a multiple of 11 and 10, 1000, 100000, ... are one less. So the remainder on "
    "division by 11 comes from the digits in the odd places minus the digits in the even places, counted from the "
    "units.",
    [A("T9.C1", "Place values: one more, one less", "Analyze",
       "Students find that place values alternate between one more and one less than a multiple of 11, and use this to "
       "decide whether 462 is divisible by 11.",
       textbook=["A Shortcut for Divisibility by 11",
                 "Interestingly, the shortcut for 11 is also based on checking the remainders with place value. Let us "
                 "see how.",
                 "Units place (1): 1 = 11 × 0 + 1, 1 is one more than a multiple of 11. Tens place (10): 10 = 11 × 1 "
                 "− 1, 10 is one less than a multiple of 11. Hundreds place (100): 100 = 11 × 9 + 1, 100 is one more "
                 "than a multiple of 11. Thousands place (1000): 1000 = 11 × 91 − 1, 1000 is one less than a multiple "
                 "of 11.",
                 "This alternating pattern of one more than 11 and one less than 11 continues for higher place values.",
                 "Since 400 contains 4 hundreds, 400 is 4 more than a multiple of 11 (396 + 4). Since 60 contains 6 "
                 "tens, 60 is 6 less than a multiple of 11 (66 − 6). Since 2 contains 2 units, 2 is 2 more than a "
                 "multiple of 11, i.e., 2 = (0 + 2).",
                 "Using these observations, can you tell whether the number 462 is divisible by 11?",
                 "What could be a general method or shortcut to check divisibility by 11?"],
       teach=["Predict first: is 462 divisible by 11? Does adding its digits help, as it did for 9?",
              "100 = 11 × 9 + 1 is one more than a multiple of 11, but 10 = 11 × 1 − 1 is one less.",
              "So hundreds and units add to the excess, while tens take away from it.",
              "For 462 the 4 hundreds give 4 extra, the 2 units give 2 extra, and the 6 tens are 6 short."],
       examples=[
           WE("Use the remainders of the place values to decide whether 462 is divisible by 11.",
              ["400 = 396 + 4, and 396 = 11 × 36, so 400 is 4 more than a multiple of 11.",
               "60 = 66 − 6, and 66 = 11 × 6, so 60 is 6 less than a multiple of 11.",
               "2 is 2 more than a multiple of 11.",
               "Altogether the excess is 4 + 2 − 6 = 0, so 462 is a multiple of 11: 462 = 11 × 42."],
              "462 is divisible by 11",
              ncert=["5.2.eleven_table", "5.2.eleven_462"])],
       key_terms=["place value", "remainder", "multiple of 11"], misconceptions=["M_ELEVEN_SUM"], minutes=10),
     A("T9.C2", "Total excess minus total shortfall", "Apply",
       "Students add the digits in the places that are one more and those that are one less than a multiple of 11, and "
       "use the difference to find the remainder on division by 11.",
       textbook=["We saw that the place values alternate as 1 more and 1 less than a multiple of 11. Using this "
                 "observation,",
                 "1. Add the digits of place values which are 1 more (than a multiple of 11), i.e., place values "
                 "corresponding to 1, 100, 10000, and so on. Purpose: to know how much in excess we are with respect to "
                 "a multiple of 11 for these place values. For the number 320185: total excess, 2 + 1 + 5 = 8.",
                 "2. Add the digits of place values which are 1 less (than a multiple of 11), i.e., place values "
                 "corresponding to 10, 1000, 100000, and so on. Purpose: to know how short we are with respect to a "
                 "multiple of 11 for these place values. Total short, 3 + 0 + 8 = 11.",
                 "3. Compute the difference between these two sums, i.e., (number in excess) − (number short). Purpose: "
                 "to know the remainder obtained when divided by 11. 8 − 11 = −3 (3 short of a multiple of 11).",
                 "If this difference is 11 or a multiple of 11, what does that say about the remainder obtained when "
                 "the number is divisible by 11?"],
       teach=["Predict first: 320185 has digit sum 19. Does that tell us anything about division by 11?",
              "Add the digits in the units, hundreds and ten thousands places: that is the excess.",
              "Add the digits in the tens, thousands and lakhs places: that is the shortfall.",
              "Excess minus shortfall gives the remainder; if the difference is 0 or a multiple of 11, the number is "
              "divisible by 11."],
       examples=[
           WE("Use the excess and the shortfall to find the remainder of 320185 on division by 11.",
              ["Places one more than a multiple of 11 (units, hundreds, ten thousands) hold 5, 1 and 2: excess "
               "2 + 1 + 5 = 8.",
               "Places one less (tens, thousands, lakhs) hold 8, 0 and 3: shortfall 3 + 0 + 8 = 11.",
               "8 − 11 = −3, so 320185 is 3 short of a multiple of 11.",
               "3 short means 8 more than the multiple before it: 320185 = 11 × 29107 + 8."],
              "320185 leaves remainder 8 on division by 11 (it is 3 short of a multiple of 11)",
              ncert=["5.2.eleven_steps"])],
       key_terms=["remainder", "excess", "shortfall"], misconceptions=["M_ELEVEN_SUM"], minutes=10),
     A("T9.C3", "Alternating plus and minus signs", "Apply",
       "Students place alternating signs before the digits starting from the units digit, evaluate the expression, and "
       "compare this procedure with the excess and shortfall method.",
       textbook=["Look at the following procedure.",
                 "1. Place alternating '+' and '−' signs before every digit starting from the unit's digit. Example for "
                 "the number 328105: −3 + 2 − 8 + 1 − 0 + 5.",
                 "2. Evaluate the expression. −3 + 2 − 8 + 1 − 0 + 5 = −3",
                 "3. The result denotes the remainder obtained when the number is divided by 11. 328105 is 3 less than "
                 "or 8 more than a multiple of 11.",
                 "Is this method similar to or different from the method we saw just before?"],
       teach=["Predict first: 328105 and 320185 have the same digits in a different order. Will they leave the same "
              "remainder on division by 11?",
              "Put + before the units digit, − before the tens digit, and keep alternating to the left.",
              "The plus digits are the excess and the minus digits are the shortfall, so this is the same method in one "
              "line.",
              "A negative result such as −3 means 3 short, so the remainder is 11 − 3 = 8."],
       examples=[
           WE("Use alternating signs to find the remainder of 328105 on division by 11.",
              ["Starting from the units digit, the signs give −3 + 2 − 8 + 1 − 0 + 5.",
               "−3 + 2 − 8 + 1 − 0 + 5 = −3.",
               "So 328105 is 3 short of a multiple of 11, which is 8 more than the multiple before it.",
               "Check: 328105 = 11 × 29827 + 8."],
              "328105 leaves remainder 8 on division by 11",
              ncert=["5.2.eleven_alt"])],
       key_terms=["alternating signs", "remainder"], misconceptions=["M_ELEVEN_SUM"], minutes=8),
     DOER("T9.C4", "Practice: testing for 11", "excess_shortfall_board", "Apply",
          "Students use the shortcut for testing divisibility by 11 to find remainders, and find missing digits that "
          "make a number divisible by 44.",
          ["Alternate + and − before the digits starting from the units digit.",
           "A result of 0 or a multiple of 11 means divisible; a negative result r means 11 + r is the remainder."],
          items=[
              FIO("5.2.eleven_test", "A Shortcut for Divisibility by 11: test and find remainders",
                  "Using this shortcut, find out whether the following numbers are divisible by 11. Further, find the "
                  "remainder if the number is not divisible by 11. (i) 158 (ii) 841 (iii) 481 (iv) 5529 (v) 90904 "
                  "(vi) 857076",
                  ["(i) 158: 8 − 5 + 1 = 4, remainder 4.",
                   "(ii) 841: 1 − 4 + 8 = 5, remainder 5.",
                   "(iii) 481: 1 − 8 + 4 = −3, which is 3 short, so remainder 8.",
                   "(iv) 5529: 9 − 2 + 5 − 5 = 7, remainder 7.",
                   "(v) 90904: 4 − 0 + 9 − 0 + 9 = 22, a multiple of 11, so divisible.",
                   "(vi) 857076: 6 − 7 + 0 − 7 + 5 − 8 = −11, a multiple of 11, so divisible."],
                  "(i) remainder 4 (ii) remainder 5 (iii) remainder 8 (iv) remainder 7 (v) divisible (vi) divisible"),
              FIO("FiO4.q6", "Figure it Out (%s, question 6)" % FIO4,
                  "If 3p7q8 is divisible by 44, list all possible pairs of values for p and q.",
                  ["44 is 4 × 11, and 4 and 11 share no factor, so the number must pass both tests.",
                   "For 4 the last two digits q8 must be a multiple of 4: 08, 28, 48, 68 and 88 all are, so q is even.",
                   "For 11: 8 − q + 7 − p + 3 = 18 − (p + q) must be 0 or a multiple of 11, so p + q is 7 or 18.",
                   "p + q = 18 needs p = q = 9, which is odd; p + q = 7 with q even gives (7, 0), (5, 2), (3, 4), "
                   "(1, 6)."],
                  "(p, q) = (7, 0), (5, 2), (3, 4), (1, 6)")],
          misconceptions=["M_ELEVEN_SUM"])],
    key_terms=["remainder", "alternating signs", "multiple of 11"]))

# ============================== T10 More on divisibility shortcuts =========================================
TOPICS.append(TOPIC(
    "T10", "M2", "More on Divisibility Shortcuts", ["5.2"], "Evaluate",
    "Students test divisibility by 6 through 2 and 3, explain with prime factorisation why 3 and 8 test for 24 but 4 "
    "and 6 do not, and fill a divisibility table quickly.",
    "To test for a number, test for factors that share no common factor and multiply to it: 2 and 3 for 6, 3 and 8 "
    "for 24. Factors that share a factor, like 4 and 6, only test for their LCM.",
    [A("T10.C1", "Divisibility by 6 through 2 and 3", "Apply",
       "Students check divisibility by 6 by testing for 2 and for 3, and verify by dividing.",
       textbook=["More on Divisibility Shortcuts",
                 "How can we find out if a number is divisible by 6?",
                 "Will checking its divisibility by its factors 2 and 3 work? Use the shortcuts for 2 and 3 on these "
                 "numbers and divide each number by 6 to verify: 38, 225, 186, 64."],
       teach=["Predict first: if a number is even and its digit sum is a multiple of 3, must it be a multiple of 6?",
              "A number divisible by 2 and by 3 is divisible by their LCM, and the LCM of 2 and 3 is 6.",
              "So test the units digit for 2 and the digit sum for 3."],
       examples=[
           WE("Use the shortcuts for 2 and 3 to decide which of 38, 225, 186 and 64 are divisible by 6, then check by "
              "dividing.",
              ["38 is even, but 3 + 8 = 11 is not a multiple of 3, so 38 fails the test for 3.",
               "225 has digit sum 9, but it is odd, so it fails the test for 2.",
               "186 is even and 1 + 8 + 6 = 15 is a multiple of 3, so it passes both: 186 = 6 × 31.",
               "64 is even, but 6 + 4 = 10 is not a multiple of 3."],
              "Only 186 is divisible by 6",
              ncert=["5.2.six"])],
       key_terms=["factor", "divisible", "LCM"], minutes=8),
     A("T10.C2", "Divisibility by 24: 3 and 8, not 4 and 6", "Evaluate",
       "Students explain with prime factorisation why testing for 3 and 8 checks divisibility by 24, while testing for "
       "4 and 6 does not.",
       textbook=["How about checking divisibility by 24? Will checking the divisibility by its factors, 4 and 6, work? "
                 "Why or why not?",
                 "Determining divisibility by 24 by checking divisibility by 4 and by 6 does not work. For example, the "
                 "number 12 is divisible by both 4 and 6, but not by 24.",
                 "To check for the divisibility by 24, we can instead check for the divisibility by 3 and divisibility "
                 "by 8.",
                 "Explain using prime factorisation why checking divisibility by 3 and 8 works for checking "
                 "divisibility by 24, but checking divisibility by 4 and 6 is not sufficient for checking divisibility "
                 "by 24.",
                 "There are such shortcuts to check divisibility by every number until 100, and for some numbers beyond "
                 "100. You may try to understand how these work after learning certain concepts in higher grades."],
       teach=["Predict first: 4 × 6 is 24. Does passing the tests for 4 and 6 prove a number is divisible by 24?",
              "24 is 2 × 2 × 2 × 3. Passing 4 shows two 2s and passing 6 shows one 2 and a 3, but the 2 in 6 may be "
              "one of the two 2s already counted.",
              "8 is 2 × 2 × 2 and 3 is a different prime, so passing both shows all of 2 × 2 × 2 × 3."],
       examples=[
           WE("Use prime factorisation to explain why 12 passes the tests for 4 and 6 but is not divisible by 24, and "
              "why the tests for 3 and 8 never let such a number through.",
              ["12 is 2 × 2 × 3: divisible by 4, which is 2 × 2, and by 6, which is 2 × 3.",
               "24 is 2 × 2 × 2 × 3 and needs three 2s, but 12 has only two, because 4 and 6 share a 2.",
               "8 is 2 × 2 × 2 and 3 shares no factor with it, so a number passing both holds 2 × 2 × 2 × 3.",
               "The LCM of 3 and 8 is 24, while the LCM of 4 and 6 is only 12."],
              "4 and 6 only test for 12, their LCM; 3 and 8 test for 24",
              ncert=["5.2.twentyfour"])],
       key_terms=["prime factorisation", "LCM", "common factor"], misconceptions=["M_PRODUCT_RULE"], minutes=10),
     DOER("T10.C3", "Practice: trapping combined tests", "combined_divisibility_trap", "Evaluate",
          "Students fill a divisibility table quickly, find missing digits that make a number a multiple of 18, and "
          "build numbers that pass two tests at once.",
          ["Test for a number using factors that share no common factor and multiply to it.",
           "Passing two tests shows divisibility by the LCM of the two divisors."],
          items=[
              FIO("5.2.table", "Checking Divisibility Quickly: fill the table",
                  "Fill in the following table: for each of 128, 990, 1586, 275, 6686, 639210, 429714, 2856, 3060 and "
                  "406839, write Yes or No for divisibility by 2, 3, 4, 5, 6, 8, 9, 10 and 11. Find a quick way to do "
                  "this.",
                  ["Columns in the order 2, 3, 4, 5, 6, 8, 9, 10, 11. Use the units digit for 2, 5 and 10, the last "
                   "two or three digits for 4 and 8, the digit sum for 3 and 9, 2 and 3 for 6, and alternating signs "
                   "for 11.",
                   "128: Yes, No, Yes, No, No, Yes, No, No, No (128 is 4 × 32).",
                   "990: Yes, Yes, No, Yes, Yes, No, Yes, Yes, Yes.",
                   "1586: Yes, No, No, No, No, No, No, No, No.",
                   "275: No, No, No, Yes, No, No, No, No, Yes.",
                   "6686: Yes, No, No, No, No, No, No, No, No.",
                   "639210: Yes, Yes, No, Yes, Yes, No, No, Yes, Yes.",
                   "429714: Yes, Yes, No, No, Yes, No, Yes, No, No.",
                   "2856: Yes, Yes, Yes, No, Yes, Yes, No, No, No.",
                   "3060: Yes, Yes, Yes, Yes, Yes, No, Yes, Yes, No.",
                   "406839: No, Yes, No, No, No, No, No, No, No."],
                  "Divisible by (2, 3, 4, 5, 6, 8, 9, 10, 11): 128 Y N Y N N Y N N N; 990 Y Y N Y Y N Y Y Y; 1586 Y N N "
                  "N N N N N N; 275 N N N Y N N N N Y; 6686 Y N N N N N N N N; 639210 Y Y N Y Y N N Y Y; 429714 Y Y N N "
                  "Y N Y N N; 2856 Y Y Y N Y Y N N N; 3060 Y Y Y Y Y N Y Y N; 406839 N Y N N N N N N N. Quick check: a "
                  "Yes for 4 or 8 needs a Yes for 2, a Yes for 9 needs a Yes for 3, and 6 is Yes exactly when 2 and 3 "
                  "are"),
              FIO("FiO4.q5", "Figure it Out (%s, question 5)" % FIO4,
                  "If 48a23b is a multiple of 18, list all possible pairs of values for a and b.",
                  ["18 is 2 × 9, and 2 and 9 share no factor, so the number must pass both tests.",
                   "For 2, b must be even.",
                   "For 9, 4 + 8 + a + 2 + 3 + b = 17 + a + b must be a multiple of 9, so a + b is 1 or 10.",
                   "a + b = 1 with b even gives (1, 0); a + b = 10 with b even gives (2, 8), (4, 6), (6, 4), (8, 2)."],
                  "(a, b) = (1, 0), (2, 8), (4, 6), (6, 4), (8, 2)"),
              FIO("FiO4.q8", "Figure it Out (%s, question 8)" % FIO4,
                  "Write five multiples of 36 between 45000 and 47000. Share your approach with the class.",
                  ["36 is 4 × 9, and 4 and 9 share no factor, so a multiple of 36 passes the tests for 4 and 9.",
                   "45000 = 36 × 1250, so 45000 is itself a multiple of 36.",
                   "Keep adding 36: 45036, 45072, 45108, 45144, 45180.",
                   "Check 45108: its last two digits 08 make a multiple of 4, and its digit sum 18 is a multiple of 9."],
                  "45036, 45072, 45108, 45144, 45180"),
              FIO("FiO4.q10", "Figure it Out (%s, question 10)" % FIO4,
                  "Write a 6-digit number that is divisible by 15, such that when the digits are reversed, it is "
                  "divisible by 6.",
                  ["Divisible by 15 means divisible by 3 and 5; the reversed number must be divisible by 2 and 3.",
                   "The units digit must be 0 or 5, and it becomes the first digit when reversed, so it must be 5.",
                   "The first digit becomes the units digit when reversed, so it must be even, say 2.",
                   "Choose the middle digits so the digit sum is a multiple of 3: 200025 has digit sum 9.",
                   "200025 ends in 5 with digit sum 9, and 520002 is even with digit sum 9."],
                  "For example 200025 (reversed 520002); any number starting with an even digit, ending in 5, with digit "
                  "sum a multiple of 3 works")],
          misconceptions=["M_PRODUCT_RULE"])],
    key_terms=["prime factorisation", "LCM", "divisible"]))

# ============================== T11 Digital roots ==========================================================
TOPICS.append(TOPIC(
    "T11", "M2", "Digital Roots", ["5.2"], "Analyze",
    "Students find digital roots, list numbers in a range with a given digital root, explain the patterns of digital "
    "roots of consecutive numbers and of multiples, and link the digital root with the remainder on division by 9.",
    "The digital root is the single digit left after adding digits repeatedly. It equals the remainder on division by "
    "9, except that multiples of 9 have digital root 9, so digital roots of consecutive numbers cycle through 1 to 9.",
    [A("T11.C1", "Finding a digital root", "Understand",
       "Students find the digital root of a number by adding its digits repeatedly, and connect it with the remainder "
       "on division by 9.",
       textbook=["Digital Roots",
                 "Take a number. Add its digits repeatedly till you get a single-digit number. This single-digit number "
                 "is called the digital root of the number. For example, the digital root of the number 489710 will be "
                 "2 (4 + 8 + 9 + 7 + 1 + 0 = 29; 2 + 9 = 11; 1 + 1 = 2).",
                 "What property do you think this digital root will have? Recall that we did this while finding the "
                 "divisibility shortcut for 9.",
                 "Aryabhata II's (c. 950 CE) work Mahāsiddhānta, mentions the method of computing the digital root of a "
                 "number by repeatedly adding the digits till a single-digit number is obtained. This method is known "
                 "to have been used to perform checks on calculations of arithmetic operations."],
       teach=["Predict first: what single digit is left if you keep adding the digits of 489710?",
              "Adding the digits keeps the remainder on division by 9, so the digital root is that remainder.",
              "The one difference: a multiple of 9 has digital root 9, not 0.",
              "Aryabhata II described this method over a thousand years ago to check calculations."],
       examples=[
           WE("Find the digital roots of 489710 and 4581, and say what they tell you about division by 9.",
              ["4 + 8 + 9 + 7 + 1 + 0 = 29. Then 2 + 9 = 11, and 1 + 1 = 2.",
               "So 489710 has digital root 2 and leaves remainder 2 on division by 9.",
               "4 + 5 + 8 + 1 = 18. Then 1 + 8 = 9.",
               "So 4581 has digital root 9 and is a multiple of 9: 4581 = 9 × 509."],
              "489710 has digital root 2 (remainder 2); 4581 has digital root 9 (a multiple of 9)",
              ncert=["5.2.dr_def", "5.2.aryabhata"])],
       key_terms=["digital root", "remainder"], misconceptions=["M_DIGITAL_ROOT_ZERO"], minutes=8),
     A("T11.C2", "Numbers in a range with a given digital root", "Apply",
       "Students list the numbers between 600 and 700 with a given digital root by stepping through the range in nines.",
       textbook=["Between the numbers 600 and 700, which numbers have the digital root: (i) 5, (ii) 7, (iii) 3?"],
       teach=["Predict first: how many numbers between 600 and 700 have digital root 5?",
              "Find the first one, then keep adding 9: adding 9 never changes the digital root.",
              "Each digital root turns up about once in every 9 numbers, so about 11 times between 600 and 700."],
       examples=[
           WE("Between 600 and 700, list the numbers with digital root 5, 7 and 3.",
              ["Digital root 5: 608 has digit sum 14 and root 5; adding 9 each time gives 608, 617, 626, 635, 644, "
               "653, 662, 671, 680, 689, 698.",
               "Digital root 7: 601 has digit sum 7; adding 9 gives 601, 610, 619, 628, 637, 646, 655, 664, 673, 682, "
               "691.",
               "Digital root 3: 606 has digit sum 12 and root 3; adding 9 gives 606, 615, 624, 633, 642, 651, 660, "
               "669, 678, 687, 696."],
              "Eleven numbers for each digital root, starting at 608, 601 and 606 and going up in nines",
              ncert=["5.2.dr_range"])],
       key_terms=["digital root"], minutes=8),
     A("T11.C3", "Patterns in digital roots", "Analyze",
       "Students write digital roots of consecutive numbers and of consecutive multiples of 3, 4 and 6, and explain "
       "the cycles they see.",
       textbook=["Write the digital roots of any 12 consecutive numbers. What do you observe?",
                 "We saw that the digital root of multiples of 9 is always 9.",
                 "Now, find the digital roots of some consecutive multiples of (i) 3, (ii) 4, and (iii) 6.",
                 "What are the digital roots of numbers that are 1 more than a multiple of 6? What do you notice?",
                 "Try to explain the patterns noticed."],
       teach=["Predict first: what are the digital roots of 25, 26, 27, ..., 36?",
              "Each step of 1 raises the digital root by 1, and after 9 it starts again at 1.",
              "Multiples of 3 add 3 each time, so their roots cycle 3, 6, 9; multiples of 6 cycle 6, 3, 9.",
              "Multiples of 4 add 4 each time and pass through all nine roots before repeating."],
       examples=[
           WE("Write the digital roots of the consecutive multiples of 4 from 4 to 36, and of the numbers 7, 13, 19, "
              "25, 31, which are 1 more than multiples of 6.",
              ["4, 8, 12, 16, 20, 24, 28, 32, 36 have digital roots 4, 8, 3, 7, 2, 6, 1, 5, 9.",
               "Each step adds 4 to the root, taking away 9 when it passes 9, so all nine roots appear before the "
               "cycle repeats.",
               "7, 13, 19, 25, 31 have digital roots 7, 4, 1, 7, 4.",
               "Adding 6 is the same as taking away 3 from the root, so 6k + 1 cycles through 7, 4, 1."],
              "Multiples of 4 cycle through all nine roots; numbers 1 more than multiples of 6 cycle 7, 4, 1",
              ncert=["5.2.dr_consec", "5.2.dr_multiples"])],
       key_terms=["digital root", "pattern"], misconceptions=["M_DIGITAL_ROOT_ZERO"], minutes=10),
     A("T11.C3x", "A digital root riddle", "Apply",
       "Students solve a riddle about a number whose digits, digit count, digit sum and digital root all point to the "
       "largest odd single digit.",
       textbook=["I'm made of digits, each tiniest and odd, No shared ground with root #1, how odd! My digits count, "
                 "their sum, my root, All point to one bold number's pursuit, The largest odd single-digit I proudly "
                 "claim. What's my number? What's my name?"],
       teach=["Predict first: what is the smallest odd digit, and what is the largest odd single digit?",
              "Every digit is 1, the tiniest odd digit, and the count of digits, the digit sum and the root are all 9.",
              "So the number has nine ones."],
       examples=[
           WE("Solve the riddle: digits each the tiniest odd digit, with the digit count, digit sum and digital root "
              "all equal to the largest odd single digit.",
              ["The tiniest odd digit is 1, so every digit is 1.",
               "The largest odd single digit is 9, so there are nine digits.",
               "Nine ones have digit sum 9 and digital root 9."],
              "111111111",
              ncert=["5.2.dr_riddle"])],
       key_terms=["digital root"], minutes=4, thin=True),
     DOER("T11.C4", "Practice: digital roots", "digital_root_dial", "Analyze",
          "Students predict how digital roots change when a fixed number is added, find the digital root of an "
          "expression, and make conjectures linking digital roots with parity and remainders.",
          ["Adding a number adds its digital root to the digital root, taking away 9 when the total passes 9.",
           "The digital root is the remainder on division by 9, with 9 in place of 0."],
          items=[
              FIO("FiO3.q1", "Figure it Out (%s, question 1)" % FIO3,
                  "The digital root of an 8-digit number is 5. What will be the digital root of 10 more than that "
                  "number?",
                  ["10 is 9 + 1, so adding 10 adds 1 to the remainder on division by 9.",
                   "So the digital root goes up from 5 to 6.",
                   "Check with 10000004: its digital root is 5, and 10000014 has digital root 6."],
                  "6"),
              FIO("FiO3.q2", "Figure it Out (%s, question 2)" % FIO3,
                  "Write any number. Generate a sequence of numbers by repeatedly adding 11. What would be the digital "
                  "roots of this sequence of numbers? Share your observations.",
                  ["11 is 9 + 2, so adding 11 raises the digital root by 2, taking away 9 when it passes 9.",
                   "Starting from 5: 5, 16, 27, 38, 49, 60 have digital roots 5, 7, 9, 2, 4, 6.",
                   "The roots go up in twos and all nine roots appear before the pattern repeats."],
                  "The digital roots go up by 2 each time (after 9, start again), so all nine appear before repeating"),
              FIO("FiO3.q3", "Figure it Out (%s, question 3)" % FIO3,
                  "What will be the digital root of the number 9a + 36b + 13?",
                  ["9a and 36b are multiples of 9, so they leave no remainder on division by 9.",
                   "So the number leaves the same remainder as 13, and 1 + 3 = 4.",
                   "Check with a = 1 and b = 1: 9 + 36 + 13 = 58, and 5 + 8 = 13, then 1 + 3 = 4."],
                  "4"),
              FIO("FiO3.q4", "Figure it Out (%s, question 4)" % FIO3,
                  "Make conjectures by examining if there are any patterns or relations between (i) the parity of a "
                  "number and its digital root. (ii) the digital root of a number and the remainder obtained when the "
                  "number is divided by 3 or 9.",
                  ["(i) 10 is even with digital root 1, and 11 is odd with digital root 2; 12 is even with root 3.",
                   "So the parity of a number does not decide the parity of its digital root.",
                   "(ii) The digital root equals the remainder on division by 9, except that a root of 9 means "
                   "remainder 0.",
                   "The remainder on division by 3 is the remainder of the digital root on division by 3: 3, 6 and 9 "
                   "give 0."],
                  "(i) No fixed link between parity and digital root (ii) The digital root is the remainder on division "
                  "by 9 (9 for remainder 0), and its remainder on division by 3 is the number's remainder on division "
                  "by 3")],
          misconceptions=["M_DIGITAL_ROOT_ZERO"])],
    key_terms=["digital root", "remainder", "pattern"]))
