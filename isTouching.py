# import statements


# classes
class Shape:
    def __init__(self, x, y, coordsforshape):        # coords forshape formatted as [[x,y],[x,y]]
        self.x = x
        self.y = y
        self.coordsforshape = coordsforshape
    def getlines(self):
        linesforshape = []
        for i in range (0, self.coordsforshape.len()):
            if i < self.coordsforshape.len():
                linesforshape.append("[" + self.coordsforshape[i] + "," + self.coordsforshape[i + 1] + "]")
            else:
                linesforshape.append("[" + self.coordsforshape[i] + "," + self.coordsforshape[0] + "]")
        return linesforshape



