# -*- coding: utf-8 -*-
"""Overrides from the placement map the user supplied on 21 Nov 2026 ("ch3_number_play_diagram_map (1).json", prompt v1).

build_v3.py merge calls apply(items, figs, notes) after merging the four chunk outputs (prompt v2). The supplied map
decides WHERE the diagram placeholders go; the v2 specs (much more detailed than the v1 ones in that file) are kept
for every item that is a diagram in both. Differences between the supplied map and the v2 result, all applied here:

  1. every required SOLUTION diagram: token at steps_tex / before_first_step (v2 had after_step_N or after_answer);
  2. M1.S3.T3.C9 (3.1 Q3 question): optional in the supplied map -> no diagram (v2 made it required); its solution
     diagram C10 therefore stands alone (derived_from null, the spec no longer says "redraw the question diagram");
  3. the four worked examples on the lettered figures c, b, f, e of 3.9 (C166, C167, C169, C170): required in the
     supplied map -> a new DIAGRAM each (v2 pointed them at the teaching images C165.IMG1 / C168.IMG1 / C168.IMG2,
     which carry a title banner and a logo). Specs written from the book pages 13 and 14 in the v2 style.
  4. v3 rules (the user's answers of 21 Nov, written into diagram_identification_prompt v3): a teaching image is never linked
     from a block. The three worked examples that v2 had pointed at a same-topic teaching image (C81, C93, C94) become
     plain "no image" items, as in the supplied map.
Optional items stay not added (the user said so on 20 Nov): C14, C30, C97, C173, C175, C210, C212 (and C9 now).
"""
STD_NOT = ["question text or instructions", "answer sentence or solution steps", "headings, Q-numbers, figure letters",
           "branding, page numbers, watermarks", "decorative clip-art"]


# ---------------------------------------------------------------- the four worked-example diagrams
def worked(cid, ncert, question_text, scene, reason, diagram):
    return {
        "lp_concept_id": cid, "role": "worked_example", "lp_book_number": None, "ncert_ref": ncert,
        "question_text": question_text, "decision": "required", "reason_codes": ["DATA_IN_FIGURE"], "reason": reason,
        "lp_placeholder_action": "add_new_image", "media_id": cid + ".IMG1", "manim_scene": scene,
        "placeholder": {"token": "{{DIAGRAM:%s.IMG1}}" % cid, "insert_into": "question_tex", "position": "after_question_text"},
        "diagram": diagram,
    }


def fig_c():
    rows = [{"row": r, "value": 32, "filled_columns": [1, 2, 3, 4, 5, 6, 7, 8]} for r in (1, 2, 3, 4)] + \
           [{"row": r, "value": 64, "filled_columns": [1, 2, 3, 8]} for r in (5, 6, 7, 8)]
    return {
        "diagram_type": "cell_grid", "aspect_ratio": "1:1", "derived_from": None,
        "content": {"type": "cell_grid", "rows": 8, "cols": 8, "cell_side": 1.0, "cell_fill": "CELL_FILL", "cell_outline": "INK",
                    "outline_px": 2, "text_colour": "INK", "digit_height": 0.4, "rows_top_to_bottom": rows,
                    "empty_columns_in_rows_5_to_8": [4, 5, 6, 7]},
        "manim_description": (
            "On a plain white BG canvas draw an arch of bordered square cells on a layout of 8 columns by 8 rows, row 1 at the top "
            "and column 1 at the left. Every cell is 1.00 unit square, filled CELL_FILL with a 2 px INK outline, and holds its "
            "number centred in INK (digit height 0.40 unit). Neighbouring cells share their outline, with no gap between them. "
            "Rows 1, 2, 3 and 4: a cell in every one of the 8 columns, each holding 32 (32 cells). Rows 5, 6, 7 and 8: a cell holding 64 "
            "in columns 1, 2 and 3 and in column 8 only (16 cells). Columns 4, 5, 6 and 7 of rows 5 to 8 stay empty white BG: no cell, "
            "no fill and no outline there, so the whole figure looks like an upside-down U. Crop tightly with a small even margin. "
            "Draw no letter, total, bracket or colour that groups the 32s apart from the 64s."),
        "visible_text": ["32", "64"],
        "must_not_show": STD_NOT + ["the figure letter c", "the total 2048 or any row total",
                                    "cells, fill or outlines inside the gap (columns 4 to 7 of rows 5 to 8)",
                                    "a title banner or any logo (the teaching image of this topic has them, this diagram has neither)"],
        "accuracy_checks": ["8 columns x 8 rows; rows 1 to 4 hold 8 cells of 32 each (32 cells in all)",
                            "rows 5 to 8 hold 4 cells of 64 each, in columns 1, 2, 3 and 8 (16 cells in all)",
                            "columns 4 to 7 of rows 5 to 8 are empty",
                            "check value, not drawn: 32 x 32 + 16 x 64 = 1024 + 1024 = 2048"],
        "alt_text": "An upside-down U of cells: four full rows of eight 32s above four rows that hold 64 only in the three left columns and the right column.",
    }


def fig_b():
    blocks = [{"rows": [2, 3], "cols": [2, 3]}, {"rows": [2, 3], "cols": [6, 7]}, {"rows": [4, 5], "cols": [4, 5]},
              {"rows": [6, 7], "cols": [2, 3]}, {"rows": [6, 7], "cols": [6, 7]}]
    faces = ["O O O O O O O O", "O F F O O F F O", "O F F O O F F O", "O O O F F O O O",
             "O O O F F O O O", "O F F O O F F O", "O F F O O F F O", "O O O O O O O O"]
    return {
        "diagram_type": "dice_grid", "aspect_ratio": "1:1", "derived_from": None,
        "content": {"type": "dice_grid", "rows": 8, "cols": 8, "tile_side": 1.0, "tile_gap": 0.06, "pip_colour": "BG", "pip_radius": 0.08,
                    "pip_layouts_from_tile_bottom_left": {"ONE": [[0.5, 0.5]],
                                                          "FIVE": [[0.27, 0.27], [0.73, 0.27], [0.27, 0.73], [0.73, 0.73], [0.5, 0.5]]},
                    "tile_fill_ONE": "SET_B", "tile_fill_FIVE": "SET_A", "five_blocks": blocks,
                    "faces_row_by_row_top_to_bottom": faces, "face_key": {"O": "ONE", "F": "FIVE"}},
        "manim_description": (
            "On a plain white BG canvas draw a grid of 8 rows by 8 columns of equal square dice tiles: tile side 1.00 unit, 0.06 unit "
            "of BG gap between tiles, row 1 at the top and column 1 at the left. Pips are filled BG circles of radius 0.08 unit, "
            "positions measured from the tile's bottom-left corner. A ONE tile is filled SET_B and has a single pip at (0.50, 0.50). "
            "A FIVE tile is filled SET_A and has pips at (0.27, 0.27), (0.73, 0.27), (0.27, 0.73), (0.73, 0.73) and (0.50, 0.50). "
            "The 20 FIVE tiles form five blocks of 2 by 2 tiles: rows 2-3 with columns 2-3; rows 2-3 with columns 6-7; rows 4-5 with "
            "columns 4-5; rows 6-7 with columns 2-3; rows 6-7 with columns 6-7. Every other tile (44 of them) is a ONE tile. "
            "Row by row (O = ONE, F = FIVE): row 1 O O O O O O O O; row 2 O F F O O F F O; row 3 O F F O O F F O; row 4 O O O F F O O O; "
            "row 5 O O O F F O O O; row 6 O F F O O F F O; row 7 O F F O O F F O; row 8 O O O O O O O O. "
            "Crop tightly with a small even margin. Write no numeral, letter or total anywhere."),
        "visible_text": [],
        "must_not_show": STD_NOT + ["the figure letter b", "any numeral at all (the dice carry dots only)", "the total 144 or any block total",
                                    "a title banner or any logo (the teaching image of this topic has them, this diagram has neither)"],
        "accuracy_checks": ["8 rows x 8 columns = 64 tiles",
                            "20 FIVE tiles, exactly in the five 2 x 2 blocks listed; the other 44 tiles are ONE",
                            "each FIVE tile has 5 pips (four corners and the centre), each ONE tile has 1 pip",
                            "check value, not drawn: 20 x 5 + 44 x 1 = 100 + 44 = 144"],
        "alt_text": "An 8 by 8 grid of dice: most show one dot, and five blocks of 2 by 2 dice show five dots, one block in the middle and four towards the corners.",
    }


def fig_f():
    r3 = [(90 + 20 * k) % 360 for k in range(18)]
    return {
        "diagram_type": "ring_pattern", "aspect_ratio": "1:1", "derived_from": None,
        "content": {"type": "ring_pattern", "outer_disc_radius": 4.0, "outer_disc_fill": "CELL_FILL", "zone_outline": "GUIDE", "outline_px": 2,
                    "zone_circle_radii": [1.62, 2.75], "coin_radius": 0.48, "coin_fill": "MARK_FILL", "coin_outline": "INK",
                    "text_colour": "INK", "text_upright": True, "digit_height": 0.30,
                    "angle_convention": "degrees anticlockwise from the positive x-axis, centre of the board at the origin",
                    "centre_coin": {"value": 1000},
                    "rings_inner_to_outer": [
                        {"ring": 1, "radius": 1.05, "count": 4, "value": 500, "angles_deg": [90, 0, 270, 180]},
                        {"ring": 2, "radius": 2.2, "count": 8, "value": 250, "angles_deg": [90, 45, 0, 315, 270, 225, 180, 135]},
                        {"ring": 3, "radius": 3.3, "count": 18, "value": 125, "angles_deg": r3}]},
        "manim_description": (
            "On a plain white BG canvas draw a round board with its centre at the middle of the canvas. Outer disc: radius 4.00 units, "
            "filled CELL_FILL with a 2 px GUIDE outline. Inside it draw two unfilled circles with a 2 px GUIDE outline, at radius 1.62 and "
            "at radius 2.75 units, so the board has three zones. Every coin is a circle of radius 0.48 unit filled MARK_FILL with a "
            "2 px INK outline and holds its number centred in INK, upright (never rotated), digit height 0.30 unit. Centre coin at the "
            "centre: 1000. Ring 1, centres 1.05 units from the centre: 4 coins holding 500, at angles 90, 0, 270 and 180 degrees. "
            "Ring 2, centres 2.20 units from the centre: 8 coins holding 250, at angles 90, 45, 0, 315, 270, 225, 180 and 135 degrees. "
            "Ring 3, centres 3.30 units from the centre: 18 coins holding 125, at angles 90, 110, 130, 150, 170, 190, 210, 230, 250, 270, "
            "290, 310, 330, 350, 10, 30, 50 and 70 degrees. Angles are measured anticlockwise from the positive x-axis. No two coins touch "
            "and no coin crosses a zone circle: ring 1 lies inside the circle of radius 1.62, ring 2 between the circles of radius 1.62 "
            "and 2.75, ring 3 between the circle of radius 2.75 and the outer edge. Crop tightly with a small even margin. "
            "Write no letter, total or ring label."),
        "visible_text": ["1000", "500", "250", "125"],
        "must_not_show": STD_NOT + ["the figure letter f", "ring totals or the total 7250", "numbers rotated along the rings",
                                    "a title banner or any logo (the teaching image of this topic has them, this diagram has neither)"],
        "accuracy_checks": ["1 + 4 + 8 + 18 = 31 coins: one 1000, four 500, eight 250, eighteen 125",
                            "coins of one ring are evenly spaced (90, 45 and 20 degrees apart) and all start at the top (90 degrees)",
                            "neighbouring coins never touch: the smallest gap is 0.09 unit (centre coin to ring 1)",
                            "check value, not drawn: 1000 + 4 x 500 + 8 x 250 + 18 x 125 = 1000 + 2000 + 2000 + 2250 = 7250"],
        "alt_text": "A round board with 1000 in the middle and rings of four 500s, eight 250s and eighteen 125s around it.",
    }


def fig_e():
    s = 0.8660
    h = 1.7321
    t = 2.5981
    small = [
        {"name": "centre", "centre": [0, 0], "numbers_by_corner": {"upper_left": 15, "upper_right": 25, "right": 35, "lower_right": 15, "lower_left": 25, "left": 35}},
        {"name": "top", "centre": [0, h], "all_six_numbers": 35},
        {"name": "bottom", "centre": [0, -h], "all_six_numbers": 35},
        {"name": "upper_right", "centre": [1.5, s], "all_six_numbers": 15},
        {"name": "lower_left", "centre": [-1.5, -s], "all_six_numbers": 15},
        {"name": "upper_left", "centre": [-1.5, s], "all_six_numbers": 25},
        {"name": "lower_right", "centre": [1.5, -s], "all_six_numbers": 25},
    ]
    pieces = [
        {"name": "top_left", "corners": [[-1.5, t], [-0.5, t], [-1.0, h], [-2.0, h]], "number": 15, "count": 4},
        {"name": "top_right", "corners": [[1.5, t], [0.5, t], [1.0, h], [2.0, h]], "number": 25, "count": 4},
        {"name": "left", "corners": [[-3.0, 0], [-2.5, s], [-2.0, 0], [-2.5, -s]], "number": 35, "count": 4},
        {"name": "right", "corners": [[3.0, 0], [2.5, s], [2.0, 0], [2.5, -s]], "number": 35, "count": 4},
        {"name": "bottom_left", "corners": [[-1.5, -t], [-0.5, -t], [-1.0, -h], [-2.0, -h]], "number": 25, "count": 4},
        {"name": "bottom_right", "corners": [[1.5, -t], [0.5, -t], [1.0, -h], [2.0, -h]], "number": 15, "count": 4},
    ]
    return {
        "diagram_type": "tiling_pattern", "aspect_ratio": "15:13", "derived_from": None,
        "content": {"type": "tiling_pattern", "unit": "R = corner radius of a small hexagon = 1.00",
                    "outer_hexagon": {"orientation": "flat_top", "corner_radius": 3.0, "centre": [0, 0], "fill": "SET_A", "outline": "INK",
                                      "corners": [[3, 0], [1.5, t], [-1.5, t], [-3, 0], [-1.5, -t], [1.5, -t]]},
                    "small_hexagons": {"orientation": "flat_top", "corner_radius": 1.0, "fill": "SET_B", "outline": "INK", "outline_px": 2,
                                       "number_colour": "INK", "number_distance_from_centre": 0.68, "list": small},
                    "blue_pieces": {"description": "the six SET_A regions left between the seven small hexagons and the outer hexagon, each a rhombus of side 1.00",
                                    "number_colour": "BG", "number_distance_from_corner": "45 percent of the way from the corner to the piece's centre", "list": pieces},
                    "numbers": {"font": "bold", "digit_height": 0.30, "upright": True},
                    "counts": {"15": 22, "25": 22, "35": 22, "numbers_in_all": 66}},
        "manim_description": (
            "On a plain white BG canvas draw one large regular hexagon with a flat top and a flat bottom, centre (0, 0), corner radius 3.00 units, "
            "corners at (3, 0), (1.5, 2.5981), (-1.5, 2.5981), (-3, 0), (-1.5, -2.5981) and (1.5, -2.5981), filled SET_A with a 2 px INK outline. "
            "On top of it draw seven regular flat-top hexagons of corner radius 1.00 unit, each filled SET_B with a 2 px INK outline, "
            "with centres at (0, 0), (0, 1.7321), (0, -1.7321), (1.5, 0.8660), (1.5, -0.8660), (-1.5, 0.8660) and (-1.5, -0.8660); neighbouring "
            "small hexagons share an edge, so they form a flower. The six SET_A regions that remain between the flower and the large hexagon "
            "are the blue pieces, each a rhombus of side 1.00 unit: top-left (-1.5, 2.5981), (-0.5, 2.5981), (-1.0, 1.7321), (-2.0, 1.7321); "
            "top-right (1.5, 2.5981), (0.5, 2.5981), (1.0, 1.7321), (2.0, 1.7321); left (-3.0, 0), (-2.5, 0.8660), (-2.0, 0), (-2.5, -0.8660); "
            "right (3.0, 0), (2.5, 0.8660), (2.0, 0), (2.5, -0.8660); bottom-left (-1.5, -2.5981), (-0.5, -2.5981), (-1.0, -1.7321), (-2.0, -1.7321); "
            "bottom-right (1.5, -2.5981), (0.5, -2.5981), (1.0, -1.7321), (2.0, -1.7321). Numbers are bold, upright, digit height 0.30 unit. "
            "Each small hexagon holds six numbers in INK, one beside each of its six corners, placed 0.68 unit from the hexagon's centre in the "
            "direction of that corner. Top and bottom hexagons: 35 at every corner. Upper-left and lower-right hexagons: 25 at every corner. "
            "Upper-right and lower-left hexagons: 15 at every corner. Centre hexagon: upper-left corner 15, upper-right corner 25, right corner 35, "
            "lower-right corner 15, lower-left corner 25, left corner 35. Each blue piece holds four equal numbers in BG, one beside each of its four "
            "corners, placed 45 percent of the way from that corner to the piece's centre: top-left piece 15, top-right piece 25, left piece 35, right piece 35, "
            "bottom-left piece 25, bottom-right piece 15. Crop tightly to the large hexagon with a small even margin. Write no letter, total or label."),
        "visible_text": ["15", "25", "35"],
        "must_not_show": STD_NOT + ["the figure letter e", "the total 1650 or any count such as 22",
                                    "a title banner or any logo (the teaching image of this topic has them, this diagram has neither)"],
        "accuracy_checks": ["7 small hexagons x 6 numbers + 6 blue pieces x 4 numbers = 42 + 24 = 66 numbers",
                            "15, 25 and 35 each appear 22 times (15: upper-right 6, lower-left 6, centre 2, top-left piece 4, bottom-right piece 4; "
                            "25: upper-left 6, lower-right 6, centre 2, top-right piece 4, bottom-left piece 4; "
                            "35: top 6, bottom 6, centre 2, left piece 4, right piece 4)",
                            "every blue piece touches the outline of the large hexagon and no number crosses a piece's edge",
                            "check value, not drawn: 22 x 15 + 22 x 25 + 22 x 35 = 22 x 75 = 1650"],
        "alt_text": "A large hexagon made of seven small hexagons and six corner pieces, holding 15s, 25s and 35s, 22 of each.",
        "render_note": "Hardest figure of the chapter: exact counts and positions of the numbers matter more than exact fonts; verify the counts in code before rendering.",
    }


WORKED = [
    ("M3.S27.T27.C166", "3.9.fig_c", "c3_9_fig_c_q", fig_c, "P14-pattern-c", "figure c"),
    ("M3.S27.T27.C167", "3.9.fig_b", "c3_9_fig_b_q", fig_b, "P13-pattern-b", "figure b"),
    ("M3.S27.T27.C169", "3.9.fig_f", "c3_9_fig_f_q", fig_f, "P14-pattern-f", "figure f"),
    ("M3.S27.T27.C170", "3.9.fig_e", "c3_9_fig_e_q", fig_e, "P14-pattern-e", "figure e"),
]


def apply(items, figs, notes):
    by = {(i["lp_concept_id"], i["role"]): i for i in items}

    # 1. solution diagrams: before the first step
    for (cid, role), it in by.items():
        if role == "solution" and it["decision"] == "required":
            it["placeholder"] = {"token": it["placeholder"]["token"], "insert_into": "steps_tex", "position": "before_first_step"}

    # 2. C9: no question diagram; C10 stands alone
    c9 = by[("M1.S3.T3.C9", "question")]
    for k in ("manim_scene", "placeholder", "diagram", "needs_lp_text_sync"):
        c9.pop(k, None)
    c9.update({
        "needs_lp_text_sync": True,          # v3 'refer picture' rule: the question text must name the data
        "decision": "optional", "reason_codes": ["FIG_REFERENCED", "REUSES_CONCEPT_IMAGE"],
        "reason": ("Placement map supplied by the user (21 Nov 2026): optional, no diagram. The book points at the first line-up on page 55 "
                   "(8 children, bubbles 0, 2, 1, 1, 0, 2, 1, 0), which the teaching image M1.S2.T2.C2.IMG1 of the previous topic already shows; "
                   "the solution diagram C10 draws that line-up with the neighbouring pair circled."),
        "text_alternative": "If the question is read away from the teaching image, say in the question text that the line-up is the first line (bubbles 0, 2, 1, 1, 0, 2, 1, 0).",
        "lp_placeholder_action": "drop_image", "media_id": None})
    c10 = by[("M1.S3.T3.C10", "solution")]
    d = c10["diagram"]
    old = "Redraw exactly the question diagram: same eight figures, same heights, same positions and the same bubbles, all in INK. "
    assert d["manim_description"].startswith(old), "C10 description changed"
    d["manim_description"] = "Draw the first line-up of eight children, all bubble digits in INK. " + d["manim_description"][len(old):]
    assert d["alt_text"].startswith("The same row of eight children")
    d["alt_text"] = "A row of eight children " + d["alt_text"][len("The same row of eight children "):]
    d["derived_from"] = None
    c10["reason"] = ("The LP solution points at the third and fourth children of the first line; circling that neighbouring pair on the line-up "
                     "is the evidence for 'Yes'. The book's own answer only says 'refer picture on page 55', and the question (C9) carries no diagram "
                     "of its own in the supplied placement map, so this figure draws the whole line-up (bubbles 0, 2, 1, 1, 0, 2, 1, 0) plus one circle.")

    # 3. the four lettered-figure worked examples become diagrams
    for cid, ncert, scene, fn, figid, name in WORKED:
        it = by[(cid, "worked_example")]
        new = worked(cid, ncert, it["question_text"], scene,
                     "Lettered %s of 3.9: its numbers and their arrangement are the data the learner totals, so the worked example needs the picture. "
                     "Drawn as its own clean diagram, as the placement map supplied by the user (21 Nov 2026) says, instead of pointing at the teaching "
                     "image of this topic (which carries a title banner and a logo)." % name, fn())
        it.clear()
        it.update(new)
        figs[figid]["mapped_to"] = "item:%s (question)" % cid

    # 4. no reuse links any more (v3): the item is a plain 'no image' item, the teaching image stays where it is
    codes = {"M2.S14.T14.C81": ["LATEX_ARITHMETIC"]}
    for it in items:
        if it["lp_placeholder_action"] == "reuse_concept_image":
            rid = it.pop("reuse_media_id")
            it["lp_placeholder_action"] = "drop_image" if it["role"] in ("question", "solution") else "no_image"
            it["reason_codes"] = codes.get(it["lp_concept_id"], ["TEXT_SUFFICIENT"])
            it["reason"] = ("No image, no link (placement map supplied by the user, 21 Nov 2026, and the v3 rules: a teaching image is never linked from a block). "
                            "The teaching image %s of this topic stays where it is. " % rid) + it["reason"]
            it["media_id"] = None

    # figure inventory: the 3.1 line-up is no longer an item figure
    figs["P01-lineup-1"]["mapped_to"] = "concept_image:M1.S2.T2.C2.IMG1"

    # notes
    stale = ("Judgement call: worked examples on figures b, c, e, f", "Concept images C165.IMG1, C168.IMG1 and C168.IMG2 carry a title banner")
    notes[:] = [n for n in notes if not any(s in n for s in stale)]
    notes.append("[supplied placement map, 21 Nov 2026] Placement follows ch3_number_play_diagram_map (1).json: all 17 solution tokens at steps_tex / "
                 "before_first_step; the 3.1 Q3 question (C9) is optional (no diagram); the worked examples on figures b, c, e, f (C167, C166, C170, C169) "
                 "are drawn as new diagrams (specs written from book pages 13-14). Optional items (C9, C14, C30, C97, C173, C175, C210, C212) are not added.")
