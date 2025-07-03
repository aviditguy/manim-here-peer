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


class BinaryToDecimal(Scene):
    def construct(self):
        label = MathTex(r"(1100100.01011100)_{{{2}}}").scale(0.8).shift(UP * 1.5)
        warr = (
            Array(data=list("1100100"), cell_width=0.7, index_from=6, index_step=-1)
            .to_edge(LEFT)
            .shift(RIGHT * 0.4)
        )
        farr = (
            Array(data=list("01011100"), cell_width=0.7, index_from=-1, index_step=-1)
            .to_edge(RIGHT)
            .shift(LEFT)
        )
        self.add(label, warr, farr)
        self.wait(1)

        warr.highlight_cell(self, 0, 1, 4, fill=RED_E)
        self.wait(1)
        weqs = (
            VGroup(MathTex(r"= 1 \cdot 2^6 + 2^5 + 2^2"), MathTex("= 100"))
            .scale(0.7)
            .arrange(DOWN, aligned_edge=LEFT)
            .next_to(warr, DOWN, buff=0.4)
        )
        self.play(Write(weqs))
        self.wait(1)

        farr.highlight_cell(self, 1, 3, 4, 5, fill=BLUE_E)
        self.wait(1)
        feqs = (
            VGroup(
                MathTex(r"= 1 \cdot 2^{-2} + 2^{-4} + 2^{-5} + 2^{-6}"),
                MathTex(r"\approx 0.36"),
            )
            .scale(0.7)
            .arrange(DOWN, aligned_edge=LEFT)
            .next_to(farr, DOWN, buff=0.4)
        )
        self.play(Write(feqs))
        self.wait(1)

        self.play(label.animate.shift(LEFT * 2))
        res = MathTex("100.36").scale(0.8).next_to(label, RIGHT, buff=1)
        self.play(Write(res))
        self.wait(2)


class BinaryToHex(Scene):
    def construct(self):
        label = MathTex(r"(1100100.01011100)_{{{2}}}").scale(0.8).shift(UP * 1.5)
        warr = (
            Array(data=list("1100100"), cell_width=0.6, index_from=6, index_step=-1)
            .to_edge(LEFT)
            .shift(RIGHT)
        )
        farr = (
            Array(data=list("01011100"), cell_width=0.6, index_from=-1, index_step=-1)
            .to_edge(RIGHT)
            .shift(LEFT)
        )
        self.add(label, warr, farr)
        self.wait(1)

        arrright = Arrow(
            start=farr.get_left(),
            end=farr.get_right(),
            tip_length=0.2,
            stroke_width=2,
            buff=0,
        ).next_to(farr, UP, buff=0.1)
        self.play(GrowArrow(arrright))
        self.wait(1)

        arrleft = Arrow(
            start=warr.get_right(),
            end=warr.get_left(),
            tip_length=0.2,
            stroke_width=2,
            buff=0,
        ).next_to(warr, UP, buff=0.1)
        self.play(GrowArrow(arrleft))
        self.wait(1)

        fl1 = MathTex("5").scale(0.7).next_to(farr, DOWN, buff=0.3).shift(LEFT * 1.2)
        fl2 = (
            MathTex(r"\text{12(C)}")
            .scale(0.7)
            .next_to(farr, DOWN, buff=0.3)
            .shift(RIGHT * 1.2)
        )
        fres = (
            MathTex(r"\text{(5C)}_{{{16}}}")
            .scale(0.7)
            .next_to(farr, DOWN, buff=0.3)
            .shift(RIGHT * 0.2)
        )

        farr.highlight_cell(self, 0, 1, 2, 3, fill=RED_E)
        self.play(Write(fl1))
        self.wait(0.5)
        farr.highlight_cell(self, 4, 5, 6, 7, fill=BLUE_E)
        self.play(Write(fl2))
        self.wait(0.5)
        self.play(ReplacementTransform(VGroup(fl1, fl2), fres))
        self.wait(1)

        warr.highlight_cell(self, 6, 5, 4, 3, fill=BLUE_E)
        warr.highlight_cell(self, 2, 1, 0, fill=RED_E)
        self.wait(1)
        warr.prepend_cell(self, values=[0])
        warr.highlight_cell(self, 0, fill=RED_E)
        self.wait(1)

        wl1 = MathTex("6").scale(0.7).next_to(warr, DOWN, buff=0.3).shift(LEFT * 1.2)
        wl2 = MathTex("4").scale(0.7).next_to(warr, DOWN, buff=0.3).shift(RIGHT * 1.2)
        wres = MathTex(r"(64)_{{{16}}}").scale(0.7).next_to(warr, DOWN, buff=0.3)
        self.play(Write(wl1), Write(wl2))
        self.wait(0.5)
        self.play(ReplacementTransform(VGroup(wl1, wl2), wres))
        self.wait(1)

        self.play(label.animate.shift(LEFT * 2))
        res = (
            MathTex(r"\text{(64.5C)}_{{{16}}}").scale(0.8).next_to(label, RIGHT, buff=1)
        )
        self.play(Write(res))
        self.wait(2)


class HexToBinary(Scene):
    def construct(self):
        label = MathTex(r"\text{(64.5C)}_{{{16}}}").scale(0.8).shift(UP * 1.1)
        arr = Array(data=list("64.5C"), cell_width=1.5, stroke_width=0, index=False)
        self.add(label, arr)
        self.wait(1)

        b = VGroup(
            MathTex("0110").scale(0.7).next_to(arr.get_cell(0), DOWN, buff=0.4),
            MathTex("0100").scale(0.7).next_to(arr.get_cell(1), DOWN, buff=0.4),
            MathTex("0101").scale(0.7).next_to(arr.get_cell(3), DOWN, buff=0.4),
            MathTex("1100").scale(0.7).next_to(arr.get_cell(4), DOWN, buff=0.4),
        )
        self.play(Write(b), run_time=3)
        self.wait(1)

        self.play(label.animate.shift(LEFT * 2))
        res = (
            MathTex("(1100100.01011100)_{{{2}}}")
            .scale(0.8)
            .next_to(label, RIGHT, buff=1)
        )
        self.play(Write(res))
        self.wait(2)
