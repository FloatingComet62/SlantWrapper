from util import Color, Position

class Base:
    position: Position
    color: Color

    def __init__(self, position: Position, color: Color):
        self.position = position
        self.color = color


from .aaline import AALine
from .arc import Arc
from .circle import Circle
from .ellipse import Ellipse
from .line import Line
from .polygon import Polygon
from .rectangle import Rectangle
from .text import Text
from .image import Image
from .sound import Sound
from .background_sound import BackgroundSound
