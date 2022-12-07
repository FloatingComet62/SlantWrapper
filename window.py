from typing import Union
import pygame

from objects import AALine, Arc, Circle, Ellipse, Line, Polygon, Rectangle, Text, Image
from objects.custom import Triangle, Square

from util import Dimension, Color, DisplayMode


class Window:
    name: str
    dimensions: Dimension
    background_color: Color
    screen: pygame.Surface
    clock: pygame.time
    fps: int
    running: bool
    display_mode: DisplayMode
    mouse: tuple[int, int]
    keys: [pygame.key]
    objs: list[Union[AALine, Arc, Circle, Ellipse, Line, Polygon, Rectangle, Text, Image, Triangle, Square]]

    def __init__(
        self,
        name: str,
        display_mode: DisplayMode,
        dimensions: Dimension,
        background_color: Color,
        fps: int
    ):
        self.name = name
        self.display_mode = display_mode
        self.dimensions = dimensions
        self.background_color = background_color
        self.screen = pygame.display.set_mode([dimensions.width, dimensions.height])
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.running = True
        self.mouse = (0, 0)
        self.objs = []
        self.keys = []

        pygame.mixer.init(44100, 16, 2, 4096)
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
                if hasattr(obj, 'draw'):
                    obj.draw()

                obj.display(self.screen, self.display_mode)

            self.clock.tick(self.fps)
            pygame.display.flip()
            pygame.display.set_caption(self.name)

        pygame.mixer.quit()
        pygame.quit()

    def addObj(self, obj: Union[AALine, Arc, Circle, Ellipse, Line, Polygon, Rectangle, Text, Image, Triangle, Square]):
        self.objs.append(obj)

    def addObjs(self, objs: list[Union[AALine, Arc, Circle, Ellipse, Line, Polygon, Rectangle, Text, Image, Triangle, Square]]):
        for obj in objs:
            self.addObj(obj)
