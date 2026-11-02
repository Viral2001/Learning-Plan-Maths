# -*- coding: utf-8 -*-
"""Topics T8 to T11 (module M3). Book section 3.4 Place Value Representation and the Summary, pp 69 to 81.
Base-60 numerals are written with the book's own device: the Hindu numerals 1 to 59 stand for the digit groups,
and a bar | separates the places (written here for the reader; the Mesopotamians used spacing only).
Mayan numerals use a dot for 1, a bar for 5 and a shell for the empty place; landmarks 1, 20, 360, 7200."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T8 Place value: the Mesopotamian system =====================================
TOPICS.append(TOPIC(
    "T8", "M3", "Place Value: The Mesopotamian System", ["3.3", "3.4"], "Apply",
    "Students explain why the Egyptian system runs out of symbols, group numbers into powers of 60, regroup when a "
    "power of 60 appears 60 or more times, and write numbers in a base-60 place value system where position alone "
    "tells the landmark.",
    "A base needs a new symbol for every new landmark. The Mesopotamians grouped in powers of 60 and then dropped the "
    "landmark symbols: the position of each group tells whether it counts 1s, 60s or 3600s. That is place value.",
    [A("T8.C1", "Base 60 with our own symbols", "Apply",
       "Students explain why a base with a symbol for every landmark needs endless symbols, group a number such as "
       "4000 into powers of 60, and write it with the numerals 1 to 59 and the landmark symbols.",
       textbook=["III. Shortcomings of the Egyptian System",
                 "If larger and larger numbers needed to be represented, then there was a need for inventing an "
                 "unending sequence of symbols for higher and higher powers of 10.",
                 "3.4 Place Value Representation. I. The Mesopotamian Number System",
                 "In later times, it became a base-60 system, also called the sexagesimal system, with a very "
                 "efficient number representation.",
                 "The influence of the Mesopotamian sexagesimal system, also known as the Babylonian number system, "
                 "can be seen even now in our units of time measurements: 1 hour is 60 minutes and 1 minute is 60 "
                 "seconds.",
                 "Note that we have actually used Indian numerals in creating these symbols.",
                 "Example: Let us represent the number 640 in this system. Grouping it into landmark numbers, we see "
                 "that 640 = (10) × 60 + 40.",
                 "Example: Let us try another number, 7530. 7530 = (2) × 3600 + (5) × 60 + 30."],
       teach=["Predict first: the Egyptians stopped at a symbol for 10000000; what happens to a bigger number?",
              "Every new landmark in a base needs a new symbol, so the symbols never end.",
              "The Mesopotamians grouped in powers of 60: 1, 60, 3600 and so on; we still use 60 in hours and "
              "minutes.",
              "We borrow our numerals 1 to 59 for the count of each power of 60, like ten 60s and one 40 for 640."],
       examples=[
           WE("Group 4000 into powers of 60 and say how it is written in base 60 with our own symbols.",
              ["The landmarks are 1, 60 and 3600; 216000 is far too big.",
               "One 3600 fits in 4000: 4000 − 3600 = 400.",
               "Six 60s fit in 400: 6 × 60 = 360, and 400 − 360 = 40.",
               "So 4000 = (1) × 3600 + (6) × 60 + 40.",
               "It is written as 1 with the 3600 symbol, 6 with the 60 symbol, and 40."],
              "4000 = (1) × 3600 + (6) × 60 + 40",
              ncert=["3.3.egypt_shortcoming", "3.4.base60_why", "3.4.time_units", "3.4.own_symbols",
                     "3.4.meso_640", "3.4.meso_7530"])],
       key_terms=["sexagesimal", "base 60"], misconceptions=["M_BASE_TEN_ONLY"], minutes=10),
     A("T8.C2", "Regrouping 60 of a landmark", "Apply",
       "Students regroup a base-60 grouping in which a power of 60 occurs 60 or more times, so that every count is "
       "from 1 to 59.",
       textbook=["Note that when a number is grouped into powers of 60 for its representation, no power of 60 can "
                 "occur 60 or more times. If this happens, then 60 of them can be grouped to form the next power of "
                 "60.",
                 "(1) × 3600 + (70) × 60 + 2 = (1) × 3600 + (60 + 10) × 60 + 2 = (2) × 3600 + (10) × 60 + 2.",
                 "Therefore, any number can be represented using the numerals from 1 to 59, along with the numerals "
                 "for landmark numbers."],
       teach=["Predict first: is 75 sixties allowed in a base-60 numeral?",
              "60 sixties make one 3600, so a count of 60 or more must be regrouped.",
              "Take 60 out of the count and add 1 to the next landmark.",
              "Every count then lies from 1 to 59."],
       examples=[
           WE("Regroup (2) × 3600 + (75) × 60 + 10 so that no count is 60 or more.",
              ["75 sixties is 60 sixties and 15 sixties.",
               "60 sixties make one 3600, so the 3600s go from 2 to 3.",
               "So (2) × 3600 + (75) × 60 + 10 = (3) × 3600 + (15) × 60 + 10.",
               "Both are 11710: 7200 + 4500 + 10 and 10800 + 900 + 10."],
              "(3) × 3600 + (15) × 60 + 10, which is 11710",
              ncert=["3.4.meso_regroup"])],
       key_terms=["regroup", "base 60"], misconceptions=["M_TEN_SYMBOLS_OK"], minutes=5, thin=True),
     A("T8.C3", "Position decides the landmark", "Analyze",
       "Students drop the landmark symbols and read a base-60 numeral by position, the rightmost group counting 1s, "
       "the next 60s and the next 3600s, and define a place value system.",
       textbook=["Now, what if we make the representation even more compact by dropping the symbols for the different "
                 "powers of 60 altogether?",
                 "This is exactly what the Mesopotamians did! In their numeral, the rightmost set of symbols showed "
                 "the number of 1s, the set of symbols to its left showed the number of 60s, the next showed the "
                 "number of 3600s and so on. Whenever there was no occurrence of a power of 60, a blank space was "
                 "given in that position.",
                 "Such a number system (having a base) that makes use of the position of each symbol in determining "
                 "the landmark number that it is associated with is called a positional number system or a place "
                 "value system.",
                 "This idea of place value marks the highest point in the history of evolution of number systems."],
       teach=["Predict first: if the landmark symbols are dropped, how can a reader still tell 60s from 1s?",
              "The place tells the landmark: rightmost 1s, next 60s, next 3600s.",
              "So only the numerals 1 to 59 are needed, never a new symbol for a bigger landmark.",
              "A system with a base where position gives the landmark is a place value system."],
       examples=[
           WE("Write 3725 in the Mesopotamian place value system, using our numerals for each place.",
              ["One 3600 fits: 3725 − 3600 = 125.",
               "Two 60s fit in 125: 125 − 120 = 5.",
               "So 3725 = (1) × 3600 + (2) × 60 + 5.",
               "Dropping the landmark symbols, it is written 1 | 2 | 5: 1 in the 3600s place, 2 in the 60s place, 5 "
               "in the 1s place."],
              "1 | 2 | 5, from 3725 = (1) × 3600 + (2) × 60 + 5",
              ncert=["3.4.drop_symbols", "3.4.place_value_def"])],
       key_terms=["place value", "positional number system"], misconceptions=["M_POSITION_SAME"], minutes=8),
     DOER("T8.C4", "Practice: write numbers in base 60", "base60_board", "Apply",
          "Students write numbers in the Mesopotamian place value system, including numbers with an empty place.",
          ["Group into powers of 60: 1, 60, 3600, ...",
           "Write the count of each power in its place; an empty place was left blank."],
          items=[
              FIO("FiOH.q1", "Figure it Out (Mesopotamian numerals, question 1)",
                  "Represent the following numbers in the Mesopotamian system: (i) 63 (ii) 132 (iii) 200 (iv) 60 "
                  "(v) 3605",
                  ["(i) 63 = (1) × 60 + 3, written 1 | 3. (ii) 132 = (2) × 60 + 12, written 2 | 12.",
                   "(iii) 200 = (3) × 60 + 20, written 3 | 20.",
                   "(iv) 60 = (1) × 60, so the 1s place is empty: written 1 followed by a blank.",
                   "(v) 3605 = (1) × 3600 + 5, so the 60s place is empty: written 1 | blank | 5."],
                  "(i) 1 | 3 (ii) 2 | 12 (iii) 3 | 20 (iv) 1 | blank (v) 1 | blank | 5")],
          misconceptions=["M_POSITION_SAME", "M_BLANK_NOTHING"])],
    key_terms=["place value", "base 60", "sexagesimal"]))

# ============================== T9 The empty place ==========================================================
TOPICS.append(TOPIC(
    "T9", "M3", "The Empty Place: Mesopotamian, Mayan and Chinese Numerals", ["3.4"], "Analyze",
    "Students show how blank spaces make Mesopotamian numerals ambiguous, read and write Mayan numerals with the "
    "shell placeholder and landmarks 1, 20, 360, and read Chinese rod numerals in base 10 with a blank for an empty "
    "place.",
    "A place value system must show an empty place, or the same numeral can be read in different ways. The later "
    "Mesopotamians and the Mayans used a placeholder symbol; the Chinese rod numerals left a blank, made easier to "
    "see by alternating vertical and horizontal rods.",
    [A("T9.C1", "Blanks make numerals ambiguous", "Analyze",
       "Students show that a base-60 numeral with blanks or uneven spacing can stand for different numbers, such as "
       "2 | 5 for 125 or 7205, and explain why a placeholder symbol is needed.",
       textbook=["The Mesopotamian system however cannot be considered a fully developed place value system. It has "
                 "certain defects that lead to confusion while reading a number.",
                 "Look at the representation of 60. What will be the representation for 3,600?",
                 "Because of the ambiguity in finding which symbols correspond to which powers of 60, the same "
                 "numeral can be read in different ways.",
                 "To address the issue arising out of blank spaces, the later Mesopotamians used a brilliant idea of "
                 "assigning a 'placeholder' symbol to denote a blank space. This is like the 0 (zero) we use in our "
                 "system.",
                 "The placeholder symbol was primarily used in the middle of numbers and not at the end; so they "
                 "would not use it to represent a number like (what we would write as) 3600."],
       teach=["Predict first: 1, 60 and 3600 in Mesopotamian numerals, can you tell them apart?",
              "1 is a single 1; 60 is 1 with an empty 1s place; 3600 is 1 with two empty places: all look like a "
              "lone 1.",
              "A blank in the middle is easy to miss, so 2 with 5 could mean two 60s and 5, or two 3600s and 5.",
              "The later Mesopotamians drew a placeholder for the empty place, which is the job our 0 does."],
       examples=[
           WE("A Mesopotamian numeral shows 2 and then 5, with a gap between them that might hide an empty place. What "
              "two numbers could it be?",
              ["If there is no empty place, 2 counts 60s and 5 counts 1s: 2 × 60 + 5 = 125.",
               "If an empty 60s place is hidden in the gap, 2 counts 3600s: 2 × 3600 + 5 = 7205.",
               "The same marks give 125 or 7205.",
               "A placeholder written in the empty place would remove the doubt."],
              "125 or 7205; only a placeholder for the empty place settles it",
              ncert=["3.4.meso_defects", "3.4.blank_ambiguity", "3.4.placeholder"])],
       key_terms=["placeholder", "ambiguity"], misconceptions=["M_BLANK_NOTHING"], minutes=8),
     A("T9.C2", "The Mayan system and its shell", "Apply",
       "Students read a Mayan numeral written from the bottom up with dots, bars and a shell, using the landmarks 1, "
       "20, 360 and 7200, and explain why 360 makes it not a true base-20 system.",
       textbook=["II. The Mayan Number System",
                 "In Central America, there flourished a civilisation known as the Mayan civilisation that made great "
                 "intellectual and cultural progress between the 3rd and 10th centuries CE. Among their intellectual "
                 "achievements stands their place value system designed independently of those in Asia. They also "
                 "made use of a placeholder symbol, for the modern-day '0', that looked like a seashell.",
                 "Why was their third landmark number 360 rather than 400? Some scholars feel that this might have "
                 "something to do with their calendars.",
                 "They used a dot for 1, and a bar for 5. These were used to denote numbers from 1 to 19.",
                 "The symbols associated with different landmark numbers were written one below the other with the "
                 "lowermost set of symbols corresponding to the number of 1s, the set above corresponding to the "
                 "number of 20s, the set above to the number of 360s and so on.",
                 "Because the Mayan system is not an actual base-20 system, it lacks the advantages that a system "
                 "with a base has for computations.",
                 "A curious fact is that we can still find the use of base-20 in the number names of some European "
                 "languages."],
       teach=["Predict first: if the second Mayan landmark is 20, what would a true base-20 system use as the third?",
              "The landmarks are 1, 20, 360, 7200, 144000: 20 times 20 would be 400, but the Mayans used 360.",
              "Dots and bars write 1 to 19 in each place; a shell marks an empty place; the places stack upward.",
              "On the book's card, 4 over 11 over a shell is 4 × 360 + 11 × 20 + 0, which is 1660."],
       examples=[
           WE("A Mayan numeral shows, from top to bottom, two dots, then three dots, then one bar. What number is it?",
              ["Read from the bottom: the lowest place counts 1s, the next 20s, the top 360s.",
               "The bottom is one bar, which is 5. The middle is three dots, which is 3. The top is two dots, which is "
               "2.",
               "So the number is 2 × 360 + 3 × 20 + 5.",
               "2 × 360 + 3 × 20 + 5 = 785."],
              "785",
              ncert=["3.4.mayan_intro", "3.4.mayan_card", "3.4.mayan_360", "3.4.mayan_base20_note"])],
       key_terms=["Mayan numerals", "placeholder"], misconceptions=["M_BASE_TEN_ONLY", "M_BLANK_NOTHING"],
       minutes=8),
     A("T9.C3", "Writing numbers in Mayan numerals", "Apply",
       "Students write 77, 100, 361 and 721 in Mayan numerals, using the shell wherever a place is empty.",
       textbook=["Represent the following numbers using the Mayan system: (i) 77 (ii) 100 (iii) 361 (iv) 721"],
       teach=["Predict first: which of 77, 100, 361 and 721 will need a shell?",
              "Group into 360s, then 20s, then 1s.",
              "Write each count with dots and bars, bottom place for 1s.",
              "Use a shell for any place with a count of 0."],
       examples=[
           WE("Write 77, 100, 361 and 721 in Mayan numerals.",
              ["77 = 3 × 20 + 17: three dots over three bars and two dots.",
               "100 = 5 × 20 + 0: one bar over a shell.",
               "361 = 1 × 360 + 0 × 20 + 1: one dot, a shell, one dot, from top to bottom.",
               "721 = 2 × 360 + 0 × 20 + 1: two dots, a shell, one dot."],
              "77 is 3 | 17, 100 is 5 | shell, 361 is 1 | shell | 1, 721 is 2 | shell | 1",
              ncert=["3.4.mayan_try"])],
       key_terms=["Mayan numerals", "shell"], misconceptions=["M_BLANK_NOTHING"], minutes=6, thin=True),
     A("T9.C4", "Chinese rod numerals", "Apply",
       "Students read and write Chinese rod numerals in base 10, alternating zong and heng rods from place to place, "
       "and leaving a blank for an empty place, as in 5072.",
       textbook=["III. The Chinese Number System",
                 "The Chinese used two number systems: a written system for recording quantities, and a system making "
                 "use of rods for performing computations. The numerals in the rod-based number system are called rod "
                 "numerals.",
                 "It was a decimal system (base-10).",
                 "Note: The zongs represent units, hundreds, tens of thousands, etc., and the hengs tens, thousands, "
                 "hundreds of thousands, etc.",
                 "(2) × 10³ + (6) × 10² + (3) × 10 + (4) × 1 = 2634",
                 "Like the Mesopotamians, the rod numerals used a blank space to indicate the skipping of a place "
                 "value. However, because of the slightly more uniform sizes of the symbols for one through nine, "
                 "the blank spaces were easier to locate than in the Mesopotamian system.",
                 "The Chinese system, with a symbol for zero, would be a fully developed place value system."],
       teach=["Predict first: why would the Chinese switch between vertical and horizontal rods from one place to "
              "the next?",
              "Rod numerals are base 10: units, tens, hundreds, thousands from right to left.",
              "Zong (vertical) rods are used for units, hundreds and ten thousands; heng (horizontal) rods for tens "
              "and thousands.",
              "Switching shapes shows where one place ends; an empty place is a blank, with no zero symbol."],
       examples=[
           WE("Write 5072 in Chinese rod numerals and read it back.",
              ["5072 = (5) × 10³ + (0) × 10² + (7) × 10 + (2) × 1.",
               "Thousands: 5 in heng form. Hundreds: empty, so a blank. Tens: 7 in heng form. Units: 2 in zong form.",
               "Reading back: 5 thousands, no hundreds, 7 tens, 2 units.",
               "(5) × 10³ + (0) × 10² + (7) × 10 + (2) × 1 = 5072."],
              "5 heng, a blank, 7 heng, 2 zong, which is 5072",
              ncert=["3.4.chinese_rods", "3.4.chinese_2634", "3.4.chinese_blank"])],
       key_terms=["rod numerals", "zong", "heng"], misconceptions=["M_BLANK_NOTHING"], minutes=8),
     DOER("T9.C5", "Practice: hold the empty place", "zero_breaker", "Analyze",
          "Students explain why the Chinese alternated zong and heng rods and show how a rod numeral without spaces "
          "or zero can be read in more than one way.",
          ["A place value system must show an empty place.",
           "Without a placeholder, the same marks can stand for different numbers."],
          items=[
              FIO("FiOI.q1", "Figure it Out (place value, question 1)",
                  "Why do you think the Chinese alternated between the Zong and Heng symbols? If only the Zong symbols "
                  "were to be used, how would 41 be represented? Could this numeral be interpreted in any other way if "
                  "there is no significant space between two successive positions?",
                  ["Alternating shapes shows where one place ends and the next begins.",
                   "With zongs only, 41 is four vertical rods for the tens and one vertical rod for the units: 5 "
                   "rods in a row.",
                   "Without a clear gap, 5 rods could be read as 5, as 2 then 3 (23), as 3 then 2 (32), or as 1, 2, "
                   "2 (122).",
                   "So alternating zong and heng keeps neighbouring places apart."],
                  "To keep neighbouring places apart; with zongs only 41 is 4 rods and 1 rod, which could also be read "
                  "as 5, 23, 32 or 122")],
          misconceptions=["M_BLANK_NOTHING", "M_POSITION_SAME"])],
    key_terms=["placeholder", "Mayan numerals", "rod numerals"]))

# ============================== T10 The Hindu number system and zero ========================================
TOPICS.append(TOPIC(
    "T10", "M3", "The Hindu Number System and Zero", ["3.4"], "Analyze",
    "Students read a Hindu numeral as a sum of digits times powers of 10, explain how 0 as a digit removes every "
    "ambiguity, describe 0 as a number with its own arithmetic, and write numbers in other bases.",
    "The Hindu number system is base 10 with place value and ten digits, one per place, including 0 for an empty "
    "place. Indian mathematicians also treated 0 as a number, which made the system unambiguous and efficient.",
    [A("T10.C1", "Base ten, ten digits and place value", "Apply",
       "Students read a Hindu numeral such as 4072 as digits times powers of 10, and explain why 0 as a digit and one "
       "digit per place make every numeral unambiguous.",
       textbook=["IV. The Hindu Number System",
                 "Where does the Hindu/Indian number system figure in the evolution of ideas of number "
                 "representation? What are its landmark numbers? And does it use a place value system?",
                 "Base-10 or Decimal. Ten symbols 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.",
                 "(3) × 10² + (7) × 10 + (5) × 1 = 375",
                 "As can be seen, the Hindu number system is a place value system. The Hindu number system has had a "
                 "symbol for 0 at least as early as 200 BCE.",
                 "Because of the use of 0 as a digit, and the use of a single digit in each position, this system does "
                 "not lead to any kind of ambiguity when reading or writing numerals."],
       teach=["Predict first: in 4072, what does the 0 tell you that a blank could not?",
              "Our landmarks are 1, 10, 100, 1000: base 10. Each place holds exactly one digit.",
              "Read a numeral as digits times landmarks: 375 is three 100s, seven 10s and five 1s.",
              "0 fills an empty place, so no reader can confuse 4072 with 472."],
       examples=[
           WE("Read 4072 as digits times powers of 10, and explain what the 0 does.",
              ["Places from the right: 1s, 10s, 100s, 1000s.",
               "4072 = (4) × 10³ + (0) × 10² + (7) × 10 + (2) × 1.",
               "Check: 4000 + 0 + 70 + 2 = 4072.",
               "The 0 says there are no hundreds; without it the digits 4, 7, 2 would read 472."],
              "4072 = (4) × 10³ + (0) × 10² + (7) × 10 + (2) × 1; the 0 holds the empty hundreds place",
              ncert=["3.4.hindu_375", "3.4.hindu_zero_digit"])],
       key_terms=["place value", "digit", "decimal"], misconceptions=["M_ZERO_NOTHING", "M_POSITION_SAME"],
       minutes=8),
     A("T10.C2", "Zero as a number", "Analyze",
       "Students state the arithmetic of 0 used by Aryabhata and Brahmagupta, explain how 0 and the negative numbers "
       "make a set closed under adding, subtracting and multiplying, and trace the five big ideas of the chapter.",
       textbook=["In Indian mathematics, indeed, zero was not just used as a placeholder in the place value system, "
                 "but was also given the status of a number in its own right, on par with other numbers.",
                 "The arithmetic properties of the number 0 (e.g., that 0 plus any number is the same number, and that "
                 "0 times any number is zero) were explicitly used by Aryabhata in his Aryabhatiya in 499 CE.",
                 "The use of 0 as a number like any other number, on which one can perform the basic arithmetic "
                 "operations, was codified by Brahmagupta in his work Brahmasphutasiddhanta in 628 CE.",
                 "By introducing 0 as a number, along with the negative numbers, Brahmagupta created what in modern "
                 "terms is called a ring, i.e., a set of numbers that is closed under addition, subtraction, and "
                 "multiplication.",
                 "Evolution of Ideas in Number Representation: 1. Count in groups of a single number. 2. Group using "
                 "landmark numbers. 3. Choosing powers of a number as landmark numbers, the idea of a base. 4. Using "
                 "positions to denote the landmark numbers, the idea of place value system. 5. The idea of 0 as a "
                 "positional digit and as a number.",
                 "The map shows the locations of the different civilisations. They existed in different time periods."],
       teach=["Predict first: is 0 a number you can add, subtract and multiply, or only a mark for an empty place?",
              "Aryabhata used 0 + a = a and 0 × a = 0 in his calculations; Brahmagupta set out the rules for 0 as a "
              "number.",
              "With 0 and the negative numbers, adding, subtracting or multiplying any two numbers always gives a "
              "number in the same set: a ring.",
              "Five ideas lead here: groups, landmarks, a base, place value, and 0 as a digit and a number."],
       examples=[
           WE("Use the rules for 0 to find 25 + 0, 25 × 0, 25 − 25 and 3 − 7. Why do we need 0 and the negative "
              "numbers for every answer to be a number?",
              ["0 plus any number is that number: 25 + 0 = 25.",
               "0 times any number is 0: 25 × 0 = 0.",
               "A number minus itself is 0: 25 − 25 = 0, so 0 must be a number for this answer to exist.",
               "3 − 7 = −4, a negative number; with 0 and the negatives, every sum, difference and product of two "
               "numbers stays in the set."],
              "25, 0, 0 and −4; without 0 and negative numbers some differences would have no answer",
              ncert=["3.4.zero_number", "3.4.brahmagupta_ring", "3.4.evolution_ideas", "3.4.map"])],
       key_terms=["zero", "ring"], misconceptions=["M_ZERO_NOTHING", "M_LINEAR_HISTORY"], minutes=8),
     A("T10.C3", "Writing a number in another base", "Apply",
       "Students write a number such as 19 with place value in base 8, base 5 and base 2, using digits from 0 to one "
       "less than the base.",
       textbook=["The ancient Indians likely used base 10 for the Hindu number system because humans have 10 fingers."],
       teach=["Predict first: in base 8, what digits would we need?",
              "In base 8 the places are 1, 8, 64; each place holds a digit from 0 to 7.",
              "Group the number into the landmarks of the base, largest first, and write the count of each.",
              "Use 0 for any empty place, exactly as in base 10."],
       examples=[
           WE("Write 19 in base 8, in base 5 and in base 2.",
              ["Base 8: one 8 would leave 11, so two 8s fit: 19 = (2) × 8 + 3, written 23.",
               "Base 5: 19 = (3) × 5 + 4, written 34.",
               "Base 2: landmarks 1, 2, 4, 8, 16; 19 = 16 + 2 + 1.",
               "19 = (1) × 16 + (0) × 8 + (0) × 4 + (1) × 2 + (1) × 1, written 10011."],
              "19 is written 23 in base 8, 34 in base 5 and 10011 in base 2")],
       key_terms=["base", "digit"], misconceptions=["M_BASE_TEN_ONLY"], minutes=6, thin=True),
     DOER("T10.C4", "Practice: compare number systems", "system_sorter", "Evaluate",
          "Students build a base-2 place value system from the Gumulgal words, judge the role of the Hindu numerals "
          "and 0 in daily life, and write 25 in base 8, base 5 and base 2.",
          ["Place value with a digit for 0 writes every number with finitely many symbols.",
           "In base n the places are 1, n, n², ... and the digits run from 0 to n − 1."],
          items=[
              FIO("FiOI.q2", "Figure it Out (place value, question 2)",
                  "Form a base-2 place value system using 'ukasar' and 'urapon' as the digits. Compare this system with "
                  "that of the Gumulgal's.",
                  ["Base 2 needs two digits: let urapon be 0 and ukasar be 1. The places are 1, 2, 4, 8, ...",
                   "1 is ukasar; 2 is ukasar urapon; 3 is ukasar ukasar; 4 is ukasar urapon urapon.",
                   "6 = (1) × 4 + (1) × 2 + (0) × 1, so 6 is ukasar ukasar urapon.",
                   "The Gumulgal joined words by adding (ukasar-ukasar-ukasar for 6) and stopped at 6; in the base-2 "
                   "system the position gives each word its value, so it never runs out."],
                  "With urapon as 0 and ukasar as 1, for example 6 is ukasar ukasar urapon; the place value version "
                  "never runs out, while the Gumulgal names add up words and stop at 6"),
              FIO("FiOI.q3", "Figure it Out (place value, question 3)",
                  "Where in your daily lives, and in which professions, do the Hindu numerals, and 0, play an "
                  "important role? How might our lives have been different if our number system and 0 hadn't been "
                  "invented or conceived of?",
                  ["Daily life: prices and bills, phone numbers, dates and times, scores, money in a bank.",
                   "Professions: shopkeepers, accountants, engineers, doctors reading doses, computer programmers.",
                   "Computers store everything in base 2 with only the digits 0 and 1.",
                   "Without place value and 0, every large number would need new symbols and calculation would be slow, "
                   "so science, trade and technology would have grown much more slowly."],
                  "Open answer: money, time, phones, computing, accounting and science all depend on them; without "
                  "them calculation would be slow and much of modern technology would be hard to build"),
              FIO("FiOI.q4", "Figure it Out (place value, question 4)",
                  "The ancient Indians likely used base 10 for the Hindu number system because humans have 10 "
                  "fingers. But what if we had only 8 fingers? How would we be writing numbers then? What would the "
                  "Hindu numerals look like if we were using base 8 instead? Base 5? Try writing the base-10 Hindu "
                  "numeral 25 as base-8 and base-5 Hindu numerals, respectively. Can you write it in base-2?",
                  ["With 8 fingers we would use base 8: digits 0 to 7 and places 1, 8, 64, ...",
                   "25 = (3) × 8 + 1, so in base 8 it is written 31.",
                   "25 = (1) × 25 + (0) × 5 + 0, so in base 5 it is written 100.",
                   "25 = 16 + 8 + 1 = (1) × 16 + (1) × 8 + (0) × 4 + (0) × 2 + (1) × 1, so in base 2 it is written "
                   "11001."],
                  "25 is written 31 in base 8, 100 in base 5 and 11001 in base 2")],
          misconceptions=["M_ZERO_NOTHING", "M_BASE_TEN_ONLY"])],
    key_terms=["Hindu number system", "zero", "place value"]))

# ============================== T11 Summary =================================================================
TOPICS.append(TOPIC(
    "T11", "M3", "Summary: A Story of Numbers", ["Summary"], "Remember",
    None,
    "A number system is a standard sequence; landmarks, a base and place value made it efficient, and 0 as a digit "
    "and as a number made the Hindu system unambiguous and usable everywhere.",
    [A("T11.C1", "Five ideas that made our numerals", "Remember",
       "Students restate what a number system, a numeral, a landmark number, a base-n system and a place value "
       "system are, and why 0 makes the Hindu number system complete.",
       textbook=["To represent numbers, we need a standard sequence of objects, names, or written symbols that have a "
                 "fixed order. This standard sequence is called a number system.",
                 "The symbols representing numbers in a written number system are called numerals.",
                 "In a number system, landmark numbers are numbers that are easily recognisable and used as reference "
                 "points for understanding and working with other numbers.",
                 "A number system whose landmark numbers are the powers of a number n is referred to as a base-n "
                 "number system.",
                 "Number systems having a base that make use of the position of a symbol in determining the landmark "
                 "number that it is associated with are called positional number systems or place value systems.",
                 "Place value representations were used in the Mesopotamian (Babylonian), Mayan, Chinese and Indian "
                 "civilisations.",
                 "The system of numerals that we use throughout the world today is the Hindu number system. It is a "
                 "place value system with (usually) 10 digits, including the digit 0 which is treated on par with "
                 "other digits."],
       teach=["Reema's question is answered: the Mesopotamians wrote 20 with two 10 symbols, 50 with five, and 100 as "
              "1 in the 60s place and four 10s in the 1s place.",
              "Five ideas carried us here: counting in groups, landmark numbers, a base, place value, and 0.",
              "Each idea fixed a weakness of the one before: too many marks, changing group sizes, endless symbols, "
              "and confusing blanks.",
              "Still open for you: invent a base of your own and write your age in it."],
       ncert=["summary"], video_focus=["RECAP"], minutes=8)],
    topic_type="summary"))
