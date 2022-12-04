from typing import Union
import pygame

from objects.aaline import AALine
from objects.arc import Arc
from objects.circle import Circle
from objects.ellipse import Ellipse
from objects.line import Line
from objects.polygon import Polygon
from objects.rectangle import Rectangle
from objects.text import Text

from util import Dimension, Color


class Window:
    name: str
    dimensions: Dimension
    background_color: Color
    screen: pygame.Surface
    clock: pygame.time
    fps: int
    running: bool
    mouse: tuple[int, int]
    objs: list[Union[AALine, Arc, Circle, Ellipse, Line, Polygon, Rectangle, Text]]

    def __init__(self, name: str, dimensions: Dimension, background_color: Color, fps: int):
        self.name = name
        self.dimensions = dimensions
        self.background_color = background_color
        self.screen = pygame.display.set_mode([dimensions.width, dimensions.height])
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.running = True
        self.mouse = (0, 0)
        self.objs = []
        self.keys = []

        pygame.init()

    def display(self, main):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill(self.background_color.toRGB())
            self.mouse = pygame.mouse.get_pos()
            self.keys = pygame.key.get_pressed()
            if not main():
                break

            for obj in self.objs:
                obj.display(self.screen)

            self.clock.tick(self.fps)
            pygame.display.flip()
            pygame.display.set_caption(self.name)

    def addObj(self, obj: Union[AALine, Arc, Circle, Ellipse, Line, Polygon, Rectangle, Text]):
        self.objs.append(obj)

    def addObjs(self, objs: list[Union[AALine, Arc, Circle, Ellipse, Line, Polygon, Rectangle, Text]]):
        for obj in objs:
            self.objs.append(obj)
