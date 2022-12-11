from objects import Polygon
from window import Window, Scene
from util import Dimension, Color, DisplayMode, Position

scene = Scene("Main", Color.from_hex("#303030"))
window = Window("Polygon", DisplayMode.CENTER, Dimension(500, 500), 420)
window.add_scene(scene)
window.set_active_scene("Main")
poly = Polygon([
    Position(50, 100),
    Position(150, 200),
    Position(230, 430),
    Position(350, 50)
], Color.from_hex("f57b42"))
scene.add_obj(poly)


def main():
    return True


window.display(main)
