from objects import Rectangle
from window import Window
from util import Dimension, Color, DisplayMode, Position

window = Window("Window", DisplayMode.CENTER, Dimension(500, 500), Color.from_hex("#303030"), 420)
obj = Rectangle(Position(250, 250), Dimension(10, 50), Color.from_hex("f57b42"))
window.addObj(obj)


def main():
    obj.center = Position.from_tuple(window.mouse)
    obj.rotation.offset(1)
    return True


window.display(main)
