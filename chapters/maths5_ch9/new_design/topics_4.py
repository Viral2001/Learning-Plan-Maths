# -*- coding: utf-8 -*-
"""Topics T8 to T11: How the Quotient Changes (module M3), True or False Statements, Always, Sometimes or Never True, and the
Chapter Revision summary (module M4). Every teaching concept has one worked example with the plan's own numbers (practice
values); every book question is an FIO item of its topic's DOER, in the book's order. The book's printed oddities are kept
and noted: Part B prints 384 ÷ 8 twice, and 86 ÷ 2 does not follow from 192 ÷ 4 by doubling or halving."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T8 How the Quotient Changes ================================================
assert 12 * 40 == 480 and 960 // 12 == 80 and 480 // 24 == 20 and 960 // 24 == 40
assert 12 * 80 == 960 and 24 * 20 == 480 and 24 * 40 == 960 and 240 // 12 == 20 and 240 // 24 == 10
assert 34 * 10 == 340 and 340 // 17 == 20 and 680 // 17 == 40 and 10 * 2 * 2 == 40 and 680 // 34 == 20 and 170 // 17 == 10
assert 680 // 68 == 10 and 17 * 20 == 340 and 17 * 40 == 680 and 34 * 20 == 680 and 17 * 10 == 170 and 68 * 10 == 680
assert 4 * 48 == 192 and 192 // 8 == 24 and 384 // 8 == 48 and 384 // 4 == 96 and 86 // 2 == 43 and 96 // 2 == 48
assert 11 * 32 == 352 and 704 // 22 == 32 and 704 // 11 == 64 and 352 // 22 == 16 and 352 * 4 == 1408 and 1408 // 44 == 32
assert 22 * 32 == 704 and 11 * 64 == 704 and 22 * 16 == 352 and 44 * 32 == 1408

TOPICS.append(TOPIC(
    "T8", "M3", "How the Quotient Changes", ["Let Us Solve"], "Analyze",
    "Students predict how the quotient is affected when the dividend or the divisor is doubled or halved, and use given "
    "divisions to find related ones.",
    "Think of a rectangle with the dividend as its area, the divisor as one side and the quotient as the other side. Doubling "
    "the dividend doubles the quotient, doubling the divisor halves it, and doubling both keeps it the same.",
    [A("T8.C1", "How the Quotient Changes", "Analyze",
       "Students predict how the quotient is affected when the dividend or the divisor is doubled or halved, or both, and "
       "write related divisions.",
       textbook=["Find the solutions for part A. Observe the relations between the quotient, divisor and dividend and use it "
                 "to answer parts B and C."],
       teach=["Predict first: 480 ÷ 12 = 40. If you double 480 and still divide by 12, will the answer be double, half or "
              "the same?",
              "Think of a rectangle. Its area is the dividend N, one side is the divisor D and the other side is the "
              "quotient Q, so N = D × Q.",
              "Double the dividend: 960 ÷ 12 = 80. The area doubled and one side stayed, so the other side, the quotient, "
              "doubled.",
              "Double the divisor: 480 ÷ 24 = 20. The area stayed and one side doubled, so the other side, the quotient, is "
              "halved.",
              "Double both: 960 ÷ 24 = 40. The area doubled and one side doubled, so the quotient stays the same.",
              "Rule: double the dividend and the quotient doubles. Double the divisor and the quotient halves. Double both "
              "and the quotient is the same."],
       examples=[WE("480 ÷ 12 = 40 (practice values). Without dividing, find 960 ÷ 12, 480 ÷ 24 and 960 ÷ 24.",
                    ["Start with 480 ÷ 12 = 40, because 12 × 40 = 480.",
                     "960 is double 480 and the divisor is the same, so the quotient doubles: 960 ÷ 12 = 80.",
                     "24 is double 12 and the dividend is the same, so the quotient is halved: 480 ÷ 24 = 20.",
                     "960 is double 480 and 24 is double 12, so the quotient is the same: 960 ÷ 24 = 40.",
                     "Check: 12 × 80 = 960, 24 × 20 = 480 and 24 × 40 = 960."],
                    "960 ÷ 12 = 80, 480 ÷ 24 = 20 and 960 ÷ 24 = 40")],
       key_terms=["quotient", "dividend", "divisor", "doubled", "halved"], misconceptions=["M_DIVISOR_DOUBLE"], minutes=6),
     DOER("T8.C2", "Practice: Quotient Change", "quotient_change", "Analyze",
          "Students use a given division to find the related divisions of parts A, B and C, saying how the dividend and the "
          "divisor were altered and what happened to the quotient.",
          ["Double the dividend and the quotient doubles.",
           "Double the divisor and the quotient halves.",
           "Double or halve both and the quotient is the same."],
          items=[
              FIO("ls2.q5a", "Let Us Solve (relations): Q5 part A",
                  "Find the solutions for part A. Observe the relations between the quotient, divisor and dividend and use it "
                  "to answer parts B and C. A. (a): 340 ÷ 34 = 10; (b): 340 ÷ 17 = ___; (c): 680 ÷ 17 = ___; (d): 680 ÷ 34 = "
                  "___; (e): 170 ÷ 17 = ___; (f): 680 ÷ 68 = ___.",
                  ["(a): 340 ÷ 34 = 10 is given, because 34 × 10 = 340.",
                   "(b): 340 ÷ 17: the divisor 17 is half of 34 and the dividend is the same, so the quotient doubles: "
                   "340 ÷ 17 = 20.",
                   "(c): 680 ÷ 17: the dividend 680 is double 340 and the divisor 17 is half of 34, so the quotient doubles "
                   "twice: 10 × 2 × 2 = 40.",
                   "(d): 680 ÷ 34: the dividend is double and the divisor is the same, so the quotient doubles: 680 ÷ 34 = 20.",
                   "(e): 170 ÷ 17: the dividend and the divisor are both halved, so the quotient is the same: 170 ÷ 17 = 10.",
                   "(f): 680 ÷ 68: the dividend and the divisor are both doubled, so the quotient is the same: 680 ÷ 68 = 10.",
                   "Check: 17 × 20 = 340, 17 × 40 = 680, 34 × 20 = 680, 17 × 10 = 170 and 68 × 10 = 680."],
                  "(a): 10; (b): 20; (c): 40; (d): 20; (e): 10; (f): 10", kind="exercise"),
              FIO("ls2.q5b", "Let Us Solve (relations): Q5 part B",
                  "B. (a): 192 ÷ 4 = 48; (b): 192 ÷ 8 = ___; (c): 384 ÷ 8 = ___; (d): 384 ÷ 4 = ___; (e): 384 ÷ 8 = ___; (f): "
                  "86 ÷ 2 = ___.",
                  ["(a): 192 ÷ 4 = 48 is given, because 4 × 48 = 192.",
                   "(b): 192 ÷ 8: the divisor is doubled and the dividend is the same, so the quotient is halved: 192 ÷ 8 = 24.",
                   "(c): 384 ÷ 8: the dividend 384 is double 192 and the divisor 8 is double 4, so the quotient is the same: "
                   "384 ÷ 8 = 48.",
                   "(d): 384 ÷ 4: the dividend is doubled and the divisor is the same, so the quotient doubles: 384 ÷ 4 = 96.",
                   "(e): the book prints 384 ÷ 8 again, so the answer is the same as (c): 48.",
                   "(f): 86 ÷ 2 does not follow from 192 ÷ 4 by doubling or halving, so divide directly: half of 86 is 43, so "
                   "86 ÷ 2 = 43. The book may mean 96 ÷ 2 = 48, which halves both numbers of 192 ÷ 4.",
                   "Check: 8 × 24 = 192, 8 × 48 = 384, 4 × 96 = 384 and 2 × 43 = 86."],
                  "(a): 48; (b): 24; (c): 48; (d): 96; (e): 48; (f): 43", kind="exercise"),
              FIO("ls2.q5c", "Let Us Solve (relations): Q5 part C",
                  "C. (a): 352 ÷ 11 = 32; (b): 704 ÷ 22 = ___; (c): 704 ÷ 11 = ___; (d): 352 ÷ 22 = ___; (e): 1,408 ÷ 44 = ___.",
                  ["(a): 352 ÷ 11 = 32 is given, because 11 × 32 = 352.",
                   "(b): 704 ÷ 22: 704 is double 352 and 22 is double 11, so the quotient is the same: 704 ÷ 22 = 32.",
                   "(c): 704 ÷ 11: the dividend is doubled and the divisor is the same, so the quotient doubles: 704 ÷ 11 = 64.",
                   "(d): 352 ÷ 22: the divisor is doubled and the dividend is the same, so the quotient is halved: 352 ÷ 22 = 16.",
                   "(e): 1,408 ÷ 44: 1,408 is 4 times 352 and 44 is 4 times 11, so the quotient is the same: 1,408 ÷ 44 = 32.",
                   "Check: 22 × 32 = 704, 11 × 64 = 704, 22 × 16 = 352 and 44 × 32 = 1,408."],
                  "(a): 32; (b): 32; (c): 64; (d): 16; (e): 32", kind="exercise")],
          misconceptions=["M_DIVISOR_DOUBLE"])],
    key_terms=["quotient", "dividend", "divisor"]))

# ============================== T9 True or False Statements ================================================
assert 6 * 5 == 30 == 20 + 10 and 18 // 3 == 6 and 2 * 4 == 8 and 9 * 4 == 36 and 36 - 16 == 20 and 20 + 16 == 36
assert 8 * 9 == 72 == 70 + 2 and 20 - 6 == 14 and 7 * 3 == 21 and 48 // 3 == 16 == 4 * 4 and 89 - 9 == 80 and 90 + 0 == 90
assert 25 + 10 == 35 == 45 - 10 and 7 * 6 == 42 and 42 - 17 == 25 and 25 + 17 == 42 and 87 + 6 == 93 and 93 // 31 == 3
assert 3 * 31 == 93 and 74 - 4 == 70 and 70 - 63 == 7 and 63 + 7 == 70 and 16 // 2 == 8 and 8 * 9 == 72 and 72 // 9 == 8

TOPICS.append(TOPIC(
    "T9", "M4", "True or False Statements", ["Mathematical Statements"], "Apply",
    "Students decide if a statement is true by finding the value of both sides of the equal sign, and complete a statement so "
    "that both sides have the same value.",
    "A statement with an equal sign is true when both sides have the same value. Find the value of each side, compare them, "
    "and when a number is missing make the two sides the same.",
    [A("T9.C1", "Both Sides of the Equal Sign", "Apply",
       "Students find the value of both sides of an equal sign, decide if the statement is true or false, and complete a "
       "statement so it is true.",
       textbook=["A true sentence is one where both sides of the '=' sign have the same value."],
       teach=["Predict first: is 6 × 5 = 20 + 10 true or false? Find the value of each side before you decide.",
              "A statement with an equal sign is true when both sides have the same value.",
              "6 × 5 = 30 and 20 + 10 = 30. Both sides are 30, so the statement is true.",
              "Now compare 18 ÷ 3 with 2 × 4. The first is 6 and the second is 8. They are different, so a statement that says they are equal is false.",
              "To complete 9 × 4 = ___ + 16: the left side is 36, so the blank must be 36 − 16 = 20. Check: 20 + 16 = 36.",
              "The equal sign does not mean that the answer comes next. It means both sides have the same value.",
              "Rule: find the value of both sides. The same value is true, different values is false."],
       examples=[WE("Decide if the statement that 6 × 5 equals 20 + 10 is true or false, and the same for the statement that "
                    "18 ÷ 3 equals 2 × 4, and complete 9 × 4 = ___ + 16 (practice values).",
                    ["6 × 5 = 30 and 20 + 10 = 30. The two sides have the same value, so the first statement is true.",
                     "18 ÷ 3 = 6 and 2 × 4 = 8. The two sides are different, so the second statement is false.",
                     "For the third statement the left side is 9 × 4 = 36.",
                     "The blank must make the right side 36 too, so the blank is 36 − 16 = 20.",
                     "Check: 20 + 16 = 36, which is the left side."],
                    "The first is true, the second is false, and the blank is 20")],
       ncert=["st.def"], key_terms=["equal sign", "both sides", "true", "false"], misconceptions=["M_EQUAL_ANSWER"],
       minutes=5),
     DOER("T9.C2", "Practice: Equal Balance", "equal_balance", "Apply",
          "Students find the value of both sides to decide if each statement is true or false, and complete statements so that "
          "both sides are equal.",
          ["Find the value of the left side and of the right side.",
           "The same value on both sides makes a true statement.",
           "A missing number makes the two sides the same."],
          items=[
              FIO("st.q1", "Mathematical Statements (true or false): Q1",
                  "Find out whether the following statements are True (T) or False (F). A true sentence is one where both "
                  "sides of the equal sign have the same value. (a): 8 × 9 = 70 + 2; (b): 20 − 6 = 7 × 3; (c): 48 ÷ 3 = 4 × 4; "
                  "(d): 89 − 9 = 90 + 0; (e): 25 + 10 = 45 − 10.",
                  ["Find the value of both sides of each statement and compare.",
                   "(a): 8 × 9 = 72 and 70 + 2 = 72. The same value, so True.",
                   "(b): 20 − 6 = 14 and 7 × 3 = 21. Different values, so False.",
                   "(c): 48 ÷ 3 = 16 and 4 × 4 = 16. The same value, so True.",
                   "(d): 89 − 9 = 80 and 90 + 0 = 90. Different values, so False.",
                   "(e): 25 + 10 = 35 and 45 − 10 = 35. The same value, so True."],
                  "(a): T; (b): F; (c): T; (d): F; (e): T", kind="exercise"),
              FIO("st.q2", "Mathematical Statements (true or false): Q2 complete the statements",
                  "Complete the following statements such that they are true. (a): 7 × 6 = ___ + 17; (b): 87 + 6 = ___ × 31; "
                  "(c): 63 + ___ = 74 − 4; (d): ___ ÷ 9 = 16 ÷ 2.",
                  ["Find the side that has no blank, then make the other side the same.",
                   "(a): the left side 7 × 6 is 42, so the blank is 42 − 17 = 25. Check: 25 + 17 = 42.",
                   "(b): the left side 87 + 6 is 93, so the blank is 93 ÷ 31 = 3. Check: 3 × 31 = 93.",
                   "(c): the right side 74 − 4 is 70, so the blank is 70 − 63 = 7. Check: 63 + 7 = 70.",
                   "(d): the right side 16 ÷ 2 is 8, so the blank is 8 × 9 = 72. Check: 72 ÷ 9 = 8."],
                  "(a): 25; (b): 3; (c): 7; (d): 72", kind="exercise")],
          misconceptions=["M_EQUAL_ANSWER"])],
    key_terms=["equal sign", "both sides", "true", "false"]))

# ============================== T10 Always, Sometimes or Never True =========================================
assert 4 + 2 == 6 and 10 + 2 == 12 and 16 + 2 == 18 and 4 + 1 == 5 and 10 + 1 == 11 and 3 * 4 == 12 and 3 * 5 == 15
assert 1 + 3 == 4 and 3 + 5 == 8 and 7 + 9 == 16 and 5 + 11 == 16 and 9 + 9 == 18 and 11 + 13 == 24 and 15 + 1 == 16
assert 2 * 3 == 6 and 2 * 5 == 10 and 2 * 7 == 14 and 2 * 9 == 18 and 20 + 10 == 30 and 12 + 10 == 22 and 8 - 3 == 5
assert 6 * 8 == 48 == 12 * 4 and 5 * 8 == 40 == 10 * 4 and 5 * 4 == 20 and 5 * 3 == 15 and 8 // 2 == 4 and 12 // 2 == 6

TOPICS.append(TOPIC(
    "T10", "M4", "Always, Sometimes or Never True", ["Mathematical Statements"], "Analyze",
    "Students test a statement with examples and decide if it is always true, sometimes true or never true, using one example "
    "that fails to show it is not always true.",
    "Test a statement with several numbers. If no example fails it is always true, if no example works it is never true, and if "
    "some work and some fail it is sometimes true. One example that fails is enough to show it is not always true.",
    [A("T10.C1", "Always, Sometimes or Never True", "Analyze",
       "Students test a statement with several number examples and decide if it is always true, sometimes true or never true.",
       textbook=["Always true", "Never true", "Sometimes true"],
       teach=["Predict first: is \"Adding 2 to an even number gives an even number\" always, sometimes or never true? Test it "
              "with some numbers.",
              "Test with examples: 4 + 2 = 6, 10 + 2 = 12 and 16 + 2 = 18. All are even. No example fails, so it is always "
              "true.",
              "Test \"Adding 1 to an even number gives an even number\": 4 + 1 = 5 and 10 + 1 = 11 are odd. No example "
              "works, so it is never true.",
              "Test \"Multiplying a number by 3 gives an even number\": 3 × 4 = 12 is even, but 3 × 5 = 15 is odd. Some "
              "work and some fail, so it is sometimes true.",
              "One example that fails shows a statement is not always true. One example that works shows it is not never "
              "true.",
              "Many examples that work do not prove a statement is always true. Look for an example that fails.",
              "Rule: always true means no example fails, never true means no example works, sometimes true means some work "
              "and some fail."],
       examples=[WE("Decide if each statement is always, sometimes or never true (practice values): adding 2 to an even number "
                    "gives an even number; adding 1 to an even number gives an even number; multiplying a number by 3 gives "
                    "an even number.",
                    ["Statement 1: test 4 + 2 = 6, 10 + 2 = 12 and 16 + 2 = 18. All are even and none fails, so it is "
                     "always true.",
                     "Statement 2: test 4 + 1 = 5 and 10 + 1 = 11. Both are odd and none works, so it is never true.",
                     "Statement 3: 3 × 4 = 12 is even, and 3 × 5 = 15 is odd. One works and one fails, so it is sometimes "
                     "true.",
                     "One example that fails is enough to show a statement is not always true."],
                    "The first is always true, the second is never true, and the third is sometimes true")],
       ncert=["st.labels"], key_terms=["always true", "never true", "sometimes true", "examples"],
       misconceptions=["M_ONE_EXAMPLE", "M_HALF_EVEN"], minutes=6),
     DOER("T10.C2", "Practice: Always, Sometimes, Never", "always_never", "Analyze",
          "Students test the book's statements with examples, give examples that work or fail, and decide if each is always, "
          "sometimes or never true.",
          ["Test a statement with several numbers.",
           "If no example fails it is always true. If no example works it is never true.",
           "If some work and some fail it is sometimes true."],
          items=[
              FIO("st.q3a", "Mathematical Statements (always, sometimes, never): Q3 (a)",
                  "Think about the following statements and find examples as suggested below. (a): “When two odd numbers are "
                  "added, the sum is even.” Find 5 examples for the above statement. Can you find an example to show that the "
                  "statement can be false?",
                  ["The statement: when two odd numbers are added, the sum is even.",
                   "Five examples: 1 + 3 = 4, 3 + 5 = 8, 7 + 9 = 16, 5 + 11 = 16 and 9 + 9 = 18. All the sums are even.",
                   "Try more: 11 + 13 = 24 and 15 + 1 = 16. These sums are even too.",
                   "Why: each odd number has one left over when counted in pairs, and the two left overs make one more pair, "
                   "so the sum has none left over.",
                   "No example shows the statement false, so it is always true."],
                  "Sample answer: 1 + 3 = 4, 3 + 5 = 8, 7 + 9 = 16, 5 + 11 = 16, 9 + 9 = 18; none is false, so always true. "
                  "Your answer may differ",
                  kind="exercise"),
              FIO("st.q3b", "Mathematical Statements (always, sometimes, never): Q3 (b)",
                  "(b): “Multiplying a number by 2 can give an odd number.” Give some example for this statement. Can you find "
                  "any?",
                  ["The statement: multiplying a number by 2 can give an odd number.",
                   "Try examples: 2 × 3 = 6, 2 × 5 = 10, 2 × 7 = 14 and 2 × 9 = 18. All are even.",
                   "Multiplying by 2 makes pairs, so there is never a number left over.",
                   "No number gives an odd number, so the statement is never true."],
                  "No example gives an odd number, so it is never true", kind="exercise"),
              FIO("st.q3c", "Mathematical Statements (always, sometimes, never): Q3 (c)",
                  "(c): “Halving a number always leads to an even number.” Give 3 examples for the statement. Can you find 3 "
                  "examples when this is not true?",
                  ["The statement: halving a number always leads to an even number.",
                   "Three examples that work: half of 8 is 4, half of 12 is 6 and half of 20 is 10. All are even.",
                   "Three examples that do not work: half of 6 is 3, half of 10 is 5 and half of 14 is 7. These are odd.",
                   "Some work and some fail, so the statement is not always true. It is sometimes true."],
                  "Sample answer: works for 8, 12, 20; fails for 6, 10, 14; so sometimes true. Your answer may differ",
                  kind="exercise"),
              FIO("st.q4", "Mathematical Statements (always, sometimes, never): Q4 tick the cell",
                  "Tick in the appropriate cell for the following statements. (a): Adding 10 to a number gives a multiple of "
                  "ten. (b): Changing the order of the numbers in subtraction makes no difference. (c): In multiplication, "
                  "doubling one number and halving the other keeps the product the same. (d): Multiplication by an odd number "
                  "gives an even number. (e): Multiplying a number by 5 leads to numbers which have ‘0’ in the Ones place.",
                  ["(a): adding 10 to 20 gives 30, a multiple of ten, but adding 10 to 12 gives 22, which is not. Some work "
                   "and some fail, so sometimes true.",
                   "(b): 8 − 3 = 5, but the other order, 3 − 8, has no whole-number answer, so the order matters. Only two "
                   "equal numbers, such as 6 − 6, stay the same. So sometimes true, only for two equal numbers. This is the "
                   "plan's reading with whole numbers.",
                   "(c): 6 × 8 = 48 and 12 × 4 = 48, and 5 × 8 = 40 and 10 × 4 = 40. The product stays the same, so always "
                   "true.",
                   "(d): 3 × 4 = 12 is even, but 3 × 5 = 15 is odd. Some work and some fail, so sometimes true.",
                   "(e): 5 × 4 = 20 ends in 0, but 5 × 3 = 15 ends in 5. Some work and some fail, so sometimes true."],
                  "(a): Sometimes; (b): Sometimes; (c): Always; (d): Sometimes; (e): Sometimes", kind="exercise",
                  q_figure="A table with the columns Statement, Always True, Sometimes True and Never True and five statements "
                           "in the rows, with all the cells empty.",
                  s_figure="The same table with one tick in each row.")],
          misconceptions=["M_ONE_EXAMPLE", "M_HALF_EVEN", "M_SUB_ORDER"])],
    key_terms=["always true", "sometimes true", "never true", "examples"]))

# ============================== T11 Chapter Revision (summary) =============================================
assert 6 * 7 == 42 and 1236 // 6 == 206 and 100 == 8 * 12 + 4 and 487 == 9 * 54 + 1 and 618 // 6 == 103

TOPICS.append(TOPIC(
    "T11", "M4", "Chapter Revision: Coconut Farm", ["Chapter summary"], "Understand",
    "",
    "The chapter's ideas in one walk through the coconut farm: division facts and N = D × Q, patterns of zeros, mental "
    "strategies, taking away groups, the remainder rule, bigger numbers, place value, word problems and bills, how the "
    "quotient changes, and statements.",
    [A("T11.C1", "Chapter Revision: Coconut Farm", "Understand",
       "",
       teach=["Predict first: you have walked through the whole coconut farm. Can you say one idea from each stop, from the "
              "array of coconuts to the always, sometimes and never statements? Read the lines below and tick each idea you "
              "remembered.",
              "Division facts: one multiplication fact gives two division facts. 3 rows of 9 is 3 × 9 = 27, so 27 ÷ 9 = 3 and "
              "27 ÷ 3 = 9. In a division, N = D × Q: 45 ÷ 5 = 9 and 5 × 9 = 45.",
              "Check: 6 × 7 = 42, so what are the two division facts? They are 42 ÷ 7 = 6 and 42 ÷ 6 = 7.",
              "Patterns: one more zero in the dividend gives one more zero in the quotient. 270 ÷ 9 = 30 and 2700 ÷ 9 = 300, "
              "using the table fact 27 ÷ 9 = 3.",
              "Mental strategies: split into convenient parts, 2856 ÷ 7 = 400 + 8 = 408. Round up and take the extra away, "
              "2994 ÷ 3 = 1000 − 2 = 998. Halve again and again for 4 and 8, 264 ÷ 4 = 66.",
              "Check: find 1236 ÷ 6 by splitting. 1236 = 1200 + 36, and 200 + 6 = 206.",
              "Taking away groups: take away groups of the divisor and add the groups. 378 ÷ 6: 20 + 20 + 20 + 3 = 63. "
              "Estimate first and take away the biggest group that fits to use fewer steps.",
              "The remainder rule: N = D × Q + R, and the remainder is less than the divisor. 487 = 9 × 54 + 1.",
              "Check: 100 ÷ 8 has quotient 12 and remainder 4, because 100 = 8 × 12 + 4.",
              "Bigger numbers: take away hundreds of groups, then tens, then ones. 6534 ÷ 18: 300 + 60 + 3 = 363.",
              "Place value: share the tens, regroup what is left into ones, and write 0 in a place that cannot be shared. "
              "412 ÷ 4 = 103.",
              "Check: 618 ÷ 6. 6 hundreds shared gives 1 hundred each, 1 ten cannot be shared so write 0, and 18 ones gives 3 "
              "each: 103.",
              "Word problems: the remainder can mean one more bag or a few left over. 94 coconuts in bags of 8 need 12 bags, "
              "but shared among 8 customers each gets 11.",
              "Bills: total = cost of 1 kg × quantity. Multiply for a missing total, and divide for a missing quantity or "
              "cost: 990 ÷ 18 = 55 kg.",
              "Steps: what is asked, what is given, what is missing. 4 × 36 = 144 coconuts, then 144 ÷ 8 = 18 in each sack.",
              "The quotient: double the dividend and the quotient doubles, double the divisor and it halves, double both and "
              "it stays. 480 ÷ 12 = 40, 960 ÷ 12 = 80, 480 ÷ 24 = 20, 960 ÷ 24 = 40.",
              "Check: if 240 ÷ 12 = 20, what is 240 ÷ 24? It is 10, because the divisor doubled.",
              "Statements: a statement with an equal sign is true when both sides have the same value. 6 × 5 = 20 + 10 is "
              "true, because both sides are 30.",
              "Always, sometimes or never: one example that fails shows a statement is not always true. Multiplying by 3 gives "
              "an even number for 3 × 4 = 12 and an odd number for 3 × 5 = 15, so it is sometimes true."],
       ncert=["summary"], key_terms=["division facts", "remainder", "place value", "quotient"], minutes=6,
       enrichment=True)],
    topic_type="summary"))
