from manim import *
from helper import Array


class BinaryAdd(Scene):
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

        # clear the scene
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)

        # binary addition of 22 + 10
        exprs = VGroup(
            MathTex(
                r"22\qquad", r"\quad\;\;1\quad", r"0\quad", r"1\quad", r"1\quad", "0"
            ),
            MathTex(
                r"10\qquad", r"\quad\;\;0\quad", r"1\quad", r"0\quad", r"1\quad", "0"
            ),
            MathTex(
                r"32\qquad", r"1\quad", r"0\quad", r"0\quad", r"0\quad", r"0\quad", "0"
            ),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        exprs[-1].shift(DOWN * 0.3)

        sym = Text("+").scale(0.7).next_to(exprs[1], LEFT, buff=0.4)

        l = Line(
            start=exprs[-1][0].get_left(), end=exprs[-1][-1].get_right(), stroke_width=1
        ).next_to(exprs[1], DOWN, buff=0.3)

        carry = VGroup(
            MathTex("1").scale(0.6).set_color(RED).next_to(exprs[0][3], UP),
            MathTex("1").scale(0.6).set_color(RED).next_to(exprs[0][2], UP),
            MathTex("1").scale(0.6).set_color(RED).next_to(exprs[0][1], UP),
            MathTex("1")
            .scale(0.6)
            .set_color(RED)
            .next_to(exprs[0][0], UP)
            .shift(RIGHT * 1.4),
        )

        sum1 = VGroup(exprs, sym, l, carry)
        self.add(sum1)
        self.wait(2)

        # clear the scene
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)

        # binary addition of 30 + 15
        exprs = VGroup(
            MathTex(
                r"30\qquad", r"\quad\;\;1\quad", r"1\quad", r"1\quad", r"1\quad", "0"
            ),
            MathTex(
                r"15\qquad", r"\quad\;\;0\quad", r"1\quad", r"1\quad", r"1\quad", "1"
            ),
            MathTex(
                r"45\qquad", r"1\quad", r"0\quad", r"1\quad", r"1\quad", r"0\quad", "1"
            ),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        exprs[-1].shift(DOWN * 0.3)

        sym = Text("+").scale(0.7).next_to(exprs[1], LEFT, buff=0.4)

        l = Line(
            start=exprs[-1][0].get_left(), end=exprs[-1][-1].get_right(), stroke_width=1
        ).next_to(exprs[1], DOWN, buff=0.3)

        carry = VGroup(
            MathTex("1").scale(0.6).set_color(RED).next_to(exprs[0][3], UP),
            MathTex("1").scale(0.6).set_color(RED).next_to(exprs[0][2], UP),
            MathTex("1").scale(0.6).set_color(RED).next_to(exprs[0][1], UP),
            MathTex("1")
            .scale(0.6)
            .set_color(RED)
            .next_to(exprs[0][0], UP)
            .shift(RIGHT * 1.4),
        )

        sum1 = VGroup(exprs, sym, l, carry)
        self.add(sum1)
        self.wait(2)

        self.play(sum1.animate.scale(0.6).to_edge(LEFT).shift(RIGHT))
        self.wait(2)

        prog = VGroup(
            MathTex(r"\text{carry} = 0"),
            MathTex(r"\text{sum} = 0 + 1 + 0 = 1"),
            MathTex(r"\text{res} = \text{sum \% 2} = 1"),
            MathTex(r"\text{carry} = \text{sum / 2} = 0"),
        ).scale(0.6).arrange(DOWN, aligned_edge=LEFT).shift(RIGHT)

        self.play(Write(prog[0]))
        self.wait(1)
        self.play(Write(prog[1]))
        self.wait(1)
        self.play(Write(prog[2]))
        self.wait(1)
        self.play(Write(prog[3]))
        self.wait(1)

        self.play(prog[1].animate.become(MathTex(r"\text{sum} = 1 + 1 + 0 = 2").scale(0.6).move_to(prog[1])))
        self.wait(1)
        self.play(prog[2].animate.become(MathTex(r"\text{res} = \text{sum \% 2} = 0").scale(0.6).move_to(prog[2])))
        self.wait(1)
        self.play(prog[3].animate.become(MathTex(r"\text{carry} = \text{sum / 2} = 1").scale(0.6).move_to(prog[3])))
        self.wait(3)
