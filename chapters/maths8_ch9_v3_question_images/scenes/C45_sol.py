from _style import *


class C45_sol(Scene):
    def construct(self):
        self.add(header("Solution", r"Using Baudh\={a}yana's Theorem, Worked Example"))

        unit = 0.8
        self.add(right_triangle([-5.8, -1.5, 0], 3 * unit, 4 * unit, left=r"3\text{ cm}",
                                bottom=r"4\text{ cm}", hyp=r"c = 5\text{ cm}", solved="hyp", size=32))

        work = steps([
            r"The right angle is between the sides 3~cm and 4~cm, so the hypotenuse is the third side.",
            r"By Baudh\={a}yana's Theorem, $a^2 + b^2 = c^2$.",
            r"$3^2 + 4^2 = 9 + 16 = 25$.",
            r"$c^2 = 25$, and $5^2 = 25$, so $c = 5$.",
        ], width=7.0, size=30, gap=0.2)
        slip = note("Common mistake", r"leaving out the unit. The sides are in cm, so the hypotenuse is in cm.",
                    width=7.0)
        ans = answer_box(r"$c = 5$ cm", width=7.0)

        column = VGroup(work, slip, ans).arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        column.move_to([RIGHT_EDGE - column.width / 2, -0.4, 0])
        self.add(column)
