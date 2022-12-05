from pygame import Surface, draw, Rect
from objects import Base
from util import Color, Position, Dimension, DisplayMode


class Rectangle(Base):
    dimension: Dimension

    def __init__(self, position: Position, dimension: Dimension, color: Color):
        super().__init__(position, color)

        self.dimension = dimension

    def display(self, screen: Surface, display_mode: DisplayMode):
        draw.rect(
            screen,
            self.color.toRGB(),
            Rect(
                self.position.x - (self.dimension.width/2 if display_mode == DisplayMode.CENTER else 0),
                self.position.y - (self.dimension.height/2 if display_mode == DisplayMode.CENTER else 0),
                self.dimension.width,
                self.dimension.height
            )
        )
