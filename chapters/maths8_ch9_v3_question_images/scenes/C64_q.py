from _style import *


class C64_q(Scene):
    def construct(self):
        self.add(header("Question", r"Triples, Q1"))

        question = para(r"Find 5 more Baudh\={a}yana triples using this idea.", width=13, size=40)
        question.move_to([LEFT_EDGE + question.width / 2, 2.3, 0])
        self.add(question)

        body = para(r"\textbf{The idea.} For any counting number $n$, "
                    r"$(n - 1)^2 + (2n - 1) = n^2$. "
                    r"If the $n$th odd number, $2n - 1$, is also a square number, we get a sum of two "
                    r"square numbers equal to another square number.", width=12.4, size=32)
        book = VGroup(
            word(r"$9 = 2 \times 5 - 1$, so $n = 5$: \quad $4^2 + 3^2 = 5^2$", 34),
            word(r"$25 = 2 \times 13 - 1$, so $n = 13$: \quad $12^2 + 5^2 = 13^2$", 34),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        block = VGroup(body, book).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        panel = RoundedRectangle(corner_radius=0.14, width=13.2, height=block.height + 0.5,
                                 fill_color=SHAPE_FILL, fill_opacity=0.4, stroke_color=BLUE, stroke_width=1.5)
        panel.move_to([0, -0.45, 0])
        block.move_to(panel)
        self.add(panel, block)
