from math import sin, cos
from util import Side, Color, Angle, Vec
from .. import Polygon


class Triangle(Polygon):
    """ Triangle """
    side_1: Side
    """ Side 1 of the triangle """
    side_2: Side
    """ Side 2 of the triangle """
    side_3: Side

    color: Color
    """ Color of the triangle """

    def __init__(self, side_1: Side, side_2: Side, color: Color):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = Side()
        self.color = color
        super().__init__([], color)
        self.draw()

    def draw(self):
        self.side_2.position = Vec(
            self.side_1.length * cos(self.side_1.angle.radian),
            self.side_1.length * sin(self.side_1.angle.radian)
        ).offset(*self.side_1.position.sep())

        absolute_a2 = Angle(degree=(self.side_2.angle.degree - 180 + self.side_1.angle.degree))

        self.side_3.position = Vec(
            self.side_2.length * cos(absolute_a2.radian),
            self.side_2.length * sin(absolute_a2.radian)
        ).offset(*self.side_2.position.sep())

        self.positions = [self.side_1.position, self.side_2.position, self.side_3.position]
