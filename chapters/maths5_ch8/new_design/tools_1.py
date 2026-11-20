# -*- coding: utf-8 -*-
"""Tool specs for T1, T2 and T3 of Class 5 Chapter 8 (Weight and Capacity): Weight Check (the free try of the intro, right
after the hook), Scale Reader and Kilogram and Gram Line. Specs only; the tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds are labelled practice values. One
activity at a time, one instruction at a time, large controls, Back and Next in the same place, visible progress,
Hint, Retry and Reset always present, immediate specific feedback that is never red."""
from topics_common import T

TOOLS = {
    "weight_check": T(
        "tool_weight_check", "Weight Check", "manipulative",
        "Decide whether a recorded weight looks right for a thing by putting the thing on a balance against a 1 kg block and "
        "reading the unit: a thing heavier than the block must weigh 1 kg or more, which is 1,000 g or more, so a weight "
        "like 40 g cannot be right for it. This is the free first try of the chapter, so it asks and shows; the video that "
        "follows names the idea.",
        "Anu's room from your maths book, drawn as a warm 3D isometric scene with soft shadows and gentle animation. A two "
        "pan balance stands on the floor in the middle of the room and is the largest thing on screen. The right pan always "
        "holds a 1 kg block labelled 1 kg = 1,000 g. Around the balance, along the wall, are picture cards of the seven things "
        "on Anu's list: an iron almirah, a bed, a rice bag, a sofa, a bucket, a water bottle and a refrigerator, each with a "
        "tag showing the weight Anu wrote (40 g, 60 kg, 5 kg, 30 g, 1 kg 800 g, 650 g, 50 g). Two bins stand at the front, "
        "Looks right and Does not look right. An instruction strip at the top shows one sentence in large type, with progress "
        "dots under it. Controls: drag a picture card onto the left pan (the balance tips and a plain sentence under it says "
        "whether the thing is heavier than, lighter than or about the same as 1 kg); drag the card's tag into a bin; for "
        "practice cards, tap one of two tags to choose the fitting unit, for example 6 g or 6 kg; Check, Hint, Retry (clears "
        "the balance and the bins for this card), Reset (returns all cards), Back and Next in the same places on every card. "
        "Read-outs: the balance tilt with its sentence, a counter of cards placed, and a card number out of 5.",
        ["Look at Anu's room and her list from the story. Anu says an iron almirah weighs 40 g. "
         "Put the iron almirah on the balance against the 1 kg block and watch which side goes down, then press Next.",
         "Put a pencil, a school bag and a brick on the balance (practice values), pick the unit tag "
         "that fits each one, sort three more practice cards into the grams bin and the kilograms bin, and tell which weights "
         "are heavier or lighter than 1 kg.",
         "Answer the book's question on Anu's list. Put each of the seven things against the 1 kg block, "
         "read its tag and drop the tag in Looks right or Does not look right."],
        ["Card 1 (practice values): put the pencil on the left pan against the 1 kg block. Which side goes down? "
         "Answer: the 1 kg block side goes down, because a pencil is lighter than 1 kg.",
         "Card 2 (practice values): put the school bag, then the brick, on the left pan. Which side goes down each "
         "time? Answer: the thing's side goes down both times, because a school bag and a brick are heavier than 1 kg.",
         "Card 3 (practice values): pick the tag that fits. The pencil is 6 g or 6 kg. The school bag is 4 g or 4 kg. "
         "Answer: the pencil is 6 g, because 6 kg is 6,000 g, far too heavy for a pencil; the school bag is 4 kg, because "
         "4 g is lighter than a pencil.",
         "Card 4 (practice values): sort the three cards into the grams bin and the kilograms bin: an egg 50 g, a bag "
         "of cement 50 kg, a sugar sachet 5 g. Answer: the egg and the sugar sachet go in the grams bin, because they are "
         "lighter than 1 kg; the bag of cement goes in the kilograms bin, because it is much heavier than 1 kg.",
         "Challenge: 'Anu has recorded the weights of the items in her house. Check if she has recorded them "
         "correctly by putting a tick against them if they look correct. 1. Iron Almirah: 40 g; 2. Bed: 60 kg; 3. Rice Bag: "
         "5 kg; 4. Sofa: 30 g; 5. Bucket: 1 kg 800 g; 6. Water Bottle: 650 g; 7. Refrigerator: 50 g.' Put each thing on the "
         "balance, read its tag against 1 kg = 1,000 g and drop the tag in a bin. Sample answer: Bed, Rice Bag, Bucket and "
         "Water Bottle look right; Iron Almirah, Sofa and Refrigerator do not, because 40 g, 30 g and 50 g are far less than "
         "1,000 g. The bed, the bucket and the bottle are matters of judgement, so your answer may differ."],
        ["When a card goes on the pan the balance tips and the sentence says so, for example: The almirah is much heavier than "
         "the 1 kg block. For the borderline things (bucket, bottle) it says: Close to the block. Decide with the tag.",
         "A tag dropped in a bin is read against the block, for example: The tag says 40 g. 40 g is less than 1 kg, which is "
         "1,000 g, but the almirah is much heavier than 1 kg. Look again at the tag. The tool never calls a borderline thing "
         "wrong.",
         "A unit tag that does not fit slides back with a clue, for example: 6 kg is 6,000 g. Is a pencil that heavy?",
         "A card in the right bin locks in with a soft chime and a one line reason, for example: A bag of cement is much "
         "heavier than 1 kg, so kg."],
        "All five cards are done: the balance has been used for each of the seven things on Anu's list, each tag is in a bin, "
        "and the student has seen why 40 g, 30 g and 50 g cannot be the weight of an almirah, a sofa and a refrigerator.",
        ["currentCard", "leftPanItem", "balanceTilt", "tagChoice", "binContents", "cardsPlaced"],
        ["M_UNIT_SIZE"],
        ["What does the right pan hold? How heavy is it in grams? Look at which side of the balance goes down.",
         "Is the thing heavier or lighter than the 1 kg block? A heavier thing must weigh 1 kg or more, which is 1,000 g or "
         "more.",
         "Read the tag. Is it more or less than 1,000 g? Is g or kg the unit for a thing this heavy or this light?",
         "The almirah is far heavier than 1 kg, but 40 g is less than 1,000 g. Drop the tag in Does not look right."]),

    "scale_reader": T(
        "tool_scale_reader", "Scale Reader", "manipulative",
        "Read a needle on four kinds of weighing scale by finding what one small mark stands for (the weight between two "
        "labels divided by the number of gaps) and counting the marks from 0 to the needle, so that the same needle spot reads "
        "600 g on one scale and 60 g on another.",
        "The weighing counter of Anu's neighbourhood market, drawn as a warm 3D isometric scene with soft shadows and gentle "
        "animation. A big round dial scale on a stand fills the middle of the screen and is the largest thing on screen: 0 in "
        "red at the top, labels round the face, small marks between the labels and a draggable needle with a round hub. A "
        "scale chooser along the left edge shows four faces: a 4 kg full turn with 40 marks (100 g a mark), a 2 kg full turn "
        "with 20 marks (100 g a mark), a 6 kg full turn with 60 marks (100 g a mark) and a 1 kg full turn with 100 marks (10 g "
        "a mark). An instruction strip at the top shows one sentence in large type, with progress dots under it. Controls: "
        "drag the needle round the face (it snaps to the nearest small mark); tap two neighbouring labels to see the weight "
        "between them and the number of gaps; tap Count marks to light the marks one at a time from 0 to the needle; two "
        "number boxes under the dial, kg and g, to type the reading; Check, Hint, Retry (resets the needle for this face), "
        "Reset (restores all faces), Back and Next in the same places on every card. Read-outs: the weight of one mark once "
        "two labels are tapped, a running count of marks as they light up, and a card number out of 6.",
        ["Look at the dial from the video, with the needle past a label. Say what the last "
         "label passed is, then press Next to find what one small mark stands for.",
         "Tap two labels to find what one mark stands for, set the needle to a weight the card gives, "
         "read a needle the tool sets and type the weight in the kg and g boxes, and compare the same needle spot on two faces "
         "(practice values).",
         "Read the book's six scales (a) to (f) one by one and type each weight."],
        ["Card 1 (practice values): on the 4 kg face tap the labels 0 and 1 kg. What weight lies between them, how "
         "many gaps are there, and what does one mark stand for? Answer: 1 kg, which is 1,000 g, in 10 gaps; 1,000 ÷ 10 = "
         "100 g, so one mark stands for 100 g.",
         "Card 2 (practice values): on the 4 kg face set the needle to 300 g. Answer: the 3rd mark after 0, because "
         "300 ÷ 100 = 3.",
         "Card 3 (practice values): on the 4 kg face set the needle to 1 kg 200 g. Answer: 12 marks after 0, or 2 "
         "marks after the 1 kg label, because 1,200 ÷ 100 = 12.",
         "Card 4 (practice values): the tool sets the needle on the 14th mark of the 2 kg face and you read it. "
         "Answer: one mark is 100 g, 14 × 100 = 1,400 g, so the weight is 1 kg 400 g.",
         "Card 5 (practice values): the needle is on the 6th mark after 0 on the 4 kg face and on the 6th mark after "
         "0 on the 1 kg face. What does each read, and why do they differ? Answer: on the 4 kg face one mark is 100 g, so "
         "6 × 100 = 600 g; on the 1 kg face one mark is 10 g, so 6 × 10 = 60 g; the marks stand for different weights.",
         "Challenge: 'Read the scales. Write the correct weight in the space given below.' Read the six scales (a) "
         "to (f) of your maths book. Answer: (a) 600 g, (b) 1 kg 800 g, (c) 2 kg 500 g, (d) 2 kg 600 g, (e) 150 g, (f) 660 g, "
         "found by working out what one mark stands for on each face and counting the marks to the needle."],
        ["The needle snaps to a mark and the read-out says how many marks it is from 0, for example: 6 marks after 0.",
         "A reading that is the nearest printed number is answered with a clue, for example: The needle is past the 1 kg "
         "label, so the weight is more than 1 kg. Count the small marks after the label.",
         "A reading that treats every mark as 1 g is answered with the step, for example: Here one mark stands for 100 g, "
         "not 1 g. 6 marks make 6 × 100 g.",
         "A correct reading shows the working in one line, for example: 18 marks × 100 g = 1,800 g, which is 1 kg 800 g."],
        "All six cards are done, including the book's six scales (a) to (f), and the student has found what one mark stands "
        "for on each face before reading the needle.",
        ["currentCard", "chosenFace", "needleMark", "tappedLabels", "markWeight", "typedKg", "typedG"],
        ["M_NEAR_LABEL", "M_MARK_IS_ONE"],
        ["Where does the needle start? Look at the 0 at the top and follow the face round to the needle.",
         "What weight lies between two labels, and how many gaps are there between them? Dividing the weight by the gaps "
         "gives the weight of one mark.",
         "Find the last label the needle has passed, then count the marks after it and multiply by the weight of one mark.",
         "Press Count marks. The marks light up one by one and the tool adds the weight of each mark to the label."]),

    "kg_g_line": T(
        "tool_kg_g_line", "Kilogram and Gram Line", "manipulative",
        "Change kg and g to g and g to kg and g by putting numbers on a double number line (× 1,000 from the kg line to the g "
        "line and ÷ 1,000 back) and by splitting a mixed weight into its kg part and its g part, with the g part in three "
        "places.",
        "The weighing counter of Anu's neighbourhood market again, drawn as a warm 3D isometric scene with soft shadows and "
        "gentle animation. Two display balances stand side by side with the same bag on both, one showing kg and one showing "
        "g. Below them a long double number line is painted on the counter edge: the top line is in kg and the bottom line is "
        "in g, with equal ticks, and it is the largest thing on screen. A number card tray sits under the line. An arrow card "
        "× 1,000 can be dragged between the lines, and a mixed weight card (for example 6 kg 40 g) splits into a kg box and a "
        "g box beside a strip that pads the g box to three places. An instruction strip at the top shows one sentence in large "
        "type, with progress dots under it. Controls: drag number cards onto ticks (they snap); drag the × 1,000 arrow; type a "
        "missing number; a mode switch kg to g, g to kg and g; Check, Hint, Retry (clears this line), Reset (restores all "
        "lines), Back and Next in the same places on every card. Read-outs: the number of ticks filled, the multiplier shown "
        "on the arrow, and a card number out of 7.",
        ["Look at the one bag that shows 2 kg on one balance and 2,000 g on the other. Say what "
         "number the g line should show for 1 kg, then press Next.",
         "Fill the double number line for 4 kg, 9 kg and 16 kg and go back from grams to kg, split "
         "mixed weights into kg and g parts and write them in grams, and go back from grams to kg and g (practice values).",
         "Match the bags, decide who is right about 5 kg 50 g of sugar, and complete the conversions, all "
         "as the book gives them."],
        ["Card 1 (practice values): put 1 kg and 1,000 g on the line, then 4 kg, 9 kg and 16 kg with their grams. "
         "Answer: 4 kg is 4 × 1,000 = 4,000 g, 9 kg is 9,000 g and 16 kg is 16,000 g; every kg number is × 1,000 on the g "
         "line.",
         "Card 2 (practice values): go back. Put 9,000 g and 16,000 g on the g line and fill the kg line. Answer: "
         "9,000 ÷ 1,000 = 9 kg and 16,000 ÷ 1,000 = 16 kg.",
         "Card 3 (practice values): split 6 kg 40 g into a kg part and a g part and write it in grams. Answer: 6 kg "
         "is 6,000 g, and 40 g takes three places, 040, so the weight is 6,040 g, not 6,400 g.",
         "Card 4 (practice values): write 11,205 g in kg and g. Answer: take out the whole thousands, 11,205 − "
         "11,000 = 205, so 11 kg 205 g.",
         "Challenge: 'Match the bags that have the same weights. You can use the double number line.' Balance 1: 5 "
         "kg, 10 kg, 3 kg, 6 kg, 25 kg, 30 kg. Balance 2: 3,000 g, 6,000 g, 10,000 g, 30,000 g, 5,000 g, 25,000 g. Answer: 5 "
         "kg and 5,000 g, 10 kg and 10,000 g, 3 kg and 3,000 g, 6 kg and 6,000 g, 25 kg and 25,000 g, 30 kg and 30,000 g, "
         "each g number being 1,000 times the kg number; the line's blanks are 8 kg = 8,000 g, 15,000 g = 15 kg, 20 kg = "
         "20,000 g.",
         "Challenge: 'Shamim and Rehan observed someone buying sugar weighing 5 kg 50 g. They thought of the "
         "quantity in grams. How much is it? Who do you think is right and why?' One child says 5,050 g and the other says "
         "5,500 g. Answer: 5,050 g is right, because 5 kg is 5,000 g and 50 g takes three places, 050; 5,500 g would be 5 kg "
         "500 g.",
         "Challenge: 'Complete the conversions by filling in the blanks. You can use the double number line given "
         "below on which some numbers have been marked. (a) 7 kg 67 g = ___ g (b) 3 kg 300 g = ___ g (c) 8 kg 69 g = ___ g "
         "(d) 10,760 g = ___ kg ___ g (e) 4,080 g = ___ kg ___ g (f) 12,042 g = ___ kg ___ g' Answer: (a) 7,067 g, (b) 3,300 "
         "g, (c) 8,069 g, (d) 10 kg 760 g, (e) 4 kg 80 g, (f) 12 kg 42 g."],
        ["A card dropped on the right tick locks in with a soft chime, and the arrow shows the multiplier, for example: × "
         "1,000: 4 kg is 4,000 g.",
         "A card on the wrong tick slides back with a clue, for example: 4 kg is 4 × 1,000. Which g number is that?",
         "A g part that is not in three places is padded in the strip and the tool says so, for example: 40 g takes three "
         "places, 040, so 6 kg 40 g is 6,040 g.",
         "A reading that glues the parts the wrong way is answered with the other weight, for example: 6,400 g is 6 kg 400 g, "
         "which is a different weight."],
        "All seven cards are done, including the book's matching task, Shamim and Rehan's sugar and the six conversions, and "
        "the student has changed weights both ways on the double number line.",
        ["currentCard", "lineMode", "kgCards", "gCards", "arrowMultiplier", "mixedWeightParts", "typedValues"],
        ["M_KG_100G", "M_PART_PLACE"],
        ["How many g make 1 kg? Look at the first mark on the line, 1 kg and 1,000 g.",
         "Going from the kg line to the g line, what do you do to the number? Going back, what do you do?",
         "Change the kg part first, then add the g part in three places. To go back, take out the whole thousands.",
         "Take 4 kg: 4 × 1,000 = 4,000. Drop the card 4,000 g under 4 kg and use the same step for the next mark."]),
}
