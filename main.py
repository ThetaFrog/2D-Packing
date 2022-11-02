# import statements
import isTouching
import random


# classes
class Shape:
    def __init__(self, x, y, coordsforshape):  # coords forshape formatted as [[x,y],[x,y]]
        self.x = x
        self.y = y
        self.coordsforshape = coordsforshape

    def shiftcoords(self):
        shiftedcoords = []
        for i in range(0, len(self.coordsforshape)):

            shiftedcoords.append([self.coordsforshape[i][0] + self.x, self.coordsforshape[i][1] + self.y])
        return shiftedcoords

    def getlines(self):
        linesforshape = []
        shiftedcoords = self.shiftcoords()
        for i in range(0, len(shiftedcoords)):
            if i < len(self.coordsforshape) - 1:
                linesforshape.append([shiftedcoords[i], shiftedcoords[i + 1]])
            else:
                linesforshape.append([shiftedcoords[i], shiftedcoords[0]])
        return linesforshape


# functions
def finddimensions(shape_coords):
    x_all = []
    y_all = []
    for j in shape_coords:
        x_all.append(j[0])
        y_all.append(j[1])
    return max(x_all), max(y_all)


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