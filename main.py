from objects.custom import Triangle
from window import Window
from util import Dimension, Color, Angle, DisplayMode, Position, Side

window = Window("Window", DisplayMode.CENTER, Dimension(500, 500), Color.from_hex("#303030"), 60)
# obj = Rectangle(Position(250, 250), Dimension(50, 50), Color.from_hex("f57b42"))
obj = Triangle(
    Side(Position(250, 250), Angle(degree=60), 50),
    Side(angle=Angle(degree=50), length=60),
    Color.from_hex("#f57b42")
)
window.addObj(obj)

def main():
    obj.side_1.angle = Angle(degree=(obj.side_1.angle.degree - 1))
    obj.draw()
    return True


window.display(main)
