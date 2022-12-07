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
        self.shiftshape(-self.x, -self.y)
        shape_w, shape_h = finddimensions(self.coordsforshape)
        rotatedcoords = []
        if degreesclockwise == 90:
            for i in range(0, len(self.coordsforshape)):
                rotatedcoords.append(
                    [self.coordsforshape[i][1], (self.coordsforshape[i][0] * -1) + shape_w])

        elif degreesclockwise == 180:
            for i in range(0, len(self.coordsforshape)):
                rotatedcoords.append([(self.coordsforshape[i][0] * -1) + shape_w,
                                      (self.coordsforshape[i][1] * -1) + shape_h])

        elif degreesclockwise == 270:
            for i in range(0, len(self.coordsforshape)):
                rotatedcoords.append(
                    [(self.coordsforshape[i][1] * -1) + shape_h, self.coordsforshape[i][0]])
        self.coordsforshape = rotatedcoords
        self.shiftshape(self.x, self.y)

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
def coordsinfo(shape_coords, x_list=False, y_list=False):
    x_all = []
    y_all = []
    for j in shape_coords:
        x_all.append(j[0])
        y_all.append(j[1])
    if x_list and y_list:
        return x_all, y_all
    elif x_list:
        return x_all
    elif y_list:
        return y_all
    else:
        return []


def finddimensions(shape_coords):
    x_all, y_all = coordsinfo(shape_coords, x_list=True, y_list=True)
    return max(x_all) - min(x_all), max(y_all) - min(y_all)

"""
def findarea(listofshapes):
    totalarea = 0
    i = listofshapes[0]
    coords = i.coordsforshape
    x_all, y_all = coordsinfo(coords, x_list=True, y_list=True)
    xprev = min(x_all)
    areamap = []
    area = 0
    while len(x_all) != 0:      # For each distinct x value
        x = min(x_all)
        ycoords = []
        for j in i.coordsforshape:
            if j[0] == x:
                ycoords.append(j[1])
        ycoords.sort()
        ylines = []
        for c in range(0, len(ycoords), 2):             # Formatting ylines so that it can be put in areamap
            ylines.append([ycoords[c], ycoords[c + 1]])
        ylines.append(x - xprev)
        areamap.append(ylines)
        xprev = x
        while x in x_all:               # Deleting x vals equal to the one already considered
            x_all.remove(x)
    # With parsed coordinates, find area
    for xval in range(1, len(areamap)):
        for yval in range(0, len(areamap[xval]) - 1):
            multiplier = areamap[xval][-1]
            closeb, closeh = areamap[xval][yval][0], areamap[xval][yval][1]

            for vx in range(xval - 1, -1, -1):
                for vy in range(0, len(areamap[vx]) - 1):
                    if areamap[vx][vy]:
                        openb, openh = areamap[vx][vy][0], areamap[vx][vy][1]
                    else:
                        continue
                    if openb == closeb and closeh == openh:
                        area += multiplier * (closeh - closeb)
                        areamap[vx][vy] = []
                        areamap[xval][yval] = []
                    elif openb < closeb < closeh < openh:
                        area += multiplier * (closeh - closeb)
                        areamap[vx][vy] = [openb, closeb]
                        areamap[vx].insert(vy + 1, [closeh, openh])
                        areamap[xval][yval] = []
                    elif closeb < openb < openh < closeh:
                        area += multiplier * (openh - openb)
                        areamap[xval][yval] = [openh, closeh]
                        areamap[xval].insert(yval + 1, [openb, closeb])
                        areamap[vx][vy] = []
                    elif openb < closeb < openh:
                        area += multiplier * (openh - closeb)
                        oldopenh = openh
                        openh = closeb
                        closeb = oldopenh
                    elif openb < closeh < openh:
                        area += multiplier * (closeh - openb)
                        oldopenb = openb
                        openb = closeh
                        closeh = oldopenb
                    elif closeb < openh < closeh:
                        area += multiplier * (openh - closeb)
                        oldopenh = openh
                        openh = closeb
                        closeb = oldopenh
                    elif closeb < openb < closeh:
                        area += multiplier * (closeh - openb)
                        oldopenb = openb
                        openb = closeh
                        closeh = oldopenb
                    if openb == openh:
                        areamap[vx][vy] = []
                    # else:
                        # areamap[vx][vy][0] = openb
                        # areamap[vx][vy][1] = openh
                    if closeh == closeb:
                        areamap[xval][yval] = []
                    else:
                        areamap[xval][yval][0] = closeb
                        areamap[xval][yval][1] = closeh
                multiplier += areamap[vx][-1]

    totalarea += area * len(listofshapes)
    return totalarea
"""
