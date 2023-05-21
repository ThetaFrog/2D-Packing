from svgwrite import Drawing
from random import randint
from shape import Shape
import numpy as np


class Plane:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        pass

    def _group_bounds(self, shapedict: dict):
        (b_x, b_y), (h_x, h_y) = list(shapedict.values())[0].get_bounds()
        for key in shapedict:
            if shapedict[key].get_bounds()[0][0] < b_x:
                b_x = shapedict[key].get_bounds()[0][0]
            if shapedict[key].get_bounds()[0][1] < b_y:
                b_y = shapedict[key].get_bounds()[0][1]
            if shapedict[key].get_bounds()[1][0] > h_x:
                h_x = shapedict[key].get_bounds()[1][0]
            if shapedict[key].get_bounds()[1][1] > h_y:
                h_y = shapedict[key].get_bounds()[1][1]
        return (b_x, b_y), (h_x, h_y)

    def _group_area(self, shapedict: dict):
        (smallest_x, smallest_y), (largest_x, largest_y) = self._group_bounds(shapedict)
        return (largest_x - smallest_x) * (largest_y - smallest_y)

    def _group_efficiency(self, shapedict: dict) -> float:
        bounding_area: float = self._group_area(shapedict)
        util_area: float = list(shapedict.values())[0].get_area() * len(shapedict)
        return util_area / bounding_area

    def _drop(self, shape_dropped: Shape, existent_shapes: dict) -> Shape:
        obstructed = False
        while not obstructed:  # Bro's infinite
            shape_dropped.shift(0, -0.1)
            for key in existent_shapes:
                if shape_dropped.is_touching(existent_shapes[key]) < 0 or shape_dropped.get_bounds()[0][1] <= 0:
                    obstructed = True
                    break
        while obstructed:
            shape_dropped.shift(0, 0.01)
            for key in existent_shapes:
                if shape_dropped.is_touching(existent_shapes[key]) >= 0 and shape_dropped.get_bounds()[0][1] >= 0:
                    obstructed = False
                    break
        return shape_dropped

    def _choose_best_drop(self, shape_dropped: Shape, existent_shapes: dict) -> (dict, float):
        min_x, max_x = self._group_bounds(existent_shapes)[0][0] - shape_dropped.get_size()[0], self._group_bounds(existent_shapes)[1][0]
        possible_shapes: dict = {}
        for i in range(int(min_x * 10), int(max_x * 10) + 1):
            shape: Shape = Shape(shape_dropped.trianglesforshape)
            shape.shift(i/10, self._group_bounds(existent_shapes)[1][1])
            self._drop(shape, existent_shapes)
            possible_shapes.update({"possibility" + str(i): shape})
        best_case: [Shape, None] = None
        best_efficiency: float = 0
        for key in possible_shapes:
            merged_dict = {**{"possibility": possible_shapes[key]}, **existent_shapes}
            if self._group_bounds(possible_shapes)[1][1] > self.height:
                break
            if self._group_efficiency(merged_dict) > best_efficiency:
                best_efficiency = self._group_efficiency(merged_dict)
                best_case = possible_shapes[key]
        return best_case, best_efficiency

    def _choose_best_orientation(self, shape_dropped: Shape, existent_shapes: dict) -> Shape:
        best_case: [Shape, None] = None
        best_efficiency: float = 0
        for orientation in range(0, 360, 180):
            shape_dropped.rotate(orientation)
            option, efficiency = self._choose_best_drop(shape_dropped, existent_shapes)
            if efficiency > best_efficiency:
                best_case = option
                best_efficiency = efficiency
        print(best_efficiency)
        return best_case

    def _arrange_block(self, trianglesforshape) -> dict:
        shapedict: dict = {"shape1": Shape(trianglesforshape)}
        for i in range(2, 6):
            prospectiveshape: Shape = Shape(trianglesforshape)
            shapedict.update({"shape" + str(i): self._choose_best_orientation(prospectiveshape, shapedict)})
        print(shapedict)

        return shapedict

    def _tile_row(self):
        pass

    def _compact(self):
        pass

    def place_max_shapes(self):
        pass

    def find_min_area(self):
        pass

    def efficiency(self, timetaken, noofshapes, rectarea, shapearea):
        spaceutil = shapearea * noofshapes / rectarea
        efficientmetric = spaceutil * (1 / (1 + timetaken))
        return spaceutil, efficientmetric

    def draw(self, dict_of_shapes: dict, svg="output.svg"):
        cm = 35.43307
        dwg = Drawing(svg)
        dwg.add(dwg.rect((0, 0), (self.width * cm, self.height * cm),
                         style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"))
        dwg.save()
        for key in dict_of_shapes:
            shape = dwg.add(dwg.g(id=key, fill=f"rgb({randint(1, 25) * 10}, {randint(1, 25) * 10}, {randint(1, 25) * 10})"))
            for triangle in dict_of_shapes[key].trianglesforshape:
                shape.add(dwg.polygon(points=[(triangle[0, 0] * cm, (self.height - triangle[0, 1]) * cm),
                                              (triangle[1, 0] * cm, (self.height - triangle[1, 1]) * cm),
                                              (triangle[2, 0] * cm, (self.height - triangle[2, 1]) * cm)]))
                dwg.save()


if __name__ == "__main__":
    plane: Plane = Plane(10, 10)
    plane.draw(plane._arrange_block(np.array([[[0, 0],
                                                    [0, 2],
                                                    [2, 2]],
                                                   [[0, 0],
                                                    [2, 0],
                                                    [2, 2]],
                                              [[2, 1], [3, 3], [3, 1]],
                                              [[2,1],[2,3],[3,3]]], dtype=float)))

