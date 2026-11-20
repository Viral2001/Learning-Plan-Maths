# -*- coding: utf-8 -*-
"""Tool write-ups (description field) for Fractions in Disguise. Keyed by tool media id."""
DESCRIPTIONS = {

"M1.S2.T2.C4.2D1": (
"The student looks at one square sheet of 100 tiles, 10 across and 10 down, with rounded corners so it reads like a sheet of postage stamps that can be torn into strips. "
"The fraction 3/4 is written large and stacked on the left. Under the sheet a counter reads '___ out of 100' and waits to be filled. "
"The AI runs this tool by setting the fraction, cutting the sheet and shading strips, and nothing on the screen is a button, so the student's work is to commit to a number before each move and say it aloud.\n\n"
"Before any cut, the student predicts how many of the 100 tiles would be red if 3/4 of the paint is red, and that guess stays on screen. "
"The AI then draws lines that cut the sheet into 4 equal strips of 25 tiles, each tabbed with its number of parts, and asks how many tiles one strip holds and how many three strips hold. "
"The student answers 25 and 75, three strips shade amber, the counter fills in 75 out of 100 and the tool writes = 75% in green beside the guess. "
"Then the sheet is cleared, 2/5 is written, and the roles swap: the student tells the AI how many equal parts to cut the sheet into. "
"The answer 5 gives 5 strips of 20 tiles, 2 strips shaded, 40 out of 100, so 40%. The sheet never changes between the two fractions, only the cutting does.\n\n"
"The last case is 1/3. Three strips are cut, 33 tiles shade fully, and the last tile is drawn hatched instead of shaded with a small tag 'and a bit'. "
"The counter stops at 33 and a bit, and the AI says that 1/3 is 33.33 percent because it never lands exactly on 100, which is fine. "
"If an answer is off, the hints come in order. First: what number do you multiply 4 by to reach 100? "
"Then the sheet is split into 5 strips and the student says what percent one strip is, which is 20. "
"If the student is still stuck, a worked example shows 7/20 scaled by 5 to 35/100, so 35%, and the student tries 9/25, which gives 36%. "
"Through predicting and answering on one unchanging sheet, the student learns that a percentage is the same fraction rebuilt as so many out of 100, and that multiplying the fraction by 100 is just a shortcut for that scaling."
),

"M2.S4.T4.C23.2D1": (
"A long bar runs nearly the full width of the screen, and most of it lies under a grey cloth with a wavy, hand-drawn edge. "
"Only the left stretch shows, in blue, labelled 92 km with a small tag 'this is 40%'. Below the bar is a row of empty dashed boxes waiting to be filled. "
"The AI moves everything and nothing is clickable, so the student estimates, works out the size of one block and says what they find aloud.\n\n"
"First the student says whether the whole trip from Delhi to Agra is more or less than 92 km, and then holds a number for how long it really is. "
"That guess is kept for the end. The AI cuts the bar into 5 equal blocks, and the visible 92 km turns out to lie on exactly 2 of them, because 40% is two fifths. "
"The AI asks how much one block is when 92 is shared between 2 blocks, and the student answers 46. "
"The dashed boxes then fill left to right as the count goes 46, 92, 138, 184, 230. "
"The cloth lifts slowly, which is the one slow, deliberate movement of the tool, and the whole bar reads 230 km with the remaining stretch of 138 km lit up in amber. "
"Last, the student's guess drops onto the bar as a small amber flag with the guessed number, so the gap between guess and truth is seen and not only stated.\n\n"
"A student who adds 40% of 92 to 92 and gets 128.8 km is taken back to the blocks: the 92 km fills only 2 of the 5 blocks, so the 40% belongs to the whole trip and not to the 92. "
"The hints come in order. First: if 40% is 92 km, what is 20%? Then: how many 20% pieces make 100%? "
"A retry follows on the same cloth with a book where 30% is 60 pages, so 140 pages are left. "
"Through estimating and then building up block by block, the student learns that a known part gives the size of one piece and the pieces build the whole, which is the reverse of taking a percentage of a known whole."
),

"M2.S4.T4.C24.2D1": (
"A tall, narrow glass tube fills the left two thirds of the screen, like the fundraising thermometer painted outside a school gate. "
"A bold line labelled TARGET, 100%, Rs 5000 crosses it only about two fifths of the way up, so a long stretch of empty tube is left above the line, with faint tick marks at 150%, 200% and 250%. "
"On the right a large figure shows the day's sales, and under it a percentage reading counts up as the liquid rises. "
"The AI pours the amounts and nothing is clickable, so the student reads the meter and says the percentages aloud.\n\n"
"On Day 1 Rs 2000 is poured and the blue liquid stops well short of the line. The student says what percent of the target that is, and 40% appears. "
"Day 2 pours Rs 3500, which is 70%, and Day 3 pours Rs 5000, where the liquid sits exactly on the line at 100%. "
"Day 4 pours Rs 6000, and the liquid does not stop at the line. It rises into the empty tube above and turns purple, which tells the student this is new territory. "
"The student says how much sticks out above the line, Rs 1000, and what part of 5000 that is, a fifth or 20%, so the whole reading is 100% plus 20%, which is 120%, or 6/5, or 1.2. "
"Then Rs 7800 and Rs 9550 are poured and the student gives the percentages alone, 156% and 191%.\n\n"
"After that the AI runs the meter backwards. It sets 150% and then 210%, the liquid rises to those marks, and the student works out the rupees before the figure counts up to check: Rs 7500 and Rs 10,500. "
"A wrong answer is first met with a hint: is 7800 more or less than the target, and by how much? "
"Then: 2800 out of 5000 is what percent, and add that to 100%. "
"A student who believes a percentage cannot pass 100 is answered by the picture itself, because the liquid has already passed the line. "
"Through reading the meter both ways, the student learns that 100% is the whole target and not the end of the scale, so a result that beats the target is more than 100%."
),

"M3.S6.T6.C50.2D1": (
"Two cardboard price tags with a string and a punched hole hang from a clothes rail at the top of the screen. "
"The left tag reads BEFORE, Rs 30, and the right tag reads AFTER, Rs 42, for 1 kg of tomatoes three years apart. "
"Below them lies a single measuring bar with a caption that always says in words which price is being measured against. "
"A small amber flag, '100% is here', clips to one tag at a time. The AI moves the flag and nothing is clickable, so the student chooses, tells and answers.\n\n"
"Before anything is drawn, the student chooses whether the price went up by 12%, 40% or 29%. "
"The AI clips the flag onto BEFORE, so the bar is as long as Rs 30, and attaches the extra Rs 12 as a separate stub on its end. "
"The student says what part of 30 the 12 is, two fifths, and the stub reads 40%. "
"Then the flag unclips, travels across and clips onto AFTER. The bar stretches to Rs 42, the stub keeps exactly the same size, and its reading changes to 28.6%. "
"The same Rs 12 gives a different answer only because the flag moved. "
"The AI asks which flag position the question 'increased from Rs 30' wants, and the student answers BEFORE.\n\n"
"The next case is a fall: theatre footfall going from 160 to 100. Because AFTER is smaller, the change is drawn as an orange notch cut out of the bar instead of a stub added to it. "
"The student says where the flag goes, on 160, and what the decrease is, 37.5%. "
"Last, a population p grows by 65%, drawn as a 100% bar with a 65% stub, and a Relabel toggle redraws the whole thing as one block labelled 165%, so 'increased by 65%' and '165% of the original' are seen to be the same object. "
"Hints come in order. First: what was the price before the change? That is your 100%. Then: the change is new minus old, so what percent of the old price is that? "
"A retry follows with a bus fare going from Rs 40 to Rs 50, which should give 25%. "
"The student learns that a change is always measured against where it started, and that moving the 100% moves the answer."
),

"M3.S8.T8.C59.2D1": (
"A shop counter is drawn in side view with a wall behind it. Across the wall runs a thick line labelled WHAT I PAID, 100%, Rs 300, at about mid height so there is room above and below it. "
"A ruler at the right has 0% at the line, marks going up at plus 10, 25 and 50 percent and down at minus 10 and minus 25 percent, and a pointer that shows the reading for the current stack of notes and coins on the counter. "
"The AI sets the line and the stack. Nothing is clickable, so the student does the thinking and says each percentage aloud.\n\n"
"The AI first stacks Rs 430, the price Kishanlal got for his sweater, and the stack rises above the line. The part above is green and tagged with its value. "
"The student says how much sticks up, Rs 130, and what that is compared with 300, and the pointer settles at 43.33%. "
"Then the line moves to Rs 253 for the wholesaler, who sold for Rs 300, and the student says where the line goes and what comes out: 18.58%. "
"For Raghu's old rice the line moves to Rs 350 and the stack is only Rs 300. The gap is drawn as a hollow orange hatched space tagged Rs 50, and the pointer drops below zero to a loss of about 14.3%.\n\n"
"Then comes the reverse. The line is hidden as a dashed question mark at an unknown height, and only a Rs 50 stack remains, tagged 'this is 125% of what I paid'. "
"The student works out what Shambhavi paid for a crayon box she sold for Rs 50 at a 25% profit: 125% is Rs 50, so 1% is 0.4 and 100% is Rs 40, and the line appears at Rs 40. "
"A side panel then shows the trap, taking 25% off Rs 50 to get Rs 37.50, with the answer struck through, because the profit was never measured from the selling price. "
"Hints come in order. First: who paid what first? That is the 100%. Then: is the selling price longer or shorter than the cost, and by how much as a part of the cost? "
"If still stuck, a worked example uses cost Rs 80 and selling price Rs 100, which is 25%, followed by a retry with cost Rs 120 and selling price Rs 150. "
"The student learns that profit and loss are one idea measured from the same line, the cost price."
),

"M4.S10.T10.C84.2D1": (
"Two glass savings jars stand side by side on a shelf, the left one labelled TAKEN OUT and the right one LEFT IN, both starting at the same coin level. "
"Below them are a table with columns Year, Start, Interest this year and End for each jar, and a graph of amount against years. "
"The student has the controls: principal from Rs 100 to Rs 1,00,000, rate from 1 to 20 percent, years from 1 to 30, a Next year button, a Run button, a Reset and a Growth or Decline switch. "
"The AI says one line, 'now go and break it', and then stays quiet.\n\n"
"The student begins with Rs 6000 at 10 percent and presses Next year. In the left jar the coin level never rises, because a handful of coins leaves each year and drops into a purse labelled 'Taken home so far', reaching Rs 1800 after 3 years, so Rs 7800 in all. "
"In the right jar each year's interest settles in amber on top of the blue coins, and the amber band is thicker every year, Rs 600, Rs 660, then Rs 726, with a dashed line marking last year's level and a small arrow beside each new interest value in the table, ending at Rs 7986. "
"On the graph the taken-out jar is a straight line and the left-in jar is a curve, and the wedge between them is shaded as what compounding gave you. "
"Both jars share one scale, so the comparison is fair.\n\n"
"Then the student explores freely. Run for 20 years. Compare 5 percent for 4 years with 10 percent for 2 years: both are 20 percent in simple interest, yet with the interest left in the 5 percent jar ends higher. "
"Watch where money doubles at 10 percent, in about 7 years with compounding against 10 without. "
"Try to make the two jars end up equal, and notice that the table agrees in year 1 and parts company from year 2. "
"The only nudge, if nothing surprises the student, is whether they tried a long time at a small rate.\n\n"
"In Decline mode there is one jar that shrinks and its coins fade out as they leave. A television worth Rs 21,000 falling 5 percent a year loses Rs 1050 in the first year and a little less, Rs 997.50, in the second. "
"The student learns that interest left in earns interest too, and that decline is the same idea in reverse."
),

"M4.S12.T12.C102.2D1": (
"A cake hangs at the top of the screen with a price tag reading Rs 200. Under it a blue price bar shows the full price with a scale from 0 to 100 and a bold label '100%, this is what the next coupon works on'. "
"At the right waits a small stack of torn paper coupons, 30% OFF, 20% OFF and 50% OFF. "
"The AI peels the coupons and nothing is clickable, so the student votes, predicts and answers aloud.\n\n"
"First the student restates the vote made earlier, Cakely with 30% plus 20% off, Cakify with 50% off, or the same, and predicts what Cakely's cake will cost. "
"The AI sticks on the 30% coupon: that part of the bar dissolves in orange and the price falls to Rs 140. "
"Then the key movement happens slowly. The 100% label and the whole scale slide down and re-attach to the shorter bar, renumbering themselves over its new length, while a faint ghost of the old, longer bar stays behind. "
"The student is asked what the 20% coupon takes 20% of, and answers Rs 140, not Rs 200. "
"The AI applies it, Rs 28 comes off, and the price is Rs 112. A second bar shows Cakify's single 50% coupon leaving Rs 100, so Cakify is cheaper.\n\n"
"Next the AI clears the cake and puts the coupons on the other way, 20% first and 30% second, and the price lands on Rs 112 again, so the order does not matter. "
"A line under everything collects the multipliers, times 0.7 then times 0.8, giving times 0.56: you pay 56% and save 44%, not 50%. "
"If an answer is off, the hints come in order. First: after the first discount what is the new price, and is the 20% taken from Rs 200 or from that? "
"Then: write both steps as multipliers, times 0.7 and then times 0.8. "
"A retry follows with 10% off and then another 10% off a Rs 500 bag, which should give Rs 405. "
"The student learns that percentages applied one after another multiply and do not add, because each one is taken from the price that has already shrunk."
),
}
