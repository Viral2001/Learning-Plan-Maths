# -*- coding: utf-8 -*-
"""Tool specs for T1 and T2 of Class 5 Chapter 15 (Data Through Pictures): Reporter's Notebook (the free try of the
intro, right after the hook) and Pictograph Maker (Stock-Taking in a Shop, with Deepti's two-wheelers). Specs only;
the tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds are
labelled practice values. One activity at a time, one instruction at a time, large controls, Back and Next in the same
place, visible progress, Hint, Retry and Reset always present, immediate specific feedback that is never red."""
from topics_common import T

TOOLS = {
    "reporters_notebook": T(
        "tool_reporters_notebook", "Reporter's Notebook", "manipulative",
        "Turn a crowd of answers into a table: move every answer into the row where it belongs, read how many answers "
        "each row holds, check that the counts add up to the number of answers, and add rows to answer questions such "
        "as more than and less than. This is the free first try straight after the hook, so it asks and shows; the "
        "video that follows names the rule.",
        "The class newsroom desk of Samaira and Kabir, drawn as a warm, polished educational-game scene with soft "
        "shadows, cream and blue-grey wall tones and gentle animation. The notebook of your maths book lies open on "
        "the desk and is the largest thing on screen: 35 faces, and beside each face a speech bubble with its "
        "answer, 1/2 hr, 1 hr, 1 1/2 hr, 2 hr or 2 1/2 hr, in a mixed order. Next to the notebook stands the table with "
        "the headings No. of Hours Spent Watching TV and No. of Children and five rows, 1/2 hour, 1 hour, 1 1/2 hour, "
        "2 hours and More than 2 hours, each row with a count box. On the practice cards a small practice notebook of 8 "
        "bubbles and a table with the three rows 1 hour, 2 hours and 3 hours take their place. On the first card one "
        "bubble glows to show where to start. An instruction strip at "
        "the top shows one sentence in large type, with progress dots under it. Controls: drag a bubble to a row, or "
        "tap the bubble and then tap the row, and the bubble slides into the row; tap a bubble that is already in a "
        "row to send it back to the notebook; a row bar for the more than and less than cards, where tapping a row adds "
        "its count to the bar (for example 2 + 2) and an answer box takes the number; answer boxes and a True and a "
        "False button for the four questions; Check, Hint, Undo (sends the last bubble back), Retry (returns the "
        "bubbles of this card to the notebook), Reset (empties the table), Back and Next in the same places on every "
        "card. Read-outs: a counter Answers still to sort (35 at the start, counting down to 0), the count box of each "
        "row, which grows by one at every drop, a pale tick in the notebook where a bubble has been sorted so that no "
        "answer is counted twice, and a sum line under the table that adds the counts of the rows (for example 4 + 2 + "
        "2 = 8) and shows the number of answers beside it.",
        ["Look at the picture of Samaira and Kabir, the two reporters, with their "
         "question How many hours a day do you spend watching TV? and the full notebook from the story. Read the "
         "instruction Every answer goes in the row where it belongs. Tap the glowing bubble, then tap the row where it "
         "belongs, watch it slide in, and press Next.",
         "Move the 8 bubbles of a small practice notebook into the rows of a table, read the "
         "count of each row, check that the counts add up to the number of answers, and answer more than and less than "
         "questions by tapping rows and adding their counts.",
         "Sort the 35 answers of the real notebook into the table of your maths book, then answer "
         "the book's four questions about the table, unchanged."],
        ["Card 1 (practice values): a small practice notebook has 8 answers, 2 hr, 1 hr, 3 hr, 1 hr, 2 hr, "
         "1 hr, 3 hr and 1 hr. Move each bubble into its row of a table with the rows 1 hour, 2 hours and 3 hours. How "
         "many answers are in each row? Answer: the row 1 hour has 4, the row 2 hours has 2 and the row 3 hours has "
         "2, and the counter Answers still to sort goes down to 0.",
         "Card 2 (practice values): read the count box of each row and add the counts. Do they add up to the "
         "number of answers? Answer: yes, 4 + 2 + 2 = 8 and there are 8 answers, so every answer is in a row once. If "
         "the sum is not 8, an answer is missed or counted twice.",
         "Card 3 (practice values): how many answered more than 1 hour? Tap the rows that are more than 1 "
         "hour and read the sum on the row bar. Answer: the rows 2 hours and 3 hours, 2 + 2 = 4. The row 1 hour is "
         "exactly 1 hour, not more, so it is not tapped.",
         "Card 4 (practice values): how many answered less than 3 hours? Tap the rows that are less than 3 "
         "hours. Answer: the rows 1 hour and 2 hours, 4 + 2 = 6. The row 3 hours is exactly 3 hours, not less, so it is "
         "not tapped.",
         "Challenge: 'Samaira and Kabir asked 35 friends: How many hours a day do you spend watching TV? "
         "Their answers are in the notebook. Fill in the number of children in each row of the table.' Sort all 35 "
         "answers of the real notebook into the five rows of the table and read the number of children in each row. "
         "Answer: 1/2 hour 9, 1 hour 13, 1 1/2 hour 7, 2 hours 3, More than 2 hours 3, and 9 + 13 + 7 + 3 + 3 = 35. "
         "The three 2 1/2 hr answers go in the row More than 2 hours.",
         "Challenge: the book's four questions on the table, unchanged: 'Look at the table and answer the "
         "following questions.' First: 'How many children watch TV for more than half an hour?' Second: 'How many "
         "children watch TV for less than two hours?' Third: 'The number of children who watch TV for more than two "
         "hours is ___.' Fourth: 'More children watch TV for two hours than half an hour. (True/False)' Answers: "
         "first 26, because 13 + 7 + 3 + 3 = 26; second 29, because 9 + 13 + 7 = 29; third 3; fourth False, because "
         "3 children watch for two hours and 9 children for half an hour, and 3 is less than 9. These questions are "
         "open: Check gives a clue and never shows the answer."],
        ["A bubble dropped in the right row slides in, the count box of that row grows by one, the counter Answers "
         "still to sort goes down by one, and a pale tick marks the bubble's place in the notebook so that no answer is "
         "counted twice.",
         "A bubble dropped in the wrong row bounces back with a soft amber glow and a clue that reads the bubble aloud, "
         "for example: This answer says 2 hr, so it goes in the row 2 hours.",
         "A bubble that says 2 1/2 hr dropped in the row 2 hours bounces back with: 2 1/2 hr is more than 2 hr, so it "
         "goes in the row More than 2 hours.",
         "When every bubble is sorted, the sum line under the table adds the counts and says whether they add up, for "
         "example: 4 + 2 + 2 = 8. You had 8 answers, so every answer is in a row once. If a bubble is still in the "
         "notebook, the line says, for example: Your counts add up to 7. There are 8 answers, so one answer is not "
         "sorted yet.",
         "On the more than and less than cards, a tapped row that does not belong gets a soft amber note, for example: "
         "The row 1 hour is not more than 1 hour. Tap the rows after it. A right set of rows shows their counts joined "
         "by plus signs, for example 2 + 2, and the answer box takes the sum.",
         "In the four questions of your maths book a wrong answer gets a soft amber clue, never a red mark and never the "
         "answer, for example: Look again. Does the row 1/2 hour belong to more than half an hour? For the last "
         "question the clue says: Find the row 2 hours and the row 1/2 hour and compare the two counts."],
        "The 8 practice answers are sorted and read, the counts of the practice table add up to 8, the more than and "
        "less than cards are answered, the real notebook is sorted into the table with counts that add up to 35, and "
        "the four questions of your maths book are answered.",
        ["bubblePlaces", "rowCounts", "answersStillToSort", "sumLine", "practiceNotebookOn", "tappedRows",
         "questionAnswers", "challengeIndex"],
        ["M_COUNT_TWICE", "M_MORE_THAN_INCLUDES"],
        ["Look at the answer in the bubble. Which row of the table has the same words as the bubble?",
         "A row can name one answer, like 2 hours, or a group of answers, like More than 2 hours. Find the row where "
         "the bubble fits. For a question, ask which rows it asks about: the rows after a row for more than, the "
         "rows before a row for less than.",
         "Match the words. A bubble that says 2 1/2 hr is more than 2 hours, so it belongs in the row More than 2 "
         "hours. For more than half an hour, the rows after the row 1/2 hour are 1 hour, 1 1/2 hour, 2 hours and More "
         "than 2 hours. Add their counts.",
         "The tool slides the bubble into its row and says why, for example This answer says 2 hr, so it goes in the "
         "row 2 hours. For a question it lights up the rows to add and shows their counts joined by plus signs, then a "
         "similar card follows."]),

    "pictograph_maker": T(
        "tool_pictograph_maker", "Pictograph Maker", "manipulative",
        "Show numbers with icons using a scale: choose the scale, place the icons of each row, read a row back as the "
        "number of icons × the scale, and see that a bigger scale needs fewer icons and that the scale must fit every "
        "number with nothing left over.",
        "Joseph Uncle's shop shelf in the class newsroom, drawn as a warm, polished educational-game scene with soft "
        "shadows, cream and blue-grey wall tones and gentle animation. On the left a small table of items with their "
        "numbers, with the headings Name of the Item and Number of Items. On the right the pictograph strip is the "
        "largest thing on screen: three rows, each with its name and room for icons, and an icon box at the top of the "
        "strip that reads 1 icon = ___ items and changes with the scale. Above the strip is the scale box 1 icon = ___ "
        "with a stepper that picks any whole number from 1 to 12 and quick buttons 1, 2, 5 and 10. Below the strip is a "
        "tray of icons in the pictures of your maths book: a train for toys, a board game, a racket for sports items "
        "and a scooter for two-wheelers. An instruction strip at the top shows one sentence in large type, with "
        "progress dots under it. On the reading cards the strip comes ready with its icons and a number box appears "
        "beside each row. Controls: pick the scale with the stepper or a quick button; drag an icon from the "
        "tray into a row, or tap a row to add one icon; tap an icon in a row to take it away; a Show the number switch "
        "that turns the icons of a row into its number; number boxes for typing an answer; Check, Hint, Undo, Retry "
        "(clears the icons of this card), Reset (clears the strip and the scale), Back and Next in the same places on "
        "every card. Read-outs: for each row a line icons × scale = number (for example 3 × 5 = 15), the total number "
        "of icons, and a fit light beside the scale box that is green when every number gives a whole number of icons "
        "and soft amber when some items would be left over, with a note that says how many. When some items are left "
        "over, the tool places no icon for them and asks for another scale.",
        ["Look at the shop shelf from the video, where one icon stands for 5 items, and "
         "read the instruction Show each number with icons. One icon stands for the scale. Press Next.",
         "Set a scale, drag icons from the tray into the rows to show a practice stock, press "
         "Show the number to read a row of icons back as icons × scale, read a ready pictograph, and change the scale "
         "of one set of numbers to see how many icons each scale needs and which scale does not fit.",
         "Answer the book's three questions about Dipesh's pictograph, choose another scale for "
         "the same data, and choose another scale for Deepti's data about two-wheelers."],
        ["Card 1 (practice values): set 1 icon = 5 and show a practice stock of toys 15, board games 30 and "
         "sports items 25. How many icons does each row need? Answer: 3 icons for the toys, because 15 ÷ 5 = 3; 6 icons "
         "for the board games, because 30 ÷ 5 = 6; 5 icons for the sports items, because 25 ÷ 5 = 5.",
         "Card 2 (practice values): a ready pictograph has 1 icon = 5 items, with toys 9 icons, board games "
         "11 icons and sports items 6 icons. Press Show the number for each row. How many items are in each row? "
         "Answer: 9 × 5 = 45 toys, 11 × 5 = 55 board games and 6 × 5 = 30 sports items.",
         "Card 3 (practice values): the numbers are 20, 30 and 50 items. Set the scale to 10 and place the "
         "icons. How many icons does each row need? Answer: 2, 3 and 5 icons, because 20 ÷ 10 = 2, 30 ÷ 10 = 3 and "
         "50 ÷ 10 = 5.",
         "Card 4 (practice values): change the scale of the same numbers, 20, 30 and 50, to 5. How many icons "
         "does each row need now, and which scale needs fewer icons? Answer: 4, 6 and 10 icons, because 20 ÷ 5 = 4, "
         "30 ÷ 5 = 6 and 50 ÷ 5 = 10. The bigger scale 10 needs fewer icons.",
         "Card 5 (practice values): change the scale of the same numbers to 4. Does it fit? Answer: no. "
         "20 ÷ 4 = 5 fits, but 30 ÷ 4 is 7 with 2 left over and 50 ÷ 4 is 12 with 2 left over, so the fit light turns "
         "amber and the tool asks for another scale.",
         "Challenge: Dipesh's pictograph of your maths book is on the strip: 1 train icon = 5 toys, 1 board "
         "game icon = 5 board games and 1 racket icon = 5 sports items, with Toys 8 icons, Board games 10 icons and "
         "Sports items 12 icons. The questions: 'How many toys does Joseph Uncle have? ___' 'How many board games "
         "does Joseph Uncle have? ___' 'How many total play items does Joseph Uncle have? ___' Then: 'Is there any "
         "other scale that you can use to make the pictograph? Choose your scale and show the same data using a "
         "pictograph in your notebook.' Answers: 40 toys, because 8 × 5 = 40; 50 board games, because 10 × 5 = 50; "
         "150 play items, because 40 + 50 + 60 = 150. Sample for the other scale: scale 10, with toys 4 icons, board "
         "games 5 icons and sports items 6 icons; the scale 2 fits too. Your answer may differ: every scale that fits "
         "all three numbers is right.",
         "Challenge: Deepti's pictograph of your maths book is on the strip: 1 scooter icon = 3 two-wheelers, "
         "with Monday 8 icons, Wednesday 4 icons and Friday 12 icons. The question: 'Choose any other scale and "
         "represent the same data using a pictograph in your notebook.' Answer: the numbers are Monday 24, Wednesday "
         "12 and Friday 36 two-wheelers. Sample: scale 6, with Monday 4 icons, Wednesday 2 icons and Friday 6 icons, "
         "because 24 ÷ 6 = 4, 12 ÷ 6 = 2 and 36 ÷ 6 = 6; the scales 1, 2, 4 and 12 fit too. Your answer may differ: "
         "every scale that fits all three numbers is right."],
        ["A right row shows its read-out in soft green, for example 3 icons, 3 × 5 = 15. This row is right.",
         "Too many icons gets a soft amber note, for example: You put 7 icons for 30 items. One icon is 5 items, so 30 "
         "items need 6 icons. Too few icons gets, for example: You put 5 icons for 30 items. 5 × 5 = 25, so 30 items "
         "need more icons.",
         "A scale that does not fit turns the fit light amber with, for example: With one icon = 4, 30 items need 7 "
         "icons and 2 items are left over. Try another scale.",
         "A wrong number when reading a row back gets a clue about the scale, for example: You wrote 9 for the toys. 9 "
         "is the number of icons. One icon stands for 5 toys, so multiply the icons by the scale.",
         "When the scale changes, the strip redraws at once and the tool says how many icons each row needs now, for "
         "example: With 1 icon = 10, 20 items need 2 icons. With 1 icon = 5, they need 4 icons. A bigger scale needs "
         "fewer icons.",
         "The choose-your-scale items are never marked wrong when the scale fits. The tool checks that every number "
         "gives a whole number of icons, shows the read-out of each row and says: Your answer may differ from the "
         "sample, and every scale that fits is right."],
        "A practice stock is shown with the scale 5, a ready pictograph is read back, the scales 10, 5 and 4 are "
        "tried on the same numbers, Dipesh's three questions are answered, and a scale that fits is chosen for "
        "Dipesh's data and for Deepti's data.",
        ["scale", "iconsPerRow", "rowNumbers", "showNumber", "readOut", "fitLight", "stripView", "challengeIndex"],
        ["M_ICON_IS_ONE", "M_SCALE_NO_FIT", "M_BIG_SCALE_MORE"],
        ["What does one icon stand for? Look at the scale box.",
         "How many groups of the scale are in the number? That is the number of icons. To read a row back, count the "
         "icons and multiply by the scale.",
         "Add icons one at a time until the read-out shows the number. For example, with 1 icon = 5, keep adding "
         "icons until the read-out says 30. If it goes past the number, take one icon away.",
         "The tool places the icons for you and shows the read-out, for example 6 icons, 6 × 5 = 30, then a similar card "
         "follows."]),
}
