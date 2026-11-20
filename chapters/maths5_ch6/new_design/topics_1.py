# -*- coding: utf-8 -*-
"""Topics T1, T1B, T2, T3 (module M1: Equal Groups, Order and Place Value) and T4, T5 (module M2: Smart Ways to
Multiply) of Class 5 Chapter 6, The Dairy Farm. The framing intro (Daljeet Kaur's pouches hook and the free Pouch
Packer), the short idea topic T1B (equal groups, with the five opening puzzles), Order of Numbers, Multiplying by
10s, 100s and 1,000s, Many Ways to Multiply, and Doubling and Halving.
Every teaching concept has one worked example with the plan's own numbers; every book question is an FIO item of its
topic's DOER, in the book's order."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 The Dairy Farm (framing) ================================================
# The framing topic holds only the hook video and the free-try tool, and no book question. The concept video and the
# five opening puzzles follow in the short idea topic T1B.
TOPICS.append(TOPIC(
    "T1", "M1", "The Dairy Farm", ["Chapter opening"], "Understand",
    "",
    "Daljeet Kaur has 60 butter milk pouches on her packing table. She packs them in groups of 2 and in groups of 3. "
    "Try the packing table yourself and find out what other groups she can make.",
    [A("T1.C1", "Daljeet Kaur's Pouches", "Understand",
       "",
       textbook=["By now, we know several multiplication facts. We have also learnt how to multiply two numbers. We "
                 "will continue to explore different ways of multiplying in this chapter."],
       teach=["Predict first: Daljeet Kaur has 60 butter milk pouches on her packing table. She packs them in groups "
              "of 2. Then she packs the same pouches in groups of 3. Can she make other equal groups too?",
              "Daljeet Kaur runs a milk processing unit. Today her packing table has 60 butter milk pouches.",
              "First she puts the pouches in pairs, with 2 pouches in every group. No pouch is left out.",
              "Then she mixes them up and packs the same 60 pouches in groups of 3. Every group has 3 pouches.",
              "The pouches are the same, but the groups are different. How many groups does she get each time?",
              "What other groups can she make? Think about it, then pack the pouches yourself on the next screen."],
       ncert=["open.intro"], key_terms=["pouches", "groups", "total"],
       video_focus=["HOOK"], enrichment=True, minutes=4),
     DOER("T1.C3", "Pouch Packer: Explore", "pouch_packer", "Understand",
          "",
          ["Daljeet Kaur has 60 butter milk pouches on her packing table.",
           "Pack them in equal groups and read the groups on the screen.",
           "Turn the picture and see what stays the same."],
          misconceptions=["M_ONE_WAY"], role="try_it", enrichment=True)],
    topic_type="framing", key_terms=["pouches", "groups", "total"]))

# ============================== T1B Equal Groups: Many Ways to Make a Total ================================
TOPICS.append(TOPIC(
    "T1B", "M1", "Equal Groups: Many Ways to Make a Total", ["Chapter opening", "Let Us Think"], "Understand",
    "Students find the different equal groups that make one total, write each way as number of groups × group size, "
    "and use this to solve the five opening puzzles.",
    "One total can be packed in equal groups in many ways. Each way has a number of groups and a group size, and "
    "number of groups × group size = total.",
    [A("T1B.C1", "Equal Groups: Many Ways to Make a Total", "Understand",
       "Students find the different ways to pack one total in equal groups and write each way as number of groups × "
       "group size.",
       teach=["Predict first: Daljeet Kaur has 36 pouches. She packs them in equal groups of 4. Can she pack the same "
              "36 pouches in other equal groups too?",
              "Yes. 9 groups of 4 pouches make 36, and 4 groups of 9 pouches make 36 too. The pouches do not change, "
              "only the way we group them.",
              "Every way has two numbers: the number of groups and the group size. The total is the number of groups "
              "times the group size.",
              "36 pouches can be packed as 18 groups of 2, 12 groups of 3, 9 groups of 4 or 6 groups of 6. Each way is "
              "a different multiplication for the same total.",
              "Turn the picture on its side and the rows become columns: 9 rows of 4 pouches turn into 4 rows of 9 "
              "pouches. It is still the same 36 pouches.",
              "Rule: a total can be packed in equal groups in many ways. Number of groups × group size = total."],
       examples=[WE("Daljeet Kaur has 36 butter milk pouches. Pack them in equal groups of 2, 3, 4 and 6. How many "
                    "groups does each way make? Write each way as number of groups × group size, and then turn the "
                    "picture of the groups of 4.",
                    ["The total is 36 pouches. Groups of 2: we need 18 groups, because 2 × 18 = 36. So 18 × 2 = 36.",
                     "Groups of 3: we need 12 groups, because 3 × 12 = 36. So 12 × 3 = 36.",
                     "Groups of 4: we need 9 groups, because 4 × 9 = 36. So 9 × 4 = 36.",
                     "Groups of 6: we need 6 groups, because 6 × 6 = 36. So 6 × 6 = 36.",
                     "Turn the picture of 9 groups of 4. The rows become columns and it shows 4 groups of 9, so "
                     "4 × 9 = 36.",
                     "Check: every way uses all 36 pouches. 18 × 2 = 36, 12 × 3 = 36, 9 × 4 = 36 and 6 × 6 = 36."],
                    "18 × 2 = 36, 12 × 3 = 36, 9 × 4 = 36 and 6 × 6 = 36. Turned, 9 × 4 = 36 becomes 4 × 9 = 36. Each "
                    "way uses all 36 pouches")],
       key_terms=["equal groups", "total", "number of groups", "group size"],
       misconceptions=["M_ONE_WAY"], minutes=5),
     DOER("T1B.C2", "Practice: Let Us Think", None, "Understand",
          "Students think through the five opening puzzles: find the numbers behind shapes, place digits for a "
          "product close to 100, find the equal groups of 60 pouches, use clues to find a number and make numbers "
          "from a grid.",
          ["One total can be packed in equal groups in many ways.",
           "Read each way as number of groups × group size.",
           "Use the clues and your trials to find a number, one clue at a time."],
          items=[FIO("lt.shapes", "Let Us Think: Q1 shapes",
                     "The given shapes stand for numbers between 1 and 24. The same shape denotes the same number "
                     "across all problems. Find the numbers hiding in all the shapes.",
                     ["The book does not say if two shapes may share a number. Here different shapes stand for "
                      "different numbers.",
                      "(d): the diamond × the pentagon = the diamond, so the pentagon is 1.",
                      "(b): the rectangle × the rectangle is the white shape, 24 or less. Try 3: 3 × 3 = 9.",
                      "(a): try the circle as 4: 3 × 4 = 12, so the triangle is 12.",
                      "(c): the parallelogram × the diamond = 12. Try 2 × 6 = 12.",
                      "(e): 2 × 4 = 8, so the half circle is 8.",
                      "(f): 8 × 3 = 24 and 2 × 12 = 24, so both sides match.",
                      "Other sets fit too (5 in all), and the pentagon is always 1. This is one set.",
                      "Check: 1, 2, 3, 4, 6, 8, 9 and 12 are all different, and every sentence is true."],
                     "Sample answer: pentagon 1, parallelogram 2, rectangle 3, circle 4, diamond 6, half circle 8, "
                     "white shape 9, triangle 12. Other sets fit too. Your answer may differ.",
                     kind="prompt",
                     q_figure="Six shape sentences: (a) blue rectangle × pink circle = purple triangle. (b) blue "
                              "rectangle × blue rectangle = white shape with notched sides. (c) yellow parallelogram "
                              "× orange diamond = purple triangle. (d) orange diamond × green pentagon = orange "
                              "diamond. (e) yellow parallelogram × pink circle = light blue half circle. (f) light "
                              "blue half circle × blue rectangle = yellow parallelogram × purple triangle.",
                     s_figure="The same six shape sentences with the number written inside every shape: pentagon 1, "
                              "parallelogram 2, rectangle 3, circle 4, diamond 6, half circle 8, white shape 9 and "
                              "triangle 12."),
                 FIO("lt.digits", "Let Us Think: Q2 digits near 100",
                     "Place the digits 2, 5, and 3 appropriately to get a product close to 100. Share your reasoning "
                     "in class.",
                     ["The frame is a two-digit number × a one-digit number, using 2, 5 and 3 once each.",
                      "One-digit number 2: 53 × 2 = 106 and 35 × 2 = 70.",
                      "One-digit number 3: 52 × 3 = 156 and 25 × 3 = 75.",
                      "One-digit number 5: 32 × 5 = 160 and 23 × 5 = 115.",
                      "Gaps from 100: 106 − 100 = 6 and 115 − 100 = 15. All the others are 25 or more away.",
                      "Why: 50 × 2 = 100, so put 5 in the tens place and use 2 as the one-digit number. The 3 goes in "
                      "the ones place.",
                      "Check: 53 × 2 = 106 is the closest, only 6 from 100."],
                     "53 × 2 = 106, only 6 more than 100. The next closest is 23 × 5 = 115.",
                     kind="prompt",
                     q_figure="A multiplication frame: a two-digit number made of two empty boxes, a times sign, a "
                              "one-digit number in one empty box, and a line for the result.",
                     s_figure="The frame filled in: 5 and 3 in the two boxes of the two-digit number, 2 in the "
                              "one-digit box and 106 on the answer line."),
                 FIO("lt.pouches", "Let Us Think: Q3 pouches",
                     "A dairy has packed butter milk pouches in the following manner. Find the number of pouches "
                     "kept in each arrangement. One is done for you. (a): 30 × 2 = 60. (b): ___ × ___ = 60. "
                     "(c): ___ × ___ = 60. (d): ___ × ___ = 60. What other groups can you make?",
                     ["The book gives no letters, so the pictures are lettered (a) to (d) in the order printed. The "
                      "first number counts the groups, as in 30 × 2 = 60.",
                      "(b): 4 groups across and 5 down make 4 × 5 = 20 groups of 3.",
                      "So (b) is 20 × 3 = 60.",
                      "(c): one block is 2 wide and 5 tall, so it has 2 × 5 = 10 pouches.",
                      "So (c) is 6 × 10 = 60, with 6 blocks.",
                      "(d): 5 rows of 12 pouches make 5 × 12 = 60.",
                      "Other groups: any two numbers that make 60, like 4 × 15, 3 × 20, 2 × 30 and 1 × 60, and each one "
                      "swapped.",
                      "Check: 20 × 3 = 60, 6 × 10 = 60 and 5 × 12 = 60."],
                     "(b): 20 × 3 = 60; (c): 6 × 10 = 60; (d): 5 × 12 = 60. Other groups: 4 × 15 = 60, 2 × 30 = 60, "
                     "1 × 60 = 60 and their swaps.",
                     kind="prompt",
                     q_figure="Four arrangements of the same 60 butter milk pouches. (a) pouches in pairs, 6 pairs "
                              "across and 5 pairs down, done for you as 30 × 2 = 60. (b) pouches in groups of 3 side "
                              "by side, 4 groups across and 5 down. (c) 6 blocks side by side, each block 2 pouches "
                              "wide and 5 pouches tall. (d) 5 rows of 12 pouches.",
                     s_figure="The four arrangements with the groups counted: (a) 30 groups of 2, (b) 20 groups of "
                              "3, (c) 6 blocks of 10 pouches, (d) 5 rows of 12 pouches."),
                 FIO("lt.number", "Let Us Think: Q4 which number am I",
                     "Which number am I? I am a two-digit number. Find me with the help of the following clues. "
                     "(a): I am greater than 8. (b): I am not a multiple of 4. (c): I am a multiple of 9. (d): I am "
                     "an odd number. (e): I am not a multiple of 11. (f): I am less than 50. (g): My ones digit is "
                     "even. (h): My tens digit is odd. Did you use all the clues to find the number? Which clues did "
                     "not help you in finding the number?",
                     ["Use the number chart: the number is from 10 to 99.",
                      "Clues (c) and (f): the multiples of 9 under 50 are 18, 27, 36 and 45.",
                      "Clue (b): 36 goes out, because 4 × 9 = 36.",
                      "Clue (g): the ones digit is even, so 27 and 45 go out. 18 is left.",
                      "18 is also greater than 8 (a), not a multiple of 11 (e), and its tens digit 1 is odd (h).",
                      "Clue (d) says odd, but 18 is even. An odd number has an odd ones digit, so (d) and (g) cannot "
                      "both be true. No number fits all eight clues.",
                      "Check: clues (a), (e) and (h) were not needed, and 18 fits every clue except (d)."],
                     "18. It fits every clue except (d), which cannot be true together with (g), so no number fits "
                     "all eight. Clues (a), (e) and (h) did not help.",
                     kind="prompt",
                     q_figure="A number chart from 0 to 99 in 10 rows of 10.",
                     s_figure="The number chart with 18, 27, 36 and 45 marked, 27, 36 and 45 crossed out one by one, "
                              "and 18 circled."),
                 FIO("lt.make", "Let Us Think: Q5 make your own numbers",
                     "Make your own numbers. Choose any two numbers and one operation from the grid. Try to make all "
                     "the numbers between 0 and 20. For example, 2 can be formed as 4 − 2. Could you make all the "
                     "numbers? Which numbers could you not make? Is it possible to make these numbers using three "
                     "numbers? You can use two operations, if needed. Which numbers between 0 and 20 can you get in "
                     "more than one way?",
                     ["The book does not say if one number may be used twice. Here we use two different numbers, one "
                      "operation and a whole-number answer.",
                      "Some numbers: 1 = 4 − 3, 2 = 4 − 2, 3 = 5 − 2, 4 = 12 ÷ 3, 5 = 10 ÷ 2, 6 = 4 + 2, 7 = 10 − 3, 8 "
                      "= 4 × 2, 9 = 12 − 3, 10 = 5 × 2.",
                      "More: 11 = 36 − 25, 12 = 10 + 2, 13 = 10 + 3, 14 = 10 + 4, 15 = 5 × 3, 16 = 12 + 4, 17 = 12 + 5, "
                      "18 = 36 ÷ 2, 20 = 5 × 4.",
                      "0 and 19 never come out, so we could not make them.",
                      "With three numbers: 100 ÷ 25 = 4 and 4 − 4 = 0, so 0 = (100 ÷ 25) − 4. Also 10 − 4 = 6 and 25 − "
                      "6 = 19, so 25 − (10 − 4) = 19.",
                      "More than one way: 2 = 5 − 3 or 10 ÷ 5 or 12 − 10, and 5 = 25 ÷ 5 or 10 − 5 or 10 ÷ 2. Only 11, "
                      "16, 17 and 18 have one way.",
                      "Check: 36 − 25 = 11, 12 + 4 = 16, 12 + 5 = 17 and 36 ÷ 2 = 18 are true."],
                     "Sample answer: 0 and 19 cannot be made with two numbers. With three, 0 = (100 ÷ 25) − 4 and "
                     "25 − (10 − 4) = 19. More than one way: 1 to 10, 12 to 15 and 20. Your answer may differ.",
                     kind="prompt",
                     q_figure="A grid of nine number tiles, 100, 25, 5 in the first row, 10, 2, 36 in the second row "
                              "and 12, 4, 3 in the third row, and four operation tiles: −, ×, +, ÷.")],
          misconceptions=["M_ONE_WAY"])],
    key_terms=["equal groups", "total", "number of groups", "group size"]))

# ============================== T2 Order of Numbers in Multiplication ======================================
TOPICS.append(TOPIC(
    "T2", "M1", "Order of Numbers in Multiplication", ["Order of Numbers in Multiplication"], "Understand",
    "Students show that swapping the number of groups and the group size does not change the product, and that any "
    "number times 0 is 0.",
    "When the number of groups and the group size swap places, the total stays the same: 7 rows of 12 packets and 12 "
    "rows of 7 packets are the same 84 packets. A number times 0 is 0, in either order.",
    [A("T2.C1", "Change the Order, Keep the Product", "Understand",
       "Students show that changing the order of the two numbers in a multiplication does not change the product, and "
       "that a number times 0 is 0.",
       textbook=["The number of groups and the group size are interchanged in each case above, but the total number "
                 "of butter packets remain the same."],
       teach=["Predict first: Daljeet Kaur packs butter packets in 7 rows of 12. Then she turns the tray so that there "
              "are 12 rows of 7 packets. Does the total number of packets change?",
              "No, it stays the same. Turning the tray moves the same packets to new places. No packet is added and "
              "none is taken away.",
              "7 rows of 12 packets is 7 × 12. Here the number of groups is 7 and the group size is 12. 12 rows of 7 "
              "packets is 12 × 7. Now the number of groups is 12 and the group size is 7.",
              "The number of groups and the group size are swapped, but the total is the same: 7 × 12 = 84 and "
              "12 × 7 = 84.",
              "What about 0? 5 groups of 0 packets hold no packets, and 0 groups of 5 packets hold no packets. So "
              "5 × 0 = 0 and 0 × 5 = 0. Any number times 0 is 0.",
              "Rule: changing the order of the numbers does not change the product."],
       examples=[WE("Daljeet Kaur has a tray of butter packets with 7 rows of 12 packets. She turns the tray so that "
                    "it has 12 rows of 7 packets. Find the total number of packets before and after the turn, and "
                    "say what stays the same.",
                    ["Before the turn there are 7 rows of 12 packets. The number of groups is 7 and the group size "
                     "is 12, so the total is 7 × 12.",
                     "Split 12 into 10 and 2: 7 × 10 = 70 and 7 × 2 = 14, and 70 + 14 = 84. So 7 × 12 = 84.",
                     "After the turn there are 12 rows of 7 packets. The number of groups is 12 and the group size "
                     "is 7, so the total is 12 × 7.",
                     "Split 12 into 10 and 2: 10 × 7 = 70 and 2 × 7 = 14, and 70 + 14 = 84. So 12 × 7 = 84.",
                     "The two numbers swapped places, but the packets are the same, so the total is the same: "
                     "7 × 12 = 84 = 12 × 7.",
                     "Check: turning the tray does not add or take away a packet, so both totals must match, and "
                     "84 = 84."],
                    "Both totals are 84 packets: 7 × 12 = 84 and 12 × 7 = 84. The order changed, but the product "
                    "stayed the same")],
       ncert=["ord.text"], key_terms=["order", "product", "number of groups", "group size"],
       misconceptions=["M_ORDER_CHANGES", "M_ZERO_TIMES"], minutes=5),
     DOER("T2.C2", "Practice: Order of Numbers", None, "Understand",
          "Students find the products of swapped pairs, describe the pattern that the order does not change the "
          "product, and explain why a number times 0 is 0.",
          ["Swapping the number of groups and the group size does not change the product.",
           "A number times 0 is 0, in either order.",
           "If you know 12 × 7 = 84, you also know 7 × 12 = 84."],
          items=[FIO("ord.pairs", "Order of Numbers: butter packets",
                     "Daljeet Kaur runs a milk processing unit. She has arranged the butter packets in the "
                     "following ways. Find the number of butter packets in each case. What pattern do you notice (or "
                     "observe)? (a): 2 × 3 = ___ and 3 × 2 = ___. (b): 5 × 8 = ___ and 8 × 5 = ___. The two big "
                     "arrays: 6 × 13 = ___ and 13 × 6 = ___. (e): 10 × 5 = ___ and 5 × 10 = ___. (f): 8 × 20 = ___ "
                     "and 20 × 8 = ___. (g): 12 × 9 = ___ and 9 × 12 = ___.",
                     ["(a): 2 × 3 = 6 and 3 × 2 = 6.",
                      "(b): 5 × 8 = 40 and 8 × 5 = 40.",
                      "Big arrays: 6 × 13 = 6 × 10 + 6 × 3 = 60 + 18 = 78.",
                      "13 × 6 = 10 × 6 + 3 × 6 = 60 + 18 = 78.",
                      "(e): 10 × 5 = 50 and 5 × 10 = 50.",
                      "(f): 8 × 20 = 160 and 20 × 8 = 160.",
                      "(g): 12 × 9 = 10 × 9 + 2 × 9 = 90 + 18 = 108, and 9 × 12 = 108.",
                      "Pattern: every pair has the same total. Swapping the number of groups and the group size keeps "
                      "the product.",
                      "Check: the two products in every pair match."],
                     "(a): 6, 6; (b): 40, 40; big arrays: 78, 78; (e): 50, 50; (f): 160, 160; (g): 108, 108. The "
                     "order does not change the product.",
                     kind="prompt",
                     q_figure="Pairs of packet arrangements. (a) 2 rows of 3 packets and 3 rows of 2 packets. (b) 5 "
                              "rows of 8 packets and 8 rows of 5 packets. Two big arrays: 6 rows of 13 packets "
                              "(number of groups 6, group size 13) and 13 rows of 6 packets. Then three pairs of "
                              "number sentences only, (e), (f) and (g).",
                     s_figure="The same pairs with the totals written beside them: 6, 40, and 78 for both big "
                              "arrays."),
                 FIO("ord.zero", "Order of Numbers: zero",
                     "What is 9 × 0? 0 × 9? Is this true for the product of any two numbers? Discuss in class.",
                     ["9 × 0 means 9 groups with 0 packets in each group. There are no packets at all, so 9 × 0 = 0.",
                      "0 × 9 means 0 groups of 9 packets. There are no groups, so there are no packets: 0 × 9 = 0.",
                      "Both are 0, so the order did not change the product here either.",
                      "Try other numbers: 5 × 0 = 0 and 0 × 5 = 0, and 100 × 0 = 0 and 0 × 100 = 0.",
                      "For any two numbers, swapping them never changes the product. And any number times 0 is 0.",
                      "Check: 9 groups of 0 and 0 groups of 9 both hold 0 packets."],
                     "9 × 0 = 0 and 0 × 9 = 0. Yes: the order never changes a product, and any number times 0 is 0.",
                     kind="prompt")],
          misconceptions=["M_ORDER_CHANGES", "M_ZERO_TIMES"])],
    key_terms=["order", "product", "number of groups", "group size"]))

# ============================== T3 Multiplying by 10s, 100s and 1,000s =====================================
TOPICS.append(TOPIC(
    "T3", "M1", "Multiplying by 10s, 100s and 1,000s", ["Patterns in Multiplication by 10s and 100s"], "Apply",
    "Students multiply by 10, 100 and 1,000 by moving each digit to the left, and multiply tens, hundreds and "
    "thousands by multiplying the digits and writing the zeros.",
    "Multiplying by 10 moves every digit one place to the left, by 100 two places and by 1,000 three places, and zeros "
    "fill the empty places. To multiply tens, hundreds or thousands, multiply the digits and write the zeros of both "
    "numbers.",
    [A("T3.C1", "Multiplying by 10 and 100", "Apply",
       "Students multiply a number by 10 and by 100 by moving each digit one or two places to the left and filling "
       "the empty places with zeros.",
       teach=["Predict first: the number 37 is multiplied by 10. Which way does each digit move on the place value "
              "board, and what fills the empty ones place?",
              "37 is 3 tens and 7 ones. 10 times 37 is 10 groups of 37. The 3 tens become 3 hundreds, and the 7 ones "
              "become 7 tens.",
              "So each digit moves one place to the left, and a 0 fills the empty ones place: 37 × 10 = 370.",
              "For 100, each digit moves two places to the left, and two zeros fill the empty places: "
              "37 × 100 = 3,700.",
              "Do not just say 'add a zero'. The zero is there because every digit moved one place to the left and "
              "the ones place became empty.",
              "Rule: multiplying by 10 moves every digit one place to the left, and multiplying by 100 moves every "
              "digit two places to the left. Zeros fill the empty places."],
       examples=[WE("A box holds 37 butter packets. How many packets are in 10 boxes? How many are in 100 boxes? "
                    "Show how the digits of 37 move on the place value board.",
                    ["37 is 3 tens and 7 ones. Put the 3 in the tens place and the 7 in the ones place on the board.",
                     "10 boxes: multiply by 10. Every digit moves one place to the left. The 3 moves to the "
                     "hundreds place and the 7 moves to the tens place.",
                     "The ones place is now empty, so a 0 goes there. The number is 3 hundreds, 7 tens and 0 ones: "
                     "37 × 10 = 370.",
                     "100 boxes: multiply by 100. Every digit moves two places to the left. The 3 moves to the "
                     "thousands place and the 7 moves to the hundreds place.",
                     "The tens and ones places are empty, so two zeros go there. The number is 3,700: "
                     "37 × 100 = 3,700.",
                     "Check: 100 is ten times ten, so 37 × 10 × 10 = 370 × 10 = 3,700."],
                    "10 boxes hold 370 packets and 100 boxes hold 3,700 packets: 37 × 10 = 370 and "
                    "37 × 100 = 3,700")],
       ncert=["pat.note"], key_terms=["place value", "digits", "zeros", "multiply by 10"],
       misconceptions=["M_ADD_ZERO"], minutes=5),
     A("T3.C2", "Multiplying Tens, Hundreds and Thousands", "Apply",
       "Students multiply tens, hundreds and thousands by multiplying the digits first and then writing the zeros of "
       "both numbers.",
       textbook=["Notice the underlined numbers. Remember, we can multiply numbers in any order."],
       teach=["Predict first: 40 × 50 means 4 tens times 5 tens. Is the answer 20, 200 or 2,000?",
              "40 is 4 × 10 and 50 is 5 × 10, so 40 × 50 = 4 × 10 × 5 × 10.",
              "The order does not change the product, so multiply the digits first: 4 × 5 = 20. Then multiply the two "
              "tens: 10 × 10 = 100.",
              "That makes 20 hundreds, which is 2,000. So 40 × 50 = 2,000.",
              "Thousands work the same way. For 9 × 4,000, multiply the digits: 9 × 4 = 36. Then write the 3 zeros of "
              "4,000 at the end: 36,000.",
              "Rule: multiply the digits that are not zero, then write all the zeros of both numbers at the end."],
       examples=[WE("The counting board shows 60 × 70. Find the product by multiplying the digits and writing the "
                    "zeros. How many zeros does the answer have at the end?",
                    ["60 is 6 tens, or 6 × 10. 70 is 7 tens, or 7 × 10.",
                     "So 60 × 70 = 6 × 10 × 7 × 10.",
                     "The order does not change the product, so multiply the digits first: 6 × 7 = 42.",
                     "Then multiply the two tens: ten times ten is 100.",
                     "42 times 100 is 42 hundreds, which is 4,200: the digits 4 and 2 move two places to the left "
                     "and two zeros fill the empty places.",
                     "So 60 × 70 = 4,200. The two zeros at the end come from 60 and 70, one from each number.",
                     "Check: 60 × 70 = 60 × 7 × 10 = 420 × 10 = 4,200."],
                    "60 × 70 = 4,200: multiply 6 × 7 = 42 and write the two zeros")],
       ncert=["pat.order"], key_terms=["tens", "hundreds", "thousands", "zeros", "digits"],
       misconceptions=["M_ZERO_COUNT"], minutes=6),
     DOER("T3.C3", "Practice: Place Value Shifter", "place_value_shifter", "Apply",
          "Students use place value tables to multiply by 10, 100 and 1,000 by moving digits, and to multiply tens, "
          "hundreds and thousands by multiplying the digits and writing the zeros.",
          ["Multiplying by 10 moves every digit one place to the left, by 100 two places, and by 1,000 three places. "
           "Zeros fill the empty places.",
           "To multiply tens, hundreds or thousands, multiply the digits that are not zero and then write the zeros "
           "of both numbers.",
           "The order does not change the product: 60 × 70 = 6 × 10 × 7 × 10 = 42 × 100 = 4,200."],
          items=[FIO("pat.q1", "Patterns in Multiplication by 10s and 100s: Q1 revise",
                     "Let us revise multiplication by 10 and by 100. (a): 4 × 10 = ___ (b): 20 × 10 = ___ (c): "
                     "10 × 40 = ___ (d): 10 × 10 = 100 (e): 20 × 50 = ___ (f): 80 × 10 = ___ (g): 3 × 100 = 100 × 3 "
                     "= 300 (h): 8 × 100 = ___ = ___ (i): 10 × 100 = ___ = ___",
                     ["(a): the 4 moves one place to the left and a 0 fills the ones place, so 4 × 10 = 40.",
                      "(b): 2 tens times 10 is 2 hundreds, so 20 × 10 = 200.",
                      "(c): the order does not change the product, so 10 × 40 = 40 × 10 = 400.",
                      "(d): this one is given: 10 × 10 = 100.",
                      "(e): multiply the digits and write the zeros: 20 × 50 = 2 × 5 × 10 × 10 = 10 × 100 = 1,000.",
                      "(f): 80 × 10 = 800.",
                      "(g): this one is given: 3 × 100 = 100 × 3 = 300.",
                      "(h): 8 × 100 = 100 × 8 = 800. The book leaves two blanks here, so the first blank is the "
                      "swapped product and the second is the answer.",
                      "(i): 10 × 100 = 100 × 10 = 1,000. The two blanks are read the same way as in (h).",
                      "Check: 10 × 100 = 1,000 has 3 zeros, one from 10 and two from 100."],
                     "(a): 40; (b): 200; (c): 400; (e): 1,000; (f): 800; (h): 100 × 8 = 800; (i): 100 × 10 = 1,000",
                     kind="exercise"),
                 FIO("pat.q2", "Patterns in Multiplication by 10s and 100s: Q2 find the answers",
                     "Find answers to the following questions. Fill in the table below and describe the pattern. "
                     "Discuss in class. 100 × 90 = ___. 400 × 10 = ___. 60 × 50 = ___. 30 × 20 = 600. 700 × 4 = ___. "
                     "10 × 45 = ___. Table (columns Problem, Th, H, T, O): 10 × 45 = (blank row); 30 × 20 = (6 in "
                     "H, 0 in T, 0 in O are filled); 400 × 10 = (blank row); 700 × 8 = (blank row); 100 × 90 = (9 "
                     "in Th, 0, 0, 0 are filled). How should we write 450 in the table?",
                     ["The boxes: 100 × 90 = 9,000 and 400 × 10 = 4,000.",
                      "60 × 50: 6 × 5 = 30, then 2 zeros: 3,000.",
                      "700 × 4: 7 × 4 = 28, then 2 zeros: 2,800.",
                      "10 × 45 = 450. The box 30 × 20 = 600 is given.",
                      "Table: 10 × 45 = 450 has hundreds 4, tens 5, ones 0. 400 × 10 = 4,000 has thousands 4, then 0, "
                      "0, 0.",
                      "The row says 700 × 8 but the box says 700 × 4. Solve both: 700 × 8 = 5,600 (thousands 5, "
                      "hundreds 6, tens 0, ones 0).",
                      "Write 450 as hundreds 4, tens 5, ones 0. The 0 in the ones place comes from multiplying by 10.",
                      "Pattern: multiply the digits, then write the zeros of both numbers.",
                      "Check: 60 × 50 has 2 zeros and 6 × 5 = 30 adds 1 more, so 3,000 has 3 zeros."],
                     "100 × 90 = 9,000; 400 × 10 = 4,000; 60 × 50 = 3,000; 700 × 4 = 2,800; 10 × 45 = 450; "
                     "700 × 8 = 5,600. Write 450 as 4 hundreds, 5 tens, 0 ones.",
                     kind="exercise",
                     q_figure="Six rounded boxes with the products 100 × 90, 400 × 10, 60 × 50, 30 × 20 = 600 (filled "
                              "in), 700 × 4 and 10 × 45, and a table with columns Problem, Th, H, T, O and five rows: "
                              "10 × 45, 30 × 20 (6, 0, 0 filled in), 400 × 10, 700 × 8 and 100 × 90 (9, 0, 0, 0 "
                              "filled in).",
                     s_figure="The table filled in digit by digit: 10 × 45 = 450, 30 × 20 = 600, 400 × 10 = 4,000, "
                              "700 × 8 = 5,600 and 100 × 90 = 9,000."),
                 FIO("pat.q2b", "Patterns in Multiplication by 10s and 100s: Q2 more tables",
                     "Fill in the two place value tables (columns Problem, Th, H, T, O) for these problems and "
                     "describe the pattern. First table: 60 × 50, 220 × 20, 11 × 300. Second table: 80 × 90, "
                     "10 × 63, 40 × 12.",
                     ["First table: 60 × 50: 6 × 5 = 30, then 2 zeros: 3,000.",
                      "220 × 20: 22 × 2 = 44, then 2 zeros: 4,400.",
                      "11 × 300: 11 × 3 = 33, then 2 zeros: 3,300.",
                      "Second table: 80 × 90: 8 × 9 = 72, then 2 zeros: 7,200.",
                      "10 × 63 = 630.",
                      "40 × 12: 4 × 12 = 48, then 1 zero: 480.",
                      "Put each digit in its place. For example, 4,400 is thousands 4, hundreds 4, tens 0, ones 0.",
                      "Pattern: multiply the digits, then write the zeros of both numbers.",
                      "Check: 220 × 20 has 2 zeros, one from each number."],
                     "First: 3,000; 4,400; 3,300. Second: 7,200; 630; 480. Multiply the digits, then write the "
                     "zeros of both numbers.",
                     kind="exercise",
                     q_figure="Two tables, each with columns Problem, Th, H, T, O and three rows. The first table has "
                              "the problems 60 × 50, 220 × 20 and 11 × 300, and the second has 80 × 90, 10 × 63 and "
                              "40 × 12. Every digit box is empty.",
                     s_figure="The two tables filled in digit by digit: 3,000, 4,400 and 3,300 in the first, and "
                              "7,200, 630 and 480 in the second."),
                 FIO("pat.thousand", "Patterns in Multiplication by 10s and 100s: multiplying by 1,000",
                     "What will happen if we multiply numbers by 1,000? 2 × 1,000 is 2 thousand, which is written "
                     "2,000. 5 × 1,000 is 5 thousand, which is written 5,000. 10 × 1,000 is 10 thousand, which is "
                     "written 10,000. 20 × 1,000 is 20 thousand, which is written 20,000.",
                     ["Look at the given facts: 2 × 1,000 = 2,000, 5 × 1,000 = 5,000, 10 × 1,000 = 10,000 and "
                      "20 × 1,000 = 20,000.",
                      "Each answer is the number followed by three zeros: 2 and 000, 5 and 000, 10 and 000, and 20 "
                      "and 000.",
                      "On the place value board every digit moves three places to the left, because 1,000 is "
                      "10 × 10 × 10. The empty ones, tens and hundreds places are filled with zeros.",
                      "Try one more: 3 × 1,000 = 3,000. And 10 × 1,000 = 10,000: the 1 moves to the ten thousands "
                      "place.",
                      "Check: 3 × 1,000 = 3 × 10 × 10 × 10 = 30 × 10 × 10 = 300 × 10 = 3,000."],
                     "Multiplying by 1,000 moves every digit three places to the left and puts three zeros at the "
                     "end: 3 × 1,000 = 3,000 and 10 × 1,000 = 10,000.",
                     kind="prompt",
                     q_figure="Two green tags marked 1,000 beside 2 × 1,000 and five green tags marked 1,000 beside "
                              "5 × 1,000.",
                     s_figure="A place value board with 3 in the thousands place and zeros in the hundreds, tens and "
                              "ones places, and an arrow showing the 3 moved three places to the left from the ones "
                              "place."),
                 FIO("pat.tk", "Patterns in Multiplication by 10s and 100s: table for 1,000",
                     "Let us fill in the table and observe the patterns. Table (columns Problem, TTh, Th, H, T, O): "
                     "2 × 1,000 = 2,000; 5 × 1,000 = 5,000; 10 × 1,000 = 10,000; 20 × 1,000 = 20,000 (these four "
                     "rows are already filled in); then 3 × 5,000 = ___; 8 × 3,000 = ___; 5 × 7,000 = ___.",
                     ["3 × 5,000: 3 × 5 = 15, then 3 zeros, so 3 × 5,000 = 15,000. Ten thousands 1, thousands 5, "
                      "hundreds 0, tens 0, ones 0.",
                      "8 × 3,000: 8 × 3 = 24, then 3 zeros, so 8 × 3,000 = 24,000. Ten thousands 2, thousands 4, "
                      "hundreds 0, tens 0, ones 0.",
                      "5 × 7,000: 5 × 7 = 35, then 3 zeros, so 5 × 7,000 = 35,000. Ten thousands 3, thousands 5, "
                      "hundreds 0, tens 0, ones 0.",
                      "Pattern: multiply the digits (3 × 5, 8 × 3 and 5 × 7), then write the three zeros of the "
                      "thousand.",
                      "Check: 3 × 5,000 = 3 × 5 × 1,000 = 15 × 1,000 = 15,000."],
                     "3 × 5,000 = 15,000; 8 × 3,000 = 24,000; 5 × 7,000 = 35,000. Multiply the digits, then write "
                     "three zeros.",
                     kind="exercise",
                     q_figure="A table with columns Problem, TTh, Th, H, T, O; the first four rows filled digit by "
                              "digit, the last three rows empty.",
                     s_figure="The table with the last three rows filled digit by digit: 15,000, 24,000 and 35,000."),
                 FIO("pat.th", "Patterns in Multiplication by 10s and 100s: table for 100",
                     "Let us fill in the table and observe the patterns. Table (columns Problem, TTh, Th, H, T, O): "
                     "20 × 100 = ___; 40 × 500 = ___; 60 × 300 = ___; 600 × 30 = ___; 80 × 900 = ___; 70 × 600 = "
                     "___; 5 × 7,000 = ___",
                     ["20 × 100: 2 × 1 = 2, then 3 zeros: 2,000.",
                      "40 × 500: 4 × 5 = 20, then 3 zeros: 20,000.",
                      "60 × 300: 6 × 3 = 18, then 3 zeros: 18,000.",
                      "600 × 30: 6 × 3 = 18, then 3 zeros: 18,000, the same as 60 × 300.",
                      "80 × 900: 8 × 9 = 72, then 3 zeros: 72,000.",
                      "70 × 600: 7 × 6 = 42, then 3 zeros: 42,000.",
                      "5 × 7,000: 5 × 7 = 35, then 3 zeros: 35,000.",
                      "Put each digit in its place. For example, 18,000 is ten thousands 1, thousands 8, then 0, 0, 0.",
                      "Pattern: multiply the digits, then write the zeros of both numbers.",
                      "Check: 40 × 500 has 3 zeros and 4 × 5 = 20 adds 1 more, so 20,000 has 4 zeros."],
                     "2,000; 20,000; 18,000; 18,000; 72,000; 42,000; 35,000. Multiply the digits, then write the "
                     "zeros of both numbers.",
                     kind="exercise",
                     q_figure="A table with columns Problem, TTh, Th, H, T, O and seven rows with the problems "
                              "20 × 100, 40 × 500, 60 × 300, 600 × 30, 80 × 900, 70 × 600 and 5 × 7,000. Every digit "
                              "box is empty.",
                     s_figure="The table filled in digit by digit: 2,000, 20,000, 18,000, 18,000, 72,000, 42,000 and "
                              "35,000.")],
          misconceptions=["M_ZERO_COUNT", "M_ADD_ZERO"])],
    key_terms=["place value", "zeros", "digits", "multiply by 10"]))

# ============================== T4 Many Ways to Multiply ===================================================
TOPICS.append(TOPIC(
    "T4", "M2", "Many Ways to Multiply", ["Many Ways to Multiply"], "Apply",
    "Students split one number into parts, multiply each part and add the parts, and check that different ways of "
    "multiplying give the same product.",
    "To multiply, split one number into parts, multiply each part and add the parts: 6 × 14 = 60 + 24 = 84. Other "
    "ways, like halving one number and doubling the other, or rounding and taking away the extra, can give the same "
    "product.",
    [A("T4.C1", "Break a Number into Parts", "Apply",
       "Students split one number into parts, multiply each part and add the parts to find a product.",
       teach=["Predict first: 6 rows of 14 packets. A friend splits the 14 columns into 10 columns and 4 columns. Is "
              "the total of the two blocks the same as the total of the whole array?",
              "Yes. The 10 columns hold 6 × 10 = 60 packets and the 4 columns hold 6 × 4 = 24 packets.",
              "Add the two blocks: 60 + 24 = 84. It is the same packets as 6 rows of 14, so 6 × 14 = 60 + 24 = 84.",
              "Both parts must be multiplied. If you multiply only one part, you leave out the packets of the other "
              "block.",
              "Choose a split that makes easy products. Splitting 14 into 10 and 4 is easy, because 10 times a number "
              "just moves its digits.",
              "Rule: split one number, multiply each part, then add the parts."],
       examples=[WE("Daljeet Kaur packs butter packets in 6 rows of 14. Find the total by splitting 14 into 10 and 4.",
                    ["6 rows of 14 packets is 6 × 14. Split 14 into 10 and 4, because 10 + 4 = 14.",
                     "Multiply the first part: 6 × 10 = 60.",
                     "Multiply the second part: 6 × 4 = 24.",
                     "Add the two parts: 60 + 24 = 84.",
                     "So 6 × 14 = 6 × 10 + 6 × 4 = 60 + 24 = 84.",
                     "Check: swap the order. 14 × 6 = 10 × 6 + 4 × 6 = 60 + 24 = 84, the same."],
                    "6 × 14 = 6 × 10 + 6 × 4 = 60 + 24 = 84 packets")],
       key_terms=["split", "parts", "product", "add"],
       misconceptions=["M_SPLIT_ONE"], minutes=5),
     DOER("T4.C2", "Practice: Many Ways to Multiply", None, "Apply",
          "Students check that five different ways of finding one product all give the same answer, and explain why "
          "each way works.",
          ["Split one number into parts, multiply each part and add the parts.",
           "Halving one number and doubling the other keeps the product.",
           "Rounding to a friendly number and taking away the extra keeps the product too.",
           "Different ways can give the same product."],
          items=[FIO("many.18x5", "Many Ways to Multiply: 18 × 5",
                     "What is 18 × 5? Five children found it in five ways. (1) Half of 18 is 9. 9 × 5 is 45 and "
                     "9 × 5 is 45. I added 45 and 45 together to get 90. (2) First, I doubled 18 to get 36. Then I "
                     "doubled 36 to get 72 and then I added 18 to 72 to get 90. (3) I separated 18 into 8 and 10. "
                     "8 × 5 is 40. 10 × 5 is 50. Then I added 40 and 50 together to get 90. (4) 18 × 5 = 9 × 10. So, "
                     "90. (5) I did 20 × 5, which is 100. Then I took away 2 × 5, which is 10. So, 100 − 10 = 90. Do "
                     "you think they are all correct? Why do you think so?",
                     ["18 × 5 = 10 × 5 + 8 × 5 = 50 + 40 = 90.",
                      "(1): half of 18 is 9 and 9 × 5 = 45, so 45 + 45 = 90. Correct.",
                      "(2): 18 × 2 = 36 and 36 × 2 = 72, then 72 + 18 = 90. Correct.",
                      "(3): 18 = 8 + 10, so 8 × 5 + 10 × 5 = 40 + 50 = 90. Correct.",
                      "(4): half of 18 is 9 and double 5 is 10, so 9 × 10 = 90. Correct.",
                      "(5): 20 × 5 = 100 and 18 is 2 less than 20, so take away 2 × 5 = 10: 100 − 10 = 90. Correct.",
                      "All five are right: each one splits or changes a number and keeps the product the same.",
                      "Check: every way gives 90 = 18 × 5."],
                     "Yes, all five are correct and give 18 × 5 = 90. Each way splits or changes a number in a way "
                     "that keeps the product the same.",
                     kind="prompt",
                     q_figure="Two blue and green number boxes 18 and 5 with a times sign, and five children each "
                              "saying how they found the product.",
                     s_figure="An array of 5 rows of 18 packets split by a line into a block of 10 columns and a "
                              "block of 8 columns, with the totals 50 and 40 and the sum 90 beside it.")],
          misconceptions=["M_SPLIT_ONE"])],
    key_terms=["split", "parts", "product", "ways"]))

# ============================== T5 Doubling and Halving ====================================================
TOPICS.append(TOPIC(
    "T5", "M2", "Doubling and Halving", ["Doubling and Halving"], "Apply",
    "Students halve one number and double the other to make a multiplication easier, and explain why this works well "
    "with 5 and 25.",
    "Cut an array of packets in the middle and put the halves together a new way: halve one number and double the "
    "other, and the product stays the same. It works well with 5 and 25, because doubling 5 makes 10 and doubling 25 "
    "twice makes 100.",
    [A("T5.C1", "Halve One Number, Double the Other", "Apply",
       "Students halve one number and double the other and show that the product stays the same.",
       textbook=["Butter packets are arranged in the following ways. Let us find some strategies to calculate the "
                 "total number of packets."],
       teach=["Predict first: 8 rows of 13 packets are cut across the middle into two equal blocks, and the blocks are "
              "put side by side. How many rows does the new array have, and how many packets are in each row?",
              "Each block has 4 rows of 13 packets. Side by side, each of the 4 rows holds 13 + 13 = 26 packets.",
              "So 8 × 13 becomes 4 × 26. We halved the 8 and doubled the 13.",
              "No packet is added or lost, the packets only move, so the total is the same: 8 × 13 = 4 × 26 = 104.",
              "Halve one number and double the other. Do not halve both or double both: 10 × 12 = 120, but "
              "5 × 6 = 30 and 20 × 24 = 480.",
              "Rule: halve one number and double the other, and the product stays the same."],
       examples=[WE("Butter packets are arranged in 8 rows of 13. Cut the rows across the middle, put the two blocks "
                    "side by side, and find the new multiplication. Show that the total is the same.",
                    ["The array has 8 rows of 13 packets, so the total is 8 × 13 = 8 × 10 + 8 × 3 = 80 + 24 = 104.",
                     "Cut across the middle: half of 8 rows is 4 rows. There are two blocks, each with 4 rows of 13 "
                     "packets.",
                     "Put the blocks side by side. Each new row has 13 + 13 = 26 packets.",
                     "The new array has 4 rows of 26 packets, so the total is 4 × 26 = 4 × 20 + 4 × 6 = 80 + 24 = "
                     "104.",
                     "We halved the 8 to get 4 and doubled the 13 to get 26, so 8 × 13 = 4 × 26 = 104.",
                     "Check: the two totals are 104 and 104. The same packets only moved, so none were gained or "
                     "lost."],
                    "8 × 13 becomes 4 × 26, and both are 104 packets. Half of 8 is 4 and double 13 is 26")],
       ncert=["dh.intro"], key_terms=["halve", "double", "product", "array"],
       misconceptions=["M_HALVE_BOTH", "M_DOUBLE_BOTH"], minutes=6),
     A("T5.C2", "Halving and Doubling with 5 and 25", "Apply",
       "Students use halving and doubling to multiply with 5 and 25, and explain why this works well with these "
       "numbers.",
       textbook=["This halving and doubling strategy works well when we have to multiply with numbers like 5 and 25. "
                 "Discuss why?"],
       teach=["Predict first: 25 × 28. Halve the 28 and double the 25, and then do it once more. Do you reach a "
              "number that is easy to multiply?",
              "Halve 28 to get 14 and double 25 to get 50: 25 × 28 = 50 × 14.",
              "Halve 14 to get 7 and double 50 to get 100: 50 × 14 = 100 × 7. Now it is easy, because "
              "100 × 7 = 700.",
              "5 needs only one step, because 5 is half of 10. Halve 46 to get 23 and double 5 to get 10: "
              "5 × 46 = 10 × 23 = 230.",
              "Why 5 and 25? Doubling 5 once gives 10, and doubling 25 twice gives 100, because 4 × 25 = 100. "
              "Multiplying by 10 or 100 only moves the digits, so the product comes quickly.",
              "Rule: with a 5, halve the other number once and double the 5 to make 10. With a 25, do it twice to "
              "make 100."],
       examples=[WE("Find 25 × 28 by halving one number and doubling the other, again and again, until one number is "
                    "100.",
                    ["Doubling 25 twice reaches 100: 25 × 2 = 50 and 50 × 2 = 100. So we halve the 28 twice.",
                     "Double the 25 once and halve the 28 once: half of 28 is 14, so 25 × 28 = 50 × 14.",
                     "Double the 50 again and halve the 14 again: half of 14 is 7, so 50 × 14 = 100 × 7.",
                     "Now it is easy: 100 × 7 = 700, because multiplying by 100 moves the 7 two places to the left.",
                     "So 25 × 28 = 50 × 14 = 100 × 7 = 700.",
                     "Check: 25 × 28 = 25 × 20 + 25 × 8 = 500 + 200 = 700."],
                    "25 × 28 = 50 × 14 = 100 × 7 = 700")],
       ncert=["dh.why"], key_terms=["halve", "double", "5 and 25", "easy"],
       misconceptions=["M_HALVE_BOTH"], minutes=6),
     DOER("T5.C3", "Practice: Halve and Double Packets", "halve_double_packets", "Apply",
          "Students halve one number and double the other to find products, check that the product stays the same, "
          "and write their own examples where halving and doubling help.",
          ["Halve one number and double the other, and the product stays the same.",
           "Cut the array of packets in the middle and put the halves together a new way.",
           "Halving and doubling works well with 5 and 25, because it makes a 10 or a 100."],
          items=[FIO("ex.dh", "Example 1: halving and doubling 3 × 18",
                     "Butter packets are arranged in the following way. Let us find a strategy to calculate the "
                     "total number of packets. 3 rows of 18 packets are cut in the middle and the two halves are put "
                     "one below the other: 3 × 18 becomes 6 × 9 = 54 (Double the 3, Half the 18). Discuss why these "
                     "are the same.",
                     ["3 rows of 18 packets: 3 × 18 = 3 × 10 + 3 × 8 = 30 + 24 = 54 packets.",
                      "Cut the 3 rows in the middle: each row of 18 splits into 9 and 9. There are two blocks of 3 "
                      "rows of 9 packets.",
                      "Put one block below the other. Now there are 3 + 3 = 6 rows of 9 packets.",
                      "6 × 9 = 54 packets.",
                      "The same packets only moved, so 3 × 18 = 6 × 9 = 54. We doubled the 3 to get 6 and halved "
                      "the 18 to get 9.",
                      "Check: 54 packets before and 54 packets after."],
                     "3 × 18 = 6 × 9 = 54. The cut packets only moved, so the total stays 54: double the 3, half the "
                     "18.",
                     kind="example",
                     q_figure="A packet arrangement of 3 rows of 18 with a scissors line in the middle; an arrow "
                              "marked Double and an arrow marked Half lead from 3 × 18 to 6 × 9 = 54, with two blocks "
                              "of 3 rows of 9 packets shown one below the other.",
                     s_figure="The 3 by 18 array cut in the middle into two 3 by 9 blocks, and the blocks stacked as "
                              "a 6 by 9 array, with 54 packets written beside both."),
                 FIO("dh.b", "Doubling and Halving: 22 × 5",
                     "Butter packets are arranged in 22 rows of 5 packets. The arrangement is cut in the middle and "
                     "the two halves are put side by side. 22 × 5 becomes ___ × ___ = ____.",
                     ["22 rows of 5 packets: 22 × 5 = 20 × 5 + 2 × 5 = 100 + 10 = 110 packets.",
                      "Cut the 22 rows in the middle: half of 22 is 11, so there are two blocks of 11 rows of 5 "
                      "packets.",
                      "Put the blocks side by side. Each new row has 5 + 5 = 10 packets.",
                      "The new array has 11 rows of 10 packets: 11 × 10 = 110.",
                      "So 22 × 5 becomes 11 × 10 = 110. Half of 22 is 11 and double 5 is 10.",
                      "Check: 110 packets before and 110 packets after."],
                     "22 × 5 becomes 11 × 10 = 110. Half of 22 is 11 and double 5 is 10.",
                     kind="prompt",
                     q_figure="A tall arrangement of 22 rows of 5 packets with a scissors line across the middle, "
                              "and two equal arrangements of the halves side by side.",
                     s_figure="The two halves side by side as one array of 11 rows of 10 packets, with 110 written "
                              "beside it."),
                 FIO("dh.c", "Doubling and Halving: Q(c) like the previous ones",
                     "Solve the following problems like the previous ones. Halve one number, double the other: "
                     "14 × 3 = ___, 16 × 4 = ___, 38 × 5 = ___, 35 × 14 = ___. For each, write the new problem as "
                     "___ × ___.",
                     ["14 × 3: half of 14 is 7 and double 3 is 6. The new problem is 7 × 6 = 42, so 14 × 3 = 42.",
                      "16 × 4: half of 16 is 8 and double 4 is 8. The new problem is 8 × 8 = 64, so 16 × 4 = 64.",
                      "38 × 5: half of 38 is 19 and double 5 is 10. The new problem is 19 × 10 = 190, so "
                      "38 × 5 = 190.",
                      "35 × 14: the book does not label the arrows of this box. 35 is odd and cannot be halved into a "
                      "whole number, so halve the 14 and double the 35. Half of 14 is 7 and double 35 is 70. The new "
                      "problem is 70 × 7 = 490, so 35 × 14 = 490.",
                      "Check: 14 × 3 = 42, 16 × 4 = 64, 38 × 5 = 190 and 35 × 14 = 490, and each new problem has the "
                      "same product."],
                     "14 × 3: 7 × 6 = 42; 16 × 4: 8 × 8 = 64; 38 × 5: 19 × 10 = 190; 35 × 14: 70 × 7 = 490",
                     kind="exercise",
                     q_figure="Four boxes, each with the problem on top, two arrows marked Half and Double leading to "
                              "two empty boxes with a times sign (the box of 35 × 14 has unlabelled arrows).",
                     s_figure="The four boxes filled in: 7 × 6, 8 × 8, 19 × 10 and 70 × 7, with the arrows marked "
                              "Half and Double."),
                 FIO("dh.d", "Doubling and Halving: Q(d) halve and double",
                     "Find the product by halving and doubling either the multiplier or the multiplicand. "
                     "(1): 5 × 18 (2): 50 × 28 (3): 15 × 22 (4): 25 × 12 (5): 12 × 45 (6): 16 × 45",
                     ["(1): half of 18 is 9 and double 5 is 10. 5 × 18 = 10 × 9 = 90.",
                      "(2): half of 28 is 14 and double 50 is 100. 50 × 28 = 100 × 14 = 1,400.",
                      "(3): half of 22 is 11 and double 15 is 30. 15 × 22 = 30 × 11 = 330.",
                      "(4): half of 12 is 6 and double 25 is 50. Do it again: half of 6 is 3 and double 50 is 100. "
                      "25 × 12 = 50 × 6 = 100 × 3 = 300.",
                      "(5): half of 12 is 6 and double 45 is 90. 12 × 45 = 6 × 90 = 540.",
                      "(6): half of 16 is 8 and double 45 is 90. 16 × 45 = 8 × 90 = 720.",
                      "Check: the long way agrees, 5 × 18 = 5 × 10 + 5 × 8 = 50 + 40 = 90, and the other products "
                      "are 1,400, 330, 300, 540 and 720."],
                     "(1): 90; (2): 1,400; (3): 330; (4): 300; (5): 540; (6): 720",
                     kind="exercise"),
                 FIO("dh.e", "Doubling and Halving: Q(e) your own examples",
                     "Give 5 examples of multiplication problems where halving and doubling will help in finding the "
                     "product easily. Find the products as well.",
                     ["Look for a 5, a 25 or a 50, or an even number that halves into an easy number. Here are five "
                      "examples.",
                      "5 × 24: half of 24 is 12 and double 5 is 10. 5 × 24 = 10 × 12 = 120.",
                      "25 × 24: half of 24 is 12 and double 25 is 50. 25 × 24 = 50 × 12 = 600.",
                      "15 × 14: half of 14 is 7 and double 15 is 30. 15 × 14 = 30 × 7 = 210.",
                      "50 × 36: half of 36 is 18 and double 50 is 100. 50 × 36 = 100 × 18 = 1,800.",
                      "35 × 12: half of 12 is 6 and double 35 is 70. 35 × 12 = 70 × 6 = 420.",
                      "Check: each pair has the same product, 120, 600, 210, 1,800 and 420. The numbers in these "
                      "examples are practice values."],
                     "Sample answer: 5 × 24 = 120, 25 × 24 = 600, 15 × 14 = 210, 50 × 36 = 1,800, 35 × 12 = 420. Your "
                     "answer may differ.",
                     kind="prompt")],
          misconceptions=["M_HALVE_BOTH", "M_DOUBLE_BOTH"])],
    key_terms=["halve", "double", "product", "array"]))
