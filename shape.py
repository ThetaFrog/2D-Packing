# imports
import numpy as np
from plane import Plane
from shapely.geometry import Polygon


# classes
class Shape:
    def __init__(self, trianglesforshape: np.array([], dtype=float)):
        """
        initialises shape class
        :param trianglesforshape: 3D array containing the shapes constituent triangles,
        their constituent points (as pairs of coordinates)
        :return: Nothing
        """
        self.trianglesforshape: np.array([]) = np.copy(trianglesforshape)
        self.x, self.y = self.get_bounds()[0]

    def __str__(self) -> str:
        """
        returns coordinates when Shape object is printed

        :return: triangles that make up the shape
        """
        return str(self.trianglesforshape)

    def get_bounds(self) -> tuple[tuple[float, float], tuple[float, float]]:
        """
        Gets the bottom-left and top-right points of the shape's bounding rectangle

        :return: ((bottom_x, bottom_y), (top_x, top_y))
        """
        b_x: float = 0
        b_y: float = 0
        h_x: float = 0
        h_y: float = 0
        for triangle in self.trianglesforshape:
            for point in triangle:
                if point[0] < b_x:
                    b_x = point[0]
                elif point[0] > h_x:
                    h_x = point[0]
                if point[1] < b_y:
                    b_y = point[1]
                elif point[1] > h_y:
                    h_y = point[1]
        return (b_x, b_y), (h_x, h_y)

    def get_size(self) -> tuple[float, float]:
        """
        Gets size of the shape

        :return: Tuple of x size and y size
        """
        (b_x, b_y), (h_x, h_y) = self.get_bounds()
        return h_x - b_x, h_y - b_y

    def _get_area(self) -> float:
        """
        Finds the area of the shape based on the area of individual triangles
        :return: area
        """
        area = 0.0
        for triangle in self.trianglesforshape:
            xs = np.array([coord[0] for coord in triangle])
            ys = np.array([coord[1] for coord in triangle])
            area += 0.5 * (max(xs) - min(xs)) * (max(ys) - min(ys))
        return area

    def shift(self, dx, dy):
        """
        translates the shape
        :param dx: shift for x
        :param dy: shift for y
        :return: Nothing
        """
        self.x += dx
        self.y += dy
        for triangle in range(0, len(self.trianglesforshape)):
            for point in range(0, len(self.trianglesforshape[triangle])):
                self.trianglesforshape[triangle, point, 0] += dx
                self.trianglesforshape[triangle, point, 1] += dy

    def rotate(self, angle):
        """
        rotates the Shape by a given angle
        :param angle: angle to rotate anticlockwise by
        :return: Nothing
        """
        rad = angle * np.pi / 180
        old_x, old_y = self.x, self.y
        self.shift(-old_x, -old_y)
        for triangle in range(0, len(self.trianglesforshape)):
            for point in range(0, 3):
                x = self.trianglesforshape[triangle, point, 0]
                y = self.trianglesforshape[triangle, point, 1]
                x_prime = x * np.cos(rad) - y * np.sin(rad)
                y_prime = y * np.cos(rad) + x * np.sin(rad)
                self.trianglesforshape[triangle, point, 0] = np.round(x_prime, 4)
                self.trianglesforshape[triangle, point, 1] = np.round(y_prime, 4)
        b_x, b_y = self.get_bounds()[0]
        self.shift(old_x - b_x, old_y - b_y)

    def is_touching(self, anothershape) -> str:
        """
        Determine whether two shape objects are touching based on intersections between lines
        :param anothershape: the shape that may be intersecting with self
        :return: "touching," "overlapping" or "not touching"
        """
        touching = False
        for triangle in self.trianglesforshape:
            for triangle2 in anothershape.trianglesforshape:
                poly1s = Polygon(triangle)
                poly2s = Polygon(triangle2)
                if poly1s.touches(poly2s):
                    touching = True
                    continue
                if poly1s.intersects(poly2s):
                    return "overlapping"
        if touching:
            return "touching"
        else:
            return "not touching"


if __name__ == "__main__":
    shape1: Shape = Shape(np.array([[[0, 0],
                                     [1, 1],
                                     [1, 0]],
                                    [[1, 1],
                                     [2, 2],
                                     [1, 0]]], dtype=float))
    shape2: Shape = Shape(np.array([[[1, 0],
                                     [2, 1],
                                     [2, 0]],
                                    [[2, 1],
                                     [3, 2],
                                     [2, 0]]], dtype=float))
    shape1.shift(5,5)
    shape2.shift(4,5)
    shape1.rotate(0)
    shapedict: dict = {"shape1": shape1, "shape2": shape2}
    plane: Plane = Plane(10, 10)
    plane.draw(shapedict)
    # print(shapedict["shape1"].is_touching(shapedict["shape2"]))
    print(shape1)
    print("----------------")
    print(shape2)
