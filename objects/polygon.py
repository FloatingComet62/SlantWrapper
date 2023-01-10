from pygame import Surface, draw
from util import Position, Color, DisplayMode


class Polygon:
    """ Pygame polygon """
    positions: [Position]
    """ Vertex Positions of the polygon """
    color: Color
    """ Color of the polygon """
    thickness: int
    """ Thickness of the polygon """

    def __init__(self, positions: [Position], color: Color, thickness: int = 0):
        self.positions = positions
        self.color = color
        self.thickness = thickness

    def display(self, screen: Surface, _: DisplayMode):
        vertexes = []
        for position in self.positions:
            vertexes.append(position.to_tuple())

        draw.polygon(
            screen,
            self.color.toRGB(),
            vertexes,
            self.thickness
        )
