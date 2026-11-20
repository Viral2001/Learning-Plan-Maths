# -*- coding: utf-8 -*-
"""Tool specs for T4 and T5 of Class 5 Chapter 15 (Data Through Pictures): Tool 3 Squares to Bars and Tool 4 Bar
Graph Builder. Specs only; the tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. One activity at a time, one instruction at a time, large controls,
Back and Next in the same places, visible progress, Hint, Undo, Retry and Reset always present, immediate specific
feedback that is never red (a soft amber note means look again)."""
from topics_common import T

TOOLS = {
    "squares_to_bars": T(
        "tool_squares_to_bars", "Squares to Bars", "manipulative",
        "See that a row of squares stands up into a bar of the same height, read the height of a bar on the vertical "
        "line with a sliding reading line, and compare two children's bars. The squares and the bars are the same "
        "data in two forms, and this tool is where the student sees one turn into the other.",
        "The graph wall of Samaira and Kabir's class newsroom, drawn as a warm, polished educational-game scene with "
        "soft shadows and gentle animation, in soft cream and blue-grey wall tones. The table and the graph are the "
        "largest things on screen and nothing else competes with them. On the left, pinned to the wall, is a table "
        "with one row for each activity: each row is a line of blue squares, one square stands for 1 hour, and the "
        "name of the activity sits at the left end of the row. On the right is an empty graph on a grid: the "
        "vertical line is marked 0 to 10 in equal steps and called Number of Hours, and the horizontal base has one "
        "place for each activity and is called Activities. A thin dotted guide joins each row to its place on the "
        "base. A reading line, a thin horizontal bar with a small round handle, rests at 0 and slides up and down "
        "the vertical line, and a small tag on it shows the number it points to. A Compare switch under the graph "
        "puts a second graph beside the first, with the same marks, so that two children's bars stand side by side. "
        "An instruction strip at the top shows one sentence in large type, with progress dots under it. Controls: "
        "tap a row of squares and it stands up into a solid bar of the same height on its place on the base, with a "
        "soft slide and settle; a small Lay down arrow on a standing bar lays it down again into its row; a small plus and a small "
        "minus at the end of a row add or take away one square (on the practice cards only); drag the reading line "
        "up or down and let go on the top of a bar; tap two bars to compare them; on the first card only, tap a mark "
        "on the vertical line to place a guess marker before a row is stood up; the Compare switch; Check; Hint; "
        "Undo, which lays down the row that was stood up last; Retry, which lays the squares of this step down "
        "again; Reset, which lays all the rows down; Back and Next in the same places on every card. Read-outs: the "
        "number of squares counted under each row (for example 4 squares), the number on the tag of the reading "
        "line, the heights of the two bars chosen with a word beside them (more, the same, or how many more, for "
        "example 4 − 3 = 1), and a card number out of 7. In the cards of your maths book the table holds Raman's five rows, as "
        "in your maths book, and the compare graph holds Sheela's five bars. Every bar has the same width and each "
        "graph has one friendly colour, in the warm colour of Sheela's bars for the first graph and soft sky blue "
        "for the second. The bar or number being asked about glows bright tangerine, a right answer turns green, "
        "and a look again note is soft amber, never red.",
        ["Three rows of squares lie on the table, like the rows in the video, and "
         "the graph is empty. Before touching anything, tap the number on the vertical line where you think the top "
         "of the longest row's bar will reach. Then tap the row and watch it stand up into a bar. The instruction "
         "reads: Stand each row up. The bar is as tall as the row is long.",
         "Samaira's week (practice values: homework 4 hours, games 2 hours and TV 1 hour) "
         "lies on the table. Stand up each row, slide the reading line to the top of each bar and read the number "
         "on the vertical line, add squares to a row to make a bar as tall as another bar, then switch Compare on "
         "to put Kabir's week (practice values) beside Samaira's and find who spent more time and by how many "
         "hours.",
         "Raman's table of squares is stood up into bars beside Sheela's bar graph, and your "
         "maths book's five questions are asked with their own words: Whose daily routine shows more time spent on "
         "sleeping? Who spends more hours in the school? How many more hours does Sheela spend studying compared to "
         "Raman? Is there any activity on which they spend the same amount of time? If yes, name the activity. "
         "Based on their data, whose routine do you think is more balanced? Why?"],
        ["Card 1 (practice values): Samaira's week has homework 4 squares, games 2 squares and TV 1 square. "
         "Tap each row to stand it up. How tall is each bar? Answer: the homework bar is 4 high, the games bar is 2 "
         "high and the TV bar is 1 high. Each bar is as tall as its row is long.",
         "Card 2: drag the reading line to the top of each bar and read the number on the vertical line. "
         "Which bar is the tallest and which is the shortest? Answer: the reading line says 4 at the homework bar, "
         "2 at the games bar and 1 at the TV bar. Homework is the tallest and TV is the shortest.",
         "Card 3: make a bar as tall as another bar. Add squares to the TV row until its bar is as tall as "
         "the games bar. How many squares did you add? Answer: 1 square. The TV row has 1 square, the games bar is "
         "2 high, and 2 − 1 = 1.",
         "Card 4 (practice values): switch Compare on. Kabir's week appears beside Samaira's, with homework "
         "3 hours, games 4 hours and TV 1 hour. Tap the two homework bars. Who spent more time on homework, and by "
         "how many hours? Answer: Samaira, because 4 is more than 3, and 4 − 3 = 1 hour more.",
         "Card 5: tap the two games bars, then the two TV bars. Who spent more time on games, and by how "
         "many hours? Is there an activity with the same time? Answer: Kabir spent more time on games, by 4 − 2 = 2 "
         "hours. TV is the same: both bars are 1 high, so each child watched for 1 hour.",
         "Challenge, questions 1 to 3: Raman's table of squares (sleeping 9, school 6, studying 2, eating "
         "and playing 6, other activities 1) stands up beside Sheela's bar graph (sleeping 8, school 7, studying 4, "
         "eating and playing 3, other activities 2). 'Whose daily routine shows more time spent on sleeping?' "
         "'Who spends more hours in the school?' 'How many more hours does Sheela spend studying compared to "
         "Raman?' Answers: Raman, with 9 hours against Sheela's 8 hours; Sheela, with 7 hours against Raman's 6 "
         "hours; Sheela spends 4 − 2 = 2 hours more.",
         "Challenge, questions 4 and 5: 'Is there any activity on which they spend the same amount of time? "
         "If yes, name the activity.' 'Based on their data, whose routine do you think is more balanced? Why?' "
         "Answers: No, the hours are different on all five activities (9 and 8, 6 and 7, 2 and 4, 6 and 3, 1 and "
         "2). Sample answer: Sheela's routine is more balanced, because her studying 4 and her eating and playing "
         "3 are closer than Raman's 2 and 6. Your answer may differ if the reason uses the numbers."],
        ["When a row is tapped it stands up and the tool says what happened, for example: The row has 4 squares, so "
         "the bar goes up to 4.",
         "If the reading line is not yet on the top of a bar, the tag shows a soft amber note: The bar is taller. "
         "Slide the line up until it touches the top. Or: The line is above the bar. Slide it down until it "
         "touches the top.",
         "A wrong reading shows a soft amber note: Look again. Read the height where the top of the bar meets the "
         "vertical line. The line is at 4 here, so the bar is 4 high.",
         "When two bars are tapped the tool says how they compare, for example: Samaira's bar is 4 high and Kabir's "
         "is 3 high. 4 is more than 3, and 4 − 3 = 1, so Samaira spent 1 hour more.",
         "When two bars are the same height the tool says: Both bars are 1 high, so the time is the same.",
         "If the student picks the shorter bar as the one with more time, a soft amber note says: Look again. The "
         "taller bar is the one with more hours. Which of the two bars is taller?",
         "All bars have the same width, and the tool says so when a bar is chosen: Only the height tells the number "
         "of hours, so a wider bar would not be a bigger number.",
         "For the open question about a more balanced routine the tool accepts any answer whose reason names two "
         "numbers from the graph, and says: Good. Your reason uses the numbers. Another answer can be right too."],
        "The student has stood up all three rows of Samaira's week, read each height with the reading line, made a "
        "bar as tall as another bar, compared Samaira's and Kabir's practice graphs, and then answered the five "
        "questions on Raman's and Sheela's days using the compare view.",
        ["rowsStoodUp", "squaresPerRow", "readingLinePosition", "compareViewOn", "selectedBars", "barComparison",
         "challengeIndex"],
        ["M_BAR_WIDTH", "M_BAR_LABEL"],
        ["How many squares are in this row? The bar will be that many squares high.",
         "Stand the row up, then slide the reading line to the top of the bar. The bar is as tall as the row is "
         "long.",
         "The homework row has 4 squares. Slide the reading line until it touches the top of the homework bar, and "
         "read the number it points to on the vertical line.",
         "The reading line is moved to the top of the bar for you and the number is shown: the row has 4 squares, so "
         "the bar goes up to 4. Then a similar card follows."]),

    "bar_graph_builder": T(
        "tool_bar_graph_builder", "Bar Graph Builder", "manipulative",
        "Make a bar graph from a table of numbers, with the names on the horizontal base and a bar up to each number "
        "on the vertical line, and make bars of real lengths in cm. The student types their own numbers and measured "
        "lengths, and the tool checks the total and the heights.",
        "The graph wall of Samaira and Kabir's class newsroom, drawn as a warm, polished educational-game scene with "
        "soft shadows and gentle animation, in soft cream and blue-grey wall tones. A blank graph sheet like the one "
        "in your maths book is the largest thing on screen, in the middle: the vertical line has equal marks "
        "labelled 0, 1, 2 and so on up to 10 and is called Number of Hours (Length in cm in the Lengths view), and "
        "the horizontal base has six places for names and is called Activities. A table sits beside the graph with "
        "one row for each name and a number box on each row. A view switch at the top of the wall has two settings: "
        "Table, with the table of activities and numbers, and Lengths, with a strip rack beside the sheet holding "
        "paper strips of one width and a cm ruler along the vertical line with 1 cm marked at the foot. An "
        "instruction strip at the top shows one sentence in large type, with progress dots under it. Controls: tap "
        "a number box and type a number, or use the small minus and plus steppers to change it by 1, and the bar of "
        "that row grows or shrinks at once; on the first card only, tap a row to light up its bar and tap a bar to "
        "light up its row; tap a place on the base and type a name, or tap one of the small name "
        "tags that the table offers; drag the top of a bar up or down to a mark, and it snaps to the nearest whole "
        "mark; in the Lengths view drag a paper strip from the rack to its place on the base and drag its top to "
        "the length the student measured, which is typed or stepped in cm; Check; Hint; Undo, which takes back the "
        "last change; Retry, which clears the bars of this step; Reset, which clears the table and the sheet; Back "
        "and Next in the same places on every card. The cutting and tearing of real paper strips is hands-on and "
        "stays outside the tool: the student measures their real strip with a ruler and types the length. "
        "Read-outs: a Total read-out under the table that adds all the numbers and, in the 24-hour challenge, "
        "compares the sum with 24, a small height tag that shows the number at the top of the bar being moved, a "
        "Longest and a Shortest read-out in the Lengths view, and a card number out of 7. Every bar and strip has "
        "the same width. The bars are one friendly colour, in the warm colour of Sheela's bars, the bar or number "
        "being asked about glows bright tangerine, a right answer turns green, and a look again note is soft "
        "amber, never red.",
        ["A ready table of three numbers stands beside its finished bar graph, like "
         "the table and the graph in the video. Tap a row and its bar lights up. Tap a bar and its row lights up. "
         "The instruction reads: Write the names on the base. Make each bar as tall as its number.",
         "Build a bar graph from a practice table of three numbers (practice values: school "
         "5 hours, studying 3 hours and sleeping 7 hours), find the mistake in a graph with one bar that is too "
         "tall, then use the Lengths view with three practice strips of 7 cm, 5 cm and 3 cm and find the longest "
         "and the shortest.",
         "Your maths book's own tasks with their own words. Record your daily routine (24 hours) "
         "in a table and make a bar graph of it; the tool checks that your hours add up to 24. Then measure the "
         "index fingers of you and four friends, paste the five strips as bars, and answer the four questions about "
         "the longest and the smallest index finger."],
        ["Card 1 (practice values): type the names school, studying and sleeping on the base and the "
         "numbers 5, 3 and 7 in the table. Watch the bars grow. How tall is each bar, and what does the Total "
         "read-out say? Answer: the bars go up to 5, 3 and 7, and the total is 5 + 3 + 7 = 15 hours.",
         "Card 2: look at the graph you built. Which bar is the tallest and which is the shortest? How many "
         "hours more is the tallest than the shortest? Answer: sleeping is the tallest, at 7, and studying is the "
         "shortest, at 3. 7 − 3 = 4 hours more.",
         "Card 3 (practice values): find the mistake. A graph of the same table has the sleeping bar drawn "
         "up to 8, but the table says 7. Drag the top of the bar to the right mark. Answer: the sleeping bar is too "
         "tall. Drag its top down from 8 to 7, because the table says sleeping 7 hours.",
         "Card 4 (practice values): switch to the Lengths view. Drag the three strips to their measured "
         "lengths, 7 cm, 5 cm and 3 cm. How tall is each bar? Answer: the bars reach 7, 5 and 3 on the vertical "
         "line, which has 1 cm marked at the foot, so the strips are 7 cm, 5 cm and 3 cm tall.",
         "Card 5: which strip is the longest and which is the shortest? How much longer is the longest "
         "than the shortest? Answer: the longest is 7 cm and the shortest is 3 cm. 7 − 3 = 4 cm longer.",
         "Challenge, Day in My Life: 'Record your daily routine (24 hours) in hours and minutes, as "
         "necessary. Note the time spent on activities like sleeping, studying, playing, eating, and others.' "
         "'Make a bar graph of the time you spend on different activities in the space given below.' The student "
         "types their own times, and the tool checks that they add up to 24. Sample answer (practice values, whole "
         "hours): sleeping 9, time in school 5, studying 2, eating 2, playing 3, other activities 3, and 9 + 5 + 2 "
         "+ 2 + 3 + 3 = 24, with six bars of those heights. Your answer will differ.",
         "Challenge, Whose Index Finger is Longer?: the student types the five lengths they measured and "
         "pastes the strips as bars, then answers: 'Whose index finger is the longest?' 'The length of the longest "
         "index finger is ___ cm.' 'The smallest index finger is ___ cm long.' 'It belongs to ___.' Sample answer "
         "(practice values): Mine 6 cm, Friend 1 with 7 cm, Friend 2 with 5 cm, Friend 3 with 8 cm and Friend 4 "
         "with 6 cm. The longest is Friend 3, 8 cm. The smallest is 5 cm and it belongs to Friend 2. Your answer "
         "will differ."],
        ["When a number is typed the bar grows to it and the tool says so, for example: Sleeping is 7 hours, so the "
         "bar goes up to 7.",
         "The Total read-out adds the numbers. In the 24-hour challenge, if the sum is not 24 a soft amber note "
         "says, for example: Your hours add up to 22. A day has 24 hours. When the sum is 24 it says: Your hours "
         "add up to 24. A day has 24 hours. Well done.",
         "If a bar is higher or lower than its number, a soft amber note says, for example: Look again. The sleeping "
         "bar reaches 8, but the table says 7. Drag the top down to 7.",
         "If a number is bigger than the top mark of the sheet, the tool says: This number is bigger than the top "
         "mark, 10. Check the number you typed.",
         "In the Lengths view a strip dragged to the right length says: The strip is 7 cm long, so its top meets 7 "
         "on the vertical line. If its top is at the wrong mark, a soft amber note says: Look again. The ruler "
         "shows 5 cm for this strip, but its top is at 6.",
         "All bars and strips have the same width, and the tool says so: Only the height tells the number or the "
         "length, so a wider bar would not be a bigger number.",
         "In the Lengths view the Longest and Shortest read-outs name the strips, for example: Longest: Friend 3, "
         "8 cm. Shortest: Friend 2, 5 cm."],
        "The student has built the bar graph of the three practice numbers, found and fixed the bar that was too "
        "tall, shown the three practice strips as bars and named the longest and the shortest, and then made a "
        "bar graph of their own 24 hours and of their five measured finger lengths and answered the four finger "
        "questions.",
        ["tableNumbers", "baseNames", "barHeights", "view", "stripLengths", "totalReadout", "longestAndShortest",
         "challengeIndex"],
        ["M_BAR_WIDTH", "M_BAR_LABEL"],
        ["Which number goes with this name? Find the name in the table, then find its place on the horizontal "
         "base.",
         "Find that number on the vertical line and draw the bar from the base up to it. Then look at the Total "
         "read-out.",
         "The table says sleeping 7. Find 7 on the vertical line and stop the top of the sleeping bar there.",
         "The bar is drawn up to 7 for you, with the words: Sleeping is 7 hours, so the bar goes up to 7. Then a "
         "similar card follows."]),
}
