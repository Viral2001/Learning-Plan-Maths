from _style import *


class C41_sol(Scene):
    def construct(self):
        self.add(header("Solution", r"Missing Sides and New Squares, Q4 (i)"))

        unit = 0.46
        R = np.array([-5.4, -1.7, 0])
        P = R + 5 * unit * UP
        Q = R + 7 * unit * RIGHT
        self.add(triangle(R, P, Q), right_mark(R, P, Q))
        self.add(side_label(r"a = 5", R, P, [-0.66, 0, 0]))
        self.add(side_label(r"b = 7", R, Q, [0, -0.38, 0]))
        self.add(side_label(r"c = \sqrt{74}", P, Q, [0.95, 0.42, 0], color=TEAL))

        work = steps([
            r"Both sides at the right angle are known, so add.",
            r"By Baudh\={a}yana's Theorem, $c^2 = a^2 + b^2$.",
            r"$c^2 = 5^2 + 7^2 = 25 + 49 = 74$, so $c = \sqrt{74}$.",
            r"$8.6^2 = 73.96$ and $8.7^2 = 75.69$,\\ so $8.6 < \sqrt{74} < 8.7$.",
        ], width=7.6, size=28)
        slip = note("Common mistake", r"writing $c = 5 + 7 = 12$. Add the squares, not the sides.",
                    width=7.6)
        ans = answer_box(r"$c = \sqrt{74}$, between 8.6 and 8.7", width=7.6)

        column = VGroup(work, slip, ans).arrange(DOWN, aligned_edge=LEFT, buff=0.26)
        column.move_to([RIGHT_EDGE - column.width / 2, -0.4, 0])
        self.add(column)
