import placingalgorithm as pa
from time import perf_counter

shape1 = [[0, 0], [0, 2], [2, 2], [2, 3], [3, 3], [3, 1], [2, 1], [2, 0]]
area1 = 6
shape2 = [[0, 0], [0, 2], [1, 2], [1, 1], [2, 1], [2, 0]]
area2 = 3
def maxarrange():
    maxshapes, rows = pa.arrangemaxshapes(10, 10, shape2, area2)
    print("shapes tiled = " + str(maxshapes))
    pa.svgarrangement(10, 10, rows)
    return maxshapes
def minarrange():
    minheight, rows = pa.findminarea(10, 180, shape1, area1)
    print("minimum height for 180 shapes = " + str(minheight))
    pa.svgarrangement(10, minheight, rows)
    return minheight

# """
t_start = perf_counter()
m = maxarrange()
t_finish = perf_counter()
print("space utilisation = " + str(pa.efficiency(t_finish - t_start, m, 10*10, area2)[0]))
print("efficiency = " + str(pa.efficiency(t_finish - t_start, m, 10*10, area2)[1]))
# """
# """
t_start = perf_counter()
m = minarrange()
t_finish = perf_counter()
print("space utilisation = " + str(pa.efficiency(t_finish - t_start, 180, 10*m, area1)[0]))
print("efficiency = " + str(pa.efficiency(t_finish - t_start, 180, 10*m, area1)[1]))
# """