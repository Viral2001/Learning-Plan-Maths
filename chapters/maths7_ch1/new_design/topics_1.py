# -*- coding: utf-8 -*-
"""Topics T1 to T5 (modules M1 and M2): a lakh, large numbers in words and numerals, the Land of Tens."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Framing: A Lakh Varieties =================================================
TOPICS.append(TOPIC(
    "T1", "M1", "A Lakh Varieties!", ["1.1"], "Understand",
    "",
    "Estu wonders whether tasting a new rice variety every day for a hundred years would come close to one lakh "
    "varieties. The question stays open until the next topic.",
    [A("T1.C1", "A lakh varieties of rice and Estu's question", "Remember",
       "",
       textbook=["1.1 A Lakh Varieties!",
                 "Eshwarappa is a farmer in Chintamani, a town in Karnataka. He visits the market regularly to buy "
                 "seeds for his rice field. During one such visit he overheard a conversation between Ramanna and "
                 "Lakshmamma. Ramanna said, \"Earlier our country had about a lakh varieties of rice. Farmers used to "
                 "preserve different varieties of seeds and use them to grow rice. Now, we only have a handful of "
                 "varieties. Also, farmers have to come to the market to buy seeds\".",
                 "Lakshmamma said, \"There is a seed bank near my house. So far, they have collected about a hundred "
                 "indigenous varieties of rice seeds from different places. You can also buy seeds from there.\"",
                 "You may have heard the word 'lakh' before. Do you know how big one lakh is? Let us find out.",
                 "Eshwarappa shared this incident with his daughter Roxie and son Estu.",
                 "Estu was surprised to know that there were about one lakh varieties of rice in this country. He "
                 "wondered \"One lakh! So far I have only tasted 3 varieties. If we tried a new variety each day, "
                 "would we even come close to tasting all the varieties in a lifetime of 100 years?\"",
                 "What do you think? Guess."],
       teach=["Picture a seed bank with jars of rice seeds, each jar a different variety. The country once had about "
              "a lakh of them.",
              "Estu has tasted 3 varieties. He asks what happens if he tries a new variety every single day for 100 "
              "years.",
              "Make a guess before the next step: would 100 years of tasting come close to one lakh varieties?"],
       ncert=["opening"], key_terms=["lakh"], video_focus=["HOOK"], minutes=4, enrichment=True),
     A("T1.C2", "The question to keep: can a lifetime reach a lakh", "Understand", "",
       teach=["Predict: about how many days are there in 100 years, a few thousand or a few lakh?",
              "To answer Estu we need two things: the number of days in a lifetime, and the number of varieties "
              "tasted each day.",
              "Keep this question in mind: the next topic builds up to one lakh and then answers it."],
       ncert=["1.1.lifetime"], enrichment=True)],
    topic_type="framing"))

# ============================== T2 Climbing to One Lakh ======================================================
TOPICS.append(TOPIC(
    "T2", "M1", "Climbing to One Lakh", ["1.1"], "Apply",
    "Students build up to one lakh from the largest five-digit number, compute the days in a lifetime as 365 times "
    "the years, compare tasting one, two and three varieties a day with one lakh, and find how far a population is "
    "from one lakh.",
    "One lakh is the smallest six-digit number, 1,00,000; a lifetime of days can be compared with it by subtraction.",
    [A("T2.C1", "From 999 up to one lakh", "Understand",
       "Students name the largest and smallest numbers with three to six digits, add one to the largest five-digit "
       "number, and read 1,00,000 as one lakh.",
       textbook=["But how much is one lakh? Observe the pattern and fill in the boxes given below.",
                 "The largest 3-digit number is 999. The smallest 4-digit number is __. The largest 4-digit number "
                 "is __. The smallest 5-digit number is __. The largest 5-digit number is __. The smallest 6-digit "
                 "number is 1,00,000.",
                 "99,995, 99,996, 99,998 ... each step is +1.",
                 "1,00,000 is read as \"One Lakh\"."],
       teach=["Predict first: what is the number that comes right after 99,999?",
              "Each time the digits run out, adding 1 gives the smallest number with one more digit: 999 to 1000, "
              "9999 to 10,000, 99,999 to 1,00,000.",
              "The smallest six-digit number is one lakh. The comma after the ten thousands place is new."],
       examples=[
           WE("Fill in the pattern: the largest 3-digit number is 999. Give the smallest 4-digit, the largest 4-digit, "
              "the smallest 5-digit, the largest 5-digit and the smallest 6-digit number.",
              ["999 + 1 = 1000, the smallest 4-digit number.", "The largest 4-digit number is 9999.",
               "9999 + 1 = 10,000, the smallest 5-digit number.", "The largest 5-digit number is 99,999.",
               "99,999 + 1 = 1,00,000, the smallest 6-digit number, read as one lakh."],
              "1000, 9999, 10,000, 99,999 and 1,00,000 (one lakh)", ncert=["1.1.pattern"])],
       key_terms=["lakh", "6-digit number"], misconceptions=["M_LAKH_ZEROS"], minutes=6),
     A("T2.C2", "Days in a lifetime and a lakh varieties", "Apply",
       "Students write the days in y years as 365 times y, work out the varieties tasted in 100 years for one, two "
       "and three varieties a day, and compare each with one lakh.",
       textbook=["Roxie and Estu found that if they ate one variety of rice a day, they would come nowhere close to a "
                 "lakh in a lifetime! Roxie suggests, \"What if we ate 2 varieties of rice every day? Would we then "
                 "be able to eat 1 lakh varieties of rice in 100 years?\"",
                 "What if a person ate 3 varieties of rice every day? Will they be able to taste all the lakh "
                 "varieties in a 100 year lifetime? Find out.",
                 "Estu said, \"We know how many days there are in a year, 365, if we ignore leap years. If we live "
                 "for y years, the number of days in our lifetime will be 365 × y.\"",
                 "Choose a number for y. How close to one lakh is the number of days in y years, for the y of your "
                 "choice?"],
       teach=["Predict first: in 100 years, will one variety a day come close to one lakh? Will three a day reach it?",
              "Days in y years: 365 × y. Varieties tasted: days × varieties a day.",
              "Choose your own y. For y = 50 the days are 365 × 50 = 18,250, which is 81,750 short of one lakh."],
       examples=[
           WE("Find the days in 100 years. Then find the varieties tasted in 100 years at one, two and three varieties "
              "a day, and compare each with one lakh.",
              ["Days in 100 years: 365 × 100 = 36,500.", "One a day: 36,500 varieties.",
               "Two a day: 36,500 × 2 = 73,000 varieties.", "Three a day: 36,500 × 3 = 1,09,500 varieties.",
               "1,00,000 − 73,000 = 27,000, so two a day falls short of one lakh.",
               "1,09,500 − 1,00,000 = 9,500, so three a day passes one lakh."],
              "36,500; 73,000; 1,09,500. Only three varieties a day passes one lakh.",
              ncert=["1.1.days", "1.1.choose_y"])],
       key_terms=["lakh", "days in y years"], misconceptions=["M_LAKH_ZEROS"], minutes=8),
     DOER("T2.C3", "Practice: how far from one lakh", "lakh_benchmark", "Apply",
          "Students place a number on a ruler marked at one lakh, say how much less or more than one lakh it is, "
          "and find the change between two populations by subtracting.",
          ["To see how far a number is below one lakh, subtract it from 1,00,000.",
           "To see how far it is above one lakh, subtract 1,00,000 from it.",
           "The change between two numbers is the larger one minus the smaller one."],
          items=[
              FIO("1.1.FiO_1", "Figure it Out, Q1 (Chintamani in 2011)",
                  "According to the 2011 Census, the population of the town of Chintamani was about 75,000. How much "
                  "less than one lakh is 75,000?",
                  ["One lakh is 1,00,000.", "1,00,000 − 75,000 = 25,000."],
                  "75,000 is 25,000 less than one lakh", tool="lakh_benchmark"),
              FIO("1.1.FiO_2", "Figure it Out, Q2 (Chintamani in 2024)",
                  "The estimated population of Chintamani in the year 2024 is 1,06,000. How much more than one lakh "
                  "is 1,06,000?",
                  ["One lakh is 1,00,000.", "1,06,000 − 1,00,000 = 6,000."],
                  "1,06,000 is 6,000 more than one lakh", tool="lakh_benchmark"),
              FIO("1.1.FiO_3", "Figure it Out, Q3 (growth of Chintamani)",
                  "By how much did the population of Chintamani increase from 2011 to 2024?",
                  ["In 2011 the population was about 75,000 and in 2024 it is 1,06,000.",
                   "The increase is the later value minus the earlier value.",
                   "1,06,000 − 75,000 = 31,000.",
                   "Check: 25,000 below one lakh and 6,000 above it give 25,000 + 6,000 = 31,000."],
                  "The population increased by 31,000", tool="lakh_benchmark")],
          ncert=["1.1.FiO_1", "1.1.FiO_2", "1.1.FiO_3"], misconceptions=["M_LAKH_ZEROS"])]))

# ============================== T3 Getting a feel for large numbers ==========================================
TOPICS.append(TOPIC(
    "T3", "M1", "Getting a Feel for Large Numbers", ["1.1"], "Analyze",
    "Students compare a tall statue and a waterfall with a building built from floors, find how many floors reach a "
    "given height, and judge whether one lakh is big or small by comparing it with things we see around us.",
    "A large number becomes easier to feel when it is compared with something familiar; one lakh is big or small "
    "depending on what it is compared with.",
    [A("T3.C1", "Comparing with Somu's building", "Apply",
       "Students find the height of a ten-floor building from the height of one floor, find how much taller a statue "
       "and a waterfall are, and count the floors needed to match the waterfall.",
       textbook=["Getting a Feel of Large Numbers",
                 "You may have come across interesting facts like these:",
                 "The world's tallest statue is the 'Statue of Unity' in Gujarat depicting Sardar Vallabhbhai Patel. "
                 "Its height is about 180 metres.",
                 "Kunchikal waterfall in Karnataka is said to drop from a height of about 450 metres.",
                 "It is not always easy to get a sense of how big these measurements are. But, we can get a better "
                 "sense of their size when we compare them with something familiar. Let us see an example.",
                 "Look at the picture on the right. Somu is 1 metre tall. If each floor is about four times his "
                 "height, what is the approximate height of the building?",
                 "Which is taller, The Statue of Unity or this building? How much taller?",
                 "We can see that the height of the Statue of Unity is close to 4 times the height of Somu's "
                 "building.",
                 "How much taller is the Kunchikal waterfall than Somu's building?",
                 "How many floors should Somu's building have to be as high as the waterfall?"],
       teach=["The picture shows Somu, 1 metre tall, standing beside a building of 10 floors. One floor is about as "
              "tall as four Somus.",
              "Predict first: will the building be taller than the statue, which is 180 metres?",
              "One floor is 4 m, so 10 floors are 40 m. Compare each tall thing with 40 m.",
              "Floors needed for a height: divide the height by 4 m, the height of one floor."],
       examples=[
           WE("Somu is 1 m tall and each floor is about 4 m. The picture shows 10 floors. Find the height of the "
              "building, how much taller the Statue of Unity (180 m) and the Kunchikal waterfall (450 m) are, and "
              "how many floors match the waterfall.",
              ["One floor is 4 × 1 = 4 m, so 10 floors are 10 × 4 = 40 m.",
               "Statue of Unity: 180 − 40 = 140 m taller than the building.",
               "Kunchikal waterfall: 450 − 40 = 410 m taller than the building.",
               "Floors for 450 m: 450 ÷ 4 is 112.5, so about 113 floors.",
               "The statue is 180 ÷ 40 = 4.5 times the building, a little more than 4 times."],
              "The building is 40 m; the statue is 140 m taller; the waterfall is 410 m taller; about 113 floors",
              ncert=["1.1.somu", "1.1.somu_statue", "1.1.somu_waterfall", "1.1.somu_floors"])],
       key_terms=["compare", "approximate"], misconceptions=["M_LAKH_SMALL"], minutes=8),
     A("T3.C2", "Is one lakh a very large number", "Evaluate",
       "Students check Roxie's lakh-days and lakh-people claims by calculation, quote Estu's reasons that a lakh can "
       "look small, and say why big or small depends on the comparison.",
       textbook=["Is One Lakh a Very Large Number?",
                 "Eshwarappa asked Roxie and Estu, \"Is a lakh big or small?\"",
                 "Roxie feels that 1 lakh is a large number: \"We had one lakh varieties of rice, that is a lot.\" "
                 "\"Living 1 lakh days would mean living for 274 years, that is a really long time!\" \"If 1 lakh "
                 "people stood shoulder to shoulder in a line they could stretch as far as 38 kilometres.\"",
                 "Estu, however, thinks it is not that big: \"Do you know that the cricket stadium in Ahmedabad has a "
                 "seating capacity of more than 1 lakh? One lakh people in such a small area!\" \"Most humans have "
                 "80,000 to 1,20,000 hairs on their heads. Imagine, 1 lakh hairs fit in such a tiny space!\" \"I "
                 "heard that there are some species of fish where a female fish can lay almost one lakh eggs at once "
                 "very comfortably. Some even lay tens of lakhs of eggs at a time.\"",
                 "How do you view a lakh, is a lakh big or small?",
                 "Note to the Teacher: Encourage students to make connections between these facts. For example, can "
                 "the whole population of Chintamani fit in the stadium? How can we imagine the line of 38 km, having "
                 "a lakh people, sitting next to each other in the stadium?"],
       teach=["Predict first: do you think a lakh days is closer to 27 years or to 274 years?",
              "Roxie compares a lakh with a lifetime and a long line, so it looks large. Estu compares it with a "
              "stadium, a head of hair and fish eggs, so it looks small.",
              "A lakh is big or small depending on what it is compared with. Check each claim with a calculation.",
              "Assume each person is about 38 cm wide; that is the assumption behind the line of 38 km."],
       examples=[
           WE("Check Roxie's two claims: 1 lakh days is about 274 years, and 1 lakh people shoulder to shoulder "
              "stretch about 38 km. Assume a person is 38 cm wide. Is a lakh big or small?",
              ["Years in 1 lakh days: 1,00,000 ÷ 365 is about 274 years.",
               "Line of people: 1,00,000 × 38 = 38,00,000 cm.",
               "38,00,000 ÷ 100 = 38,000 m, and 38,000 ÷ 1000 = 38 km.",
               "Both claims hold, so a lakh days and a lakh people in a row are long.",
               "A lakh seats in a stadium or a lakh hairs on a head fit in a small space, so a lakh can look small.",
               "So a lakh is big or small depending on what it is compared with."],
              "About 274 years and 38 km; a lakh is big or small depending on the comparison",
              ncert=["1.1.lakh_big"])],
       key_terms=["compare", "assumption"], misconceptions=["M_LAKH_SMALL"], minutes=8),
     DOER("T3.C3", "Practice: compare with something familiar", None, "Apply",
          "Students compare a tall height with a building of floors, say how many times taller it is, and judge a "
          "big number against a real thing.",
          ["Pick a familiar thing and measure the big number in units of it.",
           "Divide to find how many times bigger, subtract to find how much more.",
           "State the assumption you used."])]))

# ============================== T4 Reading and writing large numbers =========================================
TOPICS.append(TOPIC(
    "T4", "M1", "Reading and Writing Large Numbers", ["1.1"], "Apply",
    "Students read lakh numbers in words with commas in the Indian system, and write a number from its words by "
    "placing each part in its lakh, thousand and hundred place with zeros where a place is empty.",
    "Commas split an Indian-system number into lakhs, thousands and the rest, so it can be read and written part by "
    "part.",
    [A("T4.C1", "Number names with lakhs", "Apply",
       "Students place commas in the Indian system, read a number as lakhs, thousands and the rest, and write the "
       "number name of a number such as 12,78,830.",
       textbook=["Reading and Writing Numbers",
                 "We have already been using commas for 5-digit numbers like 45,830 in the Indian place value system. "
                 "As numbers grow bigger, using commas helps in reading the numbers easily. We use a comma in between "
                 "the digits representing the \"ten thousands\" place and the \"one lakh\" place as you have seen just "
                 "before (1,00,000).",
                 "The number name of 12,78,830 is twelve lakh seventy eight thousand eight hundred thirty. Similarly, "
                 "the number 15,75,000 in words is fifteen lakh seventy five thousand.",
                 "Write each of the numbers given below in words: (a) 3,00,600 (b) 5,04,085 (c) 27,30,000 "
                 "(d) 70,53,138"],
       teach=["Predict first: in 12,78,830 how many lakhs are there, and what is left after them?",
              "Read the part before the first comma from the left as lakhs, then thousands, then hundreds, tens and "
              "ones.",
              "A part that is all zeros is not said: 15,75,000 is fifteen lakh seventy five thousand."],
       examples=[
           WE("Write 12,78,830 and the numbers (a) 3,00,600 and (b) 5,04,085 in words.",
              ["12,78,830: 12 lakh, 78 thousand, 8 hundreds and 30.",
               "So 12,78,830 is twelve lakh seventy eight thousand eight hundred thirty.",
               "(a) 3,00,600: 3 lakh, 00 thousand, 600. The zero thousands are not said.",
               "(a) is three lakh six hundred.",
               "(b) 5,04,085: 5 lakh, 04 thousand, 085.",
               "(b) is five lakh four thousand eighty five."],
              "Twelve lakh seventy eight thousand eight hundred thirty; (a) three lakh six hundred; (b) five lakh "
              "four thousand eighty five",
              ncert=["1.1.words_ex", "1.1.words_a", "1.1.words_b"]),
           WE("Write (c) 27,30,000 and (d) 70,53,138 in words.",
              ["(c) 27,30,000: 27 lakh, 30 thousand, nothing else.",
               "(c) is twenty seven lakh thirty thousand.",
               "(d) 70,53,138: 70 lakh, 53 thousand, 1 hundred and 38.",
               "(d) is seventy lakh fifty three thousand one hundred thirty eight."],
              "(c) twenty seven lakh thirty thousand; (d) seventy lakh fifty three thousand one hundred thirty eight",
              ncert=["1.1.words_c", "1.1.words_d"])],
       key_terms=["lakh", "comma", "number name"], misconceptions=["M_COMMA_PLACE"], minutes=10),
     A("T4.C2", "Writing numbers from their names", "Apply",
       "Students turn a number name into digits by writing each part in its place, with zeros where a place is empty "
       "and commas in the Indian system.",
       textbook=["Write the corresponding number in the Indian place value system for each of the following:",
                 "(a) One lakh twenty three thousand four hundred and fifty six",
                 "(b) Four lakh seven thousand seven hundred and four",
                 "(c) Fifty lakhs five thousand and fifty",
                 "(d) Ten lakhs two hundred and thirty five"],
       teach=["Predict first: in 'four lakh seven thousand seven hundred and four', which place is empty and needs a "
              "zero?",
              "Write the lakh part, then two digits for thousands, then three digits for the rest, filling empty "
              "places with zeros.",
              "Then place the commas: 3 digits from the right, then groups of 2."],
       examples=[
           WE("Write in digits: (a) one lakh twenty three thousand four hundred and fifty six, (b) four lakh seven "
              "thousand seven hundred and four, (c) fifty lakhs five thousand and fifty, (d) ten lakhs two hundred "
              "and thirty five.",
              ["(a) 1 lakh, 23 thousand, 456: 1,23,456.",
               "(b) 4 lakh, 07 thousand, 704: the tens of thousands is empty, so 4,07,704.",
               "(c) 50 lakh, 05 thousand, 050: 50,05,050.",
               "(d) 10 lakh, 00 thousand, 235: 10,00,235."],
              "(a) 1,23,456 (b) 4,07,704 (c) 50,05,050 (d) 10,00,235",
              ncert=["1.1.num_a", "1.1.num_b", "1.1.num_c", "1.1.num_d"])],
       key_terms=["lakh", "place value"], misconceptions=["M_COMMA_PLACE"], minutes=8),
     DOER("T4.C3", "Practice: commas and number names", "comma_ladder", "Apply",
          "Students drop digits into a place value ladder, place the Indian-system commas, and read the number as "
          "lakhs, thousands and the rest.",
          ["Group the digits as 3, then 2, 2, ... from the right.",
           "Read each group with its name: thousand, lakh.",
           "Write a zero in every empty place."])]))

# ============================== T5 The Land of Tens ==========================================================
TOPICS.append(TOPIC(
    "T5", "M2", "The Land of Tens", ["1.2"], "Apply",
    "Students find how many times a plus-1000, plus-10 or plus-100 button must be pressed to show a number, divide by "
    "the button value, and judge which calculator can show which numbers.",
    "A calculator with one button shows a number by pressing that button the number divided by its value times, and "
    "it can only show multiples of that value.",
    [A("T5.C1", "Thoughtful Thousands", "Apply",
       "Students divide a number by 1000 to find the presses of a plus-1000 button, and multiply the presses by 1000 "
       "to find the number shown.",
       textbook=["1.2 Land of Tens",
                 "In the Land of Tens, there are special calculators with special buttons.",
                 "1. The Thoughtful Thousands only has a +1000 button. How many times should it be pressed to show: "
                 "(a) Three thousand? 3 times (b) 10,000? (c) Fifty three thousand? (d) 90,000? (e) One Lakh? "
                 "(f) ? 153 times (g) How many thousands are required to make one lakh?"],
       teach=["Predict first: how many presses of +1000 make 10,000?",
              "Presses = number ÷ 1000. If the presses are given, the number shown is presses × 1000.",
              "It can only show multiples of 1000."],
       examples=[
           WE("Thoughtful Thousands has only a +1000 button. Find the presses for (a) 3000, (b) 10,000, (c) 53,000, "
              "(d) 90,000, (e) one lakh, (f) the number shown by 153 presses, and (g) the thousands in one lakh.",
              ["(a) 3000 ÷ 1000 = 3 presses.", "(b) 10,000 ÷ 1000 = 10 presses.", "(c) 53,000 ÷ 1000 = 53 presses.",
               "(d) 90,000 ÷ 1000 = 90 presses.", "(e) 1,00,000 ÷ 1000 = 100 presses.",
               "(f) 153 × 1000 = 1,53,000.", "(g) One lakh has 100 thousands."],
              "(a) 3 (b) 10 (c) 53 (d) 90 (e) 100 (f) 1,53,000 (g) 100",
              ncert=["1.2.tt_a", "1.2.tt_b", "1.2.tt_c", "1.2.tt_d", "1.2.tt_e", "1.2.tt_f", "1.2.tt_g"])],
       key_terms=["button presses", "thousand"], misconceptions=["M_PRESS_COUNT"], minutes=8),
     A("T5.C2", "Tedious Tens", "Apply",
       "Students divide a number by 10 to find the presses of a plus-10 button, and see that counting in tens needs "
       "ten times as many presses as counting in hundreds.",
       textbook=["2. The Tedious Tens only has a +10 button. How many times should it be pressed to show: "
                 "(a) Five hundred? (b) 780? (c) 1000? (d) 3700? (e) 10,000? (f) One lakh? (g) ? 435 times"],
       teach=["Predict first: how many presses of +10 make 1000?",
              "Presses = number ÷ 10: drop one zero.",
              "One lakh needs 10,000 presses, which is why it is called tedious."],
       examples=[
           WE("Tedious Tens has only a +10 button. Find the presses for (a) 500, (b) 780, (c) 1000, (d) 3700, "
              "(e) 10,000, (f) one lakh, and the number shown by (g) 435 presses.",
              ["(a) 500 ÷ 10 = 50 presses.", "(b) 780 ÷ 10 = 78 presses.", "(c) 1000 ÷ 10 = 100 presses.",
               "(d) 3700 ÷ 10 = 370 presses.", "(e) 10,000 ÷ 10 = 1000 presses.",
               "(f) 1,00,000 ÷ 10 = 10,000 presses.", "(g) 435 × 10 = 4350."],
              "(a) 50 (b) 78 (c) 100 (d) 370 (e) 1000 (f) 10,000 (g) 4350",
              ncert=["1.2.tens_a", "1.2.tens_b", "1.2.tens_c", "1.2.tens_d", "1.2.tens_e", "1.2.tens_f",
                     "1.2.tens_g"])],
       key_terms=["button presses", "ten"], misconceptions=["M_PRESS_COUNT"], minutes=8),
     A("T5.C3", "Handy Hundreds", "Analyze",
       "Students divide by 100 to find the presses of a plus-100 button, and decide whether Handy Hundreds can show "
       "numbers that Tedious Tens and Thoughtful Thousands cannot.",
       textbook=["3. The Handy Hundreds only has a +100 button. How many times should it be pressed to show: "
                 "(a) Four hundred? (b) 3,700? (c) 10,000? (d) Fifty three thousand? (e) 90,000? (f) 97,600? "
                 "(g) 1,00,000? (h) ? 582 times (i) How many hundreds are required to make ten thousand? "
                 "(j) How many hundreds are required to make one lakh?",
                 "(k) Handy Hundreds says, \"There are some numbers which Tedious Tens and Thoughtful Thousands can't "
                 "show but I can.\" Is this statement true? Think and explore."],
       teach=["Predict first: Handy Hundreds shows 97,600 in how many presses?",
              "Presses = number ÷ 100: drop two zeros.",
              "Think about statement (k): every multiple of 100 is also a multiple of 10. So can Tedious Tens show "
              "every number that Handy Hundreds shows?"],
       examples=[
           WE("Handy Hundreds has only a +100 button. Find the presses for (a) 400, (b) 3,700, (c) 10,000, "
              "(d) 53,000, (e) 90,000, (f) 97,600, (g) 1,00,000, the number shown by (h) 582 presses, the hundreds in "
              "(i) ten thousand and (j) one lakh, and decide the statement in (k).",
              ["(a) 400 ÷ 100 = 4 presses.", "(b) 3700 ÷ 100 = 37 presses.", "(c) 10,000 ÷ 100 = 100 presses.",
               "(d) 53,000 ÷ 100 = 530 presses.", "(e) 90,000 ÷ 100 = 900 presses.",
               "(f) 97,600 ÷ 100 = 976 presses.", "(g) 1,00,000 ÷ 100 = 1000 presses.",
               "(h) 582 × 100 = 58,200.", "(i) Ten thousand has 100 hundreds.", "(j) One lakh has 1000 hundreds.",
               "(k) Every multiple of 100 is a multiple of 10, so Tedious Tens can show it too. The statement is "
               "not true."],
              "(a) 4 (b) 37 (c) 100 (d) 530 (e) 900 (f) 976 (g) 1000 (h) 58,200 (i) 100 (j) 1000 (k) No",
              ncert=["1.2.hh_a", "1.2.hh_b", "1.2.hh_c", "1.2.hh_d", "1.2.hh_e", "1.2.hh_f", "1.2.hh_g", "1.2.hh_h",
                     "1.2.hh_i", "1.2.hh_j", "1.2.hh_k"])],
       key_terms=["button presses", "hundred", "multiple"], misconceptions=["M_PRESS_COUNT"], minutes=10),
     DOER("T5.C4", "Practice: which calculator reaches it", None, "Apply",
          "Students pick the calculator that shows a given number, count its presses by dividing, and say which "
          "other calculators can show the same number.",
          ["Presses = number ÷ button value.",
           "A number must be a multiple of the button value to be shown.",
           "A multiple of 1000 is also a multiple of 100 and of 10."])]))
