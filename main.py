import objects.rectangle
from window import Window
from util import Dimension, Color, Position

window = Window("Test", Dimension(700, 500), Color.from_hex("#303030"))
obj = objects.rectangle.Rectangle(Position(500, 350), Dimension(50, 50), Color.from_hex("3254a8"))
window.addObj(obj)


def main():
    obj.position = Position.from_tuple(window.mouse).offset(-obj.dimension.width/2, -obj.dimension.height/2)


window.display(main)
