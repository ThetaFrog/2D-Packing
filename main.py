# import statements
import isTouching
import shape
import svgcommands
import random

# code
# values hardcoded as placeholder
rect_w, rect_h = 10, 10
noofshapes = 14
coords = [[0, 0], [0, 2], [2, 2], [2, 3], [3, 3], [3, 1], [2, 1], [2, 0]]
shape_w, shape_h = shape.finddimensions(coords)
shapedict = {}
# Creating shape objects at random coordinates
a = []
for i in range(1, noofshapes + 1):
    variablename = "s" + str(i)
    shapedict.update({variablename: shape.Shape(random.randint(0, rect_w - shape_w), random.randint(0, rect_h - shape_h), coords)})
    a.append(shapedict[variablename].getlines())
svgcommands.svgout(10, 10, a)
    # for j in range(1, noofshapes + 1):
        # if isTouching.checktouching(shapedict[variablename], shapedict["s" + str(j)]) == "intersecting":

