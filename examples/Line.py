from objects import Line
from window import Window, Scene
from util import Vec, Color, DisplayMode

scene = Scene("Main", Color.from_hex("#303030"))
window = Window("Window", DisplayMode.CENTER, Vec(500, 500), 420)
window.add_scene(scene)
window.set_active_scene("Main")
line = Line(Vec(10, 10), Vec(490, 490), Color.from_hex("f57b42"))
scene.add_obj(line)


def main():
    return True


window.display(main)
