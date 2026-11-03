# -*- coding: utf-8 -*-
"""Topics T10 and T11 (module M3): Travelling in Different Vehicles, and Finding Large Numbers Around Us.
T10.C1 is a real teaching concept (it replaces the priority doc's short recap video). Every number is checked in the
self-check; every real-world number is the book's, every WE number is the plan's own practice value."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T10 Travelling in Different Vehicles ========================================
TOPICS.append(TOPIC(
    "T10", "M3", "Travelling in Different Vehicles", ["Travelling, Now and Then"], "Apply",
    "Students describe how people travelled then and now, read how far each means of travel goes in one hour, and "
    "find the distance covered in several hours and the number of vehicles needed for a group.",
    "People travelled on foot, on animals and in boats long ago, and now they use cycles, cars, trains, ships, "
    "aeroplanes and spacecraft. The book gives how far a person generally travels in one hour, from a 1-digit number "
    "to a 5-digit number of kilometres. The distance in many hours is the distance in one hour times the number of "
    "hours, and the vehicles needed for a group are the people divided by the people in one vehicle.",
    [A("T10.C1", "Travelling, Now and Then", "Understand",
       "Students match a travel condition, such as a desert, a snow-covered hill, deep water or outer space, to the "
       "animal or vehicle that the book names for it.",
       textbook=["We learnt that people in the past travelled on foot, on animals, and used boats and sailing ships. "
                 "The animals that have been used for travelling include bullocks, horses, donkeys, mules, and "
                 "elephants. In hilly and snow-covered regions, yaks, dogs, and reindeers have been used, while camels "
                 "have been used in deserts.",
                 "Now, people use bicycles, motorbikes, cars, buses, trains, ships, and aeroplanes to travel from one "
                 "place to another. Submarines are used to go deep under water. Humans are also using spacecraft to "
                 "travel to outer space."],
       teach=["Predict first: you must cross a desert and your friend must cross a snow-covered hill. Which animal "
              "would each of you choose?",
              "In the past, people travelled on foot, on animals, and in boats and sailing ships. Bullocks, horses, "
              "donkeys, mules and elephants have carried people.",
              "Camels have been used in deserts. Yaks, dogs and reindeer have been used in hilly and snow-covered "
              "regions.",
              "Now, people use bicycles, motorbikes, cars, buses, trains, ships and aeroplanes. Submarines go deep "
              "under water, and spacecraft take humans to outer space.",
              "Rule: the place we want to travel in decides which animal or vehicle we use."],
       examples=[WE("Mira makes a travel card for four places. Which means of travel from the book fits each place? "
                    "(a) crossing water in the past, (b) a desert, (c) deep under water, (d) outer space.",
                    ["(a) Crossing water in the past: people used boats and sailing ships.",
                     "(b) A desert: camels have been used in deserts.",
                     "(c) Deep under water: submarines are used to go deep under water.",
                     "(d) Outer space: humans use spacecraft to travel to outer space.",
                     "Check: each answer names a place from the book and its own means of travel."],
                    "(a) boats and sailing ships, (b) camels, (c) submarines, (d) spacecraft")],
       ncert=["tr.now_then"],
       key_terms=["travel", "transport", "past"], minutes=6),

     A("T10.C2", "How far in one hour?", "Apply",
       "Students read how far a person generally travels in one hour by each means of travel, say how many digits the "
       "distance has, and find which means can cover a given distance in an hour.",
       textbook=["In an hour a person can generally travel",
                 "(a) 3 to 5 km on foot.",
                 "(b) 10 to 15 km on horseback.",
                 "(c) 12 to 20 km by cycle.",
                 "(d) 40 to 60 km by motorbike.",
                 "(e) 40 to 160 km by train.",
                 "(f) 25 to 45 km by ship.",
                 "(g) 750 to 920 km by aircraft.",
                 "(h) minimum 28,000 km by spacecraft.",
                 "Usually, we measure distances in sea and air using nautical miles. For now, we will use 1 km = "
                 "1,000 m. By now, you know different units of measuring length. We will study the units for "
                 "measuring length, kilometre, in detail in a later chapter."],
       teach=["Predict first: in one hour, how far can a person go on foot, and how far in a spacecraft? Guess one "
              "number for each.",
              "The book says a person can generally travel 3 to 5 km on foot, 10 to 15 km on horseback, 12 to 20 km "
              "by cycle and 40 to 60 km by motorbike in an hour.",
              "By train 40 to 160 km, by ship 25 to 45 km and by aircraft 750 to 920 km. By spacecraft the minimum is "
              "28,000 km.",
              "So the distance in an hour runs from a 1-digit number, 3 km on foot, to a 5-digit number, 28,000 km by "
              "spacecraft.",
              "At sea and in the air, distances are usually measured in nautical miles. For now we use kilometres, and "
              "1 km = 1,000 m.",
              "Rule: a distance fits a means of travel when it is at least the first number and at most the last "
              "number of its range."],
       examples=[WE("Suppose a traveller covers 50 km in one hour. Which means of travel in the book's list can do "
                    "that, and how many digits does 50 have?",
                    ["A means fits when 50 is at least its first number and at most its last number.",
                     "On foot (3 to 5), on horseback (10 to 15), by cycle (12 to 20) and by ship (25 to 45): 50 is "
                     "more than the last number each time, so none fits.",
                     "By aircraft (750 to 920) and by spacecraft (minimum 28,000): 50 is less than the first number, "
                     "so neither fits.",
                     "By motorbike (40 to 60): 40 is less than 50 and 50 is less than 60, so it fits.",
                     "By train (40 to 160): 40 is less than 50 and 50 is less than 160, so it fits.",
                     "50 has 2 digits."],
                    "A motorbike or a train; 50 is a 2-digit number")],
       ncert=["tr.speeds", "tr.note"],
       key_terms=["distance", "kilometre", "hour", "range"], minutes=7),

     A("T10.C3", "How many vehicles for a group?", "Apply",
       "Students find the number of vehicles needed for a group by dividing the number of people by the number of "
       "people one vehicle carries, and check the answer by multiplying.",
       teach=["Predict first: 12 children go on a trip in cars that carry 4 children each. How many cars do they "
              "need, 3, 4 or 8?",
              "Each car takes 4 children. Count in 4s: 4, 8, 12. That is 3 cars, and 12 ÷ 4 = 3.",
              "The number of vehicles is the number of people divided by the number of people in one vehicle.",
              "A vehicle that carries more people needs fewer vehicles. The same 12 children need 3 cars of 4, but "
              "only 2 big cars of 6, because 12 ÷ 6 = 2.",
              "Check by multiplying: 3 × 4 = 12 and 2 × 6 = 12.",
              "Rule: divide the people by the number one vehicle carries, then check by multiplying."],
       examples=[WE("A group of 120 people goes on a trip. How many vehicles are needed if each car carries 4 people? "
                    "How many if each big car carries 6 people?",
                    ["People in the group: 120. People in one car: 4.",
                     "Cars needed: 120 ÷ 4 = 30.",
                     "Check: 30 × 4 = 120, so 30 cars carry all 120 people.",
                     "People in one big car: 6. Big cars needed: 120 ÷ 6 = 20.",
                     "Check: 20 × 6 = 120, so 20 big cars carry all 120 people.",
                     "A big car carries more people, so fewer vehicles are needed."],
                    "30 cars, or 20 big cars")],
       key_terms=["vehicles", "group", "divide"], minutes=6),

     DOER("T10.C4", "Practice: Transport Explorer", "transport_explorer", "Apply",
          "Students use the book's distances and vehicle sizes on a transport map to find how far a cyclist goes in "
          "4 hours and how many vehicles carry 900 people, and check each answer.",
          ["The distance in many hours is the distance in one hour times the number of hours.",
           "The vehicles needed are the number of people divided by the number of people in one vehicle.",
           "A vehicle that carries more people means fewer vehicles are needed."],
          items=[FIO("LUDb.Q1", "Let Us Do (travelling), Q1 cyclist",
                     "A cyclist can cover 15 km in one hour. How much distance will she cover in 4 hours, if she "
                     "maintains the same speed?",
                     ["In 1 hour the cyclist covers 15 km.",
                      "In 2 hours: 15 + 15 = 30 km.",
                      "In 3 hours: 30 + 15 = 45 km.",
                      "In 4 hours: 45 + 15 = 60 km.",
                      "Check by multiplying: 15 × 4 = 60 km."],
                     "60 km",
                     q_figure="A cyclist at the start of a straight road that is divided into 4 equal stretches, one "
                              "for each hour, with the first stretch marked 15 km.",
                     s_figure="The same road with the end of each hour marked 0, 15, 30, 45 and 60 km."),
                 FIO("LUDb.Q2ad", "Let Us Do (travelling), Q2 (a) to (d) vehicles",
                     "A school has 461 girls and 439 boys. How many vehicles are needed for all of them to go on a "
                     "trip using the following modes of travel? The numbers in the bracket indicate the number of "
                     "people that can travel in one vehicle. (a) Bicycle (2) (b) Autorickshaw (3) (c) Car (4) "
                     "(d) Big car (6)",
                     ["Add the girls and the boys: 461 + 439 = 900 people.",
                      "Vehicles needed = 900 ÷ the number of people in one vehicle.",
                      "(a) Bicycle: 900 ÷ 2 = 450.",
                      "(b) Autorickshaw: 900 ÷ 3 = 300.",
                      "(c) Car: 900 ÷ 4 = 225.",
                      "(d) Big car: 900 ÷ 6 = 150.",
                      "Check: 450 × 2 = 900, 300 × 3 = 900, 225 × 4 = 900 and 150 × 6 = 900."],
                     "(a) 450 (b) 300 (c) 225 (d) 150",
                     q_figure="A school group of 461 girls and 439 boys beside four vehicles, a bicycle marked 2, an "
                              "autorickshaw marked 3, a car marked 4 and a big car marked 6, each mark showing the "
                              "people in one vehicle.",
                     s_figure="The 900 people as equal groups for each vehicle: 450 groups of 2, 300 groups of 3, "
                              "225 groups of 4 and 150 groups of 6."),
                 FIO("LUDb.Q2eh", "Let Us Do (travelling), Q2 (e) to (h) vehicles",
                     "A school has 461 girls and 439 boys. How many vehicles are needed for all of them to go on a "
                     "trip using the following modes of travel? The numbers in the bracket indicate the number of "
                     "people that can travel in one vehicle. (e) Tempo traveller (10) (f) Boat (20) (g) Minibus (25) "
                     "(h) Aeroplane (180)",
                     ["The school has 461 + 439 = 900 people, as before.",
                      "(e) Tempo traveller: 900 ÷ 10 = 90.",
                      "(f) Boat: 900 ÷ 20 = 45.",
                      "(g) Minibus: 900 ÷ 25 = 36.",
                      "(h) Aeroplane: 900 ÷ 180 = 5.",
                      "Check: 90 × 10 = 900, 45 × 20 = 900, 36 × 25 = 900 and 5 × 180 = 900."],
                     "(e) 90 (f) 45 (g) 36 (h) 5",
                     q_figure="A school group of 461 girls and 439 boys beside four vehicles, a tempo traveller "
                              "marked 10, a boat marked 20, a minibus marked 25 and an aeroplane marked 180.",
                     s_figure="The 900 people as equal groups for each vehicle: 90 groups of 10, 45 groups of 20, "
                              "36 groups of 25 and 5 groups of 180.")])],
    key_terms=["travel", "distance", "vehicles"]))

# ============================== T11 Finding Large Numbers Around Us ========================================
TOPICS.append(TOPIC(
    "T11", "M3", "Finding Large Numbers Around Us", ["Finding Large Numbers Around Us"], "Apply",
    "Students estimate large counts around them by multiplying the count in one part by the number of parts, and "
    "find things in a book, a classroom, a tree and a town whose counts are 4-digit or 5-digit numbers.",
    "Large numbers are not only about travel. When we count one small part and multiply by the number of parts, we "
    "can find a big count without counting one by one, and then say how many digits it has.",
    [A("T11.C1", "Where do large numbers hide?", "Apply",
       "Students estimate a large count around them by multiplying the count in one part by the number of parts, and "
       "say whether the count is a 4-digit or a 5-digit number.",
       textbook=["We saw that the distance (in kilometre) covered by different means of transport in an hour can "
                 "range from a 1-digit number to a 5-digit number. Can we find other contexts around us that contain "
                 "numbers in this range? Let us consider the situation below.",
                 "Now, let us try this with our school.",
                 "(a) Our school has ________ classrooms.",
                 "(b) There are ________ students in my class.",
                 "(c) Our classroom has ________ books in total."],
       teach=["Predict first: a box holds 40 sheets of stickers and each sheet has 100 stickers. Will the number of "
              "stickers have 3 digits, 4 digits or 5 digits?",
              "The distances in an hour that we met run from a 1-digit number, 3 km on foot, to a 5-digit number, "
              "at least 28,000 km by spacecraft. Large numbers hide in many other places too.",
              "Count one small part, then multiply by the number of parts. The stickers are 100 × 40 = 4,000, a "
              "4-digit number.",
              "Now try it with your school: our school has ___ classrooms, there are ___ students in my class, and "
              "our classroom has ___ books in total. Say how many digits each count has.",
              "Rule: count one small part, multiply by the number of parts, then count the digits."],
       examples=[WE("Suppose each sheet has 100 stickers and a box holds 40 sheets. How many stickers are in the box? "
                    "Is the count a 4-digit or a 5-digit number?",
                    ["One sheet has 100 stickers.",
                     "10 sheets have 100 × 10 = 1,000 stickers.",
                     "40 sheets are 4 groups of 10 sheets: 4 × 1,000 = 4,000 stickers.",
                     "Check: 100 × 40 = 4,000.",
                     "4,000 has 4 digits, so the count is a 4-digit number."],
                    "4,000 stickers, a 4-digit number")],
       ncert=["ar.intro", "ar.school"],
       key_terms=["estimate", "count", "digits"], minutes=6),

     DOER("T11.C2", "Pull it together and do it: Large Numbers Around Us", None, "Apply",
          "Students find things in a book, a classroom, a tree and a town whose counts are 4-digit or 5-digit "
          "numbers, and explain each count by grouping and multiplying.",
          ["Count one small part, then multiply by the number of parts.",
           "A 4-digit count is from 1,000 to 9,999. A 5-digit count is from 10,000 to 99,999.",
           "These are estimates, so your answer may differ."],
          items=[FIO("ar.book", "Finding Large Numbers Around Us, Example (words in a book)",
                     "A book has around 200 pages, and each page has about 50 words. About how many words does the "
                     "book have in all?",
                     ["The book has about 200 pages.",
                      "Each page has about 50 words.",
                      "100 pages have 100 × 50 = 5,000 words.",
                      "200 pages are 2 times as many: 5,000 × 2 = 10,000 words.",
                      "Check: 200 × 50 = 10,000, and 10,000 has 5 digits."],
                     "About 10,000 words, a 5-digit number",
                     kind="example",
                     q_figure="An open book with the labels: about 200 pages in the book, about 50 words on each "
                              "page.",
                     s_figure="Two stacks of 100 pages, each stack holding 5,000 words, joined to make 10,000 "
                              "words."),
                 FIO("ar.mathsbook", "Finding Large Numbers Around Us, Try It (maths book)",
                     "Find something in the maths book whose count is a 4-digit number.",
                     ["Pick a thing to count: the words in one chapter of the maths book.",
                      "Estimate one part: a page has about 150 words.",
                      "Count the parts: the chapter has about 16 pages.",
                      "10 pages have 10 × 150 = 1,500 words.",
                      "6 pages have 6 × 150 = 900 words.",
                      "Add the parts: 1,500 + 900 = 2,400 words.",
                      "Check: 2,400 has 4 digits, so it is a 4-digit number."],
                     "Sample answer: the words in one chapter, about 2,400 (16 pages with about 150 words each), a "
                     "4-digit number. Your answer may differ.",
                     kind="prompt"),
                 FIO("ar.classroom", "Finding Large Numbers Around Us, Try It (classroom)",
                     "Find something in the classroom whose count is a (i) 4-digit number (ii) 5-digit number.",
                     ["(i) Count the pages in one notebook from each child. Suppose the class has 40 children and a "
                      "notebook has about 100 pages.",
                      "10 notebooks have 10 × 100 = 1,000 pages.",
                      "40 notebooks are 4 groups of 10: 4 × 1,000 = 4,000 pages, a 4-digit number.",
                      "(ii) Count all the notebooks. Suppose each child has 5 notebooks: 40 × 5 = 200 notebooks.",
                      "200 notebooks with about 100 pages each: 200 × 100 = 20,000 pages, a 5-digit number.",
                      "Check the digits: 4,000 has 4 digits and 20,000 has 5 digits."],
                     "Sample answer: (i) pages in 40 notebooks, about 4,000, a 4-digit number; (ii) pages in 200 "
                     "notebooks, about 20,000, a 5-digit number. Your answer may differ.",
                     kind="prompt"),
                 FIO("ar.tree_village", "Finding Large Numbers Around Us, Try It (tree, village or town)",
                     "List some quantities whose count is a 4-digit or a 5-digit number in the context of (i) a tree "
                     "(ii) your village/town/city, or any other place of your choice.",
                     ["(i) A tree: count the leaves. Suppose a twig has 30 leaves and the tree has 90 twigs.",
                      "10 twigs have 30 × 10 = 300 leaves.",
                      "90 twigs are 9 groups of 10 twigs: 300 × 9 = 2,700 leaves, a 4-digit number.",
                      "A garden of 10 such trees has 2,700 × 10 = 27,000 leaves, a 5-digit number.",
                      "(ii) A town: count the windows. Suppose a street has 50 houses and a house has 4 windows: "
                      "50 × 4 = 200 windows on a street.",
                      "30 streets have 200 × 30 = 6,000 windows, a 4-digit number.",
                      "100 streets have 200 × 100 = 20,000 windows, a 5-digit number.",
                      "Check the digits: 2,700 and 6,000 have 4 digits; 27,000 and 20,000 have 5 digits."],
                     "Sample answer: (i) leaves on a tree, about 2,700 (4-digit), and in a garden of 10 trees, about "
                     "27,000 (5-digit); (ii) windows in a town, about 6,000 (4-digit) or 20,000 (5-digit). Your "
                     "answer may differ.",
                     kind="prompt")])],
    key_terms=["estimate", "count", "digits"]))
