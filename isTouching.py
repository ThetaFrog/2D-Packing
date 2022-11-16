# function
def checktouching(shape_1, shape_2):
    linesshape_1 = shape_1.getlines()
    linesshape_2 = shape_2.getlines()
    touching = False
    intersecting = False
    outerloopbreak = False

    for i in linesshape_1:
        touchcount = 0
        for j in linesshape_2:
            xequalsx = False
            yequalsy = False
            xinxrange = False
            yinyrange = False
            if (i[0][0] == j[0][0] or i[0][0] + i[1][0] == j[0][0]) or (i[0][0] == j[0][0] + j[1][0] or i[0][0] + i[1][0] == j[0][0] + j[1][0]):
                xequalsx = True
            elif (j[0][0] > i[0][0] > j[0][0] + j[1][0] or j[0][0] < i[0][0] < j[0][0] + j[1][0]) or (i[0][0] > j[0][0] > i[0][0] + i[1][0] or i[0][0] < j[0][0] < i[0][0] + i[1][0]):
                xinxrange = True
            if (i[0][1] == j[0][1] or i[0][1] + i[1][1] == j[0][1]) or (i[0][1] == j[0][1] + j[1][1] or i[0][1] + i[1][1] == j[0][1] + j[1][1]):
                yequalsy = True
            elif (j[0][1] > i[0][1] > j[0][1] + j[1][1] or j[0][1] < i[0][1] < j[0][1] + j[1][1]) or (i[0][1] > j[0][1] > i[0][1] + i[1][1] or i[0][1] < j[0][1] < i[0][1] + i[1][1]):
                yinyrange = True
            if (xequalsx and yequalsy) or (xequalsx and yinyrange) or (xinxrange and yequalsy):
                touching = True
                touchcount += 1
            elif (xinxrange and yinyrange) or touchcount >= 4:
                intersecting = True
                outerloopbreak = True
                break
        if outerloopbreak:
            break

    if intersecting:
        return "intersecting"
    elif touching:
        return "touching"
    else:
        return "free"
