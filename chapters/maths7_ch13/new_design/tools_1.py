# -*- coding: utf-8 -*-
"""Tool specs for module M1 (statistical questions and the mean as a fair share)."""
from topics_common import T

TOOLS = {
    "stat_question_sorter": T(
        "tool_stat_question_sorter", "Variability Test Question Sorter", "manipulative",
        "A question is statistical when answering it needs many values that vary; a question with one fixed answer or "
        "one person's reply is not. The student tests each card by imagining the answers it would collect.",
        "A deck of question cards at the top; two bins below, Statistical and Not statistical; when a card is held, a "
        "small panel shows three imagined answers the question would collect; a reason strip under each bin.",
        ["Read the card and predict the bin before opening the panel.",
         "Open the imagined answers panel and check whether the answers vary.",
         "Drop the card in a bin and pick the reason: answers vary, one fixed fact, or one person's reply.",
         "Finish the deck and review any card that came back."],
        ["How many hours do the children in your class sleep on a school night? (statistical)",
         "How many legs does a spider have? (not statistical: one fixed fact)",
         "What is your favourite colour? (not statistical: one person's reply)",
         "How much do vegetable prices change across the weeks of a month? (statistical)",
         "How tall is the tallest tree in the school ground? (not statistical: one measurement)",
         "How long do children in your area take to walk to school? (statistical)"],
        ["A card in the wrong bin returns with its imagined answers shown side by side, so the variation, or lack of "
         "it, is visible.",
         "A correct bin with a wrong reason keeps the card but asks for the reason again.",
         "The deck closes with a count of correct cards and the reasons chosen."],
        "All six cards are sorted with a correct reason.",
        ["cardIndex", "bin", "reason", "panelOpen", "correctCount"],
        ["M_ONE_ANSWER"],
        ["Who or what would you ask to answer this question?",
         "Imagine collecting several answers. Would they all be the same?",
         "If the answers would differ from person to person or day to day, the question is statistical.",
         "The answers for this card are shown; they vary (or do not), so it belongs in that bin. A new card follows."]),

    "bar_leveller": T(
        "tool_bar_leveller", "Bar Levelling Mean Finder", "manipulative",
        "The mean is the fair share: moving units from tall bars to short bars keeps the total the same, and when all "
        "bars are level their common height is the total divided by the number of bars.",
        "A row of unit-block bars for a small data set; blocks can be dragged from one bar to another; a running total "
        "that never changes; a dashed line the student places at a predicted level; a check panel showing total ÷ "
        "count when all bars are level.",
        ["Predict the level by placing the dashed line before moving any block.",
         "Drag blocks from taller bars to shorter bars until every bar has the same height.",
         "Compare the level with the prediction and with total ÷ count.",
         "For data that does not level exactly, split the leftover blocks into parts."],
        ["Guavas 3, 8, 10, 5, 4: level at 6.",
         "Guavas 5, 4, 6, 3, 4, 8: level at 5.",
         "Flowers 2, 7, 9, 4, 3: level at 5.",
         "Bounces 6, 2, 9, 5, 4, 6, 3, 5: level at 5.",
         "Runs 26, 53, 2, 15 in tens and ones blocks: level at 24.",
         "Times 17, 18, 17, 16, 19, 17, 18: 122 ÷ 7, between 17 and 18."],
        ["The total counter glows if a block is lost or added, because levelling never changes the total.",
         "A level line that is not at the same height for every bar flashes on the uneven bars.",
         "When all bars are level, the check panel shows total ÷ count and the level side by side."],
        "All six sets are levelled and each level matches total ÷ count.",
        ["bars", "total", "count", "predictedLevel", "levelReached"],
        ["M_MEAN_IN_DATA", "M_TOTAL_COMPARE"],
        ["Which bars are above the level you predicted, and which are below?",
         "Move blocks from the tallest bar to the shortest bar, one at a time.",
         "Add all the blocks and divide by the number of bars to find where they must stop.",
         "The bars are levelled for you, and the level equals total ÷ count. A new set follows."]),
}
