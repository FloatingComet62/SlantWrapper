import pygame
from typing import Union
from objects import AALine, Arc, Circle, Ellipse, Line, Polygon, Rectangle, Text, Image, Triangle, Square
from util import Vec, DisplayMode

Objects: Union = Union[AALine, Arc, Circle, Ellipse, Line, Polygon, Rectangle, Text, Image, Triangle, Square]

from .scene import Scene
from .handler import Handler


class Window:
    """ Pygame window manager """
    name: str
    """ Caption of the window """
    icon: pygame.Surface
    dimensions: Vec
    """ Dimensions of the window """
    screen: pygame.Surface
    clock: pygame.time
    fps: int
    """ FPS of the window """
    running: bool
    display_mode: DisplayMode
    """ DisplayMode of the window """
    mouse: tuple[int, int]
    """ Mouse coordinates """
    events: list[pygame.event.Event]
    event_handlers: list[Handler]
    keys: [pygame.key]
    """ Keys currently pressed """
    scenes: dict[str, Scene]
    active_scene: Scene

    def __init__(
            self,
            name: str,
            display_mode: DisplayMode,
            dimensions: Vec,
            fps: int = 60,
            icon: pygame.Surface = None
    ):
        self.name = name
        self.display_mode = display_mode
        self.dimensions = dimensions
        self.screen = pygame.display.set_mode([dimensions.w, dimensions.h])
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.running = True
        self.mouse = (0, 0)
        self.event_handlers = []
        self.keys = []
        self.scenes = {}

        if icon:
            pygame.display.set_icon(icon)

        def end():
            self.running = False

        self.add_event_handler(pygame.QUIT, end)

        pygame.display.set_caption(self.name)
        pygame.mixer.init(44100, 16, 2, 4096)
        pygame.init()

    def display(self, main: ()):
        """ Display handler for the window """
        while self.running:
            self._pre_display()

            if not main():
                break
            self._display_obj()

            self._post_display()

        pygame.mixer.quit()
        pygame.quit()

    def _pre_display(self):
        self.screen.fill(self.active_scene.background_color.toRGB())
        self.events = pygame.event.get()
        self.mouse = pygame.mouse.get_pos()
        self.keys = pygame.key.get_pressed()

        for event in self.events:
            for handle in self.event_handlers:
                if event.type == handle.event_type:
                    handle.handler()

    def _display_obj(self):
        for obj in self.active_scene.objs:
            if hasattr(obj, 'draw'):
                obj.draw()

            obj.display(self.screen, self.display_mode)

    def _post_display(self):
        self.clock.tick(self.fps)
        pygame.display.flip()

    def add_scene(self, scene: Scene):
        """ Register a scene for rendering """
        self.scenes.update({scene.name: scene})

    def set_active_scene(self, scene_name: str) -> bool:
        new_scene = self.scenes.get(scene_name)
        if not scene:
            return False

        self.active_scene = new_scene
        return True

    def add_event_handler(self, event_type: int, function: ()):
        """ Attach an event handler for a specific event """
        # We are not checking that if the handler is already in place to allow users to have isolated and
        # independent handlers for the same event if ever needed
        self.event_handlers.append(Handler(event_type, function))
