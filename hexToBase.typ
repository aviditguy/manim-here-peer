= Convert Hexadecimal $(64."5C")_(16)$ to Binary
+ Since each hex digit corresponds to $4$ binary bits, just expand each hex digit

#for (hex,bin) in ("6", "4", "5", "C").zip(("0110", "0100", "0101", "1100")){
box()[
#stack(
   box(inset: 8pt,width:55pt,height:16pt)[#hex],
   box(inset: 8pt,width:55pt)[#bin]
)]
}

*Binary Representation of $64."5C" = (1100100.01011100)_(2)$*


= Convert Hexadecimal $(64."5C")_(16)$ to Decimal
+ There is no direct way to convert Hex into Decimal
+ First convert it to Binary then from Binary to Decimal

*Decimal Representation of $quad 64."5C" arrow.r.long (1100100.01011100)_(2)arrow.r.long 100.36$*
