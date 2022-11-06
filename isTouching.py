# function
def checktouching(shape_1, shape_2):
    linesshape_1 = shape_1.getlines()
    linesshape_2 = shape_2.getlines()
    touching = False
    intersecting = False
    outerloopbreak = False
    for i in linesshape_1:
        for j in linesshape_2:
            if i[1][0] == 0 and j[1][0] == 0:  # both lines horizontal
                if (j[0][0] + j[1][0] >= i[0][0] >= j[0][0]) or (j[0][0] >= i[0][0] >= j[0][0] + j[1][0]) or (
                        i[0][0] + i[1][0] >= j[0][0] >= i[0][0]) or (i[0][0] >= j[0][0] >= i[0][0] + i[1][0]):
                    touching = True
                    continue
            elif i[1][1] == 0 and j[1][1] == 0:  # both lines vertical
                if (j[0][1] + j[1][1] >= i[0][1] >= j[0][1]) or (j[0][1] >= i[0][1] >= j[0][1] + j[1][1]) or (
                        i[0][1] + i[1][1] >= j[0][1] >= i[0][1]) or (i[0][1] >= j[0][1] >= i[0][1] + i[1][1]):
                    touching = True
                    continue
            elif (((j[0][0] + j[1][0] >= i[0][0] >= j[0][0]) or (j[0][0] >= i[0][0] >= j[0][0] + j[1][0])) and (
                    (i[0][1] + i[1][1] >= j[0][1] >= i[0][1]) or (i[0][1] >= j[0][1] >= i[0][1] + i[1][1]))) or (
                    ((i[0][0] + i[1][0] >= j[0][0] >= i[0][0]) or (i[0][0] >= j[0][0] >= i[0][0] + i[1][0])) and (
                    (j[0][1] + j[1][1] >= i[0][1] >= j[0][1]) or (j[0][1] >= i[0][1] >= j[0][1] + j[1][1]))):
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
