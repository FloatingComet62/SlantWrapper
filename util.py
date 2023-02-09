from math import radians, degrees
from dataclasses import dataclass
from enum import Enum


class Color:
    """ Color class """
    red: int
    """ the amount of red in the color """
    green: int
    """ the amount of green in the color """
    blue: int
    """ the amount of blue in the color """

    def __init__(self, red=0, green=0, blue=0):
        self.red = red
        self.green = green
        self.blue = blue

    @staticmethod
    def from_hex(hex_string: str):
        """ Make a color from hex values """
        tup = tuple(int(hex_string.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))
        return Color(tup[0], tup[1], tup[2])

    def toRGB(self) -> tuple[int, int, int]:
        """ Turns RGB value """
        return self.red, self.green, self.blue

    def toBGR(self) -> tuple[int, int, int]:
        """ Turns BGR value """
        return self.blue, self.green, self.red

    def to_hex(self):
        return "{:X}{:X}{:X}".format(self.red, self.green, self.blue)


class Angle:
    """ Angle class """
    degree: float
    """ Angle in degrees unit """
    radian: float
    """ Angle in radian unit """

    def __init__(self, **kwargs):
        deg = kwargs.get("degree")
        rad = kwargs.get("radian")
        if deg is not None:  # <<<<<
            self.degree = deg
            self.radian = radians(deg)
        elif rad is not None:  # <<<<<
            self.radian = rad
            self.degree = degrees(rad)
        else:
            raise ValueError("Please specify either \"degree\" or \"radian\"")

    def offset(self, degree: float):
        """ Offsets the value of angle """
        self.degree += degree
        self.radian = radians(self.degree)
        return self

    def offset_new(self, degree: float):
        """ Returns a new angle object with the offset """
        return Angle(degree=(self.degree + degree))


class Position:
    """ Position class """
    x: float
    """ X coordinate """
    y: float
    """ Y coordinate """

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def to_tuple(self):
        """ Convert to (x, y) """
        return self.x, self.y

    def offset(self, *offset):
        """ Offsets the position """
        self.x += offset[0]
        self.y += offset[1]
        return self  # returning self to allow chaining

    def offset_new(self, *offset):
        """ Returns a new position object with the offset """
        return Position(self.x + offset[0], self.y + offset[1])


@dataclass
class Dimension:
    width: int
    height: int


class DisplayMode(Enum):
    CORNER = False
    """ Render objects from the corner """
    CENTER = True
    """ Render objects from the center """


class Side:
    """ A side of a custom polygon """
    position: Position
    """ Position of the side (base point) """
    length: float
    """ Length of the side """
    angle: Angle
    """ Rotation of the side """

    def __init__(self, position: Position = Position(0, 0), angle: Angle = Angle(degree=0), length: float = 0):
        self.position = position
        self.angle = angle
        self.length = length
