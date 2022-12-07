from objects import Line
from window import Window
from util import Dimension, Color, DisplayMode, Position

window = Window("A line", DisplayMode.CENTER, Dimension(500, 500), Color.from_hex("#303030"), 60)
line = Line(Position(10, 10), Position(490, 490), Color.from_hex("f57b42"))
window.addObj(line)


def main():
    return True


window.display(main)
