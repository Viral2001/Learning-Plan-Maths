from _style import *


class C49_q(Scene):
    def construct(self):
        self.add(header("Question", r"Chapter Exercises, Q2"))

        question = word(r"Find the missing sidelengths in the following right triangles:", 36)
        question.move_to([LEFT_EDGE + question.width / 2, 2.6, 0])
        self.add(question)

        figures = [
            ("(a)", [-5.7, 0.3], 7 * 0.2, 9 * 0.2, r"7", r"9", r"?"),
            ("(b)", [-1.2, 0.3], 4 * 0.17, 10 * 0.17, r"4", r"10", r"?"),
            ("(c)", [2.6, 0.3], 9 * 0.075, 40 * 0.075, r"?", r"40", r"41"),
            ("(d)", [-5.7, -2.9], 10 * 0.17, 10 * 0.17, r"?", r"10", r"\sqrt{200}"),
            ("(e)", [-1.2, -2.9], 10 * 0.15, 12.25 * 0.15, r"10", r"\sqrt{150}", r"?"),
            ("(f)", [2.6, -2.9], 27 * 0.058, 36 * 0.058, r"27", r"?", r"45"),
        ]
        for tag, R, up, across, left, bottom, hyp in figures:
            self.add(word(tag, 32, INK).move_to([R[0] - 0.75, R[1] + 1.75, 0]))
            self.add(right_triangle([R[0], R[1], 0], up, across, left=left, bottom=bottom, hyp=hyp, size=34))
