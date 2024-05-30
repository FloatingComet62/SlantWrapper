from pygame import Surface, draw
from util import Color, DisplayMode, Vec


class Polygon:
    """ Pygame polygon """
    positions: list[Vec]
    """ Vertex Positions of the polygon """
    color: Color
    """ Color of the polygon """
    thickness: int
    """ Thickness of the polygon """

    def __init__(self, positions: list[Vec], color: Color, thickness: int = 0):
        self.positions = positions
        self.color = color
        self.thickness = thickness

    def display(self, screen: Surface, _: DisplayMode):
        vertexes = []
        for position in self.positions:
            vertexes.append(position.sep())

        draw.polygon(
            screen,
            self.color.toRGB(),
            vertexes,
            self.thickness
        )
