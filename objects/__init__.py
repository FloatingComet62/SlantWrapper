from util import Color, Position


class Base:
    position: Position
    color: Color

    def __init__(self, position: Position, color: Color):
        self.position = position
        self.color = color
