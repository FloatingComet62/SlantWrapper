from objects import Rectangle
from window import Window, Scene, Recorder
from util import Dimension, Color, DisplayMode, Position

window = Window("Window", DisplayMode.CENTER, Dimension(500, 500), 420)
scene = Scene("Main", Color.from_hex("#202020"))
window.add_scene(scene)
window.set_active_scene("Main")
obj = Rectangle(Position(250, 250), Dimension(50, 50), Color.from_hex("#eb4034"))
scene.add_obj(obj)

# window.recorder = Recorder('lmao', window.fps, window.dimensions)
# window.recorder.start()


def main():
    obj.center = Position(*window.mouse)
    return True


window.display(main)
