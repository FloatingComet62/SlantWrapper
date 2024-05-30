from pygame import Surface, draw
from objects import Base
from util import Color, DisplayMode, Vec


class Circle(Base):
    """ Pygame Circle """
    radius: float
    """ Radius of the circle """
    thickness: int
    """ Thickness of the circle """

    def __init__(self, position: Vec, radius: float, color: Color, thickness: int = 0):
        super().__init__(position, color)

        self.radius = radius
        self.thickness = thickness

    def display(self, screen: Surface, display_mode: DisplayMode):
        draw.circle(
            screen,
            self.color.toRGB(),
            (
                self.position.x - (0 if display_mode == DisplayMode.CENTER else self.radius),
                self.position.y - (0 if display_mode == DisplayMode.CENTER else self.radius)
            ),
            self.radius,
            self.thickness
        )
