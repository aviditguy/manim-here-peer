// Show links with a box around them or filled with a color
#show link: this => {
  let show-type = "box" // "box" or "filled", see below
  let label-color = green
  let default-color = rgb("#ff66ff")
  
  if show-type == "box" {
    if type(this.dest) == label {
      // Make the box bound the entire text:
      set text(bottom-edge: "bounds", top-edge: "bounds")
      box(this, stroke: label-color + 1pt)
    } else {
      set text(bottom-edge: "bounds", top-edge: "bounds")
      box(this, stroke: default-color + 1pt)
    }
  } else if show-type == "filled" {
    if type(this.dest) == label {
      text(this, fill: label-color)
    } else {
      text(this, fill: default-color)
    }
  } else {
    this
  }
}

#show outline.entry.where(
  level: 1
): set block(above: 1.2em)

#outline()

#line(start:(10%,20pt), end:(0%,50pt))

#line(length: 100%, stroke: 1pt)
#include "decimalToBase.typ"
#line(length: 100%, stroke: 1pt)
#include "binaryToBase.typ"
#line(length: 100%, stroke: 1pt)
#include "hexToBase.typ"
#line(length: 100%, stroke: 1pt)
#include "conversion_when_decimal_is_power_of_2.typ"
#line(length: 100%, stroke: 1pt)

