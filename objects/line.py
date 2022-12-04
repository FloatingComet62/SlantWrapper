from pygame import Surface, draw
from util import Color, Position, DisplayMode


class Line:
    position1: Position
    position2: Position
    color: Color
    thickness: int

    def __init__(self, position1: Position, position2: Position, color: Color, thickness: int = 1):
        self.position1 = position1
        self.position2 = position2
        self.color = color
        self.thickness = thickness

    def display(self, screen: Surface, _: DisplayMode):
        draw.line(
            screen,
            self.color.toRGB(),
            (self.position1.x, self.position1.y),
            (self.position2.x, self.position2.y),
            self.thickness
        )
