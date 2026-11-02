from _style import *


class C46_q(Scene):
    def construct(self):
        self.add(header("Question", r"Missing Sides and New Squares, Q1"))

        question = para(r"If a right-angled triangle has shorter sides of lengths 5 cm and 12 cm, then "
                        r"what is the length of its hypotenuse?\\[8pt]First draw the right-angled "
                        r"triangle with these sidelengths and measure the hypotenuse, then check your "
                        r"answer using Baudh\={a}yana's Theorem.", width=6.3, size=34)
        question.move_to([LEFT_EDGE + question.width / 2, 0, 0])
        self.add(question)

        unit = 0.46
        self.add(right_triangle([0.9, -1.3, 0], 5 * unit, 12 * unit, left=r"5\text{ cm}",
                                bottom=r"12\text{ cm}", hyp=r"?"))
