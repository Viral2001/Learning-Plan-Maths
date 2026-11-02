from _style import *


class C41_sol(Scene):
    def construct(self):
        self.add(header("Solution", r"Chapter Exercises, Q7"))

        unit = 0.48
        b = 24 ** 0.5 * unit
        R = np.array([-4.0, -1.8, 0])
        P = R + b * UP
        Q = R + 5 * unit * RIGHT

        # The wanted square stands on the third side
        square = Polygon(R, P, P + b * LEFT, R + b * LEFT, color=TEAL, stroke_width=4,
                         fill_color=TEAL_BG, fill_opacity=0.8)
        self.add(square, triangle(R, P, Q), right_mark(R, P, Q))
        self.add(MathTex(r"\text{area } 24", font_size=34, color=TEAL).move_to(square))
        self.add(MathTex(r"b", font_size=34, color=TEAL).move_to(R + b / 2 * UP + 0.22 * RIGHT))
        self.add(side_label(r"5", R, Q, [0, -0.36, 0]))
        self.add(side_label(r"7", P, Q, [0.34, 0.26, 0]))
        self.add(Arc(radius=7 * unit, start_angle=118 * DEGREES, angle=34 * DEGREES,
                     arc_center=Q, color=MUTED, stroke_width=3))

        work = steps([
            r"The areas are $7^2 = 49$ and $5^2 = 25$, and $49 - 25 = 24$.",
            r"Draw a side of 5 units, a right angle at one end, and swing an arc of radius 7 "
            r"from the other end to meet the perpendicular: a right triangle with hypotenuse 7 "
            r"and one side 5.",
            r"By Baudh\={a}yana's Theorem, its third side $b$ has $b^2 = 7^2 - 5^2$, which is 24.",
            r"The square on that third side has area 24 square units.",
        ], width=7.6, size=27)
        slip = note("Common mistake", r"using $7 - 5 = 2$ as the side. Subtract the areas, not the sides.",
                    width=7.6)
        ans = answer_box(r"the square on the third side of the right triangle with hypotenuse 7 "
                         r"and one side 5: area 24 square units", width=7.6, size=28)

        column = VGroup(work, slip, ans).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        column.move_to([RIGHT_EDGE - column.width / 2, -0.45, 0])
        self.add(column)
