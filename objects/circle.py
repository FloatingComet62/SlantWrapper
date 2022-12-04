from pygame import Surface, draw
from objects import Base
from util import Color, Position


class Circle(Base):
    radius: float
    thickness: int

    def __init__(self, position: Position, radius: float, color: Color, thickness: int = 0):
        super().__init__(position, color)

        self.radius = radius
        self.thickness = thickness

    def display(self, screen: Surface):
        draw.circle(
            screen,
            self.color.toRGB(),
            (self.position.x, self.position.y),
            self.radius,
            self.thickness
        )
