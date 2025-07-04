= Convert Binary $(1100100.01011100)_(2)$ to Decimal
+ Split Integer and Fraction Binary Parts
+ Indexing in Integer Part starts from $0- n$ from right to left, Fractional Part from left to right at -1 
+ Add all the bits, value of each bit is $= text("bit") dot 2^(text("index"))$

#let warr = (1, 1, 0, 0, 1, 0, 0)
#let farr = (0,1,0,1,1,1,0,0)

#grid(
   columns: 2,
   gutter: 25pt,
   [
#for (index, value) in warr.enumerate(){
box()[
#let color = if value == 1 {green}
#let idx = warr.len() - index - 1
#stack(
   box(inset: 8pt)[#text(size: 10pt)[#idx]],
   box(inset: 8pt,width:25pt, fill: color, stroke: black)[#value]
)]
}
   ],
   [
#for (index, value) in range(-1, -9, step:-1).zip(farr){
box()[
#let color = if value == 1 {green}
#stack(
   box(inset: 8pt,width:15pt)[#text(size: 10pt)[#index]],
   box(inset: 8pt,width:25pt, fill: color, stroke: black)[#value]
)]
}
   ],
   [
      $= 1 dot 2^6 + 2^5 + 2^2\
      = 100$
   ],
   [
      $= 1 dot 2^(-2) + 2^(-4) + 2^(-5) + 2^(-6)\
      approx 0.36$
   ]
)

*Decimal Representation of Binary Number is $= 100.36$*


= Convert Binary $(1100100.01011100)_(2)$ to Hexadecimal
+ Each hex corresponds to $4$ bin digits so we make groups of $4$
+ For Integer Part grouping from right to left and left to right for fractional part
+ If there is no sufficient bits to complete group we fill in with $0$

#link("./assets/BinaryToHex.mp4")[Binary To Hex Conversion Video]

*Hexadecimal Representation of Binary Number is $ = 64."5C"$*

