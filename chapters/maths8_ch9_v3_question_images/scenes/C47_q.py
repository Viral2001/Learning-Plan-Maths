from _style import *


class C47_q(Scene):
    def construct(self):
        self.add(header("Question", r"Missing Sides and New Squares, Q2"))

        question = para(
            r"If a right-angled triangle has a short side of length 8 cm and hypotenuse of "
            r"length 17 cm, what is the length of the third side?"
            r"\\[8pt]Again, try drawing the triangle and measuring, and then check your answer "
            r"using Baudh\={a}yana's Theorem.",
            width=6.2, size=36)
        question.move_to([LEFT_EDGE + question.width / 2, -0.2, 0])
        self.add(question)

        # 8 and the unknown side meet at the right angle at R
        R, A, B = [1.8, -2.4, 0], [1.8, 0.9, 0], [6.0, -2.4, 0]
        self.add(triangle(R, A, B), right_mark(R, A, B))
        self.add(side_label(r"8\text{ cm}", R, A, [-0.72, 0, 0]))
        self.add(side_label(r"17\text{ cm}", A, B, [0.62, 0.34, 0]))
        self.add(side_label(r"?", R, B, [0, -0.36, 0], color=RED, size=44))
