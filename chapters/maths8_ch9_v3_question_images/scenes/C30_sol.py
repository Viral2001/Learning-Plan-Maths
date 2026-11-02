from _style import *


class C30_sol(Scene):
    def construct(self):
        self.add(header("Solution", r"Isosceles Right Triangles, Q2"))

        rule = para(r"By Baudh\={a}yana's Theorem for an isosceles right triangle, $c^2 = 2a^2$.",
                    width=13.2, size=25)
        rule.move_to([0, 2.8, 0])
        self.add(rule)

        parts = [
            ("(i)", 3, 9, 18, 4, 5, "16", "25", "4.2", "4.3", "17.64", "18.49"),
            ("(ii)", 4, 16, 32, 5, 6, "25", "36", "5.6", "5.7", "31.36", "32.49"),
            ("(iii)", 6, 36, 72, 8, 9, "64", "81", "8.4", "8.5", "70.56", "72.25"),
            ("(iv)", 8, 64, 128, 11, 12, "121", "144", "11.3", "11.4", "127.69", "129.96"),
            ("(v)", 9, 81, 162, 12, 13, "144", "169", "12.7", "12.8", "161.29", "163.84"),
        ]
        cards = []
        for tag, a, sq, dbl, lo, hi, los, his, l, h, ls, hs in parts:
            root = r"\sqrt{%d}" % dbl
            cards.append(part_card(
                "%s equal sides %d" % (tag, a),
                [r"Square on a side: $%d \times %d = %d$. On the hypotenuse: $2 \times %d = %d$, so "
                 r"the hypotenuse is $%s$." % (a, a, sq, sq, dbl, root),
                 r"$%d^2 = %s$ and $%d^2 = %s$, so $%d < %s < %d$." % (lo, los, hi, his, lo, root, hi),
                 r"$%s^2 = %s$ and $%s^2 = %s$." % (l, ls, h, hs)],
                r"$%s$ units, with $%s < %s < %s$" % (root, l, root, h),
                height=1.92, size=22, gap=0.04))
        slip = note("Common mistake", r"doubling the side: for (i), writing the hypotenuse as "
                    r"$2 \times 3 = 6$. It is the area that doubles, not the side.",
                    width=6.5, size=25)
        self.add(card_grid(cards, 2.55, gap=0.08))
        slip.move_to(cards[4].get_center() + (cards[4].width + 0.2) * RIGHT)
        self.add(slip)
