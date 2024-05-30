from objects import Rectangle, Circle
from window import Window, Scene
from util import Color, DisplayMode, Vec

window = Window("Scenes", DisplayMode.CENTER, Vec(500, 500), 420)
left = Scene("Left", Color.from_hex("#303030"))
right = Scene("Right", Color.from_hex("#151515"))

window.add_scene(left)
window.add_scene(right)

window.set_active_scene("Left")

rect = Rectangle(Vec(250, 250), Vec(30, 50), Color.from_hex("#f57b42"))
left.add_obj(rect)
circ = Circle(Vec(250, 250), 10, Color.from_hex("#a84e32"))
right.add_obj(circ)


def main():
    if window.mouse[0] >= window.dimensions.w/2:
        window.set_active_scene("Left")
    else:
        window.set_active_scene("Right")

    rect.center = Vec(window.mouse)
    circ.position = Vec(window.mouse)
    return True


window.display(main)
