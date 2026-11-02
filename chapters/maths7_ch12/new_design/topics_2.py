# -*- coding: utf-8 -*-
"""Topics T6 to T11 (module M2: dividing decimals). Book section 4.3."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T6 Dividing by 10, 100, 1000 ===================================================
TOPICS.append(TOPIC(
    "T6", "M2", "Dividing a Decimal by 10, 100 and 1000", ["4.3"], "Apply",
    "Students divide a decimal by 10 and 100 by multiplying its fraction by the reciprocal, convert the result "
    "between metres, centimetres and millimetres, and divide decimals by 10, 100, 1000 and 10000 by moving the "
    "decimal point left.",
    "Dividing by 10, 100 or 1000 multiplies the denominator by the same number, so the decimal point moves left by "
    "as many places as the divisor has zeroes.",
    [A("T6.C1", "Cutting a ribbon into 10 and 100 pieces", "Apply",
       "Students find 3.9 ÷ 10 and 3.9 ÷ 100 by writing 3.9 as a fraction and multiplying by the reciprocal of the "
       "divisor, then write 0.039 m in centimetres and millimetres.",
       textbook=["4.3 Decimal Division",
                 "Example 6: Anuja has a 3.9 m length of ribbon and she wants to cut it into 10 equal pieces. What is "
                 "the length of each piece in decimal?",
                 "Recall that, dividing a fraction by a divisor is the same as multiplying the fraction by the "
                 "reciprocal of the divisor. The reciprocal of 10 is 1/10.",
                 "What is the length of each piece if the ribbon is cut into 100 equal pieces?",
                 "What is 0.039 m in centimetres and millimetres?"],
       teach=["Predict first: is each of the 10 pieces longer or shorter than half a metre?",
              "Write 3.9 as 39/10, then dividing by 10 means multiplying by 1/10.",
              "1 m is 100 cm and 1 cm is 10 mm, so metres become centimetres by multiplying by 100."],
       examples=[
           WE("Anuja cuts a 3.9 m ribbon into 10 equal pieces, then another such ribbon into 100 equal pieces. Find "
              "the length of each piece, and write 0.039 m in centimetres and millimetres.",
              ["3.9 = 39/10, so 3.9 ÷ 10 = 39/10 × 1/10 = 39/100 = 0.39.",
               "Each of the 10 pieces is 0.39 m.",
               "3.9 ÷ 100 = 39/10 × 1/100 = 39/1000 = 0.039, so each of the 100 pieces is 0.039 m.",
               "0.039 × 100 = 3.9, so 0.039 m is 3.9 cm.",
               "3.9 × 10 = 39, so 3.9 cm is 39 mm."],
              "0.39 m and 0.039 m; 0.039 m is 3.9 cm, which is 39 mm", ncert=["4.3.ex6", "4.3.ribbon_units"])],
       key_terms=["reciprocal"], misconceptions=["M_POINT_WRONG_WAY", "M_UNIT_MIX"], minutes=10),
     A("T6.C2", "The rule: move the point left", "Apply",
       "Students state the rule for dividing a decimal by 10, 100, 1000 and 10000, move the point left by the "
       "right number of places, and use it to complete a table.",
       textbook=["By looking at these divisions, we can frame a simple rule for dividing decimals by 1, 10, 100, "
                 "1000, and so on.",
                 "When we divide a decimal by 1, 10, 100, 1000, and so on, we can just move the decimal point to the "
                 "left by as many places as there are zeroes in the divisor!",
                 "Decimal ÷ 10 ÷ 100 ÷ 1000 ÷ 10000: 18.7, 1.87, 0.187, 0.0187, 0.00187; then 21.1, 0.13, 214.6, 58."],
       teach=["Predict first: how many zeroes come straight after the point in 0.13 ÷ 100?",
              "Count the zeroes in the divisor and move the point that many places left.",
              "Each place to the left makes every digit one tenth as big."],
       examples=[
           WE("Complete the table: divide 21.1, 0.13, 214.6 and 58 by 10, 100, 1000 and 10000.",
              ["21.1 ÷ 10 = 2.11, 21.1 ÷ 100 = 0.211, 21.1 ÷ 1000 = 0.0211, 21.1 ÷ 10000 = 0.00211.",
               "0.13 ÷ 10 = 0.013, 0.13 ÷ 100 = 0.0013, 0.13 ÷ 1000 = 0.00013, 0.13 ÷ 10000 = 0.000013.",
               "214.6 ÷ 10 = 21.46, 214.6 ÷ 100 = 2.146, 214.6 ÷ 1000 = 0.2146, 214.6 ÷ 10000 = 0.02146.",
               "58 ÷ 10 = 5.8, 58 ÷ 100 = 0.58, 58 ÷ 1000 = 0.058, 58 ÷ 10000 = 0.0058."],
              "21.1: 2.11, 0.211, 0.0211, 0.00211; 0.13: 0.013, 0.0013, 0.00013, 0.000013; 214.6: 21.46, 2.146, "
              "0.2146, 0.02146; 58: 5.8, 0.58, 0.058, 0.0058", ncert=["4.3.div_rule", "4.3.div_table"])],
       key_terms=["divisor"], misconceptions=["M_POINT_WRONG_WAY", "M_MISSING_ZERO"], minutes=10),
     DOER("T6.C3", "Practice: divide by 10, 100 and 1000", "point_shifter", "Apply",
          "Students divide decimals by 10, 100, 1000 and 10000 by moving the decimal point and convert lengths "
          "between metres, centimetres and millimetres.",
          ["Count the zeroes in the divisor.",
           "Move the decimal point left by that many places.",
           "Write zeroes in front of the digits when there are not enough places."])]))

# ============================== T7 Sharing into decimal parts ==================================================
TOPICS.append(TOPIC(
    "T7", "M2", "Sharing into Decimal Parts", ["4.3"], "Apply",
    "Students divide one counting number by another to get a decimal quotient by writing the division as a fraction "
    "and finding an equivalent fraction with denominator 10, 100 or 1000, and recognise when no such equivalent "
    "fraction exists.",
    "A quotient is a fraction; if its denominator can be grown into 10, 100 or 1000, the decimal can be read off at "
    "once.",
    [A("T7.C1", "Sharing a ribbon between 2 and among 4", "Apply",
       "Students share 29 m of ribbon between 2 and among 4 people by writing the share as a fraction and finding "
       "an equivalent fraction with denominator 10 or 100.",
       textbook=["Example 7: Neenu has 29 metres of red ribbon and wants to share it equally with Anu. What is the "
                 "length of ribbon that each of them will get?",
                 "If each of them gets 14 m, then 1 m remains. If we divide 1 m among the two, each will get another "
                 "1/2 m.",
                 "It is easy to express a fraction as a decimal if the denominator is 1, 10, 100, 1000, etc.",
                 "Now, what if the ribbon was shared between four friends instead of 2?",
                 "Is 4 a factor of 10? No. Is it a factor of 100? Yes. 4 × 25 = 100. So we can get an equivalent "
                 "fraction of 29/4 by multiplying the numerator and denominator by 25."],
       teach=["Predict first: does each of the 4 friends get more than 7 m?",
              "Write the share as a fraction, then multiply the numerator and the denominator by the same number to "
              "reach 10, 100 or 1000.",
              "Ask which of 10, 100 or 1000 the denominator divides."],
       examples=[
           WE("Neenu shares 29 m of ribbon equally with Anu. How much does each get?",
              ["Each gets 29 ÷ 2 m. If each gets 14 m, 1 m remains, which gives each another 1/2 m.",
               "1/2 = (1 × 5)/(2 × 5) = 5/10 = 0.5.",
               "So each gets 14 + 0.5 = 14.5 m."],
              "14.5 m", ncert=["4.3.ex7"]),
           WE("The same 29 m ribbon is shared equally among 4 friends. How much does each get?",
              ["Each gets 29/4 m.", "4 is not a factor of 10, but 4 × 25 = 100.",
               "29/4 = (29 × 25)/(4 × 25) = 725/100 = 7.25."],
              "7.25 m", ncert=["4.3.ex7_four"])],
       key_terms=["equivalent fraction"], misconceptions=["M_REMAINDER_STOP"], minutes=10),
     A("T7.C2", "When the denominator will not grow into 10, 100 or 1000", "Analyze",
       "Students explain why 10/3 has no equivalent fraction with denominator 10, 100 or 1000, and why powers of 2 "
       "and 5 always give decimals that end.",
       textbook=["Division Using Place Value",
                 "We have seen how to divide two counting numbers to get a decimal quotient. We first represented the "
                 "division as a fraction. Then we found an equivalent fraction, with the denominator being of the form "
                 "1, 10, 100, 1000, and so on.",
                 "Suppose we want to write the quotient 10/3 as a decimal. Can we convert this fraction to an "
                 "equivalent fraction with a denominator such as 1, 10, 100, 1000, etc.?",
                 "It is not possible. So, we need a more general method to divide any two counting numbers.",
                 "1/2 = 0.5, 1/(2 × 2) = 0.25, 1/(2 × 2 × 2) = 0.125, 1/(2 × 2 × 2 × 2) = 0.0625, "
                 "1/(2 × 2 × 2 × 2 × 2) = ?",
                 "1/5 = 0.2, 1/(5 × 5) = 0.04, 1/(5 × 5 × 5) = 0.008, 1/(5 × 5 × 5 × 5) = 0.0016, "
                 "1/(5 × 5 × 5 × 5 × 5) = ?",
                 "What pattern do you observe? Why are 2 and 5 related in this way?"],
       teach=["Predict first: can 3 ever divide 10, 100 or 1000 exactly?",
              "10 = 2 × 5, so 100 and 1000 are made only of 2s and 5s; a denominator made of 2s and 5s can always "
              "be grown into one of them.",
              "3 is not made of 2s and 5s, so 10/3 needs a different method: long division."],
       examples=[
           WE("Can 10/3 be written with denominator 10, 100 or 1000? Find 1/(2 × 2 × 2 × 2 × 2) and "
              "1/(5 × 5 × 5 × 5 × 5) as decimals, and say why 2 and 5 behave this way.",
              ["10, 100 and 1000 are 2 × 5, 4 × 25 and 8 × 125; none of them is a multiple of 3, so 10/3 has no "
               "such equivalent fraction.",
               "2 × 2 × 2 × 2 × 2 = 32 and 32 × 3125 = 100000, so 1/32 = 3125/100000 = 0.03125.",
               "5 × 5 × 5 × 5 × 5 = 3125 and 3125 × 32 = 100000, so 1/3125 = 32/100000 = 0.00032.",
               "Each 10 is one 2 times one 5, so the 2s and the 5s pair up to make 100000."],
              "No for 10/3; 0.03125 and 0.00032, because 2 × 5 = 10", ncert=["4.3.ten_thirds", "4.3.two_five"])],
       key_terms=["denominator"], misconceptions=["M_EVERY_DIVISION_ENDS"], minutes=10),
     DOER("T7.C3", "Practice: fractions as decimals", None, "Apply",
          "Students write fractions as decimals by finding an equivalent fraction with denominator 10, 100 or 1000.",
          ["Ask which of 10, 100 or 1000 the denominator divides.",
           "Multiply the numerator and the denominator by the same number.",
           "Read off the decimal from the new denominator."],
          items=[
              FIO("4.3.FiOB1", "Figure it Out (decimal divisors), Q1",
                  "Express the following fractions in decimal form: (a) 2/5 (b) 13/4 (c) 4/50 (d) 5/8",
                  ["(a) 2/5 = (2 × 2)/(5 × 2) = 4/10 = 0.4.",
                   "(b) 13/4 = (13 × 25)/(4 × 25) = 325/100 = 3.25.",
                   "(c) 4/50 = (4 × 2)/(50 × 2) = 8/100 = 0.08.",
                   "(d) 5/8 = (5 × 125)/(8 × 125) = 625/1000 = 0.625."],
                  "(a) 0.4 (b) 3.25 (c) 0.08 (d) 0.625"),
          ])]))

# ============================== T8 Long division past the Ones =================================================
TOPICS.append(TOPIC(
    "T8", "M2", "Long Division Past the Ones", ["4.3"], "Apply",
    "Students divide by place value, regrouping Ones into Tenths, Tenths into Hundredths and so on, place the "
    "decimal point in the quotient when Ones are regrouped into Tenths, and divide a decimal dividend by a counting "
    "number.",
    "Long division need not stop at the Ones: regroup what is left into Tenths, Hundredths and Thousandths, and put "
    "the decimal point in the quotient at that moment.",
    [A("T8.C1", "1324 ÷ 4 and 1325 ÷ 4", "Apply",
       "Students divide 1324 by 4 by long division, then divide 1325 by 4 and regroup the leftover Ones into Tenths "
       "and Hundredths, and verify with an equivalent fraction.",
       textbook=["Example 8: Find the value of 1324 ÷ 4.",
                 "1 Thousand ÷ 4: Not possible without regrouping. Regroup 1 Thousand into 10 Hundreds.",
                 "So, 1324 ÷ 4 gives 0 Thousands, 3 Hundreds, 3 Tens and 1 Ones, that is 331.",
                 "We also call this division using place values as 'long division'.",
                 "Division with a Decimal Quotient",
                 "We are left with 1 Ones. It is not clear how to divide 1 Ones into 4 equal parts. But we can regroup "
                 "this as 10 tenths.",
                 "To divide 2 Tenths into 4 equal parts, we have to regroup them as 20 Hundredths.",
                 "Thus, the procedure of division using place value can be extended to find quotients with decimal "
                 "values. Ones can be regrouped as tenths, tenths can be regrouped as hundredths and so on."],
       teach=["Predict first: 1324 ÷ 4 = 331. Is 1325 ÷ 4 a little more, or does it have a remainder?",
              "When Ones are left, regroup each One into 10 Tenths and keep sharing.",
              "Put the decimal point in the quotient when Ones become Tenths."],
       examples=[
           WE("Find 1324 ÷ 4 by place value.",
              ["1 Thousand cannot be shared into 4 parts; regroup it as 10 Hundreds, making 13 Hundreds.",
               "13 Hundreds ÷ 4: each part gets 3 Hundreds and 1 Hundred remains.",
               "1 Hundred is 10 Tens; with 2 Tens that makes 12 Tens, and 12 Tens ÷ 4 gives 3 Tens.",
               "4 Ones ÷ 4 gives 1 One.", "So 1324 ÷ 4 = 331."],
              "331", ncert=["4.3.ex8"]),
           WE("Find 1325 ÷ 4 by place value, and verify with an equivalent fraction.",
              ["As before, each part gets 3 Hundreds and 3 Tens; 5 Ones ÷ 4 gives 1 One, and 1 One remains.",
               "Regroup 1 One as 10 Tenths. Put the decimal point in the quotient. 10 Tenths ÷ 4 gives 2 Tenths, "
               "and 2 Tenths remain.",
               "Regroup 2 Tenths as 20 Hundredths. 20 Hundredths ÷ 4 gives 5 Hundredths.",
               "So 1325 ÷ 4 = 331.25.",
               "Check: 1325/4 = (1325 × 25)/(4 × 25) = 33125/100 = 331.25."],
              "331.25", ncert=["4.3.ex8_1325"])],
       key_terms=["regroup", "long division"], misconceptions=["M_REMAINDER_STOP", "M_POINT_IN_QUOTIENT"],
       minutes=12),
     A("T8.C2", "237 ÷ 8: regrouping down to Thousandths", "Apply",
       "Students divide 237 by 8, regrouping Ones into Tenths, Tenths into Hundredths and Hundredths into "
       "Thousandths, and place the decimal point in the quotient.",
       textbook=["Example 9: Find the value of 237 ÷ 8.",
                 "To divide 5 Ones into 8 equal parts we need to regroup them as 50 Tenths. When we regroup Ones into "
                 "Tenths, we place a decimal point in the quotient.",
                 "Remember, when we regroup Ones into Tenths we need to place a decimal point in the quotient.",
                 "To divide 4 Hundredths into 8 equal parts we need to regroup them as 40 Thousandths.",
                 "Thus, 237 ÷ 8 = 29.625."],
       teach=["Predict first: is 237 ÷ 8 nearer 29 or 30?",
              "Keep regrouping until nothing is left.",
              "The quotient point goes in when 5 Ones become 50 Tenths."],
       examples=[
           WE("Find 237 ÷ 8 by long division.",
              ["2 Hundreds are 20 Tens; with 3 Tens that makes 23 Tens. 23 Tens ÷ 8 gives 2 Tens, and 7 Tens remain.",
               "7 Tens are 70 Ones; with 7 Ones that makes 77 Ones. 77 Ones ÷ 8 gives 9 Ones, and 5 Ones remain.",
               "Regroup 5 Ones as 50 Tenths and place the decimal point. 50 Tenths ÷ 8 gives 6 Tenths, and 2 Tenths "
               "remain.",
               "20 Hundredths ÷ 8 gives 2 Hundredths, and 4 Hundredths remain.",
               "40 Thousandths ÷ 8 gives 5 Thousandths.", "So 237 ÷ 8 = 29.625."],
              "29.625", ncert=["4.3.ex9"])],
       key_terms=["thousandth"], misconceptions=["M_POINT_IN_QUOTIENT"], minutes=10),
     A("T8.C3", "Dividing a decimal by a counting number", "Apply",
       "Students divide a decimal dividend by a counting number by long division, placing the decimal point before "
       "dividing the Tenths and keeping zero place holders.",
       textbook=["Division with a Decimal Dividend",
                 "Example 10: A shopkeeper has 9.5 kg of sugar and he wants to pack it equally in 4 bags. What is the "
                 "weight of each bag of sugar?",
                 "Again, we place the decimal point in the quotient before we divide the tenths. Each bag of sugar "
                 "weighs 2.375 kg.",
                 "Example 11: What is the value of 0.06 ÷ 5?",
                 "When we move from Ones to Tenths we need to place the decimal point in the quotient.",
                 "So, the quotient is 0.012."],
       teach=["Predict first: is 0.06 ÷ 5 bigger or smaller than 0.01?",
              "Divide place by place from the left; the decimal point in the quotient sits right above the point in "
              "the dividend.",
              "A place that gives 0 still needs its 0 in the quotient."],
       examples=[
           WE("A shopkeeper packs 9.5 kg of sugar equally into 4 bags. How much is in each bag?",
              ["9 Ones ÷ 4 gives 2 Ones, and 1 One remains.",
               "Place the decimal point. 1 One and 5 Tenths make 15 Tenths; 15 Tenths ÷ 4 gives 3 Tenths, and 3 "
               "Tenths remain.",
               "30 Hundredths ÷ 4 gives 7 Hundredths, and 2 Hundredths remain.",
               "20 Thousandths ÷ 4 gives 5 Thousandths.", "So 9.5 ÷ 4 = 2.375."],
              "2.375 kg", ncert=["4.3.ex10"]),
           WE("Find 0.06 ÷ 5.",
              ["0.06 is 0 Ones, 0 Tenths and 6 Hundredths.",
               "0 Ones ÷ 5 gives 0 Ones; place the decimal point. 0 Tenths ÷ 5 gives 0 Tenths.",
               "6 Hundredths ÷ 5 gives 1 Hundredth, and 1 Hundredth remains.",
               "1 Hundredth is 10 Thousandths, and 10 Thousandths ÷ 5 gives 2 Thousandths.",
               "So 0.06 ÷ 5 = 0.012."],
              "0.012", ncert=["4.3.ex11"])],
       key_terms=["dividend"], misconceptions=["M_MISSING_ZERO", "M_POINT_IN_QUOTIENT"], minutes=10),
     DOER("T8.C4", "Practice: long division with decimals", "regrouping_tray", "Apply",
          "Students divide counting numbers and decimals by a counting number using equivalent fractions and long "
          "division, and choose the correct quotient from options.",
          ["Regroup Ones into Tenths, Tenths into Hundredths, and so on, until nothing is left.",
           "Place the decimal point in the quotient when Ones are regrouped into Tenths.",
           "Check with an equivalent fraction whose denominator is 10, 100 or 1000."],
          items=[
              FIO("4.3.FiOA1", "Figure it Out (decimal division), Q1",
                  "Find the quotient by converting the denominator into 1, 10, 100 or 1000 and verify the solution by "
                  "the long division method (division by place value). (a) 18/5 (b) 415/4 (c) 1217/2 (d) 4827/8",
                  ["(a) 18/5 = (18 × 2)/(5 × 2) = 36/10 = 3.6.",
                   "(b) 415/4 = (415 × 25)/(4 × 25) = 10375/100 = 103.75.",
                   "(c) 1217/2 = (1217 × 5)/(2 × 5) = 6085/10 = 608.5.",
                   "(d) 4827/8 = (4827 × 125)/(8 × 125) = 603375/1000 = 603.375.",
                   "Long division gives the same quotients, regrouping Ones into Tenths and placing the point there."],
                  "(a) 3.6 (b) 103.75 (c) 608.5 (d) 603.375", tool="regrouping_tray"),
              FIO("4.3.FiOA2", "Figure it Out (decimal division), Q2",
                  "Choose the correct answer: (a) 1526/4 = (i) 38.15 (ii) 380.15 (iii) 381.5 (iv) 381.05 "
                  "(b) 3567/8 = (i) 4458.75 (ii) 44.5875 (iii) 445.875 (iv) 4458.75",
                  ["(a) 1526/4 = (1526 × 25)/(4 × 25) = 38150/100 = 381.5, option (iii).",
                   "(b) 3567/8 = (3567 × 125)/(8 × 125) = 445875/1000 = 445.875, option (iii).",
                   "Size check: 1526 ÷ 4 is a little less than 400 and 3567 ÷ 8 is a little less than 450.",
                   "In (b), options (i) and (iv) are printed the same, 4458.75, and that number is ten times too big; "
                   "only (iii) is right."],
                  "(a) (iii) 381.5 (b) (iii) 445.875"),
              FIO("4.3.FiOA3", "Figure it Out (decimal division), Q3",
                  "What is the quotient? (a) 132 ÷ 4 (b) 13.2 ÷ 4 (c) 1.32 ÷ 4 (d) 0.132 ÷ 4",
                  ["(a) 132 ÷ 4 = 33.",
                   "(b) 13.2 is 132 ÷ 10, so 13.2 ÷ 4 = 33 ÷ 10 = 3.3.",
                   "(c) 1.32 ÷ 4 = 33 ÷ 100 = 0.33.", "(d) 0.132 ÷ 4 = 33 ÷ 1000 = 0.033."],
                  "(a) 33 (b) 3.3 (c) 0.33 (d) 0.033"),
              FIO("4.3.FiOA4", "Figure it Out (decimal division), Q4",
                  "What is the quotient? (a) 126 ÷ 8 (b) 12.6 ÷ 8 (c) 1.26 ÷ 8 (d) 0.126 ÷ 8 (e) 0.0126 ÷ 8",
                  ["(a) 126 ÷ 8: 15 Ones and 6 Ones remain; 60 Tenths ÷ 8 gives 7 Tenths and 4 Tenths remain; 40 "
                   "Hundredths ÷ 8 gives 5 Hundredths. So 126 ÷ 8 = 15.75.",
                   "(b) 12.6 ÷ 8 = 15.75 ÷ 10 = 1.575.", "(c) 1.26 ÷ 8 = 15.75 ÷ 100 = 0.1575.",
                   "(d) 0.126 ÷ 8 = 15.75 ÷ 1000 = 0.01575.", "(e) 0.0126 ÷ 8 = 15.75 ÷ 10000 = 0.001575."],
                  "(a) 15.75 (b) 1.575 (c) 0.1575 (d) 0.01575 (e) 0.001575"),
          ])]))

# ============================== T9 Dividing by a decimal =======================================================
TOPICS.append(TOPIC(
    "T9", "M2", "Dividing by a Decimal", ["4.3"], "Apply",
    "Students divide by a decimal by multiplying the dividend and the divisor by the same 10, 100 or 1000 so that "
    "the divisor becomes a counting number, then divide by long division, and use a given product to find related "
    "products and quotients.",
    "Multiplying the dividend and the divisor by the same number does not change the quotient, so a decimal divisor "
    "can be made a counting number first.",
    [A("T9.C1", "Average speed: 126 ÷ 2.5", "Apply",
       "Students find an average speed by dividing a distance by a decimal time, writing the divisor as a fraction "
       "and multiplying by its reciprocal.",
       textbook=["Division with a Decimal Divisor",
                 "Example 12: Ravi went from Pune to Matheran by scooter in 2.5 hours. The distance was 126 km. What "
                 "was his average speed?",
                 "We can get the average speed by dividing the distance by the time taken.",
                 "When the divisor is a decimal, we convert the divisor into a fraction.",
                 "So, the average speed at which Ravi travelled was 50.4 km per hour."],
       teach=["Predict first: Ravi rides 126 km in 2.5 hours. Is his speed more or less than 60 km per hour?",
              "2.5 = 25/10, and dividing by 25/10 is multiplying by 10/25.",
              "Then divide the counting numbers by long division."],
       examples=[
           WE("Ravi rides 126 km from Pune to Matheran in 2.5 hours. What is his average speed?",
              ["Average speed = distance ÷ time = 126 ÷ 2.5.",
               "126 ÷ (25/10) = 126 × (10/25) = 1260/25.",
               "Long division: 1260 ÷ 25 gives 50 with 10 Ones left; 100 Tenths ÷ 25 gives 4 Tenths. So 1260 ÷ 25 = "
               "50.4.",
               "His average speed is 50.4 km per hour."],
              "50.4 km per hour", ncert=["4.3.ex12"])],
       key_terms=["average speed"], misconceptions=["M_QUOTIENT_SMALLER"], minutes=10),
     A("T9.C2", "Make the divisor a counting number", "Apply",
       "Students find 4.68 ÷ 1.3 and 4.68 ÷ 0.13 by multiplying the dividend and the divisor by 10 or 100, and state "
       "the rule.",
       textbook=["Example 13: Find 4.68 ÷ 1.3.",
                 "Now, what about 4.68 ÷ 0.13?",
                 "What do you notice in these cases?",
                 "When the divisor is a decimal, we can convert it into a counting number by suitably multiplying it "
                 "by 10, 100, 1000, and so on. We must also multiply the dividend by the same number.",
                 "Once we convert the divisor into a counting number, we can then follow the division using place "
                 "value procedure to find the quotient."],
       teach=["Predict first: is 4.68 ÷ 0.13 ten times 4.68 ÷ 1.3, or one tenth of it?",
              "Multiply both numbers by the same 10 or 100 until the divisor has no decimal places.",
              "Multiplying only the divisor changes the answer."],
       examples=[
           WE("Find 4.68 ÷ 1.3 and 4.68 ÷ 0.13.",
              ["4.68 ÷ 1.3 = (4.68 × 10)/(1.3 × 10) = 46.8/13.",
               "Long division: 46 Ones ÷ 13 gives 3 Ones and 7 Ones remain; 78 Tenths ÷ 13 gives 6 Tenths. So "
               "46.8 ÷ 13 = 3.6.",
               "4.68 ÷ 0.13 = (4.68 × 100)/(0.13 × 100) = 468/13 = 36.",
               "The divisor became a counting number because both numbers were multiplied by the same 10 or 100."],
              "3.6 and 36", ncert=["4.3.ex13", "4.3.ex13_b"])],
       key_terms=["divisor"], misconceptions=["M_DIVISOR_ONLY"], minutes=10),
     DOER("T9.C3", "Practice: divide by a decimal", "divisor_clearer", "Apply",
          "Students divide by decimals, use a given product to find related products and quotients, and fill in "
          "missing divisors and multipliers.",
          ["Multiply the dividend and the divisor by the same 10, 100 or 1000.",
           "Stop when the divisor is a counting number, then use long division.",
           "Dividing by 0.1 is the same as multiplying by 10."],
          items=[
              FIO("4.3.FiOB2", "Figure it Out (decimal divisors), Q2",
                  "Find the quotients: (a) 24.86 ÷ 1.2 (b) 5.728 ÷ 1.52",
                  ["(a) 24.86 ÷ 1.2 = 248.6 ÷ 12. Long division: 20 Ones and 8 Ones remain, then 86 Tenths ÷ 12 gives "
                   "7, then 2 Tenths remain, 20 Hundredths ÷ 12 gives 1 and 8 remain, and the remainder 8 then repeats.",
                   "So 24.86 ÷ 1.2 = 20.71666..., which is 1243/60.",
                   "(b) 5.728 ÷ 1.52 = 572.8 ÷ 152. Long division gives 3.768421..., which is 358/95; it does not "
                   "end."],
                  "(a) 20.71666... (b) 3.768421..."),
              FIO("4.3.FiOB3", "Figure it Out (decimal divisors), Q3",
                  "Evaluate the following using the information 156 × 12 = 1872. (a) 15.6 × 1.2 (b) 187.2 ÷ 1.2 "
                  "(c) 18.72 ÷ 15.6 (d) 0.156 × 0.12",
                  ["(a) 1 + 1 = 2 decimal places: 15.6 × 1.2 = 18.72.",
                   "(b) 187.2 ÷ 1.2 = 1872 ÷ 12 = 156.",
                   "(c) 18.72 ÷ 15.6 = 187.2 ÷ 156 = 1.2.",
                   "(d) 3 + 2 = 5 decimal places: 0.156 × 0.12 = 0.01872."],
                  "(a) 18.72 (b) 156 (c) 1.2 (d) 0.01872", tool="divisor_clearer"),
              FIO("4.3.FiOB4", "Figure it Out (decimal divisors), Q4",
                  "Evaluate the following: (a) 25 ÷ ___ = 0.025 (b) 25 ÷ ___ = 250 (c) 25 ÷ ___ = 2.5 "
                  "(d) 25 ÷ 10 = 25 × ___ (e) 25 ÷ 0.10 = 25 × ___ (f) 25 ÷ 0.01 = 25 × ___",
                  ["(a) The point moves 3 places left, so 25 ÷ 1000 = 0.025.",
                   "(b) 25 ÷ 0.1 = 25 × 10 = 250.", "(c) 25 ÷ 10 = 2.5.",
                   "(d) Dividing by 10 is multiplying by 0.1: 25 ÷ 10 = 25 × 0.1.",
                   "(e) 0.10 = 1/10, so 25 ÷ 0.10 = 25 × 10.",
                   "(f) 0.01 = 1/100, so 25 ÷ 0.01 = 25 × 100."],
                  "(a) 1000 (b) 0.1 (c) 10 (d) 0.1 (e) 10 (f) 100"),
              FIO("4.3.FiOB5", "Figure it Out (decimal divisors), Q5",
                  "Find the quotient: (a) 2.46 ÷ 1.5 (b) 2.46 ÷ 0.15 (c) 2.46 ÷ 0.015. Is the quotient obtained in "
                  "24.6 ÷ 1.5 the same as the quotient obtained in 2.46 ÷ 0.15?",
                  ["(a) 2.46 ÷ 1.5 = 24.6 ÷ 15 = 1.64.", "(b) 2.46 ÷ 0.15 = 246 ÷ 15 = 16.4.",
                   "(c) 2.46 ÷ 0.015 = 2460 ÷ 15 = 164.",
                   "24.6 ÷ 1.5 = 246 ÷ 15 = 16.4, the same as 2.46 ÷ 0.15, because both become 246 ÷ 15."],
                  "(a) 1.64 (b) 16.4 (c) 164; yes, both are 16.4"),
          ])]))

# ============================== T10 Does this ever end =========================================================
TOPICS.append(TOPIC(
    "T10", "M2", "Does This Ever End?", ["4.3"], "Analyze",
    "Students carry out long divisions that never end, notice that a remainder repeats so the quotient digits repeat "
    "in a cycle, explore the cyclic number 142857 from 1 ÷ 7, and meet an open question about cyclic numbers.",
    "Every remainder is smaller than the divisor, so a remainder must come back; from then on the same digits repeat "
    "for ever.",
    [A("T10.C1", "10 ÷ 3: the remainder that keeps coming back", "Analyze",
       "Students divide 10 by 3 by long division, notice the remainder 1 at every step, and find 10 ÷ 9 and "
       "100 ÷ 11.",
       textbook=["Does This Ever End?",
                 "Can you calculate 10 ÷ 3? Try dividing using long division.",
                 "This never seems to end! Each time we divide by 3, there is a remainder of 1.",
                 "Will this process end?",
                 "In long division, we see that at each step we get a remainder of 1. So, the process will never end!",
                 "So, 10 ÷ 3 cannot be expressed using a finite number of digits in the decimal form.",
                 "There are decimal divisions where the quotient never ends! We will explore such numbers in greater "
                 "detail in a later class.",
                 "Can you find the quotients of 10 ÷ 9, and 100 ÷ 11?"],
       teach=["Predict first: will 10 ÷ 3 end after a few decimal places?",
              "Watch the remainder: if the same remainder comes back, the same step happens again.",
              "A quotient that never ends is written with dots, such as 3.333..."],
       examples=[
           WE("Find 10 ÷ 3 by long division. Will it end?",
              ["10 Ones ÷ 3 gives 3 Ones, and 1 One remains.",
               "1 One is 10 Tenths; 10 Tenths ÷ 3 gives 3 Tenths, and 1 Tenth remains.",
               "1 Tenth is 10 Hundredths; 10 Hundredths ÷ 3 gives 3 Hundredths, and 1 Hundredth remains.",
               "The remainder is 1 at every step, so the process never ends: 10 ÷ 3 = 3.333..."],
              "3.333..., it never ends", ncert=["4.3.never_10_3"]),
           WE("Find 10 ÷ 9 and 100 ÷ 11.",
              ["10 ÷ 9: 1 One, and 1 One remains; then 10 Tenths ÷ 9 gives 1 Tenth with 1 left, again and again.",
               "So 10 ÷ 9 = 1.111...",
               "100 ÷ 11: 9 Ones, and 1 One remains; 10 Tenths ÷ 11 gives 0 Tenths; 100 Hundredths ÷ 11 gives 9 "
               "Hundredths with 1 left, and the steps repeat.",
               "So 100 ÷ 11 = 9.0909..."],
              "1.111... and 9.0909...", ncert=["4.3.never_more"])],
       key_terms=["remainder"], misconceptions=["M_EVERY_DIVISION_ENDS"], minutes=10),
     A("T10.C2", "1 ÷ 7: a chain of remainders", "Analyze",
       "Students divide 1 by 7, list the remainders 1, 3, 2, 6, 4, 5 as a chain, and explain why the remainders and "
       "the quotient digits repeat in a cycle.",
       textbook=["Now divide 1 by 7 (1 ÷ 7). Will this end?",
                 "Note all the remainders we get. It starts with 1, then 3, then 2, then 6, and so on. Let us represent "
                 "this as a chain.",
                 "What do you observe? Can you explain why this division never ends?",
                 "Not only do the remainders repeat in a cycle, the digits of the quotient also repeat in a cycle! "
                 "0.142857 142857 14…"],
       teach=["Predict first: dividing by 7, how many different remainders other than 0 are possible?",
              "The only possible remainders are 1 to 6; if 0 never appears, one of them must come back within 6 steps.",
              "When remainder 1 comes back, the digits 142857 start again."],
       examples=[
           WE("Find 1 ÷ 7 by long division, listing every remainder.",
              ["10 Tenths ÷ 7 gives 1, remainder 3.", "30 Hundredths ÷ 7 gives 4, remainder 2.",
               "20 ÷ 7 gives 2, remainder 6; 60 ÷ 7 gives 8, remainder 4; 40 ÷ 7 gives 5, remainder 5.",
               "50 ÷ 7 gives 7, remainder 1, and remainder 1 is where we started.",
               "The remainders run 1, 3, 2, 6, 4, 5 and repeat, so 1 ÷ 7 = 0.142857142857..."],
              "0.142857142857..., the block 142857 repeats for ever", ncert=["4.3.one_seventh"])],
       key_terms=["cycle"], misconceptions=["M_EVERY_DIVISION_ENDS"], minutes=10),
     A("T10.C3", "The magic number 142857", "Analyze",
       "Students multiply 142857 by 1 to 7, notice the digits cycle round until 142857 × 7 = 999999, and recognise that "
       "1 ÷ 17 gives another cyclic number and that Artin's question is still open.",
       textbook=["A Magic Number: 142857",
                 "Let us consider the number 142857 that arose when dividing 1 by 7. Multiply 142857 by numbers from 1 "
                 "to 6.",
                 "What are the products? What do you notice?",
                 "You get the same number back, but with the digits cycled around!",
                 "Multiply 142857 by 7. What do you observe?",
                 "Are there other such numbers? Yes! To find one such number, you can find 1 ÷ 17 in decimal, and use "
                 "the repeating block of digits.",
                 "Are there infinitely many such 'cyclic' numbers? In 1927, the Austrian mathematician Emil Artin "
                 "conjectured (guessed) that there must be infinitely many such numbers. However, even today, nearly a "
                 "century later, this conjecture remains unsolved, despite a lot of research on the question by many "
                 "mathematicians!"],
       teach=["Predict first: what will 142857 × 2 look like?",
              "Look for the same six digits in the same circular order.",
              "Some questions in mathematics are still open, and this is one of them."],
       examples=[
           WE("Multiply 142857 by 1, 2, 3, 4, 5, 6 and 7. What do you notice?",
              ["142857 × 1 = 142857, 142857 × 2 = 285714, 142857 × 3 = 428571.",
               "142857 × 4 = 571428, 142857 × 5 = 714285, 142857 × 6 = 857142.",
               "Each product has the same digits in the same circular order, starting at a different digit.",
               "142857 × 7 = 999999."],
              "The digits cycle round for 1 to 6, and 142857 × 7 = 999999", ncert=["4.3.magic"]),
           WE("Find the repeating block of 1 ÷ 17 and check that it behaves like 142857.",
              ["Long division of 1 by 17 gives remainders that run through all of 1 to 16 before 1 returns.",
               "1 ÷ 17 = 0.05882352941176470588..., where the block 0588235294117647 of 16 digits repeats.",
               "0588235294117647 × 2 = 1176470588235294, the same 16 digits cycled round.",
               "Artin guessed in 1927 that there are infinitely many cyclic numbers; nobody has proved it yet."],
              "The block 0588235294117647 is another cyclic number", ncert=["4.3.seventeenth", "4.3.artin"])],
       key_terms=["cyclic number", "conjecture"], misconceptions=[], minutes=10),
     DOER("T10.C4", "Practice: does the division end?", "remainder_cycle_tracker", "Analyze",
          "Students run long divisions step by step, track the remainders, and decide whether each quotient ends or "
          "repeats, naming the repeating block.",
          ["Every remainder is less than the divisor.",
           "If a remainder is 0 the division ends; if a remainder comes back, the digits repeat.",
           "Write a quotient that never ends with dots after the repeating block."])]))

# ============================== T11 Dividend, divisor and quotient =============================================
TOPICS.append(TOPIC(
    "T11", "M2", "Dividend, Divisor and Quotient", ["4.3"], "Analyze",
    "Students compare a quotient with its dividend when the divisor is greater than 1 or between 0 and 1, build a "
    "table of the cases, and solve sharing, perimeter, juice, petrol and flour problems by dividing decimals.",
    "Dividing by a number greater than 1 makes the quotient smaller than the dividend; dividing by a number between "
    "0 and 1 makes it bigger.",
    [A("T11.C1", "Is the quotient always smaller?", "Analyze",
       "Students compare 128 ÷ 4 with 128 ÷ 0.4, test other divisors, and make a table relating the dividend, the "
       "divisor and the quotient.",
       textbook=["Dividend, Divisor, and Quotient",
                 "When we divide two counting numbers, the quotient is always less than the dividend. For example, "
                 "128 ÷ 4 = 32, and 32 (quotient) < 128 (dividend).",
                 "But what happens when we divide 128 by 0.4? 128 ÷ 0.4 = 320. The quotient is greater than the "
                 "dividend.",
                 "Will the quotient be always greater than the dividend when the divisor is a decimal? Try it out with "
                 "different values of the divisor.",
                 "Describe the relationship between the dividend, divisor, and the quotient. Create a table for "
                 "capturing this relationship in different situations, like we did for multiplication."],
       teach=["Predict first: is 128 ÷ 0.4 bigger or smaller than 128?",
              "Dividing asks how many divisors fit into the dividend; many small pieces fit.",
              "A decimal divisor greater than 1, such as 2.5, still gives a smaller quotient."],
       examples=[
           WE("Compare 128 ÷ 4 and 128 ÷ 0.4 with 128.",
              ["128 ÷ 4 = 32, and 32 < 128.",
               "128 ÷ 0.4 = 1280 ÷ 4 = 320, and 320 > 128.",
               "0.4 is less than 1, so more than 128 of them fit into 128."],
              "32 is smaller than 128; 320 is bigger than 128", ncert=["4.3.ddq"]),
           WE("Is the quotient always greater than the dividend when the divisor is a decimal? Test 12.5 ÷ 2.5, "
              "12.5 ÷ 1 and 12.5 ÷ 0.5, and make a table.",
              ["12.5 ÷ 2.5 = 125 ÷ 25 = 5: divisor greater than 1, quotient smaller than the dividend.",
               "12.5 ÷ 1 = 12.5: divisor 1, quotient equal to the dividend.",
               "12.5 ÷ 0.5 = 125 ÷ 5 = 25: divisor between 0 and 1, quotient greater than the dividend.",
               "So no: a decimal divisor greater than 1 still gives a smaller quotient."],
              "No. Divisor greater than 1: quotient smaller; divisor 1: equal; divisor between 0 and 1: quotient "
              "greater", ncert=["4.3.ddq_table"])],
       key_terms=["quotient"], misconceptions=["M_QUOTIENT_SMALLER"], minutes=10),
     DOER("T11.C2", "Practice: dividing decimals in everyday problems", "quotient_size_predictor", "Apply",
          "Students solve cutting, perimeter, sharing, petrol and flour problems by dividing decimals, predicting "
          "the size of each quotient first.",
          ["Decide whether the quotient should be bigger or smaller than the dividend.",
           "Make the divisor a counting number if it is a decimal.",
           "Convert units at the end if the answer is asked in another unit."],
          items=[
              FIO("4.3.FiOB6", "Figure it Out (decimal divisors), Q6",
                  "A 4 m long wooden block has to be cut into 5 pieces of equal length. What is the length of each "
                  "piece?",
                  ["Each piece is 4 ÷ 5 m.", "4/5 = (4 × 2)/(5 × 2) = 8/10 = 0.8."], "0.8 m"),
              FIO("4.3.FiOB7", "Figure it Out (decimal divisors), Q7",
                  "If the perimeter of a regular polygon with 12 sides is 208.8 cm, what is the length of its side?",
                  ["All 12 sides are equal, so one side is 208.8 ÷ 12.",
                   "Long division: 208 Ones ÷ 12 gives 17 and 4 Ones remain; 48 Tenths ÷ 12 gives 4 Tenths.",
                   "So 208.8 ÷ 12 = 17.4."], "17.4 cm"),
              FIO("4.3.FiOB8", "Figure it Out (decimal divisors), Q8",
                  "3 litres of watermelon juice is shared among 8 friends equally. How much watermelon juice will "
                  "each get? Express the quantity of juice in millilitres.",
                  ["Each gets 3 ÷ 8 litres.", "3/8 = (3 × 125)/(8 × 125) = 375/1000 = 0.375.",
                   "1 litre is 1000 ml, so 0.375 × 1000 = 375."], "0.375 litres, that is 375 ml",
                  tool="quotient_size_predictor"),
              FIO("4.3.FiOB9", "Figure it Out (decimal divisors), Q9",
                  "A car covers 234.45 km using 12.6 litres of petrol. What is the distance travelled per litre?",
                  ["Distance per litre = 234.45 ÷ 12.6 = 2344.5 ÷ 126.",
                   "Long division: 2344 ÷ 126 gives 18 and 76 remain; 765 Tenths ÷ 126 gives 6 Tenths and 9 remain; "
                   "90 Hundredths ÷ 126 gives 0; 900 Thousandths ÷ 126 gives 7.",
                   "So 234.45 ÷ 12.6 = 18.607..., which is 521/28, about 18.61."],
                  "About 18.61 km per litre (18.607...)"),
              FIO("4.3.FiOB10", "Figure it Out (decimal divisors), Q10",
                  "13.5 kg of flour (aata) was distributed equally among 15 students. How much flour did each student "
                  "receive?",
                  ["Each gets 13.5 ÷ 15 kg.", "13 Ones ÷ 15 gives 0 Ones; 135 Tenths ÷ 15 gives 9 Tenths.",
                   "So 13.5 ÷ 15 = 0.9."], "0.9 kg"),
          ])]))
