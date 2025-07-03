from manim import *


class IntegerToBinary(Scene):
    def construct(self):
        eqs = VGroup(
            MathTex("100", "=", "2", r"\times", "50", "+", "0"),
            MathTex("50", "=", "2", r"\times", "25", "+", "0"),
            MathTex("25", "=", "2", r"\times", "12", "+", "1"),
            MathTex("12", "=", "2", r"\times", "6", "+", "0"),
            MathTex("6", "=", "2", r"\times", "3", "+", "0"),
            MathTex("3", "=", "2", r"\times", "1", "+", "1"),
            MathTex("1", "=", "2", r"\times", "0", "+", "1"),
        ).scale(0.7)

        x, y, z, buff = -1.4, 2, 0, 0.5
        for idx, eq in enumerate(eqs):
            eq[0].move_to([x, y - idx * buff, z], aligned_edge=RIGHT)
            eq[1:].next_to(eq[0], RIGHT)
            eq[4].next_to(eq[3], RIGHT, buff=0.3, aligned_edge=RIGHT)
            eq[5:].move_to([x + 2.1, y - idx * buff, z])

        self.add(eqs)
        self.wait(1)

        arrup = Arrow(
            start=eqs.get_bottom(),
            end=eqs.get_top(),
            tip_length=0.2,
            stroke_width=2,
            buff=0,
        ).next_to(eqs, RIGHT, buff=0.4)
        self.play(GrowArrow(arrup))
        self.wait(1)

        res = (
            MathTex("(1100100)_{{{2}}}")
            .scale(0.8)
            .next_to(eqs, DOWN, buff=0.4)
            .shift(RIGHT * 0.5)
        )
        self.play(Write(res))
        self.wait(2)


class FracToBinary(Scene):
    def construct(self):
        eqs = VGroup(
            MathTex("0.36", r"\times", "2", "=", "0.72", "0"),
            MathTex("0.72", r"\times", "2", "=", "1.44", "1"),
            MathTex("0.44", r"\times", "2", "=", "0.88", "0"),
            MathTex("0.88", r"\times", "2", "=", "1.76", "1"),
            MathTex("0.76", r"\times", "2", "=", "1.52", "1"),
            MathTex("0.52", r"\times", "2", "=", "1.04", "1"),
            MathTex("0.04", r"\times", "2", "=", "0.08", "0"),
            MathTex("0.08", r"\times", "2", "=", "0.16", "0"),
        ).scale(0.7)

        x, y, z, buff = -1.2, 2, 0, 0.5
        for idx, eq in enumerate(eqs):
            eq[0].move_to([x, y - idx * buff, z], aligned_edge=RIGHT)
            eq[1:].next_to(eq[0], RIGHT)
            eq[5].move_to([x + 2.4, y - idx * buff, z])

        self.add(eqs)
        self.wait(1)

        s1 = SurroundingRectangle(eqs[1][4])
        s2 = SurroundingRectangle(eqs[1][5], color=RED_E)
        s3 = SurroundingRectangle(eqs[2][0])
        self.play(Write(s1), Write(s2, run_time=1.5))
        self.play(ReplacementTransform(s1, s3))
        self.wait(1)
        self.play(FadeOut(s2), FadeOut(s3))

        arrdwn = Arrow(
            start=eqs.get_top(),
            end=eqs.get_bottom(),
            tip_length=0.2,
            stroke_width=2,
            buff=0,
        ).next_to(eqs, RIGHT, buff=0.4)
        self.play(GrowArrow(arrdwn))
        self.wait(1)

        res = (
            MathTex("(0.01011100)_{{{2}}}")
            .scale(0.8)
            .next_to(eqs, DOWN, buff=0.4)
            .shift(RIGHT * 0.5)
        )
        self.play(Write(res))
        self.wait(2)


class DecimalToHex(Scene):
    def construct(self):
        label = MathTex("100.36").scale(0.8).to_edge(UP)

        weq = VGroup(
            MathTex("100", "=", "16", r"\times", "6", "+", "4"),
            MathTex("6", "=", "16", r"\times", "0", "+", "6"),
        ).scale(0.7)

        feq = VGroup(
            MathTex("0.36", r"\times", "16", "=", "5.76", "5"),
            MathTex("0.76", r"\times", "16", "=", "12.16", r"12\text{(C)}"),
            MathTex("0.16", r"\times", "16", "=", "2.56", "2"),
            MathTex("0.56", r"\times", "16", "=", "8.96", "8"),
            MathTex("0.96", r"\times", "16", "=", "15.36", r"15\text{(F)}"),
            MathTex("0.36", r"\times", "16", "=", "5.76", "5"),
            MathTex("0.76", r"\times", "16", "=", "12.16", r"12\text{(C)}"),
            MathTex("0.16", r"\times", "16", "=", "2.56", "2"),
        ).scale(0.7)

        x, y, z, buff = -4.2, 2, 0, 0.5
        for idx, eq in enumerate(weq):
            eq[0].move_to([x, y - idx * buff, z], aligned_edge=RIGHT)
            eq[1:].next_to(eq[0], RIGHT)
            eq[4].next_to(eq[3], RIGHT, buff=0.3, aligned_edge=RIGHT)
            eq[5:].move_to([x + 2.1, y - idx * buff, z])

        x, y, z, buff = 1.5, 2, 0, 0.5
        for idx, eq in enumerate(feq):
            eq[0].move_to([x, y - idx * buff, z], aligned_edge=RIGHT)
            eq[1:].next_to(eq[0], RIGHT)
            eq[5].move_to([x + 2.7, y - idx * buff, z], aligned_edge=LEFT)

        self.add(label, weq, feq)
        self.wait(1)

        arrup = Arrow(
            start=weq.get_bottom(),
            end=weq.get_top(),
            tip_length=0.2,
            stroke_width=2,
            buff=0,
        ).next_to(weq, RIGHT, buff=0.4)
        self.play(GrowArrow(arrup))
        self.wait(1)

        res = (
            MathTex(r"(64)_{{{16}}}")
            .scale(0.7)
            .next_to(weq, DOWN, buff=0.4)
            .shift(RIGHT * 0.5)
        )
        self.play(Write(res))
        self.wait(1)

        arrdwn = Arrow(
            start=feq.get_top(),
            end=feq.get_bottom(),
            tip_length=0.2,
            stroke_width=2,
            buff=0,
        ).next_to(feq, RIGHT, buff=0.4)
        self.play(GrowArrow(arrdwn))
        self.wait(1)

        res = (
            MathTex(r"\text{(0.5C28F5C2)}_{{{16}}}")
            .scale(0.7)
            .next_to(feq, DOWN, buff=0.4)
            .shift(RIGHT * 0.5)
        )
        self.play(Write(res))
        self.wait(1)

        self.play(label.animate.shift(LEFT * 1.5))
        res = (
            MathTex(r"\text{(64.5C28F5C2)}_{{{16}}}")
            .scale(0.8)
            .next_to(label, RIGHT, buff=1)
        )
        self.play(Write(res))
        self.wait(2)
