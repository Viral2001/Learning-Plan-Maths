from _style import *


class C42_q(Scene):
    def construct(self):
        self.add(header("Question", r"Chapter Exercises, Q2 (a)"))

        question = para(r"Find the missing sidelength in the following right triangle.",
                        width=5.6, size=40)
        question.move_to([LEFT_EDGE + question.width / 2, 0, 0])
        self.add(question)

        # Right angle at the bottom left, sides kept straight
        unit = 0.52
        R = np.array([1.4, -2.3, 0])
        P = R + 7 * unit * UP
        Q = R + 9 * unit * RIGHT
        self.add(triangle(R, P, Q), right_mark(R, P, Q))
        self.add(side_label(r"7", R, P, [-0.38, 0, 0]))
        self.add(side_label(r"9", R, Q, [0, -0.4, 0]))
        self.add(side_label(r"?", P, Q, [0.42, 0.34, 0], color=RED, size=44))
