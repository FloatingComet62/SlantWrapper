from math import atan, sqrt, cos, sin
from pygame import Surface

from objects import Polygon, Circle
from util import Color, Position, Dimension, Angle, DisplayMode


def _sqr(x): return x * x


class Rectangle(Polygon):
    """ Rectangle """
    center: Position
    """ Position of the rectangle [TOP LEFT VERTEX IN DisplayMode.CORNER] """
    dimension: Dimension
    """ Dimensions of the rectangle """
    rotation: Angle
    """ Rotation of the rectangle """

    positions: list[Position]
    """ Position of each point """
    diagonal_angle: Angle
    diagonal_length: float

    vertex1: Position
    vertex2: Position
    vertex3: Position
    vertex4: Position

    def __init__(
            self,
            position: Position,
            dimension: Dimension,
            color: Color,
            rotation: Angle = Angle(degree=0)
    ):
        self.center = position
        self.dimension = dimension
        self.rotation = rotation
        self.positions = []
        self.draw()
        super().__init__(self.positions, color)

    def draw(self):
        self.diagonal_angle = Angle(
            radian=atan(self.dimension.height / self.dimension.width)
        )
        self.diagonal_length = sqrt(_sqr(self.dimension.height) + _sqr(self.dimension.width))

        def vertex_calculator(angle: Angle):
            return Position(
                (self.diagonal_length / 2) * cos(angle.radian),
                (self.diagonal_length / 2) * sin(angle.radian)
            )

        angle1 = self.rotation.offset_new(self.diagonal_angle.degree)
        angle2 = self.rotation.offset_new(180 - self.diagonal_angle.degree)
        angle3 = self.rotation.offset_new(180 + self.diagonal_angle.degree)
        angle4 = self.rotation.offset_new(-self.diagonal_angle.degree)

        self.vertex1 = self.center.offset_new(*vertex_calculator(angle1).to_tuple())
        self.vertex2 = self.center.offset_new(*vertex_calculator(angle2).to_tuple())
        self.vertex3 = self.center.offset_new(*vertex_calculator(angle3).to_tuple())
        self.vertex4 = self.center.offset_new(*vertex_calculator(angle4).to_tuple())

        self.positions = [self.vertex1, self.vertex2, self.vertex3, self.vertex4]

    def display(self, screen: Surface, display_mode: DisplayMode):
        if display_mode == DisplayMode.CORNER:
            self.vertex1.offset(self.dimension.width/2, self.dimension.height/2)
            self.vertex2.offset(self.dimension.width/2, self.dimension.height/2)
            self.vertex3.offset(self.dimension.width/2, self.dimension.height/2)
            self.vertex4.offset(self.dimension.width/2, self.dimension.height/2)

        super().display(screen, display_mode)
