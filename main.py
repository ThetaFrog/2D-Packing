import placingalgorithm as pa
def max():
    maxshapes, rows = pa.arrangemaxshapes(10, 10, [[0, 0], [0, 2], [2, 2], [2, 3], [3, 3], [3, 1], [2, 1], [2, 0]], 6)
    print(maxshapes)
    print(rows)
    pa.svgarrangement(10, 10, rows)
def min():
    minheight, rows = pa.findminarea(10, 12, [[0, 0], [0, 2], [2, 2], [2, 3], [3, 3], [3, 1], [2, 1], [2, 0]], 6)
    print(minheight)
    print(rows)
    pa.svgarrangement(10, minheight, rows)

min()