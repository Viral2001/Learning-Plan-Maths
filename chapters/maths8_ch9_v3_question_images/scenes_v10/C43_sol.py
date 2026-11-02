from _style import *


class C43_sol(Scene):
    def construct(self):
        self.add(header("Solution", r"Chapter Exercises, Q4"))

        unit = 0.42
        R = np.array([-5.5, -1.6, 0])
        P = R + 6 * unit * UP
        Q = R + 8 * unit * RIGHT
        self.add(triangle(R, P, Q), right_mark(R, P, Q))
        self.add(side_label(r"a", R, P, [-0.32, 0, 0]))
        self.add(side_label(r"b", R, Q, [0, -0.36, 0]))
        self.add(side_label(r"c", P, Q, [0.32, 0.28, 0], color=TEAL))

        work = steps([
            r"In a right triangle, by Baudh\={a}yana's Theorem,\\ $c^2 = a^2 + b^2$.",
            r"$b^2$ is more than 0, so $c^2$ is more than $a^2$, and so $c$ is more than $a$.",
            r"In the same way $c^2$ is more than $b^2$, so $c$ is more than $b$.",
            r"So the hypotenuse is longer than each of the other two sides.",
        ], width=7.6, size=28)
        slip = note("Common mistake", r"testing only one triangle, such as 3, 4, 5. The reason must "
                    r"work for every right triangle.", width=7.6)
        ans = answer_box(r"Yes: $c^2 = a^2 + b^2$ is bigger than $a^2$ and bigger than $b^2$, so $c$ "
                         r"is the longest side", width=7.6, size=28)

        column = VGroup(work, slip, ans).arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        column.move_to([RIGHT_EDGE - column.width / 2, -0.4, 0])
        self.add(column)
