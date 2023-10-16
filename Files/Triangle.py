import math
from Points_on_a_plane import Point


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        __side1 = self.__vertices[0].distance_from_point(self.__vertices[1])
        __side2 = self.__vertices[1].distance_from_point(self.__vertices[2])
        __side3 = self.__vertices[2].distance_from_point(self.__vertices[0])
        return __side1 + __side2 + __side3


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
