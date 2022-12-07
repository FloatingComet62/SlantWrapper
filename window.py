import pygame
from typing import Union
from objects import AALine, Arc, Circle, Ellipse, Line, Polygon, Rectangle, Text, Image, Triangle, Square
from util import Dimension, Color, DisplayMode

Objects: Union = Union[AALine, Arc, Circle, Ellipse, Line, Polygon, Rectangle, Text, Image, Triangle, Square]


class Window:
    name: str
    icon: pygame.Surface
    dimensions: Dimension
    background_color: Color
    screen: pygame.Surface
    clock: pygame.time
    fps: int
    running: bool
    display_mode: DisplayMode
    mouse: tuple[int, int]
    events: list[pygame.event.Event]
    event_handlers: list[tuple[int, ()]]
    keys: [pygame.key]
    objs: list[Objects]

    def __init__(
        self,
        name: str,
        display_mode: DisplayMode,
        dimensions: Dimension,
        background_color: Color = Color.from_hex("#151515"),
        fps: int = 60,
        icon: pygame.Surface = None
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
        self.event_handlers = []
        self.objs = []
        self.keys = []

        if icon:
            pygame.display.set_icon(icon)

        def handler():
            self.running = False
        self.add_event_handler(pygame.QUIT, handler)

        pygame.mixer.init(44100, 16, 2, 4096)
        pygame.init()

    def display(self, main):
        while self.running:
            self.pre_display()

            if not main():
                break
            self.display_obj()

            self.post_display()

        pygame.mixer.quit()
        pygame.quit()

    def pre_display(self):
        self.screen.fill(self.background_color.toRGB())
        self.events = pygame.event.get()
        self.mouse = pygame.mouse.get_pos()
        self.keys = pygame.key.get_pressed()

        for event in self.events:
            for handler in self.event_handlers:
                if event.type == handler[0]:
                    handler[1]()

    def display_obj(self):
        for obj in self.objs:
            if hasattr(obj, 'draw'):
                obj.draw()

            obj.display(self.screen, self.display_mode)

    def post_display(self):
        self.clock.tick(self.fps)
        pygame.display.flip()
        pygame.display.set_caption(self.name)

    def addObj(self, obj: Objects):
        self.objs.append(obj)

    def addObjs(self, objs: list[Objects]):
        for obj in objs:
            self.addObj(obj)

    def add_event_handler(self, event_type: int, handler: ()):
        # We are not checking that if the handler is already in place to allow users to have isolated and
        # independent handlers for the same event if ever needed
        self.event_handlers.append((event_type, handler))