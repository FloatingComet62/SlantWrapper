from objects import Rectangle
from window import Window, Scene
from util import Color, DisplayMode, Vec

window = Window("Window", DisplayMode.CENTER, Vec(500, 500), 420)
scene = Scene("Main", Color.from_hex("#202020"))
window.add_scene(scene)
window.set_active_scene("Main")
obj = Rectangle(Vec(250, 250), Vec(50, 50), Color.from_hex("#eb4034"))
scene.add_obj(obj)


def main():
    obj.center = Vec(window.mouse)
    return True


window.display(main)
