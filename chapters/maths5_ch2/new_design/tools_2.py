# -*- coding: utf-8 -*-
"""Tool specs for T4, T5 and T6 of Class 5 Chapter 2 (Fractions): Equal Parts Splitter, Chikki Share and Paratha
Pieces. Specs only; the tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints.
One activity at a time, one instruction at a time, large controls, Back and Next in the same place, visible
progress, specific feedback, hints, retry and reset. All three sit in Raman's family kitchen."""
from topics_common import T

TOOLS = {
    "equal_parts_splitter": T(
        "tool_equal_parts_splitter", "Equal Parts Splitter", "manipulative",
        "Cut every part of a shaded shape into more equal pieces and watch the name of the fraction change while the "
        "shaded area stays exactly where it was: the top number and the bottom number are multiplied by the same "
        "number, so the new fraction is equivalent.",
        "A baking tray on the wooden table of Raman's family kitchen, drawn as a warm, polished 3D isometric scene "
        "with soft shadows and gentle animation. The tray holds one flat sheet of sweet, the largest thing on screen, "
        "which the student cuts into equal pieces. A tab row picks the shape: Sameer's 1/3 sweet, cut into 3 equal "
        "vertical strips with the middle strip shaded orange; the 2/5 sweet, cut into 5 equal horizontal strips with "
        "2 strips shaded orange; and a Practice tray (practice values) with two small steppers, equal parts in the "
        "whole (2 to 8) and parts shaded (1 up to one less than the whole). A thick outline traces the shaded region "
        "and never moves when cuts are added, so the student sees that the shaded area does not change. A stepper "
        "under the tray reads Cut each part into [1] pieces, with minus and plus buttons from 1 to 12; every press "
        "draws thin cut lines across every part with a soft slide. A large name card above the tray shows the "
        "fraction of the shaded part as a stacked fraction, for example 2/6, with the top number and the bottom "
        "number in two colours. Under the tray a times ribbon reads, for example, top × 2, bottom × 2. A pattern "
        "table lists one row for every cut tried: pieces per part, top number, bottom number. For the book's chains "
        "a row of number boxes under the tray, for example 1/3 = 2/6 = 3/9 = 4/12 = ___ = ___ = ___ = ___/24 = "
        "___/36, accepts typed numbers: tapping a box opens a large number pad. For pairs, two small trays sit side "
        "by side with two big buttons, Equivalent and Not equivalent. Fixed controls: Check, Hint, Retry (removes "
        "the last cuts of this card), Reset (restores the uncut shape), Back and Next in the same places on every "
        "card, and 7 progress dots. A counter shows the card number out of 7.",
        ["Look at a practice tray of 1/4 and cut each part into 2 pieces and then "
         "into 3 pieces. Say what happens to the name and to the shaded area before you touch Check.",
         "Cut Sameer's 1/3 sweet into more equal pieces, read the name card and the times "
         "ribbon each time, fill the pattern table, and test pairs of fractions by cutting both trays to the same "
         "number of parts.",
         "Fill the book's two chains of equivalent fractions on the divided pictures, then do "
         "the three Let Us Do questions on equivalent fractions: blanks, ticks and boxes."],
        ["Card 1: on Sameer's 1/3 sweet set the stepper to 2, so every third is cut into 2 equal pieces. "
         "What fraction names the shaded part now? Answer: 2/6, because 1 × 2 = 2 shaded pieces and 3 × 2 = 6 pieces "
         "in all. The outline of the shaded area has not moved.",
         "Card 2: cut every third into 3 pieces and then into 4 pieces, and read the name card each time. "
         "Answer: 3/9 (1 × 3 and 3 × 3), then 4/12 (1 × 4 and 3 × 4). 1/3, 2/6, 3/9 and 4/12 show the same shaded "
         "region.",
         "Card 3 (practice values): on the Practice tray set 4 equal parts with 1 shaded, which is 1/4. "
         "Read the pattern table rows for 2 and 3 cuts, then predict the fraction for 5 cuts before you cut. Answer: "
         "5/20, because 1 × 5 = 5 and 4 × 5 = 20. The top number and the bottom number are multiplied by the same "
         "number.",
         "Card 4 (practice values): two small trays show 3/4 and 9/12. Cut every fourth of the first tray "
         "into 3 pieces. Are the two fractions equivalent? Then test 3/4 and 10/12 the same way. Answer: yes, "
         "3/4 = 9/12, because 3 × 3 = 9 and 4 × 3 = 12. No, 3/4 and 10/12 are not equivalent, because cutting into "
         "3 gives 9/12, and 10/12 shades one more piece.",
         "Card 5 (practice values): a friend adds 1 to the top and 1 to the bottom of 1/2 and says 2/3 is "
         "equivalent. Cut the 1/2 tray into 2, 3 and 4 equal pieces. Is 2/3 on the list? Answer: the list is 2/4, "
         "3/6 and 4/8. 2/3 is not on it, so adding the same number does not make an equivalent fraction. Multiply "
         "the top and the bottom by the same number.",
         "Challenge: 'Divide the wholes given below into more equal parts and find fractions equivalent to "
         "1/3. Write them in the boxes below the images. 1/3 = 2/6 = 3/9 = 4/12 = ___ = ___ = ___ = ___/24 = "
         "___/36' and 'The below pictures show 2/5 of a whole. Find the different fractions that are equivalent to "
         "2/5 and write your fractions below each image. 2/5 = 4/10 = ___ = ___ = ___/50 = ___/100'. Answers: "
         "1/3 = 2/6 = 3/9 = 4/12 = 5/15 = 6/18 = 7/21 = 8/24 = 12/36 (the three open blanks may be other "
         "equivalents; 3 × 8 = 24 and 1 × 8 = 8, 3 × 12 = 36 and 1 × 12 = 12). 2/5 = 4/10 = 6/15 = 8/20 = 20/50 = "
         "40/100 (the two open blanks may be other equivalents; 5 × 10 = 50 and 2 × 10 = 20, 5 × 20 = 100 and "
         "2 × 20 = 40).",
         "Challenge: 'Fill in the blanks with equivalent fractions. There may be more than one answer. "
         "(a) 1/7 = ___ (b) 2/3 = ___ (c) 3/4 = ___ (d) 3/5 = ___'; 'Put a tick against the fractions that are "
         "equivalent. (a) 2/3 and 3/4 (b) 3/5 and 6/10 (c) 4/12 and 2/6 (d) 6/9 and 1/3'; 'Fill in the boxes such "
         "that the fractions become equivalent. (a) 2/5 = ___/10 (b) 3/4 = ___/16 (c) 4/7 = 8/___ (d) 5/9 = "
         "25/___'. Answers: sample blanks 1/7 = 2/14, 2/3 = 4/6, 3/4 = 6/8, 3/5 = 6/10 (more than one answer is "
         "right); ticks on (b) and (c); boxes 4, 12, 14 and 45."],
        ["A cut makes the name card change at once and shows the reason: 2/6 names the same shaded part as 1/3, "
         "because each third was cut into 2 pieces. The outline of the shaded area stays where it was.",
         "The times ribbon always shows both numbers multiplied by the same number, so the student sees that the "
         "top and the bottom change together.",
         "A typed number that is wrong makes its box blink and shows the cuts that match the bottom number given. "
         "For ___/24 it shows 8 cuts, because 3 × 8 = 24, and asks what the shaded strip becomes. The answer is "
         "never typed for the student.",
         "A pair marked wrongly is cut to the same number of parts side by side, so the shaded parts can be counted "
         "in both trays. The comparison shows the two fractions with the same bottom number.",
         "A friend's rule of adding the same number is never marked as silly: the tool lists the fractions that cuts "
         "really give and shows that the added fraction is not among them."],
        "All 7 cards are done, the two chains and the three Let Us Do questions are filled correctly, and the last "
        "card is finished without a bottom-out hint.",
        ["tray", "cutsPerPart", "shadedParts", "totalParts", "typedNumbers", "pairAnswers", "cardIndex"],
        ["M_EQUIV_ADD", "M_UNEQUAL_PARTS", "M_BIGGER_DENOM"],
        ["How many equal pieces is each part cut into? Look at the stepper and at the name card.",
         "Look at the top number and the bottom number before and after a cut. Did they change in the same way?",
         "Every part is cut into the same number of pieces, so multiply the top number and the bottom number by that "
         "number. For ___/24 ask: 3 times what number is 24?",
         "Worked step on a practice tray: for 1/4 cut into 3 pieces, 1 × 3 = 3 and 4 × 3 = 12, so the name is 3/12. "
         "Do the same with the numbers on your card."]),

    "chikki_share": T(
        "tool_chikki_share", "Chikki Share", "manipulative",
        "Share a slab of chikki between two plates and compare two fractions that have the same denominator by "
        "counting equal pieces: when the pieces are the same size, the plate with more pieces has more.",
        "A chikki slab on a wooden tray on the table of Raman's family kitchen, drawn as a warm, polished 3D "
        "isometric scene with soft shadows and gentle animation. The golden slab is the largest thing on screen, cut "
        "into equal pieces by thin lines; it starts as the book's slab of 3 equal pieces. A row of slab chips lets "
        "the student choose a slab of 4, 5, 6, 8 or 10 equal pieces (practice values). Two plates stand on either "
        "side of the tray, named Sevi and Shami. Every piece can be dragged to a plate and back; a piece that is "
        "dropped near a plate snaps in. Under each plate sit a piece counter, for example 2 pieces, and a large "
        "fraction label that updates at once, for example 2/3. A line under the slab reads Each piece is 1/3 of the "
        "slab. A button, Who has more?, makes a soft amber glow around the plate with more and shows a more or less "
        "tag on each plate. Between the two plate labels sit two big sign buttons, < and >, for the Let Us Do "
        "comparisons. Fixed controls: Hint, Retry (returns the pieces of this card to the tray), Reset (returns the "
        "whole slab), Back and Next in the same places on every card, and 7 progress dots. A counter shows the card "
        "number out of 7.",
        ["Look at the slab cut into equal pieces and share it between the two plates. "
         "Say what each plate label tells you.",
         "Give pieces to the two plates, read the labels and the tag, and say who has more. "
         "Try other splits and other slabs (practice values), including the same number of pieces on both plates.",
         "Answer the book's question about Sevi and Shami and the chikki, then compare the six "
         "pairs of fractions of the Let Us Do question with the signs < and >, each shown on a cut slab."],
        ["Card 1: on the slab of 3 equal pieces, put 1 piece on one plate and 2 pieces on the other. Read the "
         "two plate labels and the tag. Answer: the plates read 1/3 and 2/3, and the plate with 2/3 has more, because "
         "2 pieces of 1/3 are more than 1 piece of 1/3.",
         "Card 2 (practice values): choose the slab of 8 pieces. Put 2 pieces on one plate and 5 pieces on "
         "the other. Who has more? Answer: the plate with 5/8 has more, because 5 pieces of 1/8 are more than 2 "
         "pieces of 1/8.",
         "Card 3 (practice values): choose the slab of 6 pieces. Put 3 pieces on each plate. What does the "
         "tag say? Answer: the plates have the same, 3/6 and 3/6, because they have the same number of pieces of "
         "the same size.",
         "Card 4 (practice values): choose the slab of 10 pieces. One plate has 7 pieces. What is the "
         "smallest number of pieces you can put on the other plate so that it has more? Answer: 8 pieces, because "
         "8/10 > 7/10 and 7 pieces would only make the same.",
         "Card 5 (practice values): choose the slab of 5 pieces. Put 1 piece on the left plate and 4 pieces "
         "on the right plate. Press the sign between the two labels. Answer: 1/5 < 4/5, because 1 piece of 1/5 is "
         "less than 4 pieces of 1/5.",
         "Challenge: 'Sevi and Shami divided a piece of chikki between themselves. Sevi ate 1/3 and Shami "
         "ate the rest, that is, 2/3. Who ate more?' Share the slab of 3 pieces to match, press the answer and say "
         "why. Answer: Shami ate more, because 2 pieces of 1/3 are more than 1 piece of 1/3, so 2/3 > 1/3.",
         "Challenge: 'Compare the fractions given below using < and > signs. (a) 1/4 ___ 3/4 (b) 3/5 ___ "
         "4/5 (c) 5/7 ___ 2/7 (d) 7/8 ___ 3/8 (e) 5/10 ___ 6/10 (f) 2/6 ___ 1/6'. Each pair is shown on a slab cut "
         "into the matching number of pieces. Answers: (a) < (b) < (c) > (d) > (e) < (f) >."],
        ["A piece on a plate updates the counter and the plate label at once, and the line under the slab says "
         "that every piece is the same size.",
         "A correct answer shows the reason in words, for example: 2 pieces of 1/3 are more than 1 piece of 1/3. The "
         "plate with more glows.",
         "A wrong sign or a wrong plate gets a soft amber note, never red: count the pieces on each plate, the "
         "pieces are the same size, so the plate with more pieces has more.",
         "The same number of pieces on both plates shows that they have the same, so the student sees that equal "
         "does not need any sign."],
        "All 7 cards are done, the question about Sevi and Shami and the six comparisons are correct, and the last "
        "card is finished without a bottom-out hint.",
        ["slabPieces", "piecesOnPlateOne", "piecesOnPlateTwo", "signChosen", "cardIndex"],
        ["M_TOP_ONLY", "M_UNEQUAL_PARTS"],
        ["Are the pieces on the slab all the same size?",
         "Count the pieces on each plate. Which count is bigger?",
         "Both plates have pieces of the same size, so the plate with more pieces has more. Look at the top numbers "
         "of the two plate labels.",
         "Worked step on a practice slab: 6 pieces on one plate and 4 on the other, on a slab of 8. 6 pieces of 1/8 "
         "are more than 4 pieces of 1/8, so 6/8 > 4/8. The plate with 6/8 glows. Do the same with your plates."]),

    "paratha_pieces": T(
        "tool_paratha_pieces", "Paratha Pieces", "manipulative",
        "Compare two fractions that have the same numerator by laying one piece of each paratha over the other: a "
        "paratha cut into more pieces has smaller pieces, so the same number of pieces makes the smaller fraction.",
        "Two round parathas on plates on the counter of Raman's family kitchen, drawn as a warm, polished 3D "
        "isometric scene with soft shadows and gentle animation. The two parathas are the largest things on screen: "
        "the left one is cut into 5 equal pieces and the right one into 6 equal pieces, as in the book. Two stepper "
        "rows, one under each paratha, let the student change the cut from 3 to 10 equal pieces (practice values). "
        "Every piece can be tapped to pick it, and a picked piece shows its fraction, for example 1/5. A grey "
        "overlay mat sits between the plates: a piece from each paratha is dragged onto it and the pieces stack, "
        "with the smaller piece showing a bright outline on top of the bigger one. A count stepper, Pieces to take, "
        "picks the same number of pieces from each paratha, and a button, Line them up, lays the picked pieces side "
        "by side in two rows under the parathas so the two row lengths can be seen. Under each paratha a label "
        "reads, for example, cut into 6 equal pieces, and a fraction label shows the pieces taken, for example 4/6. "
        "Two big buttons, Left is bigger and Right is bigger, answer the piece question, and two sign buttons, < "
        "and >, sit between the fraction labels for the Let Us Do comparisons. Fixed controls: Hint, Retry (clears "
        "the overlay), Reset (restores both parathas), Back and Next in the same places on every card, and 7 "
        "progress dots. A counter shows the card number out of 7.",
        ["Look at the 1/3 piece and the 1/4 piece (practice values). Lay one on the other "
         "and say which piece is bigger.",
         "Lay one piece of each paratha over the other, then take the same number of pieces "
         "from each paratha, line them up and compare the two rows. Try other cuts (practice values).",
         "Answer the book's question about 4/6 and 4/5 of a paratha, then compare the six pairs "
         "of fractions of the Let Us Do question with the signs < and >."],
        ["Card 1: lay one piece of the paratha cut into 5 over one piece of the paratha cut into 6. Which "
         "piece is bigger? Answer: the 1/5 piece is bigger. The 1/6 piece fits inside it, because the paratha cut "
         "into 6 is shared among more pieces.",
         "Card 2: take 4 pieces from each paratha and line them up. Which row is longer? Answer: the row "
         "of 4 pieces of 1/5 is longer than the row of 4 pieces of 1/6, so 4/5 is more than 4/6.",
         "Card 3 (practice values): cut the left paratha into 3 pieces and the right paratha into 4 pieces. "
         "Take 2 pieces from each and line them up. Answer: 2/3 is longer than 2/4, because the 1/3 piece is bigger "
         "than the 1/4 piece.",
         "Card 4 (practice values): cut the left paratha into 8 pieces and the right paratha into 10 "
         "pieces. Take 5 pieces from each. Which row is longer? Answer: the row from the paratha cut into 8, so "
         "5/8 > 5/10, because the 1/8 piece is bigger than the 1/10 piece.",
         "Card 5 (practice values): a friend says 4/10 is more than 4/5, because 10 is bigger than 5. "
         "Cut the parathas into 10 and 5 pieces, take 4 pieces from each and line them up. Answer: the friend is "
         "not right. 4/10 < 4/5, because a paratha cut into 10 pieces has smaller pieces than a paratha cut into 5 "
         "pieces.",
         "Challenge: 'One child says: I ate 4/6 paratha yesterday evening. The other says: I ate 4/5 "
         "paratha yesterday evening. Between Sevi and Shami, can you tell who ate more? Use your fraction kit to "
         "find the answer.' Lay the pieces and answer. Answer: the child who ate 4/5 ate more, because the 1/6 piece "
         "is smaller than the 1/5 piece, so 4/6 < 4/5.",
         "Challenge: 'Compare the following fractions using < and > signs. (a) 3/8 ___ 3/7 (b) 4/9 ___ "
         "4/10 (c) 2/7 ___ 2/5 (d) 5/7 ___ 5/6 (e) 6/9 ___ 6/10 (f) 7/9 ___ 7/11'. Each pair is shown on two "
         "parathas cut to match. Answers: (a) < (b) > (c) < (d) < (e) > (f) >."],
        ["A piece laid over another shows the smaller piece outlined on the bigger one and says: 1/6 is smaller than "
         "1/5, because the paratha is shared among more pieces.",
         "The two rows lined up show the longer row glowing, so the student sees that the same number of bigger "
         "pieces is more.",
         "A wrong answer gets a soft amber note, never red: how many pieces is each paratha cut into, and which "
         "single piece is bigger?",
         "Changing a cut to more pieces makes every piece of that paratha shrink at once, so the link between a "
         "bigger bottom number and a smaller piece is seen as it happens."],
        "All 7 cards are done, the question about 4/6 and 4/5 and the six comparisons are correct, and the last "
        "card is finished without a bottom-out hint.",
        ["cutLeft", "cutRight", "piecesTaken", "overlayPieces", "rowsLinedUp", "signChosen", "cardIndex"],
        ["M_SAME_TOP_BIGGER", "M_BIGGER_DENOM"],
        ["How many equal pieces is each paratha cut into?",
         "Which single piece is bigger? Lay one piece on top of the other and look.",
         "Both take the same number of pieces. If one piece of a paratha is smaller, what does that tell you about "
         "all the pieces you took from it?",
         "Worked step on a practice pair: cut into 6 and cut into 8, 5 pieces from each. The tool lines them up: 5 "
         "pieces of 1/6 are longer than 5 pieces of 1/8, so 5/6 > 5/8. Do the same with your parathas."]),
}
