from objects.rectangle import Rectangle
from window import Window
from util import Dimension, Color, Position, DisplayMode

window = Window("Window", DisplayMode.CENTER, Dimension(500, 500), Color.from_hex("#303030"), 60)
obj = Rectangle(Position(250, 250), Dimension(50, 50), Color.from_hex("f57b42"))
window.addObj(obj)

def main():
    obj.position = Position.from_tuple(window.mouse)
    return True


window.display(main)
