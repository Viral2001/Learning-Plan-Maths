# -*- coding: utf-8 -*-
"""Topics T1 to T5 (module M1: Journeys and Big Numbers). The framing intro (hook, Travelling Then and Now, the free
Travel Explorer), the new Ten Thousands place, Read the Numbers, Write the Numbers and Number Patterns.
Every teaching concept has one worked example with the plan's own numbers; every book question is an FIO item of
its topic's DOER, in the book's order."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Journeys and Big Numbers (framing) ======================================
TOPICS.append(TOPIC(
    "T1", "M1", "Journeys and Big Numbers", ["Chapter opening"], "Understand",
    "",
    "A journey is full of numbers: how far we go, how long it takes and how many vehicles are on the road. People "
    "once travelled on foot, on animals and in boats. Today there are many more vehicles, and big numbers help us "
    "count them.",
    [A("T1.C1", "My Last Journey", "Understand",
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
       teach=["Predict first: think of your last long trip. Was the distance a 2-digit number of kilometres, a "
              "3-digit number, or more?",
              "Every trip is full of numbers: how far you went, how long it took and how many people came with you.",
              "Ask the elders who went with you to help you answer. Then wonder: how many vehicles are there in "
              "your state?",
              "Big journeys and many vehicles need big numbers. We will see how to read and write them."],
       ncert=["opening", "open.vehicles"], key_terms=["journey", "distance", "duration"],
       video_focus=["HOOK"], enrichment=True, minutes=4),
     DOER("T1.C3", "Travelling Then: Explore", "travel_explorer", "Understand",
          "",
          ["People first travelled on foot and on animals.",
           "Boats were probably the first transport humans invented, much before bullock carts.",
           "About a hundred years ago there were animal-drawn carts, cars and trains, and far fewer vehicles than "
           "today."],
          role="try_it", enrichment=True)],
    topic_type="framing", key_terms=["journey", "transport", "vehicle"]))

# ============================== T1B Travelling Then and Now (a short idea topic after the intro) ===========
# The priority doc puts this concept video between the hook and the Travel Explorer; the pipeline allows exactly one
# video in the framing topic (the hook), so the concept video opens the next topic.
TOPICS.append(TOPIC(
    "T1B", "M1", "Travelling Then and Now", ["Chapter opening"], "Understand",
    "Students name the ways of travelling of long ago and of about a hundred years ago and say which is older, a "
    "boat or a bullock cart.",
    "People travelled on foot and on animals, then in boats and ships, and about a hundred years ago also in "
    "animal-drawn carts, cars and trains. There were far fewer vehicles than there are today.",
    [A("T1B.C1", "Travelling Then and Now", "Understand",
       "Students name the ways of travelling of long ago and of about a hundred years ago and say which is older, a boat or a bullock cart.",
       textbook=["Human beings have always been interested in travelling. About a hundred years ago, there were far "
                 "fewer vehicles than today. There were animal-drawn carts, cars, and trains. Long before this, "
                 "thousands of years ago, people travelled long distances on foot or used animals to travel from one "
                 "place to another. They also built boats and ships to travel across lakes, rivers, and seas. Boats "
                 "were probably the first form of transport invented by humans, much before bullock carts!"],
       teach=["Predict first: which way of travelling is older, a boat or a bullock cart?",
              "Thousands of years ago, people travelled long distances on foot or on animals. They built boats and "
              "ships to cross lakes, rivers and seas.",
              "Boats were probably the first form of transport humans invented, much before bullock carts.",
              "About a hundred years ago there were animal-drawn carts, cars and trains, but far fewer vehicles than "
              "today.",
              "Rule: the ways of travelling grew over time, and so did the number of vehicles."],
       examples=[WE("The opening story names ways of travelling. Long ago: on foot, on animals, in boats and in ships. "
                    "About a hundred years ago: animal-drawn carts, cars and trains. How many ways of travelling "
                    "does the story name in all, and which is older, a boat or a bullock cart?",
                    ["Long ago the story names 4 ways: on foot, on animals, in boats and in ships.",
                     "About a hundred years ago it names 3 vehicles: animal-drawn carts, cars and trains.",
                     "Add the two groups: 4 + 3 = 7.",
                     "The story says boats were probably the first transport humans invented, much before bullock "
                     "carts.",
                     "So a boat is older than a bullock cart.",
                     "Check: foot, animals, boats, ships, carts, cars, trains make 7 names."],
                    "7 ways of travelling are named, and a boat is older than a bullock cart")],
       key_terms=["transport", "vehicle", "boat"], misconceptions=[], minutes=5),
     DOER("T1B.C2", "Pull it together and do it: Travelling Then and Now", None, "Understand",
          "Students sort the ways of travelling into long ago and about a hundred years ago.",
          ["People first travelled on foot and on animals.",
           "Boats were probably the first transport humans invented, much before bullock carts.",
           "About a hundred years ago there were animal-drawn carts, cars and trains, and far fewer vehicles than "
           "today."])],
    topic_type="instructional", key_terms=["transport", "vehicle", "boat"]))

# ============================== T2 Understanding Large Numbers and Place Value =============================
TOPICS.append(TOPIC(
    "T2", "M1", "Understanding Large Numbers and Place Value", ["Reading and writing large numbers"], "Understand",
    "Students count in thousands to ten thousand, write 10,000 in the new TTh column with a comma, and state the place "
    "value of each digit of a five-digit number.",
    "Adding one thousand to 9,000 gives ten thousand, 10,000. The place value chart gets a new column, TTh, to the "
    "left of Th. Ten of one place make one of the next place, and a comma helps us read large numbers.",
    [A("T2.C1", "What comes after nine thousand?", "Understand",
       "Students count in thousands from 1,000 up to 9,000, add one more thousand, and write the result as ten "
       "thousand, 10,000.",
       textbook=["How do you write numbers to show several thousand objects?",
                 "Let us start with 1,000. What numbers do we get when we keep adding a thousand?",
                 "What number do we get when we add a thousand to 9,000? We get ten thousand. How do we write this "
                 "number?"],
       teach=["Predict first: you keep adding one thousand, 1,000, 2,000, 3,000 and so on. Which number comes after "
              "9,000?",
              "Each step adds one more thousand. After 9 thousands, one more thousand makes 10 thousands.",
              "9,000 + 1,000 = 10,000. We say ten thousand.",
              "Rule: 10 thousands make 1 ten thousand, and a number with 10 thousands needs a new place."],
       examples=[WE("Start at 4,150 and keep adding one thousand. Which number do you reach after 9,150, and how do "
                    "you say it?",
                    ["Add 1,000 each time: 4,150, 5,150, 6,150, 7,150, 8,150, 9,150.",
                     "The Th place of 9,150 holds 9. One more thousand makes 10 thousands.",
                     "9,150 + 1,000 = 10,150.",
                     "10 thousands make 1 ten thousand, so write 1 in the new TTh column: 10,150.",
                     "Say it: ten thousand one hundred fifty.",
                     "Check: 10,150 − 9,150 = 1,000."],
                    "10,150, which is ten thousand one hundred fifty")],
       ncert=["r.ten_thousand"], key_terms=["thousand", "ten thousand"], misconceptions=["M_TT_COLUMN"], minutes=6),
     A("T2.C2", "The new TTh column and the value of digits", "Understand",
       "Students extend the place value chart with a TTh column, write ten thousand as 10,000 with a comma, and state "
       "the value of each digit in a number such as 9,123.",
       textbook=["Look at the table below and notice the pattern of writing numbers. In the place value chart, we "
                 "have added another column, TTh. It stands for ten thousand.",
                 "10 Ones = 1 Ten = 10",
                 "10 Tens = 1 Hundred = 100",
                 "10 Hundreds = 1 Thousand = 1,000",
                 "In the same way, 10 Thousands = Ten Thousand = 10,000.",
                 "We use a comma to help us read large numbers easily.",
                 "Do you remember how we read and write numbers in the Indian place value system? We use the same ten "
                 "digits 0 to 9 in different places to write larger numbers.",
                 "For example, 1,380 = 1 Thousand + 3 Hundreds + 8 Tens + 0 Ones.",
                 "9,123 = 9 Thousands + 1 Hundred + 2 Tens + 3 Ones."],
       teach=["Predict first: the chart has columns O, T, H and Th. Where will the digit for ten thousand go?",
              "Ten of one place make one of the next place on its left: 10 ones make 1 ten, 10 tens make 1 hundred, "
              "10 hundreds make 1 thousand, and 10 thousands make 1 ten thousand.",
              "So the chart gets a new column, TTh, to the left of Th. Ten thousand is 1 in TTh and 0 in the four "
              "places to its right: 10,000.",
              "The same ten digits 0 to 9 work in every place. The value of a digit depends on its place: the 3 in "
              "1,380 is 3 hundreds, but the 3 in 9,123 is 3 ones.",
              "A comma helps us read a large number. It comes before the last three digits.",
              "Rule: ten of one place make one of the next place on the left."],
       examples=[WE("Put the digits of 52,525 in the place value chart and say what each digit is worth.",
                    ["Write the digits from the left: TTh 5, Th 2, H 5, T 2, O 5.",
                     "The 5 in TTh is 5 ten thousands: 5 × 10,000 = 50,000.",
                     "The 2 in Th is 2 thousands: 2 × 1,000 = 2,000.",
                     "The 5 in H is 5 hundreds: 5 × 100 = 500.",
                     "The 2 in T is 2 tens: 2 × 10 = 20.",
                     "The 5 in O is 5 ones: 5 × 1 = 5.",
                     "Check: 50,000 + 2,000 + 500 + 20 + 5 = 52,525."],
                    "The three 5s are worth 50,000, 500 and 5, and the number is 52,525")],
       ncert=["r.place_chart", "r.comma", "r.indian_system", "r.expanded_1380", "r.expanded_9123"],
       key_terms=["TTh", "place value", "comma", "digit"], misconceptions=["M_TT_COLUMN", "M_COMMA_PLACE"],
       minutes=8),
     DOER("T2.C3", "Pull it together and do it: Ten Thousand and Place Value", None, "Apply",
          "Students fill the boxes from 1,000 to 9,000, add one more thousand to write 10,000, and explain how 10 "
          "thousands make one ten thousand.",
          ["Ten of one place make one of the next place on the left.",
           "10 thousands make 1 ten thousand: 10,000. TTh is the new column.",
           "A digit's value depends on its place.",
           "A comma helps us read large numbers."],
          items=[FIO("r.thousands", "Reading and writing large numbers (thousands), the boxes",
                     "Let us start with 1,000. What numbers do we get when we keep adding a thousand? Fill the boxes: "
                     "1,000, 2,000, then six empty boxes, then 9,000. What number do we get when we add a thousand to "
                     "9,000? How do we write this number?",
                     ["The first box is 1,000 and each box adds 1,000 more.",
                      "Fill the empty boxes: 3,000, 4,000, 5,000, 6,000, 7,000 and 8,000.",
                      "Check the last box: 8,000 + 1,000 = 9,000.",
                      "Add one more thousand: 9,000 + 1,000 = 10,000.",
                      "10 thousands make 1 ten thousand, so we say ten thousand.",
                      "Write 1 in the new TTh column and 0 in Th, H, T and O, with the comma before the last three "
                      "digits: 10,000."],
                     "The boxes are 1,000 to 9,000, and 9,000 + 1,000 = 10,000, which is ten thousand",
                     kind="prompt",
                     q_figure="A row of nine boxes joined by arrows: the first box shows 1,000, the second shows "
                              "2,000, the last shows 9,000, and the six boxes between 2,000 and 9,000 are empty.",
                     s_figure="The same row with every box filled from 1,000 to 9,000 and an arrow to one token "
                              "marked 10,000.")],
          misconceptions=["M_TT_COLUMN", "M_COMMA_PLACE"])],
    key_terms=["ten thousand", "TTh", "place value", "comma"]))

# ============================== T3 Read the Numbers ========================================================
TOPICS.append(TOPIC(
    "T3", "M1", "Read the Numbers", ["Reading and writing large numbers"], "Apply",
    "Students read numbers beyond ten thousand by saying the thousands part first and then the hundreds, tens and "
    "ones, and read numbers with zeros by skipping the empty places.",
    "To read a five-digit number, say the part before the comma and add thousand, then say the hundreds, tens and "
    "ones. A zero holds a place but is never said in the number name.",
    [A("T3.C1", "Reading numbers beyond ten thousand", "Apply",
       "Students read a number beyond ten thousand from its tokens and its place value chart, saying the thousands "
       "part first and then the hundreds, tens and ones.",
       textbook=["Let us see how we write numbers beyond 10,000 and how we name them. We write them in the same way as "
                 "numbers below 9,999. You can use the tokens given in the end of the book.",
                 "Tokens 10,000 and 1: number 10,001, TTh 1, Th 0, H 0, T 0, O 1, number name Ten thousand one.",
                 "Tokens 10,000, 1 and 1: number 10,002, TTh 1, Th 0, H 0, T 0, O 2, number name Ten thousand two.",
                 "Tokens 10,000 and 10: number 10,010, TTh 1, Th 0, H 0, T 1, O 0, number name Ten thousand ten.",
                 "Tokens 10,000, two 10s and four 1s: number 10,024, TTh 1, Th 0, H 0, T 2, O 4, number name Ten "
                 "thousand twenty-four."],
       teach=["Predict first: a token table shows one 10,000 token and one 1 token. Which number is it, and how do we "
              "say it?",
              "10,000 + 1 = 10,001. We say ten thousand one. The zeros hold the Th, H and T places.",
              "In the same way, 10,000 + 20 + 4 = 10,024, and we say ten thousand twenty-four.",
              "Rule: say the part before the comma and add thousand, then say the hundreds, tens and ones."],
       examples=[WE("Read the number 34,682 aloud.",
                    ["Put the digits in the chart: TTh 3, Th 4, H 6, T 8, O 2.",
                     "The part before the comma is 34. Say it and add thousand: thirty-four thousand.",
                     "H 6 is six hundred.",
                     "T 8 and O 2 make 80 + 2 = 82, so say eighty-two.",
                     "Put the parts together: thirty-four thousand six hundred eighty-two.",
                     "Check: 34,000 + 600 + 82 = 34,682."],
                    "Thirty-four thousand six hundred eighty-two")],
       ncert=["r.tok_rows"], key_terms=["number name", "token", "comma", "thousand"],
       misconceptions=["M_TT_COLUMN", "M_COMMA_PLACE"], minutes=7),
     A("T3.C2", "Reading numbers with zeros", "Apply",
       "Students read numbers that have zeros in some places, such as 30,402, by saying only the places that hold a "
       "digit and skipping every place that holds a zero.",
       teach=["Predict first: how do you read 10,010? Do you say the zeros?",
              "10,010 has TTh 1, Th 0, H 0, T 1, O 0. The 1 in the Tens place is ten.",
              "The zeros hold their places, but we do not say them. So 10,010 is ten thousand ten, not ten thousand "
              "one ten.",
              "Rule: say only the places that have a digit, and skip every place that holds a zero."],
       examples=[WE("Read the number 30,402 aloud.",
                    ["Put the digits in the chart: TTh 3, Th 0, H 4, T 0, O 2.",
                     "The part before the comma is 30. Say it and add thousand: thirty thousand. The 0 in Th is not "
                     "said.",
                     "H 4 is four hundred.",
                     "T 0 means no tens, so say nothing for it. O 2 is two.",
                     "Put the parts together: thirty thousand four hundred two.",
                     "Check: 30,000 + 400 + 2 = 30,402."],
                    "Thirty thousand four hundred two")],
       key_terms=["zero", "number name", "place"], misconceptions=["M_ZERO_NAME"], minutes=6),
     DOER("T3.C3", "Practice: Read It", "number_reading", "Apply",
          "Students read the number name of five-digit numbers from tokens, charts and digits, and check each name by "
          "writing the number back from it.",
          ["Count the tokens of each kind to find the digit in each place.",
           "Say the part before the comma and add thousand. Then say the hundreds, tens and ones.",
           "A zero holds a place. Do not say it.",
           "Check by writing the number back from its name."],
          items=[FIO("r.tok_a", "Token table (large numbers), first two rows",
                     "Fill in the token table. Write the number and write its digits in the TTh, Th, H, T and O "
                     "columns. Row 1: the tokens are one 10,000, three 10s and three 1s, and the number name is Ten "
                     "thousand thirty-three. Row 2: the number is 10,458 and the number name is Ten thousand four "
                     "hundred fifty-eight; write its digits.",
                     ["Row 1: count the tokens: one 10,000, three 10s and three 1s.",
                      "Three 10s are 30 and three 1s are 3: 10,000 + 30 + 3 = 10,033.",
                      "The digits are TTh 1, Th 0, H 0, T 3, O 3, and the name ten thousand thirty-three matches.",
                      "Row 2: the number is 10,458, so the digits from the left are TTh 1, Th 0, H 4, T 5, O 8.",
                      "Check with the tokens: 10,000 + 400 + 50 + 8 = 10,458."],
                     "10,033 has digits 1, 0, 0, 3, 3 and 10,458 has digits 1, 0, 4, 5, 8",
                     kind="prompt",
                     q_figure="A token table with the columns Token(s), Number, TTh, Th, H, T, O and Number Name: "
                              "row 1 shows one 10,000 token, three 10 tokens and three 1 tokens with the name Ten "
                              "thousand thirty-three, and row 2 shows one 10,000 token, four 100 tokens, five 10 "
                              "tokens and eight 1 tokens with the number 10,458 and the name Ten thousand four "
                              "hundred fifty-eight; the number and digit cells that are not given are empty.",
                     s_figure="The same two rows with the number and every digit cell filled."),
                 FIO("r.tok_b", "Token table (large numbers), last four rows",
                     "Fill in the token table. (a) The tokens are one 10,000, one 1,000, two 100s, one 10 and four "
                     "1s, and the digits are TTh 1, Th 1, H 2, T 1, O 4: write the number and its number name. "
                     "(b) The number is 13,520, Thirteen thousand five hundred twenty: write its digits. (c) The "
                     "number is 20,000, Twenty thousand: write its digits. (d) The number is 45,867, Forty-five "
                     "thousand eight hundred sixty-seven: write its digits.",
                     ["(a) The tokens make 10,000 + 1,000 + 200 + 10 + 4 = 11,214.",
                      "(a) The part before the comma is 11: eleven thousand two hundred fourteen.",
                      "(b) 13,520 has TTh 1, Th 3, H 5, T 2, O 0. The 0 holds the Ones place.",
                      "(c) Two 10,000 tokens make 2 × 10,000 = 20,000, so TTh 2 and 0 in Th, H, T and O.",
                      "(d) 45,867 has TTh 4, Th 5, H 8, T 6, O 7.",
                      "Check (d): 40,000 + 5,000 + 800 + 60 + 7 = 45,867."],
                     "(a) 11,214, Eleven thousand two hundred fourteen. (b) 1, 3, 5, 2, 0. (c) 2, 0, 0, 0, 0. "
                     "(d) 4, 5, 8, 6, 7",
                     kind="prompt",
                     q_figure="A token table with the columns Token(s), Number, TTh, Th, H, T, O and Number Name: "
                              "row 1 shows one 10,000, one 1,000, two 100, one 10 and four 1 tokens with the digits "
                              "1, 1, 2, 1, 4; row 2 shows one 10,000, three 1,000, five 100 and two 10 tokens with "
                              "13,520 and its name; row 3 shows two 10,000 tokens with 20,000 and Twenty thousand; "
                              "row 4 shows four 10,000, five 1,000, eight 100, six 10 and seven 1 tokens with "
                              "45,867 and its name; the cells that are not given are empty.",
                     s_figure="The same four rows with every number, digit and number name filled."),
                 FIO("LUDa.Q2read", "Let Us Do (large numbers), Q2 read",
                     "Fill in the blanks appropriately. Use commas as required. Write the number name of each of "
                     "these numbers: 7,209; 10,599; 13,579; 45,045; 39,593; 50,005; 26,050; 81,200.",
                     ["Say the part before the comma and add thousand. Then say the hundreds, tens and ones. Skip "
                      "every place that holds 0.",
                      "7,209: seven thousand, 2 hundreds, 0 tens, 9 ones: Seven thousand two hundred nine.",
                      "10,599: Ten thousand five hundred ninety-nine.",
                      "13,579: Thirteen thousand five hundred seventy-nine.",
                      "45,045: the Hundreds place is 0, so we skip it: Forty-five thousand forty-five.",
                      "39,593: Thirty-nine thousand five hundred ninety-three.",
                      "50,005: the Th, H and T places are 0, so only the ones are said: Fifty thousand five.",
                      "26,050: the Hundreds and Ones places are 0: Twenty-six thousand fifty.",
                      "81,200: the Tens and Ones places are 0: Eighty-one thousand two hundred.",
                      "Check one: 26,000 + 50 = 26,050, which is twenty-six thousand fifty."],
                     "Seven thousand two hundred nine; Ten thousand five hundred ninety-nine; Thirteen thousand five "
                     "hundred seventy-nine; Forty-five thousand forty-five; Thirty-nine thousand five hundred "
                     "ninety-three; Fifty thousand five; Twenty-six thousand fifty; Eighty-one thousand two hundred",
                     q_figure="A two-column table, Number and Number Name, with eight rows that show a number and an "
                              "empty name: 7,209, 10,599, 13,579, 45,045, 39,593, 50,005, 26,050 and 81,200.")],
          misconceptions=["M_ZERO_NAME", "M_COMMA_PLACE"])],
    key_terms=["number name", "token", "zero", "thousand"]))

# ============================== T4 Write the Numbers =======================================================
TOPICS.append(TOPIC(
    "T4", "M1", "Write the Numbers", ["Reading and writing large numbers"], "Apply",
    "Students write numbers beyond ten thousand from their names, placing each digit in its own place and using a "
    "zero in every place the name skips.",
    "To write a number from its name, find the word thousand. The part before it goes in TTh and Th, and the rest goes "
    "in H, T and O. Every place the name skips needs a zero.",
    [A("T4.C1", "Writing a number from its name", "Apply",
       "Students write a number beyond ten thousand from its number name by placing the digits in the TTh, Th, H, T and "
       "O places and putting the comma before the last three digits.",
       teach=["Predict first: a ticket says Seventy-two thousand four hundred fifteen. How many digits will its "
              "number have, and which digit goes in the TTh place?",
              "Find the word thousand. The part before it, seventy-two, gives the TTh and Th digits: 7 and 2.",
              "The part after it, four hundred fifteen, gives H 4, T 1 and O 5. The number is 72,415.",
              "Rule: write the digits you hear from the left, and put the comma before the last three digits."],
       examples=[WE("Write in numbers: Sixty-eight thousand five hundred nineteen.",
                    ["Find the word thousand. The part before it is sixty-eight, so TTh 6 and Th 8.",
                     "After it: five hundred nineteen. H is 5, and nineteen is 10 + 9, so T 1 and O 9.",
                     "Put the digits in the chart: TTh 6, Th 8, H 5, T 1, O 9.",
                     "Write them together with the comma before the last three digits: 68,519.",
                     "Check: 68,000 + 500 + 19 = 68,519."],
                    "68,519")],
       key_terms=["number name", "digit", "comma", "chart"], misconceptions=["M_COMMA_PLACE", "M_TT_COLUMN"],
       minutes=6),
     A("T4.C2", "Zero holds a place when we write", "Apply",
       "Students write numbers whose names skip a place, such as forty thousand eight, by putting a zero in every "
       "empty place of the chart.",
       teach=["Predict first: the name is forty thousand eight. How many digits does the number have, and is it "
              "4,008?",
              "Forty thousand is 4 in TTh and 0 in Th. There are no hundreds and no tens. Eight is in the Ones place.",
              "Each skipped place needs a 0 so that the digits stay where they belong: the number is 40,008, with 5 "
              "digits.",
              "Rule: after you place the digits you hear, put 0 in every empty place so that all five places are "
              "filled."],
       examples=[WE("Write in numbers: Sixty thousand two hundred nine.",
                    ["Find the word thousand. The part before it is sixty, so TTh 6 and Th 0.",
                     "After it: two hundred nine. H is 2. There are no tens, so T is 0. O is 9.",
                     "Fill every place: TTh 6, Th 0, H 2, T 0, O 9.",
                     "Write the digits together with the comma: 60,209.",
                     "Check: 60,000 + 200 + 9 = 60,209, and the name read back is sixty thousand two hundred nine."],
                    "60,209")],
       key_terms=["zero", "place", "digit"], misconceptions=["M_ZERO_NAME"], minutes=6),
     DOER("T4.C3", "Practice: Write It", "number_construction", "Apply",
          "Students write numbers from their number names, fill each empty place with a zero, and check each answer by "
          "reading the number back.",
          ["Find the word thousand. The part before it goes in TTh and Th.",
           "Then write the hundreds, tens and ones you hear.",
           "Put 0 in every place the name skips.",
           "Read the number back to check it."],
          items=[FIO("LUDa.Q2write", "Let Us Do (large numbers), Q2 write",
                     "Fill in the blanks appropriately. Use commas as required. Write the number for each of these "
                     "names: Ten thousand seven hundred forty-three; Ten thousand ten; Fifty-six thousand four "
                     "hundred ninety-one; Ninety thousand nine; Twenty-three thousand two hundred thirty; "
                     "Thirty-six thousand one.",
                     ["Find the word thousand in each name. The part before it gives the TTh and Th digits. Put 0 in "
                      "every place the name skips.",
                      "Ten thousand seven hundred forty-three: TTh 1, Th 0, H 7, T 4, O 3, so 10,743.",
                      "Ten thousand ten: TTh 1, Th 0, H 0, T 1, O 0, so 10,010.",
                      "Fifty-six thousand four hundred ninety-one: TTh 5, Th 6, H 4, T 9, O 1, so 56,491.",
                      "Ninety thousand nine: TTh 9, Th 0, H 0, T 0, O 9, so 90,009.",
                      "Twenty-three thousand two hundred thirty: TTh 2, Th 3, H 2, T 3, O 0, so 23,230.",
                      "Thirty-six thousand one: TTh 3, Th 6, H 0, T 0, O 1, so 36,001.",
                      "Check one: 90,000 + 9 = 90,009, which is ninety thousand nine."],
                     "10,743; 10,010; 56,491; 90,009; 23,230; 36,001",
                     q_figure="A two-column table, Number and Number Name, with six rows that show an empty number "
                              "and a name: Ten thousand seven hundred forty-three, Ten thousand ten, Fifty-six "
                              "thousand four hundred ninety-one, Ninety thousand nine, Twenty-three thousand two "
                              "hundred thirty and Thirty-six thousand one.")],
          misconceptions=["M_ZERO_NAME", "M_COMMA_PLACE"])],
    key_terms=["number name", "zero", "digit", "TTh"]))

# ============================== T5 Number Patterns =========================================================
TOPICS.append(TOPIC(
    "T5", "M1", "Number Patterns", ["Let Us Do"], "Analyze",
    "Students find the rule of a number pattern by comparing neighbouring numbers, continue patterns that go up, go "
    "down or pass ten thousand, and check the rule on every pair.",
    "In a number pattern, each number changes by the same amount from the one before. Subtract neighbouring numbers to "
    "find that amount, then add it or subtract it to continue the pattern.",
    [A("T5.C1", "Finding the rule of a pattern", "Analyze",
       "Students find the rule of a number pattern by subtracting neighbouring numbers, test it on every pair, and "
       "write the next numbers.",
       teach=["Predict first: 120, 135, 150. What is added each time, and what comes next?",
              "Find the jump between neighbours: 135 − 120 = 15 and 150 − 135 = 15. The jump is the same, so the rule "
              "is add 15.",
              "The next number is 150 + 15 = 165. Test the rule on every pair, not only the first two. If one jump "
              "is different, the rule is wrong.",
              "Rule: a pattern adds or subtracts the same number each time. Find that number and use it."],
       examples=[WE("Find the rule and write the next two numbers: 2,150, 2,450, 2,750, 3,050.",
                    ["Subtract each number from the one after it: 2,450 − 2,150 = 300.",
                     "2,750 − 2,450 = 300.",
                     "3,050 − 2,750 = 300.",
                     "The jump is the same every time, so the rule is add 300.",
                     "The next number is 3,050 + 300 = 3,350.",
                     "Then 3,350 + 300 = 3,650.",
                     "Check: 2,150 to 3,650 is 5 jumps, and 5 × 300 = 1,500, so 2,150 + 1,500 = 3,650."],
                    "The rule is add 300, and the next numbers are 3,350 and 3,650")],
       key_terms=["pattern", "rule", "sequence"], misconceptions=["M_PATTERN_RULE"], minutes=6),
     A("T5.C2", "Patterns that go down or cross ten thousand", "Analyze",
       "Students continue a pattern that goes down by subtracting the same number, and a pattern that passes ten "
       "thousand, and name the rule in words.",
       teach=["Predict first: 9,700, 9,800, 9,900. What is the next number, and how many digits does it have?",
              "The rule is add 100. 9,900 + 100 = 10,000, and the number now has five digits.",
              "In a pattern that goes down the numbers get smaller, so the rule subtracts. The pattern 8,400, 8,100, "
              "7,800 subtracts 300 each time, and the next number is 7,800 − 300 = 7,500.",
              "Rule: if the numbers grow, add the jump. If they fall, subtract it. Check every pair."],
       examples=[WE("Find the rule and write the next two numbers: 13,050, 12,050, 11,050, 10,050.",
                    ["The numbers get smaller, so the rule subtracts.",
                     "13,050 − 12,050 = 1,000.",
                     "12,050 − 11,050 = 1,000.",
                     "11,050 − 10,050 = 1,000.",
                     "The jump is the same every time, so the rule is subtract 1,000.",
                     "10,050 − 1,000 = 9,050. The number now has four digits.",
                     "9,050 − 1,000 = 8,050.",
                     "Check: 13,050 − 5,000 = 8,050, and 5 jumps of 1,000 were taken."],
                    "The rule is subtract 1,000, and the next numbers are 9,050 and 8,050")],
       key_terms=["pattern", "rule", "subtract", "ten thousand"], misconceptions=["M_PATTERN_RULE"], minutes=6),
     DOER("T5.C3", "Pull it together and do it: Number Patterns", None, "Analyze",
          "Students find the rule of each number pattern, say whether it adds or subtracts, and fill every blank, "
          "checking the last number with the rule.",
          ["Subtract neighbouring numbers to find the jump.",
           "If the jump is the same every time, that is the rule.",
           "Growing numbers mean add. Falling numbers mean subtract.",
           "Check the last number with the rule."],
          items=[FIO("LUDa.Q1abc", "Let Us Do (patterns), Q1 (a) to (c)",
                     "Fill in the blanks by continuing the pattern in each of the following sequences. Discuss the "
                     "patterns in class. (a) 456, 567, 678, then four empty boxes. (b) 1,050, an empty box, 3,150, "
                     "4,200, then three empty boxes. (c) 5,501, 6,401, 7,301, then four empty boxes.",
                     ["(a) The jump is 567 − 456 = 111. Check the next pair: 678 − 567 = 111. The rule is add 111.",
                      "(a) Add 111 each time: 678 + 111 = 789, then 900, 1,011 and 1,122.",
                      "(b) The jump is 4,200 − 3,150 = 1,050. The empty box is 3,150 − 1,050 = 2,100.",
                      "(b) Add 1,050 each time after 4,200: 4,200 + 1,050 = 5,250, then 6,300 and 7,350.",
                      "(c) The jump is 6,401 − 5,501 = 900. Check: 7,301 − 6,401 = 900. The rule is add 900.",
                      "(c) Add 900 each time: 7,301 + 900 = 8,201, then 9,101, 10,001 and 10,901.",
                      "Check (c): 10,901 − 7,301 = 3,600 = 4 × 900."],
                     "(a) 789, 900, 1,011, 1,122. (b) 2,100, 5,250, 6,300, 7,350. (c) 8,201, 9,101, 10,001, 10,901",
                     q_figure="Three chains of boxes joined by arrows: (a) 456, 567, 678 and four empty boxes; (b) "
                              "1,050, an empty box, 3,150, 4,200 and three empty boxes; (c) 5,501, 6,401, 7,301 and "
                              "four empty boxes.",
                     s_figure="The same three chains with every box filled and a curved arrow over each step marked "
                              "with its jump."),
                 FIO("LUDa.Q1defg", "Let Us Do (patterns), Q1 (d) to (g)",
                     "Fill in the blanks by continuing the pattern in each of the following sequences. Discuss the "
                     "patterns in class. (d) 10,100, 10,200, 10,300, five empty boxes, 10,900 and one more empty box. "
                     "(e) 10,105, 10,125, then eight empty boxes. (f) 10,992, 10,993, then eight empty boxes. (g) "
                     "10,794, 10,796, 10,798, then seven empty boxes.",
                     ["(d) 10,200 − 10,100 = 100, so the rule is add 100: 10,400, 10,500, 10,600, 10,700 and 10,800.",
                      "(d) Check the printed box: 10,800 + 100 = 10,900. The last box is 10,900 + 100 = 11,000.",
                      "(e) The jump is 10,125 − 10,105 = 20. Add 20 each time: 10,145, 10,165, 10,185, 10,205, "
                      "10,225, 10,245, 10,265 and 10,285.",
                      "(f) The jump is 10,993 − 10,992 = 1. Add 1 each time: 10,994, 10,995, 10,996, 10,997, "
                      "10,998, 10,999, 11,000 and 11,001.",
                      "(f) 10,999 + 1 = 11,000: the Th digit becomes 1 and the H, T and O digits turn to 0.",
                      "(g) The jump is 10,796 − 10,794 = 2. Add 2 each time: 10,800, 10,802, 10,804, 10,806, "
                      "10,808, 10,810 and 10,812.",
                      "Check (e): 10,285 − 10,105 = 180 = 9 × 20."],
                     "(d) add 100, the last box is 11,000. (e) add 20, the last box is 10,285. (f) add 1, the last "
                     "box is 11,001. (g) add 2, the last box is 10,812",
                     q_figure="Four chains of 10 boxes joined by arrows, 7 boxes in the first row and 3 in the "
                              "second row: (d) starts 10,100, 10,200, 10,300 and has 10,900 in the ninth box; (e) "
                              "starts 10,105, 10,125; (f) starts 10,992, 10,993; (g) starts 10,794, 10,796, "
                              "10,798; all the other boxes are empty."),
                 FIO("LUDa.Q1hi", "Let Us Do (patterns), Q1 (h) and (i)",
                     "Fill in the blanks by continuing the pattern in each of the following sequences. Discuss the "
                     "patterns in class. (h) 73,005, 72,004, then eight empty boxes. (i) 82,350, 83,350, then eight "
                     "empty boxes.",
                     ["(h) The numbers fall, so the rule subtracts: 73,005 − 72,004 = 1,001.",
                      "(h) Subtract 1,001 each time: 72,004 − 1,001 = 71,003, then 70,002, 69,001, 68,000, 66,999, "
                      "65,998, 64,997 and 63,996.",
                      "(h) Check the step across 68,000: 68,000 − 1,001 = 66,999.",
                      "(i) The numbers grow, so the rule adds: 83,350 − 82,350 = 1,000.",
                      "(i) Add 1,000 each time: 83,350 + 1,000 = 84,350, then 85,350, 86,350, 87,350, 88,350, "
                      "89,350, 90,350 and 91,350.",
                      "(i) Check: 91,350 − 82,350 = 9,000 = 9 × 1,000."],
                     "(h) subtract 1,001, the last box is 63,996. (i) add 1,000, the last box is 91,350",
                     q_figure="Two chains of 10 boxes joined by arrows, 7 boxes in the first row and 3 in the second "
                              "row: (h) starts 73,005, 72,004 and (i) starts 82,350, 83,350; all the other boxes are "
                              "empty.")],
          misconceptions=["M_PATTERN_RULE"])],
    key_terms=["pattern", "rule", "sequence"]))
