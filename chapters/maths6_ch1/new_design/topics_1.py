# -*- coding: utf-8 -*-
"""Topics T1 to T3 (module M1: patterns and number sequences). Chapter opening and book sections 1.1 and 1.2."""
from topics_common import A, DOER, TOPIC, WE, BOOK_TEXT, book, fio, we

TOPICS = []

# ============================== T1 Chapter opening ===========================================================
TOPICS.append(TOPIC(
    "T1", "M1", "Matchsticks That Grow", ["Chapter opening"], "Understand",
    "",
    "A row of matchstick figures grows step by step, and you can tell what comes next without being shown it.",
    [A("T1.C1", "What comes next in the matchstick row?", "Remember", "",
       textbook=["PATTERNS IN MATHEMATICS"],
       teach=["Look at the row of matchstick figures. Before reading on, guess: what would the next figure look "
              "like, and why?",
              "Each figure is a little bigger than the one before, and it grows in the same way every time.",
              "When something repeats or grows by a rule, that is a pattern, and a pattern lets us say what comes "
              "next.",
              "This chapter is about finding such patterns in numbers and in shapes, and about explaining why they "
              "happen."],
       ncert=["opening"], key_terms=["pattern", "rule"], video_focus=["HOOK"], minutes=4, enrichment=True)],
    topic_type="framing"))

# ============================== T2 What is mathematics? (1.1) ================================================
TOPICS.append(TOPIC(
    "T2", "M1", "Mathematics: the Search for Patterns", ["1.1"], "Understand",
    "Students describe mathematics as the search for patterns and for the reasons behind them, and give "
    "everyday and larger examples of where patterns help.",
    "Mathematics is the search for patterns and for the explanations of why they exist; those explanations can be "
    "used far beyond where they were found.",
    [A("T2.C1", "Patterns are all around us", "Understand",
       "Students say that mathematics is largely the search for patterns, and name patterns from nature, home, "
       "school, games and the sky.",
       textbook=book("1.1", stop=3),
       teach=["Predict first: where in your day do you meet a pattern? Think of the school bell, the days of the "
              "week, a cricket score.",
              "Patterns are in nature, in homes and schools, and in the motion of the sun, moon and stars.",
              "Mathematics is, in large part, the search for such patterns, and finding them can be creative and "
              "fun."],
       examples=[WE('Name two patterns you meet in a day, one in nature and one at school.',
                   ['Nature: day and night come back in turn, and the Moon changes shape in a fixed order.', 'School: the bell rings at fixed times, and the timetable repeats every week.', 'Each of these repeats by a rule, so each is a pattern.'],
                   'Day and night, and the weekly timetable, are patterns.')],
       key_terms=["pattern", "mathematics"], misconceptions=["M_MATHS_SUMS"], minutes=8),
     A("T2.C2", "Why the explanation matters", "Understand",
       "Students explain that mathematics looks for the reason a pattern exists, and that a reason found in one "
       "place can be used elsewhere, as with gravitation and genomes.",
       textbook=book("1.1", start=3, stop=5),
       teach=["Predict first: if you notice that the Moon comes back to the same shape every month, is that enough "
              "for a mathematician?",
              "No. Mathematics also asks why the pattern happens. The reason can then be used in other places.",
              "Patterns in the motion of stars, planets and satellites led to the theory of gravitation, which "
              "lets us launch satellites and rockets.",
              "Patterns in genomes have helped in diagnosing and curing diseases."],
       examples=[WE('The Sun rises every day. Why does mathematics not stop at noticing this?',
                   ['Noticing tells us only that the Sun comes back every day.', 'Mathematics asks why, and looks for a rule for the motion of the Sun, Moon and stars.', 'A rule found for one place can be used in other places, such as in launching satellites.'],
                   'The reason gives a rule that can be used elsewhere, which a list of what happened cannot.')],
       key_terms=["pattern", "explanation"], misconceptions=["M_MATHS_SUMS"], minutes=8),
     DOER("T2.C3", "Practice: Where mathematics helps", None, "Understand",
          "Students give their own examples of mathematics in everyday life and in the progress of humanity.",
          ["Mathematics is the search for patterns and for the reasons they exist.",
           "A reason found for one pattern can be used well beyond where it was found."],
          items=[fio("1.1.FiO.Q1"), fio("1.1.FiO.Q2")],
          misconceptions=["M_MATHS_SUMS"])]))

# ============================== T3 Patterns in numbers (1.2) =================================================
TOPICS.append(TOPIC(
    "T3", "M1", "Number Sequences", ["1.2"], "Apply",
    "Students read a number sequence from Table 1, state the rule that forms its terms, and write the next terms.",
    "A number sequence is a list of numbers formed by a rule; knowing the rule gives the next term.",
    [A("T3.C1", "Sequences that grow by a steady step", "Understand",
       "Students describe a number sequence as an ordered list formed by a rule, and state the rule for the "
       "All 1's, counting, odd and even number sequences.",
       textbook=book("1.2", stop=10),
       teach=["Predict first: what comes after 1, 3, 5, 7, 9? How did you know?",
              "A list of numbers in a fixed order that follows a rule is a number sequence. The branch of "
              "mathematics that studies patterns in whole numbers is number theory.",
              "All 1's: every term is 1. Counting numbers: add 1 each time. Odd numbers: add 2 each time from 1. "
              "Even numbers: add 2 each time from 2.",
              "The rule is what tells us the next term, however far we go."],
       examples=[WE('Find the rule and the next term of 4, 7, 10, 13, 16.',
                   ['The jump from each term to the next is 3.', 'So the rule is add 3 each time.', '16 + 3 = 19.'],
                   'Add 3 each time; the next term is 19.')],
       key_terms=["number sequence", "term", "rule"],
       misconceptions=["M_ALL_ONES_NO_PATTERN", "M_RULE_FROM_TWO"], minutes=10),
     A("T3.C2", "Sequences whose jumps keep changing", "Analyze",
       "Students find the rule for the triangular, square and cube number sequences, seeing that the jump between "
       "terms changes each time.",
       textbook=book("1.2", start=10, stop=13),
       teach=["Predict first: 1, 3, 6, 10, 15. Does it add the same number each time?",
              "No. The jumps are 2, 3, 4, 5, so each jump is one bigger. These are the triangular numbers.",
              "Squares are 1 × 1, 2 × 2, 3 × 3 and so on, giving 1, 4, 9, 16, 25. Cubes are 1 × 1 × 1, "
              "2 × 2 × 2 and so on, giving 1, 8, 27, 64, 125.",
              "The next triangular number after 28 adds 8, giving 36."],
       examples=[WE('Find the next term of 2, 5, 9, 14, 20.',
                   ['The jumps are 3, 4, 5, 6, each one bigger than the one before.', 'The next jump is 7.', '20 + 7 = 27.'],
                   'The next term is 27.')],
       key_terms=["triangular number", "square number", "cube"],
       misconceptions=["M_ADD_SAME_ONLY", "M_SQUARE_IS_DOUBLE"], minutes=10),
     A("T3.C3", "Sequences built from earlier terms", "Analyze",
       "Students find the rule for the Virahanka numbers and for the powers of 2 and 3, where each term is made "
       "from the term or terms before it.",
       textbook=book("1.2", start=13, stop=16),
       teach=["Predict first: 1, 2, 3, 5, 8, 13. Look at 3, 5 and 8. How is 8 made from the two before it?",
              "Each Virahanka number is the sum of the two terms before it: 3 + 5 = 8 and 5 + 8 = 13.",
              "Powers of 2: multiply the last term by 2 to get 1, 2, 4, 8, 16, 32, 64. Powers of 3: multiply the "
              "last term by 3 to get 1, 3, 9, 27, 81.",
              "So a rule can add, or multiply, or use the earlier terms together."],
       examples=[WE('Find the next term of 3, 4, 7, 11, 18.',
                   ['Look for a rule from earlier terms: 3 + 4 = 7, 4 + 7 = 11, 7 + 11 = 18.', 'Each term is the sum of the two terms before it.', '11 + 18 = 29.'],
                   'The next term is 29.')],
       key_terms=["Virahanka numbers", "powers of 2"],
       misconceptions=["M_POWERS_ADD", "M_VIRAHANKA_COUNT"], minutes=10),
     DOER("T3.C4", "Pull it together and do it: Sequence Rule Finder", "sequence_rule_finder", "Apply",
          "Students pick the rule for a sequence on the tool, test it on every term, and write the next terms.",
          ["A number sequence follows a rule; the rule gives every next term.",
           "A rule may add the same number, add a growing number, multiply, or use the two terms before.",
           "Test a rule on all the terms shown, not just the first two."],
          items=[fio("1.2.FiO.Q1"), fio("1.2.FiO.Q2")],
          misconceptions=["M_ADD_SAME_ONLY", "M_RULE_FROM_TWO"])]))
