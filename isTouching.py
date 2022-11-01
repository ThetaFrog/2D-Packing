# import statements
import random


# classes
class Shape:
    def __init__(self, x, y, coordsforshape):  # coords forshape formatted as [[x,y],[x,y]]
        self.x = x
        self.y = y
        self.coordsforshape = coordsforshape

    def shiftcoords(self):
        for i in range(0, len(self.coordsforshape)):
            self.coordsforshape[i][0] = self.coordsforshape[i][0] + self.x
            self.coordsforshape[i][1] = self.coordsforshape[i][1] + self.y
        return self.coordsforshape

    def getlines(self):
        self.shiftcoords()
        linesforshape = []
        for i in range(0, len(self.coordsforshape)):
            if i < len(self.coordsforshape) - 1:
                linesforshape.append([self.coordsforshape[i], self.coordsforshape[i + 1]])
            else:
                linesforshape.append([self.coordsforshape[i], self.coordsforshape[0]])
        return linesforshape


# functions
def finddimensions(shape_coords):
    x_all = []
    y_all = []
    for i in shape_coords:
        x_all.append(i[0])
        y_all.append(i[1])
    return max(x_all), max(y_all)


# code
# values hardcoded as placeholder
rect_w, rect_h = 10, 10
noofshapes = 2
coords = [[0, 0], [0, 2], [2, 2], [2, 3], [3, 3], [3, 1], [2, 1], [2, 0]]
shape_w, shape_h = finddimensions(coords)
shapedict = {}
for i in range(1, noofshapes + 1):
    variablename = "s" + str(i)
    shapedict.update(
        {variablename: Shape(round(random.uniform(0, rect_w - shape_w), 2), round(random.uniform(0, rect_h - shape_h), 2), coords)})

