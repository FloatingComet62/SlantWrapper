from pygame import Surface, draw, Rect
from objects import Base
from util import Color, Position, Dimension, DisplayMode


class Ellipse(Base):
    dimension: Dimension
    thickness: int

    def __init__(self, position: Position, dimension: Dimension, color: Color, thickness: int = 0):
        super().__init__(position, color)

        self.dimension = dimension
        self.thickness = thickness

    def display(self, screen: Surface, display_mode: DisplayMode):
        draw.ellipse(
            screen,
            self.color.toRGB(),
            Rect(
                self.position.x - (self.dimension.width/2 if display_mode == DisplayMode.CENTER else 0),
                self.position.y - (self.dimension.height/2 if display_mode == DisplayMode.CENTER else 0),
                self.dimension.width,
                self.dimension.height
            ),
            self.thickness
        )
