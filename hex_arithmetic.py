from manim import *


class HexAdd(Scene):
    def construct(self):
        title = Text("Hexadecimal Addition").scale(0.8).to_edge(UP)

        hexsum = (
            VGroup(
                MathTex("0 + 0 = 0"),
                MathTex(r"9 + 1 = 10\text{ (A)}"),
                MathTex(r"\text{A} + \text{D} =  17"),
                MathTex(r"\text{F} + \text{F} =  1\text{E}"),
            )
            .scale(0.8)
            .arrange(DOWN, aligned_edge=LEFT)
            .next_to(title, DOWN, buff=0.5)
        )

        exps = (
            VGroup(
                MathTex(
                    r"\text{A} + \text{D} \qquad 10 + 13 = 23 \longrightarrow 23 - 16 = 7 \text{ with carry } 1 = 17"
                ),
                MathTex(
                    r"\text{F} + \text{F} \qquad 15 + 15 = 30 \longrightarrow 30 - 16 = 14 \text{ (E) with carry } 1 = 1\text{E}"
                ),
            )
            .scale(0.8)
            .arrange(DOWN, aligned_edge=LEFT)
            .next_to(hexsum, DOWN, buff=0.8)
        )

        self.add(title, hexsum, exps)
        self.wait(2)
        self.play(FadeOut(hexsum), FadeOut(exps))

        exprs = (
            VGroup(
                MathTex(r"7\;2\;5\qquad\quad", r"2\quad", r"\text{D}\quad", "5"),
                MathTex(r"1\;0\;0\qquad\quad", r"0\quad", r"6\quad", "4"),
                MathTex(r"8\;2\;5\qquad\quad", r"3\quad", r"3\quad", "9"),
            )
            .arrange(DOWN, aligned_edge=RIGHT)
            .next_to(title, DOWN, buff=0.8)
        )
        exprs[1][1].set_color(BLACK)
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
        exp1 = MathTex("5 + 4 = 9").scale(0.7).next_to(exprs[0], RIGHT, buff=1)
        exp2 = (
            MathTex(r"\text{res} = 9 \;\%\; 16 = 9")
            .scale(0.7)
            .next_to(exp1, DOWN, aligned_edge=LEFT)
        )
        exp3 = (
            MathTex(r"\text{carr} = 9 \;/\; 16 = 0")
            .scale(0.7)
            .next_to(exp2, DOWN, aligned_edge=LEFT)
        )

        self.play(
            exprs[0][3].animate.set_color(ORANGE), exprs[1][3].animate.set_color(ORANGE)
        )
        self.play(Write(exp1))
        self.play(Write(exp2))
        self.play(Write(exp3))
        self.play(Write(exprs[2][3]))
        self.play(FadeOut(exp1), FadeOut(exp2), FadeOut(exp3))
        self.wait(0.1)

        ################################################################################
        exp1 = (
            MathTex(r"\text{D} + 6 = 13 + 6 = 19")
            .scale(0.7)
            .next_to(exprs[0], RIGHT, buff=1)
        )
        exp2 = (
            MathTex(r"\text{res} = 19 \;\%\; 16 = 3")
            .scale(0.7)
            .next_to(exp1, DOWN, aligned_edge=LEFT)
        )
        exp3 = (
            MathTex(r"\text{carr} = 19 \;/\; 16 = 1")
            .scale(0.7)
            .next_to(exp2, DOWN, aligned_edge=LEFT)
        )

        carry = MathTex("1").scale(0.6).set_color(RED).next_to(exprs[0][1], UP)

        self.play(
            exprs[0][2].animate.set_color(ORANGE), exprs[1][2].animate.set_color(ORANGE)
        )
        self.play(Write(exp1))
        self.play(Write(exp2))
        self.play(Write(exp3))
        self.play(Write(exprs[2][2]))
        self.play(Write(carry))
        self.play(FadeOut(exp1), FadeOut(exp2), FadeOut(exp3))
        self.wait(0.1)

        ################################################################################
        exp1 = MathTex(r"1 + 2 = 3").scale(0.7).next_to(exprs[0], RIGHT, buff=1)
        exp2 = (
            MathTex(r"\text{res} = 3 \;\%\; 16 = 3")
            .scale(0.7)
            .next_to(exp1, DOWN, aligned_edge=LEFT)
        )
        exp3 = (
            MathTex(r"\text{carr} = 3 \;/\; 16 = 0")
            .scale(0.7)
            .next_to(exp2, DOWN, aligned_edge=LEFT)
        )

        self.play(exprs[0][1].animate.set_color(ORANGE))
        self.play(Write(exp1))
        self.play(Write(exp2))
        self.play(Write(exp3))
        self.play(Write(exprs[2][1]))
        self.play(FadeOut(exp1), FadeOut(exp2), FadeOut(exp3))
        self.wait(0.1)

        self.play(Write(exprs[2][0]))

        self.wait(3)


class HexSub(Scene):
    def construct(self):
        title = Text("Hexadecimal Subtraction").scale(0.8).to_edge(UP)

        hexsub = (
            VGroup(
                MathTex("0 - 0 = 0"),
                MathTex(r"\text{A} - 1 = 9"),
                MathTex(
                    r"\text{A} - \text{F} = \text{B, borrow 1 } \longrightarrow (16 + 10) - 15 = 11\text{ (B)}"
                ),
            )
            .scale(0.8)
            .arrange(DOWN, aligned_edge=LEFT)
            .next_to(title, DOWN, buff=0.5)
        )

        self.add(title, hexsub)
        self.wait(2)
        self.play(FadeOut(hexsub))

        exprs = (
            VGroup(
                MathTex(r"7\;2\;0\qquad\quad", r"2\quad", r"\text{D}\quad", "0"),
                MathTex(r"1\;0\;0\qquad\quad", r"0\quad", r"6\quad", "4"),
                MathTex(r"6\;2\;0\qquad\quad", r"2\quad", r"6\quad", r"\text{C}"),
            )
            .arrange(DOWN, aligned_edge=RIGHT)
            .next_to(title, DOWN, buff=0.8)
        )
        exprs[1][1].set_color(BLACK)
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
        slash1 = Line(
            start=exprs[0][3].get_corner(UR),
            end=exprs[0][3].get_corner(DL),
            buff=0,
            color=RED,
        ).rotate(-PI / 4)
        slash2 = Line(
            start=exprs[0][2].get_corner(UR),
            end=exprs[0][2].get_corner(DL),
            buff=0,
            color=RED,
        ).rotate(-PI / 4)

        carry1 = MathTex("16").scale(0.6).set_color(RED).next_to(exprs[0][3], UP)
        carry2 = MathTex(r"\text{C}").scale(0.6).set_color(RED).next_to(exprs[0][2], UP)

        self.play(Write(slash1), Write(slash2))
        self.play(Write(carry1), Write(carry2))

        exp = (
            MathTex(r"16 - 4 = 12\text{ (C)}")
            .scale(0.7)
            .next_to(exprs[0], RIGHT, buff=1)
        )

        self.play(
            exprs[0][3].animate.set_color(ORANGE), exprs[1][3].animate.set_color(ORANGE)
        )
        self.play(Write(exp))
        self.play(Write(exprs[2][3]))
        self.play(FadeOut(exp))
        self.wait(0.1)

        ################################################################################
        exp = (
            MathTex(r"\text{C} - 6 = 12 - 6 = 6")
            .scale(0.7)
            .next_to(exprs[0], RIGHT, buff=1)
        )

        self.play(
            exprs[0][2].animate.set_color(ORANGE), exprs[1][2].animate.set_color(ORANGE)
        )
        self.play(Write(exp))
        self.play(Write(exprs[2][2]))
        self.play(FadeOut(exp))
        self.wait(0.1)

        ################################################################################
        self.play(exprs[0][1].animate.set_color(ORANGE))
        self.play(Write(exprs[2][1]))
        self.wait(0.1)

        self.play(Write(exprs[2][0]))

        self.wait(3)


class HexMul(Scene):
    def construct(self):
        title = Text("Hexadecimal Multiplication").scale(0.8).to_edge(UP)

        hexmul = (
            VGroup(
                MathTex(r"0 \times 0 = 0"),
                MathTex(r"1 \times \text{F} = \text{F}"),
                MathTex(r"\text{F} \times \text{F} = \text{E}1"),
            )
            .scale(0.8)
            .arrange(DOWN, aligned_edge=LEFT)
            .next_to(title, DOWN)
        )

        exp = (
            VGroup(
                MathTex(r"\text{F} \times \text{F} = 15 \times 15 = 225"),
                MathTex(r"\text{res} = 225 \;\%\; 16 = 1"),
                MathTex(
                    r"\text{carry} = 225 \;/\; 16 = 14\text{ (E)} \longrightarrow \text{E}1"
                ),
            )
            .scale(0.7)
            .arrange(DOWN, aligned_edge=LEFT)
            .next_to(hexmul, DOWN, buff=0.5)
            .shift(RIGHT)
        )

        self.add(title, hexmul, exp)
        self.wait(2)
        self.play(FadeOut(hexmul), FadeOut(exp))

        exprs = (
            VGroup(
                MathTex(r"6\;1\qquad", r"3\quad", r"\text{D}"),
                MathTex(r"2\;6\qquad", r"1\quad", r"\text{A}"),
                MathTex(r"2\quad", r"6\quad", "2"),
                MathTex(r"3\quad", r"\text{D}\quad", "0"),
                MathTex(r"1\;5\;8\;6\qquad", r"6\quad", r"3\quad", "2"),
            )
            .scale(0.8)
            .arrange(DOWN, aligned_edge=RIGHT)
            .next_to(title, DOWN, buff=0.8)
            .shift(LEFT)
        )
        exprs[3][-1].set_color(BLACK)
        exprs[2:].shift(DOWN * 0.2)
        exprs[-1].shift(DOWN * 0.2)

        sym = Text("x").scale(0.6).next_to(exprs[1], LEFT, buff=0.6)

        l1 = (
            Line(start=exprs[0].get_left(), end=exprs[0].get_right(), stroke_width=2)
            .scale(1.1)
            .next_to(exprs[1], DOWN, buff=0.2)
        )

        l2 = l1.copy().next_to(exprs[-2], DOWN)

        self.play(FadeIn(exprs[:2]), FadeIn(sym), FadeIn(l1))
        self.wait(1)

        ################################################################################
        exp = (
            VGroup(
                MathTex(r"\text{A} \times \text{D} = 10 \times 13 = 130"),
                MathTex(r"\text{res} = 130 \;\%\; 16 = 2"),
                MathTex(r"\text{carr} = 130 \;/\; 16 = 8"),
            )
            .scale(0.6)
            .arrange(DOWN, aligned_edge=LEFT)
            .next_to(exprs[1], RIGHT, buff=1)
        )
        carry = MathTex("8").scale(0.7).set_color(RED).next_to(exprs[0][1], UP)
        self.play(Write(exp))
        self.play(Write(exprs[2][2]))
        self.play(Write(carry))
        self.play(FadeOut(exp))
        self.wait(0.1)

        ################################################################################
        exp = (
            VGroup(
                MathTex(r"8 + \text{A} \times 3 = 38"),
                MathTex(r"\text{res} = 38 \;\%\; 16 = 6"),
                MathTex(r"\text{carr} = 38 \;/\; 16 = 2"),
            )
            .scale(0.6)
            .arrange(DOWN, aligned_edge=LEFT)
            .next_to(exprs[1], RIGHT, buff=1)
        )
        self.play(Write(exp))
        self.play(Write(exprs[2][1]))
        self.play(Write(exprs[2][0]))
        self.play(FadeOut(exp))
        self.wait(0.2)

        ################################################################################
        self.play(FadeIn(exprs[3:]), FadeIn(l2))
        self.wait(3)
