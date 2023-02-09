from pygame import font, Surface
from util import Position, Color, DisplayMode


class Text:
    """ Pygame Text """
    string: str
    """ Text """
    position: Position
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
        position: Position,
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
        rect.center = self.position.to_tuple()

        screen.blit(text, rect)
