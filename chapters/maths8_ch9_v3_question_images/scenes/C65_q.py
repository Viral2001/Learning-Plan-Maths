from _style import *


class C65_q(Scene):
    def construct(self):
        self.add(header("Question", r"Triples, Q2"))

        question = para(r"Does this method yield non-primitive Baudh\={a}yana triples?",
                        width=5.4, size=42)
        question.move_to([LEFT_EDGE + question.width / 2, 0, 0])
        self.add(question)

        # "This method" means nothing on its own in an image, so it is restated here
        method = note("The method", r"take an odd square and call it $2n - 1$. "
                      r"Then $(n - 1)^2 + (2n - 1) = n^2$ gives a triple."
                      r"\\[8pt]For 25: $n = 13$, so $12^2 + 25 = 13^2$, the triple $(5, 12, 13)$.",
                      width=6.4, size=30, fill=SHAPE_FILL, colour=BLUE)
        method.move_to([RIGHT_EDGE - method.width / 2, 0, 0])
        self.add(method)
