# function
def checktouching(shape_1, shape_2):
    linesshape_1 = shape_1.getlines()
    linesshape_2 = shape_2.getlines()
    touching = False
    intersecting = False
    outerloopbreak = False
    if linesshape_1 == linesshape_2:
        return "overlapping"
    for i in linesshape_1:
        touchlist = []
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
                touchlist.append(True)
            elif (xinxrange and yinyrange) or (touchlist.count(True) >= 4):
                intersecting = True
                outerloopbreak = True
                break
            else:
                touchlist.append(False)
        if outerloopbreak:
            break
        wheretouching = [index for index, element in enumerate(touchlist) if element]
        wherenottouching = [index for index, element in enumerate(touchlist) if not element]
        try:
            if (max(wheretouching) - min(wheretouching) + 1 != len(wheretouching)): # and (max(wherenottouching) - min(wherenottouching) + 1 != len(wherenottouching)):
                intersecting = True
        except ValueError:
            pass
    for i in linesshape_2:
        if outerloopbreak:
            break
        touchlist = []
        for j in linesshape_1:
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
                touchlist.append(True)
            elif (xinxrange and yinyrange) or (touchlist.count(True) >= 4):
                intersecting = True
                outerloopbreak = True
                break
            wheretouching = [index for index, element in enumerate(touchlist) if element]
            try:
                if max(wheretouching) - min(wheretouching) + 1 != len(wheretouching):
                    intersecting = True
            except ValueError:
                pass
    if intersecting:
        return "overlapping"
    elif touching:
        return "touching"
    else:
        return "not touching"
