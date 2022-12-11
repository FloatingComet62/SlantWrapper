from objects import Rectangle
from window import Window, Scene
from util import Dimension, Color, DisplayMode, Position

scene = Scene("Main", Color.from_hex("#303030"))
window = Window("Rotating Rectangle", DisplayMode.CENTER, Dimension(500, 500), 420)
window.add_scene(scene)
window.set_active_scene("Main")
rect = Rectangle(Position(250, 250), Dimension(30, 50), Color.from_hex("f57b42"))
scene.add_obj(rect)


def main():
    rect.rotation.offset(1)
    return True


window.display(main)
