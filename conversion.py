from manim import *
from helper import Array


class DecimalToBinary(Scene):
    def construct(self):
        weqs = VGroup(
            MathTex("100", "=", "2", r"\times", "50", "+", "0"),
            MathTex("50", "=", "2", r"\times", "25", "+", "0"),
            MathTex("25", "=", "2", r"\times", "12", "+", "1"),
            MathTex("12", "=", "2", r"\times", "6", "+", "0"),
            MathTex("6", "=", "2", r"\times", "3", "+", "0"),
            MathTex("3", "=", "2", r"\times", "1", "+", "1"),
            MathTex("1", "=", "2", r"\times", "0", "+", "1"),
        ).scale(0.6)

        feqs = VGroup(
            MathTex("0.36", r"\times", "2", "=", "0.72", "0"),
            MathTex("0.72", r"\times", "2", "=", "1.44", "1"),
            MathTex("0.44", r"\times", "2", "=", "0.88", "0"),
            MathTex("0.88", r"\times", "2", "=", "1.76", "1"),
            MathTex("0.76", r"\times", "2", "=", "1.52", "1"),
            MathTex("0.52", r"\times", "2", "=", "1.04", "1"),
            MathTex("0.04", r"\times", "2", "=", "0.08", "0"),
            MathTex("0.08", r"\times", "2", "=", "0.16", "0"),
        ).scale(0.6)

        x, y, z, buff = -4.5, 2, 0, 0.4
        for idx, eq in enumerate(weqs):
            eq[0].move_to([x, y - idx * buff, z], aligned_edge=RIGHT)
            eq[1:].next_to(eq[0], RIGHT)
            eq[4].next_to(eq[3], RIGHT, buff=0.3, aligned_edge=RIGHT)
            eq[5:].move_to([x + 2.1, y - idx * buff, z])

        arrup = Arrow(
            start=weqs.get_bottom(),
            end=weqs.get_top(),
            tip_length=0.2,
            stroke_width=2,
            buff=0,
        ).next_to(weqs, RIGHT, buff=0.4)

        wres = (
            MathTex("(1100100)_{{{2}}}")
            .scale(0.7)
            .next_to(weqs, DOWN, buff=0.4)
            .shift(RIGHT * 0.4)
        )

        x, y, z, buff = 1, 2, 0, 0.4
        for idx, eq in enumerate(feqs):
            eq[0].move_to([x, y - idx * buff, z], aligned_edge=RIGHT)
            eq[1:].next_to(eq[0], RIGHT)
            eq[5].move_to([x + 2.4, y - idx * buff, z])

        s1 = SurroundingRectangle(feqs[1][4], stroke_width=2)
        s2 = SurroundingRectangle(feqs[1][5], color=RED_E, stroke_width=2)
        s3 = SurroundingRectangle(feqs[2][0], stroke_width=2)

        arrdwn = Arrow(
            start=feqs.get_top(),
            end=feqs.get_bottom(),
            tip_length=0.2,
            stroke_width=2,
            buff=0,
        ).next_to(feqs, RIGHT, buff=0.4)

        fres = (
            MathTex("(0.01011100)_{{{2}}}")
            .scale(0.7)
            .next_to(feqs, DOWN, buff=0.4)
            .shift(RIGHT * 0.3)
        )

        self.add(weqs, arrup, wres, feqs, s1, s2, s3, arrdwn, fres)


class DecimalToHexadecimal(Scene):
    def construct(self):
        weqs = VGroup(
            MathTex("100", "=", "16", r"\times", "6", "+", "4"),
            MathTex("6", "=", "16", r"\times", "0", "+", "6"),
        ).scale(0.6)

        feqs = VGroup(
            MathTex("0.36", r"\times", "16", "=", "5.76", "5"),
            MathTex("0.76", r"\times", "16", "=", "12.16", r"12\text{(C)}"),
            MathTex("0.16", r"\times", "16", "=", "2.56", "2"),
            MathTex("0.56", r"\times", "16", "=", "8.96", "8"),
            MathTex("0.96", r"\times", "16", "=", "15.36", r"15\text{(F)}"),
            MathTex("0.36", r"\times", "16", "=", "5.76", "5"),
            MathTex("0.76", r"\times", "16", "=", "12.16", r"12\text{(C)}"),
            MathTex("0.16", r"\times", "16", "=", "2.56", "2"),
        ).scale(0.6)

        x, y, z, buff = -4.2, 2, 0, 0.4
        for idx, eq in enumerate(weqs):
            eq[0].move_to([x, y - idx * buff, z], aligned_edge=RIGHT)
            eq[1:].next_to(eq[0], RIGHT)
            eq[4].next_to(eq[3], RIGHT, buff=0.3, aligned_edge=RIGHT)
            eq[5:].move_to([x + 2.1, y - idx * buff, z])

        arrup = Arrow(
            start=weqs.get_bottom(),
            end=weqs.get_top(),
            tip_length=0.2,
            stroke_width=2,
            buff=0,
        ).next_to(weqs, RIGHT, buff=0.4)

        wres = (
            MathTex(r"(64)_{{{16}}}")
            .scale(0.7)
            .next_to(weqs, DOWN, buff=0.4)
            .shift(RIGHT * 0.3)
        )

        x, y, z, buff = 1, 2, 0, 0.4
        for idx, eq in enumerate(feqs):
            eq[0].move_to([x, y - idx * buff, z], aligned_edge=RIGHT)
            eq[1:].next_to(eq[0], RIGHT)
            eq[5].move_to([x + 2.7, y - idx * buff, z], aligned_edge=LEFT)

        s1 = SurroundingRectangle(feqs[1][4], stroke_width=2)
        s2 = SurroundingRectangle(feqs[1][5], color=RED_E, stroke_width=2)
        s3 = SurroundingRectangle(feqs[2][0], stroke_width=2)

        arrdwn = Arrow(
            start=feqs.get_top(),
            end=feqs.get_bottom(),
            tip_length=0.2,
            stroke_width=2,
            buff=0,
        ).next_to(feqs, RIGHT, buff=0.4)

        fres = (
            MathTex(r"\text{(0.5C28F5C2)}_{{{16}}}")
            .scale(0.7)
            .next_to(feqs, DOWN, buff=0.4)
            .shift(RIGHT * 0.4)
        )

        self.add(weqs, arrup, wres, feqs, s1, s2, s3, arrdwn, fres)


class BinaryToDecimal(Scene):
    def construct(self):
        warr = (
            Array(
                data=list("1100100"),
                cell_width=0.6,
                cell_height=0.5,
                index_from=6,
                index_step=-1,
            )
            .to_edge(LEFT)
            .shift(RIGHT * 1.2)
        )
        farr = (
            Array(
                data=list("01011100"),
                cell_width=0.6,
                cell_height=0.5,
                index_from=-1,
                index_step=-1,
            )
            .to_edge(RIGHT)
            .shift(LEFT * 1.1)
        )

        warr.highlight_cell(self, 0, 1, 4, fill=GREEN_E, animate=False)
        farr.highlight_cell(self, 1, 3, 4, 5, fill=GREEN_E, animate=False)

        weqs = (
            VGroup(MathTex(r"= 1 \cdot 2^6 + 2^5 + 2^2"), MathTex("= 100"))
            .scale(0.6)
            .arrange(DOWN, aligned_edge=LEFT)
            .next_to(warr, DOWN, buff=0.4, aligned_edge=LEFT)
        )

        feqs = (
            VGroup(
                MathTex(r"= 1 \cdot 2^{-2} + 2^{-4} + 2^{-5} + 2^{-6}"),
                MathTex(r"\approx 0.36"),
            )
            .scale(0.6)
            .arrange(DOWN, aligned_edge=LEFT)
            .next_to(farr, DOWN, buff=0.4, aligned_edge=LEFT)
        )

        self.add(warr, farr, weqs, feqs)


class BinaryToHexadecimal(Scene):
    def construct(self):
        warr = (
            Array(
                data=list("01100100"),
                cell_width=0.6,
                cell_height=0.5,
                stroke_width=0,
                index=False,
            )
            .to_edge(LEFT)
            .shift(RIGHT * 1.2)
        )
        warr.get_label(0).set_color("RED")

        farr = (
            Array(
                data=list("01011100"),
                cell_width=0.6,
                cell_height=0.5,
                stroke_width=0,
                index=False,
            )
            .to_edge(RIGHT)
            .shift(LEFT * 1.1)
        )

        left = Arrow(
            start=warr.get_label(7).get_center(),
            end=warr.get_label(0).get_center(),
            tip_length=0.2,
            stroke_width=2,
            buff=0,
        ).next_to(warr, UP, buff=0.1)

        right = Arrow(
            start=farr.get_label(0).get_center(),
            end=farr.get_label(7).get_center(),
            tip_length=0.2,
            stroke_width=2,
            buff=0,
        ).next_to(farr, UP, buff=0.1)

        b1 = BraceBetweenPoints(
            warr.get_label(0).get_center(), warr.get_label(3).get_center()
        ).shift(DOWN * 0.1)
        b2 = BraceBetweenPoints(
            warr.get_label(4).get_center(), warr.get_label(7).get_center()
        ).shift(DOWN * 0.1)
        b3 = BraceBetweenPoints(
            farr.get_label(0).get_center(), farr.get_label(3).get_center()
        ).shift(DOWN * 0.1)
        b4 = BraceBetweenPoints(
            farr.get_label(4).get_center(), farr.get_label(7).get_center()
        ).shift(DOWN * 0.1)

        h1 = MathTex("6").next_to(b1, DOWN).scale(0.7)
        h2 = MathTex("4").next_to(b2, DOWN).scale(0.7)
        h3 = MathTex("5").next_to(b3, DOWN).scale(0.7)
        h4 = MathTex(r"\text{C}").next_to(b4, DOWN).scale(0.7)

        self.add(warr, farr, left, right, b1, b2, b3, b4, h1, h2, h3, h4)


class HexadecimalToBinary(Scene):
    def construct(self):
        arr = Array(data=list("645C"), cell_width=1.5, stroke_width=0, index=False)

        b = VGroup(
            MathTex("0110").scale(0.7).next_to(arr.get_cell(0), DOWN, buff=0.3),
            MathTex("0100").scale(0.7).next_to(arr.get_cell(1), DOWN, buff=0.3),
            MathTex("0101").scale(0.7).next_to(arr.get_cell(2), DOWN, buff=0.3),
            MathTex("1100").scale(0.7).next_to(arr.get_cell(3), DOWN, buff=0.3),
        )

        self.add(arr, b)


class BinaryAddition(Scene):
    def construct(self):
        arr1 = Array(
            data=[22, " ", " ", 1, 0, 1, 1, 0],
            cell_width=0.6,
            cell_height=0.5,
            stroke_width=0,
            index=False,
            fs=18,
        )
        arr2 = Array(
            data=[10, " ", " ", 0, 1, 0, 1, 0],
            cell_width=0.6,
            cell_height=0.5,
            stroke_width=0,
            index=False,
            fs=18,
        ).next_to(arr1, DOWN, buff=0)

        arr3 = Array(
            data=[32, " ", 1, 0, 0, 0, 0, 0],
            cell_width=0.6,
            cell_height=0.5,
            stroke_width=0,
            index=False,
            fs=18,
        ).next_to(arr2, DOWN, buff=0, aligned_edge=RIGHT)

        sym = MathTex("+").scale(0.7).next_to(arr2, LEFT, buff=0.5)

        line = Line(start=arr2.get_left(), end=arr2.get_right(), buff=0).next_to(
            arr2, DOWN, buff=0
        )

        carry = VGroup(
            MathTex("1")
            .scale(0.4)
            .set_color(RED)
            .next_to(arr1.get_cell(5), UP, buff=0),
            MathTex("1")
            .scale(0.4)
            .set_color(RED)
            .next_to(arr1.get_cell(4), UP, buff=0),
            MathTex("1")
            .scale(0.4)
            .set_color(RED)
            .next_to(arr1.get_cell(3), UP, buff=0),
            MathTex("1")
            .scale(0.4)
            .set_color(RED)
            .next_to(arr1.get_cell(2), UP, buff=0),
        )

        self.add(arr1, arr2, arr3, sym, line, carry)


class BinarySubtraction(Scene):
    def construct(self):
        arr1 = Array(
            data=[22, " ", " ", 1, 0, 1, 1, 0],
            cell_width=0.6,
            cell_height=0.5,
            stroke_width=0,
            index=False,
            fs=18,
        )
        arr2 = Array(
            data=[10, " ", " ", 0, 1, 0, 1, 0],
            cell_width=0.6,
            cell_height=0.5,
            stroke_width=0,
            index=False,
            fs=18,
        ).next_to(arr1, DOWN, buff=0)

        arr3 = Array(
            data=[12, " ", " ", 0, 1, 1, 0, 0],
            cell_width=0.6,
            cell_height=0.5,
            stroke_width=0,
            index=False,
            fs=18,
        ).next_to(arr2, DOWN, buff=0, aligned_edge=RIGHT)

        sym = MathTex("-").scale(0.7).next_to(arr2, LEFT, buff=0.5)

        line = Line(start=arr2.get_left(), end=arr2.get_right(), buff=0).next_to(
            arr2, DOWN, buff=0
        )

        slash = Line(
            start=arr1.get_cell(3).get_corner(UR),
            end=arr1.get_cell(3).get_corner(DL),
            buff=0,
            color=RED,
            stroke_width=1,
        ).scale(0.5)

        carry = VGroup(
            MathTex("0")
            .scale(0.5)
            .set_color(RED)
            .next_to(arr1.get_cell(3), UP, buff=0),
            MathTex("10")
            .scale(0.5)
            .set_color(RED)
            .next_to(arr1.get_cell(4), UP, buff=0),
        )

        self.add(arr1, arr2, arr3, sym, line, slash, carry)


class BinaryMultiplication(Scene):
    def construct(self):
        arr1 = Array(
            data=[5, " ", " ", " ", 1, 0, 1],
            cell_width=0.6,
            cell_height=0.4,
            stroke_width=0,
            index=False,
            fs=18,
        )

        arr2 = Array(
            data=[4, " ", " ", " ", 1, 0, 0],
            cell_width=0.6,
            cell_height=0.4,
            stroke_width=0,
            index=False,
            fs=18,
        ).next_to(arr1, DOWN, buff=0)

        products = (
            VGroup(
                Array(
                    data=[" ", " ", " ", " ", 0, 0, 0],
                    cell_width=0.6,
                    cell_height=0.4,
                    stroke_width=0,
                    index=False,
                    fs=18,
                ),
                Array(
                    data=[" ", " ", " ", 0, 0, 0, 0],
                    cell_width=0.6,
                    cell_height=0.4,
                    stroke_width=0,
                    index=False,
                    fs=18,
                ),
                Array(
                    data=[" ", " ", 1, 0, 1, 0, 0],
                    cell_width=0.6,
                    cell_height=0.4,
                    stroke_width=0,
                    index=False,
                    fs=18,
                ),
            )
            .arrange(DOWN, buff=0)
            .next_to(arr2, DOWN, buff=0.1)
        )
        products[1].get_label(6).set_color(RED_E)
        products[2].get_label(5).set_color(RED_E)
        products[2].get_label(6).set_color(RED_E)

        res = Array(
            data=[20, " ", 1, 0, 1, 0, 0],
            cell_width=0.6,
            cell_height=0.4,
            stroke_width=0,
            index=False,
            fs=18,
        ).next_to(products, DOWN, buff=0.1)


class BinaryDivision(Scene):
    def construct(self):

        hline = Line(start=[0, 0, 0], end=[0, 0.5, 0], stroke_width=2)
        vline = Line(start=[0, 0.5, 0], end=[1.2, 0.5, 0], stroke_width=2)

        q1 = MathTex("100").scale(0.6).next_to(hline, LEFT, buff=0.2)
        q2 = MathTex("10111").scale(0.6).next_to(hline, RIGHT, buff=0.2)

        eq = (
            MathTex(r"\frac{23}{4} = 5 \cdot \frac{3}{4}")
            .scale(0.6)
            .next_to(q1, LEFT, buff=1)
        )

        quo = (
            MathTex(r"101 \quad \longrightarrow 5")
            .scale(0.6)
            .next_to(q2, UP, aligned_edge=LEFT, buff=0.3)
        )

        p1 = MathTex("100").scale(0.6).next_to(q2, DOWN, aligned_edge=LEFT)
        l1 = (
            vline.copy()
            .set_stroke_width(1)
            .scale(0.6)
            .next_to(p1, DOWN, buff=0.1)
            .shift(RIGHT * 0.2)
        )

        p2 = MathTex("111").scale(0.6).next_to(p1, DOWN).shift(RIGHT * 0.35)
        p3 = MathTex("100").scale(0.6).next_to(p2, DOWN)
        l2 = vline.copy().set_stroke_width(1).scale(0.4).next_to(p3, DOWN, buff=0.1)
        p4 = (
            MathTex(r"011 \quad \longrightarrow \text{remainder} = 3")
            .scale(0.6)
            .next_to(p3, DOWN, aligned_edge=LEFT)
        )

        self.add(hline, vline, eq, q1, q2, quo, p1, l1, p2, p3, l2, p4)
