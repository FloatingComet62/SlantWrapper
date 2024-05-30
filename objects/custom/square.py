from util import Color, Vec
from .. import Rectangle


class Square(Rectangle):
    """ Square """
    def __init__(self, position: Vec, length: int, color: Color):
        super().__init__(position, Vec(length, length), color)
