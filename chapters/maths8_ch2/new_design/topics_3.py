# -*- coding: utf-8 -*-
"""Topics T10 to T14 (modules M5 and M6, summary). Book sections 2.4, 2.5 Did You Ever Wonder, 2.5 A Pinch of
History, the summary and the Tremendous in Ten game, pp 30 to 47."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T10 Powers of 10 and scientific notation ===================================
TOPICS.append(TOPIC(
    "T10", "M5", "Powers of 10 and Scientific Notation", ["2.4"], "Apply",
    "Students write numbers in expanded form with powers of 10, write very large numbers in scientific notation, "
    "explain why the exponent of 10 matters more than the coefficient, and compare distances in the Solar System.",
    "Any number can be written as a number from 1 up to 10 times a power of 10; the exponent tells the size, and "
    "the coefficient gives the finer detail.",
    [A("T10.C1", "Expanded form with powers of 10", "Apply",
       "Students write 47561, 172, 5642 and 6374 in expanded form using powers of 10, and write the decimal 561.903 "
       "using negative powers of 10 for the decimal places.",
       textbook=["2.4 Powers of 10",
                 "We have used numbers like 10, 100, 1000, and so on when writing Indian numerals in an expanded form. "
                 "For example, 47561 = (4 × 10000) + (7 × 1000) + (5 × 100) + (6 × 10) + 1.",
                 "This can be written using powers of 10 as (4 × 10⁴) + (7 × 10³) + (5 × 10²) + (6 × 10 to the power "
                 "1) + (1 × 10 to the power 0).",
                 "Write these numbers in the same way: (i) 172, (ii) 5642, (iii) 6374.",
                 "How can we write 561.903? Writing it using powers of 10, we have 561.903 as (5 × 10²) + (6 × 10 to "
                 "the power 1) + (1 × 10 to the power 0) + (9 × 10 to the power −1) + (0 × 10 to the power −2) + "
                 "(3 × 10 to the power −3)."],
       teach=["Predict first: which power of 10 goes with the 4 in 47561?",
              "Each place value is a power of 10: ones 10 to the power 0, tens 10 to the power 1, hundreds 10², and "
              "so on.",
              "So 47561 is 4 × 10⁴ plus 7 × 10³ plus 5 × 10² plus 6 tens plus 1 one.",
              "After the decimal point the places are tenths, hundredths, thousandths: 10 to the powers −1, −2, −3."],
       examples=[
           WE("Write 5642 in expanded form with powers of 10, and write 561.903 using powers of 10.",
              ["5642 has 5 thousands, 6 hundreds, 4 tens and 2 ones.",
               "So 5642 is (5 × 10³) + (6 × 10²) + (4 × 10 to the power 1) + (2 × 10 to the power 0).",
               "Check: 5000 + 600 + 40 + 2 = 5642.",
               "561.903 is 5 hundreds, 6 tens, 1 one, 9 tenths, 0 hundredths and 3 thousandths.",
               "So it is (5 × 10²) + (6 × 10 to the power 1) + (1 × 10 to the power 0) + (9 × 10 to the power −1) + "
               "(0 × 10 to the power −2) + (3 × 10 to the power −3)."],
              "5642 is 5 × 10³ + 6 × 10² + 4 × 10 + 2; the decimal places of 561.903 use 10 to the powers −1, −2 "
              "and −3",
              ncert=["2.4.expanded", "2.4.write_three", "2.4.decimal"])],
       key_terms=["expanded form", "powers of 10", "place value"], misconceptions=["M_POW_TIMES"], minutes=10),
     A("T10.C2", "Scientific notation for very large numbers", "Apply",
       "Students write 5900 as a number from 1 up to 10 times a power of 10, and write three very large facts "
       "about the Sun, the galaxy and the Earth in scientific notation.",
       textbook=["Scientific Notation",
                 "Let's look at some facts involving large numbers: (i) The Sun is located 300000000000000000000 m "
                 "from the centre of our Milky Way galaxy. (ii) The number of stars in our galaxy is 100000000000. "
                 "(iii) The mass of the Earth is 5976000000000000000000000 kg.",
                 "As the number of digits increases, it becomes difficult to read the numbers correctly. We may "
                 "miscount the number of zeroes.",
                 "For example, the number 5900 can be expressed as 590 × 10, 59 × 10², 5.9 × 10³ or 0.59 × 10⁴.",
                 "Any number can be written as the product of a number between 1 and 10 and a power of 10.",
                 "In scientific notation or scientific form (also called standard form), we write numbers as x × 10 "
                 "to the power y, where x ≥ 1 and x < 10 is the coefficient and y, the exponent, is any integer."],
       teach=["Predict first: how many zeroes does the mass of the Earth have, and could you read it aloud?",
              "Move the decimal point until one nonzero digit is left before it, and count the moves.",
              "5900 becomes 5.9 after 3 moves, so 5900 is 5.9 × 10³.",
              "The Sun's distance is 3 followed by 20 zeroes: 3 × 10 to the power 20 m."],
       examples=[
           WE("Write 5900 in four ways using powers of 10, and write the three large-number facts in scientific "
              "notation.",
              ["5900 is 590 × 10, 59 × 10², 5.9 × 10³ and 0.59 × 10⁴. Only 5.9 × 10³ has a coefficient from 1 up "
               "to 10.",
               "The Sun's distance is 3 followed by 20 zeroes, so 3 × 10 to the power 20 m.",
               "The stars in the galaxy number 1 followed by 11 zeroes, so 1 × 10 to the power 11.",
               "The mass of the Earth: move the point 24 places to get 5.976, so 5.976 × 10 to the power 24 kg."],
              "5900 is 5.9 × 10³; the facts are 3 × 10 to the power 20 m, 1 × 10 to the power 11 stars and 5.976 × 10 "
              "to the power 24 kg",
              ncert=["2.4.facts", "2.4.5900", "2.4.write_facts", "2.4.sci_form"])],
       key_terms=["scientific notation", "coefficient", "exponent"], misconceptions=["M_SCI_COEFF"], minutes=10),
     A("T10.C3", "The exponent matters more than the coefficient", "Analyze",
       "Students compare changing the coefficient and changing the exponent in Mumbai's population, and use "
       "Kohima's population to explain that the digits of the coefficient show how precise a number is.",
       textbook=["Often, the exponent y is more important than the coefficient x. When we write the 2 crore population "
                 "of Mumbai as 2 × 10 to the power 7, the 7 is more important than the 2.",
                 "If the 2 is changed to 3, the population increases by one-half, i.e., 2 crore to 3 crore, whereas if "
                 "the 7 is changed to 8, the change in population is 10 times, i.e., 2 crores to 20 crores.",
                 "If we say that the population of Kohima is 142395, then it gives the impression that we are quite "
                 "sure about this number up to the units place. If we are only sure that the population is around 1 "
                 "lakh 42 thousand, we can write it as 1.42 × 10 to the power 5.",
                 "The number of digits in the coefficient reflects how well we know the number.",
                 "How old is this dinosaur's skeleton? It is 70 million and 15 years old... when I started working "
                 "here, it was 70 million years old."],
       teach=["Predict first: which change makes Mumbai's population bigger, changing the 2 to a 3 or the 7 to an 8?",
              "Changing the coefficient from 2 to 3 adds half again: 2 crore becomes 3 crore.",
              "Changing the exponent from 7 to 8 multiplies by 10: 2 crore becomes 20 crore.",
              "Kohima's 1.42 × 10 to the power 5 says we know three digits; adding 15 years to 70 million is silly for "
              "the same reason."],
       examples=[
           WE("Mumbai's population is about 2 × 10 to the power 7. Compare changing the coefficient to 3 with changing "
              "the exponent to 8. Then write Kohima's population of about 1 lakh 42 thousand in standard form.",
              ["2 × 10 to the power 7 is 2 crore.",
               "Coefficient 3: 3 crore, which is one and a half times 2 crore.",
               "Exponent 8: 20 crore, which is 10 times 2 crore.",
               "Kohima: about 142000, which is 1.42 × 10 to the power 5, keeping only the digits we are sure of."],
              "Changing the exponent multiplies by 10, changing the coefficient only by 1.5; Kohima is about 1.42 × 10 "
              "to the power 5",
              ncert=["2.4.mumbai_kohima", "2.4.comic"])],
       key_terms=["exponent", "coefficient", "estimate"], misconceptions=["M_SCI_COEFF"], minutes=8),
     A("T10.C4", "Comparing distances in standard form", "Analyze",
       "Students compare the Sun to Saturn, Saturn to Uranus and Sun to Earth distances written in standard form, find "
       "the smallest by comparing exponents first, and mark the Earth's relative position on a number line.",
       textbook=["The distance between the Sun and Saturn is 1433500000000 m, which is 1.4335 × 10 to the power 12 m.",
                 "The distance between Saturn and Uranus is 1439000000000 m, which is 1.439 × 10 to the power 12 m. "
                 "The distance between the Sun and Earth is 149600000000 m, which is 1.496 × 10 to the power 11 m.",
                 "Can you say which of the three distances is the smallest?",
                 "The number line below shows the distance between the Sun and Saturn. On the number line, mark the "
                 "relative position of the Earth."],
       teach=["Predict first: 1.496 has the biggest coefficient, so is the Sun to Earth distance the largest?",
              "Compare exponents first: 10 to the power 11 is one tenth of 10 to the power 12.",
              "So the Sun to Earth distance, with exponent 11, is the smallest even though 1.496 looks largest.",
              "On a line from Sun to Saturn, the Earth sits at about 1.496 ÷ 14.335 of the way, about one tenth."],
       examples=[
           WE("Which is the smallest of the distances Sun to Saturn (1.4335 × 10 to the power 12 m), Saturn to Uranus "
              "(1.439 × 10 to the power 12 m) and Sun to Earth (1.496 × 10 to the power 11 m)? Where does the Earth sit "
              "on a line from the Sun to Saturn?",
              ["Two distances have exponent 12 and one has exponent 11.",
               "The exponent 11 distance is the smallest: Sun to Earth.",
               "Write both with exponent 11: Sun to Saturn is 14.335 × 10 to the power 11 m.",
               "1.496 ÷ 14.335 ≈ 0.104, so the Earth is about one tenth of the way from the Sun to Saturn."],
              "Sun to Earth is the smallest; the Earth is about one tenth of the way from the Sun to Saturn",
              ncert=["2.4.distances", "2.4.mark_earth"])],
       key_terms=["standard form", "compare", "distance"], misconceptions=["M_SCI_COEFF"], minutes=8, thin=True),
     A("T10.C5", "Write numbers in standard form", "Apply",
       "Students write 59853, 65950, 3430000 and 70040000000 in standard form by moving the decimal point and "
       "counting the places moved.",
       textbook=["Express the following numbers in standard form. (i) 59853 (ii) 65950 (iii) 3430000 "
                 "(iv) 70040000000"],
       teach=["Predict first: what is the exponent of 10 for 3430000?",
              "Place the point after the first digit and count the digits after it.",
              "Drop zeroes at the end of the coefficient: 6.5950 becomes 6.595."],
       examples=[
           WE("Write 59853, 65950, 3430000 and 70040000000 in standard form.",
              ["59853: the point moves 4 places, so 5.9853 × 10⁴.",
               "65950: 4 places, so 6.595 × 10⁴.",
               "3430000: 6 places, so 3.43 × 10 to the power 6.",
               "70040000000: 10 places, so 7.004 × 10 to the power 10."],
              "5.9853 × 10⁴, 6.595 × 10⁴, 3.43 × 10 to the power 6 and 7.004 × 10 to the power 10",
              ncert=["2.4.standard_form"])],
       key_terms=["standard form"], misconceptions=["M_SCI_COEFF"], minutes=6, thin=True),
     DOER("T10.C6", "Practice: compare powers and numbers in standard form", "power_comparison_duel", "Evaluate",
          "Students decide the greater of two powers with a reason, scale a given square to decimals and larger "
          "numbers, and choose the correct total of two populations of about 10 to the power 9.",
          ["Compare numbers in standard form by the exponent first, then by the coefficient.",
           "A bigger base does not always mean a bigger power."],
          items=[
              FIO("FiO2.q8", "Figure it Out (power play, question 8)",
                  "Identify the greater number in each of the following: (i) 4³ or 3⁴ (ii) 2 to the power 8 or 8² "
                  "(iii) 100² or 2 to the power 100",
                  ["(i) 4³ = 64 and 3⁴ = 81, so 3⁴ is greater.",
                   "(ii) 2 to the power 8 is 256 and 8² is 64, so 2 to the power 8 is greater.",
                   "(iii) 100² = 10000, while 2 to the power 100 is more than 2 to the power 14, which is 16384.",
                   "So 2 to the power 100 is far greater."],
                  "(i) 3⁴ (ii) 2 to the power 8 (iii) 2 to the power 100"),
              FIO("FiO2.q6", "Figure it Out (power play, question 6)",
                  "If 12² = 144, what is (i) (1.2)² (ii) (0.12)² (iii) (0.012)² (iv) 120²?",
                  ["(i) 1.2 is 12 ÷ 10, so (1.2)² is 144 ÷ 100, which is 1.44.",
                   "(ii) 0.12 is 12 ÷ 100, so (0.12)² is 144 ÷ 10000, which is 0.0144.",
                   "(iii) 0.012 is 12 ÷ 1000, so (0.012)² is 144 ÷ 1000000, which is 0.000144.",
                   "(iv) 120 is 12 × 10, so 120² is 144 × 100, which is 14400."],
                  "(i) 1.44 (ii) 0.0144 (iii) 0.000144 (iv) 14400"),
              FIO("FiO2.q12", "Figure it Out (power play, question 12)",
                  "The worldwide population of sheep (2024) is about 10 to the power 9, and that of goats is also about "
                  "the same. What is the total population of sheep and goats? (i) 20 to the power 9 (ii) 10 to the power "
                  "11 (iii) 10 to the power 10 (iv) 10 to the power 18 (v) 2 × 10 to the power 9 (vi) 10 to the power 9 "
                  "+ 10 to the power 9",
                  ["Adding two equal amounts doubles: 1 billion and 1 billion make 2 billion.",
                   "10 to the power 9 + 10 to the power 9 is 2 × 10 to the power 9, so (v) and (vi) are the same number.",
                   "20 to the power 9, 10 to the power 10, 10 to the power 11 and 10 to the power 18 multiply instead of "
                   "adding, and are far too large.",
                   "The book lists only (vi), but (v) is equally correct."],
                  "(v) 2 × 10 to the power 9, which is the same as (vi)"),
              FIO("tremendous_ten", "Tremendous in Ten! (game)",
                  "In a game, each player has 10 seconds to write the larger number. Roxie wrote 10000000000000 and "
                  "Estu wrote 999999 × 999999. Whose number is greater? In Round 2, Roxie wrote 10 to the power 1000 "
                  "four times added, and Estu wrote 10 to the power 1000000 × 9000. Whose is greater?",
                  ["Roxie's number is 1 followed by 13 zeroes, which is 10 to the power 13.",
                   "Estu's 999999 is less than 10 to the power 6, so his product is less than (10 to the power 6)², "
                   "which is 10 to the power 12.",
                   "So Roxie wins Round 1.",
                   "Round 2: four copies of 10 to the power 1000 is 4 × 10 to the power 1000, while Estu's number has "
                   "exponent 1000000, so Estu's is far greater."],
                  "Round 1: Roxie's number; Round 2: Estu's number")],
          misconceptions=["M_BIGGER_BASE", "M_SCI_COEFF"])],
    key_terms=["powers of 10", "scientific notation", "standard form"]))

# ============================== T11 Did you ever wonder: estimation ========================================
TOPICS.append(TOPIC(
    "T11", "M6", "Did You Ever Wonder? Guess, Model, Estimate", ["2.5"], "Apply",
    "Students guess first, describe the relationships between quantities, make reasonable assumptions and estimate "
    "the worth of a Tulabhara offering, coins equal to a weight, the length of a long walk, and the steps of a ladder "
    "to the Moon.",
    "Guess, then model: write how the quantities are related, assume sensible values, compute, and compare the answer "
    "with the guess; linear growth adds the same amount each step, while exponential growth multiplies.",
    [A("T11.C1", "Tulabhara: worth of an offering", "Apply",
       "Students write the worth of jaggery equal to Roxie's weight and wheat equal to Estu's weight as weight times "
       "cost per kilogram, assume weights and prices, and compute 45 × 70 and 50 × 50 rupees.",
       textbook=["2.5 Did You Ever Wonder?",
                 "Nanjundappa wants to donate jaggery equal to Roxie's weight and wheat equal to Estu's weight. He is "
                 "wondering how much it would cost.",
                 "Worth of jaggery (in rupees) = Roxie's weight in kg × cost of 1 kg jaggery. Worth of wheat (in "
                 "rupees) = Estu's weight in kg × cost of 1 kg wheat.",
                 "Assuming Roxie's weight to be 45 kg and the cost of 1 kg of jaggery to be 70 rupees, the worth of "
                 "donated jaggery is 45 × 70 = 3150 rupees.",
                 "Assuming Estu's weight to be 50 kg and the cost of 1 kg of wheat to be 50 rupees, the worth of "
                 "donated wheat is 50 × 50 = 2500 rupees.",
                 "The practice of offering goods equal to the weight of a person, called Tulabhara or Tulabharam, is "
                 "quite old and is still followed in many places in Southern India."],
       teach=["Predict first: will the jaggery cost hundreds, thousands or lakhs of rupees?",
              "Write the relationship in words: worth is weight in kg times the cost of 1 kg.",
              "Assume values you can defend: a 13 year old might weigh about 45 kg; jaggery might cost about 70 "
              "rupees a kg.",
              "Compute and compare with the guess: 45 × 70 is 3150 rupees."],
       examples=[
           WE("Estimate the worth of jaggery equal to Roxie's weight and wheat equal to Estu's weight.",
              ["Worth of jaggery is Roxie's weight times the cost of 1 kg of jaggery.",
               "Assume 45 kg and 70 rupees a kg: 45 × 70 = 3150, so about 3150 rupees.",
               "Worth of wheat is Estu's weight times the cost of 1 kg of wheat.",
               "Assume 50 kg and 50 rupees a kg: 50 × 50 = 2500, so about 2500 rupees."],
              "About 3150 rupees of jaggery and about 2500 rupees of wheat",
              ncert=["2.5.tulabhara"])],
       key_terms=["estimate", "assumptions", "model"], misconceptions=["M_POW_COUNT"], minutes=8),
     A("T11.C2", "Coins equal to a weight", "Apply",
       "Students guess and then estimate how many 1-rupee coins balance Roxie's weight by assuming the weight of a "
       "coin, and extend it to 5-rupee coins and 10-rupee notes.",
       textbook=["Roxie wonders, \"Instead of jaggery if we use 1-rupee coins, how many coins are needed to equal my "
                 "weight?\"",
                 "1. Guessing: Make an instinctive guess of what the answer could be, without any calculations.",
                 "2. Calculating using estimation and approximation: (i) Describe the relationships among the "
                 "quantities. (ii) Make reasonable assumptions and approximations. (iii) Compute and find the answer "
                 "(and check how close your guess was).",
                 "Would the number of coins be in hundreds, thousands, lakhs, crores, or even more?",
                 "Estu asks, \"What if we use 5-rupee coins or 10-rupee notes instead? How much money could it be?\""],
       teach=["Predict first: are the coins in hundreds, thousands, lakhs or crores?",
              "Number of coins is Roxie's weight divided by the weight of one coin.",
              "Assume a 1-rupee coin weighs about 4 g and Roxie weighs 45 kg, which is 45000 g.",
              "45000 ÷ 4 = 11250, so about 11 thousand coins, worth about 11250 rupees."],
       examples=[
           WE("About how many 1-rupee coins weigh as much as Roxie, if she weighs 45 kg and a coin weighs about 4 g?",
              ["Number of coins is Roxie's weight divided by the weight of one coin.",
               "45 kg is 45000 g.",
               "45000 ÷ 4 = 11250, so about 11250 coins, which is in the thousands.",
               "With heavier 5-rupee coins there would be fewer coins but more money; with notes, far more notes."],
              "About 11250 coins, roughly 11 thousand",
              ncert=["2.5.coins_weight", "2.5.coins_notes"])],
       key_terms=["estimate", "coins", "assumptions"], misconceptions=["M_POW_COUNT"], minutes=8),
     A("T11.C3", "Long walks: padayatra and walking around the Earth", "Apply",
       "Students estimate how long a 400 km padayatra took and how many times a person could walk around the 40000 km "
       "Earth in a lifetime, stating each assumption about walking speed and time.",
       textbook=["Estu says, \"When I become an adult, I would like to donate notebooks worth my weight every year\". "
                 "Roxie says, \"When I grow up, I would like to do annadana worth my weight every year\". How many "
                 "people might benefit from each of these offerings in a year?",
                 "Roxie and Estu overheard someone saying: \"We did padayatra for about 400 km to reach this place! We "
                 "arrived early this morning.\" How long ago would they have started their journey?",
                 "How many times can a person circumnavigate the Earth in their lifetime if they walk non-stop? "
                 "Consider the distance around the Earth as 40000 km."],
       teach=["Predict first: could one person walk around the Earth once in a lifetime, ten times, or a hundred times?",
              "Assume a walking pace of about 5 km an hour and a life of about 70 years of non-stop walking.",
              "Distance walked is 5 × 24 × 365 × 70 km, which is 3066000 km.",
              "Divide by 40000 km: about 76 times around the Earth."],
       examples=[
           WE("A group walked about 400 km. If they walked about 25 km a day, how long ago did they start? How many "
              "times could a person walk around the 40000 km Earth in 70 years of non-stop walking at 5 km an hour?",
              ["Padayatra: 400 ÷ 25 = 16, so they started about 16 days ago.",
               "Distance in a lifetime: 5 km an hour for 24 hours a day, 365 days a year, for 70 years.",
               "5 × 24 × 365 × 70 = 3066000 km.",
               "3066000 ÷ 40000 ≈ 76.65, so about 76 times around the Earth."],
              "About 16 days ago; about 76 times around the Earth",
              ncert=["2.5.mt_donations", "2.5.padayatra", "2.5.circumnavigate"])],
       key_terms=["estimate", "assumptions", "distance"], misconceptions=["M_POW_COUNT"], minutes=8, thin=True),
     A("T11.C4", "Linear growth versus exponential growth", "Analyze",
       "Students count the 20 cm steps of a ladder to the Moon, about 192 crore steps, compare it with 46 folds of "
       "paper, and give examples of additive and multiplicative growth.",
       textbook=["Linear Growth vs. Exponential Growth",
                 "Roxie tells Estu about a science-fiction novel where they build a ladder to reach the moon: \"I wonder "
                 "if we actually had a ladder like that, how many steps would it have?\"",
                 "Let's assume a reasonable distance of 20 cm. We have to find out how many 20 cm make 384400 km.",
                 "If we calculate the value, we get the result as 1922000000 steps, which is 192 crore and 20 lakh "
                 "steps. The fixed increase in the distance with each step is called linear growth.",
                 "To cover the distance between the Earth and the Moon, it takes 1922000000 steps with linear growth "
                 "whereas it takes just 46 folds of a piece of paper with exponential growth! Linear growth is "
                 "additive, whereas exponential growth is multiplicative.",
                 "Can you come up with some examples of linear growth and of exponential growth?"],
       teach=["Predict first: would a ladder to the Moon have thousands, lakhs, crores or more steps?",
              "Each step adds the same 20 cm, so the number of steps is distance divided by 20 cm.",
              "384400 km is 38440000000 cm, and dividing by 20 gives 1922000000 steps.",
              "Folding multiplies by 2 each time and needs only 46 folds: multiplying beats adding."],
       examples=[
           WE("How many 20 cm steps would a ladder to the Moon, 384400 km away, have? Compare it with folding paper.",
              ["384400 km is 38440000000 cm, since 1 km is 100000 cm.",
               "Steps: 38440000000 ÷ 20 = 1922000000, which is 192 crore 20 lakh steps.",
               "Each step adds 20 cm: linear, additive growth.",
               "Each fold doubles: 46 folds reach the Moon, exponential, multiplicative growth."],
              "1922000000 steps, about 192 crore, against just 46 folds",
              ncert=["2.5.ladder", "2.5.linear_exp_examples"])],
       key_terms=["linear growth", "exponential growth"], misconceptions=["M_LINEAR_EXP"], minutes=10),
     DOER("T11.C5", "Practice: model and estimate", None, "Apply",
          "Students model a container problem as repeated addition, compute the total after 40 days, and write the "
          "answer in scientific notation.",
          ["Guess first, then write how the quantities are related.",
           "A fixed amount added each day is linear growth."],
          items=[
              FIO("FiO2.q2", "Figure it Out (power play, question 2)",
                  "There are 5 bottles in a container. Every day, a new container is brought in. How many bottles would "
                  "there be after 40 days?",
                  ["Each day adds one container of 5 bottles: the same amount added each day, linear growth.",
                   "After 40 days: 5 × 40 = 200 bottles.",
                   "In scientific notation 200 is 2 × 10²."],
                  "200 bottles, which is 2 × 10²")],
          misconceptions=["M_LINEAR_EXP"])],
    key_terms=["estimate", "assumptions", "linear growth"]))

# ============================== T12 Getting a sense for large numbers ======================================
TOPICS.append(TOPIC(
    "T12", "M6", "Getting a Sense for Large Numbers", ["2.5"], "Apply",
    "Students write animal populations and other counts as powers of 10, compute ratios such as ants per human in "
    "scientific notation, express ages in days, hours and seconds, and place events on a time scale of powers of 10.",
    "Powers of 10 put counts from 2 rhinos to 10 to the power 25 drops of water on one scale, and turn ages and "
    "timelines into seconds that can be compared by their exponents.",
    [A("T12.C1", "Populations as powers of 10", "Apply",
       "Students connect lakh, crore and arab to powers of 10, write animal populations such as starlings and "
       "mosquitoes in scientific notation, and estimate the number of people for every African elephant.",
       textbook=["Getting a Sense for Large Numbers",
                 "A lakh is 10 to the power 5 (100000), a crore is 10 to the power 7 (10000000), and an arab is 10 to "
                 "the power 9, whereas a million is 10 to the power 6 and a billion is 10 to the power 9.",
                 "As of mid-2025, there are only two northern white rhinos remaining in the world. There are just 242 "
                 "Kakapo alive. As of 2018, there are around 4.15 lakh African elephants.",
                 "The estimated global population of starlings is around 1.3 arab or 1.3 billion. The global human "
                 "population as of 2025 is 8.2 arab or 8.2 billion.",
                 "The estimated mosquito population worldwide (2023) is 11 neel or 110 trillion.",
                 "With a global human population of about 8 × 10 to the power 9 and about 4 × 10 to the power 5 African "
                 "elephants, can we say that there are nearly 20000 people for every African elephant?"],
       teach=["Predict first: are there more starlings or more people in the world?",
              "1.3 billion starlings is 1.3 × 10 to the power 9; people are 8.2 × 10 to the power 9, so more people.",
              "110 trillion mosquitoes is 1.1 × 10 to the power 14.",
              "People per elephant: 8 ÷ 4 is 2, and 9 − 5 is 4, so 2 × 10⁴, which is 20000."],
       examples=[
           WE("Write the starling and mosquito populations in scientific notation, and check that there are about "
              "20000 people for every African elephant.",
              ["1.3 billion is 1300000000, which is 1.3 × 10 to the power 9 starlings.",
               "110 trillion is 110000000000000, which is 1.1 × 10 to the power 14 mosquitoes.",
               "People per elephant: 8 × 10 to the power 9 divided by 4 × 10 to the power 5.",
               "Divide the coefficients, 8 ÷ 4 = 2, and subtract the exponents, 9 − 5 = 4: 2 × 10⁴ = 20000."],
              "1.3 × 10 to the power 9 starlings, 1.1 × 10 to the power 14 mosquitoes, and yes, about 20000 people per "
              "elephant",
              ncert=["2.5.lakh_crore_arab", "2.5.species", "2.5.starling_mosquito", "2.5.per_elephant"])],
       key_terms=["powers of 10", "population", "scientific notation"], misconceptions=["M_SCI_COEFF"], minutes=10),
     A("T12.C2", "Calculating with numbers in scientific notation", "Apply",
       "Students find ants per human, flocks of starlings, leaves on all trees and sheets of paper to the Moon, "
       "calculating in scientific notation: they multiply or divide the coefficients and combine the exponents.",
       textbook=["The estimated population of ants globally is 20 padma or 20 quadrillion (2 × 10 to the power 16).",
                 "The estimated number of trees (2023) globally stands at 3 trillion (3 × 10 to the power 12).",
                 "Calculate and write the answer using scientific notation: (i) How many ants are there for every "
                 "human in the world? (ii) If a flock of starlings contains 10000 birds, how many flocks could there "
                 "be in the world? (iii) If each tree had about 10⁴ leaves, find the total number of leaves on all the "
                 "trees in the world. (iv) If you stacked sheets of paper on top of each other, how many would you "
                 "need to reach the Moon?"],
       teach=["Predict first: are there more ants per person or more leaves per tree?",
              "To divide, divide the coefficients and subtract the exponents; to multiply, multiply and add.",
              "Ants per human: 2 × 10 to the power 16 over 8 × 10 to the power 9 gives 0.25 × 10 to the power 7.",
              "Write 0.25 × 10 to the power 7 in standard form as 2.5 × 10 to the power 6."],
       examples=[
           WE("Find, in scientific notation, the ants per human, the flocks of 10000 starlings, the leaves on all "
              "trees, and the sheets of paper (0.001 cm thick) needed to reach the Moon 384400 km away.",
              ["Ants per human: 2 ÷ 8 = 0.25 and 16 − 9 = 7, so 0.25 × 10 to the power 7, which is 2.5 × 10 to the "
               "power 6.",
               "Flocks: 1.3 × 10 to the power 9 divided by 10⁴ is 1.3 × 10 to the power 5.",
               "Leaves: 3 × 10 to the power 12 times 10⁴ is 3 × 10 to the power 16.",
               "Sheets: 384400 km is 3.844 × 10 to the power 10 cm, and each sheet is 10 to the power −3 cm, so "
               "3.844 × 10 to the power 13 sheets."],
              "2.5 × 10 to the power 6 ants per human, 1.3 × 10 to the power 5 flocks, 3 × 10 to the power 16 leaves, "
              "3.844 × 10 to the power 13 sheets",
              ncert=["2.5.calc_four"])],
       key_terms=["scientific notation", "multiply", "divide"], misconceptions=["M_SCI_COEFF"], minutes=10),
     A("T12.C3", "A different way to say your age", "Apply",
       "Students turn Roxie's 4840 days into hours, decide what her 6970710 means, find Estu's birthday from 4070 "
       "days, and work out how old someone is after a million seconds.",
       textbook=["A different way to say your age!",
                 "\"I'm 4840 days old today!\" said Roxie. \"I'm ______ hours old!\" said Roxie. Make an estimate "
                 "before finding this number.",
                 "Roxie says, \"I am 6970710 ... old\". What could this number mean? Find out!",
                 "Estu: \"I am 4070 days old today. Can you find out my date of birth?\"",
                 "If you have lived for a million seconds, how old would you be?"],
       teach=["Predict first: is a million seconds a few days, a few months or a few years?",
              "Hours: 4840 days × 24 hours a day is 116160 hours.",
              "6970710 is too big for hours; in minutes, 4840 days is 4840 × 24 × 60, about 6969600, so it is minutes.",
              "A day has 86400 seconds, so a million seconds is about 11.57 days, less than two weeks."],
       examples=[
           WE("Roxie is 4840 days old. Find her age in hours, decide what unit 6970710 is in, find Estu's age in years "
              "for 4070 days, and find how many days a million seconds is.",
              ["Hours: 4840 × 24 = 116160 hours.",
               "Minutes: 6970710 ÷ 1440 is about 4840.8 days, so 6970710 is Roxie's age in minutes.",
               "Estu: 4070 ÷ 365 is 11 with 55 days left; allowing about 3 leap days, he is 11 years and about 52 days "
               "old, so count back that far from today.",
               "A day has 24 × 60 × 60 = 86400 seconds, and 1000000 ÷ 86400 ≈ 11.57 days."],
              "116160 hours; 6970710 minutes; Estu is about 11 years and 52 days old; a million seconds is about 11.6 "
              "days",
              ncert=["2.5.age_hours", "2.5.age_puzzle", "2.5.estu_birth", "2.5.million_seconds"])],
       key_terms=["age", "seconds", "estimate"], misconceptions=["M_POW_COUNT"], minutes=8, thin=True),
     A("T12.C4", "A time scale in powers of 10 seconds", "Analyze",
       "Students place events from a falling ball to the age of the Earth on a time scale of powers of 10 seconds, "
       "convert two ancient ages to seconds, and estimate two very long times.",
       textbook=["Time in seconds, compared to real-world events: 10 to the power 0 seconds, time taken for a ball thrown "
                 "up to fall back; 10 to the power 1 seconds, time blood takes to complete one circulation; about 10² "
                 "seconds, making a cup of tea.",
                 "10 to the power 5 seconds is about 1.16 days and 10 to the power 6 seconds is about 11.57 days.",
                 "Notice how rapid exponential growth is: 10 to the power 6 seconds is less than a fortnight, but 10 to "
                 "the power 9 seconds is a whopping 31 years.",
                 "A fossil of a terror bird is dated to 15 million years ago. Plants on land started 47 crore years "
                 "ago.",
                 "Calculate and write the answer using scientific notation: (i) If one star is counted every second, "
                 "how long would it take to count all the stars in the universe? (ii) If one could drink a glass of "
                 "water (200 ml) every 10 seconds, how long would it take to finish the entire volume of water on "
                 "Earth?"],
       teach=["Predict first: is 10 to the power 9 seconds closer to a month, a year or a lifetime?",
              "A year is about 3.15 × 10 to the power 7 seconds, so multiply years by that.",
              "15 million years is about 4.7 × 10 to the power 14 seconds; 47 crore years is about 1.5 × 10 to the "
              "power 16 seconds.",
              "Each step up the scale multiplies by 10, so a few steps take us from days to lifetimes."],
       examples=[
           WE("Convert 15 million years to seconds. How long would it take to count 2 × 10 to the power 23 stars at one "
              "per second, and to drink 2 × 10 to the power 25 drops of water (16 drops per ml) at 200 ml every 10 "
              "seconds?",
              ["One year is about 3.15 × 10 to the power 7 seconds.",
               "15 million years: 1.5 × 10 to the power 7 years times 3.15 × 10 to the power 7 s, about 4.7 × 10 to the "
               "power 14 seconds.",
               "Stars: one per second, so 2 × 10 to the power 23 seconds.",
               "Water: 2 × 10 to the power 25 drops is 1.25 × 10 to the power 24 ml, which is 6.25 × 10 to the power "
               "21 glasses; at 10 seconds a glass that is 6.25 × 10 to the power 22 seconds."],
              "About 4.7 × 10 to the power 14 seconds; 2 × 10 to the power 23 seconds; 6.25 × 10 to the power 22 "
              "seconds",
              ncert=["2.5.time_table", "2.5.events_order", "2.5.terror_plants", "2.5.try_stars_water"])],
       key_terms=["time scale", "seconds", "powers of 10"], misconceptions=["M_POW_COUNT"], minutes=10),
     DOER("T12.C5", "Practice: large numbers in scientific notation", "standard_form_fixer", "Apply",
          "Students estimate totals such as clothes, honeybees, bacteria and eating time in scientific notation, and "
          "find the date one billion seconds ago.",
          ["Multiply coefficients and add exponents; then put the answer in standard form.",
           "A day has 86400 seconds and a year about 3.15 × 10 to the power 7 seconds."],
          items=[
              FIO("FiO2.q13", "Figure it Out (power play, question 13)",
                  "Calculate and write the answer in scientific notation: (i) If each person in the world had 30 pieces "
                  "of clothing, find the total number of pieces of clothing. (ii) There are about 100 million bee "
                  "colonies in the world. Find the number of honeybees if each colony has about 50000 bees. (iii) The "
                  "human body has about 38 trillion bacterial cells. Find the bacterial population residing in all "
                  "humans in the world. (iv) Total time spent eating in a lifetime in seconds.",
                  ["(i) 8.2 × 10 to the power 9 people times 30 is 246 × 10 to the power 9, which is 2.46 × 10 to the "
                   "power 11.",
                   "(ii) 10 to the power 8 colonies times 5 × 10⁴ bees is 5 × 10 to the power 12.",
                   "(iii) 3.8 × 10 to the power 13 cells times 8.2 × 10 to the power 9 people is 31.16 × 10 to the "
                   "power 22, which is 3.116 × 10 to the power 23.",
                   "(iv) Assume 1 hour of eating a day for 70 years: 3600 × 365 × 70 = 91980000 seconds, which is "
                   "9.198 × 10 to the power 7."],
                  "(i) 2.46 × 10 to the power 11 (ii) 5 × 10 to the power 12 (iii) 3.116 × 10 to the power 23 "
                  "(iv) about 9.198 × 10 to the power 7 seconds"),
              FIO("FiO2.q14", "Figure it Out (power play, question 14)",
                  "What was the date 1 arab or 1 billion seconds ago?",
                  ["A day has 86400 seconds.",
                   "1000000000 ÷ 86400 ≈ 11574 days.",
                   "11574 ÷ 365 is about 31.7 years.",
                   "Count back about 31 years and 8 months from today's date."],
                  "About 11574 days, or about 31.7 years, before today")],
          misconceptions=["M_SCI_COEFF", "M_POW_COUNT"])],
    key_terms=["large numbers", "powers of 10", "scientific notation"]))

# ============================== T13 A pinch of history =====================================================
TOPICS.append(TOPIC(
    "T13", "M6", "A Pinch of History: Names for Powers of 10", ["2.5"], "Understand",
    "Students trace Indian number names for powers of 10 from the Lalitavistara onwards, build the Indian and "
    "international naming systems by multiplying by 100 and by 1000, and meet the googol and googolplex.",
    "Indian texts named powers of 10 up to 10 to the power 140 long ago; Indian names step up by 100 and "
    "international names by 1000, so their exponents grow by 2 and by 3.",
    [A("T13.C1", "Indian names for powers of 10", "Understand",
       "Students read the Lalitavistara's names for odd powers of 10 up to 10 to the power 53, and build lakh, crore, "
       "arab, kharab and neel by multiplying by 100, so each exponent grows by 2.",
       textbook=["2.5 A Pinch of History",
                 "In the Lalitavistara, a Buddhist treatise from the first century BCE, we see number-names for odd "
                 "powers of ten up to 10 to the power 53.",
                 "\"Hundred kotis are called an ayuta (10 to the power 9), hundred ayutas a niyuta (10 to the power 11), "
                 "hundred niyutas a kankara (10 to the power 13), ..., a hundred vibhutangamas is a tallakshana (10 to "
                 "the power 53).\"",
                 "Mahaviracharya gives a list of 24 terms in his treatise Ganita-sara-sangraha. An anonymous Jaina "
                 "treatise Amalasiddhi gives a name for each power of ten up to 10 to the power 96. A Pali grammar "
                 "treatise of Kaccayana lists number-names up to 10 to the power 140.",
                 "A hundred thousand is a lakh: 100 × 1000 = 100000, and 10² × 10³ is 10 to the power 5. A hundred lakhs is a "
                 "crore. A hundred crores is an arab. A hundred arab is a kharab.",
                 "Continuing this, a hundred kharab is a neel, a hundred neel is a padma, a hundred padma is a shankh "
                 "and a hundred shankh is a maha shankh."],
       teach=["Predict first: how many zeroes does a crore have, and how many does an arab have?",
              "Each new Indian name is a hundred of the previous one, so multiply by 10².",
              "Multiplying by 10² adds 2 to the exponent: lakh 10 to the power 5, crore 10 to the power 7, arab 10 to "
              "the power 9.",
              "The Lalitavistara's names also step by a hundred, so they cover the odd powers up to 10 to the power 53."],
       examples=[
           WE("Starting from a lakh as 10² × 10³, find the powers of 10 for a crore, an arab, a kharab and a neel.",
              ["A lakh is 100 × 1000 = 100000, which is 10 to the power 2 + 3, 10 to the power 5.",
               "A crore is 100 lakh: 10² × 10 to the power 5 gives 10 to the power 7.",
               "An arab is 100 crore: 10 to the power 9. A kharab is 100 arab: 10 to the power 11.",
               "A neel is 100 kharab: 10 to the power 13."],
              "Crore 10 to the power 7, arab 10 to the power 9, kharab 10 to the power 11, neel 10 to the power 13",
              ncert=["hist.lalitavistara", "hist.indian_names"])],
       key_terms=["number names", "powers of 10"], misconceptions=["M_POW_COUNT"], minutes=8),
     A("T13.C2", "International names, googol and googolplex", "Understand",
       "Students build million, billion and trillion by multiplying by 1000, so each exponent grows by 3, and meet "
       "the googol, 10 to the power 100, the googolplex, and record banknotes.",
       textbook=["In the American or International system, we say: A thousand thousand is a million, 10³ × 10³ is 10 to "
                 "the power 6. A thousand million is a billion, 10³ × 10 to the power 6 is 10 to the power 9. A thousand "
                 "billion is a trillion, 10 to the power 12.",
                 "Continuing this, a thousand trillion is a quadrillion (10 to the power 15). Observe the names "
                 "million, billion, trillion, quadrillion, quintillion, sextillion, septillion, octillion, nonillion, "
                 "decillion.",
                 "The number 10 to the power 100 is also called a googol. The estimated number of atoms in the universe "
                 "is 10 to the power 78 to 10 to the power 82. The number 10 to the power googol is called a "
                 "googolplex.",
                 "The highest numerical value banknote ever printed was a special note valued 1 sextillion pengo (10 to "
                 "the power 21) printed in Hungary in 1946. In 2009, Zimbabwe printed a 100 trillion (10 to the power "
                 "14) Zimbabwean dollar note."],
       teach=["Predict first: is a googol more or less than the number of atoms in the universe?",
              "Each international name is a thousand of the previous one, so multiply by 10³ and add 3 to the "
              "exponent.",
              "Million 10 to the power 6, billion 10 to the power 9, trillion 10 to the power 12, quadrillion 10 to the "
              "power 15.",
              "A googol, 10 to the power 100, is far more than 10 to the power 82 atoms."],
       examples=[
           WE("Find the powers of 10 for a billion, a trillion and a quintillion, and compare a googol with the number "
              "of atoms in the universe.",
              ["A million is 1000 × 1000, which is 10 to the power 6.",
               "A billion is a thousand million: 10 to the power 6 + 3, 10 to the power 9.",
               "A trillion is 10 to the power 12, a quadrillion 10 to the power 15 and a quintillion 10 to the power 18.",
               "A googol is 10 to the power 100; the atoms are at most 10 to the power 82, so a googol is 10 to the "
               "power 18 times as many."],
              "Billion 10 to the power 9, trillion 10 to the power 12, quintillion 10 to the power 18; a googol is far "
              "larger",
              ncert=["hist.western_names", "hist.googol_notes"])],
       key_terms=["number names", "googol"], misconceptions=["M_POW_COUNT"], minutes=8),
     DOER("T13.C3", "Practice: decode the number names", None, "Analyze",
          "Students work out what the first part of each international number name denotes by writing each name as "
          "a power of 1000 times 1000.",
          ["International names step up by 1000, adding 3 to the exponent.",
           "Indian names step up by 100, adding 2 to the exponent."],
          items=[
              FIO("hist.first_part", "A pinch of history: the names",
                  "Observe the names million (10 to the power 6), billion (10 to the power 9), trillion (10 to the power "
                  "12), quadrillion (10 to the power 15), quintillion (10 to the power 18). What does the first part of "
                  "each name denote?",
                  ["Write each as 1000 multiplied by more 1000s: a billion is 1000 × 1000 × 1000.",
                   "bi means 2: a billion is 1000 with 2 more 1000s multiplied, 10 to the power 3 + 3 × 2.",
                   "tri means 3: a trillion is 10 to the power 3 + 3 × 3, which is 10 to the power 12.",
                   "quadri means 4 and quinti means 5, giving 10 to the power 15 and 10 to the power 18."],
                  "The first part counts how many times 1000 is multiplied onto 1000: bi 2, tri 3, quadri 4, quinti 5")],
          misconceptions=["M_POW_COUNT"])],
    key_terms=["number names", "powers of 10"]))

# ============================== T14 Summary ================================================================
TOPICS.append(TOPIC(
    "T14", "M6", "Summary: Power Play", ["Summary"], "Remember",
    None,
    "Exponents write repeated multiplication compactly; their rules hold for all integer exponents, scientific "
    "notation makes very large numbers readable, and estimation shows how large a quantity is.",
    [A("T14.C1", "What powers did in this chapter", "Remember",
       "Students restate the meaning of a power, the exponent rules for products, quotients, powers of powers and "
       "zero and negative exponents, and the standard form for large numbers.",
       textbook=["We analysed some situations, asked questions, and found answers by first guessing, then modelling the "
                 "problem statement, followed by making assumptions and approximations to carry out the calculations.",
                 "We experienced how rapid exponential growth, also called multiplicative growth, can be compared to "
                 "additive growth.",
                 "n to the power a is n × n × n × ... × n (n multiplied by itself a times), and n to the power −a is 1 "
                 "over n to the power a.",
                 "Operations with exponents satisfy: n to the power a × n to the power b = n to the power a + b; "
                 "(n to the power a) to the power b = n to the power a × b; n to the power a ÷ n to the power b = n to "
                 "the power a − b; n to the power a × m to the power a = (n × m) to the power a; n to the power a ÷ m "
                 "to the power a = (n ÷ m) to the power a; n to the power 0 is 1 (n ≠ 0).",
                 "The scientific notation for the number 308100000 is 3.081 × 10 to the power 8. The standard form of "
                 "any number is x × 10 to the power y, where x ≥ 1 and x < 10, and y is an integer.",
                 "Engaging in interesting thought experiments can be used as means to understand how large a number "
                 "or a quantity is."],
       teach=["Our opening question is settled: 46 folds of a 0.001 cm sheet give about 7 lakh km, beyond the Moon.",
              "A power counts factors; the rules for exponents come from counting factors and cancelling them.",
              "Standard form puts the size of a number in its exponent of 10.",
              "Still open for you: play Tremendous in Ten with a friend and find the largest number you can write."],
       ncert=["summary"], video_focus=["RECAP"], minutes=8)],
    topic_type="summary"))
