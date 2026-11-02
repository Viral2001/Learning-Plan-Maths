from _style import *


class C44_sol(Scene):
    def construct(self):
        self.add(header("Solution", r"Missing Sides and New Squares, Q1"))

        unit = 0.36
        self.add(right_triangle([-6.0, -1.0, 0], 5 * unit, 12 * unit, left=r"5", bottom=r"12",
                                hyp=r"c = 13", solved="hyp", size=34))

        work = steps([
            r"Draw sides of 5 cm and 12 cm at a right angle and join their ends; the join "
            r"measures about 13 cm.",
            r"Both shorter sides are known, so add their squares.",
            r"By Baudh\={a}yana's Theorem, $c^2 = a^2 + b^2$.",
            r"$c^2 = 5^2 + 12^2 = 25 + 144 = 169$.",
            r"$13^2 = 169$, so $c = 13$.",
        ], width=7.4, size=28)
        slip = note("Common mistake", r"writing $c = 5 + 12 = 17$. Add the squares, not the sides.",
                    width=7.4)
        ans = answer_box(r"13 cm", width=7.4)

        column = VGroup(work, slip, ans).arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        column.move_to([RIGHT_EDGE - column.width / 2, -0.4, 0])
        self.add(column)
