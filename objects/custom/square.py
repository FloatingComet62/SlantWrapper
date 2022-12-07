from util import Position, Dimension, Color
from .. import Rectangle

class Square(Rectangle):
    def __init__(self, position: Position, length: float, color: Color):
        super().__init__(position, Dimension(length, length), color)