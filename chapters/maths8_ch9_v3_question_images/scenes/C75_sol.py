from _style import *


class C75_sol(Scene):
    def construct(self):
        self.add(header("Solution", r"Chapter Exercises, Q8"))

        slip = note("Common mistake", r"counting only upright squares. Tilted squares, as in (a) and (d), "
                    r"count too.", width=13.2, size=25)
        self.add(slip.move_to([0, 2.78, 0]))

        panels = [
            ("(a) area 2", -6.3, [(1, 0), (2, 1), (1, 2), (0, 1)]),
            ("(b) area 3", -3.0, None),
            ("(c) area 4", 0.3, [(1, 1), (3, 1), (3, 3), (1, 3)]),
            ("(d) area 5", 3.6, [(1, 0), (3, 1), (2, 3), (0, 2)]),
        ]
        for label, x, corners in panels:
            origin = [x, 0.62]
            self.add(dot_grid(origin, gap=0.42))
            if corners:
                self.add(grid_square(origin, corners, gap=0.42))
            else:
                text = word(r"\textbf{not possible}", 22, RED)
                text.move_to([x + 0.84, 1.46, 0])
                self.add(BackgroundRectangle(text, color=WHITE, fill_opacity=1, buff=0.06), text)
            self.add(word(label, 26, INK).move_to([x + 2.5, 1.46, 0]))

        first = part_card("(i)", [
            r"A square with its corners on grid dots has a side that goes $p$ dots across and $q$ "
            r"dots up, so by Baudh\={a}yana's Theorem its area is $p^2 + q^2$.",
            r"(a) $p = 1$, $q = 1$: $1^2 + 1^2 = 2$, a tilted square of area 2.",
            r"(c) $p = 2$, $q = 0$: an upright 2 by 2 square, area 4.",
            r"(d) $p = 1$, $q = 2$: $1^2 + 2^2 = 5$, a tilted square of area 5.",
            r"(b) 3 is not a sum of two squares: $0 + 1$, $1 + 1$, $0 + 4$ and $1 + 4$ give "
            r"1, 2, 4 and 5, never 3.",
        ], r"Yes for areas 2, 4 and 5; no square of area 3 is possible", height=3.9, size=23, gap=0.1)
        second = part_card("(ii)", [
            r"Every such square has area $p^2 + q^2$, where $p$ and $q$ are whole numbers of grid steps.",
            r"List the sums of two squares: $0 + 1 = 1$, $1 + 1 = 2$, $0 + 4 = 4$, $1 + 4 = 5$, "
            r"$4 + 4 = 8$, $0 + 9 = 9$, $1 + 9 = 10$, $4 + 9 = 13$, $0 + 16 = 16$, $1 + 16 = 17$, "
            r"$9 + 9 = 18$, $4 + 16 = 20$, $9 + 16 = 25$.",
            r"Numbers such as 3, 6, 7, 11, 12, 14 and 15 are not sums of two squares, so no grid "
            r"square has those areas.",
        ], r"Exactly the counting numbers that are a sum of two squares: 1, 2, 4, 5, 8, 9, 10, 13, "
           r"16, 17, 18, 20, 25 and so on", height=3.9, size=23, gap=0.1)
        self.add(card_grid([first, second], 0.42))
