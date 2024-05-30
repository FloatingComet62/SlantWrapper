from pygame import Surface, draw
from .line import Line
from util import Color, DisplayMode, Vec


class AALine(Line):
    """ Pygame AALine """
    def __init__(self, position1: Vec, position2: Vec, color: Color, thickness: int = 1):
        super().__init__(position1, position2, color, thickness)

    def display(self, screen: Surface, _: DisplayMode):
        draw.aaline(
            screen,
            self.color.toRGB(),
            (self.position1.x, self.position1.y),
            (self.position2.x, self.position2.y),
            self.thickness
        )
