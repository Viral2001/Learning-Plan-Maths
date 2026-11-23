# Chunk C notes (Class 5 Ch 3 "Angles as Turns"): topics M3.S19.T19, M3.S20.T20, M3.S21.T21

Result: 12 items, required 7 / optional 2 / none 3. Validator: errors 0, warnings 0.

| Item | Decision | Media id |
|---|---|---|
| C73 worked example (arrow down to left) | optional (not added) | - |
| C74 worked example (Padma, West, 3 right angles anti-clockwise) | optional (not added) | - |
| C76 question (four creatures) | required | M3.S20.T20.C76.IMG1 |
| C77 solution (creatures, ticked) | required | M3.S20.T20.C77.IMG1 |
| C78 question (tap, lid, nut) | none | - |
| C79 solution (tap, lid, nut) | none | - |
| C80 question (Fun with Turns Q1, compass) | required | M3.S21.T21.C80.IMG1 |
| C81 solution (Fun with Turns Q1) | none (LATEX_TABLE) | - |
| C82 question (Padma Q2) | required | M3.S21.T21.C82.IMG1 |
| C83 solution (Padma Q2, half turn clockwise) | required | M3.S21.T21.C83.IMG1 |
| C84 question (Padma, other way) | required | M3.S21.T21.C84.IMG1 |
| C85 solution (Padma, half turn anti-clockwise) | required | M3.S21.T21.C85.IMG1 |

Base figures claimed: P09-creatures-3, P10-compass-1, P10-table-2 (none: LATEX_TABLE), P10-scene-3, plus four NEW- entries for further uses of the creatures and the street picture (C77, C83, C84, C85). The two clocks P09-clock-1 and P09-clock-2 (Let Us Do Q6 f and g) are not mine and are not claimed.

## (1) Judgement calls

- **Creatures (C76).** The base `unclear` note (facing read by eye) is settled: I enlarged page 9 and read the head ends. Ladybug left then up, snail down then left, bee left then down, ant up then left. This agrees with the LP `q_figure` and with the LP answer (a) clockwise, (b) clockwise, (c) anti-clockwise, (d) anti-clockwise: 9 to 12 and 6 to 9 are clockwise, 9 to 6 and 12 to 9 are against the clock.
- **Creatures: option boxes in the picture.** The book prints the caption (Clockwise/Anti-clockwise) under each panel. I draw it as two option boxes per panel, so the solution figure can tick the right one (the task is "Tick the direction"). The LP question text lists the same two words too; the picture only repeats the book's figure.
- **Creatures: letters.** (a) to (d) are drawn, because the LP answer text refers to the creatures by letter (decision 3).
- **Creatures solution (C77).** Required, not none: the answer is a ticked figure (ACTION_ON_FIGURE), derived from the question diagram. The C81 solution is none: its filled table is plain words (LATEX_TABLE), so the two are not siblings.
- **Padma street (C82, C84, C83, C85).** The book's picture is a cartoon street. A cartoon would be decorative clip-art and cannot be drawn faithfully, so the spec is a labelled plan view that keeps only what the question uses: Padma facing the toy shop, bookstall on her left, parking sign on her right, ice cream cart behind her. The guard beside the parking sign is left out: only the four places she can face are drawn. Labels follow the LP words (bookstall, parking sign, ice cream cart); the book's signs read BOOKSTORE, PARKING and Ice Cream.
- **Padma solutions.** One 180-degree arc (a half turn) in ANSWER green with a dot at the first quarter turn (parking sign side, or bookstall side) and the tag "half turn clockwise" or "half turn anti-clockwise". C83 and C85 are mirror images, so they get the same decision (sibling consistency).
- **C84 question (required).** The book prints "What other way can she turn to face the same place?" under the same street picture, so by the rule "the same book picture used by several items gets one diagram per item" it gets the same diagram as C82 (render_note says so). See Borderline.
- **Compass for Fun with Turns Q1 (C80).** The book prints the compass next to the table, and it is the only thing that fixes which direction a clockwise right angle leads to. I treat it as the question's given figure. The table itself is not drawn (plain table of words, the LP question text lists the seven rows), so the base figure P10-table-2 is `none:LATEX_TABLE`. The solution is none: the filled table is LaTeX, the compass would only repeat the question figure. I wrote the full LaTeX rows in `text_alternative` of C81.
- **Tap, lid, nut (C78, C79).** Both none. The book has no figure; the answer is a sentence with "your tap may differ". A drawn tap with one arrow would fix a viewing side and a result.
- **Decision 5 (teaching images).** C73 and C74 each keep one teaching image (IMG1). Neither was used as a reason: the two worked examples are optional because the book gives no figure and the text is complete, not because a teaching image exists. No REUSES_CONCEPT_IMAGE anywhere in this chunk.
- **Media ids.** All seven required items use IMG1 of their own concept (no kept images in C76 to C85, so IMG1 is free). The old card ids (for example C76.IMG1, C77.IMG1/IMG2) are being replaced; `lp_ids_dropped` is empty as the brief says.

## Borderline

- **C73 and C74 worked examples: optional.** The turn is a spatial idea (SPATIAL_GEOMETRY) and a figure (arrow down then left; compass with Padma facing West) would make it easier. But the book gives no figure, the LP question states both positions in words, and the steps give the clock numbers or the order West, South, East, North, so a careful student can solve it from the text. I applied the tie-breaker as written ("only makes it nicer" is optional). If the user wants a figure on every worked example of a teaching concept, flip these two to required: the specs would be an arrow before and after the quarter turn (C73) and a compass with Padma facing West (C74), no turning arrow.
- **C80 compass: required.** If the user thinks the clockwise order North, East, South, West is common knowledge, this is the item to drop (the LP solution states the order in its first step).
- **C84 question: required.** The answer (a half turn the other way) does not depend on the street at all, but the question points to "the same place" from the previous question and the book prints it under the picture. If dropped, C85's solution would stay required (draws the whole figure itself, derived_from null).
- **C79 tap, lid, nut solution: none.** The picture that would help is a tap, lid and nut with a curved arrow; not drawn because of the viewing-side problem above.

## (2) LP text issues

- **M3.S21.T21.C80 / C81 (row g):** the book prints no number before "right angles clockwise" in the last row (print slip), and the LP question has a blank "___". The LP answer uses a sample "if it is 3, North". Suggested sentence for the question: "(g): West, ___ right angles clockwise (the number is missing in the book; take 3 as an example), four 1/2 right angles anti-clockwise." No diagram of mine shows this row, so no value is corrected in a spec.
- **M3.S21.T21.C84 (question):** "the same place" is not named. Suggested sentence: "Padma is facing the toy shop and takes a half turn clockwise to face the ice cream cart. What other way can she turn to face the same place?" (it reveals the answer to the previous question, which the learner has just done).
- **M3.S21.T21.C82 and C84 (questions):** the LP question text does not say where the other places are; only the figure does. This is fine as long as the question diagram is shown; if the figure is ever dropped, add: "The bookstall is on her left, the parking sign on her right and the ice cream cart behind her."
- **M3.S20.T20.C76 (question):** the text names the creatures but not which way they face before and after; this is carried only by the figure.
- **M3.S20.T20.C77 and M3.S21.T21.C81, C83 (`text` field):** the old text has `[Image: ...]` markers in the middle of the steps and after the answer (from the old cards). The builder should remove them when the token is put before step 1.
- **Wording:** LP says "bookstall"; the book's sign says BOOKSTORE. The diagram uses the LP word. Either word is fine, but the LP and the picture must agree.

## (3) Book unclear

- Fun with Turns Q1, row 7: no number before "right angles clockwise", as above. The base guesses 1/2 or 1 1/2; neither fits (West turned 1/2 right angle ends between two directions), so I left it alone.
- The "after" pictures of the ladybug and the snail in the book are drawn slightly tilted; I read all four as exact quarter turns, as the question says.
- The book's compass tags for East and West use rotated text; in the diagram all four tags carry horizontal text, and directions are written North, East, South, West (LP style; the book prints capitals).
- The book has no printed solutions in this pdf, so every answer here follows the LP solution text (it agrees with the pictures).
