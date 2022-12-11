from objects import Line
from window import Window, Scene
from util import Dimension, Color, DisplayMode, Position

scene = Scene("Main", Color.from_hex("#303030"))
window = Window("Window", DisplayMode.CENTER, Dimension(500, 500), 420)
window.add_scene(scene)
window.set_active_scene("Main")
line = Line(Position(10, 10), Position(490, 490), Color.from_hex("f57b42"))
scene.add_obj(line)


def main():
    return True


window.display(main)
