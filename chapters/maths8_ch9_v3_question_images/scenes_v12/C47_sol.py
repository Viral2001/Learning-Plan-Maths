from _style import *


class C47_sol(Scene):
    def construct(self):
        self.add(header("Solution", r"Chapter Exercises, Q2"))

        rule = para(r"By Baudh\={a}yana's Theorem, $c^2 = a^2 + b^2$, where $c$ faces the right angle. "
                    r"Add if $c$ is missing; subtract if it is given.", width=13.2, size=25)
        rule.move_to([0, 2.8, 0])
        self.add(rule)

        def fig(up, across, left, bottom, hyp, solved):
            return right_triangle([0, 0, 0], up, across, left=left, bottom=bottom, hyp=hyp, size=24,
                                  solved=solved)

        look = dict(height=1.95, size=21, gap=0.03)
        cards = [
            part_card("(a) sides 7 and 9 at the right angle",
                      [r"The missing side faces the right angle: the hypotenuse.",
                       r"$c^2 = 7^2 + 9^2 = 49 + 81 = 130$, so $c = \sqrt{130}$.",
                       r"$11.4^2 = 129.96$ and $11.5^2 = 132.25$."],
                      r"$\sqrt{130}$, between 11.4 and 11.5",
                      figure=fig(0.77, 0.99, "7", "9", r"\sqrt{130}", "hyp"), **look),
            part_card("(b) sides 4 and 10 at the right angle",
                      [r"The missing side is the hypotenuse.",
                       r"$c^2 = 4^2 + 10^2 = 16 + 100 = 116$, so $c = \sqrt{116}$.",
                       r"$10.7^2 = 114.49$ and $10.8^2 = 116.64$."],
                      r"$\sqrt{116}$, between 10.7 and 10.8",
                      figure=fig(0.48, 1.2, "4", "10", r"\sqrt{116}", "hyp"), **look),
            part_card("(c) side 40, hypotenuse 41",
                      [r"41 faces the right angle, so it is the hypotenuse; subtract.",
                       r"$41^2 - 40^2 = 1681 - 1600 = 81$.",
                       r"$9^2 = 81$, so the missing side is 9."],
                      r"9",
                      figure=fig(0.3, 1.34, "9", "40", "41", "left"), **look),
            part_card(r"(d) side 10, hypotenuse $\sqrt{200}$",
                      [r"$\sqrt{200}$ faces the right angle, so it is the hypotenuse; subtract.",
                       r"$(\sqrt{200})^2 - 10^2 = 200 - 100 = 100$.",
                       r"$10^2 = 100$, so the missing side is 10: the triangle is isosceles."],
                      r"10",
                      figure=fig(0.95, 0.95, "10", "10", r"\sqrt{200}", "left"), **look),
            part_card(r"(e) sides 10 and $\sqrt{150}$ at the right angle",
                      [r"The missing side is the hypotenuse.",
                       r"$c^2 = 10^2 + (\sqrt{150})^2 = 100 + 150 = 250$, so $c = \sqrt{250}$.",
                       r"$15.8^2 = 249.64$ and $15.9^2 = 252.81$."],
                      r"$\sqrt{250}$, between 15.8 and 15.9",
                      figure=fig(0.8, 0.98, "10", r"\sqrt{150}", r"\sqrt{250}", "hyp"), **look),
            part_card("(f) side 27, hypotenuse 45",
                      [r"45 is the hypotenuse, so subtract.",
                       r"$45^2 - 27^2 = 2025 - 729 = 1296$.",
                       r"$36^2 = 1296$, so the missing side is 36."],
                      r"36",
                      figure=fig(0.75, 1.0, "27", "36", "45", "bottom"), **look),
        ]
        self.add(card_grid(cards, 2.55, gap=0.07))
