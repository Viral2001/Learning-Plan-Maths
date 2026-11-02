from _style import *


class C48_sol(Scene):
    def construct(self):
        self.add(header("Solution", r"Missing Sides and New Squares, Q4"))

        rule = para(r"By Baudh\={a}yana's Theorem, $c^2 = a^2 + b^2$. If $c$ is the missing side, "
                    r"add the squares; if $c$ is given, subtract.", width=13.2, size=26)
        rule.move_to([0, 2.8, 0])
        self.add(rule)

        cards = [
            part_card("(i) $a = 5$, $b = 7$",
                      [r"Both sides at the right angle are known, so add.",
                       r"$c^2 = 5^2 + 7^2 = 25 + 49 = 74$, so $c = \sqrt{74}$.",
                       r"$8.6^2 = 73.96$ and $8.7^2 = 75.69$."],
                      r"$c = \sqrt{74}$, between 8.6 and 8.7", height=1.92, gap=0.05),
            part_card("(ii) $a = 8$, $b = 12$",
                      [r"Both sides at the right angle are known, so add.",
                       r"$c^2 = 8^2 + 12^2 = 64 + 144 = 208$, so $c = \sqrt{208}$.",
                       r"$14.4^2 = 207.36$ and $14.5^2 = 210.25$."],
                      r"$c = \sqrt{208}$, between 14.4 and 14.5", height=1.92, gap=0.05),
            part_card("(iii) $a = 9$, $c = 15$",
                      [r"The hypotenuse $c$ is given, so subtract.",
                       r"$b^2 = 15^2 - 9^2 = 225 - 81 = 144$.",
                       r"$12^2 = 144$, so $b = 12$."],
                      r"$b = 12$", height=1.92, gap=0.05),
            part_card("(iv) $a = 7$, $b = 12$",
                      [r"Both sides at the right angle are known, so add.",
                       r"$c^2 = 7^2 + 12^2 = 49 + 144 = 193$, so $c = \sqrt{193}$.",
                       r"$13.8^2 = 190.44$ and $13.9^2 = 193.21$."],
                      r"$c = \sqrt{193}$, between 13.8 and 13.9", height=1.92, gap=0.05),
            part_card("(v) $a = 1.5$, $b = 3.5$",
                      [r"Both sides at the right angle are known, so add.",
                       r"$c^2 = 1.5^2 + 3.5^2 = 2.25 + 12.25 = 14.5$, so $c = \sqrt{14.5}$.",
                       r"$3.8^2 = 14.44$ and $3.9^2 = 15.21$."],
                      r"$c = \sqrt{14.5}$, between 3.8 and 3.9", height=1.92, gap=0.05),
        ]
        self.add(card_grid(cards, 2.5, gap=0.1))
        slip = note("Common mistake", r"in (iii), adding $9^2 + 15^2$. The hypotenuse is the longest "
                    r"side, so its square is the total: subtract.", width=6.5, size=25)
        slip.move_to(cards[4].get_center() + (cards[4].width + 0.2) * RIGHT)
        self.add(slip)
