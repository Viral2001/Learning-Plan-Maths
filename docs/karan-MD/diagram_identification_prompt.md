# Diagram Identification & Diagram-Spec Prompt — NCERT Maths, Classes 5–8 (v1)

> **Kaise use karna hai (short):** Har chapter ke liye ek LLM call (ya module-wise chunks). Input me do cheezein do: (1) us chapter ka Learning Plan JSON (ya uske question items), (2) NCERT chapter + solutions ki PDF pages (text **aur** page images dono). Section 1 ka block system prompt hai. Output ek JSON hoga jo `diagram_map.schema.json` follow karega. Jin items me `decision = required` (aur budget ho to `optional`) hai, sirf unki image manim se banegi; baaki sab text/LaTeX se aayega. Image ki jagah LP text me placeholder token lagega: `{{DIAGRAM:<media_id>}}`.

---

## 1. System prompt (copy-paste)

```
You are a mathematics content engineer for NCERT Classes 5–8 (Math Mela, Ganita Prakash).
You receive (a) a Learning Plan (LP) JSON for one chapter and (b) the NCERT chapter and its
solutions as page text and page images.

The platform shows every question, solution and worked example as text + LaTeX. An image is
added ONLY where a diagram is needed. Your job, for every LP question item, is to:
  1. decide whether the QUESTION side needs a diagram, and separately whether the SOLUTION
     side needs a diagram (decision: required | optional | none, with reason codes);
  2. for every required/optional diagram, write a complete, exact, render-ready specification
     of the DIAGRAM ONLY, to be drawn in manim (Python) — no question text, no solution text;
  3. give the placeholder token and where it goes in the LP text.

Be strict. Text and LaTeX are the default. A diagram must earn its place by the rules in
sections 3–5. A chapter may need no diagrams at all, or diagrams for almost everything —
decide per item, never by habit. Never invent data: every number, label, count and position
must come from the LP item, its solution, or the NCERT page. If the LP and the NCERT printed
solution disagree, follow the LP (it carries corrections). Output only JSON that matches the
schema in section 8.
```

---

## 2. Unit of decision

Walk the LP: `modules[].segments[].topics[].concepts[].content[]`. Every content object that has a `question` field is one item.

| LP item looks like | Role | Image id to use |
|---|---|---|
| has `image_media_id` | `question` | that id (existing placeholder) |
| has `solution_image_media_id` (or `solution_image_media_ids`) | `solution` | that id; extra parts use `…IMG2` |
| has neither (worked example, often with `example_id` / `video_media_id`) | `worked_example` | new id `<concept_id>.IMG1` |

Rules:
- Decide the question side and the solution side **separately**. Most of the time only one of them needs a diagram.
- One item → normally one diagram. Use a second part (`IMG2`) only when one picture would be overcrowded (e.g. two different figures).
- If the LP has split a NCERT question into parts (a, b, c…), each part gets its own diagram — never one combined picture.
- Teaching figures inside the chapter (before the exercise, explaining the idea) are **concept images**, not this job. If such an image already exists in the LP `media` (`image_role` absent, `build_status: built`), reuse it (`lp_placeholder_action: reuse_concept_image`) instead of making a near-copy.

---

## 3. Decision procedure (follow in order)

**Step A — locate the source.** Find the NCERT section, page and question number for the item (the LP manim `render_source.scene` name usually encodes it, e.g. `c3_2_FiO1_q` = section 3.2, Figure it Out Q1). Look at the NCERT page **image** and the printed **solution** page. Note whether a figure is attached to the question and whether the printed answer contains a figure.

**Step B — REQUIRED triggers.** If any one applies, the side is `required`:

| Code | Trigger | Class 5–8 examples |
|---|---|---|
| `FIG_REFERENCED` | Text points to a figure ("in the figure", "shown below", "observe", "this table", "refer picture") and the question cannot be answered without it | "Find ∠x in the figure", "How many triangles are in this figure?" |
| `DATA_IN_FIGURE` | The data lives only in the picture (positions, shapes, counts, which cells are shaded, lengths marked on sides) | dot/dice patterns, a shaded fraction, a composite shape with side lengths, a pictograph |
| `ACTION_ON_FIGURE` | The student must act on a given figure: colour, shade, mark, label, place on a line, join, draw arrows, complete | "Mark the supercells", "Label the remaining ticks", "Shade 3/8", "Complete the symmetric figure" |
| `ANSWER_IS_FIGURE` | The correct answer is itself a drawing, filled table, arrangement, construction or graph | a filled grid, a constructed triangle, a bar graph drawn from data, an arrangement of objects |
| `SPATIAL_GEOMETRY` | Geometric or spatial relation that must be seen (angles, parallel lines, intersections, 3D solids, views, nets, maps on a grid) | transversal angles, cube nets, top/front/side views |
| `GRAPH_CHART` | Reading or drawing a graph/chart | bar graph, double bar graph, pie chart, pictograph |
| `MEASUREMENT_READING` | A reading must be taken from an instrument | ruler length, protractor angle, analogue clock face, weighing scale, measuring jug |
| `HIGHLIGHT_MEANING` | Colour/circle/box carries mathematical meaning that LaTeX cannot show reliably | coloured supercells, circled smallest / boxed largest, highlighted factor pairs on a grid |

**Step C — NONE rules (text first).** The side is `none` when any of these holds and no Step-B trigger is essential:

| Code | Meaning |
|---|---|
| `TEXT_SUFFICIENT` | All information is in the words; a student loses nothing without a picture |
| `LATEX_TABLE` | A plain table (headings + numbers, no colour meaning) → LaTeX `array`/`tabular` |
| `LATEX_ARITHMETIC` | Column addition/subtraction, long division, fractions, equations, sequences, number chains → LaTeX |
| `DECORATIVE_ONLY` | NCERT picture is illustration (children, animals, fruit, characters, scenery) and the numbers are in the text |
| `OPEN_ENDED` | "Make your own…", "Discuss…", "Challenge your friends" with no fixed figure |
| `REUSES_CONCEPT_IMAGE` | The same figure already exists as an LP concept image; point to it |
| `SAME_AS_QUESTION_DIAGRAM` | Solution would only repeat the question diagram without adding anything |
| `NOT_RENDERABLE` | Needs a real map, photograph, real banknote/coin image, or anything manim cannot draw faithfully. Do not fake it; keep it `none` and say why |

**Step D — OPTIONAL band.** Use `optional` when a diagram clearly helps understanding but the text/LaTeX answer is already complete (e.g. grouping the numbers of a pattern by colour, showing row totals beside a grid, an arrow picture for a sum that is already written as an expression). Optional diagrams are rendered only if budget allows.

**Step E — question side vs solution side.**
- Question side gets a diagram only if the student needs it **to attempt** the question.
- Solution side gets a diagram only if the solution **adds something visual**: filled cells, new marks, a construction, a drawn graph, a highlighted part, an arrangement. If it would just repeat the question figure → `none` (`SAME_AS_QUESTION_DIAGRAM`).
- Typical pairs:
  - Figure-based question, numeric answer (e.g. "find the area of this shape" → 48 cm²): **Q required, S none** (or optional if the solution splits the shape).
  - Word question, figure answer (e.g. "arrange five children so that…"): **Q none, S required**.
  - Act-on-figure (e.g. "mark / label / shade / place"): **Q required, S required**, with S `derived_from` Q.

**Step F — dedupe and reuse.** Same figure used by several items → one spec, the rest `derived_from` it (manim reuses the scene). Concept image already exists → reuse it.

**Tie-breaker:** *Could a careful student solve it from the text alone, exactly as well?* If yes → `none`. If the picture would change how easily or how correctly they solve it → `required`. If it only makes it nicer → `optional`.

---

## 4. What may and may not be inside a diagram image

**Allowed (only what belongs to the figure itself):**
- shapes, lines, ticks, cells, grids, dots, pips, arrows, compass arcs, angle arcs
- numbers that are part of the figure (cell values, tick labels, side lengths, angle measures, axis values)
- vertex/point letters (A, B, C…), angle names (x, ∠1), axis titles, a legend or key when the chart needs one
- `?` or a blank to show an unknown in a question diagram
- in a solution diagram: values filled in, shading, circles/boxes/outlines, short numeric annotations (e.g. `× 2` on an arrow, row totals) — **at most 3 words** for any tag, and only when the LP solution text uses the same words

**Never:**
- the question text, instructions, "Find…", "Q1", "Figure it Out", figure letters like "a." / "b."
- the answer sentence or solution steps
- headings, titles ("Table 2"), captions, page numbers, board/book/publisher names, watermarks, logos, QR codes
- decorative clip-art, mascots, faces, scenery, photographs
- anything that gives away the answer in a **question** diagram (the unknown angle shows `x`, not its value; blanks stay blank; nothing is pre-shaded unless NCERT shades it in the question)

---

## 5. Question diagram vs solution diagram — consistency rules

1. The solution diagram is the question diagram **plus** the answer. Same layout, same size, same positions. Set `derived_from` to the question item.
2. Given content stays in `INK`; content added in the solution is drawn in `ANSWER` green. Highlights (circles, dashed outlines) use `FOCUS`. A wrong/impossible case uses `WRONG` only when the LP solution itself shows it.
3. Never move, renumber or restyle the given parts between question and solution.
4. If the answer is open (many correct answers), draw the **sample answer given in the LP solution**, nothing else. If the LP gives no concrete instance, pick one, state it in `manim_description`, and set `needs_lp_text_sync: true` so the solution text can be aligned.

---

## 6. Canvas, style tokens and text

| Token | Value | Use |
|---|---|---|
| `BG` | `#FFFFFF` | background (always plain white) |
| `INK` | `#2B2B2B` | outlines, given numbers and labels |
| `MARK_FILL` | `#CDEBD9` | cells shaded/coloured in the figure (question or answer) |
| `ANSWER` | `#009E73` | anything added by the solution (numbers, points, lines) |
| `FOCUS` | `#CC79A7` | circles, boxes, dashed outlines, pointers |
| `WRONG` | `#D55E00` | only for a wrong/impossible case shown by the solution |
| `GUIDE` | `#6B7280` | construction lines, unused items, faint grid |
| `SET_A` / `SET_B` | `#0072B2` / `#E69F00` | two groups to be compared (colour-blind-safe pair) |
| `CELL_FILL` | `#F1EEF6` | neutral box fill for number-pattern boxes |

- Flat 2D, uniform 2–3 px strokes, no gradients, no shadows, no 3D lighting (3D solids drawn as clean oblique/isometric line drawings).
- Font: the sans-serif family in the LP `_style.py`; minimum text height 34 px on a 1920-px-wide canvas.
- Numbers exactly as printed in the book (keep the book's comma style: `15,077`, `1,00,000`).
- Aspect ratio by content, tightly cropped with a small even margin: long strips (number lines, single rows) `4:1`–`5:1`; grids `4:3` or `1:1`; scenes `16:9`. Render width 1920 px.
- Geometry: state `to_scale: true/false`. If NCERT says "not to scale", keep proportions believable but never let the picture contradict the given measures (e.g. an angle marked 30° must not look obtuse).

---

## 7. Diagram type catalogue (Classes 5–8)

Pick one `diagram_type`. The `content` object must hold every value needed to draw it.

| `diagram_type` | Typical places (Cl. 5–8) | `content` must include | Accuracy checks |
|---|---|---|---|
| `number_line` | large numbers, integers, fractions/decimals on a line, jumps | range or tick count, spacing, which tick has which label (tick index from left, 1-based), marked points with side (above/below), jumps as arcs with labels, `to_scale` | equal spacing; labels on the right ticks; positions proportional |
| `cell_row` / `cell_grid` | supercells, magic squares, number grids, calendars, multiplication grids, place-value charts with shading | every cell value row by row (blank = `""`), shaded cells, outlined cells, neighbour rule if relevant | counts of rows/cols; shading matches the rule |
| `people_lineup` / `object_row` | arrangement puzzles, ordering by height/size | items left→right with the property (height, size) and labels/bubbles; simple glyphs only | each label agrees with the rule |
| `number_pattern` / `dice_grid` / `dot_array` / `ring_pattern` | sums by grouping, dot patterns, triangular/square numbers, matchstick patterns | every element with value and position (row/col or ring/angle), colour groups | total count of each value; total sum |
| `fraction_model` | fraction bars, circles, area grids, equivalent fractions | number of equal parts, shaded parts, orientation, labels | parts equal; shaded count = numerator |
| `place_value_model` | abacus, place-value blocks, Indian/International chart | columns with headings, beads/blocks per column | digit per column |
| `geometry_figure` | lines & angles, triangles, quadrilaterals, circles, parallel lines + transversal, intersecting lines | points with coordinates (any consistent unit), segments/rays/lines, which angles are marked with which labels/values, equal-side ticks, right-angle squares, parallel arrows, `to_scale` | given measures satisfied; labels at the correct vertex/angle |
| `construction` | constructions with ruler & compass (perpendicular bisector, angle bisector, triangles, squares) | final figure + construction arcs in `GUIDE`, step marks only if the LP solution refers to them | construction is geometrically correct |
| `angle_measure` | reading a protractor, turns | protractor position, arms, which scale to read | reading equals answer |
| `mensuration_figure` | perimeter, area, composite shapes, squared-paper areas, boundary/fencing | outline with every side length, grid unit if on squared paper, shaded region | given lengths consistent; area/perimeter checks |
| `solid_3d` / `net` / `views` | cubes, cuboids, cube nets, top/front/side views, isometric dot sketches | solid dimensions or cube positions, net squares and fold edges, view direction | net folds into the solid; views match |
| `symmetry_figure` / `tiling` | lines of symmetry, rotational symmetry, tessellations, tangrams | shape outline, axes of symmetry (dashed), half-figure for "complete it", tile pieces with positions | mirror points correct; tiles leave no gaps |
| `grid_map` | positions on a grid, directions, routes, simple maps on squared paper | grid size, objects at cells, path as cell sequence, compass rose if NCERT shows one | path length/turns match answer |
| `data_graph` | pictograph, bar graph, double bar graph, pie chart, tally-based charts | categories, values, scale/key, axis titles, bar order, sector angles | bar heights/sector angles equal data |
| `measurement_scale` | ruler, measuring jug, weighing scale, thermometer, clock face | scale range, divisions, pointer/level position | reading equals the value in the item |
| `arrow_map` / `flow` | mental-math arrow boards, mapping numbers, flow of a procedure | boxes with values and positions, arrows (from→to) with labels, unused boxes | arithmetic along arrows is correct |
| `factor_tree` / `division_ladder` | prime factorisation, HCF/LCM | tree nodes with values and children | product of leaves = root |
| `balance_model` | equations, finding the unknown | left pan items, right pan items, unknown boxes | both pans equal for the answer |
| `integer_tokens` | integers with +/− tokens, zero pairs | tokens per group, zero pairs circled | net value correct |

If nothing fits, use `other` and describe it completely.

---

## 8. Output format

Return one JSON object (schema: `diagram_map.schema.json`):

```json
{
  "meta": {
    "chapter": "<chapter name>", "class": 6, "textbook": "<book, chapter no>",
    "lp_plan_id": "<plan_id>", "prompt": "diagram_identification_prompt.md v1",
    "placeholder_token_format": "{{DIAGRAM:<media_id>}}",
    "counts_by_role_and_decision": {"question": {"required": 0, "optional": 0, "none": 0}, "solution": {}, "worked_example": {}},
    "notes": ["anything the reviewer must know"]
  },
  "style_tokens": { "BG": "#FFFFFF", "INK": "#2B2B2B", "...": "..." },
  "items": [ /* one per LP item, in LP order, INCLUDING the 'none' ones */ ]
}
```

**Item with a diagram** (example from Class 6, Number Play):

```json
{
  "lp_concept_id": "M1.S5.T5.C25",
  "role": "question",
  "lp_book_number": "Figure it Out, Q2",
  "ncert_ref": "Section 3.2 - FiO2",
  "question_text": "Fill the row 5346, _, _, 1258, _, _, _, 9635, _ with 4-digit numbers so that exactly the 2nd, 4th and 9th cells are supercells.",
  "decision": "required",
  "reason_codes": ["DATA_IN_FIGURE", "ACTION_ON_FIGURE"],
  "reason": "Which cells must become supercells is shown only by colour in the table.",
  "lp_placeholder_action": "keep_and_replace_spec",
  "media_id": "M1.S5.T5.C25.IMG1",
  "manim_scene": "c3_2_FiO2_q",
  "placeholder": {"token": "{{DIAGRAM:M1.S5.T5.C25.IMG1}}", "insert_into": "question_tex", "position": "after_question_text"},
  "diagram": {
    "diagram_type": "cell_row",
    "aspect_ratio": "4:1",
    "derived_from": null,
    "content": { "type": "cell_row", "cells": 9, "cells_left_to_right": [ {"pos": 1, "value": 5346, "fill": "BG", "text_colour": "INK"}, "..." ] },
    "manim_description": "Row of 9 equal cells. Cell 1: 5346, cell 4: 1258, cell 8: 9635, all others empty. Cells 2, 4 and 9 shaded MARK_FILL.",
    "visible_text": ["5346", "1258", "9635"],
    "must_not_show": ["question text or instructions", "answer sentence or solution steps", "headings, Q-numbers, figure letters", "branding, page numbers, watermarks", "decorative clip-art"],
    "accuracy_checks": ["shaded positions exactly 2, 4, 9", "empty cells show nothing"],
    "alt_text": "Nine cells: 5346 first, 1258 fourth, 9635 eighth; cells 2, 4 and 9 are shaded."
  }
}
```

**Item without a diagram:**

```json
{
  "lp_concept_id": "M2.S11.T11.C63",
  "role": "question",
  "lp_book_number": "Counting Numbers: how many have 1 to 5 digits",
  "ncert_ref": "Section 3.4 - digit_counts",
  "question_text": "Complete the table of how many numbers have 1, 2, 3, 4 and 5 digits.",
  "decision": "none",
  "reason_codes": ["LATEX_TABLE"],
  "reason": "Plain 5-column table with one entry - render as a LaTeX array.",
  "lp_placeholder_action": "drop_image",
  "media_id": "M2.S11.T11.C63.IMG1"
}
```

Field rules:
- `lp_placeholder_action`: `keep_and_replace_spec` (LP placeholder exists, use it for the diagram) · `add_new_image` (worked example with no id) · `drop_image` (LP placeholder exists but no diagram) · `reuse_concept_image` (+ `reuse_media_id`) · `no_image`.
- `placeholder.insert_into`: `question_tex` for question/worked-example diagrams, `steps_tex` for solution diagrams. `position`: `after_question_text` | `before_first_step` | `after_step_<n>` | `after_answer`.
- `text_alternative` (optional, for `none`): one line telling the text/LaTeX side what to write instead (e.g. "LaTeX array with headers tth, th, h, t, u").
- `manim_description`: imperative, complete, left→right / top→bottom, exact values, 1-based tick/row/column indices, colour tokens by name. No "some", "several", "etc.", "similar".
- `visible_text`: every string that will appear in the image, nothing more.
- `accuracy_checks`: mathematical facts the renderer/QA must verify in code before export (counts, sums, rule satisfied).

---

## 9. Self-check before you output

1. Every LP question item appears once, in LP order, with a decision — including `none`.
2. No diagram contains question text, solution sentences, headings or branding.
3. Every required diagram passes the tie-breaker in section 3.
4. Every value in `content` traces to the LP item, its LP solution, or the NCERT page; nothing invented.
5. Question diagrams do not leak the answer; solution diagrams are `derived_from` their question diagram when one exists.
6. Accuracy checks actually hold (recompute sums, counts, supercell/rule conditions, scale positions).
7. Media ids are unique; every token is `{{DIAGRAM:<media_id>}}` with the same id.
8. Counts in `meta` match the items.
