# Notes, chunk B (Class 7 Ch 11 "Finding Common Ground", plan cbse_eng_maths7_ch11_v30)

Result: 15 units, 28 items. Required 2 (both solutions) / optional 0 / none 26. Validator: errors 0, warnings 0.
Output: `map/out_B.json`. Figures claimed: P08-factorisation_match-1, P08-factorisation_match-2 (items), P09-illustration-1 (none:DECORATIVE_ONLY).

## 1. Judgement calls

1. **Example 4 and Example 5 solutions are REQUIRED (M1.S18.T18.C57.IMG1, M1.S18.T18.C59.IMG1).** This is the one real call in the chunk.
   - The book (p.8) prints each worked answer as a picture: the two factorisations aligned one under the other, the minimum-count common subparts boxed, then the HCF line. B2 says a printed answer that is a picture makes the solution required, and the boxes carry the meaning (which 2 and which 3, or which 3 and which two 5s, are shared).
   - The earlier author's `s_figure` hint describes the same picture for both.
   - Against it: a plain factorisation and a minimum-count step could also be written in LaTeX. If the user wants these two dropped to `none`, change them to `drop_image` with `LATEX_ARITHMETIC`; nothing else in the chunk depends on them.
   - Question side of both is `none`: the question gives only the two numbers, and the book's picture is the answer, so a question figure would leak it. `derived_from` is therefore null.
   - Spec details: the book's red/green digits and blue boxes are replaced by house tokens (digits INK, boxes FOCUS, result line ANSWER). The result line "HCF = 2 × 3 = 6" / "HCF = 3 × 5 × 5 = 75" is kept because the book prints it in the picture and the LP solution's last step uses the same words. Example 4 uses a connected step-shaped outline for the two 3s (row 1 factor 2, row 2 factor 4), as in the book. Example 5 uses a shared five-column grid so the three tall boxes (columns 2, 3, 4) line up.
2. **Why Examples 6 and 7 (LCM) and the Figure it Out answers are `none`, although Examples 4 and 5 are required.** The book prints no picture for them. The sibling rule is about the same kind of answer in the same question set; the reason is stated in each item. The Venn and stacks pictures for Examples 6 and 7 exist only as teaching images and are never linked.
3. **M1.S17.T17.C54 (worked example, HCF of 36, 60 and 84): `none`.** The book has no figure here (p.8 says only that a similar method can be followed), and this example is the plan's own. A three-row aligned figure with the minimum counts boxed would only make it nicer, so it is not marked optional either. Teaching image C55 shows it as three panels.
4. **Toran, gajak and idli-vada solutions: `none` (LATEX_ARITHMETIC).** Each is two plain lists of multiples and their first shared value. Two aligned rulers would only make them nicer, the book prints no such picture, and the three items get the same decision. The toran `s_figure` hint (two rows of strips meeting at 24 and 48) is therefore not followed; teaching image C64 covers it.
5. **P09-illustration-1** (boys laying cloth strips): the base entry was unsure whether it carries data. I checked the page picture: no lengths, counts or labels, and the 6 cm and 8 cm are in the question text. Decoration. The question side of the toran question is `none` with DECORATIVE_ONLY.
6. **M3.S27.T27.C88 (worked example, HCFs of consecutive numbers): `none`.** The book prints no figure (Figure it Out 3.3 Q1, Math Talk). The number line with arcs is already teaching image C88.IMG1 (kept, never linked).
7. **M3.S28 patterns:** Q1 is open-ended (find pairs, describe them in words), Q2 is algebra in symbols. Neither needs a picture. The book's picture on p.12 (the talking numbers 18 and 6) is decoration and gives no data.

## 2. Things in the LP that look off (none blocks a diagram)

- **M1.S18.T18.C56 (Example 4 question):** the LP question adds "using the minimum count of each common prime", which is not in the book ("Find the HCF of 30 and 72"). The book also states both factorisations before asking the example, while the LP question does not give them, so the factorisations appear only in the solution. Not a figure issue.
- **M2.S23.T23.C74 (gajak):** the LP says "free gajak every 7 days". The book says the shop gives gajak every Monday and today is a Monday, which is why the multiples of 7 appear. Same arithmetic, but the weekday context is lost.
- **M2.S23.T23.C76 / C77 (idli-vada):** the question text does not label the four pairs (a) to (d), but the answers do ("(a): 12; (b): 77" and "(c): 210; (d): 165"). A student cannot tell which letter is which pair.
- **M3.S27.T27.C88 (worked example):** it covers book Figure it Out 3.3 Q1 parts (a), (b), (d) and 12 and 13, but is written as a "find the HCF" example, not as the book's "make a general statement" question. Fine as a teaching example.
- **M3.S28.T28.C90:** "Find three more pairs" where the book says "Find more such number pairs". Harmless.
- All arithmetic in the chunk was re-checked: every factorisation multiplies back, and every HCF and LCM is right (Examples 4 to 7; Figure it Out 3.1 Q1 (a) to (e) = 12, 3, 6, 100, 100; Q2 HCF 72; Figure it Out 3.2 Q1 = 360, 108, 1365, 1110; gajak 70; idli-vada 12, 77, 210, 165; 3.3 pairs). No LP solution contradicts the book.

## 3. Where the book is unclear

- This pdf has no printed-solutions section, so no printed answer other than the Example 4 and Example 5 pictures was available; every other decision rests on the LP solution text.
- Pictures on the chapter pages in my chunk that carry no data and are not in the base inventory, not added: the gajak photograph (p.9, already noted by the inventory agent), and the talking-numbers art 18 and 6 (p.12). Both would be `none:DECORATIVE_ONLY` if the merge wants them listed.
- No picture on pp.10 to 13 carries mathematical content; I checked all four page images.
