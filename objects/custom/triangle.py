from math import sin, cos
from util import Side, Color, Position, Angle
from ..polygon import Polygon

class Triangle(Polygon):
    side_1: Side
    side_2: Side
    side_3: Side

    def __init__(self, side_1: Side, side_2: Side, color: Color):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = Side()
        super().__init__([], color)
        self.draw()


    def draw(self):
        self.side_2.position = Position.from_tuple((
            self.side_1.length * cos(self.side_1.angle.radian),
            self.side_1.length * sin(self.side_1.angle.radian)
        )).offset(*self.side_1.position.to_tuple())

        absolute_a2 = Angle(degree=(self.side_2.angle.degree - 180 + self.side_1.angle.degree))

        self.side_3.position = Position.from_tuple((
            self.side_2.length * cos(absolute_a2.radian),
            self.side_2.length * sin(absolute_a2.radian)
        )).offset(*self.side_2.position.to_tuple())

        self.positions = [self.side_1.position, self.side_2.position, self.side_3.position]