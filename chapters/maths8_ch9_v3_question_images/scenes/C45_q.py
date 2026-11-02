from _style import *


class C45_q(Scene):
    def construct(self):
        self.add(header("Question", r"Using Baudh\={a}yana's Theorem, Worked Example"))

        question = para(r"A right-angled triangle has shorter sides 3 cm and 4 cm. Find the hypotenuse.",
                        width=6.3, size=38)
        question.move_to([LEFT_EDGE + question.width / 2, 0, 0])
        self.add(question)

        unit = 0.95
        self.add(right_triangle([1.1, -1.8, 0], 3 * unit, 4 * unit, left=r"3\text{ cm}",
                                bottom=r"4\text{ cm}", hyp=r"?", size=40))
