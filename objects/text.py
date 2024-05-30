from pygame import font, Surface
from util import Color, DisplayMode, Vec


class Text:
    """ Pygame Text """
    string: str
    """ Text """
    position: Vec
    """ Position of the text """
    size: int
    """ Font size of the text """
    color: Color
    """ Color of the text """
    font: str
    """ Font of the text """

    def __init__(
        self,
        string: str,
        position: Vec,
        size: int,
        color: Color,
        font_name: str = "freesansbold.ttf"
    ):
        self.string = string
        self.position = position
        self.size = size
        self.color = color
        self.font = font_name

    def display(self, screen: Surface, _: DisplayMode):
        font_render = font.Font(self.font, self.size)
        text = font_render.render(self.string, True, self.color.toRGB())
        rect = text.get_rect()
        rect.center = self.position.sep()

        screen.blit(text, rect)
