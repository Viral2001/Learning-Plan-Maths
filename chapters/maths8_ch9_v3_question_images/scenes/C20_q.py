from _style import *


class C20_q(Scene):
    def construct(self):
        self.add(header("Question", r"Isosceles Right Triangles, Example 1"))

        question = para(r"Find the hypotenuse of an isosceles right triangle whose equal sides have "
                        r"length 12.", width=6.3, size=38)
        question.move_to([LEFT_EDGE + question.width / 2, 0, 0])
        self.add(question)

        self.add(right_triangle([1.4, -2.0, 0], 3.8, 3.8, left=r"12", bottom=r"12", hyp=r"?", size=42))
