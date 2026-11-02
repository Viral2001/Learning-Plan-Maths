# -*- coding: utf-8 -*-
"""Topics T1 to T6 (modules M1 and M2: collecting and organising data, pictographs). Book sections 4.1 and 4.2."""
from topics_common import A, DOER, TOPIC, BOOK_TEXT, book, fio, we

TOPICS = []
H41 = "4.1 Collecting and Organising Data"
H42D = "Drawing a Pictograph"

# ============================== T1 Opening ===================================================================
TOPICS.append(TOPIC(
    "T1", "M1", "Which Game Is Most Popular?", ["Chapter opening"], "Understand",
    "",
    "A class wants to know its most popular game. What is data, and how do we find the answer from it?",
    [A("T1.C1", "A question about the whole class", "Remember", "",
       textbook=[l.replace("—", ", ") for l in BOOK_TEXT["extra_inv_A.json"]["opening"]["textbook_lines"][:2]] + book("4.1", H41, stop=5),
       teach=["Two friends disagree: one says cricket is the most popular game in the class, the other says "
              "hockey. Neither has asked anyone else.",
              "Make a guess before the next step: how could the two friends find out for sure, and what would "
              "they have to write down?"],
       ncert=["opening"], key_terms=["data"], video_focus=["HOOK"], minutes=4, enrichment=True)],
    topic_type="framing"))

# ============================== T2 Collecting data (4.1) =====================================================
TOPICS.append(TOPIC(
    "T2", "M1", "Collecting Data", ["4.1"], "Apply",
    "Students decide when a question needs data to be collected, collect the answers of a whole class in a "
    "list, and count the list to find the most popular choice.",
    "Data is collected by asking everyone the same question; a list is then counted to see which choice is "
    "most popular.",
    [A("T2.C1", "Asking everyone: collecting the data", "Understand",
       "Students say that the way to find the most popular game is to ask each classmate the same question and "
       "write the answers in a list, and name that list as data.",
       textbook=book("4.1", H41, start=5, stop=9),
       teach=["Predict first: Navya says cricket is the favourite of the class, because it is her favourite. "
              "Is one child's choice enough?",
              "To find what the whole class likes, ask each student the same question: what is your favourite "
              "game?",
              "Write each answer down. The list of answers collected is data.",
              "Only the list of the whole class can tell the most popular game, not one child's opinion."],
       examples=[we("4.1.q1")],
       key_terms=["data", "survey"], misconceptions=["M_LIST_ENOUGH"], minutes=8),
     A("T2.C2", "From a list to counts: the most popular game", "Apply",
       "Students group a long list of favourite games by game, count each group, and name the game with the "
       "highest count as the most popular.",
       textbook=book("4.1", H41, start=9, stop=10),
       teach=["Predict first: the list has 31 names with a game beside each. Can you read the most popular game "
              "straight off the list?",
              "No. The same games are scattered all over the list, so group the names by game first.",
              "Count each group: Hockey 8, Kabaddi 6, Cricket 6, Satoliya 5, Football 4, Badminton 2.",
              "The group with the highest count is Hockey, so hockey is the most popular game, not cricket."],
       examples=[we("4.1.q2")],
       key_terms=["frequency", "count"], misconceptions=["M_LIST_ENOUGH"], minutes=10),
     DOER("T2.C3", "Practice: Collect, count and decide", None, "Apply",
          "Students decide which questions need data collection, find the most popular choice from a list by "
          "counting, and plan a survey of their own class.",
          ["Ask every member of the group the same question and write the answers down.",
           "Group the answers by choice and count each group.",
           "The choice with the highest count is the most popular."],
          items=[fio("4.1.FiO1.Q1"), fio("4.1.FiO1.Q2"), fio("4.1.FiO1.Q3"), fio("4.1.FiO1.Q4")],
          misconceptions=["M_LIST_ENOUGH"])]))

# ============================== T3 Tally marks and frequency tables (4.1) ====================================
TOPICS.append(TOPIC(
    "T3", "M1", "Tally Marks and Frequency Tables", ["4.1"], "Apply",
    "Students count with tally marks in bundles of five, read the totals as frequencies, and see what a "
    "frequency table can answer and what it cannot.",
    "A tally mark is a stroke for each count, with every fifth stroke across four; the totals are the "
    "frequencies in a frequency table.",
    [A("T3.C1", "Tally marks: counting in bundles of five", "Apply",
       "Students count each answer with a tally stroke, cross four strokes with a fifth to make a bundle of "
       "five, and read the total of a row of tally marks.",
       textbook=book("4.1", H41, start=14, stop=16),
       teach=["Predict first: five children call out their sweet one by one. How can you keep count without "
              "losing your place?",
              "Make one stroke for each child. When the count reaches 5, draw the fifth stroke across the "
              "previous four to make a bundle of five.",
              "To read a row, count the bundles in fives and then the loose strokes: one bundle and 1 stroke "
              "is 6 children.",
              "Counting in bundles makes a long row quick and safe to read."],
       video_focus=["TALLY"], misconceptions=["M_TALLY_SINGLES"], key_terms=["tally mark"], minutes=8),
     A("T3.C2", "The frequency table: what it tells and what it cannot", "Understand",
       "Students call the total of a tally row its frequency, use a frequency table to read how many chose "
       "each sweet, and say what the table cannot tell, such as which child chose which sweet.",
       textbook=book("4.1", H41, start=18, stop=21),
       teach=["Predict first: the table says 6 children chose jalebi. Does it say which children?",
              "The number of times a choice occurs is its frequency. Jalebi has frequency 6 and gulab jamun "
              "has frequency 9.",
              "The table helped Shri Nilesh buy the right number of each sweet.",
              "It does not say which student chose which sweet. For handing out, group the students by their "
              "choice instead."],
       video_focus=["FREQUENCY"], misconceptions=["M_LIST_ENOUGH"], key_terms=["frequency", "tally mark"],
       minutes=8),
     DOER("T3.C3", "Pull it together and do it: Tally Table Maker", "tally_table", "Apply",
          "Students tally a stream of answers on the tool into bundles of five, read each total as a "
          "frequency, and name the most and least chosen item.",
          ["One stroke for each answer; the fifth stroke goes across four.",
           "Count the bundles in fives and add the loose strokes.",
           "The total of a row is its frequency."],
          items=[fio("4.1.FiO2.Q1"), fio("4.1.FiO2.Q2")],
          misconceptions=["M_TALLY_SINGLES", "M_LIST_ENOUGH"])]))

# ============================== T4 Arranging data in order (4.1) =============================================
TOPICS.append(TOPIC(
    "T4", "M1", "Arranging Data in Order", ["4.1"], "Apply",
    "Students arrange data in ascending order, read the smallest, the largest and any frequency from the "
    "ordered list, and compare it with a frequency table.",
    "Ordered data, smallest to largest, makes the smallest, the largest and every frequency easy to count.",
    [A("T4.C1", "Ascending order: shoe sizes", "Apply",
       "Students arrange the shoe sizes of a class in ascending order and read off the smallest size, the "
       "largest size and how many students wear each size.",
       textbook=book("4.1", H41, start=21, stop=23),
       teach=["Predict first: Sushri Sandhya wrote the shoe sizes on the board in the order she was told them. "
              "Can you spot the largest size quickly?",
              "Arrange them from the smallest to the largest. This is ascending order.",
              "In the ordered list the first number is the smallest size, 3, and the last is the largest, 7.",
              "Equal sizes now sit together, so each size can be counted in one go."],
       video_focus=["ORDER"], key_terms=["ascending order"], misconceptions=["M_LIST_ENOUGH"], minutes=8),
     A("T4.C2", "Two ways to arrange: an ordered list and a frequency table", "Analyze",
       "Students turn an ordered list into a frequency table by counting each value, and compare what each "
       "arrangement shows more easily.",
       textbook=book("4.1", H41, start=29, stop=30),
       teach=["Predict first: the ordered list has 27 numbers. Is there a shorter way to show the same data?",
              "Count each size: size 3 occurs 3 times, size 4 occurs 9 times, size 5 occurs 10 times, size 6 "
              "occurs 4 times and size 7 occurs 1 time.",
              "The frequency table is short, and the ordered list shows every single entry. Each way has its "
              "own advantages.",
              "To find how many students wear a size larger than 4, add the frequencies of 5, 6 and 7."],
       video_focus=["WAYS"], key_terms=["frequency", "ascending order"], misconceptions=["M_COUNT_AS_VALUE"],
       minutes=8),
     DOER("T4.C3", "Practice: Order the data and answer", None, "Apply",
          "Students order shoe sizes, answer questions from the ordered list, say why ordering helps, and "
          "tabulate trees and letters from their own surroundings.",
          ["Arrange the data from the smallest to the largest.",
           "Equal values sit together, so counting them is quick.",
           "A frequency table is another way to arrange the same data."],
          items=[fio("4.1.FiO3.Q1"), fio("4.1.FiO3.Q2"), fio("4.1.FiO3.Q3"), fio("4.1.FiO3.Q4"),
                 fio("4.1.FiO3.Q5")],
          misconceptions=["M_LIST_ENOUGH"])]))

# ============================== T5 Reading pictographs (4.2) =================================================
TOPICS.append(TOPIC(
    "T5", "M2", "Reading Pictographs", ["4.2"], "Apply",
    "Students read a pictograph using its key, find the most and the least, and work out a frequency when one "
    "symbol or half a symbol stands for several children.",
    "In a pictograph each symbol stands for the number in its key; multiply the number of symbols by the key "
    "to get the frequency.",
    [A("T5.C1", "Reading a pictograph: one smiley, one student", "Understand",
       "Students read a pictograph where one smiley is one student, and name the mode of travel used by the "
       "most and by the fewest students.",
       textbook=book("4.2", None, stop=5),
       teach=["Predict first: a picture shows rows of smileys for the way children travel to school. Which row "
              "tells you the most popular way at a glance?",
              "In this pictograph one smiley is one student, so count the smileys in each row.",
              "The longest row is the school bus, with 11 students. The shortest row is the cycle, with 3.",
              "A pictograph shows the answer at a glance, with no numbers written."],
       examples=[we("4.2.q1"), we("4.2.q2")],
       key_terms=["pictograph", "symbol"], misconceptions=["M_ONE_SYMBOL_ONE"], minutes=8),
     A("T5.C2", "The key: one symbol stands for 10 children", "Apply",
       "Students read the key of a pictograph, multiply the symbols by it, and count a half symbol as half of "
       "the key.",
       textbook=book("4.2", None, start=5, stop=7),
       teach=["Predict first: Nand Kishor's pictograph shows 5 triangles for 'Always'. Are there 5 children?",
              "Read the key first: one triangle stands for 10 children, so 5 triangles are 5 × 10 = 50 children.",
              "A half triangle stands for half of 10, which is 5 children, so 2 triangles and a half are 25 "
              "children.",
              "Always read the key before counting the symbols."],
       examples=[we("4.2.ex1")],
       key_terms=["key", "half symbol"], misconceptions=["M_KEY_IGNORED", "M_HALF_SYMBOL"], minutes=10),
     DOER("T5.C3", "Pull it together and do it: Pictograph Reader", "pictograph_reader", "Apply",
          "Students read the key on the tool, turn symbols and half symbols into numbers, and answer questions "
          "about the most, the least and the total.",
          ["Read the key: what does one symbol stand for?",
           "Number of symbols times the key gives the frequency; a half symbol is half the key.",
           "An empty row means the frequency is 0."],
          items=[fio("4.2.FiO.Q1")],
          misconceptions=["M_KEY_IGNORED", "M_HALF_SYMBOL"])]))

# ============================== T6 Drawing pictographs (4.2) =================================================
TOPICS.append(TOPIC(
    "T6", "M2", "Drawing Pictographs", ["4.2"], "Apply",
    "Students choose a key that keeps a pictograph short, use half symbols for halves of the key, and say "
    "when a pictograph becomes hard to draw.",
    "Choose a key so that the symbols stay few; a half symbol shows half the key, and numbers that are not "
    "multiples of the key are hard to show.",
    [A("T6.C1", "Too many symbols: choosing a bigger key", "Apply",
       "Students see why one symbol for each student needs too many symbols for large numbers, and choose a "
       "key such as one smiley for 5 students that saves time and space.",
       textbook=book("4.2", H42D, start=2, stop=5),
       teach=["Predict first: Jarina and Sangita counted 35 students present in one class. How many smileys "
              "does one symbol for each student need?",
              "35 smileys for one class, and 8 classes, takes a lot of time and space.",
              "Jarina made one smiley stand for 5 students. 35 students then need 7 smileys.",
              "A bigger key keeps the pictograph short but every count must now be a multiple of the key."],
       examples=[we("4.2.q3")],
       key_terms=["key", "scale"], misconceptions=["M_ONE_SYMBOL_ONE"], minutes=10),
     A("T6.C2", "Half symbols, and when a pictograph is hard to draw", "Analyze",
       "Students use a half smiley for 5 students when the key is 10, and explain why 33 or 27 students "
       "cannot be shown exactly.",
       textbook=book("4.2", H42D, start=5, stop=8) + book("4.2", H42D, start=13, stop=14),
       teach=["Predict first: Sangita let one smiley stand for 10 students. How can she show 25?",
              "Two smileys and a half smiley: 10 + 10 + 5 = 25 students.",
              "33 students are 3 smileys and 3 more. A half smiley cannot show 3 students exactly.",
              "A pictograph is hard to prepare when the data is large or the numbers are not multiples of the "
              "key."],
       examples=[we("4.2.q4")],
       key_terms=["half symbol", "key"], misconceptions=["M_HALF_SYMBOL"], minutes=10),
     DOER("T6.C3", "Pull it together and do it: Pictograph Builder", "pictograph_builder", "Create",
          "Students choose a key on the tool, place the symbols and half symbols for each category, and check "
          "the pictograph against the table.",
          ["Pick a key that divides most of the numbers.",
           "Frequency divided by the key gives the symbols; a remainder of half a key is a half symbol.",
           "Check: symbols times the key must give back the table."],
          items=[fio("4.2.FiO.Q2")],
          misconceptions=["M_HALF_SYMBOL", "M_ONE_SYMBOL_ONE"])]))
