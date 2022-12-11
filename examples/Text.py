from objects import Text
from window import Window, Scene
from util import Dimension, Color, DisplayMode, Position

scene = Scene("Main", Color.from_hex("#303030"))
window = Window("Text", DisplayMode.CENTER, Dimension(500, 500), 420)
window.add_scene(scene)
window.set_active_scene("Main")
msg = Text("Hello World!", Position(250, 250), 50, Color.from_hex("#ffffff"))
scene.add_obj(msg)


def main():
    return True


window.display(main)
