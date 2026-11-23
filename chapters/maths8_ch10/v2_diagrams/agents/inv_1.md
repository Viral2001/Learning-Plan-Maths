You build part of the "Step 0 NCERT figure inventory" for the Class 8 chapter "Proportional Reasoning-2" (Ganita Prakash, Grade 8, Chapter 10). Your pages: pdf pages 1 to 15 of the book pdf, which hold the CHAPTER text (figures a question or example refers to, teaching figures, tables). Other agents do the other pages (the whole pdf has 15 pages; chapter pages 1-15). You change nothing except the one output file named below; you do not touch staging and upload nothing.

HERE = /root/maths-learning-plan/Learning-Plan-Maths/chapters/maths8_ch10/v2_diagrams/

Read first:
1. HERE/spec/diagram_identification_prompt_v3.md - section 3, "Step 0 - NCERT figure inventory", its "Printed-solution pictures count" sentence and the "Not a diagram" list; skim section 4 (what a diagram may contain). Only Step 0 is your job: decide nothing about LP items.
2. HERE/book/chapter_text.md - the text of each pdf page (marked <!-- pdf page N -->).
3. The page pictures HERE/book/page_NN.png (NN = pdf page, two digits). LOOK at the picture of EVERY page in your range; most figures exist only in the pictures. Zoom mentally: count every row, symbol, bar, square, dot, cube, tick and label.

What to list: every figure that carries mathematical content - tables (data, frequency, tally, number grids), pictographs and bar graphs (with key/scale/axes), number lines, geometric figures, constructions, solids, nets, views, patterns (dots, dice, tiles, number patterns), arrangements of people or objects, maps and grids, clocks/scales/instruments, and any figure a question or example refers to ("the figure", "shown below", "Figure it Out" drawings), plus every picture a PRINTED ANSWER draws. Skip pure decoration: mascots/characters, scenery, page art, QR codes; a photograph is listed only when a question or example works on it. Give each figure at the granularity the book shows it: a row of steps printed side by side is ONE figure whose description lists every step; two graphs printed for comparison are two figures.

Output: ONE JSON file HERE/map/inv_base_chapter_01_15.json = a list of objects with exactly these keys:
- fig_id: "P<NN>-<kind>-<k>" (NN = two-digit pdf page, kind = short snake_case such as table, pictograph, bar_graph, number_line, shape, solid, net, pattern, k = running number on that page)
- page: integer pdf page
- source: "chapter p.<NN>"
- section: the section number printed in the book (e.g. "4.2") or "Figure it Out", "Math Talk", "Summary"
- belongs_to: the text, example or question the figure belongs to (for printed answers: the question it answers, with the printed question number), in a short quotation or paraphrase that lets a reader find it
- kind: the same snake_case kind
- shown_as: one of "teaching figure" | "given in question" | "worked example picture" | "printed answer picture"
- description: exact and complete, so someone who has not seen the page could draw it: every row, category, symbol count, key, axis title, scale, bar height, tick label, step, count, label, orientation, which parts are shaded/removed/highlighted. Write counts you verified by counting, not estimates.
- unclear: list of strings with anything you could not read with certainty (empty list if none)

Write the JSON with a small Python script kept in your scratchpad or /tmp (not in HERE), using json.dump(..., ensure_ascii=False, indent=1). Then check: python3 -I -X utf8 -c "import json;a=json.load(open('/root/maths-learning-plan/Learning-Plan-Maths/chapters/maths8_ch10/v2_diagrams/map/inv_base_chapter_01_15.json',encoding='utf-8'));print(len(a),len({x['fig_id'] for x in a}))" and make sure the fig_ids are unique. If your pages hold no figure at all, write an empty list [].

Final message: at most 50 words (number of figures, and ONE line only if a page is unreadable or something needs the user's decision). Do not paste the JSON.
