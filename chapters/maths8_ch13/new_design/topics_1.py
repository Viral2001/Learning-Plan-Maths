# -*- coding: utf-8 -*-
"""Topics T1 and T2 (module M1: tricks that always work). Book sections 6.1 and 6.2, pp 135 to 137."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Framing: can a trick read your mind? =====================================
TOPICS.append(TOPIC(
    "T1", "M1", "Algebra Play: Can a Trick Read Your Mind?", ["6.1"], "Understand",
    "",
    "A number trick that seems to read minds, and the question that drives the chapter: why does a trick or puzzle "
    "work, and can we invent our own?",
    [A("T1.C1", "A trick that seems to read your mind", "Understand",
       "",
       textbook=["6.1 Algebra Play",
                 "Over the last two years, we have used algebra to model different situations. We have learned how to "
                 "solve algebraic equations and find the values of unknown letter-numbers. Let's now have some fun with "
                 "algebra. We shall investigate tricks and puzzles, and explain why they work using algebra. We will "
                 "also see how to invent new tricks and puzzles to entertain others."],
       teach=["Predict first: a friend says, think of any number, add 3, double it, take away 6, and halve it. "
              "Can the friend say what you will get without asking your number?",
              "Try it with 4 and with 10. Each time you get back the number you started with.",
              "Is it luck with the numbers we picked, or must it always happen? Keep this question open: by the end "
              "of the chapter letter-numbers will answer it, and you will build tricks of your own."],
       ncert=["6.1.intro"], key_terms=["trick", "letter-number"], video_focus=["HOOK"], minutes=4,
       enrichment=True)],
    topic_type="framing"))

# ============================== T2 Think of a Number tricks ===============================================
TOPICS.append(TOPIC(
    "T2", "M1", "Think of a Number Tricks", ["6.2"], "Analyze",
    "Students explain with a letter-number why a Think of a Number trick always ends on the same value, change the "
    "steps to reach a new final value, and decode the date trick by writing the answer as 100M + 165 + D.",
    "Write the starting number as a letter and follow it through the steps: if the letter cancels, every start gives "
    "the same answer; in the date trick the month and the day sit in the digits of the answer.",
    [A("T2.C1", "Why the trick always ends on 2", "Analyze",
       "Students try the double, add four, halve, subtract trick with two starting numbers and use a letter-number to "
       "show that the starting number cancels, so the trick always ends on 2.",
       textbook=["6.2 Thinking about 'Think of a Number' Tricks",
                 "In Grade 7, we learned about 'Think of a Number' tricks, like this one.",
                 "1. Think of a number. 2. Double it. 3. Add four. 4. Divide by two. 5. Subtract the original number "
                 "you thought of.",
                 "I predict you get 2. Am I right? Try it out with different starting numbers. Do you always end up "
                 "with the same value, 2? Why?",
                 "We saw that we can understand such tricks through algebra.",
                 "1. Think of a number: x. 2. Double it: 2x. 3. Add four: 2x + 4. 4. Divide by 2: x + 2. 5. Subtract "
                 "the original number you thought of: x + 2 − x = 2.",
                 "Therefore, no matter what the starting number is, the end result will always be 2!"],
       teach=["Predict first: will the trick give 2 for a large number like 50 as well as for 5?",
              "Try 5 and 11. Both end on 2.",
              "Now call the number x. Doubling gives 2x, adding four gives 2x + 4, halving gives x + 2, and taking "
              "away x leaves 2.",
              "The x cancels out, so the start does not matter. Trying a few numbers shows a pattern; the letter "
              "shows it must always hold."],
       examples=[
           WE("Try the trick (double, add four, divide by two, subtract the start) with 5 and with 11, then explain "
              "with a letter-number why it always ends on 2.",
              ["Start with 5: 5 × 2 = 10, then 10 + 4 = 14, then 14 ÷ 2 = 7, then 7 − 5 = 2.",
               "Start with 11: 11 × 2 = 22, then 22 + 4 = 26, then 26 ÷ 2 = 13, then 13 − 11 = 2.",
               "Start with x: double it to get 2x, add four to get 2x + 4, divide by 2 to get x + 2.",
               "Subtract the start: x + 2 − x leaves 2, whatever x is."],
              "It always ends on 2, because the starting number cancels out",
              ncert=["6.2.trick2"])],
       key_terms=["letter-number", "trick"], misconceptions=["M_TRICK_MAGIC", "M_LETTER_ONE_VALUE"], minutes=10),
     A("T2.C2", "Change the steps, change the answer", "Create",
       "Students change one step of the trick so that it always ends on 3 or on 5, check the change with a "
       "letter-number, and design a longer trick that still ends on a fixed value.",
       textbook=["How would you change this game to make the final answer 3? What about 5?",
                 "Can you come up with more complicated steps that always lead to the same final value?",
                 "Try to devise your own 'Think of a Number' trick."],
       teach=["Predict first: which step decides that the answer is 2?",
              "Adding four, then halving, leaves an extra 2. Add six instead and halving leaves 3; add ten and it "
              "leaves 5.",
              "A longer trick works the same way: any steps are fine as long as the letter cancels at the end.",
              "Invent your own trick, write each step with x, and test it on a friend."],
       examples=[
           WE("Change the trick so it always ends on 3, then on 5. Then check this longer trick: think of a number, "
              "multiply by 3, add 12, divide by 3, subtract the number.",
              ["Add six instead of four: 2x + 6, divided by 2 is x + 3, and x + 3 − x leaves 3.",
               "Add ten instead: 2x + 10, divided by 2 is x + 5, and subtracting x leaves 5.",
               "Longer trick with x: 3x, then 3x + 12, then x + 4, then x + 4 − x leaves 4.",
               "Check with 7: 7 × 3 = 21, then 21 + 12 = 33, then 33 ÷ 3 = 11, then 11 − 7 = 4."],
              "Add 6 for a final 3, add 10 for a final 5; the longer trick always ends on 4",
              ncert=["6.2.make3_5", "6.2.complicated", "6.2.mt_own_trick"])],
       key_terms=["steps", "final value"], misconceptions=["M_TRICK_MAGIC"], minutes=10,
       tool="trick_builder"),
     A("T2.C3", "Decoding the date trick", "Analyze",
       "Students follow the date trick with M for the month and D for the day, write the final answer as "
       "100M + 165 + D, and read the date from an answer by subtracting 165.",
       textbook=["Let us now look at a different trick of this type.",
                 "Shubham: Think of a date. Multiply the month by 5. Add 6. Multiply by 4. Add 9. Multiply by 5. Add "
                 "the day. Tell me your answer.",
                 "Mukta thinks of 26 January and reports 291. Shubham says: You thought of our Republic Day.",
                 "How did Shubham figure out the date chosen by Mukta?",
                 "Let the month be M and the day be D. Multiply M by 5: 5M. Add 6: 5M + 6. Multiply by 4: 20M + 24. "
                 "Add 9: 20M + 33. Multiply by 5: 100M + 165. Add the day: 100M + 165 + D.",
                 "Mukta's answer was 291. 291 = 100M + 165 + D. 291 − 165 = 100M + D. 126 = 100M + D.",
                 "Since D is a day within a month, it is atmost 31 and requires only 2 digits. So the last 2 digits are "
                 "D and what comes before that is M. In this case, M is 1 and D is 26, i.e., the 26th of January."],
       teach=["Predict first: Shubham never asked for the date, so where in 291 is it hiding?",
              "Follow the steps with M and D: the answer is always 100M + 165 + D.",
              "Subtract 165 and you are left with 100M + D: the last two digits are the day, the digits before them "
              "are the month.",
              "For 291, taking away 165 leaves 126: month 1, day 26, which is 26 January."],
       examples=[
           WE("Mukta thinks of 26 January and follows the steps. Show that she gets 291, and how Shubham reads the "
              "date back from 291.",
              ["Month 1: 1 × 5 = 5, then 5 + 6 = 11, then 11 × 4 = 44, then 44 + 9 = 53, then 53 × 5 = 265.",
               "Add the day: 265 + 26 = 291.",
               "With letters the answer is always 100M + 165 + D.",
               "Subtract 165: 291 − 165 = 126, which is 100M + D.",
               "The last two digits, 26, are the day and the digit before them, 1, is the month."],
              "26 January: the answer minus 165 shows the month followed by the two digit day",
              ncert=["6.2.date_trick"])],
       key_terms=["month", "day", "letter-number"], misconceptions=["M_DATE_DIGITS"], minutes=10),
     A("T2.C3x", "Reading a date from 1390", "Apply",
       "Students subtract 165 from a reported answer of 1390, split the result into a month and a two digit day, and "
       "check the date by running the trick forward.",
       textbook=["Mukta thinks of another date, follows the same steps, and reports her answer as 1390. What date did "
                 "Mukta start with this time?",
                 "Subtracting 165 from 1390, we get 1225.",
                 "This means that the date she thought of was 25th December."],
       teach=["Predict first: is the month a one digit or a two digit number this time?",
              "Taking away 165 leaves 1225. The last two digits, 25, are the day; the digits before, 12, are the month.",
              "Check by running the trick forward with month 12 and day 25."],
       examples=[
           WE("Mukta reports 1390. Which date did she think of? Check by running the trick forward.",
              ["Subtract 165: 1390 − 165 = 1225.",
               "The last two digits give the day, 25. The digits before them give the month, 12.",
               "Check: 12 × 5 = 60, then 60 + 6 = 66, then 66 × 4 = 264, then 264 + 9 = 273, then 273 × 5 = 1365.",
               "Add the day: 1365 + 25 = 1390. It matches."],
              "25 December",
              ncert=["6.2.date_1390"])],
       key_terms=["month", "day"], misconceptions=["M_DATE_DIGITS"], minutes=6, thin=True),
     A("T2.C3y", "Change the steps and still find the date", "Create",
       "Students design new steps for the date trick, write the answer as 100M plus a fixed number plus D, and find "
       "the number to subtract to read the date.",
       textbook=["You can try this trick with your friends. Ask them to choose the starting date as their birthday.",
                 "Can you change the steps in this trick and still find the original date? Instead of subtracting 165 "
                 "from the final answer, you might have to subtract some other number."],
       teach=["Predict first: what must the steps do to the month so that the date can still be read?",
              "The month must end up multiplied by 100 so the day fits in the last two digits.",
              "Any fixed numbers added along the way just change the number you subtract at the end."],
       examples=[
           WE("New steps: multiply the month by 10, add 7, multiply by 10, add the day. What do you subtract to read "
              "the date? A friend reports 1295.",
              ["With letters: 10M, then 10M + 7, then 100M + 70, then 100M + 70 + D.",
               "So subtract 70 to leave 100M + D.",
               "For the friend: 1295 − 70 = 1225, so month 12 and day 25.",
               "Check: 12 × 10 = 120, then 120 + 7 = 127, then 127 × 10 = 1270, then 1270 + 25 = 1295."],
              "Subtract 70; the friend chose 25 December",
              ncert=["6.2.mt_change_steps"])],
       key_terms=["month", "steps"], minutes=6, thin=True),
     DOER("T2.C4", "Practice: decode the dates", "date_decoder", "Apply",
          "Students subtract 165 from each reported answer, split the result into month and day, and check that each "
          "date is a real date of the year.",
          ["Every answer of the date trick is 100M + 165 + D.",
           "Subtract 165: the last two digits are the day, the digits before them are the month."],
          items=[
              FIO("6.2.find_dates", "Think of a Number tricks: find the dates",
                  "Find the dates if the final answers of the date trick are the following: (i) 1269 (ii) 394 "
                  "(iii) 296.",
                  ["(i) 1269 − 165 = 1104: the day is 04 and the month is 11, so 4 November.",
                   "(ii) 394 − 165 = 229: the day is 29 and the month is 2, so 29 February, a leap year date.",
                   "(iii) 296 − 165 = 131: the day is 31 and the month is 1, so 31 January."],
                  "(i) 4 November (ii) 29 February (iii) 31 January")],
          misconceptions=["M_DATE_DIGITS"])],
    key_terms=["letter-number", "trick", "date"]))
