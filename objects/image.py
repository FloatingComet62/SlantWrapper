from pygame import Surface, image, transform
from util import Position, Dimension, DisplayMode


class Image:
    """ Pygame Image """
    position: Position
    """ Position of the image """
    dimension: Dimension
    """ Dimensions of the image """
    image: str
    """ Image file location """

    def __init__(self, position: Position, dimension: Dimension, img: str):
        self.position = position
        self.dimension = dimension
        self.image = img

    def display(self, screen: Surface, display_mode: DisplayMode):
        data = image.load(self.image).convert()
        img = transform.scale(data, (self.dimension.width, self.dimension.height))
        screen.blit(
            img,
            self.position.offset(
                -self.dimension.width/2 if display_mode == DisplayMode.CENTER else 0,
                -self.dimension.height/2 if display_mode == DisplayMode.CENTER else 0
            ).to_tuple()
        )
