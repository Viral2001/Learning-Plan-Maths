from _style import *


class C27_q(Scene):
    def construct(self):
        self.add(header("Question", r"Isosceles Right Triangles, Q3"))

        question = para(r"The hypotenuse of an isosceles right triangle is 10. What are its other "
                        r"two sidelengths?", width=5.8, size=40)
        question.move_to([LEFT_EDGE + question.width / 2, 0, 0])
        self.add(question)

        R, A, B = [1.6, -2.3, 0], [1.6, 1.6, 0], [5.5, -2.3, 0]
        self.add(triangle(R, A, B), right_mark(R, A, B))
        self.add(side_label(r"?", R, A, [-0.38, 0, 0], color=RED, size=44))
        self.add(side_label(r"?", R, B, [0, -0.4, 0], color=RED, size=44))
        self.add(side_label(r"10", A, B, [0.42, 0.34, 0]))
