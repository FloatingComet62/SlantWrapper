from pygame import Surface, image, transform
from util import DisplayMode, Vec


class Image:
    """ Pygame Image """
    position: Vec
    """ Position of the image """
    dimension: Vec
    """ Dimensions of the image """
    image: str
    """ Image file location """

    def __init__(self, position: Vec, dimension: Vec, img: str):
        self.position = position
        self.dimension = dimension
        self.image = img

    def display(self, screen: Surface, display_mode: DisplayMode):
        data = image.load(self.image).convert()
        img = transform.scale(data, (self.dimension.w, self.dimension.h))
        screen.blit(
            img,
            self.position.offset(
                -self.dimension.w/2 if display_mode == DisplayMode.CENTER else 0,
                -self.dimension.h/2 if display_mode == DisplayMode.CENTER else 0
            ).sep()
        )
