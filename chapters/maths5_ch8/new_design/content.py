# -*- coding: utf-8 -*-
"""Chapter-level content for Class 5 Chapter 8, Weight and Capacity (Maths Mela, Grade 5, Chapter 8).

The plan follows the "Class 5 Mathematics Learning Experience Designer" brief (priority_doc.md sections A to F) and the
/lp pipeline's structure; the book decides every number and every question. Book lines are verbatim except: the book's
dashes become colons or commas; minus is U+2212; the rupee sign is written before the number (₹60); the book's
numbered lists inside a question are kept as printed. No em dash and no en dash anywhere here."""
from __future__ import annotations

CHAPTER = {
    "grade": 5,
    "label": "Class 5",
    "chapter_no": 8,
    "name": "Weight and Capacity",
    "book_part": "Maths Mela, Grade 5, Chapter 8",
    "source_pdf": "textbooks/class-5/eemm108.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Weight: Choosing Units and Reading Scales",
     "Judging whether a weight looks right for a thing, choosing between grams and kilograms, and reading weighing "
     "scales that have a needle."),
    ("M2", "Weight: Units and Calculations",
     "Changing kilograms and grams to grams and back, comparing weights, the milligram, the quintal and the tonne, "
     "adding, subtracting, multiplying and sharing weights, and finding costs with a double number line."),
    ("M3", "Capacity: Litres and Millilitres",
     "Choosing between litres and millilitres, changing between them, reading container scales, comparing, adding, "
     "subtracting, multiplying and dividing capacities, solving problems, and a revision of the whole chapter."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter takes place in Anu's neighbourhood market: a home, a grocery store, a fruit stall, a milkman's "
             "cart and a petrol pump. Weighing and pouring show what a kilogram, a gram, a litre and a millilitre are, "
             "how they are linked, and how to read, change, compare and calculate with them. A short video explains "
             "each idea, and an interactive tool lets the student try it alone.",
    "points": [
        {"title": "Videos teach, tools explore",
         "text": "Every idea has one short concept video. The tool that follows is where the student explores, "
                 "builds and checks the idea alone, with hints, retry and reset. Six tools, each with its own "
                 "purpose, follow the chapter's own plan."},
        {"title": "A tool in three steps",
         "text": "Each tool opens with a short recall of the video idea, then lets the student play and apply it, and "
                 "ends with the chapter's own question, used exactly as the book gives it."},
        {"title": "Every book question has its own video",
         "text": "Every solved example, Let Us Do, Let Us Find, Let Us Think, Let Us Compare and Let Us Solve question "
                 "and every answerable prompt of the book is its own short video with a step by step solution and a "
                 "question picture and a solution picture, in a Questions topic that follows the idea it practises."},
        {"title": "The picture is the mathematics",
         "text": "Scales with a needle, double number lines, kg and g columns and measuring jugs carry each idea: the "
                 "marks are counted, the units are written on the left, and the thing being measured is the largest "
                 "thing on screen."},
        {"title": "Only the book's numbers",
         "text": "Scales, tables, weights and capacities in the questions are the book's own. Any number the plan adds "
                 "is a practice value and is said to be one."},
    ],
}

# {module_id: strand letter}: the subject strand each module belongs to (core/qt.py builds every objective's strand).
# CBSE maths catalog: N Number, A Algebra, G Geometry, M Measurement, D Data, S Statistics and Probability.
MODULE_STRANDS = {"M1": "M", "M2": "M", "M3": "M"}

# every book item, with its kind. Home concepts are listed in DESIGN.md section 3.
NCERT_ITEMS = [
    # the opener, Check! Check!, and reading scales (p. 104)
    ("open.story", "text"), ("open.check", "prompt"),
    ("scale.note", "text"), ("scale.read", "exercise"),
    # different units, same measure (pp. 105 and 106)
    ("units.same", "text"), ("units.relation", "talk"), ("units.match", "prompt"),
    ("ex.shrenu", "example"), ("ex.flour", "example"),
    ("lf1.sugar", "exercise"), ("lf1.convert", "exercise"),
    # comparison between different weights (p. 107)
    ("cmp1.fruits", "prompt"), ("cmp1.signs", "prompt"),
    # milligram, quintal, tonne, times as heavy, King's Weight (pp. 108 to 110)
    ("mg.ants", "text"), ("mg.what", "text"), ("mg.similar", "text"), ("mg.note", "text"),
    ("lf2.sachet", "exercise"), ("lf2.mgline", "exercise"), ("ex.ornament", "example"), ("lf2.goldsmith", "exercise"),
    ("lf2.compare", "exercise"), ("lf2.whale", "exercise"), ("lf2.quintal", "exercise"), ("king.weight", "prompt"),
    ("qt.know", "text"), ("units.table", "text"),
    # adding and subtracting weights (pp. 110 and 111)
    ("add.ways", "text"), ("addsub.note", "text"), ("sub.ways", "text"),
    ("ex.rice_total", "example"), ("ex.rice_extra", "example"),
    ("lud2.Q1", "exercise"), ("lud2.Q2", "exercise"), ("lud2.Q3", "exercise"), ("lud2.Q4", "exercise"),
    ("lud2.Q5", "exercise"), ("lud2.Q6", "exercise"), ("lud2.Q7", "exercise"),
    # more operations on weight, cost and scaling (pp. 112 and 113)
    ("mul.way", "text"), ("div.way", "text"), ("ex.farmer", "example"), ("ex.nuts", "example"),
    ("lud3.Q1", "exercise"), ("lud3.Q2", "exercise"), ("lud3.Q3", "exercise"), ("lud3.Q4", "exercise"),
    # capacity: measuring, big to small, same measure (pp. 113 to 115)
    ("cap.tea", "prompt"), ("cap.bucket", "prompt"),
    ("bs.ramiz", "prompt"), ("bs.muskaan", "prompt"), ("bs.containers", "prompt"),
    ("dm.milkman", "prompt"), ("dm.table", "prompt"), ("ex.dev", "example"),
    ("lt.mary", "exercise"), ("lt.convert", "exercise"),
    # let us compare (pp. 115 to 117)
    ("cap.note", "text"), ("cap.add", "text"),
    ("lc.fuel", "exercise"), ("lc.compare", "exercise"), ("ex.sam", "example"), ("ex.bike", "example"),
    # let us solve (p. 118) and the summary
    ("ls.dnl", "text"),
    ("ls.Q1", "exercise"), ("ls.Q2", "exercise"), ("ls.Q3", "exercise"), ("ls.Q4", "exercise"), ("ls.Q5", "exercise"),
    ("summary", "text"),
]

MISCONCEPTIONS = [
    ("M_UNIT_SIZE", "The number alone tells how heavy a thing is, so 40 g and 40 kg are about the same."),
    ("M_NEAR_LABEL", "On a scale with a needle, read the number printed nearest the needle and ignore the small marks."),
    ("M_MARK_IS_ONE", "Each small mark on a scale stands for 1 unit, so the 6th mark is 6 g or 6 kg whatever the scale."),
    ("M_KG_100G", "1 kg is 100 g (or 1 l is 100 ml)."),
    ("M_PART_PLACE", "The g part of a mixed weight sits in the hundreds, so 5 kg 50 g is 5,500 g and 9 l 90 ml is 990 ml."),
    ("M_BIG_NUMBER", "The bigger number is the bigger weight, whatever the units, so 5,000 g is more than 7 kg."),
    ("M_QUINTAL", "1 quintal is 10 kg, or 1 tonne is 100 quintals, or 1 g is 100 mg."),
    ("M_NO_EXCHANGE", "When the g parts add up to 1,000 g or more, leave them as they are (4 kg 1,250 g) or forget to carry "
                      "1 kg."),
    ("M_SMALL_FROM_BIG", "In a subtraction, take the smaller number from the bigger one in each column, so "
                         "2 kg 500 g minus 1 kg 750 g is 1 kg 250 g."),
    ("M_ONE_PART", "To multiply or share a weight, change only the kg part and leave the g part alone."),
    ("M_ADD_TO_SCALE", "To scale a double number line, add the same number to both lines instead of multiplying."),
    ("M_PART_FULL_PRICE", "A part of a kilogram costs the same as a whole kilogram, so 500 g of rice costs the price of "
                          "1 kg."),
    ("M_MIXED_UNITS", "Quantities in different units can be added, compared or divided as they are, without changing "
                      "to one unit."),
]

SOLUTION_NOTES = [
    {"item": "The six weighing scales (Let Us Do, first page of the chapter)",
     "printed_solution": "The book prints no answers; the readings are in the pictures.",
     "correct": "Read by counting the small marks from 0 to the needle, after measuring the needle on a high resolution "
                "render: (a) 4 kg full turn, 40 marks of 100 g, 6th mark, 600 g; (b) 2 kg full turn, 20 marks of 100 g, "
                "18th mark, 1 kg 800 g; (c) 6 kg full turn, 60 marks of 100 g, 25th mark, 2 kg 500 g; (d) as (a), 26th "
                "mark, 2 kg 600 g; (e) 1 kg full turn, 100 marks of 10 g, 15th mark, 150 g; (f) as (e), 66th mark, "
                "660 g. The answer boxes agree (grams only for (a), (e), (f)). To be confirmed."},
    {"item": "Check! Check! (Anu's list)",
     "printed_solution": "The book prints no answer.",
     "correct": "Ticks on Bed 60 kg, Rice Bag 5 kg, Bucket 1 kg 800 g and Water Bottle 650 g; crosses on Iron Almirah "
                "40 g, Sofa 30 g and Refrigerator 50 g (far too light for heavy things). Bed, bucket and bottle are "
                "matters of judgement, so the plan gives a labelled sample answer and says the student's answer may "
                "differ."},
    {"item": "Different Units but Same Measure (weight): the double number line, not to scale",
     "printed_solution": "The line has blanks; the matching task does not name them.",
     "correct": "The plan fills them by the x1,000 rule: 3 kg = 3,000 g (the x3 arrow on both lines), 8 kg = 8,000 g, "
                "15,000 g = 15 kg, 20 kg = 20,000 g, 25,000 g = 25 kg, 30 kg = 30,000 g."},
    {"item": "Let Us Find (conversions): the last two marks of the double number line",
     "printed_solution": "The two marks at the right end have blanks for both kg and g and no given value.",
     "correct": "The plan fills only the marks that have one given value (3 kg = 3,000 g, 4,000 g = 4 kg, 7 kg = 7,000 g, "
                "8 kg = 8,000 g, 10,000 g = 10 kg, 12,000 g = 12 kg) and leaves the last two marks unfilled."},
    {"item": "Shamim and Rehan, and Mary and Daisy",
     "printed_solution": "The book does not say which child is which.",
     "correct": "The plan says one child and the other child and never names who said what."},
    {"item": "Comparison between Different Weights, (c): 10035 g",
     "printed_solution": "The book prints 10035 g with no comma, while every other number has one.",
     "correct": "The question is kept as printed; the working writes 10,035 g."},
    {"item": "From Tiny to Big, the Grocery Store: speech bubble",
     "printed_solution": "The bubble ends 'total rice bought is 4 kg 250.' with no unit.",
     "correct": "The plan writes 4 kg 250 g (the working below the bubble says 4 kg 250 g)."},
    {"item": "Tea for 2 cups, and the bucket of 20 ml",
     "printed_solution": "Open questions with no printed answer and no cup size.",
     "correct": "The plan gives a labelled sample answer; where it needs a cup size it uses a practice value (a cup holds "
                "about 150 ml, cups differ). The bucket answer uses only the book's 500 ml bottle (500 is 25 times 20)."},
    {"item": "Big to Small, Small to Big: Ramiz and Muskaan",
     "printed_solution": "'Ramiz drinks ___ l of water in a day' does not say whether he drinks more than the two bottles; "
                         "'how many times would she need to refill' does not say if the first fill counts.",
     "correct": "Ramiz: the two 500 ml bottles only, 1,000 ml = 1 l. Muskaan: 3 l = 3,000 ml and 3,000 ÷ 500 = 6, so 6 "
                "bottles of 500 ml (6 times, counting every fill)."},
    {"item": "Let Us Do on adding and subtracting weights, Q7 (flour for the langar)",
     "printed_solution": "The wording can be read in more than one way.",
     "correct": "65 kg was bought on the first day and 42 kg 275 g of it was used; 52 kg 500 g was bought the next day: "
                "65 kg minus 42 kg 275 g plus 52 kg 500 g = 75 kg 225 g."},
    {"item": "More Operations on Weight: the box of nuts",
     "printed_solution": "The question asks for the weight in grams; the working prints 1 kg 200 g.",
     "correct": "The plan gives 1 kg 200 g = 1,200 g (the book's own hint, 4800 ÷ 4)."},
    {"item": "Let Us Find: the elephant and the whale",
     "printed_solution": "The picture gives 5,000 kg, an arrow 'x 40' and a blank for the whale.",
     "correct": "The whale weighs 40 times the elephant: 5,000 x 40 = 200,000 kg. The numbers are the book's, not a "
                "real measure."},
    {"item": "Let Us Compare: the table of fuel",
     "printed_solution": "The last column (total quantity of fuel) is empty and the question does not ask for it directly.",
     "correct": "The plan fills the column first (3 x 500 = 1,500; 6 x 300 = 1,800; 10 x 50 = 500; 12 x 8 = 96; 25 x 5 = "
                "125), then answers (a) 300 l and (b) 4,021 l. The book's numbers (500 litres in a truck) are kept as "
                "printed."},
    {"item": "Let Us Solve 2: milk poured into 8 glasses",
     "printed_solution": "The book says the milk is poured equally into 8 glasses of 360 ml each and 120 ml is left.",
     "correct": "Every glass is filled to its capacity: 8 x 360 = 2,880 ml poured, 120 ml left, so the bottle held "
                "3,000 ml = 3 l."},
    {"item": "Let Us Do on cost (grocery table), part of a kilogram",
     "printed_solution": "The book prints no method for the weights with a g part (12 kg 500 g, 7 kg 250 g, 3 kg 600 g, "
                         "1 kg 400 g).",
     "correct": "The plan uses the chapter's own double number line: the whole kilograms by the cost of 1 kg, and the g "
                "part from 1,000 g (500 g is half, 250 g is a quarter, 100 g is a tenth of the cost of 1 kg); no "
                "decimals are used."},
    {"item": "The notes for teachers (pages 104, 108, 110, 117)",
     "printed_solution": "Written for a teacher.",
     "correct": "Their content is used inside the concept videos; no teaching role is given to a teacher."},
    {"item": "Kit, cut-outs and the Learning Material Sheets",
     "printed_solution": "This chapter does not refer to a kit, a cut-out, a token, a grid or a sheet.",
     "correct": "The only words that look like it are 'kitchen scale' and 'community kitchen'. Nothing is taken from the supplied "
                "sheets and no assumption about a kit is made."},
    {"item": "Brief: revision video",
     "printed_solution": "The brief asks for an interactive recap or revision video.",
     "correct": "The pipeline has no recap video, so the last topic is a text summary with short concept checks."},
    {"item": "Brief: tool before video, 9 to 11 tools",
     "printed_solution": "The pipeline puts a free try tool directly after the hook and uses a tool only where the idea is "
                         "learnt by manipulation.",
     "correct": "The free try Weight Check comes before the concept video; the chapter has 6 tools, not 9 to 11."},
    {"item": "Open prompts (sample answers)",
     "printed_solution": "No single answer.",
     "correct": "The plan gives one reasoned sample answer and says the student's answer may differ."},
]
ERRATA = []

DESIGN_REFERENCES = [
    {"text": "priority_doc.md (the plan written to the 'Class 5 Mathematics Learning Experience Designer' brief, "
             "2026-11-06): topic flow, video types, the 6 tools, the shared visual language and the learning rules "
             "decide this chapter's design.", "url": ""},
    {"text": "docs/01_runbook.md and .claude/skills/lp/SKILL.md: framing intro with a free-try tool, idea topics each "
             "ending in a Practice concept, a Questions topic after every idea topic with a question concept and an "
             "answer concept per book question, and one summary topic.", "url": ""},
]

# The book's own figures that carry mathematics, keyed by authored concept key. One concept image per teaching,
# hook and summary concept where a drawn figure is the maths; the tool concepts (Practice / free try) are pictured by
# their tool.
FIGURES = {
    "T1.C1": ["Anu's room with an iron almirah, a bed, a rice bag, a sofa, a bucket, a water bottle and a refrigerator, "
              "each with its recorded weight tag from Anu's list. No tick and no answer."],
    "T1B.C1": ["A two pan balance: a pencil on one pan and a 1 kg block on the other pan, and a school bag against a 1 kg "
               "block, with the tags 6 g, 4 kg and the line 1 kg = 1,000 g."],
    "T2.C1": ["A round scale with 0 in red at the top, labels 1 kg to 5 kg round the face, 5 equal gaps between labels and "
              "a needle on the 3rd mark after 3 kg."],
    "T2.C2": ["A round scale with a 2 kg full turn, labels at 0, 500 g, 1 kg and 1 kg 500 g, 10 equal gaps between labels and "
              "a needle on the 7th mark after the 1 kg 500 g label."],
    "T3.C1": ["A double number line, kg above and g below, with 1 kg to 1,000 g, 4 kg and 9 kg joined to their grams by an "
              "arrow marked x1,000."],
    "T3.C2": ["A mixed weight 6 kg 40 g split into a 6 kg part and a 40 g part, with the g part written in three places and "
              "the result 6,040 g."],
    "T4.C1": ["A number line in grams with 4,020 g and 4,200 g marked, and 4 kg 200 g joined to 4,200 g."],
    "T5.C1": ["A double number line, g above and mg below, with 1 g to 1,000 mg, 8 g and 2 g 40 mg."],
    "T5.C2": ["A ladder of units from milligram to gram to kilogram to quintal to tonne, with arrows marked x1,000, x1,000, "
              "x100 and x10."],
    "T5.C3": ["A bar of 3,000 kg repeated 6 times, and a bar of 450 kg cut into 9 equal bars."],
    "T6.C1": ["A kg and g column sum, 3 kg 600 g plus 2 kg 700 g, with 1,300 g circled and a carry of 1 kg."],
    "T6.C2": ["A kg and g column subtraction, 5 kg 200 g minus 2 kg 800 g, with 1 kg broken into 1,000 g."],
    "T7.C1": ["Six sacks each marked 2 kg 500 g, and the sum in kg and g separately."],
    "T7.C2": ["A load of 9 kg 600 g shared into 3 equal boxes, each 3 kg 200 g."],
    "T8.C1": ["A double number line with kg above and rupees below: 1 kg to 36 rupees, 4 kg, and 500 g as half of 1 kg."],
    "T8.C2": ["A double number line with plates above and grams of lentils below: 3 plates to 240 g, an arrow x3 to 9 plates "
              "and 720 g."],
    "T9.C1": ["A cup of juice marked 200 ml beside a drum marked 200 l, with the tags ml and l."],
    "T10.C1": ["A double number line, l above and ml below, with 1 l to 1,000 ml, a jug of 4 l and 4,000 ml."],
    "T10.C2": ["A 2 l jug and a 250 ml cup side by side, with 2 l 250 ml written as 2,250 ml."],
    "T11.C1": ["A number line in ml with 2,050 ml and 2,500 ml marked."],
    "T11.C2": ["A l and ml column sum, 4 l 600 ml plus 3 l 700 ml, with a carry of 1 l, beside 6 l 200 ml minus 2 l 900 ml."],
    "T12.C1": ["Six jugs of 1 l 250 ml in a row, and a can of 9 l 600 ml poured into 8 equal cans."],
    "T13.C1": ["The market lane with a stop for each idea of the chapter: a scale, a double number line, a kg and g column, "
               "a price board and a measuring jug."],
}
