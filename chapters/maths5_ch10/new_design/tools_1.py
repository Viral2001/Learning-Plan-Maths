# -*- coding: utf-8 -*-
"""Tool specs for T1 and T2 of Class 5 Chapter 10 (Symmetrical Designs): Fold and Cut (the free try of the intro, right
after the hook) and Turn and Check. Specs only; the tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Shapes the plan adds are labelled practice values. One
activity at a time, one instruction at a time, large controls, Back and Next in the same place, visible progress, Hint,
Retry and Reset always present, immediate specific feedback that is never red."""
from topics_common import T

TOOLS = {
    "fold_and_cut": T(
        "tool_fold_and_cut", "Fold and Cut", "manipulative",
        "Find out by folding and cutting that a letter with a line of symmetry can be made by drawing only half of it "
        "(one fold) or a quarter of it (two folds), and that a fold on a line that is not a line of symmetry gives a "
        "cutout that is not the letter. This is the free first try of the chapter, so it asks and shows; the video that "
        "follows names the idea.",
        "Lali's craft table, drawn as a warm 3D isometric scene with soft shadows and gentle animation, with the Happy "
        "Birthday wall banner behind it. A large square sheet of coloured paper lies in the middle of the table and is "
        "the largest thing on screen, with a dashed vertical fold line and a dashed horizontal fold line marked on it. "
        "On the left a shelf holds letter cards, each card a plain capital letter. A pair of scissors and a pencil lie "
        "beside the paper. An instruction strip at the top shows one sentence in large type, with progress dots under "
        "it. Controls: tap a letter card to put its outline on the paper; three fold buttons, Vertical, Horizontal and "
        "Both ways (one-fourth); a Draw button that shows the part of the letter to draw along the fold; a Cut button "
        "that cuts along the outline; an Open button that unfolds the paper and shows the cutout; a results sheet on the "
        "right with a row for each letter and three columns, horizontal line, vertical line and both, that the student "
        "ticks; Check, Hint, Retry (unfolds the paper for this card), Reset (clears the results sheet), Back and Next in "
        "the same places on every card. Read-outs: the fold chosen, the part drawn (1/2 or 1/4), a message under the "
        "opened paper saying whether the cutout is the full letter, and a card number out of 7.",
        ["Look at the folded paper from the story, with half of the letter A drawn along "
         "the fold. Tap the line on the paper where it is folded, then press Next.",
         "Choose a letter, choose a fold, press Draw, Cut and Open, and see whether the cutout is "
         "the full letter. Cut A with one fold, H with two folds, M and B with the right fold, and try F with every fold.",
         "Answer the questions from the story: which of the letters E, N, X, T, K, V and O can be made "
         "by just drawing half or a quarter, and which have a horizontal line, a vertical line or both. Cut each letter "
         "and tick the results sheet."],
        ["Card 1: cut the letter A. Choose the fold, then Draw, Cut and Open. Which fold do you use and how much of "
         "the A do you draw? Answer: the vertical fold, and half (1/2) of the A. The opened cutout is the full A.",
         "Card 2: cut the letter H. Which fold do you use and how much of the H do you draw? Answer: fold both ways "
         "into one-fourth, once vertically and once horizontally, and draw a quarter (1/4) of the H. The opened cutout is "
         "the full H.",
         "Card 3 (practice values): cut the letter M. Try the Horizontal fold first, then the Vertical fold. "
         "Answer: the Horizontal fold gives a cutout that is not an M, because the top and bottom of the M do not match. "
         "The Vertical fold gives the full M, with half (1/2) drawn.",
         "Card 4 (practice values): cut the letter B. Which fold works? Answer: the Horizontal fold, with half "
         "(1/2) of the B drawn, because the top half and the bottom half of the B match.",
         "Card 5 (practice values): try to cut the letter F with every fold. Answer: no fold gives an F, because "
         "the F has no line of symmetry. Its halves never match.",
         "Challenge: 'Which of the following alphabet cutouts can be made by just drawing half (1/2) or quarter "
         "(1/4) of the letter? You can do it by drawing lines of symmetry on the letters. E N X T K V O' Cut each letter "
         "with the folds. Answer: E, X, T, K, V and O can be cut out, with 1/2 drawn for E, T, K and V and 1/4 drawn for X "
         "and O. N cannot, because it has no line of symmetry.",
         "Challenge: 'Which of the letters have a horizontal line of symmetry? Which of the letters have a "
         "vertical line of symmetry? Which letters have both vertical and horizontal lines of symmetry?' Use your results "
         "sheet. Answer: horizontal line: E, X, K, O. Vertical line: X, T, V, O. Both: X, O."],
        ["After Open, a full letter shows a soft green message such as: The halves matched, so the cutout is the full A. A "
         "cutout that is not the letter shows a soft amber message such as: The two halves do not match, so this fold is not "
         "a line of symmetry. Try the other fold.",
         "After Draw, the tool says how much of the letter is drawn, for example: You drew 1/2 of the letter. For the two-fold "
         "choice it says: You drew 1/4 of the letter.",
         "A tick on the results sheet that does not agree with the cutouts slides back with a clue such as: Cut the letter "
         "with the Horizontal fold. Do the halves match?",
         "On the card with the F, after every fold has been tried, the tool says: None of the folds gave an F, so the F has "
         "no line of symmetry."],
        "Every practice card is cut with a correct fold, the results sheet is ticked for the letters E, N, X, T, K, V and O, and "
        "the student has answered both of the story's questions from the sheet.",
        ["letterCard", "foldChoice", "partDrawn", "openedCutout", "resultsSheet", "challengeIndex"],
        ["M_ANY_LINE", "M_ONE_LINE"],
        ["Look at the letter. If you folded it, would the two halves land exactly on each other?",
         "Try the Vertical fold, then the Horizontal fold. After each one, look at the opened cutout and ask: is it the full "
         "letter?",
         "For this letter, check one side against the other: which fold makes the two halves match?",
         "Use the fold the tool shows, and draw only the part it outlines along the fold. The opened paper shows the full "
         "letter."]),

    "turn_and_check": T(
        "tool_turn_and_check", "Turn and Check", "manipulative",
        "Turn a shape by 1/4, 1/2, 3/4 and a full turn and see whether it looks the same as its starting position, so "
        "that rotational symmetry is a movement the student does: a shape has it when it looks the same after a turn "
        "smaller than a full turn.",
        "Lali's craft table, drawn as a warm 3D isometric scene with soft shadows and gentle animation. A round turntable "
        "with a pin at its centre stands in the middle and is the largest thing on screen; a windmill firki on a stick or a "
        "letter card sits on the turntable, with a red dot marking one place on it. A dashed outline shows the starting "
        "position of the shape. A turn dial with four stops, 1/4, 1/2, 3/4 and Full, sits in front of the turntable. On the "
        "right a table row has four small boxes, one for each stop, each with two cards, Looks the same and Looks different, "
        "and a last box for Rotational symmetry with the choices Yes at 1/4 turn, Yes at 1/2 turn, Yes at 3/4 turn and No. An "
        "instruction strip at the top shows one sentence in large type, with progress dots under it. Controls: tap a stop on "
        "the dial and the shape turns smoothly to the right to that stop, always the same way; tap Looks the same or Looks "
        "different for each stop; choose the rotational symmetry answer; Check, Hint, Retry (turns the shape back to the "
        "start), Reset (clears the table row), Back and Next in the same places on every card. Read-outs: the turn made, the "
        "place of the dot, and a card number out of 6.",
        ["Look at the firki from the video with a dot on one blade. Turn it a quarter of the "
         "way round with the dial and tap the blade where the dot now is, then press Next.",
         "Turn each shape through the four stops of the dial, compare it with the dashed starting "
         "outline, and tap Looks the same or Looks different. Use a pinwheel, the letters Z and T and the plus sign.",
         "Answer the questions from your maths book: does the firki look the same after 1/4, 1/2, 3/4 and "
         "a full turn, and fill in the table for the letters H, I, X and Y."],
        ["Card 1 (practice values): a pinwheel with 4 blades and a dot on the top blade. Turn it to each stop. Where "
         "is the dot after each turn, and does the pinwheel look the same? Answer: after a 1/4 turn the dot is on the right "
         "blade, after a 1/2 turn on the bottom blade, after a 3/4 turn on the left blade, and after a full turn on the top "
         "blade. The pinwheel looks the same after every turn.",
         "Card 2 (practice values): the letter Z. Turn it to each stop and fill the row. Answer: after a 1/4 turn it "
         "looks different, after a 1/2 turn it looks the same, after a 3/4 turn it looks different and after a full turn it "
         "looks the same. The Z has rotational symmetry, at 1/2 turn.",
         "Card 3 (practice values): the letter T. Turn it to each stop and fill the row. Answer: it looks different "
         "after 1/4, 1/2 and 3/4 turn and the same only after a full turn. The T has no rotational symmetry.",
         "Card 4 (practice values): the plus sign. Turn it to each stop and fill the row. Answer: it looks the same "
         "after every turn. The plus sign has rotational symmetry, at 1/4 turn.",
         "Challenge: 'Observe the dot in the firki. Does the firki look the same after 1/4, 1/2, 3/4, and a full "
         "turn?' Turn the firki to each stop. Answer: yes. It looks the same after 1/4, 1/2, 3/4 and a full turn. The dot "
         "moves, but the firki looks the same.",
         "Challenge: the table of letters. The row of H is done for you: after 1/4 turn no, after 1/2 turn yes, after "
         "3/4 turn no, after a full turn yes, rotational symmetry yes, at 1/2 turn. Fill the rows of I, X and Y. Answer: I: "
         "yes at 1/2 turn. X: yes at 1/4 turn, because it looks the same after every turn. Y: only after a full turn, so no."],
        ["When the shape stops at a turn, the dashed outline stays where it began. A shape that fits the outline shows a soft "
         "green message such as: It fits the outline, so it looks the same after this turn. A shape that does not fit shows "
         "a soft amber message such as: It does not fit the outline, so it looks different after this turn.",
         "For the firki the tool says: The dot moved, but the four blades fit the outline, so the firki looks the same.",
         "A wrong Yes or No in the table slides back with a clue such as: Turn the shape to this stop and look at the dashed "
         "outline. Does it fit?",
         "A Yes for the full turn alone shows the note: Every shape looks the same after a full turn, so only the smaller "
         "turns decide."],
        "Every practice row is filled correctly, the firki question is answered, and the rows of I, X and Y are filled with the "
        "right rotational symmetry answer.",
        ["shapeOnTurntable", "dialStop", "dotPosition", "tableRow", "symmetryAnswer", "challengeIndex"],
        ["M_FULL_TURN", "M_DOT_MOVES"],
        ["Put the shape on its starting outline. Which turn will you try first?",
         "Turn the shape a quarter of the way round, then a half and then three quarters. After each turn, ask: does it fit "
         "its starting outline?",
         "For this shape, look at the shape and not at the dot. Which stop makes it fit the outline?",
         "Turn the shape to the stop the tool shows. It fits the dashed outline there, so it looks the same after that turn."]),
}
