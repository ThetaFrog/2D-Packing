# Import Statements
import isTouching
import shape
import random
import svgcommands as sc


# Functions
def groupshapes(maxareawidth, maxareaheight, coords, area):
    shapedict = {}
    shape_w, shape_h = shape.finddimensions(coords)
    shapedict.update({"s0,1": shape.Shape(shape_w, shape_w, coords)})                         # note: coordinates are relative
    rect_w, rect_h = shape_w * 3, shape_h * 3
    efficiency = area / (shape_w * shape_h)
    highestefficiency = efficiency
    mostefficient = shapedict["s0,1"]
    timestested = 0
    while True:
        name = "s0,2"
        option = shape.Shape(random.randint(0, rect_w - shape_w), random.randint(0, rect_h - shape_h), coords)      # Possible shape
        option.rotateshape(random.randint(1, 3) * 90)                                                               # Randomise rotation
        allcoords = shapedict["s0,1"].coordsforshape
        add = True
        free = 0
        for key in shapedict:                                       # iterating through shapes that have already been placed
            if isTouching.checktouching(shapedict[key], option) == "not touching":      # checking if the randonly placed shape is overlapping with any
                free += 1
            if isTouching.checktouching(shapedict[key], option) == "overlapping" or free == len(shapedict):
                add = False
                break
        if not add:
            continue
        timestested += 1
        possiblecoords = [*allcoords, *option.coordsforshape]                           # possible coordinates are for the shape decided above and preexisting shapes
        boundingrect_w, boundingrect_h = shape.finddimensions(possiblecoords)           # Total rectangular area
        efficiency = (area * 2) / (boundingrect_w * boundingrect_h)
        if boundingrect_w > maxareawidth or boundingrect_h > maxareaheight:
            break
        if efficiency == 1:
            shapedict.update({name: option})
            break
        if efficiency > highestefficiency and (boundingrect_w * boundingrect_h) > ((shape_w * shape_h) + area):
            highestefficiency = efficiency
            mostefficient = option
        else:
            continue
        if timestested > 50:           # fix this, need to select highest efficiency shape rather than current
            shapedict.update({name: mostefficient})
            break
        shapedict.update({name: mostefficient})
        break
    finalcoords = [*allcoords, *mostefficient.coordsforshape]
    xlist, ylist = shape.coordsinfo(finalcoords, True, True)
    print(min(xlist), min(ylist))
    for key in shapedict:
        pass
        shapedict[key].shiftshape(-min(xlist), -min(ylist))

    return shapedict


def tilerow(areawidth, rownum, groupofshapes, left=True):
    shape_w, shape_h = shape.finddimensions([*groupofshapes["s0,1"].coordsforshape, *groupofshapes["s0,2"].coordsforshape])
    startheight = rownum * shape_h
    possiblegroups = int(areawidth/shape_w)
    row = {}
    if left:
        for group in range(1, possiblegroups + 1):
            name1 = "s" + str(group + (possiblegroups * rownum)) + ",1"
            name2 = "s" + str(group + (possiblegroups * rownum)) + ",2"
            shape1 = shape.Shape((group - 1) * shape_w, startheight, groupofshapes["s0,1"].coordsforshape)
            shape2 = shape.Shape((group - 1) * shape_w, startheight, groupofshapes["s0,2"].coordsforshape)
            row.update({name1: shape1})
            row.update({name2: shape2})
    else:
        for group in range(possiblegroups, 0, -1):
            name1 = "s" + str(group + (possiblegroups * rownum)) + ",1"
            name2 = "s" + str(group + (possiblegroups * rownum)) + ",2"
            shape1 = shape.Shape(areawidth - (group * shape_w), startheight, groupofshapes["s0,1"].coordsforshape)
            shape2 = shape.Shape(areawidth - (group * shape_w), startheight, groupofshapes["s0,2"].coordsforshape)
            row.update({name1: shape1})
            row.update({name2: shape2})
    return row


def movegroup(shiftx, shifty, groupdict):
    for key in groupdict:
        groupdict[key].shiftshape(shiftx, shifty)


def checktouch(allshapes, group, noofshapesinrow, rowleft=False, grouponleft=False, grouponright=False):
    if group <= noofshapesinrow:
        return False
    if rowleft:
        if grouponleft:
            groupschecked = [group + 1, group - noofshapesinrow]
        elif grouponright:
            groupschecked = [group - 1, group - noofshapesinrow, group - noofshapesinrow - 1]
        else:
            groupschecked = [group + 1, group - 1, group - noofshapesinrow, group - noofshapesinrow - 1]
    else:
        if grouponleft:
            groupschecked = [group + 1, group - noofshapesinrow, group - noofshapesinrow + 1]
        elif grouponright:
            groupschecked = [group - 1, group - noofshapesinrow]
        else:
            groupschecked = [group + 1, group - 1, group - noofshapesinrow, group - noofshapesinrow - 1]
    name1 = "s" + str(group) + ",1"
    name2 = "s" + str(group) + ",2"
    for g in groupschecked:
        touchn1 = "s" + str(g) + ",1"
        touchn2 = "s" + str(g) + ",2"
        interaction1 = isTouching.checktouching(allshapes[name1], allshapes[touchn1])
        interaction2 = isTouching.checktouching(allshapes[name1], allshapes[touchn2])
        interaction3 = isTouching.checktouching(allshapes[name2], allshapes[touchn1])
        interaction4 = isTouching.checktouching(allshapes[name2], allshapes[touchn2])
        if interaction1 == "overlapping" or interaction2 == "overlapping" or interaction3 == "overlapping" or interaction4 == "overlapping":
            return True
    return False


def downtouch(currentrow, allshapes, rowleft=False):
    noinrow = int(len(currentrow)/2)
    moving = list(currentrow.keys())
    while moving:
        if len(moving) - 1 == 0:
            break
        i = 0
        key = moving[i]
        group = int(key[1:key.index(",")])
        grouponright = False
        grouponleft = False
        if min(shape.coordsinfo([*allshapes["s" + str(group) + ",1"].coordsforshape,
                                 *allshapes["s" + str(group) + ",2"].coordsforshape], y_list=True)) <= 0:
            break
        movegroup(0, - 1, currentrow)
        if group % noinrow == 1:
            grouponleft = True
        if group % noinrow == 0:
            grouponright = True
        elif i == len(moving) - 1:
            i = 0
            moving.pop(-1)
        else:
            i += 1
            moving.pop(i - 1)
        if checktouch(allshapes, group, noinrow, rowleft=rowleft, grouponleft=grouponleft, grouponright=grouponright):
            movegroup(0, 1, currentrow)
            moving.pop(i - 1)


"""
def lefttouch(currentrow, allshapes, rowleft=False):
    noinrow = int(len(currentrow) / 2)
    moving = list(currentrow.keys())
    while moving:
        if len(moving) - 1 == 0:
            break
        i = 0
        key = moving[i]
        group = int(key[1:key.index(",")])
        grouponright = False
        grouponleft = False
        if min(shape.coordsinfo([*allshapes["s" + str(group) + ",1"].coordsforshape,
                                 *allshapes["s" + str(group) + ",2"].coordsforshape], x_list=True)) <= 0:
            break
        movegroup(-1, 0, currentrow)
        if group % noinrow == 1:
            grouponleft = True
        if group % noinrow == 0:
            grouponright = True
        elif i == len(moving) - 1:
            i = 0
            moving.pop(-1)
        else:
            i += 1
            moving.pop(i - 1)
        ctouch = checktouch(allshapes, group, noinrow, rowleft=rowleft, grouponleft=grouponleft, grouponright=grouponright)
        if ctouch:
            movegroup(1, 0, currentrow)
            moving.pop(i - 1)
"""


def arrangemaxshapes(areawidth, areaheight, shapecoords, shapearea):        # returns the maximum amount of shapes in a given area
    shapes = groupshapes(areawidth, areaheight, shapecoords, shapearea)
    packed = False
    rownumber = 0
    rows = {}
    lines = 0
    while not packed:
        if rownumber % 2 == 0:
            left = True
        else:
            left = False
        newrow = tilerow(areawidth, rownumber, shapes, left=left)
        rows.update(newrow)
        downtouch(newrow, rows, rowleft=left)
        # lefttouch(newrow, rows, rowleft=left)
        heightcoords = []
        lines = [item for item in rows]
        for line in lines:
            heightcoords.extend(rows[line].coordsforshape)
        height = shape.finddimensions(heightcoords)[1]
        if height + shape.finddimensions(shapecoords)[1] > areaheight:
            packed = True
        rownumber += 1
    noofshapes = len(lines)
    return noofshapes, rows


def findminarea(areawidth, noofshapes, shapecoords, shapearea):             # returns the minimum area a given amount of shapes can occupy
    shapes = groupshapes(areawidth, shapearea*1000, shapecoords, shapearea)
    packed = False
    rownumber = 0
    rows = {}
    while not packed:
        if rownumber % 2 == 0:
            left = True
        else:
            left = False
        newrow = tilerow(areawidth, rownumber, shapes, left=left)
        rows.update(newrow)
        downtouch(newrow, rows, rowleft=left)
        # lefttouch(newrow, rows, rowleft=left)
        items = [item for item in rows]
        if len(items) >= noofshapes:
            packed = True
        # add code to remove excess shapes
        heightcoords = [item.coordsforshape for item in items]
        height = shape.finddimensions(heightcoords)[1]
        return height, rows


def svgarrangement(areawidth, areaheight, rows):
    lines = []
    for key in rows:
        lines.append(rows[key].getlines())
    sc.svgout(areawidth, areaheight, lines)


def efficiency(timetaken, noofshapes, rectarea, shapearea):
    spaceutil = shapearea * noofshapes / rectarea
    efficientmetric = spaceutil * (1/(timetaken ** 0.5))
    return spaceutil, efficientmetric

