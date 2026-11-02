from _style import *


class C42_sol(Scene):
    def construct(self):
        self.add(header("Solution", r"Chapter Exercises, Q2 (a)"))

        unit = 0.36
        R = np.array([-5.5, -1.7, 0])
        P = R + 7 * unit * UP
        Q = R + 9 * unit * RIGHT
        self.add(triangle(R, P, Q), right_mark(R, P, Q))
        self.add(side_label(r"7", R, P, [-0.34, 0, 0]))
        self.add(side_label(r"9", R, Q, [0, -0.36, 0]))
        self.add(side_label(r"c = \sqrt{130}", P, Q, [0.95, 0.42, 0], color=TEAL))

        work = steps([
            r"The right angle is between the sides 7 and 9, so the missing side faces it: "
            r"the hypotenuse.",
            r"By Baudh\={a}yana's Theorem, $c^2 = a^2 + b^2$.",
            r"$c^2 = 7^2 + 9^2 = 49 + 81 = 130$, so $c = \sqrt{130}$.",
            r"$11.4^2 = 129.96$ and $11.5^2 = 132.25$,\\ so $11.4 < \sqrt{130} < 11.5$.",
        ], width=7.6, size=28)
        slip = note("Common mistake", r"writing $c = 7 + 9 = 16$. Add the squares, not the sides.",
                    width=7.6)
        ans = answer_box(r"$c = \sqrt{130}$, between 11.4 and 11.5", width=7.6)

        column = VGroup(work, slip, ans).arrange(DOWN, aligned_edge=LEFT, buff=0.26)
        column.move_to([RIGHT_EDGE - column.width / 2, -0.4, 0])
        self.add(column)
