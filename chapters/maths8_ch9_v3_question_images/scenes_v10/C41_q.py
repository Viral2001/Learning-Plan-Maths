from _style import *


class C41_q(Scene):
    def construct(self):
        self.add(header("Question", r"Missing Sides and New Squares, Q4 (i)"))

        question = para(r"Let $a$, $b$ and $c$ denote the length of the sides of a right triangle, "
                        r"with $c$ being the length of the hypotenuse. Find the missing sidelength "
                        r"in the following case:\\[8pt](i) $a = 5$, $b = 7$",
                        width=6.2, size=36)
        question.move_to([LEFT_EDGE + question.width / 2, 0, 0])
        self.add(question)

        unit = 0.62
        R = np.array([1.4, -2.2, 0])
        P = R + 5 * unit * UP
        Q = R + 7 * unit * RIGHT
        self.add(triangle(R, P, Q), right_mark(R, P, Q))
        self.add(side_label(r"a = 5", R, P, [-0.72, 0, 0]))
        self.add(side_label(r"b = 7", R, Q, [0, -0.4, 0]))
        self.add(side_label(r"c = {?}", P, Q, [0.7, 0.42, 0], color=RED))
