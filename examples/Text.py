from objects import Text
from window import Window
from util import Dimension, Color, DisplayMode, Position

window = Window("Text", DisplayMode.CENTER, Dimension(500, 500), Color.from_hex("#303030"), 60)
msg = Text("Hello World!", Position(250, 250), 50, Color.from_hex("#ffffff"))
window.addObj(msg)


def main():
    return True


window.display(main)
