# -*- coding: utf-8 -*-
"""Chapter-level content for Class 8 Chapter 11, Exploring Some Geometric Themes (Ganita Prakash Grade 8 Part II,
Chapter 4). Book lines elsewhere are verbatim except: the book's dashes become commas, colons or "to"; minus is U+2212;
subscripts and powers are written out (R sub n is written Rn, 8 to the power n is written 8 to the power n)."""
from __future__ import annotations

CHAPTER = {
    "grade": 8,
    "label": "Class 8",
    "chapter_no": 11,
    "name": "Exploring Some Geometric Themes",
    "book_part": "Ganita Prakash Grade 8 Part II, Chapter 4",
    "source_pdf": "textbooks/class8/hegp204.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Fractals: Shapes Within Shapes",
     "Self-similar shapes in nature and in mathematics. The Sierpinski Carpet, the Sierpinski Triangle and the Koch "
     "Snowflake are built by repeating one rule; counting squares, holes, sides, area and perimeter step by step "
     "turns each picture into a pattern of numbers. Fractals in temples, blankets and prints close the module."),
    ("M2", "Visualising and Making Solids",
     "Building shapes in the imagination, profiles of solids from different viewpoints, faces, edges and vertices of "
     "prisms and pyramids, nets of the cube, cuboid, tetrahedron, cylinder, cone and octahedron, and the shortest "
     "path for an ant on the surface of a box found by unfolding it."),
    ("M3", "Projections, Shadows and Isometric Drawing",
     "Projections of points, lines, flat shapes and solids; front, top and side views; shadows as projections and "
     "the fact that parallel lines stay parallel; the isometric projection of a cube and drawing solids on an "
     "isometric grid, ending with impossible figures and a closing summary."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter follows the book's own order: fractals first, then solids. Each fractal is built one step at "
             "a time and its counts are predicted before they are revealed, so a picture becomes a rule (multiply by 8, "
             "multiply by 4). Solids are first pictured in the mind, then cut, unfolded, flattened onto a plane and "
             "finally drawn on an isometric grid.",
    "points": [
        {"title": "Predict, then check",
         "text": "Each idea opens with a question answered before the reveal: how many squares at the next step, will "
                 "this shape fold into a cube, is this path really the shortest."},
        {"title": "Imagine before you handle",
         "text": "The book asks students to visualise first and only then use cutouts. The plan keeps that order: the "
                 "video asks for a mental picture, and a tool appears only where handling the shape is the idea."},
        {"title": "Tools only where manipulation is the concept",
         "text": "Ten tools, each used once: stepping three fractals, counting the parts of solids, folding and "
                 "rolling nets, unfolding a box to find a path, tilting a solid to see its projection, turning a solid "
                 "to read its views, and stacking cubes on an isometric grid. Topics about ideas carry no tool."},
        {"title": "Many right answers",
         "text": "Profiles, projections and nets rarely have one answer. Students are asked for more than one solid "
                 "that fits a view, and for every unfolding before choosing the shortest path."},
    ],
}

NCERT_ITEMS = [
    "opening", "4.1.nature",
    # Sierpinski Carpet (pp 70 to 71)
    "4.1.carpet_steps", "4.1.carpet_pattern", "4.1.carpet_Rn", "4.1.carpet_holes",
    # Sierpinski Gasket (p 72)
    "4.1.gasket_construct", "4.1.gasket_identical",
    "FiO1.q1", "FiO1.q2", "FiO1.q3",
    # Koch Snowflake (p 73)
    "4.1.koch",
    "FiO2.q1", "FiO2.q2", "FiO2.q3",
    # Fractals in Art (pp 74 to 75)
    "4.1.art",
    # 4.2 Build it in your imagination (pp 75 to 76)
    "4.2.imagine_intro", "4.2.imagine_square", "4.2.imagine_triangle", "4.2.imagine_octagon",
    # Profiles (pp 76 to 77)
    "4.2.profile_intro", "4.2.profile_square", "4.2.profile_circle", "4.2.profile_triangle",
    "4.2.profile_pairs", "4.2.profile_unique",
    # Making solids, faces, edges, vertices, prisms and pyramids (pp 77 to 79)
    "4.2.solids_make", "4.2.fev_cube", "4.2.prism_def", "4.2.pyramid_def", "4.2.prism_count", "4.2.pyramid_count",
    # Nets (pp 79 to 84)
    "4.2.net_def", "4.2.net_fold", "4.2.net_practical",
    "FiO3.q1", "FiO3.q2", "FiO3.q3",
    "4.2.tetra_nets", "4.2.mt_tetra_pyramid", "4.2.cyl_net", "4.2.cone_net", "4.2.mt_oblique_cone",
    "4.2.prism_net", "4.2.octa_net", "4.2.dodeca", "4.2.sphere_net",
    # Shortest paths on a cube (pp 84 to 87)
    "4.2.path_cube", "4.2.path_edge", "4.2.path_sure", "4.2.path_cuboid", "4.2.path_try",
    # Projections (pp 87 to 92)
    "4.2.proj_point", "4.2.proj_line", "4.2.proj_compare", "4.2.mt_proj_square", "4.2.mt_proj_parallelogram",
    "4.2.mt_proj_polygon", "4.2.proj_solids", "4.2.proj_same", "4.2.proj_cone_same", "4.2.views", "4.2.views_fig46",
    "FiO4.q1", "FiO4.q2", "FiO4.q3",
    # Shadows (pp 94 to 95)
    "4.2.shadow_torch", "4.2.shadow_why", "4.2.shadow_sun", "4.2.shadow_parallel",
    "FiO5.q1", "FiO5.q2", "FiO5.q3", "FiO5.q4", "FiO5.q5", "FiO5.q6",
    # Isometric projections and drawing (pp 97 to 100)
    "4.2.iso_cube", "4.2.mt_iso_equal", "4.2.iso_grid",
    "4.2.tetris", "4.2.iso_axes_cube", "4.2.iso_row", "4.2.iso_why", "4.2.iso_others",
    "FiO6.q1", "FiO6.q2", "FiO6.q3", "FiO6.q4",
    "summary",
]

MISCONCEPTIONS = [
    ("M_FRACTAL_ADD", "Each step of the carpet adds 8 squares, so the count goes 1, 9, 17 instead of multiplying by 8."),
    ("M_HOLES_EQUAL", "The number of holes equals the number of squares removed at the latest step only."),
    ("M_AREA_GROWS", "A fractal with more and more pieces must have more and more area."),
    ("M_KOCH_SIDES", "Each Koch step adds 3 sides, instead of turning every side into 4."),
    ("M_ONE_PROFILE", "A given outline can come from only one solid."),
    ("M_PRISM_PYRAMID", "A prism and a pyramid with the same base have the same number of faces, edges and vertices."),
    ("M_ANY_SIX", "Any arrangement of six joined squares folds into a cube."),
    ("M_CYL_RECT", "The rectangle in a cylinder's net is as wide as the circle's diameter, not its circumference."),
    ("M_STRAIGHT_BOX", "The shortest path on a box is the path that looks straight on the box, whatever the unfolding."),
    ("M_PROJ_LONGER", "A projection of a line can be longer than the line itself."),
    ("M_PROJ_ANY", "The projection of a parallelogram can be any quadrilateral."),
    ("M_SHADOW_SIZE", "A shadow is always the same size as the object."),
    ("M_ISO_PERSPECTIVE", "On an isometric drawing, edges further away should be drawn shorter."),
]

SOLUTION_NOTES = [
    "Cube nets (Figure it Out on nets, question 1), read from the six figures: (ii) the 3 and 3 staircase, (iii) "
    "the 2, 2, 2 staircase, (iv) and (vi) the 1, 4, 1 crosses fold into a cube; (i) and (v) do not, because both "
    "extra squares sit on the same side of the row of four.",
    "Regular tetrahedron nets: only the large triangle of four and the strip of four fold. The shape with four "
    "triangles meeting at one point fails, and the last shape has five triangles.",
    "Stack of cubes (Figure it Out on shadows and views, question 5): 10 cubes are visible; the picture is a corner "
    "staircase, so the hidden cubes that hold up the upper layers give layers of 1, 3, 6 and 10, a total of 20.",
    "Figure-based items (matching objects with views, cube combinations, which solid fits three views, solids from "
    "projections, impossible figures) are answered by method in the plan; the exact pictures must be read from the "
    "book figure.",
]
ERRATA = []

DESIGN_REFERENCES = [
    {"text": "docs/25_new_design_learning_plan_playbook.md: framing intro, idea topics each ending in a practice "
             "concept, a question topic after each idea topic with exercises, and one summary topic.", "url": ""},
]

FIGURES = {}
