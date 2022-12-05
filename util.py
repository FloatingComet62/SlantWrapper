from math import pi
from enum import Enum


class Color:
    red: int
    green: int
    blue: int

    def __init__(self, red=0, green=0, blue=0):
        self.red = red
        self.green = green
        self.blue = blue

    @staticmethod
    def from_hex(hex_string: str):
        tup = tuple(int(hex_string.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))
        return Color(tup[0], tup[1], tup[2])

    def toRGB(self):
        return self.red, self.green, self.blue

    def toBGR(self):
        return self.blue, self.green, self.red

    def to_hex(self):
        return "{:X}{:X}{:X}".format(self.red, self.green, self.blue)


class Angle:
    degree: float
    radian: float

    def __init__(self, **kwargs):
        deg = kwargs.get("degree")
        rad = kwargs.get("radian")
        if deg:  # <<<<<
            self.degree = deg
            self.radian = self.deg_to_radian(deg)
        elif rad:  # <<<<<
            self.radian = rad
            self.degree = self.radian_to_deg(rad)
        else:
            print("Please specify either \"degree\" or \"radian\"")
            exit(1)

    @staticmethod
    def deg_to_radian(deg):
        return (deg * pi) / 180

    @staticmethod
    def radian_to_deg(rad):
        return (rad * 180) / pi


class Position:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def to_tuple(self):
        return self.x, self.y

    @staticmethod
    def from_tuple(tup: tuple[float, float]):
        return Position(tup[0], tup[1])

    def offset(self, *offset):
        self.x += offset[0]
        self.y += offset[1]
        return self  # returning self to allow chaining


class Dimension:
    width: float
    height: float

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height


class DisplayMode(Enum):
    CORNER = False
    CENTER = True