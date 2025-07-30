from manim import *


class BinAdd(Scene):
    def construct(self):
        title = Text("Binary Addition").scale(0.8).to_edge(UP)

        binsum = (
            VGroup(
                MathTex("0 + 0 = 0"),
                MathTex("0 + 1 = 1"),
                MathTex(
                    r"1 + 1 = 2 \text{ in decimal, } 10 \text{ in binary which is } 0 \text{ with carry } 1"
                ),
                MathTex(
                    r"1 + 1 + 1 = 3 \text{ , 11 in binary which is 1 with carry 1}"
                ),
            )
            .scale(0.8)
            .arrange(DOWN, aligned_edge=LEFT)
            .next_to(title, DOWN)
        )

        self.add(title, binsum)
        self.wait(2)
        self.play(FadeOut(binsum))

        exprs = (
            VGroup(
                MathTex(
                    r"2\;2\qquad\quad", r"1\quad", r"0\quad", r"1\quad", r"1\quad", "0"
                ),
                MathTex(
                    r"1\;5\qquad\quad", r"0\quad", r"1\quad", r"1\quad", r"1\quad", "1"
                ),
                MathTex(
                    r"3\;7\quad\;\;",
                    r"1\quad0\quad",
                    r"0\quad",
                    r"1\quad",
                    r"0\quad",
                    "1",
                ),
            )
            .arrange(DOWN, aligned_edge=RIGHT)
            .next_to(title, DOWN, buff=0.8)
        )
        exprs[2].shift(DOWN * 0.2)

        sym = Text("+").scale(0.6).next_to(exprs[1], LEFT, buff=0.4)

        l = (
            Line(start=exprs[0].get_left(), end=exprs[0].get_right(), stroke_width=2)
            .scale(1.1)
            .next_to(exprs[1], DOWN, buff=0.2)
        )

        self.play(FadeIn(exprs[:2]), FadeIn(sym), FadeIn(l))
        self.wait(1)

        ################################################################################
        exp = MathTex("0 + 1 = 1").scale(0.7).next_to(exprs[0], RIGHT, buff=1)
        self.play(
            exprs[0][5].animate.set_color(ORANGE), exprs[1][5].animate.set_color(ORANGE)
        )
        self.play(Write(exp))
        self.play(Write(exprs[2][5]))
        self.play(FadeOut(exp))
        self.wait(0.1)

        ################################################################################
        exp = MathTex("1 + 1 = 10").scale(0.7).next_to(exprs[0], RIGHT, buff=1)
        carry = MathTex("1").scale(0.6).set_color(RED).next_to(exprs[0][3], UP)
        self.play(
            exprs[0][4].animate.set_color(ORANGE), exprs[1][4].animate.set_color(ORANGE)
        )
        self.play(Write(exp))
        self.play(Write(exprs[2][4]))
        self.play(Write(carry))
        self.play(FadeOut(exp))
        self.wait(0.1)

        ################################################################################
        exp = MathTex("1 + 1 + 1 = 11").scale(0.7).next_to(exprs[0], RIGHT, buff=1)
        carry = MathTex("1").scale(0.6).set_color(RED).next_to(exprs[0][2], UP)
        self.play(
            exprs[0][3].animate.set_color(ORANGE), exprs[1][3].animate.set_color(ORANGE)
        )
        self.play(Write(exp))
        self.play(Write(exprs[2][3]))
        self.play(Write(carry))
        self.play(FadeOut(exp))
        self.wait(0.1)

        ################################################################################
        exp = MathTex("1 + 0 + 1 = 10").scale(0.7).next_to(exprs[0], RIGHT, buff=1)
        carry = MathTex("1").scale(0.6).set_color(RED).next_to(exprs[0][1], UP)
        self.play(
            exprs[0][2].animate.set_color(ORANGE), exprs[1][2].animate.set_color(ORANGE)
        )
        self.play(Write(exp))
        self.play(Write(exprs[2][2]))
        self.play(Write(carry))
        self.play(FadeOut(exp))
        self.wait(0.1)

        ################################################################################
        exp = MathTex("1 + 1 + 0 = 10").scale(0.7).next_to(exprs[0], RIGHT, buff=1)
        self.play(
            exprs[0][1].animate.set_color(ORANGE), exprs[1][1].animate.set_color(ORANGE)
        )
        self.play(Write(exp))
        self.play(Write(exprs[2][1]))
        self.play(FadeOut(exp))
        self.wait(0.1)

        ################################################################################
        self.play(Write(exprs[2][0]))
        self.wait(3)


class BinSub(Scene):
    def construct(self):
        title = Text("Binary Subtraction").scale(0.8).to_edge(UP)

        binsub = (
            VGroup(
                MathTex("0 - 0 = 0"),
                MathTex("1 - 0 = 1"),
                MathTex("1 - 1 = 0"),
                MathTex(r"0 - 1 = \text{ borrow from next column, } 10 - 1 = 1"),
            )
            .scale(0.8)
            .arrange(DOWN, aligned_edge=LEFT)
            .next_to(title, DOWN)
        )

        self.add(title, binsub)
        self.wait(2)
        self.play(FadeOut(binsub))

        exprs = (
            VGroup(
                MathTex(r"2\;2\qquad", r"1\quad", r"0\quad", r"1\quad", r"1\quad", "0"),
                MathTex(r"1\;0\qquad", r"0\quad", r"1\quad", r"0\quad", r"1\quad", "0"),
                MathTex(
                    r"1\;2\qquad",
                    r"0\quad",
                    r"1\quad",
                    r"1\quad",
                    r"0\quad",
                    "0",
                ),
            )
            .arrange(DOWN, aligned_edge=RIGHT)
            .next_to(title, DOWN, buff=0.8)
        )
        exprs[2].shift(DOWN * 0.2)

        sym = Text("-").scale(0.6).next_to(exprs[1], LEFT, buff=0.4)

        l = (
            Line(start=exprs[0].get_left(), end=exprs[0].get_right(), stroke_width=2)
            .scale(1.1)
            .next_to(exprs[1], DOWN, buff=0.2)
        )

        self.play(FadeIn(exprs[:2]), FadeIn(sym), FadeIn(l))
        self.wait(1)

        ################################################################################
        exp = MathTex("0 - 0 = 0").scale(0.7).next_to(exprs[0], RIGHT, buff=1)
        self.play(
            exprs[0][5].animate.set_color(ORANGE), exprs[1][5].animate.set_color(ORANGE)
        )
        self.play(Write(exp))
        self.play(Write(exprs[2][5]))
        self.play(FadeOut(exp))
        self.wait(0.1)

        ################################################################################
        exp = MathTex("1 - 1 = 0").scale(0.7).next_to(exprs[0], RIGHT, buff=1)
        self.play(
            exprs[0][4].animate.set_color(ORANGE), exprs[1][4].animate.set_color(ORANGE)
        )
        self.play(Write(exp))
        self.play(Write(exprs[2][4]))
        self.play(FadeOut(exp))
        self.wait(0.1)

        ################################################################################
        exp = MathTex("1 - 0 = 1").scale(0.7).next_to(exprs[0], RIGHT, buff=1)
        self.play(
            exprs[0][3].animate.set_color(ORANGE), exprs[1][3].animate.set_color(ORANGE)
        )
        self.play(Write(exp))
        self.play(Write(exprs[2][3]))
        self.play(FadeOut(exp))
        self.wait(0.1)

        ################################################################################
        slash1 = Line(
            start=exprs[0][2].get_corner(UR),
            end=exprs[0][2].get_corner(DL),
            buff=0,
            color=RED,
        ).rotate(-PI / 4)
        slash2 = Line(
            start=exprs[0][1].get_corner(UR),
            end=exprs[0][1].get_corner(DL),
            buff=0,
            color=RED,
        ).rotate(-PI / 4)

        carry1 = MathTex("10").scale(0.6).set_color(RED).next_to(exprs[0][2], UP)
        carry2 = MathTex("0").scale(0.6).set_color(RED).next_to(exprs[0][1], UP)

        self.play(Write(slash1), Write(slash2))
        self.play(Write(carry1), Write(carry2))

        exp = MathTex("10 - 1 = 1").scale(0.7).next_to(exprs[0], RIGHT, buff=1)
        self.play(
            exprs[0][2].animate.set_color(ORANGE), exprs[1][2].animate.set_color(ORANGE)
        )
        self.play(Write(exp))
        self.play(Write(exprs[2][2]))
        self.play(FadeOut(exp))
        self.wait(0.1)

        ################################################################################
        self.play(Write(exprs[2][0]))
        self.wait(3)


class BinMul(Scene):
    def construct(self):
        title = Text("Binary Multiplication").scale(0.8).to_edge(UP)

        binmul = (
            VGroup(
                MathTex(r"0 \times 0 = 0"),
                MathTex(r"1 \times 0 = 0"),
                MathTex(r"1 \times 1 = 1"),
            )
            .scale(0.8)
            .arrange(DOWN, aligned_edge=LEFT)
            .next_to(title, DOWN)
        )

        self.add(title, binmul)
        self.wait(2)
        self.play(FadeOut(binmul))

        exprs = (
            VGroup(
                MathTex(r"1\;0\qquad", r"1\quad", r"0\quad", r"1\quad", "0"),
                MathTex(r"7\qquad", r"0\quad", r"1\quad", r"1\quad", "1"),
                MathTex(r"1\quad", r"0\quad", r"1\quad", "0"),
                MathTex(r"1\quad", r"0\quad", r"1\quad", r"0\quad", "0"),
                MathTex(r"1\quad", r"0\quad", r"1\quad", r"0\quad", r"0\quad0"),
                MathTex(
                    r"7\;0\qquad",
                    r"1\quad",
                    r"0\quad",
                    r"0\quad",
                    r"0\quad",
                    r"1\quad",
                    r"1\quad",
                    "0",
                ),
            )
            .scale(0.8)
            .arrange(DOWN, aligned_edge=RIGHT)
            .next_to(title, DOWN, buff=0.8)
            .shift(LEFT)
        )
        exprs[1][1].set_color(BLACK)
        exprs[3][-1].set_color(BLACK)
        exprs[4][-1].set_color(BLACK)
        exprs[2:].shift(DOWN * 0.2)
        exprs[-1].shift(DOWN * 0.2)

        sym = Text("x").scale(0.6).next_to(exprs[1], LEFT, buff=0.8)

        l1 = (
            Line(start=exprs[0].get_left(), end=exprs[0].get_right(), stroke_width=2)
            .scale(1.1)
            .next_to(exprs[1], DOWN, buff=0.2)
        )

        l2 = l1.copy().next_to(exprs[-2], DOWN)

        self.play(FadeIn(exprs[:2]), FadeIn(sym), FadeIn(l1))
        self.wait(1)

        ################################################################################
        self.play(exprs[1][4].animate.set_color(ORANGE))
        for i in range(3, -1, -1):
            self.play(Write(exprs[2][i], run_time=0.3))
            self.wait(0.2)
        self.wait(0.1)

        ################################################################################
        self.play(exprs[1][3].animate.set_color(ORANGE))
        for i in range(4, -1, -1):
            self.play(Write(exprs[3][i], run_time=0.3))
            self.wait(0.2)
        self.wait(0.1)

        ################################################################################
        self.play(exprs[1][2].animate.set_color(ORANGE))
        for i in range(4, -1, -1):
            self.play(Write(exprs[4][i], run_time=0.3))
            self.wait(0.2)
        self.wait(0.1)

        ################################################################################
        self.play(Write(l2))
        for i in range(7, -1, -1):
            self.play(Write(exprs[5][i], run_time=0.3))
            self.wait(0.2)

        self.wait(3)


class BinDiv(Scene):
    def construct(self):
        title = Text("Binary Division").scale(0.8).to_edge(UP)

        sym = VGroup(
            Line(start=[0, 0, 0], end=[1.9, 0, 0], stroke_width=1),
            Line(start=[0, 0, 0], end=[0, -0.5, 0], stroke_width=1),
        ).next_to(title, DOWN, buff=1)

        exprs = (
            VGroup(
                MathTex(r"1\;", r"0\;", r"1\;", r"1\;", r"0", r"\qquad\quad2\;2"),
                MathTex(r"3\qquad\quad", r"1\;", r"1"),
                MathTex(r"0\;", r"1\;", r"1"),
                MathTex(r"0\;", r"1\;", r"0\;", "1"),
                MathTex(r"0\;0\;", r"1\;", r"1"),
                MathTex(r"0\;0\;", r"1\;", r"0\;", "0"),
                MathTex(r"0\;0\;0\;", r"1\;", r"1"),
                MathTex(r"0\;0\;0\;0\;", "1\qquad\quad1"),
                MathTex(r"1\;", r"1\;", "1", r"\qquad\quad7"),
            )
            .scale(0.8)
            .next_to(title, DOWN, buff=0.8)
            .shift(LEFT)
        )
        exprs[0].next_to(sym[1], RIGHT, buff=0.2)
        exprs[1].next_to(sym[1], LEFT, buff=0.2)

        exprs[2].next_to(exprs[0], DOWN, aligned_edge=LEFT)
        exprs[2][0].set_color(BLACK)

        exprs[3].next_to(exprs[2], DOWN, aligned_edge=LEFT, buff=0.3)
        exprs[3][0].set_color(BLACK)

        exprs[4].next_to(exprs[3], DOWN, aligned_edge=LEFT, buff=0.3)
        exprs[4][0].set_color(BLACK)

        exprs[5].next_to(exprs[4], DOWN, aligned_edge=LEFT, buff=0.3)
        exprs[5][0].set_color(BLACK)

        exprs[6].next_to(exprs[5], DOWN, aligned_edge=LEFT, buff=0.3)
        exprs[6][0].set_color(BLACK)

        exprs[7].next_to(exprs[6], DOWN, aligned_edge=LEFT, buff=0.3)
        exprs[7][0].set_color(BLACK)

        exprs[8].next_to(exprs[0], UP, buff=0.3)

        l1 = Line(
            start=exprs[2].get_left(), end=exprs[2].get_right(), stroke_width=2
        ).next_to(exprs[2], DOWN, buff=0.2)

        l2 = l1.copy().next_to(exprs[4], DOWN, buff=0.2).scale(1.2).shift(RIGHT * 0.2)
        l3 = l2.copy().next_to(exprs[6], DOWN, buff=0.2).shift(RIGHT * 0.4)

        a1 = Arrow(
            start=exprs[0][3].get_bottom(),
            end=exprs[3][3],
            tip_length=0.1,
            stroke_width=2,
            buff=0.18,
        )
        a2 = Arrow(
            start=exprs[0][4].get_bottom(),
            end=exprs[5][3],
            tip_length=0.1,
            stroke_width=2,
            buff=0.18,
        )

        self.add(title, sym, exprs[:2])
        self.wait(1)

        self.play(Write(exprs[-1][0]))
        self.play(Write(exprs[2]))
        self.play(Write(l1))
        self.play(Write(exprs[3][:-1]))
        self.play(GrowArrow(a1))
        self.play(Write(exprs[3][-1]))
        self.play(Write(exprs[-1][1]))
        self.play(Write(exprs[4]))
        self.play(Write(l2))
        self.play(Write(exprs[5][:-1]))
        self.play(GrowArrow(a2))
        self.play(Write(exprs[5][-1]))
        self.play(Write(exprs[-1][2]))
        self.play(Write(exprs[6]))
        self.play(Write(l3))
        self.play(Write(exprs[7]))
        self.play(Write(exprs[-1][3]))

        self.wait(3)
