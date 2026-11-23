# Audit of the user's two decisions (23 Nov 2026), Class 7 Ch 15 "Finding the Unknown" (cbse_eng_maths7_ch15_v27)

Rule 1 = book mistakes (diagram shows the correct value). Rule 2 = figure letters (letters in a combined picture only if the LP answer text uses them).
Chunks A to D audited in full; chunk E (decided after the decisions) only checked for consistency.

## Changed items

None. No `out_<CHUNK>.json` was edited, so no `.before_user_decisions` backups exist. Validator re-run on all five chunks (read only): errors 0 in A, B, C, D, E.

## Examined, left as is

### Rule 1 (book slips)
Every required diagram was recomputed against the LP solution and compared with the book page picture (pp. 1, 2, 3, 11, 17, 20, 22, 24, 25, 26).
- C5/C6, C7/C8, C9/C10 (Mobiles 1-8): every printed number and object count agrees with the LP solution (16/8, 24/12, 8/4, 18/9, 40/20, bud 2, flower 8, fish 8, submarine 4, book 4, pencil box 2, cloud 1, bolt 3, crown 5, gem 3, egg 3, donut 6, banana 3). No slip.
- C11/C12, C13/C14 (Sack scales 1-4): sacks 10, 14, 7, 15 kg recomputed (both pans 12, 28, 35, 1400). Counts of sacks match the book. No slip. (Borderline "required" status of the C12/C14 solutions left to the decision already recorded.)
- C16, C22 (worked example Mobiles 6, 7; Mobile 8 with Sack scales 1-3): same data, no slip.
- C18, C20 (matchstick triangles 1 to 4): picture shows 1, 2, 3, 4 triangles, 3/5/7/9 sticks. No slip.
- C26 (blobs): 3 blobs, 4 visible dots, 25 dots: 3b + 4 = 25, b = 7. No slip.
- C28, C30 (Q16 stick patterns): 6, 9, 12 sticks (3n + 3); staircase 4, 7, 10, 13 squares and 13, 22, 31 sticks (9n + 4), counted in an enlarged crop of p. 25. No slip.
- C76/C77 (Q19 path puzzle): all 12 boxes solved (6, 1, 3, 21, 2, -10, 13, 8, 4, 4, -13/25 and the start x = 4); every arrow on the path carries the answer of the box it leaves and is unique at each box. The printed "+4" on the arrow between -4 = 16 - 5k and 2x - 9 = 3 - x has the same value as 4 (k = 4, x = 4), so it is not a wrong value; kept as printed. Other arrow labels (-4, -1, -2, -44, 5, 6, ...) are decoys, not slips.
- C83/C84 (Example 7 tiles): book Steps 1-3 (3+1, 5+2, 7+3 tiles) and Method 1 Step 4 (4+4+4+1 = 13) agree with the LP (4, 7, 10, 13; 3k + 1). No slip.
- C93 (window grill): 34 = 3 + 3 + 5 x 2 + 6 x 3; the book marks only the top 3 cm and one 2 cm rod, the bottom border and other rods follow the LP text. A missing label, not a wrong value. No change.
- C97 (two triangles): labels y, y + 15 and x, x - 10, x + 10 as in the book/LP; angle sums 180. No slip.
- C123/C124 (chains): both chains in the book (p. 17) satisfy y = 5 at every node and every downward operation is right. `-1 - y = -6` (LP) versus `-y - 1 = -6` (book) is the same expression, not a slip; `needs_lp_text_sync` already set.
- C158 (ancient notation table, chunk E): book table p. 20 shows one dot over the 8 of "yā 2 rū 8" only; spec matches. No slip.
- Slips found elsewhere draw nothing wrong and need no change: Example 3 prints 132 for 135 on p. 7 (none item), Q5 first machine prints "+5" (none item), box 8 prints "-6v - 8x = 14" (none item, inventory entry already says so), Example 16 prints "+ (100)" (none item).

### Rule 2 (figure letters)
Combined pictures: Mobiles 1-3 (C5/C6), Mobiles 4-5 (C7/C8), Mobiles 6-8 (C9/C10), Sack scales 1-2 and 3-4 (C11-C14), Mobiles 6-7 (C16), Mobile 8 + Sack scales 1-3 (C22), position strips (C18, C20, C28, C30), two triangles (C97). None of them is a set of lettered figures: the book labels are Fig. 7.x, and the LP question and answer texts refer to them as "Mobile n", "Sack scale n", "position n", "first/second pattern", "first/second triangle". The (a)-(d) in the C28-C31 texts are the sub-questions, not figures. No spec shows figure letters (none of the `visible_text` lists contains a letter label), so nothing to add and nothing to remove.

## Unresolved

- C76/C77: the arrow between the boxes 2x + 5 = 3(x - 1) and 30 = 4 - 50n (column 3, rows 3-4) is printed without a number. It is not on the solution path, and neither the LP solution nor arithmetic forces a value for it (8 or -13/25 would both be guesses). Left blank as printed, as the spec and the inventory already say.

## For the caller (not changed)

- T21 Q1 (C123): the question text never writes the chains; the figure carries them. This is an LP text issue (already noted in notes_D.md), not touched.
