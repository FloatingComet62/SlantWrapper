from objects import Polygon
from window import Window, Scene
from util import Color, DisplayMode, Vec

scene = Scene("Main", Color.from_hex("#303030"))
window = Window("Polygon", DisplayMode.CENTER, Vec(500, 500), 420)
window.add_scene(scene)
window.set_active_scene("Main")
poly = Polygon([
    Vec(50, 100),
    Vec(150, 200),
    Vec(230, 430),
    Vec(350, 50)
], Color.from_hex("f57b42"))
scene.add_obj(poly)


def main():
    return True


window.display(main)
