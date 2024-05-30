from objects import Rectangle
from window import Window, Scene
from util import Color, DisplayMode, Vec

scene = Scene("Main", Color.from_hex("#303030"))
window = Window("Rotating Rectangle", DisplayMode.CENTER, Vec(500, 500), 420)
window.add_scene(scene)
window.set_active_scene("Main")
rect = Rectangle(Vec(250, 250), Vec(30, 50), Color.from_hex("f57b42"))
scene.add_obj(rect)


def main():
    rect.rotation.offset(1)
    return True


window.display(main)
