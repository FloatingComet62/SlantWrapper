from objects import Polygon
from window import Window
from util import Dimension, Color, DisplayMode, Position

window = Window("A polygon", DisplayMode.CENTER, Dimension(500, 500), Color.from_hex("#303030"), 60)
poly = Polygon([
    Position(50, 100),
    Position(150, 200),
    Position(230, 430),
    Position(350, 50)
], Color.from_hex("f57b42"))
window.addObj(poly)


def main():
    return True


window.display(main)
