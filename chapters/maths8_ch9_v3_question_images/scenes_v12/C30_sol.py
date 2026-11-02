from _style import *


class C30_sol(Scene):
    def construct(self):
        self.add(header("Solution", r"Isosceles Right Triangles, Q3"))

        # Two of the triangles make a square, with the hypotenuse as its diagonal
        A, B, C, D = [-5.5, -1.8, 0], [-2.5, -1.8, 0], [-2.5, 1.2, 0], [-5.5, 1.2, 0]
        self.add(Polygon(A, B, C, color=INK, stroke_width=4, fill_color=SHAPE_FILL, fill_opacity=0.65))
        self.add(Polygon(A, C, D, color=INK, stroke_width=4, fill_color=TEAL_BG, fill_opacity=0.8))
        self.add(right_mark(B, A, C), right_mark(D, A, C))
        self.add(side_label(r"10", A, C, [0.3, -0.3, 0]))
        self.add(side_label(r"\sqrt{50}", A, B, [0, -0.42, 0], color=TEAL))
        self.add(side_label(r"\sqrt{50}", A, D, [-0.62, 0, 0], color=TEAL))

        work = steps([
            r"Two such triangles make a square whose diagonal is the hypotenuse, 10.",
            r"The square on the hypotenuse has area $10 \times 10 = 100$.",
            r"The square made of the two triangles has half that area: $100 \div 2 = 50$.",
            r"Its side is an equal side of the triangle,\\ so each equal side is $\sqrt{50}$.",
            r"$7^2 = 49$ and $8^2 = 64$, so $7 < \sqrt{50} < 8$.",
            r"$7.07^2 = 49.9849$ and $7.08^2 = 50.1264$,\\ so $7.07 < \sqrt{50} < 7.08$.",
        ], width=7.6, size=26, gap=0.16)
        slip = note("Common mistake", r"taking each side as $10 \div 2 = 5$. Halve the area, not the length.",
                    width=7.6, size=25)
        ans = answer_box(r"each of the other two sides is $\sqrt{50}$, between 7.07 and 7.08",
                         width=7.6, size=28)

        column = VGroup(work, slip, ans).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        column.move_to([RIGHT_EDGE - column.width / 2, -0.45, 0])
        self.add(column)
