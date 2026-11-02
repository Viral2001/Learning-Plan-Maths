# -*- coding: utf-8 -*-
"""Topics T8 to T10: sharing in a ratio and converting units (M4), and the summary with Binairo (M5).
Book pp 172 to 178."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T8 Sharing in a ratio ======================================================
TOPICS.append(TOPIC(
    "T8", "M4", "Sharing in a Ratio", ["7.5"], "Apply",
    "Students share a whole in a ratio m : n by finding the number of groups m + n and the size of one group, "
    "share a profit by investment, and change a mixture to a new ratio.",
    "To share x in the ratio m : n, make m + n equal groups. One group is x ÷ (m + n). The first part gets m groups "
    "and the second part gets n groups. The two parts are in the ratio m : n.",
    [A("T8.C1", "Sharing counters in groups", "Apply",
       "Students share 12 counters in the ratio 3 : 1 by taking turns, then share 42 counters in the ratio 4 : 3 by "
       "finding the number of groups and the size of each group.",
       textbook=["Form a pair. Collect 12 countable objects or counters (it can be coins, seeds, or pebbles). Now, "
                 "share them between the two of you in different ways.",
                 "If you divide them equally, what is the ratio of the number of counters with each of you? Each of "
                 "you will get 6 counters. So, the ratio is 6 : 6, or 1 : 1 in its simplest form.",
                 "Now let us not share equally. If your partner gets 5 counters, how many objects will you get? What "
                 "is the ratio of the counters? The ratio of the counters of your partner to yours is 5 : 7.",
                 "Now, if you want to share the counters between the two of you in the ratio of 3 : 1, how many "
                 "counters would each of you get?",
                 "So, your partner gets 9 counters in total and you get 3 counters.",
                 "Now, if you want to share 42 counters between the two of you in the ratio of 4 : 3, how will you do "
                 "it? Using the same procedure would take a long time! There is a simpler way to share the whole with "
                 "parts in a specified ratio.",
                 "You need to divide 42 into groups such that your partner gets 4 groups and you get 3 groups.",
                 "If your partner gets 4 groups and you get 3 groups, the total number of groups is 7. So, the size of "
                 "each group is 42 ÷ 7 = 6.",
                 "Multiplying the number of groups by the size of each group, your partner gets 24 counters and you "
                 "get 18 counters, when you share 42 counters in the ratio of 4 : 3."],
       teach=["Predict first: share 12 counters in the ratio 3 : 1. Does your partner get 3 and you get 1?",
              "3 : 1 means 3 for your partner for every 1 for you: take turns 3 and 1 until the counters run out.",
              "A faster way: one round uses 3 + 1 = 4 counters, so 12 makes 12 ÷ 4 = 3 rounds.",
              "For 42 in the ratio 4 : 3, there are 4 + 3 = 7 groups of 42 ÷ 7 = 6."],
       examples=[
           WE("Share 12 counters in the ratio 3 : 1, and then 42 counters in the ratio 4 : 3.",
              ["12 in 3 : 1: one round takes 3 + 1 = 4 counters, and 12 ÷ 4 = 3 rounds.",
               "Partner: 3 × 3 = 9; you: 1 × 3 = 3.",
               "42 in 4 : 3: there are 4 + 3 = 7 groups, each of 42 ÷ 7 = 6.",
               "Partner: 4 × 6 = 24; you: 3 × 6 = 18. Check: 24 + 18 = 42."],
              "12 shared 3 : 1 gives 9 and 3; 42 shared 4 : 3 gives 24 and 18",
              ncert=["7.5.act3", "7.5.share_42"])],
       key_terms=["sharing in a ratio", "group"], misconceptions=["M_SHARE_BY_TERMS"], minutes=8),
     A("T8.C2", "The general rule: sharing a profit", "Apply",
       "Students state the two parts for sharing x in the ratio m : n, and use them to share a profit in the ratio "
       "of the investments.",
       textbook=["In general, when we want to divide a quantity, say x, in the ratio m : n, we do the following:",
                 "We need to split x into groups such that it can be divided into two parts where the first part has m "
                 "groups and the second part has n groups.",
                 "But what is the size of each group? This can be found out by dividing x by the number of groups. "
                 "The number of groups are m + n.",
                 "Thus, if we want to divide a quantity x in the ratio of m : n, then the parts will be m × x/(m + n) "
                 "and n × x/(m + n).",
                 "Prashanti and Bhuvan started a food cart business near their school. Prashanti invested ₹75,000 and "
                 "Bhuvan invested ₹25,000. At the end of the first month, they gained a profit of ₹4,000. They decided "
                 "that they would share the profit in the same ratio as that of their investment. What is each "
                 "person's share of the profit?",
                 "The ratio of their investment is 75000 : 25000. Reducing this ratio to its simplest form, we get "
                 "3 : 1.",
                 "3 + 1 is 4 and dividing the profit of 4000 by 4, we get 1000.",
                 "So, Prashanti would get ₹3,000 and Bhuvan would get ₹1,000 of the profit."],
       teach=["Predict first: Prashanti put in three times as much money as Bhuvan. Should she get three times the "
              "profit?",
              "Sharing x in the ratio m : n makes m + n groups, each of size x ÷ (m + n).",
              "The parts are m × x ÷ (m + n) and n × x ÷ (m + n).",
              "Reduce the ratio first: 75000 : 25000 is 3 : 1."],
       examples=[
           WE("Prashanti invests ₹75000 and Bhuvan ₹25000. They share a profit of ₹4000 in the ratio of their "
              "investments. What does each get?",
              ["Ratio of investments: 75000 : 25000; the HCF is 25000, so it is 3 : 1.",
               "Number of groups: 3 + 1 = 4; each group is 4000 ÷ 4 = 1000.",
               "Prashanti: 3 × 1000 = 3000; Bhuvan: 1 × 1000 = 1000.",
               "Check: 3000 + 1000 = 4000, and 3000 : 1000 is 3 : 1."],
              "Prashanti gets ₹3000 and Bhuvan gets ₹1000",
              ncert=["7.5.general", "7.5.ex11"])],
       key_terms=["sharing in a ratio", "profit"], misconceptions=["M_SHARE_BY_TERMS"], minutes=8),
     A("T8.C2x", "Changing a mixture's ratio", "Analyze",
       "Students find the sand and cement in a 40 kg mixture in the ratio 3 : 1, keep the sand fixed and find how much "
       "cement to add to make the ratio 5 : 2.",
       textbook=["A mixture of 40 kg contains sand and cement in the ratio of 3 : 1. How much cement should be added "
                 "to the mixture to make the ratio of sand to cement 5 : 2?",
                 "The ratio is 3 : 1 and the total weight is 40 kg. So, the weight of sand is 3/(3 + 1) × 40 = 30 kg. "
                 "The weight of cement is 1/(3 + 1) × 40 = 10 kg.",
                 "The weight of sand is the same in the new mixture. It remains 30. But the new ratio of sand to "
                 "cement is 5 : 2. So the question is, 5 : 2 :: 30 : ?",
                 "The new mixture should have 12 kg of cement if the ratio of sand to cement is to be 5 : 2.",
                 "There is 10 kg of cement already. So, we need to add 2 kg of cement to the original mixture."],
       teach=["Predict first: only cement is added. Which amount stays fixed?",
              "Share the 40 kg first, then keep the sand fixed and scale to the new ratio."],
       examples=[
           WE("A 40 kg mixture has sand and cement in the ratio 3 : 1. How much cement must be added to make the "
              "ratio 5 : 2?",
              ["Groups: 3 + 1 = 4, each 40 ÷ 4 = 10 kg; sand is 3 × 10 = 30 kg and cement 10 kg.",
               "Sand stays 30 kg, so 5 : 2 :: 30 : ?",
               "The second term is 2/5 of the first: 2/5 × 30 = 12 kg of cement.",
               "Cement to add: 12 − 10 = 2 kg."],
              "2 kg of cement",
              ncert=["7.5.ex12"])],
       key_terms=["mixture", "ratio"], minutes=5, thin=True),
     DOER("T8.C3", "Practice: share a whole in a ratio", "ratio_sharer", "Apply",
          "Students split a bar into m + n equal groups, give m groups and n groups to the two parts, and solve "
          "sharing problems with money, solutions, paint, food, a crane's body and a coin's metals.",
          ["Add the terms to get the number of groups.",
           "Divide the whole by the number of groups to get one group.",
           "Multiply one group by each term to get the two parts."],
          items=[
              FIO("FiO3.q1", "Figure it Out (ratio sharing, question 1)",
                  "Divide ₹4500 into two parts in the ratio 2 : 3.",
                  ["Groups: 2 + 3 = 5.",
                   "One group: 4500 ÷ 5 = 900.",
                   "Parts: 2 × 900 = 1800 and 3 × 900 = 2700."],
                  "₹1800 and ₹2700"),
              FIO("FiO3.q2", "Figure it Out (ratio sharing, question 2)",
                  "In a science lab, acid and water are mixed in the ratio of 1 : 5 to make a solution. In a bottle "
                  "that has 240 mL of the solution, how much acid and water does the solution contain?",
                  ["Groups: 1 + 5 = 6.",
                   "One group: 240 ÷ 6 = 40 mL.",
                   "Acid: 1 × 40 = 40 mL; water: 5 × 40 = 200 mL."],
                  "40 mL of acid and 200 mL of water"),
              FIO("FiO3.q3", "Figure it Out (ratio sharing, question 3)",
                  "Blue and yellow paints are mixed in the ratio of 3 : 5 to produce green paint. To produce 40 mL of "
                  "green paint, how much of these two colours are needed? To make the paint a lighter shade of green, "
                  "I added 20 mL of yellow to the mixture. What is the new ratio of blue and yellow in the paint?",
                  ["Groups: 3 + 5 = 8; one group: 40 ÷ 8 = 5 mL.",
                   "Blue: 3 × 5 = 15 mL; yellow: 5 × 5 = 25 mL.",
                   "After adding yellow: 25 + 20 = 45 mL of yellow.",
                   "New ratio 15 : 45; the HCF is 15, so it is 1 : 3."],
                  "15 mL of blue and 25 mL of yellow; the new ratio is 1 : 3"),
              FIO("FiO3.q4", "Figure it Out (ratio sharing, question 4)",
                  "To make soft idlis, you need to mix rice and urad dal in the ratio of 2 : 1. If you need 6 cups of "
                  "this mixture to make idlis tomorrow morning, how many cups of rice and urad dal will you need?",
                  ["Groups: 2 + 1 = 3.",
                   "One group: 6 ÷ 3 = 2 cups.",
                   "Rice: 2 × 2 = 4 cups; urad dal: 1 × 2 = 2 cups."],
                  "4 cups of rice and 2 cups of urad dal"),
              FIO("FiO3.q5", "Figure it Out (ratio sharing, question 5)",
                  "I have one bucket of orange paint that I made by mixing red and yellow paints in the ratio of "
                  "3 : 5. I added another bucket of yellow paint to this mixture. What is the ratio of red paint to "
                  "yellow paint in the new mixture?",
                  ["Take both buckets to hold the same amount, and split one bucket into 3 + 5 = 8 equal groups.",
                   "The orange bucket has 3 groups of red and 5 groups of yellow.",
                   "A full bucket of yellow adds 8 more groups of yellow: 5 + 8 = 13.",
                   "Red to yellow is now 3 : 13."],
                  "3 : 13 (taking both buckets to hold the same amount)"),
              FIO("FiO4.q4", "Figure it Out (unit conversions, question 4)",
                  "A crane of height 155 cm has its neck and the rest of its body in the ratio 4 : 6. For your height, "
                  "if your neck and the rest of the body also had this ratio, how tall would your neck be?",
                  ["Groups: 4 + 6 = 10; the neck takes 4 of every 10 parts of the height.",
                   "For the crane: 4 ÷ 10 × 155 = 62 cm of neck.",
                   "For your height, say 150 cm: 4 ÷ 10 × 150 = 60 cm.",
                   "So your neck would be 4/10 of your height."],
                  "4/10 of your height, for example 60 cm for a height of 150 cm (the crane's neck is 62 cm)"),
              FIO("FiO4.q12", "Figure it Out (unit conversions, question 12)",
                  "The ₹10 coin is an alloy of copper and nickel called cupro-nickel. Copper and nickel are mixed in a "
                  "3 : 1 ratio to get this alloy. The mass of the coin is 7.74 grams. If the cost of copper is ₹906 "
                  "per kg and the cost of nickel is ₹1341 per kg, what is the cost of these metals in a ₹10 coin?",
                  ["Groups: 3 + 1 = 4. Copper: 7.74 × 3 ÷ 4 = 5.805 g; nickel: 7.74 ÷ 4 = 1.935 g.",
                   "Same units: 1 kg is 1000 g. Copper cost: 906 × 5.805 ÷ 1000 ≈ 5.26 rupees.",
                   "Nickel cost: 1341 × 1.935 ÷ 1000 ≈ 2.59 rupees.",
                   "Total: 5.26 + 2.59 = 7.85 rupees."],
                  "About ₹7.85 (about ₹5.26 of copper and ₹2.59 of nickel)")])],
    key_terms=["sharing in a ratio", "group"]))

# ============================== T9 Converting units =======================================================
TOPICS.append(TOPIC(
    "T9", "M4", "Converting Units", ["7.6"], "Apply",
    "Students use the conversions for length, area and volume as proportions to change units before solving, and "
    "use the Fahrenheit and Celsius formulas, which are not a simple proportion.",
    "Most unit conversions are proportions: multiply by the number of new units in one old unit. Temperature is "
    "different: Fahrenheit = 9/5 × Celsius + 32, so it is not a simple ratio.",
    [A("T9.C1", "Unit conversions are proportions", "Apply",
       "Students read the reference conversions for length, area and volume and use one as a proportion to convert "
       "hectares to acres.",
       textbook=["We have noticed earlier that solving problems with proportionality often requires us to convert "
                 "units from one system to another. Here are a few important unit conversions for your reference.",
                 "Length: 1 metre = 3.281 feet.",
                 "Area: 1 square metre = 10.764 square feet; 1 acre = 43,560 square feet; 1 hectare = 10,000 square "
                 "metres; 1 hectare = 2.471 acres.",
                 "Volume: 1 millilitre (mL) = 1 cubic centimetre (cc); 1 litre = 1,000 mL or 1,000 cc."],
       teach=["Predict first: a plot is 2 hectares. Is that more or fewer than 2 acres?",
              "Each conversion is a ratio, such as 1 hectare : 2.471 acres.",
              "Converting is the Rule of Three: multiply by the number of new units in one old unit.",
              "Convert first so both quantities in a proportion use the same unit."],
       examples=[
           WE("A field is 2 hectares. How many acres is it? How many square metres?",
              ["1 hectare is 2.471 acres, so 1 : 2.471 :: 2 : x.",
               "2 × 2.471 = 4.942 acres.",
               "1 hectare is 10000 square metres, so 2 × 10000 = 20000 square metres."],
              "4.942 acres, which is 20000 square metres",
              ncert=["7.6.units"])],
       key_terms=["unit conversion", "acre", "hectare"], misconceptions=["M_MIXED_UNITS"], minutes=6),
     A("T9.C2", "Temperature: not a simple ratio", "Apply",
       "Students convert 25 degrees Celsius to Fahrenheit and back with the formulas and explain why the added 32 "
       "makes temperature conversion not proportional.",
       textbook=["Temperature conversion between Fahrenheit and Celsius is a bit more complicated.",
                 "0 °C = 32 °F, and Fahrenheit = 9/5 × Celsius + 32 and Celsius = 5/9 × (Fahrenheit − 32).",
                 "For example, 25 °C is 77 °F."],
       teach=["Predict first: if 0 °C is 32 °F, is 50 °C equal to 64 °F?",
              "The formula multiplies and then adds 32, so doubling Celsius does not double Fahrenheit.",
              "Celsius to Fahrenheit: multiply by 9/5, then add 32.",
              "Fahrenheit to Celsius: subtract 32 first, then multiply by 5/9."],
       examples=[
           WE("Convert 25 °C to Fahrenheit, and convert the answer back to Celsius.",
              ["9/5 × 25 = 45.",
               "45 + 32 = 77, so 25 °C is 77 °F.",
               "Back: 77 − 32 = 45.",
               "5/9 × 45 = 25, so 77 °F is 25 °C."],
              "25 °C is 77 °F",
              ncert=["7.6.temperature"])],
       key_terms=["Celsius", "Fahrenheit"], misconceptions=["M_ALWAYS_PROPORTIONAL"], minutes=6,
       tool="temperature_twin"),
     DOER("T9.C3", "Practice: convert, then reason", "unit_bridge", "Apply",
          "Students convert square feet to acres before using a proportion to find the manure for a plot and the "
          "cost of a piece of land.",
          ["Convert so both ratios use the same unit.",
           "1 acre is 43560 square feet.",
           "Then use the Rule of Three."],
          items=[
              FIO("FiO4.q8", "Figure it Out (unit conversions, question 8)",
                  "It is good farming practice to apply 10 tonnes of cow manure for 1 acre of land. A farmer is "
                  "planning to grow tomatoes in a plot of size 200 ft by 500 ft. How much manure should he buy?",
                  ["Area of the plot: 200 × 500 = 100000 square feet.",
                   "1 acre is 43560 square feet, and 10 tonnes is 10000 kg.",
                   "43560 : 10000 :: 100000 : x, so x = 10000 × 100000 ÷ 43560.",
                   "10000 × 100000 ÷ 43560 ≈ 22956.8."],
                  "About 22956.8 kg of manure (about 23 tonnes)"),
              FIO("FiO4.q10", "Figure it Out (unit conversions, question 10)",
                  "One acre of land costs ₹1500000. What is the cost of 2400 square feet of the same land?",
                  ["1 acre is 43560 square feet.",
                   "43560 : 1500000 :: 2400 : x.",
                   "x = 1500000 × 2400 ÷ 43560",
                   "1500000 × 2400 ÷ 43560 ≈ 82645."],
                  "About ₹82645")])],
    key_terms=["unit conversion", "acre"]))

# ============================== T10 Summary and Binairo ===================================================
TOPICS.append(TOPIC(
    "T10", "M5", "Summary: Proportional Reasoning", ["Summary", "Binairo"], "Remember",
    None,
    "Ratios a : b and their terms, proportion a : b :: c : d with ad = bc, sharing x in the ratio m : n, and the "
    "Binairo puzzle.",
    [A("T10.C1", "What we found about proportion", "Remember",
       "Students restate what a ratio a : b means, when two ratios are proportional (ad = bc), and the parts when x "
       "is shared in the ratio m : n.",
       textbook=["Ratios in the form of a : b indicate that for every 'a' unit of the first quantity, there are 'b' "
                 "units of the second quantity. 'a' and 'b' are the terms in the ratio.",
                 "Two ratios, a : b and c : d, are proportional (written a : b :: c : d) if their terms change by the "
                 "same factor, i.e., if ad = bc.",
                 "If x is divided into two parts in the ratio m : n, then the quantity of the first part is "
                 "m × x/(m + n) and the quantity of the second part is n × x/(m + n)."],
       teach=["The tiger copies have their answer: the good copies changed width and height by the same factor.",
              "A ratio a : b means for every a units of the first quantity there are b units of the second.",
              "a : b :: c : d when both terms change by the same factor, which is when ad = bc.",
              "Sharing x in the ratio m : n gives m × x ÷ (m + n) and n × x ÷ (m + n)."],
       ncert=["summary"], video_focus=["RECAP"], key_terms=["ratio", "proportion"], minutes=8),
     A("T10.C2", "Binairo", "Analyze",
       "Students fill a Binairo grid with horizontal and vertical lines so that every row and column is balanced, no "
       "more than two of the same symbol are adjacent, and no two rows or columns are the same.",
       textbook=["Binairo, also known as Takuzu, is a logic puzzle with simple rules. Binairo is generally played on a "
                 "square grid with no particular size. Some cells start out filled with two symbols: here horizontal "
                 "and vertical lines. The rest of the cells are empty. The task is to fill cells in such a way that:",
                 "Each row and each column must contain an equal number of horizontal and vertical lines.",
                 "More than two horizontal or vertical lines can't be adjacent.",
                 "Each row is unique. Each column is unique.",
                 "Solve the following Binairo puzzles."],
       teach=["Predict first: if a row already has two horizontal lines side by side, what must the next cell be?",
              "Look for pairs first: a pair of the same symbol forces the other symbol on both sides.",
              "Count next: once a row has half of one symbol, the rest must be the other.",
              "Finally use uniqueness to separate rows or columns that would be the same."],
       examples=[
           WE("In a Binairo row of 6 cells, the first two cells hold horizontal lines and the fifth holds a vertical "
              "line. Fill the row.",
              ["Two horizontal lines are adjacent, so the third cell must be a vertical line.",
               "A row of 6 cells needs 3 of each symbol; so far there are 2 horizontal and 2 vertical.",
               "The fourth cell next to a vertical pair would make three verticals if cells 3, 4 and 5 were all "
               "vertical, so cell 4 is horizontal.",
               "That makes 3 horizontal lines, so cell 6 is vertical: H H V H V V."],
              "H H V H V V",
              ncert=["puzzle"])],
       key_terms=["logic puzzle"], enrichment=True, minutes=6)],
    topic_type="summary"))
