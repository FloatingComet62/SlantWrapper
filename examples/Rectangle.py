from objects import Rectangle
from window import Window
from util import Dimension, Color, DisplayMode, Position

window = Window("A rectangle", DisplayMode.CENTER, Dimension(500, 500), Color.from_hex("#303030"), 60)
rect = Rectangle(Position(250, 250), Dimension(30, 50), Color.from_hex("f57b42"))
window.addObj(rect)


def main():
    return True


window.display(main)
