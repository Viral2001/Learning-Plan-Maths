# -*- coding: utf-8 -*-
"""Topics T1 to T5 (module M1: tenths and hundredths). Book sections 3.1, 3.2 and 3.3."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Introduction ==============================================================
TOPICS.append(TOPIC(
    "T1", "M1", "Sonu's Screws", ["3.1"], "Understand",
    "",
    "Two screws that look the same but are not, and an open question: how can we measure a gap smaller than the "
    "smallest mark on a ruler?",
    [A("T1.C1", "Two screws that look the same", "Remember",
       "",
       textbook=["3.1 The Need for Smaller Units",
                 "Sonu's mother was fixing a toy. She was trying to join two pieces with the help of a screw. Sonu "
                 "was watching his mother with great curiosity. His mother was unable to join the pieces. Sonu asked "
                 "why. His mother said that the screw was not of the right size.",
                 "She brought another screw from the box and was able to fix the toy.",
                 "The two screws looked the same to Sonu. But when he observed them closely, he saw they were of "
                 "slightly different lengths.",
                 "Sonu was fascinated by how such a small difference in lengths could matter so much. He was curious "
                 "to know the difference in lengths. He was also curious to know how little the difference was "
                 "because the screws looked nearly the same."],
       teach=["Picture Sonu watching his mother mend a toy. One screw does not fit, and a second screw that looks "
              "just the same does.",
              "Make a guess before the next step: how could anyone tell how much longer one screw is than the other?"],
       ncert=["3.1.story"], video_focus=["HOOK"], minutes=4, enrichment=True),
     A("T1.C2", "The question to keep: how do we measure a very small gap?", "Understand", "",
       textbook=["In the following figure, screws are placed above a scale. Measure them and write their length in "
                 "the space provided.",
                 "Which scale helped you measure the length of the screws accurately? Why?"],
       teach=["Predict: a ruler with only whole centimetre marks, or a ruler with ten small parts in every "
              "centimetre. Which one can tell the two screws apart?",
              "The next topics split a unit into smaller and smaller equal parts and give each part a name and a "
              "way of writing it."],
       ncert=["3.1.which_scale"], enrichment=True)],
    topic_type="framing"))

# ============================== T2 Tenths ====================================================================
TOPICS.append(TOPIC(
    "T2", "M1", "The Need for Smaller Units and the Tenth", ["3.1", "3.2"], "Apply",
    "Students read a length between two whole marks as units and tenths, write it both as a mixed number and as a "
    "count of tenths, and arrange lengths written in tenths in increasing order.",
    "When a length falls between two whole marks, the unit is split into 10 equal parts called tenths, and the "
    "length is written as whole units and tenths or as one count of tenths.",
    [A("T2.C1", "Reading between the marks", "Understand",
       "Students read a length that ends between two whole marks of a ruler as units and tenths of a unit, and "
       "explain why the unit was split into smaller parts.",
       textbook=["As seen on the ruler, the unit length between two consecutive numbers is divided into 10 equal "
                 "parts. To get the length 2 7/10 cm, we go from 0 to 2 and then take seven parts of 1/10. The "
                 "length of the screw is 2 cm and 7/10 cm. Similarly, we can make sense of the length 3 2/10 cm.",
                 "We read 2 7/10 cm as two and seven-tenth centimeters, and 3 2/10 cm as three and two-tenth "
                 "centimeters.",
                 "Can you explain why the unit was divided into smaller parts to measure the screws?",
                 "Measure the following objects using a scale and write their measurements in centimeters (as shown "
                 "earlier for the lengths of the screws): pen, sharpener, and any other object of your choice.",
                 "Write the measurements of the objects shown in the picture.",
                 "As seen here, when exact measures are required we can make use of smaller units of measurement."],
       teach=["Predict first: a screw ends after the 2 cm mark but before the 3 cm mark. Is it nearer 2 cm or 3 cm, "
              "and can a whole number of centimetres name its length?",
              "No whole number fits, so the centimetre is split into 10 equal parts. Each part is 1/10 of a "
              "centimetre.",
              "Count the whole centimetres first, then the tenths after them: that is how 2 7/10 cm is read.",
              "Now measure a pen, a sharpener and one object of your choice, and write each length as units and "
              "tenths."],
       examples=[
           WE("A ruler has every centimetre split into 10 equal parts. One screw ends 7 parts after the 2 cm mark "
              "and another ends 2 parts after the 3 cm mark. Write each length and say what the first one means.",
              ["The first screw is more than 2 1/2 cm but less than 3 cm, so it lies between 2 cm and 3 cm.",
               "The unit between two consecutive numbers is divided into 10 equal parts, so each part is 1/10 cm.",
               "From 0 we go to 2, then take 7 parts of 1/10: the length is 2 cm and 7/10 cm, that is 2 7/10 cm.",
               "In the same way the second screw is 3 cm and 2/10 cm, that is 3 2/10 cm."],
              "First screw 2 7/10 cm, second screw 3 2/10 cm",
              ncert=["3.1.screws", "3.1.meaning", "3.1.why_smaller", "3.1.measure"]),
           WE("Along a ruler marked in tenths of a centimetre, an eraser ends 4 parts after the 2 cm mark, a pencil "
              "ends 5 parts after the 4 cm mark and a chalk ends 4 parts after the 1 cm mark. Write each length.",
              ["Each part is 1/10 cm, so we read units first and then the parts.",
               "Eraser: 2 cm and 4 parts, so 2 4/10 cm.",
               "Pencil: 4 cm and 5 parts, so 4 5/10 cm, which is also 4 1/2 cm because 5/10 is half.",
               "Chalk: 1 cm and 4 parts, so 1 4/10 cm."],
              "Eraser 2 4/10 cm, pencil 4 5/10 cm (4 1/2 cm), chalk 1 4/10 cm",
              ncert=["3.1.objects"])],
       key_terms=["tenth", "mixed number"], misconceptions=["M_PART_AS_UNIT", "M_BIGGER_DENOMINATOR"], minutes=10),
     A("T2.C2", "A tenth part: two ways to write a length", "Understand",
       "Students write a length of whole units and tenths both as a mixed number and as a count of tenths, and read "
       "mixed numbers and tenths aloud.",
       textbook=["3.2 A Tenth Part",
                 "The length of the pencil shown in the figure below is 3 4/10 units, which can also be read as 3 "
                 "units and four one-tenths, i.e., (3 × 1) + (4 × 1/10) units.",
                 "10 times 1/10 is 1 unit. This length is the same as 34 one-tenths units because 10 "
                 "one-tenths units make one unit.",
                 "34 × 1/10 = 34/10 = 10/10 + 10/10 + 10/10 + 4/10 (34 one-tenths) = 1 + 1 + 1 + 4/10 (3 and 4 "
                 "one-tenths).",
                 "A few numbers with fractional units are shown below along with how to read them. 4 1/10 'four and "
                 "one-tenth'; 4/10 'four one-tenths' or 'four-tenths'; 41/10 'forty-one one-tenths' or 'forty-one "
                 "tenths'; 41 1/10 'forty-one and one-tenth'.",
                 "For the objects shown below, write their lengths in two ways and read them aloud. An example is "
                 "given for the USB cable. (Note that the unit length used in each diagram is not the same). The "
                 "length of the USB cable is 4 and 8/10 units or 48/10 units."],
       teach=["Predict first: a pencil is 3 units and 4 tenths long. How many tenths is that altogether?",
              "One unit is 10 tenths, so 3 units is 30 tenths. Add the 4 tenths and the pencil is 34 tenths long.",
              "So every length in tenths can be written in two ways: as whole units and tenths, or as one count of "
              "tenths."],
       examples=[
           WE("A pencil is 3 4/10 units long. Write its length as a count of tenths and show why it is the same "
              "length.",
              ["10 one-tenths make 1 unit, so 3 units is 3 × 10 = 30 tenths.",
               "30 tenths and 4 tenths make 34 tenths, so the length is 34/10 units.",
               "Check: 34/10 = 10/10 + 10/10 + 10/10 + 4/10, and each 10/10 is 1 unit, so that is 1 + 1 + 1 + 4/10 = "
               "3 4/10."],
              "34/10 units", ncert=["3.2.pencil"]),
           WE("A USB cable is 4 8/10 units long. Write it in two ways. Then read aloud 4 1/10, 4/10, 41/10 and "
              "41 1/10. Three more objects are drawn on their own unit scales: a hand that reaches 1 unit and 6 "
              "tenths, a box that is 2 units and 3 tenths, and a leaf that is 3 units and 9 tenths. Write each of "
              "these in two ways.",
              ["USB cable: 4 units and 8 tenths is 4 8/10, and 4 × 10 + 8 = 48 tenths, so 48/10.",
               "4 1/10 is four and one-tenth; 4/10 is four-tenths; 41/10 is forty-one tenths; 41 1/10 is "
               "forty-one and one-tenth.",
               "Hand: 1 6/10, and 1 × 10 + 6 = 16 tenths, so 16/10.",
               "Box: 2 3/10, and 2 × 10 + 3 = 23 tenths, so 23/10.",
               "Leaf: 3 9/10, and 3 × 10 + 9 = 39 tenths, so 39/10."],
              "USB 4 8/10 = 48/10; hand 1 6/10 = 16/10; box 2 3/10 = 23/10; leaf 3 9/10 = 39/10",
              ncert=["3.2.reading", "3.2.usb"])],
       key_terms=["one-tenth"], misconceptions=["M_PART_AS_UNIT"], minutes=10),
     A("T2.C3", "Ordering lengths written in tenths", "Apply",
       "Students arrange lengths written as mixed numbers and as counts of tenths in increasing order by writing "
       "them all as counts of tenths.",
       textbook=["Arrange these lengths in increasing order: (a) 9/10 (b) 1 7/10 (c) 130/10 (d) 13 1/10 (e) 10 "
                 "5/10 (f) 7 6/10 (g) 6 7/10 (h) 4/10",
                 "Arrange the following lengths in increasing order: 4 1/10, 4/10, 41/10, 41 1/10."],
       teach=["Predict first: which is longer, 130/10 or 13 1/10? Can you tell without changing either?",
              "Write every length as a count of tenths, and the biggest count is the longest length.",
              "A mixed number such as 7 6/10 is 7 × 10 + 6 = 76 tenths."],
       examples=[
           WE("Arrange these lengths in increasing order: 9/10, 1 7/10, 130/10, 13 1/10, 10 5/10, 7 6/10, 6 7/10, "
              "4/10.",
              ["Write each as a count of tenths: 9/10, 17/10, 130/10, 131/10, 105/10, 76/10, 67/10 and 4/10.",
               "In increasing order the counts are 4, 9, 17, 67, 76, 105, 130 and 131.",
               "So the lengths in increasing order are 4/10, 9/10, 1 7/10, 6 7/10, 7 6/10, 10 5/10, 130/10 and "
               "13 1/10."],
              "4/10, 9/10, 1 7/10, 6 7/10, 7 6/10, 10 5/10, 130/10, 13 1/10", ncert=["3.2.order1"]),
           WE("Arrange these lengths in increasing order: 4 1/10, 4/10, 41/10 and 41 1/10.",
              ["As counts of tenths they are 41, 4, 41 and 411.",
               "The smallest count is 4, so 4/10 comes first.",
               "41/10 and 4 1/10 are the same length, because both are 41 tenths.",
               "The biggest is 41 1/10, which is 411 tenths."],
              "4/10, then 4 1/10 and 41/10 (equal), then 41 1/10", ncert=["3.2.order2"])],
       key_terms=["increasing order"], misconceptions=["M_BIGGER_DENOMINATOR"], minutes=10),
     DOER("T2.C4", "Practice: read, write and order lengths in tenths", "equal_part_scale_splitter", "Apply",
          "Students read lengths between whole marks as units and tenths, write them as counts of tenths, and put "
          "them in increasing order.",
          ["Split the unit into 10 equal parts and count the parts after the lower whole mark.",
           "A length of units and tenths is also a count of tenths: units times 10, plus the tenths.",
           "To order lengths, write all of them as counts of tenths."],
          ncert=[])]))

# ============================== T3 Adding and subtracting tenths =============================================
TOPICS.append(TOPIC(
    "T3", "M1", "Adding and Subtracting Tenths", ["3.2"], "Apply",
    "Students add and subtract lengths written in units and tenths by working on the tenths first and regrouping "
    "10 tenths with 1 unit, and extend a pattern of numbers in tenths.",
    "Tenths are added and subtracted like whole numbers: 10 tenths regroup to 1 unit when adding, and 1 unit "
    "breaks into 10 tenths when subtracting.",
    [A("T3.C1", "Adding lengths in tenths", "Apply",
       "Students add two or more lengths written as units and tenths, regrouping 10 tenths as 1 unit.",
       textbook=["Sonu is measuring some of his body parts. The length of Sonu's lower arm is 2 7/10 units, and that "
                 "of his upper arm is 3 6/10 units. What is the total length of his arm?",
                 "To get the total length, let us see the lower and upper arm length as 2 units and 7 one-tenths, and "
                 "3 units and 6 one-tenths, respectively. So, there are (2 + 3) units and (7 + 6) one-tenths. "
                 "Together, they make 5 units and 13 one-tenths. But 13 one-tenths is 1 unit and 3 one-tenths. So, "
                 "the total length is 6 units and 3 one-tenths.",
                 "(2 + 3) + (7/10 + 6/10) = (2 + 3) + (13/10) = 5 + 13/10 = 5 + 10/10 + 3/10 = 5 + 1 + 3/10 = 6 + "
                 "3/10 = 6 3/10.",
                 "Or, both the lengths can be converted to tenths and then added: 27 one-tenths and 36 one-tenths "
                 "is 63 one-tenths, 27/10 + 36/10 = 63/10. 63/10 is the same as 60 one-tenths (60/10) and 3 "
                 "one-tenths (3/10), which is equal to 6 units and 3 one-tenths, i.e., 6 3/10.",
                 "The lengths of the body parts of a honeybee are given. Find its total length. Head: 2 3/10 units. "
                 "Thorax: 5 4/10 units. Abdomen: 7 5/10 units."],
       teach=["Predict first: 2 7/10 and 3 6/10. Will the tenths together be more than a whole unit?",
              "Add the whole units, add the tenths, and when the tenths reach 10 or more, change 10 tenths into 1 "
              "unit.",
              "The other way is to change both lengths to tenths, add the counts, and change back."],
       examples=[
           WE("Sonu's lower arm is 2 7/10 units and his upper arm is 3 6/10 units. What is the total length of his "
              "arm? Add in the two ways.",
              ["Units: 2 + 3 = 5. Tenths: 7/10 + 6/10 = 13/10.",
               "13 tenths is 1 unit and 3 tenths, so 5 + 13/10 = 5 + 10/10 + 3/10 = 5 + 1 + 3/10 = 6 3/10.",
               "In tenths: 2 7/10 is 27/10 and 3 6/10 is 36/10, and 27/10 + 36/10 = 63/10.",
               "63/10 is 60/10 + 3/10, which is 6 units and 3 tenths, so 6 3/10 again."],
              "6 3/10 units", ncert=["3.2.arm"]),
           WE("The parts of a honeybee are 2 3/10 units (head), 5 4/10 units (thorax) and 7 5/10 units (abdomen). "
              "Find its total length.",
              ["Whole units: 2 + 5 + 7 = 14.",
               "Tenths: 3 + 4 + 5 = 12 tenths, which is 1 unit and 2 tenths.",
               "Total: 14 + 1 = 15 units and 2 tenths."],
              "15 2/10 units", ncert=["3.2.honeybee"])],
       key_terms=["regroup"], misconceptions=["M_ADD_DENOMINATORS"], minutes=10),
     A("T3.C2", "Subtracting lengths in tenths", "Apply",
       "Students subtract one length in units and tenths from another, breaking 1 unit into 10 tenths when there "
       "are too few tenths.",
       textbook=["The length of Shylaja's hand is 12 4/10 units, and her palm is 6 7/10 units, as shown in the "
                 "picture. What is the length of the longest (middle) finger?",
                 "The length of the finger can be found by evaluating (12 + 4/10) − (6 + 7/10). This can be done in "
                 "different ways. For example, (a) 12 + 4/10 − 6 − 7/10 = (12 − 6) + (4/10 − 7/10) = 6 − 3/10 = 5 + "
                 "1 − 3/10 = 5 + 10/10 − 3/10 = 5 + 7/10 = 5 7/10. Discuss what is being done here and why.",
                 "(b) As in the case of counting numbers, it is convenient to start subtraction from the tenths. We "
                 "cannot remove 7 one-tenths from 4 one-tenths. So we split a unit from 12 and convert it to 10 "
                 "one-tenths. Now, the number has 11 units and 14 one-tenths. We subtract 7 one-tenths from 14 "
                 "one-tenths and then subtract 6 units from 11 units. 12 4/10 becomes 11 14/10, and 11 14/10 − 6 "
                 "7/10 = 5 7/10.",
                 "Try computing the difference by converting both lengths to tenths.",
                 "A Celestial Pearl Danio's length is 2 4/10 cm, and the length of a Philippine Goby is 9/10 cm. "
                 "What is the difference in their lengths? How big are these fish compared to your finger?"],
       teach=["Predict first: 12 4/10 take away 6 7/10. Can you take 7 tenths from 4 tenths?",
              "No, so one unit of the 12 is broken into 10 tenths. Now there are 11 units and 14 tenths.",
              "Take the tenths first, then the units. Or turn both lengths into tenths and take away the counts."],
       examples=[
           WE("Shylaja's hand is 12 4/10 units long and her palm is 6 7/10 units. How long is her middle finger? "
              "Solve it by breaking a unit, and check by converting to tenths.",
              ["There are only 4 tenths in the hand, and 7 tenths must be taken away.",
               "Break 1 unit of the 12 into 10 tenths: 12 4/10 becomes 11 14/10.",
               "14 tenths − 7 tenths = 7 tenths, and 11 units − 6 units = 5 units, so 5 7/10.",
               "Check in tenths: 124/10 − 67/10 = 57/10 = 5 7/10."],
              "5 7/10 units", ncert=["3.2.finger", "3.2.convert_tenths"]),
           WE("A Celestial Pearl Danio is 2 4/10 cm long and a Philippine Goby is 9/10 cm long. What is the "
              "difference in their lengths?",
              ["Write both in tenths: 2 4/10 is 24/10, and the goby is 9/10.",
               "24/10 − 9/10 = 15/10.",
               "15 tenths is 1 unit and 5 tenths, so the difference is 1 5/10 cm.",
               "Compare with your finger, which is about 6 to 8 cm long: the Danio is about 2 1/2 cm and the Goby "
               "less than 1 cm, so both fish are much shorter than a finger."],
              "1 5/10 cm", ncert=["3.2.fish"])],
       key_terms=["difference"], misconceptions=["M_BORROW_ONE"], minutes=10),
     A("T3.C3", "Patterns in tenths", "Analyze",
       "Students find the constant change in a sequence of numbers written in units and tenths and extend the "
       "sequence by four terms.",
       textbook=["Observe the given sequences of numbers. Identify the change after each term and extend the "
                 "pattern: (a) 4, 4 3/10, 4 6/10, ___ (b) 8 2/10, 8 7/10, 9 2/10, ___ (c) 7 6/10, 8 7/10, ___ (d) 5 "
                 "7/10, 5 3/10, ___ (e) 13 5/10, 13, 12 5/10, ___ (f) 11 5/10, 10 4/10, 9 3/10, ___ (four blanks "
                 "after each)."],
       teach=["Predict first: in 4, 4 3/10, 4 6/10, how much is added each time?",
              "Subtract each term from the next to find the change. If the terms get smaller, the change is a "
              "subtraction.",
              "Keep the change and extend the pattern, regrouping 10 tenths into a unit as you go."],
       examples=[
           WE("Find the change and write the next four terms: (a) 4, 4 3/10, 4 6/10 and (b) 8 2/10, 8 7/10, "
              "9 2/10. Then do (c) 7 6/10, 8 7/10 (d) 5 7/10, 5 3/10 (e) 13 5/10, 13, 12 5/10 (f) 11 5/10, "
              "10 4/10, 9 3/10 in the same way.",
              ["(a) 4 3/10 − 4 = 3/10, so add 3/10 each time: 4 9/10, 5 2/10, 5 5/10, 5 8/10.",
               "(b) 8 7/10 − 8 2/10 = 5/10, so add 5/10 each time: 9 7/10, 10 2/10, 10 7/10, 11 2/10.",
               "(c) 8 7/10 − 7 6/10 = 1 1/10, so add 1 1/10 each time: 9 8/10, 10 9/10, 12, 13 1/10.",
               "(d) 5 3/10 is 4/10 less than 5 7/10, so subtract 4/10 each time: 4 9/10, 4 5/10, 4 1/10, 3 7/10.",
               "(e) 13 is 5/10 less than 13 5/10, so subtract 5/10 each time: 12, 11 5/10, 11, 10 5/10.",
               "(f) 10 4/10 is 1 1/10 less than 11 5/10, so subtract 1 1/10 each time: 8 2/10, 7 1/10, 6, 4 9/10."],
              "(a) 4 9/10, 5 2/10, 5 5/10, 5 8/10 (b) 9 7/10, 10 2/10, 10 7/10, 11 2/10 (c) 9 8/10, 10 9/10, 12, "
              "13 1/10 (d) 4 9/10, 4 5/10, 4 1/10, 3 7/10 (e) 12, 11 5/10, 11, 10 5/10 (f) 8 2/10, 7 1/10, 6, "
              "4 9/10", ncert=["3.2.seq"])],
       key_terms=["pattern"], misconceptions=["M_BORROW_ONE"], minutes=10),
     DOER("T3.C4", "Practice: add and subtract tenths", None, "Apply",
          "Students add and subtract lengths written in units and tenths and extend patterns of tenths.",
          ["Add the units and the tenths separately; 10 tenths make 1 unit.",
           "If there are too few tenths, break 1 unit into 10 tenths.",
           "To find the change in a pattern, subtract a term from the term after it."])]))

# ============================== T4 The hundredth part ========================================================
TOPICS.append(TOPIC(
    "T4", "M1", "The Hundredth Part", ["3.3"], "Apply",
    "Students split each tenth into 10 equal parts to get hundredths, read lengths as units, tenths and "
    "hundredths in several equivalent ways, and pick the longest and shortest of a group of lengths.",
    "A tenth split into 10 equal parts gives hundredths: there are 100 hundredths in a unit and 10 hundredths in "
    "a tenth.",
    [A("T4.C1", "Splitting a tenth into ten parts", "Understand",
       "Students explain that splitting each tenth into 10 equal parts gives 100 equal parts in a unit, each a "
       "hundredth, and read a length as units, tenths and hundredths.",
       textbook=["3.3 A Hundredth Part",
                 "The length of a sheet of paper was 8 9/10 units, which can also be said as 8 units and 9 "
                 "one-tenths. It is folded in half along its length. What is its length now?",
                 "We can say that its length is between 4 4/10 units and 4 5/10 units. But we cannot state its "
                 "exact measurement, since there are no markings. Earlier, we split a unit into 10 one-tenths to "
                 "measure smaller lengths. We can do something similar and split each one-tenth into 10 parts.",
                 "What is the length of this smaller part? How many such smaller parts make a unit length?",
                 "As shown in the figure below, each one-tenth has 10 smaller parts, and there are 10 one-tenths in "
                 "a unit; therefore, there will be 100 smaller parts in a unit. Therefore, one part's length will be "
                 "1/100 of a unit.",
                 "Returning to our question, what is the length of the folded paper? We can see that it ends at 4 "
                 "4/10 5/100, read as 4 units and 4 one-tenths and 5 one-hundredths.",
                 "Math Talk: How many one-hundredths make one-tenth? Can we also say that the length is 4 units and "
                 "45 one-hundredths?"],
       teach=["Predict first: half of 8 9/10 is more than 4 4/10 but less than 4 5/10. Which mark can name it?",
              "No mark does, so each tenth is split again into 10 equal parts. There are 10 tenths in a unit, so "
              "there are 10 × 10 = 100 small parts in a unit.",
              "Each small part is 1/100 of a unit, called one-hundredth. 10 hundredths make 1 tenth."],
       examples=[
           WE("A paper strip 8 9/10 units long is folded in half. Its new length ends between 4 4/10 and 4 5/10. "
              "Split each tenth into 10 parts: what is one small part, and where does the folded strip end? Can "
              "the length also be said as 4 units and 45 hundredths?",
              ["Each tenth has 10 smaller parts and a unit has 10 tenths, so a unit has 10 × 10 = 100 smaller parts.",
               "One part is 1/100 of a unit.",
               "The folded strip ends 5 parts after the 4 4/10 mark, so it is 4 units and 4 tenths and 5 "
               "hundredths.",
               "10 hundredths make 1 tenth, so 4 tenths is 40 hundredths, and 40 + 5 = 45 hundredths.",
               "So yes, the length is also 4 units and 45 hundredths, that is 4 45/100."],
              "4 4/10 5/100, which is also 4 45/100 units", ncert=["3.3.paper", "3.3.hundredth", "3.3.mathtalk"])],
       key_terms=["hundredth"], misconceptions=["M_BIGGER_DENOMINATOR", "M_PART_AS_UNIT"], minutes=10),
     A("T4.C2", "Reading lengths in hundredths", "Apply",
       "Students read a length shown on a scale as units, tenths and hundredths, as units and hundredths, and as a "
       "count of hundredths, and say it in words.",
       textbook=["Observe the figure below. Notice the markings and the corresponding lengths written in the boxes "
                 "when measured from 0. Fill the lengths in the empty boxes.",
                 "The length of the wire in the first picture is given in three different ways. Can you see how "
                 "they denote the same length? 1 1/10 4/100 is one and one-tenth and four-hundredths. 1 14/100 is "
                 "one and fourteen-hundredths. 114/100 is one hundred and fourteen-hundredths.",
                 "For the lengths shown below write the measurements and read out the measures in words."],
       teach=["Predict first: a wire ends 4 small parts after 1 1/10. How many hundredths long is it in all?",
              "1 1/10 is 1 unit and 10 hundredths, and 4 more hundredths make 14 hundredths: 1 14/100. All in "
              "hundredths, 100 + 14 = 114, so 114/100.",
              "A mark that is 20 hundredths from 0 is the same as 2 tenths."],
       examples=[
           WE("A wire ends 4 small parts after the 1 1/10 mark. Write its length in three ways.",
              ["1 unit, 1 tenth and 4 hundredths is 1 1/10 4/100.",
               "1 tenth is 10 hundredths, so 10 + 4 = 14 hundredths: 1 14/100.",
               "1 unit is 100 hundredths, so 100 + 14 = 114 hundredths: 114/100."],
              "1 1/10 4/100 = 1 14/100 = 114/100 units", ncert=["3.3.wire"]),
           WE("Marks on a wire, measured from 0, are 1 part, 2 tenths, 20 parts, 55 parts, 99 parts, 130 parts, "
              "155 parts, 174 parts, 202 parts and 240 parts from 0, where each part is one hundredth. Write each "
              "length as a fraction of a unit.",
              ["1 part is 1/100.",
               "2 tenths is 2/10, which is 20/100, the same as the mark 20 parts.",
               "55 parts is 55/100 and 99 parts is 99/100.",
               "130 parts is 130/100, which is 1 30/100 or 1 3/10.",
               "155 parts is 155/100, which is 1 55/100.",
               "174 parts is 174/100, which is 1 74/100.",
               "202 parts is 202/100, which is 2 2/100.",
               "240 parts is 240/100, which is 2 40/100 or 2 4/10."],
              "1/100, 2/10, 20/100, 55/100, 99/100, 130/100, 155/100, 174/100, 202/100, 240/100",
              ncert=["3.3.wire_boxes"]),
           WE("Four rulers show lengths in hundredths: one reaches 37 parts after the 5 mark, another 3 parts after "
              "the 15 mark, another 52 parts after the 7 mark and the last 80 parts after the 9 mark. Write each "
              "measurement and read it in words.",
              ["37 parts after 5: 5 37/100, read 'five and thirty-seven hundredths'.",
               "3 parts after 15: 15 3/100, read 'fifteen and three hundredths'.",
               "52 parts after 7: 7 52/100, read 'seven and fifty-two hundredths'.",
               "80 parts after 9: 9 80/100, read 'nine and eighty hundredths'."],
              "5 37/100, 15 3/100, 7 52/100, 9 80/100", ncert=["3.3.read_lengths"])],
       key_terms=["hundredths"], misconceptions=["M_PART_AS_UNIT"], minutes=10),
     A("T4.C3", "The longest and the shortest", "Analyze",
       "Students compare lengths written with tenths and hundredths, pick the longest and shortest of a group by "
       "writing every length in hundredths, and mark them on a scale.",
       textbook=["In each group, identify the longest and the shortest lengths. Mark each length on the scale. (a) "
                 "3/10, 3/100, 33/100 (b) 3 1/10, 30/10, 1 3/10 (c) 45/100, 54/100, 5/10, 4/10 (d) 3 6/10, 3 "
                 "6/100, 3 6/10 6/100 (e) 8/100, 2/100, 9/100, 1 8/100 (f) 7 3/10 5/100, 7 5/10, 7 41/100 (g) 6 "
                 "5/10 15/100, 5 87/100, 5 7/100"],
       teach=["Predict first: which is longer, 3/10 or 33/100?",
              "Write every length as a count of hundredths, or as units and hundredths, so they can be compared.",
              "3 tenths is 30 hundredths, so 3/10 = 30/100."],
       examples=[
           WE("In each group find the longest and shortest length: (a) 3/10, 3/100, 33/100 (b) 3 1/10, 30/10, 1 "
              "3/10 (c) 45/100, 54/100, 5/10, 4/10 (d) 3 6/10, 3 6/100, 3 6/10 6/100 (e) 8/100, 2/100, 9/100, 1 "
              "8/100 (f) 7 3/10 5/100, 7 5/10, 7 41/100 (g) 6 5/10 15/100, 5 87/100, 5 7/100.",
              ["(a) In hundredths: 30, 3 and 33. Longest 33/100, shortest 3/100.",
               "(b) In tenths: 31, 30 and 13. Longest 3 1/10, shortest 1 3/10.",
               "(c) In hundredths: 45, 54, 50 and 40. Longest 54/100, shortest 4/10.",
               "(d) 3 60/100, 3 6/100 and 3 66/100. Longest 3 6/10 6/100, shortest 3 6/100.",
               "(e) 8, 2, 9 and 108 hundredths. Longest 1 8/100, shortest 2/100.",
               "(f) 7 35/100, 7 50/100 and 7 41/100. Longest 7 5/10, shortest 7 3/10 5/100.",
               "(g) 6 65/100 (as 6 5/10 15/100), 5 87/100 and 5 7/100. Longest 6 5/10 15/100, shortest 5 7/100."],
              "(a) 33/100, 3/100 (b) 3 1/10, 1 3/10 (c) 54/100, 4/10 (d) 3 6/10 6/100, 3 6/100 (e) 1 8/100, "
              "2/100 (f) 7 5/10, 7 3/10 5/100 (g) 6 5/10 15/100, 5 7/100", ncert=["3.3.longest"])],
       key_terms=["longest", "shortest"], misconceptions=["M_BIGGER_DENOMINATOR"], minutes=10),
     DOER("T4.C4", "Practice: read and compare lengths in hundredths", "hundredth_cell_zoom_grid", "Apply",
          "Students split a tenth into hundredths, read lengths as units, tenths and hundredths, and compare them.",
          ["10 hundredths make 1 tenth, and 100 hundredths make 1 unit.",
           "A length can be written as units, tenths and hundredths, as units and hundredths, or as a count of "
           "hundredths.",
           "To compare, write all the lengths in hundredths."])]))

# ============================== T5 Adding and subtracting hundredths ========================================
TOPICS.append(TOPIC(
    "T5", "M1", "Adding and Subtracting Hundredths", ["3.3"], "Apply",
    "Students add and subtract lengths in units, tenths and hundredths by regrouping 10 hundredths as 1 tenth and "
    "10 tenths as 1 unit, in the same way as with whole numbers.",
    "Adding and subtracting tenths and hundredths works place by place, exactly as for whole numbers: carry ten "
    "up, or break one down.",
    [A("T5.C1", "Adding with tenths and hundredths", "Apply",
       "Students add lengths in units, tenths and hundredths by adding place by place and carrying, by converting "
       "to hundredths, and compare the methods with the addition of whole numbers.",
       textbook=["What will be the sum of 15 3/10 4/100 and 2 6/10 8/100? This can be solved in different ways. "
                 "Some are shown below.",
                 "Method 1: (15 + 2) + (3/10 + 6/10) + (4/100 + 8/100) = 17 + 9/10 + 12/100 = 17 + 9/10 + 1/10 + "
                 "2/100 = 17 + 10/10 + 2/100 = 18 2/100. 10 hundredths is the same as 1 tenth.",
                 "Method 2: written as a column, the tenths add to 9 and the hundredths add to 12, which is 1 tenth "
                 "and 2 hundredths, so 10 tenths, which is 1 unit, and 2 hundredths: 18 2/100.",
                 "Math Talk: Are both these methods different? Observe the addition done below for 483 + 268. Do "
                 "you see any similarities between the methods shown above? (400 + 80 + 3) + (200 + 60 + 8) = (400 "
                 "+ 200) + (80 + 60) + (3 + 8) = 600 + 140 + 11 = 600 + 150 + 1 = 700 + 50 + 1 = 751.",
                 "One can also find the sum 15 3/10 4/100 + 2 6/10 8/100 by converting to hundredths, as follows. "
                 "(c) (15 + 2) + (34/100 + 68/100) = 17 + 102/100 = 17 + 1 + 2/100 = 18 2/100. (d) 1534/100 + "
                 "268/100 = 1802/100 = 1800/100 + 2/100 = 18 2/100.",
                 "100 hundredths is same as 1 unit. 15 is the same as 1500 hundredths and 2 is the same as 200 "
                 "hundredths."],
       teach=["Predict first: 15 3/10 4/100 plus 2 6/10 8/100. Will the hundredths together reach 10?",
              "Add hundredths to hundredths, tenths to tenths and units to units. When 10 hundredths appear, "
              "regroup them as 1 tenth.",
              "This is the same carrying we do for 483 + 268, with places worth 10 times each other.",
              "Or convert both to hundredths, add the counts, and write the result back in units."],
       examples=[
           WE("Add 15 3/10 4/100 and 2 6/10 8/100 by adding place by place, and compare with the addition 483 + "
              "268.",
              ["Units: 15 + 2 = 17. Tenths: 3 + 6 = 9. Hundredths: 4 + 8 = 12.",
               "12 hundredths is 1 tenth and 2 hundredths, so the tenths become 9 + 1 = 10 tenths.",
               "10 tenths is 1 unit, so the units become 17 + 1 = 18, leaving 2 hundredths: 18 2/100.",
               "In 483 + 268 the ones add to 11, so one ten is carried; the tens add to 150, so one hundred is "
               "carried. It is the same carrying, with a different set of places."],
              "18 2/100", ncert=["3.3.add", "3.3.add_mathtalk"]),
           WE("Add 15 3/10 4/100 and 2 6/10 8/100 again, this time by converting both to hundredths.",
              ["15 3/10 4/100 is 1500 + 30 + 4 = 1534 hundredths, so it is 1534/100.",
               "2 6/10 8/100 is 200 + 60 + 8 = 268 hundredths, so it is 268/100.",
               "1534/100 + 268/100 = 1802/100.",
               "1802/100 = 1800/100 + 2/100 = 18 + 2/100 = 18 2/100."],
              "18 2/100", ncert=["3.3.add_hundredths"])],
       key_terms=["carry"], misconceptions=["M_ADD_DENOMINATORS"], minutes=10),
     A("T5.C2", "Subtracting with tenths and hundredths", "Apply",
       "Students subtract lengths in units, tenths and hundredths, breaking a unit or a tenth where there are too "
       "few, and compare the method with subtracting whole numbers.",
       textbook=["What is the difference: 25 9/10 − 6 4/10 7/100? One way to solve this is as follows: there are "
                 "not enough hundredths, so 25 9/10 is written as 25 8/10 10/100, and then 25 8/10 10/100 − 6 4/10 "
                 "7/100 = 19 4/10 3/100.",
                 "Math Talk: Solve this by converting to hundredths.",
                 "What is the difference 15 3/10 4/100 − 2 6/10 8/100? One way to solve this is as follows: 15 3/10 "
                 "4/100 becomes 15 2/10 14/100 and then 14 12/10 14/100, and 14 12/10 14/100 − 2 6/10 8/100 = 12 "
                 "6/10 6/100.",
                 "Math Talk: Observe the subtraction done below for 653 − 268. Do you see any similarities with the "
                 "methods shown above? (600 + 50 + 3) − (200 + 60 + 8) = (600 − 200) + (50 − 60) + (3 − 8) = (600 − "
                 "200) + (40 − 60) + (13 − 8) = (600 − 200) + (40 − 60) + 5 = (500 − 200) + (140 − 60) + 5 = 300 + "
                 "80 + 5 = 385."],
       teach=["Predict first: 25 9/10 take away 6 4/10 7/100. There are no hundredths on top. Where can they come "
              "from?",
              "Break 1 tenth into 10 hundredths. Then subtract hundredths, tenths and units in turn.",
              "When both the tenths and the hundredths are too small, break a unit into tenths first, then a tenth "
              "into hundredths."],
       examples=[
           WE("Find 25 9/10 − 6 4/10 7/100, then check it by converting both numbers to hundredths.",
              ["There are no hundredths in 25 9/10 and 7 must be taken away, so break 1 tenth into 10 hundredths.",
               "25 9/10 becomes 25 8/10 10/100.",
               "Hundredths: 10 − 7 = 3. Tenths: 8 − 4 = 4. Units: 25 − 6 = 19. So the answer is 19 4/10 3/100.",
               "Check in hundredths: 2590 − 647 = 1943, and 1943/100 = 19 43/100, which is 19 4/10 3/100."],
              "19 4/10 3/100", ncert=["3.3.sub", "3.3.sub_hund"]),
           WE("Find 15 3/10 4/100 − 2 6/10 8/100, and compare the steps with 653 − 268.",
              ["Hundredths: 4 is less than 8, so break 1 tenth: 15 3/10 4/100 becomes 15 2/10 14/100.",
               "Tenths: 2 is less than 6, so break 1 unit into 10 tenths: 15 2/10 14/100 becomes 14 12/10 14/100.",
               "Hundredths: 14 − 8 = 6. Tenths: 12 − 6 = 6. Units: 14 − 2 = 12. So the answer is 12 6/10 6/100.",
               "In 653 − 268 the ones are too few, so a ten is broken into ones, and then a hundred into tens. "
               "It is the same breaking down, one place at a time."],
              "12 6/10 6/100", ncert=["3.3.sub2", "3.3.sub_mathtalk"])],
       key_terms=["break"], misconceptions=["M_BORROW_ONE"], minutes=10),
     DOER("T5.C3", "Pull it together and do it: sums and differences with tenths and hundredths",
          "carry_and_break_bench", "Apply",
          "Students find sums and differences of lengths written in units, tenths and hundredths, carrying and "
          "breaking at each place.",
          ["Always start from the hundredths, then tenths, then units.",
           "10 hundredths carry to 1 tenth and 10 tenths carry to 1 unit; break the other way when subtracting.",
           "Check a subtraction by adding the answer back."],
          items=[
              FIO("3.3.FiO", "Figure it Out (hundredths), the set of six sums and differences",
                  "Find the sums and differences: (a) 3/10 + 3 4/100 (b) 9 5/10 7/100 + 2 1/10 3/100 (c) 15 6/10 "
                  "4/100 + 14 3/10 6/100 (d) 7 7/100 − 4 4/100 (e) 8 6/100 − 5 3/100 (f) 12 6/10 2/100 − 9/10 "
                  "9/100",
                  ["(a) 3/10 is 30/100, so 30/100 + 3 4/100 = 3 34/100.",
                   "(b) Units: 9 + 2 = 11. Tenths: 5 + 1 = 6. Hundredths: 7 + 3 = 10, which is 1 tenth, so the "
                   "tenths are 7: 11 7/10.",
                   "(c) Units: 15 + 14 = 29. Tenths: 6 + 3 = 9. Hundredths: 4 + 6 = 10, which carries 1 tenth, so "
                   "the tenths are 10, which carries 1 unit: 30.",
                   "(d) Hundredths: 7 − 4 = 3. Tenths: 0. Units: 7 − 4 = 3. So 3 3/100.",
                   "(e) Hundredths: 6 − 3 = 3. Units: 8 − 5 = 3. So 3 3/100.",
                   "(f) 12 6/10 2/100 has 2 hundredths, and 9 must be taken away: break 1 tenth to get 12 5/10 "
                   "12/100. Hundredths: 12 − 9 = 3. Tenths: 5 is less than 9, so break 1 unit: 11 15/10 12/100, "
                   "15 − 9 = 6. Units: 11 − 0 = 11. So 11 6/10 3/100, which is 11 63/100."],
                  "(a) 3 34/100 (b) 11 7/10 (c) 30 (d) 3 3/100 (e) 3 3/100 (f) 11 63/100")])]))
