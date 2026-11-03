# -*- coding: utf-8 -*-
"""Topics T10 to T13 (module M3). Large numbers around us, Pastime Mathematics (river crossing, pile of pebbles, Mira's
puzzle), the King's Horses, and the chapter summary."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T10 Finding large numbers around us ========================================
TOPICS.append(TOPIC(
    "T10", "M3", "Finding Large Numbers Around Us", ["Finding Large Numbers Around Us"], "Apply",
    "Students estimate the count of a thing from a part and a number of parts, and find 4-digit and 5-digit counts in "
    "the school, the classroom, a tree and a village.",
    "Large counts are everywhere. A book with 200 pages and about 50 words on each page has about 10,000 words. "
    "Counting a part and multiplying finds a big number quickly.",
    [A("T10.C1", "How many words in a book?", "Understand",
       "Students estimate the number of words in a book from the pages and words on a page, getting a 5-digit number.",
       textbook=["We saw that the distance (in kilometre) covered by different means of transport in an hour can range "
                 "from a 1-digit number to a 5-digit number. Can we find other contexts around us that contain numbers "
                 "in this range?",
                 "A book has around 200 pages, and each page has about 50 words. The book therefore has about 10,000 "
                 "words in all.",
                 "Find something in the textbook whose count is a 4-digit number."],
       teach=["Predict first: a book has about 200 pages and about 50 words on each page. About how many words is that?",
              "50 words on 1 page, 100 on 2 pages, 500 on 10 pages, 5,000 on 100 pages, so 10,000 on 200 pages.",
              "200 × 50 = 10,000. When we count a small part and multiply, we do not need to count every word."],
       examples=[WE("A book has around 200 pages and each page has about 50 words. About how many words are in the book?",
                    ["100 pages have 100 × 50 = 5,000 words.",
                     "200 pages are 2 times as many: 5,000 × 2 = 10,000 words.",
                     "10,000 is a 5-digit number."],
                    "About 10,000 words, a 5-digit number",
                    ncert=["ar.book"])],
       key_terms=["estimate", "about"], minutes=6),
     A("T10.C2", "Counts in school, classroom, tree and village", "Apply",
       "Students name quantities in the school, the classroom, a tree and their village or town whose counts are "
       "4-digit or 5-digit numbers.",
       teach=["Predict first: is the number of leaves on a big tree a 2-digit, 4-digit or 5-digit number?",
              "Ask how many classrooms, students in a class, and books in a classroom, and use a part to estimate the "
              "whole.",
              "For a tree, count the leaves on one branch and multiply by the number of branches.",
              "For a village or town, think of people, houses, or vehicles."],
       examples=[WE("A branch has about 150 leaves and a tree has about 40 such branches. About how many leaves does "
                    "the tree have?",
                    ["150 leaves on 1 branch.",
                     "40 branches: 150 × 40 = 6,000.",
                     "6,000 is a 4-digit number."],
                    "About 6,000 leaves, a 4-digit number")],
       key_terms=["estimate", "count"], minutes=6),
     DOER("T10.C3", "Practice: find the big counts", None, "Apply",
          "Students name and estimate 4-digit and 5-digit counts in their school, classroom, a tree and a village.",
          ["A part times the number of parts estimates a big count.",
           "A 4-digit count is from 1,000 to 9,999 and a 5-digit count is from 10,000 to 99,999.",
           "Many answers are right when they are reasoned."],
          examples=[WE("Your turn: a classroom shelf has about 40 books and there are 30 such shelves in the school "
                       "library. About how many books are in the library, and how many digits does it have?",
                       ["40 books on 1 shelf, 30 shelves.",
                        "40 × 30 = 1,200."],
                       "About 1,200 books, a 4-digit number")],
          items=[FIO("ar.school", "Finding large numbers, our school",
                     "Our school has __ classrooms. There are __ students in my class. Our classroom has __ books in "
                     "total.",
                     ["A sample school has 24 classrooms.",
                      "A sample class has 40 students.",
                      "A sample classroom has 120 books in total."],
                     "Sample answer: 24 classrooms, 40 students, 120 books in a classroom (answers will differ)"),
                 FIO("ar.classroom", "Finding large numbers, the classroom",
                     "Find something in the classroom whose count is a (i) 4-digit number (ii) 5-digit number.",
                     ["(i) The number of pages in the notebooks of the class: 40 notebooks with 100 pages is 4,000, a "
                      "4-digit number.",
                      "(ii) The number of words in the textbook: about 100 pages with 120 words a page is 12,000 words, "
                      "a 5-digit number."],
                     "Sample answer: pages in notebooks, 4,000 (4-digit); words in a textbook, 12,000 (5-digit)"),
                 FIO("ar.tree_village", "Finding large numbers, a tree and a village",
                     "List some quantities whose count is a 4-digit or a 5-digit number in the context of (i) a tree "
                     "(ii) your village, town or city, or any other place of your choice.",
                     ["(i) Leaves on a tree: about 6,000, a 4-digit number. Leaves on a big banyan tree: more than "
                      "10,000, a 5-digit number.",
                      "(ii) People in a village: about 2,500, a 4-digit number. Vehicles in a town: about 15,000, a "
                      "5-digit number."],
                     "Sample answer: leaves on a tree, 6,000; people in a village, 2,500; vehicles in a town, 15,000 "
                     "(answers will differ)")])],
    key_terms=["estimate", "4-digit", "5-digit"]))

# ============================== T11 Pastime mathematics ====================================================
TOPICS.append(TOPIC(
    "T11", "M3", "Pastime Mathematics: Puzzles on the Train", ["Pastime Mathematics"], "Analyze",
    "Students solve the river crossing puzzle, find the winning strategy of the pile of pebbles, and explain why "
    "Mira's two-digit subtraction puzzle always ends in 9.",
    "Puzzles train us to think logically and strategically. The river crossing needs the right order, the pebbles game "
    "needs a mirror strategy, and Mira's puzzle always ends in 9 because every difference is a multiple of 9.",
    [A("T11.C1", "The river crossing", "Analyze",
       "Students plan the trips of a boatman who must carry a lion, a sheep and a bundle of grass across a river safely "
       "in the fewest trips.",
       textbook=["Sanju and Mira are traveling on a train. To pass time, they challenge each other with games and "
                 "puzzles.",
                 "Mira poses the river crossing puzzle to Sanju. A boatman wants to cross a river in a boat. He has to "
                 "take a lion, a sheep, and a bundle of grass with him. He can take one of them at a time. If the sheep "
                 "and grass are left on the shore, the sheep will eat the grass. And, if the sheep and lion are left on "
                 "the shore, the lion will eat the sheep.",
                 "How can the boatman take the lion, sheep, and grass across the river? Help him so that he can ferry "
                 "the lion, sheep, and grass across the river safely, and in the minimum number of trips."],
       teach=["Predict first: which of the three should the boatman take first, so that nothing is eaten?",
              "The sheep is the problem: it cannot be left with the grass, and it cannot be left with the lion.",
              "Take the sheep first. The lion and the grass can be left together, because the lion does not eat grass.",
              "Then bring something back so that the sheep is never alone with the lion or the grass."],
       examples=[WE("How can the boatman take the lion, the sheep and the grass across the river safely in the fewest "
                    "trips?",
                    ["Trip 1: take the sheep across. The lion and the grass are safe together on the first shore.",
                     "Trip 2: come back alone. Trip 3: take the lion across. The lion and the sheep cannot be left "
                     "together when the boatman leaves.",
                     "Trip 4: bring the sheep back. Trip 5: take the grass across. The lion and the grass are safe "
                     "together on the far shore.",
                     "Trip 6: come back alone. Trip 7: take the sheep across.",
                     "Seven crossings in all: sheep, back, lion, sheep back, grass, back, sheep."],
                    "Take the sheep, return, take the lion, bring the sheep back, take the grass, return, take the "
                    "sheep: 7 crossings",
                    ncert=["pm.river"])],
       key_terms=["puzzle", "trip"], minutes=8, enrichment=True),
     A("T11.C2", "The pile of pebbles", "Analyze",
       "Students find a winning strategy for two equal piles of pebbles by trying small piles and then mirroring the "
       "other player's move.",
       textbook=["Sanju introduces a game called pile of pebbles to Mira.",
                 "There are two piles of pebbles. Each pile contains 7 pebbles. Each player can pick as many pebbles "
                 "they want from either of the piles. The player who picks the last pebble wins.",
                 "Try this game with your friends. Now, how do you play so that you win?",
                 "To find a winning strategy, try playing with 1 pebble in each pile, two in each, three in each, and so "
                 "on."],
       teach=["Predict first: with two piles of 1 pebble each, does the first player or the second player win?",
              "With 1 and 1: the first player takes one pile, the second takes the last pebble and wins.",
              "With 2 and 2, 3 and 3, and so on, the second player wins by copying: whatever the first player takes "
              "from one pile, take the same amount from the other pile.",
              "Equal piles always stay equal after the second player's move, and the second player takes the last "
              "pebble."],
       examples=[WE("Two piles have 7 pebbles each. You play second. The first player takes 3 from the first pile. What "
                    "do you do, and who wins?",
                    ["Mirror the move: take 3 from the other pile. Now the piles are 4 and 4.",
                     "If the first player takes 4 from a pile, take 4 from the other: 0 and 0 and you win.",
                     "Equal piles after your move, every time, so you take the last pebble."],
                    "Take the same number from the other pile; the second player wins",
                    ncert=["pm.pebbles"])],
       key_terms=["strategy", "mirror"], minutes=8, enrichment=True),
     A("T11.C3", "Mira's puzzle that always ends in 9", "Analyze",
       "Students follow Mira's steps, record the digits, the difference of the digits and the difference of the "
       "numbers, and see that every difference is 9 times the difference of the digits.",
       textbook=["Now, it's Mira's turn. She gives a fun puzzle to Sanju with the following steps: (a) Take any two "
                 "different digits. For example 3 and 7. (b) Make two 2-digit numbers using them: 37 and 73. (c) "
                 "Subtract the smaller number from the bigger number: 73 − 37 = 36.",
                 "Now, use the two digits in the difference and repeat steps (b) and (c). Continue this process until you "
                 "get a 1-digit number. Even before everyone could finish, Mira exclaimed, \"Mind you! No matter which "
                 "two numbers you choose, you will get 9 in the end.\"",
                 "How did Mira know what the 1-digit number in the end would be? Let us explore."],
       teach=["Predict first: take 3 and 7. What do you think you will get at the end?",
              "73 − 37 = 36. Use 3 and 6: 63 − 36 = 27. Use 2 and 7: 72 − 27 = 45. Use 4 and 5: 54 − 45 = 9.",
              "Look at the differences: 36, 27, 45, 9. All are in the table of 9.",
              "The reason: the difference of the numbers is 9 times the difference of the digits. For 3 and 7, the "
              "digits differ by 4, and 36 is 9 times 4."],
       examples=[WE("Follow Mira's steps for the digits 3 and 7 and say why each difference is a multiple of 9.",
                    ["73 − 37 = 36, and 36 = 9 × 4, where 7 − 3 = 4.",
                     "63 − 36 = 27, and 27 = 9 × 3, where 6 − 3 = 3.",
                     "72 − 27 = 45, and 45 = 9 × 5, where 7 − 2 = 5.",
                     "54 − 45 = 9, and 9 = 9 × 1, where 5 − 4 = 1."],
                    "73 − 37 = 36, 63 − 36 = 27, 72 − 27 = 45 and 54 − 45 = 9; every difference is 9 times the "
                    "difference of the digits",
                    ncert=["pm.mira_steps"])],
       key_terms=["difference", "multiple of 9"], misconceptions=["M_DIGIT_DIFF"], minutes=9),
     DOER("T11.C4", "Practice: run the digit difference machine", "digit_difference_machine", "Analyze",
          "Students run Mira's process on different pairs of digits, fill the table of digits and differences, and "
          "explain why the answer is always 9.",
          ["Each difference of the numbers is 9 times the difference of the digits.",
           "A 1-digit answer in the first step needs digits that differ by 1.",
           "The process always ends in 9."],
          items=[FIO("pm.mira_explore", "Mira's puzzle, explore (1) to (4)",
                     "Observe the differences in each step. Try the puzzle using another pair of digits. What digits "
                     "give a 1-digit number in the first step itself? Find different digits such that the difference "
                     "between the numbers is 27.",
                     ["(1) 36, 27, 45 and 9 are all in the table of 9.",
                      "(2) Digits 2 and 8: 82 − 28 = 54, then 54 − 45 = 9. The differences are multiples of 9 and the "
                      "end is 9.",
                      "(3) Digits that are next to each other, like 4 and 5: 54 − 45 = 9. Their difference is 1.",
                      "(4) 27 = 9 × 3, so the digits must differ by 3: 1 and 4, 2 and 5, 3 and 6, 4 and 7, 5 and 8, 6 "
                      "and 9, 0 and 3."],
                     "(1) all in the table of 9 (2) ends in 9 (3) digits that differ by 1, such as 4 and 5 (4) digits "
                     "that differ by 3, such as 2 and 5"),
                 FIO("pm.mira_table", "Mira's puzzle, extend the table",
                     "Extend Mira's table by choosing digits so that the resulting differences are 2, 3, 5 and 7.",
                     ["Difference 2: digits 1 and 3, 3 − 1 = 2, 31 − 13 = 18.",
                      "Difference 3: digits 2 and 5, 5 − 2 = 3, 52 − 25 = 27.",
                      "Difference 5: digits 1 and 6, 6 − 1 = 5, 61 − 16 = 45.",
                      "Difference 7: digits 2 and 9, 9 − 2 = 7, 92 − 29 = 63."],
                     "1, 3: 18. 2, 5: 27. 1, 6: 45. 2, 9: 63"),
                 FIO("pm.mira_asks", "Mira's puzzle, the three questions",
                     "What do the differences between the digits indicate? List the numbers that give a 1-digit number "
                     "in the third subtraction. Identify pairs of digits that lead to the 1-digit number after the "
                     "maximum possible number of subtractions.",
                     ["The difference of the numbers is 9 times the difference of the digits.",
                      "Third subtraction gives 9: after the second step the difference must be 9 times 1, from digits "
                      "that differ by 1, like 45, 56, 67 and 78.",
                      "The longest run: 3 and 7 (36, 27, 45, 9), the run in the book, takes four subtractions."],
                     "The number difference is 9 times the digit difference; the longest runs, like 3 and 7, take four "
                     "subtractions")])],
    key_terms=["difference", "multiple of 9", "digits"]))

# ============================== T12 King's Horses ==========================================================
TOPICS.append(TOPIC(
    "T12", "M3", "King's Horses", ["King's Horses"], "Analyze",
    "Students find the caretaker's counting mistake, arrange 19 and 18 horses with 5 on each side, and find how many "
    "more horses the thief can steal.",
    "A horse at a corner of the square stable is counted on two sides. Counting 5 on each of the 4 sides gives 20, but "
    "each corner horse is counted twice, so there are fewer real horses.",
    [A("T12.C1", "The caretaker's counting mistake", "Analyze",
       "Students count the horses one by one and find that 5 on each side of 4 sides does not mean 20 horses when "
       "corner horses are counted twice.",
       textbook=["Once upon a time, there was a king who was very fond of horses. He had 20 horses of the best breed. The "
                 "horses were kept in the royal stable, and cared for by a caretaker.",
                 "One night, a thief stole one of the horses. Fearing punishment, the caretaker arranged the horses in "
                 "the stable as shown in the picture here.",
                 "The king counted 5 horses along each side. \"We have 5 horses along each side and there are 4 sides. "
                 "So there are a total of 20 horses, your majesty,\" the caretaker explained.",
                 "But wait, were there really 20 horses in the stable? Count the horses one by one and check! What was "
                 "the mistake in the caretaker's explanation?"],
       teach=["Predict first: 5 horses on each of 4 sides, so is it always 20 horses?",
              "A horse at a corner stands on two sides, so it is counted once for each side.",
              "In the caretaker's stable, one corner horse is counted twice. 20 counted − 1 counted twice = 19 horses.",
              "The caretaker added 5 + 5 + 5 + 5 without noticing that a corner horse was in two of the fives."],
       examples=[WE("The caretaker says 5 horses on each of 4 sides makes 20. One horse stands at a corner and is counted "
                    "on two sides. How many horses are really there?",
                    ["5 + 5 + 5 + 5 = 20 counts every corner horse twice.",
                     "One corner horse is counted twice, so subtract 1: 20 − 1 = 19.",
                     "There are only 19 horses."],
                    "19 horses, because the corner horse was counted twice",
                    ncert=["kh.story", "kh.mistake"])],
       key_terms=["corner", "counted twice"], misconceptions=["M_CORNER_TWICE"], minutes=8, enrichment=True),
     A("T12.C2", "Eighteen horses and how many more can go", "Analyze",
       "Students arrange 18 horses with 5 on each side by placing 2 horses at corners, and find that the thief can "
       "steal up to 2 more horses before the count of 5 on each side fails.",
       textbook=["The following night, the thief stole another horse from the stable. Now, only 18 horses remained. The "
                 "caretaker once again cleverly arranged the 18 horses, so that there were 5 horses on each side of the "
                 "square stable. How do you think he was able to do it? Arrange the 18 horses in the stable with 5 on "
                 "each side.",
                 "How many more horses can the thief steal before the king notices something is wrong? Try making the "
                 "arrangements yourself."],
       teach=["Predict first: if 19 horses had 1 corner horse, how many corner horses will 18 horses need?",
              "Counted total is 20. Real horses = 20 − (number of corner horses). For 18 horses, 20 − 18 = 2 corner "
              "horses.",
              "Put horses on 2 corners, and fill the sides so that each side still counts 5.",
              "There are 4 corners, so the most corner horses is 4 and the fewest horses is 20 − 4 = 16. The thief can "
              "steal 18 − 16 = 2 more horses from 18."],
       examples=[WE("There are 18 horses. How many corner horses are needed so that each side shows 5, and how many more "
                    "horses can the thief steal?",
                    ["The count of 20 minus the corner horses is the real number: 20 − 18 = 2 corner horses.",
                     "All 4 corners hold horses at most, so the fewest horses is 20 − 4 = 16.",
                     "From 18, the thief can steal 18 − 16 = 2 more horses."],
                    "2 corner horses are needed, and the thief can steal 2 more horses",
                    ncert=["kh.eighteen"])],
       key_terms=["arrangement"], misconceptions=["M_CORNER_TWICE"], minutes=8, enrichment=True),
     DOER("T12.C3", "Practice: fill the stable", "square_stable", "Analyze",
          "Students arrange 19, 18, 17 and 16 horses in the square stable with 5 on each side, and find the fewest "
          "horses that still show 5 on every side.",
          ["A corner horse is counted on two sides.",
           "Real horses = 20 minus the number of corner horses.",
           "The fewest horses is when all 4 corners have horses."],
          items=[FIO("kh.more", "King's Horses, how many more can be stolen",
                     "How many more horses can the thief steal before the king notices something is wrong? Try making "
                     "the arrangements yourself.",
                     ["19 horses: 1 corner horse. 18 horses: 2 corner horses. 17 horses: 3 corner horses. 16 horses: "
                      "4 corner horses.",
                      "With 15 horses, 20 − 15 = 5 corner horses would be needed, but there are only 4 corners.",
                      "So 5 on every side is possible down to 16 horses. The thief can steal 2 more from 18."],
                     "2 more horses, down to 16; with 15 the king would find 5 on a side is no longer possible")])],
    key_terms=["corner", "arrangement"]))

# ============================== T13 Summary ================================================================
TOPICS.append(TOPIC(
    "T13", "M3", "Summary: We the Travellers - I", ["Chapter summary"], "Understand",
    "",
    "Ten thousand needs a new TTh place. Five-digit numbers are read, written and compared place by place; numbers "
    "are rounded to the nearest ten, hundred and thousand; and large numbers describe journeys, counts and puzzles.",
    [A("T13.C1", "What we learned in We the Travellers - I", "Understand",
       "",
       teach=["Ten thousand is 10 thousands, written 10,000, in a new TTh column.",
              "Five-digit numbers are read from the thousands part and written with commas and number names.",
              "To compare numbers, count the digits first; with equal digits, compare from the left.",
              "The nearest ten, hundred or thousand is the neighbour with the fewest jumps.",
              "Distance in many hours is the distance in one hour times the hours, and vehicles needed come from "
              "dividing people by seats.",
              "Puzzles teach us to think strategically: the pile of pebbles is won by mirroring, and a corner horse is "
              "counted twice."],
       ncert=["summary"], video_focus=["RECAP"], key_terms=["place value", "comparing", "nearest"], minutes=5, enrichment=True)],
    topic_type="summary"))
