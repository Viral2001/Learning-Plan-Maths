# -*- coding: utf-8 -*-
"""Topics T1 to T4 (module M1: big numbers). Chapter opening, Reading and writing large numbers, the token table,
and number patterns."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Journeys and big numbers (opening) ======================================
TOPICS.append(TOPIC(
    "T1", "M1", "Journeys and Big Numbers", ["Chapter opening"], "Understand",
    "",
    "A trip is a story of big numbers: how far, how long, how many people. The odometer of a vehicle shows the "
    "distance as a number that keeps growing.",
    [A("T1.C1", "How far did you go on your last trip?", "Understand",
       "",
       textbook=["When was the last time you went on a long trip? Where did you go? How did you travel? What was the "
                 "duration of your trip? How much distance did you cover? Ask the elders who went with you to help you "
                 "answer these questions.",
                 "Human beings have always been interested in travelling. About a hundred years ago, there were far "
                 "fewer vehicles than today. There were animal-drawn carts, cars, and trains. Long before this, "
                 "thousands of years ago, people travelled long distances on foot or used animals to travel from one "
                 "place to another. They also built boats and ships to travel across lakes, rivers, and seas. Boats "
                 "were probably the first form of transport invented by humans, much before bullock carts! Do you "
                 "know how many vehicles are currently there in your state?"],
       teach=["Predict first: on your last long trip, how many kilometres did you cover, and did the number have "
              "three digits, four digits or more?",
              "People have always travelled, first on foot and on animals, then in boats, carts, cars and trains.",
              "Distances, times and the number of vehicles are all numbers, and the farther we go, the bigger the "
              "numbers get. Can you read and write a number like 12,214 without a mistake?"],
       ncert=["opening"], key_terms=["distance", "journey"], video_focus=["HOOK"], minutes=4, enrichment=True),
     DOER("T1.C2", "Try it: read the odometer", "odometer_reader", "Understand", "",
          ["An odometer shows how many kilometres a vehicle has covered.",
           "Each wheel of the odometer is one place: ones, tens, hundreds, thousands and now ten thousands.",
           "When the ones wheel passes 9 it turns back to 0 and moves the next wheel by one."],
          role="try_it", enrichment=True)],
    topic_type="framing"))

# ============================== T2 Ten thousand ============================================================
TOPICS.append(TOPIC(
    "T2", "M1", "Ten Thousand and the TTh Column", ["Reading and writing large numbers"], "Apply",
    "Students count by thousands to ten thousand, name the new Ten Thousands (TTh) column, write ten thousand as "
    "10,000, and read and write numbers such as 1,380 and 9,123 in expanded form with commas.",
    "Adding a thousand to 9,000 gives ten thousand, 10,000. The place value chart gets a new column, TTh, ten "
    "times the Thousands, and a comma helps us read large numbers.",
    [A("T2.C1", "What comes after nine thousand?", "Understand",
       "Students count in thousands up to 9,000 and say that adding one more thousand gives ten thousand.",
       textbook=["How do you write numbers to show several thousand objects?",
                 "Let us start with 1,000. What numbers do we get when we keep adding a thousand?",
                 "1,000 2,000 ... 9,000",
                 "What number do we get when we add a thousand to 9,000? We get ten thousand. How do we write this "
                 "number?"],
       teach=["Predict first: if you keep adding a thousand to 1,000, which number comes after 9,000?",
              "1,000, 2,000, 3,000, and so on up to 9,000. Each step adds one more thousand.",
              "9,000 + 1,000 = 10,000. Ten thousands make ten thousand, and the number needs a new place."],
       examples=[WE("Keep adding a thousand to 1,000. Which number do you reach after 9,000, and how many thousands "
                    "is it?",
                    ["1,000, 2,000, 3,000, 4,000, 5,000, 6,000, 7,000, 8,000, 9,000.",
                     "One more thousand: 9,000 + 1,000 = 10,000.",
                     "10,000 is 10 thousands, called ten thousand."],
                    "10,000, which is ten thousand and is 10 thousands",
                    ncert=["r.thousands", "r.ten_thousand"])],
       key_terms=["thousand", "ten thousand"], misconceptions=["M_TT_COLUMN"], minutes=7),
     A("T2.C2", "The new TTh column", "Understand",
       "Students extend the place value chart with a TTh column, state that 10 thousands is 1 ten thousand and that "
       "10 tens, 10 hundreds and 10 thousands each make the next place, and write 10,000.",
       textbook=["Look at the table below and notice the pattern of writing numbers. In the place value chart, we "
                 "have added another column, TTh. It stands for ten thousand.",
                 "10 Ones = 1 Ten = 10, 10 Tens = 1 Hundred = 100, 10 Hundreds = 1 Thousand = 1,000.",
                 "In the same way, 10 Thousands = Ten Thousand = 10,000.",
                 "We use a comma to help us read large numbers easily."],
       teach=["Predict first: the chart has columns for ones, tens, hundreds and thousands. Where will 10 thousands "
              "go?",
              "Ten of one place always make one of the next place to the left: 10 ones, 10 tens, 10 hundreds, 10 "
              "thousands.",
              "So 10 thousands make 1 in a new column, TTh, with zeros in the four places to its right: 10,000.",
              "The comma sits after the thousands place and helps the eye read the number."],
       examples=[WE("Write ten thousand in the place value chart and say how many thousands make it.",
                    ["10 Thousands = 1 Ten Thousand.",
                     "In the chart: 1 in the TTh column and 0 in the Th, H, T and O columns.",
                     "With the comma: 10,000."],
                    "1 TTh and four zeros, written 10,000, which is 10 thousands",
                    ncert=["r.place_chart", "r.comma"])],
       key_terms=["TTh", "place value chart", "comma"], misconceptions=["M_TT_COLUMN", "M_COMMA_PLACE"], minutes=8),
     A("T2.C3", "Reading numbers in the Indian place value system", "Apply",
       "Students read and write a number as thousands, hundreds, tens and ones, such as 1,380 and 9,123, using the "
       "same ten digits in different places.",
       textbook=["Do you remember how we read and write numbers in the Indian place value system? We use the same ten "
                 "digits 0 to 9 in different places to write larger numbers.",
                 "For example, 1,380 = 1 Thousand + 3 Hundreds + 8 Tens + 0 Ones.",
                 "9,123 = 9 Thousands + 1 Hundred + 2 Tens + 3 Ones."],
       teach=["Predict first: in 1,380, which digit tells how many thousands and which tells how many tens?",
              "Read the number place by place from the left: thousands, hundreds, tens and ones.",
              "The digit 0 is not left out: it holds a place so that the other digits stay where they belong."],
       examples=[WE("Write 1,380 and 9,123 as thousands, hundreds, tens and ones.",
                    ["1,380: 1 Thousand, 3 Hundreds, 8 Tens, 0 Ones.",
                     "1,380 = 1,000 + 300 + 80 + 0.",
                     "9,123 = 9 Thousands + 1 Hundred + 2 Tens + 3 Ones.",
                     "9,123 = 9,000 + 100 + 20 + 3."],
                    "1,380 = 1 Thousand + 3 Hundreds + 8 Tens + 0 Ones, and 9,123 = 9 Thousands + 1 Hundred + 2 "
                    "Tens + 3 Ones",
                    ncert=["r.indian_system", "r.expanded_1380", "r.expanded_9123"])],
       key_terms=["place value", "digit"], misconceptions=["M_ZERO_NAME"], minutes=8),
     DOER("T2.C4", "Practice: build ten thousand", "ten_thousand_builder", "Apply",
          "Students build numbers from ones to ten thousand by dropping tokens in the place value chart, watch ten "
          "tokens regroup into one of the next place, and read each number aloud.",
          ["Ten of one place make one of the next place.",
           "Nine thousands and one more thousand make a new TTh token.",
           "A comma helps us read large numbers."],
          examples=[WE("Make 12,000 from thousand tokens and say how many TTh and Th tokens are in the chart.",
                       ["12 thousand tokens: the first 10 regroup into 1 TTh token.",
                        "2 thousand tokens remain.",
                        "The chart shows TTh 1, Th 2, and the number is 12,000."],
                       "1 TTh token and 2 Th tokens, the number 12,000")])],
    key_terms=["ten thousand", "TTh", "comma", "place value"]))

# ============================== T3 Reading and writing five-digit numbers ==================================
TOPICS.append(TOPIC(
    "T3", "M1", "Reading and Writing Five-Digit Numbers", ["Reading and writing large numbers"], "Apply",
    "Students read tokens as a number, write the number in the place value chart with commas, and write the number "
    "name for five-digit numbers from 10,001 to 99,999.",
    "Five-digit numbers are written like the numbers below 9,999, with a TTh place. Read the thousands part first, "
    "then the hundreds, tens and ones, and write the name in words.",
    [A("T3.C1", "Numbers just after ten thousand", "Apply",
       "Students write the numbers made by 10,000 and a few ones or tens, such as 10,001, 10,002, 10,010 and 10,024, "
       "in the chart and in words.",
       textbook=["Let us see how we write numbers beyond 10,000 and how we name them. We write them in the same way as "
                 "numbers below 9,999. You can use the tokens given in the end of the book.",
                 "10,001: TTh 1, Th 0, H 0, T 0, O 1: Ten thousand one.",
                 "10,002: TTh 1, Th 0, H 0, T 0, O 2: Ten thousand two.",
                 "10,010: TTh 1, Th 0, H 0, T 1, O 0: Ten thousand ten.",
                 "10,024: TTh 1, Th 0, H 0, T 2, O 4: Ten thousand twenty-four."],
       teach=["Predict first: one 10,000 token and one 1 token, what number is it and how do we say it?",
              "10,000 + 1 = 10,001, said ten thousand one. The zeros hold the Th, H and T places.",
              "The same idea works for 10,002, 10,010 and 10,024: the TTh digit stays 1 and only the small places "
              "change."],
       examples=[WE("One 10,000 token with two 1 tokens, one 10,000 token with one 10 token, and one 10,000 token with "
                    "two 10 tokens and four 1 tokens. Write each number and its name.",
                    ["10,000 + 2 = 10,002, Ten thousand two.",
                     "10,000 + 10 = 10,010, Ten thousand ten.",
                     "10,000 + 20 + 4 = 10,024, Ten thousand twenty-four."],
                    "10,002 is ten thousand two, 10,010 is ten thousand ten and 10,024 is ten thousand twenty-four",
                    ncert=["r.tok_10001_10002", "r.tok_10010_10024"])],
       key_terms=["number name", "token"], misconceptions=["M_ZERO_NAME"], minutes=8),
     A("T3.C2", "From tokens to numbers and names", "Apply",
       "Students count the tokens of each kind to write a number such as 10,033, 10,458, 11,214 or 13,520, fill its "
       "TTh, Th, H, T, O digits and say its name.",
       textbook=["10,033: Ten thousand thirty-three.",
                 "10,458: Ten thousand four hundred fifty-eight.",
                 "11,214: TTh 1, Th 1, H 2, T 1, O 4.",
                 "13,520: Thirteen thousand five hundred twenty."],
       teach=["Predict first: one 10,000 token, three 10 tokens and three 1 tokens, which number is it?",
              "Count each kind of token and put the count in its column: the number follows from the chart.",
              "To name it, read the thousands part first (ten thousand, eleven thousand, thirteen thousand), then the "
              "hundreds, tens and ones."],
       examples=[WE("Tokens: one 10,000, one 1,000, two 100, one 10, four 1. Write the number in the chart and its "
                    "name.",
                    ["TTh 1, Th 1, H 2, T 1, O 4.",
                     "10,000 + 1,000 + 200 + 10 + 4 = 11,214.",
                     "Name: Eleven thousand two hundred fourteen."],
                    "11,214, eleven thousand two hundred fourteen",
                    ncert=["r.tok_10033", "r.tok_10458", "r.tok_11214"])],
       key_terms=["token", "digit"], misconceptions=["M_COMMA_PLACE"], minutes=8),
     A("T3.C3", "Round ten thousands and bigger numbers", "Apply",
       "Students write 13,520, 20,000 and 45,867 as numbers and in words and see that the thousands part is read "
       "first.",
       textbook=["13,520: Thirteen thousand five hundred twenty.",
                 "20,000: Twenty thousand.",
                 "45,867: Forty-five thousand eight hundred sixty-seven."],
       teach=["Predict first: two 10,000 tokens, what number is it and how do we say it?",
              "2 ten thousands is 20,000, said twenty thousand.",
              "45,867 has 4 TTh, 5 Th, 8 H, 6 T and 7 O. Read the first two digits with the word thousand, then the "
              "rest."],
       examples=[WE("Write 45,867 in words and in expanded form.",
                    ["45 Thousand, then 8 Hundreds, 6 Tens and 7 Ones.",
                     "Forty-five thousand eight hundred sixty-seven.",
                     "45,867 = 40,000 + 5,000 + 800 + 60 + 7."],
                    "Forty-five thousand eight hundred sixty-seven",
                    ncert=["r.tok_13520", "r.tok_20000", "r.tok_45867"])],
       key_terms=["number name", "expanded form"], misconceptions=["M_COMMA_PLACE", "M_ZERO_NAME"], minutes=8),
     DOER("T3.C4", "Practice: build and name the numbers", "token_table_builder", "Apply",
          "Students build five-digit numbers from tokens, write each number with commas in the TTh to O chart, and "
          "write the number name from the thousands part first.",
          ["Count the tokens of each kind and place each count in its column.",
           "Zero holds a place when a column has no token.",
           "Name the number from the thousands part first, then the hundreds, tens and ones."],
          items=[FIO("LUD1.names", "Let Us Do 2, write the names",
                     "Fill in the number names for 7,209, 10,599, 13,579, 45,045, 39,593, 50,005, 26,050 and 81,200.",
                     ["7,209: 7 Thousands 2 Hundreds 0 Tens 9 Ones, Seven thousand two hundred nine.",
                      "10,599: Ten thousand five hundred ninety-nine.",
                      "13,579: Thirteen thousand five hundred seventy-nine.",
                      "45,045: Forty-five thousand forty-five.",
                      "39,593: Thirty-nine thousand five hundred ninety-three.",
                      "50,005: Fifty thousand five.",
                      "26,050: Twenty-six thousand fifty.",
                      "81,200: Eighty-one thousand two hundred."],
                     "Seven thousand two hundred nine, ten thousand five hundred ninety-nine, thirteen thousand five "
                     "hundred seventy-nine, forty-five thousand forty-five, thirty-nine thousand five hundred "
                     "ninety-three, fifty thousand five, twenty-six thousand fifty, eighty-one thousand two hundred"),
                 FIO("LUD1.numbers", "Let Us Do 2, write the numbers",
                     "Write with commas: Ten thousand seven hundred forty-three, Ten thousand ten, Fifty-six thousand "
                     "four hundred ninety-one, Ninety thousand nine, Twenty-three thousand two hundred thirty and "
                     "Thirty-six thousand one.",
                     ["Ten thousand seven hundred forty-three: 10,743.",
                      "Ten thousand ten: 10,010.",
                      "Fifty-six thousand four hundred ninety-one: 56,491.",
                      "Ninety thousand nine: 90,009.",
                      "Twenty-three thousand two hundred thirty: 23,230.",
                      "Thirty-six thousand one: 36,001."],
                     "10,743, 10,010, 56,491, 90,009, 23,230 and 36,001")])],
    key_terms=["number name", "token", "TTh"]))

# ============================== T4 Number patterns ==========================================================
TOPICS.append(TOPIC(
    "T4", "M1", "Number Patterns", ["Let Us Do"], "Analyze",
    "Students find the rule in a sequence of large numbers, say whether it adds or subtracts the same number each time, "
    "and continue the sequence.",
    "In a pattern of numbers, find how much each number changes from the one before. If the change is the same each "
    "time, that change is the rule and it gives the next numbers.",
    [A("T4.C1", "Adding the same number each time", "Apply",
       "Students find the amount added from one number to the next in a sequence and continue it.",
       teach=["Predict first: 2,000, 2,500, 3,000. What do you add to get from one number to the next?",
              "Subtract each number from the one after it: 2,500 − 2,000 = 500 and 3,000 − 2,500 = 500.",
              "The change is the same each time, 500, so the rule is add 500. The next numbers are 3,500, 4,000 and "
              "4,500."],
       examples=[WE("Find the rule and write the next three numbers: 2,000, 2,500, 3,000, 3,500.",
                    ["2,500 − 2,000 = 500.", "3,000 − 2,500 = 500.", "3,500 − 3,000 = 500.",
                     "The rule is add 500. Next: 4,000, 4,500, 5,000."],
                    "The rule is add 500; the next numbers are 4,000, 4,500 and 5,000")],
       key_terms=["pattern", "rule"], minutes=8),
     A("T4.C2", "Patterns that shrink", "Apply",
       "Students find the amount taken away in a decreasing sequence of large numbers and continue it.",
       teach=["Predict first: 9,000, 8,500, 8,000. Is the rule add or subtract, and how much?",
              "The numbers are getting smaller, so each number is the one before with something taken away.",
              "9,000 − 8,500 = 500 and 8,500 − 8,000 = 500: the rule is subtract 500, giving 7,500, 7,000, "
              "6,500."],
       examples=[WE("Find the rule and write the next three numbers: 9,000, 8,500, 8,000, 7,500.",
                    ["9,000 − 8,500 = 500.", "8,500 − 8,000 = 500.", "8,000 − 7,500 = 500.",
                     "The rule is subtract 500. Next: 7,000, 6,500, 6,000."],
                    "The rule is subtract 500; the next numbers are 7,000, 6,500 and 6,000")],
       key_terms=["pattern", "rule"], minutes=8),
     DOER("T4.C3", "Practice: find the rule", "pattern_rule_finder", "Analyze",
          "Students compare neighbouring numbers in a sequence to find the rule, test it by completing the blanks, and "
          "say whether the rule adds or subtracts.",
          ["Find how much each number changes from the one before.",
           "If the change is the same each time, that is the rule; write the next numbers by using it.",
           "Check the last number by adding or subtracting the rule once more."],
          items=[FIO("LUD1.p_abc", "Let Us Do 1 (a), (b), (c), continue the patterns",
                     "Fill in the blanks by continuing the pattern: (a) 456, 567, 678, _, _, _, _ (b) 1,050, _, 3,150, "
                     "4,200 (c) 5,501, 6,401, 7,301, _, _",
                     ["(a) 567 − 456 = 111, so add 111: 456, 567, 678, 789, 900, 1,011, 1,122.",
                      "(b) 4,200 − 3,150 = 1,050, so add 1,050: 1,050, 2,100, 3,150, 4,200.",
                      "(c) 6,401 − 5,501 = 900, so add 900: 5,501, 6,401, 7,301, 8,201, 9,101."],
                     "(a) add 111: 789, 900, 1,011, 1,122; (b) add 1,050: 2,100; (c) add 900: 8,201, 9,101"),
                 FIO("LUD1.p_defg", "Let Us Do 1 (d), (e), (f), (g), continue the patterns",
                     "(d) 10,100, 10,200, 10,300, ... 10,900 (e) 10,105, 10,125, _, _ (f) 10,992, 10,993, _, _ (g) 10,794, "
                     "10,796, 10,798, _, _",
                     ["(d) The rule is add 100: 10,100, 10,200, 10,300, 10,400, 10,500, 10,600, 10,700, 10,800, 10,900.",
                      "(e) 10,125 − 10,105 = 20, so add 20: 10,105, 10,125, 10,145, 10,165.",
                      "(f) The rule is add 1: 10,992, 10,993, 10,994, 10,995.",
                      "(g) The rule is add 2: 10,794, 10,796, 10,798, 10,800, 10,802."],
                     "(d) add 100; (e) add 20: 10,145, 10,165; (f) 10,994, 10,995; (g) 10,800, 10,802"),
                 FIO("LUD1.p_hi", "Let Us Do 1 (h), (i), continue the patterns",
                     "(h) 73,005, 72,004, _, _ (i) 82,350, 83,350, _, _",
                     ["(h) 73,005 − 72,004 = 1,001, so subtract 1,001: 73,005, 72,004, 71,003, 70,002.",
                      "(i) 83,350 − 82,350 = 1,000, so add 1,000: 82,350, 83,350, 84,350, 85,350."],
                     "(h) subtract 1,001: 71,003, 70,002; (i) add 1,000: 84,350, 85,350")])],
    key_terms=["pattern", "rule", "sequence"]))
