# -*- coding: utf-8 -*-
"""Topics T11 to T16 (modules M3 and M4). Book sections 3.7 and 3.8, the end of chapter questions and the summary."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T11 Adding decimals ==========================================================
TOPICS.append(TOPIC(
    "T11", "M3", "Adding Decimals", ["3.7"], "Apply",
    "Students add decimals by lining up the decimal points and adding place by place with carrying, and estimate "
    "a sum from the whole number parts before computing.",
    "Decimals are added like whole numbers once the points are in one line; the whole number parts give a range "
    "that the sum must fall in.",
    [A("T11.C1", "Adding decimals place by place", "Apply",
       "Students add two decimals in the compact column form with the decimal points in one line, carrying from the "
       "right, and connect it to the place value working.",
       textbook=["3.7 Addition and Subtraction of Decimals",
                 "Priya requires 2.7 m of cloth for her skirt, and Shylaja requires 3.5m for her kurti. What is the "
                 "total quantity of cloth needed? We have to find the sum of 2.7m + 3.5m.",
                 "Earlier, we saw how to add 2 7/10 + 3 5/10 (also shown below). Can you carry out the same addition "
                 "using decimal notation? It is shown below. Share your observations. The total quantity of cloth "
                 "needed is 6.2 m.",
                 "As you can see, the standard procedure for adding and subtracting whole numbers can be used to add "
                 "and subtract decimals.",
                 "A detailed view of the underlying place value calculation is shown below for the sum 75.345 + "
                 "86.691. Its compact form is shown next to it."],
       teach=["Predict first: 2.7 and 3.5. The tenths are 7 and 5. Will they need a carry?",
              "Line up the decimal points, then add from the right, exactly as with whole numbers.",
              "The point stays in its place in the answer."],
       examples=[
           WE("Priya needs 2.7 m of cloth and Shylaja needs 3.5 m. How much cloth is needed in all? Compare with "
              "adding 2 7/10 and 3 5/10.",
              ["Write the numbers with the points in one line: 2.7 above 3.5.",
               "Tenths: 7 + 5 = 12 tenths, which is 1 unit and 2 tenths. Write 2 and carry 1.",
               "Units: 2 + 3 + 1 carried = 6. The point stays between the 6 and the 2.",
               "In fractions, 2 7/10 + 3 5/10 = 5 12/10 = 6 2/10, which is 6.2 again."],
              "6.2 m", ncert=["3.7.cloth_add"]),
           WE("Add 75.345 and 86.691 in the compact form, and say what each carry means.",
              ["Line up the points: 75.345 above 86.691.",
               "Thousandths: 5 + 1 = 6. Hundredths: 4 + 9 = 13, so write 3 and carry 1 to the tenths.",
               "Tenths: 3 + 6 + 1 = 10, so write 0 and carry 1 to the units. Units: 5 + 6 + 1 = 12, so write 2 and "
               "carry 1 to the tens.",
               "Tens: 7 + 8 + 1 = 16, so write 6 and carry 1 to the hundreds. Hundreds: 1.",
               "The sum is 162.036."],
              "162.036", ncert=["3.7.detail_add"])],
       key_terms=["carry"], misconceptions=["M_POINT_ALIGN"], minutes=10),
     A("T11.C2", "Estimating a sum first", "Analyze",
       "Students test Sonu's claim about the range in which the sum of two decimals lies, and use it to check a "
       "sum before computing.",
       textbook=["Estimating Sums and Differences",
                 "Sonu has observed sums and differences of decimal numbers and says, “If we add two decimal "
                 "numbers, then the sum will always be greater than the sum of their whole number parts. Also, the "
                 "sum will always be less than 2 more than the sum of their whole number parts.”",
                 "Let us use an example to understand what his claim means: If the two numbers to be added are "
                 "25.936 and 8.202, the claim is that their sum will be greater than 25 + 8 (whole number parts) and "
                 "will be less than 25 + 1 + 8 + 1.",
                 "What do you think about this claim? Verify if this is true for these numbers. Will it work for "
                 "any 2 decimal numbers? What about for the sum of 25.93603259 and 8.202?",
                 "Note to the Teacher: Estimating the result before computing may help in identifying if a mistake "
                 "happens with the calculation."],
       teach=["Predict first: 25.936 and 8.202. What is the least the sum could be, and what is the most?",
              "Each decimal is its whole part plus a fraction that is less than 1. So the sum is the whole parts "
              "total plus something that is at least 0 and under 2.",
              "Check the claim for 25.936 and 8.202, and for 25.93603259 and 8.202, then think about when the sum "
              "is exactly the whole parts total."],
       examples=[
           WE("Check Sonu's claim for 25.936 and 8.202, and for 25.93603259 and 8.202.",
              ["Whole parts: 25 and 8, total 33. The range from the claim is 33 to 35.",
               "25.936 + 8.202 = 34.138. It is above 33 and below 35, so the claim holds.",
               "25.93603259 + 8.202 = 34.13803259, which also lies between 33 and 35.",
               "Each fractional part is under 1, so two of them together are under 2. That is why the sum stays "
               "under the whole parts total plus 2.",
               "The sum equals the whole parts total only when both fractional parts are zero, such as 5.0 and 3.0, "
               "so 'greater than' should really read 'greater than or equal to'."],
              "34.138 and 34.13803259 both lie between 33 and 35; the claim holds for any two decimals, with "
              "'equal to' allowed at the low end", ncert=["3.7.est_sum"])],
       key_terms=["estimate"], misconceptions=["M_EST_RANGE"], minutes=10),
     DOER("T11.C3", "Practice: add decimals with the points in a line", "point_aligned_addition_column", "Apply",
          "Students add decimals with the points in a line, carrying from the right, and check each sum against an "
          "estimate.",
          ["Line up the decimal points before adding.",
           "Add from the smallest place on the right and carry any ten.",
           "Estimate first: the sum lies from the whole parts total up to that total plus 2."],
          items=[
              FIO("3.7.FiO1", "Figure it Out (adding and subtracting decimals), Q1",
                  "Find the sums: (a) 5.3 + 2.6 (b) 18 + 8.8 (c) 2.15 + 5.26 (d) 9.01 + 9.10 (e) 29.19 + 9.91 (f) "
                  "0.934 + 0.6 (g) 0.75 + 0.03 (h) 6.236 + 0.487",
                  ["(a) Tenths: 3 + 6 = 9. Units: 5 + 2 = 7. So 7.9.",
                   "(b) Write 18 as 18.0. Tenths: 0 + 8 = 8. Units: 8 + 8 = 16, so 26.8.",
                   "(c) Hundredths: 5 + 6 = 11, write 1 and carry 1. Tenths: 1 + 2 + 1 = 4. Units: 2 + 5 = 7. So 7.41.",
                   "(d) Hundredths: 1 + 0 = 1. Tenths: 0 + 1 = 1. Units: 9 + 9 = 18. So 18.11.",
                   "(e) Hundredths: 9 + 1 = 10, write 0 and carry 1. Tenths: 1 + 9 + 1 = 11, write 1 and carry 1. "
                   "Units: 9 + 9 + 1 = 19, write 9 and carry 1. Tens: 2 + 1 = 3 and 1. So 39.10.",
                   "(f) Write 0.6 as 0.600. Thousandths: 4. Hundredths: 3. Tenths: 9 + 6 = 15, write 5 and carry 1. "
                   "Units: 0 + 0 + 1 = 1. So 1.534.",
                   "(g) Write 0.03 as 0.03. Hundredths: 5 + 3 = 8. Tenths: 7. So 0.78.",
                   "(h) Thousandths: 6 + 7 = 13, write 3 and carry 1. Hundredths: 3 + 8 + 1 = 12, write 2 and "
                   "carry 1. Tenths: 2 + 4 + 1 = 7. Units: 6. So 6.723."],
                  "(a) 7.9 (b) 26.8 (c) 7.41 (d) 18.11 (e) 39.10 (f) 1.534 (g) 0.78 (h) 6.723",
                  tool="point_aligned_addition_column"),
              FIO("end.FiO7", "Figure it Out (end of chapter), Q7",
                  "Mahi purchases 0.25 kg of beans, 0.3 kg of carrots, 0.5 kg of potatoes, 0.2 kg of capsicums, and "
                  "0.05 kg of ginger. Calculate the total weight of the items she bought.",
                  ["Write each with two places: 0.25, 0.30, 0.50, 0.20 and 0.05.",
                   "Hundredths: 5 + 0 + 0 + 0 + 5 = 10, write 0 and carry 1 to the tenths.",
                   "Tenths: 2 + 3 + 5 + 2 + 1 carried = 13, write 3 and carry 1 to the units.",
                   "Units: 1. The total is 1.30 kg."],
                  "1.3 kg", tool="point_aligned_addition_column"),
              FIO("end.FiO15", "Figure it Out (end of chapter), Q15",
                  "Using each digit 0 to 9 not more than once, fill the boxes of a sum of two decimals, each with "
                  "one digit before the point and three digits after it, so that the sum is closest to 10.5.",
                  ["Each number is a digit, a point and three more digits, so eight different digits are used.",
                   "Aim for a sum of exactly 10.500. The thousandths digits must add to 10, and every other place "
                   "must add to make the right sum with a carry.",
                   "Try 0.643 + 9.857: thousandths 3 + 7 = 10, hundredths 4 + 5 + 1 = 10, tenths 6 + 8 + 1 = 15, "
                   "units 0 + 9 + 1 = 10.",
                   "The sum is 10.500 and the eight digits 0, 6, 4, 3, 9, 8, 5, 7 are all different, so the gap "
                   "from 10.5 is zero."],
                  "0.643 + 9.857 is exactly 10.500",
                  tool="point_aligned_addition_column")])]))

# ============================== T12 Subtracting decimals =====================================================
TOPICS.append(TOPIC(
    "T12", "M3", "Subtracting Decimals", ["3.7"], "Apply",
    "Students subtract decimals by lining up the points, filling the shorter number with zeroes and borrowing "
    "from the left, and estimate a difference before computing.",
    "Decimals are subtracted like whole numbers once the points are in one line and the shorter number is filled "
    "with zeroes; the whole number parts give a range for the difference.",
    [A("T12.C1", "Subtracting decimals place by place", "Apply",
       "Students subtract one decimal from another with the points lined up and with borrowing, in the compact "
       "form, and connect it to the place value working.",
       textbook=["How much longer is Shylaja’s cloth compared to Priya’s?",
                 "We have to find the difference of 3.5m − 2.7m. Again, observe how the differences 3 5/10 − 2 7/10 "
                 "and 3.5m − 2.7m are computed.",
                 "As you can see, the standard procedure for adding and subtracting whole numbers can be used to add "
                 "and subtract decimals.",
                 "Write the detailed place value computation for 84.691 − 77.345, and its compact form."],
       teach=["Predict first: 3.5 take away 2.7. There are 5 tenths and 7 must go. Where do the tenths come from?",
              "Break 1 unit into 10 tenths. Then subtract tenths, and then units, with the point kept in place.",
              "Do the same for 84.691 and 77.345, writing every borrow."],
       examples=[
           WE("Shylaja needs 3.5 m of cloth and Priya needs 2.7 m. How much longer is Shylaja's cloth? Compare with "
              "3 5/10 − 2 7/10.",
              ["Line up the points: 3.5 above 2.7.",
               "Tenths: 5 is less than 7, so borrow 1 unit from the 3. The 3 becomes 2 and the 5 tenths become 15 "
               "tenths.",
               "15 − 7 = 8 tenths. Units: 2 − 2 = 0. So the difference is 0.8.",
               "In fractions, 3 5/10 − 2 7/10 = 2 15/10 − 2 7/10 = 0 8/10, which is 0.8 again."],
              "0.8 m", ncert=["3.7.cloth_sub"]),
           WE("Find 84.691 − 77.345 in the place value form and in the compact form.",
              ["Line up the points: 84.691 above 77.345.",
               "Thousandths: 1 is less than 5, so borrow 1 hundredth: 11 − 5 = 6, and the hundredths 9 become 8.",
               "Hundredths: 8 − 4 = 4. Tenths: 6 − 3 = 3.",
               "Units: 4 is less than 7, so borrow 1 ten: 14 − 7 = 7, and the tens 8 become 7. Tens: 7 − 7 = 0.",
               "The difference is 7.346."],
              "7.346", ncert=["3.7.detail_sub"])],
       key_terms=["borrow"], misconceptions=["M_POINT_ALIGN", "M_BORROW_ONE"], minutes=10),
     A("T12.C2", "Estimating a difference first", "Analyze",
       "Students narrow down the whole numbers within which the difference of two decimals must lie, and use the "
       "range to check a difference.",
       textbook=["Similarly, come up with a way to narrow down the range of whole numbers within which the "
                 "difference of two decimals will lie.",
                 "Note to the Teacher: Estimating the result before computing may help in identifying if a mistake "
                 "happens with the calculation."],
       teach=["Predict first: for 8.9 minus 3.1, what is the least and what is the most the answer could be?",
              "Each decimal is its whole part plus a fraction under 1. The difference of the whole parts is the "
              "base, and the fractions can move it up or down by less than 1.",
              "So the difference lies between the whole parts difference minus 1 and the whole parts difference "
              "plus 1."],
       examples=[
           WE("Find a range for 84.691 − 77.345 and for 5.2 − 4.9, from the whole number parts, then check.",
              ["84.691 and 77.345 have whole parts 84 and 77, whose difference is 7. The range is from 6 to 8.",
               "The actual difference is 7.346, which lies between 6 and 8.",
               "5.2 and 4.9 have whole parts 5 and 4, whose difference is 1. The range is from 0 to 2.",
               "The actual difference is 0.3, which lies between 0 and 2.",
               "Each fractional part is under 1, so their difference is more than −1 and less than 1. That is why "
               "the range is the whole parts difference with 1 taken off and added."],
              "The difference lies between the whole parts difference minus 1 and plus 1: 7.346 is between 6 and 8, "
              "0.3 is between 0 and 2", ncert=["3.7.est_diff"])],
       key_terms=["range"], misconceptions=["M_EST_RANGE"], minutes=10),
     DOER("T12.C3", "Practice: subtract decimals with zeroes filled in", "zero_filled_subtraction_column", "Apply",
          "Students subtract decimals with the points lined up, zeroes filled in and borrowing, and check each "
          "difference against an estimate.",
          ["Line up the decimal points and fill the shorter number with zeroes on the right.",
           "Borrow from the next place on the left when a digit is too small.",
           "Estimate first: the difference lies within 1 of the whole parts difference."],
          items=[
              FIO("3.7.FiO2", "Figure it Out (adding and subtracting decimals), Q2",
                  "Find the differences: (a) 5.6 − 2.3 (b) 18 − 8.8 (c) 10.4 − 4.5 (d) 17 − 16.198 (e) 17 − 0.05 "
                  "(f) 34.505 − 18.1 (g) 9.9 − 9.09 (h) 6.236 − 0.487",
                  ["(a) Tenths: 6 − 3 = 3. Units: 5 − 2 = 3. So 3.3.",
                   "(b) Write 18 as 18.0. Tenths: borrow, 10 − 8 = 2. Units: 17 − 8 = 9. So 9.2.",
                   "(c) Tenths: borrow, 14 − 5 = 9. Units: 9 − 4 = 5. So 5.9.",
                   "(d) Write 17 as 17.000. 17.000 − 16.198: the thousandths, hundredths and tenths all borrow, "
                   "giving 0.802.",
                   "(e) Write 17 as 17.00. 17.00 − 0.05 = 16.95.",
                   "(f) Write 18.1 as 18.100. 34.505 − 18.100 = 16.405.",
                   "(g) Write 9.9 as 9.90. 9.90 − 9.09 = 0.81.",
                   "(h) 6.236 − 0.487: thousandths borrow, hundredths borrow, tenths borrow, giving 5.749."],
                  "(a) 3.3 (b) 9.2 (c) 5.9 (d) 0.802 (e) 16.95 (f) 16.405 (g) 0.81 (h) 5.749",
                  tool="zero_filled_subtraction_column"),
              FIO("end.FiO8", "Figure it Out (end of chapter), Q8",
                  "Pinto supplies 3.79 L, 4.2 L, and 4.25 L of milk to a milk dairy in the first three days. In 6 "
                  "days, he supplies 25 litres of milk. Find the total quantity of milk supplied to the dairy in the "
                  "last three days.",
                  ["First three days: 3.79 + 4.20 + 4.25. Hundredths: 9 + 0 + 5 = 14, write 4 and carry 1. Tenths: "
                   "7 + 2 + 2 + 1 = 12, write 2 and carry 1. Units: 3 + 4 + 4 + 1 = 12. The total is 12.24 L.",
                   "In 6 days he supplies 25 L, so the last three days are 25 − 12.24.",
                   "Write 25 as 25.00. 25.00 − 12.24 = 12.76."],
                  "12.76 L", tool="zero_filled_subtraction_column"),
              FIO("end.FiO9", "Figure it Out (end of chapter), Q9",
                  "Tinku weighed 35.75 kg in January and 34.50 kg in February. Has he gained or lost weight? How "
                  "much is the change?",
                  ["February's weight 34.50 is less than January's 35.75, so he lost weight.",
                   "The change is 35.75 − 34.50. Hundredths: 5 − 0 = 5. Tenths: 7 − 5 = 2. Units: 5 − 4 = 1.",
                   "The change is 1.25 kg."],
                  "He has lost weight, 1.25 kg", tool="zero_filled_subtraction_column")])]))

# ============================== T13 Decimal sequences ========================================================
TOPICS.append(TOPIC(
    "T13", "M3", "Decimal Sequences", ["3.7"], "Analyze",
    "Students find the constant change in a sequence of decimals, extend the sequence, and make sequences of "
    "their own.",
    "A decimal sequence changes by the same amount each time; subtract one term from the next to find the change "
    "and apply it again.",
    [A("T13.C1", "Finding the change and extending a decimal sequence", "Analyze",
       "Students find the change between terms of a decimal sequence, add or subtract it to extend the sequence, "
       "and invent sequences for others to extend.",
       textbook=["Decimal Sequences",
                 "Observe this sequence of decimal numbers and identify the change after each term. 4.4, 4.8. 5.2, "
                 "5.6, 6.0, …",
                 "We can see that 0.4 is being added to a term to get the next term. Continue this sequence and "
                 "write the next 3 terms.",
                 "Similarly, identify the change and write the next 3 terms for each sequence given below. Try to do "
                 "this computation mentally. (a) 4.4, 4.45, 4.5, … (b) 25.75, 26.25, 26.75, … (c) 10.56, 10.67, "
                 "10.78, … (d) 13.5, 16, 18.5, … (e) 8.5, 9.4, 10.3, … (f) 5, 4.95, 4.90, … (g) 12.45, 11.95, "
                 "11.45, … (h) 36.5, 33, 29.5, …",
                 "Make your own sequences and challenge your classmates to extend the pattern."],
       teach=["Predict first: in 4.4, 4.8, 5.2 the terms grow. By how much each time?",
              "Subtract one term from the next. If the answer is the same each time, that is the change.",
              "Add the change to get on, or subtract it if the terms fall.",
              "Then make your own sequence, hide the next terms and challenge a classmate."],
       examples=[
           WE("Find the change in 4.4, 4.8, 5.2, 5.6, 6.0 and write the next 3 terms.",
              ["4.8 − 4.4 = 0.4, and 5.2 − 4.8 = 0.4, so 0.4 is added each time.",
               "6.0 + 0.4 = 6.4. 6.4 + 0.4 = 6.8. 6.8 + 0.4 = 7.2."],
              "6.4, 6.8, 7.2", ncert=["3.7.seq_try"]),
           WE("Find the change and the next 3 terms: (a) 4.4, 4.45, 4.5 (b) 25.75, 26.25, 26.75 (c) 10.56, 10.67, "
              "10.78 (d) 13.5, 16, 18.5 (e) 8.5, 9.4, 10.3 (f) 5, 4.95, 4.90 (g) 12.45, 11.95, 11.45 (h) 36.5, "
              "33, 29.5.",
              ["(a) Add 0.05 each time: 4.55, 4.60, 4.65.",
               "(b) Add 0.5 each time: 27.25, 27.75, 28.25.",
               "(c) Add 0.11 each time: 10.89, 11.00, 11.11.",
               "(d) Add 2.5 each time: 21.0, 23.5, 26.0.",
               "(e) Add 0.9 each time: 11.2, 12.1, 13.0.",
               "(f) Subtract 0.05 each time: 4.85, 4.80, 4.75.",
               "(g) Subtract 0.5 each time: 10.95, 10.45, 9.95.",
               "(h) Subtract 3.5 each time: 26.0, 22.5, 19.0."],
              "(a) +0.05: 4.55, 4.60, 4.65 (b) +0.5: 27.25, 27.75, 28.25 (c) +0.11: 10.89, 11.00, 11.11 (d) +2.5: "
              "21.0, 23.5, 26.0 (e) +0.9: 11.2, 12.1, 13.0 (f) −0.05: 4.85, 4.80, 4.75 (g) −0.5: 10.95, 10.45, "
              "9.95 (h) −3.5: 26.0, 22.5, 19.0", ncert=["3.7.seq_more", "3.7.seq_own"])],
       key_terms=["sequence", "change"], misconceptions=["M_BORROW_ONE"], minutes=10),
     DOER("T13.C2", "Practice: extend a decimal pattern", None, "Analyze",
          "Students find the rule of a decimal pattern, including one that alternates between two changes, and "
          "extend it.",
          ["Subtract one term from the next to find the change.",
           "A pattern can alternate between two changes, so check more than one step.",
           "Test your rule on every pair of terms."],
          items=[
              FIO("end.FiO10", "Figure it Out (end of chapter), Q10",
                  "Extend the pattern: 5.5, 6.4, 6.39, 7.29, 7.28, 8.18, 8.17, ____, ____",
                  ["6.4 − 5.5 = 0.9, so the first change is plus 0.9.",
                   "6.39 is 0.01 less than 6.4, so the next change is minus 0.01.",
                   "7.29 − 6.39 = 0.9 and 7.28 is 0.01 less than 7.29, so the changes alternate: plus 0.9, minus "
                   "0.01, plus 0.9, minus 0.01.",
                   "The last term shown is 8.17 after a minus 0.01, so the next change is plus 0.9: 9.07.",
                   "Then minus 0.01 gives 9.06."],
                  "9.07, 9.06")])]))

# ============================== T14 Decimal mix-ups ==========================================================
TOPICS.append(TOPIC(
    "T14", "M4", "Decimal Mix-ups in Everyday Life", ["3.8"], "Evaluate",
    "Students explain how misplaced decimal points and unit slips cause real problems, and read time, feet and "
    "overs that only look like decimals.",
    "A misplaced decimal point or a mixed unit can change a quantity by 10 or 100 times; some numbers that look "
    "decimal, such as hours, feet and overs, are not.",
    [A("T14.C1", "Decimal and measurement disasters", "Evaluate",
       "Students explain how a decimal point or a unit slip caused an Amsterdam payment error, a fuel shortage and a "
       "medicine error, and how big each error was.",
       textbook=["3.8 More on the Decimal System",
                 "Decimal and Measurement Disasters",
                 "Decimal point and unit conversion mistakes may seem minor sometimes but they can lead to serious "
                 "problems. Here are some actual incidents in which such errors caused major issues.",
                 "In 2013, the finance office of Amsterdam City Council (Netherlands) mistakenly sent out €188 "
                 "million in housing benefits instead of the intended €1.8 million due to a programming error that "
                 "processed payments in euro cents instead of euros. (1 euro-cent = 1/100 euro).",
                 "In 1983, a decimal error nearly caused a disaster for an Air Canada Boeing 767. The ground staff "
                 "miscalculated the fuel, loading 22,300 pounds instead of kilograms, about half of what was needed "
                 "(1 pound ~ 0.453 kg). The plane ran out of fuel mid-air, forcing the pilots to make an "
                 "emergency landing at an abandoned airfield. Fortunately, everyone survived.",
                 "Several incidents have occurred due to incorrect reading of decimal numbers while giving "
                 "medication. For example, reading 0.05 mg as 0.5 mg can lead to using a medicine 10 times more than "
                 "the prescribed quantity. It is therefore important to pay attention to units and the location of "
                 "the decimal point."],
       teach=["Predict first: if a payment is made in euro cents when euros were meant, is the amount sent more "
              "or less than meant, and by how many times?",
              "A euro-cent is a hundredth of a euro, so a count of cents read as euros is 100 times too big.",
              "In the same way, 22300 pounds is less than half of what 22300 kilograms would be, since a pound "
              "is only about 0.453 kg."],
       examples=[
           WE("In 2013 a council meant to send 1.8 million euros but sent 188 million euros, because payments were "
              "processed in euro cents instead of euros. How many times larger was the amount sent? Also, why is "
              "0.05 mg read as 0.5 mg a serious error?",
              ["188 million divided by 1.8 million is about 104, so roughly 100 times larger. That matches the "
               "slip between cents and euros, where one euro-cent is 1/100 euro.",
               "0.05 mg is 5 hundredths of a mg. 0.5 mg is 5 tenths of a mg.",
               "5 tenths is 10 times 5 hundredths, so reading 0.05 as 0.5 gives a dose 10 times too big.",
               "Always check the unit and the place of the decimal point."],
              "About 100 times larger; the medicine dose would be 10 times larger", ncert=["3.8.disasters"]),
           WE("A ground crew loaded 22300 pounds of fuel when 22300 kilograms was needed, and 1 pound is about "
              "0.453 kg. About how many kilograms was loaded, and how does it compare with what was needed?",
              ["22300 × 0.453 is about 10102 kg, found by multiplying the pounds by 0.453.",
               "What was needed was 22300 kg.",
               "10102 is a little less than half of 22300, so the plane carried about half of the fuel it "
               "needed.",
               "The unit slip, pounds for kilograms, is the same kind of error as a decimal slip."],
              "About 10102 kg, about half of what was needed", ncert=["3.8.fuel"])],
       key_terms=["unit conversion"], misconceptions=["M_UNIT_SHIFT"], minutes=10),
     A("T14.C2", "Numbers that look decimal but are not", "Evaluate",
       "Students read 4.5 hours, 2.5 feet and 5.5 overs correctly, and give other examples of decimal-like "
       "numbers that are not decimals.",
       textbook=["Deceptive Decimal Notation",
                 "Sarayu gets a message: “The bus will reach the station 4.5 hours post noon.” When will the bus "
                 "reach the station: 4:05 p.m., 4:50 p.m., 4:25 p.m.?",
                 "None of these! Here, 0.5 hours means splitting an hour into 10 equal parts and taking 5 parts out "
                 "of it. Each part will be 6 minutes (60 minutes/10) long. 5 such parts make 30 minutes. So, the bus "
                 "will reach the station at 4:30.",
                 "Here is a short-story of a decimal mishap: A girl measures the width of an opening as 2 ft 5 inches "
                 "but conveys to the carpenter to make a door 2.5 ft wide. The carpenter makes a door of width 2 ft "
                 "6 inches (since 1 ft = 12 inches, 0.5 ft = 6 inches), and it wouldn’t close fully.",
                 "If you watch cricket, you might have noticed decimal-looking numbers like ‘Overs left: 5.5’. Does "
                 "this mean 5 overs and 5 balls or 5 overs and 3 balls? Here, 5.5 overs means 5 5/6 overs (as 1 over = "
                 "6 balls), i.e., 5 overs and 5 balls.",
                 "Where else can we see such ‘non-decimals’ with a decimal-like notation?"],
       teach=["Predict first: the bus will arrive 4.5 hours after noon. Is it 4:05, 4:25, 4:30 or 4:50?",
              "0.5 hours is 5 of 10 equal parts of an hour, and each part is 6 minutes, so 30 minutes: 4:30.",
              "Feet are 12 inches, not 10, and overs are 6 balls, not 10. So 2.5 ft and 5.5 overs do not follow the "
              "tenths rule.",
              "Look for other places where a point is used between two numbers that are not a decimal, such as "
              "a time written as hours and minutes."],
       examples=[
           WE("A message says the bus reaches at 4.5 hours post noon. When does it arrive? Then, a door was "
              "ordered 2.5 ft wide when the opening was 2 ft 5 inches. How wide did the carpenter make it?",
              ["0.5 hours is 5 parts out of 10 equal parts of an hour. Each part is 60 ÷ 10 = 6 minutes.",
               "5 parts make 5 × 6 = 30 minutes, so the bus arrives at 4:30 p.m.",
               "A foot is 12 inches, so 0.5 ft is half of 12 inches, that is 6 inches.",
               "The carpenter made a door 2 ft 6 inches wide, 1 inch too wide for the opening, so it would not "
               "close fully."],
              "4:30 p.m.; the door was 2 ft 6 inches, 1 inch too wide", ncert=["3.8.bus", "3.8.door"]),
           WE("A scoreboard shows 'Overs left: 5.5'. How many overs and balls is that? Then name other places where "
              "a point is used but the number is not a decimal.",
              ["An over has 6 balls, so one ball is 1/6 of an over.",
               "5.5 overs means 5 5/6 overs, that is 5 overs and 5 balls, not 5 overs and 3 balls.",
               "Other examples: a time written as 2.30 for 2 hours 30 minutes, a height of 5.11 for 5 feet 11 "
               "inches, a date written as 2.10 for the second of October, or version numbers such as 1.10 of an app."],
              "5 5/6 overs, that is 5 overs and 5 balls", ncert=["3.8.overs", "3.8.nondecimals"])],
       key_terms=["overs"], misconceptions=["M_TIME_DECIMAL"], minutes=10),
     DOER("T14.C3", "Practice: spot the decimal mix-up", None, "Evaluate",
          "Students explain how a misplaced decimal point or a unit slip changes a quantity, and read decimal-like "
          "numbers of time, feet and overs correctly.",
          ["Check the unit and the place of the decimal point before using a number.",
           "A number with a point is a decimal only if each place is worth ten times the next.",
           "Hours, feet and overs are not counted in tens."])]))

# ============================== T15 A pinch of history =======================================================
TOPICS.append(TOPIC(
    "T15", "M4", "A Pinch of History: Decimal Notation Over Time", ["3.8"], "Understand",
    "Students describe how decimal fractions and decimal notation were used in India and by al-Uqlidisi, the "
    "notations of the 15th century, and the point and the comma of the 16th century.",
    "Decimal fractions were used in ancient India, modern decimal notation was written down around 950 CE, and "
    "the point became the most popular separator in the Indian place value system.",
    [A("T15.C1", "From India to the first decimal notation", "Understand",
       "Students tell where decimal fractions first appear in the work of ancient Indian mathematicians, who "
       "described modern decimal notation around 950 CE, and what the 15th century notations looked like.",
       textbook=["A Pinch of History: Decimal Notation Over Time",
                 "Decimal fractions (i.e., fractions with denominators like 1/10, 1/100, 1/1000, and so on) are used "
                 "in the works of a number of ancient Indian astronomers and mathematicians, including in the "
                 "important 8th century works of Śhrīdharāchārya on arithmetic and algebra.",
                 "Decimal notation, in essentially its modern form, was described in detail in Kitāb al-Fuṣūl fī "
                 "al-Ḥisāb al Hindī (The Book of Chapters on Indian Arithmetic) by Abūl Ḥassan al-Uqlīdisī, an "
                 "Arab mathematician, in around 950 CE. He represented the number 0.059375 with a small vertical "
                 "mark placed after the zero that is the whole number part.",
                 "In the 15th century, to separate whole numbers from fractional parts, a number of different "
                 "notations were used: a vertical mark on the last digit of the whole number part (as shown "
                 "above), use of different colours and a numerical superscript giving the number of fractional "
                 "decimal places (0.36 would be written as the digits 36 with a small 2 above them)."],
       teach=["Predict first: which came earlier, the idea of tenths and hundredths, or the decimal point we use?",
              "Fractions with denominators 10, 100 and 1000 were used by ancient Indian astronomers and "
              "mathematicians, including Shridharacharya in the 8th century.",
              "Around 950 CE al-Uqlidisi described decimal notation in its modern form. By the 15th century people "
              "marked the whole part with a vertical mark, with colours, or with a small number telling how many "
              "decimal places there are."],
       examples=[
           WE("Order these events from earliest to latest: the 8th century works of Shridharacharya, the book of "
              "al-Uqlidisi around 950 CE, the 15th century notations, and the use of the point in the 16th "
              "century.",
              ["The 8th century is the 700s.",
               "950 CE is in the 900s, so it comes after the 8th century.",
               "The 15th century is the 1400s, and the 16th century is the 1500s.",
               "So the order is Shridharacharya, al-Uqlidisi, the 15th century marks, and the 16th century point."],
              "8th century, about 950 CE, 15th century, 16th century", ncert=["3.8.history_india"])],
       key_terms=["decimal fraction"], misconceptions=[], minutes=8),
     A("T15.C2", "The point and the comma", "Understand",
       "Students explain how the point and the comma were used in the 16th century, and how some countries today "
       "write one thousand and five tenths.",
       textbook=["In the 16th century, John Napier, a Scottish mathematician, and Christopher Clavius, a German "
                 "mathematician, used the point/period (‘.’) to separate the whole number and the fractional parts, "
                 "while François Viète, a French mathematician, used the comma (‘,’) instead.",
                 "Currently, several countries use the comma to separate the integer part and the fractional part. "
                 "In these countries, the number 1,000.5 is written with a space after the 1 and a comma before the "
                 "5 (space as a thousand separator). But the decimal point has endured as the most popular notation "
                 "for writing numbers having fractional parts in the Indian place value system."],
       teach=["Predict first: if one country uses a point and another a comma to split the whole part from the "
              "fraction, can the same figure be misread?",
              "In the 16th century Napier and Clavius used the point, and Viete used the comma.",
              "Today several countries use the comma. There, one thousand and five tenths has a space after the 1 "
              "and a comma before the 5. But the point is the most popular in the Indian place value system."],
       examples=[
           WE("In a country that uses the comma, how would a number such as one thousand and five tenths be "
              "written, and why is it important to know which notation is in use?",
              ["In the point notation it is 1,000.5, with a comma between thousands and a point before the tenths.",
               "In the comma notation the space takes the thousand separator's place and the comma becomes the "
               "decimal mark, so it reads 1 000,5.",
               "A reader who does not know which notation is used could take the comma as a thousand separator and "
               "misread the number, so check the notation first."],
              "1 000,5 in the comma notation, and the notation must be checked", ncert=["3.8.history_point_comma"])],
       key_terms=["decimal separator"], misconceptions=[], minutes=8),
     DOER("T15.C3", "Practice: place the notations in time", None, "Understand",
          "Students place the early uses of decimal fractions and decimal notation in order and say how the point and "
          "the comma differ.",
          ["Decimal fractions appear in ancient India; modern decimal notation was written down around 950 CE.",
           "The 16th century brought the point and the comma.",
           "The point is the most popular separator in the Indian place value system."])]))

# ============================== T16 Summary ==================================================================
TOPICS.append(TOPIC(
    "T16", "M4", "Chapter Summary", ["3.8"], "Understand",
    "",
    "Smaller units give exact measures; the place value system extends to the right of the units; decimals can be "
    "compared, located, added and subtracted.",
    [A("T16.C1", "Putting the chapter together", "Understand",
       "",
       textbook=["SUMMARY",
                 "We can split a unit into smaller parts to get more exact/accurate measurements.",
                 "We extended the Indian place value system and saw that 1 unit = 10 one-tenths, 1 tenth = 10 "
                 "one-hundredths, 1 hundredth = 10 one-thousandths, 10 one-hundredths = 1 tenth, 100 "
                 "one-hundredths = 1 unit.",
                 "A decimal point (‘.’) is used in the Indian place value system to separate the whole number part "
                 "of a number from its fractional part.",
                 "We also learnt how to compare decimal numbers, locate them on the number line, and perform "
                 "addition and subtraction on them."],
       teach=["Look back at the screws: a very small gap needed a very small unit, and a new way of writing it.",
              "Tenths, hundredths and thousandths continue the place value ladder to the right of the units, and "
              "the decimal point marks where the units end.",
              "Decimals are compared place by place, located by zooming, and added or subtracted with the points "
              "in one line."],
       ncert=["summary"], video_focus=["RECAP"], enrichment=True)],
    topic_type="summary"))
