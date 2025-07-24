from manim import *


class HexadecimalArithmetic(Scene):
    def construct(self):
        title = Text("Hexadecimal Addition").scale(0.8).shift(UP)

        hexsum = (
            VGroup(
                MathTex("1 + 0 = 1"),
                MathTex(r"9 + 1 = 10\text{(A)}"),
                MathTex(r"\text{F} + 1 = 10"),
                MathTex(r"\text{F} + \text{F} =  1\text{E}"),
            )
            .scale(0.8)
            .arrange(DOWN, aligned_edge=LEFT)
            .next_to(title, DOWN)
        )
        exp = (
            MathTex(
                r"\text{F}(15) + \text{F}(15) = 30 \longrightarrow 30 - 16 = 14\text{(E)} \text{ with carry 1 } = 1\text{E}"
            )
            .scale(0.7)
            .next_to(hexsum, DOWN, buff=0.5)
        )

        self.add(title, hexsum, exp)
        self.wait(2)

        self.play(FadeOut(hexsum), FadeOut(exp))
        self.wait(1)

        # hexadecimal addition of 90 + 22
        exprs = (
            VGroup(
                MathTex(r"90\qquad", r"5\quad", r"\text{A}"),
                MathTex(r"22\qquad", r"1\quad", r"6"),
            )
            .arrange(DOWN, buff=0.2)
            .next_to(title, DOWN, buff=1)
            .shift(LEFT)
        )
        exprs[-1].shift(DOWN * 0.2)

        sym = Text("+").scale(0.7).next_to(exprs[1], LEFT, buff=0.4)

        l = (
            Line(
                start=exprs[-1][0].get_left(),
                end=exprs[-1][-1].get_right(),
                stroke_width=1,
            )
            .scale(1.2)
            .next_to(exprs[1], DOWN, buff=0.2)
        )

        self.add(exprs, sym, l)
        self.wait(1)

        self.play(
            exprs[0][2].animate.set_color(ORANGE), exprs[1][2].animate.set_color(ORANGE)
        )
        exp = (
            MathTex(r"\text{A}(10) + 6 \longrightarrow 16 - 16 \longrightarrow 10")
            .scale(0.7)
            .next_to(exprs, RIGHT, buff=1)
        )
        self.play(Write(exp))
        self.play(Write(MathTex("0").next_to(exprs[1][2], DOWN, buff=0.3)))
        self.play(
            Write(MathTex("1").scale(0.6).set_color(RED).next_to(exprs[0][1], UP))
        )
        self.play(FadeOut(exp))
        self.wait(0.4)

        self.play(
            exprs[0][1].animate.set_color(ORANGE), exprs[1][1].animate.set_color(ORANGE)
        )
        exp = MathTex(r"1 + 5 + 1 = 7").scale(0.7).next_to(exprs, RIGHT, buff=1)
        self.play(Write(exp))
        self.play(Write(MathTex("7").next_to(exprs[1][1], DOWN, buff=0.3)))
        self.wait(0.4)

        self.play(Write(MathTex("112").next_to(exprs[1][0], DOWN, buff=0.3)))

        self.wait(3)

        ################################################################################
        ################################################################################

        # clear the scene
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)

        ################################################################################
        ################################################################################

        title = Text("Hexadecimal Subtraction").scale(0.8).shift(UP)

        hexsub = (
            VGroup(
                MathTex("1 - 0 = 1"),
                MathTex(r"\text{A} - 1 = 9"),
                MathTex(r"\text{F} - 1 = \text{E}"),
                MathTex(r"\text{E} - \text{F} = \text{F}"),
            )
            .scale(0.8)
            .arrange(DOWN, aligned_edge=LEFT)
            .next_to(title, DOWN)
        )

        exp = (
            MathTex(
                r"\text{E} - \text{F we take borrow from next column}\\"
                r"\text{E} \longrightarrow 16 + \text{E}(14) = 30 \text{ so, E} - \text{F} = 30 - 15 = 15\text{(F)}"
            )
            .scale(0.6)
            .next_to(hexsub, DOWN, buff=0.3)
        )

        self.add(title, hexsub, exp)
        self.wait(2)

        self.play(FadeOut(hexsub), FadeOut(exp))
        self.wait(1)

        # hex subtraction of 64 - 16
        exprs = (
            VGroup(
                MathTex(r"100\qquad", r"6\quad", "4"),
                MathTex(r"22\qquad", r"1\quad", "6"),
                MathTex(r"78\qquad", r"4\quad", r"\text{E}"),
            )
            .arrange(DOWN, buff=0.3, aligned_edge=RIGHT)
            .shift(DOWN)
        )
        exprs[-1].shift(DOWN * 0.2)

        sym = Text("-").scale(0.7).next_to(exprs[1], LEFT, buff=0.4)

        l = (
            Line(
                start=exprs[-1][0].get_left(),
                end=exprs[-1][-1].get_right(),
                stroke_width=1,
            )
            .scale(1.2)
            .next_to(exprs[1], DOWN, buff=0.3)
        )

        self.add(exprs[:2], sym, l)
        self.wait(1)

        self.play(
            exprs[0][2].animate.set_color(ORANGE), exprs[1][2].animate.set_color(ORANGE)
        )
        slash1 = Line(
            start=exprs[0][1].get_corner(UR),
            end=exprs[0][1].get_corner(DL),
            buff=0,
            color=RED,
        ).rotate(-PI / 4)
        brrow1 = MathTex("5").scale(0.6).set_color(RED).next_to(exprs[0][1], UP)

        slash2 = Line(
            start=exprs[0][2].get_corner(UR),
            end=exprs[0][2].get_corner(DL),
            buff=0,
            color=RED,
        ).rotate(-PI / 4)
        brrow2 = MathTex("20").scale(0.6).set_color(RED).next_to(exprs[0][2], UP)

        self.play(Write(slash1), Write(slash2))
        self.play(Write(brrow1), Write(brrow2))

        exp1 = (
            MathTex(r"4 \longrightarrow 16 + 4 = 20")
            .scale(0.7)
            .next_to(exprs, RIGHT, buff=1)
        )
        exp2 = MathTex(r"20 - 6 = 14\text{(E)}").scale(0.7).next_to(exp1, DOWN)
        self.play(Write(exp1))
        self.play(Write(exp2))

        self.play(Write(MathTex(r"\text{E}").next_to(exprs[1][2], DOWN, buff=0.4)))
        self.play(FadeOut(exp1), FadeOut(exp2))
        self.wait(0.4)

        self.play(
            exprs[0][1].animate.set_color(ORANGE), exprs[1][1].animate.set_color(ORANGE)
        )
        exp1 = MathTex(r"5 - 1 = 4").scale(0.7).next_to(exprs, RIGHT, buff=1)
        self.play(Write(exp1))
        self.play(Write(MathTex("4").next_to(exprs[1][1], DOWN, buff=0.4)))
        self.play(FadeOut(exp1))
        self.wait(0.4)

        self.play(Write(MathTex("78").next_to(exprs[1][0], DOWN, buff=0.4)))
        self.wait(3)
