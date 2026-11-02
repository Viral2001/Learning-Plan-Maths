from _style import *


class C22_sol(Scene):
    def construct(self):
        self.add(header("Solution", r"Chapter Exercises, Q1"))

        s = 3.2
        A = np.array([-5.6, -1.9, 0])
        B, C, D = A + s * RIGHT, A + s * RIGHT + s * UP, A + s * UP
        self.add(Polygon(B, C, D, color=INK, stroke_width=4, fill_opacity=0))
        self.add(triangle(A, B, D), right_mark(A, B, D))
        self.add(MathTex(r"5", font_size=34, color=INK).next_to(Line(A, B), DOWN, buff=0.14))
        self.add(MathTex(r"5", font_size=34, color=INK).next_to(Line(A, D), LEFT, buff=0.14))
        self.add(MathTex(r"c = \sqrt{50}", font_size=34, color=TEAL)
                 .move_to((B + D) / 2 + [0.72, 0.5, 0]))

        work = steps([
            r"The diagonal cuts the square into two isosceles right triangles with equal sides 5 cm.",
            r"By Baudh\={a}yana's Theorem for an isosceles right triangle, $c^2 = 2a^2$.",
            r"The diagonal is their hypotenuse: $c^2 = 2 \times 5^2 = 2 \times 25 = 50$.",
            r"So $c = \sqrt{50}$.",
            r"$7.07^2 = 49.9849$ and $7.08^2 = 50.1264$, so $7.07 < \sqrt{50} < 7.08$.",
        ], width=7.6, size=28)
        slip = note("Common mistake", r"writing $c = 5 + 5 = 10$. Add the squares, not the sides.",
                    width=7.6)
        ans = answer_box(r"$\sqrt{50}$ cm, about 7.07 cm", width=7.6)

        column = VGroup(work, slip, ans).arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        column.move_to([RIGHT_EDGE - column.width / 2, -0.4, 0])
        self.add(column)
