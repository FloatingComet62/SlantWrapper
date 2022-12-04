from pygame import Surface, draw, Rect
from objects import Base
from util import Color, Position, Dimension


class Rectangle(Base):
    dimension: Dimension

    def __init__(self, position: Position, dimension: Dimension, color: Color):
        super().__init__(position, color)

        self.dimension = dimension

    def display(self, screen: Surface):
        draw.rect(
            screen,
            self.color.toRGB(),
            Rect(
                self.position.x,
                self.position.y,
                self.dimension.width,
                self.dimension.height
            )
        )
