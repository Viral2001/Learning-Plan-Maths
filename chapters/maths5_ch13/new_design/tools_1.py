# -*- coding: utf-8 -*-
"""Tool specs for T1 and T2 of Class 5 Chapter 13 (Animal Jumps): Hidden Number Box (the free try of the intro, right
after the hook) and Array Maker. Specs only; the tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds are labelled practice values. One
activity at a time, one instruction at a time, large controls, Back and Next in the same place, visible progress,
Hint, Retry and Reset always present, immediate specific feedback that is never red."""
from topics_common import T

TOOLS = {
    "hidden_number_box": T(
        "tool_hidden_number_box", "Hidden Number Box", "manipulative",
        "Find out by running a box backwards that every number that comes out is a multiple of the multiplier: a "
        "multiplier fits when every number that came out divides by it exactly, and more than one multiplier can fit. "
        "This is the free first try of the chapter, so it asks and shows; the video that follows names the multipliers "
        "factors and the numbers that come out multiples.",
        "A flat stone clearing at the start of the cobbled road in Mowgli's jungle, drawn as a warm 3D isometric scene "
        "with soft shadows and gentle animation. A cardboard box with one arrow going in and one arrow coming out "
        "stands in the middle and is the largest thing on screen. Four large number tags rest above its out arrow, as "
        "in your maths book. Under the box is an inside tray with four empty slots, one under each tag. Beside the box "
        "is a multiplier dial with a plus and a minus that sets a number from 1 to 12, shown in big type on the side of "
        "the box. A shelf at the right holds the multipliers that fit. Robby the rabbit and Deeku the deer sit at the "
        "side and watch. An instruction strip at the top shows one sentence in large type, with progress dots under "
        "it. Controls: the plus and minus on the multiplier dial; Run backwards (the box divides each number that came "
        "out by the multiplier: a whole number drops into the inside slot with a soft chime, and a number that does not "
        "divide exactly shows a soft amber note such as 28 ÷ 3 is not a whole number); Keep it (puts a multiplier that "
        "fits on the shelf); Put in (type a number and see the box send it out multiplied); answer cards for the "
        "challenge cards; Check, Hint, Retry (clears the dial and the tray for this card), Reset (returns the card's "
        "first numbers), Back and Next in the same places on every card. Read-outs: the multiplier on the box, the four "
        "inside slots, the shelf of multipliers that fit, and a card number out of 7.",
        ["Look at the box from the story, with 28, 36, 48 and 72 flying out. The box "
         "multiplied each number that went in by a secret number. Tap Next, then try a multiplier on the dial.",
         "Set the multiplier dial and run the box backwards to see what must have gone in; "
         "keep every multiplier that gives a whole number for all the numbers that came out; put in your own numbers "
         "and watch what comes out (practice values).",
         "Answer the questions from the story, Can you guess the multiplier if you see the 4 "
         "numbers coming out of the box? Is there more than one possible multiplier? What numbers might have been put "
         "inside the box? Then share your thoughts in the class, or play the game with a friend."],
        ["Card 1 (practice values): the box gives out 10, 15, 20 and 35. Try the multipliers 1, 2 and 5 and run "
         "the box backwards. Which of them give a whole number for all four? Answer: 1 and 5. With 5 the numbers 2, 3, "
         "4 and 7 went in. 2 does not fit, because 15 ÷ 2 is not a whole number: 7 × 2 = 14 and 8 × 2 = 16.",
         "Card 2 (practice values): the multiplier is 5. Put in 2, 3, 4 and 7. What comes out? Answer: 10, 15, "
         "20 and 35, because 2 × 5 = 10, 3 × 5 = 15, 4 × 5 = 20 and 7 × 5 = 35.",
         "Card 3 (practice values): the box gives out 18, 30 and 42. Find every multiplier that fits. Answer: "
         "1, 2, 3 and 6. The biggest is 6, and with 6 the numbers 3, 5 and 7 went in, because 3 × 6 = 18, 5 × 6 = 30 "
         "and 7 × 6 = 42.",
         "Card 4 (practice values): the box gives out 21, 28 and 35. Try the multiplier 3 and then the "
         "multiplier 7. Answer: 3 does not fit, because 28 is not a multiple of 3: 9 × 3 = 27 and 10 × 3 = 30. 7 fits, "
         "with 3, 4 and 5 going in. The multipliers that fit are 1 and 7.",
         "Card 5 (practice values): a friend picks the multiplier 6 and puts in 3, 4 and 8. What comes out, and "
         "what do you notice about the numbers that come out? Answer: 18, 24 and 48, because 3 × 6 = 18, 4 × 6 = 24 "
         "and 8 × 6 = 48. Each number that comes out is a multiple of 6, and 6 is a factor of each of them.",
         "Challenge: 'Can you guess the multiplier if you see the 4 numbers coming out of the box?' The four "
         "numbers are 28, 36, 48 and 72. Run the box backwards with different multipliers. Answer: 4 fits, and 7, 9, 12 "
         "and 18 went in. A guess of 4, 2 or 1 is right, because all three fit.",
         "Challenge: 'Is there more than one possible multiplier?' and 'What numbers might have been put "
         "inside the box?' Keep every multiplier that fits for 28, 36, 48 and 72. Answer: yes, 1, 2 and 4. With 4 the "
         "numbers 7, 9, 12 and 18 went in; with 2, the numbers 14, 18, 24 and 36; with 1, the numbers 28, 36, 48 and "
         "72. Your thoughts may differ in the class. Next stop: the names for these numbers, factors and multiples."],
        ["Run backwards divides each number that came out by the multiplier. A whole number drops into its inside slot "
         "with a soft chime. A number that does not divide exactly shows a soft amber note, for example: 28 ÷ 3 is "
         "not a whole number, so 3 cannot be the multiplier.",
         "When every slot is a whole number, the tool says: This multiplier fits all the numbers. Keep it? and Keep it "
         "puts the multiplier on the shelf.",
         "Put in shows the multiplied number on the out arrow, for example: 4 × 6 = 24.",
         "A wrong answer card slides back with a clue such as: Try dividing each number that came out by your "
         "multiplier. Does it come out exactly? A right card locks in with a soft chime.",
         "The tool never shows the full list of multipliers before the student has tried the dial; it only says how "
         "many fits are still hidden, for example: There are 2 more multipliers that fit."],
        "The student has kept the multipliers that fit on every practice card, named a multiplier for 28, 36, 48 and 72, "
        "found that more than one multiplier fits, and given numbers that could have gone in.",
        ["multiplier", "numbersOut", "insideSlots", "fittingMultipliers", "challengeIndex"],
        ["M_ONE_MULTIPLIER", "M_FACTOR_MULTIPLE"],
        ["What does the box do to a number that goes in? Look at the numbers that came out: could they be a number "
         "times the secret multiplier?",
         "Try a multiplier on the dial and run the box backwards. If every number that came out divides exactly, the "
         "multiplier fits.",
         "Try 2 first, then 4. Divide each number that came out by it and see whether every answer is a whole number.",
         "Set the dial to 4 and run the box backwards: 28 ÷ 4 = 7, 36 ÷ 4 = 9, 48 ÷ 4 = 12 and 72 ÷ 4 = 18. All four "
         "are whole numbers, so 4 fits. Now try a smaller multiplier."]),

    "array_maker": T(
        "tool_array_maker", "Array Maker", "manipulative",
        "Make every array of a number with square tiles, write each array as a multiplication and collect the "
        "factors: the numbers in the multiplications are the factors of the number, and a number with only one array "
        "has only the two factors 1 and itself.",
        "A smooth stone terrace in the jungle, drawn as a warm 3D isometric scene with soft shadows and gentle "
        "animation. A tile bag at the left holds square tiles, and a large tile board in the middle is the largest "
        "thing on screen, with a grid where tiles snap into rows. A number card at the top shows how many tiles there "
        "are. A rows control (a plus and a minus) sets the number of rows: when the number of rows divides the tiles "
        "exactly, every row has the same number of tiles and the array glows green; when it does not, the last row is "
        "short and the missing places show in soft amber with the words does not fill the rows. Beside the board is a "
        "factor shelf: each array that fills exactly is written as a multiplication card (for example 3 × 6 = 18) and "
        "its two numbers drop onto the shelf as factor chips in order of size. Controls: the plus and minus on rows; "
        "Save array (stores the array and its multiplication card); Turn round (turns 6 rows of 3 into 3 rows of 6 to "
        "show it is the same array); Next number; Check, Hint, Retry (clears the board), Reset (clears the shelf), "
        "Back and Next in the same places on every card. Read-outs: rows by tiles in each row, the multiplication "
        "cards, the factor chips with a counter factors found, and a card number out of 6.",
        ["Look at the 3 rows of 5 tiles from the video, 3 × 5 = 15, with the words "
         "Factors under the 3 and the 5. Tap Next, then choose a number of rows and watch the tiles.",
         "Set the rows for a number of tiles, save every array that fills exactly, turn arrays "
         "round, collect the factor chips and find numbers that have only one array (practice values).",
         "Use the board for the book's own questions: other arrays for 15, the arrays and factors "
         "of ten numbers, and why 13 and 37 are called prime numbers."],
        ["Card 1 (practice values): 8 tiles. Set the rows to 1, 2, 3 and 4 and save every array that fills "
         "exactly. Answer: 1 × 8 and 2 × 4 fill exactly. 3 rows leave a short row, because 3 × 2 = 6 and 3 × 3 = 9. The "
         "factors are 1, 2, 4 and 8.",
         "Card 2 (practice values): 9 tiles. Save every array that fills exactly. Answer: 1 × 9 and 3 × 3. The "
         "factors are 1, 3 and 9. The factor 3 shows once, because 3 rows of 3 is a square.",
         "Card 3 (practice values): 11 tiles. Try every number of rows from 2 to 10. Answer: none of them "
         "fills exactly, so the only array is 1 × 11. The factors are 1 and 11.",
         "Card 4 (practice values): find three different numbers up to 30, other than 11, that have only one "
         "array. Answer: for example 13, 17, 19, 23 or 29. Each has only the array 1 × the number, so only the two "
         "factors 1 and itself. Numbers such as 2, 3, 5 and 7 also have only one array.",
         "Challenge: 'A number, when arranged in an array, shows the factors of that number. Are there other "
         "numbers that are factors of 15? Try to make other arrays for the number 15.' Answer: yes. The array 1 × 15 as "
         "well as 3 × 5. The factors of 15 are 1, 3, 5 and 15.",
         "Challenge: 'Make different arrays for the following numbers. Identify the factors in each case.' (a) "
         "10 (b) 14 (c) 13 (d) 20 (e) 25 (f) 32 (g) 37 (h) 46 (i) 54. Then: 'Numbers like 13 and 37 are called prime "
         "numbers. Why?' Answer: the factors are (a) 1, 2, 5, 10; (b) 1, 2, 7, 14; (c) 1, 13; (d) 1, 2, 4, 5, 10, 20; "
         "(e) 1, 5, 25; (f) 1, 2, 4, 8, 16, 32; (g) 1, 37; (h) 1, 2, 23, 46; (i) 1, 2, 3, 6, 9, 18, 27, 54. 13 and 37 "
         "have only the array 1 × the number, so only two factors: they are prime numbers."],
        ["When the rows divide the tiles exactly, the array glows green and the tool writes the multiplication, for "
         "example: 2 rows of 9 tiles, 2 × 9 = 18. 2 and 9 are factors of 18.",
         "When the rows do not divide the tiles exactly, the last row is short and a soft amber note says: 4 rows of 4 "
         "is 16 tiles and 5 rows of 4 is 20 tiles. 18 tiles do not fill 4 rows evenly.",
         "Turn round shows the same array on its side and says: 6 × 3 is the same array as 3 × 6. It gives no new "
         "factor.",
         "The factor chips fill in order of size and the counter shows how many factors are found, but the tool never "
         "shows the full list before the student has tried the rows.",
         "For a number with only one array the tool says: Only 1 × the number fills exactly, so this number has only "
         "two factors."],
        "The student has saved every array of each practice number, collected the factors, found numbers with only one "
        "array, and answered the book's questions on 15, the ten numbers and the prime numbers 13 and 37.",
        ["tiles", "rows", "savedArrays", "factorChips", "challengeIndex"],
        ["M_MISS_ONE_SELF", "M_PRIME_NO_FACTORS", "M_FACTOR_MULTIPLE"],
        ["What does an array need? Every row must have the same number of tiles. How many rows could you try?",
         "Start with 1 row and add one row at a time. Save the arrays that fill exactly and write down their two "
         "numbers.",
         "For 15 tiles, try 1 row, 2 rows, 3 rows, 4 rows and 5 rows. Which of them fill every row evenly?",
         "1 row of 15 tiles fills exactly, 1 × 15. 3 rows of 5 tiles fill exactly, 3 × 5. 2 rows and 4 rows do not. "
         "The factors are 1, 3, 5 and 15. Now try the next number the same way."]),
}
