# import statements
import isTouching
import random
# code
# values hardcoded as placeholder
rect_w, rect_h = 10, 10
noofshapes = 14
coords = [[0, 0], [0, 2], [2, 2], [2, 3], [3, 3], [3, 1], [2, 1], [2, 0]]
shape_w, shape_h = isTouching.finddimensions(coords)
shapedict = {}
# Creating shape objects at random coordinates
for i in range(1, noofshapes + 1):
    variablename = "s" + str(i)
    shapedict.update({variablename: isTouching.Shape(random.randint(0, rect_w - shape_w), random.randint(0, rect_h - shape_h), coords)})
    print(shapedict[variablename].getlines())