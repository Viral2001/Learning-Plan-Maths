# -*- coding: utf-8 -*-
"""Topics T1 to T4: the chapter opening and similar change (M1), ratios, proportion and the missing term (M2).
Book pp 159 to 167."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Which copies look right? ================================================
TOPICS.append(TOPIC(
    "T1", "M1", "Which Copies Look Right?", ["Chapter opening"], "Understand",
    "",
    "One picture resized into five copies: three look like the original and two look stretched or squashed, even "
    "though every copy is a rectangle. What did the good copies keep?",
    [A("T1.C1", "One picture, five sizes", "Understand",
       "",
       textbook=["We are all familiar with digital images. We often change the size and orientation of these images "
                 "to suit our needs. Observe the set of images below.",
                 "We can see that all the images are of different sizes.",
                 "Which images look similar and which ones look different?",
                 "Images (A, C, and D) look similar, even though they have different sizes.",
                 "Do images B and E look like the other three images?",
                 "No, they are slightly distorted. The tiger appears elongated in B, and compressed and fatter in E!"],
       teach=["Predict first: a tiger photo is resized into five copies. Which copies will still look like the real "
              "tiger, and which will look odd?",
              "Three copies look right even though their sizes are different; one looks stretched and one looks "
              "squashed.",
              "All five copies are rectangles, so being a rectangle is not what keeps the shape.",
              "Keep this question open: what did the good copies keep that the odd copies lost?"],
       ncert=["7.1.images"], key_terms=["similar", "resize"], video_focus=["HOOK"], minutes=4,
       enrichment=True)],
    topic_type="framing"))

# ============================== T2 Same factor, same shape =================================================
TOPICS.append(TOPIC(
    "T2", "M1", "Same Factor, Same Shape", ["7.1"], "Analyze",
    "Students compare the widths and heights of resized pictures, decide whether both changed by the same factor "
    "(multiplication) or by the same amount (subtraction), and call a change that keeps the shape proportional.",
    "Pictures look similar when their width and height change by the same factor. Changing both by the same amount "
    "does not keep the shape. Changes by the same factor are called proportional.",
    [A("T2.C1", "Same factor or same difference?", "Analyze",
       "Students compare image A with images C and B, find that C halves both sides while B takes 20 mm off both "
       "sides, and explain why only C looks similar to A.",
       textbook=["You may notice that images A, C, and D are rectangular, but E is square. Maybe that is why E looks "
                 "different. But B is also a rectangle! Why does it look different from the other rectangular images?",
                 "Can we observe any pattern to answer this question? Perhaps by measuring the rectangles?",
                 "Image A: width 60 mm, height 40 mm. Image B: width 40 mm, height 20 mm. Image C: width 30 mm, height "
                 "20 mm. Image D: width 90 mm, height 60 mm. Image E: width 60 mm, height 60 mm.",
                 "What makes images A, C, and D appear similar, and B and E different?",
                 "When we compare image A with C, we notice that the width of C is half that of A. The height is also "
                 "half of A. Both the width and height have changed by the same factor (through multiplication), 1/2 "
                 "in this case. Since the widths and heights have changed by the same factor, the images look similar.",
                 "When we compare image A with image B, we notice that the width of B is 20 millimetre (mm) less than "
                 "that of A. The height too is 20 mm less than the height of A. Even though the difference (through "
                 "subtraction) is the same, the images look different. Have the width and height changed by the same "
                 "factor? The height of B is half the height of A. But the width of B is not half the width of A. "
                 "Since the width and height have not changed by the same factor, the images look different."],
       teach=["Predict first: image B is 20 mm narrower and 20 mm shorter than image A. Should it look like A?",
              "Measure: A is 60 mm by 40 mm, B is 40 mm by 20 mm, C is 30 mm by 20 mm.",
              "From A to C, both sides are multiplied by 1/2, the same factor, so C keeps the shape.",
              "From A to B, both sides lose 20 mm, the same difference, but the height is halved while the width is "
              "not, so B looks stretched."],
       examples=[
           WE("Image A is 60 mm wide and 40 mm high. Image C is 30 mm by 20 mm and image B is 40 mm by 20 mm. Which "
              "of B and C changed both sides by the same factor?",
              ["A to C: 60 ÷ 2 = 30 and 40 ÷ 2 = 20, so both sides are multiplied by 1/2.",
               "A to B: 60 − 20 = 40 and 40 − 20 = 20, so both sides lose the same 20 mm.",
               "But for B the height factor is 20 ÷ 40 = 1/2, while the width factor is 40 ÷ 60 = 2/3.",
               "The factors are different, so B is stretched; C used one factor, so it keeps the shape."],
              "C changed both sides by the factor 1/2, so it looks similar to A; B did not",
              ncert=["7.1.why", "7.1.factor_ac", "7.1.diff_ab"])],
       key_terms=["factor", "difference", "width", "height"], misconceptions=["M_ADD_SAME"], minutes=8),
     A("T2.C2", "Checking the factor, and the word proportional", "Apply",
       "Students find the factors that take image A's width and height to image D's, check whether they match, and "
       "use the word proportional for changes by the same factor.",
       textbook=["Can you check by what factors the width and height of image D change as compared to image A? Are "
                 "the factors the same?",
                 "Images A, C, and D look similar because their widths and heights have changed by the same factor. "
                 "We say that the changes to their widths and heights are proportional.",
                 "Note to the Teacher: In all these activities, encourage students to reason why their drawings are "
                 "proportional."],
       teach=["Predict first: image D is 90 mm by 60 mm. Is it A made bigger, or A stretched?",
              "Divide new by old for each side: if both give the same number, the change used one factor.",
              "Image E is 60 mm by 60 mm: its width factor and height factor differ, so E is squashed.",
              "When both measurements change by the same factor, we say the changes are proportional."],
       examples=[
           WE("Image A is 60 mm by 40 mm. Image D is 90 mm by 60 mm and image E is 60 mm by 60 mm. Which of them "
              "changed proportionally?",
              ["D: width factor 90 ÷ 60 = 3/2 and height factor 60 ÷ 40 = 3/2.",
               "The two factors are the same, so D is A enlarged by 3/2.",
               "E: width factor 60 ÷ 60 = 1 but height factor 60 ÷ 40 = 3/2.",
               "The factors differ, so E is not proportional to A."],
              "D is proportional to A (factor 3/2 on both sides); E is not",
              ncert=["7.1.factor_ad", "7.1.proportional"])],
       ncert=["7.4.note_drawings"],
       key_terms=["proportional", "factor of change"], misconceptions=["M_ADD_SAME"], minutes=8),
     DOER("T2.C3", "Practice: resize a picture without stretching it", "scale_stretcher", "Apply",
          "Students resize rectangles and figures by choosing a factor for each side, see that only equal factors "
          "keep the shape, and check rectangles and body drawings by comparing ratios.",
          ["A resized picture keeps its shape only when width and height change by the same factor.",
           "Taking the same amount off both sides does not keep the shape.",
           "Changes by the same factor are proportional."],
          items=[
              FIO("FiO1.q4", "Figure it Out (ratios and proportions, question 4)",
                  "Look at the five rectangles A, B, C, D and E. Which rectangles are similar to each other? You can "
                  "verify this by measuring the width and height using a scale and comparing their ratios.",
                  ["Measure the width and the height of each rectangle with a scale.",
                   "Write width : height for each rectangle.",
                   "Reduce each ratio to its simplest form by dividing both terms by their HCF.",
                   "Rectangles whose simplest forms are the same are similar; the others are not."],
                  "Rectangles with the same width to height ratio in simplest form are similar"),
              FIO("FiO1.q5", "Figure it Out (ratios and proportions, question 5)",
                  "Look at the given rectangle. Can you draw a smaller rectangle and a bigger rectangle with the same "
                  "width to height ratio in your notebooks? Compare your rectangles with your classmates' drawings. "
                  "Are all of them the same? If they are different from yours, can you think why? Are they wrong?",
                  ["Measure the rectangle and write width : height, for example 6 cm : 4 cm, which is 3 : 2.",
                   "For a smaller one, multiply both sides by one factor less than 1: 6 × 1/2 = 3 and 4 × 1/2 = 2.",
                   "For a bigger one, multiply both sides by one factor more than 1: 6 × 2 = 12 and 4 × 2 = 8.",
                   "Classmates may use other factors, so the sizes differ, but every drawing with ratio 3 : 2 is "
                   "correct."],
                  "Yes; drawings of different sizes are all correct as long as their width to height ratio is the same"),
              FIO("FiO1.q7", "Figure it Out (ratios and proportions, question 7)",
                  "Let us draw some human figures. Measure your friend's body: the lengths of their head, torso, arms "
                  "and legs. Write the ratios head : torso, torso : arms and torso : legs. Now draw a figure with "
                  "head, torso, arms and legs in equivalent ratios. Does the drawing look more realistic if the "
                  "ratios are proportional? Why? Why not?",
                  ["Measure the four lengths, for example head 20 cm, torso 60 cm, arms 60 cm, legs 80 cm.",
                   "Write the ratios: head : torso is 20 : 60, which is 1 : 3; torso : legs is 60 : 80, which is "
                   "3 : 4.",
                   "Choose one factor for the drawing, for example 1/10: 20 × 1/10 = 2 cm for the head and "
                   "60 × 1/10 = 6 cm for the torso.",
                   "Scaling every length by the same factor keeps the ratios, so the figure looks realistic."],
                  "Yes; when every length is scaled by the same factor, the ratios stay the same and the figure "
                  "looks realistic")])],
    key_terms=["factor of change", "proportional", "similar"]))

# ============================== T3 Ratios and their simplest form ===========================================
TOPICS.append(TOPIC(
    "T3", "M2", "Ratios and Their Simplest Form", ["7.2", "7.3", "7.4"], "Apply",
    "Students write ratios a : b and read them as 'for every a units, b units', reduce ratios to their simplest form "
    "by dividing by the HCF, decide whether two ratios are in proportion (a : b :: c : d), and compare mixtures such "
    "as filter coffee by their ratios.",
    "A ratio a : b says for every a units of the first quantity there are b units of the second. Dividing both terms "
    "by their HCF gives the simplest form. Two ratios with the same simplest form are in proportion, written "
    "a : b :: c : d. Mixtures with the same ratio taste the same.",
    [A("T3.C1", "A ratio compares two quantities", "Understand",
       "Students write the width to height ratios of the pictures, name the terms of a ratio, read a : b as 'for "
       "every a units there are b units', and multiply both terms by one factor.",
       textbook=["We use the notion of a ratio to represent such proportional relationships in mathematics.",
                 "We can say that the ratio of width to height of image A is 60 : 40.",
                 "The numbers 60 and 40 are called the terms of the ratio.",
                 "The ratio of width to height of image C is 30 : 20, and that of image D is 90 : 60.",
                 "In a ratio of the form a : b, we can say that for every 'a' units of the first quantity, there are "
                 "'b' units of the second quantity.",
                 "So, in image A, we can say that for every 60 mm of width, there are 40 mm of height.",
                 "We can say that the ratios of width to height of images A, C, and D are proportional because the "
                 "terms of these ratios change by the same factor. Let us see how.",
                 "Image A: 60 : 40. Multiplying both the terms by 1/2, we get 60 × 1/2 : 40 × 1/2, which is 30 : 20, "
                 "the ratio of width to height in image C."],
       teach=["Predict first: does the ratio 60 : 40 say the same thing as 40 : 60?",
              "A ratio a : b compares two quantities in order: for every a units of the first there are b units of "
              "the second. The numbers a and b are its terms.",
              "Image A has width to height 60 : 40: for every 60 mm of width there are 40 mm of height.",
              "Multiplying both terms by the same factor gives a proportional ratio: 60 : 40 becomes 30 : 20."],
       examples=[
           WE("Write the width to height ratio of image A (60 mm by 40 mm) and say what it means. Then multiply both "
              "terms by 1/2 and say which image you get.",
              ["Width to height of image A is 60 : 40, with terms 60 and 40.",
               "It means for every 60 mm of width there are 40 mm of height.",
               "Multiply both terms by 1/2: 60 × 1/2 = 30 and 40 × 1/2 = 20.",
               "The new ratio is 30 : 20, which is image C."],
              "60 : 40, for every 60 mm of width there are 40 mm of height; halving both terms gives 30 : 20, image C",
              ncert=["7.2.ratio", "7.2.meaning", "7.2.half"])],
       key_terms=["ratio", "term of a ratio"], misconceptions=["M_RATIO_ORDER"], minutes=8),
     A("T3.C2", "Simplest form and proportion", "Apply",
       "Students reduce ratios to their simplest form by dividing both terms by the HCF and use the simplest forms to "
       "decide whether two ratios are in proportion, writing a : b :: c : d.",
       textbook=["By what factor should we multiply the ratio 60 : 40 (image A) to get 90 : 60 (image D)?",
                 "A more systematic way to compare whether the ratios are proportional is to reduce them to their "
                 "simplest form and see if these simplest forms are the same.",
                 "We can reduce ratios to their simplest form by dividing the terms by their HCF.",
                 "In image A, the terms are 60 and 40. What is the HCF of 60 and 40? It is 20. Dividing the terms by "
                 "20, we get the ratio of image A to be 3 : 2 in its simplest form.",
                 "The ratio of image D is 90 : 60. Dividing both terms by 30 (HCF of 90 and 60), we get the simplest "
                 "form to be 3 : 2. So the ratios of images A and D are proportional as well.",
                 "What is the simplest form of the ratios of images B and E?",
                 "The ratio of image B is 40 : 20; in its simplest form, it is 2 : 1.",
                 "The ratio of image E is 60 : 60; in its simplest form, it is 1 : 1.",
                 "These ratios are not the same as 3 : 2. So, we can say that the ratios of width to height of images "
                 "B and E are not proportional to the ratios of images A, C, and D.",
                 "When two ratios are the same in their simplest forms, we say that the ratios are in proportion, or "
                 "that the ratios are proportional. We use the '::' symbol to indicate that they are proportional.",
                 "So a : b :: c : d indicates that the ratios a : b and c : d are proportional.",
                 "Thus, 60 : 40 :: 30 : 20 and 60 : 40 :: 90 : 60."],
       teach=["Predict first: are 60 : 40 and 90 : 60 the same comparison? Guess before you divide.",
              "Divide both terms by their HCF to get the simplest form.",
              "60 : 40 and 90 : 60 both reduce to 3 : 2, so they are in proportion: 60 : 40 :: 90 : 60.",
              "B gives 2 : 1 and E gives 1 : 1, not 3 : 2, so B and E are not in proportion with A."],
       examples=[
           WE("Reduce the width to height ratios of images A (60 : 40), D (90 : 60), B (40 : 20) and E (60 : 60) to "
              "simplest form. Which are in proportion with A?",
              ["A: the HCF of 60 and 40 is 20; 60 ÷ 20 = 3 and 40 ÷ 20 = 2, so 3 : 2.",
               "D: the HCF of 90 and 60 is 30; 90 ÷ 30 = 3 and 60 ÷ 30 = 2, so 3 : 2.",
               "B: the HCF is 20; 40 ÷ 20 = 2 and 20 ÷ 20 = 1, so 2 : 1.",
               "E: the HCF is 60; 60 ÷ 60 = 1, so 1 : 1.",
               "Only D matches 3 : 2, so 60 : 40 :: 90 : 60. The factor from A to D is 90 ÷ 60 = 3/2."],
              "A and D are both 3 : 2, so 60 : 40 :: 90 : 60; B (2 : 1) and E (1 : 1) are not in proportion with A",
              ncert=["7.2.factor_d", "7.3.simplest", "7.3.b_e", "7.3.proportion"])],
       key_terms=["simplest form", "HCF", "proportion"], misconceptions=["M_ONE_TERM_SCALED"], minutes=9),
     A("T3.C2x", "Testing two ratios: 3 : 4 and 72 : 96", "Apply",
       "Students test whether 3 : 4 and 72 : 96 are proportional by reducing 72 : 96 to its simplest form.",
       textbook=["Are the ratios 3 : 4 and 72 : 96 proportional?",
                 "3 : 4 is already in its simplest form.",
                 "To find the simplest form of 72 : 96, we need to divide both terms by their HCF.",
                 "What is the HCF of 72 and 96?",
                 "The HCF of 72 and 96 is 24. Dividing both terms by 24, we get 3 : 4.",
                 "Since both ratios in their simplest form are the same, they are proportional."],
       teach=["Predict first: 72 : 96 has much bigger numbers. Can it still be the same comparison as 3 : 4?",
              "Reduce the bigger ratio and compare simplest forms."],
       examples=[
           WE("Are the ratios 3 : 4 and 72 : 96 proportional?",
              ["3 : 4 is already in simplest form, because the HCF of 3 and 4 is 1.",
               "The HCF of 72 and 96 is 24.",
               "72 ÷ 24 = 3 and 96 ÷ 24 = 4, so 72 : 96 reduces to 3 : 4.",
               "The simplest forms are the same, so 3 : 4 :: 72 : 96."],
              "Yes, 72 : 96 reduces to 3 : 4, so the ratios are proportional",
              ncert=["7.4.ex1"])],
       key_terms=["simplest form", "HCF"], minutes=5, thin=True),
     A("T3.C3", "Filter coffee: stronger or lighter?", "Analyze",
       "Students compare the decoction to milk ratios of regular, strong and light filter coffee and explain which "
       "mixture is stronger by comparing the ratios, not the amounts.",
       textbook=["Filter coffee is a beverage made by mixing coffee decoction with milk. Manjunath usually mixes 15 mL "
                 "of coffee decoction with 35 mL of milk to make one cup of filter coffee in his coffee shop.",
                 "In this case, we can say that the ratio of coffee decoction to milk is 15 : 35.",
                 "If customers want 'stronger' filter coffee, Manjunath mixes 20 mL of decoction with 30 mL of milk. "
                 "The ratio here is 20 : 30.",
                 "Why is this coffee stronger?",
                 "And when they want 'lighter' filter coffee, he mixes 10 mL of coffee and 40 mL of milk, making the "
                 "ratio 10 : 40.",
                 "Why is this coffee lighter?"],
       teach=["Predict first: all three cups hold 50 mL. Which cup tastes strongest, and how can you tell without "
              "tasting?",
              "Strength depends on decoction compared with milk, so compare the ratios in simplest form.",
              "Regular 15 : 35 is 3 : 7; strong 20 : 30 is 2 : 3; light 10 : 40 is 1 : 4.",
              "Compare decoction for each mL of milk: the bigger it is, the stronger the coffee."],
       examples=[
           WE("Regular filter coffee is 15 mL decoction to 35 mL milk, strong is 20 : 30 and light is 10 : 40. "
              "Explain why the strong one is stronger and the light one is lighter.",
              ["Simplest forms: 15 : 35 is 3 : 7, 20 : 30 is 2 : 3, 10 : 40 is 1 : 4.",
               "Decoction for each mL of milk, regular: 15 ÷ 35 = 3/7 ≈ 0.43.",
               "Strong: 20 ÷ 30 ≈ 0.67, which is more than 0.43, so more decoction for the same milk.",
               "Light: 10 ÷ 40 = 0.25, which is less than 0.43, so less decoction for the same milk."],
              "Strong coffee has more decoction for each mL of milk (2 : 3 against 3 : 7); light coffee has less "
              "(1 : 4)",
              ncert=["7.4.coffee", "7.4.coffee_strong", "7.4.coffee_light"])],
       key_terms=["mixture", "decoction", "ratio"], misconceptions=["M_RATIO_ORDER"], minutes=8),
     DOER("T3.C4", "Practice: same mixture or a different one?", "ratio_mixer", "Analyze",
          "Students mix two drinks in chosen ratios, see that drinks with the same simplest form taste the same, and "
          "sort ratios and statements of proportion as true or false.",
          ["A ratio a : b means for every a units of the first quantity there are b units of the second.",
           "Divide both terms by their HCF to get the simplest form.",
           "Two ratios are in proportion when their simplest forms are the same."],
          items=[
              FIO("7.4.coffee_table", "Try This (filter coffee table)",
                  "Manjunath mixes coffee decoction with milk in these amounts: 300 mL with 600 mL, 150 mL with "
                  "500 mL, 200 mL with 400 mL, 24 mL with 56 mL, and 100 mL with 300 mL. Regular coffee is 15 mL "
                  "decoction with 35 mL milk. Is each one regular, strong or light?",
                  ["Regular is 15 : 35, which is 3 : 7, and 15 ÷ 35 = 3/7 ≈ 0.43.",
                   "300 : 600 is 1 : 2 and 300 ÷ 600 = 0.5, more than 0.43, so strong.",
                   "150 : 500 is 3 : 10 and 150 ÷ 500 = 0.3, less than 0.43, so light.",
                   "200 : 400 is 1 : 2, so strong.",
                   "24 : 56 is 3 : 7, the same as regular, so regular.",
                   "100 : 300 is 1 : 3 and 100 ÷ 300 ≈ 0.33, less than 0.43, so light."],
                  "300 : 600 strong, 150 : 500 light, 200 : 400 strong, 24 : 56 regular, 100 : 300 light"),
              FIO("FiO1.q1", "Figure it Out (ratios and proportions, question 1)",
                  "Circle the following statements of proportion that are true. (i) 4 : 7 :: 12 : 21 "
                  "(ii) 8 : 3 :: 24 : 6 (iii) 7 : 12 :: 12 : 7 (iv) 21 : 6 :: 35 : 10 (v) 12 : 18 :: 28 : 12 "
                  "(vi) 24 : 8 :: 9 : 3",
                  ["Reduce each ratio to its simplest form and compare.",
                   "(i) 12 : 21 is 4 : 7, the same as 4 : 7, so true.",
                   "(ii) 24 : 6 is 4 : 1, but 8 : 3 is already in simplest form, so false.",
                   "(iii) 7 : 12 and 12 : 7 have their terms in a different order, so false.",
                   "(iv) 21 : 6 is 7 : 2 and 35 : 10 is 7 : 2, so true.",
                   "(v) 12 : 18 is 2 : 3 and 28 : 12 is 7 : 3, so false.",
                   "(vi) 24 : 8 is 3 : 1 and 9 : 3 is 3 : 1, so true."],
                  "(i), (iv) and (vi) are true"),
              FIO("FiO1.q6", "Figure it Out (ratios and proportions, question 6)",
                  "A long brick wall has patterns made using grey and coloured bricks, and each wall continues its "
                  "pattern throughout. In wall (a), one block of the pattern has 2, 3 and 4 grey bricks in its rows "
                  "and 3, 2 and 1 coloured bricks. In wall (b), one block has 16 grey bricks and 12 coloured bricks. "
                  "What is the ratio of grey bricks to coloured bricks? Give the ratios in simplest form.",
                  ["Wall (a): grey bricks in one block are 2 + 3 + 4 = 9.",
                   "Coloured bricks in one block are 3 + 2 + 1 = 6.",
                   "9 : 6 has HCF 3, so the simplest form is 3 : 2.",
                   "Wall (b): 16 : 12 has HCF 4, so the simplest form is 4 : 3.",
                   "The pattern repeats, so the whole wall has the same ratio as one block."],
                  "(a) 9 : 6, which is 3 : 2; (b) 16 : 12, which is 4 : 3"),
              FIO("FiO4.q1", "Figure it Out (unit conversions, question 1)",
                  "Anagh mixes 600 mL of orange juice with 900 mL of apple juice to make a fruit drink. Write the "
                  "ratio of orange juice to apple juice in its simplest form.",
                  ["Orange juice to apple juice is 600 : 900.",
                   "The HCF of 600 and 900 is 300.",
                   "600 ÷ 300 = 2 and 900 ÷ 300 = 3."],
                  "2 : 3")])],
    key_terms=["ratio", "simplest form", "proportion"]))

# ============================== T4 Finding a missing term ==================================================
TOPICS.append(TOPIC(
    "T4", "M2", "Finding a Missing Term", ["7.4"], "Apply",
    "Students find the factor of change from the given pair of terms, apply the same factor to the other term to "
    "fill in a missing term (including fractional factors), and use this to keep a recipe the same or to compare "
    "two jobs.",
    "To fill in a missing term, find the factor that takes one known term to its partner and multiply the other "
    "term by the same factor. The factor can be a fraction.",
    [A("T4.C1", "Scale both terms by one factor", "Apply",
       "Students fill in missing terms of ratios proportional to 14 : 21, finding a whole-number factor, a "
       "fractional factor and a factor that comes from dividing by the HCF.",
       textbook=["Fill in the missing numbers for the following ratios that are proportional to 14 : 21. "
                 "______ : 42, 6 : ______, 2 : ______",
                 "In the first ratio, we don't know the first term. But the second term is 42. It is 2 times the "
                 "second term of the ratio 14 : 21. So, the first term should also be 2 times 14 (the first term). "
                 "Hence the proportional ratio is 28 : 42.",
                 "For the second ratio, the first term is 6.",
                 "What factor should we multiply 14 by to get 6? Can it be an integer? Or should it be a fraction?",
                 "We can model this as 14y = 6. So, y = 6/14 = 3/7.",
                 "So, we need to multiply 21 (the second term of 14 : 21) also by the same factor 3/7.",
                 "21 × 3/7 is 9. So, the ratio is 6 : 9.",
                 "In the third ratio, the first term is 2.",
                 "We can see that when we divide 14 (the first term of 14 : 21) by 7 (HCF of 14 and 21) we get 2.",
                 "If we divide 21 also by 7, we get 3. So, the ratio is 2 : 3.",
                 "Note to the Teacher: Give more such examples that students can relate to and ask them to give "
                 "reasons why they think they are correct. Engaging with these problems and finding solutions "
                 "through a process of proportional reasoning should go along with learning procedures and methods "
                 "to solve the problems."],
       teach=["Predict first: can 14 : 21 become a ratio that starts with 6? The factor would have to be less than 1.",
              "Find the factor from the pair you know: new term ÷ old term.",
              "Multiply the other term by the same factor.",
              "The factor can be a fraction: 14 × 3/7 = 6, so 21 × 3/7 = 9."],
       examples=[
           WE("Fill in the missing terms so that each ratio is proportional to 14 : 21: ___ : 42, 6 : ___, 2 : ___.",
              ["___ : 42: the factor is 42 ÷ 21 = 2, and 14 × 2 = 28, so 28 : 42.",
               "6 : ___: the factor is 6 ÷ 14 = 3/7, and 21 × 3/7 = 9, so 6 : 9.",
               "2 : ___: the HCF of 14 and 21 is 7; 14 ÷ 7 = 2 and 21 ÷ 7 = 3, so 2 : 3."],
              "28 : 42, 6 : 9 and 2 : 3",
              ncert=["7.4.ex7"])],
       ncert=["7.4.note_relate"],
       key_terms=["factor of change", "missing term"], misconceptions=["M_FACTOR_INTEGER", "M_ONE_TERM_SCALED"],
       minutes=8),
     A("T4.C2", "Keeping a recipe the same: lemonade", "Apply",
       "Students model keeping lemonade equally sweet as a proportion 6 : 10 :: 18 : ?, find the factor of change "
       "and the missing number of spoons.",
       textbook=["Kesang wanted to make lemonade for a celebration. She made 6 glasses of lemonade in a vessel and "
                 "added 10 spoons of sugar to the drink. Her father expected more people to join the celebration. So "
                 "he asked her to make 18 more glasses of lemonade.",
                 "To make the lemonade with the same sweetness, how many spoons of sugar should she add?",
                 "To maintain the same sweetness, the ratio of the number of glasses of lemonade to the number of "
                 "spoons of sugar should be proportional. For 6 glasses of lemonade, she added 10 spoons of sugar.",
                 "The ratio of glasses of lemonade to spoons of sugar is 6 : 10. We can model this problem as "
                 "6 : 10 :: 18 : ?",
                 "We know that each term in the ratio must change by the same factor, for the ratios to be "
                 "proportional.",
                 "How can we find the factor of change in the ratio?",
                 "The first term has increased from 6 to 18. To find the factor of change, we can divide 18 by 6 to "
                 "get 3.",
                 "The second term should also change by the same factor. When 10 increases by a factor of 3, it "
                 "becomes 30. Thus, 6 : 10 :: 18 : 30.",
                 "So, she should use 30 spoons of sugar to make 18 glasses of lemonade with the same sweetness as "
                 "earlier."],
       teach=["Predict first: 6 glasses need 10 spoons of sugar. For 18 glasses, is it 22 spoons (add 12) or 30 "
              "spoons (times 3)?",
              "Same sweetness means the same ratio of glasses to spoons.",
              "Find the factor from glasses: 18 ÷ 6 = 3, then multiply the spoons by the same factor.",
              "Adding 12 to both terms would change the sweetness."],
       examples=[
           WE("Kesang uses 10 spoons of sugar for 6 glasses of lemonade. How many spoons does she need for 18 "
              "glasses in all with the same sweetness?",
              ["Glasses to spoons: 6 : 10 :: 18 : ?",
               "Factor of change for the glasses: 18 ÷ 6 = 3.",
               "Spoons change by the same factor: 10 × 3 = 30.",
               "So 6 : 10 :: 18 : 30."],
              "30 spoons of sugar",
              ncert=["7.4.ex2"])],
       key_terms=["factor of change", "same sweetness"], misconceptions=["M_ADD_SAME"], minutes=7),
     A("T4.C2x", "Equally strong walls", "Analyze",
       "Students compare the ratio of wall length to bags of cement for two walls and decide whether the walls are "
       "equally strong.",
       textbook=["Nitin and Hari were constructing a compound wall around their house. Nitin was building the longer "
                 "side, 60 ft in length, and Hari was building the shorter side, 40 ft in length. Nitin used 3 bags of "
                 "cement but Hari used only 2 bags of cement. Nitin was worried that the wall Hari built would not be "
                 "as strong as the wall he built because she used less cement. Is Nitin correct in his thinking?",
                 "In Nitin and Hari's case, we should compare the ratio of the length of the wall to the bags of "
                 "cement used by each of them and see whether they are proportional.",
                 "The ratio in Nitin's case is 60 : 3, i.e., 20 : 1 (in its simplest form).",
                 "The ratio in Hari's case is 40 : 2, i.e., 20 : 1 (in its simplest form).",
                 "Since both ratios are proportional, the walls are equally strong. Nitin should not worry!"],
       teach=["Predict first: Hari used fewer bags of cement. Is her wall weaker?",
              "Compare length to cement for each wall, not the bags alone."],
       examples=[
           WE("Nitin builds a 60 ft wall with 3 bags of cement and Hari builds a 40 ft wall with 2 bags. Are the "
              "walls equally strong?",
              ["Nitin: 60 : 3; 60 ÷ 3 = 20, so 20 : 1.",
               "Hari: 40 : 2; 40 ÷ 2 = 20, so 20 : 1.",
               "Both are 20 : 1, so 60 : 3 :: 40 : 2: each 20 ft of wall gets one bag."],
              "Yes, both walls use one bag for every 20 ft, so they are equally strong",
              ncert=["7.4.ex3"])],
       key_terms=["proportional", "compare"], minutes=5, thin=True),
     DOER("T4.C3", "Practice: fill in the missing term", "ratio_table", "Apply",
          "Students build columns of a ratio table by multiplying both terms by one factor, fill in missing terms, "
          "and write ratios proportional to a given ratio.",
          ["Find the factor from the known pair: new term ÷ old term.",
           "Multiply the other term by the same factor; the factor may be a fraction.",
           "Adding the same number to both terms does not give a proportional ratio."],
          items=[
              FIO("FiO1.q2", "Figure it Out (ratios and proportions, question 2)",
                  "Give 3 ratios that are proportional to 4 : 9.",
                  ["Multiply both terms by the same number.",
                   "By 2: 4 × 2 = 8 and 9 × 2 = 18, so 8 : 18.",
                   "By 3: 4 × 3 = 12 and 9 × 3 = 27, so 12 : 27.",
                   "By 4: 4 × 4 = 16 and 9 × 4 = 36, so 16 : 36."],
                  "For example 8 : 18, 12 : 27 and 16 : 36"),
              FIO("FiO1.q3", "Figure it Out (ratios and proportions, question 3)",
                  "Fill in the missing numbers for these ratios that are proportional to 18 : 24. 3 : ___, "
                  "12 : ___, 20 : ___, 27 : ___",
                  ["Simplest form first: the HCF of 18 and 24 is 6, so 18 : 24 is 3 : 4.",
                   "3 : ___ is 3 : 4.",
                   "12 : ___: 12 ÷ 3 = 4 and 4 × 4 = 16, so 12 : 16.",
                   "20 : ___: the second term is 20 × 4 ÷ 3 = 80/3, so 20 : 80/3.",
                   "27 : ___: 27 ÷ 3 = 9 and 9 × 4 = 36, so 27 : 36."],
                  "3 : 4, 12 : 16, 20 : 80/3 and 27 : 36"),
              FIO("7.4.ex4", "Example (teachers and students in your school)",
                  "In my school, there are 5 teachers and 170 students. The ratio of teachers to students in my "
                  "school is 5 : 170. Count the number of teachers and students in your school. What is the ratio of "
                  "teachers to students in your school? Is it proportional to the one in my school?",
                  ["Simplest form of 5 : 170: the HCF is 5, so it is 1 : 34.",
                   "Count your school, for example 12 teachers and 360 students: 12 : 360.",
                   "The HCF of 12 and 360 is 12, so 12 : 360 is 1 : 30.",
                   "1 : 30 is not 1 : 34, so the two ratios are not proportional; your school has fewer students for "
                   "each teacher."],
                  "5 : 170 is 1 : 34; your school's ratio is proportional only if it also reduces to 1 : 34"),
              FIO("7.4.ex5", "Example (blackboard rectangle)",
                  "Measure the width and height (to the nearest cm) of the blackboard in your classroom. What is the "
                  "ratio of width to height of the blackboard? Can you draw a rectangle in your notebook whose width "
                  "and height are proportional to the ratio of the blackboard? Compare the rectangle you have drawn "
                  "to those drawn by your classmates. Do they all look the same?",
                  ["Measure, for example, width 360 cm and height 120 cm: 360 : 120.",
                   "The HCF is 120, so the simplest form is 3 : 1.",
                   "Draw a rectangle 3 cm wide and 1 cm high, or 9 cm by 3 cm: any pair in the ratio 3 : 1.",
                   "Classmates' rectangles may be different sizes, but all with ratio 3 : 1 have the same shape."],
                  "The blackboard's ratio in simplest form, for example 3 : 1; every rectangle in that ratio has the "
                  "same shape though sizes differ")])],
    key_terms=["missing term", "factor of change", "ratio table"]))
