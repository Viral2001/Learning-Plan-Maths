# -*- coding: utf-8 -*-
"""Topics T9 to T13. T9 to T11 are module M3 (fractions at work); T12 and T13 are module M4 (puzzle, summary)."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T9 Problems with fractions =====================================================
TOPICS.append(TOPIC(
    "T9", "M3", "Problems with Fractions", ["8.3"], "Apply",
    "Students decide whether a story needs a multiplication or a division, write the matching expression, and "
    "solve tea, brick and fountain problems with fractions.",
    "In a story about sharing or fitting, ask which quantity is unknown; write it as a multiplication with a "
    "missing number, then divide by multiplying with the reciprocal.",
    [A("T9.C1", "Milk in each cup of tea", "Apply",
       "Students find the milk in one cup by writing 5 × (milk per cup) = 1/4 and dividing 1/4 by 5 with the "
       "reciprocal of 5.",
       textbook=["8.3 Some Problems Involving Fractions",
                 "Example 3: Leena made 5 cups of tea. She used 1/4 litre of milk for this. How much milk is there "
                 "in each cup of tea?",
                 "Leena used 1/4 litres of milk in 5 cups of tea. So, in 1 cup of tea the volume of milk should be "
                 "1/4 ÷ 5. Writing this as multiplication, we have: 5 × (milk per cup) = 1/4.",
                 "We perform the division as follows as per Brahmagupta's method: The reciprocal of 5 (the divisor) "
                 "is 1/5. Multiplying this reciprocal by the dividend (1/4), we get 1/5 × 1/4 = 1/20. So, each cup "
                 "of tea has 1/20 litre of milk."],
       teach=["Predict first: should each cup have more milk than 1/4 litre, or less?",
              "5 cups share 1/4 litre, so one cup has 1/4 ÷ 5, and 5 × (milk per cup) = 1/4.",
              "The reciprocal of 5 is 1/5, so the milk in one cup is 1/5 × 1/4 = 1/20 litre."],
       examples=[
           WE("Leena made 5 cups of tea with 1/4 litre of milk. How much milk is there in each cup?",
              ["Milk in 5 cups is 1/4 litre, so milk in 1 cup is 1/4 ÷ 5.",
               "As a multiplication: 5 × (milk per cup) = 1/4.",
               "The reciprocal of the divisor 5 is 1/5; multiply the dividend by it: 1/5 × 1/4 = 1/20."],
              "1/20 litre", ncert=["8.3.ex3"])],
       key_terms=["reciprocal"], misconceptions=["M_WRONG_OPERATION"], minutes=8),
     A("T9.C2", "Square bricks from an old geometry text", "Apply",
       "Students find how many square bricks of side 1/5 unit cover 7 1/2 square units, from number of bricks × "
       "area of a brick = total area.",
       textbook=["Example 4: Some of the oldest examples of working with non-unit fractions occur in humanity's "
                 "oldest geometry texts, the Śhulbasūtra. Here is an example from Baudhāyana's Śhulbasūtra "
                 "(c. 800 BCE). Cover an area of 7 1/2 square units with square bricks each of whose sides is "
                 "1/5 units. How many such square bricks are needed?",
                 "Each square brick has an area of 1/5 × 1/5 = 1/25 square units. The total area to be covered is "
                 "7 1/2 sq. units = 15/2 sq. units.",
                 "As (Number of bricks) × (Area of a brick) = Total Area, Number of bricks = 15/2 ÷ (1/25). The "
                 "reciprocal of the divisor is 25. Multiplying the reciprocal by the dividend, we get "
                 "25 × 15/2 = 25 × 15/2 = 375/2."],
       teach=["Predict first: a brick is tiny, so will the number of bricks be a lot more than 7 or about the same?",
              "One brick has area 1/5 × 1/5 = 1/25 square unit.",
              "Number of bricks × area of a brick = total area, so the number is 15/2 ÷ (1/25).",
              "Multiply by the reciprocal 25: 25 × 15/2 = 375/2, which is 187 1/2 bricks."],
       examples=[
           WE("Cover 7 1/2 square units with square bricks of side 1/5 unit. How many bricks are needed?",
              ["Area of one brick = 1/5 × 1/5 = 1/25 square unit.",
               "Total area = 7 1/2 = 15/2 square units.",
               "Number of bricks × 1/25 = 15/2, so the number is 15/2 ÷ (1/25).",
               "The reciprocal of 1/25 is 25: 25 × 15/2 = 375/2."],
              "375/2 bricks, that is 187 1/2", ncert=["8.3.ex4"])],
       key_terms=["area", "reciprocal"], misconceptions=["M_WRONG_OPERATION"], minutes=10),
     A("T9.C3", "Four fountains and a cistern", "Apply",
       "Students find how fast four fountains fill a cistern together by counting how many cisterns each fills in "
       "a day and adding.",
       textbook=["Example 5: This problem was posed by Chaturveda Pṛithūdakasvāmī (c. 860 CE) in his commentary on "
                 "Brahmagupta's book Brāhmasphuṭasiddhānta.",
                 "Four fountains fill a cistern. The first fountain can fill the cistern in a day. The second can "
                 "fill it in half a day. The third can fill it in a quarter of a day. The fourth can fill the "
                 "cistern in one fifth of a day. If they all flow together, in how much time will they fill the "
                 "cistern?",
                 "Let us solve this problem step by step. In a day, the number of times the first fountain will "
                 "fill the cistern is 1 ÷ 1 = 1; the second is 1 ÷ (1/2) = ___; the third is 1 ÷ (1/4) = ___; the "
                 "fourth is 1 ÷ (1/5) = ___.",
                 "The number of times the four fountains together will fill the cistern in a day is 1 + 2 + 4 + 5 "
                 "= 12. Thus, the total time needed by the four fountains to fill the cistern together is 1/12 "
                 "days."],
       teach=["Predict first: will the fountains together take more or less than half a day?",
              "In one day the first fills the cistern 1 time, the second 1 ÷ (1/2) = 2 times, the third 1 ÷ (1/4) = 4 "
              "times, the fourth 1 ÷ (1/5) = 5 times.",
              "Together that is 1 + 2 + 4 + 5 = 12 fillings in one day.",
              "12 fillings in a whole day means one filling takes 1/12 of a day."],
       examples=[
           WE("Four fountains fill a cistern in 1 day, 1/2 day, 1/4 day and 1/5 day respectively. How long do they "
              "take together?",
              ["In a day the first fountain fills the cistern 1 ÷ 1 = 1 time.",
               "The second fills it 1 ÷ (1/2) = 2 times, the third 1 ÷ (1/4) = 4 times, the fourth 1 ÷ (1/5) = 5 times.",
               "Together in a day: 1 + 2 + 4 + 5 = 12 times.",
               "So one filling takes 1/12 of a day."],
              "1/12 of a day", ncert=["8.3.ex5"])],
       key_terms=["cistern"], misconceptions=["M_WRONG_OPERATION"], minutes=10),
     DOER("T9.C4", "Pull it together and do it: multiply or divide?", "operation_chooser", "Apply",
          "Students choose between a multiplication and a division for a story, and solve problems with lace, "
          "ribbon, flour, rotis, a book of Sridharacharya, pages, petrol, journeys and a cake.",
          ["Decide which quantity is unknown and write the story as a multiplication with a missing number.",
           "If the unknown multiplies the given, divide by multiplying with the reciprocal.",
           "Check the size of your answer against the story."],
          items=[
              FIO("8.3.FiOD2", "Figure it Out (problems with fractions), Q2",
                  "For each of the questions below, choose the expression that describes the solution. Then "
                  "simplify it. (a) Maria bought 8 m of lace to decorate the bags she made for school. She used "
                  "1/4 m for each bag and finished the lace. How many bags did she decorate? (i) 8 × 1/4 "
                  "(ii) 1/8 × 1/4 (iii) 8 ÷ (1/4) (iv) 1/4 ÷ 8 (b) 1/2 meter of ribbon is used to make 8 badges. "
                  "What is the length of the ribbon used for each badge? (i) 8 × 1/2 (ii) 1/2 ÷ (1/8) (iii) 8 ÷ (1/2) "
                  "(iv) 1/2 ÷ 8 (c) A baker needs 1/6 kg of flour to make one loaf of bread. He has 5 kg of "
                  "flour. How many loaves of bread can he make? (i) 5 × 1/6 (ii) 1/6 ÷ 5 (iii) 5 ÷ (1/6) "
                  "(iv) 5 × 6/3 ÷ (7/9)",
                  ["(a) The number of bags times 1/4 m is 8 m, so the number of bags is 8 ÷ (1/4), option (iii). "
                   "8 ÷ (1/4) = 8 × 4 = 32.",
                   "(b) 8 badges share 1/2 m, so one badge uses 1/2 ÷ 8, option (iv). 1/2 ÷ 8 = 1/2 × 1/8 = 1/16 m.",
                   "(c) The number of loaves times 1/6 kg is 5 kg, so it is 5 ÷ (1/6), option (iii). "
                   "5 ÷ (1/6) = 5 × 6 = 30."],
                  "(a) 8 ÷ (1/4) = 32 bags (b) 1/2 ÷ 8 = 1/16 m (c) 5 ÷ (1/6) = 30 loaves",
                  tool="operation_chooser"),
              FIO("8.3.FiOD3", "Figure it Out (problems with fractions), Q3",
                  "If 1/4 kg of flour is used to make 12 rotis, how much flour is used to make 6 rotis?",
                  ["One roti uses 1/4 ÷ 12 = 1/4 × 1/12 = 1/48 kg.",
                   "6 rotis use 6 × 1/48 = 1/8 kg. Or: 6 rotis is half of 12 rotis, so half of 1/4 kg is 1/8 kg."],
                  "1/8 kg"),
              FIO("8.3.FiOD4", "Figure it Out (problems with fractions), Q4",
                  "Pāṭīgaṇita, a book written by Sridharacharya in the 9th century CE, mentions this problem: "
                  "\"Friend, after thinking, what sum will be obtained by adding together 1 ÷ (1/6), 1 ÷ (1/10), "
                  "1 ÷ (1/13), 1 ÷ (1/9), and 1 ÷ (1/2)\". What should the friend say?",
                  ["1 ÷ (1/6) = 6, 1 ÷ (1/10) = 10, 1 ÷ (1/13) = 13, 1 ÷ (1/9) = 9, 1 ÷ (1/2) = 2.",
                   "Sum = 6 + 10 + 13 + 9 + 2 = 40."],
                  "40"),
              FIO("8.3.FiOD5", "Figure it Out (problems with fractions), Q5",
                  "Mira is reading a novel that has 400 pages. She read 1/5 of the pages yesterday and 3/10 of "
                  "the pages today. How many more pages does she need to read to finish the novel?",
                  ["Part read: 1/5 + 3/10 = 2/10 + 3/10 = 5/10 = 1/2.",
                   "Part left: 1 − 1/2 = 1/2 of 400 pages = 200 pages."],
                  "200 pages"),
              FIO("8.3.FiOD6", "Figure it Out (problems with fractions), Q6",
                  "A car runs 16 km using 1 litre of petrol. How far will it go using 2 3/4 litres of petrol?",
                  ["2 3/4 litres = 11/4 litres.",
                   "Distance = 16 × 11/4 = 4 × 11 = 44 km."],
                  "44 km"),
              FIO("8.3.FiOD7", "Figure it Out (problems with fractions), Q7",
                  "Amritpal decides on a destination for his vacation. If he takes a train, it will take him "
                  "5 1/6 hours to get there. If he takes a plane, it will take him 1/2 hour. How many hours does "
                  "the plane save?",
                  ["Time saved = 5 1/6 − 1/2 = 31/6 − 3/6 = 28/6 = 14/3.",
                   "14/3 hours is 4 2/3 hours."],
                  "4 2/3 hours"),
              FIO("8.3.FiOD8", "Figure it Out (problems with fractions), Q8",
                  "Mariam's grandmother baked a cake. Mariam and her cousins finished 4/5 of the cake. The "
                  "remaining cake was shared equally by Mariam's three friends. How much of the cake did each "
                  "friend get?",
                  ["Cake remaining: 1 − 4/5 = 1/5.",
                   "Each friend gets 1/5 ÷ 3 = 1/5 × 1/3 = 1/15 of the cake."],
                  "1/15 of the whole cake"),
          ])]))

# ============================== T10 Fractional relations =======================================================
TOPICS.append(TOPIC(
    "T10", "M3", "Fractions of Fractions in a Square", ["8.3"], "Apply",
    "Students find what fraction of a whole square a shaded region covers by taking a fraction of a fraction at "
    "each step, and follow splitting paths of ants.",
    "A shaded part inside a part is found by multiplying the fractions of the steps; the parts of one whole add to "
    "1.",
    [A("T10.C1", "A square with lines drawn inside", "Apply",
       "Students find the shaded fraction of a whole square by finding the red top-right quarter, the yellow "
       "triangle which is half of it, and then 3/4 of the triangle.",
       textbook=["Fractional Relations",
                 "Here is a square with some lines drawn inside (Fig. 8.4). What fraction of area of the whole "
                 "square does the shaded region occupy? There are different ways to solve this problem. Here is one "
                 "of them:",
                 "Let the area of the whole square be 1 square unit. We can see that the top right square (in "
                 "Fig. 8.5), occupies 1/4 of the area of the whole square. Area of red square = 1/4 square units.",
                 "Let us look at this red square. The area of the triangle inside it (coloured yellow) is half the "
                 "area of the red square. So, the area of the yellow triangle = 1/2 × 1/4 = 1/8 square units.",
                 "What fraction of this yellow triangle is shaded? The shaded region occupies 3/4 of the area of "
                 "the yellow triangle. Are you able to see why? The area of shaded part = 3/4 × 1/8 = 3/32 square "
                 "units. Thus, the shaded region occupies 3/32 of the area of the whole square."],
       teach=["Predict first: is the shaded part more or less than 1/8 of the square?",
              "The whole square is 1. The red top-right square is 1/4 of it.",
              "The yellow triangle is half the red square: 1/2 × 1/4 = 1/8.",
              "The shaded part is 3/4 of the triangle: 3/4 × 1/8 = 3/32.",
              "Another way to find a part of a part: multiply the fractions all the way down, 1/4 × 1/2 × 3/4."],
       examples=[
           WE("A square has a red top-right quarter, a yellow triangle inside it that is half of the red square, "
              "and a shaded part that is 3/4 of the triangle. What fraction of the whole square is shaded?",
              ["Area of the whole square = 1 square unit.",
               "Red square = 1/4 of the whole.",
               "Yellow triangle = 1/2 × 1/4 = 1/8.",
               "Shaded part = 3/4 × 1/8 = 3/32."],
              "3/32 of the whole square", ncert=["8.3.fig84"])],
       key_terms=["area"], misconceptions=["M_FRACTION_OF_WHOLE"], minutes=10),
     A("T10.C2", "Two more squares to try", "Apply",
       "Students find the shaded fraction of the big square in two figures by splitting the square into quarters "
       "and halves.",
       textbook=["In each of the figures given below, find the fraction of the big square that the shaded region "
                 "occupies.",
                 "We will solve more interesting problems of this kind in a later chapter."],
       teach=["Predict first: in each figure, can the shaded part be built from halves and quarters of the whole?",
              "Figure (a): the shaded diagonal band is the lower half of the square minus a small corner triangle "
              "of 1/8, so it covers 1/2 − 1/8 = 3/8 of the big square.",
              "Figure (b): split the big square into four equal squares; the diamond sits in one of them and the "
              "two shaded corner triangles are 2 × 1/8 = 1/4 of that square, which is 1/4 × 1/4 = 1/16."],
       examples=[
           WE("A big square is split into four equal squares. In the top-left square a diamond is drawn with "
              "corners at the middles of the sides, and the four corner triangles are the part left over. Two "
              "corner triangles, the ones on the right, are shaded. What fraction of the big square is shaded?",
              ["Each small square is 1/4 of the big square.",
               "The diamond is half of its small square, so the four corner triangles together are the other half.",
               "Each corner triangle is 1/4 of 1/2, which is 1/8 of the small square; two triangles are 1/4 of the "
               "small square.",
               "Shaded part = 1/4 × 1/4 = 1/16 of the big square."],
              "1/16", ncert=["8.3.practice_b"]),
           WE("A big square has one diagonal drawn from its top-left corner to its bottom-right corner. A second line "
              "is drawn parallel to it from the middle of the left side to the middle of the bottom side. The band "
              "between the two parallel lines is shaded. What fraction of the big square is shaded?",
              ["The diagonal cuts the big square into two equal triangles, so the bottom-left triangle is 1/2.",
               "The second line cuts a small corner triangle off the bottom-left corner. Its two short sides are "
               "half the side of the big square, so it is 1/4 of the bottom-left half, which is 1/4 × 1/2 = 1/8 "
               "of the big square.",
               "The band is the bottom-left half minus that small corner triangle: 1/2 − 1/8 = 3/8."],
              "3/8", ncert=["8.3.practice_a"])],
       key_terms=["area"], misconceptions=["M_FRACTION_OF_WHOLE"], minutes=10),
     DOER("T10.C3", "Practice: parts of a square and a colony of ants", "fraction_splitter", "Apply",
          "Students find a shaded fraction of a square and the shares of ants reaching two food sources, by taking "
          "a fraction of a fraction at each split.",
          ["Call the whole 1 and find the fraction at each step.",
           "Multiply the fractions down a path.",
           "Check that the shares of all the paths add to 1."],
          items=[
              FIO("8.3.FiOD10", "Figure it Out (problems with fractions), Q10",
                  "What fraction of the whole square is shaded? (The whole square is cut into four equal squares. "
                  "In the bottom-right square, two lines run from its top corners to its centre and a vertical "
                  "line goes down from the centre. The shaded part is the part left of the vertical line below "
                  "the left line.)",
                  ["The bottom-right square is 1/4 of the whole.",
                   "The two lines from its top corners to its centre cut off a triangle that is half of it: "
                   "1/2 × 1/4 = 1/8 of the whole.",
                   "The vertical line splits that part so that the shaded piece is 3/4 of it: 3/4 × 1/8 = 3/32.",
                   "So 1/4 × 1/2 × 3/4 = 3/32."],
                  "3/32 of the whole square",
                  tool="fraction_splitter"),
              FIO("8.3.FiOD11", "Figure it Out (problems with fractions), Q11",
                  "A colony of ants set out in search of food. As they search, they keep splitting equally at "
                  "each point and reach two food sources, one near a mango tree and another near a sugarcane "
                  "field. What fraction of the original group reached each food source? (At the first split the "
                  "group goes half to a path to the mango tree and half upwards. The second split sends half of "
                  "that group to the mango tree and half upwards. The third split sends the group into four "
                  "equal parts: two go to the mango tree, one goes to the sugarcane field and one goes upwards. "
                  "The last split sends half to the mango tree and half to the sugarcane field.)",
                  ["First split: 1/2 reaches the mango tree and 1/2 goes on.",
                   "Second split: 1/2 × 1/2 = 1/4 reaches the mango tree and 1/4 goes on.",
                   "Third split: the 1/4 splits into four equal parts of 1/16: two parts reach the mango tree, "
                   "one reaches the sugarcane field, and 1/16 goes on.",
                   "Last split: the 1/16 splits into 1/32 for the mango tree and 1/32 for the sugarcane field.",
                   "Mango tree: 1/2 + 1/4 + 2/16 + 1/32 = 16/32 + 8/32 + 4/32 + 1/32 = 29/32.",
                   "Sugarcane field: 1/16 + 1/32 = 3/32. The two add to 1."],
                  "29/32 reached the mango tree and 3/32 reached the sugarcane field"),
          ])]))

# ============================== T11 A dramma-tic donation ======================================================
TOPICS.append(TOPIC(
    "T11", "M3", "A Dramma-tic Donation", ["8.3"], "Apply",
    "Students multiply a chain of fractions to find how many cowrie shells a dramma gift gives, convert a pana and a "
    "cowrie shell into a part of a dinar, and read how Indian mathematicians developed the arithmetic of fractions.",
    "A long chain of fractions is multiplied the same way as two fractions, and coin values convert by multiplying "
    "the fractions along the chain.",
    [A("T11.C1", "How many cowrie shells did the miser give?", "Apply",
       "Students multiply 1/2 × 2/3 × 3/4 × 1/5 × 1/16 × 1/4 to find the fraction of a dramma, then convert to "
       "cowrie shells given that 1 dramma is 1280 cowrie shells.",
       textbook=["A Dramma-tic Donation",
                 "The following problem is translated from Bhāskarāchārya's (Bhāskara II's) book, Līlāvatī, written "
                 "in 1150 CE.",
                 "\"O wise one! A miser gave to a beggar 1/5 of 1/16 of 1/4 of 1/2 of 2/3 of 3/4 of a dramma. If you "
                 "know the mathematics of fractions well, tell me O child, how many cowrie shells were given by "
                 "the miser to the beggar.\"",
                 "Dramma refers to a silver coin used in those times. The tale says that 1 dramma was equivalent to "
                 "1280 cowrie shells. Let's see what fraction of a dramma the person gave: (1/2 × 2/3 × 3/4 × 1/5 "
                 "× 1/16 × 1/4)th part of a dramma.",
                 "Evaluating it gives 6/7680. Upon simplifying to its lowest form, we get 6/7680 = 1/1280. So, one "
                 "cowrie shell was given to the beggar.",
                 "You can see in the answer Bhāskarāchārya's humour! The miser had given the beggar only one coin "
                 "of the least value (cowrie)."],
       teach=["Predict first: a dramma is 1280 cowrie shells, so will the beggar get many shells or few?",
              "Each 'of' is a multiplication: the gift is 1/2 × 2/3 × 3/4 × 1/5 × 1/16 × 1/4 of a dramma.",
              "Cancel the 2s and the 3s: 1/2 × 2/3 × 3/4 is 1/4, and the rest gives 1/4 × 1/5 × 1/16 × 1/4 = 1/1280.",
              "1/1280 of a dramma, and 1 dramma is 1280 cowrie shells, so the beggar got just 1 cowrie shell."],
       examples=[
           WE("A miser gave a beggar 1/5 of 1/16 of 1/4 of 1/2 of 2/3 of 3/4 of a dramma. If 1 dramma equals 1280 "
              "cowrie shells, how many cowrie shells did the beggar get?",
              ["The fraction of a dramma is 1/2 × 2/3 × 3/4 × 1/5 × 1/16 × 1/4.",
               "Multiply the numerators: 1 × 2 × 3 × 1 × 1 × 1 = 6. Multiply the denominators: 2 × 3 × 4 × 5 × 16 "
               "× 4 = 7680.",
               "6/7680 = 1/1280 in lowest form.",
               "1/1280 of 1280 cowrie shells is 1 cowrie shell."],
              "1 cowrie shell", ncert=["8.3.dramma"])],
       key_terms=["dramma", "cowrie"], misconceptions=[], minutes=10),
     A("T11.C2", "From a cowrie shell to a gold dinar", "Apply",
       "Students convert between coins by multiplying unit fractions: a copper pana is 1/48 of a gold dinar, a "
       "cowrie shell is 1/30 of a pana, and a cowrie shell is 1/1440 of a gold dinar.",
       textbook=["Around the 12th century, several types of coins were in use in different kingdoms of the Indian "
                 "subcontinent. Most commonly used were gold coins (called dinars/gadyanas and hunas), silver coins "
                 "(called drammas/tankas), copper coins (called kasus/panas and mashakas), and cowrie shells.",
                 "Gold coins had high value and were used in large transactions and to store wealth. Silver coins "
                 "were more commonly used in everyday transactions. Copper coins had low value and were used in "
                 "smaller transactions. Cowrie shells were the lowest denomination and were used in very small "
                 "transactions and as change.",
                 "If we assume 1 gold dinar = 12 silver drammas, 1 silver dramma = 4 copper panas, 1 copper pana = "
                 "6 mashakas, and 1 pana = 30 cowrie shells, 1 copper pana = 1/48 gold dinar (1/12 × 1/4); "
                 "1 cowrie shell = ____ copper panas; 1 cowrie shell = ____ gold dinar."],
       teach=["Predict first: is a cowrie shell worth more or less than a hundredth of a gold dinar?",
              "1 dinar = 12 drammas and 1 dramma = 4 panas, so 1 pana is 1/4 × 1/12 = 1/48 of a dinar.",
              "1 pana = 30 cowrie shells, so 1 cowrie shell is 1/30 of a pana.",
              "1 cowrie shell is 1/30 of 1/48 of a dinar, which is 1/1440 of a dinar."],
       examples=[
           WE("Take 1 gold dinar = 12 silver drammas, 1 dramma = 4 copper panas and 1 pana = 30 cowrie shells. "
              "How much of a gold dinar is 1 copper pana, and how much is 1 cowrie shell?",
              ["1 pana = 1/4 dramma and 1 dramma = 1/12 dinar, so 1 pana = 1/12 × 1/4 = 1/48 dinar.",
               "1 cowrie shell = 1/30 pana.",
               "1 cowrie shell = 1/30 × 1/48 dinar = 1/1440 dinar."],
              "1 pana = 1/48 dinar; 1 cowrie shell = 1/30 pana = 1/1440 dinar",
              ncert=["8.3.coins"])],
       key_terms=["dinar", "pana"], misconceptions=[], minutes=8),
     A("T11.C3", "How fractions grew in India", "Remember", "",
       textbook=["A Pinch of History",
                 "As you have seen, fractions are an important type of number, playing a critical role in a variety "
                 "of everyday problems that involve sharing and dividing quantities equally. The general notion of "
                 "non-unit fractions as we use them today, equipped with the arithmetic operations of addition, "
                 "subtraction, multiplication, and division, developed largely in India. The ancient Indian "
                 "geometry texts called the Śhulbasūtra, which go back as far as 800 BCE, used general non-unit "
                 "fractions extensively, including performing division of such fractions as we saw in Example 3.",
                 "Fractions even became commonplace in the popular culture of India as far back as 150 BCE, as "
                 "evidenced by an offhand reference to the reduction of fractions to lowest terms in the "
                 "philosophical work of the revered Jain scholar Umasvati.",
                 "General rules for performing arithmetic operations on fractions, in essentially the modern form "
                 "in which we carry them out today, were first codified by Brahmagupta in his Brāhmasphuṭasiddhānta "
                 "in 628 CE. For multiplying general fractions, Brahmagupta wrote: \"Multiplication of two or more "
                 "fractions is obtained by taking the product of the numerators divided by the product of the "
                 "denominators.\" That is, a/b × c/d = (a × c)/(b × d).",
                 "For division of general fractions, Brahmagupta wrote: \"The division of fractions is performed "
                 "by interchanging the numerator and denominator of the divisor; the numerator of the dividend is "
                 "then multiplied by the (new) numerator, and the denominator by the (new) denominator.\" Bhāskara "
                 "II in his book Līlāvatī in 1150 CE clarifies Brahmagupta's statement further in terms of the "
                 "notion of reciprocal: \"Division of one fraction by another is equivalent to multiplication of "
                 "the first fraction by the reciprocal of the second.\" Both of these verses are equivalent to the "
                 "formula a/b ÷ c/d = a/b × d/c = (a × d)/(b × c).",
                 "Bhāskara I, in his 629 CE commentary on Aryabhata's 499 CE work, described the geometric "
                 "interpretation of multiplication of fractions in terms of the division of a square into "
                 "rectangles via equal divisions along the length and breadth (1/5 × 1/4 = 1/20).",
                 "Many other Indian mathematicians, such as Śhrīdharāchārya (c. 750 CE), Mahāvīrāchārya (c. 850 CE), "
                 "Caturveda Pṛithūdakasvāmī (c. 860 CE), and Bhāskara II (c. 1150 CE) developed the usage of "
                 "arithmetic of fractions significantly further.",
                 "The Indian theory of fractions and arithmetic operations on them was transmitted to, and its "
                 "usage developed further by, Arab and African mathematicians such as al-Hassâr (c. 1192 CE) of "
                 "Morocco. The theory was then transmitted to Europe via the Arabs over the next few centuries, "
                 "and came into general use in Europe in only around the 17th century, after which it spread "
                 "worldwide. The theory is indeed indispensable today in modern mathematics."],
       teach=["Fractions with addition, subtraction, multiplication and division grew largely in India.",
              "The old geometry texts, the Shulbasutra, used fractions around 800 BCE.",
              "Brahmagupta wrote the rules for multiplying and dividing fractions in 628 CE; Bhaskara II explained "
              "division through the reciprocal in 1150 CE.",
              "Bhaskara I showed a product of fractions by cutting a square into rectangles.",
              "The theory travelled through Arab and African mathematicians to Europe."],
       ncert=["8.3.history_final"], key_terms=["Brahmagupta", "reciprocal"], enrichment=True, minutes=4),
     DOER("T11.C4", "Practice: a product that gets smaller and smaller", None, "Analyze",
          "Students multiply a chain of fractions of the form 1 − 1/n, notice the pattern, and state a general "
          "rule.",
          ["Write each bracket as a single fraction first.",
           "Cancel across the chain.",
           "Look for what is left."],
          items=[
              FIO("8.3.FiOD12", "Figure it Out (problems with fractions), Q12",
                  "What is 1 − 1/2? (1 − 1/2) × (1 − 1/3)? (1 − 1/2) × (1 − 1/3) × (1 − 1/4) × (1 − 1/5)? "
                  "(1 − 1/2) × (1 − 1/3) × (1 − 1/4) × (1 − 1/5) × (1 − 1/6) × (1 − 1/7) × (1 − 1/8) × (1 − 1/9) "
                  "× (1 − 1/10)? Make a general statement and explain.",
                  ["1 − 1/2 = 1/2.",
                   "(1 − 1/2) × (1 − 1/3) = 1/2 × 2/3 = 1/3.",
                   "(1 − 1/2) × (1 − 1/3) × (1 − 1/4) × (1 − 1/5) = 1/2 × 2/3 × 3/4 × 4/5 = 1/5.",
                   "Up to (1 − 1/10): 1/2 × 2/3 × 3/4 × ... × 9/10 = 1/10.",
                   "Each numerator cancels the denominator before it, so only the first numerator 1 and the last "
                   "denominator remain.",
                   "In general, (1 − 1/2) × (1 − 1/3) × ... × (1 − 1/n) = 1/n."],
                  "1/2, 1/3, 1/5, 1/10; in general the product up to (1 − 1/n) is 1/n"),
          ])]))

# ============================== T12 Puzzle: non-attacking queens ===============================================
TOPICS.append(TOPIC(
    "T12", "M4", "Puzzle: Non-attacking Queens", ["Chess Puzzles"], "Analyze",
    "Students place queens on a chess board so that no two queens attack each other along a row, a column or a "
    "diagonal.",
    "A queen attacks along a row, a column and a diagonal; place queens so that no two attack each other.",
    [A("T12.C1", "Place the queens so none can attack", "Analyze", "",
       textbook=["Chess Puzzles: Non-attacking Queens",
                 "Chess is a popular 2-player strategy game. This game has its origins in India. It is played on an "
                 "8 × 8 chequered grid. There are 2 sets of pieces, black and white, one set for each player. Find "
                 "out how each piece should move and the rules of the game.",
                 "Here is a famous chess-based puzzle. From its current position, a Queen piece can move along the "
                 "horizontal, vertical or diagonal. Place 4 Queens such that no 2 queens attack each other. For "
                 "example, the arrangement shown is not valid as the queens are in the line of attack of each "
                 "other.",
                 "Now, place 8 queens on this 8 × 8 grid so that no 2 queens attack each other!"],
       teach=["A queen attacks along its row, its column and both diagonals.",
              "On a 4 × 4 board, put one queen in each row. One answer has the queens in columns 2, 4, 1, 3 from "
              "the top row to the bottom row; the other is the mirror image, columns 3, 1, 4, 2.",
              "On the 8 × 8 board, one answer has the queens in columns 1, 5, 8, 6, 3, 7, 2, 4 from the top row to "
              "the bottom row."],
       ncert=["puzzle.queens"], enrichment=True, minutes=8),
     DOER("T12.C2", "Practice: place the queens", None, "Analyze", "",
          ["One queen in every row and every column.",
           "Check the diagonals: two queens on one diagonal have the same difference of row and column, or the "
           "same sum."],
          enrichment=True)]))

# ============================== T13 Summary ====================================================================
TOPICS.append(TOPIC(
    "T13", "M4", "Summary: Working with Fractions", ["Summary"], "Remember",
    None,
    "Brahmagupta's rules for multiplying and dividing fractions, cancelling, and how the product and quotient "
    "compare with the numbers used.",
    [A("T13.C1", "What we found about multiplying and dividing fractions", "Remember",
       "Students restate Brahmagupta's formula for multiplication and division of fractions, cancelling common "
       "factors, the reciprocal, and when a product or quotient is greater or less than the number it comes from.",
       textbook=["Summary",
                 "Brahmagupta's formula for multiplication of fractions: a/b × c/d = (a × c)/(b × d).",
                 "When multiplying fractions, if the numerators and denominators have some common factors, we can "
                 "cancel them first before multiplying the numerators and denominators.",
                 "In multiplication, when one of the numbers being multiplied is between 0 and 1, the product is "
                 "less than the other number. If one of the numbers being multiplied is greater than 1, then the "
                 "product is greater than the other number.",
                 "The reciprocal of a fraction a/b is b/a. When we multiply a fraction by its reciprocal, the "
                 "product is 1.",
                 "Brahmagupta's formula for division of fractions: a/b ÷ c/d = a/b × d/c = (a × d)/(b × c).",
                 "In division, when the divisor is between 0 and 1, the quotient is greater than the dividend. "
                 "When the divisor is greater than 1, the quotient is less than the dividend."],
       teach=["Our opening question is settled: the tortoise walks 1/2 × 1/4 = 1/8 km in half an hour.",
              "Multiply the tops and the bottoms; cancel common factors first; divide by multiplying with the "
              "reciprocal of the divisor.",
              "Still open for you: if a tortoise walks 1/4 km in an hour, how long does it take to walk 1/16 km?"],
       ncert=["summary"], video_focus=["RECAP"], minutes=8)],
    topic_type="summary"))
