# -*- coding: utf-8 -*-
"""Topics T1 to T4 (module M1: multiplying fractions). Book section 8.1, first half."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Introduction ==============================================================
TOPICS.append(TOPIC(
    "T1", "M1", "Aaron and the Tortoise", ["Chapter opening", "8.1"], "Understand",
    "",
    "Aaron walks 3 km in an hour and his pet tortoise walks only a quarter of a kilometre in an hour. How far does "
    "each of them go when the time is a fraction of an hour?",
    [A("T1.C1", "A tortoise on a garden path", "Remember",
       "",
       textbook=["Working with Fractions",
                 "8.1 Multiplication of Fractions",
                 "Aaron walks 3 kilometres in 1 hour. How far can he walk in 5 hours?",
                 "Aaron's pet tortoise walks at a much slower pace. It can walk only 1/4 kilometre in 1 hour. How far "
                 "can it walk in 3 hours?"],
       teach=["Picture Aaron's pet tortoise creeping along a garden path. It walks only 1/4 km in 1 hour.",
              "Make a guess before the next step: how far does it walk in half an hour?",
              "Does the answer come from adding, from dividing, or from something else?"],
       ncert=["opening"], key_terms=["fraction"], video_focus=["HOOK"], minutes=4, enrichment=True),
     A("T1.C2", "The question to keep: what if the time is a fraction of an hour?", "Understand", "",
       teach=["Predict: if the tortoise walks 1/4 km in 1 hour, is the distance in half an hour more than 1/4 km "
              "or less?",
              "For whole numbers of hours the distance is found by multiplying: Aaron walks 5 × 3 = 15 km in 5 hours.",
              "Keep this question in mind: the next topics find what multiplying means when the number of hours, or "
              "the distance, is a fraction."],
       enrichment=True)],
    topic_type="framing"))

# ============================== T2 A fraction and a whole number ==============================================
TOPICS.append(TOPIC(
    "T2", "M1", "A Fraction and a Whole Number", ["8.1"], "Apply",
    "Students multiply a whole number and a fraction, in either order, by dividing by the denominator and then "
    "multiplying by the numerator, and use this in distance, land, money, milk, oil and time problems.",
    "A fraction times a whole number is found in two steps: divide the whole number by the denominator, then "
    "multiply the result by the numerator.",
    [A("T2.C1", "A whole number of hours", "Apply",
       "Students find the distance covered in a whole number of hours when the distance in one hour is a fraction, "
       "by repeated addition and multiplication.",
       textbook=["Distance covered in 1 hour = 3 km.",
                 "Therefore, distance covered in 5 hours = 5 × 3 km = 3 + 3 + 3 + 3 + 3 km = 15 km.",
                 "Here, the distance covered in an hour is a fraction. This does not matter. The total distance "
                 "covered is calculated in the same way, as multiplication.",
                 "Distance covered in 1 hour = 1/4 km.",
                 "Therefore, distance covered in 3 hours = 3 × 1/4 km = 1/4 + 1/4 + 1/4 km = 3/4 km.",
                 "The tortoise can walk 3/4 km in 3 hours."],
       teach=["Predict first: is 3 × 1/4 more than 1 or less than 1?",
              "Aaron walks 5 × 3 = 3 + 3 + 3 + 3 + 3 = 15 km in 5 hours.",
              "The tortoise's distance in one hour is a fraction, but the total is found the same way: by "
              "multiplication, or by adding the same fraction again and again."],
       examples=[
           WE("Aaron's pet tortoise can walk 1/4 km in 1 hour. How far can it walk in 3 hours?",
              ["Distance covered in 1 hour = 1/4 km.",
               "Distance covered in 3 hours = 3 × 1/4 km.",
               "3 × 1/4 = 1/4 + 1/4 + 1/4 = 3/4.",
               "So the tortoise can walk 3/4 km in 3 hours."],
              "3/4 km", ncert=["8.1.aaron", "8.1.tortoise3"])],
       key_terms=["fraction"], misconceptions=["M_WHOLE_ONLY_TOP"], minutes=8),
     A("T2.C2", "A fraction of an hour", "Apply",
       "Students find the distance covered in a fraction of an hour by dividing the distance in one hour into equal "
       "parts and then multiplying by the numerator.",
       textbook=["Let us consider a case where the time spent walking is a fraction of an hour.",
                 "We saw that Aaron can walk 3 kilometres in 1 hour. How far can he walk in 1/5 hours?",
                 "We continue to calculate the total distance covered through multiplication. Distance covered in "
                 "1/5 hours = 1/5 × 3 km.",
                 "In 1/5 hours, distance covered is equal to the length we get by dividing 3 km into 5 equal parts, "
                 "which is 3/5 km. This tells us that 1/5 × 3 = 3/5.",
                 "How far can Aaron walk in 2/5 hours? Once again, we have: distance covered = 2/5 × 3 km.",
                 "1. We can first find the distance covered in 1/5 hours.",
                 "2. Since the duration 2/5 is twice 1/5, we multiply this distance by 2 to get the total distance "
                 "covered.",
                 "Multiplying this distance by 2, we get 2 × 3/5 = 6/5 km. From this we can see that 2/5 × 3 = 6/5.",
                 "We did this multiplication as follows: First, we divided the multiplicand, 3, by the denominator "
                 "of the multiplier, 5, to get 3/5. We then multiplied the result by the numerator of the "
                 "multiplier, that is 2, to get 6/5. Thus, whenever we need to multiply a fraction and a whole "
                 "number, we follow the steps above."],
       teach=["Predict first: is the distance in 2/5 of an hour more than 3 km or less?",
              "In 1/5 of an hour Aaron covers one of 5 equal parts of 3 km, which is 3 ÷ 5 = 3/5 km.",
              "2/5 of an hour is two such parts, so the distance is 2 × 3/5 = 6/5 km.",
              "To multiply a fraction and a whole number: divide the whole number by the denominator, then "
              "multiply by the numerator."],
       examples=[
           WE("Aaron can walk 3 km in 1 hour. How far can he walk in 2/5 of an hour?",
              ["Distance covered in 1 hour = 3 km.",
               "In 1/5 of an hour he covers 3 km divided into 5 equal parts: 3 ÷ 5 = 3/5 km.",
               "2/5 of an hour is twice 1/5 of an hour, so multiply by 2: 2 × 3/5 = 6/5 km.",
               "So 2/5 × 3 = 6/5, which is 1 1/5 km."],
              "6/5 km, that is 1 1/5 km", ncert=["8.1.fifth", "8.1.two_fifths", "8.1.rule_whole"])],
       key_terms=["multiplier", "multiplicand", "numerator", "denominator"], misconceptions=["M_WHOLE_ONLY_TOP"],
       minutes=10),
     A("T2.C3", "Land for grandchildren and internet time", "Apply",
       "Students multiply a whole number and a fraction in a land-sharing problem, and multiply a fraction and a "
       "whole number after converting a mixed fraction.",
       textbook=["Example 1: A farmer had 5 grandchildren. She distributed 2/3 acre of land to each of her "
                 "grandchildren. How much land in all did she give to her grandchildren?",
                 "5 × 2/3 = 2/3 + 2/3 + 2/3 + 2/3 + 2/3 = 10/3.",
                 "Example 2: 1 hour of internet time costs ₹8. How much will 1 1/4 hours of internet time cost?",
                 "1 1/4 hours is 5/4 hours (converting from a mixed fraction).",
                 "Cost of 5/4 hour of internet time = 5/4 × 8 = 5 × 8/4 = 5 × 2 = 10.",
                 "It costs ₹10 for 1 1/4 hours of internet time."],
       teach=["Predict first: is 5 × 2/3 more than 2 or less than 2?",
              "Repeated addition gives 10/3; multiplying the whole number into the numerator gives the same.",
              "A mixed fraction is changed into a fraction first, so 1 1/4 becomes 5/4."],
       examples=[
           WE("A farmer had 5 grandchildren. She gave 2/3 acre of land to each of them. How much land did she give "
              "in all?",
              ["Land for each grandchild = 2/3 acre.",
               "In all: 5 × 2/3 = 2/3 + 2/3 + 2/3 + 2/3 + 2/3 = 10/3.",
               "The same answer comes from 5 × 2 = 10 parts of size 1/3."],
              "10/3 acre, that is 3 1/3 acre", ncert=["8.1.ex1"]),
           WE("1 hour of internet time costs ₹8. How much will 1 1/4 hours of internet time cost?",
              ["1 1/4 hours is 5/4 hours (converting from a mixed fraction).",
               "Cost of 5/4 hour = 5/4 × 8.",
               "5/4 × 8 = 5 × 8/4 = 5 × 2 = 10.",
               "It costs ₹10 for 1 1/4 hours of internet time."],
              "₹10", ncert=["8.1.ex2"])],
       key_terms=["mixed fraction"], misconceptions=["M_MIXED_PARTS"], minutes=10),
     DOER("T2.C4", "Practice: a fraction and a whole number", "fraction_distance_strip", "Apply",
          "Students multiply a whole number and a fraction in problems about milk, canals, oil and the Moon, and "
          "write the product as a mixed fraction.",
          ["Divide the whole number by the denominator, then multiply by the numerator.",
           "Or multiply the whole number into the numerator and keep the denominator.",
           "Write an improper result as a mixed fraction when the question asks."],
          items=[
              FIO("8.1.FiOA1", "Figure it Out (a fraction and a whole number), Q1",
                  "Tenzin drinks 1/2 glass of milk every day. How many glasses of milk does he drink in a week? How "
                  "many glasses of milk did he drink in the month of January?",
                  ["A week has 7 days: 7 × 1/2 = 7/2 glasses.",
                   "January has 31 days: 31 × 1/2 = 31/2 glasses."],
                  "7/2 glasses (3 1/2) in a week and 31/2 glasses (15 1/2) in January",
                  tool="fraction_distance_strip"),
              FIO("8.1.FiOA2", "Figure it Out (a fraction and a whole number), Q2",
                  "A team of workers can make 1 km of a water canal in 8 days. So, in one day, the team can make ___ "
                  "km of the water canal. If they work 5 days a week, they can make ___ km of the water canal in a "
                  "week.",
                  ["In one day the team makes 1 ÷ 8 = 1/8 km.",
                   "In 5 days they make 5 × 1/8 = 5/8 km."],
                  "1/8 km in one day and 5/8 km in a week"),
              FIO("8.1.FiOA3", "Figure it Out (a fraction and a whole number), Q3",
                  "Manju and two of her neighbours buy 5 litres of oil every week and share it equally among the 3 "
                  "families. How much oil does each family get in a week? How much oil will one family get in 4 "
                  "weeks?",
                  ["Each family gets 5 ÷ 3 = 5/3 litres in a week.",
                   "In 4 weeks one family gets 4 × 5/3 = 20/3 litres."],
                  "5/3 litres (1 2/3) in a week and 20/3 litres (6 2/3) in 4 weeks"),
              FIO("8.1.FiOA4", "Figure it Out (a fraction and a whole number), Q4",
                  "Safia saw the Moon setting on Monday at 10 pm. Her mother, who is a scientist, told her that "
                  "every day the Moon sets 5/6 hour later than the previous day. How many hours after 10 pm will "
                  "the moon set on Thursday?",
                  ["From Monday to Thursday is 3 days.",
                   "The Moon sets 3 × 5/6 = 15/6 = 5/2 hours later, which is 2 1/2 hours.",
                   "2 1/2 hours after 10 pm is 12:30 am."],
                  "5/2 hours, that is 2 1/2 hours after 10 pm, so the Moon sets at 12:30 am"),
              FIO("8.1.FiOA5", "Figure it Out (a fraction and a whole number), Q5",
                  "Multiply and then convert it into a mixed fraction: (a) 7 × 3/5 (b) 4 × 1/3 (c) 9/7 × 6 "
                  "(d) 13/11 × 6",
                  ["(a) 7 × 3/5 = 21/5 = 4 1/5.",
                   "(b) 4 × 1/3 = 4/3 = 1 1/3.",
                   "(c) 9/7 × 6 = 54/7 = 7 5/7.",
                   "(d) 13/11 × 6 = 78/11 = 7 1/11."],
                  "(a) 4 1/5 (b) 1 1/3 (c) 7 5/7 (d) 7 1/11"),
          ])]))

# ============================== T3 Two fractions with a unit square ==========================================
TOPICS.append(TOPIC(
    "T3", "M1", "Multiplying Two Fractions with a Unit Square", ["8.1"], "Apply",
    "Students multiply two fractions by dividing the second fraction into as many equal parts as the denominator of "
    "the first and then taking the numerator's worth of parts, using a unit square as the whole, and link the "
    "product to the area of a rectangle.",
    "A fraction of a fraction is found by cutting the unit square into rows and columns and counting the shaded "
    "parts.",
    [A("T3.C1", "Half of a quarter", "Apply",
       "Students find half of a quarter by cutting a unit square, and connect the product of two fractions to the "
       "area of a rectangle with fractional sides.",
       textbook=["What happens when both numbers in the multiplication are fractions?",
                 "Multiplying Two Fractions",
                 "We know, that Aaron's pet tortoise can walk only 1/4 km in 1 hour. How far can it walk in half an "
                 "hour?",
                 "Following our approach of using multiplication to solve such problems, we have: distance covered "
                 "in 1/2 hour = 1/2 × 1/4 km.",
                 "Therefore, the distance covered in 1/2 an hour is the length we get by dividing 1/4 into 2 equal "
                 "parts. To find this, it is useful to represent fractions using the unit square to stand for a "
                 "\"whole\".",
                 "Since the whole is divided into 8 equal parts and one of the parts is shaded, we can say that 1/8 "
                 "of the whole is shaded. So, the distance covered by the tortoise in half an hour is 1/8 km. This "
                 "tells us that 1/2 × 1/4 = 1/8.",
                 "Connection between the Area of a Rectangle and Fraction Multiplication",
                 "In the figure, what is the length and breadth of the shaded rectangle? Since we started with a "
                 "unit square (of side 1 unit), the length and breadth are 1/2 unit and 1/4 unit.",
                 "What is the area of this rectangle? We see that 8 such rectangles give the square of area 1 "
                 "square unit. So, the area of each rectangle is 1/8 square units.",
                 "Do you see any relation between the area and the product of length and breadth? The area of a "
                 "rectangle of fractional sides equals the product of its sides."],
       teach=["Predict first: is half of a quarter more than a quarter or less?",
              "Draw a unit square as the whole and shade 1/4 of it, then cut that quarter into 2 equal parts.",
              "The whole is now cut into 8 equal parts and one is shaded, so 1/2 × 1/4 = 1/8.",
              "The shaded piece is a rectangle with sides 1/2 and 1/4, and its area is 1/8 square unit."],
       examples=[
           WE("Aaron's pet tortoise walks 1/4 km in 1 hour. How far can it walk in half an hour?",
              ["Distance covered in 1/2 hour = 1/2 × 1/4 km.",
               "Take the unit square as the whole and shade 1/4 of it.",
               "Divide that quarter into 2 equal parts: the whole is now cut into 8 equal parts and 1 is shaded.",
               "So 1/2 × 1/4 = 1/8, and the tortoise walks 1/8 km in half an hour."],
              "1/8 km", ncert=["8.1.half_quarter"]),
           WE("In the unit square, a shaded rectangle has sides 1/2 unit and 1/4 unit, and 8 such rectangles fill the "
              "square. What is its area, and how does it relate to the sides?",
              ["The unit square has side 1 unit and area 1 square unit.",
               "8 such rectangles fill the square, so each has area 1/8 square unit.",
               "The sides are 1/2 unit and 1/4 unit, and 1/2 × 1/4 = 1/8.",
               "The area of a rectangle of fractional sides equals the product of its sides."],
              "1/8 square unit, which equals 1/2 × 1/4", ncert=["8.1.area_link"])],
       key_terms=["unit square", "area"], misconceptions=["M_FRACTION_OF_WHOLE"], minutes=10),
     A("T3.C2", "Three quarters of two fifths", "Apply",
       "Students multiply 3/4 by 2/5 by finding 1/4 of 2/5 in a unit square of 5 rows and 4 columns and then taking "
       "3 of those parts.",
       textbook=["If the tortoise walks faster and it can cover 2/5 km in 1 hour, how far will it walk in 3/4 of an "
                 "hour? Distance covered = 3/4 × 2/5.",
                 "(i) First find the distance covered in 1/4 of an hour. (ii) Multiply the result by 3, to get the "
                 "distance covered in 3/4 of an hour.",
                 "Distance in km covered in 1/4 of an hour = the quantity we get by dividing 2/5 into 4 equal parts.",
                 "The whole is divided into 5 rows and 4 columns, creating 5 × 4 = 20 equal parts. Number of these "
                 "parts shaded = 2. So, the distance covered in 1/4 of an hour = 2/20.",
                 "Now, we need to multiply 2/20 by 3. Distance covered in 3/4 of an hour = 3 × 2/20 = 6/20. So, "
                 "3/4 × 2/5 = 6/20 = 3/10.",
                 "In the case of a fraction multiplied by another fraction, we follow a method similar to the one we "
                 "used when we multiplied a fraction by a whole number. We multiplied as follows: 2/5 ÷ 4 = 2/20 "
                 "(divide the multiplicand by 4), then 3 × 2/20 = 6/20 (multiply by the numerator 3)."],
       teach=["Predict first: is 3/4 of 2/5 more than 2/5 or less?",
              "The unit square is cut into 5 rows (fifths) and 4 columns (quarters), making 20 equal parts.",
              "2/5 is 2 rows; dividing it into 4 equal parts gives 2 of the 20 parts, which is 2/20.",
              "Multiplying by the numerator 3 gives 6/20, and 6/20 = 3/10 in the lowest form."],
       examples=[
           WE("A tortoise covers 2/5 km in 1 hour. How far will it walk in 3/4 of an hour?",
              ["Distance = 3/4 × 2/5 km.",
               "First find the distance in 1/4 of an hour: divide 2/5 into 4 equal parts.",
               "The unit square has 5 rows and 4 columns, so 5 × 4 = 20 equal parts, and 2 of them are shaded: 2/20.",
               "Multiply by 3 for 3/4 of an hour: 3 × 2/20 = 6/20.",
               "So 3/4 × 2/5 = 6/20 = 3/10."],
              "3/10 km", ncert=["8.1.three_fourths_two_fifths"])],
       key_terms=["unit square", "multiplier"], misconceptions=["M_ADD_ACROSS"], minutes=10),
     A("T3.C3", "Five quarters of three halves", "Analyze",
       "Students multiply 5/4 by 3/2 using a unit square for 3/2, a whole and a half, divided into 4 equal parts "
       "and then taking 5 of them.",
       textbook=["Using this understanding, multiply 5/4 × 3/2.",
                 "First, let us represent 3/2, taking the unit square as the whole. Since the fraction 3/2 is one "
                 "whole and a half, it can be seen as one whole square and half of a second square.",
                 "Following the steps of multiplication, we need to first divide this fraction 3/2 into 4 equal "
                 "parts. The yellow shaded region represents the fraction obtained by dividing 3/2 into 4 equal "
                 "parts. What is its value?",
                 "We see that the whole is divided into 2 rows and 4 columns, creating 2 × 4 = 8 equal parts. "
                 "Number of parts shaded = 3. So the yellow shaded part = 3/8.",
                 "Now, the next step is multiplying this result by 5. This gives the product of 5/4 and 3/2: "
                 "5/4 × 3/2 = 5 × 3/8 = 15/8."],
       teach=["Predict first: is 5/4 × 3/2 more than 3/2 or less?",
              "3/2 is one whole square and half of another. Cut each square into 2 rows and 4 columns, which is "
              "8 equal parts per square.",
              "Dividing 3/2 into 4 equal parts leaves 3 of the 8 parts, which is 3/8.",
              "Multiplying by the numerator 5 gives 5 × 3/8 = 15/8, which is more than 3/2, because 5/4 is more "
              "than 1."],
       examples=[
           WE("Multiply 5/4 × 3/2, using a unit square as the whole.",
              ["Represent 3/2 as one whole square and half of a second square.",
               "Divide 3/2 into 4 equal parts: the whole is divided into 2 rows and 4 columns, which is 2 × 4 = 8 "
               "equal parts, and 3 of them are shaded.",
               "So one quarter of 3/2 is 3/8.",
               "Multiply by 5: 5/4 × 3/2 = 5 × 3/8 = 15/8."],
              "15/8, that is 1 7/8", ncert=["8.1.mathtalk_54_32"])],
       key_terms=["numerator"], misconceptions=["M_MULT_BIGGER"], minutes=10),
     DOER("T3.C4", "Practice: products with a unit square", "unit_square_product", "Apply",
          "Students find products of unit fractions with a unit square as the whole, and notice how the rows and "
          "columns grow.",
          ["Cut the unit square into rows and columns, one for each denominator.",
           "The number of equal parts is the number of rows times the number of columns.",
           "Shade the parts that make up the fraction, and read the product from the whole."],
          items=[
              FIO("8.1.FiOB1", "Figure it Out (two fractions), Q1",
                  "Find the following products. Use a unit square as a whole for representing the fractions: "
                  "(a) 1/3 × 1/5 (b) 1/4 × 1/3 (c) 1/5 × 1/2 (d) 1/6 × 1/5. Now, find 1/12 × 1/18.",
                  ["(a) The unit square has 5 rows and 3 columns, 15 parts, and 1 is shaded: 1/3 × 1/5 = 1/15.",
                   "(b) 3 rows and 4 columns make 12 parts: 1/4 × 1/3 = 1/12.",
                   "(c) 2 rows and 5 columns make 10 parts: 1/5 × 1/2 = 1/10.",
                   "(d) 5 rows and 6 columns make 30 parts: 1/6 × 1/5 = 1/30.",
                   "For 1/12 × 1/18 the whole has 18 rows and 12 columns, 216 parts, and 1 is shaded: 1/216."],
                  "(a) 1/15 (b) 1/12 (c) 1/10 (d) 1/30, and 1/12 × 1/18 = 1/216",
                  tool="unit_square_product"),
          ])]))

# ============================== T4 Numerators and denominators ================================================
TOPICS.append(TOPIC(
    "T4", "M1", "Multiplying Numerators and Denominators", ["8.1"], "Apply",
    "Students state and use Brahmagupta's rule that the product of two fractions has the product of the numerators "
    "over the product of the denominators, including when one of the numbers is a whole number.",
    "Multiply the numerators together and the denominators together; a whole number is a fraction over 1.",
    [A("T4.C1", "Unit fractions: one over the product of the denominators", "Analyze",
       "Students explain why 1/b × 1/d = 1/(b × d) from the rows and columns of the unit square and use it for "
       "1/12 × 1/18.",
       textbook=["Doing this by representing the fractions using a unit square is cumbersome. Let us find the "
                 "product by observing what we did in the above cases.",
                 "In each case, the whole is divided into rows and columns. The number of rows is the denominator "
                 "of the multiplicand, which is 18 in this case. The number of columns is the denominator of the "
                 "multiplier, which is 12 in this case. Thus, the whole is divided into 18 × 12 equal parts.",
                 "So, 1/18 × 1/12 = 1/(18 × 12) = 1/216.",
                 "Thus, when two fractional units are multiplied, their product is 1/(product of denominators). "
                 "We express this as: 1/b × 1/d = 1/(b × d)."],
       teach=["Predict first: how many equal parts does the unit square have for 1/12 × 1/18?",
              "The rows come from one denominator and the columns from the other, so the parts number 12 × 18 = 216.",
              "One part is shaded, so 1/12 × 1/18 = 1/216; in general 1/b × 1/d = 1/(b × d)."],
       examples=[
           WE("Find 1/12 × 1/18 without drawing the unit square.",
              ["The unit square would have 18 rows and 12 columns.",
               "The number of equal parts is 18 × 12 = 216.",
               "One part is shaded, so 1/12 × 1/18 = 1/216.",
               "In general, 1/b × 1/d = 1/(b × d)."],
              "1/216", ncert=["8.1.unit_rule"])],
       key_terms=["numerator", "denominator"], misconceptions=["M_ADD_ACROSS"], minutes=8),
     A("T4.C2", "Brahmagupta's rule: 5/12 × 7/18", "Apply",
       "Students multiply 5/12 by 7/18 by dividing 7/18 into 12 equal parts and taking 5, and state a/b × c/d = "
       "(a × c)/(b × d), first stated by Brahmagupta.",
       textbook=["Multiplying Numerators and Denominators",
                 "Now, find 5/12 × 7/18. Like the previous case, let us find the product by performing the "
                 "multiplication, step by step.",
                 "First, the whole is divided into 18 rows and 12 columns creating 12 × 18 equal parts. The value we "
                 "get by dividing 7/18 into 12 equal parts is 7/(12 × 18).",
                 "Then, we multiply this result by 5 to get the product. This is (5 × 7)/(12 × 18). So, 5/12 × 7/18 "
                 "= (5 × 7)/(12 × 18) = 35/216.",
                 "From this we can see that, in general, a/b × c/d = (a × c)/(b × d).",
                 "This formula was first stated in this general form by Brahmagupta in his Brāhmasphuṭasiddhānta in "
                 "628 CE."],
       teach=["Predict first: what are the top and the bottom of 5/12 × 7/18?",
              "Dividing 7/18 into 12 equal parts gives 7/(12 × 18) = 7/216.",
              "Multiplying by the numerator 5 gives 5 × 7/216 = 35/216.",
              "The rule: multiply the numerators, multiply the denominators, so a/b × c/d = (a × c)/(b × d)."],
       examples=[
           WE("Find 5/12 × 7/18.",
              ["Divide 7/18 into 12 equal parts: the whole has 12 × 18 = 216 equal parts, so one twelfth of 7/18 is "
               "7/216.",
               "Multiply by 5: 5 × 7/216 = 35/216.",
               "So 5/12 × 7/18 = (5 × 7)/(12 × 18) = 35/216.",
               "In general, a/b × c/d = (a × c)/(b × d)."],
              "35/216", ncert=["8.1.five_twelfths", "8.1.brahmagupta_mult"])],
       key_terms=["numerator", "denominator", "Brahmagupta"], misconceptions=["M_ADD_ACROSS"], minutes=10),
     A("T4.C3", "Whole numbers as fractions over 1", "Apply",
       "Students apply the rule when one number is a whole number by writing it as a fraction with denominator 1.",
       textbook=["The formula above works even when the multiplier or multiplicand is a whole number. We can simply "
                 "rewrite the whole number as a fraction with denominator 1. For example, 3 × 3/4 can be written "
                 "3/1 × 3/4 = (3 × 3)/(1 × 4) = 9/4.",
                 "And, 3/5 × 4 can be written 3/5 × 4/1 = (3 × 4)/(5 × 1) = 12/5."],
       teach=["Predict first: what is a whole number as a fraction?",
              "A whole number n is the fraction n/1, so the same rule works.",
              "3 × 3/4 = 3/1 × 3/4 = 9/4 and 3/5 × 4 = 3/5 × 4/1 = 12/5."],
       examples=[
           WE("Find 3 × 3/4.",
              ["Write 3 as 3/1.",
               "3/1 × 3/4 = (3 × 3)/(1 × 4) = 9/4."],
              "9/4, that is 2 1/4", ncert=["8.1.whole_as_fraction"]),
           WE("Find 3/5 × 4.",
              ["Write 4 as 4/1.",
               "3/5 × 4/1 = (3 × 4)/(5 × 1) = 12/5."],
              "12/5, that is 2 2/5", ncert=["8.1.whole_as_fraction"])],
       key_terms=["whole number"], misconceptions=["M_WHOLE_ONLY_TOP"], minutes=8),
     DOER("T4.C4", "Practice: multiply the numerators and the denominators", None, "Apply",
          "Students multiply two fractions by multiplying the numerators and the denominators, and reduce the "
          "answer to its lowest form.",
          ["Multiply the numerators for the top and the denominators for the bottom.",
           "A whole number is a fraction over 1.",
           "Write the answer in its lowest form."],
          items=[
              FIO("8.1.FiOB2", "Figure it Out (two fractions), Q2",
                  "Find the following products. Use a unit square as a whole for representing the fractions and "
                  "carrying out the operations. (a) 2/3 × 4/5 (b) 1/4 × 2/3 (c) 3/5 × 1/2 (d) 4/6 × 3/5",
                  ["(a) 2/3 × 4/5 = (2 × 4)/(3 × 5) = 8/15.",
                   "(b) 1/4 × 2/3 = (1 × 2)/(4 × 3) = 2/12 = 1/6.",
                   "(c) 3/5 × 1/2 = (3 × 1)/(5 × 2) = 3/10.",
                   "(d) 4/6 × 3/5 = (4 × 3)/(6 × 5) = 12/30 = 2/5.",
                   "In the unit square, each product is the shaded parts counted over the rows times the columns."],
                  "(a) 8/15 (b) 1/6 (c) 3/10 (d) 2/5"),
          ])]))
