# -*- coding: utf-8 -*-
"""Topics T1 to T5 (module M1: the balancing act, mean and median). Book section 5.1, pp 103 to 115."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Where is the centre? =====================================================
TOPICS.append(TOPIC(
    "T1", "M1", "Where Is the Centre?", ["Chapter opening", "5.1"], "Understand",
    "",
    "Two numbers, their mean, and the question that drives the chapter: where is the centre of some data?",
    [A("T1.C1", "The mean of two numbers sits halfway", "Remember",
       "",
       textbook=["5.1 The Balancing Act",
                 "Last year, we learnt about the mean and median. Recall that the mean of some data is the sum of all "
                 "the values divided by the number of values in the data. The median is the middle value when the "
                 "data is sorted.",
                 "We shall try to understand the mean and median from a different perspective and see how the mean "
                 "behaves with changing data.",
                 "Consider any 2 numbers. Find their average/arithmetic mean. Repeat this by taking other pairs. "
                 "What do you observe?",
                 "For example, let the two numbers be 3 and 7. Their average is (3 + 7) ÷ 2 = 5. Taking another pair "
                 "of numbers, say 8 and 9, their average is (8 + 9) ÷ 2 = 8.5. Visualising these as dot plots we get "
                 "the picture. Notice that the mean is exactly halfway between the two numbers."],
       teach=["Predict first: put a dot on 3 and a dot on 7 on a number line. Where would you put a finger so the "
              "two dots balance?",
              "The mean of 3 and 7 is 5, exactly halfway. For 8 and 9 it is 8.5, again halfway.",
              "For two numbers the mean is the centre. Is that still true when there are three numbers, or four?"],
       ncert=["opening", "5.1.pairs"], key_terms=["mean", "centre"], video_focus=["HOOK"], minutes=4,
       enrichment=True)],
    topic_type="framing"))

# ============================== T2 The balancing act: mean as centre and how it changes =====================
TOPICS.append(TOPIC(
    "T2", "M1", "The Balancing Act: How the Mean Changes", ["5.1"], "Analyze",
    "Students show that the mean is the balance point where distances to the left and right are equal and that "
    "there is only one such centre. They predict how adding, removing, shifting or multiplying every value moves "
    "the mean, and prove the shift and multiply rules with algebra.",
    "The mean balances the distances on both sides, a new value above it pulls it up, a value below pulls it down, "
    "adding k to every value adds k to the mean, and multiplying every value by k multiplies the mean by k.",
    [A("T2.C1", "The mean as the balance point", "Analyze",
       "Students mark the mean of a dot plot, verify that the total distance to values on the left equals the total "
       "on the right, and explain why a second centre cannot exist.",
       textbook=["Calculate and mark the mean of each collection of data below.",
                 "Can you explain how the mean is the centre of each collection?",
                 "Is the mean the midpoint of the two endpoints/extremes of the data? It is not always so. Instead, "
                 "the total distances are equal on both the sides of the mean.",
                 "Verify that this holds for all the collections of data shown earlier.",
                 "Can there be more than one such centre? In other words, is there any other value such that the sum "
                 "of the distances to the values lower than it and the values higher than it will still be equal?",
                 "In the case of the collection 10, 10, 11, and 17 whose mean is 12, suppose there is a different "
                 "centre larger than 12. Clearly, all the distances on the LHS will increase and the distances on the "
                 "RHS will decrease. Thus, it is no longer the centre. Similarly, for any value smaller than 12, the "
                 "distances on the LHS will decrease while those on the RHS will increase.",
                 "Therefore, there is only one centre."],
       teach=["Predict first: for 10, 10, 11 and 17, is the mean the midpoint of 10 and 17? Check it before reading on.",
              "The mean is 12, but the midpoint of 10 and 17 is 13.5. So the mean is not the midpoint of the "
              "extremes. What it balances is distance.",
              "Distances to the left of 12 add to 2 + 2 + 1 = 5. The distance to the right is 17 − 12 = 5. Equal.",
              "Move the finger to 13: the left distances grow, the right distance shrinks, no balance. Move to 11: "
              "the opposite. Only 12 balances, so there is only one centre."],
       examples=[
           WE("Show that the mean of 10, 10, 11 and 17 balances the distances, and that 13 does not.",
              ["The mean is (10 + 10 + 11 + 17) ÷ 4 = 48 ÷ 4 = 12.",
               "Left of 12: 2 + 2 + 1 = 5. Right of 12: 17 − 12 = 5. They are equal.",
               "Try 13. Left of 13: 3 + 3 + 2 = 8. Right of 13: 17 − 13 = 4. Not equal.",
               "Try 11. Left of 11: 1 + 1 + 0 = 2. Right of 11: 6 + 0 = 6. Not equal."],
              "Only 12 balances the distances; 13 and 11 do not",
              ncert=["5.1.mt_distances", "5.1.mt_one_centre"])],
       key_terms=["mean", "balance", "distance"], misconceptions=["M_MID_ENDS", "M_MEAN_DATA"], minutes=10),
     A("T2.C1x", "Is the centre of 2, 6, 10 and 12 a whole number?", "Apply",
       "Students find the mean of a second collection that is not a whole number and check that the distances "
       "to the values on its left and right still add to the same total.",
       teach=["Predict first: will the centre of 2, 6, 10 and 12 land on one of the dots, or between them?",
              "The mean is 7.5, between the dots, and the distances on each side add to 7."],
       examples=[
           WE("Find the mean of 2, 6, 10 and 12 and check the balance.",
              ["The mean is (2 + 6 + 10 + 12) ÷ 4 = 30 ÷ 4 = 7.5.",
               "Left of 7.5: 5.5 + 1.5 = 7. Right of 7.5: 2.5 + 4.5 = 7.",
               "The two sides are equal, so 7.5 is the centre."],
              "The mean is 7.5 and the distances on both sides add to 7",
              ncert=["5.1.three_collections", "5.1.centre_explain"])],
       key_terms=["mean", "balance", "distance"], misconceptions=["M_MEAN_DATA"], minutes=6, thin=True),
     A("T2.C2", "A value added, removed or kept: the mean moves", "Analyze",
       "Students predict whether the mean rises, falls or stays when one value is added or removed, and find pairs "
       "or triples of values that leave the mean unchanged.",
       textbook=["Will including a new value in the data increase or decrease the mean?",
                 "When a new value greater than the mean is included, the mean increases to maintain the balance "
                 "between the sum of distances on the LHS and RHS. Similarly, if a value smaller than the mean is "
                 "included, then the new mean will be less than before.",
                 "What happens to the mean when an existing value is removed? When will the mean increase, decrease, "
                 "or stay the same? What happens to the mean if a value equal to the mean is included or removed? "
                 "Try to explain this using the fair-share interpretation of mean that we studied last year.",
                 "Unchanging Mean! Explore if it is possible to include or remove 2 values such that the mean is "
                 "unchanged.",
                 "How about including or removing 3 values without changing the mean? Is it possible? Can we include "
                 "2 values less than the mean and 1 value greater than the mean, so that the mean remains the same?",
                 "Try to include 2 values greater than the mean and 1 value less than the mean, so that the mean "
                 "stays the same."],
       teach=["Predict first: the data 5, 5, 10, 24 has mean 11. A new value 17 is added. Up, down or same?",
              "17 is greater than 11, so the mean rises: (5 + 5 + 10 + 24 + 17) ÷ 5 = 61 ÷ 5 = 12.2.",
              "A value equal to the mean changes nothing, because it adds no distance on either side. Fair share "
              "view: a person who already holds the average share leaves every share as it was.",
              "To keep the mean fixed, the surplus distance of the values above must equal the deficit of the values "
              "below. Two values each 3 above and below the mean cancel; so do one value 4 below and two values 2 above."],
       examples=[
           WE("The data 5, 5, 10, 24 has mean 11. Find the new mean after including 17.",
              ["Sum of the data = 5 + 5 + 10 + 24 = 44, and 44 ÷ 4 = 11.",
               "New sum = 44 + 17 = 61, with 5 values.", "New mean = 61 ÷ 5 = 12.2.",
               "17 is above 11, so the mean moved up, as predicted."],
              "The new mean is 12.2, higher than 11", ncert=["5.1.new_value"])],
       key_terms=["mean", "included", "removed", "unchanged"], misconceptions=["M_ADD_NO_CHANGE"], minutes=10),
     A("T2.C2x", "Two new values that leave the mean unchanged", "Apply",
       "Students choose two values, one below and one above the mean by the same amount, include them in the "
       "data, and check that the mean stays exactly the same.",
       teach=["Predict first: if one value 4 below the mean and one 4 above join, does the mean move?",
              "The deficit below and the surplus above cancel, so the mean stays where it was."],
       examples=[
           WE("The data 5, 5, 10, 24 has mean 11. Include 2 values, one 4 below 11 and one 4 above, "
              "and check the mean is unchanged.",
              ["The new values are 7 and 15.", "New sum = 44 + 7 + 15 = 66, with 6 values.",
               "New mean = 66 ÷ 6 = 11.", "The deficit 4 and the surplus 4 cancel."],
              "The mean stays 11", ncert=["5.1.unchanged2", "5.1.remove_value", "5.1.mt_fair_share"])],
       key_terms=["mean", "unchanged", "included"], misconceptions=["M_ADD_NO_CHANGE"], minutes=6, thin=True),
     A("T2.C3", "Every value shifted or multiplied", "Apply",
       "Students predict and prove that adding a fixed number to every value adds it to the mean, subtracting "
       "subtracts it, and multiplying every value multiplies the mean by that number.",
       textbook=["What happens to the mean if every value in the collection increases by some fixed number?",
                 "Consider the data: 8, 3, 10, 13, 4, 6, 7, 7, 8, 8, 5. Calculate its mean. Now, consider this data "
                 "with every value increased by 10: 18, 13, 20, 23, 14, 16, 17, 17, 18, 18, 15. What is its mean? "
                 "Is there a quicker way to find out?",
                 "The mean of the new collection also increases by 10. Notice that the relative position of the "
                 "mean stays the same.",
                 "Suppose there are n values in the collection, x1, x2, x3, … xn. Their average is a. When a fixed "
                 "number, for example, 3 is added to every value, the new average is a + 3.",
                 "Try to explain, using algebra, what the average is when a fixed number, e.g., 2 is subtracted from "
                 "every value in the collection. Try to explain this using the fair-share interpretation of average.",
                 "What happens to the average if every value in the collection is doubled? The average also doubles.",
                 "When a fixed number, for example, 5 is multiplied to every value, the new average is 5a."],
       teach=["Predict first: every value in 8, 3, 10, 13, 4, 6, 7, 7, 8, 8, 5 goes up by 10. Do you have to add all "
              "eleven values again to get the new mean?",
              "The sum of the 11 values is 79, so the mean is 79 ÷ 11 ≈ 7.18. Every dot slides 10 to the right, so the "
              "mean slides 10 too: about 17.18. Its position among the dots does not change.",
              "Algebra: the new sum is x1 + x2 + … + xn + 3n, and dividing by n gives a + 3.",
              "Multiplying: each value becomes 5 times larger, the sum becomes 5 times larger, so the mean becomes 5a."],
       examples=[
           WE("The data 8, 3, 10, 13, 4, 6, 7, 7, 8, 8, 5 has 11 values. Find its mean, then the mean when every "
              "value is increased by 10, and when every value is doubled.",
              ["The sum is 8 + 3 + 10 + 13 + 4 + 6 + 7 + 7 + 8 + 8 + 5 = 79.", "The mean is 79 ÷ 11 ≈ 7.18.",
               "Every value plus 10: the mean is 7.18 + 10 = 17.18.",
               "Every value minus 1: the mean is 7.18 − 1 = 6.18.",
               "Every value doubled: the mean is 2 × 7.18 = 14.36."],
              "About 7.18, then 17.18 after adding 10, 6.18 after subtracting 1, and 14.36 after doubling",
              ncert=["5.1.add_k", "5.1.multiply_k"])],
       key_terms=["shift", "multiply", "algebra"], misconceptions=["M_SHIFT_MEDIAN_ONLY", "M_DOUBLE_ADD"], minutes=12),
     A("T2.C3x", "Subtract 2 from every value: the algebra", "Analyze",
       "Students write the sum of n values with mean a, subtract 2 from each value, and show with algebra that "
       "the new mean is exactly a minus 2.",
       teach=["Predict first: if 2 comes off every value, does the mean drop by 2, or by 2 times the number of values?",
              "Each value loses 2, so the sum loses 2n, and dividing by n takes exactly 2 off the mean."],
       examples=[
           WE("Use algebra to show what happens to the mean when 2 is subtracted from every one of n values whose "
              "mean is a.",
              ["The values are x1, x2, … xn, and (x1 + x2 + … + xn) ÷ n = a.",
               "The new sum is (x1 − 2) + (x2 − 2) + … + (xn − 2) = x1 + x2 + … + xn − 2n.",
               "Dividing by n gives a − 2."],
              "The new mean is a − 2", ncert=["5.1.try_subtract", "5.1.try_fair_share_shift", "5.1.try_two_greater",
                                              "5.1.unchanged3"])],
       key_terms=["shift", "algebra", "mean"], misconceptions=["M_DOUBLE_ADD"], minutes=6, thin=True),
     DOER("T2.C4", "Practice: move the dots, watch the mean", "data_explorer", "Analyze",
          "Students drag dots, add and remove values, and shift or scale the whole data on a dot plot, predicting "
          "each time where the mean will land and checking the balance of distances.",
          ["The mean is the one point where the distances on the two sides are equal.",
           "A new value above the mean raises it, below lowers it, equal leaves it.",
           "Adding k to every value adds k to the mean; multiplying by k multiplies the mean by k."],
          items=[
              FIO("FiO1.q1", "Figure it Out (mean and median, question 1)",
                  "Find the mean of the following data and share your observations: (i) The first 50 natural "
                  "numbers. (ii) The first 50 odd numbers. (iii) The first 50 multiples of 4.",
                  ["(i) The sum is 50 × 51 ÷ 2 = 1275, so the mean is 1275 ÷ 50 = 25.5.",
                   "(ii) The first 50 odd numbers add to 50 × 50 = 2500, so the mean is 2500 ÷ 50 = 50.",
                   "(iii) These are 4 times the natural numbers, so the mean is 4 × 25.5 = 102.",
                   "Observation: for evenly spaced values the mean is the average of the first and the last value."],
                  "(i) 25.5 (ii) 50 (iii) 102", expect=[25.5, 50, 102]),
              FIO("FiO1.q2", "Figure it Out (mean and median, question 2)",
                  "The dot plot shows a collection of data and its average; but one dot is missing. Mark the missing "
                  "value so that the mean is 9. The ten dots shown are at 4, 7, 8, 8, 9, 9, 9, 9, 9 and 11.",
                  ["Count the dots shown: 10 values, and the missing one makes 11 values.",
                   "For mean 9 the total must be 9 × 11 = 99.",
                   "The shown values add to 83, so the missing value is 99 − 83 = 16.",
                   "Check with distances: the dots below 9 are 5 + 2 + 1 + 1 = 9 away in total, and those above are "
                   "2 + 7 = 9 away."],
                  "The missing dot is at 16"),
              FIO("FiO1.q3", "Figure it Out (mean and median, question 3)",
                  "Shreyas measures the heights of all 24 students and finds an average of 150.2 cm. The students "
                  "wore uniform shoes that add 1 cm to the height. (i) Must the heights be measured again without "
                  "shoes? (ii) What is the correct average height?",
                  ["(i) No. Every height is exactly 1 cm too large, so every value is shifted by the same amount.",
                   "(ii) The mean shifts by the same amount: 150.2 − 1 = 149.2."],
                  "No need to measure again; the correct average is 149.2 cm, option (d)", expect=149.2),
              FIO("FiO1.q4", "Figure it Out (mean and median, question 4)",
                  "Three dot plots show lengths in minutes of songs in albums A, B and C. Which has a mean of 5.57 "
                  "minutes? Explain how you arrived at the answer.",
                  ["Album A has songs of 5, 5, 5.25, 5.5, 5.75, 6 and 6.5 minutes, which add to 39.",
                   "39 ÷ 7 ≈ 5.57, so A has a mean of 5.57.",
                   "Albums B and C have most of their dots below 5, so their means fall well under 5.57."],
                  "Album A"),
              FIO("FiO3.q1", "Figure it Out (more on mean and median, question 1)",
                  "Mean grids: (i) Fill a 3 by 3 grid with 9 distinct numbers so that the average along each row, "
                  "column and diagonal is 10. (ii) Can we fill the grid by changing a few numbers and still get 10 "
                  "as the average in all directions?",
                  ["An average of 10 over 3 numbers means each line adds to 30.",
                   "Start from the magic square 2, 7, 6 / 9, 5, 1 / 4, 3, 8 whose lines add to 15 and add 5 to every "
                   "value. This shifts every line total by 15.",
                   "The grid is 7, 12, 11 / 14, 10, 6 / 9, 8, 13. Each row, column and both diagonals add to 30.",
                   "(ii) Yes. Swapping the grid across its main diagonal changes six cells and still gives 30 in "
                   "every direction."],
                  "7, 12, 11 / 14, 10, 6 / 9, 8, 13 works; yes, other grids also work"),
              FIO("FiO3.q5", "Figure it Out (more on mean and median, question 5)",
                  "Check whether each statement is true and justify it, using algebra if needed: (i) The average of "
                  "two even numbers is even. (ii) The average of any two multiples of 5 is a multiple of 5. "
                  "(iii) The average of any 5 multiples of 5 is also a multiple of 5.",
                  ["(i) Write the numbers as 2a and 2b. Their average is a + b, which can be odd. 2 and 4 give 3. False.",
                   "(ii) Write them as 5a and 5b. The average is 5(a + b) ÷ 2, which is not always a multiple of 5. "
                   "5 and 10 give 7.5. False.",
                   "(iii) The average of 5a, 5b, 5c, 5d, 5e is a + b + c + d + e, which need not be a multiple of 5. "
                   "5, 5, 5, 5, 10 give 6. False."],
                  "All three statements are false"),
              FIO("FiO3.q7", "Figure it Out (more on mean and median, question 7)",
                  "Is 17 the average of the data in the dot plot? The dot plot has 2 dots at 14, 2 at 15, 3 at 16, "
                  "5 at 17, 4 at 18, 4 at 19, 3 at 20, 1 at 21 and 1 at 23. Share the method you used.",
                  ["Count the dots: 2 + 2 + 3 + 5 + 4 + 4 + 3 + 1 + 1 = 25.",
                   "Add the values: 28 + 30 + 48 + 85 + 72 + 76 + 60 + 21 + 23 = 443.",
                   "The mean is 443 ÷ 25 = 17.72, not 17.",
                   "Check by distances from 17: on the left 6 + 4 + 3 = 13, on the right 4 + 8 + 9 + 4 + 6 = 31. "
                   "They are not equal, so 17 is not the balance point."],
                  "No, the mean is 17.72", expect=17.72)])],
    key_terms=["mean", "balance", "shift"]))

# ============================== T3 Tinkering with the median, finding the unknown ===========================
TOPICS.append(TOPIC(
    "T3", "M1", "Tinkering with the Median and Finding the Unknown", ["5.1"], "Apply",
    "Students predict how adding or removing a value moves the median, and use a given mean or median to find "
    "a missing value, a total, or the effect of a correction. They judge statements about mean and median as "
    "always, sometimes or never true.",
    "A value above the median pulls it up, one below pulls it down, and a given mean gives the total, so one "
    "missing value or one correction can be worked out.",
    [A("T3.C1", "Tinkering with the median", "Analyze",
       "Students predict the direction in which the median moves when a value above or below it is included or "
       "removed, and compute the new median as the average of two middle values.",
       textbook=["We know that the median is the middle value in the sorted data: there are an equal number of "
                 "values less than it and greater than it.",
                 "Will including a new value to the data increase or decrease the median? Let us consider the "
                 "following data. The median of this data is 8.",
                 "Suppose we include a value 11. The new value included is greater than the (earlier) median: the "
                 "median can no longer be 8 as there are more values greater than it. Therefore, the median will "
                 "also increase. The median, now, will be the average of the two middle values 8 and 11, which is 9.5.",
                 "We can similarly argue that when a value less than the median is included, the median will decrease."],
       teach=["Predict first: the median of the data is 8. Include 11. Does the median move up, down, or stay?",
              "11 is above the median, so more values now sit above 8 than below it. The middle shifts up. The "
              "two middle values are now 8 and 11, and the median is 9.5.",
              "A value below the median moves the middle down. Removing a value works the other way round."],
       examples=[
           WE("A data set has median 8 and its two middle values after including 11 are 8 and 11. Find the new median.",
              ["The new median is the average of the two middle values 8 and 11.",
               "(8 + 11) ÷ 2 = 19 ÷ 2 = 9.5.", "9.5 is above 8, so the median rose, as predicted."],
              "The new median is 9.5", ncert=["5.1.median_tinker"])],
       key_terms=["median", "middle value"], misconceptions=["M_MEDIAN_MEAN"], minutes=8),
     A("T3.C2", "Finding the unknown: a missing weight", "Apply",
       "Students write an equation from a given mean, a given count and one smudged value, and solve it to find "
       "the missing value.",
       textbook=["Coach Balwan noted down the weights of the kushti players (wrestlers) and the mean as shown. But "
                 "one value that was written down got smudged. Can you find out the missing value?",
                 "Average weight of the players = Sum of weight of all players ÷ Number of players.",
                 "Let the unknown weight be w kg. (42 + 40 + 39 + 33 + 48 + 38 + 42 + 35 + 32 + w) ÷ 10 = 39.2. "
                 "Simplifying this we get, 349 + w = 392, w = 392 − 349 = 43. The missing value is 43 kg."],
       teach=["Predict first: the mean of 10 weights is 39.2. Without knowing the 10th weight, what can you already "
              "say about the total?",
              "Mean times the number of players is the total: 39.2 × 10 = 392.",
              "The nine known weights add to 349. So the missing weight is 392 − 349 = 43 kg."],
       examples=[
           WE("Coach Balwan's mean weight of 10 players is 39.2 kg. Nine weights are 42, 40, 39, 33, 48, 38, 42, 35 "
              "and 32 kg. Find the smudged weight.",
              ["The nine known weights add to 42 + 40 + 39 + 33 + 48 + 38 + 42 + 35 + 32 = 349.",
               "Let the missing weight be w. Then (349 + w) ÷ 10 = 39.2.", "349 + w = 39.2 × 10 = 392.",
               "w = 392 − 349 = 43."],
              "The missing weight is 43 kg", ncert=["5.1.kushti"], expect=43)],
       key_terms=["missing value", "equation"], minutes=8),
     A("T3.C3", "Finding the unknown: a harvest corrected", "Apply",
       "Students recover a total from a mean and a count, correct the total for an error in one value, and find "
       "the corrected mean without the individual data.",
       textbook=["Venkayya keeps track of the coconut harvest in his farm. He calculates the average harvest per "
                 "tree as 25.6. His son verifies the counts and finds that one tree's harvest count is incorrectly "
                 "noted as 3 more than the actual number. Can you find the correct average if the number of trees is 15?",
                 "The data of harvest per tree is not given. Can we still find out the number of coconuts harvested?",
                 "z ÷ 15 = 25.6, so z = 25.6 × 15 = 384. The actual total harvest count is 384 − 3 = 381. The "
                 "correct average harvest is 381 ÷ 15 = 25.4."],
       teach=["Predict first: one count was 3 too high among 15 trees. By how much will the mean drop: 3, or less?",
              "The mean times the number of trees gives the total harvest even without the list: 25.6 × 15 = 384.",
              "Remove the 3 extra: 381. The corrected mean is 381 ÷ 15 = 25.4, a drop of 0.2, which is 3 shared over "
              "15 trees."],
       examples=[
           WE("The mean harvest of 15 trees is 25.6, but one count was written 3 more than the actual. Find the "
              "correct mean.",
              ["Total harvest as noted = 25.6 × 15 = 384.", "Correct total = 384 − 3 = 381.",
               "Correct mean = 381 ÷ 15 = 25.4."],
              "The correct average is 25.4 coconuts per tree", ncert=["5.1.coconut"], expect=25.4)],
       key_terms=["total", "correction", "average"], minutes=8),
     DOER("T3.C4", "Practice: find the missing value", "missing_value_lab", "Apply",
          "Students use a given mean or median with a count to build an equation, find the missing value or the "
          "corrected result, and test claims about adding or removing values.",
          ["Total = mean × number of values.",
           "A missing value is the total minus the sum of the values we know.",
           "A value above the median raises the median, below lowers it."],
          items=[
              FIO("FiO1.q5", "Figure it Out (mean and median, question 5)",
                  "Find the median of 8, 10, 19, 23, 26, 34, 40, 41, 41, 48, 51, 55, 70, 84, 91, 92. (i) What value "
                  "can be included without affecting the median? (ii) What two values? (iii) What one value can be "
                  "removed without affecting the median?",
                  ["There are 16 values, so the median is the average of the 8th and 9th values 41 and 41, which is 41.",
                   "(i) Include 41. The middle value stays 41.",
                   "(ii) Include one value at most 41 and one at least 41, for example 10 and 90.",
                   "(iii) Remove one of the two 41s. The 15 values left have the 8th value as 41."],
                  "The median is 41; add 41; add a pair like 10 and 90; remove a 41"),
              FIO("FiO1.q6", "Figure it Out (mean and median, question 6)",
                  "Justify whether each statement is always true, sometimes true or never true: (i) Removing a "
                  "value less than the median will decrease the median. (ii) Including a value less than the mean "
                  "will decrease the mean. (iii) Including any 4 values will not affect the median. (iv) Including 4 "
                  "values less than the median will increase the median.",
                  ["(i) Never true. The middle moves up or stays; for 1, 2, 3 removing 1 gives 2 and 3 with median 2.5.",
                   "(ii) Always true. A value below the mean adds more left distance, so the balance point moves down.",
                   "(iii) Sometimes true. Two low and two high values leave it; four high values do not.",
                   "(iv) Never true. Values below the median push it down or leave it."],
                  "(i) never (ii) always (iii) sometimes (iv) never"),
              FIO("FiO1.q7", "Figure it Out (mean and median, question 7)",
                  "The mean of the numbers 8, 13, 10, 4, 5, 20, y, 10 is 10.375. Find the value of y.",
                  ["There are 8 values, so the total is 10.375 × 8 = 83.",
                   "The known values add to 8 + 13 + 10 + 4 + 5 + 20 + 10 = 70.", "y = 83 − 70 = 13."],
                  "y = 13", expect=13),
              FIO("FiO1.q8", "Figure it Out (mean and median, question 8)",
                  "The mean of a set of data with 15 values is 134. Find the sum of the data.",
                  ["Sum = mean × number of values = 134 × 15 = 2010."],
                  "2010", expect=2010),
              FIO("FiO1.q9", "Figure it Out (mean and median, question 9)",
                  "Consider the data 12, 47, 8, 73, 18, 35, 39, 8, 29, 25, p. Which of these could be p if the "
                  "median is 29? (i) 10 (ii) 25 (iii) 40 (iv) 100 (v) 29 (vi) 47 (vii) 30",
                  ["With p there are 11 values, so the median is the 6th value when sorted.",
                   "Without p the sorted values are 8, 8, 12, 18, 25, 29, 35, 39, 47, 73.",
                   "If p is below 29 the 6th value drops to 25 at most, so p must be at least 29.",
                   "For p at least 29 the five values below stay 8, 8, 12, 18, 25 and the 6th is 29."],
                  "p could be 40, 100, 29, 47 or 30, that is (iii), (iv), (v), (vi), (vii)"),
              FIO("FiO3.q2", "Figure it Out (more on mean and median, question 2)",
                  "Give two examples of data for each condition: (i) 3 numbers whose mean is 8. (ii) 4 numbers whose "
                  "median is 15.5. (iii) 5 numbers whose mean is 13.6. (iv) 6 numbers whose mean equals the "
                  "median. (v) 6 numbers whose mean is greater than the median.",
                  ["(i) The total is 24: 7, 8, 9 and 4, 8, 12.",
                   "(ii) The middle two must add to 31: 10, 15, 16, 20 and 1, 15, 16, 99.",
                   "(iii) The total is 68: 10, 12, 13, 15, 18 and 1, 2, 3, 4, 58.",
                   "(iv) 1, 2, 3, 4, 5, 6 has mean 3.5 and median 3.5. All six values equal also works.",
                   "(v) 1, 2, 3, 4, 5, 50 has median 3.5 and mean 65 ÷ 6 ≈ 10.8."],
                  "Examples as shown"),
              FIO("FiO3.q3", "Figure it Out (more on mean and median, question 3)",
                  "Fill in the blanks so the median is 13: 5, 21, 14, _, _, _. How many possibilities exist if only "
                  "counting numbers are allowed?",
                  ["With 6 values the median is the average of the 3rd and 4th, so they must add to 26.",
                   "For example 1, 12, 14 gives 1, 5, 12, 14, 14, 21 with middle values 12 and 14.",
                   "Also 12, 13, 13 gives 5, 12, 13, 13, 14, 21, and 3, 12, 100 works.",
                   "One blank can be made as large as we like, so the possibilities never end."],
                  "For example 1, 12, 14; there are infinitely many possibilities"),
              FIO("FiO3.q4", "Figure it Out (more on mean and median, question 4)",
                  "Fill in the blanks so the mean is 6.5: 3, 11, _, _, 15, 6. How many possibilities exist if "
                  "only counting numbers are allowed?",
                  ["The total must be 6.5 × 6 = 39.", "The known values add to 3 + 11 + 15 + 6 = 35.",
                   "The two blanks add to 39 − 35 = 4, so they are 1 and 3, or 2 and 2."],
                  "Two possibilities: 1 and 3, or 2 and 2"),
              FIO("FiO3.q6", "Figure it Out (more on mean and median, question 6)",
                  "Two new students join a class whose average height was 150.2 cm with 24 students. (i) Which "
                  "statements are correct? (ii) The new heights are 149 cm and 152 cm: what happens to the mean? "
                  "(iii) What happens to the median?",
                  ["(i) The new heights have to be measured, since they decide the new average. The others claim too much.",
                   "(ii) 149 is 1.2 below 150.2 and 152 is 1.8 above. The surplus wins, so the average increases "
                   "slightly: (24 × 150.2 + 149 + 152) ÷ 26 ≈ 150.22.",
                   "(iii) The median depends on the actual heights, which we are not given, so there is not enough "
                   "information."],
                  "(i) the new heights must be measured (ii) the average increases (iii) not enough information"),
              FIO("FiO3.q8", "Figure it Out (more on mean and median, question 8)",
                  "The average weight of a group last month was 65.3 kg and the median 67 kg. This month one person "
                  "lost 2 kg and two persons gained 1 kg each. What can we say about the change in mean and median?",
                  ["The total changes by −2 + 1 + 1 = 0, and the number of people stays the same, so the mean stays "
                   "65.3 kg.",
                   "The median depends on who the three people are and where they sit in the sorted list, so we "
                   "cannot say."],
                  "The mean is unchanged; nothing can be said about the median")])],
    key_terms=["median", "missing value", "total"]))

# ============================== T4 Mean and median with frequencies =========================================
TOPICS.append(TOPIC(
    "T4", "M1", "Mean and Median with Frequencies", ["5.1"], "Apply",
    "Students find the mean from a frequency table by weighting each value with its frequency, and find the median "
    "by adding frequencies until the middle positions are reached.",
    "Each value is counted as many times as it occurs, so the mean uses value times frequency and the median is found "
    "from running totals of the frequencies.",
    [A("T4.C1", "The mean of a frequency table", "Apply",
       "Students compute the mean family size from a frequency table by adding every value as many times as it "
       "occurs, and explain why averaging the distinct values is wrong.",
       textbook=["What is the average family size of students in your class? How would you find this out?",
                 "We can collect the data of how many family members each student has, add them up, and divide it "
                 "by the number of students. The family size data of students in a class is shown in the table.",
                 "Some of you may have thought, Easy! (3 + 4 + 5 + 6 + 7 + 8 + 9 + 10) ÷ 8 = 52 ÷ 8 = 6.5.",
                 "Remember that finding the average involves adding all the values in the data. The number 3 occurs "
                 "three times, the number 4 occurs eleven times, and so on. Do these reflect in your calculation?",
                 "Accounting for the frequencies of each value, the average is 188 ÷ 36 = 5.22. The average family "
                 "size of this class is 5.22."],
       teach=["Predict first: the family sizes run from 3 to 10, and 4 occurs 11 times while 10 occurs once. Will the "
              "true average be bigger or smaller than 6.5, the middle of 3 and 10?",
              "Adding 3 + 4 + ... + 10 counts each size once. But 4 occurs 11 times and 10 only once.",
              "Weight each value by its frequency: the total is 188 and there are 36 students, so the mean is "
              "188 ÷ 36 ≈ 5.22, below 6.5."],
       examples=[
           WE("Find the mean family size of the class from the table: size 3, 4, 5, 6, 7, 8, 9, 10 occurs 3, 11, 9, "
              "7, 3, 1, 1, 1 times.",
              ["Number of students = 3 + 11 + 9 + 7 + 3 + 1 + 1 + 1 = 36.",
               "Total of all values = 9 + 44 + 45 + 42 + 21 + 8 + 9 + 10 = 188.", "Mean = 188 ÷ 36 ≈ 5.22."],
              "The mean family size is about 5.22", ncert=["5.1.family_mean"], expect=5.22)],
       key_terms=["frequency", "mean"], misconceptions=["M_RAW_FREQ"], minutes=8),
     A("T4.C2", "The median from running totals", "Apply",
       "Students locate the middle positions in a frequency table by adding frequencies, and name the median "
       "without writing out every value.",
       textbook=["What is the median family size of this class? We know that there are 36 values in the data. The "
                 "median would be the average of the 18th and 19th value in the sequence when the data is ordered.",
                 "Do we need to write all the 36 numbers in order? Is there a quicker way to find out? We can make "
                 "use of the table where the frequencies are listed.",
                 "Adding the frequencies of 3 and 4, we get 3 + 11 = 14. This means the value in the 14th position when "
                 "the data is sorted is 4. Adding the frequencies of 3, 4, and 5, we get 3 + 11 + 9 = 23. We can see "
                 "that all the values from positions 15 to 23 are 5. Therefore, the median of this data is 5."],
       teach=["Predict first: with 36 values, which positions hold the median?",
              "The 18th and 19th. Add frequencies from the smallest: 3, then 3 + 11 = 14, then 14 + 9 = 23.",
              "Positions 15 to 23 all hold 5, so the 18th and 19th are both 5 and the median is 5."],
       examples=[
           WE("Find the median family size from the same table by adding frequencies.",
              ["There are 36 values, so the median is the average of the 18th and 19th.",
               "Running totals: size 3 reaches 3, size 4 reaches 3 + 11 = 14, size 5 reaches 14 + 9 = 23.",
               "Positions 15 to 23 hold 5, so both the 18th and 19th values are 5.", "The median is 5."],
              "The median family size is 5", ncert=["5.1.family_median"], expect=5)],
       key_terms=["frequency", "median", "running total"], minutes=8),
     DOER("T4.C3", "Practice: build and read a frequency table", "frequency_table_lab", "Apply",
          "Students enter frequencies, see the total, the mean and the running totals update, and locate the median "
          "position for tables of their own.",
          ["Mean = sum of value times frequency, divided by sum of frequencies.",
           "The median sits where the running total passes the middle position."],
          items=[
              FIO("FiO1.q10", "Figure it Out (mean and median, question 10)",
                  "The number of times students rode their cycles in a week is shown in a dot plot. Four students "
                  "rode twice. (i) Find the average number of rides. (ii) Find the median. (iii) Which statements "
                  "are valid: (a) Everyone used their cycle at least once. (b) Almost everyone used their cycle a few "
                  "times. (c) Some students cycled more than once on some days. (d) Exactly 5 students used their "
                  "cycles more than once on some days. (e) The next week all cycled 1 more time: new average and median?",
                  ["The counts read from the plot: 0 rides 3 students, 1 ride 1, 2 rides 4, 3 rides 7, 4 rides 7, "
                   "5 rides 5, 6 rides 4, 7 rides 6, 8 rides 3, 10 rides 2. That is 42 students.",
                   "(i) Total rides = 0 + 1 + 8 + 21 + 28 + 25 + 24 + 42 + 24 + 20 = 193. Mean = 193 ÷ 42 ≈ 4.6.",
                   "(ii) The 21st and 22nd values: the running totals are 3, 4, 8, 15, 22. Both are 4, so the median is 4.",
                   "(iii) (a) is not valid because 3 students rode 0 times. (b) is valid: 39 of 42 rode at least once. "
                   "(c) is valid: someone who rode 8 or 10 times in a week must have ridden twice on a day. "
                   "(d) is valid: exactly 3 + 2 = 5 students rode more than 7 times.",
                   "(e) Every value goes up by 1, so the mean becomes about 5.6 and the median 5."],
                  "(i) about 4.6 (ii) 4 (iii) (b), (c), (d) are valid (e) about 5.6 and 5"),
              FIO("FiO1.q11", "Figure it Out (mean and median, question 11)",
                  "In a dart competition the number of throws needed to hit the bull's eye is given: trials 1 to 10 "
                  "had 1, 0, 0, 1, 4, 9, 12, 15, 10, 10 students. Describe the data using its minimum, maximum, "
                  "mean and median.",
                  ["Students = 1 + 0 + 0 + 1 + 4 + 9 + 12 + 15 + 10 + 10 = 62.",
                   "Minimum 1 trial, maximum 10 trials.",
                   "Total trials = 1 + 4 + 20 + 54 + 84 + 120 + 90 + 100 = 473, so mean = 473 ÷ 62 ≈ 7.6.",
                   "The 31st and 32nd values: the running totals are 1, 2, 6, 15, 27, 42, so both are 8 and the "
                   "median is 8."],
                  "Minimum 1, maximum 10, mean about 7.6, median 8")])],
    key_terms=["frequency", "mean", "median"]))

# ============================== T5 Spreadsheets =============================================================
TOPICS.append(TOPIC(
    "T5", "M1", "Spreadsheets: Totals and Averages Fast", ["5.1"], "Apply",
    "Students name cells and ranges in a spreadsheet and write formulae that find the total or the average of a "
    "row or column, then use them on a class marks table.",
    "A cell is named by column letter and row number, a range is Start:End, and SUM and AVERAGE formulae do the "
    "adding and dividing at once.",
    [A("T5.C1", "Reading a spreadsheet: cells and ranges", "Understand",
       "Students locate a value from a column letter and a row number and describe a row or a column as a range "
       "written Start:End.",
       textbook=["Sudhakar has collected the mid-term exam marks obtained by his Grade 8 students in a table of 22 "
                 "students and 6 subjects.",
                 "Sudhakar has to calculate the total marks scored by each student. He is also interested in knowing "
                 "the average marks scored in each subject. But there are so many numbers! Is there any way to further "
                 "quicken this process?",
                 "A spreadsheet is like a digital notebook with rows and columns of small boxes called cells. In each "
                 "cell, we can type text or numbers.",
                 "Can you tell which cell has the marks obtained by Farooq in Mathematics? Cells are named by the "
                 "column headers A, B, C, … and row headers 1, 2, 3, … Farooq's score in Mathematics is in cell E5.",
                 "Can you tell what data is in column B7? In which subjects has Ashwin scored more than 30 marks?",
                 "We can describe a row of cells by an expression of the form Start:End. Nagesh's marks are described "
                 "by B3:G3, Gowri's marks in Odia, Telugu and English by B7:D7, and D2:D6 describes the marks in "
                 "English for the first five students."],
       teach=["Predict first: with the names down column A and subjects across row 1, where would Farooq's Maths "
              "marks sit? Count the column letter and the row number.",
              "Columns are letters, rows are numbers. Farooq is in row 5 and Maths is column E, so the cell is E5, "
              "with 42 marks.",
              "A run of cells is written Start:End. B3:G3 is Nagesh across all six subjects, D2:D6 is five English "
              "marks going down."],
       examples=[
           WE("Find the cell of Farooq's Mathematics marks and describe Nagesh's marks as a range.",
              ["Farooq is in row 5 and Mathematics is in column E, so the cell is E5 and it holds 42.",
               "Nagesh is in row 3, and his six marks run from column B to column G.",
               "So his marks are the range B3:G3."],
              "E5 holds 42; Nagesh's marks are B3:G3", ncert=["5.1.sheet_intro", "5.1.sheet_cells"])],
       key_terms=["cell", "range", "spreadsheet"], minutes=8),
     A("T5.C2", "Formulae: SUM and AVERAGE", "Apply",
       "Students type a SUM or AVERAGE formula over a range to find a student's total or a subject's class "
       "average, and compare two subjects.",
       textbook=["We can also enter formulae in a cell. We can write a formula that computes the sum or average of "
                 "a row, or column of cells.",
                 "=SUM(B3:G3) calculates the total marks for Nagesh across all subjects, while =AVERAGE(B7:D7) "
                 "calculates Gowri's average marks across Odia, Telugu and English.",
                 "What formula would you type to find out the class average marks in Science? Find out if the "
                 "class average marks in Odia is greater than the class average marks in Telugu. Show the average "
                 "marks in other subjects after the last row by typing the appropriate formulae. Get the total "
                 "scores of each student by typing the appropriate formulae.",
                 "Note to the teacher: any spreadsheet application can be used, and students can share a computer "
                 "in groups, or the screen can be projected."],
       teach=["Predict first: which would be quicker for Nagesh's total, adding six numbers or typing one formula?",
              "=SUM(B3:G3) adds the range, here 41 + 43 + 48 + 39 + 40 + 39 = 250. =AVERAGE(B7:D7) averages "
              "Gowri's first three marks.",
              "A column works the same way: a formula over a column gives a subject's class average, and two such "
              "averages can be compared."],
       examples=[
           WE("Nagesh's marks are 41, 43, 48, 39, 40 and 39. Find his total, and say the formula.",
              ["Add: 41 + 43 = 84, 84 + 48 = 132, 132 + 39 = 171, 171 + 40 = 211, 211 + 39 = 250.",
               "The formula over his row is =SUM(B3:G3)."],
              "His total is 250, found with =SUM(B3:G3)", ncert=["5.1.sheet_formulae"])],
       key_terms=["formula", "SUM", "AVERAGE"], minutes=8),
     A("T5.C2x", "Gowri's average with one formula", "Apply",
       "Students type an AVERAGE formula over a range of three cells to find Gowri's average marks and check it "
       "against adding the marks and dividing by three.",
       teach=["Predict first: will Gowri's average of 27, 29 and 34 be above or below 30?",
              "=AVERAGE(B7:D7) adds the three cells and divides by 3, giving 30."],
       examples=[
           WE("Gowri's marks in Odia, Telugu and English are 27, 29 and 34. Find their average and the formula.",
              ["27 + 29 + 34 = 90.", "90 ÷ 3 = 30.", "The formula is =AVERAGE(B7:D7)."],
              "The average is 30, from =AVERAGE(B7:D7)", ncert=["5.1.sheet_tasks", "5.1.sheet_note"])],
       key_terms=["formula", "AVERAGE", "range"], minutes=6, thin=True),
     DOER("T5.C3", "Practice: type the formulae", "spreadsheet_sim", "Apply",
          "Students click cells, type SUM and AVERAGE formulae over rows and columns of the marks table, and "
          "check totals, subject averages and which of two subjects has the higher average.",
          ["A cell is a column letter followed by a row number.",
           "Start:End names a run of cells; SUM adds them and AVERAGE finds their mean."])],
    key_terms=["spreadsheet", "formula", "cell"]))
