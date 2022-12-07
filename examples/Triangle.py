from objects import Triangle
from window import Window
from util import Dimension, Color, DisplayMode, Side, Position, Angle

window = Window("A triangle", DisplayMode.CENTER, Dimension(500, 500), Color.from_hex("#303030"), 60)
tri = Triangle(
    Side(Position(200, 200), Angle(degree=60), 100),
    Side(angle=Angle(degree=60), length=100),
    Color.from_hex("f57b42")
)
window.addObj(tri)


def main():
    return True


window.display(main)
