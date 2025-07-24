from manim import *


class BinaryArithmetic(Scene):
    def construct(self):
        title = Text("Binary Addition").scale(0.8).shift(UP)

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
        self.wait(1)

        # binary addition of 22 + 10
        exprs = (
            VGroup(
                MathTex(
                    r"22\qquad",
                    r"\quad\;\;1\quad",
                    r"0\quad",
                    r"1\quad",
                    r"1\quad",
                    "0",
                ),
                MathTex(
                    r"14\qquad",
                    r"\quad\;\;0\quad",
                    r"1\quad",
                    r"1\quad",
                    r"1\quad",
                    "0",
                ),
            )
            .arrange(DOWN, buff=0.3, aligned_edge=LEFT)
            .shift(DOWN * 0.7)
        )
        exprs[-1].shift(DOWN * 0.3)

        sym = Text("+").scale(0.7).next_to(exprs[1], LEFT, buff=0.4)

        l = Line(
            start=exprs[-1][0].get_left(), end=exprs[-1][-1].get_right(), stroke_width=1
        ).next_to(exprs[1], DOWN, buff=0.3)

        sum1 = VGroup(exprs, sym, l)
        self.add(sum1)
        self.wait(1)

        self.play(
            exprs[0][5].animate.set_color(ORANGE), exprs[1][5].animate.set_color(ORANGE)
        )
        bitsum_expr = MathTex("0 + 0 = 0").scale(0.7).next_to(exprs, RIGHT, buff=1)
        self.play(Write(bitsum_expr))
        bitsum = MathTex("0").next_to(exprs[1][5], DOWN, buff=0.5)
        self.play(Write(bitsum))
        self.wait(0.4)
        self.play(FadeOut(bitsum_expr))
        self.wait(0.5)

        self.play(
            exprs[0][4].animate.set_color(ORANGE), exprs[1][4].animate.set_color(ORANGE)
        )
        bitsum_expr = MathTex("1 + 1 = 10").scale(0.7).next_to(exprs, RIGHT, buff=1)
        self.play(Write(bitsum_expr, run_time=1.5))
        self.wait(0.5)
        bitsum = MathTex("0").next_to(exprs[1][4], DOWN, buff=0.5)
        carry = MathTex("1").scale(0.6).set_color(RED).next_to(exprs[0][3], UP)
        self.play(Write(bitsum), Write(carry))
        self.wait(0.4)
        self.play(FadeOut(bitsum_expr))
        self.wait(0.5)

        self.play(
            exprs[0][3].animate.set_color(ORANGE), exprs[1][3].animate.set_color(ORANGE)
        )
        bitsum_expr = MathTex("1 + 1 + 1 = 11").scale(0.7).next_to(exprs, RIGHT, buff=1)
        self.play(Write(bitsum_expr, run_time=1.5))
        self.wait(0.5)
        bitsum = MathTex("1").next_to(exprs[1][3], DOWN, buff=0.5)
        carry = MathTex("1").scale(0.6).set_color(RED).next_to(exprs[0][2], UP)
        self.play(Write(bitsum), Write(carry))
        self.wait(0.4)
        self.play(FadeOut(bitsum_expr))
        self.wait(0.5)

        self.play(
            exprs[0][2].animate.set_color(ORANGE), exprs[1][2].animate.set_color(ORANGE)
        )
        bitsum_expr = MathTex("1 + 0 + 1 = 10").scale(0.7).next_to(exprs, RIGHT, buff=1)
        self.play(Write(bitsum_expr, run_time=1.5))
        self.wait(0.5)
        bitsum = MathTex("0").next_to(exprs[1][2], DOWN, buff=0.5)
        carry = MathTex("1").scale(0.6).set_color(RED).next_to(exprs[0][1], UP)
        self.play(Write(bitsum), Write(carry))
        self.wait(0.4)
        self.play(FadeOut(bitsum_expr))
        self.wait(0.5)

        self.play(
            exprs[0][1].animate.set_color(ORANGE), exprs[1][1].animate.set_color(ORANGE)
        )
        bitsum_expr = MathTex("1 + 1 + 0 = 10").scale(0.7).next_to(exprs, RIGHT, buff=1)
        self.play(Write(bitsum_expr, run_time=1.5))
        self.wait(0.5)
        bitsum = MathTex("0").next_to(exprs[1][1], DOWN, buff=0.5)
        carry = (
            MathTex("1")
            .scale(0.6)
            .set_color(RED)
            .next_to(exprs[0][1], UP)
            .shift(LEFT * 0.8)
        )
        self.play(Write(bitsum), Write(carry))
        self.wait(0.4)
        self.play(FadeOut(bitsum_expr))
        self.wait(0.5)

        self.play(
            Write(MathTex("1").next_to(exprs[1][1], DOWN, buff=0.5).shift(LEFT * 0.8))
        )
        self.wait(0.4)
        self.play(Write(MathTex("36").next_to(exprs[1][0], DOWN, buff=0.5)))

        self.wait(3)

        #######################################################################################
        #######################################################################################

        # Fade out all mobjects in the scene
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)

        #######################################################################################
        #######################################################################################

        title = Text("Binary Subtraction").scale(0.8).shift(UP)

        binsum = (
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

        self.add(title, binsum)
        self.wait(2)

        self.play(FadeOut(binsum))
        self.wait(1)

        # binary addition of 22 - 10
        exprs = (
            VGroup(
                MathTex(
                    r"22\qquad",
                    r"\quad\;\;1\quad",
                    r"0\quad",
                    r"1\quad",
                    r"1\quad",
                    "0",
                ),
                MathTex(
                    r"10\qquad",
                    r"\quad\;\;0\quad",
                    r"1\quad",
                    r"0\quad",
                    r"1\quad",
                    "0",
                ),
            )
            .arrange(DOWN, buff=0.3, aligned_edge=LEFT)
            .shift(DOWN * 0.7)
        )

        sym = Text("-").scale(0.7).next_to(exprs[1], LEFT, buff=0.4)

        l = Line(
            start=exprs[-1][0].get_left(), end=exprs[-1][-1].get_right(), stroke_width=1
        ).next_to(exprs[1], DOWN, buff=0.3)

        sub1 = VGroup(exprs, sym, l)
        self.add(sub1)
        self.wait(2)

        self.play(
            exprs[0][5].animate.set_color(ORANGE), exprs[1][5].animate.set_color(ORANGE)
        )
        bitsub_expr = MathTex("0 - 0 = 0").scale(0.7).next_to(exprs, RIGHT, buff=1)
        self.play(Write(bitsub_expr, run_time=1.5))
        bitsub = MathTex("0").next_to(exprs[1][5], DOWN, buff=0.5)
        self.play(Write(bitsub))
        self.wait(0.4)
        self.play(FadeOut(bitsub_expr))
        self.wait(0.5)

        self.play(
            exprs[0][4].animate.set_color(ORANGE), exprs[1][4].animate.set_color(ORANGE)
        )
        bitsub_expr = MathTex("1 - 1 = 0").scale(0.7).next_to(exprs, RIGHT, buff=1)
        self.play(Write(bitsub_expr, run_time=1.5))
        self.wait(0.5)
        bitsub = MathTex("0").next_to(exprs[1][4], DOWN, buff=0.5)
        self.play(Write(bitsub))
        self.wait(0.4)
        self.play(FadeOut(bitsub_expr))
        self.wait(0.5)

        self.play(
            exprs[0][3].animate.set_color(ORANGE), exprs[1][3].animate.set_color(ORANGE)
        )
        bitsub_expr = MathTex("1 - 0 = 1").scale(0.7).next_to(exprs, RIGHT, buff=1)
        self.play(Write(bitsub_expr, run_time=1.5))
        self.wait(0.5)
        bitsub = MathTex("1").next_to(exprs[1][3], DOWN, buff=0.5)
        self.play(Write(bitsub))
        self.wait(0.4)
        self.play(FadeOut(bitsub_expr))
        self.wait(0.5)

        self.play(
            exprs[0][2].animate.set_color(ORANGE), exprs[1][2].animate.set_color(ORANGE)
        )

        slash1 = Line(
            start=exprs[0][2].get_corner(UR),
            end=exprs[0][2].get_corner(DL),
            buff=0,
            color=RED,
        ).rotate(-PI / 4)

        carry1 = MathTex("10").scale(0.6).set_color(RED).next_to(exprs[0][2], UP)

        slash2 = Line(
            start=exprs[0][1].get_corner(UR),
            end=exprs[0][1].get_corner(DL),
            buff=0,
            color=RED,
        ).rotate(-PI / 4)

        carry2 = MathTex("0").scale(0.6).set_color(RED).next_to(exprs[0][1], UP)

        self.play(Write(slash1), Write(slash2))
        self.wait(0.3)
        self.play(Write(carry1), Write(carry2))
        self.wait(0.3)

        bitsub_expr = MathTex("10 - 1 = 1").scale(0.7).next_to(exprs, RIGHT, buff=1)
        self.play(Write(bitsub_expr, run_time=1.5))
        self.wait(0.5)
        bitsub = MathTex("1").next_to(exprs[1][2], DOWN, buff=0.5)
        self.play(Write(bitsub))
        self.wait(0.4)
        self.play(FadeOut(bitsub_expr))
        self.wait(0.5)

        bitsub_expr = MathTex("0 - 0 = 0").scale(0.7).next_to(exprs, RIGHT, buff=1)
        self.play(Write(bitsub_expr, run_time=1.5))
        self.wait(0.5)
        bitsub = MathTex("0").next_to(exprs[1][1], DOWN, buff=0.5)
        self.play(Write(bitsub))
        self.wait(0.4)
        self.play(FadeOut(bitsub_expr))
        self.wait(0.5)

        self.play(Write(MathTex("12").next_to(exprs[1][0], DOWN, buff=0.5)))

        self.wait(3)

        #######################################################################################
        #######################################################################################

        # Fade out all mobjects in the scene
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)

        #######################################################################################
        #######################################################################################

        title = Text("Binary Multiplication").scale(0.8).shift(UP * 1.5)

        binmul = (
            VGroup(
                MathTex(r"0 \text{ x } 0 = 0"),
                MathTex(r"1 \text{ x } 0 = 0"),
                MathTex(r"1 \text{ x } 1 = 1"),
            )
            .scale(0.8)
            .arrange(DOWN, aligned_edge=LEFT)
            .next_to(title, DOWN)
        )

        self.add(title, binmul)
        self.wait(2)

        self.play(FadeOut(binmul))
        self.wait(1)

        # binary multiplication of 18 * 4
        exprs = (
            VGroup(
                MathTex(r"18\qquad", r"1\quad", r"0\quad", r"0\quad", r"1\quad", "0"),
                MathTex(r"4\qquad\quad\quad\;\;\;\;\;", r"1\quad", r"0\quad", "0"),
                MathTex(r"0\quad", r"0\quad", r"0\quad", r"0\quad", "0"),
                MathTex(r"0\quad", r"0\quad", r"0\quad", r"0\quad", r"0\quad"),
                MathTex(r"1\quad", r"0\quad", r"0\quad", r"1\quad", r"0\quad"),
                MathTex(
                    r"1\quad",
                    r"0\quad",
                    r"0\quad",
                    r"1\quad",
                    r"0\quad",
                    r"0\quad",
                    r"0\quad",
                ),
            )
            .arrange(DOWN, buff=0.3, aligned_edge=RIGHT)
            .next_to(title, DOWN, buff=0.4)
        )

        sym = Text("x").scale(0.7).next_to(exprs[1], LEFT, buff=0.4)

        l = Line(
            start=exprs[0][0].get_left(), end=exprs[0][-1].get_right(), stroke_width=1
        ).next_to(exprs[1], DOWN, buff=0.3)

        sub1 = VGroup(exprs[:2], sym, l)
        self.add(sub1)
        self.wait(2)

        self.play(exprs[1][3].animate.set_color(ORANGE))
        self.play(Write(exprs[2][4].next_to(exprs[0][5], DOWN, buff=1.2)))
        self.play(Write(exprs[2][3].next_to(exprs[0][4], DOWN, buff=1.2)))
        self.play(Write(exprs[2][2].next_to(exprs[0][3], DOWN, buff=1.2)))
        self.play(Write(exprs[2][1].next_to(exprs[0][2], DOWN, buff=1.2)))
        self.play(Write(exprs[2][0].next_to(exprs[0][1], DOWN, buff=1.2)))
        self.wait(0.4)

        self.play(exprs[1][2].animate.set_color(ORANGE))
        self.play(Write(exprs[3][4].next_to(exprs[0][4], DOWN, buff=1.7)))
        self.play(Write(exprs[3][3].next_to(exprs[0][3], DOWN, buff=1.7)))
        self.play(Write(exprs[3][2].next_to(exprs[0][2], DOWN, buff=1.7)))
        self.play(Write(exprs[3][1].next_to(exprs[0][1], DOWN, buff=1.7)))
        self.play(
            Write(exprs[3][0].next_to(exprs[0][1], DOWN, buff=1.7).shift(LEFT * 0.7))
        )
        self.wait(0.4)

        self.play(exprs[1][1].animate.set_color(ORANGE))
        self.play(Write(exprs[4][4].next_to(exprs[0][3], DOWN, buff=2.2)))
        self.play(Write(exprs[4][3].next_to(exprs[0][2], DOWN, buff=2.2)))
        self.play(Write(exprs[4][2].next_to(exprs[0][1], DOWN, buff=2.2)))
        self.play(
            Write(exprs[4][1].next_to(exprs[0][1], DOWN, buff=2.2).shift(LEFT * 0.7))
        )
        self.play(
            Write(exprs[4][0].next_to(exprs[0][1], DOWN, buff=2.2).shift(LEFT * 1.4))
        )
        self.wait(0.4)

        l2 = l.copy().shift(DOWN * 1.9)
        self.play(Write(l2))

        self.play(Write(exprs[5][6].next_to(exprs[2][4], DOWN, buff=1.6)))
        self.play(Write(exprs[5][5].next_to(exprs[2][3], DOWN, buff=1.6)))
        self.play(Write(exprs[5][4].next_to(exprs[4][4], DOWN, buff=0.57)))
        self.play(Write(exprs[5][3].next_to(exprs[4][3], DOWN, buff=0.57)))
        self.play(Write(exprs[5][2].next_to(exprs[4][2], DOWN, buff=0.57)))
        self.play(Write(exprs[5][1].next_to(exprs[4][1], DOWN, buff=0.57)))
        self.play(Write(exprs[5][0].next_to(exprs[4][0], DOWN, buff=0.57)))

        self.wait(0.4)
        self.play(Write(MathTex("72").next_to(exprs[5][0], LEFT, buff=1)))

        self.wait(3)

        #######################################################################################
        #######################################################################################

        # Fade out all mobjects in the scene
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)

        #######################################################################################
        #######################################################################################

        title = Text("Binary Division").scale(0.8).shift(UP * 1.5)

        divsym = VGroup(
            Line(start=[0, 0, 0], end=[2.1, 0, 0], stroke_width=1),
            Line(start=[0, 0, 0], end=[0, -0.6, 0], stroke_width=1),
        ).shift(LEFT)

        # binary division of 20 / 3
        exprs = VGroup(
            MathTex("3 \qquad\quad 1\;1"),
            MathTex("1\;", "0\;", "1\;", "0\;", "0", "\qquad\quad 20"),
            MathTex("1\;", "1"),
            MathTex("1\;", "0\;", "0"),
            MathTex("1\;", "1"),
            MathTex("1\;", "0", r"\qquad\quad2"),
            MathTex("1\;", "1\;", "0", "\qquad\quad\quad\;\;6"),
        )
        exprs[-1].next_to(divsym[0], UP, buff=0.2, aligned_edge=LEFT).shift(RIGHT * 0.3)
        exprs[0].next_to(divsym[1], LEFT, buff=0.2)
        exprs[1].next_to(divsym[1], RIGHT, buff=0.2)
        exprs[2].next_to(exprs[1][2], DOWN, buff=0.2, aligned_edge=RIGHT)

        self.add(title, divsym, exprs[:2])
        self.wait(1)

        self.play(Write(exprs[-1][0]))
        self.play(Write(exprs[2]))

        l = Line(
            start=exprs[1][0].get_left(), end=exprs[1][2].get_right(), stroke_width=1
        ).next_to(exprs[2], DOWN, aligned_edge=RIGHT)
        self.play(Write(l))

        exprs[3][:2].next_to(l, DOWN, aligned_edge=RIGHT, buff=0.1)
        self.play(Write(exprs[3][:2]))

        arrow = Arrow(
            start=[0, 0, 0],
            end=[0, -1, 0],
            tip_length=0.1,
            stroke_width=1,
        ).shift(DOWN * 0.4 + RIGHT * 0.4)
        self.play(GrowArrow(arrow))

        self.play(Write(exprs[3][2].next_to(exprs[3][1], RIGHT, buff=0.15)))

        self.play(Write(exprs[-1][1]))
        exprs[4].next_to(exprs[3][2], DOWN, aligned_edge=RIGHT, buff=0.1)
        self.play(Write(exprs[4]))

        l2 = l.copy().next_to(exprs[4], DOWN, buff=0.1, aligned_edge=RIGHT)
        self.play(Write(l2))

        exprs[5].next_to(l2, DOWN, buff=0.1).shift(RIGHT * 1.5)
        self.play(Write(exprs[5][0]))

        arrow2 = arrow.copy().scale(3).next_to(exprs[1][4], DOWN, buff=0.1)
        self.play(GrowArrow(arrow2))
        self.play(Write(exprs[5][1:]))

        self.play(Write(exprs[-1][2:]))

        self.wait(3)
