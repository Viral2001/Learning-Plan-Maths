from _style import *


class C50_q(Scene):
    def construct(self):
        self.add(header("Question", r"Chapter Exercises, Q4"))

        question = para(r"Is the hypotenuse the longest side of a right triangle? Justify your answer.",
                        width=5.8, size=42)
        question.move_to([LEFT_EDGE + question.width / 2, 0, 0])
        self.add(question)

        unit = 0.56
        R = np.array([1.6, -2.2, 0])
        P = R + 6 * unit * UP
        Q = R + 8 * unit * RIGHT
        self.add(triangle(R, P, Q), right_mark(R, P, Q))
        self.add(side_label(r"a", R, P, [-0.34, 0, 0]))
        self.add(side_label(r"b", R, Q, [0, -0.38, 0]))
        c = side_label(r"c", P, Q, [0.34, 0.3, 0])
        self.add(c, word(r"(hypotenuse)", 30, MUTED).next_to(c, RIGHT, buff=0.14))
