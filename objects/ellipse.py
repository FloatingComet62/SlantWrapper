from pygame import Surface, draw, Rect
from objects import Base
from util import Color, Position, Dimension


class Ellipse(Base):
    dimension: Dimension
    thickness: int

    def __init__(self, position: Position, dimension: Dimension, color: Color, thickness: int = 1):
        super().__init__(position, color)

        self.dimension = dimension
        self.thickness = thickness

    def display(self, screen: Surface):
        draw.ellipse(
            screen,
            self.color.toRGB(),
            Rect(
                self.position.x,
                self.position.y,
                self.dimension.width,
                self.dimension.height
            ),
            self.thickness
        )
