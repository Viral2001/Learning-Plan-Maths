from _style import *


class C67_q(Scene):
    def construct(self):
        self.add(header("Question", r"Chapter Exercises, Q5"))

        question = para(r"\textbf{True or False:} Every Baudh\={a}yana triple is either a primitive "
                        r"triple or a scaled version of a primitive triple.", width=10.4, size=46)
        question.move_to([0, -0.2, 0])
        self.add(question)
