from . import Objects
from util import Color


class Scene:
    name: str
    """ Name of the scene """
    background_color: Color
    """ Background color of the window """
    objs: list[Objects]

    def __init__(self, name: str, background_color: Color):
        self.name = name
        self.background_color = background_color
        self.objs = []

    def add_obj(self, obj: Objects):
        """ Register an object to be rendered """
        self.objs.append(obj)

    def add_objs(self, objs: list[Objects]):
        """ Register multiple object to be rendered """
        self.objs.extend(objs)
