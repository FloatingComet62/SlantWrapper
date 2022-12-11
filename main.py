from objects import Rectangle
from window import Window, Scene
from util import Dimension, Color, DisplayMode, Position

scene = Scene("Main", Color.from_hex("#303030"))
window = Window("Window", DisplayMode.CENTER, Dimension(500, 500), 420)
window.add_scene(scene)
window.set_active_scene("Main")
obj = Rectangle(Position(250, 250), Dimension(10, 50), Color.from_hex("f57b42"))
scene.add_obj(obj)


def main():
    obj.center = Position.from_tuple(window.mouse)
    obj.rotation.offset(1)
    return True


window.display(main)
