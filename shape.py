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
                vector = [shiftedcoords[i + 1][0] - shiftedcoords[i][0], shiftedcoords[i + 1][1] - shiftedcoords[i][1]]
            else:
                vector = [shiftedcoords[0][0] - shiftedcoords[i][0], shiftedcoords[0][1] - shiftedcoords[i][1]]

            linesforshape.append([shiftedcoords[i], vector])
        return linesforshape


# functions
def finddimensions(shape_coords):
    x_all = []
    y_all = []
    for j in shape_coords:
        x_all.append(j[0])
        y_all.append(j[1])
    return max(x_all), max(y_all)

