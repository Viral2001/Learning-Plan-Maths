from _style import *


class C68_sol(Scene):
    def construct(self):
        self.add(header("Solution", r"Chapter Exercises, Q6"))

        A, B, C, D = [-5.6, 0.45, 0], [-3.2, 0.45, 0], [-3.2, 2.25, 0], [-5.6, 2.25, 0]
        self.add(Polygon(A, B, C, D, color=INK, stroke_width=4, fill_color=SHAPE_FILL, fill_opacity=0.65))
        self.add(Line(A, C, color=TEAL, stroke_width=4))
        self.add(side_label(r"4", A, B, [0, -0.3, 0], size=30))
        self.add(side_label(r"3", B, C, [0.26, 0, 0], size=30))
        self.add(side_label(r"5", A, C, [-0.18, 0.26, 0], size=30, color=TEAL))

        table = grid_table([
            [r"Rectangle", r"Diagonal"],
            [r"3 by 4", "5"],
            [r"6 by 8", "10"],
            [r"5 by 12", "13"],
            [r"8 by 15", "17"],
            [r"7 by 24", "25"],
        ], widths=[2.3, 2.0], row_h=0.52, size=27, colours={1: TEAL})
        table.move_to([LEFT_EDGE + 0.1 + table.width / 2, -1.85, 0])
        self.add(table)

        work = steps([
            r"The diagonal of a rectangle is the hypotenuse of the right triangle made by two of its sides.",
            r"So the two sides and the diagonal must form a Baudh\={a}yana triple.",
            r"$3^2 + 4^2 = 5^2$, $6^2 + 8^2 = 10^2$, $5^2 + 12^2 = 13^2$, $8^2 + 15^2 = 17^2$, "
            r"$7^2 + 24^2 = 25^2$.",
        ], width=7.6, size=28)
        ans = answer_box(r"3 by 4 (diagonal 5), 6 by 8 (10), 5 by 12 (13), 8 by 15 (17), 7 by 24 (25)",
                         width=7.6, size=28)
        slip = note("Common mistake", r"using the longest number of a triple as a side. "
                    r"For $(3, 4, 5)$, the rectangle is 3 by 4, and 5 is the diagonal.",
                    width=7.6, size=25)

        column = VGroup(work, ans, slip).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        column.move_to([RIGHT_EDGE - column.width / 2, -0.4, 0])
        self.add(column)
