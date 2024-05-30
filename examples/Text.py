from objects import Text
from window import Window, Scene
from util import Color, DisplayMode, Vec

scene = Scene("Main", Color.from_hex("#303030"))
window = Window("Text", DisplayMode.CENTER, Vec(500, 500), 420)
window.add_scene(scene)
window.set_active_scene("Main")
msg = Text("Hello World!", Vec(250, 250), 50, Color.from_hex("#ffffff"))
scene.add_obj(msg)


def main():
    return True


window.display(main)
