# Chunk E notes: topic M3.S12.T12 "Questions: Example" (units 65-73, 18 items)

Result: required 5 / optional 2 / none 11. Validator: errors 0, one warning (C116, see Borderline: the figure is not printed in the book).

| Unit | Concepts | Question side | Solution side |
|---|---|---|---|
| 65 Kishanlal's profit % (book Ex 4) | C105 / C106 | none | REQUIRED (bar, CP = 100%) |
| 66 Wholesaler and manufacturer | C107 / C108 | REQUIRED (sweater journey) | none |
| 67 Notebooks | C109 / C110 | none | none |
| 68 Crayons | C111 / C112 | none | optional (not added) |
| 69 Raghu's loss % (book Ex 5) | C113 / C114 | none | REQUIRED (bar) |
| 70 Damaged vase (book Ex 6) | C115 / C116 | none | REQUIRED (bar, borderline) |
| 71 Strawberries | C117 / C118 | none | optional (not added) |
| 72 Cooker | C119 / C120 | none | none |
| 73 Is the bill correct? | C121 / C122 | REQUIRED (receipt) | none |

Figures claimed (5): P16-flow_diagram-1 (concept image M3.S11.T11.C97.IMG1), NEW-P16-flow_diagram-1-q (item C107 question), P17-bar_model-1 (C106 solution), P17-bar_model-2 (C114 solution), P19-receipt-1 (C121 question). I checked all four base descriptions against page_16, page_17 and page_19 (zoomed on the receipt and the price tags): they are correct, no CORRECTED entries. P18-bar_model-1/2 (Manisha, teaching figures) are not claimed: no unit of this chunk uses them (chunk D's units 62/63 do). The clothes-shop "SALE 30%" picture on p.18 is decoration (not in the base inventory, skipped per Step 0).

Merge hint: P16, P17-bar_model-1, P17-bar_model-2 and P19-receipt-1 also sit in book sections of chunk D units (59 "Kishanlal's profit", 61 "Per kg?", 64 "A bill from home"). I claim the base ids for my items; if D also uses one of these figures for an item of its own, one of us needs a `NEW-<id>-<suffix>` entry. For P16 I claimed the base id as concept_image C97.IMG1 (the teaching use, same meaning D should give it) and a separate NEW- entry for my question item.

## 1. Judgement calls

- **C107 question, sweater journey: required.** The book's question ("Find the profit percentage of the wholesaler and the manufacturer") has no numbers; the cost and selling prices of the manufacturer (230 / 253) and the wholesaler (253 / 300) exist only in the p.16 picture, and the LP question text is just the title "Wholesaler and manufacturer". DATA_IN_FIGURE plus the tie-breaker (a careful student cannot attempt it from the text). The picture is also teaching image C97.IMG1, but v3 says a teaching image is never linked, so the item gets its own figure. I did not use the 'refer picture' exception (question optional): that exception is for a book answer that only points at a picture, and the book here has no printed answer and the question text carries no data. Figure = boxes and price tags only; the book's illustrations of workers, vans and shoppers are decoration and are left out. All three tags are drawn (the book gives all three), each tag under the arrow leaving the seller it belongs to.
- **C106 and C114 solutions (Examples 4 and 5): required.** The book prints a rough bar with each example as the worked solution (CP = 100%, the profit or loss beyond or inside it). v3 B2: a printed solution picture makes the solution side required; and the picture changes how correctly a student reads "which base": the LP steps "130 over the CP of 300" and "50 over the CP of 350" only say it in words. The question sides have no figure (the book question is text only; the card text of C105 even said "No diagram is needed"), so the solution figures draw the whole bar (derived_from null) with the answer percentage in ANSWER green.
- **Example 4 bar: the book's "?" is not drawn.** The book puts "?" under the 430 line (which would literally be 143.33%, the selling price as a percentage of the cost) while its answer 43.3% belongs to the 130 part. To keep a clean final state without adding a number that is in neither the LP nor the book, the 430 line has no bottom label and the 130 part gets its own ANSWER arrow "43.33%".
- **Example 5 bar: "300" added above the middle line.** The book leaves that line unlabelled above although 300 is in its text; the final-state figure needs it. 100% sits under the 350 line (the cost price is the base), as in the book.
- **Percentage numbers follow the LP.** Example 4: LP 43.33% (book prints 43.3%, one decimal). Example 5: LP 14.29% (book prints 14.28%, see "Book mistakes").
- **C108 (wholesaler / manufacturer solution): none.** Two fractions of numbers that are already on the question figure; the book prints no solution picture. (The LP video draws cost-price bars, but the video is not this job.) Not made optional-with-bars because Examples 4 and 5 have a printed bar and these do not.
- **C122 (bill solution): none.** The check is 9% of 450 twice and a sum; it adds nothing visual. Highlighting the tax lines would only make it nicer (optional at most, not needed).
- **C112 crayons and C118 strawberries solutions: optional, not added.** A bar (CP = 100%, SP = 125% or 88%) would help the reverse-percentage step, but the book prints none and does not ask the student to draw one. C98.IMG1 (a teaching image) already shows the crayon bar.
- **C110 notebooks and C120 cooker: none.** Plain arithmetic, no figure in the book.
- **Question sides of C105, C109, C111, C113, C115, C117, C119: none (TEXT_SUFFICIENT).** The book question of each is text with its numbers in words. The LP question texts are bare titles (see LP text issues): I did not change a decision for that.
- **C121 receipt aspect.** The receipt is a little taller than wide; the pipeline draws 16:9 cards, so the paper (760 x 900 px) is centred on a 1920x1080 card. Bulb logo of the book receipt left out (decorative); the stray full stop after "Price" in the book is not drawn. The receipt's arithmetic is correct (3 x 150 = 450; 9% of 450 = 40.50 twice; 450 + 81 = 531), so no correction needed.
- **Colour use.** House tokens only (book yellow/red replaced by MARK_FILL / INK). In C116 the values the solution works out (2173, 477, 82%) are ANSWER green and the given ones (2650, 18%, 0, 100%) INK; in C106 / C114 only the final percentage is ANSWER.

## Borderline

1. C107 question: required vs optional ('refer picture' exception). Chose required (reasons above).
2. C106 and C114 solutions: required vs none/optional (the bar restates numbers the LP text carries). Chose required per v3 B2 (printed solution picture) and user decision 4.
3. **C116 (vase) solution: required although the book prints no figure.** The book says right after Example 6: "Try making an estimate. Draw a rough diagram depicting the given situation", then shows two methods ("keep 82%" / "subtract 18%"). The answer to that prompt is a drawing (ANSWER_IS_FIGURE) and Examples 4 and 5 directly above have the same kind of bar printed (sibling consistency), so the solution draws that rough bar: buying price 2650 = 100%, loss 18% = 477, selling price 82% = 2173. All numbers are on book p.18 or in the LP solution. If the user would rather draw only what the book prints, flip C116 to optional (action drop_image) and delete its diagram; nothing else depends on it. This is the only required item with no inventory figure behind it (hence the validator warning).
4. C112 / C118 optional (not added) while C116 is required: the difference is the book's explicit "draw a rough diagram" prompt for the vase.
5. C121 solution none vs optional (circle the CGST / SGST lines): chose none.

## 2. Book mistakes (spec shows the corrected value)

- Example 5 (Raghu): the book prints the loss percentage as 14.28% (50/350 = 14.2857..., cut off instead of rounded). The LP says 14.29%, which is right. The base inventory keeps what the book prints (it does not print the percentage inside the picture); the spec, `visible_text` and `manim_description` use 14.29%, and `must_not_show` lists 14.28%.
- Example 4: the book prints 43.3% (rounded to one decimal; 130/300 = 43.33%). Not an error, but the spec uses the LP's 43.33%.

## 3. Places where the book itself is unclear

- Example 4 bar: the "?" under the 430 line (see Judgement calls).
- Shambhavi's notebooks: "200 page notebooks at ₹36 per book ... Find the selling price" means notebooks of 200 pages; it does not say "per notebook" (the LP answer is ₹43.20 per notebook, i.e. 36 x 1.2).
- "Profit margin of 20% / 25%" does not say with respect to what; the chapter's Figure it Out Q1 says "with respect to the cost", and the LP answers follow that.
- The sweater picture's tags are not labelled with whose prices they are; reading them as the seller to the left of each arrow fits the chain (each SP equals the next CP: 253, 300) and the LP's own q_figure text.
- Example 6: the book asks the student to draw a rough diagram but prints none.

## LP text issues (not changed, only listed)

Concept id, what is wrong or missing, suggested sentence.

- **M3.S12.T12.C105** question "Kishanlal's profit %": no data (cost 300, selling price 430). Suggest: "Kishanlal buys a sweater for ₹300 and sells it for ₹430. Find his percentage profit."
- **M3.S12.T12.C106** step "130 over the CP of 300.": does not say where 130 comes from. Suggest: "Profit = ₹430 − ₹300 = ₹130, and the cost price (₹300) is the 100%, so the profit is 130 over 300."
- **M3.S12.T12.C107** question "Wholesaler and manufacturer": no data; everything is in the picture. Suggest: "Use the prices in the picture. Find the profit percentage of the wholesaler and of the manufacturer." (the answer lists wholesaler first, then manufacturer: keep that order.)
- **M3.S12.T12.C108** steps "47 over 253; 23 over 230.": not said which is which or where 47 and 23 come from. Suggest: "Wholesaler: profit 300 − 253 = 47 over the CP 253. Manufacturer: profit 253 − 230 = 23 over the CP 230."
- **M3.S12.T12.C109** question "Notebooks": no data. Suggest: "Shambhavi buys 200-page notebooks at ₹36 each and sells them with a profit margin of 20%. Find the selling price of one notebook."
- **M3.S12.T12.C110** step "36 × 1.2.": Suggest: "20% profit on the cost: selling price = 36 × 1.2 = ₹43.20 per notebook."
- **M3.S12.T12.C111** question "Crayons": no data. Suggest: "Shambhavi sells crayon boxes at ₹50 each with a profit margin of 25% on the cost. At what price did she buy one box from the wholesaler?"
- **M3.S12.T12.C112** step "50 ÷ 1.25.": Suggest: "The selling price ₹50 is 125% of the cost price, so cost price = 50 ÷ 1.25 = ₹40."
- **M3.S12.T12.C113** question "Raghu's loss %": no data. Suggest: "Raghu bought rice at ₹35 per kg and sells 10 kg for ₹300. Find his percentage loss."
- **M3.S12.T12.C114** step "50 over the CP of 350." and the answer text: the step does not show 10 x 35 = 350 and 350 − 300 = 50; the answer carries a parenthetical "(the book shows 14.28%, cut off rather than rounded)" that a learner will read as part of the answer. Suggest: "Cost = 10 × ₹35 = ₹350; loss = ₹350 − ₹300 = ₹50; loss over the CP: 50 over 350." and move the book remark to a teacher note.
- **M3.S12.T12.C115** question "Damaged vase": no data. Suggest: "Shyamala bought a decorative vase for ₹2650. It is slightly damaged and she sells it at a loss of 18%. How much does she get? Try drawing a rough diagram first."
- **M3.S12.T12.C116** step "Keep 82% of 2650, or subtract 18% of it.": Suggest: "Two ways: 82% of 2650 = 0.82 × 2650 = 2173, or 2650 − (18% of 2650 = 477) = 2173."
- **M3.S12.T12.C117** question "Strawberries": no data. Suggest: "Snehal sells strawberries at ₹80 per kg and makes a 12% loss. What was the cost price per kg?"
- **M3.S12.T12.C119** question "Cooker": no data. Suggest: "A cooker with MRP ₹1800 is sold at a 35% discount. What is the selling price? If the cost price was ₹900, what is the percentage profit?"
- **M3.S12.T12.C120** step 2 "profit 270 over 900": does not show 1170 − 900 = 270. Suggest: "Step 2 base is the CP: profit = 1170 − 900 = 270, so 270 over 900."
- **M3.S12.T12.C121** question "Is the bill correct?": the bill exists only in the figure (that is why the figure is required); fine once the figure is added, but "Check if the calculations on the bill are correct." matches the book better.
- **Concept names and book numbers**: C105/C106 are named "Example 4" and C111/C112 also "Example 4"; C107/C108 "Example 2", C109/C110 "Example 3", C117/C118 "Example 7", C119/C120 "Example 8", C121/C122 "Example 9". In the book only Kishanlal (Ex 4), Raghu (Ex 5) and the vase (Ex 6) are numbered; the wholesaler/manufacturer, notebooks, crayons, strawberries, cooker and bill items are unnumbered "?" prompts, and the book's real Examples 7, 8 and 9 (the ₹6000 deposit, the total received, compounding) are later in the chapter (chunk F). The labels clash with those. Suggest names such as "Try this: wholesaler and manufacturer", "Try this: notebooks", "Try this: crayons", "Try this: strawberries", "Try this: cooker", "Try this: the bill".
