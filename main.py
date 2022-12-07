from objects.custom import Triangle, Square
from window import Window
from util import Dimension, Color, Angle, DisplayMode, Position, Side

window = Window("Window", DisplayMode.CENTER, Dimension(500, 500), Color.from_hex("#303030"), 60)
# obj = Rectangle(Position(250, 250), Dimension(50, 50), Color.from_hex("f57b42"))
tri = Triangle(
    Side(Position(250, 250), Angle(degree=60), 50),
    Side(angle=Angle(degree=50), length=60),
    Color.from_hex("#f57b42")
)
sqr = Square(Position(250, 250), 50, Color.from_hex("#32a852"))
window.addObjs([tri, sqr])

def main():
    sqr.position = Position.from_tuple(window.mouse)
    tri.side_1.angle.offset(-1)
    return True


window.display(main)
