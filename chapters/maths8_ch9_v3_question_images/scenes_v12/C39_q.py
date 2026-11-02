from _style import *


class C39_q(Scene):
    def construct(self):
        self.add(header("Question", r"Missing Sides and New Squares, Q3"))

        question = para(r"Using the constructions you have now seen, how would you construct a square "
                        r"whose area is triple the area of a given square?\\[8pt]Five times the area "
                        r"of a given square?\\[8pt](Baudh\={a}yana's \'Sulba-S\={u}tra, Verse 1.10)",
                        width=6.8, size=36)
        question.move_to([LEFT_EDGE + question.width / 2, 0, 0])
        self.add(question)

        given = Square(3.2, color=INK, stroke_width=4, fill_color=SHAPE_FILL, fill_opacity=0.65)
        given.move_to([3.6, 0, 0])
        self.add(given, word(r"given square", 30, INK).move_to(given))
