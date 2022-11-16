# classes
class Shape:
    def __init__(self, x, y, coordsforshape):  # coords for shape formatted as [[x,y],[x,y]]
        self.x = x
        self.y = y
        self.coordsforshape = coordsforshape
        self.shiftshape(self.x, self.y)

    def shiftshape(self, shift_x, shift_y):
        shiftedcoords = []
        for i in range(0, len(self.coordsforshape)):
            shiftedcoords.append([self.coordsforshape[i][0] + shift_x, self.coordsforshape[i][1] + shift_y])
        self.coordsforshape = shiftedcoords

    def rotateshape(self, degreesclockwise):
        shape_w, shape_h = finddimensions(self.coordsforshape)
        rotatedcoords = []
        if degreesclockwise == 90:
            for i in range(0, len(self.coordsforshape)):
                rotatedcoords.append(
                    [self.coordsforshape[i][1] + self.y, (self.coordsforshape[i][0] * -1) + self.x + shape_w])

        elif degreesclockwise == 180:
            for i in range(0, len(self.coordsforshape)):
                rotatedcoords.append([(self.coordsforshape[i][0] * -1) + self.x + shape_w,
                                      (self.coordsforshape[i][1] * -1) + self.y + shape_h])

        elif degreesclockwise == 270:
            for i in range(0, len(self.coordsforshape)):
                rotatedcoords.append(
                    [(self.coordsforshape[i][1] * -1) + self.y + shape_h, self.coordsforshape[i][0] + self.x])
        self.coordsforshape = rotatedcoords

    def getlines(self):
        linesforshape = []
        for i in range(0, len(self.coordsforshape)):
            if i < len(self.coordsforshape) - 1:
                vector = [self.coordsforshape[i + 1][0] - self.coordsforshape[i][0], self.coordsforshape[i + 1][1] - self.coordsforshape[i][1]]
            else:
                vector = [self.coordsforshape[0][0] - self.coordsforshape[i][0], self.coordsforshape[0][1] - self.coordsforshape[i][1]]

            linesforshape.append([self.coordsforshape[i], vector])
        return linesforshape


# functions
def finddimensions(shape_coords):
    x_all = []
    y_all = []
    for j in shape_coords:
        x_all.append(j[0])
        y_all.append(j[1])
    return max(x_all), max(y_all)
