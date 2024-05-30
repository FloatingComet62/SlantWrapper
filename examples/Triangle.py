from objects import Triangle
from window import Window, Scene
from util import Angle, Color, DisplayMode, Side, Vec

scene = Scene("Main", Color.from_hex("#303030"))
window = Window("Triangle", DisplayMode.CENTER, Vec(500, 500), 420)
window.add_scene(scene)
window.set_active_scene("Main")
tri = Triangle(
    Side(Vec(200, 200), Angle(degree=60), 100),
    Side(angle=Angle(degree=60), length=100),
    Color.from_hex("f57b42")
)
scene.add_obj(tri)


def main():
    return True


window.display(main)
