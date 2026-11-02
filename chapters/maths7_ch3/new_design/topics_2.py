# -*- coding: utf-8 -*-
"""Topics T6 to T10 (module M2 decimal place value and units; start of module M3). Book sections 3.4 to 3.6."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T6 Extending the place value system ==========================================
TOPICS.append(TOPIC(
    "T6", "M2", "Extending the Place Value System", ["3.4"], "Understand",
    "Students explain why a unit is split into 10 equal parts, extend the place value ladder to tenths, "
    "hundredths and thousandths, and answer how many of one place make one of another.",
    "Each place is 10 times the place on its right, so the ladder of places continues to the right with tenths, "
    "hundredths and thousandths, which is why the system is called decimal.",
    [A("T6.C1", "Why split a unit into ten parts", "Understand",
       "Students compare splitting a unit into 4 equal parts with splitting it into 10, and explain why 10 is used "
       "every time in the Indian place value system.",
       textbook=["3.4 Decimal Place Value",
                 "You may have noticed that whenever we need to measure something more accurately, we split a part "
                 "into 10 (smaller) equal parts ― we split a unit into 10 one-tenths and then split each one-tenth "
                 "into 10, one-hundredths and then we use these smaller parts to measure.",
                 "Can we not split a unit into 4 equal parts, 5 equal parts, 8 equal parts, or any other number of "
                 "equal parts instead?",
                 "Yes, we can. The example below compares how the same length is represented when the unit is split "
                 "into 10 equal parts and when the unit is split into 4 equal parts.",
                 "If an even more precise measure is needed, each quarter can further be split into four equal parts. "
                 "Each part then measures 1/16 of a unit, i.e., 16 such parts make 1 unit.",
                 "Then why split a unit into 10 parts every time?",
                 "The reason is the special role that 10 plays in the Indian place value system. For a whole number "
                 "written in the Indian place value system ― for example, 281 ― the place value of 2 is hundreds "
                 "(100), that of 8 is tens (10), and that of 1 is one (1). Each place value is 10 times bigger than "
                 "the one immediately to its right. Equivalently, each place value is 10 times smaller than the one "
                 "immediately to its left: 10 ones make 1 ten, 10 tens make 1 hundred, 10 hundreds make 1 thousand, "
                 "and so on."],
       teach=["Predict first: if a unit can be split into 4 or 5 or 8 equal parts, why do we keep choosing 10?",
              "Splitting into 4 and then splitting each quarter into 4 again gives 16 parts in a unit. Splitting "
              "into 10 and then each tenth into 10 gives 100 parts.",
              "In 281 each place is worth 10 times the place on its right. Splitting a unit into 10 continues the "
              "same pattern."],
       examples=[
           WE("A unit is split into 4 equal parts, and each part is split into 4 equal parts again. How many tiny "
              "parts make a unit, and how is that different from splitting by 10 twice?",
              ["First split: 4 equal parts, each 1/4 of a unit.",
               "Second split: each quarter into 4 parts, so 4 × 4 = 16 parts in a unit, each 1/16 of a unit.",
               "Splitting by 10 twice gives 10 × 10 = 100 parts, each 1/100 of a unit.",
               "In the number 281 each place is 10 times the place on its right: 10 ones make 1 ten, 10 tens make 1 "
               "hundred. Splitting a unit into 10 keeps that same rule going to the right of the ones."],
              "16 parts of 1/16 each, against 100 parts of 1/100 each; 10 matches the 10 times rule of the places",
              ncert=["3.4.why_ten"])],
       key_terms=["place value"], misconceptions=["M_PART_AS_UNIT"], minutes=8),
     A("T6.C2", "Tenths, hundredths, thousandths and the decimal system", "Understand",
       "Students extend the ladder of places to one-thousandth by splitting a hundredth into 10 equal parts, and "
       "say why the system is called decimal.",
       textbook=["In order to extend this system of writing numbers to quantities smaller than one, we divide one "
                 "into 10 equal parts. What does this give? It gives one-tenth. Further dividing it into 10 parts "
                 "gives one-hundredth, and so on.",
                 "Can we extend this further? What will the fraction be when 1/100 is split into 10 equal parts?",
                 "It will be 1/1000, i.e., a thousand such parts make up a unit.",
                 "Just as when we extend to the left of 10,000, we get bigger place values at each step, we can also "
                 "extend to the right of 1/1000, getting smaller place values at each step.",
                 "This way of writing numbers is called the “decimal system” since it is based on the number 10; "
                 "“decem” means ten in Latin, which in turn is cognate to the Sanskrit daśha meaning 10, with "
                 "similar words for 10 occurring across many Indian languages including Odia, Konkani, Marathi, "
                 "Gujarati, Hindi, Kashmiri, Bodo, and Assamese. We shall learn about other ways of writing numbers "
                 "in later grades."],
       teach=["Predict first: split one hundredth into 10 equal parts. What fraction of a unit is each part?",
              "100 × 10 = 1000, so each part is 1/1000 of a unit, called a thousandth.",
              "The ladder now runs 1000, 100, 10, 1, then 1/10, 1/100, 1/1000 and on. Each step right divides by "
              "10 and each step left multiplies by 10.",
              "A system built on ten is called decimal, from the word for ten."],
       examples=[
           WE("Split one hundredth into 10 equal parts. What is one part called, and how many make a unit? Then "
              "write the ladder of place values from 1000 down to a thousandth.",
              ["One unit has 100 hundredths, and each hundredth is split into 10 parts.",
               "So a unit has 100 × 10 = 1000 parts, and each part is 1/1000 of a unit, one thousandth.",
               "The ladder is 1000, 100, 10, 1, 1/10, 1/100, 1/1000.",
               "Going one step to the right divides by 10; going one step to the left multiplies by 10."],
              "1/1000 of a unit, one thousandth; 1000 of them make a unit", ncert=["3.4.thousandth"])],
       key_terms=["thousandth", "decimal system"], misconceptions=["M_PART_AS_UNIT"], minutes=8),
     A("T6.C3", "How big? Counting parts of different places", "Apply",
       "Students answer how many of a smaller place make one of a bigger place, using the factor of 10 for each "
       "step between the places, and make questions of their own.",
       textbook=["How Big?",
                 "We already know that a hundred 10s make 1000, and a hundred 100s make 10000.",
                 "We can ask similar questions about fractional parts: (a) How many thousandths make one unit? (b) "
                 "How many thousandths make one tenth? (c) How many thousandths make one hundredth? (d) How many "
                 "tenths make one ten? (e) How many hundredths make one ten?",
                 "Make a few more questions of this kind and answer them."],
       teach=["Predict first: how many thousandths make one hundredth?",
              "Count the steps between the two places on the ladder. Each step is a factor of 10.",
              "Then make a few questions of your own, such as how many hundredths make one tenth."],
       examples=[
           WE("(a) How many thousandths make one unit? (b) How many make one tenth? (c) How many make one "
              "hundredth? (d) How many tenths make one ten? (e) How many hundredths make one ten?",
              ["(a) From a unit to a thousandth is 3 steps of 10, so 10 × 10 × 10 = 1000 thousandths.",
               "(b) From a tenth to a thousandth is 2 steps, so 100 thousandths.",
               "(c) From a hundredth to a thousandth is 1 step, so 10 thousandths.",
               "(d) A ten is 10 units and each unit is 10 tenths, so 100 tenths.",
               "(e) A ten is 100 tenths and each tenth is 10 hundredths, so 1000 hundredths.",
               "Own question: how many hundredths make one tenth? One step, so 10."],
              "(a) 1000 (b) 100 (c) 10 (d) 100 (e) 1000", ncert=["3.4.howbig"])],
       key_terms=["one-thousandth"], misconceptions=["M_UNIT_SHIFT"], minutes=8),
     DOER("T6.C4", "Practice: how many of one place make one of another", None, "Apply",
          "Students use the factor of 10 between neighbouring places to say how many of a smaller place make one "
          "of a bigger place.",
          ["Each step right on the ladder divides by 10, and each step left multiplies by 10.",
           "Count the steps between two places, and multiply 10 for each step.",
           "Ten hundredths make a tenth, and a thousand thousandths make a unit."],
          items=[
              FIO("end.FiO13", "Figure it Out (end of chapter), Q13",
                  "Which is greater? (a) 10/1000 or 1/10 (b) one-hundredth or 90 thousandths (c) one-thousandth or "
                  "90 hundredths",
                  ["(a) 10/1000 is 10 thousandths. A tenth is 100 thousandths. 100 is more than 10, so 1/10 is "
                   "greater.",
                   "(b) One hundredth is 10 thousandths. 90 thousandths is more than 10 thousandths, so 90 "
                   "thousandths is greater.",
                   "(c) 90 hundredths is 900 thousandths, far more than 1 thousandth, so 90 hundredths is greater."],
                  "(a) 1/10 is greater (b) 90 thousandths is greater (c) 90 hundredths is greater")])]))

# ============================== T7 Decimal notation ==========================================================
TOPICS.append(TOPIC(
    "T7", "M2", "Decimal Notation: Writing and Reading", ["3.4"], "Apply",
    "Students write quantities of units, tenths, hundredths and thousandths in decimal notation with a decimal "
    "point, read decimals digit by digit, and write counts of tenths or hundredths as decimals.",
    "The decimal point sits between the units and the tenths, so every digit keeps its place value; zeroes hold "
    "empty places, and a count of tenths or hundredths is written by moving the point.",
    [A("T7.C1", "Why we need a point", "Understand",
       "Students show that 705 can mean three different quantities if the places are not marked, and explain how a "
       "decimal point separates the whole part from the fractional part.",
       textbook=["Notation, Writing and Reading of Numbers",
                 "We have been writing numbers in a particular way, say 456, instead of writing them as 4 × 100 (4 "
                 "hundreds) + 5 × 10 (5 tens) + 6 × 1 (6 ones). Similarly, can we skip writing tenths and "
                 "hundredths?",
                 "Can the quantity 4 2/10 be written as 42 (skipping the 1/10 in 2 × 1/10)? If yes, how would we know "
                 "if 42 means 4 tens and 2 units or it means 4 units and 2 tenths?",
                 "Similarly, 705 could mean: (a) 7 hundreds, and 0 tens and 5 ones (700 + 0 + 5) (b) 7 tens and 0 "
                 "units and 5 tenths (70 + 0 + 5/10) (c) 7 units and 0 tenths and 5 hundredths (7 + 0/10 + 5/100)",
                 "Since these are different quantities, we need to have distinct ways of writing them.",
                 "To identify the place value where integers end and the fractional parts start, we use a point or "
                 "period (‘.’) as a separator, called a decimal point.",
                 "The above quantities in decimal notation are then: 7 hundreds and 5 ones is 705; 7 tens and 5 "
                 "tenths is 70.5; 7 units and 5 hundredths is 7.05.",
                 "Thus decimal notation is a natural extension of the Indian place value system to numbers also "
                 "having fractional parts. Just as 705 means 7 × 100 + 5 × 1, the number 70.5 means 7 × 10 + 5 × "
                 "1/10, and 7.05 means 7 × 1 + 5 × 1/100."],
       teach=["Predict first: if we drop the fraction parts and write 4 2/10 as 42, how would a reader know it is "
              "not 4 tens and 2 units?",
              "The digits 7, 0 and 5 can sit in different places and mean three different quantities.",
              "A point marks where the whole units end and the fractional parts begin. The digit just before the "
              "point is the units digit."],
       examples=[
           WE("The digits 7, 0 and 5 can mean 7 hundreds and 5 ones, or 7 tens and 5 tenths, or 7 units and 5 "
              "hundredths. Write each quantity in decimal notation and show the place of each digit.",
              ["7 hundreds, 0 tens, 5 ones is 700 + 0 + 5 = 705: no point is needed.",
               "7 tens, 0 units, 5 tenths is 70 + 0 + 5/10, written 70.5: the 7 is tens, the 0 is units, the 5 is "
               "tenths.",
               "7 units, 0 tenths, 5 hundredths is 7 + 0/10 + 5/100, written 7.05: the 7 is units, the 0 is tenths, "
               "the 5 is hundredths.",
               "So 705, 70.5 and 7.05 are three different quantities, and the point shows which is which."],
              "705, 70.5 and 7.05", ncert=["3.4.notation", "3.4.mathtalk"])],
       key_terms=["decimal point"], misconceptions=["M_READ_PLACE"], minutes=8),
     A("T7.C2", "Reading decimals and the place table", "Apply",
       "Students read a decimal digit by digit after the point, and write quantities given in places in decimal "
       "form with a place value table.",
       textbook=["We have seen how to write numbers using the decimal point (‘.’). But how do we read/say these "
                 "numbers?",
                 "We know that 705 is read as seven hundred and five. 70.5 is read as seventy point five, short for "
                 "seventy and five-tenths. 7.05 is read as seven point zero five, short for seven and five "
                 "hundredths.",
                 "0.274 is read as zero point two seven four. We don’t read it as zero point two hundred and seventy "
                 "four as 0.274 means 2 one-tenths and 7 one-hundredths and 4 one-thousandths.",
                 "Make a place value table similar to the one above. Write each quantity in decimal form and in "
                 "terms of place value, and read the number: (a) 2 ones, 3 tenths and 5 hundredths (b) 1 ten and 5 "
                 "tenths (c) 4 ones and 6 hundredths (d) 1 hundred, 1 one and 1 hundredth (e) 8/100 and 9/10 (f) "
                 "5/100 (g) 1/10 (h) 2 1/100, 4 1/10 and 7 7/1000"],
       teach=["Predict first: how would you say 0.274, as 'zero point two hundred and seventy four' or digit by "
              "digit?",
              "Digit by digit after the point: zero point two seven four, because 0.274 is 2 tenths, 7 hundredths "
              "and 4 thousandths.",
              "To write a quantity in decimal form, fill a place table, put a zero in every empty place between the "
              "digits, and put the point after the units."],
       examples=[
           WE("Write each quantity in decimal form, with its place values, and read it: (a) 2 ones, 3 tenths and 5 "
              "hundredths (b) 1 ten and 5 tenths (c) 4 ones and 6 hundredths (d) 1 hundred, 1 one and 1 hundredth.",
              ["(a) 2 + 3/10 + 5/100 is 2.35, read 'two point three five'.",
               "(b) 10 + 5/10 is 10.5, read 'ten point five'.",
               "(c) 4 + 0/10 + 6/100 is 4.06, with a zero in the empty tenths place, read 'four point zero six'.",
               "(d) 100 + 0 + 1 + 0/10 + 1/100 is 101.01, read 'one hundred one point zero one'."],
              "(a) 2.35 (b) 10.5 (c) 4.06 (d) 101.01", ncert=["3.4.readtable_a"]),
           WE("Write in decimal form and read aloud: (e) 8/100 and 9/10 (f) 5/100 (g) 1/10 (h) 2 1/100, 4 1/10 "
              "and 7 7/1000. Then read 13.117.",
              ["(e) 9/10 + 8/100 is 0.98, read 'zero point nine eight'.",
               "(f) 5/100 is 0.05, read 'zero point zero five'.",
               "(g) 1/10 is 0.1, read 'zero point one'.",
               "(h) 2 1/100 is 2.01, 4 1/10 is 4.1, and 7 7/1000 is 7.007, read 'two point zero one', 'four point "
               "one' and 'seven point zero zero seven'.",
               "13.117 is read 'thirteen point one one seven'."],
              "(e) 0.98 (f) 0.05 (g) 0.1 (h) 2.01, 4.1 and 7.007; 13.117 is thirteen point one one seven",
              ncert=["3.4.readtable_e"])],
       key_terms=["place value table"], misconceptions=["M_READ_PLACE"], minutes=8),
     A("T7.C3", "Counts of tenths and hundredths as decimals", "Apply",
       "Students write a count of hundreds, tens, tenths or hundredths as a decimal by splitting it into places or "
       "by moving the point.",
       textbook=["In the chapter on large numbers, we learned how to write 23 hundreds.",
                 "23 hundreds = 23 × 100 = 2000 + 300 = 2300.",
                 "Similarly, 23 tens would be: 23 tens = 23 × 10 = 200 + 30 = 230.",
                 "How can we write 234 tenths in decimal form? 234 tenths = 234/10 = 200/10 + 30/10 + 4/10 = 20 + 3 "
                 "+ 4/10 = 23.4.",
                 "Write these quantities in decimal form: (a) 234 hundredths, (b) 105 tenths."],
       teach=["Predict first: 234 tenths. Is it bigger or smaller than 234, and by how much?",
              "Each tenth is one tenth of a unit, so 234 tenths is 234 divided by 10. The digits stay and the point "
              "moves one place left.",
              "234 hundredths is 234 divided by 100, so the point moves two places left."],
       examples=[
           WE("Write 234 tenths in decimal form. Then write (a) 234 hundredths and (b) 105 tenths.",
              ["234 tenths = 234/10 = 200/10 + 30/10 + 4/10 = 20 + 3 + 4/10 = 23.4.",
               "(a) 234 hundredths = 234/100 = 200/100 + 30/100 + 4/100 = 2 + 3/10 + 4/100 = 2.34.",
               "(b) 105 tenths = 105/10 = 100/10 + 5/10 = 10 + 5/10 = 10.5."],
              "234 tenths is 23.4; (a) 2.34 (b) 10.5", ncert=["3.4.tenths", "3.4.hundredths"])],
       key_terms=["tenths"], misconceptions=["M_UNIT_SHIFT"], minutes=8),
     DOER("T7.C4", "Practice: write and read decimals", "place_chart_decimal_writer", "Apply",
          "Students write fractions and quantities as decimals, split decimals into tenths, hundredths and "
          "thousandths, and read them aloud.",
          ["The point goes right after the units place.",
           "A zero fills every empty place between the digits and the point.",
           "Read the digits after the point one by one."],
          items=[
              FIO("end.FiO1", "Figure it Out (end of chapter), Q1",
                  "Convert the following fractions into decimals: (a) 5/100 (b) 16/1000 (c) 12/10 (d) 254/1000",
                  ["(a) 5/100 is 5 hundredths, so the 5 sits in the hundredths place: 0.05.",
                   "(b) 16/1000 is 1 hundredth and 6 thousandths, so 0.016.",
                   "(c) 12/10 is 1 unit and 2 tenths, so 1.2.",
                   "(d) 254/1000 is 2 tenths, 5 hundredths and 4 thousandths, so 0.254."],
                  "(a) 0.05 (b) 0.016 (c) 1.2 (d) 0.254", tool="place_chart_decimal_writer"),
              FIO("end.FiO2", "Figure it Out (end of chapter), Q2",
                  "Convert the following decimals into a sum of tenths, hundredths and thousandths: (a) 0.34 (b) "
                  "1.02 (c) 0.8 (d) 0.362",
                  ["(a) 0.34 has 3 tenths and 4 hundredths: 3/10 + 4/100.",
                   "(b) 1.02 has 1 unit, 0 tenths and 2 hundredths: 1 + 2/100, where the unit is 100/100.",
                   "(c) 0.8 has 8 tenths: 8/10.",
                   "(d) 0.362 has 3 tenths, 6 hundredths and 2 thousandths: 3/10 + 6/100 + 2/1000."],
                  "(a) 3/10 + 4/100 (b) 100/100 + 2/100, which is 1 + 2/100 (c) 8/10 (d) 3/10 + 6/100 + 2/1000"),
              FIO("end.FiO14", "Figure it Out (end of chapter), Q14",
                  "Write the decimal forms of the quantities mentioned. An example is given: 87 ones, 5 tenths and "
                  "60 hundredths is 88.10. (a) 12 tens and 12 tenths (b) 10 tens, 10 ones, 10 tenths, and 10 "
                  "hundredths (c) 25 tens, 25 ones, 25 tenths, and 25 hundredths",
                  ["Example: 87 + 0.5 + 0.60 = 88.10, since 60 hundredths is 6 tenths.",
                   "(a) 12 tens is 120, and 12 tenths is 1.2, so 121.2.",
                   "(b) 10 tens is 100, 10 ones is 10, 10 tenths is 1, and 10 hundredths is 0.1, so 111.1.",
                   "(c) 25 tens is 250, 25 ones is 25, 25 tenths is 2.5, and 25 hundredths is 0.25: 250 + 25 + 2.5 "
                   "+ 0.25 = 277.75."],
                  "(a) 121.2 (b) 111.1 (c) 277.75"),
              FIO("end.FiO16", "Figure it Out (end of chapter), Q16",
                  "Write the following fractions in decimal form: (a) 1/2 (b) 3/2 (c) 1/4 (d) 3/4 (e) 1/5 (f) 4/5",
                  ["(a) 1/2 is 5/10, so 0.5.",
                   "(b) 3/2 is 15/10, so 1.5.",
                   "(c) 1/4 is 25/100, so 0.25.",
                   "(d) 3/4 is 75/100, so 0.75.",
                   "(e) 1/5 is 2/10, so 0.2.",
                   "(f) 4/5 is 8/10, so 0.8."],
                  "(a) 0.5 (b) 1.5 (c) 0.25 (d) 0.75 (e) 0.2 (f) 0.8")])]))

# ============================== T8 Units of measurement ======================================================
TOPICS.append(TOPIC(
    "T8", "M2", "Units of Measurement", ["3.5"], "Apply",
    "Students convert between millimetres, centimetres, metres and kilometres, between grams, kilograms and "
    "milligrams, and between paise and rupees, by writing the smaller unit as a decimal part of the bigger unit.",
    "A smaller unit is one-tenth, one-hundredth or one-thousandth of the bigger unit, so changing units moves the "
    "decimal point by as many places as there are zeroes in the exchange rate.",
    [A("T8.C1", "Length: millimetres, centimetres and metres", "Apply",
       "Students convert between millimetres and centimetres and between centimetres and metres by using one tenth "
       "and one hundredth as the exchange rates.",
       textbook=["3.5 Units of Measurement",
                 "Length Conversion",
                 "We have been using a scale to measure length for a few years. We already know that 1 cm = 10 mm "
                 "(millimeters). How many cm is 1 mm?",
                 "1 mm = 1/10 cm = 0.1 cm (i.e., one-tenth of a cm). How many cm is (a) 5 mm? (b) 12 mm?",
                 "5 mm = 5/10 cm = 0.5 cm. 12 mm = 10 mm + 2 mm = 1 cm + 2/10 cm = 1.2 cm.",
                 "How many mm is 5.6 cm? Since each cm has 10 mm, 5.6 cm (5 cm + 0.6 cm) is 56 mm.",
                 "Fill in the blanks below (mm to cm): 12 mm = 1.2 cm, 56 mm = 5.6 cm, 70 mm = _____, _____ = 0.9 "
                 "cm, 134 mm = _____, _____ = 203.6 cm",
                 "We also know that 1 m = 100 cm. Based on this, we can say that 1 cm = 1/100 m = 0.01 m.",
                 "How many m is (a) 10 cm? (b) 15 cm? 10 cm = 10/100 m = 1/10 m = 0.1 m. Since each cm is "
                 "one-hundredth of a meter, 15 cm can be written as 15 cm = 15/100 m = 10/100 m + 5/100 m = 1/10 m + "
                 "5/100 m = 0.15 m.",
                 "Fill in the blanks below (cm to m): 36 cm = _____, 50 cm = _____, _____ = 0.89 m, 4 cm = _____, "
                 "325 cm = _____, _____ = 2.07 m",
                 "How many mm does 1 meter have? Can we write 1 mm = 1/1000 m?"],
       teach=["Predict first: 12 mm is more than a centimetre. Will it be 0.12 cm or 1.2 cm?",
              "10 mm make 1 cm, so each mm is a tenth of a cm. 12 mm is 1 cm and 2 tenths of a cm.",
              "100 cm make 1 m, so each cm is a hundredth of a metre. 15 cm is 1 tenth and 5 hundredths of a metre.",
              "The illustration of small things (a hair, a newspaper, a mustard seed, the smallest ant and snail) "
              "shows how many tiny lengths are written in mm with decimals. Try an approximate measure of each."],
       examples=[
           WE("Fill in the blanks (mm to cm): 12 mm, 56 mm, 70 mm, 9 mm, 134 mm, and the length in mm that is 203.6 "
              "cm.",
              ["1 mm is 1/10 cm = 0.1 cm.",
               "12 mm = 10 mm + 2 mm = 1 cm + 0.2 cm = 1.2 cm.",
               "56 mm = 5.6 cm. 70 mm = 7.0 cm. 9 mm = 0.9 cm. 134 mm = 13.4 cm.",
               "203.6 cm is 203 cm and 6 tenths of a cm. Each cm is 10 mm, so 2036 mm."],
              "56 mm = 5.6 cm; 70 mm = 7.0 cm; 9 mm = 0.9 cm; 134 mm = 13.4 cm; 203.6 cm = 2036 mm",
              ncert=["3.5.mm_cm", "3.5.mm_cm_blanks", "3.5.small_things"]),
           WE("Fill in the blanks (cm to m): 36 cm, 50 cm, the cm that make 0.89 m, 4 cm, 325 cm, and the cm that "
              "make 2.07 m. How many mm make 1 m, and can we write 1 mm = 1/1000 m?",
              ["1 cm is 1/100 m = 0.01 m. 36 cm = 0.36 m. 50 cm = 0.50 m = 0.5 m.",
               "0.89 m = 89 cm. 4 cm = 0.04 m. 325 cm = 3.25 m. 2.07 m = 207 cm.",
               "1 m = 100 cm and each cm is 10 mm, so 100 × 10 = 1000 mm make 1 m.",
               "So 1 mm is 1/1000 of a metre, and yes, we can write 1 mm = 1/1000 m = 0.001 m."],
              "36 cm = 0.36 m; 50 cm = 0.5 m; 89 cm = 0.89 m; 4 cm = 0.04 m; 325 cm = 3.25 m; 207 cm = 2.07 m; "
              "1 m = 1000 mm; yes",
              ncert=["3.5.cm_m", "3.5.cm_m_blanks", "3.5.m_mm", "3.5.facts_cm"])],
       key_terms=["millimetre"], misconceptions=["M_UNIT_SHIFT"], minutes=10),
     A("T8.C2", "Weight: grams, kilograms and milligrams", "Apply",
       "Students convert between grams and kilograms with one thousandth as the exchange rate, and between "
       "milligrams and grams.",
       textbook=["Weight Conversion",
                 "Let us look at kilograms (kg). We know that 1 kg = 1000 gram (g). We can say that 1 g = 1/1000 kg = "
                 "0.001 kg.",
                 "How many kilograms is 5 g? 5 g = 5/1000 kg = 0.005 kg. How many kilograms is 10 g? 10 g = 10/1000 "
                 "kg = 1/100 kg = 0.010 kg.",
                 "As each gram is one-thousandth of a kg, 254 g can be written as 254 g = 254/1000 kg = (200/1000 + "
                 "50/1000 + 4/1000) kg = (2/10 + 5/100 + 4/1000) kg = 0.254 kg.",
                 "Fill in the blanks below (g to kg): 465 g = _____, 68 g = _____, 1560 g = _____, 704 g = _____, "
                 "_____ = 0.56 kg, _____ = 2.5 kg",
                 "Look at the picture below showing different quantities of rice. Starting from the 1g heap, "
                 "subsequent heaps can be found that are 10 times heavier than the previous heap/packets. The "
                 "combined weight of rice in this picture is 11.111 kg.",
                 "Also, 1 gram = 1000 milligrams (mg). So, 1 mg = 1/1000 g = 0.001 g."],
       teach=["Predict first: 5 g in kilograms. Will it be 0.5, 0.05 or 0.005 kg?",
              "1000 g make 1 kg, so each gram is a thousandth of a kg. 254 g is 2 tenths, 5 hundredths and 4 "
              "thousandths of a kg.",
              "The same pattern holds one level down: 1000 mg make 1 g, so 1 mg is 0.001 g."],
       examples=[
           WE("Fill in the blanks (g to kg): 465 g, 68 g, 1560 g, 704 g, and the grams in 0.56 kg and in 2.5 kg.",
              ["1 g is 1/1000 kg = 0.001 kg, so the point moves 3 places left.",
               "465 g = 0.465 kg. 68 g = 0.068 kg, with a zero in the tenths place.",
               "1560 g = 1.560 kg = 1.56 kg. 704 g = 0.704 kg.",
               "0.56 kg = 560 g. 2.5 kg = 2500 g."],
              "465 g = 0.465 kg; 68 g = 0.068 kg; 1560 g = 1.56 kg; 704 g = 0.704 kg; 0.56 kg = 560 g; "
              "2.5 kg = 2500 g", ncert=["3.5.g_kg", "3.5.g_kg_blanks"]),
           WE("Rice heaps start at 1 g and each next heap is 10 times heavier than the one before. There are five "
              "heaps: 1 g, 10 g, 100 g, 1 kg and 10 kg. Show their combined weight is 11.111 kg. Then write 1 mg "
              "in grams.",
              ["In grams the heaps are 1, 10, 100, 1000 and 10000.",
               "Total: 1 + 10 + 100 + 1000 + 10000 = 11111 g.",
               "11111 g = 11.111 kg, since 1000 g make a kg.",
               "1 g = 1000 mg, so 1 mg = 1/1000 g = 0.001 g."],
              "11.111 kg; 1 mg = 0.001 g", ncert=["3.5.rice", "3.5.mg", "3.5.facts_nature"])],
       key_terms=["milligram"], misconceptions=["M_UNIT_SHIFT"], minutes=10),
     A("T8.C3", "Money: paise and rupees", "Apply",
       "Students convert between paise and rupees with one hundredth as the exchange rate, and compare old and new "
       "prices.",
       textbook=["Rupee ─ Paise conversion",
                 "You may have heard of ‘paisa’. 100 paise is equal to 1 rupee. As we have coins and notes for "
                 "rupees, coins for paise were also used commonly until recently. There were coins for 1 paisa, 2 "
                 "paise, 3 paise, 5 paise, 10 paise, 20 paise, 25 paise, and 50 paise. All denominations of 25 "
                 "paise and less were removed from use in the year 2011. But we still see paise in bills, account "
                 "statements, etc.",
                 "1 rupee = 100 paise. 1 paisa = 1/100 rupee = 0.01 rupee. As each paisa is one-hundredth of a "
                 "rupee, 75 paise = 75/100 rupee = (70/100 + 5/100) rupee = (7/10 + 5/100) rupee = 0.75 rupee.",
                 "Fill in the blanks below (rupee to paise): 10 p = _____, _____ p = ₹ 0.05, _____ p = ₹ 0.36, "
                 "_____ = ₹ 0.50, 99 p = _____, 250 p = _____",
                 "During the 1970s, a masala dosa cost just 50 paise, one could buy a banana for 20 to 25 paise, a "
                 "handful of peppermints were available for 2 paise or 3 paise, and a kg of rice cost ₹2.45.",
                 "Discuss with adults at home/school the prices of different products and services during their "
                 "childhood. Try to find old coins and stamps."],
       teach=["Predict first: 75 paise in rupees. Is it 7.5, 0.75 or 0.075?",
              "100 paise make a rupee, so each paisa is a hundredth of a rupee. 75 paise is 7 tenths and 5 "
              "hundredths of a rupee.",
              "In the 1970s a masala dosa cost 50 paise, a banana 20 to 25 paise, a handful of peppermints 2 or 3 "
              "paise and a kilogram of rice Rs 2.45.",
              "Ask adults at home about prices in their childhood, and look for old coins and stamps."],
       examples=[
           WE("Fill in the blanks (paise to rupees): 10 p, 5 p, 36 p, 50 p, 99 p, 250 p. Then write 75 paise in "
              "rupees, step by step.",
              ["1 paisa is 1/100 rupee = ₹0.01, so the point moves 2 places left.",
               "75 paise = 75/100 rupee = 70/100 + 5/100 = 7/10 + 5/100 = ₹0.75.",
               "10 p = ₹0.10. 5 p = ₹0.05. 36 p = ₹0.36. 50 p = ₹0.50. 99 p = ₹0.99. 250 p = ₹2.50."],
              "75 p = ₹0.75; 10 p = ₹0.10; 5 p = ₹0.05; 36 p = ₹0.36; 50 p = ₹0.50; 99 p = ₹0.99; "
              "250 p = ₹2.50", ncert=["3.5.paise", "3.5.paise_blanks"]),
           WE("A masala dosa cost 50 paise in the 1970s, and a kg of rice cost ₹2.45. Write the dosa price in "
              "rupees, and say how many such dosas the rice price would buy.",
              ["50 paise = ₹0.50.",
               "A kg of rice cost ₹2.45, which is 245 paise.",
               "245 ÷ 50 = 4.9, so the rice price would buy 4 dosas and a little more.",
               "Prices from your own elders' childhood can be written the same way in rupees with a decimal."],
              "₹0.50 for the dosa; ₹2.45 buys 4 dosas with 45 paise left", ncert=["3.5.old_prices"])],
       key_terms=["paise"], misconceptions=["M_UNIT_SHIFT"], minutes=10),
     DOER("T8.C4", "Practice: convert between units", "exchange_rate_step_counter", "Apply",
          "Students convert lengths, weights and money between a bigger and a smaller unit by moving the decimal "
          "point.",
          ["Find the exchange rate between the two units: 10, 100 or 1000.",
           "To a bigger unit, divide, which moves the point left; to a smaller unit, multiply, which moves it "
           "right.",
           "Check by converting back."],
          items=[
              FIO("end.FiO11", "Figure it Out (end of chapter), Q11",
                  "How many millimetres make 1 kilometre?",
                  ["1 km = 1000 m.", "1 m = 1000 mm.", "So 1 km = 1000 × 1000 mm = 1000000 mm."],
                  "1000000 mm (ten lakh millimetres)", tool="exchange_rate_step_counter"),
              FIO("end.FiO12", "Figure it Out (end of chapter), Q12",
                  "Indian Railways offers optional travel insurance for passengers who book e-tickets. It costs 45 "
                  "paise per passenger. If 1 lakh people opt for insurance in a day, what is the total insurance "
                  "fee paid?",
                  ["1 lakh is 100000 passengers.",
                   "Total in paise: 45 × 100000 = 4500000 paise.",
                   "100 paise make 1 rupee, so 4500000 paise = ₹45000."],
                  "₹45,000", tool="exchange_rate_step_counter")])]))

# ============================== T9 Locating decimals on the number line ======================================
TOPICS.append(TOPIC(
    "T9", "M3", "Locating Decimals on the Number Line", ["3.6"], "Apply",
    "Students locate a decimal on the number line by zooming digit by digit, read the decimal at a marked point on "
    "a line, and work out the value of one division when the line has different end marks.",
    "Each digit of a decimal tells which of 10 equal parts to zoom into next; the end marks of a line decide what "
    "one division is worth.",
    [A("T9.C1", "Tenths and hundredths on the number line", "Understand",
       "Students locate a decimal on the number line by splitting the unit into 10 equal parts, name the "
       "divisions between 1 and 1.1, and read decimals at marks.",
       textbook=["3.6 Locating and Comparing Decimals",
                 "Let us consider the decimal number 1.4. It is equal to 1 unit and 4 tenths. This means that the "
                 "unit between 1 and 2 is divided into 10 equal parts, and 4 such parts are taken. Hence, 1.4 lies "
                 "between 1 and 2. Draw the number line and divide the unit between 1 and 2 into 10 equal parts. "
                 "Take the fourth part, and we have 1.4 on the number line.",
                 "Name all the divisions between 1 and 1.1 on the number line.",
                 "Identify and write the decimal numbers against the letters."],
       teach=["Predict first: where does 1.4 sit on the number line, nearer 1 or nearer 2?",
              "Split the unit from 1 to 2 into 10 equal parts and count 4 parts from 1.",
              "Zoom into the part between 1 and 1.1 and split it into 10 as well: the new marks are hundredths."],
       examples=[
           WE("Locate 1.4 on the number line. Then name all the divisions between 1 and 1.1.",
              ["1.4 is 1 unit and 4 tenths, so it lies between 1 and 2.",
               "Split the unit from 1 to 2 into 10 equal parts: 1.1, 1.2, 1.3 and so on, and take the 4th part to "
               "reach 1.4.",
               "Between 1 and 1.1 split the gap into 10 equal parts as well; each part is 1 hundredth.",
               "The divisions are 1.01, 1.02, 1.03, 1.04, 1.05, 1.06, 1.07, 1.08 and 1.09."],
              "1.4 is the 4th mark after 1; the divisions are 1.01 to 1.09", ncert=["3.6.one_four", "3.6.divisions"]),
           WE("A line has large marks at 5, 5.1, 5.2, 5.3 and 5.4, with 10 small marks between neighbouring large "
              "marks. The letter A is 9 small marks after 5, B is 3 small marks after 5.1, C is on the large mark "
              "5.2 and D is 1 small mark after 5.3. Read the decimal at each letter.",
              ["Large marks are tenths: 5, 5.1, 5.2, 5.3, 5.4.",
               "Ten small marks fill a tenth, so each small mark is one hundredth.",
               "A is 9 small marks after 5: 5 + 0.09 = 5.09.",
               "B is 3 small marks after 5.1: 5.1 + 0.03 = 5.13.",
               "C is on the large mark 5.2.",
               "D is 1 small mark after 5.3: 5.3 + 0.01 = 5.31."],
              "A = 5.09, B = 5.13, C = 5.2, D = 5.31", ncert=["3.6.identify_abcd"])],
       key_terms=["number line"], misconceptions=["M_LINE_MARKS"], minutes=10),
     A("T9.C2", "Zooming in digit by digit", "Apply",
       "Students locate a decimal such as 4.185 by zooming into one gap per digit, read the decimal at the end of a "
       "zoom, and draw zoom lines for 9.876 and 0.407.",
       textbook=["Observe the number lines in Figure (a) below. At each level, a particular segment of the number "
                 "line is magnified to locate the number 4.185.",
                 "Identify the decimal number in the last number line in Figure (b) denoted by ‘?’.",
                 "Make such number lines for the decimal numbers: (a) 9.876 (b) 0.407."],
       teach=["Predict first: to find 4.185, which two whole numbers do we zoom into first?",
              "Each digit gives one zoom. The 4 chooses the gap 4 to 5; the 1 chooses the gap 4.1 to 4.2; the 8 "
              "chooses 4.18 to 4.19; the 5 chooses the middle mark 4.185.",
              "To read a decimal at a mark, read the end marks of each zoom in turn."],
       examples=[
           WE("Locate 4.185 by zooming. Then read the decimal marked '?' in a zoom that goes from 3 to 4, then "
              "3.0 to 3.1, then 3.05 to 3.06, and ends at the 9th mark of the last gap of 10 parts.",
              ["4.185: the units digit 4 gives the gap 4 to 5. The tenths digit 1 gives 4.1 to 4.2. The "
               "hundredths digit 8 gives 4.18 to 4.19. The thousandths digit 5 gives the middle mark, 4.185.",
               "'?': the first zoom is 3 to 4, so units 3. The second zoom is 3.0 to 3.1, so tenths 0. The third "
               "zoom is 3.05 to 3.06, so hundredths 5. The mark is the 9th part after 3.05 in a gap of 10 parts.",
               "9 thousandths more than 3.05, so the decimal is 3.059."],
              "4.185 is the middle mark of 4.18 to 4.19; '?' is 3.059", ncert=["3.6.zoom_4185", "3.6.zoom_q"]),
           WE("Make the zoom lines for (a) 9.876 and (b) 0.407.",
              ["(a) 9.876: zoom 9 to 10, then 9.8 to 9.9, then 9.87 to 9.88, and mark the 6th of 10 parts.",
               "(b) 0.407: zoom 0 to 1, then 0.4 to 0.5, then 0.40 to 0.41, and mark the 7th of 10 parts.",
               "Notice the zero in 0.407: the hundredths digit 0 means the zoom takes the very first gap, 0.40 to "
               "0.41."],
              "(a) 9 to 10, 9.8 to 9.9, 9.87 to 9.88, mark 9.876 (b) 0 to 1, 0.4 to 0.5, 0.40 to 0.41, mark 0.407",
              ncert=["3.6.zoom_make"])],
       key_terms=["zoom"], misconceptions=["M_LINE_MARKS"], minutes=10),
     A("T9.C3", "Reading marks on lines with different end points", "Analyze",
       "Students find the value of one division on a line with given end points and use it to read the decimals at "
       "marked points.",
       textbook=["In the number line shown below, what decimal numbers do the boxes labelled ‘a’, ‘b’, and ‘c’ "
                 "denote?",
                 "The box with ‘b’ corresponds to the decimal number 7.5; are you able to see how? There are 5 units "
                 "between 5 and 10, divided into 10 equal parts. Hence, every 2 divisions make a unit, and so every "
                 "division is 1/2 unit. What numbers do ‘a’ and ‘c’ denote?",
                 "Using similar reasoning find out the decimal numbers in the boxes below."],
       teach=["Predict first: a line from 5 to 10 is cut into 10 equal parts. Is each part one tenth?",
              "No. The length is 5 units, so each part is 5 divided by 10, which is half a unit.",
              "Always find the value of one division first: the length of the line divided by the number of parts."],
       examples=[
           WE("On a line from 5 to 10 cut into 10 equal parts, the box b is at the 5th division, a is at the 2nd "
              "division and c is at the 9th. Find the decimals.",
              ["The line is 10 − 5 = 5 units long, in 10 equal parts, so each part is 0.5.",
               "b: 5 parts after 5 is 5 + 5 × 0.5 = 7.5.",
               "a: 2 parts after 5 is 5 + 2 × 0.5 = 6.",
               "c: 9 parts after 5 is 5 + 9 × 0.5 = 9.5."],
              "a = 6, b = 7.5, c = 9.5", ncert=["3.6.line5to10"]),
           WE("One line runs from 8 to 8.1 and is cut into 10 equal parts, with d at the 1st mark and e at the "
              "5th. Another line starts at 4.3 and has marks every 0.05, with 4.8 at the 10th mark. The letter f "
              "is at the 1st mark, g is at the 4th mark and h is one mark past the 4.8 label. Find d, e, f, g "
              "and h.",
              ["Line 8 to 8.1: it is 0.1 long in 10 parts, so each part is 0.01. d is 8.01 and e is 8.05.",
               "Line from 4.3: 10 marks of 0.05 reach 4.3 + 0.5 = 4.8, which fits the label.",
               "f: 1 mark after 4.3 is 4.3 + 0.05 = 4.35.",
               "g: 4 marks after 4.3 is 4.3 + 0.20 = 4.5.",
               "h: one mark past 4.8 is 4.8 + 0.05 = 4.85."],
              "d = 8.01, e = 8.05, f = 4.35, g = 4.5, h = 4.85", ncert=["3.6.line_def"])],
       key_terms=["division"], misconceptions=["M_LINE_MARKS"], minutes=10),
     DOER("T9.C4", "Practice: locate and read decimals on a number line", "digit_zoom_locator", "Apply",
          "Students locate decimals by zooming and read the decimals at marked points on lines with different end "
          "points.",
          ["Each digit gives one zoom into one of ten equal parts.",
           "Find the value of one division first: the length of the line divided by the number of parts.",
           "Read the end marks of the last zoom to name the decimal."],
          items=[
              FIO("end.FiO3", "Figure it Out (end of chapter), Q3",
                  "What decimal number does each letter represent in the number line? The line runs from 6.4 to "
                  "6.6, with marks every 0.025 between them. The point a is at the 2nd mark after 6.4, the point "
                  "c is at the 5th mark and the point b is at the 6th mark.",
                  ["The line runs from 6.4 to 6.6, which is 0.2 long, with 8 equal parts.",
                   "Each mark is 0.2 ÷ 8 = 0.025 apart.",
                   "a: 2 marks after 6.4 is 6.4 + 2 × 0.025 = 6.45.",
                   "c: 5 marks after 6.4 is 6.4 + 5 × 0.025 = 6.525.",
                   "b: 6 marks after 6.4 is 6.4 + 6 × 0.025 = 6.55."],
                  "a = 6.45, c = 6.525, b = 6.55", tool="digit_zoom_locator")])]))

# ============================== T10 Comparing and closest decimals ===========================================
TOPICS.append(TOPIC(
    "T10", "M3", "Comparing and Closest Decimals", ["3.6"], "Analyze",
    "Students compare decimals place by place from the left, show that zeroes at the right end do not change a "
    "decimal, order a group of decimals, and find the decimal closest to a given number.",
    "Decimals are compared from the biggest place down to the first place where the digits differ; a zero at the "
    "end changes nothing, and the closest number is the one with the smallest gap.",
    [A("T10.C1", "The zero dilemma", "Analyze",
       "Students decide whether zeroes written at the right end of a decimal change its value, using a place value "
       "table, and tell which decimals among a group are equal.",
       textbook=["There is Zero Dilemma!",
                 "Sonu says that 0.2 can also be written as 0.20, 0.200; Zara thinks that putting zeros on the "
                 "right side may alter the value of the decimal number. What do you think?",
                 "We can figure this out by looking at the quantities these numbers represent using place value.",
                 "We can see that 0.2, 0.20, and 0.200 are all equal as they represent the same quantity, i.e., 2 "
                 "tenths. But 0.2, 0.02, and 0.002 are different.",
                 "Can you tell which of these is the smallest and which is the largest?",
                 "Which of these are the same: 4.5, 4.05, 0.405, 4.050, 4.50, 4.005, 04.50?"],
       teach=["Predict first: Sonu says 0.2 equals 0.20 and 0.200. Zara says extra zeroes may change the value. "
              "Who is right?",
              "Put each in a place table. 0.2 is 2 tenths. 0.20 is 2 tenths and 0 hundredths. 0.200 adds 0 "
              "thousandths. All three are 2 tenths.",
              "A zero at the far right adds nothing. A zero between the point and a digit changes everything: 0.02 "
              "is 2 hundredths."],
       examples=[
           WE("Use a place table to settle Sonu and Zara, and then say which of 0.2, 0.20, 0.200, 0.02 and 0.002 "
              "is smallest and largest.",
              ["0.2: units 0, tenths 2. 0.20: tenths 2, hundredths 0. 0.200: tenths 2, hundredths 0, thousandths 0.",
               "All three show 2 tenths, so Sonu is right: they are equal.",
               "0.02 is 2 hundredths and 0.002 is 2 thousandths, which are different quantities.",
               "2 tenths is the most, then 2 hundredths, then 2 thousandths: the largest is 0.2 (= 0.20 = 0.200) "
               "and the smallest is 0.002."],
              "0.2, 0.20 and 0.200 are equal; the smallest is 0.002", ncert=["3.6.zero_dilemma", "3.6.zero_order"]),
           WE("Which of these are the same: 4.5, 4.05, 0.405, 4.050, 4.50, 4.005, 04.50?",
              ["Strip zeroes from the right end of the decimal part and from the left end of the whole part.",
               "4.50 is 4.5 and 04.50 is 4.5, so 4.5, 4.50 and 04.50 are equal.",
               "4.050 is 4.05, so 4.05 and 4.050 are equal.",
               "0.405 and 4.005 are different from all of these."],
              "4.5 = 4.50 = 04.50, and 4.05 = 4.050; 0.405 and 4.005 stand alone", ncert=["3.6.same"])],
       key_terms=["equal decimals"], misconceptions=["M_RIGHT_ZERO"], minutes=10),
     A("T10.C2", "Comparing place by place", "Analyze",
       "Students compare two decimals digit by digit from the biggest place, stop at the first place where the "
       "digits differ, and explain why the later digits cannot change the answer.",
       textbook=["Which is larger: 6.456 or 6.465?",
                 "To answer this, we can use the number line to locate both decimal numbers and show which is "
                 "larger. This can also be done by comparing the corresponding digits at each place value, as we do "
                 "with whole numbers. This comparison is visualised step by step below.",
                 "Both numbers have 6 units. Both numbers have 6 units and 4 tenths. Both numbers have 6 units and 4 "
                 "tenths, but the first number has only 5 hundredths, whereas the second number has 6 hundredths.",
                 "We start by comparing the most significant digits (digits with the highest place value) of the "
                 "two numbers. If the digits are the same, we compare the next smaller place value. We keep going "
                 "till we find a position where the digits are not equal. The number with the larger digit at this "
                 "position is the greater of the two.",
                 "Why can we stop comparing at this point? Can we be sure that whatever digits are there after this "
                 "will not affect our conclusion?",
                 "Which decimal number is greater? (a) 1.23 or 1.32 (b) 3.81 or 13.800 (c) 1.009 or 1.090"],
       teach=["Predict first: 6.456 or 6.465. The first has the digits 456 and the second 465. Which is bigger?",
              "Start from the biggest place. Both have 6 units, and both have 4 tenths. At the hundredths, 5 is "
              "less than 6.",
              "So we stop there. The digits after only add less than one more hundredth, so they cannot undo the "
              "difference of one hundredth."],
       examples=[
           WE("Which is larger, 6.456 or 6.465? Compare step by step and say why we can stop.",
              ["Units: 6 and 6, equal. Tenths: 4 and 4, equal.",
               "Hundredths: 5 and 6, and 6 is greater, so 6.465 is the greater number.",
               "Why stop: the digits after the hundredths place together are less than 1 hundredth. So the first "
               "number can gain at most just under one more hundredth, and the second is already one hundredth "
               "ahead."],
              "6.465 is larger", ncert=["3.6.compare_6456", "3.6.why_stop"]),
           WE("Which is greater? (a) 1.23 or 1.32 (b) 3.81 or 13.800 (c) 1.009 or 1.090",
              ["(a) Units equal. Tenths: 2 and 3, so 1.32 is greater.",
               "(b) Tens: 3.81 has 0 tens and 13.800 has 1 ten, so 13.800 is greater, though it has a zero at the "
               "end.",
               "(c) Units equal, tenths equal at 0. Hundredths: 0 and 9, so 1.090 is greater."],
              "(a) 1.32 (b) 13.800 (c) 1.090", ncert=["3.6.compare_three"])],
       key_terms=["compare"], misconceptions=["M_MORE_DIGITS_BIGGER", "M_FIRST_DIGIT"], minutes=10),
     A("T10.C3", "Closest decimals", "Analyze",
       "Students find the decimal nearest to a target by comparing the size of each gap, and use a set of digits to "
       "make a decimal as close as possible to a target.",
       textbook=["Closest Decimals",
                 "Consider the decimal numbers 0.9, 1.1, 1.01, and 1.11. Identify the decimal number that is closest "
                 "to 1.",
                 "Let us compare the decimal numbers. Arranging these in ascending order, we get 0.9 < 1 < 1.01 < 1.1 "
                 "< 1.11. Among the neighbours of 1, 1.01 is 1/100 away from 1 whereas 0.9 is 10/100 away from 1. "
                 "Therefore, 1.01 is closest to 1.",
                 "Which of the above is closest to 1.09?",
                 "Which among these is closest to 4: 3.56, 3.65, 3.099?",
                 "Which among these is closest to 1: 0.8, 0.69, 1.08?",
                 "In each case below use the digits 4, 1, 8, 2, and 5 exactly once and try to make a decimal "
                 "number as close as possible to 25."],
       teach=["Predict first: which of 0.9, 1.1, 1.01 and 1.11 is nearest to 1? Do not use the first digit alone.",
              "Closeness means the size of the gap, found by subtracting the smaller from the bigger.",
              "To build a number close to 25 from digits, put the digits so the tens and units are 2 and 5."],
       examples=[
           WE("Which of 0.9, 1.1, 1.01 and 1.11 is closest to 1? Then which is closest to 1.09?",
              ["Gaps from 1: 0.9 is 0.1 away, 1.1 is 0.1 away, 1.01 is 0.01 away, and 1.11 is 0.11 away. So 1.01 "
               "is closest.",
               "Gaps from 1.09: 0.9 is 0.19, 1.1 is 0.01, 1.01 is 0.08, and 1.11 is 0.02.",
               "The smallest gap is 0.01, so 1.1 is closest to 1.09."],
              "1.01 is closest to 1; 1.1 is closest to 1.09", ncert=["3.6.closest1", "3.6.closest109"]),
           WE("Which of 3.56, 3.65 and 3.099 is closest to 4? Which of 0.8, 0.69 and 1.08 is closest to 1?",
              ["Gaps from 4: 3.56 is 0.44, 3.65 is 0.35, and 3.099 is 0.901. The smallest is 0.35, so 3.65.",
               "Gaps from 1: 0.8 is 0.2, 0.69 is 0.31, and 1.08 is 0.08. The smallest is 0.08, so 1.08."],
              "3.65 is closest to 4; 1.08 is closest to 1", ncert=["3.6.closest4", "3.6.closest_1b"]),
           WE("Use the digits 4, 1, 8, 2 and 5 exactly once each to make a decimal as close as possible to 25, "
              "with the point placed in different places.",
              ["With the point after one digit, such as 8.5421, the number is far from 25.",
               "With the point after two digits, the tens and units can be 2 and 5: 25.148, which is 0.148 from 25.",
               "With the point after three digits, such as 124.58, the number is far too big.",
               "The best layout puts 2 and 5 as tens and units, then the smallest digits after the point: the "
               "remaining digits 1, 4 and 8 in order give 25.148."],
              "25.148 is the closest, 0.148 away", ncert=["3.6.closest25"])],
       key_terms=["closest"], misconceptions=["M_FIRST_DIGIT"], minutes=10),
     DOER("T10.C4", "Practice: compare, order and find the closest", "place_by_place_comparator", "Analyze",
          "Students compare and order decimals place by place and find the decimal closest to a number.",
          ["Compare from the biggest place and stop at the first place where the digits differ.",
           "Zeroes at the right end change nothing; zeroes before a digit do.",
           "For closeness, find each gap and pick the smallest gap."],
          items=[
              FIO("end.FiO4", "Figure it Out (end of chapter), Q4",
                  "Arrange the following quantities in descending order: (a) 11.01, 1.011, 1.101, 11.10, 1.01 (b) "
                  "2.567, 2.675, 2.768, 2.499, 2.698 (c) 4.678 g, 4.595 g, 4.600 g, 4.656 g, 4.666 g (d) 33.13 m, "
                  "33.31 m, 33.133 m, 33.331 m, 33.313 m",
                  ["(a) Write with 3 decimal places: 11.010, 1.011, 1.101, 11.100, 1.010. The tens digit puts 11.100 "
                   "and 11.010 first, then 1.101, 1.011 and 1.010.",
                   "(b) Tenths: 5, 6, 7, 4, 6. So 2.768 first and 2.499 last; of the 6s, 2.698 is above 2.675; of "
                   "the 5s, only 2.567.",
                   "(c) Hundredths decide: 4.678 g, 4.666 g, 4.656 g, 4.600 g, 4.595 g.",
                   "(d) Write with 3 decimal places: 33.130, 33.310, 33.133, 33.331, 33.313. The order is 33.331, "
                   "33.313, 33.310, 33.133, 33.130."],
                  "(a) 11.10, 11.01, 1.101, 1.011, 1.01 (b) 2.768, 2.698, 2.675, 2.567, 2.499 (c) 4.678 g, 4.666 "
                  "g, 4.656 g, 4.600 g, 4.595 g (d) 33.331 m, 33.313 m, 33.31 m, 33.133 m, 33.13 m",
                  tool="place_by_place_comparator"),
              FIO("end.FiO5", "Figure it Out (end of chapter), Q5",
                  "Using the digits 1, 4, 0, 8, and 6 make: (a) the decimal number closest to 30 (b) the smallest "
                  "possible decimal number between 100 and 1000.",
                  ["(a) A number close to 30 needs its tens and units digits close to 30. The digits 1, 4, 0, 8, "
                   "6 cannot make 3, so try the tens digit 4 with the smallest digits after it: 40.168, which is "
                   "10.168 away.",
                   "Other tries are farther: 18.046 is 11.954 below 30, and 61.048 is 31.048 above 30.",
                   "(b) Between 100 and 1000 means 3 whole digits. The smallest puts the smallest non-zero digit "
                   "first, 1, then 0, then 4, then the rest in order: 104.68."],
                  "(a) 40.168 (b) 104.68"),
              FIO("end.FiO6", "Figure it Out (end of chapter), Q6",
                  "Will a decimal number with more digits be greater than a decimal number with fewer digits?",
                  ["Try 2.05 and 2.5. The first has more digits after the point.",
                   "Tenths: 0 and 5, so 2.5 is greater.",
                   "So the number of digits does not decide, and the answer is no."],
                  "No. For example 2.5 is greater than 2.05, though 2.05 has more digits")])]))
