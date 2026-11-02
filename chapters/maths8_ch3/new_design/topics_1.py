# -*- coding: utf-8 -*-
"""Topics T1 to T3 (module M1). Book sections 3.1 and the first half of 3.2, pp 48 to 58."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Framing: Reema's loose page ==============================================
TOPICS.append(TOPIC(
    "T1", "M1", "A Story of Numbers: Reema's Curiosity", ["3.1"], "Understand",
    "",
    "A loose page of strange symbols turns out to be numbers written 4000 years ago, and opens the question of how "
    "people counted and wrote numbers before our numerals, and where our numerals came from.",
    [A("T1.C1", "A loose page of strange symbols", "Understand",
       "",
       textbook=["3.1 Reema's Curiosity",
                 "One lazy afternoon, Reema was flipping through an old book when, whoosh!, a piece of paper slipped "
                 "out and floated to the floor. She picked it up and stared at the strange symbols all over it. "
                 "\"What is this?\" she wondered.",
                 "She ran to her father, holding the paper as if it were a secret treasure. He looked at it and "
                 "smiled. \"Around 4000 years ago, there flourished a civilisation in a region called Mesopotamia, in "
                 "the western part of Asia, containing a major part of the present-day Iraq and a few other "
                 "neighbouring countries. This is one of the ways they wrote their numbers!\"",
                 "Reema's eyes lit up, \"Seriously? These strange symbols were numbers?\"",
                 "Since when have humans been counting? What was their need for counting? What were they counting?",
                 "Since when have people been writing numbers in the modern form?",
                 "How would the Mesopotamians have written 20? 50? 100?"],
       teach=["Predict first: if you had never seen our digits, how would you write the number of days in a month?",
              "Reema's page shows numbers written about 4000 years ago, with no digits we would recognise.",
              "Her questions are ours too: why did people count, what did they count, and how did they write it?",
              "Keep the last question open: how would those people have written 20, 50 or 100? We answer it in the "
              "last part of the chapter."],
       ncert=["3.1.reema", "3.1.questions"], key_terms=["number", "symbol", "numeral"], video_focus=["HOOK"],
       minutes=4, enrichment=True)],
    topic_type="framing"))

# ============================== T2 The mechanism of counting ================================================
TOPICS.append(TOPIC(
    "T2", "M1", "The Mechanism of Counting", ["3.1"], "Understand",
    "Students count and compare collections with no number names by one-to-one mapping with sticks, use letters and "
    "Roman symbols as a standard sequence, and explain what a number system and a numeral are and why a system must "
    "never run out.",
    "Counting is a one-to-one mapping between objects and a standard sequence with a fixed order; such a sequence is "
    "a number system, and the written symbols in it are numerals. A good system never runs out and is easy to count "
    "with.",
    [A("T1.C2", "Where our numerals came from", "Understand",
       "",
       textbook=["Humans had the need to count even as early as the Stone Age. They were counting to determine the "
                 "quantity of food they had, the number of animals in their livestock, details regarding trades of "
                 "goods, the number of offerings given in rituals, etc.",
                 "Ancient Indian texts, such as the Yajurveda Samhita, mentioned names of numbers based on powers of "
                 "10, almost as we say them orally today. For example, they listed names for the numbers one (eka), "
                 "ten (dasha), hundred (shata), thousand (sahasra), ten thousand (ayuta), etc., all the way up to 10 "
                 "to the power 12 and beyond.",
                 "The first known instance of numbers being written using ten digits, including the digit 0 (which "
                 "was then notated as a dot), occurs in the Bakhshali manuscript (c. 3rd century CE).",
                 "The Indian number system was transmitted to the Arab world by around 800 CE.",
                 "From the Arab world, the Hindu numerals were transmitted to Europe and to parts of Africa by around "
                 "1100 CE.",
                 "\"The ingenious method of expressing every possible number using a set of ten symbols (each symbol "
                 "having a place value and an absolute value) emerged in India.\" (Pierre-Simon Laplace)",
                 "The most commonly used terminologies for the numbers we use today are 'Hindu numerals', 'Indian "
                 "numerals', and the transitional 'Hindu-Arabic numerals'.",
                 "The shape of the digits 0, 1, 2, ..., 9 used to write numbers in the Indian number system today "
                 "evolved over a period of time."],
       teach=["Predict first: in which part of the world did the digits 0 to 9 begin?",
              "People counted from the Stone Age: food, animals, trades, offerings and the passing days.",
              "Old Indian texts named numbers by powers of 10: eka, dasha, shata, sahasra, ayuta.",
              "The ten digits with a dot for zero appear in the Bakhshali manuscript; the system travelled to the "
              "Arab world and then to Europe, which is why some people wrongly call them Arabic numerals."],
       examples=[
           WE("The Yajurveda lists eka, dasha, shata, sahasra and ayuta. Which numbers are these, and how is each one "
              "related to the one before it?",
              ["eka is one and dasha is ten: 10 × 1 = 10.",
               "shata is a hundred: 10 × 10 = 100.",
               "sahasra is a thousand: 10 × 100 = 1000.",
               "ayuta is ten thousand: 10 × 1000 = 10000.",
               "Each name is 10 times the one before it, so the names follow powers of 10, just as we say numbers "
               "today."],
              "1, 10, 100, 1000 and 10000; each is 10 times the one before",
              ncert=["3.1.need_count", "3.1.yajurveda", "3.1.bakhshali", "3.1.transmission", "3.1.laplace",
                     "3.1.naming", "3.1.digit_evolution"])],
       key_terms=["Hindu numerals", "powers of 10"], misconceptions=["M_ARABIC_ORIGIN"], minutes=6, thin=True,
       enrichment=True),
     A("T2.C1", "One stick for every cow: one-to-one mapping", "Apply",
       "Students check that a herd has returned, compare two herds and find how many more cows are needed by matching "
       "each cow with exactly one stick, without number names.",
       textbook=["The Mechanism of Counting",
                 "Imagine that we are living in the Stone Age, say, around ten thousand years ago. Suppose we have a "
                 "herd of cows.",
                 "Q1. How do we ensure that all cows have returned safely after grazing? Q2. Do we have fewer cows "
                 "than our neighbour? Q3. If there are fewer, how many more cows would we need so that we have the "
                 "same number of cows as our neighbour?",
                 "Method 1: We could tackle the questions by using pebbles, sticks or any object that is available in "
                 "abundance. Let us choose sticks. For every cow in the herd, we could keep a stick.",
                 "This way of associating each cow with a stick, such that no two cows are associated or mapped to "
                 "the same stick is called a one-to-one mapping.",
                 "How will you use such sticks to answer the other two questions (Q2 and Q3)?"],
       teach=["Predict first: with no number names at all, can you tell whether every cow came home?",
              "Keep one stick for each cow in the morning. In the evening, take one stick out for each cow that "
              "returns.",
              "A stick left over means a cow is missing; this pairing, one cow to one stick, is a one-to-one mapping.",
              "To compare with a neighbour, pair your sticks with theirs: the unpaired sticks show who has more and "
              "how many more are needed."],
       examples=[
           WE("In the morning a herder keeps one stick for each cow. In the evening she takes out one stick for each "
              "cow that returns, and 2 sticks are left. Her neighbour's stick bundle, paired stick by stick with "
              "hers, has 3 sticks without partners. What can she say?",
              ["Each returning cow removes exactly one stick, so every stick left stands for a cow that did not "
               "return.",
               "2 sticks are left, so 2 cows are still missing.",
               "Pairing her sticks with the neighbour's sticks one to one, the 3 unpaired sticks are on the "
               "neighbour's side.",
               "So she has fewer cows than her neighbour, and she needs 3 more cows to have the same number."],
              "2 cows are missing; she has fewer cows than her neighbour and needs 3 more",
              ncert=["3.1.cows_mt", "3.1.sticks", "3.1.sticks_q2q3"])],
       key_terms=["one-to-one mapping", "collection"], misconceptions=["M_COUNT_NEEDS_NAMES"], minutes=8),
     A("T2.C2", "Letters and symbols as a counting sequence", "Apply",
       "Students count with the letters a to z and with the Roman symbols of Table 1, find the letter or symbol for "
       "a given count, and explain why the letters run out after 26.",
       textbook=["Method 2: Instead of objects, we could use a standard sequence of sounds or names. For example, we "
                 "could use the sounds of the letters of any language.",
                 "An obvious limitation of using only the letters of the English alphabet in this form is that it "
                 "cannot be used to count collections having more than 26 objects.",
                 "How many numbers can you represent in this way using the sounds of the letters of your language?",
                 "Method 3: We could use a sequence of written symbols as follows.",
                 "I, II, III, IV, V, VI, VII, VIII, IX, X, XI, XII, XIII, XIV, XV, XVI, XVII, XVIII, XIX, XX (Table 1)",
                 "Do you see a way of extending this method to represent bigger numbers as well? How?"],
       teach=["Predict first: using the letters a to z, which letter goes with the 20th object?",
              "Say the letters in order, one letter for each object; the last letter said tells the count.",
              "The 20th letter is t, but there is no letter for a 27th object, so this sequence runs out.",
              "The symbols of Table 1 keep going: after XX come XXI, XXII and so on, with new symbols for bigger "
              "groups."],
       examples=[
           WE("Using the letters a to z as a counting sequence, which letter counts the 20th object, and what happens "
              "with 27 objects? Then use Table 1 to write 13 and 18 in Roman symbols.",
              ["Match the objects with a, b, c, ... in order: the 20th letter of the alphabet is t.",
               "The alphabet has only 26 letters, so the 27th object has no letter; the sequence runs out.",
               "In Table 1, 13 is X followed by three I's: XIII.",
               "18 is X, then V, then three I's: XVIII."],
              "The 20th object is t; 27 objects cannot be counted; 13 is XIII and 18 is XVIII",
              ncert=["3.1.letters", "3.1.letters_mt", "3.1.symbols_extend", "3.1.roman_table1"])],
       key_terms=["standard sequence", "letter-order"], misconceptions=["M_SYSTEM_ENDLESS"], minutes=8),
     A("T2.C3", "A number system is a standard sequence", "Analyze",
       "Students define a number system and a numeral, and compare sticks, letters and Roman symbols on whether each "
       "sequence never ends and whether it is easy to count with.",
       textbook=["For counting and finding the size of a collection, we need a standard sequence of objects, or names, "
                 "or written symbols, that has a fixed order. Let us call this standard sequence a number system.",
                 "Since there is no end to numbers, the challenge is to come up with an unending standard "
                 "sequence/number system that is easy to count with.",
                 "Using sticks gives an unending standard sequence/number system. However, it is not convenient to "
                 "count larger collections, as we will need as many sticks as the number of objects being counted.",
                 "The standard sequence/number system given in Method 3 was actually the system used in Europe before "
                 "it got replaced by the Hindu number system. It is called the Roman number system.",
                 "The symbols occurring in a written number system are called numerals."],
       teach=["Predict first: which of the three methods could count a herd of a thousand cows most easily?",
              "A number system is a standard sequence with a fixed order; we count by mapping objects to it one to "
              "one.",
              "Sticks never run out but need one stick per object; letters are easy to say but stop at 26; Roman "
              "symbols need new symbols for bigger numbers.",
              "The written symbols of a number system are its numerals, like 0, 1, 5, 36 and 193 in ours."],
       examples=[
           WE("Compare the three counting methods (sticks, letters a to z, Roman symbols) on two questions: does the "
              "sequence ever end, and is it easy to count a large collection with it?",
              ["Sticks: add one more stick each time, so the sequence never ends; but 500 cows need 500 sticks, which "
               "is slow and heavy.",
               "Letters: easy to say quickly, but after z there is no next letter, so it ends at 26.",
               "Roman symbols: compact, but bigger and bigger numbers keep needing new symbols.",
               "None of the three is both unending and easy; that is the challenge a good number system must meet."],
              "Sticks never end but are slow; letters are quick but end at 26; Roman symbols need ever new symbols",
              ncert=["3.1.number_system", "3.1.numerals"])],
       key_terms=["number system", "numeral"], misconceptions=["M_SYSTEM_ENDLESS"], minutes=8),
     DOER("T2.C4", "Practice: count, compare and extend", "stick_matcher", "Apply",
          "Students compute with collections of sticks without number names, extend the letter system to all numbers, "
          "and design a number system of their own.",
          ["Counting is a one-to-one mapping with a standard sequence.",
           "A good number system never runs out and is easy to count with."],
          items=[
              FIO("FiOA.q1", "Figure it Out (the mechanism of counting, question 1)",
                  "Suppose you are using the number system that uses sticks to represent numbers, as in Method 1. "
                  "Without using either the number names or the numerals of the Hindu number system, give a method "
                  "for adding, subtracting, multiplying and dividing two numbers or two collections of sticks.",
                  ["To add, put the two collections of sticks together; the joined pile is the sum.",
                   "To subtract, pair each stick of the smaller pile with a stick of the larger pile and take the pairs "
                   "away; the unpaired sticks are the difference.",
                   "To multiply, lay out the first pile once for every stick of the second pile and join all the "
                   "copies.",
                   "To divide, keep taking out groups the size of the second pile; the number of groups is the "
                   "quotient and the sticks that cannot make a full group are the remainder."],
                  "Add by joining, subtract by pairing and removing, multiply by repeating one pile once per stick of "
                  "the other, divide by taking out equal groups"),
              FIO("FiOA.q2", "Figure it Out (the mechanism of counting, question 2)",
                  "One way of extending the number system in Method 2 is by using strings with more than one letter, "
                  "for example, we could use 'aa' for 27. How can you extend this system to represent all the "
                  "numbers? There are many ways of doing it!",
                  ["After z, start again with doubled letters: aa, bb, cc, ..., zz count the next 26 objects.",
                   "Then use tripled letters aaa, bbb, ..., zzz for the next 26, and so on.",
                   "Another way: after z use aa, ab, ac, ..., az, then ba, bb, ..., like the columns of a spreadsheet.",
                   "Either way, longer strings can always be made, so the sequence never runs out."],
                  "One way: a to z, then aa, bb, ..., zz, then aaa, bbb, ..., zzz and so on; many other ways work"),
              FIO("FiOA.q3", "Figure it Out (the mechanism of counting, question 3)",
                  "Try making your own number system.",
                  ["Choose a standard sequence with a fixed order: objects, sounds or written marks.",
                   "Check that it never runs out: decide how to make the next symbol after any symbol.",
                   "Check that it is easy to count with: for example, give a new mark to every group of five.",
                   "Test it by writing a few numbers, such as the number of students in your class."],
                  "Open answer: any fixed-order sequence that never runs out and is easy to count with")],
          misconceptions=["M_COUNT_NEEDS_NAMES", "M_SYSTEM_ENDLESS"])],
    key_terms=["one-to-one mapping", "number system", "numeral"]))

# ============================== T3 Some early number systems ================================================
TOPICS.append(TOPIC(
    "T3", "M1", "Some Early Number Systems", ["3.2"], "Analyze",
    "Students describe counting with body parts and tally marks, explain how Gumulgal number names are built by "
    "counting in twos, and analyse why grouping by one size helps the eye but still becomes cumbersome for large "
    "numbers.",
    "Early systems used body parts and tally marks, one mark per object. Counting in groups, in twos for the "
    "Gumulgal or in fives for tally marks, made numbers shorter, but one group size alone is still slow for large "
    "numbers.",
    [A("T3.C1", "Body parts and tally marks", "Understand",
       "Students describe counting with body parts and with tally marks on bones, and group the 29 notches of the "
       "Lebombo bone into fives to read them faster.",
       textbook=["3.2 Some Early Number Systems",
                 "I. Use of Body Parts: Many groups of people across the world have used their hands and body parts "
                 "for counting.",
                 "II. Tally Marks on Bones and Other Surfaces: One of the oldest methods of number representation is "
                 "by making notches, marks cut on a surface such as a bone or a wall of a cave. These marks are also "
                 "called tally marks.",
                 "In this method, a mark is made for each object that is being counted.",
                 "The Lebombo bone, discovered in South Africa, is an even older tally stick with 29 notches, "
                 "estimated to be around 44,000 years old."],
       teach=["Predict first: is a row of 29 notches easy to read at a glance?",
              "Body-part counting points to fingers, wrist, elbow, shoulder and so on, in a fixed order.",
              "A tally makes one mark for each object, just like keeping one stick for each cow.",
              "Long rows of marks are hard to read, which is why people began to bunch them in groups."],
       examples=[
           WE("The Lebombo bone has 29 notches. Group them in fives. How many full groups are there, and how many "
              "notches are left over?",
              ["Count off five notches at a time: 5, 10, 15, 20, 25.",
               "That is 5 full groups of five, and 5 × 5 = 25.",
               "29 − 25 = 4, so 4 notches are left over.",
               "So the 29 notches read as 5 groups of five and 4 more: 5 × 5 + 4 = 29."],
              "5 groups of five and 4 more",
              ncert=["3.2.body_parts", "3.2.tally", "3.2.bones"])],
       key_terms=["tally marks", "notch"], misconceptions=["M_COUNT_NEEDS_NAMES"], minutes=8),
     A("T3.C2", "Gumulgal names: counting in twos", "Analyze",
       "Students explain how the Gumulgal names for 3 to 6 are built from urapon (1) and ukasar (2), and build the "
       "name for a number up to 6.",
       textbook=["III. Number Names Obtained by Counting in Twos",
                 "A group of indigenous people in Australia called the Gumulgal had the following words for their "
                 "numbers: 1 urapon, 2 ukasar, 3 ukasar-urapon, 4 ukasar-ukasar, 5 ukasar-ukasar-urapon, 6 "
                 "ukasar-ukasar-ukasar.",
                 "The numbers are counted in 2s, using which the number names are formed: 3 = 2 + 1, 4 = 2 + 2, "
                 "5 = 2 + 2 + 1, 6 = 2 + 2 + 2.",
                 "Gumulgal called any number greater than 6 ras.",
                 "Despite being so far apart geographically, and with no trace of contact between them, these three "
                 "groups have developed equivalent number systems!"],
       teach=["Predict first: if urapon is 1 and ukasar is 2, what might the name for 3 be?",
              "Each name is made of twos and at most one extra one: 3 is ukasar-urapon, 2 + 1.",
              "4 is two ukasars, 5 is two ukasars and an urapon, 6 is three ukasars.",
              "Beyond 6 they just said ras, many; the Bakairi and the Bushmen counted in twos in the same way."],
       examples=[
           WE("In the Gumulgal system, urapon is 1 and ukasar is 2. Build the names for 5 and 6, and say what a "
              "Gumulgal speaker would say for 7.",
              ["Split 5 into twos and a one: 5 = 2 + 2 + 1.",
               "So 5 is ukasar-ukasar-urapon.",
               "6 = 2 + 2 + 2, so 6 is ukasar-ukasar-ukasar.",
               "Any number greater than 6 was simply called ras."],
              "5 is ukasar-ukasar-urapon, 6 is ukasar-ukasar-ukasar, and 7 is ras",
              ncert=["3.2.gumulgal", "3.2.gumulgal_mt", "3.2.equivalent_systems"])],
       key_terms=["counting in twos", "number name"], misconceptions=["M_BASE_TEN_ONLY"], minutes=8),
     A("T3.C3", "Grouping by one size, and its limit", "Analyze",
       "Students find the group size they can see at a glance, explain why tally marks were bunched in fives, and "
       "show that counting 1345 in fives alone still needs 269 groups.",
       textbook=["A general form which this idea has taken in different number systems is as follows: count in "
                 "groups of a certain number (like 2 in the case of Gumulgal's system), and use the word or symbol "
                 "associated with this group size to represent bigger numbers.",
                 "Some of the commonly used group sizes in different number systems have been 2, 5, 10 and 20.",
                 "Up to what group size could you immediately see the number of objects without counting? Most "
                 "humans find it difficult to count groups having 5 or more objects in a single glance.",
                 "What could be the difficulties with using a number system that counts only in groups of a single "
                 "particular size? How would you represent a number like 1345 in a system that counts only by 5s?"],
       teach=["Predict first: how many dots can you see at a glance without counting, 3, 6 or 10?",
              "Most people see up to about 4 at once; 5 or more need counting, so marks were bunched in fives.",
              "Counting in groups of one size, such as 2 or 5, shortens a long row of marks.",
              "But a large number still needs a huge number of groups, so one group size alone is not enough."],
       examples=[
           WE("In a system that counts only by 5s, how would 1345 be written? How many group symbols are needed?",
              ["Find how many fives make 1345: 1345 ÷ 5 = 269.",
               "Check: 269 × 5 = 1345, so nothing is left over.",
               "So 1345 needs the symbol for five written 269 times.",
               "That is far too many symbols to write or read, so a single group size soon becomes cumbersome."],
              "269 symbols for five, too many to write or read easily",
              ncert=["3.2.group_size", "3.2.subitize", "3.2.only_fives_mt"])],
       key_terms=["group size", "glance"], misconceptions=["M_BASE_TEN_ONLY"], minutes=8),
     DOER("T3.C4", "Practice: count in groups", "gumulgal_builder", "Apply",
          "Students explain why some people use different counting sequences for different objects, and add, "
          "subtract, multiply and divide numbers written in the Gumulgal system extended beyond 6.",
          ["Gumulgal names count in twos: urapon is 1 and ukasar is 2.",
           "Counting in groups shortens numbers, but one group size alone is still slow for large numbers."],
          items=[
              FIO("FiOC.q1", "Figure it Out (early number systems, question 1)",
                  "A group of indigenous people in a Pacific island use different sequences of number names to count "
                  "different objects. Why do you think they do this?",
                  ["Think about what was being counted: fish, coconuts, canoes, days.",
                   "Things that come in bunches or pairs may be easier to count in their own groups.",
                   "A separate sequence also tells the listener what kind of object is meant.",
                   "So the sequences may follow how each kind of object is usually grouped, traded or used."],
                  "Open answer: for example, each kind of object is grouped or traded in its own way, and the name also "
                  "tells what is being counted"),
              FIO("FiOC.q2", "Figure it Out (early number systems, question 2)",
                  "Consider the extension of the Gumulgal number system beyond 6 in the same way of counting by 2s. "
                  "Come up with ways of performing the different arithmetic operations (+, −, ×, ÷) for numbers "
                  "occurring in this system, without using Hindu numerals. Use this to evaluate the following: "
                  "(i) (ukasar-ukasar-ukasar-ukasar-urapon) + (ukasar-ukasar-ukasar-urapon) "
                  "(ii) (ukasar-ukasar-ukasar-ukasar-urapon) − (ukasar-ukasar-ukasar) "
                  "(iii) (ukasar-ukasar-ukasar-ukasar-urapon) × (ukasar-ukasar) "
                  "(iv) (ukasar-ukasar-ukasar-ukasar-ukasar-ukasar-ukasar-ukasar) ÷ (ukasar-ukasar)",
                  ["(i) Join the words: 4 ukasar and 3 ukasar give 7 ukasar, and the two urapons make one more ukasar, "
                   "so 8 ukasar. Check: 9 + 7 = 16.",
                   "(ii) Take 3 ukasar away from 4 ukasar and an urapon: ukasar-urapon is left. Check: 9 − 6 = 3.",
                   "(iii) ukasar-ukasar is two twos, so write the first number two times and then double the result, 4 "
                   "copies in all: 16 ukasar and 4 urapons, and the 4 urapons make 2 more ukasar, so 18 ukasar. "
                   "Check: 9 × 4 = 36.",
                   "(iv) Share 8 ukasar into groups of ukasar-ukasar: there are 4 groups, written ukasar-ukasar. "
                   "Check: 16 ÷ 4 = 4."],
                  "(i) ukasar written 8 times (ii) ukasar-urapon (iii) ukasar written 18 times (iv) ukasar-ukasar")],
          misconceptions=["M_BASE_TEN_ONLY"])],
    key_terms=["tally marks", "counting in groups", "group size"]))
