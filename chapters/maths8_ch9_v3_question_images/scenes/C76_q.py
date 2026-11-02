from _style import *


class C76_q(Scene):
    def construct(self):
        self.add(header("Question", r"Chapter Exercises, Q9"))

        question = para(r"Find the area of an equilateral triangle with sidelength 6 units.",
                        width=5.6, size=42)
        question.move_to([LEFT_EDGE + question.width / 2, 0, 0])
        self.add(question)

        side = 4.6
        A = np.array([1.2, -2.2, 0])
        B = A + side * RIGHT
        C = A + side * np.array([0.5, 3 ** 0.5 / 2, 0])
        self.add(triangle(A, B, C))
        self.add(side_label(r"6", A, B, [0, -0.4, 0]))
        self.add(side_label(r"6", A, C, [-0.34, 0.2, 0]))
        self.add(side_label(r"6", B, C, [0.34, 0.2, 0]))
