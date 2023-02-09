from util import Position, Dimension, Color
from .. import Rectangle


class Square(Rectangle):
    """ Square """
    def __init__(self, position: Position, length: int, color: Color):
        super().__init__(position, Dimension(length, length), color)
