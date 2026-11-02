# -*- coding: utf-8 -*-
"""Topics T12 to T14 (module M4): book section 5.6 and the summary."""
from topics_common import A, DOER, TOPIC, BOOK_TEXT, book, fio, we, wem

TOPICS = []

# ============================== T12 Special numbers (5.6) ====================================================
TOPICS.append(TOPIC(
    "T12", "M4", "Special Numbers", ["5.6"], "Analyze",
    "Students give true reasons for why a number is special in a box of four, using factors, multiples, primes and "
    "digits, and check each classmate's reason.",
    "A number can be special for many true reasons; each reason must be checked against the other numbers.",
    [A("T12.C1", "Why is a number special?", "Analyze",
       "Students read the classmates' reasons for the box 9, 16, 25, 43, check each against all four numbers, and "
       "find that one number can be special for more than one reason.",
       textbook=book("5.6", "Special numbers", stop=8),
       teach=["Predict first: in the box 9, 16, 25, 43, which number looks special to you?",
              "Karnawati says 9 is the only one-digit number. True.",
              "Yadnyikee says 43 is the only prime. True: 9, 16 and 25 have more than two factors.",
              "Radha says 43 is the only number that is not a square. True: 9, 16 and 25 are squares. 43 is special "
              "for two reasons."],
       examples=[we("5.6.q1")],
       key_terms=["prime", "multiple", "factor"], misconceptions=["M_ONE_REASON_SPECIAL"], minutes=8),
     DOER("T12.C2", "Practice: Special reasons", None, "Analyze",
          "Students look at four numbers in each box, name how each is special compared to the rest with factors, "
          "multiples and primes, and check the reasons they give are true for that number only.",
          ["Check a reason against all four numbers, not just one.",
           "Factors, multiples, primes and digits each give reasons.",
           "A number may be special for more than one reason."],
          items=[], ncert=["5.6.q2"],
          misconceptions=["M_ONE_REASON_SPECIAL"])]))

# ============================== T13 A prime puzzle (5.6) =====================================================
TOPICS.append(TOPIC(
    "T13", "M4", "A Prime Puzzle", ["5.6"], "Analyze",
    "Students fill a 3 by 3 grid with primes so that each row and column multiplies to its clue, by breaking each "
    "clue into primes.",
    "Break each clue into primes and place them so that every row and column product matches.",
    [A("T13.C1", "The rules of the prime puzzle", "Understand",
       "Students work out the rules of the grid puzzle from a solved example and follow a solved puzzle in which "
       "every row and column multiplies to its clue.",
       textbook=book("5.6", "A prime puzzle"),
       teach=["Predict first: what rules could turn a grid of primes into a puzzle?",
              "Fill the grid with primes only. The product of each row is the number to its right.",
              "The product of each column is the number below it.",
              "Start with the clue that has the fewest primes in it."],
       examples=[we("5.6.q3"), we("5.6.q4")],
       key_terms=["prime", "prime factorisation"], misconceptions=["M_STOP_AT_COMPOSITE"], minutes=10),
     A("T13.C2", "Solving harder prime grids", "Apply",
       "Students solve harder grids by breaking each clue into primes and checking every row and column product.",
       textbook=[],
       teach=["Predict first: a row clue of 8 has only one prime factorisation: 2 × 2 × 2.",
              "A clue like 27 gives 3 × 3 × 3; a clue like 105 gives 3 × 5 × 7.",
              "Place primes so that every column also multiplies to its clue.",
              "Multiply every row and column to check."],
       examples=[we("5.6.q5"), we("5.6.q6")],
       key_terms=["prime factorisation"], misconceptions=["M_ORDER_MATTERS"], minutes=10),
     DOER("T13.C3", "Pull it together and do it: Prime Grid Puzzle", "prime_grid", "Apply",
          "Students fill 3 by 3 grids with primes by breaking each clue into primes and matching every row "
          "and column product.",
          ["Break each clue into primes first.",
           "Fill the tightest row or column first.",
           "Check every row and every column by multiplying."],
          items=[fio("5.6.q7", tool="prime_grid")],
          misconceptions=["M_ORDER_MATTERS"])]))

# ============================== T14 Summary ==================================================================
TOPICS.append(TOPIC(
    "T14", "M4", "Summary: Prime Time", ["Summary"], "Remember",
    None,
    "Factors and multiples, primes and composites, co-primes, prime factorisation and its two uses, and the "
    "divisibility tests.",
    [A("T14.C1", "What we found about primes", "Remember",
       "Students restate what factors, primes, composites, co-primes and prime factorisation are, and how prime "
       "factorisation checks co-primes and divisibility.",
       textbook=["If a number is divisible by another, the second number is called a factor of the first. For example, 4 is a factor of 12 because 12 is divisible by 4."] + book("5.6", "Summary", start=1, stop=8),
       teach=["Our opening question is settled: two bells meet at the first common multiple, and co-prime numbers "
              "meet only at their product.",
              "Primes have exactly two factors, composites have more, and 1 is neither.",
              "Every number above 1 has one prime factorisation, apart from order.",
              "No common prime means co-prime; the primes of one inside the other means it divides it."],
       ncert=[], video_focus=["RECAP"], minutes=8)],
    topic_type="summary"))
