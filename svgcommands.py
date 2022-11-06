# imports
import random

import svgwrite as sw


# Functions
def formatlines(lines, frame_w, frame_h):
    finallinelist = []
    for i in lines:
        finalstring = "M"
        for j in i:
            finalstring = finalstring + " " + str(j[0][0] * 35.43307) + "," + str((frame_h - j[0][1]) * 35.43307)
        finalstring = finalstring + " Z"
        finallinelist.append(finalstring)
    print(finallinelist)
    return finallinelist


def svgout(frame_w, frame_h, lines):
    dwg = sw.Drawing("output.svg")
    dwg.add(dwg.rect((0, 0), (frame_w * 35.43307, frame_h * 35.43307), style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"))
    dwg.save()
    for i in formatlines(lines, frame_w, frame_h):
        dwg.add(dwg.path(style="fill:rgb({}, {}, {});stroke:#000000;stroke-width:0px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1".format(random.randint(1, 25) * 10, random.randint(1, 25) * 10, random.randint(1, 25) * 10), d=i))
        dwg.save()
