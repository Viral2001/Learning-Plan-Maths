# Chunk B notes (Class 5 Ch 14 "Maps and Locations")

Units: T9 Street Map (5 pairs), T10 Reading a Metro Map (2 worked), T11 Metro Map (2 pairs), T12 Metro Routes (4 pairs), T13 Making a Map with a Key (1 worked),
T14 Let Us Do (1 pair), T15 Distance and Direction on a Grid (2 worked), T16 Example 1 (1 pair). 31 items: required 29, optional 0, none 2. Validator: errors 0, 4 warnings
(see "Warnings" below). Generator scripts are outside HERE (scratchpad).

## 1. Judgement calls

- **How the maps are drawn.** The street map, the metro map, the library plan and the school sample are redrawn as flat schematic diagrams (rectangles, bands, circles, capsules,
  labels). Left out on purpose: the red printed bus route of the street map (it belongs to the Bus Route fill-in blanks, chunk A, not to questions (a) to (e)), trees, see-saw, swings,
  court lines, the river of the metro map, the title box "Delhi Metro Map" and the "KEYS" tab (no headings, no scenery). The key box itself is kept (the book says "Read the key").
- **Metro map geometry.** Station positions were measured from the page 5 picture (circle detection + my own check on 3x to 5x crops) in a 784 x 530 unit frame; capsule dots read from the
  picture. 146 plain circles and 19 capsules are listed. Every circle count between named stations that the LP solutions use was re-counted on the picture and agrees:
  Qutb Minar-Hauz Khas 2, Hauz Khas-INA 2, INA-Central Secretariat 3, Central Secretariat-Rajiv Chowk 1, Rajiv Chowk-Supreme Court 2, Supreme Court-Yamuna Bank 1,
  Yamuna Bank-Mayur Vihar 1, Mayur Vihar-Botanical Garden 5, Hauz Khas-Kalkaji Mandir 4, Kalkaji Mandir-Botanical Garden 7, Kalkaji Mandir-Badarpur 6, Janakpuri West-Hauz Khas 10,
  Janakpuri West-Rajouri Garden 4, Rajouri Garden-Kriti Nagar 2, Kriti Nagar-Rajiv Chowk 6, Rajouri Garden-INA 7, INA-pink/violet capsule 1, that capsule-Mayur Vihar 3,
  Qutb Minar-Millennium 8. The LP totals 14 / 15 / 25 for routes A / B / C and 31 for the Janakpuri West way all recompute.
- **Station names** use the LP spelling and title case (e.g. "Millennium City Centre Gurugram"; the book prints MILLENIUM, a spelling slip, corrected per decision 1).
- **Red.** There is no red style token; red dots (hidden objects, bookmark) use the WRONG token colour (#D55E00, the nearest red), said in `render_note`.
- **Route bands on the metro map** (T12): routes A, B, C are drawn as bands 6 units wide, shifted -8 / 0 / +8 units across the direction of travel so that the shared stretches
  (Qutb Minar to Hauz Khas, Mayur Vihar to Supreme Court) stay readable; colours ANSWER / SET_B / FOCUS. Lali's route in (b) is the same path as route C.
- **Text size.** 34 px text on a 1920 px canvas makes the metro map crowded; the spec lets the renderer nudge a name up to 20 units along its own side.
- **T11 Q1 (C42/C43).** Question diagram required (the question is about the coloured lines and the key, which exist only in the picture); solution `none`
  (SAME_AS_QUESTION_DIAGRAM): the answer is a sentence and the key and lines are already in the question figure.
- **T14 (C56/C57).** The question is an open activity: `none` (OPEN_ENDED). The book's sample school map and its key strips (P06-map-1, P06-key-1) are mapped `none:OPEN_ENDED`.
  The solution draws the LP's own sample answer (gate in the west wall, road on the west side, building on the east side, tree and bench near the middle, garden near the south wall,
  3 red dots, 7-row key), not the book's sample.
- **T13 library corner (C54)** and the **ant worked examples C58 / C59** use scenarios written in the LP, not book pictures, so they have no base inventory figure (hence the warnings).
  C58 uses the book's 11 x 11 grid layout with the ant at the centre point (5,5): leaf (1,5), seed (5,11), berry (7,1). C59 is one picture with 3 small grids (7 x 5 squares), one per route.
- **T16 Example 1 (C61/C62).** The question figure is the book grid with the ant at (5,5) and the four foods at laddoos (7,5), sugar (5,2), bread (2,7), apple (8,8), without the printed red
  dots and dashed routes (those are answers of (a) to (d), chunk C). The solution adds a green arrow ant -> laddoos with the tag "2 cm east".
- **Teaching images** (C39.IMG1, C40.IMG1, C54.IMG1, C58.IMG1, C59.IMG1) stay and are never linked; the new diagrams are `IMG2` of those concepts (decision 5). Excerpts C39 and C40 do not print
  the answers the teaching images print (no "4 + 1 + 6", no line names on the lines).
- **Inventory.** Base figures claimed: P04-map-1 (question C29, NEW-P04-map-1-<id> for every further street-map use, question or solution), P05-map-1 (question C42, NEW-P05-map-1-<id> for the
  other metro items), P05-key-1 (C39), P06-map-1 and P06-key-1 (none:OPEN_ENDED), P07-grid_map-1 (question C61, NEW- entry for C62). Chunk A also uses the street map and chunk C the ant grid:
  the merge renames the later claim.

## 2. Borderline

- T9 solutions Q1 (C30), Q3 (C34), Q5 (C38): the answer is complete in text (two house names, "Stop 1", "south"), but each adds rings, lines or an arrow on the map; required for consistency with the route
  solutions Q2 and Q4 (printed answer is a drawing).
- T11 Q1 question required, solution none (see above).
- T12 (c) C51 and (d) C53 solutions: the answer is a number / an opinion; required because the solution counts along three routes on the map and the figure shows those routes with the counts
  (sibling consistency with (a) and (b)). (d) is an open answer, drawn as the LP sample (route A).
- T14 C56 question none although the book prints a sample map "given below": the learner can do the task without it.
- T15 C58 and C59: all data is in words, but the steps say "count the squares" of a grid and Route 3's wrong-way step is spatial; required.
- C39 and C40: required although teaching images show similar pictures (decision 5).
- T11 Q2 solution (C45): two rings on the map; required (the marked map is the answer).

## 3. LP text issues

- **M2.S13.T13.C54**, first block: "A sample map and its key are given below. Gate, Road, ..." refers to the book's school sample map, which the plan does not show (the teaching image is a library corner).
  Suggested: "Here is a sample map of a library corner and its key." or show the school sample.
- **M2.S14.T14.C57** (steps and answer): the sample map has a school wall (the gate is "in the west wall") but the key lists no wall; suggested: add "wall" to the key sentence and the key box, or
  say "the boundary line".
- **M2.S12.T12.C51 / C53** (and C50 / C52 questions): routes A, B, C are named only in the answer of the first question (C47); the questions of (c) and (d) do not define them. Suggested first step of C51: "Use
  the three routes A, B and C of the first question."
- **M2.S12.T12.C51**, Route C: "3 stations from Qutb Minar to Hauz Khas" includes Hauz Khas, while Route A counts Hauz Khas on its own ("(2), Hauz Khas (1)"). The total 25 is right. Suggested: "2 stations from
  Qutb Minar to Hauz Khas, Hauz Khas (1), 4 on the Magenta Line to Kalkaji Mandir, ..." giving 2 + 1 + 4 + 1 + 7 + 1 + 5 + 1 + 1 + 1 + 1 = 25.
- **M3.S16.T16.C61** question text: "To get to the laddoos" has no sentence saying that the ant and the laddoos are on the grid shown; the figure carries them, so the question diagram is required.
- No missing data was found for the street map items; all LP routes follow roads of the book picture (checked against the road bands).

## 4. Places where the book is unclear

- Metro map: several circles carry no label (on the Airport Express diagonal, on the Blue/Pink lines); positions are measured, so accurate to about 3 to 5 units. The book's title "MILLENIUM" is a spelling slip.
- Street map: the west road has no name; where the Children's Park route ends is not stated (the spec ends the LP route at the Hospital Road / Park Road corner, level with the park). The S1 stop stands at the
  hospital building's lower right edge next to Hospital Road ("hospital gate" in the LP).
- School sample map: no direction arrow is printed; the sample answer in the LP gets N at the top because the LP says so.

## Warnings

The validator prints 4 warnings: required items with no inventory figure (C54 library corner, C57 LP sample school map, C58 and C59 ant worked examples), whose pictures are LP scenarios and not printed in the book.
