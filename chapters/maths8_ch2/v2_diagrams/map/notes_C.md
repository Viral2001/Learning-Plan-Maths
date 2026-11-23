# Notes, chunk C (Class 8 Ch 2 "Power Play", plan cbse_eng_maths8_ch2_v35)

Result: 30 items (18 units). required 5, optional 1, none 24. Validator `--chunk C`: errors 0, warnings 0.

| Item | Decision | Diagram |
|---|---|---|
| M4.S20.T20.C91 worked example | required | power line of 4 + the 3 expressions (M4.S20.T20.C91.IMG2; IMG1 is the kept teaching image) |
| M4.S21.T21.C96 question | required | power line of 7 + the 8 expressions (IMG1) |
| M4.S21.T21.C97 solution | required | same, with the 8 results in ANSWER green (IMG1, derived_from C96.IMG1) |
| M5.S23.T23.C108 question | required | blank Sun-Saturn line (IMG1) |
| M5.S23.T23.C109 solution | required | same line in 10 equal parts, Earth at tick 1 (IMG1, derived_from C108.IMG1) |
| M6.S25.T25.C123 worked example | optional (not added) | the book's Earth-ladder-Moon sketch would help |
| all other 24 items | none | text / LaTeX |

Aspect ratios: the two power-line figures are tall (12 and 11 rows with stacked fractions), so they are 4:3 (canvas 12 x 9 units); the Sun-Saturn line is a long strip drawn on a 16:9 canvas. All coordinates in the specs are in canvas units (origin at the centre).

## 1. Judgement calls

- **C91 (worked example, power line of 4): required.** The example says "Use the power line of 4"; the values of 4^8 ... 4^-2 live only in that line, so it is treated exactly like the power line for 7 (C96). The diagram is the GIVEN state: the line plus the three expressions of the LP question (as the book prints the power line for 7 with its expressions beside it). The book's own picture of the line of 4 also carries curved arrows and two merging brackets (a teaching figure that shows the answer 4^5); those are not drawn. The book's right bracket reads `16384 x 1/16`, the LP reads `16384 / 16`; same value, the LP is followed. P11-number_line-1 is mapped to this item (the teaching image M4.S20.T20.C91.IMG1 is not linked).
- **C97 (solution of power line of 7): no arrows.** The book's printed answer picture has none. The LP `s_figure` hint speaks of arrows from each expression to the power it lands on; not drawn, because 7^-6 (the last result) lies below the end of the line (7^-4) and an arrow would have nowhere to land. One picture carries all eight results even though the LP card has two card ids (IMG1, IMG2): a pair gets one solution diagram.
- **Number style in the power-line figures.** No commas anywhere (823543, 2401 x 49, 16807, 117649, ...), as in the LP text and on the line itself. The book prints Indian commas in the expressions (2,401; 16,807; 8,23,543; 1,17,649) but plain digits on the line. The 8 expressions are reproduced from the book's picture, not as instructions.
- **C108 / C109 (Earth on the Sun-Saturn line).** Question figure = only what the book prints: the line with `Sun` and `Saturn` ticks (no values, no Earth). Solution figure = the book's printed answer: the line in 10 equal parts, `Earth` at the first tick (nearest tick to the true ratio 1.496e11 / 1.4335e12 = 0.104). The added ticks and the Earth label are ANSWER green (added by the solution); the given ticks and labels stay INK.
- **P33-number_line-1** is the question's number line reprinted in the answers part, so it is accounted as `none:SAME_AS_QUESTION_DIAGRAM` (the printed answer picture itself is P34-number_line-1, mapped to the C109 solution).
- **P14-illustration-1** (painted Sun, Saturn, Uranus strip, no labels or numbers) is `none:DECORATIVE_ONLY`; the question is answered from the printed distances.
- **P29-expression_pair-1 and -2** (handwritten Tremendous in Ten expressions): `none:TEXT_SUFFICIENT`. The same expressions are in the LP question text; the red/blue colour only says who wrote it. So C114 is none/none.
- **Concept-image accounting (nothing is linked):** P15-illustration-1 -> M6.S25.T25.C120.IMG1; P18-schematic-1 and P18-expression_braces-1 -> M6.S25.T25.C123.IMG1.
- **C120 (Tulabhara): none.** The book picture is two scene illustrations (Roxie and Estu in a balance pan against jaggery / wheat) with no numbers; the numbers are assumptions given in the text.
- **C121, C122: none.** The book prints no figure for the coin question; the padayatra crowd strip on p.17 is scene art.
- **Figures not claimed, deliberately.** (a) P11-table-2 (the green box of the three general forms on book p.29 / pdf p.11) sits in section 2.3 above the "Power Lines" heading and belongs to the Zero and Negative Exponents topics (chunk B); if no chunk claims it, the merged check will say so. (b) The two banknote photographs at the top of pdf p.26 (Hungarian 1 milliard pengo, Zimbabwe 100 trillion dollars), the dinosaur comic on p.14, the padayatra crowd strip and the ladder-to-the-Moon scene on p.17: photographs or pure scene art that no item of this chunk works on; the inventory rules skip them, so no `NEW-` entries were made.

### Borderline
- **C91 required** (the LP steps already give 65536 = 4^8 etc., so a careful student could follow from text; kept required because the example is explicitly "use the power line" and for consistency with C96). Alternative: none / TEXT_SUFFICIENT.
- **C94 question: none** although the power line of 4 (pdf p.11) is on the previous page. The question text carries 16384, 1024, 4^2 and 4^-2 and never says "use the line". Alternative: required (DATA_IN_FIGURE).
- **C123 worked example: optional** (not added): the Earth-ladder-Moon sketch with "20 cm" and "3,84,400 km" would help but the text gives both numbers; the two growth expressions (20 + 20 + ..., 0.001 x 2 x 2 ...) can be LaTeX.
- **C106 question: none**: the three large-number facts are plain text in the book; they are missing from the LP text (see below), which does not change the decision.
- **Tall figures at 4:3**: if the builder wants every card strictly 16:9, the power-line figures will be letterboxed.

## 2. LP text issues

- **M5.S23.T23.C106** (question; also C107 steps refer to it): the question says "write the three large-number facts in scientific notation" but never states the facts. Suggested sentence: "The Sun is 30,00,00,00,00,00,00,00,00,000 m from the centre of the Milky Way; our galaxy has 1,00,00,00,00,000 stars; the Earth has a mass of 59,76,00,00,00,00,00,00,00,00,00,000 kg." (zeros checked: 3 x 10^20, 1 x 10^11, 5.976 x 10^24, as the LP solution says).
- **M5.S23.T23.C108** (question): it never says the Earth is to be marked on the number line with the Sun and Saturn ends. Suggested sentence: "On the number line below, with the Sun at one end and Saturn at the 1.4335 x 10^12 m mark, show where the Earth (1.496 x 10^11 m from the Sun) sits."
- **M4.S19.T19.C89, M5.S24.T24.C116, M5.S24.T24.C118** (book numbers): the LP calls them "Figure it Out, Q1", "Figure it Out, Q1", "Figure it Out, Q2"; in the book they are Q3, Q6 and Q12 (ncert_refs FiO2.q3, FiO2.q6, FiO2.q12 are right). The LP numbering restarts in each topic.
- **M4.S21.T21.C95** (answer_tex): "$4^2$ is $4^4$, which is $256$, times $4^{-2}$" is correct but reads awkwardly. Suggested: "$4^2$ is $4^4 = 256$ times larger than $4^{-2}$."
- **M5.S22.T22.C100**: ncert_refs lists `2.4.comic` but neither the question nor the steps use the dinosaur comic. Harmless.
- Checked and correct (recomputed): C90 (all nine products equal 2^18, 2^48 x 3^8, 2^-25), C91 (all three = 1024 = 4^5), C95 (16384/1024 = 16, 4^2 / 4^-2 = 256), C97 (eight results), C105, C107, C109 (0.104), C111 (4, 4, 6, 10), C113, C115, C117, C119, C121 (11250), C122 (16 days, 3066000 km, 76.65), C123 (1922000000 steps = 192 crore 20 lakh), C126 (200 = 2 x 10^2).

## 3. Book doubts

- pdf p.27 Q12: the option labels are printed "(ii) 20^9, (ii) 10^11, (iii) 10^10 ..." (the first (ii) should be (i)); the LP relabels it (i). The book's printed answer says only (vi); the LP rightly says (v) is equally correct.
- pdf p.33 printed answer for the power line of 7: the equations show 49^3 = 7^6 and 1/343 x 1/343 = 7^-6, both right; no print slip found. The line itself ends at 7^-4, so 7^-6 is only a result, not a tick.
- pdf p.14 number line: the inventory said the Saturn tick is about 6/7 along the line; measured on the page picture it is at 0.9 (the line runs about one tenth of the Sun-Saturn length past Saturn, the same as the printed answer picture). Corrected in the figure_inventory description.
- pdf p.34 printed answer: Earth is drawn at tick 1 of 10 (0.1) while the exact ratio is 0.104; kept as drawn.
- pdf p.35 printed answer for Figure it Out Q3 (book numbering) (ii)/(iii): the book lists `2^40 x 2^8 x 3^8`, `2^40 x 6^8`, `4^-12 x 2^-1`; all are valid products but differ from the LP samples (also valid). Not a diagram.
- pdf p.33 printed answer (172 = 1 x 10^2 + 7 +10^1 + 2 x 10^0) has a slip ("7 +10^1" for "7 x 10^1"); the item in this plan (5642, 561.903) is not affected.
