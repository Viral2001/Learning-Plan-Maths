from _style import *


class C21_q(Scene):
    def construct(self):
        self.add(header("Question", r"Isosceles Right Triangles, Example 2"))

        question = para(r"If the hypotenuse of an isosceles right triangle is $\sqrt{72}$, find its "
                        r"other two sides.", width=6.3, size=38)
        question.move_to([LEFT_EDGE + question.width / 2, 0, 0])
        self.add(question)

        self.add(right_triangle([1.4, -2.0, 0], 3.8, 3.8, left=r"?", bottom=r"?", hyp=r"\sqrt{72}", size=42))
