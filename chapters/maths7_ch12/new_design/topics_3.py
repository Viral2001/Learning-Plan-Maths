# -*- coding: utf-8 -*-
"""Topics T12 to T16 (modules M3 and M4). Book section 4.4, the end of chapter questions, the summary and the
Hidato puzzle."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T12 Look before you leap =======================================================
TOPICS.append(TOPIC(
    "T12", "M3", "Look Before You Leap!", ["4.4"], "Evaluate",
    "Students use decimal multiplication with 365.2422 days to compare calendar days with the days the Earth takes "
    "over 4, 100 and 1000 years, write expressions for the days in a span of calendar years, and evaluate how each "
    "leap year rule (every 4th year, not the 100th, but the 400th) narrows the gap.",
    "A year is 365.2422 days, not 365; each leap year rule is a decimal correction, checked by multiplying "
    "365.2422 by the number of years.",
    [A("T12.C1", "The year is 365.2422 days", "Understand",
       "Students find how far the calendar falls behind the Earth after 100 years of 365 days by multiplying 0.2422 "
       "by 100.",
       textbook=["4.4 Look Before You Leap!",
                 "Did you know that it takes the Earth 365.2422 days to go around the Sun and not 365 days? For our "
                 "convenience, we consider 365 days as a year in a calendar. We are talking about Gregorian calendar.",
                 "This means that, after one calendar year or 365 days, the Earth still needs 0.2422 more days to "
                 "complete one full revolution around the Sun. This doesn't seem like much. But what happens after 100 "
                 "such calendar years?",
                 "Using our understanding of decimal multiplication, 0.2422 × 100 = 24.22 days.",
                 "If our calendar does not accurately indicate the position of the Earth around the Sun, our seasons "
                 "and our annual calendar will not match!",
                 "To correct this problem, the idea of a leap year was introduced. Every fourth year, one additional "
                 "day is added to the calendar year."],
       teach=["Predict first: after 100 calendar years of 365 days, is the Earth behind by less than a week or more?",
              "Each year leaves 0.2422 of a day unfinished, and multiplying by 100 moves the point 2 places right.",
              "A leap year adds 1 day every 4th year to catch up."],
       examples=[
           WE("The Earth takes 365.2422 days to go round the Sun. After 100 calendar years of 365 days, how many more "
              "days does the Earth need to finish its 100th revolution?",
              ["Each calendar year is short by 365.2422 − 365 = 0.2422 days.",
               "Over 100 years: 0.2422 × 100 = 24.22 days.",
               "That is more than 3 weeks, so the seasons would drift."],
              "24.22 days", ncert=["4.4.year"])],
       key_terms=["revolution", "leap year"], misconceptions=["M_UNIT_MIX"], minutes=8),
     A("T12.C2", "A leap day every 4 years", "Apply",
       "Students count the days in 4 and in 100 calendar years with a leap day every 4th year, compare with 4 and "
       "100 revolutions of the Earth, and see that the calendar overcompensates.",
       textbook=["Is the year divisible by 4? Yes: the year has 366 days. No: the year has 365 days.",
                 "Do you know which month has this extra day?",
                 "Looking at the above sequence, the number of days after 4 calendar years is 4 × 365 + 1 = 1461 days.",
                 "What is the number of days that the Earth needs to make 4 full revolutions around the Sun? "
                 "4 × 365.2422 = 1460.9688 days.",
                 "With this new scheme of adding one extra day every 4th year, what is the number of days in 100 "
                 "calendar years? Can you write an expression to calculate that number?",
                 "How many years are divisible by 4 in 100 years?",
                 "So, the number of days in 100 calendar years is, (100 × 365 + 100/4 × 1) = 36525 days.",
                 "Can you form different expressions for the same question?",
                 "The actual number of days that the Earth takes to go around the Sun 100 times is, 100 × 365.2422 = "
                 "36524.22 days.",
                 "Thus, by adding a day every fourth year, after 100 years, the calendar days are more than the actual "
                 "number of days taken by the Earth to go around the Sun. We have overcompensated."],
       teach=["Predict first: with a leap day every 4 years, does the calendar now run ahead of the Earth or behind?",
              "The extra day is 29 February.",
              "Compare the calendar total with 365.2422 times the number of years."],
       examples=[
           WE("With a leap day every 4th year, how many days are in 4 calendar years? How many days does the Earth "
              "take for 4 revolutions?",
              ["Calendar: 4 × 365 + 1 = 1461 days.", "Earth: 4 × 365.2422 = 1460.9688 days.",
               "The calendar is ahead by 1461 − 1460.9688 = 0.0312 days."],
              "1461 days and 1460.9688 days", ncert=["4.4.four_years"]),
           WE("With a leap day every 4th year, how many days are in 100 calendar years? Compare with 100 revolutions.",
              ["100 years have 100/4 = 25 years divisible by 4, each with 1 extra day.",
               "Calendar: 100 × 365 + 25 × 1 = 36525 days.",
               "Another expression: 25 × 366 + 75 × 365 = 9150 + 27375 = 36525.",
               "Earth: 100 × 365.2422 = 36524.22 days.",
               "36525 − 36524.22 = 0.78, so the calendar is ahead by 0.78 days: we have overcompensated."],
              "36525 days against 36524.22 days, ahead by 0.78 days", ncert=["4.4.hundred_years"])],
       key_terms=["leap year"], misconceptions=[], minutes=10),
     A("T12.C3", "Not the 100th year, but the 400th", "Evaluate",
       "Students write the days in 100 and 1000 calendar years with no leap day in the 100th year, compare them "
       "with the Earth, and count the leap years in 1000 years under the 400th year rule.",
       textbook=["So, the good people who designed calendars decided that they will not add 1 extra day in every "
                 "hundredth year!",
                 "We saw that there are 25 years divisible by 4 in 100 years. 100 is also divisible by 4, but we have "
                 "to exclude it. So only 24 years have 366 days, and the rest (76 years) have 365 days.",
                 "(100/4 − 100/100) × 366 + (100 − (100/4 − 100/100)) × 365 = (24 × 366) + (76 × 365) = 36524 days.",
                 "This is close to 36524.22 days but is it close enough? What happens after 1000 years with this "
                 "adjustment?",
                 "The number of calendar days in 1000 years is 36524 × 10 = 365240 days. The number of days the Earth "
                 "takes to go around the Sun 1000 times is 1000 × 365.2422 = 365242.2 days. So, there is a difference "
                 "of 2.2 days.",
                 "To bridge this gap, it was decided that every 400th year would be a leap year!",
                 "So, the total number of days in 1000 calendar years is (750 × 365) + (240 × 366) + (8 × 365) + "
                 "(2 × 366) = 365242 days.",
                 "Hence, in 1000 years, the calendar year is slightly shorter (by 0.2 days) than the actual number of "
                 "days the Earth takes to go around the Sun.",
                 "Do you wonder how people figured out that the Earth completes one revolution around the Sun in "
                 "exactly 365.2422 days?",
                 "Investigate how traditional calendars in India managed to consistently align the days in the "
                 "calendar with astronomical events like the Earth going around the Sun or even the positions of the "
                 "stars in the sky accurately."],
       teach=["Predict first: if the 100th year has no leap day, is the calendar now behind the Earth after 1000 "
              "years?",
              "Each rule is checked the same way: count the 366-day years, add one day for each to 365 times the "
              "years, and compare with 365.2422 times the years.",
              "Wonder about it: people measured the year by watching the Sun, the Moon and the stars over many years, "
              "and traditional Indian calendars kept in step with the sky with their own corrections."],
       examples=[
           WE("With no leap day in the 100th year, how many days are in 100 calendar years and in 1000 calendar "
              "years? Compare with the Earth.",
              ["In 100 years, 25 years are divisible by 4 but the 100th is left out, so 24 years have 366 days and 76 "
               "have 365.",
               "(24 × 366) + (76 × 365) = 8784 + 27740 = 36524 days, against 36524.22.",
               "In 1000 years: 36524 × 10 = 365240 days.",
               "Earth: 1000 × 365.2422 = 365242.2 days, so the calendar is behind by 365242.2 − 365240 = 2.2 days."],
              "36524 days in 100 years; 365240 against 365242.2 in 1000 years, a gap of 2.2 days",
              ncert=["4.4.no_100th", "4.4.thousand"]),
           WE("Every 400th year is a leap year after all. Count the years of each kind in 1000 calendar years and find "
              "the total number of days.",
              ["Divisible by 400: 1000 ÷ 400 gives 2 years, each 366 days.",
               "Divisible by 100 but not by 400: 10 − 2 = 8 years, each 365 days.",
               "Divisible by 4 but not by 100: 250 − 10 = 240 years, each 366 days.",
               "The rest: 1000 − (2 + 8 + 240) = 750 years, each 365 days.",
               "(750 × 365) + (240 × 366) + (8 × 365) + (2 × 366) = 365242 days.",
               "Against 365242.2, the calendar is short by only 0.2 days."],
              "365242 days, short by 0.2 days", ncert=["4.4.rule_400", "4.4.how_measured", "4.4.try_calendars"])],
       key_terms=["leap year"], misconceptions=[], minutes=12),
     DOER("T12.C4", "Practice: test the leap year rules", "leap_rule_ledger", "Evaluate",
          "Students count leap years and ordinary years under the full rule for a long span, compare the calendar "
          "with the Earth, and suggest a fix for the gap.",
          ["Count the years divisible by 400, by 100 but not 400, and by 4 but not 100.",
           "Add 366 days for each leap year and 365 for each other year.",
           "Compare with 365.2422 times the number of years."],
          items=[
              FIO("4.4.try_10000", "Try This (10,000 years)",
                  "With this final scheme of leap years can you calculate the number of calendar days in 10,000 years "
                  "and the number of actual days the Earth will take to make 10,000 revolutions around the Sun? What "
                  "is the difference? If there is a big difference, can you suggest a way to fix this problem?",
                  ["Divisible by 400: 25 years. Divisible by 100 but not 400: 100 − 25 = 75 years.",
                   "Divisible by 4 but not 100: 2500 − 100 = 2400 years. The rest: 10000 − 2500 = 7500 years.",
                   "Calendar: (2400 + 25) × 366 + (7500 + 75) × 365 = 887550 + 2764875 = 3652425 days.",
                   "Earth: 10000 × 365.2422 = 3652422 days.",
                   "The calendar is 3652425 − 3652422 = 3 days ahead.",
                   "One fix: drop 3 leap days every 10000 years, for example no leap day in years divisible by 4000."],
                  "3652425 calendar days against 3652422; the calendar is 3 days ahead, which could be fixed by "
                  "dropping about 3 leap days every 10000 years", tool="leap_rule_ledger"),
          ])]))

# ============================== T13 Everyday decimal problems ==================================================
TOPICS.append(TOPIC(
    "T13", "M3", "Decimals in Everyday Problems", ["Figure it Out"], "Apply",
    "Students choose decimal multiplication or division to find which pack is cheaper per gram, read decimals on "
    "number lines, find profit, fit books on a shelf, convert units, and divide mixed fractions as decimals.",
    "Decide first whether the story multiplies or divides; then use the decimal rules and check the units.",
    [A("T13.C1", "Which pack is cheaper?", "Apply",
       "Students compare two packs of different weights by finding the price of 1 gram of each by decimal "
       "division.",
       teach=["Predict first: is a bigger pack always cheaper?",
              "Find the price of 1 gram of each pack by dividing the price by the weight.",
              "Compare the two prices per gram."],
       examples=[
           WE("A 250 g pack of biscuits costs ₹40 and a 150 g pack costs ₹27. Which is cheaper?",
              ["Price of 1 g in the big pack: 40 ÷ 250 = 4/25 = 16/100 = 0.16, so ₹0.16.",
               "Price of 1 g in the small pack: 27 ÷ 150 = 9/50 = 18/100 = 0.18, so ₹0.18.",
               "0.16 < 0.18, so the 250 g pack is cheaper."],
              "The 250 g pack, at ₹0.16 per gram against ₹0.18", ncert=[])],
       key_terms=["per"], misconceptions=["M_UNIT_MIX"], minutes=8),
     DOER("T13.C2", "Practice: everyday decimal problems", None, "Apply",
          "Students solve price, number line, profit, shelf, unit and mixed fraction problems with decimal "
          "multiplication and division.",
          ["Decide whether to multiply or divide.", "Convert units before comparing.",
           "Check that the answer is a sensible size."],
          items=[
              FIO("4.4.end1", "End of chapter Figure it Out, Q1",
                  "A 210 gram packet of peanut chikki costs ₹70.5, while a 110 gram packet of potato chips costs "
                  "₹33.25. Which is cheaper?",
                  ["Chikki: 70.5 ÷ 210 = 0.3357..., so about ₹0.336 per gram.",
                   "Chips: 33.25 ÷ 110 = 0.3022..., so about ₹0.302 per gram.",
                   "0.302 < 0.336, so the potato chips are cheaper per gram."],
                  "The potato chips (about ₹0.302 per gram against about ₹0.336)"),
              FIO("4.4.end2", "End of chapter Figure it Out, Q2",
                  "Write the decimal number at the arrow mark: (a) a number line from 3.1 to 3.2 split into 10 equal "
                  "parts, with the arrow at the 6th mark after 3.1 (b) a number line from 2.15 to 2.17 split into 10 "
                  "equal parts, with the arrow at the 6th mark after 2.15",
                  ["(a) The gap 3.2 − 3.1 = 0.1 is split into 10 parts, so each part is 0.1 ÷ 10 = 0.01.",
                   "The arrow is 6 parts after 3.1, at 3.1 + 6 × 0.01 = 3.16.",
                   "(b) The gap 2.17 − 2.15 = 0.02 is split into 10 parts, so each part is 0.02 ÷ 10 = 0.002.",
                   "The middle mark is 2.16; the arrow is 6 parts after 2.15, at 2.15 + 6 × 0.002 = 2.162."],
                  "(a) 3.16 (b) 2.162"),
              FIO("4.4.end3", "End of chapter Figure it Out, Q3",
                  "Shyamala bought 3 kg bananas at ₹30 per kg. She counted 35 bananas in all. She sells each banana "
                  "for ₹5. How much profit does she make selling all the bananas?",
                  ["Cost: 3 × 30 = 90, so ₹90.", "Sales: 35 × 5 = 175, so ₹175.",
                   "Profit: 175 − 90 = 85, so ₹85."], "₹85"),
              FIO("4.4.end4", "End of chapter Figure it Out, Q4",
                  "A teacher placed books that are 2.5 cm thick on a bookshelf. The teacher wanted to place 80 "
                  "books on the shelf. The bookshelf is 160 cm long. How many books could be placed on the shelf? "
                  "Was there any space left? If yes, how much?",
                  ["Books that fit: 160 ÷ 2.5 = 1600 ÷ 25 = 64.", "64 books take 64 × 2.5 = 160 cm, so no space is left.",
                   "80 books would need 80 × 2.5 = 200 cm, more than the shelf."],
                  "64 books; no space left (80 books would need 200 cm)"),
              FIO("4.4.end5", "End of chapter Figure it Out, Q5",
                  "Fill in the following blanks appropriately (1 cm = 10 mm, 1 m = 100 cm, 1 km = 1000 m, "
                  "1 kg = 1000 g, 1 g = 1000 mg, 1 l = 1000 ml): 5.5 km = ___ m, 35 cm = ___ m, 14.5 cm = ___ mm, "
                  "68 g = ___ kg, 9.02 m = ___ mm, 125.5 ml = ___ l",
                  ["5.5 × 1000 = 5500, so 5.5 km = 5500 m.", "35 ÷ 100 = 0.35, so 35 cm = 0.35 m.",
                   "14.5 × 10 = 145, so 14.5 cm = 145 mm.", "68 ÷ 1000 = 0.068, so 68 g = 0.068 kg.",
                   "9.02 × 1000 = 9020, so 9.02 m = 9020 mm.", "125.5 ÷ 1000 = 0.1255, so 125.5 ml = 0.1255 l."],
                  "5500 m, 0.35 m, 145 mm, 0.068 kg, 9020 mm, 0.1255 l"),
              FIO("4.4.end6", "End of chapter Figure it Out, Q6",
                  "The following problem was set by Sridharacharya in his book, Patiganita. \"6 1/4 is divided by "
                  "2 1/2, and 60 1/4 is divided by 3 1/2. Tell the quotients separately.\" Can you try to solve it by "
                  "converting the fractions into decimals?",
                  ["6 1/4 = 6.25 and 2 1/2 = 2.5, so 6.25 ÷ 2.5 = 62.5 ÷ 25 = 2.5.",
                   "60 1/4 = 60.25 and 3 1/2 = 3.5, so 60.25 ÷ 3.5 = 602.5 ÷ 35.",
                   "Long division: 602.5 ÷ 35 = 17.2142857..., which is 241/14; it does not end."],
                  "2.5 and 17.2142857... (that is 241/14)"),
          ])]))

# ============================== T14 Reasoning with decimals ====================================================
TOPICS.append(TOPIC(
    "T14", "M3", "Reasoning with Products and Quotients", ["Figure it Out"], "Evaluate",
    "Students use a given product or quotient to find related ones, fill boxes to make a given product, complete a "
    "table of quotients, arrange digits to reach a target product, and order expressions by size without computing "
    "them.",
    "The digits of a product or quotient come from the whole numbers; the decimal point, and the size, come from "
    "reasoning.",
    [A("T14.C1", "One fact, many answers", "Analyze",
       "Students use one given whole-number product to write related decimal products and quotients by reasoning "
       "about decimal places and size.",
       teach=["Predict first: given 45 × 12 = 540, is 4.5 × 1.2 nearer 5 or nearer 50?",
              "The digits stay the same; the decimal places and a size check place the point.",
              "For a quotient, multiply the dividend and the divisor by the same 10 or 100 to reach the given fact."],
       examples=[
           WE("Given 45 × 12 = 540, find 4.5 × 1.2, 0.45 × 12 and 54 ÷ 1.2.",
              ["4.5 × 1.2: 1 + 1 = 2 decimal places, so 4.5 × 1.2 = 5.40 = 5.4.",
               "0.45 × 12: 2 decimal places, so 0.45 × 12 = 5.40 = 5.4.",
               "54 ÷ 1.2 = 540 ÷ 12 = 45."],
              "5.4, 5.4 and 45", ncert=[])],
       key_terms=["product", "quotient"], misconceptions=["M_POINT_ALIGN", "M_DIVISOR_ONLY"], minutes=8),
     DOER("T14.C2", "Pull it together and do it: reasoning with decimals", None, "Evaluate",
          "Students use reasoning with decimal places to fill boxes for given products, use 756 ÷ 36 = 21 to find related quotients, complete a "
          "table of a ÷ b, arrange digits for target products, and order expressions by size.",
          ["Use the given whole-number fact for the digits.",
           "Use decimal places, or multiply both numbers in a division by the same 10, to place the point.",
           "Multiplying or dividing by a number less than 1 changes the size the other way."],
          items=[
              FIO("4.4.end7", "End of chapter Figure it Out, Q7",
                  "Fill the boxes in at least 2 different ways: (a) □ × □ = 2.4 (b) □ × □ = 14.5",
                  ["(a) 12 × 2 = 24, so 1.2 × 2 = 2.4; also 6 × 4 = 24, so 0.6 × 4 = 2.4.",
                   "(b) 29 × 5 = 145, so 2.9 × 5 = 14.5; also 145 × 10 = 1450, so 1.45 × 10 = 14.5."],
                  "(a) for example 1.2 × 2 and 0.6 × 4 (b) for example 2.9 × 5 and 1.45 × 10"),
              FIO("4.4.end8", "End of chapter Figure it Out, Q8",
                  "Find the following quotients given that 756 ÷ 36 = 21: (a) 75.6 ÷ 3.6 (b) 7.56 ÷ 0.36 "
                  "(c) 756 ÷ 0.36 (d) 75.6 ÷ 360 (e) 7560 ÷ 3.6 (f) 7.56 ÷ 0.36",
                  ["(a) 75.6 ÷ 3.6 = 756 ÷ 36 = 21.", "(b) 7.56 ÷ 0.36 = 756 ÷ 36 = 21.",
                   "(c) 756 ÷ 0.36 = 75600 ÷ 36 = 2100.", "(d) 75.6 ÷ 360 = 756 ÷ 3600 = 0.21.",
                   "(e) 7560 ÷ 3.6 = 75600 ÷ 36 = 2100.", "(f) is the same division as (b), so it is 21."],
                  "(a) 21 (b) 21 (c) 2100 (d) 0.21 (e) 2100 (f) 21"),
              FIO("4.4.end9", "End of chapter Figure it Out, Q9",
                  "Find the missing cells if each cell represents a ÷ b. Rows b: 37, 3.7, 0.37, 0.037, 370. Columns a: "
                  "1517, 151.7, 15.17, 1.517, 15170. Given: 1517 ÷ 37 = 41, 15.17 ÷ 3.7 = 4.1, 151.7 ÷ 0.037 = 4100.",
                  ["Each step right in a divides the quotient by 10; the last column multiplies it by 10. Each step "
                   "down in b multiplies the quotient by 10; the last row divides it by 10.",
                   "b = 37: 41, 4.1, 0.41, 0.041, 410.", "b = 3.7: 410, 41, 4.1, 0.41, 4100.",
                   "b = 0.37: 4100, 410, 41, 4.1, 41000.", "b = 0.037: 41000, 4100, 410, 41, 410000.",
                   "b = 370: 4.1, 0.41, 0.041, 0.0041, 41."],
                  "37: 41, 4.1, 0.41, 0.041, 410; 3.7: 410, 41, 4.1, 0.41, 4100; 0.37: 4100, 410, 41, 4.1, 41000; "
                  "0.037: 41000, 4100, 410, 41, 410000; 370: 4.1, 0.41, 0.041, 0.0041, 41"),
              FIO("4.4.end10", "End of chapter Figure it Out, Q10",
                  "Using the digits 2, 4, 5, 8, and 0 fill the boxes □□.□ × □.□ to get the: (a) maximum product "
                  "(b) minimum product (c) product greater than 150 (d) product nearest to 100 (e) product nearest "
                  "to 5",
                  ["(a) Put the biggest digits in the biggest places: 82.0 × 5.4 = 442.8.",
                   "(b) Make the second number as small as possible: 45.8 × 0.2 = 9.16.",
                   "(c) For example 28.0 × 5.4 = 151.2.",
                   "(d) 20.5 × 4.8 = 98.4 is nearest to 100.",
                   "(e) The smallest product, 45.8 × 0.2 = 9.16, is the nearest to 5."],
                  "(a) 82.0 × 5.4 = 442.8 (b) 45.8 × 0.2 = 9.16 (c) for example 28.0 × 5.4 = 151.2 "
                  "(d) 20.5 × 4.8 = 98.4 (e) 45.8 × 0.2 = 9.16"),
              FIO("4.4.end11", "End of chapter Figure it Out, Q11",
                  "Sort the following expressions in increasing order: (a) 245.05 × 0.942368 (b) 245.05 × 7.9682 "
                  "(c) 245.05 ÷ 7.9682 (d) 245.05 ÷ 0.942368 (e) 245.05 (f) 7.9682",
                  ["Multiplying by 0.942368, which is less than 1, makes 245.05 a little smaller: (a) is about 230.9.",
                   "Dividing by 0.942368 makes it a little bigger: (d) is about 260.0.",
                   "Multiplying by 7.9682 makes it about 8 times bigger: (b) is about 1952.6.",
                   "Dividing by 7.9682 makes it about 8 times smaller: (c) is about 30.75.",
                   "So (f) 7.9682 < (c) < (a) < (e) 245.05 < (d) < (b)."],
                  "(f) < (c) < (a) < (e) < (d) < (b)"),
          ])]))

# ============================== T15 Hidato =====================================================================
TOPICS.append(TOPIC(
    "T15", "M4", "Puzzle Time: Hidato", ["Puzzle"], "Analyze",
    "Students fill a Hidato grid with a continuous path of consecutive numbers from the lowest to the highest, "
    "moving to any adjacent cell, including diagonally.",
    "A Hidato path joins consecutive numbers through touching cells; the given numbers pin the path down.",
    [A("T15.C1", "Find the path of consecutive numbers", "Analyze",
       "",
       textbook=["Hidato",
                 "In Hidato, a grid of cells is given. It is usually square-shaped, like Sudoku or Kakuro, but it can "
                 "also include hexagons or any shape that forms a tessellation. It can have inner holes (like a disc), "
                 "but it is made of only one piece.",
                 "Usually, in every Hidato puzzle the lowest and the highest numbers are given on the grid.",
                 "Your task is to fill the grid such that there is a continuous path of consecutive numbers from the "
                 "lowest to the highest number. The next number must be in any one of the adjacent cells, including "
                 "diagonally adjacent cells.",
                 "The grid comes pre-filled with some numbers (with values between the smallest and the highest) to "
                 "ensure that these puzzles have a single solution.",
                 "Try solving the following Hidato puzzles.",
                 "In each grid below, a number is a given cell, □ is a cell to fill and · is no cell.",
                 "Solved example (1 to 40), row 1: □ 33 35 □ □ · · ·",
                 "Solved example (1 to 40), row 2: □ □ 24 22 □ · · ·",
                 "Solved example (1 to 40), row 3: □ □ □ 21 □ □ · ·",
                 "Solved example (1 to 40), row 4: □ 26 □ 13 40 11 · ·",
                 "Solved example (1 to 40), row 5: 27 □ □ □ 9 □ 1 ·",
                 "Solved example (1 to 40), row 6: · · □ □ 18 □ □ ·",
                 "Solved example (1 to 40), row 7: · · · · □ 7 □ □",
                 "Solved example (1 to 40), row 8: · · · · · · 5 □",
                 "Practice grid 1 (1 to 25), row 1: 25 □ 1 □ □",
                 "Practice grid 1 (1 to 25), row 2: □ 20 □ □ 4",
                 "Practice grid 1 (1 to 25), row 3: □ 14 □ 8 □",
                 "Practice grid 1 (1 to 25), row 4: □ □ 15 □ 9",
                 "Practice grid 1 (1 to 25), row 5: □ □ □ □ □",
                 "Practice grid 2 (1 to 39), row 1: · 36 1 2 □ □ ·",
                 "Practice grid 2 (1 to 39), row 2: □ □ □ 4 6 13 □",
                 "Practice grid 2 (1 to 39), row 3: □ · 34 □ □ 12 □",
                 "Practice grid 2 (1 to 39), row 4: 39 · · 30 □ · □",
                 "Practice grid 2 (1 to 39), row 5: · · 31 □ □ · ·",
                 "Practice grid 2 (1 to 39), row 6: · □ □ □ □ 17 ·",
                 "Practice grid 2 (1 to 39), row 7: □ 26 □ 23 21 □ □",
                 "Practice grid 3 (1 to 56), row 1: · · · · □ 9 · · · ·",
                 "Practice grid 3 (1 to 56), row 2: · · · · 7 10 · · · ·",
                 "Practice grid 3 (1 to 56), row 3: · · □ □ □ □ □ □ · ·",
                 "Practice grid 3 (1 to 56), row 4: · · 5 □ □ 1 17 15 · ·",
                 "Practice grid 3 (1 to 56), row 5: · □ □ □ □ □ □ □ □ ·",
                 "Practice grid 3 (1 to 56), row 6: · 44 □ 49 □ □ 28 □ □ ·",
                 "Practice grid 3 (1 to 56), row 7: □ 54 42 □ 50 □ 29 26 □ □",
                 "Practice grid 3 (1 to 56), row 8: 56 □ □ □ □ 35 34 25 23 □",
                 "Practice grid 3 (1 to 56), row 9: · · · · □ □ · · · ·",
                 "Practice grid 3 (1 to 56), row 10: · · · · 39 □ · · · ·"],
       teach=["Start at 1 and look for the next given number: how many steps away is it, and how many cells lie "
              "between?",
              "Fill the cells that have only one possible neighbour first; a cell with one open neighbour must be an "
              "end of a gap.",
              "In the solved example the path runs from 1 to 40; check every step touches the last one, side or "
              "corner. Two cells of the printed solution are misprinted: read 29 where 39 is printed in the fourth "
              "row, and 6 where 16 is printed in the seventh row.",
              "Solved example, completed path, row 1: 32 33 35 36 37 · · ·",
              "Solved example, completed path, row 2: 31 34 24 22 38 · · ·",
              "Solved example, completed path, row 3: 30 25 23 21 12 39 · ·",
              "Solved example, completed path, row 4: 29 26 20 13 40 11 · ·",
              "Solved example, completed path, row 5: 27 28 14 19 9 10 1 ·",
              "Solved example, completed path, row 6: · · 15 16 18 8 2 ·",
              "Solved example, completed path, row 7: · · · · 17 7 6 3",
              "Solved example, completed path, row 8: · · · · · · 5 4",
              "Practice grid 1, completed path, row 1: 25 23 1 2 3",
              "Practice grid 1, completed path, row 2: 24 20 22 5 4",
              "Practice grid 1, completed path, row 3: 19 14 21 8 6",
              "Practice grid 1, completed path, row 4: 18 13 15 7 9",
              "Practice grid 1, completed path, row 5: 17 16 12 11 10",
              "Practice grid 2 cannot be completed as printed: it has 37 cells, but its path must run from 1 to 39, which needs 39 cells. Count the cells to see why.",
              "Practice grid 3, completed path, row 1: · · · · 8 9 · · · ·",
              "Practice grid 3, completed path, row 2: · · · · 7 10 · · · ·",
              "Practice grid 3, completed path, row 3: · · 4 6 11 12 13 14 · ·",
              "Practice grid 3, completed path, row 4: · · 5 3 2 1 17 15 · ·",
              "Practice grid 3, completed path, row 5: · 45 46 47 48 31 16 18 19 ·",
              "Practice grid 3, completed path, row 6: · 44 43 49 32 30 28 27 20 ·",
              "Practice grid 3, completed path, row 7: 55 54 42 51 50 33 29 26 24 21",
              "Practice grid 3, completed path, row 8: 56 53 52 41 36 35 34 25 23 22",
              "Practice grid 3, completed path, row 9: · · · · 40 37 · · · ·",
              "Practice grid 3, completed path, row 10: · · · · 39 38 · · · ·"],
       ncert=["puzzle.hidato"], key_terms=[], enrichment=True, minutes=8),
     DOER("T15.C2", "Practice: solve the Hidato grids", None, "Analyze",
          "",
          ["Every number touches the next one, side or corner.",
           "Count the gap between two given numbers and the cells that can fill it."],
          enrichment=True)]))

# ============================== T16 Summary ====================================================================
TOPICS.append(TOPIC(
    "T16", "M4", "Summary: Another Peek Beyond the Point", ["Summary"], "Remember",
    None,
    "Multiplying decimals through fractions and decimal places, long division past the Ones, dividing by a decimal, "
    "divisions that never end, and leap years in one place.",
    [A("T16.C1", "What we found about multiplying and dividing decimals", "Remember",
       "Students restate the rule of decimal places for multiplication, the long division procedure that regroups "
       "past the Ones, how to divide by a decimal, and that some divisions never end.",
       textbook=["Summary",
                 "In this chapter, we learnt procedures to perform decimal multiplication and division.",
                 "For decimal multiplication, we first multiply the multiplier and multiplicand as counting numbers. "
                 "The number of decimal digits in the product is the total number of decimal digits in the multiplier "
                 "and multiplicand.",
                 "Division of decimals uses the same procedure, i.e., division using place value (long division), as "
                 "with counting numbers. The regrouping continues after the Ones place to Tenths, Hundredths, "
                 "Thousandths, and so on. When the Ones are regrouped to Tenths, a decimal point is placed in the "
                 "quotient.",
                 "There are decimal divisions where the quotient never ends. After each regrouping and dividing there "
                 "is always a remainder!"],
       teach=["Our opening question is settled: Arshad pays 9.5 × 5 = 47.5, that is ₹47.5, for 5 pens.",
              "Multiply as counting numbers, then count decimal places; divide by long division, putting the point "
              "in when Ones become Tenths; make a decimal divisor a counting number first.",
              "Still open for you: does 3 ÷ 11 ever end, and what repeats?"],
       ncert=["summary"], video_focus=["RECAP"], minutes=8)],
    topic_type="summary"))
