from pygame import Surface, draw
from objects import Base
from util import Position, Color


class Polygon:
    positions: [Position]
    color: Color
    thickness: int

    def __init__(self, positions: [Position], color: Color, thickness:int = 0):
        self.positions = positions
        self.color = color
        self.thickness = thickness

    def display(self, screen: Surface):
        vertexes = []
        for position in self.positions:
            vertexes.append(position.to_tuple())

        draw.polygon(
            screen,
            self.color.toRGB(),
            vertexes,
            self.thickness
        )


