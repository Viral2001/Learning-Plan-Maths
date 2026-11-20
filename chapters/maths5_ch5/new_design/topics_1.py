# -*- coding: utf-8 -*-
"""Topics T1, T1B, T2 and T3 (modules M1 and M2): the framing intro (Shikha and Sonu at the weaving centre, a hook and
the free Unit Picker), the short idea topic T1B (Choosing and Naming Units with the Let Us Find and weaving centre
questions), Comparing Lengths (Let Us Compare), and Measuring Long Distances (the kilometre, equal pieces, the Kilometre
Race).
Every teaching concept has one worked example with the plan's own numbers (practice values); every book question is an
FIO item of its topic's DOER, in the book's order."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Which Unit Fits? (framing) ==============================================
# The framing topic holds only the hook video and the free-try tool, and no book question. The concept videos and the
# opener's questions follow in the short idea topic T1B.
TOPICS.append(TOPIC(
    "T1", "M1", "Which Unit Fits?", ["Chapter opening"], "Understand",
    "",
    "Shikha and Sonu are measuring saris and stoles in the village weaving centre. One tape is marked in centimetres "
    "and one in metres. Try the unit tags and find out which unit fits each length.",
    [A("T1.C1", "Shikha and Sonu at the Weaving Centre", "Understand",
       "",
       textbook=["We have learnt about measuring length and some standard units we use to measure length. In this "
                 "chapter we will learn some more units of measuring distances and the relationships between "
                 "different units.",
                 "Shikha and Sonu are measuring the lengths of saris and stoles in the village weaving centre."],
       teach=["Predict first: Shikha and Sonu are measuring a sari at the village weaving centre. Shikha's tape is "
              "marked in centimetres and Sonu's tape is marked in metres. Will they read out the same number?",
              "Shikha and Sonu are measuring the lengths of saris and stoles in the village weaving centre.",
              "Shikha reads a number from her tape. Sonu reads a different number from his tape. It is the same "
              "sari!",
              "Which tape would you use for a handkerchief? For a sari? For the height of India Gate? Think about it, "
              "then try it on the next screen."],
       ncert=["open.intro", "sari.story"], key_terms=["length", "unit", "measure"],
       video_focus=["HOOK"], enrichment=True, minutes=4),
     DOER("T1.C3", "Unit Picker: Explore", "unit_picker", "Understand",
          "",
          ["Shikha's tape is marked in centimetres and Sonu's tape is marked in metres.",
           "A handkerchief, a sari and the height of India Gate are very different lengths.",
           "Drop the cm tag or the m tag on a number and see which one fits."],
          misconceptions=["M_UNIT_ANY"], role="try_it", enrichment=True)],
    topic_type="framing", key_terms=["length", "unit", "measure"]))

# ============================== T1B Choosing and Naming Units ==============================================
TOPICS.append(TOPIC(
    "T1B", "M1", "Choosing and Naming Units", ["Let Us Find", "Different Units but Same Measure"], "Understand",
    "Students choose a sensible unit, cm or m, for a length, and write one length in both m and cm.",
    "Short things are measured in cm and long things in m, so the number sounds sensible. One length has two names: "
    "1 m = 100 cm, so m become cm when you multiply by 100.",
    [A("T1B.C1", "Choosing a Unit That Fits", "Understand",
       "Students choose cm or m for a length by asking how big the thing is and picking the unit that gives a "
       "sensible number.",
       teach=["Predict first: would you measure a pencil in centimetres or in metres? And a classroom wall?",
              "A pencil fits in your hand, so its length is a small number of centimetres. A classroom wall is much "
              "longer than you, so its length is a small number of metres.",
              "Ask two questions: how big is the thing, and does the number sound sensible? 17 cm for a pencil sounds "
              "right. 17 m for a pencil would be longer than a classroom.",
              "A short length such as a pencil, a handkerchief or a mobile phone is measured in cm. A long length such "
              "as a room, a well or a tall building is measured in m.",
              "Rule: pick the unit that gives a sensible number, cm for short things and m for long things."],
       examples=[WE("Shikha measures a pencil and Sonu measures a classroom wall (practice values). The pencil is 17 "
                    "long and the wall is 8 long. Write cm or m for each.",
                    ["The pencil fits in a hand, so it is short. Its unit is cm: 17 cm.",
                     "The classroom wall is longer than a child, so it is long. Its unit is m: 8 m.",
                     "Check the pencil: 17 m would be longer than a classroom, so 17 cm is the sensible length.",
                     "Check the wall: 8 cm would be shorter than the pencil, so 8 m is the sensible length."],
                    "The pencil is 17 cm and the wall is 8 m, because the pencil is short and the wall is long")],
       key_terms=["unit", "cm", "m", "sensible"], misconceptions=["M_UNIT_ANY"], minutes=4),
     A("T1B.C2", "Metres and Centimetres: One Length, Two Names", "Understand",
       "Students change a length from m to cm and from cm to m and cm using 1 m = 100 cm.",
       teach=["Predict first: Shikha's tape says 300 and Sonu's tape says 3 for the same stole. Can both numbers be "
              "right?",
              "Yes. The two tapes use different units. 1 m is the same length as 100 cm, so one length has two "
              "names.",
              "A double number line shows both names. The top line is in m, the bottom line is in cm, and from the top "
              "line to the bottom line every number is multiplied by 100.",
              "To change m to cm, multiply by 100: 3 m = 3 × 100 = 300 cm.",
              "To change cm to m and cm, take out the hundreds: 450 cm = 400 cm + 50 cm = 4 m 50 cm, because "
              "400 ÷ 100 = 4.",
              "A part bigger than 100 cm is allowed too: 3 m 130 cm = 300 cm + 130 cm = 430 cm.",
              "Rule: 1 m = 100 cm, so multiply by 100 to change m to cm."],
       examples=[WE("Sonu measures a stole as 3 m. How many cm is that? Shikha measures another stole as 450 cm. How "
                    "many m and cm is that? (practice values)",
                    ["1 m = 100 cm, so change m to cm by multiplying by 100.",
                     "3 m = 3 × 100 = 300 cm.",
                     "To change 450 cm, take out the hundreds: 450 cm = 400 cm + 50 cm.",
                     "400 cm = 400 ÷ 100 = 4 m, so 450 cm = 4 m 50 cm.",
                     "Check: 4 m 50 cm = 4 × 100 + 50 = 450 cm."],
                    "3 m = 300 cm and 450 cm = 4 m 50 cm")],
       key_terms=["1 m = 100 cm", "double number line", "multiply by 100"],
       misconceptions=["M_M_TEN_CM", "M_JOIN_NUMBERS"], minutes=5),
     DOER("T1B.C3", "Practice: Units and Names", None, "Apply",
          "Students choose the unit, m or cm, for six lengths, and name the same length in m and cm by filling in "
          "number lines side by side and matching lengths.",
          ["Pick the unit that gives a sensible number: cm for short things and m for long things.",
           "1 m = 100 cm, so multiply by 100 to change m to cm and take out the hundreds to change cm to m.",
           "Change every length to cm and the matching lengths are easy to see."],
          items=[FIO("find.units", "Let Us Find: unit for each length",
                     "Identify the appropriate units for measuring each of the following. Write m or cm "
                     "after each number. (a): the height of India Gate is 42 ___; (b): the length of a "
                     "handkerchief is 40 ___; (c): the depth of a well is 50 ___; (d): the length of a mobile phone is "
                     "13 ___; (e): the length of an elephant's trunk is 2 ___; (f): the distance between two buttons "
                     "on a shirt is 5 ___.",
                     ["Ask for each one: how big is the thing? Then pick m or cm so the number sounds sensible.",
                      "(a): India Gate is a tall building. 42 m is a sensible height, 42 cm is not.",
                      "(b): A handkerchief fits in your hand. 40 cm is sensible.",
                      "(c): A well is deep. 50 m is a sensible depth, a well that is only 50 cm deep is not possible.",
                      "(d): A mobile phone fits in your hand. 13 cm is sensible.",
                      "(e): An elephant's trunk is longer than a child's arm. 2 m is sensible, 2 cm is far too short.",
                      "(f): Two buttons on a shirt are close together. 5 cm is sensible.",
                      "Check: the tall and long things are in m, and the small things are in cm."],
                     "(a): m; (b): cm; (c): m; (d): cm; (e): m; (f): cm",
                     kind="exercise",
                     q_figure="A table with six rows, height of India Gate 42, length of a handkerchief 40, depth of a "
                              "well 50, length of a mobile phone 13, length of an elephant's trunk 2 and distance "
                              "between two buttons on a shirt 5, each with an empty box for the unit, m or cm."),
                 FIO("sari.line", "Different Units but Same Measure: fill the double number line",
                     "Shikha and Sonu are measuring the lengths of saris and stoles in the village weaving centre. "
                     "You can take help of the double number line below. Fill in the blanks. Top line: 100 cm, ___ cm, "
                     "400 cm, 500 cm, 700 cm. Bottom line: 1 m, 2 m, ___ m, ___ m, ___ m.",
                     ["The top line is in cm and the bottom line is in m. The arrow ×100 says that m become cm when "
                      "you multiply by 100.",
                      "The arrow ×2 says that 2 m is twice 1 m, so the cm are twice 100 cm: 2 × 100 = 200 cm. The "
                      "first blank is 200 cm.",
                      "400 cm is 400 ÷ 100 = 4 m, so the first blank on the bottom line is 4 m.",
                      "500 cm is 500 ÷ 100 = 5 m, so the next blank is 5 m.",
                      "700 cm is 700 ÷ 100 = 7 m, so the last blank is 7 m.",
                      "Check: 4 × 100 = 400, 5 × 100 = 500 and 7 × 100 = 700."],
                     "Top line: 200 cm. Bottom line: 4 m, 5 m, 7 m",
                     kind="prompt",
                     q_figure="A double number line with five ticks: the top line is labelled 100 cm, a blank cm, "
                              "400 cm, 500 cm and 700 cm, the bottom line is labelled 1 m, 2 m and three blank m, with "
                              "an arrow ×100 between 1 m and 100 cm and an arrow ×2 from 100 cm to the blank cm.",
                     s_figure="The same double number line with every blank filled in: 200 cm on the top line, and "
                              "4 m, 5 m and 7 m on the bottom line."),
                 FIO("sari.match", "Different Units but Same Measure: match the lengths",
                     "Shikha and Sonu are measuring the lengths of saris and stoles in the village weaving centre. "
                     "Find which measures represent the same sari or stole. First list: 204 cm, 540 cm, 750 cm, "
                     "240 cm, 404 cm. Second list: 5 m 40 cm, 2 m 204 cm, 2 m 4 cm, 2 m 40 cm, 6 m 150 cm.",
                     ["Change every length in the second list to cm. 1 m = 100 cm.",
                      "5 m 40 cm = 5 × 100 + 40 = 540 cm. It matches 540 cm.",
                      "2 m 204 cm = 2 × 100 + 204 = 404 cm. It matches 404 cm.",
                      "2 m 4 cm = 2 × 100 + 4 = 204 cm. It matches 204 cm.",
                      "2 m 40 cm = 2 × 100 + 40 = 240 cm. It matches 240 cm.",
                      "6 m 150 cm = 6 × 100 + 150 = 750 cm. It matches 750 cm.",
                      "Check: the five matches use every length in both lists once."],
                     "204 cm = 2 m 4 cm; 540 cm = 5 m 40 cm; 750 cm = 6 m 150 cm; 240 cm = 2 m 40 cm; 404 cm = 2 m 204 cm",
                     kind="prompt",
                     q_figure="A table with five rows: the first column has 204 cm, 540 cm, 750 cm, 240 cm and 404 cm "
                              "and the second column has 5 m 40 cm, 2 m 204 cm, 2 m 4 cm, 2 m 40 cm and 6 m 150 cm.",
                     s_figure="The same table with lines joining 204 cm to 2 m 4 cm, 540 cm to 5 m 40 cm, 750 cm to "
                              "6 m 150 cm, 240 cm to 2 m 40 cm and 404 cm to 2 m 204 cm.")],
          misconceptions=["M_UNIT_ANY", "M_M_TEN_CM", "M_JOIN_NUMBERS"])],
    key_terms=["unit", "1 m = 100 cm", "double number line"]))

# ============================== T2 Comparing Lengths =======================================================
TOPICS.append(TOPIC(
    "T2", "M1", "Comparing Lengths", ["Let Us Compare"], "Apply",
    "Students compare two lengths given in different units by changing them to one unit, and find how much longer "
    "one length is than another.",
    "To compare lengths, change them to the same unit, the smaller one, and compare the numbers. The difference is the "
    "longer length minus the shorter length in that unit.",
    [A("T2.C1", "Comparing Lengths in Different Units", "Apply",
       "Students compare two lengths given in different units by changing both to the same unit and then comparing "
       "the numbers.",
       teach=["Predict first: which is longer, 7 m 9 cm or 790 cm?",
              "Do not compare the numbers 7 and 790 straight away. They are in different units, and 7 m 9 cm is not "
              "7 m 90 cm.",
              "Change both lengths to cm. 7 m 9 cm = 7 × 100 + 9 = 709 cm.",
              "Now both are in cm. 709 is less than 790, so 7 m 9 cm is less than 790 cm.",
              "Take care with a small part: 4 m 3 cm is 403 cm, not 430 cm. The 3 cm is 3 cm, not 30 cm.",
              "Rule: change both lengths to the same unit, the smaller one, then compare the numbers."],
       examples=[WE("Compare 7 m 9 cm and 790 cm using <, = or > (practice values).",
                    ["The units are different, so change both lengths to cm.",
                     "7 m 9 cm = 7 × 100 + 9 = 709 cm.",
                     "790 cm is already in cm.",
                     "Compare 709 and 790: 709 is less than 790.",
                     "So 7 m 9 cm < 790 cm.",
                     "Check: 790 cm is 7 m 90 cm, and 7 m 9 cm is shorter than 7 m 90 cm."],
                    "7 m 9 cm < 790 cm, because 709 cm is less than 790 cm")],
       key_terms=["compare", "same unit", "length"], misconceptions=["M_BIGGER_NUMBER", "M_JOIN_NUMBERS"], minutes=5),
     A("T2.C2", "How Much Longer? The Difference of Two Lengths", "Apply",
       "Students find how much longer one length is than another by changing both to one unit and subtracting, and "
       "find the length that doubles to a given length.",
       teach=["Predict first: Sonu's stole is 285 cm long and Shikha's stole is 2 m 60 cm long. Which is longer, and "
              "by how much?",
              "First change both to cm. 2 m 60 cm = 2 × 100 + 60 = 260 cm.",
              "The difference is the longer length minus the shorter length: 285 − 260 = 25 cm.",
              "So Sonu's stole is longer by 25 cm.",
              "Doubling a length means multiplying it by 2. A rope of 90 cm doubled is 90 × 2 = 180 cm.",
              "To find the length that becomes 180 cm when doubled, halve it: 180 ÷ 2 = 90 cm.",
              "Rule: the difference is the bigger length minus the smaller length in the same unit. To undo doubling, "
              "halve."],
       examples=[WE("Sonu's stole is 285 cm long and Shikha's stole is 2 m 60 cm long (practice values). Which is "
                    "longer and by how much? A third piece doubled is 180 cm long. How long is the third piece?",
                    ["Change 2 m 60 cm to cm: 2 × 100 + 60 = 260 cm.",
                     "Compare 285 and 260: 285 is more, so Sonu's stole is longer.",
                     "Subtract the smaller from the bigger: 285 − 260 = 25 cm.",
                     "A piece that doubled is 180 cm: doubling is × 2, so the piece is 180 ÷ 2 = 90 cm.",
                     "Check: 260 + 25 = 285 and 90 × 2 = 180."],
                    "Sonu's stole is longer by 25 cm, and the third piece is 90 cm long")],
       key_terms=["difference", "doubled", "subtract"], minutes=5),
     DOER("T2.C3", "Practice: Length Bars", "length_bars", "Apply",
          "Students compare the length of rods with <, = and > by changing to one unit, and find the difference of "
          "two statue heights, the least and the largest differences, and the statue that doubles to the tallest.",
          ["Change both lengths to the same unit, the smaller one, then compare the numbers.",
           "The difference is the bigger length minus the smaller length in the same unit.",
           "Doubling is × 2 and halving undoes it."],
          items=[FIO("cmp.q1", "Let Us Compare: Q1 five rods",
                     "Ritika is comparing the lengths of different rods. Compare them using <, =, > signs. (a): 456 cm "
                     "___ 5 m; (b): 55 cm + 200 cm ___ 200 cm + 54 cm; (c): 6 m 5 cm ___ 6 m 50 cm; (d): 2 m 150 cm "
                     "___ 3 m 50 cm; (e): 238 cm ___ 138 cm + 1 m.",
                     ["Change both sides to the same unit, cm, then compare. 1 m = 100 cm.",
                      "(a): 5 m = 5 × 100 = 500 cm. 456 is less than 500, so 456 cm < 5 m.",
                      "(b): 55 cm + 200 cm = 255 cm and 200 cm + 54 cm = 254 cm. 255 is more than 254, so the left "
                      "side is more.",
                      "(c): 6 m 5 cm = 6 × 100 + 5 = 605 cm and 6 m 50 cm = 6 × 100 + 50 = 650 cm. 605 is less than "
                      "650, so the left side is less.",
                      "(d): 2 m 150 cm = 2 × 100 + 150 = 350 cm and 3 m 50 cm = 3 × 100 + 50 = 350 cm. They are "
                      "equal.",
                      "(e): 138 cm + 1 m = 138 + 100 = 238 cm. 238 cm is equal to 238 cm.",
                      "Check (c): 5 cm is less than 50 cm, so 6 m 5 cm is less than 6 m 50 cm."],
                     "(a): <; (b): >; (c): <; (d): =; (e): =",
                     kind="exercise"),
                 FIO("cmp.q2a", "Let Us Compare: Q2 (a) difference with the Statue of Liberty",
                     "Look at the picture of some of the world's tallest statues. What is the difference between the "
                     "height of the tallest statue in the world and the Statue of Liberty?",
                     ["Find the tallest statue in the picture: the Statue of Unity, 182 m.",
                      "The Statue of Liberty is 93 m.",
                      "The difference is the bigger height minus the smaller height: 182 − 93 = 89 m.",
                      "Check: 93 + 89 = 182."],
                     "89 m",
                     kind="exercise",
                     q_figure="Six statues in a row on one base line, with their heights: Statue of Unity, India, "
                              "182 m; Spring Temple Buddha, China, 128 m; Guanyin of Nanshan, China, 108 m; Statue of "
                              "Liberty, USA, 93 m; The Motherland Calls, Russia, 91 m; Christ the Redeemer, Brazil, "
                              "38 m.",
                     s_figure="The same six statues with the Statue of Unity and the Statue of Liberty highlighted and "
                              "the gap between their heights marked 89 m."),
                 FIO("cmp.q2b", "Let Us Compare: Q2 (b) least difference",
                     "Look at the picture of some of the world's tallest statues. Identify the statues whose heights "
                     "have the least difference.",
                     ["List the heights from the tallest to the shortest: 182 m, 128 m, 108 m, 93 m, 91 m, 38 m.",
                      "Find the difference of each statue and the next one in the list: 182 − 128 = 54 m, "
                      "128 − 108 = 20 m, 108 − 93 = 15 m, 93 − 91 = 2 m, 91 − 38 = 53 m.",
                      "Two statues that are not next to each other have a statue between them, so they differ by even "
                      "more.",
                      "The least difference is 2 m, between the Statue of Liberty (93 m) and The Motherland Calls "
                      "(91 m).",
                      "Check: 93 − 91 = 2, and every other pair is farther apart."],
                     "The Statue of Liberty and The Motherland Calls, 2 m apart",
                     kind="exercise",
                     q_figure="Six statues in a row on one base line, with their heights: Statue of Unity, India, "
                              "182 m; Spring Temple Buddha, China, 128 m; Guanyin of Nanshan, China, 108 m; Statue of "
                              "Liberty, USA, 93 m; The Motherland Calls, Russia, 91 m; Christ the Redeemer, Brazil, "
                              "38 m.",
                     s_figure="The same six statues with the Statue of Liberty and The Motherland Calls highlighted and "
                              "the gap between their heights marked 2 m."),
                 FIO("cmp.q2c", "Let Us Compare: Q2 (c) largest difference",
                     "Look at the picture of some of the world's tallest statues. Identify the statues whose heights "
                     "have the largest difference.",
                     ["The largest difference is between the tallest statue and the shortest statue.",
                      "The tallest is the Statue of Unity, 182 m. The shortest is Christ the Redeemer, 38 m.",
                      "The difference is 182 − 38 = 144 m.",
                      "Check: 38 + 144 = 182, and every other pair is closer, for example 182 − 91 = 91 m."],
                     "The Statue of Unity and Christ the Redeemer, 144 m apart",
                     kind="exercise",
                     q_figure="Six statues in a row on one base line, with their heights: Statue of Unity, India, "
                              "182 m; Spring Temple Buddha, China, 128 m; Guanyin of Nanshan, China, 108 m; Statue of "
                              "Liberty, USA, 93 m; The Motherland Calls, Russia, 91 m; Christ the Redeemer, Brazil, "
                              "38 m.",
                     s_figure="The same six statues with the Statue of Unity and Christ the Redeemer highlighted and "
                              "the gap between their heights marked 144 m."),
                 FIO("cmp.q2d", "Let Us Compare: Q2 (d) doubled to the Statue of Unity",
                     "Look at the picture of some of the world's tallest statues. The height of which statue will be "
                     "equal to the height of the Statue of Unity, if it is doubled?",
                     ["If a statue doubled is 182 m, its height is half of 182 m.",
                      "182 ÷ 2 = 91 m.",
                      "The Motherland Calls is 91 m tall.",
                      "Check: 91 × 2 = 182, and no other statue has a height that doubles to 182."],
                     "The Motherland Calls, 91 m",
                     kind="exercise",
                     q_figure="Six statues in a row on one base line, with their heights: Statue of Unity, India, "
                              "182 m; Spring Temple Buddha, China, 128 m; Guanyin of Nanshan, China, 108 m; Statue of "
                              "Liberty, USA, 93 m; The Motherland Calls, Russia, 91 m; Christ the Redeemer, Brazil, "
                              "38 m.",
                     s_figure="The same six statues with The Motherland Calls highlighted and a second copy of it "
                              "stacked on top, reaching the height of the Statue of Unity.")],
          misconceptions=["M_BIGGER_NUMBER", "M_JOIN_NUMBERS"])],
    key_terms=["compare", "difference", "same unit"]))

# ============================== T3 Measuring Long Distances ================================================
TOPICS.append(TOPIC(
    "T3", "M2", "Measuring Long Distances", ["Measuring Long Distances", "Let Us Explore", "Kilometre Race"], "Apply",
    "Students change a distance between km and m using 1 km = 1,000 m, and find how many equal ropes or stops fit "
    "along a distance and where they stand.",
    "1 km = 1,000 m. To find how many equal pieces fit along a distance, change the distance to m and divide by the "
    "length of one piece; the stops stand at 1, 2, 3 and so on times that length.",
    [A("T3.C1", "The Kilometre", "Understand",
       "Students change a distance between kilometres and metres using 1 km = 1,000 m, and say that kilo stands "
       "for thousand.",
       textbook=["Here are some ways in which you can measure long distances.",
                 "When we walk 1,000 m, we say we have walked 1 km.",
                 "1,000 m = 1 km",
                 "Kilo stands for thousand. This unit is used to measure long distances."],
       teach=["Predict first: how many metres do you walk to cover 1 km?",
              "When we walk 1,000 m, we say we have walked 1 km. So 1 km = 1,000 m.",
              "Kilo stands for thousand. A km is 1,000 times as long as a m, so the km is used to measure long "
              "distances.",
              "Your maths book shows four ways to measure long distances: a long tape, a rodometer (a measuring "
              "wheel), a rangefinder and a laser distance meter.",
              "To change km to m, multiply by 1,000: 7 km = 7 × 1,000 = 7,000 m.",
              "To change m to km, take out the thousands: 5,400 m = 5,000 m + 400 m = 5 km 400 m.",
              "Rule: 1 km = 1,000 m, so multiply by 1,000 to change km to m."],
       examples=[WE("A path is 7 km long. How many m is that? A road is 5,400 m long. How many km and m is that? "
                    "(practice values)",
                    ["1 km = 1,000 m, so multiply the km by 1,000.",
                     "7 km = 7 × 1,000 = 7,000 m.",
                     "To change 5,400 m, take out the thousands: 5,400 m = 5,000 m + 400 m.",
                     "5,000 m = 5,000 ÷ 1,000 = 5 km, so 5,400 m = 5 km 400 m.",
                     "Check: 5 km 400 m = 5 × 1,000 + 400 = 5,400 m."],
                    "7 km = 7,000 m and 5,400 m = 5 km 400 m")],
       ncert=["km.tools", "km.def"], key_terms=["kilometre", "1 km = 1,000 m", "kilo"],
       misconceptions=["M_KM_HUNDRED"], minutes=5),
     A("T3.C2", "Equal Pieces Along a Distance", "Apply",
       "Students find how many equal ropes or stops fit along a distance by dividing the distance by the length of "
       "one piece, and say where each stop stands.",
       teach=["Predict first: a 2 km cycle track has a flag after every 400 m. How many flags are needed, and where "
              "do they stand?",
              "First change 2 km to m: 2 km = 2 × 1,000 = 2,000 m.",
              "Each piece of the track is 400 m long, so divide: 2,000 ÷ 400 = 5 pieces, and so 5 flags.",
              "The flags stand at 1, 2, 3, 4 and 5 times 400 m from the start: 400 m, 800 m, 1,200 m, 1,600 m and "
              "2,000 m. The last flag is at the end.",
              "The same idea tells how many ropes make 1 km. If every rope is 125 m long, 1,000 ÷ 125 = 8 ropes make "
              "1 km.",
              "Rule: the number of equal pieces is the whole distance ÷ the length of one piece. The stops stand at "
              "1, 2, 3 and so on times the length of one piece."],
       examples=[WE("A cycle track is 2 km long. A flag stands after every 400 m, and the last flag is at the end of "
                    "the track (practice values). How many flags are needed, and at which positions?",
                    ["Change 2 km to m: 2 × 1,000 = 2,000 m.",
                     "Divide the track into pieces of 400 m: 2,000 ÷ 400 = 5.",
                     "So 5 flags are needed.",
                     "The flags stand at 1, 2, 3, 4 and 5 times 400 m: 400 m, 800 m, 1,200 m, 1,600 m and 2,000 m.",
                     "Check: 5 × 400 = 2,000, the whole track."],
                    "5 flags, at 400 m, 800 m, 1,200 m, 1,600 m and 2,000 m")],
       key_terms=["equal pieces", "divide", "positions"], misconceptions=["M_STOP_COUNT"], minutes=6),
     DOER("T3.C3", "Practice: Kilometre Track", "kilometre_track", "Apply",
          "Students find how many ropes of a given length make 1 kilometre, and how many water stations, children and "
          "flags a 3 km race track needs, with their positions.",
          ["1 km = 1,000 m, so change km to m first.",
           "The number of equal pieces = the distance ÷ the length of one piece.",
           "The stops stand at 1, 2, 3 and so on times the length of one piece."],
          items=[FIO("walk.steps", "Measuring Long Distances: walk and count steps",
                     "Measure 100 m and 200 m on your school playground, or any other place in and around your "
                     "school, using a long tape. Mark these points and draw a straight line. Walk on the lines and "
                     "count the number of steps. Use this relationship between the number of steps taken and distance "
                     "walked to find distances around you for at least 3 locations. Wherever possible, walk and find "
                     "the number of steps. Otherwise, find the distance and estimate the number of steps. (a): "
                     "Identify and write the locations that are the nearest and the farthest from your home. (b): "
                     "Write the distances obtained above in increasing order. (c): Name a location that is equal to "
                     "or more than 1,000 m from your home.",
                     ["This is an activity at your school and near your home. The numbers below are practice values "
                      "that show how to do it. Yours will differ.",
                      "Use a long tape to measure 100 m and 200 m on the playground, mark the points and walk each "
                      "line, counting steps. Practice values: 100 m takes 125 steps and 200 m takes 250 steps.",
                      "Find the length of one step: 100 m = 100 × 100 = 10,000 cm, and 10,000 ÷ 125 = 80 cm. So one "
                      "step is 80 cm.",
                      "Use the step to find other distances. A tea shop is 120 m away: 12,000 ÷ 80 = 150 steps. A "
                      "school gate is 400 m away: 40,000 ÷ 80 = 500 steps. A temple is 1,600 m away: 160,000 ÷ 80 = "
                      "2,000 steps.",
                      "(a): The nearest is the tea shop, 120 m. The farthest is the temple, 1,600 m.",
                      "(b): In increasing order: 120 m, 400 m, 1,600 m.",
                      "(c): The temple is more than 1,000 m away: 1,600 m = 1 km 600 m.",
                      "Check: 125 × 80 = 10,000 cm, which is 100 m."],
                     "Sample answer, practice values: nearest 120 m; farthest 1,600 m; in order 120 m, 400 m, 1,600 m; "
                     "(c): 1 km 600 m. Your answer may differ.",
                     kind="exercise",
                     q_figure="Four pictures of tools for measuring long distances: a long tape, a rodometer "
                              "(measuring wheel), a rangefinder and a laser distance meter."),
                 FIO("rope.table", "Measuring Long Distances: ropes for 1 km",
                     "Ropes of different lengths are used to make 1 km. Find how many ropes of each length are needed "
                     "to make 1 km. A rope of 1,000 m: 1 rope. (a): a rope of 100 m: ___ ropes; (b): a rope of 10 m: "
                     "___ ropes; (c): a rope of 200 m: ___ ropes; (d): a rope of 500 m: ___ ropes; (e): a rope of "
                     "250 m: ___ ropes.",
                     ["1 km = 1,000 m. The number of ropes = 1,000 ÷ the length of one rope.",
                      "(a): 100 m: 1,000 ÷ 100 = 10 ropes.",
                      "(b): 10 m: 1,000 ÷ 10 = 100 ropes.",
                      "(c): 200 m: 1,000 ÷ 200 = 5 ropes.",
                      "(d): 500 m: 1,000 ÷ 500 = 2 ropes.",
                      "(e): 250 m: 1,000 ÷ 250 = 4 ropes.",
                      "Check: a shorter rope needs more ropes. 10 m is the shortest rope and needs the most, 100 "
                      "ropes."],
                     "(a): 10; (b): 100; (c): 5; (d): 2; (e): 4",
                     kind="prompt",
                     q_figure="A table with two columns, length of rope and number of ropes needed to make 1 km: "
                              "1,000 m has 1 and the rows 100 m, 10 m, 200 m, 500 m and 250 m have empty boxes.",
                     s_figure="The same table filled in: 100 m needs 10 ropes, 10 m needs 100, 200 m needs 5, 500 m "
                              "needs 2 and 250 m needs 4."),
                 FIO("race.q1", "Kilometre Race: Q1 water stations",
                     "Sheena and Jennifer are helping to organise a 3 km race. Help them with the arrangements for "
                     "the race. Water stations are to be arranged after every 500 m. How many water stations must be "
                     "set up? At what positions from the starting point will these water stations be placed?",
                     ["Change 3 km to m: 3 × 1,000 = 3,000 m.",
                      "A water station after every 500 m: 3,000 ÷ 500 = 6 stations. The last one is at the finish "
                      "line.",
                      "The stations stand at 1, 2, 3, 4, 5 and 6 times 500 m from the start.",
                      "Positions: 500 m, 1 km, 1 km 500 m, 2 km, 2 km 500 m and 3 km.",
                      "Check: 6 × 500 = 3,000 m, the whole race."],
                     "6 stations, at 500 m, 1 km, 1 km 500 m, 2 km, 2 km 500 m and 3 km",
                     kind="exercise",
                     q_figure="A straight race track of 3 km from the starting point to the finish line.",
                     s_figure="The same track with six water cups at 500 m, 1 km, 1 km 500 m, 2 km, 2 km 500 m and "
                              "3 km."),
                 FIO("race.q2", "Kilometre Race: Q2 children",
                     "Sheena and Jennifer are helping to organise a 3 km race. Children need to stand at an interval "
                     "of 300 m to direct the runners. How many children are needed? At what positions from the "
                     "starting point will the children be standing?",
                     ["Change 3 km to m: 3 × 1,000 = 3,000 m.",
                      "Children at an interval of 300 m: 3,000 ÷ 300 = 10 children. The last one is at the finish "
                      "line.",
                      "They stand at 1, 2, 3 and so on up to 10 times 300 m from the start.",
                      "Positions: 300 m, 600 m, 900 m, 1,200 m, 1,500 m, 1,800 m, 2,100 m, 2,400 m, 2,700 m and "
                      "3,000 m.",
                      "Check: 10 × 300 = 3,000 m."],
                     "10 children, at every 300 m from 300 m to 3,000 m",
                     kind="exercise",
                     q_figure="A straight race track of 3 km from the starting point to the finish line.",
                     s_figure="The same track with ten children standing at 300 m, 600 m, 900 m and so on up to "
                              "3,000 m."),
                 FIO("race.q3", "Kilometre Race: Q3 flags",
                     "Sheena and Jennifer are helping to organise a 3 km race. Red and blue flags are to be placed "
                     "alternately at every 50 m. How many red and blue flags are needed till the finish line?",
                     ["Change 3 km to m: 3 × 1,000 = 3,000 m.",
                      "A flag at every 50 m: 3,000 ÷ 50 = 60 flags till the finish line. The first flag is at 50 m "
                      "and the last is at the finish line.",
                      "The flags are red and blue by turns: red, blue, red, blue and so on. Half are red and half are "
                      "blue.",
                      "60 ÷ 2 = 30, so there are 30 red flags and 30 blue flags.",
                      "Check: 30 + 30 = 60, and 60 × 50 = 3,000 m."],
                     "60 flags: 30 red and 30 blue",
                     kind="exercise",
                     q_figure="A straight race track of 3 km from the starting point to the finish line.",
                     s_figure="The same track with red and blue flags by turns at 50 m, 100 m, 150 m and so on up to "
                              "3,000 m.")],
          misconceptions=["M_KM_HUNDRED", "M_STOP_COUNT"])],
    key_terms=["kilometre", "1 km = 1,000 m", "equal pieces"]))
