from pygame import Surface, draw
from objects.line import Line
from util import Position, Color


class AALine(Line):
    def __init__(self, position1: Position, position2: Position, color: Color, thickness: int = 1):
        super().__init__(position1, position2, color, thickness)

    def display(self, screen: Surface):
        draw.aaline(
            screen,
            self.color.toRGB(),
            (self.position1.x, self.position1.y),
            (self.position2.x, self.position2.y),
            self.thickness
        )
