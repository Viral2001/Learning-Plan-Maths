from _style import *


class C73_q(Scene):
    def construct(self):
        self.add(header("Question", r"A Problem from Bh\={a}skar\={a}ch\={a}rya's L\={\i}l\={a}vat\={\i}, Worked Example"))

        question = para(r"A lotus tip is 1 unit above the water. Swayed by the breeze, the tip touches "
                        r"the water 3 units from its original position. Find the depth of the lake.",
                        width=6.0, size=36)
        question.move_to([LEFT_EDGE + question.width / 2, 0, 0])
        self.add(question)

        self.add(lotus_figure([2.3, 1.2, 0]))
