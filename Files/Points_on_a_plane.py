import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        __x_distance = abs(self.__x-x)
        __y_distance = abs(self.__y-y)
        return math.hypot(__x_distance, __y_distance)
        # Write code here
        #

    def distance_from_point(self, point):
        return self.distance_from_xy(point.__x, point.__y)
