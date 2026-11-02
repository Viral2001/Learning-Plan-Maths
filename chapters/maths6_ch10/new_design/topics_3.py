# -*- coding: utf-8 -*-
"""Topics T13 to T18 (module M4): border sums, the amazing grid, integer puzzles, history and Brahmagupta's rules,
the snakes and ladders game, and the summary. Book sections 10.4, 10.5, the Game and the Summary."""
from topics_common import A, DOER, TOPIC, book, fio, we

TOPICS = []
S4 = "10.4"
H_HOLLOW = "A hollow integer grid"
H_AMAZE = "An amazing grid of numbers!"

# ============================== T13 Hollow integer grids (10.4) ==============================================
TOPICS.append(TOPIC(
    "T13", "M4", "Hollow Integer Grids", [S4], "Apply",
    "Students find the border sum of a hollow grid and fill in a grid to reach a given border sum.",
    "In a hollow grid the two rows and the two columns on the border all add to the same number, the border sum, "
    "and that fact fills in missing numbers.",
    [A("T13.C1", "The border sum", "Understand",
       "Students add the four sides of a hollow grid and see that all four sums are the same.",
       textbook=book(S4, H_HOLLOW, stop=7),
       teach=["Think first: in the first grid the top row 4, −1, −3 adds to 0. Will the bottom row also give 0?",
              "Yes: top row 4 + (−1) + (−3) = 0 and bottom row (−1) + (−1) + 2 = 0. The left column and the right "
              "column also give 0.",
              "The common sum of the two rows and two columns is the border sum. Check the second grid and see "
              "whether the four sums match."],
       examples=[we("10.4.q1")],
       key_terms=["border sum", "hollow grid"], misconceptions=["M_IGNORE_SIGN", "M_GRID_CHOICE"], minutes=8),
     A("T13.C2", "Filling a grid to match a border sum", "Apply",
       "Students find the missing number of a side from the border sum and the two numbers already given.",
       textbook=book(S4, H_HOLLOW, start=7),
       teach=["Think first: a side has 4, −1 and a blank, and the border sum is 0. What goes in the blank?",
              "The three numbers must add to the border sum. 4 + (−1) = 3, and 3 + (−3) = 0, so the blank is −3.",
              "The corner numbers belong to two sides, so choose them first, then the middle numbers follow. If "
              "the corners can be changed, the grid can be filled in more than one way."],
       key_terms=["border sum", "missing number"], misconceptions=["M_GRID_CHOICE", "M_ADD_BIGGER"], minutes=8),
     DOER("T13.C3", "Pull it together and do it: Border Grid", "border_grid", "Apply",
          "Students fill hollow grids to reach a border sum, find more than one filling and make a puzzle.",
          ["Each of the four sides adds to the border sum.",
           "A missing number is the border sum minus the other two numbers on that side.",
           "A corner is shared by two sides, so many grids can be filled in more than one way."],
          items=[fio("10.4.FiO1.Q1"), fio("10.4.FiO1.Q2"), fio("10.4.FiO1.Q3"), fio("10.4.FiO1.Q4"),
                 fio("10.4.FiO1.Q5")],
          misconceptions=["M_GRID_CHOICE"])]))

# ============================== T14 An amazing grid (10.4) ===================================================
TOPICS.append(TOPIC(
    "T14", "M4", "An Amazing Grid of Numbers", [S4], "Analyze",
    "Students play the circle and strike game on a grid, find that the sum never changes, and explain why.",
    "In the amazing grid every choice of circled numbers gives the same total, because each row and each column "
    "is used exactly once.",
    [A("T14.C1", "Circle, strike and add", "Apply",
       "Students play the circle and strike out game on a grid and add the numbers they circled.",
       textbook=book(S4, H_AMAZE, stop=6),
       teach=["Think first: you circle any number, strike out its row and column, and repeat. Will the sum depend "
              "on what you choose?",
              "In the book's example the circled numbers are −1, 9, −7 and −2, and they add to −1.",
              "Play again with other choices and add each time. The sum comes out the same."],
       examples=[we("10.4.ac1")],
       key_terms=["row", "column"], misconceptions=["M_GRID_CHOICE"], minutes=8),
     A("T14.C2", "Why the sum never changes", "Analyze",
       "Students explain that each circled number comes from a different row and column, so the sum is fixed.",
       textbook=book(S4, H_AMAZE, start=6),
       teach=["Think first: look along row 2. Each number is 5 less than the number above it in row 1. Is there "
              "a pattern like this in every row?",
              "Every number in the grid is a row number plus a column number: row 2 is the first row with 5 "
              "taken off, row 3 is the first row with 2 taken off, and row 4 is the first row with 10 taken off.",
              "Each circle uses one row and one column exactly once, so the total is the sum of the first row, "
              "3 + 4 + 0 + 9 = 16, plus 0 − 5 − 2 − 10 = −17, which is −1 every time. The magic is in the way "
              "the numbers are arranged."],
       key_terms=["pattern"], misconceptions=["M_GRID_CHOICE"], minutes=10),
     DOER("T14.C3", "Pull it together and do it: Amazing Grids", None, "Analyze",
          "Students play the game on new grids, say what is special about them and make a grid of their own.",
          ["Circle one number, strike out its row and column, and repeat until none is left.",
           "The sum is the same for every choice.",
           "A grid with this magic is built from a row of numbers and a column of numbers added together."],
          items=[fio("10.4.FiO2.Q1"), fio("10.4.FiO2.Q2"), fio("10.4.FiO2.Q3")],
          misconceptions=["M_GRID_CHOICE"])]))

# ============================== T15 Integer puzzles (10.4) ===================================================
TOPICS.append(TOPIC(
    "T15", "M4", "Integer Puzzles", [S4], "Apply",
    "Students list the integers between two numbers, count years across 1 BCE and 1 CE, and use sums and "
    "differences to solve puzzles.",
    "Integers between two numbers leave out the two ends, and years before the year 1 CE have no year 0, so "
    "counting back across it needs one extra step.",
    [A("T15.C1", "Integers between two numbers", "Understand",
       "Students list all the integers between two given integers in increasing order, leaving out the ends.",
       textbook=[],
       teach=["Think first: which integers lie between −4 and 4? Do −4 and 4 count?",
              "Between −4 and 4 are −3, −2, −1, 0, 1, 2, 3. The two ends are not between themselves.",
              "When both numbers are negative, such as −8 and −15, the integers between them are −14 up to −9, "
              "listed from the smallest to the greatest."],
       key_terms=["between", "increasing order"], misconceptions=["M_BETWEEN_ENDS", "M_BIGGER_DIGIT"], minutes=6),
     A("T15.C2", "Years before and after the year 1", "Apply",
       "Students count years back from a CE year to a BCE year and say why there is no year 0.",
       textbook=[],
       teach=["Think first: the year after 1 BCE is 1 CE. Is there a year 0 in between?",
              "No. The years run ..., 2 BCE, 1 BCE, 1 CE, 2 CE, ... So going back 3 years from 2 CE gives 2 "
              "BCE: 1 CE, then 1 BCE, then 2 BCE.",
              "As a calculation, 2 − 3 = −1, and the first negative year, −1, is called 2 BCE. One extra step "
              "is needed because the year 0 is missing."],
       key_terms=["BCE", "CE"], misconceptions=["M_YEAR_ZERO"], minutes=8),
     DOER("T15.C3", "Pull it together and do it: Integer Puzzles", None, "Apply",
          "Students solve the second set of Figure it Out puzzles on integers between, sums, dice, years, "
          "sequences, cards and a string of tokens.",
          ["List integers between two numbers without the ends.",
           "A sum can be made in many ways, so test an answer by adding it up.",
           "Years across 1 BCE and 1 CE skip the year 0."],
          items=[fio("10.4.FiO3.Q1"), fio("10.4.FiO3.Q2"), fio("10.4.FiO3.Q3"), fio("10.4.FiO3.Q4"),
                 fio("10.4.FiO3.Q5"), fio("10.4.FiO3.Q6"), fio("10.4.FiO3.Q7"), fio("10.4.FiO3.Q8"),
                 fio("10.4.FiO3.Q9")],
          misconceptions=["M_BETWEEN_ENDS", "M_YEAR_ZERO", "M_SIGN_RULE_ALWAYS"])]))

# ============================== T16 A pinch of history (10.5) ================================================
TOPICS.append(TOPIC(
    "T16", "M4", "A Pinch of History and Brahmagupta's Rules", ["10.5"], "Understand",
    "Students say where negative numbers were first used, and state Brahmagupta's five rules for adding and five "
    "for subtracting with an example for each.",
    "Brahmagupta treated positive numbers, negative numbers and zero as equal numbers, and gave rules that "
    "add and subtract any of them.",
    [A("T16.C1", "Negative numbers in old accounts", "Remember",
       "Students tell where negative numbers were first used and who gave the first general treatment of them.",
       textbook=book("10.5", None, stop=4),
       teach=["Think first: where would an old trader first need a number below zero?",
              "In accounts: debts and credits. The Chinese book Jiuzhang Suanshu and the Indian writer Kautilya "
              "both write about it.",
              "In 628 CE Brahmagupta treated positive numbers, negative numbers and zero all as numbers and gave "
              "rules for adding and subtracting them."],
       key_terms=["Brahmagupta", "accounting"], misconceptions=["M_NEG_NOTHING"], minutes=6),
     A("T16.C2", "Brahmagupta's five rules for adding", "Understand",
       "Students state the five rules for adding integers and check each one with the lift.",
       textbook=book("10.5", None, start=4, stop=11),
       teach=["Think first: in Bela's lift, 2 floors up and then 3 floors up is 5 floors up. Which rule is that?",
              "Rule 1: two positives give a positive, 2 + 3 = 5. Rule 2: add two negatives without the signs and "
              "put a minus, (−2) + (−3) = −5.",
              "Rule 3: for one positive and one negative, subtract the smaller from the greater and take the sign "
              "of the greater, so 5 + (−8) = −3. Rule 4: a number plus its inverse is 0. Rule 5: adding 0 changes "
              "nothing."],
       key_terms=["rules for addition"], misconceptions=["M_SIGN_RULE_ALWAYS", "M_IGNORE_SIGN"], minutes=10),
     A("T16.C3", "Brahmagupta's five rules for subtracting", "Understand",
       "Students state the five rules for subtracting integers and check each one on the number line.",
       textbook=book("10.5", None, start=11, stop=19),
       teach=["Think first: what do you get from 2 − (−3) on the number line? From −3 to 2 you move 5 steps "
              "right.",
              "Rule 3: subtracting a negative number is the same as adding the corresponding positive number, so "
              "2 − (−3) = 2 + 3 = 5. Rule 4: a number minus itself is 0.",
              "Rule 1: 3 − 2 = 1. Rule 2: 2 − 3 = −1. Rule 5: subtracting 0 changes nothing, and 0 − 2 = −2, the "
              "inverse of 2."],
       key_terms=["rules for subtraction"], misconceptions=["M_SUB_NEG_SMALLER", "M_SUB_SMALLER"], minutes=10),
     DOER("T16.C4", "Pull it together and do it: Explain the Rules", None, "Understand",
          "Students explain each of Brahmagupta's rules with the lift or the number line and give their own "
          "example for each.",
          ["Five rules for adding and five for subtracting cover every integer.",
           "Every rule can be explained by a lift movement or a number-line jump.",
           "Subtracting a number is adding its inverse."],
          items=[fio("10.5.FiO.Q1"), fio("10.5.FiO.Q2")],
          misconceptions=["M_SIGN_RULE_ALWAYS"])]))

# ============================== T17 The game (Snakes and Ladders) ============================================
TOPICS.append(TOPIC(
    "T17", "M4", "Integers: Snakes and Ladders", ["Game"], "Apply",
    "Students play the two-dice integer game, choose whether to add or subtract the two numbers rolled, and move "
    "towards +50 or −50.",
    "Each roll gives a choice between adding and subtracting the two numbers, so a player can pick the move that "
    "suits the plan.",
    [A("T17.C1", "Rolling a positive and a negative die", "Apply",
       "Students roll one die of +1 to +6 and one of −1 to −6, then add or subtract in either order to get a "
       "move.",
       textbook=book("Game", "Rules"),
       teach=["Think first: you roll +4 and −5. Adding gives −1. What does subtracting give, in each order?",
              "(+4) + (−5) = −1, (+4) − (−5) = 9 and (−5) − (+4) = −9. A positive result moves you towards +50 and "
              "a negative result moves you towards −50.",
              "Choose the result that helps most; the winner is the first to reach +50 or −50."],
       examples=[we("10.G.ac1", steps=["Roll the +1 to +6 die and the −1 to −6 die.",
                                       "Add or subtract the two numbers in either order.",
                                       "Move that many steps: towards +50 if positive, towards −50 if negative."],
                    answer="Play the game: the first pawn to reach +50 or −50 wins.")],
       key_terms=["pawn", "two dice"], misconceptions=["M_DIE_CHOICE"], minutes=8),
     DOER("T17.C2", "Pull it together and do it: Snakes and Ladders", "snakes_ladders", "Apply",
          "Students play the two-dice integer game against a friend and choose the best move on each roll.",
          ["Add or subtract the two numbers in either order.",
           "A positive result moves towards +50, a negative result towards −50.",
           "A ladder or a snake changes the square you stand on."],
          misconceptions=["M_DIE_CHOICE"])]))

# ============================== T18 Summary ==================================================================
TOPICS.append(TOPIC(
    "T18", "M4", "Chapter Summary: The Other Side of Zero", ["Summary"], "Understand",
    "Students recall that integers extend the number line left of zero and that adding and subtracting them follow one set of rules.", "Integers extend the number line to the left of zero, and adding and subtracting them follow one set of "
        "rules.",
    [A("T18.C1", "The other side of zero, in one page", "Understand",
       "Students recall what integers are and how adding and subtracting them follow one set of rules.",
       textbook=book("Summary", None, stop=3),
       teach=["Think first: if someone asks you what the other side of zero holds, what will you say?",
              "Numbers less than zero are negative numbers; with the positive numbers and zero they make the "
              "integers, and every integer has an additive inverse.",
              "Starting Position + Movement = Target Position, and subtracting an integer is adding its inverse. "
              "Smaller numbers lie to the left of larger ones, and credits, debits, heights and temperatures all "
              "use integers."],
       ncert=["summary"], video_focus=["RECAP"], minutes=8)],
    topic_type="summary"))
